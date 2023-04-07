# Comparing `tmp/Lab_3419-0.0.3-py3-none-any.whl.zip` & `tmp/Lab_3419-1.0.0-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 5100 bytes, number of entries: 6
--rw-rw-rw-  2.0 fat     3818 b- defN 22-Jul-29 20:18 Lab_3419/__init__.py
--rw-rw-rw-  2.0 fat     1090 b- defN 22-Aug-03 11:41 Lab_3419-0.0.3.dist-info/LICENSE
--rw-rw-rw-  2.0 fat     4306 b- defN 22-Aug-03 11:41 Lab_3419-0.0.3.dist-info/METADATA
--rw-rw-rw-  2.0 fat       92 b- defN 22-Aug-03 11:41 Lab_3419-0.0.3.dist-info/WHEEL
--rw-rw-rw-  2.0 fat        9 b- defN 22-Aug-03 11:41 Lab_3419-0.0.3.dist-info/top_level.txt
-?rw-rw-r--  2.0 fat      467 b- defN 22-Aug-03 11:41 Lab_3419-0.0.3.dist-info/RECORD
-6 files, 9782 bytes uncompressed, 4254 bytes compressed:  56.5%
+Zip file size: 5475 bytes, number of entries: 6
+-rw-rw-rw-  2.0 fat     6713 b- defN 23-Apr-07 05:35 Lab_3419/__init__.py
+-rw-rw-rw-  2.0 fat     1090 b- defN 23-Apr-07 05:41 Lab_3419-1.0.0.dist-info/LICENSE
+-rw-rw-rw-  2.0 fat     4443 b- defN 23-Apr-07 05:41 Lab_3419-1.0.0.dist-info/METADATA
+-rw-rw-rw-  2.0 fat       92 b- defN 23-Apr-07 05:41 Lab_3419-1.0.0.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat        9 b- defN 23-Apr-07 05:41 Lab_3419-1.0.0.dist-info/top_level.txt
+-rw-rw-r--  2.0 fat      467 b- defN 23-Apr-07 05:41 Lab_3419-1.0.0.dist-info/RECORD
+6 files, 12814 bytes uncompressed, 4629 bytes compressed:  63.9%
```

## zipnote {}

```diff
@@ -1,19 +1,19 @@
 Filename: Lab_3419/__init__.py
 Comment: 
 
-Filename: Lab_3419-0.0.3.dist-info/LICENSE
+Filename: Lab_3419-1.0.0.dist-info/LICENSE
 Comment: 
 
-Filename: Lab_3419-0.0.3.dist-info/METADATA
+Filename: Lab_3419-1.0.0.dist-info/METADATA
 Comment: 
 
-Filename: Lab_3419-0.0.3.dist-info/WHEEL
+Filename: Lab_3419-1.0.0.dist-info/WHEEL
 Comment: 
 
-Filename: Lab_3419-0.0.3.dist-info/top_level.txt
+Filename: Lab_3419-1.0.0.dist-info/top_level.txt
 Comment: 
 
-Filename: Lab_3419-0.0.3.dist-info/RECORD
+Filename: Lab_3419-1.0.0.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Lab_3419/__init__.py

```diff
@@ -1,38 +1,71 @@
 import numpy as np
 from multiprocessing import Pool
 
 
-# Point in 3D ---> point = (x, y, z)
-# Line in 3D  ---> line points = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)])
-# Line in 3D  ---> line = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)])
-# Fiited line ---> line = numpy.array([(x1, y1, z1), (x2, y2, z2)])
+# Point in 3D  ---> point = (x, y, z)
+# Points in 3D ---> line points = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)])
+# Line in 3D   ---> line = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)])
+# Fiited line  ---> line = numpy.array([(x1, y1, z1), (x2, y2, z2)])
 
 
 def add_resolusion(points_, res_=0.0):
     data_x_, data_y_, data_z_ = points_.T
     data_x_e_ = data_x_ + np.random.normal(0, res_, len(data_x_))
     data_y_e_ = data_y_ + np.random.normal(0, res_, len(data_y_))
     # data_z_e_ = data_z_ + np.random.normal(0, res_, len(data_z_))
     data_z_e_ = data_z_
     data_xyz_e_ = np.array([data_x_e_, data_y_e_, data_z_e_]).T
     return data_xyz_e_
 
+def find_angle(track_1, track_2):
+    cos_theta_ = np.dot(track_1, track_2) / (np.linalg.norm(track_1) * np.linalg.norm(track_2))
+    theta_rad_ = np.arccos(np.clip(cos_theta_, -1.0, 1.0))
+    theta_deg_ = np.rad2deg(theta_rad_)
+    return theta_deg_
+
+def check_tracklets(points_):
+    tracklet_1 = points_[0] - points_[1]
+    tracklet_2 = points_[1] - points_[2]
+    tracklet_3 = points_[0] - points_[2]
+    tracklet_4 = points_[3] - points_[4]
+    tracklet_5 = points_[4] - points_[5]
+    tracklet_6 = points_[3] - points_[5]
+    theta_1 = find_angle(tracklet_1, tracklet_2)
+    theta_2 = find_angle(tracklet_2, tracklet_3)
+    theta_3 = find_angle(tracklet_1, tracklet_3)
+    theta_4 = find_angle(tracklet_4, tracklet_5)
+    theta_5 = find_angle(tracklet_5, tracklet_6)
+    theta_6 = find_angle(tracklet_4, tracklet_6)
+    theta_tracklet = max(theta_1, theta_2, theta_3, theta_4, theta_5, theta_6)
+    return theta_tracklet
 
 def fit_3D(points_):
     data_x_, data_y_, data_z_ = points_.T
     fit_z_ = np.array([data_z_[0], data_z_[-1]])
-    m_zx_, c_zx_, *_ = np.polyfit(data_x_, data_z_, 1)
-    m_zy_, c_zy_, *_ = np.polyfit(data_y_, data_z_, 1)
-    fit_x_ = (fit_z_ - c_zx_) / m_zx_
-    fit_y_ = (fit_z_ - c_zy_) / m_zy_
+    m_zx_, c_zx_, *_ = np.polyfit(data_z_, data_x_, 1)
+    m_zy_, c_zy_, *_ = np.polyfit(data_z_, data_y_, 1)
+    fit_x_ = m_zx_ * fit_z_ + c_zx_
+    fit_y_ = m_zy_ * fit_z_ + c_zy_
     fit_xyz_ = np.array([fit_x_, fit_y_, fit_z_]).T
     return fit_xyz_
 
 
+def fit_3D_with_parameters(points_):
+    data_x_, data_y_, data_z_ = points_.T
+    fit_z_ = np.array([data_z_[0], data_z_[-1]])
+    m_zx_, c_zx_, *_ = np.polyfit(data_z_, data_x_, 1)
+    m_zy_, c_zy_, *_ = np.polyfit(data_z_, data_y_, 1)
+    fit_x_ = m_zx_ * fit_z_ + c_zx_
+    fit_y_ = m_zy_ * fit_z_ + c_zy_
+    fit_xyz_ = np.array([fit_x_, fit_y_, fit_z_]).T
+    fit_params_ = {'line': fit_xyz_, 'm_zx': m_zx_, 'c_zx': c_zx_, 'm_zy': m_zy_, 'c_zy': c_zy_}
+    return fit_params_
+
+
 def POCA_Point(line_1_, line_2_):
     P0_, P1_ = line_1_[0], line_1_[1]
     Q0_, Q1_ = line_2_[0], line_2_[1]
     u_, v_, w_ = (P1_ - P0_), (Q1_ - Q0_), (P0_ - Q0_)
     cos_theta_ = np.dot(u_, v_) / (np.linalg.norm(u_) * np.linalg.norm(v_))
     theta_rad_ = np.arccos(np.clip(cos_theta_, -1.0, 1.0))
     theta_deg_ = np.rad2deg(theta_rad_)
@@ -41,41 +74,72 @@
     if f_ == 0.0: f_ = 1.0e-10  # to avoid zero division error
     sc_, tc_ = (b_ * e_ - c_ * d_) / f_, (a_ * e_ - b_ * d_) / f_
     M1_, M2_ = (P0_ + sc_ * u_), (Q0_ + tc_ * v_)
     M_ = (M1_ + M2_) / 2.0
     return M_, theta_deg_
 
 
-def calculate(data_):
+def POCA_Point_with_parameters(line_1_, line_2_):
+    P0_, P1_ = line_1_[0], line_1_[1]
+    Q0_, Q1_ = line_2_[0], line_2_[1]
+    u_, v_, w_ = (P1_ - P0_), (Q1_ - Q0_), (P0_ - Q0_)
+    cos_theta_ = np.dot(u_, v_) / (np.linalg.norm(u_) * np.linalg.norm(v_))
+    theta_rad_ = np.arccos(np.clip(cos_theta_, -1.0, 1.0))
+    theta_deg_ = np.rad2deg(theta_rad_)
+    a_, b_, c_ = np.dot(u_, u_), np.dot(u_, v_), np.dot(v_, v_)
+    d_, e_, f_ = np.dot(u_, w_), np.dot(v_, w_), (a_ * c_ - b_ * b_)
+    if f_ == 0.0: f_ = 1.0e-10  # to avoid zero division error
+    sc_, tc_ = (b_ * e_ - c_ * d_) / f_, (a_ * e_ - b_ * d_) / f_
+    M1_, M2_ = (P0_ + sc_ * u_), (Q0_ + tc_ * v_)
+    M12_ = np.linalg.norm(M2_ - M1_)
+    M_ = (M1_ + M2_) / 2.0
+    poca_params_ = {'poca': M_, 'deviation': theta_deg_, 'poca_1': M1_, 'poca_2': M2_, 'poca_gap': M12_}
+    return poca_params_
+
+
+def calculate(data_, sigma_=0.100):
     data_c_ = np.array([float(_) for _ in data_.split()])
     data_c_ = data_c_[0:18]
     rpc_hits_ = data_c_.reshape(6, 3)
-    sigma_ = 0.0
+#    sigma_ = 0.100
     rpc_hits_ = add_resolusion(rpc_hits_, sigma_)
     top_hits_, bottom_hits_ = rpc_hits_[0:3], rpc_hits_[3:6]
     top_line_ = fit_3D(top_hits_)
     bottom_line_ = fit_3D(bottom_hits_)
     (xp_, yp_, zp_), theta_deg_ = POCA_Point(top_line_, bottom_line_)
     return xp_, yp_, zp_, theta_deg_
 
 
+def calculate_with_parameters(data_, sigma_=0.100):
+    data_c_ = np.array([float(_) for _ in data_.split()])
+    data_c_ = data_c_[0:18]
+    rpc_hits_ = data_c_.reshape(6, 3)
+    # sigma_ = 0.100
+    rpc_hits_ = add_resolusion(rpc_hits_, sigma_)
+    top_hits_, bottom_hits_ = rpc_hits_[0:3], rpc_hits_[3:6]
+    top_line_ = fit_3D_with_parameters(top_hits_)
+    bottom_line_ = fit_3D_with_parameters(bottom_hits_)
+    (xp_, yp_, zp_), theta_deg_ = POCA_Point_with_parameters(top_line_, bottom_line_)
+    return xp_, yp_, zp_, theta_deg_
+
+
 def file_to_poca(file_name_, is_save=False):
     file_i_ = open(file_name_, 'r')
     data_file_ = file_i_.readlines()
     file_i_.close()
     print('Process started...')
     all_poca_data_ = []
     for line_ in data_file_:
         poca_data_ = calculate(line_)
         all_poca_data_.append(poca_data_)
     print('Reading Complited...')
     all_poca_data_ = np.array(all_poca_data_)
     if is_save:
         print('Saving Data...')
-        np.savetxt(file_name_[:-4]+'_poca_points.txt', all_poca_data_, fmt='%.4f')
+        np.savetxt(file_name_[:-4] + '_poca_points.txt', all_poca_data_, fmt='%.4f')
     print('Analysis Complited...')
     return all_poca_data_
 
 
 def file_to_poca_mt(file_name_, is_save=False):
     file_i_ = open(file_name_, 'r')
     data_file_ = file_i_.readlines()
@@ -85,20 +149,19 @@
     all_poca_data_ = process_pool_.map(calculate, data_file_)
     process_pool_.close()
     process_pool_.join()
     print('Reading Complited. ..')
     all_poca_data_ = np.array(all_poca_data_)
     if is_save:
         print('Saving Data...')
-        np.savetxt(file_name_[:-4]+'_poca_points.txt', all_poca_data_, fmt='%.4f')
+        np.savetxt(file_name_[:-4] + '_poca_points.txt', all_poca_data_, fmt='%.4f')
     print('Analysis Complited...')
     return all_poca_data_
 
 
 def filter_poca_data(poca_data_, min_theta_):
     filter_data_ = []
     for xp_, yp_, zp_, theta_deg_ in poca_data_:
-        if theta_deg_ < min_theta_ : continue
+        if theta_deg_ < min_theta_: continue
         filter_data_.append([xp_, yp_, zp_, theta_deg_])
     filter_data_ = np.array(filter_data_)
     return filter_data_
-
```

## Comparing `Lab_3419-0.0.3.dist-info/LICENSE` & `Lab_3419-1.0.0.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `Lab_3419-0.0.3.dist-info/METADATA` & `Lab_3419-1.0.0.dist-info/METADATA`

 * *Files 22% similar despite different names*

```diff
@@ -1,107 +1,112 @@
-Metadata-Version: 2.1
-Name: Lab-3419
-Version: 0.0.3
-Summary: A small example package
-Author-email: Subhendu Das <subhendudas.sinp@gmail.com>
-License: MIT License        
-        Copyright (c) 2022 Subhendu Das        
-        Permission is hereby granted, free of charge, to any person obtaining a copy
-        of this software and associated documentation files (the "Software"), to deal
-        in the Software without restriction, including without limitation the rights
-        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-        copies of the Software, and to permit persons to whom the Software is
-        furnished to do so, subject to the following conditions:        
-        The above copyright notice and this permission notice shall be included in all
-        copies or substantial portions of the Software.        
-        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-        SOFTWARE.        
-Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: OS Independent
-Requires-Python: >=3.6
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
-Lab 3419
-========
-Lab_3419 is a cross-platform python library. It contains some useful function for MST simulation
-
-Installation
-============
-`pip install Lab_3419`
-
-Dependencies
-============
-
-Lab_3419 supports Python 3.6 and later. If you are installing Lab_3419 from PyPI using pip:
-please install numpy before installing Lab_3419.
-
-Example Usage
-=============
-### Import Lab_3419 module
-```python
-    >>> import Lab_3419 as lb
-```
-### Some important data format
-```
-1. A point in 3D Space --> point = (x, y, z)
-2. Line points in 3D Space --> points = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3), ...])
-3. A fitted Line in 3D Space --> fitted_line = numpy.array([(x1, y1, z1), (x2, y2, z2)])
-```
-
-### Fit 3D line
-```python
-    >>> simulated_points = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)])
-    >>> points = lb.add_resolusion(points_=simulated_points, res_=position_resolution)
-    >>> fitted_line = lb.fit_3D(points)
-```
-
-### Find POCA point
-```python
-    >>> poca_xyz, deviation = lb.POCA_Point(fitted_line_1, fitted_line_)
-```
-
-### Find POCA point directly from data string
-```python
-    >>> data_string = "x1 y1 z1 x2 y2 z2 x3 y3 z3 x4 y4 z4 x5 y5 z5 x6 y6 z6"
-    >>> poca_x, poca_y, poca_z, deviation = lb.calculate(data_string)
-```
-### Find POCA points directly from data file
-A file contains multiple number of data string. 
-
-Example data file: data_file.txt
-```
--279.717 270.73 -391 -233.76 277.098 -321 -187.807 283.464 -251 140.424 328.94 249 186.895 335.379 319.776 232.346 341.674 389
-42.0465 62.3473 -391 28.2942 59.1205 -321 14.5489 55.8892 -251 -83.7591 32.7117 249.426 -97.4228 29.4739 319 -111.175 26.2129 389
-138.413 682.409 -391 134.046 628.646 -321 129.676 574.895 -251 98.4977 190.939 249 94.075 136.334 320.099 89.7752 83.4056 389
-174.57 -20.909 -391 149.972 -1.86935 -321 125.373 17.1698 -251 -50.315 153.155 249 -74.9115 172.191 319 -99.567 191.274 389
-```
-
-Example code
-```python
-    >>> all_poca_points = lb.file_to_poca("data_file.txt", is_save=False)
-    # To write into new file use "is_save = True". 
-    # This will create a file "data_file_poca_points.txt"
-    >>> lb.file_to_poca("data_file.txt", is_save=True)
-    # Same function with multi-threaded mode
-    >>> all_poca_points = lb.file_to_poca_mt("data_file.txt", is_save=False)
-    >>> lb.file_to_poca_mt("data_file.txt", is_save=True)
-```
-
-### Filter POCA points according to their deviation angle
-Example poca file: data_file.txt
-```
--320.1396 -187.6816 -157.1030 1.0040
-351.6875 -307.2162 -125.7960 0.0117
-288.7207 349.4853 474.8601 3.0034
--41.1887 42.8014 32.7391 0.0243
-```
-
-```python
-    >>> filter_poca_points = lb.filter_poca_data(poca_data_array, minimum_theta)
-```
+Metadata-Version: 2.1
+Name: Lab-3419
+Version: 1.0.0
+Summary: Lab_3419 is a cross-platform python library
+Author-email: Subhendu Das <subhendudas.sinp@gmail.com>
+License: MIT License
+        
+        Copyright (c) 2022 Subhendu Das
+        
+        Permission is hereby granted, free of charge, to any person obtaining a copy
+        of this software and associated documentation files (the "Software"), to deal
+        in the Software without restriction, including without limitation the rights
+        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
+        copies of the Software, and to permit persons to whom the Software is
+        furnished to do so, subject to the following conditions:
+        
+        The above copyright notice and this permission notice shall be included in all
+        copies or substantial portions of the Software.
+        
+        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
+        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
+        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
+        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
+        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
+        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
+        SOFTWARE.
+        
+Classifier: Programming Language :: Python :: 3
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Requires-Python: >=3.6
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
+Lab 3419
+========
+Lab_3419 is a cross-platform python library. It contains some useful function for MST simulation
+
+Installation
+============
+`pip install Lab_3419`
+
+Dependencies
+============
+
+Lab_3419 supports Python 3.6 and later. If you are installing Lab_3419 from PyPI using pip:
+please install numpy before installing Lab_3419.
+
+Example Usage
+=============
+### Import Lab_3419 module
+```python
+    >>> import Lab_3419 as lb
+```
+### Some important data format
+```
+1. A point in 3D Space --> point = (x, y, z)
+2. Line points in 3D Space --> points = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3), ...])
+3. A fitted Line in 3D Space --> fitted_line = numpy.array([(x1, y1, z1), (x2, y2, z2)])
+```
+
+### Fit 3D line
+```python
+    >>> simulated_points = numpy.array([(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)])
+    >>> points = lb.add_resolusion(points_=simulated_points, res_=position_resolution)
+    >>> fitted_line = lb.fit_3D(points)
+```
+
+### Find POCA point
+```python
+    >>> poca_xyz, deviation = lb.POCA_Point(fitted_line_1, fitted_line_)
+```
+
+### Find POCA point directly from data string
+```python
+    >>> data_string = "x1 y1 z1 x2 y2 z2 x3 y3 z3 x4 y4 z4 x5 y5 z5 x6 y6 z6"
+    >>> poca_x, poca_y, poca_z, deviation = lb.calculate(data_string)
+```
+### Find POCA points directly from data file
+A file contains multiple number of data string. 
+
+Example data file: data_file.txt
+```
+-279.717 270.73 -391 -233.76 277.098 -321 -187.807 283.464 -251 140.424 328.94 249 186.895 335.379 319.776 232.346 341.674 389
+42.0465 62.3473 -391 28.2942 59.1205 -321 14.5489 55.8892 -251 -83.7591 32.7117 249.426 -97.4228 29.4739 319 -111.175 26.2129 389
+138.413 682.409 -391 134.046 628.646 -321 129.676 574.895 -251 98.4977 190.939 249 94.075 136.334 320.099 89.7752 83.4056 389
+174.57 -20.909 -391 149.972 -1.86935 -321 125.373 17.1698 -251 -50.315 153.155 249 -74.9115 172.191 319 -99.567 191.274 389
+```
+
+Example code
+```python
+    >>> all_poca_points = lb.file_to_poca("data_file.txt", is_save=False)
+    # To write into new file use "is_save = True". 
+    # This will create a file "data_file_poca_points.txt"
+    >>> lb.file_to_poca("data_file.txt", is_save=True)
+    # Same function with multi-threaded mode
+    >>> all_poca_points = lb.file_to_poca_mt("data_file.txt", is_save=False)
+    >>> lb.file_to_poca_mt("data_file.txt", is_save=True)
+```
+
+### Filter POCA points according to their deviation angle
+Example poca file: data_file.txt
+```
+-320.1396 -187.6816 -157.1030 1.0040
+351.6875 -307.2162 -125.7960 0.0117
+288.7207 349.4853 474.8601 3.0034
+-41.1887 42.8014 32.7391 0.0243
+```
+
+```python
+    >>> filter_poca_points = lb.filter_poca_data(poca_data_array, minimum_theta)
+```
```

