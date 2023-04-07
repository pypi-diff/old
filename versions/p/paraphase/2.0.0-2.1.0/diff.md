# Comparing `tmp/paraphase-2.0.0.tar.gz` & `tmp/paraphase-2.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "paraphase-2.0.0.tar", last modified: Sat Mar 11 03:03:35 2023, max compression
+gzip compressed data, was "paraphase-2.1.0.tar", last modified: Fri Apr  7 03:41:14 2023, max compression
```

## Comparing `paraphase-2.0.0.tar` & `paraphase-2.1.0.tar`

### file list

```diff
@@ -1,88 +1,92 @@
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:35.280345 paraphase-2.0.0/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     1675 2022-10-20 20:09:26.000000 paraphase-2.0.0/LICENSE
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     7224 2023-03-11 03:03:35.278351 paraphase-2.0.0/PKG-INFO
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     6894 2023-03-11 01:37:23.000000 paraphase-2.0.0/README.md
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.504341 paraphase-2.0.0/paraphase/
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)       19 2022-10-20 17:37:48.000000 paraphase-2.0.0/paraphase/__init__.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       67 2022-12-06 22:33:14.000000 paraphase-2.0.0/paraphase/__main__.py
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.535148 paraphase-2.0.0/paraphase/data/
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.573853 paraphase-2.0.0/paraphase/data/cfc1/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)      395 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/cfc1/cfc1_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    20766 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/cfc1/homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    23411 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/cfc1/ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/cfc1/ref.fa.fai
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.585147 paraphase-2.0.0/paraphase/data/f8/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)      441 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/f8/f8_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     8586 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/f8/homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    11204 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/f8/ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/f8/ref.fa.fai
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     2352 2022-10-20 17:37:49.000000 paraphase-2.0.0/paraphase/data/genome_region.bed
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.717339 paraphase-2.0.0/paraphase/data/ikbkg/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    12998 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ikbkg/homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)      726 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ikbkg/ikbkg_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    19751 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ikbkg/ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ikbkg/ref.fa.fai
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.759158 paraphase-2.0.0/paraphase/data/ncf1/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    40348 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ncf1/homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)      612 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ncf1/ncf1_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    24426 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ncf1/ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/ncf1/ref.fa.fai
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.802400 paraphase-2.0.0/paraphase/data/neb/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    11794 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/neb/homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)      460 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/neb/neb_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    10225 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/neb/ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/neb/ref.fa.fai
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.823131 paraphase-2.0.0/paraphase/data/pms2/
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      501 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/pms2/pms2_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    21990 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/pms2/pms2_homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    25949 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/pms2/pms2_ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       36 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/pms2/pms2_ref.fa.fai
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.837133 paraphase-2.0.0/paraphase/data/rccx/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)      256 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/rccx/cyp21_diff_sites.txt
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      844 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/rccx/rccx_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    30104 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/rccx/rccx_homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    36382 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/rccx/rccx_ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/rccx/rccx_ref.fa.fai
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:35.104704 paraphase-2.0.0/paraphase/data/smn1/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    78194 2022-10-20 17:37:49.000000 paraphase-2.0.0/paraphase/data/smn1/homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)   657457 2022-10-20 17:37:49.000000 paraphase-2.0.0/paraphase/data/smn1/known_haplotypes.json
--rw-r--r--   0 xchen    (71795) Domain Users (10513) 10776692 2023-03-09 18:01:15.000000 paraphase-2.0.0/paraphase/data/smn1/ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       41 2023-03-09 18:01:17.000000 paraphase-2.0.0/paraphase/data/smn1/ref.fa.fai
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    48846 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/smn1/ref_smn2.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/smn1/ref_smn2.fa.fai
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      968 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/smn1/smn1_config.yaml
--rw-r--r--   0 xchen    (71795) Domain Users (10513)  1584900 2022-10-20 17:37:49.000000 paraphase-2.0.0/paraphase/data/smn1/smn_matching_pos.txt
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:35.133116 paraphase-2.0.0/paraphase/data/strc/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    20334 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/strc/homopolymer_sites.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    21377 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/strc/ref.fa
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       39 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/strc/ref.fa.fai
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      667 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/data/strc/strc_config.yaml
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:35.243347 paraphase-2.0.0/paraphase/genes/
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/genes/__init__.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     3096 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/genes/cfc1_phaser.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     6304 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/genes/f8_phaser.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     6494 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/genes/ikbkg_phaser.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     4452 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/genes/ncf1_phaser.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     5012 2023-03-11 01:37:23.000000 paraphase-2.0.0/paraphase/genes/neb_phaser.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     3103 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/genes/pms2_phaser.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)    25912 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/genes/rccx_phaser.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    25425 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/genes/smn1_phaser.py
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     4833 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/genes/strc_phaser.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     1161 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/genome_depth.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    47635 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/haplotype_assembler.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    11837 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/paraphase.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    34312 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/phaser.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    27751 2023-03-11 01:37:24.000000 paraphase-2.0.0/paraphase/prepare_bam_and_vcf.py
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:34.542864 paraphase-2.0.0/paraphase.egg-info/
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     7224 2023-03-11 03:03:32.000000 paraphase-2.0.0/paraphase.egg-info/PKG-INFO
--rw-r--r--   0 xchen    (71795) Domain Users (10513)     2269 2023-03-11 03:03:33.000000 paraphase-2.0.0/paraphase.egg-info/SOURCES.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)        1 2023-03-11 03:03:32.000000 paraphase-2.0.0/paraphase.egg-info/dependency_links.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       55 2023-03-11 03:03:32.000000 paraphase-2.0.0/paraphase.egg-info/entry_points.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       45 2023-03-11 03:03:33.000000 paraphase-2.0.0/paraphase.egg-info/requires.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       10 2023-03-11 03:03:33.000000 paraphase-2.0.0/paraphase.egg-info/top_level.txt
--rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-03-11 03:03:35.281342 paraphase-2.0.0/setup.cfg
--rw-r--r--   0 xchen    (71795) Domain Users (10513)      816 2023-03-11 01:56:22.000000 paraphase-2.0.0/setup.py
-drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-03-11 03:03:35.264357 paraphase-2.0.0/tests/
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    16147 2023-03-11 01:37:24.000000 paraphase-2.0.0/tests/test_haplotype_assembler.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     5560 2023-03-11 01:37:24.000000 paraphase-2.0.0/tests/test_phaser.py
--rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     7921 2023-03-11 01:37:24.000000 paraphase-2.0.0/tests/test_smn1_phaser.py
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:14.535842 paraphase-2.1.0/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     1675 2022-10-20 20:09:26.000000 paraphase-2.1.0/LICENSE
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     7224 2023-04-07 03:41:14.534854 paraphase-2.1.0/PKG-INFO
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     6894 2023-03-11 03:44:27.000000 paraphase-2.1.0/README.md
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:12.996913 paraphase-2.1.0/paraphase/
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)       22 2023-04-06 23:04:32.000000 paraphase-2.1.0/paraphase/__init__.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       67 2023-04-06 16:01:02.000000 paraphase-2.1.0/paraphase/__main__.py
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.054910 paraphase-2.1.0/paraphase/data/
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.195904 paraphase-2.1.0/paraphase/data/cfc1/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)      395 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/cfc1/cfc1_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    20766 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/cfc1/homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    23411 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/cfc1/ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/cfc1/ref.fa.fai
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.243910 paraphase-2.1.0/paraphase/data/f8/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)      441 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/f8/f8_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     8586 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/f8/homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    11204 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/f8/ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/f8/ref.fa.fai
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     2352 2022-10-20 17:37:49.000000 paraphase-2.1.0/paraphase/data/genome_region.bed
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.358895 paraphase-2.1.0/paraphase/data/ikbkg/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    12998 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/ikbkg/homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)      726 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/ikbkg/ikbkg_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    19751 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/ikbkg/ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/ikbkg/ref.fa.fai
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.506907 paraphase-2.1.0/paraphase/data/ncf1/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    40348 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/ncf1/homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)      457 2023-03-29 22:16:27.000000 paraphase-2.1.0/paraphase/data/ncf1/ncf1_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    61026 2023-03-29 20:13:13.000000 paraphase-2.1.0/paraphase/data/ncf1/ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-03-29 20:13:19.000000 paraphase-2.1.0/paraphase/data/ncf1/ref.fa.fai
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.596883 paraphase-2.1.0/paraphase/data/neb/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    11794 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/neb/homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)      412 2023-03-28 20:33:47.000000 paraphase-2.1.0/paraphase/data/neb/neb_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    10225 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/neb/ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       40 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/neb/ref.fa.fai
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.660885 paraphase-2.1.0/paraphase/data/pms2/
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      501 2023-03-27 19:15:03.000000 paraphase-2.1.0/paraphase/data/pms2/pms2_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    21990 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/pms2/pms2_homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    53907 2023-03-23 19:24:34.000000 paraphase-2.1.0/paraphase/data/pms2/pms2_ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       36 2023-03-23 19:24:39.000000 paraphase-2.1.0/paraphase/data/pms2/pms2_ref.fa.fai
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.734878 paraphase-2.1.0/paraphase/data/rccx/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)      256 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/rccx/cyp21_diff_sites.txt
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      780 2023-03-28 21:38:54.000000 paraphase-2.1.0/paraphase/data/rccx/rccx_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    30104 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/rccx/rccx_homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    36382 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/rccx/rccx_ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/rccx/rccx_ref.fa.fai
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:14.140870 paraphase-2.1.0/paraphase/data/smn1/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    78194 2022-10-20 17:37:49.000000 paraphase-2.1.0/paraphase/data/smn1/homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)   657457 2022-10-20 17:37:49.000000 paraphase-2.1.0/paraphase/data/smn1/known_haplotypes.json
+-rw-r--r--   0 xchen    (71795) Domain Users (10513) 10776692 2023-03-09 18:01:15.000000 paraphase-2.1.0/paraphase/data/smn1/ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       41 2023-03-09 18:01:17.000000 paraphase-2.1.0/paraphase/data/smn1/ref.fa.fai
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    48846 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/smn1/ref_smn2.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/smn1/ref_smn2.fa.fai
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      968 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/smn1/smn1_config.yaml
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)  1584900 2022-10-20 17:37:49.000000 paraphase-2.1.0/paraphase/data/smn1/smn_matching_pos.txt
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:14.278856 paraphase-2.1.0/paraphase/data/strc/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    20334 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/strc/homopolymer_sites.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    21377 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/strc/ref.fa
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       39 2023-03-11 03:44:27.000000 paraphase-2.1.0/paraphase/data/strc/ref.fa.fai
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)      693 2023-04-06 17:41:33.000000 paraphase-2.1.0/paraphase/data/strc/strc_config.yaml
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:14.428849 paraphase-2.1.0/paraphase/genes/
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-06 16:01:12.000000 paraphase-2.1.0/paraphase/genes/__init__.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     2978 2023-03-31 14:46:10.000000 paraphase-2.1.0/paraphase/genes/cfc1_phaser.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     6357 2023-03-30 18:11:44.000000 paraphase-2.1.0/paraphase/genes/f8_phaser.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     6974 2023-04-06 22:45:14.000000 paraphase-2.1.0/paraphase/genes/ikbkg_phaser.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     4416 2023-04-06 18:44:52.000000 paraphase-2.1.0/paraphase/genes/ncf1_phaser.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     5079 2023-04-06 18:45:09.000000 paraphase-2.1.0/paraphase/genes/neb_phaser.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     3172 2023-04-06 19:57:52.000000 paraphase-2.1.0/paraphase/genes/pms2_phaser.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    26027 2023-04-07 03:09:01.000000 paraphase-2.1.0/paraphase/genes/rccx_phaser.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    25358 2023-03-31 14:47:50.000000 paraphase-2.1.0/paraphase/genes/smn1_phaser.py
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     5466 2023-04-06 22:46:57.000000 paraphase-2.1.0/paraphase/genes/strc_phaser.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     1063 2023-03-28 22:28:30.000000 paraphase-2.1.0/paraphase/genome_depth.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    47635 2023-03-11 03:44:28.000000 paraphase-2.1.0/paraphase/haplotype_assembler.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    11846 2023-04-06 16:01:06.000000 paraphase-2.1.0/paraphase/paraphase.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    44876 2023-04-07 02:36:41.000000 paraphase-2.1.0/paraphase/phaser.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    29281 2023-04-06 20:02:04.000000 paraphase-2.1.0/paraphase/prepare_bam_and_vcf.py
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:13.042920 paraphase-2.1.0/paraphase.egg-info/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     7224 2023-04-07 03:41:10.000000 paraphase-2.1.0/paraphase.egg-info/PKG-INFO
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     2269 2023-04-07 03:41:11.000000 paraphase-2.1.0/paraphase.egg-info/SOURCES.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)        1 2023-04-07 03:41:10.000000 paraphase-2.1.0/paraphase.egg-info/dependency_links.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       55 2023-04-07 03:41:10.000000 paraphase-2.1.0/paraphase.egg-info/entry_points.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       45 2023-04-07 03:41:10.000000 paraphase-2.1.0/paraphase.egg-info/requires.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       10 2023-04-07 03:41:10.000000 paraphase-2.1.0/paraphase.egg-info/top_level.txt
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)       38 2023-04-07 03:41:14.536843 paraphase-2.1.0/setup.cfg
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)      816 2023-04-06 23:05:03.000000 paraphase-2.1.0/setup.py
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:14.491843 paraphase-2.1.0/tests/
+drwxr-xr-x   0 xchen    (71795) Domain Users (10513)        0 2023-04-07 03:41:19.878099 paraphase-2.1.0/tests/__pycache__/
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    24662 2023-04-07 03:41:19.398129 paraphase-2.1.0/tests/__pycache__/test_haplotype_assembler.cpython-38-pytest-7.1.2.pyc
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)     8518 2023-04-07 03:41:19.493133 paraphase-2.1.0/tests/__pycache__/test_phaser.cpython-38-pytest-7.1.2.pyc
+-rw-r--r--   0 xchen    (71795) Domain Users (10513)    10959 2023-04-07 03:41:19.878112 paraphase-2.1.0/tests/__pycache__/test_smn1_phaser.cpython-38-pytest-7.1.2.pyc
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)    16147 2023-03-11 01:37:24.000000 paraphase-2.1.0/tests/test_haplotype_assembler.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     5560 2023-03-11 03:44:28.000000 paraphase-2.1.0/tests/test_phaser.py
+-rwxr-xr-x   0 xchen    (71795) Domain Users (10513)     7921 2023-03-11 03:44:28.000000 paraphase-2.1.0/tests/test_smn1_phaser.py
```

### Comparing `paraphase-2.0.0/LICENSE` & `paraphase-2.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/PKG-INFO` & `paraphase-2.1.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: paraphase
-Version: 2.0.0
+Version: 2.1.0
 Summary: paraphase: HiFi-based caller for highly homologous genes
 Home-page: https://github.com/PacificBiosciences/paraphase
 Author: Xiao Chen
 Author-email: xchen@pacificbiosciences.com
 License: BSD-3-Clause-Clear
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `paraphase-2.0.0/README.md` & `paraphase-2.1.0/README.md`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/cfc1/homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/cfc1/homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/cfc1/ref.fa` & `paraphase-2.1.0/paraphase/data/cfc1/ref.fa`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/f8/homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/f8/homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/f8/ref.fa` & `paraphase-2.1.0/paraphase/data/f8/ref.fa`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/genome_region.bed` & `paraphase-2.1.0/paraphase/data/genome_region.bed`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/ikbkg/homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/ikbkg/homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/ikbkg/ikbkg_config.yaml` & `paraphase-2.1.0/paraphase/data/ikbkg/ikbkg_config.yaml`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/ikbkg/ref.fa` & `paraphase-2.1.0/paraphase/data/ikbkg/ref.fa`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/ncf1/homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/ncf1/homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/ncf1/ref.fa` & `paraphase-2.1.0/paraphase/data/strc/ref.fa`

 * *Files 17% similar despite different names*

```diff
@@ -1,402 +1,352 @@
->chr7_74768800_74792800
-GCGGCGGGGTGCAGGGGGCCCTTCCTATTAGCACTCGGGACGTGGGGGAATTCTTGGGGC
-CCTGGTATTGTTCTAACACCCAGTGATGGTTCACCAGCTGTCTCCTTTATAATAATTAGG
-TAAGAGATGTGGTTTTCTACATATTTCACAATACAAACATTTTTAGAAATTCTATTTCCT
-TCCCCTGAAAAAACTCTCTTATCTCTTTATTACTTCCTTCCTTAACTTTATTTTATTTTA
-TTTTATTTATTTATTTTTTGAAACCAAGTCTACTCTGTTACCCAGCCTGGAGTGCAGTGG
-TGTGATCTCGGCTCACTGCAACCTCTGCCTCCCAGGTTCAAGCGATTCTTCTGCCTCAGC
-CTCCCAAGTAGCTGGGATTATAGGCTTGCAATGCCATGCCTGGCTAATTTTTTTATTTTT
-AGTAGAGACCCGGTTTCACCGTGTTGGCCAAGCTGGTCCCGAACTCCTGACCTCAGATGA
-CCCACCCACCTTGGCCTCCCAAAGTGCTGGAATTACAGGCATGAGCCACTGCACCTATCT
-TTTTTTTTTTAATTAAAAAAATTATTTGGTACCTTGTTTCATCCATGCATTAAATTAAAT
-CCTGGCCAGACACAGTGGCTTATGCCTGTAATCCCAGCATTTTGGGAGGCTGAGGTGGGA
-GGACCACTTGATACTGGAGCTTGAGACCAGGCCGAGCAGCATCTCGAGACCCCGTCTCTA
-CAAAAAAAAAATAATAATAATAATAATAATAAATAAAAAGTGGAAAAAATCCTATGTCAT
-CCTGAAAAAAGGCTGTAAGCCTGCTTACAGAGGTCATTACAAGGTCAAACTCAAGTTCGG
-AGCGCTTCCTGCCTCTGCTCATCCAACAAACTTGCTGGATACCTCCTGTCTGCAGAGCAC
-TTTGAGGGAACATAACAGGGTCTTGGGAGGCCACAGGAGGAGAGTTGAAAGATCACAGCC
-AGGGGCTCAGGGTGTCCACAGGACAAGTACCCTTGGCCAGGCAGTTACGCAAGTGTGGAA
-AGACTGCTAGAGGAAGGGAAGGAAGTGCCGAGAGCCCACAAAATTCTCTGCTTACAACCA
-GCCCCACTAGAACCTTCCTCTGCCCTGCCTCGACATGCCCAGGAGAGCACCGCTGCAGGT
-CTGGCCTCTGTGCTGAGCCTTTTTTTTTTTTTTTTCCTGAGACAGAATCTCACTCTGCTT
-CCCAGGCTGGAGTGCAGTGGCAGGATCTCGGCTCACTGCAACCTCCACCTCCCTGGTTCA
-AGTGATTCTCCTGTCTTACCCTCCGGAGTAGCTGGGATTACAGGTGTGTGCCACCATGCC
-CAGCTAATTTTTGTATTTTTAGTGGAGACTGGGTTTCACCATGTTGGGCCAGCTGGTCTT
-GAACTCCTGACCTCAGGTGATCCGCCCACCGTAGCCTCCCAAAGTTCTGGGATTAGAGCT
-ATGAGCCACCATGCCTGGCTACCGTGCTGGGCCTTTCGAGGAGGCATTTGACAGGGAAGA
-TGAGAGACAAATTGAGTGTCAGGGAAGGGGTGTTGATAGAAAAATTACAGGAGAGCACAC
-AACTTTCAGCGGGTGAGCCCAGTGCCTGAGCTGCGGGACCACCCTACCAATGACCTTGAA
-CTTATCTGACTGCAGCCTTGAACTCCTGAGCTCAAGGAGTCCTTCTGCCTCAGCCTCCTC
-CCAAGTAGCTGGGACTACTGGCACATGCCACCATGCCCAGCTAATTATTTTATTTATTTT
-ATTTTATTTTATTTTATTTTATTTTATTTTGAGATGGAGTTTTGTCCTTGTTGCCCAGGC
-TGGAGTGCAATGGTGCAATCTCAGCTCGCCGCAACTTCTGCCTCCCAGGTGCAAGCGAAT
-TCTCCTGCCTCAGCCTCCTGAGTAGCTGGGATTACAGGCATGTGCCACCACGCCTGGCTA
-ATTTTGTATTTTTAGTAGAGACGGGGTTTCACCATGTTGGCCACGCTGGTCTCGAACCCC
-TGACCTCAGGTGATCCACCTGCCTCGGCCTCCCAAAGTACTGAGATTACAGGCATGAGCC
-ACCGCACCTGGCCCCACTTGTGGAACTAGCATCTATCTGGAGAGGAGGCAAACATCGCCC
-ACCACCTCCCGCTCTCTCCTGTCACCACTGTCCCCACCATCATTCCAGAGGTCACCCTGG
-CTTCCAACACCACAGCCTGGCTTGGGCAGTTTTCAAGCCTCGTATAAATGACATCCTCCA
-GAACATGTGCTCTGTGCCTGCCTTCCTTCCGTCAGTGATGTATCTGGAAGATTCCACTGT
-GTCGCCCTGTGGGACAGGTCCTTGTCATTGCTGAGTAGATCCTGTTGCAAATGCCTATCT
-CTCTTCATGGAAAGATCCAAGATACACAGATGGAAATCATCATAGGAAGGGCTGGCAAGG
-CCGTTCACACCCAGGGCTGGGGACCTCAGGGTGGAGGTGGGGGACAGTAAGGACCAGAAG
-GAGCAGGTGCCGGCGGGTGATGTGAGCTTTCTTCTCTATAGAGAAGTGAAGGCCGGGTGC
-AGTGGCTCACTCCTGTAATCCCAGCGCTTTGGGAGGTCGAGGCGGGCAGATCACTTGAGG
-TCAGGAGTTCGAGACCAGCCTGGGCAATTTGGTGAAACCCCATCACTATAAAAATACAAA
-AAATTAGCCGGACATGGTGGTGCACGCCTGTAATCCCAGCTATTTGGGAGGCTGAGGCAG
-GAGAATTGCTTGTACCCGGAAGGTGAAGGTTGCAGTGAGCCGAGATCATGCCACTGCATA
-CCAGCCTGGGGGACAGAAAGAGACTCTGTCTCAAAAAAAAAAAAAAGAAAAAAAGAAGTG
-AAGCACTTGCCAAGCAAATCTTTCAGAGCAGGTGGAGTGGACCCTACACCTCTTGGATAA
-TAAATGCACTGGATAATAAAAGCAGGAACAGGCCAGGTGCGGTGGCATGTGCCTGTAGTC
-CCAACCTACTGGGGAGGCCAAGGCAGGAGGACTGCTTGAGCCCAGGAGTTGGAGGCTGCA
-GTGAGTTATGACCAGGCAACTGCACTCCAGCCTGGGTGACAGATAGAGACCCTGTCTTTA
-AAAAAAAAAAAAAAAAAAAAAGGGCCAAGCACAGTGGCTCATGCCTGTAATCCCAACACT
-TTGGGAGGCTGAGGTGGGTGGATCTCCTGAGCTCAGGAGTTCAAGACCAGCCTGGCCAAC
-AGGGTGATACCCCTTCTCTACTAAAAATACAAAATTAGCCAGGCGTGGTGGCGCACACCT
-GTAATCCCAGCTACTTGGGAAGCTGAGGCAGGAGAATCGCTTGAACCTGGAAGGCAGAGG
-TTGCAGTGAGCCGAGATTGTGCCACTGCACTCCAGCTTGGGCAACAAGAGCGAAACTTCG
-CTTCAAACAAATAAATTAACGCCCAGCATGTCTTGGCTTTCATCTGCCAGACCTCAACCC
-TCACCCCCAGGAGATCAGGTCCGGACCATGAGCTGACCCTGGACTCAGGCAAGGGTGAGT
-TGGTGCAGCCCTGGCCTGCTGGGAGGCACAGGCTGCAGCAGGCTGCCTGGGGCTGAGGCC
-CGCCACTCATGAACTCATGACCTTGAATGAGCTCCAAAAGCTCTGGGCCTCCCAGGCTCT
-AGGGGGAGTGGGAGAGAGAGGCCTCAGCCTGTCCCTGGGCATGCTGCCCCCTCCTCACCT
-CTTTGTCCCAAATCCCCTTCCTGGCAAAGCTGACAGTCTTAATATCACTCTGGAGAAAAC
-TGAGTCAGCCCTAAGGAACAATTCAATGAACCATTTGCTTACTTGAGGATTGGAACTCAA
-GTCTCACTCAAAGTCTGTGCCATTTTCGTCCCAGCTGTCACTGGCCCTCATCCACACACA
-CCCAAGGATGAGCATCTAACGCTTGCATGCACACTCCCATGCCCGCGTTCATTCACTCAT
-TCATTCATTCATTCACTCATTCATTGACTCATTCATTCATTCACTCACTCATTCATTCAC
-TCAGTGAATGTTGCAGTCACGATCCAAATATTTATGGCCTCTGTGTGCCAGGCACTAGAT
-GGAGGGGCTGGGGCTAGAGCCCCTGATAACCCGGTCATGCCCTAGCTTTCCTGGGACACA
-CATTGTGGTAAGGGGAGACTAAAAAAATTAAGTCAGGCCAGGCACGGTGGCTCATGCCTG
-AATCCCAGCACTTTGGGAGGCCGAGGCGAGTGAATTACCTGAGGTCAGGAGTTCAAGACC
-AGCCTGGCCAACATGGAGAAACCCAGTCTCTAATTAAAAAAAAAAAAAATTAACCAGGTG
-TGGTGGCACATGCCTGTAATCCCAGCTACTCAGGAGACTAACGCAAGAGAATTGCTTGAA
-CCCAGGAGGCAGAGGTTGCGGTGAGCCGAGATCGCGCCATTGCACTCCAGCCTGGGAAAC
-AAGAGCGAGACTCCATCTCAAAAAAAAAAAAGTGGGAGGCAGAGGCAGGAGGATCACTAG
-AGGCCAGTAGTTTGAGACCATCCTGGGCAACATAGCAGGACCCTGTCTGTACAAAAAAAT
-TAAAAAAAATTTAACCGGGCATGGTGGCACACACCCGTAGTCCCAGCTACTCCAGAGGCT
-GAGGCAGGAGGATCGCTGGAGCCCAGGAGTTGGAGGCTGCAGTGAACTGTGATCCCACCA
-CTGCACTTAAGCCTGGATAACAAAGCAAGACCCTGTCTCAAATAACAATAGCAATAATAA
-TAAAGAAAAATTAAATGCAATTTGCGATGCATCAGTGATAAGTGCTCTGCAGAAAAAGGA
-GGCAGGAAGAGGCTGAGAAAGGTATGAGGTTTGCTATGCAATGTGAAGTTATCAAGGAAG
-GCTTCTCGGAAGAGGTGACATTTGAGCAGAGAAATGGAGGAGAGTTATGGAGGGAAGATG
-GTGAATGGGGGGAACATGGTCAAGACCAGGAATATGGTCAAGGGGGGAAAGATGGTCAAG
-GGGACGCAGCAAATGCAAAGGCCCTGAGGCAGGAGCAGCTTGATTCACCCCCAAAACCCG
-TGGGGCCCGTGCAGGCGACGGGAAGGACAAGTGTAAACCCTTTTCCTTGTCCCTGCAGGT
-GTGTGTGAACATGAGTCTGCCCATGTTTACACCCTGCAAGCCTGAAGAGTCCCCAGAAAC
-TGAAAGAAGAAGCAAAGCCCTTTCTGTACCCTCCCTGCCCCCTGTCCCGACCGCGACAAA
-AGCGACTTCCTCTTTCCAGTGCATTTAAGGCGCAGCCTGGAAGTGCCAGGGAGCACTGGA
-GGCCACCCAGTCATGGGGGACACCTTCATCCGTCACATCGCCCTGCTGGGCTTTGAGAAG
-CGCTTCGTACCCAGCCAGCACTATGTGAGTAGCTGGTGGAGGGCATCCCGTGGGGGGAAT
-ACGGGAGGGACAGCACGGCCACCCTTGCAGTCCCAGGGCCAACCAGCTCCAGTGAGGACT
-AACGGGGCAGGGTCTTGGGCACCTGGTCCCTGGTCTTTGAGCCTGGATCTACCCCTCTGA
-TCCCTGGGAAGACAGTTCCCTTGGACCCGCCCTGGGCCCCAGCCCTTTACTGTCCCCGCC
-TGTGTCCCCAGCCAGGCCCTCAGCCTTAGCCAGGAGTCCTCTTTCTGCTCCCCTGCCATG
-GCCAGGCAGCCCAGCGCTCTCTCAGGTCCGAGGCCCACTCCTCCAGGAAGCCTTCCCTGA
-CTAGCCCAGCTATCAGAGAGTGGCCCTCCCAAGAGGGAGGCCTGGAAACTAAAGCTCTCT
-CTCTCCCCAGCTGCCTGTAGTGTCAGTTAGAGTCTTATCCTCTCCAGTAGGGTGACACCA
-TGACAGGGGCCAATAGAGTCCTCCCATCTGTCCCCAAGGAGGCTGGACAAATGCCTGCTC
-AGACACACAAGTCCACTGGGTCCCCTAATCCCATAGGAAGGCCAGGGAGGAACTACATTT
-AGGAAATTGAAGCTTGTATGGAACATTTAGTCCTATGTGCCAAGACCTTTCTCTTTTTTG
-TTATTTTTTTGTTTTTTGAGACAGAGTCTTGATCTGTTGCCCAGGCCAGAGTGCAGTGGC
-ACGATCTCAGCTCACTGCAACCTCCGCCTTCCAGGTTCAACTGGTTCTCCTGCCTCAGCC
-TCCAGAGTAGTTGGGATTACAGGTGCCCACCACCACGCCTGGCTAATTTTTGTATTTTTA
-GTAGAGACAGGGTTTCACCATGTTGGCCAGACTGGTCTCAAACTCCTGACCTCAAGTGAT
-CCACCCACCTGGGCCTCCCAAAGTGCTGGGATTACAGGCATGAGCCACCGTGCCTGGCCT
-GTTTTTTTGAAATGAGGTCTGGAGTGCAGTGGTGCGATCATAGTTCACTGCAGCCTCGAC
-CTCCCAGGCCCAAGTGATCCTCCTGCCTCAGCCCCTTGAGTAGCTGGGGCTACAGGCGCA
-CACCACCATGCCTGGCTAGTTTTTAAAATTTTTGTGGAGATGAGGTTTCACTATGTTGTC
-CAGGCTAATCTTGAACTCCTCGGCTTAAGCAACCCTCTGGTCTCAGCCTCCCACAGTGCT
-AGGATTACAAGCGTGAGCTACCGTGCCTAGTCACTTTTCTCCTTTTCTTTGTAACTTTCA
-GTTTTGAAATTTCAAATTTACAGAAAGGCTACTGGGTGTCAAAACGGTACCAGTCACTCC
-AATAGTCTTTCACTCACCTTCATCCACACCTCTCTTTCTGGGGATATTTTCTGAATTATT
-TGAGAGTGAGTTGAAGACGTGTTTCTTTACCTCTAAATACTAGTTGTTGGGCATTTCTTA
-AAATCAAGGCATTCTCTTACATAATCACAACACACGTGTCAAAATCAGGAAATTAACATG
-GACAAAACACCATTATCCACCCACAGACTTTACTGAGGTTTCCCCGATTATCCTGCTTGT
-CCTCTGCAGTGAAAACTTTTTTCAGGTCTAGGATCCAGTCAAGGATCAATGTCATAGCCT
-TTAACCTTCTTTAATCTGGATCAGTCTTTTTTCTTTTTCTTTTTCTTTTTTTGGACACGG
-AATCTCACTCTGTCGCCAGACTGGAGTGCAGTGGTGCAATCTCGGCTCATTGCAACCTCT
-GCCTCCTGGGTTCAAGAGATTCTCCTGCCTCAGCCTCCTGAGTAGCTGGGAATACAGGTG
-CGCGCCACCATGCCCAGCTCGCATTTTTTGGTAGAGACAGGGTTTTGCCATATTGATTCT
-GGATCAGTCTTTTTTTTTTTTTTATGAGATGGAGTCTTACTCTGTCACCCAGGCTGGAGT
-GCAATGGCACAATCTCCACTCACTGCATCCTCCGCCTCCCAGGTTCAAGCAATTCTCGTG
-CCTCAGCCTCCCGAGTAGCTGGGATTACAGGCATGCGCCACCATGCCCGGCTACTTTTTG
-TATTTTTAGTAGAGACAGGGTTTCACCATGTTAGCCAGGCTGATCTCGAACTCCTGACGT
-CAGGTGATCTGCCCGCCTCGACCTCCCAAAGTGCTGGGATTACAGGCGTGAGCCACCGTG
-CCAGCGGATTCTGGATCGGTCTTAATCAGTCTTTGTCTTTTGCAACTTTGATGTTTTGCA
-GAGAGCAGACCAGTTACCTTGTAGAATGTCCCTTAGTTTGGGTTTATCTTCATTAGATTC
-AGTTTGTGTATCCAGGGCAGTGGATCTTAGATGCAATTCTGTCTTCTTTTTAATTTTTTT
-GAGAGGGAGTCTCGCTCTGTCACCCAGGCTGGAGTGCAGTGGCACAACCTCAGCTCACTG
-CAGCCTCCGCCTCCCGGGTTCAAGCAATTATCCTGTCCCAGCCTCCCAAGTAGCTGGGAT
-CACAGGTGCCCATCACCACTACCGGGTAATTTTTGTGTTTTTAGTAGAGACAGGGTTTCA
-CCATATTGGTCAGGCTGGTCTTGAACGCCTGACCTCAGGTGATCCACCTGCCTTGGCCTC
-CCAAAGTGCTGGGATTACAGACGGGAGCCAACATGCCCAGCCTTCCTGCCCCTCCCGTCC
-CCTCCCCTCTCCTCCTGTCCCCTCCCTTCCCCTCCCCTCCCCACCCAAGCTGGAGTGCAG
-TGGTGCAATCATAGCTCACTAAAGCCTTGACCTCCAAGTCTCAAGCAATTCTCCTGCCTC
-ACCTGGGGCCACAGGTGTGCGGCACCACACCCGGACAATTTTTGTGTTTTTAGTAGATAT
-GGGGGTCTCGCTATGTTGCCCAGGCTGGTCTCAAACTCTTGGACTCAAGCGATCTTCCCA
-CCTCGGTACTAAAAAGTGCTGGGATTCCAGGTGTGAGCCACCGTGCCCAGCCTAGGTCCT
-ACTTTTATCTCCAATTTACAGATGAGTCCATTTGAGAGAAGCTGACCCTCTTGCCCTGGG
-TCTCAAGGCTGGGGCGTGGCAGCACTTGGGTCCACGTTTGTGCCCTTTCTGCAATCCAGG
-ACAACCGCAAAGATGGTCCTCACCCCAATCCTCTGGGCTTCCTCCAGTGGGTAGTGGGAT
-CCTGGGTGCACACAGCAAAGCCTCTTTGGAGGCTGAATGGGGTCCCCCGACTCTGGCTTT
-CCCCCAGGTGTACATGTTCCTGGTGAAATGGCAGGACCTGTCGGAGAAGGTGGTCTACCG
-GCGCTTCACCGAGATCTACGAGTTCCATGTGAGTGTGGGGATGGAGGAGGGACAGGGACC
-CACCGTTCCAGCTCCACCCTTTGGGAAGGACCTTAGCCCAGGTGATGGGGAAACTGCAGA
-ACCCAGAATCCCCTCCCAGACCACAGTTAAAGGGGATTTATTTATTTATATAAATTTTTG
-TGACAGGGTCTTGCTCTGTCACCACTCTGAACACCTCATGTTCTCTGATTACAGGCATGA
-GCCCCCACGCTCGGCCTTTTAGGTGGTTTTGAGAGGTATTTAGGTTTGCAGTGCAGGGGC
-GCAATCATAGCTCACTGCAGCCTCGACCTCTGGGGCTCAAGCGATCCTCCTGCCTCAGCC
-TCCTGAGTAGCTGGGACTATAGGTGCGCATCACCATGTGTGGCTAATTTTTGTATTTTTT
-ATAAAGATGGGGATCTCACTATGTTGCCCAGGCTGGTCTTGAACTCCAGACCTCAAGTGA
-TCCTCCTGCCTTGGCCTCCCAAAGCTAAGGGGGCATTAAAAGAAAAAAACATTTTTCCCC
-CTGAAACATTTAAGTAGTCTTACTGAAAACAATAAAACACAGAAACACCAGATTCTCATT
-TTAAAGTAAAACAGACAGGATCTCCCAGAACCTTCCTAGAATGGAACCATTCTTGTCGCT
-TTTGAAAAACAAAGCCAAGTTCTAGATCCCAAATAAATGCACCTGCTGGTGAACATTCTC
-CTTGTGGTTCTCGTCCCTATGTTAGTTATTTTCCTAAATTTTACATTTGTACCTTTTTAA
-GAATGAGTTATCAGTTTTTTTATATTTGCTTTTCTTTTGAGATGGGGTCTTGCTCTGTCA
-CCCAGGCTGGGGTGCAGTGGTGCAATCACGGCTCACTGCAGCCTCAACCTCCAGGGCTGA
-AGCGATTCTCCCATCTCAGCCTCCCATGTTGAGATCACAGGTGTGCACCACCACACCTGG
-CTCCTTTTCCTGATTTGTTTTTTGTAGAGATGGGATTTCGCTATGTTGCCCAGGCTGGTC
-TCTAACTCCTGGACTCAAGTGATCCTCCCGCCTCAGCCTCCCAAATTGCTAGGATTACAG
-GTTTGAGCCCCTGCACCTGGTCAACCTGAGTTTTAAGAGGATCCCTTTGGCGACTGGATT
-GAGGACAGACAAGAGTGGACGGGGGACACAAGGAGGCCATTTTCGTTATCCAGGCCTGGT
-AGTGGCTAGGGCCAGGAGGGTGGGGTTGGTGGGAAGCAGTCAGATCCCAAAGAGATTTGG
-GGATTGGAAGCAAAAGGATTTGCTGGTGACTTGCACATGGGAGGGAGAGAGGTCAGTGCC
-TCTGCTAATCAAGGAATCCAGATTGCCACCGAAATTTCTAGGCCCGAGATATTTAGGTAG
-TGTCTCACTCTGTCACCCAGGATGGAGTGCAGTGGCACCATCTCGGCTCACTGTAACCTC
-CGCCTCCCAGGTTTAAGCGATTCTCCCACCTCAGCCTCCTGAGTAGCTGGGATTACAGGC
-ATGTGCCACCACTCCCGGCTAATTTTTGTATTTTTAGTAGAGACGGGGTTTCACCACGTT
-GGCCAGGCTGGTCTTGAACTCCTGACCTCAAGTGATCCACCCACGACAGCCTCCCAAAGT
-GCTGGGATTACAGGCGTGAGCCACCATGCTCGGCCTTTTAGGTGGTTTTGAGAGGTATTT
-AGGTCACTTCCAATCTCGTGCTTTTCCAAGTGTTGTAAACTACAAATATTCCTTCACGTC
-TTCTTGTCTTTTTAATGTTTAGAAAACCTTAAAAGAAATGTTCCCTATTGAGGCAGGGGC
-GATCAATCCAGAGAACAGGATCATCCCCCACCTCCCAGGTGAGCACGGGGCTGAGCCGCC
-TGTCAGGGGGTCATTGGCGGGGGCTCACCTGCCCTCCCAGCCCCTCTCGGGCTTGACCTC
-ATGTTCTCTGGTGCCAGCTCCCAAGTGGTTTGACGGGCAGCGGGCCGCCGAGAACCGCCA
-GGGCACACTTACCGAGTACTGCAGCACGCTCATGAGCCTGCCCACCAAGATCTCCCGCTG
-TCCCCACCTCCTCGACTTCTTCAAGGTGCGCCCTGATGACCTCAAGCTCCCCACGGACAA
-CCAGTGAGTGAACTTTTCACCCTGCCAGGTGGGAGAGGGAAGGAGGGGTGGGACTTTCTG
-TGTTTTGCAGATGAGGAAACCAAGGCTCAGAGAGGGAAAGCCACCTTCCCAGAGCCACAC
-AGCCAGAAAGAGGAGGCAAATTCCACCTCCGGCCCCTGTGACCCCGCCAAGCCTCCACCT
-TAATCTTTCACACCTCAGGGCACTGGGGGAAGCACTCGGGGCTGGAGGTTCAAAGTCCTG
-GGTCCTCATCCTGACATTATGGCCACCTGGCCATGGGACCTGGAGCCAGTCACCACTGCT
-CTCTGAATGCAGGTTCTCCATTTCTATAATGGGCAGTGAGGATCAGATGAAGCATTGGGT
-GTCTTGCGGAGCCCCCCAGAAGGATGTGGGGTTGATGCCTCTGCTAAGTGCTGAGCATGT
-CTGGGGTCTCCTGTACCCAGGACCCTGTGTGGAAGGCACCTGAGAGGCTGAGGGAGCTCC
-AGGCAGGCTGGGGAAGTCCCCTTCTCCACTCCTCTCTGGTCACTGAAGCTCGAAGTGGGG
-AGCATGAGGACAGGACGTTACCCCTTGTCAAGGCACCCAGGCTGCCAAGACAGAGACAAG
-CAGCATTGCTCCGGCCAGCACTTATTGACGCTTGAAGGTGTCCCCTGGCCCAAGGAAGGG
-CAGTTATCATCAGCCCGGGAGGCGGGGGAAGGATGGACTCTGCAGTGGGGTCCGCTCCTC
-ATTGCCTGCTCTCTCAGGGCTCCAGAAGGAGGAAGAGGCCGGGCACAGTGGCTCACACGT
-ATAATCCCAGCACTTTGGAAGGTCGAGGTGGGCAGATCACCTGAGGTTGGGAGTTTGAGA
-CCAGCCTGGCCAACATGGTGAAACCCCATCTCTACCAAAAATATAAAAATTTAGTCAGGC
-ATGGTGGTGTGCGCTTGTAATCCCAGCTACTTGGGAGGCCGAGGCAGGAGAATCGCTTGA
-ACCCGGGAGGCAGAGGTTGCAGTGAGCTGAGACTGCGCCACTGCACTCCAGCCTGGGTGA
-CAGAGCGAGACTCTGTCTAAGAAAAAAAAAAGAAAAGAAGAAAGAAGATGGCCTGGGAGC
-CCGCAAGAGCATTTTCCAGGCTTAGGGCATCCTTTGGGTCTGCAGAAGGCTATGCAGTGT
-CCTCCTCATGTCCCTCCCTTGGGCTGCCCGAGCAGATCCGCCCGCCCCCATCACTTCCTG
-AAGCCCTTCCTCAGCCAGTCCAGTTGCTGTCTTCTCTCCGCAGTGCCCCTTCCCTTTCCC
-GGGTCCCTCTTCTCTTGGGAAGTTCTTCTGCAGGTCTACCCAGTGCCTCTTCTTCCTCCA
-TGGGAAGCCAAGGGTCTCACCCAGACTGTTCTCTCCTCAGGACAAAAAAGCCAGAGACAT
-ACTTGATGCCCAAAGATGGCAAGAGTACCGCGACAGGTGAGAGGACGGGGGGCAGCCGGC
-GGGGGGGGACACCCTGAGGAGACCCAGAGTGTTCAGGGAATGGAGCAGGGGCTGGGAGCA
-GGCTGGGAGGGCTCACAGCTACCCTGCTGAAGAATTGGGTCTTTGGGCCGGGTGCGGTTG
-CTCATGCCTGTAATCCCAGCAGTTTGGGAGGCCGAGGCAGGTGGATCACTTGAGGTCAGG
-AGTTTGAGACCAGCCTGGCCAACATGGAGAAACCCTGTCTCTACTAAAAATCCAAATTAG
-CCAGGCGTGGTGACAGGTGCCTGTAGTCCCAGCCACTTGGGAGGCTGAGGCAGGAGAATT
-GCTTGAACCCGGAAGACGGAGTTTGCAGTGAGCCGAGATCGTGCCACTGCACTCCAGCCT
-GGGCAGCAGAGCCAGACTCCATCTCAAAAAAAAAAAAAAAAAAAAAGAAGAATTGGGTCT
-TTGGAAGGTCCCTGGAGACTGAAAGGAGCCCTTTGCAGGTGGCAGTGCAGAGACCAGCGC
-AGACCCTTGCTACTGGCAGCCGGGGGAGTGTTTGCGGCTGAATGAATGAACAGGTTTTGG
-AGGGCAGTGTGGCCTTCAGAGGCGATGCAGGGCTGTGGCAGTTTCTAATACTTATTGCAC
-AGTCACTGCTAATAACAATAATAATAATAATACCTAACATTAATGGAGTGCTTACTCTGT
-GCCAGCCACTATTTTGTTTTTGTTGTTTTCAGTGACAGGGTCTCGCTCTGTTGCCCAGGC
-TAGAGTGAAGTGGTGTGATCATAGCTCACTACAGCCTCGACCTCCTGGGCTGAAGCGATC
-CTCCCACCTCAGCCTCCCAAGTAGCTGGGATTACAGGTGTGTGCCACCATGTCCAGCTAA
-TTTTTAATTTTCTGGTAGAGATGGGGTCTCACTACATTGCCCAAGCTGGTCTTAAGCTCT
-TGGCCTCAAGCAACCCTCCTGCCTCAGCCTCCCAAAGTGCTGAGATTATAGACATGAGCC
-ACTGTGCCCGGCTTTTTCTTCTTCTTATAAGGACACGAGGCCTGTTGGGTTAGGGCCCAC
-TCTACTGACCTCATTTTAATTTAATTACCTCTTGAAACGTACTTAAGAGTACCTTTCTCT
-TAATACACCCACACTGTAAGGTACTGGGTGGTTAGGACTTCAACATATGAATTTTGAGAA
-GGCGGATGTCAGCCAATACTAAACAGCATCAGCACCTCCACGGTTGGATGAAGGGCTGGT
-CAGAAATGCACACTCAGGTCCCACAGTGGACCTACTGAACAGGATAGGCATTTTAGCAAA
-ATCCCAGGTATTCGGGTGCACCTTAAAGTTAGGAAAAGGTCAGGCACTGTGGCTCATGCC
-TGTAATCCCAGCACTTTGGGAGGCCGAGGCGGTTGAATCACCTGAGGTCAGGAGTTCGAG
-ACCAGCCTGACCAATATCGTGAAACTCCATCTCTACTAAAAATACAAAAATTAGCCAGGT
-GTGGTGGCGGGTGCTTGTAGTCCCAGCTACTTGGGAGGCTGAGGCAGGTGAATTACTTGA
-ACCTGGGAGGTGGAGGTTGCAATGAGCCAAGATTGCACCACTGCACTCCAGTGACAGAGC
-GAGACTCCATCTCAAAAAAAAAAAAAAAAAAGTTGGGAAAAGGCCAGGTGCAGTGGCTCC
-ACACCTGTAATCCCAACACTTTAAGAGGCTGAGGTGGGAGAATCCTTTGAGCCCAGGAGT
-TCGAGACCAGCCTGGGCATTGTCCCAAGACCTTGTCTTTACAAAAAATTAGCCGGGTGTG
-GTGGCATACGTCTATGGTCCCAGCTATTCGGGAGGCTGAGGCAGGGAGATTGCTTGAGCC
-TAGGAGTCCAGGGCTGTAGTGAGCTGTGATCACGTCACTGTACTCTAGCCTGGGCAACAG
-AGCAAGACTCTGTCTCCAAAAAAGAAAATAAAGTTGGGAAAGGCTCACTAACTTCATCAG
-ATGAGAACAAGGACATGTTTGAAGTGTGAGGCCGAAGCCTGGAGAACGCTATGCGCCCAG
-GAAATGCAGGGCAGCAGAGACTCAAGATGCCAGCGCCTGTTCTGGAGGCCCAGATGGGCC
-CTGCAATGCCCACTCACCCTGCCCTCCCTCTTGCCCCAGACATCACCGGCCCCATCATCC
-TGCAGACGTACCGCGCCATTGCCAACTACGAGAAGACCTCGGGCTCCGAGATGGCTCTGT
-CCACGGGGGACGTGGTGGAGGTCGTAGAGAAGAGCGAGAGCGGTCAGACCTCCCACCTTA
-CGGGGCTCCTTCCCCTGGTGCTCAGGAACCCACAGCCACAAGCCCCCTGCCAAGGCTCAG
-GCAGCCTTGCCCCTGGGAGGACTCCGGCTCTGTTAGGGGCCCTAAATGTCCTCCCCACAC
-TGTGGGTCGCCTTCTGTCTTAGTGTGCACCCTGTGGTGGCTGTGGGCATCTGTGCATGGC
-AGGCCGGGGCGGGGCATGTCTGCGTGTTCTGTCTGGATGGGTATGGGACCGTCTGTTCAT
-TATGAAGTGGGCTCAGAGCTGTGATTCTGTGAGCATGTGTGCATGCATGCATGTGACCTC
-ATTGTCCAGTGTGGTGAAGGTGACATTTCCAAATCTGAGCATTGGACATCAGTGTGTCTG
-TGTCCCTGTGTCCTCACCATCCCTGATGGCTGCAGGGAGCCGCTGGGCCCTGCCCCTCAG
-TCACATTCCCGCACCTCTGGCACAGGTTGGTGGTTCTGTCAGATGAAAGCAAAGCGAGGC
-TGGATCCCAGCGTCCTTCCTCGAGCCCCTGGACAGTCCTGACGAGACGGAAGACCCTGAG
-CCCAACTATGCAGGTGCCCCCTGCCCTCCGAGGCTGTAGGGGTGTGGGAGAAAGGGGCAG
-GCAGGGCTCAGGGATATTGAGTGACTGCTTTGGAGTCTGGGCTGGTTGCTGGCTTGGCAG
-AAAAGTCAGGGCTAAGATCTCATCGACTCTGGCTTGGGGGCCCTGGCAGGTTGTGATGCC
-CTTGGTCTGGACAGGGAACCAGGAGGAGGAGCAGACGACTGGGGAGAGTGGGAGGCCAGT
-GGTGTCTGTGGATATGTGGCCAGGTTCAGTGGGAAGCTGAAGGATGAGCAGACCTTAGGC
-TCAGGAAGGAGGGCTGCCTGGAAGTGGGGGCATCATCACTGACCAGAAAGGGAAAACTGG
-CAGTGCCAGGGCTGGATGGGGCCTGCATTGAGCTTGAAAAAAACTATAATAGAATTGGTT
-ACCATTTTATTTTATTATTTATTTATTTATTTTACTTTTTTGAGATAGAGTCTCACTCCC
-TTGCTAAGGCTGGAGTGCGGTGGTGCTATCTCAGCTCACTGCAACCTCTGCCTCCCAGGA
-TCAAGTGATTCTCCAGCCTCAGCCTCCCCAAGTAGCTGGGATTACAAGCATGCACCACCA
-TGCCTGGATAATTTTTGTATTTTTAGTTGAGACGGGGTTTCACCAGGTTGGCCAGACTGG
-TCTCGAACTTCTGACCTCAGGTGATCTGCCTGCCTTGGCCTCCCAAAGTGCTGGAATTAC
-AGATGTGAGCCACTGTCCCTGGCCTGGTTACCCACATTTTAAAATGGAGTGATTTCACCC
-TTTTATGTGGATTTACAGCTTTTTTTTTTTTTTTTGAGACAAAGTCTGGCTCTGTCACCC
-AGGCTGGAGTGCAGTAATGCAATCTCAGCTCACTGCAACCTTAGCCTCCTGGGTTCAAGC
-AATTCTCCTGCCTCAGCCACCTGAGTAGCTGGGATTACAGGCATGCACCACCACGCCAGG
-CTAATTTTTTGTATTTTTAGTAGAGATGGGGTTTCGCCATGTTGGCCAGGCTGGTCTCGA
-ACTCCTGACCTCAGGTGATCCGCCCGCCTTGGCCTCCCAAAGTGCTAGGATTACAGGTGG
-GAACCACCTTGCCCAGCCTGTGGCTATCGTTTAAACACTGGGAAGGCCTGCAGCCCCCAG
-GCCGACAGTTAGCTGCAGCTGAGCAGTTCCCAGTGCCAGGTAGACGGATGCTCCACCCAC
-CTACTCATGGCTGATCTCTTGTCATAGTGAAGTGTCTGGACAGACCTTCATCGTTATGGG
-ATCTCTGGTCCCCAGAGTGGGTGGCAATGAATGGGAGTGGACAAGCTCACCTGGGTGTAG
-GGGGCAGAGGGCCGAAGTCCAGAGTGTACCCCCAGAGTGGGTGCCAGCAGGAGCTTGCCG
-AGGGATCTGGGATGGAGCAGGAGGGTGGAGGGAGGAGACCCAGAAGAGGGGGAACTGTGG
-GCCCTGGGTGGGTCTGGAGTGCCTGGAGGAAGCCCAGGCGCAGAGAGGAGAAGATGGGAT
-GGGTGGCGAGCCCCAGGCTGGGCCGACCTCACACTGTGCTCTGTGCCCCTGCCGTGGACC
-AGGTGAGCCATACGTCGCCATCAAGGCCTACACTGCTGTGGAGGGGGACGAGGTGTCCCT
-GCTCGAGGGTGAAGCTGTTGAGGTCATTCACAAGCTCCTGGACGGCTGGTGGGTCATCAG
-GTAGGAGGGCCCCTCTCCATCCAGAGCACCCATCTGAGTCAGCCCCAGCCAGGACGGGGT
-GTTTAGGGATCTGGGGTGACTTGTCCCTGGGACTCTGGGTAAGCCACTGCCCCTCTCTGG
-GCTTAGTTTCCATCTCAGTAGCAGGGAGGAATGAGCCCACCCTTGCCTGTCTTGTGGGGA
-TCCAATGTCCTTGTCCAAGTGGGTGCATTTCTCCTTTGTGATTTAGGGTCTCTTCCCAAC
-CATCTATTATTATTCCTTCTCTGGCAACATGGTGAACTGTTGTATAAATAATTACATTCC
-TAGCTAGGCGCAATGGCTCAGGCCTGTAATCCCAGCACTTTGGGAGCCCAGGACAGGACG
-ATCATGTGAGGTCAGGAGTTCGAGACCACCCTGGCCAACATGGCAAAACCCTATCTCTAC
-TAAAAACACAAACATGAGCCGGGTGTGGTGGTGGGAGCCTGTAATCCCAGCTACTCGGGA
-GTCTGAGACAAGAGAATCACTTCAACCCGGGAGGCGGAGGTTGCAGTGAGCCAAGATCGC
-GCCATTGCACTCCAGCCTGGGCAACGAGAGCGAAACTCCGTCTCAAAAAAAAAAAAAAAA
-AAAAAGATTACTTTCTTTTTATCATTCCTTTATCTTTTAAAGCTTTCTTGCAGTCAGGTG
-CAGTGTCTCATGCCTGTAATCCCAACACTTTGGGAAGCTGAGGTGGGAGGATCACTCAAG
-GCTACAAGTTCAAGACCAACCTGGGCAATGTAGGGAGACCTCTGTCTCTACAAAAAAAAT
-TAAAAAATAGCTGGATGTGGTAGCACACACCTGTAGCCCCAGCTACTCAGGAGGCTGAGG
-TGAAAGGATCACTTGACCCCAGGAGTTGGAGGCTGCAGTGAGCTATGACTGCACCACTGC
-ACCCCAGCCTGGGTGATGGAGCAAGACCCTGTCTCAAAAAAAAAAAAAAAAAAAAAGCTT
-CCATTGCAATTCCCATCTGTTTATCCTCCAAATGAATGCAGAAATACTAATTATCTTTTT
-TCTGGTTCTGGGGAACACAGAATTCTAGCGGCTTGTGGAGCCATTTCCCTGGAGCCATGG
-GGCCTCCCAGGTCCTTTCCTGTGTCTTCATTTTTTACGAATTTTTTCATTTTTTGAGACA
-GGATCTTGCTCTGACTCCCAAGCTGGAGCACAATCATCGCTCACTCAAGCGATCCTCCCA
-CCTCAGGCTCCCACGTAGCTGGGACTACAGGTGAGCACCACCACATCTGGCTAATGTTTT
-TTAATTTTTTTGTAGGGATGGGGTCTCACTATGGTGCCAAGACTAGTCTTAAACTCCTGG
-CCTCAAGAGTTCCTCCTGCCTTGGCCTCCCAAAGCACTGGGATTACAGGAATGAGCCTCC
-ATGCTGGGCCTTTGCTGGCGTCTTCAGAGCCCTAGGTCACAGGGCCAGCCTGGCGCCCTG
-CCGCAAGCTTATCTTAAAGCTGGGACCACAACATGCATACCTGCAGCCGGGCCCGGGGCC
-AGAGGGCTTTGAGGCAGCATTTCTCAGCCTTTTAGACACACACTCTGTTAACCCCCATCC
-TGTGTCTCTGATAATCTTCTTGTGATCCTCCCACCAGCCAAGAATTGGGTTTTATGTGAA
-CCTTGTATTATGCAAAGTTTTCTTTTGTTTTTTTTTTCACTCCCAAATATAATATTGAGA
-ATAGAAAGAAAGTCTTTTCAACAAATGGTGCTGGAACAGATGGATTTCCATACTGGAAAA
-AAAAAAAAAAGAGCAAAAAACAAACCTAGACCCCTTCCTCACACTGTACACATATGTTTA
-CTTCAGATGGATCACAGGTTTATCCCAGAGTAAAACCTGAAACTAAAAACCATTTGGGGC
-TGGACAGGGAGCTCACGCCTGTAATCTCAGCACTTTGGGAGGCTGAGGCAGGTGGATCAC
-TTGATGTCAGGAGTTTGAGACCAGCCATGACCAACATGGTGAAATCCTGTCTCTACTAAA
-AAAATACAAAATTAACCAAGTGTGGTGGTGCATGCCTGTAATCCCAGCTACTTGGGAAGC
-TGAGACAGGAGAATTGCTTGAACTTGGGAAGCAGAGGTTGCAATGAGTCGACATCATGCC
-ATTGCACTCCAGCCTAGGCAACAAGAGCAAAACTCTGTCTTGGGGTTGGGCGGGGGAAAA
-GCATTTGGAAGAAAGCATAGAATTTGGTGGCTTGGAGGTAGGCAAAGGTTCGTAGGAGAC
-AGAAGGCAGTTAACATAAAAGAAAAATTGGCAAATATAATCCGCCAATGTCTTCTTTTTT
-CTTTACTTTTTTCGGGAGGTAGAGATAGGGGTCTTGCTATGTTACCCAGGCTGATCTCCA
-ACTCCTGGCCTCAAGCGATCCTCCCACCTAGATCCCTCAAAGTACTGGGATTACAGGCGT
-GAGCGACCGTGCCCTGCCCATTCTTGCCAATGTCTTATAGCAAATACCTGTCCCCTGCGG
-TGACCTGGATCTGCTAACCTCCACCCCTGCCTAGACTGTGGAAGGATTGCTGGAAGGGTC
-TCAGTTGCACAGACCAGGAAACTGAGGCCCACAGAGGCAGGTGTCCGGTTGTTTGCAACC
-TCTCAGCCTGTGCTAACCCCAATTGTTCAGAGAGAGCCCTGAAACCCTCTCCTCTGGGCG
-CCCCCAGGTGACTGCCCCAGCCTCAAGGGCTGCCTCTGTTGCAGGAAAGACGACGTCACA
-GGCTACTTCCCGTCCATGTACCTGCAAAAGTCAGGGCAAGACGTGTCCCAGGCCCAACGC
-CAGATCAAGCGGGGGGCGCCGCCCCGCAGGTAAGCGGGGGTCCCCGGGGCTGGGCGGGGT
-CGAGCGGGGCGCACCACGGGTTCGCTCTGTCTAGGCCATAGCTTGGCAGTGCCGGGGCGG
-GGGCTCTCAGCCTGGCAGGAGAGGCAGGACCCTCACGGGGGAAAGGGGCTGGACGCGCCT
-GGCCGCGGTGTGGGGCTGGCACGGGGGCGGAAGGAAAGCGGCGATGCCCGGGGGCTTTGG
-GGATGGGCAGTCCAGGGGGGGTCCCCGGAGAGGGGGACGACAGACCGAAGGCTGGTGAGG
-GGCGTGGAAAACCGCCCAGGCTCTGCTGCAGGGCAAGGGTCCTTGTCGTGACGGGGGCAG
-CCGCCTCTTGTCCCGCCGGGGTCGTGCAGACTACCGGCCCCCTACTGCCCCCCACTTCCT
-CGGACCAGGGGTGCCCATCTGAGTCCCTGGGGGCAGGGGCGCCCTCGGGCTTTGACGACG
-CCCCGTCCCGCTGGGCCAGGTCGTCCATCCGCAACGCGCACAGCATCCACCAGCGGTCGC
-GGAAGCGCCTCAGCCAGGACGCCTATCGCCGCAACAGCGTCCGTTTTCTGCAGCAGCGAC
-GCCGCCAGGCGCGGCCGGGACCGCAGAGCCCCGGGAGCCCGCTCGGTGAGTGCAGCGGGA
-GAGGGCAGGAAGGGCAAGCCCTAGAGGCGGAGTCAGCGGGAGAGGCGGGGCCAGAGGTAG
-GGCCAGAGTAGCGGGGCGGGACCAGAGGGCGGAATCAGAGGGAGAGGCGGGGACTGGAGG
-CGGGGTCAGAGGAGGAGCCAGCGCTAGGGGGCGGAGCGATCCCTAAGAGGCGGAGTCAGA
-GGGAGAGGCACAAGCGGGAGGCGAGGCCAGAGCGCGGAGCAGGAGTTGGAGACCGCGGCG
-GGGCGAGGCCAGAGAGCGCTGTGGGCGGGGCCAGTGTGCGGGGCGGGGCGTCTGACTCGG
-CCCCGCTCTCTGCCCGCAGAGGAGGAGCGGCAGACGCAGCGCTCTAAACCGCAGCCGGCG
-GTGCCCCCGCGGCCGAGCGCCGACCTCATCCTGAACCGCTGCAGCGAGAGCACCAAGCGG
-AAGCTGGCGTCTGCCGTCTGAGGCTGGAGCGCAGTCCCCAGCTAGCGTCTCGGCCCTTGC
-CGCCCCGTGCCTGTATATACGTGTTCTATAGAGCCTGGCGTCTGGACGCCGAGGGCAGCC
-CCGACCCCTGTCCAGCGCGGCTCCCGCCACCCTCAATAAATGTTGCTTGGAGTGGACCGA
-GGCTCTGCAGGAATGCAGGGAGGGCCGGGCTCCGCCCCAGGGTTATTTCTAAGTTGAGGA
-CAGGAGGTTGTGAGTTCTGCTGGGGGGAAGTTGCAAGAGCCGAGGTCTGGTTGCATGTTG
-CCCTGGTCTTGGCCAAGAACAGGTTTGCACAAGGCCAAGTTCAAGAGGAACTCCCGGTTT
-CCTGCTGACCGTTTGGTCAGAAACCACCTGCTTGGACTCTGGCGGAAGAGTGCTGAAGAT
-GGGTGCACACAGTGCAGCAGGGCAGCCCTGTCTCATGACAGGAGACAGGCTGCCGTCCAG
-GGTGTAGGAGTGACCTCATAGCTGGGATAAAAAATATATTATAACTTAGGTTCGGGCGCG
-GTGGCTCACGCCTGTAACCCAGCACTTTGGGAGACCGAGGTGGGAGGATCCGTTGAGCTC
-AGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCATCTCTACCAAAAATATAAAA
-ATTAGCTGGGCGTGGTGGCATGCATCCATAATCCCAGCTACTGGGGAGGCTGAGGCATGA
-GAATCGCTTGAACCGGGGAGGCAGATGTTGCAGTGAGCCGAGACGGCGCCACTGGACTCC
-AGCCTGGACAACATGGTGAAACCCCATCTGTACCAAAAATATAAAAATTAGCTGGGCGTG
-GTGGCATGCATCCACAATCCCAGCTACTGGGGAGGCTGAGGCATGAGAATCGCTTGAACC
-GGGGAGGCAGATGTTGCAGTGAGCCGAGACGGCGCCACTGCACTCCAGCCTGGACTACAG
-AGCGAGACTCTAGCTCAAAAAAAAAAAAAAAAAAAAGTAACTTAGGTGCAGGGTGTCCTC
-TGTTATTCACTGAGACCGTGCCCCGGTTATGAGGTTGTACCAGAAAGCAAGTATTCACTA
-TGCACACTATTCACCGCTCACCCTAGCATTGAAGCCAGCCTGTAGCCTGAAAGCCTTTGC
-TTTGAGGGCAGGTCTTTCCCCAAAATGCAGACACGAAGGTGCAAAGTGAAGCTGCCAGTC
-TTGCAAAAGATGTAACTTGTCACGAAGGCCACGAGTGGCAGGGAGAGCTGTCCCACATTT
-GCGGAAGTGGCTATGTGAGGACGGGGGAGGCGGGTCCCTTAGAGATAAGAGACAATCATA
-AGGGGAGATATCAGAGAAAATCGTAAGGGGAGCAGATGGTTGTCAAGAGAATAGGCTGAC
-CATCGAAGGACTGGCAGAAGCTTTCAGAAAACCACTGGACGGCTGGGCACAGTGGCTTAG
-GCCTGTAATCCCAGCACTTTGGGAGGCTGACGCGGGTGAATCACTTGAGGTCAGGAGTTC
-CAGACCAGCCTGGCCAACATGGTGAAACCCCATCTCTACAGAAAATATAAAAATTAGCCA
-GGCGTGGTGGCACAAGCCTAGAATCCCAGCTACTTGGGAGGCTGAGGCAGGCGAATGGCT
-TGAACCCAGGAGTCAGAGGCTGCAGTGAGTCGAGAGTGTTCCACTGCACTCCAGCCTGGG
-TGACAGTGCAAGACTCCTTCCAAAAAAAAAAAAAGAAGAAAAAAGAAAACCACTGCAGCT
-CTAAACTAGTTCTGCATTTTTGCCGAACCTGGTTTGCTGGAAAAGCCCAGCACCAAAGGC
-TATCATACAAAGCTGTGGGAAATTGAATCACCAACCTCACCCCTTCTGCTTGTTCAGTTG
-CAGTTATAACCCTTTTATTAAATACAGTATAAAATACCACGCCTCTAATCCGAGTGCTCT
-GGGAGGCCAAGGTGGAAGGATTGCTTGGGGCAGGGAGTTCAAGACCAGCCTGGGCCACAC
-GGTGAGACCCATCTAGACAAACATTTTTAAAAATTAGACAGGTGTGGTGGTGTGCACCTG
-TAGTCCCAGGCTGGGTGGGAGGATCGCTTGAGCCCAGGAGTTTGAGGCTGCAGTAAGCTG
-TGATCGTGCCACTGTACTTCAGCCTGGGTGACAGAGCAAGACCCTGTCTCTAAAAAAAAA
-ACAAATTAAGGCCAGCCACAATGTTTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAG
-GCAGGCGGATGACTTGAGGCCAGGAGTTCGAGACCAGCTTGGCCAACATGGTGAAAGCTT
-GTCTCTGCTAAAAATACAACAACAACAACAAAATTAGCCGGGTGTGGTGGTACACGTCTG
-TAATCCCAGGTACTCAGGAGGCTGAGGCGGAAGAATCACTTGAACCCGGGAGGCAGAGGT
-TACAGTGAGCCGAGATCACGCCACCACACTCCAGCCTGGGCGACAGAGCATGACTCTGTC
-TCAAAAATAAATAAATAAATAAATAAAAATAAAAAAATACATACATATAAAAAAGAAGAG
-AAAATACTTATTTTCATGATTGTTTCATTTTTTTCCAAGCTGAGGTCCTGACCAAATGTT
-TCCCCGTGGTTTTTGTATATTTCTGATCCCCTTAAAGTGGCCCTTGCAGCGTGCTGGGGA
-GGAGGCCTCTCGGTGGGTGGGTGATTGGGAAGCCACGCCCACAGGGAAGGGAGAAAAAAA
-CTGAAGTTGCCTGCTCTAAGGGCTGCACCTCTGTTTAGCCAACAATTTTCTTGAGGCCAG
-TCATAGTGCTGGGCTCATTCCATCATCTCCAGTTCTGAGACCAACACTGTCTGGTAGGTG
-TTTTATGGATGAGGAAACCAAAGCTCATAAAATTAATTAAGTGGTTTGCTTATGAAATAA
-TGCAAGAAAGCAACAGTGCTGGGAGGTGGAACCGGGTTTTTCTTTTCTTCTTCTTTTTTT
-TTTTTTTGATGGAGTTTCGCTCTTGTCACCCAGGTGGAGTACAATGGAGCGACCTCAGCT
-CACTGCAACCTCTGCCTCCCGGGTTCAAGTGATTCTCCTGCCTCAGCCTCCCGAGTAGCT
-GGGATTACAGGTGCCCGCCACCCTGCCCAGCTAATTTTTTGTATTTTTAGTAGAGATGAG
-GTTTCACCATGTTGGCCAGGCTGGTCTTGAACTCCTGACCTCAGGTAATCCGCCTGCCTT
-GGCCTTCCAAAGTGGTGGGATTACAGGCATGAGCCACTGCGGCTGGCCCAGGCTTTTCTT
-TTTGATTCTAAGGCCTTCCAGATCCAGTACTTTATCCTGACCCTGCAGAGCTCAGGATCT
-GTGGTTCAGGCCTGCGGCTCAGAGGAGGGAATACGGCACACAGGTACGTGCCAGGCCAAG
-TGTGAGGGGGTCTGGCTTCCAGGGCCCTCTGCAGACCCCTAGTCCCAGGGCCTGTGTTGG
-AGGAGAGATTGGCTCTTTCCTCTGCCCATCCTGGGATGAGAAGTCGGGGACTTGGGATAG
-ATGCAGTGCAATCCCTGCCCCTGAAAATTGACAAAGACCCACCAAATCTAGCCCCTACTC
-CTAGGCTGGGCCCCTGCCCATCTCCCTGGACCACACCACTCTCAAGGGCTCTCGTTTGCA
-GACACCCCATTGCCCTACTAAAAACCTCTCCTGGCCAGGCTTGGTGGCTCACGCCTGTAA
-T
+>chr15_43599000_43620000
+GCCGAAATATGGCAGTGAGTGAGCCTCCGGGATGTAAGATAATCTGAAATGAAATTCAGG
+TTGAGTGGGGAGGCAATTGGAAATGAGCAGGCAAGTCAGTCAGTGATAAAGAAAAACTCA
+GACTGTAGGAAGCAGATCAAAGATTAGTGTCCCTTAGGTGGAGCTGGTGCAACTGGTCAT
+CGATGGAGTAAACTATTTGATTGATTGTGAACGGCGTCTGGAGAGAGGCCAGGATATCCG
+CATCCCCACACCTGTCATCCACACCAAGCATTAACTCCCCATCGCCAGCTGATGACTCAA
+GATTCCCAGGAGTTCTGCTCATTCTAATGATGGCCCATTCTACTTGCTCTGGACCTGCCC
+CCGCATCCCCTGCCTCCATCCTAGTAAAGACTCCTTGCTATGCTGCAGCTGTCTGTGTTA
+CTTCTAATGGTGGGGTGAGGAGGGAGCAGCCTTCAGGAAATGAAAAGAGGCAGTGGGATT
+ATTTATGATGGAAAGAGACTCCAGATATGGCAACCCAGGAACACTGATTCTCAGGTGGGT
+GGAAAGCATTAACATTTTACCCATATTCCTCATCAGCTTCTGAAAATAATCAGGATGCAC
+TTCTGTTTGCACTTTATTCATTATGACTTAAGATTTCTCTCCCCACAATCTCCTTCTACT
+GTAGAGACAGGCTCATAGCAGGTGGCCAAGGAAGCTGATAGTCAATACCAGGGACCAGGA
+AGGTCGTGACCAGTCCTGGAGGCCCCAGGCTGTACTTCGACCTATAATAGACAGGGAATG
+GGAGTAATATCACAACTCAGCTCTCCAGGAGCATTGATACTTGGAAATTAGCGCTCTGCC
+TGTAGACTCCTTCACTCCAGGGATCTCCCTGGGTGCACTCTAAGAGCCAGACAGCACCAA
+ATTAGGGGTTTGATTCTGGGTCAGGAGATGGAGGATCAAGCTGTGCAGCTGGGAACTCAC
+CTTGCTGTTCTGGGCTCTCCTTTCCCTCATGTTGGGCCCATGCAACTGCTCGTCGCTGCT
+CAGGACTCAGAAAGGCCATTTGCTCAGGAGTGACAGCCACAGCCTGAGCACTGGTGAGAC
+TAGATAGTTGGATGGGACTAAACACCACCTGAGGGCAGGGGTAGGAATCAGTGCATGCAT
+GTAGTCCCCATTGGGCCCTGGCTCTCCTGTGGTCACCCCAGTCCATTAATACTTACAGCA
+AATTTAGGAGGAGGGATGACAGAAATGGCAAGAGGAGTAACGCCCTGGATCTGTCCCCGC
+AGCAGTGCTGAAAGAGCCAGGTCTGGGATCCCAGCTGTTGAAGCAAGTGGCATCCAAACA
+TTGTCTTAGACTGACCTTCCCTCTCTTCAAACCTATAGACCTTCTCTAACTACTCCCAAA
+GTGCCCTATCATAGACCTTCCCCAATATGTCTCTAGCCCCTTATTTAAACACCCTCAGGC
+CCCCACCTTAAGAATTGCAGGGCAGTCTTCCATCCAGTCCACCCATGGTATAGAAACCAA
+ACCAACTTGCACCAGCAGTGGCCCAGCTCCCCACCTGCTATGGTGCCAATTTCAGTGAAG
+ATCTCAGGCCCCCAGTTACTGATTGGGCCAAACCCACCAGGCAGTACAAGTAGGTGGGCC
+AGAACCTCCAGTTGTTCCTCAGAGCACTGGAGATGCAGGGTGCCGAGGAAGAGAGCTGCT
+TGGCTGTAGAACAGTAGGAAGGAAGGAAGAAGAATTCGGCTTCAGTGAAAGGGGCTGTGG
+TCATGAGACAAAGGAAGAGATGGCTTCAAATGAGTTCCCTTCCTCCATGGGACCAGACCT
+TCATGATCCTTCTTTCCCCAGTAAGTCCACCTTTACCTCAGCACCACCACCCTCAGCCCC
+TTCACAAATGACCTGAACTCCCAACTGCTGATGTGCTGGAGCTCCTCTGGCCGCAGTCCA
+CAGAGAGTATAACCCAGCGCTGTCAGATGAACGAAGTCCAGGTGGCTCACATGCCGACCA
+CTCTGCCGTAGGAAACTGGAGACCACAATGCGGAGCTGGGGTGGGGGGTGGGAGAAGAGG
+GGAAGGAGGAAAGTTATGGAGAATTAATGGACAGGGAAGTGATAGGTGTTACTGGGTTAT
+ATTCTGTTACTATTAAGACCTAAGGAGTCATGGGGAAGGCTGAGGACTCAGAAAAGAAAA
+GGAAAGAAAAAGAGGAAGCCTCCAGGAAAAGAGGTAGGAGACAGTATTATGTGTCCAGGG
+CCTCAGAGTGAATAAATCAGAGTCCTGAAGGTCACTAGTATGGGGTATCAACAAAAGATA
+GAAAGAAGGACCAGGTAGGGTCACAGGAAAAAAATTCCTTGGGCTTTAGATGATCTATAG
+GGCTGGGTCTGTGGGATGGGTGTTTGGGAAGCCGTAGGGAGGAGGAAAAGTGTTACCTGA
+GTGGTGCTCCAGCCATCTATCTGCCCCAGGGTGCTCAGCACTCCCCAGTCCACTAGGATC
+AGCTCCTGTAGTTCCCGATCTCCTAGACCTATTAAGAGCCTACCAAGCTGCAGGATCTGC
+TCAGGACGAAATCCCCGGGGGGGACCCCACAACTAGGAGAAAGACAGGAACAATGTGAGT
+GGAAAAGCAGTGGATTGGGAGTCATACTGCTGGGTTTTAAGTCTTGCCTCTGCCCTTAGC
+TGTATAACTCTAGGTAAATCATTTGCCTTTTCTTTAGTTTCCTCCACTATAAAATGAGAC
+CGTTGCCTTACAGTTCCTCTAAGGTGTTTTGAAAGACATTACAATCAGTGGAAAAGAAGA
+GCAAACTAACTCTAGTCCATGAGTTCCACACTTTTATGTGCATCAGACACAGAGACGCTT
+ATTAAAACAGATGCCTAGGGCCCAGCACAGTGGCTAACAGCTGTAATCCCAGCACTTTGG
+GAGGCTGAGGTGGGAGGATTGCTTGAGCCCAGAAGTTCGAGACCATCCTGGGCAACATAG
+TGAAACCCCATCTCTACCAAAGATACAAAAATTAGCCAGGTGTGGTGCACCTGTAGTCCC
+AGCTACTTGAGAGGCTGAGGCAGGAGGATCGTTTGAACCCAGGATGTAGAGGTTACAGTG
+AGCCAAGATCACACCACTGCACTCCAGCCTGGATGCTGGGTGACAGAGTGAGACTCTGTC
+TCAAAAAAAAAAAAAAAAAAAAAAAAAGGAGATGCAGATGTCTAGACTCTTTCCCCCAGA
+GGCTTATTTTTTAATTTATGAGACAGGGTCTTGCTCTGACACCCAGGCTGGAGGGCAGTG
+GTGCGATCTTGGCACATTGCACCCTCCACCTCCTGCACTCATGGGATTCTCCTACCCCAG
+CCTCCTGAGTAGCTGGGATTACAGGCATGTGCCGCCACACCCAGCTAATGTTTTTTCTAT
+TTTTAGTAGAGACAGGGTTTCACCATGTTGCCCAGTCTGGTCTCTAACTCCTGGGCTCAA
+GCAATCCACCTGCCTCCGCCTCCCAAAGTGCTGTGATTACAGGCATGAGTCACTGCGCCC
+AGCCTCCCCAAAGGTTTTTATTAAGTCAGTGAAGCATGGTAATCTGGCACTGGCACTGTT
+CCCATGCTCAGTTCAGCAGCACATACCCCAAAAAATTGGAATGATACAGAGATTTGCATG
+GCGCCTGTGCAAGGATAACACGCAAATTCATGAAGCATGCCTTTTTTTTTTTTTTTTTTT
+TTTGAGATGGAGTCTTGCTCTGTCACCCAGGATGGAGTGCATTGGCTTGACTTCGGCTCA
+CTGCAAGCTCCCCCTCCCAGGTTCACGCCATTCTCCTGCCTCAGCCTCCCAAGTAGCTGG
+GACAACAAGTGTGCACCACCATGCCCGGCTAACTTTTTTGTATTTTTAGTAGAGACCGTG
+TTTCGCCGTGTTAGACAGGATGGTCTTGATCTCCTGACCTCGTGATCTGCCCGCCTTGGC
+CTCCCAAAGTTCTGAGATTATAGGCGTGAGCCGCTGCACCCAGCCGAAGCATGCCATTAT
+TTTTTTAAGAAAGAAAAAAAAATAAAGAAAAAAATCTGTTCCCTTGATGATCGTGATATG
+CATTAAAATTTGGTAACCACTGCTTTCGTCCCTCTATTCATTATACTAGCTCTCTTTCCT
+CAATATTTATCTCCCTTCACCTCCTACTTGTGACCCAAATCTTCTAACTCTTCTATCTCT
+TGCTTCCCCCACCTCTCATCCAACTCTCCATTCTCTTTGTGTCCTACATCACACCCAAAT
+AGCTTCCTCATGGCCAACCCCAGTTGGCTCTCCATCCCTAACCTGTTTTGCTTTGCCCAT
+GGCTGCCCGCAGTTCCTCAGGCCCAAGTCCTGGGTCTCCTGCAAATAATGTCAGGCAGTC
+CTCAAAGTCTGAGAGCTCCATCTCTGCAATCTGGGTTGCAGACCAGGCTGCTGGGAATGT
+CCCTCGTACATCTGCACAATTTGGCACAGGTTCTGAAGGGGGAAGGCAGGGCCAGGAGGT
+CAGCGCAGTAATAAAATATGCCCAGAGAGATATCTGTAGATAGAGTGAGTCTTCCAACCT
+TTGGAGGATAGAGCACTGTGAGAAATAGGGATCAAAGGAGTATTACAGAGTAATATGTAT
+AGGGCTTAGGAGATAATAGAACAAGAAGTGATTGGAGATGCCAAGACTTTTATAGATGGA
+AGACTGAGGATGTTATTCAGAGATTTAATGGTAGCACTGAATTTGAACCCAGTTCTCCAG
+CCTCACAATGTCTCCTTCAAAGCTTCTAGGGATCTCCCCAGCAGAGAGCTCCACACTTAG
+CCGAGCTAGAGCTGAGTCTAGAGCAGACACGAGAGAGCAGGAAAATGGAAGTTCTGGGCT
+AAAAGAAAACTTAATAGTTTACAAACTCCCAGAACTACAGAATTCTAGAACTACAAGAGG
+CTTGAAGATCATCCCTCTAAACTCTTTGCTTTATAAATTAGAAAACCCAGTCCCAGGGAA
+GAGCACATGTAGAACCCAGACCGTTTGATACTCCCTGTACATCCTGCTGGACATATAAGT
+ATTTGGGTAGTTTCACCTGGAAGATCCTCAGCAGCTGGTCGCACCACCCCTGCTACCAGG
+GCTGCTTTCTTGGCAGCAAGCTGTGGCTCCCTACACAGCTGTCCAACTCTGCTCTGCTCC
+CAGCTCTGCTGCTTTTCTAGAAGCCGCTCCAGGGTCTCTGGACCCAAGGCCTCCTGCATG
+AGAAGGTAGAAGGAGAGTGGGGAGATCTGGACAGATCAGGACCTGCTGCTATAGCTCTAA
+GTCCAAAGTCCTGTCTCTGTTTTGCAGTCTCCCCCCAGATCTAGGCTTCATATCCTTTGC
+CCTCTTTGGCCACGGGTCCCCATAACCAGCTCACCAGTCCCCTCTATGCATTTACTCCCT
+TCCCTTCTTCCTTCATCTCACCCTGGGGATCAAGGAAATTGCCTCAGTAGACAGAGTGAA
+TACTAGGCGTCCAGCTTGCTCTACTTCATCCTGGCTCCACAACTCTGGTTTCCTGGGGAC
+AGGAAGAAAATCGGGGGCTGGGGAGCTGAGGGAACTGTGAGGAAAAGGAAGGGGAAAAGA
+GGACATGCTAGGATTTCGGACACAGGGCTCCAGGGGACCTTAAGAATATGGAACAGGCTG
+CCACTGATGATGGTGGCTGAGGGACTGGGTATAGAATGAGTTAGAATCTGAAGTTCTCGA
+AGGTCCATACCCAAGAACAGACTCCTGCAATAGCAGCCATCCCAGCTCTGTGGCAAATGT
+CTCTCCTAGGCAGAAGCCTTGCAGCTGACTGAGATGGGACAGCAGGATCTGTAGGGGGAT
+CTGTCGTGTGCTCTCTGTCCCCAGGAATCCAACCAAAGGGCCTAAGGTCTCCAGCACTTC
+CCCTGAGACTGGAGTCTCCTTTGGAGCCTGGAGAAGAGCATCAGAACTTGGACAATGCAC
+TTCTGACTCAGAATACCAGACACCTTGATCAAGACACCAAGCCCCCTAACCTTCCCTCCC
+TCCTGCTCCCAGCTCAGCACCCTATGATGCTCACTACCTTTGTTCACTTCCTTAAGCAAT
+GAGCCCAGATAGGAGCAGGCAGAAAGACTGAGAGGTGGACTCCAAGAGATTTCTCGGACT
+CCAAGAGGTATGGACAAGTAACGTGAAGCATATTATCAAGGAACAGAACCCAGAGGCAAA
+ACAGGGGCCAGGCCTTGTAGACAGGAATCTGTTTGGCAGCAAGAAAGCAAGAAGTAGAGG
+GTTGGGGGACAGTCAGAGAGCATTGTCTGAGGAGCAAGAATTGCCCAGGGCAGCAAATCT
+GAGTCTGGTAGGGTGGACTCTTACCAGGTTTTGTAGTGCCCTCTCTGCCAGGGCTGCCTG
+GTGGAGGGGGGTCAGTGCCAGCAGCTGCTCTGGAGCTCTTTGCACCAGCTCCACCACCAA
+CATAATGGATTCATTGGATAGTCTGTCCATCAACTGGATCCTATTACAGCAATTTGACAA
+CAACAGGATTCAGGTGGAGCTGGGCCAAGTCGAGAAGGGACCACAAAACCCCACAGTCCG
+CAGCTAAGATGTGACCCCAGACCAAATTTAGTGAAGCTGGACAGGAACTGATAGTAAACA
+GCTCCAGGGCCAATTCCCACCATCAAGCTTGAGTGGGGGAGAAAAAGGGAGCAACATATT
+TCTAGTCTTCCTAAAAAAAAAAAATAACGAACAATCCTACCTGATCTAATGGACTCAAAA
+GCTCCAAATATTAAGTACCATTAACATTTCCCCATTTTATAGATTAAAAAACTGAGGTTC
+ACAGAGATCAAATGTTGAGGTCTCTCACTCCCAATTCCCGTTTTTTTCCACAGGACCACC
+CTTCCTCTGCTTGTGAAGAGGTCCCTTCTTGTTTGTACGTGCTATACAATTTACAAAGTT
+CTTTCAGGTGTTATCTCATTTGATCCTACAACAAGACCTGGCCTCACTCCATCACTCAGG
+CTGGAGCACAGTGGTGCTGCGATCTCAGTTCACTGCAACCCGCACCTCCCAGGTTCAAGC
+AATTCTCGTGCCTCAGCCTCCCGAATAGCTGGAATTACACGCACGTGCCACCACGCCCAG
+CTAACTTTTGTATTTTTAGTAGAGATGGTGTTTTGCCATGTTGGCCAGTCTGGTCTTGAA
+CACCTGACCTCCGTGATCCACCCACCTTGGCCTCCCCAAATGCTGGGATTATAGGCATGA
+GCCACTGCACCCAGACAAAATAGGTGTTTCTCTTATCCTTCTTTCACAAATGAGAAACTC
+AAGTTTTTTGATGCATGGTCTAGGATCTTTCACCTCATCTGTAACCTTGGGATTCTAAAT
+TATCTCACAGAACCCACATATTTAAACAGATCTGAATGGCATTAAAAAAAAGTAAAAACA
+GGCCGGACGCAGTGGCTCATGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCAGGCAGA
+TCACAGGGTCAGAAATTCGAGACCACCCTGAGCAACATGGTGAAACCCCGTCTCTACTAA
+AAATGCAAAAATTAGCCGGGTGTGGTGGCACGCGCCTGTAATCCCAGCTACTCAGCAGGC
+TGAGGCAGGAGAATTGCTTGAACCCCAGAGGGAGAGGTTGCAGTGAGCCGAGATGGCACC
+ATTGCACTCCAGCCTGGGTGACAGAGCGAGACTCTGTCTCAAAAATATAAATAAATAAAC
+AAATAAATAAATAAATCCCTTTTACCCGAAATCAGAGGTGATAACCTGTACCCTACCTAG
+GATTACCAGTTCTGGAACTGGGCTAAGTCATACAAGAGCTGAAATCTGTGGAAAGGCCTA
+TAAAAATATAAGAATGTTGGGAAGCCGAGGTGGGCAGATCACTTGAAGCCAGGAGTTCAA
+GACCAGCCTGGCCAACATGGTGAAAGCTCGTCCCTACAACAAATACAAAAATTAGCCTGG
+CATGGTGGTGCACACCTACAGTCCCAGCTACTCGGGAGACTGAGGCAGGAGAATTGCTTG
+AACCTGGAAGATGGAGGTTGCAGTGAGCCGAGATCACGTCACTGCACTCCAGCCTTGGTG
+ACACAGCAAAACTCTGTCTCAAAAAAAAAAAAAAAGAAAAAAAAGAAAAAAGTAGGAATG
+AAGTCAACTGCTTTTACTCCACTTCAGCTCCATATTCCCCAGGAAGACTGTAACACCAGC
+ATTTTCCTATCCTGACTTACAGTGCGGATGGCAACGGGGTGGTGGTAGGGGTAAAATGAG
+AAAAGCAGCATATGAGTAACATACTAATAAATTTCTCCATGGGTAGGGAGGAGCCTTGGG
+TTCCTATAGCCTTTTCTTCCCACAACCTGTATATGAACGTGCTCTACAACATTCCTGCCA
+TGGGGCCATCTGGCTTAGGCTCGAACAGCTCCAAGGACCAGGAACTCACTACCTTAGTTT
+TTCTTATACTATGTAAAAATCTGATCTCCGTTAACTACTCTTAGTCTTGCCCAATGGGGC
+CACTCATAAATATGACAATCTAATTTCTACTTGATAGCCCCTCAGGTATTTGAAGGTATT
+TATCACATTTTTCATATATTTTTCTCTCGATCTACTCCTCTGAATGCACTAAGAACACAG
+TGCCCTGAGCAAACTACAATCCTCTGGGGCAGATTTGGAGCATTGCCTCCCTCACTTCAG
+ATGCTCTGTCTCAATCTCAATTAATGTGGACTAGGTTATTGTAAGATTACTTGGCAGGCT
+TCAATACAGTGTTGCCACCCTCAGCTGCCCTGTGCTGGAGCATATTCTGGGAACCAGTCA
+ATACATAGAGCAACTTTGAATAAAATCCTCTGCTTTGGGCTATAAATTATGTCAGGGAAC
+TACCAGACAGAAAAACTACCTCCTCCAGGGCATTCCCTAAGGGCAGATCTTCACCCCAGA
+TTGAGCTTTCTGAGGGGCCAATATCTCTAGCTGCAGTACTTACGGTAAGTCCAGGAGTAG
+CTTGCTATCCAGCCCGTTCAGTTCTGGCCCTACAGTTGTCCATTCTGGTTCTGGCATTGC
+CATCCTCCGCTGTAGCTCTGCCCAGATACAGGCCCTCTGTAGGGAAGCAGTGTGAGGCCA
+GAGCAGAACATAGGAGCTGGGTTCTATACCTAGGGTCCCAGCCTCCCTGCTCCCACTAAA
+GTCCAGGCACCCCCTCTCACCAGGCTCCCTCGAACTCTAGTGGGCAGCTGATAGATCATG
+TGCACCACTTCAAGGAAGTCTACCATGGAGTTGATCTGCTGCAGAAACTCACAGGACATG
+CCTCCTGCCAGGGTGCCCAGAGCCCTGTGGGTGTGTGAGTGGGGAGAGGCTCATTCAACA
+CATACAACAGCCTGTTTGCTCCTTGATATCAGTACTCTCAACACAAGTACAGATGTTCAT
+CCACCGTAATTTATGGTTTGAGAAATGTTTTTACATAGATATCTCATCAGCTCCCCATAA
+CATCACTGCTGTTTATCAGAGGAGAAAATAAGGATTTATGGAAGTCAGGTGACATTCCCA
+ACATCATTCTGCTAGAAATGTGGTAAACTGAAACTAGAGCCATGTCTTAGATTCTGAAGC
+CCTTGGGAGGCTGAGGCGGGTGGATCACCTGAGGTCAGGAGTTTGAGACCAGCCTGGCCA
+AAATGGTGAAACCCCATCTCTACTAAAAATACAAAAATTAGCTGGGTATGGTGGCACATT
+CCTGTAATCCCAGCTACTCCAGAGGCTGAGACAGGAGAATCGCTTGAACCTGGGAGGCAG
+AGGTTGCAGTGAGCCGAAATCGCGCCACTGCACTCCAGCCTGGGCAACAGAGCAAGACTG
+TCTCGAAAAAAAAAAAAAAAAAAAGATTCTGAAGCCCATTGTTCTTCTAATGTGGGTGTA
+AGTAAAGTGATACCTTCTTATTCCTATTTATTCTTGCTTGGCCAGTGCCTCTGAAGTCAT
+CCTGAAGTAAACTAACAGTAGCAAATGACTACTGGGACTTTACAATGGACCAAACACTGT
+GTTAAATATCTTACATGACCTACCTCATTTAATCTTCACAGTAACTACCTATGAGGCTGG
+TGCCATTGTAATTCTCATTTAAAGAAGGGAAAACTGACACAGGGACGTTAAATGACTTGC
+CCAAGAGGACAAGTAGGTGACAGGACTGGAACCTGAATCCAGGTTTTCTGAGTCCTTTGG
+CTCTAGTCAGGATAGGCATGGCACTGTGGAAGGAAAGGAGGGCAAAGGGAGGTGCTAGGA
+GAACGTCCACGAGGCAGGGACTATGCATCATTCATCCCTATATCCCCCATTCCATATCAC
+ATGGTGCCTGGCACATAGTAAGCACTCAAAAAAATGTTGGTCGAATTCAGCGCACTGCTC
+AACACAAGTTACTCACTGCAGATTCCTGAGGGTAAGGTTGGTGGGTACTTGCATCTTCTT
+CCAGAGAAACTGTGCCTACAAGAGAAAGAAAGACGAGCCCCTTCCCAGAAGAGACACTGT
+CCAAGGATACCCCCTAGAGTGGAGAGGCAGGACTGCCTTGGACCCAGTCCTGCCTCCTCA
+CTCTGTGGGACCCACCAGCCTCCCACTCTCCCAGATGCCCACTCTTCTCTCGAGAGTGAG
+AAAGAAATGAAAGAAAAGGGAAGGAGAAAGAAAAAGAAAAGCAAGTCACATTATAAGAGA
+TACTAGGGGGCTGGGTGCAGTGGCTCAGGTCTGTAATCCCAGCACTTTGGGAGGCCAAGG
+CAGGAGGATTGCTTGAGGCCAGGAGTTCAAGACCAATCTGGACAGCATAGTACCTCAACA
+TAGTGTCTCCACATAGTGTCCACATTTTTGTATTGTCTGTCTCTACAAAAAATTTAAAAA
+TTGGCCGGGCATGGTGGCTCACACCTGTAATCCCAGCACTTTGAGAGGCAGAGGCAGGCA
+GATCACAAGGTCAGCAGTTCGAGACCAGCCTGGCCAATATGGTGAAACCCTGTCTCTACT
+AAAACAAAAAAAAAATTAGCCAGGCATTGTGGGGAGTGCCTGTAGTCCCAGCTACTCGGG
+AGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGACAGAGGTTGCAGTGAGCCAAGCTTG
+TGCCACTGTACTCAAGCCTGGGTGACAGAGCAAGACTTCATCTCAAAAAACAAAAAAAAA
+ATTTAAAAATTAGCCAGGCATGGTGGTAACCACCTGTCGTCCTAGCTATTCAGGAGGCTG
+AGGCAGAAAGATTGCCTGAGCTCAGGAGTTTGAGGTTACAGCGAACTCTGATCATGCCAC
+TGCACTGCAGCCTGGGCAACAGAGTGAGACTGTATCTCAAACAATCAAATAAAGGATAGT
+AGGGATAAGCTGGCCAAATAGGGCTAAGGGATAGGTAAAGAAGGTAGACTACATTGAGGG
+AGGAAGTTCTGAAATTAAGTGGGGAGAATTACCTGCTGCTCAGACCAGGGCAGCTCCCAG
+TAGCGTCTTCGATTTGCCAGAAGAGCCAAGGAATCCAGTTGTAGCAGCTTTAATGGGAGC
+AGGGGAAGCAGGCAGTCTGGCCAGGTGGTGGGAATAGGCTGCTGGCGGTGATGGGTATAG
+CAGTGTAGTGATAGGTGAGAGAGTCTGTACTTAGCACTCAGAGAAAAGGAACCATGGGGG
+TGGAAAGGGACCAAAGCTAGGACAGAAGTGGAATGGCATTTGCCACTGTAGCAATAAACG
+CCTAAGAGCCTCACACTGCAGGCTGCTGTGGTCAAGTGTTGCTGCTAGTTAGGCACCAGG
+CAAACAAAGTCCCTTAGCTTCTCCCAGCCTTGGTCTTTTCATCTGAAAGCAGGGTGGGTG
+GCCTGGAAGATTTCTCAGGCCCTTCCAGCTTTGACATTAGTCTAGGACAATGTGAGTGGA
+TCATGCTGTCCTGCATCTGGCACTGGGGAGGGCTGCTAATGGGCACAGAGCTAACCAGAA
+CTCTCAGGGCCACTGCAGGGTAGTGTGGGAGGTAGCACCAGCCATATGAAACTGCCCCAG
+AATGGGGAGAGGAGCTCAGTTGGGAGATCTCACACTTACCTGACCAGGGATACACACAGC
+TGGACCAGCACCTGTTGTACCCATATTTTTAACACCATCTTTAACCTGCATGAGAATTGG
+TTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTGTAAGTGGGGAGGTATGAAAGG
+CCTTCCCTGGCCTCAGGGAAGATGCCTTCCTCCCAACCAGAAAGAGCCGGTATCCCTGAT
+TATCTCATCCTCCTTGCCACTCTCATACCCGAAAGGTCTGCAGCAGTGCTGCGGTCTGGC
+AGGCTGAGAGGCGTGACAGTTCAGGGGCCAGGCAGGAACAAGCCCCGACCAGGACTCGCC
+TAGGGATGGCCTGGAGTGTCTGGGGGCTGAGGCCTGGTAGCAGAAGGTGCAAGGAGCAGA
+GTTCCTCCAGGGATAGCTAAAGAGCAAGAGAGACAAGAGGCCTGAAGAAGAAGGGAAGGG
+TGTTGGGGAAGACAACAATCACAATGCAGCAAGGCAGTAAGTATGAGGGGAGCGGAGAGA
+GAGGAGGGGCAGATGCAGGAGCCAGGTTAAAAGAGGATAGAGACCTCTGGCGGGAGGCTG
+AGAAGTTGCTGCTACTCACATCGTGCCTAGGAAGGAGCCGTCCAAGCAGCAGGACAGCCT
+GTGTTGGGATGGGACCGAAAACAACAGCTCTCAGGACCCAGCAGCCAGGTCCTAAGTGGG
+TTCCTAAGGCAAACCCTCCAAAACTTCCCGCTGCCTCTTAACCATCCCTAGTAACCATCC
+TCAGTGACTCAGGTCCCTTCTTGATCTGAGGAAAGGGAATGAAGGCGTCCTCCTGCAGAC
+AGAGTTTACCTCTACTGTTCACCCAGGGAAAGGAGGGGCTGCTTTTATCCCTGAATGGGA
+TTCTCTTGACTGGGGCTCAAGCGGGGATGGAGGGTACATGCCAGGGAGTGAGACAGGCAA
+ACCTGAGCAGGTGTAACACTAGTTCCCTGCAGGACAGGAAGCATGGCTCTAAGCTGGGGC
+TCTGACAGCTCCTGAAGGAAGCGGAGGCCCAGCTGAGAGAAGAGAGGGGCCCAGACCCGC
+AGCTCCCGGGGGCTCAGCACCGCTCCTCCAGATGAGCGCAACACACCCAGAAGTTCATAT
+GCCACCTGTAACCAAAGAAGGTTTAGGACTGGAGAGAAAAGACAGATGAACCTTGAACTT
+CCTCTCTAATCCCACATCTGAATTTCCCAGGGCCTGGGCTAGGGTTTGGAACTAGGGATT
+GGACTGGAGTAGATTAGGTTCAAAATGGCAAAGGGTATGTTTGGGGTGCTACAGACCAGA
+TAGAGAAGGGCCAGGAAGAGGTGGTAACAGGTAAGAATGGCCATGGAGTAAGGAATGGAG
+GTTGCAAAAGTGGGATGGGGGCTGGCACCACTGTGCTCAAGTTGACACAATGGGAAAGCC
+ATCCACACAGACCCAGGGGAAGCCTAAAGTCTTGTAGGCTTGTGCTGAGGGGCTCACCCG
+TCCTTCTGGGCTGAGGGTCCCATTGGCTGCACATTCCAGCAGCCCCCGTTCTACTGGCCC
+CGTTGGATCACTCAGGGGCACTAGGCTCTGCAGCTCCTCAGGGCTCAGGAAACAGGCGAG
+GGGCCCAAGCCTGAGGAGGGCATGAAGCTGACCTTTGTGTGGTCCCCAAGACTAGCACTA
+AGGCAGGCCTGGCAGCAGATGGTATGGGTACATACACTGGGCACTCTGACACTACACCAC
+TACACAGGGGCACCATCTATAGACCTCTCTCCTGGAACTCTATGCTGCCTGAGGCCACTG
+CCTACTCTCTTGCCCCTTTCTTCCTAGAACACCGACCCAGCGTGACAGCTGTGCCTTCCT
+CTCTCTACCTCTTCCACTCTTGCCTTGGTTACTGATCCCACAACAACTCACCTGCGTACC
+TGCTCCTCACCATCCTGGACACTCTGGTTTACCAGGCTGCGCAGCACATGGCGGGCATGC
+CCTGGCCCCAGACCTGCTGCTGGCCAGCTATCCTCCAGGGCCTGGATCTGAGATGGGGAA
+GGTTAGCTCGCACTGGGGTCACTATAGGGTTCTTGCAGGGAGGGGCCACTGAGAGACATG
+CCATTGACTCTTTGTCCCCACTAGCAGAAGATGGGCCAGTCAAGTAAAGAAGATGATTCT
+CATACCTGGTGAGGGCTGAGCTGCAAAAAGTTCTCCAGAGGGAGGTGGGGGAGCAGGGGC
+AGCACTGCCCACAGCAGCTCCTGGGGCCAGGCAGGCACTTCCCCAAACAGTTCAGGGGCC
+AGCAGTCGCTTTGCCAGAGCCTCCTTCTGTTCAGGCCTCATTCCTGGGCTGTAATCCCGG
+ATGGCAGCCAGGCTGCGAGGAGTCATGGGTCTTAACCCTTTGTCTTCCTCCAAACTGTTT
+TCCTCTGACCCTCTGTAGCCCTGCTGTCTAGATAGGAAGGAGACTCTCCCTGTTTTTTTG
+TTTTGTTTTGTTTTTTGTTTTTTTTAAGACGGAGTCTCGCTCTGTCACCCAGGCTGGAGT
+GCAGTGGCACGATCTTGGTTCACTGCAACCTCTGCCTCCCAGGTTCAAGCTATCCTCCTG
+CCTCAGCCTCCAGAGTAACTGGGACTACAAGCGCCCACCACCATGCCTGGCTAATTTTTG
+TAGTTTAATAGAGACGGGGTTTCACCATATTGGCCAGGCTGGTCTCGAACTCACTAGGCG
+GACCTAGTGATCCACCTGCCTCGGGCTCCCAACGTGCTGGGATTACAGGCATGAGCCACC
+ACGCCCATCCTCTCCCTGGTTTTAATAGAGAGGAGCTCTCTGATCCTTTTGTAGTTCATT
+AGCATAATGATTGGGTTTTCACACTCAGGCGTGAGATGTGCCTCTCTCAAACCTTGCTAC
+GATGTTGGCACATTGCCTATCTGGCATGAAAGAAAAAAACAGAGAGGAGCTCCGGAAGGG
+GCTGCTCCAGGTGGATGCGGTTGGCCTGACCGTGACAGGAGCAGGAGGAGTAGTGCAAGA
+ACCTTACACACTGTCGTTGGCTAACAGGGATGGTGGGAAGCGCATCAGGTCAGAGACAGC
+CAAGAAAGGGATGAGTGGTGACAGGTCAATGAAGAGCTGGGAGGTGAGGCGTGGGTACCG
+CTGGAGCAGCAGGGCTGTCAGGCGACCCAGGGCCTGCTCCTCGGATGGTGGTACCTGTAG
+GGGCACAGGAATGGATTCTGCCTCTGGAGATGCTCAGTATCCCTGCCATTTCCTCTCTGG
+AGTTCCTCCTCCCACTAAAGCAAGCCCTCTGAACACTAGGCTCCAGGTGCCCTTGCTCCC
+CTTTCTCAGTGCTCACCTGCAGCTTCCCCTGCAGCTTCCCCTGCAGCATGAGTGTCAGGA
+AGCCCTGTGCAGCCTCCCTCTCTGCTGAAAGCACCAGCTGCTGGAGGTTTTCTGGGGGCA
+TATGCAGGTACGCCTGCGAATAGGAGGTCATGGTGGGTATGGCCTCACCTCACGGGGCAG
+GGACCTCCAGCCATGGCTGTCACCCAGCCCACCCATGTGCCCTCCACCTGTTACCTGCAC
+TAGAATCTGCAGGGCCCAAACACTCTTTTCCCTCTGGAGCAGATCCCACAGCACAGGCTG
+GTGGGAAGAAAGACAATATGCCAACAGAGCTGTCTTCTCTGTCTCTCCTGCAGCTCCCCC
+AGGCATTCCAGCTCCACTTGCTGGGATGCTTGTCCATCATCTCAAGTGTGATTCTTCAGA
+TATTAAGCTCTTTTAGGTCCGGGATCATATCTCTAATTTCTCTTGTACCCTCTCCCATGC
+CAGGTCCATAGTTGGCTCAATTAATACTTGTAGACCTGAACCAAATACTATGAGACTATC
+TAATTCCATTTTACTGGGCCCAGGGTTTGAAAAAGGTGGCCCCAACATGGAGTAAGAAAT
+CTTTATATATCCTACAGAACCTAGCAAAGTGCCTTGCATATAATAGGCACTCAGTGAATT
+AATTATGGTGTTTAACATATTCTCACCCCTCCATTCTACAGACTAAAAACTGAAGCCCAG
+AAAAACTAAATGAAATTGCTTGCCTAAGATCACACTAATTTGTGGCACAGTTGAACCTAG
+AACCAAAGTCTTCTGATTGGTAGTGTCCCTGAATCTTTCTCATTCCTACCTTATCTTCCT
+GTATTCTGCCAGCCTCCAATTCTCACTCTCTAGGGGAAAAATTTAGAGTCCTCTAACTTG
+ATCCTTTTTCTTTCTGGTGCAGAAAGTGAGAGAGTCAAAGAGCCCAAAAGAATAACAAGG
+TAATATTTATTGCATGTTTGTGTATCATGCACTGTGCTAAGCCCACAGCATGTATTATCT
+CATATACCATTATCATCCCTAGTTTATAAATGAGACGAGAAAAATATTGCTCAGAGAAGT
+TAAATAACTCATTCAAGGCTGGTCACAGAACCAAGATATGAATCCAAGCCTGTCTGACTC
+TAGAGCTGTGTGCTTCAACTACTACCCCACACTACTGCCTCTGAGTATTCGAGGAATTCC
+CCTGGAGGGCCTTCTCACTGTTCTAGGAGCTTTCCCTCTGGCAGAGCACTCACACTAAAG
+CAGGCCAGCAGCTCCATCTTGCTTATACCAGAGCTGGGGTTGACAGTGGGTTCAAAGCCT
+GATGGGGTTGGCTGCTCCTCATCTTGTTCCAGGTATTCCCCAATCGTCCGTAGCACACTG
+CGCCGGCCCTCTGGGCGAAAGGCATCCCAGAAGGAGCAGTTGTCTGGGAGACTGGAGAGC
+AGTAGGGCCCGACCCAGCATCCCCTGGGCCTCAGCGCCCCCAGCCCCTGGACCCAAGAGG
+AAGGTCAGCAGGCGGAGGAGATAGTGTAGGCGTGTGGGGTGAGCAAGAGCTGGGACAGAG
+GACTGACAGCGTGGCAACTGGGATAGCATGCCAAGGAGGAAGGGGCCAGGGGTCAGACAG
+AGTGGGGATGGTCCCAGTGGTGGCAGAGAGGGCAGAAGGGGGCCCAGCAGCCCTTCTAGG
+AAGCAAGTGTCATTGCCCCCACGACTTATCCTGCATTGGCCTGCTAGCCAAGGCCAGAAG
+GGCACCAGGACCTCATACATGGTGTCATTGGCACAGACCATCACCAGGAAGCTGCCCCCA
+TCCGGGCAGCGTTCCCCACAGGGTCCAATGTGGCATGGTGGGGAGGCAGTGACATCTGGG
+GTGGGGCCCTGGCACACATGCTGGACCCAAGCCTGGTTGCTGGGGGGCACAGCCTGTAGA
+CTTGCCTCCCCACACAGTCGCTCAGCCCACAGAGTCTCATTCTCCAAGAAGCAGCCCCAA
+AAGATGTCTGGGGTGAGGGGAACAGGGGGCAGGCCTTCAGGGCAGCTGGTAGGGGGTGGG
+AGCAGGCCAGCACAGAGCCGCTTCACCAGGCGGCGGTTGGAGCCAGACAGGGCTGAAAAG
+GAGAGGTTACTGCAGATCGCATCCAAAAACTCATCAGGAAACTGGTCGTGGCAGGCCTGT
+AGCCAGCCTTGGGCACCTGGTGCCCAGGACACTGCATACCACACAGCTGTCTGGCAGATG
+GCAGTGGTGCTGGGATGGGGCTGTGGAGTGGCAGGCTTGGTGTGCTGGCAGAGCAAGTGG
+ATGGAGAAGTTGGAAATGCTGTAGGGTGGTGCTGGGCCTAAGTGGTTCTCACAGAGGGCC
+TCCACAGTGATGGCTCGCCGTTGGCGTGGGCTGATGTGGGCTGACGGCTGAGAAGCTCTG
+GGCAGAGGCACGCCCGTGCTCAGGCAGTGAAGGAGGGCAGGGGGTGGGGGTGGTGATCCA
+GACAGAAAGCCCAGCGCCTGGACATCCCAGGAAAGGTTGTGCCGGACGCCCCTGGGTGCA
+GAGGGAGGAGCAGGCAGGATCTGGTCAGTTCACATTTCCTCCAGCTGAAGATTCTGACCC
+TGACTCAGAGCCCTCAAGGGGCATGGCAAGCATAGGCTTTTCTACAAGCGAGGTCCCTGA
+GAGTTTAGGCGTTACTGGTTGAAATGCTGCAACGGGGCAAAAAAGAGAAAGCTGCCCTGC
+CAAGGTCCAAAATCACCTAGGAGAAGCCCCAGTTGGAATTCTTTCTGTCCACCTGGCCCC
+CTTCTGTCTCCTTTCTTCGTATGCTTTTAGATAGCTTAAACACAACCCTCAGCGGGCCTC
+ATGTTAGGAAATCTGCTCAGCAACTCAATATGTCTAACTACTGTCTGGCATTGTTGTACT
+GAAGTAGTAAGGGGGTAGAGGAATCCAGCTGTGTCCTTATTTTCCAAATCCCATCTTTAC
+TAGCTAACATTATTAAGCGCTATGTGCCAGCACGGTTTTAAGTCGTTTGCATACACAGTA
+TCAACTCATTTAACCGGGTGCAACAACTCTGTGGTAACTAATATTATCATTCTCATTTTA
+TAAATGGGGAAACTGAGGTATAGAAAGACTATGTAACCTGCTCAAGGTCATATGGCTAGG
+AAGAGGTGGAGCTGGGACACCAACCCAGACAGTCACACCCCAAAACCACTAAACTACACT
+CCTCCCATCAGTTTTCCTCTCTAGAGGCTGAGGTCTTCAGCTCTTCACCTCCAGATTTTC
+CAGGCCCAATCCCTCAGAACTGGTCTCCTGTTACTTACCATAAGAGCAGCTGTTGAAGGT
+TACCTAGGAGGGAAAGAGTAAGGAAGAAAACTACCCCAATTTCACTTTCCTTGCCCTGCC
+ACATCCCAGTCCCAGCCCTGGCCACACTCACCTCCCTGGCACTGCCCATTGGTATCAGGC
+TCTGGCTGCCCCAAAATGGAGAAGACCTCATCCTGCAGGGAGTGAGTGACACGGAGCAGC
+CCCTCCTGAAAGGCAGCATAGAGGGGGGCCCCCACTGTGCGTAGCAGACCGCCCCAAAGA
+GCCTCCTTGGAGCCTAGCTCCCCTGTTGGGGTAAGCAAACCCAACAGACCCTGCAAAAAG
+TGAGGAGCTGCCTCCCTCCCATCGAGGCCTGTGGCATTGGTGGGGTCCACACTGGGCTGC
+ACCTGCACCAGAGCTTGCCAGCGTGTGCCCTCTAACAACAGCAGCAGAGAAGGCAACCAG
+TCAGCAGCCAGGACACAGTCAGACGGCCCATCACGGGTGCATGGGGGCCGAGTTGGGGTA
+GGGGGGCCCCCAGGAACTAAGGCTCCCAGCAGCACCTCCACAAGTCCACCCAGCACCCCT
+GCCTGGTGCACCAGGAAATCTCGGGGAGTCTGCTCCTGTCCCAGCAGTGCCAGCATATCC
+CCTAGCAGCCCTAGCATTGGCTCCCAGTCGGGGCTACCTCTCAGTGTCACTAGAAAATCA
+TGGAGCCGCAGAGCAGGCGGCTGGAGAGGTGGGGGCTCTCCTACTGGTCCTTCCCCCATT
+CTCCCAGGCTCAAAGGAAGAAGAAATGTTGGCCAGGAATGTAAAGAACCGTGAGCGGCTC
+AGGGAGCCCTGGGGAGCCTGGTCCAGAGTGGAGAGCAATGACTTCAGGAAGGAGAGACCA
+GGGTCCAGGGAATGAGGCCCAGTAGGGGCCAGAGTCACTGTAAGGAGAGAAACCAGAGGT
+CACTGAAGGAGAGGAACACAGAGCCCAAACTCAACCCTGCCCCTGAGCACAGTTCCCTAC
+CTGGATCTAAAGATGAGGTGAGGGGATGGTGAGCTGAACCCCTTTCACTGGCCTACAGTA
+AGTCTTGGCCTGCTTTTCTTAACCCTCATTTTTCCCTTTTGCACAAGTCTCTGCCTCTCT
+CCTTTGTCCTTCTATCTAACAGGTTCACCTCCATATTCTTAAAGTCTTTTTCCAGCCACC
+CTCCTCCTCATCCCCAGTTCTGCTCACTGTTCTTCTTACCTGCAAAGGACAGCAGCAGCA
+GCAGCAGCAGCAGCAGCAGCAGGGGCCAGAGGCTGAGAGCCATGTTTCCAAGTGAACACT
+GGTACCGGAGGTGAGTTCTGGTTATTCTCACCTGTGTGGGATAGCCAGGTGAGGGCAGGG
+CACTGCAGGCAACCTGAGGCTCCACTGACACTGTAGTGTGGTCTTTCAGGAAACAATATG
+TGTAACCTGACAGCAGGTTTGTTACCTGAGCCGCTGAATATCTGATCCTTTAGCTCTGGA
+GAAGGGTATGCTTCTGTGAGAGGGACTAATGATAGGGGATCCCAGGGGCCCCTCAGAGAA
+ACCCAAGGAGATTGCTTGAGTTAGGAGCCAGTGATGCAGAAAGGAACAGGCAGACATGGA
+GATGGAGAACTGGAGACCAGGGGTGTAATCTGGGGTTCTGCAGAAGCAAAGAAAACAAAG
+AGGATATGAAGGAGCTAAGAAGCAAGTAGGATTTGAGGAAATTGAAGAAGAAATGACGCC
+CAGGAGAAACAAACTGCACAGCAAGGTATAAACAGACGAGAGGTCCAGTCCAAGGATGGA
+GAATTCAGGAAGAGGAGAGCTGCTTTCAACTACTACCCAGAACCACAGAGTGTCAAGAGC
+TGAGCAGTACCCCAGAGATCACATACACCAAACTTTTTCACTTATGGATAAGGAAACAGA
+CCCAGAGAAATGTGATTTGCTCATTAGGCCATTCAAATGTTTGGGTCTTTCCTTCCCCCT
+CCGGGATCCCCTATCATTTGGTTCTTTCTCTGTGGCCTAGGTGAAAGCCCTATCAAAAAC
+TCTGAGCTGAGAAGACAGAAACCAGATTAAATCACTATGCACAGGGACTGATCTCCCTAC
+ACACAGAACTGCTCATGGAACAGAGAAAGAGATTTCATTCAAAATAATCTGGTCTGGTCA
+GGGTTAGAAGTCTTTTTTCGTCATTTTTGTTTTTTGTTTTATTGGTTTTTTGGTTTTGGT
+TTTTTTGAGATGGAATCTCTCTCTGTTGCCCAGGCTGGAGTTCAGTGGGGCTATCTGACC
+ACTGCAACCCCTGCCTCCTGGGTTCAAGCGATTTTCCTGCCTCAGCCTCCCAAGTAGCTG
+GGATTACAGGCACGTGCCACCACACCCAGCTAATTTTTGTATTTTTAGTAGAGATGGGGT
+TTCACCATGTTGGCCAGGCAGGTCTTGAACTCCTGACCTCAAGTGATCTGCCCACCTCAG
+CCTCCCAAAGTGCTGGGGTTACAGGTGTGAGCCACCGCGGCATTTTTTTTTTTTTTTTTG
+AGATGGAGTCTCACTCTGTTACCCAGGCTGGAGTGCAGTGGCACTATCTTGGCTCACTGC
+A
```

### Comparing `paraphase-2.0.0/paraphase/data/neb/homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/neb/homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/neb/ref.fa` & `paraphase-2.1.0/paraphase/data/neb/ref.fa`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/pms2/pms2_homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/pms2/pms2_homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/pms2/pms2_ref.fa` & `paraphase-2.1.0/paraphase/data/pms2/pms2_ref.fa`

 * *Files 24% similar despite different names*

```diff
@@ -1,427 +1,885 @@
->chr7_5967000_5992500
-CTCTTGCCTAGTGGTGTTGCCATCTTGTTTGGAAAAGTCTAGATTATCAGAGAGAGATGA
-GGGAGAGCGGGCAGACTTCTCCCCTTTTTTGTCTGCTTTTTTCTTTTCTTTCACCATTGC
-CTTGGGAAGATCCAATGGTTACTTGAATCAAATGATTTCTTTGGTTCAGAGCTGCTTGTT
-TCAAAGCACTGATGAGTTTTATCTGAAAAATAAAAATTACGTCTCCAAACACTTGGGGTT
-TTCATTTGTAGTTAAAATTTCAGTTTTACAACACAATGTCATTATCATTCTCCTGACAAA
-GTCTGAAAAATTAGTTACCAGGGCCGGGTGTGGTGGCTCACACCTGCGATCTCAGCACGT
-TGAAGGGCCAAGGTGGGAGGATCATGTGAGTCCAGGAGAGGGAGATCAGCCTAGGCCACG
-TAGTGAGATGCCACCTCTCTACAAAAAATAAAAATAAATTAGCCAGGCGTGGTGGCACAT
-GCCTGTAGTCCCAGCTACTAGGGAGGCTCAGGTGGGAGGACTGCTTGAGCCTGGGAGGTC
-GAGGCTGCAGTGAGTAGTGTCACACCACTGCACTCCAGTCTGGGTATCAGAGCAAGACTC
-TGTCTCAAAAATGACTATAATTACAAGTTTCAAGTACCATCAGTTTATAAAAATACAACC
-TCAACATCGCATTGCTTGTTCCTAAAATTTTTTTATTTTTAATTTTTGAGACAGAGTCTC
-ACTCTGTCACCCAGGCTGGAGGGCAGTGGCACAATCACAGCTCACTCTAGCCTCAACCTC
-CTAGGCTCTGACGATCCTTCCATCTCAGCCTCCCAAGTAGCTGGGACCACAGGCATGCAT
-TACCACACCTGGCTAATTTTTTGTAGAGACAGGGTCTTGCTATCTTGCCCCGGCTGGTCT
-GGAACTCCTGAGCTCAAGCAATCCGCCTGTCTCAGCCTCCCAAAGTGCTGGGATTATAGG
-TGTGAGCCACTGTACCTTGCCCCAAAAATTATTTAAGTTGGAACCATTGTCTAGCATTGT
-TTCTTGAAAGGTAACCCTACACATGAAATAGGCTACTTCACCTCTCAGGTCTTGCATGCA
-GCCAATTCACACTTTAAAAGCCCCTCTCTGGCCGGATGCAGTGGCTCACACCTGTAGTCC
-CAGCACTTTGGGAGGCCAAGGCAGGTGGATCACGAGGTCAGGAGATTGAGACCACCCTGG
-CTAACACTGTGAAACCCCGTCTCTACTAAAAATACAAAAAATTAGCCAGGCATGGTGGCA
-CATGCCTGTAATCCCAGCTACTCAGGAGGCTGAGGCAGGAGAATCACTTGAACCCAGGAG
-GTGGAGGTTGCAGTGAGCCGAGATCACACCACTGCACTCTAGCCTCGGCAACAGAGCAAG
-ATTCTGTCTCAAAAAAAACAAAACAAAACAAAAGCCCCTCTCCTTATAGGTCAGCATTGT
-AAAGTGTGCAAGAGCTGGATTCGGAGTCCTGCATTGCCCATTACCAGTTCTATGGGTTTG
-TTTATTTATTTATTTATTTATTTTTGAGACGGAGTCTCACTCTCTTGCCCAGGCTGGAGT
-GCGGTGGTGCGATCTTGGCTCACTGCAAGCTCCACCTCCCGGGTTCATGCCATTCTCCTG
-CCTCAGCCTCCTGAGTAGCTAGGACTACAGGCGCCCACCACCACACCTGGCTAATTCTTT
-TTGTATTTTTAGTAGAGACGGGGTTTCACCGGGTTAGCCAGGATGGTCTCAATCTCCTGA
-CCTCGTGATCTGCCCGCCTTGGCCTCCAAAGTGCTGGGATTACAGGCGTGAGTCACCGGG
-TGTGGGTGCCCGGCCCAGTTCTGTGTTTTTTGGGTTTGTTTTTTTTTTTTTTTTTAGACA
-GACTCTCTAGCCCTGTCCTGCAGGTTGGAATGCAGTGGCAGGATCTTGGCTCACTGGCTC
-ACTGCAACCTCACTGCAGGTTCAAGTGATTCTCCTGCCTCAGCCTCTCGAGTAGCTGGGA
-TTACAGGCACCTGCCTCCATACTCAGCTAATTTTTGTATTTTTAGTAGAGATGGGGTTTC
-ACTGTGTTGGCCAGGCTGGTGTCGAACTCCTGACCTCGTGATCTGCCCGCCTTGGCCTCC
-CAAAGTGCTGGGATAACAAGTGTGAGCCACCGTGCCTGGCTGGTTTCCTTTTTTTTTTTT
-TTTTTTTTTTTTTTTTTTGAGACGGGGTGTTGTACATTTTGCCCAGGCTGGTTTCAAACT
-CCTGGCCTCAAGCAATCTTCCCACCTTCTCCTCCCAAAGTGCTAGGATTGCGGGCATGAG
-CCACTGAGCTCGGCCAAGTGCTGTGTTCTGAAGCAAGCTGCTTAATCTCCTCTGCCTCAC
-AAATAGAAATAACAGAACCTTGTCTCATAAGAATTAAACCGATGACACACAGAAAAATCC
-CTAAGTACAGGATACAGAGCAAAGTCAATAAATTGAGTGATTATCTCGTCCCTTTCCTGT
-TTTCAAACTTGAAATCATTGGTTTCCCACTCCCTCTAGCACTGCCATCGATTGAGTGCCT
-CTCATATGCCGGACAAGCAAGGACCGGTGTGCTGGAGTTGCGTTTCCAGCGCATGGTTGC
-TTGAGCTGTATTTCCAGCGCATCGTTGCTCGAGCTCCGTTTCCAGCGCATATCTTTGCTT
-GTCTGGCATATGAGCTGCGGTGCAGGGTTTCAAAGCCATAGTTTTCATGGCTTTCCTAAT
-CTGGCCCCGCTGAAAGCACCCTGGTCCATCAGGCAGGATGCATAGGTGAGCCCTGTGGTG
-AAGGCCAGGTCTGGTCCCTTTTCGTAGGCCCCGACGGGTGCAGTGGGCACTTCTTGCCCT
-CTTCTTCCTGGATGCCATCCTCTGGACACCCCACCCTCCAGCTGAACCCATCTCCAGCCT
-TCTCTCTTCCTCCATTATTTATTTATTGAGACAGGGTCTCGCTCTGTCACCCAGGCTGGA
-GTGCAGTGGCACAGTCTTGGCTCACTGCAACCTTCCGGGTTCAAGTGATTCTTCTGCCCT
-AGCCTCCCAAGTAGTTGGGATTACAGGTGCCTGCAACCACTCCCGGCTAATTTTTGTATT
-TTTAGTAGAGCCAGGGTTTCACCATGTTGCCCAGGCTGGTCTCAAACTCCTAACCTCAGG
-TGATCCGCCCGCCTCGGCCTCCCAAAAGTGCTGGGGTTACAGGCGTGAGCCACCGCGCCC
-GGCCAAGCCTTCTCGCTTCCTTCCAACACCCTTGCTCCTTCCCGCCCCCGACTACTGTCT
-CAGCGAAGCCGCCCCTGGGTCCCCTAGCCCAAGGTGCTCTCACCTCTAAATTTAGAGGGG
-CCTTTACTACGAGCTTTTCGGTCTTCTGTCAGTGATCTACAAATAAGTGAACTACAAATC
-AAGCCAATTTCGTTTCTCAGTGCGTTTCCTAATGTTTCCTCTGTTCTCCTGGGCTTAAGG
-AGAGGCCATCTCTCTCCTGTGTCTACGGTGAGCCGGGAAGAATCGGCTCCCTGCACTGGT
-CTGCCCGGCCTAGGCCCTCCTCGCCCATCACGCACGTGCTCGGGTCCTGGGAGGCCGCGT
-CAGTCCGGCCGGGAAGGAGCAGGACCCAGTCGCCATGGCTGTCCCGGCGTACGCAGGACC
-GCGGCCTGGGGCGCTCACCTCGCTCCAGGAGCCCAGAGACCTCGCCGGGCTCGGGCTGAG
-GTGTTGCCGGGCTCTCGGCGTCCCAGACCCGGCTCCGGTCTCCAGGCAACCGCGGACGCC
-GCCAGGCCCACCCTGTGCTCTTAAAGGGGCCGCGCGCCAGCGCCAAGCAGGTGTCCCGCC
-CTTGCTGGTCCTGAAGGCCGGGGGAAAGGCTGGACGCTGGAGGCAGCAGGCCAGGGTTTT
-CCCAGCTCTGCTAACTGCTTCATCATAAAATAGGAATAACGCAGGCATTAGTTTTCCATT
-GCTGCCGCAAACAAATTACCATAAATTTAGTGGTTCGAAGCAACACAAATTTATTACCCT
-ACAGTATGTAAATTAGTCCCACAGTGCTGGTTCCTTCCAGAGGCTGAGGGAGAGAATGCG
-TTTTCTTGCCTTTTCCAGCTTTTCCAGAAGCGGTCCCCAACCTTTTTGGCACCAGAGACC
-GGTTTCGCGGAACACAATTTTTCCATGGATTGGGGTCGGGGAGGGATGGTTTCAGGACGA
-TTCAAGTGCATTGCATTTATTGTGCACTTTATTTCTACTATTATTACATTGTAACATATA
-ATTAAATAATTCTACAACTCACCATCACAGAGACTCAGTGGGAGCCCTGAGCTTGTTTTC
-CTGCAACTAGACAGCCCCATCTGGGGGTGACGGGAGACAGTGACAGATCATCAGGCATCA
-GATTCTCATAAGGAGCGTGCAACCTACATCCCTCGTGTGTGCAGTTCACAATAGGGCTCG
-TGCTGCTATGAGAATCTAATGCCCACCGCTGATGTGACAGGAGGCGGAGCTCGGGTGGTA
-ACGCCAGCGACGGGGAGTGGCTATAAATACAGATGAAGCTTCGCTGGCTTGCCGGCCCCT
-AACCTGCTGTGCACCCCACTTCCTAATAGGCCATGGACCACTACTGGTCTGTGTCCGGAG
-TGTTGGAATCCCTGTTCTAGAGACTGCTTGCAATCCTTGACTAGTGGTACCTCCTTCCAT
-CTCCAAAACCAGCAAGACAGCCTCTCTCTGGCCAGCAGGGAAAGGTCTCCACCTTTGAAG
-GACTCACCCAATGGACTGGGCCCACCCAGACAATCCAGGATAATCTCTCTGTTGCAAGAT
-CCTTAACTCAGCCAGGCATGATGGCTCACACCTGTAATCCCAGCACTTTGGGAGGCCGAG
-GCGGTCGGATCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGTCAACATGGTGAAACCCT
-GTCTCTACTAAAAATACAAAAATTAGCCAGTATGGTTCTGGACACCTGTAATCCCAGCTA
-CTCGGGAGGCTGAGGTGGGAGAATCACTTGAACCTGGGAGGCAGAGGCTGCAGTGAGCTG
-AGATCATGCTATTGAACTCCAGCCTGGGCAACAAGAGCGAAACTTCATCTCAAAGAAAAA
-AAAAAAAAAGATCCTTCACTCAATCACACCTGCCGAGTCCCTTCTGCCACGTGAGGCAGC
-GTGGTCACAGGTTCTGGGGATTAGGACACAGCTGTCTTGGGGGCTGTTATCCTGCCACAG
-CTCCCAATCTGGAGAGTTCATAAGTGGGATCCTGCAGACCACGCCAGCACAGTGCCAGAC
-ACGATGGCACAGTGACTACTGTACTGCCTCCTCCATCTGAGGGATTCTAAAGCAGGAAGG
-GGAGCCGCCCACAGTCTGGAGAAGGGGTGGGGGCAGCAGGGGGAGCCACATCTGTCATCT
-CTGGGCCCCCAAGAGGGCATCTTTACTTCCATTTTCAGCCAAGTTCAAACAGGACAAGGT
-TCCATGAAAACTATTTGAAAAGACAGACAGGGATTCTTATATTCCCAGAACCATTCAAGG
-CCAGTAACTGGAATGTTCTACAGTTCACATCCTGAGGAAACCAAATCACAGCATCAAATT
-ATGGGAAATCAAACTCTTTTTGTTCCCCTGCGAGGACAGCATTTTGCGACCTTGGCCGCA
-CAGAGGAATGTTTCAAATAGTGACCCCTGTCCCATCCAGTCATTTTCTTCCAGCCGGGCA
-GAGAATCCCCCGTGTTTAAAAATTTAATGTGAATCAGGGCTGAGAATCACTAACTGAAAA
-GGACCCTACTTTTAAATTTATGAAATTAAACAAAGATGAATTTAATTATCATTAAGGGTT
-GAAAGTTATAGACTAAACTATGTCCAGCCAGAGCAGAGGCCTGAGTAACTTCCAAAGTGG
-TTTGGTTTTTTTTTTTTTGTTTTGTTTTGTTTTGTTTTTTGAGACACAGTCTTGTTCTAT
-CTCACCCAGGCTGGAGCGCAGTGGCGCAATCTCGGTTCACTGCAACCTCCGTCTCCCGGG
-TTCAAGCGATTCTCCTGCCTCAGCCTCCTGGGTAGCGGGGATTACAGGCATGCGCCAGCA
-CACCTGGCTAATTTTGTATTTTTAGTAGAGGCAGGGTTTCTCCATGTTGGTCAGGCTGGT
-CTCGAACTTCTGATCTCAGGTGATCCGCCGGCCTCGGCCTCCCAAAGTGCTGCGATCACA
-GGCATGAGCCACCATGCCCAGCCCAAGTGTTCTTATTTTTATAAAATGTGTTCTTGCCTG
-GACACACACACACGAGCGCATGCAAACATAGAGAAAAAAAATTTGCAAGCAATGCTCCAT
-CTGGTTTGAAAAGGTTCTCAAGATCACTTTTAAATGGGTGTGATGTGTATTTTTTTTAAG
-TAGCAGGTTCATTTTAAAACAAAAAAGGTTAGTGAAGACTCTGTCTTTCAAAACATAAAA
-ATCTGCGATAAAACCAATTATTCCATACAGTGACTACGGTCAGTTCTGAGAAATGACACC
-CAGGTTGGCGATGTGTCTCATGGTTGGCCTTCCATGGGGACAGTTCCAGGGGTGGTCCAT
-CTCCCCCATGTGGGTGATCAGTTTCTTCATCTCGCTTGTGTTAAGAGCAGTCCCAATCAT
-CACCTGAGTGTGAGACACAATGGTTCAACGTTTTAGTAGTTTTTTGACGTCAGAATGGCA
-GCTCTTCAGAAGCATTCTTCTCTAAAATAAGGCTGGACAAGATTACAGCTCAAAAACTAC
-CTTCCCTGAAAAACCTTCCCCCAGAGAAGCCTAGGTTCTAGATCTCAGCCCTCCACCCTT
-CTGTGAAATCAGGCTCCTTGTGGCTCCTTCAAGGTGGCACCGCCTCCACTCCAGACGCCG
-ACCACACCTGTCTCAGCAGCCACCCTGCCCTCTCACCCTGGCAGGTGCAGCAGCCTCCCA
-GCAGGCCTCCCTGCCCCACTGCGACCCCTCCGAGCCGCTCTCCACTCAGCAGCCAGTGAT
-TACTTTTAAAGGGCTGTCAGGTTATTCATTCCACTTCACAGCTCTCCCCCTCACCTGAAT
-AAAAGCCCCCGTCTGTCCCCTGACTTGGCCCTCGCTGGGCTGTGCCTGCACCCCCACCTC
-CAAGCACGAATGCCTCCCTTCCTCACCCCAGCTGCACTGCTACTCCCTTCCTCTTGCACA
-GGCCCATCACGCAAACACCTGCCTTGGGACTGTGGCACTCCCGGGACCCTCTCCCCCAAT
-GGGTGCAGGCGTCACTCCCCCTCTGTCGAGCTCCGACCTGCTGCCCATAGCACTCCAGCC
-CTGGCCCTGCTGCCTCCCTGCCATGGGTCCTCTGACAGGAAGGAGAGGACACAAGCCTGA
-AGCCCAATGTCACCTTCTTTCTTCCTGCAGCACCCTGAGGGCTCGCCATGTGCCAAGCAC
-AGTCAGAAGGCTGGGGTGACAGCAGGTTGGAGAAGGACAGACAATCAACAAGTCAACAGA
-GAACCAAGACAGGTGGCACCAGGCGAGGCGGCCTGCTCAGGTGTGGGGATGGGGTGAAGG
-GTGACGGTGGCAAACCCAGGTAGAGAGGAGAGTAGGGAGAAAGGGTGTAAGGCAGGGAGG
-AGACTGAGGCGAGCGTGGAACTGGAAGGCAGCTACATGGCTGGAAGCTACATGGTGGGGA
-GATGGGGCTGGAAGGGTGGGCAGGGCTCAAAGCAGGAGCCTCCTGGGCAGGCAGTGACAA
-CACCGGAGATGGACGGGTAGGCCAGGGCGAGAGGGAAGGAGCAGCCTGTGGTTCCCCGGG
-CCACTGAGTCACACTAAACTCAGGACATCAAAACTGCCCGGCTATGAGCTCAGCTCCACG
-CTCTCACTCACAGACTCCAAGACTGGAAGATCCATATTATGTCTTTTATTTTGGTGAGGT
-CAGGGGTGGTGGAGAGACTCTGTCTCCCAGGCTGGAATGCAATGGTGCGATCTCAGCTCA
-CTGCAACTCCGCCTCCCAGATTCAAGCAATTCTCCCGCTTCAGCCTCCCGAGTAGCTGGG
-ATTACAGGCGCCCACCACCATGCCCAGCTAATTTTCGTACTTTTAGTAGGGATGGGGTTT
-CACCATGTTGGCCAAGCTGGTCTCAAATTCCTGACCTCAGGTGATCAACCCACCTCCGCC
-TTCCAAAGTGCTGGGATTACAGGTGTGAGCCACCACGCCCAGCCCCTATTAGGTCTTTAT
-CCAAGAAACACTGTGGCTAGAAGTCAGACTCTGGGCCCTCTTCTAATTAAACTCTGCCCT
-TGAGTCATTTCATCTAATCTCATGGCTGTAAATTACACCTGAAGCTCACACAGCAGGCTC
-CATCCCACCCACTCCCCACGTGGCCCCCAGCTGCTGCTCTCCTCAGCGGCCGCAGCCACC
-GCACCCCTTCCAGTCTGTTCTCTCTCCAGCAGCTGCAATCACGGGACTCCTTCCCGTCTG
-TTCTCTCCAGTGGCTCGTGCCACACACAGCACAGACCCCCAGGGTCTAGGTATGACCGGC
-AACACTCTACGTGGCTGTCCTCTGGACGCCGCTCTGCTCACTCCCTTCCCCTCTCCAGGG
-ACACAATCAGCCTCTGGCTTCAGTCTTGCTACTTCCTTCGCTTGGAAAGTTCTTACCCAA
-GAGGGCTCCATTCTACCTTTTTTTTTTTTTTTTTTGAGACAAGGTCTTACTCTGTCACCC
-AGGCTGGAGTGCAGTTGCGTGATGTTGGCTCATTGTAACCTCGACCTCCCTGGCTCAAGT
-GATCCTCCCACCTCAGCCTCCTGAGTAGCTGTGACTACAGGCACATGCCACCACACCTGG
-CTAATCTTTTAATTTTTTGTACACATGGGGTCTGCCTGTGTTGCCCAGGCTGGTCTCTTA
-ACTCCTGGCCTCAAGCAATCCTCCTGCCTTGGCCTCCCAAAATGCTGGGATTACACGTGT
-GAGCCACCATGCCTGGCTTCCATCCCACCTTTTAGATGGCAGCTGAGATGCCACCTGCCC
-AGATGCCATTCCCTGACCACCATCTCACCTGGTCACCATGTTTTTCTCTTGTCATTTCCT
-GCCCCAAAACGCTGTTTTAGGCCAGGTGCGGTGGCTCACGCCTGTAATCCCAGCACTTTG
-GGAGACCAAGGCGGGCAGATCATGAGGTCAGGAGATCAACACCAGCCTGACCAACATGGT
-GAAACCCCATCTCTATTAAAAATATAAAAATTAGCCAGGTGTGGTGGGTGCCTGTAGTCC
-CAGCTACTTGGGAGGCTGAGGCAGGAGAATCGCTTGAACCTGGGAGGCGGAGGTTGCAGT
-GAGCTGAGATCACATCACTGCACTCCAGCCTAGTAACAGAGCGAGACTCCGTCTCAAAAA
-CAGACAAAGAAAAATGCTGTTTGAATCTCTTGACTGTGCTTACTGGCATCTAATGCGTGT
-CATTTATTTGTGGTGATGCCTATTTCTCCCCACTGTCTGCTCCACAGGGGCAGGGGCTGC
-AGCCGCCTTGTTACCTCTGTGTCCCGAGCACCTGGAGCAGGGCGGGCCCCACATCAGGGG
-CTCAAGGAGCACCTGCTGAATAAATAAAGGAATGGCGTCCTGGCCCTTCCCAGTGGCCAG
-CTGATACACAGTCACTTTTCTTGGACATCAGGCTAATCCCCACTGCAGGCAGAACCACTG
-CTGCCACCTTCCCACACCAACCGAAGCAGCGGCAGTGACGCCACGTGCAATGACAACCAC
-GGCACCCCGTGAAGCACCTGCTGCCTCGATGACTCTGCAGAATCGTGTCCAATGTCGCCG
-AGTCCTGGCAGCAGCAAATCTTTATCTCCCAATGTTGTTATGACCCATAAGGTCCATAGA
-CGAACAAGGTACCTCAAACGCTAACTGCGTTGGAGTCAACCAAAGCTCGGAGATAGAATA
-CTGGCCGGGCCAGGCACAGTGGCTCATGCCTGTAATTCCAGCACTTTGGGAGGCTGAGAC
-AAGGGGCAAAAGGAGACCATGTTTCTACAAAAAATTTAAAAATTAGCTGGGCATGGTGGT
-GCATGCCTGTGGTCACAACTACTTGGGAGACAGAGAGAGGAGGATCGCTTCAGCCTGGTA
-CGTCAAGGCTGCAGTGAGCTGTGATTGTGCCACTGCACTCCAGCCTGGGGGACAGAGGGA
-GAATCTGTCTAAAAAAAAAAAAAAGAAGAATTCTGGGTTTTTTTTGTTTTTTTGAGACGG
-AGTCTCGCTCTGTCGCCCAGGTTGGAGTGCAGTGGTATGAACTTGGCTCACTGCAAGTTC
-CGCCTTCTGGGTTCACGCCATTCTCCTGCCTCAGCCTCCCGAGTAGCTGGGACTATAGGC
-GCCCGACACCACGCCCGGCTAATTTTTTTGTATTTTTAGTAGAGACGGGCTTTCACCATG
-TTAGCCAGGATGGTCTCGATCTCCTGAACTCGTGATCCGCCCGCCTCAGCTTCCCAAAGT
-GCTGGGATTAGAGGCTTGAGCCACCATGCCCGGCCAAGAATACTGCTTAACAGAGGTAAC
-AAAAGAGCAATAATTATGAGTTCAAGGTCACAGAGAACGCAGACGACACAGATGCTCAGC
-TACGACGCTGCACGTAGCTCTCTGTGTAAAATGACCCCTGGCAATCACAAAGGCGTTTAC
-AACCTTGACCAAATCAGGAGCTGGGCTGAGACCTTCCTCGACTGCAAGCTTGAGCAGCTG
-AGCTGACAGCCAGGCTTTCTTTACTTACCGACTTCCGGCAGGCTCTGGAGGCAAACATCT
-GCTTGACTCGGGAAGGCCGGCACATGACCCCAGGGCTGTCGCTCAGCATGAAGATCAGTT
-CATCGACGTCCTGGGGTCCGAAGGTCCAGTTTTTACTAGTTGGCAAGGAAATCAGTTTAG
-CCCTTTCAGTGACTGGAGCTAAAAGAATACAATTTTGAGAAAAATCCATGACTTGACAAA
-CACGTTTCACTTGAAAGCTACTTAGGATGAACATCTGAGGCCGGGCGTGGTGGCTCACGC
-CTGTAATCCCTGCACTTTGGGAGGCTGAGGCCAGCGGATCATGAGGTCAGGAGATACAGA
-CCATCCTGGCTAACATGGTGAAACCCCGTCTCTACTAAAAAATAGAAAAAATTAGCTGGG
-TGTGGTGGCAGGCACCTGTAGTCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATGGTGTG
-AACCTGGGAGGCGGAGCTTGCAGTGAGCCGAGATCGGCACCACTGCGCTCCAGCCTGGGC
-GACAGAGCAAGACTCCATCTCAGAAAAAAAAAAAGTGAACACCTGAAAGAGAGGAAACTC
-ACAAAATGCTTTTTGGAGGAACTTTTTAATCTTTTATAAAATTAAAAAAAACTGGTCTAT
-ATGACCTGAAAGATTATTCCCAGCTCTAAAAAGACAAGAATCTATAGTTCTGATTTTTTT
-TTTTTTTTGAGACAGAGTTTCACTCTTGTTGCCCAGGCTGGAGTGCAGTGACGTGATCTC
-GGCTCACTGCAACCTCCACCTCCCGGGTTCAAGCGATTCTCCCACCTCAGCCTCCTGAGT
-AGCTGGGATTACAGGCACCCGCCACCACGCCCGGCTACTTTTTGTATTTTCAGTAGAGAT
-GGGGTTTCACCATGTTAGCCAGGCTGGTCTCAAACTCCTGACCTCAGGCGATCTGCCCGC
-CTTGGCCTCCCAGAGTGCTGGGATTACAGACGTGAGCCACCACACCCAGCCGCTATAGTT
-CTAATTAATAACTTACCATTTTCATCGATAACAAAATCAAAGCCATTCTTTCTAAATATT
-TCCAGATTTTCTATCAGAACAGCTTCATTAACAGCAGTTAAGTTGAGAGTCTGAGGTCTG
-AAAAACACAAAAATGATTCAAACCATATCCTGAAGTCAAACATTTAGCTTTACAGCAGAA
-ATGAAATGAAAACAACAATACTGTATTTTGAATTCATGTCAAAATAACAACACAAATAAC
-AACACTACTCAGCTAAGTGTCACAAAACTTCCTGAGAAGTTCCTTTTAATTTTCTCTTTC
-TTAAAGTTCTTTTTAGAAGTTAAAGTAGCTACAGGCCAGGTGCGGTGGCTCACGCCTGTA
-ATCTCAGCACTTTAGGAGCCCGAGGCAGGCAGATCTCTTGAGGCCAGGAGTTTGAGACCG
-GCCTGGTCAACACAGCGAAACACTCTCTCTACTAAAAATATAAAAATTAGGCCAGGCATG
-GTGGCGCACGCCTGTAGTCCCAGCTACTTGGGAGGCTTAGGCATGAGATTCGTTTGAACC
-CAGGAGGGAGGCAGAGGTTGTAGTGAGAGCCAAGATCACGCCACTGTACTCCAGCCTGGG
-CGACACAACAAGACTCTGTCTCAAAAAAAAAAAAAAAAAAAAAACACCCATAAAAACAAA
-AATTAGCTGGAAGTGGTGGCTCATGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCACT
-AGAATTGCTTGAACCCAGGAGGTGGAGGTTGCAGTGAGCCAAGATCACACCACTGCACTC
-CAGCCTGGGCAACAGGGCAAGACTCTGTCTCAAAAAAAAAAAAAAAGTTCAAGTAGCTAC
-AAAAGTAGTTTGCTTTTTCCTCAGCCTGCCACGCCAATGACTCCCACTTTTTCTGAATCC
-TTTCCTTAAGGATAACAGTATCACAAAAATGCTATTTTTCCTCCTTCTAATACAGAATTT
-GAAACACTGGGTTAGGTCATTGCCAGCATTTGTAAACAGAATGAACAGACAGCTTTTATT
-TTGCTATCCTGTTCCTTCCTCTGCCTGTATTATATCTCCATCCCTCTCTCCTCCTGGATT
-TACTGTTTGTTTTTTTTTAACCTTTCGTTATTTTTTTCAAAGATAGAGACAGGGTCTCAC
-TATGTTGCCCAGGCTGCTCTCAAACTCCTGGGCTCAAGCGATCCTTCCACTTCAGCCTCC
-CAAAGTGCTGGGATTACGAGTGTGAGCCACTGCATCTGGTCCTGAGTGCTGGATAAGACA
-AACACTGCTCAAGGCAGGAGACAGCTGGTGAGCAAACACAGGCTTGGTCCTGGAGCCAAC
-AGATTACCGGGGAAGAAAGACGTTGAGCAAATACTCAGGCAAGTCGATTATGATGAGAAA
-CGACAGGAAGGTCAGGAAGAAAAAGCAGCCAGTGTCATAGAGAGACTTCACCCTGGGGTC
-AGGAAGTGACCTTTGAGCTGAGTCCGGGGATAAGAGAGTTAATCAGGTAACGGGGGAGAA
-GTGGGTGCAGGGTGCAGGACAAGTATTCTAGACAGGGACAACAATCTGTGCCAAGCCCCA
-GGATGGACCGCTGATGTTTGCAGAGCCACACATAAAGATATCCTTCATTCTGCTTAGTGG
-CCACATAGGGATTCATCAGGCCTGCCAAGGGAAAAAGAAAGACAGCCAGAGAGGCTTGAG
-TACAGGGAACAAGGGGAAGACGAACGGGAAAAGCTACAGAGGTCAACAGGGCCACCCTAC
-ACAGGGGCTGGCAGGGCAGGGTGGAACTGGGTCTTTATCCTTTAATCTTGAAGTGTGGTC
-CATCTGGGACCCTAAGTGGTCTGTGATTACCTGGGCCAACTTGAAATGTCACAGATGAGA
-GGTTATCTTTGCCGAATGGCTAAAAAATACAAGACCTCAGCCGGGCATGGTGGCTCACAC
-CTGTAATCCCAGCACTTTGGGAGGCTGAGGTTGGTGGATCACCTGAGGTCAGGAGTTCAA
-GACCAGCCTGACAAACATGGCAAAACTCCCTATCTATTAAAAATCCAAAAATTAGCCAGG
-TGTGGTGGCGGGTGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCACTTG
-AACCCGAGAGGCAGAGGTTGCAGTAAGCCGAGATCACATCACTGCACTCCAGTATGGGCG
-AAAGAGTGAAACTCTGTCTCAAAAACACAAAAACAAAAAACCTCTATTAAGAGGAACAGG
-GAAGGGATATAAAGTAGCTTACTAAATGTCTATTATTACCATTGCCTCCTACTGAGAATA
-AAAACAATTCACGCATTCCACAGGAGAGTACTCAGCAAACTACACAGGAGAGTACTCAGC
-AAACTACACAGGAGAGTACTCAGTAAACTACACAGGAGAGTACTCAGCAAACTACACAGG
-TTCAGTGGTACATTTCTCCATGTGGGATCTACTTGTTGGGATCTGAGTTTACTTCACTAC
-GTGGTTTAATTTCCCACACGAAAATCCATGACCTCTTCTTCTAACTTTGCTGAAGACAAG
-ACTTTGGTTTTACATGATACTATCACACCTGACCTTTGTGAAGTAGTCAGGGTAAAACAT
-TCCAGTTTGGCCGAGGAGAGAGAAATACCAAATTCTGCAGTGACTATCTTAAAATAATTT
-TTAAATTTTATTTTATTTTATTTATTAATTTATTTGTGAGACAGAGTCTCACTGTCTCAC
-TCTGTCACCCAGGCTGGAGAGCTGTGCAGTGGCACGATCATGGCAGCCTCAATCTCCTGG
-GCTCAAACGATCCTCCCACCTCAGCCTCCCGAATAGCTGGGACCACAGGCACACACCATC
-AAGTCTGACTAATTTTTTACATTTGTTGTAGAGACAAGGTTTCACCATGATGCCCAGGCT
-GGTCTCAAACTCCTAAGCTCGAGGGATCTGCCTGCCTCAGCCTCCCAAAGCTCTGGGATT
-ACAGGCGTGTGCCCCTGCATCCAACCTGCAGTGACTATCTGACTTCTGATTACTCTACTG
-TCAATCAACACTGGCGCACAGGCTGTCTGTCTTTCTGAACACACACATTCCATACACTAT
-GCATACTAATACTCCATACTATCAATTGCCCTCATCAGAAGGATCTTCTGGCTAACCAGT
-GATCAACATTTTTAATAGCGAAAAATACCTGATACTTAGAGAACATGTTAACCACGTGAA
-CTGGGGCAGGTTACTCAACCTCTCTGCATGTGCCTCAGTTTTATCGCTTGTGGAATGGTG
-ATGGTAACAGTAACAACCCCATAGGTTTTTGAGGATTAAAGGAACTAATACACATACATT
-ATTTCAACAGTGCCTGGCAGATTCTAGGCACTGAATAAATGGTAACTATCACTATTATGT
-AAAAAGTATAAAAATCTGCTATATGAATACTTATGGAAAAATACATATATACATATAGAC
-ACACATATAAACTATTAGGTCTCTTTTTTTTTTTGAGATAGAATCTCGCTCTGTCACCCA
-GGCTGGAGTGCAGTGGTGCGATCTCGGCTCACTGCAACCTCTGTCTCCCAGGTTCAAGCG
-ATTCTCCTACCTCAGTCTCCTGAGTAGCTGGAATTACAGGCGTGCACTGCCATGCCCAGC
-TAATTTTTTGTATTTTTATTTTTTATCATTATTATTATTTTTTGAGACGGAGTTTCACTC
-TTGTTGCCCAGGCTGGAGTGCGATGGCACGAACTCGGCTCGCTGCAAACTCCGCCTCCCG
-GGTTCAAGCGATTCTCCTGCCTCAGCCTCCCAAGTAGCTGGGACTACAGGCGCCCGCCAC
-CACGCCTGGCTAATTTTGTATTTTTAGTAGAGACAGGTCTCACCATGTTGGTCAGGCTGG
-TCTCGAACTCCCGACCTGAAGTGATCTGCCCACCTCGGCCTCCCAAAGTGCCGGGATTAT
-AGGCGTGAGCCACCGTGCCTGGCCTTTTTGTATTTTTAGTAGAGGCGGGGTTTCACCACG
-TTGGCCAGGCTGGTCTCCAACTCCTGACCTCAGGTGATCTGCCTGCCTCGGCCTCCCAAA
-GTGCTGGGATTACAGGTGTGAGGCACCGCGCCTGGCCAACTAGATATTTTTTATTTTTTA
-CACCCCTCCTTCCTAGATCTCTTCTTTTTTAAAGTAGATACAAGGTCTTGCTGTGTTGTC
-CGGGCTGGTCTCAAACTCCTGGCCTCTTGTGATCCTCCTGCCTTGGCCTCTATTAGATCT
-TCAATTTGAGGGGGAGTCTGGGAATGAACACTAAACACACTCACGCTATGAGCCTCTGCC
-CCTGGAGCACGGTGTGCTGCTGCAGCATCTCGAAGTTATACTTCTCGTCCGTGGCATGCT
-GGTCCACTATGAAGATATCCTCATTCAGTTTGGTTATTATAAATCCCAGGTTAAACTGAC
-CAATGATTTCCATTTCTGCAAACATCGTTTTACTGCAGGTAGAAAATGTTAATTATCAGA
-CATTTTACAAGATTATTTTTCTGATTATGTTATAGAACACTGTAATAAAAAAAAAGTCAA
-ACAATACAAAAACAAAATAAAGTCCCTAGCCATCCCGCTTTCTTTTTTTTTGAAACAGAG
-TCTCGTTCTGTCACCCAGGCTACAGTGCAATGGCACAATCTTGGCTCACTGCAACCTCCA
-CCTCCCGGGTTCGAGTGATTCTTCTGCCTCAGCCTCCTGAGTAGCTGGGATTACAGGTGC
-GCCACCATGCCCAGCTAATTTTTGTATTTTTAGTAGAGACAGAGTTCCACCATGTTGGTC
-AGGCTGGTCTCGAACTCCTGACCTCATGATCTGCCCGCCTTGGCCTCCCAAAGTGCTGGG
-ATTACAGGCGTGAGCCACTGCGTTCGGCTTAACCATCCCACTTTCTAAAGATAACATTAA
-TTATTCATTCATCCAACTCTCCGGAGAAGACATCAGTTGCTACTATTAACGATTTAAATG
-GAATATATCCTTCTAGACCCTTGTCTCCATATATAATTTTTTTTAATTTTAAAAAACAAA
-AATGGAATCTTAATTCTCCATTCTGTCATCACTTAATGCATCTGAAACAAGTTTTCAGAC
-CTGTACACATAGATCTACTTCATTATTTTTTCTTTTTTTTTTTCTTTTAAGACGGAGTCT
-CACTCTCTGTTGCCCAGGCTGGACTGCAGTGGCGTGACCGTGGCTCACTGCAACCTGCGC
-CTCCCAGGTTCGAGCGATTCTCCTGCCTCAGCCTCCCGAGTAGCTGGGACTACAGGCATG
-CACCGCCAAGCCCGGCTAATTTTTTTATTTTTAGTAGAGACAAGGTTTCACCATGTTGGC
-TAGGCTGGTCTTGAACTCCCGACCTCAAGTGATCCACCTGCCTCGGCCTCCCAAAGTGCT
-GGGATTACAGGCGTGAGCCACCGCACCTGGCCTACTTCATTCTTTTTAATGGCCACATAG
-GAATTCATTGCATGGATGTACCATAATTTGTCTGACAAATCCCCTACTAAAGGACATTTC
-AGTTGTTTCCAATTTCAATAGCGCACTCAAAGCTGCAACAAATACTTCTGTGCATAAACC
-TACTCATCTGTGGGTGCATTTCCGTGAGACAGACGCTAGAGGGAGAACTACATATGTACT
-TCTTGACGGGAAATCTGTGAAAAGTCACACTCCCACCAATGGTGTGTAAGAGCACCTTTC
-TGCCAATGCTGGATATCAATCCTTCTCATCTTTGCCAGGCCCACCACTGGGTCCTTTGCG
-GGTGGCTTCAACATCTAATGTCATTAAATACTAACTTAGTCAATCTGGACAAAAGACAGA
-CACCACCGCTAACCTTCACACGAGAAATTGACACTGTCATTCTCAGTCCCACACAATTAA
-ATCCGGTGAAAATGGATTTTCCGCAGTATCAGCGCGGTGATGACAAGAAATGGCTCTGTT
-AAAGCAGCCATGGACGTTTTCTGGTTCTCACCTGGTGGCCTGAGCTGAGGATGAAAGCAG
-CTGTAATGTAATCCCAGCACTTTGGGAAGACAAGGTGGGCAGATCATTTGAGGTTGGGAG
-TTCAAGACCAGCCTGGCCAACATGGTGAAACCCCATCTCTACTAAAAATAAAAAAATTAG
-CCAGGCATGGTGGTGGACACCTGTACTCCCAGCTACTTGGGAAACGAAGGCAGAAGAATC
-GTTTGAACCCGGGAGGCAGAGCTTGCAGTGAGCTGAGATCGTGCCAGTGCACTCCAGCCT
-GGGCGAAAGAGTGAGACTCTTGTCTCAAAAAAAAAACAAAGGAGCTGATATTGTTGTTTC
-TTTCTATAAGTGCTCCAGGAAGACCCGGTCCCATGCCACCATGCTCGTCACCATCACAAT
-CAACCACAGGGGACAGTTTGGTGAACTGTGAGACCTCCACATGGCATGGATTACTGAGCC
-CACATTTCCTATGGTGAGGGGCTCCACACAGAGCTCAAATCCAAGTCATAACCAAACCAG
-TCCCCAAATCCTATCTTTGAGGGTCTGTTTCCTGGTACCAATTCCAGATCAGGCAGAGTG
-CAATCAATCAAGAGACAAAAACCACACCAGTGATTTTAACAGGGACTTTTTTTTTTAAGA
-CAGGGTCTTGCTCTGTCACCCAGGCTGGAGTGCAATGGCATGATCATAGCTCACTGCAGC
-CTCAAACTCCTGGGCTCAAGTGAGCCTCCTGCCTCAGCCCCCTGAGTACCTGGGACTACA
-GGCGTACAGCAATGTACTTAGCTAATTTTTTTTTTTTTTTTTTTTTTTTAGAGATGGGGC
-CTCATTATATTGCCCAGGCTGGTCTCAAACTCCTAGCCTCAAGTGATTCTCCTGCCTCAG
-CCTCCCAAAGTGCTGGAATTACAAGGTGTGCACCACCATGTTAGGCCTGAGGAGGAAAAA
-TGTATAATAAGGCATTACACAAACTAGTAAAAGGTGGTTAACTACTATGCTAAGAAATAC
-AGGAATGGAAAATGCTACTATCCTAGGGAAGAGGGAGAGTCCTCAGAAAAGGAACTCTTT
-TTTTCTTTTTTCTTTTTCTTTTTTTTTTTTTTGAGATGGAGTTCGCTCTTGTTGCCCAGG
-CTGGAGTGCAATGGTGCAATCTCGGCTCACCACAACCTCCACCTCCCGGGTTCAAGCAAT
-TCTCCTGCCTCAGCCTCCCAAGTAGCTGGGATTACAGGCATGCACCACCATATCCCACTA
-ATTTTGCATTTTTAGTAGAGAAAAGGTTTCTCCATGTTGGTCAGCCTGGTCTCGAACTCC
-CAACCTCAGGTGATCCACCCACCTCAGCCTCCCAAAGTGCTGGGATTACAGGCATGAGCC
-ACCATGCCCAGCAGAAAAGGAACTCTTGTAAGAGGCTCCTACCCACTCAGGCTGAGTTTC
-AGACCTCCTTGGAGCAGGAGTGGCCGCAGCCTGCTGGATGGAGAGAAGCTGCCAGAGTGA
-GTGATGACACAGGAACTCCTGCCGCACAGGAGGGAAGGAAAAGAACATCCCAGAAGCATC
-CCAGATGCCAGCACAAATACCACCTCCCCTGGCGCCGATCCCAGGCTCTCCCAGGAATTG
-TCTGAATATGCCCTGGTTCCCAGTACATAGATAATCTGCTCAAAAGCTGGTGCTGGCCTA
-AAAGACCCAAGTCTTCCATGTGTTTGGAGTCTGTGTCCTGCCACAGAGAACAGGATCTGG
-CCAGGCGCAGATGCCGGAATTACAACTGCGCACTACCGCGCCCAGCCAATTTTATTGTAG
-AGACGAGGTCTCCCTATGTTGTCCAGGCTGGTCTTGAACTCCTGGGCTCAAGTGATCCTC
-CCTCCTTGGCTTGGCCTCCCAAAGTACTGGGATTACAGGTGTGAGCCACCACACCTAGCC
-TCAAAATACTCTTAAGAAAAAACTTTACCTGGCCGGGTGTGGTGGCTCACACCTGTAATC
-CCAGCACTTTGGGAGGCCAAGGTGGCTGGATCACCTGAAGTCAGGAGTTCGAGACCAGCC
-CAGCCAACATGGTGAAACCCTGTTTCCACCAAAAATATAAAAATTAGCCAGGCATGGTGG
-CGTGCACCTGTAATCCCAGCTACTCAGGAGGCTGAGGCAGGAGAAACGCTTGAACCCGGG
-AGGTGGAGGCTGCAGTGAGCCAAGATCATGCCACTGCATTCCAGCCTGCGCAACAGAGCA
-AGACTCTGTCTCAAAAAAATAAAAAATAAAAATAAAAATTTTAGATAAAAAGAGAAAAAG
-TAAAAAATTAAAACTTTACCTTATCTCTTTTCTTAGTTCATCTTCGGCTGCTTGATTTTC
-TCCAGGACAAATCTTTGCCCTAAACTTCCTGTAATTCTGTTCCCCTTCACTTTGCTGTGC
-TTCATGATGTAACTGCTTTATTCGTTTAGCTAAAGAACTCATAGAAAAGTCCAGGGGCAC
-AACTTTCTTATTAATTTTCACAGCTACATCAACCTGAGAGGCTGACATGTCCTGAGTATT
-TACTAACTTTTGACAAATGTCAGAACTGGAAAGAATTTCTTCTTTTTTAAAACGCTTTGT
-GTTTGGGGTTGCGAGATTAGTTGGCTGAGGCAAAACTCGAAATTTACATCCGGTATCTTC
-CTGGTTTGAATGGCAGTCCACATCTGAAAAAGAGTCGTCAGTTTTAGGCGCTTTCTCCTG
-AGAGTCCACATGTTCCTGCGAGCCCCTGTCCCCTGGGGAGCTGGCCGCATACTCGCTGCT
-GCAGTGACTGCCCGTGTCTGGGATGCTGAACCCCTCAGAATCCACGGAAGTGCTGCCGTG
-CCCCGAGTCCTTCTCCACCTCCGCTCTGTCCGTAGGGTCACTGGGTCCGTGACTGGAACT
-CACTGCCTCTTTCTGAGGTCTCAGGACGCCTTTGTCAGAGATGGCACCTGAAGTGCTAGA
-AGACAGCATACCCCTTTTCTGTCCTAGAGGGCTCCTTCTTGGTTCTGGAGTCTTTGGGCT
-GTGAGGCTTGTTCTCTGTTGTGTGACGAAGAGAAAAGGCCTCTCGCAGTCTGGAAATGGA
-CACGTCTTTTTTTTCTTCTCCAGTCCTTAATGAAGGGGATTGATCCTGCTTTTCTACCAT
-GGGCTTTTCCAAATCCGCTGCATGCATTTTTATTAAGTTACCTAAGCAAACGTGGACGGA
-GAAGAGGGTCAGGGACTATCCTGAAATGGTGAGAGGACGTGCTTATGTGAACAGATACTT
-CACAAAAGAGGAGATCCACATGCTAATTACACAGATGAACACAGTTCAATGTTCAAAATA
-AAACTATAATATGGGCCAGGTGTGGTGGCTTACGCCTGTTATCCCAGCACTTTAGGAGGC
-CAAGGCAGGGGGATCACATGAGGCTAGGAGTTCAGGACTGGTCTGGACAACATGGTAAAA
-CCCTGTTTCTACTAAAAATACAAAAATTAGCCGGGTGTGGTGGCATATCTGTCATCCCAG
-CTACTTGGGAGGCTGAGGCACGAGAATCCCTTTAGCCCGGGAGGCAGAGGTTGCAGTGAG
-CCAAGATGCCACCACTGCTCTCCAGCCTGGGTGACAGAGCAACACTCTGTCTCAAAAAAA
-AAAAAAAAAAAAAAAAAAACCACAACACAATGCAATATGGCCATATACTCACCAGAATGG
-TAAAATTAAAAAAACAACAAATGCTCACAAAGATCAGGATCAAGAGGAATGCCTGAATAC
-CTCTGGTAGGAATGAACCTGGTACAGCTGCTTTGAAAAGTTCTCTGGGAATACCTCCTAA
-ATCTGAATGTATGCACACCTGCAACCCAGCATAGCTACTCCTATCAGAAGTGCCTATTGG
-CCGGCACAGTGGCTCACGCCTGTAATCCTAGCCCTTTGAGGTCAGGAGTTCAAGACCAGC
-CTGACCAACATGGTGAAACCTCATCTCTACTAAAAATACAAAAAAAAAATTAGCAGGGCA
-TAGTGGAATGCACTTATAATCCCAGCTACTAGGGAGAATGAGAATGAGGCAGGAGAATCA
-CTTGAACCTGGAAGGCAGGGTTGCAGCGAGCCAAGATCACTCCACTGCACTCCAGCCTGG
-GCGACAGAGTGAGACTCCCTCTCAAAAAAAAGAAAGAAGTGCCTATCTATGCTCGTCAAA
-AAGACGTGGATGAGGATGTTCATGACAGCATTCTTCATTATAGCCCCAAACTGGAAACAA
-TTCAAATATTCACAAATGATGATATCTGACTATAATGGAACACTGTATAGCGAACGAATA
-AATGAATTTTGCCACATGACTTGGGTGAATCTCACAAACAAAATAATGAGAGAAAGAAAC
-AAATCACAGAAAAGGACAGACTGAATAACTTCAAATTAAAAACAGATTAAACTATACCGT
-TTTGGGTTTTTTTTGTTTGTTTGTCTGTTTTTTTGAGACGGAGTCTCGCTTTGTCACCCA
-GGCTGGAGTGCAGTGGCACAATCTTGGCTCACTGCAAGCCCCTCCTCCCGGGTTCACGCC
-ATTCTCCTGAGTCAGCCTCCTGAGTAGCTGGGACTACAGGCGCCCGCCACCACGCCCGGC
-TAATTTTTTGTATTTTTAGTAGAGACAGAGTTTCACCGTGTTAGATAGTCTCGATCTCCT
-GACCTCGTGAGCCGCCCGCCTTGGCCTCCCAAAGTACTGGGATTACAAGCATGAGCCGCT
-GCGCCTGGCCTAAATTCTACTGTTAGAAGTCAGGAAATCCCAGCATTTTCAGAGGCCAAG
-GCTAGAGGACTGCTTGAGCTCAAGAGTTTGAGACCAGCCTGGGCATCATGGAGAAACCCC
-ATCTCTAATGACAATACAAACATTAGCCAGGTGTGGTGGTGGGCGCCTGTAATCCCAGCT
-ACTCAGGAGGCTGAGGCAGGAGAATCTCTTGAACGTGGGAGGCTTCAAGGTTGCAGTGAG
-CTGAGATCGCATCATTGCACTCCAGCCTGGGTGACAAGAGCGAAACTCCATCTCAAAAAA
-ACAGACATGACAAGGGAGTTAAAAATGCAGTCACTGCAGACTTCTTCTAATCATATATCT
-TATATGACTTCATCCGTTTACAGTTTACAAAAAACTAGAGGTACTTGGAGGCAGCTACTT
-GGGAGGCTGAGGCAGGAAGATGGCCTGAGCCCAGGAGTGTGATGCTGCAGTGAGCTACAA
-TGGCACCACTGCAGTCCAGCCTGGGTGACAGAGCAAGTCCCTGTCTCAAAAAAGAATTAA
-AAATGATAAAATAATATAAGAGACTTTGTTTTCATGTCAAAAAAAAGTTTACTTGGAAAA
-AATAAGGAAACACATTAGCTAAAAGCTTTAGAAGCTGTTTGTACACTGTATTTTTCTTAC
-CTTCAACATCCAGCAGTGGCTGCTGACTGACATTTAGCTTGTTGACATCACTATCAAACA
-TTCCTATCAAAGAGGTCTTTAAAACTGCCAACAAAAGCTTTTCCTCTTGTAGCAAAATTT
-GCCTTTTATCTGGAGTAACATTGATATCAACGCATTCTAAGGCAAAAAAGAAAACATATT
-TATTATGTTTAAATTCACTTTTATTTTATTTATTAATTATTATTTTCAGACAGCGTCTCA
-CTCTGTCGCCTAGGCTGGAGTGCAGTGGCGCGATCTCAGCTCACTGCAACCTCCGCCTCC
-TGGGTTCAAGTGATTCTCCCTGCCTCAGCCTCCGAAGTAGCTAGGATTACAGGCAAGTGC
-CACCACACTGGCTAATTTTTGTATTTTTAGTAGAGATGGGGTTTCACCGTGTTGGCCAGG
-CTGGTCTCGAACTCACAACCTCAAGTGATCCACCCGCCTTGGCCTCCCAAAGTTCTGGGA
-TTACAGGCGTGAGCCACCGCGCCCAGCCAAATTCACTTTTAACAATAGAAATTTCCCCAT
-CTATTATTTCATTCACTTGTATTTATCACAAGTGCTATTAAAAACATTACAGTGTCCAGG
-TTAAGATTCATAAGTTATGAAATCAGCTTTTTCAAATAAATGAGCAAAAGACAATTTTTG
-AATAGACAAAATACGGAAGGGCTTAATTAGGTAAATTGTTAAAGGAAAAGCAAATAAACA
-CATAAAAATAATTTTAAATATGCAAACTAAAATAAGATATTTTAATCCCCTACTGAATTT
-AGCTTAACAATTATAATACCTAGTACATTATAGGTAGGTGTGTAAATTGGTACATCTAGA
-ACACAATACAGAAAAAGCCTTAAAATGATCATATTCACTGACCCAGTAATTCTACTCCCG
-GCAATTTATATTCAGAATAATTAAAGATGTAGGCTGAGTGCAGTGGCTCACACCCTGTAA
-TCCCAGCACTTTGGGAGGCTGAGACGAACAGATAAGTTAAGGTCAGGAGTTCAAGACCAG
-CCTGGCCAACATGGCGAAACCCCGTCTCTACTAAAAACACAAAAAATTAGTCAGGCATGG
-TGGCAGGTGCCTGTAATCCGTGCTACTCAGGAGGCTGAGGCGGGAGAATCGCTTGAACTC
-AGGAATCGGAGGTTACAGTGAGCTGATATTACACCACTGCACTCCAGCTTGGGAGACAGA
-GCAAGACTCTGTCTCAAAAAATATCTAATAATAAAGATGCAGATAATGATTTAATTATAA
-GGAAAGTATTTATAATTTCCAAAAACTAAAAACAATTTAATTTTGAAAAATTTAAAAATT
-AAAATACCAAACTATAACCATGCATTGGAATATAATTCACCTATTAAAACCACATTTCTG
-ATCAATTTCTAATAACATGGAAAAGAAAACATTCACATCTAAGGATAAAGAGCAGTATAC
-AAAATTATTTTCTCATCCCAAAGAATATGGGAGTAGGGGAGAGAGAGAGAAAGAGAGAGA
-GGACAGAAGATATTTTTTAAGGTATGTACATATGTGTTTCTAAGTATCTAGAAAAAATAC
-TCAATTACAATAAACCAAAATTTTAACAATCAGAAAAAAAAATCTATATGAAATGAATTA
-TTTATGAAATTAGGAAGAACATTTCATCTACTTTCTCCCTTGGTTGACATTAAAAAAAAT
-TACATTTTCCTAACAATATAATTAACATAGTCTCAAGTAGAAAGCGGGAACTCTGTTTAA
-AAAAAAAAAAAATTATAGGGCCAGGCACGGTGGCTCATGCCTGTAATCCCAGCACTTTGG
-GAGGCCAAGACGGGCAGATCACGAGGTCAGGAGATCGAGACCATCCTGGCTAACACGGTG
-AAACCCTGTCTCTACTAAAAATACAAAAAATTAGCCAGGTGTGGTGGCACGCACCTGTAG
-TCCCAGCTACTTGGGAGGCTGAGTCAGGAGAATCGCTTGAACCCGGGAGGCAGAGGTTGC
-AGTGAGCCGAGATCACGCCACCACACTCCAGCCTGGGTGACAGAGCAAGACCCCGTCTCA
-AAAAAAAACAAAAACAAAAAACTTACATGACCATAAATTGTTATCTCATTCCAGTCATAG
-CAGAGCTGTAGAATTTCATTTTATTCTTTGAGGCATTAGTCACTAGTTGTACTGAAATGC
-CAATGGAACTTACCTGAATCAACAGAAATGTTAAGAACAACAAATGGATACTGGTGTCGA
-TTATACATGTGGTAGACCTCATTCACGAGTCTGCAGACCTGCACAAAATACAAGGAGTAG
-AAAAGAATAAATGACAAATGTTCCCAGCCCCCCGCATTCTAACAACATTCTATTCTAACC
-AACCAGCATGTTCTTAGAAGGGGATACTTTTTTGTTTTTTTTTTTTTTGAGTCAAGGTCT
-CGCCTTGTCACAGCCTGGAGTGCAGTGGAGCAATCATGGCTCACTGCAGCCTCAACCTCC
-CAGGCTCAAGTGATCCTCCTGTGTCAGCCTGACATGTAACTTGGATTACAGGCAGGATTT
-TTTTTTCTTTTTTTTTTTCAACGGAGTCTCGCTCTTGTTACCCAGACTGGAGTGTAATGG
-CACGATCTTGGCTCACTGCAACCTCTGCCTCCGGGGCTCAAGTGATTATCCTGACTCAGC
-CTCCAGAGTAGCTGGGATTACAGGCACACGCCACCATGACCAGATAATTTTTGTGTTTTT
-A
+>chr7_5957000_6010000
+CTCGTTTCTAAAAAAAAAAAAATTATTTTTTTAGTTAGCCAGGCATGGTGGCAGTGGGCA
+CCTCTGTAGTCTCAGCTACAGGGGAGGCTGAGGTGGGAGGATCGCTTGAGCCAAGGAGGT
+AGAGAGCCCTGATTGCACAACTGCAGTCCAGCCTGGGCAACAGAGCAAGACTCTGTCTCT
+AAAAACAAACGAACACGCTGGGCGCTGTGGCTTACGCCTGTAATCCTAGCACTCTGGGAA
+GCCGAGGCAGGTGGATCACTTGAGGTCAGGAGTTCGAAACCAGTCTGGCCAACATGGTGA
+AACCCCGTCTCTACTGAAAATACAAAAAAAAAAAAAAATTAGCCGGGCCATGGTGGTGGG
+TGCCTGTAATCTCAGCTACTCCAGAGGCTGAGGCAGGAGAATTGCTTGAACCCAGGAGGT
+GGAGGCTGCAGTGAGCTGAGATCCTGCCACCGCACTCCAGCCTGGGCAACAGAGCAAGAC
+TCTGTCTCTAAAAACAAACAAACAGGCTGGGTGTGGTGGCTCACGCCTGTAATCGCAGCA
+CTTTAGGAGGCTGAGGCGCGCGGATCACTTGAGGTCCGGAGTTCGAAACCAACCTGGCCA
+ACATGGTGAAACCCCGTCTCTACTAAAAATACAAAAAAAACAATTAGCCCGGCCGTGGTG
+GTGGTGGGTACCTGTAATCTCAGCTACTCCAGAGGCTGAGGCAGGAGAATTGCTTGAACC
+CGGGAGGTGGAGGCTGCAGTGAGCCAAGATTGCGCCAGTGCACTCCAGCCTGGGAGACAG
+ACAGAGAGAGACTCTGTCTCAAAACAAAAACAAAAACAAAAACAAAACCCAAAAAGAAAT
+ATACATGTGTTGAGAATCGGCGGAGCATCCGCCTCTGGGTATAAGCTGCTACCCCGCCCG
+GGCGTACCTGGATGCCCCTCTCCCACCGCCCGGTGTACTCTTCGTTGGTGGTCAGCCACC
+TCATCCTCCCCTCCCCGTGGCGCATGTTGTCTTCCCACTGGCCTTCGTATATATTTCCAG
+ATTTATAACTAGGATGAAAGAAACCAAAGAAAAACAATCAGTTACCTCCTACACAACATT
+TACCTTTAAGACATTCTTTTAAACACTCCCCTTGAGCTCCTTTGAAGAAATCCACCCCTT
+GTACTTATACAATCTTCTCTGTATTTAAATTCAGGCCAGGCGTGGTGGCTCACGCCTGTA
+ATCCCAGCACTTTGGGAGGCCGAGGCTGGAGGATCACCTGAGGTTGGGAGTTTGAGACCA
+GCCTGACCAACATGGAGAAACTCCATCTCTACTAAAAATACAAAATTAGCCCAGCTACTT
+GGGAGGCAAAACTCCATCTCAAAAGAAAAAAAAAAATGCAAAAATTAGCCGGACATGGTG
+GCAGGCACCTGTAATCCCAGCTATTCAGGAGGCTGAGGCAGGAGAATCACTTGAACTCAG
+AAGGTGCAGGTTGCAATGAGCCGAGATCATGCCACTGCACTCTAGCCTGGGCAACAGAGC
+GAGACTGTCTAAAAAATAAATAAATAAAATTTTTAAAAAATCAATGGATAGGCTCATGGT
+CCTAAGGGAGCAGAATGAGTCACTTTATTAAATCTTCTGACTATTTAATAAGGGGACAAA
+GTGGGTAAGAGCCGGGTTTTTAAAATTTTTTAATAATTCCCTATTGTATCATGATTAGTG
+AATATTTGGCCAGTTTTTGAGATGAGATCTCACTGTGTCACCAAGGCTGGAGAGCAGTGG
+TGTGATCATGGCAGGAGAATTGCTTGAACCCAGAAGGCAGAGGTTGAAGTGAGCTGAGAT
+GGCACCACTGCACTCCAGCCTGGGTGACAGAACAAGACTCCGTCTCAAAGAAAAGAGAAA
+AAATCCACTCTGCTTAGAGAGAAAATGTTCCGTGCAACTTTTGCATCTTACTTTTAAATA
+TCCGAGGTGAACGCTATTGGGCCCACAAACCCTTCTTCATCTACACCCCAAGCGCGGCGG
+TGGTCATACCTACCATCTTATTCCCCAGCCCTTTTTGATGTTTTGTACCCAGTCTCCCTC
+GTACCAACACGTACCCTCTTGATTGTAATAAATGGAGCCCTGAAACAAATAATGTCATCT
+TTAAAACTATCAAGCCTCATGACACAAATGCTTTGTCAAATGTAAGGATATTAACTTGAA
+AAGTAGAACCTACACAGAGGTCAATGTCATACATAGGCAAGACATGTAAACTGCTATTTT
+TCTGTTTTGCTATCAAGAAAATGGTAAAACTGCTGCACAAAGGGAAATGAGATAATGTCA
+CAAATCAATTGCTCCTTAATAAAGTGCCATATTGGCCAGGCACGGTGGCTCACGTCTGTA
+ATCCCAGCACTTTGGGAGGCCGAGGTGGGCGGATCACAAGGTCATGAGTTCAAGACCAGC
+CTGGCCAACACGGTGAAACCCCGTCTCTACTAAAAACACAAAAATTAGCTAGGAGTGGTG
+GAGCGTGCCTGTAATCCCAGCTACTTGGGAGGCTGAGGCAGGATAATCGCTTGAACCTGG
+GAGGCAGAGGTTGCAGTGAGCCCAGATCGTGCCACTGCACTCCAGCCTGGGCAACAGAGC
+AAGACTCCATCTCAAAATAAAATAAAATAAAAAGTATCACATTAAGGCACAGAATGACTG
+TATTCATCATATTCGAGTATATTCATTCTATCCAGTAACTATTAGTCAATTAAGTACCTA
+GAGAAATCCTGTCTGTTGCCACCTGGAGTGAACAGTTGCGCCTTCCATGTAACGGAAGGT
+CACTCTCTCTTAGGCACCAGATCCACTGTTGTTTTACCCATTTGGACATGCTACTCATTT
+TACCGCCTCCGAGTATAAGTGAGCATAGAGTACCCTTTGTTTGATCTACATAGAAAAGCC
+TCAAAAGGCTTTTTCACAGGTTTATCTGTGTGTGTGAGAGAGAATTTTTCTATCTTCTTT
+CTCATGATCAGGCAAACTCATTCCTTCTTGCAGCCATGCAGATGCTGCTGTCTAGAAGTC
+ACCACCCCCAATCCCTCCAATATGTCTCAAGCAATCTGCTGTAAAACACACACACACACA
+CACACACACACACACACACAACAACAACAACAACACAACTCAATAAATAGCCTATTAAAG
+CATGCATACGGCCAGGCACAGTGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCTG
+AGGTGGGTGGATCACTTGGGATCAGGAGTTCAAGACCACCCTGGCCAACATGGCGAAACC
+CCATCTCTACTAAAAATACAAAAATTAGCTGGGCGTGGTGGTGCACACCTGTAGTCCCAG
+CAACCTGGGAGGCTGAGGCAGGAGATTTGCTTGAACCCGGGAGGCAGAGGTTGCAGTGAG
+CTGAGATGGCACCATTGCACTCCCGCCTGGGCGACAGAGCAAGACTCCATCTCAAAAAAA
+AAAAAAATTAATAAAATGGTTAATTTATGTGATGTGAATTTCGCCTCAATAAACAAAAAG
+TGAATATGCCCTGGACAGCGCCGCTAGCCCCTACCCCCTTCTCTCCCTCCATGTGGCCAC
+CCAGCCCCTCCCCTGCCCTCCACATGGCCACCCCACCCCCTTTCTGCCCCCCCGACCTCC
+CCGACCTTGCCCCCTCATGGCTGCCCCCCCCATGTCCGCCCACCCCCTTCACTCCTGCCC
+CACCTGCCCTCCACGTGGCCACCTCGCCCACCTTCCCGTGCCGCTTGCCATTGCACCAGT
+GGCCGATGTAGGACACAGGCTGGGTGCTGCACTTGAACATCCCGAATCCGTTCCTCATGC
+CGTTGACCACTTCGCCTTCATACATGCTGCCGTCCGGCCACGTGTACACGCCGTGGTTCA
+TCGGGACATTCTTCACAAAGTCGCCCTGAAGCAGAACGGCCATGGGGTGACAGAAGGAAG
+TGTTGGGGGGTGGGGGCGGGAATCCCTAGTCCTGCGGGCGGTTCCAGGAGCTGCTTGACC
+TCTGATTCTGTTCTTGCCTCTCCTGTGGACACACTGAACATCCCCCTCACACTCTCTCTC
+TTCCTTCCTTGTCTGCTCTCATCGCATCCTCTCTCATCTGACCCGACCAGTGGGCGGAAG
+CTCAGGCAGGAGGAAATATCTGGGAGGTTGCAGGTTGACTAAGTTCGAAGAAACAAGCAG
+GTGACGTTGGAAAGTGCTGGCTTCCAATCCTGACCTGGGGAACTTCAGATTCTTAGAACC
+CACCTTGGCAAGGTGCAGTGGCTCACACTTGTAATCACAGCACTTTGGGAGACTGAGGCG
+GGAGGACTGCTTGAGGCCGGGAATTTGAGGCCAGTCTGGGCAACCTAGGAAGACCCTGTC
+TCTAGAAAAAGATTTTATTTGTTTTTGTTTTTATTTTTGAGACAGAGTCTCACTCTGTCG
+CCCAGGCTGTAGTGCAATGGCGCCATCTCGGCTCACTGCAACCTCTGCCTCCCAGGTTCA
+AGCAGTTCTCCTGCCTCAGCCTCCCAAGTAGCTGGGATTACAGGCACCCATCATCACACC
+CTGCTAATTTTTTTTGTATTTTTAGGAGAGACGGGGTTTTGCCATGTTGGCCAGGCTGGT
+CTCGAACTCCTGACCTGAGGTGATCCACCTGCCTCGGCTTCCCAAAGTGCTGAGATTAAC
+AGGCATTTAACAGGCATGAGCCATCATGCCTAGTTTTTGTGGATTTTTTGTTGTTGTTTT
+TTTGTTTTTTTGAGACAGGGTCTCACCCTGTCACCTAGGTTGGAGTGCAGCGGCACAATC
+ATAGCTCACTGCAGCCTCGACCTCCCAGGCTCAAGAGATCCTCCCACCACAGCCCCCCAA
+GTAGCTGAGACTACAAGTGTGTGTGCCACCAAGCCTCACTACTTTTTAAATTTTTTGTGG
+AGATGGAGTTTCTCTATGTTGCCCAGGCTGGTCTGGTCTCAAACTCCCAGCCTCAAGTGA
+TCTTCCCACCTTGGCCTCCCAAGTAGCTGGGACTACAGGTGCTGGCCACCAAGGTGCAGT
+GGTGCACGCCTATAATCCCAGCACTTTGGGGGTGCTGACGTGAGAGGATCTGTTGAGCCC
+AGGAGGTTGAGGCTGCAGTGAACTATGACCACTGCATTCCAGCCTGGGCGACAGAGCAAG
+ATCCTGTCTCTAATGAAAAAAAAAATAACCCGCTCGAAGGAGGTGAATTCACTGTTCCCT
+CCAAGGCTTAGTGATGACTGGGGACATCCCTCTTTCTTTTTCCTTTTTTTTTCAAGATGG
+AGTTTTGCTCTTGTTCCCCAGGCTGGAGTGTAATGGTGTAGTCTCGGCTCACTGCAACCT
+CCGCCTCCCAGGTTTAAGCAATTCTCCTGCCTCAGCTTTCCGAGTAGCTGGGATCACAGG
+TGTGCACCACCATGCCCCGCAAATTTTTGTAGTTTTAGTAGAGACAGGATTTCACCATAT
+TGGCCAGGCTGGTCTTGAACTCCTGACCTCAGATGATCTGCCCACCTTGGCCTCCCAAAG
+TATTGGGATTACAGGCGTGAGCCACCATGCCCGGTCAGGAAATCCCTCTTTCTGCCACGG
+TCATCAAAATAGTCTGTAAACAAATCAGCCAACAGCCTGCCCCAGGGGCACCTGCCAGGG
+AACGCGCTCTGCCCAGGACGCCTGAGTGGGCAGCAGGCAGCACAGTGCACAGCACCCAGC
+AGCATCGGATTCTCTTCCAGGAACCTGAACTCCCTGGAGGCAGCCACAGCAGCAGAGAAA
+AGAGGACAGCACGCCGTGGCCTGATCACCAGCCAGGACCCATGAGGCCAGTCGGCCTCTG
+AGAATGCTTCTAGGAGCCCCCCGAGTCCTGCCCAGAAGCCCCCCTGACTGGGCTGGAGTG
+GGGGTCTGTGCCTGCAAAAATGACCTCCCCCCCTGCCGGGAGTTTCCCGAGACAACGAGG
+CACAGGGCGGTTCTTGGTAAGTTGTCACTTAAGGACCAGAAACTGGCCCAGTGCGGTGGC
+TCACACCTGTAATCCCTGCACTTCGGGAGGCTGAGGTGGGCAGATCACCTGAAGCCAGGG
+GTTTGAGACCAGCCTGGCCAACATGGCGAAAGCCCGTCTCTACTAAAAATACAAAAAGTA
+GCCCGGCGTGGTGGCGGGCGCCTGTAATCCCAGCTACTCTGGAGGCTGAGGCAGGAGAAT
+TGCTTGAACCCAGGAGGTGGAGGTTGCAGTGAGCCGAGATCCCCCCGCTGCACTCCAGCC
+TGGGTGACAGAGCAAGACTCTGTCCCACAAAAATAAATAAAATAAAGACCAGAAACCTTA
+CATGTCAGCCACCGGCTAGAAGGCGGGATGTCGCGTGGGAAGGGAGCTGGCATGAACCCA
+AGGTGGGGGCCCAATCCTCAGGCTCCCCTGGAACTTGGAGATCCTCCTCGCCCCGCCAGT
+GACGGTCAGCCCCTCCCTCCCTCTCCCCGCTCCTCTGCAGCATGCCTCTCACCGCCCAGC
+TGCAGGTGGCTTCCCGGCCCAAACTTGACTCCGTTTCCATCATTGCCTGTGTGTTATTTG
+AATAAGTGCGTTATGCGCATGTGTTTTAAATGTCATCATTACCATTTATAAACACCATCT
+GTTAGCAACTCTGCATTTGGGATTTTTAGAATAGCATTTCAGGTGCTCACTCACTTTGTG
+GGTGGGAATTGAGCCTGGTACAATCTCTTGGCGAACAATTTGGTCCTTGCAATCAGCTTA
+AAAATACACATTCCCCTCAACCCCACAAGACAGGTTAAATAAAAGCCACATAATGGAATA
+CATGCAGCCACTAAAAACAGATCTACATGAATGGATATGGTTTGATCTCAAAATTAAAGG
+TACAGGCCAGGTGTGGTGGCTCACGCCTGTAATCCCCAGCACTTTGGGAGGCCAAGGTGG
+GAGGATCGCTTAAGCTTAGGAGTTCGAGACCAGCCTGGGCAACATGGCAAACCCTGTCTC
+TACAAAAAAAAAAAAAAAAAGTAAAAATAAATTAGCCGCGTGCTGCGGAGCACACCTCTA
+GTCACAGCTACTCAGCAGGCTGAGCCAACAGGATCGCTTGAGCCTAGGAGTTCAAGGCTG
+CAGTGAGTCATGATCTCACCACTGCACTACAGCCTGGGTGACAGAGCAAGACCCCATCTC
+AGACTCACTAACTAACTAAGTAAATATGCCAAAGAGAGTGTATAATAAACTATGTGTGTT
+TGTAAAAAGCAAGACAGGCTACAGAAGTTCCAGGCTGCAGTGTTATGATCGTACCACTAT
+ACTCCAGCCTGGGCAACAGAGCAAGACCCTGTCTCAAAGAAAAAAGTAGGACAAGCTACA
+TACATGTACGTGTGCTCTCTGTGCTTAGAACACATAGAATACCTCTAGAACACACAGATG
+AAACCAATAACAATTACTGGCGGGTCCCATGCAGTCATGAGTTACTAGATCCTCTGGTTC
+TGCAAATTTTTCTTAACCCATATGCTGAATGACATCTACGAAAACAGTCTGTTCAATTGT
+GGGAAACTGATTGTTCCATCCAATAATCACAGCTTAGAACTATAACTGGTTATATGCCTC
+ACCTCATATTTTAATCCATCGGCCCAAATATAAGTCCCCTGTCCATGCATGAGTCCTTCT
+GAAAACATACCCTTCAAAACAAAACAAAGCAACGACAAACACTTAGAATACAGCTGACAC
+ATATACATATTTGAGATAGGGTCTGGTTCTGTCACCCAGGCTGGAGTGCAGTGGTGTGAT
+CATAGCTCACTGCAGCCTCGAACTCCCAGGCTCAAGCAATCCTCCCACTTCAGCCTCCCG
+AGTAGCTGGGACTACAGGCATCCACCACCATGCCCAGCTAATTTTTGTATTTTTTGTGGA
+GACGGGATTTCACCATGTTGGCCAGGCTGGTCTTGAAATCCTGAGCTCTAGCAATGCGCC
+CGCCTTGGCCTCCCAAAGTGCTGGGATTATAGGCATGAGCCACCGCGCCTGGCCTGCAGC
+TGATGATTCTCTCCCACAACTGCCTTATCCCGATTTCACATGCGTGAAGATGCTTGTCTG
+CACACTCAGCACCAGCTGAGTCCTAGTGAGTCCTACTCTGAGCTGCCTCCATGCTGGGCT
+CCATCCTTCTCTAAAAAGGATCTAAGAGGTCCTCATCTTCATGACCTAAGGATGACCTCA
+GCTACAAAAATGTGTTCTCAACCGGGTGCGGGGGCTCACACCTGCAATCCCAGCACTTTA
+GGAGTCTGAGGCAGGAGGATAACTTGTGCCCGGCAGTTCAAGACCAGCCCTGGCAACGTA
+GCAACTCCTTGTCTCTACCAAAAAAAAAAAAAAAAAAATTAAATTAGCCAGGCGTGCTAG
+CTCACACCTGTAGTCCCAGCTATTCAAGAGGCTGAGGAGGGAGGATCATTTGACTCCAGG
+AGGTCGAGGCCACAATGAGTTATGATTGTGCCACTGCACTCCAGCTTGGGTGACACAGTG
+AGACCCTGTCTCAAAAAATATAAAATAATCAGGAAAAGAAACAAATCTAAAATAACTTTT
+GTTATATTGAGCATTATTTTTACCTTAAATAGGTAATCAGGTTTCAGAATAAAATCGGCA
+TGAAGAGCTTCCGATTTCTTTTGAAGCATCAGTGGATTTTACTGAAGATTTACAAATCTA
+CGACCATCACCCCACACCTTCCTCCCCTTCCTGCAGGTTCTCAAATGGGCAACTTACACG
+ATAGGTACAACCGCCTTGAAAGGCTGCGAAGCCTTCTCCCTCATACAGCCCACGAACCTT
+TTCCCCTTCATAGCTACAAAGAAATAAAGGTAATTCAAGGTAATGAACAATGTGAATAAA
+CCCAAGTGACAGTGGGTTAAACTATATAACTATGTAATGGGAAGAATGAAGTCAGAAAAA
+AAAAAATATATATATATATATATACACAGAGCTAGAAAGTAGAAGAGGTTACCAGGGGTT
+TGAAAGTAGGGTGAGGAATGAAGGCGTTTCGGGGTTTTTTTGTTTGTTTTTTGGGGATTT
+TTTTTGAGATGGAGTCTCACTCTGTCGCCCGGGCTGGATGGAGTGCAATGACGTGATCTT
+GGCTCACTGCAACCTCTGCCTCCCGGGTTCAAGTGATTCTCCCGCCTCAGCCTCCTGAGT
+AGCTGGGATTACAGGCACATGTCACCACGCCCAGCTAATTATTGTGTTTTTAGTAGAGAT
+GGAGTTTCACCATATTGGCCAGACTGGTCTCAAACTCCTGGCCTCAAGTGATCTGCCCGC
+CTCAGCCTCCCAAAGTGCTGGGATTACAGGCTTGAACCACCGCATCTGGCCAGGAGTTAC
+TATTTAATAGACGGTCGTACAACACTATGAACGTACTTAATGCCATTGAATTGTACACTT
+AAAATAATTAAGATAGTACATTTTGTTATATGTTTCACCACAATAAACTCTATATATACA
+CACGCCATGGGGCTGTATGTTTGCTATTTGGGTGATGGGCTTACTTAGAAGCCCAAACCT
+CAGCATCACACAACATGCCCATGTAACAAACCTGCACATGTAACCCTCTAAATCTAAAAT
+AAAATAATTTTTTTAAATACATAAAATTACCTTCAGGCCAGGCACAGTGGCTTACGCCTG
+TAATCCCAGCACTTTGGGAGGCTGAGGCAGGTGGCTCACCTGAGGTCAGGAGTTCGAGAC
+CAGCCTGGCCAACAGGGTGAAACCTTGTCTCTACTAAAAGTACAAAAATTAGCCAGGCAT
+GGTGGCGGGCACCTGTAATCCCAGCTACTCAGGAGGCTGAGGCAGGAGAATTGCTTGAAT
+GTGGGAGGTGGAGGTTGCAGTGAGCCAAGATCACACCACTGCACTCCAGCCTGAACGACA
+GAGTGAAACTCTGTCTCAAAGTAAAATAAGATAAACCGCCTGACTGGCAGTGTTATACCC
+GATGGCACCCCCATTAAAATCACCTTTCCACTATGAGTTTGGTCAGAATGGACTCTTCGT
+ATTGGGTGGCATCTTCGTTCTGCTGAACGTTTTGGCGGTCTTTTTTGGGTTTCACTTCGT
+TGAGCTGCATTCCCAGCAATGGGACACCAGCTGGGGACATCTCTTGCCTAGTGGTGTTGC
+CATCTTGTTTGGAAAAGTCTAGATTATCAGAGAGAGATGAGGGAGAGCGGGCAGACTTCT
+CCCCTTTTTTGTCTGCTTTTTTCTTTTCTTTCACCATTGCCTTGGGAAGATCCAATGGTT
+ACTTGAATCAAATGATTTCTTTGGTTCAGAGCTGCTTGTTTCAAAGCACTGATGAGTTTT
+ATCTGAAAAATAAAAATTACGTCTCCAAACACTTGGGGTTTTCATTTGTAGTTAAAATTT
+CAGTTTTACAACACAATGTCATTATCATTCTCCTGACAAAGTCTGAAAAATTAGTTACCA
+GGGCCGGGTGTGGTGGCTCACACCTGCGATCTCAGCACGTTGAAGGGCCAAGGTGGGAGG
+ATCATGTGAGTCCAGGAGAGGGAGATCAGCCTAGGCCACGTAGTGAGATGCCACCTCTCT
+ACAAAAAATAAAAATAAATTAGCCAGGCGTGGTGGCACATGCCTGTAGTCCCAGCTACTA
+GGGAGGCTCAGGTGGGAGGACTGCTTGAGCCTGGGAGGTCGAGGCTGCAGTGAGTAGTGT
+CACACCACTGCACTCCAGTCTGGGTATCAGAGCAAGACTCTGTCTCAAAAATGACTATAA
+TTACAAGTTTCAAGTACCATCAGTTTATAAAAATACAACCTCAACATCGCATTGCTTGTT
+CCTAAAATTTTTTTATTTTTAATTTTTGAGACAGAGTCTCACTCTGTCACCCAGGCTGGA
+GGGCAGTGGCACAATCACAGCTCACTCTAGCCTCAACCTCCTAGGCTCTGACGATCCTTC
+CATCTCAGCCTCCCAAGTAGCTGGGACCACAGGCATGCATTACCACACCTGGCTAATTTT
+TTGTAGAGACAGGGTCTTGCTATCTTGCCCCGGCTGGTCTGGAACTCCTGAGCTCAAGCA
+ATCCGCCTGTCTCAGCCTCCCAAAGTGCTGGGATTATAGGTGTGAGCCACTGTACCTTGC
+CCCAAAAATTATTTAAGTTGGAACCATTGTCTAGCATTGTTTCTTGAAAGGTAACCCTAC
+ACATGAAATAGGCTACTTCACCTCTCAGGTCTTGCATGCAGCCAATTCACACTTTAAAAG
+CCCCTCTCTGGCCGGATGCAGTGGCTCACACCTGTAGTCCCAGCACTTTGGGAGGCCAAG
+GCAGGTGGATCACGAGGTCAGGAGATTGAGACCACCCTGGCTAACACTGTGAAACCCCGT
+CTCTACTAAAAATACAAAAAATTAGCCAGGCATGGTGGCACATGCCTGTAATCCCAGCTA
+CTCAGGAGGCTGAGGCAGGAGAATCACTTGAACCCAGGAGGTGGAGGTTGCAGTGAGCCG
+AGATCACACCACTGCACTCTAGCCTCGGCAACAGAGCAAGATTCTGTCTCAAAAAAAACA
+AAACAAAACAAAAGCCCCTCTCCTTATAGGTCAGCATTGTAAAGTGTGCAAGAGCTGGAT
+TCGGAGTCCTGCATTGCCCATTACCAGTTCTATGGGTTTGTTTATTTATTTATTTATTTA
+TTTTTGAGACGGAGTCTCACTCTCTTGCCCAGGCTGGAGTGCGGTGGTGCGATCTTGGCT
+CACTGCAAGCTCCACCTCCCGGGTTCATGCCATTCTCCTGCCTCAGCCTCCTGAGTAGCT
+AGGACTACAGGCGCCCACCACCACACCTGGCTAATTCTTTTTGTATTTTTAGTAGAGACG
+GGGTTTCACCGGGTTAGCCAGGATGGTCTCAATCTCCTGACCTCGTGATCTGCCCGCCTT
+GGCCTCCAAAGTGCTGGGATTACAGGCGTGAGTCACCGGGTGTGGGTGCCCGGCCCAGTT
+CTGTGTTTTTTGGGTTTGTTTTTTTTTTTTTTTTTAGACAGACTCTCTAGCCCTGTCCTG
+CAGGTTGGAATGCAGTGGCAGGATCTTGGCTCACTGGCTCACTGCAACCTCACTGCAGGT
+TCAAGTGATTCTCCTGCCTCAGCCTCTCGAGTAGCTGGGATTACAGGCACCTGCCTCCAT
+ACTCAGCTAATTTTTGTATTTTTAGTAGAGATGGGGTTTCACTGTGTTGGCCAGGCTGGT
+GTCGAACTCCTGACCTCGTGATCTGCCCGCCTTGGCCTCCCAAAGTGCTGGGATAACAAG
+TGTGAGCCACCGTGCCTGGCTGGTTTCCTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTGA
+GACGGGGTGTTGTACATTTTGCCCAGGCTGGTTTCAAACTCCTGGCCTCAAGCAATCTTC
+CCACCTTCTCCTCCCAAAGTGCTAGGATTGCGGGCATGAGCCACTGAGCTCGGCCAAGTG
+CTGTGTTCTGAAGCAAGCTGCTTAATCTCCTCTGCCTCACAAATAGAAATAACAGAACCT
+TGTCTCATAAGAATTAAACCGATGACACACAGAAAAATCCCTAAGTACAGGATACAGAGC
+AAAGTCAATAAATTGAGTGATTATCTCGTCCCTTTCCTGTTTTCAAACTTGAAATCATTG
+GTTTCCCACTCCCTCTAGCACTGCCATCGATTGAGTGCCTCTCATATGCCGGACAAGCAA
+GGACCGGTGTGCTGGAGTTGCGTTTCCAGCGCATGGTTGCTTGAGCTGTATTTCCAGCGC
+ATCGTTGCTCGAGCTCCGTTTCCAGCGCATATCTTTGCTTGTCTGGCATATGAGCTGCGG
+TGCAGGGTTTCAAAGCCATAGTTTTCATGGCTTTCCTAATCTGGCCCCGCTGAAAGCACC
+CTGGTCCATCAGGCAGGATGCATAGGTGAGCCCTGTGGTGAAGGCCAGGTCTGGTCCCTT
+TTCGTAGGCCCCGACGGGTGCAGTGGGCACTTCTTGCCCTCTTCTTCCTGGATGCCATCC
+TCTGGACACCCCACCCTCCAGCTGAACCCATCTCCAGCCTTCTCTCTTCCTCCATTATTT
+ATTTATTGAGACAGGGTCTCGCTCTGTCACCCAGGCTGGAGTGCAGTGGCACAGTCTTGG
+CTCACTGCAACCTTCCGGGTTCAAGTGATTCTTCTGCCCTAGCCTCCCAAGTAGTTGGGA
+TTACAGGTGCCTGCAACCACTCCCGGCTAATTTTTGTATTTTTAGTAGAGCCAGGGTTTC
+ACCATGTTGCCCAGGCTGGTCTCAAACTCCTAACCTCAGGTGATCCGCCCGCCTCGGCCT
+CCCAAAAGTGCTGGGGTTACAGGCGTGAGCCACCGCGCCCGGCCAAGCCTTCTCGCTTCC
+TTCCAACACCCTTGCTCCTTCCCGCCCCCGACTACTGTCTCAGCGAAGCCGCCCCTGGGT
+CCCCTAGCCCAAGGTGCTCTCACCTCTAAATTTAGAGGGGCCTTTACTACGAGCTTTTCG
+GTCTTCTGTCAGTGATCTACAAATAAGTGAACTACAAATCAAGCCAATTTCGTTTCTCAG
+TGCGTTTCCTAATGTTTCCTCTGTTCTCCTGGGCTTAAGGAGAGGCCATCTCTCTCCTGT
+GTCTACGGTGAGCCGGGAAGAATCGGCTCCCTGCACTGGTCTGCCCGGCCTAGGCCCTCC
+TCGCCCATCACGCACGTGCTCGGGTCCTGGGAGGCCGCGTCAGTCCGGCCGGGAAGGAGC
+AGGACCCAGTCGCCATGGCTGTCCCGGCGTACGCAGGACCGCGGCCTGGGGCGCTCACCT
+CGCTCCAGGAGCCCAGAGACCTCGCCGGGCTCGGGCTGAGGTGTTGCCGGGCTCTCGGCG
+TCCCAGACCCGGCTCCGGTCTCCAGGCAACCGCGGACGCCGCCAGGCCCACCCTGTGCTC
+TTAAAGGGGCCGCGCGCCAGCGCCAAGCAGGTGTCCCGCCCTTGCTGGTCCTGAAGGCCG
+GGGGAAAGGCTGGACGCTGGAGGCAGCAGGCCAGGGTTTTCCCAGCTCTGCTAACTGCTT
+CATCATAAAATAGGAATAACGCAGGCATTAGTTTTCCATTGCTGCCGCAAACAAATTACC
+ATAAATTTAGTGGTTCGAAGCAACACAAATTTATTACCCTACAGTATGTAAATTAGTCCC
+ACAGTGCTGGTTCCTTCCAGAGGCTGAGGGAGAGAATGCGTTTTCTTGCCTTTTCCAGCT
+TTTCCAGAAGCGGTCCCCAACCTTTTTGGCACCAGAGACCGGTTTCGCGGAACACAATTT
+TTCCATGGATTGGGGTCGGGGAGGGATGGTTTCAGGACGATTCAAGTGCATTGCATTTAT
+TGTGCACTTTATTTCTACTATTATTACATTGTAACATATAATTAAATAATTCTACAACTC
+ACCATCACAGAGACTCAGTGGGAGCCCTGAGCTTGTTTTCCTGCAACTAGACAGCCCCAT
+CTGGGGGTGACGGGAGACAGTGACAGATCATCAGGCATCAGATTCTCATAAGGAGCGTGC
+AACCTACATCCCTCGTGTGTGCAGTTCACAATAGGGCTCGTGCTGCTATGAGAATCTAAT
+GCCCACCGCTGATGTGACAGGAGGCGGAGCTCGGGTGGTAACGCCAGCGACGGGGAGTGG
+CTATAAATACAGATGAAGCTTCGCTGGCTTGCCGGCCCCTAACCTGCTGTGCACCCCACT
+TCCTAATAGGCCATGGACCACTACTGGTCTGTGTCCGGAGTGTTGGAATCCCTGTTCTAG
+AGACTGCTTGCAATCCTTGACTAGTGGTACCTCCTTCCATCTCCAAAACCAGCAAGACAG
+CCTCTCTCTGGCCAGCAGGGAAAGGTCTCCACCTTTGAAGGACTCACCCAATGGACTGGG
+CCCACCCAGACAATCCAGGATAATCTCTCTGTTGCAAGATCCTTAACTCAGCCAGGCATG
+ATGGCTCACACCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGTCGGATCACCTGAGGT
+CAGGAGTTCGAGACCAGCCTGGTCAACATGGTGAAACCCTGTCTCTACTAAAAATACAAA
+AATTAGCCAGTATGGTTCTGGACACCTGTAATCCCAGCTACTCGGGAGGCTGAGGTGGGA
+GAATCACTTGAACCTGGGAGGCAGAGGCTGCAGTGAGCTGAGATCATGCTATTGAACTCC
+AGCCTGGGCAACAAGAGCGAAACTTCATCTCAAAGAAAAAAAAAAAAAAGATCCTTCACT
+CAATCACACCTGCCGAGTCCCTTCTGCCACGTGAGGCAGCGTGGTCACAGGTTCTGGGGA
+TTAGGACACAGCTGTCTTGGGGGCTGTTATCCTGCCACAGCTCCCAATCTGGAGAGTTCA
+TAAGTGGGATCCTGCAGACCACGCCAGCACAGTGCCAGACACGATGGCACAGTGACTACT
+GTACTGCCTCCTCCATCTGAGGGATTCTAAAGCAGGAAGGGGAGCCGCCCACAGTCTGGA
+GAAGGGGTGGGGGCAGCAGGGGGAGCCACATCTGTCATCTCTGGGCCCCCAAGAGGGCAT
+CTTTACTTCCATTTTCAGCCAAGTTCAAACAGGACAAGGTTCCATGAAAACTATTTGAAA
+AGACAGACAGGGATTCTTATATTCCCAGAACCATTCAAGGCCAGTAACTGGAATGTTCTA
+CAGTTCACATCCTGAGGAAACCAAATCACAGCATCAAATTATGGGAAATCAAACTCTTTT
+TGTTCCCCTGCGAGGACAGCATTTTGCGACCTTGGCCGCACAGAGGAATGTTTCAAATAG
+TGACCCCTGTCCCATCCAGTCATTTTCTTCCAGCCGGGCAGAGAATCCCCCGTGTTTAAA
+AATTTAATGTGAATCAGGGCTGAGAATCACTAACTGAAAAGGACCCTACTTTTAAATTTA
+TGAAATTAAACAAAGATGAATTTAATTATCATTAAGGGTTGAAAGTTATAGACTAAACTA
+TGTCCAGCCAGAGCAGAGGCCTGAGTAACTTCCAAAGTGGTTTGGTTTTTTTTTTTTTGT
+TTTGTTTTGTTTTGTTTTTTGAGACACAGTCTTGTTCTATCTCACCCAGGCTGGAGCGCA
+GTGGCGCAATCTCGGTTCACTGCAACCTCCGTCTCCCGGGTTCAAGCGATTCTCCTGCCT
+CAGCCTCCTGGGTAGCGGGGATTACAGGCATGCGCCAGCACACCTGGCTAATTTTGTATT
+TTTAGTAGAGGCAGGGTTTCTCCATGTTGGTCAGGCTGGTCTCGAACTTCTGATCTCAGG
+TGATCCGCCGGCCTCGGCCTCCCAAAGTGCTGCGATCACAGGCATGAGCCACCATGCCCA
+GCCCAAGTGTTCTTATTTTTATAAAATGTGTTCTTGCCTGGACACACACACACGAGCGCA
+TGCAAACATAGAGAAAAAAAATTTGCAAGCAATGCTCCATCTGGTTTGAAAAGGTTCTCA
+AGATCACTTTTAAATGGGTGTGATGTGTATTTTTTTTAAGTAGCAGGTTCATTTTAAAAC
+AAAAAAGGTTAGTGAAGACTCTGTCTTTCAAAACATAAAAATCTGCGATAAAACCAATTA
+TTCCATACAGTGACTACGGTCAGTTCTGAGAAATGACACCCAGGTTGGCGATGTGTCTCA
+TGGTTGGCCTTCCATGGGGACAGTTCCAGGGGTGGTCCATCTCCCCCATGTGGGTGATCA
+GTTTCTTCATCTCGCTTGTGTTAAGAGCAGTCCCAATCATCACCTGAGTGTGAGACACAA
+TGGTTCAACGTTTTAGTAGTTTTTTGACGTCAGAATGGCAGCTCTTCAGAAGCATTCTTC
+TCTAAAATAAGGCTGGACAAGATTACAGCTCAAAAACTACCTTCCCTGAAAAACCTTCCC
+CCAGAGAAGCCTAGGTTCTAGATCTCAGCCCTCCACCCTTCTGTGAAATCAGGCTCCTTG
+TGGCTCCTTCAAGGTGGCACCGCCTCCACTCCAGACGCCGACCACACCTGTCTCAGCAGC
+CACCCTGCCCTCTCACCCTGGCAGGTGCAGCAGCCTCCCAGCAGGCCTCCCTGCCCCACT
+GCGACCCCTCCGAGCCGCTCTCCACTCAGCAGCCAGTGATTACTTTTAAAGGGCTGTCAG
+GTTATTCATTCCACTTCACAGCTCTCCCCCTCACCTGAATAAAAGCCCCCGTCTGTCCCC
+TGACTTGGCCCTCGCTGGGCTGTGCCTGCACCCCCACCTCCAAGCACGAATGCCTCCCTT
+CCTCACCCCAGCTGCACTGCTACTCCCTTCCTCTTGCACAGGCCCATCACGCAAACACCT
+GCCTTGGGACTGTGGCACTCCCGGGACCCTCTCCCCCAATGGGTGCAGGCGTCACTCCCC
+CTCTGTCGAGCTCCGACCTGCTGCCCATAGCACTCCAGCCCTGGCCCTGCTGCCTCCCTG
+CCATGGGTCCTCTGACAGGAAGGAGAGGACACAAGCCTGAAGCCCAATGTCACCTTCTTT
+CTTCCTGCAGCACCCTGAGGGCTCGCCATGTGCCAAGCACAGTCAGAAGGCTGGGGTGAC
+AGCAGGTTGGAGAAGGACAGACAATCAACAAGTCAACAGAGAACCAAGACAGGTGGCACC
+AGGCGAGGCGGCCTGCTCAGGTGTGGGGATGGGGTGAAGGGTGACGGTGGCAAACCCAGG
+TAGAGAGGAGAGTAGGGAGAAAGGGTGTAAGGCAGGGAGGAGACTGAGGCGAGCGTGGAA
+CTGGAAGGCAGCTACATGGCTGGAAGCTACATGGTGGGGAGATGGGGCTGGAAGGGTGGG
+CAGGGCTCAAAGCAGGAGCCTCCTGGGCAGGCAGTGACAACACCGGAGATGGACGGGTAG
+GCCAGGGCGAGAGGGAAGGAGCAGCCTGTGGTTCCCCGGGCCACTGAGTCACACTAAACT
+CAGGACATCAAAACTGCCCGGCTATGAGCTCAGCTCCACGCTCTCACTCACAGACTCCAA
+GACTGGAAGATCCATATTATGTCTTTTATTTTGGTGAGGTCAGGGGTGGTGGAGAGACTC
+TGTCTCCCAGGCTGGAATGCAATGGTGCGATCTCAGCTCACTGCAACTCCGCCTCCCAGA
+TTCAAGCAATTCTCCCGCTTCAGCCTCCCGAGTAGCTGGGATTACAGGCGCCCACCACCA
+TGCCCAGCTAATTTTCGTACTTTTAGTAGGGATGGGGTTTCACCATGTTGGCCAAGCTGG
+TCTCAAATTCCTGACCTCAGGTGATCAACCCACCTCCGCCTTCCAAAGTGCTGGGATTAC
+AGGTGTGAGCCACCACGCCCAGCCCCTATTAGGTCTTTATCCAAGAAACACTGTGGCTAG
+AAGTCAGACTCTGGGCCCTCTTCTAATTAAACTCTGCCCTTGAGTCATTTCATCTAATCT
+CATGGCTGTAAATTACACCTGAAGCTCACACAGCAGGCTCCATCCCACCCACTCCCCACG
+TGGCCCCCAGCTGCTGCTCTCCTCAGCGGCCGCAGCCACCGCACCCCTTCCAGTCTGTTC
+TCTCTCCAGCAGCTGCAATCACGGGACTCCTTCCCGTCTGTTCTCTCCAGTGGCTCGTGC
+CACACACAGCACAGACCCCCAGGGTCTAGGTATGACCGGCAACACTCTACGTGGCTGTCC
+TCTGGACGCCGCTCTGCTCACTCCCTTCCCCTCTCCAGGGACACAATCAGCCTCTGGCTT
+CAGTCTTGCTACTTCCTTCGCTTGGAAAGTTCTTACCCAAGAGGGCTCCATTCTACCTTT
+TTTTTTTTTTTTTTTGAGACAAGGTCTTACTCTGTCACCCAGGCTGGAGTGCAGTTGCGT
+GATGTTGGCTCATTGTAACCTCGACCTCCCTGGCTCAAGTGATCCTCCCACCTCAGCCTC
+CTGAGTAGCTGTGACTACAGGCACATGCCACCACACCTGGCTAATCTTTTAATTTTTTGT
+ACACATGGGGTCTGCCTGTGTTGCCCAGGCTGGTCTCTTAACTCCTGGCCTCAAGCAATC
+CTCCTGCCTTGGCCTCCCAAAATGCTGGGATTACACGTGTGAGCCACCATGCCTGGCTTC
+CATCCCACCTTTTAGATGGCAGCTGAGATGCCACCTGCCCAGATGCCATTCCCTGACCAC
+CATCTCACCTGGTCACCATGTTTTTCTCTTGTCATTTCCTGCCCCAAAACGCTGTTTTAG
+GCCAGGTGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGACCAAGGCGGGCAGAT
+CATGAGGTCAGGAGATCAACACCAGCCTGACCAACATGGTGAAACCCCATCTCTATTAAA
+AATATAAAAATTAGCCAGGTGTGGTGGGTGCCTGTAGTCCCAGCTACTTGGGAGGCTGAG
+GCAGGAGAATCGCTTGAACCTGGGAGGCGGAGGTTGCAGTGAGCTGAGATCACATCACTG
+CACTCCAGCCTAGTAACAGAGCGAGACTCCGTCTCAAAAACAGACAAAGAAAAATGCTGT
+TTGAATCTCTTGACTGTGCTTACTGGCATCTAATGCGTGTCATTTATTTGTGGTGATGCC
+TATTTCTCCCCACTGTCTGCTCCACAGGGGCAGGGGCTGCAGCCGCCTTGTTACCTCTGT
+GTCCCGAGCACCTGGAGCAGGGCGGGCCCCACATCAGGGGCTCAAGGAGCACCTGCTGAA
+TAAATAAAGGAATGGCGTCCTGGCCCTTCCCAGTGGCCAGCTGATACACAGTCACTTTTC
+TTGGACATCAGGCTAATCCCCACTGCAGGCAGAACCACTGCTGCCACCTTCCCACACCAA
+CCGAAGCAGCGGCAGTGACGCCACGTGCAATGACAACCACGGCACCCCGTGAAGCACCTG
+CTGCCTCGATGACTCTGCAGAATCGTGTCCAATGTCGCCGAGTCCTGGCAGCAGCAAATC
+TTTATCTCCCAATGTTGTTATGACCCATAAGGTCCATAGACGAACAAGGTACCTCAAACG
+CTAACTGCGTTGGAGTCAACCAAAGCTCGGAGATAGAATACTGGCCGGGCCAGGCACAGT
+GGCTCATGCCTGTAATTCCAGCACTTTGGGAGGCTGAGACAAGGGGCAAAAGGAGACCAT
+GTTTCTACAAAAAATTTAAAAATTAGCTGGGCATGGTGGTGCATGCCTGTGGTCACAACT
+ACTTGGGAGACAGAGAGAGGAGGATCGCTTCAGCCTGGTACGTCAAGGCTGCAGTGAGCT
+GTGATTGTGCCACTGCACTCCAGCCTGGGGGACAGAGGGAGAATCTGTCTAAAAAAAAAA
+AAAAGAAGAATTCTGGGTTTTTTTTGTTTTTTTGAGACGGAGTCTCGCTCTGTCGCCCAG
+GTTGGAGTGCAGTGGTATGAACTTGGCTCACTGCAAGTTCCGCCTTCTGGGTTCACGCCA
+TTCTCCTGCCTCAGCCTCCCGAGTAGCTGGGACTATAGGCGCCCGACACCACGCCCGGCT
+AATTTTTTTGTATTTTTAGTAGAGACGGGCTTTCACCATGTTAGCCAGGATGGTCTCGAT
+CTCCTGAACTCGTGATCCGCCCGCCTCAGCTTCCCAAAGTGCTGGGATTAGAGGCTTGAG
+CCACCATGCCCGGCCAAGAATACTGCTTAACAGAGGTAACAAAAGAGCAATAATTATGAG
+TTCAAGGTCACAGAGAACGCAGACGACACAGATGCTCAGCTACGACGCTGCACGTAGCTC
+TCTGTGTAAAATGACCCCTGGCAATCACAAAGGCGTTTACAACCTTGACCAAATCAGGAG
+CTGGGCTGAGACCTTCCTCGACTGCAAGCTTGAGCAGCTGAGCTGACAGCCAGGCTTTCT
+TTACTTACCGACTTCCGGCAGGCTCTGGAGGCAAACATCTGCTTGACTCGGGAAGGCCGG
+CACATGACCCCAGGGCTGTCGCTCAGCATGAAGATCAGTTCATCGACGTCCTGGGGTCCG
+AAGGTCCAGTTTTTACTAGTTGGCAAGGAAATCAGTTTAGCCCTTTCAGTGACTGGAGCT
+AAAAGAATACAATTTTGAGAAAAATCCATGACTTGACAAACACGTTTCACTTGAAAGCTA
+CTTAGGATGAACATCTGAGGCCGGGCGTGGTGGCTCACGCCTGTAATCCCTGCACTTTGG
+GAGGCTGAGGCCAGCGGATCATGAGGTCAGGAGATACAGACCATCCTGGCTAACATGGTG
+AAACCCCGTCTCTACTAAAAAATAGAAAAAATTAGCTGGGTGTGGTGGCAGGCACCTGTA
+GTCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATGGTGTGAACCTGGGAGGCGGAGCTTG
+CAGTGAGCCGAGATCGGCACCACTGCGCTCCAGCCTGGGCGACAGAGCAAGACTCCATCT
+CAGAAAAAAAAAAAGTGAACACCTGAAAGAGAGGAAACTCACAAAATGCTTTTTGGAGGA
+ACTTTTTAATCTTTTATAAAATTAAAAAAAACTGGTCTATATGACCTGAAAGATTATTCC
+CAGCTCTAAAAAGACAAGAATCTATAGTTCTGATTTTTTTTTTTTTTTGAGACAGAGTTT
+CACTCTTGTTGCCCAGGCTGGAGTGCAGTGACGTGATCTCGGCTCACTGCAACCTCCACC
+TCCCGGGTTCAAGCGATTCTCCCACCTCAGCCTCCTGAGTAGCTGGGATTACAGGCACCC
+GCCACCACGCCCGGCTACTTTTTGTATTTTCAGTAGAGATGGGGTTTCACCATGTTAGCC
+AGGCTGGTCTCAAACTCCTGACCTCAGGCGATCTGCCCGCCTTGGCCTCCCAGAGTGCTG
+GGATTACAGACGTGAGCCACCACACCCAGCCGCTATAGTTCTAATTAATAACTTACCATT
+TTCATCGATAACAAAATCAAAGCCATTCTTTCTAAATATTTCCAGATTTTCTATCAGAAC
+AGCTTCATTAACAGCAGTTAAGTTGAGAGTCTGAGGTCTGAAAAACACAAAAATGATTCA
+AACCATATCCTGAAGTCAAACATTTAGCTTTACAGCAGAAATGAAATGAAAACAACAATA
+CTGTATTTTGAATTCATGTCAAAATAACAACACAAATAACAACACTACTCAGCTAAGTGT
+CACAAAACTTCCTGAGAAGTTCCTTTTAATTTTCTCTTTCTTAAAGTTCTTTTTAGAAGT
+TAAAGTAGCTACAGGCCAGGTGCGGTGGCTCACGCCTGTAATCTCAGCACTTTAGGAGCC
+CGAGGCAGGCAGATCTCTTGAGGCCAGGAGTTTGAGACCGGCCTGGTCAACACAGCGAAA
+CACTCTCTCTACTAAAAATATAAAAATTAGGCCAGGCATGGTGGCGCACGCCTGTAGTCC
+CAGCTACTTGGGAGGCTTAGGCATGAGATTCGTTTGAACCCAGGAGGGAGGCAGAGGTTG
+TAGTGAGAGCCAAGATCACGCCACTGTACTCCAGCCTGGGCGACACAACAAGACTCTGTC
+TCAAAAAAAAAAAAAAAAAAAAAACACCCATAAAAACAAAAATTAGCTGGAAGTGGTGGC
+TCATGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCACTAGAATTGCTTGAACCCAGGA
+GGTGGAGGTTGCAGTGAGCCAAGATCACACCACTGCACTCCAGCCTGGGCAACAGGGCAA
+GACTCTGTCTCAAAAAAAAAAAAAAAGTTCAAGTAGCTACAAAAGTAGTTTGCTTTTTCC
+TCAGCCTGCCACGCCAATGACTCCCACTTTTTCTGAATCCTTTCCTTAAGGATAACAGTA
+TCACAAAAATGCTATTTTTCCTCCTTCTAATACAGAATTTGAAACACTGGGTTAGGTCAT
+TGCCAGCATTTGTAAACAGAATGAACAGACAGCTTTTATTTTGCTATCCTGTTCCTTCCT
+CTGCCTGTATTATATCTCCATCCCTCTCTCCTCCTGGATTTACTGTTTGTTTTTTTTTAA
+CCTTTCGTTATTTTTTTCAAAGATAGAGACAGGGTCTCACTATGTTGCCCAGGCTGCTCT
+CAAACTCCTGGGCTCAAGCGATCCTTCCACTTCAGCCTCCCAAAGTGCTGGGATTACGAG
+TGTGAGCCACTGCATCTGGTCCTGAGTGCTGGATAAGACAAACACTGCTCAAGGCAGGAG
+ACAGCTGGTGAGCAAACACAGGCTTGGTCCTGGAGCCAACAGATTACCGGGGAAGAAAGA
+CGTTGAGCAAATACTCAGGCAAGTCGATTATGATGAGAAACGACAGGAAGGTCAGGAAGA
+AAAAGCAGCCAGTGTCATAGAGAGACTTCACCCTGGGGTCAGGAAGTGACCTTTGAGCTG
+AGTCCGGGGATAAGAGAGTTAATCAGGTAACGGGGGAGAAGTGGGTGCAGGGTGCAGGAC
+AAGTATTCTAGACAGGGACAACAATCTGTGCCAAGCCCCAGGATGGACCGCTGATGTTTG
+CAGAGCCACACATAAAGATATCCTTCATTCTGCTTAGTGGCCACATAGGGATTCATCAGG
+CCTGCCAAGGGAAAAAGAAAGACAGCCAGAGAGGCTTGAGTACAGGGAACAAGGGGAAGA
+CGAACGGGAAAAGCTACAGAGGTCAACAGGGCCACCCTACACAGGGGCTGGCAGGGCAGG
+GTGGAACTGGGTCTTTATCCTTTAATCTTGAAGTGTGGTCCATCTGGGACCCTAAGTGGT
+CTGTGATTACCTGGGCCAACTTGAAATGTCACAGATGAGAGGTTATCTTTGCCGAATGGC
+TAAAAAATACAAGACCTCAGCCGGGCATGGTGGCTCACACCTGTAATCCCAGCACTTTGG
+GAGGCTGAGGTTGGTGGATCACCTGAGGTCAGGAGTTCAAGACCAGCCTGACAAACATGG
+CAAAACTCCCTATCTATTAAAAATCCAAAAATTAGCCAGGTGTGGTGGCGGGTGCCTGTA
+ATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCACTTGAACCCGAGAGGCAGAGGTTG
+CAGTAAGCCGAGATCACATCACTGCACTCCAGTATGGGCGAAAGAGTGAAACTCTGTCTC
+AAAAACACAAAAACAAAAAACCTCTATTAAGAGGAACAGGGAAGGGATATAAAGTAGCTT
+ACTAAATGTCTATTATTACCATTGCCTCCTACTGAGAATAAAAACAATTCACGCATTCCA
+CAGGAGAGTACTCAGCAAACTACACAGGAGAGTACTCAGCAAACTACACAGGAGAGTACT
+CAGTAAACTACACAGGAGAGTACTCAGCAAACTACACAGGTTCAGTGGTACATTTCTCCA
+TGTGGGATCTACTTGTTGGGATCTGAGTTTACTTCACTACGTGGTTTAATTTCCCACACG
+AAAATCCATGACCTCTTCTTCTAACTTTGCTGAAGACAAGACTTTGGTTTTACATGATAC
+TATCACACCTGACCTTTGTGAAGTAGTCAGGGTAAAACATTCCAGTTTGGCCGAGGAGAG
+AGAAATACCAAATTCTGCAGTGACTATCTTAAAATAATTTTTAAATTTTATTTTATTTTA
+TTTATTAATTTATTTGTGAGACAGAGTCTCACTGTCTCACTCTGTCACCCAGGCTGGAGA
+GCTGTGCAGTGGCACGATCATGGCAGCCTCAATCTCCTGGGCTCAAACGATCCTCCCACC
+TCAGCCTCCCGAATAGCTGGGACCACAGGCACACACCATCAAGTCTGACTAATTTTTTAC
+ATTTGTTGTAGAGACAAGGTTTCACCATGATGCCCAGGCTGGTCTCAAACTCCTAAGCTC
+GAGGGATCTGCCTGCCTCAGCCTCCCAAAGCTCTGGGATTACAGGCGTGTGCCCCTGCAT
+CCAACCTGCAGTGACTATCTGACTTCTGATTACTCTACTGTCAATCAACACTGGCGCACA
+GGCTGTCTGTCTTTCTGAACACACACATTCCATACACTATGCATACTAATACTCCATACT
+ATCAATTGCCCTCATCAGAAGGATCTTCTGGCTAACCAGTGATCAACATTTTTAATAGCG
+AAAAATACCTGATACTTAGAGAACATGTTAACCACGTGAACTGGGGCAGGTTACTCAACC
+TCTCTGCATGTGCCTCAGTTTTATCGCTTGTGGAATGGTGATGGTAACAGTAACAACCCC
+ATAGGTTTTTGAGGATTAAAGGAACTAATACACATACATTATTTCAACAGTGCCTGGCAG
+ATTCTAGGCACTGAATAAATGGTAACTATCACTATTATGTAAAAAGTATAAAAATCTGCT
+ATATGAATACTTATGGAAAAATACATATATACATATAGACACACATATAAACTATTAGGT
+CTCTTTTTTTTTTTGAGATAGAATCTCGCTCTGTCACCCAGGCTGGAGTGCAGTGGTGCG
+ATCTCGGCTCACTGCAACCTCTGTCTCCCAGGTTCAAGCGATTCTCCTACCTCAGTCTCC
+TGAGTAGCTGGAATTACAGGCGTGCACTGCCATGCCCAGCTAATTTTTTGTATTTTTATT
+TTTTATCATTATTATTATTTTTTGAGACGGAGTTTCACTCTTGTTGCCCAGGCTGGAGTG
+CGATGGCACGAACTCGGCTCGCTGCAAACTCCGCCTCCCGGGTTCAAGCGATTCTCCTGC
+CTCAGCCTCCCAAGTAGCTGGGACTACAGGCGCCCGCCACCACGCCTGGCTAATTTTGTA
+TTTTTAGTAGAGACAGGTCTCACCATGTTGGTCAGGCTGGTCTCGAACTCCCGACCTGAA
+GTGATCTGCCCACCTCGGCCTCCCAAAGTGCCGGGATTATAGGCGTGAGCCACCGTGCCT
+GGCCTTTTTGTATTTTTAGTAGAGGCGGGGTTTCACCACGTTGGCCAGGCTGGTCTCCAA
+CTCCTGACCTCAGGTGATCTGCCTGCCTCGGCCTCCCAAAGTGCTGGGATTACAGGTGTG
+AGGCACCGCGCCTGGCCAACTAGATATTTTTTATTTTTTACACCCCTCCTTCCTAGATCT
+CTTCTTTTTTAAAGTAGATACAAGGTCTTGCTGTGTTGTCCGGGCTGGTCTCAAACTCCT
+GGCCTCTTGTGATCCTCCTGCCTTGGCCTCTATTAGATCTTCAATTTGAGGGGGAGTCTG
+GGAATGAACACTAAACACACTCACGCTATGAGCCTCTGCCCCTGGAGCACGGTGTGCTGC
+TGCAGCATCTCGAAGTTATACTTCTCGTCCGTGGCATGCTGGTCCACTATGAAGATATCC
+TCATTCAGTTTGGTTATTATAAATCCCAGGTTAAACTGACCAATGATTTCCATTTCTGCA
+AACATCGTTTTACTGCAGGTAGAAAATGTTAATTATCAGACATTTTACAAGATTATTTTT
+CTGATTATGTTATAGAACACTGTAATAAAAAAAAAGTCAAACAATACAAAAACAAAATAA
+AGTCCCTAGCCATCCCGCTTTCTTTTTTTTTGAAACAGAGTCTCGTTCTGTCACCCAGGC
+TACAGTGCAATGGCACAATCTTGGCTCACTGCAACCTCCACCTCCCGGGTTCGAGTGATT
+CTTCTGCCTCAGCCTCCTGAGTAGCTGGGATTACAGGTGCGCCACCATGCCCAGCTAATT
+TTTGTATTTTTAGTAGAGACAGAGTTCCACCATGTTGGTCAGGCTGGTCTCGAACTCCTG
+ACCTCATGATCTGCCCGCCTTGGCCTCCCAAAGTGCTGGGATTACAGGCGTGAGCCACTG
+CGTTCGGCTTAACCATCCCACTTTCTAAAGATAACATTAATTATTCATTCATCCAACTCT
+CCGGAGAAGACATCAGTTGCTACTATTAACGATTTAAATGGAATATATCCTTCTAGACCC
+TTGTCTCCATATATAATTTTTTTTAATTTTAAAAAACAAAAATGGAATCTTAATTCTCCA
+TTCTGTCATCACTTAATGCATCTGAAACAAGTTTTCAGACCTGTACACATAGATCTACTT
+CATTATTTTTTCTTTTTTTTTTTCTTTTAAGACGGAGTCTCACTCTCTGTTGCCCAGGCT
+GGACTGCAGTGGCGTGACCGTGGCTCACTGCAACCTGCGCCTCCCAGGTTCGAGCGATTC
+TCCTGCCTCAGCCTCCCGAGTAGCTGGGACTACAGGCATGCACCGCCAAGCCCGGCTAAT
+TTTTTTATTTTTAGTAGAGACAAGGTTTCACCATGTTGGCTAGGCTGGTCTTGAACTCCC
+GACCTCAAGTGATCCACCTGCCTCGGCCTCCCAAAGTGCTGGGATTACAGGCGTGAGCCA
+CCGCACCTGGCCTACTTCATTCTTTTTAATGGCCACATAGGAATTCATTGCATGGATGTA
+CCATAATTTGTCTGACAAATCCCCTACTAAAGGACATTTCAGTTGTTTCCAATTTCAATA
+GCGCACTCAAAGCTGCAACAAATACTTCTGTGCATAAACCTACTCATCTGTGGGTGCATT
+TCCGTGAGACAGACGCTAGAGGGAGAACTACATATGTACTTCTTGACGGGAAATCTGTGA
+AAAGTCACACTCCCACCAATGGTGTGTAAGAGCACCTTTCTGCCAATGCTGGATATCAAT
+CCTTCTCATCTTTGCCAGGCCCACCACTGGGTCCTTTGCGGGTGGCTTCAACATCTAATG
+TCATTAAATACTAACTTAGTCAATCTGGACAAAAGACAGACACCACCGCTAACCTTCACA
+CGAGAAATTGACACTGTCATTCTCAGTCCCACACAATTAAATCCGGTGAAAATGGATTTT
+CCGCAGTATCAGCGCGGTGATGACAAGAAATGGCTCTGTTAAAGCAGCCATGGACGTTTT
+CTGGTTCTCACCTGGTGGCCTGAGCTGAGGATGAAAGCAGCTGTAATGTAATCCCAGCAC
+TTTGGGAAGACAAGGTGGGCAGATCATTTGAGGTTGGGAGTTCAAGACCAGCCTGGCCAA
+CATGGTGAAACCCCATCTCTACTAAAAATAAAAAAATTAGCCAGGCATGGTGGTGGACAC
+CTGTACTCCCAGCTACTTGGGAAACGAAGGCAGAAGAATCGTTTGAACCCGGGAGGCAGA
+GCTTGCAGTGAGCTGAGATCGTGCCAGTGCACTCCAGCCTGGGCGAAAGAGTGAGACTCT
+TGTCTCAAAAAAAAAACAAAGGAGCTGATATTGTTGTTTCTTTCTATAAGTGCTCCAGGA
+AGACCCGGTCCCATGCCACCATGCTCGTCACCATCACAATCAACCACAGGGGACAGTTTG
+GTGAACTGTGAGACCTCCACATGGCATGGATTACTGAGCCCACATTTCCTATGGTGAGGG
+GCTCCACACAGAGCTCAAATCCAAGTCATAACCAAACCAGTCCCCAAATCCTATCTTTGA
+GGGTCTGTTTCCTGGTACCAATTCCAGATCAGGCAGAGTGCAATCAATCAAGAGACAAAA
+ACCACACCAGTGATTTTAACAGGGACTTTTTTTTTTAAGACAGGGTCTTGCTCTGTCACC
+CAGGCTGGAGTGCAATGGCATGATCATAGCTCACTGCAGCCTCAAACTCCTGGGCTCAAG
+TGAGCCTCCTGCCTCAGCCCCCTGAGTACCTGGGACTACAGGCGTACAGCAATGTACTTA
+GCTAATTTTTTTTTTTTTTTTTTTTTTTTAGAGATGGGGCCTCATTATATTGCCCAGGCT
+GGTCTCAAACTCCTAGCCTCAAGTGATTCTCCTGCCTCAGCCTCCCAAAGTGCTGGAATT
+ACAAGGTGTGCACCACCATGTTAGGCCTGAGGAGGAAAAATGTATAATAAGGCATTACAC
+AAACTAGTAAAAGGTGGTTAACTACTATGCTAAGAAATACAGGAATGGAAAATGCTACTA
+TCCTAGGGAAGAGGGAGAGTCCTCAGAAAAGGAACTCTTTTTTTCTTTTTTCTTTTTCTT
+TTTTTTTTTTTTGAGATGGAGTTCGCTCTTGTTGCCCAGGCTGGAGTGCAATGGTGCAAT
+CTCGGCTCACCACAACCTCCACCTCCCGGGTTCAAGCAATTCTCCTGCCTCAGCCTCCCA
+AGTAGCTGGGATTACAGGCATGCACCACCATATCCCACTAATTTTGCATTTTTAGTAGAG
+AAAAGGTTTCTCCATGTTGGTCAGCCTGGTCTCGAACTCCCAACCTCAGGTGATCCACCC
+ACCTCAGCCTCCCAAAGTGCTGGGATTACAGGCATGAGCCACCATGCCCAGCAGAAAAGG
+AACTCTTGTAAGAGGCTCCTACCCACTCAGGCTGAGTTTCAGACCTCCTTGGAGCAGGAG
+TGGCCGCAGCCTGCTGGATGGAGAGAAGCTGCCAGAGTGAGTGATGACACAGGAACTCCT
+GCCGCACAGGAGGGAAGGAAAAGAACATCCCAGAAGCATCCCAGATGCCAGCACAAATAC
+CACCTCCCCTGGCGCCGATCCCAGGCTCTCCCAGGAATTGTCTGAATATGCCCTGGTTCC
+CAGTACATAGATAATCTGCTCAAAAGCTGGTGCTGGCCTAAAAGACCCAAGTCTTCCATG
+TGTTTGGAGTCTGTGTCCTGCCACAGAGAACAGGATCTGGCCAGGCGCAGATGCCGGAAT
+TACAACTGCGCACTACCGCGCCCAGCCAATTTTATTGTAGAGACGAGGTCTCCCTATGTT
+GTCCAGGCTGGTCTTGAACTCCTGGGCTCAAGTGATCCTCCCTCCTTGGCTTGGCCTCCC
+AAAGTACTGGGATTACAGGTGTGAGCCACCACACCTAGCCTCAAAATACTCTTAAGAAAA
+AACTTTACCTGGCCGGGTGTGGTGGCTCACACCTGTAATCCCAGCACTTTGGGAGGCCAA
+GGTGGCTGGATCACCTGAAGTCAGGAGTTCGAGACCAGCCCAGCCAACATGGTGAAACCC
+TGTTTCCACCAAAAATATAAAAATTAGCCAGGCATGGTGGCGTGCACCTGTAATCCCAGC
+TACTCAGGAGGCTGAGGCAGGAGAAACGCTTGAACCCGGGAGGTGGAGGCTGCAGTGAGC
+CAAGATCATGCCACTGCATTCCAGCCTGCGCAACAGAGCAAGACTCTGTCTCAAAAAAAT
+AAAAAATAAAAATAAAAATTTTAGATAAAAAGAGAAAAAGTAAAAAATTAAAACTTTACC
+TTATCTCTTTTCTTAGTTCATCTTCGGCTGCTTGATTTTCTCCAGGACAAATCTTTGCCC
+TAAACTTCCTGTAATTCTGTTCCCCTTCACTTTGCTGTGCTTCATGATGTAACTGCTTTA
+TTCGTTTAGCTAAAGAACTCATAGAAAAGTCCAGGGGCACAACTTTCTTATTAATTTTCA
+CAGCTACATCAACCTGAGAGGCTGACATGTCCTGAGTATTTACTAACTTTTGACAAATGT
+CAGAACTGGAAAGAATTTCTTCTTTTTTAAAACGCTTTGTGTTTGGGGTTGCGAGATTAG
+TTGGCTGAGGCAAAACTCGAAATTTACATCCGGTATCTTCCTGGTTTGAATGGCAGTCCA
+CATCTGAAAAAGAGTCGTCAGTTTTAGGCGCTTTCTCCTGAGAGTCCACATGTTCCTGCG
+AGCCCCTGTCCCCTGGGGAGCTGGCCGCATACTCGCTGCTGCAGTGACTGCCCGTGTCTG
+GGATGCTGAACCCCTCAGAATCCACGGAAGTGCTGCCGTGCCCCGAGTCCTTCTCCACCT
+CCGCTCTGTCCGTAGGGTCACTGGGTCCGTGACTGGAACTCACTGCCTCTTTCTGAGGTC
+TCAGGACGCCTTTGTCAGAGATGGCACCTGAAGTGCTAGAAGACAGCATACCCCTTTTCT
+GTCCTAGAGGGCTCCTTCTTGGTTCTGGAGTCTTTGGGCTGTGAGGCTTGTTCTCTGTTG
+TGTGACGAAGAGAAAAGGCCTCTCGCAGTCTGGAAATGGACACGTCTTTTTTTTCTTCTC
+CAGTCCTTAATGAAGGGGATTGATCCTGCTTTTCTACCATGGGCTTTTCCAAATCCGCTG
+CATGCATTTTTATTAAGTTACCTAAGCAAACGTGGACGGAGAAGAGGGTCAGGGACTATC
+CTGAAATGGTGAGAGGACGTGCTTATGTGAACAGATACTTCACAAAAGAGGAGATCCACA
+TGCTAATTACACAGATGAACACAGTTCAATGTTCAAAATAAAACTATAATATGGGCCAGG
+TGTGGTGGCTTACGCCTGTTATCCCAGCACTTTAGGAGGCCAAGGCAGGGGGATCACATG
+AGGCTAGGAGTTCAGGACTGGTCTGGACAACATGGTAAAACCCTGTTTCTACTAAAAATA
+CAAAAATTAGCCGGGTGTGGTGGCATATCTGTCATCCCAGCTACTTGGGAGGCTGAGGCA
+CGAGAATCCCTTTAGCCCGGGAGGCAGAGGTTGCAGTGAGCCAAGATGCCACCACTGCTC
+TCCAGCCTGGGTGACAGAGCAACACTCTGTCTCAAAAAAAAAAAAAAAAAAAAAAAAAAC
+CACAACACAATGCAATATGGCCATATACTCACCAGAATGGTAAAATTAAAAAAACAACAA
+ATGCTCACAAAGATCAGGATCAAGAGGAATGCCTGAATACCTCTGGTAGGAATGAACCTG
+GTACAGCTGCTTTGAAAAGTTCTCTGGGAATACCTCCTAAATCTGAATGTATGCACACCT
+GCAACCCAGCATAGCTACTCCTATCAGAAGTGCCTATTGGCCGGCACAGTGGCTCACGCC
+TGTAATCCTAGCCCTTTGAGGTCAGGAGTTCAAGACCAGCCTGACCAACATGGTGAAACC
+TCATCTCTACTAAAAATACAAAAAAAAAATTAGCAGGGCATAGTGGAATGCACTTATAAT
+CCCAGCTACTAGGGAGAATGAGAATGAGGCAGGAGAATCACTTGAACCTGGAAGGCAGGG
+TTGCAGCGAGCCAAGATCACTCCACTGCACTCCAGCCTGGGCGACAGAGTGAGACTCCCT
+CTCAAAAAAAAGAAAGAAGTGCCTATCTATGCTCGTCAAAAAGACGTGGATGAGGATGTT
+CATGACAGCATTCTTCATTATAGCCCCAAACTGGAAACAATTCAAATATTCACAAATGAT
+GATATCTGACTATAATGGAACACTGTATAGCGAACGAATAAATGAATTTTGCCACATGAC
+TTGGGTGAATCTCACAAACAAAATAATGAGAGAAAGAAACAAATCACAGAAAAGGACAGA
+CTGAATAACTTCAAATTAAAAACAGATTAAACTATACCGTTTTGGGTTTTTTTTGTTTGT
+TTGTCTGTTTTTTTGAGACGGAGTCTCGCTTTGTCACCCAGGCTGGAGTGCAGTGGCACA
+ATCTTGGCTCACTGCAAGCCCCTCCTCCCGGGTTCACGCCATTCTCCTGAGTCAGCCTCC
+TGAGTAGCTGGGACTACAGGCGCCCGCCACCACGCCCGGCTAATTTTTTGTATTTTTAGT
+AGAGACAGAGTTTCACCGTGTTAGATAGTCTCGATCTCCTGACCTCGTGAGCCGCCCGCC
+TTGGCCTCCCAAAGTACTGGGATTACAAGCATGAGCCGCTGCGCCTGGCCTAAATTCTAC
+TGTTAGAAGTCAGGAAATCCCAGCATTTTCAGAGGCCAAGGCTAGAGGACTGCTTGAGCT
+CAAGAGTTTGAGACCAGCCTGGGCATCATGGAGAAACCCCATCTCTAATGACAATACAAA
+CATTAGCCAGGTGTGGTGGTGGGCGCCTGTAATCCCAGCTACTCAGGAGGCTGAGGCAGG
+AGAATCTCTTGAACGTGGGAGGCTTCAAGGTTGCAGTGAGCTGAGATCGCATCATTGCAC
+TCCAGCCTGGGTGACAAGAGCGAAACTCCATCTCAAAAAAACAGACATGACAAGGGAGTT
+AAAAATGCAGTCACTGCAGACTTCTTCTAATCATATATCTTATATGACTTCATCCGTTTA
+CAGTTTACAAAAAACTAGAGGTACTTGGAGGCAGCTACTTGGGAGGCTGAGGCAGGAAGA
+TGGCCTGAGCCCAGGAGTGTGATGCTGCAGTGAGCTACAATGGCACCACTGCAGTCCAGC
+CTGGGTGACAGAGCAAGTCCCTGTCTCAAAAAAGAATTAAAAATGATAAAATAATATAAG
+AGACTTTGTTTTCATGTCAAAAAAAAGTTTACTTGGAAAAAATAAGGAAACACATTAGCT
+AAAAGCTTTAGAAGCTGTTTGTACACTGTATTTTTCTTACCTTCAACATCCAGCAGTGGC
+TGCTGACTGACATTTAGCTTGTTGACATCACTATCAAACATTCCTATCAAAGAGGTCTTT
+AAAACTGCCAACAAAAGCTTTTCCTCTTGTAGCAAAATTTGCCTTTTATCTGGAGTAACA
+TTGATATCAACGCATTCTAAGGCAAAAAAGAAAACATATTTATTATGTTTAAATTCACTT
+TTATTTTATTTATTAATTATTATTTTCAGACAGCGTCTCACTCTGTCGCCTAGGCTGGAG
+TGCAGTGGCGCGATCTCAGCTCACTGCAACCTCCGCCTCCTGGGTTCAAGTGATTCTCCC
+TGCCTCAGCCTCCGAAGTAGCTAGGATTACAGGCAAGTGCCACCACACTGGCTAATTTTT
+GTATTTTTAGTAGAGATGGGGTTTCACCGTGTTGGCCAGGCTGGTCTCGAACTCACAACC
+TCAAGTGATCCACCCGCCTTGGCCTCCCAAAGTTCTGGGATTACAGGCGTGAGCCACCGC
+GCCCAGCCAAATTCACTTTTAACAATAGAAATTTCCCCATCTATTATTTCATTCACTTGT
+ATTTATCACAAGTGCTATTAAAAACATTACAGTGTCCAGGTTAAGATTCATAAGTTATGA
+AATCAGCTTTTTCAAATAAATGAGCAAAAGACAATTTTTGAATAGACAAAATACGGAAGG
+GCTTAATTAGGTAAATTGTTAAAGGAAAAGCAAATAAACACATAAAAATAATTTTAAATA
+TGCAAACTAAAATAAGATATTTTAATCCCCTACTGAATTTAGCTTAACAATTATAATACC
+TAGTACATTATAGGTAGGTGTGTAAATTGGTACATCTAGAACACAATACAGAAAAAGCCT
+TAAAATGATCATATTCACTGACCCAGTAATTCTACTCCCGGCAATTTATATTCAGAATAA
+TTAAAGATGTAGGCTGAGTGCAGTGGCTCACACCCTGTAATCCCAGCACTTTGGGAGGCT
+GAGACGAACAGATAAGTTAAGGTCAGGAGTTCAAGACCAGCCTGGCCAACATGGCGAAAC
+CCCGTCTCTACTAAAAACACAAAAAATTAGTCAGGCATGGTGGCAGGTGCCTGTAATCCG
+TGCTACTCAGGAGGCTGAGGCGGGAGAATCGCTTGAACTCAGGAATCGGAGGTTACAGTG
+AGCTGATATTACACCACTGCACTCCAGCTTGGGAGACAGAGCAAGACTCTGTCTCAAAAA
+ATATCTAATAATAAAGATGCAGATAATGATTTAATTATAAGGAAAGTATTTATAATTTCC
+AAAAACTAAAAACAATTTAATTTTGAAAAATTTAAAAATTAAAATACCAAACTATAACCA
+TGCATTGGAATATAATTCACCTATTAAAACCACATTTCTGATCAATTTCTAATAACATGG
+AAAAGAAAACATTCACATCTAAGGATAAAGAGCAGTATACAAAATTATTTTCTCATCCCA
+AAGAATATGGGAGTAGGGGAGAGAGAGAGAAAGAGAGAGAGGACAGAAGATATTTTTTAA
+GGTATGTACATATGTGTTTCTAAGTATCTAGAAAAAATACTCAATTACAATAAACCAAAA
+TTTTAACAATCAGAAAAAAAAATCTATATGAAATGAATTATTTATGAAATTAGGAAGAAC
+ATTTCATCTACTTTCTCCCTTGGTTGACATTAAAAAAAATTACATTTTCCTAACAATATA
+ATTAACATAGTCTCAAGTAGAAAGCGGGAACTCTGTTTAAAAAAAAAAAAAATTATAGGG
+CCAGGCACGGTGGCTCATGCCTGTAATCCCAGCACTTTGGGAGGCCAAGACGGGCAGATC
+ACGAGGTCAGGAGATCGAGACCATCCTGGCTAACACGGTGAAACCCTGTCTCTACTAAAA
+ATACAAAAAATTAGCCAGGTGTGGTGGCACGCACCTGTAGTCCCAGCTACTTGGGAGGCT
+GAGTCAGGAGAATCGCTTGAACCCGGGAGGCAGAGGTTGCAGTGAGCCGAGATCACGCCA
+CCACACTCCAGCCTGGGTGACAGAGCAAGACCCCGTCTCAAAAAAAAACAAAAACAAAAA
+ACTTACATGACCATAAATTGTTATCTCATTCCAGTCATAGCAGAGCTGTAGAATTTCATT
+TTATTCTTTGAGGCATTAGTCACTAGTTGTACTGAAATGCCAATGGAACTTACCTGAATC
+AACAGAAATGTTAAGAACAACAAATGGATACTGGTGTCGATTATACATGTGGTAGACCTC
+ATTCACGAGTCTGCAGACCTGCACAAAATACAAGGAGTAGAAAAGAATAAATGACAAATG
+TTCCCAGCCCCCCGCATTCTAACAACATTCTATTCTAACCAACCAGCATGTTCTTAGAAG
+GGGATACTTTTTTGTTTTTTTTTTTTTTGAGTCAAGGTCTCGCCTTGTCACAGCCTGGAG
+TGCAGTGGAGCAATCATGGCTCACTGCAGCCTCAACCTCCCAGGCTCAAGTGATCCTCCT
+GTGTCAGCCTGACATGTAACTTGGATTACAGGCAGGATTTTTTTTTCTTTTTTTTTTTCA
+ACGGAGTCTCGCTCTTGTTACCCAGACTGGAGTGTAATGGCACGATCTTGGCTCACTGCA
+ACCTCTGCCTCCGGGGCTCAAGTGATTATCCTGACTCAGCCTCCAGAGTAGCTGGGATTA
+CAGGCACACGCCACCATGACCAGATAATTTTTGTGTTTTTAGTAGAGATGGGGTTTCACC
+ATGTTGGCCAGGCTGGTCTCGAACTCCTGACCTCAGTTGATCCGCCCGCCTCAACCTCCC
+AAAGTGCTGGGATTATAGGCGTAAGCCACTACACCTGGCCTAAGGATACATTTTTTTAAC
+AGCTTTACTGAGATATGACTAACATGGAATAAACTACACATATTTAAAGTGTGCAATTTC
+ATAAGTTTTGACATATACACAAACACCTGTGAAACTATCCCCACAATCAAGATAATGAAT
+ATATCCATCACCAAAAGTTTCCTCACAATCTCAAAGTGATATTTCTCTAATCATAGATTC
+CTAAAACTGAATATTTTTCCAACTTAAAGTTGCTCTATGAGAAATTCTAGTGAAATGCAA
+GTGCAGCTTAAATGTTCATAAAACATATTCAATGTACATAGAAAAGTATCTATGACATTA
+AAATGTCATTAGAAATAAACCAAAATATCACATTATTAATAGTTATAATTAATAATTATG
+AATCCATCACACTATAGGTTAAAAAATTTAGAAGTTCAACCACATCTGGCAGATTACAAG
+CAAACTCTAAAGCATCATTGAAAAACAGGGGCTGGGAGCGGTGGCTCACGCCTGTAATCC
+CAGCACTTTGGGAGGTCAAGGCAGGTGGATTGCCTGAGCTCAGGAGTTCTTGACTAGCCT
+GGGCAACACAGTGAAACCCCATCTCTACTCAAATACAAAAAATTAGCCAGGCATGGCAGC
+ATGTGCCTATAATCCCAGCTACTTGAGAGGCTGAGGCAGGAGAATTGCTTGAACCTGGGA
+GGGAGAGCTTGCAGTGAGCCAAGATCACGTCACTGCACTCTAGCCTGGGCGACAGAGCTA
+GACTCCGTCTCAAAAAAAAAAAAAAAAAAAAGAAAGAAAGAAAAAAAAACAAAATATTAC
+TGAGGTACAATGTGTTGCTAAGATACAAACTCAAAAAACCCATGTCATCATATCAAGATG
+ATCAATTTAAATCTGAGGCAGAAGTAATCTGAGCCCTTATTTTCCTAGGAAAATAGAAAG
+AAGAGAAAATATAGAAATCTATAGAAAATATAGAAACCATGGGCCGGGCGCGGTGGCTCA
+TGCCTGTAATCCCAGCACTTTGGGAGACAGAGGCGGGTGGATCACGAGGTCAGGAGTTCG
+AGACCAGCCTGGCCAATGTGGTGAAACCCCGTATCTACTAAAAATACAAAAATTAGCCGG
+GTGTGGTGATGCGTGCCTGTAGTCCTAGCTACTAGAGAGGCTGGGGCAGGAGAATGGCGT
+GAACCTGGGAGGCGGTGCTTGCAGTGAGCAGAGATCATGCCACTGCACTCCAGCCTGGGG
+GTGACAGAGCGAGACTCTGTCTCAAAAAAAAAAAAAAAAAAAAAAAAAGGAAATATAGAA
+ACCATGTAATCAGTCTATACTGAAAGGTGACATAGAATGTTATAAAATGTTTAGTTTCTT
+CAAATAGTTTTAGTTTTTACAATAATAAATATACTGGTAATATGTGTTTATATATTTATG
+TATCTATACACACAACACATATAATGTATATATGCAGATACAAACACACTCACGTATATG
+CAATTTAAAAAACTATACAGAGGCCAGGCGCGGTGGTTCACGCCTGTAATCCCAGCACTT
+CGGGAGGCCAAGGCAGGCAGATCACGAGGTCAGGATTTCAAGACCATCCTGGCCACATGG
+TGAAATTCCGTCTCTACTAAAGACACAAAAACTTAGCCGGGCGTGGTGGCGCGCGCCTGT
+AATCCCAGCTACTTGGGAGGCTGAGGCAGGAGAATCGCTTGAACTCGGGAGGTGGAGGTT
+GCAGTGAGCCAAAATCGCACCATTGCACTCCAGACTGGCCAACAGGGCGAGACTCCATCT
+CAAAAAAAAACCCAAAAAACAACAACAAAAAAAACTGTACACAGATAGATGCGCTCCTTA
+ACTTATGATAGGGTTATGTCCTGATAAACCCATAAGTTAAAAATATTGTATCTGCTGGGC
+GCGGTGGCTCACACCTGTAATTCCAGCACTTTGGGAGGCCGAGGTGGGCGGATCACGAGG
+TCAGGAGATCAAAACCATCCTGGCTAACAAGGTGAAACCCCGTCTCTACTAAAAATACAA
+AAAAAAATTAACCAGGCGTGGTGGCAGGCACCTGTAGTCCCAGCTACTCGGGAGGCTGAG
+GCAGGAGAATGGCGTGAACCTGGGAGGCGGAGCTTGCAGTGAGCCGAGACCACGCCACTG
+CACTCCAGCCTGGGTGACAAACAAGACTCCGTCTCAGAAAAAAAAAAAGAAAGAAAAGAA
+AATACTGTATGTCAAAAATGCCTTTGTGATAACCTAACCTACTGAATGTCCCATCTCAGC
+CTTGCCTCAGAATACTTACATAGTCTATAGGCAAAATAACCTATTTTATAATAAAATGTT
+GAATATCTTCTGTAATTTATTGAATACTATACCGAAAAACAATGGTTCAATAGGTACTTG
+AAGTATGGTATCTACTGCAAAAAATAACTTCTGCAACAAGGTAAAGTAGTAGAAAAAAAT
+ATATATATATTTTTTTGAAACACAGTCTCGCTCTGTCACCCAGGCTGGAGTGCAGTGGCA
+TAATCTCGGCTTACTGCAAGCTCCATCTCCCAGGTTCAAGTGATCCTCCTGCCTCAGCCT
+CCCATGTAGCTGGGATTACAGGCGTGGAACACCATGCCTGGTTATTTTTTGTATTTTAGT
+AGAGACGGGGTTTTGTCATGTTGGCCAGGCTGGTCTCGAACTCCTGGCCTCAGGCAATCC
+ACCCGCCTCGGCCTCCCAAAGTGCTGGGATTACAGGCATGAGCCACTGCGCCCGGACAGA
+AAAGTCTTCAGTTGAAACATCTGAAGCTGGGGGCCATCTGCGGTAGACTTCTGTAAATGC
+ACAAAATAAGATAATGTTAAAGCCATGTTTCTCAAAGTCCCGAGCTCCACGTAAACTGCC
+TATTATCAGAAAAAAGTTATCAATTAAAAGTCAAAGGCATAAAGAACAAACTAACACAAA
+AAAATTTTAAATACCTTTGCTGGGTCACAAGGCCGCCGGTTGATAAAGAAAAACTGTCTG
+TCTGTTGAACTCCTTCCAACTCCATGCGTGCATTGTGAAATGAAACCTGAGATGCTATTC
+AACATTAATATGGTAAGGGCAGGATTCCAGAGTGAAAGGGATTAGAAATACGATCACATG
+GCACATTCTTAAAGTGAAATGAAAACAAAACACCAGGTGACATGCTGATAAGGATCACTA
+TTGCAGTTCACGGGTATCTGTGCTCCAAATCTTGATGAGTCATCAAAGAACCAAACCTTC
+TGGAATATTCTAAAGCTCCTACAGTCAACCAATGCACCACAGGTGATGCAGTGCGTCCAA
+AACTGATGTGTTGCAGCTCTCCTTACCCTTCCTGATAAATCCTCAGCCTCTGTAAGTGGG
+TCTCGCTTCAAATGCATTCTCAGAACCTCCGTGCTGCCACCCCTGGTTTGTCAATGAAGT
+CTAACCACTTGTGCTCAGAATTTTGCCCACATTCCCTCCCCTTTCAAAACCTCCCGGGTA
+GGACGCTTATATCTCATGTCTTGGTAAAGCGCTTGCTTCACATGAGACCCACCCCAGGGA
+TACCGGCATTTCCAGAAGAACACCACCTTCACATAAAGACATAAAGCTCCATGTTTACCA
+TTTCAGGCATAAGCCAAAAGCAAGTGGAGGAAGAGTAAGAAATATAGATCTCAAGGCAAC
+AAACAAACAAACAAAAAGAAATACAGATCTTAGGCTGGGTGTGGTGGCTCATGCCTGTAA
+TTCCAGAGCCTTGAGAGGCCAAGGTGGGTGGATCACCTGAGGTCAGGAGTTCAAGACCAG
+CCTGGGCAACATGGCGAAACCCCGTCTCCACTAAAAATACAAAAAATCAGCCGGGCATGG
+TGGTGAACACCTGTAGTCCCAGCTTCTCGGAAGGCTGAGGCAGGAGTATCGCTTGAACCT
+GGGAGGCAGAGGTTGCAGGGAGGCAGAGGTTGCAGTGAGCCAAGATCACGGCACTGCACT
+GCAGCCTAGGCAACAAAGCAAGACTCCATCTCAAAGCTAAAAAAAAAAAAAATATATATA
+TATATATATATATACACACAGATAGATAGATATCTTTACAGGACCAATCCTATTTATGGA
+AGTGTCTATTTTCTTATACGAAAAGTAATGACACTGAACTGCCTTCATCAGATGCCAGGA
+AAGTCAAAATCATTTAAAATGATAAAATAATTTACAAGTTAGTCTAACTAAACAGAGCCT
+TAAAGAAGACCTGCTCAACAGAAAACCACCTGAAATATACCACTTACTCAAAACATGGTT
+TGAATTAAGCAACTGACTCCTTTGTATAAATCATCTTTCTTAGCCACAGCATTGCTCACA
+GTTTTATAAAGGACATAAAAAACTATTATCCCTAGCCAGGCGTGGTGGCTCATGCCTGTA
+ATCCCAGCACTTTGGGACACCAAGGTGGGCGGATCATCTGAGGTCAGGAGTTCGAGACCA
+GCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAATACAAAATTAGCCGGGTGTGGT
+GGCACGTGCCTGTAATCCCAGCTACTCAGGAGGCTGAGGCAGGAGAATTGCTTGAACTCA
+GGAGGTAGAGGTTGCAGTGAGCCAAGATAGCACCATTGCACTCCAGCCTGGGCAACAAAG
+CAAGACTCCGTCTCAAGAAAAAAAAAAAAAGACACGAAACTATTAGCCTTAGAATCACTA
+TCTTTAAAAAAAAAGCTCTCAGGATAAAATGTTCAATTGTAGTTCTCTTGCCAGCAATCT
+ACTTACTAAAAAAGATTATGCAGAGCATCGGAACAGCTCAAACCGTACTCTTCACACACG
+GAGTCACTAGGGGGCAGCTGAACAAAAGGAATGAGGCTTTGCAACTGAAAAAAAAAAAAA
+AAAATTCACAGTTACTTCCTAATAAAGACAGAGTGGACTTAATCTGTTTTCTTTCTTAGT
+CAAGCTATTGACATTACAAGCGCAAAAAAAATTAAAAGAATCTTTTGTTTTGTTTTGTTT
+TTTGAGACAGGGTCTCCCTCTATTGCCCAGGCTGGAGTACAATGGCTCAATCATACCTCA
+CTGCAATGTCAAACTCGTGGGTTCAAGCAATCCTCCTGCGTCAGCCTGTCGAGTGAGTAG
+CTGGGACTACAGGTGCACACCACCACACCTGGCTAATTTTTTAATTTTTTTGTAGAGATG
+GGATCTTGCCGTGTTATCCAAGCTGGTCTTAAATTCCTGGGCTCAAGCGATTCTCCCACC
+TCAAAATTGTTGGCCGGGTGGTTCAAACACATAATCCCAACAGTTTCCTCTCCCAGAGTG
+CTGGGATTACATGTGTGAGCCGTGGGAACAACAATTTTGATTTTATGATATAAGAAAGAT
+GAAACAAGTACCTACTTATTCAGAACCCACACATTGCCCACAATAACTTATATTTTTTTC
+AGAGAGAGAGTGAAAAGACGCAGTATACGAGTGTCTCTGGAAGAATAAAATGAAACACAT
+TCAGCTCTCAAACATCAATTTTTGTGATAGGTACTTTGTTTTTTTTTTTTTTTTTTTCCT
+GGGATGGTGTCTTGCTCTCTCGCCCAGGCTGCAGTGCAGTGGTGCAATCTCAGCTCACTG
+CAACCTCCATCTCCCGGGTTCCAGCGACTCTCCTGCCTCAGCCTCCTGAGTAGCTGGGAT
+TACAGGTGCCTGCCACCACGAACAGATAATTTTTGTATTTTTAGTAGAGATGGGGTTTCA
+CCATATTGATCAGGCTGGTCTCAAACTCCTGACCTCGTGATCCGCCCACCTCAGCCTCCC
+AAAGTGCTGGGATTACAGACGTGAGCCACTGCGCCGGGCCTTGTGATAGGCACTTTAAAA
+ATCAATTCTTAATCTGGGCGCAGTGGCTCACGTCTGTAATCCCAGCACTTTGGGAGGCCG
+AGGCAGGCGGATCACTAGAGGTCAGGAGTTCGAGGCCAGTCTGGCCAACAAGATGAAACC
+CCATCTCTACTAAAAATACAAAAAATTAGCTGGGCCTGGTGGCATGTGCCTGTAATCCCA
+GCTACTCAGGAGGCTAAGGTAGGAGAATTGCTTCAACGCGGGAGGCAGAGGTTGCAGTGA
+GCCAAGATGGCGCCACTGCACTCCAACCTGGGCAACAGAGCAAGACTCCAGCTCAAAAAA
+AAAAAAAACCGGCCGGGCTTGGTGGCTCACACCTGTAATCCCAGCACTTTGGGAGGCCGA
+GGCTGGTGGATCACGAGGTCAGGAATTCGAGACCAGCCTGGCCAACACGGTGAAACCCCG
+TCTCTACTAAAGATACAAAAAATTAGCCTGGCGTAGTGGAGCATGCTTGTAATCCCACTA
+CTCGGGAGGCTGAGGCAGGAGAATTGCTTGAATCTGGGAGGCGGAGGTTGCAGTGAGCCA
+AGACAACACCACTGCACTCCAGCCTGGGCAGCAGTGCGAGACTCCCTCTCAAAAAAAAAA
+AAAAAATCAATTCTAAGATTTTATTCTCCATTCTACTGGAAGGGACAATGGAAACCCGCT
+ATAATCACTAGAGCAATAAGAGGCGTTGAAGTAACCGGCCATCACTACCTGCTTCTGCCC
+AAACACAGAGCCGATATTTTCCTTTATGCTGGGGCTTCCACCTGTGCATACCACAGGCTG
+TCGTTTTCCTTGTCCAAGCTGATTGGTGCAACTTACACGGATGCCTGCTGAAATGATACA
+GTATGCATGTAAGACCTGGACCATTTTGGCATACTCCTGTTTAAAAAACACAAACACAAT
+ATTCTACATTACTTTAATATTATAGGAATTACACAGCTCAAGTTACAACATCCAACGCAA
+GGTTCTCACATCATCGCACAAATCAAGGGAAGCACTGTTGACAGAATGATCTGTAAAGAG
+GTGTCTTCCTATATTCTACAGAAAGGAACGCAGAGCTTTTGGCTCCTGGTCACAGTCCTC
+TCACTTCCCAATGTGCCATGCATCCTGGTAAAACAACTAAAAAGTACAGCCTGTAATCCC
+AGCTACTCAGGAGGCTGAGGGCAGGAGGATCACTTGAGACCAGGAGTTCAAGACCAGCCT
+GGGCAACACAGCAAGACCCTGTCTCTACAAAAAATTTAAAAAAAAAATTAGCCGGGCGTC
+ATGGCATGTGCCTGTAGTCACAGCTACTGAGGAGGCTGAGGTGGGAGGATCGCTTGAGCC
+TAGGAGTTCAAGGCTGCAGTGAGCCATGATTGCACCACTGCACTCCAGCCTCGGTGACAG
+AGTGAGGCCCTATCTCTAAAAATGAAAATTAAAAAACTGAAACGTACATTGTGTTTGATT
+TTATAATCTCTCCTTTTGAAATGTATCTTCGTATAATAGAAACACTGGCACAAGCATTTT
+GGTATGCAAAGAGATACACAAAAATGTTCACTGAAACAATCTCTATGAACAAACAGAAAC
+AACCTAAGCAAGCATCATTGAGGAGTTGATTAATTATGGTATAGCCATAGCGCAGCAGAA
+TGACAACAAATAAGGCAGTGTGCACCGACTAAAAAAGACAATCACAATATGCTAAGTAAA
+AAGTCAGTTATAGGGCCAGGCATGATGGTTCACACCTGTAATCCCAGCACTTTGGGAGGC
+TGAGGCGGGAGGATCACTTGAGCCCACGAGTTCGAGACCTGCCTGGGCAACACAGAAGGA
+CCCATCTCTACAAAAAAAACAAAAATTAGCCGGGCATGGTAGCACGGGCCTGGAGTCCCA
+GCTACTTGGGAGGCTGAAGTGGGAAGATTCATTGAGCCTGGGAGATCATGGCTGCGGTAA
+GCTGAGATTGTGCCACTACATCCCAGCCTAGGTGAGAGAGCAAGACCCTGTCTCAATTAA
+AAAAAAAAAAAAAAAAAAAATACAACTTTCAACCACATACAATTCTGTATTACTTGCATG
+TTGTACATTCTATATTACTTGCTTTCATTATATTAACTTATGAATTTATCTTGAAAATTA
+TTCCAACAGTTATAAACACATGAAATTAAAAGCAGCCTGAAAAGATATACAAACTGTAAA
+TAACAGTTATCTCTGACAAATAGAAGTTCTACATTCCTGTATTCTGCTAAGGCACTAATT
+TTTTTACCATAAGATACAAAAAAAGAGTAAGTTTTCTCTACTTTAGAAAATTTAAATTTG
+TGAAAAAATGTAATAAAGTTAAAATTAGCAGCCAAGTGCAGTGGCTCACACCTGTAATCC
+CAGCACTTTGGGAGGCTGAGGCAGGTGGATCACTTGAGGTCAGGGGTGCAAGACCAGGCT
+AGCCAACATGGTGAAACTCCATCTCTACTAAAAATACAAAAATTAGCTGGGCGTGGTGGC
+GCACACCTATAATCCCAGCTACTCGAGAGGCTGAGGCAGGAGAATCACTTGAACCCAGGA
+GGTGGAGGTTGCAGTGAGCCGAGATCGCACCACTGCACTCCAGCCTGGGCGACAGAGTGA
+GAAGACTCCATCTAAAAAAAAAGAAAGTTAAAATTAGCACCAAATGCTTTACAAGTAAAA
+AAAGTTTTTAGCTGCATATGTTTAAGTAACTTTTTAGATTATGAAAAACACACATACAAA
+ATGGGAAGGCACAAAGAAGACAGCAAAAACTGCATGAGATCTCACATCCAAGGATAACTG
+CTGAGAACATGAAAGTGCCGAGTCTTCCAGCCTTTATACTATACACATTTAGGCTTGTTG
+TTTTGTTTTCACAAAATTGTAATCAAATAATACAGACAGTTCTATAATCTGCTTTTTAAA
+CACAACGACTATATAACATTTAGCTATTTTCATTTGCATTCAAATTCATAAGGGTTCTAA
+TAGCTCATTTCTCAGAAAACCAAGAGAAATATTCTTTTTTTTTTTTTTTTGAGATGGGGT
+CTGGCTCTGTGCCCAGGCTGGAGTGCAATAGCTTGATCTCGGCTCACCGCAACCTCTGCC
+TCCCGGATTCCAGCGATTCTCCTGCCTCAGCCTCCCAAGGAGCTGGGACTACAGGCACAT
+GCCACCATGCCCAGCTAATTTTTGTATTTTTAGTAGAGATGGGGTTTCACCAGTTTGGCC
+AGGATGGCTTTGATCTCTTGACCTCGTGATCCACCCGCCTCAGCCTCCCAAAGTGCTGGG
+ATTACAGGTGTGAGCCACTGTGCCTGGCCGAGAAATATTCTTATTAAAATATAAGTACAT
+AAGGCCAGGCATGGTGGCTCAGGCCTGTAATCCCAGCACTTTGAGAGGCCAAGGTGGGCA
+GATCACCTGAGGTCAGGAATTCGAGACCAGCCTGGCCAGCCTGGACAACATGGTGAAACC
+CCGTCTCTACTAAAAATACAAAAATTAGCCAGCTGTGGTGGTACACGCCTGTAATTGCAG
+CTACTCAGAAGGCTGAGGCAGGAGAATCGCTTGAACTCAGGAGGTGGAGGTTGCAGTGAA
+CCAAGATCGCGCCACCGCACTCCAGCCAGGGCGCCAAAGAGAAACTCCATCTCAAAAAAA
+GATAAAAATAAAAAATAAAAAATATATATATATGTATATATATTTTTCCAGACAGGATCT
+TATTCTGTCTCCCAGTCTTAAGTGCAGTGGCGCAATCATAGCTCACTGCAGCCTCAAGTT
+CCTGGGCTCAAGTGATCCTCCCACTTCAGCCTCCCAAGTAGCTGGAACTACAGGTACATG
+TCACCATGCCCAGTAAATTTTTTTTTAAAATTTTTCATAGAGACAGGGTCTCACTGTGTT
+GCCCAGTCCTAATAAACACTATGTGATGAAAAGAAAAAAGTAAATCATCCTAAAGTTAAG
+TCTTTAATGTTAAATCTTTAATGAGAAATGCAAATAAAGCATTTCTCAATAATTTATGGG
+AAGAGAATCAACTGAAGAATAAACATCTTTAGTAAATCTTTTGCTCATGTGCATTAACCA
+ATACTCTTGAAAACCAGGATTAATTTACTGTACCTTCTTAATATTCCTTTGAAATTCCTT
+ATGGCGCACAGGTAGTGTGGAAAATAACTGCTGCACGCTGACTGTGGTCCCTCTGGGGCG
+GGGGTAGGGGGTTTTCTGGATAATTTTCCCATTGTGATCAAACATCAGTCGAGTTCCAAC
+CTTCGCCGATGCGTGGCAGGTAGAAATGGTGACATCGCTGTGAGAGAATACCAGGCATGG
+TGTGTTCAGTGAGAGACCCATGATGTTGGGCACTGACTACTCTTTTCTTCACTTGCTTTT
+CTCTCAAAATTTTCTTAAAAAGCTGACGATCCCTCTGAGATAATCAAGATCTAAATGGTT
+GAGGAGTCATCATAAAATCTAAGGTTTGGCATCTAAAAGACAGTGAGACAGAGAGCACTA
+AACATGCTTTGCTTTGATAAAAGCTTTGATTTCGTTTTTCAGGTTGAACTGCAAAACCAT
+AAATGATCTTAAGATTTATTTATTCACAAACACAGATTTGTTTTGTTATTACTCTTCGAA
+CAAATTTTTTTTAAAGAATCTAACAAATATTATAATTAAAATGTATATGTAGGGCAGAGC
+GTGGTGGCTCATGCCTGTTATCCCAGCACTTTGGGAGGCCAAGGCAGGCAGATCACTTGA
+GGCCAGGAGTTTGAGACCAGCCTAGGCAACATGGTGAAATCCCATCTCTACTAAAAATAC
+AAAAATTAGCCAGGAGTGGTGGTGCATGCCTATAGTACCAGCTCCTCAGGAGGCTCAGGC
+ACGAGAATCACTTGAACCTGGAAGGCAGAGATTGCAGTGAGCCGAGACTGTGCCACTGCA
+CTCCAGCCTGGGTGACAAAGAGAGACTCTGTCTAAAAAAAAAAAAAGATATATATATATA
+TATATAATTATTTATAAAAATTTCATATCTGTGCTATAATTAAATAGTGCTTTGGTGAAA
+TGTTTCCCTAAAAATTGATAATGAAAACCAATGGTAACTATCATTTATTATCTACATGTT
+AGGTTAAAATTGAGAATTACTGTTTTAATAAGGGTAACCATCTTTTTAACAATACTATTT
+GCTTCATTTCATTCATTTATTGCTCACATTTCAGAAGTACTATGACTTAGATTGGCAGCG
+AGACAAAACAGAATTCAGAAGCTAGAAGTTGAGATGTTGAGATAGAAAACTGAAAATAAT
+AATGATTCCAATTAATTTTCAGAGAGGTTTCTCTAAGGGGTCAAGTGAGTGGATAAAAAT
+ATTGTATCACCTCAGTGCACAAAGTGAGCTCAGAGCTTCCCCCCGAAAGCCAAAAGTTTC
+AACCTGAGTTAGGTCGGCAAACTCTTGAATCTTAGATGTGTGATGTTTCAGAGCTGAAAG
+AGAGTGTAAAGTAAGGACTAAGATATCTCAAGTGCTATAACAACAAAATATACATGATAT
+CTAGTAACTGGCTTTAAAAAACTGTTTTTGCATTTCCCAAGACAGTGTTACTCAAAATTC
+TGAGACATGTGACCCAATTATTTTATAATAGGATTAGAAAAAGTCAACTTACTTAAGCCT
+TCGAAGTTTTCTTCTTCTACCCCACATCCATTGTCTGAAACTTCAATAAGATCCACTCCA
+TAGTCCTTAAGCTTTAGATCTAGAAAGTTTAAAATATTTACATATTTATTAAAAACGGAC
+CCATGCTATCAGTTTTTATATTGACATTATTTATAACATATGCAAATTTAAGAGTCATAA
+CTATACCTTTAGTTAAACATACTAGTGTCATTTTGTATATTTCATTGTTATAAAGTCCTT
+TCTGGCTATTTACTAGCCCAGACTAAATAGTTTAGCTTTTTCTTTCTTTCCTCTTTTTTT
+TTCCCTAGGCTAGTGAAGTGAAGCAGTTGGAGTGGAGAAGGAACAAAAAAAATCTGTAAC
+TGGTGGTGATCAATTAGCTGTAAACCGCGTTGCACTTTGACCATCCTTTTCTTTTGAAAG
+AAATAATTTTAACATACCCAATAAAGAGAACGGGGACCGGGTGCAGTGGTTCATGCCTGT
+AATTCCAGCACTTTGGGAGGCCAAAGCGAGCAGATCACCTGAGGTCAGGAGTTCGAGACC
+AGCCTGACCAACATGGAGAAACCCTGTCTCTACTAAAAATACAAAATTAGCCAGGCTTGG
+TGGCGCATGCCTGTCATCCCAGCTACTCAGGAAGCTGAGGCAGGAGAATCACTTGAACCC
+AGGAGGTGGAGGTTGCAGTGAGCCGAGATCGTGCCATTGCACTATAGCCTGGGCAACAAG
+AGCAAAACTCTATCTCAAAAAAAAAAAAAAAAAGAGAATGGGTTCTGGAATCAGACTTCC
+TGGATCCTATTTTATCAGCTTTATAATCTCAAAAAAAGGAAATTTCCTATCCCCTAATTT
+CCTCATTTGTAAAATAGAGAATAATAAGTTCTATCTCATAAAGTTATTCTGCAGATTAAT
+AATTCTTTGGTTTTTTTTATTTTATTATTCTTTTCTTTTCTTTTGAGATGGAGTTTTGCT
+CGTCACCCAGGCTGGAGTGCAGTGGTACGATCTTGGCTCACTGCAGCCTCCACCTCCCAG
+GTTCAAGCAATTCTCCTCCTTCAGCGTCCTGAGGAGCTGAGATTACAGCCATGCACCACC
+ACATCTGGCTAATTTTTGTATTTTTAGTAGAGACAGGGTTTCATCATGTTGGTTAGGCTG
+GTCTAGAACTCCTGACCTCAAATGATCAGCCCCCCTCAGCCTCCCAAAGTGCTGGTATTA
+CAGATGTGAGCCACTACTCCAGCCCTATTTTGTTTTATGTTTTTGAGATGGAATCTTGCT
+CTGTCCCCAGGCTGGCATGCAGTGGCACGATCTCGGCTTACTGCAACCTCCGTCTCTCGG
+CTTCAAGCAATTCTCGTGCCTCAGTGTCCCAAGTAGCTGGGATTACAGGCTTCTGCCACC
+AGGTCCAGCTAATTTTTGTATTTTTAGTAGAGACAGAGTTTCACCACTTTGGACAGGCTG
+GTCTCGAACTCCTGACCTCAGGTATCCACCCGCCTTGGCCTCCCAAAGTGCTGGGATTAC
+AGGCGTGAGCCACTATGCCTGGCCTACTTTATTTTTCAATAGAGACAAGGTCTCACCATG
+TTGGCCAGGTTGGTCTTGAACTCTTGGCCTCAAGCAATTCCCCCACCTCGGCCTCTCAAA
+GGGCTAGGATTATAGGCGTGAGACACCACGCCCAGCTGTTCTGCAAATTAAATATTTCTG
+TGCAATTCTTAGCATAACACCTGCCTGGCACACCGTAAGAACACAATAAAAGCTGTTATT
+ATTATTACTACCTAGCTAAGTACTAGGCACATAATAGGTGCTAACTTCAACTTAAAAATA
+ATAATTTATTACTACATCAACACTTGATAGTCTTATTTCAATAACAAATGTTTCTTAACT
+ACAACAACATTCACAGATCATTTCTTGTGGCTTAAAACTCTCCCAAACTTACCAATATTA
+GTGGCACCAGCATCCAGACTGTTTTCTACTAACTCCTTTACCGCAGTGCTTAGACTCAGT
+ACCACCTGCCCAGAGCAAATCTGATGGACTGACTTCCGATCAATAGGTTTGATGGCCTTA
+GCAGGTTCTGTACTAGAGAAATCAGTTACAAGAAACAAATCAAGTATTCAGCTATATATT
+TTCATCCTGATTTTAACTGTGGGAAATGACTCAACACTGTAAATAATTTATGGGTCTAAT
+CTATTCATTTATTATATTAGCAAATACATTTATTATATCCAGAAATAGAAACACTGTTTT
+ACAATCCTTAAACATGTACCCAAAATACTTCTGGATAGATACTTCAAATTCAACAGATCC
+TTACTATCTAATTATACTAAGATCCACATGGAGAAAACATACATTGTATCTCTCAAATTA
+CCAAAATCTTTGGCAACAATGGTGTCTTCTTTCTTGAAAAGTGAAAGCATGGCTGGCTGT
+GGTGGCTCATGCCTGTAATCCCAGCACTTTGGGAAGCAGAGATGGGTGGATAACTTGAGG
+TCAGGAGTTCGACACCAGCCTGGCCAACACGGTGAAACCCCGTCTTTACTAAAAATACAA
+AAAATTAGCCAGGCATGGTGGTGGGCACCTGTAATCCTAGCTACTCAGGAGGCTGAGGCA
+GGAGAATCGCTTAAATCCAGGAGGCGGAGGTTGCAGTGAGCTGAGATTGCGGCATTGCAC
+TCCAGCCTGGGCAACGAGCAAAAAAAAAAATGAAAGTAACATAATTTCCCAACATAATTA
+GAAAAACCAACAGTATGCTGGGAAATACACAATGTTTAAGTCAAAATCATCTCAGAAATT
+GGGTACCAGTTATATAACTATTCCTTATACACAGTTGCCTTTGATACCCCACTCCAAACT
+GAAGCTGCCAGCTGCTGTCTTAGCAAAGACCCTCAAAGCTCTTGCTGTACTAGCTTTAAG
+AGTTTTATAAAGGTTTTATCTCCCCTTATTCCCTGCTCCAATACATCCTCCACTCTATCA
+CCAGAGCTATTTTTGAAATCACAAATCTGGTCAAATAATTTTTCTGCTTAAAAATTTACT
+AGTGCCCCACTTCCTACTATATGAAAGTTAAAATTTAGTCATCATTGGGGCCAAAACTAC
+CTTCTTTTCAGAATCTCTCTAATCCTTTCCCTTCATCAAGTCCCCTACATTATTATTATT
+ATTATTATTATTATTGTTATTATTGTTATTATTTGAGACAGAGTCTCACCCCGTTGCCTA
+TGCTAGAGGGCAATGGCATGAGCTCAGCTCACTGCAACCTCCGCCTCCCAGGTTCAAGCG
+ATTCTCCTATCTCAGCCTCCCAAGTAGCTGGGATTACAGGCGCCCACCATCACACCCAGC
+TAATTTTTGTGTTTTTAGAAGAGATAGGGTTTCACCATGTTGGCCAGGCTGGTCTCGAAC
+TCCTGACCTCAGGTGATCCGCCTGCCTCGGCCTCCCAAAGTGCTAGGATTACAGGGGACC
+GCAACCAGCCATCCCCTATATTGTAGCACAGTGAACAACTGTCCTGAACATCACAAGCTC
+TTTGAGACACTACAGTGTATAAGCAGGTCTCTGTCTAAACCGCTCTCCTCTTCCTCCTCT
+GCCCAAACAATGTCTGCTCAAAGAATGTATCCCGTGTGTTCATTAACTTAGCAATTTCCA
+GCAAACAGTTTAATTGATAACTTGTTAAGAGAAGGCAGGAAACCTCCATGAAAGAGAAAT
+CACTGGGTATTTCCTACAGCATTTAACACATCGTAGGCCTTTAATAAACCCTTCTGAAAT
+AAACAAACCTCTTTACTCTTCATTCCACCTTGCTAAGAATCTCACCTAAGTCTGTCTACC
+ATGTGAAACTGCAGATGACCTCACAGAAAATGGAAAGAAGTATCTCTAAAAATAAGTTTA
+TTTGGCAGCACACTATAGGCTACAGGTCCACTTCTGATTTTTTTTTTTTTTTTTTTTTGA
+GACCGAGTCTTGCTGCGTTGCCCAGGCCGGACTGCAGTGGCACGATCTCAGCTCACTGCA
+ACCTCCGCCTCCTGGGTTCCAGCGATTCTCCTGCCTCAGCCTCCAAAGTAGCTAGGATTA
+CAGGCTCCCGCCATCATGCCCAGTTAATTTTTGTATTTTTAGTAGAAACGGATTTCACCA
+TGTTGGCCAGGCTGGTCATGAACTCCTGACTTCATGATCCACCCGCCTTGGCCTCCCAAA
+GTGCTGGGATTATAGGCGTGAGTCACCGCTCTCGGCCCACTTCAGATATTTATTTTGAGG
+AGGGAGCGCATTTAGACACAGACCCCAAATTTATTTAAATGTCTCAATACATTTAAATGT
+AGTTACCTAAATATATCTAATATATTTAAATGCAGAGAGCAAATTTGCGTTTACAAATCT
+GACATGGAATGCAAATGTGCTAGCCAAGATTCGGTGTAGCTTACCAGCCAGAAATCACAC
+ATCCTAACAGGTAGAAACGTATTGCATTTTTAAAAACTGCGCAGCTATGCAAATAAGGAT
+GTGTCTGGACGCTCTACCGTCCCCAAAATAACCTTAATTTTTTAAAAAGGCCAGGCACGG
+TGCATCATGCCTTTAATTCCAGCACTTTGAGGGGCCAAGGCGGGCGGATTGCTTGAGCTC
+AGGCGTTCGAGACCAGCCTGGGCAACGCAGCGAAATCCCCGTCTCTACAAAAAAAAATTA
+AAAATAAAATACTATAAAAATAAAAATAAAAGGGGAGAGAGAACAGGTAGAAAGGAAATG
+CATTCAGTCTATGGGGATTTCACGCTCCCGCTTCAAGTCCACGGCCCTGTGATGGGATGT
+GGGCAAGGCCTGTCTGGGACAGGCCGAACCCAACTCCTCACAGGGCCGAATCCTTTGCCC
+GCAGCCCAGGACCCCGAAGGAGCTTGCCTCGGCCTCAAGGCGCACCCAAGGGGCACGAGA
+TCGCTGCAACACTGAGGTCGCCACTCCGGGGCCTCCAGGGGGCTGCCTCGCCACGCGCCT
+CGGCCATGTTCCCCCCATTTCCAGGGAGGTTGGAATGCCGTGGGTCTCAAAGAGGGCGCG
+CGAGAGGGGACACCGGAAGACTGCGAGCCCCGCTCACCTCGAGCTCTCAGCTCGCTCCAT
+GGATGCAACACCCGATCCGCCTCGGGGACTGGGAAAGTTCCCTCCAGGGCTCCCACAGGC
+GCTCCGCCTCCTGAACTCCCATTGGCTGCTTTCGACGTTGTGCTCCACCCTTTCCGGGCG
+GGGCGGCAAAAATACTTCCCGTCTCTCCTTTTCGCCTATTGGCTCTGTCAAAGGTCGACT
+TCGTGACGTCAAAGAGCCTGGGCCAATCAGAGCACACCGGACTGCGTTTTCCCGAACGCC
+CGCAGCAGGGTCAGAAGGGAGGTGGCCGGTCTCCGTCGTGACCTCTGACGGTTTCTGAGC
+GTTGGCCTTTGGCACGCGCTACCCCCTTTTGCTTTGGTTCTGCCATGCCGATGTACCAGG
+TAAAGCCCTATCACGGGGGCGGCGCGCCTCTCCGTGTGGAGCTTCCCACCTGCATGTACC
+GGCTCCCCAACGTGCACGGCAGGAGCTACGGCCCAGCGCCGGGCGCTGGCCACGTGCAGG
+TAGGAGCGCGGGGCCCCCCGCCCAGTGCGCACGCGCGGCGACCGGCTGCTGGCCCGGGTC
+CCCCCAGGCCGGAGCGAGCGCGTCCCAACCGGTTCACGGCCCCACCCCGGCATCTGTGCC
+GGCCGGCCAGGGACTCACTCAGACTTTTATGTTTTAAAAGATTTATCCAGGCCGGGCGCC
+GTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGATCACCTGAGGT
+CAGGAGTTCGAGACTAGCCTGGCCAACATGGTAAAACCTCGTCTCTACTAAAAATACAGA
+AATTGGCCGGGTGTGGTGAGGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAG
+AATCGTTTGAACCCTGGAGGCGGAGTTTGCAGTGAGCTGAGATCGAGCCATTGCACTCGA
+GCCTGGGCAACAAGAGCTAAACTCTATCTCAAAAAAAAAAAAAAAAAAAAAAAAAATATA
+TATATATATATATGTATGTAT
```

### Comparing `paraphase-2.0.0/paraphase/data/rccx/rccx_config.yaml` & `paraphase-2.1.0/paraphase/data/rccx/rccx_config.yaml`

 * *Files 22% similar despite different names*

```diff
@@ -18,16 +18,14 @@
 
     clip_3p_positions: [32046127]
     clip_5p_positions: [32013270]
     
     deletion1_size: 6367
     deletion2_size: 120
 
-    noisy_region: [[32029159, 32029159], [32022483, 32022483]]
-
     left_boundary: 32013300
     right_boundary: 32046000
 
     # 120bp sv
     del2_3p_pos1: 32043700
     del2_3p_pos2: 32043723
     del2_5p_pos1: 32043828
```

### Comparing `paraphase-2.0.0/paraphase/data/rccx/rccx_homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/rccx/rccx_homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/rccx/rccx_ref.fa` & `paraphase-2.1.0/paraphase/data/rccx/rccx_ref.fa`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/smn1/homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/smn1/homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/smn1/known_haplotypes.json` & `paraphase-2.1.0/paraphase/data/smn1/known_haplotypes.json`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/smn1/ref.fa` & `paraphase-2.1.0/paraphase/data/smn1/ref.fa`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/smn1/ref_smn2.fa` & `paraphase-2.1.0/paraphase/data/smn1/ref_smn2.fa`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/smn1/smn1_config.yaml` & `paraphase-2.1.0/paraphase/data/smn1/smn1_config.yaml`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/smn1/smn_matching_pos.txt` & `paraphase-2.1.0/paraphase/data/smn1/smn_matching_pos.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/strc/homopolymer_sites.txt` & `paraphase-2.1.0/paraphase/data/strc/homopolymer_sites.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/data/strc/strc_config.yaml` & `paraphase-2.1.0/paraphase/data/strc/strc_config.yaml`

 * *Files 10% similar despite different names*

```diff
@@ -15,14 +15,16 @@
     extract_region1: "chr15:43599000-43620000"
     extract_region2: "chr15:43698814-43719466"
     
     noisy_region: [[43602500, 43603700], [43602165, 43602176]]
 
     depth_region: [[43610000, 43660000]]
 
+    pivot_site: 43602487
+
     left_boundary: 43599500
     right_boundary: 43619600
 
     # deletion in pseudogene
     deletion1_size: 314
     del1_3p_pos1: 43602628
     del1_3p_pos2: 43602631
```

### Comparing `paraphase-2.0.0/paraphase/genes/cfc1_phaser.py` & `paraphase-2.1.0/paraphase/genes/cfc1_phaser.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,21 +20,18 @@
         Phaser.__init__(self, sample_id, outdir, wgs_depth)
 
     def call(self):
         if self.check_coverage_before_analysis() is False:
             return None
         self.get_homopolymer()
         self.get_candidate_pos()
-        # add pivot site
-        if "130593061_A_G" not in self.candidate_pos:
-            self.candidate_pos.add("130593061_A_G")
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
 
-        raw_read_haps = self.get_haplotypes_from_reads(self.het_sites)
+        raw_read_haps = self.get_haplotypes_from_reads(add_sites=["130593061_A_G"])
 
         (
             ass_haps,
             original_haps,
             hcn,
             uniquely_supporting_reads,
             nonuniquely_supporting_reads,
```

### Comparing `paraphase-2.0.0/paraphase/genes/f8_phaser.py` & `paraphase-2.1.0/paraphase/genes/f8_phaser.py`

 * *Files 2% similar despite different names*

```diff
@@ -92,15 +92,17 @@
                 break
         if var_found is False:
             self.candidate_pos.add("155386860_C_G")
 
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
 
-        raw_read_haps = self.get_haplotypes_from_reads(self.het_sites, check_clip=True)
+        raw_read_haps = self.get_haplotypes_from_reads(
+            check_clip=True, kept_sites=["155386300_A_C", "155386860_C_G"]
+        )
 
         (
             ass_haps,
             original_haps,
             hcn,
             uniquely_supporting_reads,
             nonuniquely_supporting_reads,
```

### Comparing `paraphase-2.0.0/paraphase/genes/ikbkg_phaser.py` & `paraphase-2.1.0/paraphase/genes/ikbkg_phaser.py`

 * *Files 5% similar despite different names*

```diff
@@ -42,14 +42,15 @@
             self.del1_5p_pos1,
             self.del1_5p_pos2,
             self.deletion1_size,
         )
 
         self.get_candidate_pos(min_vaf=0.095)
 
+        # add these sites for duplication/deletion calling
         var_found = False
         for var in self.candidate_pos:
             pos = int(var.split("_")[0])
             if pos > self.clip_3p_positions[0]:
                 var_found = True
                 break
         if var_found is False:
@@ -64,17 +65,18 @@
         if var_found is False:
             self.candidate_pos.add("154555882_C_G")
 
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
 
         raw_read_haps = self.get_haplotypes_from_reads(
-            self.het_sites,
             check_clip=True,
             partial_deletion_reads=self.del1_reads_partial,
+            kept_sites=["154569800_T_G"],
+            add_sites=["154555882_C_G"],
         )
         het_sites = self.het_sites
         if self.del1_reads_partial != set():
             raw_read_haps, het_sites = self.update_reads_for_deletions(
                 raw_read_haps,
                 het_sites,
                 self.del1_3p_pos1,
@@ -97,33 +99,34 @@
 
         total_cn = len(ass_haps)
         tmp = {}
         gene_counter = 0
         pseudo_counter = 0
         dup_counter = 0
         deletion_haplotypes = []
-        for i, hap in enumerate(ass_haps):
-            nsite = min(len(hap), 10)
-            start_seq = hap[:nsite]
-            if start_seq.startswith("0") is False:
-                if start_seq.count("1") >= start_seq.count("2"):
-                    gene_counter += 1
-                    hap_name = f"ikbkg_hap{gene_counter}"
-                    tmp.setdefault(hap, hap_name)
-                    if "3" in hap:
-                        deletion_haplotypes.append(hap_name)
+        pivot_index, index_found = self.get_pivot_site_index()
+        if index_found is True:
+            for i, hap in enumerate(ass_haps):
+                start_seq = hap[: pivot_index + 1]
+                if start_seq.startswith("0") is False:
+                    if start_seq.count("1") >= start_seq.count("2"):
+                        gene_counter += 1
+                        hap_name = f"ikbkg_hap{gene_counter}"
+                        tmp.setdefault(hap, hap_name)
+                        if "3" in hap:
+                            deletion_haplotypes.append(hap_name)
+                    else:
+                        pseudo_counter += 1
+                        hap_name = f"pseudo_hap{pseudo_counter}"
+                        tmp.setdefault(hap, hap_name)
+                        if "3" in hap:
+                            deletion_haplotypes.append(hap_name)
                 else:
-                    pseudo_counter += 1
-                    hap_name = f"pseudo_hap{pseudo_counter}"
-                    tmp.setdefault(hap, hap_name)
-                    if "3" in hap:
-                        deletion_haplotypes.append(hap_name)
-            else:
-                dup_counter += 1
-                tmp.setdefault(hap, f"dup_hap{dup_counter}")
+                    dup_counter += 1
+                    tmp.setdefault(hap, f"dup_hap{dup_counter}")
         ass_haps = tmp
 
         haplotypes = None
         dvar = None
         if self.het_sites != []:
             haplotypes, dvar = self.output_variants_in_haplotypes(
                 ass_haps,
@@ -157,14 +160,22 @@
         new_alleles = []
         for allele in alleles:
             new_allele = []
             for hap in allele:
                 new_allele.append(ass_haps[hap])
             new_alleles.append(new_allele)
 
+        if gene_counter == 0 or pseudo_counter == 0:
+            total_cn = None
+            gene_counter = None
+        # homozygous case
+        if total_cn == 0:
+            total_cn = None
+            gene_counter = None
+
         self.close_handle()
 
         return self.GeneCall(
             total_cn,
             gene_counter,
             ass_haps,
             deletion_haplotypes,
```

### Comparing `paraphase-2.0.0/paraphase/genes/ncf1_phaser.py` & `paraphase-2.1.0/paraphase/genes/ncf1_phaser.py`

 * *Files 3% similar despite different names*

```diff
@@ -23,31 +23,28 @@
         super().set_parameter(config)
 
     def call(self):
         if self.check_coverage_before_analysis() is False:
             return None
         pivot_site = self.pivot_site
         for pileupcolumn in self._bamh.pileup(
-            self.nchr, pivot_site - 1, pivot_site, truncate=True
+            self.nchr, pivot_site, pivot_site + 1, truncate=True
         ):
             bases = [
                 a.upper() for a in pileupcolumn.get_query_sequences(add_indels=True)
             ]
         gene_reads = bases.count("G")
         pseudo_reads = bases.count("G-2NN")
 
         self.get_homopolymer()
         self.get_candidate_pos()
-        # add pivot site
-        if "74777266_G_A" not in self.candidate_pos:
-            self.candidate_pos.add("74777266_G_A")
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
 
-        raw_read_haps = self.get_haplotypes_from_reads(self.het_sites)
+        raw_read_haps = self.get_haplotypes_from_reads(add_sites=["74777265_A_T"])
 
         (
             ass_haps,
             original_haps,
             hcn,
             uniquely_supporting_reads,
             nonuniquely_supporting_reads,
@@ -111,14 +108,18 @@
                 counter_gene = None
                 total_cn = None
         # scenario where only three haplotypes are found, possibly each at CN2
         if counter_gene == 1 and counter_pseudo == 2 and total_cn == 3:
             counter_gene = None
             total_cn = None
 
+        # homozygous case
+        if total_cn == 0:
+            total_cn = None
+
         self.close_handle()
 
         return self.GeneCall(
             total_cn,
             counter_gene,
             ass_haps,
             two_cp_haps,
```

### Comparing `paraphase-2.0.0/paraphase/genes/neb_phaser.py` & `paraphase-2.1.0/paraphase/genes/neb_phaser.py`

 * *Files 1% similar despite different names*

```diff
@@ -27,15 +27,15 @@
         if self.check_coverage_before_analysis() is False:
             return None
         self.get_homopolymer()
         self.get_candidate_pos()
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
 
-        raw_read_haps = self.get_haplotypes_from_reads(self.het_sites)
+        raw_read_haps = self.get_haplotypes_from_reads()
 
         (
             ass_haps,
             original_haps,
             hcn,
             uniquely_supporting_reads,
             nonuniquely_supporting_reads,
@@ -123,14 +123,18 @@
         ):
             new_alleles = []
             total_cn = None
         elif len(tri1) > 2 or len(tri3) > 2:
             total_cn = None
             new_alleles = []
 
+        # homozygous case
+        if total_cn == 0:
+            total_cn = None
+
         self.close_handle()
 
         return self.GeneCall(
             total_cn,
             ass_haps,
             two_cp_haps,
             alleles,
```

### Comparing `paraphase-2.0.0/paraphase/genes/pms2_phaser.py` & `paraphase-2.1.0/paraphase/genes/pms2_phaser.py`

 * *Files 6% similar despite different names*

```diff
@@ -23,17 +23,17 @@
         if self.check_coverage_before_analysis() is False:
             return None
         self.get_homopolymer()
         self.get_candidate_pos()
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
         # for distinguishing pms2 from pms2cl
-        self.het_sites.append("5989137_G_A")
-
-        raw_read_haps = self.get_haplotypes_from_reads(self.het_sites, check_clip=True)
+        raw_read_haps = self.get_haplotypes_from_reads(
+            check_clip=True, add_sites=["5989137_G_A"]
+        )
 
         (
             ass_haps,
             original_haps,
             hcn,
             uniquely_supporting_reads,
             nonuniquely_supporting_reads,
@@ -73,14 +73,19 @@
         total_cn = len(ass_haps) + len(two_cp_haps)
         pms2_cn = len([a for a in ass_haps.values() if "cl" not in a]) + len(
             [a for a in two_cp_haps if "cl" not in a]
         )
         # bigger cnvs are not handled here yet
         if pms2_cn != 2:
             pms2_cn = None
+
+        # homozygous case
+        if total_cn == 0:
+            total_cn = None
+
         self.close_handle()
 
         return self.GeneCall(
             total_cn,
             pms2_cn,
             ass_haps,
             two_cp_haps,
```

### Comparing `paraphase-2.0.0/paraphase/genes/rccx_phaser.py` & `paraphase-2.1.0/paraphase/genes/rccx_phaser.py`

 * *Files 0% similar despite different names*

```diff
@@ -239,15 +239,15 @@
             tmp = sorted(allele_var, key=lambda x: len(x))
             if tmp[0] == []:
                 if tmp[1] == []:
                     annotated_allele = "gene_duplication"
                 elif abs(len(tmp[1]) - len(tmp[2])) <= 1 and len(tmp[2]) >= 6:
                     annotated_allele = "pseudogene_duplication"
                 else:
-                    annotated_allele = "duplicaton_WT_plus_" + ",".join(tmp[1])
+                    annotated_allele = "duplication_WT_plus_" + ",".join(tmp[1])
             else:
                 if abs(len(tmp[1]) - len(tmp[2])) <= 1 and len(tmp[2]) >= 6:
                     annotated_allele = ",".join(tmp[0]) + "_pseudogene_duplication"
                 else:
                     annotated_allele = (
                         "duplication_" + ",".join(tmp[0]) + "_plus_" + ",".join(tmp[1])
                     )
@@ -363,15 +363,15 @@
                             new_alleles = [
                                 [starting_copies[0], ending_copies[0]],
                                 [starting_copies[0], ending_copies[1]],
                             ]
                             successful_phasing = True
 
             # add missing links when there is no two-cp haplotypes
-            if two_cp_haplotypes == []:
+            if two_cp_haplotypes == [] and len(ending_copies) <= 2:
                 # add the missing link in cn=4
                 if (
                     len(final_haps) in [3, 4]
                     and len(new_alleles) == 1
                     and len(new_alleles[0]) == 2
                 ):
                     remaining_hap = [
@@ -505,19 +505,22 @@
                 var_found = True
                 break
         if var_found is False and self.candidate_pos != set():
             self.candidate_pos.add("32013265_A_T")
 
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
-        het_sites = self.het_sites
 
         raw_read_haps = self.get_haplotypes_from_reads(
-            het_sites, check_clip=True, partial_deletion_reads=self.del1_reads_partial
+            check_clip=True,
+            partial_deletion_reads=self.del1_reads_partial,
+            kept_sites=["32046300_G_A", "32013265_A_T"],
         )
+
+        het_sites = self.het_sites
         if self.del2_reads_partial != set():
             raw_read_haps, het_sites = self.update_reads_for_deletions(
                 raw_read_haps,
                 het_sites,
                 self.del2_3p_pos1,
                 self.del2_5p_pos2,
                 self.del2_reads_partial,
@@ -610,15 +613,15 @@
                     if var in self.known_variants:
                         hap_variants[hap].append(self.known_variants[var])
 
         total_cn = len(ass_haps) + len(two_cp_haplotypes)
         if ass_haps == [] and self.het_sites == []:
             # homozygous, feed all reads to call variants
             total_cn = 2
-        if total_cn < 2:
+        if total_cn < 2 or len(ending_copies) > 2:
             total_cn = None
 
         annotated_alleles = self.annotate_alleles(
             successful_phasing,
             new_alleles,
             hap_variants,
             ending_copies,
```

### Comparing `paraphase-2.0.0/paraphase/genes/smn1_phaser.py` & `paraphase-2.1.0/paraphase/genes/smn1_phaser.py`

 * *Files 1% similar despite different names*

```diff
@@ -507,22 +507,20 @@
             ]
         if self.smn1_del_reads_partial != set():
             regions_to_check += [
                 [self.del1_3p_pos1, self.del1_3p_pos2],
                 [self.del1_5p_pos1, self.del1_5p_pos2],
             ]
         self.get_candidate_pos(regions_to_check=regions_to_check)
-        # always add splice site
-        if self.candidate_pos != set():
-            self.candidate_pos.add("70951946_C_T")
 
-        het_sites = sorted(list(self.candidate_pos))
-        raw_read_haps = self.get_haplotypes_from_reads(het_sites)
+        self.het_sites = sorted(list(self.candidate_pos))
+        raw_read_haps = self.get_haplotypes_from_reads(add_sites=["70951946_C_T"])
 
         # update reads for those overlapping known deletions
+        het_sites = self.het_sites
         if self.smn2_del_reads_partial != set():
             raw_read_haps, het_sites = self.update_reads_for_deletions(
                 raw_read_haps,
                 het_sites,
                 self.del2_3p_pos1,
                 self.del2_5p_pos2,
                 self.smn2_del_reads_partial,
```

### Comparing `paraphase-2.0.0/paraphase/genes/strc_phaser.py` & `paraphase-2.1.0/paraphase/genes/strc_phaser.py`

 * *Files 10% similar despite different names*

```diff
@@ -25,15 +25,14 @@
     def set_parameter(self, config):
         super().set_parameter(config)
         self.deletion1_size = config["coordinates"]["hg38"]["deletion1_size"]
         self.del1_3p_pos1 = config["coordinates"]["hg38"]["del1_3p_pos1"]
         self.del1_3p_pos2 = config["coordinates"]["hg38"]["del1_3p_pos2"]
         self.del1_5p_pos1 = config["coordinates"]["hg38"]["del1_5p_pos1"]
         self.del1_5p_pos2 = config["coordinates"]["hg38"]["del1_5p_pos2"]
-        self.intergenic = config["coordinates"]["hg38"]["depth_region"]
         self.depth_region = config["coordinates"]["hg38"]["depth_region"]
 
     def call(self):
         if self.check_coverage_before_analysis() is False:
             return None
         genome_bamh = pysam.AlignmentFile(self.genome_bam, "rb")
         intergenic_depth = self.get_regional_depth(genome_bamh, self.depth_region)[0]
@@ -46,15 +45,15 @@
             self.del1_5p_pos2,
             self.deletion1_size,
         )
         self.get_candidate_pos()
         self.het_sites = sorted(list(self.candidate_pos))
         self.remove_noisy_sites()
 
-        raw_read_haps = self.get_haplotypes_from_reads(self.het_sites)
+        raw_read_haps = self.get_haplotypes_from_reads(add_sites=["43602487_C_G"])
         het_sites = self.het_sites
         if self.del1_reads_partial != set():
             raw_read_haps, het_sites = self.update_reads_for_deletions(
                 raw_read_haps,
                 het_sites,
                 self.del1_3p_pos1,
                 self.del1_5p_pos2,
@@ -69,57 +68,76 @@
             hcn,
             uniquely_supporting_reads,
             nonuniquely_supporting_reads,
             raw_read_haps,
             read_counts,
         ) = self.phase_haps(raw_read_haps)
 
+        haplotypes = None
+        dvar = None
+        two_cp_haps = []
         tmp = {}
         counter_gene = 0
         counter_pseudo = 0
         for hap in ass_haps:
             if "3" in hap:
                 counter_pseudo += 1
                 tmp.setdefault(hap, f"strcp1_hap{counter_pseudo}")
             else:
                 counter_gene += 1
                 tmp.setdefault(hap, f"strc_hap{counter_gene}")
         ass_haps = tmp
 
-        haplotypes = None
-        dvar = None
         if self.het_sites != []:
             haplotypes, dvar = self.output_variants_in_haplotypes(
                 ass_haps,
                 uniquely_supporting_reads,
                 nonuniquely_supporting_reads,
             )
 
-        two_cp_haps = []
-        if intergenic_depth > 5 and len(ass_haps) == 2:
-            two_cp_haps = list(ass_haps.values())
-        elif counter_gene == 1 or counter_pseudo == 1:
-            two_cp_haps = self.compare_depth(haplotypes)
-        for hap in two_cp_haps:
-            if "strcp1" not in hap:
-                counter_gene += 1
+            if counter_gene == 1 or counter_pseudo == 1:
+                two_cp_haps = self.compare_depth(haplotypes)
+                for hap in two_cp_haps:
+                    if "strcp1" not in hap:
+                        counter_gene += 1
+                    else:
+                        counter_pseudo += 1
+            if (
+                intergenic_depth > 5
+                and counter_gene == 1
+                and counter_pseudo == 1
+                and two_cp_haps == []
+            ):
+                two_cp_haps = list(ass_haps.values())
+                for hap in two_cp_haps:
+                    if "strcp1" not in hap:
+                        counter_gene += 1
+                    else:
+                        counter_pseudo += 1
+
+            total_cn = len(ass_haps) + len(two_cp_haps)
+
+            # check depth between STRC and pseudogene
+            if self.mdepth is not None:
+                prob = self.depth_prob(int(intergenic_depth), self.mdepth / 2)
+                if prob[0] < 0.9 and counter_gene == 1:
+                    counter_gene = None
+                    total_cn = None
+                if prob[0] > 0.95 and counter_gene > 1 and counter_pseudo > 1:
+                    counter_gene = None
+                    total_cn = None
+
+        # homozygous case
+        else:
+            total_cn = 2
+            # both copies are pseudogene
+            if self.del1_reads_partial != set() or "43604720_G_A" in self.homo_sites:
+                counter_gene = 0
             else:
-                counter_pseudo += 1
-
-        total_cn = len(ass_haps) + len(two_cp_haps)
-
-        # check depth between STRC and pseudogene
-        if self.mdepth is not None:
-            prob = self.depth_prob(int(intergenic_depth), self.mdepth / 2)
-            if prob[0] < 0.9 and counter_gene == 1:
-                counter_gene = None
-                total_cn = None
-            if prob[0] > 0.95 and counter_gene > 1 and two_cp_haps != []:
-                counter_gene = None
-                total_cn = None
+                counter_gene = 2
 
         self.close_handle()
 
         return self.GeneCall(
             total_cn,
             counter_gene,
             ass_haps,
```

### Comparing `paraphase-2.0.0/paraphase/genome_depth.py` & `paraphase-2.1.0/paraphase/genome_depth.py`

 * *Files 8% similar despite different names*

```diff
@@ -17,21 +17,19 @@
     def get_genome_depth(self):
         depth = []
         with open(self.genome_depth_region_file) as f:
             for line in f:
                 at = line.split()
                 nchr = at[0]
                 pos1 = int(at[1])
-                site_depth = 0
                 for pos in [pos1, pos1 + 1600]:
-                    for pileupcolumn in self._bamh.pileup(
-                        nchr, pos - 1, pos, truncate=True
-                    ):
-                        site_depth = pileupcolumn.get_num_aligned()
-                depth.append(site_depth)
+                    site_depth = self._bamh.count(
+                        nchr, pos - 1, pos, read_callback="all"
+                    )
+                    depth.append(site_depth)
         self.mdepth = np.median(depth)
         self.mad = np.median([abs(a - self.mdepth) for a in depth]) / self.mdepth
 
     def call(self):
         self.get_genome_depth()
         self._bamh.close()
         return self.mdepth, self.mad
```

### Comparing `paraphase-2.0.0/paraphase/haplotype_assembler.py` & `paraphase-2.1.0/paraphase/haplotype_assembler.py`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/paraphase/paraphase.py` & `paraphase-2.1.0/paraphase/paraphase.py`

 * *Files 2% similar despite different names*

```diff
@@ -207,15 +207,15 @@
             if os.path.exists(data_file) is False:
                 raise Exception(f"File {data_file} not found.")
     return configs
 
 
 def main():
     parser = argparse.ArgumentParser(
-        description="paraphase: HiFi-based SMN1/SMN2 variant caller."
+        description="paraphase: HiFi-based caller for highly homologous genes"
     )
     all_genes_joined = ",".join(ACCEPTED_GENES)
     inputp = parser.add_argument_group("Input Options")
     outputp = parser.add_argument_group("Output Options")
     input_group = inputp.add_mutually_exclusive_group(required=True)
     input_group.add_argument(
         "-b",
```

### Comparing `paraphase-2.0.0/paraphase/phaser.py` & `paraphase-2.1.0/paraphase/phaser.py`

 * *Files 13% similar despite different names*

```diff
@@ -6,22 +6,32 @@
 import os
 import copy
 import numpy as np
 from collections import Counter
 import re
 import logging
 from scipy.stats import poisson
+from collections import namedtuple
 from .haplotype_assembler import VariantGraph
 
 
 class Phaser:
 
     clip_5p = r"^\d+S|^\d+H"
     clip_3p = r"\d+S$|\d+H$"
     deletion = r"\d+D"
+    GeneCall = namedtuple(
+        "GeneCall",
+        "total_cn final_haplotypes two_copy_haplotypes \
+        highest_total_cn assembled_haplotypes sites_for_phasing \
+        unique_supporting_reads het_sites_not_used_in_phasing homozygous_sites \
+        haplotype_details variant_genotypes nonunique_supporting_reads \
+        read_details genome_depth",
+    )
+    MEAN_BASE_QUAL = 25
 
     def __init__(self, sample_id, outdir, wgs_depth=None, genome_bam=None):
         self.outdir = outdir
         self.sample_id = sample_id
         self.homopolymer_sites = {}
         self.het_sites = []  # for phasing
         self.het_no_phasing = []
@@ -65,19 +75,18 @@
     def get_regional_depth(self, bam_handle, query_region, ninterval=100):
         """Get depth of the query regions"""
         region_depth = []
         for region in query_region:
             depth = []
             nstep = max(1, int((region[1] - region[0]) / ninterval))
             for pos in range(region[0], region[1], nstep):
-                for pileupcolumn in bam_handle.pileup(
-                    self.nchr, pos - 1, pos, truncate=True
-                ):
-                    site_depth = pileupcolumn.get_num_aligned()
-                    depth.append(site_depth)
+                site_depth = bam_handle.count(
+                    self.nchr, pos - 1, pos, read_callback="all"
+                )
+                depth.append(site_depth)
             region_depth.append(np.median(depth))
         return region_depth
 
     def check_coverage_before_analysis(self):
         """check low coverage regions for enrichment data"""
         region_depth = self.get_regional_depth(
             self._bamh, [[self.left_boundary, self.right_boundary]]
@@ -205,102 +214,176 @@
                 and read.query_name in partial_deletion_reads
             ):
                 read_names.append(read.query_name)
         return read_names
 
     def get_haplotypes_from_reads(
         self,
-        het_sites,
+        exclude_reads=[],
+        min_mapq=5,
+        min_clip_len=50,
+        check_clip=False,
+        partial_deletion_reads=[],
+        kept_sites=[],
+        add_sites=[],
+    ):
+        """
+        Go through reads and get bases at sites of interest.
+        Two rounds, with variant site filtering in between.
+        """
+        raw_read_haps = self.get_haplotypes_from_reads_step(
+            exclude_reads,
+            min_mapq,
+            min_clip_len,
+            check_clip,
+            partial_deletion_reads,
+        )
+        self.remove_var(raw_read_haps, kept_sites)
+        if self.het_sites != []:
+            for var in add_sites:
+                if var not in self.het_sites:
+                    self.het_sites.append(var)
+        self.het_sites = sorted(self.het_sites)
+        raw_read_haps = self.get_haplotypes_from_reads_step(
+            exclude_reads,
+            min_mapq,
+            min_clip_len,
+            check_clip,
+            partial_deletion_reads,
+        )
+        return raw_read_haps
+
+    def get_haplotypes_from_reads_step(
+        self,
         exclude_reads=[],
         min_mapq=5,
         min_clip_len=50,
         check_clip=False,
         partial_deletion_reads=[],
     ):
         """
         Go through reads and get bases at sites of interest
         Returns:
             read_haps (dict of str:list): collapse each read into just the positions
             of interest. 1 corresponds to ref, 2 corresponds to alt
         """
+        het_sites = self.het_sites
         read_haps = {}
         nvar = len(het_sites)
         for dsnp_index, allele_site in enumerate(het_sites):
             snp_position_gene1, allele1, allele2, *at = allele_site.split("_")
             snp_position = int(snp_position_gene1)
+            reads_with_flanking_indels = []
             for pileupcolumn in self._bamh.pileup(
                 self.nchr,
-                snp_position - 1,
+                snp_position - 2,
                 snp_position,
                 truncate=True,
-                min_base_quality=29,
+                min_base_quality=self.MEAN_BASE_QUAL,
             ):
-                for read in pileupcolumn.pileups:
-                    read_names = self.get_read_names(
-                        read.alignment, partial_deletion_reads
-                    )
-                    for read_name in read_names:
-                        if (
-                            not read.is_del
-                            and not read.is_refskip
-                            and not read.alignment.is_secondary
-                            and read.alignment.mapping_quality >= min_mapq
-                            and read_name not in exclude_reads
-                        ):
-                            read_seq = read.alignment.query_sequence
-                            start_pos = read.query_position
-                            end_pos = start_pos + 1
-                            if end_pos < len(read_seq):
-                                hap = read_seq[start_pos:end_pos]
-                                if read_name not in read_haps:
-                                    read_haps.setdefault(read_name, ["x"] * nvar)
-                                if hap.upper() == allele1.upper():
-                                    read_haps[read_name][dsnp_index] = "1"
-                                elif hap.upper() == allele2.upper():
-                                    read_haps[read_name][dsnp_index] = "2"
+                # require that the base on the read is not flanked by any indels
+                if pileupcolumn.reference_pos == snp_position - 2:
+                    for read in pileupcolumn.pileups:
+                        if read.indel != 0 or read.is_del:
+                            read_names = self.get_read_names(
+                                read.alignment, partial_deletion_reads
+                            )
+                            for read_name in read_names:
+                                reads_with_flanking_indels.append(read_name)
+                if pileupcolumn.reference_pos == snp_position - 1:
+                    for read in pileupcolumn.pileups:
+                        read_names = self.get_read_names(
+                            read.alignment, partial_deletion_reads
+                        )
+                        for read_name in read_names:
+                            if (
+                                not read.is_del
+                                and not read.is_refskip
+                                and not read.alignment.is_secondary
+                                and read.alignment.mapping_quality >= min_mapq
+                                and read_name not in exclude_reads
+                                and read.indel == 0
+                                and read_name not in reads_with_flanking_indels
+                            ):
+                                read_seq = read.alignment.query_sequence
+                                start_pos = read.query_position
+                                end_pos = start_pos + 1
+                                if end_pos < len(read_seq):
+                                    hap = read_seq[start_pos:end_pos]
+                                    if read_name not in read_haps:
+                                        read_haps.setdefault(read_name, ["x"] * nvar)
+                                    if hap.upper() == allele1.upper():
+                                        read_haps[read_name][dsnp_index] = "1"
+                                    elif hap.upper() == allele2.upper():
+                                        read_haps[read_name][dsnp_index] = "2"
 
         # for softclips starting at a predefined position, mark sites as 0 instead of x
         if check_clip:
             for dsnp_index, allele_site in enumerate(het_sites):
                 snp_position_gene1, allele1, allele2, *at = allele_site.split("_")
                 snp_position = int(snp_position_gene1)
                 for clip_position in sorted(self.clip_3p_positions):
                     if snp_position > clip_position:
                         for read in self._bamh.fetch(
                             self.nchr, clip_position - 10, clip_position + 10
                         ):
                             read_name = self.get_read_name(read)
-                            if read_name in read_haps:
-                                if abs(read.reference_end - clip_position) < 20:
-                                    find_clip_3p = re.findall(
-                                        self.clip_3p, read.cigarstring
-                                    )
-                                    if (
-                                        find_clip_3p != []
-                                        and int(find_clip_3p[0][:-1]) >= min_clip_len
-                                    ):
-                                        read_haps[read_name][dsnp_index] = "0"
+                            if read_name not in read_haps:
+                                read_haps.setdefault(read_name, ["x"] * nvar)
+                            if abs(read.reference_end - clip_position) < 20:
+                                find_clip_3p = re.findall(
+                                    self.clip_3p, read.cigarstring
+                                )
+                                if (
+                                    find_clip_3p != []
+                                    and int(find_clip_3p[0][:-1]) >= min_clip_len
+                                ):
+                                    read_haps[read_name][dsnp_index] = "0"
                 for clip_position in sorted(self.clip_5p_positions, reverse=True):
                     if snp_position < clip_position:
                         for read in self._bamh.fetch(
                             self.nchr, clip_position - 10, clip_position + 10
                         ):
                             read_name = self.get_read_name(read)
-                            if read_name in read_haps:
-                                if abs(read.reference_start - clip_position) < 20:
-                                    find_clip_5p = re.findall(
-                                        self.clip_5p, read.cigarstring
-                                    )
-                                    if (
-                                        find_clip_5p != []
-                                        and int(find_clip_5p[0][:-1]) >= min_clip_len
-                                    ):
-                                        read_haps[read_name][dsnp_index] = "0"
+                            if read_name not in read_haps:
+                                read_haps.setdefault(read_name, ["x"] * nvar)
+                            if abs(read.reference_start - clip_position) < 20:
+                                find_clip_5p = re.findall(
+                                    self.clip_5p, read.cigarstring
+                                )
+                                if (
+                                    find_clip_5p != []
+                                    and int(find_clip_5p[0][:-1]) >= min_clip_len
+                                ):
+                                    read_haps[read_name][dsnp_index] = "0"
         return read_haps
 
+    def remove_var(self, raw_read_haps, kept_sites):
+        """remove variants that are not present after checking each read-haplotype"""
+        bases_per_site = {}
+        sites_to_remove = []
+        for i in range(len(self.het_sites)):
+            for read, hap in raw_read_haps.items():
+                base = hap[i]
+                bases_per_site.setdefault(i, []).append(base)
+
+        for pos in bases_per_site:
+            bases = bases_per_site[pos]
+            bases_x = bases.count("x")
+            bases_ref = bases.count("1")
+            bases_alt = bases.count("2")
+            this_var = self.het_sites[pos]
+            if bases_x == len(bases):
+                sites_to_remove.append(this_var)
+            if bases_ref + bases_alt == len(bases) - bases_x and bases_alt <= 3:
+                if this_var not in kept_sites:
+                    sites_to_remove.append(this_var)
+        for var in sites_to_remove:
+            self.het_sites.remove(var)
+
     def allow_del_bases(self, pos):
         return False
 
     def process_indel(self, pos, ref_seq, var_seq):
         """Translate pysam indel seq into real sequence"""
         if "+" in var_seq:
             ins_base = var_seq.split(re.findall(r"\+\d+", var_seq)[0])[1]
@@ -339,91 +422,100 @@
         variants_no_phasing = {}
         for pos in pileups_raw:
             all_bases = pileups_raw[pos]
             total_depth = len(all_bases)
             del_bases_count = all_bases.count("*")
             # get reference base
             offset_pos = pos - self.offset
-            ref_seq = self._refh.fetch(self.nchr_old, offset_pos - 1, offset_pos)
+            ref_seq_genome = self._refh.fetch(self.nchr_old, offset_pos - 1, offset_pos)
 
             if total_depth >= min_read_support and (
                 del_bases_count < min_read_support or self.allow_del_bases(pos)
             ):
                 all_bases = [a for a in all_bases if a != "*"]
                 counter = Counter(all_bases)
-                bases = counter.most_common(2)
-                if (
-                    len(counter) >= 2
-                    and bases[1][1] >= min_read_support
-                    and bases[1][1] / total_depth > min_vaf
-                ):
-                    var_seq = None
-                    found_ref = ref_seq in [a[0] for a in bases]
-                    for base in bases:
-                        if base[0] != ref_seq:
-                            var_seq = base[0]
-                            break
-                    if found_ref is True and var_seq is not None:
-                        # SNV
-                        if "-" not in var_seq and "+" not in var_seq:
-                            if pos not in self.homopolymer_sites:
-                                variants.setdefault(pos, (ref_seq, var_seq))
-                            else:
-                                prohibited_bases = self.homopolymer_sites[pos].split(
-                                    ","
-                                )
-                                if var_seq not in prohibited_bases:
-                                    if "1" in prohibited_bases:
-                                        variants.setdefault(pos, (ref_seq, var_seq))
-                                    else:
-                                        variants_no_phasing.setdefault(
-                                            pos, (ref_seq, var_seq)
-                                        )
-                        # indels
-                        elif pos not in self.homopolymer_sites:
-                            ref_seq, var_seq, indel_size = self.process_indel(
-                                pos, ref_seq, var_seq
-                            )
-                            if indel_size < 25:
-                                variants_no_phasing.setdefault(pos, (ref_seq, var_seq))
-                elif len(counter) == 1 or (
+                # include multi-allelic sites
+                bases = counter.most_common(3)
+                # homozygous
+                if len(counter) == 1 or (
                     len(counter) >= 2
                     and bases[0][1] > len(all_bases) - min_read_support
                 ):
                     var_seq = bases[0][0]
+                    ref_seq = ref_seq_genome
                     if var_seq != ref_seq:
                         # SNV and indels
                         if "-" not in var_seq and "+" not in var_seq:
                             # "homo" sites in large deletions should be put back into het sites
                             if (
                                 self.allow_del_bases(pos)
                                 and del_bases_count >= min_read_support
                                 and pos not in self.homopolymer_sites
                             ):
-                                variants.setdefault(pos, (ref_seq, var_seq))
+                                variants.setdefault(pos, []).append((ref_seq, var_seq))
                             elif pos not in self.homopolymer_sites or (
                                 pos in self.homopolymer_sites
                                 and var_seq
                                 not in self.homopolymer_sites[pos].split(",")
                             ):
                                 self.homo_sites.append(f"{pos}_{ref_seq}_{var_seq}")
                         elif pos not in self.homopolymer_sites:
                             ref_seq, var_seq, indel_size = self.process_indel(
                                 pos, ref_seq, var_seq
                             )
                             if indel_size < 25:
                                 self.homo_sites.append(f"{pos}_{ref_seq}_{var_seq}")
+                elif len(counter) >= 2:
+                    found_ref = ref_seq_genome in [a[0] for a in bases]
+                    if found_ref:
+                        for var_seq, var_count in bases:
+                            ref_seq = ref_seq_genome
+                            if (
+                                var_seq != ref_seq
+                                and var_count >= min_read_support
+                                and var_count / total_depth > min_vaf
+                            ):
+                                # SNV
+                                if "-" not in var_seq and "+" not in var_seq:
+                                    if pos not in self.homopolymer_sites:
+                                        variants.setdefault(pos, []).append(
+                                            (ref_seq, var_seq)
+                                        )
+                                    else:
+                                        prohibited_bases = self.homopolymer_sites[
+                                            pos
+                                        ].split(",")
+                                        if var_seq not in prohibited_bases:
+                                            if "1" in prohibited_bases:
+                                                variants.setdefault(pos, []).append(
+                                                    (ref_seq, var_seq)
+                                                )
+                                            else:
+                                                variants_no_phasing.setdefault(
+                                                    pos, (ref_seq, var_seq)
+                                                )
+                                # indels
+                                elif pos not in self.homopolymer_sites:
+                                    ref_seq, var_seq, indel_size = self.process_indel(
+                                        pos, ref_seq, var_seq
+                                    )
+                                    if indel_size < 25:
+                                        variants_no_phasing.setdefault(
+                                            pos, (ref_seq, var_seq)
+                                        )
+
         # exclude variants caused by shifted softclips of the big deletions
         excluded_variants = []
         for region in regions_to_check:
             var_to_check = [a for a in variants if region[0] < a < region[1]]
             excluded_variants += var_to_check
         for pos in variants:
-            if pos not in excluded_variants:
-                ref_seq, var_seq = variants[pos]
+            # for now, filter out multi-allelic sites
+            if pos not in excluded_variants and len(variants[pos]) == 1:
+                ref_seq, var_seq = variants[pos][0]
                 self.candidate_pos.add(f"{pos}_{ref_seq}_{var_seq}")
 
         excluded_variants = []
         for region in regions_to_check:
             var_to_check = [a for a in variants_no_phasing if region[0] < a < region[1]]
             excluded_variants += var_to_check
         for pos in variants_no_phasing:
@@ -644,17 +736,17 @@
                         hap[pos1 - 1] == "0"
                         and pos1 - 1 >= 0
                         and hap[pos1 + 1] == "0"
                         and pos1 + 1 < len(hap)
                     ):
                         hap[pos1] = "0"
                     else:
-                        flanking_left = hap[min(0, pos1 - 2) : pos1]
+                        flanking_left = hap[max(0, pos1 - 2) : pos1]
                         flanking_right = hap[
-                            max(pos1 + 1, len(hap)) : max(pos1 + 3, len(hap))
+                            min(pos1 + 1, len(hap)) : min(pos1 + 3, len(hap))
                         ]
                         if "x" not in flanking_left and "x" not in flanking_right:
                             hap[pos1] = "1"
                     raw_read_haps[read] = "".join(hap)
         return raw_read_haps, het_sites
 
     def get_read_counts(self, uniquely_supporting_haps):
@@ -695,15 +787,15 @@
         read_count = {}
         for hap in uniquely_supporting_haps:
             reads = uniquely_supporting_haps[hap]
             lreads = [a for a in reads if a[nstart:nend] != "x" * (nend - nstart)]
             read_count.setdefault(hap, len(lreads))
         return read_count
 
-    def phase_haps(self, raw_read_haps, debug=False):
+    def phase_haps(self, raw_read_haps, min_support=4, debug=False):
         """
         Assemble and evaluate haplotypes
         """
         het_sites = self.het_sites
         haplotypes_to_reads, raw_read_haps = self.simplify_read_haps(raw_read_haps)
 
         ass_haps = []
@@ -718,16 +810,53 @@
         else:
             pivot_index, _ = self.get_pivot_site_index()
             hap_graph = VariantGraph(
                 raw_read_haps, pivot_index, figure_id=self.sample_id
             )
             ass_haps, original_haps, hcn = hap_graph.run(debug=debug, make_plot=debug)
 
-        read_support = VariantGraph.match_reads_and_haplotypes(raw_read_haps, ass_haps)
+        (
+            uniquely_supporting_reads,
+            nonuniquely_supporting_reads,
+            read_counts,
+        ) = self.get_read_support(raw_read_haps, haplotypes_to_reads, ass_haps)
 
+        # remove spurious ones
+        ass_haps = self.adjust_spurious_haplotypes(uniquely_supporting_reads)
+        (
+            uniquely_supporting_reads,
+            nonuniquely_supporting_reads,
+            read_counts,
+        ) = self.get_read_support(raw_read_haps, haplotypes_to_reads, ass_haps)
+
+        # remove low-support ones
+        ass_haps = [
+            a
+            for a in uniquely_supporting_reads
+            if len(uniquely_supporting_reads[a]) >= min_support
+        ]
+        (
+            uniquely_supporting_reads,
+            nonuniquely_supporting_reads,
+            read_counts,
+        ) = self.get_read_support(raw_read_haps, haplotypes_to_reads, ass_haps)
+
+        return (
+            ass_haps,
+            original_haps,
+            hcn,
+            uniquely_supporting_reads,
+            nonuniquely_supporting_reads,
+            raw_read_haps,
+            read_counts,
+        )
+
+    def get_read_support(self, raw_read_haps, haplotypes_to_reads, ass_haps):
+        """Find uniquely and nonuniquely supporting reads for given haplotypes"""
+        read_support = VariantGraph.match_reads_and_haplotypes(raw_read_haps, ass_haps)
         uniquely_supporting_haps = read_support.unique
         read_counts = self.get_read_counts(uniquely_supporting_haps)
 
         uniquely_supporting_reads = {}
         for hap in ass_haps:
             uniquely_supporting_reads.setdefault(hap, [])
         for hap in uniquely_supporting_haps:
@@ -740,20 +869,16 @@
         for read in read_support.by_read:
             num_matches = len(read_support.by_read[read])
             if num_matches > 1:
                 nonuniquely_supporting_reads.setdefault(
                     read, read_support.by_read[read]
                 )
         return (
-            ass_haps,
-            original_haps,
-            hcn,
             uniquely_supporting_reads,
             nonuniquely_supporting_reads,
-            raw_read_haps,
             read_counts,
         )
 
     def compare_depth(self, haplotypes, loose=False):
         """
         For each haplotype, identify the variants where it's different
         from other haplotypes. Check depth at those variant sites and
@@ -792,15 +917,19 @@
                 elif var not in this_hap_var and other_haps_var.count(var) == other_cn:
                     sites.setdefault(pos, ref)
 
             counts = []
             for pos in sites:
                 hap_base = sites[pos]
                 for pileupcolumn in bamh.pileup(
-                    self.nchr, pos - 1, pos, truncate=True, min_base_quality=29
+                    self.nchr,
+                    pos - 1,
+                    pos,
+                    truncate=True,
+                    min_base_quality=self.MEAN_BASE_QUAL,
                 ):
                     bases = [a.upper() for a in pileupcolumn.get_query_sequences()]
                     base_num = bases.count(hap_base)
                     counts.append([base_num, len(bases) - base_num])
 
             probs = []
             nsites = len(sites)
@@ -811,10 +940,139 @@
                 two_cp_haps.append(hap)
             elif loose is True:
                 if len(probs_fil) >= nsites * 0.5 and nsites >= 5:
                     two_cp_haps.append(hap)
 
         return two_cp_haps
 
+    def adjust_spurious_haplotypes(self, uniquely_supporting_reads, flanking_bp=10):
+        """Identify spurious haplotypes caused by locally misaligned reads"""
+        passing_haplotypes = list(uniquely_supporting_reads.keys())
+        suspicious_hap_pair = []
+        lhap = uniquely_supporting_reads.keys()
+        for hap1 in lhap:
+            for hap2 in lhap:
+                if hap1 != hap2:
+                    nmatch = 0
+                    nmismatch = 0
+                    mismatch_sites = []
+                    for i, base1 in enumerate(hap1):
+                        base2 = hap2[i]
+                        if "x" not in [base1, base2]:
+                            if base1 == base2:
+                                nmatch += 1
+                            elif base1 in ["1", "2"] and base2 in ["1", "2"]:
+                                nmismatch += 1
+                                mismatch_sites.append(self.het_sites[i])
+                    if nmatch >= 5 and nmismatch == 1 and len(mismatch_sites) == 1:
+                        mismatch_pos = int(mismatch_sites[0].split("_")[0])
+                        hap1_reads = uniquely_supporting_reads[hap1]
+                        hap2_reads = uniquely_supporting_reads[hap2]
+                        hap_pair = None
+                        if len(hap1_reads) <= 5 and len(hap2_reads) >= 6:
+                            hap_pair = [hap2, hap1]
+                        elif len(hap2_reads) <= 5 and len(hap1_reads) >= 6:
+                            hap_pair = [hap1, hap2]
+                        if (
+                            hap_pair is not None
+                            and [
+                                hap_pair,
+                                mismatch_pos,
+                            ]
+                            not in suspicious_hap_pair
+                        ):
+                            suspicious_hap_pair.append([hap_pair, mismatch_pos])
+
+        for hap_pair, mismatch_pos in suspicious_hap_pair:
+            hap1, hap2 = hap_pair
+            hap1_reads = uniquely_supporting_reads[hap1]
+            hap2_reads = uniquely_supporting_reads[hap2]
+            hap1_reads_at_pos = []
+            hap2_reads_at_pos = []
+            for pileupcolumn in self._bamh.pileup(
+                self.nchr,
+                mismatch_pos - 1,
+                mismatch_pos,
+                truncate=True,
+                min_base_quality=self.MEAN_BASE_QUAL,
+            ):
+                for read in pileupcolumn.pileups:
+                    if not read.is_del and not read.is_refskip:
+                        read_name = read.alignment.query_name
+                        read_seq = read.alignment.query_sequence
+                        read_pos = read.query_position
+                        if (
+                            read_name in hap1_reads + hap2_reads
+                            and read_pos >= flanking_bp
+                            and read_pos + flanking_bp < len(read_seq)
+                        ):
+                            start_pos = read_pos - flanking_bp
+                            end_pos = read_pos + flanking_bp
+                            if read_name in hap1_reads:
+                                hap1_reads_at_pos.append(read_seq[start_pos:end_pos])
+                            if read_name in hap2_reads:
+                                hap2_reads_at_pos.append(read_seq[start_pos:end_pos])
+
+            if set(hap1_reads_at_pos).intersection(set(hap2_reads_at_pos)) != set():
+                passing_haplotypes.remove(hap2)
+        return passing_haplotypes
+
+    def call(self):
+        """Main function to phase haplotypes and call copy numbers"""
+        if self.check_coverage_before_analysis() is False:
+            return None
+        self.get_homopolymer()
+        self.get_candidate_pos()
+        self.het_sites = sorted(list(self.candidate_pos))
+        self.remove_noisy_sites()
+
+        raw_read_haps = self.get_haplotypes_from_reads()
+
+        (
+            ass_haps,
+            original_haps,
+            hcn,
+            uniquely_supporting_reads,
+            nonuniquely_supporting_reads,
+            raw_read_haps,
+            read_counts,
+        ) = self.phase_haps(raw_read_haps)
+
+        tmp = {}
+        for i, hap in enumerate(ass_haps):
+            tmp.setdefault(hap, f"hap{i+1}")
+        ass_haps = tmp
+
+        haplotypes = None
+        dvar = None
+        if self.het_sites != []:
+            haplotypes, dvar = self.output_variants_in_haplotypes(
+                ass_haps,
+                uniquely_supporting_reads,
+                nonuniquely_supporting_reads,
+            )
+
+        two_cp_haps = self.compare_depth(haplotypes)
+        total_cn = len(ass_haps) + len(two_cp_haps)
+
+        self.close_handle()
+
+        return self.GeneCall(
+            total_cn,
+            ass_haps,
+            two_cp_haps,
+            hcn,
+            original_haps,
+            self.het_sites,
+            uniquely_supporting_reads,
+            self.het_no_phasing,
+            self.homo_sites,
+            haplotypes,
+            dvar,
+            nonuniquely_supporting_reads,
+            raw_read_haps,
+            self.mdepth,
+        )
+
     def close_handle(self):
         self._bamh.close()
         self._refh.close()
```

### Comparing `paraphase-2.0.0/paraphase/prepare_bam_and_vcf.py` & `paraphase-2.1.0/paraphase/prepare_bam_and_vcf.py`

 * *Files 2% similar despite different names*

```diff
@@ -384,17 +384,17 @@
         var_seq = ref_seq
         if all_bases != []:
             counter = Counter(all_bases)
             most_common_base = counter.most_common(2)
             var_seq = most_common_base[0][0]
             ad = most_common_base[0][1]
             if (
-                dp >= 3
-                and ad >= 2
-                and (len(most_common_base) == 1 or ad > most_common_base[1][1])
+                len(var_seq) == 1 and len(ref_seq) == 1 and dp >= 3 and ad > dp * 0.5
+            ) or (
+                (len(var_seq) > 1 or len(ref_seq) > 1) and dp >= 5 and ad >= dp * 0.7
             ):
                 if var_seq == ref_seq or var_seq == "*":
                     gt = "0"
                 else:
                     gt = "1"
         return [var_seq, dp, ad, gt]
 
@@ -553,20 +553,26 @@
                 true_pos = pos
                 refh_pos = pos + offset
             else:
                 true_pos = pos + offset
                 refh_pos = pos
             ref_seq = refh.fetch(ref_name, refh_pos - 1, refh_pos)
             alt_all_reads = self.get_var(all_bases, ref_seq)
-            if None not in hap_bound and hap_bound[0] < true_pos < hap_bound[1]:
+            if hap_bound == [] or (
+                None not in hap_bound and hap_bound[0] < true_pos < hap_bound[1]
+            ):
                 # use only unique reads for positions at the edge
-                if true_pos < hap_bound[2] or true_pos > hap_bound[3]:
+                if (
+                    hap_bound == []
+                    or true_pos < hap_bound[2]
+                    or true_pos > hap_bound[3]
+                ):
                     bases_uniq_reads = []
                     for i, read_base in enumerate(all_bases):
-                        if read_names[pos][i] in uniq_reads:
+                        if uniq_reads is None or read_names[pos][i] in uniq_reads:
                             bases_uniq_reads.append(read_base)
                     alt_uniq_reads = self.get_var(bases_uniq_reads, ref_seq)
                     if alt_uniq_reads[-1] != ".":
                         var_seq, dp, ad, gt = alt_uniq_reads
                     else:
                         var_seq, dp, ad, gt = alt_all_reads
                         gt = "."
@@ -619,14 +625,49 @@
         nhap = len(final_haps) + len(
             [a for a in two_cp_haplotypes if a in final_haps.values()]
         )
 
         bamh = pysam.AlignmentFile(self.bam, "rb")
         refh = pysam.FastaFile(self.ref)
 
+        if final_haps == {}:
+            hap_name = "homozygous_hap1"
+            hap_vcf_out = os.path.join(
+                self.vcf_dir, self.sample_id + f"_{self.gene}_{hap_name}.vcf"
+            )
+            vcf_out = open(hap_vcf_out, "w")
+            self.write_header(vcf_out)
+            pileups_raw = {}
+            read_names = {}
+            for pileupcolumn in bamh.pileup(
+                self.nchr,
+                truncate=True,
+                min_base_quality=30,
+            ):
+                pos = pileupcolumn.pos + 1
+                this_pos_bases = [
+                    a.upper() for a in pileupcolumn.get_query_sequences(add_indels=True)
+                ]
+                pileups_raw.setdefault(pos, this_pos_bases)
+                read_names.setdefault(pos, pileupcolumn.get_query_names())
+            variants_called = self.pileup_to_variant(
+                pileups_raw,
+                read_names,
+                None,
+                refh,
+                0 - self.offset,
+                [],
+                vcf_out,
+            )
+            vcf_out.close()
+            for pos, var_name, dp, ad, qual, gt in variants_called:
+                vars.setdefault(
+                    pos, [[var_name, dp, ad, qual, gt], [var_name, dp, ad, qual, gt]]
+                )
+
         i = 0
         for hap_name in final_haps.values():
             hap_bound = self.get_hap_bound(hap_name)
             hap_vcf_out = os.path.join(
                 self.vcf_dir, self.sample_id + f"_{self.gene}_{hap_name}.vcf"
             )
             vcf_out = open(hap_vcf_out, "w")
```

### Comparing `paraphase-2.0.0/paraphase.egg-info/PKG-INFO` & `paraphase-2.1.0/paraphase.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: paraphase
-Version: 2.0.0
+Version: 2.1.0
 Summary: paraphase: HiFi-based caller for highly homologous genes
 Home-page: https://github.com/PacificBiosciences/paraphase
 Author: Xiao Chen
 Author-email: xchen@pacificbiosciences.com
 License: BSD-3-Clause-Clear
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `paraphase-2.0.0/paraphase.egg-info/SOURCES.txt` & `paraphase-2.1.0/paraphase.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/setup.py` & `paraphase-2.1.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 def readme():
     with open("README.md") as f:
         return f.read()
 
 
 setup(
     name="paraphase",
-    version="2.0.0",
+    version="2.1.0",
     description="paraphase: HiFi-based caller for highly homologous genes",
     long_description=readme(),
     url="https://github.com/PacificBiosciences/paraphase",
     author="Xiao Chen",
     author_email="xchen@pacificbiosciences.com",
     license="BSD-3-Clause-Clear",
     packages=["paraphase", "paraphase.genes"],
```

### Comparing `paraphase-2.0.0/tests/test_haplotype_assembler.py` & `paraphase-2.1.0/tests/test_haplotype_assembler.py`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/tests/test_phaser.py` & `paraphase-2.1.0/tests/test_phaser.py`

 * *Files identical despite different names*

### Comparing `paraphase-2.0.0/tests/test_smn1_phaser.py` & `paraphase-2.1.0/tests/test_smn1_phaser.py`

 * *Files identical despite different names*

