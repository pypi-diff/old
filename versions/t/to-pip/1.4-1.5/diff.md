# Comparing `tmp/to-pip-1.4.tar.gz` & `tmp/to-pip-1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "to-pip-1.4.tar", last modified: Fri Apr  7 13:43:56 2023, max compression
+gzip compressed data, was "to-pip-1.5.tar", last modified: Fri Apr  7 14:55:20 2023, max compression
```

## Comparing `to-pip-1.4.tar` & `to-pip-1.5.tar`

### file list

```diff
@@ -1,12 +1,13 @@
-drwxr-xr-x   0 chiubowen   (501) staff       (20)        0 2023-04-07 13:43:56.014484 to-pip-1.4/
--rw-r--r--   0 chiubowen   (501) staff       (20)     2065 2023-04-07 13:43:56.014371 to-pip-1.4/PKG-INFO
--rw-r--r--   0 chiubowen   (501) staff       (20)     1903 2023-04-07 13:43:55.000000 to-pip-1.4/README.md
--rw-r--r--   0 chiubowen   (501) staff       (20)       38 2023-04-07 13:43:56.014524 to-pip-1.4/setup.cfg
--rw-r--r--   0 chiubowen   (501) staff       (20)      486 2023-04-07 13:43:55.000000 to-pip-1.4/setup.py
-drwxr-xr-x   0 chiubowen   (501) staff       (20)        0 2023-04-07 13:43:56.014242 to-pip-1.4/to_pip.egg-info/
--rw-r--r--   0 chiubowen   (501) staff       (20)     2065 2023-04-07 13:43:56.000000 to-pip-1.4/to_pip.egg-info/PKG-INFO
--rw-r--r--   0 chiubowen   (501) staff       (20)      181 2023-04-07 13:43:56.000000 to-pip-1.4/to_pip.egg-info/SOURCES.txt
--rw-r--r--   0 chiubowen   (501) staff       (20)        1 2023-04-07 13:43:56.000000 to-pip-1.4/to_pip.egg-info/dependency_links.txt
--rw-r--r--   0 chiubowen   (501) staff       (20)       40 2023-04-07 13:43:56.000000 to-pip-1.4/to_pip.egg-info/entry_points.txt
--rw-r--r--   0 chiubowen   (501) staff       (20)        7 2023-04-07 13:43:56.000000 to-pip-1.4/to_pip.egg-info/top_level.txt
--rwxr-xr-x   0 chiubowen   (501) staff       (20)     3103 2023-04-07 13:43:55.000000 to-pip-1.4/to_pip.py
+drwxr-xr-x   0 chiubowen   (501) staff       (20)        0 2023-04-07 14:55:20.817757 to-pip-1.5/
+-rw-r--r--   0 chiubowen   (501) staff       (20)     2065 2023-04-07 14:55:20.817594 to-pip-1.5/PKG-INFO
+-rw-r--r--   0 chiubowen   (501) staff       (20)     1903 2023-04-07 14:55:20.000000 to-pip-1.5/README.md
+-rw-r--r--   0 chiubowen   (501) staff       (20)       38 2023-04-07 14:55:20.817803 to-pip-1.5/setup.cfg
+-rw-r--r--   0 chiubowen   (501) staff       (20)      486 2023-04-07 14:55:20.000000 to-pip-1.5/setup.py
+drwxr-xr-x   0 chiubowen   (501) staff       (20)        0 2023-04-07 14:55:20.817299 to-pip-1.5/to_pip.egg-info/
+-rw-r--r--   0 chiubowen   (501) staff       (20)     2065 2023-04-07 14:55:20.000000 to-pip-1.5/to_pip.egg-info/PKG-INFO
+-rw-r--r--   0 chiubowen   (501) staff       (20)      210 2023-04-07 14:55:20.000000 to-pip-1.5/to_pip.egg-info/SOURCES.txt
+-rw-r--r--   0 chiubowen   (501) staff       (20)        1 2023-04-07 14:55:20.000000 to-pip-1.5/to_pip.egg-info/dependency_links.txt
+-rw-r--r--   0 chiubowen   (501) staff       (20)       40 2023-04-07 14:55:20.000000 to-pip-1.5/to_pip.egg-info/entry_points.txt
+-rw-r--r--   0 chiubowen   (501) staff       (20)       48 2023-04-07 14:55:20.000000 to-pip-1.5/to_pip.egg-info/requires.txt
+-rw-r--r--   0 chiubowen   (501) staff       (20)        7 2023-04-07 14:55:20.000000 to-pip-1.5/to_pip.egg-info/top_level.txt
+-rwxr-xr-x   0 chiubowen   (501) staff       (20)     4448 2023-04-07 14:55:20.000000 to-pip-1.5/to_pip.py
```

### Comparing `to-pip-1.4/PKG-INFO` & `to-pip-1.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: to-pip
-Version: 1.4
+Version: 1.5
 Summary: UNKNOWN
 Home-page: UNKNOWN
 License: UNKNOWN
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
 
 # To-pip
```

### Comparing `to-pip-1.4/README.md` & `to-pip-1.5/README.md`

 * *Files identical despite different names*

### Comparing `to-pip-1.4/to_pip.egg-info/PKG-INFO` & `to-pip-1.5/to_pip.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: to-pip
-Version: 1.4
+Version: 1.5
 Summary: UNKNOWN
 Home-page: UNKNOWN
 License: UNKNOWN
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
 
 # To-pip
```

### Comparing `to-pip-1.4/to_pip.py` & `to-pip-1.5/to_pip.py`

 * *Files 26% similar despite different names*

```diff
@@ -19,52 +19,53 @@
     parser.add_argument("-v", "--package_version", help="Package version", required=True)
     parser.add_argument("-u", "--pypi_username", help="PyPI username", default="")
     parser.add_argument("-p", "--pypi_password", help="PyPI password", default="")
     parser.add_argument("python_files", nargs="*", help="Python files to include")
     return parser.parse_args()
 
 
-def to_pip():
-    args = parse_args()
-
-    if not args.python_files:
-        usage()
-
+def create_package_dir(package_name, package_version, python_files):
     tmp_dir = tempfile.mkdtemp()
-    package_dir = os.path.join(tmp_dir, f"{args.package_name}-{args.package_version}")
+    package_dir = os.path.join(tmp_dir, f"{package_name}-{package_version}")
     os.makedirs(package_dir)
 
-    for file in args.python_files:
-        with open(file) as src, open(
-                os.path.join(package_dir, os.path.basename(file)), "w"
-        ) as dest:
+    for file in python_files:
+        file_name = os.path.basename(file)
+        if os.path.exists(os.path.join(package_dir, file_name)):
+            print(f"Error: File {file_name} already exists in the package directory.")
+            sys.exit(1)
+        with open(file) as src, open(os.path.join(package_dir, file_name), "w") as dest:
             dest.write("#!/usr/bin/env python\n")
             dest.write(src.read())
         os.system(f"chmod +x {os.path.join(package_dir, os.path.basename(file))}")
 
     if os.path.exists("requirements.txt"):
         shutil.copy("requirements.txt", os.path.join(package_dir, "requirements.txt"))
 
-    modules = ", ".join([f"'{os.path.basename(file).split('.')[0].replace('-', '_')}'" for file in args.python_files])
+    return package_dir
+
+
+def write_setup_py(package_dir, package_name, package_version, python_files):
+    modules = ", ".join([f"'{os.path.basename(file).split('.')[0].replace('-', '_')}'" for file in python_files])
     entry_points = ", ".join(
         [
             f"{os.path.basename(file).split('.')[0].replace('-', '_')} = {os.path.basename(file).split('.')[0].replace('-', '_')}:main"
-            for file in args.python_files
+            for file in python_files
         ]
     )
 
     setup_py = f"""
 from setuptools import setup, find_packages
 
 with open('requirements.txt') as f:
     requirements = [line.strip() for line in f.readlines()]
 
 setup(
-    name="{args.package_name}",
-    version="{args.package_version}",
+    name="{package_name}",
+    version="{package_version}",
     packages=find_packages(),
     py_modules=[{modules}],
     install_requires=requirements,
     entry_points={{
         'console_scripts': [
             '{entry_points}',
         ],
@@ -72,35 +73,69 @@
     long_description=open('README.md', 'r').read(),
     long_description_content_type='text/markdown',)
 """
 
     with open(os.path.join(package_dir, "setup.py"), "w") as f:
         f.write(setup_py)
 
+
+def handle_readme(package_dir, package_name):
     if os.path.exists("README.md"):
         shutil.copy("README.md", os.path.join(package_dir, "README.md"))
+    else:
+        with open(os.path.join(package_dir, "README.md"), "w") as f:
+            f.write(f"# {package_name}\n\nThis is a placeholder README.md file.")
 
-    os.system(f"cd {package_dir} && python setup.py sdist bdist_wheel")
 
-    if args.pypi_username and args.pipy_password:
-        pypirc_content = f"""
+def create_pypirc_file(pypi_username, pypi_password):
+    pypirc_content = f"""
 [distutils]
 index-servers =
   pypi
 
 [pypi]
 repository: https://upload.pypi.org/legacy/
-username: {args.pipy_username}
-password: {args.pipy_password}
+username: {pypi_username}
+password: {pypi_password}
 """
-        with open(os.path.expanduser("~/.pypirc"), "w") as f:
-            f.write(pypirc_content)
+    with open(os.path.expanduser("~/.pypirc"), "w") as f:
+        f.write(pypirc_content)
+
+
+def to_pip(python_files, package_name, package_version, pypi_username=None, pypi_password=None):
+    if not python_files:
+        usage()
+
+    package_dir = create_package_dir(package_name, package_version, python_files)
+    write_setup_py(package_dir, package_name, package_version, python_files)
+    handle_readme(package_dir, package_name)
+
+    if pypi_username and pypi_password:
+        create_pypirc_file(pypi_username, pypi_password)
+
+    # Build the package before uploading
+    build_exit_code = os.system(f"cd {package_dir} && python setup.py sdist bdist_wheel")
+    if build_exit_code != 0:
+        print("Error: Failed to build the package.")
+        sys.exit(1)
+
+    exit_code = os.system(f"cd {package_dir} && twine upload dist/*")
+    if exit_code != 0:
+        print("Error: Failed to upload the package.")
+        sys.exit(1)
+
+
+def to_pip_args():
+    args = parse_args()
+
+    if not args.python_files:
+        usage()
 
-    os.system(f"cd {package_dir} && twine upload dist/*")
+    to_pip(args.python_files, args.package_name, args.package_version, args.pypi_username, args.pypi_password)
 
 
 def main():
-    to_pip()
+    to_pip_args()
 
 
 if __name__ == "__main__":
-    main()
+    main()
```

