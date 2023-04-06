# Comparing `tmp/roboweb-extension-0.1.2.tar.gz` & `tmp/roboweb-extension-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "roboweb-extension-0.1.2.tar", last modified: Wed Apr  5 05:32:47 2023, max compression
+gzip compressed data, was "roboweb-extension-0.1.4.tar", last modified: Thu Apr  6 20:20:57 2023, max compression
```

## Comparing `roboweb-extension-0.1.2.tar` & `roboweb-extension-0.1.4.tar`

### file list

```diff
@@ -1,34 +1,36 @@
-drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-05 05:32:47.558582 roboweb-extension-0.1.2/
--rw-r--r--   0 hamel      (501) staff       (20)        0 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/LICENSE
--rw-r--r--   0 hamel      (501) staff       (20)      389 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/MANIFEST.in
--rw-r--r--   0 hamel      (501) staff       (20)     3089 2023-04-05 05:32:47.558404 roboweb-extension-0.1.2/PKG-INFO
--rw-r--r--   0 hamel      (501) staff       (20)     1990 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/README.md
--rw-r--r--   0 hamel      (501) staff       (20)      195 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/install.json
-drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-05 05:32:47.554595 roboweb-extension-0.1.2/lib/
--rw-r--r--   0 hamel      (501) staff       (20)     5671 2023-04-05 05:22:21.000000 roboweb-extension-0.1.2/lib/index.js
--rw-r--r--   0 hamel      (501) staff       (20)     1651 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/package.json
--rw-r--r--   0 hamel      (501) staff       (20)     2625 2023-04-05 05:32:31.000000 roboweb-extension-0.1.2/pyproject.toml
-drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-05 05:32:47.555057 roboweb-extension-0.1.2/roboweb-extension/
--rw-r--r--   0 hamel      (501) staff       (20)      318 2023-04-05 04:05:39.000000 roboweb-extension-0.1.2/roboweb-extension/__init__.py
--rw-r--r--   0 hamel      (501) staff       (20)       23 2023-04-05 05:16:17.000000 roboweb-extension-0.1.2/roboweb-extension/_version.py
-drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-05 05:32:47.555345 roboweb-extension-0.1.2/roboweb-extension/labextension/
--rw-r--r--   0 hamel      (501) staff       (20)     1767 2023-04-05 04:50:10.000000 roboweb-extension-0.1.2/roboweb-extension/labextension/package.json
-drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-05 05:32:47.556291 roboweb-extension-0.1.2/roboweb-extension/labextension/static/
--rw-r--r--   0 hamel      (501) staff       (20)     2630 2023-04-05 04:50:10.000000 roboweb-extension-0.1.2/roboweb-extension/labextension/static/568.aea6e3c0e1f50e177d7b.js
--rw-r--r--   0 hamel      (501) staff       (20)     6382 2023-04-05 04:50:10.000000 roboweb-extension-0.1.2/roboweb-extension/labextension/static/remoteEntry.10fb487c8458b0d298fb.js
--rw-r--r--   0 hamel      (501) staff       (20)      118 2023-04-05 04:50:08.000000 roboweb-extension-0.1.2/roboweb-extension/labextension/static/style.js
--rw-r--r--   0 hamel      (501) staff       (20)       20 2023-04-05 04:50:10.000000 roboweb-extension-0.1.2/roboweb-extension/labextension/static/third-party-licenses.json
-drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-05 05:32:47.557615 roboweb-extension-0.1.2/roboweb_extension.egg-info/
--rw-r--r--   0 hamel      (501) staff       (20)     3089 2023-04-05 05:32:47.000000 roboweb-extension-0.1.2/roboweb_extension.egg-info/PKG-INFO
--rw-r--r--   0 hamel      (501) staff       (20)      747 2023-04-05 05:32:47.000000 roboweb-extension-0.1.2/roboweb_extension.egg-info/SOURCES.txt
--rw-r--r--   0 hamel      (501) staff       (20)        1 2023-04-05 05:32:47.000000 roboweb-extension-0.1.2/roboweb_extension.egg-info/dependency_links.txt
--rw-r--r--   0 hamel      (501) staff       (20)        1 2023-04-05 03:55:01.000000 roboweb-extension-0.1.2/roboweb_extension.egg-info/not-zip-safe
--rw-r--r--   0 hamel      (501) staff       (20)       15 2023-04-05 05:32:47.000000 roboweb-extension-0.1.2/roboweb_extension.egg-info/requires.txt
--rw-r--r--   0 hamel      (501) staff       (20)       18 2023-04-05 05:32:47.000000 roboweb-extension-0.1.2/roboweb_extension.egg-info/top_level.txt
--rw-r--r--   0 hamel      (501) staff       (20)       38 2023-04-05 05:32:47.558645 roboweb-extension-0.1.2/setup.cfg
--rw-r--r--   0 hamel      (501) staff       (20)     2820 2023-04-05 05:31:43.000000 roboweb-extension-0.1.2/setup.py
-drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-05 05:32:47.558081 roboweb-extension-0.1.2/style/
--rw-r--r--   0 hamel      (501) staff       (20)        0 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/style/base.css
--rw-r--r--   0 hamel      (501) staff       (20)       25 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/style/index.css
--rw-r--r--   0 hamel      (501) staff       (20)       21 2023-04-05 03:39:55.000000 roboweb-extension-0.1.2/style/index.js
--rw-r--r--   0 hamel      (501) staff       (20)   134496 2023-04-05 04:50:03.000000 roboweb-extension-0.1.2/yarn.lock
+drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-06 20:20:57.698100 roboweb-extension-0.1.4/
+-rw-r--r--   0 hamel      (501) staff       (20)        0 2023-04-05 03:39:55.000000 roboweb-extension-0.1.4/LICENSE
+-rw-r--r--   0 hamel      (501) staff       (20)      389 2023-04-05 03:39:55.000000 roboweb-extension-0.1.4/MANIFEST.in
+-rw-r--r--   0 hamel      (501) staff       (20)     3032 2023-04-06 20:20:57.697914 roboweb-extension-0.1.4/PKG-INFO
+-rw-r--r--   0 hamel      (501) staff       (20)     1990 2023-04-05 03:39:55.000000 roboweb-extension-0.1.4/README.md
+-rw-r--r--   0 hamel      (501) staff       (20)      195 2023-04-05 03:39:55.000000 roboweb-extension-0.1.4/install.json
+drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-06 20:20:57.693499 roboweb-extension-0.1.4/lib/
+-rw-r--r--   0 hamel      (501) staff       (20)     6241 2023-04-06 17:58:25.000000 roboweb-extension-0.1.4/lib/index.js
+-rw-r--r--   0 hamel      (501) staff       (20)     1681 2023-04-06 04:34:06.000000 roboweb-extension-0.1.4/package.json
+-rw-r--r--   0 hamel      (501) staff       (20)     2625 2023-04-06 20:20:51.000000 roboweb-extension-0.1.4/pyproject.toml
+drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-06 20:20:57.694014 roboweb-extension-0.1.4/roboweb-extension/
+-rw-r--r--   0 hamel      (501) staff       (20)      318 2023-04-05 04:05:39.000000 roboweb-extension-0.1.4/roboweb-extension/__init__.py
+-rw-r--r--   0 hamel      (501) staff       (20)       23 2023-04-05 05:16:17.000000 roboweb-extension-0.1.4/roboweb-extension/_version.py
+drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-06 20:20:57.694657 roboweb-extension-0.1.4/roboweb-extension/labextension/
+-rw-r--r--   0 hamel      (501) staff       (20)    21793 2023-04-06 04:54:23.000000 roboweb-extension-0.1.4/roboweb-extension/labextension/build_log.json
+-rw-r--r--   0 hamel      (501) staff       (20)     1797 2023-04-06 04:54:23.000000 roboweb-extension-0.1.4/roboweb-extension/labextension/package.json
+drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-06 20:20:57.696059 roboweb-extension-0.1.4/roboweb-extension/labextension/static/
+-rw-r--r--   0 hamel      (501) staff       (20)     8229 2023-04-06 04:54:23.000000 roboweb-extension-0.1.4/roboweb-extension/labextension/static/lib_index_js.d67964a8beaa2177af6b.js
+-rw-r--r--   0 hamel      (501) staff       (20)     7879 2023-04-06 04:54:23.000000 roboweb-extension-0.1.4/roboweb-extension/labextension/static/lib_index_js.d67964a8beaa2177af6b.js.map
+-rw-r--r--   0 hamel      (501) staff       (20)    27606 2023-04-06 04:54:23.000000 roboweb-extension-0.1.4/roboweb-extension/labextension/static/remoteEntry.8a272f966fe7e1b18b7b.js
+-rw-r--r--   0 hamel      (501) staff       (20)    26379 2023-04-06 04:54:23.000000 roboweb-extension-0.1.4/roboweb-extension/labextension/static/remoteEntry.8a272f966fe7e1b18b7b.js.map
+-rw-r--r--   0 hamel      (501) staff       (20)      118 2023-04-06 04:54:23.000000 roboweb-extension-0.1.4/roboweb-extension/labextension/static/style.js
+drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-06 20:20:57.697121 roboweb-extension-0.1.4/roboweb_extension.egg-info/
+-rw-r--r--   0 hamel      (501) staff       (20)     3032 2023-04-06 20:20:57.000000 roboweb-extension-0.1.4/roboweb_extension.egg-info/PKG-INFO
+-rw-r--r--   0 hamel      (501) staff       (20)      895 2023-04-06 20:20:57.000000 roboweb-extension-0.1.4/roboweb_extension.egg-info/SOURCES.txt
+-rw-r--r--   0 hamel      (501) staff       (20)        1 2023-04-06 20:20:57.000000 roboweb-extension-0.1.4/roboweb_extension.egg-info/dependency_links.txt
+-rw-r--r--   0 hamel      (501) staff       (20)        1 2023-04-05 03:55:01.000000 roboweb-extension-0.1.4/roboweb_extension.egg-info/not-zip-safe
+-rw-r--r--   0 hamel      (501) staff       (20)       15 2023-04-06 20:20:57.000000 roboweb-extension-0.1.4/roboweb_extension.egg-info/requires.txt
+-rw-r--r--   0 hamel      (501) staff       (20)       18 2023-04-06 20:20:57.000000 roboweb-extension-0.1.4/roboweb_extension.egg-info/top_level.txt
+-rw-r--r--   0 hamel      (501) staff       (20)       38 2023-04-06 20:20:57.698140 roboweb-extension-0.1.4/setup.cfg
+-rw-r--r--   0 hamel      (501) staff       (20)     2820 2023-04-06 20:10:40.000000 roboweb-extension-0.1.4/setup.py
+drwxr-xr-x   0 hamel      (501) staff       (20)        0 2023-04-06 20:20:57.697637 roboweb-extension-0.1.4/style/
+-rw-r--r--   0 hamel      (501) staff       (20)        0 2023-04-05 03:39:55.000000 roboweb-extension-0.1.4/style/base.css
+-rw-r--r--   0 hamel      (501) staff       (20)       25 2023-04-05 03:39:55.000000 roboweb-extension-0.1.4/style/index.css
+-rw-r--r--   0 hamel      (501) staff       (20)       21 2023-04-05 03:39:55.000000 roboweb-extension-0.1.4/style/index.js
+-rw-r--r--   0 hamel      (501) staff       (20)   134496 2023-04-05 04:50:03.000000 roboweb-extension-0.1.4/yarn.lock
```

### Comparing `roboweb-extension-0.1.2/PKG-INFO` & `roboweb-extension-0.1.4/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,18 +1,16 @@
 Metadata-Version: 2.1
 Name: roboweb-extension
-Version: 0.1.2
+Version: 0.1.4
 Summary: Roboweb extension
-Home-page: https://github.com/github_username/roboweb-extension
+Home-page: https://github.com/jlewi/roboweb
 Author: Jeremy Lewi
 Author-email: Francisco Uribe <francisco.uribe@gmail.com>
-License: UNKNOWN
 Project-URL: Homepage, https://github.com/github_username/roboweb-extension
 Keywords: Jupyter,JupyterLab,JupyterLab3
-Platform: UNKNOWN
 Classifier: Framework :: Jupyter
 Classifier: Framework :: Jupyter :: JupyterLab
 Classifier: Framework :: Jupyter :: JupyterLab :: 3
 Classifier: Framework :: Jupyter :: JupyterLab :: Extensions
 Classifier: Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python
@@ -91,9 +89,7 @@
 To update the version, install tbump and use it to bump the version.
 By default it will also create a tag.
 
 ```bash
 pip install tbump
 tbump <new-version>
 ```
-
-
```

### Comparing `roboweb-extension-0.1.2/README.md` & `roboweb-extension-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `roboweb-extension-0.1.2/lib/index.js` & `roboweb-extension-0.1.4/lib/index.js`

 * *Files 12% similar despite different names*

#### js-beautify {}

```diff
@@ -7,164 +7,207 @@
 import {
     IThemeManager
 } from '@jupyterlab/apputils';
 import {
     ITranslator
 } from '@jupyterlab/translation';
 import {
+    NotebookActions,
     INotebookTracker
 } from '@jupyterlab/notebook';
 import {
     Widget
 } from '@lumino/widgets';
 import {
     ICommandPalette
 } from '@jupyterlab/apputils';
-// import myimage from '../static/test.jpeg';
 
 class AssistantSidebar extends Widget {
     constructor() {
         super();
         this.id = 'assistant-panel';
         this.addClass('assistant-panel');
         this.title.caption = 'Assistant';
         this.title.iconClass = 'fa fa-robot';
     }
 }
 
+function waitForNonNullVariable(reader, callback) {
+    var variable = reader();
+    if (variable !== null) {
+        callback(variable);
+    } else {
+        setTimeout(function() {
+            waitForNonNullVariable(reader, callback);
+        }, 100); // Wait 1 second before checking again
+    }
+}
+
+function replaceCurrentCell(tracker, code) {
+    const currentNotebook = tracker.currentWidget;
+    if (!currentNotebook) {
+        return;
+    }
+    const index = currentNotebook.content.activeCellIndex;
+    var cell;
+    if (code.startsWith("pip") || code.startsWith("gcloud")) {
+        code = "!" + code;
+        cell = currentNotebook.content.model.contentFactory.createCodeCell({});
+        cell.value.text = code;
+        //add cell at the beginning of the notebook
+        currentNotebook.content.model.cells.insert(0, newCell);
+        console.log("Adding new cell at the beginning");
+    } else if (index === -1) {
+        cell = currentNotebook.content.model.contentFactory.createCodeCell({});
+        cell.value.text = code;
+        currentNotebook.content.model.cells.push(newCell);
+        console.log("Adding new cell");
+    } else {
+        cell = currentNotebook.content.model.cells.get(index);
+        cell.value.text = code;
+        console.log("Replacing code in current cell");
+    }
+};
+
+function getCellContent(cell) {
+    var outputText = "";
+    const outputJSON = cell.outputArea.model.toJSON();
+    if (outputJSON.length > 0) {
+        const traceback = outputJSON[0].traceback;
+        if (traceback != null) {
+            for (var i = 0; i < traceback.length; i++) {
+                const escapeRegex = /\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]/g;
+                const plainTextString = traceback[i].replace(escapeRegex, '');
+                outputText += plainTextString + "\n";
+            }
+        } else {
+            outputText = outputJSON[0].text;
+        }
+    }
+    return {
+        "text": cell.model.value.text,
+        "output": outputText
+    }
+}
+
+function getCurrentCellContent(tracker, app) {
+    const currentNotebook = tracker.currentWidget;
+    if (!currentNotebook) {
+        return;
+    }
+    //get index of currently selected cell
+    const index = currentNotebook.content.activeCellIndex;
+    if (index === -1) {
+        return "";
+    } else {
+        //retrieve cell text including its kernel output
+        const current = app.shell.currentWidget.content.activeCell;
+        return getCellContent(current);
+    }
+}
+
+function loadFlutterApp() {
+    window.isJupyter = true;
+    var serviceWorkerVersion = "124778936";
+    const flutter_script = document.createElement('script');
+    flutter_script.src = '/roboweb-server-extension/flutter.js';
+    document.head.appendChild(flutter_script);
+
+    flutter_script.onload = function() {
+        console.log('Downloading main.dart.js');
+        _flutter.loader.loadEntrypoint({
+            serviceWorker: {
+                serviceWorkerVersion: serviceWorkerVersion,
+            }
+        }).then(function(engineInitializer) {
+            console.log('Initializing engine');
+            waitForNonNullVariable(function() {
+                return document.getElementById("assistant-panel")
+            }, function(target) {
+                engineInitializer.initializeEngine({
+                    hostElement: target,
+                }).then(function(appRunner) {
+                    return appRunner.runApp();
+                })
+            });
+            //if target is null sleep for 100 ms 
+        });
+    };
+}
 const plugin = {
     id: 'roboweb-extension',
     requires: [INotebookTracker, ICommandPalette],
     activate: (app, tracker, palette) => {
         console.log(
-            'Roboweb extension activated'
+            'Roboweb extension activated v0.1'
         );
         const widget = new AssistantSidebar();
-        widget.node.style.minWidth = "500px";
+        widget.node.style.minWidth = "450px";
         app.shell.add(widget, 'right', {
             rank: 0
         });
-        //set min width of the sidebar
+
 
         //register function to retrieve current cell text
         window.currentCellText = function() {
-            const currentNotebook = tracker.currentWidget;
-            if (!currentNotebook) {
-                return;
-            }
-            //get index of currently selected cell
-            const index = currentNotebook.content.activeCellIndex;
-            if (index === -1) {
-                return "";
-            } else {
-                //retrieve cell text including its kernel output
-                const current = app.shell.currentWidget.content.activeCell;
-                window.current = current;
-
-
-                var outputText = "";
-                const outputJSON = current.outputArea.model.toJSON();
-                if (outputJSON.length > 0) {
-                    const traceback = outputJSON[0].traceback;
-                    for (var i = 0; i < traceback.length; i++) {
-                        const escapeRegex = /\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]/g;
-                        const plainTextString = traceback[i].replace(escapeRegex, '');
-                        outputText += plainTextString + "\n";
-                    }
-                }
-
-                return {
-                    "text": current.model.value.text,
-                    "output": outputText
-                }
-            }
+            return getCurrentCellContent(tracker, app);
         }
+
         //register function to edit current cell text
         window.replaceCodeCurrentCell = function(code) {
-            const currentNotebook = tracker.currentWidget;
-            if (!currentNotebook) {
-                return;
-            }
-            //get index of currently selected cell
-            const index = currentNotebook.content.activeCellIndex;
-            //if code starts with pip or gcloud add ! at the beginning
-            if (code.startsWith("pip") || code.startsWith("gcloud")) {
-                code = "!" + code;
-                const newCell = currentNotebook.content.model.contentFactory.createCodeCell({});
-                newCell.value.text = code;
-                //add cell at the beginning of the notebook
-                currentNotebook.content.model.cells.insert(0, newCell);
-                console.log("Adding new cell at the beginning");
-            } else if (index === -1) {
-                const newCell = currentNotebook.content.model.contentFactory.createCodeCell({});
-                newCell.value.text = code;
-                currentNotebook.content.model.cells.push(newCell);
-                console.log("Adding new cell");
-            } else {
-                const cell = currentNotebook.content.model.cells.get(index);
-                cell.value.text = code;
-                console.log("Replacing code in current cell");
-            }
-        };
-
+            replaceCurrentCell(tracker, code);
+        }
 
+        //track and log executions 
+        NotebookActions.executed.connect(async (_, args) => {
+            const {
+                cell,
+                notebook,
+                success,
+                error
+            } = args;
+            var cellContent = getCellContent(cell);
+            const input = cellContent.text;
+            const output = cellContent.output;
+            console.log("Logging execution" + input + " " + output);
+            window.logCellExecution(cellContent.text, cellContent.output);
+        });
 
         app.commands.addCommand('fix-cell-extension:fixCell', {
             label: 'Fix',
             execute: () => {
+                console.log("Fixing cell");
                 const currentNotebook = tracker.currentWidget;
                 if (!currentNotebook) {
+                    console.log("No notebook open");
                     return;
                 }
                 const currentCell = window.currentCellText();
                 const errorPrompt = "My code has an error. Ideally give me a quick command to fix it. If that's not available give me python code to fix it. Assume i dont have a credentials or key file. \n\nCode: \n\n" + currentCell.text + "\n\nError: \n\n" + currentCell.output;
+                console.log("Pasting prompt " + errorPrompt);
                 window.pastePrompt(errorPrompt);
             }
         });
 
         app.contextMenu.addItem({
             command: 'fix-cell-extension:fixCell',
             selector: '.jp-Notebook',
             rank: 0
         });
-        window.isJupyter = true;
-        var serviceWorkerVersion = "124778936";
-        const flutter_script = document.createElement('script');
-        flutter_script.src = '/roboweb-server-extension/flutter.js';
-        document.head.appendChild(flutter_script);
-
-        const main_script = document.createElement('script');
-        main_script.src = '/roboweb-server-extension/main.js';
-        document.head.appendChild(main_script);
-
-        flutter_script.onload = function() {
-            console.log('Downloading main.dart.js');
-            _flutter.loader.loadEntrypoint({
-                serviceWorker: {
-                    serviceWorkerVersion: serviceWorkerVersion,
-                }
-            }).then(function(engineInitializer) {
-                console.log('Initializing engine');
-                let target = document.getElementById("assistant-panel");
-                return engineInitializer.initializeEngine({
-                    hostElement: target,
-                });
-            }).then(function(appRunner) {
-                //remove focus from the sidebar when clicking outside of it
-                console.log('Running app');
-                return appRunner.runApp();
-            });
-        };
-
-
-        //add img/test.jpeg to target
 
-        // const testIMG= document.createElement('img');
-        // testIMG.src = myimage;
-        // target.appendChild(img);
+        window.addEventListener('click', function(event) {
+            const assistantPanelDiv = document.querySelector('#assistant-panel');
+            if (!assistantPanelDiv.contains(event.target)) {
+                removeFocus();
+            }
 
+        }, {
+            passive: true
+        });
 
 
+        //embed flutter app 
+        loadFlutterApp();
     },
     autoStart: true
 };
 export default plugin;
```

### Comparing `roboweb-extension-0.1.2/package.json` & `roboweb-extension-0.1.4/package.json`

 * *Files 3% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9955882352941177%*

 * *Differences: {"'scripts'": "{'build:labextension': 'python -m jupyter labextension build .', "*

 * *              "'build:labextension:dev': 'python -m jupyter labextension build --development True "*

 * *              ".', 'watch:labextension': 'python -m jupyter labextension watch .'}"}*

```diff
@@ -37,22 +37,22 @@
     "repository": {
         "type": "git",
         "url": "https://github.com/github_username/roboweb-extension.git"
     },
     "scripts": {
         "build": "npm run build:labextension:dev",
         "build:all": "npm run build",
-        "build:labextension": "jupyter labextension build .",
-        "build:labextension:dev": "jupyter labextension build --development True .",
+        "build:labextension": "python -m jupyter labextension build .",
+        "build:labextension:dev": "python -m jupyter labextension build --development True .",
         "build:prod": "npm run build:labextension",
         "clean:all": "npm run clean:labextension",
         "clean:labextension": "rimraf roboweb-extension/labextension",
         "prepare": "npm run build:prod",
         "watch": "npm run watch:labextension",
-        "watch:labextension": "jupyter labextension watch ."
+        "watch:labextension": "python -m jupyter labextension watch ."
     },
     "sideEffects": [
         "style/*.css",
         "style/index.js"
     ],
     "version": "0.1.0"
 }
```

### Comparing `roboweb-extension-0.1.2/pyproject.toml` & `roboweb-extension-0.1.4/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -28,15 +28,15 @@
     "Programming Language :: Python",
     "Programming Language :: Python :: 3",
     "Programming Language :: Python :: 3.7",
     "Programming Language :: Python :: 3.8",
     "Programming Language :: Python :: 3.9",
     "Programming Language :: Python :: 3.10",
 ]
-version = "0.1.2"
+version = "0.1.4"
 
 [project.license]
 file = "LICENSE"
 
 [project.urls]
 Homepage = "https://github.com/github_username/roboweb-extension"
 
@@ -84,15 +84,15 @@
 file = [
     { src = "pyproject.toml" },
     { src = "roboweb-extension/_version.py" },
     { src = "package.json" },
 ]
 
 [tool.tbump.version]
-current = "0.1.2"
+current = "0.1.4"
 regex = "(?P<major>\\d+)\\.(?P<minor>\\d+)\\.(?P<patch>\\d+)((?P<channel>a|b|rc|.dev)(?P<release>\\d+))?"
 
 [tool.tbump.git]
 message_template = "Bump to {new_version}"
 tag_template = "v{new_version}"
 
 [license]
```

### Comparing `roboweb-extension-0.1.2/roboweb-extension/labextension/package.json` & `roboweb-extension-0.1.4/roboweb-extension/labextension/package.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9943627450980393%*

 * *Differences: {"'jupyterlab'": "{'_build': {'load': 'static/remoteEntry.8a272f966fe7e1b18b7b.js'}}",*

 * * "'scripts'": "{'build:labextension': 'python -m jupyter labextension build .', "*

 * *              "'build:labextension:dev': 'python -m jupyter labextension build --development True "*

 * *              ".', 'watch:labextension': 'python -m jupyter labextension watch .'}"}*

```diff
@@ -18,15 +18,15 @@
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,js,eot,gif,html,jpg,json,png,svg,woff2,ttf}"
     ],
     "homepage": "https://github.com/github_username/roboweb-extension",
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.10fb487c8458b0d298fb.js"
+            "load": "static/remoteEntry.8a272f966fe7e1b18b7b.js"
         },
         "extension": true,
         "outputDir": "roboweb-extension/labextension"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
@@ -41,22 +41,22 @@
     "repository": {
         "type": "git",
         "url": "https://github.com/github_username/roboweb-extension.git"
     },
     "scripts": {
         "build": "npm run build:labextension:dev",
         "build:all": "npm run build",
-        "build:labextension": "jupyter labextension build .",
-        "build:labextension:dev": "jupyter labextension build --development True .",
+        "build:labextension": "python -m jupyter labextension build .",
+        "build:labextension:dev": "python -m jupyter labextension build --development True .",
         "build:prod": "npm run build:labextension",
         "clean:all": "npm run clean:labextension",
         "clean:labextension": "rimraf roboweb-extension/labextension",
         "prepare": "npm run build:prod",
         "watch": "npm run watch:labextension",
-        "watch:labextension": "jupyter labextension watch ."
+        "watch:labextension": "python -m jupyter labextension watch ."
     },
     "sideEffects": [
         "style/*.css",
         "style/index.js"
     ],
     "version": "0.1.0"
 }
```

### Comparing `roboweb-extension-0.1.2/roboweb_extension.egg-info/PKG-INFO` & `roboweb-extension-0.1.4/roboweb_extension.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,18 +1,16 @@
 Metadata-Version: 2.1
 Name: roboweb-extension
-Version: 0.1.2
+Version: 0.1.4
 Summary: Roboweb extension
-Home-page: https://github.com/github_username/roboweb-extension
+Home-page: https://github.com/jlewi/roboweb
 Author: Jeremy Lewi
 Author-email: Francisco Uribe <francisco.uribe@gmail.com>
-License: UNKNOWN
 Project-URL: Homepage, https://github.com/github_username/roboweb-extension
 Keywords: Jupyter,JupyterLab,JupyterLab3
-Platform: UNKNOWN
 Classifier: Framework :: Jupyter
 Classifier: Framework :: Jupyter :: JupyterLab
 Classifier: Framework :: Jupyter :: JupyterLab :: 3
 Classifier: Framework :: Jupyter :: JupyterLab :: Extensions
 Classifier: Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python
@@ -91,9 +89,7 @@
 To update the version, install tbump and use it to bump the version.
 By default it will also create a tag.
 
 ```bash
 pip install tbump
 tbump <new-version>
 ```
-
-
```

### Comparing `roboweb-extension-0.1.2/setup.py` & `roboweb-extension-0.1.4/setup.py`

 * *Files identical despite different names*

### Comparing `roboweb-extension-0.1.2/yarn.lock` & `roboweb-extension-0.1.4/yarn.lock`

 * *Files identical despite different names*

