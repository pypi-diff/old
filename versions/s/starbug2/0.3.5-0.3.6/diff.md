# Comparing `tmp/starbug2-0.3.5.tar.gz` & `tmp/starbug2-0.3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "starbug2-0.3.5.tar", last modified: Wed Apr  5 10:16:47 2023, max compression
+gzip compressed data, was "starbug2-0.3.6.tar", last modified: Thu Apr  6 11:40:12 2023, max compression
```

## Comparing `starbug2-0.3.5.tar` & `starbug2-0.3.6.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 10:16:47.838388 starbug2-0.3.5/
--rw-r--r--   0 runner    (1001) docker     (123)      388 2023-04-05 10:16:31.000000 starbug2-0.3.5/CITATION.cff
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-04-05 10:16:31.000000 starbug2-0.3.5/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-05 10:16:31.000000 starbug2-0.3.5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     4277 2023-04-05 10:16:47.838388 starbug2-0.3.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4032 2023-04-05 10:16:31.000000 starbug2-0.3.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 10:16:47.834388 starbug2-0.3.5/bin/
--rwxr-xr-x   0 runner    (1001) docker     (123)    10678 2023-04-05 10:16:31.000000 starbug2-0.3.5/bin/starbug2
--rwxr-xr-x   0 runner    (1001) docker     (123)     3644 2023-04-05 10:16:31.000000 starbug2-0.3.5/bin/starbug2-match
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 10:16:47.834388 starbug2-0.3.5/extras/
--rw-r--r--   0 runner    (1001) docker     (123)     1829 2023-04-05 10:16:31.000000 starbug2-0.3.5/extras/starbug2.completion
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-04-05 10:16:31.000000 starbug2-0.3.5/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-04-05 10:16:47.838388 starbug2-0.3.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-04-05 10:16:31.000000 starbug2-0.3.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 10:16:47.834388 starbug2-0.3.5/starbug2/
--rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-04-05 10:16:31.000000 starbug2-0.3.5/starbug2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14164 2023-04-05 10:16:31.000000 starbug2-0.3.5/starbug2/matching.py
--rw-r--r--   0 runner    (1001) docker     (123)     4215 2023-04-05 10:16:31.000000 starbug2-0.3.5/starbug2/misc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 10:16:47.834388 starbug2-0.3.5/starbug2/param/
--rw-r--r--   0 runner    (1001) docker     (123)     3360 2023-04-05 10:16:31.000000 starbug2-0.3.5/starbug2/param/default.param
--rw-r--r--   0 runner    (1001) docker     (123)    26920 2023-04-05 10:16:31.000000 starbug2-0.3.5/starbug2/routines.py
--rw-r--r--   0 runner    (1001) docker     (123)    28293 2023-04-05 10:16:31.000000 starbug2-0.3.5/starbug2/starbug.py
--rw-r--r--   0 runner    (1001) docker     (123)     9241 2023-04-05 10:16:31.000000 starbug2-0.3.5/starbug2/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 10:16:47.834388 starbug2-0.3.5/starbug2.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4277 2023-04-05 10:16:47.000000 starbug2-0.3.5/starbug2.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      488 2023-04-05 10:16:47.000000 starbug2-0.3.5/starbug2.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 10:16:47.000000 starbug2-0.3.5/starbug2.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 10:16:47.000000 starbug2-0.3.5/starbug2.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-05 10:16:47.000000 starbug2-0.3.5/starbug2.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 10:16:47.834388 starbug2-0.3.5/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-04-05 10:16:31.000000 starbug2-0.3.5/tests/test_routines.py
--rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-04-05 10:16:31.000000 starbug2-0.3.5/tests/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:12.725770 starbug2-0.3.6/
+-rw-r--r--   0 runner    (1001) docker     (123)      388 2023-04-06 11:39:57.000000 starbug2-0.3.6/CITATION.cff
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-04-06 11:39:57.000000 starbug2-0.3.6/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-06 11:39:57.000000 starbug2-0.3.6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4392 2023-04-06 11:40:12.725770 starbug2-0.3.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4147 2023-04-06 11:39:57.000000 starbug2-0.3.6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:12.725770 starbug2-0.3.6/bin/
+-rwxr-xr-x   0 runner    (1001) docker     (123)    10896 2023-04-06 11:39:57.000000 starbug2-0.3.6/bin/starbug2
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3644 2023-04-06 11:39:57.000000 starbug2-0.3.6/bin/starbug2-match
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:12.725770 starbug2-0.3.6/extras/
+-rw-r--r--   0 runner    (1001) docker     (123)     1829 2023-04-06 11:39:57.000000 starbug2-0.3.6/extras/starbug2.completion
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-04-06 11:39:57.000000 starbug2-0.3.6/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      487 2023-04-06 11:40:12.725770 starbug2-0.3.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-04-06 11:39:57.000000 starbug2-0.3.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:12.725770 starbug2-0.3.6/starbug2/
+-rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-04-06 11:39:57.000000 starbug2-0.3.6/starbug2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14164 2023-04-06 11:39:57.000000 starbug2-0.3.6/starbug2/matching.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5818 2023-04-06 11:39:57.000000 starbug2-0.3.6/starbug2/misc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:12.725770 starbug2-0.3.6/starbug2/param/
+-rw-r--r--   0 runner    (1001) docker     (123)     3427 2023-04-06 11:39:57.000000 starbug2-0.3.6/starbug2/param/default.param
+-rw-r--r--   0 runner    (1001) docker     (123)    26759 2023-04-06 11:39:57.000000 starbug2-0.3.6/starbug2/routines.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28078 2023-04-06 11:39:57.000000 starbug2-0.3.6/starbug2/starbug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9301 2023-04-06 11:39:57.000000 starbug2-0.3.6/starbug2/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:12.725770 starbug2-0.3.6/starbug2.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4392 2023-04-06 11:40:12.000000 starbug2-0.3.6/starbug2.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      488 2023-04-06 11:40:12.000000 starbug2-0.3.6/starbug2.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:40:12.000000 starbug2-0.3.6/starbug2.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-04-06 11:40:12.000000 starbug2-0.3.6/starbug2.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 11:40:12.000000 starbug2-0.3.6/starbug2.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:12.725770 starbug2-0.3.6/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-04-06 11:39:57.000000 starbug2-0.3.6/tests/test_routines.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-04-06 11:39:57.000000 starbug2-0.3.6/tests/test_utils.py
```

### Comparing `starbug2-0.3.5/LICENSE.txt` & `starbug2-0.3.6/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `starbug2-0.3.5/PKG-INFO` & `starbug2-0.3.6/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,7 @@
-Metadata-Version: 2.1
-Name: starbug2
-Version: 0.3.5
-Summary: JWST PSF photometry in complex crowded fields.
-Author: Conor Nally
-Author-email: conor.nally@ed.ac.uk
-License: GNU General Public License v3.0
-Description-Content-Type: text/markdown
-
 # StarBugII
 
 JWST PSF photometry in dusty crowded fields.
 Last updated: v0.3.0
 
 [![Python application](https://github.com/conornally/starbug2/actions/workflows/python-app.yml/badge.svg)](https://github.com/conornally/starbug2/actions/workflows/python-app.yml)
 [![PyPI version fury.io](https://badge.fury.io/py/starbug2.svg)](https://pypi.python.org/pypi/starbug2/)
@@ -44,14 +35,15 @@
 ```
 
 Finally verify the installation by running `starbug2 --version`
 
 ## Usage
 
 ```bash
+
 Starbug II - JWST PSF photometry
 usage: starbug2 [-ABCDfhMPv] [-b bgdfile] [-d apfile] [-n ncores] [-o directory] [-p file.param] [-s opt=val] image.fits ...
    -A  --apphot          : run aperture photometry on a source list
    -B  --background      : run background estimation
    -b  --bgdfile         : load background (-bgd.fits) file
    -C  --clean           : run source cleaning before photometry 
    -d  --apfile  ap.fits : load a source detection (-ap.fits) file to skip the source detection step
@@ -66,27 +58,30 @@
    -P  --photom          : run psf photometry
    -s  --set      option : set value in parameter file at runtime (-s SIGSKY=3)
    -S  --subbgd          : subtract background from image
    -v  --verbose         : display verbose outputs
 
    --> Single run commands
        --init                     : Initialise Starbug (post install)
-       --generate-psf             : Generate ALL the PSF files to "PSFDIR"
        --local-param              : Make a local copy of the default parameter file
+       --update-param             : Update an out-of-date local parameter file
+       --generate-psf             : Generate ALL the PSF files to "STARBUG_DATDIR"
        --generate-region   a.fits : Make a ds9 region file with a detection file
-       --clean-table       a.fits : Clean up an individual table
        --generate-run      *.fits : Generate a simple run script
+       --clean-table       a.fits : Clean up an individual table
        --version                  : Print starbug2 version
 
    --> typical runs
       $~ starbug2 -vD -p file.param image.fits      //Source detect on image with a parameter file
       $~ starbug2 -vDM -n4 images*.fits             //Source detect and match outputs of a list of images
       $~ starbug2 -vd image-ap.fits -BP image.fits  //PSF photometry on an image with a source file (image-ap.fits)
+
 ```
 
 See [starbug-manual](https://github.com/conornally/starbug2/blob/main/docs/starbug-manual.md) for more detailed instructions.
 
 ## TODO
 
 * Need to really figure out setup.cfg to include the extras files
+* MIRI Background masking
```

### Comparing `starbug2-0.3.5/README.md` & `starbug2-0.3.6/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,7 +1,16 @@
+Metadata-Version: 2.1
+Name: starbug2
+Version: 0.3.6
+Summary: JWST PSF photometry in complex crowded fields.
+Author: Conor Nally
+Author-email: conor.nally@ed.ac.uk
+License: GNU General Public License v3.0
+Description-Content-Type: text/markdown
+
 # StarBugII
 
 JWST PSF photometry in dusty crowded fields.
 Last updated: v0.3.0
 
 [![Python application](https://github.com/conornally/starbug2/actions/workflows/python-app.yml/badge.svg)](https://github.com/conornally/starbug2/actions/workflows/python-app.yml)
 [![PyPI version fury.io](https://badge.fury.io/py/starbug2.svg)](https://pypi.python.org/pypi/starbug2/)
@@ -35,14 +44,15 @@
 ```
 
 Finally verify the installation by running `starbug2 --version`
 
 ## Usage
 
 ```bash
+
 Starbug II - JWST PSF photometry
 usage: starbug2 [-ABCDfhMPv] [-b bgdfile] [-d apfile] [-n ncores] [-o directory] [-p file.param] [-s opt=val] image.fits ...
    -A  --apphot          : run aperture photometry on a source list
    -B  --background      : run background estimation
    -b  --bgdfile         : load background (-bgd.fits) file
    -C  --clean           : run source cleaning before photometry 
    -d  --apfile  ap.fits : load a source detection (-ap.fits) file to skip the source detection step
@@ -57,27 +67,30 @@
    -P  --photom          : run psf photometry
    -s  --set      option : set value in parameter file at runtime (-s SIGSKY=3)
    -S  --subbgd          : subtract background from image
    -v  --verbose         : display verbose outputs
 
    --> Single run commands
        --init                     : Initialise Starbug (post install)
-       --generate-psf             : Generate ALL the PSF files to "PSFDIR"
        --local-param              : Make a local copy of the default parameter file
+       --update-param             : Update an out-of-date local parameter file
+       --generate-psf             : Generate ALL the PSF files to "STARBUG_DATDIR"
        --generate-region   a.fits : Make a ds9 region file with a detection file
-       --clean-table       a.fits : Clean up an individual table
        --generate-run      *.fits : Generate a simple run script
+       --clean-table       a.fits : Clean up an individual table
        --version                  : Print starbug2 version
 
    --> typical runs
       $~ starbug2 -vD -p file.param image.fits      //Source detect on image with a parameter file
       $~ starbug2 -vDM -n4 images*.fits             //Source detect and match outputs of a list of images
       $~ starbug2 -vd image-ap.fits -BP image.fits  //PSF photometry on an image with a source file (image-ap.fits)
+
 ```
 
 See [starbug-manual](https://github.com/conornally/starbug2/blob/main/docs/starbug-manual.md) for more detailed instructions.
 
 ## TODO
 
 * Need to really figure out setup.cfg to include the extras files
+* MIRI Background masking
```

### Comparing `starbug2-0.3.5/bin/starbug2` & `starbug2-0.3.6/bin/starbug2`

 * *Files 1% similar despite different names*

```diff
@@ -17,19 +17,20 @@
    -P  --photom          : run psf photometry
    -s  --set      option : set value in parameter file at runtime (-s SIGSKY=3)
    -S  --subbgd          : subtract background from image
    -v  --verbose         : display verbose outputs
 
    --> Single run commands
        --init                     : Initialise Starbug (post install)
-       --generate-psf             : Generate ALL the PSF files to "STARBUG_DATDIR"
        --local-param              : Make a local copy of the default parameter file
+       --update-param             : Update an out-of-date local parameter file
+       --generate-psf             : Generate ALL the PSF files to "STARBUG_DATDIR"
        --generate-region   a.fits : Make a ds9 region file with a detection file
-       --clean-table       a.fits : Clean up an individual table
        --generate-run      *.fits : Generate a simple run script
+       --clean-table       a.fits : Clean up an individual table
        --version                  : Print starbug2 version
 
    --> typical runs
       $~ starbug2 -vD -p file.param image.fits      //Source detect on image with a parameter file
       $~ starbug2 -vDM -n4 images*.fits             //Source detect and match outputs of a list of images
       $~ starbug2 -vd image-ap.fits -BP image.fits  //PSF photometry on an image with a source file (image-ap.fits)
 
@@ -55,14 +56,15 @@
 DOBGDSUB=0x8000
 DOGEOM  =0x10000
 
 GENRATPSF =0x100000
 GENRATRUN =0x200000
 GENRATREG =0x400000
 INITSB    =0x800000
+UPDATEPRM =0x1000000
 
 options=0
 
 pfile=None
 setdict={}
 output='.'
 ncores=1
@@ -70,15 +72,15 @@
 
 def usage():
     if not (options&VERBOSE): quit(__doc__.split('\n')[1])
     else: quit(__doc__)
 
 opts,args=getopt.getopt(sys.argv[1:],"ABCDfGhMPSvb:d:n:o:p:s:", ("apphot","background", "clean", "detect", "find", "geom", "help", "match", "photom", "subbgd", "verbose", "xtest",
                                                       "bgdfile=", "apfile=", "ncores=", "output=", "param=", "set=",
-                                                      "init", "generate-psf", "local-param", "generate-region=", "clean-table", "version", "generate-run"))
+                                                      "init", "generate-psf", "local-param", "generate-region=", "clean-table", "version", "generate-run", "update-param"))
 
 for opt,optarg in opts:
     if opt in ("-h","--help"):    usage()
     if opt in ("-p","--param"):   pfile= optarg
     if opt in ("-v","--verbose"):
         options|=VERBOSE
 
@@ -118,14 +120,16 @@
             setdict[key]=val
         else:
             perror("unable to set parameter, use syntax -s KEY=VALUE\n")
             options|=KILLPROC
 
     if opt=="--init": options|=(INITSB|STOPPROC)
     if opt=="--generate-psf": options|=(GENRATPSF|STOPPROC)
+    if opt=="--update-param": options|=(UPDATEPRM|STOPPROC)
+    if opt=="--generate-run": options|=(GENRATRUN|STOPPROC)
 
     if opt=="--local-param":
         os.system("cp %s/default.param starbug.param"%pkg_resources.resource_filename("starbug2","param/"))
         printf("--> generating starbug.param\n")
         options|=STOPPROC
 
     if opt=="--generate-region":
@@ -135,16 +139,14 @@
     if opt=="--clean-table":
         printf("cleaning table <-- %s\n"%optarg)
         table=Table.read(optarg,format="fits")#load_table(optarg)
         options|=STOPPROC
 
     if opt=="--version": quit(starbug2.logo%("starbug2-v%s"%pkg_resources.get_distribution("starbug2").version))
 
-    if opt=="--generate-run": 
-        options|=(GENRATRUN|STOPPROC)
 
 ##############################################
 # Options set, verify/run one time functions #
 ##############################################
 
 if ncores>1: options&= ~VERBOSE
 
@@ -164,14 +166,17 @@
 if options&GENRATPSF:
     generate_psfs()
 
 if options&GENRATRUN:
     cmd="starbug2 "#"+ " ".join( ["-vf"])
     generate_runscript(args, cmd)
 
+if options&UPDATEPRM:
+    update_paramfile(pfile)
+
 if options&GENRATREG:
     fname=misc.get("REGION_TAB")
     if fname and os.path.exists(fname):
         table=Table.read(fname,format="fits")
         _,name,_=split_fname(fname)
         export_region(table, colour=init_parameters["REGION_COL"], scale_radius=init_parameters["REGION_SCAL"],
                              region_radius=init_parameters["REGION_RAD"], xcol=init_parameters["REGION_XCOL"],
```

### Comparing `starbug2-0.3.5/bin/starbug2-match` & `starbug2-0.3.6/bin/starbug2-match`

 * *Files identical despite different names*

### Comparing `starbug2-0.3.5/extras/starbug2.completion` & `starbug2-0.3.6/extras/starbug2.completion`

 * *Files identical despite different names*

### Comparing `starbug2-0.3.5/starbug2/__init__.py` & `starbug2-0.3.6/starbug2/__init__.py`

 * *Files identical despite different names*

### Comparing `starbug2-0.3.5/starbug2/matching.py` & `starbug2-0.3.6/starbug2/matching.py`

 * *Files identical despite different names*

### Comparing `starbug2-0.3.5/starbug2/misc.py` & `starbug2-0.3.6/starbug2/misc.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 """
 Miscillaneous functions...
 """
 import os,stat,sys,numpy as np
+import pkg_resources
 import starbug2
 from starbug2.utils import *
 from starbug2.matching import sort_exposures
 from astropy.io import fits
 
 
 
@@ -110,7 +111,55 @@
                     s=args +"${CMDS} -n%d "%len(exps)
                     for exp in exps: s+="%s "%exp[0].header["FILENAME"]
                     fp.write("%s\n"%s)
     fp.close()
     os.chmod(RUNFILE,stat.S_IXUSR|stat.S_IWUSR|stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH)
     printf("->%s\n"%RUNFILE)
 
+
+def update_paramfile(fname):
+    """
+    When the local parameter file is from an older version, add or remove the
+    new or obselete keys
+    INPUT: fname=local file to update
+    """
+    default_fname="%s/default.param"%pkg_resources.resource_filename("starbug2","param/")
+    default_param=load_params(default_fname)
+    current_param=load_params(fname)
+
+    if default_fname==fname:
+        #perror("cannot change default parameter file")
+        return 
+
+    if os.path.exists(fname):
+        printf("Updating \"%s\"\n"%fname)
+        fpi=open(fname, 'r')
+        fpd=open(default_fname, 'r')
+        fpo=open("/tmp/starbug.param",'w')
+
+        add_keys=set(default_param.keys())-set(current_param.keys())
+        del_keys=set(current_param.keys())-set(default_param.keys())
+        if add_keys: printf("-> adding: %s  \n"%(', '.join(add_keys)))
+        if del_keys: printf("-> removing: %s\n"%(', '.join(del_keys)))
+        
+        if not len(add_keys|del_keys): 
+            printf("-> No updates needed\n")
+            return 
+
+        for inline in fpd.readlines():
+            if inline[0] in "# \t\n":
+                fpo.write(inline)
+                continue
+
+            key,value,comment=parse("{}={}//{}\n",inline)
+            key=key.strip().rstrip()
+
+            if key not in add_keys:
+                value=current_param[key]
+
+            outline="%-24s"%("%-12s"%key+"= "+str(value))+" //"+comment+"\n"
+            fpo.write(outline)
+
+        os.system("mv /tmp/starbug.param %s"%fname)
+    else: perror("local parameter file '%s' does not exist\n"%fname)
+
+
```

### Comparing `starbug2-0.3.5/starbug2/param/default.param` & `starbug2-0.3.6/starbug2/param/default.param`

 * *Files 4% similar despite different names*

```diff
@@ -3,20 +3,20 @@
 TEST = 0    //.
 
 ## GENERIC
 VERBOSE =0       // (0:false 1:true)
 OUTDIR	=. //.
 HDUNAME =  //If using a non standard HDU name, name it here (str or int)
 
-## DETECTETION - Aperture photomtry
+## DETECTETION 
 SIGSKY		=2.0  // (float>0) 
 SIGSRC		=5.0  // (float>0) Source value mininmum N sigma above background
 BOX_SIZE	=2    // (int>0) Background estimation kernal size (pix)
-#FILTER_SIZE	=3    //.
 DOBGD2D     =1    // Run background2D estimation (usually finds more sources but takes time)
+CLEANSRC    =1    // Run source cleaning after detection (removes likely contaminants)
 SHARP_LO    = 0.4 // cutoff in detection
 SHARP_HI    = 0.9 // cutoff in detection
 ROUND_LO    =-1.0 // cutoff in detection
 ROUND_HI    = 1.0 // cutoff in detection
 
 ## APERTURE PHOTOMOETRY
 APPHOT_R    =1.5   //Radius in number of pixels
@@ -46,15 +46,15 @@
 GEN_RESIDUAL=0     //generate a residual image
 
 ## SOURCE STATS
 CALC_CROWD  =1     //Run crowding metric calculation (execution time scales N^2)
 
 ## CATALOGUE MATCHING
 MATCH_THRESH =0.1  					//when combining background subtraction catalogue, minimum separation (arcsec) of centroids to be considered separate sources
-MATCH_COLS = // EXTRA columns to include in output matched table i.e sharpness
+MATCH_COLS =                        // EXTRA columns to include in output matched table i.e sharpness
 RM_MATCH =-1                        // Remove any sources with less matches than N-RM_MATCH. (if -1, keep everything)
 
 ## ARTIFICAL STARS
 NUMBER_ARTIFICIAL_STARS =500   //number of individual stars to test
 SUBIMAGE_SIZE =500             //number of pixels ? to crop around artificial star
 MIN_FLUX    =10                //minimun flux for artificial star
 MAX_FLUX    =10000             //maximum flux for artificial star
```

### Comparing `starbug2-0.3.5/starbug2/routines.py` & `starbug2-0.3.6/starbug2/routines.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,154 +1,158 @@
 """
 Routines for Starbug
 """
-import os
 import sys
 import time
 import numpy as np
 import pkg_resources
 from scipy.stats import norm#, mode
 from scipy.optimize import curve_fit
+from scipy.ndimage import convolve
+from skimage.feature import match_template
 
-from astropy.io import fits
-from astropy.stats import SigmaClip, sigma_clipped_stats, sigma_clip
-from astropy.wcs import WCS
+from astropy.stats import sigma_clipped_stats, sigma_clip
 from astropy.coordinates import SkyCoord
 from astropy.table import Column, Table, QTable, hstack
-import astropy.units as u
 from astropy.modeling.fitting import LevMarLSQFitter
+from astropy.convolution import RickerWavelet2DKernel
 
-from photutils.background import Background2D, SExtractorBackground, BackgroundBase
+from photutils.background import Background2D, BackgroundBase
 from photutils.aperture import CircularAperture, CircularAnnulus, aperture_photometry
 from photutils.detection import StarFinderBase, DAOStarFinder
 from photutils.psf.groupstars import DAOGroup
-from photutils.psf import BasicPSFPhotometry, IterativelySubtractedPSFPhotometry, FittableImageModel
-from photutils.psf.sandbox import DiscretePRF
+from photutils.psf import BasicPSFPhotometry
 
 from photutils.datasets import make_model_sources_image, make_random_models_table
-from starbug2.utils import loading, split_fname, tabppend, printf, perror, extnames, warn, export_region
+from starbug2.utils import loading, printf, perror, warn
 from starbug2 import *
 
 
 class Detection_Routine(StarFinderBase):
     """
     Detection routine- called by starbug
     A standalone detection that runs on a 2D image.
     It uses DAOStarFinder as the base for peak detection but run
     several times on a series of background subtracted images.
     Each run the background subtraction is differemt, bringing out a
     different set of sources
     """
     def __init__(self,  sig_src=5, sig_sky=3, fwhm=1,
                         sharplo=0.2, sharphi=1, roundlo=-1, roundhi=1,
-                        match_threshold=1.0, verbose=0,
-                        bgd2d=1, boxsize=2, filtersize=3):
+                        verbose=0, cleansrc=1, bgd2d=1, boxsize=2):
         self.sig_src=sig_src
         self.sig_sky=sig_sky
         self.fwhm = fwhm
         self.sharphi=sharphi
         self.sharplo=sharplo
         self.roundhi=roundhi
         self.roundlo=roundlo
+        self.cleansrc=cleansrc
 
-        self.match_threshold=u.Quantity(match_threshold)*u.dimensionless_unscaled
-        self.catalogue=None
+        #self.match_threshold=u.Quantity(match_threshold)*u.dimensionless_unscaled
+        self.catalogue=Table()
         self.verbose=verbose
 
         self.bgd2d=bgd2d
         self.boxsize=boxsize
-        self.filtersize=filtersize
+        #self.filtersize=filtersize
 
-    def detect(self, data, bkg_estimator=None, xycoords=None, clean=1):
+    def detect(self, data, bkg_estimator=None, xycoords=None):
         """
-        docstring
+        The core detection step (DAOStarFinder
+        INPUT:  
+                data=array to detect on
+                bkg_estimator=background array the same shape as data array
+                xycorrds= table of initial guesses (xcentroid,ycentroid)
+        RETURNS:
+                Sourcelist Table
         """
         bkg=np.zeros(data.shape)
         if bkg_estimator:
             bkg=bkg_estimator(data)
-            """
-            try:
-                fits.PrimaryHDU(data=data-bkg).writeto("/tmp/bgd.fits",overwrite=True)
-            except: pass
-            """
-
-        mean,median,std=sigma_clipped_stats(data,sigma=self.sig_sky)
-        if clean:
-            daofind=DAOStarFinder(std*self.sig_src, self.fwhm, sharplo=self.sharplo, sharphi=self.sharphi,
-                    roundlo=self.roundlo, roundhi=self.roundhi, peakmax=np.inf, xycoords=xycoords)
-        else: ## i dont want it to lose sharp/round values on the final run
-            daofind=DAOStarFinder(-np.inf, self.fwhm, sharplo=-np.inf, sharphi=np.inf,
-                    roundlo=-np.inf, roundhi=np.inf, peakmax=np.inf, xycoords=xycoords)
 
+        _,_,std=sigma_clipped_stats(data,sigma=self.sig_sky)
+        daofind=DAOStarFinder(std*self.sig_src, self.fwhm, sharplo=self.sharplo, sharphi=self.sharphi,
+                roundlo=self.roundlo, roundhi=self.roundhi, peakmax=np.inf, xycoords=xycoords)
         return daofind(data - bkg)
 
     def _bkg2d(self, data):
-        return Background2D(data, self.boxsize, filter_size=self.filtersize).background
+        return Background2D(data, self.boxsize, filter_size=3).background
 
     def match(self, base, cat):
         """
         Internal function to class
         Used to match detenctoins from separate background subtracted images
         into the main catalogue. This will append a source if its matched separation
         is above the threshold self.match_threshold
         """
-        #added=0
-        #b_ra, b_dec = self.wcs.all_pix2world( base["xcentroid"], base["ycentroid"], 0)
-        #c_ra, c_dec = self.wcs.all_pix2world( cat["xcentroid"], cat["ycentroid"], 0)
-
-        #base_sky=SkyCoord(b_ra*u.degree, b_dec*u.degree)
-        #cat_sky=SkyCoord(c_ra*u.degree, c_dec*u.degree)
-        #_,separation,_=cat_sky.match_to_catalog_3d(base_sky)
-        #for src,sep in zip(cat,separation):
-        #    if sep>self.match_threshold:
-        #        base.add_row(src)
-        #        added+=1
-        #return added
 
         added=0
         base_sky=SkyCoord(x=base["xcentroid"], y=base["ycentroid"], z=np.zeros(len(base)), representation_type="cartesian")
         cat_sky=SkyCoord(x=cat["xcentroid"], y=cat["ycentroid"], z=np.zeros(len(cat)), representation_type="cartesian")
         _,separation,_=cat_sky.match_to_catalog_3d(base_sky)
-        mask=(separation.to_value()>1)
         for src,sep in zip(cat,separation.to_value()):
-            if sep>1:#1 pixel?
+            if sep>self.fwhm:#1 pixel?
                 base.add_row(src)
                 added+=1
         return added
 
     def find_stars(self, data, mask=None):
         """
+        Main function of Routine
+        FUNC:
+            This routine runs source detection several times, but on a different form
+            of the data array each time. Each form has been "skewed" somehow to brighten the
+            most faint sources and flatten the differential background.
+            1- Plain detections
+            2- Subtract Background estimation
+            3- RickerWave convolution
+
+        INPUT:
+            data=array to detect on
+            mask=pixels to mask out
         """
         if data is None: return None
+        if mask is None: mask=np.where(np.isnan(data))
+        _,median,_=sigma_clipped_stats(data,sigma=self.sig_sky)
+        data[mask]=median
 
         self.catalogue=self.detect(data)
         if self.verbose: printf("-> [PLAIN] pass: %d sources\n"%len(self.catalogue))
-        sigma_clip = SigmaClip(sigma=self.sig_sky, maxiters=10)
 
-        #self.match(self.catalogue, self.detect(data, MedianBackground(sigma_clip=sigma_clip)))
+        self.match(self.catalogue, self.detect(data, self._bkg2d))
+        if self.verbose: printf("-> [BGD2D] pass: %d sources\n"%len(self.catalogue))
 
-        self.match(self.catalogue, self.detect(data, SExtractorBackground(sigma_clip=sigma_clip)))
-        if self.verbose: printf("-> [SExTr] pass: %d sources\n"%len(self.catalogue))
-
-        if self.bgd2d:
-            self.match(self.catalogue, self.detect(data, self._bkg2d))
-            if self.verbose: printf("-> [BGD2D] pass: %d sources\n"%len(self.catalogue))
+        ## 2nd order differential detection
+        kernel=RickerWavelet2DKernel(1)
+        conv=convolve(data, kernel)
+        corr=match_template(conv/np.amax(conv), kernel.array)
+        _detections=self.detect(corr)
+        _detections["xcentroid"]+=kernel.shape[0]//2
+        _detections["ycentroid"]+=kernel.shape[0]//2
+        self.match(self.catalogue, _detections)
+        if self.verbose: printf("-> [CONVL] pass: %d sources\n"%len(self.catalogue))
 
         ## Now with xycoords DAOStarfinder will refit the sharp and round values at the detected locations
         #self.catalogue=self.detect(data, xycoords=np.array([self.catalogue["xcentroid"],self.catalogue["ycentroid"]]).T)#, clean=0)
-        tmp=SourceProperties(data,self.catalogue).calculate_geometry(self.fwhm)
-        if tmp: 
-            mask=(~np.isnan(tmp["xcentroid"]) & ~np.isnan(tmp["ycentroid"]))
-            mask &= ((tmp["sharpness"]>self.sharplo)
-                    &(tmp["sharpness"]<self.sharphi)
-                    &(tmp["roundness1"]>self.roundlo)
-                    &(tmp["roundness1"]<self.roundhi)
-                    &(tmp["roundness2"]>self.roundlo)
-                    &(tmp["roundness2"]<self.roundhi))
-            self.catalogue=tmp[mask]
+        tmp=SourceProperties(data,self.catalogue, verbose=self.verbose).calculate_geometry(self.fwhm)
+        if tmp: self.catalogue=tmp
+
+        mask=(~np.isnan(self.catalogue["xcentroid"]) & ~np.isnan(self.catalogue["ycentroid"]))
+        self.catalogue.remove_rows(~mask)
+
+        mask = ((self.catalogue["sharpness"]>self.sharplo)
+               &(self.catalogue["sharpness"]<self.sharphi)
+               &(self.catalogue["roundness1"]>self.roundlo)
+               &(self.catalogue["roundness1"]<self.roundhi)
+               &(self.catalogue["roundness2"]>self.roundlo)
+               &(self.catalogue["roundness2"]<self.roundhi))
+        if self.cleansrc: 
+            if self.verbose: printf("-> cleaning %d+ unlikley point sources\n"%sum(~mask))
+            self.catalogue.remove_rows(~mask)
         
         if self.verbose: printf("Total: %d sources\n"%len(self.catalogue))
 
         self.catalogue.replace_column("id", Column(range(1,1+len(self.catalogue))))
 
         return self.catalogue
 
@@ -260,44 +264,46 @@
         if verbose:
             printf("-> best matching encircled energy %.1f, with radius %g pixels\n"%(line["eefraction"],line["radius"]))
             printf("-> using aperture correction: %f\n"%line["apcorr"])
 
         return line["apcorr"], line["radius"]
 
     def log(self,msg):
+        """
+        log message if in verbose mode
+        """
         if self.verbose: 
             printf(msg)
             sys.stdout.flush()
 
 
 class BackGround_Estimate_Routine(BackgroundBase):
     """
     """
-    bgd=None
-    sourcelist=None
     def __init__(self, sourcelist, boxsize=2, fwhm=2, verbose=0, bgd=None):#mask_r0=7, mask_r1=9
         self.sourcelist=sourcelist
         self.boxsize=boxsize
         self.fwhm=fwhm
         self.verbose=verbose
         self.bgd=bgd
+        super().__init__()
 
     def calc_peaks(self,im):
         """
         Determine peak pixel value for each source in xy
         """
         x=self.sourcelist["xcentroid"]
         y=self.sourcelist["ycentroid"]
         apertures=CircularAperture(np.array((x,y)).T,2).to_mask()
         peaks=np.full(len(x),np.nan)
         for i,mask in enumerate(apertures):
             peaks[i]=np.nanmax( mask.multiply(im) )
         return peaks
 
-    def __call__(self, data):
+    def __call__(self, data, axis=None, masked=False):
         if self.sourcelist is None or data is None: return self.bgd
         _data=np.copy(data)
         X,Y=np.ogrid[:data.shape[1], :data.shape[0]]
         peaks=self.calc_peaks(data)
 
         rlist=np.sqrt(peaks**0.7)*self.fwhm/1.5 ## <-- that works but hmm
         D=50
@@ -363,17 +369,15 @@
 
 
 class PSFPhot_Routine(BasicPSFPhotometry):
     """
     PSF Photometry routine called by starbug
     """
     def __init__(self, crit_separation, psf_model, fitshape,
-            #sig_sky=3, sig_src=5,
-            #sharplo=0.2, sharphi=1.0, roundlo=-1.0, roundhi=1.0,
-            force_fit=False, dposition_threshold=2, background=None, wcs=None, verbose=1):
+            force_fit=False, dposition_threshold=2, background=None, verbose=1):
 
         self.verbose=verbose
         self.force_fit=force_fit        
         self.dpos_thresh=dposition_threshold
 
         group_maker=_grouping(crit_separation=crit_separation)
         bkg_estimator=BackGround_Estimate_Routine(None, bgd=background)
@@ -383,42 +387,35 @@
             psf_model.fixed.update( {"x_0":True,"y_0":True} )
             if fitter.load is not None: fitter.load.msg+=" (forced)"
 
         super().__init__(group_maker=group_maker, bkg_estimator=bkg_estimator,
                 psf_model=psf_model, fitshape=fitshape,
                 finder=None, fitter=fitter)
 
-    def _bkg(self, axis=None,masked=None):
-        return self.background
-
+    #def _bkg(self, axis=None,masked=None):
+        #return self.background
 
-    #def do_photometry(self, image, init_guesses=None):
     def do_photometry(self, image, mask=None, init_guesses=None, progress_bar=False):
         """
         """ 
         _cat=None
         _fixcat=None
 
         if init_guesses is None:
             perror("Must include source list\n")
             return None
 
         if self.verbose: printf("-> fitting %d sources\n"%len(init_guesses))
         cat=super().do_photometry(image, mask=mask, init_guesses=init_guesses, progress_bar=False)
-        #cat=super().do_photometry(image, init_guesses=init_guesses)
-
-
 
-        #cat.rename_column("flux_fit","flux")
         if "flux_unc" not in cat.colnames:
             cat.add_column(Column(np.full(len(cat),np.nan), name="eflux"))
             perror("NO ERRORS??\n")
         else: cat.rename_column("flux_unc","eflux")
 
-        #cat.remove_rows( cat["flux_fit"]<=0)
         return cat
 
 class Cleaning_Routine(object):
     """
     docstring...
     """
     sharp_mu=0
```

### Comparing `starbug2-0.3.5/starbug2/starbug.py` & `starbug2-0.3.6/starbug2/starbug.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,35 +1,37 @@
 import starbug2
 from starbug2.utils import *
 from starbug2.misc import *
 from starbug2.routines import *
 
+from astropy.wcs import WCS
 from astropy.table import hstack, vstack
-from photutils.psf import EPSFModel, subtract_psf
+from photutils.psf import EPSFModel, subtract_psf, FittableImageModel
 
 
 class StarbugBase(object):
     """
     StarbugBase is the overall container for the photometry package. It holds the active image,
     the parameter file and the output images/tables.
-    It is self contained enough to simply run "photometry" and everything should just take care 
+    It is self contained enough to simply run "photometry" and everything should just take care
     of itself from there on.
     """
     filter=None
     stage=0
     fname=None
     detections=None
     psfcatalogue=None
     residuals=None
     background=None
     source_stats=None
     psf=None
 
     _image=None
     _nHDU=-1
+    _unit=None
     wcs=None
     def __init__(self, fname, pfile=None, options={}):
         """
         fname : FITS image file name
         pfile : parameter file name
         options : extra options to load into starbug
         """
@@ -82,42 +84,42 @@
         > first ImageHDU
         > image[0]
         """
         if self._nHDU >=0: return self._image[self._nHDU]
         enames=extnames(self._image)
 
         ## HDUNAME in param file
-        n=self.options["HDUNAME"] 
+        n=self.options["HDUNAME"]
         if n and n in enames:
             self._nHDU=enames.index(n)
             return self._image[n]
 
         ## SCI, BGD, RES (common names)
         for n in ("SCI","BGD","RES"):
-            if n in enames: 
+            if n in enames:
                 self._nHDU=enames.index(n)
                 return self._image[n]
 
         ## First ImageHDU
         for n,hdu in enumerate(self._image):
-            if type[hdu]==fits.ImageHDU: 
+            if type[hdu]==fits.ImageHDU:
                 self._nHDU=enames.index(n)
                 return hdu
 
         self._nHDU=0
         return self._image[0]
 
 
 
     def log(self, msg):
         """
         Print message if in verbose mode (just a macro really)
         INPUT:  msg=message to print out
         """
-        if self.options["VERBOSE"]: 
+        if self.options["VERBOSE"]:
             printf(msg)
             sys.stdout.flush()
 
 
     def load_image(self, fname):
         """
         Given fname, load the image into starbug to be worked on.
@@ -136,40 +138,41 @@
                     if ("FILTER" in self.header) and (self.header["FILTER"] in starbug2.filters.keys()):
                         self.filter=self.header["FILTER"]
                         self.log("-> photometric band: %s\n"%self.filter)
                     else: warn();perror("Unable to determine image filter\n")
 
                     if "DETECTOR" in self.info.keys():
                         self.log("-> detector module: %s\n"%self.info["DETECTOR"])
-                        
+                    if "BUNIT" in self.image.header:
+                        self._unit=self.image.header["BUNIT"]
                     self.wcs=WCS(self.image.header)
 
                     ## I NEED TO DETERMINE BETTER WHAT STAGE IT IS IN
                     exts=extnames(self._image)
                     if "DQ" in exts:
                         if "AREA" in exts: self.stage=2
                         else: self.stage=2.5
-                    elif "WHT" in exts: self.stage=3 
+                    elif "WHT" in exts: self.stage=3
                     elif "CALIBLEVEL" in self.image.header: self.stage=self.image.header["CALIBLEVEL"]
-                    else: 
+                    else:
                         warn();
                         perror("Unable to determine jwst pipeline level, assuming 3\n")
                         self.stage=3
 
 
                     #self.log("loaded: \"%s\"\n"%fname)
                     self.log("-> pipeline stage: %d\n"%self.stage)
 
                 else: warn();perror("fits file \"%s\" does not exist\n"%fname)
             else: warn();perror("included file must be FITS format\n")
 
     def load_apfile(self,fname=None):
         """
         Load a AP_FILE to be used during photometry
-        INPUT:  
+        INPUT:
             fname : file-ap.fits (this file is exported during source detection step
         """
         if not fname: fname=self.options["AP_FILE"]
         if os.path.exists(fname):
             self.detections=Table().read(fname,format="fits")#data=fp[1].data._get_raw_data())
             cn=self.detections.colnames
 
@@ -186,15 +189,15 @@
                 else: perror("WARNING, unable to determine physical coordinates from detections table\n")
             if len( set(("x_0","y_0"))&set(self.detections.colnames))==2: self.detections.rename_columns(("x_0","y_0"),("xcentroid","ycentroid"))
         else: perror("AP_FILE='%s' does not exists\n"%fname)
 
     def load_bgdfile(self,fname=None):
         """
         Load a BGD_FILE to be used during photometry
-        INPUT:  
+        INPUT:
             fname : file-bgd.fits (this file is exported during background estimation step
         """
         if not fname: fname=self.options["BGD_FILE"]
         if os.path.exists(fname):
             self.background=fits.open(fname)[1]
             self.log("loaded BGD_FILE='%s'\n"%fname)
         else: perror("BGD_FILE='%s' does not exist\n"%fname)
@@ -205,26 +208,27 @@
         INPUT:
             fname : psf.fits
         """
         status=0
         if not fname:
             fltr=starbug2.filters[self.filter]
             dtname=self.info["DETECTOR"]
+            #print(dtname)
             if dtname=="MULTIPLE":
                 if   fltr.instr==starbug2.NIRCAM and fltr.length==starbug2.SHORT: dtname="NRCA1"
                 elif fltr.instr==starbug2.NIRCAM and fltr.length==starbug2.LONG:  dtname="NRCALONG"
                 elif fltr.instr==starbug2.MIRI:  dtname=""
             if dtname=="MIRIMAGE": dtname=""
             fname="%s/%s%s.fits"%(starbug2.DATDIR,self.filter,dtname)
         if os.path.exists(fname):
             fp=fits.open(fname)
             self.psf=fp[1].data ####hmm
             fp.close()
             self.log("loaded PSF_FILE='%s'\n"%(fname))
-        else: 
+        else:
             perror("PSF_FILE='%s' does not exist\n"%fname)
             status=1
         return status
 
 
     def detect(self):
         """
@@ -239,17 +243,18 @@
                                         fwhm=FWHM,
                                         sharplo=self.options["SHARP_LO"],
                                         sharphi=self.options["SHARP_HI"],
                                         roundlo=self.options["ROUND_LO"],
                                         roundhi=self.options["ROUND_HI"],
                                         bgd2d=self.options["DOBGD2D"],
                                         boxsize=int(self.options["BOX_SIZE"]),
+                                        cleansrc=self.options["CLEANSRC"],
                                         verbose=self.options["VERBOSE"])
 
-            self.detections=detector(self.image.data)["xcentroid","ycentroid","sharpness","roundness1","roundness2"]
+            self.detections=detector(self.image.data.copy())["xcentroid","ycentroid","sharpness","roundness1","roundness2"]
 
             ra,dec=self.wcs.all_pix2world(self.detections["xcentroid"], self.detections["ycentroid"],0)
             self.detections.add_column( Column(ra, name="RA"), index=1)
             self.detections.add_column( Column(dec, name="DEC"), index=2)
             self.aperture_photometry()
 
             self.detections.meta=dict(self.header.items())
@@ -259,29 +264,29 @@
     def aperture_photometry(self):
 
         if self.detections is None:
             perror("No detection source file loaded (-d file-ap.fits)\n")
             return
         if len(set(("x_0","y_0","xcentroid","ycentroid")) & set(self.detections.colnames))<2:
             perror("No pixel coordinates in source file\n")
-            return 
+            return
 
         new_columns=("flux","eflux","sky", "flag", self.filter,"e%s"%self.filter)
         self.detections.remove_columns( set(new_columns)&set(self.detections.colnames) )
 
 
         #######################
         # APERTURE PHOTOMETRY #
         #######################
         self.log("Running Aperture Photometry\n")
         image=self.image.data.copy() ##dont work on the real image!
 
-        ######################### 
+        #########################
         # Unit Conversion to Jy #
-        ######################### 
+        #########################
         error=None
 
         scalefactor=get_MJysr2Jy_scalefactor(self.image)
         self.log("-> converting unit from MJy/sr to Jr with factor: %e\n"%scalefactor)
         #if self._image["SCI"].header["BUNIT"]=="MJy/sr":
             #scalefactor=1e6*float(self._image["SCI"].header["PIXAR_SR"])
 
@@ -328,42 +333,40 @@
 
     def bgd_estimate(self):
         """
         Estimate the background of the active image
         Saves the result as an ImageHDU self.background
         """
         self.log("Estimating Background\n")
-        #image=self._image["SCI"].data.copy() / self._image["SCI"].header["PHOTMJSR"]
         if self.detections:
             xname="xcentroid" if "xcentroid" in self.detections.colnames else "x_0"
             yname="ycentroid" if "ycentroid" in self.detections.colnames else "y_0"
 
             sources=self.detections[[xname,yname]]
             sources=sources[ sources[xname]>=0 ]
             sources=sources[ sources[yname]>=0 ]
             sources=sources[ sources[xname]<self.image.header["NAXIS1"]]
             sources=sources[ sources[yname]<self.image.header["NAXIS2"]]
-            bgd=BackGround_Estimate_Routine(sources, 
+            bgd=BackGround_Estimate_Routine(sources,
                                             boxsize=int(self.options["BOX_SIZE"]),
-                                            #fwhm=starbug2.filters[self.filter][2],
                                             fwhm=starbug2.filters[self.filter].pFWHM,
                                             verbose=self.options["VERBOSE"])
-            self.background=fits.ImageHDU(data=bgd(self.image.data), header=self.wcs.to_header())
+            self.background=fits.ImageHDU(data=bgd(self.image.data.copy()), header=self.wcs.to_header())
         else:
             perror("unable to estimate background, no source list loaded\n")
 
     def bgd_subtraction(self):
         """
         Internally subtract a background array from an image array
         """
         self.log("Subtracting Background\n")
 
         if self.background is None:
             perror("No background array loaded (-b file-bgd.fits)\n")
-            return 
+            return
         array= self.image.data - self.background.data
         self.residuals = array
         self._image[self._nHDU].data=array
 
     def photometry(self):
         """
         Full photometry routine
@@ -385,16 +388,23 @@
         if self.image:
             self.log("Running PSF Photometry\n")
 
             ###################################
             # Collect relevent files and data #
             ###################################
 
-            image=self.image.data.copy()/ self.image.header["PHOTMJSR"] #https://spacetelescope.github.io/jdat_notebooks/notebooks/psf_photometry/NIRCam_PSF_Photometry_Example.html
-            bgd = self.background.data.copy() / self.image.header["PHOTMJSR"] 
+            image=self.image.data.copy()
+            bgd = self.background.data.copy()
+
+            _bunit=self.image.header.get("BUNIT")
+            _scalefactor=self.image.header.get("PHOTMJSR")
+            if _scalefactor:#https://spacetelescope.github.io/jdat_notebooks/notebooks/psf_photometry/NIRCam_PSF_Photometry_Example.html
+                self.log("-> PHOTMJSR: %f\n"%_scalefactor)
+                image/=_scalefactor
+                bgd/=_scalefactor
 
             psf_model=FittableImageModel(self.psf)
             #psf_model=EPSFModel(fp[1].data)
             if self.options["PSF_SIZE"]>0: size=int(self.options["PSF_SIZE"])
             else: size=psf_model.shape[0]
             if not size%2: size-=1
             self.log("-> psf size: %d\n"%size)
@@ -413,27 +423,28 @@
             init_guesses=init_guesses[ init_guesses["y_0"]<self.image.header["NAXIS2"]]
             init_guesses=init_guesses[["x_0","y_0","flux",self.filter, "flag"]]
             init_guesses.remove_column("flux")
             #init_guesses.rename_column("flux","flux_0")
             init_guesses.rename_column(self.filter,"ap_%s"%self.filter)
             #init_guesses=init_guesses[init_guesses["flux_0"]>0]
             #init_guesses.remove_column("flux_0")
-            
+
             ###########
             # Run Fit #
             ###########
 
             _psf_cat=None
             _fixpsf_cat=None
 
             if not self.options["FORCE_POS"]:
                 dpos= self.options["DPOS_THRESH"] / np.sqrt( self.image.header["PIXAR_A2"])
                 self.log("-> position fit threshold [pix]: %.2g\n"%dpos)
                 phot=PSFPhot_Routine(self.options["CRIT_SEP"], psf_model, size, background=bgd, force_fit=0, verbose=self.options["VERBOSE"])
                 _psf_cat=phot(image,init_guesses=init_guesses)
+
                 d = (_psf_cat["x_0"]-_psf_cat["x_fit"])**2.0 + (_psf_cat["y_0"]-_psf_cat["y_fit"])**2.0
                 ii=np.where(d>=dpos**2.0)
                 init_guesses=init_guesses[ii]
                 _psf_cat.remove_rows(ii)
                 if len(init_guesses): self.log("-> number bad position fits: %d\n"%len(init_guesses))
 
             if len(init_guesses):
@@ -445,15 +456,14 @@
             elif _psf_cat is None: psf_cat=_fixpsf_cat
             else: psf_cat=_psf_cat
 
             ra,dec=self.wcs.all_pix2world(psf_cat["x_fit"], psf_cat["y_fit"],0)
             psf_cat.add_column( Column(ra, name="RA"), index=1)
             psf_cat.add_column( Column(dec, name="DEC"), index=2)
 
-
             ##################
             # Residual Image #
             ##################
 
             if self.options["GEN_RESIDUAL"]:
                 self.log("-> generating residual\n")
                 residual = subtract_psf(image-bgd, psf_model, psf_cat[["x_fit","y_fit","flux_fit"]], subshape=(size,size))
@@ -472,15 +482,15 @@
             #mag-=dmag
             #self.log("Photometric offset: %f\n"%dmag)
 
             psf_cat.add_column(mag,name=self.filter)
             psf_cat.add_column(magerr,name="e%s"%self.filter)
             self.psfcatalogue=tabppend(self.psfcatalogue, psf_cat)
             self.psfcatalogue.meta=dict(self.header.items())
-            self.background=fits.ImageHDU(data=phot.bkg_estimator.bgd, name="BACKGROUND", header=self.wcs.to_header()) ##So is it supposed to be a fits image or a numpy array?!
+            #self.background=fits.ImageHDU(data=phot.bkg_estimator.bgd, name="BACKGROUND", header=self.wcs.to_header()) ##So is it supposed to be a fits image or a numpy array?!
 
     def cleanup(self):
         """
         """
         self.log("Cleaning up..\n")
 
         if self.detections:
@@ -544,51 +554,37 @@
         """
         if not outdir: outdir=self.options["OUTDIR"]
         if not os.path.exists("%s/"%outdir):
             perror("output directory '%s' does not exist, using /tmp instead\n"%outdir)
             outdir="/tmp"
 
         dname,fname,ext=split_fname(self.fname)
-        if self.detections: 
+        if self.detections:
             self.detections.meta["FILTER"]=self.filter
             reindex(self.detections)
             hdulist=[fits.PrimaryHDU(header=self.header),fits.BinTableHDU(data=self.detections)]
             fits.HDUList(hdulist).writeto("%s/%s-ap.fits"%(outdir,fname), overwrite=True)
             #export_table(self.detections, fname="%s/%s-ap.fits"%(outdir,fname))
-        if self.psfcatalogue: 
+        if self.psfcatalogue:
             reindex(self.psfcatalogue)
             hdulist=[fits.PrimaryHDU(header=self.header),fits.BinTableHDU(data=self.psfcatalogue)]
             fits.HDUList(hdulist).writeto("%s/%s-psf.fits"%(outdir,fname), overwrite=True)
             #export_table(self.psfcatalogue, fname="%s/%s-psf.fits"%(outdir,fname))
-        
         if self.background: 
             #self.background.header.update(header)
             self.background.writeto("%s/%s-bgd.fits"%(outdir,fname), overwrite=True)
-
         if self.residuals is not None:
             im=fits.ImageHDU(data=self.residuals, name="RES", header=self.header)
             im.header.update(self.wcs.to_header())
             im.writeto("%s/%s-res.fits"%(outdir,fname), overwrite=True)
-
         if self.source_stats is not None:
             reindex(self.source_stats)
             hdulist=[fits.PrimaryHDU(header=self.header),fits.BinTableHDU(data=self.source_stats)]
             fits.HDUList(hdulist).writeto("%s/%s-stat.fits"%(outdir,fname), overwrite=True)
 
-        #hdulist=[fits.PrimaryHDU(header=header)]
-        #hdulist=[fits.PrimaryHDU()]
-        #for n,res in enumerate(self.residuals,1):
-        #    im=fits.ImageHDU(data=res,name="RESIDUAL%d"%n, header=self.header)#self.wcs.to_header())
-        #    im.header.update(self.header)
-        #    #im.header.update(header)
-        #    hdulist.append(im)
-
-        #if len(hdulist)>1: 
-        #    fits.HDUList(hdulist).writeto("%s/%s-res.fits"%(outdir,fname), overwrite=True)
-
     def source_geometry(self):
         """
         Calculate source geometry stats for a given image and source list
         """
         if self.detections is None: perror("No source file loaded\n")
         else:
             self.log("Running Source Geometry\n")
@@ -638,15 +634,15 @@
             warn()
             perror("Unable to locate OUTDIR='%s'\n"%dname)
             status=1
 
         tmp=load_params("%sdefault.param"%pkg_resources.resource_filename("starbug2","param/"))
         if set(tmp.keys()) - set(self.options.keys()):
             warn()
-            perror("parameter file version mismatch. Run starbug --local-param to update\n")
+            perror("parameter file version mismatch. Run starbug --update-param to update\n")
             status=1
 
         return status
 
     def __getstate__(self):
         state=self.__dict__.copy()
         if "_image" in state:
```

### Comparing `starbug2-0.3.5/starbug2/utils.py` & `starbug2-0.3.6/starbug2/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -133,15 +133,16 @@
             for line in fp.readlines():
                 if line[0] in "# \t\n":
                     continue
                 key,value,_=parse("{}={}//{}\n",line)
                 key=key.strip()
                 value=value.strip()
                 try:
-                    value=float(value)
+                    if '.' in value: value=float(value)
+                    else: value=int(value)
                 except:
                     pass
 
                 ## Special case values
                 if key in ("AP_FILE","BGD_FILE","PSF_FILE"): value=os.path.expandvars(value)
                 config[key]=value
     else:
```

### Comparing `starbug2-0.3.5/starbug2.egg-info/PKG-INFO` & `starbug2-0.3.6/starbug2.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: starbug2
-Version: 0.3.5
+Version: 0.3.6
 Summary: JWST PSF photometry in complex crowded fields.
 Author: Conor Nally
 Author-email: conor.nally@ed.ac.uk
 License: GNU General Public License v3.0
 Description-Content-Type: text/markdown
 
 # StarBugII
@@ -44,14 +44,15 @@
 ```
 
 Finally verify the installation by running `starbug2 --version`
 
 ## Usage
 
 ```bash
+
 Starbug II - JWST PSF photometry
 usage: starbug2 [-ABCDfhMPv] [-b bgdfile] [-d apfile] [-n ncores] [-o directory] [-p file.param] [-s opt=val] image.fits ...
    -A  --apphot          : run aperture photometry on a source list
    -B  --background      : run background estimation
    -b  --bgdfile         : load background (-bgd.fits) file
    -C  --clean           : run source cleaning before photometry 
    -d  --apfile  ap.fits : load a source detection (-ap.fits) file to skip the source detection step
@@ -66,27 +67,30 @@
    -P  --photom          : run psf photometry
    -s  --set      option : set value in parameter file at runtime (-s SIGSKY=3)
    -S  --subbgd          : subtract background from image
    -v  --verbose         : display verbose outputs
 
    --> Single run commands
        --init                     : Initialise Starbug (post install)
-       --generate-psf             : Generate ALL the PSF files to "PSFDIR"
        --local-param              : Make a local copy of the default parameter file
+       --update-param             : Update an out-of-date local parameter file
+       --generate-psf             : Generate ALL the PSF files to "STARBUG_DATDIR"
        --generate-region   a.fits : Make a ds9 region file with a detection file
-       --clean-table       a.fits : Clean up an individual table
        --generate-run      *.fits : Generate a simple run script
+       --clean-table       a.fits : Clean up an individual table
        --version                  : Print starbug2 version
 
    --> typical runs
       $~ starbug2 -vD -p file.param image.fits      //Source detect on image with a parameter file
       $~ starbug2 -vDM -n4 images*.fits             //Source detect and match outputs of a list of images
       $~ starbug2 -vd image-ap.fits -BP image.fits  //PSF photometry on an image with a source file (image-ap.fits)
+
 ```
 
 See [starbug-manual](https://github.com/conornally/starbug2/blob/main/docs/starbug-manual.md) for more detailed instructions.
 
 ## TODO
 
 * Need to really figure out setup.cfg to include the extras files
+* MIRI Background masking
```

### Comparing `starbug2-0.3.5/tests/test_routines.py` & `starbug2-0.3.6/tests/test_routines.py`

 * *Files identical despite different names*

### Comparing `starbug2-0.3.5/tests/test_utils.py` & `starbug2-0.3.6/tests/test_utils.py`

 * *Files identical despite different names*

