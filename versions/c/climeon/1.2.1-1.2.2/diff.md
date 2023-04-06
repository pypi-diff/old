# Comparing `tmp/climeon-1.2.1.tar.gz` & `tmp/climeon-1.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "climeon-1.2.1.tar", last modified: Thu Mar 23 16:33:55 2023, max compression
+gzip compressed data, was "climeon-1.2.2.tar", last modified: Thu Apr  6 14:40:49 2023, max compression
```

## Comparing `climeon-1.2.1.tar` & `climeon-1.2.2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-03-23 16:33:55.630287 climeon-1.2.1/
--rw-rw-rw-   0        0        0      580 2023-03-23 16:33:55.629287 climeon-1.2.1/PKG-INFO
--rw-rw-rw-   0        0        0       26 2023-03-23 16:33:28.000000 climeon-1.2.1/README.md
-drwxrwxrwx   0        0        0        0 2023-03-23 16:33:55.607281 climeon-1.2.1/climeon/
--rw-rw-rw-   0        0        0       88 2023-03-23 16:33:28.000000 climeon-1.2.1/climeon/__init__.py
--rw-rw-rw-   0        0        0    27262 2023-03-23 16:33:25.000000 climeon-1.2.1/climeon/api.py
--rw-rw-rw-   0        0        0     2085 2023-03-23 16:33:25.000000 climeon-1.2.1/climeon/identifiers.py
--rw-rw-rw-   0        0        0    10565 2023-03-23 16:33:25.000000 climeon-1.2.1/climeon/plotting.py
-drwxrwxrwx   0        0        0        0 2023-03-23 16:33:55.624291 climeon-1.2.1/climeon.egg-info/
--rw-rw-rw-   0        0        0      580 2023-03-23 16:33:54.000000 climeon-1.2.1/climeon.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      250 2023-03-23 16:33:55.000000 climeon-1.2.1/climeon.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-23 16:33:54.000000 climeon-1.2.1/climeon.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       68 2023-03-23 16:33:54.000000 climeon-1.2.1/climeon.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2023-03-23 16:33:54.000000 climeon-1.2.1/climeon.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-23 16:33:55.630287 climeon-1.2.1/setup.cfg
--rw-rw-rw-   0        0        0      867 2023-03-23 16:33:28.000000 climeon-1.2.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:40:49.881736 climeon-1.2.2/
+-rw-rw-rw-   0        0        0      580 2023-04-06 14:40:49.879705 climeon-1.2.2/PKG-INFO
+-rw-rw-rw-   0        0        0       26 2023-04-06 14:40:30.000000 climeon-1.2.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 14:40:49.853700 climeon-1.2.2/climeon/
+-rw-rw-rw-   0        0        0       88 2023-04-06 14:40:30.000000 climeon-1.2.2/climeon/__init__.py
+-rw-rw-rw-   0        0        0    27566 2023-04-06 14:40:22.000000 climeon-1.2.2/climeon/api.py
+-rw-rw-rw-   0        0        0     2085 2023-04-06 14:40:22.000000 climeon-1.2.2/climeon/identifiers.py
+-rw-rw-rw-   0        0        0    10921 2023-04-06 14:40:22.000000 climeon-1.2.2/climeon/plotting.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:40:49.871709 climeon-1.2.2/climeon.egg-info/
+-rw-rw-rw-   0        0        0      580 2023-04-06 14:40:48.000000 climeon-1.2.2/climeon.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      250 2023-04-06 14:40:49.000000 climeon-1.2.2/climeon.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:40:48.000000 climeon-1.2.2/climeon.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       85 2023-04-06 14:40:48.000000 climeon-1.2.2/climeon.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 14:40:48.000000 climeon-1.2.2/climeon.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:40:49.883708 climeon-1.2.2/setup.cfg
+-rw-rw-rw-   0        0        0      896 2023-04-06 14:40:30.000000 climeon-1.2.2/setup.py
```

### Comparing `climeon-1.2.1/PKG-INFO` & `climeon-1.2.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: climeon
-Version: 1.2.1
+Version: 1.2.2
 Summary: Climeon API client
 Home-page: UNKNOWN
 Author: Emil Hjelm
 Author-email: emil.hjelm@climeon.com
 License: MIT
 Keywords: climeon,REST,API
 Platform: UNKNOWN
```

### Comparing `climeon-1.2.1/climeon/api.py` & `climeon-1.2.2/climeon/api.py`

 * *Files 0% similar despite different names*

```diff
@@ -233,21 +233,25 @@
         response = self.post("/Analytics", body)
         raw_data = response.json()
         dataframe = json_to_dataframe(raw_data[machine_id])
         if dataframe.empty:
             self.logger.warning("No data found for %s between %s and %s",
                                 machine_id, date_from, date_to)
             return dataframe
-        dataframe = format_dataframe(dataframe, date_from.tzinfo)
+        dataframe = format_dataframe(dataframe, date_from.tzinfo, False)
         rec_int = (dataframe.index[1] - dataframe.index[0]).total_seconds()
         if SQL_INTERVALS[interval] < rec_int:
             int_str = next(i for i, v in SQL_INTERVALS.items() if v >= rec_int)
             self.logger.warning("Requested interval %s could not be fetched, "
                                 "got interval %s instead. Use logfile data to "
                                 "get higher resolution.", interval, int_str)
+        else:
+            int_str = interval
+        pandas_interval = int_str[2:].replace("M", "T")
+        dataframe = dataframe.resample(pandas_interval).first()
         save_dataframe(dataframe, filename)
         return dataframe
 
     def analytics_variables(self, machine_id):
         """Get all available variables for a machine."""
         endpoint = f"/Analytics/variables/{machine_id}"
         response = self.get(endpoint)
@@ -603,15 +607,15 @@
     columns.insert(0, "Timestamp")
     data = [p["values"] for p in raw_data["properties"]]
     data.insert(0, raw_data["timestamps"])
     data = list(map(list, zip(*data)))
     dataframe = pd.DataFrame(data, columns=columns)
     return dataframe
 
-def format_dataframe(dataframe, original_tz):
+def format_dataframe(dataframe, original_tz, resample=True):
     """Clean up and properly timestamp dataframe."""
     dataframe = dataframe.loc[:, ~dataframe.columns.str.contains("^Unnamed")]
     ts_1 = parse_datetime(dataframe["Timestamp"][0])
     ts_2 = parse_datetime(dataframe["Timestamp"][1])
     if ts_2 - ts_1 < timedelta(seconds=0.5):
         # Blackbox file, need to use Timestamp column to maintain resolution
         utc_1 = parse_datetime(dataframe["Timestamp UTC [-]"][0])
@@ -625,14 +629,17 @@
         dataframe["Timestamp"] = pd.to_datetime(dataframe["Timestamp"])
     dataframe = dataframe.set_index("Timestamp")
     if dataframe.index.tz is None:
         dataframe.index = dataframe.index.tz_localize(timezone.utc)
     dataframe.index = dataframe.index.tz_convert(original_tz)
     dataframe.fillna(value=np.nan, inplace=True)
     dataframe.replace(-32768, np.nan, inplace=True)
+    if resample:
+        # Add missing timestamps as NaN
+        dataframe = dataframe.resample("1S").first()
     return dataframe
 
 def default_sql_interval(date_from, date_to):
     """Figure out a reasonable interval for a time range."""
     diff = (date_to - date_from).total_seconds()
     for interval, max_result in MAX_SQL_INTERVALS.items():
         if diff < max_result:
```

### Comparing `climeon-1.2.1/climeon/identifiers.py` & `climeon-1.2.2/climeon/identifiers.py`

 * *Files identical despite different names*

### Comparing `climeon-1.2.1/climeon/plotting.py` & `climeon-1.2.2/climeon/plotting.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,16 +1,18 @@
 """Climeon plotting utilities."""
 
 # Standard modules
 import math
 
 # External modules
 from pandas import DataFrame
-from plotly.graph_objects import Scatter
+from plotly.graph_objects import Scattergl
 from plotly.subplots import make_subplots
+from plotly_resampler import FigureResampler, FigureWidgetResampler, \
+    EveryNthPoint
 
 STATES = [
     "INIT",
     "IDLE",
     "READY",
     "START",
     "RUNNING",
@@ -72,37 +74,26 @@
     "", # EXHAUST_VALVE_OPEN
     "", # VACANT
     "", # VACANT
     "", # VACANT
     "REMOTE_CONTROL"
 ]
 
-REGULATORS = [
-    "",
-    "Power regulator",
-    "Current regulator",
-    "Turbine winding temp",
-    "Condenser pressure regulator",
-    "Return water regulator",
-    "Base regualtor",
-    "Incomplete evap killer",
-]
-
 def add_transition(fig, data, variable, color, states, template, pos):
     """Add status transitions for a specific variable in a plotly figure."""
     # pylint: disable=too-many-arguments
     if variable not in data:
         return
     template = template or "%s"
-    edges = data[(data[variable].diff() != 0).fillna(False)]
-    for idx, (timestamp, state) in enumerate(zip(edges.index, edges[variable])):
-        if idx == 0 or state == 0:
+    edges = data[abs(data[variable].diff()) > 0][variable].astype(int)
+    for idx, (timestamp, state) in enumerate(zip(edges.index, edges)):
+        if state == 0:
             continue
-        if variable in ["StatusWord [-]", "SecondaryStatusWord [-]"]:
-            bit = int(state ^ edges[variable][idx-1]).bit_length() - 1
+        if variable in ["StatusWord [-]", "SecondaryStatusWord [-]"] and idx > 0:
+            bit = int(state ^ edges[idx-1]).bit_length() - 1
             if not (state >> bit) & 1 or not states[bit]:
                 continue
             text = "%s" % states[bit]
         elif states and not states[state]:
             continue
         elif states:
             text = template % states[state]
@@ -126,19 +117,19 @@
     add_transition(fig, data, "AlarmCode [-]", "red", None, "AlarmCode %s", 1.04)
     add_transition(fig, data, "NoOfGreasingCyclesFrontBearing [-]", "blue",
                    None, "Front greasing", 1)
     add_transition(fig, data, "NoOfGreasingCyclesRearBearing [-]", "blue",
                    None, "Rear greasing", 1)
     add_transition(fig, data, "NoOfAtuCycles [-]", "green", None, "ATU", 1)
     if "State [-]" not in data:
-        add_transition(fig, data, "StatusWord [-]", "green", STATUS_WORD, None, 0.96)
+        add_transition(fig, data, "StatusWord [-]", "blue", STATUS_WORD, None, 0.96)
     if "Wetgas detected [-]" in data:
         color_code(fig, data["Wetgas detected [-]"], [None, "red"])
     elif "SecondaryStatusWord [-]" in data:
-        wet_gas = (data["SecondaryStatusWord [-]"] & (1 << 10) > 0) * 1
+        wet_gas = (data["SecondaryStatusWord [-]"].dropna().astype(int) & (1 << 10) > 0) * 1
         color_code(fig, wet_gas, [None, "red"])
 
 def color_code(fig, state, colors, text=""):
     """Color code the background of a plot based on state."""
     state_notnull = state.fillna(False)
     state_changes = state_notnull[state_notnull.diff() != 0]
     for idx, timestamp in enumerate(state_changes.index):
@@ -147,32 +138,39 @@
         else:
             end_idx = state_changes.index[idx + 1]
         color = colors[int(state_changes[timestamp])]
         if color is not None:
             fig.add_vrect(timestamp, end_idx, annotation_text=text,
                           fillcolor=color, opacity=0.2, line_width=0)
 
-def add_regulators(fig, data):
-    """Add active regulator to a plot."""
-    temp = data.copy()
-    temp["ActiveController [-]"] = \
-        (data["SecondaryStatusWord [-]"].apply(lambda x: (x >> 24) & 1) * 1) + \
-        (data["SecondaryStatusWord [-]"].apply(lambda x: (x >> 25) & 1) * 2) + \
-        (data["SecondaryStatusWord [-]"].apply(lambda x: (x >> 26) & 1) * 3) + \
-        (data["SecondaryStatusWord [-]"].apply(lambda x: (x >> 27) & 1) * 4) + \
-        (data["SecondaryStatusWord [-]"].apply(lambda x: (x >> 28) & 1) * 5) + \
-        (data["SecondaryStatusWord [-]"].apply(lambda x: (x >> 29) & 1) * 6) + \
-        (data["SecondaryStatusWord [-]"].apply(lambda x: (x >> 30) & 1) * 7)
-    add_transition(fig, temp, "ActiveController [-]", "green", REGULATORS, None, 1)
+def get_figure(rows=1, secondary_y=True, resampler=True, height=900):
+    """Convenience function for creating a plotly figure.
+
+    Parameters:
+        rows (int): Amount of plot rows to include (subplots).
+        secondary_y (bool):
+        resampler (bool): Indicates if resampling should be done dynamically
+                          to improve loading times.
+        height (int): Figure height.
+    """
+    specs = [[{"secondary_y": secondary_y}] for _ in range(rows)]
+    fig = make_subplots(rows, 1, shared_xaxes=True, vertical_spacing=0.02, specs=specs)
+    if resampler:
+        if is_notebook():
+            fig = FigureWidgetResampler(fig)
+        else:
+            fig = FigureResampler(fig)
+    fig.update_layout(hovermode="x", height=height)
+    fig.update_traces(mode="lines", hovertemplate=None)
+    return fig
 
-def standard_plot(data):
+def standard_plot(data, resampler=True):
     """Create a plot with state transitions and useful variables."""
     # pylint: disable=too-many-statements
-    specs = [[{"secondary_y": True}], [{"secondary_y": True}]]
-    fig = make_subplots(2, 1, shared_xaxes=True, vertical_spacing=0.02, specs=specs)
+    fig = get_figure(rows=2, resampler=resampler)
     fig.update_layout(hovermode="x", height=900)
     fig.update_traces(mode="lines", hovertemplate=None)
 
     # 1st plot: Power and Control with state transitions
     # 1st axis [kW], [krpm]
     add_trace(fig, data, "PowerOutput [kW]", 1)
     if "TurbSpeed [rpm]" in data:
@@ -250,15 +248,29 @@
     fig["layout"]["yaxis4"]["title"] = "[bar], [-]"
     fig["layout"]["yaxis4"]["showgrid"] = False
     fig["layout"]["yaxis4"]["zeroline"] = False
 
     add_transitions(fig, data)
     return fig
 
-def add_trace(fig, data, variable, row, visible=None, yaxis=None, secondary_y=False):
-    """Add a trace to a figure."""
+def add_trace(fig, data, variable, row, visible=None, secondary_y=False):
+    """Add a trace to a resampled plotly figure."""
     # pylint: disable=too-many-arguments
     if not variable in data:
         return
-    trace = Scatter(x=data.index, y=data[variable].values, name=variable,
-                    visible=visible, yaxis=yaxis)
-    fig.add_trace(trace, row=row, col=1, secondary_y=secondary_y)
+    if isinstance(fig, FigureWidgetResampler):
+        trace = Scattergl(name=variable, visible=visible)
+        fig.add_trace(trace, row=row, col=1, secondary_y=secondary_y,
+                      hf_x=data.index, hf_y=data[variable].values,
+                      downsampler=EveryNthPoint(interleave_gaps=False))
+    else:
+        trace = Scattergl(x=data.index, y=data[variable].values, name=variable,
+                          visible=visible)
+        fig.add_trace(trace, row=row, col=1, secondary_y=secondary_y)
+
+def is_notebook():
+    """Check if code is running in a notebook."""
+    try:
+        get_ipython()
+        return True
+    except NameError:
+        return False
```

### Comparing `climeon-1.2.1/climeon.egg-info/PKG-INFO` & `climeon-1.2.2/climeon.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: climeon
-Version: 1.2.1
+Version: 1.2.2
 Summary: Climeon API client
 Home-page: UNKNOWN
 Author: Emil Hjelm
 Author-email: emil.hjelm@climeon.com
 License: MIT
 Keywords: climeon,REST,API
 Platform: UNKNOWN
```

### Comparing `climeon-1.2.1/setup.py` & `climeon-1.2.2/setup.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 00000000: 0d0a 6672 6f6d 2073 6574 7570 746f 6f6c  ..from setuptool
 00000010: 7320 696d 706f 7274 2073 6574 7570 2c20  s import setup, 
 00000020: 6669 6e64 5f70 6163 6b61 6765 730d 0a0d  find_packages...
 00000030: 0a73 6574 7570 280d 0a20 2020 206e 616d  .setup(..    nam
 00000040: 653d 2263 6c69 6d65 6f6e 222c 0d0a 2020  e="climeon",..  
 00000050: 2020 7061 636b 6167 6573 3d66 696e 645f    packages=find_
 00000060: 7061 636b 6167 6573 2829 2c0d 0a20 2020  packages(),..   
-00000070: 2076 6572 7369 6f6e 3d22 312e 322e 3122   version="1.2.1"
+00000070: 2076 6572 7369 6f6e 3d22 312e 322e 3222   version="1.2.2"
 00000080: 2c0d 0a20 2020 206c 6963 656e 7365 3d22  ,..    license="
 00000090: 4d49 5422 2c0d 0a20 2020 2064 6573 6372  MIT",..    descr
 000000a0: 6970 7469 6f6e 3d22 436c 696d 656f 6e20  iption="Climeon 
 000000b0: 4150 4920 636c 6965 6e74 222c 0d0a 2020  API client",..  
 000000c0: 2020 6c6f 6e67 5f64 6573 6372 6970 7469    long_descripti
 000000d0: 6f6e 3d22 436c 696d 656f 6e20 4150 4920  on="Climeon API 
 000000e0: 636c 6965 6e74 222c 0d0a 2020 2020 6175  client",..    au
@@ -21,35 +21,36 @@
 00000140: 6c69 6d65 6f6e 222c 2022 5245 5354 222c  limeon", "REST",
 00000150: 2022 4150 4922 5d2c 0d0a 2020 2020 7079   "API"],..    py
 00000160: 7468 6f6e 5f72 6571 7569 7265 733d 223e  thon_requires=">
 00000170: 3d33 2e37 2e31 222c 0d0a 2020 2020 696e  =3.7.1",..    in
 00000180: 7374 616c 6c5f 7265 7175 6972 6573 3d5b  stall_requires=[
 00000190: 0d0a 2020 2020 2020 2020 2270 6c6f 746c  ..        "plotl
 000001a0: 793e 3d35 2c3c 3622 2c0d 0a20 2020 2020  y>=5,<6",..     
-000001b0: 2020 2022 6d73 616c 3e3d 312e 3135 2e30     "msal>=1.15.0
-000001c0: 2c3c 3222 2c0d 0a20 2020 2020 2020 2022  ,<2",..        "
-000001d0: 7061 6e64 6173 3e3d 312c 3c32 222c 0d0a  pandas>=1,<2",..
-000001e0: 2020 2020 2020 2020 2272 6571 7565 7374          "request
-000001f0: 7322 2c0d 0a20 2020 2020 2020 2022 6461  s",..        "da
-00000200: 7465 7061 7273 6572 3e3d 312c 3c32 220d  teparser>=1,<2".
-00000210: 0a20 2020 205d 2c0d 0a20 2020 2063 6c61  .    ],..    cla
-00000220: 7373 6966 6965 7273 3d5b 0d0a 2020 2020  ssifiers=[..    
-00000230: 2020 2020 2244 6576 656c 6f70 6d65 6e74      "Development
-00000240: 2053 7461 7475 7320 3a3a 2033 202d 2041   Status :: 3 - A
-00000250: 6c70 6861 222c 0d0a 2020 2020 2020 2020  lpha",..        
-00000260: 2249 6e74 656e 6465 6420 4175 6469 656e  "Intended Audien
-00000270: 6365 203a 3a20 4465 7665 6c6f 7065 7273  ce :: Developers
-00000280: 222c 0d0a 2020 2020 2020 2020 2254 6f70  ",..        "Top
-00000290: 6963 203a 3a20 536f 6674 7761 7265 2044  ic :: Software D
-000002a0: 6576 656c 6f70 6d65 6e74 203a 3a20 4c69  evelopment :: Li
-000002b0: 6272 6172 6965 7320 3a3a 2050 7974 686f  braries :: Pytho
-000002c0: 6e20 4d6f 6475 6c65 7322 2c0d 0a20 2020  n Modules",..   
-000002d0: 2020 2020 2022 4c69 6365 6e73 6520 3a3a       "License ::
-000002e0: 204f 5349 2041 7070 726f 7665 6420 3a3a   OSI Approved ::
-000002f0: 204d 4954 204c 6963 656e 7365 222c 0d0a   MIT License",..
-00000300: 2020 2020 2020 2020 2250 726f 6772 616d          "Program
-00000310: 6d69 6e67 204c 616e 6775 6167 6520 3a3a  ming Language ::
-00000320: 2050 7974 686f 6e22 2c0d 0a20 2020 2020   Python",..     
-00000330: 2020 2022 4f70 6572 6174 696e 6720 5379     "Operating Sy
-00000340: 7374 656d 203a 3a20 4f53 2049 6e64 6570  stem :: OS Indep
-00000350: 656e 6465 6e74 220d 0a20 2020 205d 0d0a  endent"..    ]..
-00000360: 290d 0a                                  )..
+000001b0: 2020 2022 706c 6f74 6c79 2d72 6573 616d     "plotly-resam
+000001c0: 706c 6572 222c 0d0a 2020 2020 2020 2020  pler",..        
+000001d0: 226d 7361 6c3e 3d31 2e31 352e 302c 3c32  "msal>=1.15.0,<2
+000001e0: 222c 0d0a 2020 2020 2020 2020 2270 616e  ",..        "pan
+000001f0: 6461 733e 3d31 2c3c 3222 2c0d 0a20 2020  das>=1,<2",..   
+00000200: 2020 2020 2022 7265 7175 6573 7473 222c       "requests",
+00000210: 0d0a 2020 2020 2020 2020 2264 6174 6570  ..        "datep
+00000220: 6172 7365 723e 3d31 2c3c 3222 0d0a 2020  arser>=1,<2"..  
+00000230: 2020 5d2c 0d0a 2020 2020 636c 6173 7369    ],..    classi
+00000240: 6669 6572 733d 5b0d 0a20 2020 2020 2020  fiers=[..       
+00000250: 2022 4465 7665 6c6f 706d 656e 7420 5374   "Development St
+00000260: 6174 7573 203a 3a20 3320 2d20 416c 7068  atus :: 3 - Alph
+00000270: 6122 2c0d 0a20 2020 2020 2020 2022 496e  a",..        "In
+00000280: 7465 6e64 6564 2041 7564 6965 6e63 6520  tended Audience 
+00000290: 3a3a 2044 6576 656c 6f70 6572 7322 2c0d  :: Developers",.
+000002a0: 0a20 2020 2020 2020 2022 546f 7069 6320  .        "Topic 
+000002b0: 3a3a 2053 6f66 7477 6172 6520 4465 7665  :: Software Deve
+000002c0: 6c6f 706d 656e 7420 3a3a 204c 6962 7261  lopment :: Libra
+000002d0: 7269 6573 203a 3a20 5079 7468 6f6e 204d  ries :: Python M
+000002e0: 6f64 756c 6573 222c 0d0a 2020 2020 2020  odules",..      
+000002f0: 2020 224c 6963 656e 7365 203a 3a20 4f53    "License :: OS
+00000300: 4920 4170 7072 6f76 6564 203a 3a20 4d49  I Approved :: MI
+00000310: 5420 4c69 6365 6e73 6522 2c0d 0a20 2020  T License",..   
+00000320: 2020 2020 2022 5072 6f67 7261 6d6d 696e       "Programmin
+00000330: 6720 4c61 6e67 7561 6765 203a 3a20 5079  g Language :: Py
+00000340: 7468 6f6e 222c 0d0a 2020 2020 2020 2020  thon",..        
+00000350: 224f 7065 7261 7469 6e67 2053 7973 7465  "Operating Syste
+00000360: 6d20 3a3a 204f 5320 496e 6465 7065 6e64  m :: OS Independ
+00000370: 656e 7422 0d0a 2020 2020 5d0d 0a29 0d0a  ent"..    ]..)..
```

