# Comparing `tmp/ampel-interface-0.8a1.tar.gz` & `tmp/ampel_interface-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ampel-interface-0.8a1.tar", max compression
+gzip compressed data, was "ampel_interface-0.9.0.tar", max compression
```

## Comparing `ampel-interface-0.8a1.tar` & `ampel_interface-0.9.0.tar`

### file list

```diff
@@ -1,82 +1,96 @@
--rw-r--r--   0        0        0     1512 2021-08-18 13:38:15.705117 ampel-interface-0.8a1/LICENSE
--rw-r--r--   0        0        0      124 2021-08-18 13:38:15.705117 ampel-interface-0.8a1/README.md
--rw-r--r--   0        0        0      612 2021-08-18 13:38:15.705117 ampel-interface-0.8a1/ampel/abstract/AbsApplicable.py
--rwxr-xr-x   0        0        0      949 2021-08-18 13:38:15.705117 ampel-interface-0.8a1/ampel/abstract/AbsCLIOperation.py
--rwxr-xr-x   0        0        0     1677 2021-08-18 13:38:15.705117 ampel-interface-0.8a1/ampel/abstract/AbsCustomStateT2Unit.py
--rw-r--r--   0        0        0     1235 2021-08-18 13:38:15.705117 ampel-interface-0.8a1/ampel/abstract/AbsIdMapper.py
--rwxr-xr-x   0        0        0     1847 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsPointT2Unit.py
--rwxr-xr-x   0        0        0     1000 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsSecretProvider.py
--rwxr-xr-x   0        0        0     1128 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsStateT2Unit.py
--rwxr-xr-x   0        0        0     1018 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsStockT2Unit.py
--rwxr-xr-x   0        0        0     1257 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsT0Unit.py
--rwxr-xr-x   0        0        0     1018 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsT1CombineUnit.py
--rwxr-xr-x   0        0        0      821 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsT1ComputeUnit.py
--rwxr-xr-x   0        0        0     1013 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsT1RetroCombineUnit.py
--rwxr-xr-x   0        0        0     1806 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsT3Unit.py
--rwxr-xr-x   0        0        0     3132 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsTiedCustomStateT2Unit.py
--rwxr-xr-x   0        0        0     1939 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsTiedPointT2Unit.py
--rwxr-xr-x   0        0        0     2611 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsTiedStateT2Unit.py
--rwxr-xr-x   0        0        0     1013 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsTiedStockT2Unit.py
--rwxr-xr-x   0        0        0     1093 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/AbsTiedT2Unit.py
--rwxr-xr-x   0        0        0      794 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/abstract/Secret.py
--rwxr-xr-x   0        0        0     3192 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/alert/AmpelAlert.py
--rw-r--r--   0        0        0     5963 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/base/AmpelABC.py
--rwxr-xr-x   0        0        0     4804 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/base/AmpelBaseModel.py
--rw-r--r--   0        0        0      576 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/base/AmpelFlexModel.py
--rwxr-xr-x   0        0        0     2621 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/base/AuxUnitRegister.py
--rwxr-xr-x   0        0        0      356 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/base/BadConfig.py
--rwxr-xr-x   0        0        0     2524 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/base/LogicalUnit.py
--rw-r--r--   0        0        0     1913 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/base/decorator.py
--rw-r--r--   0        0        0    16293 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/cli/AmpelArgumentParser.py
--rw-r--r--   0        0        0     2174 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/cli/AmpelHelpFormatter.py
--rw-r--r--   0        0        0     7806 2021-08-18 13:38:15.709117 ampel-interface-0.8a1/ampel/cli/ArgParserBuilder.py
--rw-r--r--   0        0        0      664 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/cli/LoadAllOfAction.py
--rw-r--r--   0        0        0      664 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/cli/LoadAnyOfAction.py
--rw-r--r--   0        0        0      515 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/cli/LoadJSONAction.py
--rw-r--r--   0        0        0      584 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/cli/MaybeIntAction.py
--rw-r--r--   0        0        0     3309 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/cli/main.py
--rwxr-xr-x   0        0        0     5159 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/config/AmpelConfig.py
--rwxr-xr-x   0        0        0      827 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/DataPoint.py
--rwxr-xr-x   0        0        0     1187 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/EventDocument.py
--rwxr-xr-x   0        0        0     1189 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/JournalRecord.py
--rwxr-xr-x   0        0        0     1737 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/LogDocument.py
--rwxr-xr-x   0        0        0     1201 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/MetaRecord.py
--rwxr-xr-x   0        0        0     1581 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/StockDocument.py
--rwxr-xr-x   0        0        0     1698 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/T1Document.py
--rwxr-xr-x   0        0        0     1964 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/T2Document.py
--rwxr-xr-x   0        0        0     1486 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/content/T3Document.py
--rwxr-xr-x   0        0        0     2170 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/enum/DocumentCode.py
--rwxr-xr-x   0        0        0      574 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/enum/EventCode.py
--rwxr-xr-x   0        0        0     1260 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/StateT2Dependency.py
--rw-r--r--   0        0        0     1075 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/StrictGenericModel.py
--rw-r--r--   0        0        0     1373 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/StrictModel.py
--rwxr-xr-x   0        0        0      932 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/T2IngestOptions.py
--rw-r--r--   0        0        0     1364 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/UnitModel.py
--rwxr-xr-x   0        0        0      520 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/operator/AllOf.py
--rwxr-xr-x   0        0        0      774 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/operator/AnyOf.py
--rw-r--r--   0        0        0      762 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/operator/FlatAnyOf.py
--rwxr-xr-x   0        0        0      497 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/model/operator/OneOf.py
--rwxr-xr-x   0        0        0     1414 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/protocol/LoggerProtocol.py
--rwxr-xr-x   0        0        0      544 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/protocol/LoggingHandlerProtocol.py
--rw-r--r--   0        0        0        0 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/py.typed
--rwxr-xr-x   0        0        0     1339 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/secret/AESecret.py
--rwxr-xr-x   0        0        0     1033 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/secret/AmpelVault.py
--rwxr-xr-x   0        0        0      944 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/secret/NamedSecret.py
--rwxr-xr-x   0        0        0      792 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/secret/Secret.py
--rwxr-xr-x   0        0        0     1436 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/struct/AmpelBuffer.py
--rwxr-xr-x   0        0        0     1937 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/struct/JournalAttributes.py
--rwxr-xr-x   0        0        0     1265 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/struct/T1CombineResult.py
--rwxr-xr-x   0        0        0     1077 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/struct/UnitResult.py
--rw-r--r--   0        0        0     1457 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/types.py
--rw-r--r--   0        0        0     1059 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/util/bson.py
--rw-r--r--   0        0        0     1612 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/util/compression.py
--rwxr-xr-x   0        0        0     2484 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/util/docstringutils.py
--rw-r--r--   0        0        0     1276 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/util/freeze.py
--rw-r--r--   0        0        0     3613 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/util/json.py
--rw-r--r--   0        0        0     1809 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/util/serialize.py
--rwxr-xr-x   0        0        0      818 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/view/ReadOnlyDict.py
--rwxr-xr-x   0        0        0     6419 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/view/SnapView.py
--rwxr-xr-x   0        0        0     3596 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/ampel/view/T2DocView.py
--rw-r--r--   0        0        0     1149 2021-08-18 13:38:15.713117 ampel-interface-0.8a1/pyproject.toml
--rw-r--r--   0        0        0     1273 2021-08-18 13:38:37.046801 ampel-interface-0.8a1/setup.py
--rw-r--r--   0        0        0     1253 2021-08-18 13:38:37.047139 ampel-interface-0.8a1/PKG-INFO
+-rw-r--r--   0        0        0     1512 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/LICENSE
+-rw-r--r--   0        0        0      124 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/README.md
+-rw-r--r--   0        0        0      642 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsApplicable.py
+-rwxr-xr-x   0        0        0     1050 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsCLIOperation.py
+-rwxr-xr-x   0        0        0     1721 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsCustomStateT2Unit.py
+-rw-r--r--   0        0        0     1228 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsIdMapper.py
+-rwxr-xr-x   0        0        0     2088 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsPointT2Unit.py
+-rwxr-xr-x   0        0        0     1109 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsSecretProvider.py
+-rwxr-xr-x   0        0        0     1179 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsStateT2Unit.py
+-rwxr-xr-x   0        0        0     1042 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsStockT2Unit.py
+-rwxr-xr-x   0        0        0     1268 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsT0Unit.py
+-rwxr-xr-x   0        0        0     1031 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsT1CombineUnit.py
+-rwxr-xr-x   0        0        0      832 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsT1ComputeUnit.py
+-rwxr-xr-x   0        0        0     1046 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsT1RetroCombineUnit.py
+-rwxr-xr-x   0        0        0     1885 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsT3Unit.py
+-rwxr-xr-x   0        0        0      733 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsT4Unit.py
+-rwxr-xr-x   0        0        0     1984 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsTiedCustomStateT2Unit.py
+-rwxr-xr-x   0        0        0     1345 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsTiedPointT2Unit.py
+-rwxr-xr-x   0        0        0     1396 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsTiedStateT2Unit.py
+-rwxr-xr-x   0        0        0     1064 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsTiedStockT2Unit.py
+-rwxr-xr-x   0        0        0     1123 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/abstract/AbsTiedT2Unit.py
+-rwxr-xr-x   0        0        0     4034 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/alert/AmpelAlert.py
+-rwxr-xr-x   0        0        0    12019 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/AlternativeAmpelBaseModel.py
+-rw-r--r--   0        0        0     5987 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/AmpelABC.py
+-rw-r--r--   0        0        0     1025 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/AmpelBaseModel.py
+-rw-r--r--   0        0        0      615 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/AmpelFlexModel.py
+-rw-r--r--   0        0        0     1017 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/AmpelGenericModel.py
+-rw-r--r--   0        0        0     7033 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/AmpelUnit.py
+-rwxr-xr-x   0        0        0     2858 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/AuxUnitRegister.py
+-rwxr-xr-x   0        0        0      386 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/BadConfig.py
+-rwxr-xr-x   0        0        0     1832 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/LogicalUnit.py
+-rw-r--r--   0        0        0     1970 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/base/decorator.py
+-rwxr-xr-x   0        0        0    16556 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/AmpelArgumentParser.py
+-rw-r--r--   0        0        0     2349 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/AmpelHelpFormatter.py
+-rw-r--r--   0        0        0     6624 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/ArgParserBuilder.py
+-rw-r--r--   0        0        0      702 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/LoadAllOfAction.py
+-rw-r--r--   0        0        0      702 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/LoadAnyOfAction.py
+-rw-r--r--   0        0        0      545 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/LoadJSONAction.py
+-rw-r--r--   0        0        0      661 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/MaybeIntAction.py
+-rw-r--r--   0        0        0     1202 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/config.py
+-rw-r--r--   0        0        0    12099 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/cli/main.py
+-rwxr-xr-x   0        0        0     5237 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/config/AmpelConfig.py
+-rwxr-xr-x   0        0        0      938 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/DataPoint.py
+-rwxr-xr-x   0        0        0     1374 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/EventDocument.py
+-rwxr-xr-x   0        0        0     1442 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/JournalRecord.py
+-rwxr-xr-x   0        0        0     1791 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/LogDocument.py
+-rwxr-xr-x   0        0        0      935 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/MetaActivity.py
+-rwxr-xr-x   0        0        0     1470 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/MetaRecord.py
+-rwxr-xr-x   0        0        0     1613 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/StockDocument.py
+-rwxr-xr-x   0        0        0     1774 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/T1Document.py
+-rwxr-xr-x   0        0        0     2150 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/T2Document.py
+-rwxr-xr-x   0        0        0     1907 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/T3Document.py
+-rwxr-xr-x   0        0        0     1523 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/content/T4Document.py
+-rwxr-xr-x   0        0        0     2588 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/enum/DocumentCode.py
+-rwxr-xr-x   0        0        0      729 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/enum/EventCode.py
+-rwxr-xr-x   0        0        0     1898 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/enum/JournalActionCode.py
+-rwxr-xr-x   0        0        0     1138 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/enum/MetaActionCode.py
+-rwxr-xr-x   0        0        0     2335 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/model/DPSelection.py
+-rwxr-xr-x   0        0        0     1491 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/model/StateT2Dependency.py
+-rw-r--r--   0        0        0     1171 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/model/UnitModel.py
+-rwxr-xr-x   0        0        0      565 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/model/operator/AllOf.py
+-rwxr-xr-x   0        0        0      838 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/model/operator/AnyOf.py
+-rw-r--r--   0        0        0      839 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/model/operator/FlatAnyOf.py
+-rwxr-xr-x   0        0        0      532 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/model/operator/OneOf.py
+-rwxr-xr-x   0        0        0     1292 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/protocol/AmpelAlertProtocol.py
+-rwxr-xr-x   0        0        0     1343 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/protocol/LoggerProtocol.py
+-rwxr-xr-x   0        0        0      712 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/protocol/LoggingHandlerProtocol.py
+-rw-r--r--   0        0        0        0 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/py.typed
+-rwxr-xr-x   0        0        0     1368 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/secret/AESecret.py
+-rwxr-xr-x   0        0        0     1269 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/secret/AmpelVault.py
+-rwxr-xr-x   0        0        0      981 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/secret/NamedSecret.py
+-rwxr-xr-x   0        0        0      850 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/secret/Secret.py
+-rwxr-xr-x   0        0        0     1382 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/struct/AmpelBuffer.py
+-rwxr-xr-x   0        0        0     1941 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/struct/JournalAttributes.py
+-rwxr-xr-x   0        0        0     1669 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/struct/Resource.py
+-rwxr-xr-x   0        0        0     1236 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/struct/StockAttributes.py
+-rwxr-xr-x   0        0        0     1267 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/struct/T1CombineResult.py
+-rwxr-xr-x   0        0        0     4149 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/struct/T3Store.py
+-rwxr-xr-x   0        0        0     1839 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/struct/UnitResult.py
+-rw-r--r--   0        0        0     1856 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/types.py
+-rw-r--r--   0        0        0     1089 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/util/bson.py
+-rw-r--r--   0        0        0     1674 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/util/compression.py
+-rwxr-xr-x   0        0        0     2528 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/util/docstringutils.py
+-rw-r--r--   0        0        0     1300 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/util/freeze.py
+-rwxr-xr-x   0        0        0     3838 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/util/hash.py
+-rw-r--r--   0        0        0     3387 2023-04-06 18:46:52.216273 ampel_interface-0.9.0/ampel/util/json.py
+-rwxr-xr-x   0        0        0    10563 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/util/mappings.py
+-rw-r--r--   0        0        0     1691 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/util/recursion.py
+-rw-r--r--   0        0        0     2473 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/util/serialize.py
+-rw-r--r--   0        0        0     3181 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/util/tag.py
+-rwxr-xr-x   0        0        0      863 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/view/ReadOnlyDict.py
+-rwxr-xr-x   0        0        0    10196 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/view/SnapView.py
+-rwxr-xr-x   0        0        0     7075 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/view/T2DocView.py
+-rwxr-xr-x   0        0        0     3745 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/ampel/view/T3DocView.py
+-rw-r--r--   0        0        0     1229 2023-04-06 18:46:52.220272 ampel_interface-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0     1301 1970-01-01 00:00:00.000000 ampel_interface-0.9.0/PKG-INFO
```

### Comparing `ampel-interface-0.8a1/LICENSE` & `ampel_interface-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsApplicable.py` & `ampel_interface-0.9.0/ampel/abstract/AbsApplicable.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-core/ampel/abstract/AbsApplicable.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 27.02.2020
-# Last Modified Date: 09.05.2020
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-core/ampel/abstract/AbsApplicable.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                27.02.2020
+# Last Modified Date:  09.05.2020
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.AmpelBaseModel import AmpelBaseModel
 
 class AbsApplicable(AmpelABC, AmpelBaseModel, abstract=True):
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsCLIOperation.py` & `ampel_interface-0.9.0/ampel/abstract/AbsCLIOperation.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,28 +1,34 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsCLIOperation.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 16.03.2021
-# Last Modified Date: 22.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsCLIOperation.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                16.03.2021
+# Last Modified Date:  14.08.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Sequence, Dict, Any, Optional, Union
+from typing import Any
+from collections.abc import Sequence
 from argparse import ArgumentParser
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.cli.AmpelArgumentParser import AmpelArgumentParser
 
 
 class AbsCLIOperation(AmpelABC, abstract=True):
 	"""
 	Implementing subclasses shall be placed in package ampel.cli
 	"""
 
+	@staticmethod
 	@abstractmethod
-	def get_parser(self, sub_op: Optional[str] = None) -> Union[ArgumentParser, AmpelArgumentParser]:
+	def get_sub_ops() -> None | list[str]:
 		...
 
 	@abstractmethod
-	def run(self, args: Dict[str, Any], unknown_args: Sequence[str], sub_op: Optional[str] = None) -> None:
+	def get_parser(self, sub_op: None | str = None) -> ArgumentParser | AmpelArgumentParser:
+		...
+
+	@abstractmethod
+	def run(self, args: dict[str, Any], unknown_args: Sequence[str], sub_op: None | str = None) -> None:
 		...
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsCustomStateT2Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsCustomStateT2Unit.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsCustomStateT2Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 28.12.2019
-# Last Modified Date: 03.04.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsCustomStateT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                28.12.2019
+# Last Modified Date:  03.04.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Iterable, Generic, Union
+from typing import Generic
+from collections.abc import Iterable
 from ampel.types import T, UBson
 from ampel.struct.UnitResult import UnitResult
 from ampel.content.T1Document import T1Document
 from ampel.content.DataPoint import DataPoint
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.LogicalUnit import LogicalUnit
@@ -34,13 +35,13 @@
 		For example, AbsCustomStateT2Unit[LightCurve] would return a
 		:class:`~ampel.view.LightCurve.LightCurve` instance.
 		"""
 		...
 
 
 	@abstractmethod
-	def process(self, arg: T) -> Union[UBson, UnitResult]:
+	def process(self, arg: T) -> UBson | UnitResult:
 		"""
 		Returned object should contain computed science results to be saved into the DB.
 
 		.. note:: the returned dict must have only string keys and be BSON-encodable
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsIdMapper.py` & `ampel_interface-0.9.0/ampel/abstract/AbsIdMapper.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsIdMapper.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 12.02.2021
-# Last Modified Date: 12.02.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsIdMapper.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                12.02.2021
+# Last Modified Date:  12.02.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import List, Union, overload
+from typing import overload
 from ampel.types import StrictIterable, StockId
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.AmpelBaseModel import AmpelBaseModel
 
 
 class AbsIdMapper(AmpelABC, AmpelBaseModel, abstract=True):
@@ -19,29 +19,29 @@
 	@overload
 	@classmethod
 	def to_ampel_id(cls, ext_id: str) -> int:
 		...
 
 	@overload
 	@classmethod
-	def to_ampel_id(cls, ext_id: StrictIterable[str]) -> List[int]:
+	def to_ampel_id(cls, ext_id: StrictIterable[str]) -> list[int]:
 		...
 
 	@classmethod
 	@abstractmethod
-	def to_ampel_id(cls, ext_id: Union[str, StrictIterable[str]]) -> Union[int, List[int]]:
+	def to_ampel_id(cls, ext_id: str | StrictIterable[str]) -> int | list[int]:
 		...
 
 	@overload
 	@classmethod
 	def to_ext_id(cls, ampel_id: StockId) -> str:
 		...
 
 	@overload
 	@classmethod
-	def to_ext_id(cls, ampel_id: StrictIterable[StockId]) -> List[str]:
+	def to_ext_id(cls, ampel_id: StrictIterable[StockId]) -> list[str]:
 		...
 
 	@classmethod
 	@abstractmethod
-	def to_ext_id(cls, ampel_id: Union[StockId, StrictIterable[StockId]]) -> Union[str, List[str]]:
+	def to_ext_id(cls, ampel_id: StockId | StrictIterable[StockId]) -> str | list[str]:
 		...
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsPointT2Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsPointT2Unit.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,59 +1,55 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsPointT2Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 28.12.2019
-# Last Modified Date: 03.04.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsPointT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                28.12.2019
+# Last Modified Date:  28.09.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Union, Optional, ClassVar
 from ampel.types import UBson
 from ampel.struct.UnitResult import UnitResult
 from ampel.content.DataPoint import DataPoint
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.LogicalUnit import LogicalUnit
-from ampel.model.T2IngestOptions import T2IngestOptions
 
 
 class AbsPointT2Unit(AmpelABC, LogicalUnit, abstract=True):
 	"""
 	A T2 unit bound to a :class:`~ampel.content.DataPoint.DataPoint`
-	"""
-
-	# See T2IngestOptions docstring for more info
-	#: Which :class:`~ampel.content.DataPoint.DataPoint` to create
-	#: :class:`T2 documents <ampel.content.T2Document.T2Document>` for
-	#:
-	#: Example::
-	#:    {'filter': 'PPSFilter', 'sort': 'jd', 'select': 'first'}
-	#:
-	#: "first"
-	#:   first datapoint for a stock
-	#: "last"
-	#:   most recent datapoint for a stock
-	#: "all"
-	#:   every datapoint (default)
-	#: :class:`tuple`
-	#:   :class:`slice` of datapoints
-	#:
-	#: Example::
-	#:
-	#:   {"select": (1, -2, 5)}
-	#:
-	#: will create documents bound to every 5th datapoint starting from the 2nd
-	#: and ending with the 3rd-to-last
-	#:
-	#: If unspecified, a T2 document will be created for each datapoint.
 
-	ingest: ClassVar[Optional[T2IngestOptions]] = None
+	Note that the implementing class can customize the default ingestion behavior
+	(which :class:`~ampel.content.DataPoint.DataPoint` to create
+	:class:`T2 documents <ampel.content.T2Document.T2Document>` for)
+	by defining the class variable 'eligible'
+	
+	Example::
+	  ingest: ClassVar[DPSelection] = DPSelection(select=(1, -2, 5))
+	
+	will create documents bound to every 5th datapoint starting from the 2nd
+	and ending with the 3rd-to-last
+
+	Example::
+	   ingest: ClassVar[DPSelection] = DPSelection(filter=UnitModel(unit='SimpleTagFilter', config={'require': ['ZTF_DP']}), sort='jd', select='first'}
+
+	will create documents bound to the first datapoint with tag 'ZTF_DP', in order of body.jd.
+	
+	select options:
+	  - "first": first datapoint for a stock
+	  - "last": most recent datapoint for a stock
+	  - "all": every datapoint (default)
+	  - :class:`tuple`: :class:`slice` of datapoints
+	-> see DPSelection docstring for info regarding 'filter' and 'sort'.
 
+	If 'eligible' is not specified, default ingestion will occur:
+	a T2 document will be created for each datapoint
+	"""
 
 	@abstractmethod
-	def process(self, datapoint: DataPoint) -> Union[UBson, UnitResult]:
+	def process(self, datapoint: DataPoint) -> UBson | UnitResult:
 		"""
 		Returned object should contain computed science results to be saved into the DB.
 
 		.. note:: the returned dict must have only string keys and be BSON-encodable
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsSecretProvider.py` & `ampel_interface-0.9.0/ampel/abstract/AbsSecretProvider.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,29 +1,31 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsSecretProvider.py
-# License           : BSD-3-Clause
-# Author            : Jakob van Santen <jakob.van.santen@desy.de>
-# Date              : 14.08.2020
-# Last Modified Date: 21.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsSecretProvider.py
+# License:             BSD-3-Clause
+# Author:              Jakob van Santen <jakob.van.santen@desy.de>
+# Date:                14.08.2020
+# Last Modified Date:  21.06.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from ampel.abstract.Secret import Secret
+from typing import Type
+from ampel.secret.Secret import Secret
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 
 
 class AbsSecretProvider(AmpelABC, abstract=True):
 	"""
 	Interface to a secret store used to resolve secrets.
 	The underlying store may be as simple as a dict loaded from a JSON file
 	or a complete key manager like Vault.
 	"""
 
 	@abstractmethod
-	def tell(self, arg: Secret) -> bool:
+	def tell(self, arg: Secret, ValueType: type) -> bool:
 		"""
 		Potentially update an initialized Secret instance with
 		the actual sensitive information associable with it.
 		:returns: True if the Secret was told/resolved or False
-		if the provided Secret is unknown to this secret provider
+		if the provided Secret is either unknown to this secret
+		provider, or resolves to a value of the wrong type.
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsStateT2Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsStateT2Unit.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsStateT2Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 28.12.2019
-# Last Modified Date: 30.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsStateT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                28.12.2019
+# Last Modified Date:  30.05.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Iterable, Union
+from typing import Union
+from collections.abc import Iterable
 from ampel.types import UBson
 from ampel.struct.UnitResult import UnitResult
 from ampel.content.T1Document import T1Document
 from ampel.content.DataPoint import DataPoint
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.LogicalUnit import LogicalUnit
@@ -19,13 +20,13 @@
 
 class AbsStateT2Unit(AmpelABC, LogicalUnit, abstract=True):
 	"""
 	A T2 unit bound to a :class:`~ampel.content.T1Document.T1Document` (state of a stock)
 	"""
 
 	@abstractmethod
-	def process(self, compound: T1Document, datapoints: Iterable[DataPoint]) -> Union[UBson, UnitResult]:
+	def process(self, compound: T1Document, datapoints: Iterable[DataPoint]) -> UBson | UnitResult:
 		"""
 		Returned object should contain computed science results to be saved into the DB.
 
 		.. note:: the returned dict must have only string keys and be BSON-encodable
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsStockT2Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsStockT2Unit.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsStockT2Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 28.12.2019
-# Last Modified Date: 11.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsStockT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                28.12.2019
+# Last Modified Date:  11.06.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from ampel.types import Union, UBson
 from ampel.struct.UnitResult import UnitResult
 from ampel.content.StockDocument import StockDocument
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.LogicalUnit import LogicalUnit
@@ -17,13 +17,13 @@
 
 class AbsStockT2Unit(AmpelABC, LogicalUnit, abstract=True):
 	"""
 	A T2 unit bound to a :class:`~ampel.content.StockDocument.StockDocument`
 	"""
 
 	@abstractmethod
-	def process(self, stock_doc: StockDocument) -> Union[UBson, UnitResult]:
+	def process(self, stock_doc: StockDocument) -> UBson | UnitResult:
 		"""
 		Returned object should contain computed science results to be saved into the DB.
 
 		.. note:: the returned dict must have only string keys and be BSON-encodable
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsT0Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsT0Unit.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsT0Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 07.10.2019
-# Last Modified Date: 15.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsT0Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                07.10.2019
+# Last Modified Date:  15.05.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Any, List, Optional
+from typing import Any
 from ampel.types import StockId
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.LogicalUnit import LogicalUnit
 from ampel.content.DataPoint import DataPoint
 
 
@@ -25,11 +25,11 @@
 	For example, in the case of ZiDataPointShaper:
 		* The field candid is renamed in id
 		* A new field 'tag' is created
 		...
 	"""
 
 	@abstractmethod
-	def process(self, arg: Any, stock: Optional[StockId] = None) -> List[DataPoint]:
+	def process(self, arg: Any, stock: None | StockId = None) -> list[DataPoint]:
 		"""
 		Convert an external object to Ampel format
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsT1ComputeUnit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsT1ComputeUnit.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsT1ComputeUnit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 13.05.2021
-# Last Modified Date: 13.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsT1ComputeUnit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                13.05.2021
+# Last Modified Date:  13.05.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import List, Union, Tuple
+from typing import Tuple
 from ampel.types import UBson, StockId
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.decorator import abstractmethod
 from ampel.base.LogicalUnit import LogicalUnit
 from ampel.content.DataPoint import DataPoint
 from ampel.struct.UnitResult import UnitResult
 	
 
 class AbsT1ComputeUnit(AmpelABC, LogicalUnit, abstract=True):
 
 	@abstractmethod
-	def compute(self, datapoints: List[DataPoint]) -> Tuple[Union[UBson, UnitResult], StockId]:
+	def compute(self, datapoints: list[DataPoint]) -> tuple[UBson | UnitResult, StockId]:
 		...
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsT1RetroCombineUnit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsTiedStockT2Unit.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,29 +1,29 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsT1RetroCombineUnit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 17.06.2021
-# Last Modified Date: 17.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsTiedStockT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                17.02.2021
+# Last Modified Date:  03.04.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Union, Iterable, List
-from ampel.types import ChannelId, DataPointId
-from ampel.base.AmpelABC import AmpelABC
+from typing import Union
+from collections.abc import Sequence
+from ampel.types import UBson
+from ampel.struct.UnitResult import UnitResult
+from ampel.view.T2DocView import T2DocView
 from ampel.base.decorator import abstractmethod
-from ampel.base.LogicalUnit import LogicalUnit
-from ampel.content.DataPoint import DataPoint
-from ampel.struct.T1CombineResult import T1CombineResult
+from ampel.content.StockDocument import StockDocument
+from ampel.abstract.AbsTiedT2Unit import AbsTiedT2Unit
 
 
-class AbsT1RetroCombineUnit(AmpelABC, LogicalUnit, abstract=True):
-	""" A unit that combines datapoints """
-
-	debug: bool = False
-	channel: ChannelId
-	access: List[Union[int, str]]
-	policy: List[Union[int, str]]
+class AbsTiedStockT2Unit(AbsTiedT2Unit, abstract=True):
+	""" Later """
 
 	@abstractmethod
-	def combine(self, datapoints: Iterable[DataPoint]) -> Union[List[List[DataPointId]], List[T1CombineResult]]:
-		...
+	def process(self, stock: StockDocument, t2_view: Sequence[T2DocView]) -> UBson | UnitResult:
+		"""
+		Returned object should contain computed science results to be saved into the DB.
+
+		.. note:: the returned dict must have only string keys and be BSON-encodable
+		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsTiedCustomStateT2Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsTiedCustomStateT2Unit.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsTiedCustomStateT2Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 03.04.2020
-# Last Modified Date: 30.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsTiedCustomStateT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                03.04.2020
+# Last Modified Date:  28.09.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Generic, Iterable, Sequence, Dict, Any, Union, Optional, TypeVar
+from typing import Generic, TypeVar
+from collections.abc import Iterable, Sequence
 from ampel.types import T, UBson
 from ampel.struct.UnitResult import UnitResult
 from ampel.view.T2DocView import T2DocView
 from ampel.content.DataPoint import DataPoint
 from ampel.base.decorator import abstractmethod
 from ampel.content.T1Document import T1Document
 from ampel.abstract.AbsTiedT2Unit import AbsTiedT2Unit
 from ampel.model.StateT2Dependency import StateT2Dependency
 
-U = TypeVar("U")
+U = TypeVar("U", bound=str)
 
 
 class AbsTiedCustomStateT2Unit(Generic[T, U], AbsTiedT2Unit, abstract=True):
 	"""
 	A T2 unit bound to a custom type *constructed* from a :class:`compound <ampel.content.T1Document.T1Document>`,
 	as well as the results of other T2 units.
 
@@ -39,36 +40,14 @@
 		"""
 		Create the parametrized type using compound and datapoints.
 		For example, AbsTiedCustomStateT2Unit[LightCurve] would return a
 		:class:`~ampel.view.LightCurve.LightCurve` instance.
 		"""
 		...
 
-	@staticmethod
-	@abstractmethod(force=True)
-	def get_link(link_override: Dict[Any, Any], arg: T) -> Optional[Union[int, bytes]]:
-		"""
-		Method used by T2Processor if 't2_dependency' is specified in the t2 config dict
-		and if 'link_override' is defined in there.
-
-		T2Processor needs to retrieve the T2Records of units tied with this unit.
-		If unspecified in config, t2 dependencies are resolved - for each unit defined in get_tied_unit_names() -
-		using the db match query: {unit: <unit_name>, config: None, link: <same link as root doc>}.
-
-		This behavior is overridable/customizable by adding the keyword 't2_dependency' to the t2 config dict.
-		The value of t2_dependency should be of type Union[T2Dependency, List[T2Dependency]].
-		The parameter 'link_override' in T2Dependency allows to link this state T2 with a different value
-		than the one registered as 'link' in the T2Record (which is the _id of a compound document for state t2s).
-
-		This method thus enables to tie a state T2 with the result of a point t2
-		(the returned link could be the id of the first datapoint contained in the compound)
-
-		:returns: the value of 'link' (tied t2 document) to be matched
-		"""
-
 	@abstractmethod
-	def process(self, arg: T, t2_views: Sequence[T2DocView]) -> Union[UBson, UnitResult]:
+	def process(self, arg: T, t2_views: Sequence[T2DocView]) -> UBson | UnitResult:
 		"""
 		Returned object should contain computed science results to be saved into the DB.
 
 		.. note:: the returned dict must have only string keys and be BSON-encodable
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsTiedStockT2Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsTiedStateT2Unit.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,28 +1,40 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsTiedStockT2Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 17.02.2021
-# Last Modified Date: 03.04.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsTiedStateT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                11.03.2020
+# Last Modified Date:  28.09.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Sequence, Union
+from typing import Generic
+from collections.abc import Sequence
 from ampel.types import UBson
 from ampel.struct.UnitResult import UnitResult
 from ampel.view.T2DocView import T2DocView
 from ampel.base.decorator import abstractmethod
-from ampel.content.StockDocument import StockDocument
+from ampel.content.T1Document import T1Document
+from ampel.content.DataPoint import DataPoint
 from ampel.abstract.AbsTiedT2Unit import AbsTiedT2Unit
+from ampel.model.StateT2Dependency import StateT2Dependency, T
 
 
-class AbsTiedStockT2Unit(AbsTiedT2Unit, abstract=True):
-	""" Later """
+class AbsTiedStateT2Unit(Generic[T], AbsTiedT2Unit, abstract=True):
+	"""
+	A T2 unit bound to a :class:`~ampel.content.T1Document.T1Document` (state of a stock),
+	as well as the results of other T2 units
+	"""
+
+	t2_dependency: Sequence[StateT2Dependency[T]]
 
 	@abstractmethod
-	def process(self, stock: StockDocument, t2_view: Sequence[T2DocView]) -> Union[UBson, UnitResult]:
+	def process(self,
+		compound: T1Document,
+		datapoints: Sequence[DataPoint],
+		t2_views: Sequence[T2DocView]
+	) -> UBson | UnitResult:
 		"""
 		Returned object should contain computed science results to be saved into the DB.
 
 		.. note:: the returned dict must have only string keys and be BSON-encodable
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/AbsTiedT2Unit.py` & `ampel_interface-0.9.0/ampel/abstract/AbsTiedT2Unit.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/AbsTiedT2Unit.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 06.02.2021
-# Last Modified Date: 31.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/abstract/AbsTiedT2Unit.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                06.02.2021
+# Last Modified Date:  31.05.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Sequence
 from ampel.model.UnitModel import UnitModel
 from ampel.base.AmpelABC import AmpelABC
 from ampel.base.LogicalUnit import LogicalUnit
```

### Comparing `ampel-interface-0.8a1/ampel/abstract/Secret.py` & `ampel_interface-0.9.0/ampel/secret/Secret.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,22 +1,23 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/abstract/Secret.py
-# License           : BSD-3-Clause
-# Author            : Jakob van Santen <jakob.van.santen@desy.de>
-# Date              : 14.08.2020
-# Last Modified Date: 20.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/secret/Secret.py
+# License:             BSD-3-Clause
+# Author:              Jakob van Santen <jakob.van.santen@desy.de>
+# Date:                14.08.2020
+# Last Modified Date:  08.09.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Generic
-from ampel.types import T
+from typing import Generic, TypeVar
 from ampel.base.decorator import abstractmethod
 from ampel.base.AmpelABC import AmpelABC
 
+T = TypeVar('T')
 
+# mypy: disable-error-code = empty-body
 class Secret(Generic[T], AmpelABC, abstract=True):
     """
     A wrapper for a piece of sensitive data, e.g. a password or access token.
     """
 
     @abstractmethod
     def get(self) -> T:
```

### Comparing `ampel-interface-0.8a1/ampel/alert/AmpelAlert.py` & `ampel_interface-0.9.0/ampel/alert/AmpelAlert.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,144 +1,164 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/alert/AmpelAlert.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 26.01.2020
-# Last Modified Date: 25.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/alert/AmpelAlert.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                26.01.2020
+# Last Modified Date:  02.01.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import operator
-from typing import Dict, Tuple, List, Sequence, Optional, Any, Callable, Union
-from ampel.types import StockId
-
-osa = object.__setattr__
+from typing import Any
+from collections.abc import Callable, Sequence
+from ampel.types import JDict, StockId, Tag
 
 # Do not enable customizations of operators by sub-classes for now
-ops: Dict[str, Callable[[str, Any], bool]] = {
+ops: dict[str, Callable[[str, Any], bool]] = {
 	'>': operator.gt,
 	'<': operator.lt,
 	'>=': operator.ge,
 	'<=': operator.le,
 	'==': operator.eq,
 	'!=': operator.ne,
 	'is': operator.is_,
-	'is not': operator.is_not
+	'is not': operator.is_not,
+	'contains': operator.contains,
+	'exists': None, # type: ignore
 }
 
-def __ro__(self, *args, **kwargs):
-	raise RuntimeError("Cannot modify AmpelAlert")
-
 
 class AmpelAlert:
+	"""
+	Implements AmpelAlertProtocol
+	"""
+
+	__slots__ = '_id', '_stock', '_datapoints', '_tag', '_extra'
+
+	def __init__(self,
+		id: int, #: unique identifier for this alert
+		stock: StockId, #: stock this alert belongs to
+		datapoints: Sequence[JDict],
+		tag: None | Tag | list[Tag] = None, #: Optional tag associated with this alert
+		extra: None | JDict = None #: Optional information associated with this alert
+	) -> None:
+		sa = object.__setattr__
+		sa(self, '_id', id)
+		sa(self, '_stock', stock)
+		sa(self, '_datapoints', datapoints)
+		sa(self, '_tag', tag)
+		sa(self, '_extra', extra)
+
+	@property
+	def id(self) -> int:
+		return self._id # type: ignore[attr-defined]
+
+	@property
+	def stock(self) -> StockId:
+		return self._stock # type: ignore[attr-defined]
+
+	@property
+	def datapoints(self) -> Sequence[JDict]:
+		return self._datapoints # type: ignore[attr-defined]
+
+	@property
+	def tag(self) -> None | Tag | list[Tag]:
+		return self._tag # type: ignore[attr-defined]
+
+	@property
+	def extra(self) -> None | JDict:
+		return self._extra # type: ignore[attr-defined]
 
-	__slots__ = 'id', 'stock_id', 'dps', 'new'
-	__setattr__ = __ro__
-
-	id: int #: unique identifier for this alert
-	stock_id: StockId #: stock this alert belongs to
-	dps: Sequence[Dict] #: datapoints
-
-
-	def __init__(self, id: Union[int, str], stock_id: StockId, dps: Sequence[Dict]) -> None:
-		osa(self, 'id', id)
-		osa(self, 'stock_id', stock_id)
-		osa(self, 'dps', dps)
+	def __reduce__(self):
+		return (
+			type(self),
+			(self._id, self._stock, self._datapoints, self._tag, self._extra)
+		)
 
+	def __setattr__(self, k, v):
+		raise ValueError("AmpelAlert is read only")
 
-	def __reduce__(self):
-		return (type(self), (self.id, self.stock_id, self.dps))
+	def __delattr__(self, k):
+		raise ValueError("AmpelAlert is read only")
 
 
 	def get_values(self,
 		key: str,
-		filters: Optional[Sequence[Dict[str, Any]]] = None,
-		data: Optional[Sequence[Dict]] = None
-	) -> List[Any]:
+		filters: None | Sequence[JDict] = None
+	) -> list[Any]:
 		"""
 		Example:
 			
 			get_values("magpsf")
 		"""
-
-		if not data:
-			data = self.dps
-
-		if filters:
-			data = AmpelAlert.apply_filter(data, filters)
-
+		data = self.apply_filter(self.datapoints, filters) if filters else self.datapoints
 		return [el[key] for el in data if key in el]
 
 
 	def get_tuples(self,
 		key1: str, key2: str,
-		filters: Optional[Sequence[Dict[str, Any]]] = None,
-		data: Optional[Sequence[Dict]] = None
-	) -> List[Tuple[Any, Any]]:
+		filters: None | Sequence[JDict] = None
+	) -> list[tuple[Any, Any]]:
 		"""
 		Example::
 			
 			get_tuples("jd", "magpsf")
 		"""
-
-		if not data:
-			data = self.dps
-
-		if filters:
-			data = AmpelAlert.apply_filter(data, filters)
-
+		data = self.apply_filter(self.datapoints, filters) if filters else self.datapoints
 		return [
 			(el[key1], el[key2])
 			for el in data if key1 in el and key2 in el
 		]
 
 
 	def get_ntuples(self,
-		params: List[str],
-		filters: Optional[Sequence[Dict[str, Any]]] = None,
-		data: Optional[Sequence[Dict]] = None
-	) -> List[Tuple]:
+		params: list[str],
+		filters: None | Sequence[JDict] = None
+	) -> list[tuple]:
 		"""
 		Example:
 			
 			get_ntuples(["fid", "jd", "magpsf"])
 		"""
-
-		if not data:
-			data = self.dps
-
-		if filters:
-			data = AmpelAlert.apply_filter(data, filters)
-
+		data = self.apply_filter(self.datapoints, filters) if filters else self.datapoints
 		return [
 			tuple(el[param] for param in params)
 			for el in data if all(param in el for param in params)
 		]
 
 
 	def is_new(self) -> bool:
-		return len(self.dps) == 1
-
-
-	def dict(self) -> Dict[str, Any]:
-		return {'id': self.id, 'stock_id': self.stock_id, 'dps': self.dps}
+		return len(self.datapoints) == 1
 
 
-	@staticmethod
-	def apply_filter(
-		dicts: Sequence[Dict],
-		filters: Sequence[Dict[str, Any]]
-	) -> Sequence[Dict]:
+	def apply_filter(self,
+		dicts: Sequence[JDict],
+		filters: Sequence[JDict]
+	) -> Sequence[JDict]:
 
 		if isinstance(filters, dict):
 			filters = [filters]
 		else:
 			if filters is None or not isinstance(filters, (list, tuple)):
 				raise ValueError("Parameter 'filters' must be a dict or a sequence of dicts")
 
 		for f in filters:
-			op = ops[f['operator']]
-			f_attr = f['attribute']
-			f_val = f['value']
-			dicts = [d for d in dicts if f_attr in d and op(d[f_attr], f_val)]
+			attr = f['attribute']
+			op = f['operator']
+			if op == 'exists':
+				if f['value'] is True:
+					dicts = [d for d in dicts if attr in d]
+				else:
+					dicts = [d for d in dicts if attr not in d]
+			else:
+				dicts = [d for d in dicts if attr in d and ops[op](d[attr], f['value'])]
 
 		return dicts
+
+
+	def dict(self) -> JDict:
+		return {
+			'id': self.id,
+			'stock': self.stock,
+			'datapoints': self.datapoints,
+			'extra': self.extra,
+		}
```

### Comparing `ampel-interface-0.8a1/ampel/base/AmpelABC.py` & `ampel_interface-0.9.0/ampel/base/AmpelABC.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/base/AmpelABC.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 27.12.2017
-# Last Modified Date: 17.02.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/base/AmpelABC.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                27.12.2017
+# Last Modified Date:  17.02.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import inspect
-from typing import Type, Callable
+from typing import Callable
 
 
 class AmpelABC:
 	"""
 	This class resembles python's standart ABC module (Abstract Base Class) but can additionaly
 	check method signatures. As a consequence, a subclass that inherits AmpelABC, will not be able to
 	implement methods declared as abstract by the parent class using different method arguments.
@@ -59,15 +59,15 @@
 
 			if cls._abcheck:
 				cls._check_methods(cls, "abstract_method")
 				cls._check_methods(cls, "default_method")
 
 
 	@staticmethod
-	def _check_methods(Klass: Type, func_attr: str) -> None:
+	def _check_methods(Klass: type, func_attr: str) -> None:
 
 		# Gather abstract methods (marked by the decorator @abstractmethod)
 		abs_methods = {
 			method_name: (base_cls, method)
 			for base_cls in reversed(Klass.mro())
 				for method_name, method in base_cls.__dict__.items()
 					if hasattr(method, func_attr)
```

### Comparing `ampel-interface-0.8a1/ampel/base/AmpelFlexModel.py` & `ampel_interface-0.9.0/ampel/base/AmpelFlexModel.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/base/AmpelFlexModel.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 17.03.2021
-# Last Modified Date: 17.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/base/AmpelFlexModel.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                17.03.2021
+# Last Modified Date:  06.02.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from ampel.base.AmpelBaseModel import AmpelBaseModel
 
 
 class AmpelFlexModel(AmpelBaseModel):
 	"""
 	Allows/Ignores extra kwargs parameters
 	"""
 
 	def __init__(self, **kwargs):
-		super().__init__(**{k: kwargs[k] for k in kwargs if k in self._annots})
+		super().__init__(**{k: kwargs[k] for k in kwargs if k in self.get_model_keys()})
```

### Comparing `ampel-interface-0.8a1/ampel/base/AuxUnitRegister.py` & `ampel_interface-0.9.0/ampel/base/AuxUnitRegister.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,75 +1,81 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/base/AuxUnitRegister.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 17.02.2021
-# Last Modified Date: 05.08.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/base/AuxUnitRegister.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                17.02.2021
+# Last Modified Date:  08.11.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from importlib import import_module
-from typing import Dict, Type, Any, Union, Optional, ClassVar, overload # type: ignore[attr-defined]
+from typing import Any, ClassVar, overload # type: ignore[attr-defined]
 from ampel.types import T, check_class
 from ampel.model.UnitModel import UnitModel
-from ampel.base.AmpelBaseModel import AmpelBaseModel
+from ampel.base.AmpelUnit import AmpelUnit
+from ampel.config.AmpelConfig import AmpelConfig
 
 
 class AuxUnitRegister:
 
 	# References unit definitions of auxiliary units
 	# allows units to load aux units by themselve or
 	# aux units to load other aux units
-	_defs: ClassVar[Dict[str, Any]] = {}
-	_dyn: ClassVar[Dict[str, Any]] = {}
+	_defs: ClassVar[dict[str, Any]] = {}
+	_dyn: ClassVar[dict[str, Any]] = {}
 
 	@classmethod
-	def initialize(cls, defs: Dict[str, Any]) -> None:
-		cls._defs = defs
+	def initialize(cls, config: AmpelConfig) -> None:
+		cls._defs = {
+			k: v for k, v in config.get("unit", ret_type=dict, raise_exc=True).items()
+			if 'ContextUnit' not in v.get('base', []) and 'LogicalUnit' not in v.get('base', [])
+		}
 
 	@overload
 	@classmethod
-	def new_unit(cls, model: UnitModel, *, sub_type: Type[T], **kwargs) -> T:
+	def new_unit(cls, model: UnitModel, *, sub_type: type[T], **kwargs) -> T:
 		...
 	@overload
 	@classmethod
-	def new_unit(cls, model: UnitModel, *, sub_type: None = ..., **kwargs) -> AmpelBaseModel:
+	def new_unit(cls, model: UnitModel, *, sub_type: None = ..., **kwargs) -> AmpelUnit:
 		...
 
 	@classmethod
-	def new_unit(cls,
-		model: UnitModel, *, sub_type: Optional[Type[T]] = None, **kwargs
-	) -> Union[T, AmpelBaseModel]:
-		"""	:raises: ValueError is model.config is not of type Optional[dict] """
+	def new_unit(cls, model: UnitModel, *, sub_type: None | type[T] = None, **kwargs) -> T | AmpelUnit:
+		"""	:raises: ValueError is model.config is not of type None | dict """
 
 		if model.unit in cls._dyn:
 			Klass = cls._dyn[model.unit]
 		else:
 			Klass = cls.get_aux_class(klass=model.unit, sub_type=sub_type)
 
 		if model.config:
 			if isinstance(model.config, dict):
 				return Klass(**(model.config | kwargs)) # type: ignore[call-arg]
 			raise ValueError("Auxiliary units cannot use config aliases")
 
-		return Klass(**kwargs) # type: ignore[call-arg]
+		unit = Klass(**kwargs) # type: ignore[call-arg]
+		if hasattr(unit, "post_init"):
+			unit.post_init() # type: ignore[union-attr]
+
+		return unit
 
 
 	@overload
 	@classmethod
-	def get_aux_class(cls, klass: str, *, sub_type: Type[T]) -> Type[T]:
+	def get_aux_class(cls, klass: str, *, sub_type: type[T]) -> type[T]:
 		...
 
 	@overload
 	@classmethod
-	def get_aux_class(cls, klass: str, *, sub_type: None = ...) -> Type[AmpelBaseModel]:
+	def get_aux_class(cls, klass: str, *, sub_type: None = ...) -> type[AmpelUnit]:
 		...
 
 	@classmethod
-	def get_aux_class(cls, klass: str, *, sub_type: Optional[Type[T]] = None) -> Union[Type[T], Type[AmpelBaseModel]]:
+	def get_aux_class(cls, klass: str, *, sub_type: None | type[T] = None) -> type[T | AmpelUnit]:
 		""" :raises: ValueError if unit is unknown """
 
 		if klass not in cls._defs:
 			if not cls._defs:
 				raise ValueError(
 					f"Unknown auxiliary unit {klass}:"
 					f"- make sure a context is loaded (requirement)\n"
@@ -77,13 +83,13 @@
 			else:
 				raise ValueError(
 					f"Unknown auxiliary unit {klass}:\n"
 					f"- check your ampel conf to see if the unit is properly registered"
 				)
 
 		fqn = cls._defs[klass]['fqn']
-		ret = getattr(import_module(fqn), fqn.split('.')[-1])
+		ret = getattr(import_module(fqn), klass)
 
 		if sub_type:
 			check_class(ret, sub_type)
 
 		return ret
```

### Comparing `ampel-interface-0.8a1/ampel/base/decorator.py` & `ampel_interface-0.9.0/ampel/base/decorator.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/base/decorator.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 27.12.2017
-# Last Modified Date: 17.05.2020
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/base/decorator.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                27.12.2017
+# Last Modified Date:  17.05.2020
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from functools import partial
-from typing import TypeVar, Callable, overload
+from typing import TypeVar, overload
+from collections.abc import Callable
 
 F = TypeVar('F', bound=Callable)
 
 
 @overload
 def abstractmethod(func: F) -> F:
 	...
```

### Comparing `ampel-interface-0.8a1/ampel/cli/AmpelArgumentParser.py` & `ampel_interface-0.9.0/ampel/cli/AmpelArgumentParser.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,26 +1,25 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/cli/AmpelArgumentParser.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 17.03.2021
-# Last Modified Date: 22.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-import textwrap
-from os import environ
-from os.path import isfile
-from typing import Dict, Optional, List, Union, Set, Any, Tuple
+# File:                Ampel-interface/ampel/cli/AmpelArgumentParser.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                17.03.2021
+# Last Modified Date:  20.08.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
+
+import textwrap, os
+from typing import Any
 from ampel.cli.MaybeIntAction import MaybeIntAction
 from ampel.cli.LoadJSONAction import LoadJSONAction
 from ampel.cli.LoadAnyOfAction import LoadAnyOfAction
 from ampel.cli.LoadAllOfAction import LoadAllOfAction
 from argparse import ArgumentParser, _ArgumentGroup
 from ampel.cli.AmpelHelpFormatter import AmpelHelpFormatter
+from ampel.cli.config import get_user_data_config_path
 
 
 class AmpelArgumentParser(ArgumentParser):
 	"""
 	Argument parser with additional features.
 	Supports adding notes and examples.
 
@@ -35,17 +34,17 @@
 		* Arguments requiring at least two values: -parameter # # ...
 		* Arguments requiring a JSON string: -parameter '{#}'
 	- A "notation section" is generated dynamically and added automatically
 	- The arguments column (left) is larger (width of 40 vs 27 for ArgumentParser's default formatter)
 
 	Note:
 	The parameter -config (path to an ampel config file) is automatically moved from the
-	*required* argument group to the *optional* argument group if the environment variable
-	AMPELCONF exists and points to a valid file. In this case, a note is added and
-	"-config ampel_conf.yaml" is stripped out of added examples automatically (deactivable)
+	*required* argument group to the *optional* argument group if an installed config is present.
+	In this case, a note is added and "-config ampel_conf.yaml" is stripped out
+	of added examples automatically (deactivable via option 'auto_strip_config')
 
 	Conveniences methods:
 	- move_group_up: moves a group up in order
 	- create_logic_args: creates 4 arguments for a given name.
 	  For example, parser.create_opt_logic_args("channel", "Channel") will create:
 	  -channel #                 Channel to be matched (non-exclusively)
 	  -channels-or # # ...       Channels to be matched (OR connected)
@@ -56,36 +55,37 @@
 	  so that the calling code should not have to differenciate between these.
 	  Moreover, each generated argument is associated with a dedicated action:
 	  MaybeIntAction, LoadAnyOfAction, LoadAllOfAction and LoadJSONAction in ampel/cli
 
 	See the class ampel.cli.T2Command for an full utilization of this class
 	"""
 
-	def __init__(self, ampel_op: Optional[str] = None, **kwargs) -> None:
+	def __init__(self, ampel_op: None | str = None, **kwargs) -> None:
 
 		super().__init__(formatter_class=AmpelHelpFormatter, **kwargs)
-		self.notes: List[str] = []
-		self.examples: List[str] = []
-		self.args_descr: Dict[str, str] = {}
+		self._notes: list[str] = []
+		self._examples: list[str] = []
+		self.args_descr: dict[str, str] = {}
 		self._logic_ops_note_added = False
-		self.notations: Set[Union[str, Tuple[str, str]]] = set()
+		self.args_not_required = False
+		self.notations: set[str | tuple[str, str]] = set()
 		self.has_env_conf = False
-		self.groups: Dict[str, _ArgumentGroup] = {}
+		self.groups: dict[str, _ArgumentGroup] = {}
 		self.bullet = "\u2022"
 		self.usage = "" # required by argparse (AssertionError), unclear why
 		self._ampel_op = ampel_op
 
 		self.spacer = "  "
 		self.note_open = "["
 		self.note_close = "]"
 		self.ex_open = "|"
 		self.ex_close = "|"
 
 
-		# Pop optional group to reorder it, putting required arguments first (really questionable defaults there...)
+		# Pop optional group to reorder it, putting required arguments first
 		optional_group = self._action_groups.pop()
 
 		# Add a reference by name
 		self.groups["optional"] = optional_group
 
 		# Suppress "-h, --help show this help message and exit" (chicken and egg)
 		# optional._option_string_actions = {}
@@ -96,21 +96,16 @@
 
 		# Add required argument group (first pos)
 		self.groups["required"] = self.add_argument_group('Required arguments')
 
 		# Re-insert optional group
 		self._action_groups.append(optional_group)
 
-		if "AMPELCONF" in environ and environ["AMPELCONF"]:
-			if isfile(environ["AMPELCONF"]):
-				self.has_env_conf = True
-			else:
-				print("\n=================================================================")
-				print("Warning: environment variable AMPELCONF points to an invalid file")
-				print("=================================================================")
+		if os.path.exists(get_user_data_config_path()):
+			self.has_env_conf = True
 
 
 	def set_ampel_sub_op(self, name: str) -> None:
 		self.ampel_sub_op = name
 	
 
 	def set_bullet(self, bullet: str) -> None:
@@ -123,15 +118,15 @@
 		self.groups[name].title = title
 
 
 	def set_group_defaults(self, name: str, **kwargs):
 		self.groups[name].set_defaults(**kwargs)
 
 
-	def add_description(self, descr: Optional[Union[str, List[str]]]) -> None:
+	def add_description(self, descr: None | str | list[str]) -> None:
 
 		if not descr:
 			return
 
 		if isinstance(descr, str):
 			descr = [
 				ell for el in descr.split("\n")
@@ -153,55 +148,72 @@
 	def get_group_index_pos(self, group: _ArgumentGroup) -> int:
 		for i, el in enumerate(self._action_groups):
 			if el == group:
 				return i
 		return -1
 
 
-	def get_group(self, name: str) -> Optional[_ArgumentGroup]:
+	def get_group(self, name: str) -> None | _ArgumentGroup:
 		return self.groups.get(name)
 
 
-	def add_arg(self,
-		name: str, group: Union[str, _ArgumentGroup] = "optional",
-		help: Optional[str] = None, **kwargs
+	def req(self, name: str, help: None | str = None, **kwargs) -> None:
+		self.arg(name, 'required', help, **kwargs)
+
+
+	# For explicity
+	def opt(self, name: str, help: None | str = None, **kwargs) -> None:
+		self.arg(name, 'optional', help, **kwargs)
+
+
+	def arg(self,
+		name: str, group: str | _ArgumentGroup = "optional",
+		help: None | str = None, **kwargs
 	) -> None:
 		"""
 		:param target:
 		Example:
-			- add_arg("verbose", "optional")
-			- add_arg("out", "required")
+			- arg("verbose")
+			- arg("out", "required")
 		"""
 
 		self._auto_metavar(kwargs)
 
 		# Add only the nomemclature elements that are actually used
 		if "const" in kwargs:
-			self.notations.add(("-argument [#]", "Argument with an overridable default value"))
+			self.notations.add(("-option [#]", "Option with an overridable default value"))
 		elif kwargs.get("nargs") == "+":
-			self.notations.add(("-argument # [# ...]", "Argument accepting one or more values"))
+			self.notations.add(("-option # [# ...]", "Option accepting one or more values"))
 		elif isinstance(kwargs.get("action"), str):
-			self.notations.add(("-argument", "Argument without value (flag)"))
+			self.notations.add(("-option", "Option without value (flag)"))
 		else:
-			self.notations.add(("-argument #", "Argument requiring one value"))
+			self.notations.add(("-option #", "Option requiring one value"))
 
 		if name == "config" and group == "required" and self.has_env_conf:
-			self.add_note(f"{environ['AMPELCONF']} will be used unless an override using -config is specified")
+			self.note("Installed config file will be used unless option -config <path> is specified")
 			group = "optional"
 
 		if isinstance(group, str):
 			group = self.groups[group]
 
 		group.add_argument(
 			f"--{name}", help=help or self.args_descr.get(name),
 			required=True if group == self.groups["required"] else False, **kwargs
 		)
 
 
-	def add_x_args(self, group: str = "optional", *args: Dict[str, Any]):
+	def xargs_req(self, *args: dict[str, Any]):
+		return self.xargs('required', *args)
+
+
+	def xargs_opt(self, *args: dict[str, Any]):
+		return self.xargs('optional', *args)
+
+
+	def xargs(self, group: str = "optional", *args: dict[str, Any]):
 		"""
 		Create a mutually exclusive group, attach it to the group defined in 'target'
 		and add arguments to it according to provided definitions (*args)
 		"""
 		self.notation_add_mutual_exclusivity()
 
 		try:
@@ -214,31 +226,31 @@
 					list(self._option_string_actions.keys())[-1]
 				]
 				last_args.help = (last_args.help or "") + "\n\n"
 		except Exception:
 			pass
 		x = self.groups[group].add_mutually_exclusive_group()
 		for arg in args:
-			self.add_arg(group=x, **arg)
+			self.arg(group=x, **arg)
 
 
-	def _auto_metavar(self, kw: Dict) -> None:
+	def _auto_metavar(self, kw: dict) -> None:
 		if "dest" in kw or "metavar" in kw:
 			return
 		if (a := kw.get("action")) and a != MaybeIntAction:
 			return
 		kw['metavar'] = "#"
 
 
-	def set_help_descr(self, args_descr: Dict) -> None:
+	def set_help_descr(self, args_descr: dict) -> None:
 		""" Sets help parameter descriptions """
 		self.args_descr = args_descr
 
 
-	def add_note(self, note: str, pos: Optional[int] = None, ref: Optional[str] = None) -> None:
+	def note(self, note: str, pos: None | int = None, ref: None | str = None) -> None:
 		""" Newlines in note are supported and will be properly formatted """
 
 		notes = note.split("\n")
 		for i in range(len(notes)):
 			if len(notes[i]) > 100:
 				notes[i:i+1] = textwrap.wrap(notes[i], width=100)
 
@@ -252,96 +264,100 @@
 
 		for i, el in enumerate(notes):
 			if i > 0:
 				content += "\n" + " " * len(start)
 			content += el
 
 		if pos is not None:
-			self.notes.insert(pos, content)
+			self._notes.insert(pos, content)
 		else:
-			self.notes.append(content)
+			self._notes.append(content)
 
 
-	def add_notes(self, notes: List[str]) -> None:
+	def notes(self, notes: list[str]) -> None:
 		""" Each note will start with a bullet """
 		for el in notes:
-			self.add_note(el)
+			self.note(el)
 
 
-	def add_example(self,
-		ex: str, prepend="ampel ", append="", auto_strip_config: bool = True,
-		ref: Optional[str] = None
+	def example(self,
+		ex: str,
+		prepend: str = "ampel ",
+		append: str = "",
+		auto_strip_config: bool = True,
+		ref: None | str = None
 	) -> None:
 		if ref:
 			prepend = f"{self.ex_open}{ref}{self.ex_close} {prepend}"
 		payload = f"{self.spacer}{self.bullet} {prepend}{ex}{append}"
 		if auto_strip_config and self.has_env_conf:
-			self.examples.append(payload.replace(" -config ampel_conf.yaml ", " "))
+			self._examples.append(payload.replace(" -config ampel_conf.yaml ", " "))
 		else:
-			self.examples.append(payload)
+			self._examples.append(payload)
 
 
-	def create_logic_args(self,
-		name: str, group: str, descr: str, metavar: str = "#",
-		required: bool = False, pos: Optional[int] = None,
-		ref: Optional[str] = None, excl: bool = False,
-		**kwargs
+	def logic_args(self,
+		base_name: str, group: str, descr: str, metavar: str = "#",
+		required: bool = False, pos: None | int = None,
+		ref: None | str = None, excl: bool = False,
+		json: bool = True, **kwargs
 	) -> None:
 		"""
 		Ex: channel, channels-and, channels-or, channels-json
 		Ex: with-tag, with-tags-and, with-tags-or, with-tags-json
 		"""
 		
 		what = "excluded" if excl else "matched"
-		dest = name.replace("-", "_")
+		dest = base_name.replace("-", "_")
 
 		# Cosmetic
 		if not self._logic_ops_note_added:
 			last_args = self.groups[group]._option_string_actions[
 				list(self._option_string_actions.keys())[-1]
 			]
 			last_args.help = (last_args.help or "") + "\n\n"
 
 		self.notation_add_mutual_exclusivity()
-		self.notations.add(("-argument # # ...", "Argument requiring at least two values"))
+		self.notations.add(("-option # # ...", "Option requiring at least two values"))
 		
 		mux = self.groups[group].add_mutually_exclusive_group(required=required)
 		mux.add_argument(
-			f"--{name}", metavar=metavar,
+			f"--{base_name}", metavar=metavar,
 			type=str, nargs=1, default=None, action=MaybeIntAction,
 			help=f"{descr} to be {what} (non-exclusively)"
 		)
 
 		mux.add_argument(
-			f"--{name}s-or", dest=dest, action=LoadAnyOfAction,
+			f"--{base_name}s-or", dest=dest, action=LoadAnyOfAction,
 			metavar=metavar, type=str, default=None, nargs="+",
 			help=f"{descr}s to be {what} (OR connected)"
 		)
 
 		mux.add_argument(
-			f"--{name}s-and", dest=dest, action=LoadAllOfAction,
+			f"--{base_name}s-and", dest=dest, action=LoadAllOfAction,
 			metavar=metavar, type=str, default=None, nargs="+",
-			help=f"{descr}s to be {what} (AND connected)"
-		)
-
-		suffix = f"{self.note_open}{ref}{self.note_close}" if ref else ""
-		mux.add_argument(
-			f"--{name}s-json", dest=dest, action=LoadJSONAction,
-			metavar=metavar, type=str, default=None,
-			help=f"{descr}s to be {what} {suffix}\n\n"
+			help=f"{descr}s to be {what} (AND connected)" + ("" if json else "\n\n")
 		)
 
-		# Add note about JSON arg
-		if not self._logic_ops_note_added:
-			self.add_note(
-				"Allows the use of logic operators such as:\n" +
-				"Nested logic: \'{\"any_of\": [\"VAL1\", {\"all_of\": [\"VAL2\", \"VAL3\"]}]}\'\n" +
-				"Exclusive match: \'{\"one_of\": [\"VAL1\"]}\'", pos=pos, ref=ref
+		if json:
+			suffix = f"{self.note_open}{ref}{self.note_close}" if ref else ""
+			mux.add_argument(
+				f"--{base_name}s-json", dest=dest, action=LoadJSONAction,
+				metavar=metavar, type=str, default=None,
+				help=f"{descr}s to be {what} {suffix}\n\n"
 			)
-			self._logic_ops_note_added = True
+
+			# Add note about JSON arg
+			if not self._logic_ops_note_added:
+				self.note(
+					"Allows the use of logic operators such as:\n" +
+					"Nested logic: \'{\"any_of\": [\"VAL1\", {\"all_of\": [\"VAL2\", \"VAL3\"]}]}\'\n" +
+					"Exclusive match: \'{\"one_of\": [\"VAL1\"]}\'", pos=pos, ref=ref
+				)
+				self._logic_ops_note_added = True
 
 
 	# Cosmetic
 	def error(self, message: str) -> Any:
 		""" As for now, there is no better way to do this  """
 		if "-" in message:
 			message = message.replace(" --", " -")
@@ -361,33 +377,33 @@
 
 	def notation_add_mutual_exclusivity(self):
 		self.notations.add(
 			f"{self.spacer}Consecutive mutually exclusive arguments are marked with \u22BB"
 		)
 		
 
-	def hint_query_logic(self, pos: Optional[int] = None, ref: Optional[str] = None):
-		self.add_note(
+	def hint_query_logic(self, pos: None | int = None, ref: None | str = None):
+		self.note(
 			"Matching criteria related to different keys are AND-combined with each other",
 			pos, ref
 		)
 
 
-	def hint_time_format(self, pos: Optional[int] = None, ref: Optional[str] = None):
-		self.add_note(
+	def hint_time_format(self, pos: None | int = None, ref: None | str = None):
+		self.note(
 			"Date-time strings are parsed using datetime.fromisoformat(<value>).\n" +
 			"Example of supported formats (unexhaustive): 2011-11-04 or 2011-11-04T00:05:23",
 			pos, ref
 		)
 
 
-	def hint_config_override(self, pos: Optional[int] = None, ref: Optional[str] = None):
-		self.add_note(
+	def hint_config_override(self, pos: None | int = None, ref: None | str = None):
+		self.note(
 			"Any existing config parameter can be overriden using -path.to.config.key value\n" +
-			"Example: -db.prefix AmpelTest",
+			"Example: -mongo.prefix AmpelTest",
 			pos, ref
 		)
 
 
 	def print_help(self,  # type: ignore[override]
 		show_description: bool = True,
 		show_usage: bool = True,
@@ -399,35 +415,37 @@
 
 		if show_description and self.description:
 			print("\nOperation:\n" + self.description)
 
 		if show_usage:
 			print("\nUsage:")
 			sub_op = getattr(self, "ampel_sub_op", None) # ex: show
+			remainder = [el.dest for el in self._actions if el.nargs == '...']
+			rs = f"{remainder[0]}, ..." if remainder else ""
 			if self._ampel_op:
 				if sub_op: # "ampel log show"
-					print(f"{self.spacer}ampel {self._ampel_op} {sub_op} <arguments>")
+					print(f"{self.spacer}ampel {self._ampel_op} {sub_op} <options> {rs}")
 				else: # "ampel run" (No sub-op/action defined)
-					print(f"{self.spacer}ampel {self._ampel_op} <arguments>")
+					print(f"{self.spacer}ampel {self._ampel_op} <options> {rs}")
 			else: # "ampel"
-				print(f"{self.spacer}ampel <operation> <arguments>")
+				print(f"{self.spacer}ampel \033[1m\033[36m<operation>\033[0m <options> {rs}")
 
 		# Core (arguments) help section
 		formatter = self._get_formatter()
 		for action_group in self._action_groups:
 			formatter.start_section(action_group.title)
 			formatter.add_text(action_group.description)
 			formatter.add_arguments(action_group._group_actions)
 			formatter.end_section()
 
 		fh = formatter.format_help()
 
 		# Cosmetic: use numbers for references
-		fh = self._numerate(fh, self.notes, self.note_open, self.note_close)
-		fh = self._numerate(fh, self.examples, self.ex_open, self.ex_open)
+		fh = self._numerate(fh, self._notes, self.note_open, self.note_close)
+		fh = self._numerate(fh, self._examples, self.ex_open, self.ex_open)
 
 		if show_notation and self.notations:
 			cw = getattr(formatter, "_action_max_length", 30) # col width
 			print("\nNotation:")
 			if (x := sorted([v for v in self.notations if isinstance(v, str)], key=lambda x: len(x))):
 				print("\n".join(x) + "\n")
 			raw_not = sorted(
@@ -435,37 +453,37 @@
 				key=lambda x: len(x[0])
 			)
 			print("\n".join([self._format(v[0], v[1], cw) for v in raw_not]))
 
 		if show_arguments:
 			print("\n" + fh, end="")
 
-		if show_notes and self.notes:
+		if show_notes and self._notes:
 			# Put numerated notes first
-			print("\nNote%s:" % ("s" if len(self.notes) > 1 else ""))
-			print("\n".join(self._sort(self.notes)))
+			print("\nNote%s:" % ("s" if len(self._notes) > 1 else ""))
+			print("\n".join(self._sort(self._notes)))
 
-		if show_examples and self.examples:
-			print("\nExample%s:" % ("s" if len(self.examples) > 1 else ""))
-			print("\n".join(self._sort(self.examples)) + "\n")
+		if show_examples and self._examples:
+			print("\nExample%s:" % ("s" if len(self._examples) > 1 else ""))
+			print("\n".join(self._sort(self._examples)) + "\n")
 
 		if self.epilog:
 			print(self.epilog.strip())
 
 		print("")
 
 
 	def _format(self, k: str, v: str, l: int) -> str:
 		filler = (l - len(k) - 1) * " "
 		return self.spacer + k + filler + v
 
 
-	def _numerate(self, fh: str, target: List[Any], open_key: str, close_key: str) -> str:
+	def _numerate(self, fh: str, target: list[Any], open_key: str, close_key: str) -> str:
 		try:
-			l: List[str] = []
+			l: list[str] = []
 			y = 1
 			for i, el in enumerate(target):
 				if isinstance(el, str) and el[4] == open_key:
 					l.append(el[5])
 					target[i] = el[:5] + str(y) + el[6:]
 					y += 1
 			for i, el in enumerate(l, 1):
@@ -474,29 +492,29 @@
 					open_key + str(i) + close_key
 				)
 		except Exception:
 			pass
 
 		return fh
 
-	def _sort(self, target: List[Any]) -> List[str]:
+	def _sort(self, target: list[Any]) -> list[str]:
 		""" # Put numerated notes/examples first. If not notes, then examples """
 		opn = self.note_open if target == self.notes else self.ex_open
 		return [el for el in target if el[4] == opn] + \
 			[el for el in target if el[4] != opn]
 
 
 	@classmethod
 	def build_choice_help(cls,
-		op: str, sub_ops: List[str], hlp: Dict[str, str],
-		description: Optional[str] = None
+		op: str, sub_ops: list[str], hlp: dict[str, str],
+		description: None | str = None
 	) -> 'AmpelArgumentParser':
 
 		parser = AmpelArgumentParser(ampel_op=op)
-		parser.set_ampel_sub_op("<action>")
+		parser.set_ampel_sub_op('\033[1m\033[36m<action>\033[0m')
 
 		if description:
 			parser.add_description(description)
 
 		sp_action = parser.add_subparsers(parser_class=cls)
 		parser._action_groups[0].title = "Actions"
```

### Comparing `ampel-interface-0.8a1/ampel/cli/ArgParserBuilder.py` & `ampel_interface-0.9.0/ampel/cli/ArgParserBuilder.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,247 +1,226 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/cli/ArgParserBuilder.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 17.03.2021
-# Last Modified Date: 23.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/cli/ArgParserBuilder.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                17.03.2021
+# Last Modified Date:  20.08.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Dict, Optional, List, Union, Any, Tuple
+from typing import Any
 from ampel.cli.AmpelArgumentParser import AmpelArgumentParser
 
 
 class ArgParserBuilder:
 	"""
 	Creates one or many instances of AmpelArgumentParser
 	"""
 
-	def __init__(self, op: Optional[str] = None) -> None:
+	def __init__(self, op: None | str = None) -> None:
 		"""
 		"""
-		self.parsers: Dict[str, AmpelArgumentParser] = {}
+		self.parsers: dict[str, AmpelArgumentParser] = {}
 		self._op = op
 
 
-	def add_parser(self, name: str, hlp: Dict[str, str]):
-		self.parsers[name] = AmpelArgumentParser(ampel_op=self._op)
-		self.parsers[name].set_help_descr(hlp)
-		setattr(self.parsers[name], '_sub_op', name)
+	def add_parser(self, name: str, hlp: dict[str, str]) -> AmpelArgumentParser:
+		parser = AmpelArgumentParser(ampel_op=self._op)
+		parser.set_help_descr(hlp)
+		setattr(parser, '_sub_op', name)
+		self.parsers[name] = parser
+		return parser
 
 
-	def add_parsers(self, names: List[str], hlp: Dict[str, str]):
-		for el in names:
-			self.add_parser(el, hlp)
+	def add_parsers(self, names: list[str], hlp: dict[str, str]) -> list[AmpelArgumentParser]:
+		return [self.add_parser(el, hlp) for el in names]
 
 
-	def get(self) -> Dict[str, AmpelArgumentParser]:
+	def get(self) -> dict[str, AmpelArgumentParser]:
 		""" Returns parsers created during the build procedure """
 		return self.parsers
 
 
-	def add_group(self, target: str, title: str, **kwargs):
+	def add_group(self, group: str, title: str, sub_ops: str, **kwargs):
 		"""
-		:param target: see add_arg(...) docstring
+		:param sub_ops: see arg(...) docstring
 		"""
-		parsers, group = self.get_targets(target, False)
-		for p in parsers:
+		for p in self.get_parsers(sub_ops):
 			p.groups[group] = p.add_argument_group(group, **kwargs)
 			p.groups[group].title = title
 
 
-	def set_group_defaults(self, target: str, **kwargs):
+	def set_group_defaults(self, group: str, sub_ops: str, **kwargs):
 		"""
-		:param target: see add_arg(...) docstring
+		:param sub_ops: see arg(...) docstring
 		"""
-		parsers, group = self.get_targets(target, True)
-		for p in parsers:
+		for p in self.get_parsers(sub_ops):
 			p.groups[group].set_defaults(**kwargs)
 
 
-	def add_description(self, target: str, descr: Optional[Union[str, List[str]]]) -> None:
+	def description(self, descr: None | str | list[str], sub_ops: str) -> None:
 		"""
 		Calls method 'add_description' (see AmpelArgumentParser docstring) for the selected parser(s).
-		:param target: see add_arg(...) docstring
+		:param sub_ops: see arg(...) docstring
 		"""
 
-		parsers, _ = self.get_targets(target, False)
-		for p in parsers:
+		for p in self.get_parsers(sub_ops):
 			p.add_description(descr)
 
 
-	def add_arg(self, target: str, name: str, **kwargs):
+	def opt(self, opt_name: str, sub_ops: str = 'all', **kwargs):
+		return self.arg(opt_name, 'optional', sub_ops, **kwargs)
+
+
+	def req(self, opt_name: str, sub_ops: str = 'all', **kwargs):
+		return self.arg(opt_name, 'required', sub_ops, **kwargs)
+
+
+	def arg(self, opt_name: str, group: str, sub_ops: str = 'all', **kwargs):
 		"""
-		:param target:
-		- str:
-			ex: add_arg('optional', 'verbose')
-			Adds the argument to the provided group ('target' value) of all underlying parsers.
-			For example, if two sub-parsers exist (say one for operation 'show' and one for 'write'),
-			both subparsers will feature the argument 'verbose'
-		- str.str:
-			ex: add_arg('write.required', 'out-file')
-			The first part of the string, delimited by '.', targets a sub-parser by name.
-			The second part targets an argument group (by name) of the specified subparser(s).
-			In the example above, the argument 'out-file' will be added to the group
-			with name 'required' of sub-parser with name 'write'.
-		- all.str:
-			ex: add_arg('all.required', 'out-file'). Same as the first case (str), only explicit
-		- str|str.str:
-			ex: add_arg('write|show|tail.optional', 'to-json')
-			Multiple sub-parsers can be targeted using '|'.
-			In the example above, the argument 'to-json' will be added to the
-			argument group 'optional' of the sub-parser of the 'write', 'show' and 'tail' sub-operations
-		"""
-
-		parsers, group = self.get_targets(target, True)
-		for p in parsers:
-			p.add_arg(name, group, **kwargs)
-
-
-	def add_x_args(self, target: str, *args: Dict[str, Any]) -> None:
-		"""
-		Calls method 'add_x_args' (see AmpelArgumentParser docstring) for the selected parser(s).
-		:param target: see add_arg(...) docstring
-		"""
-		parsers, group = self.get_targets(target, True)
-		for p in parsers:
-			p.add_x_args(group, *args)
-
-
-	def get_targets(self, target: str, check_group: bool = True) -> Tuple[List[AmpelArgumentParser], str]:
-		"""
-		:param target: see add_arg(...) docstring
-		"""
-		if "." in target:
-			sp = target.split(".")
-			parsers = self._get_parsers(sp[0])
-			group = sp[1]
-		else:
-			parsers = self._get_parsers("all")
-			group = target
+		:param name: option name
+		:param group: group name. Multiple sub-parsers can be targeted using '|'.
+		If no is specified, option will be added to all existing subparsers.
+		Ex: arg('to-json', 'show|export|tail')
+		"""
+		for p in self.get_parsers(sub_ops):
+			p.arg(opt_name, group, **kwargs)
 
-		if check_group:
-			for p in parsers:
-				if group not in p.groups:
-					raise ValueError(
-						f"Group '{group}' unknown in parser with name "
-						f"\'{getattr(p, '_sub_op')}\', please create it first\n"
-					)
 
-		return parsers, group
+	def xargs(self, group: str, sub_ops: str, xargs: list[dict[str, Any]]) -> None:
+		"""
+		Calls method 'x_args' (see AmpelArgumentParser docstring) for the selected parser(s).
+		:param sub_ops: see arg(...) docstring
+		"""
+		for p in self.get_parsers(sub_ops):
+			p.xargs(group, *xargs)
 
 
-	def _get_parsers(self, arg: str) -> List[AmpelArgumentParser]:
+	def get_parsers(self, sub_ops: str = 'all') -> list[AmpelArgumentParser]:
 		"""
-		:param arg: string containing one or more parser names.
-		Multiple parser names mst be separated by the character "|".
-		Unlike parameter 'target' of add_arg(...), not dot ('.') can be used with 'arg'.
+		:param sub_ops: string containing one or more parser names.
+		Multiple parsers can be retrieved using the separating character "|".
 		"""
 
-		if "|" in arg:
-			pp = arg.split("|")
+		if "|" in sub_ops:
+			pp = sub_ops.split("|")
 			for el in pp:
 				if el not in self.parsers:
 					raise ValueError(f"Unknown parser: '{el}', please create it using add_parser")
 
-			ret1: List[AmpelArgumentParser] = [
+			ret1: list[AmpelArgumentParser] = [
 				v for k, v in self.parsers.items()
 				if k in pp
 			]
 
-		elif arg == "all":
+		elif sub_ops == "all":
 			ret1 = list(self.parsers.values())
 
 		else:
-			if arg not in self.parsers:
-				raise ValueError(f"Unknown parser: '{arg}', please create it using add_parser")
-			ret1 = [self.parsers[arg]]
+			if sub_ops not in self.parsers:
+				raise ValueError(f"Unknown parser: '{sub_ops}', please create it using add_parser")
+			ret1 = [self.parsers[sub_ops]]
 
 		return ret1
 
 
-	def create_logic_args(self,
-		target: str, name: str, descr: str, metavar: str = "#",
-		required: bool = False, pos: Optional[int] = None,
-		ref: Optional[str] = None, excl: bool = False,
-		**kwargs
+	def logic_args(self,
+		base_name: str,
+		descr: str,
+		group: str,
+		sub_ops: str = 'all',
+		metavar: str = "#",
+		required: bool = False,
+		pos: None | int = None,
+		ref: None | str = None,
+		excl: bool = False,
+		json: bool = True, **kwargs
 	) -> None:
 		"""
 		Calls method 'create_logic_args' (see AmpelArgumentParser docstring) for the selected parser(s).
-		:param target: see add_arg() docstring
+		:param sub_ops: see arg() docstring
 		"""
-		parsers, group = self.get_targets(target, True)
-		for p in parsers:
-			p.create_logic_args(name, group, descr, metavar, required, pos, ref, excl)
+		for p in self.get_parsers(sub_ops):
+			p.logic_args(base_name, group, descr, metavar, required, pos, ref, excl, json)
 
 
-	def add_note(self, parsers: str, note: str, pos: Optional[int] = None, ref: Optional[str] = None) -> None:
-		"""
-		Calls method 'add_note' (see AmpelArgumentParser docstring) for the selected parser(s).
-		:param parsers: see _get_parsers() docstring
-		"""
-		for p in self._get_parsers(parsers):
-			p.add_note(note, pos, ref)
+	def logic_args_opt(self,
+		base_name: str, descr: str, sub_ops: str = 'all', metavar: str = "#", required: bool = False,
+		pos: None | int = None, ref: None | str = None, excl: bool = False, json: bool = True, **kwargs
+	) -> None:
+		self.logic_args(
+			base_name, descr, "optional", sub_ops, metavar, required,
+			pos, ref, excl, json, **kwargs
+		)
 
 
-	def add_all_note(self, note: str, pos: Optional[int] = None, ref: Optional[str] = None) -> None:
+	def logic_args_req(self,
+		base_name: str, descr: str, sub_ops: str = 'all', metavar: str = "#", required: bool = False,
+		pos: None | int = None, ref: None | str = None, excl: bool = False, json: bool = True, **kwargs
+	) -> None:
+		self.logic_args(
+			base_name, descr, "required", sub_ops, metavar, required,
+			pos, ref, excl, json, **kwargs
+		)
+
+
+	def note(self,
+		note: str,
+		sub_ops: str = 'all',
+		pos: None | int = None,
+		ref: None | str = None
+	) -> None:
 		"""
-		Calls method 'add_note' (see AmpelArgumentParser docstring) of all the underlying parsers.
+		Calls method 'note' (see AmpelArgumentParser docstring) for the selected parser(s).
+		:param parsers: see _get_parsers() docstring
 		"""
-		for p in self.parsers.values():
-			p.add_note(note, pos, ref)
+		for p in self.get_parsers(sub_ops):
+			p.note(note, pos, ref)
 
 
-	def add_example(self,
-		parsers: str, ex: str, prepend=None, append="",
-		auto_strip: bool = True, ref: Optional[str] = None
+	def example(self,
+		sub_ops: str,
+		ex: str,
+		prepend = None,
+		append="",
+		auto_strip: bool = True, ref: None | str = None
 	) -> None:
 		"""
-		Calls method 'add_example' (see AmpelArgumentParser docstring) for the selected parser(s).
+		Calls method 'example' (see AmpelArgumentParser docstring) for the selected parser(s).
 		:param parsers: see _get_parsers() docstring
 		"""
-		for p in self._get_parsers(parsers):
-			p.add_example(
+		for p in self.get_parsers(sub_ops):
+			p.example(
 				ex,
 				prepend or f"ampel {self._op or ''} {getattr(p, '_sub_op', '')} ",
 				append, auto_strip, ref
 			)
 
 
-	def add_all_example(self,
-		ex: str, prepend="ampel ", append="", auto_strip: bool = True, ref: Optional[str] = None
-	) -> None:
-		"""
-		Calls method 'add_example' (see AmpelArgumentParser docstring) of all the underlying parsers.
-		"""
-		for p in self.parsers.values():
-			p.add_example(ex, prepend, append, auto_strip, ref)
-
-
-	def hint_query_logic(self, parsers: str, pos: Optional[int] = None, ref: Optional[str] = None):
-		for p in self._get_parsers(parsers):
+	def hint_query_logic(self, sub_op: str, pos: None | int = None, ref: None | str = None):
+		for p in self.get_parsers(sub_op):
 			p.hint_query_logic(pos, ref)
 
 
-	def hint_all_query_logic(self, pos: Optional[int] = None, ref: Optional[str] = None):
+	def hint_all_query_logic(self, pos: None | int = None, ref: None | str = None):
 		for p in self.parsers.values():
 			p.hint_query_logic(pos, ref)
 
 
-	def hint_time_format(self, parsers: str, pos: Optional[int] = None, ref: Optional[str] = None):
-		for p in self._get_parsers(parsers):
+	def hint_time_format(self, sub_ops: str, pos: None | int = None, ref: None | str = None):
+		for p in self.get_parsers(sub_ops):
 			p.hint_time_format(pos, ref)
 
 
-	def hint_all_time_format(self, pos: Optional[int] = None, ref: Optional[str] = None):
+	def hint_all_time_format(self, pos: None | int = None, ref: None | str = None):
 		for p in self.parsers.values():
 			p.hint_time_format(pos, ref)
 
 
-	def hint_all_config_override(self, pos: Optional[int] = None, ref: Optional[str] = None):
+	def hint_all_config_override(self, pos: None | int = None, ref: None | str = None):
 		for p in self.parsers.values():
 			p.hint_config_override(pos, ref)
 
 
 	def notation_add_note_references(self):
 		for p in self.parsers.values():
 			p.notation_add_note_references()
```

### Comparing `ampel-interface-0.8a1/ampel/cli/LoadAllOfAction.py` & `ampel_interface-0.9.0/ampel/cli/LoadAnyOfAction.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/cli/LoadAllOfAction.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 18.03.2021
-# Last Modified Date: 18.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/cli/LoadAnyOfAction.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                18.03.2021
+# Last Modified Date:  22.10.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from argparse import Action
-from ampel.model.operator.AllOf import AllOf
+from ampel.model.operator.AnyOf import AnyOf
 
-class LoadAllOfAction(Action):
+class LoadAnyOfAction(Action):
 
 	def __call__(self, parser, namespace, values, option_string=None):
 
 		v = [
 			int(el) if el.lstrip("-+").isdigit() else el
 			for el in values
 		]
 
-		if len(v) == 1:
-			v = [0]
-
-		setattr(namespace, self.dest, AllOf(all_of = v))
+		setattr(
+			namespace,
+			self.dest,
+			v[0] if len(v) == 1 else AnyOf(any_of = v)
+		)
```

### Comparing `ampel-interface-0.8a1/ampel/config/AmpelConfig.py` & `ampel_interface-0.9.0/ampel/config/AmpelConfig.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,121 +1,122 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/config/AmpelConfig.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 22.10.2019
-# Last Modified Date: 04.08.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/config/AmpelConfig.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                22.10.2019
+# Last Modified Date:  04.08.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import yaml, json
-from typing import Dict, List, Union, Optional, Type, Literal, Any, TypeVar, overload, get_origin
+from typing import Sequence, Union, Literal, Any, TypeVar, overload, get_origin
 from ampel.util.freeze import recursive_freeze
+from ampel.util.mappings import try_int
 from ampel.view.ReadOnlyDict import ReadOnlyDict
 
-UJson = Union[None, str, int, float, bool, List[Any], Dict[str, Any]]
-JT = TypeVar('JT', None, str, int, float, bool, bytes, List[Any], Dict[str, Any])
+UJson = Union[None, str, int, float, bool, list[Any], dict[str, Any]]
+JT = TypeVar('JT', None, str, int, float, bool, bytes, list[Any], dict[str, Any])
 
 
 class AmpelConfig:
 	"""Container for the central Ampel configuration"""
 
-	_config: Dict
+	_config: dict
 	_check_types: int = 1
 
 
 	@classmethod
 	def load(cls, config_file_path: str, freeze: bool = True) -> 'AmpelConfig':
 		with open(config_file_path, "r") as f:
-			return cls(yaml.safe_load(f), freeze)
+			config = yaml.safe_load(f)
+		# Convert potentially stringified int keys (JSON compatibility) back to int
+		for s in ('channel', 'confid'):
+			for k in list(config[s]):
+				config[s][try_int(k)] = config[s].pop(k)
+		return cls(config, freeze)
 
 
-	def __init__(self, config: Dict, freeze: bool = False) -> None:
+	def __init__(self, config: dict, freeze: bool = False) -> None:
 		"""
 		:raises: ValueError if provided config is None or empty
 		"""
 		if config is None or not config:
 			raise ValueError("Please provide a config")
 
-		# Convert potentially stringified int keys (JSON compatibility) back to int
-		for s in ('channel', 'confid'):
-			for k in [el for el in config[s].keys() if isinstance(el, str) and el.isdigit()]:
-				config[s][int(k)] = config[s].pop(k)
-
-		self._config: Dict = recursive_freeze(config) if freeze else config
+		self._config: dict = recursive_freeze(config) if freeze else config
 
 		if 'general' in config and 'check_types' in config['general']:
 			self._check_types = config['general']['check_types']
 
 	# Overloads for method call without 'entry'
 
 	@overload
-	def get(self) -> Dict[str, Any]:
+	def get(self) -> dict[str, Any]:
 		""" config.get() """
 
 	@overload
-	def get(self, entry: None) -> Dict[str, Any]:
+	def get(self, entry: None) -> dict[str, Any]:
 		""" config.get(None) """
 
 	@overload
-	def get(self, entry: None, ret_type: Any) -> Dict[str, Any]:
+	def get(self, entry: None, ret_type: Any) -> dict[str, Any]:
 		""" config.get(None, None/dict) """
 
 	@overload
-	def get(self, entry: None, ret_type: Any, *, raise_exc: bool) -> Dict[str, Any]:
+	def get(self, entry: None, ret_type: Any, *, raise_exc: bool) -> dict[str, Any]:
 		""" config.get(None, None/dict, raise_exc=True/False) """
 
 	@overload
-	def get(self, entry: None, *, raise_exc: bool) -> Dict[str, Any]:
+	def get(self, entry: None, *, raise_exc: bool) -> dict[str, Any]:
 		""" config.get(None, raise_exc=True/False) """
 
 
 	# Overloads for method call with 'entry' but without return type
 
 	@overload
-	def get(self, entry: Union[str, List[str]]) -> UJson:
+	def get(self, entry: str | int | Sequence[str | int]) -> UJson:
 		""" config.get('logging') """
 
 	@overload
-	def get(self, entry: Union[str, List[str]], ret_type: None) -> UJson:
+	def get(self, entry: str | int | Sequence[str | int], ret_type: None) -> UJson:
 		""" config.get('logging', None) """
 
 	@overload
-	def get(self, entry: Union[str, List[str]], *, raise_exc: bool) -> UJson:
+	def get(self, entry: str | int | Sequence[str | int], *, raise_exc: bool) -> UJson:
 		""" config.get('logging', raise_exc=False/True) """
 
 	@overload
-	def get(self, entry: Union[str, List[str]], ret_type: None, *, raise_exc: bool) -> UJson:
+	def get(self, entry: str | int | Sequence[str | int], ret_type: None, *, raise_exc: bool) -> UJson:
 		""" config.get('logging', None, raise_exc=False/True) """
 
 
 	# Overloads for method call with 'entry' and return type
 
 	@overload
-	def get(self, entry: Union[str, List[str]], ret_type: Type[JT]) -> Optional[JT]:
+	def get(self, entry: str | int | Sequence[str | int], ret_type: type[JT]) -> None | JT:
 		""" config.get('logging', dict) """
 
 	@overload
-	def get(self, entry: Union[str, List[str]], ret_type: Type[JT], *, raise_exc: Literal[False]) -> Optional[JT]:
+	def get(self, entry: str | int | Sequence[str | int], ret_type: type[JT], *, raise_exc: Literal[False]) -> None | JT:
 		""" config.get('logging', dict, raise_exc=False) """
 
 	@overload
-	def get(self, entry: Union[str, List[str]], ret_type: Type[JT], *, raise_exc: Literal[True]) -> JT:
+	def get(self, entry: str | int | Sequence[str | int], ret_type: type[JT], *, raise_exc: Literal[True]) -> JT:
 		""" config.get('logging', dict, raise_exc=True) """
 
 
 	def get(self, # type: ignore[misc]
-		entry: Optional[Union[str, List[str]]] = None,
-		ret_type: Optional[Type[JT]] = None,
+		entry: None | str | int | Sequence[str | int] = None,
+		ret_type: None | type[JT] = None,
 		*, raise_exc: bool = False
-	) -> Union[UJson, Optional[JT]]:
+	) -> UJson | None | JT:
 		"""
 		Optional arguments:
 		
-		:param ret_type: expected return type (str, int, Dict, List, ...).
+		:param ret_type: expected return type (str, int, dict, list, ...).
 		:param entry: sub-config element will be returned.
 		
 		Examples::
 			
 			get("channel.HU_RANDOM")
 		
 		::
@@ -130,18 +131,18 @@
 
 		if isinstance(entry, str):
 			entry = entry.split(".")
 
 		ret = self._config # pointer
 
 		# Integerizes int path elements encoded as str
-		for el in [(el if not el.isdigit() else int(el)) for el in entry]:
+		for el in [entry] if isinstance(entry, int) else (try_int(el) for el in entry):
 			if el not in ret:
 				if raise_exc:
-					raise ValueError(f'Config element \'{".".join(entry)}\' not found')
+					raise ValueError(f'Config element {repr(entry)} not found')
 				return None
 			ret = ret[el]
 
 		if ret_type:
 
 			if origin := get_origin(ret_type):
 				ret_type = origin
@@ -152,24 +153,24 @@
 					f"Expected: {ret_type}\n"
 					f"Found: {type(ret)}"
 				)
 
 		return ret
 
 
-	def get_conf_id(self, conf_id: int) -> Dict[str, Any]:
+	def get_conf_id(self, conf_id: int) -> dict[str, Any]:
 
 		if conf_id not in self._config['confid']:
 			raise ValueError(f"Config with id {conf_id} not found")
 
 		return self._config['confid'][conf_id]
 
 
 	def print(self,
-		entry: Optional[str] = None, format: Literal['json', 'yaml'] = 'yaml'
+		entry: None | str = None, format: Literal['json', 'yaml'] = 'yaml'
 	) -> None:
 
 		out = self.get(entry)
 		print(
 			yaml.dump(out) if format == 'yaml'
 			else json.dumps(out, indent=4)
 		)
```

### Comparing `ampel-interface-0.8a1/ampel/content/JournalRecord.py` & `ampel_interface-0.9.0/ampel/content/JournalRecord.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,49 +1,59 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/content/JournalRecord.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 12.12.2019
-# Last Modified Date: 22.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/content/JournalRecord.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                12.12.2019
+# Last Modified Date:  05.09.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Sequence, Union, Literal, Any, Dict, TypedDict
+from typing import Literal, Any, TypedDict
+from collections.abc import Sequence
 from ampel.types import ChannelId, Tag
 
 
 class JournalRecord(TypedDict, total=False):
 	"""
 	A record of activity on a stock document.
 
 	.. seealso:: :class:`~ampel.struct.JournalAttributes.JournalAttributes`
 	"""
 
 	#: Tier of the associated process
 	tier: Literal[-1, 0, 1, 2, 3]
 
 	#: UNIX epoch of the activity
-	ts: Union[int, float]
+	ts: int | float
 
 	#: Channels associated with the activity
-	channel: Union[ChannelId, Sequence[ChannelId]]
+	channel: ChannelId | Sequence[ChannelId]
 
 	#: Name of the associated process
-	process: Union[int, str]
+	process: int | str
 
 	#: Free-form labels
-	tag: Union[Tag, Sequence[Tag]]
+	tag: Tag | Sequence[Tag]
 
 	#: Run(s) associated with this record
 	run: int
 
 	#: Status code of the associated process
 	code: int
 
+	#: Action code(s) built from :class:`~ampel.enum.JournalActionCode.JournalActionCode`
+	action: int
+
 	#: Duration of the process
-	duration: Union[int, float]
+	duration: int | float
 
 	#: Trace ids
-	traceid: Dict[str, int]
+	traceid: dict[str, int]
+
+	#: id of the unit associated with this record
+	unit: int | str
+
+	#: id of the document associated with the invocation
+	doc: int | bytes
 
 	#: Free-form information
-	extra: Dict[str, Any]
+	extra: dict[str, Any]
```

### Comparing `ampel-interface-0.8a1/ampel/content/LogDocument.py` & `ampel_interface-0.9.0/ampel/content/LogDocument.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,35 +1,32 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/content/LogDocument.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 14.02.2020
-# Last Modified Date: 16.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-import sys
-if sys.version_info.minor > 8:
-	from typing import TypedDict
-else:
-	from typing_extensions import TypedDict
-from typing import Sequence, Union, Any, Dict
+# File:                Ampel-interface/ampel/content/LogDocument.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                14.02.2020
+# Last Modified Date:  15.12.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
+
+from typing import Any, TypedDict
+from typing_extensions import Required
+from collections.abc import Sequence
 from ampel.types import ChannelId, StockId
 
 
 class ChannelLogEntry(TypedDict):
 	"""
 	Abbreviations:
 	s: stock, a: alert, f: flag, r: run, m: msg, c: channel
 
 	Used to save multiple channel specific messages into a single LogDocument
 	Example of a LogDocument embedding two ChannelLogEntry entries: {
 		"_id" : ObjectId("5be4aa6254048041edbac352"),
-		"s" : NumberLong(1810101032122523),
-		"a" : NumberLong(404105201415015004),
+		"s" : 1810101032122523,
+		"a" : 404105201415015004,
 		"f" : 572784643,
 		"r" : 509,
 		"m" : [
 			{"c" : "NO_FILTER", "m": "Alert accepted"},
 			{"c" : "HU_RANDOM", "m": "Alert accepted"},
 		]
 	}
@@ -57,23 +54,29 @@
 	}
 	"""
 
 	#: database key
 	_id: bytes
 
 	#: flag
-	f: int
+	f: Required[int]
 
 	#: run id
-	r: Union[int, Sequence[int]]
+	r: Required[int | Sequence[int]]
 
 	#: msg
-	m: Union[str, Sequence[str], ChannelLogEntry]
+	m: str | Sequence[str] | ChannelLogEntry
 
 	#: stock
-	s: Union[StockId, Sequence[StockId]]
+	s: StockId | Sequence[StockId]
 
 	#: channel
-	c: Union[ChannelId, Sequence[ChannelId]]
+	c: ChannelId | Sequence[ChannelId]
+
+	#: unit
+	u: str
 
 	#: extra
-	e: Dict[str, Any]
+	x: dict[str, Any]
+
+	#: file:line_number (set DBLoggingHanlder.log_provenance to True)
+	p: tuple[str, int]
```

### Comparing `ampel-interface-0.8a1/ampel/content/StockDocument.py` & `ampel_interface-0.9.0/ampel/content/StockDocument.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/content/StockDocument.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 28.12.2019
-# Last Modified Date: 05.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/content/StockDocument.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                28.12.2019
+# Last Modified Date:  05.05.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Any, Sequence, Union, Dict, TypedDict, Literal
+from typing import Any, TypedDict, Literal
+from collections.abc import Sequence
 from ampel.types import StockId, ChannelId, Tag
 from ampel.content.JournalRecord import JournalRecord
 
 
 class StockDocument(TypedDict, total=False):
 	"""
 	The stock record ties together data from various sources, selected by
@@ -35,17 +36,17 @@
 	#: Channels asscoiated with this stock
 	channel: Sequence[ChannelId]
 
 	#: Records of activity
 	journal: Sequence[JournalRecord]
 
 	#: Creation time (UNIX epoch) in each channel
-	ts: Dict[ChannelId, Dict[Literal['tied', 'upd'], float]]
+	ts: dict[ChannelId, dict[Literal['tied', 'upd'], float]]
 
 	#: Last update time for any channel
-	updated: Union[int, float]
+	updated: int | float
 
 	#: External name(s) associated with the stock
-	name: Sequence[Union[int, str]]
+	name: Sequence[int | str]
 
 	#: Optional specific content
-	body: Dict[str, Any]
+	body: dict[str, Any]
```

### Comparing `ampel-interface-0.8a1/ampel/content/T1Document.py` & `ampel_interface-0.9.0/ampel/content/T1Document.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,17 +1,19 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/content/T1Document.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : Unspecified
-# Last Modified Date: 17.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-from typing import Sequence, Literal, Union, TypedDict
+# File:                Ampel-interface/ampel/content/T1Document.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                Unspecified
+# Last Modified Date:  25.06.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
+
+from typing import Literal, TypedDict
+from typing_extensions import Required
+from collections.abc import Sequence
 from ampel.types import UBson, StockId, DataPointId, ChannelId, Tag, UnitId
 from ampel.content.MetaRecord import MetaRecord
 
 
 class T1Document(TypedDict, total=False):
 	"""
 	A symbolic collection of :class:`~ampel.content.DataPoint.DataPoint`,
@@ -24,35 +26,32 @@
 	#: Name of AbsT1ComputeUnit potentially associated with this doc
 	unit: UnitId
 
 	#: Optional hashed config of t1 unit
 	config: int
 
 	#: stock(s) this doc is associated to
-	stock: Union[StockId, Sequence[StockId]]
+	stock: Required[StockId | Sequence[StockId]]
 
 	#: Optional instrument/source identifier
 	origin: int
 
 	#: Result of AbsT1CombineUnit units
-	dps: Sequence[DataPointId]
+	dps: Required[Sequence[DataPointId]]
 
 	#: intger hash hash of dps (referenced by stated T2 units)
-	link: int
+	link: Required[int]
 
-	#: channel(s) associated with this doc
-	channel: Sequence[ChannelId]
+	#: visible by any projection (not channel bound)
+	tag: Sequence[Tag]
 
-	#: DocumentCode.NEW for T1 units requiring computation, DocumentCode.OK otherwise
-	code: int
+	#: Ampel channel(s) associated with this document
+	channel: Required[Sequence[ChannelId]]
 
-	#: Set by ingesters (ex: ZTF_PUB)
-	tag: Sequence[Tag]
+	#: DocumentCode.NEW for T1 units requiring computation, DocumentCode.OK otherwise
+	code: Required[int]
 
 	#: References among other things the id of process invocation that created this doc
-	meta: Sequence[MetaRecord]
-
-	#: Ampel tier of the process that created this doc (-1 is ops)
-	tier: Literal[-1, 0, 1, 3]
+	meta: Required[Sequence[MetaRecord]]
 
 	#: Potential result of AbsT1ComputeUnit subclasses
 	body: Sequence[UBson]
```

### Comparing `ampel-interface-0.8a1/ampel/content/T2Document.py` & `ampel_interface-0.9.0/ampel/content/T2Document.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,56 +1,58 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/content/T2Document.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 13.01.2018
-# Last Modified Date: 23.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-from typing import TypedDict, Union, Optional, Sequence
+# File:                Ampel-interface/ampel/content/T2Document.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                13.01.2018
+# Last Modified Date:  25.06.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
+
+from typing import TypedDict
+from typing_extensions import Required
+from collections.abc import Sequence
 from ampel.types import UBson, ChannelId, StockId, Tag, UnitId, T2Link
 from ampel.content.MetaRecord import MetaRecord
 
 
 class T2Document(TypedDict, total=False):
 	"""
 	Specifications for tier2 documents stored as BSON structures in the ampel DB.
 	Calculations of the associated t2 unit is performed based on ampel data referenced by the attribute 'link'.
 	Linked input data type can be either :class:`~ampel.content.StockDocument.StockDocument`,
 	:class:`~ampel.content.DataPoint.DataPoint`, or :class:`~ampel.content.T1Document.T1Document`.
 	"""
 
 	#: Stock id associated with the data
-	stock: Union[StockId, Sequence[StockId]]
+	stock: Required[StockId | Sequence[StockId]]
 
 	#: Optional source origin (avoids potential stock collision between different data sources)
 	origin: int
 
 	#: Name of the unit to be run. This may be hashed for performance reasons.
-	unit: UnitId
+	unit: Required[UnitId]
 
 	#: Configuration hash, if unit defaults were overridden. The underlying values can be resolved with
 	#: :meth:`UnitLoader.get_init_config() <ampel.core.UnitLoader.UnitLoader.get_init_config>`
-	config: Optional[int]
+	config: Required[None | int]
 
 	#: References to input data
-	link: T2Link
+	link: Required[T2Link]
 
+	#: visible by any projection (not channel bound)
 	tag: Sequence[Tag]
-	channel: Sequence[ChannelId]
+
+	#: Ampel channel(s) associated with this document
+	channel: Required[Sequence[ChannelId]]
 
 	#: Records of activity on this document
-	meta: Sequence[MetaRecord]
+	meta: Required[Sequence[MetaRecord]]
 
-	#: Name of the database collection holding the input data
+	#: Name of the database collection holding the input data (t1 if unspecified)
 	#: (enables efficient DB queries at T3 level)
 	col: str
 
-	#: Ever increasing global and unique run identifier
-	run: Union[int, Sequence[int]]
-
 	#: DocumentCode.NEW for new T2 document, DocumentCode.OK if computation was successful
-	code: int
+	code: Required[int]
 
 	#: value(s) returned by T2 unit execution(s)
-	body: Sequence[UBson]
+	body: Required[Sequence[UBson]]
```

### Comparing `ampel-interface-0.8a1/ampel/content/T3Document.py` & `ampel_interface-0.9.0/ampel/content/T3Document.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,54 +1,64 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/content/T3Document.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 23.02.2021
-# Last Modified Date: 18.04.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-from bson import ObjectId
-from typing import Sequence, Union, TypedDict
-from ampel.types import ChannelId, StockId, Tag, UBson
+# File:                Ampel-interface/ampel/content/T3Document.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                23.02.2021
+# Last Modified Date:  25.06.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
+
+from typing import TypedDict, Any
+from typing_extensions import Required
+from collections.abc import Sequence
+from ampel.types import ChannelId, StockId, Tag, UBson, UnitId
 from ampel.content.MetaRecord import MetaRecord
 
 
 class T3Document(TypedDict, total=False):
 	"""
 	Specifications for tier3 documents stored as BSON structures in the ampel DB
 	"""
 
-	#: Database primary id (contains time of creation)
-	_id: ObjectId
+	#: Database primary id
+	_id: str | bytes
 
 	#: Name of the associated T3 process (may be a hash)
-	process: Union[int, str]
+	process: int | str
 
 	#: T3 unit name
-	unit: str
+	unit: Required[UnitId]
 
-	#: T3 unit config (hashed)
-	config: int
+	#: Hash of config (including defaults defined in unit class)
+	confid: Required[int]
 
-	#: Ever increasing global and unique run identifier
-	run: int
+	#: Resolved T3 unit config for convenience
+	config: dict[str, Any]
 
-	channel: Union[ChannelId, Sequence[ChannelId]]
+	#: visible by any projection (not channel bound)
+	tag: Tag | Sequence[Tag]
+
+	#: Ampel channel(s) associated with this document
+	channel: ChannelId | Sequence[ChannelId]
 
 	#: Note: might contain versions of dependent external services
 	#: (not only those used by t3 units but also potentially versions of resources
 	#: used by session and/or complement routines)
-	meta: MetaRecord
+	meta: Required[MetaRecord]
+
+	#: Records session info, if any
+	session: None | dict[str, Any]
 
 	#: Stock id of the views provided to unit
-	stock: Sequence[StockId]
+	stock: None | Sequence[StockId]
 
 	#: Optional source origin (avoids potential stock collision between different data sources)
 	origin: int
 
-	tag: Sequence[Tag]
-
 	#: Negative values must be member of :class:`~ampel.enum.DocumentCode.DocumentCode`
-	code: int
+	code: Required[int]
+
+	#: Optional human friendly date time stamp
+	datetime: str
 
+	#: Optional in t1 and t3 docs, mandatory in t0 and t2 docs
 	body: UBson
```

### Comparing `ampel-interface-0.8a1/ampel/model/UnitModel.py` & `ampel_interface-0.9.0/ampel/model/UnitModel.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,42 +1,33 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/model/UnitModel.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 26.09.2019
-# Last Modified Date: 17.02.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-from typing import Dict, Optional, Any, Union, Generic
-from ampel.types import T
-from ampel.secret.NamedSecret import NamedSecret
-from ampel.secret.AESecret import AESecret
-from ampel.model.StrictGenericModel import StrictGenericModel
+# File:                Ampel-interface/ampel/model/UnitModel.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                26.09.2019
+# Last Modified Date:  15.09.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
+
+from typing import Any, Generic, TypeVar
+from ampel.base.AmpelGenericModel import AmpelGenericModel
+T = TypeVar("T", bound=str)
 
 
-class UnitModel(StrictGenericModel, Generic[T]):
+class UnitModel(AmpelGenericModel, Generic[T]):
 	"""
 	Specification of a processing unit.
-	Note: generic parametrization allows to constrain unit ids (ex: UnitModel[Literal[T2SNCosmo]])
+	Note: generic parametrization allows to constrain unit ids (ex: UnitModel[Literal['T2SNCosmo']])
 	"""
 
 	#: Name of ampel unit class
 	unit: T
 
 	#: - None: no config (use class defaults)
 	#: - dict: config 'as is'
 	#: - str: a corresponding alias key in the AmpelConfig must match the provided string
 	#: - int: used internally for T2 units, a corresponding int key (AmpelConfig, base key 'confid') must match the provided integer
-	config: Union[None, int, str, Dict[str, Any]]
+	config: None | int | str | dict[str, Any] = None
 
-	secrets: Union[None, NamedSecret, AESecret]
+	secrets: None | dict[str, Any] = None
 
 	#: Values to override in the config
-	override: Optional[Dict[str, Any]]
-
-
-	def dict(self, **kwargs):
-		ret = super().dict(**kwargs)
-		if 'secrets' in ret:
-			del ret['secrets']
-		return ret
+	override: None | dict[str, Any] = None
```

### Comparing `ampel-interface-0.8a1/ampel/secret/AESecret.py` & `ampel_interface-0.9.0/ampel/secret/AESecret.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,22 +1,21 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-core/ampel/secret/AESecret.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 20.06.2021
-# Last Modified Date: 20.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-from typing import Optional
-from pydantic import BaseModel
-from ampel.abstract.Secret import Secret
+# File:                Ampel-interface/ampel/secret/AESecret.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                20.06.2021
+# Last Modified Date:  30.12.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
+from ampel.secret.Secret import Secret
+from ampel.base.AmpelBaseModel import AmpelBaseModel
 
-class AESecret(Secret[str], BaseModel):
+
+class AESecret(Secret[str], AmpelBaseModel):
 	"""
 	AES encrypted secret.
 
 	To create an encrypted secret, please:
 	- go to https://bitwiseshiftleft.github.io/sjcl/demo/
 	- enter the shared password in the green box
 	- enter the secret message (authtoken for example) in the red box
@@ -36,15 +35,15 @@
 	ts: int
 	mode: str
 	adata: str
 	cipher: str
 	salt: str
 	ct: str
 
-	value: Optional[str]
+	value: None | str
 
 	def __repr__(self):
 		return '<AESecret>'
 
 	def set(self, value: str) -> None:
 		self.value = value
```

### Comparing `ampel-interface-0.8a1/ampel/secret/NamedSecret.py` & `ampel_interface-0.9.0/ampel/secret/NamedSecret.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,33 +1,32 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/secret/NamedSecret.py
-# License           : BSD-3-Clause
-# Author            : Jakob van Santen <jakob.van.santen@desy.de>
-# Date              : 14.08.2020
-# Last Modified Date: 20.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
-
-from typing import Optional
-from ampel.abstract.Secret import Secret, T
-from pydantic import BaseModel
+# File:                Ampel-interface/ampel/secret/NamedSecret.py
+# License:             BSD-3-Clause
+# Author:              Jakob van Santen <jakob.van.santen@desy.de>
+# Date:                14.08.2020
+# Last Modified Date:  30.12.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
+from ampel.secret.Secret import Secret, T
+from ampel.base.AmpelBaseModel import AmpelBaseModel
 
-class NamedSecret(Secret[T], BaseModel):
+
+class NamedSecret(Secret[T], AmpelBaseModel):
 	"""
 	A Secret:
 	- featuring a label used as lookup key during secret resolution
 	- holding a simple reference to a sensitive payload value
 	"""
 
 	label: str
-	value: Optional[T] = None
+	value: None | T = None
 
 	def __repr__(self):
-		return '<NamedSecret>'
+		return f'NamedSecret(label={repr(self.label)})'
 
 	def get(self) -> T:
 		if self.value is None:
 			raise ValueError("Secret not yet resolved")
 		return self.value
 
 	def set(self, arg: T) -> None:
```

### Comparing `ampel-interface-0.8a1/ampel/struct/AmpelBuffer.py` & `ampel_interface-0.9.0/ampel/struct/AmpelBuffer.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,37 +1,36 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/struct/AmpelBuffer.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 31.05.2018
-# Last Modified Date: 04.04.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/struct/AmpelBuffer.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                31.05.2018
+# Last Modified Date:  01.12.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Optional, Dict, List, Any, TypedDict, Literal
+from typing import Any, TypedDict, Literal
 from ampel.types import StockId
 from ampel.content.StockDocument import StockDocument
 from ampel.content.DataPoint import DataPoint
 from ampel.content.T1Document import T1Document
 from ampel.content.T2Document import T2Document
-from ampel.content.T3Document import T3Document
 from ampel.content.LogDocument import LogDocument
 
 # Please update BufferKey on AmpelBuffer udpates
 # There is currently unfortunately no way of extracting a Literal out of a TypedDict
-BufferKey = Literal['id', 'stock', 't0', 't1', 't2', 't3', 'logs', 'extra']
+BufferKey = Literal['id', 'stock', 'origin', 't0', 't1', 't2', 'logs', 'extra']
 
 class AmpelBuffer(TypedDict, total=False):
 	"""
 	Content bundle used to build :class:`~ampel.view.SnapView.SnapView`.
 	
 	This is a dict containing 1 or more of the following items:
 	"""
-	# Could stock be of type List[StockDocument] to enable hybrid/dual transients ?
+	# Could stock be of type list[StockDocument] to enable hybrid/dual transients ?
 	id: StockId
-	stock: Optional[StockDocument]
-	t0: Optional[List[DataPoint]]
-	t1: Optional[List[T1Document]]
-	t2: Optional[List[T2Document]]
-	t3: Optional[List[T3Document]]
-	logs: Optional[List[LogDocument]]
-	extra: Optional[Dict[str, Any]]
+	stock: None | StockDocument
+	origin: None | int | list[int]
+	t0: None | list[DataPoint]
+	t1: None | list[T1Document]
+	t2: None | list[T2Document]
+	logs: None | list[LogDocument]
+	extra: None | dict[str, Any]
```

### Comparing `ampel-interface-0.8a1/ampel/struct/JournalAttributes.py` & `ampel_interface-0.9.0/ampel/struct/JournalAttributes.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,43 +1,44 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/struct/JournalAttributes.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 15.10.2018
-# Last Modified Date: 12.05.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/struct/JournalAttributes.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                15.10.2018
+# Last Modified Date:  12.05.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Dict, Optional, Sequence, Union, Any
+from typing import Any
+from collections.abc import Sequence
 from ampel.types import Tag
 from ampel.content.JournalRecord import JournalRecord
 
 
 class JournalAttributes:
 	"""
 	Structure potentialy used by Ampel units to customize
 	the stock journal entry created after a process is run.
 	"""
 
 	__slots__ = 'tag', 'code', 'extra'
 
 	#: code / status
-	code: Optional[int]
+	code: None | int
 
 	#: journal entry tag(s)
-	tag: Optional[Union[Tag, Sequence[Tag]]]
+	tag: None | Tag | Sequence[Tag]
 
 	#: if provided, will be included as-is under the journal root key 'extra'
-	extra: Optional[Dict[str, Any]]
+	extra: None | dict[str, Any]
 
 
 	def __init__(self,
-		code: Optional[int] = None,
-		tag: Optional[Union[Tag, Sequence[Tag]]] = None,
-		extra: Optional[Dict[str, Any]] = None
+		code: None | int = None,
+		tag: None | Tag | Sequence[Tag] = None,
+		extra: None | dict[str, Any] = None
 	) -> None:
 		"""
 		:param code: potential integer code of the executed process
 		:param tag: journal entry tag(s)
 		:param extra: optional dict, which if provided, will be included 'as is' under journal root key 'extra'
 		Note regarding the type of extra: as of june 2020, mypy does not support recursive / json type
 		-> https://github.com/python/mypy/issues/731
```

### Comparing `ampel-interface-0.8a1/ampel/struct/T1CombineResult.py` & `ampel_interface-0.9.0/ampel/struct/T1CombineResult.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,32 +1,32 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/struct/T1CombineResult.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 04.05.2021
-# Last Modified Date: 17.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/struct/T1CombineResult.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                04.05.2021
+# Last Modified Date:  17.06.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Optional, Dict, Any, List
+from typing import Any
 from ampel.types import DataPointId
 
 
 class T1CombineResult:
 	"""
 	Structure potentialy returned by Ampel AbsT1CombineUnit instances
 	to customize code or meta of T1Documents.
 	"""
 
 	__slots__ = 'code', 'meta', 'dps'
 
 	def __init__(self,
-		dps: List[DataPointId],
-		code: Optional[int] = None,
-		meta: Optional[Dict[str, Any]] = None
+		dps: list[DataPointId],
+		code: None | int = None,
+		meta: None | dict[str, Any] = None
 	) -> None:
 		"""
 		:param dps: ids of the datapoints to combine
 		:param code: customize DocumentCode (ex: DocumentCode.RERUN_REQUESTED)
 		:param meta: customize meta dict
 		"""
```

### Comparing `ampel-interface-0.8a1/ampel/util/compression.py` & `ampel_interface-0.9.0/ampel/util/compression.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,58 +1,58 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/util/compression.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 29.06.2021
-# Last Modified Date: 29.06.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/util/compression.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                29.06.2021
+# Last Modified Date:  20.04.2022
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import zipfile
 from io import BytesIO
-from typing import Dict, Tuple, Literal
+from typing import Literal
 
-Compression = Literal['ZIP_DEFLATED', 'ZIP_DEFLATED', 'ZIP_BZIP2']
+TCompression = Literal['ZIP_DEFLATED', 'ZIP_LZMA', 'ZIP_BZIP2']
 
 def compress(
 	payload: bytes,
 	filename: str,
-	alg: Compression = "ZIP_DEFLATED",
-	compress_level: int = 9
+	alg: TCompression = "ZIP_DEFLATED",
+	compression_level: int = 9
 ) -> bytes:
 
-	outbio, zf = _new(alg, compress_level)
+	outbio, zf = _new_zip_file(alg, compression_level)
 	zf.writestr(filename, payload)
 	zf.close()
 	return outbio.getvalue()
 
 
 def compress_many(
-	arg: Dict[str, bytes],
-	alg: Compression = "ZIP_DEFLATED",
-	compress_level: int = 9
+	arg: dict[str, bytes],
+	alg: TCompression = "ZIP_DEFLATED",
+	compression_level: int = 9
 ) -> bytes:
 
-	outbio, zf = _new(alg, compress_level)
+	outbio, zf = _new_zip_file(alg, compression_level)
 	for k, v in arg.items():
 		zf.writestr(k, v)
 	zf.close()
 
 	return outbio.getvalue()
 
 
-def _new(
-	alg: Compression = "ZIP_DEFLATED",
-	compress_level: int = 9
-) -> Tuple[BytesIO, zipfile.ZipFile]:
+def _new_zip_file(
+	alg: TCompression = "ZIP_DEFLATED",
+	compression_level: int = 9
+) -> tuple[BytesIO, zipfile.ZipFile]:
 
 	outbio = BytesIO()
 	return outbio, zipfile.ZipFile(
 		outbio, "w", getattr(zipfile, alg), False,
-		compresslevel = compress_level
+		compresslevel = compression_level
 	)
 
 
 def decompress(arg: bytes) -> bytes:
 	bio = BytesIO()
 	bio.write(arg)
 	zf = zipfile.ZipFile(bio)
@@ -60,12 +60,12 @@
 	return zf.read(file_name)
 
 
 def decompress_str(arg: bytes) -> str:
 	return str(decompress(arg), "utf8")
 
 
-def decompress_many(arg: bytes) -> Dict[str, bytes]:
+def decompress_many(arg: bytes) -> dict[str, bytes]:
 	bio = BytesIO()
 	bio.write(arg)
 	zf = zipfile.ZipFile(bio)
 	return {file_name: zf.read(file_name) for file_name in zf.namelist()}
```

### Comparing `ampel-interface-0.8a1/ampel/util/docstringutils.py` & `ampel_interface-0.9.0/ampel/util/docstringutils.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,67 +1,67 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : ampel/utils/docstringutils.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 02.09.2018
-# Last Modified Date: 11.12.2019
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                ampel/utils/docstringutils.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                02.09.2018
+# Last Modified Date:  11.12.2019
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 import inspect, re
 
 regex_ignore = re.compile(':[ \t]*?ClassVar|[ \t]*?#')
 regex_stop = re.compile('^[ \t]*?@|^[ \t]*?def|^class ')
 
 def gendocstring(klass):
 	"""
 	=============================================================================
-	Decorator for pydantic BaseModel child classes and python 3.7 dataclasses.
-	-> Automatically generates doctring based on class members (makes required 
+	Decorator for model sub-classes and python 3.7 dataclasses.
+	-> Automatically generates doctring based on class members (makes required
 	variables (including type hints) available in docstring)
 	=============================================================================
 
 	Note: the module 'inspect' does not work with classes defined within ipython
 	
 	Code example:
 	~~~~~~~~~~~~~
 	
-		from pydantic import BaseModel
+		from ampel.base.AmpelBaseModel import AmpelBaseModel
 		from ampel.util.docstringutils import gendocstring
 	
 		@gendocstring
-		class MyConfig(BaseModel):
+		class MyConfig(AmpelBaseModel):
 			my_str: str
 			my_int: int = 0
 	
 		@gendocstring
-		class MyConfig2(BaseModel):
+		class MyConfig2(AmpelBaseModel):
 			\"\"\"
 			Existing docstrings will be preserved
 			\"\"\"
 			my_str2: str
 			my_int2: int = 0
 
 	Generated docstrings:
 	~~~~~~~~~~~~~~~~~~~~~
 	
 		In []: print(MyConfig.__doc__)
 		Out []:
 		===================
-		Fields: 
+		Fields:
 		  my_str: str
 		  my_int: int = 0
 		===================
 	
 		In []: print(MyConfig2.__doc__)
 		Out []:
 		=====================================
 		Existing docstrings will be preserved
 		-------------------------------------
-		Fields: 
+		Fields:
 		  my_str2: str
 		  my_int2: int = 0
 		=====================================
 	"""
 	out_doc = []
 	exisiting_doc = []
 	in_doc = inspect.getdoc(klass)
```

### Comparing `ampel-interface-0.8a1/ampel/util/freeze.py` & `ampel_interface-0.9.0/ampel/util/freeze.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/util/freeze.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 10.12.2019
-# Last Modified Date: 09.06.2020
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/util/freeze.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                10.12.2019
+# Last Modified Date:  09.06.2020
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
-from typing import Dict, Any
+from typing import Any
 from ampel.view.ReadOnlyDict import ReadOnlyDict
 
 
 def recursive_freeze(arg: Any) -> Any:
 	"""
 	Return an immutable shallow copy
 	:param arg:
@@ -35,15 +35,15 @@
 
 	if isinstance(arg, set):
 		return frozenset(arg)
 
 	return arg
 
 
-def recursive_unfreeze(arg: ReadOnlyDict) -> Dict:
+def recursive_unfreeze(arg: ReadOnlyDict) -> dict:
 	"""
 	Inverse of recursive_freeze
 	"""
 	if isinstance(arg, ReadOnlyDict):
 		return dict(
 			{
 				recursive_unfreeze(k): recursive_unfreeze(v)
```

### Comparing `ampel-interface-0.8a1/ampel/util/json.py` & `ampel_interface-0.9.0/ampel/util/json.py`

 * *Files 17% similar despite different names*

```diff
@@ -13,32 +13,27 @@
 			line,
 			object_hook=partial(
 				object_hook,
 				ignore_missing_modules=ignore_missing_modules
 			)
 		)
 
-# mypy 0.770 fails with:
-# ampel/util/json.py:20: error: Name 'json.JSONEncoder' is not defined
-# FIXME remove when namespace packages are properly supported, see
-# https://github.com/python/mypy/issues/5759
-
-class AmpelEncoder(json.JSONEncoder): # type: ignore[name-defined]
+class AmpelEncoder(json.JSONEncoder):
 	"""
 	Serialize objects in a mix of:
 	a) JSONRPC 1.0-like class hinting for custom Ampel types
 	b) PyMongo-provided JSON representation for BSON types
 	"""
-	def __init__(self, *args, lossy=False, **kwargs):
+	def __init__(self, *args, lossy: bool=False, **kwargs):
 		"""
 		if lossy, cast mappingproxy to dict, set and tuple to list, etc
 		"""
 		self.lossy = lossy
 		super().__init__(*args, **kwargs)
-		self.bson_options = bson.json_util.STRICT_JSON_OPTIONS
+		self.bson_options = bson.json_util.CANONICAL_JSON_OPTIONS
 
 	def default(self, obj, fallthrough=False):
 		"""
 		Encode selected types in jsonrpc class-hint notation
 		"""
 		serializer = self.get_serializer(obj)
 		if serializer is not None:
@@ -94,15 +89,15 @@
 		elif isinstance(obj, MappingProxyType):
 			return lambda x: [dict(obj)]
 		else:
 			return None
 
 def object_hook(
     dct,
-    options=bson.json_util.STRICT_JSON_OPTIONS,
+    options=bson.json_util.CANONICAL_JSON_OPTIONS,
     ignore_missing_modules=True
 ):
 	"""
 	Deserialize an object serialized by AmpelEncoder
 	"""
 	obj = bson.json_util.object_hook(dct, options)
 	if type(obj) != type(dct):
```

### Comparing `ampel-interface-0.8a1/ampel/util/serialize.py` & `ampel_interface-0.9.0/ampel/util/serialize.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,43 +1,59 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/util/serialize.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : 25.03.2021
-# Last Modified Date: 25.03.2021
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/util/serialize.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                25.03.2021
+# Last Modified Date:  20.12.2021
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 from typing import Any
-from bson import ObjectId
 from base64 import b64encode, b64decode
+
+try:
+	from bson import ObjectId
+	HAVE_BSON = True
+except ImportError:
+	HAVE_BSON = False
  
 dsi = dict.__setitem__
 
-def walk_and_encode(arg: Any) -> Any:
+def walk_and_encode(arg: Any, destructive: bool = True) -> Any:
 	"""
 	Convert bytes values into "b64:<string>"
 	Convert ObjectId instances into "oid:<hex>"
-	Note: destructive op: modifies the input dict(s)
+	:param destructive: true modifies the input dict(s)
 	"""
 
 	if isinstance(arg, (list, tuple, set)):
-		return [walk_and_encode(el) for el in arg]
+		return [walk_and_encode(el, destructive) for el in arg]
 
 	elif isinstance(arg, dict):
-		for k, v in arg.items():
-			if isinstance(v, ObjectId):
-				dsi(arg, k, "oid:" + v.binary.hex())
-			elif isinstance(v, bytes):
-				dsi(arg, k, "b64:" + b64encode(v).decode('ascii'))
-			else:
-				dsi(arg, k, walk_and_encode(v))
-		return arg
+		if destructive:
+			for k, v in arg.items():
+				if HAVE_BSON and isinstance(v, ObjectId):
+					dsi(arg, k, "oid:" + v.binary.hex())
+				elif isinstance(v, bytes):
+					dsi(arg, k, "b64:" + b64encode(v).decode('ascii'))
+				else:
+					dsi(arg, k, walk_and_encode(v, destructive))
+			return arg
+		else:
+			return {
+				k: ("oid:" + v.binary.hex())
+				if HAVE_BSON and isinstance(v, ObjectId) else (
+					("b64:" + b64encode(v).decode('ascii'))
+					if isinstance(v, bytes)
+					else walk_and_encode(v, destructive)
+				)
+				for k, v in arg.items()
+			}
 
-	elif isinstance(arg, ObjectId):
+	elif HAVE_BSON and isinstance(arg, ObjectId):
 		return "oid:" + arg.binary.hex()
 
 	elif isinstance(arg, bytes):
 		return "b64:" + b64encode(arg).decode('ascii')
 
 	return arg
 
@@ -52,19 +68,26 @@
 		return [walk_and_decode(el) for el in arg]
 
 	elif isinstance(arg, dict):
 		for k, v in arg.items():
 			if isinstance(v, str) and v.startswith("b64:"):
 				arg[k] = b64decode(v[4:])
 			elif isinstance(v, str) and v.startswith("oid:"):
-				arg[k] = ObjectId(v[4:])
+				if HAVE_BSON:
+					arg[k] = ObjectId(v[4:])
+				else:
+					raise ValueError(f"got ObjectId {v}, but pymongo is not installed")
+
 			else:
 				arg[k] = walk_and_decode(v)
 		return arg
 
 	elif isinstance(arg, str) and arg.startswith("b64:"):
 		return b64decode(arg[4:])
 
 	elif isinstance(arg, str) and arg.startswith("oid:"):
-		return ObjectId(arg[4:])
+		if HAVE_BSON:
+			return ObjectId(arg[4:])
+		else:
+			raise ValueError(f"got ObjectId {arg}, but pymongo is not installed")
 
 	return arg
```

### Comparing `ampel-interface-0.8a1/ampel/view/ReadOnlyDict.py` & `ampel_interface-0.9.0/ampel/view/ReadOnlyDict.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-# File              : Ampel-interface/ampel/view/ReadOnlyDict.py
-# License           : BSD-3-Clause
-# Author            : vb <vbrinnel@physik.hu-berlin.de>
-# Date              : Unspecified
-# Last Modified Date: 16.04.2020
-# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>
+# File:                Ampel-interface/ampel/view/ReadOnlyDict.py
+# License:             BSD-3-Clause
+# Author:              valery brinnel <firstname.lastname@gmail.com>
+# Date:                Unspecified
+# Last Modified Date:  16.04.2020
+# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>
 
 
 class ReadOnlyDict(dict):
 	"""A dict whose items can't be changed."""
 
 	def __readonly__(self, *args, **kwargs):
 		""":raises RuntimeError: whenever called"""
@@ -17,13 +17,13 @@
 
 	__setitem__ = __readonly__
 	__delitem__ = __readonly__
 	pop = __readonly__ # type: ignore
 	popitem = __readonly__
 	clear = __readonly__
 	update = __readonly__ # type: ignore
-	setdefault = __readonly__
+	setdefault = __readonly__ # type: ignore
 
 	del __readonly__
 
 	def __reduce__(self):
 		return type(self), (dict(self),)
```

### Comparing `ampel-interface-0.8a1/PKG-INFO` & `ampel_interface-0.9.0/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,31 +1,32 @@
 Metadata-Version: 2.1
 Name: ampel-interface
-Version: 0.8a1
+Version: 0.9.0
 Summary: Base classes for the Ampel analysis platform
 Home-page: https://ampelproject.github.io
 License: BSD-3-Clause
 Author: Valery Brinnel
 Maintainer: Jakob van Santen
 Maintainer-email: jakob.van.santen@desy.de
-Requires-Python: >=3.8,<4.0
+Requires-Python: >=3.10,<4.0
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Scientific/Engineering :: Information Analysis
 Classifier: Typing :: Typed
 Provides-Extra: docs
-Requires-Dist: PyYAML (>=5.4.1,<6.0.0)
-Requires-Dist: Sphinx (>=3.5.1,<4.0.0); extra == "docs"
-Requires-Dist: pydantic (>=1.8.1,<2.0.0)
-Requires-Dist: pymongo (>=3.10,<4.0)
-Requires-Dist: sphinx-autodoc-typehints (>=1.11.1,<2.0.0); extra == "docs"
-Requires-Dist: tomlkit (>=0.7.0,<0.8.0); extra == "docs"
+Requires-Dist: PyYAML (>=6.0.0,<7.0.0)
+Requires-Dist: Sphinx (>=6.0.0,<7.0.0) ; extra == "docs"
+Requires-Dist: pydantic (>=1.9.0,<2.0.0)
+Requires-Dist: sphinx-autodoc-typehints (>=1.11.1,<2.0.0) ; extra == "docs"
+Requires-Dist: tomlkit (>=0.11.0,<0.12.0) ; extra == "docs"
+Requires-Dist: ujson (>=5.1.0,<6.0.0)
+Requires-Dist: xxhash (>=3.0.0,<4.0.0)
 Project-URL: Repository, https://github.com/AmpelProject/Ampel-interface
 Description-Content-Type: text/markdown
 
 # Ampel-interface
 
 `ampel-interface` provides type-hinted abstract base classes for [Ampel](https://ampelproject.github.io).
```

