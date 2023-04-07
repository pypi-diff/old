# Comparing `tmp/QDetective-0.0.1.tar.gz` & `tmp/QDetective-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\QDetective-0.0.1.tar", last modified: Thu Mar 30 14:20:33 2023, max compression
+gzip compressed data, was "dist\QDetective-0.0.2.tar", last modified: Fri Apr  7 06:34:48 2023, max compression
```

## Comparing `QDetective-0.0.1.tar` & `QDetective-0.0.2.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxrwx   0        0        0        0 2023-03-30 14:20:33.360982 QDetective-0.0.1/
--rw-rw-rw-   0        0        0      649 2023-03-30 14:20:33.344351 QDetective-0.0.1/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-03-30 14:20:33.080536 QDetective-0.0.1/QDetective/
--rw-rw-rw-   0        0        0     4576 2023-03-30 14:10:12.000000 QDetective-0.0.1/QDetective/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-30 14:20:33.277433 QDetective-0.0.1/QDetective.egg-info/
--rw-rw-rw-   0        0        0      649 2023-03-30 14:20:32.000000 QDetective-0.0.1/QDetective.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      178 2023-03-30 14:20:32.000000 QDetective-0.0.1/QDetective.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-30 14:20:32.000000 QDetective-0.0.1/QDetective.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       11 2023-03-30 14:20:32.000000 QDetective-0.0.1/QDetective.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      133 2023-03-30 13:52:44.000000 QDetective-0.0.1/README.rst
--rw-rw-rw-   0        0        0       42 2023-03-30 14:20:33.361980 QDetective-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0      957 2023-03-30 14:20:08.000000 QDetective-0.0.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 06:34:48.517797 QDetective-0.0.2/
+-rw-rw-rw-   0        0        0      649 2023-04-07 06:34:48.500811 QDetective-0.0.2/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-07 06:34:48.302784 QDetective-0.0.2/QDetective/
+-rw-rw-rw-   0        0        0     4720 2023-04-07 03:44:53.000000 QDetective-0.0.2/QDetective/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 06:34:48.445994 QDetective-0.0.2/QDetective.egg-info/
+-rw-rw-rw-   0        0        0      649 2023-04-07 06:34:48.000000 QDetective-0.0.2/QDetective.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      178 2023-04-07 06:34:48.000000 QDetective-0.0.2/QDetective.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 06:34:48.000000 QDetective-0.0.2/QDetective.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       11 2023-04-07 06:34:48.000000 QDetective-0.0.2/QDetective.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      133 2023-03-30 13:52:44.000000 QDetective-0.0.2/README.rst
+-rw-rw-rw-   0        0        0       42 2023-04-07 06:34:48.518794 QDetective-0.0.2/setup.cfg
+-rw-rw-rw-   0        0        0      957 2023-04-07 03:50:24.000000 QDetective-0.0.2/setup.py
```

### Comparing `QDetective-0.0.1/PKG-INFO` & `QDetective-0.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: QDetective
-Version: 0.0.1
+Version: 0.0.2
 Summary: 量化大侦探-数据通道
 Home-page: UNKNOWN
 Author: suliang
 Author-email: suliang_321@sina.ccom
 License: BSD License
 Description: # QDetective DataChannel
         This is a simple package used for factor sharing.
```

### Comparing `QDetective-0.0.1/QDetective/__init__.py` & `QDetective-0.0.2/QDetective/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -25,27 +25,26 @@
     def __init__(self, username, password, host='124.223.105.49'):
         """
         host: FTP服务器地址
         username: 账号
         password: 密码
         """
         
-        self.ftp = FTP()
+        self.ftp = FTP(timeout=100)
         self.ftp.encoding = 'gbk'
         
         self.ftp.connect(host)
         try:
             self.ftp.login(username, password)
         except:
             print('【{}】用户信息有误，请检查输入是否正确。'.format(username))
         self.ftp.set_pasv(True)
         print("【{}】已成功链接服务器...有问题请联系suliang".format(username))
         self.factor_info = self.get_factor_info()
         
-    
     def connect(self, username, password, host='124.223.105.49'):
         self.ftp = FTP()
         self.ftp.encoding = 'gbk'
         self.ftp.connect(host)
         self.ftp.login(username, password)
         self.ftp.set_pasv(True)
         print("【{}】已成功链接服务器...有问题请联系suliang".format(username))
@@ -67,15 +66,15 @@
     def get_factor(self, factor_name, end_date=None, start_date='20180101', is_stated=True):
         # 下载因子数据
         def read_file(ftp, remotepath):
             file = io.BytesIO()
             ftp.retrbinary('RETR ' + remotepath, file.write)
             file.seek(0)
             if remotepath.split('.')[-1] == 'csv':
-                result = pd.read_csv(file, engine='python')
+                result = pd.read_csv(file, engine='python', encoding='utf_8_sig')
             elif remotepath.split('.')[-1] == 'txt':
                 result = pd.read_table(file, encoding='gbk', header=None)
             return result
         
         # 输出因子说明
         factor_statement = read_file(self.ftp, r'\因子库\{}\0.因子计算说明.txt'.format(factor_name))
         [print(x[0]) for x in list(factor_statement.values)]
@@ -117,8 +116,12 @@
         localpath: 本地路径
         """
         fp = open(localpath, 'rb')
         self.ftp.storbinary('STOR ' + remotepath, fp)
         self.ftp.set_debuglevel(0)
         fp.close()
         return None
-    
+
+if __name__  == '__main__':
+    dc = DataChannel('suliang', '863228920')
+    time.sleep(10)
+    dc.get_factor_info()
```

### Comparing `QDetective-0.0.1/QDetective.egg-info/PKG-INFO` & `QDetective-0.0.2/QDetective.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: QDetective
-Version: 0.0.1
+Version: 0.0.2
 Summary: 量化大侦探-数据通道
 Home-page: UNKNOWN
 Author: suliang
 Author-email: suliang_321@sina.ccom
 License: BSD License
 Description: # QDetective DataChannel
         This is a simple package used for factor sharing.
```

### Comparing `QDetective-0.0.1/setup.py` & `QDetective-0.0.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 from distutils.core import setup
 from setuptools import find_packages
 
 with open("README.rst", "r") as f:
   long_description = f.read()
 
 setup(name='QDetective',  # 包名
-      version='0.0.1',  # 版本号
+      version='0.0.2',  # 版本号
       description='量化大侦探-数据通道',
       long_description=long_description,
       author='suliang',
       author_email='suliang_321@sina.ccom',
       url='',
       install_requires=[],
       license='BSD License',
```

