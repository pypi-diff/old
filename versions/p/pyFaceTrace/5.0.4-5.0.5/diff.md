# Comparing `tmp/pyFaceTrace-5.0.4.tar.gz` & `tmp/pyFaceTrace-5.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\pyFaceTrace-5.0.4.tar", last modified: Thu Apr  6 01:40:09 2023, max compression
+gzip compressed data, was "dist\pyFaceTrace-5.0.5.tar", last modified: Thu Apr  6 09:54:02 2023, max compression
```

## Comparing `pyFaceTrace-5.0.4.tar` & `pyFaceTrace-5.0.5.tar`

### file list

```diff
@@ -1,21 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 01:40:09.000000 pyFaceTrace-5.0.4/
--rw-rw-rw-   0        0        0     1078 2020-03-22 02:51:13.000000 pyFaceTrace-5.0.4/LICENSE.txt
--rw-rw-rw-   0        0        0       19 2020-03-22 16:38:07.000000 pyFaceTrace-5.0.4/MANIFEST.in
--rw-rw-rw-   0        0        0     4322 2023-04-06 01:40:09.000000 pyFaceTrace-5.0.4/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-06 01:40:09.000000 pyFaceTrace-5.0.4/pyFaceTrace/
--rw-rw-rw-   0        0        0      655 2023-04-04 22:22:06.000000 pyFaceTrace-5.0.4/pyFaceTrace/demo.py
--rw-rw-rw-   0        0        0     1936 2020-03-22 16:35:09.000000 pyFaceTrace-5.0.4/pyFaceTrace/dowloadTest.py
--rw-rw-rw-   0        0        0      506 2023-04-06 01:23:56.000000 pyFaceTrace-5.0.4/pyFaceTrace/extractZipFile.py
--rw-rw-rw-   0        0        0    13431 2023-04-06 01:37:05.000000 pyFaceTrace-5.0.4/pyFaceTrace/pyFaceTrace.py
--rw-rw-rw-   0        0        0      505 2023-04-06 01:23:00.000000 pyFaceTrace-5.0.4/pyFaceTrace/testzip.py
--rw-rw-rw-   0        0        0      837 2023-04-06 01:34:12.000000 pyFaceTrace-5.0.4/pyFaceTrace/zipFolder.py
--rw-rw-rw-   0        0        0    13432 2023-04-06 01:39:26.000000 pyFaceTrace-5.0.4/pyFaceTrace/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 01:40:09.000000 pyFaceTrace-5.0.4/pyFaceTrace.egg-info/
--rw-rw-rw-   0        0        0        1 2023-04-06 01:40:08.000000 pyFaceTrace-5.0.4/pyFaceTrace.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0     4322 2023-04-06 01:40:08.000000 pyFaceTrace-5.0.4/pyFaceTrace.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0       46 2023-04-06 01:40:08.000000 pyFaceTrace-5.0.4/pyFaceTrace.egg-info/requires.txt
--rw-rw-rw-   0        0        0      392 2023-04-06 01:40:09.000000 pyFaceTrace-5.0.4/pyFaceTrace.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0       12 2023-04-06 01:40:08.000000 pyFaceTrace-5.0.4/pyFaceTrace.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     3108 2023-04-02 15:05:25.000000 pyFaceTrace-5.0.4/README.md
--rw-rw-rw-   0        0        0       42 2023-04-06 01:40:09.000000 pyFaceTrace-5.0.4/setup.cfg
--rw-rw-rw-   0        0        0     1113 2023-04-06 01:39:55.000000 pyFaceTrace-5.0.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/
+-rw-rw-rw-   0        0        0     1078 2020-03-22 02:51:13.000000 pyFaceTrace-5.0.5/LICENSE.txt
+-rw-rw-rw-   0        0        0       19 2020-03-22 16:38:07.000000 pyFaceTrace-5.0.5/MANIFEST.in
+-rw-rw-rw-   0        0        0     4902 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/pyFaceTrace/
+-rw-rw-rw-   0        0        0     1120 2023-04-06 09:52:22.000000 pyFaceTrace-5.0.5/pyFaceTrace/demo.py
+-rw-rw-rw-   0        0        0     1936 2020-03-22 16:35:09.000000 pyFaceTrace-5.0.5/pyFaceTrace/dowloadTest.py
+-rw-rw-rw-   0        0        0      506 2023-04-06 01:23:56.000000 pyFaceTrace-5.0.5/pyFaceTrace/extractZipFile.py
+-rw-rw-rw-   0        0        0    13431 2023-04-06 01:37:05.000000 pyFaceTrace-5.0.5/pyFaceTrace/pyFaceTrace.py
+-rw-rw-rw-   0        0        0      837 2023-04-06 01:34:12.000000 pyFaceTrace-5.0.5/pyFaceTrace/zipFolder.py
+-rw-rw-rw-   0        0        0    13432 2023-04-06 01:39:26.000000 pyFaceTrace-5.0.5/pyFaceTrace/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/pyFaceTrace.egg-info/
+-rw-rw-rw-   0        0        0        1 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/pyFaceTrace.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0     4902 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/pyFaceTrace.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0       46 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/pyFaceTrace.egg-info/requires.txt
+-rw-rw-rw-   0        0        0      369 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/pyFaceTrace.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0       12 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/pyFaceTrace.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     3608 2023-04-06 09:53:02.000000 pyFaceTrace-5.0.5/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 09:54:02.000000 pyFaceTrace-5.0.5/setup.cfg
+-rw-rw-rw-   0        0        0     1113 2023-04-06 09:53:53.000000 pyFaceTrace-5.0.5/setup.py
```

### Comparing `pyFaceTrace-5.0.4/LICENSE.txt` & `pyFaceTrace-5.0.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pyFaceTrace-5.0.4/PKG-INFO` & `pyFaceTrace-5.0.5/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyFaceTrace
-Version: 5.0.4
+Version: 5.0.5
 Summary: easy Face Recognition for python
 Home-page: https://pypi.org/project/pyFaceTrace
 Author: KuoYuan Li
 Author-email: funny4875@gmail.com
 License: UNKNOWN
 Description: # Author:KuoYuan Li
         [![N|Solid](https://images2.imgbox.com/8f/03/gv0QnOdH_o.png)](https://sites.google.com/ms2.ccsh.tn.edu.tw/pclearn0915)  
@@ -36,25 +36,35 @@
         ft.downloadImageSamples()  
         ```
         ##### work with opencv webcam process (detail)  
         ```
         import pyFaceTrace as ft
         import cv2
         from PIL import ImageFont
+        #至train資料夾載入樣本,欲辨識之目標圖片可放入 train資料夾
         ft.loadDB()
+        #設定文字物件
+        FONT = ImageFont.truetype("kaiu.ttf",50,index=0)
+        #webcamd 影像處理迴圈
         cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
         while True:
             ret, img = cap.read()
-            FONT = ImageFont.truetype("kaiu.ttf",50,index=0)
-            rect=ft.detector(img,1)[0]
-            fv=ft.getFeatureVector(img,rect)
-            tag,dist = ft.predictFromDB(fv)
-            cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,0,255),3)
-            img=ft.addText2Img_cv2(img,tag,FONT,position=(rect.left(),rect.top()-FONT.size-1))
+            if not ret : continue
+            #取得 img 中所有人臉之矩型區域，放入rects
+            rects=ft.detector(img,1)
+            for rect in rects:
+                #取得webcam img 中人臉之特徵向量
+                fv=ft.getFeatureVector(img,rect)
+                #將特徵向量和 ft.DB 中之人特徵向量做比對，找到距離最短的(dist)當作辨識結果(tag)
+                tag,dist = ft.predictFromDB(fv)
+                #將辨識結果顯示在 img 上
+                cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,0,255),3)
+                img=ft.addText2Img_cv2(img,tag,FONT,position=(rect.left(),rect.top()-FONT.size-1))
             if cv2.waitKey(10) == 27: break
+            # 將 img show在視窗中
             cv2.imshow('press esc to exit...', img)
         cap.release()
         cv2.destroyAllWindows()
         ```
         ##### work with opencv webcam process (esay)
         ```
         import pyFaceTrace as ft
```

### Comparing `pyFaceTrace-5.0.4/pyFaceTrace/dowloadTest.py` & `pyFaceTrace-5.0.5/pyFaceTrace/dowloadTest.py`

 * *Files identical despite different names*

### Comparing `pyFaceTrace-5.0.4/pyFaceTrace/pyFaceTrace.py` & `pyFaceTrace-5.0.5/pyFaceTrace/pyFaceTrace.py`

 * *Files identical despite different names*

### Comparing `pyFaceTrace-5.0.4/pyFaceTrace/zipFolder.py` & `pyFaceTrace-5.0.5/pyFaceTrace/zipFolder.py`

 * *Files identical despite different names*

### Comparing `pyFaceTrace-5.0.4/pyFaceTrace/__init__.py` & `pyFaceTrace-5.0.5/pyFaceTrace/__init__.py`

 * *Files identical despite different names*

### Comparing `pyFaceTrace-5.0.4/pyFaceTrace.egg-info/PKG-INFO` & `pyFaceTrace-5.0.5/pyFaceTrace.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyFaceTrace
-Version: 5.0.4
+Version: 5.0.5
 Summary: easy Face Recognition for python
 Home-page: https://pypi.org/project/pyFaceTrace
 Author: KuoYuan Li
 Author-email: funny4875@gmail.com
 License: UNKNOWN
 Description: # Author:KuoYuan Li
         [![N|Solid](https://images2.imgbox.com/8f/03/gv0QnOdH_o.png)](https://sites.google.com/ms2.ccsh.tn.edu.tw/pclearn0915)  
@@ -36,25 +36,35 @@
         ft.downloadImageSamples()  
         ```
         ##### work with opencv webcam process (detail)  
         ```
         import pyFaceTrace as ft
         import cv2
         from PIL import ImageFont
+        #至train資料夾載入樣本,欲辨識之目標圖片可放入 train資料夾
         ft.loadDB()
+        #設定文字物件
+        FONT = ImageFont.truetype("kaiu.ttf",50,index=0)
+        #webcamd 影像處理迴圈
         cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
         while True:
             ret, img = cap.read()
-            FONT = ImageFont.truetype("kaiu.ttf",50,index=0)
-            rect=ft.detector(img,1)[0]
-            fv=ft.getFeatureVector(img,rect)
-            tag,dist = ft.predictFromDB(fv)
-            cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,0,255),3)
-            img=ft.addText2Img_cv2(img,tag,FONT,position=(rect.left(),rect.top()-FONT.size-1))
+            if not ret : continue
+            #取得 img 中所有人臉之矩型區域，放入rects
+            rects=ft.detector(img,1)
+            for rect in rects:
+                #取得webcam img 中人臉之特徵向量
+                fv=ft.getFeatureVector(img,rect)
+                #將特徵向量和 ft.DB 中之人特徵向量做比對，找到距離最短的(dist)當作辨識結果(tag)
+                tag,dist = ft.predictFromDB(fv)
+                #將辨識結果顯示在 img 上
+                cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,0,255),3)
+                img=ft.addText2Img_cv2(img,tag,FONT,position=(rect.left(),rect.top()-FONT.size-1))
             if cv2.waitKey(10) == 27: break
+            # 將 img show在視窗中
             cv2.imshow('press esc to exit...', img)
         cap.release()
         cv2.destroyAllWindows()
         ```
         ##### work with opencv webcam process (esay)
         ```
         import pyFaceTrace as ft
```

### Comparing `pyFaceTrace-5.0.4/README.md` & `pyFaceTrace-5.0.5/README.md`

 * *Files 15% similar despite different names*

```diff
@@ -28,25 +28,35 @@
 ft.downloadImageSamples()  
 ```
 ##### work with opencv webcam process (detail)  
 ```
 import pyFaceTrace as ft
 import cv2
 from PIL import ImageFont
+#至train資料夾載入樣本,欲辨識之目標圖片可放入 train資料夾
 ft.loadDB()
+#設定文字物件
+FONT = ImageFont.truetype("kaiu.ttf",50,index=0)
+#webcamd 影像處理迴圈
 cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
 while True:
     ret, img = cap.read()
-    FONT = ImageFont.truetype("kaiu.ttf",50,index=0)
-    rect=ft.detector(img,1)[0]
-    fv=ft.getFeatureVector(img,rect)
-    tag,dist = ft.predictFromDB(fv)
-    cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,0,255),3)
-    img=ft.addText2Img_cv2(img,tag,FONT,position=(rect.left(),rect.top()-FONT.size-1))
+    if not ret : continue
+    #取得 img 中所有人臉之矩型區域，放入rects
+    rects=ft.detector(img,1)
+    for rect in rects:
+        #取得webcam img 中人臉之特徵向量
+        fv=ft.getFeatureVector(img,rect)
+        #將特徵向量和 ft.DB 中之人特徵向量做比對，找到距離最短的(dist)當作辨識結果(tag)
+        tag,dist = ft.predictFromDB(fv)
+        #將辨識結果顯示在 img 上
+        cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,0,255),3)
+        img=ft.addText2Img_cv2(img,tag,FONT,position=(rect.left(),rect.top()-FONT.size-1))
     if cv2.waitKey(10) == 27: break
+    # 將 img show在視窗中
     cv2.imshow('press esc to exit...', img)
 cap.release()
 cv2.destroyAllWindows()
 ```
 ##### work with opencv webcam process (esay)
 ```
 import pyFaceTrace as ft
```

### Comparing `pyFaceTrace-5.0.4/setup.py` & `pyFaceTrace-5.0.5/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 #from distutils.core import setup  
 
 with open('README.md',encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
         name='pyFaceTrace',   
-        version='5.0.4',   
+        version='5.0.5',   
         description='easy Face Recognition for python',#long_description=foruser,
         long_description=long_description,
         long_description_content_type='text/markdown',
         author='KuoYuan Li',  
         author_email='funny4875@gmail.com',  
         url='https://pypi.org/project/pyFaceTrace',      
         packages=['pyFaceTrace'],
```

