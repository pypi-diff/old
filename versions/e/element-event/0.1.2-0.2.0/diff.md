# Comparing `tmp/element-event-0.1.2.tar.gz` & `tmp/element-event-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "element-event-0.1.2.tar", last modified: Thu Oct 13 13:30:41 2022, max compression
+gzip compressed data, was "element-event-0.2.0.tar", last modified: Thu Apr  6 20:47:00 2023, max compression
```

## Comparing `element-event-0.1.2.tar` & `element-event-0.2.0.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 13:30:41.854532 element-event-0.1.2/
--rw-r--r--   0 runner    (1001) docker     (121)     1066 2022-10-13 13:30:39.000000 element-event-0.1.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     4177 2022-10-13 13:30:41.854532 element-event-0.1.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3811 2022-10-13 13:30:39.000000 element-event-0.1.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 13:30:41.854532 element-event-0.1.2/element_event/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-13 13:30:39.000000 element-event-0.1.2/element_event/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5647 2022-10-13 13:30:39.000000 element-event-0.1.2/element_event/event.py
--rw-r--r--   0 runner    (1001) docker     (121)     7718 2022-10-13 13:30:39.000000 element-event-0.1.2/element_event/trial.py
--rw-r--r--   0 runner    (1001) docker     (121)       46 2022-10-13 13:30:39.000000 element-event-0.1.2/element_event/version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 13:30:41.854532 element-event-0.1.2/element_event.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4177 2022-10-13 13:30:41.000000 element-event-0.1.2/element_event.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      307 2022-10-13 13:30:41.000000 element-event-0.1.2/element_event.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-13 13:30:41.000000 element-event-0.1.2/element_event.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       16 2022-10-13 13:30:41.000000 element-event-0.1.2/element_event.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       14 2022-10-13 13:30:41.000000 element-event-0.1.2/element_event.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-13 13:30:41.854532 element-event-0.1.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      948 2022-10-13 13:30:39.000000 element-event-0.1.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:47:00.769889 element-event-0.2.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-06 20:46:58.000000 element-event-0.2.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4177 2023-04-06 20:47:00.769889 element-event-0.2.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3811 2023-04-06 20:46:58.000000 element-event-0.2.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:47:00.765890 element-event-0.2.0/element_event/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:46:58.000000 element-event-0.2.0/element_event/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7083 2023-04-06 20:46:58.000000 element-event-0.2.0/element_event/event.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10704 2023-04-06 20:46:58.000000 element-event-0.2.0/element_event/trial.py
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-06 20:46:58.000000 element-event-0.2.0/element_event/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:47:00.769889 element-event-0.2.0/element_event.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4177 2023-04-06 20:47:00.000000 element-event-0.2.0/element_event.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      307 2023-04-06 20:47:00.000000 element-event-0.2.0/element_event.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:47:00.000000 element-event-0.2.0/element_event.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 20:47:00.000000 element-event-0.2.0/element_event.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 20:47:00.000000 element-event-0.2.0/element_event.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 20:47:00.769889 element-event-0.2.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-04-06 20:46:58.000000 element-event-0.2.0/setup.py
```

### Comparing `element-event-0.1.2/LICENSE` & `element-event-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `element-event-0.1.2/PKG-INFO` & `element-event-0.2.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: element-event
-Version: 0.1.2
+Version: 0.2.0
 Summary: DataJoint Elements for Trialized Experiments
 Home-page: https://github.com/datajoint/element-event
 Author: DataJoint
 Author-email: info@datajoint.com
 License: MIT
 Keywords: neuroscience behavior bpod trials datajoint
 Platform: UNKNOWN
```

### Comparing `element-event-0.1.2/README.md` & `element-event-0.2.0/README.md`

 * *Files identical despite different names*

### Comparing `element-event-0.1.2/element_event/event.py` & `element-event-0.2.0/element_event/event.py`

 * *Files 19% similar despite different names*

```diff
@@ -8,39 +8,42 @@
 
 _linking_module = None
 
 
 def activate(
     schema_name, *, create_schema=True, create_tables=True, linking_module=None
 ):
+    """Activate this schema.
+
+    Args:
+        schema_name (str): schema name on the database server
+        create_schema (bool): when True (default), create schema in the database if it
+                            does not yet exist.
+        create_tables (str): when True (default), create schema tables in the database
+                             if they do not yet exist.
+        linking_module (str): a module (or name) containing the required dependencies.
+
+    Dependencies:
+    Upstream tables:
+        Session: parent table to BehaviorRecording, identifying a recording session.
+        Project: the project with which experimental sessions are associated
+        Experimenter: the experimenter(s) participating in a given session
+                      To supply from element-lab add `Experimenter = lab.User`
+                      to your `workflow/pipeline.py` before `session.activate()`
+    Functions:
+        get_experiment_root_data_dir(): Retrieve the root data director(y/ies) with
+                                        behavioral recordings (e.g., bpod files) for
+                                        all subject/sessions, returns a string for
+                                        full path to the root data directory.
+        get_session_directory(session_key: dict): Retrieve the session directory
+                                                containing the recording(s) for a
+                                                given Session, returns a string for
+                                                full path to the session directory
     """
-    activate(schema_name, *, create_schema=True, create_tables=True,
-             linking_module=None)
-        :param schema_name: schema name on the database server to activate
-                            the `behavior` element
-        :param create_schema: when True (default), create schema in the
-                              database if it does not yet exist.
-        :param create_tables: when True (default), create tables in the
-                              database if they do not yet exist.
-        :param linking_module: a module (or name) containing the required
-                               dependencies to activate the `event` element:
-            Upstream tables:
-                + Session: parent table to BehaviorRecording, typically
-                           identifying a recording session.
-            Functions:
-                + get_experiment_root_data_dir() -> list
-                    Retrieve the root data director(y/ies) with behavioral
-                    recordings (e.g., bpod files) for all subject/sessions.
-                    :return: a string for full path to the root data directory
-                + get_session_directory(session_key: dict) -> str
-                    Retrieve the session directory containing the recording(s)
-                    for a given Session
-                    :param session_key: a dictionary of one Session `key`
-                    :return: a string for full path to the session directory
-    """
+
     if isinstance(linking_module, str):
         linking_module = importlib.import_module(linking_module)
     assert inspect.ismodule(linking_module), (
         "The argument 'dependency' must" + " be a module or module name"
     )
 
     schema.activate(
@@ -51,103 +54,142 @@
     )
 
 
 # -------------- Functions required by the element-trial   ---------------
 
 
 def get_experiment_root_data_dir() -> list:
-    """
-    All data paths, directories in DataJoint Elements are recommended to be
-    stored as relative paths, with respect to some user-configured "root"
-    directory, which varies from machine to machine
-
-    get_experiment_root_data_dir() -> list
-        This user-provided function retrieves the list of possible root data
-        directories containing the behavioral data for all subjects/sessions
-        :return: a string for full path to the behavioral root data directory,
-         or list of strings for possible root data directories
+    """Pulls relevant func from parent namespace to specify root data dir(s).
+
+    It is recommended that all paths in DataJoint Elements stored as relative
+    paths, with respect to some user-configured "root" director(y/ies). The
+    root(s) may vary between data modalities and user machines. Returns a
+    full path string to behavioral root data directory or list of strings
+    for possible root data directories.
+
+    Returns:
+        Paths (list): List of path(s) to root directories for event data
     """
     return _linking_module.get_experiment_root_data_dir()
 
 
 def get_session_directory(session_key: dict) -> str:
+    """Pulls relative function from parent namespace.
+
+    Retrieves the session directory containing the recorded data for a given
+    Session. Returns a string for full path to the session directory.
+
+    Returns:
+        Session_dir (str): Relative path to session directory
     """
-    get_session_directory(session_key: dict) -> str
-        Retrieve the session directory containing the
-         recorded data for a given Session
-        :param session_key: a dictionary of one Session `key`
-        :return: a string for full path to the session directory
-    """
+
     return _linking_module.get_session_directory(session_key)
 
 
 # ----------------------------- Table declarations ----------------------
 
 
 @schema
 class EventType(dj.Lookup):
+    """Set of unique events present within a recording session
+
+    Attributes:
+        event_type ( varchar(16) ): Unique event type.
+        event_type_description ( varchar(256) ): Event type description.
+    """
+
     definition = """
     event_type                : varchar(16)
     ---
     event_type_description='' : varchar(256)
     """
 
 
 @schema
 class BehaviorRecording(dj.Manual):
+    """Behavior Recordings
+
+    Attributes:
+        Session (foreign key): Session primary key.
+        recording_start_time (datetime): Start time of recording.
+        recording_duration (float): Duration of recording.
+        recording_notes ( varchar(256) ): Optional recording related notes.
+    """
+
     definition = """
     -> Session
     ---
     recording_start_time=null : datetime
     recording_duration=null   : float
     recording_notes=''     : varchar(256)
     """
 
     class File(dj.Part):
+        """File IDs and paths associated with a behavior recording
+
+        Attributes:
+            BehaviorRecording (foreign key): Behavior recording primary key.
+            filepath ( varchar(64) ): file path of video, relative to root data dir.
+        """
+
         definition = """
         -> master
         filepath              : varchar(64)
         """
 
 
 @schema
 class Event(dj.Imported):
+    """Automated table with event related information
+
+    WRT: With respect to
+
+    Attributes:
+        BehaviorRecording (foreign key): Behavior recording primary key.
+        EventType (foreign key): EventType primary key.
+        event_start_time (decimal(10, 4)): Time of event onset in seconds, WRT recording start.
+        event_end_time (float): Optional. Seconds WRT recording start.
+    """
+
     definition = """
     -> BehaviorRecording
     -> EventType
-    event_start_time          : float  # (second) relative to recording start
+    event_start_time          : decimal(10, 4)  # (second) relative to recording start
     ---
     event_end_time=null       : float  # (second) relative to recording start
     """
 
     def make(self, key):
+        """Populate based on unique entries in BehaviorRecording and EventType."""
         raise NotImplementedError("For `insert`, use `allow_direct_insert=True`")
 
 
-"""
------ AlignmentEvent -----
-- The following `AlignmentEvent` table is designed to provide a mechanism for performing
-event-aligned analyses, such as Peristimulus Time Histogram (PSTH) analysis commonly
-used in electrophysiology studies.
-- One entry in the `AlignmentEvent` table defines an
-event type to align signal/activity timeseries to. 
-- Start and end event types define the beginning and end of a data window
-- time_shift is seconds of adjustment with respect to the alignment variable, or the beginning/end of the window via start/end event types.
-- To use entries from trial.Trial, trial_start_time and trial_end_time must be entered in
-the Event table.
-"""
-
-
 @schema
 class AlignmentEvent(dj.Manual):
+    """Table designed to provide a mechanism for performing event-aligned analyses
+
+    To use entries from trial.Trial, trial_start_time and trial_end_time must be entered
+    in the Event table. WRT = With respect to
+
+    Attributes
+        alignment_name ( varchar(32) ): Unique alignment name.
+        alignment_description ( varchar(1000) ): Optional. Longer description.
+        alignment_event_type (foreign key): Event type to align to.
+        alignment_time_shift (float): Seconds WRT alignment_event_type
+        start_event_type (foreign key): Event before alignment event type
+        start_time_shift (float): Seconds WRT start_event_type
+        end_event_type (foreign key): Event after alignment event type
+        end_time_shift (float): Seconds WRT end_event_type
+
+    """
+
     definition = """ # time_shift is seconds to shift with respect to (WRT) a variable
     alignment_name: varchar(32)
     ---
     alignment_description='': varchar(1000)  
     -> EventType.proj(alignment_event_type='event_type') # event type to align to
     alignment_time_shift: float                      # (s) WRT alignment_event_type
     -> EventType.proj(start_event_type='event_type') # event before alignment_event_type
     start_time_shift: float                          # (s) WRT start_event_type
     -> EventType.proj(end_event_type='event_type')   # event after alignment_event_type
     end_time_shift: float                            # (s) WRT end_event_type
     """
-    # WRT - with respect to
```

### Comparing `element-event-0.1.2/element_event/trial.py` & `element-event-0.2.0/element_event/trial.py`

 * *Files 25% similar despite different names*

```diff
@@ -15,30 +15,40 @@
     trial_schema_name,
     event_schema_name,
     *,
     create_schema=True,
     create_tables=True,
     linking_module=None,
 ):
-    """
-    activate(trial_schema_name, event_schema_name, *, create_schema=True,
-             create_tables=True, linking_module=None)
-        :param trial_schema_name: schema name on the database server to activate
-                            the `trial` element
-        :param event_schema_name: schema name on the database server to activate
-                            the `event` element
-        :param create_schema: when True (default), create schema in the
-                              database if it does not yet exist.
-        :param create_tables: when True (default), create tables in the
-                              database if they do not yet exist.
-        :param linking_module: a module (or name) containing the required
-                               dependencies to activate the `trial` element:
-        Upstream tables:
-            + Session: parent table to BehaviorRecording, typically
-                       identifying a recording session.
+    """Activate this schema.
+
+    Args:
+        trial_schema_name (str): schema name on the database server to activate the
+                                 `trial` element
+        event_schema_name (str): schema name on the database server to activate the
+                                 `event` element
+        create_schema (bool): when True (default), create schema in the database if it
+                            does not yet exist.
+        create_tables (str): when True (default), create schema tables in the database
+                             if they do not yet exist.
+        linking_module (str): a module (or name) containing the required dependencies
+                              to activate the `trial` element
+
+    Dependencies:
+    Upstream tables:
+        Session: parent table to BehaviorRecording, identifying a recording session.
+
+    Functions:
+        get_trialized_alignment_event_times(alignment_event_key: dict, trial_restriction:
+                                            dict): For the trials identified by
+                                            trial_restriction, identify recording times
+                                            with respect to a given alignment_event.
+                                            Returns pandas dataframe with trial_key,
+                                            start (recording time), event (recording time),
+                                            and end (recording time).
     """
     if isinstance(linking_module, str):
         linking_module = importlib.import_module(linking_module)
     assert inspect.ismodule(linking_module), (
         "The argument 'dependency' must" + " be a module or module name"
     )
 
@@ -61,106 +71,173 @@
 
 
 # ----------------------------- Table declarations ----------------------
 
 
 @schema
 class Block(dj.Imported):
+    """Set of experimental blocks within a recording session
+
+    Attributes
+        event.BehaviorRecording (foreign key): event.BehaviorRecording primary key.
+        block_id (smallint): block number (1-based indexing)
+        block_start_time (float): Seconds relative to recording start
+        block_stop_time (float): Seconds relative to recording stop
+    """
+
     definition = """ # Experimental blocks
     -> event.BehaviorRecording
     block_id               : smallint # block number (1-based indexing)
     ---
     block_start_time       : float     # (s) relative to recording start
-    block_stop_time        : float     # (s) relative to recording start
+    block_stop_time        : float     # (s) relative to recording stop
     """
 
     class Attribute(dj.Part):
+        """Extra Block attributes to fully describe a block
+
+        Attributes:
+             Block (foreign key): Block table primary key. 
+             attribute_name ( varchar(32) ): Name of block attribute
+             attribute_value ( varchar(2000) ): Optional. Block attribute value
+             attribute_blob (longblob): Optional. Block attribute numerical numerical data
+        """
+
         definition = """  # Additional block attributes to fully describe a block
         -> master
         attribute_name    : varchar(32)
         ---
         attribute_value='': varchar(2000)
         attribute_blob=null: longblob
-        """   
+        """
 
     def make(self, key):
+        """Populate each unique entry in event.BehaviorRecording"""
         raise NotImplementedError("For `insert`, use `allow_direct_insert=True`")
 
 
 @schema
 class TrialType(dj.Lookup):
+    """Set of unique trial types present within a recording session
+
+    Attributes:
+        trial_type ( varchar(16) ): Name of trial type
+        trial_type_description ( varchar(256) ): Optional. Long Description.
+    """
+
     definition = """
     trial_type                : varchar(16)
     ---
     trial_type_description='' : varchar(256)
     """
 
 
 @schema
 class Trial(dj.Imported):
+    """Set of all experimental trials from a behavioral recording
+
+    Attributes:
+        event.BehaviorRecording (foreign key): BehaviorRecording primary key
+        trial_id (smallint): trial number (1-based indexing)
+        TrialType (foreign key): Optional. TrialType primary key
+        trial_start_time (float): Seconds relative to recording start
+        trial_stop_time (float): Seconds relative to recording stop
+    """
+
     definition = """  # Experimental trials
     -> event.BehaviorRecording
     trial_id            : smallint # trial number (1-based indexing)
     ---
     -> [nullable] TrialType
     trial_start_time    : float  # (second) relative to recording start
-    trial_stop_time     : float  # (second) relative to recording start
+    trial_stop_time     : float  # (second) relative to recording stop
     """
 
     class Attribute(dj.Part):
+        """Extra trial attributes to fully describe a trial
+
+        Attributes:
+            Trial (foreign key): Trial table primary key.
+            attribute_name ( varchar(32) ): Name of trial attribute
+            attribute_value ( varchar(2000) ): Optional. Trial attribute value
+            attribute_blob (longblob): Optional. Trial attribute numerical data
+        """
+
         definition = """  # Additional trial attributes to fully describe a trial
         -> master
         attribute_name  : varchar(32)
         ---
         attribute_value='': varchar(2000)
         attribute_blob=null: longblob
-        """   
+        """
 
     def make(self, key):
+        """Populate for each unique entry in event.BehaviorRecording"""
         raise NotImplementedError("For `insert`, use `allow_direct_insert=True`")
 
 
 @schema
 class BlockTrial(dj.Imported):
+    """Set of trials associated with certain blocks
+
+    Attributes:
+        Block (foreign key): Block primary key
+        Trial (foreign key): Trial primary key
+    """
+
     definition = """
     -> Block
     -> Trial
-    """    
-    
+    """
+
     def make(self, key):
+        """Populate for each unique entry in Trial and Block"""
         raise NotImplementedError("For `insert`, use `allow_direct_insert=True`")
 
 
 @schema
 class TrialEvent(dj.Imported):
+    """Set of trials associated with certain events
+
+    Attributes:
+        Block (foreign key): Block primary key
+        event.Event (foreign key): event.Event primary key
+    """
+
     definition = """
     -> Trial
     -> event.Event
     """
 
     def make(self, key):
+        """Populate for each unique entry in Trial and event.Event"""
         raise NotImplementedError("For `insert`, use `allow_direct_insert=True`")
 
 
-# ---- HELPER ----
+# ---- HELPER Functions ----
 
 
 def get_trialized_alignment_event_times(alignment_event_key, trial_restriction):
-    """
-    For the trials identified by trial_restriction, identify recording times with 
-        with respect to a given alignment_event. 
-    :param alignment_event_key: key including information from event.AlignmentEvent
-    :param trial_restriction: set or subset of trials from trial.Trial
-    
-    returns pandas dataframe with each of the following
-        trial_key: key identifying a single trial
-        start: recording time (s) of the beginning of an alignment window
-        event: recording time (s) of an alignment event within the trial. 
-               If multiple events within a trial, select the last one.
-        end:  recording time (s) of the end of an alignment window
+    """For the trials in trial_restriction, identify times WRT a given alignment_event.
+
+    WRT = With respect to
+
+    Args:
+        alignment_event_key (dict): key including information from event.AlignmentEvent
+        trial_restriction (dict): set or subset of trials from trial.Trial
+
+    Returns:
+        dataset (pandas): Dataframe with each of the items listed below.
+
+    Dataset:
+        trial_key (dict): key identifying a single trial \n
+        start (float): recording time (s) of the beginning of an alignment window \n
+        event (float): recording time (s) of an alignment event within the trial.
+            If multiple events within a trial, select the last one\n
+        end  (float): recording time (s) of the end of an alignment window
     """
 
     import pandas as pd
 
     session_key = (_linking_module.Session & trial_restriction).fetch1("KEY")
     trial_keys, trial_starts, trial_ends = (Trial ^ trial_restriction).fetch(
         "KEY", "trial_start_time", "trial_stop_time", order_by="trial_id"
```

### Comparing `element-event-0.1.2/element_event.egg-info/PKG-INFO` & `element-event-0.2.0/element_event.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: element-event
-Version: 0.1.2
+Version: 0.2.0
 Summary: DataJoint Elements for Trialized Experiments
 Home-page: https://github.com/datajoint/element-event
 Author: DataJoint
 Author-email: info@datajoint.com
 License: MIT
 Keywords: neuroscience behavior bpod trials datajoint
 Platform: UNKNOWN
```

### Comparing `element-event-0.1.2/setup.py` & `element-event-0.2.0/setup.py`

 * *Files identical despite different names*

