# Comparing `tmp/dns-crawler-1.5.8.tar.gz` & `tmp/dns-crawler-1.6.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/dns-crawler-1.5.8.tar", last modified: Tue Mar 23 13:59:34 2021, max compression
+gzip compressed data, was "dns-crawler-1.6.0.tar", last modified: Thu Apr  6 14:45:42 2023, max compression
```

## Comparing `dns-crawler-1.5.8.tar` & `dns-crawler-1.6.0.tar`

### file list

```diff
@@ -1,46 +1,46 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/
--rw-rw-rw-   0 root         (0) root         (0)      118 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/.flake8
--rw-rw-rw-   0 root         (0) root         (0)      152 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/.gitignore
--rw-rw-rw-   0 root         (0) root         (0)     2080 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/.gitlab-ci.yml
--rw-rw-rw-   0 root         (0) root         (0)    12682 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/CHANGELOG.md
--rw-rw-rw-   0 root         (0) root         (0)      667 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/Dockerfile
--rw-rw-rw-   0 root         (0) root         (0)    35061 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/LICENSE
--rw-r--r--   0 root         (0) root         (0)    23737 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)    19609 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/README.md
--rw-rw-rw-   0 root         (0) root         (0)      176 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/config.docker.yml
--rw-rw-rw-   0 root         (0) root         (0)     3920 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/config.yml
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3044 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/certificate.py
--rw-rw-rw-   0 root         (0) root         (0)     6115 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/config_loader.py
--rw-rw-rw-   0 root         (0) root         (0)     6037 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/controller.py
--rw-rw-rw-   0 root         (0) root         (0)     8112 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/crawl.py
--rw-rw-rw-   0 root         (0) root         (0)    11221 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/dns_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     2852 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/geoip_utils.py
--rw-rw-rw-   0 root         (0) root         (0)      909 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/hsts_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     2282 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/ip_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     4229 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/mail_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     2029 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/redis_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     2157 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/single.py
--rw-rw-rw-   0 root         (0) root         (0)      874 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/timestamp.py
--rw-rw-rw-   0 root         (0) root         (0)      861 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/utils.py
--rw-rw-rw-   0 root         (0) root         (0)    13191 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/web_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     1774 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/worker.py
--rw-rw-rw-   0 root         (0) root         (0)     5044 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/dns_crawler/workers.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler.egg-info/
--rw-r--r--   0 root         (0) root         (0)    23737 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      885 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      202 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)      297 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       12 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/dns_crawler.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)      297 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/requirements.txt
--rw-rw-rw-   0 root         (0) root         (0)   122671 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/result-example.json
--rw-rw-rw-   0 root         (0) root         (0)    22796 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/result-schema.json
--rw-r--r--   0 root         (0) root         (0)       38 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     2673 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-03-23 13:59:34.000000 dns-crawler-1.5.8/test/
--rw-rw-rw-   0 root         (0) root         (0)       81 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/test/config-nodns.yml
--rw-rw-rw-   0 root         (0) root         (0)      135 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/test/config-odvr.yml
--rw-rw-rw-   0 root         (0) root         (0)     1859 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/test/nic.cz.test.py
--rw-rw-rw-   0 root         (0) root         (0)      139 2021-03-23 13:56:03.000000 dns-crawler-1.5.8/update-docker-img.sh
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:45:42.009989 dns-crawler-1.6.0/
+-rw-rw-rw-   0 root         (0) root         (0)      144 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/.flake8
+-rw-rw-rw-   0 root         (0) root         (0)      152 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/.gitignore
+-rw-rw-rw-   0 root         (0) root         (0)     2147 2023-03-02 14:50:23.000000 dns-crawler-1.6.0/.gitlab-ci.yml
+-rw-rw-rw-   0 root         (0) root         (0)    14552 2023-04-06 14:39:24.000000 dns-crawler-1.6.0/CHANGELOG.md
+-rw-rw-rw-   0 root         (0) root         (0)      667 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/Dockerfile
+-rw-rw-rw-   0 root         (0) root         (0)    35061 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)    20434 2023-04-06 14:45:42.005989 dns-crawler-1.6.0/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)    19596 2023-03-02 14:50:23.000000 dns-crawler-1.6.0/README.md
+-rw-rw-rw-   0 root         (0) root         (0)      176 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/config.docker.yml
+-rw-rw-rw-   0 root         (0) root         (0)     4187 2023-03-02 14:15:34.000000 dns-crawler-1.6.0/config.yml
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:45:42.005989 dns-crawler-1.6.0/dns_crawler/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/dns_crawler/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3946 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/certificate.py
+-rw-rw-rw-   0 root         (0) root         (0)     6326 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/config_loader.py
+-rw-rw-rw-   0 root         (0) root         (0)     6612 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/controller.py
+-rw-rw-rw-   0 root         (0) root         (0)    11081 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/crawl.py
+-rw-rw-rw-   0 root         (0) root         (0)    12402 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/dns_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     2801 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/geoip_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)      909 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/hsts_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     2282 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/ip_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     4421 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/mail_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     2029 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/redis_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     2157 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/single.py
+-rw-rw-rw-   0 root         (0) root         (0)      874 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/timestamp.py
+-rw-rw-rw-   0 root         (0) root         (0)      861 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/utils.py
+-rw-rw-rw-   0 root         (0) root         (0)    16147 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/web_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     1935 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/worker.py
+-rw-rw-rw-   0 root         (0) root         (0)     5101 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/dns_crawler/workers.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:45:42.005989 dns-crawler-1.6.0/dns_crawler.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    20434 2023-04-06 14:45:41.000000 dns-crawler-1.6.0/dns_crawler.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      885 2023-04-06 14:45:41.000000 dns-crawler-1.6.0/dns_crawler.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 14:45:41.000000 dns-crawler-1.6.0/dns_crawler.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      202 2023-04-06 14:45:41.000000 dns-crawler-1.6.0/dns_crawler.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)      306 2023-04-06 14:45:41.000000 dns-crawler-1.6.0/dns_crawler.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       12 2023-04-06 14:45:41.000000 dns-crawler-1.6.0/dns_crawler.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)      305 2023-04-06 14:33:34.000000 dns-crawler-1.6.0/requirements.txt
+-rw-rw-rw-   0 root         (0) root         (0)   229038 2023-04-06 11:45:35.000000 dns-crawler-1.6.0/result-example.json
+-rw-rw-rw-   0 root         (0) root         (0)    23932 2023-04-06 11:45:35.000000 dns-crawler-1.6.0/result-schema.json
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 14:45:42.009989 dns-crawler-1.6.0/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     2733 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:45:42.005989 dns-crawler-1.6.0/test/
+-rw-rw-rw-   0 root         (0) root         (0)       81 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/test/config-nodns.yml
+-rw-rw-rw-   0 root         (0) root         (0)      135 2023-04-06 14:43:33.000000 dns-crawler-1.6.0/test/config-odvr.yml
+-rw-rw-rw-   0 root         (0) root         (0)     1861 2023-04-06 13:56:53.000000 dns-crawler-1.6.0/test/nic.cz.test.py
+-rw-rw-rw-   0 root         (0) root         (0)      139 2023-02-23 15:46:15.000000 dns-crawler-1.6.0/update-docker-img.sh
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `dns-crawler-1.5.8/.gitlab-ci.yml` & `dns-crawler-1.6.0/.gitlab-ci.yml`

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-image: python:3.7
+image: python:3.9
 
 variables:
     PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
 
 cache:
   paths:
     - .cache/pip
@@ -22,17 +22,17 @@
     - pip install flake8 flake8-quotes
   script:
     - flake8 --config=.flake8
 
 validate_result_example:
   stage: lint
   before_script:
-    - pip install -q jsonschema
+    - pip install -q check-jsonschema
   script: 
-    - jsonschema -i result-example.json result-schema.json
+    - check-jsonschema --schemafile result-schema.json result-example.json
 
 download_geoip:
   image: ubuntu
   stage: setup
   variables:
     GEOIP_ACCOUNTID: $GEOIP_ACCOUNTID
     GEOIP_KEY: $GEOIP_KEY
@@ -50,38 +50,39 @@
 
 test_odvr:
   stage: test
   dependencies:
     - download_geoip
   before_script:
     - pip install .
-    - pip install -q jsonschema
+    - pip install -q check-jsonschema
   script: 
     - export PYTHONPATH="$(pwd)"
     - cd test
     - mv config-odvr.yml config.yml
     - python nic.cz.test.py > nic.cz.json
-    - jsonschema -i nic.cz.json ../result-schema.json
+    - check-jsonschema --schemafile ../result-schema.json nic.cz.json
   artifacts:
     paths:
       - ./test/nic.cz.json
 
 test_system_dns:
   stage: test
   dependencies:
     - download_geoip
   before_script:
     - pip install .
-    - pip install -q jsonschema
+    - pip install -q check-jsonschema
   script: 
     - export PYTHONPATH="$(pwd)"
     - cd test
     - mv config-nodns.yml config.yml
     - python nic.cz.test.py > nic.cz-nodns.json
-    - jsonschema -i nic.cz-nodns.json ../result-schema.json
+    - check-jsonschema --schemafile ../result-schema.json nic.cz-nodns.json
+
   artifacts:
     paths:
       - ./test/nic.cz-nodns.json
 
 build:
   stage: build
   script:
```

### Comparing `dns-crawler-1.5.8/CHANGELOG.md` & `dns-crawler-1.6.0/CHANGELOG.md`

 * *Files 12% similar despite different names*

```diff
@@ -1,7 +1,42 @@
+## 1.6.0 (2023-04-06)
+
+- Minimal supported Python version is now 3.7
+- Updated `PyICU` dependency so it installs smoothly on distros with new sw versions (eg. Gentoo & Arch)
+- Updated `cryptography` and `pyOpenSSL` to make things work with new OpenSSL
+- Updated `RQ`, we are now using its `enqueue_many` feature instead of the old custom implementation (which was basically the same thing, but now it's upstream)
+- Updated most of other dependencies to latest stable versions
+- Less confusing error messages when Redis runs out of memory during the job queue creation
+- Configurable worker niceness (on operating systems supporting it)
+
+### DNS:
+
+- `DMARC` and `SPF` (both from `TXT` and deprecated `SPF`) records are now parsed with `checkdmarc` instead of the old custom regex/dict-based parsers
+- Added parent zone info and glue records
+- Fixed handling of NS records with CNAMES
+
+### MAIL:
+
+- DKIM records. Some common DKIM selectors are in the default config.
+- Workaround for TLSA on invalid MX records
+- Check for MTA-STS record
+- Workaround for weird Outlook domain ownership check MX records("….msv1.invalid.")
+
+### WEB:
+
+- New config option `web.paths` for fetch other URLs than just website root
+- Workaround for https://github.com/pyca/cryptography/issues/3856
+- Fix for webservers redirecting to invalid or empty URLs (eg. `HTTP 301, Location: https://www..cz/` → `urllib3.exceptions.LocationParseError`)
+- Stop trying to detect encoding for responses with empty content
+- Fixed getting TLS info from the HTTPS socket after requests/urllib internals changed
+- Fixed a bunch of other exceptions caused by weird webservers
+- Fixed binary content detection and added mimetypes with autodetection via libmagic so we don't have to trust Content-Type headers
+- IP & GeoIP is in every redirect step now
+- Added `active` (boolean) and `expires_in` (day count) for certificates
+
 ## 1.5.8 (2021-03-23)
 
 ### DNS:
 
 - Fix response truncation detection (used for retries over TCP)
 
 ## 1.5.7 (2021-02-25)
@@ -200,15 +235,15 @@
         ```yaml
         dns:
         additional:
             - SPF
             - CAA
             - LOC
         ```
-    - currently using this to get the legacy/deprecated SPF records, requested by Eda Rejthar from CSIRT (we were getting SPF just from TXTs until now, now it's doing both)
+    - currently using this to get the legacy/deprecated SPF records, requested by CSIRT (we were getting SPF just from TXTs until now, now it's doing both)
     - it's also pretty easy to plug in your own parsers for these records (we're using it for SPF, since we already got TXT SPFs with the same format)
     - it works with just the IN class records and just for the 2nd level domain, not any subdomains… at least for now
 - added `authors.bind` and `fortune` chaos txts, we'll see if it's just taking up space or if we can use it for some version fingerprinting…
 
 
 ### MAIL:
```

### Comparing `dns-crawler-1.5.8/Dockerfile` & `dns-crawler-1.6.0/Dockerfile`

 * *Files identical despite different names*

### Comparing `dns-crawler-1.5.8/LICENSE` & `dns-crawler-1.6.0/LICENSE`

 * *Files identical despite different names*

### Comparing `dns-crawler-1.5.8/PKG-INFO` & `dns-crawler-1.6.0/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,440 +1,444 @@
 Metadata-Version: 2.1
 Name: dns-crawler
-Version: 1.5.8
+Version: 1.6.0
 Summary: A crawler for getting info about DNS domains and services attached to them.
 Home-page: https://gitlab.nic.cz/adam/dns-crawler
 Author: Jiri Helebrant
 Author-email: jiri.helebrant@nic.cz
 License: UNKNOWN
 Project-URL: Operation in .CZ, https://www.csirt.cz/en/dns-crawler/
+Project-URL: CZ.NIC stats dashboard, https://stats.nic.cz/
 Project-URL: Project ADAM, https://adam.nic.cz/
-Description: # `dns-crawler`
-        
-        > A crawler for getting info about *(possibly a huge number of)* DNS domains
-        
-        [<img alt="CZ.NIC" src="https://adam.nic.cz/media/filer_public/5f/27/5f274de4-7c39-40b2-9942-ef5e7cb66d12/logo-cznic.svg" height="35">](https://www.nic.cz/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-        [<img alt="ADAM" src="https://adam.nic.cz/static/img/logo-adam.svg" height="50">](https://adam.nic.cz/)
-        
-        [![PyPI version shields.io](https://img.shields.io/pypi/v/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        [![PyPI pyversions](https://img.shields.io/pypi/pyversions/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        [![PyPI license](https://img.shields.io/pypi/l/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        [![PyPI downloads per week](https://img.shields.io/pypi/dm/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        
-        # What does it do?
-        
-        Despite the name, the crawler gets info for more services than just DNS:
-        
-        - DNS:
-          - all A/AAAA records (for the 2nd level domain and `www.` subdomain), optionally annotated with GeoIP
-          - TXT records (with SPF and DMARC parsed for easier filtering)
-          - TLSA (for the 2nd level domain and `www.` subdomain)
-          - MX
-          - DNSSEC validation
-          - nameservers:
-            - each server IP optionally annotated with GeoIP
-            - HOSTNAME.BIND, VERSION.BIND, AUTHORS.BIND and fortune (also for all IPs)
-          - users can add custom additional RRs in the config file
-        - E-mail (for every server from MX):
-          - SMTP server banners (optional, ports are configurable)
-          - TLSA records
-        - Web:
-          - HTTP status & headers (inc. parsed cookies) for ports 80 & 443 on each IP from A/AAAA records
-          - certificate info for HTTPS (optionally with an entire cert chain)
-          - webpage content (optional)
-          - everything of the above is saved for each _step_ in the redirect history – the crawler follows redirects until it gets a non-redirecting status or hits a configurable limit
-        
-        Answers from name and mail servers are cached, so the crawler shouldn't flood hosting providers with repeating queries.
-         
-        If you need to configure a firewall, the crawler connects to ports `53` (both UDP and TCP), `25` (TCP), `80` (TCP), and `443` (TCP for now, but we might add UDP with HTTP3…).
-        
-        See [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json) to get an idea what the resulting JSON looks like.
-        
-        ## How fast is it anyway?
-        
-        A single fairly modern laptop on ~50Mbps connection can crawl the entire *.cz* zone (~1.3M second level domains) overnight, give or take, using 8 workers per CPU thread.
-        
-        Since the crawler is designed to be parallel, the actual speed depends almost entirely on the worker count. And it can scale accross multiple machines almost infinitely, so should you need a million domains crawled in an hour, you can always just throw more hardware at it (see below).
-        
-        CZ.NIC uses 4 machines in production (8-core Xeon Bronze 3106, 16 GB RAM, gigabit line) and crawling the entire *.cz* zone takes under 3 hours.
-        
-        ## Installation
-        
-        Create and activate a virtual environment:
-        
-        ```bash
-        mkdir dns-crawler
-        cd dns-crawler
-        python3 -m venv .venv
-        source .venv/bin/activate
-        ```
-        
-        Install `dns-crawler`:
-        
-        ```bash
-        pip install dns-crawler
-        ```
-        
-        Depending on your OS/distro, you might need to install some system packages. On Debian/Ubuntu, `apt install libicu-dev pkg-config build-essential` should do the trick (assumung you already have python3 installed of course).
-        
-        ## Basic usage
-        
-        To run a single-threaded crawler (suitable for small domain counts), just pass a domain list:
-        
-        ```
-        $ echo -e "nic.cz\nnetmetr.cz\nroot.cz" > domain-list.txt
-        $ dns-crawler domain-list.txt > results.json
-        [2019-12-03 11:03:54] Reading domains from domain-list.txt.
-        [2019-12-03 11:03:54] Read 3 domains.
-        [2019-12-03 11:03:55] 1/3
-        [2019-12-03 11:03:55] 2/3
-        [2019-12-03 11:03:56] 3/3
-        [2019-12-03 11:03:56] Finished.
-        ```
-        
-        Results are printed to stdout – JSON for every domain, separated by `\n`:
-        
-        ```
-        $ cat results.json
-        {"domain": "nic.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
-        {"domain": "netmetr.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
-        {"domain": "root.cz", "timestamp": "2019-12-03 10:03:56", "results": {…}}
-        ```
-        
-        If you want formatted JSONs, just pipe the output through [jq](https://stedolan.github.io/jq/) or your tool of choice: `dns-crawler domain-list.txt | jq`.
-        
-        ## Multithreaded crawling
-        
-        First, you need a Redis server running & listening.
-        
-        The crawler can run with multiple threads to speed things up when you have a lot of domains to go through. Communication betweeen the controller and workers is done through Redis (this makes it easy to run workers on multiple machines if needed, see below).
-        
-        Start Redis. The exact command depends on your system. If you want to use a different machine for Redis & the crawler controller, see [CLI parameters for dns-crawler-controller](#dns-crawler-controller).
-        
-        Feed domains into queue and wait for results:
-        
-        ```
-        $ dns-crawler-controller domain-list.txt > result.json
-        ```
-        
-        (in another shell) Start workers which process the domains and return results to the controller:
-        
-        ```
-        $ dns-crawler-workers
-        ```
-        
-        Using the controller also gives you caching of repeating queries (mailserver banners and hostname.bind/version.bind for nameservers) for free.
-        
-        ### Redis configuration
-        
-        No special config needed, but increase the memory limit if you have a lot of domains to process (eg. `maxmemory 2G`). You can also disable disk snapshots to save some I/O time (comment out the `save …` lines). If you're not already using Redis for other things, read its log – there are often some recommendations for performance improvements.
-        
-        ## Results
-        
-        Results are printed to the main process' (`dns-crawler` or `dns-crawler-controller`) stdout – JSON for every domain, separated by `\n`:
-        
-        ```
-        …
-        [2019-05-03 07:38:17] 2/3
-        {"domain": "nic.cz", "timestamp": "2019-09-24T05:28:06.536991", "results": {…}}
-        …
-        ```
-        
-        The progress info with timestamp is printed to stderr, so you can save just the output easily – `dns-crawler list.txt > results`.
-        
-        A JSON schema for the output JSON is included in the repository: [`result-schema.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-schema.json), and also an example for nic.cz: [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json).
-        
-        There are several tools for schema validation, viewing, and even code generation.
-        
-        To validate a result against schema (CI is set up to do it automatically):
-        
-        ```bash
-        $ pip install jsonschema
-        $ jsonschema -i result-example.json result-schema.json # if it prints nothing, it's valid
-        ```
-        
-        Or, if you don't loathe JS, `ajv` has a much better output:
-        
-        ```bash
-        $ npm i -g ajv-cli
-        $ ajv validate -s result-schema.json -d result-example.json
-        ```
-        
-        ### Storing crawler results
-        
-        In production, CZ.NIC uses Hadoop cluster to store the results file after the crawler run is over – see a script in `utils/crawler-hadoop.sh` (pushes the results file to Hadoop and notifies a Mattermost channel).
-        
-        You can even pipe the output right to hadoop without even storing it on your disk:
-        
-        ```
-        dns-crawler-controller domain-list.txt | ssh user@hadoop-node "HADOOP_USER_NAME=… hadoop fs -put - /path/to/results.json;"
-        ```
-        
-        ### Working with the results
-        
-        - [R package for dns-crawler output processing](https://gitlab.nic.cz/adam/dnscrawler.parser)
-        
-        ## Usage in Python code
-        
-        Just import and use the `process_domain` function like so:
-        
-        ```
-        $ python
-        >>> from dns_crawler.crawl import process_domain
-        >>> result = process_domain("nic.cz")
-        >>> result
-        {'domain': 'nic.cz', 'timestamp': '2019-09-13T09:21:10.136303', 'results': { … 
-        >>>
-        >>> result["results"]["DNS_LOCAL"]["DNS_AUTH"]
-        [{'value': 'a.ns.nic.cz.'}, {'value': 'b.ns.nic.cz.'}, {'value': 'd.ns.nic.cz.'}]
-        ```
-        
-        The `process_domain` function returns Python `dict`s. If you want json, use `from dns_crawler.crawl import get_json_result` instead:
-        
-        ```
-        $ python
-        >>> from dns_crawler.crawl import get_json_result
-        >>> result = get_json_result("nic.cz")
-        >>> result
-        # same as above, just converted to JSON
-        ```
-        
-        This function just calls `crawl_domain` and converts the `dict` to JSON string. It's used by the workers, so the conversion is done by them to take some pressure off the controller process.
-        
-        
-        ## Config file
-        
-        GeoIP DB paths, DNS resolver IP(s), timeouts, and bunch of other things are read from `config.yml` in the working directory, if present.
-        
-        The default values are listed in [`config.yml`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/config.yml) with explanatory comments.
-        
-        If you're using the multi-threaded crawler (`dns-crawler-controller` & `dns-crawler-workers`), the config is loaded by the controlled and shared with the workers via Redis.
-        
-        You can override it on the worker machines if needed – just create a `config.yml` in their working dir (eg. to set different resolver IP(s) or GeoIP paths on each machine). The config is then merged – directives not defined in the worker config are loaded from the controller one (and defaults are used if the're not defined there either). But – depending on values you change – you might then get a different results from each worker machine of course.
-        
-        
-        ### GeoIP annotation
-        
-        For this to work, you need to get GeoIP databases for the crawler to use. It supports both paid and free ones ([can be downloaded here after registration](https://dev.maxmind.com/geoip/geoip2/geolite2/)).
-        
-        The crawler expects them in `/usr/share/GeoIP` (Maxmind's [geoipupdate](https://github.com/maxmind/geoipupdate) places them there by default), but that can be easily changed in a config file:
-        
-        ```yaml
-        geoip:
-          enabled: True
-          country: /path/to/GeoLite2-Country.mmdb
-          asn: /path/to/GeoLite2-ASN.mmdb
-        ```
-        
-        Using commercial (GeoIP2 Country and ISP) DBs instead of free (GeoLite2 Country and ASN) ones:
-        
-        ```yaml
-        geoip:
-          enabled: True
-          country: /usr/share/GeoIP/GeoLite2-Country.mmdb
-          #  asn: /usr/share/GeoIP/GeoLite2-ASN.mmdb  # 'asn' is the free DB
-          isp: /usr/share/GeoIP/GeoIP2-ISP.mmdb  # 'isp' is the commercial one
-        ```
-        
-        (use either absolute paths or relative to the working directory)
-        
-        `ISP` (paid) database is preferred over `ASN` (free), if both are defined. The difference is described on Maxmind's website: https://dev.maxmind.com/faq/what-is-the-difference-between-the-geoip-isp-and-organization-databases/.
-        
-        The free `GeoLite2-Country` seems to be a bit inaccurate, especially for IPv6 (it places some CZ.NIC nameservers in Ukraine etc.).
-        
-        ### Getting additional DNS resource records:
-        
-        You can easily get some additional RRs (for the 2nd level domain) which aren't included in the crawler by default:
-        
-        ```yaml
-        dns:
-          additional:
-            - SPF
-            - CAA
-            - CERT
-            - LOC
-            - SSHFP
-        ```
-        
-        See the [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types) for some ideas. Things like OPENPGPKEY won't work though, because they are intented to be used on a subdomain (generated as a hash of part of e-mail address in this case).
-        
-        You can plug a parser for the record by adding a function to the `additional_parsers` enum in `dns_utils.py`. The only one included by default is SPF (since the deprecated SPF record has the same format as SPF from TXT which the crawler is getting by default).
-        
-        ## Command line parameters
-        
-        ### dns-crawler
-        
-        ```
-        dns-crawler - a single-threaded crawler to process a small number of domains without a need for Redis
-        
-        Usage: dns-crawler <file>
-               file - plaintext domain list, one domain per line, empty lines are ignored
-        ```
-        
-        ### dns-crawler-controller
-        
-        ```
-        dns-crawler-controller - the main process controlling the job queue and printing results.
-        
-        Usage: dns-crawler-controller <file> [redis]
-               file - plaintext domain list, one domain per line, empty lines are ignored
-               redis - redis host:port:db, localhost:6379:0 by default
-        
-        Examples: dns-crawler-controller domains.txt
-                  dns-crawler-controller domains.txt 192.168.0.22:4444:0
-                  dns-crawler-controller domains.txt redis.foo.bar:7777:2
-                  dns-crawler-controller domains.txt redis.foo.bar # port 6379 and DB 0 will be used if not specified
-        ```
-        
-        The controller process uses threads (4 for each CPU core) to create the jobs faster when you give it a lot of domains (>1000× CPU core count).
-        
-        It's *much* faster on (more) modern machines – eg. i7-7600U (with HT) in a laptop does about 19k jobs/s, while server with Xeon X3430 (without HT) does just about ~7k (both using 16 threads, as they both appear as 4 core to the system).
-        
-        To cancel the process, just send a kill signal or hit `Ctrl-C` any time. The process will perform cleanup and exit.
-        
-        ### dns-crawler-workers
-        
-        ```
-        dns-crawler-workers - a process that spawns crawler workers.
-        
-        Usage: dns-crawler-workers [count] [redis]
-               count - worker count, 8 workers per CPU core by default
-               redis - redis host:port:db, localhost:6379:0 by default
-        
-        Examples: dns-crawler-workers 8
-                  dns-crawler-workers 24 192.168.0.22:4444:0
-                  dns-crawler-workers 16 redis.foo.bar:7777:2
-                  dns-crawler-workers 16 redis.foo.bar # port 6379 and DB 0 will be used if not specified
-        ```
-        
-        Trying to use more than 24 workers per CPU core will result in a warning (and countdown before it actually starts the workers):
-        
-        ```
-        $ dns-crawler-workers 999
-        Whoa. You are trying to run 999 workers on 4 CPU cores. It's easy toscale
-        across multiple machines, if you need to. See README.md for details.
-        
-        Cancel now (Ctrl-C) or have a fire extinguisher ready.
-        5 - 4 - 3 -
-        ```
-        
-        Stopping works the same way as with the controller process – `Ctrl-C` (or kill signal) will finish the current job(s) and exit.
-        
-        ## Resuming work
-        
-        Stopping the workers won't delete the jobs from Redis. So, if you stop the `dns-crawler-workers` process and then start a new one (perhaps to use different worker count…), it will pick up the unfinished jobs and continue.
-        
-        This can also be used change the worker count if it turns out to be too low or high for your machine or network:
-        
-        - to reduce the worker count, just stop the `dns-crawler-workers` process and start a new one with a new count
-        - to increase the worker count, either use the same approach, or just start a second `dns-crawler-workers` process in another shell, the worker count will just add up
-        - scaling to multiple machines works the same way, see below
-        
-        ## Running on multiple machines
-        
-        Since all communication between the controller and workers is done through Redis, it's easy to scale the crawler to any number of machines:
-        
-        ```
-        machine-1                     machine-1
-        ┬───────────────────────────┐         ┬─────────────────────┐
-        │    dns-crawler-controller │ ------- │ dns-crawler-workers │
-        │             +             │         └─────────────────────┘
-        │           redis           │
-        │             +             │
-        │        DNS resolver       │
-        └───────────────────────────┘
-                                              machine-2
-                                              ┬─────────────────────┐
-                                      ------- │ dns-crawler-workers │
-                                              └─────────────────────┘
-                                              …
-                                              …
-        
-                                              machine-n
-                                              ┬─────────────────────┐
-                                      _______ │ dns-crawler-workers │
-                                              └─────────────────────┘
-        ```
-        
-        Just tell the workers to connect to the shared Redis on the main server, eg.:
-        
-        ```
-        $ dns-crawler-workers 24 192.168.0.2:6379
-                            ^            ^
-                            24 threads   redis host
-        ```
-        
-        Make sure to run the workers with ~same Python version on these machines, otherwise you'll get `unsupported pickle protocol` errors. See the [pickle protocol versions in Python docs](https://docs.python.org/3.8/library/pickle.html#data-stream-format).
-        
-        The DNS resolver doesn't have to be on a same machine as the `dns-crawler-controller`, of course – just set it's IP in `config.yml`. The crawler is tested primarily with CZ.NIC's [Knot Resolver](https://www.knot-resolver.cz/), but should work with any sane resolver supporting DNSSEC. Systemd's `systemd-resolved` seems to be really slow though.
-        
-        Same goes for Redis, you can point both controller and workers to a separate machine running Redis (don't forget to point them to an empty DB if you're using Redis for other things than the dns-crawler, it uses `0` by default).
-        
-        ## Updating dependencies
-        
-        MaxMind updates GeoIP DBs on Tuesdays, so it may be a good idea to set a cron job to keep them fresh. More about that on [maxmind.com: Automatic Updates for GeoIP2](https://dev.maxmind.com/geoip/geoipupdate/).
-        
-        If you use multiple machines to run the workers, don't forget to update GeoIP on all of them (or set up a shared location, eg. via sshfs or nfs).
-        
-        ## Monitoring
-        
-        ### Command line
-        
-        ```
-        $ rq info
-        default      |████████████████████ 219458
-        1 queues, 219458 jobs total
-        
-        0 workers, 1 queues
-        ```
-        
-        ### Web interface
-        
-        ```
-        $ pip install rq-dashboard
-        $ rq-dashboard
-        RQ Dashboard version 0.4.0                                                 
-         * Serving Flask app "rq_dashboard.cli" (lazy loading)                            
-         * Environment: production                                                
-           WARNING: Do not use the development server in a production environment. 
-           Use a production WSGI server instead.                                          
-         * Debug mode: off                            
-         * Running on http://0.0.0.0:9181/ (Press CTRL+C to quit)
-         ```
-        
-        <a href="https://i.vgy.me/sk7zWa.png">
-        <img alt="RQ Dashboard screenshot" src="https://i.vgy.me/sk7zWa.png" width="40%">
-        </a>
-        <a href="https://i.vgy.me/4y5Zee.png">
-        <img alt="RQ Dashboard screenshot" src="https://i.vgy.me/4y5Zee.png" width="40%">
-        </a>
-        
-        ## Tests
-        
-        Some basic tests are in the `tests` directory in this repo. If you want to run them manually, take a look at the `test` stage jobs in `.gitlab-ci.yml`. Basically it just downloads free GeoIP DBs, tells the crawler to use them, and crawles some domains, checking values in JSON output. It runs the tests twice – first with the default DNS resolvers (ODVR) and then with system one(s).
-        
-        If you're looking into writing some additional tests, be aware that some Docker containers used in GitLab CI don't have IPv6 configured (even if it's working on the host machine), so checking for eg. `WEB6_80_www_VENDOR` will fail without additional setup.
-        
-        
-        ## OS support
-        
-        The crawler is developed primarily for Linux, but it should work on any OS supported by Python – at least the worker part (but the controller should work too, if you manage to get a Redis server running on your OS).
-        
-        One exception is Windows, because it [doesn't support `fork()`](https://github.com/rq/rq/issues/859), but it's possible to get it working under WSL (Windows Subsystem for Linux):
-        
-        ![win10 screenshot](https://i.vgy.me/emJjGN.png)
-        
-        …so you can turn a gaming machine into an internet crawler quite easily.
-        
-        
-        ## Bug reporting
-        
-        Please create [issues in this Gitlab repo](https://gitlab.nic.cz/adam/dns-crawler/issues).
 Keywords: crawler,dns,http,https
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: OS Independent
-Requires-Python: >=3.6
+Requires-Python: >=3.7
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# `dns-crawler`
+
+> A crawler for getting info about *(possibly a huge number of)* DNS domains
+
+[<img alt="CZ.NIC" src="https://adam.nic.cz/media/filer_public/5f/27/5f274de4-7c39-40b2-9942-ef5e7cb66d12/logo-cznic.svg" height="35">](https://www.nic.cz/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
+[<img alt="ADAM" src="https://adam.nic.cz/static/img/logo-adam.svg" height="50">](https://adam.nic.cz/)
+
+[![PyPI version shields.io](https://img.shields.io/pypi/v/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+[![PyPI license](https://img.shields.io/pypi/l/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+[![PyPI downloads per week](https://img.shields.io/pypi/dm/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+
+# What does it do?
+
+Despite the name, the crawler gets info for more services than just DNS:
+
+- DNS:
+  - all A/AAAA records (for the 2nd level domain and `www.` subdomain), optionally annotated with GeoIP
+  - TXT records (with SPF and DMARC parsed for easier filtering)
+  - TLSA (for the 2nd level domain and `www.` subdomain)
+  - MX
+  - DNSSEC validation
+  - nameservers:
+    - each server IP optionally annotated with GeoIP
+    - HOSTNAME.BIND, VERSION.BIND, AUTHORS.BIND and fortune (also for all IPs)
+  - users can add custom additional RRs in the config file
+- E-mail (for every server from MX):
+  - SMTP server banners (optional, ports are configurable)
+  - TLSA records
+- Web:
+  - HTTP status & headers (inc. parsed cookies) for ports 80 & 443 on each IP from A/AAAA records
+  - certificate info for HTTPS (optionally with an entire cert chain)
+  - webpage content (optional)
+  - everything of the above is saved for each _step_ in the redirect history – the crawler follows redirects until it gets a non-redirecting status or hits a configurable limit
+
+Answers from name and mail servers are cached, so the crawler shouldn't flood hosting providers with repeating queries.
+ 
+If you need to configure a firewall, the crawler connects to ports `53` (both UDP and TCP), `25` (TCP), `80` (TCP), and `443` (TCP for now, but we might add UDP with HTTP3…).
+
+See [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json) to get an idea what the resulting JSON looks like.
+
+## How fast is it anyway?
+
+A single fairly modern laptop on ~50Mbps connection can crawl the entire *.cz* zone (~1.3M second level domains) overnight, give or take, using 8 workers per CPU thread.
+
+Since the crawler is designed to be parallel, the actual speed depends almost entirely on the worker count. And it can scale accross multiple machines almost infinitely, so should you need a million domains crawled in an hour, you can always just throw more hardware at it (see below).
+
+CZ.NIC uses 4 machines in production (8-core Xeon Bronze 3106, 16 GB RAM, gigabit line) and crawling the entire *.cz* zone takes under 3 hours.
+
+## Installation
+
+Create and activate a virtual environment:
+
+```bash
+mkdir dns-crawler
+cd dns-crawler
+python3 -m venv .venv
+source .venv/bin/activate
+```
+
+Install `dns-crawler`:
+
+```bash
+pip install dns-crawler
+```
+
+Depending on your OS/distro, you might need to install some system packages. On Debian/Ubuntu, `apt install libicu-dev pkg-config build-essential` should do the trick (assumung you already have python3 installed of course).
+
+## Basic usage
+
+To run a single-threaded crawler (suitable for small domain counts), just pass a domain list:
+
+```
+$ echo -e "nic.cz\nnetmetr.cz\nroot.cz" > domain-list.txt
+$ dns-crawler domain-list.txt > results.json
+[2019-12-03 11:03:54] Reading domains from domain-list.txt.
+[2019-12-03 11:03:54] Read 3 domains.
+[2019-12-03 11:03:55] 1/3
+[2019-12-03 11:03:55] 2/3
+[2019-12-03 11:03:56] 3/3
+[2019-12-03 11:03:56] Finished.
+```
+
+Results are printed to stdout – JSON for every domain, separated by `\n`:
+
+```
+$ cat results.json
+{"domain": "nic.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
+{"domain": "netmetr.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
+{"domain": "root.cz", "timestamp": "2019-12-03 10:03:56", "results": {…}}
+```
+
+If you want formatted JSONs, just pipe the output through [jq](https://stedolan.github.io/jq/) or your tool of choice: `dns-crawler domain-list.txt | jq`.
+
+## Multithreaded crawling
+
+First, you need a Redis server running & listening.
+
+The crawler can run with multiple threads to speed things up when you have a lot of domains to go through. Communication betweeen the controller and workers is done through Redis (this makes it easy to run workers on multiple machines if needed, see below).
+
+Start Redis. The exact command depends on your system. If you want to use a different machine for Redis & the crawler controller, see [CLI parameters for dns-crawler-controller](#dns-crawler-controller).
+
+Feed domains into queue and wait for results:
+
+```
+$ dns-crawler-controller domain-list.txt > result.json
+```
+
+(in another shell) Start workers which process the domains and return results to the controller:
+
+```
+$ dns-crawler-workers
+```
+
+Using the controller also gives you caching of repeating queries (mailserver banners and hostname.bind/version.bind for nameservers) for free.
+
+### Redis configuration
+
+No special config needed, but increase the memory limit if you have a lot of domains to process (eg. `maxmemory 2G`). You can also disable disk snapshots to save some I/O time (comment out the `save …` lines). If you're not already using Redis for other things, read its log – there are often some recommendations for performance improvements.
+
+## Results
+
+Results are printed to the main process' (`dns-crawler` or `dns-crawler-controller`) stdout – JSON for every domain, separated by `\n`:
+
+```
+…
+[2019-05-03 07:38:17] 2/3
+{"domain": "nic.cz", "timestamp": "2019-09-24T05:28:06.536991", "results": {…}}
+…
+```
+
+The progress info with timestamp is printed to stderr, so you can save just the output easily – `dns-crawler list.txt > results`.
+
+A JSON schema for the output JSON is included in the repository: [`result-schema.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-schema.json), and also an example for nic.cz: [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json).
+
+There are several tools for schema validation, viewing, and even code generation.
+
+To validate a result against schema (CI is set up to do it automatically):
+
+```bash
+$ pip install check-jsonschema
+$ check-jsonschema --schemafile result-schema.json result-example.json
+```
+
+Or, if you don't loathe JS, `ajv` has a much better output:
+
+```bash
+$ npm i -g ajv-cli
+$ ajv validate -s result-schema.json -d result-example.json
+```
+
+### Storing crawler results
+
+In production, CZ.NIC uses Hadoop cluster to store the results file after the crawler run is over – see a script in `utils/crawler-hadoop.sh` (pushes the results file to Hadoop and notifies a Mattermost channel).
+
+You can even pipe the output right to hadoop without even storing it on your disk:
+
+```
+dns-crawler-controller domain-list.txt | ssh user@hadoop-node "HADOOP_USER_NAME=… hadoop fs -put - /path/to/results.json;"
+```
+
+### Working with the results
+
+- [R package for dns-crawler output processing](https://gitlab.nic.cz/adam/dnscrawler.parser)
+
+## Usage in Python code
+
+Just import and use the `process_domain` function like so:
+
+```
+$ python
+>>> from dns_crawler.crawl import process_domain
+>>> result = process_domain("nic.cz")
+>>> result
+{'domain': 'nic.cz', 'timestamp': '2019-09-13T09:21:10.136303', 'results': { … 
+>>>
+>>> result["results"]["DNS_LOCAL"]["DNS_AUTH"]
+[{'value': 'a.ns.nic.cz.'}, {'value': 'b.ns.nic.cz.'}, {'value': 'd.ns.nic.cz.'}]
+```
+
+The `process_domain` function returns Python `dict`s. If you want json, use `from dns_crawler.crawl import get_json_result` instead:
+
+```
+$ python
+>>> from dns_crawler.crawl import get_json_result
+>>> result = get_json_result("nic.cz")
+>>> result
+# same as above, just converted to JSON
+```
+
+This function just calls `crawl_domain` and converts the `dict` to JSON string. It's used by the workers, so the conversion is done by them to take some pressure off the controller process.
+
+
+## Config file
+
+GeoIP DB paths, DNS resolver IP(s), timeouts, and bunch of other things are read from `config.yml` in the working directory, if present.
+
+The default values are listed in [`config.yml`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/config.yml) with explanatory comments.
+
+If you're using the multi-threaded crawler (`dns-crawler-controller` & `dns-crawler-workers`), the config is loaded by the controlled and shared with the workers via Redis.
+
+You can override it on the worker machines if needed – just create a `config.yml` in their working dir (eg. to set different resolver IP(s) or GeoIP paths on each machine). The config is then merged – directives not defined in the worker config are loaded from the controller one (and defaults are used if the're not defined there either). But – depending on values you change – you might then get a different results from each worker machine of course.
+
+
+### GeoIP annotation
+
+For this to work, you need to get GeoIP databases for the crawler to use. It supports both paid and free ones ([can be downloaded here after registration](https://dev.maxmind.com/geoip/geoip2/geolite2/)).
+
+The crawler expects them in `/usr/share/GeoIP` (Maxmind's [geoipupdate](https://github.com/maxmind/geoipupdate) places them there by default), but that can be easily changed in a config file:
+
+```yaml
+geoip:
+  enabled: True
+  country: /path/to/GeoLite2-Country.mmdb
+  asn: /path/to/GeoLite2-ASN.mmdb
+```
+
+Using commercial (GeoIP2 Country and ISP) DBs instead of free (GeoLite2 Country and ASN) ones:
+
+```yaml
+geoip:
+  enabled: True
+  country: /usr/share/GeoIP/GeoLite2-Country.mmdb
+  #  asn: /usr/share/GeoIP/GeoLite2-ASN.mmdb  # 'asn' is the free DB
+  isp: /usr/share/GeoIP/GeoIP2-ISP.mmdb  # 'isp' is the commercial one
+```
+
+(use either absolute paths or relative to the working directory)
+
+`ISP` (paid) database is preferred over `ASN` (free), if both are defined. The difference is described on Maxmind's website: https://dev.maxmind.com/faq/what-is-the-difference-between-the-geoip-isp-and-organization-databases/.
+
+The free `GeoLite2-Country` seems to be a bit inaccurate, especially for IPv6 (it places some CZ.NIC nameservers in Ukraine etc.).
+
+### Getting additional DNS resource records:
+
+You can easily get some additional RRs (for the 2nd level domain) which aren't included in the crawler by default:
+
+```yaml
+dns:
+  additional:
+    - SPF
+    - CAA
+    - CERT
+    - LOC
+    - SSHFP
+```
+
+See the [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types) for some ideas. Things like OPENPGPKEY won't work though, because they are intented to be used on a subdomain (generated as a hash of part of e-mail address in this case).
+
+You can plug a parser for the record by adding a function to the `additional_parsers` enum in `dns_utils.py`. The only one included by default is SPF (since the deprecated SPF record has the same format as SPF from TXT which the crawler is getting by default).
+
+## Command line parameters
+
+### dns-crawler
+
+```
+dns-crawler - a single-threaded crawler to process a small number of domains without a need for Redis
+
+Usage: dns-crawler <file>
+       file - plaintext domain list, one domain per line, empty lines are ignored
+```
+
+### dns-crawler-controller
+
+```
+dns-crawler-controller - the main process controlling the job queue and printing results.
+
+Usage: dns-crawler-controller <file> [redis]
+       file - plaintext domain list, one domain per line, empty lines are ignored
+       redis - redis host:port:db, localhost:6379:0 by default
+
+Examples: dns-crawler-controller domains.txt
+          dns-crawler-controller domains.txt 192.168.0.22:4444:0
+          dns-crawler-controller domains.txt redis.foo.bar:7777:2
+          dns-crawler-controller domains.txt redis.foo.bar # port 6379 and DB 0 will be used if not specified
+```
+
+The controller process uses threads (4 for each CPU core) to create the jobs faster when you give it a lot of domains (>1000× CPU core count).
+
+It's *much* faster on (more) modern machines – eg. i7-7600U (with HT) in a laptop does about 19k jobs/s, while server with Xeon X3430 (without HT) does just about ~7k (both using 16 threads, as they both appear as 4 core to the system).
+
+To cancel the process, just send a kill signal or hit `Ctrl-C` any time. The process will perform cleanup and exit.
+
+### dns-crawler-workers
+
+```
+dns-crawler-workers - a process that spawns crawler workers.
+
+Usage: dns-crawler-workers [count] [redis]
+       count - worker count, 8 workers per CPU core by default
+       redis - redis host:port:db, localhost:6379:0 by default
+
+Examples: dns-crawler-workers 8
+          dns-crawler-workers 24 192.168.0.22:4444:0
+          dns-crawler-workers 16 redis.foo.bar:7777:2
+          dns-crawler-workers 16 redis.foo.bar # port 6379 and DB 0 will be used if not specified
+```
+
+Trying to use more than 24 workers per CPU core will result in a warning (and countdown before it actually starts the workers):
+
+```
+$ dns-crawler-workers 999
+Whoa. You are trying to run 999 workers on 4 CPU cores. It's easy toscale
+across multiple machines, if you need to. See README.md for details.
+
+Cancel now (Ctrl-C) or have a fire extinguisher ready.
+5 - 4 - 3 -
+```
+
+Stopping works the same way as with the controller process – `Ctrl-C` (or kill signal) will finish the current job(s) and exit.
+
+## Resuming work
+
+Stopping the workers won't delete the jobs from Redis. So, if you stop the `dns-crawler-workers` process and then start a new one (perhaps to use different worker count…), it will pick up the unfinished jobs and continue.
+
+This can also be used change the worker count if it turns out to be too low or high for your machine or network:
+
+- to reduce the worker count, just stop the `dns-crawler-workers` process and start a new one with a new count
+- to increase the worker count, either use the same approach, or just start a second `dns-crawler-workers` process in another shell, the worker count will just add up
+- scaling to multiple machines works the same way, see below
+
+## Running on multiple machines
+
+Since all communication between the controller and workers is done through Redis, it's easy to scale the crawler to any number of machines:
+
+```
+machine-1                     machine-1
+┬───────────────────────────┐         ┬─────────────────────┐
+│    dns-crawler-controller │ ------- │ dns-crawler-workers │
+│             +             │         └─────────────────────┘
+│           redis           │
+│             +             │
+│        DNS resolver       │
+└───────────────────────────┘
+                                      machine-2
+                                      ┬─────────────────────┐
+                              ------- │ dns-crawler-workers │
+                                      └─────────────────────┘
+                                      …
+                                      …
+
+                                      machine-n
+                                      ┬─────────────────────┐
+                              _______ │ dns-crawler-workers │
+                                      └─────────────────────┘
+```
+
+Just tell the workers to connect to the shared Redis on the main server, eg.:
+
+```
+$ dns-crawler-workers 24 192.168.0.2:6379
+                    ^            ^
+                    24 threads   redis host
+```
+
+Make sure to run the workers with ~same Python version on these machines, otherwise you'll get `unsupported pickle protocol` errors. See the [pickle protocol versions in Python docs](https://docs.python.org/3.8/library/pickle.html#data-stream-format).
+
+The DNS resolver doesn't have to be on a same machine as the `dns-crawler-controller`, of course – just set it's IP in `config.yml`. The crawler is tested primarily with CZ.NIC's [Knot Resolver](https://www.knot-resolver.cz/), but should work with any sane resolver supporting DNSSEC. Systemd's `systemd-resolved` seems to be really slow though.
+
+Same goes for Redis, you can point both controller and workers to a separate machine running Redis (don't forget to point them to an empty DB if you're using Redis for other things than the dns-crawler, it uses `0` by default).
+
+## Updating dependencies
+
+MaxMind updates GeoIP DBs on Tuesdays, so it may be a good idea to set a cron job to keep them fresh. More about that on [maxmind.com: Automatic Updates for GeoIP2](https://dev.maxmind.com/geoip/geoipupdate/).
+
+If you use multiple machines to run the workers, don't forget to update GeoIP on all of them (or set up a shared location, eg. via sshfs or nfs).
+
+## Monitoring
+
+### Command line
+
+```
+$ rq info
+default      |████████████████████ 219458
+1 queues, 219458 jobs total
+
+0 workers, 1 queues
+```
+
+### Web interface
+
+```
+$ pip install rq-dashboard
+$ rq-dashboard
+RQ Dashboard version 0.4.0                                                 
+ * Serving Flask app "rq_dashboard.cli" (lazy loading)                            
+ * Environment: production                                                
+   WARNING: Do not use the development server in a production environment. 
+   Use a production WSGI server instead.                                          
+ * Debug mode: off                            
+ * Running on http://0.0.0.0:9181/ (Press CTRL+C to quit)
+ ```
+
+<a href="https://i.vgy.me/sk7zWa.png">
+<img alt="RQ Dashboard screenshot" src="https://i.vgy.me/sk7zWa.png" width="40%">
+</a>
+<a href="https://i.vgy.me/4y5Zee.png">
+<img alt="RQ Dashboard screenshot" src="https://i.vgy.me/4y5Zee.png" width="40%">
+</a>
+
+## Tests
+
+Some basic tests are in the `tests` directory in this repo. If you want to run them manually, take a look at the `test` stage jobs in `.gitlab-ci.yml`. Basically it just downloads free GeoIP DBs, tells the crawler to use them, and crawles some domains, checking values in JSON output. It runs the tests twice – first with the default DNS resolvers (ODVR) and then with system one(s).
+
+If you're looking into writing some additional tests, be aware that some Docker containers used in GitLab CI don't have IPv6 configured (even if it's working on the host machine), so checking for eg. `WEB6_80_www_VENDOR` will fail without additional setup.
+
+
+## OS support
+
+The crawler is developed primarily for Linux, but it should work on any OS supported by Python – at least the worker part (but the controller should work too, if you manage to get a Redis server running on your OS).
+
+One exception is Windows, because it [doesn't support `fork()`](https://github.com/rq/rq/issues/859), but it's possible to get it working under WSL (Windows Subsystem for Linux):
+
+![win10 screenshot](https://i.vgy.me/emJjGN.png)
+
+…so you can turn a gaming machine into an internet crawler quite easily.
+
+
+## Bug reporting
+
+Please create [issues in this Gitlab repo](https://gitlab.nic.cz/adam/dns-crawler/issues).
+
```

### Comparing `dns-crawler-1.5.8/README.md` & `dns-crawler-1.6.0/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -134,16 +134,16 @@
 A JSON schema for the output JSON is included in the repository: [`result-schema.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-schema.json), and also an example for nic.cz: [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json).
 
 There are several tools for schema validation, viewing, and even code generation.
 
 To validate a result against schema (CI is set up to do it automatically):
 
 ```bash
-$ pip install jsonschema
-$ jsonschema -i result-example.json result-schema.json # if it prints nothing, it's valid
+$ pip install check-jsonschema
+$ check-jsonschema --schemafile result-schema.json result-example.json
 ```
 
 Or, if you don't loathe JS, `ajv` has a much better output:
 
 ```bash
 $ npm i -g ajv-cli
 $ ajv validate -s result-schema.json -d result-example.json
```

### Comparing `dns-crawler-1.5.8/config.yml` & `dns-crawler-1.6.0/config.yml`

 * *Files 4% similar despite different names*

```diff
@@ -9,40 +9,50 @@
     - 193.17.47.1  # https://www.nic.cz/odvr/
     - 2001:148f:ffff::1
   check_www: True  # get A/AAAA/TLSA records for the `www.` subdomain (and use them for WEB_* stuff later, too)
   auth_chaos_txt:  # CH TXT to query the domain's auth server for (eg. `authors.bind` or `fortune`)
     - hostname.bind
     - version.bind
   # add 'additional' here to get more DNS records, more about that in Readme
-  # additional:
-  #  - SPF
+  additional:
+   - SPF
+   - CSYNC
+  dkim_selectors:
+   - dkim
+   - default
+   - google
+   - sig1
+  fingerprint: True
 timeouts:
   job: 80  # seconds, overall job (one domain crawl) duration when using dns-crawler-controller, jobs will fail after that and you can retry/abort them as needed
   dns: 2  # seconds, timeout for dns queries
   http: 2  # seconds, connection timeout for HTTP(S)/TLS requests
   http_read: 5  # seconds, read timeout when saving web content
   cache: 3600  # TTL for cached responses (used for mail and name servers), they will expire after this much seconds since their last use
 mail:
-  get_banners: True  # connect to SMTP servers and save banners they send (you might want to keep it off if your ISP is touchy about higher traffic on port 25, or just to save time)
+  get_banners: False  # connect to SMTP servers and save banners they send (you might want to keep it off if your ISP is touchy about higher traffic on port 25, or just to save time)
   ports: # ports to use for TLSA records (_PORT._tcp.…) and mailserver banners
     - 25
     - 465
     - 587
+  max_ips_per_host: 4
 web:
   save_content: True  # save website content – beware, turning this on will output HUGE files for higher domain counts, especially when save_intermediate_steps is enabled as well
   save_binary: True  # save even binary content (eg. application/octet-stream) in base64 data uris
   max_redirects: 6  # follow HTTP redirrects (301, 302, …) until this limit
   user_agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36  # User-Agent header to use for HTTP(S) requests
   accept_language: en-US;q=0.9,en;q=0.8  # Accept-Language header to use for HTTP(S) requests
-  content_size_limit: 5120000  # Truncate the saved content to this number of chacters (or bytes for binary content). If you choose to use strip_html, the content is truncated _after_ that. Huge values (hunderds of MB, depending on your RAM size and number of workers) can cause UnpicklingError when reading the result from Redis.
-  max_ips_per_domain: null  # max A/AAAA records to try to get web content from for each www/nonwww–80/443-ipv4/6 combination, integer or null for unlimited. Some domains take it the extreme (> 20 records) and have broken HTTPS on webservers, so adjust HTTP and job timeouts accordingly…
+  content_size_limit: 5120000  # Truncate the saved content to this number of chacters (or bytes for binary content). Huge values (hundreds of MB, depending on your RAM size and number of workers) can cause UnpicklingError when reading the result from Redis.
+  max_ips_per_domain: null  # max A/AAAA records to try to get web content from for each www/nonwww–80/443-ipv4/6 combination. Integer, or null for unlimited. Some domains take it the extreme (> 20 records) and have broken HTTPS on webservers, so adjust HTTP and job timeouts accordingly…
   check_http: True  # Try to connect via HTTP (port 80)
   check_https: True  # Try to connect via HTTPS (port 443)
   check_ipv4: True  # Try to connect to IP(s) from A records
   check_ipv6: True  # Try to connect to IP(s) from AAAA records
   save_intermediate_steps: True  # Save intermediate redirect steps (otherwise save just the last one).
-  save_cert_chain: False # save the entire certificate chain for each HTTPS step
+  save_cert_chain: False # Save the entire certificate chain for each HTTPS step
   flatten_output: False  # If only one of www/nonwww–ipv4/ipv6–http/https combinations is left, save it directly into "WEB" field. Also save the per-ip object directly into web results if there was only one IpP(either from DNS of by setting max_ips_per_domain to 1)
+  paths: [] # Paths to fetch in addition to `/`. They will be saved in `.results.WEB_paths`. Be aware that this can create HUGE output!
 connectivity_check_ips: # IPs used for an initial connectivity check and getting a source addresses for HTTP(S) connections, you can set these to any public DNS (or anything that listens on port 53 UDP…) or `null` to disable the 4/6 protocol. These default ones are just CZ.NIC's public resolvers (CZ.NIC ODVR, https://www.nic.cz/odvr/).
   ipv4: 193.17.47.1
   ipv6: 2001:148f:ffff::1
 save_worker_hostname: False # Include the worker hostname in JSON output, might be useful for debugging or determining if you ended up on some blacklist etc. 
+worker_niceness: 10 # dns-crawler-workers launches the individual workers with nice -n N
```

### Comparing `dns-crawler-1.5.8/dns_crawler/config_loader.py` & `dns-crawler-1.6.0/dns_crawler/config_loader.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -35,31 +35,39 @@
     },
     "dns": {
         "resolvers": [
             "193.17.47.1",
             "2001:148f:ffff::1"
         ],
         "additional": [],
+        "dkim_selectors": [
+            "dkim",
+            "default",
+            "google",
+            "sig1"
+        ],
         "auth_chaos_txt": [
             "version.bind",
             "hostname.bind"
         ],
-        "check_www": True
+        "check_www": True,
+        "fingerprint": False
     },
     "timeouts": {
         "job": 80,
         "dns": 2,
         "http": 2,
         "http_read": 5,
         "mail": 2,
         "cache": 3600
     },
     "mail": {
         "get_banners": False,
-        "ports": [25, 465, 587]
+        "ports": [25, 465, 587],
+        "max_ips_per_host": 4
     },
     "web": {
         "save_content": False,
         "save_binary": True,
         "max_redirects": 6,
         "save_cert_chain": False,
         "user_agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
@@ -72,15 +80,16 @@
         "check_ipv6": True,
         "save_intermediate_steps": True
     },
     "connectivity_check_ips": {
         "ipv4": "193.17.47.1",
         "ipv6": "2001:148f:ffff::1"
     },
-    "save_worker_hostname": False
+    "save_worker_hostname": False,
+    "worker_niceness": 10
 }
 
 
 def merge_dicts(source, destination):
     for key, value in source.items():
         if isinstance(value, dict):
             node = destination.setdefault(key, {})
```

### Comparing `dns-crawler-1.5.8/dns_crawler/controller.py` & `dns-crawler-1.6.0/dns_crawler/controller.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -16,18 +16,18 @@
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 import pickle
 import sys
 from os.path import basename
 from time import sleep
+
 from redis import Redis
-from redis.exceptions import ConnectionError as RedisConnectionError
+from redis.exceptions import ConnectionError, ExecAbortError, ResponseError
 from rq import Queue
-from rq.job import Job
 from rq.registry import FinishedJobRegistry
 
 from .config_loader import default_config_filename, load_config
 from .crawl import get_json_result
 from .redis_utils import get_redis_host
 from .timestamp import timestamp
 
@@ -49,23 +49,34 @@
     sys.stderr.write(f"          {exe} domains.txt 192.168.0.22:4444:0\n")
     sys.stderr.write(f"          {exe} domains.txt redis.foo.bar:7777:2\n")
     sys.stderr.write(f"          {exe} domains.txt redis.foo.bar # port 6379 and DB 0 will be used if not specified\n")
     sys.exit(1)
 
 
 def create_jobs(domains, function, redis, queue, timeout):
-    job_count = 0
     pipe = redis.pipeline()
+    jobs = []
     for domain in domains:
-        job = Job.create(function, args=(domain,), id=domain, timeout=timeout,
-                         result_ttl=-1, connection=redis, description=domain)
-        queue.enqueue_job(job, pipeline=pipe)
-        job_count += 1
-    pipe.execute()
-    return job_count
+        jobs.append(Queue.prepare_data(function, (domain,), job_id=domain,
+                                       description=domain, timeout=timeout, result_ttl=-1))
+    queue.enqueue_many(jobs, pipeline=pipe)
+    try:
+        pipe.execute()
+    except (ExecAbortError, ResponseError):
+        sys.stderr.write("Redis reports a reponse error. ")
+        maxmemory = int(redis.config_get("maxmemory")["maxmemory"])
+        used_memory = int(redis.info()["used_memory"])
+        if maxmemory / used_memory < 1.5:
+            sys.stderr.write("Looks like it might be running out of memory:\n")
+            sys.stderr.write(f"  used:  {used_memory}\n")
+            sys.stderr.write(f"  limit: {maxmemory}\n")
+            sys.stderr.write("Try increasing the `maxmemory` config option in redis.conf.\n")
+        redis.flushdb()
+        sys.exit(1)
+    return len(jobs)
 
 
 def main():
     if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) < 2:
         print_help()
 
     try:
@@ -142,14 +153,14 @@
     except KeyboardInterrupt:
         created_count = queue.count
         sys.stderr.write(f"{timestamp()} Cancelled. Deleting {created_count} jobs…\n")
         redis.flushdb()
         sys.stderr.write(f"{timestamp()} All jobs deleted, exiting.\n")
         sys.exit(1)
 
-    except RedisConnectionError:
+    except ConnectionError:
         sys.stderr.write(f"{timestamp()} Connection to Redis lost. :(\n")
         sys.exit(1)
 
     except FileNotFoundError:
         sys.stderr.write(f"File '{filename}' does not exist.\n\n")
         print_help()
```

### Comparing `dns-crawler-1.5.8/dns_crawler/dns_utils.py` & `dns-crawler-1.6.0/dns_crawler/dns_utils.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -19,15 +19,17 @@
 import json
 import re
 
 import dns.dnssec
 import dns.name
 import dns.resolver
 
-from .geoip_utils import annotate_geoip
+import checkdmarc
+
+from .geoip_utils import geoip_single
 
 
 def get_local_resolver(config):
     dns_timeout = config["timeouts"]["dns"]
     use_custom_dns = "dns" in config and len(config["dns"]["resolvers"]) > 0
 
     local_resolver = dns.resolver.Resolver(configure=(not use_custom_dns))
@@ -135,95 +137,62 @@
             except IndexError:
                 continue
             else:
                 item["algorithm"] = dns.dnssec.algorithm_to_text(int(alg_number))
     return items
 
 
-def parse_dmarc(items, key="value"):
-    if not items:
-        return None
-    items = [item for item in items if item[key] and item[key].startswith('"v=DMARC')]
-    if len(items) == 0:
+def parse_dmarc(items, domain, key="value"):
+    if (not items) or len(items) == 0:
         return None
     parsed = []
     for item in items:
-        record = item[key].strip('"').strip(" ")
-        raw_tags = [t.split("=") for t in record.split(";") if t]
-        output = {t[0].strip(): t[1].strip() for t in raw_tags if len(t) >= 2}
-        item = {k: v for k, v in output.items() if v is not None}
-        parsed.append(item)
+        try:
+            r = checkdmarc.parse_dmarc_record(item[key], domain)
+            parsed.append(r["tags"])
+        except (checkdmarc.DMARCError) as e:
+            parsed.append({"error": str(e)})
+        except AttributeError as e:
+            parsed.append({"error": f"empty record? {str(e)}"})
     if len(parsed) == 0:
         return None
     return parsed
 
 
-def get_spf_ips(record, protocol):
-    key = f"ip{str(protocol)}:"
-    ips = [f.replace(key, "") for f in record if f.startswith(key)]
-    if len(ips) == 0:
-        return None
-    return ips
-
-
-def get_spf_includes(record):
-    key = "include:"
-    includes = [f.replace(key, "") for f in record if f.startswith(key)]
-    if len(includes) == 0:
-        return None
-    return includes
-
-
-def get_spf_rules(record):
-    return record[1:]
-
-
-def get_spf_all(record):
-    alls = [k for k in record if "all" in k]
-    if len(alls) == 0:
-        return None
-    else:
-        all = alls[-1]
-        if all == "all":
-            all = "+all"
-        return all.replace("all", "")
+def get_spf_pass_ips(parsed_record, ipv):
+    return [item["value"] for item in parsed_record["parsed"]["pass"]
+            if "mechanism" in item and item["mechanism"] == f"ip{ipv}"]
 
 
-def parse_spf(items, key="value"):
-    if not items:
-        return None
-    items = [item for item in items if item[key] and item[key].startswith('"v=spf')]
-    if len(items) == 0:
+def parse_spf(items, domain, key="value"):
+    if (not items) or len(items) == 0:
         return None
     parsed = []
-    for item in items.copy():
-        output = {}
-        record = re.sub(r" +", " ", item[key].strip('"')).split(" ")
-        kvs = [k for k in record if "=" in k]
-        for kv in kvs:
-            data = kv.split("=")
-            output[data[0]] = data[1]
-        output["rules"] = get_spf_rules(record)
-        output["ip4"] = get_spf_ips(record, 4)
-        output["ip6"] = get_spf_ips(record, 6)
-        output["include"] = get_spf_includes(record)
-        output["all"] = get_spf_all(record)
-        item = {k: v for k, v in output.items() if v is not None}
-        parsed.append(item)
+    for item in items:
+        try:
+            r = checkdmarc.parse_spf_record(item[key], domain)
+            if "pass" in r["parsed"]:
+                r["parsed"]["ip4"] = get_spf_pass_ips(r, 4)
+                r["parsed"]["ip6"] = get_spf_pass_ips(r, 6)
+            parsed.append(r["parsed"])
+        except checkdmarc.SPFError as e:
+            parsed.append({"error": str(e)})
+        except AttributeError as e:
+            parsed.append({"error": f"empty record? {str(e)}"})
     if len(parsed) == 0:
         return None
     return parsed
 
 
 def parse_tlsa(items, key="value"):
     if not items:
         return None
     parsed = []
     for item in items:
-        if not item[key]:
+        if key not in item or item[key] is None:
             continue
         output = {}
         fields = item[key].split(" ")
         output["usage"] = int(fields[0])
         output["selector"] = int(fields[1])
         output["matchingtype"] = int(fields[2])
         output["data"] = fields[3]
@@ -259,35 +228,86 @@
             answers_l.append(str(answer).replace('"', ""))
         result = {"value": answers_l}
     except Exception as e:
         result = {"value": None, "error": str(e)}
     return result
 
 
-def get_ns_info(ip, chaosrecords, geoip_dbs, timeout, cache_timeout, redis):
+def fingerprint_ns(ip, domain, timeout):
+    NSECs = [dns.rdatatype.NSEC, dns.rdatatype.NSEC3]
+    try:
+        r = dns.query.tcp(dns.message.make_query(f"does-not-exist\x00does-not-exist.{domain}",
+                          dns.rdatatype.A, want_dnssec=True), ip, timeout=timeout)
+    except (EOFError,
+            OSError,
+            TimeoutError,
+            dns.exception.Timeout,
+            dns.query.BadResponse,
+            dns.exception.FormError,
+            ConnectionRefusedError) as e:
+        return {
+            "error": str(e)
+        }
+    types = []
+    for item in r.authority:
+        types.append(item.rdtype)
+    guess = None
+    if r.rcode() == dns.rcode.SERVFAIL:
+        guess = "PowerDNS"
+    if r.rcode() == dns.rcode.NXDOMAIN and len(types) > 1:
+        if (r.authority[0].rdtype == dns.rdatatype.SOA
+           and r.authority[1].rdtype in NSECs):
+            guess = "Knot DNS"
+        if (r.authority[0].rdtype == dns.rdatatype.SOA
+           and r.authority[1].rdtype == dns.rdatatype.RRSIG
+           and r.authority[1].covers == dns.rdatatype.SOA
+           and r.authority[2].rdtype in NSECs
+           and r.authority[3].covers == r.authority[2].rdtype):
+            guess = "BIND"
+        if (types[0] in NSECs
+           and r.authority[1].covers == r.authority[0].rdtype
+           and r.authority[-2].rdtype == dns.rdatatype.SOA
+           and r.authority[-1].covers == r.authority[-2].rdtype):
+            guess = "NSD"
+    return {
+        "guess": guess,
+        "answer": r.to_text()
+    }
+
+
+def get_ns_info(ip, domain, chaosrecords, geoip_dbs, timeout, cache_timeout, fingerprint_enabled, redis):
     cache_key = f"cache-ns-{ip['value']}"
     if redis is not None:
         cached = redis.get(cache_key)
         if cached is not None:
             redis.expire(cache_key, cache_timeout)
             return json.loads(cached.decode("utf-8"))
     if ip["value"] is None:
         return None
-    geoip = annotate_geoip([ip], geoip_dbs)[0]
+    geoip = geoip_single(ip["value"], geoip_dbs)
     result = {
         "ip": ip["value"],
-        "geoip": geoip["geoip"] if "geoip" in geoip else None
+        "geoip": geoip,
     }
+    if fingerprint_enabled:
+        result["fingerprint"] = fingerprint_ns(ip["value"], domain, timeout)
     for record in chaosrecords:
         result[record.replace(".", "")] = get_chaostxt(ip["value"], record, timeout)
     if redis is not None:
         redis.set(cache_key, json.dumps(result), ex=cache_timeout)
     return result
 
 
+def get_dkim(domain, selectors, resolver):
+    result = {}
+    for selector in selectors:
+        result[selector] = get_record(selector + "._domainkey." + domain, "TXT", resolver)
+    return result
+
+
 def value_from_record(record, data):
     return re.sub(r".*" + re.escape(record) + " ", "", data)
 
 
 def get_record(domain_name, record, resolver, protocol="udp", cname_count=None):
     results = []
     domain = dns.name.from_text(domain_name)
@@ -327,14 +347,16 @@
                 results.append({
                     "cname": cname_domain,
                     "value": None
                 })
         if item.rdtype == dns.rdatatype.from_text(record) and "cname" in results[-1]:
             for line in str(item).split("\n"):
                 results.append({"value": value_from_record(record, line), "from_cname": str(item.name)})
+    for item in response.additional:
+        results.append({"additional": str(item)})
     if len(results) > 0:
         return results
     else:
         return None
 
 
 additional_parsers = {
```

### Comparing `dns-crawler-1.5.8/dns_crawler/geoip_utils.py` & `dns-crawler-1.6.0/dns_crawler/geoip_utils.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -12,16 +12,15 @@
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
-from os import path, getcwd
-
+from os import getcwd, path
 from sys import stderr
 
 import geoip2.database
 
 from .ip_utils import is_valid_ip_address
 
 
@@ -51,30 +50,34 @@
             geoip_asn = geoip2.database.Reader(db_path)
         except FileNotFoundError:
             stderr.write(f"GeoIP ASN DB cannot be found in '{db_path}'. Disabling.\n")
 
     return (geoip_country, geoip_isp, geoip_asn)
 
 
-def annotate_geoip(items, dbs, key="value"):
+def geoip_single(ip, dbs):
     geoip_country, geoip_isp, geoip_asn = dbs
+    try:
+        result = {}
+        if geoip_country:
+            country = geoip_country.country(ip).country
+            result["country"] = country.iso_code
+        if geoip_isp:
+            isp = geoip_isp.isp(ip)
+        if geoip_asn and not geoip_isp:
+            isp = geoip_asn.asn(ip)
+        if geoip_asn or geoip_isp:
+            result["org"] = isp.autonomous_system_organization
+            result["asn"] = isp.autonomous_system_number
+    except Exception as e:
+        result["error"] = str(e)
+    return result
+
+
+def annotate_geoip(items, dbs, key="value"):
     if items:
         for item in items:
             ip = item[key]
             if not is_valid_ip_address(ip):
                 continue
-            try:
-                result = {}
-                if geoip_country:
-                    country = geoip_country.country(ip).country
-                    result["country"] = country.iso_code
-                if geoip_isp:
-                    isp = geoip_isp.isp(ip)
-                if geoip_asn and not geoip_isp:
-                    isp = geoip_asn.asn(ip)
-                if geoip_asn or geoip_isp:
-                    result["org"] = isp.autonomous_system_organization
-                    result["asn"] = isp.autonomous_system_number
-            except Exception as e:
-                result["error"] = str(e)
-            item["geoip"] = result
+            item["geoip"] = geoip_single(ip, dbs)
     return items
```

### Comparing `dns-crawler-1.5.8/dns_crawler/hsts_utils.py` & `dns-crawler-1.6.0/dns_crawler/hsts_utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
```

### Comparing `dns-crawler-1.5.8/dns_crawler/ip_utils.py` & `dns-crawler-1.6.0/dns_crawler/ip_utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
```

### Comparing `dns-crawler-1.5.8/dns_crawler/mail_utils.py` & `dns-crawler-1.6.0/dns_crawler/mail_utils.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -17,16 +17,16 @@
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 
 import json
 import socket
 
 from .dns_utils import get_record, parse_tlsa
-from .ip_utils import is_valid_ipv4_address, is_valid_ipv6_address
 from .geoip_utils import annotate_geoip
+from .ip_utils import is_valid_ipv4_address, is_valid_ipv6_address
 
 
 def get_smtp_banner(host_ip, port, timeout):
     result = {}
     if is_valid_ipv4_address(host_ip):
         inet = socket.AF_INET
     elif is_valid_ipv6_address(host_ip):
@@ -35,22 +35,22 @@
         return None
     try:
         s = socket.socket(inet, socket.SOCK_STREAM)
         s.settimeout(timeout)
         s.connect((host_ip, port))
         banner = s.recv(1024).decode().replace("\r\n", "")
         result["banner"] = banner
+        s.close()
     except Exception as e:
         result["error"] = str(e)
-    s.close()
     return result
 
 
 def get_mailserver_info(host, ports, geoip_dbs, timeout, get_banners, cache_timeout,
-                        resolver, redis, source_ipv4, source_ipv6):
+                        resolver, redis, source_ipv4, source_ipv6, max_ips_per_host):
     cache_key_host = f"cache-mail-host-{host}"
     if redis is not None:
         cached_host = redis.get(cache_key_host)
         if cached_host is not None:
             redis.expire(cache_key_host, cache_timeout)
             return json.loads(cached_host.decode("utf-8"))
     result = {}
@@ -64,15 +64,17 @@
             host_ip4s = get_record(host, "A", resolver) or []
             host_ip6s = get_record(host, "AAAA", resolver) or []
             host_ips = host_ip4s + host_ip6s
         if source_ipv4 and not source_ipv6:
             host_ips = get_record(host, "A", resolver) or []
         if source_ipv6 and not source_ipv4:
             host_ips = get_record(host, "AAAA", resolver) or []
-        for host_ip in host_ips:
+        for host_ip in host_ips[:max_ips_per_host]:
+            if "value" not in host_ip:
+                continue
             host_ip = host_ip["value"]
             cache_key_ip = f"cache-mail-ip-{host_ip}"
             if redis is not None:
                 cached_ip = redis.get(cache_key_ip)
                 if cached_ip is not None:
                     redis.expire(cache_key_ip, cache_timeout)
                     result["banners"].append(json.loads(cached_ip.decode("utf-8")))
@@ -89,18 +91,19 @@
         annotate_geoip(result["banners"], geoip_dbs, "ip")
     if redis is not None:
         redis.set(cache_key_host, json.dumps(result), ex=cache_timeout)
     return result
 
 
 def get_mx_info(mx_records, ports, geoip_dbs, timeout, get_banners, cache_timeout,
-                resolver, redis, source_ipv4, source_ipv6):
+                resolver, redis, source_ipv4, source_ipv6, max_ips_per_host):
     results = []
     if not mx_records:
         return None
     for mx in mx_records:
         if mx and mx["value"]:
             host = mx["value"].split(" ")[-1]
             if host and host != ".":
                 results.append(get_mailserver_info(host, ports, geoip_dbs, timeout, get_banners,
-                                                   cache_timeout, resolver, redis, source_ipv4, source_ipv6))
+                                                   cache_timeout, resolver, redis, source_ipv4, source_ipv6,
+                                                   max_ips_per_host))
     return results
```

### Comparing `dns-crawler-1.5.8/dns_crawler/redis_utils.py` & `dns-crawler-1.6.0/dns_crawler/redis_utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
```

### Comparing `dns-crawler-1.5.8/dns_crawler/single.py` & `dns-crawler-1.6.0/dns_crawler/single.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
```

### Comparing `dns-crawler-1.5.8/dns_crawler/timestamp.py` & `dns-crawler-1.6.0/dns_crawler/timestamp.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
```

### Comparing `dns-crawler-1.5.8/dns_crawler/utils.py` & `dns-crawler-1.6.0/dns_crawler/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
```

### Comparing `dns-crawler-1.5.8/dns_crawler/web_utils.py` & `dns-crawler-1.6.0/dns_crawler/web_utils.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -16,32 +16,35 @@
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 import base64
 import re
 from itertools import takewhile
 from urllib.parse import unquote, urljoin, urlparse
+from time import time
 
+import cert_human
+from dns_crawler.geoip_utils import geoip_single
+import icu
 import idna
 import requests
 import urllib3
-
-import cert_human
-import icu
 from forcediphttpsadapter.adapters import ForcedIPHTTPSAdapter
 from requests_toolbelt.adapters.source import SourceAddressAdapter
 
 from .certificate import parse_cert
 from .ip_utils import is_valid_ipv6_address
 
 urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 cert_human.enable_urllib3_patch()
 
 fallback_encodings = ["windows-1250", "iso-8859-2", "windows-1252"]
 
+CHUNK_SIZE = 10240
+
 
 class CrawlerAdapter(SourceAddressAdapter, ForcedIPHTTPSAdapter):
     pass
 
 
 def create_request_headers(domain, user_agent, accept_language):
     if not domain:
@@ -57,14 +60,15 @@
             host = None
     return {
         "Host": host,
         "Upgrade-Insecure-Requests": "1",
         "User-Agent": user_agent,
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
         "Accept-Encoding": "gzip, deflate",
+        "Connection": "Keep-Alive",
         "Accept-Language": accept_language,
     }
 
 
 def parse_alt_svc(header):
     result = {}
     for pair in [i.split(";")[0].replace('"', "") for i in re.findall(r"[a-zA-Z0-9-]+=[^,]+", header)]:
@@ -101,29 +105,14 @@
 header_parsers = {
     "alt-svc": parse_alt_svc,
     "strict-transport-security": parse_hsts,
     "content-length": parse_content_length
 }
 
 
-def headers_look_like_binary(headers):
-    if "content-type" in headers:
-        if ((headers["content-type"].startswith("application/")
-             and (headers["content-type"] != "application/json" or "xml" not in headers["content-type"])
-             )
-                or headers["content-type"].startswith("audio/")
-                or headers["content-type"].startswith("video/")
-                or (headers["content-type"].startswith("image/") and "svg" not in headers["content-type"])
-                or headers["content-type"].startswith("font/")):
-            return True
-    if "accept-range" in headers and headers["accept-range"] == "bytes":
-        return True
-    return False
-
-
 def emsg(e):
     if isinstance(e, (requests.exceptions.Timeout, requests.exceptions.ConnectTimeout)):
         msg = "timeout"
     else:
         msg = str(e)
     return msg
 
@@ -149,78 +138,155 @@
                 return (None, None)
             else:
                 next_encoding = fallback_encodings[fallback_encodings.index(forced_encoding) + 1]
                 return autodetect_encoding(data, forced_encoding=next_encoding)
     return (data, encoding)
 
 
-def get_webserver_info(domain, ips, config, source_ip, ipv6=False, tls=False):
+def get_webserver_info(domain, ips, config, source_ip, geoip_dbs, path="/", ipv6=False, tls=False):
     if not ips or len(ips) < 1:
         return None
     http_timeout = (config["timeouts"]["http"], config["timeouts"]["http_read"])
     save_content = config["web"]["save_content"]
     save_binary = config["web"]["save_binary"]
     content_size_limit = config["web"]["content_size_limit"]
     max_redirects = config["web"]["max_redirects"]
     protocol = "https" if tls else "http"
-    path = "/"
     results = []
     ip_index = 0
     for entry in ips:
         ip_index += 1
         if config["web"]["max_ips_per_domain"] is not None and ip_index > config["web"]["max_ips_per_domain"]:
             break
         ip = entry["value"]
         if ip is None:
             continue
         s1 = requests.session()
         s2 = requests.session()
         s1.mount("https://", CrawlerAdapter(dest_ip=ip, source_address=source_ip))
         s2.mount("https://", SourceAddressAdapter(source_address=source_ip))
         s2.mount("http://", SourceAddressAdapter(source_address=source_ip))
-        headers = create_request_headers(domain, config["web"]["user_agent"], config["web"]["accept_language"])
+
+        headers = create_request_headers(domain,
+                                         config["web"]["user_agent"],
+                                         config["web"]["accept_language"])
+        first = {}
         try:
+            content_bytes = []
             if protocol == "https":
                 url = f"{protocol}://{domain}{path}"
-                r = s1.get(url, allow_redirects=False,
-                           verify=False, stream=True, timeout=http_timeout, headers=headers)
+                first["r"] = s1.get(url,
+                                    allow_redirects=False,
+                                    verify=False,
+                                    stream=True,
+                                    timeout=http_timeout,
+                                    headers=headers)
+                try:
+                    first["ip"] = first["r"].raw._connection.sock.socket.getpeername()[0]
+                except AttributeError:
+                    first["ip"] = None
+                try:
+                    first["tls"] = {
+                        "version": str(first["r"].raw._fp.fp.raw._sock.connection.get_protocol_version_name()),
+                        "cipher_bits": int(first["r"].raw._fp.fp.raw._sock.connection.get_cipher_bits()),
+                        "cipher_name": str(first["r"].raw._fp.fp.raw._sock.connection.get_cipher_name())
+                    }
+                except AttributeError:
+                    pass
+                chunk_len = 0
+                start_time = time()
+                for chunk in first["r"].iter_content(CHUNK_SIZE):
+                    chunk_len += CHUNK_SIZE
+                    content_bytes.append(chunk)
+                    if chunk_len > content_size_limit or time() - start_time > config["timeouts"]["http_read"]:
+                        first["r"].close()
             else:
                 if ipv6:
                     host = f"[{ip}]"
                 else:
                     host = ip
                 url = f"{protocol}://{host}{path}"
-                r = s2.get(url,
-                           allow_redirects=False, stream=True, timeout=http_timeout, headers=headers)
+                first["r"] = s2.get(url,
+                                    allow_redirects=False,
+                                    stream=True,
+                                    timeout=http_timeout,
+                                    headers=headers)
+                try:
+                    first["ip"] = first["r"].raw._connection.sock.socket.getpeername()[0]
+                except AttributeError:
+                    first["ip"] = None
+                chunk_len = 0
+                start_time = time()
+                for chunk in first["r"].iter_content(CHUNK_SIZE):
+                    chunk_len += CHUNK_SIZE
+                    content_bytes.append(chunk)
+                    if chunk_len > content_size_limit or time() - start_time > config["timeouts"]["http_read"]:
+                        first["r"].close()
         except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout,
-                ValueError, UnicodeDecodeError) as e:
+                ValueError, AttributeError, UnicodeDecodeError,
+                requests.exceptions.ContentDecodingError,
+                requests.exceptions.ChunkedEncodingError) as e:
             if isinstance(e, AttributeError):
                 pass
             else:
                 results.append({
                     "ip": ip,
                     "error": emsg(e)
                 })
                 continue
+        first["url"] = url
         redirect_count = 0
-        history = [{"r": r, "url": url}]
+        history = [first]
         while "r" in history[-1] and history[-1]["r"].is_redirect:
-            url = urljoin(history[-1]["url"], history[-1]["r"].headers["location"])
+            content_bytes = []
+            location = history[-1]["r"].headers["location"]
+            url = urljoin(history[-1]["url"], location)
             h = {
                 "url": url
             }
+            if location == "":
+                h["e"] = "Empty Location header in previous step"
             try:
-                h["r"] = s1.get(url, verify=False, allow_redirects=False, stream=True, timeout=http_timeout,
-                                headers=create_request_headers(urlparse(url).hostname, config["web"]["user_agent"],
-                                                               config["web"]["accept_language"]))
+                h["r"] = s1.get(url,
+                                verify=False,
+                                allow_redirects=False,
+                                stream=True,
+                                timeout=http_timeout,
+                                headers=create_request_headers(urlparse(url).hostname,
+                                                               config["web"]["user_agent"],
+                                                               config["web"]["accept_language"])
+                                )
+                try:
+                    h["ip"] = h["r"].raw._connection.sock.socket.getpeername()[0]
+                except AttributeError:
+                    h["ip"] = None
+                try:
+                    h["tls"] = {
+                        "version": h["r"].raw._fp.fp.raw._sock.connection.get_protocol_version_name(),
+                        "cipher_bits": h["r"].raw._fp.fp.raw._sock.connection.get_cipher_bits(),
+                        "cipher_name": h["r"].raw._fp.fp.raw._sock.connection.get_cipher_name()
+                    }
+                except AttributeError:
+                    h["tls"] = None
+                chunk_len = 0
+                start_time = time()
+                for chunk in h["r"].iter_content(CHUNK_SIZE):
+                    chunk_len += CHUNK_SIZE
+                    content_bytes.append(chunk)
+                    if chunk_len > content_size_limit or time() - start_time > config["timeouts"]["http_read"]:
+                        h["r"].close()
             except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout,
-                    requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema, UnicodeError) as e:
+                    requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema,
+                    requests.exceptions.ContentDecodingError, requests.exceptions.ChunkedEncodingError,
+                    UnicodeError, ValueError) as e:
                 h["e"] = emsg(e)
             except requests.exceptions.InvalidHeader as e:
-                h["e"] = f"Invalid Location header: '{url}' - {emsg(e)}"
+                h["e"] = f"Invalid Location header in previous step. '{url}' - {emsg(e)}"
+            except urllib3.exceptions.LocationParseError as e:
+                h["e"] = emsg(e)
             history.append(h)
             redirect_count = redirect_count + 1
             if redirect_count >= max_redirects:
                 break
 
         steps = []
         for (i, h) in enumerate(history):
@@ -258,66 +324,65 @@
                 elif key in header_parsers:
                     headers[key] = header_parsers[key](v)
                 else:
                     headers[key] = v
             step["headers"] = headers
             if i == 0:
                 step["ip"] = ip
+            else:
+                step["ip"] = h["ip"]
+            step["geoip"] = geoip_single(step["ip"], geoip_dbs) if step["ip"] else None
             step["url"] = step["url"].replace(f"//{ip}/", f"//{domain}/").replace(f"//[{ip}]/", f"//{domain}/")
             if step_tls:
-                if h["r"].raw._fp.fp:
-                    if hasattr(h["r"].raw._fp.fp.raw._sock, "connection"):
-                        step["tls"] = {
-                            "version": h["r"].raw._fp.fp.raw._sock.connection.get_protocol_version_name(),
-                            "cipher_bits": h["r"].raw._fp.fp.raw._sock.connection.get_cipher_bits(),
-                            "cipher_name": h["r"].raw._fp.fp.raw._sock.connection.get_cipher_name()
-                        }
+                if "tls" in h:
+                    step["tls"] = h["tls"]
                 if config["web"]["save_cert_chain"]:
                     if h["r"].raw.peer_cert_chain:
                         cert_chain = []
                         for cert in h["r"].raw.peer_cert_chain:
                             cert_chain.append(parse_cert(cert.to_cryptography()))
                         step["cert"] = cert_chain
                 else:
                     if h["r"].raw.peer_cert:
                         step["cert"] = [parse_cert(h["r"].raw.peer_cert.to_cryptography())]
             if save_content:
+                import magic
                 detected_encoding = None
-                content = None
-                content_is_binary = headers_look_like_binary(step["headers"])
+                content = b"".join(content_bytes)
+                f = magic.Magic(uncompress=True, mime=True, mime_encoding=True)
+                mimetype = f.from_buffer(content).split("; ")
+                content_is_binary = mimetype[1] == "charset=binary"
 
                 try:
                     if content_is_binary:
                         if save_binary:
-                            for chunk in h["r"].iter_content(content_size_limit):
-                                content = f"data:{step['headers']['content-type']};base64,"\
-                                        f"{base64.b64encode(chunk).decode()}"
-                                break
+                            content = f"data:{mimetype[0]};base64,"\
+                                      f"{base64.b64encode(content).decode()}"
                     else:
                         try:
-                            content, detected_encoding = autodetect_encoding(h["r"].content)
+                            content, detected_encoding = autodetect_encoding(content)
                         except (requests.exceptions.ChunkedEncodingError,
                                 requests.exceptions.ContentDecodingError) as e:
                             results.append({
                                 "ip": ip,
                                 "error": emsg(e)
                             })
                             continue
                 except requests.exceptions.ConnectionError:
                     content = None
                 if content == "":
                     content = None
-                if content and not content_is_binary:
-                    if len(content) > content_size_limit:
-                        content = content[:content_size_limit]
+                if content is None:
+                    detected_encoding = None
                 step["content"] = content
                 if content_is_binary:
                     step["content_is_binary"] = True
                 if detected_encoding is not None:
                     step["detected_encoding"] = detected_encoding.lower()
+                step["detected_mimetype"] = mimetype[0]
             h["r"].close()
             steps.append(step)
 
         result = {
             "ip": ip,
             "redirect_count": redirect_count
         }
```

### Comparing `dns-crawler-1.5.8/dns_crawler/worker.py` & `dns-crawler-1.6.0/dns_crawler/worker.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -15,40 +15,48 @@
 
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 import logging
 import sys
 from os.path import basename
+from os import nice
+
 from redis import Redis
 from rq import Connection, Worker
 
 from .crawl import process_domain, get_json_result  # noqa F401
 
 logger = logging.getLogger("rq.worker")
 
 
 def print_help():
     exe = basename(sys.argv[0])
     sys.stderr.write(f"{exe} - a single worker process\n\n")
     sys.stderr.write("While it's possible to run it directly, it's meant to be used by dns-crawler-workers.\n")
-    sys.stderr.write(f"Usage: {exe} <redis_host> <redis_port> <redis_db> <worker_name>\n")
+    sys.stderr.write(f"Usage: {exe} <redis_host> <redis_port> <redis_db> <worker_name> <worker_niceness>\n")
     sys.exit(1)
 
 
 class CrawlerWorker(Worker):
     log_result_lifespan = False
     log_job_description = False
 
 
 def main():
-    if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) != 5:
+    if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) < 5:
         print_help()
 
     redis_host = sys.argv[1]
     redis_port = sys.argv[2]
     redis_db = sys.argv[3]
+    try:
+        niceness = int(sys.argv[5])
+    except (IndexError, ValueError):
+        niceness = 0
+
+    nice(niceness)
 
     with Connection(Redis(host=redis_host, port=redis_port, db=redis_db)):
         q = ["default"]
         w = CrawlerWorker(q, name=sys.argv[4])
         w.work(burst=True)
```

### Comparing `dns-crawler-1.5.8/dns_crawler/workers.py` & `dns-crawler-1.6.0/dns_crawler/workers.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -106,15 +106,16 @@
     commands = []
 
     for n in range(worker_count):
         commands.append(["dns-crawler-worker",
                          redis_host[0],
                          str(redis_host[1]),
                          str(redis_host[2]),
-                         f"{hostname}-{n+1}"
+                         f"{hostname}-{n+1}",
+                         str(config["worker_niceness"])
                          ])
 
     while redis.get("locked") == b"1":
         try:
             sys.stderr.write(f"{timestamp()} Waiting for the controller to unlock the queue.\n")
             sleep(5)
         except KeyboardInterrupt:
```

### Comparing `dns-crawler-1.5.8/dns_crawler.egg-info/PKG-INFO` & `dns-crawler-1.6.0/dns_crawler.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,440 +1,444 @@
 Metadata-Version: 2.1
 Name: dns-crawler
-Version: 1.5.8
+Version: 1.6.0
 Summary: A crawler for getting info about DNS domains and services attached to them.
 Home-page: https://gitlab.nic.cz/adam/dns-crawler
 Author: Jiri Helebrant
 Author-email: jiri.helebrant@nic.cz
 License: UNKNOWN
 Project-URL: Operation in .CZ, https://www.csirt.cz/en/dns-crawler/
+Project-URL: CZ.NIC stats dashboard, https://stats.nic.cz/
 Project-URL: Project ADAM, https://adam.nic.cz/
-Description: # `dns-crawler`
-        
-        > A crawler for getting info about *(possibly a huge number of)* DNS domains
-        
-        [<img alt="CZ.NIC" src="https://adam.nic.cz/media/filer_public/5f/27/5f274de4-7c39-40b2-9942-ef5e7cb66d12/logo-cznic.svg" height="35">](https://www.nic.cz/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-        [<img alt="ADAM" src="https://adam.nic.cz/static/img/logo-adam.svg" height="50">](https://adam.nic.cz/)
-        
-        [![PyPI version shields.io](https://img.shields.io/pypi/v/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        [![PyPI pyversions](https://img.shields.io/pypi/pyversions/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        [![PyPI license](https://img.shields.io/pypi/l/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        [![PyPI downloads per week](https://img.shields.io/pypi/dm/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
-        
-        # What does it do?
-        
-        Despite the name, the crawler gets info for more services than just DNS:
-        
-        - DNS:
-          - all A/AAAA records (for the 2nd level domain and `www.` subdomain), optionally annotated with GeoIP
-          - TXT records (with SPF and DMARC parsed for easier filtering)
-          - TLSA (for the 2nd level domain and `www.` subdomain)
-          - MX
-          - DNSSEC validation
-          - nameservers:
-            - each server IP optionally annotated with GeoIP
-            - HOSTNAME.BIND, VERSION.BIND, AUTHORS.BIND and fortune (also for all IPs)
-          - users can add custom additional RRs in the config file
-        - E-mail (for every server from MX):
-          - SMTP server banners (optional, ports are configurable)
-          - TLSA records
-        - Web:
-          - HTTP status & headers (inc. parsed cookies) for ports 80 & 443 on each IP from A/AAAA records
-          - certificate info for HTTPS (optionally with an entire cert chain)
-          - webpage content (optional)
-          - everything of the above is saved for each _step_ in the redirect history – the crawler follows redirects until it gets a non-redirecting status or hits a configurable limit
-        
-        Answers from name and mail servers are cached, so the crawler shouldn't flood hosting providers with repeating queries.
-         
-        If you need to configure a firewall, the crawler connects to ports `53` (both UDP and TCP), `25` (TCP), `80` (TCP), and `443` (TCP for now, but we might add UDP with HTTP3…).
-        
-        See [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json) to get an idea what the resulting JSON looks like.
-        
-        ## How fast is it anyway?
-        
-        A single fairly modern laptop on ~50Mbps connection can crawl the entire *.cz* zone (~1.3M second level domains) overnight, give or take, using 8 workers per CPU thread.
-        
-        Since the crawler is designed to be parallel, the actual speed depends almost entirely on the worker count. And it can scale accross multiple machines almost infinitely, so should you need a million domains crawled in an hour, you can always just throw more hardware at it (see below).
-        
-        CZ.NIC uses 4 machines in production (8-core Xeon Bronze 3106, 16 GB RAM, gigabit line) and crawling the entire *.cz* zone takes under 3 hours.
-        
-        ## Installation
-        
-        Create and activate a virtual environment:
-        
-        ```bash
-        mkdir dns-crawler
-        cd dns-crawler
-        python3 -m venv .venv
-        source .venv/bin/activate
-        ```
-        
-        Install `dns-crawler`:
-        
-        ```bash
-        pip install dns-crawler
-        ```
-        
-        Depending on your OS/distro, you might need to install some system packages. On Debian/Ubuntu, `apt install libicu-dev pkg-config build-essential` should do the trick (assumung you already have python3 installed of course).
-        
-        ## Basic usage
-        
-        To run a single-threaded crawler (suitable for small domain counts), just pass a domain list:
-        
-        ```
-        $ echo -e "nic.cz\nnetmetr.cz\nroot.cz" > domain-list.txt
-        $ dns-crawler domain-list.txt > results.json
-        [2019-12-03 11:03:54] Reading domains from domain-list.txt.
-        [2019-12-03 11:03:54] Read 3 domains.
-        [2019-12-03 11:03:55] 1/3
-        [2019-12-03 11:03:55] 2/3
-        [2019-12-03 11:03:56] 3/3
-        [2019-12-03 11:03:56] Finished.
-        ```
-        
-        Results are printed to stdout – JSON for every domain, separated by `\n`:
-        
-        ```
-        $ cat results.json
-        {"domain": "nic.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
-        {"domain": "netmetr.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
-        {"domain": "root.cz", "timestamp": "2019-12-03 10:03:56", "results": {…}}
-        ```
-        
-        If you want formatted JSONs, just pipe the output through [jq](https://stedolan.github.io/jq/) or your tool of choice: `dns-crawler domain-list.txt | jq`.
-        
-        ## Multithreaded crawling
-        
-        First, you need a Redis server running & listening.
-        
-        The crawler can run with multiple threads to speed things up when you have a lot of domains to go through. Communication betweeen the controller and workers is done through Redis (this makes it easy to run workers on multiple machines if needed, see below).
-        
-        Start Redis. The exact command depends on your system. If you want to use a different machine for Redis & the crawler controller, see [CLI parameters for dns-crawler-controller](#dns-crawler-controller).
-        
-        Feed domains into queue and wait for results:
-        
-        ```
-        $ dns-crawler-controller domain-list.txt > result.json
-        ```
-        
-        (in another shell) Start workers which process the domains and return results to the controller:
-        
-        ```
-        $ dns-crawler-workers
-        ```
-        
-        Using the controller also gives you caching of repeating queries (mailserver banners and hostname.bind/version.bind for nameservers) for free.
-        
-        ### Redis configuration
-        
-        No special config needed, but increase the memory limit if you have a lot of domains to process (eg. `maxmemory 2G`). You can also disable disk snapshots to save some I/O time (comment out the `save …` lines). If you're not already using Redis for other things, read its log – there are often some recommendations for performance improvements.
-        
-        ## Results
-        
-        Results are printed to the main process' (`dns-crawler` or `dns-crawler-controller`) stdout – JSON for every domain, separated by `\n`:
-        
-        ```
-        …
-        [2019-05-03 07:38:17] 2/3
-        {"domain": "nic.cz", "timestamp": "2019-09-24T05:28:06.536991", "results": {…}}
-        …
-        ```
-        
-        The progress info with timestamp is printed to stderr, so you can save just the output easily – `dns-crawler list.txt > results`.
-        
-        A JSON schema for the output JSON is included in the repository: [`result-schema.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-schema.json), and also an example for nic.cz: [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json).
-        
-        There are several tools for schema validation, viewing, and even code generation.
-        
-        To validate a result against schema (CI is set up to do it automatically):
-        
-        ```bash
-        $ pip install jsonschema
-        $ jsonschema -i result-example.json result-schema.json # if it prints nothing, it's valid
-        ```
-        
-        Or, if you don't loathe JS, `ajv` has a much better output:
-        
-        ```bash
-        $ npm i -g ajv-cli
-        $ ajv validate -s result-schema.json -d result-example.json
-        ```
-        
-        ### Storing crawler results
-        
-        In production, CZ.NIC uses Hadoop cluster to store the results file after the crawler run is over – see a script in `utils/crawler-hadoop.sh` (pushes the results file to Hadoop and notifies a Mattermost channel).
-        
-        You can even pipe the output right to hadoop without even storing it on your disk:
-        
-        ```
-        dns-crawler-controller domain-list.txt | ssh user@hadoop-node "HADOOP_USER_NAME=… hadoop fs -put - /path/to/results.json;"
-        ```
-        
-        ### Working with the results
-        
-        - [R package for dns-crawler output processing](https://gitlab.nic.cz/adam/dnscrawler.parser)
-        
-        ## Usage in Python code
-        
-        Just import and use the `process_domain` function like so:
-        
-        ```
-        $ python
-        >>> from dns_crawler.crawl import process_domain
-        >>> result = process_domain("nic.cz")
-        >>> result
-        {'domain': 'nic.cz', 'timestamp': '2019-09-13T09:21:10.136303', 'results': { … 
-        >>>
-        >>> result["results"]["DNS_LOCAL"]["DNS_AUTH"]
-        [{'value': 'a.ns.nic.cz.'}, {'value': 'b.ns.nic.cz.'}, {'value': 'd.ns.nic.cz.'}]
-        ```
-        
-        The `process_domain` function returns Python `dict`s. If you want json, use `from dns_crawler.crawl import get_json_result` instead:
-        
-        ```
-        $ python
-        >>> from dns_crawler.crawl import get_json_result
-        >>> result = get_json_result("nic.cz")
-        >>> result
-        # same as above, just converted to JSON
-        ```
-        
-        This function just calls `crawl_domain` and converts the `dict` to JSON string. It's used by the workers, so the conversion is done by them to take some pressure off the controller process.
-        
-        
-        ## Config file
-        
-        GeoIP DB paths, DNS resolver IP(s), timeouts, and bunch of other things are read from `config.yml` in the working directory, if present.
-        
-        The default values are listed in [`config.yml`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/config.yml) with explanatory comments.
-        
-        If you're using the multi-threaded crawler (`dns-crawler-controller` & `dns-crawler-workers`), the config is loaded by the controlled and shared with the workers via Redis.
-        
-        You can override it on the worker machines if needed – just create a `config.yml` in their working dir (eg. to set different resolver IP(s) or GeoIP paths on each machine). The config is then merged – directives not defined in the worker config are loaded from the controller one (and defaults are used if the're not defined there either). But – depending on values you change – you might then get a different results from each worker machine of course.
-        
-        
-        ### GeoIP annotation
-        
-        For this to work, you need to get GeoIP databases for the crawler to use. It supports both paid and free ones ([can be downloaded here after registration](https://dev.maxmind.com/geoip/geoip2/geolite2/)).
-        
-        The crawler expects them in `/usr/share/GeoIP` (Maxmind's [geoipupdate](https://github.com/maxmind/geoipupdate) places them there by default), but that can be easily changed in a config file:
-        
-        ```yaml
-        geoip:
-          enabled: True
-          country: /path/to/GeoLite2-Country.mmdb
-          asn: /path/to/GeoLite2-ASN.mmdb
-        ```
-        
-        Using commercial (GeoIP2 Country and ISP) DBs instead of free (GeoLite2 Country and ASN) ones:
-        
-        ```yaml
-        geoip:
-          enabled: True
-          country: /usr/share/GeoIP/GeoLite2-Country.mmdb
-          #  asn: /usr/share/GeoIP/GeoLite2-ASN.mmdb  # 'asn' is the free DB
-          isp: /usr/share/GeoIP/GeoIP2-ISP.mmdb  # 'isp' is the commercial one
-        ```
-        
-        (use either absolute paths or relative to the working directory)
-        
-        `ISP` (paid) database is preferred over `ASN` (free), if both are defined. The difference is described on Maxmind's website: https://dev.maxmind.com/faq/what-is-the-difference-between-the-geoip-isp-and-organization-databases/.
-        
-        The free `GeoLite2-Country` seems to be a bit inaccurate, especially for IPv6 (it places some CZ.NIC nameservers in Ukraine etc.).
-        
-        ### Getting additional DNS resource records:
-        
-        You can easily get some additional RRs (for the 2nd level domain) which aren't included in the crawler by default:
-        
-        ```yaml
-        dns:
-          additional:
-            - SPF
-            - CAA
-            - CERT
-            - LOC
-            - SSHFP
-        ```
-        
-        See the [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types) for some ideas. Things like OPENPGPKEY won't work though, because they are intented to be used on a subdomain (generated as a hash of part of e-mail address in this case).
-        
-        You can plug a parser for the record by adding a function to the `additional_parsers` enum in `dns_utils.py`. The only one included by default is SPF (since the deprecated SPF record has the same format as SPF from TXT which the crawler is getting by default).
-        
-        ## Command line parameters
-        
-        ### dns-crawler
-        
-        ```
-        dns-crawler - a single-threaded crawler to process a small number of domains without a need for Redis
-        
-        Usage: dns-crawler <file>
-               file - plaintext domain list, one domain per line, empty lines are ignored
-        ```
-        
-        ### dns-crawler-controller
-        
-        ```
-        dns-crawler-controller - the main process controlling the job queue and printing results.
-        
-        Usage: dns-crawler-controller <file> [redis]
-               file - plaintext domain list, one domain per line, empty lines are ignored
-               redis - redis host:port:db, localhost:6379:0 by default
-        
-        Examples: dns-crawler-controller domains.txt
-                  dns-crawler-controller domains.txt 192.168.0.22:4444:0
-                  dns-crawler-controller domains.txt redis.foo.bar:7777:2
-                  dns-crawler-controller domains.txt redis.foo.bar # port 6379 and DB 0 will be used if not specified
-        ```
-        
-        The controller process uses threads (4 for each CPU core) to create the jobs faster when you give it a lot of domains (>1000× CPU core count).
-        
-        It's *much* faster on (more) modern machines – eg. i7-7600U (with HT) in a laptop does about 19k jobs/s, while server with Xeon X3430 (without HT) does just about ~7k (both using 16 threads, as they both appear as 4 core to the system).
-        
-        To cancel the process, just send a kill signal or hit `Ctrl-C` any time. The process will perform cleanup and exit.
-        
-        ### dns-crawler-workers
-        
-        ```
-        dns-crawler-workers - a process that spawns crawler workers.
-        
-        Usage: dns-crawler-workers [count] [redis]
-               count - worker count, 8 workers per CPU core by default
-               redis - redis host:port:db, localhost:6379:0 by default
-        
-        Examples: dns-crawler-workers 8
-                  dns-crawler-workers 24 192.168.0.22:4444:0
-                  dns-crawler-workers 16 redis.foo.bar:7777:2
-                  dns-crawler-workers 16 redis.foo.bar # port 6379 and DB 0 will be used if not specified
-        ```
-        
-        Trying to use more than 24 workers per CPU core will result in a warning (and countdown before it actually starts the workers):
-        
-        ```
-        $ dns-crawler-workers 999
-        Whoa. You are trying to run 999 workers on 4 CPU cores. It's easy toscale
-        across multiple machines, if you need to. See README.md for details.
-        
-        Cancel now (Ctrl-C) or have a fire extinguisher ready.
-        5 - 4 - 3 -
-        ```
-        
-        Stopping works the same way as with the controller process – `Ctrl-C` (or kill signal) will finish the current job(s) and exit.
-        
-        ## Resuming work
-        
-        Stopping the workers won't delete the jobs from Redis. So, if you stop the `dns-crawler-workers` process and then start a new one (perhaps to use different worker count…), it will pick up the unfinished jobs and continue.
-        
-        This can also be used change the worker count if it turns out to be too low or high for your machine or network:
-        
-        - to reduce the worker count, just stop the `dns-crawler-workers` process and start a new one with a new count
-        - to increase the worker count, either use the same approach, or just start a second `dns-crawler-workers` process in another shell, the worker count will just add up
-        - scaling to multiple machines works the same way, see below
-        
-        ## Running on multiple machines
-        
-        Since all communication between the controller and workers is done through Redis, it's easy to scale the crawler to any number of machines:
-        
-        ```
-        machine-1                     machine-1
-        ┬───────────────────────────┐         ┬─────────────────────┐
-        │    dns-crawler-controller │ ------- │ dns-crawler-workers │
-        │             +             │         └─────────────────────┘
-        │           redis           │
-        │             +             │
-        │        DNS resolver       │
-        └───────────────────────────┘
-                                              machine-2
-                                              ┬─────────────────────┐
-                                      ------- │ dns-crawler-workers │
-                                              └─────────────────────┘
-                                              …
-                                              …
-        
-                                              machine-n
-                                              ┬─────────────────────┐
-                                      _______ │ dns-crawler-workers │
-                                              └─────────────────────┘
-        ```
-        
-        Just tell the workers to connect to the shared Redis on the main server, eg.:
-        
-        ```
-        $ dns-crawler-workers 24 192.168.0.2:6379
-                            ^            ^
-                            24 threads   redis host
-        ```
-        
-        Make sure to run the workers with ~same Python version on these machines, otherwise you'll get `unsupported pickle protocol` errors. See the [pickle protocol versions in Python docs](https://docs.python.org/3.8/library/pickle.html#data-stream-format).
-        
-        The DNS resolver doesn't have to be on a same machine as the `dns-crawler-controller`, of course – just set it's IP in `config.yml`. The crawler is tested primarily with CZ.NIC's [Knot Resolver](https://www.knot-resolver.cz/), but should work with any sane resolver supporting DNSSEC. Systemd's `systemd-resolved` seems to be really slow though.
-        
-        Same goes for Redis, you can point both controller and workers to a separate machine running Redis (don't forget to point them to an empty DB if you're using Redis for other things than the dns-crawler, it uses `0` by default).
-        
-        ## Updating dependencies
-        
-        MaxMind updates GeoIP DBs on Tuesdays, so it may be a good idea to set a cron job to keep them fresh. More about that on [maxmind.com: Automatic Updates for GeoIP2](https://dev.maxmind.com/geoip/geoipupdate/).
-        
-        If you use multiple machines to run the workers, don't forget to update GeoIP on all of them (or set up a shared location, eg. via sshfs or nfs).
-        
-        ## Monitoring
-        
-        ### Command line
-        
-        ```
-        $ rq info
-        default      |████████████████████ 219458
-        1 queues, 219458 jobs total
-        
-        0 workers, 1 queues
-        ```
-        
-        ### Web interface
-        
-        ```
-        $ pip install rq-dashboard
-        $ rq-dashboard
-        RQ Dashboard version 0.4.0                                                 
-         * Serving Flask app "rq_dashboard.cli" (lazy loading)                            
-         * Environment: production                                                
-           WARNING: Do not use the development server in a production environment. 
-           Use a production WSGI server instead.                                          
-         * Debug mode: off                            
-         * Running on http://0.0.0.0:9181/ (Press CTRL+C to quit)
-         ```
-        
-        <a href="https://i.vgy.me/sk7zWa.png">
-        <img alt="RQ Dashboard screenshot" src="https://i.vgy.me/sk7zWa.png" width="40%">
-        </a>
-        <a href="https://i.vgy.me/4y5Zee.png">
-        <img alt="RQ Dashboard screenshot" src="https://i.vgy.me/4y5Zee.png" width="40%">
-        </a>
-        
-        ## Tests
-        
-        Some basic tests are in the `tests` directory in this repo. If you want to run them manually, take a look at the `test` stage jobs in `.gitlab-ci.yml`. Basically it just downloads free GeoIP DBs, tells the crawler to use them, and crawles some domains, checking values in JSON output. It runs the tests twice – first with the default DNS resolvers (ODVR) and then with system one(s).
-        
-        If you're looking into writing some additional tests, be aware that some Docker containers used in GitLab CI don't have IPv6 configured (even if it's working on the host machine), so checking for eg. `WEB6_80_www_VENDOR` will fail without additional setup.
-        
-        
-        ## OS support
-        
-        The crawler is developed primarily for Linux, but it should work on any OS supported by Python – at least the worker part (but the controller should work too, if you manage to get a Redis server running on your OS).
-        
-        One exception is Windows, because it [doesn't support `fork()`](https://github.com/rq/rq/issues/859), but it's possible to get it working under WSL (Windows Subsystem for Linux):
-        
-        ![win10 screenshot](https://i.vgy.me/emJjGN.png)
-        
-        …so you can turn a gaming machine into an internet crawler quite easily.
-        
-        
-        ## Bug reporting
-        
-        Please create [issues in this Gitlab repo](https://gitlab.nic.cz/adam/dns-crawler/issues).
 Keywords: crawler,dns,http,https
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: OS Independent
-Requires-Python: >=3.6
+Requires-Python: >=3.7
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# `dns-crawler`
+
+> A crawler for getting info about *(possibly a huge number of)* DNS domains
+
+[<img alt="CZ.NIC" src="https://adam.nic.cz/media/filer_public/5f/27/5f274de4-7c39-40b2-9942-ef5e7cb66d12/logo-cznic.svg" height="35">](https://www.nic.cz/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
+[<img alt="ADAM" src="https://adam.nic.cz/static/img/logo-adam.svg" height="50">](https://adam.nic.cz/)
+
+[![PyPI version shields.io](https://img.shields.io/pypi/v/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+[![PyPI license](https://img.shields.io/pypi/l/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+[![PyPI downloads per week](https://img.shields.io/pypi/dm/dns-crawler.svg)](https://pypi.python.org/pypi/dns-crawler/)
+
+# What does it do?
+
+Despite the name, the crawler gets info for more services than just DNS:
+
+- DNS:
+  - all A/AAAA records (for the 2nd level domain and `www.` subdomain), optionally annotated with GeoIP
+  - TXT records (with SPF and DMARC parsed for easier filtering)
+  - TLSA (for the 2nd level domain and `www.` subdomain)
+  - MX
+  - DNSSEC validation
+  - nameservers:
+    - each server IP optionally annotated with GeoIP
+    - HOSTNAME.BIND, VERSION.BIND, AUTHORS.BIND and fortune (also for all IPs)
+  - users can add custom additional RRs in the config file
+- E-mail (for every server from MX):
+  - SMTP server banners (optional, ports are configurable)
+  - TLSA records
+- Web:
+  - HTTP status & headers (inc. parsed cookies) for ports 80 & 443 on each IP from A/AAAA records
+  - certificate info for HTTPS (optionally with an entire cert chain)
+  - webpage content (optional)
+  - everything of the above is saved for each _step_ in the redirect history – the crawler follows redirects until it gets a non-redirecting status or hits a configurable limit
+
+Answers from name and mail servers are cached, so the crawler shouldn't flood hosting providers with repeating queries.
+ 
+If you need to configure a firewall, the crawler connects to ports `53` (both UDP and TCP), `25` (TCP), `80` (TCP), and `443` (TCP for now, but we might add UDP with HTTP3…).
+
+See [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json) to get an idea what the resulting JSON looks like.
+
+## How fast is it anyway?
+
+A single fairly modern laptop on ~50Mbps connection can crawl the entire *.cz* zone (~1.3M second level domains) overnight, give or take, using 8 workers per CPU thread.
+
+Since the crawler is designed to be parallel, the actual speed depends almost entirely on the worker count. And it can scale accross multiple machines almost infinitely, so should you need a million domains crawled in an hour, you can always just throw more hardware at it (see below).
+
+CZ.NIC uses 4 machines in production (8-core Xeon Bronze 3106, 16 GB RAM, gigabit line) and crawling the entire *.cz* zone takes under 3 hours.
+
+## Installation
+
+Create and activate a virtual environment:
+
+```bash
+mkdir dns-crawler
+cd dns-crawler
+python3 -m venv .venv
+source .venv/bin/activate
+```
+
+Install `dns-crawler`:
+
+```bash
+pip install dns-crawler
+```
+
+Depending on your OS/distro, you might need to install some system packages. On Debian/Ubuntu, `apt install libicu-dev pkg-config build-essential` should do the trick (assumung you already have python3 installed of course).
+
+## Basic usage
+
+To run a single-threaded crawler (suitable for small domain counts), just pass a domain list:
+
+```
+$ echo -e "nic.cz\nnetmetr.cz\nroot.cz" > domain-list.txt
+$ dns-crawler domain-list.txt > results.json
+[2019-12-03 11:03:54] Reading domains from domain-list.txt.
+[2019-12-03 11:03:54] Read 3 domains.
+[2019-12-03 11:03:55] 1/3
+[2019-12-03 11:03:55] 2/3
+[2019-12-03 11:03:56] 3/3
+[2019-12-03 11:03:56] Finished.
+```
+
+Results are printed to stdout – JSON for every domain, separated by `\n`:
+
+```
+$ cat results.json
+{"domain": "nic.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
+{"domain": "netmetr.cz", "timestamp": "2019-12-03 10:03:55", "results": {…}}
+{"domain": "root.cz", "timestamp": "2019-12-03 10:03:56", "results": {…}}
+```
+
+If you want formatted JSONs, just pipe the output through [jq](https://stedolan.github.io/jq/) or your tool of choice: `dns-crawler domain-list.txt | jq`.
+
+## Multithreaded crawling
+
+First, you need a Redis server running & listening.
+
+The crawler can run with multiple threads to speed things up when you have a lot of domains to go through. Communication betweeen the controller and workers is done through Redis (this makes it easy to run workers on multiple machines if needed, see below).
+
+Start Redis. The exact command depends on your system. If you want to use a different machine for Redis & the crawler controller, see [CLI parameters for dns-crawler-controller](#dns-crawler-controller).
+
+Feed domains into queue and wait for results:
+
+```
+$ dns-crawler-controller domain-list.txt > result.json
+```
+
+(in another shell) Start workers which process the domains and return results to the controller:
+
+```
+$ dns-crawler-workers
+```
+
+Using the controller also gives you caching of repeating queries (mailserver banners and hostname.bind/version.bind for nameservers) for free.
+
+### Redis configuration
+
+No special config needed, but increase the memory limit if you have a lot of domains to process (eg. `maxmemory 2G`). You can also disable disk snapshots to save some I/O time (comment out the `save …` lines). If you're not already using Redis for other things, read its log – there are often some recommendations for performance improvements.
+
+## Results
+
+Results are printed to the main process' (`dns-crawler` or `dns-crawler-controller`) stdout – JSON for every domain, separated by `\n`:
+
+```
+…
+[2019-05-03 07:38:17] 2/3
+{"domain": "nic.cz", "timestamp": "2019-09-24T05:28:06.536991", "results": {…}}
+…
+```
+
+The progress info with timestamp is printed to stderr, so you can save just the output easily – `dns-crawler list.txt > results`.
+
+A JSON schema for the output JSON is included in the repository: [`result-schema.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-schema.json), and also an example for nic.cz: [`result-example.json`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/result-example.json).
+
+There are several tools for schema validation, viewing, and even code generation.
+
+To validate a result against schema (CI is set up to do it automatically):
+
+```bash
+$ pip install check-jsonschema
+$ check-jsonschema --schemafile result-schema.json result-example.json
+```
+
+Or, if you don't loathe JS, `ajv` has a much better output:
+
+```bash
+$ npm i -g ajv-cli
+$ ajv validate -s result-schema.json -d result-example.json
+```
+
+### Storing crawler results
+
+In production, CZ.NIC uses Hadoop cluster to store the results file after the crawler run is over – see a script in `utils/crawler-hadoop.sh` (pushes the results file to Hadoop and notifies a Mattermost channel).
+
+You can even pipe the output right to hadoop without even storing it on your disk:
+
+```
+dns-crawler-controller domain-list.txt | ssh user@hadoop-node "HADOOP_USER_NAME=… hadoop fs -put - /path/to/results.json;"
+```
+
+### Working with the results
+
+- [R package for dns-crawler output processing](https://gitlab.nic.cz/adam/dnscrawler.parser)
+
+## Usage in Python code
+
+Just import and use the `process_domain` function like so:
+
+```
+$ python
+>>> from dns_crawler.crawl import process_domain
+>>> result = process_domain("nic.cz")
+>>> result
+{'domain': 'nic.cz', 'timestamp': '2019-09-13T09:21:10.136303', 'results': { … 
+>>>
+>>> result["results"]["DNS_LOCAL"]["DNS_AUTH"]
+[{'value': 'a.ns.nic.cz.'}, {'value': 'b.ns.nic.cz.'}, {'value': 'd.ns.nic.cz.'}]
+```
+
+The `process_domain` function returns Python `dict`s. If you want json, use `from dns_crawler.crawl import get_json_result` instead:
+
+```
+$ python
+>>> from dns_crawler.crawl import get_json_result
+>>> result = get_json_result("nic.cz")
+>>> result
+# same as above, just converted to JSON
+```
+
+This function just calls `crawl_domain` and converts the `dict` to JSON string. It's used by the workers, so the conversion is done by them to take some pressure off the controller process.
+
+
+## Config file
+
+GeoIP DB paths, DNS resolver IP(s), timeouts, and bunch of other things are read from `config.yml` in the working directory, if present.
+
+The default values are listed in [`config.yml`](https://gitlab.nic.cz/adam/dns-crawler/-/blob/master/config.yml) with explanatory comments.
+
+If you're using the multi-threaded crawler (`dns-crawler-controller` & `dns-crawler-workers`), the config is loaded by the controlled and shared with the workers via Redis.
+
+You can override it on the worker machines if needed – just create a `config.yml` in their working dir (eg. to set different resolver IP(s) or GeoIP paths on each machine). The config is then merged – directives not defined in the worker config are loaded from the controller one (and defaults are used if the're not defined there either). But – depending on values you change – you might then get a different results from each worker machine of course.
+
+
+### GeoIP annotation
+
+For this to work, you need to get GeoIP databases for the crawler to use. It supports both paid and free ones ([can be downloaded here after registration](https://dev.maxmind.com/geoip/geoip2/geolite2/)).
+
+The crawler expects them in `/usr/share/GeoIP` (Maxmind's [geoipupdate](https://github.com/maxmind/geoipupdate) places them there by default), but that can be easily changed in a config file:
+
+```yaml
+geoip:
+  enabled: True
+  country: /path/to/GeoLite2-Country.mmdb
+  asn: /path/to/GeoLite2-ASN.mmdb
+```
+
+Using commercial (GeoIP2 Country and ISP) DBs instead of free (GeoLite2 Country and ASN) ones:
+
+```yaml
+geoip:
+  enabled: True
+  country: /usr/share/GeoIP/GeoLite2-Country.mmdb
+  #  asn: /usr/share/GeoIP/GeoLite2-ASN.mmdb  # 'asn' is the free DB
+  isp: /usr/share/GeoIP/GeoIP2-ISP.mmdb  # 'isp' is the commercial one
+```
+
+(use either absolute paths or relative to the working directory)
+
+`ISP` (paid) database is preferred over `ASN` (free), if both are defined. The difference is described on Maxmind's website: https://dev.maxmind.com/faq/what-is-the-difference-between-the-geoip-isp-and-organization-databases/.
+
+The free `GeoLite2-Country` seems to be a bit inaccurate, especially for IPv6 (it places some CZ.NIC nameservers in Ukraine etc.).
+
+### Getting additional DNS resource records:
+
+You can easily get some additional RRs (for the 2nd level domain) which aren't included in the crawler by default:
+
+```yaml
+dns:
+  additional:
+    - SPF
+    - CAA
+    - CERT
+    - LOC
+    - SSHFP
+```
+
+See the [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types) for some ideas. Things like OPENPGPKEY won't work though, because they are intented to be used on a subdomain (generated as a hash of part of e-mail address in this case).
+
+You can plug a parser for the record by adding a function to the `additional_parsers` enum in `dns_utils.py`. The only one included by default is SPF (since the deprecated SPF record has the same format as SPF from TXT which the crawler is getting by default).
+
+## Command line parameters
+
+### dns-crawler
+
+```
+dns-crawler - a single-threaded crawler to process a small number of domains without a need for Redis
+
+Usage: dns-crawler <file>
+       file - plaintext domain list, one domain per line, empty lines are ignored
+```
+
+### dns-crawler-controller
+
+```
+dns-crawler-controller - the main process controlling the job queue and printing results.
+
+Usage: dns-crawler-controller <file> [redis]
+       file - plaintext domain list, one domain per line, empty lines are ignored
+       redis - redis host:port:db, localhost:6379:0 by default
+
+Examples: dns-crawler-controller domains.txt
+          dns-crawler-controller domains.txt 192.168.0.22:4444:0
+          dns-crawler-controller domains.txt redis.foo.bar:7777:2
+          dns-crawler-controller domains.txt redis.foo.bar # port 6379 and DB 0 will be used if not specified
+```
+
+The controller process uses threads (4 for each CPU core) to create the jobs faster when you give it a lot of domains (>1000× CPU core count).
+
+It's *much* faster on (more) modern machines – eg. i7-7600U (with HT) in a laptop does about 19k jobs/s, while server with Xeon X3430 (without HT) does just about ~7k (both using 16 threads, as they both appear as 4 core to the system).
+
+To cancel the process, just send a kill signal or hit `Ctrl-C` any time. The process will perform cleanup and exit.
+
+### dns-crawler-workers
+
+```
+dns-crawler-workers - a process that spawns crawler workers.
+
+Usage: dns-crawler-workers [count] [redis]
+       count - worker count, 8 workers per CPU core by default
+       redis - redis host:port:db, localhost:6379:0 by default
+
+Examples: dns-crawler-workers 8
+          dns-crawler-workers 24 192.168.0.22:4444:0
+          dns-crawler-workers 16 redis.foo.bar:7777:2
+          dns-crawler-workers 16 redis.foo.bar # port 6379 and DB 0 will be used if not specified
+```
+
+Trying to use more than 24 workers per CPU core will result in a warning (and countdown before it actually starts the workers):
+
+```
+$ dns-crawler-workers 999
+Whoa. You are trying to run 999 workers on 4 CPU cores. It's easy toscale
+across multiple machines, if you need to. See README.md for details.
+
+Cancel now (Ctrl-C) or have a fire extinguisher ready.
+5 - 4 - 3 -
+```
+
+Stopping works the same way as with the controller process – `Ctrl-C` (or kill signal) will finish the current job(s) and exit.
+
+## Resuming work
+
+Stopping the workers won't delete the jobs from Redis. So, if you stop the `dns-crawler-workers` process and then start a new one (perhaps to use different worker count…), it will pick up the unfinished jobs and continue.
+
+This can also be used change the worker count if it turns out to be too low or high for your machine or network:
+
+- to reduce the worker count, just stop the `dns-crawler-workers` process and start a new one with a new count
+- to increase the worker count, either use the same approach, or just start a second `dns-crawler-workers` process in another shell, the worker count will just add up
+- scaling to multiple machines works the same way, see below
+
+## Running on multiple machines
+
+Since all communication between the controller and workers is done through Redis, it's easy to scale the crawler to any number of machines:
+
+```
+machine-1                     machine-1
+┬───────────────────────────┐         ┬─────────────────────┐
+│    dns-crawler-controller │ ------- │ dns-crawler-workers │
+│             +             │         └─────────────────────┘
+│           redis           │
+│             +             │
+│        DNS resolver       │
+└───────────────────────────┘
+                                      machine-2
+                                      ┬─────────────────────┐
+                              ------- │ dns-crawler-workers │
+                                      └─────────────────────┘
+                                      …
+                                      …
+
+                                      machine-n
+                                      ┬─────────────────────┐
+                              _______ │ dns-crawler-workers │
+                                      └─────────────────────┘
+```
+
+Just tell the workers to connect to the shared Redis on the main server, eg.:
+
+```
+$ dns-crawler-workers 24 192.168.0.2:6379
+                    ^            ^
+                    24 threads   redis host
+```
+
+Make sure to run the workers with ~same Python version on these machines, otherwise you'll get `unsupported pickle protocol` errors. See the [pickle protocol versions in Python docs](https://docs.python.org/3.8/library/pickle.html#data-stream-format).
+
+The DNS resolver doesn't have to be on a same machine as the `dns-crawler-controller`, of course – just set it's IP in `config.yml`. The crawler is tested primarily with CZ.NIC's [Knot Resolver](https://www.knot-resolver.cz/), but should work with any sane resolver supporting DNSSEC. Systemd's `systemd-resolved` seems to be really slow though.
+
+Same goes for Redis, you can point both controller and workers to a separate machine running Redis (don't forget to point them to an empty DB if you're using Redis for other things than the dns-crawler, it uses `0` by default).
+
+## Updating dependencies
+
+MaxMind updates GeoIP DBs on Tuesdays, so it may be a good idea to set a cron job to keep them fresh. More about that on [maxmind.com: Automatic Updates for GeoIP2](https://dev.maxmind.com/geoip/geoipupdate/).
+
+If you use multiple machines to run the workers, don't forget to update GeoIP on all of them (or set up a shared location, eg. via sshfs or nfs).
+
+## Monitoring
+
+### Command line
+
+```
+$ rq info
+default      |████████████████████ 219458
+1 queues, 219458 jobs total
+
+0 workers, 1 queues
+```
+
+### Web interface
+
+```
+$ pip install rq-dashboard
+$ rq-dashboard
+RQ Dashboard version 0.4.0                                                 
+ * Serving Flask app "rq_dashboard.cli" (lazy loading)                            
+ * Environment: production                                                
+   WARNING: Do not use the development server in a production environment. 
+   Use a production WSGI server instead.                                          
+ * Debug mode: off                            
+ * Running on http://0.0.0.0:9181/ (Press CTRL+C to quit)
+ ```
+
+<a href="https://i.vgy.me/sk7zWa.png">
+<img alt="RQ Dashboard screenshot" src="https://i.vgy.me/sk7zWa.png" width="40%">
+</a>
+<a href="https://i.vgy.me/4y5Zee.png">
+<img alt="RQ Dashboard screenshot" src="https://i.vgy.me/4y5Zee.png" width="40%">
+</a>
+
+## Tests
+
+Some basic tests are in the `tests` directory in this repo. If you want to run them manually, take a look at the `test` stage jobs in `.gitlab-ci.yml`. Basically it just downloads free GeoIP DBs, tells the crawler to use them, and crawles some domains, checking values in JSON output. It runs the tests twice – first with the default DNS resolvers (ODVR) and then with system one(s).
+
+If you're looking into writing some additional tests, be aware that some Docker containers used in GitLab CI don't have IPv6 configured (even if it's working on the host machine), so checking for eg. `WEB6_80_www_VENDOR` will fail without additional setup.
+
+
+## OS support
+
+The crawler is developed primarily for Linux, but it should work on any OS supported by Python – at least the worker part (but the controller should work too, if you manage to get a Redis server running on your OS).
+
+One exception is Windows, because it [doesn't support `fork()`](https://github.com/rq/rq/issues/859), but it's possible to get it working under WSL (Windows Subsystem for Linux):
+
+![win10 screenshot](https://i.vgy.me/emJjGN.png)
+
+…so you can turn a gaming machine into an internet crawler quite easily.
+
+
+## Bug reporting
+
+Please create [issues in this Gitlab repo](https://gitlab.nic.cz/adam/dns-crawler/issues).
+
```

### Comparing `dns-crawler-1.5.8/dns_crawler.egg-info/SOURCES.txt` & `dns-crawler-1.6.0/dns_crawler.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dns-crawler-1.5.8/result-schema.json` & `dns-crawler-1.6.0/result-schema.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9762751455112048%*

 * *Differences: {"'definitions'": "{'spf_record_array': {'items': {delete: ['properties', 'required', "*

 * *                  "'additionalProperties']}}, 'txt_dmarc_record_array': {'items': {replace: "*

 * *                  "OrderedDict([('oneOf', [OrderedDict([('type', 'object'), ('properties', "*

 * *                  "OrderedDict([('v', OrderedDict([('type', 'object')])), ('p', "*

 * *                  "OrderedDict([('type', 'object')])), ('pct', OrderedDict([('type', 'object')])), "*

 * *                  "('sp', OrderedDict([('type', 'objec […]*

```diff
@@ -1,14 +1,18 @@
 {
     "$schema": "http://json-schema.org/draft-07/schema#",
     "additionalProperties": false,
     "definitions": {
         "certificate": {
             "additionalProperties": false,
             "properties": {
+                "active": {
+                    "description": "Certificate is in its validity period.",
+                    "type": "boolean"
+                },
                 "algorithm": {
                     "description": "Certificate algorithm.",
                     "enum": [
                         "sha1",
                         "sha512-224",
                         "sha512-256",
                         "sha224",
@@ -35,19 +39,23 @@
                     "type": "array"
                 },
                 "error": {
                     "description": "Error message from SSL (python socket).",
                     "type": "string"
                 },
                 "expired": {
+                    "description": "Certificate is expired.",
                     "type": "boolean"
                 },
                 "expired_for": {
                     "description": "Period for which the certificate is expired (days).",
-                    "minimum": 0,
+                    "type": "integer"
+                },
+                "expires_in": {
+                    "description": "Days until certificate expiration.",
                     "type": "integer"
                 },
                 "fingerprint": {
                     "description": "Cetificate and pubkey fingerprints.",
                     "properties": {
                         "cert": {
                             "$ref": "#/definitions/certificate_fingerprint"
@@ -261,51 +269,14 @@
                 "type": "object"
             },
             "type": "array"
         },
         "spf_record_array": {
             "description": "SPF records parsed into JSON objects",
             "items": {
-                "additionalProperties": false,
-                "properties": {
-                    "all": {
-                        "type": "string"
-                    },
-                    "include": {
-                        "items": {
-                            "type": "string"
-                        },
-                        "type": "array"
-                    },
-                    "ip4": {
-                        "items": {
-                            "type": "string"
-                        },
-                        "type": "array"
-                    },
-                    "ip6": {
-                        "items": {
-                            "type": "string"
-                        },
-                        "type": "array"
-                    },
-                    "rules": {
-                        "items": {
-                            "type": "string"
-                        },
-                        "type": "array"
-                    },
-                    "v": {
-                        "type": "string"
-                    }
-                },
-                "required": [
-                    "v",
-                    "rules"
-                ],
                 "type": "object"
             },
             "type": "array"
         },
         "tls_info": {
             "properties": {
                 "cipher_bits": {
@@ -356,24 +327,64 @@
                     "type": "array"
                 }
             ]
         },
         "txt_dmarc_record_array": {
             "description": "DMARC records parsed into JSON objects",
             "items": {
-                "additionalProperties": true,
-                "properties": {
-                    "v": {
-                        "type": "string"
+                "oneOf": [
+                    {
+                        "additionalProperties": false,
+                        "properties": {
+                            "adkim": {
+                                "type": "object"
+                            },
+                            "aspf": {
+                                "type": "object"
+                            },
+                            "fo": {
+                                "type": "object"
+                            },
+                            "p": {
+                                "type": "object"
+                            },
+                            "pct": {
+                                "type": "object"
+                            },
+                            "rf": {
+                                "type": "object"
+                            },
+                            "ri": {
+                                "type": "object"
+                            },
+                            "rua": {
+                                "type": "object"
+                            },
+                            "ruf": {
+                                "type": "object"
+                            },
+                            "sp": {
+                                "type": "object"
+                            },
+                            "v": {
+                                "type": "object"
+                            }
+                        },
+                        "type": "object"
+                    },
+                    {
+                        "additionalProperties": false,
+                        "properties": {
+                            "error": {
+                                "type": "string"
+                            }
+                        },
+                        "type": "object"
                     }
-                },
-                "required": [
-                    "v"
-                ],
-                "type": "object"
+                ]
             },
             "type": "array"
         },
         "value_null_error": {
             "properties": {
                 "error": {
                     "type": "string"
@@ -428,43 +439,84 @@
                                             "description": "Certificate used for HTTPS connection",
                                             "items": {
                                                 "$ref": "#/definitions/certificate"
                                             },
                                             "type": "array"
                                         },
                                         "content": {
-                                            "type": "string"
+                                            "oneOf": [
+                                                {
+                                                    "type": "string"
+                                                },
+                                                {
+                                                    "type": "null"
+                                                }
+                                            ]
                                         },
                                         "content_is_binary": {
                                             "type": "boolean"
                                         },
                                         "detected_encoding": {
-                                            "type": "string"
+                                            "oneOf": [
+                                                {
+                                                    "type": "string"
+                                                },
+                                                {
+                                                    "type": "null"
+                                                }
+                                            ]
+                                        },
+                                        "detected_mimetype": {
+                                            "oneOf": [
+                                                {
+                                                    "type": "string"
+                                                },
+                                                {
+                                                    "type": "null"
+                                                }
+                                            ]
                                         },
                                         "error": {
                                             "type": "string"
                                         },
+                                        "geoip": {
+                                            "oneOf": [
+                                                {
+                                                    "$ref": "#/definitions/geoip"
+                                                },
+                                                {
+                                                    "type": "null"
+                                                }
+                                            ]
+                                        },
                                         "headers": {
                                             "type": "object"
                                         },
                                         "ip": {
                                             "$ref": "#/definitions/webserver_ip",
                                             "description": "IP of the webserver the crawler connected to"
                                         },
                                         "is_redirect": {
                                             "type": "boolean"
                                         },
                                         "status": {
                                             "$ref": "#/definitions/http_status"
                                         },
                                         "tls": {
-                                            "$ref": "#/definitions/tls_info"
+                                            "oneOf": [
+                                                {
+                                                    "$ref": "#/definitions/tls_info"
+                                                },
+                                                {
+                                                    "type": "null"
+                                                }
+                                            ]
                                         },
                                         "url": {
-                                            "description": "ULR, either implied (eg. http://<domain>.cz) or got from the Location header when redirected",
+                                            "description": "URL, either implied (eg. http://<domain>.cz) or got from the Location header when redirected",
                                             "type": "string"
                                         }
                                     },
                                     "required": [
                                         "url",
                                         "status",
                                         "headers"
@@ -480,22 +532,33 @@
                         "type": "object"
                     },
                     "type": "array"
                 }
             ]
         },
         "webserver_ip": {
-            "type": "string"
+            "oneOf": [
+                {
+                    "type": "string"
+                },
+                {
+                    "type": "null"
+                }
+            ]
         }
     },
     "properties": {
         "domain": {
             "description": "Domain name that was crawled.",
             "type": "string"
         },
+        "parent": {
+            "description": "Info about the parent zone",
+            "type": "object"
+        },
         "results": {
             "additionalProperties": false,
             "description": "A wrapper object holding all the results.",
             "properties": {
                 "DNS_AUTH": {
                     "anyOf": [
                         {
```

### Comparing `dns-crawler-1.5.8/setup.py` & `dns-crawler-1.6.0/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -63,13 +63,14 @@
         "Programming Language :: Python",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent"
     ],
     project_urls={
         "Operation in .CZ": "https://www.csirt.cz/en/dns-crawler/",
-        "Project ADAM": "https://adam.nic.cz/"
+        "CZ.NIC stats dashboard": "https://stats.nic.cz/",
+        "Project ADAM": "https://adam.nic.cz/",
     },
-    python_requires=">=3.6",
+    python_requires=">=3.7",
     long_description=long_description,
     long_description_content_type="text/markdown"
 )
```

### Comparing `dns-crawler-1.5.8/test/nic.cz.test.py` & `dns-crawler-1.6.0/test/nic.cz.test.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright © 2019-2020 CZ.NIC, z. s. p. o.
+# Copyright © 2019-2023 CZ.NIC, z. s. p. o.
 # SPDX-License-Identifier: GPL-3.0-or-later
 #
 # This file is part of dns-crawler.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
@@ -12,31 +12,32 @@
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
-from dns_crawler.crawl import process_domain
 import json
 
+from dns_crawler.crawl import process_domain
+
 r = process_domain("nic.cz")
 
 print(json.dumps(r))
 
 
 def sort_by_value(list):
     return sorted(list, key=lambda k: k["value"])
 
 
 assert sort_by_value(r["results"]["DNS_LOCAL"]["NS_AUTH"]) == sort_by_value(
     [{"value": "a.ns.nic.cz."}, {"value": "b.ns.nic.cz."}, {"value": "d.ns.nic.cz."}]
 )
 assert r["results"]["WEB"]["WEB4_80"][0]["steps"][0]["status"] == 301
-assert r["results"]["WEB"]["WEB4_80"][0]["steps"][0]["headers"]["server"] == "nginx"
+assert r["results"]["WEB"]["WEB4_80"][0]["steps"][-1]["headers"]["server"] == "nginx"
 
 assert r["results"]["WEB"]["WEB4_443"][0]["steps"][-1]["cert"][0]["subject"]["CN"] == "nic.cz"
 assert r["results"]["WEB"]["WEB4_443"][0]["steps"][-1]["cert"][0]["version"] == 3
 assert r["results"]["WEB"]["WEB4_443"][0]["steps"][-1]["cert"][0]["algorithm"] == "sha256"
 assert r["results"]["WEB"]["WEB4_443_www"][0]["steps"][-1]["status"] == 200
 
 assert r["results"]["DNS_LOCAL"]["DNSSEC"]["valid"]
```

