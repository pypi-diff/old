# Comparing `tmp/pyarmor.cli-8.1.dev4-py2.py3-none-any.whl.zip` & `tmp/pyarmor.cli-8.1.dev5-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,20 +1,20 @@
-Zip file size: 32419 bytes, number of entries: 18
--rw-r--r--  2.0 unx       22 b- defN 23-Apr-03 12:07 pyarmor/cli/__init__.py
--rw-r--r--  2.0 unx    20053 b- defN 23-Apr-04 05:28 pyarmor/cli/__main__.py
+Zip file size: 33153 bytes, number of entries: 18
+-rw-r--r--  2.0 unx     1292 b- defN 23-Apr-05 16:02 pyarmor/cli/__init__.py
+-rw-r--r--  2.0 unx    20053 b- defN 23-Apr-06 11:47 pyarmor/cli/__main__.py
 -rw-r--r--  2.0 unx     8608 b- defN 23-Apr-02 14:49 pyarmor/cli/config.py
--rw-r--r--  2.0 unx    15496 b- defN 23-Apr-04 02:49 pyarmor/cli/context.py
--rw-r--r--  2.0 unx     7416 b- defN 23-Apr-04 02:37 pyarmor/cli/default.cfg
+-rw-r--r--  2.0 unx    15734 b- defN 23-Apr-06 12:16 pyarmor/cli/context.py
+-rw-r--r--  2.0 unx     7836 b- defN 23-Apr-06 13:44 pyarmor/cli/default.cfg
 -rw-r--r--  2.0 unx      880 b- defN 23-Jan-12 09:29 pyarmor/cli/errors.py
--rw-r--r--  2.0 unx     5742 b- defN 23-Apr-04 02:42 pyarmor/cli/generate.py
+-rw-r--r--  2.0 unx     5603 b- defN 23-Apr-05 01:07 pyarmor/cli/generate.py
 -rw-r--r--  2.0 unx     4008 b- defN 23-Feb-11 01:53 pyarmor/cli/mixer.py
 -rw-r--r--  2.0 unx     2487 b- defN 23-Mar-25 22:51 pyarmor/cli/public_capsule.zip
--rw-r--r--  2.0 unx    10971 b- defN 23-Apr-03 22:32 pyarmor/cli/register.py
+-rw-r--r--  2.0 unx    10971 b- defN 23-Apr-04 13:15 pyarmor/cli/register.py
 -rw-r--r--  2.0 unx    11386 b- defN 23-Mar-29 13:18 pyarmor/cli/repack.py
--rw-r--r--  2.0 unx     6179 b- defN 23-Apr-03 13:02 pyarmor/cli/resource.py
+-rw-r--r--  2.0 unx     6366 b- defN 23-Apr-06 11:59 pyarmor/cli/resource.py
 -rw-r--r--  2.0 unx     2193 b- defN 23-Feb-22 14:43 pyarmor/cli/shell.py
--rw-r--r--  2.0 unx     2405 b- defN 23-Apr-04 05:37 pyarmor.cli-8.1.dev4.dist-info/METADATA
--rw-r--r--  2.0 unx      110 b- defN 23-Apr-04 05:37 pyarmor.cli-8.1.dev4.dist-info/WHEEL
--rw-r--r--  2.0 unx       41 b- defN 23-Apr-04 05:37 pyarmor.cli-8.1.dev4.dist-info/entry_points.txt
--rw-r--r--  2.0 unx        8 b- defN 23-Apr-04 05:37 pyarmor.cli-8.1.dev4.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1463 b- defN 23-Apr-04 05:37 pyarmor.cli-8.1.dev4.dist-info/RECORD
-18 files, 99468 bytes uncompressed, 30037 bytes compressed:  69.8%
+-rw-r--r--  2.0 unx     2405 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/METADATA
+-rw-r--r--  2.0 unx      110 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/WHEEL
+-rw-r--r--  2.0 unx       41 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx        8 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1465 b- defN 23-Apr-06 14:56 pyarmor.cli-8.1.dev5.dist-info/RECORD
+18 files, 101446 bytes uncompressed, 30771 bytes compressed:  69.7%
```

## zipnote {}

```diff
@@ -33,23 +33,23 @@
 
 Filename: pyarmor/cli/resource.py
 Comment: 
 
 Filename: pyarmor/cli/shell.py
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev4.dist-info/METADATA
+Filename: pyarmor.cli-8.1.dev5.dist-info/METADATA
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev4.dist-info/WHEEL
+Filename: pyarmor.cli-8.1.dev5.dist-info/WHEEL
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev4.dist-info/entry_points.txt
+Filename: pyarmor.cli-8.1.dev5.dist-info/entry_points.txt
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev4.dist-info/top_level.txt
+Filename: pyarmor.cli-8.1.dev5.dist-info/top_level.txt
 Comment: 
 
-Filename: pyarmor.cli-8.1.dev4.dist-info/RECORD
+Filename: pyarmor.cli-8.1.dev5.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## pyarmor/cli/__init__.py

```diff
@@ -1 +1,46 @@
-__VERSION__ = '8.0.1'
+import logging
+
+__VERSION__ = '8.1'
+
+
+def resoptions(meth):
+
+    def process(self, res, *args, **kwargs):
+        self._options = self.ctx.get_res_options(res.fullname, self._Catalog)
+        return meth(self, res, *args, **kwargs)
+
+    return process
+
+
+class Component(object):
+
+    trace_loggers = {
+        'StrProtector': 'trace.mix.str',
+        'CallProtector': 'trace.assert.call',
+        'ImportProtector': 'trace.assert.import',
+        'CoPatcher': 'trace.co',
+        'BccPatcher': 'trace.bcc',
+    }
+
+    def __init__(self, ctx):
+        self.ctx = ctx
+        self._options = {}
+
+        clsname = self.__class__.__name__
+        self.logger = logging.getLogger(self.trace_loggers[clsname])
+
+    def __getattr__(self, opt):
+        if opt.startswith('o_'):
+            return self._options.get(opt[2:])
+        elif opt.startswith('oi_'):
+            return int(self._options.get(opt[3:]))
+        elif opt.startswith('ob_'):
+            v = self._options.get(opt[3:], '')
+            if isinstance(v, str):
+                return v.lower() in ('1', 'true', 'on', 'yes')
+            return v
+        return AttributeError(opt)
+
+    def trace(self, res, node, value):
+        lineno = getattr(node, 'lineno', -1)
+        self.logger.info('%s:%s:%s', res.fullname, lineno, value)
```

## pyarmor/cli/__main__.py

```diff
@@ -112,15 +112,15 @@
 
 
 def check_cross_platform(ctx, platforms):
     try:
         from pyarmor.cli import runtime
     except ModuleNotFoundError:
         raise CliError('cross platform need pyarmor.cli.runtime, please '
-                       'run "pip install pyarmor.cli.runtime==2.1.dev1" first')
+                       'run "pip install pyarmor.cli.runtime==2.1.dev5" first')
 
     platnames = []
     for path in runtime.__path__:
         platnames.extend(os.listdir(os.path.join(path, 'libs')))
 
     map_platform = runtime.map_platform
     unknown = set([map_platform(x) for x in platforms]) - set(platnames)
```

## pyarmor/cli/context.py

```diff
@@ -118,21 +118,22 @@
         self.input_paths = []
         self.outputs = []
         self.resources = []
         self.extra_resources = []
 
         self.module_relations = {}
         self.module_types = {}
+        self.variable_types = {}
         self.module_builtins = set()
 
-        self.extra_libs = {}
         self.obfuscated_modules = set()
+        self.extra_libs = {}
 
         self.rft_auto_excludes = set()
-        self.rft_modules = set()
+        self.rft_export_names = set()
 
         self.runtime_key = None
 
         self.cmd_options = {}
 
     def _read_config(self, filelist, encoding=None):
         cfg = configparser.ConfigParser(
@@ -180,19 +181,19 @@
 
     def get_res_options(self, name, sect='finder'):
         options = {}
         if self.cfg.has_section(sect):
             options.update(self.cfg.items(sect))
         if sect == 'finder':
             options.update(self.cmd_options.get('finder', {}))
+        elif sect == 'builder':
+            options.update(self.cmd_options)
         extra_sect = ':'.join([name, sect])
         if self.cfg.has_section(extra_sect):
             options.update(self.cfg.items(extra_sect))
-        if sect in ('builder', 'finder'):
-            options.update(self.cmd_options)
         cfg = self._named_config(name + '.ruler')
         if cfg.has_section(sect):
             options.update(cfg.items(sect))
         return options
 
     def get_path(self, local=True):
         return self.local_path if local else self.global_path
@@ -517,7 +518,13 @@
     def runtime_messages(self):
         value = self.cfg['runtime'].get('messages', '')
         if value:
             name, encoding = (value + ':utf-8').split(':')[:2]
             cfg = self._named_config(name, encoding=encoding)
             if cfg.has_section('runtime.message'):
                 return cfg
+
+    @property
+    def need_package_relations(self):
+        opts = self.get_res_options('xxx', 'builder')
+        return any([opts.get(x) for x in (
+            'enable_rft', 'assert_call', 'assert_import')])
```

## pyarmor/cli/default.cfg

```diff
@@ -200,20 +200,38 @@
 ;; Target platforms
 ; platforms =
 
 ;; If there are customized runtime messages
 messages = messages.cfg:utf-8
 
 [rft]
-enables = builtin import function class method global local argument
+;;
+;; All rft options must be globl/local, could not be model level
+;;
+
+; File name to store variable types
+type_file = variable.types
+
+;; Now argument is not available
+enables = builtin import function class method global local
+
+;; How to refactor
+;;   simple, make sure script works, but may keep more names
+;;   advanced, need users do more to make script work, but rename more
+rft_mode = simple
 
 ; includes =
 ; excludes =
 
+;; Do not change names list here
 auto_excludes = super
+
+;; Export module and classes
+;; export_names = a.b a.e
+
 mix_import_name = 0
 
 [assert.call]
 enables = all
 
 ; includes =
 ; excludes =
```

## pyarmor/cli/generate.py

```diff
@@ -135,17 +135,14 @@
             if not os.path.exists(opt):
                 raise CliError('no found input "%s"' % opt)
         self.ctx.input_paths = options['inputs']
 
         output = options.get('output', 'dist')
         self.ctx.outputs = output.split(',')
 
-        rft_auto_excludes = self.ctx.cfg['rft'].get('auto_excludes').split()
-        self.ctx.rft_auto_excludes.update(rft_auto_excludes)
-
         finder = Finder(self.ctx)
         finder.process(pack=pack)
 
         Pytransform3.pre_build(self.ctx)
 
         self.ctx.runtime_key = self.generate_runtime_key()
```

## pyarmor/cli/resource.py

```diff
@@ -53,14 +53,21 @@
 
     @property
     def fullpath(self):
         return self.path if self.is_top() else \
             os.path.join(self.parent.fullpath, self.path)
 
     @property
+    def pkgname(self):
+        suffix = '.__init__'
+        if self.fullname.endswith(suffix):
+            return self.fullname[:-len(suffix)]
+        return self.fullname
+
+    @property
     def output_path(self):
         return self.parent.fullname.replace('.', os.path.sep)
 
 
 class FileResource(Resource):
 
     def __init__(self, path, name=None, parent=None):
```

## Comparing `pyarmor.cli-8.1.dev4.dist-info/METADATA` & `pyarmor.cli-8.1.dev5.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyarmor.cli
-Version: 8.1.dev4
+Version: 8.1.dev5
 Summary: A comand line tool to obfuscate python scripts
 Home-page: https://github.com/dashingsoft/pyarmor
 Author: Jondy Zhao
 Author-email: pyarmor@163.com
 License: Free To Use But Restricted
 Keywords: protect obfuscate encrypt obfuscation distribute
 Platform: UNKNOWN
```

