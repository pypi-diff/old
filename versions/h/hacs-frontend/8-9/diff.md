# Comparing `tmp/hacs-frontend-8.tar.gz` & `tmp/hacs-frontend-9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/hacs-frontend-8.tar", last modified: Sun Nov 17 12:38:19 2019, max compression
+gzip compressed data, was "dist/hacs-frontend-9.tar", last modified: Sun Nov 17 16:50:42 2019, max compression
```

## Comparing `hacs-frontend-8.tar` & `hacs-frontend-9.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (115)        0 2019-11-17 12:38:19.815927 hacs-frontend-8/
--rw-r--r--   0 runner    (1001) docker     (115)       45 2019-11-17 12:37:43.000000 hacs-frontend-8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (115)      236 2019-11-17 12:38:19.815927 hacs-frontend-8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (115)      171 2019-11-17 12:37:43.000000 hacs-frontend-8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (115)        0 2019-11-17 12:38:19.815927 hacs-frontend-8/hacs_frontend/
--rw-r--r--   0 runner    (1001) docker     (115)      181 2019-11-17 12:37:43.000000 hacs-frontend-8/hacs_frontend/__init__.py
--rw-r--r--   0 runner    (1001) docker     (115)    80725 2019-11-17 12:38:19.000000 hacs-frontend-8/hacs_frontend/main.js
--rw-r--r--   0 runner    (1001) docker     (115)    17642 2019-11-17 12:38:19.000000 hacs-frontend-8/hacs_frontend/main.js.gz
-drwxr-xr-x   0 runner    (1001) docker     (115)        0 2019-11-17 12:38:19.815927 hacs-frontend-8/hacs_frontend.egg-info/
--rw-r--r--   0 runner    (1001) docker     (115)      236 2019-11-17 12:38:19.000000 hacs-frontend-8/hacs_frontend.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (115)      287 2019-11-17 12:38:19.000000 hacs-frontend-8/hacs_frontend.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (115)        1 2019-11-17 12:38:19.000000 hacs-frontend-8/hacs_frontend.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (115)        1 2019-11-17 12:38:19.000000 hacs-frontend-8/hacs_frontend.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (115)       14 2019-11-17 12:38:19.000000 hacs-frontend-8/hacs_frontend.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (115)       38 2019-11-17 12:38:19.815927 hacs-frontend-8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (115)      377 2019-11-17 12:37:45.000000 hacs-frontend-8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (115)        0 2019-11-17 16:50:42.070242 hacs-frontend-9/
+-rw-r--r--   0 runner    (1001) docker     (115)       45 2019-11-17 16:50:02.000000 hacs-frontend-9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (115)      236 2019-11-17 16:50:42.070242 hacs-frontend-9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (115)      171 2019-11-17 16:50:02.000000 hacs-frontend-9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (115)        0 2019-11-17 16:50:42.070242 hacs-frontend-9/hacs_frontend/
+-rw-r--r--   0 runner    (1001) docker     (115)      181 2019-11-17 16:50:02.000000 hacs-frontend-9/hacs_frontend/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (115)    80762 2019-11-17 16:50:41.000000 hacs-frontend-9/hacs_frontend/main.js
+-rw-r--r--   0 runner    (1001) docker     (115)    17658 2019-11-17 16:50:41.000000 hacs-frontend-9/hacs_frontend/main.js.gz
+drwxr-xr-x   0 runner    (1001) docker     (115)        0 2019-11-17 16:50:42.070242 hacs-frontend-9/hacs_frontend.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (115)      236 2019-11-17 16:50:41.000000 hacs-frontend-9/hacs_frontend.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (115)      287 2019-11-17 16:50:41.000000 hacs-frontend-9/hacs_frontend.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (115)        1 2019-11-17 16:50:41.000000 hacs-frontend-9/hacs_frontend.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (115)        1 2019-11-17 16:50:41.000000 hacs-frontend-9/hacs_frontend.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (115)       14 2019-11-17 16:50:41.000000 hacs-frontend-9/hacs_frontend.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (115)       38 2019-11-17 16:50:42.070242 hacs-frontend-9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (115)      377 2019-11-17 16:50:04.000000 hacs-frontend-9/setup.py
```

### Comparing `hacs-frontend-8/hacs_frontend/main.js` & `hacs-frontend-9/hacs_frontend/main.js`

 * *Files 2% similar despite different names*

#### js-beautify {}

```diff
@@ -1192,22 +1192,29 @@
             o = `/community_plugin/${t.full_name.split("/")[1]}/${t.file_name}`;
         return void 0 !== e.resources && e.resources.forEach(t => {
             s || t.url === o && (s = !0)
         }), s
     }
     return !0
 }
+
+function bt(t, e) {
+    var s = !1;
+    return e.config.components.forEach(e => {
+        e.includes(t.domain) && (s = !0)
+    }), s
+}
 ft = t([st("hacs-help-button")], ft);
-class bt extends lt {
+class wt extends lt {
     static get styles() {
         return vt
     }
 }
-t([rt()], bt.prototype, "hass", void 0), t([rt()], bt.prototype, "repository", void 0);
-let wt = class extends bt {
+t([rt()], wt.prototype, "hass", void 0), t([rt()], wt.prototype, "repository", void 0);
+let $t = class extends wt {
     render() {
         return M`
             <mwc-button @click=${this.ExecuteAction}>
                 ${this.hass.localize("component.hacs.store.clear_new")}
             </mwc-button>
         `
     }
@@ -1216,16 +1223,16 @@
             type: "hacs/settings",
             action: "clear_new",
             category: this.category
         };
         this.hass.connection.sendMessage(t)
     }
 };
-t([rt()], wt.prototype, "category", void 0), wt = t([st("hacs-button-clear-new")], wt);
-let $t = class extends lt {
+t([rt()], $t.prototype, "category", void 0), $t = t([st("hacs-button-clear-new")], $t);
+let xt = class extends lt {
     constructor() {
         super(...arguments), this.repository_view = !1, this.SearchTerm = ""
     }
     render() {
         if ("repository" === this.panel) return M`
       <hacs-panel-repository
         .hass=${this.hass}
@@ -1358,15 +1365,15 @@
     </script>
           `
         }
     }
     StatusAndDescription(t) {
         var e = t.status,
             s = t.status_description;
-        return t.installed && ("plugin" !== t.category || _t(t, this.lovelaceconfig) ? "integration" !== t.category || this.hass.config.components.includes(t.domain) || (e = "pending-restart", s = "Not loaded in Home Assistant") : (e = "pending-restart", s = "Not loaded in lovelace")), {
+        return t.installed && ("plugin" !== t.category || _t(t, this.lovelaceconfig) ? "integration" !== t.category || bt(t, this.hass) || (e = "pending-restart", s = "Not loaded in Home Assistant") : (e = "pending-restart", s = "Not loaded in lovelace")), {
             status: e,
             description: s
         }
     }
     DoSearch(t) {
         this.SearchTerm = t.composedPath()[0].value.toLowerCase(), localStorage.setItem("hacs-search", this.SearchTerm)
     }
@@ -1450,59 +1457,59 @@
           .content {
             padding: 0;
           }
         }
     `]
     }
 };
-t([rt()], $t.prototype, "hass", void 0), t([rt()], $t.prototype, "repositories", void 0), t([rt()], $t.prototype, "configuration", void 0), t([rt()], $t.prototype, "route", void 0), t([rt()], $t.prototype, "panel", void 0), t([rt()], $t.prototype, "repository_view", void 0), t([rt()], $t.prototype, "repository", void 0), t([rt()], $t.prototype, "SearchTerm", void 0), t([rt()], $t.prototype, "lovelaceconfig", void 0), $t = t([st("hacs-panel")], $t);
+t([rt()], xt.prototype, "hass", void 0), t([rt()], xt.prototype, "repositories", void 0), t([rt()], xt.prototype, "configuration", void 0), t([rt()], xt.prototype, "route", void 0), t([rt()], xt.prototype, "panel", void 0), t([rt()], xt.prototype, "repository_view", void 0), t([rt()], xt.prototype, "repository", void 0), t([rt()], xt.prototype, "SearchTerm", void 0), t([rt()], xt.prototype, "lovelaceconfig", void 0), xt = t([st("hacs-panel")], xt);
 /**
  * @license
  * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
  * This code may only be used under the BSD style license found at
  * http://polymer.github.io/LICENSE.txt
  * The complete set of authors may be found at
  * http://polymer.github.io/AUTHORS.txt
  * The complete set of contributors may be found at
  * http://polymer.github.io/CONTRIBUTORS.txt
  * Code distributed by Google as part of the polymer project is also
  * subject to an additional IP rights grant found at
  * http://polymer.github.io/PATENTS.txt
  */
-const xt = new WeakMap,
-    St = (t => (...s) => {
+const St = new WeakMap,
+    kt = (t => (...s) => {
         const o = t(...s);
         return e.set(o, !0), o
     })(t => e => {
         if (!(e instanceof x)) throw new Error("unsafeHTML can only be used in text bindings");
-        const s = xt.get(e);
+        const s = St.get(e);
         if (void 0 !== s && _(t) && t === s.value && e.value === s.fragment) return;
         const o = document.createElement("template");
         o.innerHTML = t;
         const i = document.importNode(o.content, !0);
-        e.setValue(i), xt.set(e, {
+        e.setValue(i), St.set(e, {
             value: t,
             fragment: i
         })
     });
 
-function kt(t, e, s, o) {
+function Pt(t, e, s, o) {
     let i;
     i = void 0 !== o ? {
         type: "hacs/repository/data",
         action: s,
         repository: e,
         data: o
     } : {
         type: "hacs/repository",
         action: s,
         repository: e
     }, t.connection.sendMessage(i)
 }
-let Pt = class extends lt {
+let Ct = class extends lt {
     render() {
         return "0" === String(this.authors.length) ? M`` : M`
             <div class="autors">
                 <p><b>${this.hass.localize("component.hacs.repository.authors")}: </b>
 
                     ${this.authors.map(t=>M`
                         <a href="https://github.com/${t.replace("@","")}"
@@ -1518,16 +1525,16 @@
         return [vt, pt`
             .autors {
 
             }
         `]
     }
 };
-t([rt()], Pt.prototype, "hass", void 0), t([rt()], Pt.prototype, "authors", void 0), Pt = t([st("hacs-authors")], Pt);
-let Ct = class extends lt {
+t([rt()], Ct.prototype, "hass", void 0), t([rt()], Ct.prototype, "authors", void 0), Ct = t([st("hacs-authors")], Ct);
+let At = class extends lt {
     render() {
         return M`
         <paper-menu-button no-animations horizontal-align="right" role="group" aria-haspopup="true" vertical-align="top" aria-disabled="false">
         <paper-icon-button icon="hass:dots-vertical" slot="dropdown-trigger" role="button"></paper-icon-button>
             <paper-listbox slot="dropdown-content" role="listbox" tabindex="0">
 
 
@@ -1578,68 +1585,68 @@
           paper-menu-button {
             float: right;
             top: -65px;
           }
         `]
     }
     RepositoryReload() {
-        kt(this.hass, this.repository.id, "set_state", "other"), kt(this.hass, this.repository.id, "update")
+        Pt(this.hass, this.repository.id, "set_state", "other"), Pt(this.hass, this.repository.id, "update")
     }
     RepositoryBeta() {
-        kt(this.hass, this.repository.id, "set_state", "other"), this.repository.beta ? kt(this.hass, this.repository.id, "hide_beta") : kt(this.hass, this.repository.id, "show_beta")
+        Pt(this.hass, this.repository.id, "set_state", "other"), this.repository.beta ? Pt(this.hass, this.repository.id, "hide_beta") : Pt(this.hass, this.repository.id, "show_beta")
     }
     RepositoryHide() {
-        kt(this.hass, this.repository.id, "set_state", "other"), this.repository.hide ? kt(this.hass, this.repository.id, "unhide") : kt(this.hass, this.repository.id, "hide")
+        Pt(this.hass, this.repository.id, "set_state", "other"), this.repository.hide ? Pt(this.hass, this.repository.id, "unhide") : Pt(this.hass, this.repository.id, "hide")
     }
 };
-t([rt()], Ct.prototype, "hass", void 0), t([rt()], Ct.prototype, "repository", void 0), Ct = t([st("hacs-repository-menu")], Ct);
-let At = class extends bt {
+t([rt()], At.prototype, "hass", void 0), t([rt()], At.prototype, "repository", void 0), At = t([st("hacs-repository-menu")], At);
+let Tt = class extends wt {
     render() {
         if ("plugin" != this.repository.category) return M``;
         if (!this.repository.installed) return M``;
         const t = this.repository.local_path.split("/");
         return M`
             <a href="/community_plugin/${t.pop()}/${this.repository.file_name}" target="_blank">
                 <mwc-button>
                     ${this.hass.localize("component.hacs.repository.open_plugin")}
                 </mwc-button>
             </a>
         `
     }
 };
-At = t([st("hacs-button-open-plugin")], At);
-let Tt = class extends bt {
+Tt = t([st("hacs-button-open-plugin")], Tt);
+let zt = class extends wt {
     render() {
         return M`
             <a href="https://github.com/${this.repository.full_name}" rel='noreferrer' target="_blank">
                 <mwc-button>
                     ${this.hass.localize("component.hacs.repository.repository")}
                 </mwc-button>
             </a>
         `
     }
 };
-Tt = t([st("hacs-button-open-repository")], Tt);
-let zt = class extends bt {
+zt = t([st("hacs-button-open-repository")], zt);
+let Et = class extends wt {
     render() {
         return this.repository.installed ? M`
             <mwc-button @click=${this.RepositoryUnInstall}>
                 ${"uninstalling"==this.repository.state?M`<paper-spinner active></paper-spinner>`:M`${this.hass.localize("component.hacs.repository.uninstall")}`}
             </mwc-button>
         ` : M``
     }
     RepositoryUnInstall() {
         window.confirm(this.hass.localize("component.hacs.confirm.uninstall", "item", this.repository.name)) && this.ExecuteAction()
     }
     ExecuteAction() {
-        kt(this.hass, this.repository.id, "set_state", "uninstalling"), kt(this.hass, this.repository.id, "uninstall")
+        Pt(this.hass, this.repository.id, "set_state", "uninstalling"), Pt(this.hass, this.repository.id, "uninstall")
     }
 };
-zt = t([st("hacs-button-uninstall")], zt);
-let Et = class extends bt {
+Et = t([st("hacs-button-uninstall")], Et);
+let Nt = class extends wt {
     constructor() {
         super(...arguments), this.pathExists = !1
     }
     firstUpdated() {
         this.hass.connection.sendMessagePromise({
             type: "hacs/check_path",
             path: this.repository.local_path
@@ -1656,36 +1663,36 @@
             </mwc-button>
         `
     }
     RepositoryInstall() {
         this.repository.can_install ? this.pathExists && !this.repository.installed ? window.confirm(this.hass.localize("component.hacs.confirm.exsist", "item", this.repository.local_path) + "\n" + this.hass.localize("component.hacs.confirm.overwrite") + "\n" + this.hass.localize("component.hacs.confirm.continue")) && this.ExecuteAction() : this.ExecuteAction() : window.alert(`This repository version requires Home Assistant version ${this.repository.homeassistant}`)
     }
     ExecuteAction() {
-        kt(this.hass, this.repository.id, "set_state", "installing"), kt(this.hass, this.repository.id, "install")
+        Pt(this.hass, this.repository.id, "set_state", "installing"), Pt(this.hass, this.repository.id, "install")
     }
 };
-t([rt()], Et.prototype, "pathExists", void 0), Et = t([st("hacs-button-main-action")], Et);
-let Nt = class extends bt {
+t([rt()], Nt.prototype, "pathExists", void 0), Nt = t([st("hacs-button-main-action")], Nt);
+let Rt = class extends wt {
     render() {
         if (!this.repository.pending_upgrade) return M``;
         var t = `https://github.com/${this.repository.full_name}/releases`;
         return "commit" === this.repository.version_or_commit && (t = `https://github.com/${this.repository.full_name}/compare/${this.repository.installed_version}...${this.repository.available_version}`), M`
         <a href="${t}" rel='noreferrer' target="_blank">
           <mwc-button>
           ${this.hass.localize("component.hacs.repository.changelog")}
           </mwc-button>
         </a>
         `
     }
     RepositoryInstall() {
-        kt(this.hass, this.repository.id, "set_state", "installing"), kt(this.hass, this.repository.id, "uninstall")
+        Pt(this.hass, this.repository.id, "set_state", "installing"), Pt(this.hass, this.repository.id, "uninstall")
     }
 };
-Nt = t([st("hacs-button-changelog")], Nt);
-let Rt = class extends lt {
+Rt = t([st("hacs-button-changelog")], Rt);
+let Mt = class extends lt {
     render() {
         return M`
             <div class="lovelace-hint">
                 <p class="example-title">${this.hass.localize("component.hacs.repository.lovelace_instruction")}:</p>
                 <pre id="LovelaceExample" class="yaml">
 - url: /community_plugin/${this.repository.full_name.split("/")[1]}/${this.repository.file_name}
   type: ${void 0!==this.repository.javascript_type?M`${this.repository.javascript_type}`:M`${this.hass.localize("component.hacs.repository.lovelace_no_js_type")}`}</pre>
@@ -1724,16 +1731,16 @@
                 width: calc(100% - 46px);
                 white-space: pre-wrap;
             }
 
         `]
     }
 };
-t([rt()], Rt.prototype, "hass", void 0), t([rt()], Rt.prototype, "configuration", void 0), t([rt()], Rt.prototype, "repository", void 0), Rt = t([st("hacs-lovelace-hint")], Rt);
-let Mt = class extends lt {
+t([rt()], Mt.prototype, "hass", void 0), t([rt()], Mt.prototype, "configuration", void 0), t([rt()], Mt.prototype, "repository", void 0), Mt = t([st("hacs-lovelace-hint")], Mt);
+let Vt = class extends lt {
     render() {
         return M`
             <div class="repository-note">
             <p>${this.hass.localize("component.hacs.repository.note_installed")} '${this.repository.local_path}'
 
             ${"appdaemon"===this.repository.category?M`,
             ${this.hass.localize(`component.hacs.repository.note_${this.repository.category}`)}`:""}
@@ -1763,16 +1770,16 @@
             }
             p {
                 font-style: italic;
             }
         `]
     }
 };
-t([rt()], Mt.prototype, "hass", void 0), t([rt()], Mt.prototype, "configuration", void 0), t([rt()], Mt.prototype, "repository", void 0), Mt = t([st("hacs-repository-note")], Mt);
-let Vt = class extends bt {
+t([rt()], Vt.prototype, "hass", void 0), t([rt()], Vt.prototype, "configuration", void 0), t([rt()], Vt.prototype, "repository", void 0), Vt = t([st("hacs-repository-note")], Vt);
+let Ut = class extends wt {
     render() {
         return this.configuration.experimental && this.repository.installed ? null === this.repository.javascript_type ? M`` : M`
             <mwc-button @click=${this.RepositoryAddToLovelace}>
                 Add to Lovelace
             </mwc-button>
         ` : M``
     }
@@ -1791,24 +1798,25 @@
                 config: e
             })
         }, t => {
             console.error(t)
         })
     }
 };
-t([rt()], Vt.prototype, "lovelaceconfig", void 0), t([rt()], Vt.prototype, "configuration", void 0), Vt = t([st("hacs-button-add-to-lovelace")], Vt);
-let Ut = class extends lt {
+t([rt()], Ut.prototype, "lovelaceconfig", void 0), t([rt()], Ut.prototype, "configuration", void 0), Ut = t([st("hacs-button-add-to-lovelace")], Ut);
+let Dt = class extends lt {
     render() {
         if (!this.repository.installed) return M``;
         var t = "",
             e = "",
             s = "";
         if ("pending-restart" == this.repository.status) s = "alert", e = "Restart pending", t = "\n            You need to restart Home Assistant.\n            ";
-        else if ("integration" == this.repository.category) this.hass.config.components.includes(this.repository.domain) || (s = "warning", e = "Not Loaded", t = "\n                This integration is not loaded in Home Assistant.\n                ");
-        else if ("plugin" == this.repository.category) {
+        else if ("integration" == this.repository.category) {
+            bt(this.repository, this.hass) || (s = "warning", e = "Not Loaded", t = "\n                This integration is not loaded in Home Assistant.\n                ")
+        } else if ("plugin" == this.repository.category) {
             if (void 0 !== this.lovelaceconfig) _t(this.repository, this.lovelaceconfig) || (s = "warning", e = "Not Loaded", t = "\n                    This plugin is not added to your Lovelace resources.\n                    ")
         }
         return 0 == t.length ? M`` : "plugin" !== this.repository.category ? M`
             <ha-card header="${e}" class="${s}">
                 <div class="card-content">
                     ${t}
                 </div>
@@ -1845,21 +1853,21 @@
             }
             .info {
 
             }
         `]
     }
 };
-t([rt()], Ut.prototype, "hass", void 0), t([rt()], Ut.prototype, "repository", void 0), t([rt()], Ut.prototype, "configuration", void 0), t([rt()], Ut.prototype, "lovelaceconfig", void 0), Ut = t([st("hacs-repository-banner-note")], Ut);
-let Dt = class extends lt {
+t([rt()], Dt.prototype, "hass", void 0), t([rt()], Dt.prototype, "repository", void 0), t([rt()], Dt.prototype, "configuration", void 0), t([rt()], Dt.prototype, "lovelaceconfig", void 0), Dt = t([st("hacs-repository-banner-note")], Dt);
+let Lt = class extends lt {
     constructor() {
         super(...arguments), this.repository_view = !1
     }
     firstUpdated() {
-        this.repo.updated_info || (kt(this.hass, this.repo.id, "set_state", "other"), kt(this.hass, this.repo.id, "update"))
+        this.repo.updated_info || (Pt(this.hass, this.repo.id, "set_state", "other"), Pt(this.hass, this.repo.id, "update"))
     }
     render() {
         if (void 0 === this.repository) return M`
       <hacs-panel
         .hass=${this.hass}
         .configuration=${this.configuration}
         .repositories=${this.repositories}
@@ -1949,29 +1957,29 @@
       </div>
 
     </ha-card>
 
     <ha-card class="additional">
       <div class="card-content">
         <div class="more_info">
-          ${St(this.repo.additional_info)}
+          ${kt(this.repo.additional_info)}
         </div>
       <hacs-repository-note
         .hass=${this.hass}
         .configuration=${this.configuration}
         .repository=${this.repo}
       ></hacs-repository-note>
       </div>
     </ha-card>
           `
     }
     SetVersion(t) {
-        kt(this.hass, this.repo.id, "set_state", "other");
+        Pt(this.hass, this.repo.id, "set_state", "other");
         var e = t.composedPath()[2].outerText;
-        e && kt(this.hass, this.repo.id, "set_version", e)
+        e && Pt(this.hass, this.repo.id, "set_version", e)
     }
     GoBackToStore() {
         this.repository = void 0, this.repo.installed ? this.panel = "installed" : this.panel = this.repo.category, ut(0, `/${this._rootPath}/${this.panel}`), this.requestUpdate()
     }
     get _rootPath() {
         return "hacs_dev" === window.location.pathname.split("/")[1] ? "hacs_dev" : "hacs"
     }
@@ -2023,30 +2031,30 @@
         color: var(--dark-primary-color);
         margin-right: 8px;
       }
 
     `]
     }
 };
-t([rt()], Dt.prototype, "hass", void 0), t([rt()], Dt.prototype, "repositories", void 0), t([rt()], Dt.prototype, "configuration", void 0), t([rt()], Dt.prototype, "repository", void 0), t([rt()], Dt.prototype, "panel", void 0), t([rt()], Dt.prototype, "route", void 0), t([rt()], Dt.prototype, "repository_view", void 0), t([rt()], Dt.prototype, "repo", void 0), t([rt()], Dt.prototype, "lovelaceconfig", void 0), Dt = t([st("hacs-panel-repository")], Dt);
-let Lt = class extends lt {
+t([rt()], Lt.prototype, "hass", void 0), t([rt()], Lt.prototype, "repositories", void 0), t([rt()], Lt.prototype, "configuration", void 0), t([rt()], Lt.prototype, "repository", void 0), t([rt()], Lt.prototype, "panel", void 0), t([rt()], Lt.prototype, "route", void 0), t([rt()], Lt.prototype, "repository_view", void 0), t([rt()], Lt.prototype, "repo", void 0), t([rt()], Lt.prototype, "lovelaceconfig", void 0), Lt = t([st("hacs-panel-repository")], Lt);
+let It = class extends lt {
     updated() {
         this.SaveSpinner = !1
     }
     Delete(t) {
         if (window.confirm(this.hass.localize("component.hacs.confirm.delete", "item", t.composedPath()[3].innerText))) {
             var e = t.composedPath()[4].repoID;
-            kt(this.hass, e, "delete")
+            Pt(this.hass, e, "delete")
         }
     }
     Save(t) {
         this.SaveSpinner = !0;
         var e = t.composedPath()[1].children[1].selectedItem.category,
             s = t.composedPath()[1].children[0].value;
-        kt(this.hass, s, "add", e)
+        Pt(this.hass, s, "add", e)
     }
     render() {
         return this.custom = this.repositories.filter((function(t) {
             return !!t.custom
         })), M`
         <ha-card header="${this.hass.localize("component.hacs.settings.custom_repositories")}">
             <div class="card-content">
@@ -2127,19 +2135,19 @@
                 position: absolute;
                 right: 10px;
                 bottom: 22px;
             }
         `]
     }
 };
-t([rt()], Lt.prototype, "hass", void 0), t([rt()], Lt.prototype, "repositories", void 0), t([rt()], Lt.prototype, "custom", void 0), t([rt()], Lt.prototype, "status", void 0), t([rt()], Lt.prototype, "configuration", void 0), t([rt()], Lt.prototype, "SaveSpinner", void 0), Lt = t([st("hacs-custom-repositories")], Lt);
-let It = class extends lt {
+t([rt()], It.prototype, "hass", void 0), t([rt()], It.prototype, "repositories", void 0), t([rt()], It.prototype, "custom", void 0), t([rt()], It.prototype, "status", void 0), t([rt()], It.prototype, "configuration", void 0), t([rt()], It.prototype, "SaveSpinner", void 0), It = t([st("hacs-custom-repositories")], It);
+let Ot = class extends lt {
     UnHide(t) {
         var e = t.composedPath()[4].repoID;
-        kt(this.hass, e, "unhide")
+        Pt(this.hass, e, "unhide")
     }
     render() {
         return this._hidden = this.repositories.filter((function(t) {
             return t.hide
         })), 0 === this._hidden.length ? M`` : M`
         <ha-card header="${this.hass.localize("component.hacs.settings.hidden_repositories").toUpperCase()}">
             <div class="card-content">
@@ -2171,16 +2179,16 @@
             .listicon {
                 color: var(--primary-color);
                 left: 0px;
             }
         `]
     }
 };
-t([rt()], It.prototype, "hass", void 0), t([rt()], It.prototype, "repositories", void 0), t([rt()], It.prototype, "_hidden", void 0), It = t([st("hacs-hidden-repositories")], It);
-let Ot = class extends lt {
+t([rt()], Ot.prototype, "hass", void 0), t([rt()], Ot.prototype, "repositories", void 0), t([rt()], Ot.prototype, "_hidden", void 0), Ot = t([st("hacs-hidden-repositories")], Ot);
+let qt = class extends lt {
     render() {
         return this.status.reloading_data, M`
 
     <ha-card header="${this.hass.localize("component.hacs.config.title")}">
       <div class="card-content">
         <p><b>${this.hass.localize("component.hacs.common.version")}:</b> ${this.configuration.version}</p>
         <p><b>${this.hass.localize("component.hacs.common.repositories")}:</b> ${this.repositories.length}</p>
@@ -2290,16 +2298,16 @@
     }
     mwc-button {
       margin: 0 8px 0 8px;
     }
     `]
     }
 };
-t([rt()], Ot.prototype, "hass", void 0), t([rt()], Ot.prototype, "repositories", void 0), t([rt()], Ot.prototype, "configuration", void 0), t([rt()], Ot.prototype, "status", void 0), Ot = t([st("hacs-panel-settings")], Ot);
-let qt = class extends lt {
+t([rt()], qt.prototype, "hass", void 0), t([rt()], qt.prototype, "repositories", void 0), t([rt()], qt.prototype, "configuration", void 0), t([rt()], qt.prototype, "status", void 0), qt = t([st("hacs-panel-settings")], qt);
+let Ht = class extends lt {
     constructor() {
         super(...arguments), this.error = void 0
     }
     clearError() {
         this.error = void 0
     }
     firstUpdated() {
@@ -2339,16 +2347,16 @@
             .alert {
                 background-color: var(--hacs-status-pending-restart);
                 color: var(--text-primary-color);
             }
         `]
     }
 };
-t([rt()], qt.prototype, "hass", void 0), t([rt()], qt.prototype, "error", void 0), qt = t([st("hacs-error")], qt);
-let Ht = class extends lt {
+t([rt()], Ht.prototype, "hass", void 0), t([rt()], Ht.prototype, "error", void 0), Ht = t([st("hacs-error")], Ht);
+let jt = class extends lt {
     async Acknowledge(t) {
         var e = t.composedPath()[3].repository;
         const s = await this.hass.connection.sendMessagePromise({
             type: "hacs/critical",
             repository: e
         });
         this.critical = s.data
@@ -2394,16 +2402,16 @@
             .alert {
                 background-color: var(--hacs-status-pending-restart);
                 color: var(--text-primary-color);
             }
         `]
     }
 };
-t([rt()], Ht.prototype, "hass", void 0), t([rt()], Ht.prototype, "critical", void 0), Ht = t([st("hacs-critical")], Ht);
-let jt = class extends lt {
+t([rt()], jt.prototype, "hass", void 0), t([rt()], jt.prototype, "critical", void 0), jt = t([st("hacs-critical")], jt);
+let Ft = class extends lt {
     constructor() {
         super(...arguments), this.repository_view = !1
     }
     getRepositories() {
         this.hass.connection.sendMessagePromise({
             type: "hacs/repositories"
         }).then(t => {
@@ -2562,8 +2570,8 @@
       z-index: 99;
       width: 300px;
       height: 300px;
    }
     `]
     }
 };
-t([rt()], jt.prototype, "hass", void 0), t([rt()], jt.prototype, "repositories", void 0), t([rt()], jt.prototype, "configuration", void 0), t([rt()], jt.prototype, "status", void 0), t([rt()], jt.prototype, "route", void 0), t([rt()], jt.prototype, "critical", void 0), t([rt()], jt.prototype, "narrow", void 0), t([rt()], jt.prototype, "panel", void 0), t([rt()], jt.prototype, "repository", void 0), t([rt()], jt.prototype, "repository_view", void 0), t([rt()], jt.prototype, "lovelaceconfig", void 0), jt = t([st("hacs-frontend")], jt);
+t([rt()], Ft.prototype, "hass", void 0), t([rt()], Ft.prototype, "repositories", void 0), t([rt()], Ft.prototype, "configuration", void 0), t([rt()], Ft.prototype, "status", void 0), t([rt()], Ft.prototype, "route", void 0), t([rt()], Ft.prototype, "critical", void 0), t([rt()], Ft.prototype, "narrow", void 0), t([rt()], Ft.prototype, "panel", void 0), t([rt()], Ft.prototype, "repository", void 0), t([rt()], Ft.prototype, "repository_view", void 0), t([rt()], Ft.prototype, "lovelaceconfig", void 0), Ft = t([st("hacs-frontend")], Ft);
```

