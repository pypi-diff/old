# Comparing `tmp/mpyl-0.0.8-py3-none-any.whl.zip` & `tmp/mpyl-0.0.9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,70 +1,72 @@
-Zip file size: 70700 bytes, number of entries: 68
--rw-r--r--  2.0 unx     1952 b- defN 23-Mar-13 15:41 mpyl/__init__.py
--rw-r--r--  2.0 unx      215 b- defN 23-Mar-13 15:41 mpyl/__main__.py
--rw-r--r--  2.0 unx    11406 b- defN 23-Mar-13 15:41 mpyl/project.py
--rw-r--r--  2.0 unx     1069 b- defN 23-Mar-13 15:41 mpyl/validation.py
--rw-r--r--  2.0 unx       38 b- defN 23-Mar-13 15:41 mpyl/cli/__init__.py
--rw-r--r--  2.0 unx       51 b- defN 23-Mar-13 15:41 mpyl/cli/build/__init__.py
--rw-r--r--  2.0 unx     2212 b- defN 23-Mar-13 15:41 mpyl/cli/build/jenkins.py
--rw-r--r--  2.0 unx     4353 b- defN 23-Mar-13 15:41 mpyl/cli/build/mpyl.py
--rw-r--r--  2.0 unx       19 b- defN 23-Mar-13 15:41 mpyl/cli/commands/__init__.py
--rw-r--r--  2.0 unx     3210 b- defN 23-Mar-13 15:41 mpyl/cli/commands/build.py
--rw-r--r--  2.0 unx     2178 b- defN 23-Mar-13 15:41 mpyl/cli/commands/meta_info.py
--rw-r--r--  2.0 unx     1457 b- defN 23-Mar-13 15:41 mpyl/cli/commands/projects.py
--rw-r--r--  2.0 unx        0 b- defN 23-Mar-13 15:41 mpyl/projects/__init__.py
--rw-r--r--  2.0 unx      265 b- defN 23-Mar-13 15:41 mpyl/projects/find.py
--rw-r--r--  2.0 unx       92 b- defN 23-Mar-13 15:41 mpyl/reporting/__init__.py
--rw-r--r--  2.0 unx       76 b- defN 23-Mar-13 15:41 mpyl/reporting/formatting/__init__.py
--rw-r--r--  2.0 unx     2564 b- defN 23-Mar-13 15:41 mpyl/reporting/formatting/markdown.py
--rw-r--r--  2.0 unx     1148 b- defN 23-Mar-13 15:41 mpyl/reporting/formatting/text.py
--rw-r--r--  2.0 unx      488 b- defN 23-Mar-13 15:41 mpyl/reporting/targets/__init__.py
--rw-r--r--  2.0 unx     5538 b- defN 23-Mar-13 15:41 mpyl/reporting/targets/github.py
--rw-r--r--  2.0 unx     4264 b- defN 23-Mar-13 15:41 mpyl/reporting/targets/jira.py
--rw-r--r--  2.0 unx     5755 b- defN 23-Mar-13 15:41 mpyl/reporting/targets/slack.py
--rw-r--r--  2.0 unx     5688 b- defN 23-Mar-13 15:41 mpyl/schema/mpyl_config.schema.yml
--rw-r--r--  2.0 unx    26691 b- defN 23-Mar-13 15:41 mpyl/schema/project.schema.yml
--rw-r--r--  2.0 unx        0 b- defN 23-Mar-13 15:41 mpyl/stages/__init__.py
--rw-r--r--  2.0 unx     2408 b- defN 23-Mar-13 15:41 mpyl/stages/discovery.py
--rw-r--r--  2.0 unx     6135 b- defN 23-Mar-13 15:41 mpyl/steps/__init__.py
--rw-r--r--  2.0 unx     4536 b- defN 23-Mar-13 15:41 mpyl/steps/models.py
--rw-r--r--  2.0 unx     1589 b- defN 23-Mar-13 15:41 mpyl/steps/run.py
--rw-r--r--  2.0 unx     5715 b- defN 23-Mar-13 15:41 mpyl/steps/steps.py
--rw-r--r--  2.0 unx       59 b- defN 23-Mar-13 15:41 mpyl/steps/build/__init__.py
--rw-r--r--  2.0 unx     2255 b- defN 23-Mar-13 15:41 mpyl/steps/build/docker_after_build.py
--rw-r--r--  2.0 unx     2032 b- defN 23-Mar-13 15:41 mpyl/steps/build/dockerbuild.py
--rw-r--r--  2.0 unx      765 b- defN 23-Mar-13 15:41 mpyl/steps/build/echo.py
--rw-r--r--  2.0 unx     2388 b- defN 23-Mar-13 15:41 mpyl/steps/build/sbt.py
--rw-r--r--  2.0 unx       60 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/__init__.py
--rw-r--r--  2.0 unx     1001 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/echo.py
--rw-r--r--  2.0 unx     1960 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/kubernetes.py
--rw-r--r--  2.0 unx        0 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/__init__.py
--rw-r--r--  2.0 unx     2195 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/helm.py
--rw-r--r--  2.0 unx     1431 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/rancher.py
--rw-r--r--  2.0 unx    11097 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/service.py
--rw-r--r--  2.0 unx        0 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/resources/__init__.py
--rw-r--r--  2.0 unx     4418 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/resources/crd.py
--rw-r--r--  2.0 unx     1330 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/resources/customresources.py
--rw-r--r--  2.0 unx    11697 b- defN 23-Mar-13 15:41 mpyl/steps/deploy/k8s/resources/schema/traeffik.schema.yml
--rw-r--r--  2.0 unx       58 b- defN 23-Mar-13 15:41 mpyl/steps/test/__init__.py
--rw-r--r--  2.0 unx     1428 b- defN 23-Mar-13 15:41 mpyl/steps/test/after_test.py
--rw-r--r--  2.0 unx     2453 b- defN 23-Mar-13 15:41 mpyl/steps/test/before_test.py
--rw-r--r--  2.0 unx     2830 b- defN 23-Mar-13 15:41 mpyl/steps/test/dockertest.py
--rw-r--r--  2.0 unx      724 b- defN 23-Mar-13 15:41 mpyl/steps/test/echo.py
--rw-r--r--  2.0 unx     4706 b- defN 23-Mar-13 15:41 mpyl/steps/test/sbt.py
--rw-r--r--  2.0 unx        0 b- defN 23-Mar-13 15:41 mpyl/utilities/__init__.py
--rw-r--r--  2.0 unx     3315 b- defN 23-Mar-13 15:41 mpyl/utilities/docker/__init__.py
--rw-r--r--  2.0 unx     1547 b- defN 23-Mar-13 15:41 mpyl/utilities/github/__init__.py
--rw-r--r--  2.0 unx     1542 b- defN 23-Mar-13 15:41 mpyl/utilities/jenkins/__init__.py
--rw-r--r--  2.0 unx     5016 b- defN 23-Mar-13 15:41 mpyl/utilities/jenkins/runner.py
--rw-r--r--  2.0 unx     1280 b- defN 23-Mar-13 15:41 mpyl/utilities/junit/__init__.py
--rw-r--r--  2.0 unx      754 b- defN 23-Mar-13 15:41 mpyl/utilities/pyaml_env/__init__.py
--rw-r--r--  2.0 unx     2558 b- defN 23-Mar-13 15:41 mpyl/utilities/repo/__init__.py
--rw-r--r--  2.0 unx     1087 b- defN 23-Mar-13 15:41 mpyl/utilities/sbt/__init__.py
--rw-r--r--  2.0 unx     1338 b- defN 23-Mar-13 15:41 mpyl/utilities/subprocess/__init__.py
--rw-r--r--  2.0 unx    11357 b- defN 23-Mar-13 15:42 mpyl-0.0.8.dist-info/LICENSE
--rw-r--r--  2.0 unx     2914 b- defN 23-Mar-13 15:42 mpyl-0.0.8.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Mar-13 15:42 mpyl-0.0.8.dist-info/WHEEL
--rw-r--r--  2.0 unx       35 b- defN 23-Mar-13 15:42 mpyl-0.0.8.dist-info/entry_points.txt
--rw-r--r--  2.0 unx        5 b- defN 23-Mar-13 15:42 mpyl-0.0.8.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     5759 b- defN 23-Mar-13 15:42 mpyl-0.0.8.dist-info/RECORD
-68 files, 194598 bytes uncompressed, 61558 bytes compressed:  68.4%
+Zip file size: 74388 bytes, number of entries: 70
+-rw-r--r--  2.0 unx     1927 b- defN 23-Mar-16 09:26 mpyl/__init__.py
+-rw-r--r--  2.0 unx      215 b- defN 23-Mar-16 09:26 mpyl/__main__.py
+-rw-r--r--  2.0 unx    11538 b- defN 23-Mar-16 09:26 mpyl/project.py
+-rw-r--r--  2.0 unx     1069 b- defN 23-Mar-16 09:26 mpyl/validation.py
+-rw-r--r--  2.0 unx      568 b- defN 23-Mar-16 09:26 mpyl/cli/__init__.py
+-rw-r--r--  2.0 unx       51 b- defN 23-Mar-16 09:26 mpyl/cli/build/__init__.py
+-rw-r--r--  2.0 unx     2250 b- defN 23-Mar-16 09:26 mpyl/cli/build/jenkins.py
+-rw-r--r--  2.0 unx     4542 b- defN 23-Mar-16 09:26 mpyl/cli/build/mpyl.py
+-rw-r--r--  2.0 unx      471 b- defN 23-Mar-16 09:26 mpyl/cli/commands/__init__.py
+-rw-r--r--  2.0 unx     4539 b- defN 23-Mar-16 09:26 mpyl/cli/commands/build.py
+-rw-r--r--  2.0 unx     2170 b- defN 23-Mar-16 09:26 mpyl/cli/commands/meta_info.py
+-rw-r--r--  2.0 unx     1756 b- defN 23-Mar-16 09:26 mpyl/cli/commands/projects.py
+-rw-r--r--  2.0 unx       39 b- defN 23-Mar-16 09:26 mpyl/cli/projects/__init__.py
+-rw-r--r--  2.0 unx        0 b- defN 23-Mar-16 09:26 mpyl/projects/__init__.py
+-rw-r--r--  2.0 unx      265 b- defN 23-Mar-16 09:26 mpyl/projects/find.py
+-rw-r--r--  2.0 unx       92 b- defN 23-Mar-16 09:26 mpyl/reporting/__init__.py
+-rw-r--r--  2.0 unx       76 b- defN 23-Mar-16 09:26 mpyl/reporting/formatting/__init__.py
+-rw-r--r--  2.0 unx     2622 b- defN 23-Mar-16 09:26 mpyl/reporting/formatting/markdown.py
+-rw-r--r--  2.0 unx     1148 b- defN 23-Mar-16 09:26 mpyl/reporting/formatting/text.py
+-rw-r--r--  2.0 unx      488 b- defN 23-Mar-16 09:26 mpyl/reporting/targets/__init__.py
+-rw-r--r--  2.0 unx     5538 b- defN 23-Mar-16 09:26 mpyl/reporting/targets/github.py
+-rw-r--r--  2.0 unx     4656 b- defN 23-Mar-16 09:26 mpyl/reporting/targets/jira.py
+-rw-r--r--  2.0 unx     5755 b- defN 23-Mar-16 09:26 mpyl/reporting/targets/slack.py
+-rw-r--r--  2.0 unx     5920 b- defN 23-Mar-16 09:26 mpyl/schema/mpyl_config.schema.yml
+-rw-r--r--  2.0 unx    24999 b- defN 23-Mar-16 09:26 mpyl/schema/project.schema.yml
+-rw-r--r--  2.0 unx        0 b- defN 23-Mar-16 09:26 mpyl/stages/__init__.py
+-rw-r--r--  2.0 unx     2408 b- defN 23-Mar-16 09:26 mpyl/stages/discovery.py
+-rw-r--r--  2.0 unx     6135 b- defN 23-Mar-16 09:26 mpyl/steps/__init__.py
+-rw-r--r--  2.0 unx     4839 b- defN 23-Mar-16 09:26 mpyl/steps/models.py
+-rw-r--r--  2.0 unx     2166 b- defN 23-Mar-16 09:26 mpyl/steps/run.py
+-rw-r--r--  2.0 unx     5815 b- defN 23-Mar-16 09:26 mpyl/steps/steps.py
+-rw-r--r--  2.0 unx       59 b- defN 23-Mar-16 09:26 mpyl/steps/build/__init__.py
+-rw-r--r--  2.0 unx     2255 b- defN 23-Mar-16 09:26 mpyl/steps/build/docker_after_build.py
+-rw-r--r--  2.0 unx     2032 b- defN 23-Mar-16 09:26 mpyl/steps/build/dockerbuild.py
+-rw-r--r--  2.0 unx      765 b- defN 23-Mar-16 09:26 mpyl/steps/build/echo.py
+-rw-r--r--  2.0 unx     2402 b- defN 23-Mar-16 09:26 mpyl/steps/build/sbt.py
+-rw-r--r--  2.0 unx       60 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/__init__.py
+-rw-r--r--  2.0 unx     1001 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/echo.py
+-rw-r--r--  2.0 unx      876 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/kubernetes.py
+-rw-r--r--  2.0 unx     1008 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/kubernetes_job.py
+-rw-r--r--  2.0 unx     1491 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/__init__.py
+-rw-r--r--  2.0 unx    13565 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/chart.py
+-rw-r--r--  2.0 unx     2097 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/helm.py
+-rw-r--r--  2.0 unx     1431 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/rancher.py
+-rw-r--r--  2.0 unx        0 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/resources/__init__.py
+-rw-r--r--  2.0 unx     4418 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/resources/crd.py
+-rw-r--r--  2.0 unx     1330 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/resources/customresources.py
+-rw-r--r--  2.0 unx    11697 b- defN 23-Mar-16 09:26 mpyl/steps/deploy/k8s/resources/schema/traeffik.schema.yml
+-rw-r--r--  2.0 unx       58 b- defN 23-Mar-16 09:26 mpyl/steps/test/__init__.py
+-rw-r--r--  2.0 unx     1428 b- defN 23-Mar-16 09:26 mpyl/steps/test/after_test.py
+-rw-r--r--  2.0 unx     2453 b- defN 23-Mar-16 09:26 mpyl/steps/test/before_test.py
+-rw-r--r--  2.0 unx     2830 b- defN 23-Mar-16 09:26 mpyl/steps/test/dockertest.py
+-rw-r--r--  2.0 unx      724 b- defN 23-Mar-16 09:26 mpyl/steps/test/echo.py
+-rw-r--r--  2.0 unx     4669 b- defN 23-Mar-16 09:26 mpyl/steps/test/sbt.py
+-rw-r--r--  2.0 unx        0 b- defN 23-Mar-16 09:26 mpyl/utilities/__init__.py
+-rw-r--r--  2.0 unx     3315 b- defN 23-Mar-16 09:26 mpyl/utilities/docker/__init__.py
+-rw-r--r--  2.0 unx     1547 b- defN 23-Mar-16 09:26 mpyl/utilities/github/__init__.py
+-rw-r--r--  2.0 unx     1542 b- defN 23-Mar-16 09:26 mpyl/utilities/jenkins/__init__.py
+-rw-r--r--  2.0 unx     5016 b- defN 23-Mar-16 09:26 mpyl/utilities/jenkins/runner.py
+-rw-r--r--  2.0 unx     1280 b- defN 23-Mar-16 09:26 mpyl/utilities/junit/__init__.py
+-rw-r--r--  2.0 unx      754 b- defN 23-Mar-16 09:26 mpyl/utilities/pyaml_env/__init__.py
+-rw-r--r--  2.0 unx     2708 b- defN 23-Mar-16 09:26 mpyl/utilities/repo/__init__.py
+-rw-r--r--  2.0 unx     1520 b- defN 23-Mar-16 09:26 mpyl/utilities/sbt/__init__.py
+-rw-r--r--  2.0 unx     1338 b- defN 23-Mar-16 09:26 mpyl/utilities/subprocess/__init__.py
+-rw-r--r--  2.0 unx    11357 b- defN 23-Mar-16 09:27 mpyl-0.0.9.dist-info/LICENSE
+-rw-r--r--  2.0 unx     2914 b- defN 23-Mar-16 09:27 mpyl-0.0.9.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Mar-16 09:27 mpyl-0.0.9.dist-info/WHEEL
+-rw-r--r--  2.0 unx       35 b- defN 23-Mar-16 09:27 mpyl-0.0.9.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx        5 b- defN 23-Mar-16 09:27 mpyl-0.0.9.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     5937 b- defN 23-Mar-16 09:27 mpyl-0.0.9.dist-info/RECORD
+70 files, 202066 bytes uncompressed, 64970 bytes compressed:  67.8%
```

## zipnote {}

```diff
@@ -30,14 +30,17 @@
 
 Filename: mpyl/cli/commands/meta_info.py
 Comment: 
 
 Filename: mpyl/cli/commands/projects.py
 Comment: 
 
+Filename: mpyl/cli/projects/__init__.py
+Comment: 
+
 Filename: mpyl/projects/__init__.py
 Comment: 
 
 Filename: mpyl/projects/find.py
 Comment: 
 
 Filename: mpyl/reporting/__init__.py
@@ -108,24 +111,27 @@
 
 Filename: mpyl/steps/deploy/echo.py
 Comment: 
 
 Filename: mpyl/steps/deploy/kubernetes.py
 Comment: 
 
+Filename: mpyl/steps/deploy/kubernetes_job.py
+Comment: 
+
 Filename: mpyl/steps/deploy/k8s/__init__.py
 Comment: 
 
-Filename: mpyl/steps/deploy/k8s/helm.py
+Filename: mpyl/steps/deploy/k8s/chart.py
 Comment: 
 
-Filename: mpyl/steps/deploy/k8s/rancher.py
+Filename: mpyl/steps/deploy/k8s/helm.py
 Comment: 
 
-Filename: mpyl/steps/deploy/k8s/service.py
+Filename: mpyl/steps/deploy/k8s/rancher.py
 Comment: 
 
 Filename: mpyl/steps/deploy/k8s/resources/__init__.py
 Comment: 
 
 Filename: mpyl/steps/deploy/k8s/resources/crd.py
 Comment: 
@@ -180,26 +186,26 @@
 
 Filename: mpyl/utilities/sbt/__init__.py
 Comment: 
 
 Filename: mpyl/utilities/subprocess/__init__.py
 Comment: 
 
-Filename: mpyl-0.0.8.dist-info/LICENSE
+Filename: mpyl-0.0.9.dist-info/LICENSE
 Comment: 
 
-Filename: mpyl-0.0.8.dist-info/METADATA
+Filename: mpyl-0.0.9.dist-info/METADATA
 Comment: 
 
-Filename: mpyl-0.0.8.dist-info/WHEEL
+Filename: mpyl-0.0.9.dist-info/WHEEL
 Comment: 
 
-Filename: mpyl-0.0.8.dist-info/entry_points.txt
+Filename: mpyl-0.0.9.dist-info/entry_points.txt
 Comment: 
 
-Filename: mpyl-0.0.8.dist-info/top_level.txt
+Filename: mpyl-0.0.9.dist-info/top_level.txt
 Comment: 
 
-Filename: mpyl-0.0.8.dist-info/RECORD
+Filename: mpyl-0.0.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## mpyl/__init__.py

```diff
@@ -34,29 +34,28 @@
  - [Slack](https://slack.com/) `mpyl.reporting.targets.slack`
 
 .. include:: ../../README-usage.md
 
 .. include:: ../../README-dev.md
 """
 
-from importlib.metadata import version as version_meta
-
 import click
 
+from .cli.commands import get_version
 from .cli.commands.build import build
 from .cli.commands.meta_info import version
 from .cli.commands.projects import projects
 from .utilities.pyaml_env import parse_config
 from .utilities.repo import RepoConfig, Repository
 
 
 @click.group(name='mpyl')
 def main_group():
     """Command Line Interface for MPyL"""
 
 
 def main():
-    main_group.help = f"Command Line Interface for MPyL {version_meta('mpyl')}"
+    main_group.help = f"Command Line Interface for MPyL {get_version()}"
     main_group.add_command(projects)
     main_group.add_command(build)
     main_group.add_command(version)
     main_group()  # pylint: disable = no-value-for-parameter
```

## mpyl/project.py

```diff
@@ -11,14 +11,15 @@
 </details>
 
 .. include:: ../../README-dev.md
 """
 
 import logging
 import pkgutil
+import time
 import traceback
 from dataclasses import dataclass
 from enum import Enum
 from pathlib import Path
 from typing import Optional, TypeVar, Dict, Any, TextIO
 
 import jsonschema
@@ -192,27 +193,31 @@
 @dataclass(frozen=True)
 class Kubernetes:
     port_mappings: dict[int, int]
     liveness_probe: Optional[Probe]
     startup_probe: Optional[Probe]
     metrics: Optional[Metrics]
     resources: Resources
+    cron: dict
 
     @staticmethod
     def from_config(values: dict):
         mappings = values.get('portMappings')
         liveness_probe = values.get('livenessProbe')
         startup_probe = values.get('startupProbe')
-        metrics = values.get('metrics')
+        metrics = values.get('metrics', None)
         resources = values.get('resources')
-        return Kubernetes(port_mappings=mappings if mappings else {},
-                          liveness_probe=Probe.from_config(liveness_probe) if liveness_probe else None,
-                          startup_probe=Probe.from_config(startup_probe) if startup_probe else None,
-                          metrics=Metrics.from_config(metrics) if metrics else None,
-                          resources=Resources.from_config(resources) if resources else None)
+        return Kubernetes(
+            port_mappings=mappings if mappings else {},
+            liveness_probe=Probe.from_config(liveness_probe) if liveness_probe else None,
+            startup_probe=Probe.from_config(startup_probe) if startup_probe else None,
+            metrics=Metrics.from_config(metrics) if metrics else None,
+            resources=Resources.from_config(resources) if resources else None,
+            cron=values.get('cron', {})
+        )
 
 
 @dataclass(frozen=True)
 class Host:
     host: TargetProperty[str]
     tls: TargetProperty[str]
     whitelists: TargetProperty[list[str]]
@@ -316,15 +321,15 @@
 
 def validate_project(file: TextIO) -> dict:
     """
     :file the file to validate
     :return: the validated schema
     :raises `jsonschema.exceptions.ValidationError` when validation fails
     """
-    yaml_values = YAML().load(file)
+    yaml_values = YAML(typ='unsafe').load(file)
     template = pkgutil.get_data(__name__, "schema/project.schema.yml")
     if not template:
         raise ValueError('Schema project.schema.yml not found in package')
     validate(yaml_values, template.decode('utf-8'))
 
     return yaml_values
 
@@ -335,18 +340,18 @@
     :param root_dir: root source directory
     :param project_path: relative path from `root_dir` to the `project.yml`
     :param strict: indicates whether the schema should be validated
     :return: `Project` data class
     """
     with open(root_dir / project_path, encoding='utf-8') as file:
         try:
-            yaml_values = validate_project(file) if strict else YAML().load(file)
-
+            start = time.time()
+            yaml_values = validate_project(file) if strict else YAML(typ='unsafe').load(file)
             project = Project.from_config(yaml_values, project_path)
-            logging.debug(f'Loaded project {project.path}')
+            logging.debug(f'Loaded project {project.path} in {(time.time() - start) * 1000} ms')
             return project
         except jsonschema.exceptions.ValidationError as exc:
             logging.warning(f'{project_path} does not comply with schema: {exc.message}')
             raise
         except TypeError:
             traceback.print_exc()
             logging.warning('Type error', exc_info=True)
```

## mpyl/cli/__init__.py

```diff
@@ -1 +1,17 @@
 """Command Line Interface for MPyL"""
+import logging
+
+from rich.console import Console
+from rich.logging import RichHandler
+
+FORMAT = "%(message)s"
+
+
+def create_console_logger(local: bool, verbose: bool) -> Console:
+    console = Console(markup=True, width=None if local else 135, no_color=False, log_path=False, color_system='256')
+    logging.basicConfig(
+        level="DEBUG" if verbose else "INFO", format=FORMAT, datefmt="[%X]",
+        handlers=[RichHandler(markup=True,
+                              console=console, show_path=local)]
+    )
+    return console
```

## mpyl/cli/build/jenkins.py

```diff
@@ -42,12 +42,13 @@
                 status.update(f'Fetching Jenkins info for {pipeline_info.human_readable()} ...')
 
                 runner = JenkinsRunner(pipeline=pipeline_info,
                                        jenkins=Jenkins(jenkins_config.url, username=run_config.jenkins_user,
                                                        password=run_config.jenkins_password), status=status)
                 runner.run()
             except requests.ConnectionError:
+                status.console.bell()
                 status.console.log('⚠️ Could not connect. Are you on VPN?')
             except Exception as exc:
                 status.console.log(f'Unexpected exception: {exc}')
                 status.console.print_exception()
                 raise exc
```

## mpyl/cli/build/mpyl.py

```diff
@@ -1,32 +1,32 @@
 """Simple MPyL build runner"""
 
 import logging
-import sys
 from dataclasses import dataclass
 from pathlib import Path
 from typing import Optional
 
 from rich.console import Console
 from rich.logging import RichHandler
+from rich.markdown import Markdown
 
 from ...project import load_project, Stage, Project
 from ...reporting.formatting.markdown import run_result_to_markdown
 from ...reporting.targets import Reporter
 from ...stages.discovery import for_stage, find_invalidated_projects_per_stage
 from ...steps.models import RunProperties
 from ...steps.run import RunResult
 from ...steps.steps import Steps
 from ...utilities.repo import Repository, RepoConfig
 
 
 @dataclass(frozen=True)
 class MpylRunConfig:
     config: dict
-    run_properties: dict
+    run_properties: RunProperties
 
 
 @dataclass(frozen=True)
 class MpylCliParameters:
     local: bool
     verbose: bool = False
     all: bool = False
@@ -37,68 +37,73 @@
     run_config: MpylRunConfig
     parameters: MpylCliParameters
 
 
 FORMAT = "%(name)s  %(message)s"
 
 
+def get_build_plan(logger: logging.Logger, repo: Repository, mpyl_run_parameters: MpylRunParameters) -> RunResult:
+    params = mpyl_run_parameters.parameters
+    logger.info(f"Running with {params}")
+    if not params.local:
+        pull_result = repo.pull_main_branch()
+        logger.info(f'Pulled `{pull_result[0].remote_ref_path.strip()}` to local')
+
+    changes_in_branch = repo.changes_in_branch_including_local() if params.local else repo.changes_in_branch()
+    logger.debug(f'Changes: {changes_in_branch}')
+
+    projects_per_stage: dict[Stage, set[Project]] = find_build_set(repo, changes_in_branch, params.all)
+    return RunResult(run_properties=mpyl_run_parameters.run_config.run_properties, run_plan=projects_per_stage)
+
+
 def run_mpyl(mpyl_run_parameters: MpylRunParameters, reporter: Optional[Reporter]) -> RunResult:
     params = mpyl_run_parameters.parameters
     console = Console(markup=True, width=None if params.local else 135, no_color=False, log_path=False,
                       color_system='256')
     logging.basicConfig(
         level="DEBUG" if params.verbose else "INFO", format=FORMAT, datefmt="[%X]",
         handlers=[RichHandler(markup=True,
                               console=console, show_path=params.local)]
     )
     logger = logging.getLogger('mpyl')
     try:
         with Repository(RepoConfig(mpyl_run_parameters.run_config.config)) as repo:
 
-            logger.info(f"Running with {params}")
-            if not params.local:
-                pull_result = repo.pull_main_branch()
-                logger.info(f'Pulled `{pull_result[0].remote_ref_path.strip()}` to local')
-
-            changes_in_branch = repo.changes_in_branch_including_local() if params.local else repo.changes_in_branch()
-            logger.debug(f'Changes: {changes_in_branch}')
+            run_plan = get_build_plan(logger, repo, mpyl_run_parameters)
 
-            project_paths = repo.find_projects()
-
-            all_projects = set(map(lambda p: load_project(Path("."), Path(p), False), project_paths))
-
-            projects_per_stage: dict[Stage, set[Project]] = find_build_set(all_projects, changes_in_branch, params.all)
-
-            if params.local:
-                mpyl_run_parameters.run_config.run_properties['build']['versioning']['revision'] = repo.get_sha
-                mpyl_run_parameters.run_config.run_properties['build']['versioning']['pr_number'] = '123'
-
-            run_properties = RunProperties.from_configuration(
-                run_properties=mpyl_run_parameters.run_config.run_properties,
-                config=mpyl_run_parameters.run_config.config)
-            if not projects_per_stage.items():
+            if not run_plan.run_plan.items():
                 logger.info("Nothing to do. Exiting..")
-                sys.exit()
+                return run_plan
 
             logger.info("Building plan:")
-            run_plan = RunResult(run_properties=run_properties, run_plan=projects_per_stage)
-            logger.info(f"\n\n{run_result_to_markdown(run_plan)}")
+            console.print(Markdown(f"\n\n{run_result_to_markdown(run_plan)}"))
 
-            run_result = run_build(run_plan, Steps(logger=logger, properties=run_properties), reporter)
+            run_result: RunResult = run_plan
+            try:
+                steps = Steps(logger=logger, properties=mpyl_run_parameters.run_config.run_properties)
+                run_result = run_build(run_plan, steps, reporter)
+            except Exception as exc:  # pylint: disable=broad-except
+                console.log(f'Exception during build execution: {exc}')
+                console.print_exception()
+                run_result.exception = exc
 
-            logger.info(run_result_to_markdown(run_result))
+            console.print(run_result.status_line)
+            console.print(Markdown(run_result_to_markdown(run_result)))
             return run_result
 
     except Exception as exc:
         console.log(f'Unexpected exception: {exc}')
         console.print_exception()
         raise exc
 
 
-def find_build_set(all_projects, changes_in_branch, build_all: bool) -> dict[Stage, set[Project]]:
+def find_build_set(repo: Repository, changes_in_branch, build_all: bool) -> dict[Stage, set[Project]]:
+    project_paths = repo.find_projects()
+    all_projects = set(map(lambda p: load_project(Path("."), Path(p), False), project_paths))
+
     if build_all:
         return {Stage.BUILD: for_stage(all_projects, Stage.BUILD),
                 Stage.TEST: for_stage(all_projects, Stage.TEST),
                 Stage.DEPLOY: for_stage(all_projects, Stage.DEPLOY)}
 
     return find_invalidated_projects_per_stage(all_projects, changes_in_branch)
```

## mpyl/cli/commands/__init__.py

```diff
@@ -1 +1,23 @@
 """CLI commands"""
+import importlib
+from dataclasses import dataclass
+from importlib.metadata import version as version_meta
+
+from rich.console import Console
+
+from ...utilities.repo import Repository
+
+
+@dataclass(frozen=True)
+class CliContext:
+    config: dict
+    repo: Repository
+    console: Console
+    verbose: bool
+
+
+def get_version():
+    try:
+        return f"v{version_meta('mpyl')}"
+    except importlib.metadata.PackageNotFoundError:
+        return '(local)'
```

## mpyl/cli/commands/build.py

```diff
@@ -1,67 +1,85 @@
 """Commands related to build"""
 from typing import Any, Optional
 
 import click
 from click import Parameter, Context
+from rich.markdown import Markdown
 
+from . import CliContext
+from .. import create_console_logger
 from ..build.jenkins import JenkinsRunParameters, run_jenkins
-from ..build.mpyl import MpylRunParameters, run_mpyl, MpylCliParameters, MpylRunConfig
+from ..build.mpyl import MpylRunParameters, run_mpyl, MpylCliParameters, MpylRunConfig, find_build_set
+from ...reporting.formatting.markdown import run_result_to_markdown
+from ...steps.models import RunProperties
+from ...steps.run import RunResult
 from ...utilities.pyaml_env import parse_config
+from ...utilities.repo import Repository, RepoConfig
 
 
 @click.group('build')
 @click.option('--config', '-c', required=True, type=click.Path(exists=True), help='Path to config.yml',
-              default='config.yml')
+              envvar="MPYL_CONFIG_PATH", default='config.yml')
+@click.option('--verbose', '-v', is_flag=True, default=False)
 @click.pass_context
-def build(ctx, config):
+def build(ctx, config, verbose):
     """Pipeline build commands"""
-    if ctx.obj is None:
-        ctx.obj = {}
-    ctx.obj["config"] = parse_config(config)
+    console = create_console_logger(local=False, verbose=verbose)
+    parsed_config = parse_config(config)
+    repo = ctx.with_resource(Repository(config=RepoConfig(parsed_config)))
+    ctx.obj = CliContext(parsed_config, repo, console, verbose)
 
 
 @build.command(help='Run an MPyL build')
-@click.option('--properties', '-p', required=True, type=click.Path(exists=True), help='Path to run properties',
-              default='run_properties.yml')
+@click.option('--properties', '-p', required=False, type=click.Path(exists=False), help='Path to run properties',
+              envvar="MPYL_RUN_PROPERTIES_PATH", default='run_properties.yml')
 @click.option('--local', '-l', is_flag=True, default=True, help='Local vs CI build')
 @click.option('--all', 'all_', is_flag=True, default=False, help='Build all projects, regardless of changes on branch')
-@click.option('--verbose', '-v', is_flag=True, default=False)
 @click.pass_obj
 def run(obj, properties, local, all_, verbose):
+    run_properties = RunProperties.for_local_run(obj.config, obj.repo.get_sha, obj.repo.get_branch) if local \
+        else RunProperties.from_configuration(parse_config(properties), obj.config)
+
     run_parameters = MpylRunParameters(
-        run_config=MpylRunConfig(config=obj['config'], run_properties=parse_config(properties)),
+        run_config=MpylRunConfig(config=obj.config, run_properties=run_properties),
         parameters=MpylCliParameters(local=local, all=all_, verbose=verbose)
     )
     run_mpyl(run_parameters, None)
 
 
-@build.command()
-def status():
-    click.echo('build status')
+@build.command(help="The status of the current local branch from MPyL's perspective")
+@click.pass_obj
+def status(obj: CliContext):
+    changes_in_branch = obj.repo.changes_in_branch_including_local()
+    build_set = find_build_set(obj.repo, changes_in_branch, False)
+    run_properties = RunProperties.for_local_run(obj.config, obj.repo.get_short_sha, obj.repo.get_branch)
+    result = RunResult(run_properties=run_properties, run_plan=build_set)
+    version = run_properties.versioning
+    header: str = f"**Revision:** `{version.branch}` at `{version.revision}`  \n"
+    obj.console.print(Markdown(markup=header + "**Execution plan:**  \n" + run_result_to_markdown(result)))
 
 
 def get_default(ctx):
     if not ctx:
         return 'config.jenkins.defaultPipeline'
 
-    return ctx.obj['config']['jenkins']['defaultPipeline']
+    return ctx.obj.config['jenkins']['defaultPipeline']
 
 
 class DynamicChoice(click.Choice):
     def __init__(self):
         super().__init__([])
 
     def convert(
             self, value: Any, param: Optional[Parameter], ctx: Optional[Context]
     ) -> Any:
         if ctx is None:
             raise KeyError("Context needs to be set. Did you use @click.pass_context in the parent group?")
 
-        config = ctx.obj['config']
+        config = ctx.obj.config
         if value is None:
             value = config['jenkins']['defaultPipeline']
         self.choices = config['jenkins']['pipelines'].keys()
         return super().convert(value, param, ctx)
 
 
 @build.command(help='Run a multi branch pipeline build on Jenkins')
@@ -85,13 +103,13 @@
          'Default value is `jenkins.defaultPipeline',
     type=DynamicChoice(),
     required=True,
     default=lambda: get_default(click.get_current_context(silent=True))
 )
 @click.pass_obj
 def jenkins(obj, user, password, pipeline):
-    run_argument = JenkinsRunParameters(user, password, obj['config'], pipeline)
+    run_argument = JenkinsRunParameters(user, password, obj.config, pipeline)
     run_jenkins(run_argument)
 
 
 if __name__ == '__main__':
     build()  # pylint: disable=no-value-for-parameter
```

## mpyl/cli/commands/meta_info.py

```diff
@@ -1,14 +1,16 @@
 """Extractors for package meta information"""
 
 import os
-from importlib.metadata import version as version_meta, distribution
+from importlib.metadata import distribution
 
 import click
 
+from . import get_version
+
 VDB_LOGO = """
                                          .::.               
                                          :~~~^:.            
                                          ^~~~~~~^:.         
                .........................:~~~~~~~~~^^.       
              .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^:.    
              .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^:. 
@@ -32,15 +34,15 @@
   .^~~~~~~~~~~~~~~~~^:........................              
     .:^~~~~~~~~~~^^.                                        
        .:::^^:::.
 """
 
 
 def simple_version():
-    return f"Version {version_meta('mpyl')}"
+    return f"MPyL {get_version()}"
 
 
 def about():
     dist = distribution('mpyl')
     details = os.linesep.join(str(dist.metadata).split(os.linesep)[1:16])
     return f'{details}{VDB_LOGO}'
```

## mpyl/cli/commands/projects.py

```diff
@@ -1,46 +1,50 @@
 """Commands related to projects and how they relate"""
 from pathlib import Path
 
 import click
 import jsonschema
 
+from . import CliContext
+from .. import create_console_logger
 from ...project import validate_project
 from ...utilities.pyaml_env import parse_config
 from ...utilities.repo import Repository, RepoConfig
 
 
 @click.group('projects')
-@click.option('--config', '-c', required=True, type=click.Path(exists=True), help='Path to config.yml',
-              default='config.yml')
+@click.option('--config', '-c', required=True, type=click.Path(exists=True), help='Path to the config.yml',
+              envvar="MPYL_CONFIG_PATH", default='config.yml')
+@click.option('--verbose', '-v', is_flag=True, default=False)
 @click.pass_context
-def projects(ctx, config):
+def projects(ctx, config, verbose):
     """Commands related to projects"""
+    console = create_console_logger(local=False, verbose=verbose)
     parsed_config = parse_config(config)
-    ctx.obj = ctx.with_resource(Repository(config=RepoConfig(parsed_config)))
+    ctx.obj = CliContext(parsed_config, ctx.with_resource(Repository(config=RepoConfig(parsed_config))), console,
+                         verbose)
 
 
 @projects.command(name='list', help='List found projects')
 @click.pass_obj
-def list_projects(repo):
-    found_projects = repo.find_projects()
+def list_projects(obj: CliContext):
+    found_projects = obj.repo.find_projects()
     for proj in found_projects:
-        click.echo(proj)
+        obj.console.log(proj)
 
 
 @projects.command(help='Validate the yaml of found projects against their schema')
 @click.pass_obj
-def lint(repo):
-    found_projects: set[str] = repo.find_projects()
-    for project in found_projects:
+def lint(obj: CliContext):
+    for project in obj.repo.find_projects():
         try:
             project_path = Path('.') / Path(project)
             with open(project_path, encoding='utf-8') as file:
                 validate_project(file)
         except jsonschema.exceptions.ValidationError as exc:
-            click.echo(f'❌ {project}: {exc.message}')
+            obj.console.log(f'❌ {project}: {exc.message}')
         else:
-            click.echo(f'✅ {project}')
+            obj.console.log(f'✅ {project}')
 
 
 if __name__ == '__main__':
     projects()  # pylint: disable=no-value-for-parameter
```

## mpyl/reporting/formatting/markdown.py

```diff
@@ -40,30 +40,30 @@
     suites: list[list[TestSuite]] = list(map(to_test_suites, test_artifacts))
     flattened = list(itertools.chain(*suites))
     return flattened
 
 
 def stage_to_icon(stage: Stage):
     if stage == Stage.BUILD:
-        return 'building_construction'
+        return '🏗️ '
     if stage == Stage.TEST:
-        return 'test_tube'
+        return '🧪'
     if stage == Stage.DEPLOY:
-        return 'rocket'
-    return 'arrow_right'
+        return '🚀'
+    return '➡️'
 
 
 def run_result_to_markdown(run_result: RunResult) -> str:
-    result: str = ""
+    result: str = f'❗Exception: \n```\n{run_result.exception}\n```\n' if run_result.exception else ""
 
     for stage in Stage:
         step_results: list[StepResult] = run_result.results_for_stage(stage)
         plan: set[Project] = run_result.plan_for_stage(stage)
         if step_results or plan:
-            result += f":{stage_to_icon(stage)}: {__to_oneliner(step_results, plan)} \n"
+            result += f"{stage_to_icon(stage)}  {__to_oneliner(step_results, plan)}  \n"
             test_results = __collect_test_results(step_results)
             if test_results:
                 result += to_markdown_test_report(
                     test_results) + f' [link]({run_result.run_properties.details.tests_url}) \n'
 
     return result
```

### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

## mpyl/reporting/targets/jira.py

```diff
@@ -61,32 +61,37 @@
 
 
 @dataclass(frozen=True)
 class JiraConfig:
     site: str
     user_name: str
     password: str
+    token: Optional[str]
 
     @staticmethod
     def from_config(config: dict):
-        return JiraConfig(site=config['site'], user_name=config['userName'], password=config['password'])
+        return JiraConfig(site=config['site'], user_name=config['userName'], password=config['password'],
+                          token=config.get('token'))
 
 
 class JiraReporter(Reporter):
 
     def __init__(self, config: dict, branch: str, logger: Logger):
         jira_config = config.get('jira')
         if not jira_config:
             raise ValueError('jira section needs to be defined in config.yml')
         self._ticket = extract_ticket_from_branch(branch)
 
         jira_config = JiraConfig.from_config(jira_config)
         self._config = jira_config
-        self._jira = Jira(url=jira_config.site, username=jira_config.user_name, password=jira_config.password,
-                          api_version='3', cloud=True)
+        self._jira = Jira(url=jira_config.site, token=jira_config.token, api_version='3',
+                          cloud=True) if jira_config.token else Jira(url=jira_config.site,
+                                                                     username=jira_config.user_name,
+                                                                     password=jira_config.password,
+                                                                     api_version='3', cloud=True)
         self._logger = logger
 
     def send_report(self, results: RunResult) -> None:
         if not self._ticket:
             return None
 
         issue_response = self._jira.get_issue(self._ticket)
```

## mpyl/schema/mpyl_config.schema.yml

```diff
@@ -170,14 +170,24 @@
         type: boolean
       testWithCoverage:
         type: string
       javaOpts:
         type: string
       sbtOpts:
         type: string
+      clientMode:
+        type: object
+        additionalProperties: false
+        properties:
+          build:
+            type: boolean
+            default: true
+          test:
+            type: boolean
+            default: true
     required:
       - command
       - javaOpts
       - sbtOpts
     title: Sbt
   Project:
     type: object
@@ -226,11 +236,11 @@
         description: "Only works with the cloud version of Jira"
         type: string
         format: uri
       userName:
         type: string
       password:
         type: string
+      token:
+        type: string
     required:
       - site
-      - userName
-      - password
```

## mpyl/schema/project.schema.yml

```diff
@@ -83,14 +83,15 @@
           - Ephemeral Docker Deploy
           - Echo Deploy
           - NUC Deploy
           - Kubernetes Deploy
           - Echo Kubernetes Deploy
           - Kubernetes Job Deploy
           - Kubernetes Job Template Deploy
+          - Kubernetes Spark Job Deploy
           - CloudFront Kubernetes Deploy
           - Renew Lets Encrypt Deploy
           - Helm Deploy
           - Dagster Deploy
       postdeploy:
         description: Additional steps that can be done after the project has been deployed.
         examples:
@@ -217,57 +218,17 @@
       s3:
         additionalProperties: false
         type: object
         required:
           - bucket
         properties:
           bucket:
-            type: object
-            additionalProperties: false
-            oneOf:
-              - required:
-                  - pr
-                  - test
-                  - acceptance
-                  - production
-              - required:
-                  - all
-            properties:
-              pr:
-                type: string
-              test:
-                type: string
-              acceptance:
-                type: string
-              production:
-                type: string
-              all:
-                type: string
+            $ref: '#/definitions/dtapValue'
           path:
-            type: object
-            additionalProperties: false
-            oneOf:
-              - required:
-                  - pr
-                  - test
-                  - acceptance
-                  - production
-              - required:
-                  - all
-            properties:
-              pr:
-                type: string
-              test:
-                type: string
-              acceptance:
-                type: string
-              production:
-                type: string
-              all:
-                type: string
+            $ref: '#/definitions/dtapValue'
       kubernetes:
         $ref: '#/definitions/kubernetes'
       traefik:
         additionalProperties: false
         type: object
         properties:
           enabled:
@@ -368,14 +329,36 @@
         type: string
       acceptance:
         type: string
       production:
         type: string
       all:
         type: string
+  dtapNumberValue:
+    type: object
+    additionalProperties: false
+    oneOf:
+      - required:
+          - pr
+          - test
+          - acceptance
+          - production
+      - required:
+          - all
+    properties:
+      pr:
+        type: number
+      test:
+        type: number
+      acceptance:
+        type: number
+      production:
+        type: number
+      all:
+        type: number
   traefikHost:
     type: object
     additionalProperties: false
     required:
       - host
     properties:
       host:
@@ -678,39 +661,19 @@
           production:
             default: '512'
             type: integer
           all:
             default: '512'
             type: integer
       disk:
-        type: object
-        additionalProperties: false
+        $ref: '#/definitions/dtapValue'
         description: >-
           Sets the amount of swap space a pod can use. Note: this is not
           persistent storage.
           https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
-        oneOf:
-          - required:
-              - pr
-              - test
-              - acceptance
-              - production
-          - required:
-              - all
-        properties:
-          pr:
-            type: number
-          test:
-            type: number
-          acceptance:
-            type: number
-          production:
-            type: number
-          all:
-            type: number
   limitResources:
     type: object
     additionalProperties: false
     description: >-
       Sets the upper limit for resource consumption. Any consumption more than
       this will be curtailed.
       https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits
@@ -768,39 +731,19 @@
             type: integer
           production:
             default: '2048'
             type: integer
           all:
             type: integer
       disk:
-        type: object
-        additionalProperties: false
+        $ref: '#/definitions/dtapNumberValue'
         description: >-
           Sets the amount of swap space a pod can use. Note: this is not
           persistent storage.
           https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
-        oneOf:
-          - required:
-              - pr
-              - test
-              - acceptance
-              - production
-          - required:
-              - all
-        properties:
-          pr:
-            type: number
-          test:
-            type: number
-          acceptance:
-            type: number
-          production:
-            type: number
-          all:
-            type: number
   alert:
     type: object
     required:
       - name
       - expr
       - forDuration
       - severity
@@ -825,36 +768,53 @@
         additionalItems: false
         required:
           - name
         properties:
           name:
             type: string
       cron:
+        description: 'CronJobSpec describes how the job execution will look like and when it
+          will actually run. Identical to See https://kubernetesjsonschema.dev/v1.14.0/_definitions.json#/definitions/io.k8s.api.batch.v1beta1.CronJobSpec
+          but without jobTemplate'
         additionalProperties: false
-        type: object
-        required:
-          - schedule
         properties:
-          schedule:
-            type: string
-          successfulJobHistory:
-            type: integer
-            description: number of jobs to keep in history that succeeded
-          failedJobHistory:
-            type: integer
-            description: number of jobs to keep in history that failed
           concurrencyPolicy:
+            description: 'Specifies how to treat concurrent executions of a Job. Valid values
+              are: - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids
+              concurrent runs, skipping next run if previous run hasn''t finished yet; - "Replace":
+              cancels currently running job and replaces it with a new one
+              See https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/#concurrency-policy
+              '
             type: string
             enum:
               - Allow
               - Forbid
               - Replace
-            description: >-
-              treatment of concurrent job executions. See
-              https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/#concurrency-policy
+          failedJobsHistoryLimit:
+            description: The number of failed finished jobs to retain. This is a pointer to
+              distinguish between explicit zero and not specified. Defaults to 1.
+            format: int32
+            type: integer
+          schedule:
+            description: The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.
+            type: string
+          startingDeadlineSeconds:
+            description: Optional deadline in seconds for starting the job if it misses scheduled
+              time for any reason.  Missed jobs executions will be counted as failed ones.
+            format: int64
+            type: integer
+          successfulJobsHistoryLimit:
+            description: The number of successful finished jobs to retain. This is a pointer
+              to distinguish between explicit zero and not specified. Defaults to 3.
+            format: int32
+            type: integer
+          suspend:
+            description: This flag tells the controller to suspend subsequent executions,
+              it does not apply to already started executions.  Defaults to false.
+            type: boolean
       policies:
         type: array
         minItems: 1
       labels:
         type: array
         items:
           $ref: '#/definitions/label'
@@ -868,57 +828,18 @@
       livenessProbe:
         description: >-
           Detects whether a pod is healthy by running a command or making a
           network request inside the container. Containers that fail the
           check are restarted.
         $ref: '#/definitions/livenessProbe'
       cmd:
-        type: object
-        additionalProperties: false
-        oneOf:
-          - required:
-              - pr
-              - test
-              - acceptance
-              - production
-          - required:
-              - all
-        properties:
-          pr:
-            type: string
-          test:
-            type: string
-          acceptance:
-            type: string
-          production:
-            type: string
-          all:
-            type: string
+        $ref: '#/definitions/dtapValue'
       args:
         type: object
-        additionalProperties: false
-        oneOf:
-          - required:
-              - pr
-              - test
-              - acceptance
-              - production
-          - required:
-              - all
-        properties:
-          pr:
-            type: string
-          test:
-            type: string
-          acceptance:
-            type: string
-          production:
-            type: string
-          all:
-            type: string
+        $ref: '#/definitions/dtapValue'
       resources:
         type: object
         properties:
           instances:
             description: Sets the number of replicas to be started
             type: object
             additionalProperties: false
@@ -950,57 +871,17 @@
             $ref: '#/definitions/limitResources'
           request:
             $ref: '#/definitions/requestResources'
         additionalProperties: false
       portMappings:
         type: object
       ttlSecondsAfterFinished:
-        type: object
-        additionalProperties: false
-        oneOf:
-          - required:
-              - pr
-              - test
-              - acceptance
-              - production
-          - required:
-              - all
-        properties:
-          pr:
-            type: number
-          test:
-            type: number
-          acceptance:
-            type: number
-          production:
-            type: number
-          all:
-            type: number
+        $ref: '#/definitions/dtapNumberValue'
       activeDeadlineSeconds:
-        type: object
-        additionalProperties: false
-        oneOf:
-          - required:
-              - pr
-              - test
-              - acceptance
-              - production
-          - required:
-              - all
-        properties:
-          pr:
-            type: number
-          test:
-            type: number
-          acceptance:
-            type: number
-          production:
-            type: number
-          all:
-            type: number
+        $ref: '#/definitions/dtapNumberValue'
       role:
         type: object
         additionalProperties: false
         required:
           - resources
           - verbs
         properties:
```

## mpyl/steps/models.py

```diff
@@ -61,14 +61,19 @@
     versioning: VersioningProperties
     config: dict
     """Globally specified configuration, to be used by specific steps. Complies with the schema as
     specified in `mpyl_config.schema.yml`
      """
 
     @staticmethod
+    def for_local_run(config: Dict, revision: str, branch: Optional[str]):
+        return RunProperties(details=RunContext("", "", "", "", "", None), target=Target.PULL_REQUEST,
+                             versioning=VersioningProperties(revision, branch, 123, None), config=config)
+
+    @staticmethod
     def from_configuration(run_properties: Dict, config: Dict):
         build = run_properties['build']
         versioning = build['versioning']
         versioning = VersioningProperties(revision=versioning['revision'], branch=versioning['branch'],
                                           pr_number=int(versioning.get('pr_number')), tag=versioning.get('tag'))
 
         return RunProperties(details=RunContext.from_configuration(build['run']),
```

## mpyl/steps/run.py

```diff
@@ -17,14 +17,31 @@
     _exception: Optional[Exception]
 
     def __init__(self, run_properties: RunProperties, run_plan=None):
         if run_plan is None:
             run_plan = {}
         self._run_properties = run_properties
         self._run_plan = run_plan
+        self._exception = None
+
+    @property
+    def status_line(self) -> str:
+        if self._exception:
+            return '❗Failed with exception'
+        if self._results_success():
+            return '✅Successful'
+        return '❌Failed'
+
+    @property
+    def exception(self) -> Optional[Exception]:
+        return self._exception
+
+    @exception.setter
+    def exception(self, exception: Exception):
+        self._exception = exception
 
     @property
     def run_properties(self) -> RunProperties:
         return self._run_properties
 
     @property
     def run_plan(self) -> dict[Stage, set[Project]]:
@@ -34,14 +51,19 @@
         self._results.append(result)
 
     def extend(self, results: list[StepResult]):
         self._results.extend(results)
 
     @property
     def is_success(self):
+        if self._exception:
+            return False
+        return self._results_success()
+
+    def _results_success(self):
         return all(r.output.success for r in self._results)
 
     @staticmethod
     def sort_chronologically(results: list[StepResult]) -> list[StepResult]:
         return sorted(results, key=operator.attrgetter('timestamp'))
 
     def results_for_stage(self, stage: Stage) -> list[StepResult]:
```

### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

## mpyl/steps/steps.py

```diff
@@ -12,14 +12,15 @@
 
 from . import Step
 from .build.dockerbuild import BuildDocker
 from .build.echo import BuildEcho
 from .build.sbt import BuildSbt
 from .deploy.echo import DeployEcho
 from .deploy.kubernetes import DeployKubernetes
+from .deploy.kubernetes_job import DeployKubernetesJob
 from .models import Output, Input, RunProperties, ArtifactType, Artifact
 from .test.dockertest import TestDocker
 from .test.echo import TestEcho
 from .test.sbt import TestSbt
 from ..project import Project
 from ..project import Stage
 from ..validation import validate
@@ -58,15 +59,16 @@
             Stage.TEST: {
                 TestEcho(logger),
                 TestSbt(logger),
                 TestDocker(logger)
             },
             Stage.DEPLOY: {
                 DeployEcho(logger),
-                DeployKubernetes(logger)
+                DeployKubernetes(logger),
+                DeployKubernetesJob(logger)
             }
         }
 
         self._properties = properties
         for stage, steps in self._step_executors.items():
             self._logger.debug(f"Registered executors for stage {stage.name}: "
                                f"{[step.meta.name for step in steps]}")
```

## mpyl/steps/build/sbt.py

```diff
@@ -50,10 +50,10 @@
             command for command in [
                 f'project {step_input.project.name}',
                 f'set docker / imageNames := Seq(ImageName("{image_name}"))',
                 check_fmt,
                 'docker'
             ] if command is not None
         ]
-        command = SbtConfig.from_config(config=step_input.run_properties.config).to_command()
-        command.append("; ".join(commands))
+        config = SbtConfig.from_config(config=step_input.run_properties.config)
+        command = config.to_command(config.build_with_client, commands)
         return command
```

## mpyl/steps/deploy/kubernetes.py

```diff
@@ -1,15 +1,13 @@
 """ Step that deploys the docker image produced in the build stage to Kubernetes, using HELM. """
 
 from logging import Logger
 
-from kubernetes import config, client
-
-from .k8s import helm
-from .k8s.rancher import rancher_namespace_metadata, cluster_config
+from .k8s import deploy_helm_chart
+from .k8s.chart import ChartBuilder, to_service_chart
 from .. import Step, Meta
 from ..models import Input, Output, ArtifactType
 from ...project import Stage
 
 
 class DeployKubernetes(Step):
 
@@ -18,31 +16,9 @@
             name='Kubernetes Deploy',
             description='Deploy to k8s',
             version='0.0.1',
             stage=Stage.DEPLOY
         ), produced_artifact=ArtifactType.NONE, required_artifact=ArtifactType.DOCKER_IMAGE)
 
     def execute(self, step_input: Input) -> Output:
-        self._logger.info(f"Deploying project {step_input.project.name} with dry run: {step_input.dry_run}")
-        if not step_input.required_artifact:
-            return Output(success=False, message=f"Step requires artifact of type {self.required_artifact}")
-
-        properties = step_input.run_properties
-        context = cluster_config(properties.target).context
-
-        config.load_kube_config(context=context)
-        self._logger.info(f"Deploying target {properties.target} and k8s context {context}")
-        api = client.CoreV1Api()
-
-        namespace = f'pr-{properties.versioning.pr_number}'
-        meta_data = rancher_namespace_metadata(namespace, properties.target)
-
-        namespaces = api.list_namespace(field_selector=f'metadata.name={namespace}')
-        if len(namespaces.items) == 0 and not step_input.dry_run:
-            api.create_namespace(
-                client.V1Namespace(api_version='v1', kind='Namespace', metadata=meta_data))
-        else:
-            self._logger.info(f"Found namespace {namespace}")
-
-        helm_result = helm.install(self._logger, step_input, namespace, context)
-        self._logger.info(helm_result.message)
-        return helm_result
+        builder = ChartBuilder(step_input)
+        return deploy_helm_chart(self._logger, to_service_chart(builder), step_input, builder.release_name)
```

## mpyl/steps/deploy/k8s/__init__.py

```diff
@@ -0,0 +1,94 @@
+00000000: 2222 224b 7562 6572 6e65 7465 7320 6465  """Kubernetes de
+00000010: 706c 6f79 6d65 6e74 2072 656c 6174 6564  ployment related
+00000020: 2068 656c 7065 7220 6d65 7468 6f64 7322   helper methods"
+00000030: 2222 0a66 726f 6d20 6c6f 6767 696e 6720  "".from logging 
+00000040: 696d 706f 7274 204c 6f67 6765 720a 0a66  import Logger..f
+00000050: 726f 6d20 6b75 6265 726e 6574 6573 2069  rom kubernetes i
+00000060: 6d70 6f72 7420 636f 6e66 6967 2c20 636c  mport config, cl
+00000070: 6965 6e74 0a0a 6672 6f6d 202e 2e2e 6465  ient..from ...de
+00000080: 706c 6f79 2e6b 3873 2e72 6573 6f75 7263  ploy.k8s.resourc
+00000090: 6573 2e63 7264 2069 6d70 6f72 7420 4375  es.crd import Cu
+000000a0: 7374 6f6d 5265 736f 7572 6365 4465 6669  stomResourceDefi
+000000b0: 6e69 7469 6f6e 0a66 726f 6d20 2e2e 2e2e  nition.from ....
+000000c0: 7374 6570 7320 696d 706f 7274 2049 6e70  steps import Inp
+000000d0: 7574 2c20 4f75 7470 7574 0a66 726f 6d20  ut, Output.from 
+000000e0: 2e2e 2e2e 7374 6570 732e 6465 706c 6f79  ....steps.deploy
+000000f0: 2e6b 3873 2069 6d70 6f72 7420 6865 6c6d  .k8s import helm
+00000100: 0a66 726f 6d20 2e2e 2e2e 7374 6570 732e  .from ....steps.
+00000110: 6465 706c 6f79 2e6b 3873 2e72 616e 6368  deploy.k8s.ranch
+00000120: 6572 2069 6d70 6f72 7420 636c 7573 7465  er import cluste
+00000130: 725f 636f 6e66 6967 2c20 7261 6e63 6865  r_config, ranche
+00000140: 725f 6e61 6d65 7370 6163 655f 6d65 7461  r_namespace_meta
+00000150: 6461 7461 0a0a 0a64 6566 2075 7073 6572  data...def upser
+00000160: 745f 6e61 6d65 7370 6163 6528 6c6f 6767  t_namespace(logg
+00000170: 6572 3a20 4c6f 6767 6572 2c20 7374 6570  er: Logger, step
+00000180: 5f69 6e70 7574 3a20 496e 7075 742c 2063  _input: Input, c
+00000190: 6f6e 7465 7874 3a20 7374 7229 3a0a 2020  ontext: str):.  
+000001a0: 2020 7072 6f70 6572 7469 6573 203d 2073    properties = s
+000001b0: 7465 705f 696e 7075 742e 7275 6e5f 7072  tep_input.run_pr
+000001c0: 6f70 6572 7469 6573 0a0a 2020 2020 636f  operties..    co
+000001d0: 6e66 6967 2e6c 6f61 645f 6b75 6265 5f63  nfig.load_kube_c
+000001e0: 6f6e 6669 6728 636f 6e74 6578 743d 636f  onfig(context=co
+000001f0: 6e74 6578 7429 0a20 2020 206c 6f67 6765  ntext).    logge
+00000200: 722e 696e 666f 2866 2244 6570 6c6f 7969  r.info(f"Deployi
+00000210: 6e67 2074 6172 6765 7420 7b70 726f 7065  ng target {prope
+00000220: 7274 6965 732e 7461 7267 6574 7d20 616e  rties.target} an
+00000230: 6420 6b38 7320 636f 6e74 6578 7420 7b63  d k8s context {c
+00000240: 6f6e 7465 7874 7d22 290a 2020 2020 6170  ontext}").    ap
+00000250: 6920 3d20 636c 6965 6e74 2e43 6f72 6556  i = client.CoreV
+00000260: 3141 7069 2829 0a0a 2020 2020 6e61 6d65  1Api()..    name
+00000270: 7370 6163 6520 3d20 6627 7072 2d7b 7072  space = f'pr-{pr
+00000280: 6f70 6572 7469 6573 2e76 6572 7369 6f6e  operties.version
+00000290: 696e 672e 7072 5f6e 756d 6265 727d 270a  ing.pr_number}'.
+000002a0: 2020 2020 6d65 7461 5f64 6174 6120 3d20      meta_data = 
+000002b0: 7261 6e63 6865 725f 6e61 6d65 7370 6163  rancher_namespac
+000002c0: 655f 6d65 7461 6461 7461 286e 616d 6573  e_metadata(names
+000002d0: 7061 6365 2c20 7072 6f70 6572 7469 6573  pace, properties
+000002e0: 2e74 6172 6765 7429 0a0a 2020 2020 6e61  .target)..    na
+000002f0: 6d65 7370 6163 6573 203d 2061 7069 2e6c  mespaces = api.l
+00000300: 6973 745f 6e61 6d65 7370 6163 6528 6669  ist_namespace(fi
+00000310: 656c 645f 7365 6c65 6374 6f72 3d66 276d  eld_selector=f'm
+00000320: 6574 6164 6174 612e 6e61 6d65 3d7b 6e61  etadata.name={na
+00000330: 6d65 7370 6163 657d 2729 0a20 2020 2069  mespace}').    i
+00000340: 6620 6c65 6e28 6e61 6d65 7370 6163 6573  f len(namespaces
+00000350: 2e69 7465 6d73 2920 3d3d 2030 2061 6e64  .items) == 0 and
+00000360: 206e 6f74 2073 7465 705f 696e 7075 742e   not step_input.
+00000370: 6472 795f 7275 6e3a 0a20 2020 2020 2020  dry_run:.       
+00000380: 2061 7069 2e63 7265 6174 655f 6e61 6d65   api.create_name
+00000390: 7370 6163 6528 0a20 2020 2020 2020 2020  space(.         
+000003a0: 2020 2063 6c69 656e 742e 5631 4e61 6d65     client.V1Name
+000003b0: 7370 6163 6528 6170 695f 7665 7273 696f  space(api_versio
+000003c0: 6e3d 2776 3127 2c20 6b69 6e64 3d27 4e61  n='v1', kind='Na
+000003d0: 6d65 7370 6163 6527 2c20 6d65 7461 6461  mespace', metada
+000003e0: 7461 3d6d 6574 615f 6461 7461 2929 0a20  ta=meta_data)). 
+000003f0: 2020 2065 6c73 653a 0a20 2020 2020 2020     else:.       
+00000400: 206c 6f67 6765 722e 696e 666f 2866 2246   logger.info(f"F
+00000410: 6f75 6e64 206e 616d 6573 7061 6365 207b  ound namespace {
+00000420: 6e61 6d65 7370 6163 657d 2229 0a20 2020  namespace}").   
+00000430: 2072 6574 7572 6e20 6e61 6d65 7370 6163   return namespac
+00000440: 650a 0a0a 6465 6620 6465 706c 6f79 5f68  e...def deploy_h
+00000450: 656c 6d5f 6368 6172 7428 6c6f 6767 6572  elm_chart(logger
+00000460: 3a20 4c6f 6767 6572 2c20 6368 6172 743a  : Logger, chart:
+00000470: 2064 6963 745b 7374 722c 2043 7573 746f   dict[str, Custo
+00000480: 6d52 6573 6f75 7263 6544 6566 696e 6974  mResourceDefinit
+00000490: 696f 6e5d 2c20 7374 6570 5f69 6e70 7574  ion], step_input
+000004a0: 3a20 496e 7075 742c 0a20 2020 2020 2020  : Input,.       
+000004b0: 2020 2020 2020 2020 2020 2020 2020 2072                 r
+000004c0: 656c 6561 7365 5f6e 616d 653a 2073 7472  elease_name: str
+000004d0: 2920 2d3e 204f 7574 7075 743a 0a20 2020  ) -> Output:.   
+000004e0: 2070 726f 7065 7274 6965 7320 3d20 7374   properties = st
+000004f0: 6570 5f69 6e70 7574 2e72 756e 5f70 726f  ep_input.run_pro
+00000500: 7065 7274 6965 730a 2020 2020 636f 6e74  perties.    cont
+00000510: 6578 7420 3d20 636c 7573 7465 725f 636f  ext = cluster_co
+00000520: 6e66 6967 2870 726f 7065 7274 6965 732e  nfig(properties.
+00000530: 7461 7267 6574 292e 636f 6e74 6578 740a  target).context.
+00000540: 2020 2020 6e61 6d65 7370 6163 6520 3d20      namespace = 
+00000550: 7570 7365 7274 5f6e 616d 6573 7061 6365  upsert_namespace
+00000560: 286c 6f67 6765 722c 2073 7465 705f 696e  (logger, step_in
+00000570: 7075 742c 2063 6f6e 7465 7874 290a 2020  put, context).  
+00000580: 2020 7265 7475 726e 2068 656c 6d2e 696e    return helm.in
+00000590: 7374 616c 6c28 6c6f 6767 6572 2c20 6368  stall(logger, ch
+000005a0: 6172 742c 2073 7465 705f 696e 7075 742c  art, step_input,
+000005b0: 2072 656c 6561 7365 5f6e 616d 652c 206e   release_name, n
+000005c0: 616d 6573 7061 6365 2c20 636f 6e74 6578  amespace, contex
+000005d0: 7429 0a                                  t).
```

## mpyl/steps/deploy/k8s/helm.py

```diff
@@ -2,55 +2,49 @@
 step.
 """
 
 import shutil
 from logging import Logger
 from pathlib import Path
 
-from .service import ServiceChart
-from ...models import RunProperties, Input, Output
+from .resources.crd import to_yaml, CustomResourceDefinition
+from ...models import RunProperties, Output, Input
 from ....utilities.subprocess import custom_check_output
 
 
 def to_chart_metadata(chart_name: str, run_properties: RunProperties):
     return f"""apiVersion: v3
 name: {chart_name}
-description: A helm chart used by the MPL pipeline
+description: A helm chart used by the MPyL pipeline
 type: application
 version: 0.1.0
 appVersion: "{run_properties.versioning.identifier}"
 """
 
 
-def write_chart(step_input: Input, chart_path: Path, chart_metadata: str) -> None:
-    if step_input.required_artifact:
-        image_name = step_input.required_artifact.spec['image']
-    else:
-        raise ValueError('Required artifact must be defined')
-
-    service_chart = ServiceChart(step_input, image_name)
-
+def write_chart(chart: dict[str, CustomResourceDefinition], chart_path: Path, chart_metadata: str) -> None:
     shutil.rmtree(chart_path, ignore_errors=True)
     template_path = chart_path / Path("templates")
     template_path.mkdir(parents=True, exist_ok=True)
 
     with open(chart_path / Path("Chart.yaml"), mode='w+', encoding='utf-8') as file:
         file.write(chart_metadata)
     with open(chart_path / Path("values.yaml"), mode='w+', encoding='utf-8') as file:
         file.write("# This file is intentionally left empty. All values in /templates have been pre-interpolated")
 
-    templates = service_chart.to_chart()
-    for name, template in templates.items():
-        with open(template_path / str(name), mode='w+', encoding='utf-8') as file:
+    my_dictionary: dict[str, str] = dict(map(lambda item: (item[0], to_yaml(item[1])), chart.items()))
+
+    for name, template in my_dictionary.items():
+        with open(template_path / name, mode='w+', encoding='utf-8') as file:
             file.write(template)
 
 
-def install(logger: Logger, step_input: Input, name_space: str, kube_context: str) -> Output:
-    chart_name = step_input.project.name.lower()
+def install(logger: Logger, chart: dict[str, CustomResourceDefinition], step_input: Input, chart_name: str,
+            name_space: str, kube_context: str) -> Output:
     chart_path = Path(step_input.project.target_path) / "chart"
-    write_chart(step_input, chart_path, to_chart_metadata(chart_name, step_input.run_properties))
+    write_chart(chart, chart_path, to_chart_metadata(chart_name, step_input.run_properties))
 
     cmd = f"helm upgrade -i {chart_name} -n {name_space} --kube-context {kube_context} {chart_path}"
     if step_input.dry_run:
         cmd = f"helm upgrade -i {chart_name} -n namespace --kube-context {kube_context} {chart_path} --debug --dry-run"
 
     return custom_check_output(logger, cmd)
```

## mpyl/steps/test/sbt.py

```diff
@@ -88,15 +88,13 @@
 
     @staticmethod
     def _construct_sbt_command_test_without_coverage(step_input: Input):
         return [f'{step_input.project.name}/test']
 
     @staticmethod
     def _construct_sbt_command(step_input: Input, config: SbtConfig, commands_fn: Callable[[Input], list[str]]):
-        command = config.to_command()
-        command.append("; ".join(commands_fn(step_input)))
-        return command
+        return config.to_command(config.test_with_client, commands_fn(step_input))
 
     @staticmethod
     def _extract_test_report(project: Project, step_input: Input) -> Artifact:
         return input_to_artifact(artifact_type=ArtifactType.JUNIT_TESTS, step_input=step_input,
                                  spec={TEST_OUTPUT_PATH_KEY: f'{project.test_report_path}'})
```

## mpyl/utilities/repo/__init__.py

```diff
@@ -44,14 +44,18 @@
         return self
 
     @property
     def get_sha(self):
         return self._repo.head.commit.hexsha
 
     @property
+    def get_short_sha(self):
+        return self._repo.git.rev_parse(self._repo.head, short=True)
+
+    @property
     def get_branch(self):
         return self._repo.active_branch.name
 
     def root_dir(self) -> Path:
         return Path(self._root_dir)
 
     def changes_in_branch(self) -> list[Revision]:
@@ -70,10 +74,11 @@
         main = self._config.main_branch
         return remote.fetch(f"+refs/heads/{main}:refs/heads/{main}")
 
     def changes_in_commit(self) -> set[str]:
         changed: set[str] = set(self._repo.git.diff(None, name_only=True).splitlines())
         return changed.union(self._repo.untracked_files)
 
-    def find_projects(self) -> set[str]:
+    def find_projects(self) -> list[str]:
         """ returns a set of all project.yml files """
-        return set(self._repo.git.ls_files(f'**/{Project.project_yaml_path()}').splitlines())
+        projects = set(self._repo.git.ls_files(f'**/{Project.project_yaml_path()}').splitlines())
+        return sorted(projects)
```

## mpyl/utilities/sbt/__init__.py

```diff
@@ -7,27 +7,37 @@
 @dataclass(frozen=True)
 class SbtConfig:
     java_opts: str
     sbt_opts: str
     sbt_command: str
     test_with_coverage: bool
     verbose: bool
+    build_with_client: bool
+    test_with_client: bool
 
     @staticmethod
     def from_config(config: Dict):
         sbt_config = config.get('sbt', None)
         if not sbt_config:
             raise KeyError(f"'sbt' could not be loaded from {config}")
-        return SbtConfig(sbt_command=sbt_config['command'],
-                         java_opts=sbt_config['javaOpts'],
-                         sbt_opts=sbt_config['sbtOpts'],
-                         test_with_coverage=(str(sbt_config['testWithCoverage']).lower() == 'true'),
-                         verbose=(str(sbt_config['verbose']).lower() == 'true')
-                         )
+        return SbtConfig(
+            sbt_command=sbt_config['command'],
+            java_opts=sbt_config['javaOpts'],
+            sbt_opts=sbt_config['sbtOpts'],
+            test_with_coverage=(str(sbt_config['testWithCoverage']).lower() == 'true'),
+            verbose=(str(sbt_config['verbose']).lower() == 'true'),
+            build_with_client=(str(sbt_config.get('clientMode', {}).get('build')).lower() == 'true'),
+            test_with_client=(str(sbt_config.get('clientMode', {}).get('test')).lower() == 'true')
+        )
 
-    def to_command(self):
+    def to_command(self, client_mode: bool, sbt_commands: list[str]):
         cmd = [self.sbt_command]
         if self.verbose:
             cmd.append('-v')
+        if client_mode:
+            cmd.append('--client')
         cmd.extend([f'-J{opt}' for opt in self.java_opts.split(' ')])
         cmd.extend([f'-D{opt}' for opt in self.sbt_opts.split(' ')])
+
+        joined_commands = "; ".join(sbt_commands)
+        cmd.append(f"'{joined_commands}" if client_mode else joined_commands)
         return cmd
```

## Comparing `mpyl/steps/deploy/k8s/service.py` & `mpyl/steps/deploy/k8s/chart.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,25 +1,25 @@
 """
 Data classes for the composition of Custom Resource Definitions.
 More info: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
 """
 
 from dataclasses import dataclass
-from typing import Dict, Optional
+from typing import Dict
 
 from kubernetes.client import V1Deployment, V1Container, V1DeploymentSpec, V1ObjectMeta, V1PodSpec, \
     V1RollingUpdateDeployment, V1LabelSelector, V1ContainerPort, V1EnvVar, V1Service, \
     V1ServiceSpec, V1ServicePort, V1ServiceAccount, V1LocalObjectReference, \
     V1EnvVarSource, V1SecretKeySelector, V1Probe, ApiClient, V1HTTPGetAction, V1ResourceRequirements, \
-    V1PodTemplateSpec, V1DeploymentStrategy
+    V1PodTemplateSpec, V1DeploymentStrategy, V1Job, V1JobSpec, V1CronJob, V1CronJobSpec, V1JobTemplateSpec
 from ruamel.yaml import YAML
 
-from .resources.crd import to_yaml  # pylint: disable = no-name-in-module
+from .resources.crd import CustomResourceDefinition, to_dict  # pylint: disable = no-name-in-module
 from .resources.customresources import V1AlphaIngressRoute, V1SealedSecret  # pylint: disable = no-name-in-module
-from ...models import Input
+from ...models import Input, ArtifactType
 from ....project import Project, KeyValueProperty, Probe, Deployment, TargetProperty, Resources, Target
 
 yaml = YAML()
 
 # Determined (unscientifically) to be sensible factors.
 # Based on actual CPU usage, pods rarely use more than 10% of the allocated CPU. 60% usage is healthy, so we
 # scale down to 20% in order to keep some slack.
@@ -51,47 +51,45 @@
     @staticmethod
     def from_config(values: dict):
         return KubernetesConfig(resources_defaults=ResourceDefaults.from_config(values['resources']),
                                 liveness_probe_defaults=values['livenessProbe'],
                                 startup_probe_defaults=values['startupProbe'])
 
 
-class ServiceChart:
+class ChartBuilder:
     step_input: Input
     project: Project
     mappings: dict[int, int]
     env: list[KeyValueProperty]
     sealed_secrets: list[KeyValueProperty]
     deployment: Deployment
     target: Target
     release_name: str
-    image_name: str
     kubernetes_config: KubernetesConfig
 
-    def __init__(self, step_input: Input, image_name: str):
+    def __init__(self, step_input: Input):
         self.step_input = step_input
         project = self.step_input.project
         self.project = project
         if project.deployment is None:
             raise AttributeError("deployment field should be set")
         kubernetes_config_dict = step_input.run_properties.config.get('project', {}).get('deployment', {}).get(
             'kubernetes', {})
         if kubernetes_config_dict is None:
             raise KeyError("Configuration should have project.deployment.kubernetes section")
 
         self.kubernetes_config = KubernetesConfig.from_config(kubernetes_config_dict)
 
         self.deployment = project.deployment
         properties = self.deployment.properties
-        self.env = properties.env if properties.env else []
-        self.sealed_secrets = properties.sealed_secret if properties.sealed_secret else []
+        self.env = properties.env if properties and properties.env else []
+        self.sealed_secrets = properties.sealed_secret if properties and properties.sealed_secret else []
         self.mappings = self.project.kubernetes.port_mappings
         self.target = step_input.run_properties.target
         self.release_name = self.project.name.lower()
-        self.image_name = image_name
 
     def _to_labels(self) -> Dict:
         run_properties = self.step_input.run_properties
         app_labels = {'name': self.project.name, 'app.kubernetes.io/version': run_properties.versioning.identifier,
                       'app.kubernetes.io/managed-by': 'Helm', 'app.kubernetes.io/name': self.release_name,
                       'app.kubernetes.io/instance': self.release_name}
 
@@ -120,107 +118,134 @@
     def _to_k8s_model(values: dict, model_type):
         return ApiClient()._ApiClient__deserialize(values, model_type)  # pylint: disable=protected-access
 
     @staticmethod
     def _to_probe(probe: Probe, defaults: dict, target: Target) -> V1Probe:
         values = defaults.copy()
         values.update(probe.values)
-        v1_probe: V1Probe = ServiceChart._to_k8s_model(values, V1Probe)
+        v1_probe: V1Probe = ChartBuilder._to_k8s_model(values, V1Probe)
         path = probe.path.get_value(target)
         v1_probe.http_get = V1HTTPGetAction(path='/health' if path is None else path, port='port-0')
         return v1_probe
 
     def to_service(self) -> V1Service:
         service_ports = list(map(lambda key: V1ServicePort(port=key, target_port=self.mappings[key], protocol="TCP",
                                                            name=f"{key}-webservice-port"), self.mappings.keys()))
 
         return V1Service(api_version='v1', kind='Service', metadata=self._to_object_meta(),
                          spec=V1ServiceSpec(type="ClusterIP", ports=service_ports,
                                             selector=self._to_selector().match_labels))
 
-    def to_ingress_routes(self) -> Optional[V1AlphaIngressRoute]:
-        if not self.deployment.traefik:
-            return None
+    def to_job(self) -> V1Job:
+        job_container = V1Container(
+            name=self.project.name, image=self._get_image(), env=self._get_env_vars(), image_pull_policy="Always",
+            resources=self._get_resources()
+        )
+        pod_template = V1PodTemplateSpec(
+            metadata=self._to_object_meta(),
+            spec=V1PodSpec(containers=[job_container], service_account=self.release_name,
+                           service_account_name=self.release_name),
+        )
+        return V1Job(api_version='batch/v1', kind='Job', metadata=self._to_object_meta(),
+                     spec=V1JobSpec(ttl_seconds_after_finished=3600, template=pod_template))
+
+    def to_cron_job(self) -> V1CronJob:
+        values = self._get_kubernetes().cron
+        job_template = V1JobTemplateSpec(spec=self.to_job().spec)
+        template_dict = to_dict(job_template)
+        values['jobTemplate'] = template_dict
+        v1_cron_job_spec: V1CronJobSpec = ChartBuilder._to_k8s_model(values, V1CronJobSpec)
+        return V1CronJob(api_version='batch/v1', kind='CronJob', metadata=self._to_object_meta(), spec=v1_cron_job_spec)
+
+    def to_ingress_routes(self) -> V1AlphaIngressRoute:
+        if self.deployment.traefik is None:
+            raise AttributeError("deployment.traefik field should be set")
+
         return V1AlphaIngressRoute(metadata=self._to_object_meta(), hosts=self.deployment.traefik.hosts,
                                    service_port=123, name=self.release_name, target=self.target)
 
     def to_service_account(self) -> V1ServiceAccount:
         return V1ServiceAccount(api_version="v1", kind="ServiceAccount", metadata=self._to_object_meta(),
                                 image_pull_secrets=[V1LocalObjectReference("bigdataregistry")])
 
-    def to_chart(self) -> dict[str, str]:
-        chart = {'deployment': to_yaml(self.to_deployment()), 'serviceaccount': to_yaml(self.to_service_account()),
-                 'service': to_yaml(self.to_service())}
-        if self.sealed_secrets:
-            chart['sealedsecrets'] = to_yaml(self.to_sealed_secrets())
-
-        if self.deployment.traefik:
-            chart['ingress-https-route'] = to_yaml(self.to_ingress_routes())
-
-        return chart
-
-    def to_sealed_secrets(self) -> Optional[V1SealedSecret]:
-        if self.sealed_secrets is None:
-            return None
-
+    def to_sealed_secrets(self) -> V1SealedSecret:
         secrets: dict[str, str] = {}
         for secret in self.sealed_secrets:
             secrets[secret.key] = secret.get_value(self.target)
 
         return V1SealedSecret(name=self.release_name, secrets=secrets)
 
     @staticmethod
     def _to_resources(resources: Resources, defaults: ResourceDefaults, target: Target):
-        cpus = resources.cpus if resources.cpus else defaults.cpus
+        cpus = resources.cpus if resources and resources.cpus else defaults.cpus
         cpus_limit = cpus.get_value(target=target) * 1000.0
         cpus_request = cpus_limit * CPU_REQUEST_SCALE_FACTOR
 
-        mem = resources.mem if resources.mem else defaults.mem
+        mem = resources.mem if resources and resources.mem else defaults.mem
         mem_limit = mem.get_value(target=target)
         mem_request = mem_limit * MEM_REQUEST_SCALE_FACTOR
         return V1ResourceRequirements(limits={'cpu': f'{int(cpus_limit)}m', 'memory': f'{int(mem_limit)}Mi'},
                                       requests={'cpu': f'{int(cpus_request)}m', 'memory': f'{int(mem_request)}Mi'})
 
-    def to_deployment(self) -> V1Deployment:
+    def _get_image(self):
+        docker_image = self.step_input.required_artifact
+        if not docker_image or docker_image.artifact_type != ArtifactType.DOCKER_IMAGE:
+            raise ValueError(f'Required artifact of type {ArtifactType.DOCKER_IMAGE.name} must be defined')
+        return docker_image.spec['image']
+
+    def _get_kubernetes(self):
         kubernetes = self.deployment.kubernetes
         if kubernetes is None:
             raise AttributeError("deployment.kubernetes field should be set")
+        return kubernetes
 
-        ports = [
-            V1ContainerPort(container_port=key, host_port=self.mappings[key], protocol="TCP", name=f'port-{idx}')
-            for idx, key in enumerate(self.mappings.keys())
-        ]
+    def _get_resources(self):
+        kubernetes = self._get_kubernetes()
+        resources = kubernetes.resources
+        defaults = self.kubernetes_config.resources_defaults
+        return ChartBuilder._to_resources(resources, defaults, self.target)
+
+    def _get_env_vars(self):
         env_vars = list(
             filter(lambda v: v.value, map(lambda e: V1EnvVar(name=e.key, value=e.get_value(self.target)), self.env)))
-
         sealed_for_target = list(
-            filter(lambda v: v.get_value(self.target) is not None, self.deployment.properties.sealed_secret))
+            filter(lambda v: v.get_value(self.target) is not None, self.sealed_secrets))
         sealed_secrets = list(map(lambda e: V1EnvVar(name=e.key, value_from=V1EnvVarSource(
             secret_key_ref=V1SecretKeySelector(key=e.key, name=self.release_name, optional=False))),
                                   sealed_for_target))
+        return env_vars + sealed_secrets
 
+    def to_deployment(self) -> V1Deployment:
+
+        ports = [
+            V1ContainerPort(container_port=key, host_port=self.mappings[key], protocol="TCP", name=f'port-{idx}')
+            for idx, key in enumerate(self.mappings.keys())
+        ]
+
+        kubernetes = self._get_kubernetes()
         resources = kubernetes.resources
         defaults = self.kubernetes_config.resources_defaults
-        instances = resources.instances if resources.instances else defaults.instances
 
         container = V1Container(
             name=self.project.name,
-            image=self.image_name,
-            env=env_vars + sealed_secrets,
+            image=self._get_image(),
+            env=self._get_env_vars(),
             ports=ports,
             image_pull_policy="Always",
-            resources=ServiceChart._to_resources(resources, defaults, self.target),
-            liveness_probe=ServiceChart._to_probe(kubernetes.liveness_probe,
+            resources=ChartBuilder._to_resources(resources, defaults, self.target),
+            liveness_probe=ChartBuilder._to_probe(kubernetes.liveness_probe,
                                                   self.kubernetes_config.liveness_probe_defaults,
                                                   self.target) if kubernetes.liveness_probe else None,
-            startup_probe=ServiceChart._to_probe(kubernetes.startup_probe,
+            startup_probe=ChartBuilder._to_probe(kubernetes.startup_probe,
                                                  self.kubernetes_config.startup_probe_defaults,
                                                  self.target) if kubernetes.startup_probe else None
         )
 
+        instances = resources.instances if resources.instances else defaults.instances
+
         return V1Deployment(
             api_version="apps/v1",
             kind="Deployment",
             metadata=V1ObjectMeta(annotations=self._to_annotations(), name=self.release_name,
                                   labels=self._to_labels()),
             spec=V1DeploymentSpec(
                 replicas=instances.get_value(target=self.target),
@@ -231,7 +256,37 @@
                 ),
                 strategy=V1DeploymentStrategy(
                     rolling_update=V1RollingUpdateDeployment(max_surge="25%", max_unavailable="25%"),
                     type="RollingUpdate"),
                 selector=self._to_selector(),
             ),
         )
+
+
+def to_service_chart(builder: ChartBuilder) -> dict[str, CustomResourceDefinition]:
+    chart = {'deployment': builder.to_deployment(), 'serviceaccount': builder.to_service_account(),
+             'service': builder.to_service()}
+    if builder.sealed_secrets:
+        chart['sealedsecrets'] = builder.to_sealed_secrets()
+
+    if builder.deployment.traefik:
+        chart['ingress-https-route'] = builder.to_ingress_routes()
+
+    return chart
+
+
+def to_job_chart(builder: ChartBuilder) -> dict[str, CustomResourceDefinition]:
+    chart = {'job': builder.to_job(), 'serviceaccount': builder.to_service_account()}
+
+    if builder.sealed_secrets:
+        chart['sealedsecrets'] = builder.to_sealed_secrets()
+
+    return chart
+
+
+def to_cron_job_chart(builder: ChartBuilder) -> dict[str, CustomResourceDefinition]:
+    chart = {'cronjob': builder.to_cron_job(), 'serviceaccount': builder.to_service_account()}
+
+    if builder.sealed_secrets:
+        chart['sealedsecrets'] = builder.to_sealed_secrets()
+
+    return chart
```

## Comparing `mpyl-0.0.8.dist-info/LICENSE` & `mpyl-0.0.9.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `mpyl-0.0.8.dist-info/METADATA` & `mpyl-0.0.9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mpyl
-Version: 0.0.8
+Version: 0.0.9
 Summary: Modular Pipeline Library
 Home-page: https://vandebron.github.io/mpyl
 Author: Vandebron Energie BV
 Project-URL: Documentation, https://vandebron.github.io/mpyl
 Project-URL: Source, https://github.com/Vandebron/mpyl
 Project-URL: Tracker, https://github.com/Vandebron/mpyl/issues
 Classifier: Topic :: Software Development :: Build Tools
```

## Comparing `mpyl-0.0.8.dist-info/RECORD` & `mpyl-0.0.9.dist-info/RECORD`

 * *Files 8% similar despite different names*

```diff
@@ -1,68 +1,70 @@
-mpyl/__init__.py,sha256=yHcp2JWhf43KQ1wkTXrMxLqVbQsBSoWFj_4w8KeLzCo,1952
+mpyl/__init__.py,sha256=P3C0ql70EyN6Mk3zitknkQd1YLiWrQ7p4kKjr1f2EHE,1927
 mpyl/__main__.py,sha256=S7WS_61OT3kRc5RJq3vz4AI6N4YRU5h2KG1kBeQKK6I,215
-mpyl/project.py,sha256=_5NaYDYh5hA3xSM0KMDKv6TqgXtiECa2_ZQWcegHfN4,11406
+mpyl/project.py,sha256=eOoOq3q0GwAO98d6kKT9rt-3b8BLszmBKyhjrsoyzBA,11538
 mpyl/validation.py,sha256=aSyfAetAlnmFlj5QZittgCdU_P_FVjWnArRQ_Wzk2Xc,1069
-mpyl/cli/__init__.py,sha256=9TBRwB04WDyQfGoF9vc1P9p7sgb79_mfGulRiGnvttQ,38
+mpyl/cli/__init__.py,sha256=ylIL8Wh6ZFB_8ilrV8sh9DLRXngwz9xdyL6ECgIL7Wo,568
 mpyl/cli/build/__init__.py,sha256=HYego6gfL5ffgwUi7XLuUkQZiApwlxMIRns8ABcONdo,51
-mpyl/cli/build/jenkins.py,sha256=uLeSCt9f7PjLSVOR4mW5rqKb4_ySbJ4DmW_Pzu67k7A,2212
-mpyl/cli/build/mpyl.py,sha256=MlLd4xAIfCqj6cQZIW5oUbPptgl0KZ65s5qizxOTiN4,4353
-mpyl/cli/commands/__init__.py,sha256=UH7MdYduBG_YoulgdiWkUCtcgGLzuYRGFzxaqoa0pyg,19
-mpyl/cli/commands/build.py,sha256=rVvPDavHIQvIZtnUY1OHiJ7IplbXeCjyxWmShs1i1IQ,3210
-mpyl/cli/commands/meta_info.py,sha256=L2Mj5CS-KDL2DVoC9zFG2Mf1A1lXYJ0JSYBwfpBHahQ,2178
-mpyl/cli/commands/projects.py,sha256=yt35d0iinH8wOQM3pDA13yHoWKmc9SvOKZif9VyLRCM,1457
+mpyl/cli/build/jenkins.py,sha256=-zYAuGIT_G2bkSKYCXJIpMA0JsVELffwRqKwvhbnRFE,2250
+mpyl/cli/build/mpyl.py,sha256=gnfhZiUYoVNLJmZ5SAQ5V2hcdYQJhIdFidxVFf0UuPM,4542
+mpyl/cli/commands/__init__.py,sha256=WCIqCDghvbs1k1Yi5Z77uWADYr5mMGIULQqbSljrBnw,471
+mpyl/cli/commands/build.py,sha256=C1J9wdhJ7GOer0qfCdgQmjsth66kWuIu5ClMB_S40zk,4539
+mpyl/cli/commands/meta_info.py,sha256=MJhWR8GxSL1Anx7Cs_6c0QU6_tYP_pNxaazGV8JoO60,2170
+mpyl/cli/commands/projects.py,sha256=gzVGCwYq8kuIT1kgXmc23gzAR5ouN9cHbng4Z6_Iq2o,1756
+mpyl/cli/projects/__init__.py,sha256=BNpkKojzNeQBtvivF3nsTV8HBvGMTClFckKtpvIuyaY,39
 mpyl/projects/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 mpyl/projects/find.py,sha256=Rck2cuTXiGNJuEcnHBGDQvAlDlQL-MiK1b8i2WNJ1js,265
 mpyl/reporting/__init__.py,sha256=vRvt_67opWXCfe_zYZChT-YhjoPOahAjLagoaVzOcFM,92
 mpyl/reporting/formatting/__init__.py,sha256=GAvYJpHT2SMQxjiLCSqFy57PNWsGI_Ow2bFnA8cX08k,76
-mpyl/reporting/formatting/markdown.py,sha256=cZb6o1gAiWA1BJvXdRPHDBO-uFNtxe-UDVOnmLE2yCg,2564
+mpyl/reporting/formatting/markdown.py,sha256=RuTFSlK3D6O3ojry_465bf6G9J3fVUxZY5s8hKp3YBc,2622
 mpyl/reporting/formatting/text.py,sha256=YAQGBHfb8XktvGIqeKAyjaJeppEmVrMWQu8Oszm1TN8,1148
 mpyl/reporting/targets/__init__.py,sha256=OEj6eAiU_j6C3fcyMV9MgTTKdEMco2dYUVAf9OzpRYc,488
 mpyl/reporting/targets/github.py,sha256=dARo6Q1zarulI_b6-i02S4R74heVTlNFwZK4rWhKAJU,5538
-mpyl/reporting/targets/jira.py,sha256=xCuZSqELi2id9zK18YwjDrqngHWpWYOSIjZx6Y0UWVw,4264
+mpyl/reporting/targets/jira.py,sha256=KgHJcNy-Xa504lHT8aULNC18HKXn8x0fzTUw9YBmeB8,4656
 mpyl/reporting/targets/slack.py,sha256=T8gbKgJUzSZdl7ZkgXZdc-MGdmsIn3kzzf0QQuGFx88,5755
-mpyl/schema/mpyl_config.schema.yml,sha256=IWLUJpcYJbmE66us9z7bZgxKl0UPGA_Wh3z0QNQnKg8,5688
-mpyl/schema/project.schema.yml,sha256=xY-g-b89bMS985uHTM5F2oZKEVYMWr3JzBgG-Pl97sQ,26691
+mpyl/schema/mpyl_config.schema.yml,sha256=7pek7Qty3gxr6TjVFyb-VxHtrrDSWRePehwsKt2Ttz0,5920
+mpyl/schema/project.schema.yml,sha256=vd-LnJRgG1uCLJ3VhO785gufXuvb1N4toZUy7X1hnwQ,24999
 mpyl/stages/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 mpyl/stages/discovery.py,sha256=iIizkXgT3-F5nAJe1UZFAwyTJN0iLQa-Bh1wPRC1yxE,2408
 mpyl/steps/__init__.py,sha256=jpcKUPNLQm_8LngC7mbwYUzaoiisgyJy4R8u0qOkmAU,6135
-mpyl/steps/models.py,sha256=Q5ZQ5ROUNxdym104cpOpyaLSiVub-U2VjZURTxNUFFM,4536
-mpyl/steps/run.py,sha256=nuE59ax48YR1SGH9NHdFXa1uhNbqWRRQTYfRrJBCayo,1589
-mpyl/steps/steps.py,sha256=soXKwFCHlbNiUVCrmrtDVRqOawIbWH3Map6TRY6pRQk,5715
+mpyl/steps/models.py,sha256=WzLkdCvszRODvgxX1nF0OXUoBxol7hyPX0jn8jQl9Bw,4839
+mpyl/steps/run.py,sha256=h26b4qbL_2CIh4-KU8Tn8DHsGDz2-eFqpsZz4tLGe3M,2166
+mpyl/steps/steps.py,sha256=QC8LvfWyOQ9ceO-g-xqmglTc0r6sAjM07RhcvVQ6L_s,5815
 mpyl/steps/build/__init__.py,sha256=EyPUNNDMQfJK-RVjYM9WvPhEDITbu2n4fx9mxhGLlDs,59
 mpyl/steps/build/docker_after_build.py,sha256=IAs69oDgdaoyjTOY3NGCUUPGP9hK4Wjx-MG2ii_hQ8s,2255
 mpyl/steps/build/dockerbuild.py,sha256=LMayPPf4ckOwwJAvOe6H9eAM7OMMAw67gGMqS0_P5U0,2032
 mpyl/steps/build/echo.py,sha256=on6n-zYs55z6_CouMrSTRIV_JDSTVdQ53raTt3im1qU,765
-mpyl/steps/build/sbt.py,sha256=gxf7M2GOlXO5l_SlorHAyRBHlGeJdTTqO8B-PNEo3hM,2388
+mpyl/steps/build/sbt.py,sha256=rvJzIVgsx6KrX5HW_jqEhu6yV2QAttEXQRJ3A7XJJ-k,2402
 mpyl/steps/deploy/__init__.py,sha256=14PYgOvt7YEO2Zw4kEeZxWUNBR7Lz91nSoJZpvJHqzE,60
 mpyl/steps/deploy/echo.py,sha256=f43TQmiY96Da_OLZcjkQx-RjCvlo09Dclpezv9RoMlo,1001
-mpyl/steps/deploy/kubernetes.py,sha256=px32sHTnYY_pSkcKnAXsLLrl4a9life31cW-f-SdTp8,1960
-mpyl/steps/deploy/k8s/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
-mpyl/steps/deploy/k8s/helm.py,sha256=AWGMnVY47FGq2K0pwHI_BJVw___pd_0XERFjeS5NyS4,2195
+mpyl/steps/deploy/kubernetes.py,sha256=60FnJ0nba3T87Pef_BAoxOcQxsNcr95LiOc_NgX-fM0,876
+mpyl/steps/deploy/kubernetes_job.py,sha256=2365tZnTuoumEFqgNoqUX6ectXrXFc_YVyysbLcip0E,1008
+mpyl/steps/deploy/k8s/__init__.py,sha256=v1Rev8KnpCg3FSx4BrxBLDeeUioDr_UHu9Qu2cFE8sQ,1491
+mpyl/steps/deploy/k8s/chart.py,sha256=fl3u-8ZD4JN51a5VWr8NUquO3EBb3mWJjytumXlxs_0,13565
+mpyl/steps/deploy/k8s/helm.py,sha256=r0OoYfvvzAe2IAJ4qPMG_zIB78w-idkL0_9IV2eKXWs,2097
 mpyl/steps/deploy/k8s/rancher.py,sha256=7P5nc6Jir3O3z2oE2Vd0HBlQxDesMwkQ86Omchh1-Es,1431
-mpyl/steps/deploy/k8s/service.py,sha256=Vj0UVsQICO8MyhLMpQuk3uQFq-q7cu9zRLlEyC8irM4,11097
 mpyl/steps/deploy/k8s/resources/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 mpyl/steps/deploy/k8s/resources/crd.py,sha256=ShjvwOK9648yM0-US4m6OS5824hfgMEnUU8uwIe91fI,4418
 mpyl/steps/deploy/k8s/resources/customresources.py,sha256=qoIy0Xso1B4ftM5i00pcsgSOZkv6frAGsT9k3p9JxoA,1330
 mpyl/steps/deploy/k8s/resources/schema/traeffik.schema.yml,sha256=TJAs7dC-xSajyQfQFFFc9AAa2_VyHDFpRMh7I17W2MY,11697
 mpyl/steps/test/__init__.py,sha256=XL1gSbIMJYSFcy4Vf8YRbZM9yAs3Fzvq2tfX9xTDZX8,58
 mpyl/steps/test/after_test.py,sha256=bKTBVFm88s4Kzr6JypxLAbKTlbRsha7gff3RjSr3ip0,1428
 mpyl/steps/test/before_test.py,sha256=IOUvAa3lKox8IKS28aGmmWJMNWcQWv9yGnTydVBvM14,2453
 mpyl/steps/test/dockertest.py,sha256=2IOKdT2FqcDGtWqOJGmSZWOjktH9d9sZPOqODJH55Qk,2830
 mpyl/steps/test/echo.py,sha256=Ca-kMWw4V9uFl3wSiOoJRbVTdbnI_MHnWx6y5e-LeNk,724
-mpyl/steps/test/sbt.py,sha256=a1_zqi8eK1M9ODE3_IPVZz2Dakue53LyaGnjwCSDC1c,4706
+mpyl/steps/test/sbt.py,sha256=vemH1UWKw4jolwQeeVdhrLpQeDostkLG_WbHce-ewbM,4669
 mpyl/utilities/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 mpyl/utilities/docker/__init__.py,sha256=vOS-pgSfCdYw7fFtIZkPDVCJDYiYSLNh_PHEe15DlY8,3315
 mpyl/utilities/github/__init__.py,sha256=VumtjLWl2QAeQvPWGDGQ51EGmvGA1rm1xOLsivW3s5E,1547
 mpyl/utilities/jenkins/__init__.py,sha256=hUtF0yi5TeiE_wBhT1-mhkkohKSnyZffMkPY1wAC8Uo,1542
 mpyl/utilities/jenkins/runner.py,sha256=pv8N4jZy0r8cVzyrzanA2dVEXW9AeEkhtuxoZNULDWY,5016
 mpyl/utilities/junit/__init__.py,sha256=ZnIs3muoUPTpb9DlcrjWl4G8HC8Xb3PIcL7AHGdzb1Q,1280
 mpyl/utilities/pyaml_env/__init__.py,sha256=mJaO3uKnt5QUBvqKAIer3uvv1aD4qOX4djvNc27P71g,754
-mpyl/utilities/repo/__init__.py,sha256=8xJlCr80SMhgvwjXxAihCpLQIkgCU9j0LvQ0P8gc58k,2558
-mpyl/utilities/sbt/__init__.py,sha256=67sQE8z_v5kvSMoTRu83uGe-2jjdMPQTaOazAsQbNMA,1087
+mpyl/utilities/repo/__init__.py,sha256=qRCDDtXRqSY7rR4I88nsbzyZucRa1wboOMoazmxW7X0,2708
+mpyl/utilities/sbt/__init__.py,sha256=zriEJFx9s-mg2qNrHxZeygEqztGDhP9Kk54pKVwFIS0,1520
 mpyl/utilities/subprocess/__init__.py,sha256=eIE5t57AVwuRUC1QFYzKSviE8tVa4QjF3s9KQWi_eyU,1338
-mpyl-0.0.8.dist-info/LICENSE,sha256=xx0jnfkXJvxRnG63LTGOxlggYnIysveWIZ6H3PNdCrQ,11357
-mpyl-0.0.8.dist-info/METADATA,sha256=hzjTaqveO9Aa9fwNEy9K_e2w-bmG0wvv4Xv8VgBH7Wk,2914
-mpyl-0.0.8.dist-info/WHEEL,sha256=2wepM1nk4DS4eFpYrW1TTqPcoGNfHhhO_i5m4cOimbo,92
-mpyl-0.0.8.dist-info/entry_points.txt,sha256=Jf4zjGLsiokFbaQ2dfX9AC5Bu3kp7zxrBOAzErmAYs8,35
-mpyl-0.0.8.dist-info/top_level.txt,sha256=xVSrrk0ECDxKYaW8mAyGy02yY8KhKlUSyzHaq9UDVNs,5
-mpyl-0.0.8.dist-info/RECORD,,
+mpyl-0.0.9.dist-info/LICENSE,sha256=xx0jnfkXJvxRnG63LTGOxlggYnIysveWIZ6H3PNdCrQ,11357
+mpyl-0.0.9.dist-info/METADATA,sha256=EQ7arkX8CO7VvsIhiQo-kqy6RThIxo71z4H24ZjvU-c,2914
+mpyl-0.0.9.dist-info/WHEEL,sha256=2wepM1nk4DS4eFpYrW1TTqPcoGNfHhhO_i5m4cOimbo,92
+mpyl-0.0.9.dist-info/entry_points.txt,sha256=Jf4zjGLsiokFbaQ2dfX9AC5Bu3kp7zxrBOAzErmAYs8,35
+mpyl-0.0.9.dist-info/top_level.txt,sha256=xVSrrk0ECDxKYaW8mAyGy02yY8KhKlUSyzHaq9UDVNs,5
+mpyl-0.0.9.dist-info/RECORD,,
```

