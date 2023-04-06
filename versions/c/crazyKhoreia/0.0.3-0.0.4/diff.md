# Comparing `tmp/crazyKhoreia-0.0.3.tar.gz` & `tmp/crazyKhoreia-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "crazyKhoreia-0.0.3.tar", last modified: Fri May 13 18:16:22 2022, max compression
+gzip compressed data, was "crazyKhoreia-0.0.4.tar", last modified: Thu Apr  6 18:59:02 2023, max compression
```

## Comparing `crazyKhoreia-0.0.3.tar` & `crazyKhoreia-0.0.4.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2022-05-13 18:16:22.991250 crazyKhoreia-0.0.3/
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)    35149 2022-04-11 22:32:09.000000 crazyKhoreia-0.0.3/LICENSE
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     8685 2022-05-13 18:16:22.991250 crazyKhoreia-0.0.3/PKG-INFO
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     8069 2022-05-13 18:13:07.000000 crazyKhoreia-0.0.3/README.md
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       84 2022-04-11 22:32:09.000000 crazyKhoreia-0.0.3/pyproject.toml
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)      805 2022-05-13 18:16:22.991250 crazyKhoreia-0.0.3/setup.cfg
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       68 2022-04-11 22:32:09.000000 crazyKhoreia-0.0.3/setup.py
-drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2022-05-13 18:16:22.991250 crazyKhoreia-0.0.3/src/
-drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2022-05-13 18:16:22.991250 crazyKhoreia-0.0.3/src/crazyKhoreia/
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     6292 2022-04-30 22:10:02.000000 crazyKhoreia-0.0.3/src/crazyKhoreia/_3DIoU.py
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2022-04-11 22:32:09.000000 crazyKhoreia-0.0.3/src/crazyKhoreia/__init__.py
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     7090 2022-04-12 02:31:44.000000 crazyKhoreia-0.0.3/src/crazyKhoreia/crazyKhoreia.py
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     4221 2022-04-12 02:37:52.000000 crazyKhoreia-0.0.3/src/crazyKhoreia/lightPainting.py
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     3994 2022-05-13 17:50:38.000000 crazyKhoreia-0.0.3/src/crazyKhoreia/multiDronFormation.py
-drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2022-05-13 18:16:22.991250 crazyKhoreia-0.0.3/src/crazyKhoreia.egg-info/
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     8685 2022-05-13 18:16:22.000000 crazyKhoreia-0.0.3/src/crazyKhoreia.egg-info/PKG-INFO
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)      412 2022-05-13 18:16:22.000000 crazyKhoreia-0.0.3/src/crazyKhoreia.egg-info/SOURCES.txt
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)        1 2022-05-13 18:16:22.000000 crazyKhoreia-0.0.3/src/crazyKhoreia.egg-info/dependency_links.txt
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       50 2022-05-13 18:16:22.000000 crazyKhoreia-0.0.3/src/crazyKhoreia.egg-info/requires.txt
--rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       13 2022-05-13 18:16:22.000000 crazyKhoreia-0.0.3/src/crazyKhoreia.egg-info/top_level.txt
+drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2023-04-06 18:59:02.667758 crazyKhoreia-0.0.4/
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)    35149 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/LICENSE
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     8070 2023-04-06 18:59:02.667758 crazyKhoreia-0.0.4/PKG-INFO
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     7454 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/README.md
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       84 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/pyproject.toml
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)      813 2023-04-06 18:59:02.667758 crazyKhoreia-0.0.4/setup.cfg
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       68 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/setup.py
+drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2023-04-06 18:59:02.667758 crazyKhoreia-0.0.4/src/
+drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2023-04-06 18:59:02.667758 crazyKhoreia-0.0.4/src/crazyKhoreia/
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     6292 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/src/crazyKhoreia/_3DIoU.py
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/src/crazyKhoreia/__init__.py
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     7924 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/src/crazyKhoreia/crazyKhoreia.py
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     5535 2023-04-06 16:18:07.000000 crazyKhoreia-0.0.4/src/crazyKhoreia/lightPainting.py
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)    12870 2023-04-06 17:53:19.000000 crazyKhoreia-0.0.4/src/crazyKhoreia/multiDroneFormation.py
+drwxrwxr-x   0 santiagorg2401  (1000) santiagorg2401  (1000)        0 2023-04-06 18:59:02.667758 crazyKhoreia-0.0.4/src/crazyKhoreia.egg-info/
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)     8070 2023-04-06 18:59:02.000000 crazyKhoreia-0.0.4/src/crazyKhoreia.egg-info/PKG-INFO
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)      413 2023-04-06 18:59:02.000000 crazyKhoreia-0.0.4/src/crazyKhoreia.egg-info/SOURCES.txt
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)        1 2023-04-06 18:59:02.000000 crazyKhoreia-0.0.4/src/crazyKhoreia.egg-info/dependency_links.txt
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       57 2023-04-06 18:59:02.000000 crazyKhoreia-0.0.4/src/crazyKhoreia.egg-info/requires.txt
+-rw-rw-r--   0 santiagorg2401  (1000) santiagorg2401  (1000)       13 2023-04-06 18:59:02.000000 crazyKhoreia-0.0.4/src/crazyKhoreia.egg-info/top_level.txt
```

### Comparing `crazyKhoreia-0.0.3/LICENSE` & `crazyKhoreia-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `crazyKhoreia-0.0.3/setup.cfg` & `crazyKhoreia-0.0.4/setup.cfg`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = crazyKhoreia
-version = 0.0.3
+version = 0.0.4
 author = Santiago Restrepo Garcia
 author_email = sanrega24@gmail.com
 description = Python package for the crazyKhoreia project.
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/santiagorg2401/crazyKhoreia
 project_urls = 
@@ -17,19 +17,20 @@
 
 [options]
 package_dir = 
 	= src
 packages = find:
 python_requires = >=3.6
 install_requires = 
-	opencv-python
-	numpy
+	cycler
 	matplotlib
+	numpy
+	opencv_python
+	scikit_learn
 	scipy
-	scikit-learn
 
 [options.packages.find]
 where = src
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `crazyKhoreia-0.0.3/src/crazyKhoreia/_3DIoU.py` & `crazyKhoreia-0.0.4/src/crazyKhoreia/_3DIoU.py`

 * *Files identical despite different names*

### Comparing `crazyKhoreia-0.0.3/src/crazyKhoreia/crazyKhoreia.py` & `crazyKhoreia-0.0.4/src/crazyKhoreia/crazyKhoreia.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,54 +1,82 @@
 #!/usr/bin/env python3
 
 import cv2 as cv
 import numpy as np
-from matplotlib import pyplot as plt
 from cycler import cycler
+from matplotlib import pyplot as plt
 
 
 class crazyKhoreia():
-    def __init__(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT, in_path, led=False):
-        self.MAX_WIDTH, self.MAX_HEIGHT, self.MIN_WIDTH, self.MIN_HEIGHT, self.in_path, self.led = MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT, in_path, led
+    """
+    CrazyKhoreia class performs image-based waypoint generation.
+    Attributes:
+        dims        (array):    2x3 float array containing flight space constraints in the x, y, and z axis [[MIN_X, MIN_Y, MIN_Z],[MAX_X, MAX_Y, MAX_Z]]
+        in_path     (str):      Global image's path to process.
+        led         (bool):     Whether or not to control LED light relative to out of contour travel. TODO: Is this really necessary?
+        
+        cnt_scaled  (list):     List of processed contours.
+
+    Methods:
+        process_image():
+            Processes image, generate and return a contour list.
+        process_contours(contours):
+            Processes contours and returns a new list of processed contours.
+        get_waypoints():
+            Extracts waypoints from processed contours, if set, add a LED control column.
+        plot_contour_inspection(waypoints):
+            Plot a figure containing al contours and waypoints with their start/end points.
+    """
+
+    def __init__(self, dims, in_path, led=False):
+        self.dims, self.in_path, self.led = dims, in_path, led
 
         # Read image.
         self.img = cv.imread(self.in_path, cv.IMREAD_UNCHANGED)
 
         # Proccess image and get contours from it.
         contours = self.process_image()
 
         # Proccess the contours and get its parameters relative to the input image.
-        self.cnt_scaled, self.ImgShape_X, self.ImgShape_Y = self.process_contours(
-            contours)
+        self.cnt_scaled = self.process_contours(contours)
 
     def process_image(self):
         # If the image type is png, it'll have a fourth channel known as alpha, which is transparency,
         # in that case, the background will be filled in white.
         if self.img.shape[2] == 4:
             bg = np.array([255, 255, 255])
             alpha = (self.img[:, :, 3] /
                      255).reshape(self.img.shape[:2] + (1,))
             self.img = ((bg * (1 - alpha)) +
                         (self.img[:, :, :3] * alpha)).astype(np.uint8)
 
         # Flip image.
         img_flipped = cv.flip(self.img, 0)
 
-        # Invert the input image before detecting contours (see: https://stackoverflow.com/questions/29329866/how-to-avoid-detecting-image-frame-when-using-findcontours).
-        img_flipped = 255 - img_flipped
-
         # Convert the image from BGR to grayscale.
         im_gray = cv.cvtColor(img_flipped, cv.COLOR_BGR2GRAY)
 
         # Binarize the grayscale image.
         th, img_bw = cv.threshold(im_gray, 128, 192, cv.THRESH_OTSU)
 
         # Find countours.
         contours, hierarchy = cv.findContours(
             image=img_bw, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
+        contours = list(contours)
+
+        # Find frame countour, if any, and delete it (see: https://stackoverflow.com/questions/29329866/how-to-avoid-detecting-image-frame-when-using-findcontours).
+        for contour in contours:
+            x, y, w, h = cv.boundingRect(contour)
+            cnt_size = w*h
+            ImgShape_Y, ImgShape_X = self.img.shape[:2]
+            img_size = ImgShape_Y*ImgShape_X
+            ERROR_THRESHOLD = 0.01
+            error = abs(cnt_size-img_size)
+            if(error <= ERROR_THRESHOLD):
+                contours.remove(contour)
 
         # Create subplots for original image and image with contours visualization.
         fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)
 
         # img[..., ::-1] reverts the image's channel order from BGR to RGB so it can be correctly displayed by plt.imshow()
         ax0.imshow(self.img[..., ::-1])
         ax0.set_axis_off()
@@ -57,47 +85,39 @@
         ax1.set_axis_off()
         ax1.set_title("Threshold image.")
         ax2.set_axis_off()
         ax2.set_title("Image with contours.")
 
         # Draw contours on original image.
         img_with_contour = cv.drawContours(
-            image=255 - img_flipped, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=3, lineType=cv.LINE_AA)
+            image=img_flipped, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=3, lineType=cv.LINE_AA)
 
         ax2.imshow(cv.flip(img_with_contour[..., ::-1], 0))
 
         return contours
 
     def process_contours(self, contours):
         # Get image's dimensions.
         ImgShape_Y, ImgShape_X = self.img.shape[:2]
 
         # Get image's scale factor from its dimensions and user's parameters.
-        scale_fact_x = ImgShape_X/(self.MAX_WIDTH - self.MIN_WIDTH)
-        scale_fact_y = ImgShape_Y/(self.MAX_HEIGHT - self.MIN_HEIGHT)
+        scale_fact_x = ImgShape_X/(self.dims[1][1] - self.dims[0][1])
+        scale_fact_y = ImgShape_Y/(self.dims[1][2] - self.dims[0][2])
 
         # Scale contours if needed to satisfy maximum dimensions requirements.
         cnt_scaled = []
 
         for cnt in contours:
             cnt = cnt - [ImgShape_X/2, ImgShape_Y/2]
             if(scale_fact_x > 1.0 or scale_fact_y > 1.0):
                 if(scale_fact_x > scale_fact_y):
                     cnt_scaled.append(cnt*(1.0/scale_fact_x))
                 else:
                     cnt_scaled.append(cnt*(1.0/scale_fact_y))
 
-        # Adjust image parameters relative to its scaled contours.
-        if(scale_fact_x > scale_fact_y):
-            ImgShape_X /= scale_fact_x
-            ImgShape_Y /= scale_fact_x
-        if(scale_fact_y > scale_fact_x):
-            ImgShape_X /= scale_fact_y
-            ImgShape_Y /= scale_fact_y
-
        # Translate the scaled contours to satisfy minimum dimensions requirements.
         minX = []
         minY = []
 
         for cnt in cnt_scaled:
             x = np.array(cnt)
             x = np.reshape(x, (len(cnt), 2))
@@ -105,20 +125,20 @@
             minY.append(min(x[:, 1]))
 
         minX = abs(min(minX))
         minY = abs(min(minY))
 
         cnt_scaled_x = []
         for cnt in cnt_scaled:
-            cnt_x = cnt + [minX, minY] + [self.MIN_WIDTH, self.MIN_HEIGHT]
+            cnt_x = cnt + [minX, minY] + [self.dims[0][1], self.dims[0][2]]
             cnt_scaled_x.append(cnt_x)
 
         cnt_scaled = cnt_scaled_x
 
-        return cnt_scaled, ImgShape_X, ImgShape_Y
+        return cnt_scaled
 
     def plot_contour_inspection(self, wayPoints):
         strPoints = np.empty((0, 2))
         endPoints = np.empty((0, 2))
 
         # See https://matplotlib.org/3.5.1/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py for more colors.
         cc = (cycler(color=['purple', 'orange', 'lime', 'royalblue', 'steelblue', 'cyan', 'gold']) +
@@ -174,8 +194,8 @@
                     [1.5*np.ones(shape=(len(x),)), x[:, 0], x[:, 1], led]).T
             else:
                 stck = np.array(
                     [1.5*np.ones(shape=(len(x),)), x[:, 0], x[:, 1]]).T
 
             wayPoints = np.vstack([wayPoints, stck])
 
-        return wayPoints
+        return wayPoints
```

