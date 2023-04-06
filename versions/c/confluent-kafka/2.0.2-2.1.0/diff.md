# Comparing `tmp/confluent-kafka-2.0.2.tar.gz` & `tmp/confluent_kafka-2.1.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.zip`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "confluent-kafka-2.0.2.tar", last modified: Tue Jan 24 12:43:37 2023, max compression
+Zip archive data, at least v2.0 to extract, compression method=store
```

## filetype from diffoscope

```diff
@@ -1 +1 @@
-GzipFile
+ZipFile
```

