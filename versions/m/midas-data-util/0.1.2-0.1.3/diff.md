# Comparing `tmp/midas-data-util-0.1.2.tar.gz` & `tmp/midas-data-util-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "midas-data-util-0.1.2.tar", last modified: Fri Apr  7 09:09:29 2023, max compression
+gzip compressed data, was "midas-data-util-0.1.3.tar", last modified: Fri Apr  7 11:11:19 2023, max compression
```

## Comparing `midas-data-util-0.1.2.tar` & `midas-data-util-0.1.3.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.177409 midas-data-util-0.1.2/
--rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.2/LICENSE
--rw-rw-rw-   0        0        0      520 2023-04-07 09:09:29.176404 midas-data-util-0.1.2/PKG-INFO
--rw-rw-rw-   0        0        0      116 2023-04-07 08:58:48.000000 midas-data-util-0.1.2/README.md
--rw-rw-rw-   0        0        0      489 2023-04-07 09:08:55.000000 midas-data-util-0.1.2/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 09:09:29.177409 midas-data-util-0.1.2/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.141584 midas-data-util-0.1.2/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.156545 midas-data-util-0.1.2/src/midas/
--rw-rw-rw-   0        0        0     2032 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/__init__.py
--rw-rw-rw-   0        0        0     5817 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/data_encoder.py
--rw-rw-rw-   0        0        0     5445 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/event.py
--rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.2/src/midas/playfab.py
--rw-rw-rw-   0        0        0     7436 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/session.py
--rw-rw-rw-   0        0        0     3218 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/user.py
-drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.174409 midas-data-util-0.1.2/src/midas_data_util.egg-info/
--rw-rw-rw-   0        0        0      520 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      331 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        6 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 11:11:19.899156 midas-data-util-0.1.3/
+-rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.3/LICENSE
+-rw-rw-rw-   0        0        0      520 2023-04-07 11:11:19.886935 midas-data-util-0.1.3/PKG-INFO
+-rw-rw-rw-   0        0        0      116 2023-04-07 08:58:48.000000 midas-data-util-0.1.3/README.md
+-rw-rw-rw-   0        0        0      489 2023-04-07 11:10:36.000000 midas-data-util-0.1.3/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 11:11:19.899156 midas-data-util-0.1.3/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 11:11:19.801974 midas-data-util-0.1.3/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 11:11:19.819635 midas-data-util-0.1.3/src/midas/
+-rw-rw-rw-   0        0        0     1975 2023-04-07 11:10:36.000000 midas-data-util-0.1.3/src/midas/__init__.py
+-rw-rw-rw-   0        0        0     5817 2023-04-07 08:19:44.000000 midas-data-util-0.1.3/src/midas/data_encoder.py
+-rw-rw-rw-   0        0        0     5445 2023-04-07 08:19:44.000000 midas-data-util-0.1.3/src/midas/event.py
+-rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.3/src/midas/playfab.py
+-rw-rw-rw-   0        0        0     7436 2023-04-07 08:19:44.000000 midas-data-util-0.1.3/src/midas/session.py
+-rw-rw-rw-   0        0        0     3218 2023-04-07 08:19:44.000000 midas-data-util-0.1.3/src/midas/user.py
+drwxrwxrwx   0        0        0        0 2023-04-07 11:11:19.868609 midas-data-util-0.1.3/src/midas_data_util.egg-info/
+-rw-rw-rw-   0        0        0      520 2023-04-07 11:11:19.000000 midas-data-util-0.1.3/src/midas_data_util.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      331 2023-04-07 11:11:19.000000 midas-data-util-0.1.3/src/midas_data_util.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 11:11:19.000000 midas-data-util-0.1.3/src/midas_data_util.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 11:11:19.000000 midas-data-util-0.1.3/src/midas_data_util.egg-info/top_level.txt
```

### Comparing `midas-data-util-0.1.2/LICENSE` & `midas-data-util-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.2/PKG-INFO` & `midas-data-util-0.1.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: midas-data-util
-Version: 0.1.2
+Version: 0.1.3
 Summary: a package with useful functions for downloading and working with midas generated analytics data
 Author-email: nightcycle <coyer@nightcycle.us>
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `midas-data-util-0.1.2/src/midas/__init__.py` & `midas-data-util-0.1.3/src/midas/__init__.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,16 +1,13 @@
 import pandas as pd
 from pandas import DataFrame
 from typing import Any
-from event import Event, EventDumpData
-from session import Session, SessionDumpData
-from user import User, UserDumpData
-import event as event_class
-import session as session_class
-import user as user_class
+from .event import Event, get_events_from_df
+from .session import Session, SessionDumpData,  get_sessions_from_events, get_survival_rate
+from .user import User, UserDumpData, get_users_from_session_list
 
 def dump(objects: list[Event] | list[Session] | list[User]):
 	untyped_objects: Any = objects
 	object_count = len(objects)
 	if type(objects[0]) == Event:
 		event_list: list[Event] = untyped_objects
 		event_data_list: list[Any] = []
@@ -34,23 +31,23 @@
 		return user_df	
 	
 
 	
 def load(decoded_df: DataFrame) -> tuple[list[Event], list[Session], list[User]]:
 
 	print("assembling events")
-	events = event_class.get_events_from_df(decoded_df)
+	events = get_events_from_df(decoded_df)
 
 	print("assembling sessions")
-	sessions = session_class.get_sessions_from_events(events)
+	sessions = get_sessions_from_events(events)
 	
 	print("assembling users")
-	users = user_class.get_users_from_session_list(sessions)
+	users = get_users_from_session_list(sessions)
 	
-	survival_rate = session_class.get_survival_rate(sessions)
+	survival_rate = get_survival_rate(sessions)
 
 	print("event survival rate: "+str(round(survival_rate*100000)/1000)+"%")
 
 	final_sessions: list[Session] = []
 	for user in users:
 		for session in user.sessions:
 			final_sessions.append(session)
```

### Comparing `midas-data-util-0.1.2/src/midas/data_encoder.py` & `midas-data-util-0.1.3/src/midas/data_encoder.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.2/src/midas/event.py` & `midas-data-util-0.1.3/src/midas/event.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.2/src/midas/playfab.py` & `midas-data-util-0.1.3/src/midas/playfab.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.2/src/midas/session.py` & `midas-data-util-0.1.3/src/midas/session.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.2/src/midas/user.py` & `midas-data-util-0.1.3/src/midas/user.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.2/src/midas_data_util.egg-info/PKG-INFO` & `midas-data-util-0.1.3/src/midas_data_util.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: midas-data-util
-Version: 0.1.2
+Version: 0.1.3
 Summary: a package with useful functions for downloading and working with midas generated analytics data
 Author-email: nightcycle <coyer@nightcycle.us>
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

