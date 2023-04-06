# Comparing `tmp/Simba-UW-tf-dev-1.55.1.tar.gz` & `tmp/Simba-UW-tf-dev-1.55.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/Simba-UW-tf-dev-1.55.1.tar", last modified: Thu Apr  6 01:08:38 2023, max compression
+gzip compressed data, was "dist/Simba-UW-tf-dev-1.55.2.tar", last modified: Thu Apr  6 19:53:42 2023, max compression
```

## Comparing `Simba-UW-tf-dev-1.55.1.tar` & `Simba-UW-tf-dev-1.55.2.tar`

### file list

```diff
@@ -1,379 +1,380 @@
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/
--rw-r--r--   0 simon      (501) staff       (20)      579 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/PKG-INFO
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/
--rw-r--r--   0 simon      (501) staff       (20)    32569 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.1/simba/video_processing.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/blob_storage/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-21 20:39:46.000000 Simba-UW-tf-dev-1.55.1/simba/blob_storage/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/
--rw-r--r--   0 simon      (501) staff       (20)    10851 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/unsupervised_ui.py
--rw-r--r--   0 simon      (501) staff       (20)     6566 2023-03-21 14:26:03.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/misc.py
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     7227 2023-03-21 11:41:26.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/dataset_creator.py
--rw-r--r--   0 simon      (501) staff       (20)     4061 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/data_extractors.py
--rw-r--r--   0 simon      (501) staff       (20)    11192 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/dbcv.py
--rw-r--r--   0 simon      (501) staff       (20)    11456 2023-03-21 18:17:26.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/visualizers.py
--rw-r--r--   0 simon      (501) staff       (20)     7526 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/umap_embedder.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/visualization_tools/
--rw-r--r--   0 simon      (501) staff       (20)     2019 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/visualization_tools/vtk_embeddings.py
--rw-r--r--   0 simon      (501) staff       (20)      150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/ui_tools.py
--rw-r--r--   0 simon      (501) staff       (20)    49992 2023-03-22 15:08:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/pop_up_classes.py
--rw-r--r--   0 simon      (501) staff       (20)    16189 2023-03-21 15:42:27.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/cluster_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)     6642 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/hdbscan_clusterer.py
--rw-r--r--   0 simon      (501) staff       (20)     3789 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/tsne.py
--rw-r--r--   0 simon      (501) staff       (20)     5630 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/unsupervised/cluster_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    18493 2023-04-06 00:17:28.000000 Simba-UW-tf-dev-1.55.1/simba/enums.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     7463 2023-03-15 19:17:12.000000 Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/agg_boundary_stats.py
--rw-r--r--   0 simon      (501) staff       (20)     8562 2023-03-15 19:17:04.000000 Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/find_bounderies.py
--rw-r--r--   0 simon      (501) staff       (20)    24434 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/boundary_menus.py
--rw-r--r--   0 simon      (501) staff       (20)     9530 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/boundary_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)    12627 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/visualize_boundaries.py
--rw-r--r--   0 simon      (501) staff       (20)    32772 2023-04-04 14:38:01.000000 Simba-UW-tf-dev-1.55.1/simba/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/
--rw-r--r--   0 simon      (501) staff       (20)    42807 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_14bp.py
--rw-r--r--   0 simon      (501) staff       (20)    21541 2023-03-15 19:11:32.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_7bp.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/
--rw-r--r--   0 simon      (501) staff       (20)     2732 2023-04-04 19:46:36.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/read_in_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    14141 2023-03-15 17:20:08.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/fish_feature_extractor_2022.py
--rw-r--r--   0 simon      (501) staff       (20)     2053 2023-04-04 03:00:41.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/convex_hull_3_scratch_3.py
--rw-r--r--   0 simon      (501) staff       (20)     5762 2023-04-04 01:54:33.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/convex_hull_scratch_1.py
--rw-r--r--   0 simon      (501) staff       (20)    19620 2023-04-03 12:08:14.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/fish_feature_extractor_2023.py
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 19:36:02.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     7127 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/egocentrical_aligner.py
--rw-r--r--   0 simon      (501) staff       (20)     4708 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/graph_creator.py
--rw-r--r--   0 simon      (501) staff       (20)     3954 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/termite_rois.csv
--rw-r--r--   0 simon      (501) staff       (20)      732 2023-03-20 12:13:51.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/mutual_exclusive.py
--rw-r--r--   0 simon      (501) staff       (20)     1862 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/graph_3d_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)     2692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/add_probability_cnt_features.py
--rw-r--r--   0 simon      (501) staff       (20)     2058 2023-04-03 23:51:37.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/convex_hull_scratch_2.py
--rw-r--r--   0 simon      (501) staff       (20)    28028 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_8bps_2_animals.py
--rw-r--r--   0 simon      (501) staff       (20)    10244 2023-04-06 00:34:11.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     2347 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/perimeter_jit.py
--rw-r--r--   0 simon      (501) staff       (20)     9386 2023-04-05 13:10:58.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_subsets.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__init__.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/
--rw-r--r--   0 simon      (501) staff       (20)      905 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi
--rw-r--r--   0 simon      (501) staff       (20)   238196 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc
--rw-r--r--   0 simon      (501) staff       (20)    69038 2023-04-04 11:32:25.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc
--rw-r--r--   0 simon      (501) staff       (20)   238298 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc
--rw-r--r--   0 simon      (501) staff       (20)    69338 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc
--rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi
--rw-r--r--   0 simon      (501) staff       (20)     2179 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi
--rw-r--r--   0 simon      (501) staff       (20)    36798 2023-03-15 17:04:48.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/extract_features_9bp.py
--rw-r--r--   0 simon      (501) staff       (20)     8428 2023-03-15 19:11:54.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_user_defined.py
--rw-r--r--   0 simon      (501) staff       (20)     5323 2023-03-19 18:30:53.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/unit_tests.py
--rw-r--r--   0 simon      (501) staff       (20)    46473 2023-04-04 13:07:58.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_16bp.py
--rw-r--r--   0 simon      (501) staff       (20)    24093 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_8bp.py
--rw-r--r--   0 simon      (501) staff       (20)    16763 2023-03-15 19:11:50.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_4bp.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/
--rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/features_scripts.iml
--rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/encodings.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/inspectionProfiles/
--rw-r--r--   0 simon      (501) staff       (20)      822 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/libraries/
--rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/libraries/R_User_Library.xml
--rw-r--r--   0 simon      (501) staff       (20)      273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/.gitignore
--rw-r--r--   0 simon      (501) staff       (20)     8081 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/workspace.xml
--rw-r--r--   0 simon      (501) staff       (20)      291 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/modules.xml
--rw-r--r--   0 simon      (501) staff       (20)       23 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/.name
--rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/misc.xml
--rw-r--r--   0 simon      (501) staff       (20)     6044 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/plotly_create_h5.py
--rw-r--r--   0 simon      (501) staff       (20)    15348 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/requirements.txt
--rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-15 19:16:48.000000 Simba-UW-tf-dev-1.55.1/simba/severity_processor.py
--rw-r--r--   0 simon      (501) staff       (20)     5941 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.1/simba/user_pose_config_creator.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/mixins/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:26:03.000000 Simba-UW-tf-dev-1.55.1/simba/mixins/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    41856 2023-04-05 17:24:50.000000 Simba-UW-tf-dev-1.55.1/simba/mixins/pop_up_mixin.py
--rw-r--r--   0 simon      (501) staff       (20)     8182 2023-04-05 13:03:24.000000 Simba-UW-tf-dev-1.55.1/simba/mixins/config_reader.py
--rw-r--r--   0 simon      (501) staff       (20)     5140 2023-04-05 13:03:25.000000 Simba-UW-tf-dev-1.55.1/simba/mixins/feature_extraction_mixin.py
--rw-r--r--   0 simon      (501) staff       (20)    34347 2023-04-05 20:27:12.000000 Simba-UW-tf-dev-1.55.1/simba/machine_model_settings_pop_up.py
--rw-r--r--   0 simon      (501) staff       (20)     5266 2023-03-15 15:43:20.000000 Simba-UW-tf-dev-1.55.1/simba/remove_keypoints_in_pose.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/
--rw-r--r--   0 simon      (501) staff       (20)     6326 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/deepethogram_importer.py
--rw-r--r--   0 simon      (501) staff       (20)     9947 2023-03-18 15:35:38.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/BORIS_appender.py
--rw-r--r--   0 simon      (501) staff       (20)     9170 2023-03-22 19:35:38.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/observer_importer.py
--rw-r--r--   0 simon      (501) staff       (20)    16922 2023-03-28 20:30:38.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/tools.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-04-01 14:10:06.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)    18283 2023-04-01 14:14:21.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/third_party_appender.py
--rw-r--r--   0 simon      (501) staff       (20)     8336 2023-03-15 19:12:46.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/ethovision_import.py
--rw-r--r--   0 simon      (501) staff       (20)     6919 2023-03-19 15:03:14.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/BENTO_appender.py
--rw-r--r--   0 simon      (501) staff       (20)     5426 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/solomon_importer.py
--rw-r--r--   0 simon      (501) staff       (20)     7261 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/multi_cropper.py
--rw-r--r--   0 simon      (501) staff       (20)    13056 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.1/simba/FSTTC_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)    12627 2023-04-06 00:17:28.000000 Simba-UW-tf-dev-1.55.1/simba/create_project_pop_up.py
--rw-r--r--   0 simon      (501) staff       (20)    13266 2023-03-19 20:04:35.000000 Simba-UW-tf-dev-1.55.1/simba/video_info_table.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:25:58.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     8507 2023-03-15 19:09:16.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_clf_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)    13530 2023-03-15 19:08:52.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    19562 2023-03-15 16:59:44.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_menues.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)     1660 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_tools.py
--rw-r--r--   0 simon      (501) staff       (20)    16374 2023-03-15 19:09:04.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    13160 2023-03-20 13:43:59.000000 Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_movement_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)     2813 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/extract_frames_fast.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/utils/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 20:15:03.000000 Simba-UW-tf-dev-1.55.1/simba/utils/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     5626 2023-03-28 20:35:14.000000 Simba-UW-tf-dev-1.55.1/simba/utils/warnings.py
--rw-r--r--   0 simon      (501) staff       (20)     3466 2023-03-28 19:21:28.000000 Simba-UW-tf-dev-1.55.1/simba/utils/lookups.py
--rw-r--r--   0 simon      (501) staff       (20)    11857 2023-03-28 17:56:16.000000 Simba-UW-tf-dev-1.55.1/simba/utils/errors.py
--rw-r--r--   0 simon      (501) staff       (20)    21581 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/labelling_interface.py
--rw-r--r--   0 simon      (501) staff       (20)     9937 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.1/simba/timebins_movement_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    45524 2023-04-04 20:09:14.000000 Simba-UW-tf-dev-1.55.1/simba/train_model_functions.py
--rw-r--r--   0 simon      (501) staff       (20)    49699 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/SimBA_dash_app.py
--rw-r--r--   0 simon      (501) staff       (20)     7520 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.1/simba/timebins_clf_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     8240 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.1/simba/calculate_px_dist.py
--rw-r--r--   0 simon      (501) staff       (20)     6548 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/movement_processor.py
--rw-r--r--   0 simon      (501) staff       (20)     2904 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pybursts.py
--rw-r--r--   0 simon      (501) staff       (20)     5265 2023-03-29 18:04:02.000000 Simba-UW-tf-dev-1.55.1/simba/run_model_new.py
--rw-r--r--   0 simon      (501) staff       (20)     3104 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/rw_dfs.py
--rw-r--r--   0 simon      (501) staff       (20)     6684 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/reverse_2_animal_tracking.py
--rw-r--r--   0 simon      (501) staff       (20)     9743 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.1/simba/Directing_animals_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     4357 2023-03-30 16:19:09.000000 Simba-UW-tf-dev-1.55.1/simba/Validate_model_one_video_run_clf.py
--rw-r--r--   0 simon      (501) staff       (20)     9548 2023-04-06 00:40:25.000000 Simba-UW-tf-dev-1.55.1/simba/tkinter_functions.py
--rw-r--r--   0 simon      (501) staff       (20)    13767 2023-03-24 12:49:19.000000 Simba-UW-tf-dev-1.55.1/simba/setting_menu.py
--rw-r--r--   0 simon      (501) staff       (20)     6614 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/interpolate_pose.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/
--rw-r--r--   0 simon      (501) staff       (20)     8571 2023-03-30 10:06:59.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/gantt_creator.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/tools/
--rw-r--r--   0 simon      (501) staff       (20)     5353 2023-03-30 15:38:37.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/tools/tkinter_tools.py
--rw-r--r--   0 simon      (501) staff       (20)    17962 2023-03-24 13:40:30.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_plotter_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    14592 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/shap_agg_stats_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    12928 2023-03-30 10:08:46.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/gantt_creator_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    15777 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_clf_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     8884 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/probability_plot_creator.py
--rw-r--r--   0 simon      (501) staff       (20)    16058 2023-03-22 14:43:52.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/misc_visualizations.py
--rw-r--r--   0 simon      (501) staff       (20)    13501 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/plot_clf_results.py
--rw-r--r--   0 simon      (501) staff       (20)    17696 2023-03-29 16:22:09.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/plot_clf_results_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    16328 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_feature_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    12588 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_location.py
--rw-r--r--   0 simon      (501) staff       (20)    12585 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/probability_plot_creator_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     5341 2023-03-30 15:46:49.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/interactive_probability_grapher.py
--rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-29 17:02:51.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/plot_pose_in_dir.py
--rw-r--r--   0 simon      (501) staff       (20)    12184 2023-03-31 13:53:09.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/single_run_model_validation_video.py
--rw-r--r--   0 simon      (501) staff       (20)    11202 2023-03-19 16:21:53.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/frame_mergerer_ffmpeg.py
--rw-r--r--   0 simon      (501) staff       (20)    12442 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/Directing_animals_visualizer_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     9856 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/clf_validator.py
--rw-r--r--   0 simon      (501) staff       (20)    17290 2023-04-06 00:33:50.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/path_plotter_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    19958 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_feature_visualizer_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    10157 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/data_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)    12444 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/path_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)     8609 2023-03-15 13:37:59.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/ez_lineplot.py
--rw-r--r--   0 simon      (501) staff       (20)    12970 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/distance_plotter_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    15626 2023-03-29 17:05:49.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)    13165 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_clf.py
--rw-r--r--   0 simon      (501) staff       (20)     8891 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/distance_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)    13554 2023-04-01 13:12:31.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/single_run_model_validation_video_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     9839 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/Directing_animals_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    16155 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_location_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     5029 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/run_dash_tkinter.py
--rw-r--r--   0 simon      (501) staff       (20)     7454 2023-03-13 22:11:36.000000 Simba-UW-tf-dev-1.55.1/simba/interpolate_smooth_post_hoc.py
--rw-r--r--   0 simon      (501) staff       (20)    24474 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/dash_app.py
--rw-r--r--   0 simon      (501) staff       (20)     6350 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/reverse_tracking_order.py
--rw-r--r--   0 simon      (501) staff       (20)     5772 2023-03-20 13:55:20.000000 Simba-UW-tf-dev-1.55.1/simba/concatenator_pop_up.py
--rw-r--r--   0 simon      (501) staff       (20)     2824 2023-03-24 16:12:51.000000 Simba-UW-tf-dev-1.55.1/simba/extract_annotation_frames.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/
--rw-r--r--   0 simon      (501) staff       (20)     7385 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_time_bin_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)     2248 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_movement_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-20 12:47:56.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    43831 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_define.py
--rw-r--r--   0 simon      (501) staff       (20)     3384 2023-03-20 12:41:16.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_reset.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)    21382 2023-03-31 10:40:20.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    11920 2023-03-31 10:48:40.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_feature_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     3537 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_multiply.py
--rw-r--r--   0 simon      (501) staff       (20)      961 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_size_calculations.py
--rw-r--r--   0 simon      (501) staff       (20)     3505 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_zoom.py
--rw-r--r--   0 simon      (501) staff       (20)    11335 2023-04-05 11:07:42.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_directing_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    10128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_move_shape.py
--rw-r--r--   0 simon      (501) staff       (20)     5097 2023-04-05 20:01:02.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_menus.py
--rw-r--r--   0 simon      (501) staff       (20)    15175 2023-03-20 12:28:41.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_clf_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)    22682 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_image.py
--rw-r--r--   0 simon      (501) staff       (20)    57395 2023-04-06 00:28:01.000000 Simba-UW-tf-dev-1.55.1/simba/misc_tools.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/
--rw-r--r--   0 simon      (501) staff       (20)     2494 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/read_DANNCE_mat.py
--rw-r--r--   0 simon      (501) staff       (20)    25782 2023-03-20 12:51:35.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/sleap_importer_slp.py
--rw-r--r--   0 simon      (501) staff       (20)    24720 2023-03-13 15:26:36.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/sleap_importer_h5.py
--rw-r--r--   0 simon      (501) staff       (20)    26507 2023-03-21 12:58:39.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/dlc_multi_animal_importer.py
--rw-r--r--   0 simon      (501) staff       (20)    23731 2023-03-20 12:55:04.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/sleap_importer_csv.py
--rw-r--r--   0 simon      (501) staff       (20)    16536 2023-03-20 13:30:18.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/import_trk.py
--rw-r--r--   0 simon      (501) staff       (20)     7837 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/import_mars.py
--rw-r--r--   0 simon      (501) staff       (20)     8905 2023-03-20 13:49:13.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/dlc_importer_csv.py
--rw-r--r--   0 simon      (501) staff       (20)     8173 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_importers/trk_importer.py
--rw-r--r--   0 simon      (501) staff       (20)   232785 2023-04-06 00:45:09.000000 Simba-UW-tf-dev-1.55.1/simba/pop_up_classes.py
--rw-r--r--   0 simon      (501) staff       (20)     4692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/extract_seqframes.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/
--rw-r--r--   0 simon      (501) staff       (20)    14340 2023-03-30 11:05:37.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/bp_names/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:00.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/bp_names/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     1316 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/bp_names/bp_names.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/no_animals/
--rw-r--r--   0 simon      (501) staff       (20)       24 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/no_animals/no_animals.csv
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:19.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/no_animals/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/configuration_names/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:14.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/configuration_names/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)      267 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/configuration_names/pose_config_names.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-30 10:45:10.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    39805 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/8.png
--rw-r--r--   0 simon      (501) staff       (20)    62501 2023-03-30 10:39:05.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/9.png
--rw-r--r--   0 simon      (501) staff       (20)     6172 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/12.png
--rw-r--r--   0 simon      (501) staff       (20)    69501 2023-03-30 10:44:04.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/11.png
--rw-r--r--   0 simon      (501) staff       (20)    69410 2023-03-30 10:40:01.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/10.png
--rw-r--r--   0 simon      (501) staff       (20)    16000 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/4.png
--rw-r--r--   0 simon      (501) staff       (20)    28150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/5.png
--rw-r--r--   0 simon      (501) staff       (20)    31140 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/7.png
--rw-r--r--   0 simon      (501) staff       (20)    30634 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/6.png
--rw-r--r--   0 simon      (501) staff       (20)    15417 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/2.png
--rw-r--r--   0 simon      (501) staff       (20)    15786 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/3.png
--rw-r--r--   0 simon      (501) staff       (20)    18939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/1.png
--rw-r--r--   0 simon      (501) staff       (20)     7273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/get_coordinates_tools_v2.py
--rw-r--r--   0 simon      (501) staff       (20)    16252 2023-03-15 19:16:56.000000 Simba-UW-tf-dev-1.55.1/simba/pup_retrieval_protocol.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/
--rw-r--r--   0 simon      (501) staff       (20)     7712 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/outlier_corrector_movement.py
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-15 17:05:05.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)     8264 2023-03-15 17:05:35.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/outlier_corrector_location.py
--rw-r--r--   0 simon      (501) staff       (20)     4362 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/skip_outlier_correction.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/
--rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/outlier_scripts.iml
--rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/encodings.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/inspectionProfiles/
--rw-r--r--   0 simon      (501) staff       (20)      668 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/libraries/
--rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/libraries/R_User_Library.xml
--rw-r--r--   0 simon      (501) staff       (20)     8102 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/workspace.xml
--rw-r--r--   0 simon      (501) staff       (20)      289 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/modules.xml
--rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/misc.xml
--rw-r--r--   0 simon      (501) staff       (20)     2569 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/pose_reset.py
--rw-r--r--   0 simon      (501) staff       (20)    17642 2023-04-04 23:10:52.000000 Simba-UW-tf-dev-1.55.1/simba/train_mutiple_models.py
--rw-r--r--   0 simon      (501) staff       (20)    59794 2023-04-06 00:38:56.000000 Simba-UW-tf-dev-1.55.1/simba/SimBA.py
--rw-r--r--   0 simon      (501) staff       (20)    27431 2023-04-04 14:39:01.000000 Simba-UW-tf-dev-1.55.1/simba/labelling_advanced_interface.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/unsupervised/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/unsupervised/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)   109483 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/unsupervised/model_names.parquet
--rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/unsupervised/features.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/
--rw-r--r--   0 simon      (501) staff       (20)     1177 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/down_arrow.jpg
--rw-r--r--   0 simon      (501) staff       (20)     1733 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/intruder_shape.jpg
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/feature_categories/
--rw-r--r--   0 simon      (501) staff       (20)      109 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/feature_categories/.~lock.shap_feature_categories.csv#
--rw-r--r--   0 simon      (501) staff       (20)    17420 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/feature_categories/shap_feature_categories.csv
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     1665 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_shape.jpg
--rw-r--r--   0 simon      (501) staff       (20)     2415 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_intruder_shape.jpg
--rw-r--r--   0 simon      (501) staff       (20)     2012 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/animal_distances.jpg
--rw-r--r--   0 simon      (501) staff       (20)     4422 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/baseline_scale.jpg
--rw-r--r--   0 simon      (501) staff       (20)   353824 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/ubuntu.regular.ttf
--rw-r--r--   0 simon      (501) staff       (20)     6672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/side_scale.jpg
--rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/UbuntuMono-Regular.ttf
--rw-r--r--   0 simon      (501) staff       (20)     2737 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/side_scale_5.jpg
--rw-r--r--   0 simon      (501) staff       (20)     1785 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/intruder_movement.jpg
--rw-r--r--   0 simon      (501) staff       (20)     1435 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_movement.jpg
--rw-r--r--   0 simon      (501) staff       (20)     3134 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/color_bar.jpg
--rw-r--r--   0 simon      (501) staff       (20)     2120 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_intruder_movement.jpg
--rw-r--r--   0 simon      (501) staff       (20)    16388 2023-04-05 16:43:31.000000 Simba-UW-tf-dev-1.55.1/simba/assets/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/lookups/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/lookups/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)   270783 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/lookups/model_names.parquet
--rw-r--r--   0 simon      (501) staff       (20)     2426 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/lookups/feature_extraction_headers.csv
--rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/lookups/features.csv
--rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/lookups/unsupervised_example_x.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/stl/
--rw-r--r--   0 simon      (501) staff       (20)   551576 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/stl/operant_tray.stl
--rw-r--r--   0 simon      (501) staff       (20)    67647 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/stl/operant_lever.stl
--rw-r--r--   0 simon      (501) staff       (20)    92896 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/stl/operant_walls.stl
--rw-r--r--   0 simon      (501) staff       (20)  4759984 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/stl/grid_floor.stl
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/img/
--rw-r--r--   0 simon      (501) staff       (20)   399272 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/img/about_me.png
--rw-r--r--   0 simon      (501) staff       (20)   454535 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/img/splash.png
--rw-r--r--   0 simon      (501) staff       (20)    69267 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/img/splash.pptx
--rw-r--r--   0 simon      (501) staff       (20)    79664 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/img/bg.png
--rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/UbuntuMono-Regular.ttf
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/
--rw-r--r--   0 simon      (501) staff       (20)     1350 2023-03-17 17:59:27.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/factory.png
--rw-r--r--   0 simon      (501) staff       (20)     1413 2023-03-21 13:03:06.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/cluster.png
--rw-r--r--   0 simon      (501) staff       (20)     1340 2023-03-17 16:51:08.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/load.png
--rw-r--r--   0 simon      (501) staff       (20)     4507 2023-03-20 14:13:48.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/gif.png
--rw-rw-r--   0 simon      (501) staff       (20)     4566 2023-03-18 18:12:27.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/pose.png
--rw-rw-r--   0 simon      (501) staff       (20)     1943 2023-03-18 18:14:10.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/features.png
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-04-05 17:25:36.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/.DS_Store
--rw-rw-r--   0 simon      (501) staff       (20)     4896 2023-03-17 19:17:29.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/settings.png
--rw-r--r--   0 simon      (501) staff       (20)     1252 2023-03-19 16:48:40.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/link.png
--rw-r--r--   0 simon      (501) staff       (20)    14250 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/dash_simba.css
--rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-05 16:43:13.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/documentation.png
--rw-r--r--   0 simon      (501) staff       (20)     4503 2023-03-20 14:08:00.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/fps.png
--rw-r--r--   0 simon      (501) staff       (20)     1299 2023-03-21 13:02:07.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/dimensionality_reduction.png
--rw-rw-r--   0 simon      (501) staff       (20)     4823 2023-03-17 19:03:29.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/roi.png
--rw-r--r--   0 simon      (501) staff       (20)      920 2023-03-20 14:25:03.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/superimpose.png
--rw-r--r--   0 simon      (501) staff       (20)     1136 2023-03-18 20:25:31.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/label.png
--rw-r--r--   0 simon      (501) staff       (20)     1016 2023-03-20 14:28:47.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/change.png
--rw-r--r--   0 simon      (501) staff       (20)     1124 2023-03-17 18:05:26.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/crop.png
--rw-r--r--   0 simon      (501) staff       (20)     1057 2023-03-20 14:03:42.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/path.png
--rw-r--r--   0 simon      (501) staff       (20)      950 2023-03-17 18:07:33.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/clip.png
--rw-r--r--   0 simon      (501) staff       (20)     2121 2023-04-04 14:37:43.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/restart.png
--rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-17 18:11:59.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/calipher.png
--rw-r--r--   0 simon      (501) staff       (20)     1291 2023-03-21 20:16:55.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/add_on.png
--rw-rw-r--   0 simon      (501) staff       (20)     4695 2023-03-17 17:57:16.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/create.png
--rw-r--r--   0 simon      (501) staff       (20)    78182 2023-03-20 16:35:36.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/SimBA_logo.ico
--rw-r--r--   0 simon      (501) staff       (20)     1067 2023-03-20 14:22:44.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/print.png
--rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-18 20:27:58.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/clf.png
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/
--rw-r--r--   0 simon      (501) staff       (20)     6027 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/mosaic.png
--rw-r--r--   0 simon      (501) staff       (20)     5654 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/vertical.png
--rw-r--r--   0 simon      (501) staff       (20)     5542 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/horizontal.png
--rw-r--r--   0 simon      (501) staff       (20)     5939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/mixed_mosaic.png
--rw-r--r--   0 simon      (501) staff       (20)     2060 2023-03-20 14:26:12.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/merge.png
--rw-------   0 simon      (501) staff       (20)     4725 2023-03-18 20:27:47.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/clf_2.png
--rw-rw-r--   0 simon      (501) staff       (20)     4795 2023-03-17 18:10:10.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/visualize.png
--rw-r--r--   0 simon      (501) staff       (20)     2142 2023-03-20 14:10:28.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat.png
--rw-r--r--   0 simon      (501) staff       (20)     1474 2023-03-17 19:20:24.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/boris.png
--rw-rw-r--   0 simon      (501) staff       (20)     4804 2023-03-19 16:43:01.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/frames.png
--rw-r--r--   0 simon      (501) staff       (20)     2425 2023-03-19 16:44:55.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/video.png
--rw-r--r--   0 simon      (501) staff       (20)     2089 2023-03-20 14:05:58.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/sample.png
--rw-r--r--   0 simon      (501) staff       (20)     1471 2023-03-21 13:04:02.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/metrics.png
--rw-r--r--   0 simon      (501) staff       (20)     4555 2023-03-20 14:21:02.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/grey.png
--rw-r--r--   0 simon      (501) staff       (20)      930 2023-03-18 18:07:29.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/exit.png
--rw-r--r--   0 simon      (501) staff       (20)     4751 2023-03-18 20:31:58.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/outlier.png
--rw-r--r--   0 simon      (501) staff       (20)     4392 2023-03-20 14:16:15.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/clahe.png
--rw-rw-r--   0 simon      (501) staff       (20)     4637 2023-03-17 19:03:55.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/trash.png
--rw-r--r--   0 simon      (501) staff       (20)     1239 2023-03-19 16:51:21.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/about.png
--rw-rw-r--   0 simon      (501) staff       (20)     4666 2023-03-17 18:01:21.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/convert.png
--rw-r--r--   0 simon      (501) staff       (20)    93229 2023-03-20 16:01:42.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/SimBA_logo.icns
--rw-r--r--   0 simon      (501) staff       (20)      991 2023-03-20 19:02:33.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/reorganize.png
--rw-rw-r--   0 simon      (501) staff       (20)     4784 2023-03-17 18:50:35.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/browse.png
--rw-r--r--   0 simon      (501) staff       (20)    30707 2023-03-20 16:33:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/SimBA_logo.png
--rw-r--r--   0 simon      (501) staff       (20)     2293 2023-03-17 19:24:38.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/ethovision.png
--rw-r--r--   0 simon      (501) staff       (20)     1018 2023-04-05 15:24:49.000000 Simba-UW-tf-dev-1.55.1/simba/assets/icons/close.png
--rw-r--r--   0 simon      (501) staff       (20)    13672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/dash_simba_base.css
--rw-r--r--   0 simon      (501) staff       (20)    31812 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/assets/TheGoldenLab.PNG
--rw-r--r--   0 simon      (501) staff       (20)    21392 2023-03-22 19:01:48.000000 Simba-UW-tf-dev-1.55.1/simba/drop_bp_cords.py
--rw-r--r--   0 simon      (501) staff       (20)     8116 2023-03-19 18:27:51.000000 Simba-UW-tf-dev-1.55.1/simba/read_config_unit_tests.py
--rw-r--r--   0 simon      (501) staff       (20)    11564 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/project_config_creator.py
--rw-r--r--   0 simon      (501) staff       (20)    27444 2023-03-15 15:58:40.000000 Simba-UW-tf-dev-1.55.1/simba/set_hyperparameters.py
--rw-r--r--   0 simon      (501) staff       (20)    20780 2023-04-04 23:58:36.000000 Simba-UW-tf-dev-1.55.1/simba/train_single_model.py
--rw-r--r--   0 simon      (501) staff       (20)     6426 2023-03-17 16:57:53.000000 Simba-UW-tf-dev-1.55.1/simba/create_clf_log.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-17 14:43:38.000000 Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    24806 2023-03-19 20:13:19.000000 Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/batch_process_menus.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)    10936 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py
--rw-r--r--   0 simon      (501) staff       (20)     9563 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.1/simba/Kleinberg_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)     8392 2023-04-03 14:06:05.000000 Simba-UW-tf-dev-1.55.1/simba/reorganize_keypoint_in_pose.py
--rw-r--r--   0 simon      (501) staff       (20)      165 2023-03-25 11:18:21.000000 Simba-UW-tf-dev-1.55.1/simba/~$features.pptx
--rw-r--r--   0 simon      (501) staff       (20)     6557 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.1/simba/play_annotation_video.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/
--rw-rw-r--   0 simon      (501) staff       (20)      579 2023-04-06 01:08:37.000000 Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/PKG-INFO
--rw-rw-r--   0 simon      (501) staff       (20)    12823 2023-04-06 01:08:37.000000 Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/SOURCES.txt
--rw-rw-r--   0 simon      (501) staff       (20)       44 2023-04-06 01:08:37.000000 Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/entry_points.txt
--rw-rw-r--   0 simon      (501) staff       (20)      640 2023-04-06 01:08:37.000000 Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/requires.txt
--rw-rw-r--   0 simon      (501) staff       (20)        6 2023-04-06 01:08:37.000000 Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/top_level.txt
--rw-rw-r--   0 simon      (501) staff       (20)        1 2023-04-06 01:08:37.000000 Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/dependency_links.txt
--rw-rw-r--   0 simon      (501) staff       (20)     7652 2020-05-13 13:27:38.000000 Simba-UW-tf-dev-1.55.1/LICENSE.md
--rw-rw-r--   0 simon      (501) staff       (20)      136 2021-04-10 10:44:06.000000 Simba-UW-tf-dev-1.55.1/MANIFEST.in
--rw-rw-r--   0 simon      (501) staff       (20)     9598 2020-05-13 13:27:40.000000 Simba-UW-tf-dev-1.55.1/README.md
--rw-rw-r--   0 simon      (501) staff       (20)     1897 2023-04-06 00:33:50.000000 Simba-UW-tf-dev-1.55.1/setup.py
--rw-r--r--   0 simon      (501) staff       (20)       38 2023-04-06 01:08:38.000000 Simba-UW-tf-dev-1.55.1/setup.cfg
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/
+-rw-r--r--   0 simon      (501) staff       (20)      579 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/PKG-INFO
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/
+-rw-r--r--   0 simon      (501) staff       (20)    32569 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.2/simba/video_processing.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/blob_storage/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-21 20:39:46.000000 Simba-UW-tf-dev-1.55.2/simba/blob_storage/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/
+-rw-r--r--   0 simon      (501) staff       (20)    10851 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/unsupervised_ui.py
+-rw-r--r--   0 simon      (501) staff       (20)     6566 2023-03-21 14:26:03.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/misc.py
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     7227 2023-03-21 11:41:26.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/dataset_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)     4061 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/data_extractors.py
+-rw-r--r--   0 simon      (501) staff       (20)    11192 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/dbcv.py
+-rw-r--r--   0 simon      (501) staff       (20)    11456 2023-03-21 18:17:26.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/visualizers.py
+-rw-r--r--   0 simon      (501) staff       (20)     7526 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/umap_embedder.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/visualization_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     2019 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/visualization_tools/vtk_embeddings.py
+-rw-r--r--   0 simon      (501) staff       (20)      150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/ui_tools.py
+-rw-r--r--   0 simon      (501) staff       (20)    49992 2023-03-22 15:08:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/pop_up_classes.py
+-rw-r--r--   0 simon      (501) staff       (20)    16189 2023-03-21 15:42:27.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/cluster_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)     6642 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/hdbscan_clusterer.py
+-rw-r--r--   0 simon      (501) staff       (20)     3789 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/tsne.py
+-rw-r--r--   0 simon      (501) staff       (20)     5630 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/unsupervised/cluster_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    19024 2023-04-06 19:25:58.000000 Simba-UW-tf-dev-1.55.2/simba/enums.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     7463 2023-03-15 19:17:12.000000 Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/agg_boundary_stats.py
+-rw-r--r--   0 simon      (501) staff       (20)     8562 2023-03-15 19:17:04.000000 Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/find_bounderies.py
+-rw-r--r--   0 simon      (501) staff       (20)    24561 2023-04-06 11:22:38.000000 Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/boundary_menus.py
+-rw-r--r--   0 simon      (501) staff       (20)     9530 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/boundary_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)    12627 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/visualize_boundaries.py
+-rw-r--r--   0 simon      (501) staff       (20)    32772 2023-04-04 14:38:01.000000 Simba-UW-tf-dev-1.55.2/simba/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/
+-rw-r--r--   0 simon      (501) staff       (20)    42807 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_14bp.py
+-rw-r--r--   0 simon      (501) staff       (20)    21541 2023-03-15 19:11:32.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_7bp.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/
+-rw-r--r--   0 simon      (501) staff       (20)     2732 2023-04-04 19:46:36.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/read_in_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    14141 2023-03-15 17:20:08.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/fish_feature_extractor_2022.py
+-rw-r--r--   0 simon      (501) staff       (20)     2053 2023-04-04 03:00:41.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/convex_hull_3_scratch_3.py
+-rw-r--r--   0 simon      (501) staff       (20)     5762 2023-04-04 01:54:33.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/convex_hull_scratch_1.py
+-rw-r--r--   0 simon      (501) staff       (20)    19620 2023-04-03 12:08:14.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/fish_feature_extractor_2023.py
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 19:36:02.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     7127 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/egocentrical_aligner.py
+-rw-r--r--   0 simon      (501) staff       (20)     4708 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/graph_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)     3954 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/termite_rois.csv
+-rw-r--r--   0 simon      (501) staff       (20)      732 2023-03-20 12:13:51.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/mutual_exclusive.py
+-rw-r--r--   0 simon      (501) staff       (20)     1862 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/graph_3d_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)     2692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/add_probability_cnt_features.py
+-rw-r--r--   0 simon      (501) staff       (20)     2058 2023-04-03 23:51:37.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/convex_hull_scratch_2.py
+-rw-r--r--   0 simon      (501) staff       (20)    28028 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_8bps_2_animals.py
+-rw-r--r--   0 simon      (501) staff       (20)    10244 2023-04-06 18:38:15.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     2347 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/perimeter_jit.py
+-rw-r--r--   0 simon      (501) staff       (20)    10734 2023-04-06 14:57:55.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_subsets.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__init__.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/
+-rw-r--r--   0 simon      (501) staff       (20)      905 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi
+-rw-r--r--   0 simon      (501) staff       (20)   238196 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc
+-rw-r--r--   0 simon      (501) staff       (20)    69038 2023-04-04 11:32:25.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc
+-rw-r--r--   0 simon      (501) staff       (20)   238298 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc
+-rw-r--r--   0 simon      (501) staff       (20)    69338 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc
+-rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi
+-rw-r--r--   0 simon      (501) staff       (20)     2179 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi
+-rw-r--r--   0 simon      (501) staff       (20)    36798 2023-03-15 17:04:48.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/extract_features_9bp.py
+-rw-r--r--   0 simon      (501) staff       (20)     8428 2023-03-15 19:11:54.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_user_defined.py
+-rw-r--r--   0 simon      (501) staff       (20)     5323 2023-03-19 18:30:53.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/unit_tests.py
+-rw-r--r--   0 simon      (501) staff       (20)    46473 2023-04-04 13:07:58.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_16bp.py
+-rw-r--r--   0 simon      (501) staff       (20)    24093 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_8bp.py
+-rw-r--r--   0 simon      (501) staff       (20)    16763 2023-03-15 19:11:50.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_4bp.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/
+-rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/features_scripts.iml
+-rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/encodings.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/inspectionProfiles/
+-rw-r--r--   0 simon      (501) staff       (20)      822 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/libraries/
+-rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/libraries/R_User_Library.xml
+-rw-r--r--   0 simon      (501) staff       (20)      273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/.gitignore
+-rw-r--r--   0 simon      (501) staff       (20)     8081 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/workspace.xml
+-rw-r--r--   0 simon      (501) staff       (20)      291 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/modules.xml
+-rw-r--r--   0 simon      (501) staff       (20)       23 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/.name
+-rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/misc.xml
+-rw-r--r--   0 simon      (501) staff       (20)     6044 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/plotly_create_h5.py
+-rw-r--r--   0 simon      (501) staff       (20)    15351 2023-04-06 14:48:36.000000 Simba-UW-tf-dev-1.55.2/simba/requirements.txt
+-rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-15 19:16:48.000000 Simba-UW-tf-dev-1.55.2/simba/severity_processor.py
+-rw-r--r--   0 simon      (501) staff       (20)     5941 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.2/simba/user_pose_config_creator.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/mixins/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:26:03.000000 Simba-UW-tf-dev-1.55.2/simba/mixins/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    41856 2023-04-05 17:24:50.000000 Simba-UW-tf-dev-1.55.2/simba/mixins/pop_up_mixin.py
+-rw-r--r--   0 simon      (501) staff       (20)     8182 2023-04-05 13:03:24.000000 Simba-UW-tf-dev-1.55.2/simba/mixins/config_reader.py
+-rw-r--r--   0 simon      (501) staff       (20)     6781 2023-04-06 14:21:49.000000 Simba-UW-tf-dev-1.55.2/simba/mixins/feature_extraction_mixin.py
+-rw-r--r--   0 simon      (501) staff       (20)    34512 2023-04-06 19:49:53.000000 Simba-UW-tf-dev-1.55.2/simba/machine_model_settings_pop_up.py
+-rw-r--r--   0 simon      (501) staff       (20)     5266 2023-03-15 15:43:20.000000 Simba-UW-tf-dev-1.55.2/simba/remove_keypoints_in_pose.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/
+-rw-r--r--   0 simon      (501) staff       (20)     6326 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/deepethogram_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)     9947 2023-03-18 15:35:38.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/BORIS_appender.py
+-rw-r--r--   0 simon      (501) staff       (20)     9170 2023-03-22 19:35:38.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/observer_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)    16922 2023-03-28 20:30:38.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/tools.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-04-01 14:10:06.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)    18283 2023-04-01 14:14:21.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/third_party_appender.py
+-rw-r--r--   0 simon      (501) staff       (20)     8336 2023-03-15 19:12:46.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/ethovision_import.py
+-rw-r--r--   0 simon      (501) staff       (20)     6919 2023-03-19 15:03:14.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/BENTO_appender.py
+-rw-r--r--   0 simon      (501) staff       (20)     5426 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/solomon_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)     7261 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/multi_cropper.py
+-rw-r--r--   0 simon      (501) staff       (20)    13056 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.2/simba/FSTTC_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)    12620 2023-04-06 11:43:07.000000 Simba-UW-tf-dev-1.55.2/simba/create_project_pop_up.py
+-rw-r--r--   0 simon      (501) staff       (20)    13421 2023-04-06 11:40:29.000000 Simba-UW-tf-dev-1.55.2/simba/video_info_table.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:25:58.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     8507 2023-03-15 19:09:16.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_clf_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)    13530 2023-03-15 19:08:52.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    18253 2023-04-06 11:29:26.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_menues.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)     1660 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_tools.py
+-rw-r--r--   0 simon      (501) staff       (20)    16374 2023-03-15 19:09:04.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    13160 2023-03-20 13:43:59.000000 Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_movement_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)     2813 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/extract_frames_fast.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/utils/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 20:15:03.000000 Simba-UW-tf-dev-1.55.2/simba/utils/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     5626 2023-03-28 20:35:14.000000 Simba-UW-tf-dev-1.55.2/simba/utils/warnings.py
+-rw-r--r--   0 simon      (501) staff       (20)     3825 2023-04-06 19:25:38.000000 Simba-UW-tf-dev-1.55.2/simba/utils/lookups.py
+-rw-r--r--   0 simon      (501) staff       (20)    11967 2023-04-06 19:37:44.000000 Simba-UW-tf-dev-1.55.2/simba/utils/errors.py
+-rw-r--r--   0 simon      (501) staff       (20)    21581 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/labelling_interface.py
+-rw-r--r--   0 simon      (501) staff       (20)     9937 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.2/simba/timebins_movement_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    45524 2023-04-04 20:09:14.000000 Simba-UW-tf-dev-1.55.2/simba/train_model_functions.py
+-rw-r--r--   0 simon      (501) staff       (20)    49699 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/SimBA_dash_app.py
+-rw-r--r--   0 simon      (501) staff       (20)     7520 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.2/simba/timebins_clf_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     8240 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.2/simba/calculate_px_dist.py
+-rw-r--r--   0 simon      (501) staff       (20)     6548 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/movement_processor.py
+-rw-r--r--   0 simon      (501) staff       (20)     2904 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pybursts.py
+-rw-r--r--   0 simon      (501) staff       (20)     5265 2023-03-29 18:04:02.000000 Simba-UW-tf-dev-1.55.2/simba/run_model_new.py
+-rw-r--r--   0 simon      (501) staff       (20)     3104 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/rw_dfs.py
+-rw-r--r--   0 simon      (501) staff       (20)     6684 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/reverse_2_animal_tracking.py
+-rw-r--r--   0 simon      (501) staff       (20)     9743 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.2/simba/Directing_animals_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     4357 2023-03-30 16:19:09.000000 Simba-UW-tf-dev-1.55.2/simba/Validate_model_one_video_run_clf.py
+-rw-r--r--   0 simon      (501) staff       (20)     9548 2023-04-06 00:40:25.000000 Simba-UW-tf-dev-1.55.2/simba/tkinter_functions.py
+-rw-r--r--   0 simon      (501) staff       (20)    13767 2023-03-24 12:49:19.000000 Simba-UW-tf-dev-1.55.2/simba/setting_menu.py
+-rw-r--r--   0 simon      (501) staff       (20)     6614 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/interpolate_pose.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/
+-rw-r--r--   0 simon      (501) staff       (20)     8571 2023-03-30 10:06:59.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/gantt_creator.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/tools/
+-rw-r--r--   0 simon      (501) staff       (20)     5353 2023-03-30 15:38:37.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/tools/tkinter_tools.py
+-rw-r--r--   0 simon      (501) staff       (20)    17962 2023-03-24 13:40:30.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_plotter_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    14592 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/shap_agg_stats_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    12928 2023-03-30 10:08:46.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/gantt_creator_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    15777 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_clf_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     8884 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/probability_plot_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)    16058 2023-03-22 14:43:52.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/misc_visualizations.py
+-rw-r--r--   0 simon      (501) staff       (20)    13501 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/plot_clf_results.py
+-rw-r--r--   0 simon      (501) staff       (20)    17696 2023-03-29 16:22:09.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/plot_clf_results_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    16328 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_feature_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    12588 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_location.py
+-rw-r--r--   0 simon      (501) staff       (20)    12585 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/probability_plot_creator_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     5341 2023-03-30 15:46:49.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/interactive_probability_grapher.py
+-rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-29 17:02:51.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/plot_pose_in_dir.py
+-rw-r--r--   0 simon      (501) staff       (20)    12184 2023-03-31 13:53:09.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/single_run_model_validation_video.py
+-rw-r--r--   0 simon      (501) staff       (20)    11202 2023-03-19 16:21:53.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/frame_mergerer_ffmpeg.py
+-rw-r--r--   0 simon      (501) staff       (20)    12442 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/Directing_animals_visualizer_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     9856 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/clf_validator.py
+-rw-r--r--   0 simon      (501) staff       (20)    17290 2023-04-06 00:33:50.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/path_plotter_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    19958 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_feature_visualizer_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    10157 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/data_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)    12444 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/path_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)     8609 2023-03-15 13:37:59.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/ez_lineplot.py
+-rw-r--r--   0 simon      (501) staff       (20)    12970 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/distance_plotter_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    15626 2023-03-29 17:05:49.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)    13165 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_clf.py
+-rw-r--r--   0 simon      (501) staff       (20)     8891 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/distance_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)    13554 2023-04-01 13:12:31.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/single_run_model_validation_video_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     9839 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/Directing_animals_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    16155 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_location_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     5029 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/run_dash_tkinter.py
+-rw-r--r--   0 simon      (501) staff       (20)     7454 2023-03-13 22:11:36.000000 Simba-UW-tf-dev-1.55.2/simba/interpolate_smooth_post_hoc.py
+-rw-r--r--   0 simon      (501) staff       (20)    24474 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/dash_app.py
+-rw-r--r--   0 simon      (501) staff       (20)     6350 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/reverse_tracking_order.py
+-rw-r--r--   0 simon      (501) staff       (20)     5772 2023-03-20 13:55:20.000000 Simba-UW-tf-dev-1.55.2/simba/concatenator_pop_up.py
+-rw-r--r--   0 simon      (501) staff       (20)     2824 2023-03-24 16:12:51.000000 Simba-UW-tf-dev-1.55.2/simba/extract_annotation_frames.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     7385 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_time_bin_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)     2248 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_movement_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-20 12:47:56.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    43831 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_define.py
+-rw-r--r--   0 simon      (501) staff       (20)     3384 2023-03-20 12:41:16.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_reset.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)    21382 2023-03-31 10:40:20.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    11920 2023-03-31 10:48:40.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_feature_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     3537 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_multiply.py
+-rw-r--r--   0 simon      (501) staff       (20)      961 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_size_calculations.py
+-rw-r--r--   0 simon      (501) staff       (20)     3505 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_zoom.py
+-rw-r--r--   0 simon      (501) staff       (20)    11335 2023-04-05 11:07:42.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_directing_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    10128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_move_shape.py
+-rw-r--r--   0 simon      (501) staff       (20)     5097 2023-04-05 20:01:02.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_menus.py
+-rw-r--r--   0 simon      (501) staff       (20)    15175 2023-03-20 12:28:41.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_clf_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)    22682 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_image.py
+-rw-r--r--   0 simon      (501) staff       (20)    57395 2023-04-06 00:28:01.000000 Simba-UW-tf-dev-1.55.2/simba/misc_tools.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/
+-rw-r--r--   0 simon      (501) staff       (20)     2494 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/read_DANNCE_mat.py
+-rw-r--r--   0 simon      (501) staff       (20)    25782 2023-03-20 12:51:35.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/sleap_importer_slp.py
+-rw-r--r--   0 simon      (501) staff       (20)    24720 2023-03-13 15:26:36.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/sleap_importer_h5.py
+-rw-r--r--   0 simon      (501) staff       (20)    26507 2023-03-21 12:58:39.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/dlc_multi_animal_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)    23731 2023-03-20 12:55:04.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/sleap_importer_csv.py
+-rw-r--r--   0 simon      (501) staff       (20)    16536 2023-03-20 13:30:18.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/import_trk.py
+-rw-r--r--   0 simon      (501) staff       (20)     7837 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/import_mars.py
+-rw-r--r--   0 simon      (501) staff       (20)     8905 2023-03-20 13:49:13.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/dlc_importer_csv.py
+-rw-r--r--   0 simon      (501) staff       (20)     8173 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_importers/trk_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)   232876 2023-04-06 14:21:49.000000 Simba-UW-tf-dev-1.55.2/simba/pop_up_classes.py
+-rw-r--r--   0 simon      (501) staff       (20)     4692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/extract_seqframes.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/
+-rw-r--r--   0 simon      (501) staff       (20)    14340 2023-03-30 11:05:37.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/bp_names/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:00.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/bp_names/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     1316 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/bp_names/bp_names.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/no_animals/
+-rw-r--r--   0 simon      (501) staff       (20)       24 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/no_animals/no_animals.csv
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:19.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/no_animals/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/configuration_names/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:14.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/configuration_names/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)      267 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/configuration_names/pose_config_names.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-30 10:45:10.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    39805 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/8.png
+-rw-r--r--   0 simon      (501) staff       (20)    62501 2023-03-30 10:39:05.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/9.png
+-rw-r--r--   0 simon      (501) staff       (20)     6172 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/12.png
+-rw-r--r--   0 simon      (501) staff       (20)    69501 2023-03-30 10:44:04.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/11.png
+-rw-r--r--   0 simon      (501) staff       (20)    69410 2023-03-30 10:40:01.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/10.png
+-rw-r--r--   0 simon      (501) staff       (20)    16000 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/4.png
+-rw-r--r--   0 simon      (501) staff       (20)    28150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/5.png
+-rw-r--r--   0 simon      (501) staff       (20)    31140 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/7.png
+-rw-r--r--   0 simon      (501) staff       (20)    30634 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/6.png
+-rw-r--r--   0 simon      (501) staff       (20)    15417 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/2.png
+-rw-r--r--   0 simon      (501) staff       (20)    15786 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/3.png
+-rw-r--r--   0 simon      (501) staff       (20)    18939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/1.png
+-rw-r--r--   0 simon      (501) staff       (20)     7273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/get_coordinates_tools_v2.py
+-rw-r--r--   0 simon      (501) staff       (20)    16252 2023-03-15 19:16:56.000000 Simba-UW-tf-dev-1.55.2/simba/pup_retrieval_protocol.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     7712 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/outlier_corrector_movement.py
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-15 17:05:05.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)     8264 2023-03-15 17:05:35.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/outlier_corrector_location.py
+-rw-r--r--   0 simon      (501) staff       (20)     4362 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/skip_outlier_correction.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/
+-rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/outlier_scripts.iml
+-rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/encodings.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/inspectionProfiles/
+-rw-r--r--   0 simon      (501) staff       (20)      668 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/libraries/
+-rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/libraries/R_User_Library.xml
+-rw-r--r--   0 simon      (501) staff       (20)     8102 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/workspace.xml
+-rw-r--r--   0 simon      (501) staff       (20)      289 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/modules.xml
+-rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/misc.xml
+-rw-r--r--   0 simon      (501) staff       (20)     2569 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/pose_reset.py
+-rw-r--r--   0 simon      (501) staff       (20)    17642 2023-04-04 23:10:52.000000 Simba-UW-tf-dev-1.55.2/simba/train_mutiple_models.py
+-rw-r--r--   0 simon      (501) staff       (20)    60134 2023-04-06 19:52:45.000000 Simba-UW-tf-dev-1.55.2/simba/SimBA.py
+-rw-r--r--   0 simon      (501) staff       (20)    27431 2023-04-04 14:39:01.000000 Simba-UW-tf-dev-1.55.2/simba/labelling_advanced_interface.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/unsupervised/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/unsupervised/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)   109483 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/unsupervised/model_names.parquet
+-rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/unsupervised/features.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/
+-rw-r--r--   0 simon      (501) staff       (20)     1177 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/down_arrow.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     1733 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/intruder_shape.jpg
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/feature_categories/
+-rw-r--r--   0 simon      (501) staff       (20)      109 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/feature_categories/.~lock.shap_feature_categories.csv#
+-rw-r--r--   0 simon      (501) staff       (20)    17420 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/feature_categories/shap_feature_categories.csv
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     1665 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_shape.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     2415 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_intruder_shape.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     2012 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/animal_distances.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     4422 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/baseline_scale.jpg
+-rw-r--r--   0 simon      (501) staff       (20)   353824 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/ubuntu.regular.ttf
+-rw-r--r--   0 simon      (501) staff       (20)     6672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/side_scale.jpg
+-rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/UbuntuMono-Regular.ttf
+-rw-r--r--   0 simon      (501) staff       (20)     2737 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/side_scale_5.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     1785 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/intruder_movement.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     1435 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_movement.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     3134 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/color_bar.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     2120 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_intruder_movement.jpg
+-rw-r--r--   0 simon      (501) staff       (20)    16388 2023-04-06 18:20:18.000000 Simba-UW-tf-dev-1.55.2/simba/assets/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/lookups/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/lookups/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)   270783 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/lookups/model_names.parquet
+-rw-r--r--   0 simon      (501) staff       (20)     2426 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/lookups/feature_extraction_headers.csv
+-rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/lookups/features.csv
+-rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/lookups/unsupervised_example_x.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/stl/
+-rw-r--r--   0 simon      (501) staff       (20)   551576 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/stl/operant_tray.stl
+-rw-r--r--   0 simon      (501) staff       (20)    67647 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/stl/operant_lever.stl
+-rw-r--r--   0 simon      (501) staff       (20)    92896 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/stl/operant_walls.stl
+-rw-r--r--   0 simon      (501) staff       (20)  4759984 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/stl/grid_floor.stl
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/img/
+-rw-r--r--   0 simon      (501) staff       (20)   399272 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/img/about_me.png
+-rw-r--r--   0 simon      (501) staff       (20)   322242 2023-04-06 16:38:51.000000 Simba-UW-tf-dev-1.55.2/simba/assets/img/bg_2.png
+-rw-r--r--   0 simon      (501) staff       (20)   454535 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/img/splash.png
+-rw-r--r--   0 simon      (501) staff       (20)    69267 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/img/splash.pptx
+-rw-r--r--   0 simon      (501) staff       (20)   204362 2023-04-06 15:01:45.000000 Simba-UW-tf-dev-1.55.2/simba/assets/img/bg.png
+-rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/UbuntuMono-Regular.ttf
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/
+-rw-r--r--   0 simon      (501) staff       (20)     1350 2023-03-17 17:59:27.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/factory.png
+-rw-r--r--   0 simon      (501) staff       (20)     1413 2023-03-21 13:03:06.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/cluster.png
+-rw-r--r--   0 simon      (501) staff       (20)     1340 2023-03-17 16:51:08.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/load.png
+-rw-r--r--   0 simon      (501) staff       (20)     4507 2023-03-20 14:13:48.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/gif.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4566 2023-03-18 18:12:27.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/pose.png
+-rw-rw-r--   0 simon      (501) staff       (20)     1943 2023-03-18 18:14:10.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/features.png
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-04-05 17:25:36.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/.DS_Store
+-rw-rw-r--   0 simon      (501) staff       (20)     4896 2023-03-17 19:17:29.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/settings.png
+-rw-r--r--   0 simon      (501) staff       (20)     1252 2023-03-19 16:48:40.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/link.png
+-rw-r--r--   0 simon      (501) staff       (20)    14250 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/dash_simba.css
+-rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-05 16:43:13.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/documentation.png
+-rw-r--r--   0 simon      (501) staff       (20)     4503 2023-03-20 14:08:00.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/fps.png
+-rw-r--r--   0 simon      (501) staff       (20)     1299 2023-03-21 13:02:07.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/dimensionality_reduction.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4823 2023-03-17 19:03:29.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/roi.png
+-rw-r--r--   0 simon      (501) staff       (20)      920 2023-03-20 14:25:03.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/superimpose.png
+-rw-r--r--   0 simon      (501) staff       (20)     1136 2023-03-18 20:25:31.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/label.png
+-rw-r--r--   0 simon      (501) staff       (20)     1016 2023-03-20 14:28:47.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/change.png
+-rw-r--r--   0 simon      (501) staff       (20)     1124 2023-03-17 18:05:26.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/crop.png
+-rw-r--r--   0 simon      (501) staff       (20)     1057 2023-03-20 14:03:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/path.png
+-rw-r--r--   0 simon      (501) staff       (20)      950 2023-03-17 18:07:33.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/clip.png
+-rw-r--r--   0 simon      (501) staff       (20)     2121 2023-04-04 14:37:43.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/restart.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-17 18:11:59.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/calipher.png
+-rw-r--r--   0 simon      (501) staff       (20)     1291 2023-03-21 20:16:55.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/add_on.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4695 2023-03-17 17:57:16.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/create.png
+-rw-r--r--   0 simon      (501) staff       (20)    78182 2023-03-20 16:35:36.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/SimBA_logo.ico
+-rw-r--r--   0 simon      (501) staff       (20)     1067 2023-03-20 14:22:44.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/print.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-18 20:27:58.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/clf.png
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/
+-rw-r--r--   0 simon      (501) staff       (20)     6027 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/mosaic.png
+-rw-r--r--   0 simon      (501) staff       (20)     5654 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/vertical.png
+-rw-r--r--   0 simon      (501) staff       (20)     5542 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/horizontal.png
+-rw-r--r--   0 simon      (501) staff       (20)     5939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/mixed_mosaic.png
+-rw-r--r--   0 simon      (501) staff       (20)     2060 2023-03-20 14:26:12.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/merge.png
+-rw-------   0 simon      (501) staff       (20)     4725 2023-03-18 20:27:47.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/clf_2.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4795 2023-03-17 18:10:10.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/visualize.png
+-rw-r--r--   0 simon      (501) staff       (20)     2142 2023-03-20 14:10:28.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat.png
+-rw-r--r--   0 simon      (501) staff       (20)     1474 2023-03-17 19:20:24.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/boris.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4804 2023-03-19 16:43:01.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/frames.png
+-rw-r--r--   0 simon      (501) staff       (20)     2425 2023-03-19 16:44:55.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/video.png
+-rw-r--r--   0 simon      (501) staff       (20)     2089 2023-03-20 14:05:58.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/sample.png
+-rw-r--r--   0 simon      (501) staff       (20)     1471 2023-03-21 13:04:02.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/metrics.png
+-rw-r--r--   0 simon      (501) staff       (20)     4555 2023-03-20 14:21:02.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/grey.png
+-rw-r--r--   0 simon      (501) staff       (20)      930 2023-03-18 18:07:29.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/exit.png
+-rw-r--r--   0 simon      (501) staff       (20)     4751 2023-03-18 20:31:58.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/outlier.png
+-rw-r--r--   0 simon      (501) staff       (20)     4392 2023-03-20 14:16:15.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/clahe.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4637 2023-03-17 19:03:55.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/trash.png
+-rw-r--r--   0 simon      (501) staff       (20)     1239 2023-03-19 16:51:21.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/about.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4666 2023-03-17 18:01:21.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/convert.png
+-rw-r--r--   0 simon      (501) staff       (20)    93229 2023-03-20 16:01:42.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/SimBA_logo.icns
+-rw-r--r--   0 simon      (501) staff       (20)      991 2023-03-20 19:02:33.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/reorganize.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4784 2023-03-17 18:50:35.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/browse.png
+-rw-r--r--   0 simon      (501) staff       (20)    30707 2023-03-20 16:33:38.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/SimBA_logo.png
+-rw-r--r--   0 simon      (501) staff       (20)     2293 2023-03-17 19:24:38.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/ethovision.png
+-rw-r--r--   0 simon      (501) staff       (20)     1018 2023-04-05 15:24:49.000000 Simba-UW-tf-dev-1.55.2/simba/assets/icons/close.png
+-rw-r--r--   0 simon      (501) staff       (20)    13672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/dash_simba_base.css
+-rw-r--r--   0 simon      (501) staff       (20)    31812 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/assets/TheGoldenLab.PNG
+-rw-r--r--   0 simon      (501) staff       (20)    21392 2023-03-22 19:01:48.000000 Simba-UW-tf-dev-1.55.2/simba/drop_bp_cords.py
+-rw-r--r--   0 simon      (501) staff       (20)     8116 2023-03-19 18:27:51.000000 Simba-UW-tf-dev-1.55.2/simba/read_config_unit_tests.py
+-rw-r--r--   0 simon      (501) staff       (20)    11564 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/project_config_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)    27444 2023-03-15 15:58:40.000000 Simba-UW-tf-dev-1.55.2/simba/set_hyperparameters.py
+-rw-r--r--   0 simon      (501) staff       (20)    20780 2023-04-04 23:58:36.000000 Simba-UW-tf-dev-1.55.2/simba/train_single_model.py
+-rw-r--r--   0 simon      (501) staff       (20)     6426 2023-03-17 16:57:53.000000 Simba-UW-tf-dev-1.55.2/simba/create_clf_log.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-17 14:43:38.000000 Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    24896 2023-04-06 11:29:26.000000 Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/batch_process_menus.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)    10936 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py
+-rw-r--r--   0 simon      (501) staff       (20)     9563 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.2/simba/Kleinberg_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)     8392 2023-04-03 14:06:05.000000 Simba-UW-tf-dev-1.55.2/simba/reorganize_keypoint_in_pose.py
+-rw-r--r--   0 simon      (501) staff       (20)      165 2023-03-25 11:18:21.000000 Simba-UW-tf-dev-1.55.2/simba/~$features.pptx
+-rw-r--r--   0 simon      (501) staff       (20)     6557 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.2/simba/play_annotation_video.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/
+-rw-rw-r--   0 simon      (501) staff       (20)      579 2023-04-06 19:53:41.000000 Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/PKG-INFO
+-rw-rw-r--   0 simon      (501) staff       (20)    12849 2023-04-06 19:53:41.000000 Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/SOURCES.txt
+-rw-rw-r--   0 simon      (501) staff       (20)       44 2023-04-06 19:53:41.000000 Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/entry_points.txt
+-rw-rw-r--   0 simon      (501) staff       (20)      640 2023-04-06 19:53:41.000000 Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/requires.txt
+-rw-rw-r--   0 simon      (501) staff       (20)        6 2023-04-06 19:53:41.000000 Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/top_level.txt
+-rw-rw-r--   0 simon      (501) staff       (20)        1 2023-04-06 19:53:41.000000 Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/dependency_links.txt
+-rw-rw-r--   0 simon      (501) staff       (20)     7652 2020-05-13 13:27:38.000000 Simba-UW-tf-dev-1.55.2/LICENSE.md
+-rw-rw-r--   0 simon      (501) staff       (20)      136 2021-04-10 10:44:06.000000 Simba-UW-tf-dev-1.55.2/MANIFEST.in
+-rw-rw-r--   0 simon      (501) staff       (20)     9598 2020-05-13 13:27:40.000000 Simba-UW-tf-dev-1.55.2/README.md
+-rw-rw-r--   0 simon      (501) staff       (20)     1897 2023-04-06 19:53:39.000000 Simba-UW-tf-dev-1.55.2/setup.py
+-rw-r--r--   0 simon      (501) staff       (20)       38 2023-04-06 19:53:42.000000 Simba-UW-tf-dev-1.55.2/setup.cfg
```

### Comparing `Simba-UW-tf-dev-1.55.1/PKG-INFO` & `Simba-UW-tf-dev-1.55.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Simba-UW-tf-dev
-Version: 1.55.1
+Version: 1.55.2
 Summary: Toolkit for computer classification of complex social behaviors in experimental animals
 Home-page: https://github.com/sgoldenlab/simba
 Author: Simon Nilsson, Jia Jie Choong, Sophia Hwang
 Author-email: sronilsson@gmail.com
 License: GNU Lesser General Public License v3 (LGPLv3)
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/video_processing.py` & `Simba-UW-tf-dev-1.55.2/simba/video_processing.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/blob_storage/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/blob_storage/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/unsupervised_ui.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/unsupervised_ui.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/misc.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/misc.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/dataset_creator.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/dataset_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/data_extractors.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/data_extractors.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/dbcv.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/dbcv.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/visualizers.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/visualizers.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/umap_embedder.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/umap_embedder.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/visualization_tools/vtk_embeddings.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/visualization_tools/vtk_embeddings.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/pop_up_classes.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/pop_up_classes.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/cluster_statistics.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/cluster_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/hdbscan_clusterer.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/hdbscan_clusterer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/tsne.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/tsne.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/unsupervised/cluster_visualizer.py` & `Simba-UW-tf-dev-1.55.2/simba/unsupervised/cluster_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/enums.py` & `Simba-UW-tf-dev-1.55.2/simba/enums.py`

 * *Files 2% similar despite different names*

```diff
@@ -108,15 +108,15 @@
     ABOUT_ME = Path('assets/img/about_me.png')
     PROBABILITY_PLOTS_DIR = Path('frames/output/probability_plots/')
     ROI_DEFINITIONS = Path('measures/ROI_definitions.h5')
     DETAILED_ROI_DATA_DIR = Path('logs/Detailed_ROI_data/')
     SHAP_LOGS = Path('logs/shap/')
     SPLASH_PATH_WINDOWS = Path('assets/img/splash.png')
     SPLASH_PATH_LINUX = Path('assets/img/splash.PNG')
-    BG_IMG_PATH = Path('assets/img/bg.png')
+    BG_IMG_PATH = Path('assets/img/bg_2.png')
     LOGO_ICON_WINDOWS_PATH = Path('assets/icons/SimBA_logo.ico')
     LOGO_ICON_DARWIN_PATH = Path('assets/icons/SimBA_logo.png')
     UNSUPERVISED_MODEL_NAMES = Path('assets/lookups/model_names.parquet')
 
 class Formats(Enum):
     MP4_CODEC = 'mp4v'
     AVI_CODEC = 'XVID'
@@ -183,15 +183,15 @@
                                             'Annotations EVENT COUNT conflict',
                                             'Annotations data file NOT FOUND']
 
 class Defaults(Enum):
     MAX_TASK_PER_CHILD = 10
     CHUNK_SIZE = 1
     SPLASH_TIME = 2500
-    WELCOME_MSG = 'Welcome fellow scientists :) \n'
+    WELCOME_MSG = 'Welcome fellow scientists \n'
     BROWSE_FOLDER_BTN_TEXT = 'Browse Folder'
     BROWSE_FILE_BTN_TEXT = 'Browse File'
     NO_FILE_SELECTED_TEXT = 'No file selected'
 
 
 
 class DirNames(Enum):
@@ -225,14 +225,16 @@
     STR = 'str'
     INT = 'int'
     FLOAT = 'float'
     NONE = 'None'
     SQRT = 'sqrt'
     ENTROPY = 'entropy'
 
+
+
 class Methods(Enum):
     USER_DEFINED = 'user_defined'
     CLASSIC_TRACKING = 'Classic tracking'
     THREE_D_TRACKING = '3D tracking'
     MULTI_TRACKING = 'Multi tracking'
     CREATE_POSE_CONFIG = 'Create pose config...'
     RANDOM_UNDERSAMPLE = 'random undersample'
@@ -322,8 +324,14 @@
     PSEUDO_LBL = 'https://github.com/sgoldenlab/simba/blob/master/docs/pseudoLabel.md'
     ADVANCED_LBL = 'https://github.com/sgoldenlab/simba/blob/master/docs/advanced_labelling.md'
     TRAIN_ML_MODEL = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#step-7-train-machine-model'
     VISUALIZATION = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario2.md#part-5--visualizing-results'
     PLOTLY = 'https://github.com/sgoldenlab/simba/blob/master/docs/plotly_dash.md'
     VIDEO_PARAMETERS = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#step-3-set-video-parameters'
     OUTLIERS_DOC = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#step-4-outlier-correction'
-    CREATE_PROJECT = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#step-1-generate-project-config'
+    CREATE_PROJECT = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#step-1-generate-project-config'
+    LOAD_PROJECT = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#part-2-load-project-1'
+    SCENARIO_2 = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario2.md'
+    BBOXES = 'https://github.com/sgoldenlab/simba/blob/master/docs/anchored_rois.md'
+    CUE_LIGHTS = 'https://github.com/sgoldenlab/simba/blob/master/docs/cue_light_tutorial.md'
+    ADDITIONAL_IMPORTS = 'https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#step-2-optional-step--import-more-dlc-tracking-data-or-videos'
+
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/agg_boundary_stats.py` & `Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/agg_boundary_stats.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/find_bounderies.py` & `Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/find_bounderies.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/boundary_menus.py` & `Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/boundary_menus.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 from simba.read_config_unit_tests import (read_config_entry,
                                           read_config_file,
                                           check_int,
                                           read_project_path_and_file_type)
 from simba.tkinter_functions import (DropDownMenu,
-                                     Entry_Box)
+                                     Entry_Box,
+                                     CreateLabelFrameWithIcon)
 from simba.drop_bp_cords import (create_body_part_dictionary,
                                  getBpNames)
 from simba.misc_tools import (check_multi_animal_status,
                               get_fn_ext,
                               get_named_colors)
 from simba.enums import ReadConfig, Dtypes, Formats
 
@@ -15,14 +16,15 @@
 import pickle
 from tkinter import *
 from simba.bounding_box_tools.find_bounderies import AnimalBoundaryFinder
 from simba.bounding_box_tools.visualize_boundaries import BoundaryVisualizer
 from simba.bounding_box_tools.boundary_statistics import BoundaryStatisticsCalculator
 from simba.bounding_box_tools.agg_boundary_stats import AggBoundaryStatisticsCalculator
 from simba.utils.errors import NoFilesFoundError, NoChoosenMeasurementError
+from simba.enums import Keys, Links
 
 class BoundaryMenus(object):
     """
     Class creating GUI interface for extrapolating bounding boxes from pose-estimation data, and calculating
     statstics on bounding boxes and pose-estmated key-point intersections.
 
     Parameters
@@ -47,15 +49,16 @@
         self.project_path, _ = read_project_path_and_file_type(config=self.config)
         self.video_dir = os.path.join(self.project_path, 'videos')
         self.no_animals = read_config_entry(self.config, ReadConfig.GENERAL_SETTINGS.value, ReadConfig.ANIMAL_CNT.value, Dtypes.INT.value)
         self.boundary_main_frm = Toplevel()
         self.boundary_main_frm.minsize(750, 300)
         self.boundary_main_frm.wm_title("SIMBA ANCHORED ROI (BOUNDARY BOXES ANALYSIS)")
         self.named_shape_colors = get_named_colors()
-        self.settings_frm = LabelFrame(self.boundary_main_frm, text='SETTINGS', font=Formats.LABELFRAME_HEADER_FORMAT.value, pady=5, padx=15)
+
+        self.settings_frm = CreateLabelFrameWithIcon(parent=self.boundary_main_frm, header='SETTINGS', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.BBOXES.value)
         self.multi_animal_status, self.multi_animal_id_lst = check_multi_animal_status(self.config, self.no_animals)
         self.x_cols, self.y_cols, self.pcols = getBpNames(config_path)
         self.animal_bp_dict = create_body_part_dictionary(self.multi_animal_status, list(self.multi_animal_id_lst), self.no_animals, list(self.x_cols), list(self.y_cols), [], [])
         self.max_animal_name_char = len(max([x for x in list(self.animal_bp_dict.keys())]))
         self.find_boundaries_btn = Button(self.settings_frm, text='FIND ANIMAL BOUNDARIES', command=lambda: self.__launch_find_boundaries_pop_up())
         self.visualize_boundaries_btn = Button(self.settings_frm, text='VISUALIZE BOUNDARIES', command=lambda: self.__launch_visualize_boundaries())
         self.boundary_statistics_btn = Button(self.settings_frm, text='CALCULATE BOUNDARY STATISTICS', command=lambda: self.__launch_boundary_statistics())
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/boundary_statistics.py` & `Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/boundary_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/bounding_box_tools/visualize_boundaries.py` & `Simba-UW-tf-dev-1.55.2/simba/bounding_box_tools/visualize_boundaries.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_14bp.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_14bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_7bp.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_7bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/read_in_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/read_in_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/fish_feature_extractor_2022.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/fish_feature_extractor_2022.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/convex_hull_3_scratch_3.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/convex_hull_3_scratch_3.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/convex_hull_scratch_1.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/convex_hull_scratch_1.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/fish_feature_extractor_2023.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/fish_feature_extractor_2023.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/egocentrical_aligner.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/egocentrical_aligner.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/graph_creator.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/graph_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/termite_rois.csv` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/termite_rois.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/mutual_exclusive.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/mutual_exclusive.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/graph_3d_plotter.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/graph_3d_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/add_probability_cnt_features.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/add_probability_cnt_features.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/misc/convex_hull_scratch_2.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/misc/convex_hull_scratch_2.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_8bps_2_animals.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_8bps_2_animals.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/perimeter_jit.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/perimeter_jit.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_subsets.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_subsets.py`

 * *Files 8% similar despite different names*

```diff
@@ -55,14 +55,16 @@
                 self.animal_convex_hulls()
             elif self.feature_family == 'Entire animal convex hull area (mm2)':
                 self.calc_animal_convex_hulls_area()
             elif self.feature_family == 'Frame-by-frame body-part movements (mm)':
                 self.calc_movements()
             elif self.feature_family == 'Frame-by-frame body-part distances to ROI centers (mm)':
                 self.calc_roi_center_distances()
+            elif self.feature_family == 'Frame-by-frame body-parts inside ROIs (Boolean)':
+                self.calc_inside_roi()
 
             self.__save()
             self.video_timer.stop_timer()
             print(f'Video {self.video_name} complete (elapsed time {self.video_timer.elapsed_time_str}s)...')
         self.timer.stop_timer()
         print(f'SIMBA COMPLETE: {self.feature_family} for {str(len(self.outlier_corrected_paths))} videos saved in {self.save_dir} (elapsed time: {self.timer.elapsed_time_str}s')
 
@@ -129,23 +131,39 @@
             for bp in animal_bps:
                 bp_arr = self.df[[f'{bp}_x', f'{bp}_y']].values.astype(float)
                 for shape_type, shape_data in self.roi_dict.items():
                     for shape_name in shape_data['Name'].unique():
                         center_point = shape_data.loc[(shape_data['Video'] == self.video_name) & (shape_data['Name'] == shape_name)][['Center_X', 'Center_Y']].astype(float).values[0]
                         self.results[f'{animal} {bp} to {shape_name} center distance (mm)'] = self.framewise_euclidean_distance_roi(location_1=bp_arr, location_2=center_point, px_per_mm=self.pixel_per_mm)
 
+
+    def calc_inside_roi(self):
+        self.read_roi_data()
+        for animal, animal_bps in self.animal_bps.items():
+            for bp in animal_bps:
+                bp_arr = self.df[[f'{bp}_x', f'{bp}_y']].values.astype(float)
+                for shape_type, shape_data in self.roi_dict.items():
+                    for shape_name in shape_data['Name'].unique():
+                        if shape_type == 'rectangles':
+                            shape_data = shape_data.loc[(shape_data['Video'] == self.video_name) & (shape_data['Name'] == shape_name)][['topLeftX', 'topLeftY', 'Bottom_right_X', 'Bottom_right_Y']].values.reshape(2, 2)
+                            self.results[f'{animal} {bp} inside rectangle {shape_name} (Boolean)'] = self.framewise_inside_rectangle_roi(bp_location=bp_arr, roi_coords=shape_data)
+                        if shape_type == 'polygons':
+                            shape_data = shape_data.loc[(shape_data['Video'] == self.video_name) & (shape_data['Name'] == shape_name)][['vertices']].values[0][0]
+                            self.results[f'{animal} {bp} inside polygon {shape_name} (Boolean)'] = self.framewise_inside_polygon_roi(bp_location=bp_arr, roi_coords=shape_data)
+
+
     def __save(self):
         save_path = os.path.join(self.save_dir, f'{self.video_name}.csv')
         self.results.round(2).to_csv(save_path)
 
 
 
 
 # test = FeatureSubsetsCalculator(config_path='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini',
-#                                 feature_family='Frame-by-frame distance to ROI centers (mm)',
+#                                 feature_family='Frame-by-frame body-parts inside ROIs (Boolean)',
 #                                 save_dir='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/data')
 # test.run()
 
 
 
 
 # test = FeatureSubsetsCalculator(config_path='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini',
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/extract_features_9bp.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/extract_features_9bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_user_defined.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_user_defined.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/unit_tests.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/unit_tests.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_16bp.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_16bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_8bp.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_8bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/feature_extractor_4bp.py` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/feature_extractor_4bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/features_scripts.iml` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/features_scripts.iml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/feature_extractors/.idea/workspace.xml` & `Simba-UW-tf-dev-1.55.2/simba/feature_extractors/.idea/workspace.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotly_create_h5.py` & `Simba-UW-tf-dev-1.55.2/simba/plotly_create_h5.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/requirements.txt` & `Simba-UW-tf-dev-1.55.2/simba/requirements.txt`

 * *Files 0% similar despite different names*

```diff
@@ -135,15 +135,15 @@
 # define_new_pose_config.py: 6
 # path_plot.py: 8
 imutils == 0.5.2
 
 # features_scripts\extract_features_16bp_new.py: 11
 # features_scripts\extract_features_16bp_new_2.py: 9
 # outlier_scripts\movement\correct_devs_mov_16bp.py: 8
-numba == 0.48.0
+numba == 0.52.0
 
 # features_scripts\extract_features_16bp_new.py: 9
 numexpr == 2.6.9
 
 # ROI_add_to_features.py: 4
 # ROI_analysis_2.py: 5
 # ROI_draw_defined.py: 4
@@ -403,15 +403,15 @@
 # outlier_scripts\movement\feature_selection.py: 46,139,140
 # sklearn_DLC_RF_train_model.py: 5,6,7,8,9,14
 # train_model\train_model_user_defined.py: 9,10,11,16,25,26,27,31
 # train_model_2.py: 34
 # train_model_3_scramble.py: 33
 # train_multiple_models_from_meta.py: 7,8,12,13,22,23
 # train_multiple_models_from_meta_scramble.py: 7,8,12,13,22,23
-sklearn == 0.0
+sklearn == 0.22.2
 
 # outlier_scripts\movement\feature_selection.py: 6
 statsmodels == 0.9.0
 
 # SimBA.py: 17
 # train_multiple_models_from_meta.py: 18
 # train_multiple_models_from_meta_scramble.py: 18
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/severity_processor.py` & `Simba-UW-tf-dev-1.55.2/simba/severity_processor.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/user_pose_config_creator.py` & `Simba-UW-tf-dev-1.55.2/simba/user_pose_config_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/mixins/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/mixins/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/mixins/pop_up_mixin.py` & `Simba-UW-tf-dev-1.55.2/simba/mixins/pop_up_mixin.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/mixins/config_reader.py` & `Simba-UW-tf-dev-1.55.2/simba/mixins/config_reader.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/mixins/feature_extraction_mixin.py` & `Simba-UW-tf-dev-1.55.2/simba/mixins/feature_extraction_mixin.py`

 * *Files 19% similar despite different names*

```diff
@@ -16,14 +16,15 @@
                                  getBpNames)
 from simba.misc_tools import check_multi_animal_status
 
 class FeatureExtractionMixin(object):
 
     def __init__(self,
                  config_path: str):
+
         self.config = read_config_file(config_path)
         self.project_path, self.file_type = read_project_path_and_file_type(config=self.config)
         self.data_in_dir = os.path.join(self.project_path, Paths.OUTLIER_CORRECTED.value)
         self.save_dir = os.path.join(self.project_path, Paths.FEATURES_EXTRACTED_DIR.value)
         if not os.path.exists(self.save_dir): os.makedirs(self.save_dir)
         self.vid_info_df = read_video_info_csv(os.path.join(self.project_path, Paths.VIDEO_INFO.value))
         self.no_animals = read_config_entry(self.config, ReadConfig.GENERAL_SETTINGS.value, ReadConfig.ANIMAL_CNT.value, Dtypes.INT.value)
@@ -98,8 +99,44 @@
                                          centimeter: bool = False) -> np.array:
 
         results = np.full((location_1.shape[0]), np.nan)
         for i in prange(location_1.shape[0]):
             results[i] = np.linalg.norm(location_1[i] - location_2) / px_per_mm
         if centimeter:
             results = results / 10
+        return results
+
+    @staticmethod
+    @jit(nopython=True)
+    def framewise_inside_rectangle_roi(bp_location: np.array,
+                                       roi_coords: np.array) -> np.array:
+
+        results = np.full((bp_location.shape[0]), 0)
+        within_x_idx = np.argwhere((bp_location[:, 0] <= roi_coords[1][0]) & (bp_location[:, 0] >= roi_coords[0][0])).flatten()
+        within_y_idx = np.argwhere((bp_location[:, 1] <= roi_coords[1][1]) & (bp_location[:, 1] >= roi_coords[0][1])).flatten()
+        for i in prange(within_x_idx.shape[0]):
+            match = np.argwhere(within_y_idx == within_x_idx[i])
+            if match.shape[0] > 0:
+                results[within_x_idx[i]] = 1
+        return results
+
+    @staticmethod
+    @jit(nopython=True)
+    def framewise_inside_polygon_roi(bp_location: np.array,
+                                     roi_coords: np.array) -> np.array:
+        results = np.full((bp_location.shape[0]), 0)
+        for i in prange(0, results.shape[0]):
+            x, y, n = bp_location[i][0], bp_location[i][1], len(roi_coords)
+            p2x, p2y, xints, inside = 0.0, 0.0, 0.0, False
+            p1x, p1y = roi_coords[0]
+            for j in prange(n + 1):
+                p2x, p2y = roi_coords[j % n]
+                if (y > min(p1y, p2y)) and (y <= max(p1y, p2y)) and (x <= max(p1x, p2x)):
+                    if p1y != p2y:
+                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
+                    if p1x == p2x or x <= xints:
+                        inside = not inside
+                p1x, p1y = p2x, p2y
+            if inside:
+                results[i] = 1
+
         return results
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/machine_model_settings_pop_up.py` & `Simba-UW-tf-dev-1.55.2/simba/machine_model_settings_pop_up.py`

 * *Files 1% similar despite different names*

```diff
@@ -45,15 +45,14 @@
         self.over_sample_options = Options.OVERSAMPLE_OPTIONS.value
         self.class_weighing_options = Options.CLASS_WEIGHT_OPTIONS.value
         self.train_test_sizes_options = Options.CLF_TEST_SIZE_OPTIONS.value
         self.class_weights_options = list(range(1, 11, 1))
         self.clf_cnt = read_config_entry(self.config, ReadConfig.SML_SETTINGS.value, ReadConfig.TARGET_CNT.value, 'int')
         self.clf_names = list(get_all_clf_names(config=self.config, target_cnt=self.clf_cnt))
         load_meta_data_frm = CreateLabelFrameWithIcon(parent=main, header='LOAD META-DATA', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.TRAIN_ML_MODEL.value)
-        #load_meta_data_frm = LabelFrame(main, text='LOAD META-DATA', font=Formats.LABELFRAME_HEADER_FORMAT.value)
         self.select_config_file = FileSelect(load_meta_data_frm, 'CONFIG PATH:')
         load_config_btn = Button(load_meta_data_frm, text='LOAD', fg='blue', command= lambda: self.load_config())
         label_link = Label(load_meta_data_frm,text='[MODEL SETTINGS TUTORIAL]', fg='blue')
         label_link.bind('<Button-1>', lambda e: webbrowser.open_new('https://github.com/sgoldenlab/simba/blob/master/docs/tutorial.md#step-7-train-machine-model'))
 
         machine_model_frm = LabelFrame(main, text='MACHINE MODEL ALGORITHM', font=Formats.LABELFRAME_HEADER_FORMAT.value)
         self.machine_model_dropdown = DropDownMenu(machine_model_frm, 'ALGORITHM: ', self.clf_options, '25')
@@ -439,16 +438,21 @@
             self.learning_curve_data_splits_entry_box.set_state(DISABLED)
 
         if self.meta['generate_shap_scores']:
             self.calc_shap_scores_var.set(value=True)
             self.shap_present.set_state(NORMAL)
             self.shap_absent.set_state(NORMAL)
             self.shap_absent.set_state(NORMAL)
+            self.shap_save_it_dropdown.enable()
             self.shap_present.entry_set(val=self.meta['shap_target_present_no'])
             self.shap_absent.entry_set(val=self.meta['shap_target_absent_no'])
+            if 'shap_save_iteration' in self.meta.keys():
+                self.shap_save_it_dropdown.setChoices(self.meta['shap_save_iteration'])
+            else:
+                self.shap_save_it_dropdown.setChoices('ALL FRAMES')
         else:
             self.calc_shap_scores_var.set(value=False)
             self.shap_present.set_state(DISABLED)
             self.shap_absent.set_state(DISABLED)
             self.shap_save_it_dropdown.enable()
 
         if 'train_test_split_type' in self.meta.keys():
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/remove_keypoints_in_pose.py` & `Simba-UW-tf-dev-1.55.2/simba/remove_keypoints_in_pose.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/deepethogram_importer.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/deepethogram_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/BORIS_appender.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/BORIS_appender.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/observer_importer.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/observer_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/tools.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/third_party_appender.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/third_party_appender.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/ethovision_import.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/ethovision_import.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/BENTO_appender.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/BENTO_appender.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/third_party_label_appenders/solomon_importer.py` & `Simba-UW-tf-dev-1.55.2/simba/third_party_label_appenders/solomon_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/multi_cropper.py` & `Simba-UW-tf-dev-1.55.2/simba/multi_cropper.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/FSTTC_calculator.py` & `Simba-UW-tf-dev-1.55.2/simba/FSTTC_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/create_project_pop_up.py` & `Simba-UW-tf-dev-1.55.2/simba/create_project_pop_up.py`

 * *Files 2% similar despite different names*

```diff
@@ -110,17 +110,17 @@
         reset_btn.grid(row=0, column=1, sticky=NW)
         run_frm.grid(row=3, column=0, sticky=NW)
         create_project_btn.grid(row=0, column=0, sticky=NW)
 
         self.create_import_videos_menu(parent_frm=self.import_videos_tab)
         self.create_import_pose_menu(parent_frm=self.import_data_tab)
 
-        extract_frames_frm = LabelFrame(self.extract_frms_tab, text='Extract Frames into project folder', fg='black', font=Formats.LABELFRAME_HEADER_FORMAT.value, pady=5, padx=5)
+        extract_frames_frm = LabelFrame(self.extract_frms_tab, text='EXTRACT FRAMES INTO PROJECT', fg='black', font=Formats.LABELFRAME_HEADER_FORMAT.value, pady=5, padx=5)
         extract_frames_note = Label(extract_frames_frm, text='Note: This is no longer needed for any of the parts of the SimBA pipeline.\n Caution: This extract all frames from all videos in project. \n and is computationally expensive if there is a lot of videos at high frame rates/resolution.')
-        extract_frames_btn = Button(extract_frames_frm, text='Extract frames', fg='blue', command=lambda: None)
+        extract_frames_btn = Button(extract_frames_frm, text='EXTRACT FRAMES', fg='blue', command=lambda: None)
 
         extract_frames_frm.grid(row=0, column=0, sticky=NW)
         extract_frames_note.grid(row=0, column=0, sticky=NW)
         extract_frames_btn.grid(row=1, column=0, sticky=NW)
         self.update_body_part_dropdown(Methods.CLASSIC_TRACKING.value)
         self.main_frm.mainloop()
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/video_info_table.py` & `Simba-UW-tf-dev-1.55.2/simba/video_info_table.py`

 * *Files 6% similar despite different names*

```diff
@@ -6,17 +6,17 @@
 from simba.misc_tools import (get_fn_ext,
                               get_video_meta_data)
 from simba.read_config_unit_tests import (read_config_file,
                                           read_config_entry,
                                           read_project_path_and_file_type)
 from simba.feature_extractors.unit_tests import (read_video_info_csv,
                                                read_video_info)
-from simba.enums import Paths, ReadConfig, Dtypes
+from simba.enums import Paths, ReadConfig, Dtypes, Keys, Links, Formats
 from simba.get_coordinates_tools_v2 import get_coordinates_nilsson
-from simba.tkinter_functions import hxtScrollbar
+from simba.tkinter_functions import hxtScrollbar, CreateLabelFrameWithIcon
 import collections
 from simba.utils.errors import NoFilesFoundError, ParametersFileError
 
 class VideoInfoTable(object):
     """
     Class for creating Tkinter GUI video meta data table. Allows users to modify resolutions, fps, and pixels-per-mm
     interactively of videos within the SimBA project. Data is stored within the project_folder/logs/video_info.csv
@@ -132,32 +132,33 @@
 
     def create_window(self):
         self.main_frm = Toplevel()
         self.main_frm.minsize(1550, 800)
         self.main_frm.wm_title("Video Info")
         self.main_frm = Canvas(hxtScrollbar(self.main_frm))
         self.main_frm.pack(expand=True,fill=BOTH)
-        self.instructions_frm = LabelFrame(self.main_frm, text='INSTRUCTIONS', font=('Helvetica', 15, 'bold'))
+
+        self.instructions_frm = CreateLabelFrameWithIcon(parent=self.main_frm, header='INSTRUCTIONS', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.VIDEO_PARAMETERS.value)
         self.intructions_label_1 = Label(self.instructions_frm, text='1. Enter the known distance (millimeters) in the "DISTANCE IN MM" column. Consider using the "autopopulate" entry box in the main project window you have a lot of videos.', font=('Helvetica', 15))
         self.intructions_label_2 = Label(self.instructions_frm, text='2. Click on "Calculate distance" button(s) to calculate pixels/mm for each video.', font=('Helvetica', 15))
         self.intructions_label_3 = Label(self.instructions_frm, text='3. Click <SAVE DATA> when all the data are filled in.', font=('Helvetica', 15))
         self.instructions_frm.grid(row=0, column=0, sticky=W)
         self.intructions_label_1.grid(row=0, column=0, sticky=W)
         self.intructions_label_2.grid(row=1, column=0, sticky=W)
         self.intructions_label_3.grid(row=2, column=0, sticky=W)
-        self.execute_frm = LabelFrame(self.main_frm, text='EXECUTE', font=('Helvetica', 15, 'bold'))
+        self.execute_frm = LabelFrame(self.main_frm, text='EXECUTE', font=Formats.LABELFRAME_HEADER_FORMAT.value)
         self.save_data_btn = Button(self.execute_frm, text='SAVE DATA', fg='green', command=lambda: self.__save_data())
         self.execute_frm.grid(row=1, column=0, sticky=W)
         self.save_data_btn.grid(row=0, column=0, sticky=W)
-        self.video_frm = LabelFrame(self.main_frm, text='PROJECT VIDEOS', font=('Helvetica', 15, 'bold'))
+        self.video_frm = LabelFrame(self.main_frm, text='PROJECT VIDEOS', font=Formats.LABELFRAME_HEADER_FORMAT.value)
         self.column_names = ['INDEX', 'VIDEO', 'FPS', 'RESOLUTION WIDTH', 'RESOLUTION HEIGHT', 'DISTANCE IN MM', 'FIND DISTANCE', 'PIXELS PER MM']
         self.col_widths = ['5',self.max_char_vid_name,'18','18','18','18', '18', '18']
         self.video_frm.grid(row=6, column=0)
         for cnt, (col_name, col_width) in enumerate(zip(self.column_names, self.col_widths)):
-            col_header_label = Label(self.video_frm, text=col_name, width=col_width, font=('Helvetica', 14, 'bold'))
+            col_header_label = Label(self.video_frm, text=col_name, width=col_width, font=Formats.LABELFRAME_HEADER_FORMAT.value)
             col_header_label.grid(row=0, column=cnt, sticky=W)
         self.videos = {}
         self.__append_videos_from_video_folder()
         self.__check_for_duplicate_names()
         self.duplicate_btn = Button(self.video_frm, text='Duplicate index 1 pixels/mm (CAUTION!)', fg='red', command=lambda: self.__duplicate_idx_1_px_mm())
         self.duplicate_btn.grid(row=1, column=7, sticky=W, padx=5)
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_clf_statistics.py` & `Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_clf_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_menues.py` & `Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_menues.py`

 * *Files 4% similar despite different names*

```diff
@@ -8,53 +8,19 @@
 import pandas as pd
 from simba.cue_light_tools.cue_light_analyzer import CueLightAnalyzer
 from simba.cue_light_tools.cue_light_visualizer import CueLightVisualizer
 from simba.train_model_functions import get_all_clf_names
 from simba.cue_light_tools.cue_light_clf_statistics import CueLightClfAnalyzer
 from simba.cue_light_tools.cue_light_movement_statistics import CueLightMovementAnalyzer
 from simba.utils.errors import NoFilesFoundError, CountError, NoROIDataError, NoChoosenClassifierError
+from simba.tkinter_functions import hxtScrollbar, CreateLabelFrameWithIcon
+from simba.enums import Keys, Links
+
 import webbrowser
 
-def onMousewheel(event, canvas):
-    try:
-        scrollSpeed = event.delta
-        if platform.system() == 'Darwin':
-            scrollSpeed = event.delta
-        elif platform.system() == 'Windows':
-            scrollSpeed = int(event.delta / 120)
-        canvas.yview_scroll(-1 * (scrollSpeed), "units")
-    except:
-        pass
-
-def bindToMousewheel(event, canvas):
-    canvas.bind_all("<MouseWheel>", lambda event: onMousewheel(event, canvas))
-
-def unbindToMousewheel(event, canvas):
-    canvas.unbind_all("<MouseWheel>")
-
-def onFrameConfigure(canvas):
-    canvas.configure(scrollregion=canvas.bbox("all"))
-
-def hxtScrollbar(master):
-    bg = master.cget("background")
-    acanvas = Canvas(master, borderwidth=0, background=bg)
-    frame = Frame(acanvas, background=bg)
-    vsb = Scrollbar(master, orient="vertical", command=acanvas.yview)
-    vsb2 = Scrollbar(master, orient='horizontal', command=acanvas.xview)
-    acanvas.configure(yscrollcommand=vsb.set)
-    acanvas.configure(xscrollcommand=vsb2.set)
-    vsb.pack(side="right", fill="y")
-    vsb2.pack(side="bottom", fill="x")
-    acanvas.pack(side="left", fill="both", expand=True)
-
-    acanvas.create_window((10, 10), window=frame, anchor="nw")
-    acanvas.bind("<Configure>", lambda event, canvas=acanvas: onFrameConfigure(acanvas))
-    acanvas.bind('<Enter>', lambda event: bindToMousewheel(event, acanvas))
-    acanvas.bind('<Leave>', lambda event: unbindToMousewheel(event,acanvas))
-    return frame
 
 class CueLightAnalyzerMenu(object):
     """
     Class for lunching cue light analysis GUI in SimBA.
 
     Parameters
     ----------
@@ -89,15 +55,16 @@
         if len(self.shape_names) == 0:
             raise CountError(msg='SIMBA ERROR: Cue light analysis require ROI definitions. Please define ROIs before doing cue light analysis')
         self.cue_light_main_frame = Toplevel()
         self.cue_light_main_frame.minsize(750, 300)
         self.cue_light_main_frame.wm_title("SIMBA CUE LIGHT ANALYZER")
         self.cue_light_main_frame.lift()
         self.lights_dict = {}
-        self.cue_light_settings_frm = LabelFrame(self.cue_light_main_frame, text='DEFINE CUE LIGHTS', font=('Helvetica', 15, 'bold'), pady=5, padx=15)
+
+        self.cue_light_settings_frm = CreateLabelFrameWithIcon(parent=self.cue_light_main_frame, header='DEFINE CUE LIGHTS', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.CUE_LIGHTS.value)
         self.choose_lights_cnt_lbl = Label(self.cue_light_settings_frm, text='# Cue lights', width=10, anchor=W)
         self.choose_lights_cnt_var = IntVar()
         self.choose_lights_cnt_var.set(1)
         self.choose_lights_cnt_dropdown = OptionMenu(self.cue_light_settings_frm, self.choose_lights_cnt_var, *list(range(1, len(self.shape_names) + 1)), command=self.__create_cue_light_menus)
         self.cue_light_settings_frm.grid(row=0, sticky=NW)
         self.choose_lights_cnt_lbl.grid(row=0, column=0, sticky=W)
         self.choose_lights_cnt_dropdown.grid(row=0, column=1, sticky=W)
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_tools.py` & `Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_visualizer.py` & `Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/cue_light_tools/cue_light_movement_statistics.py` & `Simba-UW-tf-dev-1.55.2/simba/cue_light_tools/cue_light_movement_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/extract_frames_fast.py` & `Simba-UW-tf-dev-1.55.2/simba/extract_frames_fast.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/utils/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/utils/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/utils/warnings.py` & `Simba-UW-tf-dev-1.55.2/simba/utils/warnings.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/utils/lookups.py` & `Simba-UW-tf-dev-1.55.2/simba/utils/lookups.py`

 * *Files 17% similar despite different names*

```diff
@@ -8,14 +8,15 @@
 from simba.feature_extractors.extract_features_9bp import extract_features_wotarget_9
 from simba.feature_extractors.feature_extractor_8bp import ExtractFeaturesFrom8bps
 from simba.feature_extractors.feature_extractor_8bps_2_animals import ExtractFeaturesFrom8bps2Animals
 from simba.feature_extractors.feature_extractor_7bp import ExtractFeaturesFrom7bps
 from simba.feature_extractors.feature_extractor_4bp import ExtractFeaturesFrom4bps
 from simba.feature_extractors.feature_extractor_user_defined import UserDefinedFeatureExtractor
 from simba.misc_tools import get_fn_ext
+import struct
 import simba
 
 
 def get_body_part_configurations() -> dict:
 
     """Helper to return dict with named body-part schematics of pose-estimation schemas in SimBA installation as keys,
     and paths to the images representing those body-part schematics as values.
@@ -75,8 +76,21 @@
 
 def get_third_party_appender_file_formats() -> dict:
     return {'BORIS': 'csv',
             'ETHOVISION': 'xlsx',
             'OBSERVER': 'xlsx',
             'SOLOMON': 'csv',
             'DEEPETHOGRAM': 'csv',
-            'BENTO': 'annot'}
+            'BENTO': 'annot'}
+
+
+def get_emojis() -> dict:
+    return {'thank_you': ''.join(chr(x) for x in struct.unpack('>2H', '\U0001f64f'.encode('utf-16be'))),
+            'relaxed': ''.join(chr(x) for x in struct.unpack('>2H', '\U0001F600'.encode('utf-16be'))),
+            'angry': ''.join(chr(x) for x in struct.unpack('>2H', '\U0001F92C'.encode('utf-16be')))}
+
+
+
+
+
+
+
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/utils/errors.py` & `Simba-UW-tf-dev-1.55.2/simba/utils/errors.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 from tkinter import messagebox as mb
 
+
 WINDOW_TITLE = 'SIMBA ERROR'
 
 class SimbaError(Exception):
     def __init__(self, msg: str, show_window: bool):
+        from simba.utils.lookups import get_emojis
         self.msg = msg
+        self.emojis = get_emojis()
         if show_window:
             mb.showerror(title=WINDOW_TITLE, message=msg)
 
     def __str__(self):
         return self.msg
 
 
 class NoSpecifiedOutputError(SimbaError):
     def __init__(self, msg: str, show_window: bool = False):
         super().__init__(msg=msg, show_window=show_window)
-        print(f'SIMBA ERROR: {msg}')
+        print(f'SIMBA ERROR: {msg}' + self.emojis['angry'])
 
 class ROICoordinatesNotFoundError(SimbaError):
     def __init__(self, expected_file_path: str, show_window: bool = False):
         msg = f'No ROI coordinates found. Please use the [ROI] tab to define ROIs. Expected at location {expected_file_path}'
         super().__init__(msg=msg, show_window=show_window)
         print(f'SIMBA ERROR: {msg}')
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/labelling_interface.py` & `Simba-UW-tf-dev-1.55.2/simba/labelling_interface.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/timebins_movement_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/timebins_movement_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/train_model_functions.py` & `Simba-UW-tf-dev-1.55.2/simba/train_model_functions.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/SimBA_dash_app.py` & `Simba-UW-tf-dev-1.55.2/simba/SimBA_dash_app.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/timebins_clf_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/timebins_clf_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/calculate_px_dist.py` & `Simba-UW-tf-dev-1.55.2/simba/calculate_px_dist.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/movement_processor.py` & `Simba-UW-tf-dev-1.55.2/simba/movement_processor.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pybursts.py` & `Simba-UW-tf-dev-1.55.2/simba/pybursts.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/run_model_new.py` & `Simba-UW-tf-dev-1.55.2/simba/run_model_new.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/rw_dfs.py` & `Simba-UW-tf-dev-1.55.2/simba/rw_dfs.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/reverse_2_animal_tracking.py` & `Simba-UW-tf-dev-1.55.2/simba/reverse_2_animal_tracking.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/Directing_animals_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/Directing_animals_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/Validate_model_one_video_run_clf.py` & `Simba-UW-tf-dev-1.55.2/simba/Validate_model_one_video_run_clf.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/tkinter_functions.py` & `Simba-UW-tf-dev-1.55.2/simba/tkinter_functions.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/setting_menu.py` & `Simba-UW-tf-dev-1.55.2/simba/setting_menu.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/interpolate_pose.py` & `Simba-UW-tf-dev-1.55.2/simba/interpolate_pose.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/gantt_creator.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/gantt_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/tools/tkinter_tools.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/tools/tkinter_tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_plotter_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_plotter_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/shap_agg_stats_visualizer.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/shap_agg_stats_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/gantt_creator_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/gantt_creator_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_clf_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_clf_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/probability_plot_creator.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/probability_plot_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/misc_visualizations.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/misc_visualizations.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/plot_clf_results.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/plot_clf_results.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/plot_clf_results_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/plot_clf_results_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_feature_visualizer.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_feature_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_location.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_location.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/probability_plot_creator_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/probability_plot_creator_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/interactive_probability_grapher.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/interactive_probability_grapher.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/plot_pose_in_dir.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/plot_pose_in_dir.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/single_run_model_validation_video.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/single_run_model_validation_video.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/frame_mergerer_ffmpeg.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/frame_mergerer_ffmpeg.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/Directing_animals_visualizer_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/Directing_animals_visualizer_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/clf_validator.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/clf_validator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/path_plotter_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/path_plotter_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_feature_visualizer_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_feature_visualizer_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/data_plotter.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/data_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/path_plotter.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/path_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/ez_lineplot.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/ez_lineplot.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/distance_plotter_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/distance_plotter_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/ROI_plotter.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/ROI_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_clf.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_clf.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/distance_plotter.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/distance_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/single_run_model_validation_video_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/single_run_model_validation_video_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/Directing_animals_visualizer.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/Directing_animals_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/plotting/heat_mapper_location_mp.py` & `Simba-UW-tf-dev-1.55.2/simba/plotting/heat_mapper_location_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/run_dash_tkinter.py` & `Simba-UW-tf-dev-1.55.2/simba/run_dash_tkinter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/interpolate_smooth_post_hoc.py` & `Simba-UW-tf-dev-1.55.2/simba/interpolate_smooth_post_hoc.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/dash_app.py` & `Simba-UW-tf-dev-1.55.2/simba/dash_app.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/reverse_tracking_order.py` & `Simba-UW-tf-dev-1.55.2/simba/reverse_tracking_order.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/concatenator_pop_up.py` & `Simba-UW-tf-dev-1.55.2/simba/concatenator_pop_up.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/extract_annotation_frames.py` & `Simba-UW-tf-dev-1.55.2/simba/extract_annotation_frames.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_time_bin_calculator.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_time_bin_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_movement_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_movement_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_define.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_define.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_reset.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_reset.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_feature_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_feature_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_multiply.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_multiply.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_size_calculations.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_size_calculations.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_zoom.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_zoom.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_directing_analyzer.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_directing_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_move_shape.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_move_shape.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_menus.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_menus.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_clf_calculator.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_clf_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/roi_tools/ROI_image.py` & `Simba-UW-tf-dev-1.55.2/simba/roi_tools/ROI_image.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/misc_tools.py` & `Simba-UW-tf-dev-1.55.2/simba/misc_tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/read_DANNCE_mat.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/read_DANNCE_mat.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/sleap_importer_slp.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/sleap_importer_slp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/sleap_importer_h5.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/sleap_importer_h5.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/dlc_multi_animal_importer.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/dlc_multi_animal_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/sleap_importer_csv.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/sleap_importer_csv.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/import_trk.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/import_trk.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/import_mars.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/import_mars.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/dlc_importer_csv.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/dlc_importer_csv.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_importers/trk_importer.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_importers/trk_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pop_up_classes.py` & `Simba-UW-tf-dev-1.55.2/simba/pop_up_classes.py`

 * *Files 0% similar despite different names*

```diff
@@ -3456,15 +3456,17 @@
         self.feature_subset_options = ['Two-point body-part distances (mm)',
                                        'Within-animal three-point body-part angles (degrees)',
                                        'Within-animal three-point convex hull perimeters (mm)',
                                        'Within-animal four-point convex hull perimeters (mm)',
                                        'Entire animal convex hull perimeters (mm)',
                                        'Entire animal convex hull area (mm2)',
                                        'Frame-by-frame body-part movements (mm)',
-                                       'Frame-by-frame distance to ROI centers (mm)']
+                                       'Frame-by-frame distance to ROI centers (mm)',
+                                       'Frame-by-frame body-parts inside ROIs (Boolean)']
+
         self.config_path = config_path
         self.settings_frm = CreateLabelFrameWithIcon(parent=self.main_frm, header='SETTINGS', icon_name='documentation', icon_link=Links.FEATURE_SUBSETS.value)
         self.feature_family_dropdown = DropDownMenu(self.settings_frm, 'FEATURE FAMILY:', self.feature_subset_options, '20')
         self.feature_family_dropdown.setChoices(self.feature_subset_options[0])
         self.save_dir = FolderSelect(self.settings_frm, 'SAVE DIRECTORY:', lblwidth=20)
         self.create_run_frm(run_function=self.run)
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/extract_seqframes.py` & `Simba-UW-tf-dev-1.55.2/simba/extract_seqframes.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/bp_names/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/bp_names/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/bp_names/bp_names.csv` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/bp_names/bp_names.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/no_animals/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/no_animals/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/configuration_names/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/configuration_names/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/8.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/8.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/9.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/9.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/12.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/12.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/11.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/11.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/10.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/10.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/4.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/4.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/5.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/5.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/7.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/7.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/6.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/6.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/2.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/2.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/3.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/3.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_configurations/schematics/1.png` & `Simba-UW-tf-dev-1.55.2/simba/pose_configurations/schematics/1.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/get_coordinates_tools_v2.py` & `Simba-UW-tf-dev-1.55.2/simba/get_coordinates_tools_v2.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pup_retrieval_protocol.py` & `Simba-UW-tf-dev-1.55.2/simba/pup_retrieval_protocol.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/outlier_tools/outlier_corrector_movement.py` & `Simba-UW-tf-dev-1.55.2/simba/outlier_tools/outlier_corrector_movement.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/outlier_tools/outlier_corrector_location.py` & `Simba-UW-tf-dev-1.55.2/simba/outlier_tools/outlier_corrector_location.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/outlier_tools/skip_outlier_correction.py` & `Simba-UW-tf-dev-1.55.2/simba/outlier_tools/skip_outlier_correction.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/outlier_scripts.iml` & `Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/outlier_scripts.iml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml` & `Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/outlier_tools/.idea/workspace.xml` & `Simba-UW-tf-dev-1.55.2/simba/outlier_tools/.idea/workspace.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/pose_reset.py` & `Simba-UW-tf-dev-1.55.2/simba/pose_reset.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/train_mutiple_models.py` & `Simba-UW-tf-dev-1.55.2/simba/train_mutiple_models.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/SimBA.py` & `Simba-UW-tf-dev-1.55.2/simba/SimBA.py`

 * *Files 2% similar despite different names*

```diff
@@ -110,27 +110,30 @@
 from simba.enums import (Formats,
                          OS,
                          Defaults)
 from simba.utils.lookups import get_bp_config_code_class_pairs, get_icons_paths
 from simba.mixins.pop_up_mixin import PopUpMixin
 from simba.create_project_pop_up import ProjectCreatorPopUp
 from simba.plotly_create_h5 import create_plotly_container
+from simba.utils.lookups import get_emojis
 #from simba.unsupervised.unsupervised_ui import UnsupervisedGUI
 import sys
 import subprocess
 
 sys.setrecursionlimit(10 ** 6)
 currentPlatform = platform.system()
 
 class LoadProjectPopUp(object):
     def __init__(self):
         main_frm = Toplevel()
         main_frm.minsize(300, 200)
         main_frm.wm_title("Load SimBA project (project_config.ini file)")
-        load_project_frm = LabelFrame(main_frm, text='LOAD SIMBA PROJECT_CONFIG.INI', font=("Helvetica", 12, 'bold'), pady=5, padx=5, fg='black')
+
+
+        load_project_frm = CreateLabelFrameWithIcon(parent=main_frm, header='LOAD SIMBA PROJECT_CONFIG.INI', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.LOAD_PROJECT.value)
         self.selected_file = FileSelect(load_project_frm,'Select file: ', title='Select project_config.ini file')
         load_project_btn = Button(load_project_frm, text='LOAD PROJECT', font=("Helvetica", 12, 'bold'), command=lambda: self.launch_project())
 
         load_project_frm.grid(row=0)
         self.selected_file.grid(row=0,sticky=NW)
         load_project_btn.grid(row=1,pady=10, sticky=NW)
 
@@ -189,15 +192,16 @@
 
         tab_parent.grid(row=0)
         tab_parent.enable_traversal()
 
         import_frm = LabelFrame(tab2)
         import_frm.grid(row=0, column=0, sticky=NW)
 
-        further_methods_frm = LabelFrame(import_frm, text='FURTHER METHODS', font=Formats.LABELFRAME_HEADER_FORMAT.value, pady=5, padx=5, fg='black')
+
+        further_methods_frm = CreateLabelFrameWithIcon(parent=import_frm, header='FURTHER METHODS', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.ADDITIONAL_IMPORTS.value)
         extract_frm_btn = Button(further_methods_frm, text='EXTRACT FRAMES FOR ALL VIDEOS IN SIMBA PROJECT', fg='blue', command= lambda: extract_frames_from_all_videos_in_directory(config_path=self.config_path, directory=self.video_dir))
         import_frm_dir_btn = Button(further_methods_frm,text='IMPORT FRAMES DIRECTORY TO SIMBA PROJECT', fg='blue', command=lambda: ImportFrameDirectoryPopUp(config_path=self.config_path))
         add_clf_btn = Button(further_methods_frm, text='ADD CLASSIFIER TO SIMBA PROJECT', fg='blue', command=lambda: AddClfPopUp(config_path=self.config_path))
         remove_clf_btn = Button(further_methods_frm, text='REMOVE CLASSIFIER FROM SIMBA PROJECT', fg='blue', command=lambda: RemoveAClassifierPopUp(config_path=self.config_path))
         archive_files_btn = Button(further_methods_frm, text='ARCHIVE PROCESSED FILES IN SIMBA PROJECT', fg='blue', command=lambda: ArchiveProcessedFilesPopUp(config_path=self.config_path))
         reverse_btn = Button(further_methods_frm, text='REVERSE TRACKING IDENTITIES IN SIMBA PROJECT',fg='blue', command=lambda: self.reverseid())
         interpolate_btn = Button(further_methods_frm, text='INTERPOLATE POSE IN SIMBA PROJECT', fg='blue', command=lambda: InterpolatePopUp(config_path=self.config_path))
@@ -207,28 +211,26 @@
         #label_setscale = LabelFrame(tab3,text='VIDEO PARAMETERS (FPS, RESOLUTION, PPX/MM ....)', font=Formats.LABELFRAME_HEADER_FORMAT.value, pady=5,padx=5,fg='black')
         self.distance_in_mm_eb = Entry_Box(label_setscale, 'KNOWN DISTANCE (MILLIMETERS)', '25', validation='numeric')
         button_setdistanceinmm = Button(label_setscale, text='AUTO-POPULATE', fg='green', command=lambda: self.set_distance_mm())
 
         button_setscale = Button(label_setscale, text='CONFIGURE VIDEO PARAMETERS', compound='left', image=self.btn_icons['calipher']['img'], relief=RAISED, fg='blue', command=lambda: self.create_video_info_table())
         button_setscale.image = self.btn_icons['calipher']['img']
 
-        self.new_ROI_frm = LabelFrame(tab6, text='SIMBA ROI INTERFACE', font=Formats.LABELFRAME_HEADER_FORMAT.value)
+
+
+        self.new_ROI_frm = CreateLabelFrameWithIcon(parent=tab6, header='SIMBA ROI INTERFACE', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.ROI.value)
         self.start_new_ROI = Button(self.new_ROI_frm, text='DEFINE ROIs', fg='green', compound='left', image=self.btn_icons['roi']['img'], relief=RAISED, command= lambda: ROI_menu(self.config_path))
         self.start_new_ROI.image = self.btn_icons['roi']['img']
 
         self.delete_all_ROIs = Button(self.new_ROI_frm, text='DELETE ALL ROI DEFINITIONS', fg='red', compound='left', image=self.btn_icons['trash']['img'], command=lambda: delete_all_ROIs(self.config_path))
         self.delete_all_ROIs.image = self.btn_icons['trash']['img']
 
-        self.tutorial_link = Label(self.new_ROI_frm, text='[Link to ROI user-guide]', cursor='hand2',  font='Verdana 8 underline')
-        self.tutorial_link.bind("<Button-1>", lambda e: self.callback('https://github.com/sgoldenlab/simba/blob/master/docs/ROI_tutorial_new.md'))
-
         self.new_ROI_frm.grid(row=0, sticky=NW)
         self.start_new_ROI.grid(row=0, sticky=NW)
         self.delete_all_ROIs.grid(row=1, column=0, sticky=NW)
-        self.tutorial_link.grid(row=2, sticky=W)
 
         self.roi_draw = LabelFrame(tab6, text='ANALYZE ROI DATA', font=Formats.LABELFRAME_HEADER_FORMAT.value)
         analyze_roi_btn = Button(self.roi_draw, text='ANALYZE ROI DATA: AGGREGATES', fg='green', command=lambda: SettingsMenu(config_path=self.config_path, title='ROI ANALYSIS'))
         analyze_roi_time_bins_btn = Button(self.roi_draw, text='ANALYZE ROI DATA: TIME-BINS',  fg='blue', command=lambda: SettingsMenu(config_path=self.config_path, title='TIME BINS: ANALYZE ROI'))
 
         self.roi_draw.grid(row=0, column=1, sticky=N)
         analyze_roi_btn.grid(row=0, sticky='NW')
@@ -364,15 +366,16 @@
         button_runvalidmodel = Button(label_model_validation, text='RUN MODEL', fg='blue', command=lambda: self.validate_model_first_step())
 
         button_generateplot = Button(label_model_validation, text="INTERACTIVE PROBABILITY PLOT", fg='blue', command= lambda: self.launch_interactive_plot())
         self.dis_threshold = Entry_Box(label_model_validation, 'DISCRIMINATION THRESHOLD (0.0-1.0):', '30')
         self.min_behaviorbout = Entry_Box(label_model_validation, 'MINIMUM BOUT LENGTH (MS):', '30', validation='numeric')
         button_validate_model = Button(label_model_validation, text='CREATE VALIDATION VIDEO', fg='blue', command= lambda: ValidationVideoPopUp(config_path=config_path, simba_main_frm=self))
 
-        label_runmachinemodel = LabelFrame(tab9,text='RUN MACHINE MODEL',font=Formats.LABELFRAME_HEADER_FORMAT.value, padx=5, pady=5, fg='black')
+
+        label_runmachinemodel = CreateLabelFrameWithIcon(parent=tab9, header='RUN MACHINE MODEL', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.SCENARIO_2.value)
         button_run_rfmodelsettings = Button(label_runmachinemodel,text='MODEL SETTINGS', fg='green', compound='left', image=self.btn_icons['settings']['img'], command= lambda: SetMachineModelParameters(config_path=self.config_path))
         button_run_rfmodelsettings.image = self.btn_icons['settings']['img']
 
         button_runmachinemodel = Button(label_runmachinemodel,text='RUN MODELS', fg='green', compound='left', image=self.btn_icons['clf']['img'], command=self.runrfmodel)
         button_runmachinemodel.image = self.btn_icons['clf']['img']
 
         kleinberg_button = Button(label_runmachinemodel,text='KLEINBERG SMOOTHING', fg='green', command=lambda: KleinbergPopUp(config_path=self.config_path))
@@ -716,14 +719,15 @@
         webbrowser.open_new(url)
 
 
 
 class App(object):
     def __init__(self):
         bg_path = os.path.join(os.path.dirname(__file__), Paths.BG_IMG_PATH.value)
+        emojis = get_emojis()
         icon_path_windows = os.path.join(os.path.dirname(__file__), Paths.LOGO_ICON_WINDOWS_PATH.value)
         icon_path_darwin = os.path.join(os.path.dirname(__file__), Paths.LOGO_ICON_DARWIN_PATH.value)
         self.menu_icons = get_icons_paths()
         self.root = Tk()
         self.root.title('SimBA')
         self.root.minsize(750,750)
         self.root.geometry(Formats.ROOT_WINDOW_SIZE.value)
@@ -732,15 +736,15 @@
         if currentPlatform == OS.WINDOWS.value:
             self.root.iconbitmap(icon_path_windows)
         if currentPlatform == OS.MAC.value:
             self.root.iconphoto(False, ImageTk.PhotoImage(PIL.Image.open(icon_path_darwin)))
         for k in self.menu_icons.keys():
             self.menu_icons[k]['img'] = ImageTk.PhotoImage(image=PIL.Image.open(os.path.join(os.path.dirname(__file__), self.menu_icons[k]['icon_path'])))
         bg_img = PhotoImage(file=bg_path)
-        background = Label(self.root, image=bg_img, bd=0)
+        background = Label(self.root, image=bg_img, bd=0, bg='white')
         background.pack(fill='both', expand=True)
         background.image = bg_img
 
         menu = Menu(self.root)
         self.root.config(menu=menu)
 
         file_menu = Menu(menu)
@@ -808,19 +812,25 @@
         links_menu.add_command(label='SimBA github', command=lambda: webbrowser.open_new(str(r'https://github.com/sgoldenlab/simba')))
         links_menu.add_command(label='Gitter Chatroom', command=lambda: webbrowser.open_new(str(r'https://gitter.im/SimBA-Resource/community')))
         links_menu.add_command(label='Install FFmpeg',command =lambda: webbrowser.open_new(str(r'https://m.wikihow.com/Install-FFmpeg-on-Windows')))
         links_menu.add_command(label='Install graphviz', command=lambda: webbrowser.open_new(str(r'https://bobswift.atlassian.net/wiki/spaces/GVIZ/pages/20971549/How+to+install+Graphviz+software')))
         help_menu.add_cascade(label="Links",menu=links_menu, compound='left', image=self.menu_icons['link']['img'])
         help_menu.add_command(label='About', compound='left', image=self.menu_icons['about']['img'], command=AboutSimBAPopUp)
 
-        self.frame = Frame(background, bd=2, relief=SUNKEN, width=300, height=300)
+        self.frame = Frame(background, bd=2, relief=SUNKEN, width=750, height=300)
+        y_sb = Scrollbar(self.frame, orient=VERTICAL)
         self.frame.pack(expand=True)
-        self.txt = Text(self.frame, bg='white')
-        self.txt.config(state=DISABLED, font=Formats.TKINTER_FONT.value)
+        self.txt = Text(self.frame, bg='white', insertborderwidth=2, height=40, width=100, yscrollcommand=y_sb)
+        self.txt.tag_configure("center", justify='center', foreground='blue', font=("Rockwell", 16, 'bold'))
+        self.txt.insert(INSERT, Defaults.WELCOME_MSG.value + emojis['relaxed'] + '\n' * 2)
+        self.txt.tag_add("center", "1.0", "2.25")
+        y_sb.pack(side=RIGHT, fill=Y)
         self.txt.pack(expand=True, fill='both')
+        y_sb.config(command=self.txt.yview)
+        self.txt.config(state=DISABLED, font=Formats.TKINTER_FONT.value)
         sys.stdout = StdRedirector(self.txt)
 
     def restart(self):
         confirm_restart = askyesno(title='RESTART', message='Are you sure that you want restart SimBA?')
         if confirm_restart:
             self.root.destroy()
             python = sys.executable
@@ -880,9 +890,9 @@
         ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
     root = Tk()
     root.overrideredirect(True)
     _ = SplashScreen(root)
     root.after(Defaults.SPLASH_TIME.value, root.destroy)
     root.mainloop()
     app = App()
-    print(Defaults.WELCOME_MSG.value)
+    #print(Defaults.WELCOME_MSG.value)
     app.root.mainloop()
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/labelling_advanced_interface.py` & `Simba-UW-tf-dev-1.55.2/simba/labelling_advanced_interface.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/unsupervised/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/assets/unsupervised/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/unsupervised/model_names.parquet` & `Simba-UW-tf-dev-1.55.2/simba/assets/unsupervised/model_names.parquet`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/unsupervised/features.csv` & `Simba-UW-tf-dev-1.55.2/simba/assets/unsupervised/features.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/down_arrow.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/down_arrow.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/intruder_shape.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/intruder_shape.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/feature_categories/shap_feature_categories.csv` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/feature_categories/shap_feature_categories.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_shape.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_shape.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_intruder_shape.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_intruder_shape.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/animal_distances.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/animal_distances.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/baseline_scale.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/baseline_scale.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/ubuntu.regular.ttf` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/ubuntu.regular.ttf`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/side_scale.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/side_scale.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/UbuntuMono-Regular.ttf` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/UbuntuMono-Regular.ttf`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/side_scale_5.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/side_scale_5.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/intruder_movement.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/intruder_movement.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_movement.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_movement.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/color_bar.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/color_bar.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/shap/resident_intruder_movement.jpg` & `Simba-UW-tf-dev-1.55.2/simba/assets/shap/resident_intruder_movement.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/assets/.DS_Store`

 * *Files 10% similar despite different names*

```diff
@@ -484,37 +484,37 @@
 00001e30: 010a 010b 010c 0118 0121 0122 0124 0125  .........!.".$.%
 00001e40: 012a 0133 0134 0136 0137 013c 0145 0146  .*.3.4.6.7.<.E.F
 00001e50: 0148 0149 014f 0158 0159 015b 015c 0164  .H.I.O.X.Y.[.\.d
 00001e60: 016d 016e 0171 0172 017b 0184 0185 0187  .m.n.q.r.{......
 00001e70: 0188 0197 01a0 01a1 01a2 01ac 01ad 01b6  ................
 00001e80: 01bb 01c4 0000 0000 0000 0201 0000 0000  ................
 00001e90: 0000 004a 0000 0000 0000 0000 0000 0000  ...J............
-00001ea0: 0000 01c5 36ee c441 0000 0005 0069 0063  ....6..A.....i.c
+00001ea0: 0000 01c5 eeee c441 0000 0005 0069 0063  .......A.....i.c
 00001eb0: 006f 006e 0073 6d6f 6444 626c 6f62 0000  .o.n.smodDblob..
-00001ec0: 0008 81c7 e5e4 36ee c441 0000 0005 0069  ......6..A.....i
+00001ec0: 0008 7ef0 e459 eeee c441 0000 0005 0069  ..~..Y...A.....i
 00001ed0: 0063 006f 006e 0073 7068 3153 636f 6d70  .c.o.n.sph1Scomp
-00001ee0: 0000 0000 0007 c000 0000 0005 0069 0063  .............i.c
+00001ee0: 0000 0000 0007 e000 0000 0005 0069 0063  .............i.c
 00001ef0: 006f 006e 0073 7653 726e 6c6f 6e67 0000  .o.n.svSrnlong..
 00001f00: 0001 0000 0003 0069 006d 0067 6277 7370  .......i.m.gbwsp
-00001f10: 626c 6f62 0000 00ca 6270 6c69 7374 3030  blob....bplist00
+00001f10: 626c 6f62 0000 00c9 6270 6c69 7374 3030  blob....bplist00
 00001f20: d701 0203 0405 0607 0808 0a08 0a0d 0a5d  ...............]
 00001f30: 5368 6f77 5374 6174 7573 4261 725b 5368  ShowStatusBar[Sh
 00001f40: 6f77 5061 7468 6261 725b 5368 6f77 546f  owPathbar[ShowTo
 00001f50: 6f6c 6261 725b 5368 6f77 5461 6256 6965  olbar[ShowTabVie
 00001f60: 775f 1014 436f 6e74 6169 6e65 7253 686f  w_..ContainerSho
 00001f70: 7753 6964 6562 6172 5c57 696e 646f 7742  wSidebar\WindowB
 00001f80: 6f75 6e64 735b 5368 6f77 5369 6465 6261  ounds[ShowSideba
-00001f90: 7208 0809 0809 5f10 197b 7b33 3535 2c20  r....._..{{355, 
-00001fa0: 3132 357d 2c20 7b31 3037 362c 2036 3231  125}, {1076, 621
-00001fb0: 7d7d 0908 1725 313d 4960 6d79 7a7b 7c7d  }}...%1=I`myz{|}
-00001fc0: 7e9a 0000 0000 0000 0101 0000 0000 0000  ~...............
-00001fd0: 000f 0000 0000 0000 0000 0000 0000 0000  ................
-00001fe0: 009b 0000 0003 0069 006d 0067 6c67 3153  .......i.m.glg1S
-00001ff0: 636f 6d70 0000 0000 000f 4cf2 0000 0003  comp......L.....
-00002000: 0069 006d 0000 0000 0000 0012 0000 0005  .i.m............
+00001f90: 7208 0809 0809 5f10 187b 7b32 302c 2031  r....._..{{20, 1
+00001fa0: 3232 7d2c 207b 3130 3736 2c20 3632 317d  22}, {1076, 621}
+00001fb0: 7d09 0817 2531 3d49 606d 797a 7b7c 7d7e  }...%1=I`myz{|}~
+00001fc0: 9900 0000 0000 0001 0100 0000 0000 0000  ................
+00001fd0: 0f00 0000 0000 0000 0000 0000 0000 0000  ................
+00001fe0: 9a00 0000 0300 6900 6d00 676c 6731 5363  ......i.m.glg1Sc
+00001ff0: 6f6d 7000 0000 0000 0f4c f200 0000 0300  omp......L......
+00002000: 6900 6d00 0000 0000 0000 0012 0000 0005  i.m.............
 00002010: 0069 0063 006f 006e 0073 6277 7370 626c  .i.c.o.n.sbwspbl
 00002020: 6f62 0000 00c9 6270 6c69 7374 3030 d701  ob....bplist00..
 00002030: 0203 0405 0607 0808 0a08 0a0d 0a5d 5368  .............]Sh
 00002040: 6f77 5374 6174 7573 4261 725b 5368 6f77  owStatusBar[Show
 00002050: 5061 7468 6261 725b 5368 6f77 546f 6f6c  Pathbar[ShowTool
 00002060: 6261 725b 5368 6f77 5461 6256 6965 775f  bar[ShowTabView_
 00002070: 1014 436f 6e74 6169 6e65 7253 686f 7753  ..ContainerShowS
@@ -522,15 +522,15 @@
 00002090: 6e64 735b 5368 6f77 5369 6465 6261 7208  nds[ShowSidebar.
 000020a0: 0809 0809 5f10 187b 7b32 302c 2031 3232  ...._..{{20, 122
 000020b0: 7d2c 207b 3130 3736 2c20 3632 317d 7d09  }, {1076, 621}}.
 000020c0: 0817 2531 3d49 606d 797a 7b7c 7d7e 9900  ..%1=I`myz{|}~..
 000020d0: 0000 0000 0001 0100 0000 0000 0000 0f00  ................
 000020e0: 0000 0000 0000 0000 0000 0000 0000 9a00  ................
 000020f0: 0000 0500 6900 6300 6f00 6e00 736c 6731  ....i.c.o.n.slg1
-00002100: 5363 6f6d 7000 0000 0000 0584 0400 0000  Scomp...........
+00002100: 5363 6f6d 7000 0000 0000 058b 9300 0000  Scomp...........
 00002110: 0500 6900 6300 6f00 6e00 736c 7376 4362  ..i.c.o.n.slsvCb
 00002120: 6c6f 6200 0002 b062 706c 6973 7430 30da  lob....bplist00.
 00002130: 0102 0304 0506 0708 090a 0b0c 0d18 4849  ..............HI
 00002140: 484a 4b0c 5f10 1276 6965 774f 7074 696f  HJK._..viewOptio
 00002150: 6e73 5665 7273 696f 6e5f 100f 7368 6f77  nsVersion_..show
 00002160: 4963 6f6e 5072 6576 6965 7757 636f 6c75  IconPreviewWcolu
 00002170: 6d6e 735f 1011 6361 6c63 756c 6174 6541  mns_..calculateA
@@ -612,140 +612,140 @@
 00002630: 017d 017e 0187 0189 018b 018c 018d 0196  .}.~............
 00002640: 0198 019a 019b 019c 01a5 01a7 01a9 01aa  ................
 00002650: 01ab 01b4 01b6 01b9 01ba 01bb 01bc 01c5  ................
 00002660: 01ce 01d3 01dc 0000 0000 0000 0201 0000  ................
 00002670: 0000 0000 004c 0000 0000 0000 0000 0000  .....L..........
 00002680: 0000 0000 01dd 0000 0005 0069 0063 006f  ...........i.c.o
 00002690: 006e 0073 6d6f 4444 626c 6f62 0000 0008  .n.smoDDblob....
-000026a0: 81c7 e5e4 36ee c441 0000 0005 0069 0063  ....6..A.....i.c
+000026a0: 7ef0 e459 eeee c441 0000 0005 0069 0063  ~..Y...A.....i.c
 000026b0: 006f 006e 0073 6d6f 6444 626c 6f62 0000  .o.n.smodDblob..
-000026c0: 0008 81c7 e5e4 36ee c441 0000 0005 0069  ......6..A.....i
+000026c0: 0008 7ef0 e459 eeee c441 0000 0005 0069  ..~..Y...A.....i
 000026d0: 0063 006f 006e 0073 7068 3153 636f 6d70  .c.o.n.sph1Scomp
-000026e0: 0000 0000 0007 c000 0000 0005 0069 0063  .............i.c
+000026e0: 0000 0000 0007 e000 0000 0005 0069 0063  .............i.c
 000026f0: 006f 006e 0073 7653 726e 6c6f 6e67 0000  .o.n.svSrnlong..
 00002700: 0001 0000 0003 0069 006d 0067 6277 7370  .......i.m.gbwsp
-00002710: 626c 6f62 0000 00ca 6270 6c69 7374 3030  blob....bplist00
+00002710: 626c 6f62 0000 00c9 6270 6c69 7374 3030  blob....bplist00
 00002720: d701 0203 0405 0607 0808 0a08 0a0d 0a5d  ...............]
 00002730: 5368 6f77 5374 6174 7573 4261 725b 5368  ShowStatusBar[Sh
 00002740: 6f77 5061 7468 6261 725b 5368 6f77 546f  owPathbar[ShowTo
 00002750: 6f6c 6261 725b 5368 6f77 5461 6256 6965  olbar[ShowTabVie
 00002760: 775f 1014 436f 6e74 6169 6e65 7253 686f  w_..ContainerSho
 00002770: 7753 6964 6562 6172 5c57 696e 646f 7742  wSidebar\WindowB
 00002780: 6f75 6e64 735b 5368 6f77 5369 6465 6261  ounds[ShowSideba
-00002790: 7208 0809 0809 5f10 197b 7b33 3535 2c20  r....._..{{355, 
-000027a0: 3132 357d 2c20 7b31 3037 362c 2036 3231  125}, {1076, 621
-000027b0: 7d7d 0908 1725 313d 4960 6d79 7a7b 7c7d  }}...%1=I`myz{|}
-000027c0: 7e9a 0000 0000 0000 0101 0000 0000 0000  ~...............
-000027d0: 000f 0000 0000 0000 0000 0000 0000 0000  ................
-000027e0: 009b 0000 0003 0069 006d 0067 6c67 3153  .......i.m.glg1S
-000027f0: 636f 6d70 0000 0000 000f 4cf2 0000 0003  comp......L.....
-00002800: 0069 006d 0067 6c73 7643 626c 6f62 0000  .i.m.glsvCblob..
-00002810: 0279 6270 6c69 7374 3030 d801 0203 0405  .ybplist00......
-00002820: 0607 0809 090b 1646 4748 495f 1010 7573  .......FGHI_..us
-00002830: 6552 656c 6174 6976 6544 6174 6573 5f10  eRelativeDates_.
-00002840: 0f73 686f 7749 636f 6e50 7265 7669 6577  .showIconPreview
-00002850: 5763 6f6c 756d 6e73 5f10 1163 616c 6375  Wcolumns_..calcu
-00002860: 6c61 7465 416c 6c53 697a 6573 5874 6578  lateAllSizesXtex
-00002870: 7453 697a 655a 736f 7274 436f 6c75 6d6e  tSizeZsortColumn
-00002880: 5869 636f 6e53 697a 655f 1012 7669 6577  XiconSize_..view
-00002890: 4f70 7469 6f6e 7356 6572 7369 6f6e 0909  OptionsVersion..
-000028a0: ab0c 151a 1f23 282d 3237 3c41 d40d 0e0f  .....#(-27<A....
-000028b0: 1009 1209 1457 7669 7369 626c 6555 7769  .....WvisibleUwi
-000028c0: 6474 6859 6173 6365 6e64 696e 675a 6964  dthYascendingZid
-000028d0: 656e 7469 6669 6572 0911 0127 0954 6e61  entifier...'.Tna
-000028e0: 6d65 d40d 0e0f 1016 1716 1908 1023 0858  me...........#.X
-000028f0: 7562 6971 7569 7479 d40d 0e0f 1009 1c16  ubiquity........
-00002900: 1e09 10b5 085c 6461 7465 4d6f 6469 6669  .....\dateModifi
-00002910: 6564 d40d 0e0f 1016 1c16 2208 085b 6461  ed........"..[da
-00002920: 7465 4372 6561 7465 64d4 0d0e 0f10 0925  teCreated......%
-00002930: 1627 0910 6108 5473 697a 65d4 0d0e 0f10  .'..a.Tsize.....
-00002940: 092a 092c 0910 7309 546b 696e 64d4 0d0e  .*.,..s.Tkind...
-00002950: 0f10 162f 0931 0810 6409 556c 6162 656c  .../.1..d.Ulabel
-00002960: d40d 0e0f 1016 3409 3608 104b 0957 7665  ......4.6..K.Wve
-00002970: 7273 696f 6ed4 0d0e 0f10 1639 093b 0811  rsion......9.;..
-00002980: 012c 0958 636f 6d6d 656e 7473 d40d 0e0f  .,.Xcomments....
-00002990: 1016 3e16 4008 10c8 085e 6461 7465 4c61  ..>.@....^dateLa
-000029a0: 7374 4f70 656e 6564 d40d 0e0f 1016 1c16  stOpened........
-000029b0: 4408 0859 6461 7465 4164 6465 6408 2340  D..YdateAdded.#@
-000029c0: 2800 0000 0000 0054 6e61 6d65 2340 3000  (......Tname#@0.
-000029d0: 0000 0000 0010 0100 0800 1900 2c00 3e00  ............,.>.
-000029e0: 4600 5a00 6300 6e00 7700 8c00 8d00 8e00  F.Z.c.n.w.......
-000029f0: 9a00 a300 ab00 b100 bb00 c600 c700 ca00  ................
-00002a00: cb00 d000 d900 da00 dc00 dd00 e600 ef00  ................
-00002a10: f000 f200 f301 0001 0901 0a01 0b01 1701  ................
-00002a20: 2001 2101 2301 2401 2901 3201 3301 3501   .!.#.$.).2.3.5.
-00002a30: 3601 3b01 4401 4501 4701 4801 4e01 5701  6.;.D.E.G.H.N.W.
-00002a40: 5801 5a01 5b01 6301 6c01 6d01 7001 7101  X.Z.[.c.l.m.p.q.
-00002a50: 7a01 8301 8401 8601 8701 9601 9f01 a001  z...............
-00002a60: a101 ab01 ac01 b501 ba01 c300 0000 0000  ................
-00002a70: 0002 0100 0000 0000 0000 4a00 0000 0000  ..........J.....
-00002a80: 0000 0000 0000 0000 0001 c500 0000 0300  ................
-00002a90: 6900 6d00 676c 7376 7062 6c6f 6200 0002  i.m.glsvpblob...
-00002aa0: 5e62 706c 6973 7430 30d8 0102 0304 0506  ^bplist00.......
-00002ab0: 0708 0909 0b1d 4647 4824 5f10 1075 7365  ......FGH$_..use
-00002ac0: 5265 6c61 7469 7665 4461 7465 735f 100f  RelativeDates_..
-00002ad0: 7368 6f77 4963 6f6e 5072 6576 6965 7757  showIconPreviewW
-00002ae0: 636f 6c75 6d6e 735f 1011 6361 6c63 756c  columns_..calcul
-00002af0: 6174 6541 6c6c 5369 7a65 7358 7465 7874  ateAllSizesXtext
-00002b00: 5369 7a65 5a73 6f72 7443 6f6c 756d 6e58  SizeZsortColumnX
-00002b10: 6963 6f6e 5369 7a65 5f10 1276 6965 774f  iconSize_..viewO
-00002b20: 7074 696f 6e73 5665 7273 696f 6e09 09d9  ptionsVersion...
-00002b30: 0c0d 0e0f 1011 1213 1415 1e23 282c 3136  ...........#(,16
-00002b40: 3b40 5863 6f6d 6d65 6e74 735e 6461 7465  ;@Xcomments^date
-00002b50: 4c61 7374 4f70 656e 6564 5c64 6174 654d  LastOpened\dateM
-00002b60: 6f64 6966 6965 645b 6461 7465 4372 6561  odified[dateCrea
-00002b70: 7465 6454 7369 7a65 556c 6162 656c 546b  tedTsizeUlabelTk
-00002b80: 696e 6457 7665 7273 696f 6e54 6e61 6d65  indWversionTname
-00002b90: d416 1718 191a 1b09 1d55 696e 6465 7855  .........UindexU
-00002ba0: 7769 6474 6859 6173 6365 6e64 696e 6757  widthYascendingW
-00002bb0: 7669 7369 626c 6510 0711 012c 0908 d416  visible....,....
-00002bc0: 1718 191f 201d 1d10 0810 c808 08d4 1617  .... ...........
-00002bd0: 1819 2425 1d09 1001 10b5 0809 d416 1718  ..$%............
-00002be0: 1929 251d 1d10 0208 08d4 1617 1819 2d2e  .)%...........-.
-00002bf0: 1d09 1003 1061 0809 d416 1718 1932 3309  .....a.......23.
-00002c00: 1d10 0510 6409 08d4 1617 1819 3738 0909  ....d.......78..
-00002c10: 1004 1073 0909 d416 1718 193c 3d09 1d10  ...s.......<=...
-00002c20: 0610 4b09 08d4 1617 1819 4142 0909 1000  ..K.......AB....
-00002c30: 1101 2709 0908 2340 2800 0000 0000 0054  ..'...#@(......T
-00002c40: 6e61 6d65 2340 3000 0000 0000 0000 0800  name#@0.........
-00002c50: 1900 2c00 3e00 4600 5a00 6300 6e00 7700  ..,.>.F.Z.c.n.w.
-00002c60: 8c00 8d00 8e00 a100 aa00 b900 c600 d200  ................
-00002c70: d700 dd00 e200 ea00 ef00 f800 fe01 0401  ................
-00002c80: 0e01 1601 1801 1b01 1c01 1d01 2601 2801  ............&.(.
-00002c90: 2a01 2b01 2c01 3501 3701 3901 3a01 3b01  *.+.,.5.7.9.:.;.
-00002ca0: 4401 4601 4701 4801 5101 5301 5501 5601  D.F.G.H.Q.S.U.V.
-00002cb0: 5701 6001 6201 6401 6501 6601 6f01 7101  W.`.b.d.e.f.o.q.
-00002cc0: 7301 7401 7501 7e01 8001 8201 8301 8401  s.t.u.~.........
-00002cd0: 8d01 8f01 9201 9301 9401 9501 9e01 a300  ................
-00002ce0: 0000 0000 0002 0100 0000 0000 0000 4900  ..............I.
-00002cf0: 0000 0000 0000 0000 0000 0000 0001 ac00  ................
-00002d00: 0000 0300 6900 6d00 676d 6f44 4462 6c6f  ....i.m.gmoDDblo
-00002d10: 6200 0000 08b8 f4ea d3d4 e1c4 4100 0000  b...........A...
-00002d20: 0300 6900 6d00 676d 6f64 4462 6c6f 6200  ..i.m.gmodDblob.
-00002d30: 0000 08b8 f4ea d3d4 e1c4 4100 0000 0300  ..........A.....
-00002d40: 6900 6d00 6770 6831 5363 6f6d 7000 0000  i.m.gph1Scomp...
-00002d50: 0000 0f60 0000 0000 0300 6900 6d00 6776  ...`......i.m.gv
-00002d60: 5372 6e6c 6f6e 6700 0000 0100 0000 0700  Srnlong.........
-00002d70: 6c00 6f00 6f00 6b00 7500 7000 7362 7773  l.o.o.k.u.p.sbws
-00002d80: 7062 6c6f 6200 0000 c862 706c 6973 7430  pblob....bplist0
-00002d90: 30d7 0102 0304 0506 0708 080a 080a 0d0a  0...............
-00002da0: 5d53 686f 7753 7461 7475 7342 6172 5b53  ]ShowStatusBar[S
-00002db0: 686f 7750 6174 6862 6172 5b53 686f 7754  howPathbar[ShowT
-00002dc0: 6f6f 6c62 6172 5b53 686f 7754 6162 5669  oolbar[ShowTabVi
-00002dd0: 6577 5f10 1443 6f6e 7461 696e 6572 5368  ew_..ContainerSh
-00002de0: 6f77 5369 6465 6261 725c 5769 6e64 6f77  owSidebar\Window
-00002df0: 426f 756e 6473 5b53 686f 7753 6964 6562  Bounds[ShowSideb
-00002e00: 6172 0808 0908 095f 1017 7b7b 302c 2031  ar....._..{{0, 1
-00002e10: 3136 7d2c 207b 3132 3530 2c20 3736 317d  16}, {1250, 761}
-00002e20: 7d09 0817 2531 3d49 606d 797a 7b7c 7d7e  }...%1=I`myz{|}~
-00002e30: 9800 0000 0000 0001 0100 0000 0000 0000  ................
-00002e40: 0f00 0000 0000 0000 0000 0000 0000 0000  ................
-00002e50: 9900 0000 0700 6c00 6f00 6f00 6b00 7500  ......l.o.o.k.u.
-00002e60: 7000 736c 6731 5363 6f6d 7000 0000 0000  p.slg1Scomp.....
-00002e70: 04b1 fb00 0000 0000 0000 0000 0000 0000  ................
+00002790: 7208 0809 0809 5f10 187b 7b32 302c 2031  r....._..{{20, 1
+000027a0: 3232 7d2c 207b 3130 3736 2c20 3632 317d  22}, {1076, 621}
+000027b0: 7d09 0817 2531 3d49 606d 797a 7b7c 7d7e  }...%1=I`myz{|}~
+000027c0: 9900 0000 0000 0001 0100 0000 0000 0000  ................
+000027d0: 0f00 0000 0000 0000 0000 0000 0000 0000  ................
+000027e0: 9a00 0000 0300 6900 6d00 676c 6731 5363  ......i.m.glg1Sc
+000027f0: 6f6d 7000 0000 0000 0f4c f200 0000 0300  omp......L......
+00002800: 6900 6d00 676c 7376 4362 6c6f 6200 0002  i.m.glsvCblob...
+00002810: 7962 706c 6973 7430 30d8 0102 0304 0506  ybplist00.......
+00002820: 0708 0909 0b16 4647 4849 5f10 1075 7365  ......FGHI_..use
+00002830: 5265 6c61 7469 7665 4461 7465 735f 100f  RelativeDates_..
+00002840: 7368 6f77 4963 6f6e 5072 6576 6965 7757  showIconPreviewW
+00002850: 636f 6c75 6d6e 735f 1011 6361 6c63 756c  columns_..calcul
+00002860: 6174 6541 6c6c 5369 7a65 7358 7465 7874  ateAllSizesXtext
+00002870: 5369 7a65 5a73 6f72 7443 6f6c 756d 6e58  SizeZsortColumnX
+00002880: 6963 6f6e 5369 7a65 5f10 1276 6965 774f  iconSize_..viewO
+00002890: 7074 696f 6e73 5665 7273 696f 6e09 09ab  ptionsVersion...
+000028a0: 0c15 1a1f 2328 2d32 373c 41d4 0d0e 0f10  ....#(-27<A.....
+000028b0: 0912 0914 5776 6973 6962 6c65 5577 6964  ....WvisibleUwid
+000028c0: 7468 5961 7363 656e 6469 6e67 5a69 6465  thYascendingZide
+000028d0: 6e74 6966 6965 7209 1101 2709 546e 616d  ntifier...'.Tnam
+000028e0: 65d4 0d0e 0f10 1617 1619 0810 2308 5875  e...........#.Xu
+000028f0: 6269 7175 6974 79d4 0d0e 0f10 091c 161e  biquity.........
+00002900: 0910 b508 5c64 6174 654d 6f64 6966 6965  ....\dateModifie
+00002910: 64d4 0d0e 0f10 161c 1622 0808 5b64 6174  d........"..[dat
+00002920: 6543 7265 6174 6564 d40d 0e0f 1009 2516  eCreated......%.
+00002930: 2709 1061 0854 7369 7a65 d40d 0e0f 1009  '..a.Tsize......
+00002940: 2a09 2c09 1073 0954 6b69 6e64 d40d 0e0f  *.,..s.Tkind....
+00002950: 1016 2f09 3108 1064 0955 6c61 6265 6cd4  ../.1..d.Ulabel.
+00002960: 0d0e 0f10 1634 0936 0810 4b09 5776 6572  .....4.6..K.Wver
+00002970: 7369 6f6e d40d 0e0f 1016 3909 3b08 1101  sion......9.;...
+00002980: 2c09 5863 6f6d 6d65 6e74 73d4 0d0e 0f10  ,.Xcomments.....
+00002990: 163e 1640 0810 c808 5e64 6174 654c 6173  .>.@....^dateLas
+000029a0: 744f 7065 6e65 64d4 0d0e 0f10 161c 1644  tOpened........D
+000029b0: 0808 5964 6174 6541 6464 6564 0823 4028  ..YdateAdded.#@(
+000029c0: 0000 0000 0000 546e 616d 6523 4030 0000  ......Tname#@0..
+000029d0: 0000 0000 1001 0008 0019 002c 003e 0046  ...........,.>.F
+000029e0: 005a 0063 006e 0077 008c 008d 008e 009a  .Z.c.n.w........
+000029f0: 00a3 00ab 00b1 00bb 00c6 00c7 00ca 00cb  ................
+00002a00: 00d0 00d9 00da 00dc 00dd 00e6 00ef 00f0  ................
+00002a10: 00f2 00f3 0100 0109 010a 010b 0117 0120  ............... 
+00002a20: 0121 0123 0124 0129 0132 0133 0135 0136  .!.#.$.).2.3.5.6
+00002a30: 013b 0144 0145 0147 0148 014e 0157 0158  .;.D.E.G.H.N.W.X
+00002a40: 015a 015b 0163 016c 016d 0170 0171 017a  .Z.[.c.l.m.p.q.z
+00002a50: 0183 0184 0186 0187 0196 019f 01a0 01a1  ................
+00002a60: 01ab 01ac 01b5 01ba 01c3 0000 0000 0000  ................
+00002a70: 0201 0000 0000 0000 004a 0000 0000 0000  .........J......
+00002a80: 0000 0000 0000 0000 01c5 0000 0003 0069  ...............i
+00002a90: 006d 0067 6c73 7670 626c 6f62 0000 025e  .m.glsvpblob...^
+00002aa0: 6270 6c69 7374 3030 d801 0203 0405 0607  bplist00........
+00002ab0: 0809 090b 1d46 4748 245f 1010 7573 6552  .....FGH$_..useR
+00002ac0: 656c 6174 6976 6544 6174 6573 5f10 0f73  elativeDates_..s
+00002ad0: 686f 7749 636f 6e50 7265 7669 6577 5763  howIconPreviewWc
+00002ae0: 6f6c 756d 6e73 5f10 1163 616c 6375 6c61  olumns_..calcula
+00002af0: 7465 416c 6c53 697a 6573 5874 6578 7453  teAllSizesXtextS
+00002b00: 697a 655a 736f 7274 436f 6c75 6d6e 5869  izeZsortColumnXi
+00002b10: 636f 6e53 697a 655f 1012 7669 6577 4f70  conSize_..viewOp
+00002b20: 7469 6f6e 7356 6572 7369 6f6e 0909 d90c  tionsVersion....
+00002b30: 0d0e 0f10 1112 1314 151e 2328 2c31 363b  ..........#(,16;
+00002b40: 4058 636f 6d6d 656e 7473 5e64 6174 654c  @Xcomments^dateL
+00002b50: 6173 744f 7065 6e65 645c 6461 7465 4d6f  astOpened\dateMo
+00002b60: 6469 6669 6564 5b64 6174 6543 7265 6174  dified[dateCreat
+00002b70: 6564 5473 697a 6555 6c61 6265 6c54 6b69  edTsizeUlabelTki
+00002b80: 6e64 5776 6572 7369 6f6e 546e 616d 65d4  ndWversionTname.
+00002b90: 1617 1819 1a1b 091d 5569 6e64 6578 5577  ........UindexUw
+00002ba0: 6964 7468 5961 7363 656e 6469 6e67 5776  idthYascendingWv
+00002bb0: 6973 6962 6c65 1007 1101 2c09 08d4 1617  isible....,.....
+00002bc0: 1819 1f20 1d1d 1008 10c8 0808 d416 1718  ... ............
+00002bd0: 1924 251d 0910 0110 b508 09d4 1617 1819  .$%.............
+00002be0: 2925 1d1d 1002 0808 d416 1718 192d 2e1d  )%...........-..
+00002bf0: 0910 0310 6108 09d4 1617 1819 3233 091d  ....a.......23..
+00002c00: 1005 1064 0908 d416 1718 1937 3809 0910  ...d.......78...
+00002c10: 0410 7309 09d4 1617 1819 3c3d 091d 1006  ..s.......<=....
+00002c20: 104b 0908 d416 1718 1941 4209 0910 0011  .K.......AB.....
+00002c30: 0127 0909 0823 4028 0000 0000 0000 546e  .'...#@(......Tn
+00002c40: 616d 6523 4030 0000 0000 0000 0008 0019  ame#@0..........
+00002c50: 002c 003e 0046 005a 0063 006e 0077 008c  .,.>.F.Z.c.n.w..
+00002c60: 008d 008e 00a1 00aa 00b9 00c6 00d2 00d7  ................
+00002c70: 00dd 00e2 00ea 00ef 00f8 00fe 0104 010e  ................
+00002c80: 0116 0118 011b 011c 011d 0126 0128 012a  ...........&.(.*
+00002c90: 012b 012c 0135 0137 0139 013a 013b 0144  .+.,.5.7.9.:.;.D
+00002ca0: 0146 0147 0148 0151 0153 0155 0156 0157  .F.G.H.Q.S.U.V.W
+00002cb0: 0160 0162 0164 0165 0166 016f 0171 0173  .`.b.d.e.f.o.q.s
+00002cc0: 0174 0175 017e 0180 0182 0183 0184 018d  .t.u.~..........
+00002cd0: 018f 0192 0193 0194 0195 019e 01a3 0000  ................
+00002ce0: 0000 0000 0201 0000 0000 0000 0049 0000  .............I..
+00002cf0: 0000 0000 0000 0000 0000 0000 01ac 0000  ................
+00002d00: 0003 0069 006d 0067 6d6f 4444 626c 6f62  ...i.m.gmoDDblob
+00002d10: 0000 0008 b8f4 ead3 d4e1 c441 0000 0003  ...........A....
+00002d20: 0069 006d 0067 6d6f 6444 626c 6f62 0000  .i.m.gmodDblob..
+00002d30: 0008 b8f4 ead3 d4e1 c441 0000 0003 0069  .........A.....i
+00002d40: 006d 0067 7068 3153 636f 6d70 0000 0000  .m.gph1Scomp....
+00002d50: 000f 6000 0000 0003 0069 006d 0067 7653  ..`......i.m.gvS
+00002d60: 726e 6c6f 6e67 0000 0001 0000 0007 006c  rnlong.........l
+00002d70: 006f 006f 006b 0075 0070 0073 6277 7370  .o.o.k.u.p.sbwsp
+00002d80: 626c 6f62 0000 00c8 6270 6c69 7374 3030  blob....bplist00
+00002d90: d701 0203 0405 0607 0808 0a08 0a0d 0a5d  ...............]
+00002da0: 5368 6f77 5374 6174 7573 4261 725b 5368  ShowStatusBar[Sh
+00002db0: 6f77 5061 7468 6261 725b 5368 6f77 546f  owPathbar[ShowTo
+00002dc0: 6f6c 6261 725b 5368 6f77 5461 6256 6965  olbar[ShowTabVie
+00002dd0: 775f 1014 436f 6e74 6169 6e65 7253 686f  w_..ContainerSho
+00002de0: 7753 6964 6562 6172 5c57 696e 646f 7742  wSidebar\WindowB
+00002df0: 6f75 6e64 735b 5368 6f77 5369 6465 6261  ounds[ShowSideba
+00002e00: 7208 0809 0809 5f10 177b 7b30 2c20 3131  r....._..{{0, 11
+00002e10: 367d 2c20 7b31 3235 302c 2037 3631 7d7d  6}, {1250, 761}}
+00002e20: 0908 1725 313d 4960 6d79 7a7b 7c7d 7e98  ...%1=I`myz{|}~.
+00002e30: 0000 0000 0000 0101 0000 0000 0000 000f  ................
+00002e40: 0000 0000 0000 0000 0000 0000 0000 0099  ................
+00002e50: 0000 0007 006c 006f 006f 006b 0075 0070  .....l.o.o.k.u.p
+00002e60: 0073 6c67 3153 636f 6d70 0000 0000 0004  .slg1Scomp......
+00002e70: b1fb 0000 0000 0000 0000 0000 0000 0000  ................
 00002e80: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00002e90: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00002ea0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00002eb0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00002ec0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00002ed0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00002ee0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
@@ -868,37 +868,37 @@
 00003630: 010a 010b 010c 0118 0121 0122 0124 0125  .........!.".$.%
 00003640: 012a 0133 0134 0136 0137 013c 0145 0146  .*.3.4.6.7.<.E.F
 00003650: 0148 0149 014f 0158 0159 015b 015c 0164  .H.I.O.X.Y.[.\.d
 00003660: 016d 016e 0171 0172 017b 0184 0185 0187  .m.n.q.r.{......
 00003670: 0188 0197 01a0 01a1 01a2 01ac 01ad 01b6  ................
 00003680: 01bb 01c4 0000 0000 0000 0201 0000 0000  ................
 00003690: 0000 004a 0000 0000 0000 0000 0000 0000  ...J............
-000036a0: 0000 01c5 36ee c441 0000 0005 0069 0063  ....6..A.....i.c
+000036a0: 0000 01c5 eeee c441 0000 0005 0069 0063  .......A.....i.c
 000036b0: 006f 006e 0073 6d6f 6444 626c 6f62 0000  .o.n.smodDblob..
-000036c0: 0008 81c7 e5e4 36ee c441 0000 0005 0069  ......6..A.....i
+000036c0: 0008 7ef0 e459 eeee c441 0000 0005 0069  ..~..Y...A.....i
 000036d0: 0063 006f 006e 0073 7068 3153 636f 6d70  .c.o.n.sph1Scomp
-000036e0: 0000 0000 0007 c000 0000 0005 0069 0063  .............i.c
+000036e0: 0000 0000 0007 e000 0000 0005 0069 0063  .............i.c
 000036f0: 006f 006e 0073 7653 726e 6c6f 6e67 0000  .o.n.svSrnlong..
 00003700: 0001 0000 0003 0069 006d 0067 6277 7370  .......i.m.gbwsp
-00003710: 626c 6f62 0000 00ca 6270 6c69 7374 3030  blob....bplist00
+00003710: 626c 6f62 0000 00c9 6270 6c69 7374 3030  blob....bplist00
 00003720: d701 0203 0405 0607 0808 0a08 0a0d 0a5d  ...............]
 00003730: 5368 6f77 5374 6174 7573 4261 725b 5368  ShowStatusBar[Sh
 00003740: 6f77 5061 7468 6261 725b 5368 6f77 546f  owPathbar[ShowTo
 00003750: 6f6c 6261 725b 5368 6f77 5461 6256 6965  olbar[ShowTabVie
 00003760: 775f 1014 436f 6e74 6169 6e65 7253 686f  w_..ContainerSho
 00003770: 7753 6964 6562 6172 5c57 696e 646f 7742  wSidebar\WindowB
 00003780: 6f75 6e64 735b 5368 6f77 5369 6465 6261  ounds[ShowSideba
-00003790: 7208 0809 0809 5f10 197b 7b33 3535 2c20  r....._..{{355, 
-000037a0: 3132 357d 2c20 7b31 3037 362c 2036 3231  125}, {1076, 621
-000037b0: 7d7d 0908 1725 313d 4960 6d79 7a7b 7c7d  }}...%1=I`myz{|}
-000037c0: 7e9a 0000 0000 0000 0101 0000 0000 0000  ~...............
-000037d0: 000f 0000 0000 0000 0000 0000 0000 0000  ................
-000037e0: 009b 0000 0003 0069 006d 0067 6c67 3153  .......i.m.glg1S
-000037f0: 636f 6d70 0000 0000 000f 4cf2 0000 0003  comp......L.....
-00003800: 0069 006d 0000 0006 0000 0000 0000 380b  .i.m..........8.
+00003790: 7208 0809 0809 5f10 187b 7b32 302c 2031  r....._..{{20, 1
+000037a0: 3232 7d2c 207b 3130 3736 2c20 3632 317d  22}, {1076, 621}
+000037b0: 7d09 0817 2531 3d49 606d 797a 7b7c 7d7e  }...%1=I`myz{|}~
+000037c0: 9900 0000 0000 0001 0100 0000 0000 0000  ................
+000037d0: 0f00 0000 0000 0000 0000 0000 0000 0000  ................
+000037e0: 9a00 0000 0300 6900 6d00 676c 6731 5363  ......i.m.glg1Sc
+000037f0: 6f6d 7000 0000 0000 0f4c f200 0000 0300  omp......L......
+00003800: 6900 6d00 0000 0006 0000 0000 0000 380b  i.m...........8.
 00003810: 0000 0045 0000 100b 0000 300b 0000 200c  ...E......0... .
 00003820: 0000 180b 0000 0000 0000 0000 0000 0000  ................
 00003830: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00003840: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00003850: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00003860: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00003870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
@@ -996,30 +996,30 @@
 00003e30: 010a 010b 010c 0118 0121 0122 0124 0125  .........!.".$.%
 00003e40: 012a 0133 0134 0136 0137 013c 0145 0146  .*.3.4.6.7.<.E.F
 00003e50: 0148 0149 014f 0158 0159 015b 015c 0164  .H.I.O.X.Y.[.\.d
 00003e60: 016d 016e 0171 0172 017b 0184 0185 0187  .m.n.q.r.{......
 00003e70: 0188 0197 01a0 01a1 01a2 01ac 01ad 01b6  ................
 00003e80: 01bb 01c4 0000 0000 0000 0201 0000 0000  ................
 00003e90: 0000 004a 0000 0000 0000 0000 0000 0000  ...J............
-00003ea0: 0000 01c5 36ee c441 0000 0005 0069 0063  ....6..A.....i.c
+00003ea0: 0000 01c5 eeee c441 0000 0005 0069 0063  .......A.....i.c
 00003eb0: 006f 006e 0073 6d6f 6444 626c 6f62 0000  .o.n.smodDblob..
-00003ec0: 0008 81c7 e5e4 36ee c441 0000 0005 0069  ......6..A.....i
+00003ec0: 0008 7ef0 e459 eeee c441 0000 0005 0069  ..~..Y...A.....i
 00003ed0: 0063 006f 006e 0073 7068 3153 636f 6d70  .c.o.n.sph1Scomp
-00003ee0: 0000 0000 0007 c000 0000 0005 0069 0063  .............i.c
+00003ee0: 0000 0000 0007 e000 0000 0005 0069 0063  .............i.c
 00003ef0: 006f 006e 0073 7653 726e 6c6f 6e67 0000  .o.n.svSrnlong..
 00003f00: 0001 0000 0003 0069 006d 0067 6277 7370  .......i.m.gbwsp
-00003f10: 626c 6f62 0000 00ca 6270 6c69 7374 3030  blob....bplist00
+00003f10: 626c 6f62 0000 00c9 6270 6c69 7374 3030  blob....bplist00
 00003f20: d701 0203 0405 0607 0808 0a08 0a0d 0a5d  ...............]
 00003f30: 5368 6f77 5374 6174 7573 4261 725b 5368  ShowStatusBar[Sh
 00003f40: 6f77 5061 7468 6261 725b 5368 6f77 546f  owPathbar[ShowTo
 00003f50: 6f6c 6261 725b 5368 6f77 5461 6256 6965  olbar[ShowTabVie
 00003f60: 775f 1014 436f 6e74 6169 6e65 7253 686f  w_..ContainerSho
 00003f70: 7753 6964 6562 6172 5c57 696e 646f 7742  wSidebar\WindowB
 00003f80: 6f75 6e64 735b 5368 6f77 5369 6465 6261  ounds[ShowSideba
-00003f90: 7208 0809 0809 5f10 197b 7b33 3535 2c20  r....._..{{355, 
-00003fa0: 3132 357d 2c20 7b31 3037 362c 2036 3231  125}, {1076, 621
-00003fb0: 7d7d 0908 1725 313d 4960 6d79 7a7b 7c7d  }}...%1=I`myz{|}
-00003fc0: 7e9a 0000 0000 0000 0101 0000 0000 0000  ~...............
-00003fd0: 000f 0000 0000 0000 0000 0000 0000 0000  ................
-00003fe0: 009b 0000 0003 0069 006d 0067 6c67 3153  .......i.m.glg1S
-00003ff0: 636f 6d70 0000 0000 000f 4cf2 0000 0003  comp......L.....
-00004000: 0069 006d                                .i.m
+00003f90: 7208 0809 0809 5f10 187b 7b32 302c 2031  r....._..{{20, 1
+00003fa0: 3232 7d2c 207b 3130 3736 2c20 3632 317d  22}, {1076, 621}
+00003fb0: 7d09 0817 2531 3d49 606d 797a 7b7c 7d7e  }...%1=I`myz{|}~
+00003fc0: 9900 0000 0000 0001 0100 0000 0000 0000  ................
+00003fd0: 0f00 0000 0000 0000 0000 0000 0000 0000  ................
+00003fe0: 9a00 0000 0300 6900 6d00 676c 6731 5363  ......i.m.glg1Sc
+00003ff0: 6f6d 7000 0000 0000 0f4c f200 0000 0300  omp......L......
+00004000: 6900 6d00                                i.m.
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/lookups/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/assets/lookups/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/lookups/model_names.parquet` & `Simba-UW-tf-dev-1.55.2/simba/assets/lookups/model_names.parquet`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/lookups/feature_extraction_headers.csv` & `Simba-UW-tf-dev-1.55.2/simba/assets/lookups/feature_extraction_headers.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/lookups/features.csv` & `Simba-UW-tf-dev-1.55.2/simba/assets/lookups/features.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/lookups/unsupervised_example_x.csv` & `Simba-UW-tf-dev-1.55.2/simba/assets/lookups/unsupervised_example_x.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/stl/operant_tray.stl` & `Simba-UW-tf-dev-1.55.2/simba/assets/stl/operant_tray.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/stl/operant_lever.stl` & `Simba-UW-tf-dev-1.55.2/simba/assets/stl/operant_lever.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/stl/operant_walls.stl` & `Simba-UW-tf-dev-1.55.2/simba/assets/stl/operant_walls.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/stl/grid_floor.stl` & `Simba-UW-tf-dev-1.55.2/simba/assets/stl/grid_floor.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/img/about_me.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/img/about_me.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/img/splash.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/img/splash.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/img/splash.pptx` & `Simba-UW-tf-dev-1.55.2/simba/assets/img/splash.pptx`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/UbuntuMono-Regular.ttf` & `Simba-UW-tf-dev-1.55.2/simba/assets/UbuntuMono-Regular.ttf`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/factory.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/factory.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/cluster.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/cluster.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/load.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/load.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/gif.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/gif.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/pose.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/pose.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/features.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/features.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/settings.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/settings.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/link.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/link.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/dash_simba.css` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/dash_simba.css`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/documentation.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/documentation.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/fps.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/fps.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/dimensionality_reduction.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/dimensionality_reduction.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/roi.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/roi.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/superimpose.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/superimpose.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/label.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/label.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/change.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/change.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/crop.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/crop.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/path.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/path.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/clip.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/clip.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/restart.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/restart.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/calipher.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/calipher.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/add_on.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/add_on.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/create.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/create.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/SimBA_logo.ico` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/SimBA_logo.ico`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/print.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/print.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/clf.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/clf.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/mosaic.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/mosaic.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/vertical.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/vertical.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/horizontal.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/horizontal.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat_icons/mixed_mosaic.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat_icons/mixed_mosaic.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/merge.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/merge.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/clf_2.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/clf_2.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/visualize.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/visualize.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/concat.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/concat.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/boris.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/boris.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/frames.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/frames.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/video.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/video.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/sample.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/sample.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/metrics.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/metrics.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/grey.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/grey.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/exit.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/exit.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/outlier.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/outlier.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/clahe.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/clahe.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/trash.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/trash.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/about.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/about.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/convert.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/convert.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/SimBA_logo.icns` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/SimBA_logo.icns`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/reorganize.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/reorganize.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/browse.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/browse.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/SimBA_logo.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/SimBA_logo.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/ethovision.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/ethovision.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/icons/close.png` & `Simba-UW-tf-dev-1.55.2/simba/assets/icons/close.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/dash_simba_base.css` & `Simba-UW-tf-dev-1.55.2/simba/assets/dash_simba_base.css`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/assets/TheGoldenLab.PNG` & `Simba-UW-tf-dev-1.55.2/simba/assets/TheGoldenLab.PNG`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/drop_bp_cords.py` & `Simba-UW-tf-dev-1.55.2/simba/drop_bp_cords.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/read_config_unit_tests.py` & `Simba-UW-tf-dev-1.55.2/simba/read_config_unit_tests.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/project_config_creator.py` & `Simba-UW-tf-dev-1.55.2/simba/project_config_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/set_hyperparameters.py` & `Simba-UW-tf-dev-1.55.2/simba/set_hyperparameters.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/train_single_model.py` & `Simba-UW-tf-dev-1.55.2/simba/train_single_model.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/create_clf_log.py` & `Simba-UW-tf-dev-1.55.2/simba/create_clf_log.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/.DS_Store` & `Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/batch_process_menus.py` & `Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/batch_process_menus.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 from tkinter import *
 import glob, os
 from simba.misc_tools import get_fn_ext, get_video_meta_data
-from simba.tkinter_functions import hxtScrollbar
+from simba.tkinter_functions import hxtScrollbar, CreateLabelFrameWithIcon
 import re
 import datetime
 import cv2
 from simba.read_config_unit_tests import check_file_exist_and_readable
 import json
 from simba.batch_process_videos.batch_process_create_ffmpeg_commands import FFMPEGCommandCreator
 from simba.utils.errors import NoFilesFoundError
-from simba.enums import Options
+from simba.enums import Options, Keys, Links
 
 class BatchProcessFrame(object):
     """
     Class for creating interactive windows that collect user-inputs for batch processing videos (e.g., cropping,
     clipping etc.). User-selected output is stored in json file format within the user-defined `output_dir`
 
     Parameters
@@ -66,15 +66,16 @@
     def create_main_window(self):
         self.batch_process_main_frame = Toplevel()
         self.batch_process_main_frame.minsize(1600, 600)
         self.batch_process_main_frame.wm_title("BATCH PRE-PROCESS VIDEOS IN SIMBA")
         self.batch_process_main_frame.lift()
         self.batch_process_main_frame = Canvas(hxtScrollbar(self.batch_process_main_frame))
         self.batch_process_main_frame.pack(fill="both", expand=True)
-        self.quick_settings_frm = LabelFrame(self.batch_process_main_frame, text='QUICK SETTINGS', font=('Helvetica', 15, 'bold'), pady=5, padx=15)
+
+        self.quick_settings_frm = CreateLabelFrameWithIcon(parent=self.batch_process_main_frame, header='QUICK SETTINGS', icon_name=Keys.DOCUMENTATION.value, icon_link=Links.BATCH_PREPROCESS.value)
         self.clip_video_settings_frm = LabelFrame(self.quick_settings_frm, text='Clip Videos Settings', padx=5)
         self.quick_clip_start_entry_lbl = Label(self.clip_video_settings_frm, text="Start Time: ")
         self.quick_clip_start_entry_box_val = StringVar()
         self.quick_clip_start_entry_box_val.set('00:00:00')
         self.quick_clip_start_entry_box = Entry(self.clip_video_settings_frm, width=15, textvariable=self.quick_clip_start_entry_box_val)
         self.quick_clip_end_entry_lbl = Label(self.clip_video_settings_frm, text="End Time: ")
         self.quick_clip_end_entry_box_val = StringVar()
```

### Comparing `Simba-UW-tf-dev-1.55.1/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py` & `Simba-UW-tf-dev-1.55.2/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/Kleinberg_calculator.py` & `Simba-UW-tf-dev-1.55.2/simba/Kleinberg_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/reorganize_keypoint_in_pose.py` & `Simba-UW-tf-dev-1.55.2/simba/reorganize_keypoint_in_pose.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/simba/play_annotation_video.py` & `Simba-UW-tf-dev-1.55.2/simba/play_annotation_video.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/PKG-INFO` & `Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Simba-UW-tf-dev
-Version: 1.55.1
+Version: 1.55.2
 Summary: Toolkit for computer classification of complex social behaviors in experimental animals
 Home-page: https://github.com/sgoldenlab/simba
 Author: Simon Nilsson, Jia Jie Choong, Sophia Hwang
 Author-email: sronilsson@gmail.com
 License: GNU Lesser General Public License v3 (LGPLv3)
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/SOURCES.txt` & `Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -119,14 +119,15 @@
 simba/assets/icons/visualize.png
 simba/assets/icons/concat_icons/horizontal.png
 simba/assets/icons/concat_icons/mixed_mosaic.png
 simba/assets/icons/concat_icons/mosaic.png
 simba/assets/icons/concat_icons/vertical.png
 simba/assets/img/about_me.png
 simba/assets/img/bg.png
+simba/assets/img/bg_2.png
 simba/assets/img/splash.png
 simba/assets/img/splash.pptx
 simba/assets/lookups/.DS_Store
 simba/assets/lookups/feature_extraction_headers.csv
 simba/assets/lookups/features.csv
 simba/assets/lookups/model_names.parquet
 simba/assets/lookups/unsupervised_example_x.csv
```

### Comparing `Simba-UW-tf-dev-1.55.1/Simba_UW_tf_dev.egg-info/requires.txt` & `Simba-UW-tf-dev-1.55.2/Simba_UW_tf_dev.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/LICENSE.md` & `Simba-UW-tf-dev-1.55.2/LICENSE.md`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/README.md` & `Simba-UW-tf-dev-1.55.2/README.md`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.1/setup.py` & `Simba-UW-tf-dev-1.55.2/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 Licensed under GNU Lesser General Public License v3.0
 """
 
 import setuptools
 
 setuptools.setup(
     name="Simba-UW-tf-dev",
-    version="1.55.1",
+    version="1.55.2",
     author="Simon Nilsson, Jia Jie Choong, Sophia Hwang",
     author_email="sronilsson@gmail.com",
     description="Toolkit for computer classification of complex social behaviors in experimental animals",
     url="https://github.com/sgoldenlab/simba",
     install_requires=['Pillow == 5.4.1', 'pyyaml == 5.3.1','shapely == 1.7','wxpython == 4.0.4',
               'dtreeviz == 0.8.1','eli5 == 0.10.1','graphviz == 0.11',
               'imblearn == 0.0','imgaug == 0.4.0','imutils == 0.5.2','matplotlib == 3.0.3', 'numpy == 1.18.1',
```

