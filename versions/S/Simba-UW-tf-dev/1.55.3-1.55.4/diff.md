# Comparing `tmp/Simba-UW-tf-dev-1.55.3.tar.gz` & `tmp/Simba-UW-tf-dev-1.55.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/Simba-UW-tf-dev-1.55.3.tar", last modified: Thu Apr  6 19:58:46 2023, max compression
+gzip compressed data, was "dist/Simba-UW-tf-dev-1.55.4.tar", last modified: Thu Apr  6 20:10:45 2023, max compression
```

## Comparing `Simba-UW-tf-dev-1.55.3.tar` & `Simba-UW-tf-dev-1.55.4.tar`

### file list

```diff
@@ -1,380 +1,380 @@
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/
--rw-r--r--   0 simon      (501) staff       (20)      579 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/PKG-INFO
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/
--rw-r--r--   0 simon      (501) staff       (20)    32569 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.3/simba/video_processing.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/blob_storage/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-21 20:39:46.000000 Simba-UW-tf-dev-1.55.3/simba/blob_storage/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/
--rw-r--r--   0 simon      (501) staff       (20)    10851 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/unsupervised_ui.py
--rw-r--r--   0 simon      (501) staff       (20)     6566 2023-03-21 14:26:03.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/misc.py
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     7227 2023-03-21 11:41:26.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/dataset_creator.py
--rw-r--r--   0 simon      (501) staff       (20)     4061 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/data_extractors.py
--rw-r--r--   0 simon      (501) staff       (20)    11192 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/dbcv.py
--rw-r--r--   0 simon      (501) staff       (20)    11456 2023-03-21 18:17:26.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/visualizers.py
--rw-r--r--   0 simon      (501) staff       (20)     7526 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/umap_embedder.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/visualization_tools/
--rw-r--r--   0 simon      (501) staff       (20)     2019 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/visualization_tools/vtk_embeddings.py
--rw-r--r--   0 simon      (501) staff       (20)      150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/ui_tools.py
--rw-r--r--   0 simon      (501) staff       (20)    49992 2023-03-22 15:08:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/pop_up_classes.py
--rw-r--r--   0 simon      (501) staff       (20)    16189 2023-03-21 15:42:27.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/cluster_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)     6642 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/hdbscan_clusterer.py
--rw-r--r--   0 simon      (501) staff       (20)     3789 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/tsne.py
--rw-r--r--   0 simon      (501) staff       (20)     5630 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/unsupervised/cluster_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    19024 2023-04-06 19:25:58.000000 Simba-UW-tf-dev-1.55.3/simba/enums.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     7463 2023-03-15 19:17:12.000000 Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/agg_boundary_stats.py
--rw-r--r--   0 simon      (501) staff       (20)     8562 2023-03-15 19:17:04.000000 Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/find_bounderies.py
--rw-r--r--   0 simon      (501) staff       (20)    24561 2023-04-06 11:22:38.000000 Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/boundary_menus.py
--rw-r--r--   0 simon      (501) staff       (20)     9530 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/boundary_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)    12627 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/visualize_boundaries.py
--rw-r--r--   0 simon      (501) staff       (20)    32772 2023-04-04 14:38:01.000000 Simba-UW-tf-dev-1.55.3/simba/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/
--rw-r--r--   0 simon      (501) staff       (20)    42807 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_14bp.py
--rw-r--r--   0 simon      (501) staff       (20)    21541 2023-03-15 19:11:32.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_7bp.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/
--rw-r--r--   0 simon      (501) staff       (20)     2732 2023-04-04 19:46:36.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/read_in_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    14141 2023-03-15 17:20:08.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/fish_feature_extractor_2022.py
--rw-r--r--   0 simon      (501) staff       (20)     2053 2023-04-04 03:00:41.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/convex_hull_3_scratch_3.py
--rw-r--r--   0 simon      (501) staff       (20)     5762 2023-04-04 01:54:33.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/convex_hull_scratch_1.py
--rw-r--r--   0 simon      (501) staff       (20)    19620 2023-04-03 12:08:14.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/fish_feature_extractor_2023.py
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 19:36:02.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     7127 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/egocentrical_aligner.py
--rw-r--r--   0 simon      (501) staff       (20)     4708 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/graph_creator.py
--rw-r--r--   0 simon      (501) staff       (20)     3954 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/termite_rois.csv
--rw-r--r--   0 simon      (501) staff       (20)      732 2023-03-20 12:13:51.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/mutual_exclusive.py
--rw-r--r--   0 simon      (501) staff       (20)     1862 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/graph_3d_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)     2692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/add_probability_cnt_features.py
--rw-r--r--   0 simon      (501) staff       (20)     2058 2023-04-03 23:51:37.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/convex_hull_scratch_2.py
--rw-r--r--   0 simon      (501) staff       (20)    28028 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_8bps_2_animals.py
--rw-r--r--   0 simon      (501) staff       (20)    10244 2023-04-06 18:38:15.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     2347 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/perimeter_jit.py
--rw-r--r--   0 simon      (501) staff       (20)    10734 2023-04-06 14:57:55.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_subsets.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__init__.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/
--rw-r--r--   0 simon      (501) staff       (20)      905 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi
--rw-r--r--   0 simon      (501) staff       (20)   238196 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc
--rw-r--r--   0 simon      (501) staff       (20)    69038 2023-04-04 11:32:25.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc
--rw-r--r--   0 simon      (501) staff       (20)   238298 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc
--rw-r--r--   0 simon      (501) staff       (20)    69338 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc
--rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi
--rw-r--r--   0 simon      (501) staff       (20)     2179 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi
--rw-r--r--   0 simon      (501) staff       (20)    36798 2023-03-15 17:04:48.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/extract_features_9bp.py
--rw-r--r--   0 simon      (501) staff       (20)     8428 2023-03-15 19:11:54.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_user_defined.py
--rw-r--r--   0 simon      (501) staff       (20)     5323 2023-03-19 18:30:53.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/unit_tests.py
--rw-r--r--   0 simon      (501) staff       (20)    46473 2023-04-04 13:07:58.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_16bp.py
--rw-r--r--   0 simon      (501) staff       (20)    24093 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_8bp.py
--rw-r--r--   0 simon      (501) staff       (20)    16763 2023-03-15 19:11:50.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_4bp.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/
--rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/features_scripts.iml
--rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/encodings.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/inspectionProfiles/
--rw-r--r--   0 simon      (501) staff       (20)      822 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/libraries/
--rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/libraries/R_User_Library.xml
--rw-r--r--   0 simon      (501) staff       (20)      273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/.gitignore
--rw-r--r--   0 simon      (501) staff       (20)     8081 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/workspace.xml
--rw-r--r--   0 simon      (501) staff       (20)      291 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/modules.xml
--rw-r--r--   0 simon      (501) staff       (20)       23 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/.name
--rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/misc.xml
--rw-r--r--   0 simon      (501) staff       (20)     6044 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/plotly_create_h5.py
--rw-r--r--   0 simon      (501) staff       (20)    15351 2023-04-06 14:48:36.000000 Simba-UW-tf-dev-1.55.3/simba/requirements.txt
--rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-15 19:16:48.000000 Simba-UW-tf-dev-1.55.3/simba/severity_processor.py
--rw-r--r--   0 simon      (501) staff       (20)     5941 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.3/simba/user_pose_config_creator.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/mixins/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:26:03.000000 Simba-UW-tf-dev-1.55.3/simba/mixins/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    41856 2023-04-05 17:24:50.000000 Simba-UW-tf-dev-1.55.3/simba/mixins/pop_up_mixin.py
--rw-r--r--   0 simon      (501) staff       (20)     8182 2023-04-05 13:03:24.000000 Simba-UW-tf-dev-1.55.3/simba/mixins/config_reader.py
--rw-r--r--   0 simon      (501) staff       (20)     6781 2023-04-06 14:21:49.000000 Simba-UW-tf-dev-1.55.3/simba/mixins/feature_extraction_mixin.py
--rw-r--r--   0 simon      (501) staff       (20)    34512 2023-04-06 19:49:53.000000 Simba-UW-tf-dev-1.55.3/simba/machine_model_settings_pop_up.py
--rw-r--r--   0 simon      (501) staff       (20)     5266 2023-03-15 15:43:20.000000 Simba-UW-tf-dev-1.55.3/simba/remove_keypoints_in_pose.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/
--rw-r--r--   0 simon      (501) staff       (20)     6326 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/deepethogram_importer.py
--rw-r--r--   0 simon      (501) staff       (20)     9947 2023-03-18 15:35:38.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/BORIS_appender.py
--rw-r--r--   0 simon      (501) staff       (20)     9170 2023-03-22 19:35:38.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/observer_importer.py
--rw-r--r--   0 simon      (501) staff       (20)    16922 2023-03-28 20:30:38.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/tools.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-04-01 14:10:06.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)    18283 2023-04-01 14:14:21.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/third_party_appender.py
--rw-r--r--   0 simon      (501) staff       (20)     8336 2023-03-15 19:12:46.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/ethovision_import.py
--rw-r--r--   0 simon      (501) staff       (20)     6919 2023-03-19 15:03:14.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/BENTO_appender.py
--rw-r--r--   0 simon      (501) staff       (20)     5426 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/solomon_importer.py
--rw-r--r--   0 simon      (501) staff       (20)     7261 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/multi_cropper.py
--rw-r--r--   0 simon      (501) staff       (20)    13056 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.3/simba/FSTTC_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)    12620 2023-04-06 11:43:07.000000 Simba-UW-tf-dev-1.55.3/simba/create_project_pop_up.py
--rw-r--r--   0 simon      (501) staff       (20)    13421 2023-04-06 11:40:29.000000 Simba-UW-tf-dev-1.55.3/simba/video_info_table.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:25:58.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     8507 2023-03-15 19:09:16.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_clf_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)    13530 2023-03-15 19:08:52.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    18253 2023-04-06 11:29:26.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_menues.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)     1660 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_tools.py
--rw-r--r--   0 simon      (501) staff       (20)    16374 2023-03-15 19:09:04.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    13160 2023-03-20 13:43:59.000000 Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_movement_statistics.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)     2813 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/extract_frames_fast.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/utils/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 20:15:03.000000 Simba-UW-tf-dev-1.55.3/simba/utils/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     5626 2023-03-28 20:35:14.000000 Simba-UW-tf-dev-1.55.3/simba/utils/warnings.py
--rw-r--r--   0 simon      (501) staff       (20)     3825 2023-04-06 19:25:38.000000 Simba-UW-tf-dev-1.55.3/simba/utils/lookups.py
--rw-r--r--   0 simon      (501) staff       (20)    11967 2023-04-06 19:37:44.000000 Simba-UW-tf-dev-1.55.3/simba/utils/errors.py
--rw-r--r--   0 simon      (501) staff       (20)    21581 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/labelling_interface.py
--rw-r--r--   0 simon      (501) staff       (20)     9937 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.3/simba/timebins_movement_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    45524 2023-04-04 20:09:14.000000 Simba-UW-tf-dev-1.55.3/simba/train_model_functions.py
--rw-r--r--   0 simon      (501) staff       (20)    49699 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/SimBA_dash_app.py
--rw-r--r--   0 simon      (501) staff       (20)     7520 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.3/simba/timebins_clf_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     8240 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.3/simba/calculate_px_dist.py
--rw-r--r--   0 simon      (501) staff       (20)     6548 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/movement_processor.py
--rw-r--r--   0 simon      (501) staff       (20)     2904 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pybursts.py
--rw-r--r--   0 simon      (501) staff       (20)     5265 2023-03-29 18:04:02.000000 Simba-UW-tf-dev-1.55.3/simba/run_model_new.py
--rw-r--r--   0 simon      (501) staff       (20)     3104 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/rw_dfs.py
--rw-r--r--   0 simon      (501) staff       (20)     6684 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/reverse_2_animal_tracking.py
--rw-r--r--   0 simon      (501) staff       (20)     9743 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.3/simba/Directing_animals_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     4357 2023-03-30 16:19:09.000000 Simba-UW-tf-dev-1.55.3/simba/Validate_model_one_video_run_clf.py
--rw-r--r--   0 simon      (501) staff       (20)     9548 2023-04-06 00:40:25.000000 Simba-UW-tf-dev-1.55.3/simba/tkinter_functions.py
--rw-r--r--   0 simon      (501) staff       (20)    13767 2023-03-24 12:49:19.000000 Simba-UW-tf-dev-1.55.3/simba/setting_menu.py
--rw-r--r--   0 simon      (501) staff       (20)     6614 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/interpolate_pose.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/
--rw-r--r--   0 simon      (501) staff       (20)     8571 2023-03-30 10:06:59.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/gantt_creator.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/tools/
--rw-r--r--   0 simon      (501) staff       (20)     5353 2023-03-30 15:38:37.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/tools/tkinter_tools.py
--rw-r--r--   0 simon      (501) staff       (20)    17962 2023-03-24 13:40:30.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_plotter_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    14592 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/shap_agg_stats_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    12928 2023-03-30 10:08:46.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/gantt_creator_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    15777 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_clf_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     8884 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/probability_plot_creator.py
--rw-r--r--   0 simon      (501) staff       (20)    16058 2023-03-22 14:43:52.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/misc_visualizations.py
--rw-r--r--   0 simon      (501) staff       (20)    13501 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/plot_clf_results.py
--rw-r--r--   0 simon      (501) staff       (20)    17696 2023-03-29 16:22:09.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/plot_clf_results_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    16328 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_feature_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    12588 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_location.py
--rw-r--r--   0 simon      (501) staff       (20)    12585 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/probability_plot_creator_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     5341 2023-03-30 15:46:49.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/interactive_probability_grapher.py
--rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-29 17:02:51.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/plot_pose_in_dir.py
--rw-r--r--   0 simon      (501) staff       (20)    12184 2023-03-31 13:53:09.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/single_run_model_validation_video.py
--rw-r--r--   0 simon      (501) staff       (20)    11202 2023-03-19 16:21:53.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/frame_mergerer_ffmpeg.py
--rw-r--r--   0 simon      (501) staff       (20)    12442 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/Directing_animals_visualizer_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     9856 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/clf_validator.py
--rw-r--r--   0 simon      (501) staff       (20)    17290 2023-04-06 00:33:50.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/path_plotter_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    19958 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_feature_visualizer_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    10157 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/data_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)    12444 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/path_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)     8609 2023-03-15 13:37:59.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/ez_lineplot.py
--rw-r--r--   0 simon      (501) staff       (20)    12970 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/distance_plotter_mp.py
--rw-r--r--   0 simon      (501) staff       (20)    15626 2023-03-29 17:05:49.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)    13165 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_clf.py
--rw-r--r--   0 simon      (501) staff       (20)     8891 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/distance_plotter.py
--rw-r--r--   0 simon      (501) staff       (20)    13554 2023-04-01 13:12:31.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/single_run_model_validation_video_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     9839 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/Directing_animals_visualizer.py
--rw-r--r--   0 simon      (501) staff       (20)    16155 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_location_mp.py
--rw-r--r--   0 simon      (501) staff       (20)     5029 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/run_dash_tkinter.py
--rw-r--r--   0 simon      (501) staff       (20)     7454 2023-03-13 22:11:36.000000 Simba-UW-tf-dev-1.55.3/simba/interpolate_smooth_post_hoc.py
--rw-r--r--   0 simon      (501) staff       (20)    24474 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/dash_app.py
--rw-r--r--   0 simon      (501) staff       (20)     6350 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/reverse_tracking_order.py
--rw-r--r--   0 simon      (501) staff       (20)     5772 2023-03-20 13:55:20.000000 Simba-UW-tf-dev-1.55.3/simba/concatenator_pop_up.py
--rw-r--r--   0 simon      (501) staff       (20)     2824 2023-03-24 16:12:51.000000 Simba-UW-tf-dev-1.55.3/simba/extract_annotation_frames.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/
--rw-r--r--   0 simon      (501) staff       (20)     7385 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_time_bin_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)     2248 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_movement_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-20 12:47:56.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    43831 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_define.py
--rw-r--r--   0 simon      (501) staff       (20)     3384 2023-03-20 12:41:16.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_reset.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)    21382 2023-03-31 10:40:20.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    11920 2023-03-31 10:48:40.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_feature_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)     3537 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_multiply.py
--rw-r--r--   0 simon      (501) staff       (20)      961 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_size_calculations.py
--rw-r--r--   0 simon      (501) staff       (20)     3505 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_zoom.py
--rw-r--r--   0 simon      (501) staff       (20)    11335 2023-04-05 11:07:42.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_directing_analyzer.py
--rw-r--r--   0 simon      (501) staff       (20)    10128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_move_shape.py
--rw-r--r--   0 simon      (501) staff       (20)     5097 2023-04-05 20:01:02.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_menus.py
--rw-r--r--   0 simon      (501) staff       (20)    15175 2023-03-20 12:28:41.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_clf_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)    22682 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_image.py
--rw-r--r--   0 simon      (501) staff       (20)    57395 2023-04-06 00:28:01.000000 Simba-UW-tf-dev-1.55.3/simba/misc_tools.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/
--rw-r--r--   0 simon      (501) staff       (20)     2494 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/read_DANNCE_mat.py
--rw-r--r--   0 simon      (501) staff       (20)    25782 2023-03-20 12:51:35.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/sleap_importer_slp.py
--rw-r--r--   0 simon      (501) staff       (20)    24720 2023-03-13 15:26:36.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/sleap_importer_h5.py
--rw-r--r--   0 simon      (501) staff       (20)    26507 2023-03-21 12:58:39.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/dlc_multi_animal_importer.py
--rw-r--r--   0 simon      (501) staff       (20)    23731 2023-03-20 12:55:04.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/sleap_importer_csv.py
--rw-r--r--   0 simon      (501) staff       (20)    16536 2023-03-20 13:30:18.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/import_trk.py
--rw-r--r--   0 simon      (501) staff       (20)     7837 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/import_mars.py
--rw-r--r--   0 simon      (501) staff       (20)     8905 2023-03-20 13:49:13.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/dlc_importer_csv.py
--rw-r--r--   0 simon      (501) staff       (20)     8173 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_importers/trk_importer.py
--rw-r--r--   0 simon      (501) staff       (20)   232876 2023-04-06 14:21:49.000000 Simba-UW-tf-dev-1.55.3/simba/pop_up_classes.py
--rw-r--r--   0 simon      (501) staff       (20)     4692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/extract_seqframes.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/
--rw-r--r--   0 simon      (501) staff       (20)    14340 2023-03-30 11:05:37.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/bp_names/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:00.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/bp_names/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     1316 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/bp_names/bp_names.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/no_animals/
--rw-r--r--   0 simon      (501) staff       (20)       24 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/no_animals/no_animals.csv
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:19.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/no_animals/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/configuration_names/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:14.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/configuration_names/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)      267 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/configuration_names/pose_config_names.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-30 10:45:10.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    39805 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/8.png
--rw-r--r--   0 simon      (501) staff       (20)    62501 2023-03-30 10:39:05.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/9.png
--rw-r--r--   0 simon      (501) staff       (20)     6172 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/12.png
--rw-r--r--   0 simon      (501) staff       (20)    69501 2023-03-30 10:44:04.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/11.png
--rw-r--r--   0 simon      (501) staff       (20)    69410 2023-03-30 10:40:01.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/10.png
--rw-r--r--   0 simon      (501) staff       (20)    16000 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/4.png
--rw-r--r--   0 simon      (501) staff       (20)    28150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/5.png
--rw-r--r--   0 simon      (501) staff       (20)    31140 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/7.png
--rw-r--r--   0 simon      (501) staff       (20)    30634 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/6.png
--rw-r--r--   0 simon      (501) staff       (20)    15417 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/2.png
--rw-r--r--   0 simon      (501) staff       (20)    15786 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/3.png
--rw-r--r--   0 simon      (501) staff       (20)    18939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/1.png
--rw-r--r--   0 simon      (501) staff       (20)     7273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/get_coordinates_tools_v2.py
--rw-r--r--   0 simon      (501) staff       (20)    16252 2023-03-15 19:16:56.000000 Simba-UW-tf-dev-1.55.3/simba/pup_retrieval_protocol.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/
--rw-r--r--   0 simon      (501) staff       (20)     7712 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/outlier_corrector_movement.py
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-15 17:05:05.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)     8264 2023-03-15 17:05:35.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/outlier_corrector_location.py
--rw-r--r--   0 simon      (501) staff       (20)     4362 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/skip_outlier_correction.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/
--rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/outlier_scripts.iml
--rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/encodings.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/inspectionProfiles/
--rw-r--r--   0 simon      (501) staff       (20)      668 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/libraries/
--rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/libraries/R_User_Library.xml
--rw-r--r--   0 simon      (501) staff       (20)     8102 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/workspace.xml
--rw-r--r--   0 simon      (501) staff       (20)      289 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/modules.xml
--rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/misc.xml
--rw-r--r--   0 simon      (501) staff       (20)     2569 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/pose_reset.py
--rw-r--r--   0 simon      (501) staff       (20)    17642 2023-04-04 23:10:52.000000 Simba-UW-tf-dev-1.55.3/simba/train_mutiple_models.py
--rw-r--r--   0 simon      (501) staff       (20)    60134 2023-04-06 19:52:45.000000 Simba-UW-tf-dev-1.55.3/simba/SimBA.py
--rw-r--r--   0 simon      (501) staff       (20)    27431 2023-04-04 14:39:01.000000 Simba-UW-tf-dev-1.55.3/simba/labelling_advanced_interface.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/unsupervised/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/unsupervised/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)   109483 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/unsupervised/model_names.parquet
--rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/unsupervised/features.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/
--rw-r--r--   0 simon      (501) staff       (20)     1177 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/down_arrow.jpg
--rw-r--r--   0 simon      (501) staff       (20)     1733 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/intruder_shape.jpg
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/feature_categories/
--rw-r--r--   0 simon      (501) staff       (20)      109 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/feature_categories/.~lock.shap_feature_categories.csv#
--rw-r--r--   0 simon      (501) staff       (20)    17420 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/feature_categories/shap_feature_categories.csv
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)     1665 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_shape.jpg
--rw-r--r--   0 simon      (501) staff       (20)     2415 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_intruder_shape.jpg
--rw-r--r--   0 simon      (501) staff       (20)     2012 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/animal_distances.jpg
--rw-r--r--   0 simon      (501) staff       (20)     4422 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/baseline_scale.jpg
--rw-r--r--   0 simon      (501) staff       (20)   353824 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/ubuntu.regular.ttf
--rw-r--r--   0 simon      (501) staff       (20)     6672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/side_scale.jpg
--rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/UbuntuMono-Regular.ttf
--rw-r--r--   0 simon      (501) staff       (20)     2737 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/side_scale_5.jpg
--rw-r--r--   0 simon      (501) staff       (20)     1785 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/intruder_movement.jpg
--rw-r--r--   0 simon      (501) staff       (20)     1435 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_movement.jpg
--rw-r--r--   0 simon      (501) staff       (20)     3134 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/color_bar.jpg
--rw-r--r--   0 simon      (501) staff       (20)     2120 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_intruder_movement.jpg
--rw-r--r--   0 simon      (501) staff       (20)    16388 2023-04-06 18:20:18.000000 Simba-UW-tf-dev-1.55.3/simba/assets/.DS_Store
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/lookups/
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/lookups/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)   270783 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/lookups/model_names.parquet
--rw-r--r--   0 simon      (501) staff       (20)     2426 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/lookups/feature_extraction_headers.csv
--rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/lookups/features.csv
--rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/lookups/unsupervised_example_x.csv
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/stl/
--rw-r--r--   0 simon      (501) staff       (20)   551576 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/stl/operant_tray.stl
--rw-r--r--   0 simon      (501) staff       (20)    67647 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/stl/operant_lever.stl
--rw-r--r--   0 simon      (501) staff       (20)    92896 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/stl/operant_walls.stl
--rw-r--r--   0 simon      (501) staff       (20)  4759984 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/stl/grid_floor.stl
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/img/
--rw-r--r--   0 simon      (501) staff       (20)   399272 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/img/about_me.png
--rw-r--r--   0 simon      (501) staff       (20)   322242 2023-04-06 16:38:51.000000 Simba-UW-tf-dev-1.55.3/simba/assets/img/bg_2.png
--rw-r--r--   0 simon      (501) staff       (20)   454535 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/img/splash.png
--rw-r--r--   0 simon      (501) staff       (20)    69267 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/img/splash.pptx
--rw-r--r--   0 simon      (501) staff       (20)   204362 2023-04-06 15:01:45.000000 Simba-UW-tf-dev-1.55.3/simba/assets/img/bg.png
--rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/UbuntuMono-Regular.ttf
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/
--rw-r--r--   0 simon      (501) staff       (20)     1350 2023-03-17 17:59:27.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/factory.png
--rw-r--r--   0 simon      (501) staff       (20)     1413 2023-03-21 13:03:06.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/cluster.png
--rw-r--r--   0 simon      (501) staff       (20)     1340 2023-03-17 16:51:08.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/load.png
--rw-r--r--   0 simon      (501) staff       (20)     4507 2023-03-20 14:13:48.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/gif.png
--rw-rw-r--   0 simon      (501) staff       (20)     4566 2023-03-18 18:12:27.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/pose.png
--rw-rw-r--   0 simon      (501) staff       (20)     1943 2023-03-18 18:14:10.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/features.png
--rw-r--r--   0 simon      (501) staff       (20)     6148 2023-04-05 17:25:36.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/.DS_Store
--rw-rw-r--   0 simon      (501) staff       (20)     4896 2023-03-17 19:17:29.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/settings.png
--rw-r--r--   0 simon      (501) staff       (20)     1252 2023-03-19 16:48:40.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/link.png
--rw-r--r--   0 simon      (501) staff       (20)    14250 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/dash_simba.css
--rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-05 16:43:13.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/documentation.png
--rw-r--r--   0 simon      (501) staff       (20)     4503 2023-03-20 14:08:00.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/fps.png
--rw-r--r--   0 simon      (501) staff       (20)     1299 2023-03-21 13:02:07.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/dimensionality_reduction.png
--rw-rw-r--   0 simon      (501) staff       (20)     4823 2023-03-17 19:03:29.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/roi.png
--rw-r--r--   0 simon      (501) staff       (20)      920 2023-03-20 14:25:03.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/superimpose.png
--rw-r--r--   0 simon      (501) staff       (20)     1136 2023-03-18 20:25:31.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/label.png
--rw-r--r--   0 simon      (501) staff       (20)     1016 2023-03-20 14:28:47.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/change.png
--rw-r--r--   0 simon      (501) staff       (20)     1124 2023-03-17 18:05:26.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/crop.png
--rw-r--r--   0 simon      (501) staff       (20)     1057 2023-03-20 14:03:42.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/path.png
--rw-r--r--   0 simon      (501) staff       (20)      950 2023-03-17 18:07:33.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/clip.png
--rw-r--r--   0 simon      (501) staff       (20)     2121 2023-04-04 14:37:43.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/restart.png
--rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-17 18:11:59.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/calipher.png
--rw-r--r--   0 simon      (501) staff       (20)     1291 2023-03-21 20:16:55.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/add_on.png
--rw-rw-r--   0 simon      (501) staff       (20)     4695 2023-03-17 17:57:16.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/create.png
--rw-r--r--   0 simon      (501) staff       (20)    78182 2023-03-20 16:35:36.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/SimBA_logo.ico
--rw-r--r--   0 simon      (501) staff       (20)     1067 2023-03-20 14:22:44.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/print.png
--rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-18 20:27:58.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/clf.png
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/
--rw-r--r--   0 simon      (501) staff       (20)     6027 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/mosaic.png
--rw-r--r--   0 simon      (501) staff       (20)     5654 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/vertical.png
--rw-r--r--   0 simon      (501) staff       (20)     5542 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/horizontal.png
--rw-r--r--   0 simon      (501) staff       (20)     5939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/mixed_mosaic.png
--rw-r--r--   0 simon      (501) staff       (20)     2060 2023-03-20 14:26:12.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/merge.png
--rw-------   0 simon      (501) staff       (20)     4725 2023-03-18 20:27:47.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/clf_2.png
--rw-rw-r--   0 simon      (501) staff       (20)     4795 2023-03-17 18:10:10.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/visualize.png
--rw-r--r--   0 simon      (501) staff       (20)     2142 2023-03-20 14:10:28.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat.png
--rw-r--r--   0 simon      (501) staff       (20)     1474 2023-03-17 19:20:24.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/boris.png
--rw-rw-r--   0 simon      (501) staff       (20)     4804 2023-03-19 16:43:01.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/frames.png
--rw-r--r--   0 simon      (501) staff       (20)     2425 2023-03-19 16:44:55.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/video.png
--rw-r--r--   0 simon      (501) staff       (20)     2089 2023-03-20 14:05:58.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/sample.png
--rw-r--r--   0 simon      (501) staff       (20)     1471 2023-03-21 13:04:02.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/metrics.png
--rw-r--r--   0 simon      (501) staff       (20)     4555 2023-03-20 14:21:02.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/grey.png
--rw-r--r--   0 simon      (501) staff       (20)      930 2023-03-18 18:07:29.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/exit.png
--rw-r--r--   0 simon      (501) staff       (20)     4751 2023-03-18 20:31:58.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/outlier.png
--rw-r--r--   0 simon      (501) staff       (20)     4392 2023-03-20 14:16:15.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/clahe.png
--rw-rw-r--   0 simon      (501) staff       (20)     4637 2023-03-17 19:03:55.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/trash.png
--rw-r--r--   0 simon      (501) staff       (20)     1239 2023-03-19 16:51:21.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/about.png
--rw-rw-r--   0 simon      (501) staff       (20)     4666 2023-03-17 18:01:21.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/convert.png
--rw-r--r--   0 simon      (501) staff       (20)    93229 2023-03-20 16:01:42.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/SimBA_logo.icns
--rw-r--r--   0 simon      (501) staff       (20)      991 2023-03-20 19:02:33.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/reorganize.png
--rw-rw-r--   0 simon      (501) staff       (20)     4784 2023-03-17 18:50:35.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/browse.png
--rw-r--r--   0 simon      (501) staff       (20)    30707 2023-03-20 16:33:38.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/SimBA_logo.png
--rw-r--r--   0 simon      (501) staff       (20)     2293 2023-03-17 19:24:38.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/ethovision.png
--rw-r--r--   0 simon      (501) staff       (20)     1018 2023-04-05 15:24:49.000000 Simba-UW-tf-dev-1.55.3/simba/assets/icons/close.png
--rw-r--r--   0 simon      (501) staff       (20)    13672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/dash_simba_base.css
--rw-r--r--   0 simon      (501) staff       (20)    31812 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/assets/TheGoldenLab.PNG
--rw-r--r--   0 simon      (501) staff       (20)    21392 2023-03-22 19:01:48.000000 Simba-UW-tf-dev-1.55.3/simba/drop_bp_cords.py
--rw-r--r--   0 simon      (501) staff       (20)     8116 2023-03-19 18:27:51.000000 Simba-UW-tf-dev-1.55.3/simba/read_config_unit_tests.py
--rw-r--r--   0 simon      (501) staff       (20)    11564 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/project_config_creator.py
--rw-r--r--   0 simon      (501) staff       (20)    27444 2023-03-15 15:58:40.000000 Simba-UW-tf-dev-1.55.3/simba/set_hyperparameters.py
--rw-r--r--   0 simon      (501) staff       (20)    20780 2023-04-04 23:58:36.000000 Simba-UW-tf-dev-1.55.3/simba/train_single_model.py
--rw-r--r--   0 simon      (501) staff       (20)     6426 2023-03-17 16:57:53.000000 Simba-UW-tf-dev-1.55.3/simba/create_clf_log.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/
--rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-17 14:43:38.000000 Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/.DS_Store
--rw-r--r--   0 simon      (501) staff       (20)    24896 2023-04-06 11:29:26.000000 Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/batch_process_menus.py
--rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/__init__.py
--rw-r--r--   0 simon      (501) staff       (20)    10936 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py
--rw-r--r--   0 simon      (501) staff       (20)     9563 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.3/simba/Kleinberg_calculator.py
--rw-r--r--   0 simon      (501) staff       (20)     8392 2023-04-03 14:06:05.000000 Simba-UW-tf-dev-1.55.3/simba/reorganize_keypoint_in_pose.py
--rw-r--r--   0 simon      (501) staff       (20)      165 2023-03-25 11:18:21.000000 Simba-UW-tf-dev-1.55.3/simba/~$features.pptx
--rw-r--r--   0 simon      (501) staff       (20)     6557 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.3/simba/play_annotation_video.py
-drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/
--rw-rw-r--   0 simon      (501) staff       (20)      579 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/PKG-INFO
--rw-rw-r--   0 simon      (501) staff       (20)    12849 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/SOURCES.txt
--rw-rw-r--   0 simon      (501) staff       (20)       44 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/entry_points.txt
--rw-rw-r--   0 simon      (501) staff       (20)      642 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/requires.txt
--rw-rw-r--   0 simon      (501) staff       (20)        6 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/top_level.txt
--rw-rw-r--   0 simon      (501) staff       (20)        1 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/dependency_links.txt
--rw-rw-r--   0 simon      (501) staff       (20)     7652 2020-05-13 13:27:38.000000 Simba-UW-tf-dev-1.55.3/LICENSE.md
--rw-rw-r--   0 simon      (501) staff       (20)      136 2021-04-10 10:44:06.000000 Simba-UW-tf-dev-1.55.3/MANIFEST.in
--rw-rw-r--   0 simon      (501) staff       (20)     9598 2020-05-13 13:27:40.000000 Simba-UW-tf-dev-1.55.3/README.md
--rw-rw-r--   0 simon      (501) staff       (20)     1899 2023-04-06 19:58:41.000000 Simba-UW-tf-dev-1.55.3/setup.py
--rw-r--r--   0 simon      (501) staff       (20)       38 2023-04-06 19:58:46.000000 Simba-UW-tf-dev-1.55.3/setup.cfg
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/
+-rw-r--r--   0 simon      (501) staff       (20)      579 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/PKG-INFO
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/
+-rw-r--r--   0 simon      (501) staff       (20)    32569 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.4/simba/video_processing.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/blob_storage/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-21 20:39:46.000000 Simba-UW-tf-dev-1.55.4/simba/blob_storage/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/
+-rw-r--r--   0 simon      (501) staff       (20)    10851 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/unsupervised_ui.py
+-rw-r--r--   0 simon      (501) staff       (20)     6566 2023-03-21 14:26:03.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/misc.py
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     7227 2023-03-21 11:41:26.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/dataset_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)     4061 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/data_extractors.py
+-rw-r--r--   0 simon      (501) staff       (20)    11192 2023-03-21 20:14:50.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/dbcv.py
+-rw-r--r--   0 simon      (501) staff       (20)    11456 2023-03-21 18:17:26.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/visualizers.py
+-rw-r--r--   0 simon      (501) staff       (20)     7526 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/umap_embedder.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/visualization_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     2019 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/visualization_tools/vtk_embeddings.py
+-rw-r--r--   0 simon      (501) staff       (20)      150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/ui_tools.py
+-rw-r--r--   0 simon      (501) staff       (20)    49992 2023-03-22 15:08:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/pop_up_classes.py
+-rw-r--r--   0 simon      (501) staff       (20)    16189 2023-03-21 15:42:27.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/cluster_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)     6642 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/hdbscan_clusterer.py
+-rw-r--r--   0 simon      (501) staff       (20)     3789 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/tsne.py
+-rw-r--r--   0 simon      (501) staff       (20)     5630 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/unsupervised/cluster_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    19024 2023-04-06 19:25:58.000000 Simba-UW-tf-dev-1.55.4/simba/enums.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     7463 2023-03-15 19:17:12.000000 Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/agg_boundary_stats.py
+-rw-r--r--   0 simon      (501) staff       (20)     8562 2023-03-15 19:17:04.000000 Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/find_bounderies.py
+-rw-r--r--   0 simon      (501) staff       (20)    24561 2023-04-06 11:22:38.000000 Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/boundary_menus.py
+-rw-r--r--   0 simon      (501) staff       (20)     9530 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/boundary_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)    12627 2023-03-15 16:54:41.000000 Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/visualize_boundaries.py
+-rw-r--r--   0 simon      (501) staff       (20)    32772 2023-04-04 14:38:01.000000 Simba-UW-tf-dev-1.55.4/simba/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/
+-rw-r--r--   0 simon      (501) staff       (20)    42807 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_14bp.py
+-rw-r--r--   0 simon      (501) staff       (20)    21541 2023-03-15 19:11:32.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_7bp.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/
+-rw-r--r--   0 simon      (501) staff       (20)     2732 2023-04-04 19:46:36.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/read_in_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    14141 2023-03-15 17:20:08.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/fish_feature_extractor_2022.py
+-rw-r--r--   0 simon      (501) staff       (20)     2053 2023-04-04 03:00:41.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/convex_hull_3_scratch_3.py
+-rw-r--r--   0 simon      (501) staff       (20)     5762 2023-04-04 01:54:33.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/convex_hull_scratch_1.py
+-rw-r--r--   0 simon      (501) staff       (20)    19620 2023-04-03 12:08:14.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/fish_feature_extractor_2023.py
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 19:36:02.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     7127 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/egocentrical_aligner.py
+-rw-r--r--   0 simon      (501) staff       (20)     4708 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/graph_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)     3954 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/termite_rois.csv
+-rw-r--r--   0 simon      (501) staff       (20)      732 2023-03-20 12:13:51.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/mutual_exclusive.py
+-rw-r--r--   0 simon      (501) staff       (20)     1862 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/graph_3d_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)     2692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/add_probability_cnt_features.py
+-rw-r--r--   0 simon      (501) staff       (20)     2058 2023-04-03 23:51:37.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/convex_hull_scratch_2.py
+-rw-r--r--   0 simon      (501) staff       (20)    28028 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_8bps_2_animals.py
+-rw-r--r--   0 simon      (501) staff       (20)    10244 2023-04-06 18:38:15.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     2347 2023-04-04 12:57:34.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/perimeter_jit.py
+-rw-r--r--   0 simon      (501) staff       (20)    10734 2023-04-06 14:57:55.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_subsets.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__init__.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/
+-rw-r--r--   0 simon      (501) staff       (20)      905 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi
+-rw-r--r--   0 simon      (501) staff       (20)   238196 2023-04-04 11:31:57.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc
+-rw-r--r--   0 simon      (501) staff       (20)    69038 2023-04-04 11:32:25.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc
+-rw-r--r--   0 simon      (501) staff       (20)   238298 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc
+-rw-r--r--   0 simon      (501) staff       (20)    69338 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc
+-rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-04 11:32:29.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi
+-rw-r--r--   0 simon      (501) staff       (20)     2179 2023-04-04 11:32:26.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi
+-rw-r--r--   0 simon      (501) staff       (20)    36798 2023-03-15 17:04:48.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/extract_features_9bp.py
+-rw-r--r--   0 simon      (501) staff       (20)     8428 2023-03-15 19:11:54.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_user_defined.py
+-rw-r--r--   0 simon      (501) staff       (20)     5323 2023-03-19 18:30:53.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/unit_tests.py
+-rw-r--r--   0 simon      (501) staff       (20)    46473 2023-04-04 13:07:58.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_16bp.py
+-rw-r--r--   0 simon      (501) staff       (20)    24093 2023-04-04 13:11:31.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_8bp.py
+-rw-r--r--   0 simon      (501) staff       (20)    16763 2023-03-15 19:11:50.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_4bp.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/
+-rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/features_scripts.iml
+-rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/encodings.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/inspectionProfiles/
+-rw-r--r--   0 simon      (501) staff       (20)      822 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/libraries/
+-rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/libraries/R_User_Library.xml
+-rw-r--r--   0 simon      (501) staff       (20)      273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/.gitignore
+-rw-r--r--   0 simon      (501) staff       (20)     8081 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/workspace.xml
+-rw-r--r--   0 simon      (501) staff       (20)      291 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/modules.xml
+-rw-r--r--   0 simon      (501) staff       (20)       23 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/.name
+-rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/misc.xml
+-rw-r--r--   0 simon      (501) staff       (20)     6044 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/plotly_create_h5.py
+-rw-r--r--   0 simon      (501) staff       (20)    15351 2023-04-06 14:48:36.000000 Simba-UW-tf-dev-1.55.4/simba/requirements.txt
+-rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-15 19:16:48.000000 Simba-UW-tf-dev-1.55.4/simba/severity_processor.py
+-rw-r--r--   0 simon      (501) staff       (20)     5941 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.4/simba/user_pose_config_creator.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/mixins/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:26:03.000000 Simba-UW-tf-dev-1.55.4/simba/mixins/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    41856 2023-04-05 17:24:50.000000 Simba-UW-tf-dev-1.55.4/simba/mixins/pop_up_mixin.py
+-rw-r--r--   0 simon      (501) staff       (20)     8182 2023-04-05 13:03:24.000000 Simba-UW-tf-dev-1.55.4/simba/mixins/config_reader.py
+-rw-r--r--   0 simon      (501) staff       (20)     6781 2023-04-06 14:21:49.000000 Simba-UW-tf-dev-1.55.4/simba/mixins/feature_extraction_mixin.py
+-rw-r--r--   0 simon      (501) staff       (20)    34512 2023-04-06 19:49:53.000000 Simba-UW-tf-dev-1.55.4/simba/machine_model_settings_pop_up.py
+-rw-r--r--   0 simon      (501) staff       (20)     5266 2023-03-15 15:43:20.000000 Simba-UW-tf-dev-1.55.4/simba/remove_keypoints_in_pose.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/
+-rw-r--r--   0 simon      (501) staff       (20)     6326 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/deepethogram_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)     9947 2023-03-18 15:35:38.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/BORIS_appender.py
+-rw-r--r--   0 simon      (501) staff       (20)     9170 2023-03-22 19:35:38.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/observer_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)    16922 2023-03-28 20:30:38.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/tools.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-04-01 14:10:06.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)    18283 2023-04-01 14:14:21.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/third_party_appender.py
+-rw-r--r--   0 simon      (501) staff       (20)     8336 2023-03-15 19:12:46.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/ethovision_import.py
+-rw-r--r--   0 simon      (501) staff       (20)     6919 2023-03-19 15:03:14.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/BENTO_appender.py
+-rw-r--r--   0 simon      (501) staff       (20)     5426 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/solomon_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)     7261 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/multi_cropper.py
+-rw-r--r--   0 simon      (501) staff       (20)    13056 2023-03-19 16:33:18.000000 Simba-UW-tf-dev-1.55.4/simba/FSTTC_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)    12620 2023-04-06 11:43:07.000000 Simba-UW-tf-dev-1.55.4/simba/create_project_pop_up.py
+-rw-r--r--   0 simon      (501) staff       (20)    13421 2023-04-06 11:40:29.000000 Simba-UW-tf-dev-1.55.4/simba/video_info_table.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-15 17:25:58.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     8507 2023-03-15 19:09:16.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_clf_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)    13530 2023-03-15 19:08:52.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    18253 2023-04-06 11:29:26.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_menues.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)     1660 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_tools.py
+-rw-r--r--   0 simon      (501) staff       (20)    16374 2023-03-15 19:09:04.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    13160 2023-03-20 13:43:59.000000 Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_movement_statistics.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)     2813 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/extract_frames_fast.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/utils/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-14 20:15:03.000000 Simba-UW-tf-dev-1.55.4/simba/utils/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     5626 2023-03-28 20:35:14.000000 Simba-UW-tf-dev-1.55.4/simba/utils/warnings.py
+-rw-r--r--   0 simon      (501) staff       (20)     3825 2023-04-06 19:25:38.000000 Simba-UW-tf-dev-1.55.4/simba/utils/lookups.py
+-rw-r--r--   0 simon      (501) staff       (20)    11967 2023-04-06 19:37:44.000000 Simba-UW-tf-dev-1.55.4/simba/utils/errors.py
+-rw-r--r--   0 simon      (501) staff       (20)    21581 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/labelling_interface.py
+-rw-r--r--   0 simon      (501) staff       (20)     9937 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.4/simba/timebins_movement_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    45524 2023-04-04 20:09:14.000000 Simba-UW-tf-dev-1.55.4/simba/train_model_functions.py
+-rw-r--r--   0 simon      (501) staff       (20)    49699 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/SimBA_dash_app.py
+-rw-r--r--   0 simon      (501) staff       (20)     7520 2023-03-19 16:35:16.000000 Simba-UW-tf-dev-1.55.4/simba/timebins_clf_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     8240 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.4/simba/calculate_px_dist.py
+-rw-r--r--   0 simon      (501) staff       (20)     6548 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/movement_processor.py
+-rw-r--r--   0 simon      (501) staff       (20)     2904 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pybursts.py
+-rw-r--r--   0 simon      (501) staff       (20)     5265 2023-03-29 18:04:02.000000 Simba-UW-tf-dev-1.55.4/simba/run_model_new.py
+-rw-r--r--   0 simon      (501) staff       (20)     3104 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/rw_dfs.py
+-rw-r--r--   0 simon      (501) staff       (20)     6684 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/reverse_2_animal_tracking.py
+-rw-r--r--   0 simon      (501) staff       (20)     9743 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.4/simba/Directing_animals_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     4357 2023-03-30 16:19:09.000000 Simba-UW-tf-dev-1.55.4/simba/Validate_model_one_video_run_clf.py
+-rw-r--r--   0 simon      (501) staff       (20)     9548 2023-04-06 00:40:25.000000 Simba-UW-tf-dev-1.55.4/simba/tkinter_functions.py
+-rw-r--r--   0 simon      (501) staff       (20)    13767 2023-03-24 12:49:19.000000 Simba-UW-tf-dev-1.55.4/simba/setting_menu.py
+-rw-r--r--   0 simon      (501) staff       (20)     6614 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/interpolate_pose.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/
+-rw-r--r--   0 simon      (501) staff       (20)     8571 2023-03-30 10:06:59.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/gantt_creator.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/tools/
+-rw-r--r--   0 simon      (501) staff       (20)     5353 2023-03-30 15:38:37.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/tools/tkinter_tools.py
+-rw-r--r--   0 simon      (501) staff       (20)    17962 2023-03-24 13:40:30.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_plotter_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    14592 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/shap_agg_stats_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    12928 2023-03-30 10:08:46.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/gantt_creator_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    15777 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_clf_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     8884 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/probability_plot_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)    16058 2023-03-22 14:43:52.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/misc_visualizations.py
+-rw-r--r--   0 simon      (501) staff       (20)    13501 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/plot_clf_results.py
+-rw-r--r--   0 simon      (501) staff       (20)    17696 2023-03-29 16:22:09.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/plot_clf_results_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    16328 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_feature_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    12588 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_location.py
+-rw-r--r--   0 simon      (501) staff       (20)    12585 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/probability_plot_creator_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     5341 2023-03-30 15:46:49.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/interactive_probability_grapher.py
+-rw-r--r--   0 simon      (501) staff       (20)     5832 2023-03-29 17:02:51.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/plot_pose_in_dir.py
+-rw-r--r--   0 simon      (501) staff       (20)    12184 2023-03-31 13:53:09.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/single_run_model_validation_video.py
+-rw-r--r--   0 simon      (501) staff       (20)    11202 2023-03-19 16:21:53.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/frame_mergerer_ffmpeg.py
+-rw-r--r--   0 simon      (501) staff       (20)    12442 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/Directing_animals_visualizer_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     9856 2023-03-17 16:23:58.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/clf_validator.py
+-rw-r--r--   0 simon      (501) staff       (20)    17290 2023-04-06 00:33:50.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/path_plotter_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    19958 2023-03-24 13:47:50.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_feature_visualizer_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    10157 2023-03-17 16:27:19.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/data_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)    12444 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/path_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)     8609 2023-03-15 13:37:59.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/ez_lineplot.py
+-rw-r--r--   0 simon      (501) staff       (20)    12970 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/distance_plotter_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)    15626 2023-03-29 17:05:49.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)    13165 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_clf.py
+-rw-r--r--   0 simon      (501) staff       (20)     8891 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/distance_plotter.py
+-rw-r--r--   0 simon      (501) staff       (20)    13554 2023-04-01 13:12:31.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/single_run_model_validation_video_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     9839 2023-03-17 16:34:02.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/Directing_animals_visualizer.py
+-rw-r--r--   0 simon      (501) staff       (20)    16155 2023-03-20 13:34:43.000000 Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_location_mp.py
+-rw-r--r--   0 simon      (501) staff       (20)     5029 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/run_dash_tkinter.py
+-rw-r--r--   0 simon      (501) staff       (20)     7454 2023-03-13 22:11:36.000000 Simba-UW-tf-dev-1.55.4/simba/interpolate_smooth_post_hoc.py
+-rw-r--r--   0 simon      (501) staff       (20)    24474 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/dash_app.py
+-rw-r--r--   0 simon      (501) staff       (20)     6350 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/reverse_tracking_order.py
+-rw-r--r--   0 simon      (501) staff       (20)     5772 2023-03-20 13:55:20.000000 Simba-UW-tf-dev-1.55.4/simba/concatenator_pop_up.py
+-rw-r--r--   0 simon      (501) staff       (20)     2824 2023-03-24 16:12:51.000000 Simba-UW-tf-dev-1.55.4/simba/extract_annotation_frames.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     7385 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_time_bin_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)     2248 2023-03-24 13:34:06.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_movement_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-20 12:47:56.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    43831 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_define.py
+-rw-r--r--   0 simon      (501) staff       (20)     3384 2023-03-20 12:41:16.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_reset.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)    21382 2023-03-31 10:40:20.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    11920 2023-03-31 10:48:40.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_feature_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)     3537 2023-03-15 17:12:38.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_multiply.py
+-rw-r--r--   0 simon      (501) staff       (20)      961 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_size_calculations.py
+-rw-r--r--   0 simon      (501) staff       (20)     3505 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_zoom.py
+-rw-r--r--   0 simon      (501) staff       (20)    11335 2023-04-05 11:07:42.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_directing_analyzer.py
+-rw-r--r--   0 simon      (501) staff       (20)    10128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_move_shape.py
+-rw-r--r--   0 simon      (501) staff       (20)     5097 2023-04-05 20:01:02.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_menus.py
+-rw-r--r--   0 simon      (501) staff       (20)    15175 2023-03-20 12:28:41.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_clf_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)    22682 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_image.py
+-rw-r--r--   0 simon      (501) staff       (20)    57395 2023-04-06 00:28:01.000000 Simba-UW-tf-dev-1.55.4/simba/misc_tools.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/
+-rw-r--r--   0 simon      (501) staff       (20)     2494 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/read_DANNCE_mat.py
+-rw-r--r--   0 simon      (501) staff       (20)    25782 2023-03-20 12:51:35.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/sleap_importer_slp.py
+-rw-r--r--   0 simon      (501) staff       (20)    24720 2023-03-13 15:26:36.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/sleap_importer_h5.py
+-rw-r--r--   0 simon      (501) staff       (20)    26507 2023-03-21 12:58:39.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/dlc_multi_animal_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)    23731 2023-03-20 12:55:04.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/sleap_importer_csv.py
+-rw-r--r--   0 simon      (501) staff       (20)    16536 2023-03-20 13:30:18.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/import_trk.py
+-rw-r--r--   0 simon      (501) staff       (20)     7837 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/import_mars.py
+-rw-r--r--   0 simon      (501) staff       (20)     8905 2023-03-20 13:49:13.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/dlc_importer_csv.py
+-rw-r--r--   0 simon      (501) staff       (20)     8173 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_importers/trk_importer.py
+-rw-r--r--   0 simon      (501) staff       (20)   232876 2023-04-06 14:21:49.000000 Simba-UW-tf-dev-1.55.4/simba/pop_up_classes.py
+-rw-r--r--   0 simon      (501) staff       (20)     4692 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/extract_seqframes.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/
+-rw-r--r--   0 simon      (501) staff       (20)    14340 2023-03-30 11:05:37.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/bp_names/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:00.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/bp_names/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     1316 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/bp_names/bp_names.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/no_animals/
+-rw-r--r--   0 simon      (501) staff       (20)       24 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/no_animals/no_animals.csv
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:19.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/no_animals/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/configuration_names/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-16 13:26:14.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/configuration_names/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)      267 2023-03-20 15:55:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/configuration_names/pose_config_names.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-30 10:45:10.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    39805 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/8.png
+-rw-r--r--   0 simon      (501) staff       (20)    62501 2023-03-30 10:39:05.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/9.png
+-rw-r--r--   0 simon      (501) staff       (20)     6172 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/12.png
+-rw-r--r--   0 simon      (501) staff       (20)    69501 2023-03-30 10:44:04.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/11.png
+-rw-r--r--   0 simon      (501) staff       (20)    69410 2023-03-30 10:40:01.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/10.png
+-rw-r--r--   0 simon      (501) staff       (20)    16000 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/4.png
+-rw-r--r--   0 simon      (501) staff       (20)    28150 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/5.png
+-rw-r--r--   0 simon      (501) staff       (20)    31140 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/7.png
+-rw-r--r--   0 simon      (501) staff       (20)    30634 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/6.png
+-rw-r--r--   0 simon      (501) staff       (20)    15417 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/2.png
+-rw-r--r--   0 simon      (501) staff       (20)    15786 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/3.png
+-rw-r--r--   0 simon      (501) staff       (20)    18939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/1.png
+-rw-r--r--   0 simon      (501) staff       (20)     7273 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/get_coordinates_tools_v2.py
+-rw-r--r--   0 simon      (501) staff       (20)    16252 2023-03-15 19:16:56.000000 Simba-UW-tf-dev-1.55.4/simba/pup_retrieval_protocol.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/
+-rw-r--r--   0 simon      (501) staff       (20)     7712 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/outlier_corrector_movement.py
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-15 17:05:05.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)     8264 2023-03-15 17:05:35.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/outlier_corrector_location.py
+-rw-r--r--   0 simon      (501) staff       (20)     4362 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/skip_outlier_correction.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/
+-rw-r--r--   0 simon      (501) staff       (20)      617 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/outlier_scripts.iml
+-rw-r--r--   0 simon      (501) staff       (20)      138 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/encodings.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/inspectionProfiles/
+-rw-r--r--   0 simon      (501) staff       (20)      668 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/libraries/
+-rw-r--r--   0 simon      (501) staff       (20)      128 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/libraries/R_User_Library.xml
+-rw-r--r--   0 simon      (501) staff       (20)     8102 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/workspace.xml
+-rw-r--r--   0 simon      (501) staff       (20)      289 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/modules.xml
+-rw-r--r--   0 simon      (501) staff       (20)      294 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/misc.xml
+-rw-r--r--   0 simon      (501) staff       (20)     2569 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/pose_reset.py
+-rw-r--r--   0 simon      (501) staff       (20)    17642 2023-04-04 23:10:52.000000 Simba-UW-tf-dev-1.55.4/simba/train_mutiple_models.py
+-rw-r--r--   0 simon      (501) staff       (20)    60142 2023-04-06 20:06:44.000000 Simba-UW-tf-dev-1.55.4/simba/SimBA.py
+-rw-r--r--   0 simon      (501) staff       (20)    27431 2023-04-04 14:39:01.000000 Simba-UW-tf-dev-1.55.4/simba/labelling_advanced_interface.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/unsupervised/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/unsupervised/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)   109483 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/unsupervised/model_names.parquet
+-rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/unsupervised/features.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/
+-rw-r--r--   0 simon      (501) staff       (20)     1177 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/down_arrow.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     1733 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/intruder_shape.jpg
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/feature_categories/
+-rw-r--r--   0 simon      (501) staff       (20)      109 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/feature_categories/.~lock.shap_feature_categories.csv#
+-rw-r--r--   0 simon      (501) staff       (20)    17420 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/feature_categories/shap_feature_categories.csv
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)     1665 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_shape.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     2415 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_intruder_shape.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     2012 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/animal_distances.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     4422 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/baseline_scale.jpg
+-rw-r--r--   0 simon      (501) staff       (20)   353824 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/ubuntu.regular.ttf
+-rw-r--r--   0 simon      (501) staff       (20)     6672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/side_scale.jpg
+-rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/UbuntuMono-Regular.ttf
+-rw-r--r--   0 simon      (501) staff       (20)     2737 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/side_scale_5.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     1785 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/intruder_movement.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     1435 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_movement.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     3134 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/color_bar.jpg
+-rw-r--r--   0 simon      (501) staff       (20)     2120 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_intruder_movement.jpg
+-rw-r--r--   0 simon      (501) staff       (20)    16388 2023-04-06 18:20:18.000000 Simba-UW-tf-dev-1.55.4/simba/assets/.DS_Store
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/lookups/
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/lookups/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)   270783 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/lookups/model_names.parquet
+-rw-r--r--   0 simon      (501) staff       (20)     2426 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/lookups/feature_extraction_headers.csv
+-rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/lookups/features.csv
+-rw-r--r--   0 simon      (501) staff       (20)    14175 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/lookups/unsupervised_example_x.csv
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/stl/
+-rw-r--r--   0 simon      (501) staff       (20)   551576 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/stl/operant_tray.stl
+-rw-r--r--   0 simon      (501) staff       (20)    67647 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/stl/operant_lever.stl
+-rw-r--r--   0 simon      (501) staff       (20)    92896 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/stl/operant_walls.stl
+-rw-r--r--   0 simon      (501) staff       (20)  4759984 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/stl/grid_floor.stl
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/img/
+-rw-r--r--   0 simon      (501) staff       (20)   399272 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/img/about_me.png
+-rw-r--r--   0 simon      (501) staff       (20)   322242 2023-04-06 16:38:51.000000 Simba-UW-tf-dev-1.55.4/simba/assets/img/bg_2.png
+-rw-r--r--   0 simon      (501) staff       (20)   454535 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/img/splash.png
+-rw-r--r--   0 simon      (501) staff       (20)    69267 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/img/splash.pptx
+-rw-r--r--   0 simon      (501) staff       (20)   204362 2023-04-06 15:01:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/img/bg.png
+-rw-r--r--   0 simon      (501) staff       (20)   189004 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/UbuntuMono-Regular.ttf
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/
+-rw-r--r--   0 simon      (501) staff       (20)     1350 2023-03-17 17:59:27.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/factory.png
+-rw-r--r--   0 simon      (501) staff       (20)     1413 2023-03-21 13:03:06.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/cluster.png
+-rw-r--r--   0 simon      (501) staff       (20)     1340 2023-03-17 16:51:08.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/load.png
+-rw-r--r--   0 simon      (501) staff       (20)     4507 2023-03-20 14:13:48.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/gif.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4566 2023-03-18 18:12:27.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/pose.png
+-rw-rw-r--   0 simon      (501) staff       (20)     1943 2023-03-18 18:14:10.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/features.png
+-rw-r--r--   0 simon      (501) staff       (20)     6148 2023-04-05 17:25:36.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/.DS_Store
+-rw-rw-r--   0 simon      (501) staff       (20)     4896 2023-03-17 19:17:29.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/settings.png
+-rw-r--r--   0 simon      (501) staff       (20)     1252 2023-03-19 16:48:40.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/link.png
+-rw-r--r--   0 simon      (501) staff       (20)    14250 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/dash_simba.css
+-rw-r--r--   0 simon      (501) staff       (20)      917 2023-04-05 16:43:13.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/documentation.png
+-rw-r--r--   0 simon      (501) staff       (20)     4503 2023-03-20 14:08:00.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/fps.png
+-rw-r--r--   0 simon      (501) staff       (20)     1299 2023-03-21 13:02:07.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/dimensionality_reduction.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4823 2023-03-17 19:03:29.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/roi.png
+-rw-r--r--   0 simon      (501) staff       (20)      920 2023-03-20 14:25:03.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/superimpose.png
+-rw-r--r--   0 simon      (501) staff       (20)     1136 2023-03-18 20:25:31.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/label.png
+-rw-r--r--   0 simon      (501) staff       (20)     1016 2023-03-20 14:28:47.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/change.png
+-rw-r--r--   0 simon      (501) staff       (20)     1124 2023-03-17 18:05:26.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/crop.png
+-rw-r--r--   0 simon      (501) staff       (20)     1057 2023-03-20 14:03:42.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/path.png
+-rw-r--r--   0 simon      (501) staff       (20)      950 2023-03-17 18:07:33.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/clip.png
+-rw-r--r--   0 simon      (501) staff       (20)     2121 2023-04-04 14:37:43.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/restart.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-17 18:11:59.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/calipher.png
+-rw-r--r--   0 simon      (501) staff       (20)     1291 2023-03-21 20:16:55.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/add_on.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4695 2023-03-17 17:57:16.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/create.png
+-rw-r--r--   0 simon      (501) staff       (20)    78182 2023-03-20 16:35:36.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/SimBA_logo.ico
+-rw-r--r--   0 simon      (501) staff       (20)     1067 2023-03-20 14:22:44.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/print.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4653 2023-03-18 20:27:58.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/clf.png
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/
+-rw-r--r--   0 simon      (501) staff       (20)     6027 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/mosaic.png
+-rw-r--r--   0 simon      (501) staff       (20)     5654 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/vertical.png
+-rw-r--r--   0 simon      (501) staff       (20)     5542 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/horizontal.png
+-rw-r--r--   0 simon      (501) staff       (20)     5939 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/mixed_mosaic.png
+-rw-r--r--   0 simon      (501) staff       (20)     2060 2023-03-20 14:26:12.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/merge.png
+-rw-------   0 simon      (501) staff       (20)     4725 2023-03-18 20:27:47.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/clf_2.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4795 2023-03-17 18:10:10.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/visualize.png
+-rw-r--r--   0 simon      (501) staff       (20)     2142 2023-03-20 14:10:28.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat.png
+-rw-r--r--   0 simon      (501) staff       (20)     1474 2023-03-17 19:20:24.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/boris.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4804 2023-03-19 16:43:01.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/frames.png
+-rw-r--r--   0 simon      (501) staff       (20)     2425 2023-03-19 16:44:55.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/video.png
+-rw-r--r--   0 simon      (501) staff       (20)     2089 2023-03-20 14:05:58.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/sample.png
+-rw-r--r--   0 simon      (501) staff       (20)     1471 2023-03-21 13:04:02.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/metrics.png
+-rw-r--r--   0 simon      (501) staff       (20)     4555 2023-03-20 14:21:02.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/grey.png
+-rw-r--r--   0 simon      (501) staff       (20)      930 2023-03-18 18:07:29.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/exit.png
+-rw-r--r--   0 simon      (501) staff       (20)     4751 2023-03-18 20:31:58.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/outlier.png
+-rw-r--r--   0 simon      (501) staff       (20)     4392 2023-03-20 14:16:15.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/clahe.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4637 2023-03-17 19:03:55.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/trash.png
+-rw-r--r--   0 simon      (501) staff       (20)     1239 2023-03-19 16:51:21.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/about.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4666 2023-03-17 18:01:21.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/convert.png
+-rw-r--r--   0 simon      (501) staff       (20)    93229 2023-03-20 16:01:42.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/SimBA_logo.icns
+-rw-r--r--   0 simon      (501) staff       (20)      991 2023-03-20 19:02:33.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/reorganize.png
+-rw-rw-r--   0 simon      (501) staff       (20)     4784 2023-03-17 18:50:35.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/browse.png
+-rw-r--r--   0 simon      (501) staff       (20)    30707 2023-03-20 16:33:38.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/SimBA_logo.png
+-rw-r--r--   0 simon      (501) staff       (20)     2293 2023-03-17 19:24:38.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/ethovision.png
+-rw-r--r--   0 simon      (501) staff       (20)     1018 2023-04-05 15:24:49.000000 Simba-UW-tf-dev-1.55.4/simba/assets/icons/close.png
+-rw-r--r--   0 simon      (501) staff       (20)    13672 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/dash_simba_base.css
+-rw-r--r--   0 simon      (501) staff       (20)    31812 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/assets/TheGoldenLab.PNG
+-rw-r--r--   0 simon      (501) staff       (20)    21392 2023-03-22 19:01:48.000000 Simba-UW-tf-dev-1.55.4/simba/drop_bp_cords.py
+-rw-r--r--   0 simon      (501) staff       (20)     8116 2023-03-19 18:27:51.000000 Simba-UW-tf-dev-1.55.4/simba/read_config_unit_tests.py
+-rw-r--r--   0 simon      (501) staff       (20)    11564 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/project_config_creator.py
+-rw-r--r--   0 simon      (501) staff       (20)    27444 2023-03-15 15:58:40.000000 Simba-UW-tf-dev-1.55.4/simba/set_hyperparameters.py
+-rw-r--r--   0 simon      (501) staff       (20)    20780 2023-04-04 23:58:36.000000 Simba-UW-tf-dev-1.55.4/simba/train_single_model.py
+-rw-r--r--   0 simon      (501) staff       (20)     6426 2023-03-17 16:57:53.000000 Simba-UW-tf-dev-1.55.4/simba/create_clf_log.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/
+-rw-r--r--   0 simon      (501) staff       (20)     8196 2023-03-17 14:43:38.000000 Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/.DS_Store
+-rw-r--r--   0 simon      (501) staff       (20)    24896 2023-04-06 11:29:26.000000 Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/batch_process_menus.py
+-rw-r--r--   0 simon      (501) staff       (20)        0 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/__init__.py
+-rw-r--r--   0 simon      (501) staff       (20)    10936 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py
+-rw-r--r--   0 simon      (501) staff       (20)     9563 2023-03-19 16:33:17.000000 Simba-UW-tf-dev-1.55.4/simba/Kleinberg_calculator.py
+-rw-r--r--   0 simon      (501) staff       (20)     8392 2023-04-03 14:06:05.000000 Simba-UW-tf-dev-1.55.4/simba/reorganize_keypoint_in_pose.py
+-rw-r--r--   0 simon      (501) staff       (20)      165 2023-03-25 11:18:21.000000 Simba-UW-tf-dev-1.55.4/simba/~$features.pptx
+-rw-r--r--   0 simon      (501) staff       (20)     6557 2023-03-10 20:04:56.000000 Simba-UW-tf-dev-1.55.4/simba/play_annotation_video.py
+drwxr-xr-x   0 simon      (501) staff       (20)        0 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/
+-rw-rw-r--   0 simon      (501) staff       (20)      579 2023-04-06 20:10:44.000000 Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/PKG-INFO
+-rw-rw-r--   0 simon      (501) staff       (20)    12849 2023-04-06 20:10:44.000000 Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/SOURCES.txt
+-rw-rw-r--   0 simon      (501) staff       (20)       44 2023-04-06 20:10:44.000000 Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/entry_points.txt
+-rw-rw-r--   0 simon      (501) staff       (20)      642 2023-04-06 20:10:44.000000 Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/requires.txt
+-rw-rw-r--   0 simon      (501) staff       (20)        6 2023-04-06 20:10:44.000000 Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/top_level.txt
+-rw-rw-r--   0 simon      (501) staff       (20)        1 2023-04-06 20:10:44.000000 Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/dependency_links.txt
+-rw-rw-r--   0 simon      (501) staff       (20)     7652 2020-05-13 13:27:38.000000 Simba-UW-tf-dev-1.55.4/LICENSE.md
+-rw-rw-r--   0 simon      (501) staff       (20)      136 2021-04-10 10:44:06.000000 Simba-UW-tf-dev-1.55.4/MANIFEST.in
+-rw-rw-r--   0 simon      (501) staff       (20)     9598 2020-05-13 13:27:40.000000 Simba-UW-tf-dev-1.55.4/README.md
+-rw-rw-r--   0 simon      (501) staff       (20)     1899 2023-04-06 20:08:49.000000 Simba-UW-tf-dev-1.55.4/setup.py
+-rw-r--r--   0 simon      (501) staff       (20)       38 2023-04-06 20:10:45.000000 Simba-UW-tf-dev-1.55.4/setup.cfg
```

### Comparing `Simba-UW-tf-dev-1.55.3/PKG-INFO` & `Simba-UW-tf-dev-1.55.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Simba-UW-tf-dev
-Version: 1.55.3
+Version: 1.55.4
 Summary: Toolkit for computer classification of complex social behaviors in experimental animals
 Home-page: https://github.com/sgoldenlab/simba
 Author: Simon Nilsson, Jia Jie Choong, Sophia Hwang
 Author-email: sronilsson@gmail.com
 License: GNU Lesser General Public License v3 (LGPLv3)
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `Simba-UW-tf-dev-1.55.3/simba/video_processing.py` & `Simba-UW-tf-dev-1.55.4/simba/video_processing.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/blob_storage/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/blob_storage/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/unsupervised_ui.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/unsupervised_ui.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/misc.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/misc.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/dataset_creator.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/dataset_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/data_extractors.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/data_extractors.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/dbcv.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/dbcv.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/visualizers.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/visualizers.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/umap_embedder.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/umap_embedder.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/visualization_tools/vtk_embeddings.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/visualization_tools/vtk_embeddings.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/pop_up_classes.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/pop_up_classes.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/cluster_statistics.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/cluster_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/hdbscan_clusterer.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/hdbscan_clusterer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/tsne.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/tsne.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/unsupervised/cluster_visualizer.py` & `Simba-UW-tf-dev-1.55.4/simba/unsupervised/cluster_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/enums.py` & `Simba-UW-tf-dev-1.55.4/simba/enums.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/agg_boundary_stats.py` & `Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/agg_boundary_stats.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/find_bounderies.py` & `Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/find_bounderies.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/boundary_menus.py` & `Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/boundary_menus.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/boundary_statistics.py` & `Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/boundary_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/bounding_box_tools/visualize_boundaries.py` & `Simba-UW-tf-dev-1.55.4/simba/bounding_box_tools/visualize_boundaries.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_14bp.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_14bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_7bp.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_7bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/read_in_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/read_in_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/fish_feature_extractor_2022.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/fish_feature_extractor_2022.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/convex_hull_3_scratch_3.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/convex_hull_3_scratch_3.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/convex_hull_scratch_1.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/convex_hull_scratch_1.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/fish_feature_extractor_2023.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/fish_feature_extractor_2023.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/egocentrical_aligner.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/egocentrical_aligner.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/graph_creator.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/graph_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/termite_rois.csv` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/termite_rois.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/mutual_exclusive.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/mutual_exclusive.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/graph_3d_plotter.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/graph_3d_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/add_probability_cnt_features.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/add_probability_cnt_features.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/misc/convex_hull_scratch_2.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/misc/convex_hull_scratch_2.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_8bps_2_animals.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_8bps_2_animals.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/perimeter_jit.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/perimeter_jit.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_subsets.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_subsets.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.nbi`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.quickhull_2d-16.py36m.1.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.1.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.1.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.2.nbc`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.convex_hull_perimeter_2d-16.py36m.nbi`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/__pycache__/perimeter_jit.process-7.py36m.nbi`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/extract_features_9bp.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/extract_features_9bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_user_defined.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_user_defined.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/unit_tests.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/unit_tests.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_16bp.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_16bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_8bp.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_8bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/feature_extractor_4bp.py` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/feature_extractor_4bp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/features_scripts.iml` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/features_scripts.iml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/inspectionProfiles/Project_Default.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/feature_extractors/.idea/workspace.xml` & `Simba-UW-tf-dev-1.55.4/simba/feature_extractors/.idea/workspace.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotly_create_h5.py` & `Simba-UW-tf-dev-1.55.4/simba/plotly_create_h5.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/requirements.txt` & `Simba-UW-tf-dev-1.55.4/simba/requirements.txt`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/severity_processor.py` & `Simba-UW-tf-dev-1.55.4/simba/severity_processor.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/user_pose_config_creator.py` & `Simba-UW-tf-dev-1.55.4/simba/user_pose_config_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/mixins/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/mixins/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/mixins/pop_up_mixin.py` & `Simba-UW-tf-dev-1.55.4/simba/mixins/pop_up_mixin.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/mixins/config_reader.py` & `Simba-UW-tf-dev-1.55.4/simba/mixins/config_reader.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/mixins/feature_extraction_mixin.py` & `Simba-UW-tf-dev-1.55.4/simba/mixins/feature_extraction_mixin.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/machine_model_settings_pop_up.py` & `Simba-UW-tf-dev-1.55.4/simba/machine_model_settings_pop_up.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/remove_keypoints_in_pose.py` & `Simba-UW-tf-dev-1.55.4/simba/remove_keypoints_in_pose.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/deepethogram_importer.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/deepethogram_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/BORIS_appender.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/BORIS_appender.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/observer_importer.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/observer_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/tools.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/third_party_appender.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/third_party_appender.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/ethovision_import.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/ethovision_import.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/BENTO_appender.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/BENTO_appender.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/third_party_label_appenders/solomon_importer.py` & `Simba-UW-tf-dev-1.55.4/simba/third_party_label_appenders/solomon_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/multi_cropper.py` & `Simba-UW-tf-dev-1.55.4/simba/multi_cropper.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/FSTTC_calculator.py` & `Simba-UW-tf-dev-1.55.4/simba/FSTTC_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/create_project_pop_up.py` & `Simba-UW-tf-dev-1.55.4/simba/create_project_pop_up.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/video_info_table.py` & `Simba-UW-tf-dev-1.55.4/simba/video_info_table.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_clf_statistics.py` & `Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_clf_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_menues.py` & `Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_menues.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_tools.py` & `Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_visualizer.py` & `Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/cue_light_tools/cue_light_movement_statistics.py` & `Simba-UW-tf-dev-1.55.4/simba/cue_light_tools/cue_light_movement_statistics.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/extract_frames_fast.py` & `Simba-UW-tf-dev-1.55.4/simba/extract_frames_fast.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/utils/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/utils/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/utils/warnings.py` & `Simba-UW-tf-dev-1.55.4/simba/utils/warnings.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/utils/lookups.py` & `Simba-UW-tf-dev-1.55.4/simba/utils/lookups.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/utils/errors.py` & `Simba-UW-tf-dev-1.55.4/simba/utils/errors.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/labelling_interface.py` & `Simba-UW-tf-dev-1.55.4/simba/labelling_interface.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/timebins_movement_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/timebins_movement_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/train_model_functions.py` & `Simba-UW-tf-dev-1.55.4/simba/train_model_functions.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/SimBA_dash_app.py` & `Simba-UW-tf-dev-1.55.4/simba/SimBA_dash_app.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/timebins_clf_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/timebins_clf_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/calculate_px_dist.py` & `Simba-UW-tf-dev-1.55.4/simba/calculate_px_dist.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/movement_processor.py` & `Simba-UW-tf-dev-1.55.4/simba/movement_processor.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pybursts.py` & `Simba-UW-tf-dev-1.55.4/simba/pybursts.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/run_model_new.py` & `Simba-UW-tf-dev-1.55.4/simba/run_model_new.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/rw_dfs.py` & `Simba-UW-tf-dev-1.55.4/simba/rw_dfs.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/reverse_2_animal_tracking.py` & `Simba-UW-tf-dev-1.55.4/simba/reverse_2_animal_tracking.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/Directing_animals_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/Directing_animals_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/Validate_model_one_video_run_clf.py` & `Simba-UW-tf-dev-1.55.4/simba/Validate_model_one_video_run_clf.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/tkinter_functions.py` & `Simba-UW-tf-dev-1.55.4/simba/tkinter_functions.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/setting_menu.py` & `Simba-UW-tf-dev-1.55.4/simba/setting_menu.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/interpolate_pose.py` & `Simba-UW-tf-dev-1.55.4/simba/interpolate_pose.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/gantt_creator.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/gantt_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/tools/tkinter_tools.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/tools/tkinter_tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_plotter_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_plotter_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/shap_agg_stats_visualizer.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/shap_agg_stats_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/gantt_creator_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/gantt_creator_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_clf_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_clf_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/probability_plot_creator.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/probability_plot_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/misc_visualizations.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/misc_visualizations.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/plot_clf_results.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/plot_clf_results.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/plot_clf_results_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/plot_clf_results_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_feature_visualizer.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_feature_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_location.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_location.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/probability_plot_creator_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/probability_plot_creator_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/interactive_probability_grapher.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/interactive_probability_grapher.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/plot_pose_in_dir.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/plot_pose_in_dir.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/single_run_model_validation_video.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/single_run_model_validation_video.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/frame_mergerer_ffmpeg.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/frame_mergerer_ffmpeg.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/Directing_animals_visualizer_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/Directing_animals_visualizer_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/clf_validator.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/clf_validator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/path_plotter_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/path_plotter_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_feature_visualizer_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_feature_visualizer_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/data_plotter.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/data_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/path_plotter.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/path_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/ez_lineplot.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/ez_lineplot.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/distance_plotter_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/distance_plotter_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/ROI_plotter.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/ROI_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_clf.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_clf.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/distance_plotter.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/distance_plotter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/single_run_model_validation_video_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/single_run_model_validation_video_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/Directing_animals_visualizer.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/Directing_animals_visualizer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/plotting/heat_mapper_location_mp.py` & `Simba-UW-tf-dev-1.55.4/simba/plotting/heat_mapper_location_mp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/run_dash_tkinter.py` & `Simba-UW-tf-dev-1.55.4/simba/run_dash_tkinter.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/interpolate_smooth_post_hoc.py` & `Simba-UW-tf-dev-1.55.4/simba/interpolate_smooth_post_hoc.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/dash_app.py` & `Simba-UW-tf-dev-1.55.4/simba/dash_app.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/reverse_tracking_order.py` & `Simba-UW-tf-dev-1.55.4/simba/reverse_tracking_order.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/concatenator_pop_up.py` & `Simba-UW-tf-dev-1.55.4/simba/concatenator_pop_up.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/extract_annotation_frames.py` & `Simba-UW-tf-dev-1.55.4/simba/extract_annotation_frames.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_time_bin_calculator.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_time_bin_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_movement_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_movement_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_define.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_define.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_reset.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_reset.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_feature_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_feature_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_multiply.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_multiply.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_size_calculations.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_size_calculations.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_zoom.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_zoom.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_directing_analyzer.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_directing_analyzer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_move_shape.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_move_shape.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_menus.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_menus.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_clf_calculator.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_clf_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/roi_tools/ROI_image.py` & `Simba-UW-tf-dev-1.55.4/simba/roi_tools/ROI_image.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/misc_tools.py` & `Simba-UW-tf-dev-1.55.4/simba/misc_tools.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/read_DANNCE_mat.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/read_DANNCE_mat.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/sleap_importer_slp.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/sleap_importer_slp.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/sleap_importer_h5.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/sleap_importer_h5.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/dlc_multi_animal_importer.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/dlc_multi_animal_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/sleap_importer_csv.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/sleap_importer_csv.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/import_trk.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/import_trk.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/import_mars.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/import_mars.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/dlc_importer_csv.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/dlc_importer_csv.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_importers/trk_importer.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_importers/trk_importer.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pop_up_classes.py` & `Simba-UW-tf-dev-1.55.4/simba/pop_up_classes.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/extract_seqframes.py` & `Simba-UW-tf-dev-1.55.4/simba/extract_seqframes.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/bp_names/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/bp_names/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/bp_names/bp_names.csv` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/bp_names/bp_names.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/no_animals/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/no_animals/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/configuration_names/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/configuration_names/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/8.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/8.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/9.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/9.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/12.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/12.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/11.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/11.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/10.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/10.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/4.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/4.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/5.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/5.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/7.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/7.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/6.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/6.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/2.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/2.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/3.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/3.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_configurations/schematics/1.png` & `Simba-UW-tf-dev-1.55.4/simba/pose_configurations/schematics/1.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/get_coordinates_tools_v2.py` & `Simba-UW-tf-dev-1.55.4/simba/get_coordinates_tools_v2.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pup_retrieval_protocol.py` & `Simba-UW-tf-dev-1.55.4/simba/pup_retrieval_protocol.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/outlier_tools/outlier_corrector_movement.py` & `Simba-UW-tf-dev-1.55.4/simba/outlier_tools/outlier_corrector_movement.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/outlier_tools/outlier_corrector_location.py` & `Simba-UW-tf-dev-1.55.4/simba/outlier_tools/outlier_corrector_location.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/outlier_tools/skip_outlier_correction.py` & `Simba-UW-tf-dev-1.55.4/simba/outlier_tools/skip_outlier_correction.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/outlier_scripts.iml` & `Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/outlier_scripts.iml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml` & `Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/inspectionProfiles/Project_Default.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/outlier_tools/.idea/workspace.xml` & `Simba-UW-tf-dev-1.55.4/simba/outlier_tools/.idea/workspace.xml`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/pose_reset.py` & `Simba-UW-tf-dev-1.55.4/simba/pose_reset.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/train_mutiple_models.py` & `Simba-UW-tf-dev-1.55.4/simba/train_mutiple_models.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/SimBA.py` & `Simba-UW-tf-dev-1.55.4/simba/SimBA.py`

 * *Files 0% similar despite different names*

```diff
@@ -735,15 +735,15 @@
         self.root.columnconfigure(0, weight=1)
         if currentPlatform == OS.WINDOWS.value:
             self.root.iconbitmap(icon_path_windows)
         if currentPlatform == OS.MAC.value:
             self.root.iconphoto(False, ImageTk.PhotoImage(PIL.Image.open(icon_path_darwin)))
         for k in self.menu_icons.keys():
             self.menu_icons[k]['img'] = ImageTk.PhotoImage(image=PIL.Image.open(os.path.join(os.path.dirname(__file__), self.menu_icons[k]['icon_path'])))
-        bg_img = PhotoImage(file=bg_path)
+        bg_img = ImageTk.PhotoImage(file=bg_path)
         background = Label(self.root, image=bg_img, bd=0, bg='white')
         background.pack(fill='both', expand=True)
         background.image = bg_img
 
         menu = Menu(self.root)
         self.root.config(menu=menu)
```

### Comparing `Simba-UW-tf-dev-1.55.3/simba/labelling_advanced_interface.py` & `Simba-UW-tf-dev-1.55.4/simba/labelling_advanced_interface.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/unsupervised/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/assets/unsupervised/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/unsupervised/model_names.parquet` & `Simba-UW-tf-dev-1.55.4/simba/assets/unsupervised/model_names.parquet`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/unsupervised/features.csv` & `Simba-UW-tf-dev-1.55.4/simba/assets/unsupervised/features.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/down_arrow.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/down_arrow.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/intruder_shape.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/intruder_shape.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/feature_categories/shap_feature_categories.csv` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/feature_categories/shap_feature_categories.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_shape.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_shape.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_intruder_shape.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_intruder_shape.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/animal_distances.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/animal_distances.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/baseline_scale.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/baseline_scale.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/ubuntu.regular.ttf` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/ubuntu.regular.ttf`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/side_scale.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/side_scale.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/UbuntuMono-Regular.ttf` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/UbuntuMono-Regular.ttf`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/side_scale_5.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/side_scale_5.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/intruder_movement.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/intruder_movement.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_movement.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_movement.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/color_bar.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/color_bar.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/shap/resident_intruder_movement.jpg` & `Simba-UW-tf-dev-1.55.4/simba/assets/shap/resident_intruder_movement.jpg`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/assets/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/lookups/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/assets/lookups/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/lookups/model_names.parquet` & `Simba-UW-tf-dev-1.55.4/simba/assets/lookups/model_names.parquet`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/lookups/feature_extraction_headers.csv` & `Simba-UW-tf-dev-1.55.4/simba/assets/lookups/feature_extraction_headers.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/lookups/features.csv` & `Simba-UW-tf-dev-1.55.4/simba/assets/lookups/features.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/lookups/unsupervised_example_x.csv` & `Simba-UW-tf-dev-1.55.4/simba/assets/lookups/unsupervised_example_x.csv`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/stl/operant_tray.stl` & `Simba-UW-tf-dev-1.55.4/simba/assets/stl/operant_tray.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/stl/operant_lever.stl` & `Simba-UW-tf-dev-1.55.4/simba/assets/stl/operant_lever.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/stl/operant_walls.stl` & `Simba-UW-tf-dev-1.55.4/simba/assets/stl/operant_walls.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/stl/grid_floor.stl` & `Simba-UW-tf-dev-1.55.4/simba/assets/stl/grid_floor.stl`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/img/about_me.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/img/about_me.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/img/bg_2.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/img/bg_2.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/img/splash.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/img/splash.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/img/splash.pptx` & `Simba-UW-tf-dev-1.55.4/simba/assets/img/splash.pptx`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/img/bg.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/img/bg.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/UbuntuMono-Regular.ttf` & `Simba-UW-tf-dev-1.55.4/simba/assets/UbuntuMono-Regular.ttf`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/factory.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/factory.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/cluster.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/cluster.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/load.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/load.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/gif.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/gif.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/pose.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/pose.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/features.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/features.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/settings.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/settings.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/link.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/link.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/dash_simba.css` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/dash_simba.css`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/documentation.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/documentation.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/fps.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/fps.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/dimensionality_reduction.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/dimensionality_reduction.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/roi.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/roi.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/superimpose.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/superimpose.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/label.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/label.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/change.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/change.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/crop.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/crop.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/path.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/path.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/clip.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/clip.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/restart.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/restart.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/calipher.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/calipher.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/add_on.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/add_on.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/create.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/create.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/SimBA_logo.ico` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/SimBA_logo.ico`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/print.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/print.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/clf.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/clf.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/mosaic.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/mosaic.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/vertical.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/vertical.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/horizontal.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/horizontal.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat_icons/mixed_mosaic.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat_icons/mixed_mosaic.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/merge.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/merge.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/clf_2.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/clf_2.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/visualize.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/visualize.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/concat.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/concat.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/boris.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/boris.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/frames.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/frames.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/video.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/video.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/sample.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/sample.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/metrics.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/metrics.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/grey.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/grey.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/exit.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/exit.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/outlier.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/outlier.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/clahe.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/clahe.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/trash.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/trash.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/about.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/about.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/convert.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/convert.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/SimBA_logo.icns` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/SimBA_logo.icns`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/reorganize.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/reorganize.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/browse.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/browse.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/SimBA_logo.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/SimBA_logo.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/ethovision.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/ethovision.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/icons/close.png` & `Simba-UW-tf-dev-1.55.4/simba/assets/icons/close.png`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/dash_simba_base.css` & `Simba-UW-tf-dev-1.55.4/simba/assets/dash_simba_base.css`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/assets/TheGoldenLab.PNG` & `Simba-UW-tf-dev-1.55.4/simba/assets/TheGoldenLab.PNG`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/drop_bp_cords.py` & `Simba-UW-tf-dev-1.55.4/simba/drop_bp_cords.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/read_config_unit_tests.py` & `Simba-UW-tf-dev-1.55.4/simba/read_config_unit_tests.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/project_config_creator.py` & `Simba-UW-tf-dev-1.55.4/simba/project_config_creator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/set_hyperparameters.py` & `Simba-UW-tf-dev-1.55.4/simba/set_hyperparameters.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/train_single_model.py` & `Simba-UW-tf-dev-1.55.4/simba/train_single_model.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/create_clf_log.py` & `Simba-UW-tf-dev-1.55.4/simba/create_clf_log.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/.DS_Store` & `Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/.DS_Store`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/batch_process_menus.py` & `Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/batch_process_menus.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py` & `Simba-UW-tf-dev-1.55.4/simba/batch_process_videos/batch_process_create_ffmpeg_commands.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/Kleinberg_calculator.py` & `Simba-UW-tf-dev-1.55.4/simba/Kleinberg_calculator.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/reorganize_keypoint_in_pose.py` & `Simba-UW-tf-dev-1.55.4/simba/reorganize_keypoint_in_pose.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/simba/play_annotation_video.py` & `Simba-UW-tf-dev-1.55.4/simba/play_annotation_video.py`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/PKG-INFO` & `Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Simba-UW-tf-dev
-Version: 1.55.3
+Version: 1.55.4
 Summary: Toolkit for computer classification of complex social behaviors in experimental animals
 Home-page: https://github.com/sgoldenlab/simba
 Author: Simon Nilsson, Jia Jie Choong, Sophia Hwang
 Author-email: sronilsson@gmail.com
 License: GNU Lesser General Public License v3 (LGPLv3)
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/SOURCES.txt` & `Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/Simba_UW_tf_dev.egg-info/requires.txt` & `Simba-UW-tf-dev-1.55.4/Simba_UW_tf_dev.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/LICENSE.md` & `Simba-UW-tf-dev-1.55.4/LICENSE.md`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/README.md` & `Simba-UW-tf-dev-1.55.4/README.md`

 * *Files identical despite different names*

### Comparing `Simba-UW-tf-dev-1.55.3/setup.py` & `Simba-UW-tf-dev-1.55.4/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 Licensed under GNU Lesser General Public License v3.0
 """
 
 import setuptools
 
 setuptools.setup(
     name="Simba-UW-tf-dev",
-    version="1.55.3",
+    version="1.55.4",
     author="Simon Nilsson, Jia Jie Choong, Sophia Hwang",
     author_email="sronilsson@gmail.com",
     description="Toolkit for computer classification of complex social behaviors in experimental animals",
     url="https://github.com/sgoldenlab/simba",
     install_requires=['Pillow == 5.4.1', 'pyyaml == 5.3.1','shapely == 1.7','wxpython == 4.0.4',
               'dtreeviz == 0.8.1','eli5 == 0.10.1','graphviz == 0.11',
               'imblearn == 0.7.0','imgaug == 0.4.0','imutils == 0.5.2','matplotlib == 3.0.3', 'numpy == 1.18.1',
```

