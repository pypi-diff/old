# Comparing `tmp/stackdiac-0.0.1.dev8.tar.gz` & `tmp/stackdiac-0.0.1.dev9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "stackdiac-0.0.1.dev8.tar", max compression
+gzip compressed data, was "stackdiac-0.0.1.dev9.tar", max compression
```

## Comparing `stackdiac-0.0.1.dev8.tar` & `stackdiac-0.0.1.dev9.tar`

### file list

```diff
@@ -1,24 +1,25 @@
--rw-r--r--   0        0        0     1066 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/LICENSE
--rw-r--r--   0        0        0      867 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/README.md
--rw-r--r--   0        0        0      554 2023-03-29 10:24:30.471415 stackdiac-0.0.1.dev8/pyproject.toml
--rw-r--r--   0        0        0        0 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/__init__.py
--rw-r--r--   0        0        0       23 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/api/__init__.py
--rw-r--r--   0        0        0     1179 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/api/server.py
--rw-r--r--   0        0        0     1621 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/cli/__init__.py
--rw-r--r--   0        0        0      729 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/cli/build.py
--rw-r--r--   0        0        0     1594 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/cli/create.py
--rw-r--r--   0        0        0      464 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/cli/ui.py
--rw-r--r--   0        0        0      325 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/models/__init__.py
--rw-r--r--   0        0        0     1956 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/models/binary.py
--rw-r--r--   0        0        0     3240 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/models/cluster.py
--rw-r--r--   0        0        0     2414 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/models/config.py
--rw-r--r--   0        0        0      161 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/models/provider.py
--rw-r--r--   0        0        0     5172 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/models/repo.py
--rw-r--r--   0        0        0     4903 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/models/stack.py
--rw-r--r--   0        0        0       72 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/stackd/__init__.py
--rw-r--r--   0        0        0      256 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/stackd/sdmod.py
--rw-r--r--   0        0        0     6195 2023-03-29 10:24:17.363254 stackdiac-0.0.1.dev8/stackdiac/stackd/stackd.py
--rw-r--r--   0        0        0   338698 2023-03-29 10:24:17.367254 stackdiac-0.0.1.dev8/stackdiac/ui/bundle.js
--rw-r--r--   0        0        0     2572 2023-03-29 10:24:17.367254 stackdiac-0.0.1.dev8/stackdiac/ui/bundle.js.LICENSE.txt
--rw-r--r--   0        0        0      415 2023-03-29 10:24:17.367254 stackdiac-0.0.1.dev8/stackdiac/ui/index.html
--rw-r--r--   0        0        0     1699 1970-01-01 00:00:00.000000 stackdiac-0.0.1.dev8/PKG-INFO
+-rw-r--r--   0        0        0     1066 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/LICENSE
+-rw-r--r--   0        0        0      867 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/README.md
+-rw-r--r--   0        0        0      554 2023-03-30 13:17:36.204860 stackdiac-0.0.1.dev9/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/__init__.py
+-rw-r--r--   0        0        0       23 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/api/__init__.py
+-rw-r--r--   0        0        0     1179 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/api/server.py
+-rw-r--r--   0        0        0     1621 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/cli/__init__.py
+-rw-r--r--   0        0        0      729 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/cli/build.py
+-rw-r--r--   0        0        0     1594 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/cli/create.py
+-rw-r--r--   0        0        0      464 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/cli/ui.py
+-rw-r--r--   0        0        0      325 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/__init__.py
+-rw-r--r--   0        0        0     1956 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/binary.py
+-rw-r--r--   0        0        0     3295 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/cluster.py
+-rw-r--r--   0        0        0     2414 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/config.py
+-rw-r--r--   0        0        0      561 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/operation.py
+-rw-r--r--   0        0        0      161 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/provider.py
+-rw-r--r--   0        0        0     5172 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/repo.py
+-rw-r--r--   0        0        0     4995 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/models/stack.py
+-rw-r--r--   0        0        0       72 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/stackd/__init__.py
+-rw-r--r--   0        0        0      256 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/stackd/sdmod.py
+-rw-r--r--   0        0        0     6195 2023-03-30 13:17:20.472867 stackdiac-0.0.1.dev9/stackdiac/stackd/stackd.py
+-rw-r--r--   0        0        0   338889 2023-03-30 13:17:20.476867 stackdiac-0.0.1.dev9/stackdiac/ui/bundle.js
+-rw-r--r--   0        0        0     2572 2023-03-30 13:17:20.476867 stackdiac-0.0.1.dev9/stackdiac/ui/bundle.js.LICENSE.txt
+-rw-r--r--   0        0        0      415 2023-03-30 13:17:20.476867 stackdiac-0.0.1.dev9/stackdiac/ui/index.html
+-rw-r--r--   0        0        0     1699 1970-01-01 00:00:00.000000 stackdiac-0.0.1.dev9/PKG-INFO
```

### Comparing `stackdiac-0.0.1.dev8/LICENSE` & `stackdiac-0.0.1.dev9/LICENSE`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/README.md` & `stackdiac-0.0.1.dev9/README.md`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/pyproject.toml` & `stackdiac-0.0.1.dev9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "stackdiac"
-version = "0.0.1-dev8"
+version = "0.0.1-dev9"
 description = ""
 authors = ["sysr9 <38893296+sysr9@users.noreply.github.com>"]
 license = "MIT"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.10"
```

### Comparing `stackdiac-0.0.1.dev8/stackdiac/api/server.py` & `stackdiac-0.0.1.dev9/stackdiac/api/server.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/cli/__init__.py` & `stackdiac-0.0.1.dev9/stackdiac/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/cli/build.py` & `stackdiac-0.0.1.dev9/stackdiac/cli/build.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/cli/create.py` & `stackdiac-0.0.1.dev9/stackdiac/cli/create.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/models/binary.py` & `stackdiac-0.0.1.dev9/stackdiac/models/binary.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/models/cluster.py` & `stackdiac-0.0.1.dev9/stackdiac/models/cluster.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,16 @@
 from pydantic import BaseModel, parse_obj_as
 import logging
 from typing import Any
 from deepmerge import always_merger
 
 import yaml
 
+from stackdiac.models.operation import Operation
+
 from .stack import Stack
 
 logger = logging.getLogger(__name__)
 
 class ClusterStack(BaseModel):
     name: str | None = None
     src: str | None = None
@@ -63,14 +65,15 @@
         cluster.built_stacks[self.name] = self.stack
 
 class Cluster(BaseModel):
     name: str
     vars: dict[str, Any] = {}    
     stacks: dict[str, ClusterStack] = {}
     built_stacks: dict[str, Stack] = {}
+    
 
     def __init__(self, **data: Any) -> None:
         super().__init__(**data)
         for sname, s in self.stacks.items():
             # s.cluster = self
             s.name = sname
```

### Comparing `stackdiac-0.0.1.dev8/stackdiac/models/config.py` & `stackdiac-0.0.1.dev9/stackdiac/models/config.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/models/repo.py` & `stackdiac-0.0.1.dev9/stackdiac/models/repo.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/models/stack.py` & `stackdiac-0.0.1.dev9/stackdiac/models/stack.py`

 * *Files 3% similar despite different names*

```diff
@@ -2,14 +2,16 @@
 from urllib.parse import urlparse
 from pydantic import BaseModel
 from deepmerge import always_merger
 from copy import deepcopy
 import logging, os
 from typing import Any
 
+from stackdiac.models.operation import Operation
+
 logger = logging.getLogger(__name__)
 
 
 
 class Module(BaseModel):
     name: str | None = None
     source: str | None = None
@@ -127,14 +129,15 @@
          
 
 
 class Stack(BaseModel):
     name: str | None = None
     src: str | None = None
     example_vars: dict[str, Any] = {}  
+    operations: dict[str, Operation] = {}
     modules: dict[str, Module]
     vars: dict[str, Any] = {}
 
     class Config:
         orm_mode = True
         exclude = {'cluster'}
```

### Comparing `stackdiac-0.0.1.dev8/stackdiac/stackd/stackd.py` & `stackdiac-0.0.1.dev9/stackdiac/stackd/stackd.py`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/stackdiac/ui/bundle.js` & `stackdiac-0.0.1.dev9/stackdiac/ui/bundle.js`

 * *Files 1% similar despite different names*

#### js-beautify {}

```diff
@@ -13,15 +13,15 @@
                         return e
                     }, r.apply(this, arguments)
                 }
                 var a;
                 n.d(t, {
                         AV: () => B,
                         Ep: () => p,
-                        Gn: () => j,
+                        Gn: () => _,
                         J0: () => s,
                         LX: () => T,
                         PP: () => i,
                         PQ: () => V,
                         RQ: () => F,
                         WK: () => X,
                         X3: () => Q,
@@ -345,15 +345,15 @@
                     let a = w(e);
                     ! function(e) {
                         e.sort(((e, t) => e.score !== t.score ? t.score - e.score : function(e, t) {
                             return e.length === t.length && e.slice(0, -1).every(((e, n) => e === t[n])) ? e[e.length - 1] - t[t.length - 1] : 0
                         }(e.routesMeta.map((e => e.childrenIndex)), t.routesMeta.map((e => e.childrenIndex)))))
                     }(a);
                     let o = null;
-                    for (let e = 0; null == o && e < a.length; ++e) o = _(a[e], D(r));
+                    for (let e = 0; null == o && e < a.length; ++e) o = j(a[e], D(r));
                     return o
                 }
 
                 function w(e, t, n, r) {
                     void 0 === t && (t = []), void 0 === n && (n = []), void 0 === r && (r = "");
                     let a = (e, a, o) => {
                         let i = {
@@ -398,15 +398,15 @@
 
                 function N(e, t) {
                     let n = e.split("/"),
                         r = n.length;
                     return n.some(R) && (r += P), t && (r += k), n.filter((e => !R(e))).reduce(((e, t) => e + (S.test(t) ? x : "" === t ? C : O)), r)
                 }
 
-                function _(e, t) {
+                function j(e, t) {
                     let {
                         routesMeta: n
                     } = e, r = {}, a = "/", o = [];
                     for (let e = 0; e < n.length; ++e) {
                         let i = n[e],
                             l = e === n.length - 1,
                             u = "/" === a ? t : t.slice(a.length) || "/",
@@ -424,15 +424,15 @@
                             pathnameBase: U(F([a, s.pathnameBase])),
                             route: c
                         }), "/" !== s.pathnameBase && (a = F([a, s.pathnameBase]))
                     }
                     return o
                 }
 
-                function j(e, t) {
+                function _(e, t) {
                     void 0 === t && (t = {});
                     let n = e;
                     return n.endsWith("*") && "*" !== n && !n.endsWith("/*") && (c(!1, 'Route path "' + n + '" will be treated as if it were "' + n.replace(/\*$/, "/*") + '" because the `*` character must always follow a `/` in the pattern. To get rid of this warning, please change the route path to "' + n.replace(/\*$/, "/*") + '".'), n = n.replace(/\*$/, "/*")), (n.startsWith("/") ? "/" : "") + n.split(/\/+/).map(((e, n, r) => {
                         if (n === r.length - 1 && "*" === e) return t["*"];
                         const a = e.match(/^:(\w+)(\??)$/);
                         if (a) {
                             const [, e, n] = a;
@@ -731,16 +731,16 @@
                             blockers: new Map
                         },
                         C = a.Pop,
                         O = !1,
                         P = !1,
                         R = !1,
                         N = [],
-                        _ = [],
-                        j = new Map,
+                        j = [],
+                        _ = new Map,
                         T = 0,
                         D = -1,
                         L = new Map,
                         M = new Set,
                         I = new Map,
                         z = new Map,
                         F = new Map,
@@ -764,15 +764,15 @@
                             location: n,
                             initialized: !0,
                             navigation: re,
                             revalidation: "idle",
                             restoreScrollPosition: pe(n, o.matches || k.matches),
                             preventScrollReset: d,
                             blockers: new Map(k.blockers)
-                        })), P || C === a.Pop || (C === a.Push ? e.history.push(n, n.state) : C === a.Replace && e.history.replace(n, n.state)), C = a.Pop, O = !1, P = !1, R = !1, N = [], _ = []
+                        })), P || C === a.Pop || (C === a.Push ? e.history.push(n, n.state) : C === a.Replace && e.history.replace(n, n.state)), C = a.Pop, O = !1, P = !1, R = !1, N = [], j = []
                     }
                     async function B(l, u, c) {
                         S && S.abort(), S = null, C = l, P = !0 === (c && c.startUninterruptedRevalidation),
                             function(e, t) {
                                 if (f && p && h) {
                                     let n = t.map((e => De(e, k.loaderData))),
                                         r = p(e, n) || e.key;
@@ -883,15 +883,15 @@
                             let h = u || (p.formMethod && p.formAction && p.formData && p.formEncType ? {
                                     formMethod: p.formMethod,
                                     formAction: p.formAction,
                                     formData: p.formData,
                                     formEncType: p.formEncType
                                 } : void 0),
                                 m = t || i,
-                                [v, y] = de(e.history, k, o, h, a, R, N, _, I, m, e.basename, f, d);
+                                [v, y] = de(e.history, k, o, h, a, R, N, j, I, m, e.basename, f, d);
                             if (ce((e => !(o && o.some((t => t.route.id === e))) || v && v.some((t => t.route.id === e)))), 0 === v.length && 0 === y.length) return $(a, r({
                                 matches: o,
                                 loaderData: {},
                                 errors: d || null
                             }, f ? {
                                 actionData: f
                             } : {})), {
@@ -918,24 +918,24 @@
                                     actionData: null
                                 } : {
                                     actionData: e
                                 } : {}, y.length > 0 ? {
                                     fetchers: new Map(k.fetchers)
                                 } : {}))
                             }
-                            D = ++T, y.forEach((e => j.set(e.key, S)));
+                            D = ++T, y.forEach((e => _.set(e.key, S)));
                             let {
                                 results: g,
                                 loaderResults: b,
                                 fetcherResults: w
                             } = await W(k.matches, o, v, y, n);
                             if (n.signal.aborted) return {
                                 shortCircuited: !0
                             };
-                            y.forEach((e => j.delete(e.key)));
+                            y.forEach((e => _.delete(e.key)));
                             let E = ke(g);
                             if (E) return await K(k, E, {
                                 replace: c
                             }), {
                                 shortCircuited: !0
                             };
                             let {
@@ -1027,44 +1027,44 @@
                                 type: v.error,
                                 error: xe(404, {
                                     pathname: t.path
                                 })
                             }))]),
                             s = u.slice(0, a.length),
                             c = u.slice(a.length);
-                        return await Promise.all([_e(t, a, s, l.signal, !1, k.loaderData), _e(t, i.map((e => e.match)), c, l.signal, !0)]), {
+                        return await Promise.all([je(t, a, s, l.signal, !1, k.loaderData), je(t, i.map((e => e.match)), c, l.signal, !0)]), {
                             results: u,
                             loaderResults: s,
                             fetcherResults: c
                         }
                     }
 
                     function V() {
                         R = !0, N.push(...ce()), I.forEach(((e, t) => {
-                            j.has(t) && (_.push(t), X(t))
+                            _.has(t) && (j.push(t), X(t))
                         }))
                     }
 
                     function H(e, t, n) {
                         let r = Ee(k.matches, t);
                         J(e), q({
                             errors: {
                                 [r.route.id]: n
                             },
                             fetchers: new Map(k.fetchers)
                         })
                     }
 
                     function J(e) {
-                        j.has(e) && X(e), I.delete(e), L.delete(e), M.delete(e), k.fetchers.delete(e)
+                        _.has(e) && X(e), I.delete(e), L.delete(e), M.delete(e), k.fetchers.delete(e)
                     }
 
                     function X(e) {
-                        let t = j.get(e);
-                        s(t, "Expected fetch controller: " + e), t.abort(), j.delete(e)
+                        let t = _.get(e);
+                        s(t, "Expected fetch controller: " + e), t.abort(), _.delete(e)
                     }
 
                     function Y(e) {
                         for (let t of e) {
                             let e = {
                                 state: "idle",
                                 data: Q(t).data,
@@ -1237,15 +1237,15 @@
                                         blockers: new Map(k.blockers)
                                     })
                                 }
                             })
                         },
                         fetch: function(a, l, u, c) {
                             if (ue) throw new Error("router.fetch() was called during the server render, but it shouldn't be. You are likely calling a useFetcher() method in the body of your component. Try moving it to a useEffect or a callback.");
-                            j.has(a) && X(a);
+                            _.has(a) && X(a);
                             let f = b(t || i, u, e.basename);
                             if (!f) return void H(a, l, xe(404, {
                                 pathname: u
                             }));
                             let {
                                 path: d,
                                 submission: p
@@ -1267,19 +1267,19 @@
                                         " _hasFetcherDoneAnything ": !0
                                     });
                                 k.fetchers.set(a, h), q({
                                     fetchers: new Map(k.fetchers)
                                 });
                                 let m = new AbortController,
                                     v = ye(e.history, u, m.signal, d);
-                                j.set(a, m);
+                                _.set(a, m);
                                 let y = await ve("action", v, c, f, o, n, E.basename);
-                                if (v.signal.aborted) return void(j.get(a) === m && j.delete(a));
+                                if (v.signal.aborted) return void(_.get(a) === m && _.delete(a));
                                 if (Re(y)) {
-                                    j.delete(a), M.add(a);
+                                    _.delete(a), M.add(a);
                                     let e = r({
                                         state: "loading"
                                     }, d, {
                                         data: void 0,
                                         " _hasFetcherDoneAnything ": !0
                                     });
                                     return k.fetchers.set(a, e), q({
@@ -1302,40 +1302,40 @@
                                 let A = r({
                                     state: "loading",
                                     data: y.data
                                 }, d, {
                                     " _hasFetcherDoneAnything ": !0
                                 });
                                 k.fetchers.set(a, A);
-                                let [F, U] = de(e.history, k, O, d, g, R, N, _, I, x, e.basename, {
+                                let [F, U] = de(e.history, k, O, d, g, R, N, j, I, x, e.basename, {
                                     [c.route.id]: y.data
                                 }, void 0);
                                 U.filter((e => e.key !== a)).forEach((e => {
                                     let t = e.key,
                                         n = k.fetchers.get(t),
                                         r = {
                                             state: "loading",
                                             data: n && n.data,
                                             formMethod: void 0,
                                             formAction: void 0,
                                             formEncType: void 0,
                                             formData: void 0,
                                             " _hasFetcherDoneAnything ": !0
                                         };
-                                    k.fetchers.set(t, r), j.set(t, m)
+                                    k.fetchers.set(t, r), _.set(t, m)
                                 })), q({
                                     fetchers: new Map(k.fetchers)
                                 });
                                 let {
                                     results: B,
                                     loaderResults: Q,
                                     fetcherResults: J
                                 } = await W(k.matches, O, F, U, w);
                                 if (m.signal.aborted) return;
-                                L.delete(a), j.delete(a), U.forEach((e => j.delete(e.key)));
+                                L.delete(a), _.delete(a), U.forEach((e => _.delete(e.key)));
                                 let X = ke(B);
                                 if (X) return K(k, X);
                                 let {
                                     loaderData: Y,
                                     errors: Z
                                 } = be(k, k.matches, F, Q, void 0, U, J, z), ee = {
                                     state: "idle",
@@ -1375,17 +1375,17 @@
                                         " _hasFetcherDoneAnything ": !0
                                     });
                                 k.fetchers.set(t, d), q({
                                     fetchers: new Map(k.fetchers)
                                 });
                                 let p = new AbortController,
                                     h = ye(e.history, i, p.signal);
-                                j.set(t, p);
+                                _.set(t, p);
                                 let m = await ve("loader", h, l, u, o, n, E.basename);
-                                if (Oe(m) && (m = await je(m, h.signal, !0) || m), j.get(t) === p && j.delete(t), h.signal.aborted) return;
+                                if (Oe(m) && (m = await _e(m, h.signal, !0) || m), _.get(t) === p && _.delete(t), h.signal.aborted) return;
                                 if (Re(m)) return void await K(k, m);
                                 if (Pe(m)) {
                                     let e = Ee(k.matches, a);
                                     return k.fetchers.delete(t), void q({
                                         fetchers: new Map(k.fetchers),
                                         errors: {
                                             [e.route.id]: m.error
@@ -1424,15 +1424,15 @@
                             l && l(), u.clear(), S && S.abort(), k.fetchers.forEach(((e, t) => J(t))), k.blockers.forEach(((e, t) => Z(t)))
                         },
                         getBlocker: function(e, t) {
                             let n = k.blockers.get(e) || oe;
                             return F.get(e) !== t && F.set(e, t), n
                         },
                         deleteBlocker: Z,
-                        _internalFetchControllers: j,
+                        _internalFetchControllers: _,
                         _internalActiveDeferreds: z,
                         _internalSetRoutes: function(e) {
                             t = e
                         }
                     }, E
                 }
 
@@ -1790,27 +1790,27 @@
                 function Re(e) {
                     return (e && e.type) === v.redirect
                 }
 
                 function Ne(e) {
                     return G.has(e)
                 }
-                async function _e(e, t, n, r, a, o) {
+                async function je(e, t, n, r, a, o) {
                     for (let i = 0; i < n.length; i++) {
                         let l = n[i],
                             u = t[i];
                         if (!u) continue;
                         let s = e.find((e => e.route.id === u.route.id)),
                             c = null != s && !pe(s, u) && void 0 !== (o && o[u.route.id]);
-                        Oe(l) && (a || c) && await je(l, r, a).then((e => {
+                        Oe(l) && (a || c) && await _e(l, r, a).then((e => {
                             e && (n[i] = e || n[i])
                         }))
                     }
                 }
-                async function je(e, t, n) {
+                async function _e(e, t, n) {
                     if (void 0 === n && (n = !1), !await e.deferredData.resolveData(t)) {
                         if (n) try {
                             return {
                                 type: v.data,
                                 data: e.deferredData.unwrappedData
                             }
                         } catch (e) {
@@ -2176,16 +2176,16 @@
                     x = Symbol.for("react.fragment"),
                     k = Symbol.for("react.strict_mode"),
                     C = Symbol.for("react.profiler"),
                     O = Symbol.for("react.provider"),
                     P = Symbol.for("react.context"),
                     R = Symbol.for("react.forward_ref"),
                     N = Symbol.for("react.suspense"),
-                    _ = Symbol.for("react.suspense_list"),
-                    j = Symbol.for("react.memo"),
+                    j = Symbol.for("react.suspense_list"),
+                    _ = Symbol.for("react.memo"),
                     T = Symbol.for("react.lazy");
                 Symbol.for("react.scope"), Symbol.for("react.debug_trace_mode");
                 var D = Symbol.for("react.offscreen");
                 Symbol.for("react.legacy_hidden"), Symbol.for("react.cache"), Symbol.for("react.tracing_marker");
                 var A = Symbol.iterator;
 
                 function L(e) {
@@ -2295,26 +2295,26 @@
                             return "Portal";
                         case C:
                             return "Profiler";
                         case k:
                             return "StrictMode";
                         case N:
                             return "Suspense";
-                        case _:
+                        case j:
                             return "SuspenseList"
                     }
                     if ("object" == typeof e) switch (e.$$typeof) {
                         case P:
                             return (e.displayName || "Context") + ".Consumer";
                         case O:
                             return (e._context.displayName || "Context") + ".Provider";
                         case R:
                             var t = e.render;
                             return (e = e.displayName) || (e = "" !== (e = t.displayName || t.name || "") ? "ForwardRef(" + e + ")" : "ForwardRef"), e;
-                        case j:
+                        case _:
                             return null !== (t = e.displayName || null) ? t : $(e.type) || "Memo";
                         case T:
                             t = e._payload, e = e._init;
                             try {
                                 return $(e(t))
                             } catch (e) {}
                     }
@@ -2715,23 +2715,23 @@
                 }
 
                 function Re(e, t) {
                     return e(t)
                 }
 
                 function Ne() {}
-                var _e = !1;
+                var je = !1;
 
-                function je(e, t, n) {
-                    if (_e) return e(t, n);
-                    _e = !0;
+                function _e(e, t, n) {
+                    if (je) return e(t, n);
+                    je = !0;
                     try {
                         return Re(e, t, n)
                     } finally {
-                        _e = !1, (null !== xe || null !== ke) && (Ne(), Pe())
+                        je = !1, (null !== xe || null !== ke) && (Ne(), Pe())
                     }
                 }
 
                 function Te(e, t) {
                     var n = e.stateNode;
                     if (null === n) return null;
                     var r = Ea(n);
@@ -3039,16 +3039,16 @@
                 function wt(e) {
                     return 1 < (e &= -e) ? 4 < e ? 0 != (268435455 & e) ? 16 : 536870912 : 4 : 1
                 }
                 var Et, St, xt, kt, Ct, Ot = !1,
                     Pt = [],
                     Rt = null,
                     Nt = null,
-                    _t = null,
-                    jt = new Map,
+                    jt = null,
+                    _t = new Map,
                     Tt = new Map,
                     Dt = [],
                     At = "mousedown mouseup touchcancel touchend touchstart auxclick dblclick pointercancel pointerdown pointerup dragend dragstart drop compositionend compositionstart keydown keypress keyup input textInput copy cut paste click change contextmenu reset submit".split(" ");
 
                 function Lt(e, t) {
                     switch (e) {
                         case "focusin":
@@ -3057,19 +3057,19 @@
                             break;
                         case "dragenter":
                         case "dragleave":
                             Nt = null;
                             break;
                         case "mouseover":
                         case "mouseout":
-                            _t = null;
+                            jt = null;
                             break;
                         case "pointerover":
                         case "pointerout":
-                            jt.delete(t.pointerId);
+                            _t.delete(t.pointerId);
                             break;
                         case "gotpointercapture":
                         case "lostpointercapture":
                             Tt.delete(t.pointerId)
                     }
                 }
 
@@ -3109,15 +3109,15 @@
                 }
 
                 function Ft(e, t, n) {
                     zt(e) && n.delete(t)
                 }
 
                 function Ut() {
-                    Ot = !1, null !== Rt && zt(Rt) && (Rt = null), null !== Nt && zt(Nt) && (Nt = null), null !== _t && zt(_t) && (_t = null), jt.forEach(Ft), Tt.forEach(Ft)
+                    Ot = !1, null !== Rt && zt(Rt) && (Rt = null), null !== Nt && zt(Nt) && (Nt = null), null !== jt && zt(jt) && (jt = null), _t.forEach(Ft), Tt.forEach(Ft)
                 }
 
                 function qt(e, t) {
                     e.blockedOn === t && (e.blockedOn = null, Ot || (Ot = !0, a.unstable_scheduleCallback(a.unstable_NormalPriority, Ut)))
                 }
 
                 function $t(e) {
@@ -3127,15 +3127,15 @@
                     if (0 < Pt.length) {
                         qt(Pt[0], e);
                         for (var n = 1; n < Pt.length; n++) {
                             var r = Pt[n];
                             r.blockedOn === e && (r.blockedOn = null)
                         }
                     }
-                    for (null !== Rt && qt(Rt, e), null !== Nt && qt(Nt, e), null !== _t && qt(_t, e), jt.forEach(t), Tt.forEach(t), n = 0; n < Dt.length; n++)(r = Dt[n]).blockedOn === e && (r.blockedOn = null);
+                    for (null !== Rt && qt(Rt, e), null !== Nt && qt(Nt, e), null !== jt && qt(jt, e), _t.forEach(t), Tt.forEach(t), n = 0; n < Dt.length; n++)(r = Dt[n]).blockedOn === e && (r.blockedOn = null);
                     for (; 0 < Dt.length && null === (n = Dt[0]).blockedOn;) It(n), null === n.blockedOn && Dt.shift()
                 }
                 var Bt = w.ReactCurrentBatchConfig,
                     Qt = !0;
 
                 function Kt(e, t, n, r) {
                     var a = bt,
@@ -3166,18 +3166,18 @@
                         else if (function(e, t, n, r, a) {
                                 switch (t) {
                                     case "focusin":
                                         return Rt = Mt(Rt, e, t, n, r, a), !0;
                                     case "dragenter":
                                         return Nt = Mt(Nt, e, t, n, r, a), !0;
                                     case "mouseover":
-                                        return _t = Mt(_t, e, t, n, r, a), !0;
+                                        return jt = Mt(jt, e, t, n, r, a), !0;
                                     case "pointerover":
                                         var o = a.pointerId;
-                                        return jt.set(o, Mt(jt.get(o) || null, e, t, n, r, a)), !0;
+                                        return _t.set(o, Mt(_t.get(o) || null, e, t, n, r, a)), !0;
                                     case "gotpointercapture":
                                         return o = a.pointerId, Tt.set(o, Mt(Tt.get(o) || null, e, t, n, r, a)), !0
                                 }
                                 return !1
                             }(a, e, t, n, r)) r.stopPropagation();
                         else if (Lt(e, r), 4 & t && -1 < At.indexOf(e)) {
                             for (; null !== a;) {
@@ -3518,30 +3518,30 @@
                         changedTouches: 0,
                         altKey: 0,
                         metaKey: 0,
                         ctrlKey: 0,
                         shiftKey: 0,
                         getModifierState: Cn
                     })),
-                    _n = an(I({}, sn, {
+                    jn = an(I({}, sn, {
                         propertyName: 0,
                         elapsedTime: 0,
                         pseudoElement: 0
                     })),
-                    jn = I({}, pn, {
+                    _n = I({}, pn, {
                         deltaX: function(e) {
                             return "deltaX" in e ? e.deltaX : "wheelDeltaX" in e ? -e.wheelDeltaX : 0
                         },
                         deltaY: function(e) {
                             return "deltaY" in e ? e.deltaY : "wheelDeltaY" in e ? -e.wheelDeltaY : "wheelDelta" in e ? -e.wheelDelta : 0
                         },
                         deltaZ: 0,
                         deltaMode: 0
                     }),
-                    Tn = an(jn),
+                    Tn = an(_n),
                     Dn = [9, 13, 27, 32],
                     An = c && "CompositionEvent" in window,
                     Ln = null;
                 c && "documentMode" in document && (Ln = document.documentMode);
                 var Mn = c && "TextEvent" in window && !Ln,
                     In = c && (!An || Ln && 8 < Ln && 11 >= Ln),
                     zn = String.fromCharCode(32),
@@ -3626,15 +3626,15 @@
                 function tr() {
                     Wn && (Wn.detachEvent("onpropertychange", nr), Vn = Wn = null)
                 }
 
                 function nr(e) {
                     if ("value" === e.propertyName && Jn(Vn)) {
                         var t = [];
-                        Kn(t, Vn, e, Ee(e)), je(Hn, t)
+                        Kn(t, Vn, e, Ee(e)), _e(Hn, t)
                     }
                 }
 
                 function rr(e, t, n) {
                     "focusin" === e ? (tr(), Vn = n, (Wn = t).attachEvent("onpropertychange", nr)) : "focusout" === e && tr()
                 }
 
@@ -3784,22 +3784,22 @@
                     return e
                 }
                 c && (kr = document.createElement("div").style, "AnimationEvent" in window || (delete Sr.animationend.animation, delete Sr.animationiteration.animation, delete Sr.animationstart.animation), "TransitionEvent" in window || delete Sr.transitionend.transition);
                 var Or = Cr("animationend"),
                     Pr = Cr("animationiteration"),
                     Rr = Cr("animationstart"),
                     Nr = Cr("transitionend"),
-                    _r = new Map,
-                    jr = "abort auxClick cancel canPlay canPlayThrough click close contextMenu copy cut drag dragEnd dragEnter dragExit dragLeave dragOver dragStart drop durationChange emptied encrypted ended error gotPointerCapture input invalid keyDown keyPress keyUp load loadedData loadedMetadata loadStart lostPointerCapture mouseDown mouseMove mouseOut mouseOver mouseUp paste pause play playing pointerCancel pointerDown pointerMove pointerOut pointerOver pointerUp progress rateChange reset resize seeked seeking stalled submit suspend timeUpdate touchCancel touchEnd touchStart volumeChange scroll toggle touchMove waiting wheel".split(" ");
+                    jr = new Map,
+                    _r = "abort auxClick cancel canPlay canPlayThrough click close contextMenu copy cut drag dragEnd dragEnter dragExit dragLeave dragOver dragStart drop durationChange emptied encrypted ended error gotPointerCapture input invalid keyDown keyPress keyUp load loadedData loadedMetadata loadStart lostPointerCapture mouseDown mouseMove mouseOut mouseOver mouseUp paste pause play playing pointerCancel pointerDown pointerMove pointerOut pointerOver pointerUp progress rateChange reset resize seeked seeking stalled submit suspend timeUpdate touchCancel touchEnd touchStart volumeChange scroll toggle touchMove waiting wheel".split(" ");
 
                 function Tr(e, t) {
-                    _r.set(e, t), u(t, [e])
+                    jr.set(e, t), u(t, [e])
                 }
-                for (var Dr = 0; Dr < jr.length; Dr++) {
-                    var Ar = jr[Dr];
+                for (var Dr = 0; Dr < _r.length; Dr++) {
+                    var Ar = _r[Dr];
                     Tr(Ar.toLowerCase(), "on" + (Ar[0].toUpperCase() + Ar.slice(1)))
                 }
                 Tr(Or, "onAnimationEnd"), Tr(Pr, "onAnimationIteration"), Tr(Rr, "onAnimationStart"), Tr("dblclick", "onDoubleClick"), Tr("focusin", "onFocus"), Tr("focusout", "onBlur"), Tr(Nr, "onTransitionEnd"), s("onMouseEnter", ["mouseout", "mouseover"]), s("onMouseLeave", ["mouseout", "mouseover"]), s("onPointerEnter", ["pointerout", "pointerover"]), s("onPointerLeave", ["pointerout", "pointerover"]), u("onChange", "change click focusin focusout input keydown keyup selectionchange".split(" ")), u("onSelect", "focusout contextmenu dragend focusin keydown keyup mousedown mouseup selectionchange".split(" ")), u("onBeforeInput", ["compositionend", "keypress", "textInput", "paste"]), u("onCompositionEnd", "compositionend focusout keydown keypress keyup mousedown".split(" ")), u("onCompositionStart", "compositionstart focusout keydown keypress keyup mousedown".split(" ")), u("onCompositionUpdate", "compositionupdate focusout keydown keypress keyup mousedown".split(" "));
                 var Lr = "abort canplay canplaythrough durationchange emptied encrypted ended error loadeddata loadedmetadata loadstart pause play playing progress ratechange resize seeked seeking stalled suspend timeupdate volumechange waiting".split(" "),
                     Mr = new Set("cancel close invalid load scroll toggle".split(" ").concat(Lr));
 
                 function Ir(e, t, n) {
@@ -3902,20 +3902,20 @@
                                     continue e
                                 }
                                 l = l.parentNode
                             }
                         }
                         r = r.return
                     }
-                    je((function() {
+                    _e((function() {
                         var r = o,
                             a = Ee(n),
                             i = [];
                         e: {
-                            var l = _r.get(e);
+                            var l = jr.get(e);
                             if (void 0 !== l) {
                                 var u = cn,
                                     s = e;
                                 switch (e) {
                                     case "keypress":
                                         if (0 === tn(n)) break e;
                                     case "keydown":
@@ -3962,15 +3962,15 @@
                                         break;
                                     case Or:
                                     case Pr:
                                     case Rr:
                                         u = yn;
                                         break;
                                     case Nr:
-                                        u = _n;
+                                        u = jn;
                                         break;
                                     case "scroll":
                                         u = dn;
                                         break;
                                     case "wheel":
                                         u = Tn;
                                         break;
@@ -4267,17 +4267,17 @@
 
                 function Oa(e, t) {
                     xa++, Sa[xa] = e.current, e.current = t
                 }
                 var Pa = {},
                     Ra = ka(Pa),
                     Na = ka(!1),
-                    _a = Pa;
+                    ja = Pa;
 
-                function ja(e, t) {
+                function _a(e, t) {
                     var n = e.type.contextTypes;
                     if (!n) return Pa;
                     var r = e.stateNode;
                     if (r && r.__reactInternalMemoizedUnmaskedChildContext === t) return r.__reactInternalMemoizedMaskedChildContext;
                     var a, o = {};
                     for (a in n) o[a] = t[a];
                     return r && ((e = e.stateNode).__reactInternalMemoizedUnmaskedChildContext = t, e.__reactInternalMemoizedMaskedChildContext = o), o
@@ -4301,21 +4301,21 @@
                     if (t = t.childContextTypes, "function" != typeof r.getChildContext) return n;
                     for (var a in r = r.getChildContext())
                         if (!(a in t)) throw Error(o(108, B(e) || "Unknown", a));
                     return I({}, n, r)
                 }
 
                 function Ma(e) {
-                    return e = (e = e.stateNode) && e.__reactInternalMemoizedMergedChildContext || Pa, _a = Ra.current, Oa(Ra, e), Oa(Na, Na.current), !0
+                    return e = (e = e.stateNode) && e.__reactInternalMemoizedMergedChildContext || Pa, ja = Ra.current, Oa(Ra, e), Oa(Na, Na.current), !0
                 }
 
                 function Ia(e, t, n) {
                     var r = e.stateNode;
                     if (!r) throw Error(o(169));
-                    n ? (e = La(e, t, _a), r.__reactInternalMemoizedMergedChildContext = e, Ca(Na), Ca(Ra), Oa(Ra, e)) : Ca(Na), Oa(Na, n)
+                    n ? (e = La(e, t, ja), r.__reactInternalMemoizedMergedChildContext = e, Ca(Na), Ca(Ra), Oa(Ra, e)) : Ca(Na), Oa(Na, n)
                 }
                 var za = null,
                     Fa = !1,
                     Ua = !1;
 
                 function qa(e) {
                     null === za ? za = [e] : za.push(e)
@@ -4532,24 +4532,24 @@
 
                 function Ro(e) {
                     null === Po ? Po = [e] : Po.push(e)
                 }
 
                 function No(e, t, n, r) {
                     var a = t.interleaved;
-                    return null === a ? (n.next = n, Ro(t)) : (n.next = a.next, a.next = n), t.interleaved = n, _o(e, r)
+                    return null === a ? (n.next = n, Ro(t)) : (n.next = a.next, a.next = n), t.interleaved = n, jo(e, r)
                 }
 
-                function _o(e, t) {
+                function jo(e, t) {
                     e.lanes |= t;
                     var n = e.alternate;
                     for (null !== n && (n.lanes |= t), n = e, e = e.return; null !== e;) e.childLanes |= t, null !== (n = e.alternate) && (n.childLanes |= t), n = e, e = e.return;
                     return 3 === n.tag ? n.stateNode : null
                 }
-                var jo = !1;
+                var _o = !1;
 
                 function To(e) {
                     e.updateQueue = {
                         baseState: e.memoizedState,
                         firstBaseUpdate: null,
                         lastBaseUpdate: null,
                         shared: {
@@ -4583,17 +4583,17 @@
                 }
 
                 function Lo(e, t, n) {
                     var r = e.updateQueue;
                     if (null === r) return null;
                     if (r = r.shared, 0 != (2 & Nu)) {
                         var a = r.pending;
-                        return null === a ? t.next = t : (t.next = a.next, a.next = t), r.pending = t, _o(e, n)
+                        return null === a ? t.next = t : (t.next = a.next, a.next = t), r.pending = t, jo(e, n)
                     }
-                    return null === (a = r.interleaved) ? (t.next = t, Ro(r)) : (t.next = a.next, a.next = t), r.interleaved = t, _o(e, n)
+                    return null === (a = r.interleaved) ? (t.next = t, Ro(r)) : (t.next = a.next, a.next = t), r.interleaved = t, jo(e, n)
                 }
 
                 function Mo(e, t, n) {
                     if (null !== (t = t.updateQueue) && (t = t.shared, 0 != (4194240 & n))) {
                         var r = t.lanes;
                         n |= r &= e.pendingLanes, t.lanes = n, gt(e, n)
                     }
@@ -4628,15 +4628,15 @@
                         }, void(e.updateQueue = n)
                     }
                     null === (e = n.lastBaseUpdate) ? n.firstBaseUpdate = t : e.next = t, n.lastBaseUpdate = t
                 }
 
                 function zo(e, t, n, r) {
                     var a = e.updateQueue;
-                    jo = !1;
+                    _o = !1;
                     var o = a.firstBaseUpdate,
                         i = a.lastBaseUpdate,
                         l = a.shared.pending;
                     if (null !== l) {
                         a.shared.pending = null;
                         var u = l,
                             s = u.next;
@@ -4672,15 +4672,15 @@
                                         case 3:
                                             h.flags = -65537 & h.flags | 128;
                                         case 0:
                                             if (null == (d = "function" == typeof(h = m.payload) ? h.call(p, f, d) : h)) break e;
                                             f = I({}, f, d);
                                             break e;
                                         case 2:
-                                            jo = !0
+                                            _o = !0
                                     }
                                 }
                                 null !== l.callback && 0 !== l.lane && (e.flags |= 64, null === (d = a.effects) ? a.effects = [l] : d.push(l))
                             } else p = {
                                 eventTime: p,
                                 lane: d,
                                 tag: l.tag,
@@ -4750,26 +4750,26 @@
                     return "function" == typeof(e = e.stateNode).shouldComponentUpdate ? e.shouldComponentUpdate(r, o, i) : !(t.prototype && t.prototype.isPureReactComponent && ur(n, r) && ur(a, o))
                 }
 
                 function Qo(e, t, n) {
                     var r = !1,
                         a = Pa,
                         o = t.contextType;
-                    return "object" == typeof o && null !== o ? o = Oo(o) : (a = Ta(t) ? _a : Ra.current, o = (r = null != (r = t.contextTypes)) ? ja(e, a) : Pa), t = new t(n, o), e.memoizedState = null !== t.state && void 0 !== t.state ? t.state : null, t.updater = $o, e.stateNode = t, t._reactInternals = e, r && ((e = e.stateNode).__reactInternalMemoizedUnmaskedChildContext = a, e.__reactInternalMemoizedMaskedChildContext = o), t
+                    return "object" == typeof o && null !== o ? o = Oo(o) : (a = Ta(t) ? ja : Ra.current, o = (r = null != (r = t.contextTypes)) ? _a(e, a) : Pa), t = new t(n, o), e.memoizedState = null !== t.state && void 0 !== t.state ? t.state : null, t.updater = $o, e.stateNode = t, t._reactInternals = e, r && ((e = e.stateNode).__reactInternalMemoizedUnmaskedChildContext = a, e.__reactInternalMemoizedMaskedChildContext = o), t
                 }
 
                 function Ko(e, t, n, r) {
                     e = t.state, "function" == typeof t.componentWillReceiveProps && t.componentWillReceiveProps(n, r), "function" == typeof t.UNSAFE_componentWillReceiveProps && t.UNSAFE_componentWillReceiveProps(n, r), t.state !== e && $o.enqueueReplaceState(t, t.state, null)
                 }
 
                 function Wo(e, t, n, r) {
                     var a = e.stateNode;
                     a.props = n, a.state = e.memoizedState, a.refs = Uo, To(e);
                     var o = t.contextType;
-                    "object" == typeof o && null !== o ? a.context = Oo(o) : (o = Ta(t) ? _a : Ra.current, a.context = ja(e, o)), a.state = e.memoizedState, "function" == typeof(o = t.getDerivedStateFromProps) && (qo(e, t, o, n), a.state = e.memoizedState), "function" == typeof t.getDerivedStateFromProps || "function" == typeof a.getSnapshotBeforeUpdate || "function" != typeof a.UNSAFE_componentWillMount && "function" != typeof a.componentWillMount || (t = a.state, "function" == typeof a.componentWillMount && a.componentWillMount(), "function" == typeof a.UNSAFE_componentWillMount && a.UNSAFE_componentWillMount(), t !== a.state && $o.enqueueReplaceState(a, a.state, null), zo(e, n, a, r), a.state = e.memoizedState), "function" == typeof a.componentDidMount && (e.flags |= 4194308)
+                    "object" == typeof o && null !== o ? a.context = Oo(o) : (o = Ta(t) ? ja : Ra.current, a.context = _a(e, o)), a.state = e.memoizedState, "function" == typeof(o = t.getDerivedStateFromProps) && (qo(e, t, o, n), a.state = e.memoizedState), "function" == typeof t.getDerivedStateFromProps || "function" == typeof a.getSnapshotBeforeUpdate || "function" != typeof a.UNSAFE_componentWillMount && "function" != typeof a.componentWillMount || (t = a.state, "function" == typeof a.componentWillMount && a.componentWillMount(), "function" == typeof a.UNSAFE_componentWillMount && a.UNSAFE_componentWillMount(), t !== a.state && $o.enqueueReplaceState(a, a.state, null), zo(e, n, a, r), a.state = e.memoizedState), "function" == typeof a.componentDidMount && (e.flags |= 4194308)
                 }
 
                 function Vo(e, t, n) {
                     if (null !== (e = n.ref) && "function" != typeof e && "object" != typeof e) {
                         if (n._owner) {
                             if (n = n._owner) {
                                 if (1 !== n.tag) throw Error(o(309));
@@ -5179,15 +5179,15 @@
                         do {
                             i = a.lane, mi.lanes |= i, Iu |= i, a = a.next
                         } while (a !== e)
                     } else null === a && (n.lanes = 0);
                     return [t.memoizedState, n.dispatch]
                 }
 
-                function _i(e) {
+                function ji(e) {
                     var t = Pi(),
                         n = t.queue;
                     if (null === n) throw Error(o(311));
                     n.lastRenderedReducer = e;
                     var r = n.dispatch,
                         a = n.pending,
                         i = t.memoizedState;
@@ -5198,23 +5198,23 @@
                             i = e(i, l.action), l = l.next
                         } while (l !== a);
                         lr(i, t.memoizedState) || (wl = !0), t.memoizedState = i, null === t.baseQueue && (t.baseState = i), n.lastRenderedState = i
                     }
                     return [i, r]
                 }
 
-                function ji() {}
+                function _i() {}
 
                 function Ti(e, t) {
                     var n = mi,
                         r = Pi(),
                         a = t(),
                         i = !lr(r.memoizedState, a);
                     if (i && (r.memoizedState = a, wl = !0), r = r.queue, Qi(Li.bind(null, n, r, e), [e]), r.getSnapshot !== t || i || null !== yi && 1 & yi.memoizedState.tag) {
-                        if (n.flags |= 2048, Fi(9, Ai.bind(null, n, r, a, t), void 0, null), null === _u) throw Error(o(349));
+                        if (n.flags |= 2048, Fi(9, Ai.bind(null, n, r, a, t), void 0, null), null === ju) throw Error(o(349));
                         0 != (30 & hi) || Di(n, t, a)
                     }
                     return a
                 }
 
                 function Di(e, t, n) {
                     e.flags |= 16384, e = {
@@ -5244,15 +5244,15 @@
                         return !lr(e, n)
                     } catch (e) {
                         return !0
                     }
                 }
 
                 function Ii(e) {
-                    var t = _o(e, 1);
+                    var t = jo(e, 1);
                     null !== t && rs(t, e, 1, -1)
                 }
 
                 function zi(e) {
                     var t = Oi();
                     return "function" == typeof e && (e = e()), t.memoizedState = t.baseState = e, e = {
                         pending: null,
@@ -5483,27 +5483,27 @@
                         useSyncExternalStore: function(e, t, n) {
                             var r = mi,
                                 a = Oi();
                             if (ao) {
                                 if (void 0 === n) throw Error(o(407));
                                 n = n()
                             } else {
-                                if (n = t(), null === _u) throw Error(o(349));
+                                if (n = t(), null === ju) throw Error(o(349));
                                 0 != (30 & hi) || Di(r, t, n)
                             }
                             a.memoizedState = n;
                             var i = {
                                 value: n,
                                 getSnapshot: t
                             };
                             return a.queue = i, Bi(Li.bind(null, r, i, e), [e]), r.flags |= 2048, Fi(9, Ai.bind(null, r, i, n, t), void 0, null), n
                         },
                         useId: function() {
                             var e = Oi(),
-                                t = _u.identifierPrefix;
+                                t = ju.identifierPrefix;
                             if (ao) {
                                 var n = Ya;
                                 t = ":" + t + "R" + (n = (Xa & ~(1 << 32 - it(Xa) - 1)).toString(32) + n), 0 < (n = wi++) && (t += "H" + n.toString(32)), t += ":"
                             } else t = ":" + t + "r" + (n = Ei++).toString(32) + ":";
                             return e.memoizedState = t
                         },
                         unstable_isNewReconciler: !1
@@ -5525,42 +5525,42 @@
                         useDebugValue: Ji,
                         useDeferredValue: function(e) {
                             return Gi(Pi(), vi.memoizedState, e)
                         },
                         useTransition: function() {
                             return [Ni(Ri)[0], Pi().memoizedState]
                         },
-                        useMutableSource: ji,
+                        useMutableSource: _i,
                         useSyncExternalStore: Ti,
                         useId: el,
                         unstable_isNewReconciler: !1
                     },
                     sl = {
                         readContext: Oo,
                         useCallback: Xi,
                         useContext: Oo,
                         useEffect: Qi,
                         useImperativeHandle: Hi,
                         useInsertionEffect: Ki,
                         useLayoutEffect: Wi,
                         useMemo: Yi,
-                        useReducer: _i,
+                        useReducer: ji,
                         useRef: Ui,
                         useState: function() {
-                            return _i(Ri)
+                            return ji(Ri)
                         },
                         useDebugValue: Ji,
                         useDeferredValue: function(e) {
                             var t = Pi();
                             return null === vi ? t.memoizedState = e : Gi(t, vi.memoizedState, e)
                         },
                         useTransition: function() {
-                            return [_i(Ri)[0], Pi().memoizedState]
+                            return [ji(Ri)[0], Pi().memoizedState]
                         },
-                        useMutableSource: ji,
+                        useMutableSource: _i,
                         useSyncExternalStore: Ti,
                         useId: el,
                         unstable_isNewReconciler: !1
                     };
 
                 function cl(e, t) {
                     try {
@@ -5718,61 +5718,61 @@
 
                 function Ol(e, t) {
                     var n = t.ref;
                     (null === e && null !== n || null !== e && e.ref !== n) && (t.flags |= 512, t.flags |= 2097152)
                 }
 
                 function Pl(e, t, n, r, a) {
-                    var o = Ta(n) ? _a : Ra.current;
-                    return o = ja(t, o), Co(t, a), n = ki(e, t, n, r, o, a), r = Ci(), null === e || wl ? (ao && r && eo(t), t.flags |= 1, El(e, t, n, a), t.child) : (t.updateQueue = e.updateQueue, t.flags &= -2053, e.lanes &= ~a, Kl(e, t, a))
+                    var o = Ta(n) ? ja : Ra.current;
+                    return o = _a(t, o), Co(t, a), n = ki(e, t, n, r, o, a), r = Ci(), null === e || wl ? (ao && r && eo(t), t.flags |= 1, El(e, t, n, a), t.child) : (t.updateQueue = e.updateQueue, t.flags &= -2053, e.lanes &= ~a, Kl(e, t, a))
                 }
 
                 function Rl(e, t, n, r, a) {
                     if (Ta(n)) {
                         var o = !0;
                         Ma(t)
                     } else o = !1;
                     if (Co(t, a), null === t.stateNode) Ql(e, t), Qo(t, n, r), Wo(t, n, r, a), r = !0;
                     else if (null === e) {
                         var i = t.stateNode,
                             l = t.memoizedProps;
                         i.props = l;
                         var u = i.context,
                             s = n.contextType;
-                        s = "object" == typeof s && null !== s ? Oo(s) : ja(t, s = Ta(n) ? _a : Ra.current);
+                        s = "object" == typeof s && null !== s ? Oo(s) : _a(t, s = Ta(n) ? ja : Ra.current);
                         var c = n.getDerivedStateFromProps,
                             f = "function" == typeof c || "function" == typeof i.getSnapshotBeforeUpdate;
-                        f || "function" != typeof i.UNSAFE_componentWillReceiveProps && "function" != typeof i.componentWillReceiveProps || (l !== r || u !== s) && Ko(t, i, r, s), jo = !1;
+                        f || "function" != typeof i.UNSAFE_componentWillReceiveProps && "function" != typeof i.componentWillReceiveProps || (l !== r || u !== s) && Ko(t, i, r, s), _o = !1;
                         var d = t.memoizedState;
-                        i.state = d, zo(t, r, i, a), u = t.memoizedState, l !== r || d !== u || Na.current || jo ? ("function" == typeof c && (qo(t, n, c, r), u = t.memoizedState), (l = jo || Bo(t, n, l, r, d, u, s)) ? (f || "function" != typeof i.UNSAFE_componentWillMount && "function" != typeof i.componentWillMount || ("function" == typeof i.componentWillMount && i.componentWillMount(), "function" == typeof i.UNSAFE_componentWillMount && i.UNSAFE_componentWillMount()), "function" == typeof i.componentDidMount && (t.flags |= 4194308)) : ("function" == typeof i.componentDidMount && (t.flags |= 4194308), t.memoizedProps = r, t.memoizedState = u), i.props = r, i.state = u, i.context = s, r = l) : ("function" == typeof i.componentDidMount && (t.flags |= 4194308), r = !1)
+                        i.state = d, zo(t, r, i, a), u = t.memoizedState, l !== r || d !== u || Na.current || _o ? ("function" == typeof c && (qo(t, n, c, r), u = t.memoizedState), (l = _o || Bo(t, n, l, r, d, u, s)) ? (f || "function" != typeof i.UNSAFE_componentWillMount && "function" != typeof i.componentWillMount || ("function" == typeof i.componentWillMount && i.componentWillMount(), "function" == typeof i.UNSAFE_componentWillMount && i.UNSAFE_componentWillMount()), "function" == typeof i.componentDidMount && (t.flags |= 4194308)) : ("function" == typeof i.componentDidMount && (t.flags |= 4194308), t.memoizedProps = r, t.memoizedState = u), i.props = r, i.state = u, i.context = s, r = l) : ("function" == typeof i.componentDidMount && (t.flags |= 4194308), r = !1)
                     } else {
-                        i = t.stateNode, Do(e, t), l = t.memoizedProps, s = t.type === t.elementType ? l : yo(t.type, l), i.props = s, f = t.pendingProps, d = i.context, u = "object" == typeof(u = n.contextType) && null !== u ? Oo(u) : ja(t, u = Ta(n) ? _a : Ra.current);
+                        i = t.stateNode, Do(e, t), l = t.memoizedProps, s = t.type === t.elementType ? l : yo(t.type, l), i.props = s, f = t.pendingProps, d = i.context, u = "object" == typeof(u = n.contextType) && null !== u ? Oo(u) : _a(t, u = Ta(n) ? ja : Ra.current);
                         var p = n.getDerivedStateFromProps;
-                        (c = "function" == typeof p || "function" == typeof i.getSnapshotBeforeUpdate) || "function" != typeof i.UNSAFE_componentWillReceiveProps && "function" != typeof i.componentWillReceiveProps || (l !== f || d !== u) && Ko(t, i, r, u), jo = !1, d = t.memoizedState, i.state = d, zo(t, r, i, a);
+                        (c = "function" == typeof p || "function" == typeof i.getSnapshotBeforeUpdate) || "function" != typeof i.UNSAFE_componentWillReceiveProps && "function" != typeof i.componentWillReceiveProps || (l !== f || d !== u) && Ko(t, i, r, u), _o = !1, d = t.memoizedState, i.state = d, zo(t, r, i, a);
                         var h = t.memoizedState;
-                        l !== f || d !== h || Na.current || jo ? ("function" == typeof p && (qo(t, n, p, r), h = t.memoizedState), (s = jo || Bo(t, n, s, r, d, h, u) || !1) ? (c || "function" != typeof i.UNSAFE_componentWillUpdate && "function" != typeof i.componentWillUpdate || ("function" == typeof i.componentWillUpdate && i.componentWillUpdate(r, h, u), "function" == typeof i.UNSAFE_componentWillUpdate && i.UNSAFE_componentWillUpdate(r, h, u)), "function" == typeof i.componentDidUpdate && (t.flags |= 4), "function" == typeof i.getSnapshotBeforeUpdate && (t.flags |= 1024)) : ("function" != typeof i.componentDidUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 4), "function" != typeof i.getSnapshotBeforeUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 1024), t.memoizedProps = r, t.memoizedState = h), i.props = r, i.state = h, i.context = u, r = s) : ("function" != typeof i.componentDidUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 4), "function" != typeof i.getSnapshotBeforeUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 1024), r = !1)
+                        l !== f || d !== h || Na.current || _o ? ("function" == typeof p && (qo(t, n, p, r), h = t.memoizedState), (s = _o || Bo(t, n, s, r, d, h, u) || !1) ? (c || "function" != typeof i.UNSAFE_componentWillUpdate && "function" != typeof i.componentWillUpdate || ("function" == typeof i.componentWillUpdate && i.componentWillUpdate(r, h, u), "function" == typeof i.UNSAFE_componentWillUpdate && i.UNSAFE_componentWillUpdate(r, h, u)), "function" == typeof i.componentDidUpdate && (t.flags |= 4), "function" == typeof i.getSnapshotBeforeUpdate && (t.flags |= 1024)) : ("function" != typeof i.componentDidUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 4), "function" != typeof i.getSnapshotBeforeUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 1024), t.memoizedProps = r, t.memoizedState = h), i.props = r, i.state = h, i.context = u, r = s) : ("function" != typeof i.componentDidUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 4), "function" != typeof i.getSnapshotBeforeUpdate || l === e.memoizedProps && d === e.memoizedState || (t.flags |= 1024), r = !1)
                     }
                     return Nl(e, t, n, r, o, a)
                 }
 
                 function Nl(e, t, n, r, a, o) {
                     Ol(e, t);
                     var i = 0 != (128 & t.flags);
                     if (!r && !i) return a && Ia(t, n, !1), Kl(e, t, o);
                     r = t.stateNode, bl.current = t;
                     var l = i && "function" != typeof n.getDerivedStateFromError ? null : r.render();
                     return t.flags |= 1, null !== e && i ? (t.child = Yo(t, e.child, null, o), t.child = Yo(t, null, l, o)) : El(e, t, l, o), t.memoizedState = r.state, a && Ia(t, n, !0), t.child
                 }
 
-                function _l(e) {
+                function jl(e) {
                     var t = e.stateNode;
                     t.pendingContext ? Aa(0, t.pendingContext, t.pendingContext !== t.context) : t.context && Aa(0, t.context, !1), ai(e, t.containerInfo)
                 }
 
-                function jl(e, t, n, r, a) {
+                function _l(e, t, n, r, a) {
                     return ho(), mo(a), t.flags |= 256, El(e, t, n, r), t.child
                 }
                 var Tl, Dl, Al, Ll, Ml = {
                     dehydrated: null,
                     treeContext: null,
                     retryLane: 0
                 };
@@ -5801,15 +5801,15 @@
                         }, a, 0, null), (i = Ms(i, a, l, null)).flags |= 2, r.return = t, i.return = t, r.sibling = i, t.child = r, 0 != (1 & t.mode) && Yo(t, e.child, null, l), t.child.memoizedState = Il(l), t.memoizedState = Ml, i);
                         if (0 == (1 & t.mode)) return Ul(e, t, l, null);
                         if ("$!" === a.data) {
                             if (r = a.nextSibling && a.nextSibling.dataset) var u = r.dgst;
                             return r = u, Ul(e, t, l, r = fl(i = Error(o(419)), r, void 0))
                         }
                         if (u = 0 != (l & e.childLanes), wl || u) {
-                            if (null !== (r = _u)) {
+                            if (null !== (r = ju)) {
                                 switch (l & -l) {
                                     case 4:
                                         a = 2;
                                         break;
                                     case 16:
                                         a = 8;
                                         break;
@@ -5838,15 +5838,15 @@
                                         break;
                                     case 536870912:
                                         a = 268435456;
                                         break;
                                     default:
                                         a = 0
                                 }
-                                0 !== (a = 0 != (a & (r.suspendedLanes | l)) ? 0 : a) && a !== i.retryLane && (i.retryLane = a, _o(e, a), rs(r, e, a, -1))
+                                0 !== (a = 0 != (a & (r.suspendedLanes | l)) ? 0 : a) && a !== i.retryLane && (i.retryLane = a, jo(e, a), rs(r, e, a, -1))
                             }
                             return vs(), Ul(e, t, l, r = fl(Error(o(421))))
                         }
                         return "$?" === a.data ? (t.flags |= 128, t.child = e.child, t = Rs.bind(null, e), a._reactRetry = t, null) : (e = i.treeContext, ro = sa(a.nextSibling), no = t, ao = !0, oo = null, null !== e && (Va[Ha++] = Xa, Va[Ha++] = Ya, Va[Ha++] = Ja, Xa = e.id, Ya = e.overflow, Ja = t), (t = Fl(t, r.children)).flags |= 4096, t)
                     }(e, t, u, a, r, i, n);
                     if (l) {
                         l = a.fallback, u = t.mode, r = (i = e.child).sibling;
@@ -6893,16 +6893,16 @@
                     }
                 }
                 var ku, Cu = Math.ceil,
                     Ou = w.ReactCurrentDispatcher,
                     Pu = w.ReactCurrentOwner,
                     Ru = w.ReactCurrentBatchConfig,
                     Nu = 0,
-                    _u = null,
                     ju = null,
+                    _u = null,
                     Tu = 0,
                     Du = 0,
                     Au = ka(0),
                     Lu = 0,
                     Mu = null,
                     Iu = 0,
                     zu = 0,
@@ -6929,27 +6929,27 @@
 
                 function ns(e) {
                     return 0 == (1 & e.mode) ? 1 : 0 != (2 & Nu) && 0 !== Tu ? Tu & -Tu : null !== vo.transition ? (0 === es && (es = mt()), es) : 0 !== (e = bt) ? e : e = void 0 === (e = window.event) ? 16 : Xt(e.type)
                 }
 
                 function rs(e, t, n, r) {
                     if (50 < Yu) throw Yu = 0, Gu = null, Error(o(185));
-                    yt(e, n, r), 0 != (2 & Nu) && e === _u || (e === _u && (0 == (2 & Nu) && (zu |= n), 4 === Lu && us(e, Tu)), as(e, r), 1 === n && 0 === Nu && 0 == (1 & t.mode) && (Bu = Ye() + 500, Fa && $a()))
+                    yt(e, n, r), 0 != (2 & Nu) && e === ju || (e === ju && (0 == (2 & Nu) && (zu |= n), 4 === Lu && us(e, Tu)), as(e, r), 1 === n && 0 === Nu && 0 == (1 & t.mode) && (Bu = Ye() + 500, Fa && $a()))
                 }
 
                 function as(e, t) {
                     var n = e.callbackNode;
                     ! function(e, t) {
                         for (var n = e.suspendedLanes, r = e.pingedLanes, a = e.expirationTimes, o = e.pendingLanes; 0 < o;) {
                             var i = 31 - it(o),
                                 l = 1 << i,
                                 u = a[i]; - 1 === u ? 0 != (l & n) && 0 == (l & r) || (a[i] = pt(l, t)) : u <= t && (e.expiredLanes |= l), o &= ~l
                         }
                     }(e, t);
-                    var r = dt(e, e === _u ? Tu : 0);
+                    var r = dt(e, e === ju ? Tu : 0);
                     if (0 === r) null !== n && He(n), e.callbackNode = null, e.callbackPriority = 0;
                     else if (t = r & -r, e.callbackPriority !== t) {
                         if (null != n && He(n), 1 === t) 0 === e.tag ? function(e) {
                             Fa = !0, qa(e)
                         }(ss.bind(null, e)) : qa(ss.bind(null, e)), ia((function() {
                             0 == (6 & Nu) && $a()
                         })), n = null;
@@ -6964,39 +6964,39 @@
                                 case 16:
                                 default:
                                     n = tt;
                                     break;
                                 case 536870912:
                                     n = rt
                             }
-                            n = _s(n, os.bind(null, e))
+                            n = js(n, os.bind(null, e))
                         }
                         e.callbackPriority = t, e.callbackNode = n
                     }
                 }
 
                 function os(e, t) {
                     if (Zu = -1, es = 0, 0 != (6 & Nu)) throw Error(o(327));
                     var n = e.callbackNode;
                     if (xs() && e.callbackNode !== n) return null;
-                    var r = dt(e, e === _u ? Tu : 0);
+                    var r = dt(e, e === ju ? Tu : 0);
                     if (0 === r) return null;
                     if (0 != (30 & r) || 0 != (r & e.expiredLanes) || t) t = ys(e, r);
                     else {
                         t = r;
                         var a = Nu;
                         Nu |= 2;
                         var i = ms();
-                        for (_u === e && Tu === t || (Qu = null, Bu = Ye() + 500, ps(e, t));;) try {
+                        for (ju === e && Tu === t || (Qu = null, Bu = Ye() + 500, ps(e, t));;) try {
                             bs();
                             break
                         } catch (t) {
                             hs(e, t)
                         }
-                        So(), Ou.current = i, Nu = a, null !== ju ? t = 0 : (_u = null, Tu = 0, t = Lu)
+                        So(), Ou.current = i, Nu = a, null !== _u ? t = 0 : (ju = null, Tu = 0, t = Lu)
                     }
                     if (0 !== t) {
                         if (2 === t && 0 !== (a = ht(e)) && (r = a, t = is(e, a)), 1 === t) throw n = Mu, ps(e, 0), us(e, r), as(e, Ye()), n;
                         if (6 === t) us(e, r);
                         else {
                             if (a = e.current.alternate, 0 == (30 & r) && ! function(e) {
                                     for (var t = e;;) {
@@ -7124,16 +7124,16 @@
                 function ds() {
                     Du = Au.current, Ca(Au)
                 }
 
                 function ps(e, t) {
                     e.finishedWork = null, e.finishedLanes = 0;
                     var n = e.timeoutHandle;
-                    if (-1 !== n && (e.timeoutHandle = -1, aa(n)), null !== ju)
-                        for (n = ju.return; null !== n;) {
+                    if (-1 !== n && (e.timeoutHandle = -1, aa(n)), null !== _u)
+                        for (n = _u.return; null !== n;) {
                             var r = n;
                             switch (to(r), r.tag) {
                                 case 1:
                                     null != (r = r.type.childContextTypes) && Da();
                                     break;
                                 case 3:
                                     oi(), Ca(Na), Ca(Ra), fi();
@@ -7153,15 +7153,15 @@
                                     break;
                                 case 22:
                                 case 23:
                                     ds()
                             }
                             n = n.return
                         }
-                    if (_u = e, ju = e = As(e.current, null), Tu = Du = t, Lu = 0, Mu = null, Fu = zu = Iu = 0, qu = Uu = null, null !== Po) {
+                    if (ju = e, _u = e = As(e.current, null), Tu = Du = t, Lu = 0, Mu = null, Fu = zu = Iu = 0, qu = Uu = null, null !== Po) {
                         for (t = 0; t < Po.length; t++)
                             if (null !== (r = (n = Po[t]).interleaved)) {
                                 n.interleaved = null;
                                 var a = r.next,
                                     o = n.pending;
                                 if (null !== o) {
                                     var i = o.next;
@@ -7171,25 +7171,25 @@
                             } Po = null
                     }
                     return e
                 }
 
                 function hs(e, t) {
                     for (;;) {
-                        var n = ju;
+                        var n = _u;
                         try {
                             if (So(), di.current = il, gi) {
                                 for (var r = mi.memoizedState; null !== r;) {
                                     var a = r.queue;
                                     null !== a && (a.pending = null), r = r.next
                                 }
                                 gi = !1
                             }
                             if (hi = 0, yi = vi = mi = null, bi = !1, wi = 0, Pu.current = null, null === n || null === n.return) {
-                                Lu = 1, Mu = t, ju = null;
+                                Lu = 1, Mu = t, _u = null;
                                 break
                             }
                             e: {
                                 var i = e,
                                     l = n.return,
                                     u = n,
                                     s = t;
@@ -7241,70 +7241,70 @@
                                             }
                                     }
                                     i = i.return
                                 } while (null !== i)
                             }
                             Es(n)
                         } catch (e) {
-                            t = e, ju === n && null !== n && (ju = n = n.return);
+                            t = e, _u === n && null !== n && (_u = n = n.return);
                             continue
                         }
                         break
                     }
                 }
 
                 function ms() {
                     var e = Ou.current;
                     return Ou.current = il, null === e ? il : e
                 }
 
                 function vs() {
-                    0 !== Lu && 3 !== Lu && 2 !== Lu || (Lu = 4), null === _u || 0 == (268435455 & Iu) && 0 == (268435455 & zu) || us(_u, Tu)
+                    0 !== Lu && 3 !== Lu && 2 !== Lu || (Lu = 4), null === ju || 0 == (268435455 & Iu) && 0 == (268435455 & zu) || us(ju, Tu)
                 }
 
                 function ys(e, t) {
                     var n = Nu;
                     Nu |= 2;
                     var r = ms();
-                    for (_u === e && Tu === t || (Qu = null, ps(e, t));;) try {
+                    for (ju === e && Tu === t || (Qu = null, ps(e, t));;) try {
                         gs();
                         break
                     } catch (t) {
                         hs(e, t)
                     }
-                    if (So(), Nu = n, Ou.current = r, null !== ju) throw Error(o(261));
-                    return _u = null, Tu = 0, Lu
+                    if (So(), Nu = n, Ou.current = r, null !== _u) throw Error(o(261));
+                    return ju = null, Tu = 0, Lu
                 }
 
                 function gs() {
-                    for (; null !== ju;) ws(ju)
+                    for (; null !== _u;) ws(_u)
                 }
 
                 function bs() {
-                    for (; null !== ju && !Je();) ws(ju)
+                    for (; null !== _u && !Je();) ws(_u)
                 }
 
                 function ws(e) {
                     var t = ku(e.alternate, e, Du);
-                    e.memoizedProps = e.pendingProps, null === t ? Es(e) : ju = t, Pu.current = null
+                    e.memoizedProps = e.pendingProps, null === t ? Es(e) : _u = t, Pu.current = null
                 }
 
                 function Es(e) {
                     var t = e;
                     do {
                         var n = t.alternate;
                         if (e = t.return, 0 == (32768 & t.flags)) {
-                            if (null !== (n = Hl(n, t, Du))) return void(ju = n)
+                            if (null !== (n = Hl(n, t, Du))) return void(_u = n)
                         } else {
-                            if (null !== (n = Jl(n, t))) return n.flags &= 32767, void(ju = n);
-                            if (null === e) return Lu = 6, void(ju = null);
+                            if (null !== (n = Jl(n, t))) return n.flags &= 32767, void(_u = n);
+                            if (null === e) return Lu = 6, void(_u = null);
                             e.flags |= 32768, e.subtreeFlags = 0, e.deletions = null
                         }
-                        if (null !== (t = t.sibling)) return void(ju = t);
-                        ju = t = e
+                        if (null !== (t = t.sibling)) return void(_u = t);
+                        _u = t = e
                     } while (null !== t);
                     0 === Lu && (Lu = 5)
                 }
 
                 function Ss(e, t, n) {
                     var r = bt,
                         a = Ru.transition;
@@ -7326,15 +7326,15 @@
                                         e.pendingLanes = t, e.suspendedLanes = 0, e.pingedLanes = 0, e.expiredLanes &= t, e.mutableReadLanes &= t, e.entangledLanes &= t, t = e.entanglements;
                                         var r = e.eventTimes;
                                         for (e = e.expirationTimes; 0 < n;) {
                                             var a = 31 - it(n),
                                                 o = 1 << a;
                                             t[a] = 0, r[a] = -1, e[a] = -1, n &= ~o
                                         }
-                                    }(e, i), e === _u && (ju = _u = null, Tu = 0), 0 == (2064 & n.subtreeFlags) && 0 == (2064 & n.flags) || Hu || (Hu = !0, _s(tt, (function() {
+                                    }(e, i), e === ju && (_u = ju = null, Tu = 0), 0 == (2064 & n.subtreeFlags) && 0 == (2064 & n.flags) || Hu || (Hu = !0, js(tt, (function() {
                                         return xs(), null
                                     }))), i = 0 != (15990 & n.flags), 0 != (15990 & n.subtreeFlags) || i) {
                                     i = Ru.transition, Ru.transition = null;
                                     var l = bt;
                                     bt = 1;
                                     var u = Nu;
                                     Nu |= 4, Pu.current = null,
@@ -7584,21 +7584,21 @@
                             }
                             t = t.return
                         }
                 }
 
                 function Os(e, t, n) {
                     var r = e.pingCache;
-                    null !== r && r.delete(t), t = ts(), e.pingedLanes |= e.suspendedLanes & n, _u === e && (Tu & n) === n && (4 === Lu || 3 === Lu && (130023424 & Tu) === Tu && 500 > Ye() - $u ? ps(e, 0) : Fu |= n), as(e, t)
+                    null !== r && r.delete(t), t = ts(), e.pingedLanes |= e.suspendedLanes & n, ju === e && (Tu & n) === n && (4 === Lu || 3 === Lu && (130023424 & Tu) === Tu && 500 > Ye() - $u ? ps(e, 0) : Fu |= n), as(e, t)
                 }
 
                 function Ps(e, t) {
                     0 === t && (0 == (1 & e.mode) ? t = 1 : (t = ct, 0 == (130023424 & (ct <<= 1)) && (ct = 4194304)));
                     var n = ts();
-                    null !== (e = _o(e, t)) && (yt(e, t, n), as(e, n))
+                    null !== (e = jo(e, t)) && (yt(e, t, n), as(e, n))
                 }
 
                 function Rs(e) {
                     var t = e.memoizedState,
                         n = 0;
                     null !== t && (n = t.retryLane), Ps(e, n)
                 }
@@ -7616,24 +7616,24 @@
                             break;
                         default:
                             throw Error(o(314))
                     }
                     null !== r && r.delete(t), Ps(e, n)
                 }
 
-                function _s(e, t) {
+                function js(e, t) {
                     return Ve(e, t)
                 }
 
-                function js(e, t, n, r) {
+                function _s(e, t, n, r) {
                     this.tag = e, this.key = n, this.sibling = this.child = this.return = this.stateNode = this.type = this.elementType = null, this.index = 0, this.ref = null, this.pendingProps = t, this.dependencies = this.memoizedState = this.updateQueue = this.memoizedProps = null, this.mode = r, this.subtreeFlags = this.flags = 0, this.deletions = null, this.childLanes = this.lanes = 0, this.alternate = null
                 }
 
                 function Ts(e, t, n, r) {
-                    return new js(e, t, n, r)
+                    return new _s(e, t, n, r)
                 }
 
                 function Ds(e) {
                     return !(!(e = e.prototype) || !e.isReactComponent)
                 }
 
                 function As(e, t) {
@@ -7654,30 +7654,30 @@
                         case k:
                             l = 8, a |= 8;
                             break;
                         case C:
                             return (e = Ts(12, n, t, 2 | a)).elementType = C, e.lanes = i, e;
                         case N:
                             return (e = Ts(13, n, t, a)).elementType = N, e.lanes = i, e;
-                        case _:
-                            return (e = Ts(19, n, t, a)).elementType = _, e.lanes = i, e;
+                        case j:
+                            return (e = Ts(19, n, t, a)).elementType = j, e.lanes = i, e;
                         case D:
                             return Is(n, a, i, t);
                         default:
                             if ("object" == typeof e && null !== e) switch (e.$$typeof) {
                                 case O:
                                     l = 10;
                                     break e;
                                 case P:
                                     l = 9;
                                     break e;
                                 case R:
                                     l = 11;
                                     break e;
-                                case j:
+                                case _:
                                     l = 14;
                                     break e;
                                 case T:
                                     l = 16, r = null;
                                     break e
                             }
                             throw Error(o(130, null == e ? e : typeof e, ""))
@@ -7778,15 +7778,15 @@
                     if (null !== e)
                         if (e.memoizedProps !== t.pendingProps || Na.current) wl = !0;
                         else {
                             if (0 == (e.lanes & n) && 0 == (128 & t.flags)) return wl = !1,
                                 function(e, t, n) {
                                     switch (t.tag) {
                                         case 3:
-                                            _l(t), ho();
+                                            jl(t), ho();
                                             break;
                                         case 5:
                                             ii(t);
                                             break;
                                         case 1:
                                             Ta(t.type) && Ma(t);
                                             break;
@@ -7818,26 +7818,26 @@
                             wl = 0 != (131072 & e.flags)
                         }
                     else wl = !1, ao && 0 != (1048576 & t.flags) && Za(t, Wa, t.index);
                     switch (t.lanes = 0, t.tag) {
                         case 2:
                             var r = t.type;
                             Ql(e, t), e = t.pendingProps;
-                            var a = ja(t, Ra.current);
+                            var a = _a(t, Ra.current);
                             Co(t, n), a = ki(null, t, r, e, a, n);
                             var i = Ci();
                             return t.flags |= 1, "object" == typeof a && null !== a && "function" == typeof a.render && void 0 === a.$$typeof ? (t.tag = 1, t.memoizedState = null, t.updateQueue = null, Ta(r) ? (i = !0, Ma(t)) : i = !1, t.memoizedState = null !== a.state && void 0 !== a.state ? a.state : null, To(t), a.updater = $o, t.stateNode = a, a._reactInternals = t, Wo(t, r, e, n), t = Nl(null, t, r, !0, i, n)) : (t.tag = 0, ao && i && eo(t), El(null, t, a, n), t = t.child), t;
                         case 16:
                             r = t.elementType;
                             e: {
                                 switch (Ql(e, t), e = t.pendingProps, r = (a = r._init)(r._payload), t.type = r, a = t.tag = function(e) {
                                         if ("function" == typeof e) return Ds(e) ? 1 : 0;
                                         if (null != e) {
                                             if ((e = e.$$typeof) === R) return 11;
-                                            if (e === j) return 14
+                                            if (e === _) return 14
                                         }
                                         return 2
                                     }(r), e = yo(r, e), a) {
                                     case 0:
                                         t = Pl(null, t, r, e, n);
                                         break e;
                                     case 1:
@@ -7855,32 +7855,32 @@
                             return t;
                         case 0:
                             return r = t.type, a = t.pendingProps, Pl(e, t, r, a = t.elementType === r ? a : yo(r, a), n);
                         case 1:
                             return r = t.type, a = t.pendingProps, Rl(e, t, r, a = t.elementType === r ? a : yo(r, a), n);
                         case 3:
                             e: {
-                                if (_l(t), null === e) throw Error(o(387));r = t.pendingProps,
+                                if (jl(t), null === e) throw Error(o(387));r = t.pendingProps,
                                 a = (i = t.memoizedState).element,
                                 Do(e, t),
                                 zo(t, r, null, n);
                                 var l = t.memoizedState;
                                 if (r = l.element, i.isDehydrated) {
                                     if (i = {
                                             element: r,
                                             isDehydrated: !1,
                                             cache: l.cache,
                                             pendingSuspenseBoundaries: l.pendingSuspenseBoundaries,
                                             transitions: l.transitions
                                         }, t.updateQueue.baseState = i, t.memoizedState = i, 256 & t.flags) {
-                                        t = jl(e, t, r, n, a = cl(Error(o(423)), t));
+                                        t = _l(e, t, r, n, a = cl(Error(o(423)), t));
                                         break e
                                     }
                                     if (r !== a) {
-                                        t = jl(e, t, r, n, a = cl(Error(o(424)), t));
+                                        t = _l(e, t, r, n, a = cl(Error(o(424)), t));
                                         break e
                                     }
                                     for (ro = sa(t.stateNode.containerInfo.firstChild), no = t, ao = !0, oo = null, n = Go(t, null, r, n), t.child = n; n;) n.flags = -3 & n.flags | 4096, n = n.sibling
                                 } else {
                                     if (ho(), r === a) {
                                         t = Kl(e, t, n);
                                         break e
@@ -8064,30 +8064,30 @@
                             if (t.current.memoizedState.isDehydrated) {
                                 var n = ft(t.pendingLanes);
                                 0 !== n && (gt(t, 1 | n), as(t, Ye()), 0 == (6 & Nu) && (Bu = Ye() + 500, $a()))
                             }
                             break;
                         case 13:
                             fs((function() {
-                                var t = _o(e, 1);
+                                var t = jo(e, 1);
                                 if (null !== t) {
                                     var n = ts();
                                     rs(t, e, 1, n)
                                 }
                             })), Vs(e, 1)
                     }
                 }, St = function(e) {
                     if (13 === e.tag) {
-                        var t = _o(e, 134217728);
+                        var t = jo(e, 134217728);
                         null !== t && rs(t, e, 134217728, ts()), Vs(e, 134217728)
                     }
                 }, xt = function(e) {
                     if (13 === e.tag) {
                         var t = ns(e),
-                            n = _o(e, t);
+                            n = jo(e, t);
                         null !== n && rs(n, e, t, ts()), Vs(e, t)
                     }
                 }, kt = function() {
                     return bt
                 }, Ct = function(e, t) {
                     var n = bt;
                     try {
@@ -8816,17 +8816,17 @@
                         storageKey: n
                     } = e;
                     return B({
                         getKey: t,
                         storageKey: n
                     }), null
                 }
-                var N, _;
+                var N, j;
 
-                function j(e) {
+                function _(e) {
                     let t = r.useContext(a.w3);
                     return t || (0, o.J0)(!1), t
                 }
 
                 function T(e) {
                     let t = r.useContext(a.FR);
                     return t || (0, o.J0)(!1), t
@@ -8883,15 +8883,15 @@
                 function L() {
                     return M()
                 }
 
                 function M(e, t) {
                     let {
                         router: n
-                    } = j(N.UseSubmitImpl), a = I();
+                    } = _(N.UseSubmitImpl), a = I();
                     return r.useCallback((function(r, i) {
                         if (void 0 === i && (i = {}), "undefined" == typeof document) throw new Error("You are calling submit during the server render. Try calling submit within a `useEffect` or callback instead.");
                         let {
                             method: l,
                             encType: f,
                             formData: d,
                             url: p
@@ -8954,22 +8954,22 @@
                     }
                     return e && "." !== e || !s.route.index || (c.search = c.search ? c.search.replace(/^\?/, "?index&") : "?index"), "/" !== l && (c.pathname = "/" === c.pathname ? l : (0, o.RQ)([l, c.pathname])), (0, o.Ep)(c)
                 }(function(e) {
                     e.UseScrollRestoration = "useScrollRestoration", e.UseSubmitImpl = "useSubmitImpl", e.UseFetcher = "useFetcher"
                 })(N || (N = {})),
                 function(e) {
                     e.UseFetchers = "useFetchers", e.UseScrollRestoration = "useScrollRestoration"
-                }(_ || (_ = {}));
+                }(j || (j = {}));
                 let z = 0;
 
                 function F() {
                     var e;
                     let {
                         router: t
-                    } = j(N.UseFetcher), n = r.useContext(a.pW);
+                    } = _(N.UseFetcher), n = r.useContext(a.pW);
                     n || (0, o.J0)(!1);
                     let l = null == (e = n.matches[n.matches.length - 1]) ? void 0 : e.route.id;
                     null == l && (0, o.J0)(!1);
                     let [u] = r.useState((() => String(++z))), [s] = r.useState((() => (l || (0, o.J0)(!1), function(e, t) {
                         return r.forwardRef(((n, a) => r.createElement(P, i({}, n, {
                             ref: a,
                             fetcherKey: e,
@@ -8984,29 +8984,29 @@
                     }, d)), [d, s, f, c]);
                     return r.useEffect((() => () => {
                         t ? t.deleteFetcher(u) : console.warn("No fetcher available to clean up from useFetcher()")
                     }), [t, u]), p
                 }
 
                 function U() {
-                    return [...T(_.UseFetchers).fetchers.values()]
+                    return [...T(j.UseFetchers).fetchers.values()]
                 }
                 const q = "react-router-scroll-positions";
                 let $ = {};
 
                 function B(e) {
                     let {
                         getKey: t,
                         storageKey: n
                     } = void 0 === e ? {} : e, {
                         router: o
-                    } = j(N.UseScrollRestoration), {
+                    } = _(N.UseScrollRestoration), {
                         restoreScrollPosition: i,
                         preventScrollReset: l
-                    } = T(_.UseScrollRestoration), u = (0, a.TH)(), s = (0, a.SN)(), c = (0, a.HJ)();
+                    } = T(j.UseScrollRestoration), u = (0, a.TH)(), s = (0, a.SN)(), c = (0, a.HJ)();
                     r.useEffect((() => (window.history.scrollRestoration = "manual", () => {
                             window.history.scrollRestoration = "auto"
                         })), []),
                         function(e, t) {
                             let {
                                 capture: n
                             } = {};
@@ -9081,15 +9081,15 @@
                     HJ: () => U,
                     KP: () => ae,
                     Oe: () => ce,
                     SN: () => $,
                     TH: () => E,
                     UO: () => R,
                     Us: () => h,
-                    V$: () => _,
+                    V$: () => j,
                     V4: () => Q,
                     VA: () => G,
                     WU: () => N,
                     Z5: () => re,
                     aQ: () => X,
                     b6: () => fe,
                     bS: () => x,
@@ -9233,15 +9233,15 @@
                         matches: r
                     } = o.useContext(v), {
                         pathname: i
                     } = E(), l = JSON.stringify((0, a.Zq)(r).map((e => e.pathnameBase)));
                     return o.useMemo((() => (0, a.pC)(e, JSON.parse(l), i, "path" === n)), [e, l, i, n])
                 }
 
-                function _(e, t) {
+                function j(e, t) {
                     w() || (0, a.J0)(!1);
                     let {
                         navigator: n
                     } = o.useContext(h), r = o.useContext(d), {
                         matches: i
                     } = o.useContext(v), l = i[i.length - 1], u = l ? l.params : {}, s = (l && l.pathname, l ? l.pathnameBase : "/");
                     l && l.route;
@@ -9271,15 +9271,15 @@
                                 key: "default"
                             }, c),
                             navigationType: a.aU.Pop
                         }
                     }, x) : x
                 }
 
-                function j() {
+                function _() {
                     let e = W(),
                         t = (0, a.WK)(e) ? e.status + " " + e.statusText : e instanceof Error ? e.message : JSON.stringify(e),
                         n = e instanceof Error ? e.stack : null,
                         r = {
                             padding: "0.5rem",
                             backgroundColor: "rgba(200,200,200, 0.5)"
                         };
@@ -9346,15 +9346,15 @@
                     if (null != i) {
                         let e = r.findIndex((e => e.route.id && (null == i ? void 0 : i[e.route.id])));
                         e >= 0 || (0, a.J0)(!1), r = r.slice(0, Math.min(r.length, e + 1))
                     }
                     return r.reduceRight(((e, a, l) => {
                         let u = a.route.id ? null == i ? void 0 : i[a.route.id] : null,
                             s = null;
-                        n && (s = a.route.ErrorBoundary ? o.createElement(a.route.ErrorBoundary, null) : a.route.errorElement ? a.route.errorElement : o.createElement(j, null));
+                        n && (s = a.route.ErrorBoundary ? o.createElement(a.route.ErrorBoundary, null) : a.route.errorElement ? a.route.errorElement : o.createElement(_, null));
                         let c = t.concat(r.slice(0, l + 1)),
                             f = () => {
                                 let t = e;
                                 return u ? t = s : a.route.Component ? t = o.createElement(a.route.Component, null) : a.route.element && (t = a.route.element), o.createElement(D, {
                                     match: a,
                                     routeContext: {
                                         outlet: e,
@@ -9609,15 +9609,15 @@
                 }
 
                 function re(e) {
                     let {
                         children: t,
                         location: n
                     } = e, r = o.useContext(f);
-                    return _(r && !t ? r.router.routes : se(t), n)
+                    return j(r && !t ? r.router.routes : se(t), n)
                 }
 
                 function ae(e) {
                     let {
                         children: t,
                         errorElement: n,
                         resolve: r
@@ -9907,24 +9907,24 @@
                                 return null === e || "object" != typeof e ? null : "function" == typeof(e = p && e[p] || e["@@iterator"]) ? e : null
                             }(e), "function" == typeof c)
                             for (e = c.call(e), s = 0; !(l = e.next()).done;) u += N(l = l.value, t, a, c = o + R(l, s++), i);
                         else if ("object" === l) throw t = String(e), Error("Objects are not valid as a React child (found: " + ("[object Object]" === t ? "object with keys {" + Object.keys(e).join(", ") + "}" : t) + "). If you meant to render a collection of children, use an array instead.");
                     return u
                 }
 
-                function _(e, t, n) {
+                function j(e, t, n) {
                     if (null == e) return e;
                     var r = [],
                         a = 0;
                     return N(e, r, "", "", (function(e) {
                         return t.call(n, e, a++)
                     })), r
                 }
 
-                function j(e) {
+                function _(e) {
                     if (-1 === e._status) {
                         var t = e._result;
                         (t = t()).then((function(t) {
                             0 !== e._status && -1 !== e._status || (e._status = 1, e._result = t)
                         }), (function(t) {
                             0 !== e._status && -1 !== e._status || (e._status = 2, e._result = t)
                         })), -1 === e._status && (e._status = 0, e._result = t)
@@ -9940,28 +9940,28 @@
                     },
                     A = {
                         ReactCurrentDispatcher: T,
                         ReactCurrentBatchConfig: D,
                         ReactCurrentOwner: x
                     };
                 t.Children = {
-                    map: _,
+                    map: j,
                     forEach: function(e, t, n) {
-                        _(e, (function() {
+                        j(e, (function() {
                             t.apply(this, arguments)
                         }), n)
                     },
                     count: function(e) {
                         var t = 0;
-                        return _(e, (function() {
+                        return j(e, (function() {
                             t++
                         })), t
                     },
                     toArray: function(e) {
-                        return _(e, (function(e) {
+                        return j(e, (function(e) {
                             return e
                         })) || []
                     },
                     only: function(e) {
                         if (!O(e)) throw Error("React.Children.only expected to receive a single React element child.");
                         return e
                     }
@@ -10019,15 +10019,15 @@
                 }, t.isValidElement = O, t.lazy = function(e) {
                     return {
                         $$typeof: d,
                         _payload: {
                             _status: -1,
                             _result: e
                         },
-                        _init: j
+                        _init: _
                     }
                 }, t.memo = function(e, t) {
                     return {
                         $$typeof: f,
                         type: e,
                         compare: void 0 === t ? null : t
                     }
@@ -10196,37 +10196,37 @@
                     P = 5,
                     R = -1;
 
                 function N() {
                     return !(t.unstable_now() - R < P)
                 }
 
-                function _() {
+                function j() {
                     if (null !== C) {
                         var e = t.unstable_now();
                         R = e;
                         var n = !0;
                         try {
                             n = C(!0, e)
                         } finally {
                             n ? x() : (k = !1, C = null)
                         }
                     } else k = !1
                 }
                 if ("function" == typeof b) x = function() {
-                    b(_)
+                    b(j)
                 };
                 else if ("undefined" != typeof MessageChannel) {
-                    var j = new MessageChannel,
-                        T = j.port2;
-                    j.port1.onmessage = _, x = function() {
+                    var _ = new MessageChannel,
+                        T = _.port2;
+                    _.port1.onmessage = j, x = function() {
                         T.postMessage(null)
                     }
                 } else x = function() {
-                    y(_, 0)
+                    y(j, 0)
                 };
 
                 function D(e) {
                     C = e, k || (k = !0, x())
                 }
 
                 function A(e, n) {
@@ -10641,36 +10641,36 @@
         O.displayName = "NavbarBrand";
         const P = O;
 
         function R(e) {
             return e && e.ownerDocument || document
         }
         var N = /([A-Z])/g,
-            _ = /^ms-/;
+            j = /^ms-/;
 
-        function j(e) {
+        function _(e) {
             return function(e) {
                 return e.replace(N, "-$1").toLowerCase()
-            }(e).replace(_, "-ms-")
+            }(e).replace(j, "-ms-")
         }
         var T = /^((translate|rotate|scale)(X|Y|Z|3d)?|matrix(3d)?|perspective|skew(X|Y)?)$/i;
         const D = function(e, t) {
             var n = "",
                 r = "";
-            if ("string" == typeof t) return e.style.getPropertyValue(j(t)) || function(e, t) {
+            if ("string" == typeof t) return e.style.getPropertyValue(_(t)) || function(e, t) {
                 return function(e) {
                     var t = R(e);
                     return t && t.defaultView || window
                 }(e).getComputedStyle(e, t)
-            }(e).getPropertyValue(j(t));
+            }(e).getPropertyValue(_(t));
             Object.keys(t).forEach((function(a) {
                 var o = t[a];
                 o || 0 === o ? function(e) {
                     return !(!e || !T.test(e))
-                }(a) ? r += a + "(" + o + ") " : n += j(a) + ": " + o + ";" : e.style.removeProperty(j(a))
+                }(a) ? r += a + "(" + o + ") " : n += _(a) + ": " + o + ";" : e.style.removeProperty(_(a))
             })), r && (n += "transform: " + r + ";"), e.style.cssText += ";" + n
         };
 
         function A(e, t) {
             return A = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(e, t) {
                 return e.__proto__ = t, e
             }, A(e, t)
@@ -11197,15 +11197,15 @@
         }
         const Pe = "data-rr-ui-";
 
         function Re(e) {
             return `${Pe}${e}`
         }
         const Ne = Re("modal-open"),
-            _e = class {
+            je = class {
                 constructor({
                     ownerDocument: e,
                     handleContainerOverflow: t = !0,
                     isRTL: n = !1
                 } = {}) {
                     this.handleContainerOverflow = t, this.isRTL = n, this.modals = [], this.ownerDocument = e
                 }
@@ -11248,20 +11248,20 @@
                 remove(e) {
                     const t = this.modals.indexOf(e); - 1 !== t && (this.modals.splice(t, 1), !this.modals.length && this.handleContainerOverflow && this.removeContainerStyle(this.state), this.removeModalAttributes(e))
                 }
                 isTopModal(e) {
                     return !!this.modals.length && this.modals[this.modals.length - 1] === e
                 }
             },
-            je = (0, e.createContext)(K ? window : void 0);
+            _e = (0, e.createContext)(K ? window : void 0);
 
         function Te() {
-            return (0, e.useContext)(je)
+            return (0, e.useContext)(_e)
         }
-        je.Provider;
+        _e.Provider;
         const De = (e, t) => K ? null == e ? (t || R()).body : ("function" == typeof e && (e = e()), e && "current" in e && (e = e.current), e && ("nodeType" in e || e.getBoundingClientRect) ? e : null) : null,
             Ae = function({
                 children: t,
                 in: n,
                 onExited: r,
                 mountOnEnter: a,
                 unmountOnExit: o
@@ -11356,16 +11356,16 @@
                 manager: x,
                 container: k,
                 onShow: C,
                 onHide: O = (() => {}),
                 onExit: P,
                 onExited: R,
                 onExiting: N,
-                onEnter: _,
-                onEntering: j,
+                onEnter: j,
+                onEntering: _,
                 onEntered: T
             } = t, D = function(e, t) {
                 if (null == e) return {};
                 var n, r, a = {},
                     o = Object.keys(e);
                 for (r = 0; r < o.length; r++) n = o[r], t.indexOf(n) >= 0 || (a[n] = e[n]);
                 return a
@@ -11381,15 +11381,15 @@
                         const e = De(t);
                         e !== a && o(e)
                     }), [t, a]), a
                 }(k),
                 M = function(t) {
                     const n = Te(),
                         r = t || function(e) {
-                            return ze || (ze = new _e({
+                            return ze || (ze = new je({
                                 ownerDocument: null == e ? void 0 : e.document
                             })), ze
                         }(n),
                         a = (0, e.useRef)({
                             dialog: null,
                             backdrop: null
                         });
@@ -11487,16 +11487,16 @@
                 appear: !0,
                 in: !!r,
                 onExit: P,
                 onExiting: N,
                 onExited: (...e) => {
                     U(!0), null == R || R(...e)
                 },
-                onEnter: _,
-                onEntering: j,
+                onEnter: j,
+                onEntering: _,
                 onEntered: T,
                 children: G
             });
             let Z = null;
             return s && (Z = S({
                 ref: M.setBackdropRef,
                 onClick: W
@@ -11510,15 +11510,15 @@
                 children: L.createPortal((0, l.jsxs)(l.Fragment, {
                     children: [Z, G]
                 }), A)
             })
         }));
         Fe.displayName = "Modal";
         const Ue = Object.assign(Fe, {
-                Manager: _e
+                Manager: je
             }),
             qe = {
                 [F]: "show",
                 [U]: "show"
             },
             $e = e.forwardRef((({
                 className: t,
@@ -11657,15 +11657,15 @@
 
         function ut(e, t) {
             return e.replace(new RegExp("(^|\\s)" + t + "(?:\\s|$)", "g"), "$1").replace(/\s+/g, " ").replace(/^\s*|\s*$/g, "")
         }
         const st = ".fixed-top, .fixed-bottom, .is-fixed, .sticky-top",
             ct = ".sticky-top",
             ft = ".navbar-toggler";
-        class dt extends _e {
+        class dt extends je {
             adjustAndStore(e, t, n) {
                 const r = t.style[e];
                 t.dataset[e] = r, D(t, {
                     [e]: `${parseFloat(D(t,e))+n}px`
                 })
             }
             restore(e, t) {
@@ -11732,16 +11732,16 @@
             onExit: x,
             onExiting: k,
             onEnter: C,
             onEntering: O,
             onExited: P,
             backdropClassName: R,
             manager: N,
-            renderStaticNode: _,
-            ...j
+            renderStaticNode: j,
+            ..._
         }, T) => {
             const D = (0, e.useRef)();
             t = f(t, "offcanvas");
             const {
                 onToggle: A
             } = (0, e.useContext)(de) || {}, [L, M] = (0, e.useState)(!1), I = ke(u || "xs", "up");
             (0, e.useEffect)((() => {
@@ -11755,21 +11755,21 @@
                 })), [z]),
                 U = (0, e.useCallback)((e => (0, l.jsx)("div", {
                     ...e,
                     className: i()(`${t}-backdrop`, R)
                 })), [R, t]),
                 q = e => (0, l.jsx)("div", {
                     ...e,
-                    ...j,
+                    ..._,
                     className: i()(n, u ? `${t}-${u}` : t, `${t}-${o}`),
                     "aria-labelledby": a,
                     children: r
                 });
             return (0, l.jsxs)(l.Fragment, {
-                children: [!L && (u || _) && q({}), (0, l.jsx)(He.Provider, {
+                children: [!L && (u || j) && q({}), (0, l.jsx)(He.Provider, {
                     value: F,
                     children: (0, l.jsx)(Ue, {
                         show: L,
                         ref: T,
                         backdrop: c,
                         container: y,
                         keyboard: d,
@@ -11947,16 +11947,16 @@
                 disabled: r
             }, a));
             return (0, l.jsx)(i, Object.assign({}, a, o, {
                 ref: t
             }))
         }));
         Nt.displayName = "Button";
-        const _t = Nt,
-            jt = ["as", "active", "eventKey"];
+        const jt = Nt,
+            _t = ["as", "active", "eventKey"];
 
         function Tt({
             key: t,
             onClick: n,
             active: r,
             id: a,
             role: o,
@@ -11979,24 +11979,24 @@
                 i || (null == n || n(e), null != t && l && !e.isPropagationStopped() && l(t, e))
             })), [f, {
                 isActive: c
             }]
         }
         const Dt = e.forwardRef(((e, t) => {
             let {
-                as: n = _t,
+                as: n = jt,
                 active: r,
                 eventKey: a
             } = e, o = function(e, t) {
                 if (null == e) return {};
                 var n, r, a = {},
                     o = Object.keys(e);
                 for (r = 0; r < o.length; r++) n = o[r], t.indexOf(n) >= 0 || (a[n] = e[n]);
                 return a
-            }(e, jt);
+            }(e, _t);
             const [i, u] = Tt(Object.assign({
                 key: v(a, o.href),
                 active: r
             }, o));
             return i[Re("active")] = u.isActive, (0, l.jsx)(n, Object.assign({}, o, i, {
                 ref: t
             }))
@@ -12431,50 +12431,50 @@
             0 === t.i || 1 === t.i ? t.j() : t.g = !0
         }
 
         function Rn(e, t) {
             t._ = t.p.length;
             var n = t.p[0],
                 r = void 0 !== e && e !== n;
-            return t.h.O || wn("ES5").S(t, e, r), r ? (n[Vn].P && (kn(t), rn(4)), on(e) && (e = Nn(t, e), t.l || jn(t, e)), t.u && wn("Patches").M(n[Vn].t, e, t.u, t.s)) : e = Nn(t, n, []), kn(t), t.u && t.v(t.u, t.s), e !== Kn ? e : void 0
+            return t.h.O || wn("ES5").S(t, e, r), r ? (n[Vn].P && (kn(t), rn(4)), on(e) && (e = Nn(t, e), t.l || _n(t, e)), t.u && wn("Patches").M(n[Vn].t, e, t.u, t.s)) : e = Nn(t, n, []), kn(t), t.u && t.v(t.u, t.s), e !== Kn ? e : void 0
         }
 
         function Nn(e, t, n) {
             if (bn(t)) return t;
             var r = t[Vn];
             if (!r) return ln(t, (function(a, o) {
-                return _n(e, r, t, a, o, n)
+                return jn(e, r, t, a, o, n)
             }), !0), t;
             if (r.A !== e) return t;
-            if (!r.P) return jn(e, r.t, !0), r.t;
+            if (!r.P) return _n(e, r.t, !0), r.t;
             if (!r.I) {
                 r.I = !0, r.A._--;
                 var a = 4 === r.i || 5 === r.i ? r.o = vn(r.k) : r.o,
                     o = a,
                     i = !1;
                 3 === r.i && (o = new Set(a), a.clear(), i = !0), ln(o, (function(t, o) {
-                    return _n(e, r, a, t, o, n, i)
-                })), jn(e, a, !1), n && e.u && wn("Patches").N(r, n, e.u, e.s)
+                    return jn(e, r, a, t, o, n, i)
+                })), _n(e, a, !1), n && e.u && wn("Patches").N(r, n, e.u, e.s)
             }
             return r.o
         }
 
-        function _n(e, t, n, r, a, o, i) {
+        function jn(e, t, n, r, a, o, i) {
             if (an(a)) {
                 var l = Nn(e, a, o && t && 3 !== t.i && !sn(t.R, r) ? o.concat(r) : void 0);
                 if (fn(n, r, l), !an(l)) return;
                 e.m = !1
             } else i && n.add(a);
             if (on(a) && !bn(a)) {
                 if (!e.h.D && e._ < 1) return;
-                Nn(e, a), t && t.A.l || jn(e, a)
+                Nn(e, a), t && t.A.l || _n(e, a)
             }
         }
 
-        function jn(e, t, n) {
+        function _n(e, t, n) {
             void 0 === n && (n = !1), !e.l && e.h.D && e.m && yn(t, n)
         }
 
         function Tn(e, t) {
             var n = e[Vn];
             return (n ? mn(n) : e)[t]
         }
@@ -12981,26 +12981,26 @@
             },
             kr = Object.defineProperty,
             Cr = Object.defineProperties,
             Or = Object.getOwnPropertyDescriptors,
             Pr = Object.getOwnPropertySymbols,
             Rr = Object.prototype.hasOwnProperty,
             Nr = Object.prototype.propertyIsEnumerable,
-            _r = function(e, t, n) {
+            jr = function(e, t, n) {
                 return t in e ? kr(e, t, {
                     enumerable: !0,
                     configurable: !0,
                     writable: !0,
                     value: n
                 }) : e[t] = n
             },
-            jr = function(e, t) {
-                for (var n in t || (t = {})) Rr.call(t, n) && _r(e, n, t[n]);
+            _r = function(e, t) {
+                for (var n in t || (t = {})) Rr.call(t, n) && jr(e, n, t[n]);
                 if (Pr)
-                    for (var r = 0, a = Pr(t); r < a.length; r++) n = a[r], Nr.call(t, n) && _r(e, n, t[n]);
+                    for (var r = 0, a = Pr(t); r < a.length; r++) n = a[r], Nr.call(t, n) && jr(e, n, t[n]);
                 return e
             },
             Tr = function(e, t) {
                 return Cr(e, Or(t))
             },
             Dr = "undefined" != typeof window && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ : function() {
                 if (0 !== arguments.length) return "object" == typeof arguments[0] ? vr : vr.apply(null, arguments)
@@ -13041,15 +13041,15 @@
 
         function Ir(e, t) {
             function n() {
                 for (var n = [], r = 0; r < arguments.length; r++) n[r] = arguments[r];
                 if (t) {
                     var a = t.apply(void 0, n);
                     if (!a) throw new Error("prepareAction did not return an object");
-                    return jr(jr({
+                    return _r(_r({
                         type: e,
                         payload: a.payload
                     }, "meta" in a && {
                         meta: a.meta
                     }), "error" in a && {
                         error: a.error
                     })
@@ -13102,15 +13102,15 @@
                 var t = "function" == typeof e.extraReducers ? zr(e.extraReducers) : [e.extraReducers],
                     n = t[0],
                     a = void 0 === n ? {} : n,
                     o = t[1],
                     i = void 0 === o ? [] : o,
                     u = t[2],
                     s = void 0 === u ? void 0 : u,
-                    c = jr(jr({}, a), l);
+                    c = _r(_r({}, a), l);
                 return function(e, t, n, r) {
                     void 0 === n && (n = []);
                     var a, o = zr(t),
                         i = o[0],
                         l = o[1],
                         u = o[2];
                     if (function(e) {
@@ -13201,36 +13201,36 @@
                 }
             },
             Kr = function() {
                 function e(e, t, n) {
                     var r = Ir(e + "/fulfilled", (function(e, t, n, r) {
                             return {
                                 payload: e,
-                                meta: Tr(jr({}, r || {}), {
+                                meta: Tr(_r({}, r || {}), {
                                     arg: n,
                                     requestId: t,
                                     requestStatus: "fulfilled"
                                 })
                             }
                         })),
                         a = Ir(e + "/pending", (function(e, t, n) {
                             return {
                                 payload: void 0,
-                                meta: Tr(jr({}, n || {}), {
+                                meta: Tr(_r({}, n || {}), {
                                     arg: t,
                                     requestId: e,
                                     requestStatus: "pending"
                                 })
                             }
                         })),
                         o = Ir(e + "/rejected", (function(e, t, r, a, o) {
                             return {
                                 payload: a,
                                 error: (n && n.serializeError || Qr)(e || "Rejected"),
-                                meta: Tr(jr({}, o || {}), {
+                                meta: Tr(_r({}, o || {}), {
                                     arg: r,
                                     requestId: t,
                                     rejectedWithValue: !!a,
                                     requestStatus: "rejected",
                                     aborted: "AbortError" === (null == e ? void 0 : e.name),
                                     condition: "ConditionError" === (null == e ? void 0 : e.name)
                                 })
@@ -13945,19 +13945,19 @@
             if (e === t || !(Ra(e) && Ra(t) || Array.isArray(e) && Array.isArray(t))) return t;
             for (var n = Object.keys(t), r = Object.keys(e), a = n.length === r.length, o = Array.isArray(t) ? [] : {}, i = 0, l = n; i < l.length; i++) {
                 var u = l[i];
                 o[u] = Na(e[u], t[u]), a && (a = e[u] === o[u])
             }
             return a ? e : o
         }
-        var _a = function() {
+        var ja = function() {
                 for (var e = [], t = 0; t < arguments.length; t++) e[t] = arguments[t];
                 return fetch.apply(void 0, e)
             },
-            ja = function(e) {
+            _a = function(e) {
                 return e.status >= 200 && e.status <= 299
             },
             Ta = function(e) {
                 return /ion\/(vnd\.api\+)?json/.test(e.get("content-type") || "")
             };
 
         function Da(e) {
@@ -15562,16 +15562,16 @@
                             }({
                                 queryThunk: d,
                                 mutationThunk: p,
                                 api: e,
                                 serializeQueryArgs: o,
                                 context: n
                             }),
-                            _ = N.buildInitiateQuery,
-                            j = N.buildInitiateMutation,
+                            j = N.buildInitiateQuery,
+                            _ = N.buildInitiateMutation,
                             T = N.getRunningMutationThunk,
                             D = N.getRunningMutationsThunk,
                             A = N.getRunningQueriesThunk,
                             L = N.getRunningQueryThunk,
                             M = N.getRunningOperationPromises,
                             I = N.removalWarning;
                         return go(e.util, {
@@ -15584,19 +15584,19 @@
                         }), {
                             name: bo,
                             injectEndpoint: function(t, n) {
                                 var r, a = e;
                                 null != (r = a.endpoints)[t] || (r[t] = {}), qa(n) ? go(a.endpoints[t], {
                                     name: t,
                                     select: O(t, n),
-                                    initiate: _(t, n)
+                                    initiate: j(t, n)
                                 }, g(d, t)) : n.type === Aa.mutation && go(a.endpoints[t], {
                                     name: t,
                                     select: P(),
-                                    initiate: j(t)
+                                    initiate: _(t)
                                 }, g(p, t))
                             }
                         }
                     }
                 }
             },
             Eo = (wo(), a(688)),
@@ -15622,17 +15622,17 @@
                     store: a,
                     subscription: o,
                     getServerState: i
                 } = n(), l = Po(o.addNestedSub, a.getState, i || a.getState, t, r);
                 return (0, e.useDebugValue)(l), l
             }
         }
-        const _o = No();
+        const jo = No();
         a(679), a(973);
-        const jo = {
+        const _o = {
             notify() {},
             get: () => []
         };
         const To = "undefined" != typeof window && void 0 !== window.document && void 0 !== window.document.createElement ? e.useLayoutEffect : e.useEffect;
         let Do = null;
 
         function Ao(t = Co) {
@@ -15769,15 +15769,15 @@
             ui = io(wo(), function(t) {
                 var n = {},
                     r = n.batch,
                     a = void 0 === r ? L.unstable_batchedUpdates : r,
                     o = n.useDispatch,
                     i = void 0 === o ? Io : o,
                     l = n.useSelector,
-                    u = void 0 === l ? _o : l,
+                    u = void 0 === l ? jo : l,
                     s = n.useStore,
                     c = void 0 === s ? Lo : s,
                     f = n.unstable__sideEffectsInRender,
                     d = void 0 !== f && f;
                 return {
                     name: li,
                     init: function(t, n, r) {
@@ -16021,33 +16021,33 @@
                                                 }), [h, c, v, b]),
                                                 k = E.endpointName,
                                                 C = E.data,
                                                 O = E.status,
                                                 P = E.isLoading,
                                                 R = E.isSuccess,
                                                 N = E.isError,
-                                                _ = E.error;
+                                                j = E.error;
                                             (0, e.useDebugValue)({
                                                 endpointName: k,
                                                 data: C,
                                                 status: O,
                                                 isLoading: P,
                                                 isSuccess: R,
                                                 isError: N,
-                                                error: _
+                                                error: j
                                             });
-                                            var j = (0, e.useMemo)((function() {
+                                            var _ = (0, e.useMemo)((function() {
                                                 return Jo(Ho({}, E), {
                                                     originalArgs: S,
                                                     reset: x
                                                 })
                                             }), [E, S, x]);
                                             return (0, e.useMemo)((function() {
-                                                return [g, j]
-                                            }), [g, j])
+                                                return [g, _]
+                                            }), [g, _])
                                         }
                                     },
                                     usePrefetch: function(t, r) {
                                         var a = o(),
                                             i = Go(r);
                                         return (0, e.useCallback)((function(e, r) {
                                             return a(n.util.prefetch(t, e, Ho(Ho({}, i), r)))
@@ -16138,34 +16138,34 @@
                     var n = e,
                         r = n.baseUrl,
                         a = n.prepareHeaders,
                         o = void 0 === a ? function(e) {
                             return e
                         } : a,
                         i = n.fetchFn,
-                        l = void 0 === i ? _a : i,
+                        l = void 0 === i ? ja : i,
                         u = n.paramsSerializer,
                         s = n.isJsonContentType,
                         c = void 0 === s ? Ta : s,
                         f = n.jsonContentType,
                         d = void 0 === f ? "application/json" : f,
                         p = n.jsonReplacer,
                         h = n.timeout,
                         m = n.validateStatus,
                         v = Ca(n, ["baseUrl", "prepareHeaders", "fetchFn", "paramsSerializer", "isJsonContentType", "jsonContentType", "jsonReplacer", "timeout", "validateStatus"]);
-                    return "undefined" == typeof fetch && l === _a && console.warn("Warning: `fetch` is not available. Please supply a custom `fetchFn` property to use `fetchBaseQuery` on SSR environments."),
+                    return "undefined" == typeof fetch && l === ja && console.warn("Warning: `fetch` is not available. Please supply a custom `fetchFn` property to use `fetchBaseQuery` on SSR environments."),
                         function(e, n) {
                             return Oa(t, null, (function() {
-                                var t, a, i, s, f, g, b, w, E, S, x, k, C, O, P, R, N, _, j, T, D, A, L, M, I, z, F, U, q, $, B, Q, K, W, V, H;
+                                var t, a, i, s, f, g, b, w, E, S, x, k, C, O, P, R, N, j, _, T, D, A, L, M, I, z, F, U, q, $, B, Q, K, W, V, H;
                                 return ha(this, (function(J) {
                                     switch (J.label) {
                                         case 0:
                                             return t = n.signal, a = n.getState, i = n.extra, s = n.endpoint, f = n.forced, g = n.type, E = (w = "string" == typeof e ? {
                                                 url: e
-                                            } : e).url, S = w.headers, x = void 0 === S ? new Headers(v.headers) : S, k = w.params, C = void 0 === k ? void 0 : k, O = w.responseHandler, P = void 0 === O ? "json" : O, R = w.validateStatus, N = void 0 === R ? null != m ? m : ja : R, _ = w.timeout, j = void 0 === _ ? h : _, T = Ca(w, ["url", "headers", "params", "responseHandler", "validateStatus", "timeout"]), D = xa(ka(xa({}, v), {
+                                            } : e).url, S = w.headers, x = void 0 === S ? new Headers(v.headers) : S, k = w.params, C = void 0 === k ? void 0 : k, O = w.responseHandler, P = void 0 === O ? "json" : O, R = w.validateStatus, N = void 0 === R ? null != m ? m : _a : R, j = w.timeout, _ = void 0 === j ? h : j, T = Ca(w, ["url", "headers", "params", "responseHandler", "validateStatus", "timeout"]), D = xa(ka(xa({}, v), {
                                                 signal: t
                                             }), T), x = new Headers(Da(x)), A = D, [4, o(x, {
                                                 getState: a,
                                                 extra: i,
                                                 endpoint: s,
                                                 forced: f,
                                                 type: g
@@ -16183,17 +16183,17 @@
                                                 return "" + (e = function(e) {
                                                     return e.replace(/\/$/, "")
                                                 }(e)) + n + function(e) {
                                                     return e.replace(/^\//, "")
                                                 }(t)
                                             }(r, E), z = new Request(E, D), F = z.clone(), b = {
                                                 request: F
-                                            }, q = !1, $ = j && setTimeout((function() {
+                                            }, q = !1, $ = _ && setTimeout((function() {
                                                 q = !0, n.abort()
-                                            }), j), J.label = 2;
+                                            }), _), J.label = 2;
                                         case 2:
                                             return J.trys.push([2, 4, 5, 6]), [4, l(z)];
                                         case 3:
                                             return U = J.sent(), [3, 6];
                                         case 4:
                                             return B = J.sent(), [2, {
                                                 error: {
@@ -16416,15 +16416,15 @@
                     return "string" == typeof c && (e = `${e}-${c}`), (0, l.jsx)("div", {
                         className: e,
                         children: v
                     })
                 }
                 return v
             })),
-            _i = function(t) {
+            ji = function(t) {
                 var n = t.title,
                     r = t.data,
                     a = Object.entries(r).filter((function(e) {
                         return e[0], null !== e[1]
                     }));
                 return e.createElement(Ri, null, e.createElement(Ri.Header, null, n), e.createElement(Ri.Body, null, e.createElement(Ni, {
                     hover: !0
@@ -16432,15 +16432,15 @@
                     var n = t[0],
                         r = t[1];
                     return e.createElement("tr", {
                         key: n
                     }, e.createElement("td", null, n), e.createElement("td", null, "object" == typeof r ? JSON.stringify(r) : r))
                 }))))))
             },
-            ji = function(t) {
+            _i = function(t) {
                 var n = t.title,
                     r = t.columns,
                     a = t.data,
                     o = Object.entries(a).filter((function(e) {
                         return e[0], null !== e[1]
                     }));
                 return o[0], e.createElement(Ri, null, e.createElement(Ri.Header, null, n), e.createElement(Ri.Body, null, e.createElement(Ni, {
@@ -16463,38 +16463,38 @@
                 var t = pi(),
                     n = t.data,
                     r = t.error,
                     a = t.isLoading;
                 return console.log(n, r, a, JSON.stringify(n, null, 2)), a ? e.createElement("div", null, "Loading...") : e.createElement(m, {
                     fluid: !0,
                     className: "mb-4"
-                }, e.createElement(en, null, e.createElement(nn, null, e.createElement(_i, {
+                }, e.createElement(en, null, e.createElement(nn, null, e.createElement(ji, {
                     title: "Project",
                     data: n.conf.project
-                })), e.createElement(nn, null, e.createElement(_i, {
+                })), e.createElement(nn, null, e.createElement(ji, {
                     title: "Variables",
                     data: n.conf.vars
                 }))), e.createElement(en, null, e.createElement(nn, {
                     md: 12,
                     className: "mt-4"
-                }, e.createElement(ji, {
+                }, e.createElement(_i, {
                     title: "Repos",
                     data: n.conf.repos,
                     columns: ["name", "url", "branch", "tag", "local"]
                 })), e.createElement(nn, {
                     md: 12,
                     className: "mt-3"
-                }, e.createElement(ji, {
+                }, e.createElement(_i, {
                     title: "Binaries",
                     data: n.conf.binaries,
                     columns: ["binary", "url", "extract"]
                 })), e.createElement(nn, {
                     md: 12,
                     className: "mt-3"
-                }, e.createElement(ji, {
+                }, e.createElement(_i, {
                     title: "Providers",
                     data: n.providers,
                     columns: ["name", "source", "version"]
                 }))))
             },
             Di = function() {
                 return e.createElement("h1", null, "About Page")
@@ -16527,15 +16527,15 @@
                 if (!Ar(o)) throw new Error('"reducer" is a required argument, and must be a function or an object of functions that can be passed to combineReducers');
                 t = mr(o)
             }
             var h = l;
             "function" == typeof h && (h = h(n));
             var m = yr.apply(void 0, h),
                 v = vr;
-            s && (v = Dr(jr({
+            s && (v = Dr(_r({
                 trace: !1
             }, "object" == typeof s && s)));
             var y = [m];
             return Array.isArray(p) ? y = xr([m], p) : "function" == typeof p && (y = p(y)), hr(t, f, v.apply(void 0, y))
         }({
             reducer: (Ai = {}, Ai[ci.reducerPath] = ci.reducer, Ai),
             middleware: function(e) {
@@ -16960,29 +16960,35 @@
                     className: "mb-3",
                     defaultActiveKey: "stacks"
                 }, e.createElement(ol, {
                     eventKey: "stacks",
                     title: "Stacks"
                 }, e.createElement(Ni, {
                     hover: !0
-                }, e.createElement("thead", null, e.createElement("tr", null, e.createElement("th", null, "Stack"), e.createElement("th", null, "Source"), e.createElement("th", null, "Modules"))), e.createElement("tbody", null, Object.keys(a.stacks).map((function(t) {
+                }, e.createElement("thead", null, e.createElement("tr", null, e.createElement("th", null, "Stack"), e.createElement("th", null, "Source"), e.createElement("th", null, "Modules"), e.createElement("th", null, "Operations"))), e.createElement("tbody", null, Object.keys(a.stacks).map((function(t) {
                     var n = a.stacks[t];
                     return e.createElement("tr", {
                         key: n.name
                     }, e.createElement("td", null, n.name), e.createElement("td", null, n.src), e.createElement("td", null, Object.keys(n.stack.modules).map((function(t) {
                         return e.createElement(Ii, {
                             variant: "success",
                             className: "mx-1",
                             key: t
                         }, t)
+                    }))), e.createElement("td", null, Object.keys(n.stack.operations).map((function(t) {
+                        return e.createElement(Ii, {
+                            variant: "primary",
+                            className: "mx-1",
+                            key: t
+                        }, t)
                     }))))
                 }))))), e.createElement(ol, {
                     eventKey: "vars",
                     title: "Variables"
-                }, e.createElement(_i, {
+                }, e.createElement(ji, {
                     title: "Variables",
                     data: a.vars
                 })), e.createElement(ol, {
                     eventKey: "json",
                     title: "JSON"
                 }, " ", e.createElement("code", null, e.createElement("pre", null, JSON.stringify(a, null, 2)))))))))
             };
@@ -16990,15 +16996,15 @@
             store: t,
             context: n,
             children: r,
             serverState: a
         }) {
             const o = (0, e.useMemo)((() => {
                     const e = function(e, t) {
-                        let n, r = jo;
+                        let n, r = _o;
 
                         function a() {
                             i.onStateChange && i.onStateChange()
                         }
 
                         function o() {
                             n || (n = t ? t.addNestedSub(a) : e.subscribe(a), r = function() {
@@ -17045,15 +17051,15 @@
                             },
                             handleChangeWrapper: a,
                             isSubscribed: function() {
                                 return Boolean(n)
                             },
                             trySubscribe: o,
                             tryUnsubscribe: function() {
-                                n && (n(), n = void 0, r.clear(), r = jo)
+                                n && (n(), n = void 0, r.clear(), r = _o)
                             },
                             getListeners: () => r
                         };
                         return i
                     }(t);
                     return {
                         store: t,
```

### Comparing `stackdiac-0.0.1.dev8/stackdiac/ui/bundle.js.LICENSE.txt` & `stackdiac-0.0.1.dev9/stackdiac/ui/bundle.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `stackdiac-0.0.1.dev8/PKG-INFO` & `stackdiac-0.0.1.dev9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: stackdiac
-Version: 0.0.1.dev8
+Version: 0.0.1.dev9
 Summary: 
 License: MIT
 Author: sysr9
 Author-email: 38893296+sysr9@users.noreply.github.com
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

