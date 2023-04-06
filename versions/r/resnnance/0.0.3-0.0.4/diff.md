# Comparing `tmp/resnnance-0.0.3.tar.gz` & `tmp/resnnance-0.0.4.tar.gz`

## Comparing `resnnance-0.0.3.tar` & `resnnance-0.0.4.tar`

### file list

```diff
@@ -1,12 +1,16 @@
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/__init__.py
--rw-r--r--   0        0        0     1355 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/core/__init__.py
--rw-r--r--   0        0        0      362 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/core/templates/template.vhd
--rw-r--r--   0        0        0     1394 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/pyNN/__init__.py
--rw-r--r--   0        0        0      839 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/pyNN/populations.py
--rw-r--r--   0        0        0      131 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/pyNN/recording.py
--rw-r--r--   0        0        0     2015 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/pyNN/simulator.py
--rw-r--r--   0        0        0       98 2020-02-02 00:00:00.000000 resnnance-0.0.3/src/resnnance/pyNN/models/cells.py
--rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 resnnance-0.0.3/.gitignore
--rw-r--r--   0        0        0       98 2020-02-02 00:00:00.000000 resnnance-0.0.3/README.md
--rw-r--r--   0        0        0      703 2020-02-02 00:00:00.000000 resnnance-0.0.3/pyproject.toml
--rw-r--r--   0        0        0      727 2020-02-02 00:00:00.000000 resnnance-0.0.3/PKG-INFO
+-rw-r--r--   0        0        0      140 2020-02-02 00:00:00.000000 resnnance-0.0.4/setup.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/__init__.py
+-rw-r--r--   0        0        0     1969 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/core/__init__.py
+-rw-r--r--   0        0        0      362 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/core/templates/template.vhd
+-rw-r--r--   0        0        0      848 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/__init__.py
+-rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/control.py
+-rw-r--r--   0        0        0     4758 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/populations.py
+-rw-r--r--   0        0        0     2372 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/projections.py
+-rw-r--r--   0        0        0     1291 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/recording.py
+-rw-r--r--   0        0        0     2439 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/simulator.py
+-rw-r--r--   0        0        0       98 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/models/cells.py
+-rw-r--r--   0        0        0      431 2020-02-02 00:00:00.000000 resnnance-0.0.4/src/resnnance/pyNN/models/synapses.py
+-rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 resnnance-0.0.4/.gitignore
+-rw-r--r--   0        0        0       98 2020-02-02 00:00:00.000000 resnnance-0.0.4/README.md
+-rw-r--r--   0        0        0      715 2020-02-02 00:00:00.000000 resnnance-0.0.4/pyproject.toml
+-rw-r--r--   0        0        0      751 2020-02-02 00:00:00.000000 resnnance-0.0.4/PKG-INFO
```

### Comparing `resnnance-0.0.3/src/resnnance/pyNN/__init__.py` & `resnnance-0.0.4/src/resnnance/pyNN/control.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,14 +1,11 @@
 from pyNN.common import control
 from pyNN.common.control import DEFAULT_MAX_DELAY, DEFAULT_TIMESTEP, DEFAULT_MIN_DELAY
 
 from resnnance.pyNN import simulator
-from resnnance.pyNN.populations import Population, PopulationView, Assembly
-from resnnance.pyNN.models.cells import *
-
 
 def setup(timestep=DEFAULT_TIMESTEP, min_delay=DEFAULT_MIN_DELAY, **extra_params):
     """
     Initial configuration of the ReSNNance simulator (singleton model: there is only
     one instance of the simulator, defined here)
     """
 
@@ -31,15 +28,21 @@
     simulator.state.dt = timestep
 
 
 def end():
     """
     Simulator clean up and exit
     """
+    # Write to files on end
+    for (population, variables, filename) in simulator.state.write_on_end:
+        io = get_io(filename)
+        population.write_data(io, variables)
+    simulator.state.write_on_end = []
 
     # Remove simulator singleton
     simulator.state = None
 
 
 run, run_until = control.build_run(simulator)
+run_for = run
 reset = control.build_reset(simulator)
 get_current_time, get_time_step, get_min_delay, get_max_delay, num_processes, rank = control.build_state_queries(simulator)
```

### Comparing `resnnance-0.0.3/src/resnnance/pyNN/simulator.py` & `resnnance-0.0.4/src/resnnance/pyNN/simulator.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,14 +1,22 @@
 import logging
 from typing import Optional
 
 from pyNN.common import control
+from pyNN.common import populations
 
 import resnnance.core as core
 
+class ID(int, populations.IDMixin):
+
+    def __init__(self, n):
+        """Create an ID object with numerical value `n`."""
+        int.__init__(n)
+        populations.IDMixin.__init__(self)
+
 
 class State(control.BaseState):
     """
     ReSNNance PyNN simulator interface
     """
 
     def __init__(self):
@@ -27,43 +35,46 @@
         handler.setFormatter(formatter)
         self.logger.addHandler(handler)
 
         # Log ReSNNance environment creation
         self.logger.info("Created new ReSNNance pyNN environment")
 
         # PyNN common attributes
-        self.t = 0                      # Current time (ms)
-        self.dt = 0                     # Integration time step (ms)
         self.min_delay = 0              # Minimum allowed synaptic delay (ms)
         self.max_delay = 0              # Maximum allowed synaptic delay (ms)
+        self.dt = 0.1                   # Integration time step (ms)
         self.num_processes = 1          # MPI processes - meaningless on ReSNNance, always 1
         self.mpi_rank = 0               # MPI rank - meaningless on ReSNNance, always 0 (head node)
-        self.recorders = set([])        # Empty set of recorders
+
+        # Clear recorders and reset
+        self.clear()
 
         # ReSNNance
         self.core = core.ReSNNance()    # Core generator/simulator
 
-
-    def reset(self):
-        """
-        Resets the simulator
-        """
-
-        # Reset simulator time
-        self.t = 0
-
+    def run(self, simtime):
+        self.t += simtime
+        self.running = True
+        self.logger.info(f"Simulation T = {(self.t):.1f} ms")
 
     def run_until(self, tstop):
-        """
-        Runs the simulator
-        """
-
-        # Update simulator time
         self.t = tstop
+        self.running = True
+        self.logger.info(f"Simulation T = {(self.t):.1f} ms")
 
-        # Log simulation runtime
-        self.logger.info(f"Simulation T = {(tstop):.1f} ms")
+    def clear(self):
+        self.recorders = set([])
+        self.id_counter = 0
+        self.segment_counter = -1
+        self.reset()
+
+    def reset(self):
+        """Reset the state of the current network to time t = 0."""
+        self.running = False
+        self.t = 0
+        self.t_start = 0
+        self.segment_counter += 1
 
 
 # ReSNNance simulator singleton object (instantiated in setup())
 # Optional[] is a type hint: state can be a State object or None
 state: Optional[State] = None
```

### Comparing `resnnance-0.0.3/pyproject.toml` & `resnnance-0.0.4/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "resnnance"
-version = "0.0.3"
+version = "0.0.4"
 authors = [
     { name = "Samuel López Asunción", email = "samuel.lopez.asuncion@upm.es"},
 ]
 description = "An FPGA hardware accelerator generator for spiking neural networks + PyNN frontend"
 readme = "README.md"
 requires-python = ">=3.9"
 dependencies = [
-    "numpy", "jinja2", "pyNN"
+    "numpy", "jinja2", "networkx", "pyNN"
 ]
 classifiers = [
     "Development Status :: 1 - Planning",
     "Programming Language :: Python :: 3",
     "Operating System :: OS Independent",
 ]
```

### Comparing `resnnance-0.0.3/PKG-INFO` & `resnnance-0.0.4/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 Metadata-Version: 2.1
 Name: resnnance
-Version: 0.0.3
+Version: 0.0.4
 Summary: An FPGA hardware accelerator generator for spiking neural networks + PyNN frontend
 Project-URL: Homepage, https://repo-lsi.die.upm.es/slopez/resnnance
 Project-URL: Bug Tracker, https://repo-lsi.die.upm.es/slopez/resnnance/issues
 Author-email: Samuel López Asunción <samuel.lopez.asuncion@upm.es>
 Classifier: Development Status :: 1 - Planning
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.9
 Requires-Dist: jinja2
+Requires-Dist: networkx
 Requires-Dist: numpy
 Requires-Dist: pynn
 Description-Content-Type: text/markdown
 
 ### ReSNNance
 
 An FPGA hardware accelerator generator for spiking neural networks + PyNN frontend
```

