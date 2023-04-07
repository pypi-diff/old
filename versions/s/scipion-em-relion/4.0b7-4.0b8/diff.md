# Comparing `tmp/scipion-em-relion-4.0b7.tar.gz` & `tmp/scipion-em-relion-4.0b8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "scipion-em-relion-4.0b7.tar", last modified: Thu Nov 11 18:54:21 2021, max compression
+gzip compressed data, was "scipion-em-relion-4.0b8.tar", last modified: Sat Nov 27 18:21:59 2021, max compression
```

## Comparing `scipion-em-relion-4.0b7.tar` & `scipion-em-relion-4.0b8.tar`

### file list

```diff
@@ -1,93 +1,93 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.637692 scipion-em-relion-4.0b7/
--rw-r--r--   0 runner    (1001) docker     (121)     6140 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/CHANGES.txt
--rw-r--r--   0 runner    (1001) docker     (121)    35147 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      230 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     6038 2021-11-11 18:54:21.637692 scipion-em-relion-4.0b7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     4320 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.625692 scipion-em-relion-4.0b7/relion/
--rw-r--r--   0 runner    (1001) docker     (121)     3956 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4265 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/bibtex.py
--rw-r--r--   0 runner    (1001) docker     (121)     4393 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.629692 scipion-em-relion-4.0b7/relion/convert/
--rw-r--r--   0 runner    (1001) docker     (121)     8093 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4457 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/convert30.py
--rw-r--r--   0 runner    (1001) docker     (121)    24811 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/convert31.py
--rw-r--r--   0 runner    (1001) docker     (121)     8085 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/convert_base.py
--rw-r--r--   0 runner    (1001) docker     (121)     7506 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/convert_coordinates.py
--rw-r--r--   0 runner    (1001) docker     (121)    21375 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/convert_deprecated.py
--rw-r--r--   0 runner    (1001) docker     (121)     8692 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/convert_utils.py
--rw-r--r--   0 runner    (1001) docker     (121)    17745 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/dataimport.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.629692 scipion-em-relion-4.0b7/relion/convert/mtfs/
--rw-r--r--   0 runner    (1001) docker     (121)     9038 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_de20_300.star
--rw-r--r--   0 runner    (1001) docker     (121)    15520 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f2_300.star
--rw-r--r--   0 runner    (1001) docker     (121)     1428 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f3_200_ec.star
--rw-r--r--   0 runner    (1001) docker     (121)     1422 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f3_300_ec.star
--rw-r--r--   0 runner    (1001) docker     (121)     1385 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f4_200_ec.star
--rw-r--r--   0 runner    (1001) docker     (121)     1385 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f4_300_ec.star
--rw-r--r--   0 runner    (1001) docker     (121)    15406 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_k2_300_ec.star
--rw-r--r--   0 runner    (1001) docker     (121)     5133 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/objects.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.633692 scipion-em-relion-4.0b7/relion/protocols/
--rw-r--r--   0 runner    (1001) docker     (121)     3048 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.633692 scipion-em-relion-4.0b7/relion/protocols/_legacy/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/_legacy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    23085 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/_legacy/protocol31_initialmodel.py
--rw-r--r--   0 runner    (1001) docker     (121)    15592 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_assign_optic_groups.py
--rw-r--r--   0 runner    (1001) docker     (121)     5195 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_autopick.py
--rw-r--r--   0 runner    (1001) docker     (121)     7532 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_autopick_log.py
--rw-r--r--   0 runner    (1001) docker     (121)    24635 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_autopick_ref.py
--rw-r--r--   0 runner    (1001) docker     (121)    72066 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_base.py
--rw-r--r--   0 runner    (1001) docker     (121)    23016 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_bayesian_polishing.py
--rw-r--r--   0 runner    (1001) docker     (121)     3781 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_center_averages.py
--rw-r--r--   0 runner    (1001) docker     (121)     5111 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_classify2d.py
--rw-r--r--   0 runner    (1001) docker     (121)     6767 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_classify3d.py
--rw-r--r--   0 runner    (1001) docker     (121)     4526 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_compress_estimate_gain.py
--rw-r--r--   0 runner    (1001) docker     (121)     6176 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_compress_movies.py
--rw-r--r--   0 runner    (1001) docker     (121)     9305 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_create_mask3d.py
--rw-r--r--   0 runner    (1001) docker     (121)     6901 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_crop_resize.py
--rw-r--r--   0 runner    (1001) docker     (121)    15726 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_ctf_refinement.py
--rw-r--r--   0 runner    (1001) docker     (121)     5226 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_expand_symmetry.py
--rw-r--r--   0 runner    (1001) docker     (121)     3439 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_export_coords.py
--rw-r--r--   0 runner    (1001) docker     (121)     6545 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_export_ctf.py
--rw-r--r--   0 runner    (1001) docker     (121)     5966 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_export_particles.py
--rw-r--r--   0 runner    (1001) docker     (121)    21115 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_extract_particles.py
--rw-r--r--   0 runner    (1001) docker     (121)     6941 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_gentle_clean.py
--rw-r--r--   0 runner    (1001) docker     (121)    18466 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_initialmodel.py
--rw-r--r--   0 runner    (1001) docker     (121)    10098 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_localres.py
--rw-r--r--   0 runner    (1001) docker     (121)    29794 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_motioncor.py
--rw-r--r--   0 runner    (1001) docker     (121)    18530 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_multibody.py
--rw-r--r--   0 runner    (1001) docker     (121)    14927 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_postprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)    13050 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_preprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)     7387 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_reconstruct.py
--rw-r--r--   0 runner    (1001) docker     (121)     7671 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_refine3d.py
--rw-r--r--   0 runner    (1001) docker     (121)     7257 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_remove_views.py
--rw-r--r--   0 runner    (1001) docker     (121)     5947 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_select_classes.py
--rw-r--r--   0 runner    (1001) docker     (121)    15704 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_subtract.py
--rw-r--r--   0 runner    (1001) docker     (121)     3519 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols/protocol_symmetrize_volume.py
--rw-r--r--   0 runner    (1001) docker     (121)     5946 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/protocols.conf
--rw-r--r--   0 runner    (1001) docker     (121)    15098 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/relion_logo.jpg
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.633692 scipion-em-relion-4.0b7/relion/tests/
--rw-r--r--   0 runner    (1001) docker     (121)     1486 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    36717 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/tests/test_convert_relion.py
--rw-r--r--   0 runner    (1001) docker     (121)     6328 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/tests/test_projection_subtraction_no_relion.py
--rw-r--r--   0 runner    (1001) docker     (121)    63612 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/tests/test_protocols_relion.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    15844 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/tests/test_protocols_relion3.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     7238 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/tests/test_workflow_relion3.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.633692 scipion-em-relion-4.0b7/relion/viewers/
--rw-r--r--   0 runner    (1001) docker     (121)     1459 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    38359 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/viewer_base.py
--rw-r--r--   0 runner    (1001) docker     (121)    16162 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/viewer_ctfrefine.py
--rw-r--r--   0 runner    (1001) docker     (121)     5896 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/viewer_locres.py
--rw-r--r--   0 runner    (1001) docker     (121)     7208 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/viewer_motioncor.py
--rw-r--r--   0 runner    (1001) docker     (121)     6209 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/viewer_multibody.py
--rw-r--r--   0 runner    (1001) docker     (121)     4537 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/viewer_polishing.py
--rw-r--r--   0 runner    (1001) docker     (121)    10929 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/viewers/viewer_postprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)     7732 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/relion/wizards.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-11 18:54:21.637692 scipion-em-relion-4.0b7/scipion_em_relion.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     6038 2021-11-11 18:54:21.000000 scipion-em-relion-4.0b7/scipion_em_relion.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2924 2021-11-11 18:54:21.000000 scipion-em-relion-4.0b7/scipion_em_relion.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-11 18:54:21.000000 scipion-em-relion-4.0b7/scipion_em_relion.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       37 2021-11-11 18:54:21.000000 scipion-em-relion-4.0b7/scipion_em_relion.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)       19 2021-11-11 18:54:21.000000 scipion-em-relion-4.0b7/scipion_em_relion.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        7 2021-11-11 18:54:21.000000 scipion-em-relion-4.0b7/scipion_em_relion.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-11-11 18:54:21.637692 scipion-em-relion-4.0b7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     8485 2021-11-11 18:52:23.000000 scipion-em-relion-4.0b7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.437534 scipion-em-relion-4.0b8/
+-rw-r--r--   0 runner    (1001) docker     (121)     6140 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/CHANGES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)    35147 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      230 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     6017 2021-11-27 18:21:59.437534 scipion-em-relion-4.0b8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     4299 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.429534 scipion-em-relion-4.0b8/relion/
+-rw-r--r--   0 runner    (1001) docker     (121)     3932 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4265 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/bibtex.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4342 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.429534 scipion-em-relion-4.0b8/relion/convert/
+-rw-r--r--   0 runner    (1001) docker     (121)     8093 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4457 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/convert30.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24811 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/convert31.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8085 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/convert_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7506 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/convert_coordinates.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21375 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/convert_deprecated.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8692 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/convert_utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17745 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/dataimport.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.429534 scipion-em-relion-4.0b8/relion/convert/mtfs/
+-rw-r--r--   0 runner    (1001) docker     (121)     9038 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_de20_300.star
+-rw-r--r--   0 runner    (1001) docker     (121)    15520 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f2_300.star
+-rw-r--r--   0 runner    (1001) docker     (121)     1428 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f3_200_ec.star
+-rw-r--r--   0 runner    (1001) docker     (121)     1422 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f3_300_ec.star
+-rw-r--r--   0 runner    (1001) docker     (121)     1385 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f4_200_ec.star
+-rw-r--r--   0 runner    (1001) docker     (121)     1385 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f4_300_ec.star
+-rw-r--r--   0 runner    (1001) docker     (121)    15406 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_k2_300_ec.star
+-rw-r--r--   0 runner    (1001) docker     (121)     5133 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/objects.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.433534 scipion-em-relion-4.0b8/relion/protocols/
+-rw-r--r--   0 runner    (1001) docker     (121)     3039 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.433534 scipion-em-relion-4.0b8/relion/protocols/_legacy/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/_legacy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23085 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/_legacy/protocol31_initialmodel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15592 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_assign_optic_groups.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5195 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_autopick.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7532 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_autopick_log.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24635 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_autopick_ref.py
+-rw-r--r--   0 runner    (1001) docker     (121)    72066 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23016 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_bayesian_polishing.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3781 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_center_averages.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5111 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_classify2d.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6767 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_classify3d.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7973 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_compress_movies.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9305 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_create_mask3d.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6901 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_crop_resize.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15726 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_ctf_refinement.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5079 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_estimate_gain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5226 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_expand_symmetry.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3439 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_export_coords.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6545 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_export_ctf.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5966 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_export_particles.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21115 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_extract_particles.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6941 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_gentle_clean.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18466 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_initialmodel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10098 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_localres.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29794 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_motioncor.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18530 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_multibody.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14927 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_postprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13050 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_preprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7387 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_reconstruct.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7671 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_refine3d.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7257 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_remove_views.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5947 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_select_classes.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15704 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_subtract.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3519 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols/protocol_symmetrize_volume.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5946 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/protocols.conf
+-rw-r--r--   0 runner    (1001) docker     (121)    15098 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/relion_logo.jpg
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.433534 scipion-em-relion-4.0b8/relion/tests/
+-rw-r--r--   0 runner    (1001) docker     (121)     1486 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36717 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/tests/test_convert_relion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6328 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/tests/test_projection_subtraction_no_relion.py
+-rw-r--r--   0 runner    (1001) docker     (121)    63612 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/tests/test_protocols_relion.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    15690 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/tests/test_protocols_relion3.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     7238 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/tests/test_workflow_relion3.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.433534 scipion-em-relion-4.0b8/relion/viewers/
+-rw-r--r--   0 runner    (1001) docker     (121)     1459 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38359 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/viewer_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16162 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/viewer_ctfrefine.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5896 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/viewer_locres.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7208 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/viewer_motioncor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6209 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/viewer_multibody.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4537 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/viewer_polishing.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10929 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/viewers/viewer_postprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7732 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/relion/wizards.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-27 18:21:59.433534 scipion-em-relion-4.0b8/scipion_em_relion.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     6017 2021-11-27 18:21:59.000000 scipion-em-relion-4.0b8/scipion_em_relion.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2915 2021-11-27 18:21:59.000000 scipion-em-relion-4.0b8/scipion_em_relion.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-27 18:21:59.000000 scipion-em-relion-4.0b8/scipion_em_relion.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       37 2021-11-27 18:21:59.000000 scipion-em-relion-4.0b8/scipion_em_relion.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       19 2021-11-27 18:21:59.000000 scipion-em-relion-4.0b8/scipion_em_relion.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        7 2021-11-27 18:21:59.000000 scipion-em-relion-4.0b8/scipion_em_relion.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2021-11-27 18:21:59.437534 scipion-em-relion-4.0b8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     8485 2021-11-27 18:20:25.000000 scipion-em-relion-4.0b8/setup.py
```

### Comparing `scipion-em-relion-4.0b7/CHANGES.txt` & `scipion-em-relion-4.0b8/CHANGES.txt`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/LICENSE` & `scipion-em-relion-4.0b8/LICENSE`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/PKG-INFO` & `scipion-em-relion-4.0b8/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: scipion-em-relion
-Version: 4.0b7
+Version: 4.0b8
 Summary: Plugin to use Relion programs within the Scipion framework
 Home-page: https://github.com/scipion-em/scipion-em-relion
 Author: Grigory Sharov, J.M. De la Rosa Trevin, Josue Gomez Blanco
 Author-email: gsharov@mrc-lmb.cam.ac.uk, delarosatrevin@scilifelab.se, josue.gomez-blanco@mcgill.ca
 License: UNKNOWN
 Project-URL: Bug Reports, https://github.com/scipion-em/scipion-em-relion/issues
 Project-URL: Source, https://github.com/scipion-em/scipion-em-relion/
@@ -72,15 +72,15 @@
         - If you want to use **2D class ranker** protocol, you also need to set *RELION_PYTHON* that points to a Python which includes torch and numpy modules.
         
         To check the installation, simply run one of the tests. A complete list of tests can be displayed by executing ``scipion test --show --grep relion``
         
         Supported versions
         ------------------
         
-        3.1.0, 3.1.1, 3.1.2, 3.1.3, 4.0
+        3.1.3, 4.0
         
         Protocols
         ---------
         
         * 2D class ranker
         * 2D classification         
         * 3D auto-refine
```

### Comparing `scipion-em-relion-4.0b7/README.rst` & `scipion-em-relion-4.0b8/README.rst`

 * *Files 1% similar despite different names*

```diff
@@ -62,15 +62,15 @@
 - If you want to use **2D class ranker** protocol, you also need to set *RELION_PYTHON* that points to a Python which includes torch and numpy modules.
 
 To check the installation, simply run one of the tests. A complete list of tests can be displayed by executing ``scipion test --show --grep relion``
 
 Supported versions
 ------------------
 
-3.1.0, 3.1.1, 3.1.2, 3.1.3, 4.0
+3.1.3, 4.0
 
 Protocols
 ---------
 
 * 2D class ranker
 * 2D classification         
 * 3D auto-refine
```

### Comparing `scipion-em-relion-4.0b7/relion/__init__.py` & `scipion-em-relion-4.0b8/relion/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -28,22 +28,22 @@
 
 import pyworkflow.utils as pwutils
 import pwem
 
 from .constants import *
 
 
-__version__ = '4.0b7'
+__version__ = '4.0b8'
 _logo = "relion_logo.jpg"
 _references = ['Scheres2012a', 'Scheres2012b', 'Kimanius2016', 'Zivanov2018']
 
 
 class Plugin(pwem.Plugin):
     _homeVar = RELION_HOME
-    _supportedVersions = [V3_1_0, V3_1_1, V3_1_2, V3_1_3, V4_0]
+    _supportedVersions = [V3_1_3, V4_0]
     _url = "https://github.com/scipion-em/scipion-em-relion"
 
     @classmethod
     def _defineVariables(cls):
         cls._defineEmVar(RELION_HOME, 'relion-%s' % V4_0)
         cls._defineVar(RELION_CUDA_LIB, pwem.Config.CUDA_LIB)
         cls._defineVar(RELION_PYTHON, None)
```

### Comparing `scipion-em-relion-4.0b7/relion/bibtex.py` & `scipion-em-relion-4.0b8/relion/bibtex.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/constants.py` & `scipion-em-relion-4.0b8/relion/constants.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,17 +31,14 @@
 # ----------------- Constants values ------------------------------------------
 
 RELION_HOME = 'RELION_HOME'
 RELION_CUDA_LIB = 'RELION_CUDA_LIB'
 RELION_PYTHON = 'RELION_PYTHON'
 
 # Supported versions:
-V3_1_0 = '3.1.0'
-V3_1_1 = '3.1.1'
-V3_1_2 = '3.1.2'
 V3_1_3 = '3.1.3'
 V4_0 = '4.0'
 
 MASK_FILL_ZERO = 0
 MASK_FILL_NOISE = 1
 
 ANGULAR_SAMPLING_LIST = ['30', '15', '7.5', '3.7', '1.8', '0.9', '0.5',
```

### Comparing `scipion-em-relion-4.0b7/relion/convert/__init__.py` & `scipion-em-relion-4.0b8/relion/convert/__init__.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/convert30.py` & `scipion-em-relion-4.0b8/relion/convert/convert30.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/convert31.py` & `scipion-em-relion-4.0b8/relion/convert/convert31.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/convert_base.py` & `scipion-em-relion-4.0b8/relion/convert/convert_base.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/convert_coordinates.py` & `scipion-em-relion-4.0b8/relion/convert/convert_coordinates.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/convert_deprecated.py` & `scipion-em-relion-4.0b8/relion/convert/convert_deprecated.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/convert_utils.py` & `scipion-em-relion-4.0b8/relion/convert/convert_utils.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/dataimport.py` & `scipion-em-relion-4.0b8/relion/convert/dataimport.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_de20_300.star` & `scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_de20_300.star`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f2_300.star` & `scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f2_300.star`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f3_200_ec.star` & `scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f3_200_ec.star`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f3_300_ec.star` & `scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f3_300_ec.star`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f4_200_ec.star` & `scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f4_200_ec.star`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_f4_300_ec.star` & `scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_f4_300_ec.star`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/convert/mtfs/mtf_k2_300_ec.star` & `scipion-em-relion-4.0b8/relion/convert/mtfs/mtf_k2_300_ec.star`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/objects.py` & `scipion-em-relion-4.0b8/relion/objects.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/__init__.py` & `scipion-em-relion-4.0b8/relion/protocols/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -28,15 +28,15 @@
 from .protocol_assign_optic_groups import ProtRelionAssignOpticsGroup
 from .protocol_autopick_log import ProtRelionAutopickLoG
 from .protocol_autopick_ref import ProtRelion2Autopick
 from .protocol_bayesian_polishing import ProtRelionBayesianPolishing
 from .protocol_center_averages import ProtRelionCenterAverages
 from .protocol_classify2d import ProtRelionClassify2D
 from .protocol_classify3d import ProtRelionClassify3D
-from .protocol_compress_estimate_gain import ProtRelionCompressEstimateGain
+from .protocol_estimate_gain import ProtRelionCompressEstimateGain
 from .protocol_compress_movies import ProtRelionCompressMovies
 from .protocol_create_mask3d import ProtRelionCreateMask3D
 from .protocol_crop_resize import ProtRelionResizeVolume
 from .protocol_ctf_refinement import ProtRelionCtfRefinement
 from .protocol_expand_symmetry import ProtRelionExpandSymmetry
 from .protocol_export_coords import ProtRelionExportCoordinates
 from .protocol_export_ctf import ProtRelionExportCtf
```

### Comparing `scipion-em-relion-4.0b7/relion/protocols/_legacy/protocol31_initialmodel.py` & `scipion-em-relion-4.0b8/relion/protocols/_legacy/protocol31_initialmodel.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_assign_optic_groups.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_assign_optic_groups.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_autopick.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_autopick.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_autopick_log.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_autopick_log.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_autopick_ref.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_autopick_ref.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_base.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_base.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_bayesian_polishing.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_bayesian_polishing.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_center_averages.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_center_averages.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_classify2d.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_classify2d.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_classify3d.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_classify3d.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_compress_estimate_gain.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_estimate_gain.py`

 * *Files 16% similar despite different names*

```diff
@@ -26,83 +26,85 @@
 
 import pyworkflow.protocol.params as params
 import pyworkflow.utils as pwutils
 from pyworkflow.protocol import STEPS_SERIAL
 from pyworkflow.constants import PROD
 from pwem.protocols import ProtProcessMovies
 
-import relion
 import relion.convert as convert
 
 
 class ProtRelionCompressEstimateGain(ProtProcessMovies):
     """
-    Using *relion_convert_to_tiff* to estimate the gain that can be used
-    for better compression.
+    Using *relion_convert_to_tiff* to estimate the gain reference from a set of movies.
     """
-    _label = 'estimate gain to compress'
+    _label = 'estimate gain reference'
     _devStatus = PROD
 
     def __init__(self, **kwargs):
         ProtProcessMovies.__init__(self, **kwargs)
         self.stepsExecutionMode = STEPS_SERIAL
 
     def _getConvertExtension(self, filename):
         """ Check whether it is needed to convert to .mrc or not """
         ext = pwutils.getExt(filename).lower()
         return None if ext in ['.mrc', '.mrcs', '.tiff', '.tif'] else 'mrc'
 
+    def _createFilenameTemplates(self):
+        """ Centralize how files are called. """
+        myDict = {'input_star': self._getTmpPath('input_movies.star'),
+                  'output_gain': self._getPath('gain_estimate.bin'),
+                  'output_gain_extra': self._getPath('gain_estimate_reliablity.bin')
+                  }
+        self._updateFilenamesDict(myDict)
+
     # -------------------------- DEFINE param functions -----------------------
     def _defineParams(self, form):
         form.addSection(label=pwutils.Message.LABEL_INPUT)
-
         form.addParam('inputMovies', params.PointerParam,
                       pointerClass='SetOfMovies',
                       important=True,
                       label=pwutils.Message.LABEL_INPUT_MOVS,
                       help='Select a set of movies to be used in the gain '
                            'estimation.')
-
         form.addParam('moviesSubset', params.IntParam, default=0,
                       label='Subset',
                       help="Use a subset of the movies for the estimation. "
                            "If 0, all input movies will be used. ")
 
         form.addParallelSection(threads=4, mpi=0)
 
     # --------------------------- STEPS functions -------------------------------
     def _insertAllSteps(self):
+        self._createFilenameTemplates()
         self._insertFunctionStep('convertInputStep',
                                  self.inputMovies.getObjId(),
                                  self.moviesSubset.get())
 
         self._insertFunctionStep('estimateGainStep')
         self._insertFunctionStep('createOutputStep')
 
     def convertInputStep(self, moviesId, subset):
         self.info("Relion version:")
         self.runJob("relion_convert_to_tiff --version", "", numberOfMpi=1)
-        self.info("Detected version from config: %s"
-                  % relion.Plugin.getActiveVersion())
 
         moviesList = self.inputMovies.get()
         if subset > 0:
             moviesList = [m.clone()
                           for i, m in enumerate(moviesList) if i < subset]
 
-        micStar = self._getTmpPath('input_movies.star')
-        tmp = self._getTmpPath()
-        writer = convert.createWriter(rootDir=tmp, outputDir=tmp)
-        writer.writeSetOfMovies(moviesList, micStar)
+        writer = convert.createWriter()
+        writer.writeSetOfMovies(moviesList, self._getFileName("input_star"))
 
     def estimateGainStep(self):
-        args = "--i input_movies.star --o ../ "
-        args += "--estimate_gain --j %s " % self.numberOfThreads
+        args = " --i %s --o %s" % (self._getFileName("input_star"),
+                                   self._getPath())
+        args += " --estimate_gain --j %d" % self.numberOfThreads
 
-        self.runJob('relion_convert_to_tiff', args, cwd=self._getTmpPath())
+        self.runJob('relion_convert_to_tiff', args)
 
     def createOutputStep(self):
         pass
 
     def _stepsCheck(self):
         pass
 
@@ -112,12 +114,18 @@
         return summary
 
     def _citations(self):
         return ['Zivanov2019']
 
     def _validate(self):
         errors = []
+        inputMovies = self.inputMovies.get()
+
+        if self.moviesSubset.get() > len(inputMovies):
+            errors.append("Subset size cannot be bigger than input set!")
+
+        firstMovie = inputMovies.getFirstItem()
+        if pwutils.getExt(firstMovie.getFileName()) not in [".mrcs", ".mrc"]:
+            errors.append("Gain estimation only makes sense for 32-bit float MRC(S) format.")
 
         return errors
 
-    def getOutputGain(self):
-        return self._getPath('gain_estimate.bin')
```

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_compress_movies.py` & `scipion-em-relion-4.0b8/relion/viewers/viewer_motioncor.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # ******************************************************************************
 # *
-# * Authors:     J.M. De la Rosa Trevin (delarosatrevin@scilifelab.se) [1]
+# * Authors:     Grigory Sharov     (gsharov@mrc-lmb.cam.ac.uk)
 # *
-# * [1] SciLifeLab, Stockholm University
+# * MRC Laboratory of Molecular Biology, MRC-LMB
 # *
 # * This program is free software; you can redistribute it and/or modify
 # * it under the terms of the GNU General Public License as published by
 # * the Free Software Foundation; either version 3 of the License, or
 # * (at your option) any later version.
 # *
 # * This program is distributed in the hope that it will be useful,
@@ -20,142 +20,141 @@
 # * 02111-1307  USA
 # *
 # *  All comments concerning this program package may be sent to the
 # *  e-mail address 'scipion@cnb.csic.es'
 # *
 # ******************************************************************************
 
-import os
-
-import pyworkflow.protocol.params as params
-import pyworkflow.utils as pwutils
-from pyworkflow.constants import PROD
-from pwem.protocols import ProtAlignMovies
-from pwem.objects import MovieAlignment
-from pyworkflow.protocol import STEPS_PARALLEL
-
-import relion
-
-
-class ProtRelionCompressMovies(ProtAlignMovies):
-    """
-    Using *relion_convert_to_tiff* to compress a set of movies.
-    """
-    _label = 'compress movies'
-    _devStatus = PROD
-
-    OP_COMPRESS = 0
-    OP_ESTIMATE = 1
-
-    def __init__(self, **kwargs):
-
-        ProtAlignMovies.__init__(self, **kwargs)
-        self.stepsExecutionMode = STEPS_PARALLEL
-
-    def _getConvertExtension(self, filename):
-        """ Check whether it is needed to convert to .mrc or not """
-        ext = pwutils.getExt(filename).lower()
-        return None if ext in ['.mrc', '.mrcs', '.tiff', '.tif'] else 'mrc'
-
-    # -------------------------- DEFINE param functions -----------------------
-    def _defineAlignmentParams(self, form):
-
-        form.addParam('inputGainProt', params.PointerParam, allowsNull=True,
-                      pointerClass='ProtRelionCompressEstimateGain',
-                      label='Input gain (Optional)',
-                      help='Provide as input a compress estimate protocol '
-                           'from where the estimated gain file will be taken.')
-
-        group = form.addGroup("TIFF Options")
-
-        group.addParam('compression', params.EnumParam, default=1,
-                       choices=['none', 'auto', 'zip', 'lzw'],
-                       label='Compression type')
-
-        group.addParam('deflateLevel', params.IntParam, default=6,
-                       label='Deflate level',
-                       help="deflate level. 1 (fast) "
-                            "to 9 (slowest but best compression)")
-
-        form.addParallelSection(threads=4, mpi=1)
-
-    # --------------------------- STEPS functions -------------------------------
-    def _convertInputStep(self):
-        self.info("Relion version:")
-        self.runJob("relion_convert_to_tiff --version", "", numberOfMpi=1)
-        self.info("Detected version from config: %s"
-                  % relion.Plugin.getActiveVersion())
-        # Create a local link to the input gain file if necessary
-        inputGain = self.getInputGain()
-        if inputGain:
-            tmpGain = self._getTmpPath('gain_estimate.bin')
-            pwutils.createLink(inputGain, tmpGain)
-            pwutils.createLink(inputGain.replace('.bin', '_reliablity.bin'),
-                               tmpGain.replace('.bin', '_reliablity.bin'))
-        ProtAlignMovies._convertInputStep(self)
-
-    def _processMovie(self, movie):
-        fn = movie.getAttributeValue('_originalFileName', movie.getFileName())
-        baseName = os.path.basename(fn)
-        compression = self.getEnumText('compression')
-        pwutils.createLink(fn, self._getTmpPath(baseName))
-        args = "--i %s --o ../extra/ " % baseName
-        args += "--compression %s " % compression
-        # TODO: Check if deflateLevel is only valid for zip (deflate)
-        if compression == 'zip':  # deflate
-            args += "--deflate_level %d" % self.deflateLevel
-
-        if self.getInputGain():
-            args += "--gain gain_estimate.bin "
-
-        self.runJob('relion_convert_to_tiff', args, cwd=self._getTmpPath())
-
-    # --------------------------- INFO functions ------------------------------
-    def _summary(self):
-        summary = []
-        return summary
-
-    def _citations(self):
-        return ['Zivanov2019']
-
-    def _validate(self):
-        # Check base validation before the specific ones for Motioncor
-        errors = ProtAlignMovies._validate(self)
-
-        return errors
-
-    # ------------------------ Extra BASE functions ---------------------------
-    def _getRelPath(self, baseName, refPath):
-        return os.path.relpath(self._getExtraPath(baseName), refPath)
-
-    def _getNameExt(self, movie, postFix, ext, extra=False):
-        fn = self._getMovieRoot(movie) + postFix + '.' + ext
-        return self._getExtraPath(fn) if extra else fn
-
-    def _createOutputMovies(self):
-        return True
-
-    def _createOutputMicrographs(self):
-        return False
-
-    def _createOutputWeightedMicrographs(self):
-        return False
-
-    def _savePsSum(self):
-        return self.getAttributeValue('savePSsum', False)
-
-    def _createOutputMovie(self, movie):
-        n = movie.getNumberOfFrames()
-        newMovie = movie.clone()
-        movieName = pwutils.replaceBaseExt(movie.getFileName(), 'tif')
-        newMovie.setFileName(self._getExtraPath(movieName))
-        newMovie.setAlignment(MovieAlignment(first=1, last=n,
-                                             xshifts=[0]*n, yshifts=[0]*n))
-        return newMovie
-
-    def getInputGain(self):
-        inputGainProt = self.inputGainProt.get()
-        if inputGainProt is not None:
-            inputGain = inputGainProt.getOutputGain()
-            if os.path.exists(inputGain):
-                return inputGain
-        return None
+from pyworkflow.utils import cleanPath
+from pyworkflow.viewer import DESKTOP_TKINTER, WEB_DJANGO
+from pyworkflow.protocol.params import LabelParam
+from pwem.viewers import MicrographsView, EmProtocolViewer, EmPlotter
+import pwem.viewers.showj as showj
+from pwem.objects import SetOfMovies
+
+from ..protocols import ProtRelionMotioncor
+
+
+class RelionMotioncorrViewer(EmProtocolViewer):
+    """ Visualization of relion motioncor results. """
+
+    _targets = [ProtRelionMotioncor]
+    _environments = [DESKTOP_TKINTER, WEB_DJANGO]
+    _label = 'viewer motioncor'
+
+    def _defineParams(self, form):
+        form.addSection(label='Visualization')
+        if self.hasMics():
+            form.addParam('doShowMics', LabelParam,
+                          label="Show aligned micrographs?", default=True,
+                          help="Show the output aligned micrographs.")
+        if self.hasDWMics():
+            form.addParam('doShowMicsDW', LabelParam,
+                          label="Show aligned DOSE-WEIGHTED micrographs?",
+                          default=True,
+                          help="Show the output aligned dose-weighted "
+                               "micrographs.")
+        form.addParam('doShowMovies', LabelParam,
+                      label="Show output movies?", default=True,
+                      help="Show the output movies with alignment "
+                           "information.")
+        form.addParam('doShowFailedMovies', LabelParam,
+                      label="Show FAILED movies?", default=True,
+                      help="Create a set of failed movies "
+                           "and display it.")
+        form.addParam('doShowMotion', LabelParam,
+                      label="Plot motion per frame", default=True,
+                      help="Show accumulated motion for all micrographs. "
+                           "Early motion default cut-off is 4 e/A2.")
+
+    def _getVisualizeDict(self):
+        self._errors = []
+        visualizeDict = {'doShowMovies': self._viewParam,
+                         'doShowFailedMovies': self._viewParam,
+                         'doShowMotion': self._plotMotion,
+                         }
+        if self.hasMics():
+            visualizeDict.update({'doShowMics': self._viewParam})
+
+        if self.hasDWMics():
+            visualizeDict.update({'doShowMicsDW': self._viewParam})
+
+        return visualizeDict
+
+    def hasMics(self):
+        return hasattr(self.protocol, 'outputMicrographs')
+
+    def hasDWMics(self):
+        return hasattr(self.protocol, 'outputMicrographsDoseWeighted')
+
+    def _viewParam(self, param=None):
+        labelsDef = 'enabled id _filename _samplingRate '
+        labelsDef += '_acquisition._dosePerFrame _acquisition._doseInitial '
+        viewParamsDef = {showj.MODE: showj.MODE_MD,
+                         showj.ORDER: labelsDef,
+                         showj.VISIBLE: labelsDef,
+                         showj.RENDER: None
+                         }
+        if param == 'doShowMics':
+            return [MicrographsView(self.getProject(),
+                                    self.protocol.outputMicrographs)]
+
+        elif param == 'doShowMicsDW':
+            return [MicrographsView(self.getProject(),
+                                    self.protocol.outputMicrographsDoseWeighted)]
+
+        elif param == 'doShowMovies':
+            if getattr(self.protocol, 'outputMovies', None) is not None:
+                output = self.protocol.outputMovies
+                return [self.objectView(output, viewParams=viewParamsDef)]
+            else:
+                return [self.errorMessage('No output movies found!',
+                                          title="Visualization error")]
+
+        elif param == 'doShowFailedMovies':
+            self.failedList = self.protocol._readFailedList()
+            if not self.failedList:
+                return [self.errorMessage('No failed movies found!',
+                                          title="Visualization error")]
+            else:
+                sqliteFn = self.protocol._getPath('movies_failed.sqlite')
+                self.createFailedMoviesSqlite(sqliteFn)
+                return [self.objectView(sqliteFn, viewParams=viewParamsDef)]
+
+    def createFailedMoviesSqlite(self, path):
+        inputMovies = self.protocol.inputMovies.get()
+        cleanPath(path)
+        movieSet = SetOfMovies(filename=path)
+        movieSet.copyInfo(inputMovies)
+        movieSet.copyItems(inputMovies,
+                           updateItemCallback=self._findFailedMovies)
+
+        movieSet.write()
+        movieSet.close()
+
+        return movieSet
+
+    def _findFailedMovies(self, item, row):
+        if item.getObjId() not in self.failedList:
+            setattr(item, "_appendItem", False)
+
+    def _plotMotion(self, param=None):
+        if self.hasDWMics():
+            output = self.protocol.outputMicrographsDoseWeighted
+            columns = '_rlnAccumMotionTotal _rlnAccumMotionEarly _rlnAccumMotionLate'
+            xplotter = EmPlotter.createFromFile(output.getFileName(), '',
+                                                plotType='Plot',
+                                                columnsStr=columns,
+                                                colorsStr='r g b',
+                                                linesStr='- - -',
+                                                markersStr='. . .',
+                                                xcolumn='id',
+                                                ylabel='Motion per frame (A)',
+                                                xlabel='Micrograph id',
+                                                title='Accumulated motion per frame',
+                                                bins=False,
+                                                orderColumn='id',
+                                                orderDirection='ASC')
+            return [xplotter]
+        else:
+            return [self.errorMessage('Plot is available only when dose weighting is ON',
+                                      title="Visualization error")]
```

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_create_mask3d.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_create_mask3d.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_crop_resize.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_crop_resize.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_ctf_refinement.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_ctf_refinement.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_expand_symmetry.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_expand_symmetry.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_export_coords.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_export_coords.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_export_ctf.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_export_ctf.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_export_particles.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_export_particles.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_extract_particles.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_extract_particles.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_gentle_clean.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_gentle_clean.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_initialmodel.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_initialmodel.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_localres.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_localres.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_motioncor.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_motioncor.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_multibody.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_multibody.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_postprocess.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_postprocess.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_preprocess.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_preprocess.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_reconstruct.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_reconstruct.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_refine3d.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_refine3d.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_remove_views.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_remove_views.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_select_classes.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_select_classes.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_subtract.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_subtract.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols/protocol_symmetrize_volume.py` & `scipion-em-relion-4.0b8/relion/protocols/protocol_symmetrize_volume.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/protocols.conf` & `scipion-em-relion-4.0b8/relion/protocols.conf`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/relion_logo.jpg` & `scipion-em-relion-4.0b8/relion/relion_logo.jpg`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/tests/__init__.py` & `scipion-em-relion-4.0b8/relion/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/tests/test_convert_relion.py` & `scipion-em-relion-4.0b8/relion/tests/test_convert_relion.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/tests/test_projection_subtraction_no_relion.py` & `scipion-em-relion-4.0b8/relion/tests/test_projection_subtraction_no_relion.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/tests/test_protocols_relion.py` & `scipion-em-relion-4.0b8/relion/tests/test_protocols_relion.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/tests/test_protocols_relion3.py` & `scipion-em-relion-4.0b8/relion/tests/test_protocols_relion3.py`

 * *Files 2% similar despite different names*

```diff
@@ -74,19 +74,14 @@
                                  'Data courtesy of Takyuki Kato in the Namba '
                                  'group\n(Osaka University, Japan)')
         protImport = cls.launchProtocol(protImport)
 
         return protImport
 
     def _runRelionMc(self, protImport, **kwargs):
-        # if not relion.Plugin.IS_30():
-        #     protInput = self._runAssignOptics(protImport)
-        # else:
-        #     protInput = protImport
-
         protInput = protImport
 
         args = {
             'objLabel': 'relion - motioncor',
             'patchX': 5,
             'patchY': 5,
             'numberOfThreads': CPUS
```

### Comparing `scipion-em-relion-4.0b7/relion/tests/test_workflow_relion3.py` & `scipion-em-relion-4.0b8/relion/tests/test_workflow_relion3.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/viewers/__init__.py` & `scipion-em-relion-4.0b8/relion/viewers/__init__.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/viewers/viewer_base.py` & `scipion-em-relion-4.0b8/relion/viewers/viewer_base.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/viewers/viewer_ctfrefine.py` & `scipion-em-relion-4.0b8/relion/viewers/viewer_ctfrefine.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/viewers/viewer_locres.py` & `scipion-em-relion-4.0b8/relion/viewers/viewer_locres.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/viewers/viewer_motioncor.py` & `scipion-em-relion-4.0b8/relion/viewers/viewer_multibody.py`

 * *Files 23% similar despite different names*

```diff
@@ -20,141 +20,125 @@
 # * 02111-1307  USA
 # *
 # *  All comments concerning this program package may be sent to the
 # *  e-mail address 'scipion@cnb.csic.es'
 # *
 # ******************************************************************************
 
-from pyworkflow.utils import cleanPath
-from pyworkflow.viewer import DESKTOP_TKINTER, WEB_DJANGO
-from pyworkflow.protocol.params import LabelParam
-from pwem.viewers import MicrographsView, EmProtocolViewer, EmPlotter
-import pwem.viewers.showj as showj
-from pwem.objects import SetOfMovies
-
-from ..protocols import ProtRelionMotioncor
-
-
-class RelionMotioncorrViewer(EmProtocolViewer):
-    """ Visualization of relion motioncor results. """
-
-    _targets = [ProtRelionMotioncor]
-    _environments = [DESKTOP_TKINTER, WEB_DJANGO]
-    _label = 'viewer motioncor'
+from pyworkflow.protocol.constants import STATUS_FINISHED
+
+from .viewer_base import *
+from ..protocols import ProtRelionMultiBody
+
+
+class MultibodyViewer(RelionViewer):
+    """ Visualization of Relion 3D multi-body results. """
+    _targets = [ProtRelionMultiBody]
+    _environments = [DESKTOP_TKINTER]
+
+    _label = 'viewer multi-body'
 
     def _defineParams(self, form):
+        showAnimation = self.protocol.runFlexAnalysis.get()
+
         form.addSection(label='Visualization')
-        if self.hasMics():
-            form.addParam('doShowMics', LabelParam,
-                          label="Show aligned micrographs?", default=True,
-                          help="Show the output aligned micrographs.")
-        if self.hasDWMics():
-            form.addParam('doShowMicsDW', LabelParam,
-                          label="Show aligned DOSE-WEIGHTED micrographs?",
-                          default=True,
-                          help="Show the output aligned dose-weighted "
-                               "micrographs.")
-        form.addParam('doShowMovies', LabelParam,
-                      label="Show output movies?", default=True,
-                      help="Show the output movies with alignment "
-                           "information.")
-        form.addParam('doShowFailedMovies', LabelParam,
-                      label="Show FAILED movies?", default=True,
-                      help="Create a set of failed movies "
-                           "and display it.")
-        form.addParam('doShowMotion', LabelParam,
-                      label="Plot motion per frame", default=True,
-                      help="Show accumulated motion for all micrographs. "
-                           "Early motion default cut-off is 4 e/A2.")
+        form.addParam('viewIter', params.EnumParam,
+                      choices=['last', 'selection'], default=ITER_LAST,
+                      display=params.EnumParam.DISPLAY_LIST,
+                      label="Iteration to visualize",
+                      help="""
+        *last*: only the last iteration will be visualized.
+        *selection*: you may specify a range of iterations.
+        Examples:
+        "1,5-8,10" -> [1,5,6,7,8,10]
+        "2,6,9-11" -> [2,6,9,10,11]
+        "2 5, 6-8" -> [2,5,6,7,8]                      
+                                   """)
+        form.addParam('iterSelection', params.NumericRangeParam,
+                      condition='viewIter==%d' % ITER_SELECTION,
+                      label="Iterations list",
+                      help="Write the iteration list to visualize.")
+
+        group = form.addGroup('3D Bodies')
+        group.addParam('showHalves', params.EnumParam, default=3,
+                       choices=['half1', 'half2', 'both', 'final'],
+                       label='Volume to visualize',
+                       help='Select which half do you want to visualize.')
+        group.addParam('displayVol', params.EnumParam,
+                       choices=['slices', 'chimera'],
+                       display=params.EnumParam.DISPLAY_HLIST,
+                       default=VOLUME_SLICES,
+                       label='Display volumes with',
+                       help='*slices*: display volumes as 2D slices along z axis.\n'
+                            '*chimera*: display volumes as surface with Chimera.')
+
+        if showAnimation:
+            group = form.addGroup('Flexibility analysis')
+            group.addParam('component', params.IntParam, default=1,
+                           label="Principal component to show")
+            group.addParam('showMovie', params.LabelParam,
+                           label="Show Chimera animation")
 
     def _getVisualizeDict(self):
-        self._errors = []
-        visualizeDict = {'doShowMovies': self._viewParam,
-                         'doShowFailedMovies': self._viewParam,
-                         'doShowMotion': self._plotMotion,
-                         }
-        if self.hasMics():
-            visualizeDict.update({'doShowMics': self._viewParam})
-
-        if self.hasDWMics():
-            visualizeDict.update({'doShowMicsDW': self._viewParam})
-
-        return visualizeDict
-
-    def hasMics(self):
-        return hasattr(self.protocol, 'outputMicrographs')
-
-    def hasDWMics(self):
-        return hasattr(self.protocol, 'outputMicrographsDoseWeighted')
-
-    def _viewParam(self, param=None):
-        labelsDef = 'enabled id _filename _samplingRate '
-        labelsDef += '_acquisition._dosePerFrame _acquisition._doseInitial '
-        viewParamsDef = {showj.MODE: showj.MODE_MD,
-                         showj.ORDER: labelsDef,
-                         showj.VISIBLE: labelsDef,
-                         showj.RENDER: None
-                         }
-        if param == 'doShowMics':
-            return [MicrographsView(self.getProject(),
-                                    self.protocol.outputMicrographs)]
-
-        elif param == 'doShowMicsDW':
-            return [MicrographsView(self.getProject(),
-                                    self.protocol.outputMicrographsDoseWeighted)]
-
-        elif param == 'doShowMovies':
-            if getattr(self.protocol, 'outputMovies', None) is not None:
-                output = self.protocol.outputMovies
-                return [self.objectView(output, viewParams=viewParamsDef)]
-            else:
-                return [self.errorMessage('No output movies found!',
-                                          title="Visualization error")]
-
-        elif param == 'doShowFailedMovies':
-            self.failedList = self.protocol._readFailedList()
-            if not self.failedList:
-                return [self.errorMessage('No failed movies found!',
-                                          title="Visualization error")]
-            else:
-                sqliteFn = self.protocol._getPath('movies_failed.sqlite')
-                self.createFailedMoviesSqlite(sqliteFn)
-                return [self.objectView(sqliteFn, viewParams=viewParamsDef)]
-
-    def createFailedMoviesSqlite(self, path):
-        inputMovies = self.protocol.inputMovies.get()
-        cleanPath(path)
-        movieSet = SetOfMovies(filename=path)
-        movieSet.copyInfo(inputMovies)
-        movieSet.copyItems(inputMovies,
-                           updateItemCallback=self._findFailedMovies)
-
-        movieSet.write()
-        movieSet.close()
-
-        return movieSet
-
-    def _findFailedMovies(self, item, row):
-        if item.getObjId() not in self.failedList:
-            setattr(item, "_appendItem", False)
-
-    def _plotMotion(self, param=None):
-        if self.hasDWMics():
-            output = self.protocol.outputMicrographsDoseWeighted
-            columns = '_rlnAccumMotionTotal _rlnAccumMotionEarly _rlnAccumMotionLate'
-            xplotter = EmPlotter.createFromFile(output.getFileName(), '',
-                                                plotType='Plot',
-                                                columnsStr=columns,
-                                                colorsStr='r g b',
-                                                linesStr='- - -',
-                                                markersStr='. . .',
-                                                xcolumn='id',
-                                                ylabel='Motion per frame (A)',
-                                                xlabel='Micrograph id',
-                                                title='Accumulated motion per frame',
-                                                bins=False,
-                                                orderColumn='id',
-                                                orderDirection='ASC')
-            return [xplotter]
-        else:
-            return [self.errorMessage('Plot is available only when dose weighting is ON',
-                                      title="Visualization error")]
+        self._load()
+        return {'displayVol': self._showVolumes,
+                'showMovie': self._showMovie
+                }
+
+    def _createVolumesSqlite(self):
+        """ Write an sqlite with all volumes selected for visualization. """
+        path = self.protocol._getExtraPath('relion_viewer_volumes.sqlite')
+        samplingRate = self.protocol.protRefine.get()._getInputParticles().getSamplingRate()
+
+        files = []
+        volumes = self._getVolumeNames()
+        for volFn in volumes:
+            if not os.path.exists(volFn.replace(':mrc', '')):
+                raise Exception("Missing volume file: %s\n Please select "
+                                "a valid class or iteration number."
+                                % volFn)
+            print("Adding vol: %s" % volFn)
+            files.append(volFn)
+
+        self.createVolumesSqlite(files, path, samplingRate)
+        return [ObjectView(self._project, self.protocol.strId(), path)]
+
+    def _getVolumeNames(self):
+        vols = []
+        prefixes = self._getVolumePrefixes()
+        num = self.protocol._getNumberOfBodies()
+        print("self._iterations: ", self._iterations)
+        for it in self._iterations:
+            for ref3d in range(1, num+1):
+                for prefix in prefixes:
+                    volFn = self.protocol._getFileName(prefix + 'volume_mbody',
+                                                       iter=it, ref3d=ref3d)
+                    if os.path.exists(volFn.replace(':mrc', '')):
+                        vols.append(volFn)
+                    else:
+                        raise Exception("Volume %s does not exists. \n"
+                                        "Please select a valid iteration "
+                                        "number." % volFn)
+        return vols
+
+    @protected_show
+    def _showMovie(self, paramName=None):
+        """ Create a chimera script to visualize animation. """
+        prot = self.protocol
+        if prot.getStatus() != STATUS_FINISHED:
+            raise Exception("Protocol has not finished yet, results are not ready!")
+
+        compToShow = self.component.get()
+        totalComp = prot.numberOfEigenvectors.get()
+        if compToShow > totalComp:
+            raise Exception("You only have %d components!" % totalComp)
+
+        vols = "analyse_component%03d_bin*.mrc" % compToShow
+        cmdFile = prot._getExtraPath('chimera_animation_comp%d.cxc' % compToShow)
+
+        with open(cmdFile, 'w') as f:
+            f.write("open %s vseries true\n" % vols)
+            f.write('vseries play #1 loop true direction oscillate\n')
+
+        views = ChimeraView(cmdFile)
+
+        return [views]
```

### Comparing `scipion-em-relion-4.0b7/relion/viewers/viewer_polishing.py` & `scipion-em-relion-4.0b8/relion/viewers/viewer_polishing.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/viewers/viewer_postprocess.py` & `scipion-em-relion-4.0b8/relion/viewers/viewer_postprocess.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/relion/wizards.py` & `scipion-em-relion-4.0b8/relion/wizards.py`

 * *Files identical despite different names*

### Comparing `scipion-em-relion-4.0b7/scipion_em_relion.egg-info/PKG-INFO` & `scipion-em-relion-4.0b8/scipion_em_relion.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: scipion-em-relion
-Version: 4.0b7
+Version: 4.0b8
 Summary: Plugin to use Relion programs within the Scipion framework
 Home-page: https://github.com/scipion-em/scipion-em-relion
 Author: Grigory Sharov, J.M. De la Rosa Trevin, Josue Gomez Blanco
 Author-email: gsharov@mrc-lmb.cam.ac.uk, delarosatrevin@scilifelab.se, josue.gomez-blanco@mcgill.ca
 License: UNKNOWN
 Project-URL: Bug Reports, https://github.com/scipion-em/scipion-em-relion/issues
 Project-URL: Source, https://github.com/scipion-em/scipion-em-relion/
@@ -72,15 +72,15 @@
         - If you want to use **2D class ranker** protocol, you also need to set *RELION_PYTHON* that points to a Python which includes torch and numpy modules.
         
         To check the installation, simply run one of the tests. A complete list of tests can be displayed by executing ``scipion test --show --grep relion``
         
         Supported versions
         ------------------
         
-        3.1.0, 3.1.1, 3.1.2, 3.1.3, 4.0
+        3.1.3, 4.0
         
         Protocols
         ---------
         
         * 2D class ranker
         * 2D classification         
         * 3D auto-refine
```

### Comparing `scipion-em-relion-4.0b7/scipion_em_relion.egg-info/SOURCES.txt` & `scipion-em-relion-4.0b8/scipion_em_relion.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -31,19 +31,19 @@
 relion/protocols/protocol_autopick_log.py
 relion/protocols/protocol_autopick_ref.py
 relion/protocols/protocol_base.py
 relion/protocols/protocol_bayesian_polishing.py
 relion/protocols/protocol_center_averages.py
 relion/protocols/protocol_classify2d.py
 relion/protocols/protocol_classify3d.py
-relion/protocols/protocol_compress_estimate_gain.py
 relion/protocols/protocol_compress_movies.py
 relion/protocols/protocol_create_mask3d.py
 relion/protocols/protocol_crop_resize.py
 relion/protocols/protocol_ctf_refinement.py
+relion/protocols/protocol_estimate_gain.py
 relion/protocols/protocol_expand_symmetry.py
 relion/protocols/protocol_export_coords.py
 relion/protocols/protocol_export_ctf.py
 relion/protocols/protocol_export_particles.py
 relion/protocols/protocol_extract_particles.py
 relion/protocols/protocol_gentle_clean.py
 relion/protocols/protocol_initialmodel.py
```

### Comparing `scipion-em-relion-4.0b7/setup.py` & `scipion-em-relion-4.0b8/setup.py`

 * *Files identical despite different names*

