# Comparing `tmp/redfin-scraper-0.1.4.tar.gz` & `tmp/redfin-scraper-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "redfin-scraper-0.1.4.tar", last modified: Tue Apr  4 15:04:54 2023, max compression
+gzip compressed data, was "redfin-scraper-0.1.5.tar", last modified: Thu Apr  6 15:28:16 2023, max compression
```

## Comparing `redfin-scraper-0.1.4.tar` & `redfin-scraper-0.1.5.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxrwxrwx   0        0        0        0 2023-04-04 15:04:53.998934 redfin-scraper-0.1.4/
--rw-rw-rw-   0        0        0     1087 2023-03-18 00:15:21.000000 redfin-scraper-0.1.4/LICENSE.txt
--rw-rw-rw-   0        0        0     4016 2023-04-04 15:04:53.998934 redfin-scraper-0.1.4/PKG-INFO
--rw-rw-rw-   0        0        0     2150 2023-03-23 15:47:49.000000 redfin-scraper-0.1.4/README.md
--rw-rw-rw-   0        0        0      904 2023-04-04 15:03:15.000000 redfin-scraper-0.1.4/pyproject.toml
-drwxrwxrwx   0        0        0        0 2023-04-04 15:04:53.964500 redfin-scraper-0.1.4/redfin_scraper/
--rw-rw-rw-   0        0        0      120 2023-04-04 15:03:24.000000 redfin-scraper-0.1.4/redfin_scraper/__init__.py
--rw-rw-rw-   0        0        0      325 2023-03-18 17:58:54.000000 redfin-scraper-0.1.4/redfin_scraper/config.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:04:53.990500 redfin-scraper-0.1.4/redfin_scraper/core/
--rw-rw-rw-   0        0        0        0 2023-03-11 03:00:34.000000 redfin-scraper-0.1.4/redfin_scraper/core/__init__.py
--rw-rw-rw-   0        0        0    11702 2023-04-04 14:59:59.000000 redfin-scraper-0.1.4/redfin_scraper/core/redfin_scraper.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:04:53.996927 redfin-scraper-0.1.4/redfin_scraper/resources/
--rw-rw-rw-   0        0        0        0 2023-02-25 20:03:01.000000 redfin-scraper-0.1.4/redfin_scraper/resources/__init__.py
--rw-rw-rw-   0        0        0     1116 2023-03-11 03:00:17.000000 redfin-scraper-0.1.4/redfin_scraper/resources/json_tools.py
--rw-rw-rw-   0        0        0     2462 2023-04-04 15:04:28.000000 redfin-scraper-0.1.4/redfin_scraper/resources/logging.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:04:53.988509 redfin-scraper-0.1.4/redfin_scraper.egg-info/
--rw-rw-rw-   0        0        0     4016 2023-04-04 15:04:53.000000 redfin-scraper-0.1.4/redfin_scraper.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      459 2023-04-04 15:04:53.000000 redfin-scraper-0.1.4/redfin_scraper.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-04 15:04:53.000000 redfin-scraper-0.1.4/redfin_scraper.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       43 2023-04-04 15:04:53.000000 redfin-scraper-0.1.4/redfin_scraper.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-04-04 15:04:53.000000 redfin-scraper-0.1.4/redfin_scraper.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-04 15:04:53.999934 redfin-scraper-0.1.4/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 15:28:16.463302 redfin-scraper-0.1.5/
+-rw-rw-rw-   0        0        0     1087 2023-03-18 00:15:21.000000 redfin-scraper-0.1.5/LICENSE.txt
+-rw-rw-rw-   0        0        0     4020 2023-04-06 15:28:16.458304 redfin-scraper-0.1.5/PKG-INFO
+-rw-rw-rw-   0        0        0     2154 2023-04-04 15:15:03.000000 redfin-scraper-0.1.5/README.md
+-rw-rw-rw-   0        0        0      904 2023-04-06 15:25:40.000000 redfin-scraper-0.1.5/pyproject.toml
+drwxrwxrwx   0        0        0        0 2023-04-06 15:28:16.417199 redfin-scraper-0.1.5/redfin_scraper/
+-rw-rw-rw-   0        0        0      120 2023-04-06 15:25:43.000000 redfin-scraper-0.1.5/redfin_scraper/__init__.py
+-rw-rw-rw-   0        0        0      325 2023-03-18 17:58:54.000000 redfin-scraper-0.1.5/redfin_scraper/config.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:28:16.449300 redfin-scraper-0.1.5/redfin_scraper/core/
+-rw-rw-rw-   0        0        0        0 2023-03-11 03:00:34.000000 redfin-scraper-0.1.5/redfin_scraper/core/__init__.py
+-rw-rw-rw-   0        0        0    11730 2023-04-06 15:27:53.000000 redfin-scraper-0.1.5/redfin_scraper/core/redfin_scraper.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:28:16.454300 redfin-scraper-0.1.5/redfin_scraper/resources/
+-rw-rw-rw-   0        0        0        0 2023-02-25 20:03:01.000000 redfin-scraper-0.1.5/redfin_scraper/resources/__init__.py
+-rw-rw-rw-   0        0        0     1116 2023-03-11 03:00:17.000000 redfin-scraper-0.1.5/redfin_scraper/resources/json_tools.py
+-rw-rw-rw-   0        0        0     2462 2023-04-04 15:04:28.000000 redfin-scraper-0.1.5/redfin_scraper/resources/logging.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:28:16.445088 redfin-scraper-0.1.5/redfin_scraper.egg-info/
+-rw-rw-rw-   0        0        0     4020 2023-04-06 15:28:16.000000 redfin-scraper-0.1.5/redfin_scraper.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      459 2023-04-06 15:28:16.000000 redfin-scraper-0.1.5/redfin_scraper.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:28:16.000000 redfin-scraper-0.1.5/redfin_scraper.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       43 2023-04-06 15:28:16.000000 redfin-scraper-0.1.5/redfin_scraper.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 15:28:16.000000 redfin-scraper-0.1.5/redfin_scraper.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 15:28:16.464301 redfin-scraper-0.1.5/setup.cfg
```

### Comparing `redfin-scraper-0.1.4/LICENSE.txt` & `redfin-scraper-0.1.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `redfin-scraper-0.1.4/PKG-INFO` & `redfin-scraper-0.1.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: redfin-scraper
-Version: 0.1.4
+Version: 0.1.5
 Summary: A Python library used to scrape data from Redfin.com using the unofficial Stringray API.
 Author-email: Ryan Sherby <ryan.m.sherby@gmail.com>
 License: MIT License
         
         Copyright (c) 2023 Ryan Sherby
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
@@ -49,15 +49,15 @@
 
 > [Sample Config](https://github.com/ryansherby/RedfinScraper/blob/main/config.json)
 
 
 
 ## Getting Started
 ### Installation
-`pip install redfin-scraper`
+`pip3 install -U redfin-scraper`
 
 ### Import Module
 `from redfin_scraper import RedfinScraper`  
 
 ### Initialize Module
 `scraper = RedfinScraper()`
```

### Comparing `redfin-scraper-0.1.4/README.md` & `redfin-scraper-0.1.5/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 
 > [Sample Config](https://github.com/ryansherby/RedfinScraper/blob/main/config.json)
 
 
 
 ## Getting Started
 ### Installation
-`pip install redfin-scraper`
+`pip3 install -U redfin-scraper`
 
 ### Import Module
 `from redfin_scraper import RedfinScraper`  
 
 ### Initialize Module
 `scraper = RedfinScraper()`
```

### Comparing `redfin-scraper-0.1.4/pyproject.toml` & `redfin-scraper-0.1.5/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 [build-system]
 requires      = ["setuptools>=61.0.0", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "redfin-scraper"
-version = "0.1.4"
+version = "0.1.5"
 description = "A Python library used to scrape data from Redfin.com using the unofficial Stringray API."
 readme = "README.md"
 authors = [{ name = "Ryan Sherby", email = "ryan.m.sherby@gmail.com" }]
 license = { file = "LICENSE.txt" }
 classifiers = [
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python",
```

### Comparing `redfin-scraper-0.1.4/redfin_scraper/core/redfin_scraper.py` & `redfin-scraper-0.1.5/redfin_scraper/core/redfin_scraper.py`

 * *Files 1% similar despite different names*

```diff
@@ -155,17 +155,17 @@
 
 
         if len(df_list)==0:
             self.data[self.data_id]=None
             return None
 
 
-        concat_df=pd.concat(df_list,axis=0)
+        concat_df=pd.concat(df_list,axis=0,ignore_index=True)
         concat_df=concat_df.apply(lambda row:pd.to_numeric(row,errors='ignore'))
-        concat_df.reset_index(inplace=True)
+        concat_df.reset_index(inplace=True,drop=True)
     
         self.df=concat_df
 
         self.data[self.data_id]=self.df
         return self.df
```

### Comparing `redfin-scraper-0.1.4/redfin_scraper/resources/json_tools.py` & `redfin-scraper-0.1.5/redfin_scraper/resources/json_tools.py`

 * *Files identical despite different names*

### Comparing `redfin-scraper-0.1.4/redfin_scraper/resources/logging.py` & `redfin-scraper-0.1.5/redfin_scraper/resources/logging.py`

 * *Files identical despite different names*

### Comparing `redfin-scraper-0.1.4/redfin_scraper.egg-info/PKG-INFO` & `redfin-scraper-0.1.5/redfin_scraper.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: redfin-scraper
-Version: 0.1.4
+Version: 0.1.5
 Summary: A Python library used to scrape data from Redfin.com using the unofficial Stringray API.
 Author-email: Ryan Sherby <ryan.m.sherby@gmail.com>
 License: MIT License
         
         Copyright (c) 2023 Ryan Sherby
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
@@ -49,15 +49,15 @@
 
 > [Sample Config](https://github.com/ryansherby/RedfinScraper/blob/main/config.json)
 
 
 
 ## Getting Started
 ### Installation
-`pip install redfin-scraper`
+`pip3 install -U redfin-scraper`
 
 ### Import Module
 `from redfin_scraper import RedfinScraper`  
 
 ### Initialize Module
 `scraper = RedfinScraper()`
```

