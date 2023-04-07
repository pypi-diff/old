# Comparing `tmp/tipset-0.2.2.tar.gz` & `tmp/tipset-0.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tipset-0.2.2.tar", last modified: Wed Jan  4 07:09:32 2023, max compression
+gzip compressed data, was "dist/tipset-0.2.3.tar", last modified: Fri Apr  7 06:35:31 2023, max compression
```

## Comparing `tipset-0.2.2.tar` & `tipset-0.2.3.tar`

### file list

```diff
@@ -1,32 +1,34 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:32.000000 tipset-0.2.2/
--rw-r--r--   0 runner    (1001) docker     (123)     3472 2023-01-04 07:09:32.000000 tipset-0.2.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2992 2023-01-04 07:09:28.000000 tipset-0.2.2/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-04 07:09:32.000000 tipset-0.2.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1476 2023-01-04 07:09:28.000000 tipset-0.2.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14260 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/aws_amis_search.py
--rw-r--r--   0 runner    (1001) docker     (123)     3259 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/aws_ebs_search.py
--rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/aws_instance_search.py
--rw-r--r--   0 runner    (1001) docker     (123)     4003 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/aws_reportportal_sum.py
--rw-r--r--   0 runner    (1001) docker     (123)     7714 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/aws_snapshot_search.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset/cfg/
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/cfg/aws_reportportal_sum.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset/data/
--rw-r--r--   0 runner    (1001) docker     (123)    84820 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/data/tips_data.json
--rw-r--r--   0 runner    (1001) docker     (123)     7447 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/html_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     6167 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/json_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset/libs/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/libs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9206 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/libs/aws_libs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/libs/minilog.py
--rw-r--r--   0 runner    (1001) docker     (123)    19962 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/libs/polarion_adm.py
--rw-r--r--   0 runner    (1001) docker     (123)    10306 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/libs/rmt_ssh.py
--rw-r--r--   0 runner    (1001) docker     (123)     3868 2023-01-04 07:09:28.000000 tipset-0.2.2/tipset/tipsearch.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3472 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      611 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-01-04 07:09:32.000000 tipset-0.2.2/tipset.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:31.000000 tipset-0.2.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     3472 2023-04-07 06:35:31.000000 tipset-0.2.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2992 2023-04-07 06:35:27.000000 tipset-0.2.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 06:35:31.000000 tipset-0.2.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1498 2023-04-07 06:35:27.000000 tipset-0.2.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14260 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/aws_amis_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3259 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/aws_ebs_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/aws_instance_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10339 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/aws_reportportal_sum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7714 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/aws_snapshot_search.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset/cfg/
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/cfg/aws_reportportal_sum.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset/data/
+-rw-r--r--   0 runner    (1001) docker     (123)    86720 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/data/tips_data.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)     4041 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/docs/awscli_quick_start_with_examples.md
+-rw-r--r--   0 runner    (1001) docker     (123)     8104 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/html_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6167 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/json_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset/libs/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/libs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9206 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/libs/aws_libs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/libs/minilog.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20675 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/libs/polarion_adm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12788 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/libs/rmt_ssh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3868 2023-04-07 06:35:27.000000 tipset-0.2.3/tipset/tipsearch.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3472 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      659 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 06:35:31.000000 tipset-0.2.3/tipset.egg-info/top_level.txt
```

### Comparing `tipset-0.2.2/PKG-INFO` & `tipset-0.2.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tipset
-Version: 0.2.2
+Version: 0.2.3
 Summary: tipset is a colletion of mini tools about various tips under linux.
 Home-page: https://github.com/liangxiao1/tipset
 Author: Xiao Liang
 Author-email: xiliang@redhat.com
 License: GPLv3+
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Programming Language :: Python :: 3
```

### Comparing `tipset-0.2.2/README.md` & `tipset-0.2.3/README.md`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/setup.py` & `tipset-0.2.3/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,24 +1,25 @@
 import setuptools
 import os
 
 setuptools.setup(
     name="tipset",
-    version="0.2.2",
+    version="0.2.3",
     author="Xiao Liang",
     author_email="xiliang@redhat.com",
     description="tipset is a colletion of mini tools about various tips under linux.",
     long_description=open('README.md').read(),
     long_description_content_type="text/markdown",
     url="https://github.com/liangxiao1/tipset",
     #packages=setuptools.find_packages(),
     packages=[ 'tipset','tipset.libs'],
     package_data={
         'tipset': [
             'data/*',
+            'docs/*',
             'cfg/*'
         ]
     },
     include_package_data=True,
     install_requires=['argparse'],
     license="GPLv3+",
     classifiers=[
```

### Comparing `tipset-0.2.2/tipset/aws_amis_search.py` & `tipset-0.2.3/tipset/aws_amis_search.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset/aws_ebs_search.py` & `tipset-0.2.3/tipset/aws_ebs_search.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset/aws_instance_search.py` & `tipset-0.2.3/tipset/aws_instance_search.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset/aws_snapshot_search.py` & `tipset-0.2.3/tipset/aws_snapshot_search.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset/data/tips_data.json` & `tipset-0.2.3/tipset/data/tips_data.json`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9551868239921336%*

 * *Differences: {"'tip_109'": "OrderedDict([('subject', 'find local subnet ips'), ('demo_steps', "*

 * *              "[OrderedDict([('step', '# arp-scan --interface=eth0 --localnet'), ('out', '')])]), "*

 * *              "('tags', 'arp, network'), ('comments', ''), ('link', '')])",*

 * * "'tip_110'": "OrderedDict([('subject', 'add user to sudoers'), ('demo_steps', "*

 * *              "[OrderedDict([('step', '# usermod -aG wheel $user'), ('out', '')])]), ('tags', "*

 * *              "'sudo, sudoers'), ('comments', ''), ('link', "*

 * *               […]*

```diff
@@ -327,14 +327,26 @@
                 "step": "<graphics type='vnc' port='5950' autoport='no' listen='0.0.0.0' passwd='password'>"
             }
         ],
         "link": "",
         "subject": "virsh enable guest vnc",
         "tags": "virsh, vnc"
     },
+    "tip_109": {
+        "comments": "",
+        "demo_steps": [
+            {
+                "out": "",
+                "step": "# arp-scan --interface=eth0 --localnet"
+            }
+        ],
+        "link": "",
+        "subject": "find local subnet ips",
+        "tags": "arp, network"
+    },
     "tip_11": {
         "comments": "",
         "demo_steps": [
             {
                 "out": "",
                 "step": "Ctrl+L: Clear the screen. This is similar to running the \u201cclear\u201d command."
             },
@@ -399,14 +411,74 @@
                 "step": "Ctrl+G: Leave history searching mode without running a command."
             }
         ],
         "link": "",
         "subject": "OS shortcuts",
         "tags": "cli, shortcut, terminal"
     },
+    "tip_110": {
+        "comments": "",
+        "demo_steps": [
+            {
+                "out": "",
+                "step": "# usermod -aG wheel $user"
+            }
+        ],
+        "link": "https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/",
+        "subject": "add user to sudoers",
+        "tags": "sudo, sudoers"
+    },
+    "tip_111": {
+        "comments": "",
+        "demo_steps": [
+            {
+                "out": "",
+                "step": "# git pull origin main --rebase"
+            },
+            {
+                "out": "",
+                "step": "# git push origin main"
+            }
+        ],
+        "link": "https://articles.assembla.com/en/articles/748133-failed-to-push-some-refs-git-error",
+        "subject": "git push error: failed to push some refs to",
+        "tags": "git, github"
+    },
+    "tip_112": {
+        "comments": "Be caution, it is not recommended way without history left",
+        "demo_steps": [
+            {
+                "out": "",
+                "step": "# git reset --hard commitid"
+            },
+            {
+                "out": "",
+                "step": "# git push --force"
+            }
+        ],
+        "link": "",
+        "subject": "totally abandon a commit instead of revert",
+        "tags": "git, github"
+    },
+    "tip_113": {
+        "comments": "",
+        "demo_steps": [
+            {
+                "out": "",
+                "step": "# ps -eo pid,ppid,%mem,%cpu,cmd --sort=-%cpu | head"
+            },
+            {
+                "out": "",
+                "step": "# top -b | head -10"
+            }
+        ],
+        "link": "",
+        "subject": "find out high cpu usage process",
+        "tags": "linux, ps"
+    },
     "tip_12": {
         "comments": "",
         "demo_steps": [
             {
                 "out": "",
                 "step": "yum install -y virt-install libvirt-daemon-config-network libvirt libguestfs-tools"
             },
@@ -2431,14 +2503,18 @@
                 "step": "systemctl disable --now firewalld"
             },
             {
                 "out": "",
                 "step": "systemctl enable --now cockpit"
             },
             {
+                "out": "no need if no such file found",
+                "step": "sed  's/^root/#root/g' /etc/cockpit/disallowed-users"
+            },
+            {
                 "out": "",
                 "step": "vist https://hostname:9090/"
             }
         ],
         "link": "",
         "subject": "Linux cockpit web console",
         "tags": "cockpit, management"
@@ -3480,14 +3556,18 @@
         "demo_steps": [
             {
                 "out": "",
                 "step": "yum install -y gdb"
             },
             {
                 "out": "",
+                "step": "sudo yum debuginfo-install python311"
+            },
+            {
+                "out": "",
                 "step": "gdb -p 9593"
             },
             {
                 "out": "",
                 "step": "(gdb) py-bt (if not found, try to install required pks when start gdb)"
             },
             {
@@ -3507,15 +3587,15 @@
                 "step": "(gdb) call pthread_exit(0) (exit current thread, but will not work if it is waiting for a lock)"
             },
             {
                 "out": "",
                 "step": "# ldd /usr/bin/gdb | grep python"
             }
         ],
-        "link": "",
+        "link": "https://devguide.python.org/advanced-tools/gdb/",
         "subject": "gdb to debug a running python process",
         "tags": "debug, grep"
     },
     "tip_98": {
         "comments": "you may kill start adb and enable/disable usb debug on you phone more times",
         "demo_steps": [
             {
```

### Comparing `tipset-0.2.2/tipset/html_parser.py` & `tipset-0.2.3/tipset/html_parser.py`

 * *Files 7% similar despite different names*

```diff
@@ -34,14 +34,17 @@
 except ImportError:
     from urllib.request import urlopen
 import logging
 import argparse
 import string
 import re
 
+log = logging.getLogger(__name__)
+logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(message)s")
+
 def walk_child(elements, key, is_found=False, results=[]):
     if hasattr(elements, 'children'):
         for child in elements.children:
             if not hasattr(child, 'children'):
                 if len(child)>1 and is_found and key not in child:
                     results.append(child)
             if key in child:
@@ -59,85 +62,63 @@
         elif re.match('.*'+keyword+'.*', src_content.get_text()):
             ret = True
         else:
             if match_any and ret:
                 break
     return ret
 
-def main():
-    parser = argparse.ArgumentParser('Script for get info from html')
-    parser.add_argument('--url',dest='url',action='store',help='specify url',default=None,required=True)
-    parser.add_argument('--keyword',dest='keyword',action='store',help='specify keyword you are looking for, regex accepted',default=None,required=True)
-    parser.add_argument('--andkeys',dest='andkeys',action='store',help='must have keys in and',default=None,required=False)
-    parser.add_argument('--orkeys',dest='orkeys',action='store',help='must have keys in or',default=None,required=False)
-    parser.add_argument('--excludekeys',dest='excludekeys',action='store',help='specify keyword you are not looking for',default=None,required=False)
-    parser.add_argument('--tag',dest='tag',action='store',help='optional specify prefix tag, default is JOB_',default='JOB_',required=False)
-    parser.add_argument('--name',dest='name',action='store',help='optional specify suffix name, default is PKGURL',default='PKGURL',required=False)
-    parser.add_argument('--field',dest='check_field',action='store',help='href|text, default is href',default='href',required=False)
-    parser.add_argument('--outputfield',dest='output_field',action='store',help='href|text, default is href',default='href',required=False)
-    parser.add_argument('--element',dest='check_element',action='store',help='default is "a", you can specify others like "br","tr","div"',default='a',required=False)
-    parser.add_argument('-r', dest='is_walk',action='store_true',help='walk the child to find match items, only support when filed is text', required=False,default=False)
-    parser.add_argument('--dir', dest='file_dir', action='store', default='/tmp',
-                                help='optional, output location, default is /tmp', required=False)
-    args=parser.parse_args()
-    
-    log = logging.getLogger(__name__)
-    logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(message)s")
-    url = args.url
-    keywords = args.keyword
-    andkeys = args.andkeys
-    orkeys = args.orkeys
-    excludekeys = args.excludekeys
-    tag = args.tag
-    name = args.name
+def paser_html_data(url=None,keywords=None, andkeys=None, orkeys=None, excludekeys=None, tag=None,name=None, check_field='href', output_field=None, element='a', is_walk=True, allow_empty=False, file_dir='/tmp'):
     url_fh = urlopen(url)
     html_src = url_fh.read()
     with open('arch_taskinfo.txt','w') as fh:
         fh.writelines(str(html_src))
     soup = BeautifulSoup(html_src,'lxml')
     log.info("loading data done")
-    JOB_DIR = args.file_dir
+    JOB_DIR = file_dir
     JOB_ENV_YAML = JOB_DIR+"/job_env.yaml"
     JOB_ENV_TXT = JOB_DIR+"/job_env.txt"
     results=[]
     
-    s=soup.findAll(args.check_element)
+    s=soup.findAll(element)
     
     for i in s:
         #log.info("name: %s, url: %s",i.get_text(),  i['href'])
-        is_exclude = filter_key(i, excludekeys, args.check_field)
-        is_and_key = filter_key(i,andkeys, args.check_field, match_any=False)
-        is_or_key = filter_key(i,orkeys, args.check_field)
+        is_exclude = filter_key(i, excludekeys, check_field)
+        is_and_key = filter_key(i,andkeys, check_field, match_any=False)
+        is_or_key = filter_key(i,orkeys, check_field)
         if not keywords:
             break
         for keyword in keywords.split(','):
             if is_exclude and excludekeys:
                 break
             if not is_and_key and andkeys:
                 break
             if not is_or_key and orkeys:
                 break
             #breakpoint()
-            if args.check_field == 'href' and i.get('href') and re.match('.*'+keyword+'.*', i.get('href')):
-                log.info("found href %s for target %s", i.get('href'), i.get_text())
-                if args.output_field == 'href':
+            if check_field == 'href' and i.get('href') and re.match('.*'+keyword+'.*', i.get('href')):
+                if not allow_empty:
+                    if not i.get_text() or i.get_text().startswith((' ','\n','  ')):
+                        continue
+                log.info("found href %s for target '%s'", i.get('href'), i.get_text())
+                if output_field == 'href':
                     results.append(i.get('href'))
                 else:
                     results.append(i.get_text())
             elif re.match('.*'+keyword+'.*', i.get_text()):
                 log.info("found %s", i.get_text())
-                if args.output_field == 'href':
+                if output_field == 'href':
                     try:
                         results.append(i.get('href'))
                     except:
                         log.info("no href for %s", i.get_text())
                         results.append(i.get_text())
                 else:
                     results.append(i.get_text())
-        if len(results) == 0 and args.is_walk:
+        if len(results) == 0 and is_walk:
             for keyword in keywords.split(','):
                 x, y = walk_child(i, keyword)
                 if x:
                     results.extend(y)
             if len(results) > 0:
                 log.info("Not found in self content, try to look for child......")
                 log.info("Got {}".format(results))
@@ -149,9 +130,32 @@
             log.info("Write to %s", JOB_ENV_YAML)
         with open(JOB_ENV_TXT, 'a') as fh:
             fh.write("%s%s='%s'\n"% (tag, name,','.join(results)))
             log.info("Write to %s", JOB_ENV_TXT)
     else:
         log.info("Not found any match content!")
 
+def main():
+    parser = argparse.ArgumentParser('Script for get info from html')
+    parser.add_argument('--url',dest='url',action='store',help='specify url',default=None,required=True)
+    parser.add_argument('--keyword',dest='keyword',action='store',help='specify keyword you are looking for, regex accepted',default=None,required=True)
+    parser.add_argument('--andkeys',dest='andkeys',action='store',help='must have keys in and',default=None,required=False)
+    parser.add_argument('--orkeys',dest='orkeys',action='store',help='must have keys in or',default=None,required=False)
+    parser.add_argument('--excludekeys',dest='excludekeys',action='store',help='specify keyword you are not looking for',default=None,required=False)
+    parser.add_argument('--tag',dest='tag',action='store',help='optional specify prefix tag, default is JOB_',default='JOB_',required=False)
+    parser.add_argument('--name',dest='name',action='store',help='optional specify suffix name, default is PKGURL',default='PKGURL',required=False)
+    parser.add_argument('--field',dest='check_field',action='store',help='href|text, default is href',default='href',required=False)
+    parser.add_argument('--outputfield',dest='output_field',action='store',help='href|text, default is href',default='href',required=False)
+    parser.add_argument('--element',dest='check_element',action='store',help='default is "a", you can specify others like "br","tr","div"',default='a',required=False)
+    parser.add_argument('-r', dest='is_walk',action='store_true',help='walk the child to find match items, only support when filed is text', required=False,default=False)
+    parser.add_argument('--allow_empty', dest='allow_empty',action='store_true',help='allow text is empty or starts with space, tab or newline', required=False,default=False)
+    parser.add_argument('--dir', dest='file_dir', action='store', default='/tmp',
+                                help='optional, output location, default is /tmp', required=False)
+    args=parser.parse_args()
+    paser_html_data(url=args.url,keywords=args.keyword, andkeys=args.andkeys, orkeys=args.orkeys,
+        excludekeys=args.excludekeys, tag=args.tag,name=args.name, check_field=args.check_field, output_field=args.output_field, 
+        element=args.check_element, is_walk=args.is_walk, allow_empty=args.allow_empty, file_dir=args.file_dir)
+    
+    
+
 if __name__ == "__main__":
     main()
```

### Comparing `tipset-0.2.2/tipset/json_parser.py` & `tipset-0.2.3/tipset/json_parser.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset/libs/aws_libs.py` & `tipset-0.2.3/tipset/libs/aws_libs.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset/libs/minilog.py` & `tipset-0.2.3/tipset/libs/minilog.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset/libs/polarion_adm.py` & `tipset-0.2.3/tipset/libs/polarion_adm.py`

 * *Files 2% similar despite different names*

```diff
@@ -168,30 +168,44 @@
         tc.caseposneg="positive"
         tc.subsystemteam = _update_item(tc.subsystemteam, "subsystem_team", "sst_virtualization_cloud")
         tc.testtype = _update_item( tc.testtype, "test_type", "functional")
         #tc.hyperlinks= _update_item( tc.hyperlinks, "automation_field", "")
     
         if tc.test_steps.steps:
             if tc.test_steps.steps[0].values[0].content != self.casedoc.get("key_steps") or \
-               tc.test_steps.steps[0].values[1].content != self.casedoc.get("Expected Result"):
+               tc.test_steps.steps[0].values[1].content != self.casedoc.get("expected_result"):
                 step1 = TestStep()
-                step1.values = [self.casedoc.get("key_steps") or '', self.casedoc.get("Expected Result") or '']
+                step1.values = [self.casedoc.get("key_steps") or '', self.casedoc.get("expected_result") or '']
                 tc.set_test_steps([step1])
                 msg += "{}: Test step is changed.\n".format(tc.work_item_id)
         # TCMS Bugs can only append, and need de-duplication
         if self.casedoc.get('bug_id'):
             tcmsbug_list = tc.tcmsbug.split(',') if tc.tcmsbug else []
             tcmsbug_list_new = list(set([x.strip(' ') for x in tcmsbug_list]))
             for bug_id in str(self.casedoc.get('bug_id', '')).split(','):
                 bug_id = bug_id.strip(' ')
                 if bug_id not in tcmsbug_list_new:
                     tcmsbug_list_new.append(bug_id)
                     changed = True
                     msg += "{}: {} is added to tcmsbugs.\n".format(tc.work_item_id, bug_id)
             tc.tcmsbug = ','.join(tcmsbug_list_new)
+        update_case_hyperlinks = True
+        if len(tc.hyperlinks) > 0:
+            # Check if the hyperlink exists
+            for i in range(len(tc.hyperlinks)):
+                if tc.hyperlinks[i].role == "testscript" and \
+                   tc.hyperlinks[i].uri == self.casedoc.get("automation_field"):
+                   update_case_hyperlinks = False
+                   break
+        if update_case_hyperlinks:
+            #_update_item( tc.hyperlinks, "automation_field")
+            add_hyperlink = tc.add_hyperlink(self.casedoc.get("automation_field"),"testscript")
+            if add_hyperlink:
+                changed = True
+                print("Add hyperlink for case {}".format(tc.work_item_id))
         if changed:
             try:
                 tc.update()
                 log.info('Updated successfully!')
             except Exception as e:
                 log.error('Failed to update {}: {}. Exception: {}'.format(tc.work_item_id, tc.title, str(e)))
         if msg:
```

### Comparing `tipset-0.2.2/tipset/libs/rmt_ssh.py` & `tipset-0.2.3/tipset/libs/rmt_ssh.py`

 * *Files 11% similar despite different names*

```diff
@@ -10,15 +10,75 @@
     print("Please install paramiko if do remote access")
 
 import logging
 import time
 import sys
 import os
 from . import minilog
+import threading
+import select
+import argparse
+import socket
+
+def sig_handler(signum, frame):
+    print("sig_handlerXXXXXXXXXX")
+    logging.info('Got signal %s, exit!', signum)
+    sys.exit(0)
+
+
+def handler(chan, host, port):
+    sock = socket.socket()
+    try:
+        sock.connect((host, port))
+    except Exception as e:
+        logging.info("Forwarding request to %s:%d failed: %r" % 
+                  (host, port, e))
+        return
+
+    logging.info(
+        "Connected!  Tunnel open %r -> %r -> %r"
+        % (chan.origin_addr, chan.getpeername(), (host, port))
+    )
+    retry_count = 0
+    while True:
+        r, w, x = select.select([sock, chan], [], [])
+        if sock in r:
+            data = sock.recv(1024)
+            if len(data) == 0:
+                retry_count+=1
+                if retry_count>100:
+                    logging.info("No data received from sock")
+                    break
+            else:
+                chan.send(data)
+        if chan in r:
+            data = chan.recv(1024)
+            if len(data) == 0:
+                if retry_count>100:
+                    logging.info("No data received from chan")
+                    break
+            else:
+                sock.send(data)
+    chan.close()
+    sock.close()
+    logging.info("Tunnel closed from %r" % (chan.origin_addr,))
+ 
+ 
+def reverse_forward_tunnel(server_port, remote_host, remote_port, transport):
+    transport.request_port_forward("", server_port)
 
+    while True:
+        chan = transport.accept(1000)
+        if chan is None:
+            continue
+        thr = threading.Thread(
+            target=handler, args=(chan, remote_host, remote_port)
+        )
+        thr.setDaemon(True)
+        thr.start()
 
 class RemoteSSH():
     """
     quick example:
     from tipset.libs import rmt_ssh
     X = rmt_ssh.RemoteSSH()
     X.rmt_node = 'xxxxxx'
@@ -33,21 +93,22 @@
     def __init__(self):
         self.ssh_client = None
         self.rmt_node = None
         self.port = 22
         self.rmt_user = None
         self.rmt_password = None
         self.rmt_keyfile = None
+        self.rmt_proxy = None 
         self.timeout = 180
         self.interval = 10
         self.log = None
 
     def create_connection(self):
         self.ssh_client = build_connection(rmt_node=self.rmt_node, port=self.port, rmt_user=self.rmt_user,
-                rmt_password=self.rmt_password, rmt_keyfile=self.rmt_keyfile, timeout=self.timeout, interval=self.interval, log=self.log)
+                rmt_password=self.rmt_password, rmt_keyfile=self.rmt_keyfile, rmt_proxy=self.rmt_proxy, timeout=self.timeout, interval=self.interval, log=self.log)
 
     def cli_run(self, cmd=None, timeout=180, rmt_get_pty=False):
         return cli_run(self.ssh_client, cmd, timeout, rmt_get_pty=rmt_get_pty, log=self.log)
 
     def remote_excute(self, cmd, timeout=180, redirect_stdout=False, redirect_stderr=False, rmt_get_pty=False):
         return remote_excute(self.ssh_client, cmd, timeout, redirect_stdout=redirect_stdout, redirect_stderr=redirect_stderr, rmt_get_pty=rmt_get_pty, log=self.log)
 
@@ -112,15 +173,15 @@
         ret, _, _ = self.cli_run(cmd='uname -r')
         if ret != 0:
             self.log.info("connection is not active via sending cmd")
             return False
         self.log.info("connection is active")
         return True
 
-def build_connection(rmt_node=None, port=22, rmt_user='ec2-user', rmt_password=None, rmt_keyfile=None, timeout=180, interval=10, log=None):
+def build_connection(rmt_node=None, port=22, rmt_user='ec2-user', rmt_password=None, rmt_keyfile=None, rmt_proxy=None, timeout=180, interval=10, log=None):
     if log is None:
         log = minilog.minilog()
     if isinstance(log, logging.Logger):
         logging.getLogger("paramiko").setLevel(logging.INFO)
     log.info("Try to make connection {}@{}:{}".format(rmt_user, rmt_node, port))
     ssh_client = paramiko.SSHClient()
     ssh_client.load_system_host_keys()
@@ -162,14 +223,26 @@
                         port=port,
                         username=rmt_user,
                         #key_filename=rmt_keyfile,
                         pkey=pkey_RSAKey,
                         look_for_keys=False,
                         timeout=60
                     )
+                    if rmt_proxy is not None:
+                        log.info(
+                            "Now forwarding remote port 8080 to %s ..."
+                            % (rmt_proxy))
+                        try:
+                            th_reverse = threading.Thread(target=reverse_forward_tunnel, args=(
+                                8080, rmt_proxy.split(':')[0], int(rmt_proxy.split(':')[
+                                    1]),ssh_client.get_transport()))
+                            th_reverse.setDaemon(True)
+                            th_reverse.start()
+                        except KeyboardInterrupt:
+                            print("C-c: Port forwarding stopped.")
                     return ssh_client
                 except BadHostKeyException as e:
                     badhostkey = True
                     exception_list.append(e)
                 except Exception as e:
                     exception_list.append(e)         
                 raise Exception(exception_list)
```

### Comparing `tipset-0.2.2/tipset/tipsearch.py` & `tipset-0.2.3/tipset/tipsearch.py`

 * *Files identical despite different names*

### Comparing `tipset-0.2.2/tipset.egg-info/PKG-INFO` & `tipset-0.2.3/tipset.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tipset
-Version: 0.2.2
+Version: 0.2.3
 Summary: tipset is a colletion of mini tools about various tips under linux.
 Home-page: https://github.com/liangxiao1/tipset
 Author: Xiao Liang
 Author-email: xiliang@redhat.com
 License: GPLv3+
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Programming Language :: Python :: 3
```

### Comparing `tipset-0.2.2/tipset.egg-info/SOURCES.txt` & `tipset-0.2.3/tipset.egg-info/SOURCES.txt`

 * *Files 18% similar despite different names*

```diff
@@ -13,12 +13,13 @@
 tipset.egg-info/SOURCES.txt
 tipset.egg-info/dependency_links.txt
 tipset.egg-info/entry_points.txt
 tipset.egg-info/requires.txt
 tipset.egg-info/top_level.txt
 tipset/cfg/aws_reportportal_sum.yaml
 tipset/data/tips_data.json
+tipset/docs/awscli_quick_start_with_examples.md
 tipset/libs/__init__.py
 tipset/libs/aws_libs.py
 tipset/libs/minilog.py
 tipset/libs/polarion_adm.py
 tipset/libs/rmt_ssh.py
```

