# Comparing `tmp/honeybee-radiance-1.9.1.tar.gz` & `tmp/honeybee-radiance-1.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/honeybee-radiance-1.9.1.tar", last modified: Fri Feb 14 21:08:50 2020, max compression
+gzip compressed data, was "dist/honeybee-radiance-1.9.2.tar", last modified: Wed Mar 25 03:23:55 2020, max compression
```

## Comparing `honeybee-radiance-1.9.1.tar` & `honeybee-radiance-1.9.2.tar`

### file list

```diff
@@ -1,218 +1,222 @@
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:50.000000 honeybee-radiance-1.9.1/
--rw-rw-r--   0 travis    (2000) travis    (2000)       82 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/.dockerignore
--rw-rw-r--   0 travis    (2000) travis    (2000)      372 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/Dockerfile
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/.github/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1750 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/.github/project-manager.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)      247 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/MANIFEST.in
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/docs/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/docs/_build/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/docs/_build/docs/
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/_build/docs/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/_build/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/_build/.nojekyll
--rw-rw-r--   0 travis    (2000) travis    (2000)      478 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)     6567 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/conf.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      939 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/index.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)      170 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/cli.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)       88 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/docs/modules.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)      279 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/CODE_OF_CONDUCT.md
--rw-rw-r--   0 travis    (2000) travis    (2000)       55 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     2162 2020-02-14 21:08:50.000000 honeybee-radiance-1.9.1/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)      317 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/.releaserc.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1268 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)      194 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/.gitignore
--rw-rw-r--   0 travis    (2000) travis    (2000)      445 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/CONTRIBUTING.md
--rw-rw-r--   0 travis    (2000) travis    (2000)      102 2020-02-14 21:08:50.000000 honeybee-radiance-1.9.1/setup.cfg
--rw-rw-r--   0 travis    (2000) travis    (2000)     1245 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/.travis.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/LICENSE
--rw-rw-r--   0 travis    (2000) travis    (2000)       21 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/.coveragerc
--rw-rw-r--   0 travis    (2000) travis    (2000)      215 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/dev-requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     1201 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/setup.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      696 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/deploy.sh
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/tests/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1361 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/rad_string_collection.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2399 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_ring_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3821 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/material_glass_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2305 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/material_trans_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4814 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/sunpath_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2627 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/material_light_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1930 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_sphere_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3546 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/material_plastic_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5613 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/shade_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2379 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_cylinder_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2458 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_cone_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1764 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/primitive_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9314 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/modifier_set_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6105 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/aperture_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1918 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_source_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      351 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_bubble_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      337 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_cup_test.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/tests/assets/
--rw-rw-r--   0 travis    (2000) travis    (2000)   260641 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/klemsfull.xml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/tests/assets/epw/
--rw-rw-r--   0 travis    (2000) travis    (2000)  1646625 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/epw/denver.epw
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/tests/assets/model/
--rw-rw-r--   0 travis    (2000) travis    (2000)     3594 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/model/test_model.rad
--rw-rw-r--   0 travis    (2000) travis    (2000)      117 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/test_points.pts
--rw-rw-r--   0 travis    (2000) travis    (2000)      143 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/view.vf
--rw-rw-r--   0 travis    (2000) travis    (2000)      267 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/header_reader_test.amb
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/tests/assets/grid/
--rw-rw-r--   0 travis    (2000) travis    (2000)      262 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/grid/sensor_grid_merge_0002.pts
--rw-rw-r--   0 travis    (2000) travis    (2000)     1169 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/grid/sensor_grid_split.pts
--rw-rw-r--   0 travis    (2000) travis    (2000)      222 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/grid/sensor_grid_merge_0000.pts
--rw-rw-r--   0 travis    (2000) travis    (2000)      248 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/grid/sensor_grid_merge_0001.pts
--rw-rw-r--   0 travis    (2000) travis    (2000)      298 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/grid/sensor_grid_merge_0003.pts
--rw-rw-r--   0 travis    (2000) travis    (2000)   335885 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/tensortree.xml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/tests/assets/temp/
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/temp/.placeholder
--rw-rw-r--   0 travis    (2000) travis    (2000)   335885 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/assets/temp/tensortree.xml
--rw-rw-r--   0 travis    (2000) travis    (2000)      349 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_tube_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    15670 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/model_extend_test.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:50.000000 honeybee-radiance-1.9.1/tests/cli/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1944 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/cli/sunpath_cli_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      816 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/cli/sky_cli_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1308 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/cli/grid_cli_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/cli/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6349 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/face_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1895 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/material_bsdf_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5660 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/room_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3427 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/material_metal_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1251 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/ground_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1839 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/reader_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2262 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/material_glow_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3827 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/view_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1286 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/sky_hemisphere_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5703 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/door_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1907 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/sky_certain_irradiance_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1882 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/geometry_polygon_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1418 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/sensor_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2295 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/tests/sensorgrid_test.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2140 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/mutil.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2764 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/sensor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8449 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/sensorgrid.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1654 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/putil.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      131 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/config.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/
--rw-rw-r--   0 travis    (2000) travis    (2000)      788 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/modifierbase.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/
--rw-rw-r--   0 travis    (2000) travis    (2000)      639 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/interface.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      722 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/spotlight.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2603 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/brtdfunc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      930 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/dielectric.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12826 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/glass.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      442 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/metfunc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      449 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/materialbase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      955 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/antimatter.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      402 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/metal2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      794 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/ashik2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1145 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/prism1.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      537 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/prism2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      622 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/transdata.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      665 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/metal.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10166 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/plastic.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      842 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/transfunc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    15983 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/trans.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18297 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/bsdf.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      623 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/trans2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1199 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/plasdata.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6831 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/light.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      808 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/illum.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3437 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/mist.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      770 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      475 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/metdata.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1413 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/plastic2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8944 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/glow.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1437 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/plasfunc.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/
--rw-rw-r--   0 travis    (2000) travis    (2000)      495 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/colorfunc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1277 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/colortext.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      540 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/patternbase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      879 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/colorpict.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1088 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/colordata.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      263 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      515 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/brightdata.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      477 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/brightfunc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1999 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/brighttext.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/
--rw-rw-r--   0 travis    (2000) travis    (2000)      650 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixpict.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      562 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixturebase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      962 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixfunc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      842 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixtext.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      142 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      532 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixdata.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/
--rw-rw-r--   0 travis    (2000) travis    (2000)      740 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/texdata.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       84 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      551 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/texturebase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      576 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/texfunc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       62 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifier/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1304 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/_loadmodifiersets.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/data/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/data/modifiersets/
--rw-rw-r--   0 travis    (2000) travis    (2000)     6950 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/data/modifiersets/default.json
--rw-rw-r--   0 travis    (2000) travis    (2000)       86 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/data/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/data/modifiers/
--rw-rw-r--   0 travis    (2000) travis    (2000)      154 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/data/modifiers/user_library.mat
--rw-rw-r--   0 travis    (2000) travis    (2000)     1736 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/data/modifiers/default.mat
--rw-rw-r--   0 travis    (2000) travis    (2000)     1829 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/_loadmodifiers.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7088 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/modifiers.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       72 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3741 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lib/modifiersets.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    35480 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/modifierset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6249 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/reader.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22323 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/view.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       86 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/__main__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/
--rw-rw-r--   0 travis    (2000) travis    (2000)     6676 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/ring.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6122 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/cylinder.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1521 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/instance.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      322 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/bubble.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5210 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/source.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      422 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/tube.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      824 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/geometrybase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5399 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/polygon.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6919 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/cone.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      608 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/cup.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      313 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4863 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/sphere.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1477 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/geometry/mesh.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8561 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/writer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12272 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/config.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/
--rw-rw-r--   0 travis    (2000) travis    (2000)    18614 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/_gendaylit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8724 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sunpath.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4067 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/hemisphere.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1052 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/_skybase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       80 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6251 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/certainirradiance.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4192 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/ground.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       39 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/lightsource/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4365 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/room.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6289 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/_base.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4845 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/shade.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5426 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/door.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5547 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/aperture.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       36 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18358 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/model.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4404 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/properties/face.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance/cli/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2274 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/cli/util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9544 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/cli/sunpath.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1023 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/cli/sky.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3124 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/cli/grid.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      649 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/cli/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      651 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2889 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/_extend_honeybee.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16712 2020-02-14 21:07:56.000000 honeybee-radiance-1.9.1/honeybee_radiance/primitive.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance.egg-info/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2162 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance.egg-info/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance.egg-info/dependency_links.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       24 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance.egg-info/top_level.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     6556 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance.egg-info/SOURCES.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       73 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance.egg-info/requires.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       70 2020-02-14 21:08:49.000000 honeybee-radiance-1.9.1/honeybee_radiance.egg-info/entry_points.txt
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       82 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/.dockerignore
+-rw-rw-r--   0 travis    (2000) travis    (2000)      372 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/Dockerfile
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/.github/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1750 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/.github/project-manager.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)      247 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/MANIFEST.in
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/docs/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/docs/_templates/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3775 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/_templates/layout.html
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/docs/_build/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/docs/_build/docs/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/_build/docs/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/_build/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/_build/.nojekyll
+-rw-rw-r--   0 travis    (2000) travis    (2000)      478 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7141 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/conf.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      949 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/index.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)      170 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/cli.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)       88 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/modules.rst
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/docs/_static/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      939 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/docs/_static/custom.css
+-rw-rw-r--   0 travis    (2000) travis    (2000)      279 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/CODE_OF_CONDUCT.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)       55 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2162 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)      317 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/.releaserc.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1268 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)      194 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/.gitignore
+-rw-rw-r--   0 travis    (2000) travis    (2000)      445 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/CONTRIBUTING.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)      102 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/setup.cfg
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1245 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/.travis.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/LICENSE
+-rw-rw-r--   0 travis    (2000) travis    (2000)       21 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/.coveragerc
+-rw-rw-r--   0 travis    (2000) travis    (2000)      215 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/dev-requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1231 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/setup.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      696 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/deploy.sh
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/tests/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1361 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/rad_string_collection.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2399 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_ring_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3821 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/material_glass_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2305 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/material_trans_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5184 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/sunpath_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2627 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/material_light_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1930 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_sphere_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3546 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/material_plastic_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5613 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/shade_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2379 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_cylinder_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2458 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_cone_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1764 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/primitive_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9314 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/modifier_set_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6105 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/aperture_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1918 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_source_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      351 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_bubble_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      337 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_cup_test.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/tests/assets/
+-rw-rw-r--   0 travis    (2000) travis    (2000)   260641 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/klemsfull.xml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/tests/assets/epw/
+-rw-rw-r--   0 travis    (2000) travis    (2000)  1646625 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/epw/denver.epw
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/tests/assets/model/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3594 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/model/test_model.rad
+-rw-rw-r--   0 travis    (2000) travis    (2000)      117 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/test_points.pts
+-rw-rw-r--   0 travis    (2000) travis    (2000)      143 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/view.vf
+-rw-rw-r--   0 travis    (2000) travis    (2000)      267 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/header_reader_test.amb
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/tests/assets/grid/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      262 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/grid/sensor_grid_merge_0002.pts
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1169 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/grid/sensor_grid_split.pts
+-rw-rw-r--   0 travis    (2000) travis    (2000)      222 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/grid/sensor_grid_merge_0000.pts
+-rw-rw-r--   0 travis    (2000) travis    (2000)      248 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/grid/sensor_grid_merge_0001.pts
+-rw-rw-r--   0 travis    (2000) travis    (2000)      298 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/grid/sensor_grid_merge_0003.pts
+-rw-rw-r--   0 travis    (2000) travis    (2000)   335885 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/tensortree.xml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/tests/assets/temp/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/temp/.placeholder
+-rw-rw-r--   0 travis    (2000) travis    (2000)   335885 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/assets/temp/tensortree.xml
+-rw-rw-r--   0 travis    (2000) travis    (2000)      349 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_tube_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    15670 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/model_extend_test.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/tests/cli/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1944 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/cli/sunpath_cli_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      816 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/cli/sky_cli_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1308 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/cli/grid_cli_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/cli/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6349 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/face_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1895 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/material_bsdf_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5660 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/room_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3427 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/material_metal_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1251 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/ground_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1839 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/reader_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2262 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/material_glow_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3827 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/view_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1286 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/sky_hemisphere_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5703 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/door_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1907 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/sky_certain_irradiance_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1882 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/geometry_polygon_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1418 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/sensor_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2295 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/tests/sensorgrid_test.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2140 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/mutil.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2846 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/sensor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8606 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/sensorgrid.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1654 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/putil.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      131 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/config.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1011 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/modifierbase.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1581 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/interface.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1664 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/spotlight.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3546 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/brtdfunc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1872 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/dielectric.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13084 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/glass.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1358 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/metfunc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      590 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/materialbase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1900 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/antimatter.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1317 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/metal2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1737 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/ashik2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2088 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/prism1.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1479 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/prism2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1564 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/transdata.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2086 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/metal.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10351 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/plastic.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1785 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/transfunc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16118 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/trans.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18539 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/bsdf.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1565 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/trans2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2142 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/plasdata.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6965 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/light.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1751 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/illum.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4357 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/mist.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      770 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1391 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/metdata.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2357 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/plastic2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9077 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/glow.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2379 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/plasfunc.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      522 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/colorfunc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1334 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/colortext.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      758 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/patternbase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      906 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/colorpict.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1115 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/colordata.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      263 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      542 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/brightdata.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      504 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/brightfunc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2053 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/brighttext.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      677 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixpict.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      679 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixturebase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      989 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixfunc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      896 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixtext.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      142 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      558 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixdata.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      767 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/texdata.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       84 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      690 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/texturebase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      603 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/texfunc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       62 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifier/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1304 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/_loadmodifiersets.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/data/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/data/modifiersets/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6950 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/data/modifiersets/default.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)       86 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/data/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/data/modifiers/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      154 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/data/modifiers/user_library.mat
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1736 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/data/modifiers/default.mat
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1829 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/_loadmodifiers.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7088 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/modifiers.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       72 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3741 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lib/modifiersets.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    36483 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/modifierset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6270 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/reader.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22816 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/view.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       86 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/__main__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6779 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/ring.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6189 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/cylinder.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1547 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/instance.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1021 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/bubble.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5297 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/source.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1244 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/tube.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1065 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/geometrybase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5437 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/polygon.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7000 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/cone.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1507 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/cup.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      313 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4905 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/sphere.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1504 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/geometry/mesh.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8553 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/writer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9753 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/config.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18616 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/_gendaylit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8857 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sunpath.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4200 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/hemisphere.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1128 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/_skybase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       80 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6471 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/certainirradiance.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4328 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/ground.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       39 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/lightsource/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4747 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/room.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6210 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/_base.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5358 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/shade.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5934 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/door.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6062 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/aperture.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       36 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18311 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/model.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4915 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/properties/face.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance/cli/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2274 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/cli/util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9544 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/cli/sunpath.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1023 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/cli/sky.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3124 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/cli/grid.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      649 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/cli/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      651 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2889 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/_extend_honeybee.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16572 2020-03-25 03:23:01.000000 honeybee-radiance-1.9.2/honeybee_radiance/primitive.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-03-25 03:23:55.000000 honeybee-radiance-1.9.2/honeybee_radiance.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2162 2020-03-25 03:23:54.000000 honeybee-radiance-1.9.2/honeybee_radiance.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-03-25 03:23:54.000000 honeybee-radiance-1.9.2/honeybee_radiance.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       24 2020-03-25 03:23:54.000000 honeybee-radiance-1.9.2/honeybee_radiance.egg-info/top_level.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6608 2020-03-25 03:23:54.000000 honeybee-radiance-1.9.2/honeybee_radiance.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      100 2020-03-25 03:23:54.000000 honeybee-radiance-1.9.2/honeybee_radiance.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       70 2020-03-25 03:23:54.000000 honeybee-radiance-1.9.2/honeybee_radiance.egg-info/entry_points.txt
```

### Comparing `honeybee-radiance-1.9.1/.github/project-manager.yml` & `honeybee-radiance-1.9.2/.github/project-manager.yml`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/docs/conf.py` & `honeybee-radiance-1.9.2/docs/conf.py`

 * *Files 4% similar despite different names*

```diff
@@ -42,16 +42,16 @@
     'sphinx.ext.doctest',
     'sphinx.ext.todo',
     'sphinx.ext.coverage',
     'sphinx.ext.imgmath',
     'sphinx.ext.ifconfig',
     'sphinx.ext.viewcode',
     'sphinx.ext.githubpages',
-	'sphinxcontrib.fulltoc',
-	'sphinx.ext.napoleon',
+    'sphinxcontrib.fulltoc',
+    'sphinx.ext.napoleon',
     'sphinx_click.ext'
 ]
 
 # Add any paths that contain templates here, relative to this directory.
 templates_path = ['_templates']
 
 # The suffix(es) of source filenames.
@@ -96,32 +96,36 @@
 #
 html_theme_options = {
     # For black navbar, do "navbar navbar-inverse"
     'navbar_class': "navbar navbar-inverse",
     # Fix navigation bar to top of page?
     # Values: "true" (default) or "false"
     'navbar_fixed_top': "true",
-	'navbar_pagenav': True,
+    'navbar_pagenav': True,
     'source_link_position': "nav",
-	'bootswatch_theme': "united",
+    'bootswatch_theme': "united",
     'bootstrap_version': "3",
-	}
+}
+
+# Bootstrap theme custom file paths (relative to this file)
+# Layout.html path (already added above, include if different)
+# templates_path = ['_templates']
 
 # on_rtd is whether we are on readthedocs.org
 # on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
 
 # if not on_rtd:  # only import and set the theme if we're building docs locally
 #    import sphinx_rtd_theme
 #    html_theme = 'sphinx_rtd_theme'
 #    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
 
 # Add any paths that contain custom static files (such as style sheets) here,
 # relative to this directory. They are copied after the builtin static files,
 # so a file named "default.css" will overwrite the builtin "default.css".
-# html_static_path = ['_static']
+html_static_path = ['_static']
 
 # Custom sidebar templates, must be a dictionary that maps document names
 # to template names.
 #
 # The default sidebars (for documents that don't match any pattern) are
 # defined by theme itself.  Builtin themes are using these templates by
 # default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
@@ -212,7 +216,24 @@
 
 # -- Extension configuration -------------------------------------------------
 
 # -- Options for todo extension ----------------------------------------------
 
 # If true, `todo` and `todoList` produce output, else they produce nothing.
 todo_include_todos = True
+
+# -- Options for autodoc extension --------------------------------------------
+autodoc_default_options = {
+    'inherited-members': True,
+}
+
+autodoc_member_order = 'groupwise'
+
+
+def setup(app):
+    """Run custom code with access to the Sphinx application object
+    Args:
+        app: the Sphinx application object
+    """
+
+    # Add bootstrap theme custom stylesheet
+    app.add_stylesheet("custom.css")
```

### Comparing `honeybee-radiance-1.9.1/docs/index.rst` & `honeybee-radiance-1.9.2/docs/index.rst`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 
 Welcome to Honeybee Radiance's documentation!
-===================================
+=============================================
 
 .. image:: http://www.ladybug.tools/assets/img/honeybee.png
 
 `Radiance <https://radiance-online.org/>`_ extension for `honeybee <https://github.com/ladybug-tools/honeybee-core/>`_
 
 Honeybee-radiance adds radiance functionalities to honeybee for daylight simulation.
```

### Comparing `honeybee-radiance-1.9.1/PKG-INFO` & `honeybee-radiance-1.9.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-radiance
-Version: 1.9.1
+Version: 1.9.2
 Summary: Daylight and light simulation extension for honeybee.
 Home-page: https://github.com/ladybug-tools/honeybee-radiance
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: # honeybee-radiance
```

### Comparing `honeybee-radiance-1.9.1/README.md` & `honeybee-radiance-1.9.2/README.md`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/.travis.yml` & `honeybee-radiance-1.9.2/.travis.yml`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/LICENSE` & `honeybee-radiance-1.9.2/LICENSE`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/setup.py` & `honeybee-radiance-1.9.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -18,15 +18,15 @@
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ladybug-tools/honeybee-radiance",
     packages=setuptools.find_packages(exclude=["tests"]),
     include_package_data=True,
     install_requires=requirements,
     extras_require={
-        'cli': ['click>=5.1']
+        'cli': ['click>=5.1', 'honeybee-core[cli]>=1.10.0']
     },
     entry_points={
         "console_scripts": ["honeybee-radiance = honeybee_radiance.cli:radiance"]
     },
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3.6",
```

### Comparing `honeybee-radiance-1.9.1/deploy.sh` & `honeybee-radiance-1.9.2/deploy.sh`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/rad_string_collection.py` & `honeybee-radiance-1.9.2/tests/rad_string_collection.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/geometry_ring_test.py` & `honeybee-radiance-1.9.2/tests/geometry_ring_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/material_glass_test.py` & `honeybee-radiance-1.9.2/tests/material_glass_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/material_trans_test.py` & `honeybee-radiance-1.9.2/tests/material_trans_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/sunpath_test.py` & `honeybee-radiance-1.9.2/tests/sunpath_test.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 """Test SensorGrid class."""
 from honeybee_radiance.lightsource.sunpath import Sunpath
+from ladybug.sunpath import Sunpath as LBSunpath
 from ladybug.wea import Wea
 from ladybug.location import Location
 from ladybug.analysisperiod import AnalysisPeriod
 
 import pytest
 import os
 
@@ -41,29 +42,31 @@
 def test_invalid_input():
     with pytest.raises(AssertionError):
         Sunpath('Denver')
 
 
 def test_write_to_fie():
     sp = Sunpath(location)
+    lb_sp = LBSunpath.from_location(location)
     folder = './tests/assets/temp'
     filename = 'sunpath_annual'
     sp.to_file(folder, filename)
     sp_file = os.path.join(folder, '%s.rad' % filename)
     sp_mod_file = os.path.join(folder, '%s.mod' % filename)
     assert os.path.isfile(sp_file)
     assert os.path.isfile(sp_mod_file)
     with open(sp_mod_file) as inf:
         for count, _ in enumerate(inf):
             pass
-    assert count == 4427  # number of suns - 1
+    lb_tot = [i for i in range(8760) if lb_sp.calculate_sun_from_hoy(i).is_during_day]
+    assert count == len(lb_tot) - 1  # number of suns - 1
     with open(sp_file) as inf:
         for count, _ in enumerate(inf):
             pass
-    assert count == 4427  # number of suns - 1
+    assert count == len(lb_tot) - 1  # number of suns - 1
 
     # check line info
     with open(sp_file) as inf:
         data = inf.readline().split()
     
     assert data[6] == data[6] == data[6] == '1000000.0'
     assert data[-1] == '0.533'
@@ -135,22 +138,25 @@
     
     assert data[6] == data[6] == data[6] != '1000000.0'
 
 
 def test_split_modifiers():
     ap = AnalysisPeriod(timestep=4)
     sp = Sunpath(location)
+    lb_sp = LBSunpath.from_location(location)
     folder = './tests/assets/temp'
     filename = 'sunpath_timestep_4'
     sp.to_file(folder, filename, hoys=ap.hoys)
     sp_file = os.path.join(folder, '%s.rad' % filename)
     sp_mod_files = [
         os.path.join(folder, '%s_%d.mod' % (filename, count)) for count in range(2)
     ]
     assert os.path.isfile(sp_file)
-    sun_count = [8851, 8852]
+
+    lb_tot = [i for i in ap.hoys if lb_sp.calculate_sun_from_hoy(i).is_during_day]
+    sun_count = [int(len(lb_tot) / 2) - 1, int(len(lb_tot) / 2)]
     for sp_count, sp_mod_file in enumerate(sp_mod_files):
         assert os.path.isfile(sp_mod_file)
         with open(sp_mod_file) as inf:
             for count, _ in enumerate(inf):
                 pass
         assert count == sun_count[sp_count]
```

### Comparing `honeybee-radiance-1.9.1/tests/material_light_test.py` & `honeybee-radiance-1.9.2/tests/material_light_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/geometry_sphere_test.py` & `honeybee-radiance-1.9.2/tests/geometry_sphere_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/material_plastic_test.py` & `honeybee-radiance-1.9.2/tests/material_plastic_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/shade_extend_test.py` & `honeybee-radiance-1.9.2/tests/shade_extend_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/geometry_cylinder_test.py` & `honeybee-radiance-1.9.2/tests/geometry_cylinder_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/geometry_cone_test.py` & `honeybee-radiance-1.9.2/tests/geometry_cone_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/primitive_test.py` & `honeybee-radiance-1.9.2/tests/primitive_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/modifier_set_test.py` & `honeybee-radiance-1.9.2/tests/modifier_set_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/aperture_extend_test.py` & `honeybee-radiance-1.9.2/tests/aperture_extend_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/geometry_source_test.py` & `honeybee-radiance-1.9.2/tests/geometry_source_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/assets/klemsfull.xml` & `honeybee-radiance-1.9.2/tests/assets/klemsfull.xml`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/assets/epw/denver.epw` & `honeybee-radiance-1.9.2/tests/assets/epw/denver.epw`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/assets/model/test_model.rad` & `honeybee-radiance-1.9.2/tests/assets/model/test_model.rad`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/assets/grid/sensor_grid_split.pts` & `honeybee-radiance-1.9.2/tests/assets/grid/sensor_grid_split.pts`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/assets/tensortree.xml` & `honeybee-radiance-1.9.2/tests/assets/tensortree.xml`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/assets/temp/tensortree.xml` & `honeybee-radiance-1.9.2/tests/assets/temp/tensortree.xml`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/model_extend_test.py` & `honeybee-radiance-1.9.2/tests/model_extend_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/cli/sunpath_cli_test.py` & `honeybee-radiance-1.9.2/tests/cli/sunpath_cli_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/cli/sky_cli_test.py` & `honeybee-radiance-1.9.2/tests/cli/sky_cli_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/cli/grid_cli_test.py` & `honeybee-radiance-1.9.2/tests/cli/grid_cli_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/face_extend_test.py` & `honeybee-radiance-1.9.2/tests/face_extend_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/material_bsdf_test.py` & `honeybee-radiance-1.9.2/tests/material_bsdf_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/room_extend_test.py` & `honeybee-radiance-1.9.2/tests/room_extend_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/material_metal_test.py` & `honeybee-radiance-1.9.2/tests/material_metal_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/ground_test.py` & `honeybee-radiance-1.9.2/tests/ground_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/reader_test.py` & `honeybee-radiance-1.9.2/tests/reader_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/material_glow_test.py` & `honeybee-radiance-1.9.2/tests/material_glow_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/view_test.py` & `honeybee-radiance-1.9.2/tests/view_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/sky_hemisphere_test.py` & `honeybee-radiance-1.9.2/tests/sky_hemisphere_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/door_extend_test.py` & `honeybee-radiance-1.9.2/tests/door_extend_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/sky_certain_irradiance_test.py` & `honeybee-radiance-1.9.2/tests/sky_certain_irradiance_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/geometry_polygon_test.py` & `honeybee-radiance-1.9.2/tests/geometry_polygon_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/sensor_test.py` & `honeybee-radiance-1.9.2/tests/sensor_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/tests/sensorgrid_test.py` & `honeybee-radiance-1.9.2/tests/sensorgrid_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/mutil.py` & `honeybee-radiance-1.9.2/honeybee_radiance/mutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/sensor.py` & `honeybee-radiance-1.9.2/honeybee_radiance/sensor.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,35 +1,42 @@
 """A light version of test points."""
 from __future__ import division
 import honeybee.typing as typing
 
 
 class Sensor(object):
-    """A radiance sensor."""
+    """A radiance sensor.
 
+    Args:
+        position: Position of sensor as (x, y, z) (Default: (0, 0, 0)).
+        direction: Direction of sensor as (x, y, z) (Default: (0, 0, 1)).
+
+    Properties:
+        * position
+        * direction
+
+    """
     __slots__ = ('_pos', '_dir')
 
     def __init__(self, position=None, direction=None):
-        """Create a sensor.
-        
-        Args:
-            position: Position of sensor as (x, y, z) (Default: (0, 0, 0)).
-            direction: Direction of sensor as (x, y, z) (Default: (0, 0, 1)).
-        """
+        """Create a sensor."""
         self._pos = typing.tuple_with_length(position) if position is not None \
             else (0, 0, 0)
         self._dir = typing.tuple_with_length(direction) if direction is not None \
             else (0, 0, 1)
 
     @classmethod
     def from_dict(cls, sensor_dict):
         """Create a sensor from dictionary.
+
+        .. code-block:: python
+
             {
-                'x': float, 'y': float, 'z': float,
-                'dx': float, 'dx': float, 'dz': float
+            'x': float, 'y': float, 'z': float,
+            'dx': float, 'dx': float, 'dz': float
             }
         """
         return cls(
             [sensor_dict['x'], sensor_dict['y'], sensor_dict['z']],
             [sensor_dict['dx'], sensor_dict['dy'], sensor_dict['dz']]
         )
 
@@ -64,17 +71,20 @@
         return '%s %s' % (
             ' '.join(str(v) for v in self.position),
             ' '.join(str(v) for v in self.direction)
         )
 
     def to_dict(self):
         """Get the sensor as a dictionary.
+
+        .. code-block:: python
+
             {
-                'x': float, 'y': float, 'z': float,
-                'dx': float, 'dx': float, 'dz': float
+            'x': float, 'y': float, 'z': float,
+            'dx': float, 'dx': float, 'dz': float
             }
         """
         return {
             'x': self.position[0], 'y': self.position[1], 'z': self.position[2],
             'dx': self.direction[0], 'dy': self.direction[1], 'dz': self.direction[2]
         }
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/sensorgrid.py` & `honeybee-radiance-1.9.2/honeybee_radiance/sensorgrid.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,41 +10,48 @@
 except:
     # python 3
     pass
 
 class SensorGrid(object):
     """A grid of sensors.
 
-    Attributes:
-        name
-        sensors
-        positions
-        directions
+    Args:
+        name: A unique name for this SensorGrid.
+        sensors: A collection of Sensors.
+
+    Properties:
+        * name
+        * sensors
+        * positions
+        * directions
     """
 
     __slots__ = ('_sensors', '_name')
 
     def __init__(self, name, sensors):
-        """Initialize a SensorGrid.
-
-        Args:
-            name: A unique name for this SensorGrid.
-            sensors: A collection of Sensors.
-        """
+        """Initialize a SensorGrid."""
         self.name = typing.valid_string(name)
         self._sensors = tuple(sensors)
         for sen in self._sensors:
             if not isinstance(sen, Sensor):
                 raise ValueError(
                     'Sensors in SensorGrid must be form type Sensor not %s' % type(sen)
                 )
 
     @classmethod
     def from_dict(cls, ag_dict):
-        """Create a sensor grid from a dictionary."""
+        """Create a sensor grid from a dictionary in the following format.
+
+        .. code-block:: python
+
+            {
+            "name": str,  # SensorGrid name
+            "sensors": []  # list of Sensor dictionaries
+            }
+        """
         sensors = (Sensor.from_dict(sensor) for sensor in ag_dict['sensors'])
         return cls(name=ag_dict["name"], sensors=sensors)
 
     @classmethod
     def from_planar_grid(cls, name, positions, plane_normal):
         """Create a sensor grid from a collection of positions with the same direction.
 
@@ -88,15 +95,15 @@
             end_line: End line as an integer including the comments
                 (default: last line in file).
             name: An optional name for SensorGrid otherwise the file name will be used.
         """
         if not os.path.isfile(file_path):
             raise IOError("Can't find {}.".format(file_path))
         name = name or os.path.split(os.path.splitext(file_path)[0])[-1]
-        
+
         start_line = int(start_line) if start_line is not None else 0
         try:
             end_line = int(end_line)
         except TypeError:
             end_line = float('+inf')
 
         line_count = end_line - start_line + 1
@@ -152,20 +159,20 @@
 
     def to_radiance(self):
         """Return sensors grid as a Radiance string."""
         return "\n".join((ap.to_radiance() for ap in self._sensors))
 
     def to_file(self, folder, file_name=None, mkdir=False):
         """Write this sensor grid to a Radiance sensors file.
-        
+
         Args:
             folder: Target folder.
             file_name: Optional file name without extension (Default: self.name).
             mkdir: A boolean to indicate if the folder should be created in case it
-                doesn't exist already (Default: False). 
+                doesn't exist already (Default: False).
 
         Returns:
             Full path to newly created file.
         """
         name = file_name or self.name + '.pts'
         return futil.write_to_file_by_name(
             folder, name, self.to_radiance() + '\n', mkdir)
@@ -191,15 +198,15 @@
         # calculate sensor count in each file
         sc = int(round(self.count / count))
         sensors = iter(self._sensors)
         for fc in range(count - 1):
             name = '%s_%04d.pts' % (base_name, fc)
             content = '\n'.join((next(sensors).to_radiance() for _ in range(sc)))
             futil.write_to_file_by_name(folder, name, content + '\n', mkdir)
-        
+
         # write whatever is left to the last file
         name = '%s_%04d.pts' % (base_name, count - 1)
         content = '\n'.join((sensor.to_radiance() for sensor in sensors))
         futil.write_to_file_by_name(folder, name, content + '\n', mkdir)
 
         grids_info = []
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/putil.py` & `honeybee-radiance-1.9.2/honeybee_radiance/putil.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/modifierbase.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/modifierbase.py`

 * *Files 20% similar despite different names*

```diff
@@ -9,15 +9,28 @@
 
 https://floyd.lbl.gov/radiance/refer/ray.html
 """
 from ..primitive import Primitive
 
 
 class Modifier(Primitive):
-    """Base class for Radiance modifiers."""
+    """Base class for Radiance modifiers.
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+        * is_texture
+        * is_pattern
+        * is_mixture
+        * is_opaque
+    """
 
     __slots__ = ()
 
     @property
     def is_modifier(self):
         """Get a boolean indicating whether this object is a Radiance modifier.
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/brtdfunc.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/brtdfunc.py`

 * *Files 23% similar despite different names*

```diff
@@ -9,14 +9,16 @@
 class BRTDfunc(Material):
     """Radiance BRTDfunc Material.
 
     The material BRTDfunc gives the maximum flexibility over surface reflectance and
     transmittance, providing for spectrally-dependent specular rays and reflectance and
     transmittance distribution functions.
 
+    .. code-block:: shell
+
         mod BRTDfunc id
         10+  rrefl  grefl  brefl
              rtrns  gtrns  btrns
              rbrtd  gbrtd  bbrtd
              funcfile  transform
         0
         9+   rfdif gfdif bfdif
@@ -45,11 +47,33 @@
     will be available through the special variables CrP, CgP and CbP.
 
     Care must be taken when using this material type to produce a physically valid
     reflection model. The reflectance functions should be bidirectional, and under no
     circumstances should the sum of reflected diffuse, transmitted diffuse, reflected
     specular, transmitted specular and the integrated directional diffuse component be
     greater than one.
+
+    Args:
+        name: Primitive name as a string. Cannot contain white spaces or special
+            characters.
+        modifier: Modifier. It can be primitive, mixture, texture or pattern.
+            (Default: "void").
+        values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
+            refer to a line number in the radiance primitve definitions and the
+            values in each array correspond to values occurring within each line.
+        is_opaque: A boolean to indicate whether this primitive is opaque.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives that are
+            defined based on other primitives. (Default: []).
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+        * is_opaque
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/dielectric.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/dielectric.py`

 * *Files 26% similar despite different names*

```diff
@@ -13,16 +13,39 @@
     Its behavior is determined by the index of refraction and transmission coefficient in
     each wavelength band per unit length. Common glass has a index of refraction (n)
     around 1.5, and a transmission coefficient of roughly 0.92 over an inch. An
     additional number, the Hartmann constant, describes how the index of refraction
     changes as a function of wavelength. It is usually zero. (A pattern modifies only the
     refracted value.)
 
+    .. code-block:: shell
+
         mod dielectric id
         0
         0
         5 rtn gtn btn n hc
 
+    Args:
+        name: Primitive name as a string. Cannot contain white spaces or special
+            characters.
+        modifier: Modifier. It can be primitive, mixture, texture or pattern.
+            (Default: "void").
+        values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
+            refer to a line number in the radiance primitve definitions and the
+            values in each array correspond to values occurring within each line.
+        is_opaque: A boolean to indicate whether this primitive is opaque.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives that are
+            defined based on other primitives. (Default: []).
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+        * is_opaque
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/glass.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/glass.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,41 +6,56 @@
 
 import math
 from .materialbase import Material
 import honeybee.typing as typing
 
 
 class Glass(Material):
-    """Radiance glass material."""
+    """Radiance glass material.
+
+    Args:
+        name: Material name as a string. Do not use white space or special character
+        r_transmissivity: Transmissivity for red. The value should be between 0 and 1
+            (Default: 0).
+        g_transmissivity: Transmissivity for green. The value should be between 0
+            and 1 (Default: 0).
+        b_transmissivity: Transmissivity for blue. The value should be between 0 and
+            1 (Default: 0).
+        refraction: Index of refraction. 1.52 for glass and 1.4 for ETFE
+            (Default: 1.52).
+        modifier: Material modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * r_transmissivity
+        * g_transmissivity
+        * b_transmissivity
+        * refraction_index
+        * average_transmissivity
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+
+    Usage:
+
+    .. code-block:: python
+
+        glass_material = Glass("generic_glass", .65, .65, .65)
+        print(glass_material)
+    """
 
     def __init__(self, name, r_transmissivity=0.0, g_transmissivity=0.0,
                  b_transmissivity=0.0, refraction_index=None, modifier="void",
                  dependencies=None):
-        """Create glass material.
-
-        args:
-            name: Material name as a string. Do not use white space or special character
-            r_transmissivity: Transmissivity for red. The value should be between 0 and 1
-                (Default: 0).
-            g_transmissivity: Transmissivity for green. The value should be between 0
-                and 1 (Default: 0).
-            b_transmissivity: Transmissivity for blue. The value should be between 0 and
-                1 (Default: 0).
-            refraction: Index of refraction. 1.52 for glass and 1.4 for ETFE
-                (Default: 1.52).
-            modifier: Material modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-
-        Usage:
-
-            glass_material = Glass("generic_glass", .65, .65, .65)
-            print(glass_material)
-        """
+        """Create glass material."""
         Material.__init__(self, name, modifier=modifier,
                           dependencies=dependencies)
         self.r_transmissivity = r_transmissivity
         self.g_transmissivity = g_transmissivity
         self.b_transmissivity = b_transmissivity
         self.refraction_index = refraction_index
         self._update_values()
@@ -138,14 +153,16 @@
             modifier: Material modifier (Default: "void").
             dependencies: A list of primitives that this primitive depends on. This
                 argument is only useful for defining advanced primitives where the
                 primitive is defined based on other primitives. (Default: [])
 
         Usage:
 
+        .. code-block:: python
+
             glass_material = Glass.from_transmittance("generic_glass", .60, .60, .60)
             print(glass_material)
         """
         rt = cls.get_transmissivity(r_transmittance)
         gt = cls.get_transmissivity(g_transmittance)
         bt = cls.get_transmissivity(b_transmittance)
         return cls(name, rt, gt, bt, refraction_index, modifier, dependencies=dependencies)
@@ -162,17 +179,20 @@
             rgb_transmissivity: Transmissivity for red, green and blue. The value should
                 be between 0 and 1 (Default: 0).
             refraction: Index of refraction. 1.52 for glass and 1.4 for ETFE
                 (Default: 1.52).
             modifier: Material modifier (Default: "void").
             dependencies: A list of primitives that this primitive depends on. This
                 argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])            
+                primitive is defined based on other primitives. (Default: [])
 
         Usage:
+
+        .. code-block:: python
+
             glassMaterial = Glass.by_single_trans_value("generic glass", .65)
             print(glassMaterial)
         """
         return cls(
             name, r_transmissivity=rgb_transmissivity, g_transmissivity=rgb_transmissivity,
             b_transmissivity=rgb_transmissivity, refraction_index=refraction_index,
             modifier=modifier, dependencies=dependencies)
@@ -191,14 +211,17 @@
                 (Default: 1.52).
             modifier: Material modifier (Default: "void").
             dependencies: A list of primitives that this primitive depends on. This
                 argument is only useful for defining advanced primitives where the
                 primitive is defined based on other primitives. (Default: [])
 
         Usage:
+
+        .. code-block:: python
+
             glassMaterial = Glass.by_single_trans_value("generic glass", .65)
             print(glassMaterial)
         """
         rgb_transmissivity = cls.get_transmissivity(rgb_transmittance)
         return cls(
             name,
             r_transmissivity=rgb_transmissivity, g_transmissivity=rgb_transmissivity,
@@ -208,22 +231,22 @@
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize Glass from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "glass", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "glass",  # primitive type
+            "name": "",  # primitive name
+            "values": [] , # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != 'glass':
             raise ValueError('Type must be glass not %s.' % primitive_dict['type'])
 
         modifier, dependencies = cls.filter_dict_input(primitive_dict)
@@ -247,25 +270,25 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize Glass from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "name": "", // Material Name
-                "type": "glass",
-                "r_transmissivity": float, // Transmissivity for red
-                "g_transmissivity": float, // Transmissivity for green
-                "b_transmissivity": float, // Transmissivity for blue
-                "refraction_index": float, // Index of refraction
-                "modifier": "", // material modifier (Default: "void")
-                "dependencies": []
+            "name": "",  # Material Name
+            "type": "glass",
+            "r_transmissivity": float,  # Transmissivity for red
+            "g_transmissivity": float,  # Transmissivity for green
+            "b_transmissivity": float,  # Transmissivity for blue
+            "refraction_index": float,  # Index of refraction
+            "modifier": "",  # material modifier (Default: "void")
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != 'glass':
             raise ValueError('Type must be glass not %s.' % data['type'])
 
         modifier, dependencies = Material.filter_dict_input(data)
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/ashik2.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/ashik2.py`

 * *Files 26% similar despite different names*

```diff
@@ -11,15 +11,39 @@
 
     Ashik2 is the anisotropic reflectance model by Ashikhmin & Shirley. The string
     arguments are the same as for plastic2, but the real arguments have additional
     flexibility to specify the specular color. Also, rather than roughness, specular
     power is used, which has no physical meaning other than larger numbers are equivalent
     to a smoother surface.
 
+    .. code-block:: shell
+
         mod ashik2 id
         4+ ux uy uz funcfile transform
         0
         8 dred dgrn dblu sred sgrn sblu u-power v-power
+
+    Args:
+        name: Primitive name as a string. Cannot contain white spaces or special
+            characters.
+        modifier: Modifier. It can be primitive, mixture, texture or pattern.
+            (Default: "void").
+        values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
+            refer to a line number in the radiance primitve definitions and the
+            values in each array correspond to values occurring within each line.
+        is_opaque: A boolean to indicate whether this primitive is opaque.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives that are
+            defined based on other primitives. (Default: []).
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+        * is_opaque
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/prism1.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/prism1.py`

 * *Files 19% similar despite different names*

```diff
@@ -13,19 +13,43 @@
     generating virtual light sources. It can only be used to modify a planar surface
     (i.e., a polygon or disk) and should not result in either light concentration or
     scattering. The new direction of the ray can be on either side of the material, and
     the definitions must have the correct bidirectional properties to work properly with
     virtual light sources. The arguments give the coefficient for the redirected light
     and its direction.
 
+    .. code-block:: shell
+
         mod prism1 id
         5+ coef dx dy dz funcfile transform
         0
         n A1 A2 .. An
 
     The new direction variables dx, dy and dz need not produce a normalized vector. For
     convenience, the variables DxA, DyA and DzA are defined as the normalized direction
     to the target light source.
+
+    Args:
+        name: Primitive name as a string. Cannot contain white spaces or special
+            characters.
+        modifier: Modifier. It can be primitive, mixture, texture or pattern.
+            (Default: "void").
+        values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
+            refer to a line number in the radiance primitve definitions and the
+            values in each array correspond to values occurring within each line.
+        is_opaque: A boolean to indicate whether this primitive is opaque.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives that are
+            defined based on other primitives. (Default: []).
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+        * is_opaque
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/plastic.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/plastic.py`

 * *Files 13% similar despite different names*

```diff
@@ -5,47 +5,64 @@
 from __future__ import division
 
 from .materialbase import Material
 import honeybee.typing as typing
 
 
 class Plastic(Material):
-    """Radiance plastic material."""
+    """Radiance plastic material.
+
+    Args:
+        name: Material name as a string. Do not use white space or special
+            character.
+        r_reflectance: Reflectance for red. The value should be between 0 and 1
+            (Default: 0).
+        g_reflectance: Reflectance for green. The value should be between 0 and 1
+            (Default: 0).
+        b_reflectance: Reflectance for blue. The value should be between 0 and 1
+            (Default: 0).
+        specularity: Fraction of specularity. Specularity fractions greater than 0.1
+            are not realistic (Default: 0).
+        roughness: Roughness is specified as the rms slope of surface facets. A
+            value of 0 corresponds to a perfectly smooth surface, and a value of 1
+            would be a very rough surface. Roughness values greater than 0.2 are not
+            very realistic. (Default: 0).
+        modifier: Material modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * r_reflectance
+        * g_reflectance
+        * b_reflectance
+        * specularity
+        * roughness
+        * average_reflectance
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+
+    Usage:
+
+    .. code-block:: python
+
+        wall_material = Plastic("generic_wall", .55, .65, .75)
+        print(wall_material)
+    """
 
     __slots__ = ('_r_reflectance', '_g_reflectance', '_b_reflectance',
                  '_specularity', '_roughness')
 
     def __init__(self, name, r_reflectance=0.0, g_reflectance=0.0, b_reflectance=0.0,
                  specularity=0.0, roughness=0.0, modifier="void", dependencies=None):
-        """Create plastic material.
-
-        args:
-            name: Material name as a string. Do not use white space or special
-                character.
-            r_reflectance: Reflectance for red. The value should be between 0 and 1
-                (Default: 0).
-            g_reflectance: Reflectance for green. The value should be between 0 and 1
-                (Default: 0).
-            b_reflectance: Reflectance for blue. The value should be between 0 and 1
-                (Default: 0).
-            specularity: Fraction of specularity. Specularity fractions greater than 0.1
-                are not realistic (Default: 0).
-            roughness: Roughness is specified as the rms slope of surface facets. A
-                value of 0 corresponds to a perfectly smooth surface, and a value of 1
-                would be a very rough surface. Roughness values greater than 0.2 are not
-                very realistic. (Default: 0).
-            modifier: Material modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-
-        Usage:
-            wall_material = Plastic("generic_wall", .55, .65, .75)
-            print(wall_material)
-        """
+        """Create plastic material."""
         Material.__init__(self, name, modifier=modifier, dependencies=dependencies)
         self.r_reflectance = r_reflectance
         self.g_reflectance = g_reflectance
         self.b_reflectance = b_reflectance
         self.specularity = specularity
         self.roughness = roughness
 
@@ -153,36 +170,39 @@
                 realistic. (Default: 0).
             modifier: Material modifier (Default: "void").
             dependencies: A list of primitives that this primitive depends on. This
                 argument is only useful for defining advanced primitives where the
                 primitive is defined based on other primitives. (Default: [])
 
         Usage:
+
+        .. code-block:: python
+
             wall_material = Plastic.by_single_reflect_value("generic_wall", .55)
             print(wall_material)
         """
         return cls(name, r_reflectance=rgb_reflectance, g_reflectance=rgb_reflectance,
                    b_reflectance=rgb_reflectance, specularity=specularity,
                    roughness=roughness, modifier=modifier, dependencies=dependencies)
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize Plastic from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "plastic", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "plastic",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
             )
@@ -207,26 +227,26 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize Plastic from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": {} or void, // Material modifier
-                "type": "plastic", // Material type
-                "name": "", // Material Name
-                "r_reflectance": float, // Reflectance for red
-                "g_reflectance": float, // Reflectance for green
-                "b_reflectance": float, // Reflectance for blue
-                "specularity": float, // Material specularity
-                "roughness": float, // Material roughness
-                "dependencies": []
+            "modifier": {} or void,  # Material modifier
+            "type": "plastic",  # Material type
+            "name": "",  # Material Name
+            "r_reflectance": float,  # Reflectance for red
+            "g_reflectance": float,  # Reflectance for green
+            "b_reflectance": float,  # Reflectance for blue
+            "specularity": float,  # Material specularity
+            "roughness": float,  # Material roughness
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                     data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/trans.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/trans.py`

 * *Files 3% similar despite different names*

```diff
@@ -6,47 +6,62 @@
 from __future__ import division
 
 from .materialbase import Material
 import honeybee.typing as typing
 
 
 class Trans(Material):
-    """Radiance translucent material."""
+    """Radiance translucent material.
+
+    Args:
+        name: Material name as a string. Do not use white space or special
+            character.
+        r_reflectance: Reflectance for red. The value should be between 0 and 1
+            (Default: 0).
+        g_reflectance: Reflectance for green. The value should be between 0 and 1
+            (Default: 0).
+        b_reflectance: Reflectance for blue. The value should be between 0 and 1
+            (Default: 0).
+        specularity: Fraction of specularity. Specularity fractions greater than 0.1
+            are not realistic (Default: 0).
+        roughness: Roughness is specified as the rms slope of surface facets. A
+            value of 0 corresponds to a perfectly smooth surface, and a value of 1
+            would be a very rough surface. Roughness values greater than 0.2 are not
+            very realistic. (Default: 0).
+        transmitted_diff: The transmitted diffuse component is the fraction of
+            transmitted light that is transmitted diffusely in as scattering fashion.
+        transmitted_spec: The transmitted specular component is the fraction of
+            transmitted light that is not diffusely scattered.
+        modifier: Material modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * r_reflectance
+        * g_reflectance
+        * b_reflectance
+        * specularity
+        * roughness
+        * transmitted_diff
+        * transmitted_spec
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+    """
     __slots__ = ('_r_reflectance', '_g_reflectance', '_b_reflectance',
                  '_specularity', '_roughness', '_transmitted_diff', '_transmitted_spec')
 
     def __init__(self, name, r_reflectance=0.0, g_reflectance=0.0, b_reflectance=0.0,
                  specularity=0.0, roughness=0.0, transmitted_diff=0.0,
                  transmitted_spec=0.0, modifier="void", dependencies=None):
-        """Create trans material.
-
-        args:
-            name: Material name as a string. Do not use white space or special
-                character.
-            r_reflectance: Reflectance for red. The value should be between 0 and 1
-                (Default: 0).
-            g_reflectance: Reflectance for green. The value should be between 0 and 1
-                (Default: 0).
-            b_reflectance: Reflectance for blue. The value should be between 0 and 1
-                (Default: 0).
-            specularity: Fraction of specularity. Specularity fractions greater than 0.1
-                are not realistic (Default: 0).
-            roughness: Roughness is specified as the rms slope of surface facets. A
-                value of 0 corresponds to a perfectly smooth surface, and a value of 1
-                would be a very rough surface. Roughness values greater than 0.2 are not
-                very realistic. (Default: 0).
-            transmitted_diff: The transmitted diffuse component is the fraction of
-                transmitted light that is transmitted diffusely in as scattering fashion.
-            transmitted_spec: The transmitted specular component is the fraction of
-                transmitted light that is not diffusely scattered.
-            modifier: Material modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-        """
+        """Create trans material."""
         Material.__init__(self, name, modifier=modifier,
                           dependencies=dependencies)
         self.r_reflectance = r_reflectance
         self.g_reflectance = g_reflectance
         self.b_reflectance = b_reflectance
         self.specularity = specularity
         self.roughness = roughness
@@ -276,22 +291,22 @@
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize Trans from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "trans", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "trans",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (
                     cls.__name__.lower(), primitive_dict['type'])
@@ -320,28 +335,28 @@
     @classmethod
     def from_dict(cls, input_dict):
         """Initialize Trans from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": {} or void, // Material modifier
-                "type": "trans", // Material type
-                "name": "", // Material Name
-                "r_reflectance": float, // Reflectance for red
-                "g_reflectance": float, // Reflectance for green
-                "b_reflectance": float, // Reflectance for blue
-                "specularity": float, // Material specularity
-                "roughness": float, // Material roughness
-                "transmitted_diff": float,
-                "transmitted_spec": float,
-                "dependencies": []
+            "modifier": {} or void,  # Material modifier
+            "type": "trans",  # Material type
+            "name": "", // Material Name
+            "r_reflectance": float,  # Reflectance for red
+            "g_reflectance": float,  # Reflectance for green
+            "b_reflectance": float,  # Reflectance for blue
+            "specularity": float,  # Material specularity
+            "roughness": float,  # Material roughness
+            "transmitted_diff": float,
+            "transmitted_spec": float,
+            "dependencies": []
             }
         """
         assert 'type' in input_dict, 'Input dictionary is missing "type".'
         if input_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                                              input_dict['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/bsdf.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/bsdf.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,59 +20,78 @@
         # IronPython
         from StringIO import StringIO
 
 
 class BSDF(Material):
     """Radiance BSDF material.
 
-    mod BSDF id
-    6+ thick BSDFfile ux uy uz funcfile transform
-    0
-    0|3|6|9
-        rfdif gfdif bfdif
-        rbdif gbdif bbdif
-        rtdif gtdif btdif
+    .. code-block:: shell
+
+        mod BSDF id
+        6+ thick BSDFfile ux uy uz funcfile transform
+        0
+        0|3|6|9
+            rfdif gfdif bfdif
+            rbdif gbdif bbdif
+            rtdif gtdif btdif
 
     The __init__ method sets additional diffuse reflectance for front and  back as well
     as addition diffuse transmittance to 0. You can set-up these values by using their
     respective property.
+
+    Args:
+        bsdf_file: Path to an xml file. Data will NOT be cached in memory.
+        up_orientation: (x, y ,z) vector that sets the hemisphere that the
+            BSDF material faces.  For materials that are symmetrical about
+            the face plane (like non-angled venetian blinds), this can be
+            any vector that is not perfectly normal to the face. For
+            asymmetrical materials like angled venetian blinds, this variable
+            should be coordinated with the direction the face are facing.
+            The default is set to (0.01, 0.01, 1.00), which should hopefully
+            not be perpendicular to any typical face.
+        thickness: Optional number to set the thickness of the BSDF material.
+            (default: 0).
+        modifier: Material modifier (Default: 'void').
+        function_file: Optional input for function file (Default: .).
+        transform: Optional transform input to to scale the thickness and reorient
+            the up vector (default: None).
+        angle_basis: BSDF file angle basis. If not provided by user honeybee tries to
+            find it by parsing BSDF file itself.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+
+    Properties:
+        * name
+        * bsdf_file
+        * up_orientation
+        * thickness
+        * function_file
+        * transform
+        * angle_basis
+        * front_diffuse_reflectance
+        * back_diffuse_reflectance
+        * diffuse_transmittance
+        * dependencies
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
     """
     __slots__ = ('_bsdf_file', '_up_orientation', '_thickness', '_function_file',
                  '_transform', '_angle_basis', '_front_diffuse_reflectance',
                  '_back_diffuse_reflectance', '_diffuse_transmittance')
 
     # TODO(): compress file content: https://stackoverflow.com/a/15529390/4394669
     def __init__(self, bsdf_file, name=None, up_orientation=None, thickness=0,
                  modifier='void', function_file='.', transform=None, angle_basis=None,
                  dependencies=None):
-        """Create BSDF material.
-
-        Args:
-            bsdf_file: Path to an xml file. Data will NOT be cached in memory.
-            up_orientation: (x, y ,z) vector that sets the hemisphere that the
-                BSDF material faces.  For materials that are symmetrical about
-                the face plane (like non-angled venetian blinds), this can be
-                any vector that is not perfectly normal to the face. For
-                asymmetrical materials like angled venetian blinds, this variable
-                should be coordinated with the direction the face are facing.
-                The default is set to (0.01, 0.01, 1.00), which should hopefully
-                not be perpendicular to any typical face.
-            thickness: Optional number to set the thickness of the BSDF material.
-                (default: 0).
-            modifier: Material modifier (Default: 'void').
-            function_file: Optional input for function file (Default: .).
-            transform: Optional transform input to to scale the thickness and reorient
-                the up vector (default: None).
-            angle_basis: BSDF file angle basis. If not provided by user honeybee tries to
-                find it by parsing BSDF file itself.
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-
-        """
+        """Create BSDF material."""
         name = name or '.'.join(os.path.split(bsdf_file)[-1].split('.')[:-1])
 
         Material.__init__(self, name, modifier=modifier,
                           dependencies=dependencies)
 
         self.bsdf_file = bsdf_file
         self.angle_basis = angle_basis
@@ -100,15 +119,15 @@
 
         if self.front_diffuse_reflectance is not None:
             self._values[2] = list(self.front_diffuse_reflectance)
 
             if self.back_diffuse_reflectance is not None:
                 for v in self.back_diffuse_reflectance:
                     self._values[2].append(v)
-            
+
             if self.diffuse_transmittance is not None:
                 for v in self.diffuse_transmittance:
                     self._values[2].append(v)
 
     @property
     def bsdf_file(self):
         """Path to BSDF file."""
@@ -256,22 +275,22 @@
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize a BSDF from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "BSDF", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "BSDF",  # primitive type
+            "name": "",  # primitive name
+            "values": []  # values,
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != 'BSDF':
             raise ValueError(
                 'Type must be %s not %s.' % ('BSDF', primitive_dict['type'])
             )
@@ -290,18 +309,18 @@
             transform=values[6] if len(values) == 7 else None,
             angle_basis=None,
             dependencies=dependencies
         )
 
         # this might look redundant but it is NOT. see glass for explanation.
         cls_.values = primitive_dict['values']
-        
+
         if not extra_values:
             return cls_
-        
+
         values_length = len(extra_values)
         assert values_length in (3, 6, 9), \
             'Length of real values should be 3, 6 or 9 not %d.' % values_length
 
         if values_length == 3:
             cls_.front_diffuse_reflectance = extra_values
         elif values_length == 6:
@@ -318,28 +337,28 @@
     def from_dict(cls, data, folder='.'):
         """Initialize a BSDF from a dictionary.
 
         Args:
             data: A dictionary in the format below.
             folder: Path to a destination folder to save the bsdf file.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // material modifier (Default: "void")
-                "type": "BSDF", // Material type
-                "name": string, // Material Name
-                "up_orientation": [number, number, number],
-                "thickness": number, // default: 0
-                "function_file": string, // default: '.'
-                "transform": string, // default: None
-                "bsdf_data": bytes, // bsdf file data as bytes
-                "front_diffuse_reflectance": [number, number, number],  // optional
-                "back_diffuse_reflectance": [number, number, number],  // optional
-                "diffuse_transmittance": [number, number, number],  // optional
+            "modifier": "",  # material modifier (Default: "void")
+            "type": "BSDF",  # Material type
+            "name": string,  # Material Name
+            "up_orientation": [number, number, number],
+            "thickness": number,  # default: 0
+            "function_file": string,  # default: '.'
+            "transform": string,  # default: None
+            "bsdf_data": bytes,  # bsdf file data as bytes
+            "front_diffuse_reflectance": [number, number, number],  # optional
+            "back_diffuse_reflectance": [number, number, number],  # optional
+            "diffuse_transmittance": [number, number, number]  # optional
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != 'BSDF':
             raise ValueError(
                 'Type must be %s not %s.' % ('BSDF', data['type'])
             )
@@ -347,15 +366,15 @@
 
         if not os.path.isdir(folder):
             os.makedirs(folder)
 
         fp = os.path.join(folder, '%s.xml' % data['name'])
         # write bytes to xml file
         cls.decompress_bytes_to_file(data['bsdf_data'], fp)
-        
+
         uo_dict = data['up_orientation']
         cls_ = cls(
             bsdf_file=fp,
             name=data['name'],
             up_orientation=[uo_dict['x'], uo_dict['y'], uo_dict['z']],
             thickness=data['thickness'],
             modifier=modifier,
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/light.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/light.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,33 +4,44 @@
 """
 
 from .materialbase import Material
 import honeybee.typing as typing
 
 
 class Light(Material):
-    """Radiance Light material."""
+    """Radiance Light material.
+
+    Args:
+        name: Material name as a string. The name should not have whitespaces or
+            special characters.
+        r_emittance: A positive value for the Red channel of the light (default: 0).
+        g_emittance: A positive value for the Green channel of the light (default: 0).
+        b_emittance: A positive value for the Blue channel of the light (default: 0).
+        modifier: Material modifier. The default value is void.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * r_emittance
+        * g_emittance
+        * b_emittance
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+    """
 
     __slots__ = ('_r_emittance', '_g_emittance', '_b_emittance')
 
     def __init__(self, name, r_emittance=0, g_emittance=0, b_emittance=0, modifier='void',
                  dependencies=None):
-        """Radiance Light material.
-
-        Args:
-            name: Material name as a string. The name should not have whitespaces or
-                special characters.
-            r_emittance: A positive value for the Red channel of the light (default: 0).
-            g_emittance: A positive value for the Green channel of the light (default: 0).
-            b_emittance: A positive value for the Blue channel of the light (default: 0).
-            modifier: Material modifier. The default value is void.
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-        """
+        """Radiance Light material."""
         Material.__init__(self, name, modifier=modifier,
                           dependencies=dependencies)
         self.r_emittance = r_emittance
         self.g_emittance = g_emittance
         self.b_emittance = b_emittance
         self._update_values()
 
@@ -85,35 +96,38 @@
                 between 0 and 1 (Default: 0).
             modifier: Material modifier (Default: "void").
             dependencies: A list of primitives that this primitive depends on. This
                 argument is only useful for defining advanced primitives where the
                 primitive is defined based on other primitives. (Default: [])
 
         Usage:
+
+        .. code-block:: python
+
             sample_light = Light.from_single_value("sample_light", 1)
             print(sample_light)
         """
         return cls(name, r_emittance=rgb, g_emittance=rgb, b_emittance=rgb,
                    modifier=modifier, dependencies=dependencies)
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize Light from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "light", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "light",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (
                     cls.__name__.lower(), primitive_dict['type'])
@@ -138,24 +152,24 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize Light from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "name": "", // Material Name
-                "type": "light", // primitive type
-                "r_emittance": float, // A positive value for the Red channel of the glow
-                "g_emittance": float, // A positive value for the Green channel of the glow
-                "b_emittance": float, // A positive value for the Blue channel of the glow
-                "radius": float, // Maximum radius for shadow testing
-                "dependencies: []
+            "name": "",  # Material Name
+            "type": "light",  # primitive type
+            "r_emittance": float,  # A positive value for the Red channel of the glow
+            "g_emittance": float,  # A positive value for the Green channel of the glow
+            "b_emittance": float,  # A positive value for the Blue channel of the glow
+            "radius": float,  # Maximum radius for shadow testing
+            "dependencies: []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                                              data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/mist.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/mist.py`

 * *Files 16% similar despite different names*

```diff
@@ -10,37 +10,37 @@
     """Radiance Mist Material.
 
     Mist is a virtual material used to delineate a volume of participating atmosphere. A
     list of important light sources may be given, along with an extinction coefficient,
     scattering albedo and scattering eccentricity parameter. The light sources named by
     the string argument list will be tested for scattering within the volume. Sources are
     identified by name, and virtual light sources may be indicated by giving the relaying
-    object followed by '>' followed by the source, i.e:
+    object followed by '>' followed by the source, i.e::
 
            3  source1  mirror1>source10  mirror2>mirror1>source3
 
     Normally, only one source is given per mist material, and there is an upper limit of
     32 to the total number of active scattering sources. The extinction coefficient, if
     given, is added the the global coefficient set on the command line. Extinction is in
     units of 1/distance (distance based on the world coordinates), and indicates the
     proportional loss of radiance over one unit distance. The scattering albedo, if
     present, will override the global setting within the volume. An albedo of 0 0 0 means
     a perfectly absorbing medium, and an albedo of 1 1 1 means a perfectly scattering
     medium (no absorption). The scattering eccentricity parameter will likewise override
     the global setting if it is present. Scattering eccentricity indicates how much
     scattered light favors the forward direction, as fit by the Henyey-Greenstein
-    function:
+    function::
 
         P(theta) = (1 - g*g) / (1 + g*g - 2*g*cos(theta))^1.5
 
     A perfectly isotropic scattering medium has a g parameter of 0, and a highly
     directional material has a g parameter close to 1. Fits to the g parameter may be
     found along with typical extinction coefficients and scattering albedos for various
     atmospheres and cloud types in USGS meteorological tables. (A pattern will be applied
-    to the extinction values.)
+    to the extinction values.)::
 
         mod mist id
         N src1 src2 .. srcN
         0
         0|3|6|7 [ rext gext bext [ ralb galb balb [ g ] ] ]
 
     There are two usual uses of the mist type. One is to surround a beam from a spotlight
@@ -52,11 +52,33 @@
     rendering parameters to control the atmosphere. The second application is to model
     clouds or other localized media. Complex boundary geometry may be used to give shape
     to a uniform medium, so long as the boundary encloses a proper volume. Alternatively,
     a pattern may be used to set the line integral value through the cloud for a ray
     entering or exiting a point in a given direction. For this application, it is best if
     cloud volumes do not overlap each other, and opaque objects contained within them may
     not be illuminated correctly unless the line integrals consider enclosed geometry.
+
+    Args:
+        name: Primitive name as a string. Cannot contain white spaces or special
+            characters.
+        modifier: Modifier. It can be primitive, mixture, texture or pattern.
+            (Default: "void").
+        values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
+            refer to a line number in the radiance primitve definitions and the
+            values in each array correspond to values occurring within each line.
+        is_opaque: A boolean to indicate whether this primitive is opaque.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives that are
+            defined based on other primitives. (Default: []).
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+        * is_opaque
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/__init__.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/material/glow.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/material/glow.py`

 * *Files 5% similar despite different names*

```diff
@@ -5,39 +5,51 @@
 from __future__ import division
 
 from .materialbase import Material
 import honeybee.typing as typing
 
 
 class Glow(Material):
-    """Create glow material."""
+    """Create glow material.
+
+    Args:
+        name: Material name as a string. The name should not have whitespaces or
+            special characters.
+        r_emittance: A positive value for the Red channel of the glow (default: 0).
+        g_emittance: A positive value for the Green channel of the glow (default: 0).
+        b_emittance: A positive value for the Blue channel of the glow (default: 0).
+        max_radius: Maximum radius for shadow testing (default: 0). If maxrad is
+            zero, then the surface will never be tested for shadow, although it may
+            participate in an interreflection calculation. If maxrad is negative,
+            then the surface will never contribute to scene illumination. Glow
+            sources will never illuminate objects on the other side of an illum
+            surface. This provides a convenient way to illuminate local light fixture
+            geometry without overlighting nearby objects.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * r_emittance
+        * g_emittance
+        * b_emittance
+        * max_radius
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+    """
 
     __slots__ = ('_r_emittance', '_g_emittance', '_b_emittance', '_max_radius')
 
     def __init__(self, name, r_emittance=0.0, g_emittance=0.0, b_emittance=0.0,
                  max_radius=0.0, modifier='void', dependencies=None):
-        """Init Glow material.
-
-        args:
-            name: Material name as a string. The name should not have whitespaces or
-                special characters.
-            r_emittance: A positive value for the Red channel of the glow (default: 0).
-            g_emittance: A positive value for the Green channel of the glow (default: 0).
-            b_emittance: A positive value for the Blue channel of the glow (default: 0).
-            max_radius: Maximum radius for shadow testing (default: 0). If maxrad is
-                zero, then the surface will never be tested for shadow, although it may
-                participate in an interreflection calculation. If maxrad is negative,
-                then the surface will never contribute to scene illumination. Glow
-                sources will never illuminate objects on the other side of an illum
-                surface. This provides a convenient way to illuminate local light fixture
-                geometry without overlighting nearby objects.
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-        """
+        """Init Glow material."""
         Material.__init__(self, name, modifier=modifier,
                           dependencies=dependencies)
         self.r_emittance = r_emittance
         self.g_emittance = g_emittance
         self.b_emittance = b_emittance
         self.max_radius = max_radius
         self._update_values()
@@ -82,15 +94,15 @@
 
     @b_emittance.setter
     def b_emittance(self, value):
         self._b_emittance = typing.float_positive(value)
 
     @property
     def max_radius(self):
-        """Maximum radius for shadow testing (default: 0).
+        """Maximum radius for shadow testing (default is 0).
 
         If maxrad is zero, then the surface will never be tested for shadow, although
         it may participate in an interreflection calculation. If maxrad is negative, then
         the surface will never contribute to scene illumination. Glow sources will
         never illuminate objects on the other side of an illum surface. This
         provides a convenient way to illuminate local light fixture geometry without
         overlighting nearby objects.
@@ -120,35 +132,38 @@
                 provides a convenient way to illuminate local light fixture geometry without
                 overlighting nearby objects.
             dependencies: A list of primitives that this primitive depends on. This
                 argument is only useful for defining advanced primitives where the
                 primitive is defined based on other primitives. (Default: [])
 
         Usage:
+
+        .. code-block:: python
+
             sample_glow = Glow.from_single_value("sample_glow", 100)
             print(sample_glow)
         """
         return cls(name, r_emittance=rgb, g_emittance=rgb, b_emittance=rgb,
             max_radius=max_radius, modifier=modifier, dependencies=dependencies)
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize Glow from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "glow", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "glow",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (
                     cls.__name__.lower(), primitive_dict['type'])
@@ -174,24 +189,24 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize Glow from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "name": "", // Material Name
-                "type": "glow", // primitive type
-                "r_emittance": float, // A positive value for the Red channel of the glow
-                "g_emittance": float, // A positive value for the Green channel of the glow
-                "b_emittance": float, // A positive value for the Blue channel of the glow
-                "max_radius": float, // Maximum radius for shadow testing
-                "dependencies: []
+            "name": "",  # Material Name
+            "type": "glow",  # primitive type
+            "r_emittance": float,  # A positive value for the Red channel of the glow
+            "g_emittance": float,  # A positive value for the Green channel of the glow
+            "b_emittance": float,  # A positive value for the Blue channel of the glow
+            "max_radius": float,  # Maximum radius for shadow testing
+            "dependencies: []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                                              data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/colortext.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/colortext.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,35 +12,38 @@
     Colortext is dichromatic writing in a polygonal font. The font is defined in an
     auxiliary file, such as helvet.fnt. The text itself is also specified in a separate
     file, or can be part of the material arguments. The character size, orientation,
     aspect ratio and slant is determined by right and down motion vectors. The upper left
     origin for the text block as well as the foreground and background colors must also
     be given.
 
+    .. code-block:: shell
+
         mod colortext id
         2 fontfile textfile
         0
         15+
                 Ox Oy Oz
                 Rx Ry Rz
                 Dx Dy Dz
                 rfore gfore bfore
                 rback gback bback
                 [spacing]
 
-or:
+    or:
+
+    .. code-block:: shell
 
         mod colortext id
         2+N fontfile . This is a line with N words ...
         0
         15+
                 Ox Oy Oz
                 Rx Ry Rz
                 Dx Dy Dz
                 rfore gfore bfore
                 rback gback bback
                 [spacing]
-
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/patternbase.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/patternbase.py`

 * *Files 26% similar despite different names*

```diff
@@ -8,14 +8,26 @@
 from ..modifierbase import Modifier
 
 
 class Pattern(Modifier):
     """Base class for Radiance patterns.
 
     Patterns are used to modify the reflectance of materials.
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_material
+        * is_texture
+        * is_pattern
+        * is_mixture
+        * is_opaque
     """
     __slots__ = ()
 
     @property
     def is_pattern(self):
         """Get a boolean noting whether this object is a pattern modifier."""
         return True
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/colorpict.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/colorpict.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,14 +11,16 @@
 
     Colorpict is a special case of colordata, where the pattern is a two-dimensional
     image stored in the RADIANCE picture format. The dimensions of the image data are
     determined by the picture such that the smaller dimension is always 1, and the
     other is the ratio between the larger and the smaller. For example, a 500x338
     picture would have coordinates (u,v) in the rectangle between (0,0) and (1.48,1).
 
+    .. code-block:: shell
+
         mod colorpict id
         7+
                 rfunc gfunc bfunc pictfile
                 funcfile u v transform
         0
         m A1 A2 .. Am
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/colordata.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/colordata.py`

 * *Files 12% similar despite different names*

```diff
@@ -14,14 +14,16 @@
     coordinates used to look up and interpolate the data are defined in another auxiliary
     file. The interpolated data values are modified by functions of one or three
     variables. If the functions are of one variable, then they are passed the
     corresponding color component (red or green or blue). If the functions are of three
     variables, then they are passed the original red, green, and blue values as
     parameters.
 
+    .. code-block:: shell
+
         mod colordata id
         7+n+
                 rfunc gfunc bfunc rdatafile gdatafile bdatafile
                 funcfile x1 x2 .. xn transform
         0
         m A1 A2 .. Am
     """
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/brightdata.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/brightdata.py`

 * *Files 22% similar despite different names*

```diff
@@ -7,14 +7,16 @@
 
 # TODO: Implement the class. It's currently only a generic Radiance Primitive
 class Brightdata(Pattern):
     """Radiance Brightdata Material.
 
     Brightdata is like colordata, except monochromatic.
 
+    .. code-block:: shell
+
         mod brightdata id
         3+n+
                 func datafile
                 funcfile x1 x2 .. xn transform
         0
         m A1 A2 .. Am
     """
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/pattern/brighttext.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/pattern/brighttext.py`

 * *Files 14% similar despite different names*

```diff
@@ -7,26 +7,30 @@
 
 # TODO: Implement the class. It's currently only a generic Radiance Primitive
 class Brighttext(Pattern):
     """Radiance Brighttext Pattern.
 
     Brighttext is like colortext, but the writing is monochromatic.
 
+    .. code-block:: shell
+
         mod brighttext id
         2 fontfile textfile
         0
         11+
                 Ox Oy Oz
                 Rx Ry Rz
                 Dx Dy Dz
                 foreground background
                 [spacing]
 
     or:
 
+    .. code-block:: shell
+
         mod brighttext id
         2+N fontfile . This is a line with N words ...
         0
         11+
                 Ox Oy Oz
                 Rx Ry Rz
                 Dx Dy Dz
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixpict.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixdata.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,26 +1,25 @@
-"""Radiance Mixpict Mixture.
+"""Radiance Mixdata Mixture.
 
-http://radsite.lbl.gov/radiance/refer/ray.html#Mixpict
+http://radsite.lbl.gov/radiance/refer/ray.html#Mixdata
 """
 from .mixturebase import Mixture
 
 
 # TODO: Implement the class. It's currently only a generic Radiance Primitive
-class Mixpict(Mixture):
-    """Radiance Mixpict Material.
+class Mixdata(Mixture):
+    """Radiance Mixdata Material.
 
-    Mixpict combines two modifiers based on a picture:
+    Mixdata combines two modifiers using an auxiliary data file:
 
-        mod mixpict id
-        7+
-                foreground background func pictfile
-                funcfile u v transform
+    .. code-block:: shell
+
+        mod mixdata id
+        5+n+
+                foreground background func datafile
+                funcfile x1 x2 .. xn transform
         0
         m A1 A2 .. Am
-
-    The mixing coefficient function "func" takes three arguments, the red, green and
-    blue values corresponding to the pixel at (u,v).
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixturebase.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixturebase.py`

 * *Files 26% similar despite different names*

```diff
@@ -6,14 +6,22 @@
 
 http://radsite.lbl.gov/radiance/refer/ray.html#Mixtures
 """
 from ..modifierbase import Modifier
 
 
 class Mixture(Modifier):
-    """Base class for Radiance mixtures."""
+    """Base class for Radiance mixtures.
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_mixture
+    """
     __slots__ = ()
 
     @property
     def is_mixture(self):
         """Get a boolean noting whether this object is a mixture modifier."""
         return True
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixfunc.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixfunc.py`

 * *Files 15% similar despite different names*

```diff
@@ -7,14 +7,16 @@
 
 # TODO: Implement the class. It's currently only a generic Radiance Primitive
 class Mixfunc(Mixture):
     """Radiance Mixfunc Material.
 
     A mixfunc mixes two modifiers procedurally. It is specified as follows:
 
+    .. code-block:: shell
+
         mod mixfunc id
         4+ foreground background vname funcfile transform
         0
         n A1 A2 .. An
 
     Foreground and background are modifier names that must be defined earlier in the
     scene description. If one of these is a material, then the modifier of the mixfunc
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/mixture/mixtext.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/mixture/mixtext.py`

 * *Files 18% similar despite different names*

```diff
@@ -7,25 +7,29 @@
 
 # TODO: Implement the class. It's currently only a generic Radiance Primitive
 class Mixtext(Mixture):
     """Radiance Mixtext Material.
 
     Mixtext uses one modifier for the text foreground, and one for the background:
 
+    .. code-block:: shell
+
         mod mixtext id
         4 foreground background fontfile textfile
         0
         9+
                 Ox Oy Oz
                 Rx Ry Rz
                 Dx Dy Dz
                 [spacing]
 
     or:
 
+    .. code-block:: shell
+
         mod mixtext id
         4+N
                 foreground background fontfile .
                 This is a line with N words ...
         0
         9+
                 Ox Oy Oz
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/texdata.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/texdata.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,14 +12,16 @@
 class Texdata(Texture):
     """Radiance Texdata Material.
 
     A texdata texture uses three data files to get the surface normal perturbations. The
     variables xfunc, yfunc and zfunc take three arguments each from the interpolated
     values in xdfname, ydfname and zdfname.
 
+    .. code-block:: shell
+
         mod texdata id
         8+ xfunc yfunc zfunc xdfname ydfname zdfname vfname x0 x1 .. xf
         0
         n A1 A2 .. An
 
     """
     __slots__ = ()
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/texturebase.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/texturebase.py`

 * *Files 18% similar despite different names*

```diff
@@ -5,14 +5,23 @@
 
 http://radsite.lbl.gov/radiance/refer/ray.html#Textures
 """
 from ..modifierbase import Modifier
 
 
 class Texture(Modifier):
-    """Base class for Radiance texture (Texfunc, Texdata)."""
+    """Base class for Radiance texture (Texfunc, Texdata).
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_modifier
+        * is_texture
+    """
     __slots__ = ()
 
     @property
     def is_texture(self):
         """Get a boolean noting whether this object is a texture modifier."""
         return True
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifier/texture/texfunc.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifier/texture/texfunc.py`

 * *Files 21% similar despite different names*

```diff
@@ -10,14 +10,16 @@
 
 # TODO: Implement the class. It's currently only a generic Radiance Primitive
 class Texfunc(Texture):
     """Radiance Texfunc Material.
 
     A texfunc uses an auxiliary function file to specify a procedural texture:
 
+    .. code-block:: shell
+
         mod texfunc id
         4+ xpert ypert zpert funcfile transform
         0
         n A1 A2 .. An
     """
     __slots__ = ()
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lib/_loadmodifiersets.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lib/_loadmodifiersets.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lib/data/modifiersets/default.json` & `honeybee-radiance-1.9.2/honeybee_radiance/lib/data/modifiersets/default.json`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lib/data/modifiers/default.mat` & `honeybee-radiance-1.9.2/honeybee_radiance/lib/data/modifiers/default.mat`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lib/_loadmodifiers.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lib/_loadmodifiers.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lib/modifiers.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lib/modifiers.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lib/modifiersets.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lib/modifiersets.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/modifierset.py` & `honeybee-radiance-1.9.2/honeybee_radiance/modifierset.py`

 * *Files 6% similar despite different names*

```diff
@@ -48,14 +48,33 @@
 @lockable
 class ModifierSet(object):
     """Set containting all radiance modifiers needed to create a radiance model.
 
     ModifierSets can be used to establish templates that are applied broadly
     across a Model, like a color scheme used consistently throughout a building.
 
+
+    Args:
+        name: Text string for modifier set name.
+        wall_set: An optional WallSet object for this ModifierSet.
+            If None, it will be the honeybee generic default WallSet.
+        floor_set: An optional FloorSet object for this ModifierSet.
+            If None, it will be the honeybee generic default FloorSet.
+        roof_ceiling_set: An optional RoofCeilingSet object for this ModifierSet.
+            If None, it will be the honeybee generic default RoofCeilingSet.
+        aperture_set: An optional ApertureSet object for this ModifierSet.
+            If None, it will be the honeybee generic default ApertureSet.
+        door_set: An optional DoorSet object for this ModifierSet.
+            If None, it will be the honeybee generic default DoorSet.
+        shade_set: An optional ShadeSet object for this ModifierSet.
+            If None, it will be the honeybee generic default ShadeSet.
+        air_boundary_modifier: An optional Modifier to be used for all Faces with
+            an AirBoundary face type. If None, it will be the honyebee generic
+            air wall modifier.
+
     Properties:
         * name
         * wall_set
         * floor_set
         * roof_ceiling_set
         * aperture_set
         * door_set
@@ -70,34 +89,15 @@
     __slots__ = ('_name', '_wall_set', '_floor_set', '_roof_ceiling_set',
                  '_aperture_set', '_door_set', '_shade_set', '_air_boundary_modifier',
                  '_locked')
 
     def __init__(self, name, wall_set=None, floor_set=None, roof_ceiling_set=None,
                  aperture_set=None, door_set=None, shade_set=None,
                  air_boundary_modifier=None):
-        """Initialize radiance modifier set.
-
-        Args:
-            name: Text string for modifier set name.
-            wall_set: An optional WallSet object for this ModifierSet.
-                If None, it will be the honeybee generic default WallSet.
-            floor_set: An optional FloorSet object for this ModifierSet.
-                If None, it will be the honeybee generic default FloorSet.
-            roof_ceiling_set: An optional RoofCeilingSet object for this ModifierSet.
-                If None, it will be the honeybee generic default RoofCeilingSet.
-            aperture_set: An optional ApertureSet object for this ModifierSet.
-                If None, it will be the honeybee generic default ApertureSet.
-            door_set: An optional DoorSet object for this ModifierSet.
-                If None, it will be the honeybee generic default DoorSet.
-            shade_set: An optional ShadeSet object for this ModifierSet.
-                If None, it will be the honeybee generic default ShadeSet.
-            air_boundary_modifier: An optional Modifier to be used for all Faces with
-                an AirBoundary face type. If None, it will be the honyebee generic
-                air wall modifier.
-        """
+        """Initialize radiance modifier set."""
         self._locked = False  # unlocked by default
         self.name = name
         self.wall_set = wall_set
         self.floor_set = floor_set
         self.roof_ceiling_set = roof_ceiling_set
         self.aperture_set = aperture_set
         self.door_set = door_set
@@ -337,19 +337,34 @@
     def from_dict(cls, data):
         """Create a ModifierSet from a dictionary.
 
         Note that the dictionary must be a non-abridged version for this
         classmethod to work.
 
         Args:
-            data: Dictionary describing the ModifierSet.
+            data: Dictionary describing the ModifierSet in the following format.
+
+        .. code-block:: python
+
+            {
+            'type': 'ModifierSet',
+            'name': str,  # ModifierSet name
+            'wall_set': {},  # WallSet dictionary
+            'floor_set': {},  # FloorlSet dictionary
+            'roof_ceiling_set': {},  # RoofCeilingSet dictionary
+            'aperture_set': {},  # ApertureSet dictionary
+            'door_set': {},  # DoorSet dictionary
+            'shade_set': {},  # ShadeSet dictionary
+            'air_boundary_modifier': {},  # AirBoundarySet dictionary
+            'modifiers': []  # A list of Honeybee Radiance Modifier dictionaries
+            }
         """
         assert data['type'] == 'ModifierSet', \
             'Expected ModifierSet. Got {}.'.format(data['type'])
-        
+
         # gather all modifier objects
         modifiers = {}
         for mod in data['modifiers']:
             modifiers[mod['name']] = dict_to_modifier(mod)
 
         # build each of the sub-sets
         wall_set, floor_set, roof_ceiling_set, aperture_set, door_set, shade_set, \
@@ -359,18 +374,32 @@
                    aperture_set, door_set, shade_set, air_boundary_mod)
 
     @classmethod
     def from_dict_abridged(cls, data, modifier_dict):
         """Create a ModifierSet from an abridged dictionary.
 
         Args:
-            data: A ModifierSetAbridged dictionary.
+            data: A ModifierSetAbridged dictionary with the fotmat below.
             modifier_dict: A dictionary with modifier names as keys and
                 honeybee modifier objects as values. These will be used to
-                assign the modifiers to the ModifierSet object.
+                assign the 4 to the ModifierSet object.
+
+        .. code-block:: python
+
+            {
+            'type': 'ModifierSetAbridged',
+            'name': str,  # ModifierSet name
+            'wall_set': {},  # WallSet dictionary
+            'floor_set': {},  # FloorlSet dictionary
+            'roof_ceiling_set': {},  # RoofCeilingSet dictionary
+            'aperture_set': {},  # ApertureSet dictionary
+            'door_set': {},  # DoorSet dictionary
+            'shade_set': {},  # ShadeSet dictionary
+            'air_boundary_modifier': {},  # AirBoundarySet dictionary
+            }
         """
         assert data['type'] == 'ModifierSetAbridged', \
             'Expected ModifierSetAbridged. Got {}.'.format(data['type'])
         wall_set, floor_set, roof_ceiling_set, aperture_set, door_set, shade_set, \
             air_boundary_mod = cls._get_subsets_from_abridged(data, modifier_dict)
         return cls(data['name'], wall_set, floor_set, roof_ceiling_set,
                    aperture_set, door_set, shade_set, air_boundary_mod)
@@ -435,15 +464,15 @@
 
     def _get_modifier_from_set(self, face_type_set, boundary_condition):
         """Get a specific modifier from a face_type_set."""
         if boundary_condition == 'Outdoors':
             return face_type_set.exterior_modifier
         else:
             return face_type_set.interior_modifier
-    
+
     @staticmethod
     def _get_subsets_from_abridged(data, modifiers):
         """Get subset objects from and abirdged dictionary."""
         wall_set = ModifierSet._make_modifier_subset(
             data, WallSet(), 'wall_set', modifiers)
         floor_set = ModifierSet._make_modifier_subset(
             data, FloorSet(), 'floor_set', modifiers)
@@ -454,15 +483,15 @@
         aperture_set = ModifierSet._make_aperture_subset(
             data, ApertureSet(), modifiers)
         door_set = ModifierSet._make_door_subset(data, DoorSet(), modifiers)
         if 'air_boundary_modifier' in data and data['air_boundary_modifier'] is not None:
             air_boundary_mod = modifiers[data['air_boundary_modifier']]
         else:
             air_boundary_mod = None
-        
+
         return wall_set, floor_set, roof_ceiling_set, aperture_set, door_set, \
             shade_set, air_boundary_mod
 
     @staticmethod
     def _make_modifier_subset(data, sub_set, sub_set_name, modifiers):
         """Make a WallSet, FloorSet, RoofCeilingSet, or ShadeSet from dictionary."""
         if sub_set_name in data:
@@ -555,27 +584,27 @@
 
     def __repr__(self):
         return 'Radiance Modifier Set: {}'.format(self.name)
 
 
 @lockable
 class _BaseSet(object):
-    """Base class for the sets assigned to Faces (WallSet, FloorSet, RoofCeilingSet)."""
+    """Base class for the sets assigned to Faces (WallSet, FloorSet, RoofCeilingSet).
+
+    Args:
+        exterior_modifier: A radiance modifier object for faces with an
+            Outdoors boundary condition.
+        interior_modifier: A radiance modifier object for faces with a boundary
+            condition other than Outdoors.
+    """
 
     __slots__ = ('_exterior_modifier', '_interior_modifier', '_locked')
 
     def __init__(self, exterior_modifier=None, interior_modifier=None):
-        """Initialize set.
-
-        Args:
-            exterior_modifier: A radiance modifier object for faces with an
-                Outdoors boundary condition.
-            interior_modifier: A radiance modifier object for faces with a boundary
-                condition other than Outdoors.
-        """
+        """Initialize set."""
         self._locked = False  # unlocked by default
         self.exterior_modifier = exterior_modifier
         self.interior_modifier = interior_modifier
 
     @property
     def exterior_modifier(self):
         """Get or set the modifier for exterior objects."""
@@ -634,15 +663,15 @@
                 for attr in attributes
                 }
         else:
             base = {
                 attr[1:]:getattr(self, attr[1:]).name
                 for attr in attributes
             }
-        
+
         base['type'] = self.__class__.__name__ + 'Abridged'
         return base
 
     def duplicate(self):
         """Get a copy of this set."""
         return self.__copy__()
 
@@ -742,40 +771,39 @@
     __slots__ = ()
 
 
 @lockable
 class ApertureSet(_BaseSet):
     """Set containing all radiance modifiers needed to for a radiance model's Apertures.
 
+    Args:
+        window_modifier: A modifier object for apertures with an Outdoors
+            boundary condition, False is_operable property, and Wall parent Face.
+        interior_modifier: A modifier object for apertures with a Surface
+            boundary condition.
+        skylight_modifier: : A modifier object for apertures with an Outdoors
+            boundary condition, False is_operable property, and a RoofCeiling
+            or Floor face type for their parent face.
+        operable_modifier: A modifier object for apertures with an Outdoors
+            boundary condition and a True is_operable property.
+
     Properties:
         * window_modifier
         * interior_modifier
         * skylight_modifier
         * operable_modifier
         * modifiers
         * modified_modifiers
         * is_modified
     """
     __slots__ = ('_skylight_modifier', '_operable_modifier')
 
     def __init__(self, window_modifier=None, interior_modifier=None,
                  skylight_modifier=None, operable_modifier=None):
-        """Initialize aperture set.
-
-        Args:
-            window_modifier: A modifier object for apertures with an Outdoors
-                boundary condition, False is_operable property, and Wall parent Face.
-            interior_modifier: A modifier object for apertures with a Surface
-                boundary condition.
-            skylight_modifier: : A modifier object for apertures with an Outdoors
-                boundary condition, False is_operable property, and a RoofCeiling
-                or Floor face type for their parent face.
-            operable_modifier: A modifier object for apertures with an Outdoors
-                boundary condition and a True is_operable property.
-        """
+        """Initialize aperture set."""
         _BaseSet.__init__(self, window_modifier, interior_modifier)
         self.skylight_modifier = skylight_modifier
         self.operable_modifier = operable_modifier
 
     @property
     def window_modifier(self):
         """Get or set the modifier for exterior fixed apertures in walls."""
@@ -804,15 +832,15 @@
         if self._skylight_modifier is None:
             return _default_modifiers[self.__class__.__name__]['skylight']
         return self._skylight_modifier
 
     @skylight_modifier.setter
     def skylight_modifier(self, value):
         self._skylight_modifier = self._validate_modifier(value)
-    
+
     def _to_dict(self, none_for_defaults=True):
         """Get the ModifierSet as a dictionary.
 
         Args:
             none_for_defaults: Boolean to note whether default modifiers in the
                 set should be included in detail (False) or should be None (True).
                 Default: True.
@@ -844,14 +872,25 @@
         )
 
 
 @lockable
 class DoorSet(_BaseSet):
     """Set containing all radiance modifiers needed to for an radiance model's Doors.
 
+    Args:
+        exterior_modifier: A window modifier object for apertures
+            with an Outdoors boundary condition.
+        interior_modifier: A window modifier object for apertures
+            with a Surface boundary condition.
+        exterior_glass_modifier:
+        interior_glass_modifier:
+        overhead_modifier: : A window modifier object for doors with an
+            Outdoors boundary condition and a RoofCeiling or Floor face type for
+            their parent face.
+
     Properties:
         * exterior_modifier
         * interior_modifier
         * exterior_glass_modifier
         * interior_glass_modifier
         * overhead_modifier
         * modifiers
@@ -860,27 +899,15 @@
     """
     __slots__ = ('_overhead_modifier', '_exterior_glass_modifier',
                  '_interior_glass_modifier')
 
     def __init__(self, exterior_modifier=None, interior_modifier=None,
                  exterior_glass_modifier=None, interior_glass_modifier=None,
                  overhead_modifier=None):
-        """Initialize door set.
-
-        Args:
-            exterior_modifier: A window modifier object for apertures
-                with an Outdoors boundary condition.
-            interior_modifier: A window modifier object for apertures
-                with a Surface boundary condition.
-            exterior_glass_modifier:
-            interior_glass_modifier:
-            overhead_modifier: : A window modifier object for doors with an
-                Outdoors boundary condition and a RoofCeiling or Floor face type for
-                their parent face.
-        """
+        """Initialize door set."""
         _BaseSet.__init__(self, exterior_modifier, interior_modifier)
         self.exterior_glass_modifier = exterior_glass_modifier
         self.interior_glass_modifier = interior_glass_modifier
         self.overhead_modifier = overhead_modifier
 
     @property
     def exterior_glass_modifier(self):
@@ -926,13 +953,13 @@
             self._interior_glass_modifier,
             self._overhead_modifier
         )
 
     def __repr__(self):
         return 'Door Modifier Set:\n Exterior: {}\n Interior: {}' \
             '\n Exterior Glass: {}\n Interior Glass: {}\n Overhead: {}'.format(
-            self.exterior_modifier.name,
-            self.interior_modifier.name,
-            self.exterior_glass_modifier.name,
-            self.interior_glass_modifier.name,
-            self.overhead_modifier.name
-        )
+                self.exterior_modifier.name,
+                self.interior_modifier.name,
+                self.exterior_glass_modifier.name,
+                self.interior_glass_modifier.name,
+                self.overhead_modifier.name
+                )
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/reader.py` & `honeybee-radiance-1.9.2/honeybee_radiance/reader.py`

 * *Files 2% similar despite different names*

```diff
@@ -39,14 +39,17 @@
     Args:
         file_path: Path to Radiance file
 
     Returns:
         A list of strings. Each string represents a different Radiance object.
 
     Usage:
+
+    .. code-block:: python
+
         rad_obj_strs = parse_from_file('some_file.rad')
     """
 
     assert os.path.isfile(file_path), "Can't find %s." % file_path
 
     with open(file_path, "r") as rad_file:
         return parse_from_string(rad_file.read())
@@ -158,18 +161,18 @@
 
 
 def parse_header(filepath):
     """Return radiance file header if exist.
 
     This method returns all the lines between `#?RADIANCE` and `FORMAT=*` and number of
     header lines including the white line after last header line.
-    
+
     Args:
         filepath: Full path to Radiance file.
-    
+
     Returns:
         line_count, header as a single multiline string
     """
     try:
         inf = open(filepath, 'r', encoding='utf-8')
     except:
         #python 2
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/view.py` & `honeybee-radiance-1.9.2/honeybee_radiance/view.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,16 +12,56 @@
 from honeybee_radiance_command.options import BoolOption, TupleOption, \
     StringOptionJoined, NumericOption
 
 
 class View(object):
     u"""A Radiance view.
 
+    Args:
+        position: Set the view position (-vp) to (x, y, z). This is the focal
+            point of a perspective view or the center of a parallel projection.
+            Default: (0, 0, 0)
+        direction: Set the view direction (-vd) vector to (x, y, z). The
+            length of this vector indicates the focal distance as needed by
+            the pixel depth of field (-pd) in rpict. Default: (0, 0, 1)
+        up_vector: Set the view up (-vu) vector (vertical direction) to
+            (x, y, z) default: (0, 1, 0).
+        type: Set view type (-vt) to one of the choices below.
+
+            * 0 - Perspective (v)
+            * 1 - Hemispherical fisheye (h)
+            * 2 - Parallel (l)
+            * 3 - Cylindrical panoroma (c)
+            * 4 - Angular fisheye (a)
+            * 5 - Planisphere [stereographic] projection (s)
+
+            For more detailed description about view types check rpict manual
+            page: (http://radsite.lbl.gov/radiance/man_html/rpict.1.html)
+        h_size: Set the view horizontal size (-vh). For a perspective
+            projection (including fisheye views), val is the horizontal field
+            of view (in degrees). For a parallel projection, val is the view
+            width in world coordinates.
+        v_size: Set the view vertical size (-vv). For a perspective
+            projection (including fisheye views), val is the horizontal field
+            of view (in degrees). For a parallel projection, val is the view
+            width in world coordinates.
+        shift: Set the view shift (-vs). This is the amount the actual
+            image will be shifted to the right of the specified view. This
+            option is useful for generating skewed perspectives or rendering
+            an image a piece at a time. A value of 1 means that the rendered
+            image starts just to the right of the normal view. A value of -1
+            would be to the left. Larger or fractional values are permitted
+            as well.
+        lift: Set the view lift (-vl) to a value. This is the amount the
+            actual image will be lifted up from the specified view.
+
     Usage:
 
+    .. code-block:: python
+
         v = View()
         # add a fore clip
         v.fore_clip = 100
         print(v)
 
         > -vtv -vp 0.000 0.000 0.000 -vd 0.000 0.000 1.000 -vu 0.000 1.000
            0.000 -vh 60.000 -vv 60.000 -vo 100.000
@@ -42,52 +82,15 @@
 
         > -vtv -vp 0.000 0.000 0.000 -vd 0.000 0.000 1.000 -vu 0.000 1.000
           0.000 -vh 29.341 -vv 32.204 -vs 0.500 -vl 0.500 -vo 100.000
     """
 
     def __init__(self, name, position=None, direction=None, up_vector=None, type='v',
                  h_size=60, v_size=60, shift=None, lift=None):
-        u"""Create a view.
-
-        Arg:
-            position: Set the view position (-vp) to (x, y, z). This is the focal
-                point of a perspective view or the center of a parallel projection.
-                Default: (0, 0, 0)
-            direction: Set the view direction (-vd) vector to (x, y, z). The
-                length of this vector indicates the focal distance as needed by
-                the pixel depth of field (-pd) in rpict. Default: (0, 0, 1)
-            up_vector: Set the view up (-vu) vector (vertical direction) to
-                (x, y, z) default: (0, 1, 0).
-            type: Set view type (-vt) to one of the choices below.
-                    0 - Perspective (v)
-                    1 - Hemispherical fisheye (h)
-                    2 - Parallel (l)
-                    3 - Cylindrical panoroma (c)
-                    4 - Angular fisheye (a)
-                    5 - Planisphere [stereographic] projection (s)
-                For more detailed description about view types check rpict manual
-                page: (http://radsite.lbl.gov/radiance/man_html/rpict.1.html)
-            h_size: Set the view horizontal size (-vh). For a perspective
-                projection (including fisheye views), val is the horizontal field
-                of view (in degrees). For a parallel projection, val is the view
-                width in world coordinates.
-            v_size: Set the view vertical size (-vv). For a perspective
-                projection (including fisheye views), val is the horizontal field
-                of view (in degrees). For a parallel projection, val is the view
-                width in world coordinates.
-            shift: Set the view shift (-vs). This is the amount the actual
-                image will be shifted to the right of the specified view. This
-                option is useful for generating skewed perspectives or rendering
-                an image a piece at a time. A value of 1 means that the rendered
-                image starts just to the right of the normal view. A value of -1
-                would be to the left. Larger or fractional values are permitted
-                as well.
-            lift: Set the view lift (-vl) to a value. This is the amount the
-                actual image will be lifted up from the specified view.
-        """
+        u"""Create a view."""
         self.name = name
         self._position = TupleOption(
             'vp', 'view position', position if position is not None else (0, 0, 0)
         )
         self._direction = TupleOption(
             'vd', 'view direction', direction if direction is not None else (0, 0, 1)
         )
@@ -119,18 +122,20 @@
         """Check if the view type is one of the fisheye views."""
         return self.type in ('h', 'a', 's')
 
     @property
     def type(self):
         """Set and get view type (-vt) to one of the choices below.
 
-        v - Perspective (v), h - Hemispherical fisheye (h),
-        l - Parallel (l),    c - Cylindrical panorma (c),
-        a - Angular fisheye (a),
-        s - Planisphere [stereographic] projection (s)
+            * v - Perspective (v)
+            * h - Hemispherical fisheye (h)
+            * l - Parallel (l)
+            * c - Cylindrical panorma (c)
+            * a - Angular fisheye (a)
+            * s - Planisphere [stereographic] projection (s)
         """
         return self._type
 
     @property
     def vt(self):
         """View type as a string in radiance format."""
         return self._type.to_radiance()
@@ -293,15 +298,15 @@
         and parallel view types. For fisheye view types, the clipping plane is
         actually a clipping sphere, centered on the view point with radius val.
         Objects in front of this imaginary surface will not be visible. This may
         be useful for seeing through walls (to get a longer perspective from an
         exterior view point) or for incremental rendering. A value of zero implies
         no foreground clipping. A negative value produces some interesting effects,
         since it creates an inverted image for objects behind the viewpoint.
-        """        
+        """
         return self._fore_clip
 
     @property
     def vo(self):
         """View fore clip as a string in radiance format."""
         return self._fore_clip.to_radiance()
 
@@ -330,15 +335,32 @@
 
     @aft_clip.setter
     def aft_clip(self, distance):
         self._aft_clip.value = distance
 
     @classmethod
     def from_dict(cls, view_dict):
-        """Create a view from a dictionary."""
+        """Create a view from a dictionary in the following format.
+
+        .. code-block:: python
+
+            {
+            'name': str,
+            'position': [],  # list with position value
+            'direction': [],  # list with direction value
+            'up_vector': [],  # list with up_vector value
+            'h_size': number,  # h_size.value
+            'v_size': number,  # v_size value
+            'shift': number,  # shift value
+            'lift': number,  # lift value
+            'type': number,  # type value
+            'fore_clip': number,  # fore_clip value
+            'aft_clip': number  # aft_clip value
+            }
+        """
 
         view = cls(
             name=view_dict['name'],
             position=view_dict['position'],
             direction=view_dict['direction'],
             up_vector=view_dict['up_vector'],
             h_size=view_dict['h_size'],
@@ -351,29 +373,29 @@
         view.aft_clip = view_dict['aft_clip']
 
         return view
 
     @classmethod
     def from_string(cls, name, view_string):
         """Create a view object from a string.
-        
+
         This method is similar to from_string method for radiance parameters with the
         difference that all the parameters that are not related to view will be ignored.
         """
         mapper = {
             'name': name, 'vp': 'position', 'vd': 'direction', 'vu': 'up_vector',
             'vh': 'h_size', 'vv': 'v_size', 'vs': 'shift', 'vl': 'lift',
             'vo': 'fore_clip', 'va': 'aft_clip'
         }
 
         base = {
             'name': name,
             'position': None,
             'direction': None,
-            'up_vector': None, 
+            'up_vector': None,
             'h_size': None,
             'v_size': None,
             'shift': None,
             'lift': None,
             'type': None,
             'fore_clip': None,
             'aft_clip': None
@@ -395,15 +417,15 @@
     @classmethod
     def from_file(self, file_path, name=None):
         """Create view from a view file.
 
         Args:
             file_path: Full path to view file.
             name: Optional name for this view. View name will be set to file name if not
-            provided.
+                provided.
         """
 
         if not os.path.isfile(file_path):
             raise IOError("Can't find {}.".format(file_path))
         name = name or os.path.split(os.path.splitext(file_path)[0])[-1]
 
         with open(file_path, 'r') as input_data:
@@ -424,15 +446,15 @@
             x, y,
             '-' if (self.fore_clip.to_radiance() + self.aft_clip.to_radiance() == '')
             else '+'
         )
 
     def dimension_x_y(self, x_res=None, y_res=None):
         """Get dimensions for this view as x, y.
-        
+
         Default values for x_res and y_res are set to match Radiance defaults.
         """
         # radiance default is 512
         x_res = int(x_res) if x_res is not None else 512
         y_res = int(y_res) if y_res is not None else 512
 
         if self.is_fisheye:
@@ -556,32 +578,32 @@
 
     def to_dict(self):
         """Translate view to a dictionary."""
         return {
             'name': self.name,
             'position': self.position.value,
             'direction': self.direction.value,
-            'up_vector': self.up_vector.value, 
+            'up_vector': self.up_vector.value,
             'h_size': self.h_size.value,
-            'v_size': self.v_size.value, 
+            'v_size': self.v_size.value,
             'shift': self.shift.value,
             'lift': self.lift.value,
-            'type': self.type.value, 
+            'type': self.type.value,
             'fore_clip': self.fore_clip.value,
             'aft_clip': self.aft_clip.value
         }
 
     def to_file(self, folder, file_name=None, mkdir=False):
         """Save view to a file.
 
         Args:
             folder: Target folder.
             file_name: Optional file name without extension (Default: self.name).
             mkdir: A boolean to indicate if the folder should be created in case it
-                doesn't exist already (Default: False). 
+                doesn't exist already (Default: False).
 
         Returns:
             Full path to newly created file.
         """
 
         name = file_name or self.name + '.vf'
         # add rvu before the view itself
@@ -603,15 +625,15 @@
         """
         view_up_vector = pv.Vector3D(*self.up_vector)
         view_position = pv.Point3D(*self.position)
         view_direction = pv.Vector3D(*self.direction)
         view_plane = plane.Plane(n=view_up_vector, o=view_position, x=view_direction)
         axis = pv.Vector3D(*axis) or view_up_vector
         position = pv.Point3D(*position) or view_position
-        
+
         rotated_plane = view_plane.rotate(axis, angle, position)
 
         self.position = rotated_plane.o
         self.direction = rotated_plane.x
         self.up_vector = rotated_plane.n
 
     def ToString(self):
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/ring.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/ring.py`

 * *Files 9% similar despite different names*

```diff
@@ -8,41 +8,51 @@
 
 class Ring(Geometry):
     """Radiance Ring.
 
     A ring is a circular disk given by its center, surface normal, and inner and outer
     radii:
 
+    .. code-block:: shell
+
         mod ring id
         0
         0
         8
                 xcent   ycent   zcent
                 xdir    ydir    zdir
                 r0      r1
 
+    Args:
+        name: Geometry name as a string. Do not use white space or special
+            character.
+        center_pt: Ring start center point as (x, y, z) (Default: (0, 0 ,0)).
+        normal_vector: Surface normal as (x, y, z) (Default: (0, 0 ,1)).
+        radius_inner: Ring inner radius as a number (Default: 5).
+        radius_outer: Ring outer radius as a number (Default: 10).
+        modifier: Geometry modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * center_pt
+        * normal_vector
+        * radius_inner
+        * radius_outer
+        * modifier
+        * dependencies
+        * values
     """
     __slots__ = ('_center_pt', '_normal_vector', '_radius_inner', '_radius_outer')
 
     def __init__(self, name, center_pt=None, normal_vector=None, radius_inner=5,
                  radius_outer=10, modifier=None, dependencies=None):
-        """Radiance Ring.
-
-        Args:
-            name: Geometry name as a string. Do not use white space or special
-                character.
-            center_pt: Ring start center point as (x, y, z) (Default: (0, 0 ,0)).
-            normal_vector: Surface normal as (x, y, z) (Default: (0, 0 ,1)).
-            radius_inner: Ring inner radius as a number (Default: 5).
-            radius_outer: Ring outer radius as a number (Default: 10).
-            modifier: Geometry modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-        """
+        """Radiance Ring."""
         Geometry.__init__(self, name, modifier=modifier)
         self.center_pt = center_pt or (0, 0, 0)
         self.normal_vector = normal_vector or (0, 0, 1)
         self.radius_inner = radius_inner if radius_inner is not None else 5
         self.radius_outer = radius_outer if radius_outer is not None else 10
 
         self._update_values()
@@ -52,67 +62,67 @@
         self._values[2] = \
             [self.center_pt[0], self.center_pt[1], self.center_pt[2],
              self.normal_vector[0], self.normal_vector[1], self.normal_vector[2],
              self.radius_inner, self.radius_outer]
 
     @property
     def center_pt(self):
-        """Ring start center point as (x, y, z) (Default: (0, 0 ,0))."""
+        """Ring start center point as (x, y, z). Default is (0, 0 ,0)."""
         return self._center_pt
 
     @center_pt.setter
     def center_pt(self, value):
         self._center_pt = tuple(float(v) for v in value)
         assert len(self._center_pt) == 3, \
             'Radiance Ring center point must have 3 values for (x, y, z).'
 
     @property
     def radius_inner(self):
-        """Ring inner radius as a number (Default: 5)."""
+        """Ring inner radius as a number (Default is 5)."""
         return self._radius_inner
 
     @radius_inner.setter
     def radius_inner(self, value):
         self._radius_inner = typing.float_positive(value)
 
     @property
     def normal_vector(self):
-        """Surface normal as (x, y, z) (Default: (0, 0 ,1))."""
+        """Surface normal as (x, y, z) (Default is (0, 0 ,1))."""
         return self._normal_vector
 
     @normal_vector.setter
     def normal_vector(self, value):
         self._normal_vector = tuple(float(v) for v in value)
         assert len(self._center_pt) == 3, \
             'Radiance Ring normal venctor must have 3 values for (x, y, z).'
 
     @property
     def radius_outer(self):
-        """Ring outer radius as a number (Default: 10)."""
+        """Ring outer radius as a number (Default is 10)."""
         return self._radius_outer
 
     @radius_outer.setter
     def radius_outer(self, value):
         self._radius_outer = typing.float_positive(value)
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize a Ring from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "ring", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default is "void")
+            "type": "ring",  # primitive type
+            "name": "",  # primitive name
+            "values": []  # values,
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
             )
@@ -136,25 +146,25 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize a Ring from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "type": "ring", // Geometry type
-                "modifier": {} or "void",
-                "name": "", // Geometry Name
-                "center_pt": (0, 0, 0),
-                "normal_vector": (0, 0, 1),
-                "radius_inner": float,
-                "radius_outer": float,
-                "dependencies": []
+            "type": "ring",  # Geometry type
+            "modifier": {} or "void",
+            "name": "",  # Geometry Name
+            "center_pt": (0, 0, 0),
+            "normal_vector": (0, 0, 1),
+            "radius_inner": float,
+            "radius_outer": float,
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                                              data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/cylinder.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/cylinder.py`

 * *Files 3% similar despite different names*

```diff
@@ -7,40 +7,50 @@
 
 
 class Cylinder(Geometry):
     """Radiance Cylinder.
 
     A cylinder is like a cone, but its starting and ending radii are equal.
 
+    .. code-block:: shell
+
         mod cylinder id
         0
         0
         7
                 x0      y0      z0
                 x1      y1      z1
                 rad
+
+    Args:
+        name: Geometry name as a string. Do not use white spaces or special
+            characters.
+        center_pt_start: Cylinder start center point as (x, y, z)
+            (Default: (0, 0 ,0)).
+        center_pt_end: Cylinder end center point as (x, y, z) (Default: (0, 0 ,10)).
+        radius: Cylinder start radius as a number (Default: 10).
+        modifier: Geometry modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * center_pt_start
+        * center_pt_end
+        * radius
+        * values
+        * modifier
+        * dependencies
     """
     __slots__ = ('_center_pt_start', '_center_pt_end', '_radius')
 
     def __init__(self, name, center_pt_start=None, center_pt_end=None, radius=10,
                  modifier=None, dependencies=None):
-        """Radiance Cylinder.
-
-        Args:
-            name: Geometry name as a string. Do not use white spaces or special
-                characters.
-            center_pt_start: Cylinder start center point as (x, y, z)
-                (Default: (0, 0 ,0)).
-            center_pt_end: Cylinder end center point as (x, y, z) (Default: (0, 0 ,10)).
-            radius: Cylinder start radius as a number (Default: 10).
-            modifier: Geometry modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-        """
+        """Radiance Cylinder."""
         Geometry.__init__(self, name, modifier=modifier, dependencies=dependencies)
         self.center_pt_start = center_pt_start or (0, 0, 0)
         self.center_pt_end = center_pt_end or (0, 0, 10)
         self.radius = radius if radius is not None else 10
         self._update_values()
 
     def _update_values(self):
@@ -48,58 +58,58 @@
         self._values[2] = \
             [self.center_pt_start[0], self.center_pt_start[1], self.center_pt_start[2],
              self.center_pt_end[0], self.center_pt_end[1], self.center_pt_end[2],
              self.radius]
 
     @property
     def center_pt_start(self):
-        """Cone start center point as (x, y, z) (Default: (0, 0 ,0))."""
+        """Cone start center point as (x, y, z). Default is (0, 0 ,0)."""
         return self._center_pt_start
-    
+
     @center_pt_start.setter
     def center_pt_start(self, value):
         self._center_pt_start = tuple(float(v) for v in value)
         assert len(self._center_pt_start) == 3, \
             'Radiance Cylinder center point must have 3 values for (x, y, z).'
 
     @property
     def radius(self):
-        """Cone start radius as a number (Default: 10)."""
+        """Cone start radius as a number. Default is 10."""
         return self._radius
-    
+
     @radius.setter
     def radius(self, value):
         self._radius = typing.float_positive(value)
 
     @property
     def center_pt_end(self):
-        """Cone end center point as (x, y, z) (Default: (0, 0 ,10))."""
+        """Cone end center point as (x, y, z), Default is (0, 0 ,10)."""
         return self._center_pt_end
-    
+
     @center_pt_end.setter
     def center_pt_end(self, value):
         self._center_pt_end = tuple(float(v) for v in value)
         assert len(self._center_pt_end) == 3, \
             'Radiance Cylinder center point must have 3 values for (x, y, z).'
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize a Cylinder from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "cylinder", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "cylinder",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
             )
@@ -122,24 +132,24 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize a Cylinder from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "type": "cylinder", // Geometry type
-                "modifier": {} or "void",
-                "name": "", // Geometry Name
-                "center_pt_start": (0, 0, 0),
-                "center_pt_end": (0, 0, 10),
-                "radius": float,
-                "dependencies": []
+            "type": "cylinder",  # Geometry type
+            "modifier": {} or "void",
+            "name": "",  # Geometry Name
+            "center_pt_start": (0, 0, 0),
+            "center_pt_end": (0, 0, 10),
+            "radius": float,
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                     data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/instance.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/instance.py`

 * *Files 6% similar despite different names*

```diff
@@ -9,14 +9,16 @@
 # geometry
 class Instance(Geometry):
     """Radiance Instance.
 
     An instance is a compound surface, given by the contents of an octree file (created
     by oconv).
 
+    .. code-block:: shell
+
         mod instance id
         1+ octree transform
         0
         0
 
     If the modifier is "void", then surfaces will use the modifiers given in the original
     description. Otherwise, the modifier specified is used in their place. The transform
@@ -27,12 +29,12 @@
     There are a number of important limitations to be aware of when using instances.
     First, the scene description used to generate the octree must stand on its own,
     without referring to modifiers in the parent description. This is necessary for
     oconv to create the octree. Second, light sources in the octree will not be
     incorporated correctly in the calculation, and they are not recommended. Finally,
     there is no advantage (other than convenience) to using a single instance of an
     octree, or an octree containing only a few surfaces. An xform command on the
-    subordinate description is preferred in such cases. 
+    subordinate description is preferred in such cases.
     """
     __slots__ = ()
 
     pass
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/source.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/source.py`

 * *Files 3% similar despite different names*

```diff
@@ -9,85 +9,97 @@
 class Source(Geometry):
     """Radiance Source.
 
     A source is not really a surface, but a solid angle. It is used for specifying light
     sources that are very distant. The direction to the center of the source and the
     number of degrees subtended by its disk are given as follows:
 
-    mod source id
-    0
-    0
-    4 xdir ydir zdir angle
+    .. code-block:: shell
+
+        mod source id
+        0
+        0
+        4 xdir ydir zdir angle
+
+    Args:
+        name: Geometry name as a string. Do not use white space or special
+            character.
+        direction: A vector to set source direction (x, y, z) (Default: (0, 0 ,-1)).
+        angle: Source solid angle (Default: 0.533).
+        modifier: Geometry modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * direction
+        * angle
+        * modifier
+        * dependencies
+        * values
+
+    Usage:
+
+    .. code-block:: python
+
+        source = Source("test_source", (0, 0, 10), 10)
+        print(source)
     """
     __slots__ = ('_direction', '_angle')
 
     def __init__(self, name, direction=None, angle=0.533, modifier=None,
                  dependencies=None):
-        """Radiance Source.
-
-        Args:
-            name: Geometry name as a string. Do not use white space or special
-                character.
-            direction: A vector to set source direction (x, y, z) (Default: (0, 0 ,-1)).
-            angle: Source solid angle (Default: 0.533).
-            modifier: Geometry modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-
-        Usage:
-            source = Source("test_source", (0, 0, 10), 10)
-            print(source)
-        """
+        """Radiance Source."""
         Geometry.__init__(self, name, modifier=modifier, dependencies=dependencies)
         self.direction = direction or (0, 0, -1)
         self.angle = angle if angle is not None else 0.533
 
         self._update_values()
 
     def _update_values(self):
         """update values dictionary."""
         self._values[2] = \
             [self.direction[0], self.direction[1], self.direction[2], self.angle]
 
     @property
     def direction(self):
-        """A vector to set source direction (x, y, z) (Default: (0, 0 ,-1))."""
+        """A vector to set source direction (x, y, z) (Default is (0, 0 ,-1))."""
         return self._direction
-    
+
     @direction.setter
     def direction(self, value):
         self._direction = tuple(float(v) for v in value)
         assert len(self._direction) == 3, \
             'Radiance Source direction must have 3 values for (x, y, z).'
 
     @property
     def angle(self):
-        """Source solid angle (Default: 0.533)."""
+        """Source solid angle. Default is 0.533."""
         return self._angle
-    
+
     @angle.setter
     def angle(self, value):
         self._angle = typing.float_positive(value)
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize a Source from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "source", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default is "void")
+            "type": "source",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
             )
@@ -109,23 +121,23 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize a Ring from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "type": "source", // Geometry type
-                "modifier": {} or "void",
-                "name": "", // Geometry Name
-                "direction": {"x": float, "y": float, "z": float},
-                "angle": float,
-                "dependencies": []
+            "type": "source",  # Geometry type
+            "modifier": {} or "void",
+            "name": "",  # Geometry Name
+            "direction": {"x": float, "y": float, "z": float},
+            "angle": float,
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                     data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/geometrybase.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/geometrybase.py`

 * *Files 18% similar despite different names*

```diff
@@ -9,14 +9,28 @@
 
 https://floyd.lbl.gov/radiance/refer/ray.html#Surfaces
 """
 from ..primitive import Primitive
 
 
 class Geometry(Primitive):
-    """Base class for Radiance geometries."""
+    """Base class for Radiance geometries.
+
+    Properties:
+        * name
+        * values
+        * modifier
+        * dependencies
+        * is_geometry
+        * is_modifier
+        * is_material
+        * is_texture
+        * is_pattern
+        * is_mixture
+        * is_opaque
+"""
     __slots__ = ()
 
     @property
     def is_geometry(self):
         """Get a boolean noting whether this object is a Radiance geometry."""
         return True
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/polygon.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/polygon.py`

 * *Files 3% similar despite different names*

```diff
@@ -9,82 +9,90 @@
     """Radiance Polygon.
 
     A polygon is given by a list of three-dimensional vertices, which are ordered
     counter-clockwise as viewed from the front side (into the surface normal). The last
     vertex is automatically connected to the first. Holes are represented in polygons as
     interior vertices connected to the outer perimeter by coincident edges (seams).
 
-    mod polygon id
-    0
-    0
-    3n
-            x1      y1      z1
-            x2      y2      z2
-            ...
-            xn      yn      zn
-    """
-    __slots__ = ('_vertices',)
+    .. code-block:: shell
 
-    def __init__(self, name, vertices, modifier=None, dependencies=None):
-        """Radiance Polygon.
+        mod polygon id
+        0
+        0
+        3n
+                x1      y1      z1
+                x2      y2      z2
+                ...
+                xn      yn      zn
+
+    Args:
+        name: Geometry name as a string. Do not use white space or special
+            character.
+        vertices: Minimum of three arrays, each with 3 (x, y, z) values for
+            vertices that make up the polygon. Vertices musct be ordered
+            counter-clockwise as viewed from the front side. The last vertex is
+            assumed to be connected to the first.
+        modifier: Geometry modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * vertices
+        * modifier
+        * dependencies
+        * values
 
-        Attributes:
-            name: Geometry name as a string. Do not use white space or special
-                character.
-            vertices: Minimum of three arrays, each with 3 (x, y, z) values for
-                vertices that make up the polygon. Vertices musct be ordered
-                counter-clockwise as viewed from the front side. The last vertex is
-                assumed to be connected to the first.
-            modifier: Geometry modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
+    Usage:
 
-        Usage:
+    .. code-block:: python
 
-            .. code-block:: python
+        polygon = Polygon("test_polygon", [(0, 0, 10), (10, 0, 10), (10, 0, 0)])
+        print(polygon)
+    """
+    __slots__ = ('_vertices',)
 
-            polygon = Polygon("test_polygon", [(0, 0, 10), (10, 0, 10), (10, 0, 0)])
-            print(polygon)
-        """
+    def __init__(self, name, vertices, modifier=None, dependencies=None):
+        """Radiance Polygon."""
         Geometry.__init__(self, name, modifier=modifier, dependencies=dependencies)
         self.vertices = vertices
         self._update_values()
 
     def _update_values(self):
         """update values dictionary."""
         self._values[2] = [v for pt in self.vertices for v in pt]
 
     @property
     def vertices(self):
         """List of Polygon vertices."""
         return self._vertices
-    
+
     @vertices.setter
     def vertices(self, vertices):
         self._vertices = tuple(tuple(float(v) for v in pt) for pt in vertices)
         assert len(self._vertices) > 2, 'Number of polygon vertices must be 3 or more.'
         for vert in self._vertices:
             assert len(vert) == 3, 'Polygon vertices must have 3 values for (x, y, z).'
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize a Polygon from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "polygon", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "polygon",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
             )
@@ -108,22 +116,22 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize a Polygon from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "type": "polygon", // Geometry type
-                "modifier": {} or "void",
-                "name": "", // Geometry Name
-                "vertices": [(0, 0, 10), (10, 0, 10), (10, 0, 0)],
-                "dependencies": []
+            "type": "polygon",  # Geometry type
+            "modifier": {} or "void",
+            "name": "",  # Geometry Name
+            "vertices": [(0, 0, 10), (10, 0, 10), (10, 0, 0)],
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                     data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/cone.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/cone.py`

 * *Files 10% similar despite different names*

```diff
@@ -9,41 +9,52 @@
 class Cone(Geometry):
     """Radiance Cone.
 
     A cone is a megaphone-shaped object. It is truncated by two planes perpendicular to
     its axis, and one of its ends may come to a point. It is given as two axis endpoints,
     and the starting and ending radii:
 
+    .. code-block:: shell
+
         mod cone id
         0
         0
         8
                 x0      y0      z0
                 x1      y1      z1
                 r0      r1
 
+    Args:
+        name: Geometry name as a string. Do not use white space or special
+            character.
+        center_pt_start: Cone start center point as (x, y, z) (Default: (0, 0 ,0)).
+        radius_start: Cone start radius as a number (Default: 10).
+        center_pt_end: Cone end center point as (x, y, z) (Default: (0, 0 ,10)).
+        radius_end: Cone end radius as a number (Default: 0).
+        modifier: Geometry modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * center_pt_start
+        * radius_start
+        * center_pt_end
+        * radius_end
+        * values
+        * modifier
+        * dependencies
+
     """
     __slots__ = ('_center_pt_start', '_radius_start', '_center_pt_end', '_radius_end')
 
     def __init__(self, name, center_pt_start=None, radius_start=10,
                  center_pt_end=None, radius_end=0, modifier=None, dependencies=None):
-        """Radiance Cone.
-
-        Attributes:
-            name: Geometry name as a string. Do not use white space or special
-                character.
-            center_pt_start: Cone start center point as (x, y, z) (Default: (0, 0 ,0)).
-            radius_start: Cone start radius as a number (Default: 10).
-            center_pt_end: Cone end center point as (x, y, z) (Default: (0, 0 ,10)).
-            radius_end: Cone end radius as a number (Default: 0).
-            modifier: Geometry modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
-        """
+        """Radiance Cone."""
         Geometry.__init__(self, name, modifier=modifier, dependencies=dependencies)
         self.center_pt_start = center_pt_start or (0, 0, 0)
         self.radius_start = radius_start if radius_start is not None else 10
         self.center_pt_end = center_pt_end or (0, 0, 10)
         self.radius_end = radius_end if radius_end is not None else 0
         self._update_values()
 
@@ -52,67 +63,67 @@
         self._values[2] = \
             [self.center_pt_start[0], self.center_pt_start[1], self.center_pt_start[2],
              self.center_pt_end[0], self.center_pt_end[1], self.center_pt_end[2],
              self.radius_start, self.radius_end]
 
     @property
     def center_pt_start(self):
-        """Cone start center point as (x, y, z) (Default: (0, 0 ,0))."""
+        """Cone start center point as (x, y, z). Default is (0, 0 ,0)."""
         return self._center_pt_start
-    
+
     @center_pt_start.setter
     def center_pt_start(self, value):
         self._center_pt_start = tuple(float(v) for v in value)
         assert len(self._center_pt_start) == 3, \
             'Radiance Cone center point must have 3 values for (x, y, z).'
 
     @property
     def radius_start(self):
-        """Cone start radius as a number (Default: 10)."""
+        """Cone start radius as a number. Default is 10."""
         return self._radius_start
-    
+
     @radius_start.setter
     def radius_start(self, value):
         self._radius_start = typing.float_positive(value)
 
     @property
     def center_pt_end(self):
-        """Cone end center point as (x, y, z) (Default: (0, 0 ,10))."""
+        """Cone end center point as (x, y, z). Default is (0, 0 ,10)."""
         return self._center_pt_end
-    
+
     @center_pt_end.setter
     def center_pt_end(self, value):
         self._center_pt_end = tuple(float(v) for v in value)
         assert len(self._center_pt_end) == 3, \
             'Radiance Cone center point must have 3 values for (x, y, z).'
 
     @property
     def radius_end(self):
-        """ Cone end radius as a number (Default: 0)."""
+        """ Cone end radius as a number. Default is 0."""
         return self._radius_end
-    
+
     @radius_end.setter
     def radius_end(self, value):
         self._radius_end = typing.float_positive(value)
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize a Cone from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "cone", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "cone",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
             )
@@ -136,25 +147,25 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize a Cone from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "type": "cone", // Geometry type
-                "modifier": {} or "void",
-                "name": "", // Geometry Name
-                "center_pt_start": (0, 0, 0),
-                "radius_start": float,
-                "center_pt_end": (0, 0, 10),
-                "radius_end": float,
-                "dependencies": []
+            "type": "cone",  # Geometry type
+            "modifier": {} or "void",
+            "name": "",  # Geometry Name
+            "center_pt_start": (0, 0, 0),
+            "radius_start": float,
+            "center_pt_end": (0, 0, 10),
+            "radius_end": float,
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                     data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/sphere.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/sphere.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,88 +5,97 @@
 from .geometrybase import Geometry
 import honeybee.typing as typing
 
 
 class Sphere(Geometry):
     """Radiance Sphere.
 
-    mod sphere id
-    0
-    0
-    4 xcent ycent zcent radius
-    """
-    __slots__ = ('_center_pt', '_radius')
+    .. code-block:: shell
 
-    def __init__(self, name, center_pt=None, radius=10, modifier=None,
-                 dependencies=None):
-        """Radiance Sphere.
+        mod sphere id
+        0
+        0
+        4 xcent ycent zcent radius
+
+    Args:
+        name: Geometry name as a string. Do not use white space or special
+            character.
+        center_pt: Sphere center point as (x, y, z) (Default: (0, 0 ,0)).
+        radius: Sphere radius as a number (Default: 10).
+        modifier: Geometry modifier (Default: "void").
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives where the
+            primitive is defined based on other primitives. (Default: [])
+
+    Properties:
+        * name
+        * center_pt
+        * radius
+        * modifier
+        * dependencies
+        * values
 
-        Attributes:
-            name: Geometry name as a string. Do not use white space or special
-                character.
-            center_pt: Sphere center point as (x, y, z) (Default: (0, 0 ,0)).
-            radius: Sphere radius as a number (Default: 10).
-            modifier: Geometry modifier (Default: "void").
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives where the
-                primitive is defined based on other primitives. (Default: [])
+    Usage:
 
-        Usage:
+    .. code-block:: python
 
-            .. code-block:: python
+        sphere = Sphere("test_sphere", (0, 0, 10), 10)
+        print(sphere)
+    """
+    __slots__ = ('_center_pt', '_radius')
 
-            sphere = Sphere("test_sphere", (0, 0, 10), 10)
-            print(sphere)
-        """
+    def __init__(self, name, center_pt=None, radius=10, modifier=None,
+                 dependencies=None):
+        """Radiance Sphere."""
         Geometry.__init__(self, name, modifier=modifier, dependencies=dependencies)
         self.center_pt = center_pt or (0, 0, 0)
         self.radius = radius if radius is not None else 10
 
         self._update_values()
 
     def _update_values(self):
         """update value dictionaries."""
         self._values[2] = \
             [self.center_pt[0], self.center_pt[1], self.center_pt[2], self.radius]
 
     @property
     def center_pt(self):
-        """Sphere center point as (x, y, z) (Default: (0, 0 ,0))."""
+        """Sphere center point as (x, y, z). Default is (0, 0 ,0)."""
         return self._center_pt
-    
+
     @center_pt.setter
     def center_pt(self, value):
         self._center_pt = tuple(float(v) for v in value)
         assert len(self._center_pt) == 3, \
             'Radiance Sphere center point must have 3 values for (x, y, z).'
 
     @property
     def radius(self):
-        """Sphere radius as a number (Default: 10)."""
+        """Sphere radius as a number. Default is 10."""
         return self._radius
-    
+
     @radius.setter
     def radius(self, value):
         self._radius = typing.float_positive(value)
 
     @classmethod
     def from_primitive_dict(cls, primitive_dict):
         """Initialize a Sphere from a primitive dict.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "sphere", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "sphere",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
         if primitive_dict['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
             )
@@ -108,23 +117,23 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize a Sphere from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "type": "sphere", // Geometry type
-                "modifier": {} or "void",
-                "name": "", // Geometry Name
-                "center_pt": {"x": float, "y": float, "z": float},
-                "radius": float,
-                "dependencies": []
+            "type": "sphere",  # Geometry type
+            "modifier": {} or "void",
+            "name": "",  # Geometry Name
+            "center_pt": {"x": float, "y": float, "z": float},
+            "radius": float,
+            "dependencies": []
             }
         """
         assert 'type' in data, 'Input dictionary is missing "type".'
         if data['type'] != cls.__name__.lower():
             raise ValueError(
                 'Type must be %s not %s.' % (cls.__name__.lower(),
                     data['type'])
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/geometry/mesh.py` & `honeybee-radiance-1.9.2/honeybee_radiance/geometry/mesh.py`

 * *Files 6% similar despite different names*

```diff
@@ -10,14 +10,16 @@
 class Mesh(Geometry):
     """Radiance Mesh.
 
     A mesh is a compound surface, made up of many triangles and an octree data structure
     to accelerate ray intersection. It is typically converted from a Wavefront .OBJ file
     using the obj2mesh program.
 
+    .. code-block:: shell
+
         mod mesh id
         1+ meshfile transform
         0
         0
 
     If the modifier is "void", then surfaces will use the modifiers given in the original
     mesh description. Otherwise, the modifier specified is used in their place. The
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/writer.py` & `honeybee-radiance-1.9.2/honeybee_radiance/writer.py`

 * *Files 0% similar despite different names*

```diff
@@ -74,15 +74,15 @@
 def face_to_rad(face, blk=False, minimal=False):
     """Get Face as a Radiance string.
 
     Note that the resulting string does not include modifier definitions. Nor
     does it include any states for dynamic geometry. However, it does include
     any of the shades assigned to the Face along with the Apertures and Doors
     in the Face.
-    
+
     Args:
         face: A honeyee Face for which a RAD representation will be returned.
         blk: Boolean to note whether the "blacked out" version of the Face should
             be output, which is useful for direct studies and isolation studies
             to understand the contribution of individual apertures.
         minimal: Boolean to note whether the radiance string should be written
             in a minimal format (with spaces instead of line breaks). Default: False.
@@ -151,15 +151,15 @@
 
     # write all Rooms into the file
     rooms = model.rooms
     if len(rooms) != 0:
         model_str.append('#   ================ ROOMS ================\n')
         for room in rooms:
             model_str.append(room_to_rad(room, blk, minimal))
-    
+
     # write all orphaned Faces into the file
     faces = model.orphaned_faces
     if len(faces) != 0:
         model_str.append('#   ================ FACES ================\n')
         for face in faces:
             model_str.append(face_to_rad(face, blk, minimal))
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/config.py` & `honeybee-radiance-1.9.2/honeybee_radiance/config.py`

 * *Files 18% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 
 .. code-block:: python
 
     from honeybee_radiance.config import folders
     print(folders.radiance_path)
     folders.radiance_path = "C:/Radiance/bin"
 """
+import ladybug.config as lb_config
 import honeybee.config as hb_config
 
 import os
 import platform
 import json
 
 
@@ -36,39 +37,34 @@
         * modifier_lib
         * modifierset_lib
         * config_file
         * mute
     """
 
     def __init__(self, config_file=None, mute=True):
-        # set the mute value
-        self.mute = bool(mute)
-
-        # load paths from the config JSON file 
-        self.config_file  = config_file
+        self.mute = bool(mute)  # set the mute value
+        self.config_file = config_file  # load paths from the config JSON file 
 
     @property
     def radiance_path(self):
         """Get or set the path to Radiance installation folder.
-        
+
         This is the top level folder that contains both the "bin" and the "lib"
         directories.
         """
         return self._radiance_path
-    
+
     @radiance_path.setter
     def radiance_path(self, r_path):
         exe_name = 'rad.exe' if os.name == 'nt' else 'rad'
-        if not r_path:  # check the PATH and then the default installation locations
-            r_path, rad_exe_file = self._which(exe_name)
-            if r_path is None:  # search within the default installation locations
-                r_path, rad_exe_file = self._find_radiance_folder()
+        if not r_path:  # check the default installation location
+            r_path = self._find_radiance_folder()
         else:
             r_path = os.path.join(r_path, 'bin')
-            rad_exe_file = os.path.join(r_path, exe_name)
+        rad_exe_file = os.path.join(r_path, exe_name) if r_path is not None else None
 
         if r_path:  # check that the Radiance executable exists in the installation
             assert os.path.isfile(rad_exe_file), \
                 '{} is not a valid path to a Radiance installation.'.format(r_path)
 
         # set the radiance_path
         self._radbin_path = r_path
@@ -80,40 +76,40 @@
         else:
             self._radiance_path = None
             self._radlib_path = None
 
     @property
     def radbin_path(self):
         """Get the path to Radiance bin folder.
-        
+
         This is the "bin" directory for Radiance installation (the one that
         contains the executable files).
         """
         return self._radbin_path
 
     @property
     def radlib_path(self):
         """Get the path to Radiance lib folder."""
         return self._radlib_path
 
     @property
     def standards_data_folder(self):
         """Get or set the path to the folder standards loaded to honeybee_radiance.lib.
-        
+
         This folder must have the following sub-folders in order to be valid:
-            * modifiers - folder with RAD files for modifiers.
-            * modifiersets - folder with JSON files of abridged ModifierSets.
+        * modifiers - folder with RAD files for modifiers.
+        * modifiersets - folder with JSON files of abridged ModifierSets.
         """
         return self._standards_data_folder
-    
+
     @standards_data_folder.setter
     def standards_data_folder(self, path):
         if not path:  # check the default locations of the template library
             path = self._find_standards_data_folder()
-        
+
         # gather all of the sub folders underneath the master folder
         self._modifier_lib = os.path.join(path, 'modifiers') if path else None
         self._modifierset_lib = os.path.join(path, 'modifiersets') if path else None
 
         # check that the library's sub-folders exist
         if path:
             assert os.path.isdir(self._modifier_lib), \
@@ -121,45 +117,45 @@
             assert os.path.isdir(self._modifierset_lib), \
                 '{} lacks a "modifiersets" folder.'.format(path)
 
         # set the standards_data_folder
         self._standards_data_folder = path
         if path and not self.mute:
             print('Path to the standards_data_folder is set to: '
-                    '{}'.format(self._standards_data_folder))
+                  '{}'.format(self._standards_data_folder))
 
     @property
     def modifier_lib(self):
         """Get the path to the modifier library in the standards_data_folder."""
         return self._modifier_lib
-    
+
     @property
     def modifierset_lib(self):
         """Get the path to the modifierset library in the standards_data_folder."""
         return self._modifierset_lib
 
-    @property 
+    @property
     def config_file(self):
         """Get or set the path to the config.json file from which folders are loaded.
-        
+
         Setting this to None will result in using the config.json module included
         in this package.
         """
         return self._config_file
 
     @config_file.setter
     def config_file(self, cfg):
         if cfg is None:
             cfg = os.path.join(os.path.dirname(__file__), 'config.json')
         self._load_from_file(cfg)
         self._config_file = cfg
 
     def _load_from_file(self, file_path):
         """Set all of the the properties of this object from a config JSON file.
-        
+
         Args:
             file_path: Path to a JSON file containing the file paths. A sample of this
                 JSON is the config.json file within this package.
         """
         # check the default file path
         assert os.path.isfile(str(file_path)), \
             ValueError('No file found at {}'.format(file_path))
@@ -184,126 +180,77 @@
         self.radiance_path = default_path["radiance_path"]
 
         # set path for the standards_data_folder
         self.standards_data_folder = default_path["standards_data_folder"]
 
     def _find_radiance_folder(self):
         """Find the Radiance installation in its default location.
-        
+
         This method will first attempt to return the path of a standalone Radiance
         installation and, if none are found, it will search for one that is
         installed with OpenStudio.
 
         Returns:
             File directory and full path to executable in case of success.
             None, None in case of failure.
         """
-        # first check for the default location where standalone Radiance is installed
+        # first check if there's a version installed in the ladybug_tools folder
+        lb_install = lb_config.folders.ladybug_tools_folder
         rad_path = None
-        if os.name == 'nt':  # search the C:/ drive on Windows
-            for f in os.listdir('C:\\'):
-                if f.lower() == 'radiance' and os.path.isdir('C:\\{}'.format(f)):
-                    rad_path = 'C:\\{}'.format(f)
-                    break
+        if os.path.isdir(lb_install):
+            test_path = os.path.join(lb_install, 'radiance')
+            rad_path = test_path if os.path.isdir(test_path) else None
+
+        # then check for the default location where standalone Radiance is installed
+        if rad_path is not None:
+            pass  # we found a version of radiance in the ladybug_tools folder
+        elif os.name == 'nt':  # search the C:/ drive on Windows
+            test_path = 'C:\\Radiance'
+            rad_path = test_path if os.path.isdir(test_path) else None
         elif platform.system() == 'Darwin':  # search the Applications folder on Mac
-            for f in os.listdir('/Applications/'):
-                if f.lower() == 'radiance' and os.path.isdir('/Applications/{}'.format(f)):
-                    rad_path = '/Applications/{}'.format(f)
-                    break
+            test_path = '/Applications/radiance'
+            rad_path = test_path if os.path.isdir(test_path) else None
         elif platform.system() == 'Linux':  # search the usr/local folder
-            for f in os.listdir('/usr/local/'):
-                if f.lower() == 'radiance' and os.path.isdir('/usr/local/{}'.format(f)):
-                    rad_path = '/usr/local/{}'.format(f)
-                    break
-
-        if not rad_path:  # then check the Radiance that comes with OpenStudio
-            os_path = self._find_openstudio_folder()
-            if os_path and os.path.isdir(os.path.join(os_path, 'Radiance')):
-                rad_path = os.path.join(os_path, 'Radiance')
+            test_path = '/usr/local/radiance'
+            rad_path = test_path if os.path.isdir(test_path) else None
+
+        # lastly, check if honeybee_energy is installed and get Radiance with OpenStudio
+        if not rad_path:
+            try:
+                import honeybee_energy.config as hbe_config
+                os_path = hbe_config.folders.openstudio_path
+                if os_path:
+                    test_path = os.path.join(os.path.split(os_path)[0], 'Radiance')
+                    rad_path = test_path if os.path.isdir(test_path) else None
+            except ImportError:
+                pass  # no honeybee_energy installation found
 
         if not rad_path:  # No Radiance installations were found
-            return None, None
+            return None
 
         # return the path to the executable
         rad_path = os.path.join(rad_path, 'bin')
-        exec_file = os.path.join(rad_path, 'rad.exe') if os.name == 'nt' \
-            else os.path.join(rad_path, 'rad')
-        return rad_path, exec_file
-
-    @staticmethod
-    def _find_openstudio_folder():
-        """Find the most recent OpenStudio installation in its default location.
-
-        Returns:
-            File directory and full path to executable in case of success.
-            None, None in case of failure.
-        """
-        def getversion(openstudio_path):
-            """Get digits for the version of OpenStudio."""
-            ver = ''.join(s for s in openstudio_path if (s.isdigit() or s == '.'))
-            return sum(int(d) * (10 ** i) for i, d in enumerate(reversed(ver.split('.'))))
-
-        if os.name == 'nt':  # search the C:/ drive on Windows
-            os_folders = ['C:\\{}'.format(f) for f in os.listdir('C:\\')
-                          if (f.lower().startswith('openstudio') and
-                              os.path.isdir('C:\\{}'.format(f)))]
-        elif platform.system() == 'Darwin':  # search the Applications folder on Mac
-            os_folders = ['/Applications/{}'.format(f) for f in os.listdir('/Applications/')
-                          if (f.lower().startswith('openstudio') and
-                              os.path.isdir('/Applications/{}'.format(f)))]
-        elif platform.system() == 'Linux':  # search the usr/local folder
-            os_folders = ['/usr/local/{}'.format(f) for f in os.listdir('/usr/local/')
-                          if (f.lower().startswith('openstudio') and
-                              os.path.isdir('/usr/local/{}'.format(f)))]
-        else:  # unknown operating system
-            os_folders = None
-        
-        if not os_folders:  # No Openstudio installations were found
-            return None
-        
-        # get the most recent version of OpenStudio that was found
-        return sorted(os_folders, key=getversion, reverse=True)[0]
+        return rad_path
 
     @staticmethod
     def _find_standards_data_folder():
         """Find the the user template library in its default location.
-        
-        The HOME/honeybee/honeybee_standards/data folder will be checked first,
-        which can conatain libraries that are not overwritten with the update of the
-        honeybee_energy package. If no such folder is found, this method defaults to
-        the lib/library/ folder within this package.
-        """
-        # first check the default sim folder folder, where permanent libraries live
-        home_folder = os.getenv('HOME') or os.path.expanduser('~')
-        lib_folder = os.path.join(home_folder, 'honeybee', 'honeybee_standards', 'data')
-        if os.path.isdir(lib_folder):
-            return lib_folder
-        else:  # default to the library folder that installs with this Python package
-            return os.path.join(os.path.dirname(__file__), 'lib', 'data')
-
-    @staticmethod
-    def _which(program):
-        """Find an executable program in the PATH by name.
-
-        Args:
-            program: Full file name for the program (e.g. energyplus.exe)
 
-        Returns:
-            File directory and full path to program in case of success.
-            None, None in case of failure.
-        """
-        def is_exe(fpath):
-            # Return true if the file exists and is executable
-            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
-
-        # check for the file in all path in environment
-        for path in os.environ["PATH"].split(os.pathsep):
-            exe_file = os.path.join(path.strip('"'), program)  # strip "" in Windows
-            if is_exe(exe_file):
-                return path, exe_file
+        The ladybug_tools/resources/standards/honeybee_standards folder will be
+        checked first, which can conatain libraries that are not overwritten with
+        the update of the honeybee_radiance package. If no such folder is found,
+        this method defaults to the lib/library/ folder within this package.
+        """
+        # first check the ladybug_tools installation folder were permanent lib is
+        lb_install = lb_config.folders.ladybug_tools_folder
+        if os.path.isdir(lb_install):
+            lib_folder = os.path.join(
+                lb_install, 'resources', 'standards', 'honeybee_standards')
+            if os.path.isdir(lib_folder):
+                return lib_folder
 
-        # couldn't find it in the PATH! return None :|
-        return None, None
+        # default to the library folder that installs with this Python package
+        return os.path.join(os.path.dirname(__file__), 'lib', 'data')
 
 
 """Object possesing all key folders within the configuration."""
 folders = Folders(mute=True)
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lightsource/_gendaylit.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lightsource/_gendaylit.py`

 * *Files 0% similar despite different names*

```diff
@@ -28,15 +28,15 @@
         altitude: Sun altitude in degrees.
         hoy: Day of the year starting from 1.
         directirradiance: Direct irradiance value.
         diffuseirradiance: Diffuse irradiance value.
         output_type: An integer between 0-2. 0=output in W/m^2/sr visible,
             1=output in W/m^2/sr solar, 2=output in candela/m^2 (default: 0).
     Returns:
-        solarradiance: solar irradiance.
+        solarradiance -- solar irradiance.
     """
     #
     coeff_perez = [
         1.3525, -0.2576, -0.2690, -1.4366, -0.7670, 0.0007, 1.2734, -0.1233, 2.8000,
         0.6004, 1.2375, 1.000, 1.8734, 0.6297, 0.9738, 0.2809, 0.0356, -0.1246,
         -0.5718, 0.9938, -1.2219, -0.7730, 1.4148, 1.1016, -0.2054, 0.0367, -3.9128,
         0.9156, 6.9750, 0.1774, 6.4477, -0.1239, -1.5798, -0.5081, -1.7812, 0.1080,
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sunpath.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sunpath.py`

 * *Files 9% similar despite different names*

```diff
@@ -32,16 +32,19 @@
 
 
 class Sunpath(object):
     """A Radiance-based sun-path.
 
     Args:
         location: A Ladybug location.
-        wea: A ladybug annual wea for generating climate-based sunpath. The location of
-            the wea object will be ignored.
+        north: Sunpath north angle.
+
+    Properties:
+        * location
+        * north
     """
     __slots__ = ('_location', '_north')
 
     def __init__(self, location, north=0):
         self.location = location
         self.north = north
 
@@ -56,15 +59,15 @@
             'Location must be a Ladybug Location not %s' % type(loc)
         self._location = loc
 
     @property
     def north(self):
         """Sunpath north angle."""
         return self._north
-    
+
     @north.setter
     def north(self, n):
         assert isinstance(n, (int, float)), 'north must be a numerical value.'
         self._north = n
 
     def _solar_calc(self, hoys, wea, output_type, leap_year=False,
             reverse_vectors=False):
@@ -139,19 +142,19 @@
             leap_year: Set to True if hoys are for a leap year (default: False).
             reverse_vector: Set to True to reverse the vector direction of suns. By
                 default sun vectors are coming from sun towards the ground. This option
                 will reverse the direction of the vectors. Reversed sunpath is mainly
                 useful for radiation studies (default: False).
             split_mod_files: A boolean to split the modifer file into multiple files to
                 ensure none of them includes more than 10,000 modifiers.
-        
+
         Returns:
-            dict: A dictionary with with two keys for sunpath and suns. sunpath returns
-                the path to the sunpath file and suns returns a list of path to modifier
-                files.
+            dict -- A dictionary with with two keys for sunpath and suns. sunpath returns
+            the path to the sunpath file and suns returns a list of path to modifier
+            files.
         """
         sun_vectors, sun_up_hours, radiance_values = \
             self._solar_calc(hoys, wea, output_type, leap_year, reverse_vectors)
 
         if not os.path.isdir(folder):
             os.makedirs(folder)
 
@@ -202,15 +205,24 @@
 
         return {'sunpath': fp, 'suns': sun_files}
 
 
     def to_dict(self):
         """Convert this sunpath to a dictionary.
 
-        Dictionary keys are type, location and north.
+        Args:
+            input_dict: A python dictionary in the following format
+
+        .. code-block:: python
+
+            {
+            'type': 'Sunpath',
+            'location': {}  # Location dictionary,
+            'north': 0,
+            }
         """
         return {
             'type': 'Sunpath',
             'location': self.location.to_dict(),
             'north': self.north
         }
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/hemisphere.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/hemisphere.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,80 +1,89 @@
 """Radiance sky hemisphere."""
 import honeybee.typing as typing
 import ladybug.futil as futil
 import os
 
 
 class Hemisphere(object):
-    """Radiance sky hemisphere."""
+    """Radiance sky hemisphere.
 
-    def __init__(self):
-        """Create sky hemisphere.
+    Sky hemisphere relies on skyfunc and must be used with one of the
+    Radiance sky commands.
 
-        Sky hemisphere relies on skyfunc and must be used with one of the
-        Radiance sky commands.
+    .. code-block:: shell
 
         skyfunc glow sky_glow
         0
         0
         4 1 1 1 0
         sky_glow source sky
         0
         0
         4 0 0 1 180
 
-        Note:
-        For more information see Chapter `6.3.2  Example: CIE Overcast Sky` in
-        Rendering with Radiance. The chapter is also accessible online at the
-        link below.
-        https://www.radiance-online.org/community/workshops/2003-berkeley/presentations/Mardaljevic/rwr_ch6.pdf
-
-        """
+    Note:
+    For more information see Chapter `6.3.2  Example: CIE Overcast Sky` in
+    Rendering with Radiance. The chapter is also accessible online at the
+    link below.
+    https://www.radiance-online.org/community/workshops/2003-berkeley/presentations/\
+Mardaljevic/rwr_ch6.pdf
+
+    Properties:
+        * r_emittance
+        * g_emittance
+        * b_emittance
+"""
+    def __init__(self):
+        """Create sky hemisphere."""
         self._r_emittance = 1.0
         self._g_emittance = 1.0
         self._b_emittance = 1.0
 
     @property
     def r_emittance(self):
-        """Sky hemisphere emittance values for red channel (Default: 1.0)."""
+        """Sky hemisphere emittance values for red channel (Default is 1.0)."""
         return self._r_emittance
 
     @r_emittance.setter
     def r_emittance(self, value):
         self._r_emittance = typing.float_in_range(value, 0, 1, 'r_emittance')
 
     @property
     def g_emittance(self):
-        """Sky hemisphere emittance values for green channel (Default: 1.0)."""
+        """Sky hemisphere emittance values for green channel (Default is 1.0)."""
         return self._g_emittance
 
     @g_emittance.setter
     def g_emittance(self, value):
         self._g_emittance = typing.float_in_range(value, 0, 1, 'g_emittance')
 
     @property
     def b_emittance(self):
-        """Sky hemisphere emittance values for blue channel (Default: 1.0)."""
+        """Sky hemisphere emittance values for blue channel (Default is 1.0)."""
         return self._b_emittance
 
     @b_emittance.setter
     def b_emittance(self, value):
         self._b_emittance = typing.float_in_range(value, 0, 1, 'b_emittance')
 
     @classmethod
     def from_dict(cls, input_dict):
         """Create sky_hemisphere from_dict.
-        
+
         Args:
-            input_dict:
+            input_dict: A python dictionary in the following format
+
+        .. code-block:: python
+
                 {
-                    'type': 'SkyHemisphere',
-                    'r_emittance': r_emittance,
-                    'g_emittance': g_emittance,
-                    'b_emittance': b_emittance
+                'type': 'SkyHemisphere',
+                'r_emittance': r_emittance,
+                'g_emittance': g_emittance,
+                'b_emittance': b_emittance
                 }
         """
         assert 'type' in input_dict, \
             'Input dict is missing type. Not a valid sky_hemisphere dictionary.'
         assert input_dict['type'] == 'SkyHemisphere', \
             'Input type must be SkyHemisphere not %s' % input_dict['type']
         sky_hemisphere = cls()
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/_skybase.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/_skybase.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,17 @@
 from abc import ABCMeta, abstractproperty, abstractmethod
 
 
 class Sky(object):
-    """Base class for Honeybee Skies."""
+    """Base class for Honeybee Skies.
+
+    Properties:
+        * is_point_in_time
+        * is_climate_based
+    """
     __metaclass__ = ABCMeta
     __slots__ = ()
 
     @property
     def is_point_in_time(self):
         """Return True if the sky is generated for a single point in time."""
         return False
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lightsource/sky/certainirradiance.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lightsource/sky/certainirradiance.py`

 * *Files 4% similar despite different names*

```diff
@@ -6,54 +6,64 @@
 import honeybee.typing as typing
 import ladybug.futil as futil
 
 
 class CertainIrradiance(Sky):
     """sky with certain irradiance.
 
-    The output of CertainIrradiance sky is similar to using command below:
-    `gensky -c -B desired_irradiance `
+    The output of CertainIrradiance sky is similar to using command below::
 
-    You can also generate the sky with certain illuminance using `from_illuminance`
+        gensky -c -B desired_irradiance
+
+    You can also generate the sky with certain illuminance using ``from_illuminance``
     classmethod. The method converts the illuminance value to irradiance by dividing it
-    by 179.0.
+    by 179.0::
 
-    `gensky -c -B [desired_illuminance / 179.0]`
+        gensky -c -B [desired_illuminance / 179.0]
 
     It also includes ground glow source. Ground reflectance is set to %20 by default
     which is gensky's default value. Use `ground_reflectance` property to adjust this
     value.
 
     Note:
 
     The conversion factor in the Radiance system for luminous efficacy is fixed at
     KR= 179 lumens/watt (lm/w). This should not be confused with the more usual
     daylighting value, which can be anywhere between 50 and 150 lm/w depending on the
     type of sky or light considered.
 
     For more information see links below on the Radiance forum:
-    - https://discourse.radiance-online.org/t/coefficient-179/547
-    - https://discourse.radiance-online.org/t/luminous-efficacy/1400
+
+    * https://discourse.radiance-online.org/t/coefficient-179/547
+    * https://discourse.radiance-online.org/t/luminous-efficacy/1400
+
+    Default value is set to 558.659 which corresponds to a sky with 100,000 lux
+    horizontal illuminance.
+
+    Args:
+        irradiance: Desired horizontal diffuse irradiance value in watts/meter2
+            (Default: 558.659).
+        ground_reflectance: Average ground reflectance (Default: 0.2).
+
+    Properties:
+        * irradiance
+        * illuminance
+        * ground_hemisphere
+        * sky_hemisphere
+        * ground_reflectance
+        * is_point_in_time
+        * is_climate_based
     """
     __slots__ = (
         '_irradiance', '_ground', '_ground_reflectance',
         '_ground_hemisphere', '_sky_hemisphere'
     )
 
     def __init__(self, irradiance=558.659, ground_reflectance=0.2):
-        """Create sky with certain irradiance.
-
-        Default value is set to 558.659 which corresponds to a sky with 100,000 lux
-        horizontal illuminance.
-
-        Args:
-            irradiance: Desired horizontal diffuse irradiance value in watts/meter2
-                (Default: 558.659).
-            ground_reflectance: Average ground reflectance (Default: 0.2).
-        """
+        """Create sky with certain irradiance."""
         Sky.__init__(self)
         self.irradiance = irradiance
         self.ground_reflectance = ground_reflectance
         self._ground_hemisphere = Ground()
         self._sky_hemisphere = Hemisphere()
 
 
@@ -112,22 +122,25 @@
     def is_climate_based(self):
         """Return True if the sky is created based on values from weather file."""
         return False
 
     @classmethod
     def from_dict(cls, input_dict):
         """Create the sky from a dictionary.
-        
+
         Args:
-            input_dict:
+            input_dict: A python dictionary in the following format
+
+        .. code-block:: python
+
                 {
-                    'irradiance': irradiance,
-                    'ground_reflectance': ground_reflectance,
-                    'ground_hemisphere': see ground.Ground class [optional],
-                    'sky_hemisphere': see hemisphere.Hemisphere class [optional]
+                'irradiance': 558.659,
+                'ground_reflectance': 0.2,
+                'ground_hemisphere': {},  # see ground.Ground class [optional],
+                'sky_hemisphere': {}  # see hemisphere.Hemisphere class [optional]
                 }
         """
         sky = cls(
             input_dict['irradiance'],
             input_dict['ground_reflectance']
         )
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/lightsource/ground.py` & `honeybee-radiance-1.9.2/honeybee_radiance/lightsource/ground.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,41 +4,48 @@
 """
 import honeybee.typing as typing
 import ladybug.futil as futil
 import os
 
 
 class Ground(object):
-    """Radiance ground."""
+    """Radiance ground.
 
-    def __init__(self):
-        """Create ground.
+    Ground definition relies on skyfunc and must be used with one of the Radiance
+    skies generated by gendaylit, gensky, etc. You can adjust the ground reflection
+    using -g option in gensky / gendaylit. The default value in gensky is %20.
 
-        Ground definition relies on skyfunc and must be used with one of the Radiance
-        skies generated by gendaylit, gensky, etc. You can adjust the ground reflection
-        using -g option in gensky / gendaylit. The default value in gensky is %20.
+    .. code-block:: shell
 
         skyfunc glow ground_glow
         0
         0
         4 1 1 1 0
         ground_glow source ground
         0
         0
         4 0 0 -1 180
 
         oconv some.sky ground.rad scene.rad > scene.oct
 
-        Note:
-            For more information see Chapter `6.3.4  The Ground "Glow": An "Upside-Down"
-            Sky` in Rendering with Radiance. The chapter is also accessible online at the
-        link below.
-        https://www.radiance-online.org/community/workshops/2003-berkeley/presentations/Mardaljevic/rwr_ch6.pdf
+    Note:
+        For more information see Chapter `6.3.4  The Ground "Glow": An "Upside-Down"
+        Sky` in Rendering with Radiance. The chapter is also accessible online at the
+    link below.
+    https://www.radiance-online.org/community/workshops/2003-berkeley/presentations/\
+Mardaljevic/rwr_ch6.pdf
+
+    Properties:
+        * r_emittance
+        * g_emittance
+        * b_emittance
+    """
 
-        """
+    def __init__(self):
+        """Create ground."""
         self._r_emittance = 1.0
         self._g_emittance = 1.0
         self._b_emittance = 1.0
 
     @property
     def r_emittance(self):
         """Ground emittance values for red channel (Default: 1.0)."""
@@ -67,20 +74,23 @@
         self._b_emittance = typing.float_in_range(value, 0, 1, 'b_emittance')
 
     @classmethod
     def from_dict(cls, input_dict):
         """Create ground from_dict.
 
         Args:
-            input_dict:
+            input_dict: A python dictionary in the following format
+
+        .. code-block:: python
+
                 {
-                    'type': 'SkyHemisphere',
-                    'r_emittance': r_emittance,
-                    'g_emittance': g_emittance,
-                    'b_emittance': b_emittance
+                'type': 'SkyHemisphere',
+                'r_emittance': r_emittance,
+                'g_emittance': g_emittance,
+                'b_emittance': b_emittance
                 }
         """
         assert 'type' in input_dict, \
             'Input dict is missing type. Not a valid ground dictionary.'
         assert input_dict['type'] == 'Ground', \
             'Input type must be Ground not %s' % input_dict['type']
         ground = cls()
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/properties/room.py` & `honeybee-radiance-1.9.2/honeybee_radiance/properties/room.py`

 * *Files 8% similar despite different names*

```diff
@@ -3,31 +3,30 @@
 from ..modifierset import ModifierSet
 from ..lib.modifiersets import generic_modifier_set_visible
 
 
 class RoomRadianceProperties(object):
     """Radiance Properties for Honeybee Room.
 
+    Args:
+        host: A honeybee_core Room object that hosts these properties.
+        modifier_set: A honeybee ModifierSet object to specify all default
+            modifiers for the Faces of the Room. If None, the Room will use
+            the honeybee default modifier set, which is only representitive
+            of typical indoor conditions in the visible spectrum. Default: None.
+
     Properties:
         * host
         * modifier_set
     """
 
     __slots__ = ('_host', '_modifier_set')
 
     def __init__(self, host, modifier_set=None):
-        """Initialize Room radiance properties.
-
-        Args:
-            host: A honeybee_core Room object that hosts these properties.
-            modifier_set: A honeybee ModifierSet object to specify all default
-                modifiers for the Faces of the Room. If None, the Room will use
-                the honeybee default modifier set, which is only representitive
-                of typical indoor conditions in the visible spectrum. Default: None.
-        """
+        """Initialize Room radiance properties."""
         # set the main properties of the Room
         self._host = host
         self.modifier_set = modifier_set
 
     @property
     def host(self):
         """Get the Room object hosting these properties."""
@@ -56,33 +55,48 @@
     def from_dict(cls, data, host):
         """Create RoomRadianceProperties from a dictionary.
 
         Note that the dictionary must be a non-abridged version for this
         classmethod to work.
 
         Args:
-            data: A dictionary representation of RoomRadianceProperties.
+            data: A dictionary representation of RoomRadianceProperties with the
+                format below.
             host: A Room object that hosts these properties.
+
+        .. code-block:: python
+
+            {
+            'type': 'RoomRadianceProperties',
+            'modifier_set': {},  # ModifierSet dictionary
+            }
         """
         assert data['type'] == 'RoomRadianceProperties', \
             'Expected RoomRadianceProperties. Got {}.'.format(data['type'])
 
         new_prop = cls(host)
         if 'modifier_set' in data and data['modifier_set'] is not None:
             new_prop.modifier_set = ModifierSet.from_dict(data['modifier_set'])
         return new_prop
 
     def apply_properties_from_dict(self, abridged_data, modifier_sets):
         """Apply properties from a RoomRadiancePropertiesAbridged dictionary.
 
         Args:
             abridged_data: A RoomRadiancePropertiesAbridged dictionary (typically
-                coming from a Model).
+                coming from a Model) with the format below.
             modifier_sets: A dictionary of ModifierSets with names of the sets
                 as keys, which will be used to re-assign modifier_sets.
+
+        .. code-block:: python
+
+            {
+            'type': 'RoomRadiancePropertiesAbridged',
+            'modifier_set': str,  # ModifierSet name
+            }
         """
         if 'modifier_set' in abridged_data and abridged_data['modifier_set'] is not None:
             self.modifier_set = modifier_sets[abridged_data['modifier_set']]
 
     def to_dict(self, abridged=False):
         """Return Room radiance properties as a dictionary.
 
@@ -101,16 +115,17 @@
                 self._modifier_set.name if abridged else self._modifier_set.to_dict()
 
         return base
 
     def duplicate(self, new_host=None):
         """Get a copy of this object.
 
-        new_host: A new Room object that hosts these properties.
-            If None, the properties will be duplicated with the same host.
+        Args:
+            new_host: A new Room object that hosts these properties.
+                If None, the properties will be duplicated with the same host.
         """
         _host = new_host or self._host
         new_room = RoomRadianceProperties(_host, self._modifier_set)
         return new_room
 
     def ToString(self):
         return self.__repr__()
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/properties/_base.py` & `honeybee-radiance-1.9.2/honeybee_radiance/properties/_base.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,37 +7,36 @@
 
 
 class _GeometryRadianceProperties(object):
     """Base class of Radiance Properties for all planar geometry objects.
 
     This includes (Face, Aperture, Door, Shade).
 
+    Args:
+        host: A honeybee_core object that hosts these properties.
+        modifier: A Honeybee Radiance Modifier for the object. If None,
+            it will be set by the parent Room ModifierSet or the Honeybee
+            default generic ModifierSet.
+        modifier_blk: A Honeybee Radiance Modifier to be used for this object
+            in direct solar simulations and in isolation studies (assessing
+            the contribution of individual Apertures).
+
     Properties:
         * host
         * modifier
         * modifier_blk
-        * is_opaque 
+        * is_opaque
         * is_modifier_set_on_object
-        * is_blk_overridden 
+        * is_blk_overridden
     """
 
     __slots__ = ('_host', '_modifier', '_modifier_blk')
 
     def __init__(self, host, modifier=None, modifier_blk=None):
-        """Initialize GeometryRadianceProperties.
-
-        Args:
-            host: A honeybee_core object that hosts these properties.
-            modifier: A Honeybee Radiance Modifier for the object. If None,
-                it will be set by the parent Room ModifierSet or the Honeybee
-                default generic ModifierSet.
-            modifier_blk: A Honeybee Radiance Modifier to be used for this object
-                in direct solar simulations and in isolation studies (assessing
-                the contribution of individual Apertures).
-        """
+        """Initialize GeometryRadianceProperties."""
         self._host = host
         self.modifier = modifier
         self.modifier_blk = modifier_blk
 
     @property
     def host(self):
         """Get the object hosting these properties."""
@@ -55,15 +54,15 @@
                 'Expected Radiance Modifier for shade. Got {}'.format(type(value))
             value.lock()  # lock editing in case modifier has multiple references
         self._modifier = value
 
     @property
     def modifier_blk(self):
         """Get or set a modifier to be used in direct solar and in isolation studies.
-        
+
         If None, this will be a completely black material if the object's modifier is
         opaque and will be equal to the modifier if the object's modifier is non-opaque.
         """
         if self._modifier_blk:  # set by user
             return self._modifier_blk
         mod = self.modifier  # assign a default based on whether the modifier is opaque
         if mod.is_opaque:
@@ -74,38 +73,38 @@
     @modifier_blk.setter
     def modifier_blk(self, value):
         if value is not None:
             assert isinstance(value, Modifier), \
                 'Expected Radiance Modifier. Got {}'.format(type(value))
             value.lock()  # lock editing in case modifier has multiple references
         self._modifier_blk = value
-    
+
     @property
     def is_opaque(self):
         """Boolean noting whether this object has an opaque modifier.
-        
+
         This has repercussions for how this object is written into the Radiance
         folder structure.
         """
         return self.modifier.is_opaque
 
     @property
     def is_modifier_set_on_object(self):
         """Boolean noting if modifier is assigned on the level of this object.
-        
+
         This is opposed to having the modifier assigned by a ModifierSet.
         """
         return self._modifier is not None
-    
+
     @property
     def is_blk_overridden(self):
         """Boolean noting if modifier_blk has been overridden from default on this object.
         """
         return self._modifier is not None
-    
+
     def reset_to_default(self):
         """Reset a Modifier assigned at the level of this Shade to the default.
 
         This means that the Shade's modifier will be assigned by a ModifierSet instead.
         """
         self._modifier = None
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/properties/shade.py` & `honeybee-radiance-1.9.2/honeybee_radiance/properties/shade.py`

 * *Files 3% similar despite different names*

```diff
@@ -5,39 +5,38 @@
 from ..lib.modifiers import generic_context
 from ..lib.modifiersets import generic_modifier_set_visible
 
 
 class ShadeRadianceProperties(_GeometryRadianceProperties):
     """Radiance Properties for Honeybee Shade.
 
+    Args:
+        host: A honeybee_core Shade object that hosts these properties.
+        modifier: A Honeybee Radiance Modifier object for the shade. If None,
+            it will be set by the parent Room ModifierSet or the Honeybee
+            default generic ModifierSet.
+        modifier_blk: A Honeybee Radiance Modifier object to be used for this
+            shade in direct solar simulations and in isolation studies (assessing
+            the contribution of individual Apertures). If None, this will be
+            a completely black material if the Shade's modifier is opaque and
+            will be equal to the modifier if the Shade's modifier is non-opaque.
+
     Properties:
         * host
         * modifier
         * modifier_blk
-        * is_opaque 
+        * is_opaque
         * is_modifier_set_on_object
-        * is_blk_overridden 
+        * is_blk_overridden
     """
 
     __slots__ = ()
 
     def __init__(self, host, modifier=None, modifier_blk=None):
-        """Initialize Shade radiance properties.
-
-        Args:
-            host: A honeybee_core Shade object that hosts these properties.
-            modifier: A Honeybee Radiance Modifier object for the shade. If None,
-                it will be set by the parent Room ModifierSet or the Honeybee
-                default generic ModifierSet.
-            modifier_blk: A Honeybee Radiance Modifier object to be used for this
-                shade in direct solar simulations and in isolation studies (assessing
-                the contribution of individual Apertures). If None, this will be
-                a completely black material if the Shade's modifier is opaque and
-                will be equal to the modifier if the Shade's modifier is non-opaque.
-        """
+        """Initialize Shade radiance properties."""
         _GeometryRadianceProperties.__init__(self, host, modifier, modifier_blk)
 
     @property
     def modifier(self):
         """Get or set the Shade modifier.
 
         If the modifier is not set on the shade-level, then it will be assigned
@@ -68,30 +67,47 @@
     def from_dict(cls, data, host):
         """Create ShadeRadianceProperties from a dictionary.
 
         Note that the dictionary must be a non-abridged version for this
         classmethod to work.
 
         Args:
-            data: A dictionary representation of ShadeRadianceProperties.
+            data: A dictionary representation of ShadeRadianceProperties with the
+                format below.
             host: A Shade object that hosts these properties.
+
+        .. code-block:: python
+
+            {
+            'type': 'ShadeRadianceProperties',
+            'modifier': {},  # A Honeybee Radiance Modifier dictionary
+            'modifier_blk': {}  # A Honeybee Radiance Modifier dictionary
+            }
         """
         assert data['type'] == 'ShadeRadianceProperties', \
             'Expected ShadeRadianceProperties. Got {}.'.format(data['type'])
         new_prop = cls(host)
         return cls._restore_modifiers_from_dict(new_prop, data)
 
     def apply_properties_from_dict(self, abridged_data, modifiers):
         """Apply properties from a ShadeRadiancePropertiesAbridged dictionary.
 
         Args:
             abridged_data: A ShadeRadiancePropertiesAbridged dictionary (typically
-                coming from a Model).
+                coming from a Model) with the format below.
             modifiers: A dictionary of modifiers with modifier names as keys,
                 which will be used to re-assign modifiers.
+
+        .. code-block:: python
+
+            {
+            'type': 'ShadeRadiancePropertiesAbridged',
+            'modifier': str,  # A Honeybee Radiance Modifier name
+            'modifier_blk': str  # A Honeybee Radiance Modifier name
+            }
         """
         self._apply_modifiers_from_dict(abridged_data, modifiers)
 
     def to_dict(self, abridged=False):
         """Return radiance properties as a dictionary.
 
         Args:
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/properties/door.py` & `honeybee-radiance-1.9.2/honeybee_radiance/properties/door.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,38 +5,38 @@
 from ..lib.modifiers import black
 from ..lib.modifiersets import generic_modifier_set_visible
 
 
 class DoorRadianceProperties(_GeometryRadianceProperties):
     """Radiance Properties for Honeybee Door.
 
+
+    Args:
+        host: A honeybee_core Door object that hosts these properties.
+        modifier: A Honeybee Radiance Modifier object for the door. If None,
+            it will be set by the parent Room ModifierSet or the Honeybee
+            default generic ModifierSet.
+        modifier_blk: A Honeybee Radiance Modifier object to be used for this
+            door in direct solar simulations and in isolation studies (assessing
+            the contribution of individual Apertures). If None, this will be
+            a completely black material.
+
     Properties:
         * host
         * modifier
         * modifier_blk
-        * is_opaque 
+        * is_opaque
         * is_modifier_set_on_object
-        * is_blk_overridden 
+        * is_blk_overridden
     """
 
     __slots__ = ()
 
     def __init__(self, host, modifier=None, modifier_blk=None):
-        """Initialize Door radiance properties.
-
-        Args:
-            host: A honeybee_core Door object that hosts these properties.
-            modifier: A Honeybee Radiance Modifier object for the door. If None,
-                it will be set by the parent Room ModifierSet or the Honeybee
-                default generic ModifierSet.
-            modifier_blk: A Honeybee Radiance Modifier object to be used for this
-                door in direct solar simulations and in isolation studies (assessing
-                the contribution of individual Apertures). If None, this will be
-                a completely black material.
-        """
+        """Initialize Door radiance properties."""
         _GeometryRadianceProperties.__init__(self, host, modifier, modifier_blk)
 
     @property
     def modifier(self):
         """Get or set the Door modifier.
 
         If the modifier is not set on the door-level, then it will be assigned
@@ -67,15 +67,15 @@
                 'Expected Radiance Modifier for door. Got {}'.format(type(value))
             value.lock()  # lock editing in case modifier has multiple references
         self._modifier = value
 
     @property
     def modifier_blk(self):
         """Get or set a modifier to be used in direct solar and in isolation studies.
-        
+
         If None, this will be a completely black material if the Door's modifier
         is opaque and will be equal to the modifier if the Door's modifier is non-opaque.
         """
         if self._modifier_blk:  # set by user
             return self._modifier_blk
         return black
 
@@ -91,30 +91,47 @@
     def from_dict(cls, data, host):
         """Create DoorRadianceProperties from a dictionary.
 
         Note that the dictionary must be a non-abridged version for this
         classmethod to work.
 
         Args:
-            data: A dictionary representation of DoorRadianceProperties.
+            data: A dictionary representation of DoorRadianceProperties with the
+                format below.
             host: A Door object that hosts these properties.
+
+        .. code-block:: python
+
+            {
+            'type': 'DoorRadianceProperties',
+            'modifier': {},  # A Honeybee Radiance Modifier dictionary
+            'modifier_blk': {}  # A Honeybee Radiance Modifier dictionary
+            }
         """
         assert data['type'] == 'DoorRadianceProperties', \
             'Expected DoorRadianceProperties. Got {}.'.format(data['type'])
         new_prop = cls(host)
         return cls._restore_modifiers_from_dict(new_prop, data)
 
     def apply_properties_from_dict(self, abridged_data, modifiers):
         """Apply properties from a DoorRadiancePropertiesAbridged dictionary.
 
         Args:
             abridged_data: A DoorRadiancePropertiesAbridged dictionary (typically
-                coming from a Model).
+                coming from a Model) with the format below.
             modifiers: A dictionary of modifiers with modifier names as keys,
                 which will be used to re-assign modifiers.
+
+        .. code-block:: python
+
+            {
+            'type': 'DoorRadiancePropertiesAbridged',
+            'modifier': str,  # A Honeybee Radiance Modifier name
+            'modifier_blk': str  # A Honeybee Radiance Modifier name
+            }
         """
         self._apply_modifiers_from_dict(abridged_data, modifiers)
 
     def to_dict(self, abridged=False):
         """Return radiance properties as a dictionary.
 
         Args:
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/properties/aperture.py` & `honeybee-radiance-1.9.2/honeybee_radiance/properties/aperture.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,38 +5,37 @@
 from ..lib.modifiers import black
 from ..lib.modifiersets import generic_modifier_set_visible
 
 
 class ApertureRadianceProperties(_GeometryRadianceProperties):
     """Radiance Properties for Honeybee Aperture.
 
+    Args:
+        host: A honeybee_core Aperture object that hosts these properties.
+        modifier: A Honeybee Radiance Modifier object for the aperture. If None,
+            it will be set by the parent Room ModifierSet or the Honeybee
+            default generic ModifierSet.
+        modifier_blk: A Honeybee Radiance Modifier object to be used for this
+            aperture in direct solar simulations and in isolation studies (assessing
+            the contribution of individual Apertures). If None, this will be
+            a completely black material.
+
     Properties:
         * host
         * modifier
         * modifier_blk
-        * is_opaque 
+        * is_opaque
         * is_modifier_set_on_object
-        * is_blk_overridden 
+        * is_blk_overridden
     """
 
     __slots__ = ()
 
     def __init__(self, host, modifier=None, modifier_blk=None):
-        """Initialize Aperture radiance properties.
-
-        Args:
-            host: A honeybee_core Aperture object that hosts these properties.
-            modifier: A Honeybee Radiance Modifier object for the aperture. If None,
-                it will be set by the parent Room ModifierSet or the Honeybee
-                default generic ModifierSet.
-            modifier_blk: A Honeybee Radiance Modifier object to be used for this
-                aperture in direct solar simulations and in isolation studies (assessing
-                the contribution of individual Apertures). If None, this will be
-                a completely black material.
-        """
+        """Initialize Aperture radiance properties."""
         _GeometryRadianceProperties.__init__(self, host, modifier, modifier_blk)
 
     @property
     def modifier(self):
         """Get or set the Aperture modifier.
 
         If the modifier is not set on the aperture-level, then it will be assigned
@@ -67,15 +66,15 @@
                 'Expected Radiance Modifier for aperture. Got {}'.format(type(value))
             value.lock()  # lock editing in case modifier has multiple references
         self._modifier = value
 
     @property
     def modifier_blk(self):
         """Get or set a modifier to be used in direct solar and in isolation studies.
-        
+
         If None, this will be a completely black material if the Aperture's modifier
         is opaque and will be equal to the modifier if the Aperture's modifier is non-opaque.
         """
         if self._modifier_blk:  # set by user
             return self._modifier_blk
         return black
 
@@ -91,30 +90,47 @@
     def from_dict(cls, data, host):
         """Create ApertureRadianceProperties from a dictionary.
 
         Note that the dictionary must be a non-abridged version for this
         classmethod to work.
 
         Args:
-            data: A dictionary representation of ApertureRadianceProperties.
+            data: A dictionary representation of ApertureRadianceProperties with the
+                format below.
             host: A Aperture object that hosts these properties.
+
+        .. code-block:: python
+
+            {
+            'type': 'ApertureRadianceProperties',
+            'modifier': {},  # A Honeybee Radiance Modifier dictionary
+            'modifier_blk': {}  # A Honeybee Radiance Modifier dictionary
+            }
         """
         assert data['type'] == 'ApertureRadianceProperties', \
             'Expected ApertureRadianceProperties. Got {}.'.format(data['type'])
         new_prop = cls(host)
         return cls._restore_modifiers_from_dict(new_prop, data)
 
     def apply_properties_from_dict(self, abridged_data, modifiers):
         """Apply properties from a ApertureRadiancePropertiesAbridged dictionary.
 
         Args:
             abridged_data: A ApertureRadiancePropertiesAbridged dictionary (typically
-                coming from a Model).
+                coming from a Model) with the format below.
             modifiers: A dictionary of modifiers with modifier names as keys,
                 which will be used to re-assign modifiers.
+
+        .. code-block:: python
+
+            {
+            'type': 'ApertureRadiancePropertiesAbridged',
+            'modifier': str,  # A Honeybee Radiance Modifier name
+            'modifier_blk': str  # A Honeybee Radiance Modifier name
+            }
         """
         self._apply_modifiers_from_dict(abridged_data, modifiers)
 
     def to_dict(self, abridged=False):
         """Return radiance properties as a dictionary.
 
         Args:
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/properties/model.py` & `honeybee-radiance-1.9.2/honeybee_radiance/properties/model.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,95 +13,94 @@
 except ImportError:
     pass   # python 3
 
 
 class ModelRadianceProperties(object):
     """Radiance Properties for Honeybee Model.
 
+    Args:
+        host: A honeybee_core Model object that hosts these properties.
+
     Properties:
         * host
         * modifiers
         * blk_modifiers
         * room_modifiers
         * face_modifiers
         * shade_modifiers
         * bsdf_modifiers
         * modifier_sets
         * global_modifier_set
     """
 
     def __init__(self, host):
-        """Initialize Model radiance properties.
-
-        Args:
-            host: A honeybee_core Model object that hosts these properties.
-        """
+        """Initialize Model radiance properties."""
         self._host = host
 
     @property
     def host(self):
         """Get the Model object hosting these properties."""
         return self._host
 
     @property
     def modifiers(self):
         """A list of all unique modifiers in the model.
 
         This includes modifiers across all Faces, Apertures, Doors, Shades,
         Room ModifierSets, and the global_modifier_set.
-        
+
         However, it excludes blk_modifiers and these can be obtained separately
         from the blk_modifiers property.
         """
         all_mods = self.global_modifier_set.modifiers_unique + self.room_modifiers + \
             self.face_modifiers + self.shade_modifiers
         return list(set(all_mods))
-    
+
     @property
     def blk_modifiers(self):
         """A list of all unique modifier_blk assigned to Faces, Apertures and Doors."""
         modifiers = [black]
         for room in self.host.rooms:
             for face in room.faces:  # check all Room Face modifiers
                 self._check_and_add_face_modifier_blk(face, modifiers)
         for face in self.host.orphaned_faces:  # check all orphaned Face modifiers
             self._check_and_add_face_modifier_blk(face, modifiers)
         for ap in self.host.orphaned_apertures:  # check all Aperture modifiers
             self._check_and_add_obj_modifier_blk(ap, modifiers)
         for dr in self.host.orphaned_doors:  # check all Door modifiers
             self._check_and_add_obj_modifier_blk(dr, modifiers)
-        
+
         for room in self.host.rooms:
             self._check_and_add_room_modifier_shade_blk(room, modifiers)
         for face in self.host.orphaned_faces:
             self._check_and_add_face_modifier_shade_blk(face, modifiers)
         for ap in self.host.orphaned_apertures:
             self._check_and_add_obj_modifier_shade_blk(ap, modifiers)
         for dr in self.host.orphaned_doors:
             self._check_and_add_obj_modifier_shade_blk(dr, modifiers)
         for shade in self.host.orphaned_shades:
             self._check_and_add_obj_modifier_blk(shade, modifiers)
         return list(set(modifiers))
-    
+
     @property
     def room_modifiers(self):
         """A list of all unique modifiers assigned to Room ModifierSets.
-        
+
         Note that this does not include modifiers in the global_modifier_set.
         For these, you can request global_modifier_set.modifiers_unique.
         """
         room_mods = []
         for cnstr_set in self.modifier_sets:
             room_mods.extend(cnstr_set.modified_modifiers_unique)
         return list(set(room_mods))
 
     @property
     def face_modifiers(self):
         """A list of all unique modifiers assigned to Faces, Apertures and Doors.
-        
+
         This includes both objects that are a part of Rooms as well as orphaned
         objects. It does not include the modfiers of any shades assigned to these
         objects. Nor does it include any blk modifiers.
         """
         modifiers = []
         for room in self.host.rooms:
             for face in room.faces:  # check all Room Face modifiers
@@ -278,19 +277,22 @@
         to load honeybee_radiance objects into their Python object form before
         applying them to the Model geometry.
 
         Args:
             data: A dictionary representation of an entire honeybee-core Model.
                 Note that this dictionary must have ModelRadianceProperties in order
                 for this method to successfully load the radiance properties.
-        
+
         Returns:
-            modifiers -- A dictionary with names of modifiers as keys and Python
+            A tuple with two elements
+
+            -   modifiers: A dictionary with names of modifiers as keys and Python
                 modifier objects as values.
-            modifier_sets -- A dictionary with names of modifier sets as keys
+
+            -   modifier_sets: A dictionary with names of modifier sets as keys
                 and Python modifier set objects as values.
         """
         assert 'radiance' in data['properties'], \
             'Dictionary possesses no ModelRadianceProperties.'
 
         # process all modifiers in the ModelRadianceProperties dictionary
         modifiers = {}
@@ -302,65 +304,65 @@
         if 'modifier_sets' in data['properties']['radiance'] and \
                 data['properties']['radiance']['modifier_sets'] is not None:
             for m_set in data['properties']['radiance']['modifier_sets']:
                 modifier_sets[m_set['name']] = \
                     ModifierSet.from_dict_abridged(m_set, modifiers)
 
         return modifiers, modifier_sets
-    
+
     def _check_and_add_room_modifier_shade(self, room, modifiers):
-        """Check if a modifier is assigned to a Room's shades and add it to a list.""" 
+        """Check if a modifier is assigned to a Room's shades and add it to a list."""
         self._check_and_add_obj_modifier_shade(room, modifiers)
         for face in room.faces:  # check all Face modifiers
             self._check_and_add_face_modifier_shade(face, modifiers)
 
     def _check_and_add_face_modifier_shade(self, face, modifiers):
-        """Check if a modifier is assigned to a Face's shades and add it to a list.""" 
+        """Check if a modifier is assigned to a Face's shades and add it to a list."""
         self._check_and_add_obj_modifier_shade(face, modifiers)
         for ap in face.apertures:  # check all Aperture modifiers
             self._check_and_add_obj_modifier_shade(ap, modifiers)
         for dr in face.doors:  # check all Door Shade modifiers
             self._check_and_add_obj_modifier_shade(dr, modifiers)
-    
+
     def _check_and_add_obj_modifier_shade(self, subf, modifiers):
         """Check if a modifier is assigned to an object's shades and add it to a list."""
         for shade in subf.shades:
             self._check_and_add_obj_modifier(shade, modifiers)
 
     def _check_and_add_room_modifier_shade_blk(self, room, modifiers):
-        """Check if a modifier_blk is assigned to a Room's shades and add it to a list.""" 
+        """Check if a modifier_blk is assigned to a Room's shades and add it to a list."""
         self._check_and_add_obj_modifier_shade_blk(room, modifiers)
         for face in room.faces:  # check all Face modifiers
             self._check_and_add_face_modifier_shade_blk(face, modifiers)
 
     def _check_and_add_face_modifier_shade_blk(self, face, modifiers):
         """Check if a modifier_blk is assigned to a Face's shades and add it to a list.
-        """ 
+        """
         self._check_and_add_obj_modifier_shade_blk(face, modifiers)
         for ap in face.apertures:  # check all Aperture modifiers
             self._check_and_add_obj_modifier_shade_blk(ap, modifiers)
         for dr in face.doors:  # check all Door Shade modifiers
             self._check_and_add_obj_modifier_shade_blk(dr, modifiers)
-    
+
     def _check_and_add_obj_modifier_shade_blk(self, subf, modifiers):
         """Check if a modifier_blk is assigned to an object's shades and add it to list.
         """
         for shade in subf.shades:
             self._check_and_add_obj_modifier_blk(shade, modifiers)
 
     def _check_and_add_face_modifier(self, face, modifiers):
-        """Check if a modifier is assigned to a face and add it to a list.""" 
+        """Check if a modifier is assigned to a face and add it to a list."""
         self._check_and_add_obj_modifier(face, modifiers)
         for ap in face.apertures:  # check all Aperture modifiers
             self._check_and_add_obj_modifier(ap, modifiers)
         for dr in face.doors:  # check all Door modifiers
             self._check_and_add_obj_modifier(dr, modifiers)
-    
+
     def _check_and_add_face_modifier_blk(self, face, modifiers):
-        """Check if a modifier_blk is assigned to a face and add it to a list.""" 
+        """Check if a modifier_blk is assigned to a face and add it to a list."""
         self._check_and_add_obj_modifier_blk(face, modifiers)
         for ap in face.apertures:  # check all Aperture modifiers
             self._check_and_add_obj_modifier_blk(ap, modifiers)
         for dr in face.doors:  # check all Door modifiers
             self._check_and_add_obj_modifier_blk(dr, modifiers)
 
     def _check_and_add_obj_modifier(self, obj, modifiers):
@@ -372,15 +374,15 @@
 
     def _check_and_add_obj_modifier_blk(self, obj, modifiers):
         """Check if a modifier_blk is assigned to an object and add it to a list."""
         mod = obj.properties.radiance._modifier_blk
         if mod is not None:
             if not self._instance_in_array(mod, modifiers):
                 modifiers.append(mod)
-    
+
     def _check_and_add_orphaned_shade_modifier(self, obj, modifiers):
         """Check if a modifier is assigned to an object and add it to a list."""
         mod = obj.properties.radiance._modifier
         if mod is not None:
             if not self._instance_in_array(mod, modifiers):
                 modifiers.append(mod)
         else:
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/properties/face.py` & `honeybee-radiance-1.9.2/honeybee_radiance/properties/face.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,39 +4,38 @@
 from ..modifier import Modifier
 from ..lib.modifiersets import generic_modifier_set_visible
 
 
 class FaceRadianceProperties(_GeometryRadianceProperties):
     """Radiance Properties for Honeybee Face.
 
+    Args:
+        host: A honeybee_core Face object that hosts these properties.
+        modifier: A Honeybee Radiance Modifier object for the face. If None,
+            it will be set by the parent Room ModifierSet or the Honeybee
+            default generic ModifierSet.
+        modifier_blk: A Honeybee Radiance Modifier object to be used for this
+            face in direct solar simulations and in isolation studies (assessing
+            the contribution of individual Apertures). If None, this will be
+            a completely black material if the Face's modifier is opaque and
+            will be equal to the modifier if the Face's modifier is non-opaque.
+
     Properties:
         * host
         * modifier
         * modifier_blk
-        * is_opaque 
+        * is_opaque
         * is_modifier_set_on_object
-        * is_blk_overridden 
+        * is_blk_overridden
     """
 
     __slots__ = ()
 
     def __init__(self, host, modifier=None, modifier_blk=None):
-        """Initialize Face radiance properties.
-
-        Args:
-            host: A honeybee_core Face object that hosts these properties.
-            modifier: A Honeybee Radiance Modifier object for the face. If None,
-                it will be set by the parent Room ModifierSet or the Honeybee
-                default generic ModifierSet.
-            modifier_blk: A Honeybee Radiance Modifier object to be used for this
-                face in direct solar simulations and in isolation studies (assessing
-                the contribution of individual Apertures). If None, this will be
-                a completely black material if the Face's modifier is opaque and
-                will be equal to the modifier if the Face's modifier is non-opaque.
-        """
+        """Initialize Face radiance properties."""
         _GeometryRadianceProperties.__init__(self, host, modifier, modifier_blk)
 
     @property
     def modifier(self):
         """Get or set the Face modifier.
 
         If the modifier is not set on the face-level, then it will be assigned
@@ -67,30 +66,47 @@
     def from_dict(cls, data, host):
         """Create FaceRadianceProperties from a dictionary.
 
         Note that the dictionary must be a non-abridged version for this
         classmethod to work.
 
         Args:
-            data: A dictionary representation of FaceRadianceProperties.
+            data: A dictionary representation of FaceRadianceProperties with the
+                format below.
             host: A Face object that hosts these properties.
+
+        .. code-block:: python
+
+            {
+            'type': 'FaceRadianceProperties',
+            'modifier': {},  # A Honeybee Radiance Modifier dictionary
+            'modifier_blk': {}  # A Honeybee Radiance Modifier dictionary
+            }
         """
         assert data['type'] == 'FaceRadianceProperties', \
             'Expected FaceRadianceProperties. Got {}.'.format(data['type'])
         new_prop = cls(host)
         return cls._restore_modifiers_from_dict(new_prop, data)
 
     def apply_properties_from_dict(self, abridged_data, modifiers):
         """Apply properties from a FaceRadiancePropertiesAbridged dictionary.
 
         Args:
             abridged_data: A FaceRadiancePropertiesAbridged dictionary (typically
-                coming from a Model).
+                coming from a Model) with the format below.
             modifiers: A dictionary of modifiers with modifier names as keys,
                 which will be used to re-assign modifiers.
+
+        .. code-block:: python
+
+            {
+            'type': 'FaceRadiancePropertiesAbridged',
+            'modifier': str,  # A Honeybee Radiance Modifier name
+            'modifier_blk': str  # A Honeybee Radiance Modifier name
+            }
         """
         self._apply_modifiers_from_dict(abridged_data, modifiers)
 
     def to_dict(self, abridged=False):
         """Return radiance properties as a dictionary.
 
         Args:
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/cli/util.py` & `honeybee-radiance-1.9.2/honeybee_radiance/cli/util.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/cli/sunpath.py` & `honeybee-radiance-1.9.2/honeybee_radiance/cli/sunpath.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/cli/sky.py` & `honeybee-radiance-1.9.2/honeybee_radiance/cli/sky.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/cli/grid.py` & `honeybee-radiance-1.9.2/honeybee_radiance/cli/grid.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/cli/__init__.py` & `honeybee-radiance-1.9.2/honeybee_radiance/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/__init__.py` & `honeybee-radiance-1.9.2/honeybee_radiance/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/_extend_honeybee.py` & `honeybee-radiance-1.9.2/honeybee_radiance/_extend_honeybee.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance/primitive.py` & `honeybee-radiance-1.9.2/honeybee_radiance/primitive.py`

 * *Files 3% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 from honeybee._lockable import lockable
 
 from honeybee_radiance.reader import string_to_dicts
 
 
 class Void(object):
     """Void modifier.
-    
+
     Properties:
         * name
         * is_modifier
         * is_opaque
     """
     __slots__ = ()
 
@@ -59,15 +59,31 @@
     def __repr__(self):
         return self.to_radiance()
 
 
 @lockable
 class Primitive(object):
     """Base class for Radiance Primitives.
-    
+
+    Args:
+        name: Primitive name as a string. Cannot contain white spaces or special
+            characters.
+        modifier: Modifier. It can be primitive, mixture, texture or pattern.
+            (Default: "void").
+        values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
+            refer to a line number in the radiance primitve definitions and the
+            values in each array correspond to values occurring within each line.
+            For example, [[], [], ['0.500', '0.500', '0.500', '0.000', '0.050']]
+            corresponds to values one would find for a Plastic material.
+            (Default: [[], [], []]).
+        is_opaque: A boolean to indicate whether this primitive is opaque.
+        dependencies: A list of primitives that this primitive depends on. This
+            argument is only useful for defining advanced primitives that are
+            defined based on other primitives. (Default: []).
+
     Properties:
         * name
         * values
         * modifier
         * dependencies
         * is_geometry
         * is_modifier
@@ -98,47 +114,29 @@
     PATTERNTYPES = set(('colorfunc', 'brightfunc', 'colordata', 'brightdata',
                         'colorpict', 'colortext', 'brighttext'))
 
     MIXTURETYPES = set(('mixfunc', 'mixdata', 'mixpict', 'mixtext'))
 
     # All modifier types (everything except geometry)
     MODIFIERTYPES = set().union(MATERIALTYPES, MIXTURETYPES, TEXTURETYPES, PATTERNTYPES)
-    
+
     # All Radiance primitive types
     TYPES = set().union(GEOMETRYTYPES, MODIFIERTYPES)
 
     # Modifierts that are not usually opaque. This will be used to set is_opaque property
     # if it is not overridded by the user by setting the is_opaque property
     NONEOPAQUETYPES = set(('glass', 'trans', 'trans2', 'transdata', 'transfunc',
                            'dielectric', 'BSDF', 'mixfunc', 'BRTDfunc', 'mist',
                            'prism1', 'prism2'))
 
     VOID = Void()
 
     def __init__(self, name, modifier=None, values=None, is_opaque=None,
                  dependencies=None):
-        """Create primitive base.
-
-        Args:
-            name: Primitive name as a string. Cannot contain white spaces or special
-                characters.
-            modifier: Modifier. It can be primitive, mixture, texture or pattern.
-                (Default: "void").
-            values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
-                refer to a line number in the radiance primitve definitions and the
-                values in each array correspond to values occurring within each line.
-                For example, [[], [], ['0.500', '0.500', '0.500', '0.000', '0.050']]
-                corresponds to values one would find for a Plastic material.
-                (Default: [[], [], []]).
-            is_opaque: A boolean to indicate whether this primitive is opaque.
-            dependencies: A list of primitives that this primitive depends on. This
-                argument is only useful for defining advanced primitives that are
-                defined based on other primitives. (Default: []).
-
-        """
+        """Create primitive base."""
         self.name = name
         self.type = self.__class__.__name__.lower()
         self.modifier = modifier
         self.values = values or [[], [], []]
         self._is_opaque = is_opaque
         self._dependencies = []
         dependencies = dependencies or []
@@ -164,24 +162,24 @@
         The primitive_dict is a dictionary following the base Primitive schema
         of a Radiance object. This base Primitive schema is the same for all
         Radiance Primitives (including Modifiers and Geometry) whereas the
         from_dict classmethod accepts a different schema that is customized
         to each subclass inheriting from the Radiance Primitive.
 
         Args:
-            data: A dictionary in the format below.
+            data: A dictionary in the format below
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "custom", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "custom",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         modifier, dependencies = cls.filter_dict_input(primitive_dict)
 
         cls_ = cls(
             name=primitive_dict['name'],
             modifier=modifier,
@@ -197,22 +195,22 @@
     @classmethod
     def from_dict(cls, data):
         """Initialize the object from a dictionary.
 
         Args:
             data: A dictionary in the format below.
 
-            .. code-block:: python
+        .. code-block:: python
 
             {
-                "modifier": "", // primitive modifier (Default: "void")
-                "type": "custom", // primitive type
-                "name": "", // primitive name
-                "values": [] // values,
-                "dependencies": []
+            "modifier": "",  # primitive modifier (Default: "void")
+            "type": "custom",  # primitive type
+            "name": "",  # primitive name
+            "values": [],  # values
+            "dependencies": []
             }
         """
         return cls.from_primitive_dict(data)
 
     @property
     def type(self):
         """Get or set a string for the primitive type."""
@@ -234,40 +232,40 @@
                         break
 
             assert type_str in self.TYPES, \
                 "%s is not a supported Radiance primitive type." % type_str + \
                 "Try one of these primitives:\n%s" % str(self.TYPES)
 
         self._type = type_str
-    
+
     @property
     def name(self):
         """Get or set the primitive name."""
         return self._name
 
     @name.setter
     def name(self, name):
         self._name = valid_rad_string(name)
 
     @property
     def values(self):
         """Get or set the values of the current primitive as a dictionary.
-        
+
         The keys of this dictionary should be integers between 0 and 2.
 
         Usage:
 
         .. code-block:: python
 
-        # This will erase all values except the first line, which has 9 custom items
-        primitive.values = [
-            [0.5, 0.5, 0.5, "/usr/oakfloor.pic", ".", "frac(U)", "frac(V)", "-s", 1.1667],
-            [],
-            []
-            ]
+            # This will erase all values except the first line, which has 9 custom items
+            primitive.values = [
+                [0.5, 0.5, 0.5, "/usr/oakfloor.pic", ".", "frac(U)", "frac(V)", "-s", 1.1667],
+                [],
+                []
+                ]
         """
         self._update_values()
         return self._values
 
     @values.setter
     def values(self, new_values):
         self._values  = list_with_length(new_values, 3, list, 'radiance primitive values')
@@ -292,15 +290,15 @@
                 raise AssertionError(e)
             else:
                 self._modifier = modifier
 
     @property
     def dependencies(self):
         """Get list of dependencies for this primitive.
-        
+
         Additional dependencies can be added with the add_dependent method.
         """
         return self._dependencies
 
     @property
     def is_geometry(self):
         """Get a boolean noting whether this object is a Radiance geometry."""
@@ -382,15 +380,15 @@
                 output.append(line)
 
         return ' '.join(output) if minimal else '\n'.join(output)
 
     def to_radiance(self, minimal=False, include_modifier=True,
                     include_dependencies=True):
         """Return full radiance definition.
-        
+
         Args:
             minimal: Boolean to note wehther the radiance string should be written
                 in a minimal format (with spaces instead of line breaks). Default: False.
             include_modifier: Boolean to note whether the modifier of this primitive
                 should be included in the string. Default: True.
             include_dependencies: Boolean to note whether the dependencies of this
                 primitive should be included in the string. Default: True.
@@ -432,15 +430,15 @@
 
         # try to get modifier
         if input_dict['modifier'] == 'void':
             modifier = 'void'
         else:
             modifier = mutil.dict_to_modifier(input_dict['modifier'])
 
-        if 'dependencies' not in input_dict: 
+        if 'dependencies' not in input_dict:
             dependencies = []
         else:
             dependencies = [
                 mutil.dict_to_modifier(dep) for dep in input_dict['dependencies']
             ]
 
         return modifier, dependencies
@@ -461,15 +459,15 @@
     def __ne__(self, other):
         return not self.__eq__(other)
 
     def __copy__(self):
         mod, depend = self._dup_mod_and_depend()
         values_copy = [copy(line) for line in self._values]
         return self.__class__(self.name, mod, values_copy, self._is_opaque, depend)
-    
+
     def _dup_mod_and_depend(self):
         """Duplicate this object's modifer and its dependencies."""
         mod = None if isinstance(self._modifier, Void) else self._modifier.duplicate()
         dependencies = [dep.duplicate() for dep in self._dependencies]
         return mod, dependencies
 
     def ToString(self):
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance.egg-info/PKG-INFO` & `honeybee-radiance-1.9.2/honeybee_radiance.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-radiance
-Version: 1.9.1
+Version: 1.9.2
 Summary: Daylight and light simulation extension for honeybee.
 Home-page: https://github.com/ladybug-tools/honeybee-radiance
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: # honeybee-radiance
```

### Comparing `honeybee-radiance-1.9.1/honeybee_radiance.egg-info/SOURCES.txt` & `honeybee-radiance-1.9.2/honeybee_radiance.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -19,14 +19,16 @@
 docs/cli.rst
 docs/conf.py
 docs/index.rst
 docs/modules.rst
 docs/_build/.nojekyll
 docs/_build/README.md
 docs/_build/docs/README.md
+docs/_static/custom.css
+docs/_templates/layout.html
 honeybee_radiance/__init__.py
 honeybee_radiance/__main__.py
 honeybee_radiance/_extend_honeybee.py
 honeybee_radiance/config.json
 honeybee_radiance/config.py
 honeybee_radiance/modifierset.py
 honeybee_radiance/mutil.py
```

