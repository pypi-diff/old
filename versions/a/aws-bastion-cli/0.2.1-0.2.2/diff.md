# Comparing `tmp/aws-bastion-cli-0.2.1.tar.gz` & `tmp/aws-bastion-cli-0.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aws-bastion-cli-0.2.1.tar", last modified: Sat Apr  1 00:42:41 2023, max compression
+gzip compressed data, was "aws-bastion-cli-0.2.2.tar", last modified: Fri Apr  7 11:30:22 2023, max compression
```

## Comparing `aws-bastion-cli-0.2.1.tar` & `aws-bastion-cli-0.2.2.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:42:41.864966 aws-bastion-cli-0.2.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-01 00:42:41.864966 aws-bastion-cli-0.2.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      606 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:42:41.864966 aws-bastion-cli-0.2.1/aws_bastion_cli.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-01 00:42:41.000000 aws-bastion-cli-0.2.1/aws_bastion_cli.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      439 2023-04-01 00:42:41.000000 aws-bastion-cli-0.2.1/aws_bastion_cli.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-01 00:42:41.000000 aws-bastion-cli-0.2.1/aws_bastion_cli.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-01 00:42:41.000000 aws-bastion-cli-0.2.1/aws_bastion_cli.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      323 2023-04-01 00:42:41.000000 aws-bastion-cli-0.2.1/aws_bastion_cli.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-01 00:42:41.000000 aws-bastion-cli-0.2.1/aws_bastion_cli.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:42:41.864966 aws-bastion-cli-0.2.1/bastion_cli/
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/bastion_cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13918 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/bastion_cli/command.py
--rw-r--r--   0 runner    (1001) docker     (123)    10565 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/bastion_cli/create_yaml.py
--rw-r--r--   0 runner    (1001) docker     (123)     5160 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/bastion_cli/deploy_cfn.py
--rw-r--r--   0 runner    (1001) docker     (123)      843 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/bastion_cli/main.py
--rw-r--r--   0 runner    (1001) docker     (123)     1003 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/bastion_cli/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      988 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/bastion_cli/validators.py
--rw-r--r--   0 runner    (1001) docker     (123)      203 2023-04-01 00:42:41.864966 aws-bastion-cli-0.2.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-04-01 00:42:23.000000 aws-bastion-cli-0.2.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:30:22.022451 aws-bastion-cli-0.2.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-07 11:30:22.022451 aws-bastion-cli-0.2.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      606 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:30:22.022451 aws-bastion-cli-0.2.2/aws_bastion_cli.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-07 11:30:22.000000 aws-bastion-cli-0.2.2/aws_bastion_cli.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      439 2023-04-07 11:30:22.000000 aws-bastion-cli-0.2.2/aws_bastion_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:30:22.000000 aws-bastion-cli-0.2.2/aws_bastion_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-07 11:30:22.000000 aws-bastion-cli-0.2.2/aws_bastion_cli.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      323 2023-04-07 11:30:22.000000 aws-bastion-cli-0.2.2/aws_bastion_cli.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-07 11:30:22.000000 aws-bastion-cli-0.2.2/aws_bastion_cli.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:30:22.022451 aws-bastion-cli-0.2.2/bastion_cli/
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/bastion_cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13931 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/bastion_cli/command.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10565 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/bastion_cli/create_yaml.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5160 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/bastion_cli/deploy_cfn.py
+-rw-r--r--   0 runner    (1001) docker     (123)      843 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/bastion_cli/main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1003 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/bastion_cli/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      988 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/bastion_cli/validators.py
+-rw-r--r--   0 runner    (1001) docker     (123)      203 2023-04-07 11:30:22.026451 aws-bastion-cli-0.2.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-04-07 11:30:07.000000 aws-bastion-cli-0.2.2/setup.py
```

### Comparing `aws-bastion-cli-0.2.1/LICENSE` & `aws-bastion-cli-0.2.2/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-bastion-cli-0.2.1/README.md` & `aws-bastion-cli-0.2.2/README.md`

 * *Files identical despite different names*

### Comparing `aws-bastion-cli-0.2.1/bastion_cli/command.py` & `aws-bastion-cli-0.2.2/bastion_cli/command.py`

 * *Files 0% similar despite different names*

```diff
@@ -246,15 +246,15 @@
             subnet_list = sorted(subnet_list,
                                  key=lambda x: (list(ipaddress.IPv4Network(x[2]).hosts())[0]._ip, x[1], x[3], x[0]),
                                  reverse=False)
 
             # for subnet in sorted(subnet_list, key=lambda x: (x[0])):
             for subnet in subnet_list:
                 subnet_show_data = f'''{subnet[0]} ({subnet[2]}, {subnet[1]}{f", {subnet[3]}" if subnet[3] else ""})'''
-                subnet_show_list.append((subnet_show_data, subnet[0]))
+                subnet_show_list.append((subnet_show_data, (subnet[0], subnet[1])))
 
             questions = [
                 List(
                     name='subnet',
                     message='Choose subnet',
                     choices=subnet_show_list
                 )
```

### Comparing `aws-bastion-cli-0.2.1/bastion_cli/create_yaml.py` & `aws-bastion-cli-0.2.2/bastion_cli/create_yaml.py`

 * *Files identical despite different names*

### Comparing `aws-bastion-cli-0.2.1/bastion_cli/deploy_cfn.py` & `aws-bastion-cli-0.2.2/bastion_cli/deploy_cfn.py`

 * *Files identical despite different names*

### Comparing `aws-bastion-cli-0.2.1/bastion_cli/main.py` & `aws-bastion-cli-0.2.2/bastion_cli/main.py`

 * *Files identical despite different names*

### Comparing `aws-bastion-cli-0.2.1/bastion_cli/utils.py` & `aws-bastion-cli-0.2.2/bastion_cli/utils.py`

 * *Files identical despite different names*

### Comparing `aws-bastion-cli-0.2.1/bastion_cli/validators.py` & `aws-bastion-cli-0.2.2/bastion_cli/validators.py`

 * *Files identical despite different names*

### Comparing `aws-bastion-cli-0.2.1/setup.py` & `aws-bastion-cli-0.2.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,15 +19,15 @@
     'six==1.16.0',
     'urllib3==1.26.14',
     'wcwidth==0.2.6',
 ]
 
 setup(
     name='aws-bastion-cli',
-    version='0.2.1',
+    version='0.2.2',
     author='marcus16-kang',
     description='AWS Bastion EC2 Server Stack Generator',
     author_email='marcus16-kang@outlook.com',
     license='MIT',
     entry_points={
         'console_scripts': [
             'bastion-cli=bastion_cli.main:main'
```

