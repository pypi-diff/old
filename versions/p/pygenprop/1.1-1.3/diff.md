# Comparing `tmp/pygenprop-1.1.tar.gz` & `tmp/pygenprop-1.3-py3.9.egg`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pygenprop-1.1.tar", last modified: Fri Mar  3 00:19:12 2023, max compression
+Zip archive data, at least v2.0 to extract, compression method=deflate
```

## filetype from diffoscope

```diff
@@ -1 +1 @@
-GzipFile
+ZipFile
```

