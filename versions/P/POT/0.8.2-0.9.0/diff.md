# Comparing `tmp/POT-0.8.2.tar.gz` & `tmp/POT-0.9.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.zip`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "POT-0.8.2.tar", last modified: Thu Apr 21 16:27:50 2022, max compression
+Zip archive data, at least v2.0 to extract, compression method=store
```

## filetype from diffoscope

```diff
@@ -1 +1 @@
-GzipFile
+ZipFile
```

