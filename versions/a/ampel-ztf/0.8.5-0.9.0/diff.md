# Comparing `tmp/ampel_ztf-0.8.5.tar.gz` & `tmp/ampel_ztf-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ampel_ztf-0.8.5.tar", max compression
+gzip compressed data, was "ampel_ztf-0.9.0.tar", max compression
```

## Comparing `ampel_ztf-0.8.5.tar` & `ampel_ztf-0.9.0.tar`

### file list

```diff
@@ -1,62 +1,62 @@
--rw-r--r--   0        0        0     1512 2023-03-29 09:09:58.880660 ampel_ztf-0.8.5/LICENSE
--rw-r--r--   0        0        0      391 2023-03-29 09:09:58.880660 ampel_ztf-0.8.5/README.md
--rw-r--r--   0        0        0        0 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/py.typed
--rwxr-xr-x   0        0        0     3644 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/template/ZTFLegacyChannelTemplate.py
--rwxr-xr-x   0        0        0      739 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/template/ZTFPeriodicSummaryT3.py
--rwxr-xr-x   0        0        0     2640 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/template/ZTFProcessLocalAlerts.py
--rwxr-xr-x   0        0        0    11970 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/util/Observatory.py
--rw-r--r--   0        0        0     3810 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/HealpixPathSupplier.py
--rwxr-xr-x   0        0        0     9168 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/PhotoAlertPlotter.py
--rw-r--r--   0        0        0    24540 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZTFFPbotForcedPhotometryAlertSupplier.py
--rwxr-xr-x   0        0        0     3649 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZTFForcedPhotometryAlertSupplier.py
--rwxr-xr-x   0        0        0     3582 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZTFGeneralActiveAlertRegister.py
--rwxr-xr-x   0        0        0     2132 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZTFGeneralAlertRegister.py
--rw-r--r--   0        0        0     5503 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZTFIPACForcedPhotometryAlertSupplier.py
--rwxr-xr-x   0        0        0     2375 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZiAlertSupplier.py
--rw-r--r--   0        0        0     2007 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZiHealpixAlertSupplier.py
--rwxr-xr-x   0        0        0     2119 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/ZiTaggedAlertSupplier.py
--rw-r--r--   0        0        0     5405 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/alert/load/ZTFHealpixAlertLoader.py
--rw-r--r--   0        0        0     1286 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/base/ArchiveUnit.py
--rwxr-xr-x   0        0        0     3612 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/base/CatalogMatchFilter.py
--rwxr-xr-x   0        0        0     5469 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/base/CatalogMatchUnit.py
--rwxr-xr-x   0        0        0     4803 2023-03-29 09:09:58.904660 ampel_ztf-0.8.5/ampel/ztf/dev/DevAlertConsumer.py
--rwxr-xr-x   0        0        0     6975 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/dev/DevSkyPortalClient.py
--rwxr-xr-x   0        0        0     3550 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/dev/ZTFAlert.py
--rw-r--r--   0        0        0     6187 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/ingest/ZiArchiveMuxer.py
--rw-r--r--   0        0        0      760 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/ingest/ZiCompilerOptions.py
--rwxr-xr-x   0        0        0     3580 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/ingest/ZiDataPointShaper.py
--rwxr-xr-x   0        0        0    10260 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/ingest/ZiMongoMuxer.py
--rwxr-xr-x   0        0        0     1062 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/ingest/tags.py
--rwxr-xr-x   0        0        0     2298 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/legacy_utils.py
--rwxr-xr-x   0        0        0    14327 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/DecentFilter.py
--rw-r--r--   0        0        0    17003 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/T0HealpixPathProcessor.py
--rw-r--r--   0        0        0    13501 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/T0HealpixProcessor.py
--rwxr-xr-x   0        0        0     7702 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/ZTFAlertStreamController.py
--rwxr-xr-x   0        0        0     7598 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/load/AllConsumingConsumer.py
--rwxr-xr-x   0        0        0     2947 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/load/UWAlertLoader.py
--rw-r--r--   0        0        0     2369 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/load/ZTFAlertArchiver.py
--rw-r--r--   0        0        0     3265 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/load/ZTFAlertArchiverV3.py
--rw-r--r--   0        0        0     4596 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/load/ZTFArchiveAlertLoader.py
--rw-r--r--   0        0        0     1346 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/load/avroutils.py
--rwxr-xr-x   0        0        0     2976 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t0/load/fetcherutils.py
--rwxr-xr-x   0        0        0     1198 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t1/ZiT1Combiner.py
--rwxr-xr-x   0        0        0     1048 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t1/ZiT1RetroCombiner.py
--rwxr-xr-x   0        0        0     5674 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t2/T2CatalogMatch.py
--rw-r--r--   0        0        0     2240 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t2/T2LightCurveFeatures.py
--rwxr-xr-x   0        0        0     2757 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t2/T2LightCurveSummary.py
--rwxr-xr-x   0        0        0     1339 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/T3LegacyExtJournalAppender.py
--rwxr-xr-x   0        0        0     2891 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/complement/FritzReport.py
--rwxr-xr-x   0        0        0     2481 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/complement/GROWTHMarshalReport.py
--rwxr-xr-x   0        0        0     3890 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/complement/TNSNames.py
--rwxr-xr-x   0        0        0      517 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/complement/TNSReports.py
--rwxr-xr-x   0        0        0     3031 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/complement/ZTFCutoutImages.py
--rw-r--r--   0        0        0     3171 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/resource/T3ZTFArchiveTokenGenerator.py
--rwxr-xr-x   0        0        0     1248 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/select/T3AdHocStockSelector.py
--rwxr-xr-x   0        0        0    30107 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/skyportal/SkyPortalClient.py
--rwxr-xr-x   0        0        0     3876 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/t3/skyportal/SkyPortalPublisher.py
--rwxr-xr-x   0        0        0     4337 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/util/ZTFIdMapper.py
--rw-r--r--   0        0        0     2781 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/util/ZTFNoisifiedIdMapper.py
--rw-r--r--   0        0        0     3832 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/ampel/ztf/view/ZTFT2Tabulator.py
--rw-r--r--   0        0        0     2302 2023-03-29 09:09:58.908660 ampel_ztf-0.8.5/conf/ampel-ztf/ampel.yml
--rw-r--r--   0        0        0     2685 2023-03-29 09:09:58.912660 ampel_ztf-0.8.5/pyproject.toml
--rw-r--r--   0        0        0     2475 1970-01-01 00:00:00.000000 ampel_ztf-0.8.5/PKG-INFO
+-rw-r--r--   0        0        0     1512 2023-04-07 13:56:59.167697 ampel_ztf-0.9.0/LICENSE
+-rw-r--r--   0        0        0      391 2023-04-07 13:56:59.167697 ampel_ztf-0.9.0/README.md
+-rw-r--r--   0        0        0        0 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/py.typed
+-rwxr-xr-x   0        0        0     3644 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/template/ZTFLegacyChannelTemplate.py
+-rwxr-xr-x   0        0        0      739 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/template/ZTFPeriodicSummaryT3.py
+-rwxr-xr-x   0        0        0     2819 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/template/ZTFProcessLocalAlerts.py
+-rwxr-xr-x   0        0        0    11970 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/util/Observatory.py
+-rw-r--r--   0        0        0     3810 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/HealpixPathSupplier.py
+-rwxr-xr-x   0        0        0     9168 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/PhotoAlertPlotter.py
+-rw-r--r--   0        0        0    24540 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZTFFPbotForcedPhotometryAlertSupplier.py
+-rwxr-xr-x   0        0        0     3649 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZTFForcedPhotometryAlertSupplier.py
+-rwxr-xr-x   0        0        0     3582 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZTFGeneralActiveAlertRegister.py
+-rwxr-xr-x   0        0        0     2132 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZTFGeneralAlertRegister.py
+-rw-r--r--   0        0        0     5534 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZTFIPACForcedPhotometryAlertSupplier.py
+-rwxr-xr-x   0        0        0     2375 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZiAlertSupplier.py
+-rw-r--r--   0        0        0     2007 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZiHealpixAlertSupplier.py
+-rwxr-xr-x   0        0        0     2119 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/ZiTaggedAlertSupplier.py
+-rw-r--r--   0        0        0     5405 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/alert/load/ZTFHealpixAlertLoader.py
+-rw-r--r--   0        0        0     1286 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/base/ArchiveUnit.py
+-rwxr-xr-x   0        0        0     3612 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/base/CatalogMatchFilter.py
+-rwxr-xr-x   0        0        0     5609 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/base/CatalogMatchUnit.py
+-rwxr-xr-x   0        0        0     4803 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/dev/DevAlertConsumer.py
+-rwxr-xr-x   0        0        0     6975 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/dev/DevSkyPortalClient.py
+-rwxr-xr-x   0        0        0     3550 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/dev/ZTFAlert.py
+-rw-r--r--   0        0        0     6187 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/ingest/ZiArchiveMuxer.py
+-rw-r--r--   0        0        0      760 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/ingest/ZiCompilerOptions.py
+-rwxr-xr-x   0        0        0     3580 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/ingest/ZiDataPointShaper.py
+-rwxr-xr-x   0        0        0    10260 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/ingest/ZiMongoMuxer.py
+-rwxr-xr-x   0        0        0     1062 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/ingest/tags.py
+-rwxr-xr-x   0        0        0     2298 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/legacy_utils.py
+-rwxr-xr-x   0        0        0    14327 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/DecentFilter.py
+-rw-r--r--   0        0        0    17003 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/T0HealpixPathProcessor.py
+-rw-r--r--   0        0        0    13501 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/T0HealpixProcessor.py
+-rwxr-xr-x   0        0        0     7702 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/ZTFAlertStreamController.py
+-rwxr-xr-x   0        0        0     7598 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/load/AllConsumingConsumer.py
+-rwxr-xr-x   0        0        0     2947 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/load/UWAlertLoader.py
+-rw-r--r--   0        0        0     2369 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/load/ZTFAlertArchiver.py
+-rw-r--r--   0        0        0     3265 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/load/ZTFAlertArchiverV3.py
+-rw-r--r--   0        0        0     3994 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/load/ZTFArchiveAlertLoader.py
+-rw-r--r--   0        0        0     1346 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/load/avroutils.py
+-rwxr-xr-x   0        0        0     2976 2023-04-07 13:56:59.191697 ampel_ztf-0.9.0/ampel/ztf/t0/load/fetcherutils.py
+-rwxr-xr-x   0        0        0     1198 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t1/ZiT1Combiner.py
+-rwxr-xr-x   0        0        0     1048 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t1/ZiT1RetroCombiner.py
+-rwxr-xr-x   0        0        0     5674 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t2/T2CatalogMatch.py
+-rw-r--r--   0        0        0     2240 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t2/T2LightCurveFeatures.py
+-rwxr-xr-x   0        0        0     2757 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t2/T2LightCurveSummary.py
+-rwxr-xr-x   0        0        0     1339 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/T3LegacyExtJournalAppender.py
+-rwxr-xr-x   0        0        0     2891 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/complement/FritzReport.py
+-rwxr-xr-x   0        0        0     2481 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/complement/GROWTHMarshalReport.py
+-rwxr-xr-x   0        0        0     3890 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/complement/TNSNames.py
+-rwxr-xr-x   0        0        0      517 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/complement/TNSReports.py
+-rwxr-xr-x   0        0        0     3031 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/complement/ZTFCutoutImages.py
+-rwxr-xr-x   0        0        0     1248 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/select/T3AdHocStockSelector.py
+-rwxr-xr-x   0        0        0    30107 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/skyportal/SkyPortalClient.py
+-rwxr-xr-x   0        0        0     3876 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t3/skyportal/SkyPortalPublisher.py
+-rw-r--r--   0        0        0     2986 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/t4/T4ZTFArchiveTokenGenerator.py
+-rwxr-xr-x   0        0        0     4337 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/util/ZTFIdMapper.py
+-rw-r--r--   0        0        0     2781 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/util/ZTFNoisifiedIdMapper.py
+-rw-r--r--   0        0        0     3832 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/ampel/ztf/view/ZTFT2Tabulator.py
+-rw-r--r--   0        0        0     2293 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/conf/ampel-ztf/ampel.yml
+-rw-r--r--   0        0        0     2689 2023-04-07 13:56:59.195698 ampel_ztf-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0     2481 1970-01-01 00:00:00.000000 ampel_ztf-0.9.0/PKG-INFO
```

### Comparing `ampel_ztf-0.8.5/LICENSE` & `ampel_ztf-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/template/ZTFLegacyChannelTemplate.py` & `ampel_ztf-0.9.0/ampel/template/ZTFLegacyChannelTemplate.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/template/ZTFPeriodicSummaryT3.py` & `ampel_ztf-0.9.0/ampel/template/ZTFPeriodicSummaryT3.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/template/ZTFProcessLocalAlerts.py` & `ampel_ztf-0.9.0/ampel/template/ZTFProcessLocalAlerts.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,26 +1,28 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-ZTF/ampel/template/ZTFProcessLocalAlerts.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                16.07.2021
-# Last Modified Date:  24.11.2021
+# Last Modified Date:  07.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any, Literal
 from ampel.types import ChannelId
 from ampel.log.AmpelLogger import AmpelLogger
 from ampel.model.UnitModel import UnitModel
+from ampel.model.job.JobTaskModel import JobTaskModel
 from ampel.model.ingest.T2Compute import T2Compute
-from ampel.abstract.AbsProcessorTemplate import AbsProcessorTemplate
+from ampel.abstract.AbsConfigMorpher import AbsConfigMorpher
 from ampel.template.AbsEasyChannelTemplate import AbsEasyChannelTemplate
 
 
-class ZTFProcessLocalAlerts(AbsProcessorTemplate):
+# Inheritance orders matters in this case
+class ZTFProcessLocalAlerts(JobTaskModel, AbsConfigMorpher): # type: ignore[misc]
 	"""
 	Returns adequate config for an alert consumer configured to process local alerts
 	"""
 
 	channel: ChannelId
 	folder: str
 	extension: Literal['json', 'avro', 'csv'] = "json"
@@ -35,21 +37,21 @@
 	#: units will be added automatically.
 	t2_compute: list[T2Compute] = []
 
 	extra: dict = {}
 
 
 	# Mandatory override
-	def get_model(self, config: dict[str, Any], logger: AmpelLogger) -> UnitModel:
+	def morph(self, ampel_config: dict[str, Any], logger: AmpelLogger) -> dict[str, Any]:
 
-		return UnitModel(
+		return self.dict(include=JobTaskModel.__fields__.keys()) | dict(
 			unit = 'AlertConsumer',
 			config = self.extra | AbsEasyChannelTemplate.craft_t0_processor_config(
 				channel = self.channel,
-				config = config,
+				alconf = ampel_config,
 				t2_compute = self.t2_compute,
 				supplier = self._get_supplier(),
 				shaper = "ZiDataPointShaper",
 				combiner = "ZiT1Combiner",
 				filter_dict = None,
 				muxer = None,
 				compiler_opts = {
```

### Comparing `ampel_ztf-0.8.5/ampel/util/Observatory.py` & `ampel_ztf-0.9.0/ampel/util/Observatory.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/HealpixPathSupplier.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/HealpixPathSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/PhotoAlertPlotter.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/PhotoAlertPlotter.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZTFFPbotForcedPhotometryAlertSupplier.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZTFFPbotForcedPhotometryAlertSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZTFForcedPhotometryAlertSupplier.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZTFForcedPhotometryAlertSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZTFGeneralActiveAlertRegister.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZTFGeneralActiveAlertRegister.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZTFGeneralAlertRegister.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZTFGeneralAlertRegister.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZTFIPACForcedPhotometryAlertSupplier.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZTFIPACForcedPhotometryAlertSupplier.py`

 * *Files 3% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 from bts_phot.calibrate_fps import get_baseline # type: ignore[import]
 
 from ampel.ztf.util.ZTFIdMapper import to_ampel_id
 from ampel.protocol.AmpelAlertProtocol import AmpelAlertProtocol
 from ampel.view.ReadOnlyDict import ReadOnlyDict
 from ampel.alert.AmpelAlert import AmpelAlert
 from ampel.alert.BaseAlertSupplier import BaseAlertSupplier
-from ampel.model.PlotProperties import PlotProperties
+from ampel.model.PlotProperties import PlotProperties, FormatModel
 from ampel.plot.create import create_plot_record
 
 dcast = {
 	'field': int,
 	'ccdid': int,
 	'qid': int,
 	'filter': str,
@@ -97,22 +97,22 @@
 	flux_unc_key: str = "fnu_microJy_unc"
 	flux_unc_scale: dict[str, float] = {'ZTF_g': 1., 'ZTF_r': 1., 'ZTF_i': 1.}
 	flux_unc_floor: float = 0.02
 	excl_poor_conditions: bool = True
 
 	plot_props: PlotProperties = PlotProperties(
 		tags = ["IFP", "BASELINE"],
-		file_name = {
-			"format_str": "ifp_raw_%s.svg",
-			"arg_keys": ["sn_name"]
-		},
-		title = {
-			"format_str": "IFP - %s",
-			"arg_keys": ["sn_name"]
-		}
+		file_name = FormatModel(
+			format_str = "ifp_raw_%s.svg",
+			arg_keys = ["sn_name"]
+		),
+		title = FormatModel(
+			format_str = "IFP - %s",
+			arg_keys = ["sn_name"]
+		)
 	)
 
 
 	def __init__(self, **kwargs) -> None:
 
 		kwargs['deserialize'] = None
 		super().__init__(**kwargs)
```

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZiAlertSupplier.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZiAlertSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZiHealpixAlertSupplier.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZiHealpixAlertSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/ZiTaggedAlertSupplier.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/ZiTaggedAlertSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/alert/load/ZTFHealpixAlertLoader.py` & `ampel_ztf-0.9.0/ampel/ztf/alert/load/ZTFHealpixAlertLoader.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/base/ArchiveUnit.py` & `ampel_ztf-0.9.0/ampel/ztf/base/ArchiveUnit.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/base/CatalogMatchFilter.py` & `ampel_ztf-0.9.0/ampel/ztf/base/CatalogMatchFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/base/CatalogMatchUnit.py` & `ampel_ztf-0.9.0/ampel/ztf/base/CatalogMatchUnit.py`

 * *Files 2% similar despite different names*

```diff
@@ -137,14 +137,16 @@
     def _cone_search(
         self,
         method: Literal["any", "nearest", "all"],
         ra: float,
         dec: float,
         catalogs: Sequence[ConeSearchRequest],
     ) -> list[bool] | list[None | CatalogItem] | list[None | list[CatalogItem]]:
+        if not -90 <= dec <= 90:
+            raise ValueError("Declination angle must be within -90 deg <= angle <= 90 deg, got {dec} deg")
         response = self.session.post(
             f"cone_search/{method}",
             json={
                 "ra_deg": ra,
                 "dec_deg": dec,
                 "catalogs": catalogs,
             },
```

### Comparing `ampel_ztf-0.8.5/ampel/ztf/dev/DevAlertConsumer.py` & `ampel_ztf-0.9.0/ampel/ztf/dev/DevAlertConsumer.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/dev/DevSkyPortalClient.py` & `ampel_ztf-0.9.0/ampel/ztf/dev/DevSkyPortalClient.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/dev/ZTFAlert.py` & `ampel_ztf-0.9.0/ampel/ztf/dev/ZTFAlert.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/ingest/ZiArchiveMuxer.py` & `ampel_ztf-0.9.0/ampel/ztf/ingest/ZiArchiveMuxer.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/ingest/ZiCompilerOptions.py` & `ampel_ztf-0.9.0/ampel/ztf/ingest/ZiCompilerOptions.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/ingest/ZiDataPointShaper.py` & `ampel_ztf-0.9.0/ampel/ztf/ingest/ZiDataPointShaper.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/ingest/ZiMongoMuxer.py` & `ampel_ztf-0.9.0/ampel/ztf/ingest/ZiMongoMuxer.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/ingest/tags.py` & `ampel_ztf-0.9.0/ampel/ztf/ingest/tags.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/legacy_utils.py` & `ampel_ztf-0.9.0/ampel/ztf/legacy_utils.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/DecentFilter.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/DecentFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/T0HealpixPathProcessor.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/T0HealpixPathProcessor.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/T0HealpixProcessor.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/T0HealpixProcessor.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/ZTFAlertStreamController.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/ZTFAlertStreamController.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/load/AllConsumingConsumer.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/load/AllConsumingConsumer.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/load/UWAlertLoader.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/load/UWAlertLoader.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/load/ZTFAlertArchiver.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/load/ZTFAlertArchiver.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/load/ZTFAlertArchiverV3.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/load/ZTFAlertArchiverV3.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/load/ZTFArchiveAlertLoader.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/load/ZTFArchiveAlertLoader.py`

 * *Files 7% similar despite different names*

```diff
@@ -7,15 +7,14 @@
 # Last Modified Date:  22.12.2022
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import logging, backoff, requests
 from typing import Any
 from ampel.abstract.AbsAlertLoader import AbsAlertLoader
 from ampel.base.AmpelBaseModel import AmpelBaseModel
-from ampel.struct.Resource import Resource
 
 log = logging.getLogger(__name__)
 
 
 class ZTFSource(AmpelBaseModel):
     ztf_name: str
     programid: None | int = None
@@ -35,34 +34,20 @@
     this is acknowledged and a new chunk retrieved.
     """
 
     #: Base URL of archive service
     archive: str = "https://ampel.zeuthen.desy.de/api/ztf/archive/v3"
 
     #: A stream identifier, created via POST /api/ztf/archive/streams/, or a query
-    stream: None | str | ZTFSource
-
-    #: Name of dynamic resource, fetched by a T3 process and forwarded
-    #: to suppliers/loaders by AlertConsumer via their methods add_resource
-    resource_name: str = 'ztf_stream_token'
+    stream: None | str | ZTFSource = '%%ztf_stream_token'
 
     def __init__(self, **kwargs) -> None:
         super().__init__(**kwargs)
         self._it = None
 
-    # override
-    def add_resource(self, name: str, resource: Resource) -> None:
-        if name == self.resource_name:
-            if not isinstance(resource.value, str):
-                raise ValueError(
-                    f"Unexpected {self.resource_name} resource "
-                    f"value type: {type(resource.value)}"
-                )
-            self.stream = resource.value
-
     def __iter__(self):
         return self.get_alerts()
 
     def __next__(self):
         if not self._it:
             self._it = iter(self)
         return next(self._it)
```

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/load/avroutils.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/load/avroutils.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t0/load/fetcherutils.py` & `ampel_ztf-0.9.0/ampel/ztf/t0/load/fetcherutils.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t1/ZiT1Combiner.py` & `ampel_ztf-0.9.0/ampel/ztf/t1/ZiT1Combiner.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t1/ZiT1RetroCombiner.py` & `ampel_ztf-0.9.0/ampel/ztf/t1/ZiT1RetroCombiner.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t2/T2CatalogMatch.py` & `ampel_ztf-0.9.0/ampel/ztf/t2/T2CatalogMatch.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t2/T2LightCurveFeatures.py` & `ampel_ztf-0.9.0/ampel/ztf/t2/T2LightCurveFeatures.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t2/T2LightCurveSummary.py` & `ampel_ztf-0.9.0/ampel/ztf/t2/T2LightCurveSummary.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/T3LegacyExtJournalAppender.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/T3LegacyExtJournalAppender.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/complement/FritzReport.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/complement/FritzReport.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/complement/GROWTHMarshalReport.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/complement/GROWTHMarshalReport.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/complement/TNSNames.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/complement/TNSNames.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/complement/TNSReports.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/complement/TNSReports.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/complement/ZTFCutoutImages.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/complement/ZTFCutoutImages.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/resource/T3ZTFArchiveTokenGenerator.py` & `ampel_ztf-0.9.0/ampel/ztf/t4/T4ZTFArchiveTokenGenerator.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,39 +1,36 @@
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
-# File:                Ampel-ZTF/ampel/ztf/t3/resource/T3ZTFArchiveTokenGenerator.py
+# File:                Ampel-ZTF/ampel/ztf/t4/T4ZTFArchiveTokenGenerator.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel & Simeon Reusch
 # Date:                21.12.2022
-# Last Modified Date:  21.12.2022
+# Last Modified Date:  07.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import random
 import time
 from typing import Any
-from astropy.time import Time  # type: ignore
+from astropy.time import Time  # type: ignore[import]
 from datetime import datetime
-
-from requests_toolbelt.sessions import BaseUrlSession
+from requests_toolbelt.sessions import BaseUrlSession # type: ignore[import]
 
 from ampel.types import UBson
-from ampel.struct.T3Store import T3Store
-from ampel.struct.Resource import Resource
 from ampel.struct.UnitResult import UnitResult
 from ampel.secret.NamedSecret import NamedSecret
-from ampel.abstract.AbsT3PlainUnit import AbsT3PlainUnit
+from ampel.abstract.AbsT4Unit import AbsT4Unit
 
 
-class T3ZTFArchiveTokenGenerator(AbsT3PlainUnit):
+class T4ZTFArchiveTokenGenerator(AbsT4Unit):
 
 	archive_token: NamedSecret[str] = NamedSecret(label="ztf/archive/token")
 
 	#: Base URL of archive service
 	archive: str = "https://ampel.zeuthen.desy.de/api/ztf/archive/v3/"
-	resource_name: str = 'ztf_stream_token'
+	resource_name: str = '%%ztf_stream_token'
 
 	max_dist_ps1_src: float = 0.5
 	min_detections: int = 3
 
 	date_str: None | str = None
 	date_format: str = "%Y-%m-%d"
 	days_ago: None | int = None
@@ -43,15 +40,15 @@
 
 	#: seconds to wait for query to complete
 	timeout: float = 60
 
 	debug: bool = False
 
 
-	def process(self, t3s: T3Store) -> UBson | UnitResult:
+	def do(self) -> UBson | UnitResult:
 
 		if self.date_str:
 			start_jd = Time(
 				str(datetime.strptime(self.date_str, self.date_format)),
 				format="iso", scale="utc"
 			).jd
 			delta_t = 1
@@ -106,14 +103,8 @@
 			time.sleep(random.uniform(0, delay))
 			delay *= 2
 		else:
 			raise RuntimeError(f"{session.base_url}stream/{token} still locked after {time.time() - t0:.0f} s")
 		response.raise_for_status()
 		self.logger.info("Stream created", extra=response.json())
 
-		r = Resource(name=self.resource_name, value=token)
-		t3s.add_resource(r)
-
-		if self.debug:
-			return r.dict()
-
-		return None
+		return {self.resource_name: token}
```

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/select/T3AdHocStockSelector.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/select/T3AdHocStockSelector.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/skyportal/SkyPortalClient.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/skyportal/SkyPortalClient.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/t3/skyportal/SkyPortalPublisher.py` & `ampel_ztf-0.9.0/ampel/ztf/t3/skyportal/SkyPortalPublisher.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/util/ZTFIdMapper.py` & `ampel_ztf-0.9.0/ampel/ztf/util/ZTFIdMapper.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/util/ZTFNoisifiedIdMapper.py` & `ampel_ztf-0.9.0/ampel/ztf/util/ZTFNoisifiedIdMapper.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/ampel/ztf/view/ZTFT2Tabulator.py` & `ampel_ztf-0.9.0/ampel/ztf/view/ZTFT2Tabulator.py`

 * *Files identical despite different names*

### Comparing `ampel_ztf-0.8.5/conf/ampel-ztf/ampel.yml` & `ampel_ztf-0.9.0/conf/ampel-ztf/ampel.yml`

 * *Files 6% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 - ampel.ztf.t0.DecentFilter
 - ampel.ztf.ingest.ZiDataPointShaper
 - ampel.ztf.base.CatalogMatchFilter
 - ampel.ztf.t2.T2LightCurveSummary
 - ampel.ztf.t2.T2CatalogMatch
 - ampel.ztf.t2.T2LightCurveFeatures
 - ampel.ztf.t3.skyportal.SkyPortalPublisher
-- ampel.ztf.t3.resource.T3ZTFArchiveTokenGenerator
+- ampel.ztf.t4.T4ZTFArchiveTokenGenerator
 
 # Ops units
 - ampel.ztf.t0.load.ZTFAlertArchiverV3
 
 # Aux units
 - ampel.ztf.alert.HealpixPathSupplier
 - ampel.ztf.alert.ZiAlertSupplier
```

### Comparing `ampel_ztf-0.8.5/pyproject.toml` & `ampel_ztf-0.9.0/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "ampel-ztf"
-version = "0.8.5"
+version = "0.9.0"
 description = "Zwicky Transient Facility support for the Ampel system"
 authors = [
     "Valery Brinnel",
     "Jakob van Santen <jakob.van.santen@desy.de>",
     "Sjoert van Velzen",
     "Jakob Nordin",
 ]
@@ -45,31 +45,31 @@
 fastavro = "~1.6.0"
 requests = "^2.25.1"
 requests-toolbelt = "^0.10.0"
 confluent-kafka = {version = "^2.0.0", optional = true}
 healpy = {version = "^1.15", optional = true}
 light-curve = {version = ">=0.7,<0.8", optional = true}
 ampel-ztf-archive = {version = "^0.8.0-alpha.0", optional = true}
-ampel-interface = "^0.8.7"
-ampel-core = "^0.8.6"
-ampel-photometry = "^0.8.3"
-ampel-alerts = "^0.8.3"
-ampel-plot = {version = "^0.8.3", optional = true}
+ampel-interface = "^0.9.0"
+ampel-core = "^0.9.0"
+ampel-photometry = "^0.9.0"
+ampel-alerts = "^0.9.0"
+ampel-plot = {version = "^0.8.3-3", optional = true}
 pandas = {version = "^1.5.2", optional = true}
 scipy = "^1.9.3"
 planobs = {version = "^0.6.1", optional = true}
 
 [tool.poetry.dev-dependencies]
 pytest = "^7.2.2"
 pytest-cov = "^4.0.0"
 pytest-mock = "^3.10.0"
 mongomock = "^4.1.2"
-mypy = "^1.0"
+mypy = "^1.1.1"
 pytest-timeout = "^2.1.0"
-pytest-asyncio = "^0.20.3"
+pytest-asyncio = "^0.21.0"
 types-requests = "^2.25.9"
 before_after = "^1.0.1"
 
 [tool.poetry.extras]
 archive = ["ampel-ztf-archive"]
 healpix = ["healpy"]
 light-curve = ["light-curve"]
```

### Comparing `ampel_ztf-0.8.5/PKG-INFO` & `ampel_ztf-0.9.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ampel-ztf
-Version: 0.8.5
+Version: 0.9.0
 Summary: Zwicky Transient Facility support for the Ampel system
 Home-page: https://ampelproject.github.io
 License: BSD-3-Clause
 Author: Valery Brinnel
 Maintainer: Jakob van Santen
 Maintainer-email: jakob.van.santen@desy.de
 Requires-Python: >=3.10,<3.12
@@ -21,19 +21,19 @@
 Provides-Extra: bayes
 Provides-Extra: fp
 Provides-Extra: healpix
 Provides-Extra: kafka
 Provides-Extra: light-curve
 Provides-Extra: plot
 Requires-Dist: aiohttp (>=3.7.3,<4.0.0)
-Requires-Dist: ampel-alerts (>=0.8.3,<0.9.0)
-Requires-Dist: ampel-core (>=0.8.6,<0.9.0)
-Requires-Dist: ampel-interface (>=0.8.7,<0.9.0)
-Requires-Dist: ampel-photometry (>=0.8.3,<0.9.0)
-Requires-Dist: ampel-plot (>=0.8.3,<0.9.0) ; extra == "plot" or extra == "bayes"
+Requires-Dist: ampel-alerts (>=0.9.0,<0.10.0)
+Requires-Dist: ampel-core (>=0.9.0,<0.10.0)
+Requires-Dist: ampel-interface (>=0.9.0,<0.10.0)
+Requires-Dist: ampel-photometry (>=0.9.0,<0.10.0)
+Requires-Dist: ampel-plot (>=0.8.3-3,<0.9.0) ; extra == "plot" or extra == "bayes"
 Requires-Dist: ampel-ztf-archive (>=0.8.0-alpha.0,<0.9.0) ; extra == "archive"
 Requires-Dist: astropy (>=5.0,<6.0)
 Requires-Dist: backoff (>=2.0.0,<3.0.0)
 Requires-Dist: confluent-kafka (>=2.0.0,<3.0.0) ; extra == "kafka"
 Requires-Dist: fastavro (>=1.6.0,<1.7.0)
 Requires-Dist: healpy (>=1.15,<2.0) ; extra == "healpix"
 Requires-Dist: light-curve (>=0.7,<0.8) ; extra == "light-curve"
```

