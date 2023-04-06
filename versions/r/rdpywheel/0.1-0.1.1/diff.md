# Comparing `tmp/rdpywheel-0.1.tar.gz` & `tmp/rdpywheel-0.1.1-py3-none-any.whl.zip`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rdpywheel-0.1.tar", last modified: Thu Apr  6 13:29:47 2023, max compression
+Zip archive data, at least v2.0 to extract, compression method=deflate
```

## filetype from diffoscope

```diff
@@ -1 +1 @@
-GzipFile
+ZipFile
```

