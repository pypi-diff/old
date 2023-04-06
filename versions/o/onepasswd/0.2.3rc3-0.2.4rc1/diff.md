# Comparing `tmp/onepasswd-0.2.3rc3.tar.gz` & `tmp/onepasswd-0.2.4rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "onepasswd-0.2.3rc3.tar", last modified: Wed Apr  5 16:18:47 2023, max compression
+gzip compressed data, was "onepasswd-0.2.4rc1.tar", last modified: Thu Apr  6 17:59:23 2023, max compression
```

## Comparing `onepasswd-0.2.3rc3.tar` & `onepasswd-0.2.4rc1.tar`

### file list

```diff
@@ -1,38 +1,39 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/.flake8
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.392593 onepasswd-0.2.3rc3/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.392593 onepasswd-0.2.3rc3/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     1014 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/.github/workflows/ci.yml
--rw-r--r--   0 runner    (1001) docker     (123)       74 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/onepasswd/
--rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10872 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/client.py
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/crypto.py
--rw-r--r--   0 runner    (1001) docker     (123)     1570 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/ltlog.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     5231 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/onepasswd.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/onepasswd/templates/
--rw-r--r--   0 runner    (1001) docker     (123)     7827 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/templates/index.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/onepasswd/templates/static/
--rw-r--r--   0 runner    (1001) docker     (123)    80578 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/templates/static/bootstrap.bundle.min.js
--rw-r--r--   0 runner    (1001) docker     (123)   194901 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/templates/static/bootstrap.min.css
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/templates/static/inconsolata:wght@500.css
--rw-r--r--   0 runner    (1001) docker     (123)    89795 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/templates/static/jquery-3.6.4.min.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/onepasswd/tools/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1174 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/tools/jdiff.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1844 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/tools/jmerge.py
--rw-r--r--   0 runner    (1001) docker     (123)      609 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/tools/upgrade.py
--rw-r--r--   0 runner    (1001) docker     (123)     1366 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/onepasswd/web.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/onepasswd.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-05 16:18:47.000000 onepasswd-0.2.3rc3/onepasswd.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      752 2023-04-05 16:18:47.000000 onepasswd-0.2.3rc3/onepasswd.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 16:18:47.000000 onepasswd-0.2.3rc3/onepasswd.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      191 2023-04-05 16:18:47.000000 onepasswd-0.2.3rc3/onepasswd.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       70 2023-04-05 16:18:47.000000 onepasswd-0.2.3rc3/onepasswd.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-05 16:18:47.000000 onepasswd-0.2.3rc3/onepasswd.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 16:18:47.396593 onepasswd-0.2.3rc3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1214 2023-04-05 16:18:34.000000 onepasswd-0.2.3rc3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.240979 onepasswd-0.2.4rc1/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/.flake8
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.228979 onepasswd-0.2.4rc1/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.232979 onepasswd-0.2.4rc1/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     1014 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/.github/workflows/ci.yml
+-rw-r--r--   0 runner    (1001) docker     (123)       74 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-06 17:59:23.240979 onepasswd-0.2.4rc1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.232979 onepasswd-0.2.4rc1/onepasswd/
+-rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11048 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/crypto.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1570 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/ltlog.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     5231 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/onepasswd.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.236979 onepasswd-0.2.4rc1/onepasswd/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)    10118 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/templates/index.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.236979 onepasswd-0.2.4rc1/onepasswd/templates/static/
+-rw-r--r--   0 runner    (1001) docker     (123)    80578 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/templates/static/bootstrap.bundle.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)   194901 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/templates/static/bootstrap.min.css
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/templates/static/inconsolata:wght@500.css
+-rw-r--r--   0 runner    (1001) docker     (123)    89795 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/templates/static/jquery-3.6.4.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    55371 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/templates/static/jsencrypt.min.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.240979 onepasswd-0.2.4rc1/onepasswd/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1174 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/tools/jdiff.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1844 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/tools/jmerge.py
+-rw-r--r--   0 runner    (1001) docker     (123)      609 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/tools/upgrade.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1707 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/onepasswd/web.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:59:23.236979 onepasswd-0.2.4rc1/onepasswd.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-06 17:59:23.000000 onepasswd-0.2.4rc1/onepasswd.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-04-06 17:59:23.000000 onepasswd-0.2.4rc1/onepasswd.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 17:59:23.000000 onepasswd-0.2.4rc1/onepasswd.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-04-06 17:59:23.000000 onepasswd-0.2.4rc1/onepasswd.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       70 2023-04-06 17:59:23.000000 onepasswd-0.2.4rc1/onepasswd.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 17:59:23.000000 onepasswd-0.2.4rc1/onepasswd.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 17:59:23.240979 onepasswd-0.2.4rc1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1214 2023-04-06 17:59:11.000000 onepasswd-0.2.4rc1/setup.py
```

### Comparing `onepasswd-0.2.3rc3/.github/workflows/ci.yml` & `onepasswd-0.2.4rc1/.github/workflows/ci.yml`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/client.py` & `onepasswd-0.2.4rc1/onepasswd/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -229,15 +229,20 @@
 
 @cli.command('web')
 @click.option('-h', '--host', 'host', default='0.0.0.0')
 @click.option('-p', '--port', 'port', default=10066)
 @click.option('-d', '--debug', 'debug', is_flag=True, default=False)
 @click.pass_context
 def web(ctx, host, port, debug):
-    from onepasswd import web
+    try:
+        from onepasswd import web
+    except ImportError:
+        click.echo('you must install flask if you want to use onepasswd web')
+        click.echo('try: pip install flask')
+        exit(1)
     web.init(from_ctx(ctx, 'config'))
     web.app.run(host=host, port=port, debug=debug)
 
 
 def save_passwd(ctx, entries, getpass):
     assert len(entries) >= 1
     db = get_db(ctx)
```

### Comparing `onepasswd-0.2.3rc3/onepasswd/config.py` & `onepasswd-0.2.4rc1/onepasswd/config.py`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/crypto.py` & `onepasswd-0.2.4rc1/onepasswd/crypto.py`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/ltlog.py` & `onepasswd-0.2.4rc1/onepasswd/ltlog.py`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/onepasswd.py` & `onepasswd-0.2.4rc1/onepasswd/onepasswd.py`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/templates/index.html` & `onepasswd-0.2.4rc1/onepasswd/templates/index.html`

 * *Files 20% similar despite different names*

```diff
@@ -2,31 +2,44 @@
 
 <head>
     <script src="/static/jquery-3.6.4.min.js" integrity="sha256-oP6HI9z1XaZNBrJURtCoUT5SUnxFr8s3BzRl+cbzUq8="></script>
     <link href="/static/bootstrap.min.css" rel="stylesheet"
         integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65">
     <script src="/static/bootstrap.bundle.min.js"></script>
     <link href="/static/inconsolata:wght@500.css" rel="stylesheet">
+    <script src="/static/jsencrypt.min.js"></script>
+    <script>
+        var pubkey = `{{ pubkey }}`;
+        var encryptor = new JSEncrypt();
+        encryptor.setPublicKey(pubkey, null, null, JSEncrypt.OAEP_SHA256);
+    </script>
 </head>
 
 <body>
+    <div class="input-group mb-3 search-bar text-bg-light p-3">
+        <input type="text" id="search-input" class="form-control" aria-label="Recipient's username"
+            aria-describedby="button-addon2" onkeydown="enterToCick(event, 'search-btn')">
+        <button class="btn btn-outline-secondary" type="search" id="search-btn"
+            onclick="onSearchClicked()">Search</button>
+    </div>
+
     <table class="table table-hover">
         <thead>
             <tr class="table-dark">
                 <th class="index" scope="col">#</th>
                 <th class="time" scope="col">Time</th>
                 <th class="entry" scope="col">Entry</th>
                 <th class="password" scope="col">Password</th>
                 <th class="operation"></th>
             </tr>
         </thead>
 
         <tbody>
             {% for item in items %}
-            <tr>
+            <tr index="{{ loop.index }}">
                 <th scope="row" class="index">{{ loop.index }}</th>
                 <td>{{ item.time }}</td>
                 <td>
                     {% for e in item.entry %}
                     <button type="button" onclick="onEntryClicked(this)" class="btn btn-secondary entry-btn">{{ e
                         }}</button>
                     {% endfor %}
@@ -37,24 +50,26 @@
                     <button type="button" class="btn btn-dark" onclick="onShowClicked(this)">show</button>
                 </td>
             </tr>
             {% endfor %}
         </tbody>
     </table>
 
+
     <!-- Modal -->
     <div class="modal fade" id="master-passwd-modal" tabindex="-1" aria-hidden="true">
         <div class="modal-dialog">
             <div class="modal-content">
                 <div class="modal-header">
                     <h1 class="modal-title fs-5">please input master password</h1>
                     <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                 </div>
                 <div class="modal-body">
-                    <input type="password" class="form-control" id="master-passwd" onkeydown="handleKeyDown(event)">
+                    <input type="password" class="form-control" id="master-passwd"
+                        onkeydown="enterToCick(event, 'master-passwd-ok')">
                 </div>
                 <div class="modal-footer">
                     <button type="button" id="master-passwd-ok" class="btn btn-primary">OK</button>
                 </div>
             </div>
         </div>
     </div>
@@ -75,17 +90,17 @@
         })
         $('#master-passwd-modal').on('shown.bs.modal', function () {
             $('#master-passwd').focus();
         })
 
         var copyToast = new bootstrap.Toast(document.getElementById("copy-toast"));
 
-        function handleKeyDown(event) {
+        function enterToCick(event, btnid) {
             if (event.key === 'Enter') {
-                $('#master-passwd-ok').click();
+                $('#' + btnid).click();
             }
         }
 
         function onEntryClicked(e) {
             copyText(e.innerText);
             copyToast.show();
         }
@@ -116,20 +131,64 @@
                 $(btn).text('show');
             }
         }
 
         function onPasswdOkClicked(resolve) {
             let input = document.getElementById('master-passwd');
             if (input.value != '')
-                masterPassword = input.value;
+                masterPassword = encryptor.encrypt(input.value);
             resolve();
             input.value = '';
             passwdModal.hide();
         }
 
+        function onSearchClicked() {
+            let input = document.getElementById('search-input');
+            console.log(input.value, input);
+            if (input.value == '') {
+                search([]);
+            } else {
+                search([input.value]);
+            }
+        }
+
+        function search(keywords) {
+            let rows = $('tbody > tr');
+            for (let i = 0; i < rows.length; i++) {
+                let found = false;
+                if (keywords.length != 0) {
+                    let s = new Set();
+                    let btns = $('.entry-btn', rows[i]);
+                    for (let j = 0; j < btns.length; j++) {
+                        let v = btns[j].innerText;
+                        let idx = matchKeywords(keywords, v);
+                        if (idx >= 0) {
+                            s.add(idx + 1);
+                        }
+                    }
+                    found = s.size == keywords.length;
+                } else {
+                    found = true;
+                }
+                rows[i].hidden = !found;
+            }
+        }
+
+        // focus on search
+        $('#search-input').focus();
+
+        function matchKeywords(keywords, val) {
+            for (let i = 0; i < keywords.length; i++) {
+                if (val.toLowerCase().indexOf(keywords[i].toLowerCase()) >= 0) {
+                    return i;
+                }
+            }
+            return -1;
+        }
+
         async function getMasterPassword() {
             if (masterPassword != "") {
                 return masterPassword;
             }
             let cnt = 0;
             let cb;
             let ele = document.getElementById('master-passwd-ok');
@@ -199,28 +258,34 @@
 
         table {
             width: 100%;
             text-align: left;
             table-layout: fixed;
         }
 
-        thead > th {
+        thead>th {
             padding: 10px !important;
             ;
         }
 
         thead {
             position: sticky;
             top: 0;
             font-size: x-large;
         }
 
+        .search-bar {
+            position: fixed;
+            bottom: 0;
+            margin-bottom: 0 !important;
+        }
+
         .index {
             width: 3rem;
-            border-right: 1px solid black !important; 
+            border-right: 1px solid black !important;
         }
 
         .time {
             width: 11rem;
         }
 
         .password {
```

#### html2text {}

```diff
@@ -1,9 +1,10 @@
 
 
+[                    ] Search
 #                Time            Entry                       Password
 {{ loop.index }} {{ item.time }} {% for e in item.entry %} { ****     copy show
                                  { e }} {% endfor %}
 ****** please input master password ******
 [********************]
 OK
 å·²å¤å¶
```

### Comparing `onepasswd-0.2.3rc3/onepasswd/templates/static/bootstrap.bundle.min.js` & `onepasswd-0.2.4rc1/onepasswd/templates/static/bootstrap.bundle.min.js`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/templates/static/bootstrap.min.css` & `onepasswd-0.2.4rc1/onepasswd/templates/static/bootstrap.min.css`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/templates/static/jquery-3.6.4.min.js` & `onepasswd-0.2.4rc1/onepasswd/templates/static/jquery-3.6.4.min.js`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/tools/jdiff.py` & `onepasswd-0.2.4rc1/onepasswd/tools/jdiff.py`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/tools/jmerge.py` & `onepasswd-0.2.4rc1/onepasswd/tools/jmerge.py`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/tools/upgrade.py` & `onepasswd-0.2.4rc1/onepasswd/tools/upgrade.py`

 * *Files identical despite different names*

### Comparing `onepasswd-0.2.3rc3/onepasswd/web.py` & `onepasswd-0.2.4rc1/onepasswd/web.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,18 +1,23 @@
 from flask import Flask
 from flask import render_template
-from flask import request, make_response, send_from_directory
+from flask import request, make_response
 from onepasswd import crypto
 from onepasswd import ltlog
 from onepasswd.onepasswd import DB
 import datetime
 import os
+from Crypto.PublicKey import RSA
+import base64
+from Crypto.Cipher import PKCS1_v1_5
 
 log = ltlog.getLogger('onepasswd.web')
 
+_key = RSA.generate(2048)
+_public_key = _key.public_key().export_key(format='PEM').decode()
 _db_path = ''
 _web_path = os.path.abspath(
     os.path.join(os.path.dirname(__file__), 'templates'))
 app = Flask("onepasswd", template_folder=_web_path,
             static_folder=os.path.join(_web_path, 'static'))
 
 
@@ -31,22 +36,27 @@
     items = sorted(items, key=lambda v: float(v['time']), reverse=True)
     for i, v in enumerate(items):
         items[i] = {
             'time': str(datetime.datetime.fromtimestamp(int(float(v['time'])))),
             'entry': v['entries'],
             'data': v['passwd']
         }
-    return render_template('index.html', items=items)
+    return render_template('index.html', items=items, pubkey=_public_key)
 
 
 @app.post("/decrypt")
 def decrypt():
+    resp_500 = make_response()
+    resp_500.status_code = 500
+
     data = request.json['data']
     passwd = request.json['passwd']
     log.debug(request.json)
+    decryptor = PKCS1_v1_5.new(_key)
+    passwd = decryptor.decrypt(base64.b64decode(passwd.encode()), None).decode()
+    if not passwd:
+        return resp_500
     try:
         text = crypto.decrypt_passwd(data, passwd)
     except:
-        resp = make_response()
-        resp.status_code = 500
-        return resp
+        return resp_500
     return {'data': text}
```

### Comparing `onepasswd-0.2.3rc3/onepasswd.egg-info/SOURCES.txt` & `onepasswd-0.2.4rc1/onepasswd.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -18,11 +18,12 @@
 onepasswd.egg-info/requires.txt
 onepasswd.egg-info/top_level.txt
 onepasswd/templates/index.html
 onepasswd/templates/static/bootstrap.bundle.min.js
 onepasswd/templates/static/bootstrap.min.css
 onepasswd/templates/static/inconsolata:wght@500.css
 onepasswd/templates/static/jquery-3.6.4.min.js
+onepasswd/templates/static/jsencrypt.min.js
 onepasswd/tools/__init__.py
 onepasswd/tools/jdiff.py
 onepasswd/tools/jmerge.py
 onepasswd/tools/upgrade.py
```

### Comparing `onepasswd-0.2.3rc3/setup.py` & `onepasswd-0.2.4rc1/setup.py`

 * *Files identical despite different names*

