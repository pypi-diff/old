# Comparing `tmp/libsw3-0.1.8.tar.gz` & `tmp/libsw3-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "libsw3-0.1.8.tar", last modified: Tue Feb 14 10:30:43 2023, max compression
+gzip compressed data, was "libsw3-0.1.9.tar", last modified: Tue Feb 21 05:44:11 2023, max compression
```

## Comparing `libsw3-0.1.8.tar` & `libsw3-0.1.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-14 10:30:43.000000 libsw3-0.1.8/
--rwxrwxrwx   0 root         (0) root         (0)     1074 2021-03-05 06:18:10.000000 libsw3-0.1.8/LICENSE
--rw-r--r--   0 root         (0) root         (0)      421 2023-02-14 10:30:43.000000 libsw3-0.1.8/PKG-INFO
--rwxrwxrwx   0 root         (0) root         (0)       29 2022-08-30 07:25:21.000000 libsw3-0.1.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-14 10:30:43.000000 libsw3-0.1.8/libsw3/
--rwxr-xr-x   0 root         (0) root         (0)    17695 2023-02-14 05:30:40.000000 libsw3-0.1.8/libsw3/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     9961 2023-01-27 12:12:12.000000 libsw3-0.1.8/libsw3/database.py
--rwxr-xr-x   0 root         (0) root         (0)     2816 2022-10-27 09:06:13.000000 libsw3-0.1.8/libsw3/libswn.py
--rw-rw-rw-   0 root         (0) root         (0)     4558 2023-01-03 03:20:40.000000 libsw3-0.1.8/libsw3/msgc.py
--rwxrwxrwx   0 root         (0) root         (0)     3468 2023-02-14 10:29:59.000000 libsw3-0.1.8/libsw3/sendemail.py
--rwxrwxrwx   0 root         (0) root         (0)     4482 2023-01-17 08:57:33.000000 libsw3-0.1.8/libsw3/sw.py
--rwxrwxrwx   0 root         (0) root         (0)     1232 2023-01-19 01:44:45.000000 libsw3-0.1.8/libsw3/utils.py
--rwxrwxrwx   0 root         (0) root         (0)     2718 2023-01-13 08:44:34.000000 libsw3-0.1.8/libsw3/workday.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-14 10:30:43.000000 libsw3-0.1.8/libsw3.egg-info/
--rw-r--r--   0 root         (0) root         (0)      421 2023-02-14 10:30:43.000000 libsw3-0.1.8/libsw3.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      316 2023-02-14 10:30:43.000000 libsw3-0.1.8/libsw3.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-02-14 10:30:43.000000 libsw3-0.1.8/libsw3.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-02-14 10:30:43.000000 libsw3-0.1.8/libsw3.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        7 2023-02-14 10:30:43.000000 libsw3-0.1.8/libsw3.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-02-14 10:30:43.000000 libsw3-0.1.8/setup.cfg
--rwxrwxrwx   0 root         (0) root         (0)      773 2023-02-14 10:30:41.000000 libsw3-0.1.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 05:44:11.000000 libsw3-0.1.9/
+-rwxrwxrwx   0 root         (0) root         (0)     1074 2021-03-05 06:18:10.000000 libsw3-0.1.9/LICENSE
+-rw-r--r--   0 root         (0) root         (0)      421 2023-02-21 05:44:11.000000 libsw3-0.1.9/PKG-INFO
+-rwxrwxrwx   0 root         (0) root         (0)       29 2022-08-30 07:25:21.000000 libsw3-0.1.9/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 05:44:11.000000 libsw3-0.1.9/libsw3/
+-rwxr-xr-x   0 root         (0) root         (0)    17704 2023-02-21 05:39:17.000000 libsw3-0.1.9/libsw3/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     9961 2023-01-27 12:12:12.000000 libsw3-0.1.9/libsw3/database.py
+-rwxr-xr-x   0 root         (0) root         (0)     2816 2022-10-27 09:06:13.000000 libsw3-0.1.9/libsw3/libswn.py
+-rw-rw-rw-   0 root         (0) root         (0)     4558 2023-01-03 03:20:40.000000 libsw3-0.1.9/libsw3/msgc.py
+-rwxrwxrwx   0 root         (0) root         (0)     3514 2023-02-20 10:54:53.000000 libsw3-0.1.9/libsw3/sendemail.py
+-rwxrwxrwx   0 root         (0) root         (0)     4482 2023-01-17 08:57:33.000000 libsw3-0.1.9/libsw3/sw.py
+-rwxrwxrwx   0 root         (0) root         (0)     1232 2023-01-19 01:44:45.000000 libsw3-0.1.9/libsw3/utils.py
+-rwxrwxrwx   0 root         (0) root         (0)     2718 2023-01-13 08:44:34.000000 libsw3-0.1.9/libsw3/workday.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 05:44:11.000000 libsw3-0.1.9/libsw3.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      421 2023-02-21 05:44:10.000000 libsw3-0.1.9/libsw3.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      316 2023-02-21 05:44:10.000000 libsw3-0.1.9/libsw3.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-02-21 05:44:10.000000 libsw3-0.1.9/libsw3.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-02-21 05:44:10.000000 libsw3-0.1.9/libsw3.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        7 2023-02-21 05:44:10.000000 libsw3-0.1.9/libsw3.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-02-21 05:44:11.000000 libsw3-0.1.9/setup.cfg
+-rwxrwxrwx   0 root         (0) root         (0)      773 2023-02-21 05:36:58.000000 libsw3-0.1.9/setup.py
```

### Comparing `libsw3-0.1.8/LICENSE` & `libsw3-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `libsw3-0.1.8/libsw3/__init__.py` & `libsw3-0.1.9/libsw3/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -354,15 +354,15 @@
             print(sinfo)
         else:
             sys.stderr.write(sinfo+"\n")
         if not swdb.connected:return    #事务数据库没联上，不输出数据库日志
         if swid==0 or logid==0:return   #事务id或者调用id为0则返回
         insertSql = "insert into sw_detaillog (dispathno,swid,no,log_time,log_msg,log_level) values (:dispathno,:swid,:no,sysdate,:log_msg,:log_level)"
         cur = swdb.conn.cursor()
-        cur.setinputsizes(log_msg=swdb.BLOB)
+        cur.setinputsizes(log_msg=swdb.dbdriver.BLOB)
         cur.execute(insertSql, {'dispathno':logid,'swid':swid,'no':logno,'log_msg':sinfo.encode("gbk"),'log_level':level})
         logno = logno + 1
         swdb.conn.commit()
     except:
         print("日志打印异常")
 
 def sjbj(sjhm,nr,td="AB"):  #手机报警
```

### Comparing `libsw3-0.1.8/libsw3/database.py` & `libsw3-0.1.9/libsw3/database.py`

 * *Files identical despite different names*

### Comparing `libsw3-0.1.8/libsw3/libswn.py` & `libsw3-0.1.9/libsw3/libswn.py`

 * *Files identical despite different names*

### Comparing `libsw3-0.1.8/libsw3/msgc.py` & `libsw3-0.1.9/libsw3/msgc.py`

 * *Files identical despite different names*

### Comparing `libsw3-0.1.8/libsw3/sendemail.py` & `libsw3-0.1.9/libsw3/sendemail.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,25 +1,25 @@
 #!/usr/bin/python3
 # -*- coding: utf8 -*-
 
-__all__=["可靠邮件","普通邮件"]
+__all__=["可靠邮件","普通邮件","create_html_table"]
 
 from email import encoders
 import smtplib,configparser,os
 from email.mime.text import MIMEText
 from email.mime.base import MIMEBase
 from email.mime.multipart import MIMEMultipart
 import libsw3 as sw3
 sw3.__all__=sw3.__all__ + __all__
 
 class 普通邮件(object):   #直接发送，如果发送失败，可能导致程序崩溃或者邮件发送失败
-    def __init__(self,发送者,标题,正文,接收,抄送=[],暗送=[]):
+    def __init__(self,发送者,标题,正文,接收,抄送=[],暗送=[],邮件类型="plain"):
         self.参数=[发送者,标题,正文,接收,抄送,暗送]
         self.msg=MIMEMultipart()
-        self.msg.attach(MIMEText(正文, 'plain', 'gbk'))
+        self.msg.attach(MIMEText(正文, 邮件类型, 'gbk'))
         self.msg['Subject'] = 标题
         self.msg['From'] = "%s@mail.rtfund.com" %(发送者)
         self.dz=[]
         self.msg['To'] = ','.join(self.解析地址(接收))
         self.msg['Cc'] = ','.join(self.解析地址(抄送))
         self.msg['Bcc'] = ','.join(self.解析地址(暗送))
     def 解析地址(self,地址):
```

### Comparing `libsw3-0.1.8/libsw3/sw.py` & `libsw3-0.1.9/libsw3/sw.py`

 * *Files identical despite different names*

### Comparing `libsw3-0.1.8/libsw3/utils.py` & `libsw3-0.1.9/libsw3/utils.py`

 * *Files identical despite different names*

### Comparing `libsw3-0.1.8/libsw3/workday.py` & `libsw3-0.1.9/libsw3/workday.py`

 * *Files identical despite different names*

### Comparing `libsw3-0.1.8/setup.py` & `libsw3-0.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import setuptools
 
 with open("README.md", "r",encoding='utf-8') as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="libsw3",
-    version="0.1.8",
+    version="0.1.9",
     author="Chen chuan",
     author_email="kcchen@139.com",
     description="libsw3",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     url="https://svn2.rtfund.com/svn/libsw3",
```

