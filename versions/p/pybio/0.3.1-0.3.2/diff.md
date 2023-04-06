# Comparing `tmp/pybio-0.3.1.tar.gz` & `tmp/pybio-0.3.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pybio-0.3.1.tar", last modified: Thu Apr  6 07:59:49 2023, max compression
+gzip compressed data, was "pybio-0.3.2.tar", last modified: Thu Apr  6 08:10:20 2023, max compression
```

## Comparing `pybio-0.3.1.tar` & `pybio-0.3.2.tar`

### file list

```diff
@@ -1,55 +1,55 @@
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.166423 pybio-0.3.1/
--rw-rw-r--   0 rotg     (2023757) games       (20)     9489 2023-04-06 07:59:49.166015 pybio-0.3.1/PKG-INFO
--rw-rw-r--   0 rotg     (2023757) games       (20)     9200 2023-04-03 07:10:50.000000 pybio-0.3.1/README.md
--rw-rw-r--   0 rotg     (2023757) games       (20)       38 2023-04-06 07:59:49.166519 pybio-0.3.1/setup.cfg
--rw-rw-r--   0 rotg     (2023757) games       (20)      845 2023-04-06 07:59:41.000000 pybio-0.3.1/setup.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.134940 pybio-0.3.1/src/
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.141923 pybio-0.3.1/src/pybio/
--rw-rw-r--   0 rotg     (2023757) games       (20)     7599 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/__init__.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.146039 pybio-0.3.1/src/pybio/config/
--rw-rw-r--   0 rotg     (2023757) games       (20)     1930 2023-04-03 07:11:00.000000 pybio-0.3.1/src/pybio/config/__init__.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.147119 pybio-0.3.1/src/pybio/core/
--rw-rw-r--   0 rotg     (2023757) games       (20)       98 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/core/__init__.py
--rw-rw-r--   0 rotg     (2023757) games       (20)    25251 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/core/genomes.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.156076 pybio-0.3.1/src/pybio/data/
--rw-rw-r--   0 rotg     (2023757) games       (20)      877 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Bam.py
--rw-rw-r--   0 rotg     (2023757) games       (20)    16391 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Bedgraph.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     4675 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Bedgraph2.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     1912 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Fasta.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     1244 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Fastq.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     1591 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Gene.py
--rw-rw-r--   0 rotg     (2023757) games       (20)      177 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/GeneFeature.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     3238 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Gff3.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     2777 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Gtf.py
--rw-rw-r--   0 rotg     (2023757) games       (20)      186 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Sequence.py
--rw-rw-r--   0 rotg     (2023757) games       (20)      906 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Sissrs.py
--rw-rw-r--   0 rotg     (2023757) games       (20)      956 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/TabReader.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     2019 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/Wig.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     2168 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/data/__init__.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.156570 pybio-0.3.1/src/pybio/expression/
--rw-rw-r--   0 rotg     (2023757) games       (20)     8831 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/expression/__init__.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.160061 pybio-0.3.1/src/pybio/map/
--rw-rw-r--   0 rotg     (2023757) games       (20)     2257 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/map/STAR.py
--rw-rw-r--   0 rotg     (2023757) games       (20)      131 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/map/__init__.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     1438 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/map/bowtie.py
--rw-rw-r--   0 rotg     (2023757) games       (20)      580 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/map/nano.py
--rw-rw-r--   0 rotg     (2023757) games       (20)     1061 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/map/sege.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.162186 pybio-0.3.1/src/pybio/maths/
--rw-rw-r--   0 rotg     (2023757) games       (20)      974 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/maths/__init__.py
--rw-rw-r--   0 rotg     (2023757) games       (20)    37335 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/maths/pstat.py
--rw-rw-r--   0 rotg     (2023757) games       (20)   151400 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/maths/stats.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.164131 pybio-0.3.1/src/pybio/path/
--rw-rw-r--   0 rotg     (2023757) games       (20)      347 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/path/__init__.py
--rwxrwxr-x   0 rotg     (2023757) games       (20)     3537 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/pybio
--rw-rw-r--   0 rotg     (2023757) games       (20)      101 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/pybio.config.example
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.164601 pybio-0.3.1/src/pybio/sequence/
--rw-rw-r--   0 rotg     (2023757) games       (20)     5566 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/sequence/__init__.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.165418 pybio-0.3.1/src/pybio/utils/
--rw-rw-r--   0 rotg     (2023757) games       (20)    10199 2023-04-03 07:10:50.000000 pybio-0.3.1/src/pybio/utils/__init__.py
-drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 07:59:49.145343 pybio-0.3.1/src/pybio.egg-info/
--rw-rw-r--   0 rotg     (2023757) games       (20)     9489 2023-04-06 07:59:49.142568 pybio-0.3.1/src/pybio.egg-info/PKG-INFO
--rw-rw-r--   0 rotg     (2023757) games       (20)     1030 2023-04-06 07:59:49.143167 pybio-0.3.1/src/pybio.egg-info/SOURCES.txt
--rw-rw-r--   0 rotg     (2023757) games       (20)        1 2023-04-06 07:59:49.143612 pybio-0.3.1/src/pybio.egg-info/dependency_links.txt
--rw-rw-r--   0 rotg     (2023757) games       (20)        1 2023-04-06 07:45:01.000000 pybio-0.3.1/src/pybio.egg-info/not-zip-safe
--rw-rw-r--   0 rotg     (2023757) games       (20)       32 2023-04-06 07:59:49.144894 pybio-0.3.1/src/pybio.egg-info/requires.txt
--rw-rw-r--   0 rotg     (2023757) games       (20)        6 2023-04-06 07:59:49.145419 pybio-0.3.1/src/pybio.egg-info/top_level.txt
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.473858 pybio-0.3.2/
+-rw-rw-r--   0 rotg     (2023757) games       (20)     9431 2023-04-06 08:10:20.473552 pybio-0.3.2/PKG-INFO
+-rw-rw-r--   0 rotg     (2023757) games       (20)     9200 2023-04-03 07:10:50.000000 pybio-0.3.2/README.md
+-rw-rw-r--   0 rotg     (2023757) games       (20)       38 2023-04-06 08:10:20.473972 pybio-0.3.2/setup.cfg
+-rw-rw-r--   0 rotg     (2023757) games       (20)      864 2023-04-06 08:09:27.000000 pybio-0.3.2/setup.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.450166 pybio-0.3.2/src/
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.455117 pybio-0.3.2/src/pybio/
+-rw-rw-r--   0 rotg     (2023757) games       (20)     7599 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/__init__.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.459108 pybio-0.3.2/src/pybio/config/
+-rw-rw-r--   0 rotg     (2023757) games       (20)     1930 2023-04-03 07:11:00.000000 pybio-0.3.2/src/pybio/config/__init__.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.459771 pybio-0.3.2/src/pybio/core/
+-rw-rw-r--   0 rotg     (2023757) games       (20)       98 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/core/__init__.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)    25251 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/core/genomes.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.466778 pybio-0.3.2/src/pybio/data/
+-rw-rw-r--   0 rotg     (2023757) games       (20)      877 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Bam.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)    16391 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Bedgraph.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     4675 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Bedgraph2.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     1912 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Fasta.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     1244 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Fastq.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     1591 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Gene.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)      177 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/GeneFeature.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     3238 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Gff3.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     2777 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Gtf.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)      186 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Sequence.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)      906 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Sissrs.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)      956 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/TabReader.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     2019 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/Wig.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     2168 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/data/__init__.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.467109 pybio-0.3.2/src/pybio/expression/
+-rw-rw-r--   0 rotg     (2023757) games       (20)     8831 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/expression/__init__.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.469773 pybio-0.3.2/src/pybio/map/
+-rw-rw-r--   0 rotg     (2023757) games       (20)     2257 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/map/STAR.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)      131 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/map/__init__.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     1438 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/map/bowtie.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)      580 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/map/nano.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)     1061 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/map/sege.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.470950 pybio-0.3.2/src/pybio/maths/
+-rw-rw-r--   0 rotg     (2023757) games       (20)      974 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/maths/__init__.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)    37335 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/maths/pstat.py
+-rw-rw-r--   0 rotg     (2023757) games       (20)   151400 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/maths/stats.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.472346 pybio-0.3.2/src/pybio/path/
+-rw-rw-r--   0 rotg     (2023757) games       (20)      347 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/path/__init__.py
+-rwxrwxr-x   0 rotg     (2023757) games       (20)     3537 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/pybio
+-rw-rw-r--   0 rotg     (2023757) games       (20)      101 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/pybio.config.example
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.472687 pybio-0.3.2/src/pybio/sequence/
+-rw-rw-r--   0 rotg     (2023757) games       (20)     5566 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/sequence/__init__.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.473052 pybio-0.3.2/src/pybio/utils/
+-rw-rw-r--   0 rotg     (2023757) games       (20)    10199 2023-04-03 07:10:50.000000 pybio-0.3.2/src/pybio/utils/__init__.py
+drwxrwxr-x   0 rotg     (2023757) games       (20)        0 2023-04-06 08:10:20.458433 pybio-0.3.2/src/pybio.egg-info/
+-rw-rw-r--   0 rotg     (2023757) games       (20)     9431 2023-04-06 08:10:20.455894 pybio-0.3.2/src/pybio.egg-info/PKG-INFO
+-rw-rw-r--   0 rotg     (2023757) games       (20)     1030 2023-04-06 08:10:20.456186 pybio-0.3.2/src/pybio.egg-info/SOURCES.txt
+-rw-rw-r--   0 rotg     (2023757) games       (20)        1 2023-04-06 08:10:20.457699 pybio-0.3.2/src/pybio.egg-info/dependency_links.txt
+-rw-rw-r--   0 rotg     (2023757) games       (20)        1 2023-04-06 07:45:01.000000 pybio-0.3.2/src/pybio.egg-info/not-zip-safe
+-rw-rw-r--   0 rotg     (2023757) games       (20)       32 2023-04-06 08:10:20.458239 pybio-0.3.2/src/pybio.egg-info/requires.txt
+-rw-rw-r--   0 rotg     (2023757) games       (20)        6 2023-04-06 08:10:20.458554 pybio-0.3.2/src/pybio.egg-info/top_level.txt
```

### Comparing `pybio-0.3.1/PKG-INFO` & `pybio-0.3.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 Metadata-Version: 2.1
 Name: pybio
-Version: 0.3.1
+Version: 0.3.2
 Summary: pybio genomics
 Home-page: https://github.com/grexor/pybio
 Author: Gregor Rot
 Author-email: gregor.rot@gmail.com
 Keywords: pybio,bioinformatics
 Classifier: Programming Language :: Python :: 3
 Description-Content-Type: text/markdown
 
-picture><img src="media/pybio.png" width="70"/></picture>
 ## pybio: basic genomics toolset
 
 pybio is a Python 3 framework for basic genomics/transcriptomics operations/annotations. The package is a dependency to [apa](https://github.com/grexor/apa) (alternative polyadenylation) and [RNAmotifs2](https://github.com/grexor/rnamotifs2) (motif cluster analysis). The pybio package provides:
 
 Features include automagical genome assemblies+annotation download and indexing from Ensembl and STAR, support of Fasta, Fastq, bedGraph and other file formats, motif sequence searches, and specific APA feautes like alternative polyadenylation site-pair classification (same-exon, skipped-exon, composite-exon) and more.
 
 ## Contents
```

### Comparing `pybio-0.3.1/README.md` & `pybio-0.3.2/README.md`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/__init__.py` & `pybio-0.3.2/src/pybio/__init__.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/config/__init__.py` & `pybio-0.3.2/src/pybio/config/__init__.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/core/genomes.py` & `pybio-0.3.2/src/pybio/core/genomes.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Bam.py` & `pybio-0.3.2/src/pybio/data/Bam.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Bedgraph.py` & `pybio-0.3.2/src/pybio/data/Bedgraph.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Bedgraph2.py` & `pybio-0.3.2/src/pybio/data/Bedgraph2.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Fasta.py` & `pybio-0.3.2/src/pybio/data/Fasta.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Fastq.py` & `pybio-0.3.2/src/pybio/data/Fastq.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Gene.py` & `pybio-0.3.2/src/pybio/data/Gene.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Gff3.py` & `pybio-0.3.2/src/pybio/data/Gff3.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Gtf.py` & `pybio-0.3.2/src/pybio/data/Gtf.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Sissrs.py` & `pybio-0.3.2/src/pybio/data/Sissrs.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/TabReader.py` & `pybio-0.3.2/src/pybio/data/TabReader.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/Wig.py` & `pybio-0.3.2/src/pybio/data/Wig.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/data/__init__.py` & `pybio-0.3.2/src/pybio/data/__init__.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/expression/__init__.py` & `pybio-0.3.2/src/pybio/expression/__init__.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/map/STAR.py` & `pybio-0.3.2/src/pybio/map/STAR.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/map/bowtie.py` & `pybio-0.3.2/src/pybio/map/bowtie.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/map/nano.py` & `pybio-0.3.2/src/pybio/map/nano.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/map/sege.py` & `pybio-0.3.2/src/pybio/map/sege.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/maths/__init__.py` & `pybio-0.3.2/src/pybio/maths/__init__.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/maths/pstat.py` & `pybio-0.3.2/src/pybio/maths/pstat.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/maths/stats.py` & `pybio-0.3.2/src/pybio/maths/stats.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/pybio` & `pybio-0.3.2/src/pybio/pybio`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/sequence/__init__.py` & `pybio-0.3.2/src/pybio/sequence/__init__.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio/utils/__init__.py` & `pybio-0.3.2/src/pybio/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `pybio-0.3.1/src/pybio.egg-info/PKG-INFO` & `pybio-0.3.2/src/pybio.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 Metadata-Version: 2.1
 Name: pybio
-Version: 0.3.1
+Version: 0.3.2
 Summary: pybio genomics
 Home-page: https://github.com/grexor/pybio
 Author: Gregor Rot
 Author-email: gregor.rot@gmail.com
 Keywords: pybio,bioinformatics
 Classifier: Programming Language :: Python :: 3
 Description-Content-Type: text/markdown
 
-picture><img src="media/pybio.png" width="70"/></picture>
 ## pybio: basic genomics toolset
 
 pybio is a Python 3 framework for basic genomics/transcriptomics operations/annotations. The package is a dependency to [apa](https://github.com/grexor/apa) (alternative polyadenylation) and [RNAmotifs2](https://github.com/grexor/rnamotifs2) (motif cluster analysis). The pybio package provides:
 
 Features include automagical genome assemblies+annotation download and indexing from Ensembl and STAR, support of Fasta, Fastq, bedGraph and other file formats, motif sequence searches, and specific APA feautes like alternative polyadenylation site-pair classification (same-exon, skipped-exon, composite-exon) and more.
 
 ## Contents
```

### Comparing `pybio-0.3.1/src/pybio.egg-info/SOURCES.txt` & `pybio-0.3.2/src/pybio.egg-info/SOURCES.txt`

 * *Files identical despite different names*

