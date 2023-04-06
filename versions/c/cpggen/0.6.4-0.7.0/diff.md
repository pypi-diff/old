# Comparing `tmp/cpggen-0.6.4.tar.gz` & `tmp/cpggen-0.7.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cpggen-0.6.4.tar", max compression
+gzip compressed data, was "cpggen-0.7.0.tar", max compression
```

## Comparing `cpggen-0.6.4.tar` & `cpggen-0.7.0.tar`

### file list

```diff
@@ -1,9 +1,9 @@
--rw-r--r--   0        0        0    11357 2023-04-06 01:53:20.269569 cpggen-0.6.4/LICENSE
--rw-r--r--   0        0        0     4409 2023-04-06 01:53:20.269569 cpggen-0.6.4/README.md
--rw-r--r--   0        0        0        0 2023-04-06 01:53:20.269569 cpggen-0.6.4/cpggen/__init__.py
--rw-r--r--   0        0        0     8125 2023-04-06 01:53:20.269569 cpggen-0.6.4/cpggen/cli.py
--rw-r--r--   0        0        0    15120 2023-04-06 01:53:20.269569 cpggen-0.6.4/cpggen/executor.py
--rw-r--r--   0        0        0      732 2023-04-06 01:53:20.269569 cpggen-0.6.4/cpggen/logger.py
--rw-r--r--   0        0        0     9677 2023-04-06 01:53:20.269569 cpggen-0.6.4/cpggen/utils.py
--rw-r--r--   0        0        0     1245 2023-04-06 01:53:20.269569 cpggen-0.6.4/pyproject.toml
--rw-r--r--   0        0        0     5737 1970-01-01 00:00:00.000000 cpggen-0.6.4/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-06 10:38:38.834535 cpggen-0.7.0/LICENSE
+-rw-r--r--   0        0        0     4409 2023-04-06 10:38:38.834535 cpggen-0.7.0/README.md
+-rw-r--r--   0        0        0        0 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/__init__.py
+-rw-r--r--   0        0        0     8264 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/cli.py
+-rw-r--r--   0        0        0    16008 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/executor.py
+-rw-r--r--   0        0        0      732 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/logger.py
+-rw-r--r--   0        0        0     9581 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/utils.py
+-rw-r--r--   0        0        0     1245 2023-04-06 10:38:38.834535 cpggen-0.7.0/pyproject.toml
+-rw-r--r--   0        0        0     5737 1970-01-01 00:00:00.000000 cpggen-0.7.0/PKG-INFO
```

### Comparing `cpggen-0.6.4/LICENSE` & `cpggen-0.7.0/LICENSE`

 * *Files identical despite different names*

### Comparing `cpggen-0.6.4/README.md` & `cpggen-0.7.0/README.md`

 * *Files identical despite different names*

### Comparing `cpggen-0.6.4/cpggen/cli.py` & `cpggen-0.7.0/cpggen/cli.py`

 * *Files 2% similar despite different names*

```diff
@@ -233,24 +233,27 @@
     if args.server_mode:
         return run_server(args)
     src = args.src
     cpg_out_dir = args.cpg_out_dir
     languages = args.language
     joern_home = args.joern_home
     use_container = args.use_container
-    if not os.path.exists(joern_home):
+    if joern_home and not os.path.exists(joern_home):
         if utils.check_command("docker") or utils.check_command("podman"):
             use_container = True
         else:
             console.print(
                 "Joern installation was not found. Please install joern by following the instructions at https://joern.io and set the environment variable JOERN_HOME to the directory containing the cli tools"
             )
             console.print(
                 "Alternatively, ensure docker or podman is available to use cpggen container image"
             )
+    # GitHub action is very weird
+    if os.getenv("GITHUB_PATH") and utils.check_command("joern"):
+        joern_home = ""
     is_temp_dir = False
     if src.startswith("http") or src.startswith("git"):
         clone_dir = tempfile.mkdtemp(prefix="cpggen")
         src = utils.clone_repo(src, clone_dir)
         is_temp_dir = True
     if not languages or languages == "autodetect":
         languages = utils.detect_project_type(src)
```

### Comparing `cpggen-0.6.4/cpggen/executor.py` & `cpggen-0.7.0/cpggen/executor.py`

 * *Files 9% similar despite different names*

```diff
@@ -2,15 +2,14 @@
 import os
 import subprocess
 import tempfile
 from pathlib import Path
 
 import psutil
 from psutil._common import bytes2human
-from rich.markdown import Markdown
 from rich.progress import Progress
 
 from cpggen.logger import DEBUG, LOG, console
 from cpggen.utils import (
     check_command,
     find_csharp_artifacts,
     find_go_mods,
@@ -40,31 +39,32 @@
     except Exception:
         return default_value
 
 
 cpg_tools_map = {
     "c": "%(joern_home)sc2cpg.sh -J-Xmx%(memory)s -o %(cpg_out)s %(src)s --with-include-auto-discovery",
     "cpp": "%(joern_home)sc2cpg.sh -J-Xmx%(memory)s -o %(cpg_out)s %(src)s --with-include-auto-discovery",
-    "java": "%(joern_home)sjavasrc2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s",
-    "java-with-deps": "%(joern_home)sjavasrc2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s --fetch-dependencies",
+    "java": "%(joern_home)sjavasrc2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s --fetch-dependencies",
     "binary": "%(joern_home)sghidra2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s",
     "js": "%(joern_home)sjssrc2cpg.sh -J-Xmx%(memory)s -o %(cpg_out)s %(src)s",
     "ts": "%(joern_home)sjssrc2cpg.sh -J-Xmx%(memory)s -o %(cpg_out)s %(src)s",
     "kotlin": "%(joern_home)skotlin2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s",
     "kotlin-with-deps": "%(joern_home)skotlin2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s --download-dependencies",
     "kotlin-with-classpath": "%(joern_home)skotlin2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s --classpath %(home_dir)s/.m2 --classpath %(home_dir)s/.gradle/caches/modules-2/files-2.1",
     "php": "%(joern_home)sphp2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s",
     "python": "%(joern_home)spysrc2cpg -J-Xmx%(memory)s -o %(cpg_out)s %(src)s",
     "csharp": "%(joern_home)scsharp2cpg -i %(csharp_artifacts)s -o %(cpg_out)s --ignore-tests -l error",
     "dotnet": "%(joern_home)scsharp2cpg -i %(csharp_artifacts)s -o %(cpg_out)s --ignore-tests -l error",
     "go": "%(joern_home)sgo2cpg generate -o %(cpg_out)s ./...",
-    "jar": "java -Xmx%(memory)s -jar %(joern_home)s/java2cpg.jar %(uber_jar)s -nojsp -nb --experimental-langs scala -su -o %(cpg_out)s",
-    "scala": "java -Xmx%(memory)s -jar %(joern_home)s/java2cpg.jar %(uber_jar)s -nojsp -nb --experimental-langs scala -su -o %(cpg_out)s",
-    "jsp": "java -Xmx%(memory)s -jar %(joern_home)s/java2cpg.jar %(uber_jar)s -nb --experimental-langs scala -su -o %(cpg_out)s",
-    "sbom": "cdxgen -t %(tool_lang)s -o %(sbom_out)s %(src)s",
+    "jar": "java -Xmx%(memory)s -jar /usr/local/bin/java2cpg.jar -nojsp -nb --experimental-langs scala -su -o %(cpg_out)s %(uber_jar)s",
+    "jar-with-blocklist": "java -Xmx%(memory)s -jar /usr/local/bin/java2cpg.jar -nojsp --experimental-langs scala -su -o %(cpg_out)s %(uber_jar)s",
+    "scala": "java -Xmx%(memory)s -jar /usr/local/bin/java2cpg.jar -nojsp -nb --experimental-langs scala -su -o %(cpg_out)s %(uber_jar)s",
+    "jsp": "java -Xmx%(memory)s -jar /usr/local/bin/java2cpg.jar -nb --experimental-langs scala -su -o %(cpg_out)s %(uber_jar)s",
+    "jsp-with-blocklist": "java -Xmx%(memory)s -jar /usr/local/bin/java2cpg.jar --experimental-langs scala -su -o %(cpg_out)s %(uber_jar)s",
+    "sbom": "cdxgen -r -t %(tool_lang)s -o %(sbom_out)s %(src)s",
 }
 
 build_tools_map = {
     "csharp": ["dotnet", "build"],
     "java": {
         "maven": [
             get("MVN_CMD", "mvn"),
@@ -106,15 +106,15 @@
     go_mods = find_go_mods(src)
     makes = find_makefiles(src)
     build_args = build_tools_map["go"]
     for gmod in go_mods:
         base_dir = os.path.dirname(gmod)
         try:
             LOG.debug(f"Executing {' '.join(build_args)} in {base_dir}")
-            cp = subprocess.run(
+            subprocess.run(
                 build_args,
                 stdout=subprocess.DEVNULL,
                 stderr=subprocess.DEVNULL,
                 cwd=base_dir,
                 env=env,
                 check=False,
                 shell=False,
@@ -123,15 +123,15 @@
         except Exception as e:
             LOG.debug(e)
     build_args = build_tools_map["make"]
     for make in makes:
         base_dir = os.path.dirname(make)
         try:
             LOG.debug(f"Executing {' '.join(build_args)} in {base_dir}")
-            cp = subprocess.run(
+            subprocess.run(
                 build_args,
                 stdout=subprocess.DEVNULL,
                 stderr=subprocess.DEVNULL,
                 cwd=base_dir,
                 env=env,
                 check=False,
                 shell=False,
@@ -205,24 +205,14 @@
                 "[green]" + tool_verb + " " + tool_lang + " frontend",
                 total=100,
                 start=False,
             )
             cmd_with_args = cpg_tools_map.get(tool_lang)
             if not cmd_with_args:
                 return
-            if use_container:
-                # We need to make src an absolute path since relative paths wouldn't work in container mode
-                src = os.path.abspath(src)
-                container_cli = "docker"
-                if check_command("podman"):
-                    container_cli = "podman"
-                # cmd_with_args = f"""{container_cli} run --rm -w {os.path.abspath(src)} -v /tmp:/tmp -v {os.path.abspath(src)}:{os.path.abspath(src)}:rw -v {os.path.abspath(cpg_out_dir)}:{os.path.abspath(cpg_out_dir)}:rw --cpus={os.getenv("CPGGEN_CONTAINER_CPU", cpu_count)} --memory={os.getenv("CPGGEN_CONTAINER_MEMORY", max_memory)} -t {os.getenv("CPGGEN_IMAGE", "ghcr.io/appthreat/cpggen")} {cmd_with_args}"""
-                cmd_with_args = f"""{container_cli} run --rm -w {src} -v {tempfile.gettempdir()}:/tmp -v {src}:{src}:rw -v {os.path.abspath(cpg_out_dir)}:{os.path.abspath(cpg_out_dir)}:rw -t {os.getenv("CPGGEN_IMAGE", "ghcr.io/appthreat/cpggen")} {cmd_with_args}"""
-                # We need to fix joern_home to the directory inside the container
-                joern_home = ""
             uber_jar = ""
             csharp_artifacts = ""
             # For languages like scala, jsp or jar we need to create a uber jar containing all jar, war files from the source directory
             if "uber_jar" in cmd_with_args:
                 stdout = subprocess.PIPE
                 java_artifacts = find_java_artifacts(src)
                 if len(java_artifacts) == 1:
@@ -238,14 +228,23 @@
             # For go, the modules are based on the presence of go.mod files
             if tool_lang == "go":
                 go_mods = find_go_mods(src)
                 if go_mods:
                     modules = [os.path.dirname(gmod) for gmod in go_mods]
             for amodule in modules:
                 cmd_with_args = cpg_tools_map.get(tool_lang)
+                if use_container:
+                    # We need to make src an absolute path since relative paths wouldn't work in container mode
+                    amodule = os.path.abspath(amodule)
+                    container_cli = "docker"
+                    if check_command("podman"):
+                        container_cli = "podman"
+                    cmd_with_args = f"""{container_cli} run --rm -w {amodule} -v {tempfile.gettempdir()}:/tmp -v {amodule}:{amodule}:rw -v {os.path.abspath(cpg_out_dir)}:{os.path.abspath(cpg_out_dir)}:rw -t {os.getenv("CPGGEN_IMAGE", "ghcr.io/appthreat/cpggen")} {cmd_with_args}"""
+                    # We need to fix joern_home to the directory inside the container
+                    joern_home = ""
                 sbom_cmd_with_args = cpg_tools_map.get("sbom")
                 cpg_out = (
                     cpg_out_dir
                     if cpg_out_dir.endswith(".bin.zip")
                     or cpg_out_dir.endswith(".bin")
                     or cpg_out_dir.endswith(".cpg")
                     else os.path.join(
@@ -299,14 +298,29 @@
                         os.path.basename(amodule),
                         " ".join(cmd_list_with_args),
                     )
                 )
                 cwd = amodule
                 if tool_lang in ("binary",):
                     cwd = os.getcwd()
+                # Generate sbom first since this would even download dependencies for java
+                try:
+                    subprocess.run(
+                        sbom_cmd_list_with_args,
+                        stdout=stdout,
+                        stderr=stderr,
+                        cwd=cwd,
+                        env=env,
+                        check=False,
+                        shell=False,
+                        encoding="utf-8",
+                    )
+                except Exception:
+                    # Ignore sbom generation errors
+                    pass
                 cp = subprocess.run(
                     cmd_list_with_args,
                     stdout=stdout,
                     stderr=stderr,
                     cwd=cwd,
                     env=env,
                     check=False,
@@ -319,50 +333,53 @@
                 if (
                     cp
                     and LOG.isEnabledFor(DEBUG)
                     and cp.returncode
                     and cp.stdout is not None
                 ):
                     LOG.debug(cp.stdout)
-                # Generate sbom
-                try:
-                    subprocess.run(
-                        sbom_cmd_list_with_args,
-                        stdout=stdout,
-                        stderr=stderr,
-                        cwd=cwd,
-                        env=env,
-                        check=False,
-                        shell=False,
-                        encoding="utf-8",
-                    )
-                except Exception:
-                    # Ignore sbom generation errors
-                    pass
                 progress.update(task, completed=100, total=100)
                 if os.path.exists(cpg_out):
-                    LOG.info(
-                        f"""CPG for {tool_lang} is {cpg_out}. You can import this in joern using importCpg("{cpg_out}")"""
-                    )
+                    # go2cpg seems to produce a cpg without read permissions
+                    try:
+                        os.chmod(cpg_out, 0o644)
+                    except Exception:
+                        # Ignore errors
+                        pass
+                    if os.getenv("CI"):
+                        LOG.info(
+                            f"""CPG {cpg_out} generated successfully for {tool_lang}."""
+                        )
+                    else:
+                        LOG.info(
+                            f"""CPG for {tool_lang} is {cpg_out}. You can import this in joern using importCpg("{cpg_out}")"""
+                        )
                     with open(manifest_out, mode="w") as mfp:
+                        # In case of github action, we need to convert this to relative path
+                        if os.getenv("GITHUB_PATH"):
+                            cpg_out = cpg_out.replace("/github/workspace/", "")
+                            sbom_out = sbom_out.replace("/github/workspace/", "")
+                            amodule = amodule.replace("/github/workspace/", "")
+                        language = tool_lang.split("-")[0]
+                        # Override the language for jvm
+                        if language in ("jar", "scala"):
+                            language = "java"
                         json.dump(
                             {
                                 "src": amodule,
                                 "cpg": cpg_out,
                                 "sbom": sbom_out,
-                                "language": tool_lang,
+                                "language": language,
                                 "cpg_frontend_invocation": " ".join(cmd_list_with_args),
                                 "sbom_invocation": " ".join(sbom_cmd_list_with_args),
                             },
                             mfp,
                         )
                 else:
-                    LOG.info(
-                        f"CPG {cpg_out} was not generated successfully for {tool_lang}"
-                    )
+                    LOG.info(f"CPG {cpg_out} was not generated for {tool_lang}")
                     if cp.stdout:
                         LOG.info(cp.stdout)
                     if cp.stderr:
                         LOG.info(cp.stderr)
         except Exception as e:
             if task:
                 progress.update(task, completed=20, total=10, visible=False)
```

### Comparing `cpggen-0.6.4/cpggen/logger.py` & `cpggen-0.7.0/cpggen/logger.py`

 * *Files identical despite different names*

### Comparing `cpggen-0.6.4/cpggen/utils.py` & `cpggen-0.7.0/cpggen/utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -296,28 +296,25 @@
         src_dir, ".php", False, True
     ):
         project_types.append("php")
     if find_files(src_dir, ".sbt", False, True) or find_files(
         src_dir, ".scala", False, True
     ):
         project_types.append("scala")
-    if find_files(src_dir, ".kt", False, True) or find_files(
-        src_dir, ".kts", False, True
-    ):
-        if gradle_cache_exists:
+    if find_files(src_dir, ".kt", False, True):
+        if maven_cache_exists or gradle_cache_exists:
             project_types.append("kotlin-with-classpath")
         else:
             project_types.append("kotlin")
-    if find_files(src_dir, "pom.xml", False, True) or find_files(
-        src_dir, ".gradle", False, True
+    if (
+        find_files(src_dir, "pom.xml", False, True)
+        or find_files(src_dir, ".gradle", False, True)
+        or find_files(src_dir, ".java", False, True)
     ):
-        if gradle_cache_exists or maven_cache_exists:
-            project_types.append("java-with-deps")
-        else:
-            project_types.append("java")
+        project_types.append("java")
     if find_files(src_dir, ".jsp", False, True):
         project_types.append("jsp")
     if (
         find_files(src_dir, "package.json", False, True)
         or find_files(src_dir, "yarn.lock", False, True)
         or find_files(src_dir, ".js", False, True)
         or find_files(src_dir, ".ts", False, True)
```

### Comparing `cpggen-0.6.4/pyproject.toml` & `cpggen-0.7.0/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "cpggen"
-version = "0.6.4"
+version = "0.7.0"
 description = "Generate CPG for multiple languages for use with joern"
 authors = ["Team AppThreat <cloud@appthreat.com>"]
 license = "Apache-2.0"
 readme = "README.md"
 packages = [{include = "cpggen"}]
 homepage = "https://github.com/AppThreat/cpggen"
 repository = "https://github.com/AppThreat/cpggen"
```

### Comparing `cpggen-0.6.4/PKG-INFO` & `cpggen-0.7.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cpggen
-Version: 0.6.4
+Version: 0.7.0
 Summary: Generate CPG for multiple languages for use with joern
 Home-page: https://github.com/AppThreat/cpggen
 License: Apache-2.0
 Keywords: joern,code analysis,static analysis,cpg,code property graph
 Author: Team AppThreat
 Author-email: cloud@appthreat.com
 Requires-Python: >=3.8,<3.12
```

