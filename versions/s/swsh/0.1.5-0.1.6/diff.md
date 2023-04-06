# Comparing `tmp/swsh-0.1.5.tar.gz` & `tmp/swsh-0.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "swsh-0.1.5.tar", last modified: Mon Apr  3 18:45:36 2023, max compression
+gzip compressed data, was "swsh-0.1.6.tar", last modified: Thu Apr  6 19:06:30 2023, max compression
```

## Comparing `swsh-0.1.5.tar` & `swsh-0.1.6.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 shane      (501) staff       (20)        0 2023-04-03 18:45:36.461311 swsh-0.1.5/
--rw-r--r--   0 shane      (501) staff       (20)      660 2023-04-03 18:45:36.461168 swsh-0.1.5/PKG-INFO
--rw-r--r--   0 shane      (501) staff       (20)      196 2023-03-20 20:58:55.000000 swsh-0.1.5/README.md
--rw-r--r--   0 shane      (501) staff       (20)       38 2023-04-03 18:45:36.461360 swsh-0.1.5/setup.cfg
--rw-r--r--   0 shane      (501) staff       (20)     1024 2023-04-03 18:44:54.000000 swsh-0.1.5/setup.py
-drwxr-xr-x   0 shane      (501) staff       (20)        0 2023-04-03 18:45:36.459172 swsh-0.1.5/swsh/
--rwxr-xr-x   0 shane      (501) staff       (20)     3254 2023-03-20 20:54:48.000000 swsh-0.1.5/swsh/buy_a_phone_number.py
--rwxr-xr-x   0 shane      (501) staff       (20)    13786 2023-03-29 20:31:13.000000 swsh-0.1.5/swsh/functions.py
--rwxr-xr-x   0 shane      (501) staff       (20)   135793 2023-03-31 19:10:10.000000 swsh-0.1.5/swsh/swsh.py
-drwxr-xr-x   0 shane      (501) staff       (20)        0 2023-04-03 18:45:36.460952 swsh-0.1.5/swsh.egg-info/
--rw-r--r--   0 shane      (501) staff       (20)      660 2023-04-03 18:45:36.000000 swsh-0.1.5/swsh.egg-info/PKG-INFO
--rw-r--r--   0 shane      (501) staff       (20)      273 2023-04-03 18:45:36.000000 swsh-0.1.5/swsh.egg-info/SOURCES.txt
--rw-r--r--   0 shane      (501) staff       (20)        1 2023-04-03 18:45:36.000000 swsh-0.1.5/swsh.egg-info/dependency_links.txt
--rw-r--r--   0 shane      (501) staff       (20)       40 2023-04-03 18:45:36.000000 swsh-0.1.5/swsh.egg-info/entry_points.txt
--rw-r--r--   0 shane      (501) staff       (20)        1 2023-03-30 19:29:33.000000 swsh-0.1.5/swsh.egg-info/not-zip-safe
--rw-r--r--   0 shane      (501) staff       (20)       83 2023-04-03 18:45:36.000000 swsh-0.1.5/swsh.egg-info/requires.txt
--rw-r--r--   0 shane      (501) staff       (20)        5 2023-04-03 18:45:36.000000 swsh-0.1.5/swsh.egg-info/top_level.txt
+drwxr-xr-x   0 shane      (501) staff       (20)        0 2023-04-06 19:06:30.654281 swsh-0.1.6/
+-rw-r--r--   0 shane      (501) staff       (20)      660 2023-04-06 19:06:30.653984 swsh-0.1.6/PKG-INFO
+-rw-r--r--   0 shane      (501) staff       (20)     1241 2023-04-05 15:05:42.000000 swsh-0.1.6/README.md
+-rw-r--r--   0 shane      (501) staff       (20)       38 2023-04-06 19:06:30.654375 swsh-0.1.6/setup.cfg
+-rw-r--r--   0 shane      (501) staff       (20)     1024 2023-04-06 19:04:00.000000 swsh-0.1.6/setup.py
+drwxr-xr-x   0 shane      (501) staff       (20)        0 2023-04-06 19:06:30.652162 swsh-0.1.6/swsh/
+-rwxr-xr-x   0 shane      (501) staff       (20)     3254 2023-04-05 20:48:52.000000 swsh-0.1.6/swsh/buy_a_phone_number.py
+-rwxr-xr-x   0 shane      (501) staff       (20)    13786 2023-03-29 20:31:13.000000 swsh-0.1.6/swsh/functions.py
+-rwxr-xr-x   0 shane      (501) staff       (20)   136124 2023-04-05 20:48:43.000000 swsh-0.1.6/swsh/swsh.py
+drwxr-xr-x   0 shane      (501) staff       (20)        0 2023-04-06 19:06:30.653771 swsh-0.1.6/swsh.egg-info/
+-rw-r--r--   0 shane      (501) staff       (20)      660 2023-04-06 19:06:30.000000 swsh-0.1.6/swsh.egg-info/PKG-INFO
+-rw-r--r--   0 shane      (501) staff       (20)      273 2023-04-06 19:06:30.000000 swsh-0.1.6/swsh.egg-info/SOURCES.txt
+-rw-r--r--   0 shane      (501) staff       (20)        1 2023-04-06 19:06:30.000000 swsh-0.1.6/swsh.egg-info/dependency_links.txt
+-rw-r--r--   0 shane      (501) staff       (20)       40 2023-04-06 19:06:30.000000 swsh-0.1.6/swsh.egg-info/entry_points.txt
+-rw-r--r--   0 shane      (501) staff       (20)        1 2023-04-06 19:06:30.000000 swsh-0.1.6/swsh.egg-info/not-zip-safe
+-rw-r--r--   0 shane      (501) staff       (20)       83 2023-04-06 19:06:30.000000 swsh-0.1.6/swsh.egg-info/requires.txt
+-rw-r--r--   0 shane      (501) staff       (20)        5 2023-04-06 19:06:30.000000 swsh-0.1.6/swsh.egg-info/top_level.txt
```

### Comparing `swsh-0.1.5/PKG-INFO` & `swsh-0.1.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: swsh
-Version: 0.1.5
+Version: 0.1.6
 Summary: SignalWire interactive SHell
 Home-page: https://github.com/signalwire/swish
 Author: Shane Harrell
 Author-email: shane.harrell@signalwire.com
 License: MIT
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `swsh-0.1.5/setup.py` & `swsh-0.1.6/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,15 +10,15 @@
   'Natural Language :: English',
   'Topic :: Communications',
   'Topic :: Software Development'
 ]
 
 setup(
   name='swsh',
-  version='0.1.5',
+  version='0.1.6',
   description='SignalWire interactive SHell',
   entry_points={
     'console_scripts': ['swsh=swsh.swsh:main']
   },
   #long_description=read('README.md'),
   long_description_content_type="text/markdown",
   classifiers=CLASSIFIERS,
```

### Comparing `swsh-0.1.5/swsh/buy_a_phone_number.py` & `swsh-0.1.6/swsh/buy_a_phone_number.py`

 * *Files identical despite different names*

### Comparing `swsh-0.1.5/swsh/functions.py` & `swsh-0.1.6/swsh/functions.py`

 * *Files identical despite different names*

### Comparing `swsh-0.1.5/swsh/swsh.py` & `swsh-0.1.6/swsh/swsh.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,43 +21,54 @@
     swish_version = "1.0"
 
     # Verify the OS env is set.  Ask for input if not.
     # TODO/NOTE: This does not export the vars for future use.  This may be something to push into a .swsh file at some point
     # TODO/NOTE pt 2: we can add switches like --signalwire-space <spacename> to this as well
     signalwire_space, project_id, rest_api_token = get_environment()
     if signalwire_space == "" or signalwire_space is None or project_id == "" or project_id is None or rest_api_token == "" or rest_api_token is None:
-        print("\nEnvironment variables not set.  Add the following to env for automated start-up!\n\nSIGNALWIRE_SPACE=<space_name>\nPROJECT_ID=<project_id>\n<REST_API_TOKEN=<api_token>\n")
-
+        if len(sys.argv) > 1:
+            sys.exit("""ERROR:  ENV vars not set!\n
+Run the following commands at the terminal to add to system env for non-interactive mode:
+Windows:
+  setx SIGNALWIRE_SPACE=<space_name>
+  setx PROJECT_ID=<project_id>
+  setx REST_API_TOKEN=<api_token>"
+
+Linux / MacOS
+  export SIGNALWIRE_SPACE=<space_name>
+  export PROJECT_ID=<project_id>
+  export REST_API_TOKEN=<api_token>"       
+""")
+        print("""No environment detected!\n  
+Run the following commands at the terminal to add env vars to speed up start time:
+Windows:
+  setx SIGNALWIRE_SPACE=<space_name>
+  setx PROJECT_ID=<project_id>
+  setx REST_API_TOKEN=<api_token>"
+
+Linux / MacOS
+  export SIGNALWIRE_SPACE=<space_name>
+  export PROJECT_ID=<project_id>
+  export REST_API_TOKEN=<api_token>\n\n
+""")
         if signalwire_space == "" or signalwire_space is None:
             signalwire_space = input ("\nEnter Signalwire Space: ")
-
         if project_id == "" or project_id is None:
             project_id = input ("Enter Project ID: ")
-
         if rest_api_token == "" or rest_api_token is None:
             rest_api_token = input ("Enter Rest API Token: ")
-
-    # validate what was entered and then put them into the environment
-    valid_creds = validate_signalwire_creds(signalwire_space, project_id, rest_api_token)
-    if valid_creds:
-        os.environ['SIGNALWIRE_SPACE'] = signalwire_space
-        os.environ['PROJECT_ID'] = project_id
-        os.environ['REST_API_TOKEN'] = rest_api_token
-    else:
-        print ("ERROR: This are not valid SignalWire API Credentials\n")
-
-    # validate what was entered and then put them into the environment
-    valid_creds = validate_signalwire_creds(signalwire_space, project_id, rest_api_token)
-    if valid_creds:
-        os.environ['SIGNALWIRE_SPACE'] = signalwire_space
-        os.environ['PROJECT_ID'] = project_id
-        os.environ['REST_API_TOKEN'] = rest_api_token
-    else:
-        print ("ERROR: This are not valid SignalWire API Credentials\n")
-
+        
+        # validate what was entered and then put them into the environment
+        valid_creds = validate_signalwire_creds(signalwire_space, project_id, rest_api_token)
+        if valid_creds:
+            os.environ['SIGNALWIRE_SPACE'] = signalwire_space
+            os.environ['PROJECT_ID'] = project_id
+            os.environ['REST_API_TOKEN'] = rest_api_token
+        else:
+            print ("ERROR: This are not valid SignalWire API Credentials\n")
 
     if len(sys.argv) > 1:
         # Sets up non-interactive mode
         # when passing arguments into cmd2, it requires 'quit' as the last command to exit
         # Appending quit here to make it more user friendly
 
         # Looking for sys.argv also allows us to expand to pass in additional switches at a later time
@@ -66,27 +77,28 @@
         if sys.argv[1]:
             # sys.argv.remove('-x')   # Remove the -x switch
             # Group all arguments as a single command, otherwise all arguments are processes as separate commands.  Delete every element in the list after 1.
             sys.argv[1] = ' '.join(sys.argv[1::])
             del sys.argv[2:]
             sys.argv.append('quit')   # Append the required 'quit' at the end
             noninteractive_flag = 1
-        elif sys.argv[1] == '-v' or sys.argv[1].lower() == '--version':
-            print ("Version: " + swish_version)
-            sys.exit()
-        else:
-            print ('''SWiSH Help Menu:
+
+            if sys.argv[1] == '-v' or sys.argv[1] == '--version':
+                print ("Version: " + swish_version)
+                sys.exit()
+            elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
+                print ('''SWiSH Help Menu:
 ================
 SignalWire interactive SHell
 Cross platform command line utility and shell for administering a Space or Spaces in Signalwire
 
 -h | --help       view this help menu
 -v | --version    SWiSH version
 ''')
-            sys.exit()
+                sys.exit()
 
     else:
         def __init__(self):
             super().__init__(
             completekey='tab',
             persistent_history_file='~/.swsh_history'
             )
@@ -629,14 +641,15 @@
                 json_data = json.loads(output)
                 tn_data = json_data["data"]
                 for index, value in enumerate(tn_data):
                     # Create a temporary dictionary for each number then only return the number value
                     # NOTE: Someday this could be expanded to return the number and the ID or something like that
                     temp_d = value
                     print (temp_d["number"])
+                print ("") # End with a blank line.
             else:
                 is_json = validate_json(output)
                 if is_json:
                     print_error_json(output)
                 else:
                     print (status_code + ": " + output + "\n" )
```

### Comparing `swsh-0.1.5/swsh.egg-info/PKG-INFO` & `swsh-0.1.6/swsh.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: swsh
-Version: 0.1.5
+Version: 0.1.6
 Summary: SignalWire interactive SHell
 Home-page: https://github.com/signalwire/swish
 Author: Shane Harrell
 Author-email: shane.harrell@signalwire.com
 License: MIT
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

