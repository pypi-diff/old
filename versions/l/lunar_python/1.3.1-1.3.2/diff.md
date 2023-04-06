# Comparing `tmp/lunar_python-1.3.1.tar.gz` & `tmp/lunar_python-1.3.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lunar_python-1.3.1.tar", last modified: Tue Mar 14 11:26:17 2023, max compression
+gzip compressed data, was "lunar_python-1.3.2.tar", last modified: Thu Apr  6 14:08:29 2023, max compression
```

## Comparing `lunar_python-1.3.1.tar` & `lunar_python-1.3.2.tar`

### file list

```diff
@@ -1,48 +1,48 @@
-drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-03-14 11:26:17.165107 lunar_python-1.3.1/
--rw-r--r--   0 apple      (501) staff       (20)     1061 2022-07-07 08:49:32.000000 lunar_python-1.3.1/LICENSE
--rw-r--r--   0 apple      (501) staff       (20)      348 2023-03-14 11:26:17.164578 lunar_python-1.3.1/PKG-INFO
--rw-r--r--   0 apple      (501) staff       (20)     1588 2022-12-03 09:55:03.000000 lunar_python-1.3.1/README.md
-drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-03-14 11:26:17.129968 lunar_python-1.3.1/lunar_python/
--rw-r--r--   0 apple      (501) staff       (20)    13568 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/EightChar.py
--rw-r--r--   0 apple      (501) staff       (20)     3469 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/Foto.py
--rw-r--r--   0 apple      (501) staff       (20)      946 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/FotoFestival.py
--rw-r--r--   0 apple      (501) staff       (20)      768 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/Fu.py
--rw-r--r--   0 apple      (501) staff       (20)     1263 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/Holiday.py
--rw-r--r--   0 apple      (501) staff       (20)     1383 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/JieQi.py
--rw-r--r--   0 apple      (501) staff       (20)    48723 2023-03-02 12:36:17.000000 lunar_python-1.3.1/lunar_python/Lunar.py
--rw-r--r--   0 apple      (501) staff       (20)     3757 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/LunarMonth.py
--rw-r--r--   0 apple      (501) staff       (20)     5122 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/LunarTime.py
--rw-r--r--   0 apple      (501) staff       (20)    11670 2023-03-14 09:17:59.000000 lunar_python-1.3.1/lunar_python/LunarYear.py
--rw-r--r--   0 apple      (501) staff       (20)     5148 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/NineStar.py
--rw-r--r--   0 apple      (501) staff       (20)      577 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/ShuJiu.py
--rw-r--r--   0 apple      (501) staff       (20)    14094 2023-03-14 06:36:10.000000 lunar_python-1.3.1/lunar_python/Solar.py
--rw-r--r--   0 apple      (501) staff       (20)     1690 2023-03-01 12:22:56.000000 lunar_python-1.3.1/lunar_python/SolarHalfYear.py
--rw-r--r--   0 apple      (501) staff       (20)     2196 2023-03-02 12:39:04.000000 lunar_python-1.3.1/lunar_python/SolarMonth.py
--rw-r--r--   0 apple      (501) staff       (20)     1638 2023-03-01 12:30:54.000000 lunar_python-1.3.1/lunar_python/SolarSeason.py
--rw-r--r--   0 apple      (501) staff       (20)     5707 2023-03-02 12:07:01.000000 lunar_python-1.3.1/lunar_python/SolarWeek.py
--rw-r--r--   0 apple      (501) staff       (20)     1130 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/SolarYear.py
--rw-r--r--   0 apple      (501) staff       (20)     3803 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/Tao.py
--rw-r--r--   0 apple      (501) staff       (20)      597 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/TaoFestival.py
--rw-r--r--   0 apple      (501) staff       (20)      638 2023-03-01 12:39:02.000000 lunar_python-1.3.1/lunar_python/__init__.py
-drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-03-14 11:26:17.147195 lunar_python-1.3.1/lunar_python/eightchar/
--rw-r--r--   0 apple      (501) staff       (20)     2611 2023-03-02 12:34:28.000000 lunar_python-1.3.1/lunar_python/eightchar/DaYun.py
--rw-r--r--   0 apple      (501) staff       (20)     1447 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/eightchar/LiuNian.py
--rw-r--r--   0 apple      (501) staff       (20)     1642 2022-11-06 09:05:32.000000 lunar_python-1.3.1/lunar_python/eightchar/LiuYue.py
--rw-r--r--   0 apple      (501) staff       (20)     1333 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/eightchar/XiaoYun.py
--rw-r--r--   0 apple      (501) staff       (20)     3423 2023-03-02 12:33:13.000000 lunar_python-1.3.1/lunar_python/eightchar/Yun.py
--rw-r--r--   0 apple      (501) staff       (20)      155 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/eightchar/__init__.py
-drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-03-14 11:26:17.163684 lunar_python-1.3.1/lunar_python/util/
--rw-r--r--   0 apple      (501) staff       (20)    13436 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/util/FotoUtil.py
--rw-r--r--   0 apple      (501) staff       (20)    19967 2023-03-02 12:39:39.000000 lunar_python-1.3.1/lunar_python/util/HolidayUtil.py
--rw-r--r--   0 apple      (501) staff       (20)   119455 2022-11-06 09:05:13.000000 lunar_python-1.3.1/lunar_python/util/LunarUtil.py
--rw-r--r--   0 apple      (501) staff       (20)    70850 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/util/ShouXingUtil.py
--rw-r--r--   0 apple      (501) staff       (20)     6607 2023-03-02 12:20:29.000000 lunar_python-1.3.1/lunar_python/util/SolarUtil.py
--rw-r--r--   0 apple      (501) staff       (20)     8061 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/util/TaoUtil.py
--rw-r--r--   0 apple      (501) staff       (20)      226 2022-07-07 08:49:32.000000 lunar_python-1.3.1/lunar_python/util/__init__.py
-drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-03-14 11:26:17.135587 lunar_python-1.3.1/lunar_python.egg-info/
--rw-r--r--   0 apple      (501) staff       (20)      348 2023-03-14 11:26:16.000000 lunar_python-1.3.1/lunar_python.egg-info/PKG-INFO
--rw-r--r--   0 apple      (501) staff       (20)     1108 2023-03-14 11:26:17.000000 lunar_python-1.3.1/lunar_python.egg-info/SOURCES.txt
--rw-r--r--   0 apple      (501) staff       (20)        1 2023-03-14 11:26:16.000000 lunar_python-1.3.1/lunar_python.egg-info/dependency_links.txt
--rw-r--r--   0 apple      (501) staff       (20)       13 2023-03-14 11:26:16.000000 lunar_python-1.3.1/lunar_python.egg-info/top_level.txt
--rw-r--r--   0 apple      (501) staff       (20)       38 2023-03-14 11:26:17.165303 lunar_python-1.3.1/setup.cfg
--rw-r--r--   0 apple      (501) staff       (20)      470 2023-03-14 11:25:23.000000 lunar_python-1.3.1/setup.py
+drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-04-06 14:08:29.780043 lunar_python-1.3.2/
+-rw-r--r--   0 apple      (501) staff       (20)     1061 2022-07-07 08:49:32.000000 lunar_python-1.3.2/LICENSE
+-rw-r--r--   0 apple      (501) staff       (20)      348 2023-04-06 14:08:29.778724 lunar_python-1.3.2/PKG-INFO
+-rw-r--r--   0 apple      (501) staff       (20)     1588 2022-12-03 09:55:03.000000 lunar_python-1.3.2/README.md
+drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-04-06 14:08:29.753994 lunar_python-1.3.2/lunar_python/
+-rw-r--r--   0 apple      (501) staff       (20)    13544 2023-04-06 13:43:38.000000 lunar_python-1.3.2/lunar_python/EightChar.py
+-rw-r--r--   0 apple      (501) staff       (20)     3848 2023-04-06 13:43:06.000000 lunar_python-1.3.2/lunar_python/Foto.py
+-rw-r--r--   0 apple      (501) staff       (20)      946 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/FotoFestival.py
+-rw-r--r--   0 apple      (501) staff       (20)      768 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/Fu.py
+-rw-r--r--   0 apple      (501) staff       (20)     1263 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/Holiday.py
+-rw-r--r--   0 apple      (501) staff       (20)     1383 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/JieQi.py
+-rw-r--r--   0 apple      (501) staff       (20)    48765 2023-04-06 13:52:21.000000 lunar_python-1.3.2/lunar_python/Lunar.py
+-rw-r--r--   0 apple      (501) staff       (20)     5403 2023-04-06 14:00:51.000000 lunar_python-1.3.2/lunar_python/LunarMonth.py
+-rw-r--r--   0 apple      (501) staff       (20)     5108 2023-04-06 13:49:49.000000 lunar_python-1.3.2/lunar_python/LunarTime.py
+-rw-r--r--   0 apple      (501) staff       (20)    11754 2023-04-06 13:54:42.000000 lunar_python-1.3.2/lunar_python/LunarYear.py
+-rw-r--r--   0 apple      (501) staff       (20)     5148 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/NineStar.py
+-rw-r--r--   0 apple      (501) staff       (20)      577 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/ShuJiu.py
+-rw-r--r--   0 apple      (501) staff       (20)    14116 2023-04-06 13:45:26.000000 lunar_python-1.3.2/lunar_python/Solar.py
+-rw-r--r--   0 apple      (501) staff       (20)     1690 2023-03-01 12:22:56.000000 lunar_python-1.3.2/lunar_python/SolarHalfYear.py
+-rw-r--r--   0 apple      (501) staff       (20)     2196 2023-03-02 12:39:04.000000 lunar_python-1.3.2/lunar_python/SolarMonth.py
+-rw-r--r--   0 apple      (501) staff       (20)     1638 2023-03-01 12:30:54.000000 lunar_python-1.3.2/lunar_python/SolarSeason.py
+-rw-r--r--   0 apple      (501) staff       (20)     5707 2023-03-02 12:07:01.000000 lunar_python-1.3.2/lunar_python/SolarWeek.py
+-rw-r--r--   0 apple      (501) staff       (20)     1130 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/SolarYear.py
+-rw-r--r--   0 apple      (501) staff       (20)     3803 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/Tao.py
+-rw-r--r--   0 apple      (501) staff       (20)      597 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/TaoFestival.py
+-rw-r--r--   0 apple      (501) staff       (20)      638 2023-03-01 12:39:02.000000 lunar_python-1.3.2/lunar_python/__init__.py
+drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-04-06 14:08:29.765445 lunar_python-1.3.2/lunar_python/eightchar/
+-rw-r--r--   0 apple      (501) staff       (20)     2611 2023-03-02 12:34:28.000000 lunar_python-1.3.2/lunar_python/eightchar/DaYun.py
+-rw-r--r--   0 apple      (501) staff       (20)     1447 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/eightchar/LiuNian.py
+-rw-r--r--   0 apple      (501) staff       (20)     1642 2022-11-06 09:05:32.000000 lunar_python-1.3.2/lunar_python/eightchar/LiuYue.py
+-rw-r--r--   0 apple      (501) staff       (20)     1333 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/eightchar/XiaoYun.py
+-rw-r--r--   0 apple      (501) staff       (20)     3423 2023-03-02 12:33:13.000000 lunar_python-1.3.2/lunar_python/eightchar/Yun.py
+-rw-r--r--   0 apple      (501) staff       (20)      155 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/eightchar/__init__.py
+drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-04-06 14:08:29.777247 lunar_python-1.3.2/lunar_python/util/
+-rw-r--r--   0 apple      (501) staff       (20)    14678 2023-04-06 13:41:30.000000 lunar_python-1.3.2/lunar_python/util/FotoUtil.py
+-rw-r--r--   0 apple      (501) staff       (20)    19967 2023-03-02 12:39:39.000000 lunar_python-1.3.2/lunar_python/util/HolidayUtil.py
+-rw-r--r--   0 apple      (501) staff       (20)   119267 2023-04-06 14:00:27.000000 lunar_python-1.3.2/lunar_python/util/LunarUtil.py
+-rw-r--r--   0 apple      (501) staff       (20)    70850 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/util/ShouXingUtil.py
+-rw-r--r--   0 apple      (501) staff       (20)     9960 2023-04-06 13:37:00.000000 lunar_python-1.3.2/lunar_python/util/SolarUtil.py
+-rw-r--r--   0 apple      (501) staff       (20)     8061 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/util/TaoUtil.py
+-rw-r--r--   0 apple      (501) staff       (20)      226 2022-07-07 08:49:32.000000 lunar_python-1.3.2/lunar_python/util/__init__.py
+drwxr-xr-x   0 apple      (501) staff       (20)        0 2023-04-06 14:08:29.760286 lunar_python-1.3.2/lunar_python.egg-info/
+-rw-r--r--   0 apple      (501) staff       (20)      348 2023-04-06 14:08:29.000000 lunar_python-1.3.2/lunar_python.egg-info/PKG-INFO
+-rw-r--r--   0 apple      (501) staff       (20)     1108 2023-04-06 14:08:29.000000 lunar_python-1.3.2/lunar_python.egg-info/SOURCES.txt
+-rw-r--r--   0 apple      (501) staff       (20)        1 2023-04-06 14:08:29.000000 lunar_python-1.3.2/lunar_python.egg-info/dependency_links.txt
+-rw-r--r--   0 apple      (501) staff       (20)       13 2023-04-06 14:08:29.000000 lunar_python-1.3.2/lunar_python.egg-info/top_level.txt
+-rw-r--r--   0 apple      (501) staff       (20)       38 2023-04-06 14:08:29.781122 lunar_python-1.3.2/setup.cfg
+-rw-r--r--   0 apple      (501) staff       (20)      470 2023-04-06 14:06:52.000000 lunar_python-1.3.2/setup.py
```

### Comparing `lunar_python-1.3.1/LICENSE` & `lunar_python-1.3.2/LICENSE`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/README.md` & `lunar_python-1.3.2/README.md`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/EightChar.py` & `lunar_python-1.3.2/lunar_python/EightChar.py`

 * *Files 0% similar despite different names*

```diff
@@ -110,16 +110,15 @@
     def getDayGanIndex(self):
         return self.__lunar.getDayGanIndexExact2() if 2 == self.__sect else self.__lunar.getDayGanIndexExact()
 
     def getDayZhiIndex(self):
         return self.__lunar.getDayZhiIndexExact2() if 2 == self.__sect else self.__lunar.getDayZhiIndexExact()
 
     def __getDiShi(self, zhi_index):
-        offset = self.__CHANG_SHENG_OFFSET.get(self.getDayGan())
-        index = offset + (zhi_index if self.getDayGanIndex() % 2 == 0 else -zhi_index)
+        index = self.__CHANG_SHENG_OFFSET.get(self.getDayGan()) + (zhi_index if self.getDayGanIndex() % 2 == 0 else -zhi_index)
         if index >= 12:
             index -= 12
         if index < 0:
             index += 12
         return EightChar.CHANG_SHENG[index]
 
     def getYearDiShi(self):
```

### Comparing `lunar_python-1.3.1/lunar_python/Foto.py` & `lunar_python-1.3.2/lunar_python/Foto.py`

 * *Files 9% similar despite different names*

```diff
@@ -52,21 +52,33 @@
         return self.__lunar.getMonthInChinese()
 
     def getDayInChinese(self):
         return self.__lunar.getDayInChinese()
 
     def getFestivals(self):
         festivals = []
-        md = "%d-%d" % (self.getMonth(), self.getDay())
+        md = "%d-%d" % (abs(self.getMonth()), self.getDay())
         if md in FotoUtil.FESTIVAL:
             fs = FotoUtil.FESTIVAL[md]
             for f in fs:
                 festivals.append(f)
         return festivals
 
+    def getOtherFestivals(self):
+        """
+        获取纪念日
+        :return: 非正式的节日列表，如中元节
+        """
+        festivals = []
+        key = "%d-%d" % (self.getMonth(), self.getDay())
+        if key in FotoUtil.OTHER_FESTIVAL:
+            for f in FotoUtil.OTHER_FESTIVAL[key]:
+                festivals.append(f)
+        return festivals
+
     def isMonthZhai(self):
         m = self.getMonth()
         return 1 == m or 5 == m or 9 == m
 
     def isDayYangGong(self):
         for f in self.getFestivals():
             if "杨公忌" == f.getName():
```

### Comparing `lunar_python-1.3.1/lunar_python/FotoFestival.py` & `lunar_python-1.3.2/lunar_python/FotoFestival.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/Fu.py` & `lunar_python-1.3.2/lunar_python/Fu.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/Holiday.py` & `lunar_python-1.3.2/lunar_python/Holiday.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/JieQi.py` & `lunar_python-1.3.2/lunar_python/JieQi.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/Lunar.py` & `lunar_python-1.3.2/lunar_python/Lunar.py`

 * *Files 1% similar despite different names*

```diff
@@ -243,39 +243,39 @@
     def getYearZhiByLiChun(self):
         return LunarUtil.ZHI[self.__yearZhiIndexByLiChun + 1]
 
     def getYearZhiExact(self):
         return LunarUtil.ZHI[self.__yearZhiIndexExact + 1]
 
     def getYearInGanZhi(self):
-        return self.getYearGan() + self.getYearZhi()
+        return "%s%s" % (self.getYearGan(), self.getYearZhi())
 
     def getYearInGanZhiByLiChun(self):
-        return self.getYearGanByLiChun() + self.getYearZhiByLiChun()
+        return "%s%s" % (self.getYearGanByLiChun(), self.getYearZhiByLiChun())
 
     def getYearInGanZhiExact(self):
-        return self.getYearGanExact() + self.getYearZhiExact()
+        return "%s%s" % (self.getYearGanExact(), self.getYearZhiExact())
 
     def getMonthGan(self):
         return LunarUtil.GAN[self.__monthGanIndex + 1]
 
     def getMonthGanExact(self):
         return LunarUtil.GAN[self.__monthGanIndexExact + 1]
 
     def getMonthZhi(self):
         return LunarUtil.ZHI[self.__monthZhiIndex + 1]
 
     def getMonthZhiExact(self):
         return LunarUtil.ZHI[self.__monthZhiIndexExact + 1]
 
     def getMonthInGanZhi(self):
-        return self.getMonthGan() + self.getMonthZhi()
+        return "%s%s" % (self.getMonthGan(), self.getMonthZhi())
 
     def getMonthInGanZhiExact(self):
-        return self.getMonthGanExact() + self.getMonthZhiExact()
+        return "%s%s" % (self.getMonthGanExact(), self.getMonthZhiExact())
 
     def getDayGan(self):
         return LunarUtil.GAN[self.__dayGanIndex + 1]
 
     def getDayGanExact(self):
         return LunarUtil.GAN[self.__dayGanIndexExact + 1]
 
@@ -288,30 +288,30 @@
     def getDayZhiExact(self):
         return LunarUtil.ZHI[self.__dayZhiIndexExact + 1]
 
     def getDayZhiExact2(self):
         return LunarUtil.ZHI[self.__dayZhiIndexExact2 + 1]
 
     def getDayInGanZhi(self):
-        return self.getDayGan() + self.getDayZhi()
+        return "%s%s" % (self.getDayGan(), self.getDayZhi())
 
     def getDayInGanZhiExact(self):
-        return self.getDayGanExact() + self.getDayZhiExact()
+        return "%s%s" % (self.getDayGanExact(), self.getDayZhiExact())
 
     def getDayInGanZhiExact2(self):
-        return self.getDayGanExact2() + self.getDayZhiExact2()
+        return "%s%s" % (self.getDayGanExact2(), self.getDayZhiExact2())
 
     def getTimeGan(self):
         return LunarUtil.GAN[self.__timeGanIndex + 1]
 
     def getTimeZhi(self):
         return LunarUtil.ZHI[self.__timeZhiIndex + 1]
 
     def getTimeInGanZhi(self):
-        return self.getTimeGan() + self.getTimeZhi()
+        return "%s%s" % (self.getTimeGan(), self.getTimeZhi())
 
     def getYearShengXiao(self):
         return LunarUtil.SHENGXIAO[self.__yearZhiIndex + 1]
 
     def getYearShengXiaoByLiChun(self):
         return LunarUtil.SHENGXIAO[self.__yearZhiIndexByLiChun + 1]
 
@@ -723,20 +723,18 @@
     def getZhiXing(self):
         offset = self.__dayZhiIndex - self.__monthZhiIndex
         if offset < 0:
             offset += 12
         return LunarUtil.ZHI_XING[offset + 1]
 
     def getDayTianShen(self):
-        offset = LunarUtil.ZHI_TIAN_SHEN_OFFSET[self.getMonthZhi()]
-        return LunarUtil.TIAN_SHEN[(self.__dayZhiIndex + offset) % 12 + 1]
+        return LunarUtil.TIAN_SHEN[(self.__dayZhiIndex + LunarUtil.ZHI_TIAN_SHEN_OFFSET[self.getMonthZhi()]) % 12 + 1]
 
     def getTimeTianShen(self):
-        offset = LunarUtil.ZHI_TIAN_SHEN_OFFSET[self.getDayZhiExact()]
-        return LunarUtil.TIAN_SHEN[(self.__timeZhiIndex + offset) % 12 + 1]
+        return LunarUtil.TIAN_SHEN[(self.__timeZhiIndex + LunarUtil.ZHI_TIAN_SHEN_OFFSET[self.getDayZhiExact()]) % 12 + 1]
 
     def getDayTianShenType(self):
         return LunarUtil.TIAN_SHEN_TYPE[self.getDayTianShen()]
 
     def getTimeTianShenType(self):
         return LunarUtil.TIAN_SHEN_TYPE[self.getTimeTianShen()]
```

### Comparing `lunar_python-1.3.1/lunar_python/LunarMonth.py` & `lunar_python-1.3.2/lunar_python/eightchar/Yun.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,122 +1,124 @@
 # -*- coding: utf-8 -*-
-from . import Solar, LunarYear, NineStar
-from .util import LunarUtil
+from . import DaYun
+from ..util import LunarUtil
 
 
-class LunarMonth:
+class Yun:
     """
-    农历月
+    运
     """
 
-    def __init__(self, lunar_year, lunar_month, day_count, first_julian_day):
-        self.__year = lunar_year
-        self.__month = lunar_month
-        self.__dayCount = day_count
-        self.__firstJulianDay = first_julian_day
-
-    @staticmethod
-    def fromYm(lunar_year, lunar_month):
-        from . import LunarYear
-        return LunarYear.fromYear(lunar_year).getMonth(lunar_month)
-
-    def getYear(self):
-        return self.__year
-
-    def getMonth(self):
-        return self.__month
-
-    def isLeap(self):
-        return self.__month < 0
-
-    def getDayCount(self):
-        return self.__dayCount
-
-    def getFirstJulianDay(self):
-        return self.__firstJulianDay
-
-    def getPositionTaiSui(self):
-        m = abs(self.__month) % 4
-        if 0 == m:
-            p = "巽"
-        elif 1 == m:
-            p = "艮"
-        elif 3 == m:
-            p = "坤"
+    def __init__(self, eight_char, gender, sect=1):
+        self.__lunar = eight_char.getLunar()
+        self.__gender = gender
+        yang = 0 == self.__lunar.getYearGanIndexExact() % 2
+        man = 1 == gender
+        self.__forward = (yang and man) or (not yang and not man)
+        self.__compute_start(sect)
+
+    def __compute_start(self, sect):
+        """
+        起运计算
+        """
+        prev_jie = self.__lunar.getPrevJie()
+        next_jie = self.__lunar.getNextJie()
+        current = self.__lunar.getSolar()
+        start = current if self.__forward else prev_jie.getSolar()
+        end = next_jie.getSolar() if self.__forward else current
+
+        hour = 0
+
+        if 2 == sect:
+            minutes = end.subtractMinute(start)
+            year = int(minutes / 4320)
+            minutes -= year * 4320
+            month = int(minutes / 360)
+            minutes -= month * 360
+            day = int(minutes / 12)
+            minutes -= day * 12
+            hour = minutes * 2
         else:
-            p = LunarUtil.POSITION_GAN[Solar.fromJulianDay(self.getFirstJulianDay()).getLunar().getMonthGanIndex()]
-        return p
+            end_time_zhi_index = 11 if end.getHour() == 23 else LunarUtil.getTimeZhiIndex(end.toYmdHms()[11: 16])
+            start_time_zhi_index = 11 if start.getHour() == 23 else LunarUtil.getTimeZhiIndex(start.toYmdHms()[11: 16])
+            # 时辰差
+            hour_diff = end_time_zhi_index - start_time_zhi_index
+            day_diff = end.subtract(start)
+            if hour_diff < 0:
+                hour_diff += 12
+                day_diff -= 1
+            month_diff = int(hour_diff * 10 / 30)
+            month = day_diff * 4 + month_diff
+            day = hour_diff * 10 - month_diff * 30
+            year = int(month / 12)
+            month = month - year * 12
+        self.__startYear = year
+        self.__startMonth = month
+        self.__startDay = day
+        self.__startHour = hour
 
-    def getPositionTaiSuiDesc(self):
-        return LunarUtil.POSITION_DESC[self.getPositionTaiSui()]
+    def getGender(self):
+        """
+        获取性别
+        :return: 性别(1男 ， 0女)
+        """
+        return self.__gender
 
-    def getNineStar(self):
-        index = LunarYear.fromYear(self.__year).getZhiIndex() % 3
-        m = abs(self.__month)
-        month_zhi_index = (13 + m) % 12
-        n = 27 - (index * 3)
-        if month_zhi_index < LunarUtil.BASE_MONTH_ZHI_INDEX:
-            n -= 3
-        offset = (n - month_zhi_index) % 9
-        return NineStar.fromIndex(offset)
-
-    def toString(self):
-        return "%d年%s%s月(%d天)" % (self.__year, ("闰" if self.isLeap() else ""), LunarUtil.MONTH[abs(self.__month)], self.__dayCount)
-
-    def __str__(self):
-        return self.toString()
-
-    def next(self, n):
-        """
-        获取往后推几个月的阴历月，如果要往前推，则月数用负数
-        :param n: 月数
-        :return: 阴历月
-        """
-        if 0 == n:
-            return LunarMonth.fromYm(self.__year, self.__month)
-        elif n > 0:
-            rest = n
-            ny = self.__year
-            iy = ny
-            im = self.__month
-            index = 0
-            months = LunarYear.fromYear(ny).getMonths()
-            while True:
-                size = len(months)
-                for i in range(0, size):
-                    m = months[i]
-                    if m.getYear() == iy and m.getMonth() == im:
-                        index = i
-                        break
-                more = size - index - 1
-                if rest < more:
-                    break
-                rest -= more
-                last_month = months[size - 1]
-                iy = last_month.getYear()
-                im = last_month.getMonth()
-                ny += 1
-                months = LunarYear.fromYear(ny).getMonths()
-            return months[index + rest]
-        else:
-            rest = -n
-            ny = self.__year
-            iy = ny
-            im = self.__month
-            index = 0
-            months = LunarYear.fromYear(ny).getMonths()
-            while True:
-                size = len(months)
-                for i in range(0, size):
-                    m = months[i]
-                    if m.getYear() == iy and m.getMonth() == im:
-                        index = i
-                        break
-                if rest <= index:
-                    break
-                rest -= index
-                first_month = months[0]
-                iy = first_month.getYear()
-                im = first_month.getMonth()
-                ny -= 1
-                months = LunarYear.fromYear(ny).getMonths()
-            return months[index - rest]
+    def getStartYear(self):
+        """
+        获取起运年数
+        :return: 起运年数
+        """
+        return self.__startYear
+
+    def getStartMonth(self):
+        """
+        获取起运月数
+        :return: 起运月数
+        """
+        return self.__startMonth
+
+    def getStartDay(self):
+        """
+        获取起运天数
+        :return: 起运天数
+        """
+        return self.__startDay
+
+    def getStartHour(self):
+        """
+        获取起运小时数
+        :return: 起运小时数
+        """
+        return self.__startHour
+
+    def isForward(self):
+        """
+        是否顺推
+        :return: true/false
+        """
+        return self.__forward
+
+    def getLunar(self):
+        return self.__lunar
+
+    def getStartSolar(self):
+        """
+        获取起运的阳历日期
+        :return: 阳历日期
+        """
+        solar = self.__lunar.getSolar()
+        solar = solar.nextYear(self.__startYear)
+        solar = solar.nextMonth(self.__startMonth)
+        solar = solar.next(self.__startDay)
+        return solar.nextHour(self.__startHour)
+
+    def getDaYun(self, n: int = 10):
+        """
+        获取大运
+        :param n: 轮数
+        :return: 大运
+        """
+        da_yun = []
+        for i in range(0, n):
+            da_yun.append(DaYun(self, i))
+        return da_yun
```

### Comparing `lunar_python-1.3.1/lunar_python/LunarTime.py` & `lunar_python-1.3.2/lunar_python/LunarTime.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     def getGan(self):
         return LunarUtil.GAN[self.__ganIndex + 1]
 
     def getZhi(self):
         return LunarUtil.ZHI[self.__zhiIndex + 1]
 
     def getGanZhi(self):
-        return self.getGan() + self.getZhi()
+        return "%s%s" % (self.getGan(), self.getZhi())
 
     def getShengXiao(self):
         return LunarUtil.SHENGXIAO[self.__zhiIndex + 1]
 
     def getPositionXi(self):
         return LunarUtil.POSITION_XI[self.__ganIndex + 1]
 
@@ -82,16 +82,15 @@
     def getSha(self):
         return LunarUtil.SHA[self.getZhi()]
 
     def getNaYin(self):
         return LunarUtil.NAYIN[self.getGanZhi()]
 
     def getTianShen(self):
-        offset = LunarUtil.ZHI_TIAN_SHEN_OFFSET[self.__lunar.getDayZhiExact()]
-        return LunarUtil.TIAN_SHEN[(self.__zhiIndex + offset) % 12 + 1]
+        return LunarUtil.TIAN_SHEN[(self.__zhiIndex + LunarUtil.ZHI_TIAN_SHEN_OFFSET[self.__lunar.getDayZhiExact()]) % 12 + 1]
 
     def getTianShenType(self):
         return LunarUtil.TIAN_SHEN_TYPE[self.getTianShen()]
 
     def getTianShenLuck(self):
         return LunarUtil.TIAN_SHEN_TYPE_LUCK[self.getTianShenType()]
```

### Comparing `lunar_python-1.3.1/lunar_python/LunarYear.py` & `lunar_python-1.3.2/lunar_python/LunarYear.py`

 * *Files 0% similar despite different names*

```diff
@@ -101,23 +101,26 @@
                     while hs[i + 1] > jq[2 * i] and i < 13:
                         i += 1
                     leap_year = current_year
                     leap_index = i
 
         y = prev_year
         m = 11
+        index = m
         for i in range(0, 15):
             cm = m
             if y == leap_year and i == leap_index:
                 cm = -m
-            self.__months.append(LunarMonth(y, cm, day_counts[i], hs[i] + Solar.J2000))
+            self.__months.append(LunarMonth(y, cm, day_counts[i], hs[i] + Solar.J2000, index))
             if y != leap_year or i + 1 != leap_index:
                 m += 1
+            index += 1
             if m == 13:
                 m = 1
+                index = 1
                 y += 1
 
     def getYear(self):
         return self.__year
 
     def getGanIndex(self):
         return self.__ganIndex
@@ -128,15 +131,15 @@
     def getGan(self):
         return LunarUtil.GAN[self.__ganIndex + 1]
 
     def getZhi(self):
         return LunarUtil.ZHI[self.__zhiIndex + 1]
 
     def getGanZhi(self):
-        return self.getGan() + self.getZhi()
+        return "%s%s" % (self.getGan(), self.getZhi())
 
     def toString(self):
         return str(self.__year) + ""
 
     def toFullString(self):
         return "%d年" % self.__year
```

### Comparing `lunar_python-1.3.1/lunar_python/NineStar.py` & `lunar_python-1.3.2/lunar_python/NineStar.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/ShuJiu.py` & `lunar_python-1.3.2/lunar_python/ShuJiu.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/Solar.py` & `lunar_python-1.3.2/lunar_python/Solar.py`

 * *Files 1% similar despite different names*

```diff
@@ -98,14 +98,15 @@
             years.append(start_year)
             start_year -= 60
         hours = []
         time_zhi = time_gan_zhi[1:]
         for i in range(1, len(LunarUtil.ZHI)):
             if LunarUtil.ZHI[i] == time_zhi:
                 hours.append((i - 1) * 2)
+                break
         if "子" == time_zhi:
             hours.append(23)
         for hour in hours:
             for y in years:
                 max_year = y + 3
                 year = y
                 month = 11
```

### Comparing `lunar_python-1.3.1/lunar_python/SolarHalfYear.py` & `lunar_python-1.3.2/lunar_python/SolarHalfYear.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/SolarMonth.py` & `lunar_python-1.3.2/lunar_python/SolarMonth.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/SolarSeason.py` & `lunar_python-1.3.2/lunar_python/SolarSeason.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/SolarWeek.py` & `lunar_python-1.3.2/lunar_python/SolarWeek.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/SolarYear.py` & `lunar_python-1.3.2/lunar_python/SolarYear.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/Tao.py` & `lunar_python-1.3.2/lunar_python/Tao.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/TaoFestival.py` & `lunar_python-1.3.2/lunar_python/TaoFestival.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/__init__.py` & `lunar_python-1.3.2/lunar_python/__init__.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/eightchar/DaYun.py` & `lunar_python-1.3.2/lunar_python/eightchar/DaYun.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/eightchar/LiuNian.py` & `lunar_python-1.3.2/lunar_python/eightchar/LiuNian.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/eightchar/LiuYue.py` & `lunar_python-1.3.2/lunar_python/eightchar/LiuYue.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/eightchar/XiaoYun.py` & `lunar_python-1.3.2/lunar_python/eightchar/XiaoYun.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/util/FotoUtil.py` & `lunar_python-1.3.2/lunar_python/util/FotoUtil.py`

 * *Files 15% similar despite different names*

```diff
@@ -263,9 +263,42 @@
         "12-25": [FotoFestival("三清玉帝同降，考察善恶", "犯者得奇祸"), __H],
         "12-27": [__D],
         "12-28": [__R],
         "12-29": [FotoFestival("华严菩萨诞"), __T],
         "12-30": [FotoFestival("诸神下降，察访善恶", "犯者男女俱亡")]
     }
 
+    OTHER_FESTIVAL = {
+        "1-1": ["弥勒菩萨圣诞"],
+        "1-6": ["定光佛圣诞"],
+        "2-8": ["释迦牟尼佛出家"],
+        "2-15": ["释迦牟尼佛涅槃"],
+        "2-19": ["观世音菩萨圣诞"],
+        "2-21": ["普贤菩萨圣诞"],
+        "3-16": ["准提菩萨圣诞"],
+        "4-4": ["文殊菩萨圣诞"],
+        "4-8": ["释迦牟尼佛圣诞"],
+        "4-15": ["佛吉祥日"],
+        "4-28": ["药王菩萨圣诞"],
+        "5-13": ["伽蓝菩萨圣诞"],
+        "6-3": ["韦驮菩萨圣诞"],
+        "6-19": ["观音菩萨成道"],
+        "7-13": ["大势至菩萨圣诞"],
+        "7-15": ["佛欢喜日"],
+        "7-24": ["龙树菩萨圣诞"],
+        "7-30": ["地藏菩萨圣诞"],
+        "8-15": ["月光菩萨圣诞"],
+        "8-22": ["燃灯佛圣诞"],
+        "9-9": ["摩利支天菩萨圣诞"],
+        "9-19": ["观世音菩萨出家"],
+        "9-30": ["药师琉璃光佛圣诞"],
+        "10-5": ["达摩祖师圣诞"],
+        "10-20": ["文殊菩萨出家"],
+        "11-17": ["阿弥陀佛圣诞"],
+        "11-19": ["日光菩萨圣诞"],
+        "12-8": ["释迦牟尼佛成道"],
+        "12-23": ["监斋菩萨圣诞"],
+        "12-29": ["华严菩萨圣诞"]
+    }
+
     def __init__(self):
         pass
```

### Comparing `lunar_python-1.3.1/lunar_python/util/HolidayUtil.py` & `lunar_python-1.3.2/lunar_python/util/HolidayUtil.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/util/LunarUtil.py` & `lunar_python-1.3.2/lunar_python/util/LunarUtil.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # -*- coding: utf-8 -*-
 
 
 class LunarUtil:
-    """+
+    """
     农历工具
     """
 
     BASE_MONTH_ZHI_INDEX = 2
     XUN = ("甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅")
     XUN_KONG = ("戌亥", "申酉", "午未", "辰巳", "寅卯", "子丑")
     LIU_YAO = ("先胜", "友引", "先负", "佛灭", "大安", "赤口")
@@ -97,15 +97,15 @@
     PENG_ZU_GAN = ("", "甲不开仓财物耗散", "乙不栽植千株不长", "丙不修灶必见灾殃", "丁不剃头头必生疮", "戊不受田田主不祥", "己不破券二比并亡", "庚不经络织机虚张", "辛不合酱主人不尝", "壬不泱水更难提防", "癸不词讼理弱敌强")
     PENG_ZU_ZHI = ("", "子不问卜自惹祸殃", "丑不冠带主不还乡", "寅不祭祀神鬼不尝", "卯不穿井水泉不香", "辰不哭泣必主重丧", "巳不远行财物伏藏", "午不苫盖屋主更张", "未不服药毒气入肠", "申不安床鬼祟入房", "酉不会客醉坐颠狂", "戌不吃犬作怪上床", "亥不嫁娶不利新郎")
     NUMBER = ("〇", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二")
     MONTH = ("", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "冬", "腊")
     SEASON = ("", "孟春", "仲春", "季春", "孟夏", "仲夏", "季夏", "孟秋", "仲秋", "季秋", "孟冬", "仲冬", "季冬")
     SHENGXIAO = ("", "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪")
     DAY = ("", "初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十")
-    YUE_XIANG = ("", "朔", "既朔", "蛾眉新", "蛾眉新", "蛾眉", "夕月", "上弦", "上弦", "九夜", "宵", "宵", "宵", "渐盈凸", "小望", "望", "既望", "立待", "居待", "寝待", "更待", "渐亏凸", "下弦", "下弦", "有明", "有明", "蛾眉残", "蛾眉残", "残", "晓", "晦")
+    YUE_XIANG = ("", "朔", "既朔", "蛾眉新", "蛾眉新", "蛾眉", "夕", "上弦", "上弦", "九夜", "宵", "宵", "宵", "渐盈凸", "小望", "望", "既望", "立待", "居待", "寝待", "更待", "渐亏凸", "下弦", "下弦", "有明", "有明", "蛾眉残", "蛾眉残", "残", "晓", "晦")
     FESTIVAL = {
         "1-1": "春节",
         "1-15": "元宵节",
         "2-2": "龙头节",
         "5-5": "端午节",
         "7-7": "七夕节",
         "8-15": "中秋节",
@@ -1005,23 +1005,21 @@
             right = right[index + 3:]
             left = right
             if "=" in left:
                 left = left[:right.find("=") - 2]
             matched = False
             months = left[:left.find(":")]
             for i in range(0, len(months), 2):
-                m = months[i:i + 2]
-                if m == month:
+                if months[i:i + 2] == month:
                     matched = True
                     break
             if matched:
                 ys = left[left.find(":") + 1:left.find(",")]
                 for i in range(0, len(ys), 2):
-                    m = ys[i:i + 2]
-                    arr.append(LunarUtil.__YI_JI[int(m, 16)])
+                    arr.append(LunarUtil.__YI_JI[int(ys[i:i + 2], 16)])
                 break
             index = right.find(day + "=")
         if len(arr) < 1:
             arr.append("无")
         return arr
 
     @staticmethod
@@ -1041,23 +1039,21 @@
             right = right[index + 3:]
             left = right
             if "=" in left:
                 left = left[:right.find("=") - 2]
             matched = False
             months = left[:left.find(":")]
             for i in range(0, len(months), 2):
-                m = months[i:i + 2]
-                if m == month:
+                if months[i:i + 2] == month:
                     matched = True
                     break
             if matched:
                 js = left[left.find(",") + 1:]
                 for i in range(0, len(js), 2):
-                    m = js[i:i + 2]
-                    arr.append(LunarUtil.__YI_JI[int(m, 16)])
+                    arr.append(LunarUtil.__YI_JI[int(js[i:i + 2], 16)])
                 break
             index = right.find(day + "=")
         if len(arr) < 1:
             arr.append("无")
         return arr
 
     @staticmethod
@@ -1074,16 +1070,15 @@
         index = LunarUtil.__DAY_SHEN_SHA.find(month + day + "=")
         if index > -1:
             left = LunarUtil.__DAY_SHEN_SHA[index + 4:]
             if "=" in left:
                 left = left[:left.find("=") - 3]
             js = left[:left.find(",")]
             for i in range(0, len(js), 2):
-                m = js[i:i + 2]
-                arr.append(LunarUtil.__SHEN_SHA[int(m, 16)])
+                arr.append(LunarUtil.__SHEN_SHA[int(js[i:i + 2], 16)])
         if len(arr) < 1:
             arr.append("无")
         return arr
 
     @staticmethod
     def getDayXiongSha(lunar_month, day_gan_zhi):
         """
@@ -1098,16 +1093,15 @@
         index = LunarUtil.__DAY_SHEN_SHA.find(month + day + "=")
         if index > -1:
             left = LunarUtil.__DAY_SHEN_SHA[index + 4:]
             if "=" in left:
                 left = left[:left.find("=") - 3]
             xs = left[left.find(",") + 1:]
             for i in range(0, len(xs), 2):
-                m = xs[i:i + 2]
-                arr.append(LunarUtil.__SHEN_SHA[int(m, 16)])
+                arr.append(LunarUtil.__SHEN_SHA[int(xs[i:i + 2], 16)])
         if len(arr) < 1:
             arr.append("无")
         return arr
 
     @staticmethod
     def getTimeYi(day_gan_zhi, time_gan_zhi):
         """
@@ -1122,16 +1116,15 @@
         index = LunarUtil.__TIME_YI_JI.find(day + time + "=")
         if index > -1:
             left = LunarUtil.__TIME_YI_JI[index + 5:]
             if "=" in left:
                 left = left[:left.find("=") - 4]
             ys = left[:left.find(",")]
             for i in range(0, len(ys), 2):
-                m = ys[i:i + 2]
-                arr.append(LunarUtil.__YI_JI[int(m, 16)])
+                arr.append(LunarUtil.__YI_JI[int(ys[i:i + 2], 16)])
         if len(arr) < 1:
             arr.append("无")
         return arr
 
     @staticmethod
     def getTimeJi(day_gan_zhi, time_gan_zhi):
         """
@@ -1146,16 +1139,15 @@
         index = LunarUtil.__TIME_YI_JI.find(day + time + "=")
         if index > -1:
             left = LunarUtil.__TIME_YI_JI[index + 5:]
             if "=" in left:
                 left = left[:left.find("=") - 4]
             js = left[left.find(",") + 1:]
             for i in range(0, len(js), 2):
-                m = js[i:i + 2]
-                arr.append(LunarUtil.__YI_JI[int(m, 16)])
+                arr.append(LunarUtil.__YI_JI[int(js[i:i + 2], 16)])
         if len(arr) < 1:
             arr.append("无")
         return arr
 
     @staticmethod
     def getXunIndex(gan_zhi):
         """
```

### Comparing `lunar_python-1.3.1/lunar_python/util/ShouXingUtil.py` & `lunar_python-1.3.2/lunar_python/util/ShouXingUtil.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python/util/TaoUtil.py` & `lunar_python-1.3.2/lunar_python/util/TaoUtil.py`

 * *Files identical despite different names*

### Comparing `lunar_python-1.3.1/lunar_python.egg-info/SOURCES.txt` & `lunar_python-1.3.2/lunar_python.egg-info/SOURCES.txt`

 * *Files identical despite different names*

