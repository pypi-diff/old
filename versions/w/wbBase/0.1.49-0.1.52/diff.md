# Comparing `tmp/wbBase-0.1.49.tar.gz` & `tmp/wbBase-0.1.52.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wbBase-0.1.49.tar", last modified: Fri Mar 31 15:15:32 2023, max compression
+gzip compressed data, was "wbBase-0.1.52.tar", last modified: Fri Apr  7 14:44:05 2023, max compression
```

## Comparing `wbBase-0.1.49.tar` & `wbBase-0.1.52.tar`

### file list

```diff
@@ -1,42 +1,43 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 15:15:32.295986 wbBase-0.1.49/
--rw-rw-rw-   0 root         (0) root         (0)     1079 2023-03-31 15:15:30.000000 wbBase-0.1.49/LICENSE
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 15:15:32.283985 wbBase-0.1.49/Lib/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 15:15:32.288986 wbBase-0.1.49/Lib/wbBase/
--rw-rw-rw-   0 root         (0) root         (0)      153 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    24145 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/application.py
--rw-rw-rw-   0 root         (0) root         (0)     2165 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/applicationInfo.py
--rw-rw-rw-   0 root         (0) root         (0)    20585 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/applicationWindow.py
--rw-rw-rw-   0 root         (0) root         (0)   309800 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/artprovider.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 15:15:32.292986 wbBase-0.1.49/Lib/wbBase/control/
--rw-rw-rw-   0 root         (0) root         (0)     1016 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/control/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4414 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/control/externalToolConfig.py
--rw-rw-rw-   0 root         (0) root         (0)     5891 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/control/externalToolConfigUI.py
--rw-rw-rw-   0 root         (0) root         (0)     2646 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/control/filling.py
--rw-rw-rw-   0 root         (0) root         (0)     1670 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/control/iePanel.py
--rw-rw-rw-   0 root         (0) root         (0)     8569 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/control/propgrid.py
--rw-rw-rw-   0 root         (0) root         (0)    46594 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/control/textEditControl.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 15:15:32.293986 wbBase-0.1.49/Lib/wbBase/dialog/
--rw-rw-rw-   0 root         (0) root         (0)       68 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/dialog/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2342 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/dialog/multiSaveModifiedDialog.py
--rw-rw-rw-   0 root         (0) root         (0)     3293 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/dialog/multiSaveModifiedDialogUI.py
--rw-rw-rw-   0 root         (0) root         (0)    20598 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/dialog/preferences.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 15:15:32.295986 wbBase-0.1.49/Lib/wbBase/document/
--rw-rw-rw-   0 root         (0) root         (0)    23492 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/document/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    37008 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/document/manager.py
--rw-rw-rw-   0 root         (0) root         (0)     4743 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/document/notebook.py
--rw-rw-rw-   0 root         (0) root         (0)     8052 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/document/template.py
--rw-rw-rw-   0 root         (0) root         (0)     9208 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/document/view.py
--rw-rw-rw-   0 root         (0) root         (0)    21397 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/panelManager.py
--rw-rw-rw-   0 root         (0) root         (0)     2942 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/pluginManager.py
--rw-rw-rw-   0 root         (0) root         (0)     8129 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/scripting.py
--rw-rw-rw-   0 root         (0) root         (0)      922 2023-03-31 15:15:30.000000 wbBase-0.1.49/Lib/wbBase/tools.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 15:15:32.290986 wbBase-0.1.49/Lib/wbBase.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1395 2023-03-31 15:15:32.000000 wbBase-0.1.49/Lib/wbBase.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      995 2023-03-31 15:15:32.000000 wbBase-0.1.49/Lib/wbBase.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-31 15:15:32.000000 wbBase-0.1.49/Lib/wbBase.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       58 2023-03-31 15:15:32.000000 wbBase-0.1.49/Lib/wbBase.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        7 2023-03-31 15:15:32.000000 wbBase-0.1.49/Lib/wbBase.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     1395 2023-03-31 15:15:32.295986 wbBase-0.1.49/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)      301 2023-03-31 15:15:30.000000 wbBase-0.1.49/README.md
--rw-rw-rw-   0 root         (0) root         (0)     1659 2023-03-31 15:15:32.296986 wbBase-0.1.49/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)       39 2023-03-31 15:15:30.000000 wbBase-0.1.49/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:44:05.171622 wbBase-0.1.52/
+-rw-rw-rw-   0 root         (0) root         (0)     1079 2023-04-07 14:44:03.000000 wbBase-0.1.52/LICENSE
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:44:05.158621 wbBase-0.1.52/Lib/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:44:05.164621 wbBase-0.1.52/Lib/wbBase/
+-rw-rw-rw-   0 root         (0) root         (0)      153 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    23824 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/application.py
+-rw-rw-rw-   0 root         (0) root         (0)     2165 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/applicationInfo.py
+-rw-rw-rw-   0 root         (0) root         (0)    20585 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/applicationWindow.py
+-rw-rw-rw-   0 root         (0) root         (0)   309800 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/artprovider.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:44:05.168622 wbBase-0.1.52/Lib/wbBase/control/
+-rw-rw-rw-   0 root         (0) root         (0)     1118 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/control/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4414 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/control/externalToolConfig.py
+-rw-rw-rw-   0 root         (0) root         (0)     5891 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/control/externalToolConfigUI.py
+-rw-rw-rw-   0 root         (0) root         (0)     2666 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/control/filling.py
+-rw-rw-rw-   0 root         (0) root         (0)     1670 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/control/iePanel.py
+-rw-rw-rw-   0 root         (0) root         (0)     8569 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/control/propgrid.py
+-rw-rw-rw-   0 root         (0) root         (0)    47311 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/control/textEditControl.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:44:05.169622 wbBase-0.1.52/Lib/wbBase/dialog/
+-rw-rw-rw-   0 root         (0) root         (0)       68 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/dialog/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2342 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/dialog/multiSaveModifiedDialog.py
+-rw-rw-rw-   0 root         (0) root         (0)     3293 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/dialog/multiSaveModifiedDialogUI.py
+-rw-rw-rw-   0 root         (0) root         (0)    20381 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/dialog/preferences.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:44:05.171622 wbBase-0.1.52/Lib/wbBase/document/
+-rw-rw-rw-   0 root         (0) root         (0)    23492 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/document/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    36999 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/document/manager.py
+-rw-rw-rw-   0 root         (0) root         (0)     4743 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/document/notebook.py
+-rw-rw-rw-   0 root         (0) root         (0)     8016 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/document/template.py
+-rw-rw-rw-   0 root         (0) root         (0)     9208 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/document/view.py
+-rw-rw-rw-   0 root         (0) root         (0)    21455 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/panelManager.py
+-rw-rw-rw-   0 root         (0) root         (0)     1773 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/pluginManager.py
+-rw-rw-rw-   0 root         (0) root         (0)     2942 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/pluginManager_old.py
+-rw-rw-rw-   0 root         (0) root         (0)     8136 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/scripting.py
+-rw-rw-rw-   0 root         (0) root         (0)      922 2023-04-07 14:44:03.000000 wbBase-0.1.52/Lib/wbBase/tools.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:44:05.165622 wbBase-0.1.52/Lib/wbBase.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2382 2023-04-07 14:44:05.000000 wbBase-0.1.52/Lib/wbBase.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1027 2023-04-07 14:44:05.000000 wbBase-0.1.52/Lib/wbBase.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 14:44:05.000000 wbBase-0.1.52/Lib/wbBase.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      105 2023-04-07 14:44:05.000000 wbBase-0.1.52/Lib/wbBase.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        7 2023-04-07 14:44:05.000000 wbBase-0.1.52/Lib/wbBase.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     2382 2023-04-07 14:44:05.171622 wbBase-0.1.52/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     1098 2023-04-07 14:44:03.000000 wbBase-0.1.52/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     1941 2023-04-07 14:44:05.172622 wbBase-0.1.52/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)       39 2023-04-07 14:44:03.000000 wbBase-0.1.52/setup.py
```

### Comparing `wbBase-0.1.49/LICENSE` & `wbBase-0.1.52/LICENSE`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/application.py` & `wbBase-0.1.52/Lib/wbBase/application.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,15 +14,14 @@
 from typing import TYPE_CHECKING, ClassVar, List, Optional, Union
 
 import wx
 from appdirs import AppDirs
 from wx.adv import (
     SPLASH_CENTER_ON_SCREEN,
     SPLASH_NO_TIMEOUT,
-    AboutDialogInfo,
     SplashScreen,
 )
 
 from .applicationInfo import ApplicationInfo
 from .applicationWindow import ApplicationWindow
 from .artprovider import Artprovider
 from .document import DOC_SILENT
@@ -147,52 +146,46 @@
     config: wx.ConfigBase
     instanceChecker: wx.SingleInstanceChecker
 
     _post_init_queue: List[FunctionType] = []
 
     def __init__(
         self,
-        pluginDir: Optional[str] = None,
-        redirect: bool = False,
         debug: int = 1,
-        iconName: str = "",
-        test=False,
+        iconName: str = wx.ART_EXECUTABLE_FILE,
+        test:bool=False,
+        info:Optional[ApplicationInfo]= None
     ):
         """
         Constructor
         """
         self._debug: int = debug
         self.iconName: str = iconName
         self._test = test
         self._splashScreen: Optional[AppSplashScreen] = None
-        self.info:ApplicationInfo = self._getAppInfo()
+        self.info:ApplicationInfo = self._getAppInfo(info)
         self.cmdLineArguments: Namespace = self._getCmdLineArguments()
         self._extChangeMode: int = self.EXT_CHANGE_TEST_ON_REQUEST
         self.extChangeTimerInterval: int = 60
-        self.folder: str = os.path.dirname(sys.argv[0])
         self.sharedDataDir: str = ""
         self.privateDataDir: str = ""
         self.globalObjects: List[str] = []
         self.dirs = AppDirs(self.info.AppName, self.info.VendorName)
-        if self.folder not in sys.path:
-            sys.path.insert(0, self.folder)
-        if pluginDir and os.path.isdir(pluginDir):
-            self.pluginDir = pluginDir
-        else:
-            self.pluginDir = os.path.join(self.folder, "plugin")
-        wx.App.__init__(self, redirect, useBestVisual=True)
+        wx.App.__init__(self, redirect=False, useBestVisual=True)
 
     def __repr__(self) -> str:
         return '<Application: "%s" by %s>' % (self.AppName, self.VendorName)
 
     # =========================================================================
     # Private methods
     # =========================================================================
 
-    def _getAppInfo(self) -> ApplicationInfo:
+    def _getAppInfo(self, info:Optional[ApplicationInfo]= None) -> ApplicationInfo:
+        if isinstance(info, ApplicationInfo):
+            return info
         if not self.test:
             appInfoString = self.getResource("application.yml")
             if isinstance(appInfoString, str):
                 return ApplicationInfo.fromString(appInfoString)
         return ApplicationInfo()
 
     def _getCmdLineArguments(self) -> Namespace:
@@ -294,24 +287,24 @@
                     x = round(cfg.ReadInt("x", -1) + (width - bmp.Width) / 2)
                     y = round(cfg.ReadInt("y", -1) + (height - bmp.Height) / 2)
                     pos = wx.Point(x, y)
                     # size = wx.Size(cfg.ReadInt("width", -1), cfg.ReadInt("height", -1))
                     splashScreen = AppSplashScreen(
                         bitmap=bmp,
                         splashStyle=SPLASH_NO_TIMEOUT,
-                        milliseconds=60000,
+                        milliseconds=1000,
                         parent=None,
                         id=wx.ID_ANY,
                         pos=pos,
                         size=wx.DefaultSize,
                     )
                     splashScreen.SetPosition(pos)
                     return splashScreen
         return AppSplashScreen(
-            bmp, SPLASH_CENTER_ON_SCREEN | SPLASH_NO_TIMEOUT, 60000, None
+            bmp, SPLASH_CENTER_ON_SCREEN | SPLASH_NO_TIMEOUT, 1000, None
         )
 
     # =========================================================================
     # Public methods
     # =========================================================================
 
     def OnPreInit(self) -> None:
@@ -332,24 +325,24 @@
             self.config = self.Traits.CreateConfig()
         self.instanceChecker = wx.SingleInstanceChecker(
             f"{self.AppName}-{wx.GetUserId()}"
         )
         wx.ArtProvider.Push(Artprovider())
         self.extChangeTimer = ExtChangeTestTimer()
         self.listenAndLoadTimer = ListenAndLoadTimer()
-        if hasattr(sys, "frozen") and sys.frozen:
+        if self.test or (hasattr(sys, "frozen") and sys.frozen):
             self.SetAssertMode(wx.APP_ASSERT_SUPPRESS)
 
     def OnInit(self) -> bool:
         self.prepareSingleInstanceConfig()
         self._splashScreen = self._showSplashScreen()
         self._pluginManager: PluginManager = self.pluginManagerClass()
-        self.SetTopWindow(self.topWindowClass(self.iconName))
         self.prepareSharedDataFolder()
         self.preparePrivateDataFolder()
+        self.SetTopWindow(self.topWindowClass(self.iconName))
         self.RunPostInitQueue()
         self._initExtChangesTest()
         return True
 
     def OnRun(self) -> int:
         """
         Run the application
@@ -374,15 +367,15 @@
 
         :return: Return code
         """
         return self.OnRun()
 
     def splashMessage(self, text: str) -> None:
         """
-        Show progress message on splash screen during initialisation
+        Show progress message on splash screen during initialization
         of the application.
 
         :param text: The message
         """
         if self._splashScreen:
             self._splashScreen.setMessage(text)
 
@@ -492,61 +485,64 @@
 
     def prepareSingleInstanceConfig(self) -> None:
         if self.test:
             return
         self.allowMultipleInstances = self.config.ReadBool(
             "/Application/Start/MultipleInstances", False
         )
-        if not self.allowMultipleInstances:
-            # create shared memory temporary file
-            if wx.Platform == "__WXMSW__":
-                tfile = tempfile.TemporaryFile(prefix="ag", suffix="tmp")
-                fno = tfile.fileno()
-                self._sharedMemory = mmap.mmap(fno, 1024, "shared_memory")
-            else:
-                tfile = open(
-                    os.path.join(
-                        tempfile.gettempdir(),
-                        tempfile.gettempprefix()
-                        + self.GetAppName()
-                        + "-"
-                        + wx.GetUserId()
-                        + "AGSharedMemory",
-                    ),
-                    "w+b",
-                )
-                tfile.write(b"*")  # available buffer
-                tfile.seek(1024)
-                tfile.write(b" ")
-                tfile.flush()
-                fno = tfile.fileno()
-                self._sharedMemory = mmap.mmap(fno, 1024)
-            if self.instanceChecker.IsAnotherRunning():
-                if self.cmdLineArguments.document:
-                    data = pickle.dumps(self.cmdLineArguments.document)
-                    sharedMemory = self._sharedMemory
-                    while True:
+        if self.allowMultipleInstances:
+            return
+        # create shared memory temporary file
+        if wx.Platform == "__WXMSW__":
+            tfile = tempfile.TemporaryFile(prefix="ag", suffix="tmp")
+            fno = tfile.fileno()
+            self._sharedMemory = mmap.mmap(fno, 1024, "shared_memory")
+        else:
+            tfile = open(
+                os.path.join(
+                    tempfile.gettempdir(),
+                    tempfile.gettempprefix()
+                    + self.GetAppName()
+                    + "-"
+                    + wx.GetUserId()
+                    + "AGSharedMemory",
+                ),
+                "w+b",
+            )
+            tfile.write(b"*")  # available buffer
+            tfile.seek(1024)
+            tfile.write(b" ")
+            tfile.flush()
+            fno = tfile.fileno()
+            self._sharedMemory = mmap.mmap(fno, 1024)
+        if self.instanceChecker.IsAnotherRunning():
+            if self.cmdLineArguments.document:
+                data = pickle.dumps(self.cmdLineArguments.document)
+                sharedMemory = self._sharedMemory
+                while True:
+                    sharedMemory.seek(0)
+                    marker = sharedMemory.read_byte()
+                    if marker == 0 or chr(marker) == "*":  # available buffer
                         sharedMemory.seek(0)
-                        marker = sharedMemory.read_byte()
-                        if marker == 0 or chr(marker) == "*":  # available buffer
-                            sharedMemory.seek(0)
-                            sharedMemory.write_byte(ord("-"))  # set writing marker
-                            sharedMemory.write(
-                                data
-                            )  # write files we tried to open to shared memory
-                            sharedMemory.seek(0)
-                            sharedMemory.write_byte(
-                                ord("+")
-                            )  # set finished writing marker
-                            sharedMemory.flush()
-                            break
-                        else:
-                            time.sleep(1)  # give enough time for buffer to be available
-            else:
-                self.listenAndLoadTimer.Start(250)
+                        # set writing marker
+                        sharedMemory.write_byte(ord("-"))  
+                        # write files we tried to open to shared memory
+                        sharedMemory.write(
+                            data
+                        )  
+                        sharedMemory.seek(0)
+                        sharedMemory.write_byte(
+                            ord("+")
+                        )  # set finished writing marker
+                        sharedMemory.flush()
+                        break
+                    else:
+                        time.sleep(1)  # give enough time for buffer to be available
+        else:
+            self.listenAndLoadTimer.Start(250)
 
     def prepareSharedDataFolder(self) -> None:
         self.splashMessage("Preparing shared data folder")
         cfg = self.config
         defaultFolder = os.path.join(self.dirs.user_data_dir, "shared")
         with wx.ConfigPathChanger(cfg, "/Application/SharedData/"):
             folder = cfg.Read("Dir", defaultFolder)
```

### Comparing `wbBase-0.1.49/Lib/wbBase/applicationInfo.py` & `wbBase-0.1.52/Lib/wbBase/applicationInfo.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/applicationWindow.py` & `wbBase-0.1.52/Lib/wbBase/applicationWindow.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/artprovider.py` & `wbBase-0.1.52/Lib/wbBase/artprovider.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/control/__init__.py` & `wbBase-0.1.52/Lib/wbBase/control/__init__.py`

 * *Files 15% similar despite different names*

```diff
@@ -10,27 +10,32 @@
 
 class PanelMixin:
     def __repr__(self) -> str:
         return f'<{self.__class__.__name__} of "{self.app.AppName}">'
 
     @property
     def app(self) -> App:
+        """
+        The running Workbench application.
+        """
         return wx.GetApp()
 
     @property
-    def plugin(self) -> Optional[ModuleType]:
-        plugins = self.app.pluginManager
-        for name in plugins:
-            plugin = plugins[name]
-            if hasattr(plugin, "panels"):
-                for cls, info in plugin.panels:
+    def plugin(self) -> str:
+        """
+        :return: Name of the plugin from which this panel was loaded
+        """
+        for name, module in self.app.pluginManager.items():
+            if hasattr(module, "panels"):
+                for cls, __ in module.panels:
                     if cls == self.__class__:
-                        return plugin
-        return None
+                        return name
+        return ""
 
     @property
     def config(self) -> Optional[wx.ConfigBase]:
-        if self.plugin:
+        plugin = self.plugin
+        if plugin:
             cfg = self.app.config
-            cfg.SetPath(f"/Plugin/{self.plugin.__name__}/")
+            cfg.SetPath(f"/Plugin/{plugin}/")
             return cfg
         return None
```

### Comparing `wbBase-0.1.49/Lib/wbBase/control/externalToolConfig.py` & `wbBase-0.1.52/Lib/wbBase/control/externalToolConfig.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/control/externalToolConfigUI.py` & `wbBase-0.1.52/Lib/wbBase/control/externalToolConfigUI.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/control/filling.py` & `wbBase-0.1.52/Lib/wbBase/control/filling.py`

 * *Files 2% similar despite different names*

```diff
@@ -35,15 +35,15 @@
             rootIsNamespace=rootIsNamespace,
             static=static,
         )
         self.text = FillingText(
             parent=self, style=wx.CLIP_CHILDREN | wx.NO_BORDER, static=static
         )
         self.text.SetMargins(2, 2)
-        self.applyConfig()
+        # self.applyConfig()
         wx.CallLater(25, self.SplitVertically, self.tree, self.text, 200)
         self.SetMinimumPaneSize(50)
 
         # Override the filling so that descriptions go to FillingText.
         self.tree.setText = self.text.SetText
 
         # Display the root item.
@@ -59,26 +59,26 @@
     # properties
     # -----------------------------------------------------------------------------
 
     @property
     def app(self):
         return wx.GetApp()
 
-    @property
-    def config(self):
-        return None
+    # @property
+    # def config(self):
+    #     return None
 
     # -----------------------------------------------------------------------------
     # public methods
     # -----------------------------------------------------------------------------
 
-    def applyConfig(self):
-        cfg = self.config
-        if cfg:
-            self.tree.SetBackgroundColour(cfg.backgroundColour.ChangeLightness(130))
-            # self.tree.SetForegroundColour(cfg.foregroundColour)
-            cfg.apply(self.text)
+    # def applyConfig(self):
+    #     cfg = self.config
+    #     if cfg:
+    #         self.tree.SetBackgroundColour(cfg.backgroundColour.ChangeLightness(130))
+    #         # self.tree.SetForegroundColour(cfg.foregroundColour)
+    #         cfg.apply(self.text)
 
     def OnChanged(self, event):
         # this is important: do not evaluate this event=> otherwise,
         # splitterwindow behaves strangely
         pass
```

### Comparing `wbBase-0.1.49/Lib/wbBase/control/iePanel.py` & `wbBase-0.1.52/Lib/wbBase/control/iePanel.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/control/propgrid.py` & `wbBase-0.1.52/Lib/wbBase/control/propgrid.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/control/textEditControl.py` & `wbBase-0.1.52/Lib/wbBase/control/textEditControl.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from __future__ import annotations
 
 import sys
 from collections import OrderedDict
-from typing import TYPE_CHECKING
+from typing import TYPE_CHECKING, Protocol
 
 import wx
 import wx.propgrid as pg
 import wx.stc as stc
 from wx.lib.gizmos.dynamicsash import EVT_DYNAMIC_SASH_SPLIT, EVT_DYNAMIC_SASH_UNIFY
 
 from .propgrid import (
@@ -14,14 +14,15 @@
     OptColourEditor,
     StyleSpecEditor,
     StyleSpecProperty,
 )
 
 if TYPE_CHECKING:
     from ..application import App
+    from ..dialog.preferences import PreferencesPageBase
 
 MARGIN_NUMBERS = 0
 MARGIN_SYMBOLS = 1
 MARGIN_FOLDMARK = 2
 
 
 class STCdropTarget(wx.DropTarget):
@@ -71,15 +72,15 @@
                 wx.CallAfter(self.app.TopWindow.documentManager.openDocuments, files)
             elif len(text) > 0:
                 self.control.DoDropText(x_cord, y_cord, text)
         self.initObjects()
         return drag_result
 
     @staticmethod
-    def ScrollBuffer(styledTextCtrl, x_cord, y_cord):
+    def ScrollBuffer(styledTextCtrl: stc.StyledTextCtrl, x_cord: int, y_cord: int):
         try:
             cline = styledTextCtrl.PositionFromPoint(wx.Point(x_cord, y_cord))
             if cline != stc.STC_INVALID_POSITION:
                 cline = styledTextCtrl.LineFromPosition(cline)
                 fline = styledTextCtrl.GetFirstVisibleLine()
                 lline = styledTextCtrl.GetLastVisibleLine()
                 if (cline - fline) < 2:
@@ -88,21 +89,58 @@
                     styledTextCtrl.ScrollLines(1)
                 else:
                     pass
         except wx.PyAssertionError as msg:
             wx.LogError("[droptargetft][err] ScrollBuffer: %s" % msg)
 
 
-class STCfoldMixin(object):
-    def __init__(self):
+class STCprotocol(Protocol):
+    def GetFoldExpanded(self, line: int) -> bool:
+        ...
+
+    def GetFoldLevel(self, line: int) -> int:
+        ...
+
+    def GetLastChild(self, line: int, level: int) -> int:
+        ...
+
+    def GetLineCount(self) -> int:
+        ...
+
+    def HideLines(self, lineStart: int, lineEnd: int) -> None:
+        ...
+
+    def MarkerDefine(
+        self,
+        markerNumber: int,
+        markerSymbol: int,
+        foreground: wx.Colour = wx.NullColour,
+        background: wx.Colour = wx.NullColour,
+    ):
+        ...
+
+    def SetFoldExpanded(self, line: int, expanded: bool) -> None:
+        ...
+
+    def SetMarginMask(self, margin: int, mask: int) -> None:
+        ...
+
+    def SetMarginType(self, margin: int, marginType: int) -> None:
+        ...
+
+    def ShowLines(self, lineStart: int, lineEnd: int) -> None:
+        ...
+
+class STCfoldMixin:
+    def __init__(self:STCprotocol):
         self.SetMarginType(MARGIN_FOLDMARK, stc.STC_MARGIN_SYMBOL)
         self.SetMarginMask(MARGIN_FOLDMARK, stc.STC_MASK_FOLDERS)
         self.Bind(stc.EVT_STC_MARGINCLICK, self.on_MARGINCLICK)
 
-    def defineFoldMarker(self, style, line, fill, highlight):
+    def defineFoldMarker(self: STCprotocol, style, line, fill, highlight):
         _line = line.GetAsString(wx.C2S_HTML_SYNTAX)
         _fill = fill.GetAsString(wx.C2S_HTML_SYNTAX)
         _highlight = highlight.GetAsString(wx.C2S_HTML_SYNTAX)
         box, circle, arrow, plusminus = range(4)
         md = self.MarkerDefine
         if style == box:
             md(stc.STC_MARKNUM_FOLDEROPEN, stc.STC_MARK_BOXMINUS, _fill, _line)
@@ -153,15 +191,15 @@
             md(stc.STC_MARKNUM_FOLDER, stc.STC_MARK_PLUS, _highlight, _highlight)
             md(stc.STC_MARKNUM_FOLDERSUB, stc.STC_MARK_EMPTY, _line, _line)
             md(stc.STC_MARKNUM_FOLDERTAIL, stc.STC_MARK_EMPTY, _line, _line)
             md(stc.STC_MARKNUM_FOLDEREND, stc.STC_MARK_EMPTY, _line, _line)
             md(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_EMPTY, _line, _line)
             md(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_EMPTY, _line, _line)
 
-    def FoldAll(self):
+    def FoldAll(self: STCprotocol):
         lineCount = self.GetLineCount()
         expanding = True
         # find out if we are folding or unfolding
         for lineNum in range(lineCount):
             if self.GetFoldLevel(lineNum) & stc.STC_FOLDLEVELHEADERFLAG:
                 expanding = not self.GetFoldExpanded(lineNum)
                 break
@@ -180,15 +218,23 @@
                     lastChild = self.GetLastChild(lineNum, -1)
                     self.SetFoldExpanded(lineNum, False)
 
                     if lastChild > lineNum:
                         self.HideLines(lineNum + 1, lastChild)
             lineNum = lineNum + 1
 
-    def Expand(self, line, doExpand, force=False, visLevels=0, level=-1):
+    def Expand(
+        self,
+        line,
+        doExpand,
+        force: bool = False,
+        visLevels: int = 0,
+        level: int = -1,
+    ) -> int: 
+        
         lastChild = self.GetLastChild(line, level)
         line = line + 1
         while line <= lastChild:
             if force:
                 if visLevels > 0:
                     self.ShowLines(line, line)
                 else:
@@ -214,15 +260,15 @@
                 line = line + 1
         return line
 
     # -----------------------------------------------------------------------------
     # Event handler
     # -----------------------------------------------------------------------------
 
-    def on_MARGINCLICK(self, evt):
+    def on_MARGINCLICK(self: STCprotocol, evt):
         # fold and unfold as needed
         # if evt.GetMargin() == MARGIN_FOLDMARK:
         # 	if evt.GetShift() and evt.GetControl():
         if evt.Margin == MARGIN_FOLDMARK:
             if evt.Shift and evt.Control:
                 self.FoldAll()
             else:
@@ -409,15 +455,15 @@
             return "\n"
 
     def GetLastVisibleLine(self) -> int:
         """Return what the last visible line is"""
         return self.GetFirstVisibleLine() + self.LinesOnScreen() - 1
 
 
-class TextEditDynSashMixin(object):
+class TextEditDynSashMixin:
     def __init__(self, dyn_sash):
         self.dyn_sash = dyn_sash
         self.Bind(EVT_DYNAMIC_SASH_SPLIT, self.on_DYNAMIC_SASH_SPLIT)
         self.Bind(EVT_DYNAMIC_SASH_UNIFY, self.on_DYNAMIC_SASH_UNIFY)
         self.setupScrollBars()
 
     def clone(self):
@@ -472,16 +518,17 @@
         name="TextEditSashChild",
     ):
         TextEditCtrl.__init__(self, parent, id, pos, size, style, name)
         TextEditDynSashMixin.__init__(self, parent)
 
 
 class TextEditConfig:
-    def __init__(self):
-        self.configPath: str = ""
+    def __init__(self, parent):
+        self.parent = parent
+        # self.configPath: str = ""
         """Set default values"""
         # default style spec
         self.STC_STYLE_DEFAULT = "fore:black,back:white,face:Consolas,size:10"
         self.STC_STYLE_CONTROLCHAR = ""
         self.STC_STYLE_BRACELIGHT = ""
         self.STC_STYLE_BRACEBAD = ""
         # Caret
@@ -524,43 +571,20 @@
         self.FoldFlags = 0
         self.FoldMarkBackground = wx.Colour("#808080")
         self.FoldMarkLine = wx.Colour("#000000")
         self.FoldMarkFill = wx.Colour("#FFFFFF")
         self.FoldMarkHighlight = wx.Colour("#FF0000")
         # Syntax
         self.syntax = OrderedDict()
+        self.load()
 
-    @property
-    def app(self) -> App:
-        return wx.GetApp()
-
-    @property
-    def plugin(self):
-        plugins = self.app.pluginManager
-        for pluginName in plugins:
-            plugin = plugins[pluginName]
-            for obj in plugin.__dict__.values():
-                if obj == self:
-                    return plugin
-        wx.LogDebug(f"plugin attribute of {self} is None")
 
     @property
-    def config(self):
-        win = self.app.TopWindow
-        if win:
-            cfg = self.app.config
-            if self.configPath:
-                cfg.SetPath(self.configPath)
-            elif self.plugin:
-                cfg.SetPath(f"/Plugin/{self.plugin.__name__}/")
-            else:
-                cfg = None
-        else:
-            cfg = None
-        return cfg
+    def config(self) -> wx.ConfigBase:
+        return self.parent.config
 
     @property
     def backgroundColour(self):
         back = "#FFFFFF"
         for stylePart in self.STC_STYLE_DEFAULT.split(","):
             key, value = stylePart.split(":")
             if key == "back":
@@ -787,15 +811,15 @@
             for name in self.syntax:
                 cfg.Write(name, self.syntax[name])
         else:
             wx.LogDebug(f"no config for {self}")
 
     def apply(self, textEditCtrl):
         """Apply values to TextEditCtrl"""
-        ctrl = textEditCtrl
+        ctrl: TextEditCtrl = textEditCtrl
         # default style spec
         ctrl.StyleSetSpec(stc.STC_STYLE_DEFAULT, self.STC_STYLE_DEFAULT)
         ctrl.StyleClearAll()
         ctrl.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, self.STC_STYLE_CONTROLCHAR)
         ctrl.StyleSetSpec(stc.STC_STYLE_BRACELIGHT, self.STC_STYLE_BRACELIGHT)
         ctrl.StyleSetSpec(stc.STC_STYLE_BRACEBAD, self.STC_STYLE_BRACEBAD)
         ctrl.StyleSetSpec(stc.STC_STYLE_INDENTGUIDE, self.STC_STYLE_INDENTGUIDE)
@@ -849,21 +873,21 @@
             ctrl.SetMarginSensitive(MARGIN_FOLDMARK, False)
         # Syntax colouring
         # print('Syntax colouring')
         for name in self.syntax:
             # print(' ', name, self.syntax[name])
             ctrl.StyleSetSpec(getattr(stc, name), self.syntax[name])
 
-    def registerPropertyEditors(self, page):
+    def registerPropertyEditors(self, page: PreferencesPageBase):
         if not page.GetEditorByName("OptColourEditor"):
             page.RegisterEditor(OptColourEditor, "OptColourEditor")
         if not page.GetEditorByName("StyleSpecEditor"):
             page.RegisterEditor(StyleSpecEditor, "StyleSpecEditor")
 
-    def appendProperties_main(self, page):
+    def appendProperties_main(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Main"))
         page.Append(FontfacenameMonoProperty("Font", "font", self.fontFacename))
         page.Append(pg.IntProperty("Font Size", "size", self.fontSize))
         page.Append(
             pg.ColourProperty("Foreground Colour", "foreground", self.foregroundColour)
         )
         page.Append(
@@ -881,15 +905,15 @@
         )
         page.Append(
             StyleSpecProperty(
                 "Brace mismatch", "STC_STYLE_BRACEBAD", self.STC_STYLE_BRACEBAD
             )
         )
 
-    def appendProperties_caret(self, page):
+    def appendProperties_caret(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Caret"))
         page.Append(pg.IntProperty("Caret Width", "CaretWidth", self.CaretWidth))
         page.Append(
             pg.ColourProperty("Caret Colour", "CaretForeground", self.CaretForeground)
         )
         page.Append(
             pg.BoolProperty(
@@ -903,15 +927,15 @@
         )
         page.Append(
             pg.IntProperty(
                 "Caret Line Alpha", "CaretLineBackAlpha", self.CaretLineBackAlpha
             )
         )
 
-    def appendProperties_selection(self, page):
+    def appendProperties_selection(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Selection"))
         page.Append(
             pg.BoolProperty(
                 "Use Selection Foreground", "UseSelForeground", self.UseSelForeground
             )
         )
         page.Append(
@@ -932,15 +956,15 @@
         page.Append(
             pg.IntProperty("Selection Alpha", "SelectionAlpha", self.SelectionAlpha)
         )
         page.Append(
             pg.BoolProperty("Selection EOL Filled", "SelEOLFilled", self.SelEOLFilled)
         )
 
-    def appendProperties_indentation(self, page):
+    def appendProperties_indentation(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Indentation and White Space"))
         page.Append(pg.IntProperty("Indetation Size", "Indent", self.Indent))
         page.Append(pg.IntProperty("Tab Size", "TabWidth", self.TabWidth))
         page.Append(pg.BoolProperty("Use Tabs for Indetation", "UseTabs", self.UseTabs))
         page.Append(pg.BoolProperty("Tab Indents", "TabIndents", self.TabIndents))
         page.Append(
             pg.BoolProperty(
@@ -967,28 +991,28 @@
                     stc.STC_WS_VISIBLEALWAYS,
                     stc.STC_WS_VISIBLEAFTERINDENT,
                 ),
                 self.ShowWhiteSpace,
             )
         )
 
-    def appendProperties_line_ending(self, page):
+    def appendProperties_line_ending(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Line Endings"))
         page.Append(
             pg.EnumProperty(
                 "End of Line Mode",
                 "EOLMode",
                 ("DOS/Windows [CR+LF]", "Unix/Linux [LF]", "Mac Classic [CR]"),
                 (stc.STC_EOL_CRLF, stc.STC_EOL_LF, stc.STC_EOL_CR),
                 self.EOLMode,
             )
         )
         page.Append(pg.BoolProperty("Show EOL Symbols", "ViewEOL", self.ViewEOL))
 
-    def appendProperties_line_warp(self, page):
+    def appendProperties_line_warp(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Line Wrap"))
         page.Append(
             pg.EnumProperty(
                 "Wrap Mode",
                 "WrapMode",
                 ("Disabled", "Word Boundaries", "Characters"),
                 (stc.STC_WRAP_NONE, stc.STC_WRAP_WORD, stc.STC_WRAP_CHAR),
@@ -1035,15 +1059,15 @@
                     stc.STC_WRAPVISUALFLAGLOC_END_BY_TEXT,
                     stc.STC_WRAPVISUALFLAGLOC_START_BY_TEXT,
                 ),
                 self.WrapVisualFlagsLocation,
             )
         )
 
-    def appendProperties_line_numbers(self, page):
+    def appendProperties_line_numbers(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Line Numbers"))
         page.Append(
             pg.BoolProperty(
                 "Show Line Numbers", "ShowLineNumbers", self.ShowLineNumbers
             )
         )
         page.Append(
@@ -1051,15 +1075,15 @@
         )
         page.Append(
             StyleSpecProperty(
                 "Line Numbers", "STC_STYLE_LINENUMBER", self.STC_STYLE_LINENUMBER
             )
         )
 
-    def appendProperties_code_folding(self, page):
+    def appendProperties_code_folding(self, page: PreferencesPageBase):
         page.Append(pg.PropertyCategory("Code Folding"))
         page.Append(
             pg.BoolProperty("Show Fold Marks", "ShowFoldMarks", self.ShowFoldMarks)
         )
         page.Append(
             pg.IntProperty("Column Width", "FoldMarkColWidth", self.FoldMarkColWidth)
         )
@@ -1100,35 +1124,35 @@
         page.Append(pg.ColourProperty("Fill Colour", "FoldMarkFill", self.FoldMarkFill))
         page.Append(
             pg.ColourProperty(
                 "Highlight Colour", "FoldMarkHighlight", self.FoldMarkHighlight
             )
         )
 
-    def appendProperties_syntax_colour(self, page):
+    def appendProperties_syntax_colour(self, page: PreferencesPageBase):
         if self.syntax:
             page.Append(pg.PropertyCategory("Syntax Colour"))
             for name in self.syntax:
                 label = name.split("_", 2)[2].title()
                 page.Append(StyleSpecProperty(label, name, self.syntax[name]))
 
-    def appendProperties(self, page):
+    def appendProperties(self, page: PreferencesPageBase):
         """Append properties to PreferencesPage"""
         self.registerPropertyEditors(page)
         self.appendProperties_main(page)
         self.appendProperties_caret(page)
         self.appendProperties_selection(page)
         self.appendProperties_indentation(page)
         self.appendProperties_line_ending(page)
         self.appendProperties_line_warp(page)
         self.appendProperties_line_numbers(page)
         self.appendProperties_code_folding(page)
         self.appendProperties_syntax_colour(page)
 
-    def getPropertyValues(self, page):
+    def getPropertyValues(self, page: PreferencesPageBase):
         values = page.GetPropertyValues()
         fg = values.pop("foreground", wx.BLACK).GetAsString(wx.C2S_HTML_SYNTAX)
         bg = values.pop("background", wx.WHITE).GetAsString(wx.C2S_HTML_SYNTAX)
         font = values.pop("font", "Consolas")
         size = values.pop("size", 10)
         self.STC_STYLE_DEFAULT = f"fore:{fg},back:{bg},face:{font},size:{size}"
         for name in values:
@@ -1144,16 +1168,16 @@
                 if isinstance(val, type(None)):
                     self.syntax[name] = ""
                 elif isinstance(val, str):
                     self.syntax[name] = val
 
 
 class PyTextEditConfig(TextEditConfig):
-    def __init__(self):
-        TextEditConfig.__init__(self)
+    def __init__(self, parent):
+        super().__init__(parent)
         self.syntax["STC_P_DEFAULT"] = "fore:black,back:white"
         self.syntax["STC_P_IDENTIFIER"] = "fore:#000000"
         self.syntax["STC_P_WORD"] = "fore:#000080,italic"
         self.syntax["STC_P_WORD2"] = "fore:#B00000,italic"
         self.syntax["STC_P_COMMENTLINE"] = "fore:#008000,back:#F0FFF0"
         self.syntax["STC_P_COMMENTBLOCK"] = "fore:#008000,back:#F0FFF0"
         self.syntax["STC_P_NUMBER"] = "fore:#008080"
@@ -1165,16 +1189,16 @@
         self.syntax["STC_P_DEFNAME"] = "fore:#008080,bold"
         self.syntax["STC_P_DECORATOR"] = "fore:#006060"
         self.syntax["STC_P_OPERATOR"] = "fore:#900000,bold"
         self.syntax["STC_P_STRINGEOL"] = "fore:#800080"
 
 
 class XmlTextEditConfig(TextEditConfig):
-    def __init__(self):
-        TextEditConfig.__init__(self)
+    def __init__(self, parent):
+        super().__init__(parent)
         self.syntax["STC_H_DEFAULT"] = "fore:black,back:white"
         self.syntax["STC_H_XMLSTART"] = "fore:black,back:white"
         self.syntax["STC_H_XMLEND"] = "fore:black,back:white"
         self.syntax["STC_H_TAG"] = "fore:black,back:white"
         self.syntax["STC_H_TAGEND"] = "fore:black,back:white"
         self.syntax["STC_H_TAGUNKNOWN"] = "fore:black,back:white"
         self.syntax["STC_H_ATTRIBUTE"] = "fore:black,back:white"
```

### Comparing `wbBase-0.1.49/Lib/wbBase/dialog/multiSaveModifiedDialog.py` & `wbBase-0.1.52/Lib/wbBase/dialog/multiSaveModifiedDialog.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/dialog/multiSaveModifiedDialogUI.py` & `wbBase-0.1.52/Lib/wbBase/dialog/multiSaveModifiedDialogUI.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/dialog/preferences.py` & `wbBase-0.1.52/Lib/wbBase/dialog/preferences.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 
 class PreferencesDialog(wx.Dialog):
     def __init__(
         self,
         parent,
         id: int = wx.ID_ANY,
         title: str = "Preferences",
-        pos: wx.Position = wx.DefaultPosition,
+        pos: wx.Point = wx.DefaultPosition,
         size: wx.Size = wx.Size(600, 400),
         style: int = wx.CAPTION | wx.CLOSE_BOX | wx.RESIZE_BORDER,
     ):
         wx.Dialog.__init__(self, parent, id, title, pos, size, style)
         self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
         sizer = wx.BoxSizer(wx.VERTICAL)
         self.book = wx.Treebook(
@@ -55,24 +55,20 @@
     def app(self) -> App:
         return wx.GetApp()
 
     def addPages(self):
         self.book.AddPage(AppPreferences(self.book), "Application")
         self.book.AddSubPage(PanelPreferences(self.book), "Panels")
         self.book.AddSubPage(ExternalToolPreferences(self.book), "External Tools")
-        plugins = self.app.TopWindow.pluginManager
-        for name in plugins:
-            plugin = plugins[name]
-            if hasattr(plugin, "preferencepages"):
-                pages = plugin.preferencepages
-                if len(pages) > 0:
-                    if hasattr(plugin, "name"):
-                        name = plugin.name
-                    self.book.AddPage(pages[0](self.book), "Plugin - %s" % name)
-                    for page in pages[1:]:
+        for name, module in self.app.pluginManager.items():
+            if hasattr(module, "preferencepages"):
+                for i, page in enumerate(module.preferencepages):
+                    if i == 0:
+                        self.book.AddPage(page(self.book), "Plugin - %s" % name)
+                    else:
                         self.book.AddSubPage(page(self.book), page.name)
 
     # -----------------------------------------------------------------------------
     # Event handler
     # -----------------------------------------------------------------------------
 
     def on_apply(self, event):
@@ -138,32 +134,32 @@
         size = wx.DefaultSize
         style = pg.PG_SPLITTER_AUTO_CENTER
         pg.PropertyGrid.__init__(self, parent, id, pos, size, style)
         self.CaptionBackgroundColour = wx.Colour(200, 250, 200)
         self.MarginColour = wx.Colour(20, 150, 20)
 
     @property
-    def plugin(self) -> Optional[ModuleType]:
+    def plugin(self) -> str:
         """
-        plugin module to which this Preferences Page belongs to.
+        :return: Name of the plugin to which this Preferences Page belongs to.
         """
-        for plugin in self.app.TopWindow.pluginManager.values():
-            if hasattr(plugin, "preferencepages"):
-                for page in plugin.preferencepages:
+        for name, module in self.app.pluginManager.items():
+            if hasattr(module, "preferencepages"):
+                for page in module.preferencepages:
                     if page == self.__class__:
-                        return plugin
-        return None
+                        return name
+        return ""
 
     @property
     def config(self) -> wx.ConfigBase:
-        result = self.app.TopWindow.config
-        if self.plugin is None:
-            path = "/Application/"
-        else:
-            path = "/Plugin/%s/" % self.plugin.__name__
+        result = self.app.config
+        path = "/Application/"
+        plugin = self.plugin
+        if plugin:
+            path = f"/Plugin/{plugin}/"
         result.SetPath(path)
         return result
 
 
 class AppPreferences(PreferencesPageBase):
     def __init__(self, parent: wx.Treebook):
         PreferencesPageBase.__init__(self, parent)
@@ -463,15 +459,14 @@
             "Close tab by mouse middle button click",
             "Allows to close notebook tabs by mouse middle button click.",
         ),
     )
 
     def __init__(self, parent):
         PreferencesPageBase.__init__(self, parent)
-        cfg = self.config
         panelManager = self.app.TopWindow.panelManager
         self.Append(pg.PropertyCategory("Main"))
         flags = [i[0] for i in self.draggingStyles]
         labels = [i[1] for i in self.draggingStyles]
         self.Append(
             pg.FlagsProperty(
                 "Floating/Dragging Styles",
```

### Comparing `wbBase-0.1.49/Lib/wbBase/document/__init__.py` & `wbBase-0.1.52/Lib/wbBase/document/__init__.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/document/manager.py` & `wbBase-0.1.52/Lib/wbBase/document/manager.py`

 * *Files 0% similar despite different names*

```diff
@@ -142,15 +142,15 @@
         return self._flags
 
     @property
     def plugins(self) -> Dict[str, ModuleType]:
         """
         The plugins loaded by the PluginManager
         """
-        return self.app.pluginManager._plugins
+        return self.app.pluginManager
 
     @property
     def currentView(self) -> Optional[View]:
         """
         The currently active view, may be None.
         """
         if self._currentView:
```

### Comparing `wbBase-0.1.49/Lib/wbBase/document/notebook.py` & `wbBase-0.1.52/Lib/wbBase/document/notebook.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/document/template.py` & `wbBase-0.1.52/Lib/wbBase/document/template.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,19 +2,15 @@
 
 import logging
 import os
 from typing import TYPE_CHECKING, List, Optional, Union
 
 import wx
 
-# from . import dbg
-
 if TYPE_CHECKING:
-    from types import ModuleType
-
     from ..application import App
     from . import Document
     from .manager import DocumentManager
     from .view import View
 
 log = logging.getLogger(__name__)
 
@@ -183,30 +179,31 @@
     def viewTypeName(self) -> str:
         """
         The view type name, as passed to the document template constructor.
         """
         return self._viewTypeName
 
     @property
-    def plugin(self) -> Optional[ModuleType]:
-        plugins = self.app.pluginManager
-        for pluginName in plugins:
-            plugin = plugins[pluginName]
+    def plugin(self) -> str:
+        """
+        :return: Name of the plugin from which this document template was loaded
+        """
+        for name, module in self.app.pluginManager.items():
             if (
-                hasattr(plugin, "doctemplates")
-                and self.__class__ in plugin.doctemplates
+                hasattr(module, "doctemplates")
+                and self.__class__ in module.doctemplates
             ):
-                return plugin
-        return None
+                return name
+        return ""
 
     @property
     def config(self) -> Optional[wx.ConfigBase]:
         if self.plugin:
             cfg = self.app.config
-            cfg.SetPath("/Plugin/%s/%s/" % (self.plugin.__name__, self._docTypeName))
+            cfg.SetPath("/Plugin/%s/%s/" % (self.plugin, self._docTypeName))
             return cfg
         return None
 
     # -----------------------------------------------------------------------------
     # public methods
     # -----------------------------------------------------------------------------
     def GetViewType(self, viewTypeName: str) -> Optional[type[View]]:
@@ -240,15 +237,15 @@
             else:
                 view.Destroy()
         except Exception:
             log.exception("CreateView failed:")
             view.Destroy()
         return result
 
-    def CreateDocument(self, path, flags:int, **kwds) -> Optional[Document]:
+    def CreateDocument(self, path, flags: int, **kwds) -> Optional[Document]:
         """
         Creates a new instance of the associated document class. If you have
         not supplied a class to the template constructor, you will need to
         override this function to return an appropriate document instance.
         """
         result = None
         doc: Document = self._docType(self)
```

### Comparing `wbBase-0.1.49/Lib/wbBase/document/view.py` & `wbBase-0.1.52/Lib/wbBase/document/view.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/panelManager.py` & `wbBase-0.1.52/Lib/wbBase/panelManager.py`

 * *Files 0% similar despite different names*

```diff
@@ -58,29 +58,32 @@
 
     # -----------------------------------------------------------------------------
     # Properties
     # -----------------------------------------------------------------------------
 
     @property
     def app(self) -> App:
+        """
+        The running Workbench application.
+        """
         return wx.GetApp()
 
     @property
     def documentNotebook(self) -> DocumentNotebook:
         return self._documentNotebook
 
     @property
     def config(self) -> wx.ConfigBase:
         cfg = self.app.config
         cfg.SetPath("/Window/Panels/")
         return cfg
 
     @property
     def plugins(self) -> Dict[str, ModuleType]:
-        return self.app.pluginManager._plugins
+        return self.app.pluginManager
 
     @property
     def documentManager(self) -> DocumentManager:
         return self.ManagedWindow.documentManager
 
     @property
     def menu(self) -> wx.Menu:
```

### Comparing `wbBase-0.1.49/Lib/wbBase/pluginManager.py` & `wbBase-0.1.52/Lib/wbBase/pluginManager_old.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase/scripting.py` & `wbBase-0.1.52/Lib/wbBase/scripting.py`

 * *Files 1% similar despite different names*

```diff
@@ -124,15 +124,15 @@
         return self._macroTree
 
     # ==========================================================================
     # public methods
     # ==========================================================================
 
     def addMacroTree(self, macroTree, menu:wx.Menu) -> wx.Menu:
-        bmpDir = wx.ArtProvider.GetBitmap("wxART_FOLDER", wx.ART_MENU, (16, 16))
+        bmpDir = wx.ArtProvider.GetBitmap("wxART_FOLDER", wx.ART_MENU, wx.Size(16, 16))
         for name in sorted(macroTree, key=str.lower):
             item = macroTree[name]
             if isinstance(item, dict):
                 subMenu = MacroMenu(self.handler)
                 subMenu.addMacroTree(item, subMenu)
                 menuItem = menu.AppendSubMenu(subMenu, name)
                 menuItem.SetBitmap(bmpDir)
```

### Comparing `wbBase-0.1.49/Lib/wbBase/tools.py` & `wbBase-0.1.52/Lib/wbBase/tools.py`

 * *Files identical despite different names*

### Comparing `wbBase-0.1.49/Lib/wbBase.egg-info/SOURCES.txt` & `wbBase-0.1.52/Lib/wbBase.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 Lib/wbBase/__init__.py
 Lib/wbBase/application.py
 Lib/wbBase/applicationInfo.py
 Lib/wbBase/applicationWindow.py
 Lib/wbBase/artprovider.py
 Lib/wbBase/panelManager.py
 Lib/wbBase/pluginManager.py
+Lib/wbBase/pluginManager_old.py
 Lib/wbBase/scripting.py
 Lib/wbBase/tools.py
 Lib/wbBase.egg-info/PKG-INFO
 Lib/wbBase.egg-info/SOURCES.txt
 Lib/wbBase.egg-info/dependency_links.txt
 Lib/wbBase.egg-info/requires.txt
 Lib/wbBase.egg-info/top_level.txt
```

### Comparing `wbBase-0.1.49/setup.cfg` & `wbBase-0.1.52/setup.cfg`

 * *Files 20% similar despite different names*

```diff
@@ -1,26 +1,30 @@
 [bumpversion]
-current_version = 0.1.49
+current_version = 0.1.52
 commit = True
 tag = True
 tag_name = {new_version}
 parse = (?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)?
 serialize = 
 	{major}.{minor}.{patch}
 
 [metadata]
 name = wbBase
 version = attr: wbBase.__version__
 author = Andreas Eigendorf
 description = Base package for WorkBench applications.
-url = https://gitlab.com/workbench2/wbbase
 long_description = file: README.md
 long_description_content_type = text/markdown
 license = MIT
 license_files = LICENSE
+url = https://gitlab.com/workbench2/wbbase
+project_urls = 
+	Source = https://gitlab.com/workbench2/wbbase
+	Documentation = https://workbench2.gitlab.io/wbbase
+	Tracker = https://gitlab.com/workbench2/wbbase/-/issues
 platforms = 
 	WIN32
 	WIN64
 	OSX
 	POSIX
 keywords = 
 	workbench
@@ -49,14 +53,15 @@
 packages = find:
 python_requires = >=3.8
 install_requires = 
 	appdirs>=1.4.4
 	wxpython>=4.2.0
 	GitPython>=3.1
 	PyYAML>=6.0
+	importlib_metadata;python_version<'3.10'
 
 [options.packages.find]
 where = Lib
 
 [bumpversion:file:Lib/wbBase/__init__.py]
 search = __version__ = "{current_version}"
 replace = __version__ = "{new_version}"
@@ -67,16 +72,18 @@
 	py38
 	py39
 	py10
 
 [testenv]
 deps = 
 	pytest
+	pytest-cov
+	coverage
 commands = 
-	pytest
+	pytest --cov=wbBase --cov-report html:coverage.html
 
 [tool:pytest]
 junit_family = legacy
 testpaths = 
 	tests
 
 [egg_info]
```

