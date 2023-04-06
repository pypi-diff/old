# Comparing `tmp/gocart-0.1.7.tar.gz` & `tmp/gocart-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gocart-0.1.7.tar", last modified: Tue Apr  4 15:00:55 2023, max compression
+gzip compressed data, was "gocart-0.1.8.tar", last modified: Thu Apr  6 16:57:24 2023, max compression
```

## Comparing `gocart-0.1.7.tar` & `gocart-0.1.8.tar`

### file list

```diff
@@ -1,37 +1,37 @@
-drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-04 15:00:55.041435 gocart-0.1.7/
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      663 2023-04-04 14:56:01.000000 gocart-0.1.7/CHANGES.md
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)    35149 2023-04-04 14:56:01.000000 gocart-0.1.7/LICENSE
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      377 2023-04-04 14:56:01.000000 gocart-0.1.7/MANIFEST.in
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     4203 2023-04-04 15:00:55.041435 gocart-0.1.7/PKG-INFO
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     3638 2023-04-04 14:56:01.000000 gocart-0.1.7/README.md
-drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-04 15:00:55.029434 gocart-0.1.7/gocart/
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      189 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/__init__.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)       22 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/__version__.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     6521 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/cl_utils.py
-drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-04 15:00:55.037435 gocart-0.1.7/gocart/commonutils/
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      157 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/commonutils/__init__.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     1920 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/commonutils/flatten_healpix_map.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     2956 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/commonutils/generate_skymap_stats.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      358 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/commonutils/getpackagepath.py
-drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-04 15:00:55.041435 gocart-0.1.7/gocart/convert/
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      204 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/convert/__init__.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)    10998 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/convert/aitoff.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     3293 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/convert/ascii.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     6489 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/convert/healpix2cart.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     2236 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/default_settings.yaml
-drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-04 15:00:55.041435 gocart-0.1.7/gocart/parsers/
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)       56 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/parsers/__init__.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     6496 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/parsers/lvk.py
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     9654 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/setup.cfg
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     2003 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/test_settings.yaml
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     3387 2023-04-04 14:56:01.000000 gocart-0.1.7/gocart/utKit.py
-drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-04 15:00:55.037435 gocart-0.1.7/gocart.egg-info/
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     4203 2023-04-04 15:00:54.000000 gocart-0.1.7/gocart.egg-info/PKG-INFO
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      718 2023-04-04 15:00:54.000000 gocart-0.1.7/gocart.egg-info/SOURCES.txt
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)        1 2023-04-04 15:00:54.000000 gocart-0.1.7/gocart.egg-info/dependency_links.txt
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)       48 2023-04-04 15:00:54.000000 gocart-0.1.7/gocart.egg-info/entry_points.txt
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)        1 2023-04-04 14:59:49.000000 gocart-0.1.7/gocart.egg-info/not-zip-safe
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)      113 2023-04-04 15:00:54.000000 gocart-0.1.7/gocart.egg-info/requires.txt
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)        7 2023-04-04 15:00:54.000000 gocart-0.1.7/gocart.egg-info/top_level.txt
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)       38 2023-04-04 15:00:55.041435 gocart-0.1.7/setup.cfg
--rw-r--r--   0 jenkins   (1003) jenkins   (1004)     1933 2023-04-04 14:56:01.000000 gocart-0.1.7/setup.py
+drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-06 16:57:24.471863 gocart-0.1.8/
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      899 2023-04-06 16:52:44.000000 gocart-0.1.8/CHANGES.md
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)    35149 2023-04-06 16:52:44.000000 gocart-0.1.8/LICENSE
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      377 2023-04-06 16:52:44.000000 gocart-0.1.8/MANIFEST.in
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     5996 2023-04-06 16:57:24.467863 gocart-0.1.8/PKG-INFO
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     5430 2023-04-06 16:52:44.000000 gocart-0.1.8/README.md
+drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-06 16:57:24.467863 gocart-0.1.8/gocart/
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      189 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/__init__.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)       22 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/__version__.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     7204 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/cl_utils.py
+drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-06 16:57:24.467863 gocart-0.1.8/gocart/commonutils/
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      157 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/commonutils/__init__.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     1920 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/commonutils/flatten_healpix_map.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     2956 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/commonutils/generate_skymap_stats.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      358 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/commonutils/getpackagepath.py
+drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-06 16:57:24.467863 gocart-0.1.8/gocart/convert/
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      204 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/convert/__init__.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)    11081 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/convert/aitoff.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     3293 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/convert/ascii.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     6489 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/convert/healpix2cart.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     2236 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/default_settings.yaml
+drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-06 16:57:24.467863 gocart-0.1.8/gocart/parsers/
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)       56 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/parsers/__init__.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     6496 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/parsers/lvk.py
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     9654 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/setup.cfg
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     2003 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/test_settings.yaml
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     3387 2023-04-06 16:52:44.000000 gocart-0.1.8/gocart/utKit.py
+drwxr-xr-x   0 jenkins   (1003) jenkins   (1004)        0 2023-04-06 16:57:24.467863 gocart-0.1.8/gocart.egg-info/
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     5996 2023-04-06 16:57:24.000000 gocart-0.1.8/gocart.egg-info/PKG-INFO
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      718 2023-04-06 16:57:24.000000 gocart-0.1.8/gocart.egg-info/SOURCES.txt
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)        1 2023-04-06 16:57:24.000000 gocart-0.1.8/gocart.egg-info/dependency_links.txt
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)       48 2023-04-06 16:57:24.000000 gocart-0.1.8/gocart.egg-info/entry_points.txt
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)        1 2023-04-06 16:56:24.000000 gocart-0.1.8/gocart.egg-info/not-zip-safe
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)      113 2023-04-06 16:57:24.000000 gocart-0.1.8/gocart.egg-info/requires.txt
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)        7 2023-04-06 16:57:24.000000 gocart-0.1.8/gocart.egg-info/top_level.txt
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)       38 2023-04-06 16:57:24.471863 gocart-0.1.8/setup.cfg
+-rw-r--r--   0 jenkins   (1003) jenkins   (1004)     1934 2023-04-06 16:52:44.000000 gocart-0.1.8/setup.py
```

### Comparing `gocart-0.1.7/CHANGES.md` & `gocart-0.1.8/CHANGES.md`

 * *Files 22% similar despite different names*

```diff
@@ -1,12 +1,18 @@
 
 ## Release Notes
 
 <!-- **vx.x.x - xxdatexx** -->
 
+**v0.1.8 - April 6, 2023**
+
+- **FIXED** -- echo command now parses message to the end of the partition queue
+- **FIXED** -- listen command remembers where it left off
+- **FIXED** -- sun & moon coordinates ... they were not geocentric!
+
 **v0.1.7 - April 4, 2023**
 
 - **FIXED** -- unit test fix
 
 **v0.1.6 - April 4, 2023**
 
 - **ENHANCEMENT** -- added localisation type to aitoff maps
```

### Comparing `gocart-0.1.7/LICENSE` & `gocart-0.1.8/LICENSE`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/cl_utils.py` & `gocart-0.1.8/gocart/cl_utils.py`

 * *Files 9% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 # encoding: utf-8
 """
 Documentation for gocart can be found here: http://gocart.readthedocs.org
 
 Usage:
     gocart init
     gocart echo <daysAgo> [-s <pathToSettingsFile>]
-    gocart [-t] listen [-s <pathToSettingsFile>]
+    gocart listen [-s <pathToSettingsFile>]
 
 
 Options:
     init                                   setup the gocart settings file for the first time
     echo <daysAgo>                         relisten to alerts from N <daysAgo> until now and then exit
     listen                                 reconnect to kafka stream and listen from where you left off (or from now on if connectiong for the first time).
 
@@ -62,26 +62,29 @@
             varname = arg.replace("-", "") + "Flag"
         else:
             varname = arg.replace("<", "").replace(">", "")
         a[varname] = val
         log.debug('%s = %s' % (varname, val,))
 
     firstConnect = False
-    if "gcn-kafka" in settings and settings["gcn-kafka"]["group_id"] == "XXXX":
+    if "gcn-kafka" in settings and (not settings["gcn-kafka"]["group_id"] or len(str(settings["gcn-kafka"]["group_id"])) < 7):
 
+        from os.path import expanduser
         import uuid as pyuuid
+        import re
         group_id = pyuuid.uuid1().int
         settings["gcn-kafka"]["group_id"] = group_id
 
-        from os.path import expanduser
         home = expanduser("~")
         filepath = home + "/.config/gocart/gocart.yaml"
         import codecs
         with codecs.open(filepath, encoding='utf-8', mode='r') as readFile:
-            content = readFile.read().replace("group_id: XXXX", f"group_id: {group_id}")
+            content = readFile.read()
+            regex = re.compile(r'group_id\:.*')
+            content = regex.sub(f"group_id: {group_id}", content, count=1)
         with codecs.open(filepath, encoding='utf-8', mode='w') as writeFile:
             writeFile.write(content)
         firstConnect = True
     elif "gcn-kafka" not in settings:
         return
 
     ## START LOGGING ##
@@ -115,66 +118,82 @@
 
     # CALL FUNCTIONS/OBJECTS
     if a['listen']:
         from gcn_kafka import Consumer
         from confluent_kafka import TopicPartition
         from gocart.parsers import lvk
 
-        if firstConnect:
-            print("This is your first time using the listen command. gocart will now listen for all new incoming alerts. If you stop listening and restart sometime later, gocart will immediately collect all alerts missed while off-line.")
-            config = {'group.id': settings["gcn-kafka"]["group_id"],
-                      'enable.auto.commit': False}
-        else:
-            config = {'group.id': settings["gcn-kafka"]["group_id"],
-                      'auto.offset.reset': 'earliest',
-                      'enable.auto.commit': False}
+        config = {
+            'group.id': settings["gcn-kafka"]["group_id"],
+            'enable.auto.commit': False,
+            'auto.offset.reset': 'earliest'
+        }
 
         consumer = Consumer(config=config, client_id=settings['gcn-kafka']['client_id'],
                             client_secret=settings['gcn-kafka']['client_secret'], domain='gcn.nasa.gov')
         consumer.subscribe([topic])
 
         stop = False
+        test = 0
+        more = True
         while not stop:
-            for message in consumer.consume():
-
+            # IF FISRT TIME CONNECTING THEN SKIP MESSAGES
+            if firstConnect:
+                count = 0
+                print("Marking previous messages as read, this can take a few minutes ...")
+                while more:
+                    messages = consumer.consume(num_messages=300, timeout=10)
+
+                    for message in messages:
+                        count += 1
+                        consumer.commit(message)
+                    if not len(messages):
+                        more = False
+
+                firstConnect = False
+                print(f"This is your first time using the listen command. gocart will now listen for all new incoming alerts (skipping the {count} previous alerts currently in this topic). If you stop listening and restart sometime later, gocart will immediately collect all alerts missed while off-line.")
+            for message in consumer.consume(timeout=1):
                 parser = lvk(
                     log=log,
                     record=message.value(),
                     settings=settings
                 ).parse()
-
-                if a["testFlag"]:
-                    stop = True
+                consumer.commit(message)
 
     if a['echo'] and a['daysAgo']:
         # GET MESSAGES OCCURRING IN LAST N DAYS
         from gcn_kafka import Consumer
         from confluent_kafka import TopicPartition
         from gocart.parsers import lvk
         import datetime
 
         consumer = Consumer(client_id=settings['gcn-kafka']['client_id'],
                             client_secret=settings['gcn-kafka']['client_secret'], domain='gcn.nasa.gov')
 
-        nowInMicrosec = int((datetime.datetime.now()).timestamp() * 1000)
-        timestamp1 = int((datetime.datetime.now() - datetime.timedelta(days=float(a['daysAgo']))).timestamp() * 1000)
-        timestamp2 = nowInMicrosec - 3600000  # now minus 3 mins
+        since_utc = datetime.datetime.now() - datetime.timedelta(days=float(a['daysAgo']))
+        timestamp1 = int((since_utc).timestamp() * 1000)
+        since_utc = since_utc.strftime("%Y-%m-%d %H:%M:%S")
+        print(f"Echoing alerts since {since_utc} UTC")
 
         start = consumer.offsets_for_times(
             [TopicPartition(topic, 0, timestamp1)])
-        end = consumer.offsets_for_times(
-            [TopicPartition(topic, 0, timestamp2)])
 
         consumer.assign(start)
-        for message in consumer.consume(end[0].offset - start[0].offset):
-            parser = lvk(
-                log=log,
-                record=message.value(),
-                settings=settings
-            ).parse()
+
+        more = True
+        while more:
+            messages = consumer.consume(num_messages=1, timeout=10)
+            for message in messages:
+                parser = lvk(
+                    log=log,
+                    record=message.value(),
+                    settings=settings
+                ).parse()
+            if not len(messages):
+                more = False
 
     ## FINISH LOGGING ##
     endTime = times.get_now_sql_datetime()
     runningTime = times.calculate_time_difference(startTime, endTime)
     log.info('-- FINISHED ATTEMPT TO RUN THE cl_utils.py AT %s (RUNTIME: %s) --' %
              (endTime, runningTime, ))
```

### Comparing `gocart-0.1.7/gocart/commonutils/flatten_healpix_map.py` & `gocart-0.1.8/gocart/commonutils/flatten_healpix_map.py`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/commonutils/generate_skymap_stats.py` & `gocart-0.1.8/gocart/commonutils/generate_skymap_stats.py`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/convert/aitoff.py` & `gocart-0.1.8/gocart/convert/aitoff.py`

 * *Files 2% similar despite different names*

```diff
@@ -144,52 +144,55 @@
         ax.xaxis.set_major_formatter(ThetaFormatterShiftPi(30))
         ax.set_longitude_grid_ends(90)
 
         if daynight:
             t = Time(header['DATE-OBS'], scale='utc')
 
             # FIND SUN AND PLACE ON CORRECT PLOT COORDINATE
-            sun = get_sun(t).icrs
+            sun = get_sun(t)
             sun.ra.degree = -sun.ra.degree + 180
             if sun.ra.degree > 180.:
                 sun.ra.degree -= 360
             sun.ra.radian = np.deg2rad(sun.ra.degree)
 
             # COMPUTE LONS AND LATS OF DAY/NIGHT TERMINATOR.
             nlons = 1441
             nlats = ((nlons - 1) / 2) + 1
             lons, lats = terminator(sun.ra.radian, sun.dec.radian, nlons)
 
+            # for i, l in zip(lons, lats):
+            #     print(np.rad2deg(i), np.rad2deg(l))
+
             # DRAW THIN TERMINATOR LINE
             ax.plot(lons, lats, '#002b36', linewidth=0.3)
 
             # COLOR IN THE NIGHT
             lons2 = np.linspace(-np.pi, np.pi, nlons)
             lats2 = np.linspace(-np.pi / 2, np.pi / 2, int(nlats))
             lons2, lats2 = np.meshgrid(lons2, lats2)
             daynight = np.ones(lons2.shape)
             for nlon in range(nlons):
                 daynight[:, nlon] = np.where(lats2[:, nlon] < lats[nlon], 0, daynight[:, nlon])
-            ax.contourf(lons2, lats2, daynight, 1, colors=[(0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.2)], zorder=3)
+            ax.contourf(lons2, lats2, daynight, 1, colors=[(0.0, 0.0, 0.0, 0.2), (0.0, 0.0, 0.0, 0.0)], zorder=3)
 
         # PLOT THE SUN
         if sunmoon:
             t = Time(header['DATE-OBS'], scale='utc')
 
             # FIND SUN AND PLACE ON CORRECT PLOT COORDINATE
-            sun = get_sun(t).icrs
+            sun = get_sun(t)
             sun.ra.degree = -sun.ra.degree + 180
             if sun.ra.degree > 180.:
                 sun.ra.degree -= 360
             sun.ra.radian = np.deg2rad(sun.ra.degree)
 
             ax.scatter(sun.ra.radian, sun.dec.radian, color="#b58900", alpha=0.8, s=20, marker="o", edgecolors="#cb4b16", linewidths=0.5, label="Sun", zorder=30)
 
             # PLOT THE MOON
-            moon = get_moon(t).icrs
+            moon = get_moon(t)
             moon.ra.degree = -moon.ra.degree + 180
             if moon.ra.degree > 180.:
                 moon.ra.degree -= 360
             moon.ra.radian = np.deg2rad(moon.ra.degree)
             ax.scatter(moon.ra.radian, moon.dec.radian, color="#268bd2", alpha=0.8, s=20, marker="o", edgecolors="#1e6ea7", linewidths=0.5, label="Moon", zorder=29)
 
         handles, labels = plt.gca().get_legend_handles_labels()
```

### Comparing `gocart-0.1.7/gocart/convert/ascii.py` & `gocart-0.1.8/gocart/convert/ascii.py`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/convert/healpix2cart.py` & `gocart-0.1.8/gocart/convert/healpix2cart.py`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/default_settings.yaml` & `gocart-0.1.8/gocart/default_settings.yaml`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/parsers/lvk.py` & `gocart-0.1.8/gocart/parsers/lvk.py`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/setup.cfg` & `gocart-0.1.8/gocart/setup.cfg`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/test_settings.yaml` & `gocart-0.1.8/gocart/test_settings.yaml`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart/utKit.py` & `gocart-0.1.8/gocart/utKit.py`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/gocart.egg-info/SOURCES.txt` & `gocart-0.1.8/gocart.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gocart-0.1.7/setup.py` & `gocart-0.1.8/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -40,15 +40,15 @@
       version=__version__,
       description="Listen for, collect and convert multimessenger skymaps",
       long_description=readme(),
       long_description_content_type='text/markdown',
       classifiers=[
           'Development Status :: 4 - Beta',
           'License :: OSI Approved :: MIT License',
-          'Programming Language :: Python :: 3.7',
+          'Programming Language :: Python :: 3.11',
           'Topic :: Utilities',
       ],
       keywords=['astronomy'],
       url='https://github.com/thespacedoctor/gocart',
       download_url='https://github.com/thespacedoctor/gocart/archive/v%(__version__)s.zip' % locals(
       ),
       author='David Young',
```

