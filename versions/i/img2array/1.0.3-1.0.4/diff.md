# Comparing `tmp/img2array-1.0.3.tar.gz` & `tmp/img2array-1.0.4.tar.gz`

## Comparing `img2array-1.0.3.tar` & `img2array-1.0.4.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0       33 2020-02-02 00:00:00.000000 img2array-1.0.3/requirements.txt
--rw-r--r--   0        0        0       51 2020-02-02 00:00:00.000000 img2array-1.0.3/.vscode/settings.json
--rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 img2array-1.0.3/src/img2array/__init__.py
--rw-r--r--   0        0        0     1836 2020-02-02 00:00:00.000000 img2array-1.0.3/src/img2array/__main__.py
--rw-r--r--   0        0        0     2601 2020-02-02 00:00:00.000000 img2array-1.0.3/src/img2array/img2array.py
--rw-r--r--   0        0        0     3093 2020-02-02 00:00:00.000000 img2array-1.0.3/.gitignore
--rw-r--r--   0        0        0     1067 2020-02-02 00:00:00.000000 img2array-1.0.3/LICENSE
--rw-r--r--   0        0        0      889 2020-02-02 00:00:00.000000 img2array-1.0.3/README.md
--rw-r--r--   0        0        0      755 2020-02-02 00:00:00.000000 img2array-1.0.3/pyproject.toml
--rw-r--r--   0        0        0     1511 2020-02-02 00:00:00.000000 img2array-1.0.3/PKG-INFO
+-rw-r--r--   0        0        0       33 2020-02-02 00:00:00.000000 img2array-1.0.4/requirements.txt
+-rw-r--r--   0        0        0       51 2020-02-02 00:00:00.000000 img2array-1.0.4/.vscode/settings.json
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 img2array-1.0.4/src/img2array/__init__.py
+-rw-r--r--   0        0        0     1679 2020-02-02 00:00:00.000000 img2array-1.0.4/src/img2array/__main__.py
+-rw-r--r--   0        0        0     2601 2020-02-02 00:00:00.000000 img2array-1.0.4/src/img2array/img2array.py
+-rw-r--r--   0        0        0     3093 2020-02-02 00:00:00.000000 img2array-1.0.4/.gitignore
+-rw-r--r--   0        0        0     1067 2020-02-02 00:00:00.000000 img2array-1.0.4/LICENSE
+-rw-r--r--   0        0        0      879 2020-02-02 00:00:00.000000 img2array-1.0.4/README.md
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 img2array-1.0.4/pyproject.toml
+-rw-r--r--   0        0        0     1501 2020-02-02 00:00:00.000000 img2array-1.0.4/PKG-INFO
```

### Comparing `img2array-1.0.3/src/img2array/__main__.py` & `img2array-1.0.4/src/img2array/__main__.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,61 +1,60 @@
 import sys
 import getopt
 from img2array import img2array
 
-if __name__ == "__main__":
 
-    help_text = """
+help_text = """
 Prints the pixels of an image into an array of RGB values.
 This can be copied easily to other applications, such as embedded apps.
 
 Commands:
     -h, --help    :  This help text
     -i, --image   :  Image file path
     -p, --prefix  :  Prefix for the item, like "colorFunc\\("
     -P, --postfix :  Postfix for the item, like "\\)"
     -f, --format  :  Format of the color, defaults to RGB. Possible values: RGB, RGBA, Hex, HexAlpha
 
 Example:
-    python -m img2array -i file.png --prefix=coolFunction\\( --postfix=\\) --format=RGB
-    
+    img2array -i file.png --prefix=coolFunction\\( --postfix=\\) --format=RGB
+
     Note: the \\ before () may be required or not depending on the shell you're using.
 
     This should print an array version of the image like
     {
         {coolFunction(200,200,200), coolFunction(123,123,123)},
         {coolFunction(111,111,111), coolFunction(41,0,12)}
     }
 
     You can then easily copy-paste this to your applications.
-    """
+"""
+
+argv = sys.argv[1:]
+if len(argv) <= 0:
+    print("No input data given, printing help!")
+    print(help_text)
+    sys.exit(-1)
+
+image_path = ""
+item_prefix = ""
+item_postfix = ""
+color_format = "RGB"
+
+opts, args = getopt.getopt(
+    argv, "hi:p:P:f:", ["help", "image=", "prefix=", "postfix=", "format="]
+)
 
-    argv = sys.argv[1:]
-    if len(argv) <= 0:
-        print("No input data given, printing help!")
+for opt, arg in opts:
+    if opt in ('-h', "--help"):
         print(help_text)
-        sys.exit(-1)
+        sys.exit(0)
+    elif opt in ("-i", "--image"):
+        image_path = arg
+    elif opt in ("-p", "--prefix"):
+        item_prefix = arg
+    elif opt in ("-P", "--postfix"):
+        item_postfix = arg
+    elif opt in ("-f", "--format"):
+        color_format = arg
 
-    image_path = ""
-    item_prefix = ""
-    item_postfix = ""
-    color_format = "RGB"
-
-    opts, args = getopt.getopt(
-        argv, "hi:p:P:f:", ["help", "image=", "prefix=", "postfix=", "format="]
-    )
-
-    for opt, arg in opts:
-        if opt in ('-h', "--help"):
-            print(help_text)
-            sys.exit(0)
-        elif opt in ("-i", "--image"):
-            image_path = arg
-        elif opt in ("-p", "--prefix"):
-            item_prefix = arg
-        elif opt in ("-P", "--postfix"):
-            item_postfix = arg
-        elif opt in ("-f", "--format"):
-            color_format = arg
-    
-    i2a = img2array(image_path, item_prefix, item_postfix, color_format)
-    i2a.run()
+i2a = img2array(image_path, item_prefix, item_postfix, color_format)
+i2a.run()
```

### Comparing `img2array-1.0.3/src/img2array/img2array.py` & `img2array-1.0.4/src/img2array/img2array.py`

 * *Files identical despite different names*

### Comparing `img2array-1.0.3/.gitignore` & `img2array-1.0.4/.gitignore`

 * *Files identical despite different names*

### Comparing `img2array-1.0.3/LICENSE` & `img2array-1.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `img2array-1.0.3/README.md` & `img2array-1.0.4/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 
 # Install
 
 `pip install img2array`
 
 # Example
 
-`python -m img2array -i file.png --prefix=coolFunction\( --postfix=\) --format=RGB`
+`img2array -i file.png --prefix=coolFunction\( --postfix=\) --format=RGB`
 
 **Note**: the \ before () may be required or not depending on the shell you're using.
 
 This should print an array version of the image like
 
 ```
 {
```

### Comparing `img2array-1.0.3/pyproject.toml` & `img2array-1.0.4/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "img2array"
-version = "1.0.3"
+version = "1.0.4"
 authors = [
   { name="Akseli Lahtinen", email="akselmo@akselmo.dev" },
 ]
 description = "Prints the pixels of an image into an array of RGB values, that can be easily exported to embedded applications."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
@@ -17,13 +17,13 @@
     "Operating System :: OS Independent",
 ]
 dependencies = [
   "Pillow==9.4.0",
 ]
 
 [project.scripts]
-img2array = "img2array.img2array:__main__"
+img2array = "img2array.__main__:main"
 
 [project.urls]
 "Homepage" = "https://codeberg.org/akselmo/img2array"
 "Bug Tracker" = "https://codeberg.org/akselmo/img2array/issues"
```

### Comparing `img2array-1.0.3/PKG-INFO` & `img2array-1.0.4/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: img2array
-Version: 1.0.3
+Version: 1.0.4
 Summary: Prints the pixels of an image into an array of RGB values, that can be easily exported to embedded applications.
 Project-URL: Homepage, https://codeberg.org/akselmo/img2array
 Project-URL: Bug Tracker, https://codeberg.org/akselmo/img2array/issues
 Author-email: Akseli Lahtinen <akselmo@akselmo.dev>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
@@ -28,15 +28,15 @@
 
 # Install
 
 `pip install img2array`
 
 # Example
 
-`python -m img2array -i file.png --prefix=coolFunction\( --postfix=\) --format=RGB`
+`img2array -i file.png --prefix=coolFunction\( --postfix=\) --format=RGB`
 
 **Note**: the \ before () may be required or not depending on the shell you're using.
 
 This should print an array version of the image like
 
 ```
 {
```

