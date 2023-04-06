# Comparing `tmp/gcal-sync-4.1.2.tar.gz` & `tmp/gcal-sync-4.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gcal-sync-4.1.2.tar", last modified: Tue Jan 10 17:05:56 2023, max compression
+gzip compressed data, was "gcal-sync-4.1.3.tar", last modified: Thu Apr  6 19:36:16 2023, max compression
```

## Comparing `gcal-sync-4.1.2.tar` & `gcal-sync-4.1.3.tar`

### file list

```diff
@@ -1,23 +1,30 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 17:05:56.234603 gcal-sync-4.1.2/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3899 2023-01-10 17:05:56.234603 gcal-sync-4.1.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3496 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 17:05:56.230603 gcal-sync-4.1.2/gcal_sync/
--rw-r--r--   0 runner    (1001) docker     (123)      144 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    23248 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     6468 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/const.py
--rw-r--r--   0 runner    (1001) docker     (123)      544 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    22936 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/model.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)     1813 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/store.py
--rw-r--r--   0 runner    (1001) docker     (123)     6944 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/sync.py
--rw-r--r--   0 runner    (1001) docker     (123)     4944 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/gcal_sync/timeline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 17:05:56.234603 gcal-sync-4.1.2/gcal_sync.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3899 2023-01-10 17:05:56.000000 gcal-sync-4.1.2/gcal_sync.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      417 2023-01-10 17:05:56.000000 gcal-sync-4.1.2/gcal_sync.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-10 17:05:56.000000 gcal-sync-4.1.2/gcal_sync.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-01-10 17:05:56.000000 gcal-sync-4.1.2/gcal_sync.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-10 17:05:56.000000 gcal-sync-4.1.2/gcal_sync.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      855 2023-01-10 17:05:56.234603 gcal-sync-4.1.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-01-10 17:05:44.000000 gcal-sync-4.1.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 19:36:16.840063 gcal-sync-4.1.3/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3899 2023-04-06 19:36:16.840063 gcal-sync-4.1.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3496 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 19:36:16.840063 gcal-sync-4.1.3/gcal_sync/
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23258 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6468 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/const.py
+-rw-r--r--   0 runner    (1001) docker     (123)      544 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23593 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)     1813 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/store.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6944 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/sync.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4944 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/gcal_sync/timeline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 19:36:16.840063 gcal-sync-4.1.3/gcal_sync.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3899 2023-04-06 19:36:16.000000 gcal-sync-4.1.3/gcal_sync.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      536 2023-04-06 19:36:16.000000 gcal-sync-4.1.3/gcal_sync.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 19:36:16.000000 gcal-sync-4.1.3/gcal_sync.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-04-06 19:36:16.000000 gcal-sync-4.1.3/gcal_sync.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 19:36:16.000000 gcal-sync-4.1.3/gcal_sync.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      783 2023-04-06 19:36:16.840063 gcal-sync-4.1.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 19:36:16.840063 gcal-sync-4.1.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)    26084 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/tests/test_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7871 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/tests/test_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24081 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/tests/test_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2076 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/tests/test_store.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29841 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/tests/test_sync.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34976 2023-04-06 19:36:02.000000 gcal-sync-4.1.3/tests/test_timeline.py
```

### Comparing `gcal-sync-4.1.2/LICENSE` & `gcal-sync-4.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `gcal-sync-4.1.2/PKG-INFO` & `gcal-sync-4.1.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gcal-sync
-Version: 4.1.2
+Version: 4.1.3
 Summary: A python library for syncing Google Calendar to local storage
 Home-page: https://github.com/allenporter/gcal_sync
 Author: Allen Porter
 Author-email: allen.porter@gmail.com
 License: Apache-2.0
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.9
```

### Comparing `gcal-sync-4.1.2/README.md` & `gcal-sync-4.1.3/README.md`

 * *Files identical despite different names*

### Comparing `gcal-sync-4.1.2/gcal_sync/api.py` & `gcal-sync-4.1.3/gcal_sync/api.py`

 * *Files 0% similar despite different names*

```diff
@@ -448,15 +448,15 @@
 
         allow_population_by_field_name = True
 
 
 class LocalListEventsResponse(BaseModel):
     """Api response containing a list of events."""
 
-    events: List[Event] = Field(default=[])
+    events: List[Event] = Field(default_factory=list)
     """Events returned from the local store."""
 
 
 class CalendarListStoreService:
     """Performs calendar list lookups from the local store."""
 
     def __init__(self, store: CalendarStore) -> None:
```

### Comparing `gcal-sync-4.1.2/gcal_sync/auth.py` & `gcal-sync-4.1.3/gcal_sync/auth.py`

 * *Files identical despite different names*

### Comparing `gcal-sync-4.1.2/gcal_sync/exceptions.py` & `gcal-sync-4.1.3/gcal_sync/exceptions.py`

 * *Files identical despite different names*

### Comparing `gcal-sync-4.1.2/gcal_sync/model.py` & `gcal-sync-4.1.3/gcal_sync/model.py`

 * *Files 2% similar despite different names*

```diff
@@ -72,18 +72,18 @@
 
     id: str
     """Identifier of the calendar."""
 
     summary: str = ""
     """Title of the calendar."""
 
-    description: Optional[str]
+    description: Optional[str] = None
     """Description of the calendar."""
 
-    location: Optional[str]
+    location: Optional[str] = None
     """Geographic location of the calendar as free-form text."""
 
     timezone: Optional[str] = Field(alias="timeZone", default=None)
     """The time zone of the calendar."""
 
     access_role: AccessRole = Field(alias="accessRole")
     """The effective access role that the authenticated user has on the calendar."""
@@ -105,18 +105,18 @@
 
     id: str
     """Identifier of the calendar."""
 
     summary: str = ""
     """Title of the calendar."""
 
-    description: Optional[str]
+    description: Optional[str] = None
     """Description of the calendar."""
 
-    location: Optional[str]
+    location: Optional[str] = None
     """Geographic location of the calendar as free-form text."""
 
     timezone: Optional[str] = Field(alias="timeZone", default=None)
     """The time zone of the calendar."""
 
     class Config:
         """Pydnatic model configuration."""
@@ -445,18 +445,18 @@
 
     start: DateOrDatetime
     """The (inclusive) start time of the event."""
 
     end: DateOrDatetime
     """The (exclusive) end time of the event."""
 
-    description: Optional[str]
+    description: Optional[str] = None
     """Description of the event, which can contain HTML."""
 
-    location: Optional[str]
+    location: Optional[str] = None
     """Geographic location of the event as free-form text."""
 
     transparency: str = Field(default="opaque")
     """Whether the event blocks time on the calendar.
 
     Will either be `opaque` which means the calendar does block time on the
     calendar or `transparent` which means it does not block time on the calendar.
@@ -533,14 +533,30 @@
         """Remove rrule property parameters not supported by the dateutil.rrule library."""
         if not values.get("recurrence"):
             return values
         values["recur"] = Recurrence.from_recurrence(values["recurrence"])
         return values
 
     @root_validator
+    def _adjust_duration(cls, values: dict[str, Any]) -> dict[str, Any]:
+        """Fix events with invalid durations."""
+        _LOGGER.debug("_adjust_duration")
+        if (
+            (dtstart := values.get("start"))
+            and (dtend := values.get("end"))
+            and dtstart.date
+            and dtend.date
+            and ((dtend.date - dtstart.date) <= datetime.timedelta(days=0))
+        ):
+            # Duration is zero or negative. Default to 1 day
+            dtend.date = dtstart.date + datetime.timedelta(days=1)
+            values["end"] = dtend
+        return values
+
+    @root_validator
     def _validate_rrule(cls, values: dict[str, Any]) -> dict[str, Any]:
         """The API returns invalid RRULEs that need to be coerced to valid."""
         # Rules may need updating of start time has a timezone
         if not (recur := values.get("recur")) or not (dtstart := values.get("start")):
             return values
         for rule in recur.rrule:
             cls._adjust_rrule(rule, dtstart)
```

### Comparing `gcal-sync-4.1.2/gcal_sync/store.py` & `gcal-sync-4.1.3/gcal_sync/store.py`

 * *Files identical despite different names*

### Comparing `gcal-sync-4.1.2/gcal_sync/sync.py` & `gcal-sync-4.1.3/gcal_sync/sync.py`

 * *Files identical despite different names*

### Comparing `gcal-sync-4.1.2/gcal_sync/timeline.py` & `gcal-sync-4.1.3/gcal_sync/timeline.py`

 * *Files identical despite different names*

### Comparing `gcal-sync-4.1.2/gcal_sync.egg-info/PKG-INFO` & `gcal-sync-4.1.3/gcal_sync.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gcal-sync
-Version: 4.1.2
+Version: 4.1.3
 Summary: A python library for syncing Google Calendar to local storage
 Home-page: https://github.com/allenporter/gcal_sync
 Author: Allen Porter
 Author-email: allen.porter@gmail.com
 License: Apache-2.0
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.9
```

