# Comparing `tmp/lsst-ctrl-bps-htcondor-26.0.0a20230400.tar.gz` & `tmp/lsst-ctrl-bps-htcondor-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-ctrl-bps-htcondor-26.0.0a20230400.tar", last modified: Thu Jan 26 09:55:06 2023, max compression
+gzip compressed data, was "lsst-ctrl-bps-htcondor-26.0.0a20230500.tar", last modified: Thu Feb  2 14:03:34 2023, max compression
```

## Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400.tar` & `lsst-ctrl-bps-htcondor-26.0.0a20230500.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.991217 lsst-ctrl-bps-htcondor-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-01-26 09:55:06.991217 lsst-ctrl-bps-htcondor-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      759 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.987217 lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.987217 lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/lsst.ctrl.bps.htcondor/
--rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/lsst.ctrl.bps.htcondor/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/lsst.ctrl.bps.htcondor/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6024 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/lsst.ctrl.bps.htcondor/userguide.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3087 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.987217 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.987217 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.987217 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.987217 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.991217 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/
--rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    70054 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/htcondor_service.py
--rw-r--r--   0 runner    (1001) docker     (123)    48297 2023-01-26 09:54:51.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/lssthtc.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:55:06.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:06.991217 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-01-26 09:55:06.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      668 2023-01-26 09:55:06.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:55:06.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-01-26 09:55:06.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:55:06.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:55:06.000000 lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-01-26 09:55:06.991217 lsst-ctrl-bps-htcondor-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.887729 lsst-ctrl-bps-htcondor-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-02-02 14:03:34.887729 lsst-ctrl-bps-htcondor-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      759 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.879729 lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.883729 lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/lsst.ctrl.bps.htcondor/
+-rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/lsst.ctrl.bps.htcondor/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/lsst.ctrl.bps.htcondor/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6024 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/lsst.ctrl.bps.htcondor/userguide.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3087 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.879729 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.879729 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.879729 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.879729 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.887729 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    70038 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/htcondor_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48297 2023-02-02 14:03:18.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/lssthtc.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:03:34.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:03:34.887729 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-02-02 14:03:34.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      668 2023-02-02 14:03:34.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:03:34.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-02 14:03:34.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:03:34.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:03:34.000000 lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-02-02 14:03:34.891729 lsst-ctrl-bps-htcondor-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/LICENSE` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/PKG-INFO` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps-htcondor
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: HTCondor plugin for lsst-ctrl-bps.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps_htcondor
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/README.rst` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/README.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/lsst.ctrl.bps.htcondor/CHANGES.rst` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/lsst.ctrl.bps.htcondor/CHANGES.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/lsst.ctrl.bps.htcondor/index.rst` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/lsst.ctrl.bps.htcondor/index.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/doc/lsst.ctrl.bps.htcondor/userguide.rst` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/doc/lsst.ctrl.bps.htcondor/userguide.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/pyproject.toml` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/__init__.py` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/htcondor_service.py` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/htcondor_service.py`

 * *Files 0% similar despite different names*

```diff
@@ -123,15 +123,15 @@
         """
         _LOG.debug("out_prefix = '%s'", out_prefix)
         with time_this(log=_LOG, level=logging.INFO, prefix=None, msg="Completed HTCondor workflow creation"):
             workflow = HTCondorWorkflow.from_generic_workflow(
                 config,
                 generic_workflow,
                 out_prefix,
-                f"{self.__class__.__module__}." f"{self.__class__.__name__}",
+                f"{self.__class__.__module__}.{self.__class__.__name__}",
             )
 
         with time_this(
             log=_LOG, level=logging.INFO, prefix=None, msg="Completed writing out HTCondor workflow"
         ):
             workflow.write(out_prefix)
         return workflow
@@ -519,17 +519,17 @@
                 subdir_template[final.label],
                 site_values[final.compute_site],
                 generic_workflow,
                 final,
                 out_prefix,
             )
             if "post" not in final_htjob.dagcmds:
-                final_htjob.dagcmds["post"] = (
-                    f"{os.path.dirname(__file__)}/final_post.sh" f" {final.name} $DAG_STATUS $RETURN"
-                )
+                final_htjob.dagcmds[
+                    "post"
+                ] = f"{os.path.dirname(__file__)}/final_post.sh {final.name} $DAG_STATUS $RETURN"
             htc_workflow.dag.add_final_job(final_htjob)
         elif final and isinstance(final, GenericWorkflow):
             raise NotImplementedError("HTCondor plugin does not support a workflow as the final job")
         elif final:
             return TypeError(f"Invalid type for GenericWorkflow.get_final() results ({type(final)})")
 
         return htc_workflow
@@ -896,15 +896,14 @@
         uri = Path(gwf_file.src_uri)
 
         # Note if use_shared and job_shared, don't need to transfer file.
 
         if not use_shared:  # Copy file using push to job
             inputs.append(str(uri.relative_to(out_prefix)))
         elif not gwf_file.job_shared:  # Jobs require own copy
-
             # if using shared filesystem, but still need copy in job. Use
             # HTCondor's curl plugin for a local copy.
 
             # Execution butler is represented as a directory which the
             # curl plugin does not handle. Taking advantage of inside
             # knowledge for temporary fix until have job wrapper that pulls
             # files within job.
@@ -916,15 +915,15 @@
                 if uri.suffix == ".yaml":  # Single file, so just copy.
                     inputs.append(f"file://{uri}")
                 else:
                     inputs.append(f"file://{uri / 'butler.yaml'}")
                     inputs.append(f"file://{uri / 'gen3.sqlite3'}")
             elif uri.is_dir():
                 raise RuntimeError(
-                    "HTCondor plugin cannot transfer directories locally within job " f"{gwf_file.src_uri}"
+                    f"HTCondor plugin cannot transfer directories locally within job {gwf_file.src_uri}"
                 )
             else:
                 inputs.append(f"file://{uri}")
 
     if inputs:
         htc_commands["transfer_input_files"] = ",".join(inputs)
         _LOG.debug("transfer_input_files=%s", htc_commands["transfer_input_files"])
@@ -978,15 +977,14 @@
     """
     messages = []
 
     # Collect information about the job by querying HTCondor schedd and
     # HTCondor history.
     schedd_dag_info = _get_info_from_schedd(wms_workflow_id, hist, schedds)
     if len(schedd_dag_info) == 1:
-
         # Extract the DAG info without altering the results of the query.
         schedd_name = next(iter(schedd_dag_info))
         dag_id = next(iter(schedd_dag_info[schedd_name]))
         dag_ad = schedd_dag_info[schedd_name][dag_id]
 
         # If the provided workflow id does not correspond to the one extracted
         # from the DAGMan log file in the submit directory, rerun the query
@@ -1003,15 +1001,15 @@
             schedd_dag_info.clean()
             messages.append(f"Cannot create the report for '{dag_id}': {exc}")
         else:
             if path_dag_id != dag_id:
                 schedd_dag_info = _get_info_from_schedd(path_dag_id, hist, schedds)
                 messages.append(
                     f"WARNING: Found newer workflow executions in same submit directory as id '{dag_id}'. "
-                    f"This normally occurs when a run is restarted. The report shown is for the most "
+                    "This normally occurs when a run is restarted. The report shown is for the most "
                     f"recent status with run id '{path_dag_id}'"
                 )
 
     if len(schedd_dag_info) == 0:
         run_reports = {}
     elif len(schedd_dag_info) == 1:
         _, dag_info = schedd_dag_info.popitem()
```

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst/ctrl/bps/htcondor/lssthtc.py` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst/ctrl/bps/htcondor/lssthtc.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/PKG-INFO` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps-htcondor
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: HTCondor plugin for lsst-ctrl-bps.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps_htcondor
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-htcondor-26.0.0a20230400/python/lsst_ctrl_bps_htcondor.egg-info/SOURCES.txt` & `lsst-ctrl-bps-htcondor-26.0.0a20230500/python/lsst_ctrl_bps_htcondor.egg-info/SOURCES.txt`

 * *Files identical despite different names*

