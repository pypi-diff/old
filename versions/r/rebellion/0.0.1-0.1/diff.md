# Comparing `tmp/rebellion-0.0.1.tar.gz` & `tmp/rebellion-0.1-py3-none-any.whl.zip`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rebellion-0.0.1.tar", last modified: Thu Apr  6 20:11:28 2023, max compression
+Zip archive data, at least v2.0 to extract, compression method=deflate
```

## filetype from diffoscope

```diff
@@ -1 +1 @@
-GzipFile
+ZipFile
```

