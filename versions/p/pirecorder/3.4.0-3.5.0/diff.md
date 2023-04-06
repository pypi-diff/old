# Comparing `tmp/pirecorder-3.4.0.tar.gz` & `tmp/pirecorder-3.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pirecorder-3.4.0.tar", last modified: Fri Mar 24 15:09:53 2023, max compression
+gzip compressed data, was "dist/pirecorder-3.5.0.tar", last modified: Thu Apr  6 13:20:23 2023, max compression
```

## Comparing `pirecorder-3.4.0.tar` & `pirecorder-3.5.0.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 jollewjolles   (501) staff       (20)        0 2023-03-24 15:09:53.070685 pirecorder-3.4.0/
--rw-r--r--   0 jollewjolles   (501) staff       (20)     9310 2023-03-24 15:09:53.070008 pirecorder-3.4.0/PKG-INFO
--rw-r--r--   0 jollewjolles   (501) staff       (20)     7451 2023-03-24 15:03:34.000000 pirecorder-3.4.0/README.md
-drwxr-xr-x   0 jollewjolles   (501) staff       (20)        0 2023-03-24 15:09:53.057386 pirecorder-3.4.0/pirecorder/
--rw-r--r--   0 jollewjolles   (501) staff       (20)      828 2023-03-24 15:04:14.000000 pirecorder-3.4.0/pirecorder/__init__.py
--rw-r--r--   0 jollewjolles   (501) staff       (20)      638 2023-03-24 15:05:55.000000 pirecorder-3.4.0/pirecorder/__version__.py
--rw-r--r--   0 jollewjolles   (501) staff       (20)     7575 2023-03-24 15:04:06.000000 pirecorder-3.4.0/pirecorder/camconfig.py
--rw-r--r--   0 jollewjolles   (501) staff       (20)     9870 2023-03-24 15:04:04.000000 pirecorder-3.4.0/pirecorder/convert.py
--rwxr--r--   0 jollewjolles   (501) staff       (20)    31665 2023-03-24 15:03:59.000000 pirecorder-3.4.0/pirecorder/pirecorder.py
--rwxr--r--   0 jollewjolles   (501) staff       (20)     7339 2023-03-24 15:03:56.000000 pirecorder-3.4.0/pirecorder/schedule.py
--rwxr--r--   0 jollewjolles   (501) staff       (20)     9990 2023-03-24 15:03:52.000000 pirecorder-3.4.0/pirecorder/stream.py
--rwxr--r--   0 jollewjolles   (501) staff       (20)     5187 2023-03-24 15:03:50.000000 pirecorder-3.4.0/pirecorder/videoin.py
-drwxr-xr-x   0 jollewjolles   (501) staff       (20)        0 2023-03-24 15:09:53.068997 pirecorder-3.4.0/pirecorder.egg-info/
--rw-r--r--   0 jollewjolles   (501) staff       (20)     9310 2023-03-24 15:09:52.000000 pirecorder-3.4.0/pirecorder.egg-info/PKG-INFO
--rw-r--r--   0 jollewjolles   (501) staff       (20)      410 2023-03-24 15:09:53.000000 pirecorder-3.4.0/pirecorder.egg-info/SOURCES.txt
--rw-r--r--   0 jollewjolles   (501) staff       (20)        1 2023-03-24 15:09:52.000000 pirecorder-3.4.0/pirecorder.egg-info/dependency_links.txt
--rw-r--r--   0 jollewjolles   (501) staff       (20)      195 2023-03-24 15:09:52.000000 pirecorder-3.4.0/pirecorder.egg-info/entry_points.txt
--rw-r--r--   0 jollewjolles   (501) staff       (20)      212 2023-03-24 15:09:52.000000 pirecorder-3.4.0/pirecorder.egg-info/requires.txt
--rw-r--r--   0 jollewjolles   (501) staff       (20)       11 2023-03-24 15:09:52.000000 pirecorder-3.4.0/pirecorder.egg-info/top_level.txt
--rw-r--r--   0 jollewjolles   (501) staff       (20)       38 2023-03-24 15:09:53.070856 pirecorder-3.4.0/setup.cfg
--rwxr--r--   0 jollewjolles   (501) staff       (20)     3420 2023-03-24 15:06:02.000000 pirecorder-3.4.0/setup.py
+drwxr-xr-x   0 jollewjolles   (501) staff       (20)        0 2023-04-06 13:20:23.000000 pirecorder-3.5.0/
+-rw-r--r--   0 jollewjolles   (501) staff       (20)     9310 2023-04-06 13:20:23.000000 pirecorder-3.5.0/PKG-INFO
+-rw-r--r--   0 jollewjolles   (501) staff       (20)     7451 2023-03-24 15:03:34.000000 pirecorder-3.5.0/README.md
+drwxr-xr-x   0 jollewjolles   (501) staff       (20)        0 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder/
+-rw-r--r--   0 jollewjolles   (501) staff       (20)      828 2023-03-24 15:04:14.000000 pirecorder-3.5.0/pirecorder/__init__.py
+-rw-r--r--   0 jollewjolles   (501) staff       (20)      638 2023-04-06 13:18:32.000000 pirecorder-3.5.0/pirecorder/__version__.py
+-rw-r--r--   0 jollewjolles   (501) staff       (20)     7575 2023-03-24 15:04:06.000000 pirecorder-3.5.0/pirecorder/camconfig.py
+-rw-r--r--   0 jollewjolles   (501) staff       (20)     9870 2023-03-24 15:04:04.000000 pirecorder-3.5.0/pirecorder/convert.py
+-rwxr-xr-x   0 jollewjolles   (501) staff       (20)    38737 2023-04-06 13:18:32.000000 pirecorder-3.5.0/pirecorder/pirecorder.py
+-rwxr--r--   0 jollewjolles   (501) staff       (20)     7339 2023-03-24 15:03:56.000000 pirecorder-3.5.0/pirecorder/schedule.py
+-rwxr--r--   0 jollewjolles   (501) staff       (20)     9990 2023-03-24 15:03:52.000000 pirecorder-3.5.0/pirecorder/stream.py
+-rwxr--r--   0 jollewjolles   (501) staff       (20)     5187 2023-03-24 15:03:50.000000 pirecorder-3.5.0/pirecorder/videoin.py
+drwxr-xr-x   0 jollewjolles   (501) staff       (20)        0 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder.egg-info/
+-rw-r--r--   0 jollewjolles   (501) staff       (20)     9310 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder.egg-info/PKG-INFO
+-rw-r--r--   0 jollewjolles   (501) staff       (20)      410 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder.egg-info/SOURCES.txt
+-rw-r--r--   0 jollewjolles   (501) staff       (20)        1 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder.egg-info/dependency_links.txt
+-rw-r--r--   0 jollewjolles   (501) staff       (20)      195 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder.egg-info/entry_points.txt
+-rw-r--r--   0 jollewjolles   (501) staff       (20)      212 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder.egg-info/requires.txt
+-rw-r--r--   0 jollewjolles   (501) staff       (20)       11 2023-04-06 13:20:23.000000 pirecorder-3.5.0/pirecorder.egg-info/top_level.txt
+-rw-r--r--   0 jollewjolles   (501) staff       (20)       38 2023-04-06 13:20:23.000000 pirecorder-3.5.0/setup.cfg
+-rwxr-xr-x   0 jollewjolles   (501) staff       (20)     3420 2023-04-06 13:18:32.000000 pirecorder-3.5.0/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive
+POSIX tar archive (GNU)
```

### Comparing `pirecorder-3.4.0/PKG-INFO` & `pirecorder-3.5.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: pirecorder
-Version: 3.4.0
+Version: 3.5.0
 Summary: A python package for controlled and automated image and video recording with the raspberry pi
 Home-page: https://github.com/jollejolles
 Author: Jolle Jolles
 Author-email: j.w.jolles@gmail.com
 Maintainer: Jolle Jolles
 Maintainer-email: j.w.jolles@gmail.com
 License: License :: OSI Approved :: Apache Software License
-Download-URL: https://github.com/jollejolles/pirecorder/archive/v3.4.0.tar.gz
+Download-URL: https://github.com/jollejolles/pirecorder/archive/v3.5.0.tar.gz
 Description: [![Downloads](https://pepy.tech/badge/pirecorder)](https://pepy.tech/project/pirecorder)
         
         # pirecorder
         **A Python package for controlled and automated image and video recording with the raspberry pi**
         
         *pirecorder* is a Python package, built on the [picamera](http://picamera.readthedocs.io/) and [OpenCV](https://opencv.org/) libraries, that provides a flexible solution for the collection of consistent image and video data with the raspberry pi. It was developed to overcome the need for a complete solution to help researchers, especially those with limited coding skills, to easily set up and configure their raspberry pi to run large numbers of controlled and automated image and video recordings using optimal settings.
```

#### html2text {}

```diff
@@ -1,14 +1,14 @@
-Metadata-Version: 2.1 Name: pirecorder Version: 3.4.0 Summary: A python package
+Metadata-Version: 2.1 Name: pirecorder Version: 3.5.0 Summary: A python package
 for controlled and automated image and video recording with the raspberry pi
 Home-page: https://github.com/jollejolles Author: Jolle Jolles Author-email:
 j.w.jolles@gmail.com Maintainer: Jolle Jolles Maintainer-email:
 j.w.jolles@gmail.com License: License :: OSI Approved :: Apache Software
 License Download-URL: https://github.com/jollejolles/pirecorder/archive/
-v3.4.0.tar.gz Description: [![Downloads](https://pepy.tech/badge/pirecorder)]
+v3.5.0.tar.gz Description: [![Downloads](https://pepy.tech/badge/pirecorder)]
 (https://pepy.tech/project/pirecorder) # pirecorder **A Python package for
 controlled and automated image and video recording with the raspberry pi**
 *pirecorder* is a Python package, built on the [picamera](http://
 picamera.readthedocs.io/) and [OpenCV](https://opencv.org/) libraries, that
 provides a flexible solution for the collection of consistent image and video
 data with the raspberry pi. It was developed to overcome the need for a
 complete solution to help researchers, especially those with limited coding
```

### Comparing `pirecorder-3.4.0/README.md` & `pirecorder-3.5.0/README.md`

 * *Files identical despite different names*

### Comparing `pirecorder-3.4.0/pirecorder/__init__.py` & `pirecorder-3.5.0/pirecorder/__init__.py`

 * *Files identical despite different names*

### Comparing `pirecorder-3.4.0/pirecorder/__version__.py` & `pirecorder-3.5.0/pirecorder/__version__.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,8 +11,8 @@
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """
 
-__version__ = "3.4.0"
+__version__ = "3.5.0"
```

### Comparing `pirecorder-3.4.0/pirecorder/camconfig.py` & `pirecorder-3.5.0/pirecorder/camconfig.py`

 * *Files identical despite different names*

### Comparing `pirecorder-3.4.0/pirecorder/convert.py` & `pirecorder-3.5.0/pirecorder/convert.py`

 * *Files identical despite different names*

### Comparing `pirecorder-3.4.0/pirecorder/pirecorder.py` & `pirecorder-3.5.0/pirecorder/pirecorder.py`

 * *Files 16% similar despite different names*

```diff
@@ -107,36 +107,41 @@
 
         lineprint("pirecorder "+__version__+" started!", date=True)
         lineprint("="*47, False)
 
         self.brightfile = self.setupdir+"/cusbright.yml"
         self.configfilerel = configfile
         self.configfile = self.setupdir+"/"+configfile
+        self.nametypes = ("label","date","time","datetime","counter","rpi","")
 
         self.config = LocalConfig(self.configfile, compact_form = True)
+        overwrite=True
         if not os.path.isfile(self.configfile):
             lineprint("Config file "+configfile+" not found, new file created..")
             for section in ["rec","cam","cus","img","vid"]:
                 if section not in list(self.config):
                     self.config.add_section(section)
-            self.settings(recdir="pirecorder/recordings",subdirs=False,
-                          label="test",rectype="img",rotation=0,brighttune=0,
-                          roi=None,gains=(1.0,2.5),brightness=45,contrast=10,
-                          saturation=0,iso=200,sharpness=0,compensation=0,
-                          shutterspeed=8000,imgdims=(2592,1944),maxres="v2",
-                          viddims=(1640,1232),imgfps=1,vidfps=24,imgwait=5.0,
-                          imgnr=12,imgtime=60,imgquality=50,vidduration=10,
-                          viddelay=10,vidquality=11,automode=True,internal="",
-                          maxviddur=3600,maxvidsize=0)
-            lineprint("Config settings stored..")
-
+            set=True
+        elif str(self.config).count("=")<36:
+            overwrite=False
+            set=True
         else:
+            set=False
             lineprint("Config file "+configfile+" loaded..")
             lineprint("Recording " + self.config.rec.rectype + " in " +\
                           self.home + self.config.rec.recdir)
+        if set:
+            self.settings(overwrite=overwrite,internal="",
+                          recdir="pirecorder/recordings",subdirs=False,label="test",rectype="img",maxres="v2",
+                          automode=True,brightness=45,contrast=10,saturation=0,iso=200,sharpness=0,compensation=0,shutterspeed=8000,
+                          rotation=0,brighttune=0,roi=None,gains=(1.0,2.5),annotatesize=0,nameparam1="label",nameparam2="date",nameparam3="rpi",nameparam4="counter",nameparam5="time",
+                          imgdims=(2592,1944),imgfps=1,imgwait=5.0,imgnr=12,imgtime=60,imgquality=50,
+                          viddims=(1640,1232),vidfps=24,vidduration=10,viddelay=10,vidquality=11,maxviddur=3600,maxvidsize=0)
+            lineprint("Config settings stored and updated..")
+
 
         self._imgparams()
         self._shuttertofps()
         if self.config.rec.rectype == "imgseq":
             if self.config.cam.shutterspeed/1000000.>=(self.config.img.imgwait/5):
                 lineprint("imgwait is not enough for provided shutterspeed" + \
                           ", will be overwritten..")
@@ -159,14 +164,18 @@
         import picamera
         import picamera.array
 
         self.cam = picamera.PiCamera()
         self.cam.rotation = self.config.cus.rotation
         self.cam.exposure_compensation = self.config.cam.compensation
 
+        if self.config.cus.annotatesize>5:
+            self.cam.annotate_background = picamera.Color('black')
+            self.cam.annotate_text_size = self.config.cus.annotatesize
+
         if self.config.rec.rectype in ["img","imgseq"]:
             self.cam.resolution = literal_eval(self.config.img.imgdims)
             self.cam.framerate = self.config.img.imgfps
         if self.config.rec.rectype in ["vid","vidseq"]:
             self.cam.resolution = picamconv(literal_eval(self.config.vid.viddims))
             self.cam.framerate = self.config.vid.vidfps
         if fps != None:
@@ -236,34 +245,48 @@
         fps = round(1./(self.config.cam.shutterspeed/1000000.),2)
         self.config.img.imgfps = min(max(fps, minfps), maxfps)
 
 
     def _namefile(self):
 
         """
-        Provides a filename for the media recorded. Filenames include label,
+        Provides a filename for the media recorded. Filenames can include label,
         date, rpi name, and time. Images part of image sequence additionally
-        contain a sequence number. e.g. test_180708_pi12_S01_100410
+        can contain a sequence number. e.g. test_180708_pi12_S01_100410. Filename
+        is constructed from provided nameparams 1-5.
         """
 
-        imgtypes = ["img","imgseq"]
-        self.filetype = ".jpg" if self.config.rec.rectype in imgtypes else ".h264"
+        self.filetype = ".jpg" if self.config.rec.rectype in ["img","imgseq"] else ".h264"
+        nparlist = [self.config.cus.nameparam1,self.config.cus.nameparam2,self.config.cus.nameparam3,
+                    self.config.cus.nameparam4,self.config.cus.nameparam5]
+
+        if "label" in nparlist:
+            nparlist[nparlist.index("label")] = self.config.rec.label
+        if "date" in nparlist:
+            nparlist[nparlist.index("date")] = strftime("%y%m%d")
+        if "time" in nparlist:
+            nparlist[nparlist.index("time")] = "{timestamp:%H%M%S}"
+        if "datetime" in nparlist:
+            nparlist[nparlist.index("datetime")] = strftime("%y%m%d")+"{timestamp:%H%M%S}"
+        if "rpi" in nparlist:
+            nparlist[nparlist.index("rpi")] = self.host
+        if "counter" in nparlist:
+            if self.config.rec.rectype == "imgseq":
+                counter = "im{counter:05d}" if self.config.img.imgnr>999 else "im{counter:03d}"
+                nparlist[nparlist.index("counter")] = counter
+            else:
+                nparlist[nparlist.index("counter")] = ""
+        if "" in nparlist:
+            inds = [i for (i,it) in enumerate(nparlist) if it==""]
+            nparlist = [i for j, i in enumerate(nparlist) if j not in inds]
 
-        if self.config.rec.rectype == "imgseq":
-            date = strftime("%y%m%d")
-            counter = "im{counter:05d}" if self.config.img.imgnr>999 else "im{counter:03d}"
-            time = "{timestamp:%H%M%S}"
-            self.filename = "_".join([self.config.rec.label,date,self.host,counter,time])
-            self.filename = self.filename+self.filetype
-        else:
-            date = strftime("%y%m%d")
-            self.filename = "_".join([self.config.rec.label, date, self.host])+"_"
+        self.filename = "_".join(nparlist)+self.filetype
 
         if self.config.rec.subdirs:
-            subdir = name("_".join([self.config.rec.label,date,self.host]))
+            subdir = name("_".join([self.config.rec.label, strftime("%y%m%d"), self.host]))
             os.makedirs(subdir, exist_ok=True)
             self.filename = subdir+"/"+self.filename
 
 
     def autoconfig(self):
 
         """
@@ -286,21 +309,23 @@
             lineprint("White balance gains set to "+str(self.config.cus.gains))
 
         stream.close()
         self.rawCapture.close()
         self.cam.close()
 
 
-    def settings(self, **kwargs):
+    def settings(self, overwrite = True, **kwargs):
 
         """
         Configure the camera and recording settings
 
         Parameters
         ---------------
+        overwrite : bool, default = True
+            If settings should be overwritten
         recdir : str, default = "pirecorder/recordings"
             The directory where media will be stored. Default is "recordings".
             If different, a folder with name corresponding to location will be
             created inside the home directory. If no name is provided (""), the
             files are stored in the home directory. If "NAS" is provided it will
             additionally check if the folder links to a mounted drive.
         subdirs : bool, default = False
@@ -317,14 +342,17 @@
             and dynamically for each recording.
         maxres : str or tuple, default = "v2"
             The maximum potential resolution of the camera used. Either provide
             a tuple of the max resolution, or use "v1.3", "v1.5", "v2" (default)
             or "hq" to get the maximum resolution associated with the official
             cameras directly. Note that "v2" is the default so when an older
             camera model is connected this should be set here.
+        annotatesize : int, default = 0
+            The font size of the annotation. If a value of less than6 is provided
+            no annotation will be shown.
         rotation : int, default = 0
             Custom rotation specific to the Raspberry Pi, should be either 0 or
             180.
         brighttune : int, default = 0
             A rpi-specific brightness compensation factor to standardize light
             levels across multiple rpi"s, an integer between -10 and 10.
         roi : tuple, default = None
@@ -416,94 +444,127 @@
             The maximum duration in seconds for single videos, beyond which
             videos will be automatically split. A value of 0 indicates there is
             no maximum file duration.
         maxvidsize : int, default = 0
             The maximum file size in Megabytes for single videos, beyond which
             videos will be automatically split. A value of 0 indicates there is
             no maximum file size.
+        nameparam1-5: str, default = ("label","date","rpi","counter","time")
+            The elements of the filename to include
         """
+        overwrite = kwargs["overwrite"] if "overwrite" in kwargs else overwrite
 
-        if "recdir" in kwargs:
-            self.config.rec.recdir = kwargs["recdir"]
-        if "subdirs" in kwargs:
+        if ("recdir" in kwargs and overwrite) or ("recdir" not in str(self.config) and not overwrite):
+                self.config.rec.recdir = kwargs["recdir"]
+        if ("subdirs" in kwargs and overwrite) or ("subdirs" not in str(self.config) and not overwrite):
             self.config.rec.subdirs = kwargs["subdirs"]
-        if "label" in kwargs:
+        if ("label" in kwargs and overwrite) or ("label" not in str(self.config) and not overwrite):
             self.config.rec.label = kwargs["label"]
-        if "rectype" in kwargs:
+        if ("rectype" in kwargs and overwrite) or ("rectype" not in str(self.config) and not overwrite):
             self.config.rec.rectype = kwargs["rectype"]
-        if "maxres" in kwargs:
+        if ("maxres" in kwargs and overwrite) or ("maxres" not in str(self.config) and not overwrite):
             self.config.rec.maxres = kwargs["maxres"]
             self.config.img.imgdims = (3264,2464)
             if self.config.rec.maxres is not None:
                 if self.config.rec.maxres in ("v1.5","v1.3","v2","hq"):
                     if self.config.rec.maxres in ("v1.5","v1.3"):
                         self.config.img.imgdims = (2592,1944)
                     if self.config.rec.maxres == "v2":
                         self.config.img.imgdims = (3264,2464)
                     if self.config.rec.maxres == "hq":
                         self.config.img.imgdims = (4056,3040)
                 elif isinstance(self.config.rec.maxres, tuple):
                     self.config.img.imgdims = self.config.rec.maxres
                 else:
                     try:
-                        self.config.rec.imgdims = literal_eval(self.config.rec.maxres)
+                        self.config.zrec.imgdims = literal_eval(self.config.rec.maxres)
                     except:
                         pass
 
-        if "rotation" in kwargs:
+        if ("annotatesize" in kwargs and overwrite) or ("annotatesize" not in str(self.config) and not overwrite):
+            self.config.cus.annotatesize = kwargs["annotatesize"]
+        if ("rotation" in kwargs and overwrite) or ("rotation" not in str(self.config) and not overwrite):
             self.config.cus.rotation = kwargs["rotation"]
-        if "brighttune" in kwargs:
+        if ("brighttune" in kwargs and overwrite) or ("brighttune" not in str(self.config) and not overwrite):
             self.config.cus.brighttune = kwargs["brighttune"]
-        if "roi" in kwargs:
+        if ("roi" in kwargs and overwrite) or ("roi" not in str(self.config) and not overwrite):
             self.config.cus.roi = kwargs["roi"]
-        if "gains" in kwargs:
+        if ("gains" in kwargs and overwrite) or ("gains" not in str(self.config) and not overwrite):
             self.config.cus.gains = kwargs["gains"]
 
-        if "automode" in kwargs:
+        if ("nameparam1" in kwargs and overwrite) or ("nameparam1" not in str(self.config) and not overwrite):
+            if kwargs["nameparam1"] in self.nametypes:
+                self.config.cus.nameparam1 = kwargs["nameparam1"]
+            else:
+                lineprint("Name parameter 1 does not exist..")
+        if ("nameparam2" in kwargs and overwrite) or ("nameparam2" not in str(self.config) and not overwrite):
+            if kwargs["nameparam2"] in self.nametypes:
+                self.config.cus.nameparam2 = kwargs["nameparam2"]
+            else:
+                lineprint("Name parameter 2 does not exist..")
+        if ("nameparam3" in kwargs and overwrite) or ("nameparam3" not in str(self.config) and not overwrite):
+            if kwargs["nameparam3"] in self.nametypes:
+                self.config.cus.nameparam3 = kwargs["nameparam3"]
+            else:
+                lineprint("Name parameter 3 does not exist..")
+        if ("nameparam4" in kwargs and overwrite) or ("nameparam4" not in str(self.config) and not overwrite):
+            if kwargs["nameparam4"] in self.nametypes:
+                self.config.cus.nameparam4 = kwargs["nameparam4"]
+            else:
+                lineprint("Name parameter 4 does not exist..")
+        if ("nameparam5" in kwargs and overwrite) or ("nameparam5" not in str(self.config) and not overwrite):
+            if kwargs["nameparam5"] in self.nametypes:
+                self.config.cus.nameparam5 = kwargs["nameparam5"]
+            else:
+                lineprint("Name parameter 5 does not exist..")
+
+        if ("automode" in kwargs and overwrite) or ("automode" not in str(self.config) and not overwrite):
             self.config.cam.automode = kwargs["automode"]
-        if "brightness" in kwargs:
+        if ("brightness" in kwargs and overwrite) or ("brightness" not in str(self.config) and not overwrite):
             self.config.cam.brightness = kwargs["brightness"]
-        if "contrast" in kwargs:
+        if ("contrast" in kwargs and overwrite) or ("contrast" not in str(self.config) and not overwrite):
             self.config.cam.contrast = kwargs["contrast"]
-        if "saturation" in kwargs:
+        if ("saturation" in kwargs and overwrite) or ("saturation" not in str(self.config) and not overwrite):
             self.config.cam.saturation = kwargs["saturation"]
-        if "iso" in kwargs:
+        if ("iso" in kwargs and overwrite) or ("iso" not in str(self.config) and not overwrite):
             self.config.cam.iso = kwargs["iso"]
-        if "sharpness" in kwargs:
+        if ("sharpness" in kwargs and overwrite) or ("sharpness" not in str(self.config) and not overwrite):
             self.config.cam.sharpness = kwargs["sharpness"]
-        if "compensation" in kwargs:
+        if ("compensation" in kwargs and overwrite) or ("compensation" not in str(self.config) and not overwrite):
             self.config.cam.compensation = kwargs["compensation"]
-        if "shutterspeed" in kwargs:
+        if ("shutterspeed" in kwargs and overwrite) or ("shutterspeed" not in str(self.config) and not overwrite):
             self.config.cam.shutterspeed = kwargs["shutterspeed"]
 
-        if "imgdims" in kwargs:
+        if ("imgdims" in kwargs and overwrite) or ("imgdims" not in str(self.config) and not overwrite):
             self.config.img.imgdims = kwargs["imgdims"]
-        if "viddims" in kwargs:
+        if ("viddims" in kwargs and overwrite) or ("viddims" not in str(self.config) and not overwrite):
             self.config.vid.viddims = kwargs["viddims"]
-        if "imgfps" in kwargs:
+        if ("imgfps" in kwargs and overwrite) or ("imgfps" not in str(self.config) and not overwrite):
             self.config.img.imgfps = kwargs["imgfps"]
-        if "vidfps" in kwargs:
+        if ("vidfps" in kwargs and overwrite) or ("vidfps" not in str(self.config) and not overwrite):
             self.config.vid.vidfps = kwargs["vidfps"]
 
-        if "imgwait" in kwargs:
+        if ("imgwait" in kwargs and overwrite) or ("imgwait" not in str(self.config) and not overwrite):
             self.config.img.imgwait = kwargs["imgwait"]
-        if "imgnr" in kwargs:
+        if ("imgnr" in kwargs and overwrite) or ("imgnr" not in str(self.config) and not overwrite):
             self.config.img.imgnr = kwargs["imgnr"]
-        if "imgtime" in kwargs:
+        if ("imgtime" in kwargs and overwrite) or ("imgtime" not in str(self.config) and not overwrite):
             self.config.img.imgtime = kwargs["imgtime"]
-        if "imgquality" in kwargs:
+        if ("imgquality" in kwargs and overwrite) or ("imgquality" not in str(self.config) and not overwrite):
             self.config.img.imgquality = kwargs["imgquality"]
 
-        if "vidduration" in kwargs:
+        if ("vidduration" in kwargs and overwrite) or ("vidduration" not in str(self.config) and not overwrite):
             self.config.vid.vidduration = kwargs["vidduration"]
-        if "viddelay" in kwargs:
+        if ("viddelay" in kwargs and overwrite) or ("viddelay" not in str(self.config) and not overwrite):
             self.config.vid.viddelay = kwargs["viddelay"]
-        if "maxviddur" in kwargs:
+        if ("vidquality" in kwargs and overwrite) or ("vidquality" not in str(self.config) and not overwrite):
+            self.config.vid.vidquality = kwargs["vidquality"]
+        if ("maxviddur" in kwargs and overwrite) or ("maxviddur" not in str(self.config) and not overwrite):
             self.config.vid.maxviddur = kwargs["maxviddur"]
-        if "maxvidsize" in kwargs:
+        if ("maxvidsize" in kwargs and overwrite) or ("maxvidsize" not in str(self.config) and not overwrite):
             self.config.vid.maxvidsize = kwargs["maxvidsize"]
 
         brightchange = False
         if os.path.exists(self.brightfile):
             with open(self.brightfile) as f:
                 brighttune = yaml.load(f, Loader=yaml.FullLoader)
                 if brighttune != self.config.cus.brighttune:
@@ -607,88 +668,103 @@
                      configfile = self.configfilerel)
 
 
     def record(self):
 
         """
         Starts a recording as configured and returns either one or multiple
-        .h264 or .jpg files that are named automatically according to the label,
-        the host name, date, time and potentially session number or count nr.
-
-        Example output files:
-        rectype = "img" : test_180312_pi13_101300.jpg
-        rectype = "vid" : test_180312_pi13_102352.h264
-        rectype = "imgseq" : test_180312_pi13_img00231_101750.jpg
-        rectype = "vidseq" : test_180312_pi13_101810_S01.h264
+        .h264 or .jpg files that are named automatically
         """
 
         self._setup_cam()
         self._namefile()
         startdate = datetime.now()
 
         if self.config.rec.rectype == "img":
 
-            self.filename = self.filename + strftime("%H%M%S") + self.filetype
-            self.cam.capture(self.filename, format="jpeg", resize = self.resize,
+            if "{timestamp:%H%M%S}" in self.filename:
+                filename = self.filename.replace("{timestamp:%H%M%S}",strftime("%H%M%S"))
+            if self.config.cus.annotatesize>5:
+                self.cam.annotate_text = filename.replace(".jpg","").split("/",1)[1]
+            self.cam.capture(filename, format="jpeg", resize = self.resize,
                              quality = self.config.img.imgquality)
-            lineprint("Captured "+self.filename)
+            lineprint("Captured "+filename)
 
         elif self.config.rec.rectype == "imgseq":
 
             starttime = datetime.now()
             timepoint = starttime
+            if self.config.cus.annotatesize>5:
+                if "{timestamp:%H%M%S}" in self.filename:
+                    filename = self.filename.replace("{timestamp:%H%M%S}",strftime("%H%M%S"))
+                    filename = filename.replace("{counter:03d}","001").split("/",1)[::-1][0]
+                self.cam.annotate_text = filename.replace(".jpg","")
+            counter= 1
             for i, img in enumerate(self.cam.capture_continuous(self.filename,
                                     format="jpeg", resize = self.resize,
                                     quality = self.config.img.imgquality)):
+                counter += 1
                 if startdate.day < datetime.now().day:
-                    self.cam.close
+                    self.cam.close()
                     self.record()
                 tottimepassed = (datetime.now() - starttime).total_seconds()
                 if i < self.config.img.imgnr-1 and tottimepassed < self.config.img.imgtime:
                     timepassed = (datetime.now() - timepoint).total_seconds()
                     delay = max(0, self.config.img.imgwait - timepassed)
                     lineprint("Captured "+img+", sleeping "+str(round(delay,2))+"s..")
                     sleep(delay)
                     timepoint = datetime.now()
+                    if self.config.cus.annotatesize>5:
+                        if "{timestamp:%H%M%S}" in self.filename:
+                            filename = self.filename.replace("{timestamp:%H%M%S}",strftime("%H%M%S"))
+                            filename = filename.replace("{counter:03d}","{:03d}".format(counter)).split("/",1)[::-1][0]
+                            self.cam.annotate_text = filename.split("/",1)[::-1][0].replace(".jpg","")
                 else:
                     lineprint("Captured "+img)
                     break
 
         elif self.config.rec.rectype in ["vid","vidseq"]:
 
             # Temporary fix for flicker at start of (first) video
             self.cam.start_recording(BytesIO(), format = "h264",
                                      resize = self.resize, level = "4.2")
             self.cam.wait_recording(2)
             self.cam.stop_recording()
 
             for session in ["_S%02d" % i for i in range(1,999)]:
+                if "{timestamp:%H%M%S}" in self.filename:
+                    filename = self.filename.replace("{timestamp:%H%M%S}",strftime("%H%M%S"))
                 session = "" if self.config.rec.rectype == "vid" else session
-                filename = self.filename+strftime("%H%M%S")+session
+                filename = filename.replace(".h264",session)
                 timeremaining = self.config.vid.vidduration+self.config.vid.viddelay
                 counter = 0
                 while timeremaining > 0:
                     counter += 1
                     waittime = timeremaining
                     if self.config.vid.maxviddur > 0:
                         waittime = min(timeremaining, self.config.vid.maxviddur)
                     if waittime == timeremaining and self.config.vid.maxvidsize == 0:
                         nr = ""
                     else:
                         nr = "_v"+str(counter).zfill(2)
                     finalname = filename+nr+self.filetype
                     video = VidOutput(finalname)
+                    if self.config.cus.annotatesize>5:
+                        self.cam.annotate_text = finalname.replace(".h264","").split("/",1)[::-1][0]
                     self.cam.start_recording(video, resize = self.resize,
                                              quality = self.config.vid.vidquality,
                                              level = "4.2",
                                              format = self.filetype[1:])
                     lineprint("Start recording "+filename)
                     rectime = 0
                     while video.size < self.maxvidsize*1000000 and rectime < waittime:
                         rectime += 0.1
+                        if self.config.cus.annotatesize>5:
+                            filename = self.filename.replace("{timestamp:%H%M%S}",strftime("%H%M%S"))
+                            self.cam.annotate_text = filename.replace(".h264","").split("/",1)[::-1][0]
                         self.cam.wait_recording(0.1)
                     timeremaining -= rectime
                     self.cam.stop_recording()
                     vidinfo = " ("+str(round(rectime))+"s; "+str(round(video.size/1000000,2))+"MB)"
                     lineprint("Finished recording "+finalname+vidinfo)
                 if self.config.rec.rectype == "vid":
                     break
```

### Comparing `pirecorder-3.4.0/pirecorder/schedule.py` & `pirecorder-3.5.0/pirecorder/schedule.py`

 * *Files identical despite different names*

### Comparing `pirecorder-3.4.0/pirecorder/stream.py` & `pirecorder-3.5.0/pirecorder/stream.py`

 * *Files identical despite different names*

### Comparing `pirecorder-3.4.0/pirecorder/videoin.py` & `pirecorder-3.5.0/pirecorder/videoin.py`

 * *Files identical despite different names*

### Comparing `pirecorder-3.4.0/pirecorder.egg-info/PKG-INFO` & `pirecorder-3.5.0/pirecorder.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: pirecorder
-Version: 3.4.0
+Version: 3.5.0
 Summary: A python package for controlled and automated image and video recording with the raspberry pi
 Home-page: https://github.com/jollejolles
 Author: Jolle Jolles
 Author-email: j.w.jolles@gmail.com
 Maintainer: Jolle Jolles
 Maintainer-email: j.w.jolles@gmail.com
 License: License :: OSI Approved :: Apache Software License
-Download-URL: https://github.com/jollejolles/pirecorder/archive/v3.4.0.tar.gz
+Download-URL: https://github.com/jollejolles/pirecorder/archive/v3.5.0.tar.gz
 Description: [![Downloads](https://pepy.tech/badge/pirecorder)](https://pepy.tech/project/pirecorder)
         
         # pirecorder
         **A Python package for controlled and automated image and video recording with the raspberry pi**
         
         *pirecorder* is a Python package, built on the [picamera](http://picamera.readthedocs.io/) and [OpenCV](https://opencv.org/) libraries, that provides a flexible solution for the collection of consistent image and video data with the raspberry pi. It was developed to overcome the need for a complete solution to help researchers, especially those with limited coding skills, to easily set up and configure their raspberry pi to run large numbers of controlled and automated image and video recordings using optimal settings.
```

#### html2text {}

```diff
@@ -1,14 +1,14 @@
-Metadata-Version: 2.1 Name: pirecorder Version: 3.4.0 Summary: A python package
+Metadata-Version: 2.1 Name: pirecorder Version: 3.5.0 Summary: A python package
 for controlled and automated image and video recording with the raspberry pi
 Home-page: https://github.com/jollejolles Author: Jolle Jolles Author-email:
 j.w.jolles@gmail.com Maintainer: Jolle Jolles Maintainer-email:
 j.w.jolles@gmail.com License: License :: OSI Approved :: Apache Software
 License Download-URL: https://github.com/jollejolles/pirecorder/archive/
-v3.4.0.tar.gz Description: [![Downloads](https://pepy.tech/badge/pirecorder)]
+v3.5.0.tar.gz Description: [![Downloads](https://pepy.tech/badge/pirecorder)]
 (https://pepy.tech/project/pirecorder) # pirecorder **A Python package for
 controlled and automated image and video recording with the raspberry pi**
 *pirecorder* is a Python package, built on the [picamera](http://
 picamera.readthedocs.io/) and [OpenCV](https://opencv.org/) libraries, that
 provides a flexible solution for the collection of consistent image and video
 data with the raspberry pi. It was developed to overcome the need for a
 complete solution to help researchers, especially those with limited coding
```

### Comparing `pirecorder-3.4.0/setup.py` & `pirecorder-3.5.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 DESCRIPTION="""A python package for controlled and automated image and video \
 recording with the raspberry pi"""
 
 DISTNAME="pirecorder"
 MAINTAINER="Jolle Jolles"
 MAINTAINER_EMAIL="j.w.jolles@gmail.com"
 URL="https://github.com/jollejolles"
-DOWNLOAD_URL="https://github.com/jollejolles/pirecorder/archive/v3.4.0.tar.gz"
+DOWNLOAD_URL="https://github.com/jollejolles/pirecorder/archive/v3.5.0.tar.gz"
 
 with open("README.md") as f:
     readme = f.read()
 
 if __name__ == "__main__":
 
     setup(name=DISTNAME,
```

