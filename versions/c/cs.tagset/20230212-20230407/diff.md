# Comparing `tmp/cs.tagset-20230212.tar.gz` & `tmp/cs.tagset-20230407.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cs.tagset-20230212.tar", last modified: Sun Feb 12 04:01:09 2023, max compression
+gzip compressed data, was "cs.tagset-20230407.tar", last modified: Fri Apr  7 00:06:27 2023, max compression
```

## Comparing `cs.tagset-20230212.tar` & `cs.tagset-20230407.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-02-12 04:01:09.281165 cs.tagset-20230212/
--rw-rw-r--   0 cameron    (501) cameron    (502)       18 2023-02-12 04:00:40.000000 cs.tagset-20230212/MANIFEST.in
--rw-rw-r--   0 cameron    (501) cameron    (502)    31189 2023-02-12 04:01:09.281347 cs.tagset-20230212/PKG-INFO
--rw-rw-r--   0 cameron    (501) cameron    (502)    64174 2023-02-12 04:00:46.000000 cs.tagset-20230212/README.md
-drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-02-12 04:01:09.273412 cs.tagset-20230212/lib/
-drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-02-12 04:01:09.273863 cs.tagset-20230212/lib/python/
-drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-02-12 04:01:09.277879 cs.tagset-20230212/lib/python/cs/
--rw-r--r--   0 cameron    (501) cameron    (502)   130949 2023-02-12 04:00:32.000000 cs.tagset-20230212/lib/python/cs/tagset.py
-drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-02-12 04:01:09.280916 cs.tagset-20230212/lib/python/cs.tagset.egg-info/
--rw-rw-r--   0 cameron    (501) cameron    (502)    31189 2023-02-12 04:01:09.000000 cs.tagset-20230212/lib/python/cs.tagset.egg-info/PKG-INFO
--rw-rw-r--   0 cameron    (501) cameron    (502)      298 2023-02-12 04:01:09.000000 cs.tagset-20230212/lib/python/cs.tagset.egg-info/SOURCES.txt
--rw-rw-r--   0 cameron    (501) cameron    (502)        1 2023-02-12 04:01:09.000000 cs.tagset-20230212/lib/python/cs.tagset.egg-info/dependency_links.txt
--rw-rw-r--   0 cameron    (501) cameron    (502)      298 2023-02-12 04:01:09.000000 cs.tagset-20230212/lib/python/cs.tagset.egg-info/requires.txt
--rw-rw-r--   0 cameron    (501) cameron    (502)        3 2023-02-12 04:01:09.000000 cs.tagset-20230212/lib/python/cs.tagset.egg-info/top_level.txt
--rw-rw-r--   0 cameron    (501) cameron    (502)    31834 2023-02-12 04:01:01.000000 cs.tagset-20230212/pyproject.toml
--rw-rw-r--   0 cameron    (501) cameron    (502)     1150 2023-02-12 04:01:09.282002 cs.tagset-20230212/setup.cfg
--rw-rw-r--   0 cameron    (501) cameron    (502)       59 2023-02-12 04:00:46.000000 cs.tagset-20230212/setup.py
+drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-04-07 00:06:27.871225 cs.tagset-20230407/
+-rw-rw-r--   0 cameron    (501) cameron    (502)       18 2023-04-07 00:05:56.000000 cs.tagset-20230407/MANIFEST.in
+-rw-rw-r--   0 cameron    (501) cameron    (502)    31489 2023-04-07 00:06:27.871409 cs.tagset-20230407/PKG-INFO
+-rw-rw-r--   0 cameron    (501) cameron    (502)    64474 2023-04-07 00:06:02.000000 cs.tagset-20230407/README.md
+drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-04-07 00:06:27.866511 cs.tagset-20230407/lib/
+drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-04-07 00:06:27.866836 cs.tagset-20230407/lib/python/
+drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-04-07 00:06:27.868975 cs.tagset-20230407/lib/python/cs/
+-rw-r--r--   0 cameron    (501) cameron    (502)   131222 2023-04-07 00:05:47.000000 cs.tagset-20230407/lib/python/cs/tagset.py
+drwxrwxr-x   0 cameron    (501) cameron    (502)        0 2023-04-07 00:06:27.870932 cs.tagset-20230407/lib/python/cs.tagset.egg-info/
+-rw-rw-r--   0 cameron    (501) cameron    (502)    31489 2023-04-07 00:06:27.000000 cs.tagset-20230407/lib/python/cs.tagset.egg-info/PKG-INFO
+-rw-rw-r--   0 cameron    (501) cameron    (502)      298 2023-04-07 00:06:27.000000 cs.tagset-20230407/lib/python/cs.tagset.egg-info/SOURCES.txt
+-rw-rw-r--   0 cameron    (501) cameron    (502)        1 2023-04-07 00:06:27.000000 cs.tagset-20230407/lib/python/cs.tagset.egg-info/dependency_links.txt
+-rw-rw-r--   0 cameron    (501) cameron    (502)      298 2023-04-07 00:06:27.000000 cs.tagset-20230407/lib/python/cs.tagset.egg-info/requires.txt
+-rw-rw-r--   0 cameron    (501) cameron    (502)        3 2023-04-07 00:06:27.000000 cs.tagset-20230407/lib/python/cs.tagset.egg-info/top_level.txt
+-rw-rw-r--   0 cameron    (501) cameron    (502)    32134 2023-04-07 00:06:20.000000 cs.tagset-20230407/pyproject.toml
+-rw-rw-r--   0 cameron    (501) cameron    (502)     1150 2023-04-07 00:06:27.872017 cs.tagset-20230407/setup.cfg
+-rw-rw-r--   0 cameron    (501) cameron    (502)       59 2023-04-07 00:06:02.000000 cs.tagset-20230407/setup.py
```

### Comparing `cs.tagset-20230212/PKG-INFO` & `cs.tagset-20230407/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cs.tagset
-Version: 20230212
+Version: 20230407
 Summary: Tags and sets of tags with __format__ support and optional ontology information.
 Home-page: https://bitbucket.org/cameron_simpson/css/commits/all
 Author: Cameron Simpson
 Author-email: Cameron Simpson <cs@cskk.id.au>
 License: GNU General Public License v3 or later (GPLv3+)
 Project-URL: URL, https://bitbucket.org/cameron_simpson/css/commits/all
 Keywords: python3
@@ -16,16 +16,16 @@
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Description-Content-Type: text/markdown
 
 Tags and sets of tags
 with __format__ support and optional ontology information.
 
-*Latest release 20230212*:
-Mark TagSetCriterion as Promotable.
+*Latest release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
 
 See `cs.fstags` for support for applying these to filesystem objects
 such as directories and files.
 
 See `cs.sqltags` for support for databases of entities with tags,
 not directly associated with filesystem objects.
 This is suited to both log entries (entities with no "name")
@@ -621,14 +621,16 @@
           Otherwise the argument is expected to be an entity name;
           edit the tags of that entity.
         help [-l] [subcommand-names...]
           Print the full help for the named subcommands,
           or for all subcommands if no names are specified.
           -l  Long help even if no subcommand-names provided.
         meta tag=value
+        shell
+          Run a command prompt via cmd.Cmd using this command's subcommands.
         type
             With no arguments, list the defined types.
           type type_name
             With a type name, print its `Tag`s.
           type type_name edit
             Edit the tags defining a type.
           type type_name edit meta_names_pattern...
@@ -640,14 +642,17 @@
           type type_name + entity_name [tags...]
             Create type_name.entity_name and apply the tags.
 
 # Release Log
 
 
 
+*Release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
+
 *Release 20230212*:
 Mark TagSetCriterion as Promotable.
 
 *Release 20230210*:
 * TagFile: new optional update_mapping secondary mapping to which to mirror file tags, for example to an SQLTags.
 * New .uuid:UUID property returning the UUID for the tag named 'uuid' or None.
```

### Comparing `cs.tagset-20230212/README.md` & `cs.tagset-20230407/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 Tags and sets of tags
 with __format__ support and optional ontology information.
 
-*Latest release 20230212*:
-Mark TagSetCriterion as Promotable.
+*Latest release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
 
 See `cs.fstags` for support for applying these to filesystem objects
 such as directories and files.
 
 See `cs.sqltags` for support for databases of entities with tags,
 not directly associated with filesystem objects.
 This is suited to both log entries (entities with no "name")
@@ -1530,14 +1530,16 @@
           Otherwise the argument is expected to be an entity name;
           edit the tags of that entity.
         help [-l] [subcommand-names...]
           Print the full help for the named subcommands,
           or for all subcommands if no names are specified.
           -l  Long help even if no subcommand-names provided.
         meta tag=value
+        shell
+          Run a command prompt via cmd.Cmd using this command's subcommands.
         type
             With no arguments, list the defined types.
           type type_name
             With a type name, print its `Tag`s.
           type type_name edit
             Edit the tags defining a type.
           type type_name edit meta_names_pattern...
@@ -1578,14 +1580,17 @@
 {cmd} type_name + entity_name [tags...]
   Create type_name.entity_name and apply the tags.
 
 # Release Log
 
 
 
+*Release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
+
 *Release 20230212*:
 Mark TagSetCriterion as Promotable.
 
 *Release 20230210*:
 * TagFile: new optional update_mapping secondary mapping to which to mirror file tags, for example to an SQLTags.
 * New .uuid:UUID property returning the UUID for the tag named 'uuid' or None.
```

### Comparing `cs.tagset-20230212/lib/python/cs/tagset.py` & `cs.tagset-20230407/lib/python/cs/tagset.py`

 * *Files 0% similar despite different names*

```diff
@@ -228,15 +228,15 @@
 )
 from cs.obj import SingletonMixin
 from cs.pfx import Pfx, pfx, pfx_call, pfx_method
 from cs.py3 import date_fromisoformat, datetime_fromisoformat
 from cs.resources import MultiOpenMixin
 from cs.threads import locked_property
 
-__version__ = '20230212'
+__version__ = '20230407'
 
 DISTINFO = {
     'keywords': ["python3"],
     'classifiers': [
         "Programming Language :: Python",
         "Programming Language :: Python :: 3",
     ],
@@ -3512,24 +3512,31 @@
     tagsets = self._tagsets
     if tagsets is None:
       # never loaded - no need to save
       return
     with self._lock:
       if self.is_modified():
         # there are modified TagSets
-        self.save_tagsets(
-            self.fspath,
-            tagsets,
-            self.unparsed,
-            extra_types=extra_types,
-            prune=prune,
-            update_mapping=self.update_mapping,
-            update_prefix=self.update_prefix,
-            update_uuid_tag_name=self.update_uuid_tag_name,
-        )
+        update_mapping_close = getattr(self.update_mapping, 'close', None)
+        if update_mapping_close:
+          self.update_mapping.open()
+        try:
+          self.save_tagsets(
+              self.fspath,
+              tagsets,
+              self.unparsed,
+              extra_types=extra_types,
+              prune=prune,
+              update_mapping=self.update_mapping,
+              update_prefix=self.update_prefix,
+              update_uuid_tag_name=self.update_uuid_tag_name,
+          )
+        finally:
+          if update_mapping_close:
+            pfx_call(update_mapping_close)
         self._loaded_signature = self._loadsave_signature()
         for tagset in tagsets.values():
           tagset.modified = False
 
   def update(self, name, tags, *, prefix=None, verbose=None):
     ''' Update the tags for `name` from the supplied `tags`
         as for `Tagset.update`.
```

### Comparing `cs.tagset-20230212/lib/python/cs.tagset.egg-info/PKG-INFO` & `cs.tagset-20230407/lib/python/cs.tagset.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cs.tagset
-Version: 20230212
+Version: 20230407
 Summary: Tags and sets of tags with __format__ support and optional ontology information.
 Home-page: https://bitbucket.org/cameron_simpson/css/commits/all
 Author: Cameron Simpson
 Author-email: Cameron Simpson <cs@cskk.id.au>
 License: GNU General Public License v3 or later (GPLv3+)
 Project-URL: URL, https://bitbucket.org/cameron_simpson/css/commits/all
 Keywords: python3
@@ -16,16 +16,16 @@
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Description-Content-Type: text/markdown
 
 Tags and sets of tags
 with __format__ support and optional ontology information.
 
-*Latest release 20230212*:
-Mark TagSetCriterion as Promotable.
+*Latest release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
 
 See `cs.fstags` for support for applying these to filesystem objects
 such as directories and files.
 
 See `cs.sqltags` for support for databases of entities with tags,
 not directly associated with filesystem objects.
 This is suited to both log entries (entities with no "name")
@@ -621,14 +621,16 @@
           Otherwise the argument is expected to be an entity name;
           edit the tags of that entity.
         help [-l] [subcommand-names...]
           Print the full help for the named subcommands,
           or for all subcommands if no names are specified.
           -l  Long help even if no subcommand-names provided.
         meta tag=value
+        shell
+          Run a command prompt via cmd.Cmd using this command's subcommands.
         type
             With no arguments, list the defined types.
           type type_name
             With a type name, print its `Tag`s.
           type type_name edit
             Edit the tags defining a type.
           type type_name edit meta_names_pattern...
@@ -640,14 +642,17 @@
           type type_name + entity_name [tags...]
             Create type_name.entity_name and apply the tags.
 
 # Release Log
 
 
 
+*Release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
+
 *Release 20230212*:
 Mark TagSetCriterion as Promotable.
 
 *Release 20230210*:
 * TagFile: new optional update_mapping secondary mapping to which to mirror file tags, for example to an SQLTags.
 * New .uuid:UUID property returning the UUID for the tag named 'uuid' or None.
```

### Comparing `cs.tagset-20230212/pyproject.toml` & `cs.tagset-20230407/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -6,53 +6,53 @@
 ]
 keywords = [
     "python3",
 ]
 dependencies = [
     "cs.cmdutils>=20210404",
     "cs.dateutils>=20230210",
-    "cs.deco>=20230212",
+    "cs.deco>=20230331",
     "cs.edit>=20220429",
-    "cs.fileutils>=20221118",
+    "cs.fileutils>=20230401",
     "cs.fs>=20220429",
-    "cs.lex>=20230210",
+    "cs.lex>=20230401",
     "cs.logutils>=20230212",
     "cs.mappings>=20220912.4",
     "cs.obj>=20200716",
-    "cs.pfx>=20221118",
+    "cs.pfx>=20230331",
     "cs.py3>=20220523",
-    "cs.resources>=20230212",
-    "cs.threads>=20230212",
+    "cs.resources>=20230331",
+    "cs.threads>=20230331",
     "icontract",
     "typeguard",
 ]
 classifiers = [
     "Programming Language :: Python",
     "Programming Language :: Python :: 3",
     "Development Status :: 4 - Beta",
     "Intended Audience :: Developers",
     "Operating System :: OS Independent",
     "Topic :: Software Development :: Libraries :: Python Modules",
     "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
 ]
-version = "20230212"
+version = "20230407"
 
 [project.license]
 text = "GNU General Public License v3 or later (GPLv3+)"
 
 [project.urls]
 URL = "https://bitbucket.org/cameron_simpson/css/commits/all"
 
 [project.readme]
 text = """
 Tags and sets of tags
 with __format__ support and optional ontology information.
 
-*Latest release 20230212*:
-Mark TagSetCriterion as Promotable.
+*Latest release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
 
 See `cs.fstags` for support for applying these to filesystem objects
 such as directories and files.
 
 See `cs.sqltags` for support for databases of entities with tags,
 not directly associated with filesystem objects.
 This is suited to both log entries (entities with no \"name\")
@@ -648,14 +648,16 @@
           Otherwise the argument is expected to be an entity name;
           edit the tags of that entity.
         help [-l] [subcommand-names...]
           Print the full help for the named subcommands,
           or for all subcommands if no names are specified.
           -l  Long help even if no subcommand-names provided.
         meta tag=value
+        shell
+          Run a command prompt via cmd.Cmd using this command's subcommands.
         type
             With no arguments, list the defined types.
           type type_name
             With a type name, print its `Tag`s.
           type type_name edit
             Edit the tags defining a type.
           type type_name edit meta_names_pattern...
@@ -667,14 +669,17 @@
           type type_name + entity_name [tags...]
             Create type_name.entity_name and apply the tags.
 
 # Release Log
 
 
 
+*Release 20230407*:
+Move the (optional) ORM open/close from FSTags.startup_shutdown to TagFile.save, greatly shortens the ORM lock.
+
 *Release 20230212*:
 Mark TagSetCriterion as Promotable.
 
 *Release 20230210*:
 * TagFile: new optional update_mapping secondary mapping to which to mirror file tags, for example to an SQLTags.
 * New .uuid:UUID property returning the UUID for the tag named 'uuid' or None.
```

