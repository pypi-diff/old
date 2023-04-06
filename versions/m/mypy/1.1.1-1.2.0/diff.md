# Comparing `tmp/mypy-1.1.1.tar.gz` & `tmp/mypy-1.2.0-cp39-cp39-win_amd64.whl.zip`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mypy-1.1.1.tar", last modified: Mon Mar  6 18:08:36 2023, max compression
+Zip archive data, at least v2.0 to extract, compression method=deflate
```

## filetype from diffoscope

```diff
@@ -1 +1 @@
-GzipFile
+ZipFile
```

