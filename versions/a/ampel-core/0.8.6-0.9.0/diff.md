# Comparing `tmp/ampel_core-0.8.6.tar.gz` & `tmp/ampel_core-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ampel_core-0.8.6.tar", max compression
+gzip compressed data, was "ampel_core-0.9.0.tar", max compression
```

## Comparing `ampel_core-0.8.6.tar` & `ampel_core-0.9.0.tar`

### file list

```diff
@@ -1,297 +1,278 @@
--rw-r--r--   0        0        0     1512 2023-03-28 12:54:33.480615 ampel_core-0.8.6/LICENSE
--rw-r--r--   0        0        0      262 2023-03-28 12:54:33.480615 ampel_core-0.8.6/README.md
--rwxr-xr-x   0        0        0     1251 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsBufferComplement.py
--rw-r--r--   0        0        0     1565 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsChannelTemplate.py
--rwxr-xr-x   0        0        0     6900 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsCompiler.py
--rwxr-xr-x   0        0        0      871 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsDocIngester.py
--rwxr-xr-x   0        0        0      886 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsDocUpdater.py
--rw-r--r--   0        0        0     4050 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsEventUnit.py
--rw-r--r--   0        0        0     1112 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsOpsUnit.py
--rwxr-xr-x   0        0        0     2719 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsProcessController.py
--rw-r--r--   0        0        0      708 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsProcessTemplate.py
--rw-r--r--   0        0        0      760 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsProcessorTemplate.py
--rwxr-xr-x   0        0        0     2334 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT0Muxer.py
--rwxr-xr-x   0        0        0     1410 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT3ControlUnit.py
--rwxr-xr-x   0        0        0      743 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT3Filter.py
--rwxr-xr-x   0        0        0     2502 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT3Loader.py
--rwxr-xr-x   0        0        0      767 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT3Projector.py
--rwxr-xr-x   0        0        0      777 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT3Selector.py
--rwxr-xr-x   0        0        0     1239 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT3Stager.py
--rwxr-xr-x   0        0        0      939 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsT3Supplier.py
--rw-r--r--   0        0        0      593 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsTargetSource.py
--rwxr-xr-x   0        0        0      700 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsUnitResultAdapter.py
--rwxr-xr-x   0        0        0    13954 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/AbsWorker.py
--rw-r--r--   0        0        0      282 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/abstract/README.md
--rwxr-xr-x   0        0        0    11114 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/aux/ComboDictModifier.py
--rw-r--r--   0        0        0     1248 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/aux/SimpleTagFilter.py
--rwxr-xr-x   0        0        0     1575 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/aux/filter/AbsLogicOperatorFilter.py
--rw-r--r--   0        0        0     1192 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/aux/filter/FlatDictArrayFilter.py
--rw-r--r--   0        0        0     1116 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/aux/filter/PrimitiveTypeArrayFilter.py
--rw-r--r--   0        0        0     1768 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/aux/filter/SimpleDictArrayFilter.py
--rw-r--r--   0        0        0     4243 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/cli/AbsCoreCommand.py
--rw-r--r--   0        0        0     2134 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/cli/AbsLoadCommand.py
--rwxr-xr-x   0        0        0     6032 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/cli/AbsStockCommand.py
--rw-r--r--   0        0        0     4200 2023-03-28 12:54:33.480615 ampel_core-0.8.6/ampel/cli/BufferCommand.py
--rw-r--r--   0        0        0    11533 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/ConfigCommand.py
--rw-r--r--   0        0        0     4955 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/DBCommand.py
--rw-r--r--   0        0        0     5939 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/EventCommand.py
--rw-r--r--   0        0        0    25482 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/JobCommand.py
--rw-r--r--   0        0        0     8842 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/LogCommand.py
--rw-r--r--   0        0        0     5808 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/ProcessCommand.py
--rw-r--r--   0        0        0     3321 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/RunCommand.py
--rw-r--r--   0        0        0     6326 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/StartCommand.py
--rw-r--r--   0        0        0     9315 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/T2Command.py
--rw-r--r--   0        0        0     2170 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/T3BufferExporterStager.py
--rw-r--r--   0        0        0     1888 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/T3BufferExporterUnit.py
--rw-r--r--   0        0        0     4388 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/ViewCommand.py
--rw-r--r--   0        0        0     4434 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/export.py
--rw-r--r--   0        0        0     3362 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/cli/utils.py
--rwxr-xr-x   0        0        0     1301 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/ScheduleEvaluator.py
--rw-r--r--   0        0        0      623 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/AbsConfigTemplate.py
--rw-r--r--   0        0        0     1746 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/BaseConfigChecker.py
--rwxr-xr-x   0        0        0    20308 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/ConfigBuilder.py
--rw-r--r--   0        0        0     7539 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/ConfigChecker.py
--rw-r--r--   0        0        0     1671 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/ConfigValidator.py
--rwxr-xr-x   0        0        0      570 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/DisplayOptions.py
--rwxr-xr-x   0        0        0     8513 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/DistConfigBuilder.py
--rwxr-xr-x   0        0        0     3669 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/FirstPassConfig.py
--rwxr-xr-x   0        0        0     8777 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/ProcessMorpher.py
--rw-r--r--   0        0        0     1000 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/builder/get_env.py
--rwxr-xr-x   0        0        0     1511 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/AbsDictConfigCollector.py
--rwxr-xr-x   0        0        0     2560 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/AbsForwardConfigCollector.py
--rwxr-xr-x   0        0        0      770 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/AbsListConfigCollector.py
--rwxr-xr-x   0        0        0     1985 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/AliasConfigCollector.py
--rwxr-xr-x   0        0        0     1826 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/ChannelConfigCollector.py
--rwxr-xr-x   0        0        0     2709 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/ConfigCollector.py
--rwxr-xr-x   0        0        0     2387 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/DBConfigCollector.py
--rwxr-xr-x   0        0        0     1243 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/ForwardProcessConfigCollector.py
--rwxr-xr-x   0        0        0     1958 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/LoggingCollector.py
--rwxr-xr-x   0        0        0     1390 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/ProcessConfigCollector.py
--rwxr-xr-x   0        0        0     1673 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/ResourceConfigCollector.py
--rwxr-xr-x   0        0        0     1648 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/T02ConfigCollector.py
--rwxr-xr-x   0        0        0     7085 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/config/collector/UnitConfigCollector.py
--rwxr-xr-x   0        0        0     6129 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/AmpelContext.py
--rwxr-xr-x   0        0        0    10976 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/AmpelController.py
--rwxr-xr-x   0        0        0    18998 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/AmpelDB.py
--rwxr-xr-x   0        0        0    17800 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/AmpelRegister.py
--rwxr-xr-x   0        0        0      861 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/ContextUnit.py
--rwxr-xr-x   0        0        0     6564 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/DataLoader.py
--rwxr-xr-x   0        0        0    10174 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/DefaultProcessController.py
--rwxr-xr-x   0        0        0     4453 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/EventHandler.py
--rwxr-xr-x   0        0        0     3642 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/Schedulable.py
--rwxr-xr-x   0        0        0    14814 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/core/UnitLoader.py
--rw-r--r--   0        0        0      855 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/demo/DemoFirstPointT2Unit.py
--rwxr-xr-x   0        0        0     1060 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/demo/DemoPlainT3Unit.py
--rw-r--r--   0        0        0     1075 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/demo/DemoPointT2Unit.py
--rw-r--r--   0        0        0     1657 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/demo/DemoProcessor.py
--rwxr-xr-x   0        0        0     1009 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/demo/DemoResourceT3Unit.py
--rw-r--r--   0        0        0     1357 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/demo/DemoReviewT3Unit.py
--rwxr-xr-x   0        0        0     6431 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/dev/DevAmpelContext.py
--rw-r--r--   0        0        0      841 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/dev/NoShaper.py
--rwxr-xr-x   0        0        0    27480 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/ingest/ChainedIngestionHandler.py
--rw-r--r--   0        0        0     1435 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/ingest/ChainedT0Muxer.py
--rw-r--r--   0        0        0     3115 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/ingest/StockCompiler.py
--rw-r--r--   0        0        0     2480 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/ingest/T0Compiler.py
--rw-r--r--   0        0        0     5255 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/ingest/T1Compiler.py
--rw-r--r--   0        0        0     3009 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/ingest/T2Compiler.py
--rwxr-xr-x   0        0        0     8036 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/AmpelLogger.py
--rwxr-xr-x   0        0        0      389 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/AmpelLoggingError.py
--rw-r--r--   0        0        0     1424 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/LightLogRecord.py
--rw-r--r--   0        0        0     1163 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/LogFlag.py
--rwxr-xr-x   0        0        0     1491 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/LoggingErrorReporter.py
--rw-r--r--   0        0        0     3975 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/LogsDumper.py
--rw-r--r--   0        0        0      477 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/__init__.py
--rwxr-xr-x   0        0        0     6025 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/handlers/AmpelStreamHandler.py
--rwxr-xr-x   0        0        0     2443 2023-03-28 12:54:33.484615 ampel_core-0.8.6/ampel/log/handlers/ChanRecordBufHandler.py
--rw-r--r--   0        0        0     2006 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/log/handlers/DefaultRecordBufferingHandler.py
--rw-r--r--   0        0        0     1712 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/log/handlers/EnclosedChanRecordBufHandler.py
--rw-r--r--   0        0        0     1528 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/log/handlers/RecordBufferingHandler.py
--rwxr-xr-x   0        0        0     7836 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/log/utils.py
--rw-r--r--   0        0        0     1212 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/metrics/AmpelDBCollector.py
--rw-r--r--   0        0        0     2387 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/metrics/AmpelMetricsRegistry.py
--rw-r--r--   0        0        0     1940 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/metrics/AmpelProcessCollector.py
--rw-r--r--   0        0        0     5175 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/metrics/prometheus.py
--rwxr-xr-x   0        0        0     1081 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ChannelModel.py
--rwxr-xr-x   0        0        0     1477 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ProcessModel.py
--rw-r--r--   0        0        0       93 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/Readme.md
--rw-r--r--   0        0        0      856 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/aux/AuxAliasableModel.py
--rw-r--r--   0        0        0     1253 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/aux/FilterCriterion.py
--rw-r--r--   0        0        0      580 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/builder/BuilderAliasModel.py
--rw-r--r--   0        0        0      526 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/builder/RemoteUnitDefinition.py
--rwxr-xr-x   0        0        0      938 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/CompilerOptions.py
--rw-r--r--   0        0        0     2044 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/DualIngestDirective.py
--rw-r--r--   0        0        0      737 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/FilterModel.py
--rw-r--r--   0        0        0     2065 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/IngestBody.py
--rw-r--r--   0        0        0     1286 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/IngestDirective.py
--rw-r--r--   0        0        0     1451 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/MuxModel.py
--rwxr-xr-x   0        0        0     1215 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/T1Combine.py
--rwxr-xr-x   0        0        0      780 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/T1CombineCompute.py
--rwxr-xr-x   0        0        0     1369 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/T1CombineComputeNow.py
--rwxr-xr-x   0        0        0      785 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/ingest/T2Compute.py
--rw-r--r--   0        0        0      405 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/BaseSequence.py
--rw-r--r--   0        0        0      459 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/EnvSpec.py
--rw-r--r--   0        0        0      443 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/ExpandWithItems.py
--rw-r--r--   0        0        0      708 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/ExpandWithSequence.py
--rw-r--r--   0        0        0     1582 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/ExpressionParser.py
--rw-r--r--   0        0        0     1195 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/InputArtifact.py
--rw-r--r--   0        0        0      398 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/InputArtifactHttpSource.py
--rw-r--r--   0        0        0      396 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/InputParameter.py
--rw-r--r--   0        0        0     2706 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/JobModel.py
--rw-r--r--   0        0        0      407 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/MongoOpts.py
--rw-r--r--   0        0        0      395 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/OutputArtifact.py
--rw-r--r--   0        0        0      672 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/OutputParameter.py
--rw-r--r--   0        0        0      445 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/OutputParameterSource.py
--rw-r--r--   0        0        0      386 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/Parameter.py
--rw-r--r--   0        0        0      472 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/SequenceWithCount.py
--rw-r--r--   0        0        0      451 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/SequenceWithEnd.py
--rw-r--r--   0        0        0      555 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/TaskInputs.py
--rw-r--r--   0        0        0      563 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/TaskOutputs.py
--rw-r--r--   0        0        0      921 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/TaskUnitModel.py
--rw-r--r--   0        0        0     1015 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/TemplateUnitModel.py
--rw-r--r--   0        0        0     1987 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/job/utils.py
--rwxr-xr-x   0        0        0     1757 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/purge/PurgeContentModel.py
--rw-r--r--   0        0        0     1010 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/purge/PurgeLogsModel.py
--rw-r--r--   0        0        0      620 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/purge/PurgeModel.py
--rw-r--r--   0        0        0      949 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/t3/AliasableModel.py
--rwxr-xr-x   0        0        0     1707 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/t3/LoaderDirective.py
--rwxr-xr-x   0        0        0     5003 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/t3/QueryMatchModel.py
--rwxr-xr-x   0        0        0      577 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/t3/T2FilterModel.py
--rw-r--r--   0        0        0     2072 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/t3/T3DocBuilderModel.py
--rw-r--r--   0        0        0      969 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/t3/T3IncludeDirective.py
--rwxr-xr-x   0        0        0     1053 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/t3/T3ProjectionDirective.py
--rwxr-xr-x   0        0        0      878 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/time/QueryTimeModel.py
--rwxr-xr-x   0        0        0     2007 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/time/TimeConstraintModel.py
--rwxr-xr-x   0        0        0      988 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/time/TimeDeltaModel.py
--rwxr-xr-x   0        0        0     1592 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/time/TimeLastRunModel.py
--rw-r--r--   0        0        0      723 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/time/TimeStringModel.py
--rw-r--r--   0        0        0      587 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/model/time/UnixTimeModel.py
--rw-r--r--   0        0        0      691 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/model/AmpelColModel.py
--rw-r--r--   0        0        0      679 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/model/AmpelDBModel.py
--rw-r--r--   0        0        0      765 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/model/FieldModel.py
--rw-r--r--   0        0        0      801 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/model/IndexModel.py
--rwxr-xr-x   0        0        0     1054 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/model/MongoClientOptionsModel.py
--rw-r--r--   0        0        0      476 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/model/MongoClientRoleModel.py
--rw-r--r--   0        0        0      955 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/model/ShortIndexModel.py
--rw-r--r--   0        0        0     6236 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/purge/MongoStockDeleter.py
--rwxr-xr-x   0        0        0     1981 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/query/general.py
--rwxr-xr-x   0        0        0     2395 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/query/stock.py
--rw-r--r--   0        0        0     6067 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/query/t1.py
--rwxr-xr-x   0        0        0     3764 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/query/t2.py
--rwxr-xr-x   0        0        0     5515 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/query/var/LogsLoader.py
--rwxr-xr-x   0        0        0     4725 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/query/var/LogsMatcher.py
--rwxr-xr-x   0        0        0     3018 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/query/var/events.py
--rwxr-xr-x   0        0        0    10343 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/schema.py
--rwxr-xr-x   0        0        0    13177 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/DBUpdatesBuffer.py
--rwxr-xr-x   0        0        0     1883 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/MongoStockIngester.py
--rwxr-xr-x   0        0        0     9784 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/MongoStockUpdater.py
--rwxr-xr-x   0        0        0     1806 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/MongoT0Ingester.py
--rwxr-xr-x   0        0        0     1515 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/MongoT1Ingester.py
--rwxr-xr-x   0        0        0     1505 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/MongoT2Ingester.py
--rwxr-xr-x   0        0        0      750 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/MongoT3Ingester.py
--rwxr-xr-x   0        0        0    10782 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/update/var/DBLoggingHandler.py
--rwxr-xr-x   0        0        0     2250 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/utils.py
--rw-r--r--   0        0        0     4925 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/view/AbsMongoFlatMultiView.py
--rw-r--r--   0        0        0     2052 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/view/AbsMongoView.py
--rw-r--r--   0        0        0      963 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/view/FrozenValuesDict.py
--rw-r--r--   0        0        0      932 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/view/MongoAndView.py
--rw-r--r--   0        0        0     2390 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/view/MongoOneView.py
--rw-r--r--   0        0        0      666 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/mongo/view/MongoOrView.py
--rwxr-xr-x   0        0        0     5488 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/ops/AmpelExceptionPublisher.py
--rw-r--r--   0        0        0     1837 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/ops/OpsProcessor.py
--rw-r--r--   0        0        0        0 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/py.typed
--rwxr-xr-x   0        0        0    23965 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/run/server.py
--rwxr-xr-x   0        0        0     1346 2023-03-28 12:54:33.488615 ampel_core-0.8.6/ampel/secret/AESecretProvider.py
--rwxr-xr-x   0        0        0     1873 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/secret/DictSecretProvider.py
--rw-r--r--   0        0        0     1505 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/secret/DirSecretProvider.py
--rwxr-xr-x   0        0        0      885 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/secret/PotemkinSecretProvider.py
--rw-r--r--   0        0        0       26 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t1/README.md
--rwxr-xr-x   0        0        0      883 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t1/T1SimpleCombiner.py
--rwxr-xr-x   0        0        0     1532 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t1/T1SimpleRetroCombiner.py
--rw-r--r--   0        0        0       26 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t2/README.md
--rw-r--r--   0        0        0     4170 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t2/T2Utils.py
--rwxr-xr-x   0        0        0    21046 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t2/T2Worker.py
--rw-r--r--   0        0        0     3554 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/README.md
--rwxr-xr-x   0        0        0     6600 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/T3DocBuilder.py
--rwxr-xr-x   0        0        0     3628 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/T3PlainUnitExecutor.py
--rwxr-xr-x   0        0        0     4223 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/T3Processor.py
--rwxr-xr-x   0        0        0     2664 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/T3ReviewUnitExecutor.py
--rwxr-xr-x   0        0        0     1525 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/include/session/T3SessionAlertsNumber.py
--rwxr-xr-x   0        0        0     1482 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/include/session/T3SessionLastRunTime.py
--rwxr-xr-x   0        0        0     1664 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/BaseViewGenerator.py
--rwxr-xr-x   0        0        0     1081 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/NoViewGenerator.py
--rw-r--r--   0        0        0     3901 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/README.md
--rwxr-xr-x   0        0        0     1353 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/SimpleViewGenerator.py
--rwxr-xr-x   0        0        0     7235 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3AdaptativeStager.py
--rw-r--r--   0        0        0     5496 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3AggregatingStager.py
--rwxr-xr-x   0        0        0     2102 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3BaseStager.py
--rwxr-xr-x   0        0        0     2038 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3ChannelStager.py
--rwxr-xr-x   0        0        0     2997 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3DistributiveStager.py
--rwxr-xr-x   0        0        0     8045 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3ProjectingStager.py
--rwxr-xr-x   0        0        0     3720 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3SequentialStager.py
--rwxr-xr-x   0        0        0     1719 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3SimpleStager.py
--rwxr-xr-x   0        0        0     5581 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/T3ThreadedStager.py
--rwxr-xr-x   0        0        0     1303 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/ThreadedViewGenerator.py
--rwxr-xr-x   0        0        0     4456 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/filter/T3AmpelBufferFilter.py
--rwxr-xr-x   0        0        0     6450 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/project/T3BaseProjector.py
--rwxr-xr-x   0        0        0     3537 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/stage/project/T3ChannelProjector.py
--rwxr-xr-x   0        0        0     1510 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/SimpleT2BasedSupplier.py
--rwxr-xr-x   0        0        0     3701 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/T3DefaultBufferSupplier.py
--rwxr-xr-x   0        0        0     2583 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/complement/T3ExtJournalAppender.py
--rwxr-xr-x   0        0        0     1765 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/complement/T3LogsAppender.py
--rwxr-xr-x   0        0        0     1298 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/complement/T3RandIntAppender.py
--rwxr-xr-x   0        0        0     4727 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/load/T3LatestStateDataLoader.py
--rwxr-xr-x   0        0        0     1191 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/load/T3SimpleDataLoader.py
--rwxr-xr-x   0        0        0     5069 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/select/T3FilteringStockSelector.py
--rwxr-xr-x   0        0        0     3149 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/supply/select/T3StockSelector.py
--rwxr-xr-x   0        0        0      947 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/unit/T3LogAggregatedStocks.py
--rwxr-xr-x   0        0        0      944 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/t3/unit/T3PrintStore.py
--rw-r--r--   0        0        0     1318 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/template/ChannelWithProcsTemplate.py
--rwxr-xr-x   0        0        0     7323 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/template/PeriodicSummaryT3.py
--rwxr-xr-x   0        0        0     3385 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/template/TPLCompactT3.py
--rw-r--r--   0        0        0     7913 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/conftest.py
--rwxr-xr-x   0        0        0     4370 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/dummy.py
--rw-r--r--   0        0        0    14551 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/pylintrc
--rw-r--r--   0        0        0    69357 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test-data/ZTF20abxvcrk.pkl
--rw-r--r--   0        0        0    16287 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test-data/testing-config.yaml
--rw-r--r--   0        0        0      669 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_AbsChannelTemplate.py
--rw-r--r--   0        0        0     1801 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_AmpelContext.py
--rw-r--r--   0        0        0      295 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_AmpelController.py
--rw-r--r--   0        0        0      238 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_AmpelMetricsRegistry.py
--rw-r--r--   0        0        0     1474 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_DBUpdatesBuffer.py
--rw-r--r--   0        0        0     1220 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_DefaultProcessController.py
--rw-r--r--   0        0        0    13649 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_IngestionHandler.py
--rw-r--r--   0        0        0    10304 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_JobCommand.py
--rw-r--r--   0        0        0     3361 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_JobModel.py
--rw-r--r--   0        0        0     1651 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_PeriodicSummaryT3.py
--rw-r--r--   0        0        0     3466 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_ProcessMorpher.py
--rw-r--r--   0        0        0     1065 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_SimpleTagFilter.py
--rw-r--r--   0        0        0     6575 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_T2Processor.py
--rw-r--r--   0        0        0     4564 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_T3ChannelProjector.py
--rw-r--r--   0        0        0     2201 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_T3FilteringStockSelector.py
--rw-r--r--   0        0        0     8842 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_T3Processor.py
--rw-r--r--   0        0        0      680 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_T3SimpleDataLoader.py
--rw-r--r--   0        0        0     7446 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_UnitLoader.py
--rw-r--r--   0        0        0     8909 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_concurrent.py
--rw-r--r--   0        0        0     4343 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_config.py
--rw-r--r--   0        0        0    10294 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_server.py
--rw-r--r--   0        0        0      744 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_util_mappings.py
--rw-r--r--   0        0        0     2006 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/test/test_util_template.py
--rwxr-xr-x   0        0        0     4842 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/util/collections.py
--rwxr-xr-x   0        0        0     9905 2023-03-28 12:54:33.492615 ampel_core-0.8.6/ampel/util/concurrent.py
--rw-r--r--   0        0        0     2316 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/debug.py
--rw-r--r--   0        0        0     3653 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/distrib.py
--rw-r--r--   0        0        0      883 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/getch.py
--rwxr-xr-x   0        0        0     6044 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/logicschema.py
--rw-r--r--   0        0        0     7514 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/pretty.py
--rwxr-xr-x   0        0        0    17510 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/register.py
--rw-r--r--   0        0        0     2043 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/stock.py
--rwxr-xr-x   0        0        0     2792 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/util/template.py
--rw-r--r--   0        0        0     1070 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/vendor/aiopipe/LICENSE.txt
--rw-r--r--   0        0        0     8895 2023-03-28 12:54:33.496615 ampel_core-0.8.6/ampel/vendor/aiopipe/__init__.py
--rw-r--r--   0        0        0     2823 2023-03-28 12:54:33.496615 ampel_core-0.8.6/conf/ampel-core/ampel.yaml
--rw-r--r--   0        0        0      854 2023-03-28 12:54:33.496615 ampel_core-0.8.6/conf/ampel-core/logging.yaml
--rw-r--r--   0        0        0      526 2023-03-28 12:54:33.496615 ampel_core-0.8.6/conf/ampel-core/mongo/data.yaml
--rw-r--r--   0        0        0      109 2023-03-28 12:54:33.496615 ampel_core-0.8.6/conf/ampel-core/mongo/ext.yaml
--rw-r--r--   0        0        0      341 2023-03-28 12:54:33.496615 ampel_core-0.8.6/conf/ampel-core/mongo/var.yaml
--rw-r--r--   0        0        0     3105 2023-03-28 12:54:33.496615 ampel_core-0.8.6/pyproject.toml
--rw-r--r--   0        0        0     2086 1970-01-01 00:00:00.000000 ampel_core-0.8.6/PKG-INFO
+-rw-r--r--   0        0        0     1512 2023-04-06 19:53:42.029189 ampel_core-0.9.0/LICENSE
+-rw-r--r--   0        0        0      262 2023-04-06 19:53:42.029189 ampel_core-0.9.0/README.md
+-rwxr-xr-x   0        0        0     1251 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsBufferComplement.py
+-rw-r--r--   0        0        0     1551 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsChannelTemplate.py
+-rwxr-xr-x   0        0        0     6900 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsCompiler.py
+-rw-r--r--   0        0        0      853 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsConfigMorpher.py
+-rw-r--r--   0        0        0     1004 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsConfigUpdater.py
+-rwxr-xr-x   0        0        0      871 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsDocIngester.py
+-rwxr-xr-x   0        0        0      886 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsDocUpdater.py
+-rw-r--r--   0        0        0     4524 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsEventUnit.py
+-rw-r--r--   0        0        0     1112 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsOpsUnit.py
+-rwxr-xr-x   0        0        0     2719 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsProcessController.py
+-rwxr-xr-x   0        0        0     2334 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT0Muxer.py
+-rwxr-xr-x   0        0        0      743 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT3Filter.py
+-rwxr-xr-x   0        0        0     2502 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT3Loader.py
+-rwxr-xr-x   0        0        0      767 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT3Projector.py
+-rwxr-xr-x   0        0        0      777 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT3Selector.py
+-rwxr-xr-x   0        0        0     1239 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT3Stager.py
+-rwxr-xr-x   0        0        0      939 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT3Supplier.py
+-rwxr-xr-x   0        0        0      979 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsT4ControlUnit.py
+-rw-r--r--   0        0        0      593 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsTargetSource.py
+-rwxr-xr-x   0        0        0      700 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsUnitResultAdapter.py
+-rwxr-xr-x   0        0        0    13587 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/AbsWorker.py
+-rw-r--r--   0        0        0      282 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/abstract/README.md
+-rwxr-xr-x   0        0        0    11114 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/aux/ComboDictModifier.py
+-rw-r--r--   0        0        0     1248 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/aux/SimpleTagFilter.py
+-rwxr-xr-x   0        0        0     1575 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/aux/filter/AbsLogicOperatorFilter.py
+-rw-r--r--   0        0        0     1192 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/aux/filter/FlatDictArrayFilter.py
+-rw-r--r--   0        0        0     1116 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/aux/filter/PrimitiveTypeArrayFilter.py
+-rw-r--r--   0        0        0     1768 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/aux/filter/SimpleDictArrayFilter.py
+-rw-r--r--   0        0        0     4243 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/AbsCoreCommand.py
+-rw-r--r--   0        0        0     2134 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/AbsLoadCommand.py
+-rwxr-xr-x   0        0        0     6032 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/AbsStockCommand.py
+-rw-r--r--   0        0        0     4200 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/BufferCommand.py
+-rw-r--r--   0        0        0    11533 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/ConfigCommand.py
+-rw-r--r--   0        0        0     4955 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/DBCommand.py
+-rw-r--r--   0        0        0     5939 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/EventCommand.py
+-rw-r--r--   0        0        0    23434 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/JobCommand.py
+-rw-r--r--   0        0        0     8842 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/LogCommand.py
+-rw-r--r--   0        0        0     5808 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/ProcessCommand.py
+-rw-r--r--   0        0        0     3321 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/RunCommand.py
+-rw-r--r--   0        0        0     6326 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/StartCommand.py
+-rw-r--r--   0        0        0     9315 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/T2Command.py
+-rw-r--r--   0        0        0     2170 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/T3BufferExporterStager.py
+-rw-r--r--   0        0        0     1870 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/T3BufferExporterUnit.py
+-rw-r--r--   0        0        0     4388 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/ViewCommand.py
+-rw-r--r--   0        0        0     4434 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/export.py
+-rw-r--r--   0        0        0     3362 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/cli/utils.py
+-rwxr-xr-x   0        0        0     1301 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/ScheduleEvaluator.py
+-rw-r--r--   0        0        0     1604 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/alter/HashT2Config.py
+-rw-r--r--   0        0        0     1605 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/alter/ResolveRunTimeAliases.py
+-rw-r--r--   0        0        0     1746 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/BaseConfigChecker.py
+-rwxr-xr-x   0        0        0    20019 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/ConfigBuilder.py
+-rw-r--r--   0        0        0     7539 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/ConfigChecker.py
+-rw-r--r--   0        0        0     1671 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/ConfigValidator.py
+-rwxr-xr-x   0        0        0      570 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/DisplayOptions.py
+-rwxr-xr-x   0        0        0     8493 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/DistConfigBuilder.py
+-rwxr-xr-x   0        0        0     3669 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/FirstPassConfig.py
+-rwxr-xr-x   0        0        0     8969 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/ProcessMorpher.py
+-rw-r--r--   0        0        0     1000 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/builder/get_env.py
+-rwxr-xr-x   0        0        0     1511 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/AbsDictConfigCollector.py
+-rwxr-xr-x   0        0        0     2560 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/AbsForwardConfigCollector.py
+-rwxr-xr-x   0        0        0      770 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/AbsListConfigCollector.py
+-rwxr-xr-x   0        0        0     1985 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/AliasConfigCollector.py
+-rwxr-xr-x   0        0        0     1826 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/ChannelConfigCollector.py
+-rwxr-xr-x   0        0        0     2728 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/ConfigCollector.py
+-rwxr-xr-x   0        0        0     2387 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/DBConfigCollector.py
+-rwxr-xr-x   0        0        0     1243 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/ForwardProcessConfigCollector.py
+-rwxr-xr-x   0        0        0     1958 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/LoggingCollector.py
+-rwxr-xr-x   0        0        0     1390 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/ProcessConfigCollector.py
+-rwxr-xr-x   0        0        0     1673 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/ResourceConfigCollector.py
+-rwxr-xr-x   0        0        0     1648 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/T02ConfigCollector.py
+-rwxr-xr-x   0        0        0     7085 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/config/collector/UnitConfigCollector.py
+-rwxr-xr-x   0        0        0     6743 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/core/AmpelContext.py
+-rwxr-xr-x   0        0        0    10976 2023-04-06 19:53:42.029189 ampel_core-0.9.0/ampel/core/AmpelController.py
+-rwxr-xr-x   0        0        0    19022 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/AmpelDB.py
+-rwxr-xr-x   0        0        0    17800 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/AmpelRegister.py
+-rwxr-xr-x   0        0        0      861 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/ContextUnit.py
+-rwxr-xr-x   0        0        0     6353 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/DataLoader.py
+-rwxr-xr-x   0        0        0    10174 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/DefaultProcessController.py
+-rw-r--r--   0        0        0     4740 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/DocBuilder.py
+-rwxr-xr-x   0        0        0     4688 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/EventHandler.py
+-rwxr-xr-x   0        0        0     3642 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/Schedulable.py
+-rwxr-xr-x   0        0        0    14844 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/core/UnitLoader.py
+-rw-r--r--   0        0        0      855 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/demo/DemoFirstPointT2Unit.py
+-rw-r--r--   0        0        0     1075 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/demo/DemoPointT2Unit.py
+-rw-r--r--   0        0        0     1633 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/demo/DemoProcessor.py
+-rw-r--r--   0        0        0     1336 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/demo/DemoT3Unit.py
+-rwxr-xr-x   0        0        0      878 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/demo/DemoT4RunTimeAliasGenerator.py
+-rwxr-xr-x   0        0        0     3818 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/dev/DevAmpelContext.py
+-rw-r--r--   0        0        0      841 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/dev/NoShaper.py
+-rwxr-xr-x   0        0        0    27480 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/ingest/ChainedIngestionHandler.py
+-rw-r--r--   0        0        0     1435 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/ingest/ChainedT0Muxer.py
+-rw-r--r--   0        0        0     3115 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/ingest/StockCompiler.py
+-rw-r--r--   0        0        0     2480 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/ingest/T0Compiler.py
+-rw-r--r--   0        0        0     5255 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/ingest/T1Compiler.py
+-rw-r--r--   0        0        0     3009 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/ingest/T2Compiler.py
+-rwxr-xr-x   0        0        0     8036 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/AmpelLogger.py
+-rwxr-xr-x   0        0        0      389 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/AmpelLoggingError.py
+-rw-r--r--   0        0        0     1424 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/LightLogRecord.py
+-rw-r--r--   0        0        0     1195 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/LogFlag.py
+-rwxr-xr-x   0        0        0     1491 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/LoggingErrorReporter.py
+-rw-r--r--   0        0        0     3975 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/LogsDumper.py
+-rw-r--r--   0        0        0      477 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/__init__.py
+-rwxr-xr-x   0        0        0     6010 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/handlers/AmpelStreamHandler.py
+-rwxr-xr-x   0        0        0     2443 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/handlers/ChanRecordBufHandler.py
+-rw-r--r--   0        0        0     2006 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/handlers/DefaultRecordBufferingHandler.py
+-rw-r--r--   0        0        0     1712 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/handlers/EnclosedChanRecordBufHandler.py
+-rw-r--r--   0        0        0     1528 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/handlers/RecordBufferingHandler.py
+-rwxr-xr-x   0        0        0     8251 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/log/utils.py
+-rw-r--r--   0        0        0     1212 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/metrics/AmpelDBCollector.py
+-rw-r--r--   0        0        0     2387 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/metrics/AmpelMetricsRegistry.py
+-rw-r--r--   0        0        0     1940 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/metrics/AmpelProcessCollector.py
+-rw-r--r--   0        0        0     5175 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/metrics/prometheus.py
+-rwxr-xr-x   0        0        0     1059 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ChannelModel.py
+-rwxr-xr-x   0        0        0     1484 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ProcessModel.py
+-rw-r--r--   0        0        0       93 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/Readme.md
+-rw-r--r--   0        0        0      856 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/aux/AuxAliasableModel.py
+-rw-r--r--   0        0        0     1253 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/aux/FilterCriterion.py
+-rw-r--r--   0        0        0      580 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/builder/BuilderAliasModel.py
+-rw-r--r--   0        0        0      526 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/builder/RemoteUnitDefinition.py
+-rwxr-xr-x   0        0        0      938 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/CompilerOptions.py
+-rw-r--r--   0        0        0     2044 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/DualIngestDirective.py
+-rw-r--r--   0        0        0      737 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/FilterModel.py
+-rw-r--r--   0        0        0     2065 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/IngestBody.py
+-rw-r--r--   0        0        0     1286 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/IngestDirective.py
+-rw-r--r--   0        0        0     1451 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/MuxModel.py
+-rwxr-xr-x   0        0        0     1215 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/T1Combine.py
+-rwxr-xr-x   0        0        0      780 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/T1CombineCompute.py
+-rwxr-xr-x   0        0        0     1369 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/T1CombineComputeNow.py
+-rwxr-xr-x   0        0        0      785 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/ingest/T2Compute.py
+-rw-r--r--   0        0        0      459 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/job/EnvSpec.py
+-rw-r--r--   0        0        0     1211 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/job/JobModel.py
+-rw-r--r--   0        0        0     1715 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/job/JobTaskModel.py
+-rw-r--r--   0        0        0      407 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/job/MongoOpts.py
+-rwxr-xr-x   0        0        0     1757 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/purge/PurgeContentModel.py
+-rw-r--r--   0        0        0     1010 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/purge/PurgeLogsModel.py
+-rw-r--r--   0        0        0      620 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/purge/PurgeModel.py
+-rw-r--r--   0        0        0      949 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/t3/AliasableModel.py
+-rwxr-xr-x   0        0        0     1707 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/t3/LoaderDirective.py
+-rwxr-xr-x   0        0        0     5003 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/t3/QueryMatchModel.py
+-rwxr-xr-x   0        0        0      577 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/t3/T2FilterModel.py
+-rw-r--r--   0        0        0      969 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/t3/T3IncludeDirective.py
+-rwxr-xr-x   0        0        0     1047 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/t3/T3ProjectionDirective.py
+-rwxr-xr-x   0        0        0      878 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/time/QueryTimeModel.py
+-rwxr-xr-x   0        0        0     2007 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/time/TimeConstraintModel.py
+-rwxr-xr-x   0        0        0      988 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/time/TimeDeltaModel.py
+-rwxr-xr-x   0        0        0     1592 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/time/TimeLastRunModel.py
+-rw-r--r--   0        0        0      723 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/time/TimeStringModel.py
+-rw-r--r--   0        0        0      587 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/model/time/UnixTimeModel.py
+-rw-r--r--   0        0        0      691 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/model/AmpelColModel.py
+-rw-r--r--   0        0        0      679 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/model/AmpelDBModel.py
+-rw-r--r--   0        0        0      765 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/model/FieldModel.py
+-rw-r--r--   0        0        0      801 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/model/IndexModel.py
+-rwxr-xr-x   0        0        0     1054 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/model/MongoClientOptionsModel.py
+-rw-r--r--   0        0        0      476 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/model/MongoClientRoleModel.py
+-rw-r--r--   0        0        0      955 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/model/ShortIndexModel.py
+-rw-r--r--   0        0        0     6236 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/purge/MongoStockDeleter.py
+-rwxr-xr-x   0        0        0     1981 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/query/general.py
+-rwxr-xr-x   0        0        0     2395 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/query/stock.py
+-rw-r--r--   0        0        0     6067 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/query/t1.py
+-rwxr-xr-x   0        0        0     3764 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/query/t2.py
+-rwxr-xr-x   0        0        0     5515 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/query/var/LogsLoader.py
+-rwxr-xr-x   0        0        0     4725 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/query/var/LogsMatcher.py
+-rwxr-xr-x   0        0        0     3018 2023-04-06 19:53:42.033189 ampel_core-0.9.0/ampel/mongo/query/var/events.py
+-rwxr-xr-x   0        0        0    10343 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/schema.py
+-rwxr-xr-x   0        0        0    13177 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/DBUpdatesBuffer.py
+-rwxr-xr-x   0        0        0     1883 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/MongoStockIngester.py
+-rwxr-xr-x   0        0        0     9784 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/MongoStockUpdater.py
+-rwxr-xr-x   0        0        0     1806 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/MongoT0Ingester.py
+-rwxr-xr-x   0        0        0     1515 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/MongoT1Ingester.py
+-rwxr-xr-x   0        0        0     1505 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/MongoT2Ingester.py
+-rwxr-xr-x   0        0        0      750 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/MongoT3Ingester.py
+-rwxr-xr-x   0        0        0    10782 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/update/var/DBLoggingHandler.py
+-rwxr-xr-x   0        0        0     2250 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/utils.py
+-rw-r--r--   0        0        0     4925 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/view/AbsMongoFlatMultiView.py
+-rw-r--r--   0        0        0     2052 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/view/AbsMongoView.py
+-rw-r--r--   0        0        0      963 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/view/FrozenValuesDict.py
+-rw-r--r--   0        0        0      932 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/view/MongoAndView.py
+-rw-r--r--   0        0        0     2390 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/view/MongoOneView.py
+-rw-r--r--   0        0        0      666 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/mongo/view/MongoOrView.py
+-rwxr-xr-x   0        0        0     5488 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/ops/AmpelExceptionPublisher.py
+-rw-r--r--   0        0        0     1837 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/ops/OpsProcessor.py
+-rw-r--r--   0        0        0        0 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/py.typed
+-rwxr-xr-x   0        0        0    23965 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/run/server.py
+-rwxr-xr-x   0        0        0     1346 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/secret/AESecretProvider.py
+-rwxr-xr-x   0        0        0     1873 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/secret/DictSecretProvider.py
+-rw-r--r--   0        0        0     1505 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/secret/DirSecretProvider.py
+-rwxr-xr-x   0        0        0      885 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/secret/PotemkinSecretProvider.py
+-rw-r--r--   0        0        0       26 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t1/README.md
+-rwxr-xr-x   0        0        0      883 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t1/T1SimpleCombiner.py
+-rwxr-xr-x   0        0        0     1532 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t1/T1SimpleRetroCombiner.py
+-rw-r--r--   0        0        0       26 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t2/README.md
+-rw-r--r--   0        0        0     4170 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t2/T2Utils.py
+-rwxr-xr-x   0        0        0    21046 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t2/T2Worker.py
+-rw-r--r--   0        0        0     3548 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/README.md
+-rwxr-xr-x   0        0        0     3774 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/T3Processor.py
+-rwxr-xr-x   0        0        0     1525 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/include/session/T3SessionAlertsNumber.py
+-rwxr-xr-x   0        0        0     1482 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/include/session/T3SessionLastRunTime.py
+-rwxr-xr-x   0        0        0     1664 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/BaseViewGenerator.py
+-rwxr-xr-x   0        0        0     1063 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/NoViewGenerator.py
+-rw-r--r--   0        0        0     3901 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/README.md
+-rwxr-xr-x   0        0        0     1335 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/SimpleViewGenerator.py
+-rwxr-xr-x   0        0        0     7368 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3AdaptativeStager.py
+-rw-r--r--   0        0        0     6354 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3AggregatingStager.py
+-rwxr-xr-x   0        0        0     4982 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3BaseStager.py
+-rwxr-xr-x   0        0        0     2038 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3ChannelStager.py
+-rwxr-xr-x   0        0        0     3097 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3DistributiveStager.py
+-rwxr-xr-x   0        0        0     8016 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3ProjectingStager.py
+-rwxr-xr-x   0        0        0     3823 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3SequentialStager.py
+-rwxr-xr-x   0        0        0     1689 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3SimpleStager.py
+-rwxr-xr-x   0        0        0     5629 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/T3ThreadedStager.py
+-rwxr-xr-x   0        0        0     1297 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/ThreadedViewGenerator.py
+-rwxr-xr-x   0        0        0     4456 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/filter/T3AmpelBufferFilter.py
+-rwxr-xr-x   0        0        0     6450 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/project/T3BaseProjector.py
+-rwxr-xr-x   0        0        0     3537 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/stage/project/T3ChannelProjector.py
+-rwxr-xr-x   0        0        0     1510 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/SimpleT2BasedSupplier.py
+-rwxr-xr-x   0        0        0     3701 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/T3DefaultBufferSupplier.py
+-rwxr-xr-x   0        0        0     2583 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/complement/T3ExtJournalAppender.py
+-rwxr-xr-x   0        0        0     1765 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/complement/T3LogsAppender.py
+-rwxr-xr-x   0        0        0     1298 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/complement/T3RandIntAppender.py
+-rwxr-xr-x   0        0        0     4727 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/load/T3LatestStateDataLoader.py
+-rwxr-xr-x   0        0        0     1191 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/load/T3SimpleDataLoader.py
+-rwxr-xr-x   0        0        0     5069 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/select/T3FilteringStockSelector.py
+-rwxr-xr-x   0        0        0     3149 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/supply/select/T3StockSelector.py
+-rwxr-xr-x   0        0        0      951 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t3/unit/T3LogAggregatedStocks.py
+-rwxr-xr-x   0        0        0     3082 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t4/T4Processor.py
+-rw-r--r--   0        0        0     1994 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/t4/T4RunTimeContextUpdater.py
+-rw-r--r--   0        0        0     1318 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/template/ChannelWithProcsTemplate.py
+-rwxr-xr-x   0        0        0     6163 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/template/PeriodicSummaryT3.py
+-rwxr-xr-x   0        0        0      464 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/test/DummyStateT2Unit.py
+-rw-r--r--   0        0        0     7955 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/test/conftest.py
+-rwxr-xr-x   0        0        0     4312 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/test/dummy.py
+-rw-r--r--   0        0        0    14551 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/test/pylintrc
+-rw-r--r--   0        0        0    69357 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/test/test-data/ZTF20abxvcrk.pkl
+-rw-r--r--   0        0        0    15835 2023-04-06 19:53:42.037189 ampel_core-0.9.0/ampel/test/test-data/testing-config.yaml
+-rw-r--r--   0        0        0      669 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_AbsChannelTemplate.py
+-rw-r--r--   0        0        0     1955 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_AmpelContext.py
+-rw-r--r--   0        0        0      295 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_AmpelController.py
+-rw-r--r--   0        0        0      238 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_AmpelMetricsRegistry.py
+-rw-r--r--   0        0        0     1474 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_DBUpdatesBuffer.py
+-rw-r--r--   0        0        0     1220 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_DefaultProcessController.py
+-rw-r--r--   0        0        0    13649 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_IngestionHandler.py
+-rw-r--r--   0        0        0     3431 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_JobCommand.py
+-rw-r--r--   0        0        0     1632 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_PeriodicSummaryT3.py
+-rw-r--r--   0        0        0     3466 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_ProcessMorpher.py
+-rw-r--r--   0        0        0     1065 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_SimpleTagFilter.py
+-rw-r--r--   0        0        0     6575 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_T2Processor.py
+-rw-r--r--   0        0        0     4564 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_T3ChannelProjector.py
+-rw-r--r--   0        0        0     2201 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_T3FilteringStockSelector.py
+-rw-r--r--   0        0        0     7258 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_T3Processor.py
+-rw-r--r--   0        0        0      680 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_T3SimpleDataLoader.py
+-rw-r--r--   0        0        0     7030 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_UnitLoader.py
+-rw-r--r--   0        0        0     8909 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_concurrent.py
+-rw-r--r--   0        0        0     4343 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_config.py
+-rw-r--r--   0        0        0    10276 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_server.py
+-rw-r--r--   0        0        0      744 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_util_mappings.py
+-rw-r--r--   0        0        0     2006 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/test/test_util_template.py
+-rwxr-xr-x   0        0        0     4842 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/collections.py
+-rwxr-xr-x   0        0        0     9905 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/concurrent.py
+-rw-r--r--   0        0        0      822 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/config.py
+-rw-r--r--   0        0        0     2316 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/debug.py
+-rw-r--r--   0        0        0     3653 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/distrib.py
+-rw-r--r--   0        0        0      883 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/getch.py
+-rwxr-xr-x   0        0        0     6044 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/logicschema.py
+-rw-r--r--   0        0        0     7514 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/pretty.py
+-rwxr-xr-x   0        0        0    17510 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/register.py
+-rw-r--r--   0        0        0     2043 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/stock.py
+-rwxr-xr-x   0        0        0     3879 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/util/template.py
+-rw-r--r--   0        0        0     1070 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/vendor/aiopipe/LICENSE.txt
+-rw-r--r--   0        0        0     8895 2023-04-06 19:53:42.041189 ampel_core-0.9.0/ampel/vendor/aiopipe/__init__.py
+-rw-r--r--   0        0        0     2837 2023-04-06 19:53:42.041189 ampel_core-0.9.0/conf/ampel-core/ampel.yaml
+-rw-r--r--   0        0        0      854 2023-04-06 19:53:42.041189 ampel_core-0.9.0/conf/ampel-core/logging.yaml
+-rw-r--r--   0        0        0      586 2023-04-06 19:53:42.041189 ampel_core-0.9.0/conf/ampel-core/mongo/data.yaml
+-rw-r--r--   0        0        0      109 2023-04-06 19:53:42.041189 ampel_core-0.9.0/conf/ampel-core/mongo/ext.yaml
+-rw-r--r--   0        0        0      341 2023-04-06 19:53:42.041189 ampel_core-0.9.0/conf/ampel-core/mongo/var.yaml
+-rw-r--r--   0        0        0     3105 2023-04-06 19:53:42.041189 ampel_core-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0     2087 1970-01-01 00:00:00.000000 ampel_core-0.9.0/PKG-INFO
```

### Comparing `ampel_core-0.8.6/LICENSE` & `ampel_core-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsBufferComplement.py` & `ampel_core-0.9.0/ampel/abstract/AbsBufferComplement.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsChannelTemplate.py` & `ampel_core-0.9.0/ampel/abstract/AbsChannelTemplate.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,30 +1,31 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/abstract/AbsChannelTemplate.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                27.10.2019
-# Last Modified Date:  07.04.2020
+# Last Modified Date:  04.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any
 from ampel.base.decorator import abstractmethod
+from ampel.base.AmpelABC import AmpelABC
 from ampel.log.AmpelLogger import AmpelLogger
 from ampel.model.ChannelModel import ChannelModel
 from ampel.config.builder.FirstPassConfig import FirstPassConfig
-from ampel.config.builder.AbsConfigTemplate import AbsConfigTemplate
 
 
-class AbsChannelTemplate(AbsConfigTemplate, ChannelModel, abstract=True):
+class AbsChannelTemplate(AmpelABC, ChannelModel, abstract=True):
 
+	template: None | str
 
 	def get_channel(self, logger: AmpelLogger) -> dict[str, Any]:
 		keys = ChannelModel.get_model_keys()
-		return {k: v for k,v in self.__dict__.items() if k in keys}
+		return {k: v for k, v in self.__dict__.items() if k in keys}
 
 	@abstractmethod
 	def get_processes(self, logger: AmpelLogger, first_pass_config: FirstPassConfig) -> list[dict[str, Any]]:
 		...
 
 	def transfer_channel_parameters(self, process: dict[str, Any]) -> dict[str, Any]:
 		"""
```

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsCompiler.py` & `ampel_core-0.9.0/ampel/abstract/AbsCompiler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsDocIngester.py` & `ampel_core-0.9.0/ampel/abstract/AbsDocIngester.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsDocUpdater.py` & `ampel_core-0.9.0/ampel/abstract/AbsDocUpdater.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsEventUnit.py` & `ampel_core-0.9.0/ampel/abstract/AbsEventUnit.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,24 +1,28 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/abstract/AbsEventUnit.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                04.02.2020
-# Last Modified Date:  25.07.2022
+# Last Modified Date:  05.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any
+from typing_extensions import Self
+from collections.abc import Sequence
 from ampel.types import ChannelId, OneOrMany, Traceless
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod, defaultmethod
 from ampel.core.EventHandler import EventHandler
 from ampel.core.ContextUnit import ContextUnit
 from ampel.enum.EventCode import EventCode
 from ampel.log.LogFlag import LogFlag
+from ampel.log.utils import get_logger
+from ampel.util.template import apply_templates
 
 
 class AbsEventUnit(AmpelABC, ContextUnit, abstract=True):
 	"""
 	Base class for units orchestrating an ampel event.
 	Ampel processes (from the ampel config) are the most common events.
 	They define specifications of an event using a standardized model/schema:
@@ -76,14 +80,21 @@
 
 
 	@abstractmethod(var_args=True)
 	def proceed(self, event_hdlr: EventHandler) -> Any:
 		...
 
 
+	@classmethod
+	def new(cls, templates: str | Sequence[str], **kwargs) -> Self:
+		""" To use with jupyter when templating is wished for """
+		with get_logger(kwargs['context'].config, kwargs.get('log_profile', None)) as logger:
+			return cls(**apply_templates(kwargs['context'], templates, kwargs, logger))
+
+
 	def run(self, event_hdlr: None | EventHandler = None) -> Any:
 
 		if event_hdlr is None:
 			event_hdlr = EventHandler(
 				self.process_name,
 				self.context.get_database(),
 				job_sig = self.job_sig,
@@ -113,9 +124,9 @@
 		# Set default event code if sub-class didn't customize it
 		if event_hdlr.code is None:
 			event_hdlr.code = EventCode.OK
 
 		# Update duration and code in event doc
 		event_hdlr.update()
 
-		# Forward returned run() value to caller
+		# Forward value returned by proceed() to caller
 		return ret
```

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsOpsUnit.py` & `ampel_core-0.9.0/ampel/abstract/AbsOpsUnit.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsProcessController.py` & `ampel_core-0.9.0/ampel/abstract/AbsProcessController.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsProcessTemplate.py` & `ampel_core-0.9.0/ampel/abstract/AbsConfigMorpher.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,20 +1,26 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File:                ampel/abstract/AbsProcessTemplate.py
+# File:                Ampel-core/ampel/abstract/AbsConfigMorpher.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                27.10.2019
-# Last Modified Date:  27.10.2019
+# Last Modified Date:  05.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any
 from ampel.log.AmpelLogger import AmpelLogger
 from ampel.base.decorator import abstractmethod
-from ampel.config.builder.AbsConfigTemplate import AbsConfigTemplate
+from ampel.base.AmpelABC import AmpelABC
+from ampel.base.AmpelBaseModel import AmpelBaseModel
 
 
-class AbsProcessTemplate(AbsConfigTemplate, abstract=True):
+class AbsConfigMorpher(AmpelABC, AmpelBaseModel, abstract=True):
+	"""
+	Template class aiming at forging processes conforming with ProcessModel
+	"""
+
+	template: None | str
 
 	@abstractmethod
-	def get_process(self, config: dict[str, Any], logger: AmpelLogger) -> dict[str, Any]:
+	def morph(self, ampel_config: dict[str, Any], logger: AmpelLogger) -> dict[str, Any]:
 		...
```

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsProcessorTemplate.py` & `ampel_core-0.9.0/ampel/dev/NoShaper.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,21 +1,25 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File:                Ampel-core/ampel/abstract/AbsProcessorTemplate.py
+# File:                Ampel-core/ampel/dev/NoShaper.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
-# Date:                16.07.2021
-# Last Modified Date:  16.07.2021
+# Date:                05.08.2021
+# Last Modified Date:  05.08.2021
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any
+from collections.abc import Iterable
+from ampel.types import StockId
+from ampel.abstract.AbsT0Unit import AbsT0Unit
+from ampel.content.DataPoint import DataPoint
 from ampel.log.AmpelLogger import AmpelLogger
-from ampel.base.decorator import abstractmethod
-from ampel.model.UnitModel import UnitModel
-from ampel.config.builder.AbsConfigTemplate import AbsConfigTemplate
 
 
-class AbsProcessorTemplate(AbsConfigTemplate, abstract=True):
+class NoShaper(AbsT0Unit):
 
-	@abstractmethod
-	def get_model(self, config: dict[str, Any], logger: AmpelLogger) -> UnitModel:
-		...
+	# override
+	logger: None | AmpelLogger # type: ignore[assignment]
+
+	# Mandatory implementation
+	def process(self, arg: Iterable[dict[str, Any]], stock: StockId) -> list[DataPoint]: # type: ignore[override]
+		return arg # type: ignore
```

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsT0Muxer.py` & `ampel_core-0.9.0/ampel/abstract/AbsT0Muxer.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsT3Filter.py` & `ampel_core-0.9.0/ampel/abstract/AbsT3Filter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsT3Loader.py` & `ampel_core-0.9.0/ampel/abstract/AbsT3Loader.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsT3Projector.py` & `ampel_core-0.9.0/ampel/abstract/AbsT3Projector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsT3Selector.py` & `ampel_core-0.9.0/ampel/abstract/AbsT3Selector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsT3Stager.py` & `ampel_core-0.9.0/ampel/abstract/AbsT3Stager.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsT3Supplier.py` & `ampel_core-0.9.0/ampel/abstract/AbsT3Supplier.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsTargetSource.py` & `ampel_core-0.9.0/ampel/abstract/AbsTargetSource.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsUnitResultAdapter.py` & `ampel_core-0.9.0/ampel/abstract/AbsUnitResultAdapter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/abstract/AbsWorker.py` & `ampel_core-0.9.0/ampel/abstract/AbsWorker.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/abstract/AbsWorker.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                28.05.2021
-# Last Modified Date:  15.12.2022
+# Last Modified Date:  03.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import gc, signal
 import random
 from math import ceil
 from time import time, sleep
 from typing import ClassVar, Any, TypeVar, Generic, Literal
@@ -26,15 +26,14 @@
 from ampel.content.T1Document import T1Document
 from ampel.content.T2Document import T2Document
 from ampel.enum.MetaActionCode import MetaActionCode
 from ampel.enum.EventCode import EventCode
 from ampel.log import AmpelLogger, LogFlag, VERBOSE, DEBUG
 from ampel.core.EventHandler import EventHandler
 from ampel.log.utils import report_exception, report_error
-from ampel.log.handlers.DefaultRecordBufferingHandler import DefaultRecordBufferingHandler
 from ampel.util.hash import build_unsafe_dict_id
 from ampel.abstract.AbsEventUnit import AbsEventUnit
 from ampel.abstract.AbsUnitResultAdapter import AbsUnitResultAdapter
 from ampel.model.UnitModel import UnitModel
 from ampel.mongo.update.MongoStockUpdater import MongoStockUpdater
 from ampel.mongo.utils import maybe_use_each
 from ampel.metrics.AmpelMetricsRegistry import AmpelMetricsRegistry, Histogram, Counter
@@ -425,34 +424,22 @@
 	) -> LogicalUnit:
 
 		k = f'{doc["unit"]}_{doc["config"]}'
 
 		# Check if T2 instance exists in this run
 		if k not in self._instances:
 
-			# Create channel (buffering) logger
-			buf_hdlr = DefaultRecordBufferingHandler(level=logger.level)
-			buf_hdlr._unit = doc['unit']
-			buf_logger = AmpelLogger.get_logger(
-				name = k,
-				base_flag = (getattr(logger, 'base_flag', 0) & ~LogFlag.CORE) | LogFlag.UNIT,
-				console = False,
-				handlers = [buf_hdlr]
+			# Instantiates unit with logger based on DefaultRecordBufferingHandler
+			self._instances[k] = self.context.loader.new_safe_logical_unit(
+				UnitModel(unit=doc['unit'], config=doc['config']),
+				unit_type = LogicalUnit, # maybe restrict more in the future
+				logger = logger,
+				_chan = doc.get('channel') # type: ignore # probably not good to
 			)
 
-			# Instantiate unit
-			unit_instance = self._loader.new_logical_unit(
-				model = UnitModel(unit=doc['unit'], config=doc['config']),
-				logger = buf_logger
-			)
-
-			# Shortcut to avoid unit_instance.logger.handlers[?]
-			setattr(unit_instance, '_buf_hdlr', buf_hdlr)
-			self._instances[k] = unit_instance
-
 		return self._instances[k]
 
 
 def register_stats(tier: int) -> tuple[Histogram, Counter]:
 
 	hist = AmpelMetricsRegistry.histogram(
 		'latency',
```

### Comparing `ampel_core-0.8.6/ampel/aux/ComboDictModifier.py` & `ampel_core-0.9.0/ampel/aux/ComboDictModifier.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/aux/SimpleTagFilter.py` & `ampel_core-0.9.0/ampel/aux/SimpleTagFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/aux/filter/AbsLogicOperatorFilter.py` & `ampel_core-0.9.0/ampel/aux/filter/AbsLogicOperatorFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/aux/filter/FlatDictArrayFilter.py` & `ampel_core-0.9.0/ampel/aux/filter/FlatDictArrayFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/aux/filter/PrimitiveTypeArrayFilter.py` & `ampel_core-0.9.0/ampel/aux/filter/PrimitiveTypeArrayFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/aux/filter/SimpleDictArrayFilter.py` & `ampel_core-0.9.0/ampel/aux/filter/SimpleDictArrayFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/AbsCoreCommand.py` & `ampel_core-0.9.0/ampel/cli/AbsCoreCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/AbsLoadCommand.py` & `ampel_core-0.9.0/ampel/cli/AbsLoadCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/AbsStockCommand.py` & `ampel_core-0.9.0/ampel/cli/AbsStockCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/BufferCommand.py` & `ampel_core-0.9.0/ampel/cli/BufferCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/ConfigCommand.py` & `ampel_core-0.9.0/ampel/cli/ConfigCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/DBCommand.py` & `ampel_core-0.9.0/ampel/cli/DBCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/EventCommand.py` & `ampel_core-0.9.0/ampel/cli/EventCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/JobCommand.py` & `ampel_core-0.9.0/ampel/cli/JobCommand.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,46 +1,43 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/cli/JobCommand.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                15.03.2021
-# Last Modified Date:  09.02.2023
+# Last Modified Date:  05.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-import tarfile, tempfile, ujson, yaml, io, os, signal, sys, \
+import tempfile, ujson, yaml, io, os, signal, sys, \
 	subprocess, platform, shutil, filecmp, psutil, pkg_resources
-import requests
 from time import time, sleep
 from multiprocessing import Queue, Process
 from argparse import ArgumentParser
-from importlib import import_module
-from typing import Any
+from typing import Any, Type
 from collections.abc import Sequence
 from ampel.abstract.AbsEventUnit import AbsEventUnit
-from ampel.abstract.AbsProcessorTemplate import AbsProcessorTemplate
 from ampel.model.UnitModel import UnitModel
-from ampel.struct.Resource import Resource
 from ampel.core.EventHandler import EventHandler
+from ampel.core.AmpelContext import AmpelContext
 from ampel.dev.DevAmpelContext import DevAmpelContext
 from ampel.log.AmpelLogger import AmpelLogger
 from ampel.log.LogFlag import LogFlag
 from ampel.util.freeze import recursive_freeze
 from ampel.util.hash import build_unsafe_dict_id
 from ampel.util.distrib import get_dist_names
 from ampel.util.collections import try_reduce
+from ampel.util.template import apply_templates
+from ampel.util.pretty import prettyjson
 from ampel.cli.config import get_user_data_config_path
 from ampel.cli.utils import _maybe_int
 from ampel.cli.AbsCoreCommand import AbsCoreCommand
 from ampel.cli.MaybeIntAction import MaybeIntAction
 from ampel.cli.AmpelArgumentParser import AmpelArgumentParser
 from ampel.model.job.JobModel import JobModel
-from ampel.model.job.InputArtifact import InputArtifact
-from ampel.model.job.TaskUnitModel import TaskUnitModel
-from ampel.model.job.TemplateUnitModel import TemplateUnitModel
+from ampel.model.job.JobTaskModel import JobTaskModel
 from ampel.util.pretty import out_stack, get_time_delta
 from ampel.util.debug import MockPool
 from ampel.util.getch import yes_no
 
 
 class JobCommand(AbsCoreCommand):
 	"""
@@ -50,29 +47,33 @@
 	- contains configurations of processor units to be run sequentially
 	- should also contain everything required to run the underlying processors, that is:
 	  channels or aliases definitions and custom resources potentially required by processors.
 	- requires access to an ampel config file since the database, unit and resource definitions
 	  defined therein are necessary (might be improved in the future)
 	"""
 
-	def __init__(self):
+	def __init__(self) -> None:
 		self.parser = None
 		super().__init__()
 
 	@staticmethod
 	def get_sub_ops() -> None | list[str]:
 		return None
 
+	def get_cli_op_name(self) -> str:
+		return "job"
+
 	# Mandatory implementation
 	def get_parser(self, sub_op: None | str = None) -> ArgumentParser | AmpelArgumentParser:
 
 		if self.parser:
 			return self.parser
 
-		parser = AmpelArgumentParser('job')
+		op = self.get_cli_op_name()
+		parser = AmpelArgumentParser(op)
 		parser.args_not_required = True
 		parser.set_help_descr({
 			'debug': 'Debug',
 			#'verbose': 'increases verbosity',
 			'config': 'path to an ampel config file (yaml/json)',
 			'schema': 'path to YAML job file (multiple files will be aggregated)',
 			'secrets': 'path to a YAML secrets store in sops format',
@@ -89,15 +90,15 @@
 					'"parsed": edit (possibly aggregated) schema after parsing by the yaml interpreter\n' +
 					'"model": edit job model after templating (if applicable). Only task-related changes will be taken into account',
 			'keep-edits': 'do not remove edited job schemas from temp dir',
 			'fzf': 'choose schema file using fzf (linux/max only, fzf command line utility must be installed)',
 			'task': 'only execute task(s) with provided index(es) [starting with 0].\n' +
 					'Value "last" is supported. Ignored if -interactive is used',
 			'show-plots': 'show plots created by job (requires ampel-plot-cli. Use "export AMPEL_PLOT_DPI=300" to increase png quality)',
-			'allow-resource-override': 'allow t3 units to overwrite resources previously set by other t3 units',
+			#'allow-resource-override': 'allow t3 units to overwrite resources previously set by other t3 units',
 			'show-plots-cmd': 'show command required to show plots created by job (requires ampel-plot-cli)',
 			'wait-pid': 'wait until process with PID completes before processing current job',
 			'print-schema': 'print (potentially edited) schema before execution',
 			'print-schema-after': 'print (potentially edited) schema after execution',
 			'stdin': 'read job schema from stdin',
 		})
 
@@ -112,30 +113,30 @@
 		parser.opt('keep-db', action='store_true')
 		parser.opt('reset-db', action='store_true')
 		parser.opt('max-parallel-tasks', type=int, default=os.cpu_count())
 		parser.opt('no-conf-check', action='store_true')
 		parser.opt('no-agg', action='store_true')
 		parser.opt('no-breakpoint', action='store_true')
 		parser.opt('no-mp', action='store_true')
-		parser.opt('allow-resource-override', action='store_true')
+		#parser.opt('allow-resource-override', action='store_true')
 		parser.opt('show-plots', action='store_true')
 		parser.opt('show-plots-cmd', action='store_true')
 		parser.opt('secrets', type=str)
 		parser.opt('wait-pid', type=int, default=0)
 		parser.opt('print-schema', action='store_true')
 		parser.opt('print-schema-after', action='store_true')
 		parser.opt('stdin', action='store_true')
 
 		# Example
-		parser.example('job job_file.yaml')
-		parser.example('job job_part1.yaml job_part2.yaml')
-		parser.example('job -keep-db -task last job_file.yaml')
-		parser.example('job -show-plots job.yaml')
-		parser.example('job -fzf  [requires fzf command line utility]')
-		parser.example('pbpaste | ampel job -stdin -no-conf-check -show-plots', prepend="")
+		parser.example(f'{op} job_file.yaml')
+		parser.example(f'{op} job_part1.yaml job_part2.yaml')
+		parser.example(f'{op} -keep-db -task last job_file.yaml')
+		parser.example(f'{op} -show-plots job.yaml')
+		parser.example(f'{op} -fzf  [requires fzf command line utility]')
+		parser.example(f'pbpaste | ampel {op} -stdin -no-conf-check -show-plots', prepend="")
 		return parser
 
 
 	# Mandatory implementation
 	def run(self, args: dict[str, Any], unknown_args: Sequence[str], sub_op: None | str = None) -> None:
 
 		start_time = time()
@@ -331,15 +332,14 @@
 				'\n' + yaml.dump(
 					job.dict(exclude_unset=True),
 					sort_keys=False, default_flow_style=None
 				)
 			)
 			print('#'*50)
 
-		# DevAmpelContext hashes automatically confid from potential IngestDirectives
 		ctx = self.get_context(
 			args, unknown_args, logger,
 			freeze_config = False,
 			ContextClass = DevAmpelContext,
 			purge_db = purge_db,
 			db_prefix = job.mongo.prefix,
 			require_existing_db = False,
@@ -381,79 +381,23 @@
 
 		self._patch_config(config_dict, job, logger)
 		ctx.config._config = recursive_freeze(config_dict)
 
 		# Ensure that job content saved in DB reflects options set dynamically
 		if args['task']:
 			for i in range(len(job.task)):
-				if not i in args['task']:
+				if i not in args['task']:
 					logger.info(f'Skipping task #{i} as requested')
 			job.task = [task for i, task in enumerate(job.task) if i in args['task']]
 
-		jtasks: list[dict[str, Any]] = []
-		for i, model in enumerate(job.task):
-
-			if isinstance(model, TemplateUnitModel):
-
-				if model.template not in ctx.config._config['template']:
-					raise ValueError(f'Unknown process template: {model.template}')
-
-				fqn = ctx.config._config['template'][model.template]
-				if ':' in fqn:
-					fqn, class_name = fqn.split(':')
-				else:
-					class_name = fqn.split('.')[-1]
-				Tpl = getattr(import_module(fqn), class_name)
-				if not issubclass(Tpl, AbsProcessorTemplate):
-					raise ValueError(f'Unexpected template type: {Tpl}')
-
-				tpl = Tpl(**model.config)
-				morphed_um = tpl \
-					.get_model(ctx.config._config, model.dict()) \
-					.dict(exclude_unset=True)
-
-				if args.get('debug'):
-					from ampel.util.pretty import prettyjson
-					logger.info('Task model morphed by template:')
-					for el in prettyjson(morphed_um, indent=4).split('\n'):
-						logger.info(el)
-
-				jtasks.append(morphed_um)
-
-			else:
-				jtasks.append(
-					model.dict(
-						exclude={'inputs', 'outputs', 'expand_with'},
-						exclude_unset=True
-					)
-				)
-
-			logger.info(
-				f'Registering job task#{i} with ' +
-				str(len(list(model.expand_with)) if model.expand_with else 1) +
-				'x multiplier'
-			)
+		# Morphes tasks as well (templates)
+		jtasks = self.load_tasks(ctx, job, logger, args.get('debug', False))
 
 		# recreate JobModel with templates resolved
-		job_dict = ujson.loads(
-			JobModel(
-				**(
-					job.dict(exclude_unset=True) | # type: ignore[arg-type]
-					{
-						'task': [
-							td | task.dict(
-								include={'inputs', 'outputs', 'expand_with', 'title'},
-								exclude_unset=True
-							)
-							for task, td in zip(job.task, jtasks)
-						]
-					}
-				)
-			).json(exclude_unset=True)
-		)
+		job_dict = self.get_job_dict(job, jtasks)
 
 		if args.get('edit') == 'model':
 			fd, fname = tempfile.mkstemp(suffix='.yml')
 			# Seems fd does not work with yaml.dump(), unsure why
 			with open(fname, 'wt') as f:
 				yaml.dump(job_dict, f, sort_keys=False, default_flow_style=None)
 			edit_job(fname)
@@ -473,163 +417,198 @@
 			logger.info(f'Waiting until process with PID {wpid} completes')
 			while (psutil.pid_exists(wpid)):
 				sleep(5)
 			start_time = time()
 
 		logger.info('Saving job schema')
 		job_sig = build_unsafe_dict_id(job_dict, size=-64)
+		job.sig = job_sig
 		ctx.db.get_collection('job').update_one(
 			{'_id': job_sig},
 			{'$setOnInsert': job_dict},
 			upsert=True
 		)
 
+		# Heavy lifting happens here
+		run_ids = self.run_tasks(ctx, job, jtasks, schema_descr, logger)
+
+		feedback = f"Job processed (db: {job.mongo.prefix}"
+		if len(run_ids) == 1:
+			feedback += f", run id: {run_ids[0]})"
+		elif len(run_ids) > 1:
+			feedback += ", run ids: " + " ".join([str(el) for el in run_ids]) + ")"
+		else:
+			feedback = ")"
+
+		logger.info(feedback)
+		logger.info(f'Time required: {get_time_delta(start_time)}\n')
+
+		if args.get('show_plots') or args.get('show_plots_cmd'):
+
+			cmd = [
+				'ampel', 'plot', 'show', '-stack', '300',
+				'-png', os.environ.get('AMPEL_PLOT_DPI', '150'),
+				'-t2', '-t3', '-base-path', 'body.plot', # to be improved later
+				'-db', job.mongo.prefix, '-run-id', *[str(el) for el in run_ids],
+			]
+
+			if args.get('debug'):
+				cmd.append('-debug')
+
+			print(
+				'%s\n%s command: %s' %
+				('-' * 40, 'Executing' if args.get('show_plots') else 'Plot', " ".join(cmd))
+			)
+
+			if args.get('show_plots'):
+				rr = subprocess.run(cmd, check=True, capture_output=True, text=True)
+				print(rr.stdout)
+				print(rr.stderr)
+
+		if args['print_schema_after']:
+			print('\nJob schema:\n')
+			print('#'*50)
+			print(
+				'\n' + yaml.dump(
+					job.dict(exclude_unset=True),
+					sort_keys=False, default_flow_style=None
+				)
+			)
+
+
+	def run_tasks(self,
+		ctx: AmpelContext,
+		job: JobModel,
+		jtasks: list[dict[str, Any]],
+		schema_descr: str,
+		logger: AmpelLogger
+	) -> list[int]:
+
 		run_ids = []
-		resources: dict[str, Resource] = {}
 		for i, taskd in enumerate(jtasks):
 
 			process_name = f'{job.name or schema_descr}#{i}'
 
+			if isinstance(taskd.get('template', None), dict) and 'live' in taskd['template']:
+				taskd = apply_templates(ctx, taskd['template']['live'], taskd, logger)
+				del taskd['template']
+
 			if 'title' in taskd:
 				self.print_chapter(taskd['title'] if taskd.get('title') else f'Task #{i}', logger)
 				#process_name += f' [{taskd['title']}]'
 				del taskd['title']
 			elif i != 0:
 				self.print_chapter(f'Task #{i}', logger)
-
-			taskd['override'] = taskd.pop('override', {}) | {'raise_exc': True}
-
-			# Beacons have no real use in jobs (unlike prod)
-			if taskd['unit'] == 'T2Worker' and 'send_beacon' not in taskd['config']:
-				taskd['config']['send_beacon'] = False
-
-			if (expand_with := job.task[i].expand_with) is not None:
-
-				process_queues: list[Process] = []
-				result_queues: list[Any] = []
-				resource_queues: list[Queue[Resource]] = []
-
-				signal.signal(signal.SIGINT, signal_handler)
-				signal.signal(signal.SIGTERM, signal_handler)
+				
+			if (multiplier := taskd.pop('multiplier', 1)) > 1:
 
 				try:
-					for item in expand_with:
 
-						self._fetch_inputs(job, job.task[i], item, logger)
+					process_queues: list[Process] = []
+					result_queues: list[Any] = []
+
+					signal.signal(signal.SIGINT, signal_handler)
+					signal.signal(signal.SIGTERM, signal_handler)
 
+					for item in range(multiplier):
 						result_queue: Queue = Queue()
-						resource_queue: Queue[Resource] = Queue()
 						p = Process(
 							target = run_mp_process,
-							args = (
-								result_queue,
-								resource_queue,
-								config_dict,
-								job.resolve_expressions(
-									taskd,
-									job.task[i],
-									item
-								),
-								process_name,
-							),
-							daemon = True,
+							args = (result_queue, ctx.config._config, taskd, process_name),
+							daemon = True
 						)
 						p.start()
 						process_queues.append(p)
 						result_queues.append(result_queue)
-						resource_queues.append(resource_queue)
 					
-					for i, (p, r1, r2) in enumerate(zip(process_queues, result_queues, resource_queues)):
+					for i, (p, r1) in enumerate(zip(process_queues, result_queues)):
 						p.join()
 						if (m := r1.get()):
 							logger.info(f'{taskd["unit"]}#{i} return value: {m}')
-						for r in iter(r2.get, None):
-							if r.name in resources and not args['allow_resource_override']:
-								continue
-							resources[k] = r
 
 				except KeyboardInterrupt:
 					sys.exit(1)
 			
 			else:
 				
-				self._fetch_inputs(job, job.task[i], None, logger)
-
 				proc = ctx.loader.new_context_unit(
-					model = UnitModel(**job.resolve_expressions(taskd, job.task[i])),
+					model = UnitModel(**taskd),
 					context = ctx,
 					process_name = process_name,
-					job_sig = job_sig,
+					job_sig = job.sig,
 					sub_type = AbsEventUnit,
 					base_log_flag = LogFlag.MANUAL_RUN
 				)
 
 				event_hdlr = EventHandler(
 					proc.process_name,
 					ctx.get_database(),
 					raise_exc = proc.raise_exc,
-					job_sig = job_sig,
-					extra = {'task': i},
-					resources = resources
+					job_sig = job.sig,
+					extra = {'task': i}
 				)
 
 				x = proc.run(event_hdlr)
 				if event_hdlr.run_id:
 					run_ids.append(event_hdlr.run_id)
 
-				if event_hdlr.resources:
-					for name, resource in event_hdlr.resources.items():
-						if name in resources and not args['allow_resource_override']:
-							continue
-						resources[name] = resource
-
 				logger.info(f'{taskd["unit"]} return value: {x}')
 
-		feedback = f"Job processed (db: {job.mongo.prefix}"
-		if len(run_ids) == 1:
-			feedback += f", run id: {run_ids[0]})"
-		elif len(run_ids) > 1:
-			feedback += ", run ids: " + " ".join([str(el) for el in run_ids]) + ")"
-		else:
-			feedback = ")"
+		return run_ids
 
-		logger.info(feedback)
-		logger.info(f'Time required: {get_time_delta(start_time)}\n')
 
-		if args.get('show_plots') or args.get('show_plots_cmd'):
+	def load_tasks(self,
+		ctx: AmpelContext, job: JobModel, logger: AmpelLogger, debug: bool = False
+	) -> list[dict[str, Any]]:
 
-			cmd = [
-				'ampel', 'plot', 'show', '-stack', '300',
-				'-png', os.environ.get('AMPEL_PLOT_DPI', '150'),
-				'-t2', '-t3', '-base-path', 'body.plot', # to be improved later
-				'-db', job.mongo.prefix, '-run-id', *[str(el) for el in run_ids],
-			]
+		jtasks: list[dict[str, Any]] = []
+		for i, model in enumerate(job.task):
+			if isinstance(model.template, Sequence):
+				taskd = apply_templates(ctx, model.template, model.dict(), logger)
+				del taskd['template']
+				if debug:
+					self.print_task(taskd, logger)
+			elif (
+				isinstance(model.template, dict) and
+				'pre' in model.template and model.template['pre']
+			):
+				taskd = apply_templates(ctx, model.template['pre'], model.dict(), logger)
+				del taskd['template']['pre']
+				if debug:
+					self.print_task(taskd, logger)
+			else:
+				taskd = self.get_task_dict(model)
 
-			if args.get('debug'):
-				cmd.append('-debug')
+			taskd['override'] = taskd.pop('override', {}) | {'raise_exc': True}
+			# Beacons have no real use in jobs (unlike prod)
+			if taskd['unit'] == 'T2Worker' and 'send_beacon' not in taskd['config']:
+				taskd['config']['send_beacon'] = False
 
-			print(
-				'%s\n%s command: %s' %
-				('-' * 40, 'Executing' if args.get('show_plots') else 'Plot', " ".join(cmd))
+			jtasks.append(taskd)
+			logger.info(
+				f'Registering job task#{i} with {model.get_multiplier()}x multiplier'
 			)
 
-			if args.get('show_plots'):
-				rr = subprocess.run(cmd, check=True, capture_output=True, text=True)
-				print(rr.stdout)
-				print(rr.stderr)
+		return jtasks
 
-		if args['print_schema_after']:
-			print('\nJob schema:\n')
-			print('#'*50)
-			print(
-				'\n' + yaml.dump(
-					job.dict(exclude_unset=True),
-					sort_keys=False, default_flow_style=None
-				)
-			)
+
+	def print_task(self, taskd: dict[str, Any], logger: AmpelLogger) -> None:
+		logger.info('Task model morphed by template:')
+		for el in prettyjson(taskd, indent=4).split('\n'):
+			logger.info(el)
+
+
+	def get_task_dict(self, task_model: JobTaskModel) -> dict[str, Any]:
+		return task_model.dict(exclude_unset=True)
+
+
+	def get_job_dict(self, job: JobModel, jtasks: list[dict[str, Any]]) -> dict[str, Any]:
+		out = job.dict(exclude_unset=True)
+		out['task'] = jtasks
+		return out
 
 
 	@staticmethod
 	def print_chapter(msg: str, logger: AmpelLogger) -> None:
 		logger.info(' ')
 		logger.info('=' * (space := (len(msg) + 4)))
 		logger.info('‖ ' + msg + ' ‖') # type: ignore
@@ -637,15 +616,16 @@
 		logger.info(' ')
 
 
 	@classmethod
 	def get_job_schema(cls,
 		schema_paths: None | Sequence[str] = None,
 		schema_content: None | str = None,
-		compute_sig: bool = True
+		compute_sig: bool = True,
+		Model: Type = JobModel
 	) -> tuple[None, None] | tuple[JobModel, int]:
 
 		if not (schema_paths or schema_content):
 			raise ValueError("Please provide either job file path(s) or content")
 
 		if schema_paths:
 			content = io.StringIO()
@@ -667,57 +647,15 @@
 
 		for k in list(job.keys()):
 			# job root keys starting with % are used by own convention for yaml anchors
 			# and thus need not be included in the loaded job structure
 			if k.startswith('%'):
 				del job[k]
 
-		return JobModel(**job), build_unsafe_dict_id(job, size=-64) if compute_sig else 0
-
-
-	@staticmethod
-	def _fetch_inputs(
-		job: JobModel,
-		task: TaskUnitModel | TemplateUnitModel,
-		item: None | str | dict | list,
-		logger: AmpelLogger,
-	):
-		"""
-		Ensure that input artifacts exist
-		"""
-		for artifact in task.inputs.artifacts:
-
-			resolved_artifact = InputArtifact(
-				**job.resolve_expressions(
-					ujson.loads(artifact.json()), task, item
-				)
-			)
-
-			if resolved_artifact.path.exists():
-				logger.info(f'Artifact {resolved_artifact.name} exists at {resolved_artifact.path}')
-			else:
-				logger.info(
-					f'Fetching artifact {resolved_artifact.name} from '
-					f'{resolved_artifact.http.url} to {resolved_artifact.path}'
-				)
-				os.makedirs(resolved_artifact.path.parent, exist_ok=True)
-				with tempfile.NamedTemporaryFile(delete=False) as tf:
-					r = requests.get(resolved_artifact.http.url, stream=True)
-					r.raise_for_status()
-					for chunk in r.iter_content(chunk_size=1<<13):
-						tf.write(chunk)
-					tf.flush()
-					try:
-						with tarfile.open(tf.name) as archive:
-							logger.info(f'{resolved_artifact.name} is a tarball; extracting')
-							os.makedirs(resolved_artifact.path)
-							archive.extractall(resolved_artifact.path)
-						os.unlink(tf.name)
-					except tarfile.ReadError:
-						os.rename(tf.name, resolved_artifact.path)
+		return Model(**job), build_unsafe_dict_id(job, size=-64) if compute_sig else 0
 
 
 	@staticmethod
 	def _patch_config(config_dict: dict[str, Any], job: JobModel, logger: AmpelLogger):
 
 		# Add channel(s)
 		for chan in job.channel:
@@ -733,15 +671,14 @@
 				if k not in config_dict['alias']:
 					dict.__setitem__(config_dict['alias'], k, {})
 				dict.__setitem__(config_dict['alias'][k], kk, vv)
 
 
 def run_mp_process(
 	result_queue: Queue,
-	resource_queue: Queue,
 	config: dict[str, Any],
 	tast_unit_model: dict[str, Any],
 	process_name: str,
 	job_sig: None | int = None,
 	task_nbr: None | int = None,
 	log_profile: str = 'default'
 ) -> None:
@@ -768,28 +705,21 @@
 			extra = {'task': task_nbr}
 		)
 
 		result_queue.put(
 			processor.run(eh)
 		)
 
-		if eh.resources:
-			for v in eh.resources.values():
-				resource_queue.put(v)
-		else:
-			resource_queue.put(None)
-
 	except Exception as e:
 		import traceback
 		se = str(e)
 		result_queue.put(
 			'\n' + '#'*len(se) + '\n' + str(e) + '\n' + '#'*len(se) + '\n' +
 			''.join(traceback.format_exception(type(e), e, e.__traceback__))
 		)
-		resource_queue.put(None)
 
 
 def signal_handler(sig, frame):
 	#import traceback
 	print('Interrupt detected')
 	#print('Stack frames:')
 	#traceback.print_stack(frame)
```

### Comparing `ampel_core-0.8.6/ampel/cli/LogCommand.py` & `ampel_core-0.9.0/ampel/cli/LogCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/ProcessCommand.py` & `ampel_core-0.9.0/ampel/cli/ProcessCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/RunCommand.py` & `ampel_core-0.9.0/ampel/cli/RunCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/StartCommand.py` & `ampel_core-0.9.0/ampel/cli/StartCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/T2Command.py` & `ampel_core-0.9.0/ampel/cli/T2Command.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/T3BufferExporterStager.py` & `ampel_core-0.9.0/ampel/cli/T3BufferExporterStager.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/T3BufferExporterUnit.py` & `ampel_core-0.9.0/ampel/cli/T3BufferExporterUnit.py`

 * *Files 10% similar despite different names*

```diff
@@ -6,24 +6,24 @@
 # Date:                17.08.2022
 # Last Modified Date:  17.08.2022
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from collections.abc import Generator
 from ampel.types import UBson, T3Send
 from ampel.cli.T3BufferExporterStager import TextExportOptions
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.abstract.AbsIdMapper import AbsIdMapper
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.struct.UnitResult import UnitResult
 from ampel.view.SnapView import SnapView
 from ampel.struct.T3Store import T3Store
 from ampel.cli.export import txt_export, bin_export, get_fd
 
 
-class T3BufferExporterUnit(AbsT3ReviewUnit[SnapView]):
+class T3BufferExporterUnit(AbsT3Unit[SnapView]):
 
 	# None means stdout
 	fd: None | str = None
 	binary: bool = False
 	verbose: bool = True
 	id_mapper: None | AbsIdMapper = None
 	txt_options: TextExportOptions = TextExportOptions()
```

### Comparing `ampel_core-0.8.6/ampel/cli/ViewCommand.py` & `ampel_core-0.9.0/ampel/cli/ViewCommand.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/export.py` & `ampel_core-0.9.0/ampel/cli/export.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/cli/utils.py` & `ampel_core-0.9.0/ampel/cli/utils.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/ScheduleEvaluator.py` & `ampel_core-0.9.0/ampel/config/ScheduleEvaluator.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/builder/AbsConfigTemplate.py` & `ampel_core-0.9.0/ampel/model/builder/RemoteUnitDefinition.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File:                Ampel-core/ampel/config/builder/AbsConfigTemplate.py
+# File:                Ampel-core/ampel/model/builder/RemoteUnitDefinition.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
-# Date:                14.04.2020
-# Last Modified Date:  18.12.2021
+# Date:                06.11.2019
+# Last Modified Date:  15.06.2020
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from ampel.base.AmpelABC import AmpelABC
+from typing import List
 from ampel.base.AmpelBaseModel import AmpelBaseModel
 
+class RemoteUnitDefinition(AmpelBaseModel):
 
-class AbsConfigTemplate(AmpelABC, AmpelBaseModel, abstract=True):
-	""" Known direct subclasses: AbsProcessTemplate, AbsChannelTemplate """
-
-	template: None | str
+	class_name: str
+	base: list['str']
```

### Comparing `ampel_core-0.8.6/ampel/config/builder/BaseConfigChecker.py` & `ampel_core-0.9.0/ampel/config/builder/BaseConfigChecker.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/builder/ConfigBuilder.py` & `ampel_core-0.9.0/ampel/config/builder/ConfigBuilder.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/config/builder/ConfigBuilder.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                03.09.2019
-# Last Modified Date:  12.01.2023
+# Last Modified Date:  01.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import os, sys, re, json, yaml, datetime, getpass, importlib, subprocess, pkg_resources
-from multiprocessing import Pool
 from typing import Any
+from multiprocessing import Pool
 from collections.abc import Iterable
 
 from ampel.log.utils import log_exception
 from ampel.abstract.AbsChannelTemplate import AbsChannelTemplate
 from ampel.log.AmpelLogger import AmpelLogger, VERBOSE, DEBUG, ERROR
 from ampel.config.builder.DisplayOptions import DisplayOptions
 from ampel.config.builder.FirstPassConfig import FirstPassConfig
@@ -81,31 +81,31 @@
 						else:
 							self.logger.error(f"Unknown config element: {k}.{kk}")
 
 			else:
 				self.first_pass_config[k].add(d[k], dist_name, version, register_file)
 
 		if 'template' in d:
-			self.register_channel_templates(d['template'], dist_name, version, register_file)
+			self.register_templates(d['template'], dist_name, version, register_file)
 
 
-	def register_channel_templates(self,
-		chan_templates: dict[str, str],
+	def register_templates(self,
+		arg: dict[str, str],
 		dist_name: str,
 		version: str | float | int,
-		register_file: str
+		register_file: str,
 	) -> None:
 
-		if not isinstance(chan_templates, dict):
+		if not isinstance(arg, dict):
 			raise ValueError('Provided argument must be a dict instance')
 
-		for k, v in chan_templates.items():
+		for k, v in arg.items():
 
 			if k in self.templates:
-				raise ValueError('Duplicated channel template: ' + k)
+				raise ValueError('Duplicated template: ' + k)
 
 			if self.verbose:
 				self.logger.log(VERBOSE,
 					f'Registering template "{k}" ' +
 					register_file if register_file else '' +
 					ConfigCollector.distrib_hint(distrib=dist_name)
 				)
@@ -203,14 +203,18 @@
 				):
 					if self.verbose:
 						self.logger.log(VERBOSE, f'{res[0]} dependencies: {res[1] or None}')
 					if res[1]:
 						out['unit'][res[0]]['dependencies'] = list(res[1].keys())
 						all_deps.update(res[1])
 
+
+		# Register templates in config
+		out['template'] = {k: v.__module__ for k, v in self.templates.items()}
+
 		# Add t2 init config collector (in which both hashed values of t2 run configs
 		# and t2 init config will be added)
 		out['confid'] = T02ConfigCollector(
 			conf_section='confid', options=self.options, logger=self.logger
 		)
 
 		if not ignore_processes:
@@ -244,15 +248,15 @@
 					if self.verbose:
 						self.logger.log(VERBOSE, f'Morphing standalone {tier_name} processes: {p["name"]}')
 						pass
 
 					dist_name = fp_procs_collector._origin[p["name"]][0]
 					try:
 						p_collector.add(
-							self.new_morpher(p) \
+							ProcessMorpher(p, self.logger, self.templates, self.verbose) \
 								.scope_aliases(self.first_pass_config, dist_name) \
 								.apply_template(self.first_pass_config) \
 								.hash_t2_config(out) \
 								.get(),
 							*fp_procs_collector._origin[p["name"]]
 						)
 					except Exception as e:
@@ -328,15 +332,15 @@
 								f'Morphing channel embedded t{p["tier"]} process: {p["name"]}'
 							)
 
 						try:
 							# Add transformed process to final process collector
 							dist_name = fp_chan_collector._origin[chan_name][0]
 							out['process'][f't{p["tier"]}'].add(
-								self.new_morpher(p) \
+								ProcessMorpher(p, self.logger, self.templates, self.verbose) \
 									.scope_aliases(self.first_pass_config, dist_name) \
 									.apply_template(self.first_pass_config) \
 									.hash_t2_config(out) \
 									.enforce_t3_channel_selection(chan_name) \
 									.get(),
 								*fp_chan_collector._origin[chan_name]
 							)
@@ -381,17 +385,14 @@
 				k = tup[1]
 				secret = tup[2]
 				if not sp.tell(secret, str):
 					self.logger.info(" -> Secret not resolvable with specified password(s)")
 				else:
 					d[k] = secret.get()
 
-	
-		# Register templates in config (might be used by the 'ampel job' CLI)
-		out['template'] = {k: v.__module__ for k, v in self.templates.items()}
 		self.logger.info('Done building config')
 
 		# Error Summary
 		if out['unit'].err_fqns:
 			self.logger.break_aggregation()
 			self.logger.info('Erroneous units (import failed):')
 			for el in out['unit'].err_fqns:
@@ -490,24 +491,14 @@
 			self.logger.break_aggregation()
 			with open(path, "r") as file:
 				self.logger.info(f'Config file saved as {path} [{len(file.readlines())} lines]')
 
 		return d
 
 
-	def new_morpher(self, process: dict[str, Any]) -> ProcessMorpher:
-		"""
-		Returns an instance of ProcessMorpher using the provided
-		process dict and the internal logger and templates
-		"""
-		return ProcessMorpher(
-			process, self.templates, self.logger, self.verbose
-		)
-
-
 	def _get_channel_tpl(self,
 		chan_dict: dict[str, Any],
 		register_file: str
 	) -> None | AbsChannelTemplate:
 		"""
 		Internal method used to check if a template (and which one)
 		should be applied to a given channel dict.
```

### Comparing `ampel_core-0.8.6/ampel/config/builder/ConfigChecker.py` & `ampel_core-0.9.0/ampel/config/builder/ConfigChecker.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/builder/ConfigValidator.py` & `ampel_core-0.9.0/ampel/config/builder/ConfigValidator.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/builder/DisplayOptions.py` & `ampel_core-0.9.0/ampel/config/builder/DisplayOptions.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/builder/DistConfigBuilder.py` & `ampel_core-0.9.0/ampel/config/builder/DistConfigBuilder.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,18 +4,19 @@
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                09.10.2019
 # Last Modified Date:  18.12.2022
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import json, yaml, pkg_resources, os, re
-from functools import partial
-from pkg_resources import EggInfoDistribution, DistInfoDistribution # type: ignore[attr-defined]
 from typing import Any
+from functools import partial
 from collections.abc import Callable
+from pkg_resources import EggInfoDistribution, DistInfoDistribution # type: ignore[attr-defined]
+
 from ampel.config.builder.ConfigBuilder import ConfigBuilder
 from ampel.util.distrib import get_dist_names, get_files
 from ampel.log import VERBOSE, SHOUT
 
 
 class DistConfigBuilder(ConfigBuilder):
 	"""
@@ -100,31 +101,31 @@
 						self.load_conf_using_func(distrib, f, self.first_pass_config[key].add)
 
 			# ("channel", "mongo", "resource")
 			for key in self.first_pass_config.conf_keys.keys():
 				if key == "alias":
 					continue
 				if section_conf_file := self.get_conf_file(all_conf_files, f"{key}.{ext}"):
-					self.load_conf_using_func(distrib, section_conf_file, self.first_pass_config[key].add) # type: ignore
+					self.load_conf_using_func(distrib, section_conf_file, self.first_pass_config[key].add)
 
 			# ("controller", "processor", "unit", "alias", "process")
 			for unit_type in ("alias", "process"):
 				if tier_conf_file := self.get_conf_file(all_conf_files, f"{unit_type}.{ext}"):
 					self.load_conf_using_func(
 						distrib, tier_conf_file, partial(self.register_tier_conf, unit_type)
 					)
 
 			# Try to load templates from folder template (defined by 'Ampel-ZTF' for ex.)
 			if template_conf_files := self.get_conf_files(all_conf_files, "/template/"):
 				for f in template_conf_files:
-					self.load_conf_using_func(distrib, f, self.register_channel_templates)
+					self.load_conf_using_func(distrib, f, self.register_templates)
 
 			# Try to load templates from template.conf
 			if template_conf := self.get_conf_file(all_conf_files, "/template.{ext}"):
-				self.load_conf_using_func(distrib, template_conf, self.register_channel_templates) # type: ignore
+				self.load_conf_using_func(distrib, template_conf, self.register_templates)
 
 			if all_conf_files:
 				self.logger.info(f"Not all conf files were loaded from distribution '{distrib.project_name}'")
 				self.logger.info(f"Unprocessed conf files: {all_conf_files}")
 
 		except Exception as e:
 			if raise_exc:
@@ -154,14 +155,15 @@
 
 
 	def load_conf_using_func(self,
 		distrib: EggInfoDistribution | DistInfoDistribution,
 		file_rel_path: str,
 		func: Callable[[dict[str, Any], str, str, str], None],
 		raise_exc: bool = True,
+		**kwargs
 	) -> None:
 
 		try:
 
 			if self.verbose:
 				self.logger.log(VERBOSE,
 					f"Loading {file_rel_path} from distribution '{distrib.project_name}'"
@@ -178,15 +180,16 @@
 			else:
 				payload = distrib.get_resource_string(__name__, file_rel_path)
 
 			func(
 				load(payload),
 				distrib.project_name,
 				distrib.version,
-				file_rel_path
+				file_rel_path,
+				**kwargs
 			)
 
 		except FileNotFoundError:
 			if raise_exc:
 				raise
 			self.error = True
 			self.logger.error(
```

### Comparing `ampel_core-0.8.6/ampel/config/builder/FirstPassConfig.py` & `ampel_core-0.9.0/ampel/config/builder/FirstPassConfig.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/builder/ProcessMorpher.py` & `ampel_core-0.9.0/ampel/config/builder/ProcessMorpher.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,47 +1,50 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/config/builder/ProcessMorpher.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                16.10.2019
-# Last Modified Date:  02.01.2023
+# Last Modified Date:  04.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import json
 from typing import Any
+from typing_extensions import Self
 from importlib import import_module
 from ampel.log.AmpelLogger import AmpelLogger, VERBOSE
 from ampel.model.ProcessModel import ProcessModel
 from ampel.util.recursion import walk_and_process_dict
 
 
 class ProcessMorpher:
 	""" Applies various transformations to process dicts """
 
 	def __init__(self,
 		process: dict[str, Any],
-		templates: dict[str, Any],
 		logger: AmpelLogger,
+		templates: None | dict[str, Any] = None,
 		verbose: bool = False,
-		deep_copy: bool = False
+		deep_copy: bool = False,
+		proc_name: None | str = None # enable process name override
 	) -> None:
 
 		self.process = json.loads(json.dumps(process)) if deep_copy else process
 		self.templates = templates
 		self.logger = logger
 		self.verbose = verbose
+		self.proc_name = proc_name or self.process['name']
 
 
 	def get(self) -> dict[str, Any]:
 		""" :raises: Error if the morphed process does not comply with ProcessModel """
 		return ProcessModel(**(self.process | {'version': 0})).dict()
 
 
-	def enforce_t3_channel_selection(self, chan_name: str) -> 'ProcessMorpher':
+	def enforce_t3_channel_selection(self, chan_name: str) -> Self:
 
 		if self.process['tier'] == 3:
 
 			for block in self.process['processor']['config']['execute']:
 				if block["unit"] != "T3ReviewUnitExecutor":
 					raise ValueError(
 						f'Cannot enforce channel selection: '
@@ -73,35 +76,36 @@
 				# An exception will be raised if someone embeds an admin t3 proc (without selection)
 				# within a channel (unsupported feature)
 				select['config']['channel'] = chan_name
 
 		return self
 
 
-	def apply_template(self, first_pass_config: dict) -> 'ProcessMorpher':
+	def apply_template(self, first_pass_config: dict) -> Self:
 		""" Applies template possibly associated with process """
 
+		if self.templates is None:
+			raise ValueError("No template registered")
+
 		# The process embedded in channel def requires templating itself
 		if 'template' in self.process:
 
 			if self.verbose:
 				self.logger.log(VERBOSE,
 					f'Applying {self.process["template"]} template '
-					f'to process {self.process["name"]} '
+					f'to process {self.proc_name} '
 				)
 
-			self.process = self.templates[
-				self.process['template']
-			](**self.process).get_process(first_pass_config, self.logger)
+			self.process = self.templates[self.process['template']](**self.process) \
+				.morph(first_pass_config, self.logger)
 
 		return self
 
 
-	def scope_aliases(self, first_pass_config: dict, dist_name: str) -> 'ProcessMorpher':
-		""" Note: should be called before hash_t2_config """
+	def scope_aliases(self, first_pass_config: dict, dist_name: str) -> Self:
 
 		if self.verbose:
 			self.logger.debug("Scoping aliases")
 
 		recurse = False
 
 		while walk_and_process_dict(
@@ -153,26 +157,27 @@
 				self.logger.log(VERBOSE, f'Config alias "{v}" renamed into "{scoped_alias}"')
 
 			return True
 
 		return False
 
 
-	def resolve_aliases(self, t2d: dict[str, Any], aliases: dict[str, Any], root_path: str):
+	def resolve_aliases(self, arg: dict[str, Any], aliases: dict[str, Any], root_path: str) -> None:
 		"""
-		Resolves aliases recursively (necessary before hashing t2 config)
+		Resolves aliases recursively
+		(no longer necessary before hash_t2_config(..) as it does it itself)
 		"""
 
 		if self.verbose:
 			self.logger.debug("Resolving aliases (required for hash)")
 
 		recurse = False
 
 		while walk_and_process_dict(
-			arg = t2d,
+			arg = arg,
 			callback = self._resolve_alias_callback,
 			match = ['config'],
 			aliases = aliases,
 			root_path = root_path
 		):
 			if self.verbose:
 				self.logger.debug("Alias(es) resolved %s" % ("again" if recurse else ""))
@@ -190,49 +195,49 @@
 		aliases = kwargs.get('aliases')
 
 		if not aliases:
 			raise ValueError('Parameter "aliases" missing in kwargs')
 
 		if d[k] not in aliases:
 			raise ValueError(
-				f'Unknown T2 config alias ({d[k]}) defined in process {self.process["name"]}'
+				f'Unknown T2 config alias ({d[k]}) defined in process {self.proc_name}'
 			)
 
 		if self.verbose:
 			self.logger.debug(f"Resolving alias '{d[k]}' in {kwargs.get('root_path')}")
 
 		d[k] = aliases[d[k]]
 
 
-	def hash_t2_config(self, out_config: dict) -> 'ProcessMorpher':
+	def hash_t2_config(self, out_config: dict, target: None | dict[str, Any] = None) -> Self:
 		"""
 		This method modifies the underlying self._process dict structure.
 		The 'config' (dict) value of UnitModel instances is replaced by a hash value (int).
 		Notes:
 		- Applies only to t0 and t1 processes
 		- The config path filter "t2_compute.units" is used
 		- Aliases are resolved (works recursively so that t2_dependency of tied units can use aliases as well)
 		
 		:param out_config: used to store new map entries in the ampel config: {<confid>: {<hash>: <conf dict>}}.
 		"""
 
-		if self.process['tier'] not in (0, 1):
+		if target is None and self.process['tier'] not in (0, 1):
 			return self
 
 		if self.verbose:
 			self.logger.debug("Looking for t2 config to hash")
 
 		# Example of conf_dicts keys
 		# processor.config.directives.0.combine.0.state_t2.0
  		# processor.config.directives.0.combine.0.state_t2.0.config.t2_dependency.0
  		# processor.config.directives.0.point_t2.0
 		conf_dicts: dict[str, dict[str, Any]] = {}
 
 		walk_and_process_dict(
-			arg = self.process["processor"]["config"]["directives"],
+			arg = target or self.process["processor"]["config"]["directives"],
 			callback = self._gather_t2_config_callback,
 			match = ['point_t2', 'stock_t2', 'state_t2'],
 			conf_dicts = conf_dicts
 		)
 
 		# This does the trick of processing nested config first
 		sorted_conf_dicts = {
@@ -242,23 +247,23 @@
 
 		for k, d in sorted_conf_dicts.items():
 
 			t2_unit = d["unit"]
 			conf = d.get("config", {})
 
 			if self.verbose:
-				extra = {'process': self.process['name'], 'conf': k + ".config"}
-				self.logger.debug("Hashing T2 config", extra=extra)
+				extra = {'process': self.proc_name}
+				self.logger.debug(f"Hashing T2 config {k}.config", extra=extra)
 
 			# Replace alias with content
 			if isinstance(conf, str):
 			
 				if conf not in out_config['alias']['t2']:
 					raise ValueError(
-						f'Unknown T2 config alias ({conf}) defined in process {self.process["name"]}'
+						f'Unknown T2 config alias ({conf}) defined in process {self.proc_name}'
 					)
 
 				if self.verbose:
 					self.logger.debug(f"Resolving alias '{conf}'", extra=extra)
 
 				conf = out_config['alias']['t2'][conf]
 
@@ -274,43 +279,39 @@
 					self.logger.warn(
 						f"T2 unit {t2_unit} not installed locally. "
 						f"Building *unsafe* conf dict hash: "
 						f"changes in unit defaults between releases will go undetected",
 						extra=extra
 					)
 
-				if self.verbose:
+				if self.verbose > 1:
 					self.logger.debug("Computing hash", extra=extra)
 
 				if conf is None:
 					d["config"] = None
 				else:
 					d["config"] = out_config['confid'].add(conf, None, None, None)
 
 			# For internal use only
 			elif isinstance(conf, int):
 				if conf not in out_config['confid']:
-					raise ValueError(
-						f'Unknown T2 config (int) alias defined by {k}:\n {t2_unit}'
-					)
+					raise ValueError(f'Unknown T2 config (int) alias defined by {k}:\n {t2_unit}')
 			else:
-				raise ValueError(
-					f'Unknown T2 config defined by {k}:\n {t2_unit}'
-				)
+				raise ValueError(f'Unknown T2 config defined by {k}:\n {t2_unit}')
 
 		return self
 
 
 	def _gather_t2_config_callback(self, path, k, d, **kwargs) -> None:
 		"""
 		Used by walk_and_process_dict(...) from hash_t2_config(...)
 		"""
 
-		if self.verbose:
+		if self.verbose > 1:
 			self.logger.info(f"# path: {path}.{k}")
 
 		if d[k]:
 			for i, el in enumerate(d[k]):
-				if self.verbose:
+				if self.verbose > 1:
 					self.logger.info(f"# path: {path}.{k}.{i}")
 					self.logger.info(el)
 				kwargs['conf_dicts'][f"{path}.{k}.{i}"] = el
```

### Comparing `ampel_core-0.8.6/ampel/config/builder/get_env.py` & `ampel_core-0.9.0/ampel/config/builder/get_env.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/AbsDictConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/AbsDictConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/AbsForwardConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/AbsForwardConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/AbsListConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/AbsListConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/AliasConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/AliasConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/ChannelConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/ChannelConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/ConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/ConfigCollector.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 from ampel.config.builder.DisplayOptions import DisplayOptions
 
 
 class ConfigCollector(dict):
 
 	def __init__(self,
 		conf_section: str,
-		options: DisplayOptions,
+		options: DisplayOptions = DisplayOptions(),
 		content: None | dict = None,
 		logger: None | AmpelLogger = None,
 		tier: None | Literal[0, 1, 2, 3, "ops"] = None
 	) -> None:
 
 		super().__init__(**content if content else {})
 		self.options = options
```

### Comparing `ampel_core-0.8.6/ampel/config/collector/DBConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/DBConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/ForwardProcessConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/ForwardProcessConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/LoggingCollector.py` & `ampel_core-0.9.0/ampel/config/collector/LoggingCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/ProcessConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/ProcessConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/ResourceConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/ResourceConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/T02ConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/T02ConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/config/collector/UnitConfigCollector.py` & `ampel_core-0.9.0/ampel/config/collector/UnitConfigCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/core/AmpelContext.py` & `ampel_core-0.9.0/ampel/core/AmpelContext.py`

 * *Files 8% similar despite different names*

```diff
@@ -43,14 +43,15 @@
 		"""
 
 		self.config = config
 		self.db = db
 		self.loader = loader
 		self.admin_msg = admin_msg
 		self.resource = resource
+		self.run_time_aliases: dict[str, Any] = {}
 		
 		# try to register aux units globally
 		try:
 			AuxUnitRegister.initialize(config)
 		except Exception:
 			print("UnitLoader auxiliary units auto-registration failed")
 
@@ -178,20 +179,32 @@
 			l = list(self.db.col_conf_ids.find({"_id": conf_id}))
 			if len(l) == 0:
 				return None
 			del l[0]['_id']
 			return l[0]
 
 
+	def add_conf_id(self, conf_id: int, unit_config: dict[str, Any]) -> None:
+		self.db.add_conf_id(conf_id, unit_config)
+		dict.__setitem__(self.config._config["confid"], conf_id, unit_config)
+
+
+	def add_run_time_alias(self, key: str, value: Any, overwrite: bool = False) -> None:
+		if not isinstance(key, str) or key[0] != '%' != key[1]:
+			raise ValueError('Run time aliases must begin with %%')
+		if key in self.run_time_aliases and not overwrite:
+			raise ValueError(f"Run time alias {key} already defined, set overwrite=True to ignore")
+		self.run_time_aliases[key] = value
+
+
 	def __repr__(self) -> str:
 		return "<AmpelContext>"
 
 
 	def deactivate_processes(self) -> None:
-		""" """
 		for i in range(4):
 			for p in self.config.get(f'process.t{i}', dict, raise_exc=True).values():
 				p['active'] = False
 
 
 	def activate_process(self,
 		name: str,
```

### Comparing `ampel_core-0.8.6/ampel/core/AmpelController.py` & `ampel_core-0.9.0/ampel/core/AmpelController.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/core/AmpelDB.py` & `ampel_core-0.9.0/ampel/core/AmpelDB.py`

 * *Files 1% similar despite different names*

```diff
@@ -71,15 +71,15 @@
 		:param require_exists:
 		- False: AmpelDB instantiation will succeed even if underlying database(s) do not exist
 		- True: AmpelDB instantiation will fail unless underlying databases exist
 		- str: same as True but provided value overrides prefix value otherwise loaded from AmpelConfig
 		:param one_db: whether to create or load a single database rather than having
 		collections split in in three databases (data, var, ext).
 		If 'auto' is set (for which require_exists must be True), then AmpelDB will try
-		to load a databse in single mode and try again in multi-mode if it fails.
+		to load a database in single-collection mode and try again in multi-collections mode if it fails.
 		Note that ampel 'jobs' usually operate with one_db=True.
 		:raises: ValueError in case a required config entry is missing
 		"""
 		if one_db == 'auto':
 			if require_exists is False:
 				raise ValueError("Option 'one_db' cannot be set to 'auto' if require_exists is False")
 			try:
```

### Comparing `ampel_core-0.8.6/ampel/core/AmpelRegister.py` & `ampel_core-0.9.0/ampel/core/AmpelRegister.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/core/ContextUnit.py` & `ampel_core-0.9.0/ampel/core/ContextUnit.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/core/DataLoader.py` & `ampel_core-0.9.0/ampel/core/DataLoader.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/core/DataLoader.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                13.01.2018
-# Last Modified Date:  22.04.2022
+# Last Modified Date:  04.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from bson.codec_options import CodecOptions
 from typing import Literal
 from collections.abc import Iterable, Iterator
 
 from ampel.types import StockId, ChannelId, StrictIterable, Tag
@@ -149,22 +149,16 @@
 			elif directive.col == "t2":
 
 				# the entire data will need to fit in memory anyway
 				res = list(cursor)
 
 				# whether to replace init config integer hash with 'resolved' config dict
 				if directive.resolve_config:
-
-					config_keys = self.ctx.config.get('t2.config_keys', dict)
-					if not config_keys:
-						raise ValueError("Cannot load t2 configs")
-
 					for el in res:
-						#: init config integer hash with 'resolved' config dict
-						dict.__setitem__(el, 'config', el[config_keys[el['config']]]) # type: ignore[index]
+						dict.__setitem__(el, 'config', self.ctx.config.get_conf_id(el['config']))
 
 				inc(len(res))
 
 				if directive.excluding_query:
 
 					sids = set(register.keys())
 					for el in res:
```

### Comparing `ampel_core-0.8.6/ampel/core/DefaultProcessController.py` & `ampel_core-0.9.0/ampel/core/DefaultProcessController.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/core/EventHandler.py` & `ampel_core-0.9.0/ampel/core/EventHandler.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/core/EventHandler.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                26.09.2018
-# Last Modified Date:  19.12.2022
+# Last Modified Date:  02.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from time import time
 from bson import ObjectId
 from typing import Any, Literal, TYPE_CHECKING
 from ampel.enum.EventCode import EventCode
 from ampel.struct.Resource import Resource
@@ -19,15 +19,16 @@
 if TYPE_CHECKING:
 	from ampel.core.AmpelDB import AmpelDB
 
 
 # TODO: (much later) remove explicit dependency on pymongo
 class EventHandler:
 	"""
-	Handles the creation and publication of event documents into the event database
+	Handles creation and publication of event documents into the event database.
+	Dynamic resources can also be registered with this class.
 	"""
 
 	def __init__(self,
 		process_name: str,
 		ampel_db: 'AmpelDB',
 		col_name: str = "event",
 		raise_exc = False,
@@ -50,18 +51,19 @@
 		self.col = ampel_db.get_collection(col_name)
 		self.extra: dict[str, Any] = extra or {}
 		self.resources: dict[str, Resource] = resources or {}
 
 
 	def register(self,
 		run_id: None | int = None,
-		tier: None | Literal[-1, 0, 1, 2, 3] = None,
+		tier: None | Literal[-1, 0, 1, 2, 3, 4] = None,
 		task_nbr: None | int = None,
 		code: EventCode = EventCode.RUNNING
 	) -> None:
+		""" Registers event, which, unless self.dry_run is True, creates an EventDocument in the DB """
 
 		doc = {'process': self.process_name} | self.extra
 		doc['code'] = code
 
 		if tier:
 			doc['tier'] = tier
 
@@ -108,24 +110,28 @@
 			raise ValueError(
 				f"Resource name '{resource.name}' already defined"
 				f"(use overwrite=True to ignore)"
 			)
 		self.resources[resource.name] = resource
 
 
-	def set_tier(self, val: Literal[0, 1, 2, 3]) -> None:
+	def set_tier(self, val: Literal[0, 1, 2, 3, 4]) -> None:
 		self.extra['tier'] = val
 
 
 	def set_code(self, val: EventCode):
 		if self.code == EventCode.EXCEPTION and val != EventCode.EXCEPTION:
 			raise ValueError("Cannot override EventCode.EXCEPTION")
 		self.code = val
 
 
+	def get_resources(self) -> dict[str, Resource]:
+		return self.resources
+
+
 	def handle_error(self, e: Exception, logger: AmpelLogger) -> None:
 
 		self.code = EventCode.EXCEPTION
 
 		if self.raise_exc:
 			raise e
```

### Comparing `ampel_core-0.8.6/ampel/core/Schedulable.py` & `ampel_core-0.9.0/ampel/core/Schedulable.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/core/UnitLoader.py` & `ampel_core-0.9.0/ampel/core/UnitLoader.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/core/UnitLoader.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                07.10.2019
-# Last Modified Date:  13.12.2021
+# Last Modified Date:  04.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import os, sys
 from importlib import import_module
 from pathlib import Path
 from hashlib import blake2b
 from contextlib import contextmanager
@@ -33,14 +33,15 @@
 from ampel.model.t3.AliasableModel import AliasableModel
 from ampel.config.AmpelConfig import AmpelConfig
 from ampel.log.AmpelLogger import AmpelLogger, LogFlag, VERBOSE
 from ampel.log.handlers.ChanRecordBufHandler import ChanRecordBufHandler
 from ampel.log.handlers.DefaultRecordBufferingHandler import DefaultRecordBufferingHandler
 from ampel.util.hash import build_unsafe_dict_id
 
+
 T = TypeVar('T', bound=AmpelUnit)
 LT = TypeVar('LT', bound=LogicalUnit)
 CT = TypeVar('CT', bound=ContextUnit)
 pyv = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
 env = ('conda_' + os.environ["CONDA_DEFAULT_ENV"]) if 'CONDA_DEFAULT_ENV' in os.environ else 'default'
 
 class UnitLoader:
@@ -285,44 +286,45 @@
 		config: None | int | str | dict[str, Any] = None,
 		override: None | dict[str, Any] = None,
 		kwargs: None | dict[str, Any] = None,
 		unfreeze: bool = True
 	) -> dict[str, Any]:
 		""" :raises: ValueError if config alias is not found """
 
-		ret: None | dict[str, Any] = {}
+		base_conf: dict[str, Any] = {}
 
 		if isinstance(config, (dict, str)):
-			ret = self.resolve_aliases(config)
 
+			base_conf = self.resolve_aliases(config)
+			if base_conf is None:
+				raise ValueError(f"Config alias {config} not found")
+
+		# Hashed t2 unit configs
 		elif isinstance(config, int):
 
 			try:
 				d = self.config.get_conf_id(config)
 			# confid not found (obsolete or dynamically generated by isolated process)
 			except Exception as e:
 				assert self.db
 				l = list(self.db.col_conf_ids.find({"_id": config}))
 				if len(l) == 0:
 					raise e
 				del l[0]['_id']
 				d = l[0]
 				
-			ret = recursive_unfreeze(d) if unfreeze and isinstance(d, ReadOnlyDict) else d
+			base_conf = recursive_unfreeze(d) if (unfreeze and isinstance(d, ReadOnlyDict)) else d
 
 			# save un-registered (in ampel conf but not in db) confid to external collection for posterity
 			if self.provenance:
 				assert self.db
 				if config not in self.db.conf_ids:
-					self.db.add_conf_id(config, ret)
-
-		if ret is None and config is not None:
-			raise ValueError(f"Config alias {config} not found")
+					self.db.add_conf_id(config, base_conf)
 
-		return merge_dicts([ret, override, kwargs]) or {}
+		return merge_dicts([base_conf, override, kwargs]) or {}
 
 
 	def resolve_aliases(self, value):
 		"""
 		Recursively resolve aliases from config
 		"""
 		if isinstance(value, str):
@@ -330,16 +332,16 @@
 				if value in adict:
 					return self.resolve_aliases(adict[value])
 			return value
 		elif isinstance(value, list):
 			return [self.resolve_aliases(v) for v in value]
 		elif isinstance(value, dict):
 			return {k: self.resolve_aliases(v) for k, v in value.items()}
-		else:
-			return value
+
+		return value
 
 
 	def resolve_secrets(self, unit_type: type[AmpelUnit], init_kwargs: dict[str, Any]) -> dict[str, Any]:
 		"""
 		Add a resolved Secret instance to init_kwargs for every Secret field of
 		unit_type.
 		"""
```

### Comparing `ampel_core-0.8.6/ampel/demo/DemoFirstPointT2Unit.py` & `ampel_core-0.9.0/ampel/demo/DemoFirstPointT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/demo/DemoPlainT3Unit.py` & `ampel_core-0.9.0/ampel/demo/DemoT4RunTimeAliasGenerator.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,38 +1,27 @@
-#!/usr/bin/env python
+#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
-# File:                Ampel-core/ampel/demo/DemoPlainT3Unit.py
+# File:                Ampel-core/ampel/demo/DemoT4RunTimeAliasGenerator.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
-# Date:                17.12.2021
-# Last Modified Date:  17.12.2021
+# Date:                19.12.2022
+# Last Modified Date:  04.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
+from random import randint
 from ampel.types import UBson
 from ampel.struct.UnitResult import UnitResult
-from ampel.struct.T3Store import T3Store
-from ampel.abstract.AbsT3PlainUnit import AbsT3PlainUnit
+from ampel.abstract.AbsT4Unit import AbsT4Unit
 
 
-class DemoPlainT3Unit(AbsT3PlainUnit):
-
-	a_parameter: int = 9000
-	my_t3_doc_tag: str = "A_TAG"
+class DemoT4RunTimeAliasGenerator(AbsT4Unit):
+	""" To be run with T4RunTimeContextUpdater """
 
+	debug: bool = False
+	alias_name: str = "%%steven"
 
 	def post_init(self) -> None:
 		self.logger.info("post_init was called")
 
-
-	def process(self, t3s: T3Store) -> UBson | UnitResult:
-
-		self.logger.info("Running DemoPlainT3Unit")
-
-		if not t3s.units:
-			self.logger.info(f"T3 store contains t3 views for units: {t3s.units}")
-		else:
-			self.logger.info("T3 store contains no t3 views")
-
-		return UnitResult(
-			body = {'a_parameter': self.a_parameter},
-			tag = self.my_t3_doc_tag
-		)
+	def do(self) -> UBson | UnitResult:
+		self.logger.info(f"Running {self.__class__.__name__}")
+		return {self.alias_name: randint(10, 30)}
```

### Comparing `ampel_core-0.8.6/ampel/demo/DemoPointT2Unit.py` & `ampel_core-0.9.0/ampel/demo/DemoPointT2Unit.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/demo/DemoProcessor.py` & `ampel_core-0.9.0/ampel/demo/DemoProcessor.py`

 * *Files 15% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any
 from ampel.abstract.AbsEventUnit import AbsEventUnit
 from ampel.model.UnitModel import UnitModel
 from ampel.log import AmpelLogger
 from ampel.core.EventHandler import EventHandler
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 
 
 class DemoProcessor(AbsEventUnit):
 
 	parameter_a: int
 	parameter_b: int = 200
 
@@ -45,13 +45,13 @@
 		ctx = self.context
 
 		# Which contains an instance of UnitLoader
 		loader = ctx.loader
 
 		# With which base units can be instantiated
 		unit = loader.new_logical_unit(
-			model = UnitModel(unit = "DemoReviewT3Unit"),
+			model = UnitModel(unit = "DemoT3Unit"),
 			logger = logger,
-			sub_type = AbsT3ReviewUnit
+			sub_type = AbsT3Unit
 		)
 
 		print(unit)
```

### Comparing `ampel_core-0.8.6/ampel/demo/DemoReviewT3Unit.py` & `ampel_core-0.9.0/ampel/demo/DemoT3Unit.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,43 +1,44 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File:                Ampel-core/ampel/demo/DemoReviewT3Unit.py
+# File:                Ampel-core/ampel/demo/DemoT3Unit.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                09.06.2020
-# Last Modified Date:  17.12.2021
+# Last Modified Date:  03.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from collections.abc import Generator
 from ampel.types import UBson, T3Send
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.struct.JournalAttributes import JournalAttributes
 from ampel.struct.UnitResult import UnitResult
 from ampel.view.SnapView import SnapView
 from ampel.struct.T3Store import T3Store
 
 
-class DemoReviewT3Unit(AbsT3ReviewUnit[SnapView]):
+class DemoT3Unit(AbsT3Unit[SnapView]):
 
 	parameter: int = 10
 
 	def process(self,
 		gen: Generator[SnapView, T3Send, None],
 		t3s: T3Store
 	) -> UBson | UnitResult:
 
-		self.logger.info(f"DemoReviewT3Unit output (parameter={self.parameter}):")
+		self.logger.info(f"DemoT3Unit output (parameter={self.parameter}):")
 
 		for i, v in enumerate(gen, 1):
 
 			self.logger.info("id: " + str(v.id))
 			gen.send(
 				# This journal customization will be applied only to the current 'stock'
 				JournalAttributes(tag="DemoT3SpecificTag", extra={'a': 1})
 			)
 
 		# This journal customization will be applied to all stocks
 		return UnitResult(
 			body = {'param': 'value'},
 			code = 10,
-			journal = JournalAttributes(tag="DemoReviewT3UnitTag")
+			tag = "T3DocTag",
+			journal = JournalAttributes(tag="DemoT3UnitTag")
 		)
```

### Comparing `ampel_core-0.8.6/ampel/ingest/ChainedIngestionHandler.py` & `ampel_core-0.9.0/ampel/ingest/ChainedIngestionHandler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/ingest/ChainedT0Muxer.py` & `ampel_core-0.9.0/ampel/ingest/ChainedT0Muxer.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/ingest/StockCompiler.py` & `ampel_core-0.9.0/ampel/ingest/StockCompiler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/ingest/T0Compiler.py` & `ampel_core-0.9.0/ampel/ingest/T0Compiler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/ingest/T1Compiler.py` & `ampel_core-0.9.0/ampel/ingest/T1Compiler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/ingest/T2Compiler.py` & `ampel_core-0.9.0/ampel/ingest/T2Compiler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/AmpelLogger.py` & `ampel_core-0.9.0/ampel/log/AmpelLogger.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/LightLogRecord.py` & `ampel_core-0.9.0/ampel/log/LightLogRecord.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/LogFlag.py` & `ampel_core-0.9.0/ampel/log/LogFlag.py`

 * *Files 12% similar despite different names*

```diff
@@ -10,34 +10,35 @@
 from enum import IntFlag
 
 # flake8: noqa: E221
 class LogFlag(IntFlag):
 	"""
 	Flag used for each log entry stored in the DB.
 	Value fits in a MongoDB int32.
-	bits 0-4: tier
-	bits 5-6: run type
-	bits 6-7: location (core system or base units)
-	bits 8-13: log level
+	bits 0-5: tier
+	bits 5-7: run type
+	bits 7-8: location (core system or base units)
+	bits 9-14: log level
 	"""
 
 	# Execution layer
 	T0                      = 1
 	T1                      = 2
 	T2                      = 4
 	T3                      = 8
+	T4                      = 16
 
 	# Run type
-	SCHEDULED_RUN           = 16
-	MANUAL_RUN              = 32
+	SCHEDULED_RUN           = 32
+	MANUAL_RUN              = 64
 
 	# Location
-	UNIT                    = 64
-	CORE                    = 128
+	UNIT                    = 128
+	CORE                    = 256
 
 	# Log level
-	DEBUG                   = 1<<8
-	VERBOSE                 = 1<<9
-	INFO                    = 1<<10
-	SHOUT                   = 1<<11 # SHOUT is for convenience only, saved as INFO into DB
-	WARNING                 = 1<<12
-	ERROR                   = 1<<13
+	DEBUG                   = 1<<9
+	VERBOSE                 = 1<<10
+	INFO                    = 1<<11
+	SHOUT                   = 1<<12 # SHOUT is for convenience only, saved as INFO into DB
+	WARNING                 = 1<<13
+	ERROR                   = 1<<14
```

### Comparing `ampel_core-0.8.6/ampel/log/LoggingErrorReporter.py` & `ampel_core-0.9.0/ampel/log/LoggingErrorReporter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/LogsDumper.py` & `ampel_core-0.9.0/ampel/log/LogsDumper.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/handlers/AmpelStreamHandler.py` & `ampel_core-0.9.0/ampel/log/handlers/AmpelStreamHandler.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/log/handlers/AmpelStreamHandler.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                17.10.2018
-# Last Modified Date:  24.05.2021
+# Last Modified Date:  03.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import sys, time
 from sys import _getframe
 from os.path import basename
 from time import strftime
 from typing import Literal
@@ -144,20 +144,19 @@
 		if lvl & 64:
 			out += ' UNIT'
 		if lvl & 128:
 			out += ' CORE'
 
 		if self.provenance and record.filename:
 			if record.filename[0] == '<': # ipython
-				print(lvl)
-				out += f' {record.filename} {levels[lvl >> 8]}'
+				out += f' {record.filename} {levels[lvl >> 9]}'
 			else:
-				out += f' {record.filename[:-3]}:{record.lineno} {levels[lvl >> 8]}'
+				out += f' {record.filename[:-3]}:{record.lineno} {levels[lvl >> 9]}'
 		else:
-			out += f' {levels[lvl >> 8]}'
+			out += f' {levels[lvl >> 9]}'
 
 		if record.extra:
 			suffix = [f'{k}={record.extra[k]}' for k in record.extra]
 		else:
 			suffix = []
 
 		if record.stock:
```

### Comparing `ampel_core-0.8.6/ampel/log/handlers/ChanRecordBufHandler.py` & `ampel_core-0.9.0/ampel/log/handlers/ChanRecordBufHandler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/handlers/DefaultRecordBufferingHandler.py` & `ampel_core-0.9.0/ampel/log/handlers/DefaultRecordBufferingHandler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/handlers/EnclosedChanRecordBufHandler.py` & `ampel_core-0.9.0/ampel/log/handlers/EnclosedChanRecordBufHandler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/handlers/RecordBufferingHandler.py` & `ampel_core-0.9.0/ampel/log/handlers/RecordBufferingHandler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/log/utils.py` & `ampel_core-0.9.0/ampel/log/utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,23 +3,24 @@
 # File:                Ampel-core/ampel/log/utils.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                30.09.2018
 # Last Modified Date:  11.11.2021
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-import sys, traceback
+import sys, traceback, contextlib
 from math import log2
 from bson import ObjectId
 from datetime import datetime
-from typing import overload
+from typing import overload, Generator
 from pymongo import WriteConcern
 
 from ampel.types import JDict
 from ampel.core.AmpelDB import AmpelDB
+from ampel.config.AmpelConfig import AmpelConfig
 from ampel.util.collections import has_nested_type
 from ampel.log.AmpelLogger import AmpelLogger
 from ampel.log.LogFlag import LogFlag
 from ampel.metrics.AmpelMetricsRegistry import AmpelMetricsRegistry
 from ampel.protocol.LoggerProtocol import LoggerProtocol
 
 exception_counter = AmpelMetricsRegistry.counter(
@@ -297,7 +298,24 @@
 
 	elif isinstance(arg, list):
 		if has_nested_type(arg, dict):
 			arg = arg.copy() # type: ignore[attr-defined]
 			return [convert_dollars(el) for el in arg] # type: ignore[arg-type]
 
 	return arg
+
+
+@contextlib.contextmanager
+def get_logger(ac: AmpelConfig, log_profile: None | str) -> Generator[AmpelLogger, None, None]:
+
+	if log_profile:
+		logger = AmpelLogger.get_logger(
+			console=ac.get(
+				f'logging.{log_profile}.console',
+				dict, raise_exc=True
+			)
+		)
+	else:
+		logger = AmpelLogger.get_logger()
+
+	yield logger
+	logger.flush()
```

### Comparing `ampel_core-0.8.6/ampel/metrics/AmpelDBCollector.py` & `ampel_core-0.9.0/ampel/metrics/AmpelDBCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/metrics/AmpelMetricsRegistry.py` & `ampel_core-0.9.0/ampel/metrics/AmpelMetricsRegistry.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/metrics/AmpelProcessCollector.py` & `ampel_core-0.9.0/ampel/metrics/AmpelProcessCollector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/metrics/prometheus.py` & `ampel_core-0.9.0/ampel/metrics/prometheus.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ChannelModel.py` & `ampel_core-0.9.0/ampel/model/ChannelModel.py`

 * *Files 13% similar despite different names*

```diff
@@ -3,18 +3,17 @@
 # File:                Ampel-core/ampel/model/ChannelModel.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                09.10.2019
 # Last Modified Date:  22.08.2022
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Any
 from collections.abc import Sequence
 from ampel.base.AmpelBaseModel import AmpelBaseModel
-from ampel.model.purge.PurgeModel import PurgeModel
+#from ampel.model.purge.PurgeModel import PurgeModel
 #from ampel.model.ViewModel import ViewModel
 
 
 class ChannelModel(AmpelBaseModel):
 
 	channel: int | str
 	version: None | int | float | str
```

### Comparing `ampel_core-0.8.6/ampel/model/ProcessModel.py` & `ampel_core-0.9.0/ampel/model/ProcessModel.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,29 +1,29 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/model/ProcessModel.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                06.10.2019
-# Last Modified Date:  30.12.2021
+# Last Modified Date:  04.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import schedule as sched
 from typing import Literal
 from collections.abc import Sequence
 from ampel.base.AmpelBaseModel import AmpelBaseModel
 from ampel.types import ChannelId
 from ampel.model.UnitModel import UnitModel
 from ampel.config.ScheduleEvaluator import ScheduleEvaluator
 
 
 class ProcessModel(AmpelBaseModel):
 
 	name: str
-	version: int | float | str
+	version: None | int | float | str
 	active: bool = True
 	tier: None | Literal[0, 1, 2, 3]
 	schedule: Sequence[str]
 	channel: None | ChannelId | Sequence[ChannelId]
 	distrib: None | str
 	source: None | str
 	isolate: bool = True
```

### Comparing `ampel_core-0.8.6/ampel/model/aux/AuxAliasableModel.py` & `ampel_core-0.9.0/ampel/model/aux/AuxAliasableModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/aux/FilterCriterion.py` & `ampel_core-0.9.0/ampel/model/aux/FilterCriterion.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/builder/BuilderAliasModel.py` & `ampel_core-0.9.0/ampel/model/builder/BuilderAliasModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/builder/RemoteUnitDefinition.py` & `ampel_core-0.9.0/ampel/mongo/model/AmpelDBModel.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,16 +1,18 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File:                Ampel-core/ampel/model/builder/RemoteUnitDefinition.py
+# File:                Ampel-core/ampel/model/db/AmpelDBModel.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
-# Date:                06.11.2019
-# Last Modified Date:  15.06.2020
+# Date:                19.10.2019
+# Last Modified Date:  08.03.2020
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import List
+from typing import Sequence
+from ampel.mongo.model.AmpelColModel import AmpelColModel
+from ampel.mongo.model.MongoClientRoleModel import MongoClientRoleModel
 from ampel.base.AmpelBaseModel import AmpelBaseModel
 
-class RemoteUnitDefinition(AmpelBaseModel):
-
-	class_name: str
-	base: list['str']
+class AmpelDBModel(AmpelBaseModel):
+	name: str
+	collections: Sequence[AmpelColModel]
+	role: MongoClientRoleModel
```

### Comparing `ampel_core-0.8.6/ampel/model/ingest/CompilerOptions.py` & `ampel_core-0.9.0/ampel/model/ingest/CompilerOptions.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/DualIngestDirective.py` & `ampel_core-0.9.0/ampel/model/ingest/DualIngestDirective.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/FilterModel.py` & `ampel_core-0.9.0/ampel/model/ingest/FilterModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/IngestBody.py` & `ampel_core-0.9.0/ampel/model/ingest/IngestBody.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/IngestDirective.py` & `ampel_core-0.9.0/ampel/model/ingest/IngestDirective.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/MuxModel.py` & `ampel_core-0.9.0/ampel/model/ingest/MuxModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/T1Combine.py` & `ampel_core-0.9.0/ampel/model/ingest/T1Combine.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/T1CombineCompute.py` & `ampel_core-0.9.0/ampel/model/ingest/T1CombineCompute.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/T1CombineComputeNow.py` & `ampel_core-0.9.0/ampel/model/ingest/T1CombineComputeNow.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/ingest/T2Compute.py` & `ampel_core-0.9.0/ampel/model/ingest/T2Compute.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/purge/PurgeContentModel.py` & `ampel_core-0.9.0/ampel/model/purge/PurgeContentModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/purge/PurgeLogsModel.py` & `ampel_core-0.9.0/ampel/model/purge/PurgeLogsModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/purge/PurgeModel.py` & `ampel_core-0.9.0/ampel/model/purge/PurgeModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/t3/AliasableModel.py` & `ampel_core-0.9.0/ampel/model/t3/AliasableModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/t3/LoaderDirective.py` & `ampel_core-0.9.0/ampel/model/t3/LoaderDirective.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/t3/QueryMatchModel.py` & `ampel_core-0.9.0/ampel/model/t3/QueryMatchModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/t3/T2FilterModel.py` & `ampel_core-0.9.0/ampel/model/t3/T2FilterModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/t3/T3IncludeDirective.py` & `ampel_core-0.9.0/ampel/model/t3/T3IncludeDirective.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/t3/T3ProjectionDirective.py` & `ampel_core-0.9.0/ampel/model/t3/T3ProjectionDirective.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,14 +20,14 @@
 
 	#: AbsT3Filter sub unit to use for down-selection of ampel buffers
 	filter: None | UnitModel
 
 	#: AbsT3Projector sub unit capable of discarding selected ampel buffer attributes/fields
 	project: None | UnitModel
 
-	#: t3 units (AbsT3ReviewUnit) to execute
+	#: t3 units (AbsT3Unit) to execute
 	execute: Sequence[UnitModel]
 
 	def __init__(self, **kwargs):
 		if isinstance(v := kwargs.get("execute"), (dict, UnitModel)):
 			kwargs["execute"] = [v]
 		super().__init__(**kwargs)
```

### Comparing `ampel_core-0.8.6/ampel/model/time/QueryTimeModel.py` & `ampel_core-0.9.0/ampel/model/time/QueryTimeModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/time/TimeConstraintModel.py` & `ampel_core-0.9.0/ampel/model/time/TimeConstraintModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/time/TimeDeltaModel.py` & `ampel_core-0.9.0/ampel/model/time/TimeDeltaModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/time/TimeLastRunModel.py` & `ampel_core-0.9.0/ampel/model/time/TimeLastRunModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/time/TimeStringModel.py` & `ampel_core-0.9.0/ampel/model/time/TimeStringModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/model/time/UnixTimeModel.py` & `ampel_core-0.9.0/ampel/model/time/UnixTimeModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/model/AmpelColModel.py` & `ampel_core-0.9.0/ampel/mongo/model/AmpelColModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/model/FieldModel.py` & `ampel_core-0.9.0/ampel/mongo/model/FieldModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/model/IndexModel.py` & `ampel_core-0.9.0/ampel/mongo/model/IndexModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/model/MongoClientOptionsModel.py` & `ampel_core-0.9.0/ampel/mongo/model/MongoClientOptionsModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/model/ShortIndexModel.py` & `ampel_core-0.9.0/ampel/mongo/model/ShortIndexModel.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/purge/MongoStockDeleter.py` & `ampel_core-0.9.0/ampel/mongo/purge/MongoStockDeleter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/query/general.py` & `ampel_core-0.9.0/ampel/mongo/query/general.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/query/stock.py` & `ampel_core-0.9.0/ampel/mongo/query/stock.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/query/t1.py` & `ampel_core-0.9.0/ampel/mongo/query/t1.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/query/t2.py` & `ampel_core-0.9.0/ampel/mongo/query/t2.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/query/var/LogsLoader.py` & `ampel_core-0.9.0/ampel/mongo/query/var/LogsLoader.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/query/var/LogsMatcher.py` & `ampel_core-0.9.0/ampel/mongo/query/var/LogsMatcher.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/query/var/events.py` & `ampel_core-0.9.0/ampel/mongo/query/var/events.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/schema.py` & `ampel_core-0.9.0/ampel/mongo/schema.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/DBUpdatesBuffer.py` & `ampel_core-0.9.0/ampel/mongo/update/DBUpdatesBuffer.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/MongoStockIngester.py` & `ampel_core-0.9.0/ampel/mongo/update/MongoStockIngester.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/MongoStockUpdater.py` & `ampel_core-0.9.0/ampel/mongo/update/MongoStockUpdater.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/MongoT0Ingester.py` & `ampel_core-0.9.0/ampel/mongo/update/MongoT0Ingester.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/MongoT1Ingester.py` & `ampel_core-0.9.0/ampel/mongo/update/MongoT1Ingester.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/MongoT2Ingester.py` & `ampel_core-0.9.0/ampel/mongo/update/MongoT2Ingester.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/MongoT3Ingester.py` & `ampel_core-0.9.0/ampel/mongo/update/MongoT3Ingester.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/update/var/DBLoggingHandler.py` & `ampel_core-0.9.0/ampel/mongo/update/var/DBLoggingHandler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/utils.py` & `ampel_core-0.9.0/ampel/mongo/utils.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/view/AbsMongoFlatMultiView.py` & `ampel_core-0.9.0/ampel/mongo/view/AbsMongoFlatMultiView.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/view/AbsMongoView.py` & `ampel_core-0.9.0/ampel/mongo/view/AbsMongoView.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/view/FrozenValuesDict.py` & `ampel_core-0.9.0/ampel/mongo/view/FrozenValuesDict.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/view/MongoAndView.py` & `ampel_core-0.9.0/ampel/mongo/view/MongoAndView.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/view/MongoOneView.py` & `ampel_core-0.9.0/ampel/mongo/view/MongoOneView.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/mongo/view/MongoOrView.py` & `ampel_core-0.9.0/ampel/mongo/view/MongoOrView.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/ops/AmpelExceptionPublisher.py` & `ampel_core-0.9.0/ampel/ops/AmpelExceptionPublisher.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/ops/OpsProcessor.py` & `ampel_core-0.9.0/ampel/ops/OpsProcessor.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/run/server.py` & `ampel_core-0.9.0/ampel/run/server.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/secret/AESecretProvider.py` & `ampel_core-0.9.0/ampel/secret/AESecretProvider.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/secret/DictSecretProvider.py` & `ampel_core-0.9.0/ampel/secret/DictSecretProvider.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/secret/DirSecretProvider.py` & `ampel_core-0.9.0/ampel/secret/DirSecretProvider.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/secret/PotemkinSecretProvider.py` & `ampel_core-0.9.0/ampel/secret/PotemkinSecretProvider.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t1/T1SimpleCombiner.py` & `ampel_core-0.9.0/ampel/t1/T1SimpleCombiner.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t1/T1SimpleRetroCombiner.py` & `ampel_core-0.9.0/ampel/t1/T1SimpleRetroCombiner.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t2/T2Utils.py` & `ampel_core-0.9.0/ampel/t2/T2Utils.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t2/T2Worker.py` & `ampel_core-0.9.0/ampel/t2/T2Worker.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/README.md` & `ampel_core-0.9.0/ampel/t3/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -29,15 +29,15 @@
 Known implementing class: `T3SessionLastRunTime`, `T3SessionAlertsNumber`
 
 Fetch/generate session information that will be provided to T3 units via `T3Store.session`.
 
 ## Execute
 
 Contains a list of directives.\
-A commonly used directive is `T3ReviewDirective` which allows to execute `AbsT3ReviewUnit` instances
+A commonly used directive is `T3ReviewDirective` which allows to execute `AbsT3Unit` instances
 
 ### T3ReviewDirective
 
 #### Supply
 
 ##### Select
```

### Comparing `ampel_core-0.8.6/ampel/t3/T3DocBuilder.py` & `ampel_core-0.9.0/ampel/t3/stage/T3BaseStager.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,54 +1,61 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File:                Ampel-core/ampel/t3/T3DocBuilder.py
+# File:                Ampel-core/ampel/t3/stage/T3BaseStager.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                08.12.2021
-# Last Modified Date:  28.08.2022
+# Last Modified Date:  03.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from time import time
-from datetime import datetime
-from typing import Any, Union
-from importlib import import_module
-from collections.abc import Iterable
-
-from ampel.types import Traceless, StockId, UBson, ubson
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
-from ampel.abstract.AbsT3PlainUnit import AbsT3PlainUnit
-from ampel.abstract.AbsT3ControlUnit import AbsT3ControlUnit
+from typing import Any
+from collections.abc import Generator
+
+from ampel.types import ChannelId, Traceless, OneOrMany, Tag, UBson, StockId
+from ampel.abstract.AbsT3Stager import AbsT3Stager
+from ampel.abstract.AbsT3Unit import AbsT3Unit, T
 from ampel.abstract.AbsUnitResultAdapter import AbsUnitResultAdapter
-from ampel.model.t3.T3DocBuilderModel import T3DocBuilderModel
 from ampel.log.AmpelLogger import AmpelLogger
-from ampel.core.ContextUnit import ContextUnit
 from ampel.core.EventHandler import EventHandler
-from ampel.content.T3Document import T3Document
-from ampel.content.MetaRecord import MetaRecord
+from ampel.core.DocBuilder import DocBuilder
+from ampel.model.UnitModel import UnitModel
+from ampel.struct.T3Store import T3Store
 from ampel.struct.UnitResult import UnitResult
-from ampel.enum.DocumentCode import DocumentCode
-from ampel.enum.MetaActionCode import MetaActionCode
+from ampel.content.T3Document import T3Document
 from ampel.enum.JournalActionCode import JournalActionCode
 from ampel.mongo.update.MongoStockUpdater import MongoStockUpdater
-from ampel.struct.T3Store import T3Store
+from ampel.t3.stage.BaseViewGenerator import BaseViewGenerator
 from ampel.util.mappings import dictify
-from ampel.util.tag import merge_tags
-from ampel.util.hash import build_unsafe_dict_id
-
-AbsT3s = Union[AbsT3ControlUnit, AbsT3ReviewUnit, AbsT3PlainUnit]
 
 
-class T3DocBuilder(ContextUnit, T3DocBuilderModel):
+class T3BaseStager(AbsT3Stager, DocBuilder, abstract=True):
 	"""
-	Provides methods for handling UnitResult and generating a T3Document out of it
+	Base (abstract) class for several stagers provided by ampel.
+	This class does not implement the method stage(...) required by AbsT3Stager,
+	it is up to the subclass to do it according to requirements.
 	"""
 
+
 	logger: Traceless[AmpelLogger]
 	event_hdlr: Traceless[EventHandler]
 
+	#: tag: tag(s) to add to the :class:`~ampel.content.JournalRecord.JournalRecord` of each selected stock
+	extra_journal_tag: None | OneOrMany[Tag] = None
+
+	#: Record the invocation of this event in the stock journal
+	update_journal: bool = True
+
+	#: Whether t3 result should be added to t3 store once available
+	propagate: bool = True
+
+	#: Applies only for underlying T3ReviewUnits.
+	#: Note that if True, a T3 document will be created even if a t3 unit returns None
+	save_stock_ids: bool = False
+
 
 	def __init__(self, **kwargs) -> None:
 
 		super().__init__(**kwargs)
 		self.adapters: dict[str, AbsUnitResultAdapter] = {}
 		self.stock_updr = MongoStockUpdater(
 			ampel_db = self.context.db,
@@ -59,25 +66,38 @@
 			raise_exc = self.event_hdlr.raise_exc,
 			extra_tag = self.extra_journal_tag,
 			update_journal = self.update_journal,
 			bump_updated = False
 		)
 
 
+	def get_unit(self, unit_model: UnitModel, chan: None | OneOrMany[ChannelId] = None) -> AbsT3Unit:
+
+		# new_safe_logical_unit returns a T3 unit instantiated with
+		# a logger based on DefaultRecordBufferingHandler
+		return self.context.loader.new_safe_logical_unit(
+			unit_model,
+			unit_type = AbsT3Unit,
+			logger = self.logger,
+			_chan = self.channel or chan # type: ignore # to be improved when time allows
+		)
+
+
 	def handle_t3_result(self,
-		t3_unit: AbsT3s,
+		t3_unit: AbsT3Unit,
 		res: UBson | UnitResult,
 		t3s: T3Store,
 		stocks: None | list[StockId],
-		ts: float
+		ts: float,
+		log_extra: None | dict[str, Any] = None
 	) -> None | T3Document:
 
 		# Let's consider logs as a result product
-		if (buf_hdlr := getattr(t3_unit, '_buf_hdlr')) and buf_hdlr.buffer:
-			buf_hdlr.forward(self.logger)
+		if (buf_hdlr := getattr(t3_unit, '_buf_hdlr', None)) and buf_hdlr.buffer:
+			buf_hdlr.forward(self.logger, extra=log_extra)
 
 		if isinstance(res, UnitResult):
 			if stocks and res.journal:
 				self.stock_updr.add_journal_record(
 					stock = stocks, # used to match stock docs
 					jattrs = res.journal,
 					unit = t3_unit.__class__.__name__,
@@ -88,130 +108,45 @@
 		elif res is not None or (res is None and self.save_stock_ids and stocks):
 			return self.craft_t3_doc(t3_unit, res, t3s, ts, stocks)
 
 		return None
 
 
 	def craft_t3_doc(self,
-		t3_unit: AbsT3s,
+		t3_unit: AbsT3Unit,
 		res: None | UBson | UnitResult,
 		t3s: T3Store,
 		ts: float,
 		stocks: None | list[StockId] = None
 	) -> T3Document:
 
-		t3d: T3Document = {'process': self.event_hdlr.process_name} # type: ignore[typeddict-item]
-		actact = MetaActionCode(0)
-		now = datetime.now()
-
-		if self.human_timestamp:
-			t3d['datetime'] = now.strftime(self.human_timestamp_format)
-
-		t3d['unit'] = t3_unit.__class__.__name__
-		t3d['code'] = actact
-
-		conf = t3_unit._get_trace_content()
-		meta: MetaRecord = {
-			'run': self.event_hdlr.get_run_id(),
-			'ts': int(now.timestamp()),
-			'duration': time() - ts
-		}
-
-		confid = build_unsafe_dict_id(conf)
-		self.context.db.add_conf_id(confid, conf)
-
-		# Live dangerously
-		if confid not in self.context.config._config['confid']:
-			dict.__setitem__(self.context.config._config['confid'], confid, conf)
-
-		t3d['confid'] = confid
-
-		if self.resolve_config:
-			t3d['config'] = conf
-
-		if self.channel:
-			t3d['channel'] = self.channel
-			actact |= MetaActionCode.ADD_CHANNEL
-
+		t3d = super().craft_doc(self.event_hdlr, t3_unit, res, ts, doc_type=T3Document)
 		if self.save_stock_ids and stocks:
 			t3d['stock'] = stocks
 
-		t3d['code'] = DocumentCode.OK
-		t3d['meta'] = meta # note: mongodb maintains key order
-
 		if t3s.session:
 			t3d['session'] = dictify(t3s.session)
 
-		if isinstance(res, UnitResult):
-
-			if res.code:
-				t3d['code'] = res.code
-				actact |= MetaActionCode.SET_UNIT_CODE
-			else:
-				actact |= MetaActionCode.SET_CODE
-
-			if res.tag:
-				if self.tag:
-					t3d['tag'] = merge_tags(self.tag, res.tag) # type: ignore
-				else:
-					t3d['tag'] = res.tag
-			elif self.tag:
-				t3d['tag'] = self.tag
-
-			if res.body:
-
-				if res.adapter:
-					if res.adapter not in self.adapters:
-						self.adapters[res.adapter] = getattr(
-							import_module(f"ampel.core.adapter.{res.adapter}"),
-							res.adapter
-						)(context=self.context, run_id=self.event_hdlr.get_run_id())
-					res = self.adapters[res.adapter].handle(res)
-
-				t3d['body'] = res.body
-				actact |= MetaActionCode.ADD_BODY
-
-		else:
-
-			if self.tag:
-				t3d['tag'] = self.tag
-
-			# bson
-			if isinstance(res, ubson):
-				t3d['body'] = res
-				actact |= (MetaActionCode.ADD_BODY | MetaActionCode.SET_CODE)
-
-			else:
-				actact |= MetaActionCode.SET_CODE
-
-		meta['activity'] = [{'action': actact}]
-
-		if self.human_id:
-			ids = []
-			if 'process' in self.human_id:
-				ids.append("[%s]" % self.event_hdlr.process_name)
-			if 'taskindex' in self.human_id:
-				ids.append("[#%s]" % self.event_hdlr.process_name.split("#")[-1])
-			if 'unit' in self.human_id:
-				ids.append("[%s]" % t3_unit.__class__.__name__)
-			if 'tag' in self.human_id and 'tag' in t3d:
-				ids.append("[%s]" % (t3d['tag'] if isinstance(t3d['tag'], (int, str)) else " ".join(t3d['tag']))) # type: ignore[arg-type]
-			if 'config' in self.human_id:
-				ids.append("[%s]" % build_unsafe_dict_id(conf))
-			if 'run' in self.human_id:
-				ids.append("[%s]" % self.stock_updr.run_id) # not great
-			ids.append(now.strftime(self.human_timestamp_format))
-			t3d['_id'] = " ".join(ids)
-
 		return t3d
 
 
-	def flush(self, arg: AbsT3s | Iterable[AbsT3s], extra: None | dict[str, Any] = None) -> None:
-
-		for t3_unit in [arg] if isinstance(arg, (AbsT3ControlUnit, AbsT3ReviewUnit, AbsT3PlainUnit)) else arg:
-
-			if (handlers := getattr(t3_unit.logger, 'handlers')) and handlers[0].buffer:
-				handlers[0].forward(self.logger, extra=extra)
-				self.logger.break_aggregation()
-
+	def proceed(self,
+		t3_unit: AbsT3Unit,
+		view_generator: BaseViewGenerator[T],
+		t3s: T3Store
+	) -> Generator[T3Document, None, None]:
+		"""
+		Executes method 'process' of t3 unit with provided views generator and t3 store.
+		Handles potential t3 unit result as well.
+		"""
+
+		try:
+			self.logger.info("Running T3 unit", extra={'unit': t3_unit.__class__.__name__})
+			ts = time()
+			if (ret := t3_unit.process(view_generator, t3s)) or self.save_stock_ids:
+				if x := self.handle_t3_result(t3_unit, ret, t3s, view_generator.get_stock_ids(), ts):
+					yield x
+		except Exception as e:
+			self.event_hdlr.handle_error(e, self.logger)
+		finally:
 			if self.stock_updr.update_journal:
 				self.stock_updr.flush()
```

### Comparing `ampel_core-0.8.6/ampel/t3/T3Processor.py` & `ampel_core-0.9.0/ampel/t3/T3Processor.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,68 +1,48 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/t3/T3Processor.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                26.02.2018
-# Last Modified Date:  19.12.2022
+# Last Modified Date:  03.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from importlib import import_module
 from typing import Any, Annotated
 
-from ampel.types import OneOrMany
+from ampel.types import ChannelId
 from ampel.abstract.AbsEventUnit import AbsEventUnit
 from ampel.abstract.AbsT3Supplier import AbsT3Supplier
-from ampel.abstract.AbsT3ControlUnit import AbsT3ControlUnit
-from ampel.abstract.AbsProcessorTemplate import AbsProcessorTemplate
+from ampel.abstract.AbsT3Stager import AbsT3Stager
 from ampel.struct.T3Store import T3Store
-from ampel.view.T3DocView import T3DocView
 from ampel.model.UnitModel import UnitModel
 from ampel.model.t3.T3IncludeDirective import T3IncludeDirective
 from ampel.core.EventHandler import EventHandler
 from ampel.log import AmpelLogger, LogFlag, SHOUT
 
 
 class T3Processor(AbsEventUnit):
 
-	template: None | str = None
+	# Require single channel for now (super classes allow multi-channel)
+	channel: None | ChannelId = None
+
 	include: None | T3IncludeDirective
-	execute: Annotated[OneOrMany[UnitModel], AbsT3ControlUnit]
 
+	#: Unit must be a subclass of AbsT3Supplier
+	supply: Annotated[UnitModel, AbsT3Supplier]
 
-	def __init__(self, **kwargs) -> None:
+	#: Unit must be a subclass of AbsT3Stager
+	stage: Annotated[UnitModel, AbsT3Stager]
 
-		if 'template' in kwargs:
-			tpl_name = kwargs.pop("template")
-			ctx = kwargs.pop("context")
-			if ctx is None:
-				raise ValueError("Context required")
-
-			if tpl_name not in ctx.config._config.get('template', []):
-				raise ValueError(f"Unknown process template: {tpl_name}")
-
-			fqn = ctx.config._config['template'][tpl_name]
-			class_name = fqn.split(".")[-1]
-			Tpl = getattr(import_module(fqn), class_name)
-			if not issubclass(Tpl, AbsProcessorTemplate):
-				raise ValueError(f"Unexpected template type: {Tpl}")
-
-			tpl = Tpl(
-				**{
-					k: v for k, v in kwargs.items()
-					if k not in AbsEventUnit._annots
-				}
-			)
-			kwargs.update(
-				tpl.get_model(ctx.config._config, kwargs).dict()['config']
-			)
-			kwargs['context'] = ctx
 
-		super().__init__(**kwargs)
+	def post_init(self):
+		if self.supply.unit not in self.context.config._config['unit']:
+			raise ValueError(f"Unknown supply unit: {self.supply.unit}")
+		if self.stage.unit not in self.context.config._config['unit']:
+			raise ValueError(f"Unknown stager unit: {self.stage.unit}")
 
 
 	def proceed(self, event_hdlr: EventHandler) -> None:
 
 		event_hdlr.set_tier(3)
 		logger = AmpelLogger.from_profile(
 			self.context, self.log_profile, event_hdlr.get_run_id(),
@@ -71,74 +51,81 @@
 		)
 
 		try:
 
 			# Feedback
 			logger.log(SHOUT, f'Running {self.process_name}')
 
-			loader = self.context.loader
 			t3s = T3Store()
 
 			if self.include:
 
 				if self.include.docs:
 					pass # later
 
 				if (x := self.include.session):
 					sdict: dict[str, Any] = {}
 					for model in [x] if isinstance(x, UnitModel) else x:
-						rd = loader.new_context_unit(
+						rd = self.context.loader.new_context_unit(
 							model = model,
 							context = self.context,
 							sub_type = AbsT3Supplier,
 							event_hdlr = event_hdlr,
 							logger = logger
 						).supply(t3s)
 						if rd:
 							sdict |= rd
 					if sdict:
 						t3s.add_session_info(sdict)
 
-			units = self.context.config._config['unit']
-			for i, um in enumerate([self.execute] if isinstance(self.execute, UnitModel) else self.execute):
-
-				if um.unit not in units:
-					raise ValueError(f"Unknown unit: {um.unit}")
+			supplier = self.context.loader.new_context_unit(
+				model = self.supply,
+				context = self.context,
+				sub_type = AbsT3Supplier,
+				logger = logger,
+				event_hdlr = event_hdlr
+			)
 
-				if "AbsT3ControlUnit" not in units[um.unit]['base']:
-					raise ValueError("T3Processor executes only AbsT3ControlUnit units")
+			# Stager unit
+			#############
 
-				t3_unit = loader.new_context_unit(
-					model = um,
-					context = self.context,
-					sub_type = AbsT3ControlUnit,
-					logger = logger,
-					event_hdlr = event_hdlr,
-					channel = self.channel
+			stager = self.context.loader.new_context_unit(
+				model = self.stage,
+				context = self.context,
+				sub_type = AbsT3Stager,
+				logger = logger,
+				event_hdlr = event_hdlr,
+				channel = (
+					self.stage.config['channel'] # type: ignore
+					if self.stage.config and self.stage.config.get('channel') # type: ignore[union-attr]
+					else self.channel
 				)
+			)
 
-				logger.info(
-					f"Processing run block {i}",
-					extra={'unit': t3_unit.__class__.__name__}
-				)
+			logger.info("Running stager", extra={'unit': self.stage.unit})
 
-				# Potential T3Document to be included in the t3 collection
-				if (ret := t3_unit.process(t3s)):
-					for t3d in ret:
-						t3s.add_view(T3DocView.of(t3d, self.context.config))
-						if 'meta' not in t3d:
-							raise ValueError("Invalid T3Document")
-						t3d['meta']['traceid'] = {'t3processor': self._trace_id}
-						if event_hdlr.job_sig:
-							t3d['meta']['jobid'] = event_hdlr.job_sig
-						self.context.db.get_collection('t3').insert_one(t3d) # type: ignore[arg-type]
+			if (doc_gen := stager.stage(supplier.supply(t3s), t3s)):
+				for t3d in doc_gen:
+					if 'meta' not in t3d:
+						raise ValueError("Invalid T3Document")
+					t3d['meta']['traceid'] = {'t3processor': self._trace_id}
+					if event_hdlr.job_sig:
+						t3d['meta']['jobid'] = event_hdlr.job_sig
+					self.context.db.get_collection('t3').insert_one(t3d) # type: ignore[arg-type]
 
+			"""
 			if t3s.resources:
 				for v in t3s.resources.values():
-					event_hdlr.add_resource(v)
+					event_hdlr.add_resource(v, overwrite=self.allow_resource_override)
+
+			if t3s.aliases:
+				for k, v in t3s.aliases.items():
+					event_hdlr.add_alias(k, v, overwrite=self.allow_alias_override)
+			"""
+
 
 		except Exception as e:
 			event_hdlr.handle_error(e, logger)
 
 		# Feedback
 		logger.log(SHOUT, f'Done running {self.process_name}')
 		logger.flush()
```

### Comparing `ampel_core-0.8.6/ampel/t3/include/session/T3SessionAlertsNumber.py` & `ampel_core-0.9.0/ampel/t3/include/session/T3SessionAlertsNumber.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/include/session/T3SessionLastRunTime.py` & `ampel_core-0.9.0/ampel/t3/include/session/T3SessionLastRunTime.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/stage/BaseViewGenerator.py` & `ampel_core-0.9.0/ampel/t3/stage/BaseViewGenerator.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/stage/NoViewGenerator.py` & `ampel_core-0.9.0/ampel/t3/stage/NoViewGenerator.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,24 +5,24 @@
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                17.08.2022
 # Last Modified Date:  17.08.2022
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Iterable
 from collections.abc import Generator
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.mongo.update.MongoStockUpdater import MongoStockUpdater
 from ampel.t3.stage.BaseViewGenerator import BaseViewGenerator, T, T3Send
 
 
 class NoViewGenerator(BaseViewGenerator[T]):
 
 	def __init__(self,
-		unit: AbsT3ReviewUnit,
+		unit: AbsT3Unit,
 		buffers: Iterable[AmpelBuffer],
 		stock_updr: MongoStockUpdater
 	) -> None:
 
 		super().__init__(unit_name = unit.__class__.__name__, stock_updr = stock_updr)
 		self.buffers = buffers
 		self.View = unit._View
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/README.md` & `ampel_core-0.9.0/ampel/t3/stage/README.md`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/stage/SimpleViewGenerator.py` & `ampel_core-0.9.0/ampel/t3/stage/SimpleViewGenerator.py`

 * *Files 8% similar despite different names*

```diff
@@ -5,25 +5,25 @@
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                20.04.2021
 # Last Modified Date:  09.12.2021
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Iterable
 from collections.abc import Generator
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.config.AmpelConfig import AmpelConfig
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.mongo.update.MongoStockUpdater import MongoStockUpdater
 from ampel.t3.stage.BaseViewGenerator import BaseViewGenerator, T, T3Send
 
 
 class SimpleViewGenerator(BaseViewGenerator[T]):
 
 	def __init__(self,
-		unit: AbsT3ReviewUnit,
+		unit: AbsT3Unit,
 		buffers: Iterable[AmpelBuffer],
 		stock_updr: MongoStockUpdater,
 		config: AmpelConfig,
 	) -> None:
 
 		super().__init__(unit_name = unit.__class__.__name__, stock_updr = stock_updr)
 		self.buffers = buffers
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3AdaptativeStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3AdaptativeStager.py`

 * *Files 4% similar despite different names*

```diff
@@ -17,27 +17,28 @@
 from ampel.struct.T3Store import T3Store
 from ampel.view.SnapView import SnapView
 from ampel.model.UnitModel import UnitModel
 from ampel.content.T3Document import T3Document
 from ampel.log import VERBOSE
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.base.AuxUnitRegister import AuxUnitRegister
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.abstract.AbsT3Filter import AbsT3Filter
 from ampel.abstract.AbsT3Projector import AbsT3Projector
 from ampel.t3.stage.T3ThreadedStager import T3ThreadedStager
 from ampel.t3.stage.T3ProjectingStager import RunBlock
 from ampel.t3.stage.ThreadedViewGenerator import ThreadedViewGenerator
 
 
 class T3AdaptativeStager(T3ThreadedStager):
 	"""
 	Unit stager that for each channel found in the elements loaded by the previous stages:
 	
-	- spawns a dedicated :class:`~ampel.t3.run.T3ProjectingStager.T3ProjectingStager` instance configured to filter and project elements wrt this channel
+	- spawns a dedicated :class:`~ampel.t3.run.T3ProjectingStager.T3ProjectingStager`
+	  instance configured to filter and project elements wrt this channel
 	- execute the associated T3 units
 
 	Example:
 	A general T3 process performs a broad, channel-less query.
 	Many stocks are returned, each possibly associated with different channels.
 	This unit builds a set of all channels referenced by the results.
 	Then, for each channel, the information about the referenced elements are posted into
@@ -50,14 +51,16 @@
 
 	This will cause:
 	
 	- Object 1 and 2 to be posted to slack channel #A
 	- Object 2 and 3  to be posted to slack channel #B
 	- Object 3 to be posted to slack channel #C
 	- Object 3 to be posted to slack channel #D
+
+	Note: uses put_views and create_threaded_generators from parent class but not proceed_threaded
 	"""
 
 	execute: Sequence[UnitModel]
 	white_list: None | set[str] = None
 	black_list: None | set[str] = None
 
 	remove_empty: bool = True
@@ -85,15 +88,15 @@
 
 		if self.logger.verbose > 1 and (self.white_list or self.black_list):
 			self.warned: set[ChannelId] = set()
 
 		if self.black_list and self.white_list:
 			raise ValueError("Can't have both black and white lists")
 
-		self.queues: dict[AbsT3ReviewUnit, JoinableQueue[SnapView]] = {}
+		self.queues: dict[AbsT3Unit, JoinableQueue[SnapView]] = {}
 		self.generators: list[ThreadedViewGenerator] = []
 		self.async_results: list[AsyncResult] = []
 
 
 	def stage(self,
 		gen: Generator[AmpelBuffer, None, None],
 		t3s: T3Store
@@ -173,25 +176,28 @@
 
 					self.put_views(buffers, rb.qdict)
 
 			# Send sentinel all threaded generators
 			for q in self.queues.values():
 				q.put(None) # type: ignore[arg-type]
 
-			for async_res, generator, t3_unit in zip(self.async_results, self.generators, list(self.queues.keys())):
-
+			for async_res, generator, t3_unit in zip(
+				self.async_results, self.generators, list(self.queues.keys())
+			):
 				# potential T3Record to be included in the T3Document
 				if (t3_unit_result := async_res.get()):
 					if (z := self.handle_t3_result(t3_unit, t3_unit_result, t3s, generator.stocks, ts)):
 						yield z
 
-				self.flush(t3_unit)
+			if self.stock_updr.update_journal:
+				self.stock_updr.flush()
 
 		return None
 
+
 	def filter_channels(self, channels: set[ChannelId]) -> set[ChannelId]:
 
 		if self.white_list:
 			if self.logger.verbose > 1:
 				tmp = channels & self.white_list
 				for chan in channels - self.white_list:
 					if chan not in self.warned:
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3AggregatingStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3AggregatingStager.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,39 +1,39 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/t3/stage/T3AggregatingStager.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                08.12.2021
-# Last Modified Date:  16.01.2022
+# Last Modified Date:  04.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from time import time
 from ampel.base.AmpelBaseModel import AmpelBaseModel
 from typing import Any
 from collections.abc import Generator, Sequence
 
 from ampel.types import UBson, OneOrMany
-from ampel.t3.T3DocBuilder import T3DocBuilder
+from ampel.t3.stage.T3SequentialStager import T3SequentialStager
 from ampel.struct.T3Store import T3Store
-from ampel.abstract.AbsT3Stager import AbsT3Stager
+from ampel.view.T3DocView import T3DocView
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.content.T3Document import T3Document
 from ampel.content.MetaRecord import MetaRecord
 from ampel.util.mappings import get_by_json_path
 
 
 class TargetModel(AmpelBaseModel):
 	unit: None | str
 	config: None | int | str
 	code: None | int
 	field: OneOrMany[str]
 
 
-class T3AggregatingStager(AbsT3Stager, T3DocBuilder):
+class T3AggregatingStager(T3SequentialStager):
 	"""
 	Example:
 
 	unit: T3AggregatingStager
 	config:
 	  t2:
 	  - unit: T2NedTap
@@ -94,14 +94,22 @@
 	#: Only applies to doc output
 	split_tiers: bool = False
 
 	t0: None | OneOrMany[TargetModel]
 	t1: None | OneOrMany[TargetModel]
 	t2: None | OneOrMany[TargetModel]
 
+	def __init__(self, **kwargs) -> None:
+
+		super().__init__(**kwargs)
+
+		for i, um in enumerate(self.execute):
+			if um.unit not in self.context.config._config['unit']:
+				raise ValueError(f"Unknown unit: {um.unit}")
+
 
 	def stage(self,
 		gen: Generator[AmpelBuffer, None, None],
 		t3s: T3Store
 	) -> None | Generator[T3Document, None, None]:
 
 		t0 = [self.t0] if isinstance(self.t0, TargetModel) else self.t0
@@ -144,36 +152,60 @@
 											t2d[sid].update(ret[1])
 										else:
 											t2d[sid][ret[0]] = ret[1]
 							else:
 								t2d[sid].update(ret)
 
 		if t0 and not t1 and not t2:
-			return self._craft(t0d, 't0', t3s)
+			t3d = self._craft(t0d, 't0', t3s)
 
-		if t1 and not t0 and not t2:
-			return self._craft(t1d, 't1', t3s)
+		elif t1 and not t0 and not t2:
+			t3d = self._craft(t1d, 't1', t3s)
 
-		if t2 and not t1 and not t0:
-			return self._craft(t2d, 't2', t3s)
+		elif t2 and not t1 and not t0:
+			t3d = self._craft(t2d, 't2', t3s)
 
-		out: dict[str, Any] = {}
+		else:
+			out: dict[str, Any] = {}
+			if t0:
+				self._upd(out, t0d, 't0')
+			if t1:
+				self._upd(out, t1d, 't1')
+			if t2:
+				self._upd(out, t2d, 't2')
+			t3d = self._craft(out, '', t3s)
+
+		yield t3d
+
+		if self.propagate:
+			t3s.add_view(T3DocView.of(t3d, self.context.config))
+
+		for i, t3_unit in enumerate(self.units):
+			ts = time()
+			self.logger.info(f"Processing run block {i}", extra={'unit': t3_unit.__class__.__name__})
+			if (t3_ret := t3_unit.process(self.empty_gen(), t3s)):
+				if (x := self.handle_t3_result(t3_unit, t3_ret, t3s, None, ts)):
+					if self.propagate:
+						t3s.add_view(T3DocView.of(x, self.context.config))
+					yield x
+
+		return None
 
-		if t0:
-			self._upd(out, t0d, 't0')
-		if t1:
-			self._upd(out, t1d, 't1')
-		if t2:
-			self._upd(out, t2d, 't2')
 
-		return self._craft(out, '', t3s)
+	def empty_gen(self):
+		"""
+		yield turns method into generator, preceding it with return
+		terminatesthe generator before yielding anything
+		"""
+		return
+		yield
 
 
-	def _craft(self, d: dict[str, Any], s: str, t3s: T3Store) -> Generator[T3Document, None, None]:
-		yield self.craft_t3_doc(
+	def _craft(self, d: dict[str, Any], s: str, t3s: T3Store) -> T3Document:
+		return self.craft_t3_doc(
 			self, # type: ignore
 			{k: {s: v} for k, v in d.items()} if self.split_tiers else d,
 			t3s,
 			time(),
 			[int(el) for el in d.keys()]
 		)
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3ChannelStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3ChannelStager.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3DistributiveStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3DistributiveStager.py`

 * *Files 6% similar despite different names*

```diff
@@ -26,15 +26,15 @@
 	Example: 2 threads and the buffers ABCD:
 	thread1 receives A, thread2 receives B, thread1 receive C, thread2 receives D
 	This shall allow better performance when used in combination with T3 units that are slowed down
 	by IO based operations (such as network requests to external services).
 	Note that no performance gain will be obtained if the processing is CPU limited.
 	"""
 
-	#: t3 units (AbsT3ReviewUnit) to execute
+	#: t3 units (AbsT3Unit) to execute
 	execute: UnitModel
 	nthread: int = 4
 
 	#: whether to add the thread index into log 'extra' for verbose purposes
 	log_extra: bool = False
 
 
@@ -75,19 +75,24 @@
 				for q in qs:
 					q.put(None) # type: ignore[arg-type]
 
 				for i, (async_res, generator, t3_unit) in enumerate(zip(async_results, generators, self.t3_units)):
 
 					# potential T3Record to be included in the T3Document
 					if (t3_unit_result := async_res.get()):
-						if (d := self.handle_t3_result(t3_unit, t3_unit_result, t3s, generator.stocks, ts)):
+						if (d := self.handle_t3_result(
+							t3_unit, t3_unit_result, t3s, generator.stocks, ts,
+							log_extra={'thread': i} if self.log_extra else None
+						)):
 							if self.save_stock_ids:
 								d['stock'] = generator.stocks
 							yield d
 
-					self.flush(t3_unit, extra={'thread': i} if self.log_extra else None)
+				if self.stock_updr.update_journal:
+					self.stock_updr.flush()
 
 		except Exception as e:
-			self.flush(self.t3_units)
+			if self.stock_updr.update_journal:
+				self.stock_updr.flush()
 			self.event_hdlr.handle_error(e, self.logger)
 
 		return None
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3ProjectingStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3ProjectingStager.py`

 * *Files 4% similar despite different names*

```diff
@@ -8,25 +8,22 @@
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from time import time
 from collections.abc import Generator, Iterable, Sequence
 from itertools import islice
 from multiprocessing import JoinableQueue
 from multiprocessing.pool import ThreadPool
-from typing import Type
 
 from ampel.log import VERBOSE
 from ampel.types import StockId, UBson
-from ampel.t3.T3DocBuilder import AbsT3s
 from ampel.struct.T3Store import T3Store
-from ampel.view.SnapView import SnapView
 from ampel.struct.UnitResult import UnitResult
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.content.T3Document import T3Document
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.abstract.AbsT3Filter import AbsT3Filter
 from ampel.abstract.AbsT3Projector import AbsT3Projector
 from ampel.base.AuxUnitRegister import AuxUnitRegister
 from ampel.t3.stage.T3ThreadedStager import T3ThreadedStager
 from ampel.t3.stage.SimpleViewGenerator import BaseViewGenerator, SimpleViewGenerator
 from ampel.t3.stage.NoViewGenerator import NoViewGenerator
 from ampel.model.t3.T3ProjectionDirective import T3ProjectionDirective
@@ -34,15 +31,15 @@
 
 class RunBlock:
 	"""
 	Used internally by T3UnitRunner
 	"""
 	filter: None | AbsT3Filter
 	projector: None | AbsT3Projector
-	units: list[AbsT3ReviewUnit]
+	units: list[AbsT3Unit]
 	stock_ids: None | list[StockId]
 	qdict: dict[type, list[JoinableQueue]]
 
 	def __init__(self):
 		self.filter = None
 		self.projector = None
 		self.units = []
@@ -79,14 +76,15 @@
 			rb = RunBlock()
 
 			if directive.filter:
 
 				if debug:
 					self.logger.debug(f"Setting up filter {directive.filter.unit}")
 
+				# TODO: provide buffering logger ?
 				rb.filter = self.context.loader.new(
 					model = directive.filter,
 					unit_type = AbsT3Filter,
 					logger = self.logger
 				)
 
 				if self.save_stock_ids:
@@ -94,14 +92,15 @@
 
 
 			if directive.project:
 
 				if debug:
 					self.logger.debug(f"Setting up projector {directive.project.unit}")
 
+				# TODO: provide buffering logger ?
 				rb.projector = AuxUnitRegister.new_unit(
 					model = directive.project,
 					sub_type = AbsT3Projector,
 					logger = self.logger
 				)
 
 			for exec_def in directive.execute:
@@ -257,24 +256,25 @@
 					for async_res, generator, t3_unit in zip(async_results, generators, all_units):
 
 						# potential T3Record to be included in the T3Document
 						if (t3_unit_result := async_res.get()):
 							if (z := self.handle_t3_result(t3_unit, t3_unit_result, t3s, generator.stocks, ts)):
 								yield z
 
-				for i, rb in enumerate(self.run_blocks):
-					self.flush(rb.units, extra={'directive': i})
+				if self.stock_updr.update_journal:
+					self.stock_updr.flush()
 
 		except Exception as e:
-			self.flush(all_units)
+			if self.stock_updr.update_journal:
+				self.stock_updr.flush()
 			self.event_hdlr.handle_error(e, self.logger)
 
 
 	def craft_t3_doc(self,
-		t3_unit: AbsT3s,
+		t3_unit: AbsT3Unit,
 		res: None | UBson | UnitResult,
 		t3s: T3Store,
 		ts: float,
 		stocks: None | list[StockId] = None
 	) -> T3Document:
 
 		t3_doc = super().craft_t3_doc(t3_unit, res, t3s, ts, stocks)
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3SequentialStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3SequentialStager.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,33 +1,34 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/t3/stage/T3SequentialStager.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                22.04.2021
-# Last Modified Date:  25.11.2022
-# Last Modified By:    simeon reusch <simeon.reusch@desy.de>
+# Last Modified Date:  03.04.2023
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from time import time
+from typing import Annotated
 from collections.abc import Generator, Iterable, Sequence
+from ampel.abstract.AbsT3Unit import AbsT3Unit, T
 from ampel.struct.T3Store import T3Store
 from ampel.view.T3DocView import T3DocView
 from ampel.view.SnapView import SnapView
 from ampel.model.UnitModel import UnitModel
 from ampel.content.T3Document import T3Document
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit, T
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.t3.stage.BaseViewGenerator import BaseViewGenerator, T3Send
 from ampel.t3.stage.T3BaseStager import T3BaseStager
 from ampel.mongo.update.MongoStockUpdater import MongoStockUpdater
 
 
 class SimpleGenerator(BaseViewGenerator[T]):
 
-	def __init__(self, unit: AbsT3ReviewUnit, views: Iterable[T], stock_updr: MongoStockUpdater) -> None:
+	def __init__(self, unit: AbsT3Unit, views: Iterable[T], stock_updr: MongoStockUpdater) -> None:
 		super().__init__(unit_name = unit.__class__.__name__, stock_updr = stock_updr)
 		self.views = views
 
 	def __iter__(self) -> Generator[T, T3Send, None]:
 		l = self.stocks
 		for v in self.views:
 			l.append(v.id)
@@ -45,20 +46,23 @@
 	2) Results from upstream t3 units are made available for downstream units
 	through the t3 store instance which is updated after each unit execution
 	unless propagate is set to False
 	"""
 
 	propagate: bool = True
 
-	#: t3 units (AbsT3ReviewUnit) to execute
-	execute: Sequence[UnitModel]
+	#: t3 units to execute
+	execute: Annotated[Sequence[UnitModel], AbsT3Unit]
 
 
 	def __init__(self, **kwargs) -> None:
 
+		if isinstance(kwargs.get('execute'), dict):
+			kwargs['execute'] = [kwargs['execute']]
+
 		super().__init__(**kwargs)
 
 		if self.logger.verbose > 1:
 			self.logger.debug(f"Setting up {self.__class__.__name__}")
 
 		self.units = [
 			self.get_unit(model, self.channel)
@@ -71,25 +75,27 @@
 		t3s: T3Store
 	) -> None | Generator[T3Document, None, None]:
 
 		for t3_unit, views in self.get_views(gen).items():
 
 			sg = SimpleGenerator(t3_unit, views, self.stock_updr)
 			ts = time()
+
 			if (ret := t3_unit.process(sg, t3s)):
 				if (x := self.handle_t3_result(t3_unit, ret, t3s, sg.stocks, ts)):
 					if self.propagate:
 						t3s.add_view(
 							T3DocView.of(x, self.context.config)
 						)
 					yield x
 
 		return None
 
-	def get_views(self, gen: Generator[AmpelBuffer, None, None]) -> dict[AbsT3ReviewUnit, list[SnapView]]:
+
+	def get_views(self, gen: Generator[AmpelBuffer, None, None]) -> dict[AbsT3Unit, list[SnapView]]:
 
 		Views: set[type[SnapView]] = {u._View for u in self.units}
 		conf = self.context.config
 
 		if len(Views) == 1:
 			View = next(iter(Views))
 			if self.paranoia_level:
@@ -108,15 +114,15 @@
 				return {
 					unit: [View.of(ab, conf) for ab in buffers]
 					for unit, View in (lambda x: [(u, u._View) for u in x])(self.units)
 				}
 
 			else:
 
-				optd: dict[type[SnapView], list[AbsT3ReviewUnit]] = {}
+				optd: dict[type[SnapView], list[AbsT3Unit]] = {}
 				for unit in self.units:
 					if unit._View not in optd:
 						optd[unit._View] = []
 					optd[unit._View].append(unit)
 
 				d = {}
 				for View, units in optd.items():
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3SimpleStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3SimpleStager.py`

 * *Files 25% similar despite different names*

```diff
@@ -9,33 +9,33 @@
 
 from collections.abc import Generator
 
 from ampel.types import OneOrMany, Annotated
 from ampel.struct.T3Store import T3Store
 from ampel.model.UnitModel import UnitModel
 from ampel.content.T3Document import T3Document
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.t3.stage.T3ThreadedStager import T3ThreadedStager
 from ampel.t3.stage.SimpleViewGenerator import SimpleViewGenerator
 
 
 class T3SimpleStager(T3ThreadedStager):
 	"""
 	To be used in combination with MongoViews.
 	Otherwise, use T3ProjectingStager.
 	"""
 
-	#: t3 units (AbsT3ReviewUnit) to execute
-	execute: OneOrMany[Annotated[UnitModel, AbsT3ReviewUnit]]
+	#: t3 units (AbsT3Unit) to execute
+	execute: OneOrMany[Annotated[UnitModel, AbsT3Unit]]
 
 	def __init__(self, **kwargs) -> None:
 
 		super().__init__(**kwargs)
-		self.units: list[AbsT3ReviewUnit] = []
+		self.units: list[AbsT3Unit] = []
 
 		if self.logger.verbose > 1:
 			self.logger.debug("Setting up T3SimpleStager")
 
 		for exec_def in [self.execute] if isinstance(self.execute, UnitModel) else self.execute:
 			self.units.append(self.get_unit(exec_def))
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/T3ThreadedStager.py` & `ampel_core-0.9.0/ampel/t3/stage/T3ThreadedStager.py`

 * *Files 3% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 
 from time import time
 from itertools import islice
 from multiprocessing import JoinableQueue
 from multiprocessing.pool import ThreadPool, AsyncResult
 from collections.abc import Generator, Iterable
 
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 from ampel.view.SnapView import SnapView
 from ampel.struct.T3Store import T3Store
 from ampel.content.T3Document import T3Document
 from ampel.struct.AmpelBuffer import AmpelBuffer
 from ampel.t3.stage.T3BaseStager import T3BaseStager
 from ampel.t3.stage.ThreadedViewGenerator import ThreadedViewGenerator
 
@@ -40,15 +40,15 @@
 	Views unit 2:               | F G H I J
 	                 ---------------------->
 	                         time
 	"""
 
 
 	def proceed_threaded(self,
-		t3_units: list[AbsT3ReviewUnit],
+		t3_units: list[AbsT3Unit],
 		buf_gen: Generator[AmpelBuffer, None, None],
 		t3s: T3Store
 	) -> Generator[T3Document, None, None]:
 		"""
 		Execute the method 'process' of t3 units with views crafted using the provided buffer generator and t3 store,
 		handle potential results of t3 unit.
 		Note: code is not optimized for compactness but for execution speed
@@ -96,35 +96,37 @@
 								yield x
 
 				except RuntimeError as e:
 					if "StopIteration" in str(e):
 						return None
 					raise e
 
-			self.flush(t3_units)
+			if self.stock_updr.update_journal:
+				self.stock_updr.flush()
 
 		except Exception as e:
-			self.flush(t3_units)
+			if self.stock_updr.update_journal:
+				self.stock_updr.flush()
 			self.event_hdlr.handle_error(e, self.logger)
 
 
 	def create_threaded_generators(self,
 		pool: ThreadPool,
-		t3_units: list[AbsT3ReviewUnit],
+		t3_units: list[AbsT3Unit],
 		t3s: None | T3Store = None
 	) -> tuple[
-		dict[AbsT3ReviewUnit, "JoinableQueue[SnapView]"],
+		dict[AbsT3Unit, "JoinableQueue[SnapView]"],
 		list[ThreadedViewGenerator],
 		list[AsyncResult]
 	]:
 		"""
 		Create and start T3 units "process(...)" threads (generator will block)
 		"""
 
-		queues: dict[AbsT3ReviewUnit, JoinableQueue[SnapView]] = {}
+		queues: dict[AbsT3Unit, JoinableQueue[SnapView]] = {}
 		generators: list[ThreadedViewGenerator] = []
 		async_results: list[AsyncResult] = []
 
 		for t3_unit in t3_units:
 			queues[t3_unit] = JoinableQueue()
 			generators.append(
 				ThreadedViewGenerator(
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/ThreadedViewGenerator.py` & `ampel_core-0.9.0/ampel/t3/stage/ThreadedViewGenerator.py`

 * *Files 8% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                20.04.2021
 # Last Modified Date:  26.11.2021
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from multiprocessing import JoinableQueue
 from typing import Generator
-from ampel.abstract.AbsT3ReviewUnit import T, T3Send
+from ampel.abstract.AbsT3Unit import T, T3Send
 from ampel.mongo.update.MongoStockUpdater import MongoStockUpdater
 from ampel.t3.stage.BaseViewGenerator import BaseViewGenerator
 
 
 class ThreadedViewGenerator(BaseViewGenerator[T]):
 	"""
 	Does not craft views but loads them from internal JoinableQueue and yields them
```

### Comparing `ampel_core-0.8.6/ampel/t3/stage/filter/T3AmpelBufferFilter.py` & `ampel_core-0.9.0/ampel/t3/stage/filter/T3AmpelBufferFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/stage/project/T3BaseProjector.py` & `ampel_core-0.9.0/ampel/t3/stage/project/T3BaseProjector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/stage/project/T3ChannelProjector.py` & `ampel_core-0.9.0/ampel/t3/stage/project/T3ChannelProjector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/SimpleT2BasedSupplier.py` & `ampel_core-0.9.0/ampel/t3/supply/SimpleT2BasedSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/T3DefaultBufferSupplier.py` & `ampel_core-0.9.0/ampel/t3/supply/T3DefaultBufferSupplier.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/complement/T3ExtJournalAppender.py` & `ampel_core-0.9.0/ampel/t3/supply/complement/T3ExtJournalAppender.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/complement/T3LogsAppender.py` & `ampel_core-0.9.0/ampel/t3/supply/complement/T3LogsAppender.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/complement/T3RandIntAppender.py` & `ampel_core-0.9.0/ampel/t3/supply/complement/T3RandIntAppender.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/load/T3LatestStateDataLoader.py` & `ampel_core-0.9.0/ampel/t3/supply/load/T3LatestStateDataLoader.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/load/T3SimpleDataLoader.py` & `ampel_core-0.9.0/ampel/t3/supply/load/T3SimpleDataLoader.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/select/T3FilteringStockSelector.py` & `ampel_core-0.9.0/ampel/t3/supply/select/T3FilteringStockSelector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/supply/select/T3StockSelector.py` & `ampel_core-0.9.0/ampel/t3/supply/select/T3StockSelector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/t3/unit/T3LogAggregatedStocks.py` & `ampel_core-0.9.0/ampel/t3/unit/T3LogAggregatedStocks.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File:                Ampel-core/ampel/t3/unit/T3LogAggregatedStocks.py
 # License:             BSD-3-Clause
 # Author:              valery brinnel <firstname.lastname@gmail.com>
 # Date:                14.05.2022
-# Last Modified Date:  17.07.2022
+# Last Modified Date:  03.04.2023
 # Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
+from typing import Any
 from ampel.struct.T3Store import T3Store
-from ampel.abstract.AbsT3PlainUnit import AbsT3PlainUnit
+from ampel.abstract.AbsT3Unit import AbsT3Unit
 
 
-class T3LogAggregatedStocks(AbsT3PlainUnit):
+class T3LogAggregatedStocks(AbsT3Unit):
 
 	input_unit: str = "T3AggregatingStager"
 
-	def process(self, t3s: None | T3Store = None):
+	def process(self, gen: Any, t3s: T3Store):
 
 		self.logger.info(f"Running {self.__class__.__name__}")
 
 		if not t3s:
 			raise ValueError("A T3 store is required, please check your config")
 
 		self.logger.info(
```

### Comparing `ampel_core-0.8.6/ampel/template/ChannelWithProcsTemplate.py` & `ampel_core-0.9.0/ampel/template/ChannelWithProcsTemplate.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/template/PeriodicSummaryT3.py` & `ampel_core-0.9.0/ampel/template/PeriodicSummaryT3.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,40 +1,41 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # File              : Ampel-core/ampel/template/PeriodicSummaryT3.py
 # License           : BSD-3-Clause
 # Author            : Jakob van Santen <jakob.van.santen@desy.de>
 # Date              : 10.08.2020
-# Last Modified Date: 14.12.2021
+# Last Modified Date: 04.04.2023
 # Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
 
 from typing import Any, Literal
 from collections.abc import Sequence
 
 from ampel.types import OneOrMany, ChannelId, Tag
 from ampel.model.operator.AllOf import AllOf
 from ampel.model.operator.AnyOf import AnyOf
 from ampel.model.operator.OneOf import OneOf
-from ampel.base.AmpelBaseModel import AmpelBaseModel
 from ampel.model.t3.LoaderDirective import LoaderDirective
 from ampel.model.t3.T2FilterModel import T2FilterModel
 from ampel.model.UnitModel import UnitModel
+from ampel.model.ProcessModel import ProcessModel
+from ampel.base.AmpelBaseModel import AmpelBaseModel
 from ampel.log.AmpelLogger import AmpelLogger
-from ampel.abstract.AbsProcessTemplate import AbsProcessTemplate
+from ampel.abstract.AbsConfigMorpher import AbsConfigMorpher
 
 
 class FilterModel(AmpelBaseModel):
     #: Filter based on T2 results
     t2: T2FilterModel | AllOf[T2FilterModel] | AnyOf[T2FilterModel]
 
 
-class PeriodicSummaryT3(AbsProcessTemplate):
+class PeriodicSummaryT3(AbsConfigMorpher):
     """
     A T3 process that selects stocks updated since its last invocation, and
-    supplies them, to a sequence of AbsT3ReviewUnits.
+    supplies them, to a sequence of AbsT3Units.
     """
 
     #: Process name.
     name: str
 
     tier: Literal[3] = 3
 
@@ -65,88 +66,82 @@
 
     #: Complement stages. See :ref:`t3-directive-complement`.
     complement: None | OneOrMany[str | UnitModel] = None
 
     #: Units to run. See :ref:`t3-directive-run-execute`.
     run: OneOrMany[str | UnitModel]
 
-    def get_process(self, config: dict[str, Any], logger: AmpelLogger) -> dict[str, Any]:
+
+    def morph(self, ampel_config: dict[str, Any], logger: AmpelLogger) -> dict[str, Any]:
 
         d: dict[str, Any] = {
             "include": {
                 "session": [
                     {"unit": "T3SessionAlertsNumber"}
                 ]
             },
-            "execute": [
-                {
-                    "unit": "T3ReviewUnitExecutor",
-                    "config": {
-                        "supply": {
-                            "unit": "T3DefaultBufferSupplier",
-                            "config": {
-                                "select": {
-                                    "unit": "T3StockSelector",
-                                    "config": {
-                                        "updated": {
-                                            "after": {
-                                                "match_type": "time_last_run",
-                                                "process_name": self.name,
-                                            },
-                                            "before": {"match_type": "time_delta"},
-                                        },
-                                        "channel": self.channel,
-                                        "tag": self.tag,
-                                    },
+            "supply": {
+                "unit": "T3DefaultBufferSupplier",
+                "config": {
+                    "select": {
+                        "unit": "T3StockSelector",
+                        "config": {
+                            "updated": {
+                                "after": {
+                                    "match_type": "time_last_run",
+                                    "process_name": self.name,
                                 },
-                                "load": {
-                                    "unit": "T3SimpleDataLoader",
-                                    "config": {
-                                        "directives": [{"col": col} for col in ("stock", "t0", "t1", "t2")]
-                                    }
-                                },
-                            }
+                                "before": {"match_type": "time_delta"},
+                            },
+                            "channel": self.channel,
+                            "tag": self.tag,
                         },
-                        "stage": {
-                            "unit": "T3ProjectingStager",
-                            "config": {
-                                "directives": [
-                                    {
-                                        "project": {
-                                            "unit": "T3ChannelProjector",
-                                            "config": {"channel": self.channel}
-                                        },
-                                        "execute": self.get_units(self.run),
-                                    }
-                                ]
-                            }
+                    },
+                    "load": {
+                        "unit": "T3SimpleDataLoader",
+                        "config": {
+                            "directives": [{"col": col} for col in ("stock", "t0", "t1", "t2")]
                         }
                     }
                 }
-            ]
+            },
+            "stage": {
+                "unit": "T3ProjectingStager",
+                "config": {
+                    "directives": [
+                        {
+                            "project": {
+                                "unit": "T3ChannelProjector",
+                                "config": {"channel": self.channel}
+                            },
+                            "execute": self.get_units(self.run),
+                        }
+                    ]
+                }
+            }
         }
 
         # Restrict stock selection according to T2 values
         if self.filter:
-            d["execute"][0]["config"]["supply"]["config"]["select"]["unit"] = "T3FilteringStockSelector"
-            d["execute"][0]["config"]["supply"]["config"]["select"]["config"]["t2_filter"] = self.filter.t2.dict()
+            d["supply"]["config"]["select"]["unit"] = "T3FilteringStockSelector"
+            d["supply"]["config"]["select"]["config"]["t2_filter"] = self.filter.t2.dict()
 
         if self.channel is None:
-            d["execute"][0]["config"]["stage"]["unit"] = "T3SimpleStager"
-            del d["execute"][0]["config"]["stage"]["config"]["channel"]
+            d["stage"]["unit"] = "T3SimpleStager"
+            del d["stage"]["config"]["channel"]
         else:
             # load only documents that pass channel selection
-            d["execute"][0]["config"]["supply"]["config"]["load"]["config"]["channel"] = self.channel
+            d["supply"]["config"]["load"]["config"]["channel"] = self.channel
    
         # Restrict document types to load
         if self.load:
-            d["execute"][0]["config"]["supply"]["config"]["load"]["config"]["directives"] = self.load
+            d["supply"]["config"]["load"]["config"]["directives"] = self.load
 
         if self.complement:
-            d["execute"][0]["config"]["supply"]["config"]["complement"] = self.get_units(self.complement)
+            d["supply"]["config"]["complement"] = self.get_units(self.complement)
 
         ret: dict[str, Any] = {
             "tier": self.tier,
             "schedule": self.schedule,
             "active": self.active,
             "distrib": self.distrib,
             "source": self.source,
@@ -154,40 +149,31 @@
             "name": self.name,
             "processor": {
                 "unit": "T3Processor",
                 "config": d,
             }
         }
 
-        return self._to_dict(ret)
-
+        return ProcessModel(**ret).dict()
 
-    @classmethod
-    def _to_dict(cls, item):
-        # TODO: use dictify from ampel.util.mappings ?
-        if isinstance(item, dict):
-            return {k: cls._to_dict(v) for k, v in item.items()}
-        elif isinstance(item, list):
-            return [cls._to_dict(v) for v in item]
-        elif hasattr(item, "dict"):
-            return cls._to_dict(item.dict())
-        return item
 
     def get_units(self, units: OneOrMany[str | UnitModel]) -> list[dict[str, Any]]:
         if isinstance(units, str):
             return [UnitModel(unit=units).dict()]
         elif isinstance(units, UnitModel):
             return [units.dict()]
         return [self.get_units(u)[0] for u in units]
 
+
     def get_schedule(self) -> Sequence[str]:
         if isinstance(self.schedule, str):
             return [self.schedule]
         return self.schedule
 
+
     def get_channel_tag(self) -> None | str | int:
         """
         Get channel if single channel, otherwise None
         """
         if isinstance(self.channel, str) or isinstance(self.channel, int):
             return self.channel
         return None
```

### Comparing `ampel_core-0.8.6/ampel/test/conftest.py` & `ampel_core-0.9.0/ampel/test/conftest.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,27 +1,24 @@
-from ampel.content.JournalRecord import JournalRecord
-import mongomock, pytest
-import pymongo
+import mongomock, pytest, pymongo, subprocess, json, datetime
 from os import environ
 from pathlib import Path, PosixPath
 from typing import Any
-import subprocess
-import json
-import datetime
 
 from ampel.config.builder.DistConfigBuilder import DistConfigBuilder
 from ampel.config.builder.DisplayOptions import DisplayOptions
 from ampel.mongo.update.DBUpdatesBuffer import DBUpdatesBuffer
 from ampel.dev.DevAmpelContext import DevAmpelContext
+from ampel.content.JournalRecord import JournalRecord
 
 from ampel.mongo.update.MongoStockIngester import MongoStockIngester
 from ampel.mongo.update.MongoT2Ingester import MongoT2Ingester
 from ampel.ingest.T2Compiler import T2Compiler
 from ampel.ingest.StockCompiler import StockCompiler
 from ampel.log.AmpelLogger import AmpelLogger
+from ampel.util.config import get_unit_confid
 
 from ampel.model.ingest.T1Combine import T1Combine
 from ampel.model.ingest.T2Compute import T2Compute
 from ampel.model.ingest.IngestBody import IngestBody
 from ampel.model.UnitModel import UnitModel
 from ampel.model.ingest.CompilerOptions import CompilerOptions
 from ampel.model.ingest.IngestDirective import IngestDirective
@@ -174,31 +171,26 @@
         DummyPointT2Unit,
         DummyStateT2Unit,
         DummyTiedStateT2Unit,
     ):
         integration_context.register_unit(unit)
 
     dependency = request.param
-    tied_config_id = integration_context.gen_config_id(
-        unit="DummyTiedStateT2Unit",
-        arg={"t2_dependency": [{"unit": dependency}]},
-        logger=ampel_logger,
-    )
-
+    unit_conf = {"t2_dependency": [{"unit": dependency}]}
+    tied_config_id = get_unit_confid(integration_context.loader, unit="DummyTiedStateT2Unit", config=unit_conf)
+    integration_context.add_conf_id(tied_config_id, unit_conf)
     run_id = 0
     channel = "TEST_CHANNEL"
     #now = datetime.datetime.now()
     updates_buffer = DBUpdatesBuffer(integration_context.db, run_id=run_id, logger=ampel_logger)
 
     if "stock" in dependency.lower():
         body = IngestBody(
             stock_t2=[T2Compute(unit=dependency)],
-            combine=[
-                T1Combine(unit="T1SimpleCombiner", state_t2=[T2Compute(unit="DummyTiedStateT2Unit", config=tied_config_id)])  # type: ignore[arg-type]
-            ],
+            combine=[T1Combine(unit="T1SimpleCombiner", state_t2 = [T2Compute(unit="DummyTiedStateT2Unit", config=tied_config_id)])], # type: ignore[arg-type]
         )
     elif "point" in dependency.lower():
         body = IngestBody(
             point_t2=[T2Compute(unit=dependency)],
             combine=[
                 T1Combine(unit="T1SimpleCombiner", state_t2=[T2Compute(unit="DummyTiedStateT2Unit", config=tied_config_id)])  # type: ignore[arg-type]
             ],
```

### Comparing `ampel_core-0.8.6/ampel/test/dummy.py` & `ampel_core-0.9.0/ampel/test/dummy.py`

 * *Files 6% similar despite different names*

```diff
@@ -7,18 +7,17 @@
 # Last Modified Date:  11.02.2021
 # Last Modified By:    jvs
 
 import pathlib
 import time
 from collections.abc import Sequence
 from typing import Any
-from ampel.abstract.AbsProcessorTemplate import AbsProcessorTemplate
+from ampel.abstract.AbsConfigMorpher import AbsConfigMorpher
 from ampel.core.EventHandler import EventHandler
 from ampel.log.AmpelLogger import AmpelLogger
-from ampel.model.UnitModel import UnitModel
 
 from ampel.struct.UnitResult import UnitResult
 from ampel.types import StockId, UBson
 from ampel.abstract.AbsEventUnit import AbsEventUnit
 from ampel.abstract.AbsStockT2Unit import AbsStockT2Unit
 from ampel.abstract.AbsPointT2Unit import AbsPointT2Unit
 from ampel.abstract.AbsStateT2Unit import AbsStateT2Unit
@@ -129,14 +128,14 @@
     value: str
     expected_value: str
 
     def proceed(self, event_hdlr: EventHandler) -> Any:
         assert self.value == self.expected_value
 
 
-class DummyProcessorTemplate(AbsProcessorTemplate):
+class DummyProcessorTemplate(AbsConfigMorpher):
 
     value: str
     expected_value: str
 
-    def get_model(self, config: dict[str, Any], logger: AmpelLogger) -> UnitModel:
-        return UnitModel(unit="DummyInputUnit", config=self.dict(exclude={'template'}))
+    def morph(self, config: dict[str, Any], logger: AmpelLogger) -> dict[str, Any]:
+        return {'unit': "DummyInputUnit", 'config': self.dict(exclude={'template'})}
```

### Comparing `ampel_core-0.8.6/ampel/test/pylintrc` & `ampel_core-0.9.0/ampel/test/pylintrc`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test-data/ZTF20abxvcrk.pkl` & `ampel_core-0.9.0/ampel/test/test-data/ZTF20abxvcrk.pkl`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test-data/testing-config.yaml` & `ampel_core-0.9.0/ampel/test/test-data/testing-config.yaml`

 * *Files 2% similar despite different names*

```diff
@@ -226,30 +226,14 @@
     base:
     - T3Processor
     - AbsEventUnit
     - ContextUnit
     distrib: ampel-core
     file: /Users/jakob/Documents/ZTF/Ampel-v0.8/Ampel-core/conf/ampel-core/ampel.yaml
     version: 0.8.0a1
-  T3ReviewUnitExecutor:
-    fqn: ampel.t3.T3ReviewUnitExecutor
-    base:
-    - AbsT3ControlUnit
-    - ContextUnit
-    distrib: ampel-core
-    file: Ampel-core/conf/ampel-core/ampel.yaml
-    version: 0.8.25
-  T3PlainUnitExecutor:
-    fqn: ampel.t3.T3PlainUnitExecutor
-    base:
-    - AbsT3ControlUnit
-    - ContextUnit
-    distrib: ampel-core
-    file: Ampel-core/conf/ampel-core/ampel.yaml
-    version: 0.8.25
   AmpelExceptionPublisher:
     fqn: ampel.ops.AmpelExceptionPublisher
     base:
     - AmpelExceptionPublisher
     - AbsOpsUnit
     - ContextUnit
     distrib: ampel-core
@@ -448,18 +432,18 @@
     base:
     - DemoPointT2Unit
     - AbsPointT2Unit
     - LogicalUnit
     distrib: ampel-core
     file: /Users/jakob/Documents/ZTF/Ampel-v0.8/Ampel-core/conf/ampel-core/ampel.yaml
     version: 0.8.0a1
-  DemoReviewT3Unit:
-    fqn: ampel.demo.DemoReviewT3Unit
+  DemoT3Unit:
+    fqn: ampel.demo.DemoT3Unit
     base:
-    - AbsT3ReviewUnit
+    - AbsT3Unit
     - LogicalUnit
     distrib: ampel-core
     file: /Users/jakob/Documents/ZTF/Ampel-v0.8/Ampel-core/conf/ampel-core/ampel.yaml
     version: 0.8.0a1
   NoShaper:
     fqn: ampel.dev.NoShaper
     base:
@@ -615,20 +599,20 @@
     base:
       - AbsEventUnit
   DummyOutputUnit:
     fqn: ampel.test.dummy
     version: 0.8.0a1
     base:
       - AbsEventUnit
-  DemoReviewT3Unit:
-    fqn: ampel.demo.DemoReviewT3Unit
+  DemoT3Unit:
+    fqn: ampel.demo.DemoT3Unit
     version: 0.8.2a2
     base:
-    - DemoReviewT3Unit
-    - AbsT3ReviewUnit
+    - DemoT3Unit
+    - AbsT3Unit
     - LogicalUnit
     distrib: ampel-core
     file: /Users/jakob/Documents/ZTF/Ampel-v0.8/Ampel-core/conf/ampel-cor
 process:
   t0: {}
   t1: {}
   t2: {}
```

### Comparing `ampel_core-0.8.6/ampel/test/test_AbsChannelTemplate.py` & `ampel_core-0.9.0/ampel/test/test_AbsChannelTemplate.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_AmpelContext.py` & `ampel_core-0.9.0/ampel/test/test_AmpelContext.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,40 +1,44 @@
 import copy
 
 from ampel.config.AmpelConfig import AmpelConfig
 from ampel.dev.DevAmpelContext import DevAmpelContext
-from ampel.test.dummy import DummyStateT2Unit
-
+from ampel.test.DummyStateT2Unit import DummyStateT2Unit
+from ampel.config.alter.HashT2Config import HashT2Config
 
 def test_load_old_configids(mock_context: DevAmpelContext, ampel_logger):
-    """
-    Configuration hashes stored via hash_ingest_directive are loaded from the
-    database when a new DevAmpelContext is instantiated
-    """
+    """ This test unit might no longer be required or might need a rename """
     unit_config = {"foo": 37}
     mock_context.register_unit(DummyStateT2Unit)
     pre_register_context = DevAmpelContext(
         config=AmpelConfig(copy.deepcopy(mock_context.config.get())),
         db=mock_context.db,
         loader=mock_context.loader,
     )
-    mock_context.hash_ingest_directive(
+
+    HashT2Config().alter(
+        mock_context,
         dict(
-            channel="TEST",
-            ingest=dict(
-                combine=[
-                    dict(
-                        unit="T1SimpleCombiner",
-                        state_t2=[dict(unit="DummyStateT2Unit", config=unit_config)],
+            directives=[
+                dict(
+                    channel="TEST",
+                    ingest=dict(
+                        combine=[
+                            dict(
+                                unit="T1SimpleCombiner",
+                                state_t2=[dict(unit="DummyStateT2Unit", config=unit_config)],
+                            )
+                        ]
                     )
-                ]
-            ),
+                )
+            ]
         ),
-        ampel_logger,
+        ampel_logger
     )
+
     post_register_context = DevAmpelContext(
         config=AmpelConfig(copy.deepcopy(pre_register_context.config.get())),
         db=mock_context.db,
         loader=mock_context.loader,
     )
     assert (
         isinstance(
```

### Comparing `ampel_core-0.8.6/ampel/test/test_DBUpdatesBuffer.py` & `ampel_core-0.9.0/ampel/test/test_DBUpdatesBuffer.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_DefaultProcessController.py` & `ampel_core-0.9.0/ampel/test/test_DefaultProcessController.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_IngestionHandler.py` & `ampel_core-0.9.0/ampel/test/test_IngestionHandler.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_PeriodicSummaryT3.py` & `ampel_core-0.9.0/ampel/test/test_PeriodicSummaryT3.py`

 * *Files 7% similar despite different names*

```diff
@@ -12,32 +12,32 @@
     config["process"]["t3"]["foo"] = (
         PeriodicSummaryT3(
             **{
                 "name": "foo",
                 "schedule": "every().day.at('15:00')",
                 "channel": "FOO",
                 "load": loader_directives,
-                "run": {"unit": "DemoReviewT3Unit"},
+                "run": {"unit": "DemoT3Unit"},
             }
         )
-        .get_process(config, ampel_logger) | {"version": 0}
+        .morph(core_config, ampel_logger) | {"version": 0}
     )
     # from ampel.core.EventHandler import EventHandler
     # eh = EventHandler("foo", ampel_db=None, tier=3, dry_run=True)
     assert ConfigValidator(config).validate() == config
 
 def test_single_element_run_sequence(core_config, ampel_logger):
     config = copy.deepcopy(core_config)
     config["process"]["t3"]["foo"] = (
         PeriodicSummaryT3(
             **{
                 "name": "foo",
                 "schedule": "every().day.at('15:00')",
                 "channel": {"any_of": ["HU_GP_10", "HU_GP_59"]},
                 "load": ["TRANSIENT", "DATAPOINT", "T2RECORD"],
-                "run": [{"unit": "DemoReviewT3Unit", "config": {}}],
+                "run": [{"unit": "DemoT3Unit", "config": {}}],
             }
         )
-        .get_process(config, ampel_logger) | {"version": 0}
+        .morph(config, ampel_logger) | {"version": 0}
     )
     assert ConfigValidator(config).validate() == config
     assert config["process"]["t3"]["foo"]["channel"] is None
```

### Comparing `ampel_core-0.8.6/ampel/test/test_ProcessMorpher.py` & `ampel_core-0.9.0/ampel/test/test_ProcessMorpher.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_SimpleTagFilter.py` & `ampel_core-0.9.0/ampel/test/test_SimpleTagFilter.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_T2Processor.py` & `ampel_core-0.9.0/ampel/test/test_T2Processor.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_T3ChannelProjector.py` & `ampel_core-0.9.0/ampel/test/test_T3ChannelProjector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_T3FilteringStockSelector.py` & `ampel_core-0.9.0/ampel/test/test_T3FilteringStockSelector.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_T3Processor.py` & `ampel_core-0.9.0/ampel/test/test_T3Processor.py`

 * *Files 12% similar despite different names*

```diff
@@ -18,55 +18,49 @@
 from ampel.enum.DocumentCode import DocumentCode
 from ampel.struct.JournalAttributes import JournalAttributes
 from ampel.struct.StockAttributes import StockAttributes
 from ampel.enum.EventCode import EventCode
 from ampel.view.SnapView import SnapView
 from ampel.struct.T3Store import T3Store
 from ampel.test.dummy import DummyStateT2Unit
+from ampel.util.config import get_unit_confid
 
-from ampel.abstract.AbsT3ReviewUnit import AbsT3ReviewUnit, T3Send
+from ampel.abstract.AbsT3Unit import AbsT3Unit, T3Send
 from ampel.t3.T3Processor import T3Processor
 
 
-class Mutineer(AbsT3ReviewUnit):
+class Mutineer(AbsT3Unit):
     raise_on_process: bool = False
 
     def process(self, views, t3s=None):
         if self.raise_on_process:
             raise ValueError
 
 
 def mutineer_process(config={}):
 
     return {
-        "execute": [
-            {
-                "unit": "T3ReviewUnitExecutor",
-                "config": {
-                    "supply": {
-                        "unit": "T3DefaultBufferSupplier",
-                        "config": {
-                            "select": {"unit": "T3StockSelector"},
-                            "load": {
-                                "unit": "T3SimpleDataLoader",
-                                "config": {
-                                    "directives": [{"col": "stock"}]
-                                }
-                            }
-                        }
-                    },
-                    "stage": {
-                        "unit": "T3SimpleStager",
-                        "config": {
-                            "execute": [{"unit": "Mutineer", "config": config}]
-                        }
+        "supply": {
+            "unit": "T3DefaultBufferSupplier",
+            "config": {
+                "select": {"unit": "T3StockSelector"},
+                "load": {
+                    "unit": "T3SimpleDataLoader",
+                    "config": {
+                        "directives": [{"col": "stock"}]
                     }
                 }
             }
-        ]
+        },
+        "stage": {
+            "unit": "T3SimpleStager",
+            "config": {
+                "execute": [{"unit": "Mutineer", "config": config}]
+            }
+        }
     }
 
 
 @pytest.mark.parametrize(
     "config,expect_success",
     [
         ({}, True),
@@ -85,15 +79,15 @@
     assert event
     assert event["run"] == 1
     assert event["code"] == EventCode.OK.value if expect_success else EventCode.EXCEPTION
 
 
 def test_view_generator(integration_context: DevAmpelContext, ingest_stock):
 
-    class SendySend(AbsT3ReviewUnit):
+    class SendySend(AbsT3Unit):
         raise_on_process: bool = False
 
         def process(self, gen: Generator[SnapView, T3Send, None], t3s: None | T3Store = None):
             for view in gen:
                 gen.send(
                     (
                         view.id,
@@ -107,164 +101,140 @@
 
     integration_context.register_unit(SendySend)
 
     t3 = T3Processor(
         context=integration_context,
         raise_exc=True,
         process_name="t3",
-        execute = [
-            {
-                "unit": "T3ReviewUnitExecutor",
-                "config": {
-                    "supply": {
-                        "unit": "T3DefaultBufferSupplier",
-                        "config": {
-                            "select": {"unit": "T3StockSelector"},
-                            "load": {
-                                "unit": "T3SimpleDataLoader",
-                                "config": {
-                                    "directives": [{"col": "stock"}]
-                                }
-                            }
-                        }
-                    },
-                    "stage": {
-                        "unit": "T3SimpleStager",
-                        "config": {
-                            "execute": [{"unit": "SendySend"}]
-                        }
+        supply = {
+            "unit": "T3DefaultBufferSupplier",
+            "config": {
+                "select": {"unit": "T3StockSelector"},
+                "load": {
+                    "unit": "T3SimpleDataLoader",
+                    "config": {
+                        "directives": [{"col": "stock"}]
                     }
                 }
             }
-        ]
+        },
+        stage = {
+            "unit": "T3SimpleStager",
+            "config": {
+                "execute": [{"unit": "SendySend"}]
+            }
+        }
     )
     t3.run()
 
     stock = integration_context.db.get_collection("stock").find_one()
     assert stock
     assert "TAGGYTAG" in stock["tag"]
     assert "floopsy" in stock["name"]
     assert len(entries := [jentry for jentry in stock["journal"] if jentry["tier"] == 3]) == 1
     jentry = entries[0]
     assert jentry["extra"] == {"foo": "bar"}
 
 def test_empty_generator(integration_context: DevAmpelContext, ingest_stock):
     """
     Empty selection returns cleanly, rather than raising
-    """ 
+    """
     t3 = T3Processor(
         context=integration_context,
         raise_exc=True,
         process_name="t3",
-        execute = [
-            {
-                "unit": "T3ReviewUnitExecutor",
-                "config": {
-                    "supply": {
-                        "unit": "T3DefaultBufferSupplier",
-                        "config": {
-                            "select": {
-                                "unit": "T3StockSelector",
-                                # ensure that no stocks will be selected
-                                "config": {"channel": "nonesuch"}
-                            },
-                            "load": {
-                                "unit": "T3SimpleDataLoader",
-                                "config": {
-                                    "directives": [{"col": "stock"}],
-                                }
-                            }
-                        }
-                    },
-                    "stage": {
-                        "unit": "T3SimpleStager",
-                        "config": {
-                            "execute": [{"unit": "DemoReviewT3Unit"}]
-                        }
+        supply = {
+            "unit": "T3DefaultBufferSupplier",
+            "config": {
+                "select": {
+                    "unit": "T3StockSelector",
+                    # ensure that no stocks will be selected
+                    "config": {"channel": "nonesuch"}
+                },
+                "load": {
+                    "unit": "T3SimpleDataLoader",
+                    "config": {
+                        "directives": [{"col": "stock"}],
                     }
                 }
             }
-        ]
+        },
+        stage = {
+            "unit": "T3SimpleStager",
+            "config": {
+                "execute": [{"unit": "DemoT3Unit"}]
+            }
+        }
     )
     t3.run()
 
 
-class ViewExaminer(AbsT3ReviewUnit):
+class ViewExaminer(AbsT3Unit):
     class DidAThing(Exception):
         ...
 
     expected_config: dict[str, Any]
 
     def process(self, views, t3s=None):
         for view in views:
             for t2 in view.t2:
                 assert t2.config == self.expected_config
                 raise self.DidAThing
 
 
 @pytest.mark.parametrize("num_units", [1, 2])
 def test_t2_config_resolution(mock_context: DevAmpelContext, num_units: int):
-    """
-    T3 stagers pass through resolved config ids
-    """
+    """ T3 stagers pass through resolved config ids """
+
     for unit in (ViewExaminer, DummyStateT2Unit):
         mock_context.register_unit(unit)
 
     expected_config = {"foo": 42}
-    config_id = mock_context.gen_config_id("DummyStateT2Unit", expected_config)
-
-    stock: StockDocument = {
-        "stock": 0,
-    }
+    stock: StockDocument = {"stock": 0}
+    confid = get_unit_confid(mock_context.loader, "DummyStateT2Unit", expected_config)
+    mock_context.add_conf_id(confid, expected_config)
     t2: T2Document = {
         "unit": "DummyStateT2Unit",
-        "config": config_id,
+        "config": confid,
         "stock": 0,
         "link": 0,
         "channel": "TEST",
         "meta": [],
         "body": [],
         "code": DocumentCode.OK,
     }
     mock_context.db.get_collection("stock").insert_one(dict(stock))
     mock_context.db.get_collection("t2").insert_one(dict(t2))
 
     t3 = T3Processor(
         context=mock_context,
         raise_exc=True,
         process_name="t3",
-        execute=[
-            {
-                "unit": "T3ReviewUnitExecutor",
-                "config": {
-                    "supply": {
-                        "unit": "T3DefaultBufferSupplier",
-                        "config": {
-                            "select": {
-                                "unit": "T3StockSelector",
-                            },
-                            "load": {
-                                "unit": "T3SimpleDataLoader",
-                                "config": {
-                                    "directives": [{"col": "t2"}],
-                                },
-                            },
-                        },
-                    },
-                    "stage": {
-                        "unit": "T3SimpleStager",
-                        "config": {
-                            "execute": [
-                                {
-                                    "unit": "ViewExaminer",
-                                    "config": {"expected_config": expected_config},
-                                }
-                            ]
-                            * num_units
-                        },
-                    },
+        supply = {
+            "unit": "T3DefaultBufferSupplier",
+            "config": {
+                "select": {
+                    "unit": "T3StockSelector",
                 },
+                "load": {
+                    "unit": "T3SimpleDataLoader",
+                    "config": {
+                        "directives": [{"col": "t2"}],
+                    }
+                }
+            }
+        },
+        stage = {
+            "unit": "T3SimpleStager",
+            "config": {
+                "execute": [
+                    {
+                        "unit": "ViewExaminer",
+                        "config": {"expected_config": expected_config},
+                    }
+                ]
+                * num_units
             }
-        ],
+        }
     )
     with pytest.raises(ViewExaminer.DidAThing):
         t3.run()
```

### Comparing `ampel_core-0.8.6/ampel/test/test_T3SimpleDataLoader.py` & `ampel_core-0.9.0/ampel/test/test_T3SimpleDataLoader.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_UnitLoader.py` & `ampel_core-0.9.0/ampel/test/test_UnitLoader.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from typing import Any, Optional
+from typing import Optional
 from ampel.base.LogicalUnit import LogicalUnit
 from ampel.model.ingest.CompilerOptions import CompilerOptions
 from ampel.secret.NamedSecret import NamedSecret
 from ampel.dev.DevAmpelContext import DevAmpelContext
 import pytest
 
 from ampel.secret.Secret import Secret
@@ -166,45 +166,36 @@
         UnitModel(unit="Dummy")
         UnitModel(unit="Dummy", config={"param": 37})
         with pytest.raises(TypeError):
             UnitModel(unit="Dummy", config={"param": "fish"})
         with pytest.raises(TypeError):
             UnitModel(unit="Dummy", config={"nonexistant_param": True})
 
-        t3_config: dict[str, Any] = {
-            "execute": [
-                {
-                    "unit": "T3ReviewUnitExecutor",
-                    "config": {
-                        "supply": {
-                            "unit": "T3DefaultBufferSupplier",
-                            "config": {
-                                "select": {"unit": "T3StockSelector"},
-                                "load": {
-                                    "unit": "T3SimpleDataLoader",
-                                    "config": {"directives": [{"col": "stock"}]},
-                                },
-                            },
-                        },
-                        "stage": {
-                            "unit": "T3SimpleStager",
-                            "config": {"execute": [{"unit": "DemoReviewT3Unit"}]},
-                        },
+        t3_config = dict(
+            supply = {
+                "unit": "T3DefaultBufferSupplier",
+                "config": {
+                    "select": {"unit": "T3StockSelector"},
+                    "load": {
+                        "unit": "T3SimpleDataLoader",
+                        "config": {"directives": [{"col": "stock"}]},
                     },
-                }
-            ],
-        }
+                },
+            },
+            stage = {
+                "unit": "T3SimpleStager",
+                "config": {"execute": [{"unit": "DemoT3Unit"}]},
+            }
+        )
 
         # recursive validation
         UnitModel(unit="T3Processor", config=t3_config)
 
         with pytest.raises(TypeError):
-            t3_config["execute"][0]["config"]["supply"]["config"]["select"][
-                "unit"
-            ] = "NotActuallyAUnit"
+            t3_config["supply"]["config"]["select"]["unit"] = "NotActuallyAUnit" # type: ignore
             UnitModel(unit="T3Processor", config=t3_config)
 
 
 def test_compiler_options_validation(mock_context: DevAmpelContext):
     """AuxAliasableUnit can be intialized from a string"""
 
     class Dummy(LogicalUnit):
```

### Comparing `ampel_core-0.8.6/ampel/test/test_concurrent.py` & `ampel_core-0.9.0/ampel/test/test_concurrent.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_config.py` & `ampel_core-0.9.0/ampel/test/test_config.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_server.py` & `ampel_core-0.9.0/ampel/test/test_server.py`

 * *Files 2% similar despite different names*

```diff
@@ -46,21 +46,21 @@
 
 @pytest.mark.asyncio
 async def test_get_config(dev_context: AmpelContext, test_client: AsyncClient):
     response = await test_client.get("/config/")
     assert response.status_code == 200
     assert response.json() == json.loads(json.dumps(dev_context.config.get()))
 
-    response = await test_client.get("/config/unit/DemoReviewT3Unit/")
+    response = await test_client.get("/config/unit/DemoT3Unit/")
     assert response.status_code == 200
     assert response.json() == json.loads(
-        json.dumps(dev_context.config.get(["unit", "DemoReviewT3Unit"]))
+        json.dumps(dev_context.config.get(["unit", "DemoT3Unit"]))
     )
 
-    response = await test_client.get("/config/unit/DemoReviewT3Unit/0")
+    response = await test_client.get("/config/unit/DemoT3Unit/0")
     assert response.status_code == 404
 
 
 @pytest.fixture
 def db_collector(dev_context):
     c = AmpelDBCollector(dev_context.db)
     AmpelMetricsRegistry.register_collector(c)
```

### Comparing `ampel_core-0.8.6/ampel/test/test_util_mappings.py` & `ampel_core-0.9.0/ampel/test/test_util_mappings.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/test/test_util_template.py` & `ampel_core-0.9.0/ampel/test/test_util_template.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/collections.py` & `ampel_core-0.9.0/ampel/util/collections.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/concurrent.py` & `ampel_core-0.9.0/ampel/util/concurrent.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/debug.py` & `ampel_core-0.9.0/ampel/util/debug.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/distrib.py` & `ampel_core-0.9.0/ampel/util/distrib.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/getch.py` & `ampel_core-0.9.0/ampel/util/getch.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/logicschema.py` & `ampel_core-0.9.0/ampel/util/logicschema.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/pretty.py` & `ampel_core-0.9.0/ampel/util/pretty.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/register.py` & `ampel_core-0.9.0/ampel/util/register.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/util/stock.py` & `ampel_core-0.9.0/ampel/util/stock.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/vendor/aiopipe/LICENSE.txt` & `ampel_core-0.9.0/ampel/vendor/aiopipe/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/ampel/vendor/aiopipe/__init__.py` & `ampel_core-0.9.0/ampel/vendor/aiopipe/__init__.py`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/conf/ampel-core/ampel.yaml` & `ampel_core-0.9.0/conf/ampel-core/ampel.yaml`

 * *Files 4% similar despite different names*

```diff
@@ -3,25 +3,22 @@
     stock: MongoStockIngester
     t0: MongoT0Ingester
     t1: MongoT1Ingester
     t2: MongoT2Ingester
     t3: MongoT3Ingester
 
 unit:
-
 # Controller units
 - ampel.core.DefaultProcessController
 
 # Context units
 - ampel.ops.AmpelExceptionPublisher
 - ampel.ops.OpsProcessor
 - ampel.t2.T2Worker
 - ampel.t3.T3Processor
-- ampel.t3.T3PlainUnitExecutor
-- ampel.t3.T3ReviewUnitExecutor
 - ampel.t3.include.session.T3SessionLastRunTime
 - ampel.t3.include.session.T3SessionAlertsNumber
 - ampel.t3.supply.T3DefaultBufferSupplier
 - ampel.t3.supply.SimpleT2BasedSupplier
 - ampel.t3.supply.select.T3StockSelector
 - ampel.t3.supply.select.T3FilteringStockSelector
 - ampel.t3.supply.load.T3SimpleDataLoader
@@ -32,29 +29,29 @@
 - ampel.t3.stage.T3SimpleStager
 - ampel.t3.stage.T3ProjectingStager
 - ampel.t3.stage.T3ChannelStager
 - ampel.t3.stage.T3AdaptativeStager
 - ampel.t3.stage.T3AggregatingStager
 - ampel.t3.stage.T3SequentialStager
 - ampel.t3.stage.T3DistributiveStager
+- ampel.t4.T4Processor
+- ampel.t4.T4RunTimeContextUpdater
 - ampel.cli.T3BufferExporterStager
 - ampel.cli.T3BufferExporterUnit
 - ampel.demo.DemoProcessor
 - ampel.ingest.ChainedT0Muxer
 
 # Logical units
 - ampel.t1.T1SimpleCombiner
 - ampel.t1.T1SimpleRetroCombiner
 - ampel.demo.DemoPointT2Unit
 - ampel.demo.DemoFirstPointT2Unit
-- ampel.demo.DemoReviewT3Unit
-- ampel.demo.DemoPlainT3Unit
-- ampel.demo.DemoResourceT3Unit
+- ampel.demo.DemoT3Unit
+- ampel.demo.DemoT4RunTimeAliasGenerator
 - ampel.t3.unit.T3LogAggregatedStocks
-- ampel.t3.unit.T3PrintStore
 - ampel.dev.NoShaper
 
 # Aux units
 - ampel.aux.SimpleTagFilter
 - ampel.aux.filter.SimpleDictArrayFilter
 - ampel.aux.filter.FlatDictArrayFilter
 - ampel.t3.stage.project.T3ChannelProjector
@@ -89,30 +86,29 @@
       resolve_config: true
     '%T2':
       col: t2
     '%T2RECORD':
       col: t2
 
 resource:
-
   '%mongo': mongodb://localhost:27017
   '%extcats': mongodb://localhost:27017
 
-process:
+template:
+  hash_t2_config: ampel.config.alter.HashT2Config
+  resolve_run_time_aliases: ampel.config.alter.ResolveRunTimeAliases
 
+process:
   - name: DefaultT2Process
     tier: 2
     schedule: every(5).minutes
     processor:
       unit: T2Worker
 
   - name: ExceptionPublisher
     tier: null
     schedule: every(10).minutes
     processor:
       unit: OpsProcessor
       config:
         execute:
           unit: AmpelExceptionPublisher
-
-template:
-  compact_t3: ampel.template.TPLCompactT3
```

### Comparing `ampel_core-0.8.6/conf/ampel-core/logging.yaml` & `ampel_core-0.9.0/conf/ampel-core/logging.yaml`

 * *Files identical despite different names*

### Comparing `ampel_core-0.8.6/conf/ampel-core/mongo/data.yaml` & `ampel_core-0.9.0/conf/ampel-core/mongo/data.yaml`

 * *Files 12% similar despite different names*

```diff
@@ -28,10 +28,14 @@
   - field: channel
   - field: code
   - field: meta.ts
 - name: t3
   indexes:
   - field: process
   - field: meta.ts
+- name: t4
+  indexes:
+  - field: process
+  - field: meta.ts
 role:
   r: logger
   w: writer
```

### Comparing `ampel_core-0.8.6/pyproject.toml` & `ampel_core-0.9.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "ampel-core"
-version = "0.8.6"
+version = "0.9.0"
 description = "Alice in Modular Provenance-Enabled Land"
 authors = ["Valery Brinnel"]
 maintainers = ["Jakob van Santen <jakob.van.santen@desy.de>"]
 license = "BSD-3-Clause"
 readme = "README.md"
 homepage = "https://ampelproject.github.io"
 repository = "https://github.com/AmpelProject/Ampel-core"
@@ -40,15 +40,15 @@
 'config_Build_or_update_config._Fetch_or_append_config_elements' = 'ampel.cli.ConfigCommand'
 #'start_Run_ampel_continuously._Processes_are_scheduled_according_to_config' = 'ampel.cli.StartCommand'
 't2_Match_and_either_reset_or_view_raw_t2_documents' = 'ampel.cli.T2Command'
 'buffer_Match_and_view_or_save_ampel_buffers' = 'ampel.cli.BufferCommand'
 'event_Show_events_information' = 'ampel.cli.EventCommand'
 
 [tool.poetry.dependencies]
-ampel-interface = {version = "^0.8.7"}
+ampel-interface = {version = "^0.9.0"}
 python = ">=3.10,<3.12"
 pymongo = "^4.0"
 pydantic = "^1.9.0"
 sjcl = "^0.2.1"
 schedule = "^1.0.0"
 yq = "^3.0.0"
 prometheus-client = ">=0.16,<0.17"
```

### Comparing `ampel_core-0.8.6/PKG-INFO` & `ampel_core-0.9.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ampel-core
-Version: 0.8.6
+Version: 0.9.0
 Summary: Alice in Modular Provenance-Enabled Land
 Home-page: https://ampelproject.github.io
 License: BSD-3-Clause
 Author: Valery Brinnel
 Maintainer: Jakob van Santen
 Maintainer-email: jakob.van.santen@desy.de
 Requires-Python: >=3.10,<3.12
@@ -16,15 +16,15 @@
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Scientific/Engineering :: Information Analysis
 Classifier: Typing :: Typed
 Provides-Extra: docs
 Provides-Extra: server
 Provides-Extra: slack
 Requires-Dist: Sphinx (>=6.1.2,<6.2.0) ; extra == "docs"
-Requires-Dist: ampel-interface (>=0.8.7,<0.9.0)
+Requires-Dist: ampel-interface (>=0.9.0,<0.10.0)
 Requires-Dist: appdirs (>=1.4.4,<2.0.0)
 Requires-Dist: fastapi (>=0.95,<0.96) ; extra == "server"
 Requires-Dist: prometheus-client (>=0.16,<0.17)
 Requires-Dist: psutil (>=5.8.0,<6.0.0)
 Requires-Dist: pydantic (>=1.9.0,<2.0.0)
 Requires-Dist: pymongo (>=4.0,<5.0)
 Requires-Dist: requests (>=2.0,<3.0)
```

