# Comparing `tmp/supervisely-6.9.1.tar.gz` & `tmp/supervisely-6.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "supervisely-6.9.1.tar", last modified: Thu Mar 24 17:26:38 2022, max compression
+gzip compressed data, was "supervisely-6.9.2.tar", last modified: Fri Mar 25 09:11:16 2022, max compression
```

## Comparing `supervisely-6.9.1.tar` & `supervisely-6.9.2.tar`

### file list

```diff
@@ -1,310 +1,310 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.874120 supervisely-6.9.1/
--rw-r--r--   0 runner    (1001) docker     (121)     7187 2022-03-24 17:26:38.874120 supervisely-6.9.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     6838 2022-03-24 17:26:21.000000 supervisely-6.9.1/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      119 2022-03-24 17:26:21.000000 supervisely-6.9.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-24 17:26:38.874120 supervisely-6.9.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2204 2022-03-24 17:26:21.000000 supervisely-6.9.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.846119 supervisely-6.9.1/supervisely/
--rw-r--r--   0 runner    (1001) docker     (121)     5317 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3175 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.850119 supervisely-6.9.1/supervisely/annotation/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    31239 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/annotation.py
--rw-r--r--   0 runner    (1001) docker     (121)     8111 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/annotation_transforms.py
--rw-r--r--   0 runner    (1001) docker     (121)     1126 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/json_geometries_map.py
--rw-r--r--   0 runner    (1001) docker     (121)    12340 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/label.py
--rw-r--r--   0 runner    (1001) docker     (121)     6500 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/obj_class.py
--rw-r--r--   0 runner    (1001) docker     (121)     2593 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/obj_class_collection.py
--rw-r--r--   0 runner    (1001) docker     (121)      903 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/obj_class_mapper.py
--rw-r--r--   0 runner    (1001) docker     (121)     1904 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/renamer.py
--rw-r--r--   0 runner    (1001) docker     (121)     5689 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/tag.py
--rw-r--r--   0 runner    (1001) docker     (121)     1382 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/tag_collection.py
--rw-r--r--   0 runner    (1001) docker     (121)    10193 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/tag_meta.py
--rw-r--r--   0 runner    (1001) docker     (121)     2179 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/tag_meta_collection.py
--rw-r--r--   0 runner    (1001) docker     (121)     1597 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/annotation/tag_meta_mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.854119 supervisely-6.9.1/supervisely/api/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1118 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/advanced_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1683 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/agent_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     6982 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/annotation_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    12240 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/api.py
--rw-r--r--   0 runner    (1001) docker     (121)     3979 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/app_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     6920 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/dataset_api.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.854119 supervisely-6.9.1/supervisely/api/entity_annotation/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/entity_annotation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2307 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/entity_annotation/entity_annotation_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     2974 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/entity_annotation/figure_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     2071 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/entity_annotation/object_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     3944 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/entity_annotation/tag_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    10046 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/file_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      488 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/github_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     2424 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/image_annotation_tool_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    29242 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/image_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      436 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/import_storage_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    11435 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/labeling_job_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    17324 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/module_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     7156 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/neural_network_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     2708 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/object_class_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1257 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/plugin_api.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.854119 supervisely-6.9.1/supervisely/api/pointcloud/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1607 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_annotation_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     8363 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1762 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_episode_annotation_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      906 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_episode_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1332 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_figure_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      935 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_object_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      255 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_tag_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    10124 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/project_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      889 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/project_class_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1713 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/remote_storage_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     4363 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/report_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      782 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/role_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    17621 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/task_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     6788 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/team_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     7738 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/user_api.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.854119 supervisely-6.9.1/supervisely/api/video/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/video/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1721 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/video/video_annotation_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    17073 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/video/video_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      929 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/video/video_figure_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1423 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/video/video_frame_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      540 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/video/video_object_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1521 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/video/video_tag_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1929 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/api/workspace_api.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.854119 supervisely-6.9.1/supervisely/app/
--rw-r--r--   0 runner    (1001) docker     (121)      189 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3051 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/content.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.854119 supervisely-6.9.1/supervisely/app/fastapi/
--rw-r--r--   0 runner    (1001) docker     (121)      241 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/fastapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3804 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/fastapi/subapp.py
--rw-r--r--   0 runner    (1001) docker     (121)     1421 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/fastapi/templating.py
--rw-r--r--   0 runner    (1001) docker     (121)     1315 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/fastapi/websocket.py
--rw-r--r--   0 runner    (1001) docker     (121)      341 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/jinja2.py
--rw-r--r--   0 runner    (1001) docker     (121)      406 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/singleton.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.854119 supervisely-6.9.1/supervisely/app/v1/
--rw-r--r--   0 runner    (1001) docker     (121)      900 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19860 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/app_service.py
--rw-r--r--   0 runner    (1001) docker     (121)      183 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)     2867 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/sly-icon-example.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/app/v1/widgets/
--rw-r--r--   0 runner    (1001) docker     (121)      290 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2469 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/chart.py
--rw-r--r--   0 runner    (1001) docker     (121)     3622 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/compare_gallery.py
--rw-r--r--   0 runner    (1001) docker     (121)      441 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/empty_grid_gallery.py
--rw-r--r--   0 runner    (1001) docker     (121)     6885 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/grid_gallery.py
--rw-r--r--   0 runner    (1001) docker     (121)     8079 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/predictions_dynamics_gallery.py
--rw-r--r--   0 runner    (1001) docker     (121)     3184 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/progress_bar.py
--rw-r--r--   0 runner    (1001) docker     (121)     2958 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/v1/widgets/single_image_gallery.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/app/widgets/
--rw-r--r--   0 runner    (1001) docker     (121)      414 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/app/widgets/done_label/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/done_label/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      424 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/done_label/done_label.py
--rw-r--r--   0 runner    (1001) docker     (121)      179 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/done_label/template.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/app/widgets/notification_box/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/notification_box/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1700 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/notification_box/notification_box.py
--rw-r--r--   0 runner    (1001) docker     (121)      461 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/notification_box/style.css
--rw-r--r--   0 runner    (1001) docker     (121)      523 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/notification_box/template.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/app/widgets/radio_table/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/radio_table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/radio_table/radio_table.py
--rw-r--r--   0 runner    (1001) docker     (121)      255 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/radio_table/style.css
--rw-r--r--   0 runner    (1001) docker     (121)     1356 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/radio_table/template.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/app/widgets/sly_tqdm/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/sly_tqdm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4792 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/sly_tqdm/sly_tqdm.py
--rw-r--r--   0 runner    (1001) docker     (121)      396 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/sly_tqdm/style.css
--rw-r--r--   0 runner    (1001) docker     (121)     1266 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/sly_tqdm/template.html
--rw-r--r--   0 runner    (1001) docker     (121)     2149 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/app/widgets/widget.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/aug/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/aug/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13643 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/aug/aug.py
--rw-r--r--   0 runner    (1001) docker     (121)     6511 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/aug/imgaug_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/collection/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/collection/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10815 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/collection/key_indexed_collection.py
--rw-r--r--   0 runner    (1001) docker     (121)     1250 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/collection/str_enum.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/decorators/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/decorators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4708 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/decorators/inference.py
--rw-r--r--   0 runner    (1001) docker     (121)     1227 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/decorators/profile.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/delme_fastapi_helpers/
--rw-r--r--   0 runner    (1001) docker     (121)      237 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/delme_fastapi_helpers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.858119 supervisely-6.9.1/supervisely/export/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/export/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3164 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/export/pascal_voc.py
--rw-r--r--   0 runner    (1001) docker     (121)     1664 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/function_wrapper.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.862120 supervisely-6.9.1/supervisely/geometry/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      303 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/any_geometry.py
--rw-r--r--   0 runner    (1001) docker     (121)    10800 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/bitmap.py
--rw-r--r--   0 runner    (1001) docker     (121)     7949 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/bitmap_base.py
--rw-r--r--   0 runner    (1001) docker     (121)      678 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)     1122 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/conversions.py
--rw-r--r--   0 runner    (1001) docker     (121)     8585 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/cuboid.py
--rw-r--r--   0 runner    (1001) docker     (121)     3976 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/cuboid_3d.py
--rw-r--r--   0 runner    (1001) docker     (121)     7015 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/geometry.py
--rw-r--r--   0 runner    (1001) docker     (121)    11820 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/graph.py
--rw-r--r--   0 runner    (1001) docker     (121)     3749 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/helpers.py
--rw-r--r--   0 runner    (1001) docker     (121)     5199 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/image_rotator.py
--rw-r--r--   0 runner    (1001) docker     (121)    27151 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/main_tests.py
--rw-r--r--   0 runner    (1001) docker     (121)     4832 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/multichannel_bitmap.py
--rw-r--r--   0 runner    (1001) docker     (121)     6023 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/point.py
--rw-r--r--   0 runner    (1001) docker     (121)     1508 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/point_3d.py
--rw-r--r--   0 runner    (1001) docker     (121)     5692 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/point_location.py
--rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/pointcloud.py
--rw-r--r--   0 runner    (1001) docker     (121)     7650 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/polygon.py
--rw-r--r--   0 runner    (1001) docker     (121)     4797 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/polyline.py
--rw-r--r--   0 runner    (1001) docker     (121)    10938 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/rectangle.py
--rw-r--r--   0 runner    (1001) docker     (121)     1660 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/sliding_windows.py
--rw-r--r--   0 runner    (1001) docker     (121)     3101 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/sliding_windows_fuzzy.py
--rw-r--r--   0 runner    (1001) docker     (121)     2099 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/validation.py
--rw-r--r--   0 runner    (1001) docker     (121)     6437 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/geometry/vector_geometry.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.862120 supervisely-6.9.1/supervisely/imaging/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/imaging/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1339 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/imaging/_video.py
--rw-r--r--   0 runner    (1001) docker     (121)     3796 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/imaging/color.py
--rw-r--r--   0 runner    (1001) docker     (121)     2397 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/imaging/font.py
--rw-r--r--   0 runner    (1001) docker     (121)    24894 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/imaging/image.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.862120 supervisely-6.9.1/supervisely/io/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4797 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/docker_utils.py
--rw-r--r--   0 runner    (1001) docker     (121)      424 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/env.py
--rw-r--r--   0 runner    (1001) docker     (121)     9565 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/fs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5784 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/fs_cache.py
--rw-r--r--   0 runner    (1001) docker     (121)     1750 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/github_utils.py
--rw-r--r--   0 runner    (1001) docker     (121)     1392 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/json.py
--rw-r--r--   0 runner    (1001) docker     (121)    14417 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/multipart_stream_decoder.py
--rw-r--r--   0 runner    (1001) docker     (121)     3911 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/io/network_exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.862120 supervisely-6.9.1/supervisely/labeling_jobs/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/labeling_jobs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      104 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/labeling_jobs/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)    12894 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/labeling_jobs/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/metric/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5005 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/classification_metrics.py
--rw-r--r--   0 runner    (1001) docker     (121)     2526 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/common.py
--rw-r--r--   0 runner    (1001) docker     (121)     3242 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/confusion_matrix_metric.py
--rw-r--r--   0 runner    (1001) docker     (121)     3233 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/iou_metric.py
--rw-r--r--   0 runner    (1001) docker     (121)     6158 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/map_metric.py
--rw-r--r--   0 runner    (1001) docker     (121)     3778 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/matching.py
--rw-r--r--   0 runner    (1001) docker     (121)      319 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/metric_base.py
--rw-r--r--   0 runner    (1001) docker     (121)     4438 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/metrics_tests.py
--rw-r--r--   0 runner    (1001) docker     (121)     3273 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/pixel_accuracy.py
--rw-r--r--   0 runner    (1001) docker     (121)     3426 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/precision_recall_metric.py
--rw-r--r--   0 runner    (1001) docker     (121)     3415 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/metric/projects_applier.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/nn/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2994 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/config.py
--rw-r--r--   0 runner    (1001) docker     (121)     6055 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/nn/hosted/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6802 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/class_indexing.py
--rw-r--r--   0 runner    (1001) docker     (121)      132 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)     1890 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/deploy.py
--rw-r--r--   0 runner    (1001) docker     (121)     3700 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/inference_batch.py
--rw-r--r--   0 runner    (1001) docker     (121)     7055 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/inference_batch_multiprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)    28735 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/inference_modes.py
--rw-r--r--   0 runner    (1001) docker     (121)     4440 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/inference_single_image.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/nn/hosted/legacy/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/legacy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1262 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/legacy/inference_config.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/nn/hosted/pytorch/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/pytorch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       70 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/pytorch/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)     3951 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/pytorch/inference_applier.py
--rw-r--r--   0 runner    (1001) docker     (121)    13676 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/pytorch/trainer.py
--rw-r--r--   0 runner    (1001) docker     (121)     7284 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/hosted/trainer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/nn/inference/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/inference/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1720 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/inference/rest_client.py
--rw-r--r--   0 runner    (1001) docker     (121)      300 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/inference/rest_constants.py
--rw-r--r--   0 runner    (1001) docker     (121)     3942 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/inference/rest_server.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/nn/pytorch/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/pytorch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      599 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/pytorch/cuda.py
--rw-r--r--   0 runner    (1001) docker     (121)     1044 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/pytorch/dataset.py
--rw-r--r--   0 runner    (1001) docker     (121)     1106 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/pytorch/inference.py
--rw-r--r--   0 runner    (1001) docker     (121)     1077 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/pytorch/metrics.py
--rw-r--r--   0 runner    (1001) docker     (121)     3354 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/pytorch/weights.py
--rw-r--r--   0 runner    (1001) docker     (121)     3789 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/raw_to_labels.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/nn/training/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/training/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1311 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/nn/training/eval_planner.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/pointcloud/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1194 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud/pointcloud.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.866119 supervisely-6.9.1/supervisely/pointcloud_annotation/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud_annotation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      346 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud_annotation/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)     4762 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_annotation.py
--rw-r--r--   0 runner    (1001) docker     (121)     3552 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_episode_annotation.py
--rw-r--r--   0 runner    (1001) docker     (121)     1141 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_figure.py
--rw-r--r--   0 runner    (1001) docker     (121)     2775 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_object.py
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_object_collection.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/project/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/project/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11261 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/project/pointcloud_episode_project.py
--rw-r--r--   0 runner    (1001) docker     (121)     9342 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/project/pointcloud_project.py
--rw-r--r--   0 runner    (1001) docker     (121)    48637 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/project/project.py
--rw-r--r--   0 runner    (1001) docker     (121)    12619 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/project/project_meta.py
--rw-r--r--   0 runner    (1001) docker     (121)      251 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/project/project_type.py
--rw-r--r--   0 runner    (1001) docker     (121)    10388 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/project/video_project.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/pyscripts_utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pyscripts_utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      314 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/pyscripts_utils/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/report/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/report/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1870 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/report/table.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/script/
--rw-r--r--   0 runner    (1001) docker     (121)       20 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/script/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       54 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/script/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)     6220 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/sly_logger.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/task/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/task/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1197 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/task/paths.py
--rw-r--r--   0 runner    (1001) docker     (121)     6834 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/task/progress.py
--rw-r--r--   0 runner    (1001) docker     (121)     3531 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/task/task_logger.py
--rw-r--r--   0 runner    (1001) docker     (121)      183 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/tiny_timer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/user/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/user/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      319 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/user/user.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/video/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      218 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video/get_video_info.sh
--rw-r--r--   0 runner    (1001) docker     (121)      544 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video/import_utils.py
--rw-r--r--   0 runner    (1001) docker     (121)     7502 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video/video.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/video_annotation/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      529 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)     2972 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/frame.py
--rw-r--r--   0 runner    (1001) docker     (121)     2095 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/frame_collection.py
--rw-r--r--   0 runner    (1001) docker     (121)     9143 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/key_id_map.py
--rw-r--r--   0 runner    (1001) docker     (121)     6446 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/video_annotation.py
--rw-r--r--   0 runner    (1001) docker     (121)     7918 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/video_figure.py
--rw-r--r--   0 runner    (1001) docker     (121)     5486 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/video_object.py
--rw-r--r--   0 runner    (1001) docker     (121)     1274 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/video_object_collection.py
--rw-r--r--   0 runner    (1001) docker     (121)     5826 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/video_tag.py
--rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/video_annotation/video_tag_collection.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.870119 supervisely-6.9.1/supervisely/worker_api/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7829 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_api/agent_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     2202 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_api/agent_rpc.py
--rw-r--r--   0 runner    (1001) docker     (121)     2739 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_api/chunking.py
--rw-r--r--   0 runner    (1001) docker     (121)      191 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_api/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (121)     4903 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_api/retriers.py
--rw-r--r--   0 runner    (1001) docker     (121)    11751 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_api/rpc_servicer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.874120 supervisely-6.9.1/supervisely/worker_proto/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_proto/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    59142 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_proto/worker_api_pb2.py
--rw-r--r--   0 runner    (1001) docker     (121)    28940 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely/worker_proto/worker_api_pb2_grpc.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.850119 supervisely-6.9.1/supervisely.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     7187 2022-03-24 17:26:38.000000 supervisely-6.9.1/supervisely.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     9788 2022-03-24 17:26:38.000000 supervisely-6.9.1/supervisely.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-24 17:26:38.000000 supervisely-6.9.1/supervisely.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      707 2022-03-24 17:26:38.000000 supervisely-6.9.1/supervisely.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       28 2022-03-24 17:26:38.000000 supervisely-6.9.1/supervisely.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 17:26:38.874120 supervisely-6.9.1/supervisely_lib/
--rw-r--r--   0 runner    (1001) docker     (121)      159 2022-03-24 17:26:21.000000 supervisely-6.9.1/supervisely_lib/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.147607 supervisely-6.9.2/
+-rw-r--r--   0 runner    (1001) docker     (121)     7187 2022-03-25 09:11:16.147607 supervisely-6.9.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     6838 2022-03-25 09:10:58.000000 supervisely-6.9.2/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      119 2022-03-25 09:10:59.000000 supervisely-6.9.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-25 09:11:16.147607 supervisely-6.9.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2204 2022-03-25 09:10:59.000000 supervisely-6.9.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.119609 supervisely-6.9.2/supervisely/
+-rw-r--r--   0 runner    (1001) docker     (121)     5317 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3175 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.123609 supervisely-6.9.2/supervisely/annotation/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31239 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/annotation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8111 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/annotation_transforms.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1126 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/json_geometries_map.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12340 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/label.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6500 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/obj_class.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2593 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/obj_class_collection.py
+-rw-r--r--   0 runner    (1001) docker     (121)      903 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/obj_class_mapper.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1904 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/renamer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5689 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/tag.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1382 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/tag_collection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10193 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/tag_meta.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2179 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/tag_meta_collection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1597 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/annotation/tag_meta_mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.123609 supervisely-6.9.2/supervisely/api/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1118 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/advanced_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1683 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/agent_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6982 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/annotation_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12240 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3979 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/app_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6920 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/dataset_api.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/api/entity_annotation/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/entity_annotation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2307 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/entity_annotation/entity_annotation_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2974 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/entity_annotation/figure_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2071 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/entity_annotation/object_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3944 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/entity_annotation/tag_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10046 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/file_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      488 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/github_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2424 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/image_annotation_tool_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29242 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/image_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      436 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/import_storage_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11435 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/labeling_job_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17324 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/module_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7156 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/neural_network_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2708 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/object_class_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1257 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/plugin_api.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/api/pointcloud/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1607 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_annotation_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8363 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1762 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_episode_annotation_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      906 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_episode_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1332 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_figure_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      935 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_object_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      255 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_tag_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10124 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/project_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      889 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/project_class_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1713 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/remote_storage_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4363 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/report_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      782 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/role_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17621 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/task_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6788 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/team_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7738 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/user_api.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/api/video/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/video/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1721 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/video/video_annotation_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17073 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/video/video_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      929 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/video/video_figure_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1423 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/video/video_frame_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      540 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/video/video_object_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1521 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/video/video_tag_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1929 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/api/workspace_api.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/app/
+-rw-r--r--   0 runner    (1001) docker     (121)      189 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3051 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/content.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/app/fastapi/
+-rw-r--r--   0 runner    (1001) docker     (121)      241 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/fastapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3804 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/fastapi/subapp.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1421 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/fastapi/templating.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1315 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/fastapi/websocket.py
+-rw-r--r--   0 runner    (1001) docker     (121)      341 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/jinja2.py
+-rw-r--r--   0 runner    (1001) docker     (121)      406 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/singleton.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/app/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)      900 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19860 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/app_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)      183 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2867 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/sly-icon-example.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/app/v1/widgets/
+-rw-r--r--   0 runner    (1001) docker     (121)      290 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2469 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/chart.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3622 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/compare_gallery.py
+-rw-r--r--   0 runner    (1001) docker     (121)      441 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/empty_grid_gallery.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6885 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/grid_gallery.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8079 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/predictions_dynamics_gallery.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3184 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/progress_bar.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2958 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/v1/widgets/single_image_gallery.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.127608 supervisely-6.9.2/supervisely/app/widgets/
+-rw-r--r--   0 runner    (1001) docker     (121)      414 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/app/widgets/done_label/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/done_label/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/done_label/done_label.py
+-rw-r--r--   0 runner    (1001) docker     (121)      179 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/done_label/template.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/app/widgets/notification_box/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/notification_box/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1700 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/notification_box/notification_box.py
+-rw-r--r--   0 runner    (1001) docker     (121)      461 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/notification_box/style.css
+-rw-r--r--   0 runner    (1001) docker     (121)      524 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/notification_box/template.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/app/widgets/radio_table/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/radio_table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/radio_table/radio_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)      255 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/radio_table/style.css
+-rw-r--r--   0 runner    (1001) docker     (121)     1357 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/radio_table/template.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/app/widgets/sly_tqdm/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/sly_tqdm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4792 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/sly_tqdm/sly_tqdm.py
+-rw-r--r--   0 runner    (1001) docker     (121)      396 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/sly_tqdm/style.css
+-rw-r--r--   0 runner    (1001) docker     (121)     1267 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/sly_tqdm/template.html
+-rw-r--r--   0 runner    (1001) docker     (121)     2149 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/app/widgets/widget.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/aug/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/aug/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13643 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/aug/aug.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6511 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/aug/imgaug_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/collection/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/collection/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10815 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/collection/key_indexed_collection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1250 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/collection/str_enum.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/decorators/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/decorators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4708 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/decorators/inference.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1227 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/decorators/profile.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/delme_fastapi_helpers/
+-rw-r--r--   0 runner    (1001) docker     (121)      237 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/delme_fastapi_helpers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.131608 supervisely-6.9.2/supervisely/export/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/export/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3164 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/export/pascal_voc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1664 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/function_wrapper.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.135608 supervisely-6.9.2/supervisely/geometry/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      303 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/any_geometry.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10800 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/bitmap.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7949 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/bitmap_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)      678 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1122 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/conversions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8585 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/cuboid.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3976 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/cuboid_3d.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7015 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/geometry.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11820 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/graph.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3749 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5199 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/image_rotator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27151 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/main_tests.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4832 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/multichannel_bitmap.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6023 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/point.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1508 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/point_3d.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5692 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/point_location.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/pointcloud.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7650 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/polygon.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4797 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/polyline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10938 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/rectangle.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1660 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/sliding_windows.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3101 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/sliding_windows_fuzzy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2099 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/validation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6437 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/geometry/vector_geometry.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.135608 supervisely-6.9.2/supervisely/imaging/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/imaging/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1339 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/imaging/_video.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3796 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/imaging/color.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2397 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/imaging/font.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24894 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/imaging/image.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.135608 supervisely-6.9.2/supervisely/io/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4797 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/docker_utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/env.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9565 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/fs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5784 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/fs_cache.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1750 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/github_utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1392 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/json.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14417 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/multipart_stream_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3911 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/io/network_exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.135608 supervisely-6.9.2/supervisely/labeling_jobs/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/labeling_jobs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      104 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/labeling_jobs/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12894 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/labeling_jobs/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.135608 supervisely-6.9.2/supervisely/metric/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5005 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/classification_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2526 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/common.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3242 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/confusion_matrix_metric.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3233 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/iou_metric.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6158 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/map_metric.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3778 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/matching.py
+-rw-r--r--   0 runner    (1001) docker     (121)      319 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/metric_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4438 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/metrics_tests.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3273 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/pixel_accuracy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3426 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/precision_recall_metric.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3415 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/metric/projects_applier.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/nn/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2994 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6055 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/nn/hosted/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6802 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/class_indexing.py
+-rw-r--r--   0 runner    (1001) docker     (121)      132 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1890 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/deploy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3700 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/inference_batch.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7055 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/inference_batch_multiprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28735 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/inference_modes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4440 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/inference_single_image.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/nn/hosted/legacy/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/legacy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1262 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/legacy/inference_config.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/nn/hosted/pytorch/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/pytorch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       70 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/pytorch/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3951 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/pytorch/inference_applier.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13676 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/pytorch/trainer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7284 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/hosted/trainer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/nn/inference/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/inference/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1720 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/inference/rest_client.py
+-rw-r--r--   0 runner    (1001) docker     (121)      300 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/inference/rest_constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3942 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/inference/rest_server.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/nn/pytorch/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/pytorch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      599 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/pytorch/cuda.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1044 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/pytorch/dataset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1106 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/pytorch/inference.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1077 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/pytorch/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3354 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/pytorch/weights.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3789 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/raw_to_labels.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/nn/training/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/training/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1311 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/nn/training/eval_planner.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/pointcloud/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1194 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud/pointcloud.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.139608 supervisely-6.9.2/supervisely/pointcloud_annotation/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud_annotation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud_annotation/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4762 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_annotation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3552 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_episode_annotation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1141 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_figure.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2775 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_object.py
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_object_collection.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/project/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/project/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11261 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/project/pointcloud_episode_project.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9342 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/project/pointcloud_project.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48637 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/project/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12619 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/project/project_meta.py
+-rw-r--r--   0 runner    (1001) docker     (121)      251 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/project/project_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10388 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/project/video_project.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/pyscripts_utils/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pyscripts_utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      314 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/pyscripts_utils/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/report/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/report/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1870 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/report/table.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/script/
+-rw-r--r--   0 runner    (1001) docker     (121)       20 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/script/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       54 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/script/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6220 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/sly_logger.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/task/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/task/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1197 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/task/paths.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6834 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/task/progress.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3531 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/task/task_logger.py
+-rw-r--r--   0 runner    (1001) docker     (121)      183 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/tiny_timer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/user/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/user/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      319 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/user/user.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/video/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      218 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video/get_video_info.sh
+-rw-r--r--   0 runner    (1001) docker     (121)      544 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video/import_utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7502 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video/video.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/video_annotation/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      529 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2972 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/frame.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2095 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/frame_collection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9143 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/key_id_map.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6446 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/video_annotation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7918 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/video_figure.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5486 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/video_object.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1274 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/video_object_collection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5826 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/video_tag.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/video_annotation/video_tag_collection.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/worker_api/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7829 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_api/agent_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2202 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_api/agent_rpc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2739 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_api/chunking.py
+-rw-r--r--   0 runner    (1001) docker     (121)      191 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_api/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4903 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_api/retriers.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11751 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_api/rpc_servicer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely/worker_proto/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_proto/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59142 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_proto/worker_api_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28940 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely/worker_proto/worker_api_pb2_grpc.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.119609 supervisely-6.9.2/supervisely.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     7187 2022-03-25 09:11:15.000000 supervisely-6.9.2/supervisely.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     9788 2022-03-25 09:11:16.000000 supervisely-6.9.2/supervisely.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-25 09:11:15.000000 supervisely-6.9.2/supervisely.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      707 2022-03-25 09:11:15.000000 supervisely-6.9.2/supervisely.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       28 2022-03-25 09:11:16.000000 supervisely-6.9.2/supervisely.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 09:11:16.143607 supervisely-6.9.2/supervisely_lib/
+-rw-r--r--   0 runner    (1001) docker     (121)      159 2022-03-25 09:10:59.000000 supervisely-6.9.2/supervisely_lib/__init__.py
```

### Comparing `supervisely-6.9.1/PKG-INFO` & `supervisely-6.9.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: supervisely
-Version: 6.9.1
+Version: 6.9.2
 Summary: Supervisely Python SDK.
 Home-page: https://github.com/supervisely/supervisely
 License: UNKNOWN
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
 Provides-Extra: extras
 Provides-Extra: apps
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: supervisely Version: 6.9.1 Summary: Supervisely
+Metadata-Version: 2.1 Name: supervisely Version: 6.9.2 Summary: Supervisely
 Python SDK. Home-page: https://github.com/supervisely/supervisely License:
 UNKNOWN Platform: UNKNOWN Description-Content-Type: text/markdown Provides-
 Extra: extras Provides-Extra: apps Provides-Extra: sdk-no-usages Provides-
 Extra: plugins Provides-Extra: sdk-nn-plugins
                                     ******
                                 [Supervisely]
                                  Supervisely
```

### Comparing `supervisely-6.9.1/README.md` & `supervisely-6.9.2/README.md`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/setup.py` & `supervisely-6.9.2/setup.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/__init__.py` & `supervisely-6.9.2/supervisely/__init__.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/_utils.py` & `supervisely-6.9.2/supervisely/_utils.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/annotation.py` & `supervisely-6.9.2/supervisely/annotation/annotation.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/annotation_transforms.py` & `supervisely-6.9.2/supervisely/annotation/annotation_transforms.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/json_geometries_map.py` & `supervisely-6.9.2/supervisely/annotation/json_geometries_map.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/label.py` & `supervisely-6.9.2/supervisely/annotation/label.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/obj_class.py` & `supervisely-6.9.2/supervisely/annotation/obj_class.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/obj_class_collection.py` & `supervisely-6.9.2/supervisely/annotation/obj_class_collection.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/obj_class_mapper.py` & `supervisely-6.9.2/supervisely/annotation/obj_class_mapper.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/renamer.py` & `supervisely-6.9.2/supervisely/annotation/renamer.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/tag.py` & `supervisely-6.9.2/supervisely/annotation/tag.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/tag_collection.py` & `supervisely-6.9.2/supervisely/annotation/tag_collection.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/tag_meta.py` & `supervisely-6.9.2/supervisely/annotation/tag_meta.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/tag_meta_collection.py` & `supervisely-6.9.2/supervisely/annotation/tag_meta_collection.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/annotation/tag_meta_mapper.py` & `supervisely-6.9.2/supervisely/annotation/tag_meta_mapper.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/advanced_api.py` & `supervisely-6.9.2/supervisely/api/advanced_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/agent_api.py` & `supervisely-6.9.2/supervisely/api/agent_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/annotation_api.py` & `supervisely-6.9.2/supervisely/api/annotation_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/api.py` & `supervisely-6.9.2/supervisely/api/api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/app_api.py` & `supervisely-6.9.2/supervisely/api/app_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/dataset_api.py` & `supervisely-6.9.2/supervisely/api/dataset_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/entity_annotation/entity_annotation_api.py` & `supervisely-6.9.2/supervisely/api/entity_annotation/entity_annotation_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/entity_annotation/figure_api.py` & `supervisely-6.9.2/supervisely/api/entity_annotation/figure_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/entity_annotation/object_api.py` & `supervisely-6.9.2/supervisely/api/entity_annotation/object_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/entity_annotation/tag_api.py` & `supervisely-6.9.2/supervisely/api/entity_annotation/tag_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/file_api.py` & `supervisely-6.9.2/supervisely/api/file_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/image_annotation_tool_api.py` & `supervisely-6.9.2/supervisely/api/image_annotation_tool_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/image_api.py` & `supervisely-6.9.2/supervisely/api/image_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/labeling_job_api.py` & `supervisely-6.9.2/supervisely/api/labeling_job_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/module_api.py` & `supervisely-6.9.2/supervisely/api/module_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/neural_network_api.py` & `supervisely-6.9.2/supervisely/api/neural_network_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/object_class_api.py` & `supervisely-6.9.2/supervisely/api/object_class_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/plugin_api.py` & `supervisely-6.9.2/supervisely/api/plugin_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_annotation_api.py` & `supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_annotation_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_api.py` & `supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_episode_annotation_api.py` & `supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_episode_annotation_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_episode_api.py` & `supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_episode_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_figure_api.py` & `supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_figure_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/pointcloud/pointcloud_object_api.py` & `supervisely-6.9.2/supervisely/api/pointcloud/pointcloud_object_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/project_api.py` & `supervisely-6.9.2/supervisely/api/project_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/project_class_api.py` & `supervisely-6.9.2/supervisely/api/project_class_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/remote_storage_api.py` & `supervisely-6.9.2/supervisely/api/remote_storage_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/report_api.py` & `supervisely-6.9.2/supervisely/api/report_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/role_api.py` & `supervisely-6.9.2/supervisely/api/role_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/task_api.py` & `supervisely-6.9.2/supervisely/api/task_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/team_api.py` & `supervisely-6.9.2/supervisely/api/team_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/user_api.py` & `supervisely-6.9.2/supervisely/api/user_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/video/video_annotation_api.py` & `supervisely-6.9.2/supervisely/api/video/video_annotation_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/video/video_api.py` & `supervisely-6.9.2/supervisely/api/video/video_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/video/video_figure_api.py` & `supervisely-6.9.2/supervisely/api/video/video_figure_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/video/video_frame_api.py` & `supervisely-6.9.2/supervisely/api/video/video_frame_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/video/video_object_api.py` & `supervisely-6.9.2/supervisely/api/video/video_object_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/video/video_tag_api.py` & `supervisely-6.9.2/supervisely/api/video/video_tag_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/api/workspace_api.py` & `supervisely-6.9.2/supervisely/api/workspace_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/content.py` & `supervisely-6.9.2/supervisely/app/content.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/fastapi/subapp.py` & `supervisely-6.9.2/supervisely/app/fastapi/subapp.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/fastapi/templating.py` & `supervisely-6.9.2/supervisely/app/fastapi/templating.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/fastapi/websocket.py` & `supervisely-6.9.2/supervisely/app/fastapi/websocket.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/__init__.py` & `supervisely-6.9.2/supervisely/app/v1/__init__.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/app_service.py` & `supervisely-6.9.2/supervisely/app/v1/app_service.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/sly-icon-example.html` & `supervisely-6.9.2/supervisely/app/v1/sly-icon-example.html`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/widgets/chart.py` & `supervisely-6.9.2/supervisely/app/v1/widgets/chart.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/widgets/compare_gallery.py` & `supervisely-6.9.2/supervisely/app/v1/widgets/compare_gallery.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/widgets/grid_gallery.py` & `supervisely-6.9.2/supervisely/app/v1/widgets/grid_gallery.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/widgets/predictions_dynamics_gallery.py` & `supervisely-6.9.2/supervisely/app/v1/widgets/predictions_dynamics_gallery.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/widgets/progress_bar.py` & `supervisely-6.9.2/supervisely/app/v1/widgets/progress_bar.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/v1/widgets/single_image_gallery.py` & `supervisely-6.9.2/supervisely/app/v1/widgets/single_image_gallery.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/widgets/notification_box/notification_box.py` & `supervisely-6.9.2/supervisely/app/widgets/notification_box/notification_box.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/widgets/notification_box/template.html` & `supervisely-6.9.2/supervisely/app/widgets/notification_box/template.html`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<link rel="stylesheet" href="/sly/css/app/widgets/notification_box/style.css" />
+<link rel="stylesheet" href="./sly/css/app/widgets/notification_box/style.css" />
 
 <div class="notification-box notification-box-{{{widget.box_type}}}">
   <i class="notification-box-icon zmdi {{{widget.icon}}}"></i>
 
   <div>
     <div
       v-if="data.{{{widget.widget_id}}}.title"
```

### Comparing `supervisely-6.9.1/supervisely/app/widgets/radio_table/radio_table.py` & `supervisely-6.9.2/supervisely/app/widgets/radio_table/radio_table.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/widgets/radio_table/template.html` & `supervisely-6.9.2/supervisely/app/widgets/radio_table/template.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<link rel="stylesheet" href="/sly/css/app/widgets/radio_table/style.css"/>
+<link rel="stylesheet" href="./sly/css/app/widgets/radio_table/style.css"/>
 
 <table class="beautiful-table">
     <thead>
     <tr>
         <th v-for="col in data.{{{widget.widget_id}}}['header']">
             <div v-html="col['title']"></div>
             <div
```

### Comparing `supervisely-6.9.1/supervisely/app/widgets/sly_tqdm/sly_tqdm.py` & `supervisely-6.9.2/supervisely/app/widgets/sly_tqdm/sly_tqdm.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/app/widgets/sly_tqdm/template.html` & `supervisely-6.9.2/supervisely/app/widgets/sly_tqdm/template.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<link rel="stylesheet" href="/sly/css/app/widgets/sly_tqdm/style.css"/>
+<link rel="stylesheet" href="./sly/css/app/widgets/sly_tqdm/style.css"/>
 
 
 <div>
     <div style="display: flex; flex-direction: column">
         <div style="display: flex; flex-direction: row; justify-content: space-between;
                       margin: 5px 0">
             <div v-if="data.{{{widget.widget_id}}}.message" class="progress-title">
```

### Comparing `supervisely-6.9.1/supervisely/app/widgets/widget.py` & `supervisely-6.9.2/supervisely/app/widgets/widget.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/aug/aug.py` & `supervisely-6.9.2/supervisely/aug/aug.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/aug/imgaug_utils.py` & `supervisely-6.9.2/supervisely/aug/imgaug_utils.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/collection/key_indexed_collection.py` & `supervisely-6.9.2/supervisely/collection/key_indexed_collection.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/collection/str_enum.py` & `supervisely-6.9.2/supervisely/collection/str_enum.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/decorators/inference.py` & `supervisely-6.9.2/supervisely/decorators/inference.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/decorators/profile.py` & `supervisely-6.9.2/supervisely/decorators/profile.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/export/pascal_voc.py` & `supervisely-6.9.2/supervisely/export/pascal_voc.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/function_wrapper.py` & `supervisely-6.9.2/supervisely/function_wrapper.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/bitmap.py` & `supervisely-6.9.2/supervisely/geometry/bitmap.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/bitmap_base.py` & `supervisely-6.9.2/supervisely/geometry/bitmap_base.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/constants.py` & `supervisely-6.9.2/supervisely/geometry/constants.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/conversions.py` & `supervisely-6.9.2/supervisely/geometry/conversions.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/cuboid.py` & `supervisely-6.9.2/supervisely/geometry/cuboid.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/cuboid_3d.py` & `supervisely-6.9.2/supervisely/geometry/cuboid_3d.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/geometry.py` & `supervisely-6.9.2/supervisely/geometry/geometry.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/graph.py` & `supervisely-6.9.2/supervisely/geometry/graph.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/helpers.py` & `supervisely-6.9.2/supervisely/geometry/helpers.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/image_rotator.py` & `supervisely-6.9.2/supervisely/geometry/image_rotator.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/main_tests.py` & `supervisely-6.9.2/supervisely/geometry/main_tests.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/multichannel_bitmap.py` & `supervisely-6.9.2/supervisely/geometry/multichannel_bitmap.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/point.py` & `supervisely-6.9.2/supervisely/geometry/point.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/point_3d.py` & `supervisely-6.9.2/supervisely/geometry/point_3d.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/point_location.py` & `supervisely-6.9.2/supervisely/geometry/point_location.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/pointcloud.py` & `supervisely-6.9.2/supervisely/geometry/pointcloud.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/polygon.py` & `supervisely-6.9.2/supervisely/geometry/polygon.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/polyline.py` & `supervisely-6.9.2/supervisely/geometry/polyline.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/rectangle.py` & `supervisely-6.9.2/supervisely/geometry/rectangle.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/sliding_windows.py` & `supervisely-6.9.2/supervisely/geometry/sliding_windows.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/sliding_windows_fuzzy.py` & `supervisely-6.9.2/supervisely/geometry/sliding_windows_fuzzy.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/validation.py` & `supervisely-6.9.2/supervisely/geometry/validation.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/geometry/vector_geometry.py` & `supervisely-6.9.2/supervisely/geometry/vector_geometry.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/imaging/_video.py` & `supervisely-6.9.2/supervisely/imaging/_video.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/imaging/color.py` & `supervisely-6.9.2/supervisely/imaging/color.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/imaging/font.py` & `supervisely-6.9.2/supervisely/imaging/font.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/imaging/image.py` & `supervisely-6.9.2/supervisely/imaging/image.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/io/docker_utils.py` & `supervisely-6.9.2/supervisely/io/docker_utils.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/io/fs.py` & `supervisely-6.9.2/supervisely/io/fs.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/io/fs_cache.py` & `supervisely-6.9.2/supervisely/io/fs_cache.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/io/github_utils.py` & `supervisely-6.9.2/supervisely/io/github_utils.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/io/json.py` & `supervisely-6.9.2/supervisely/io/json.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/io/multipart_stream_decoder.py` & `supervisely-6.9.2/supervisely/io/multipart_stream_decoder.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/io/network_exceptions.py` & `supervisely-6.9.2/supervisely/io/network_exceptions.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/labeling_jobs/utils.py` & `supervisely-6.9.2/supervisely/labeling_jobs/utils.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/classification_metrics.py` & `supervisely-6.9.2/supervisely/metric/classification_metrics.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/common.py` & `supervisely-6.9.2/supervisely/metric/common.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/confusion_matrix_metric.py` & `supervisely-6.9.2/supervisely/metric/confusion_matrix_metric.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/iou_metric.py` & `supervisely-6.9.2/supervisely/metric/iou_metric.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/map_metric.py` & `supervisely-6.9.2/supervisely/metric/map_metric.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/matching.py` & `supervisely-6.9.2/supervisely/metric/matching.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/metrics_tests.py` & `supervisely-6.9.2/supervisely/metric/metrics_tests.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/pixel_accuracy.py` & `supervisely-6.9.2/supervisely/metric/pixel_accuracy.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/precision_recall_metric.py` & `supervisely-6.9.2/supervisely/metric/precision_recall_metric.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/metric/projects_applier.py` & `supervisely-6.9.2/supervisely/metric/projects_applier.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/config.py` & `supervisely-6.9.2/supervisely/nn/config.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/dataset.py` & `supervisely-6.9.2/supervisely/nn/dataset.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/class_indexing.py` & `supervisely-6.9.2/supervisely/nn/hosted/class_indexing.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/deploy.py` & `supervisely-6.9.2/supervisely/nn/hosted/deploy.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/inference_batch.py` & `supervisely-6.9.2/supervisely/nn/hosted/inference_batch.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/inference_batch_multiprocess.py` & `supervisely-6.9.2/supervisely/nn/hosted/inference_batch_multiprocess.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/inference_modes.py` & `supervisely-6.9.2/supervisely/nn/hosted/inference_modes.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/inference_single_image.py` & `supervisely-6.9.2/supervisely/nn/hosted/inference_single_image.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/legacy/inference_config.py` & `supervisely-6.9.2/supervisely/nn/hosted/legacy/inference_config.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/pytorch/inference_applier.py` & `supervisely-6.9.2/supervisely/nn/hosted/pytorch/inference_applier.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/pytorch/trainer.py` & `supervisely-6.9.2/supervisely/nn/hosted/pytorch/trainer.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/hosted/trainer.py` & `supervisely-6.9.2/supervisely/nn/hosted/trainer.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/inference/rest_client.py` & `supervisely-6.9.2/supervisely/nn/inference/rest_client.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/inference/rest_server.py` & `supervisely-6.9.2/supervisely/nn/inference/rest_server.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/pytorch/cuda.py` & `supervisely-6.9.2/supervisely/nn/pytorch/cuda.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/pytorch/dataset.py` & `supervisely-6.9.2/supervisely/nn/pytorch/dataset.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/pytorch/inference.py` & `supervisely-6.9.2/supervisely/nn/pytorch/inference.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/pytorch/metrics.py` & `supervisely-6.9.2/supervisely/nn/pytorch/metrics.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/pytorch/weights.py` & `supervisely-6.9.2/supervisely/nn/pytorch/weights.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/raw_to_labels.py` & `supervisely-6.9.2/supervisely/nn/raw_to_labels.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/nn/training/eval_planner.py` & `supervisely-6.9.2/supervisely/nn/training/eval_planner.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/pointcloud/pointcloud.py` & `supervisely-6.9.2/supervisely/pointcloud/pointcloud.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_annotation.py` & `supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_annotation.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_episode_annotation.py` & `supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_episode_annotation.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_figure.py` & `supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_figure.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/pointcloud_annotation/pointcloud_object.py` & `supervisely-6.9.2/supervisely/pointcloud_annotation/pointcloud_object.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/project/pointcloud_episode_project.py` & `supervisely-6.9.2/supervisely/project/pointcloud_episode_project.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/project/pointcloud_project.py` & `supervisely-6.9.2/supervisely/project/pointcloud_project.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/project/project.py` & `supervisely-6.9.2/supervisely/project/project.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/project/project_meta.py` & `supervisely-6.9.2/supervisely/project/project_meta.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/project/video_project.py` & `supervisely-6.9.2/supervisely/project/video_project.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/report/table.py` & `supervisely-6.9.2/supervisely/report/table.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/sly_logger.py` & `supervisely-6.9.2/supervisely/sly_logger.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/task/paths.py` & `supervisely-6.9.2/supervisely/task/paths.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/task/progress.py` & `supervisely-6.9.2/supervisely/task/progress.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/task/task_logger.py` & `supervisely-6.9.2/supervisely/task/task_logger.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video/import_utils.py` & `supervisely-6.9.2/supervisely/video/import_utils.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video/video.py` & `supervisely-6.9.2/supervisely/video/video.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/constants.py` & `supervisely-6.9.2/supervisely/video_annotation/constants.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/frame.py` & `supervisely-6.9.2/supervisely/video_annotation/frame.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/frame_collection.py` & `supervisely-6.9.2/supervisely/video_annotation/frame_collection.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/key_id_map.py` & `supervisely-6.9.2/supervisely/video_annotation/key_id_map.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/video_annotation.py` & `supervisely-6.9.2/supervisely/video_annotation/video_annotation.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/video_figure.py` & `supervisely-6.9.2/supervisely/video_annotation/video_figure.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/video_object.py` & `supervisely-6.9.2/supervisely/video_annotation/video_object.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/video_object_collection.py` & `supervisely-6.9.2/supervisely/video_annotation/video_object_collection.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/video_tag.py` & `supervisely-6.9.2/supervisely/video_annotation/video_tag.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/video_annotation/video_tag_collection.py` & `supervisely-6.9.2/supervisely/video_annotation/video_tag_collection.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/worker_api/agent_api.py` & `supervisely-6.9.2/supervisely/worker_api/agent_api.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/worker_api/agent_rpc.py` & `supervisely-6.9.2/supervisely/worker_api/agent_rpc.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/worker_api/chunking.py` & `supervisely-6.9.2/supervisely/worker_api/chunking.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/worker_api/retriers.py` & `supervisely-6.9.2/supervisely/worker_api/retriers.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/worker_api/rpc_servicer.py` & `supervisely-6.9.2/supervisely/worker_api/rpc_servicer.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/worker_proto/worker_api_pb2.py` & `supervisely-6.9.2/supervisely/worker_proto/worker_api_pb2.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely/worker_proto/worker_api_pb2_grpc.py` & `supervisely-6.9.2/supervisely/worker_proto/worker_api_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely.egg-info/PKG-INFO` & `supervisely-6.9.2/supervisely.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: supervisely
-Version: 6.9.1
+Version: 6.9.2
 Summary: Supervisely Python SDK.
 Home-page: https://github.com/supervisely/supervisely
 License: UNKNOWN
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
 Provides-Extra: extras
 Provides-Extra: apps
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: supervisely Version: 6.9.1 Summary: Supervisely
+Metadata-Version: 2.1 Name: supervisely Version: 6.9.2 Summary: Supervisely
 Python SDK. Home-page: https://github.com/supervisely/supervisely License:
 UNKNOWN Platform: UNKNOWN Description-Content-Type: text/markdown Provides-
 Extra: extras Provides-Extra: apps Provides-Extra: sdk-no-usages Provides-
 Extra: plugins Provides-Extra: sdk-nn-plugins
                                     ******
                                 [Supervisely]
                                  Supervisely
```

### Comparing `supervisely-6.9.1/supervisely.egg-info/SOURCES.txt` & `supervisely-6.9.2/supervisely.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `supervisely-6.9.1/supervisely.egg-info/requires.txt` & `supervisely-6.9.2/supervisely.egg-info/requires.txt`

 * *Files identical despite different names*

