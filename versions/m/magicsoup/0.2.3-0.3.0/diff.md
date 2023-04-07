# Comparing `tmp/magicsoup-0.2.3.tar.gz` & `tmp/magicsoup-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "magicsoup-0.2.3.tar", last modified: Fri Feb 17 11:04:22 2023, max compression
+gzip compressed data, was "magicsoup-0.3.0.tar", last modified: Fri Apr  7 13:39:49 2023, max compression
```

## Comparing `magicsoup-0.2.3.tar` & `magicsoup-0.3.0.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-02-17 11:04:22.092506 magicsoup-0.2.3/
--rw-rw-r--   0 marc      (1000) marc      (1003)    34888 2023-01-23 15:27:37.000000 magicsoup-0.2.3/LICENSE
--rw-rw-r--   0 marc      (1000) marc      (1003)     5379 2023-02-17 11:04:22.092506 magicsoup-0.2.3/PKG-INFO
--rw-rw-r--   0 marc      (1000) marc      (1003)     4442 2023-02-17 11:03:09.000000 magicsoup-0.2.3/README.md
--rw-rw-r--   0 marc      (1000) marc      (1003)     1092 2023-01-26 15:22:43.000000 magicsoup-0.2.3/pyproject.toml
--rw-rw-r--   0 marc      (1000) marc      (1003)       38 2023-02-17 11:04:22.092506 magicsoup-0.2.3/setup.cfg
-drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-02-17 11:04:22.088506 magicsoup-0.2.3/src/
-drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-02-17 11:04:22.088506 magicsoup-0.2.3/src/magicsoup/
--rw-rw-r--   0 marc      (1000) marc      (1003)      151 2023-02-17 11:03:52.000000 magicsoup-0.2.3/src/magicsoup/__init__.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     1108 2023-02-09 12:51:19.000000 magicsoup-0.2.3/src/magicsoup/constants.py
--rw-rw-r--   0 marc      (1000) marc      (1003)    21944 2023-02-16 21:34:11.000000 magicsoup-0.2.3/src/magicsoup/containers.py
-drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-02-17 11:04:22.092506 magicsoup-0.2.3/src/magicsoup/examples/
--rw-rw-r--   0 marc      (1000) marc      (1003)        0 2023-01-23 15:27:37.000000 magicsoup-0.2.3/src/magicsoup/examples/__init__.py
--rw-rw-r--   0 marc      (1000) marc      (1003)      833 2023-01-23 15:27:37.000000 magicsoup-0.2.3/src/magicsoup/examples/n2_fixing.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     1473 2023-01-23 15:27:37.000000 magicsoup-0.2.3/src/magicsoup/examples/reverse_krebs.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     1930 2023-02-16 21:19:27.000000 magicsoup-0.2.3/src/magicsoup/examples/wood_ljungdahl.py
--rw-rw-r--   0 marc      (1000) marc      (1003)    10969 2023-02-09 10:43:32.000000 magicsoup-0.2.3/src/magicsoup/genetics.py
--rw-rw-r--   0 marc      (1000) marc      (1003)    28443 2023-02-16 21:26:51.000000 magicsoup-0.2.3/src/magicsoup/kinetics.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     4134 2023-01-26 11:33:27.000000 magicsoup-0.2.3/src/magicsoup/mutations.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     4320 2023-01-26 11:19:53.000000 magicsoup-0.2.3/src/magicsoup/util.py
--rw-rw-r--   0 marc      (1000) marc      (1003)    31576 2023-02-16 21:24:07.000000 magicsoup-0.2.3/src/magicsoup/world.py
-drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-02-17 11:04:22.092506 magicsoup-0.2.3/src/magicsoup.egg-info/
--rw-rw-r--   0 marc      (1000) marc      (1003)     5379 2023-02-17 11:04:22.000000 magicsoup-0.2.3/src/magicsoup.egg-info/PKG-INFO
--rw-rw-r--   0 marc      (1000) marc      (1003)      647 2023-02-17 11:04:22.000000 magicsoup-0.2.3/src/magicsoup.egg-info/SOURCES.txt
--rw-rw-r--   0 marc      (1000) marc      (1003)        1 2023-02-17 11:04:22.000000 magicsoup-0.2.3/src/magicsoup.egg-info/dependency_links.txt
--rw-rw-r--   0 marc      (1000) marc      (1003)       10 2023-02-17 11:04:22.000000 magicsoup-0.2.3/src/magicsoup.egg-info/top_level.txt
-drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-02-17 11:04:22.092506 magicsoup-0.2.3/tests/
--rw-rw-r--   0 marc      (1000) marc      (1003)      710 2023-02-09 10:42:28.000000 magicsoup-0.2.3/tests/test_containers.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     6010 2023-02-09 10:42:28.000000 magicsoup-0.2.3/tests/test_genetics.py
--rw-rw-r--   0 marc      (1000) marc      (1003)    43878 2023-02-09 10:42:28.000000 magicsoup-0.2.3/tests/test_kinetics.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     1008 2023-02-09 10:42:28.000000 magicsoup-0.2.3/tests/test_util.py
--rw-rw-r--   0 marc      (1000) marc      (1003)     7180 2023-01-27 17:42:45.000000 magicsoup-0.2.3/tests/test_world.py
+drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-04-07 13:39:49.817757 magicsoup-0.3.0/
+-rw-rw-r--   0 marc      (1000) marc      (1003)    34888 2023-01-23 15:27:37.000000 magicsoup-0.3.0/LICENSE
+-rw-rw-r--   0 marc      (1000) marc      (1003)     5297 2023-04-07 13:39:49.817757 magicsoup-0.3.0/PKG-INFO
+-rw-rw-r--   0 marc      (1000) marc      (1003)     4360 2023-04-07 09:06:36.000000 magicsoup-0.3.0/README.md
+-rw-rw-r--   0 marc      (1000) marc      (1003)     1092 2023-01-26 15:22:43.000000 magicsoup-0.3.0/pyproject.toml
+-rw-rw-r--   0 marc      (1000) marc      (1003)       38 2023-04-07 13:39:49.817757 magicsoup-0.3.0/setup.cfg
+drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-04-07 13:39:49.813758 magicsoup-0.3.0/src/
+drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-04-07 13:39:49.817757 magicsoup-0.3.0/src/magicsoup/
+-rw-rw-r--   0 marc      (1000) marc      (1003)      151 2023-04-07 13:39:24.000000 magicsoup-0.3.0/src/magicsoup/__init__.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)     1108 2023-02-09 12:51:19.000000 magicsoup-0.3.0/src/magicsoup/constants.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)    23583 2023-04-07 13:24:09.000000 magicsoup-0.3.0/src/magicsoup/containers.py
+drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-04-07 13:39:49.817757 magicsoup-0.3.0/src/magicsoup/examples/
+-rw-rw-r--   0 marc      (1000) marc      (1003)        0 2023-01-23 15:27:37.000000 magicsoup-0.3.0/src/magicsoup/examples/__init__.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)      833 2023-01-23 15:27:37.000000 magicsoup-0.3.0/src/magicsoup/examples/n2_fixing.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)     1473 2023-01-23 15:27:37.000000 magicsoup-0.3.0/src/magicsoup/examples/reverse_krebs.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)     1930 2023-02-16 21:19:27.000000 magicsoup-0.3.0/src/magicsoup/examples/wood_ljungdahl.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)    11993 2023-04-06 09:43:57.000000 magicsoup-0.3.0/src/magicsoup/genetics.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)    28598 2023-04-07 13:24:41.000000 magicsoup-0.3.0/src/magicsoup/kinetics.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)     4140 2023-03-31 15:15:22.000000 magicsoup-0.3.0/src/magicsoup/mutations.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)     5288 2023-04-07 13:25:00.000000 magicsoup-0.3.0/src/magicsoup/util.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)    41788 2023-04-07 13:26:16.000000 magicsoup-0.3.0/src/magicsoup/world.py
+drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-04-07 13:39:49.817757 magicsoup-0.3.0/src/magicsoup.egg-info/
+-rw-rw-r--   0 marc      (1000) marc      (1003)     5297 2023-04-07 13:39:49.000000 magicsoup-0.3.0/src/magicsoup.egg-info/PKG-INFO
+-rw-rw-r--   0 marc      (1000) marc      (1003)      647 2023-04-07 13:39:49.000000 magicsoup-0.3.0/src/magicsoup.egg-info/SOURCES.txt
+-rw-rw-r--   0 marc      (1000) marc      (1003)        1 2023-04-07 13:39:49.000000 magicsoup-0.3.0/src/magicsoup.egg-info/dependency_links.txt
+-rw-rw-r--   0 marc      (1000) marc      (1003)       10 2023-04-07 13:39:49.000000 magicsoup-0.3.0/src/magicsoup.egg-info/top_level.txt
+drwxrwxr-x   0 marc      (1000) marc      (1003)        0 2023-04-07 13:39:49.817757 magicsoup-0.3.0/tests/
+-rw-rw-r--   0 marc      (1000) marc      (1003)      710 2023-02-09 10:42:28.000000 magicsoup-0.3.0/tests/test_containers.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)     6012 2023-04-06 09:44:07.000000 magicsoup-0.3.0/tests/test_genetics.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)    46955 2023-04-06 09:24:16.000000 magicsoup-0.3.0/tests/test_kinetics.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)     1433 2023-04-03 15:10:20.000000 magicsoup-0.3.0/tests/test_util.py
+-rw-rw-r--   0 marc      (1000) marc      (1003)    11894 2023-04-07 09:13:18.000000 magicsoup-0.3.0/tests/test_world.py
```

### Comparing `magicsoup-0.2.3/LICENSE` & `magicsoup-0.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/PKG-INFO` & `magicsoup-0.3.0/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: magicsoup
-Version: 0.2.3
+Version: 0.3.0
 Summary: Simulation for cell metabolic and transduction pathway evolution
 Author-email: Marc <schweringmarc01@gmail.com>
 Project-URL: Documentation, https://magic-soup.readthedocs.io/
 Project-URL: Homepage, https://github.com/mRcSchwering/magic-soup
 Project-URL: Bug Tracker, https://github.com/mRcSchwering/magic-soup/issues
 Classifier: Environment :: Console
 Classifier: Environment :: GPU
@@ -35,15 +35,15 @@
 
 This game simulates cell metabolic and transduction pathway evolution.
 Define a 2D world with certain molecules and reactions.
 Add a few cells and create evolutionary pressure by selectively replicating and killing them.
 Then run and see what random mutations can do.
 
 ![co2 fixing](https://raw.githubusercontent.com/mRcSchwering/magic-soup/main/docs/img/co2fix.png)
-_In [this simulation](https://github.com/mRcSchwering/luca/tree/main/experiments/e1_co2_fixing) cells were made to fix CO2 from an artificial CO2 source in the middle of the map. (A) Total molecule counts of some molecule species over time. (B) Cell map with cells in white at chosen time points._
+_In [this simulation](https://github.com/mRcSchwering/luca/tree/main/e1_co2_fixing) cells were made to fix carbon from an artificial CO2 source in the middle of the map. (A) Total molecule counts of some molecule species over time. (B) Cell map with cells in white at chosen time points._
 
 ### Installation
 
 For CPU alone you can just do:
 
 ```
 pip install magicsoup
@@ -58,15 +58,15 @@
 
 The basic building blocks of what a cell can do are defined by the world's chemistry.
 There are molecules and reactions that can convert these molecules.
 Cells can develop proteins with domains that can transport these molecules,
 catalyze the reactions, and be regulated by molecules.
 Any reaction or transport happens only if energetically favourable.
 Below, I am defining the reaction $CO2 + NADPH \rightleftharpoons formiat + NADP$.
-Each molecule species is defined with a fictional standard Gibbs free energy of formation.
+Each molecule species is defined with a energy.
 
 ```python
 import torch
 import magicsoup as ms
 
 NADPH = ms.Molecule("NADPH", 200 * 1e3)
 NADP = ms.Molecule("NADP", 100 * 1e3)
@@ -84,24 +84,24 @@
 can be powered with the energy of energetically favourable ones.
 These domains, their specifications, and how they are coupled in proteins, is all encoded in the cell's genome.
 Here, I am generating 100 cells with random genomes of 500 basepairs each and place them
 in random places on the 2D world map.
 
 ```python
 genomes = [ms.random_genome(s=500) for _ in range(100)]
-world.add_random_cells(genomes=genomes)
+world.add_cells(genomes=genomes)
 ```
 
 Cells discover new proteins by chance through mutations.
 In the function below all cells experience 1E-3 random point mutations per nucleotide.
 10% of them will be indels.
 
 ```python
 def mutate_cells():
-    mutated = ms.point_mutations(seqs=[d.genome for d in world.cells])
+    mutated = ms.point_mutations(seqs=world.genomes)
     world.update_cells(genome_idx_pairs=mutated)
 ```
 
 Evolutionary pressure can be applied by selectively killing or replicating cells.
 Here, cells have an increased chance of dying when formiat gets too low
 and an increased chance of replicating when formiat gets high.
 
@@ -114,15 +114,15 @@
     x = world.cell_molecules[:, 2]
     idxs = sample(.01 / (.01 + x))
     world.kill_cells(cell_idxs=idxs)
 
 def replicate_cells():
     x = world.cell_molecules[:, 2]
     idxs = sample(x ** 3 / (x ** 3 + 20.0 ** 3))
-    world.replicate_cells(parent_idxs=idxs)
+    world.divide_cells(cell_idxs=idxs)
 ```
 
 Finally, the simulation itself is run in a python loop by repetitively calling the different steps.
 With `world.enzymatic_activity()` chemical reactions and molecule transport
 in cells advance by one time step.
 `world.diffuse_molecules()` lets molecules on the world map diffuse and permeate through cell membranes
 (if they can) by one time step.
```

### Comparing `magicsoup-0.2.3/README.md` & `magicsoup-0.3.0/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 This game simulates cell metabolic and transduction pathway evolution.
 Define a 2D world with certain molecules and reactions.
 Add a few cells and create evolutionary pressure by selectively replicating and killing them.
 Then run and see what random mutations can do.
 
 ![co2 fixing](https://raw.githubusercontent.com/mRcSchwering/magic-soup/main/docs/img/co2fix.png)
-_In [this simulation](https://github.com/mRcSchwering/luca/tree/main/experiments/e1_co2_fixing) cells were made to fix CO2 from an artificial CO2 source in the middle of the map. (A) Total molecule counts of some molecule species over time. (B) Cell map with cells in white at chosen time points._
+_In [this simulation](https://github.com/mRcSchwering/luca/tree/main/e1_co2_fixing) cells were made to fix carbon from an artificial CO2 source in the middle of the map. (A) Total molecule counts of some molecule species over time. (B) Cell map with cells in white at chosen time points._
 
 ### Installation
 
 For CPU alone you can just do:
 
 ```
 pip install magicsoup
@@ -35,15 +35,15 @@
 
 The basic building blocks of what a cell can do are defined by the world's chemistry.
 There are molecules and reactions that can convert these molecules.
 Cells can develop proteins with domains that can transport these molecules,
 catalyze the reactions, and be regulated by molecules.
 Any reaction or transport happens only if energetically favourable.
 Below, I am defining the reaction $CO2 + NADPH \rightleftharpoons formiat + NADP$.
-Each molecule species is defined with a fictional standard Gibbs free energy of formation.
+Each molecule species is defined with a energy.
 
 ```python
 import torch
 import magicsoup as ms
 
 NADPH = ms.Molecule("NADPH", 200 * 1e3)
 NADP = ms.Molecule("NADP", 100 * 1e3)
@@ -61,24 +61,24 @@
 can be powered with the energy of energetically favourable ones.
 These domains, their specifications, and how they are coupled in proteins, is all encoded in the cell's genome.
 Here, I am generating 100 cells with random genomes of 500 basepairs each and place them
 in random places on the 2D world map.
 
 ```python
 genomes = [ms.random_genome(s=500) for _ in range(100)]
-world.add_random_cells(genomes=genomes)
+world.add_cells(genomes=genomes)
 ```
 
 Cells discover new proteins by chance through mutations.
 In the function below all cells experience 1E-3 random point mutations per nucleotide.
 10% of them will be indels.
 
 ```python
 def mutate_cells():
-    mutated = ms.point_mutations(seqs=[d.genome for d in world.cells])
+    mutated = ms.point_mutations(seqs=world.genomes)
     world.update_cells(genome_idx_pairs=mutated)
 ```
 
 Evolutionary pressure can be applied by selectively killing or replicating cells.
 Here, cells have an increased chance of dying when formiat gets too low
 and an increased chance of replicating when formiat gets high.
 
@@ -91,15 +91,15 @@
     x = world.cell_molecules[:, 2]
     idxs = sample(.01 / (.01 + x))
     world.kill_cells(cell_idxs=idxs)
 
 def replicate_cells():
     x = world.cell_molecules[:, 2]
     idxs = sample(x ** 3 / (x ** 3 + 20.0 ** 3))
-    world.replicate_cells(parent_idxs=idxs)
+    world.divide_cells(cell_idxs=idxs)
 ```
 
 Finally, the simulation itself is run in a python loop by repetitively calling the different steps.
 With `world.enzymatic_activity()` chemical reactions and molecule transport
 in cells advance by one time step.
 `world.diffuse_molecules()` lets molecules on the world map diffuse and permeate through cell membranes
 (if they can) by one time step.
```

### Comparing `magicsoup-0.2.3/pyproject.toml` & `magicsoup-0.3.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/src/magicsoup/constants.py` & `magicsoup-0.3.0/src/magicsoup/constants.py`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/src/magicsoup/containers.py` & `magicsoup-0.3.0/src/magicsoup/containers.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,20 +1,19 @@
-from typing import Optional, Union
 import warnings
 import torch
 
 
 class Molecule:
     """
     Represents a molecule species which is part of the world, can diffuse, degrade,
     and be converted into other molecules.
 
     Arguments:
         name: Used to uniquely identify this molecule species.
-        energy: In principle a standard free Gibbs energy of formation for 1 mol of this molecule species.
+        energy: Energy for 1 mol of this molecule species.
             This amount of energy is released if the molecule would be deconstructed.
             Energetically coupled in a protein it could power other activities.
         half_life: Half life of this molecule species in time steps.
             Molecules degrade by one step if you call `world.degrade_molecules()`.
             Must be > 0.0.
         diffusivity: A measure for how quick this molecule species diffuses over the molecule map during each time step.
             Molecules diffuse when calling `world.diffuse_molecules()`.
@@ -50,15 +49,15 @@
     You can setup the simulation to always call [degrade_molecules()][magicsoup.world.World.degrade_molecules] whenever a time step is finished.
     You could define one time step to equal one second and then use the real half life value for your molecule species.
 
     Molecular diffusion in the 2D molecule map happens whenever you call [diffuse_molecules()][magicsoup.world.World.diffuse_molecules].
     The molecule map is `world.molecule_map`.
     It is a 3D tensor where dimension 0 represents all molecule species of the simulation.
     They are ordered in the same way the attribute `molecules` is ordered in the [Chemistry][magicsoup.containers.Chemistry] you defined.
-    Dimension 1 represents x positions and dimension 2 y positions.
+    Dimension 1 represents x-positions and dimension 2 y-positions.
     Diffusion is implemented as a 2D convolution over the x-y tensor for each molecule species.
     This convolution has a 9x9 kernel.
     So, it alters the Moore's neighborhood of each pixel.
     How much of the center pixel's molecules are allowed to diffuse to the surrounding 8 pixels is defined by `diffusivity`.
     `diffusivity` is the ratio `a/b` when `a` is the amount of molecules diffusing to each of the 8 surrounding pixels,
     and `b` is the amount of molecules on the center pixel.
     Thus, `diffusivity=1.0` means all molecules of the center pixel are spread equally across the 9 pixels.
@@ -67,15 +66,15 @@
     Cell molecules are defined in `world.cell_molecules`.
     It is a 2D tensor where dimension 0 represents all cells and dimension 1 represents all molecule species.
     Again, molecule species are ordered in the same way the attribute `molecules` is ordered in the [Chemistry][magicsoup.containers.Chemistry] you defined.
     Dimension 0 always changes its length depedning on how cell replicate or die.
     The cell index (`cell.idx`) for any cell equals the index in `world.cell_molecules`.
     So, the amount of molecule species currently in cell with index 100 are defined in `world.cell_molecules[100]`.
     `permeability` defines how much molecules can permeate from `world.molecule_map` into `world.cell_molecules`.
-    Each cell lives on a certain pixel with x and y position.
+    Each cell lives on a certain pixel with x- and y-position.
     And although there are already molecules on this pixel, the cell has its own molecules.
     You could imagine the cell as a bag of molecule hovering over the pixel.
     `permeability` allows molecules from that pixel in the molecule map to permeate into the cell that lives on that pixel (and vice versa).
     So e.g. if cell 100 lives on pixel 12, 450
     Molecules would be allowed to move from `world.molecule_map[:, 12, 450]` to `world.cell_molecules[100, :]`.
     Again, this happens separately for every molecule species depending on its `permeability` value.
     Specifically, `permeability` is the ratio of molecules that can permeate into the cell and the molecules that stay outside.
@@ -150,16 +149,16 @@
         self.diffusivity = diffusivity
         self.permeability = permeability
         self._hash = hash(self.name)
 
     def __hash__(self) -> int:
         return self._hash
 
-    def __lt__(self, other) -> bool:
-        return hash(self) < hash(other)
+    def __lt__(self, other: "Molecule") -> bool:
+        return self.name < other.name
 
     def __eq__(self, other) -> bool:
         return hash(self) == hash(other)
 
     def __repr__(self) -> str:
         kwargs = {
             "name": self.name,
@@ -257,16 +256,14 @@
         kwargs = {
             "molecules": self.molecules,
             "reactions": self.reactions,
         }
         args = [f"{k}:{repr(d)}" for k, d in kwargs.items()]
         return f"{type(self).__name__}({','.join(args)})"
 
-    # TODO: method to print reactions in mathjax
-
 
 class CatalyticDomain:
     """
     Container holding the specification for a catalytic domain.
 
     Arguments:
         reaction: Tuple of substrate and product molecule species that describe the reaction catalyzed by this domain.
@@ -297,14 +294,33 @@
 
     def __repr__(self) -> str:
         ins = ",".join(str(d) for d in self.substrates)
         outs = ",".join(str(d) for d in self.products)
         return f"CatalyticDomain({ins}->{outs},Km={self.km:.2e},Vmax{self.vmax:.2e})"
 
 
+class CatalyticDomainFact:
+    """
+    Container for describing a catalytic domain.
+
+    Arguments:
+        reaction: Tuple of substrate and product molecule species that describe the reaction catalyzed by this domain.
+            For stoichiometric coefficients > 1, list the molecule species multiple times.
+
+    This is currently only used for [World.generate_genome()][magicsoup.world.World.generate_genome].
+    Use this factory to describe a domain that should eventually be encoded.
+    Domain factories can be stringed together into a protein in [ProteinFact][magicsoup.containers.ProteinFact]
+    """
+
+    def __init__(self, reaction: tuple[list[Molecule], list[Molecule]]):
+        substrates, products = reaction
+        self.substrates = substrates
+        self.products = products
+
+
 class TransporterDomain:
     """
     Container holding the specification for a transporter domain.
 
     Arguments:
         molecule: The molecule species which can be transported into or out of the cell by this domain.
         km: Michaelis Menten constant of the transport (in mol).
@@ -327,14 +343,30 @@
 
     def __repr__(self) -> str:
         return (
             f"TransporterDomain({self.molecule},Km={self.km:.2e},Vmax={self.vmax:.2e})"
         )
 
 
+class TransporterDomainFact:
+    """
+    Container for describing a transporter domain.
+
+    Arguments:
+        molecule: The molecule species which can be transported into or out of the cell by this domain.
+
+    This is currently only used for [World.generate_genome()][magicsoup.world.World.generate_genome].
+    Use this factory to describe a domain that should eventually be encoded.
+    Domain factories can be stringed together into a protein in [ProteinFact][magicsoup.containers.ProteinFact]
+    """
+
+    def __init__(self, molecule: Molecule):
+        self.molecule = molecule
+
+
 class RegulatoryDomain:
     """
     Container holding the specification for a regulatory domain.
 
     Arguments:
         effector: The molecule species which will be the effector molecule.
         km: Michaelis Menten constant of the transport (in mol).
@@ -366,21 +398,42 @@
 
     def __repr__(self) -> str:
         loc = "transmembrane" if self.is_transmembrane else "cytosolic"
         eff = "inhibiting" if self.is_inhibiting else "activating"
         return f"ReceptorDomain({self.effector},Km={self.km:.2e},{loc},{eff})"
 
 
-DomainType = Union[CatalyticDomain, TransporterDomain, RegulatoryDomain]
+class RegulatoryDomainFact:
+    """
+    Container for describing a regulatory domain.
+
+    Arguments:
+        effector: The molecule species which will be the effector molecule.
+        is_transmembrane: Whether this is also a transmembrane domain.
+            If true, the domain will react to extracellular molecules instead of intracellular ones.
+
+    This is currently only used for [World.generate_genome()][magicsoup.world.World.generate_genome].
+    Use this factory to describe a domain that should eventually be encoded.
+    Domain factories can be stringed together into a protein in [ProteinFact][magicsoup.containers.ProteinFact]
+    """
+
+    def __init__(self, effector: Molecule, is_transmembrane: bool):
+        self.effector = effector
+        self.is_transmembrane = is_transmembrane
+
+
+DomainType = CatalyticDomain | TransporterDomain | RegulatoryDomain
+DomainFactType = CatalyticDomainFact | TransporterDomainFact | RegulatoryDomainFact
 
 
 class Protein:
     """
     Container class to carry domains of a protein.
 
+    Arguments:
         domains: All domains of the protein
 
     In the simulation proteins for all cells exist as a set of tensors.
     This object is just a representation of a single protein.
     You shouldn't need to instantiate it.
     Protein objects are created when calling _e.g._ [get_cell()][magicsoup.world.World.get_cell].
     """
@@ -391,99 +444,104 @@
 
     def __repr__(self) -> str:
         kwargs = {"domains": self.domains}
         args = [f"{k}:{repr(d)}" for k, d in kwargs.items()]
         return f"{type(self).__name__}({','.join(args)})"
 
 
+class ProteinFact:
+    """
+    Container for describing a protein
+
+    Arguments:
+        domain_facts: List of all domains, each described by a domain factory.
+
+    This is currently only used for [World.generate_genome()][magicsoup.world.World.generate_genome].
+    Use this factory to describe a protein that should eventually be encoded.
+    Domain factories can be [CatalyticDomainFact][magicsoup.containers.CatalyticDomainFact],
+    [TransporterDomainFact][magicsoup.containers.TransporterDomainFact],
+    [RegulatoryDomainFact][magicsoup.containers.RegulatoryDomainFact].
+    """
+
+    def __init__(self, domain_facts: list[DomainFactType]):
+        self.domain_facts = domain_facts
+        self.n_domains = len(domain_facts)
+
+
 class Cell:
     """
     Object representing a cell with its environment.
 
     Arguments:
         genome: Full genome sequence of this cell.
         proteome: List of proteins this cell has.
+        int_molecules: Intracellular molecules. A tensor with one dimension that represents
+            each molecule species in the same order as defined in [Chemistry][magicsoup.containers.Chemistry].
+        ext_molecules: Extracellular molecules. A tensor with one dimension that represents
+            each molecule species in the same order as defined in [Chemistry][magicsoup.containers.Chemistry].
+            These are the molecules of the pixel the cell is currently living on.
         position: Position on the cell map.
         idx: The current index of this cell.
         label: Label which can be used to track cells. Has no effect.
         n_survived_steps: Number of time steps this cell has survived.
-        n_replications: Number of times this cell has divided itself.
+        n_divisions: Number of times this cell's ancestors already divided.
 
-    When new cells are added to [World][magicsoup.world.World] (directly or by replication),
-    they are automatically placed, their genomes are translated, and they are given an index.
-    Then they are added as an entry to a list `world.cells`.
-    So, usually you would not directly instantiate a cell.
-
-    [World][magicsoup.world.World] maintains this list of cells `world.cells` during the simulation,
-    removing killed cells and adding new or replicated cells.
-    However, for performance reasons not all attributes on this list of cell objects is always updated.
-    If you want to get a cell object with all its current attributes, use [get_cell()][magicsoup.world.World].
-
-    Apart from the initialization arguments, there are some other useful attributes:
-    - `int_molecules` Intracellular molecules.
-      A tensor with one dimension that represents each molecule species in the same order as defined in [Chemistry][magicsoup.containers.Chemistry].
-    - `ext_molecules` Extracellular molecules.
-      A tensor with one dimension that represents each molecule species in the same order as defined in [Chemistry][magicsoup.containers.Chemistry].
-      These are the molecules of the pixel the cell is currently living on.
-
-    A map of all pixels occupied by a cell exists as a tensor `world.cell_map`.
-    A map of all extracellular molecules exists as tensor `world.molecule_map`.
-    All intracellular molecules are defined as a tensor `world.cell_molecules`.
-    `world.cell_survival` and `world.cell_divisions` are tensors that define how many round each cell has survived
-    and how many times each cell was replicated.
-    For performance reasons the simulation is working with these tensors.
-    Their values are not copied into the list of cell objects `world.cells` during the simulation.
-    By default the cell objects in `world.cells` only always have a genome, proteome, and a position.
-    If you also want to know the other attributes of a specific cell use [get_cell()][magicsoup.world.World.get_cell].
-
-    During cell division this simulation has a concept of parent and child.
-    The parent is the cell that stays on the same pixel, while the child is the new cell that will occupy another pixel.
-    The child will have `n_survived_steps=0` and `n_replications=0` when it is born.
-    The parent will keep these values. Both cells will have the same genome and proteome.
-    The child will inherit the parent's `label`.
-    This way you can track cells' origin.
+    Usually, you wouldn't instantiate this object.
+    You get it when calling [get_cell()][magicsoup.world.World.get_cell] after you have added some
+    cells to a world (via [add_cells()][magicsoup.world.World.add_cells]).
+    On the `world` object all cells are actually represented as a combination of lists and tensors.
+    [get_cell()][magicsoup.world.World.get_cell] gathers all information for one cell and
+    represents it as this `Cell` object.
+
+    When a cell replicates its genome and proteome are copied.
+    Both descendants will recieve half of all molecules each.
+    Both their `n_replications` attributes are incremented.
+    The cell's `label` will be copied as well.
+    This way you can track cells' origins.
     """
 
     def __init__(
         self,
         genome: str,
         proteome: list[Protein],
+        int_molecules: torch.Tensor,
+        ext_molecules: torch.Tensor,
         position: tuple[int, int] = (-1, -1),
         idx: int = -1,
         label: str = "C",
         n_survived_steps: int = -1,
-        n_replications: int = -1,
+        n_divisions: int = -1,
     ):
         self.genome = genome
         self.proteome = proteome
         self.label = label
+        self.int_molecules = int_molecules
+        self.ext_molecules = ext_molecules
         self.position = position
         self.idx = idx
         self.n_survived_steps = n_survived_steps
-        self.n_replications = n_replications
-        self.int_molecules: Optional[torch.Tensor] = None
-        self.ext_molecules: Optional[torch.Tensor] = None
+        self.n_divisions = n_divisions
 
     def copy(self, **kwargs) -> "Cell":
         old_kwargs = {
             "genome": self.genome,
             "proteome": self.proteome,
             "position": self.position,
             "idx": self.idx,
             "label": self.label,
             "n_survived_steps": self.n_survived_steps,
-            "n_replications": self.n_replications,
+            "n_divisions": self.n_divisions,
         }
         return Cell(**{**old_kwargs, **kwargs})  # type: ignore
 
     def __repr__(self) -> str:
         kwargs = {
             "genome": self.genome,
             "proteome": self.proteome,
             "position": self.position,
             "idx": self.idx,
             "label": self.label,
             "n_survived_steps": self.n_survived_steps,
-            "n_replications": self.n_replications,
+            "n_divisions": self.n_divisions,
         }
         args = [f"{k}:{repr(d)}" for k, d in kwargs.items()]
         return f"{type(self).__name__}({','.join(args)})"
```

### Comparing `magicsoup-0.2.3/src/magicsoup/examples/n2_fixing.py` & `magicsoup-0.3.0/src/magicsoup/examples/n2_fixing.py`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/src/magicsoup/examples/reverse_krebs.py` & `magicsoup-0.3.0/src/magicsoup/examples/reverse_krebs.py`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/src/magicsoup/examples/wood_ljungdahl.py` & `magicsoup-0.3.0/src/magicsoup/examples/wood_ljungdahl.py`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/src/magicsoup/genetics.py` & `magicsoup-0.3.0/src/magicsoup/genetics.py`

 * *Files 7% similar despite different names*

```diff
@@ -84,18 +84,18 @@
     cdss: list[str],
     dom_size: int,
     dom_type_size: int,
     dom_type_map: dict[str, int],
     one_codon_map: dict[str, int],
     two_codon_map: dict[str, int],
 ) -> list[list[tuple[int, int, int, int, int]]]:
-    idx0_slice = slice(0, 2 * CODON_SIZE)
-    idx1_slice = slice(2 * CODON_SIZE, 3 * CODON_SIZE)
-    idx2_slice = slice(3 * CODON_SIZE, 4 * CODON_SIZE)
-    idx3_slice = slice(4 * CODON_SIZE, 5 * CODON_SIZE)
+    idx0_slice = slice(0, CODON_SIZE)
+    idx1_slice = slice(CODON_SIZE, 2 * CODON_SIZE)
+    idx2_slice = slice(2 * CODON_SIZE, 3 * CODON_SIZE)
+    idx3_slice = slice(3 * CODON_SIZE, 5 * CODON_SIZE)
 
     prot_doms = []
     for cds in cdss:
         doms = []
         is_useful_prot = False
 
         i = 0
@@ -106,18 +106,18 @@
 
                 # 1=catal, 2=trnsp, 3=reg
                 dom_type = dom_type_map[dom_type_seq]
                 if dom_type != 3:
                     is_useful_prot = True
 
                 dom_spec_seq = cds[i + dom_type_size : i + dom_size]
-                idx0 = two_codon_map[dom_spec_seq[idx0_slice]]
+                idx0 = one_codon_map[dom_spec_seq[idx0_slice]]
                 idx1 = one_codon_map[dom_spec_seq[idx1_slice]]
                 idx2 = one_codon_map[dom_spec_seq[idx2_slice]]
-                idx3 = one_codon_map[dom_spec_seq[idx3_slice]]
+                idx3 = two_codon_map[dom_spec_seq[idx3_slice]]
                 doms.append((dom_type, idx0, idx1, idx2, idx3))
                 i += dom_size
                 j += dom_size
             else:
                 i += CODON_SIZE
                 j += CODON_SIZE
 
@@ -171,15 +171,15 @@
 
     Arguments:
         start_codons: Start codons which start a coding sequence
         stop_codons: Stop codons which stop a coding sequence
         p_catal_dom: Chance of encountering a catalytic domain in a random nucleotide sequence.
         p_transp_dom: Chance of encountering a transporter domain in a random nucleotide sequence.
         p_reg_dom: Chance of encountering a regulatory domain in a random nucleotide sequence.
-        n_dom_type_nts: Number of nucleotides that encodes the domain type (catalytic, transporter, regulatory).
+        n_dom_type_codons: Number of codons that encode the domain type (catalytic, transporter, regulatory).
         workers: number of workers
 
     During the simulation [World][magicsoup.world.World] uses [translate_genomes][magicsoup.genetics.Genetics.translate_genomes].
     The return value of this method is a nested list of tokens.
     These tokens are then mapped into concrete domain specifications (_e.g._ Km, Vmax, reactions, ...) by [Kinetics][magicsoup.kinetics.Kinetics].
 
     Translation happens only within coding sequences (CDSs).
@@ -208,71 +208,74 @@
     def __init__(
         self,
         start_codons: tuple[str, ...] = ("TTG", "GTG", "ATG"),
         stop_codons: tuple[str, ...] = ("TGA", "TAG", "TAA"),
         p_catal_dom: float = 0.01,
         p_transp_dom: float = 0.01,
         p_reg_dom: float = 0.01,
-        n_dom_type_nts: int = 6,
+        n_dom_type_codons: int = 2,
         workers: int = 2,
     ):
         if any(len(d) != CODON_SIZE for d in start_codons):
             raise ValueError(f"Not all start codons are of length {CODON_SIZE}")
         if any(len(d) != CODON_SIZE for d in stop_codons):
             raise ValueError(f"Not all stop codons are of length {CODON_SIZE}")
         if len(set(start_codons) & set(stop_codons)) > 0:
             raise ValueError(
                 "Overlapping start and stop codons:"
                 f" {','.join(str(d) for d in set(start_codons) & set(stop_codons))}"
             )
-        if n_dom_type_nts % CODON_SIZE != 0:
-            raise ValueError(f"n_dom_type_nts should be a multiple of {CODON_SIZE}.")
-
-        self.start_codons = start_codons
-        self.stop_codons = stop_codons
-        self.workers = workers
-
-        # Domain: domain_type (catal, trnsp, reg) + specification
-        # specification: 1 x 2-codon token, 3 x 1-codon tokens
-        # Domain can start and finish with start and stop codons, so this
-        # is also the minimum CDS size
-        self.dom_size = n_dom_type_nts + 5 * CODON_SIZE
-
         if p_catal_dom + p_transp_dom + p_reg_dom > 1.0:
             raise ValueError(
                 "p_catal_dom, p_transp_dom, p_reg_dom together must not be greater 1.0"
             )
 
-        sets = nt_seqs(n_dom_type_nts)
+        self.start_codons = start_codons
+        self.stop_codons = stop_codons
+        self.workers = workers
+
+        # Domain structure:
+        # domain type definition (domain type codons)
+        # 3 x 1-codon specifications (3 simple tokens)
+        # 1 x 2-codon specification (1 complex token)
+        # a domain can begin and end with start/stop codons
+        # so min CDS size = dom_size
+        self.dom_size = (n_dom_type_codons + 5) * CODON_SIZE
+
+        # setup domain type definitions
+        # sequences including stop codons are useless, since they would terminate the CDS
+        sets = self._get_non_stop_seqs(n_codons=n_dom_type_codons)
         random.shuffle(sets)
         n = len(sets)
 
         n_catal_doms = _get_n(p=p_catal_dom, s=n, name="catalytic domains")
         n_transp_doms = _get_n(p=p_transp_dom, s=n, name="transporter domains")
         n_reg_doms = _get_n(p=p_reg_dom, s=n, name="allosteric domains")
 
         # 1=catalytic, 2=transporter, 3=regulatory
-        domain_types: dict[int, list[str]] = {}
-        domain_types[1] = sets[:n_catal_doms]
+        self.domain_types: dict[int, list[str]] = {}
+        self.domain_types[1] = sets[:n_catal_doms]
         del sets[:n_catal_doms]
-        domain_types[2] = sets[:n_transp_doms]
+        self.domain_types[2] = sets[:n_transp_doms]
         del sets[:n_transp_doms]
-        domain_types[3] = sets[:n_reg_doms]
+        self.domain_types[3] = sets[:n_reg_doms]
         del sets[:n_reg_doms]
 
-        self.domain_map = {d: k for k, v in domain_types.items() for d in v}
-
-        self.two_codon_map: dict[str, int] = {}
-        for i, seq in enumerate(nt_seqs(n=2 * CODON_SIZE)):
-            self.two_codon_map[seq] = i + 1
+        self.domain_map = {d: k for k, v in self.domain_types.items() for d in v}
 
+        # pre-mature stop codons are excluded
         self.one_codon_map: dict[str, int] = {}
-        for i, seq in enumerate(nt_seqs(n=CODON_SIZE)):
+        for i, seq in enumerate(self._get_single_codons()):
             self.one_codon_map[seq] = i + 1
 
+        # the second codon is allowed to be a stop codon
+        self.two_codon_map: dict[str, int] = {}
+        for i, seq in enumerate(self._get_double_codons()):
+            self.two_codon_map[seq] = i + 1
+
     def translate_genomes(
         self, genomes: list[str]
     ) -> list[list[list[tuple[int, int, int, int, int]]]]:
         """
         Translate all genomes into proteomes
 
         Arguments:
@@ -301,7 +304,31 @@
             for d in genomes
         ]
 
         with mp.Pool(self.workers) as pool:
             dom_seqs = pool.starmap(_translate_genome, args)
 
         return dom_seqs
+
+    def _get_non_stop_seqs(self, n_codons: int) -> list[str]:
+        all_seqs = nt_seqs(n=n_codons * CODON_SIZE)
+        seqs = []
+        for seq in all_seqs:
+            has_stop = False
+            for i in range(n_codons):
+                a = i * CODON_SIZE
+                b = (i + 1) * CODON_SIZE
+                if seq[a:b] in self.stop_codons:
+                    has_stop = True
+            if not has_stop:
+                seqs.append(seq)
+        return seqs
+
+    def _get_single_codons(self) -> list[str]:
+        seqs = nt_seqs(n=CODON_SIZE)
+        seqs = [d for d in seqs if d not in self.stop_codons]
+        return seqs
+
+    def _get_double_codons(self) -> list[str]:
+        seqs = nt_seqs(n=2 * CODON_SIZE)
+        seqs = [d for d in seqs if d[:CODON_SIZE] not in self.stop_codons]
+        return seqs
```

### Comparing `magicsoup-0.2.3/src/magicsoup/kinetics.py` & `magicsoup-0.3.0/src/magicsoup/kinetics.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,12 +1,12 @@
-from typing import Optional, Any
+from typing import Any
 import math
 import random
 import torch
-from magicsoup.constants import GAS_CONSTANT, ALL_CODONS
+from magicsoup.constants import GAS_CONSTANT
 from magicsoup.containers import (
     Molecule,
     Protein,
     CatalyticDomain,
     TransporterDomain,
     RegulatoryDomain,
     DomainType,
@@ -223,21 +223,25 @@
         km_range: The range from which to sample Michaelis Menten constants for domains (in mol).
             The sampling will happen in the log transformed intervall, so all values must be > 0.
         vmax_range: The range from which to sample maximum velocities for domains (in mol per time step).
             The sampling will happen in the log transformed intervall, so all values must be > 0.
         device: Device to use for tensors
             (see [pytorch CUDA semantics](https://pytorch.org/docs/stable/notes/cuda.html)).
             This has to be the same device that is used by `world`.
+        scalar_enc_size: Number of tokens that can be used to encode the scalars Vmax, Km, and sign.
+            This should be the output of `max(genetics.one_codon_map.values())`.
+        vector_enc_size: Number of tokens that can be used to encode the vectors for reactions and molecules.
+            This should be the output of `max(genetics.two_codon_map.values())`.
 
     There are `c` cells, `p` proteins, `s` signals.
     Signals are basically molecule species, but we have to differentiate between intra- and extracellular molecule species.
     So, there are twice as many signals as molecule species.
     The order of molecule species is always the same as in `chemistry.molecules`.
     First, all intracellular molecule species are listed, then all extracellular.
-    The order of cells is always the same as in `world.cells` and the order of proteins
+    The order of cells is always the same as in `world.genomes` and the order of proteins
     for every cell is always the same as the order of proteins in a cell object `cell.proteome`.
 
     Attributes on this class describe cell parameters:
 
     - `Km` Affinities to every signal that is processed by each protein in every cell (c, p, s).
     - `Vmax` Maximum velocities of every protein in every cell (c, p).
     - `E` Standard reaction Gibbs free energy of every protein in every cell (c, p).
@@ -248,15 +252,14 @@
 
     The main method is [integrate_signals()][magicsoup.kinetics.Kinetics].
     When calling [enzymatic_activity()][magicsoup.world.World.enzymatic_activity], a matrix `X` of signals (c, s) is prepared
     and then [integrate_signals(X)][magicsoup.kinetics.Kinetics] is called.
     Updated signals are returned and [World][magicsoup.world.World] writes them back to `world.cell_molecules` and `world.molecule_map`.
 
     Another method, which ended up here, is [set_cell_params()][magicsoup.kinetics.Kinetics.set_cell_params]
-    (and [unset_cell_params()][magicsoup.kinetics.Kinetics.unset_cell_params])
     which reads proteomes and updates cell parameters accordingly.
     This is called whenever the proteomes of some cells changed.
     Currently, this is also the main bottleneck in performance.
 
     When this class is initialized it generates the mappings from nucleotide sequences to domains by random sampling.
     These mappings are then used throughout the simulation.
     If you initialize this class again, these mappings will be different.
@@ -268,15 +271,16 @@
         self,
         molecules: list[Molecule],
         reactions: list[tuple[list[Molecule], list[Molecule]]],
         abs_temp: float = 310.0,
         km_range: tuple[float, float] = (1e-5, 1.0),
         vmax_range: tuple[float, float] = (0.01, 10.0),
         device: str = "cpu",
-        workers: int = 2,
+        scalar_enc_size: int = 64 - 3,
+        vector_enc_size: int = 4096 - 3 * 64,
     ):
         self.abs_temp = abs_temp
         self.device = device
         self.abs_temp = abs_temp
 
         self.mol_energies = self._tensor_from([d.energy for d in molecules] * 2)
         self.mol_2_mi = {d: i for i, d in enumerate(molecules)}
@@ -287,66 +291,46 @@
         self.Km = self._tensor(0, 0, n_signals)
         self.Vmax = self._tensor(0, 0)
         self.E = self._tensor(0, 0)
         self.N = self._tensor(0, 0, n_signals)
         self.A = self._tensor(0, 0, n_signals)
 
         # the domain specifications return 4 indexes
-        # idx0 is a 2-codon idx for big mappings (4096)
-        # idx1-3 are 1-codon mappings for floats (64)
-        one_codon_size = len(ALL_CODONS)
-        two_codon_size = one_codon_size**2
+        # idx 0-2 are 1-codon idxs for scalars (n=64)
+        # idx3 is a 2-codon idx for vetors (n=4096)
 
         self.km_map = _LogWeightMapFact(
-            max_token=one_codon_size,
+            max_token=scalar_enc_size,
             weight_range=km_range,
             device=device,
         )
 
         self.vmax_map = _LogWeightMapFact(
-            max_token=one_codon_size,
+            max_token=scalar_enc_size,
             weight_range=vmax_range,
             device=device,
         )
 
-        self.sign_map = _SignMapFact(max_token=one_codon_size, device=device)
+        self.sign_map = _SignMapFact(max_token=scalar_enc_size, device=device)
 
         self.reaction_map = _ReactionMapFact(
             molmap=self.mol_2_mi,
             reactions=reactions,
-            max_token=two_codon_size,
+            max_token=vector_enc_size,
             device=device,
         )
 
         self.transport_map = _TransporterMapFact(
-            n_molecules=len(molecules), max_token=two_codon_size, device=device
+            n_molecules=len(molecules), max_token=vector_enc_size, device=device
         )
 
         self.effector_map = _RegulatoryMapFact(
-            n_molecules=len(molecules), max_token=two_codon_size, device=device
+            n_molecules=len(molecules), max_token=vector_enc_size, device=device
         )
 
-    def unset_cell_params(self, cell_prots: list[tuple[int, int]]):
-        """
-        Set cell params for these proteins to 0.0.
-        This is useful for cells that lost some of their proteins.
-
-        Arguments:
-            cell_prots: List of tuples of cell indexes and protein indexes
-        """
-        # TODO: is this method still needed?
-        if len(cell_prots) == 0:
-            return
-        cells, prots = list(map(list, zip(*cell_prots)))
-        self.E[cells, prots] = 0.0
-        self.Vmax[cells, prots] = 0.0
-        self.Km[cells, prots] = 0.0
-        self.A[cells, prots] = 0.0
-        self.N[cells, prots] = 0.0
-
     def get_proteome(
         self, proteome: list[list[tuple[int, int, int, int, int]]]
     ) -> list[Protein]:
         """
         Calculate cell parameters for a single proteome and return it as
         a list of proteins
 
@@ -359,49 +343,51 @@
         """
         N_d, A_d, Km_d, Vmax_d, dom_types = self._get_proteome_tensors(
             proteomes=[proteome]
         )
 
         prots: list[Protein] = []
         for pi in range(dom_types.size(1)):
+
             doms: list[DomainType] = []
             for di in range(dom_types.size(2)):
 
                 # catalytic domain (N has positive and negative integers)
                 if dom_types[0][pi][di].item() == 1:
                     lfts: list[Molecule] = []
                     rgts: list[Molecule] = []
                     for mi, n in enumerate(N_d[0][pi][di].tolist()):
                         if n >= 1:
                             rgts.extend(([self.mi_2_mol[mi]] * int(n)))
                         elif n <= -1:
                             lfts.extend(([self.mi_2_mol[mi]] * -int(n)))
-                    mi = self.mol_2_mi[lfts[0]]
-                    doms.append(
-                        CatalyticDomain(
-                            reaction=(lfts, rgts),
-                            km=Km_d[0][pi][di][mi].item(),
-                            vmax=Vmax_d[0][pi][di].item(),
+                    if len(lfts) > 0:
+                        mi = self.mol_2_mi[lfts[0]]
+                        doms.append(
+                            CatalyticDomain(
+                                reaction=(lfts, rgts),
+                                km=Km_d[0][pi][di][mi].item(),
+                                vmax=Vmax_d[0][pi][di].item(),
+                            )
                         )
-                    )
 
                 # transporter domain (N has one +1 and one -1)
                 if dom_types[0][pi][di].item() == 2:
                     lft = int(torch.argwhere(N_d[0][pi][di] == -1)[0].item())
                     rgt = int(torch.argwhere(N_d[0][pi][di] == 1)[0].item())
                     mi = lft if lft in self.mi_2_mol else rgt
                     doms.append(
                         TransporterDomain(
                             molecule=self.mi_2_mol[mi],
                             km=Km_d[0][pi][di][mi].item(),
                             vmax=Vmax_d[0][pi][di].item(),
                         )
                     )
 
-                # regulatory domain (A has one +1)
+                # regulatory domain (A has values != 0)
                 if dom_types[0][pi][di].item() == 3:
                     mi = int(torch.argwhere(A_d[0][pi][di] != 0)[0].item())
                     if mi in self.mi_2_mol:
                         is_trnsm = False
                         mol = self.mi_2_mol[mi]
                     else:
                         is_trnsm = True
@@ -441,15 +427,19 @@
 
         # N (c, p, d, s)
         N = N_d.sum(dim=2)
         self.N[cell_idxs] = N
 
         # A (c, p, d, s)
         A = A_d.sum(dim=2)
-        self.A[cell_idxs] = A
+        # reactants on the first domain must be added as effectors
+        # if their stoichiometric number became 0 during summing up
+        delta_N = N_d[:, :, 0].clamp(max=0.0) - N.clamp(max=0.0)
+        # A += -1.0 * delta_N.clamp(max=0.0)
+        self.A[cell_idxs] = A - delta_N.clamp(max=0.0)
 
         # Km (c, p, d, s)
         Km = Km_d.nanmean(dim=2).nan_to_num(0.0)
         self.Km[cell_idxs] = Km
 
         # Vmax_d (c, p, d)
         Vmax = Vmax_d.nanmean(dim=2).nan_to_num(0.0)
@@ -465,15 +455,15 @@
 
         Arguments:
             X: Tensor of every signal in every cell (c, s). Must all be >= 0.0.
 
         Returns:
             New tensor of the same shape which represents the updated signals for every cell.
 
-        The order of cells in `X` is the same as in `world.cells`
+        The order of cells in `X` is the same as in `world.genomes`
         The order of signals is first all intracellular molecule species in the same order as `chemistry.molecules`,
         then again all molecule species in the same order but this time describing extracellular molecule species.
         The number of intracellular molecules comes from `world.cell_molecules` for any particular cell.
         The number of extracellular molecules comes from `world.molecule_map` from the pixel the particular cell currently lives on.
         """
         # adjust direction
         lKe = -self.E / self.abs_temp / GAS_CONSTANT  # (c, p)
@@ -517,15 +507,15 @@
         Copy paremeters from a list of cells to another list of cells
 
         Arguments:
             from_idxs: List of cell indexes to copy from
             to_idxs: List of cell indexes to copy to
 
         `from_idxs` and `to_idxs` must have the same length.
-        They refer to the same cell indexes as in `world.cells`.
+        They refer to the same cell indexes as in `world.genomes`.
         """
         self.Km[to_idxs] = self.Km[from_idxs]
         self.Vmax[to_idxs] = self.Vmax[from_idxs]
         self.E[to_idxs] = self.E[from_idxs]
         self.N[to_idxs] = self.N[from_idxs]
         self.A[to_idxs] = self.A[from_idxs]
 
@@ -533,51 +523,51 @@
         """
         Remove cells from cell params
 
         Arguments:
             keep: Bool tensor (c,) which is true for every cell that should not be removed
                 and false for every cell that should be removed.
 
-        `keep` must have the same length as `world.cells`.
-        The indexes on `keep` reflect the indexes in `world.cells`.
+        `keep` must have the same length as `world.genomes`.
+        The indexes on `keep` reflect the indexes in `world.genomes`.
         """
         self.Km = self.Km[keep]
         self.Vmax = self.Vmax[keep]
         self.E = self.E[keep]
         self.N = self.N[keep]
         self.A = self.A[keep]
 
     def increase_max_cells(self, by_n: int):
         """
         Increase the cell dimension of all cell parameters
 
         Arguments:
             by_n: By how many rows to increase the cell dimension
         """
-        self.Km = self._expand(t=self.Km, n=by_n, d=0)
-        self.Vmax = self._expand(t=self.Vmax, n=by_n, d=0)
-        self.E = self._expand(t=self.E, n=by_n, d=0)
-        self.N = self._expand(t=self.N, n=by_n, d=0)
-        self.A = self._expand(t=self.A, n=by_n, d=0)
+        self.Km = self._expand_c(t=self.Km, n=by_n)
+        self.Vmax = self._expand_c(t=self.Vmax, n=by_n)
+        self.E = self._expand_c(t=self.E, n=by_n)
+        self.N = self._expand_c(t=self.N, n=by_n)
+        self.A = self._expand_c(t=self.A, n=by_n)
 
     def increase_max_proteins(self, max_n: int):
         """
         Increase the protein dimension of all cell parameters
 
         Arguments:
             max_n: The maximum number of rows required in the protein dimension
         """
         n_prots = int(self.Km.shape[1])
         if max_n > n_prots:
             by_n = max_n - n_prots
-            self.Km = self._expand(t=self.Km, n=by_n, d=1)
-            self.Vmax = self._expand(t=self.Vmax, n=by_n, d=1)
-            self.E = self._expand(t=self.E, n=by_n, d=1)
-            self.N = self._expand(t=self.N, n=by_n, d=1)
-            self.A = self._expand(t=self.A, n=by_n, d=1)
+            self.Km = self._expand_p(t=self.Km, n=by_n)
+            self.Vmax = self._expand_p(t=self.Vmax, n=by_n)
+            self.E = self._expand_p(t=self.E, n=by_n)
+            self.N = self._expand_p(t=self.N, n=by_n)
+            self.A = self._expand_p(t=self.A, n=by_n)
 
     def _get_proteome_tensors(
         self, proteomes: list[list[list[tuple[int, int, int, int, int]]]]
     ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
         # separate domain specifications into different tensors
         dom_types, idxs0, idxs1, idxs2, idxs3 = self._collect_proteome_idxs(
             proteomes=proteomes
@@ -589,21 +579,25 @@
         trnsp_mask = (dom_types == 2).float()
         reg_mask = (dom_types == 3).float()
         catal_trnsp_mask = ((dom_types == 1) | (dom_types == 2)).float()
 
         # map indices of domain specifications to concrete values
         # idx0 is a 2-codon index specific for every domain type (n=4096)
         # idx1-3 are 1-codon used for the floats (n=64)
-        reacts = self.reaction_map(idxs0)  # float (c, p, d, s)
-        trnspts = self.transport_map(idxs0)  # float (c, p, d, s)
-        effectors = self.effector_map(idxs0)  # float (c, p, d, s)
-
-        Vmaxs = self.vmax_map(idxs1)  # float (c, p, d)
-        Kms = self.km_map(idxs2)  # float (c, p, d)
-        signs = self.sign_map(idxs3)  # float (c, p, d)
+
+        # map indices of domain specifications to scalars/vectors
+        # idxs 0-2 are 1-codon indexes used for scalars (n=64 (- stop codons))
+        # idx3 is a 2-codon index used for vectors (n=4096 (- stop codons))
+        Vmaxs = self.vmax_map(idxs0)  # float (c, p, d)
+        Kms = self.km_map(idxs1)  # float (c, p, d)
+        signs = self.sign_map(idxs2)  # float (c, p, d)
+
+        reacts = self.reaction_map(idxs3)  # float (c, p, d, s)
+        trnspts = self.transport_map(idxs3)  # float (c, p, d, s)
+        effectors = self.effector_map(idxs3)  # float (c, p, d, s)
 
         # N (c, p, d, s)
         N_r = torch.einsum("cpds,cpd->cpds", reacts, catal_mask)
         N_t = torch.einsum("cpds,cpd->cpds", trnspts, trnsp_mask)
         N_d = torch.einsum("cpds,cpd->cpds", (N_r + N_t), signs)
 
         # A (c, p, d, s)
@@ -707,22 +701,24 @@
     def _get_activator_activity(self, X: torch.Tensor) -> torch.Tensor:
         act_N = self.A.clamp(0)  # (c, p, s)
         act_X = torch.einsum("cps,cs->cps", act_N, X)  # (c, p, s)
         lact = torch.log(act_X + _EPS) - torch.log(self.Km + act_X + _EPS)  # (c, p, s)
         V = (lact * act_N).sum(2).exp()  # (c, p)
         return torch.where(torch.any(self.A > 0.0, dim=2), V, 1.0)  # (c, p)
 
-    def _expand(self, t: torch.Tensor, n: int, d: int) -> torch.Tensor:
-        # TODO: this might be faster and easier to read if I just make it
-        #       2 functions: expand_c and expand_p
-        pre = t.shape[slice(d)]
-        post = t.shape[slice(d + 1, t.dim())]
-        zeros = self._tensor(*pre, n, *post)
-        return torch.cat([t, zeros], dim=d)
+    def _expand_c(self, t: torch.Tensor, n: int) -> torch.Tensor:
+        size = t.size()
+        zeros = self._tensor(n, *size[1:])
+        return torch.cat([t, zeros], dim=0)
+
+    def _expand_p(self, t: torch.Tensor, n: int) -> torch.Tensor:
+        size = t.size()
+        zeros = self._tensor(size[0], n, *size[2:])
+        return torch.cat([t, zeros], dim=1)
 
-    def _tensor(self, *args, d: Optional[float] = None) -> torch.Tensor:
+    def _tensor(self, *args, d: float | None = None) -> torch.Tensor:
         if d is None:
             return torch.zeros(*args).to(self.device)
         return torch.full(tuple(args), d).to(self.device)
 
     def _tensor_from(self, d: Any) -> torch.Tensor:
         return torch.tensor(d).to(self.device)
```

### Comparing `magicsoup-0.2.3/src/magicsoup/mutations.py` & `magicsoup-0.3.0/src/magicsoup/mutations.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,33 +13,33 @@
     """
     nt = random.choice(ALL_NTS)
     return seq[:idx] + nt + seq[idx + 1 :]
 
 
 def indel(seq: str, idx: int) -> str:
     """
-    Create insertion or deletion (1:1 chance) at a specific place in a nucleotide sequence.
+    Create insertion or deletion (2:1 chance) at a specific place in a nucleotide sequence.
 
     Arguments:
         seq: nucleotide sequence
         idx: index of indel
     """
-    if random.choice([True, False]):
+    if random.choice([True, True, False]):
         return seq[:idx] + seq[idx + 1 :]
     nt = random.choice(ALL_NTS)
     return seq[:idx] + nt + seq[idx:]
 
 
 def point_mutations(
-    seqs: list[str], p: float = 1e-3, p_indel: float = 0.1
+    seqs: list[str], p: float = 1e-6, p_indel: float = 0.4
 ) -> list[tuple[str, int]]:
     """
     Add point mutations to a list of nucleotide sequences.
     Mutations are substitutions and indels.
-    If an indel occurs, there is a 1:1 chance of it being a deletion or insertion.
+    If an indel occurs, there is a 2:1 chance of it being a deletion vs insertion.
 
     Arguments:
         seqs: nucleotide sequences
         p: probability of a mutation per nucleotide
         p_indel: probability of any point mutation being a deletion or insertion
                  (inverse probability of it being a substitution)
 
@@ -77,15 +77,15 @@
             tmps[seq_i] = substitution(seq=tmps[seq_i], idx=pos_i)
 
     idxs = list(set(d[0] for d in mut_idxs))
     return [(tmps[i], i) for i in idxs]
 
 
 def recombinations(
-    seq_pairs: list[tuple[str, str]], p: float = 1e-3
+    seq_pairs: list[tuple[str, str]], p: float = 1e-6
 ) -> list[tuple[str, str, int]]:
     """
     Add random recombinations to pairs of nucleotide sequences.
     The recombination happens by creating random strand breaks in the input sequence pairs
     and randomly re-joining them.
 
     Arguments:
```

### Comparing `magicsoup-0.2.3/src/magicsoup/util.py` & `magicsoup-0.3.0/src/magicsoup/util.py`

 * *Files 14% similar despite different names*

```diff
@@ -2,14 +2,19 @@
 from itertools import product
 import string
 import random
 import math
 from magicsoup.constants import ALL_NTS
 
 
+def round_down(d: float, to: int = 3) -> int:
+    """Round down to declared integer"""
+    return math.floor(d / to) * to
+
+
 def randstr(n: int = 12) -> str:
     """
     Generate random string of length `n`.
 
     With `n=12` and the string consisting of 62 different characters,
     there's a 50% chance of encountering one collision after 5e10 draws.
     (birthday paradox)
@@ -17,17 +22,45 @@
     return "".join(
         random.choices(
             string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n
         )
     )
 
 
-def random_genome(s=100) -> str:
-    """Generate a random nucleotide sequence of length `s`"""
-    return "".join(random.choices(ALL_NTS, k=s))
+def random_genome(s=500, excl: list[str] | None = None) -> str:
+    """
+    Generate a random nucleotide sequence
+
+    Parameters:
+        s: Length of genome in nucleotides or base pairs
+        excl: Exclude certain sequences from the genome
+
+    Returns:
+        Generated genome as string
+
+    The resulting genome is a string of all possible nucleotide letters.
+    If `excl` is given, all sequences in `excl` will be removed.
+    However, these sequences might still appear in the reverse-complement of
+    the resulting genome.
+    If you also want to get rid of those, you have to also provide their
+    reverse-complement in `excl`.
+    """
+    n = s
+    out = "".join(random.choices(ALL_NTS, k=s))
+
+    if excl is not None:
+        for seq in excl:
+            out = "".join(out.split(seq))
+        while len(out) != s:
+            n = s - len(out)
+            out += random_genome(s=n)
+            for seq in excl:
+                out = "".join(out.split(seq))
+
+    return out
 
 
 def reverse_complement(seq: str) -> str:
     """Reverse-complement of a nucleotide sequence"""
     rvsd = seq[::-1]
     return (
         rvsd.replace("A", "-")
```

### Comparing `magicsoup-0.2.3/src/magicsoup/world.py` & `magicsoup-0.3.0/src/magicsoup/world.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,30 +1,37 @@
-from typing import Optional
 import random
 from itertools import product
 import math
 from io import BytesIO
 import pickle
 from pathlib import Path
 import torch
-from magicsoup.containers import Cell, Chemistry
-from magicsoup.util import moore_nghbrhd
+from magicsoup.constants import CODON_SIZE
+from magicsoup.util import moore_nghbrhd, round_down, random_genome, randstr
+from magicsoup.containers import (
+    Cell,
+    Chemistry,
+    ProteinFact,
+    CatalyticDomainFact,
+    TransporterDomainFact,
+    RegulatoryDomainFact,
+)
 from magicsoup.kinetics import Kinetics
 from magicsoup.genetics import Genetics
 
 
-def _torch_load(map_loc: Optional[str] = None):
+def _torch_load(map_loc: str | None = None):
     # Closure rather than a lambda to preserve map_loc
     return lambda b: torch.load(BytesIO(b), map_location=map_loc)
 
 
 class _CPU_Unpickler(pickle.Unpickler):
     """Inject map_location when unpickling tensor objects"""
 
-    def __init__(self, *args, map_location: Optional[str] = None, **kwargs):
+    def __init__(self, *args, map_location: str | None = None, **kwargs):
         self._map_location = map_location
         super().__init__(*args, **kwargs)
 
     def find_class(self, module: str, name: str):
         if module == "torch.storage" and name == "_load_from_bytes":
             return _torch_load(map_loc=self._map_location)
         else:
@@ -48,43 +55,47 @@
         device: Device to use for tensors (see [pytorch CUDA semantics](https://pytorch.org/docs/stable/notes/cuda.html)).
             This can be used to move most calculations to a GPU.
         workers: Number of multiprocessing workers to use.
             These are used to parallelize some calculations that can only be done on the CPU.
 
     Most attributes on this class describe the current state of molecules and cells.
     Whenever molecules are listed or represented in one dimension, they are ordered the same way as in `chemistry.molecules`.
-    Likewise, cells are always ordered the same way as in `world.cells` (see below).
-    The index of a certain cell is the index of that cell in `world.cells`.
+    Likewise, cells are always ordered the same way as in `world.genomes` (see below).
+    The index of a certain cell is the index of that cell in `world.genomes`.
     It is the same index as `cell.idx` of a cell object you retrieved with `world.get_cell()`.
-    But whenever an operation modifies the number of cells (like `world.kill_cells()` or `world.replicate_cells()`),
+    But whenever an operation modifies the number of cells (like `world.kill_cells()` or `world.divide_cells()`),
     cells get new indexes. Here are the most important attributes:
 
     Attributes:
-        cells: A list of cell objects. These cell objects hold e.g. each cell's genome and proteome.
+        genomes: A list of cell genomes. Each cell's index in this list is what is referred to as the cell index.
+            The cell index is used for the same cell in other orderings of cells (_e.g._ `labels`, `cell_divisions`, `cell_molecules`).
+        labels: List of cell labels. Cells are ordered as in `world.genomes`. Labels are strings that can be used to
+            track cell origins. When adding new cells (`world.add_cells()`) a random label is assigned to each cell.
+            If a cell divides, its descendants will have the same label.
         cell_map: Boolean 2D tensor referencing which pixels are occupied by a cell.
             Dimension 0 represents the x, dimension 1 y.
         molecule_map: Float 3D tensor describing how many molecules (in mol) of each molecule species exist on every pixel in this world.
             Dimension 0 describes the molecule species. They are in the same order as `chemistry.molecules`.
             Dimension 1 represents x, dimension 2 y.
             So, `world.molecule_map[0, 1, 2]` is number of molecules of the 0th molecule species on pixel 1, 2.
         cell_molecules: Float 2D tensor describing the number of molecules (in mol) for each molecule species in each cell.
-            Dimension 0 is the cell index. It is the same as in `world.cells` and the same as on a cell object (`cell.idx`).
+            Dimension 0 is the cell index. It is the same as in `world.genomes` and the same as on a cell object (`cell.idx`).
             Dimension 1 describes the molecule species. They are in the same order as `chemistry.molecules`.
             So, `world.cell_molecules[0, 1]` represents how many mol of the 1st molecule species the 0th cell contains.
         cell_survival: Integer 1D tensor describing how many time steps each cell survived.
             This tensor is for monitoring and doesn't have any other effect.
-            Cells are in the same as in `world.cells` and the same as on a cell object (`cell.idx`).
-        cell_divisions: Integer 1D tensor describing how many times each cell replicated.
+            Cells are in the same as in `world.genomes` and the same as on a cell object (`cell.idx`).
+        cell_divisions: Integer 1D tensor describing how many times each cell's ancestors divided.
             This tensor is for monitoring and doesn't have any other effect.
-            Cells are in the same as in `world.cells` and the same as on a cell object (`cell.idx`).
+            Cells are in the same order as in `world.genomes` and the same as on a cell object (`cell.idx`).
 
     Methods for advancing the simulation and to use during a simulation:
 
-    - [add_random_cells()][magicsoup.world.World.add_random_cells] add new cells and place them randomly on the map
-    - [replicate_cells()][magicsoup.world.World.replicate_cells] replicate existing cells
+    - [add_cells()][magicsoup.world.World.add_cells] add new cells and place them randomly on the map
+    - [divide_cells()][magicsoup.world.World.divide_cells] replicate existing cells
     - [update_cells()][magicsoup.world.World.update_cells] update existing cells if their genome has changed
     - [kill_cells()][magicsoup.world.World.kill_cells] kill existing cells
     - [move_cells()][magicsoup.world.World.move_cells] move existing cells to a random position in their Moore's neighborhood
     - [diffuse_molecules()][magicsoup.world.World.diffuse_molecules] let molecules diffuse and permeate by one time step
     - [degrade_molecules()][magicsoup.world.World.degrade_molecules] let molecules degrade by one time step
     - [increment_cell_survival()][magicsoup.world.World.increment_cell_survival] increment `world.cell_survival` by 1
     - [enzymatic_activity()][magicsoup.world.World.enzymatic_activity] let cell proteins work for one time step
@@ -101,19 +112,14 @@
 
     Finally, the `world` object carries `world.genetics`, `world.kinetics`, and `world.chemistry`
     (which is just a reference to the chemistry object that was used when initializing `world`).
     Usually, you don't need to touch them.
     But, if you want to override them or look into some details, see the docstrings of their classes for more information.
     """
 
-    # TODO: Cell positions could be maintained in a tensor only.
-    #       That way I could keep them on the GPU
-    #       Often I move them from CPU to GPU, just to add them to cell.position
-    #       But their actual use is always on the GPU: indexing on self.cell_map
-
     def __init__(
         self,
         chemistry: Chemistry,
         map_size: int = 128,
         abs_temp: float = 310.0,
         mol_map_init: str = "randn",
         start_codons: tuple[str, ...] = ("TTG", "GTG", "ATG"),
@@ -136,15 +142,16 @@
         )
 
         self.kinetics = Kinetics(
             molecules=chemistry.molecules,
             reactions=chemistry.reactions,
             abs_temp=abs_temp,
             device=self.device,
-            workers=self.workers,
+            scalar_enc_size=max(self.genetics.one_codon_map.values()),
+            vector_enc_size=max(self.genetics.two_codon_map.values()),
         )
 
         mol_degrads: list[float] = []
         diffusion: list[torch.nn.Conv2d] = []
         permeation: list[float] = []
         for mol in chemistry.molecules:
             mol_degrads.append(math.exp(-math.log(2) / mol.half_life))
@@ -159,212 +166,347 @@
         self._permeation = permeation
 
         self._nghbrhd_map = {
             (x, y): torch.tensor(moore_nghbrhd(x, y, map_size)).to(self.device)
             for x, y in product(range(map_size), range(map_size))
         }
 
-        self.cells: list[Cell] = []
+        self.n_cells = 0
+        self.genomes: list[str] = []
+        self.labels: list[str] = []
         self.cell_map: torch.Tensor = torch.zeros(map_size, map_size).to(device).bool()
+        self.cell_positions: torch.Tensor = torch.zeros(0, 2).to(device).long()
         self.cell_survival: torch.Tensor = torch.zeros(0).to(device).int()
         self.cell_divisions: torch.Tensor = torch.zeros(0).to(device).int()
         self.cell_molecules: torch.Tensor = torch.zeros(0, self.n_molecules).to(device)
         self.molecule_map: torch.Tensor = self._get_molecule_map(
             n=self.n_molecules, size=map_size, init=mol_map_init
         )
 
     def get_cell(
         self,
-        by_idx: Optional[int] = None,
-        by_position: Optional[tuple[int, int]] = None,
+        by_idx: int | None = None,
+        by_position: tuple[int, int] | None = None,
     ) -> Cell:
         """
         Get a cell with information about its current environment.
         Raises `ValueError` if cell was not found.
 
         Parameters:
             by_idx: get cell by cell index (`cell.idx`)
             by_position: get cell by position (x, y)
 
         Returns:
             The searched cell.
 
-        When accessing `world.cells` directly, the cell object will not have all information.
         For performance reasons most cell attributes are maintained in tensors during the simulation.
-        Only index, genome and position are kept up-to-date in the cell object during the simulation.
-        When you call `world.get_cell()` all missing information will be added to the object.
+        When you call `world.get_cell()` all information about a cell is gathered in one object.
+        This is a convenience function for interactive use.
+        It's not very performant.
         """
         idx = -1
         if by_idx is not None:
             idx = by_idx
         if by_position is not None:
-            cell_positions = [d.position for d in self.cells]
-            try:
-                idx = cell_positions.index(by_position)
-            except ValueError as err:
-                raise ValueError(f"Cell at {by_position} not found") from err
-
-        cell = self.cells[idx]
-        cell.int_molecules = self.cell_molecules[idx, :]
-        cell.ext_molecules = self.molecule_map[:, cell.position[0], cell.position[1]]
-        cell.n_survived_steps = int(self.cell_survival[idx].item())
-        cell.n_replications = int(self.cell_divisions[idx].item())
+            pos = torch.tensor(by_position)
+            mask = (self.cell_positions == pos).all(dim=1)
+            idxs = torch.argwhere(mask).flatten().tolist()
+            if len(idxs) == 0:
+                raise ValueError(f"Cell at {by_position} not found")
+            idx = idxs[0]
+
+        genome = self.genomes[idx]
+        (cdss,) = self.genetics.translate_genomes(genomes=[genome])
+        pos = self.cell_positions[idx]
+
+        return Cell(
+            idx=idx,
+            genome=genome,
+            proteome=self.kinetics.get_proteome(proteome=cdss),
+            position=tuple(pos.tolist()),  # type: ignore
+            int_molecules=self.cell_molecules[idx, :],
+            ext_molecules=self.molecule_map[:, pos[0], pos[1]],
+            label=self.labels[idx],
+            n_survived_steps=int(self.cell_survival[idx].item()),
+            n_divisions=int(self.cell_divisions[idx].item()),
+        )
+
+    def generate_genome(self, proteome: list[ProteinFact], size: int = 500) -> str:
+        """
+        Generate a random genome that encodes a desired proteome
+
+        Arguments:
+            proteome: list of [ProteinFactories][magicsoup.containers.ProteinFact] that describe each protein
+            size: total length of the resulting genome (in nucleotides/base pairs)
+
+        Returns:
+            Genome as string of nucleotide letters
 
-        (cdss,) = self.genetics.translate_genomes(genomes=[cell.genome])
-        cell.proteome = self.kinetics.get_proteome(proteome=cdss)
+        This function uses the mappings from [Genetics][magicsoup.genetics.Genetics]
+        and [Kinetics][magicsoup.kinetics.Kinetics] in reverse to generate a genome.
+        So, the same [World][magicsoup.world.World] object should be used when running a simulation
+        with these generated genomes.
+        Some domain specifications are given in `proteome`, some (such as the kinetics parameters)
+        will be assigned randomly.
+
+        Note, this function is neither particularly intelligent nor performant.
+        It can happen that some proteins of the desired proteome are missing.
+        This can happen for example when a stop codon appear accidentally inside a domain definition,
+        terminating this protein pre-maturely.
+        At the same time, the resulting genome can also include proteins that were not defined.
+        E.g. the reverse-complement can encode additional proteins.
+        This function tries to avoid this, but is not capable of avoiding it all the time.
+        """
+        all_mols = self.chemistry.molecules
+        all_reacts = self.chemistry.reactions
+        dom_size = self.genetics.dom_size
+
+        req_nts = 0
+        reacts = [(tuple(sorted(s)), tuple(sorted(p))) for s, p in all_reacts]
+        fwd_bwd_reacts = reacts + [(p, s) for s, p in reacts]
+
+        for pi, prot in enumerate(proteome):
+            req_nts += 2 * CODON_SIZE + dom_size * prot.n_domains
+            for dom in prot.domain_facts:
+                if isinstance(dom, TransporterDomainFact):
+                    if dom.molecule not in all_mols:
+                        raise ValueError(
+                            f"ProteinFact {pi} has this molecule defined: {dom.molecule.name}."
+                            " This world's chemistry doesn't define this molecule species."
+                        )
+                if isinstance(dom, RegulatoryDomainFact):
+                    if dom.effector not in all_mols:
+                        raise ValueError(
+                            f"ProteinFact {pi} has this effector defined: {dom.effector.name}."
+                            " This world's chemistry doesn't define this molecule species."
+                        )
+                if isinstance(dom, CatalyticDomainFact):
+                    subs = sorted(dom.substrates)
+                    prods = sorted(dom.products)
+                    react = (tuple(subs), tuple(prods))
+                    if react not in fwd_bwd_reacts:
+                        reactstr = f"{' + '.join(d.name for d in subs)} <-> {' + '.join(d.name for d in prods)}"
+                        raise ValueError(
+                            f"ProteinFact {pi} has this reaction defined: {reactstr}."
+                            " This world's chemistry doesn't define this reaction."
+                        )
+
+        if req_nts > size:
+            raise ValueError(
+                "Genome size too small."
+                f" The given proteome would require at least {req_nts} nucleotides."
+                f" But the given genome size is size={size}."
+            )
+
+        cdss = self._get_genome_sequences(proteome=proteome)
+        n_p_pads = len(cdss) + 1
+        n_d_pads = sum(len(d) + 1 for d in cdss)
+
+        n_pad_nts = size - req_nts
+        pad_size = n_pad_nts / (n_p_pads * 0.7 + n_d_pads * 0.3)
+        d_pad_size = round_down(pad_size * 0.3, to=3)
+        d_pad_total = n_d_pads * d_pad_size
+        p_pad_size = round_down((n_pad_nts - d_pad_total) / n_p_pads, to=1)
+        p_pad_total = n_p_pads * p_pad_size
+        remaining_nts = n_pad_nts - d_pad_total - p_pad_total
+
+        excl_cdss = list(self.genetics.start_codons) + list(self.genetics.stop_codons)
+        excl_doms = excl_cdss + list(self.genetics.domain_map)
+        p_pads = [random_genome(s=p_pad_size, excl=excl_cdss) for _ in range(n_p_pads)]
+        d_pads = [random_genome(s=d_pad_size, excl=excl_doms) for _ in range(n_d_pads)]
+        tail = random_genome(s=remaining_nts, excl=excl_cdss)
+
+        parts: list[str] = []
+        for cds in cdss:
+            parts.append(p_pads.pop())
+            parts.append(random.choice(self.genetics.start_codons))
+            for dom_seq in cds:
+                parts.append(d_pads.pop())
+                parts.append(dom_seq)
+            parts.append(d_pads.pop())
+            parts.append(random.choice(self.genetics.stop_codons))
+        parts.append(p_pads.pop())
+        parts.append(tail)
 
-        return cell
+        return "".join(parts)
 
-    def add_random_cells(self, genomes: list[str]) -> list[int]:
+    def add_cells(self, genomes: list[str]) -> list[int]:
         """
-        Create new cells and place them on randomly on the map.
+        Create new cells and place them randomly on the map.
         All lists and tensors that reference cells will be updated.
 
         Parameters:
             genomes: List of genomes of the newly added cells
 
         Returns:
             The indexes of successfully added cells.
 
         Each cell will be placed randomly on the map and receive half the molecules of the pixel where it was added.
         If there are less pixels left on the cell map than cells you want to add,
         only the remaining pixels will be filled with new cells.
+        Each cell will also receive a random label.
         """
         genomes = [d for d in genomes if len(d) > 0]
         n_new_cells = len(genomes)
         if n_new_cells == 0:
             return []
 
-        xs, ys = self._find_free_random_positions(n_cells=n_new_cells)
-        n_avail_pos = len(xs)
+        free_pos = self._find_free_random_positions(n_cells=n_new_cells)
+        n_avail_pos = free_pos.size(0)
         if n_avail_pos == 0:
             return []
 
         if n_avail_pos < n_new_cells:
             n_new_cells = n_avail_pos
             random.shuffle(genomes)
             genomes = genomes[:n_new_cells]
 
         proteomes = self.genetics.translate_genomes(genomes=genomes)
-        proteomes = [d for d in proteomes if len(d) > 0]
-        n_new_cells = len(proteomes)
+
+        new_genomes = []
+        new_proteomes = []
+        new_labels = []
+        for proteome, genome in zip(proteomes, genomes):
+            if len(proteome) > 0:
+                new_genomes.append(genome)
+                new_proteomes.append(proteome)
+                new_labels.append(randstr(n=12))
+
+        n_new_cells = len(new_genomes)
         if n_new_cells == 0:
             return []
 
-        xs = xs[:n_new_cells]
-        ys = ys[:n_new_cells]
-
-        n_cells = len(self.cells)
-        new_idxs = list(range(n_cells, n_cells + n_new_cells))
-        for cell_i, genome, x, y in zip(new_idxs, genomes, xs, ys):
-            cell = Cell(idx=cell_i, genome=genome, proteome=[], position=(x, y))
-            self.cells.append(cell)
-
-        self.cell_survival = self._expand(t=self.cell_survival, n=n_new_cells, d=0)
-        self.cell_divisions = self._expand(t=self.cell_divisions, n=n_new_cells, d=0)
-        self.cell_molecules = self._expand(t=self.cell_molecules, n=n_new_cells, d=0)
+        new_pos = free_pos[:n_new_cells]
+        new_idxs = list(range(self.n_cells, self.n_cells + n_new_cells))
+        self.n_cells += n_new_cells
+        self.genomes.extend(new_genomes)
+        self.labels.extend(new_labels)
+
+        self.cell_survival = self._expand_c(t=self.cell_survival, n=n_new_cells)
+        self.cell_positions = self._expand_c(t=self.cell_positions, n=n_new_cells)
+        self.cell_divisions = self._expand_c(t=self.cell_divisions, n=n_new_cells)
+        self.cell_molecules = self._expand_c(t=self.cell_molecules, n=n_new_cells)
 
-        n_max_prots = max(len(d) for d in proteomes)
+        n_max_prots = max(len(d) for d in new_proteomes)
         self.kinetics.increase_max_proteins(max_n=n_max_prots)
         self.kinetics.increase_max_cells(by_n=n_new_cells)
-        self.kinetics.set_cell_params(cell_idxs=new_idxs, proteomes=proteomes)
+        self.kinetics.set_cell_params(cell_idxs=new_idxs, proteomes=new_proteomes)
 
         # occupy positions
+        xs = new_pos[:, 0]
+        ys = new_pos[:, 1]
         self.cell_map[xs, ys] = True
+        self.cell_positions[new_idxs] = new_pos
 
         # cell is picking up half the molecules of the pxl it is born on
         pickup = self.molecule_map[:, xs, ys] * 0.5
         self.cell_molecules[new_idxs, :] += pickup.T
         self.molecule_map[:, xs, ys] -= pickup
 
         return new_idxs
 
-    def replicate_cells(self, parent_idxs: list[int]) -> list[tuple[int, int]]:
+    def divide_cells(self, cell_idxs: list[int]) -> list[tuple[int, int]]:
         """
-        Bring cells to replicate.
+        Bring cells to divide.
         All lists and tensors that reference cells will be updated.
 
         Parameters:
-            parent_idxs: Cell indexes of the cells that should replicate.
+            cell_idxs: Cell indexes of the cells that should divide.
 
         Returns:
-            A list of tuples of parent and child cell indexes for all successfully replicated cells.
-
-        In this simulation the cell that was brought to replicate is the parent.
-        It still lives on the same pixel.
-        The child is the cell that was newly added next to the parent.
-        The child will start with 0 survived steps and 0 replications,
-        while the parent keeps its number of survived steps and increments its number of replications.
-        Half the parent's molecules will be given to the child.
+            A list of tuples of descendant cell indexes.
 
-        Each child will be placed randomly next to its parent (Moore's neighborhood).
-        If every pixel in the parent's Moore's neighborhood is taken the cell will not replicate.
+        Each cell divides by creating a clone of itself on a random pixel next to itself (Moore's neighborhood).
+        If every pixel in its Moore's neighborhood is taken, it will not be able to divide.
+        Both, the original ancestor cell and the newly placed cell will become the descendants.
+        They will have the same genome, proteome, survived steps, and label.
+        Both descendants share all molecules equally.
+        So each descendant cell will get half the molecules of the ancestor cell.
+
+        Both descendants will share the same number of divisions.
+        It is incremented by 1 for both cells.
+        So, _e.g._ if a cell with `n_divisions=2` divides, its descendants both have `n_divisions=3`.
+
+        Of the list of descendant index tuples,
+        the first descendant in each tuple is the cell that still lives on the same pixel.
+        The second descendant in that tuple is the cell that was newly created.
         """
-        if len(parent_idxs) == 0:
+        if len(cell_idxs) == 0:
             return []
 
-        succ_parent_idxs, child_idxs = self._replicate_cells_as_possible(
-            parent_idxs=parent_idxs
-        )
-        self.cell_divisions[succ_parent_idxs] += 1
+        (
+            parent_idxs,
+            child_idxs,
+            child_pos,
+        ) = self._divide_cells_as_possible(parent_idxs=cell_idxs)
 
         n_new_cells = len(child_idxs)
         if n_new_cells == 0:
             return []
 
-        self.cell_survival = self._expand(t=self.cell_survival, n=n_new_cells, d=0)
-        self.cell_divisions = self._expand(t=self.cell_divisions, n=n_new_cells, d=0)
-        self.cell_molecules = self._expand(t=self.cell_molecules, n=n_new_cells, d=0)
+        self.n_cells += n_new_cells
+
+        self.cell_survival = self._expand_c(t=self.cell_survival, n=n_new_cells)
+        self.cell_positions = self._expand_c(t=self.cell_positions, n=n_new_cells)
+        self.cell_divisions = self._expand_c(t=self.cell_divisions, n=n_new_cells)
+        self.cell_molecules = self._expand_c(t=self.cell_molecules, n=n_new_cells)
         self.kinetics.increase_max_cells(by_n=n_new_cells)
-        self.kinetics.copy_cell_params(from_idxs=succ_parent_idxs, to_idxs=child_idxs)
+        self.kinetics.copy_cell_params(from_idxs=parent_idxs, to_idxs=child_idxs)
 
-        # cell shares molecules with parent
-        self.cell_molecules[child_idxs] = self.cell_molecules[succ_parent_idxs]
-        self.cell_molecules[child_idxs + succ_parent_idxs] *= 0.5
+        # position new cells
+        # cell_map was already set in loop before
+        self.cell_positions[child_idxs] = torch.stack(child_pos)
+
+        # cells share molecules and increment cell divisions
+        descendant_idxs = parent_idxs + child_idxs
+        self.cell_molecules[child_idxs] = self.cell_molecules[parent_idxs]
+        self.cell_molecules[descendant_idxs] *= 0.5
+        self.cell_divisions[descendant_idxs] += 1
 
-        return list(zip(succ_parent_idxs, child_idxs))
+        return list(zip(parent_idxs, child_idxs))
 
     def update_cells(self, genome_idx_pairs: list[tuple[str, int]]):
         """
         Update existing cells with new genomes.
 
         Parameters:
             genome_idx_pairs: List of tuples of genomes and cell indexes
 
         The indexes refer to the index of each cell that is changed.
         The genomes refer to the genome of each cell that is changed.
-        `world.cells` will be updated with new genomes and proteomes.
         """
         if len(genome_idx_pairs) == 0:
             return
 
         kill_idxs = []
         transl_idxs = []
-        genomes = []
+        transl_genomes = []
         for genome, idx in genome_idx_pairs:
             if len(genome) > 0:
-                genomes.append(genome)
+                transl_genomes.append(genome)
                 transl_idxs.append(idx)
             else:
                 kill_idxs.append(idx)
 
-        proteomes = self.genetics.translate_genomes(genomes=genomes)
+        proteomes = self.genetics.translate_genomes(genomes=transl_genomes)
 
         set_idxs = []
         set_proteomes = []
         for proteome, idx in zip(proteomes, transl_idxs):
             if len(proteome) > 0:
                 set_proteomes.append(proteome)
                 set_idxs.append(idx)
             else:
                 kill_idxs.append(idx)
 
-        max_prots = max(len(d) for d in set_proteomes)
-        self.kinetics.increase_max_proteins(max_n=max_prots)
-        self.kinetics.set_cell_params(cell_idxs=set_idxs, proteomes=set_proteomes)
+        if len(set_proteomes) > 0:
+            max_prots = max(len(d) for d in set_proteomes)
+            self.kinetics.increase_max_proteins(max_n=max_prots)
+            self.kinetics.set_cell_params(cell_idxs=set_idxs, proteomes=set_proteomes)
+
         self.kill_cells(cell_idxs=kill_idxs)
 
     def kill_cells(self, cell_idxs: list[int]):
         """
         Remove existing cells.
         All lists and tensors referencing cells will be updated.
 
@@ -374,64 +516,78 @@
         Cells that are killed dump their molecule contents onto the pixel they used to live on.
 
         Cells will be removed from all lists and tensors that reference cells.
         Thus, after killing cells the index of some living cells will be updated.
         E.g. if there are 10 cells and you kill the cell with index 8 (the 9th cell),
         the cell that used to have index 9 (10th cell) will now have index 9.
         """
-        if len(cell_idxs) == 0:
+        n_killed_cells = len(cell_idxs)
+        if n_killed_cells == 0:
             return
 
-        xs, ys = list(map(list, zip(*[self.cells[i].position for i in cell_idxs])))
+        xs = self.cell_positions[cell_idxs, 0]
+        ys = self.cell_positions[cell_idxs, 1]
         self.cell_map[xs, ys] = False
 
         spillout = self.cell_molecules[cell_idxs, :]
         self.molecule_map[:, xs, ys] += spillout.T
 
-        keep = torch.ones(self.cell_survival.size(0), dtype=torch.bool).to(self.device)
+        n_cells = self.cell_survival.size(0)
+        keep = torch.ones(n_cells, dtype=torch.bool).to(self.device)
         keep[cell_idxs] = False
         self.cell_survival = self.cell_survival[keep]
+        self.cell_positions = self.cell_positions[keep]
         self.cell_divisions = self.cell_divisions[keep]
         self.cell_molecules = self.cell_molecules[keep]
         self.kinetics.remove_cell_params(keep=keep)
 
-        new_idx = 0
-        new_cells = []
-        for old_idx, cell in enumerate(self.cells):
-            if old_idx not in cell_idxs:
-                cell.idx = new_idx
-                new_idx += 1
-                new_cells.append(cell)
-        self.cells = new_cells
+        for idx in sorted(cell_idxs, reverse=True):
+            self.genomes.pop(idx)
+            self.labels.pop(idx)
+
+        self.n_cells -= n_killed_cells
 
     def move_cells(self, cell_idxs: list[int]):
         """
         Move cells to a random position in their Moore's neighborhood.
         If every pixel in the cells' Moore neighborhood is taken the cell will not be moved.
         `world.cell_map` will be updated.
 
         Parameters:
             cell_idxs: Indexes of cells that should be moved
         """
         if len(cell_idxs) == 0:
             return
 
-        cells = [self.cells[i] for i in cell_idxs]
-        self._randomly_move_cells(cells=cells)
+        for cell_idx in cell_idxs:
+            old_pos = self.cell_positions[cell_idx]
+            nghbrhd = self._nghbrhd_map[tuple(old_pos.tolist())]  # type: ignore
+            pxls = nghbrhd[~self.cell_map[nghbrhd[:, 0], nghbrhd[:, 1]]]
+            n = pxls.size(0)
+
+            if n == 0:
+                continue
+
+            # move cells
+            new_pos = pxls[random.randint(0, n - 1)]
+            self.cell_map[old_pos[0], old_pos[1]] = False
+            self.cell_map[new_pos[0], new_pos[1]] = True
+            self.cell_positions[cell_idx] = new_pos
 
     def enzymatic_activity(self):
         """
         Catalyze reactions for one time step.
         This includes molecule transport into or out of the cell.
         `world.molecule_map` and `world.cell_molecules` are updated.
         """
-        if len(self.cells) == 0:
+        if self.n_cells == 0:
             return
 
-        xs, ys = list(map(list, zip(*[d.position for d in self.cells])))
+        xs = self.cell_positions[:, 0]
+        ys = self.cell_positions[:, 1]
         X = torch.cat([self.cell_molecules, self.molecule_map[:, xs, ys].T], dim=1)
         X = self.kinetics.integrate_signals(X=X)
 
         self.molecule_map[:, xs, ys] = X[:, self._ext_mol_idxs].T
         self.cell_molecules = X[:, self._int_mol_idxs]
 
     @torch.no_grad()
@@ -454,18 +610,19 @@
             total_after = self.molecule_map[mol_i].sum()
 
             # attempt to fix the problem that convolusion makes a small amount of
             # molecules appear or disappear (I think because floating point)
             self.molecule_map[mol_i] += (total_before - total_after) / n_pxls
             self.molecule_map[mol_i] = self.molecule_map[mol_i].clamp(0.0)
 
-        if len(self.cells) == 0:
+        if self.n_cells == 0:
             return
 
-        xs, ys = list(map(list, zip(*[d.position for d in self.cells])))
+        xs = self.cell_positions[:, 0]
+        ys = self.cell_positions[:, 1]
         X = torch.cat([self.cell_molecules, self.molecule_map[:, xs, ys].T], dim=1)
 
         for mol_i, permeate in enumerate(self._permeation):
             d_int = X[:, mol_i] * permeate
             d_ext = X[:, mol_i + self.n_molecules] * permeate
             X[:, mol_i] += d_ext - d_int
             X[:, mol_i + self.n_molecules] += d_int - d_ext
@@ -486,16 +643,15 @@
             self.cell_molecules[:, mol_i] *= degrad
 
     def increment_cell_survival(self):
         """
         Increment `world.cell_survival` by 1.
         This is for monitoring and doesn't have any other effect.
         """
-        idxs = list(range(len(self.cells)))
-        self.cell_survival[idxs] += 1
+        self.cell_survival += 1
 
     def save(self, rundir: Path, name: str = "world.pkl"):
         """
         Write whole world object to pickle file
 
         Parameters:
             rundir: Directory of the pickle file
@@ -508,15 +664,15 @@
         """
         rundir.mkdir(parents=True, exist_ok=True)
         with open(rundir / name, "wb") as fh:
             pickle.dump(self, fh)
 
     @classmethod
     def from_file(
-        self, rundir: Path, name: str = "world.pkl", device: Optional[str] = None
+        self, rundir: Path, name: str = "world.pkl", device: str | None = None
     ) -> "World":
         """
         Restore previously saved world from pickle file.
         The file had to be saved with [save()][magicsoup.world.World.save].
 
         Parameters:
             rundir: Directory of the pickle file
@@ -546,28 +702,29 @@
         Then, `world.save_state()` can be used to save different states of that world object.
         """
         statedir.mkdir(parents=True, exist_ok=True)
         torch.save(self.cell_molecules, statedir / "cell_molecules.pt")
         torch.save(self.cell_map, statedir / "cell_map.pt")
         torch.save(self.molecule_map, statedir / "molecule_map.pt")
         torch.save(self.cell_survival, statedir / "cell_survival.pt")
+        torch.save(self.cell_positions, statedir / "cell_positions.pt")
         torch.save(self.cell_divisions, statedir / "cell_divisions.pt")
 
+        lines: list[str] = []
+        for idx, (genome, label) in enumerate(zip(self.genomes, self.labels)):
+            lines.append(f">{idx} {label}\n{genome}")
+
         with open(statedir / "cells.fasta", "w", encoding="utf-8") as fh:
-            lines = [
-                f">{d.idx} {d.label} ({d.position[0]},{d.position[1]})\n{d.genome}"
-                for d in self.cells
-            ]
             fh.write("\n".join(lines))
 
     def load_state(
         self,
         statedir: Path,
         ignore_cell_params: bool = False,
-        device: Optional[str] = None,
+        device: str | None = None,
     ):
         """
         Load a saved world state.
         The state had to be saved with [save_state()][magicsoup.world.World.save_state] previously.
 
         Parameters:
             statedir: Directory that contains all files of that state
@@ -585,95 +742,166 @@
         self.cell_map = torch.load(statedir / "cell_map.pt", map_location=device).bool()
         self.molecule_map = torch.load(
             statedir / "molecule_map.pt", map_location=device
         )
         self.cell_survival = torch.load(
             statedir / "cell_survival.pt", map_location=device
         ).int()
+        self.cell_positions = torch.load(
+            statedir / "cell_positions.pt", map_location=device
+        ).int()
         self.cell_divisions = torch.load(
             statedir / "cell_divisions.pt", map_location=device
         ).int()
 
         with open(statedir / "cells.fasta", "r", encoding="utf-8") as fh:
             text: str = fh.read()
             entries = [d.strip() for d in text.split(">") if len(d.strip()) > 0]
 
         genome_idx_pairs: list[tuple[str, int]] = []
-        self.cells = []
         for entry in entries:
             descr, seq = entry.split("\n")
-            names_part, pos_part = descr.split("(")
-            x, y = pos_part.split(")")[0].split(",")
-            names = names_part.split()
+            names = descr.split()
             idx = int(names[0].strip())
-            pos = (int(x.strip()), int(y.strip()))
             label = names[1].strip() if len(names) > 1 else ""
-            cell = Cell(idx=idx, label=label, genome=seq, proteome=[], position=pos)
-            self.cells.append(cell)
+            self.genomes.append(seq)
+            self.labels.append(label)
             genome_idx_pairs.append((seq, idx))
 
+        self.n_cells = len(genome_idx_pairs)
+
         if ignore_cell_params:
             self.update_cells(genome_idx_pairs=genome_idx_pairs)
 
-    def _randomly_move_cells(self, cells: list[Cell]):
-        for cell in cells:
-            x, y = cell.position
-            nghbrhd = self._nghbrhd_map[(x, y)]
-            pxls = nghbrhd[~self.cell_map[nghbrhd[:, 0], nghbrhd[:, 1]]]
-            n = pxls.size(0)
-
-            if n == 0:
-                continue
-
-            # move cells
-            new_x, new_y = pxls[random.randint(0, n - 1)].tolist()
-            self.cell_map[x, y] = False
-            self.cell_map[new_x, new_y] = True
-            cell.position = (new_x, new_y)
-
-    def _replicate_cells_as_possible(
+    def _divide_cells_as_possible(
         self, parent_idxs: list[int]
-    ) -> tuple[list[int], list[int]]:
-        idx = len(self.cells)
+    ) -> tuple[list[int], list[int], list[torch.Tensor]]:
+        run_idx = self.n_cells
         child_idxs = []
         successful_parent_idxs = []
+        new_positions = []
         for parent_idx in parent_idxs:
-            parent = self.cells[parent_idx]
-
-            x, y = parent.position
-            nghbrhd = self._nghbrhd_map[(x, y)]
+            pos = self.cell_positions[parent_idx]
+            nghbrhd = self._nghbrhd_map[tuple(pos.tolist())]  # type:ignore
             pxls = nghbrhd[~self.cell_map[nghbrhd[:, 0], nghbrhd[:, 1]]]
-            n = pxls.size(0)
 
+            n = pxls.size(0)
             if n == 0:
                 continue
 
-            new_x, new_y = pxls[random.randint(0, n - 1)].tolist()
-            self.cell_map[new_x, new_y] = True
+            new_pos = pxls[random.randint(0, n - 1)]
+            new_positions.append(new_pos)
+
+            # immediately set, so that it is already
+            # True for the next iteration
+            self.cell_map[new_pos[0], new_pos[1]] = True
+
+            self.genomes.append(self.genomes[parent_idx])
+            self.labels.append(self.labels[parent_idx])
 
-            child = parent.copy(idx=idx, position=(new_x, new_y), n_survived_steps=0)
             successful_parent_idxs.append(parent_idx)
-            child_idxs.append(idx)
-            self.cells.append(child)
-            idx += 1
+            child_idxs.append(run_idx)
+            run_idx += 1
 
-        return successful_parent_idxs, child_idxs
+        return successful_parent_idxs, child_idxs, new_positions
 
-    def _find_free_random_positions(self, n_cells: int) -> tuple[list[int], list[int]]:
+    def _find_free_random_positions(self, n_cells: int) -> torch.Tensor:
         # available spots on map
         pxls = torch.argwhere(~self.cell_map)
         n_pxls = pxls.size(0)
         if n_cells > n_pxls:
             n_cells = n_pxls
 
         # place cells on map
         idxs = random.sample(range(n_pxls), k=n_cells)
         chosen = pxls[idxs]
-        xs, ys = chosen.T.tolist()
-        return xs, ys
+        return chosen
+
+    def _get_genome_sequences(self, proteome: list[ProteinFact]) -> list[list[str]]:
+        proteome = proteome.copy()
+        random.shuffle(proteome)
+
+        all_mols = self.chemistry.molecules
+        all_reacts = self.chemistry.reactions
+        stops = list(self.genetics.start_codons)
+
+        dom_type_map = self.genetics.domain_types
+        one_codon_map = {v: k for k, v in self.genetics.one_codon_map.items()}
+        two_codon_map = {v: k for k, v in self.genetics.two_codon_map.items()}
+
+        react_map = {}
+        for subs, prods in all_reacts:
+            t = torch.zeros(self.n_molecules * 2)
+            for sub in subs:
+                t[self.kinetics.mol_2_mi[sub]] -= 1
+            for prod in prods:
+                t[self.kinetics.mol_2_mi[prod]] += 1
+            M = self.kinetics.reaction_map.M
+            idxs = torch.argwhere((M == t).all(dim=1)).flatten().tolist()
+            react_map[(tuple(subs), tuple(prods))] = idxs
+
+        trnsp_map = {}
+        for mi, mol in enumerate(all_mols):
+            M = self.kinetics.transport_map.M
+            idxs = torch.argwhere(M[:, mi] != 0).flatten().tolist()
+            trnsp_map[mol] = idxs
+
+        reg_map = {}
+        for mi, mol in enumerate(all_mols):
+            M = self.kinetics.effector_map.M
+            idxs = torch.argwhere(M[:, mi] != 0).flatten().tolist()
+            reg_map[mol] = idxs
+
+        sign_map = {}
+        M = self.kinetics.sign_map.signs
+        sign_map[True] = torch.argwhere(M == 1.0).flatten().tolist()
+        sign_map[False] = torch.argwhere(M == -1.0).flatten().tolist()
+
+        cdss: list[list[str]] = []
+        for prot in proteome:
+            cds = []
+            for dom in prot.domain_facts:
+                # Domain structure:
+                # 0: domain type definition (1=catalytic, 2=transporter, 3=regulatory)
+                # 1-3: 3 x 1-codon specifications (Vmax, Km, sign)
+                # 4: 1 x 2-codon specification (reaction, molecule, effector)
+
+                if isinstance(dom, CatalyticDomainFact):
+                    react = (tuple(dom.substrates), tuple(dom.products))
+                    is_fwd = True
+                    if react not in react_map:
+                        react = (tuple(dom.products), tuple(dom.substrates))
+                        is_fwd = False
+                    i3 = random.choice(sign_map[is_fwd])
+                    i4 = random.choice(react_map[react])
+                    dom_seq = random.choice(dom_type_map[1])
+                    sign_seq = one_codon_map[i3]
+                    react_seq = two_codon_map[i4]
+                    mm_seq = random_genome(s=2 * CODON_SIZE, excl=stops)
+                    cds.append(dom_seq + mm_seq + sign_seq + react_seq)
+
+                if isinstance(dom, TransporterDomainFact):
+                    i4 = random.choice(trnsp_map[dom.molecule])
+                    dom_seq = random.choice(dom_type_map[2])
+                    mol_seq = two_codon_map[i4]
+                    mm_seq = random_genome(s=2 * CODON_SIZE, excl=stops)
+                    sign_seq = random_genome(s=CODON_SIZE, excl=stops)
+                    cds.append(dom_seq + mm_seq + sign_seq + mol_seq)
+
+                if isinstance(dom, RegulatoryDomainFact):
+                    i4 = random.choice(reg_map[dom.effector])
+                    dom_seq = random.choice(dom_type_map[3])
+                    mol_seq = two_codon_map[i4]
+                    mm_seq = random_genome(s=2 * CODON_SIZE, excl=stops)
+                    sign_seq = random_genome(s=CODON_SIZE, excl=stops)
+                    cds.append(dom_seq + mm_seq + sign_seq + mol_seq)
+
+            cdss.append(cds)
+
+        return cdss
 
     def _get_molecule_map(self, n: int, size: int, init: str) -> torch.Tensor:
         args = [n, size, size]
         if init == "zeros":
             return torch.zeros(*args).to(self.device)
         if init == "randn":
             return torch.abs(torch.randn(*args) + 10.0).to(self.device)
@@ -695,16 +923,16 @@
         d = 1 / mol_perm_rate
         return 1 / (d + 1)
 
     def _get_diffuse(self, mol_diff_rate: float) -> torch.nn.Conv2d:
         if mol_diff_rate < 0.0:
             mol_diff_rate = -mol_diff_rate
 
-        # TODO: mol_diff_rate > 1.0 could also mean expanding the kernel
-        #       so that molecules can diffuse more than just 1 pxl per round
+        # mol_diff_rate > 1.0 could also mean expanding the kernel
+        # so that molecules can diffuse more than just 1 pxl per round
         if mol_diff_rate > 1.0:
             mol_diff_rate = 1.0
 
         if mol_diff_rate == 0.0:
             a = 0.0
             b = 1.0
         else:
@@ -729,19 +957,18 @@
             padding_mode="circular",
             bias=False,
             device=self.device,
         )
         conv.weight = torch.nn.Parameter(kernel, requires_grad=False)
         return conv
 
-    def _expand(self, t: torch.Tensor, n: int, d: int) -> torch.Tensor:
-        pre = t.shape[slice(d)]
-        post = t.shape[slice(d + 1, t.dim())]
-        zeros = torch.zeros(*pre, n, *post, dtype=t.dtype).to(self.device)
-        return torch.cat([t, zeros], dim=d)
+    def _expand_c(self, t: torch.Tensor, n: int) -> torch.Tensor:
+        size = t.size()
+        zeros = torch.zeros(n, *size[1:], dtype=t.dtype).to(self.device)
+        return torch.cat([t, zeros], dim=0)
 
     def __repr__(self) -> str:
         kwargs = {
             "map_size": self.map_size,
             "abs_temp": self.abs_temp,
             "device": self.device,
             "workers": self.workers,
```

### Comparing `magicsoup-0.2.3/src/magicsoup.egg-info/PKG-INFO` & `magicsoup-0.3.0/src/magicsoup.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: magicsoup
-Version: 0.2.3
+Version: 0.3.0
 Summary: Simulation for cell metabolic and transduction pathway evolution
 Author-email: Marc <schweringmarc01@gmail.com>
 Project-URL: Documentation, https://magic-soup.readthedocs.io/
 Project-URL: Homepage, https://github.com/mRcSchwering/magic-soup
 Project-URL: Bug Tracker, https://github.com/mRcSchwering/magic-soup/issues
 Classifier: Environment :: Console
 Classifier: Environment :: GPU
@@ -35,15 +35,15 @@
 
 This game simulates cell metabolic and transduction pathway evolution.
 Define a 2D world with certain molecules and reactions.
 Add a few cells and create evolutionary pressure by selectively replicating and killing them.
 Then run and see what random mutations can do.
 
 ![co2 fixing](https://raw.githubusercontent.com/mRcSchwering/magic-soup/main/docs/img/co2fix.png)
-_In [this simulation](https://github.com/mRcSchwering/luca/tree/main/experiments/e1_co2_fixing) cells were made to fix CO2 from an artificial CO2 source in the middle of the map. (A) Total molecule counts of some molecule species over time. (B) Cell map with cells in white at chosen time points._
+_In [this simulation](https://github.com/mRcSchwering/luca/tree/main/e1_co2_fixing) cells were made to fix carbon from an artificial CO2 source in the middle of the map. (A) Total molecule counts of some molecule species over time. (B) Cell map with cells in white at chosen time points._
 
 ### Installation
 
 For CPU alone you can just do:
 
 ```
 pip install magicsoup
@@ -58,15 +58,15 @@
 
 The basic building blocks of what a cell can do are defined by the world's chemistry.
 There are molecules and reactions that can convert these molecules.
 Cells can develop proteins with domains that can transport these molecules,
 catalyze the reactions, and be regulated by molecules.
 Any reaction or transport happens only if energetically favourable.
 Below, I am defining the reaction $CO2 + NADPH \rightleftharpoons formiat + NADP$.
-Each molecule species is defined with a fictional standard Gibbs free energy of formation.
+Each molecule species is defined with a energy.
 
 ```python
 import torch
 import magicsoup as ms
 
 NADPH = ms.Molecule("NADPH", 200 * 1e3)
 NADP = ms.Molecule("NADP", 100 * 1e3)
@@ -84,24 +84,24 @@
 can be powered with the energy of energetically favourable ones.
 These domains, their specifications, and how they are coupled in proteins, is all encoded in the cell's genome.
 Here, I am generating 100 cells with random genomes of 500 basepairs each and place them
 in random places on the 2D world map.
 
 ```python
 genomes = [ms.random_genome(s=500) for _ in range(100)]
-world.add_random_cells(genomes=genomes)
+world.add_cells(genomes=genomes)
 ```
 
 Cells discover new proteins by chance through mutations.
 In the function below all cells experience 1E-3 random point mutations per nucleotide.
 10% of them will be indels.
 
 ```python
 def mutate_cells():
-    mutated = ms.point_mutations(seqs=[d.genome for d in world.cells])
+    mutated = ms.point_mutations(seqs=world.genomes)
     world.update_cells(genome_idx_pairs=mutated)
 ```
 
 Evolutionary pressure can be applied by selectively killing or replicating cells.
 Here, cells have an increased chance of dying when formiat gets too low
 and an increased chance of replicating when formiat gets high.
 
@@ -114,15 +114,15 @@
     x = world.cell_molecules[:, 2]
     idxs = sample(.01 / (.01 + x))
     world.kill_cells(cell_idxs=idxs)
 
 def replicate_cells():
     x = world.cell_molecules[:, 2]
     idxs = sample(x ** 3 / (x ** 3 + 20.0 ** 3))
-    world.replicate_cells(parent_idxs=idxs)
+    world.divide_cells(cell_idxs=idxs)
 ```
 
 Finally, the simulation itself is run in a python loop by repetitively calling the different steps.
 With `world.enzymatic_activity()` chemical reactions and molecule transport
 in cells advance by one time step.
 `world.diffuse_molecules()` lets molecules on the world map diffuse and permeate through cell membranes
 (if they can) by one time step.
```

### Comparing `magicsoup-0.2.3/src/magicsoup.egg-info/SOURCES.txt` & `magicsoup-0.3.0/src/magicsoup.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/tests/test_containers.py` & `magicsoup-0.3.0/tests/test_containers.py`

 * *Files identical despite different names*

### Comparing `magicsoup-0.2.3/tests/test_genetics.py` & `magicsoup-0.3.0/tests/test_genetics.py`

 * *Files 3% similar despite different names*

```diff
@@ -46,15 +46,15 @@
 ]
 
 
 @pytest.mark.parametrize("seq, exp", DATA)
 def test_get_coding_regions(seq: str, exp: list[str]):
     # 1 codon is too small to express p=0.01 domain types
     with pytest.warns(UserWarning):
-        genetics = ms.Genetics(n_dom_type_nts=3)
+        genetics = ms.Genetics(n_dom_type_codons=1)
 
     kwargs = {
         "start_codons": genetics.start_codons,
         "stop_codons": genetics.stop_codons,
         "min_cds_size": 18,
     }
 
@@ -69,19 +69,19 @@
     dom_type_map = {"AAA": 1, "GGG": 2, "CCC": 3}
     two_codon_map = {"ACTGAT": 1, "CTGTAT": 2, "CCGCGA": 3, "GGAATC": 4, "TGTCGA": 5}
     one_codon_map = {"ACT": 1, "CTG": 2, "CCG": 3, "GGA": 4, "TGT": 5}
     dom_type_size = len(next(iter(dom_type_map)))
 
     # fmt: off
     cdss = [
-        "AGACAAAAACCGCGACTGTGTACTTAGACTAGACG",  # (1, 3, 2, 5, 1)
-        "AGACTATAGCTAGAAGCCCCTGTCGATGTACTCCGTAGACG",  # (3, 5, 5, 1, 3)
-        "AGACTAGGGCCGCGACCGGGACTGCTAGAAGCTAGACTAGACG",  # (2, 3, 3, 4, 2)
-        "AAACTGTATCCGGGATGT",  # (1, 2, 3, 4, 5)
-        "CCCCCGCGACCGGGACTGGGGGGAATCACTCTGCCG",  # (3, 3, 3, 4, 2) (2, 4, 1, 2, 3)
+        "AGACAAAAACTGTGTACTCCGCGATAGACTAGACG",  # (1, 2, 5, 1, 3)
+        "AGACTATAGCTAGAAGCCCCTGTACTCCGTGTCGATAGACG",  # (3, 5, 1, 3, 5)
+        "AGACTAGGGCCGGGACTGCCGCGACTAGAAGCTAGACTAACG",  # (2, 3, 4, 2, 3)
+        "AAACCGGGATGTCTGTAT",  # (1, 3, 4, 5, 2)
+        "CCCCCGGGACTGCCGCGAGGGACTCTGCCGGGAATC",  # (3, 3, 4, 2, 3) (2, 1, 2, 3, 4)
     ]
     # - cds 0: normal domain                                                    => 1 res[0]
     # - cds 1: single type 3 domain, so it is removed
     # - cds 2: has 2 domain 2 starts, but the second is part of the 1 domain    => 1 res[1]
     # - cds 3: defines exactly 1 domain from start to end                       => 1 res[2]
     # - cds 4: defines exactly 2 domains, a 3rd type 2 start is in the middle   => 2 res[3]
     # fmt: on
@@ -95,19 +95,19 @@
         two_codon_map=two_codon_map,
     )
 
     assert len(res[0]) == 1
     assert len(res[1]) == 1
     assert len(res[2]) == 1
     assert len(res[3]) == 2
-    assert res[0][0] == (1, 3, 2, 5, 1)
-    assert res[1][0] == (2, 3, 3, 4, 2)
-    assert res[2][0] == (1, 2, 3, 4, 5)
-    assert res[3][0] == (3, 3, 3, 4, 2)
-    assert res[3][1] == (2, 4, 1, 2, 3)
+    assert res[0][0] == (1, 2, 5, 1, 3)
+    assert res[1][0] == (2, 3, 4, 2, 3)
+    assert res[2][0] == (1, 3, 4, 5, 2)
+    assert res[3][0] == (3, 3, 4, 2, 3)
+    assert res[3][1] == (2, 1, 2, 3, 4)
 
 
 
 def test_genetics():
     # 1=catalytic, 2=transporter, 3=regulatory
     # regulatory-only proteins get sorted out, so there is a bias towards
     # fewer regulatory domains
```

### Comparing `magicsoup-0.2.3/tests/test_kinetics.py` & `magicsoup-0.3.0/tests/test_kinetics.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,10 @@
 import pytest
 import torch
 from magicsoup.containers import (
-    Protein,
     Molecule,
     CatalyticDomain,
     RegulatoryDomain,
     TransporterDomain,
 )
 from magicsoup.kinetics import Kinetics
 from magicsoup.constants import GAS_CONSTANT
@@ -89,63 +88,136 @@
     return kinetics
 
 
 def avg(*x):
     return sum(x) / len(x)
 
 
-def test_unsetting_cell_params():
-    Km = torch.randn(2, 3, 8)
-    Vmax = torch.randn(2, 3)
-    E = torch.randn(2, 3)
-    N = torch.randn(2, 3, 8)
-    A = torch.randn(2, 3, 8)
+def test_cell_params_with_catalytic_domains_and_co_factors():
+    # Dealing with stoichiometric numbers that cancel each other out
+    # in general, intermediate molecules should be 0 in N
+    # but the reaction must depend on abundance of the starting molecules
+    # the first domain defines these starting molecules
+    # if these are 0 in N, they must appear in A
+
+    # C0, P0:
+    # bc->d then d->2b so bc->2b, with N b=1 c=-1 d=0
+    # b needs to be added as activating effector A b=1
+    # C0, P1:
+    # d->2b then bc->d, with N b=1 c=-1 d=0
+    # d needs to be added as activating effector A d=1
+    #
+    # the stoichiometry in both proteins in C0 is the same, but
+    # the order in which domains were defined is different
+    # That's why they differ in A
 
-    cell_prots0 = [(0, i) for i in range(3)]
-    cell_prots1 = [(1, i) for i in range(3)]
+    # Domain spec indexes: (dom_types, reacts_trnspts_effctrs, Vmaxs, Kms, signs)
+    # fmt: off
+    c0 = [
+        [
+            (1, 2, 15, 1, 3), # catal, Vmax 1.2, Km 1.5, fwd, bc->d
+            (1, 1, 5, 1, 4), # catal, Vmax 1.1, Km 0.5, fwd, d->2b
+        ],
+        [
+            (1, 1, 5, 1, 4), # catal, Vmax 1.1, Km 0.5, fwd, d->2b
+            (1, 2, 15, 1, 3), # catal, Vmax 1.2, Km 1.5, fwd, bc->d
+        ]
+    ]
+
+    # fmt: on
+
+    Km = torch.zeros(1, 3, 8)
+    Vmax = torch.zeros(1, 3)
+    E = torch.zeros(1, 3)
+    N = torch.zeros(1, 3, 8)
+    A = torch.zeros(1, 3, 8)
 
     # test
     kinetics = get_kinetics()
     kinetics.Km = Km
     kinetics.Vmax = Vmax
     kinetics.E = E
     kinetics.N = N
     kinetics.A = A
-    kinetics.unset_cell_params(cell_prots=cell_prots0 + cell_prots1)
+    kinetics.set_cell_params(cell_idxs=[0], proteomes=[c0])
 
-    assert torch.all(Km == 0.0)
-    assert torch.all(Vmax == 0.0)
-    assert torch.all(E == 0.0)
-    assert torch.all(N == 0.0)
-    assert torch.all(A == 0.0)
+    # proteins in C0 only differ in A
+    for p in [0, 1]:
+        assert Km[0, p, 1] == pytest.approx(avg(1.5, 1 / 0.5), abs=TOLERANCE)
+        assert Km[0, p, 2] == pytest.approx(1.5, abs=TOLERANCE)
+        assert Km[0, p, 3] == pytest.approx(avg(0.5, 1 / 1.5), abs=TOLERANCE)
+        for i in [0, 4, 5, 6, 7]:
+            assert Km[0, p, i] == 0.0
+
+        assert Vmax[0, p] == pytest.approx(avg(1.1, 1.2), abs=TOLERANCE)
+
+        assert E[0, p] == 10 - 10
+
+        assert N[0, p, 1] == 1
+        assert N[0, p, 2] == -1
+        assert N[0, p, 3] == 0
+        for i in [0, 4, 5, 6, 7]:
+            assert N[0, p, i] == 0
+
+    assert A[0, 0, 1] == 1
+    assert A[0, 1, 3] == 1
+    assert A.sum() == 2
+
+    # test proteome representation
+
+    proteins = kinetics.get_proteome(proteome=c0)
+
+    p0 = proteins[0]
+    assert isinstance(p0.domains[0], CatalyticDomain)
+    assert p0.domains[0].substrates == [mb, mc]
+    assert p0.domains[0].products == [md]
+    assert p0.domains[0].vmax == pytest.approx(1.2, abs=TOLERANCE)
+    assert p0.domains[0].km == pytest.approx(1.5, abs=TOLERANCE)
+    assert isinstance(p0.domains[1], CatalyticDomain)
+    assert p0.domains[1].substrates == [md]
+    assert p0.domains[1].products == [mb, mb]
+    assert p0.domains[1].vmax == pytest.approx(1.1, abs=TOLERANCE)
+    assert p0.domains[1].km == pytest.approx(0.5, abs=TOLERANCE)
+
+    p1 = proteins[1]
+    assert isinstance(p1.domains[0], CatalyticDomain)
+    assert p1.domains[0].substrates == [md]
+    assert p1.domains[0].products == [mb, mb]
+    assert p1.domains[0].vmax == pytest.approx(1.1, abs=TOLERANCE)
+    assert p1.domains[0].km == pytest.approx(0.5, abs=TOLERANCE)
+    assert isinstance(p1.domains[1], CatalyticDomain)
+    assert p1.domains[1].substrates == [mb, mc]
+    assert p1.domains[1].products == [md]
+    assert p1.domains[1].vmax == pytest.approx(1.2, abs=TOLERANCE)
+    assert p1.domains[1].km == pytest.approx(1.5, abs=TOLERANCE)
 
 
 def test_cell_params_with_transporter_domains():
 
     # Domain spec indexes: (dom_types, reacts_trnspts_effctrs, Vmaxs, Kms, signs)
     # fmt: off
     c0 = [
         [
-            (2, 1, 5, 5, 1)  # transporter, mol a, Vmax 1.5, Km 0.5, fwd
+            (2, 5, 5, 1, 1)  # transporter, Vmax 1.5, Km 0.5, fwd, mol a
         ],
         [
-            (2, 1, 5, 5, 1), # transporter, mol a, Vmax 1.5, Km 0.5, fwd
-            (2, 1, 1, 2, 2)  # transporter, mol a, Vmax 1.1, Km 0.2, bwd
+            (2, 5, 5, 1, 1), # transporter, Vmax 1.5, Km 0.5, fwd, mol a
+            (2, 1, 2, 2, 1)  # transporter, Vmax 1.1, Km 0.2, bwd, mol a
         ],
     ]
     c1 = [
         [
-            (2, 1, 5, 4, 1), # transporter, mol a, Vmax 1.5, Km 0.4, fwd
-            (2, 1, 4, 5, 1), # transporter, mol a, Vmax 1.4, Km 0.5, fwd
-            (2, 2, 3, 6, 1), # transporter, mol b, Vmax 1.3, Km 0.6, fwd
-            (2, 3, 2, 7, 1)  # transporter, mol c, Vmax 1.2, Km 0.7, fwd
+            (2, 5, 4, 1, 1), # transporter, Vmax 1.5, Km 0.4, fwd, mol a
+            (2, 4, 5, 1, 1), # transporter, Vmax 1.4, Km 0.5, fwd, mol a
+            (2, 3, 6, 1, 2), # transporter, Vmax 1.3, Km 0.6, fwd, mol b
+            (2, 2, 7, 1, 3)  # transporter, Vmax 1.2, Km 0.7, fwd, mol c
         ],
         [
-            (1, 1, 10, 5, 1), # catal, a->b, Vmax 2.0, Km 0.5, fwd
-            (2, 1, 5, 5, 1)   # transporter, mol a, Vmax 1.5, Km 0.5, fwd
+            (1, 10, 5, 1, 1), # catal, Vmax 2.0, Km 0.5, fwd, a->b
+            (2, 5, 5, 1, 1)   # transporter, Vmax 1.5, Km 0.5, fwd, mol a
         ],
     ]
     # fmt: on
 
     Km = torch.zeros(2, 3, 8)
     Vmax = torch.zeros(2, 3)
     E = torch.zeros(2, 3)
@@ -219,15 +291,18 @@
         assert N[1, 0, i] == 0
     assert N[1, 1, 0] == -2
     assert N[1, 1, 1] == 1
     assert N[1, 1, 4] == 1
     for i in [2, 3, 5, 6, 7]:
         assert N[1, 1, i] == 0
 
-    assert not A.any()
+    # a was imported and exported, so its N=0
+    # but it must be added as effector
+    assert A[0, 1, 0] == 1
+    assert A.sum() == 1
 
     # test proteome representation
 
     proteins = kinetics.get_proteome(proteome=c0)
 
     p0 = proteins[0]
     assert isinstance(p0.domains[0], TransporterDomain)
@@ -279,35 +354,35 @@
 
 def test_cell_params_with_regulatory_domains():
 
     # Domain spec indexes: (dom_types, reacts_trnspts_effctrs, Vmaxs, Kms, signs)
     # fmt: off
     c0 = [
         [
-            (1, 1, 10, 5, 1), # catal, a->b, Vmax 2.0, Km 0.5, fwd
-            (3, 3, 0, 10, 1), # reg, c, Km 1.0, cyto, act
-            (3, 4, 0, 20, 2), # reg, d, Km 2.0, cyto, inh
+            (1, 10, 5, 1, 1), # catal, Vmax 2.0, Km 0.5, fwd, a->b
+            (3, 0, 10, 1, 3), # reg, Km 1.0, cyto, act, c
+            (3, 0, 20, 2, 4), # reg, Km 2.0, cyto, inh, d
         ],
         [
-            (1, 1, 10, 5, 1), # catal, a->b, Vmax 2.0, Km 0.5, fwd
-            (3, 1, 0, 10, 1), # reg, a, Km 1.0, cyto, act
-            (3, 5, 0, 15, 1), # reg, a, Km 1.5, transm, act
+            (1, 10, 5, 1, 1), # catal, Vmax 2.0, Km 0.5, fwd, a->b
+            (3, 0, 10, 1, 1), # reg, Km 1.0, cyto, act, a
+            (3, 0, 15, 1, 5), # reg, Km 1.5, transm, act, a
         ]
     ]
 
     c1 = [
         [
-            (1, 1, 10, 5, 1), # catal, a->b, Vmax 2.0, Km 0.5, fwd
-            (3, 2, 0, 10, 2), # reg, b, Km 1.0, cyto, inh
-            (3, 6, 0, 15, 2), # reg, b, Km 1.5, transm, inh
+            (1, 10, 5, 1, 1), # catal, Vmax 2.0, Km 0.5, fwd, a->b
+            (3, 0, 10, 2, 2), # reg, Km 1.0, cyto, inh, b
+            (3, 0, 15, 2, 6), # reg, Km 1.5, transm, inh, b
         ],
         [
-            (1, 1, 10, 5, 1), # catal, a->b, Vmax 2.0, Km 0.5, fwd
-            (3, 4, 0, 10, 1), # reg, d, Km 1.0, cyto, act
-            (3, 4, 0, 15, 1), # reg, d, Km 1.5, cyto, act
+            (1, 10, 5, 1, 1), # catal, Vmax 2.0, Km 0.5, fwd, a->b
+            (3, 0, 10, 1, 4), # reg, Km 1.0, cyto, act, d
+            (3, 0, 15, 1, 4), # reg, Km 1.5, cyto, act, d
         ]
     ]
     # fmt: on
 
     Km = torch.zeros(2, 3, 8)
     Vmax = torch.zeros(2, 3)
     E = torch.zeros(2, 3)
@@ -374,31 +449,31 @@
     assert N[0, 0, 0] == -1
     assert N[0, 0, 1] == 1
     assert N[0, 0, 2] == 0
     assert N[0, 0, 3] == 0
     for i in [4, 5, 6, 7]:
         assert N[0, 0, i] == 0
     assert N[0, 1, 0] == -1
-    assert N[0, 1, 1] == 1  # b is added and removed
+    assert N[0, 1, 1] == 1
     assert N[0, 1, 2] == 0
     assert N[0, 1, 3] == 0
     for i in [4, 5, 6, 7]:
         assert N[0, 1, i] == 0
     for i in range(8):
         assert N[0, 2, i] == 0
 
     assert N[1, 0, 0] == -1
-    assert N[1, 0, 1] == 1  # b is added and removed
+    assert N[1, 0, 1] == 1
     assert N[1, 0, 2] == 0
     assert N[1, 0, 3] == 0
     for i in [4, 5, 6, 7]:
         assert N[1, 0, i] == 0
     assert N[1, 1, 0] == -1
     assert N[1, 1, 1] == 1
-    assert N[1, 1, 2] == 0  # c is added and removed
+    assert N[1, 1, 2] == 0
     assert N[1, 1, 3] == 0
     for i in [4, 5, 6, 7]:
         assert N[1, 1, i] == 0
     for i in range(8):
         assert N[1, 2, i] == 0
 
     assert A[0, 0, 0] == 0
@@ -510,33 +585,33 @@
 
 def test_cell_params_with_catalytic_domains():
 
     # Domain spec indexes: (dom_types, reacts_trnspts_effctrs, Vmaxs, Kms, signs)
     # fmt: off
     c0 = [
         [
-            (1, 1, 1, 5, 1), # catal, a->b, Vmax 1.1, Km 0.5, fwd
-            (1, 3, 2, 15, 2), # catal, bc->d, Vmax 1.2, Km 1.5, bwd
+            (1, 1, 5, 1, 1), # catal, Vmax 1.1, Km 0.5, fwd, a->b
+            (1, 2, 15, 2, 3), # catal, Vmax 1.2, Km 1.5, bwd, bc->d
         ],
         [
-            (1, 2, 10, 9, 1), # catal, b->c, Vmax 2.0, Km 0.9, fwd
-            (1, 3, 3, 12, 2), # catal, bc->d, Vmax 1.3, Km 1.2, bwd
+            (1, 10, 9, 1, 2), # catal, Vmax 2.0, Km 0.9, fwd, b->c
+            (1, 3, 12, 2, 3), # catal, Vmax 1.3, Km 1.2, bwd, bc->d
         ],
         [
-            (1, 4, 19, 29, 1), # catal, d->bb, Vmax 2.9, Km 2.9, fwd
+            (1, 19, 29, 1, 4), # catal, Vmax 2.9, Km 2.9, fwd, d->bb
         ]
     ]
     c1 = [
         [
-            (1, 1, 1, 3, 2), # catal, a->b, Vmax 1.1, Km 0.3, bwd
-            (1, 3, 11, 14, 2), # catal, bc->d, Vmax 2.1, Km 1.4, bwd
+            (1, 1, 3, 2, 1), # catal, Vmax 1.1, Km 0.3, bwd, a->b
+            (1, 11, 14, 2, 3), # catal, Vmax 2.1, Km 1.4, bwd, bc->d
         ],
         [
-            (1, 2, 9, 3, 1), # catal, b->c, Vmax 1.9, Km 0.3, fwd
-            (1, 3, 13, 17, 1), # catal, bc->d, Vmax 2.3, Km 1.7, fwd
+            (1, 9, 3, 1, 2), # catal, Vmax 1.9, Km 0.3, fwd, b->c
+            (1, 13, 17, 1, 3), # catal, Vmax 2.3, Km 1.7, fwd, bc->d
         ]
     ]
 
     # fmt: on
 
     Km = torch.zeros(2, 3, 8)
     Vmax = torch.zeros(2, 3)
@@ -633,15 +708,20 @@
     assert N[1, 1, 2] == 0  # c is added and removed
     assert N[1, 1, 3] == 1
     for i in [4, 5, 6, 7]:
         assert N[1, 1, i] == 0
     for i in range(8):
         assert N[1, 2, i] == 0
 
-    assert not A.any()
+    # b was a reactant in the first domain,
+    # but was then created again yielding N b=0
+    # it thus has to be added as activating effector
+    assert A[0, 1, 1] == 1
+    assert A[1, 0, 1] == 1
+    assert A.sum() == 2
 
     # test protein representation
 
     proteins = kinetics.get_proteome(proteome=c0)
 
     p0 = proteins[0]
     assert isinstance(p0.domains[0], CatalyticDomain)
```

