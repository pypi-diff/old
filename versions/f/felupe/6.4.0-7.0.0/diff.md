# Comparing `tmp/felupe-6.4.0.tar.gz` & `tmp/felupe-7.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "felupe-6.4.0.tar", last modified: Sat Apr  1 08:04:16 2023, max compression
+gzip compressed data, was "felupe-7.0.0.tar", last modified: Fri Apr  7 11:58:36 2023, max compression
```

## Comparing `felupe-6.4.0.tar` & `felupe-7.0.0.tar`

### file list

```diff
@@ -1,128 +1,128 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.893940 felupe-6.4.0/
--rw-r--r--   0 runner    (1001) docker     (123)    35081 2023-04-01 08:04:04.000000 felupe-6.4.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    47674 2023-04-01 08:04:16.893940 felupe-6.4.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5963 2023-04-01 08:04:04.000000 felupe-6.4.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     1529 2023-04-01 08:04:04.000000 felupe-6.4.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-01 08:04:16.893940 felupe-6.4.0/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.877940 felupe-6.4.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.877940 felupe-6.4.0/src/felupe/
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/__about__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2469 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.881940 felupe-6.4.0/src/felupe/_assembly/
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_assembly/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6079 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_assembly/_axi.py
--rw-r--r--   0 runner    (1001) docker     (123)    10950 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_assembly/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    23823 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_assembly/_form.py
--rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_assembly/_mixed.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.881940 felupe-6.4.0/src/felupe/_basis/
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_basis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4386 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_basis/_basis.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.881940 felupe-6.4.0/src/felupe/_field/
--rw-r--r--   0 runner    (1001) docker     (123)      176 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_field/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6136 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_field/_axi.py
--rw-r--r--   0 runner    (1001) docker     (123)     9796 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_field/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5352 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_field/_container.py
--rw-r--r--   0 runner    (1001) docker     (123)     4704 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_field/_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_field/_indices.py
--rw-r--r--   0 runner    (1001) docker     (123)     5501 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/_field/_planestrain.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.885940 felupe-6.4.0/src/felupe/constitution/
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6646 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_kinematics.py
--rw-r--r--   0 runner    (1001) docker     (123)    17288 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_mixed.py
--rw-r--r--   0 runner    (1001) docker     (123)     9816 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_models_hyperelasticity.py
--rw-r--r--   0 runner    (1001) docker     (123)     4821 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_models_hyperelasticity_ad.py
--rw-r--r--   0 runner    (1001) docker     (123)    17606 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_models_linear_elasticity.py
--rw-r--r--   0 runner    (1001) docker     (123)     4032 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_models_pseudo_elasticity.py
--rw-r--r--   0 runner    (1001) docker     (123)     8202 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_user_materials.py
--rw-r--r--   0 runner    (1001) docker     (123)     4403 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_user_materials_hyperelastic.py
--rw-r--r--   0 runner    (1001) docker     (123)     5177 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/constitution/_user_materials_models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.885940 felupe-6.4.0/src/felupe/dof/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/dof/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/dof/_boundary.py
--rw-r--r--   0 runner    (1001) docker     (123)     5746 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/dof/_loadcase.py
--rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/dof/_tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.885940 felupe-6.4.0/src/felupe/element/
--rw-r--r--   0 runner    (1001) docker     (123)      407 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    13910 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/_hexahedron.py
--rw-r--r--   0 runner    (1001) docker     (123)     3439 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/_lagrange.py
--rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/_line.py
--rw-r--r--   0 runner    (1001) docker     (123)     8969 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/_quad.py
--rw-r--r--   0 runner    (1001) docker     (123)     4725 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/_tetra.py
--rw-r--r--   0 runner    (1001) docker     (123)     3755 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/element/_triangle.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.885940 felupe-6.4.0/src/felupe/math/
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/math/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2011 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/math/_field.py
--rw-r--r--   0 runner    (1001) docker     (123)     1741 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/math/_math.py
--rw-r--r--   0 runner    (1001) docker     (123)     1985 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/math/_spatial.py
--rw-r--r--   0 runner    (1001) docker     (123)     8763 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/math/_tensor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.889940 felupe-6.4.0/src/felupe/mechanics/
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3076 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_curve.py
--rw-r--r--   0 runner    (1001) docker     (123)     3430 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     5841 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_job.py
--rw-r--r--   0 runner    (1001) docker     (123)     5754 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_multipoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     2702 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_pointload.py
--rw-r--r--   0 runner    (1001) docker     (123)     4633 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_solidbody.py
--rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_solidbody_gravity.py
--rw-r--r--   0 runner    (1001) docker     (123)     7695 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_solidbody_incompressible.py
--rw-r--r--   0 runner    (1001) docker     (123)     3883 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_solidbody_pressure.py
--rw-r--r--   0 runner    (1001) docker     (123)     2721 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mechanics/_step.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.889940 felupe-6.4.0/src/felupe/mesh/
--rw-r--r--   0 runner    (1001) docker     (123)      670 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2272 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4546 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_container.py
--rw-r--r--   0 runner    (1001) docker     (123)     9268 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     7376 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_geometry.py
--rw-r--r--   0 runner    (1001) docker     (123)     4014 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     5756 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_mesh.py
--rw-r--r--   0 runner    (1001) docker     (123)     1750 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_read.py
--rw-r--r--   0 runner    (1001) docker     (123)    13988 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/mesh/_tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.889940 felupe-6.4.0/src/felupe/quadrature/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/quadrature/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/quadrature/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3911 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/quadrature/_gausslegendre.py
--rw-r--r--   0 runner    (1001) docker     (123)     2302 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/quadrature/_tetra.py
--rw-r--r--   0 runner    (1001) docker     (123)     2149 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/quadrature/_triangle.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.889940 felupe-6.4.0/src/felupe/region/
--rw-r--r--   0 runner    (1001) docker     (123)      514 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/region/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8891 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/region/_boundary.py
--rw-r--r--   0 runner    (1001) docker     (123)     4758 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/region/_region.py
--rw-r--r--   0 runner    (1001) docker     (123)     8052 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/region/_templates.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.889940 felupe-6.4.0/src/felupe/solve/
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/solve/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2574 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/solve/_solve.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.889940 felupe-6.4.0/src/felupe/tools/
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1966 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/tools/_check.py
--rw-r--r--   0 runner    (1001) docker     (123)     8398 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/tools/_newton.py
--rw-r--r--   0 runner    (1001) docker     (123)     2001 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/tools/_post.py
--rw-r--r--   0 runner    (1001) docker     (123)     4489 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/tools/_project.py
--rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/tools/_save.py
--rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-04-01 08:04:04.000000 felupe-6.4.0/src/felupe/tools/_solve.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.881940 felupe-6.4.0/src/felupe.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    47674 2023-04-01 08:04:16.000000 felupe-6.4.0/src/felupe.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3213 2023-04-01 08:04:16.000000 felupe-6.4.0/src/felupe.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-01 08:04:16.000000 felupe-6.4.0/src/felupe.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       63 2023-04-01 08:04:16.000000 felupe-6.4.0/src/felupe.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-01 08:04:16.000000 felupe-6.4.0/src/felupe.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 08:04:16.893940 felupe-6.4.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1929 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_bilinearform.py
--rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_composite.py
--rw-r--r--   0 runner    (1001) docker     (123)    12252 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_constitution.py
--rw-r--r--   0 runner    (1001) docker     (123)     3964 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_dof.py
--rw-r--r--   0 runner    (1001) docker     (123)     5262 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_element.py
--rw-r--r--   0 runner    (1001) docker     (123)     4314 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_field.py
--rw-r--r--   0 runner    (1001) docker     (123)     9285 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_form.py
--rw-r--r--   0 runner    (1001) docker     (123)     3810 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_job.py
--rw-r--r--   0 runner    (1001) docker     (123)     4401 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_math.py
--rw-r--r--   0 runner    (1001) docker     (123)    13145 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_mechanics.py
--rw-r--r--   0 runner    (1001) docker     (123)     9996 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_mesh.py
--rw-r--r--   0 runner    (1001) docker     (123)     4028 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_mpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3661 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_planestrain.py
--rw-r--r--   0 runner    (1001) docker     (123)     3970 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_quadrature.py
--rw-r--r--   0 runner    (1001) docker     (123)     3050 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_readme.py
--rw-r--r--   0 runner    (1001) docker     (123)     3782 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_region.py
--rw-r--r--   0 runner    (1001) docker     (123)     2034 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_solve.py
--rw-r--r--   0 runner    (1001) docker     (123)     9257 2023-04-01 08:04:04.000000 felupe-6.4.0/tests/test_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.311094 felupe-7.0.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    35081 2023-04-07 11:58:26.000000 felupe-7.0.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    47965 2023-04-07 11:58:36.311094 felupe-7.0.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     6203 2023-04-07 11:58:26.000000 felupe-7.0.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1544 2023-04-07 11:58:26.000000 felupe-7.0.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 11:58:36.311094 felupe-7.0.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.291093 felupe-7.0.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.295093 felupe-7.0.0/src/felupe/
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/__about__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2618 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.295093 felupe-7.0.0/src/felupe/_assembly/
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_assembly/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6039 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_assembly/_axi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6422 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_assembly/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23823 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_assembly/_form.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4195 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_assembly/_mixed.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.295093 felupe-7.0.0/src/felupe/_basis/
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_basis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4328 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_basis/_basis.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.299093 felupe-7.0.0/src/felupe/_field/
+-rw-r--r--   0 runner    (1001) docker     (123)      176 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_field/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6136 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_field/_axi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9796 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_field/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5352 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_field/_container.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4704 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_field/_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_field/_indices.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5501 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/_field/_planestrain.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.299093 felupe-7.0.0/src/felupe/constitution/
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6588 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_kinematics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17288 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_mixed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9816 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_models_hyperelasticity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4821 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_models_hyperelasticity_ad.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17606 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_models_linear_elasticity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4032 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_models_pseudo_elasticity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8202 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_user_materials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4403 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_user_materials_hyperelastic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5177 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/constitution/_user_materials_models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.299093 felupe-7.0.0/src/felupe/dof/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/dof/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/dof/_boundary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5746 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/dof/_loadcase.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/dof/_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.299093 felupe-7.0.0/src/felupe/element/
+-rw-r--r--   0 runner    (1001) docker     (123)      407 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13838 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/_hexahedron.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3439 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/_lagrange.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/_line.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10019 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/_quad.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4725 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/_tetra.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3755 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/element/_triangle.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.303094 felupe-7.0.0/src/felupe/math/
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/math/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2011 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/math/_field.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1741 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/math/_math.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1985 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/math/_spatial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8705 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/math/_tensor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.303094 felupe-7.0.0/src/felupe/mechanics/
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3076 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_curve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3410 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5952 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_job.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5661 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_multipoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2680 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_pointload.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4565 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_solidbody.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2676 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_solidbody_gravity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7497 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_solidbody_incompressible.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3815 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_solidbody_pressure.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2721 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mechanics/_step.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.303094 felupe-7.0.0/src/felupe/mesh/
+-rw-r--r--   0 runner    (1001) docker     (123)      680 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2272 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4546 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_container.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9293 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3642 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_discrete_geometry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7376 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_geometry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4126 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6990 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_mesh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_read.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14839 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/mesh/_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.307094 felupe-7.0.0/src/felupe/quadrature/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/quadrature/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/quadrature/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3911 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/quadrature/_gausslegendre.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2302 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/quadrature/_tetra.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2149 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/quadrature/_triangle.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.307094 felupe-7.0.0/src/felupe/region/
+-rw-r--r--   0 runner    (1001) docker     (123)      663 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/region/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13133 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/region/_boundary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5172 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/region/_region.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10142 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/region/_templates.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.307094 felupe-7.0.0/src/felupe/solve/
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/solve/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2574 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/solve/_solve.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.307094 felupe-7.0.0/src/felupe/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8132 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/tools/_newton.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2001 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/tools/_post.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5250 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/tools/_project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/tools/_save.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-04-07 11:58:26.000000 felupe-7.0.0/src/felupe/tools/_solve.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.295093 felupe-7.0.0/src/felupe.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    47965 2023-04-07 11:58:36.000000 felupe-7.0.0/src/felupe.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3224 2023-04-07 11:58:36.000000 felupe-7.0.0/src/felupe.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:58:36.000000 felupe-7.0.0/src/felupe.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-07 11:58:36.000000 felupe-7.0.0/src/felupe.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 11:58:36.000000 felupe-7.0.0/src/felupe.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:58:36.311094 felupe-7.0.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1929 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_bilinearform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_composite.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12252 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_constitution.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3964 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_dof.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5262 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_element.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4314 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_field.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8302 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_form.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3810 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_job.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4401 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_math.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12303 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_mechanics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11203 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_mesh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7135 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_mpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3661 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_planestrain.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3970 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_quadrature.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3050 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_readme.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4003 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_region.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2034 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_solve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8758 2023-04-07 11:58:26.000000 felupe-7.0.0/tests/test_tools.py
```

### Comparing `felupe-6.4.0/LICENSE` & `felupe-7.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/PKG-INFO` & `felupe-7.0.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: felupe
-Version: 6.4.0
+Version: 7.0.0
 Summary: Finite Element Analysis
 Author: Andreas Dutzler
 Author-email: a.dutzler@gmail.com
 License: GNU GENERAL PUBLIC LICENSE
                                Version 3, 29 June 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
@@ -690,38 +690,39 @@
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Scientific/Engineering
 Classifier: Topic :: Scientific/Engineering :: Mathematics
 Classifier: Topic :: Utilities
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Provides-Extra: all
 License-File: LICENSE
 
-# FElupe - Finite Element Analysis
+# 🔍 FElupe - Finite Element Analysis
 
 [![PyPI version shields.io](https://img.shields.io/pypi/v/felupe.svg)](https://pypi.python.org/pypi/felupe/) [![Documentation Status](https://readthedocs.org/projects/felupe/badge/?version=latest)](https://felupe.readthedocs.io/en/latest/?badge=latest) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![Made with love in Graz (Austria)](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20in-Graz%20(Austria)-0c674a) [![codecov](https://codecov.io/gh/adtzlr/felupe/branch/main/graph/badge.svg?token=J2QP6Y6LVH)](https://codecov.io/gh/adtzlr/felupe) [![DOI](https://zenodo.org/badge/360657894.svg)](https://zenodo.org/badge/latestdoi/360657894) ![Codestyle black](https://img.shields.io/badge/code%20style-black-black) ![GitHub Repo stars](https://img.shields.io/github/stars/adtzlr/felupe?logo=github) ![PyPI - Downloads](https://img.shields.io/pypi/dm/felupe)
 
-<img src="https://raw.githubusercontent.com/adtzlr/felupe/main/docs/_static/logo_light.svg" width="220px"/>
+<img src="https://raw.githubusercontent.com/adtzlr/felupe/main/docs/_static/logo_light.svg" height="120px"/> <img src="https://user-images.githubusercontent.com/5793153/230604246-5a416081-6777-4f33-afdf-efdb51338722.png" height="120px"/> <img src="https://user-images.githubusercontent.com/5793153/230604587-42e3e339-e08c-4cc8-8000-f7046a8d95df.png" height="120px"/>
 
 FElupe is a Python 3.7+ finite element analysis package focussing on the formulation and numerical solution of nonlinear problems in continuum mechanics of solid bodies. Its name is a combination of FE (finite element) and the german word *Lupe* (magnifying glass) as a synonym for getting an insight how a finite element analysis code looks like under the hood.
 
 # Installation
 Install Python, fire up a terminal and run
 
 ```shell
 pip install felupe[all]
 ```
 
-where `[all]` installs all optional dependencies. By default, FElupe only depends on `numpy` and `scipy`. In order to make use of all features of FElupe, it is suggested to install all optional dependencies (`einsumt`, `h5py`, `meshio`, `numba`, `sparse` and `tensortrax`).
+where `[all]` installs all optional dependencies. By default, FElupe depends on `numpy`, `scipy` and `einsumt`. In order to make use of all features of FElupe, it is suggested to install all optional dependencies (`h5py`, `meshio` and `tensortrax`).
 
 # Getting Started
 A quarter model of a solid cube with hyperelastic material behaviour is subjected to a uniaxial elongation applied at a clamped end-face. This involves the creation of a mesh, a region as well as a displacement field (encapsulated in a field container). Furthermore, the boundary conditions are created by a template for a uniaxial loadcase. An isotropic pseudo-elastic Ogden-Roxburgh Mullins-softening model formulation in combination with an isotropic hyperelastic Neo-Hookean material formulation is applied on a nearly-incompressible solid body. A step generates the consecutive substep-movements of a given boundary condition. The step is further added to a list of steps of a job (here, a characteristic-curve job is used). During evaluation, each substep of each step is solved by an iterative Newton-Rhapson procedure. The solution is exported after each completed substep as a time-series XDMF file. For more details beside this high-level code snippet, please have a look at the [documentation](https://felupe.readthedocs.io/en/latest/?badge=latest).
 
 ```python
 import felupe as fem
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `felupe-6.4.0/README.md` & `felupe-7.0.0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,23 +1,23 @@
-# FElupe - Finite Element Analysis
+# 🔍 FElupe - Finite Element Analysis
 
 [![PyPI version shields.io](https://img.shields.io/pypi/v/felupe.svg)](https://pypi.python.org/pypi/felupe/) [![Documentation Status](https://readthedocs.org/projects/felupe/badge/?version=latest)](https://felupe.readthedocs.io/en/latest/?badge=latest) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![Made with love in Graz (Austria)](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20in-Graz%20(Austria)-0c674a) [![codecov](https://codecov.io/gh/adtzlr/felupe/branch/main/graph/badge.svg?token=J2QP6Y6LVH)](https://codecov.io/gh/adtzlr/felupe) [![DOI](https://zenodo.org/badge/360657894.svg)](https://zenodo.org/badge/latestdoi/360657894) ![Codestyle black](https://img.shields.io/badge/code%20style-black-black) ![GitHub Repo stars](https://img.shields.io/github/stars/adtzlr/felupe?logo=github) ![PyPI - Downloads](https://img.shields.io/pypi/dm/felupe)
 
-<img src="https://raw.githubusercontent.com/adtzlr/felupe/main/docs/_static/logo_light.svg" width="220px"/>
+<img src="https://raw.githubusercontent.com/adtzlr/felupe/main/docs/_static/logo_light.svg" height="120px"/> <img src="https://user-images.githubusercontent.com/5793153/230604246-5a416081-6777-4f33-afdf-efdb51338722.png" height="120px"/> <img src="https://user-images.githubusercontent.com/5793153/230604587-42e3e339-e08c-4cc8-8000-f7046a8d95df.png" height="120px"/>
 
 FElupe is a Python 3.7+ finite element analysis package focussing on the formulation and numerical solution of nonlinear problems in continuum mechanics of solid bodies. Its name is a combination of FE (finite element) and the german word *Lupe* (magnifying glass) as a synonym for getting an insight how a finite element analysis code looks like under the hood.
 
 # Installation
 Install Python, fire up a terminal and run
 
 ```shell
 pip install felupe[all]
 ```
 
-where `[all]` installs all optional dependencies. By default, FElupe only depends on `numpy` and `scipy`. In order to make use of all features of FElupe, it is suggested to install all optional dependencies (`einsumt`, `h5py`, `meshio`, `numba`, `sparse` and `tensortrax`).
+where `[all]` installs all optional dependencies. By default, FElupe depends on `numpy`, `scipy` and `einsumt`. In order to make use of all features of FElupe, it is suggested to install all optional dependencies (`h5py`, `meshio` and `tensortrax`).
 
 # Getting Started
 A quarter model of a solid cube with hyperelastic material behaviour is subjected to a uniaxial elongation applied at a clamped end-face. This involves the creation of a mesh, a region as well as a displacement field (encapsulated in a field container). Furthermore, the boundary conditions are created by a template for a uniaxial loadcase. An isotropic pseudo-elastic Ogden-Roxburgh Mullins-softening model formulation in combination with an isotropic hyperelastic Neo-Hookean material formulation is applied on a nearly-incompressible solid body. A step generates the consecutive substep-movements of a given boundary condition. The step is further added to a list of steps of a job (here, a characteristic-curve job is used). During evaluation, each substep of each step is solved by an iterative Newton-Rhapson procedure. The solution is exported after each completed substep as a time-series XDMF file. For more details beside this high-level code snippet, please have a look at the [documentation](https://felupe.readthedocs.io/en/latest/?badge=latest).
 
 ```python
 import felupe as fem
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `felupe-6.4.0/pyproject.toml` & `felupe-7.0.0/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -30,32 +30,31 @@
   "Operating System :: OS Independent",
   "Programming Language :: Python",
   "Programming Language :: Python :: 3",
   "Programming Language :: Python :: 3.7",
   "Programming Language :: Python :: 3.8",
   "Programming Language :: Python :: 3.9",
   "Programming Language :: Python :: 3.10",
+  "Programming Language :: Python :: 3.11",
   "Topic :: Scientific/Engineering",
   "Topic :: Scientific/Engineering :: Mathematics",
   "Topic :: Utilities"
 ]
 dynamic = ["version"]
 requires-python = ">=3.7"
 dependencies = [
   "numpy",
   "scipy",
+  "einsumt",
 ]
 
 [project.optional-dependencies]
 all = [
     "meshio",
     "h5py",
-    "numba",
-    "sparse",
-    "einsumt",
     "tensortrax",
 ]
 
 [tool.setuptools.dynamic]
 version = {attr = "felupe.__about__.__version__"}
 
 [project.urls]
```

### Comparing `felupe-6.4.0/src/felupe/__init__.py` & `felupe-7.0.0/src/felupe/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -59,31 +59,35 @@
 from .mesh import Cube, Grid, Mesh, MeshContainer, Rectangle
 from .quadrature import GaussLegendre, GaussLegendreBoundary
 from .quadrature import Tetrahedron as TetrahedronQuadrature
 from .quadrature import Triangle as TriangleQuadrature
 from .region import (
     Region,
     RegionBiQuadraticQuad,
+    RegionBiQuadraticQuadBoundary,
     RegionBoundary,
     RegionConstantHexahedron,
     RegionConstantQuad,
     RegionHexahedron,
     RegionHexahedronBoundary,
     RegionLagrange,
     RegionQuad,
     RegionQuadBoundary,
     RegionQuadraticHexahedron,
+    RegionQuadraticHexahedronBoundary,
     RegionQuadraticQuad,
+    RegionQuadraticQuadBoundary,
     RegionQuadraticTetra,
     RegionQuadraticTriangle,
     RegionTetra,
     RegionTetraMINI,
     RegionTriangle,
     RegionTriangleMINI,
     RegionTriQuadraticHexahedron,
+    RegionTriQuadraticHexahedronBoundary,
 )
 
 try:
     from .constitution import UserMaterialHyperelastic
 except:
     pass
 from .mechanics import (
```

### Comparing `felupe-6.4.0/src/felupe/_assembly/_axi.py` & `felupe-7.0.0/src/felupe/_assembly/_axi.py`

 * *Files 1% similar despite different names*

```diff
@@ -130,16 +130,16 @@
 
                 form_a = IntegralForm(fun, v, self.dV, u, False, False)
 
                 self.forms = [
                     form_a,
                 ]
 
-    def integrate(self, parallel=False, jit=False):
-        values = [form.integrate(parallel=parallel, jit=jit) for form in self.forms]
+    def integrate(self, parallel=False):
+        values = [form.integrate(parallel=parallel) for form in self.forms]
 
         if self.mode == 1:
             values[0] += np.pad(values[1], ((0, 0), (1, 0), (0, 0)))
             val = values[0]
 
         if self.mode == 30:
             if len(values[0].shape) > 4:
@@ -171,11 +171,11 @@
             val = values[0]
 
         elif self.mode == 10 or self.mode == 40:
             val = values[0]
 
         return val
 
-    def assemble(self, values=None, parallel=False, jit=False):
+    def assemble(self, values=None, parallel=False):
         if values is None:
-            values = self.integrate(parallel=parallel, jit=jit)
+            values = self.integrate(parallel=parallel)
         return self.forms[0].assemble(values)
```

### Comparing `felupe-6.4.0/src/felupe/_assembly/_form.py` & `felupe-7.0.0/src/felupe/_assembly/_form.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/_assembly/_mixed.py` & `felupe-7.0.0/src/felupe/_assembly/_mixed.py`

 * *Files 2% similar despite different names*

```diff
@@ -98,23 +98,23 @@
                     grad_v=self.grad_v[i],
                     grad_u=self.grad_u[j],
                 )
                 self.forms.append(f)
         else:
             raise ValueError("Unknown input format.")
 
-    def assemble(self, values=None, parallel=False, jit=False, block=True):
+    def assemble(self, values=None, parallel=False, block=True):
 
         out = []
 
         if values is None:
             values = [None] * len(self.forms)
 
         for val, form in zip(values, self.forms):
-            out.append(form.assemble(val, parallel=parallel, jit=jit))
+            out.append(form.assemble(val, parallel=parallel))
 
         if block and self.mode == 2:
             K = np.zeros((self.nv, self.nv), dtype=object)
             for a, (i, j) in enumerate(zip(self.i, self.j)):
                 K[i, j] = out[a]
                 if i != j:
                     K[j, i] = out[a].T
@@ -123,14 +123,14 @@
 
         if block and self.mode == 1:
             return vstack(out).tocsr()
 
         else:
             return out
 
-    def integrate(self, parallel=False, jit=False):
+    def integrate(self, parallel=False):
 
         out = []
         for form in self.forms:
-            out.append(form.integrate(parallel=parallel, jit=jit))
+            out.append(form.integrate(parallel=parallel))
 
         return out
```

### Comparing `felupe-6.4.0/src/felupe/_basis/_basis.py` & `felupe-7.0.0/src/felupe/_basis/_basis.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,19 +22,15 @@
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 import numpy as np
-
-try:
-    from einsumt import einsumt
-except:
-    from numpy import einsum as einsumt
+from einsumt import einsumt
 
 
 class Basis:
     r"""A basis and its gradient built on top of a scalar- or vector-valued
     field. *Basis* refers to the trial and test field, either values or
     gradients evaluated at quadrature points. The first two indices of a basis
     are used for looping over the element shape functions ``a`` and its
```

### Comparing `felupe-6.4.0/src/felupe/_field/_axi.py` & `felupe-7.0.0/src/felupe/_field/_axi.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/_field/_base.py` & `felupe-7.0.0/src/felupe/_field/_base.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/_field/_container.py` & `felupe-7.0.0/src/felupe/_field/_container.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/_field/_fields.py` & `felupe-7.0.0/src/felupe/_field/_fields.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/_field/_indices.py` & `felupe-7.0.0/src/felupe/_field/_indices.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/_field/_planestrain.py` & `felupe-7.0.0/src/felupe/_field/_planestrain.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/__init__.py` & `felupe-7.0.0/src/felupe/constitution/__init__.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_kinematics.py` & `felupe-7.0.0/src/felupe/constitution/_kinematics.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,19 +22,15 @@
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 import numpy as np
-
-try:
-    from einsumt import einsumt
-except:
-    from numpy import einsum as einsumt
+from einsumt import einsumt
 
 from ..math import cdya_ik, cdya_il, det, dot, dya, identity, inv, transpose
 
 
 class LineChange:
     r"""Line Change.
```

### Comparing `felupe-6.4.0/src/felupe/constitution/_mixed.py` & `felupe-7.0.0/src/felupe/constitution/_mixed.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_models_hyperelasticity.py` & `felupe-7.0.0/src/felupe/constitution/_models_hyperelasticity.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_models_hyperelasticity_ad.py` & `felupe-7.0.0/src/felupe/constitution/_models_hyperelasticity_ad.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_models_linear_elasticity.py` & `felupe-7.0.0/src/felupe/constitution/_models_linear_elasticity.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_models_pseudo_elasticity.py` & `felupe-7.0.0/src/felupe/constitution/_models_pseudo_elasticity.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_user_materials.py` & `felupe-7.0.0/src/felupe/constitution/_user_materials.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_user_materials_hyperelastic.py` & `felupe-7.0.0/src/felupe/constitution/_user_materials_hyperelastic.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/constitution/_user_materials_models.py` & `felupe-7.0.0/src/felupe/constitution/_user_materials_models.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/dof/_boundary.py` & `felupe-7.0.0/src/felupe/dof/_boundary.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/dof/_loadcase.py` & `felupe-7.0.0/src/felupe/dof/_loadcase.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/dof/_tools.py` & `felupe-7.0.0/src/felupe/dof/_tools.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/element/_base.py` & `felupe-7.0.0/src/felupe/element/_base.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/element/_hexahedron.py` & `felupe-7.0.0/src/felupe/element/_hexahedron.py`

 * *Files 1% similar despite different names*

```diff
@@ -338,27 +338,24 @@
                 #
                 [0, -1, 1],
                 [1, 0, 1],
                 [0, 1, 1],
                 [-1, 0, 1],
                 #
                 [-1, -1, 0],
-                [1, 1, 0],
+                [1, -1, 0],
                 [1, 1, 0],
                 [-1, 1, 0],
                 #
-                [0, -1, 0],
-                [1, 0, 0],
-                [0, 1, 0],
-                [-1, 0, 0],
-                #
                 [-1, 0, 0],
                 [1, 0, 0],
                 [0, -1, 0],
                 [0, 1, 0],
+                [0, 0, -1],
+                [0, 0, 1],
                 #
                 [0, 0, 0],
             ],
             dtype=float,
         )
 
         self._lagrange = ArbitraryOrderLagrange(order=2, dim=3)
```

### Comparing `felupe-6.4.0/src/felupe/element/_lagrange.py` & `felupe-7.0.0/src/felupe/element/_lagrange.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/element/_line.py` & `felupe-7.0.0/src/felupe/element/_line.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/element/_quad.py` & `felupe-7.0.0/src/felupe/element/_quad.py`

 * *Files 12% similar despite different names*

```diff
@@ -292,14 +292,40 @@
         dhds[ra == 0] = (1 - r**2) * sa[ra == 0] / 2
         dhds[sa == 0] = (1 + ra[sa == 0] * r) * -2 * s / 2
 
         return np.vstack([dhdr, dhds]).T
 
 
 class BiQuadraticQuad(Element):
+    r"""Bi-Quadratic Lagrange quadrilateral element.
+
+    ..  code-block::
+
+                      ^ s
+         3 (-1/ 1)    |6 ( 0/ 1)   2 ( 1/ 1)
+          o-----------o-----------o
+          |           |           |
+          |           |           |
+          |           |           |
+          |7 (-1/ 0)  |8 ( 0/ 0)  |5 ( 1/ 0)
+          o      -----o-----------o-----> r
+          |           |           |
+          |           |           |
+          |                       |
+          |                       |
+          o-----------o-----------o
+        0 (-1/-1)     4 ( 0/-1)    1 ( 1/-1)
+
+
+    Attributes
+    ----------
+    points : ndarray
+        Array with point locations in natural coordinate system
+    """
+
     def __init__(self):
         super().__init__(shape=(9, 2))
 
         self._lagrange = ArbitraryOrderLagrange(order=2, dim=2)
 
         self._vertices = np.array([0, 2, 8, 6])
         self._edges = np.array([1, 5, 7, 3])
@@ -308,16 +334,27 @@
 
         self._permute = np.concatenate(
             (self._vertices, self._edges, self._faces, self._volume)
         )
 
         self.points = self._lagrange.points[self._permute]
 
-    def function(self, rst):
-        "quadratic quad shape functions"
+    def function(self, rs):
+        r"""Bi-Quadratic Lagrange quadrilateral - shape functions."""
+
+        return self._lagrange.function(rs)[self._permute]
 
-        return self._lagrange.function(rst)[self._permute]
+    def gradient(self, rs):
+        r"""Bi-Quadratic Lagrange quadrilateral - gradient of shape functions.
 
-    def gradient(self, rst):
-        "quadratic quad gradient of shape functions"
+        Arguments
+        ---------
+        rs : ndarray
+            Point as coordinate vector for gradient of shape function evaluation
+
+        Returns
+        -------
+        ndarray
+            Gradient of shape functions evaluated at given location
+        """
 
-        return self._lagrange.gradient(rst)[self._permute, :]
+        return self._lagrange.gradient(rs)[self._permute, :]
```

### Comparing `felupe-6.4.0/src/felupe/element/_tetra.py` & `felupe-7.0.0/src/felupe/element/_tetra.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/element/_triangle.py` & `felupe-7.0.0/src/felupe/element/_triangle.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/math/_field.py` & `felupe-7.0.0/src/felupe/math/_field.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/math/_math.py` & `felupe-7.0.0/src/felupe/math/_math.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/math/_spatial.py` & `felupe-7.0.0/src/felupe/math/_spatial.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/math/_tensor.py` & `felupe-7.0.0/src/felupe/math/_tensor.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,19 +22,15 @@
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 import numpy as np
-
-try:
-    from einsumt import einsumt
-except:
-    from numpy import einsum as einsumt
+from einsumt import einsumt
 
 
 def identity(A=None, dim=None, shape=None):
     "Identity according to matrix A with optional specified dim."
     if A is not None:
         dimA, g, e = A.shape[-3:]
         if dim is None:
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_curve.py` & `felupe-7.0.0/src/felupe/mechanics/_curve.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/mechanics/_helpers.py` & `felupe-7.0.0/src/felupe/mechanics/_helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -91,20 +91,20 @@
         # deformation gradient
         self.F = field.extract()
 
         # cell-values of the internal pressure and volume-ratio fields
         self.p = np.zeros(field.region.mesh.ncells)
         self.J = np.ones(field.region.mesh.ncells)
 
-    def h(self, parallel=False, jit=False):
+    def h(self, parallel=False):
         "Integrated shape-function gradient w.r.t. the deformed coordinates `x`."
 
         return IntegralFormMixed(
             fun=self.dJdF(self.F), v=self.field, dV=self.field.region.dV
-        ).integrate(parallel=parallel, jit=jit)[0]
+        ).integrate(parallel=parallel)[0]
 
     def v(self):
         "Cell volumes of the deformed configuration."
         dV = self.field.region.dV
         if isinstance(self.field[0], FieldAxisymmetric):
             R = self.field[0].radius
             dA = self.field.region.dV
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_job.py` & `felupe-7.0.0/src/felupe/mechanics/_job.py`

 * *Files 5% similar despite different names*

```diff
@@ -21,14 +21,16 @@
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
+from platform import architecture, machine, platform
+
 import numpy as np
 
 from ..__about__ import __version__ as version
 from ..math import dot, eigh, eigvalsh, tovoigt, transpose
 
 
 def displacement(substep):
@@ -100,15 +102,15 @@
  _______  _______  ___      __   __  _______  _______ 
 |       ||       ||   |    |  | |  ||       ||       |
 |    ___||    ___||   |    |  | |  ||    _  ||    ___|
 |   |___ |   |___ |   |    |  |_|  ||   |_| ||   |___ 
 |    ___||    ___||   |___ |       ||    ___||    ___|
 |   |    |   |___ |       ||       ||   |    |   |___ 
 |___|    |_______||_______||_______||___|    |_______|
-FElupe Version {version}
+FElupe Version {version} ({platform(terse=True)} {machine()} {architecture()[0]})
 
 """
             )
 
             print("Run Job")
             print("=======\n")
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_multipoint.py` & `felupe-7.0.0/src/felupe/mechanics/_multipoint.py`

 * *Files 22% similar despite different names*

```diff
@@ -22,133 +22,142 @@
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 import numpy as np
-import sparse
+from scipy.sparse import eye, lil_matrix
 
 from ._helpers import Assemble, Results
 
 
 class MultiPointConstraint:
     def __init__(
         self, field, points, centerpoint, skip=(False, False, False), multiplier=1e3
     ):
         "RBE2 Multi-point-constraint."
         self.field = field
         self.mesh = field.region.mesh
-        self.points = points
+        self.points = np.asarray(points)
         self.centerpoint = centerpoint
         self.mask = ~np.array(skip, dtype=bool)[: self.mesh.dim]
         self.axes = np.arange(self.mesh.dim)[self.mask]
         self.multiplier = multiplier
 
         self.results = Results(stress=False, elasticity=False)
         self.assemble = Assemble(vector=self._vector, matrix=self._matrix)
 
-    def _vector(self, field=None, parallel=False, jit=False):
+    def _vector(self, field=None, parallel=False):
         "Calculate vector of residuals with RBE2 contributions."
+
         if field is not None:
             self.field = field
-        f = self.field.fields[0]
-        r = sparse.DOK(shape=(self.mesh.npoints, self.mesh.dim))
-        c = self.centerpoint
-        for t in self.points:
-            for d in self.axes:
-                N = self.multiplier * (-f.values[t, d] + f.values[c, d])
-                r[t, d] = -N
-                r[c, d] += N
-        self.results.force = sparse.COO(r).reshape((-1, 1)).tocsr()
+
+        u = self.field.fields[0].values
+        N = self.multiplier * (-u[self.points] + u[self.centerpoint])
+        N[:, ~self.mask] = 0
+
+        r = lil_matrix(u.shape)
+        r[self.points] = -N
+        r[self.centerpoint] = N.sum(axis=0)
+
+        self.results.force = r.reshape(-1, 1).tocsr()
         return self.results.force
 
-    def _matrix(self, field=None, parallel=False, jit=False):
+    def _matrix(self, field=None, parallel=False):
         "Calculate stiffness with RBE2 contributions."
+
         if field is not None:
             self.field = field
-        L = sparse.DOK(
-            shape=(self.mesh.npoints, self.mesh.dim, self.mesh.npoints, self.mesh.dim)
-        )
-        c = self.centerpoint
-        for t in self.points:
-            for d in self.axes:
-                L[t, d, t, d] = self.multiplier
-                L[t, d, c, d] = -self.multiplier
-                L[c, d, t, d] = -self.multiplier
-                L[c, d, c, d] += self.multiplier
-        self.results.stiffness = (
-            sparse.COO(L)
-            .reshape(
-                (self.mesh.npoints * self.mesh.dim, self.mesh.npoints * self.mesh.dim)
-            )
-            .tocsr()
-        )
+
+        indices = np.arange(self.mesh.ndof).reshape(self.mesh.points.shape)
+        td = [indices[self.points.reshape(-1, 1), ax].ravel() for ax in self.axes]
+        cd = [indices[self.centerpoint, ax].ravel() for ax in self.axes]
+
+        L = lil_matrix((self.mesh.ndof, self.mesh.ndof))
+
+        for t, c in zip(td, cd):
+
+            L[t.reshape(-1, 1), t] = eye(len(t)) * self.multiplier
+            L[t.reshape(-1, 1), c] = -self.multiplier
+            L[c.reshape(-1, 1), t] = -self.multiplier
+            L[c.reshape(-1, 1), c] = eye(len(c)) * self.multiplier * len(self.points)
+
+        self.results.stiffness = L.tocsr()
         return self.results.stiffness
 
 
 class MultiPointContact:
     def __init__(
         self, field, points, centerpoint, skip=(False, False, False), multiplier=1e6
     ):
         "RBE2 Multi-point-bolt-constraint."
         self.field = field
         self.mesh = field.region.mesh
-        self.points = points
+        self.points = np.asarray(points)
         self.centerpoint = centerpoint
         self.mask = ~np.array(skip, dtype=bool)[: self.mesh.dim]
         self.axes = np.arange(self.mesh.dim)[self.mask]
         self.multiplier = multiplier
 
         self.results = Results(stress=False, elasticity=False)
         self.assemble = Assemble(vector=self._vector, matrix=self._matrix)
 
-    def _vector(self, field=None):
+    def _vector(self, field=None, parallel=False):
         "Calculate vector of residuals with RBE2 contributions."
+
         if field is not None:
             self.field = field
-        f = self.field.fields[0]
-        r = sparse.DOK(shape=(self.mesh.npoints, self.mesh.dim))
-        c = self.centerpoint
-        for t in self.points:
-            for d in self.axes:
-                Xc = self.mesh.points[c, d]
-                Xt = self.mesh.points[t, d]
-                xc = f.values[c, d] + Xc
-                xt = f.values[t, d] + Xt
-                if np.sign(-Xt + Xc) != np.sign(-xt + xc):
-                    n = -xt + xc
-                    r[t, d] = -self.multiplier * n
-                    r[c, d] += self.multiplier * n
-        self.results.force = sparse.COO(r).reshape((-1, 1)).tocsr()
+
+        u = self.field.fields[0].values
+
+        Xc = self.mesh.points[self.centerpoint]
+        Xt = self.mesh.points[self.points]
+
+        xc = u[self.centerpoint] + Xc
+        xt = u[self.points] + Xt
+
+        mask = np.sign(-Xt + Xc) == np.sign(-xt + xc)
+        mask[:, ~self.mask] = True
+        n = -xt + xc
+        n[mask] = 0
+
+        r = lil_matrix(u.shape)
+        r[self.points] = -self.multiplier * n
+        r[self.centerpoint] = self.multiplier * n.sum(axis=0)
+
+        self.results.force = r.reshape(-1, 1).tocsr()
         return self.results.force
 
-    def _matrix(self, field=None):
+    def _matrix(self, field=None, parallel=False):
         "Calculate stiffness with RBE2 contributions."
+
         if field is not None:
             self.field = field
-        f = self.field.fields[0]
-        L = sparse.DOK(
-            shape=(self.mesh.npoints, self.mesh.dim, self.mesh.npoints, self.mesh.dim)
-        )
-        c = self.centerpoint
-        for t in self.points:
-            for d in self.axes:
-                Xc = self.mesh.points[c, d]
-                Xt = self.mesh.points[t, d]
-                xc = f.values[c, d] + Xc
-                xt = f.values[t, d] + Xt
-                # n = 0
-                if np.sign(-Xt + Xc) != np.sign(-xt + xc):
-                    # n = -xt + xc
-                    L[t, d, t, d] = self.multiplier
-                    L[t, d, c, d] = -self.multiplier
-                    L[c, d, t, d] = -self.multiplier
-                    L[c, d, c, d] += self.multiplier
-        self.results.stiffness = (
-            sparse.COO(L)
-            .reshape(
-                (self.mesh.npoints * self.mesh.dim, self.mesh.npoints * self.mesh.dim)
-            )
-            .tocsr()
-        )
+
+        u = self.field.fields[0].values
+
+        Xc = self.mesh.points[self.centerpoint]
+        Xt = self.mesh.points[self.points]
+
+        xc = u[self.centerpoint] + Xc
+        xt = u[self.points] + Xt
+
+        mask = np.sign(-Xt + Xc) != np.sign(-xt + xc)
+        masks = [mask[:, ax] for ax in self.axes]
+
+        indices = np.arange(self.mesh.ndof).reshape(self.mesh.points.shape)
+        td = [indices[self.points.reshape(-1, 1), ax].ravel() for ax in self.axes]
+        cd = [indices[self.centerpoint, ax].ravel() for ax in self.axes]
+
+        L = lil_matrix((self.mesh.ndof, self.mesh.ndof))
+
+        for t, c, m in zip(td, cd, masks):
+
+            L[t[m].reshape(-1, 1), t[m]] = eye(len(t[m])) * self.multiplier
+            L[t[m].reshape(-1, 1), c] = -self.multiplier
+            L[c.reshape(-1, 1), t[m]] = -self.multiplier
+            L[c.reshape(-1, 1), c] = eye(len(c)) * self.multiplier * len(self.points[m])
+
+        self.results.stiffness = L.tocsr()
         return self.results.stiffness
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_pointload.py` & `felupe-7.0.0/src/felupe/mechanics/_pointload.py`

 * *Files 6% similar despite different names*

```diff
@@ -50,15 +50,15 @@
         self.results = Results()
         self.assemble = Assemble(vector=self._vector, matrix=self._matrix)
 
     def update(self, values):
 
         self.__init__(self.field, self.points, values, self.apply_on, self.axisymmetric)
 
-    def _vector(self, field=None, parallel=False, jit=False):
+    def _vector(self, field=None, parallel=False):
 
         if field is not None:
             self.field = field
 
         force = [np.zeros_like(f.values) for f in self.field.fields]
         force[self.apply_on][self.points] += self.values
 
@@ -69,15 +69,15 @@
 
         self.results.force = csr_matrix(
             np.concatenate([f.ravel() for f in force]).reshape(-1, 1)
         )
 
         return -self.results.force
 
-    def _matrix(self, field=None, parallel=False, jit=False):
+    def _matrix(self, field=None, parallel=False):
 
         if field is not None:
             self.field = field
 
         n = np.sum(self.field.fieldsizes)
         self.results.stiffness = csr_matrix(([0], ([0], [0])), shape=(n, n))
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_solidbody.py` & `felupe-7.0.0/src/felupe/mechanics/_solidbody.py`

 * *Files 2% similar despite different names*

```diff
@@ -64,45 +64,41 @@
             kirchhoff_stress=self._kirchhoff_stress,
         )
 
         self._area_change = AreaChange()
 
         self._form = IntegralFormMixed
 
-    def _vector(
-        self, field=None, parallel=False, jit=False, items=None, args=(), kwargs={}
-    ):
+    def _vector(self, field=None, parallel=False, items=None, args=(), kwargs={}):
 
         if field is not None:
             self.field = field
 
         self.results.stress = self._gradient(field, args=args, kwargs=kwargs)
         self.results.force = self._form(
             fun=self.results.stress[slice(items)],
             v=self.field,
             dV=self.field.region.dV,
-        ).assemble(parallel=parallel, jit=jit)
+        ).assemble(parallel=parallel)
 
         return self.results.force
 
-    def _matrix(
-        self, field=None, parallel=False, jit=False, items=None, args=(), kwargs={}
-    ):
+    def _matrix(self, field=None, parallel=False, items=None, args=(), kwargs={}):
 
         if field is not None:
             self.field = field
 
         self.results.elasticity = self._hessian(field, args=args, kwargs=kwargs)
 
         self.results.stiffness = self._form(
             fun=self.results.elasticity[slice(items)],
             v=self.field,
             u=self.field,
             dV=self.field.region.dV,
-        ).assemble(parallel=parallel, jit=jit)
+        ).assemble(parallel=parallel)
 
         return self.results.stiffness
 
     def _extract(self, field):
 
         self.field = field
         self.results.kinematics = self.field.extract()
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_solidbody_gravity.py` & `felupe-7.0.0/src/felupe/mechanics/_solidbody_gravity.py`

 * *Files 6% similar despite different names*

```diff
@@ -46,36 +46,36 @@
         self.results.gravity = np.array(gravity)
         self.results.density = density
 
     def update(self, gravity):
 
         self.__init__(self.field, gravity, self.results.density)
 
-    def _vector(self, field=None, parallel=False, jit=False):
+    def _vector(self, field=None, parallel=False):
 
         if field is not None:
             self.field = field
 
         # copy and take only the first (displacement) field of the container
         f = self.field.copy()
         f.fields = f.fields[0:1]
 
         self.results.force = self._form(
             fun=[self.results.density * self.results.gravity.reshape(-1, 1, 1)],
             v=f,
             dV=self.field.region.dV,
             grad_v=[False],
-        ).assemble(parallel=parallel, jit=jit)
+        ).assemble(parallel=parallel)
 
         if len(self.field) > 1:
             self.results.force.resize(np.sum(self.field.fieldsizes), 1)
 
         return -self.results.force
 
-    def _matrix(self, field=None, parallel=False, jit=False):
+    def _matrix(self, field=None, parallel=False):
 
         if field is not None:
             self.field = field
 
         n = np.sum(self.field.fieldsizes)
         self.results.stiffness = csr_matrix(([0], ([0], [0])), shape=(n, n))
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_solidbody_incompressible.py` & `felupe-7.0.0/src/felupe/mechanics/_solidbody_incompressible.py`

 * *Files 4% similar despite different names*

```diff
@@ -107,72 +107,65 @@
         self.evaluate = Evaluate(
             gradient=self._gradient,
             hessian=self._hessian,
             cauchy_stress=self._cauchy_stress,
             kirchhoff_stress=self._kirchhoff_stress,
         )
 
-    def _vector(
-        self, field=None, parallel=False, jit=False, items=None, args=(), kwargs={}
-    ):
+    def _vector(self, field=None, parallel=False, items=None, args=(), kwargs={}):
 
         self.results.stress = self._gradient(
-            field, parallel=parallel, jit=jit, args=args, kwargs=kwargs
+            field, parallel=parallel, args=args, kwargs=kwargs
         )
 
         form = self._form(
             fun=self.results.stress,
             v=self.field,
             dV=self.field.region.dV,
         )
 
-        h = self.results.state.h(parallel=parallel, jit=jit)
+        h = self.results.state.h(parallel=parallel)
         v = self.results.state.v()
         p = self.results.state.p
 
         values = [
-            form.integrate(parallel=parallel, jit=jit)[0]
+            form.integrate(parallel=parallel)[0]
             + h * (self.bulk * (v / self.V - 1) - p)
         ]
 
         self.results.force = form.assemble(values=values)
 
         return self.results.force
 
-    def _matrix(
-        self, field=None, parallel=False, jit=False, items=None, args=(), kwargs={}
-    ):
+    def _matrix(self, field=None, parallel=False, items=None, args=(), kwargs={}):
 
         self.results.elasticity = self._hessian(
-            field, parallel=parallel, jit=jit, args=args, kwargs=kwargs
+            field, parallel=parallel, args=args, kwargs=kwargs
         )
 
         form = self._form(
             fun=self.results.elasticity,
             v=self.field,
             u=self.field,
             dV=self.field.region.dV,
         )
 
-        h = self.results.state.h(parallel=parallel, jit=jit)
+        h = self.results.state.h(parallel=parallel)
 
-        values = [
-            form.integrate(parallel=parallel, jit=jit)[0]
-            + self.bulk / self.V * dya(h, h)
-        ]
+        values = [form.integrate(parallel=parallel)[0] + self.bulk / self.V * dya(h, h)]
 
         self.results.stiffness = form.assemble(values=values)
 
         return self.results.stiffness
 
-    def _extract(self, field, parallel=False, jit=False):
+    def _extract(self, field, parallel=False):
 
         u = field[0].values
         u0 = self.results.state.u
-        h = self.results.state.h(parallel=parallel, jit=jit)
+        h = self.results.state.h(parallel=parallel)
         v = self.results.state.v()
         J = self.results.state.J
         p = self.results.state.p
 
         du = (u - u0)[field.region.mesh.cells].transpose([1, 2, 0])
 
         # change of state variables due to change of displacement field
@@ -185,36 +178,36 @@
         # update state variables
         self.results.state.p = p + dp
         self.results.state.J = J + dJ
         self.results.state.u = u
 
         return self.results.kinematics
 
-    def _gradient(self, field=None, parallel=False, jit=False, args=(), kwargs={}):
+    def _gradient(self, field=None, parallel=False, args=(), kwargs={}):
 
         if field is not None:
-            self.results.kinematics = self._extract(field, parallel=parallel, jit=jit)
+            self.results.kinematics = self._extract(field, parallel=parallel)
 
         dJdF = self._area_change.function
         F = self.results.kinematics[0]
         statevars = self.results.statevars
 
         p = self.results.state.p
 
         gradient = self.umat.gradient([F, statevars], *args, **kwargs)
 
         self.results.stress = [gradient[0] + p * dJdF([F])[0]]
         self.results._statevars = gradient[-1]
 
         return self.results.stress
 
-    def _hessian(self, field=None, parallel=False, jit=False, args=(), kwargs={}):
+    def _hessian(self, field=None, parallel=False, args=(), kwargs={}):
 
         if field is not None:
-            self.results.kinematics = self._extract(field, parallel=parallel, jit=jit)
+            self.results.kinematics = self._extract(field, parallel=parallel)
 
         d2JdF2 = self._area_change.gradient
         F = self.results.kinematics[0]
         statevars = self.results.statevars
         p = self.results.state.p
 
         self.results.elasticity = [
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_solidbody_pressure.py` & `felupe-7.0.0/src/felupe/mechanics/_solidbody_pressure.py`

 * *Files 3% similar despite different names*

```diff
@@ -56,17 +56,15 @@
     def _extract(self, field):
 
         self.field = field
         self.results.kinematics = self.field.extract()
 
         return self.results.kinematics
 
-    def _vector(
-        self, field=None, pressure=None, parallel=False, jit=False, resize=None
-    ):
+    def _vector(self, field=None, pressure=None, parallel=False, resize=None):
 
         if field is not None:
 
             self._update(field)
             self.results.kinematics = self._extract(self.field)
 
         fun = self._area_change.function(
@@ -78,24 +76,22 @@
         if pressure is not None:
             self.results.pressure = pressure
 
         fun[0] *= self.results.pressure
 
         self.results.force = IntegralFormMixed(
             fun=fun, v=self.field, dV=self.field.region.dV, grad_v=[False]
-        ).assemble(parallel=parallel, jit=jit)
+        ).assemble(parallel=parallel)
 
         if resize is not None:
             self.results.force.resize(*resize.shape)
 
         return self.results.force
 
-    def _matrix(
-        self, field=None, pressure=None, parallel=False, jit=False, resize=None
-    ):
+    def _matrix(self, field=None, pressure=None, parallel=False, resize=None):
 
         if field is not None:
 
             self._update(field)
             self.results.kinematics = self._extract(self.field)
 
         fun = self._area_change.gradient(
@@ -112,15 +108,15 @@
         self.results.stiffness = IntegralFormMixed(
             fun=fun,
             v=self.field,
             u=self.field,
             dV=self.field.region.dV,
             grad_v=[False],
             grad_u=[True],
-        ).assemble(parallel=parallel, jit=jit)
+        ).assemble(parallel=parallel)
 
         if resize is not None:
             self.results.stiffness.resize(*resize.shape)
 
         return self.results.stiffness
 
     def _update(self, other_field, field=None):
```

### Comparing `felupe-6.4.0/src/felupe/mechanics/_step.py` & `felupe-7.0.0/src/felupe/mechanics/_step.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/mesh/__init__.py` & `felupe-7.0.0/src/felupe/mesh/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,14 +20,15 @@
     RectangleArbitraryOrderQuad,
 )
 from ._mesh import Mesh
 from ._read import read
 from ._tools import (
     concatenate,
     expand,
+    flip,
     mirror,
     revolve,
     rotate,
     runouts,
     sweep,
     triangulate,
 )
```

### Comparing `felupe-6.4.0/src/felupe/mesh/_base.py` & `felupe-7.0.0/src/felupe/mesh/_base.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/mesh/_container.py` & `felupe-7.0.0/src/felupe/mesh/_container.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/mesh/_convert.py` & `felupe-7.0.0/src/felupe/mesh/_convert.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,16 +23,16 @@
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 import numpy as np
 
+from ._discrete_geometry import DiscreteGeometry
 from ._helpers import mesh_or_data
-from ._mesh import Mesh
 
 
 @mesh_or_data
 def convert(
     points,
     cells,
     cell_type,
```

### Comparing `felupe-6.4.0/src/felupe/mesh/_geometry.py` & `felupe-7.0.0/src/felupe/mesh/_geometry.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/mesh/_helpers.py` & `felupe-7.0.0/src/felupe/mesh/_helpers.py`

 * *Files 4% similar despite different names*

```diff
@@ -23,42 +23,43 @@
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 from functools import wraps
 
-from ._mesh import Mesh
-
 
 def mesh_or_data(meshfun):
-    """If a ``Mesh`` is passed to a mesh function, extract ``points`` and
-    ``cells`` arrays along with the ``cell_type`` and return a ``Mesh``
+    """If a ``DiscreteGeometry`` is passed to a mesh function, extract ``points`` and
+    ``cells`` arrays along with the ``cell_type`` and return a ``DiscreteGeometry``
     as a result."""
 
     @wraps(meshfun)
     def mesh_or_points_cells_type(*args, **kwargs):
 
         # init mesh flag
         is_mesh = False
 
         # check if unnamed args are passed
         if len(args) > 0:
 
-            # meshfun(Mesh)
-            if isinstance(args[0], Mesh):
+            # meshfun(DiscreteGeometry)
+            if hasattr(args[0], "__mesh__"):
 
                 # set mesh flag
                 is_mesh = True
 
                 # get points, cells and cell_type
                 points = args[0].points
                 cells = args[0].cells
                 cell_type = args[0].cell_type
 
+                # get mesh class
+                Mesh = args[0].__mesh__
+
                 # remove Mesh from args
                 args = args[1:]
 
         if not is_mesh:
 
             # meshfun(points:ndarray, cells:ndarray, cell_type:str)
             if "points" in kwargs.keys():
@@ -100,15 +101,15 @@
                 cells = args[1]
                 cell_type = args[2]
                 args = args[3:]
 
         # call mesh manipulation function
         points, cells, cell_type = meshfun(points, cells, cell_type, *args, **kwargs)
 
-        # return a Mesh if a Mesh was passed
+        # return a DiscreteGeometry if a DiscreteGeometry was passed
         if is_mesh:
             return Mesh(points=points, cells=cells, cell_type=cell_type)
 
         else:
             # or (points, cells, cell_type) if arrays were given
             return points, cells, cell_type
```

### Comparing `felupe-6.4.0/src/felupe/mesh/_read.py` & `felupe-7.0.0/src/felupe/mesh/_read.py`

 * *Files 3% similar despite different names*

```diff
@@ -21,14 +21,16 @@
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
+import numpy as np
+
 from ._container import MeshContainer
 from ._mesh import Mesh
 
 
 def read(
     filename, file_format=None, cellblock=None, dim=None, merge=False, decimals=None
 ):
@@ -47,10 +49,13 @@
         cellblock = slice(None)
 
     cells = m.cells[cellblock]
 
     if not isinstance(cells, list):
         cells = [cells]
 
-    meshes = [Mesh(points, c.data, c.type) for c in cells]
+    if len(cells) > 0:
+        meshes = [Mesh(points, c.data, c.type) for c in cells]
+    else:
+        meshes = [Mesh(points, np.zeros((0, 0), dtype=int), None)]
 
     return MeshContainer(meshes, merge=merge, decimals=decimals)
```

### Comparing `felupe-6.4.0/src/felupe/mesh/_tools.py` & `felupe-7.0.0/src/felupe/mesh/_tools.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,15 +25,14 @@
 
 """
 
 import numpy as np
 
 from ..math import rotation_matrix
 from ._helpers import mesh_or_data
-from ._mesh import Mesh
 
 
 @mesh_or_data
 def expand(points, cells, cell_type, n=11, z=1):
     """Expand a 1d-Line to a 2d-Quad or a 2d-Quad to a 3d-Hexahedron Mesh.
 
     Parameters
@@ -77,15 +76,15 @@
         "quad": ("hexahedron", slice(None, None, None)),
     }[cell_type]
 
     # init new padded points array
     p = np.pad(points, ((0, 0), (0, 1)))
 
     # generate new points array for every thickness expansion ``h``
-    if isinstance(z, int) or isinstance(z, float):
+    if np.isscalar(z):
         points_z = np.linspace(0, z, n)
     else:
         points_z = z
         n = len(z)
 
     points_new = np.vstack([p + np.array([*zeros, h]) for h in points_z])
 
@@ -178,15 +177,15 @@
 
     # set new cell-type and the appropriate slice
     cell_type_new, sl = {
         "line": ("quad", slice(None, None, -1)),
         "quad": ("hexahedron", slice(None, None, None)),
     }[cell_type]
 
-    if isinstance(phi, int) or isinstance(phi, float):
+    if np.isscalar(phi):
         points_phi = np.linspace(0, phi, n)
     else:
         points_phi = phi
         n = len(points_phi)
 
     if abs(points_phi[-1]) > 360:
         raise ValueError("phi must be within |phi| <= 360 degree.")
@@ -256,14 +255,62 @@
     for i, j in zip(find, replace):
         cells_new[cells == i] = j
 
     return points_new, cells_new, cell_type
 
 
 @mesh_or_data
+def flip(points, cells, cell_type, mask=None):
+    """Ensure positive cell volumes for `tria`, `tetra`, `quad` and
+    `hexahedron` cell types.
+
+    Parameters
+    ----------
+    points : list or ndarray
+        Original point coordinates.
+    cells : list or ndarray
+        Original point-connectivity of cells.
+    cell_type : str
+        A string in VTK-convention that specifies the cell type.
+    mask: list or ndarray, optional
+        Boolean mask for selected cells to flip.
+
+    Returns
+    -------
+    points : ndarray
+        Point coordinates.
+    cells : ndarray
+        Modified point-connectivity of cells.
+    cell_type : str or None
+        A string in VTK-convention that specifies the cell type.
+
+    """
+
+    if mask is None:
+        mask = slice(None)
+    else:
+        mask = np.where(mask)[0].reshape(-1, 1)
+
+    faces_to_flip = {
+        "line": ([0, 1],),
+        "triangle": ([0, 1, 2],),
+        "tetra": ([0, 1, 2],),
+        "quad": ([0, 1, 2, 3],),
+        "hexahedron": ([0, 1, 2, 3], [4, 5, 6, 7]),
+    }[cell_type]
+
+    cells_new = cells.copy()
+
+    for face in faces_to_flip:
+        cells_new[:, face] = cells[:, face[::-1]]
+
+    return points, cells_new, cell_type
+
+
+@mesh_or_data
 def mirror(
     points, cells, cell_type, normal=[1, 0, 0], centerpoint=[0, 0, 0], axis=None
 ):
     """Mirror points by plane normal and ensure positive cell volumes for
     `tria`, `tetra`, `quad` and `hexahedron` cell types.
 
     Parameters
@@ -309,33 +356,22 @@
 
     centerpoint = np.array(centerpoint, dtype=float)[:dim]
 
     points_new = points - np.einsum(
         "i, k, ...k -> ...i", 2 * normal, normal, (points - centerpoint)
     )
 
-    faces_to_flip = {
-        "line": ([0, 1],),
-        "triangle": ([0, 1, 2],),
-        "tetra": ([0, 1, 2],),
-        "quad": ([0, 1, 2, 3],),
-        "hexahedron": ([0, 1, 2, 3], [4, 5, 6, 7]),
-    }[cell_type]
-
-    cells_new = cells.copy()
-
-    for face in faces_to_flip:
-        cells_new[:, face] = cells[:, face[::-1]]
-
-    return points_new, cells_new, cell_type
+    return flip(points_new, cells, cell_type, mask=None)
 
 
 def concatenate(meshes):
     "Join a sequence of meshes with identical cell types."
 
+    Mesh = meshes[0].__mesh__
+
     points = np.vstack([mesh.points for mesh in meshes])
     offsets = np.cumsum(np.insert([mesh.npoints for mesh in meshes][:-1], 0, 0))
     cells = np.vstack([offset + mesh.cells for offset, mesh in zip(offsets, meshes)])
     mesh = Mesh(points=points, cells=cells, cell_type=meshes[0].cell_type)
 
     return mesh
```

### Comparing `felupe-6.4.0/src/felupe/quadrature/_base.py` & `felupe-7.0.0/src/felupe/quadrature/_base.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/quadrature/_gausslegendre.py` & `felupe-7.0.0/src/felupe/quadrature/_gausslegendre.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/quadrature/_tetra.py` & `felupe-7.0.0/src/felupe/quadrature/_tetra.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/quadrature/_triangle.py` & `felupe-7.0.0/src/felupe/quadrature/_triangle.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/region/_region.py` & `felupe-7.0.0/src/felupe/region/_region.py`

 * *Files 4% similar despite different names*

```diff
@@ -21,14 +21,16 @@
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
+import warnings
+
 import numpy as np
 
 from ..math import det, inv
 
 
 class Region:
     r"""
@@ -106,10 +108,17 @@
 
             # inverse of dXdr
             self.drdX = inv(self.dXdr)
 
             # numeric **differential volume element**
             self.dV = det(self.dXdr) * self.quadrature.weights.reshape(-1, 1)
 
+            # check for negative **differential volume elements**
+            if np.any(self.dV < 0):
+                cells_negative_volume = np.where(np.any(self.dV < 0, axis=0))[0]
+                warnings.warn(
+                    f"Negative volumes in Region for cells \n {cells_negative_volume}\n Try ``mesh.flip(np.any(region.dV < 0, axis=0))`` and re-create the region."
+                )
+
             # Partial derivative of element shape function
             # w.r.t. undeformed coordinates
             self.dhdX = np.einsum("aIpc,IJpc->aJpc", self.dhdr, self.drdX)
```

### Comparing `felupe-6.4.0/src/felupe/region/_templates.py` & `felupe-7.0.0/src/felupe/region/_templates.py`

 * *Files 14% similar despite different names*

```diff
@@ -133,14 +133,66 @@
             grad=grad,
             only_surface=only_surface,
             mask=mask,
             ensure_3d=ensure_3d,
         )
 
 
+class RegionQuadraticQuadBoundary(RegionBoundary):
+    "A boundary region with a quadratic quad element."
+
+    def __init__(
+        self,
+        mesh,
+        quadrature=GaussLegendreBoundary(order=2, dim=2),
+        grad=True,
+        only_surface=True,
+        mask=None,
+        ensure_3d=False,
+    ):
+
+        element = QuadraticQuad()
+
+        super().__init__(
+            mesh,
+            element,
+            quadrature,
+            grad=grad,
+            only_surface=only_surface,
+            mask=mask,
+            ensure_3d=ensure_3d,
+        )
+
+
+class RegionBiQuadraticQuadBoundary(RegionBoundary):
+    "A boundary region with a bi-quadratic quad element."
+
+    def __init__(
+        self,
+        mesh,
+        quadrature=GaussLegendreBoundary(order=2, dim=2),
+        grad=True,
+        only_surface=True,
+        mask=None,
+        ensure_3d=False,
+    ):
+
+        element = BiQuadraticQuad()
+
+        super().__init__(
+            mesh,
+            element,
+            quadrature,
+            grad=grad,
+            only_surface=only_surface,
+            mask=mask,
+            ensure_3d=ensure_3d,
+        )
+
+
 class RegionConstantHexahedron(Region):
     "A region with a constant hexahedron element."
 
     def __init__(
         self,
         mesh,
         quadrature=GaussLegendre(order=1, dim=3),
@@ -203,23 +255,59 @@
 
     def __init__(self, mesh, quadrature=GaussLegendre(order=2, dim=3), grad=True):
 
         element = QuadraticHexahedron()
         super().__init__(mesh, element, quadrature, grad=grad)
 
 
+class RegionQuadraticHexahedronBoundary(RegionBoundary):
+    "A boundary region with a (serendipity) quadratic hexahedron element."
+
+    def __init__(
+        self,
+        mesh,
+        quadrature=GaussLegendreBoundary(order=2, dim=3),
+        grad=True,
+        only_surface=True,
+        mask=None,
+    ):
+
+        element = QuadraticHexahedron()
+        super().__init__(
+            mesh, element, quadrature, grad=grad, only_surface=only_surface, mask=mask
+        )
+
+
 class RegionTriQuadraticHexahedron(Region):
     "A region with a tri-quadratic (lagrange) hexahedron element."
 
     def __init__(self, mesh, quadrature=GaussLegendre(order=2, dim=3), grad=True):
 
         element = TriQuadraticHexahedron()
         super().__init__(mesh, element, quadrature, grad=grad)
 
 
+class RegionTriQuadraticHexahedronBoundary(RegionBoundary):
+    "A boundary region with a tri-quadratic (lagrange) hexahedron element."
+
+    def __init__(
+        self,
+        mesh,
+        quadrature=GaussLegendreBoundary(order=2, dim=3),
+        grad=True,
+        only_surface=True,
+        mask=None,
+    ):
+
+        element = TriQuadraticHexahedron()
+        super().__init__(
+            mesh, element, quadrature, grad=grad, only_surface=only_surface, mask=mask
+        )
+
+
 class RegionLagrange(Region):
     "A region with an arbitrary order lagrange element."
 
     def __init__(self, mesh, order, dim, quadrature=None, grad=True):
 
         if quadrature is None:
             quadrature = GaussLegendre(order=order, dim=dim, permute=False)
```

### Comparing `felupe-6.4.0/src/felupe/solve/_solve.py` & `felupe-7.0.0/src/felupe/solve/_solve.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe/tools/_check.py` & `felupe-7.0.0/src/felupe/tools/_post.py`

 * *Files 24% similar despite different names*

```diff
@@ -22,40 +22,40 @@
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 import numpy as np
+from scipy.interpolate import interp1d
+from scipy.sparse import issparse
 
-from ..math import norm
 
+def force(field, r, boundary):
+    if issparse(r):
+        r = r.toarray()
+    return (
+        ((np.split(r, field.offsets)[0]).reshape(-1, field[0].dim))[boundary.points]
+    ).sum(0)
 
-def check(dfields, fields, f, dof1, dof0, tol_f=1e-3, tol_x=1e-3, verbose=1):
-    "Check if solution dfields is valid."
 
-    fields = fields.fields
+def moment(field, r, boundary, point=np.zeros(3)):
+    if issparse(r):
+        r = r.toarray()
+    point = point.reshape(1, 3)
 
-    x = fields[0]
-    dx = dfields[0]
+    indices = np.array([(1, 2), (2, 0), (0, 1)])
 
-    # get reference values of "f" and "x"
-    ref_f = 1 if np.linalg.norm(f[dof0]) == 0 else np.linalg.norm(f[dof0])
-    ref_x = 1 if np.linalg.norm(x[dof0]) == 0 else np.linalg.norm(x[dof0])
+    displacements = field[0].values
+    force = (np.split(r, field.offsets)[0]).reshape(-1, 3)
 
-    norm_f = np.linalg.norm(f[dof1[dof1 < len(dx)]]) / ref_f
-    norm_x = np.linalg.norm(dx.ravel()[dof1[dof1 < len(dx)]]) / ref_x
+    d = ((point + displacements) - point)[boundary.points]
+    f = force[boundary.points]
 
-    norm_dfields = norm(dfields[1:])
+    return np.array([(f[:, i] * d[:, i[::-1]]).sum() for i in indices])
 
-    if verbose:
-        info_r = f"|r|={norm_f:1.3e} |u|={norm_x:1.3e}"
-        info_f = [f"(|δ{2+i}|={norm_f:1.3e})" for i, norm_f in enumerate(norm_dfields)]
 
-        print(" ".join([info_r, *info_f]))
-
-    if norm_f < tol_f and norm_x < tol_x:
-        success = True
-    else:
-        success = False
-
-    return success
+def curve(x, y):
+    kind = [None, "linear", "quadratic", "cubic"][min(len(y), 4) - 1]
+    f = interp1d(x[: len(y)], y, kind=kind)
+    xx = np.linspace(x[0], x[: len(y)][-1])
+    return np.array([x[: len(y)], y]), np.array([xx, f(xx)])
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `felupe-6.4.0/src/felupe/tools/_newton.py` & `felupe-7.0.0/src/felupe/tools/_newton.py`

 * *Files 9% similar despite different names*

```diff
@@ -43,19 +43,19 @@
         self.x = x
         self.fun = fun
         self.jac = jac
         self.success = success
         self.iterations = iterations
 
 
-def fun_items(items, x, parallel=False, jit=False):
+def fun_items(items, x, parallel=False):
     "Force residuals from assembly of equilibrium (weak form)."
 
     # init keyword arguments
-    kwargs = {"parallel": parallel, "jit": jit}
+    kwargs = {"parallel": parallel}
 
     # link field of items with global field
     [item.field.link(x) for item in items]
 
     # init vector with shape from global field
     shape = (np.sum(x.fieldsizes), 1)
     vector = csr_matrix(shape)
@@ -71,19 +71,19 @@
 
         # add vector
         vector += r
 
     return vector.toarray()[:, 0]
 
 
-def jac_items(items, x, parallel=False, jit=False):
+def jac_items(items, x, parallel=False):
     "Tangent stiffness matrix from assembly of linearized equilibrium."
 
     # init keyword arguments
-    kwargs = {"parallel": parallel, "jit": jit}
+    kwargs = {"parallel": parallel}
 
     # init matrix with shape from global field
     shape = (np.sum(x.fieldsizes), np.sum(x.fieldsizes))
     matrix = csr_matrix(shape)
 
     for body in items:
 
@@ -96,39 +96,39 @@
 
         # add matrix
         matrix += K
 
     return matrix
 
 
-def fun(x, umat, parallel=False, jit=False, grad=True, add_identity=True, sym=False):
+def fun(x, umat, parallel=False, grad=True, add_identity=True, sym=False):
     "Force residuals from assembly of equilibrium (weak form)."
 
     return (
         IntegralFormMixed(
             fun=umat.gradient(x.extract(grad=grad, add_identity=add_identity, sym=sym))[
                 :-1
             ],
             v=x,
             dV=x.region.dV,
         )
-        .assemble(parallel=parallel, jit=jit)
+        .assemble(parallel=parallel)
         .toarray()[:, 0]
     )
 
 
-def jac(x, umat, parallel=False, jit=False, grad=True, add_identity=True, sym=False):
+def jac(x, umat, parallel=False, grad=True, add_identity=True, sym=False):
     "Tangent stiffness matrix from assembly of linearized equilibrium."
 
     return IntegralFormMixed(
         fun=umat.hessian(x.extract(grad=grad, add_identity=add_identity, sym=sym)),
         v=x,
         dV=x.region.dV,
         u=x,
-    ).assemble(parallel=parallel, jit=jit)
+    ).assemble(parallel=parallel)
 
 
 def solve(A, b, x, dof1, dof0, offsets=None, ext0=None, solver=spsolve):
     "Solve partitioned system."
 
     system = fesolve.partition(x, A, dof1, dof0, -b)
     dx = fesolve.solve(*system, ext0, solver=solver)
@@ -145,15 +145,15 @@
     if dof1 is None:
         dof1 = slice(None)
 
     if dof0 is None:
         dof0 = slice(0, 0)
 
     fnorm = sumnorm(f[dof1]) / (eps + sumnorm(f[dof0]))
-    success = fnorm < ftol  # and xnorm < xtol
+    success = fnorm < ftol and xnorm < xtol
 
     if success and items is not None:
         for item in items:
             [item.results.update_statevars() for item in items]
 
     return xnorm, fnorm, success
 
@@ -170,26 +170,21 @@
     jac=jac,
     solve=solve,
     maxiter=16,
     update=update,
     check=check,
     args=(),
     kwargs={},
-    kwargs_solve=None,
-    kwargs_check=None,
     tol=np.sqrt(np.finfo(float).eps),
-    umat=None,
     items=None,
     dof1=None,
     dof0=None,
     ext0=None,
     solver=spsolve,
-    export_jac=False,
     verbose=True,
-    timing=True,
 ):
     """
     General-purpose Newton-Rhapson algorithm
 
     (Nonlinear) equilibrium equations `f`, as a function `f(x)` of the
     unknowns `x`, are solved by linearization of `f` at given unknowns `x0`.
 
@@ -211,33 +206,27 @@
 
          x = xn + dx                                       (6)
 
     Eq.(5) and Eq.(6) are repeated until `check(dx, x, f)` returns `True`.
 
     """
 
-    if timing:
-        time_start = perf_counter()
+    if verbose:
+        runtime = [perf_counter()]
 
     if x0 is not None:
         # take x0
         x = x0
 
     else:
         # obtain field of first body
         x = items[0].field
 
-    if umat is not None:
-        kwargs["umat"] = umat
-
-    if kwargs_solve is None:
-        kwargs_solve = {}
-
-    if kwargs_check is None:
-        kwargs_check = {}
+    kwargs_solve = {}
+    sig = inspect.signature(solve)
 
     # pre-evaluate function at given unknowns "x"
     if items is not None:
         f = fun_items(items, x, *args, **kwargs)
     else:
         f = fun(x, *args, **kwargs)
 
@@ -254,59 +243,60 @@
 
         # evaluate jacobian at unknowns "x"
         if items is not None:
             K = jac_items(items, x, *args, **kwargs)
         else:
             K = jac(x, *args, **kwargs)
 
-        # solve linear system and update solution
-        sig = inspect.signature(solve)
-
+        # create keyword-arguments for solving the linear system
         keys = ["x", "dof1", "dof0", "ext0", "solver"]
         values = [x, dof1, dof0, ext0, solver]
 
         for key, value in zip(keys, values):
 
             if key in sig.parameters:
                 kwargs_solve[key] = value
 
+        # solve linear system and update solution
+        if verbose:
+            soltime = [perf_counter()]
+
         dx = solve(K, -f, **kwargs_solve)
+
+        if verbose:
+            soltime.append(perf_counter())
+
         x = update(x, dx)
 
         # evaluate function at unknowns "x"
         if items is not None:
             f = fun_items(items, x, *args, **kwargs)
         else:
             f = fun(x, *args, **kwargs)
 
         # check success of solution
         xnorm, fnorm, success = check(
-            dx, x, f, tol, tol, dof1, dof0, items, **kwargs_check
+            dx=dx, x=x, f=f, xtol=np.inf, ftol=tol, dof1=dof1, dof0=dof0, items=items
         )
 
         if verbose:
             print("|%2d | %1.3e | %1.3e |" % (1 + iteration, fnorm, xnorm))
 
         if success:
-            if verbose and not timing:
-                print("\nSolution converged in %d iterations.\n" % (iteration + 1))
             break
 
         if np.any(np.isnan([xnorm, fnorm])):
             raise ValueError("Norm of unknowns is NaN.")
 
     if 1 + iteration == maxiter and not success:
         raise ValueError("Maximum number of iterations reached (not converged).\n")
 
     Res = Result(x=x, fun=f, success=success, iterations=1 + iteration)
 
-    if export_jac:
-        Res.jac = K
-
-    if verbose and timing:
-        time_finish = perf_counter()
+    if verbose:
+        runtime.append(perf_counter())
         print(
-            "\nSolution converged in %d iterations within %1.4g seconds.\n"
-            % (iteration + 1, time_finish - time_start)
+            "\nConverged in %d iterations (Assembly: %1.4g s, Solve: %1.4g s).\n"
+            % (iteration + 1, np.diff(runtime) - np.diff(soltime), np.diff(soltime))
         )
 
     return Res
```

### Comparing `felupe-6.4.0/src/felupe/tools/_post.py` & `felupe-7.0.0/src/felupe/tools/_solve.py`

 * *Files 22% similar despite different names*

```diff
@@ -22,40 +22,16 @@
 
 You should have received a copy of the GNU General Public License
 along with Felupe.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 
 import numpy as np
-from scipy.interpolate import interp1d
-from scipy.sparse import issparse
 
+from .. import solve as solvetools
 
-def force(field, r, boundary):
-    if issparse(r):
-        r = r.toarray()
-    return (
-        ((np.split(r, field.offsets)[0]).reshape(-1, field[0].dim))[boundary.points]
-    ).sum(0)
 
-
-def moment(field, r, boundary, point=np.zeros(3)):
-    if issparse(r):
-        r = r.toarray()
-    point = point.reshape(1, 3)
-
-    indices = np.array([(1, 2), (2, 0), (0, 1)])
-
-    displacements = field[0].values
-    force = (np.split(r, field.offsets)[0]).reshape(-1, 3)
-
-    d = ((point + displacements) - point)[boundary.points]
-    f = force[boundary.points]
-
-    return np.array([(f[:, i] * d[:, i[::-1]]).sum() for i in indices])
-
-
-def curve(x, y):
-    kind = [None, "linear", "quadratic", "cubic"][min(len(y), 4) - 1]
-    f = interp1d(x[: len(y)], y, kind=kind)
-    xx = np.linspace(x[0], x[: len(y)][-1])
-    return np.array([x[: len(y)], y]), np.array([xx, f(xx)])
+def solve(K, f, field, dof0, dof1, offsets, ext0):
+    "Solve linear equation system K dx = b"
+    system = solvetools.partition(field, K, dof1, dof0, -f)
+    dfields = np.split(solvetools.solve(*system, ext0), offsets)
+    return dfields
```

### Comparing `felupe-6.4.0/src/felupe/tools/_project.py` & `felupe-7.0.0/src/felupe/tools/_project.py`

 * *Files 24% similar despite different names*

```diff
@@ -81,66 +81,80 @@
 
 
 def project(values, region, average=True, mean=False):
     """Projection (and optionally averaging) of scalar or vectorial values
     at quadrature points to mesh-points.
     """
 
-    # 1d-reshaped values
-    dim = int(np.product(values.shape[:-2]))
+    dim = values.shape[:-2]
+    size = int(np.product(dim))
     weights = region.quadrature.weights
 
+    # transpose values
+    idx = np.arange(len(values.shape))
+    idx[: len(dim)] = idx[: len(dim)][::-1]
+    values = values.transpose(idx)
+
     if mean:
 
         # evaluate how often the values must be repeated to match the number
         # of element-points
         reps = np.ones(len(values.shape), dtype=int)
         reps[-2] = len(region.element.points)
 
         # np.average(keepdims=True) requires numpy >= 1.23.0
-        values = np.tile(
-            np.average(values, axis=-2, weights=weights),
-            reps=reps,
-        )
+        values = np.average(values, axis=-2, weights=weights)
 
         # workaround for np.average(keepdims=True)
         shape = values.shape
         shape = np.insert(shape, -1, 1)
         values = values.reshape(*shape)
 
-    u = values.T.reshape(-1, dim)
+        # broadcast averaged values to match the number of element-points
+        values = np.broadcast_to(values, shape=np.broadcast_shapes(shape, reps))
+
+    # reshape from (shape, nint.points, nelements) to 1d-values
+    u = values.T.reshape(-1, size)
 
-    # disconnected mesh
+    # disconnect the mesh
     m = region.mesh.disconnect()
 
     if mean:
         # region on disconnected mesh with original quadrature scheme
+        # a single-point quadrature would be sufficient
+        # but would require additional (not available) informations
         r = Region(m, region.element, region.quadrature, grad=False)
     else:
         # region on disconnected mesh with inverse quadrature scheme
         r = Region(m, region.element, region.quadrature.inv(), grad=False)
 
     # field for values on disconnected mesh; project values to mesh-points
-    f = Field(r, dim=dim, values=u)
+    f = Field(r, dim=size, values=u)
     v = f.interpolate()
 
     if mean:
-        v = np.tile(
-            np.average(v, axis=-2, weights=weights).reshape(dim, 1, -1), reps=reps
-        )
+
+        # due to the usage of the original quadrature scheme the averaging must be
+        # applied again
+        # np.average(keepdims=True) requires numpy >= 1.23.0
+        v = np.average(v, axis=-2, weights=weights).reshape(size, 1, -1)
+
+        # broadcast averaged values to match the number of element-points
+        shape = np.array([*v.shape[:-2], len(region.element.points), v.shape[-1]])
+        v = np.broadcast_to(v, shape=shape)
 
     if average:
 
         # create dummy field for values on original mesh
         # (used for calculation of sparse-matrix indices)
-        g = Field(region, dim=dim)
+        g = Field(region, dim=size)
 
         # average values
         w = sparsematrix(
-            (v.T.ravel(), g.indices.ai), shape=(dim * region.mesh.npoints, 1)
-        ).toarray().reshape(-1, dim) / region.mesh.cells_per_point.reshape(-1, 1)
+            (v.T.ravel(), g.indices.ai), shape=(size * region.mesh.npoints, 1)
+        ).toarray().reshape(-1, size) / region.mesh.cells_per_point.reshape(-1, 1)
 
     else:
 
-        w = v.reshape(-1, dim)
+        w = v.T.reshape(-1, size)
 
     return w
```

### Comparing `felupe-6.4.0/src/felupe/tools/_save.py` & `felupe-7.0.0/src/felupe/tools/_save.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/src/felupe.egg-info/PKG-INFO` & `felupe-7.0.0/src/felupe.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: felupe
-Version: 6.4.0
+Version: 7.0.0
 Summary: Finite Element Analysis
 Author: Andreas Dutzler
 Author-email: a.dutzler@gmail.com
 License: GNU GENERAL PUBLIC LICENSE
                                Version 3, 29 June 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
@@ -690,38 +690,39 @@
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Scientific/Engineering
 Classifier: Topic :: Scientific/Engineering :: Mathematics
 Classifier: Topic :: Utilities
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Provides-Extra: all
 License-File: LICENSE
 
-# FElupe - Finite Element Analysis
+# 🔍 FElupe - Finite Element Analysis
 
 [![PyPI version shields.io](https://img.shields.io/pypi/v/felupe.svg)](https://pypi.python.org/pypi/felupe/) [![Documentation Status](https://readthedocs.org/projects/felupe/badge/?version=latest)](https://felupe.readthedocs.io/en/latest/?badge=latest) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![Made with love in Graz (Austria)](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20in-Graz%20(Austria)-0c674a) [![codecov](https://codecov.io/gh/adtzlr/felupe/branch/main/graph/badge.svg?token=J2QP6Y6LVH)](https://codecov.io/gh/adtzlr/felupe) [![DOI](https://zenodo.org/badge/360657894.svg)](https://zenodo.org/badge/latestdoi/360657894) ![Codestyle black](https://img.shields.io/badge/code%20style-black-black) ![GitHub Repo stars](https://img.shields.io/github/stars/adtzlr/felupe?logo=github) ![PyPI - Downloads](https://img.shields.io/pypi/dm/felupe)
 
-<img src="https://raw.githubusercontent.com/adtzlr/felupe/main/docs/_static/logo_light.svg" width="220px"/>
+<img src="https://raw.githubusercontent.com/adtzlr/felupe/main/docs/_static/logo_light.svg" height="120px"/> <img src="https://user-images.githubusercontent.com/5793153/230604246-5a416081-6777-4f33-afdf-efdb51338722.png" height="120px"/> <img src="https://user-images.githubusercontent.com/5793153/230604587-42e3e339-e08c-4cc8-8000-f7046a8d95df.png" height="120px"/>
 
 FElupe is a Python 3.7+ finite element analysis package focussing on the formulation and numerical solution of nonlinear problems in continuum mechanics of solid bodies. Its name is a combination of FE (finite element) and the german word *Lupe* (magnifying glass) as a synonym for getting an insight how a finite element analysis code looks like under the hood.
 
 # Installation
 Install Python, fire up a terminal and run
 
 ```shell
 pip install felupe[all]
 ```
 
-where `[all]` installs all optional dependencies. By default, FElupe only depends on `numpy` and `scipy`. In order to make use of all features of FElupe, it is suggested to install all optional dependencies (`einsumt`, `h5py`, `meshio`, `numba`, `sparse` and `tensortrax`).
+where `[all]` installs all optional dependencies. By default, FElupe depends on `numpy`, `scipy` and `einsumt`. In order to make use of all features of FElupe, it is suggested to install all optional dependencies (`h5py`, `meshio` and `tensortrax`).
 
 # Getting Started
 A quarter model of a solid cube with hyperelastic material behaviour is subjected to a uniaxial elongation applied at a clamped end-face. This involves the creation of a mesh, a region as well as a displacement field (encapsulated in a field container). Furthermore, the boundary conditions are created by a template for a uniaxial loadcase. An isotropic pseudo-elastic Ogden-Roxburgh Mullins-softening model formulation in combination with an isotropic hyperelastic Neo-Hookean material formulation is applied on a nearly-incompressible solid body. A step generates the consecutive substep-movements of a given boundary condition. The step is further added to a list of steps of a job (here, a characteristic-curve job is used). During evaluation, each substep of each step is solved by an iterative Newton-Rhapson procedure. The solution is exported after each completed substep as a time-series XDMF file. For more details beside this high-level code snippet, please have a look at the [documentation](https://felupe.readthedocs.io/en/latest/?badge=latest).
 
 ```python
 import felupe as fem
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `felupe-6.4.0/src/felupe.egg-info/SOURCES.txt` & `felupe-7.0.0/src/felupe.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -60,14 +60,15 @@
 src/felupe/mechanics/_solidbody_incompressible.py
 src/felupe/mechanics/_solidbody_pressure.py
 src/felupe/mechanics/_step.py
 src/felupe/mesh/__init__.py
 src/felupe/mesh/_base.py
 src/felupe/mesh/_container.py
 src/felupe/mesh/_convert.py
+src/felupe/mesh/_discrete_geometry.py
 src/felupe/mesh/_geometry.py
 src/felupe/mesh/_helpers.py
 src/felupe/mesh/_mesh.py
 src/felupe/mesh/_read.py
 src/felupe/mesh/_tools.py
 src/felupe/quadrature/__init__.py
 src/felupe/quadrature/_base.py
@@ -77,15 +78,14 @@
 src/felupe/region/__init__.py
 src/felupe/region/_boundary.py
 src/felupe/region/_region.py
 src/felupe/region/_templates.py
 src/felupe/solve/__init__.py
 src/felupe/solve/_solve.py
 src/felupe/tools/__init__.py
-src/felupe/tools/_check.py
 src/felupe/tools/_newton.py
 src/felupe/tools/_post.py
 src/felupe/tools/_project.py
 src/felupe/tools/_save.py
 src/felupe/tools/_solve.py
 tests/test_basis.py
 tests/test_bilinearform.py
```

### Comparing `felupe-6.4.0/tests/test_basis.py` & `felupe-7.0.0/tests/test_basis.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_bilinearform.py` & `felupe-7.0.0/tests/test_bilinearform.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_composite.py` & `felupe-7.0.0/tests/test_composite.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_constitution.py` & `felupe-7.0.0/tests/test_constitution.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_dof.py` & `felupe-7.0.0/tests/test_dof.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_element.py` & `felupe-7.0.0/tests/test_element.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_field.py` & `felupe-7.0.0/tests/test_field.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_form.py` & `felupe-7.0.0/tests/test_form.py`

 * *Files 23% similar despite different names*

```diff
@@ -132,179 +132,165 @@
 
 def test_axi():
 
     r, u, P, A = pre_axi()
 
     for parallel in [False, True]:
 
-        for jit in [False, True]:
+        L = fe.IntegralForm(P, u, r.dV)
+        x = L.integrate(parallel=parallel)
 
-            L = fe.IntegralForm(P, u, r.dV)
-            x = L.integrate(parallel=parallel, jit=jit)
+        b = L.assemble(x, parallel=parallel).toarray()
+        assert b.shape == (r.mesh.ndof, 1)
 
-            b = L.assemble(x, parallel=parallel).toarray()
-            assert b.shape == (r.mesh.ndof, 1)
+        b = L.assemble(parallel=parallel).toarray()
+        assert b.shape == (r.mesh.ndof, 1)
 
-            b = L.assemble(parallel=parallel).toarray()
-            assert b.shape == (r.mesh.ndof, 1)
+        a = fe.IntegralForm(A, u, r.dV, u, grad_v=[True], grad_u=[True])
+        y = a.integrate(parallel=parallel)
 
-            a = fe.IntegralForm(A, u, r.dV, u, grad_v=[True], grad_u=[True])
-            y = a.integrate(parallel=parallel, jit=jit)
+        K = a.assemble(y, parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.ndof)
 
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.ndof)
-
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.ndof)
+        K = a.assemble(parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.ndof)
 
 
 def test_linearform():
 
     r, u, p, P, A = pre()
 
     for parallel in [False, True]:
 
-        for jit in [False, True]:
-
-            L = fe.IntegralForm(P, u, r.dV, grad_v=[True])
-            x = L.integrate(parallel=parallel, jit=jit)
-            b = L.assemble(x, parallel=parallel).toarray()
-            assert b.shape == (r.mesh.ndof, 1)
-            b = L.assemble(parallel=parallel, jit=jit).toarray()
-            assert b.shape == (r.mesh.ndof, 1)
-
-            L = fe.IntegralForm(p.extract(grad=False), p, r.dV, grad_v=[False])
-            x = L.integrate(parallel=parallel, jit=jit)
-            b = L.assemble(x, parallel=parallel, jit=jit).toarray()
-            assert b.shape == (r.mesh.npoints, 1)
-            b = L.assemble(parallel=parallel, jit=jit).toarray()
-            assert b.shape == (r.mesh.npoints, 1)
+        L = fe.IntegralForm(P, u, r.dV, grad_v=[True])
+        x = L.integrate(parallel=parallel)
+        b = L.assemble(x, parallel=parallel).toarray()
+        assert b.shape == (r.mesh.ndof, 1)
+        b = L.assemble(parallel=parallel).toarray()
+        assert b.shape == (r.mesh.ndof, 1)
+
+        L = fe.IntegralForm(p.extract(grad=False), p, r.dV, grad_v=[False])
+        x = L.integrate(parallel=parallel)
+        b = L.assemble(x, parallel=parallel).toarray()
+        assert b.shape == (r.mesh.npoints, 1)
+        b = L.assemble(parallel=parallel).toarray()
+        assert b.shape == (r.mesh.npoints, 1)
 
 
 def test_linearform_broadcast():
 
     r, u, p, P, A = pre_broadcast()
 
     for parallel in [False, True]:
 
-        for jit in [False, True]:
-
-            L = fe.IntegralForm(P, u, r.dV, grad_v=[True])
-            x = L.integrate(parallel=parallel, jit=jit)
-            b = L.assemble(x, parallel=parallel, jit=jit).toarray()
-            assert b.shape == (r.mesh.ndof, 1)
-            b = L.assemble(parallel=parallel, jit=jit).toarray()
-            assert b.shape == (r.mesh.ndof, 1)
-
-            L = fe.IntegralForm(p.extract(grad=False), p, r.dV, grad_v=[False])
-            x = L.integrate(parallel=parallel, jit=jit)
-            b = L.assemble(x, parallel=parallel, jit=jit).toarray()
-            assert b.shape == (r.mesh.npoints, 1)
-            b = L.assemble(parallel=parallel, jit=jit).toarray()
-            assert b.shape == (r.mesh.npoints, 1)
+        L = fe.IntegralForm(P, u, r.dV, grad_v=[True])
+        x = L.integrate(parallel=parallel)
+        b = L.assemble(x, parallel=parallel).toarray()
+        assert b.shape == (r.mesh.ndof, 1)
+        b = L.assemble(parallel=parallel).toarray()
+        assert b.shape == (r.mesh.ndof, 1)
+
+        L = fe.IntegralForm(p.extract(grad=False), p, r.dV, grad_v=[False])
+        x = L.integrate(parallel=parallel)
+        b = L.assemble(x, parallel=parallel).toarray()
+        assert b.shape == (r.mesh.npoints, 1)
+        b = L.assemble(parallel=parallel).toarray()
+        assert b.shape == (r.mesh.npoints, 1)
 
 
 def test_bilinearform():
 
     r, u, p, P, A = pre()
 
     for parallel in [False, True]:
 
-        for jit in [False, True]:
-
-            a = fe.IntegralForm(A, u, r.dV, u)
-            y = a.integrate(parallel=parallel, jit=jit)
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.ndof)
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.ndof)
-
-            a = fe.IntegralForm(P, u, r.dV, p, [True], [False])
-            y = a.integrate(parallel=parallel, jit=jit)
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.npoints)
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.npoints)
+        a = fe.IntegralForm(A, u, r.dV, u)
+        y = a.integrate(parallel=parallel)
+        K = a.assemble(y, parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.ndof)
+        K = a.assemble(parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.ndof)
+
+        a = fe.IntegralForm(P, u, r.dV, p, [True], [False])
+        y = a.integrate(parallel=parallel)
+        K = a.assemble(y, parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.npoints)
+        K = a.assemble(parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.npoints)
 
 
 def test_bilinearform_broadcast():
 
     r, u, p, P, A = pre_broadcast()
 
     for parallel in [False, True]:
 
-        for jit in [False, True]:
-
-            a = fe.IntegralForm(A, u, r.dV, u, [True], [True])
-            y = a.integrate(parallel=parallel, jit=jit)
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.ndof)
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.ndof)
-
-            a = fe.IntegralForm(P, u, r.dV, p, [True], [False])
-            y = a.integrate(parallel=parallel, jit=jit)
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.npoints)
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.ndof, r.mesh.npoints)
-
-            q = p.extract(grad=False)
-            f = fe.math.dya(q, q, mode=1)
-            a = fe.IntegralForm(f, p, r.dV, p, [False], [False])
-            y = a.integrate(parallel=parallel, jit=jit)
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.npoints, r.mesh.npoints)
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-            assert K.shape == (r.mesh.npoints, r.mesh.npoints)
+        a = fe.IntegralForm(A, u, r.dV, u, [True], [True])
+        y = a.integrate(parallel=parallel)
+        K = a.assemble(y, parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.ndof)
+        K = a.assemble(parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.ndof)
+
+        a = fe.IntegralForm(P, u, r.dV, p, [True], [False])
+        y = a.integrate(parallel=parallel)
+        K = a.assemble(y, parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.npoints)
+        K = a.assemble(parallel=parallel).toarray()
+        assert K.shape == (r.mesh.ndof, r.mesh.npoints)
+
+        q = p.extract(grad=False)
+        f = fe.math.dya(q, q, mode=1)
+        a = fe.IntegralForm(f, p, r.dV, p, [False], [False])
+        y = a.integrate(parallel=parallel)
+        K = a.assemble(y, parallel=parallel).toarray()
+        assert K.shape == (r.mesh.npoints, r.mesh.npoints)
+        K = a.assemble(parallel=parallel).toarray()
+        assert K.shape == (r.mesh.npoints, r.mesh.npoints)
 
 
 def test_mixed():
 
     r, v, f, A = pre_mixed()
 
     for parallel in [False, True]:
 
-        for jit in [False, True]:
-
-            a = fe.IntegralForm(A, v, r.dV, v)
-            y = a.integrate(parallel=parallel, jit=jit)
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-
-            z = r.mesh.ndof + 2 * r.mesh.npoints
-            assert K.shape == (z, z)
-
-            L = fe.IntegralForm(f, v, r.dV)
-            x = L.integrate(parallel=parallel, jit=jit)
-            b = L.assemble(x, parallel=parallel, jit=jit).toarray()
-            b = L.assemble(parallel=parallel, jit=jit).toarray()
+        a = fe.IntegralForm(A, v, r.dV, v)
+        y = a.integrate(parallel=parallel)
+        K = a.assemble(y, parallel=parallel).toarray()
+        K = a.assemble(parallel=parallel).toarray()
+
+        z = r.mesh.ndof + 2 * r.mesh.npoints
+        assert K.shape == (z, z)
+
+        L = fe.IntegralForm(f, v, r.dV)
+        x = L.integrate(parallel=parallel)
+        b = L.assemble(x, parallel=parallel).toarray()
+        b = L.assemble(parallel=parallel).toarray()
 
-            assert b.shape == (z, 1)
+        assert b.shape == (z, 1)
 
     r, v, f, A = pre_axi_mixed()
 
     for parallel in [False, True]:
 
-        for jit in [False, True]:
-
-            a = fe.IntegralForm(A, v, r.dV, v)
-            y = a.integrate(parallel=parallel, jit=jit)
-            K = a.assemble(y, parallel=parallel, jit=jit).toarray()
-            K = a.assemble(parallel=parallel, jit=jit).toarray()
-
-            z = r.mesh.ndof + 2 * r.mesh.npoints
-            assert K.shape == (z, z)
-
-            L = fe.IntegralForm(f, v, r.dV)
-            x = L.integrate(parallel=parallel, jit=jit)
-            b = L.assemble(x, parallel=parallel, jit=jit).toarray()
-            b = L.assemble(parallel=parallel, jit=jit).toarray()
+        a = fe.IntegralForm(A, v, r.dV, v)
+        y = a.integrate(parallel=parallel)
+        K = a.assemble(y, parallel=parallel).toarray()
+        K = a.assemble(parallel=parallel).toarray()
+
+        z = r.mesh.ndof + 2 * r.mesh.npoints
+        assert K.shape == (z, z)
+
+        L = fe.IntegralForm(f, v, r.dV)
+        x = L.integrate(parallel=parallel)
+        b = L.assemble(x, parallel=parallel).toarray()
+        b = L.assemble(parallel=parallel).toarray()
 
-            assert b.shape == (z, 1)
+        assert b.shape == (z, 1)
 
 
 if __name__ == "__main__":
     test_linearform()
     test_linearform_broadcast()
     test_bilinearform()
     test_bilinearform_broadcast()
```

### Comparing `felupe-6.4.0/tests/test_job.py` & `felupe-7.0.0/tests/test_job.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_math.py` & `felupe-7.0.0/tests/test_math.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_mechanics.py` & `felupe-7.0.0/tests/test_mechanics.py`

 * *Files 2% similar despite different names*

```diff
@@ -163,57 +163,56 @@
 
 def test_solidbody():
 
     umat, u = pre(dim=3)
     b = fe.SolidBody(umat=umat, field=u, statevars=np.ones(5))
 
     for parallel in [False, True]:
-        for jit in [False, True]:
 
-            kwargs = {"parallel": parallel, "jit": jit}
+        kwargs = {"parallel": parallel}
 
-            r1 = b.assemble.vector(u, **kwargs)
-            assert r1.shape == (81, 1)
+        r1 = b.assemble.vector(u, **kwargs)
+        assert r1.shape == (81, 1)
 
-            r1b = b.results.force
-            assert np.allclose(r1.toarray(), r1b.toarray())
+        r1b = b.results.force
+        assert np.allclose(r1.toarray(), r1b.toarray())
 
-            r2 = b.assemble.vector(**kwargs)
-            assert np.allclose(r1.toarray(), r2.toarray())
+        r2 = b.assemble.vector(**kwargs)
+        assert np.allclose(r1.toarray(), r2.toarray())
 
-            K1 = b.assemble.matrix(u, **kwargs)
-            assert K1.shape == (81, 81)
+        K1 = b.assemble.matrix(u, **kwargs)
+        assert K1.shape == (81, 81)
 
-            K1b = b.results.stiffness
-            assert np.allclose(K1.toarray(), K1b.toarray())
+        K1b = b.results.stiffness
+        assert np.allclose(K1.toarray(), K1b.toarray())
 
-            K2 = b.assemble.matrix(**kwargs)
-            assert np.allclose(K1.toarray(), K2.toarray())
+        K2 = b.assemble.matrix(**kwargs)
+        assert np.allclose(K1.toarray(), K2.toarray())
 
-            P1 = b.results.stress
-            P2 = b.evaluate.gradient()
-            P2 = b.evaluate.gradient(u)
-            assert np.allclose(P1, P2)
+        P1 = b.results.stress
+        P2 = b.evaluate.gradient()
+        P2 = b.evaluate.gradient(u)
+        assert np.allclose(P1, P2)
 
-            A1 = b.results.elasticity
-            A2 = b.evaluate.hessian()
-            A2 = b.evaluate.hessian(u)
-            assert np.allclose(A1, A2)
+        A1 = b.results.elasticity
+        A2 = b.evaluate.hessian()
+        A2 = b.evaluate.hessian(u)
+        assert np.allclose(A1, A2)
 
-            F1 = b.results.kinematics
-            F2 = b._extract(u)
-            assert np.allclose(F1, F2)
+        F1 = b.results.kinematics
+        F2 = b._extract(u)
+        assert np.allclose(F1, F2)
 
-            s1 = b.evaluate.cauchy_stress()
-            s2 = b.evaluate.cauchy_stress(u)
-            assert np.allclose(s1, s2)
+        s1 = b.evaluate.cauchy_stress()
+        s2 = b.evaluate.cauchy_stress(u)
+        assert np.allclose(s1, s2)
 
-            t1 = b.evaluate.kirchhoff_stress()
-            t2 = b.evaluate.kirchhoff_stress(u)
-            assert np.allclose(t1, t2)
+        t1 = b.evaluate.kirchhoff_stress()
+        t2 = b.evaluate.kirchhoff_stress(u)
+        assert np.allclose(t1, t2)
 
 
 def test_solidbody_incompressible():
 
     umat, u = pre(dim=3, bulk=None)
     b = fe.SolidBodyNearlyIncompressible(
         umat=umat, field=u, bulk=5000, statevars=np.ones(5)
@@ -221,217 +220,213 @@
 
     umat = fe.OgdenRoxburgh(fe.NeoHooke(mu=1), r=3, m=1, beta=0)
     b = fe.SolidBodyNearlyIncompressible(
         umat=umat, field=u, bulk=5000, state=fe.StateNearlyIncompressible(u)
     )
 
     for parallel in [False, True]:
-        for jit in [False, True]:
 
-            kwargs = {"parallel": parallel, "jit": jit}
+        kwargs = {"parallel": parallel}
 
-            r1 = b.assemble.vector(u, **kwargs)
-            assert r1.shape == (81, 1)
+        r1 = b.assemble.vector(u, **kwargs)
+        assert r1.shape == (81, 1)
 
-            r1b = b.results.force
-            assert np.allclose(r1.toarray(), r1b.toarray())
+        r1b = b.results.force
+        assert np.allclose(r1.toarray(), r1b.toarray())
 
-            r2 = b.assemble.vector(**kwargs)
-            assert np.allclose(r1.toarray(), r2.toarray())
+        r2 = b.assemble.vector(**kwargs)
+        assert np.allclose(r1.toarray(), r2.toarray())
 
-            K1 = b.assemble.matrix(u, **kwargs)
-            assert K1.shape == (81, 81)
+        K1 = b.assemble.matrix(u, **kwargs)
+        assert K1.shape == (81, 81)
 
-            K1b = b.results.stiffness
-            assert np.allclose(K1.toarray(), K1b.toarray())
+        K1b = b.results.stiffness
+        assert np.allclose(K1.toarray(), K1b.toarray())
 
-            K2 = b.assemble.matrix(**kwargs)
-            assert np.allclose(K1.toarray(), K2.toarray())
+        K2 = b.assemble.matrix(**kwargs)
+        assert np.allclose(K1.toarray(), K2.toarray())
 
-            P1 = b.results.stress
-            P2 = b.evaluate.gradient()
-            P2 = b.evaluate.gradient(u)
-            assert np.allclose(P1, P2)
+        P1 = b.results.stress
+        P2 = b.evaluate.gradient()
+        P2 = b.evaluate.gradient(u)
+        assert np.allclose(P1, P2)
 
-            A1 = b.results.elasticity
-            A2 = b.evaluate.hessian()
-            A2 = b.evaluate.hessian(u)
-            assert np.allclose(A1, A2)
+        A1 = b.results.elasticity
+        A2 = b.evaluate.hessian()
+        A2 = b.evaluate.hessian(u)
+        assert np.allclose(A1, A2)
 
-            F1 = b.results.kinematics
-            F2 = b._extract(u)
-            assert np.allclose(F1, F2)
+        F1 = b.results.kinematics
+        F2 = b._extract(u)
+        assert np.allclose(F1, F2)
 
-            s1 = b.evaluate.cauchy_stress()
-            s2 = b.evaluate.cauchy_stress(u)
-            assert np.allclose(s1, s2)
+        s1 = b.evaluate.cauchy_stress()
+        s2 = b.evaluate.cauchy_stress(u)
+        assert np.allclose(s1, s2)
 
-            t1 = b.evaluate.kirchhoff_stress()
-            t2 = b.evaluate.kirchhoff_stress(u)
-            assert np.allclose(t1, t2)
+        t1 = b.evaluate.kirchhoff_stress()
+        t2 = b.evaluate.kirchhoff_stress(u)
+        assert np.allclose(t1, t2)
 
 
 def test_solidbody_axi():
 
     umat, u = pre_axi(bulk=None)
     b = fe.SolidBodyNearlyIncompressible(umat=umat, field=u, bulk=5000)
     b = fe.SolidBodyNearlyIncompressible(
         umat=umat, field=u, bulk=5000, state=fe.StateNearlyIncompressible(u)
     )
 
     for parallel in [False, True]:
-        for jit in [False, True]:
 
-            kwargs = {"parallel": parallel, "jit": jit}
+        kwargs = {"parallel": parallel}
 
-            r1 = b.assemble.vector(u, **kwargs)
-            assert r1.shape == (18, 1)
+        r1 = b.assemble.vector(u, **kwargs)
+        assert r1.shape == (18, 1)
 
-            r2 = b.assemble.vector(**kwargs)
-            assert np.allclose(r1.toarray(), r2.toarray())
+        r2 = b.assemble.vector(**kwargs)
+        assert np.allclose(r1.toarray(), r2.toarray())
 
-            K1 = b.assemble.matrix(u, **kwargs)
-            assert K1.shape == (18, 18)
+        K1 = b.assemble.matrix(u, **kwargs)
+        assert K1.shape == (18, 18)
 
-            K2 = b.assemble.matrix(**kwargs)
-            assert np.allclose(K1.toarray(), K2.toarray())
+        K2 = b.assemble.matrix(**kwargs)
+        assert np.allclose(K1.toarray(), K2.toarray())
 
-            P1 = b.results.stress
-            P2 = b.evaluate.gradient()
-            P2 = b.evaluate.gradient(u)
-            assert np.allclose(P1, P2)
+        P1 = b.results.stress
+        P2 = b.evaluate.gradient()
+        P2 = b.evaluate.gradient(u)
+        assert np.allclose(P1, P2)
 
-            A1 = b.results.elasticity
-            A2 = b.evaluate.hessian()
-            A2 = b.evaluate.hessian(u)
-            assert np.allclose(A1, A2)
+        A1 = b.results.elasticity
+        A2 = b.evaluate.hessian()
+        A2 = b.evaluate.hessian(u)
+        assert np.allclose(A1, A2)
 
-            F1 = b.results.kinematics
-            F2 = b._extract(u)
-            assert np.allclose(F1, F2)
+        F1 = b.results.kinematics
+        F2 = b._extract(u)
+        assert np.allclose(F1, F2)
 
-            s1 = b.evaluate.cauchy_stress()
-            s2 = b.evaluate.cauchy_stress(u)
-            assert np.allclose(s1, s2)
+        s1 = b.evaluate.cauchy_stress()
+        s2 = b.evaluate.cauchy_stress(u)
+        assert np.allclose(s1, s2)
 
-            t1 = b.evaluate.kirchhoff_stress()
-            t2 = b.evaluate.kirchhoff_stress(u)
-            assert np.allclose(t1, t2)
+        t1 = b.evaluate.kirchhoff_stress()
+        t2 = b.evaluate.kirchhoff_stress(u)
+        assert np.allclose(t1, t2)
 
 
 def test_solidbody_axi_incompressible():
 
     umat, u = pre_axi()
     b = fe.SolidBody(umat=umat, field=u)
 
     for parallel in [False, True]:
-        for jit in [False, True]:
 
-            kwargs = {"parallel": parallel, "jit": jit}
+        kwargs = {"parallel": parallel}
 
-            r1 = b.assemble.vector(u, **kwargs)
-            assert r1.shape == (18, 1)
+        r1 = b.assemble.vector(u, **kwargs)
+        assert r1.shape == (18, 1)
 
-            r2 = b.assemble.vector(**kwargs)
-            assert np.allclose(r1.toarray(), r2.toarray())
+        r2 = b.assemble.vector(**kwargs)
+        assert np.allclose(r1.toarray(), r2.toarray())
 
-            K1 = b.assemble.matrix(u, **kwargs)
-            assert K1.shape == (18, 18)
+        K1 = b.assemble.matrix(u, **kwargs)
+        assert K1.shape == (18, 18)
 
-            K2 = b.assemble.matrix(**kwargs)
-            assert np.allclose(K1.toarray(), K2.toarray())
+        K2 = b.assemble.matrix(**kwargs)
+        assert np.allclose(K1.toarray(), K2.toarray())
 
-            P1 = b.results.stress
-            P2 = b.evaluate.gradient()
-            P2 = b.evaluate.gradient(u)
-            assert np.allclose(P1, P2)
+        P1 = b.results.stress
+        P2 = b.evaluate.gradient()
+        P2 = b.evaluate.gradient(u)
+        assert np.allclose(P1, P2)
 
-            A1 = b.results.elasticity
-            A2 = b.evaluate.hessian()
-            A2 = b.evaluate.hessian(u)
-            assert np.allclose(A1, A2)
+        A1 = b.results.elasticity
+        A2 = b.evaluate.hessian()
+        A2 = b.evaluate.hessian(u)
+        assert np.allclose(A1, A2)
 
-            F1 = b.results.kinematics
-            F2 = b._extract(u)
-            assert np.allclose(F1, F2)
+        F1 = b.results.kinematics
+        F2 = b._extract(u)
+        assert np.allclose(F1, F2)
 
-            s1 = b.evaluate.cauchy_stress()
-            s2 = b.evaluate.cauchy_stress(u)
-            assert np.allclose(s1, s2)
+        s1 = b.evaluate.cauchy_stress()
+        s2 = b.evaluate.cauchy_stress(u)
+        assert np.allclose(s1, s2)
 
-            t1 = b.evaluate.kirchhoff_stress()
-            t2 = b.evaluate.kirchhoff_stress(u)
-            assert np.allclose(t1, t2)
+        t1 = b.evaluate.kirchhoff_stress()
+        t2 = b.evaluate.kirchhoff_stress(u)
+        assert np.allclose(t1, t2)
 
 
 def test_solidbody_mixed():
 
     umat, u = pre_mixed(dim=3)
     b = fe.SolidBody(umat=umat, field=u)
     g = fe.SolidBodyGravity(field=u, gravity=[9810, 0, 0], density=7.85e-9)
 
     g.assemble.vector()
 
     for parallel in [False, True]:
-        for jit in [False, True]:
 
-            kwargs = {"parallel": parallel, "jit": jit}
+        kwargs = {"parallel": parallel}
 
-            r1 = b.assemble.vector(u, **kwargs)
-            r1 = b.assemble.vector(u, items=3, **kwargs)
-            assert r1.shape == (97, 1)
-
-            r2 = b.assemble.vector(**kwargs)
-            assert np.allclose(r1.toarray(), r2.toarray())
-
-            K1 = b.assemble.matrix(u, **kwargs)
-            K1 = b.assemble.matrix(u, items=6, **kwargs)
-            assert K1.shape == (97, 97)
-
-            K2 = b.assemble.matrix(**kwargs)
-            assert np.allclose(K1.toarray(), K2.toarray())
-
-            P1 = b.results.stress
-            P2 = b.evaluate.gradient()
-            P2 = b.evaluate.gradient(u)
-            for p1, p2 in zip(P1, P2):
-                assert np.allclose(p1, p2)
-
-            A1 = b.results.elasticity
-            A2 = b.evaluate.hessian()
-            A2 = b.evaluate.hessian(u)
-            for a1, a2 in zip(A1, A2):
-                assert np.allclose(a1, a2)
-
-            F1 = b.results.kinematics
-            F2 = b._extract(u)
-            for f1, f2 in zip(F1, F2):
-                assert np.allclose(f1, f2)
-
-            s1 = b.evaluate.cauchy_stress()
-            s2 = b.evaluate.cauchy_stress(u)
-            assert np.allclose(s1, s2)
-
-            t1 = b.evaluate.kirchhoff_stress()
-            t2 = b.evaluate.kirchhoff_stress(u)
-            assert np.allclose(t1, t2)
-
-            rg1 = g.assemble.vector(u, **kwargs)
-            assert rg1.shape == (97, 1)
-
-            Kg1 = g.assemble.matrix(u, **kwargs)
-            assert Kg1.shape == (97, 97)
-
-            rg2 = g.assemble.vector(**kwargs)
-            assert rg1.shape == (97, 1)
-            assert np.allclose(rg1.toarray(), rg2.toarray())
-
-            Kg2 = g.assemble.matrix(**kwargs)
-            assert Kg1.shape == (97, 97)
-            assert np.allclose(Kg1.toarray(), Kg2.toarray())
+        r1 = b.assemble.vector(u, **kwargs)
+        r1 = b.assemble.vector(u, items=3, **kwargs)
+        assert r1.shape == (97, 1)
+
+        r2 = b.assemble.vector(**kwargs)
+        assert np.allclose(r1.toarray(), r2.toarray())
+
+        K1 = b.assemble.matrix(u, **kwargs)
+        K1 = b.assemble.matrix(u, items=6, **kwargs)
+        assert K1.shape == (97, 97)
+
+        K2 = b.assemble.matrix(**kwargs)
+        assert np.allclose(K1.toarray(), K2.toarray())
+
+        P1 = b.results.stress
+        P2 = b.evaluate.gradient()
+        P2 = b.evaluate.gradient(u)
+        for p1, p2 in zip(P1, P2):
+            assert np.allclose(p1, p2)
+
+        A1 = b.results.elasticity
+        A2 = b.evaluate.hessian()
+        A2 = b.evaluate.hessian(u)
+        for a1, a2 in zip(A1, A2):
+            assert np.allclose(a1, a2)
+
+        F1 = b.results.kinematics
+        F2 = b._extract(u)
+        for f1, f2 in zip(F1, F2):
+            assert np.allclose(f1, f2)
+
+        s1 = b.evaluate.cauchy_stress()
+        s2 = b.evaluate.cauchy_stress(u)
+        assert np.allclose(s1, s2)
+
+        t1 = b.evaluate.kirchhoff_stress()
+        t2 = b.evaluate.kirchhoff_stress(u)
+        assert np.allclose(t1, t2)
+
+        rg1 = g.assemble.vector(u, **kwargs)
+        assert rg1.shape == (97, 1)
+
+        Kg1 = g.assemble.matrix(u, **kwargs)
+        assert Kg1.shape == (97, 97)
+
+        rg2 = g.assemble.vector(**kwargs)
+        assert rg1.shape == (97, 1)
+        assert np.allclose(rg1.toarray(), rg2.toarray())
+
+        Kg2 = g.assemble.matrix(**kwargs)
+        assert Kg1.shape == (97, 97)
+        assert np.allclose(Kg1.toarray(), Kg2.toarray())
 
 
 def test_load():
 
     for axi in [False, True]:
 
         if axi:
```

### Comparing `felupe-6.4.0/tests/test_mesh.py` & `felupe-7.0.0/tests/test_mesh.py`

 * *Files 4% similar despite different names*

```diff
@@ -48,14 +48,15 @@
 
     assert n.cell_type == "my-fancy-cell-type"
 
     fe.mesh.convert(m, order=0)
     fe.mesh.convert(m, order=0, calc_points=True)
     fe.mesh.convert(m, order=2)
     fe.mesh.convert(m, order=2, calc_midfaces=True)
+    m.convert(order=2)
 
     m = fe.Mesh(
         points=np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]),
         cells=np.array([[0, 1, 2, 3]]),
         cell_type="tetra",
     )
 
@@ -65,14 +66,15 @@
     fe.mesh.convert(m, order=2, calc_midfaces=True)
 
     m = fe.mesh.Line(n=5)
     assert m.points.shape == (5, 1)
     assert m.cells.shape == (4, 2)
 
     mr = fe.mesh.revolve(m, n=11, phi=180, axis=2)
+    mr = m.revolve(n=11, phi=180, axis=2)
     assert mr.ncells == 4 * 10
 
     m = fe.Rectangle(a=(-1.2, -2), b=(2, 3.1), n=(4, 9))
     assert m.points.shape == (4 * 9, 2)
     assert m.cells.shape == (3 * 8, 4)
 
     fe.mesh.convert(m, order=0)
@@ -101,14 +103,15 @@
         fe.mesh.revolve(m.points, m.cells, m.cell_type, n=11, phi=361, axis=0)
 
     fe.mesh.expand(m.points, m.cells, m.cell_type)
     fe.mesh.expand(m.points, m.cells, cell_type=m.cell_type)
     fe.mesh.expand(m.points, cells=m.cells, cell_type=m.cell_type)
     fe.mesh.expand(points=m.points, cells=m.cells, cell_type=m.cell_type)
     fe.mesh.expand(m)
+    m.expand()
 
     me1 = fe.mesh.expand(m, n=3, z=1)
     me2 = fe.mesh.expand(m, n=3, z=1.0)
     me3 = fe.mesh.expand(m, z=np.linspace(0, 1, 3))
 
     assert np.allclose(me1.points, me2.points)
     assert np.allclose(me2.points, me3.points)
@@ -121,19 +124,23 @@
 
     with pytest.raises(KeyError):
         fe.mesh.expand(m.points, m.cells, m.cell_type)
 
     with pytest.raises(KeyError):
         fe.mesh.revolve(m.points, m.cells, m.cell_type)
 
+    m.flip()
+    fe.mesh.flip(m, mask=[0, 1])
+
     fe.mesh.convert(m, order=2, calc_midfaces=True, calc_midvolumes=True)
 
     fe.mesh.rotate(m, angle_deg=10, axis=0, center=None)
     fe.mesh.rotate(m.points, m.cells, m.cell_type, angle_deg=10, axis=0, center=None)
     fe.mesh.rotate(m, angle_deg=10, axis=1, center=[0, 0, 0])
+    m.rotate(angle_deg=10, axis=0, center=None)
 
     fe.mesh.CubeArbitraryOrderHexahedron()
     fe.mesh.RectangleArbitraryOrderQuad()
 
     m = fe.Rectangle(n=5)
     m.points = np.vstack((m.points, [10, 10]))
     assert m.points.shape == (26, 2)
@@ -146,14 +153,15 @@
     m_dg = m.disconnect(points_per_cell=2, calc_points=False)
     assert np.allclose(m_dg.points, 0)
     assert m_dg.npoints == m.ncells * 2
     assert m_dg.cell_type is None
 
     fe.mesh.sweep(m)
     fe.mesh.sweep(m.points, m.cells, m.cell_type, decimals=4)
+    m.sweep()
 
     m.as_meshio(point_data={"data": m.points}, cell_data={"cell_data": [m.cells[:, 0]]})
     m.save()
 
     m.cell_type = None
     with pytest.raises(Exception):
         m.save()
@@ -172,14 +180,15 @@
     ]:
         axis = kwargs["axis"]
 
         if axis is None or axis < 1:
             m = fe.mesh.Line()
             r = fe.Region(m, fe.Line(), fe.GaussLegendre(1, 1))
             n = fe.mesh.mirror(m, **kwargs)
+            n = m.mirror(**kwargs)
             s = fe.Region(n, fe.Line(), fe.GaussLegendre(1, 1))
             assert np.isclose(r.dV.sum(), s.dV.sum())
 
         if axis is None or axis < 2:
             m = fe.Rectangle()
             r = fe.RegionQuad(m)
             n = fe.mesh.mirror(m, **kwargs)
@@ -218,14 +227,15 @@
         s = fe.RegionTetra(n)
         assert np.isclose(r.dV.sum(), s.dV.sum())
 
 
 def test_triangulate():
     m = fe.Rectangle(n=3)
     n = fe.mesh.triangulate(m)
+    n = m.triangulate()
 
     rm = fe.RegionQuad(m)
     rn = fe.RegionTriangle(n)
 
     assert np.isclose(rm.dV.sum(), rn.dV.sum())
 
     for mode in [0, 3]:
@@ -240,14 +250,15 @@
     with pytest.raises(NotImplementedError):
         n = fe.mesh.triangulate(m, mode=-1)
 
 
 def test_runouts():
     m = fe.Rectangle(n=3)
 
+    n = m.add_runouts(values=[0.0], axis=0, centerpoint=[0, 0])
     n = fe.mesh.runouts(m, values=[0.0], axis=0, centerpoint=[0, 0])
     assert n.points[:, 1].max() == m.points[:, 1].max()
 
     n = fe.mesh.runouts(m, values=[0.1], axis=0, centerpoint=[0, 0])
     assert n.points[:, 1].max() == m.points[:, 1].max() * 1.1
 
     mask = np.zeros(m.npoints, dtype=bool)
@@ -330,17 +341,53 @@
     mesh = fe.mesh.read(filename=filename, dim=None)[0]
     assert mesh.dim == 3
 
     mesh = fe.mesh.read(filename=filename, cellblock=0)[0]
     assert mesh.dim == 3
 
 
+def test_read_nocells(filename="tests/mesh_no-cells.bdf"):
+    mesh = fe.mesh.read(filename=filename, dim=2)
+    assert mesh[0].dim == 2
+    assert mesh[0].ncells == 0
+    assert mesh[0].cells.shape == (0, 0)
+
+    mesh = fe.mesh.read(filename=filename, dim=None)
+    assert mesh[0].dim == 3
+    assert mesh[0].ncells == 0
+    assert mesh[0].cells.shape == (0, 0)
+
+
+def test_mesh_methods():
+    mesh = fe.Cube()
+
+    m = mesh.collect_edges()
+    assert isinstance(m, fe.Mesh)
+
+    m = mesh.collect_faces()
+    assert isinstance(m, fe.Mesh)
+
+    m = mesh.collect_volumes()
+    assert isinstance(m, fe.Mesh)
+
+    m = mesh.add_midpoints_edges()
+    assert isinstance(m, fe.Mesh)
+
+    m = mesh.add_midpoints_faces()
+    assert isinstance(m, fe.Mesh)
+
+    m = mesh.add_midpoints_volumes()
+    assert isinstance(m, fe.Mesh)
+
+
 if __name__ == "__main__":
     test_meshes()
     test_mirror()
     test_triangulate()
     test_runouts()
     test_concatenate()
     test_grid()
     test_grid_1d()
     test_container()
     test_read(filename="mesh.bdf")
+    test_mesh_methods()
+    test_read_nocells(filename="mesh_no-cells.bdf")
```

### Comparing `felupe-6.4.0/tests/test_planestrain.py` & `felupe-7.0.0/tests/test_planestrain.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_quadrature.py` & `felupe-7.0.0/tests/test_quadrature.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_readme.py` & `felupe-7.0.0/tests/test_readme.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_region.py` & `felupe-7.0.0/tests/test_region.py`

 * *Files 6% similar despite different names*

```diff
@@ -39,18 +39,22 @@
     r = fe.RegionQuadBoundary(mesh, ensure_3d=True)
     r = fe.RegionConstantQuad(mesh)
 
     mesh2 = fe.mesh.convert(mesh, 2, True, False, False)
     r = fe.RegionQuadraticQuad(mesh2)
     f = fe.FieldsMixed(r)
 
+    r = fe.RegionQuadraticQuadBoundary(mesh2, ensure_3d=True)
+
     mesh3 = fe.mesh.convert(mesh, 2, True, True, False)
     r = fe.RegionBiQuadraticQuad(mesh3)
     f = fe.FieldsMixed(r)
 
+    r = fe.RegionBiQuadraticQuadBoundary(mesh3)
+
     mesh.cell_type = "some_fancy_cell_type"
     with pytest.raises(NotImplementedError):
         r = fe.RegionBoundary(mesh, fe.Quad(), fe.GaussLegendreBoundary(order=1, dim=2))
 
     mesh = fe.Cube()
     r = fe.RegionHexahedron(mesh)
     r = fe.RegionHexahedronBoundary(mesh)
@@ -64,18 +68,22 @@
 
     r = fe.RegionConstantHexahedron(mesh)
 
     mesh2 = fe.mesh.convert(mesh, 2, True, False, False)
     r = fe.RegionQuadraticHexahedron(mesh2)
     f = fe.FieldsMixed(r)
 
+    r = fe.RegionQuadraticHexahedronBoundary(mesh2)
+
     mesh3 = fe.mesh.convert(mesh, 2, True, True, True)
     r = fe.RegionTriQuadraticHexahedron(mesh3)
     f = fe.FieldsMixed(r)
 
+    r = fe.RegionTriQuadraticHexahedronBoundary(mesh3)
+
     triangle = fe.Triangle()
     points = triangle.points
     cells = np.arange(3).reshape(1, -1)
     mesh = fe.Mesh(points, cells, "triangle")
     r = fe.RegionTriangle(mesh)
 
     mesh2 = fe.mesh.convert(mesh, 2, True, False, False)
```

### Comparing `felupe-6.4.0/tests/test_solve.py` & `felupe-7.0.0/tests/test_solve.py`

 * *Files identical despite different names*

### Comparing `felupe-6.4.0/tests/test_tools.py` & `felupe-7.0.0/tests/test_tools.py`

 * *Files 10% similar despite different names*

```diff
@@ -40,15 +40,15 @@
     J = fe.Field(r, values=1)
 
     f = fe.FieldContainer((u, p, J))
 
     return r, f, (u, p, J)
 
 
-def test_solve_check():
+def test_solve():
 
     r, _, (u, p, J) = pre()
     f = fe.FieldContainer([u])
 
     W = fe.constitution.NeoHooke(1, 3)
 
     F = f.extract()
@@ -63,17 +63,14 @@
 
     b = L.assemble().toarray()[:, 0]
     A = a.assemble()
 
     dx = fe.tools.solve(A, b, f, dof0, dof1, f.offsets, ext0)
     assert dx[0].shape == f[0].values.ravel().shape
 
-    fe.tools.check(dx, f, b, dof1, dof0, verbose=0)
-    fe.tools.check(dx, f, b, dof1, dof0, verbose=1)
-
     fe.tools.save(r, f)
     fe.tools.save(r, f, r=b)
     fe.tools.save(
         r,
         f,
         r=b,
         gradient=W.gradient(F),
@@ -94,15 +91,15 @@
     cauchy = fe.tools.project(fe.math.tovoigt(s), region=r, average=False)
     assert cauchy.shape == (r.mesh.cells.size, 6)
 
     cauchy = fe.tools.project(fe.math.tovoigt(s), region=r, mean=True)
     assert cauchy.shape == (r.mesh.npoints, 6)
 
 
-def test_solve_mixed_check():
+def test_solve_mixed():
 
     r, f, fields = pre()
     u = fields[0]
 
     f = fe.FieldContainer(fields)
 
     F, p, J = f.extract()
@@ -125,17 +122,14 @@
 
     dx = fe.tools.solve(A, b, f, dof0, dof1, f.offsets, ext0)
 
     assert dx[0].shape == u.values.ravel().shape
     assert dx[1].shape == fields[1].values.ravel().shape
     assert dx[2].shape == fields[2].values.ravel().shape
 
-    fe.tools.check(dx, f, b, dof1, dof0, verbose=0)
-    fe.tools.check(dx, f, b, dof1, dof0, verbose=1)
-
     fe.tools.save(r, f)
     fe.tools.save(r, f, r=b)
     fe.tools.save(
         r,
         f,
         r=b,
         gradient=W_mixed.gradient([F, p, J]),
@@ -154,19 +148,15 @@
 
     def jac(x):
         return np.array([2 * (x - 3)])
 
     x0 = np.array([3.1])
 
     res = fe.tools.newtonrhapson(
-        x0, fun, jac, solve=np.linalg.solve, maxiter=32, verbose=True, timing=False
-    )
-
-    res = fe.tools.newtonrhapson(
-        x0, fun, jac, solve=np.linalg.solve, maxiter=32, verbose=True, timing=True
+        x0, fun, jac, solve=np.linalg.solve, maxiter=32, verbose=True
     )
 
     assert abs(res.fun) < 1e-6
     assert np.isclose(res.x, 3, rtol=1e-2)
 
     with pytest.raises(ValueError):
         res = fe.tools.newtonrhapson(
@@ -187,21 +177,19 @@
     displacement = fe.Field(region, dim=3)
     field = fe.FieldContainer([displacement])
     boundaries, loadcase = fe.dof.uniaxial(field, move=0.2, clamped=True)
 
     # define the constitutive material behavior
     umat = fe.NeoHooke(mu=1.0, bulk=2.0)
 
-    for kwargs in [{"parallel": True}, {"jit": True}]:
+    for kwargs in [{"parallel": True, "umat": umat}]:
 
         # newton-rhapson procedure
         res = fe.newtonrhapson(
             field,
-            umat=umat,
-            timing=True,
             verbose=True,
             kwargs=kwargs,
             **loadcase,
         )
 
 
 def test_newton_plane():
@@ -216,31 +204,27 @@
 
     # define the constitutive material behavior
     umat = fe.LinearElasticPlaneStress(E=1.0, nu=0.3)
 
     # newton-rhapson procedure
     res = fe.newtonrhapson(
         field,
-        umat=umat,
-        timing=True,
         verbose=True,
-        kwargs={},
+        kwargs=dict(umat=umat),
         **loadcase,
     )
 
     # define the constitutive material behavior
     umat = fe.LinearElasticPlaneStrain(E=1.0, nu=0.3)
 
     # newton-rhapson procedure
     res = fe.newtonrhapson(
         field,
-        umat=umat,
-        timing=True,
         verbose=True,
-        kwargs={},
+        kwargs=dict(umat=umat),
         **loadcase,
     )
 
 
 def test_newton_linearelastic():
 
     # create a hexahedron-region on a cube
@@ -253,18 +237,16 @@
 
     # define the constitutive material behavior
     umat = fe.LinearElastic(E=1.0, nu=0.3)
 
     # newton-rhapson procedure
     res = fe.newtonrhapson(
         field,
-        umat=umat,
-        timing=True,
         verbose=True,
-        kwargs={"grad": True, "sym": True, "add_identity": False},
+        kwargs={"umat": umat, "grad": True, "sym": True, "add_identity": False},
         **loadcase,
     )
 
 
 def test_newton_mixed():
 
     # create a hexahedron-region on a cube
@@ -286,15 +268,15 @@
     F = field.extract(grad=True, sym=False, add_identity=True)
 
     # define the constitutive material behavior
     nh = fe.NeoHooke(mu=1.0, bulk=2.0)
     umat = fe.ThreeFieldVariation(nh)
 
     # newton-rhapson procedure
-    res = fe.newtonrhapson(x0=field, umat=umat, kwargs={}, **loadcase)
+    res = fe.newtonrhapson(x0=field, kwargs=dict(umat=umat), **loadcase)
 
 
 def test_newton_body():
 
     # create a hexahedron-region on a cube
     mesh = fe.Cube(n=6)
     region = fe.RegionHexahedron(mesh)
@@ -323,15 +305,15 @@
         items=[body, bodyp],
         kwargs={},
         **loadcase,
     )
 
 
 if __name__ == "__main__":
-    test_solve_check()
-    test_solve_mixed_check()
+    test_solve()
+    test_solve_mixed()
     test_newton_simple()
     test_newton()
     test_newton_mixed()
     test_newton_plane()
     test_newton_linearelastic()
     test_newton_body()
```

