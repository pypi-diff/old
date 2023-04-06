# Comparing `tmp/plunk-0.1.98.tar.gz` & `tmp/plunk-0.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "plunk-0.1.98.tar", last modified: Wed Jan  4 17:47:24 2023, max compression
+gzip compressed data, was "plunk-0.1.99.tar", last modified: Wed Jan  4 18:46:28 2023, max compression
```

## Comparing `plunk-0.1.98.tar` & `plunk-0.1.99.tar`

### file list

```diff
@@ -1,268 +1,268 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.328491 plunk-0.1.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-01-04 17:46:46.000000 plunk-0.1.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-01-04 17:47:24.328491 plunk-0.1.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-01-04 17:46:46.000000 plunk-0.1.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.292490 plunk-0.1.98/plunk/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.292490 plunk-0.1.98/plunk/ap/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.292490 plunk-0.1.98/plunk/ap/audio_stream/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/audio_stream/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/audio_stream/audiostream_webservice.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.292490 plunk-0.1.98/plunk/ap/live_graph/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/live_graph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9386 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/live_graph/audio_store.py
--rw-r--r--   0 runner    (1001) docker     (123)     7915 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/live_graph/live_graph_data_buffer.py
--rw-r--r--   0 runner    (1001) docker     (123)     5722 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/live_graph/live_graph_streamlitfront.py
--rw-r--r--   0 runner    (1001) docker     (123)      796 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/snippets.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.296491 plunk-0.1.98/plunk/ap/store_explorer/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/store_explorer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2460 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/store_explorer/store_explorer_app.py
--rw-r--r--   0 runner    (1001) docker     (123)     4877 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/store_explorer/store_explorer_element.py
--rw-r--r--   0 runner    (1001) docker     (123)     1711 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/store_explorer/streamlit_store_explorer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1844 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ap/wav_encode.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.296491 plunk-0.1.98/plunk/ca/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/ca/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.296491 plunk-0.1.98/plunk/sb/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.296491 plunk-0.1.98/plunk/sb/click_detection/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/click_detection/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      958 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/click_detection/analysis.py
--rw-r--r--   0 runner    (1001) docker     (123)      528 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/click_detection/clickified.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.296491 plunk-0.1.98/plunk/sb/front_demo/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10391 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/data_prep.py
--rw-r--r--   0 runner    (1001) docker     (123)    11363 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/data_prep_scores.py
--rw-r--r--   0 runner    (1001) docker     (123)     2389 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/data_viz.py
--rw-r--r--   0 runner    (1001) docker     (123)     4027 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/learner_example.py
--rw-r--r--   0 runner    (1001) docker     (123)     5159 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/record_load_play.py
--rw-r--r--   0 runner    (1001) docker     (123)    10784 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/thor_dag_example.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.296491 plunk-0.1.98/plunk/sb/front_demo/user_story1/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.300490 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10114 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app0.py
--rw-r--r--   0 runner    (1001) docker     (123)    14648 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app1.py
--rw-r--r--   0 runner    (1001) docker     (123)    11621 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app2.py
--rw-r--r--   0 runner    (1001) docker     (123)    12025 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app3.py
--rw-r--r--   0 runner    (1001) docker     (123)    10209 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_5drill.py
--rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_6learner.py
--rw-r--r--   0 runner    (1001) docker     (123)    10192 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_7_funcnodes_exclude.py
--rw-r--r--   0 runner    (1001) docker     (123)    10208 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_drill.py
--rw-r--r--   0 runner    (1001) docker     (123)     2165 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_drill_Andie.py
--rw-r--r--   0 runner    (1001) docker     (123)    10994 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app5_drill.py
--rw-r--r--   0 runner    (1001) docker     (123)    13465 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app5_s3dol.py
--rw-r--r--   0 runner    (1001) docker     (123)     7798 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_base_audio.py
--rw-r--r--   0 runner    (1001) docker     (123)     6244 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_choosing_model.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_dummy.py
--rw-r--r--   0 runner    (1001) docker     (123)     5947 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_scrap.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.300490 plunk-0.1.98/plunk/sb/front_demo/user_story1/components/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/components/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2287 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/components/components.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.300490 plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2421 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/funcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/simple_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5210 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.300490 plunk-0.1.98/plunk/sb/front_experiments/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/audio_app.py
--rw-r--r--   0 runner    (1001) docker     (123)     1542 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/audio_histo.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.300490 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.300490 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      829 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app0.py
--rw-r--r--   0 runner    (1001) docker     (123)      635 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app0_5_folder_picker.py
--rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app0_6_folder_picker.py
--rw-r--r--   0 runner    (1001) docker     (123)     3148 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app1.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.300490 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/components/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/components/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1366 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/components/elements.py
--rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/components/folder_picker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.304490 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/dags/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/dags/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/dags/wf_store_splatter.py
--rw-r--r--   0 runner    (1001) docker     (123)      481 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/dags/wfstore_and_annots_to_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.304490 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/utils/tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.308491 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8944 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/aggrid.py
--rw-r--r--   0 runner    (1001) docker     (123)      218 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/barfi_app.py
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/chk_if_click.py
--rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/crudified_ag_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1156 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_1.py
--rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.308491 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_app/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_app/Home.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_app/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5159 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_impulse_like_bytes.py
--rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/elements.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.308491 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/js/
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/js/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/kmeans_streamz.py
--rw-r--r--   0 runner    (1001) docker     (123)     3805 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/learner_example.py
--rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/river_t.py
--rw-r--r--   0 runner    (1001) docker     (123)     1960 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap.py
--rw-r--r--   0 runner    (1001) docker     (123)     4342 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1299 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap3.py
--rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap_crude.py
--rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap_dash.py
--rw-r--r--   0 runner    (1001) docker     (123)     1086 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap_sound_tagger.py
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrapsound.py
--rw-r--r--   0 runner    (1001) docker     (123)     2786 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_store_explorer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_store_explorer2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3124 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger.py
--rw-r--r--   0 runner    (1001) docker     (123)     3251 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4938 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger3.py
--rw-r--r--   0 runner    (1001) docker     (123)     4681 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger4.py
--rw-r--r--   0 runner    (1001) docker     (123)     5150 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger5.py
--rw-r--r--   0 runner    (1001) docker     (123)     5168 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger6.py
--rw-r--r--   0 runner    (1001) docker     (123)     4416 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger7_with_tabs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3496 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger8_input_with_audio.py
--rw-r--r--   0 runner    (1001) docker     (123)      911 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/stream_df.py
--rw-r--r--   0 runner    (1001) docker     (123)      865 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/stream_live.py
--rw-r--r--   0 runner    (1001) docker     (123)     1260 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/stream_taped.py
--rw-r--r--   0 runner    (1001) docker     (123)     7332 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/tagging_tool.py
--rw-r--r--   0 runner    (1001) docker     (123)     2474 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/tagging_tool_scrap.py
--rw-r--r--   0 runner    (1001) docker     (123)     1017 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/edge_interface/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.312491 plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/get_stream.py
--rw-r--r--   0 runner    (1001) docker     (123)     1719 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/get_stream2.py
--rw-r--r--   0 runner    (1001) docker     (123)     2008 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/get_stream3.py
--rw-r--r--   0 runner    (1001) docker     (123)     1046 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlit_front_example.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.312491 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1961 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/analysis.py
--rw-r--r--   0 runner    (1001) docker     (123)     6664 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep.py
--rw-r--r--   0 runner    (1001) docker     (123)     7630 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep10.py
--rw-r--r--   0 runner    (1001) docker     (123)    10389 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep11.py
--rw-r--r--   0 runner    (1001) docker     (123)     3496 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep2.py
--rw-r--r--   0 runner    (1001) docker     (123)     2547 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep3.py
--rw-r--r--   0 runner    (1001) docker     (123)     2263 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep4.py
--rw-r--r--   0 runner    (1001) docker     (123)     3708 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep5.py
--rw-r--r--   0 runner    (1001) docker     (123)     1909 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep6.py
--rw-r--r--   0 runner    (1001) docker     (123)     7137 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep7.py
--rw-r--r--   0 runner    (1001) docker     (123)     5963 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep8.py
--rw-r--r--   0 runner    (1001) docker     (123)     5242 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep9.py
--rw-r--r--   0 runner    (1001) docker     (123)     3324 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep_scrap.py
--rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/tackle_args.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.316491 plunk-0.1.98/plunk/sb/meshed_experiments/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/meshed_experiments/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14785 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/meshed_experiments/meshed_kwargs.py
--rw-r--r--   0 runner    (1001) docker     (123)    55011 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/meshed_experiments/scrap_dag.py
--rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/meshed_experiments/scrap_dotdigraph.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.316491 plunk-0.1.98/plunk/sb/metaflow_practice/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/metaflow_practice/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/metaflow_practice/classify.py
--rw-r--r--   0 runner    (1001) docker     (123)     2070 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/metaflow_practice/classify_phone.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.316491 plunk-0.1.98/plunk/sb/odat_lab/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/odat_lab/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/odat_lab/circuit_breaker.py
--rw-r--r--   0 runner    (1001) docker     (123)      470 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/odat_lab/functional_dacc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1299 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/odat_lab/guns.py
--rw-r--r--   0 runner    (1001) docker     (123)      396 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/odat_lab/hamlet.py
--rw-r--r--   0 runner    (1001) docker     (123)      459 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/odat_lab/heartbeat.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.316491 plunk-0.1.98/plunk/sb/ordering_funcnodes/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/ordering_funcnodes/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1352 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/ordering_funcnodes/reorder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.316491 plunk-0.1.98/plunk/sb/ordering_funcnodes/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/ordering_funcnodes/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/ordering_funcnodes/tests/test_reorder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.320491 plunk-0.1.98/plunk/sb/pydantic_for_front/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/pydantic_for_front/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      812 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/pydantic_for_front/func_to_opyrator.py
--rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/pydantic_for_front/opyrator_multiple_funcs.py
--rw-r--r--   0 runner    (1001) docker     (123)      837 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/pydantic_for_front/pydantic_dispatch_enum.py
--rw-r--r--   0 runner    (1001) docker     (123)      971 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/pydantic_for_front/pydantic_streamlit_front.py
--rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/pydantic_for_front/pydantic_streamlit_input.py
--rw-r--r--   0 runner    (1001) docker     (123)     3593 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/pydantic_for_front/tooltips_app.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.320491 plunk-0.1.98/plunk/sb/sig_compatibility/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/sig_builtins.py
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/sig_code_to_dag.py
--rw-r--r--   0 runner    (1001) docker     (123)     6769 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/sig_comp.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/sig_script.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.320491 plunk-0.1.98/plunk/sb/sig_compatibility/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12393 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/tests/test_sig_builtins.py
--rw-r--r--   0 runner    (1001) docker     (123)      312 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/tests/test_sig_code_to_dag.py
--rw-r--r--   0 runner    (1001) docker     (123)      946 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/sig_compatibility/tests/test_sig_comp.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.320491 plunk-0.1.98/plunk/sb/slabsiter_experiments/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/slabsiter_experiments/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/slabsiter_experiments/dict_generators.py
--rw-r--r--   0 runner    (1001) docker     (123)     1461 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/slabsiter_experiments/livewf_slabs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.320491 plunk-0.1.98/plunk/sb/slabsiter_experiments/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/slabsiter_experiments/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      982 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/slabsiter_experiments/tests/test_dict_generators.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.320491 plunk-0.1.98/plunk/sb/type_compatibility/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/type_compatibility/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2476 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/type_compatibility/compatible.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.320491 plunk-0.1.98/plunk/sb/type_compatibility/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/type_compatibility/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1225 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/type_compatibility/tests/scrap.py
--rw-r--r--   0 runner    (1001) docker     (123)     1161 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/sb/type_compatibility/tests/test_compatible.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.324491 plunk-0.1.98/plunk/tw/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/echoed_clicks.py
--rw-r--r--   0 runner    (1001) docker     (123)     1535 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/empty_sentinel_options.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.324491 plunk-0.1.98/plunk/tw/front_examples/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.324491 plunk-0.1.98/plunk/tw/front_examples/audio_ml/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/audio_ml/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/audio_ml/take01_simple_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)    12110 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/audio_ml/tw_app4_drill.py
--rw-r--r--   0 runner    (1001) docker     (123)     4233 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/audio_ml/tw_app4_drill_components.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.324491 plunk-0.1.98/plunk/tw/front_examples/crude_examples/
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4160 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/extrude_crude_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/pydantic_examples.py
--rw-r--r--   0 runner    (1001) docker     (123)     4296 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/scrap_streamlit.py
--rw-r--r--   0 runner    (1001) docker     (123)      799 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_01_salary.py
--rw-r--r--   0 runner    (1001) docker     (123)      947 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_02_salary.py
--rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_03_salary.py
--rw-r--r--   0 runner    (1001) docker     (123)     3958 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_04_model_run.py
--rw-r--r--   0 runner    (1001) docker     (123)     2336 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_05_model_run.py
--rw-r--r--   0 runner    (1001) docker     (123)     3131 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_06_model_run.py
--rw-r--r--   0 runner    (1001) docker     (123)     4036 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_07_model_run.py
--rw-r--r--   0 runner    (1001) docker     (123)     2218 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_08_model_pipe.py
--rw-r--r--   0 runner    (1001) docker     (123)     5657 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_09_model_pipe.py
--rw-r--r--   0 runner    (1001) docker     (123)     2485 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/data_binding_1.py
--rw-r--r--   0 runner    (1001) docker     (123)     2245 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/front_examples/make_pipelines.py
--rw-r--r--   0 runner    (1001) docker     (123)     2051 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/ipython_magic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.324491 plunk-0.1.98/plunk/tw/py2py_front_example/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/py2py_front_example/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/py2py_front_example/simple_front.py
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/py2py_front_example/simple_py2http_service.py
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/py2py_front_example/simple_pycode.py
--rw-r--r--   0 runner    (1001) docker     (123)      849 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/scrap.py
--rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/things_decorators_break.py
--rw-r--r--   0 runner    (1001) docker     (123)     3855 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/tw/user_story_to_poc_demo.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.328491 plunk-0.1.98/plunk/vf/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1242 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/decorators.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.328491 plunk-0.1.98/plunk/vf/extrude/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/extrude/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.328491 plunk-0.1.98/plunk/vf/extrude/crude/
--rw-r--r--   0 runner    (1001) docker     (123)      546 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/extrude/crude/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      218 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/extrude/crude/api.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/extrude/crude/web_app.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.328491 plunk-0.1.98/plunk/vf/extrude/edge_impulse_like/
--rw-r--r--   0 runner    (1001) docker     (123)      558 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/extrude/edge_impulse_like/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      696 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/extrude/edge_impulse_like/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     2986 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/extrude/edge_impulse_like/web_app.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.328491 plunk-0.1.98/plunk/vf/front/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/front/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7708 2023-01-04 17:46:46.000000 plunk-0.1.98/plunk/vf/front/store_explorer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 17:47:24.292490 plunk-0.1.98/plunk.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-01-04 17:47:24.000000 plunk-0.1.98/plunk.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    10585 2023-01-04 17:47:24.000000 plunk-0.1.98/plunk.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 17:47:24.000000 plunk-0.1.98/plunk.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 17:47:24.000000 plunk-0.1.98/plunk.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-04 17:47:24.000000 plunk-0.1.98/plunk.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      554 2023-01-04 17:47:24.332491 plunk-0.1.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-01-04 17:46:46.000000 plunk-0.1.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.436240 plunk-0.1.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-01-04 18:45:59.000000 plunk-0.1.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-01-04 18:46:28.436240 plunk-0.1.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-01-04 18:45:59.000000 plunk-0.1.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk/ap/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk/ap/audio_stream/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/audio_stream/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/audio_stream/audiostream_webservice.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk/ap/live_graph/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/live_graph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9386 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/live_graph/audio_store.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7915 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/live_graph/live_graph_data_buffer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5722 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/live_graph/live_graph_streamlitfront.py
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/snippets.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk/ap/store_explorer/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/store_explorer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2460 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/store_explorer/store_explorer_app.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4877 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/store_explorer/store_explorer_element.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1711 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/store_explorer/streamlit_store_explorer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1844 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ap/wav_encode.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk/ca/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/ca/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk/sb/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.420240 plunk-0.1.99/plunk/sb/click_detection/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/click_detection/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      958 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/click_detection/analysis.py
+-rw-r--r--   0 runner    (1001) docker     (123)      528 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/click_detection/clickified.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.420240 plunk-0.1.99/plunk/sb/front_demo/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10391 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/data_prep.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11363 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/data_prep_scores.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2389 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/data_viz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4027 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/learner_example.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5159 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/record_load_play.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10784 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/thor_dag_example.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.420240 plunk-0.1.99/plunk/sb/front_demo/user_story1/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.420240 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10114 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app0.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14648 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11621 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12025 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10209 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_5drill.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_6learner.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10192 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_7_funcnodes_exclude.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10208 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_drill.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2165 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_drill_Andie.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10994 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app5_drill.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13465 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app5_s3dol.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7798 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_base_audio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6244 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_choosing_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)      713 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_dummy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5947 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_scrap.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.420240 plunk-0.1.99/plunk/sb/front_demo/user_story1/components/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/components/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2287 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/components/components.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.420240 plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2421 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/funcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/simple_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5210 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.424240 plunk-0.1.99/plunk/sb/front_experiments/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      713 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/audio_app.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1542 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/audio_histo.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.424240 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.424240 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      829 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app0.py
+-rw-r--r--   0 runner    (1001) docker     (123)      635 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app0_5_folder_picker.py
+-rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app0_6_folder_picker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3148 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app1.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.424240 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/components/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/components/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1366 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/components/elements.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/components/folder_picker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.424240 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/dags/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/dags/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/dags/wf_store_splatter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      481 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/dags/wfstore_and_annots_to_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.424240 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/utils/tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8944 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/aggrid.py
+-rw-r--r--   0 runner    (1001) docker     (123)      218 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/barfi_app.py
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/chk_if_click.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/crudified_ag_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1156 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_app/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_app/Home.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_app/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5159 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_impulse_like_bytes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/elements.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/js/
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/js/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/kmeans_streamz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3805 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/learner_example.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/river_t.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1960 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4342 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1299 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap_crude.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap_dash.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1086 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap_sound_tagger.py
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrapsound.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2786 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_store_explorer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_store_explorer2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3124 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3251 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4938 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4681 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5150 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger5.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5168 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger6.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4416 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger7_with_tabs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3496 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger8_input_with_audio.py
+-rw-r--r--   0 runner    (1001) docker     (123)      911 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/stream_df.py
+-rw-r--r--   0 runner    (1001) docker     (123)      865 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/stream_live.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1260 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/stream_taped.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7332 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/tagging_tool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2474 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/tagging_tool_scrap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1017 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/edge_interface/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/get_stream.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1719 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/get_stream2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2008 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/get_stream3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1046 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlit_front_example.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1961 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/analysis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6664 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7630 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10389 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3496 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2547 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2263 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3708 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep5.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1909 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep6.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7137 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep7.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5963 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5242 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep9.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3324 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep_scrap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/tackle_args.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/meshed_experiments/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/meshed_experiments/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14785 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/meshed_experiments/meshed_kwargs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55011 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/meshed_experiments/scrap_dag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/meshed_experiments/scrap_dotdigraph.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/metaflow_practice/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/metaflow_practice/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/metaflow_practice/classify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2070 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/metaflow_practice/classify_phone.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/odat_lab/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/odat_lab/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/odat_lab/circuit_breaker.py
+-rw-r--r--   0 runner    (1001) docker     (123)      470 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/odat_lab/functional_dacc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1299 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/odat_lab/guns.py
+-rw-r--r--   0 runner    (1001) docker     (123)      396 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/odat_lab/hamlet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      459 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/odat_lab/heartbeat.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/ordering_funcnodes/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/ordering_funcnodes/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1352 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/ordering_funcnodes/reorder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.428240 plunk-0.1.99/plunk/sb/ordering_funcnodes/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/ordering_funcnodes/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/ordering_funcnodes/tests/test_reorder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/sb/pydantic_for_front/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/pydantic_for_front/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      812 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/pydantic_for_front/func_to_opyrator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/pydantic_for_front/opyrator_multiple_funcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      837 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/pydantic_for_front/pydantic_dispatch_enum.py
+-rw-r--r--   0 runner    (1001) docker     (123)      971 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/pydantic_for_front/pydantic_streamlit_front.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/pydantic_for_front/pydantic_streamlit_input.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3593 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/pydantic_for_front/tooltips_app.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/sb/sig_compatibility/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/sig_builtins.py
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/sig_code_to_dag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6769 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/sig_comp.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/sig_script.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/sb/sig_compatibility/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12393 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/tests/test_sig_builtins.py
+-rw-r--r--   0 runner    (1001) docker     (123)      312 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/tests/test_sig_code_to_dag.py
+-rw-r--r--   0 runner    (1001) docker     (123)      946 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/sig_compatibility/tests/test_sig_comp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/sb/slabsiter_experiments/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/slabsiter_experiments/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/slabsiter_experiments/dict_generators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1461 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/slabsiter_experiments/livewf_slabs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/sb/slabsiter_experiments/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/slabsiter_experiments/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      982 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/slabsiter_experiments/tests/test_dict_generators.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/sb/type_compatibility/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/type_compatibility/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2476 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/type_compatibility/compatible.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/sb/type_compatibility/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/type_compatibility/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1225 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/type_compatibility/tests/scrap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1161 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/sb/type_compatibility/tests/test_compatible.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/tw/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/echoed_clicks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1535 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/empty_sentinel_options.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/tw/front_examples/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/tw/front_examples/audio_ml/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/audio_ml/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/audio_ml/take01_simple_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12110 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/audio_ml/tw_app4_drill.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4233 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/audio_ml/tw_app4_drill_components.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.432240 plunk-0.1.99/plunk/tw/front_examples/crude_examples/
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4160 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/extrude_crude_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/pydantic_examples.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4296 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/scrap_streamlit.py
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_01_salary.py
+-rw-r--r--   0 runner    (1001) docker     (123)      947 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_02_salary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_03_salary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3958 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_04_model_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2336 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_05_model_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3131 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_06_model_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4036 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_07_model_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2218 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_08_model_pipe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5657 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_09_model_pipe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2485 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/data_binding_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2245 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/front_examples/make_pipelines.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2051 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/ipython_magic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.436240 plunk-0.1.99/plunk/tw/py2py_front_example/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/py2py_front_example/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/py2py_front_example/simple_front.py
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/py2py_front_example/simple_py2http_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)      267 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/py2py_front_example/simple_pycode.py
+-rw-r--r--   0 runner    (1001) docker     (123)      849 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/scrap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/things_decorators_break.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3855 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/tw/user_story_to_poc_demo.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.436240 plunk-0.1.99/plunk/vf/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1242 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/decorators.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.436240 plunk-0.1.99/plunk/vf/extrude/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/extrude/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.436240 plunk-0.1.99/plunk/vf/extrude/crude/
+-rw-r--r--   0 runner    (1001) docker     (123)      546 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/extrude/crude/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      218 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/extrude/crude/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/extrude/crude/web_app.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.436240 plunk-0.1.99/plunk/vf/extrude/edge_impulse_like/
+-rw-r--r--   0 runner    (1001) docker     (123)      558 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/extrude/edge_impulse_like/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      696 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/extrude/edge_impulse_like/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2986 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/extrude/edge_impulse_like/web_app.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.436240 plunk-0.1.99/plunk/vf/front/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/front/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7708 2023-01-04 18:45:59.000000 plunk-0.1.99/plunk/vf/front/store_explorer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 18:46:28.416240 plunk-0.1.99/plunk.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-01-04 18:46:28.000000 plunk-0.1.99/plunk.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    10585 2023-01-04 18:46:28.000000 plunk-0.1.99/plunk.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 18:46:28.000000 plunk-0.1.99/plunk.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 18:46:28.000000 plunk-0.1.99/plunk.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-04 18:46:28.000000 plunk-0.1.99/plunk.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      554 2023-01-04 18:46:28.436240 plunk-0.1.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-01-04 18:45:59.000000 plunk-0.1.99/setup.py
```

### Comparing `plunk-0.1.98/LICENSE` & `plunk-0.1.99/LICENSE`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/audio_stream/audiostream_webservice.py` & `plunk-0.1.99/plunk/ap/audio_stream/audiostream_webservice.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/live_graph/audio_store.py` & `plunk-0.1.99/plunk/ap/live_graph/audio_store.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/live_graph/live_graph_data_buffer.py` & `plunk-0.1.99/plunk/ap/live_graph/live_graph_data_buffer.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/live_graph/live_graph_streamlitfront.py` & `plunk-0.1.99/plunk/ap/live_graph/live_graph_streamlitfront.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/snippets.py` & `plunk-0.1.99/plunk/ap/snippets.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/store_explorer/store_explorer_app.py` & `plunk-0.1.99/plunk/ap/store_explorer/store_explorer_app.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/store_explorer/store_explorer_element.py` & `plunk-0.1.99/plunk/ap/store_explorer/store_explorer_element.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/store_explorer/streamlit_store_explorer.py` & `plunk-0.1.99/plunk/ap/store_explorer/streamlit_store_explorer.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/ap/wav_encode.py` & `plunk-0.1.99/plunk/ap/wav_encode.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/click_detection/analysis.py` & `plunk-0.1.99/plunk/sb/click_detection/analysis.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/click_detection/clickified.py` & `plunk-0.1.99/plunk/sb/click_detection/clickified.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/data_prep.py` & `plunk-0.1.99/plunk/sb/front_demo/data_prep.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/data_prep_scores.py` & `plunk-0.1.99/plunk/sb/front_demo/data_prep_scores.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/data_viz.py` & `plunk-0.1.99/plunk/sb/front_demo/data_viz.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/learner_example.py` & `plunk-0.1.99/plunk/sb/front_demo/learner_example.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/record_load_play.py` & `plunk-0.1.99/plunk/sb/front_demo/record_load_play.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/thor_dag_example.py` & `plunk-0.1.99/plunk/sb/front_demo/thor_dag_example.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app0.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app0.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app1.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app1.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app2.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app2.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app3.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app3.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_5drill.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_5drill.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_6learner.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_6learner.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_7_funcnodes_exclude.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_7_funcnodes_exclude.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_drill.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_drill.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app4_drill_Andie.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app4_drill_Andie.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app5_drill.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app5_drill.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app5_s3dol.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app5_s3dol.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_base_audio.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_base_audio.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_choosing_model.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_choosing_model.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_dummy.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_dummy.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/apps/app_scrap.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/apps/app_scrap.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/components/components.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/components/components.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/funcs.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/funcs.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/simple_config.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/simple_config.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_demo/user_story1/utils/tools.py` & `plunk-0.1.99/plunk/sb/front_demo/user_story1/utils/tools.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/audio_app.py` & `plunk-0.1.99/plunk/sb/front_experiments/audio_app.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/audio_histo.py` & `plunk-0.1.99/plunk/sb/front_experiments/audio_histo.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app0.py` & `plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app0.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app0_5_folder_picker.py` & `plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app0_5_folder_picker.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app0_6_folder_picker.py` & `plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app0_6_folder_picker.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/apps/app1.py` & `plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/apps/app1.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/components/elements.py` & `plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/components/elements.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/components/folder_picker.py` & `plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/components/folder_picker.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/data_visualizer/utils/tools.py` & `plunk-0.1.99/plunk/sb/front_experiments/data_visualizer/utils/tools.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/aggrid.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/aggrid.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/chk_if_click.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/chk_if_click.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/crudified_ag_table.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/crudified_ag_table.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_1.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_1.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_2.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_2.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_3.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_3.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/edge_impulse_like_bytes.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/edge_impulse_like_bytes.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/elements.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/elements.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/kmeans_streamz.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/kmeans_streamz.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/learner_example.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/learner_example.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/river_t.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/river_t.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap2.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap2.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap3.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap3.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap_crude.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap_crude.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap_dash.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap_dash.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/scrap_sound_tagger.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/scrap_sound_tagger.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_store_explorer.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_store_explorer.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_store_explorer2.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_store_explorer2.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger2.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger2.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger3.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger3.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger4.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger4.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger5.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger5.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger6.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger6.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger7_with_tabs.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger7_with_tabs.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/sound_tagger8_input_with_audio.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/sound_tagger8_input_with_audio.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/stream_df.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/stream_df.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/stream_live.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/stream_live.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/stream_taped.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/stream_taped.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/tagging_tool.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/tagging_tool.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/tagging_tool_scrap.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/tagging_tool_scrap.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/edge_interface/utils.py` & `plunk-0.1.99/plunk/sb/front_experiments/edge_interface/utils.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/get_stream.py` & `plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/get_stream.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/get_stream2.py` & `plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/get_stream2.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/sensor_stream/get_stream3.py` & `plunk-0.1.99/plunk/sb/front_experiments/sensor_stream/get_stream3.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlit_front_example.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlit_front_example.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/analysis.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/analysis.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep10.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep10.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep11.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep11.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep2.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep2.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep3.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep3.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep4.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep4.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep5.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep5.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep6.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep6.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep7.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep7.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep8.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep8.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep9.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep9.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep_scrap.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/data_prep_scrap.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/front_experiments/streamlitfront_dataprep/tackle_args.py` & `plunk-0.1.99/plunk/sb/front_experiments/streamlitfront_dataprep/tackle_args.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/meshed_experiments/meshed_kwargs.py` & `plunk-0.1.99/plunk/sb/meshed_experiments/meshed_kwargs.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/meshed_experiments/scrap_dag.py` & `plunk-0.1.99/plunk/sb/meshed_experiments/scrap_dag.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/meshed_experiments/scrap_dotdigraph.py` & `plunk-0.1.99/plunk/sb/meshed_experiments/scrap_dotdigraph.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/metaflow_practice/classify.py` & `plunk-0.1.99/plunk/sb/metaflow_practice/classify.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/metaflow_practice/classify_phone.py` & `plunk-0.1.99/plunk/sb/metaflow_practice/classify_phone.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/odat_lab/guns.py` & `plunk-0.1.99/plunk/sb/odat_lab/guns.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/ordering_funcnodes/reorder.py` & `plunk-0.1.99/plunk/sb/ordering_funcnodes/reorder.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/pydantic_for_front/func_to_opyrator.py` & `plunk-0.1.99/plunk/sb/pydantic_for_front/func_to_opyrator.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/pydantic_for_front/opyrator_multiple_funcs.py` & `plunk-0.1.99/plunk/sb/pydantic_for_front/opyrator_multiple_funcs.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/pydantic_for_front/pydantic_dispatch_enum.py` & `plunk-0.1.99/plunk/sb/pydantic_for_front/pydantic_dispatch_enum.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/pydantic_for_front/pydantic_streamlit_front.py` & `plunk-0.1.99/plunk/sb/pydantic_for_front/pydantic_streamlit_front.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/pydantic_for_front/pydantic_streamlit_input.py` & `plunk-0.1.99/plunk/sb/pydantic_for_front/pydantic_streamlit_input.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/pydantic_for_front/tooltips_app.py` & `plunk-0.1.99/plunk/sb/pydantic_for_front/tooltips_app.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/sig_compatibility/sig_builtins.py` & `plunk-0.1.99/plunk/sb/sig_compatibility/sig_builtins.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/sig_compatibility/sig_comp.py` & `plunk-0.1.99/plunk/sb/sig_compatibility/sig_comp.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/sig_compatibility/tests/test_sig_builtins.py` & `plunk-0.1.99/plunk/sb/sig_compatibility/tests/test_sig_builtins.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/sig_compatibility/tests/test_sig_comp.py` & `plunk-0.1.99/plunk/sb/sig_compatibility/tests/test_sig_comp.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/slabsiter_experiments/dict_generators.py` & `plunk-0.1.99/plunk/sb/slabsiter_experiments/dict_generators.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/slabsiter_experiments/livewf_slabs.py` & `plunk-0.1.99/plunk/sb/slabsiter_experiments/livewf_slabs.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/slabsiter_experiments/tests/test_dict_generators.py` & `plunk-0.1.99/plunk/sb/slabsiter_experiments/tests/test_dict_generators.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/type_compatibility/compatible.py` & `plunk-0.1.99/plunk/sb/type_compatibility/compatible.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/type_compatibility/tests/scrap.py` & `plunk-0.1.99/plunk/sb/type_compatibility/tests/scrap.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/sb/type_compatibility/tests/test_compatible.py` & `plunk-0.1.99/plunk/sb/type_compatibility/tests/test_compatible.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/echoed_clicks.py` & `plunk-0.1.99/plunk/tw/echoed_clicks.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/empty_sentinel_options.py` & `plunk-0.1.99/plunk/tw/empty_sentinel_options.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/audio_ml/take01_simple_pipeline.py` & `plunk-0.1.99/plunk/tw/front_examples/audio_ml/take01_simple_pipeline.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/audio_ml/tw_app4_drill.py` & `plunk-0.1.99/plunk/tw/front_examples/audio_ml/tw_app4_drill.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/audio_ml/tw_app4_drill_components.py` & `plunk-0.1.99/plunk/tw/front_examples/audio_ml/tw_app4_drill_components.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/extrude_crude_util.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/extrude_crude_util.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/pydantic_examples.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/pydantic_examples.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/scrap_streamlit.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/scrap_streamlit.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_01_salary.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_01_salary.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_02_salary.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_02_salary.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_03_salary.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_03_salary.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_04_model_run.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_04_model_run.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_05_model_run.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_05_model_run.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_06_model_run.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_06_model_run.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_07_model_run.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_07_model_run.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_08_model_pipe.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_08_model_pipe.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/crude_examples/take_09_model_pipe.py` & `plunk-0.1.99/plunk/tw/front_examples/crude_examples/take_09_model_pipe.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/data_binding_1.py` & `plunk-0.1.99/plunk/tw/front_examples/data_binding_1.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/front_examples/make_pipelines.py` & `plunk-0.1.99/plunk/tw/front_examples/make_pipelines.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/ipython_magic.py` & `plunk-0.1.99/plunk/tw/ipython_magic.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/py2py_front_example/simple_front.py` & `plunk-0.1.99/plunk/tw/py2py_front_example/simple_front.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/scrap.py` & `plunk-0.1.99/plunk/tw/scrap.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/things_decorators_break.py` & `plunk-0.1.99/plunk/tw/things_decorators_break.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/tw/user_story_to_poc_demo.py` & `plunk-0.1.99/plunk/tw/user_story_to_poc_demo.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/vf/decorators.py` & `plunk-0.1.99/plunk/vf/decorators.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/vf/extrude/crude/__init__.py` & `plunk-0.1.99/plunk/vf/extrude/crude/__init__.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/vf/extrude/edge_impulse_like/__init__.py` & `plunk-0.1.99/plunk/vf/extrude/edge_impulse_like/__init__.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/vf/extrude/edge_impulse_like/api.py` & `plunk-0.1.99/plunk/vf/extrude/edge_impulse_like/api.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/vf/extrude/edge_impulse_like/web_app.py` & `plunk-0.1.99/plunk/vf/extrude/edge_impulse_like/web_app.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk/vf/front/store_explorer.py` & `plunk-0.1.99/plunk/vf/front/store_explorer.py`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/plunk.egg-info/SOURCES.txt` & `plunk-0.1.99/plunk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `plunk-0.1.98/setup.cfg` & `plunk-0.1.99/setup.cfg`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = plunk
-version = 0.1.98
+version = 0.1.99
 url = https://github.com/otosense/plunk
 platforms = any
 description_file = README.md
 root_url = https://github.com/otosense/
 license = apache-2.0
 author = OtoSense
 description = Dump of disorganized ML tools -- the place where homeless code goes until a home is found
```

