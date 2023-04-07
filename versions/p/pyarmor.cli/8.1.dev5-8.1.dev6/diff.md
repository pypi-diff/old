# Comparing `tmp/pyarmor.cli-8.1.dev5-py2.py3-none-any.whl.zip` & `tmp/pyarmor.cli-8.1.dev6-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,20 +1,20 @@
-Zip file size: 33153 bytes, number of entries: 18
+Zip file size: 33218 bytes, number of entries: 18
 -rw-r--r--  2.0 unx     1292 b- defN 23-Apr-05 16:02 pyarmor/cli/__init__.py
--rw-r--r--  2.0 unx    20053 b- defN 23-Apr-06 11:47 pyarmor/cli/__main__.py
+-rw-r--r--  2.0 unx    20090 b- defN 23-Apr-06 23:50 pyarmor/cli/__main__.py
 -rw-r--r--  2.0 unx     8608 b- defN 23-Apr-02 14:49 pyarmor/cli/config.py
--rw-r--r--  2.0 unx    15734 b- defN 23-Apr-06 12:16 pyarmor/cli/context.py
+-rw-r--r--  2.0 unx    15828 b- defN 23-Apr-07 00:17 pyarmor/cli/context.py
 -rw-r--r--  2.0 unx     7836 b- defN 23-Apr-06 13:44 pyarmor/cli/default.cfg
 -rw-r--r--  2.0 unx      880 b- defN 23-Jan-12 09:29 pyarmor/cli/errors.py
 -rw-r--r--  2.0 unx     5603 b- defN 23-Apr-05 01:07 pyarmor/cli/generate.py
 -rw-r--r--  2.0 unx     4008 b- defN 23-Feb-11 01:53 pyarmor/cli/mixer.py
 -rw-r--r--  2.0 unx     2487 b- defN 23-Mar-25 22:51 pyarmor/cli/public_capsule.zip
--rw-r--r--  2.0 unx    10971 b- defN 23-Apr-04 13:15 pyarmor/cli/register.py
+-rw-r--r--  2.0 unx    10980 b- defN 23-Apr-06 22:19 pyarmor/cli/register.py
 -rw-r--r--  2.0 unx    11386 b- defN 23-Mar-29 13:18 pyarmor/cli/repack.py
 -rw-r--r--  2.0 unx     6366 b- defN 23-Apr-06 11:59 pyarmor/cli/resource.py
 -rw-r--r--  2.0 unx     2193 b- defN 23-Feb-22 14:43 pyarmor/cli/shell.py
--rw-r--r--  2.0 unx     2405 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/METADATA
--rw-r--r--  2.0 unx      110 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/WHEEL
--rw-r--r--  2.0 unx       41 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/entry_points.txt
--rw-r--r--  2.0 unx        8 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1465 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/RECORD
-18 files, 101446 bytes uncompressed, 30771 bytes compressed:  69.7%
+-rw-r--r--  2.0 unx     2405 b- defN 23-Apr-07 01:10 pyarmor.cli-8.1.dev6.dist-info/METADATA
+-rw-r--r--  2.0 unx      110 b- defN 23-Apr-07 01:10 pyarmor.cli-8.1.dev6.dist-info/WHEEL
+-rw-r--r--  2.0 unx       41 b- defN 23-Apr-07 01:10 pyarmor.cli-8.1.dev6.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx        8 b- defN 23-Apr-07 01:10 pyarmor.cli-8.1.dev6.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1465 b- defN 23-Apr-07 01:10 pyarmor.cli-8.1.dev6.dist-info/RECORD
+18 files, 101586 bytes uncompressed, 30836 bytes compressed:  69.6%
```

## zipnote {}

```diff
@@ -33,23 +33,23 @@
 
 Filename: pyarmor/cli/resource.py
 Comment: 
 
 Filename: pyarmor/cli/shell.py
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev5.dist-info/METADATA
+Filename: pyarmor.cli-8.1.dev6.dist-info/METADATA
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev5.dist-info/WHEEL
+Filename: pyarmor.cli-8.1.dev6.dist-info/WHEEL
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev5.dist-info/entry_points.txt
+Filename: pyarmor.cli-8.1.dev6.dist-info/entry_points.txt
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev5.dist-info/top_level.txt
+Filename: pyarmor.cli-8.1.dev6.dist-info/top_level.txt
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev5.dist-info/RECORD
+Filename: pyarmor.cli-8.1.dev6.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## pyarmor/cli/__main__.py

```diff
@@ -112,15 +112,15 @@
 
 
 def check_cross_platform(ctx, platforms):
     try:
         from pyarmor.cli import runtime
     except ModuleNotFoundError:
         raise CliError('cross platform need pyarmor.cli.runtime, please '
-                       'run "pip install pyarmor.cli.runtime==2.1.dev5" first')
+                       'run "pip install pyarmor.cli.runtime==2.1.dev6" first')
 
     platnames = []
     for path in runtime.__path__:
         platnames.extend(os.listdir(os.path.join(path, 'libs')))
 
     map_platform = runtime.map_platform
     unknown = set([map_platform(x) for x in platforms]) - set(platnames)
@@ -621,17 +621,18 @@
     logging.basicConfig(
         level=logging.INFO,
         format='%(levelname)-8s %(message)s',
     )
 
     try:
         main_entry(sys.argv[1:])
-    except (CliError, RuntimeError) as e:
-        logger.error(e)
-        sys.exit(1)
+    # # TBD: comment for debug
+    # except (CliError, RuntimeError) as e:
+    #     logger.error(e)
+    #     sys.exit(1)
     except Exception as e:
         log_exception(e)
         logger.error(e)
         sys.exit(2)
 
 
 if __name__ == '__main__':
```

## pyarmor/cli/context.py

```diff
@@ -186,17 +186,18 @@
         if sect == 'finder':
             options.update(self.cmd_options.get('finder', {}))
         elif sect == 'builder':
             options.update(self.cmd_options)
         extra_sect = ':'.join([name, sect])
         if self.cfg.has_section(extra_sect):
             options.update(self.cfg.items(extra_sect))
-        cfg = self._named_config(name + '.ruler')
-        if cfg.has_section(sect):
-            options.update(cfg.items(sect))
+        if name:
+            cfg = self._named_config(name + '.ruler')
+            if cfg.has_section(sect):
+                options.update(cfg.items(sect))
         return options
 
     def get_path(self, local=True):
         return self.local_path if local else self.global_path
 
     def get_filename(self, local=True, name=None):
         return os.path.join(self.get_path(local), name + '.ruler') if name \
@@ -521,10 +522,11 @@
             name, encoding = (value + ':utf-8').split(':')[:2]
             cfg = self._named_config(name, encoding=encoding)
             if cfg.has_section('runtime.message'):
                 return cfg
 
     @property
     def need_package_relations(self):
-        opts = self.get_res_options('xxx', 'builder')
-        return any([opts.get(x) for x in (
-            'enable_rft', 'assert_call', 'assert_import')])
+        opts = self.get_res_options('', 'builder')
+        vals = [opts.get(x)
+                for x in ('enable_rft', 'assert_call', 'assert_import')]
+        return any([x in ('1', 'true', 'on', 1, True) for x in vals])
```

## pyarmor/cli/register.py

```diff
@@ -249,15 +249,15 @@
             if not (rcode and rcode.startswith('pyarmor-vax-')):
                 raise RuntimeError('old code "%s" can not be upgraded' % rcode)
             if info['upgrade']:
                 lines.append(upgrade_to_pro_info.substitute(rcode=rcode))
             else:
                 lines.append(upgrade_to_basic_info.substitute())
         else:
-            if info['lictype'] not in ('BASIC', 'PRO'):
+            if info['lictype'] not in ('BASIC', 'PRO', 'GROUP'):
                 raise RuntimeError('unknown license type %s' % info['lictype'])
             lines.append('This license registration information will be')
 
         fmt = '%-16s: %s'
         lines.extend([
             '',
             fmt % ('License Type', 'pyarmor-' + info['lictype'].lower()),
```

## Comparing `pyarmor.cli-8.1.dev5.dist-info/METADATA` & `pyarmor.cli-8.1.dev6.dist-info/METADATA`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyarmor.cli
-Version: 8.1.dev5
+Version: 8.1.dev6
 Summary: A comand line tool to obfuscate python scripts
 Home-page: https://github.com/dashingsoft/pyarmor
 Author: Jondy Zhao
 Author-email: pyarmor@163.com
 License: Free To Use But Restricted
 Keywords: protect obfuscate encrypt obfuscation distribute
 Platform: UNKNOWN
```

## Comparing `pyarmor.cli-8.1.dev5.dist-info/RECORD` & `pyarmor.cli-8.1.dev6.dist-info/RECORD`

 * *Files 12% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 pyarmor/cli/__init__.py,sha256=ewQIh0wc49TeewnGYkGsG_ALFMA_g314F4Ad7fRlktM,1292
-pyarmor/cli/__main__.py,sha256=WOd4rgDvkjKYDJOdwHagVkTluE2SCBZtoRLhrc6KYKw,20053
+pyarmor/cli/__main__.py,sha256=IncN4U7HAGFtPCuuvqV3CnWMll1gxo2vT1AMrHP_FNk,20090
 pyarmor/cli/config.py,sha256=HbCIOkJ2Zd7aGeanB1tUpBhWTj1LhyMiSwWGdmFgN0A,8608
-pyarmor/cli/context.py,sha256=7-Yetn7565tlue64FircL6eMyYBIRnVvZrqpdZne2D0,15734
+pyarmor/cli/context.py,sha256=6b5-LFGq6TE3kY8sqrnWKHYGzHYsqPyt_MWkcpId3vY,15828
 pyarmor/cli/default.cfg,sha256=f2tGuwMjLQjmj7OgBkfhAfJIgtUVnRbe3CZg8WFRChE,7836
 pyarmor/cli/errors.py,sha256=gNlPhcqgCS4OVdU9H8V23YxThyvHKtFI3LKAu-sxH60,880
 pyarmor/cli/generate.py,sha256=7GnIcVG2G8MlaH60-7a2UcCsyedu5Cr0OH_IoOix_GQ,5603
 pyarmor/cli/mixer.py,sha256=CQOttISF-h55lWEbRUaywsNZybxe8KsXC7axO1ISxUE,4008
 pyarmor/cli/public_capsule.zip,sha256=1r4u42ixfocGPMQc0OklpoHF3nvVW6GA1f4SwcEJWVI,2487
-pyarmor/cli/register.py,sha256=Wc6Av9GgI20iZVVgpwwAgsxPaaZqO3CEcmcuGtYeGlw,10971
+pyarmor/cli/register.py,sha256=fNtET8fjd1KxypZ34E9sy9zIA3wkmy2kI57bkDe7saA,10980
 pyarmor/cli/repack.py,sha256=JTmb-KAzPLNu_VttJTym53uJg5GJlPkmNZQ-LjM8gS8,11386
 pyarmor/cli/resource.py,sha256=ef-2nvRhlyYOlSub6LbYywnmABFmtCAADRcK6j89Udg,6366
 pyarmor/cli/shell.py,sha256=S1yJ5RQZhTIysQgXk3H4E_cJsV2Lymh-w-_GdnHFngU,2193
-pyarmor.cli-8.1.dev5.dist-info/METADATA,sha256=zbPoiWE51eJ0fMLg_qLTfzyc3XeC10I0y8x0KRX9cV0,2405
-pyarmor.cli-8.1.dev5.dist-info/WHEEL,sha256=kGT74LWyRUZrL4VgLh6_g12IeVl_9u9ZVhadrgXZUEY,110
-pyarmor.cli-8.1.dev5.dist-info/entry_points.txt,sha256=MODwyeC-iHX4KItYshzQRa5kWWQnMhIuT64w5bqKFR0,41
-pyarmor.cli-8.1.dev5.dist-info/top_level.txt,sha256=UE1ovZ_90YzwF_lZ3LV7o8HKLe-RgzUaUUvdH5UTUus,8
-pyarmor.cli-8.1.dev5.dist-info/RECORD,,
+pyarmor.cli-8.1.dev6.dist-info/METADATA,sha256=F5Xj4A1k3YBFAjQbg_4zPgWOhVdngNqar03Vw2G1VFY,2405
+pyarmor.cli-8.1.dev6.dist-info/WHEEL,sha256=kGT74LWyRUZrL4VgLh6_g12IeVl_9u9ZVhadrgXZUEY,110
+pyarmor.cli-8.1.dev6.dist-info/entry_points.txt,sha256=MODwyeC-iHX4KItYshzQRa5kWWQnMhIuT64w5bqKFR0,41
+pyarmor.cli-8.1.dev6.dist-info/top_level.txt,sha256=UE1ovZ_90YzwF_lZ3LV7o8HKLe-RgzUaUUvdH5UTUus,8
+pyarmor.cli-8.1.dev6.dist-info/RECORD,,
```

