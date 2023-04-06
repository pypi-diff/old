# Comparing `tmp/lg_april_permissions-0.1.6.tar.gz` & `tmp/lg_april_permissions-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lg_april_permissions-0.1.6.tar", max compression
+gzip compressed data, was "lg_april_permissions-0.1.7.tar", max compression
```

## Comparing `lg_april_permissions-0.1.6.tar` & `lg_april_permissions-0.1.7.tar`

### file list

```diff
@@ -1,4 +1,4 @@
--rw-r--r--   0        0        0     6891 2023-04-05 13:50:30.283574 lg_april_permissions-0.1.6/README.md
--rw-r--r--   0        0        0     7708 2023-04-05 16:02:32.863644 lg_april_permissions-0.1.6/lg_april_permissions/__init__.py
--rw-r--r--   0        0        0      571 2023-04-05 16:07:10.048268 lg_april_permissions-0.1.6/pyproject.toml
--rw-r--r--   0        0        0     7442 1970-01-01 00:00:00.000000 lg_april_permissions-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0     6891 2023-04-05 13:50:30.283574 lg_april_permissions-0.1.7/README.md
+-rw-r--r--   0        0        0     8044 2023-04-06 09:57:54.237981 lg_april_permissions-0.1.7/lg_april_permissions/__init__.py
+-rw-r--r--   0        0        0      753 2023-04-06 09:58:49.374643 lg_april_permissions-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0     7442 1970-01-01 00:00:00.000000 lg_april_permissions-0.1.7/PKG-INFO
```

### Comparing `lg_april_permissions-0.1.6/README.md` & `lg_april_permissions-0.1.7/README.md`

 * *Files identical despite different names*

### Comparing `lg_april_permissions-0.1.6/lg_april_permissions/__init__.py` & `lg_april_permissions-0.1.7/lg_april_permissions/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -70,19 +70,19 @@
     def index():
         return f"This is the buditool (version: {__version__}): https://git.itsnow.biz/kamille/buditool", 200
 
     @app.route("/sync")
     def sync():
         print("Webhook called")
         #Thread(target=sync_db_permissions).start()
-        try:
-            sync_db_permissions()
-        except Exception as e:
-            return jsonify(error=str(e)), 500
-        return jsonify(status="ok")
+        err, err_msg = sync_db_permissions()
+        if err:
+            return jsonify(error=str(err_msg)), 500
+        else:
+            return jsonify(status="ok"), 200
 
     print(f"Starting webhook backend on port {LISTEN_PORT} (version {__version__}")
     # run debug server if started with poetry run python lg_april_permissions/__init__.py -c settings.yaml --serve
     if __name__ == '__main__':
         app.run(debug=True, port=LISTEN_PORT)
     else:
         waitress.serve(app, port=LISTEN_PORT)
@@ -166,34 +166,38 @@
 
     roles = u['data']['roles']
     u = update_user_roles(userid, roles)
     roles = u['data']['roles']
     print(f"Rollen danach:\n{json.dumps(roles, indent=4)}")
 
 
-def sync_db_permissions():
+def sync_db_permissions() -> (bool, str):
     print("Syncing permissions with database")
     try:
         conn = psycopg2.connect(DB_CONNECTION)
         cur = conn.cursor()
-        cur.execute('SELECT * FROM "April_Permissions"')
+        cur.execute('SELECT fk_bikoe FROM "April_Permissions"')
         permissions = cur.fetchall()
         for permission in permissions:
-            id, fk_bikoe, role, app_id = permission
-            fk_bikoe = int(fk_bikoe)
+            fk_bikoe = int(permission[0])
             print(f"Processing Bikö {fk_bikoe}")
             cur.execute('SELECT "Vorname", "Nachname", "RL_user_id" FROM "Kontaktinfo" WHERE id = %s', (fk_bikoe,))
             vorname, nachname, bb_user_id = cur.fetchone()
             if bb_user_id.startswith("ro_ta_users_"):
                 bb_user_id = bb_user_id.replace("ro_ta_users_", "")
+            if "https://bb.itsnow.biz/app/aktionsphasen-portal" in bb_user_id:
+                print(f"WARNING: bb_user_id in Table Kontaktinfo has an invalid value: {bb_user_id}")
+                # soft fail
+                continue
             print(f" Budibase user id: {bb_user_id} ({vorname} {nachname})")
             add_permissions(bb_user_id)
     except Exception as e:
-        fail(e)
+        return True, str(e)
     print("Syncing permissions was successful")
+    return False, ""
 
 
 def show_version():
     print(f"{sys.argv[0]} v{__version__}")
     sys.exit()
 
 
@@ -226,14 +230,17 @@
     elif args.list_users:
         show_users()
     elif args.add_permissions:
         add_permissions(args.add_permissions)
     elif args.remove_permissions:
         remove_permissions(args.remove_permissions)
     elif args.sync:
-        sync_db_permissions()
+        err, err_msg = sync_db_permissions()
+        if err:
+            print(err_msg)
+            sys.exit(1)
     elif args.serve:
         run_backend()
 
 
 if __name__ == '__main__':
     main()
```

### Comparing `lg_april_permissions-0.1.6/PKG-INFO` & `lg_april_permissions-0.1.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lg-april-permissions
-Version: 0.1.6
+Version: 0.1.7
 Summary: 
 Author: kmille
 Author-email: github@androidloves.me
 Requires-Python: >=3.10,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
```

