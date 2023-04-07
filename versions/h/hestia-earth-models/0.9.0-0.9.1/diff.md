# Comparing `tmp/hestia-earth-models-0.9.0.tar.gz` & `tmp/hestia-earth-models-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/hestia-earth-models-0.9.0.tar", last modified: Wed Jul 21 07:14:05 2021, max compression
+gzip compressed data, was "dist/hestia-earth-models-0.9.1.tar", last modified: Wed Jul 21 07:27:40 2021, max compression
```

## Comparing `hestia-earth-models-0.9.0.tar` & `hestia-earth-models-0.9.1.tar`

### file list

```diff
@@ -1,494 +1,494 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/
--rw-rw-rw-   0 root         (0) root         (0)    35149 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/LICENSE
--rw-rw-rw-   0 root         (0) root         (0)       18 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1842 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     1046 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/
--rw-rw-rw-   0 root         (0) root         (0)       56 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/
--rw-rw-rw-   0 root         (0) root         (0)       76 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/agribalyse2016/
--rw-rw-rw-   0 root         (0) root         (0)      352 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/agribalyse2016/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2291 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/agribalyse2016/machineryInfrastructureDepreciatedAmountPerCycle.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/
--rw-rw-rw-   0 root         (0) root         (0)      362 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     1514 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/ch4ToAirCropResidueBurning.py
--rwxrwxrwx   0 root         (0) root         (0)     1520 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/n2OToAirCropResidueBurningDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1514 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/nh3ToAirCropResidueBurning.py
--rw-rw-rw-   0 root         (0) root         (0)     1514 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/noxToAirCropResidueBurning.py
--rw-rw-rw-   0 root         (0) root         (0)      502 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/aware/
--rw-rw-rw-   0 root         (0) root         (0)      343 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/aware/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1973 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/aware/freshwaterWithdrawals.py
--rw-rw-rw-   0 root         (0) root         (0)     2311 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/aware/scarcityWeightedWaterUse.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/
--rw-rw-rw-   0 root         (0) root         (0)      358 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1613 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/ch4ToAirNaturalVegetationBurning.py
--rw-rw-rw-   0 root         (0) root         (0)     1550 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/co2ToAirBiomassAndSoilCarbonStockChange.py
--rw-rw-rw-   0 root         (0) root         (0)     1619 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/n2OToAirNaturalVegetationBurningDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1049 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/
--rw-rw-rw-   0 root         (0) root         (0)      355 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1944 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandOccupation.py
--rw-rw-rw-   0 root         (0) root         (0)     2337 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandTransformation.py
--rw-rw-rw-   0 root         (0) root         (0)     1572 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/biodiversityLossTotalLandUseEffects.py
--rw-rw-rw-   0 root         (0) root         (0)     1011 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/
--rw-rw-rw-   0 root         (0) root         (0)      356 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      769 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialExcludingFate.py
--rw-rw-rw-   0 root         (0) root         (0)      798 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialIncludingFateAverageEurope.py
--rw-rw-rw-   0 root         (0) root         (0)      792 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialExcludingFate.py
--rw-rw-rw-   0 root         (0) root         (0)      814 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialIncludingFateAverageEurope.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/
--rw-rw-rw-   0 root         (0) root         (0)      343 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/dataCompleteness/
--rw-rw-rw-   0 root         (0) root         (0)     1473 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/dataCompleteness/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1048 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/dataCompleteness/cropResidue.py
--rw-rw-rw-   0 root         (0) root         (0)      692 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/dataCompleteness/soilAmendments.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/
--rw-rw-rw-   0 root         (0) root         (0)     2114 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      280 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioCarbon.py
--rw-rw-rw-   0 root         (0) root         (0)      439 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioDryMatter.py
--rw-rw-rw-   0 root         (0) root         (0)      272 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioEnergy.py
--rw-rw-rw-   0 root         (0) root         (0)      386 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioFedWeight.py
--rw-rw-rw-   0 root         (0) root         (0)      485 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioNitrogen.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4008 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/aggregated.py
--rw-rw-rw-   0 root         (0) root         (0)      552 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/ecoinventV3.py
--rw-rw-rw-   0 root         (0) root         (0)      961 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/value.py
--rw-rw-rw-   0 root         (0) root         (0)     1386 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/irrigated.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/post_checks/
--rw-rw-rw-   0 root         (0) root         (0)      318 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/post_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      334 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/post_checks/site.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/pre_checks/
--rw-rw-rw-   0 root         (0) root         (0)      395 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/pre_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      420 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/pre_checks/site.py
--rw-rw-rw-   0 root         (0) root         (0)      877 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/pre_checks/startDate.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1823 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/economicValueShare.py
--rw-rw-rw-   0 root         (0) root         (0)     2304 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/price.py
--rw-rw-rw-   0 root         (0) root         (0)     1484 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/primary.py
--rw-rw-rw-   0 root         (0) root         (0)      973 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/revenue.py
--rw-rw-rw-   0 root         (0) root         (0)      999 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/value.py
--rw-rw-rw-   0 root         (0) root         (0)      608 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/cycle/siteDuration.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/data/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/data/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/data/impact_assessments/
--rw-rw-rw-   0 root         (0) root         (0)      446 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/data/impact_assessments/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1257 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/data/impact_assessments/download.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/deRuijterEtAl2010/
--rw-rw-rw-   0 root         (0) root         (0)      355 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/deRuijterEtAl2010/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1968 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/deRuijterEtAl2010/nh3ToAirCropResidueDecomposition.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/
--rw-rw-rw-   0 root         (0) root         (0)      349 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     1591 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/co2ToAirFuelCombustion.py
--rwxrwxrwx   0 root         (0) root         (0)     1604 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/n2OToAirFuelCombustionDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     5451 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/nh3ToAirInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1598 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/noxToAirFuelCombustion.py
--rw-rw-rw-   0 root         (0) root         (0)     1600 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/so2ToAirFuelCombustion.py
--rw-rw-rw-   0 root         (0) root         (0)      861 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/faostat2018/
--rw-rw-rw-   0 root         (0) root         (0)      349 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/faostat2018/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2582 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/faostat2018/seed.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/globalCropWaterModel2008/
--rw-rw-rw-   0 root         (0) root         (0)      362 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/globalCropWaterModel2008/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3157 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/globalCropWaterModel2008/rootingDepth.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/
--rw-rw-rw-   0 root         (0) root         (0)      355 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1576 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/emissions.py
--rw-rw-rw-   0 root         (0) root         (0)      308 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/irrigated.py
--rw-rw-rw-   0 root         (0) root         (0)      302 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/organic.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/post_checks/
--rw-rw-rw-   0 root         (0) root         (0)      332 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/post_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      347 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/post_checks/cycle.py
--rw-rw-rw-   0 root         (0) root         (0)      342 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/post_checks/site.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/pre_checks/
--rw-rw-rw-   0 root         (0) root         (0)      331 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/pre_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      538 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/pre_checks/cycle.py
--rw-rw-rw-   0 root         (0) root         (0)      428 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/pre_checks/site.py
--rw-rw-rw-   0 root         (0) root         (0)      744 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/product.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/
--rw-rw-rw-   0 root         (0) root         (0)      346 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4128 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/aboveGroundCropResidue.py
--rw-rw-rw-   0 root         (0) root         (0)     2163 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/aboveGroundCropResidueRemoved.py
--rw-rw-rw-   0 root         (0) root         (0)     4228 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/aboveGroundCropResidueTotal.py
--rw-rw-rw-   0 root         (0) root         (0)     3741 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/belowGroundCropResidue.py
--rw-rw-rw-   0 root         (0) root         (0)     2917 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/co2ToAirOrganicSoilCultivation.py
--rw-rw-rw-   0 root         (0) root         (0)     1658 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirCropResidueDecompositionIndirect.py
--rwxrwxrwx   0 root         (0) root         (0)     1535 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirExcretaDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1797 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirExcretaIndirect.py
--rwxrwxrwx   0 root         (0) root         (0)     1601 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1870 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerIndirect.py
--rwxrwxrwx   0 root         (0) root         (0)     1595 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1858 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerIndirect.py
--rw-rw-rw-   0 root         (0) root         (0)     2838 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirOrganicSoilCultivationDirect.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/
--rw-rw-rw-   0 root         (0) root         (0)     3033 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1144 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/residueBurnt.py
--rw-rw-rw-   0 root         (0) root         (0)       62 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/residueIncorporated.py
--rw-rw-rw-   0 root         (0) root         (0)       31 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/residueLeftOnField.py
--rw-rw-rw-   0 root         (0) root         (0)      964 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/residueRemoved.py
--rw-rw-rw-   0 root         (0) root         (0)     1344 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013ExcludingFeedbacks/
--rw-rw-rw-   0 root         (0) root         (0)      364 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013ExcludingFeedbacks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      742 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013ExcludingFeedbacks/gwp100.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013IncludingFeedbacks/
--rw-rw-rw-   0 root         (0) root         (0)      364 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013IncludingFeedbacks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      742 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013IncludingFeedbacks/gwp100.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/
--rw-rw-rw-   0 root         (0) root         (0)      346 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     5306 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/ch4ToAirEntericFermentation.py
--rw-rw-rw-   0 root         (0) root         (0)     5129 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/ch4ToAirFloodedRice.py
--rw-rw-rw-   0 root         (0) root         (0)     2339 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/co2ToAirLimeHydrolysis.py
--rw-rw-rw-   0 root         (0) root         (0)     2722 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/co2ToAirUreaHydrolysis.py
--rw-rw-rw-   0 root         (0) root         (0)     1990 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/croppingDuration.py
--rw-rw-rw-   0 root         (0) root         (0)     2770 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/nitrogenContent.py
--rw-rw-rw-   0 root         (0) root         (0)     1435 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/log.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/otherBackgroundDatabase/
--rw-rw-rw-   0 root         (0) root         (0)     2699 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/otherBackgroundDatabase/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/
--rw-rw-rw-   0 root         (0) root         (0)      354 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1603 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/landOccupation.py
--rw-rw-rw-   0 root         (0) root         (0)     1853 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/n2OToAirAquaculturePondsDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1698 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/n2ToAirAquaculturePonds.py
--rw-rw-rw-   0 root         (0) root         (0)     1772 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/netPrimaryProduction.py
--rwxrwxrwx   0 root         (0) root         (0)     2568 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/nh3ToAirAquaculturePonds.py
--rw-rw-rw-   0 root         (0) root         (0)     4002 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1232 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterCropResidueDecomposition.py
--rw-rw-rw-   0 root         (0) root         (0)     1168 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterExcreta.py
--rw-rw-rw-   0 root         (0) root         (0)     1186 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1180 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterOrganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1845 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/noxToAirAquaculturePonds.py
--rw-rw-rw-   0 root         (0) root         (0)     1652 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/nurseryDuration.py
--rw-rw-rw-   0 root         (0) root         (0)     1650 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/orchardDensity.py
--rw-rw-rw-   0 root         (0) root         (0)     1747 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/orchardDuration.py
--rw-rw-rw-   0 root         (0) root         (0)     3271 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/organicFertilizerToKgOrMass.py
--rw-rw-rw-   0 root         (0) root         (0)     1612 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/saplings.py
--rw-rw-rw-   0 root         (0) root         (0)     1659 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/soilTotalNitrogenContent.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/
--rw-rw-rw-   0 root         (0) root         (0)      356 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3406 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/nErosionAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     3407 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pErosionAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1598 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pToDrainageWaterAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1597 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pToGroundwaterAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     2040 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pToSurfacewaterAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     3252 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/
--rw-rw-rw-   0 root         (0) root         (0)      342 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/measurement/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/measurement/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1075 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/measurement/value.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/post_checks/
--rw-rw-rw-   0 root         (0) root         (0)      249 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/post_checks/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/pre_checks/
--rw-rw-rw-   0 root         (0) root         (0)      249 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/site/pre_checks/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/
--rw-rw-rw-   0 root         (0) root         (0)      345 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      856 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/aware.py
--rw-rw-rw-   0 root         (0) root         (0)     3120 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/clayContent.py
--rw-rw-rw-   0 root         (0) root         (0)     2261 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/croppingIntensity.py
--rw-rw-rw-   0 root         (0) root         (0)     1432 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/drainageClass.py
--rw-rw-rw-   0 root         (0) root         (0)     1495 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/ecoClimateZone.py
--rw-rw-rw-   0 root         (0) root         (0)     1055 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/ecoregion.py
--rw-rw-rw-   0 root         (0) root         (0)     1400 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/erodibility.py
--rw-rw-rw-   0 root         (0) root         (0)     2254 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/fallowCorrection.py
--rw-rw-rw-   0 root         (0) root         (0)     1561 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/heavyWinterPrecipitation.py
--rw-rw-rw-   0 root         (0) root         (0)     1590 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/histosol.py
--rw-rw-rw-   0 root         (0) root         (0)     1454 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/nutrientLossToAquaticEnvironment.py
--rw-rw-rw-   0 root         (0) root         (0)     2925 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/rainfallAnnual.py
--rw-rw-rw-   0 root         (0) root         (0)     1338 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/region.py
--rw-rw-rw-   0 root         (0) root         (0)     1410 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/slope.py
--rw-rw-rw-   0 root         (0) root         (0)     1425 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/slopeLength.py
--rw-rw-rw-   0 root         (0) root         (0)     1461 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilOrganicCarbonContent.py
--rw-rw-rw-   0 root         (0) root         (0)     1457 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilPh.py
--rw-rw-rw-   0 root         (0) root         (0)     1521 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilPhosphorusContent.py
--rw-rw-rw-   0 root         (0) root         (0)     1567 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilTotalNitrogenContent.py
--rw-rw-rw-   0 root         (0) root         (0)     2886 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/temperatureAnnual.py
--rw-rw-rw-   0 root         (0) root         (0)     3032 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/spatial/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/
--rw-rw-rw-   0 root         (0) root         (0)      357 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4797 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1366 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirCropResidueDecompositionDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1201 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirExcretaDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1213 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirInorganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1207 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirOrganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     3173 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1145 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirCropResidueDecomposition.py
--rw-rw-rw-   0 root         (0) root         (0)     1242 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirExcreta.py
--rw-rw-rw-   0 root         (0) root         (0)     1260 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1254 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirOrganicFertilizer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/
--rw-rw-rw-   0 root         (0) root         (0)      374 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2100 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1054 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirCropResidueDecomposition.py
--rw-rw-rw-   0 root         (0) root         (0)     1151 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirExcreta.py
--rw-rw-rw-   0 root         (0) root         (0)     1169 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1163 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirOrganicFertilizer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/transformation/
--rw-rw-rw-   0 root         (0) root         (0)      352 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/transformation/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/transformation/post_checks/
--rw-rw-rw-   0 root         (0) root         (0)      333 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/transformation/post_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1787 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/transformation/post_checks/product.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/
--rw-rw-rw-   0 root         (0) root         (0)     2020 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2252 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/blank_node.py
--rw-rw-rw-   0 root         (0) root         (0)     2882 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/constant.py
--rw-rw-rw-   0 root         (0) root         (0)     1524 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/crop.py
--rw-rw-rw-   0 root         (0) root         (0)     4750 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/cycle.py
--rw-rw-rw-   0 root         (0) root         (0)      484 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/dataCompleteness.py
--rw-rw-rw-   0 root         (0) root         (0)     1025 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/ecoClimateZone.py
--rw-rw-rw-   0 root         (0) root         (0)      421 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/emission.py
--rw-rw-rw-   0 root         (0) root         (0)     1950 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/impact_assessment.py
--rw-rw-rw-   0 root         (0) root         (0)      423 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/indicator.py
--rw-rw-rw-   0 root         (0) root         (0)     1135 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/inorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     8838 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/input.py
--rw-rw-rw-   0 root         (0) root         (0)     2017 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/measurement.py
--rw-rw-rw-   0 root         (0) root         (0)     1263 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/practice.py
--rw-rw-rw-   0 root         (0) root         (0)     2321 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/product.py
--rw-rw-rw-   0 root         (0) root         (0)     2441 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/property.py
--rw-rw-rw-   0 root         (0) root         (0)     1324 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/site.py
--rw-rw-rw-   0 root         (0) root         (0)     2549 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/utils/term.py
--rw-rw-rw-   0 root         (0) root         (0)       18 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/version.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/
--rw-rw-rw-   0 root         (0) root         (0)      371 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3542 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/nh3ToAirOrganicFertilizer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth_models.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1842 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth_models.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    22192 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth_models.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth_models.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      100 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth_models.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       19 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/hestia_earth_models.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     1382 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/agribalyse2016/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/agribalyse2016/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1159 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/agribalyse2016/test_machineryInfrastructureDepreciatedAmountPerCycle.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     1575 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_ch4ToAirCropResidueBurning.py
--rwxrwxrwx   0 root         (0) root         (0)     1587 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_n2OToAirCropResidueBurningDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1575 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_nh3ToAirCropResidueBurning.py
--rw-rw-rw-   0 root         (0) root         (0)     1575 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_noxToAirCropResidueBurning.py
--rw-rw-rw-   0 root         (0) root         (0)     1134 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/aware/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/aware/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1246 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/aware/test_freshwaterWithdrawals.py
--rw-rw-rw-   0 root         (0) root         (0)     1594 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/aware/test_scarcityWeightedWaterUse.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1171 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/test_ch4ToAirNaturalVegetationBurning.py
--rw-rw-rw-   0 root         (0) root         (0)     1178 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/test_co2ToAirBiomassAndSoilCarbonStockChange.py
--rw-rw-rw-   0 root         (0) root         (0)     1177 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/test_n2OToAirNaturalVegetationBurningDirect.py
--rw-rw-rw-   0 root         (0) root         (0)      444 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/test_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1566 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/test_biodiversityLossLandOccupation.py
--rw-rw-rw-   0 root         (0) root         (0)     1722 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/test_biodiversityLossLandTransformation.py
--rw-rw-rw-   0 root         (0) root         (0)     1092 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/test_biodiversityLossTotalLandUseEffects.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      912 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_eutrophicationPotentialExcludingFate.py
--rw-rw-rw-   0 root         (0) root         (0)      925 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_eutrophicationPotentialIncludingFateAverageEurope.py
--rw-rw-rw-   0 root         (0) root         (0)      922 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialExcludingFate.py
--rw-rw-rw-   0 root         (0) root         (0)      941 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialIncludingFateAverageEurope.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/cycle/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/cycle/dataCompleteness/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/dataCompleteness/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      613 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/dataCompleteness/test_cropResidue.py
--rw-rw-rw-   0 root         (0) root         (0)      620 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/dataCompleteness/test_soilAmendments.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/cycle/input/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/input/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2348 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/input/test_aggregated.py
--rw-rw-rw-   0 root         (0) root         (0)      514 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/input/test_ecoinventV3.py
--rw-rw-rw-   0 root         (0) root         (0)     1049 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/input/test_value.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/cycle/post_checks/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/post_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      621 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/post_checks/test_site.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/cycle/pre_checks/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/pre_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      694 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/pre_checks/test_site.py
--rw-rw-rw-   0 root         (0) root         (0)     1367 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/pre_checks/test_startDate.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/cycle/product/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/product/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1529 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/product/test_economicValueShare.py
--rw-rw-rw-   0 root         (0) root         (0)      893 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/product/test_price.py
--rw-rw-rw-   0 root         (0) root         (0)     2342 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/product/test_primary.py
--rw-rw-rw-   0 root         (0) root         (0)     1126 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/product/test_revenue.py
--rw-rw-rw-   0 root         (0) root         (0)     1073 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/product/test_value.py
--rw-rw-rw-   0 root         (0) root         (0)      850 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/test_dataCompleteness.py
--rw-rw-rw-   0 root         (0) root         (0)     1504 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/test_feedConversionRatio.py
--rw-rw-rw-   0 root         (0) root         (0)     1090 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/test_irrigated.py
--rw-rw-rw-   0 root         (0) root         (0)      362 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/test_post_checks.py
--rw-rw-rw-   0 root         (0) root         (0)      360 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/test_pre_checks.py
--rw-rw-rw-   0 root         (0) root         (0)      872 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/cycle/test_siteDuration.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/deRuijterEtAl2010/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/deRuijterEtAl2010/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1636 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/deRuijterEtAl2010/test_nh3ToAirCropResidueDecomposition.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     1846 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_co2ToAirFuelCombustion.py
--rwxrwxrwx   0 root         (0) root         (0)     1852 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_n2OToAirFuelCombustionDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1993 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_nh3ToAirInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1846 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_noxToAirFuelCombustion.py
--rw-rw-rw-   0 root         (0) root         (0)     1846 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_so2ToAirFuelCombustion.py
--rw-rw-rw-   0 root         (0) root         (0)      947 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/faostat2018/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/faostat2018/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1758 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/faostat2018/test_seed.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/globalCropWaterModel2008/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/globalCropWaterModel2008/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2075 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/globalCropWaterModel2008/test_rootingDepth.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/post_checks/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/post_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      661 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/post_checks/test_cycle.py
--rw-rw-rw-   0 root         (0) root         (0)      648 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/post_checks/test_site.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/pre_checks/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/pre_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      967 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/pre_checks/test_cycle.py
--rw-rw-rw-   0 root         (0) root         (0)      832 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/pre_checks/test_site.py
--rw-rw-rw-   0 root         (0) root         (0)     1184 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/test_emissions.py
--rw-rw-rw-   0 root         (0) root         (0)      377 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/test_irrigated.py
--rw-rw-rw-   0 root         (0) root         (0)      375 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/test_oganic.py
--rw-rw-rw-   0 root         (0) root         (0)      386 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/test_post_checks.py
--rw-rw-rw-   0 root         (0) root         (0)      384 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/test_pre_checks.py
--rw-rw-rw-   0 root         (0) root         (0)      959 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/impact_assessment/test_product.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/residue/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/residue/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      401 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/residue/test_residueBurnt.py
--rw-rw-rw-   0 root         (0) root         (0)      112 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/residue/test_residueIncorporated.py
--rw-rw-rw-   0 root         (0) root         (0)      387 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/residue/test_residueRemoved.py
--rw-rw-rw-   0 root         (0) root         (0)     1177 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_aboveGroundCropResidue.py
--rw-rw-rw-   0 root         (0) root         (0)     1169 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_aboveGroundCropResidueRemoved.py
--rw-rw-rw-   0 root         (0) root         (0)     3181 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_aboveGroundCropResidueTotal.py
--rw-rw-rw-   0 root         (0) root         (0)     2100 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_belowGroundCropResidue.py
--rw-rw-rw-   0 root         (0) root         (0)     1747 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_co2ToAirOrganicSoilCultivation.py
--rw-rw-rw-   0 root         (0) root         (0)     1147 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirCropResidueDecompositionIndirect.py
--rwxrwxrwx   0 root         (0) root         (0)     2000 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirExcretaDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1427 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirExcretaIndirect.py
--rwxrwxrwx   0 root         (0) root         (0)     1554 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1385 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerIndirect.py
--rwxrwxrwx   0 root         (0) root         (0)     1550 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1786 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerIndirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1196 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirOrganicSoilCultivationDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1332 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2006/test_residue.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/ipcc2013ExcludingFeedbacks/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2013ExcludingFeedbacks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      906 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2013ExcludingFeedbacks/test_gwp100.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/ipcc2013IncludingFeedbacks/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2013IncludingFeedbacks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      906 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2013IncludingFeedbacks/test_gwp100.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3445 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/test_ch4ToAirEntericFermentation.py
--rw-rw-rw-   0 root         (0) root         (0)     1701 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/test_ch4ToAirFloodedRice.py
--rw-rw-rw-   0 root         (0) root         (0)     1404 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/test_co2ToAirLimeHydrolysis.py
--rw-rw-rw-   0 root         (0) root         (0)     1583 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/test_co2ToAirUreaHydrolysis.py
--rw-rw-rw-   0 root         (0) root         (0)     1424 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/test_croppingDuration.py
--rw-rw-rw-   0 root         (0) root         (0)     1930 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/ipcc2019/test_nitrogenContent.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1708 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_landOccupation.py
--rw-rw-rw-   0 root         (0) root         (0)     1761 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_n2OToAirAquaculturePondsDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1754 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_n2ToAirAquaculturePonds.py
--rw-rw-rw-   0 root         (0) root         (0)     1071 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_netPrimaryProduction.py
--rwxrwxrwx   0 root         (0) root         (0)     2477 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_nh3ToAirAquaculturePonds.py
--rw-rw-rw-   0 root         (0) root         (0)     2731 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)      687 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterCropResidueDecomposition.py
--rw-rw-rw-   0 root         (0) root         (0)      670 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterExcreta.py
--rw-rw-rw-   0 root         (0) root         (0)      682 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)      680 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterOrganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1747 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_noxToAirAquaculturePonds.py
--rw-rw-rw-   0 root         (0) root         (0)     1442 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_nurseryDuration.py
--rw-rw-rw-   0 root         (0) root         (0)     1441 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_orchardDensity.py
--rw-rw-rw-   0 root         (0) root         (0)     1442 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_orchardDuration.py
--rw-rw-rw-   0 root         (0) root         (0)     1959 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_organicFertilizerToKgOrMass.py
--rw-rw-rw-   0 root         (0) root         (0)     1420 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_saplings.py
--rw-rw-rw-   0 root         (0) root         (0)     1192 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_soilTotalNitrogenContent.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/schererPfister2015/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/schererPfister2015/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2199 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_nErosionAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     2199 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pErosionAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1143 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pToDrainageWaterAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1147 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pToGroundwaterAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)     1375 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pToSurfacewaterAllOrigins.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/site/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/site/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/site/measurement/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/site/measurement/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1343 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/site/measurement/test_value.py
--rw-rw-rw-   0 root         (0) root         (0)      360 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/site/test_post_checks.py
--rw-rw-rw-   0 root         (0) root         (0)      358 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/site/test_pre_checks.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/spatial/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1110 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_aware.py
--rw-rw-rw-   0 root         (0) root         (0)     2293 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_clayContent.py
--rw-rw-rw-   0 root         (0) root         (0)     1395 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_croppingIntensity.py
--rw-rw-rw-   0 root         (0) root         (0)     1316 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_drainageClass.py
--rw-rw-rw-   0 root         (0) root         (0)     1712 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_ecoClimateZone.py
--rw-rw-rw-   0 root         (0) root         (0)     1122 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_ecoregion.py
--rw-rw-rw-   0 root         (0) root         (0)     1314 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_erodibility.py
--rw-rw-rw-   0 root         (0) root         (0)     1386 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_fallowCorrection.py
--rw-rw-rw-   0 root         (0) root         (0)     1327 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_heavyWinterPrecipitation.py
--rw-rw-rw-   0 root         (0) root         (0)     1417 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_histosol.py
--rw-rw-rw-   0 root         (0) root         (0)     1335 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_nutrientLossToAquaticEnvironment.py
--rw-rw-rw-   0 root         (0) root         (0)     1619 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_rainfallAnnual.py
--rw-rw-rw-   0 root         (0) root         (0)      898 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_region.py
--rw-rw-rw-   0 root         (0) root         (0)     1308 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_slope.py
--rw-rw-rw-   0 root         (0) root         (0)     1314 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_slopeLength.py
--rw-rw-rw-   0 root         (0) root         (0)     1327 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_soilOrganicCarbonContent.py
--rw-rw-rw-   0 root         (0) root         (0)     1309 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_soilPh.py
--rw-rw-rw-   0 root         (0) root         (0)     1324 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_soilPhosphorusContent.py
--rw-rw-rw-   0 root         (0) root         (0)     1327 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_soilTotalNitrogenContent.py
--rw-rw-rw-   0 root         (0) root         (0)     1614 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/spatial/test_temperatureAnnual.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1807 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)      694 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirCropResidueDecompositionDirect.py
--rw-rw-rw-   0 root         (0) root         (0)      964 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirExcretaDirect.py
--rw-rw-rw-   0 root         (0) root         (0)      976 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirInorganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)      974 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirOrganicFertilizerDirect.py
--rw-rw-rw-   0 root         (0) root         (0)     1696 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)      688 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirCropResidueDecomposition.py
--rw-rw-rw-   0 root         (0) root         (0)      958 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirExcreta.py
--rw-rw-rw-   0 root         (0) root         (0)      970 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)      968 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirOrganicFertilizer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1532 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirAllOrigins.py
--rw-rw-rw-   0 root         (0) root         (0)      739 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirCropResidueDecomposition.py
--rw-rw-rw-   0 root         (0) root         (0)     1064 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirExcreta.py
--rw-rw-rw-   0 root         (0) root         (0)     1076 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirInorganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     1074 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirOrganicFertilizer.py
--rw-rw-rw-   0 root         (0) root         (0)     2064 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/test_otherBackgroundDatabase.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/transformation/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/transformation/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/transformation/post_checks/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/transformation/post_checks/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1317 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/transformation/post_checks/test_product.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/utils/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      417 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_cycle.py
--rw-rw-rw-   0 root         (0) root         (0)     1753 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_dataCompleteness.py
--rw-rw-rw-   0 root         (0) root         (0)      618 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_emission.py
--rw-rw-rw-   0 root         (0) root         (0)      929 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_impact_assessment.py
--rw-rw-rw-   0 root         (0) root         (0)      639 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_indicator.py
--rw-rw-rw-   0 root         (0) root         (0)      591 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_input.py
--rw-rw-rw-   0 root         (0) root         (0)     2745 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_measurement.py
--rw-rw-rw-   0 root         (0) root         (0)      618 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_practice.py
--rw-rw-rw-   0 root         (0) root         (0)     1653 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_product.py
--rw-rw-rw-   0 root         (0) root         (0)      618 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_property.py
--rw-rw-rw-   0 root         (0) root         (0)      680 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_site.py
--rw-rw-rw-   0 root         (0) root         (0)     1008 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/utils/test_term.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:14:05.000000 hestia-earth-models-0.9.0/tests/models/webbEtAl2012AndSintermannEtAl2012/
--rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/webbEtAl2012AndSintermannEtAl2012/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2274 2021-07-21 07:13:51.000000 hestia-earth-models-0.9.0/tests/models/webbEtAl2012AndSintermannEtAl2012/test_nh3ToAirOrganicFertilizer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/
+-rw-rw-rw-   0 root         (0) root         (0)    35149 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/LICENSE
+-rw-rw-rw-   0 root         (0) root         (0)       18 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1842 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     1046 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/
+-rw-rw-rw-   0 root         (0) root         (0)       56 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/
+-rw-rw-rw-   0 root         (0) root         (0)       76 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/agribalyse2016/
+-rw-rw-rw-   0 root         (0) root         (0)      352 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/agribalyse2016/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2291 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/agribalyse2016/machineryInfrastructureDepreciatedAmountPerCycle.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/
+-rw-rw-rw-   0 root         (0) root         (0)      362 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     1514 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/ch4ToAirCropResidueBurning.py
+-rwxrwxrwx   0 root         (0) root         (0)     1520 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/n2OToAirCropResidueBurningDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1514 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/nh3ToAirCropResidueBurning.py
+-rw-rw-rw-   0 root         (0) root         (0)     1514 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/noxToAirCropResidueBurning.py
+-rw-rw-rw-   0 root         (0) root         (0)      502 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/aware/
+-rw-rw-rw-   0 root         (0) root         (0)      343 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/aware/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1973 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/aware/freshwaterWithdrawals.py
+-rw-rw-rw-   0 root         (0) root         (0)     2311 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/aware/scarcityWeightedWaterUse.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/
+-rw-rw-rw-   0 root         (0) root         (0)      358 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1613 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/ch4ToAirNaturalVegetationBurning.py
+-rw-rw-rw-   0 root         (0) root         (0)     1550 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/co2ToAirBiomassAndSoilCarbonStockChange.py
+-rw-rw-rw-   0 root         (0) root         (0)     1619 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/n2OToAirNaturalVegetationBurningDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1049 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/
+-rw-rw-rw-   0 root         (0) root         (0)      355 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1944 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandOccupation.py
+-rw-rw-rw-   0 root         (0) root         (0)     2337 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandTransformation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1572 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/biodiversityLossTotalLandUseEffects.py
+-rw-rw-rw-   0 root         (0) root         (0)     1011 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/
+-rw-rw-rw-   0 root         (0) root         (0)      356 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      769 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialExcludingFate.py
+-rw-rw-rw-   0 root         (0) root         (0)      798 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialIncludingFateAverageEurope.py
+-rw-rw-rw-   0 root         (0) root         (0)      792 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialExcludingFate.py
+-rw-rw-rw-   0 root         (0) root         (0)      814 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialIncludingFateAverageEurope.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/
+-rw-rw-rw-   0 root         (0) root         (0)      343 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/dataCompleteness/
+-rw-rw-rw-   0 root         (0) root         (0)     1473 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/dataCompleteness/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1048 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/dataCompleteness/cropResidue.py
+-rw-rw-rw-   0 root         (0) root         (0)      692 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/dataCompleteness/soilAmendments.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/
+-rw-rw-rw-   0 root         (0) root         (0)     2114 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      280 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioCarbon.py
+-rw-rw-rw-   0 root         (0) root         (0)      439 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioDryMatter.py
+-rw-rw-rw-   0 root         (0) root         (0)      272 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioEnergy.py
+-rw-rw-rw-   0 root         (0) root         (0)      386 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioFedWeight.py
+-rw-rw-rw-   0 root         (0) root         (0)      485 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/feedConversionRatioNitrogen.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3833 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/aggregated.py
+-rw-rw-rw-   0 root         (0) root         (0)      552 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/ecoinventV3.py
+-rw-rw-rw-   0 root         (0) root         (0)      961 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/value.py
+-rw-rw-rw-   0 root         (0) root         (0)     1386 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/irrigated.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/post_checks/
+-rw-rw-rw-   0 root         (0) root         (0)      318 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/post_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      334 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/post_checks/site.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/pre_checks/
+-rw-rw-rw-   0 root         (0) root         (0)      395 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/pre_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      420 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/pre_checks/site.py
+-rw-rw-rw-   0 root         (0) root         (0)      877 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/pre_checks/startDate.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1823 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/economicValueShare.py
+-rw-rw-rw-   0 root         (0) root         (0)     2304 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/price.py
+-rw-rw-rw-   0 root         (0) root         (0)     1484 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/primary.py
+-rw-rw-rw-   0 root         (0) root         (0)      973 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/revenue.py
+-rw-rw-rw-   0 root         (0) root         (0)      999 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/value.py
+-rw-rw-rw-   0 root         (0) root         (0)      608 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/cycle/siteDuration.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/data/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/data/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/data/impact_assessments/
+-rw-rw-rw-   0 root         (0) root         (0)      446 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/data/impact_assessments/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1257 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/data/impact_assessments/download.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/deRuijterEtAl2010/
+-rw-rw-rw-   0 root         (0) root         (0)      355 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/deRuijterEtAl2010/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1968 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/deRuijterEtAl2010/nh3ToAirCropResidueDecomposition.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/
+-rw-rw-rw-   0 root         (0) root         (0)      349 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     1591 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/co2ToAirFuelCombustion.py
+-rwxrwxrwx   0 root         (0) root         (0)     1604 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/n2OToAirFuelCombustionDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     5451 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/nh3ToAirInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1598 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/noxToAirFuelCombustion.py
+-rw-rw-rw-   0 root         (0) root         (0)     1600 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/so2ToAirFuelCombustion.py
+-rw-rw-rw-   0 root         (0) root         (0)      861 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/faostat2018/
+-rw-rw-rw-   0 root         (0) root         (0)      349 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/faostat2018/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2582 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/faostat2018/seed.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/globalCropWaterModel2008/
+-rw-rw-rw-   0 root         (0) root         (0)      362 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/globalCropWaterModel2008/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3157 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/globalCropWaterModel2008/rootingDepth.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/
+-rw-rw-rw-   0 root         (0) root         (0)      355 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1576 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/emissions.py
+-rw-rw-rw-   0 root         (0) root         (0)      308 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/irrigated.py
+-rw-rw-rw-   0 root         (0) root         (0)      302 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/organic.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/post_checks/
+-rw-rw-rw-   0 root         (0) root         (0)      332 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/post_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      347 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/post_checks/cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)      342 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/post_checks/site.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/pre_checks/
+-rw-rw-rw-   0 root         (0) root         (0)      331 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/pre_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      538 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/pre_checks/cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)      428 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/pre_checks/site.py
+-rw-rw-rw-   0 root         (0) root         (0)      744 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/product.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/
+-rw-rw-rw-   0 root         (0) root         (0)      346 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4128 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/aboveGroundCropResidue.py
+-rw-rw-rw-   0 root         (0) root         (0)     2163 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/aboveGroundCropResidueRemoved.py
+-rw-rw-rw-   0 root         (0) root         (0)     4228 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/aboveGroundCropResidueTotal.py
+-rw-rw-rw-   0 root         (0) root         (0)     3741 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/belowGroundCropResidue.py
+-rw-rw-rw-   0 root         (0) root         (0)     2917 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/co2ToAirOrganicSoilCultivation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1658 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirCropResidueDecompositionIndirect.py
+-rwxrwxrwx   0 root         (0) root         (0)     1535 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirExcretaDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1797 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirExcretaIndirect.py
+-rwxrwxrwx   0 root         (0) root         (0)     1601 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1870 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerIndirect.py
+-rwxrwxrwx   0 root         (0) root         (0)     1595 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1858 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerIndirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     2838 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirOrganicSoilCultivationDirect.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/
+-rw-rw-rw-   0 root         (0) root         (0)     3033 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1144 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/residueBurnt.py
+-rw-rw-rw-   0 root         (0) root         (0)       62 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/residueIncorporated.py
+-rw-rw-rw-   0 root         (0) root         (0)       31 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/residueLeftOnField.py
+-rw-rw-rw-   0 root         (0) root         (0)      964 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/residueRemoved.py
+-rw-rw-rw-   0 root         (0) root         (0)     1344 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013ExcludingFeedbacks/
+-rw-rw-rw-   0 root         (0) root         (0)      364 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013ExcludingFeedbacks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      742 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013ExcludingFeedbacks/gwp100.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013IncludingFeedbacks/
+-rw-rw-rw-   0 root         (0) root         (0)      364 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013IncludingFeedbacks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      742 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013IncludingFeedbacks/gwp100.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/
+-rw-rw-rw-   0 root         (0) root         (0)      346 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     5306 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/ch4ToAirEntericFermentation.py
+-rw-rw-rw-   0 root         (0) root         (0)     5129 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/ch4ToAirFloodedRice.py
+-rw-rw-rw-   0 root         (0) root         (0)     2339 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/co2ToAirLimeHydrolysis.py
+-rw-rw-rw-   0 root         (0) root         (0)     2722 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/co2ToAirUreaHydrolysis.py
+-rw-rw-rw-   0 root         (0) root         (0)     1990 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/croppingDuration.py
+-rw-rw-rw-   0 root         (0) root         (0)     2770 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/nitrogenContent.py
+-rw-rw-rw-   0 root         (0) root         (0)     1435 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/log.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/otherBackgroundDatabase/
+-rw-rw-rw-   0 root         (0) root         (0)     2699 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/otherBackgroundDatabase/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/
+-rw-rw-rw-   0 root         (0) root         (0)      354 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1603 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/landOccupation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1853 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/n2OToAirAquaculturePondsDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1698 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/n2ToAirAquaculturePonds.py
+-rw-rw-rw-   0 root         (0) root         (0)     1772 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/netPrimaryProduction.py
+-rwxrwxrwx   0 root         (0) root         (0)     2568 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/nh3ToAirAquaculturePonds.py
+-rw-rw-rw-   0 root         (0) root         (0)     4002 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1232 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterCropResidueDecomposition.py
+-rw-rw-rw-   0 root         (0) root         (0)     1168 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterExcreta.py
+-rw-rw-rw-   0 root         (0) root         (0)     1186 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1180 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterOrganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1845 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/noxToAirAquaculturePonds.py
+-rw-rw-rw-   0 root         (0) root         (0)     1652 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/nurseryDuration.py
+-rw-rw-rw-   0 root         (0) root         (0)     1650 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/orchardDensity.py
+-rw-rw-rw-   0 root         (0) root         (0)     1747 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/orchardDuration.py
+-rw-rw-rw-   0 root         (0) root         (0)     3271 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/organicFertilizerToKgOrMass.py
+-rw-rw-rw-   0 root         (0) root         (0)     1612 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/saplings.py
+-rw-rw-rw-   0 root         (0) root         (0)     1649 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/totalNitrogenPerKgSoil.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/
+-rw-rw-rw-   0 root         (0) root         (0)      356 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3397 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/nErosionAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     3398 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pErosionAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1598 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pToDrainageWaterAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1597 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pToGroundwaterAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     2040 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pToSurfacewaterAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     3252 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/
+-rw-rw-rw-   0 root         (0) root         (0)      342 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/measurement/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/measurement/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1075 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/measurement/value.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/post_checks/
+-rw-rw-rw-   0 root         (0) root         (0)      249 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/post_checks/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/pre_checks/
+-rw-rw-rw-   0 root         (0) root         (0)      249 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/site/pre_checks/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/
+-rw-rw-rw-   0 root         (0) root         (0)      345 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      856 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/aware.py
+-rw-rw-rw-   0 root         (0) root         (0)     3120 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/clayContent.py
+-rw-rw-rw-   0 root         (0) root         (0)     2261 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/croppingIntensity.py
+-rw-rw-rw-   0 root         (0) root         (0)     1432 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/drainageClass.py
+-rw-rw-rw-   0 root         (0) root         (0)     1495 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/ecoClimateZone.py
+-rw-rw-rw-   0 root         (0) root         (0)     1055 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/ecoregion.py
+-rw-rw-rw-   0 root         (0) root         (0)     1400 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/erodibility.py
+-rw-rw-rw-   0 root         (0) root         (0)     2254 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/fallowCorrection.py
+-rw-rw-rw-   0 root         (0) root         (0)     1561 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/heavyWinterPrecipitation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1590 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/histosol.py
+-rw-rw-rw-   0 root         (0) root         (0)     1454 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/nutrientLossToAquaticEnvironment.py
+-rw-rw-rw-   0 root         (0) root         (0)     1468 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/organicCarbonPerKgSoil.py
+-rw-rw-rw-   0 root         (0) root         (0)     1512 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/phosphorusPerKgSoil.py
+-rw-rw-rw-   0 root         (0) root         (0)     2925 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/rainfallAnnual.py
+-rw-rw-rw-   0 root         (0) root         (0)     1338 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/region.py
+-rw-rw-rw-   0 root         (0) root         (0)     1410 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/slope.py
+-rw-rw-rw-   0 root         (0) root         (0)     1425 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/slopeLength.py
+-rw-rw-rw-   0 root         (0) root         (0)     1457 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/soilPh.py
+-rw-rw-rw-   0 root         (0) root         (0)     2886 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/temperatureAnnual.py
+-rw-rw-rw-   0 root         (0) root         (0)     1558 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/totalNitrogenPerKgSoil.py
+-rw-rw-rw-   0 root         (0) root         (0)     3032 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/spatial/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/
+-rw-rw-rw-   0 root         (0) root         (0)      357 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4801 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1366 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirCropResidueDecompositionDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1201 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirExcretaDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1213 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirInorganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1207 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirOrganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     3165 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1145 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirCropResidueDecomposition.py
+-rw-rw-rw-   0 root         (0) root         (0)     1242 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirExcreta.py
+-rw-rw-rw-   0 root         (0) root         (0)     1260 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1254 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirOrganicFertilizer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/
+-rw-rw-rw-   0 root         (0) root         (0)      374 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2100 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1054 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirCropResidueDecomposition.py
+-rw-rw-rw-   0 root         (0) root         (0)     1151 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirExcreta.py
+-rw-rw-rw-   0 root         (0) root         (0)     1169 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1163 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirOrganicFertilizer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/transformation/
+-rw-rw-rw-   0 root         (0) root         (0)      352 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/transformation/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/transformation/post_checks/
+-rw-rw-rw-   0 root         (0) root         (0)      333 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/transformation/post_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1787 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/transformation/post_checks/product.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/
+-rw-rw-rw-   0 root         (0) root         (0)     2020 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2252 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/blank_node.py
+-rw-rw-rw-   0 root         (0) root         (0)     2882 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/constant.py
+-rw-rw-rw-   0 root         (0) root         (0)     1524 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/crop.py
+-rw-rw-rw-   0 root         (0) root         (0)     4750 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)      484 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/dataCompleteness.py
+-rw-rw-rw-   0 root         (0) root         (0)     1025 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/ecoClimateZone.py
+-rw-rw-rw-   0 root         (0) root         (0)      421 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/emission.py
+-rw-rw-rw-   0 root         (0) root         (0)     1950 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/impact_assessment.py
+-rw-rw-rw-   0 root         (0) root         (0)      423 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/indicator.py
+-rw-rw-rw-   0 root         (0) root         (0)     1135 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/inorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     8838 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/input.py
+-rw-rw-rw-   0 root         (0) root         (0)     2017 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/measurement.py
+-rw-rw-rw-   0 root         (0) root         (0)     1263 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/practice.py
+-rw-rw-rw-   0 root         (0) root         (0)     2321 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/product.py
+-rw-rw-rw-   0 root         (0) root         (0)     2441 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/property.py
+-rw-rw-rw-   0 root         (0) root         (0)     1324 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/site.py
+-rw-rw-rw-   0 root         (0) root         (0)     2549 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/utils/term.py
+-rw-rw-rw-   0 root         (0) root         (0)       18 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/version.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/
+-rw-rw-rw-   0 root         (0) root         (0)      371 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3542 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/nh3ToAirOrganicFertilizer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth_models.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1842 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth_models.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    22176 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth_models.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth_models.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      100 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth_models.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       19 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/hestia_earth_models.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     1382 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/agribalyse2016/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/agribalyse2016/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1159 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/agribalyse2016/test_machineryInfrastructureDepreciatedAmountPerCycle.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     1575 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_ch4ToAirCropResidueBurning.py
+-rwxrwxrwx   0 root         (0) root         (0)     1587 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_n2OToAirCropResidueBurningDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1575 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_nh3ToAirCropResidueBurning.py
+-rw-rw-rw-   0 root         (0) root         (0)     1575 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_noxToAirCropResidueBurning.py
+-rw-rw-rw-   0 root         (0) root         (0)     1134 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/aware/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/aware/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1246 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/aware/test_freshwaterWithdrawals.py
+-rw-rw-rw-   0 root         (0) root         (0)     1594 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/aware/test_scarcityWeightedWaterUse.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1171 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/test_ch4ToAirNaturalVegetationBurning.py
+-rw-rw-rw-   0 root         (0) root         (0)     1178 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/test_co2ToAirBiomassAndSoilCarbonStockChange.py
+-rw-rw-rw-   0 root         (0) root         (0)     1177 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/test_n2OToAirNaturalVegetationBurningDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)      444 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/test_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1566 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/test_biodiversityLossLandOccupation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1722 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/test_biodiversityLossLandTransformation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1092 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/test_biodiversityLossTotalLandUseEffects.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      912 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_eutrophicationPotentialExcludingFate.py
+-rw-rw-rw-   0 root         (0) root         (0)      925 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_eutrophicationPotentialIncludingFateAverageEurope.py
+-rw-rw-rw-   0 root         (0) root         (0)      922 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialExcludingFate.py
+-rw-rw-rw-   0 root         (0) root         (0)      941 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialIncludingFateAverageEurope.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/cycle/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/cycle/dataCompleteness/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/dataCompleteness/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      613 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/dataCompleteness/test_cropResidue.py
+-rw-rw-rw-   0 root         (0) root         (0)      620 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/dataCompleteness/test_soilAmendments.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/cycle/input/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/input/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2348 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/input/test_aggregated.py
+-rw-rw-rw-   0 root         (0) root         (0)      514 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/input/test_ecoinventV3.py
+-rw-rw-rw-   0 root         (0) root         (0)     1049 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/input/test_value.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/cycle/post_checks/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/post_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      621 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/post_checks/test_site.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/cycle/pre_checks/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/pre_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      694 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/pre_checks/test_site.py
+-rw-rw-rw-   0 root         (0) root         (0)     1367 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/pre_checks/test_startDate.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/cycle/product/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/product/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1529 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/product/test_economicValueShare.py
+-rw-rw-rw-   0 root         (0) root         (0)      893 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/product/test_price.py
+-rw-rw-rw-   0 root         (0) root         (0)     2342 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/product/test_primary.py
+-rw-rw-rw-   0 root         (0) root         (0)     1126 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/product/test_revenue.py
+-rw-rw-rw-   0 root         (0) root         (0)     1073 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/product/test_value.py
+-rw-rw-rw-   0 root         (0) root         (0)      850 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/test_dataCompleteness.py
+-rw-rw-rw-   0 root         (0) root         (0)     1504 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/test_feedConversionRatio.py
+-rw-rw-rw-   0 root         (0) root         (0)     1090 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/test_irrigated.py
+-rw-rw-rw-   0 root         (0) root         (0)      362 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/test_post_checks.py
+-rw-rw-rw-   0 root         (0) root         (0)      360 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/test_pre_checks.py
+-rw-rw-rw-   0 root         (0) root         (0)      872 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/cycle/test_siteDuration.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/deRuijterEtAl2010/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/deRuijterEtAl2010/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1636 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/deRuijterEtAl2010/test_nh3ToAirCropResidueDecomposition.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     1846 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_co2ToAirFuelCombustion.py
+-rwxrwxrwx   0 root         (0) root         (0)     1852 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_n2OToAirFuelCombustionDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1993 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_nh3ToAirInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1846 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_noxToAirFuelCombustion.py
+-rw-rw-rw-   0 root         (0) root         (0)     1846 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_so2ToAirFuelCombustion.py
+-rw-rw-rw-   0 root         (0) root         (0)      947 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/faostat2018/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/faostat2018/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1758 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/faostat2018/test_seed.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/globalCropWaterModel2008/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/globalCropWaterModel2008/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2075 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/globalCropWaterModel2008/test_rootingDepth.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/post_checks/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/post_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      661 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/post_checks/test_cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)      648 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/post_checks/test_site.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/pre_checks/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/pre_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      967 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/pre_checks/test_cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)      832 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/pre_checks/test_site.py
+-rw-rw-rw-   0 root         (0) root         (0)     1184 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/test_emissions.py
+-rw-rw-rw-   0 root         (0) root         (0)      377 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/test_irrigated.py
+-rw-rw-rw-   0 root         (0) root         (0)      375 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/test_oganic.py
+-rw-rw-rw-   0 root         (0) root         (0)      386 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/test_post_checks.py
+-rw-rw-rw-   0 root         (0) root         (0)      384 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/test_pre_checks.py
+-rw-rw-rw-   0 root         (0) root         (0)      959 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/impact_assessment/test_product.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/residue/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/residue/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      401 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/residue/test_residueBurnt.py
+-rw-rw-rw-   0 root         (0) root         (0)      112 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/residue/test_residueIncorporated.py
+-rw-rw-rw-   0 root         (0) root         (0)      387 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/residue/test_residueRemoved.py
+-rw-rw-rw-   0 root         (0) root         (0)     1177 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_aboveGroundCropResidue.py
+-rw-rw-rw-   0 root         (0) root         (0)     1169 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_aboveGroundCropResidueRemoved.py
+-rw-rw-rw-   0 root         (0) root         (0)     3181 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_aboveGroundCropResidueTotal.py
+-rw-rw-rw-   0 root         (0) root         (0)     2100 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_belowGroundCropResidue.py
+-rw-rw-rw-   0 root         (0) root         (0)     1747 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_co2ToAirOrganicSoilCultivation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1147 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirCropResidueDecompositionIndirect.py
+-rwxrwxrwx   0 root         (0) root         (0)     2000 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirExcretaDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1427 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirExcretaIndirect.py
+-rwxrwxrwx   0 root         (0) root         (0)     1554 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1385 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerIndirect.py
+-rwxrwxrwx   0 root         (0) root         (0)     1550 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1786 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerIndirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1196 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirOrganicSoilCultivationDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1332 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2006/test_residue.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/ipcc2013ExcludingFeedbacks/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2013ExcludingFeedbacks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      906 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2013ExcludingFeedbacks/test_gwp100.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/ipcc2013IncludingFeedbacks/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2013IncludingFeedbacks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      906 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2013IncludingFeedbacks/test_gwp100.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3445 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/test_ch4ToAirEntericFermentation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1701 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/test_ch4ToAirFloodedRice.py
+-rw-rw-rw-   0 root         (0) root         (0)     1404 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/test_co2ToAirLimeHydrolysis.py
+-rw-rw-rw-   0 root         (0) root         (0)     1583 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/test_co2ToAirUreaHydrolysis.py
+-rw-rw-rw-   0 root         (0) root         (0)     1424 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/test_croppingDuration.py
+-rw-rw-rw-   0 root         (0) root         (0)     1930 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/ipcc2019/test_nitrogenContent.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1708 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_landOccupation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1761 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_n2OToAirAquaculturePondsDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1754 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_n2ToAirAquaculturePonds.py
+-rw-rw-rw-   0 root         (0) root         (0)     1071 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_netPrimaryProduction.py
+-rwxrwxrwx   0 root         (0) root         (0)     2477 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_nh3ToAirAquaculturePonds.py
+-rw-rw-rw-   0 root         (0) root         (0)     2731 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)      687 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterCropResidueDecomposition.py
+-rw-rw-rw-   0 root         (0) root         (0)      670 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterExcreta.py
+-rw-rw-rw-   0 root         (0) root         (0)      682 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)      680 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterOrganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1747 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_noxToAirAquaculturePonds.py
+-rw-rw-rw-   0 root         (0) root         (0)     1442 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_nurseryDuration.py
+-rw-rw-rw-   0 root         (0) root         (0)     1441 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_orchardDensity.py
+-rw-rw-rw-   0 root         (0) root         (0)     1442 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_orchardDuration.py
+-rw-rw-rw-   0 root         (0) root         (0)     1959 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_organicFertilizerToKgOrMass.py
+-rw-rw-rw-   0 root         (0) root         (0)     1420 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_saplings.py
+-rw-rw-rw-   0 root         (0) root         (0)     1132 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_totalNitrogenPerKgSoil.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/schererPfister2015/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/schererPfister2015/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2199 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_nErosionAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     2199 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pErosionAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1143 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pToDrainageWaterAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1147 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pToGroundwaterAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)     1375 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pToSurfacewaterAllOrigins.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/site/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/site/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/site/measurement/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/site/measurement/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1343 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/site/measurement/test_value.py
+-rw-rw-rw-   0 root         (0) root         (0)      360 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/site/test_post_checks.py
+-rw-rw-rw-   0 root         (0) root         (0)      358 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/site/test_pre_checks.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/spatial/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1110 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_aware.py
+-rw-rw-rw-   0 root         (0) root         (0)     2293 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_clayContent.py
+-rw-rw-rw-   0 root         (0) root         (0)     1395 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_croppingIntensity.py
+-rw-rw-rw-   0 root         (0) root         (0)     1316 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_drainageClass.py
+-rw-rw-rw-   0 root         (0) root         (0)     1712 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_ecoClimateZone.py
+-rw-rw-rw-   0 root         (0) root         (0)     1122 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_ecoregion.py
+-rw-rw-rw-   0 root         (0) root         (0)     1314 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_erodibility.py
+-rw-rw-rw-   0 root         (0) root         (0)     1386 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_fallowCorrection.py
+-rw-rw-rw-   0 root         (0) root         (0)     1327 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_heavyWinterPrecipitation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1417 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_histosol.py
+-rw-rw-rw-   0 root         (0) root         (0)     1335 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_nutrientLossToAquaticEnvironment.py
+-rw-rw-rw-   0 root         (0) root         (0)     1325 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_organicCarbonPerKgSoil.py
+-rw-rw-rw-   0 root         (0) root         (0)     1322 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_phosphorusPerKgSoil.py
+-rw-rw-rw-   0 root         (0) root         (0)     1619 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_rainfallAnnual.py
+-rw-rw-rw-   0 root         (0) root         (0)      898 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_region.py
+-rw-rw-rw-   0 root         (0) root         (0)     1308 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_slope.py
+-rw-rw-rw-   0 root         (0) root         (0)     1314 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_slopeLength.py
+-rw-rw-rw-   0 root         (0) root         (0)     1309 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_soilPh.py
+-rw-rw-rw-   0 root         (0) root         (0)     1614 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_temperatureAnnual.py
+-rw-rw-rw-   0 root         (0) root         (0)     1325 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/spatial/test_totalNitrogenPerKgSoil.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1609 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)      694 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirCropResidueDecompositionDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)      964 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirExcretaDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)      976 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirInorganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)      974 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirOrganicFertilizerDirect.py
+-rw-rw-rw-   0 root         (0) root         (0)     1506 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)      688 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirCropResidueDecomposition.py
+-rw-rw-rw-   0 root         (0) root         (0)      958 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirExcreta.py
+-rw-rw-rw-   0 root         (0) root         (0)      970 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)      968 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirOrganicFertilizer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1386 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirAllOrigins.py
+-rw-rw-rw-   0 root         (0) root         (0)      739 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirCropResidueDecomposition.py
+-rw-rw-rw-   0 root         (0) root         (0)     1064 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirExcreta.py
+-rw-rw-rw-   0 root         (0) root         (0)     1076 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirInorganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     1074 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirOrganicFertilizer.py
+-rw-rw-rw-   0 root         (0) root         (0)     2064 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/test_otherBackgroundDatabase.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/transformation/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/transformation/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/transformation/post_checks/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/transformation/post_checks/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1317 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/transformation/post_checks/test_product.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/utils/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      417 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)     1753 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_dataCompleteness.py
+-rw-rw-rw-   0 root         (0) root         (0)      618 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_emission.py
+-rw-rw-rw-   0 root         (0) root         (0)      929 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_impact_assessment.py
+-rw-rw-rw-   0 root         (0) root         (0)      639 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_indicator.py
+-rw-rw-rw-   0 root         (0) root         (0)      591 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_input.py
+-rw-rw-rw-   0 root         (0) root         (0)     2745 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_measurement.py
+-rw-rw-rw-   0 root         (0) root         (0)      618 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_practice.py
+-rw-rw-rw-   0 root         (0) root         (0)     1653 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_product.py
+-rw-rw-rw-   0 root         (0) root         (0)      618 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_property.py
+-rw-rw-rw-   0 root         (0) root         (0)      680 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_site.py
+-rw-rw-rw-   0 root         (0) root         (0)     1008 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/utils/test_term.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-07-21 07:27:40.000000 hestia-earth-models-0.9.1/tests/models/webbEtAl2012AndSintermannEtAl2012/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/webbEtAl2012AndSintermannEtAl2012/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2274 2021-07-21 07:27:26.000000 hestia-earth-models-0.9.1/tests/models/webbEtAl2012AndSintermannEtAl2012/test_nh3ToAirOrganicFertilizer.py
```

### Comparing `hestia-earth-models-0.9.0/LICENSE` & `hestia-earth-models-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/PKG-INFO` & `hestia-earth-models-0.9.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hestia-earth-models
-Version: 0.9.0
+Version: 0.9.1
 Summary: Hestia's set of modules for filling gaps in the activity data using external datasets (e.g. populating soil properties with a geospatial dataset using provided coordinates) and internal lookups (e.g. populating machinery use from fuel use). Includes rules for when gaps should be filled versus not (e.g. never gap fill yield, gap fill crop residue if yield provided etc.).
 Home-page: https://gitlab.com/hestia-earth/hestia-engine-models
 Author: Hestia Team
 Author-email: guillaumeroyer.mail@gmail.com
 License: GPL
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `hestia-earth-models-0.9.0/README.md` & `hestia-earth-models-0.9.1/README.md`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/agribalyse2016/machineryInfrastructureDepreciatedAmountPerCycle.py` & `hestia-earth-models-0.9.1/hestia_earth/models/agribalyse2016/machineryInfrastructureDepreciatedAmountPerCycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/ch4ToAirCropResidueBurning.py` & `hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/ch4ToAirCropResidueBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/n2OToAirCropResidueBurningDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/n2OToAirCropResidueBurningDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/nh3ToAirCropResidueBurning.py` & `hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/nh3ToAirCropResidueBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/akagiEtAl2011AndIpcc2006/noxToAirCropResidueBurning.py` & `hestia-earth-models-0.9.1/hestia_earth/models/akagiEtAl2011AndIpcc2006/noxToAirCropResidueBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/aware/freshwaterWithdrawals.py` & `hestia-earth-models-0.9.1/hestia_earth/models/aware/freshwaterWithdrawals.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/aware/scarcityWeightedWaterUse.py` & `hestia-earth-models-0.9.1/hestia_earth/models/aware/scarcityWeightedWaterUse.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/ch4ToAirNaturalVegetationBurning.py` & `hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/ch4ToAirNaturalVegetationBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/co2ToAirBiomassAndSoilCarbonStockChange.py` & `hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/co2ToAirBiomassAndSoilCarbonStockChange.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/n2OToAirNaturalVegetationBurningDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/n2OToAirNaturalVegetationBurningDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/blonkConsultants2016/utils.py` & `hestia-earth-models-0.9.1/hestia_earth/models/blonkConsultants2016/utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandOccupation.py` & `hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandOccupation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandTransformation.py` & `hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/biodiversityLossLandTransformation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/biodiversityLossTotalLandUseEffects.py` & `hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/biodiversityLossTotalLandUseEffects.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/chaudharyEtAl2015/utils.py` & `hestia-earth-models-0.9.1/hestia_earth/models/chaudharyEtAl2015/utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialExcludingFate.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialExcludingFate.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialIncludingFateAverageEurope.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/eutrophicationPotentialIncludingFateAverageEurope.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialExcludingFate.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialExcludingFate.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialIncludingFateAverageEurope.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cml2001NonBaseline/terrestrialAcidificationPotentialIncludingFateAverageEurope.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/dataCompleteness/__init__.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/dataCompleteness/__init__.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/dataCompleteness/cropResidue.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/dataCompleteness/cropResidue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/dataCompleteness/soilAmendments.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/dataCompleteness/soilAmendments.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/feedConversionRatio/__init__.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/feedConversionRatio/__init__.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/aggregated.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/aggregated.py`

 * *Files 6% similar despite different names*

```diff
@@ -4,16 +4,14 @@
 from hestia_earth.utils.model import find_primary_product, find_term_match, linked_node
 from hestia_earth.utils.tools import non_empty_list, safe_parse_date
 
 from hestia_earth.models.log import logger
 from hestia_earth.models.utils.cycle import is_organic, is_irrigated, valid_site_type
 MODEL = 'aggregated'
 MODEL_KEY = 'impactAssessment'
-HESTIA_BIBLIO_TITLE = 'Hestia: A new data platform for storing and analysing data on the productivity \
-and sustainability of agriculture'
 SEED_TERM_ID = 'seed'
 
 
 def _name_suffix(cycle: dict):
     return '-'.join(non_empty_list([
         'Organic' if is_organic(cycle) else 'Conventional',
         'Irrigated' if is_irrigated(cycle) else 'Non Irrigated'
@@ -26,15 +24,15 @@
 
 
 def _find_closest_impact(cycle: dict, country: dict, end_date: str, input: dict):
     query = {
         'bool': {
             'must': [
                 {'match': {'@type': SchemaType.IMPACTASSESSMENT.value}},
-                {'match': {'source.bibliography.title.keyword': HESTIA_BIBLIO_TITLE}},
+                {'match': {'aggregated': 'true'}},
                 {'match': {'product.name.keyword': input.get('term', {}).get('name')}},
                 {
                     'bool': {
                         # either get with exact country, or default to global
                         'should': [
                             {'match': {'country.name.keyword': {'query': country.get('name'), 'boost': 1000}}},
                             {'match': {'country.name.keyword': {'query': 'World', 'boost': 1}}}
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/ecoinventV3.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/ecoinventV3.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/input/value.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/input/value.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/irrigated.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/irrigated.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/pre_checks/startDate.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/pre_checks/startDate.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/economicValueShare.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/economicValueShare.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/price.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/price.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/primary.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/primary.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/revenue.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/revenue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/product/value.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/product/value.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/cycle/siteDuration.py` & `hestia-earth-models-0.9.1/hestia_earth/models/cycle/siteDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/data/impact_assessments/download.py` & `hestia-earth-models-0.9.1/hestia_earth/models/data/impact_assessments/download.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/deRuijterEtAl2010/nh3ToAirCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/hestia_earth/models/deRuijterEtAl2010/nh3ToAirCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/co2ToAirFuelCombustion.py` & `hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/co2ToAirFuelCombustion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/n2OToAirFuelCombustionDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/n2OToAirFuelCombustionDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/nh3ToAirInorganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/nh3ToAirInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/noxToAirFuelCombustion.py` & `hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/noxToAirFuelCombustion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/so2ToAirFuelCombustion.py` & `hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/so2ToAirFuelCombustion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/emeaEea2019/utils.py` & `hestia-earth-models-0.9.1/hestia_earth/models/emeaEea2019/utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/faostat2018/seed.py` & `hestia-earth-models-0.9.1/hestia_earth/models/faostat2018/seed.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/globalCropWaterModel2008/rootingDepth.py` & `hestia-earth-models-0.9.1/hestia_earth/models/globalCropWaterModel2008/rootingDepth.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/emissions.py` & `hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/emissions.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/pre_checks/cycle.py` & `hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/pre_checks/cycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/impact_assessment/product.py` & `hestia-earth-models-0.9.1/hestia_earth/models/impact_assessment/product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/aboveGroundCropResidue.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/aboveGroundCropResidue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/aboveGroundCropResidueRemoved.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/aboveGroundCropResidueRemoved.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/aboveGroundCropResidueTotal.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/aboveGroundCropResidueTotal.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/belowGroundCropResidue.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/belowGroundCropResidue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/co2ToAirOrganicSoilCultivation.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/co2ToAirOrganicSoilCultivation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirCropResidueDecompositionIndirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirCropResidueDecompositionIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirExcretaDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirExcretaDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirExcretaIndirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirExcretaIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerIndirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirInorganicFertilizerIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerIndirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirOrganicFertilizerIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/n2OToAirOrganicSoilCultivationDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/n2OToAirOrganicSoilCultivationDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/__init__.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/__init__.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/residueBurnt.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/residueBurnt.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/residue/residueRemoved.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/residue/residueRemoved.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2006/utils.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2006/utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013ExcludingFeedbacks/gwp100.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013ExcludingFeedbacks/gwp100.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2013IncludingFeedbacks/gwp100.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2013IncludingFeedbacks/gwp100.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/ch4ToAirEntericFermentation.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/ch4ToAirEntericFermentation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/ch4ToAirFloodedRice.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/ch4ToAirFloodedRice.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/co2ToAirLimeHydrolysis.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/co2ToAirLimeHydrolysis.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/co2ToAirUreaHydrolysis.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/co2ToAirUreaHydrolysis.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/croppingDuration.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/croppingDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/ipcc2019/nitrogenContent.py` & `hestia-earth-models-0.9.1/hestia_earth/models/ipcc2019/nitrogenContent.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/log.py` & `hestia-earth-models-0.9.1/hestia_earth/models/log.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/otherBackgroundDatabase/__init__.py` & `hestia-earth-models-0.9.1/hestia_earth/models/otherBackgroundDatabase/__init__.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/landOccupation.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/landOccupation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/n2OToAirAquaculturePondsDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/n2OToAirAquaculturePondsDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/n2ToAirAquaculturePonds.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/n2ToAirAquaculturePonds.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/netPrimaryProduction.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/netPrimaryProduction.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/nh3ToAirAquaculturePonds.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/nh3ToAirAquaculturePonds.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterExcreta.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterExcreta.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterInorganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterOrganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/no3ToGroundwaterOrganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/noxToAirAquaculturePonds.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/noxToAirAquaculturePonds.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/nurseryDuration.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/nurseryDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/orchardDensity.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/orchardDensity.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/orchardDuration.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/orchardDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/organicFertilizerToKgOrMass.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/organicFertilizerToKgOrMass.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/saplings.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/saplings.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/pooreNemecek2018/soilTotalNitrogenContent.py` & `hestia-earth-models-0.9.1/hestia_earth/models/pooreNemecek2018/totalNitrogenPerKgSoil.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,35 +3,35 @@
 from hestia_earth.utils.tools import list_average
 
 from hestia_earth.models.log import debugRequirements, logger
 from hestia_earth.models.utils import is_from_model
 from hestia_earth.models.utils.measurement import _new_measurement
 from . import MODEL
 
-TERM_ID = 'soilTotalNitrogenContent'
+TERM_ID = 'totalNitrogenPerKgSoil'
 BIBLIO_TITLE = 'Reducing food’s environmental impacts through producers and consumers'
 
 
 def _measurement(value: float):
     logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
     measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
     measurement['value'] = [value]
     measurement['depthUpper'] = 0
     measurement['depthLower'] = 50
     measurement['statsDefinition'] = MeasurementStatsDefinition.MODELLED.value
     return measurement
 
 
 def _run(carbon_content: float):
-    value = 0.0000601 * (carbon_content / 100 * 5000 * 1300) / 11 * 1000
+    value = 0.0000601 * (carbon_content * 1000 * 5000 * 1300) / 11
     return [_measurement(value)]
 
 
 def _should_run(site: dict):
-    carbon_content = find_term_match(site.get('measurements', []), 'soilOrganicCarbonContent')
+    carbon_content = find_term_match(site.get('measurements', []), 'organicCarbonPerKgSoil')
     carbon_content_value = carbon_content.get('value', [])
 
     debugRequirements(model=MODEL, term=TERM_ID,
                       carbon_content_value=carbon_content_value)
 
     should_run = not is_from_model(carbon_content) and len(carbon_content_value) > 0
     logger.info('model=%s, term=%s, should_run=%s', MODEL, TERM_ID, should_run)
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/nErosionAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pErosionAllOrigins.py`

 * *Files 4% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from hestia_earth.models.log import logger
 from hestia_earth.models.utils.emission import _new_emission
 from hestia_earth.models.utils.measurement import most_relevant_measurement_value
 from hestia_earth.models.utils.cycle import valid_site_type
 from .utils import get_pcorr, get_p_ef_c1, get_ef_p_c2, get_practice_factor, get_water, calculate_R, calculate_A
 from . import MODEL
 
-TERM_ID = 'nErosionAllOrigins'
+TERM_ID = 'pErosionAllOrigins'
 
 
 def _emission(value: float):
     logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
     emission = _new_emission(TERM_ID, MODEL)
     emission['value'] = [value]
     emission['methodTier'] = EmissionMethodTier.TIER_1.value
@@ -23,30 +23,30 @@
 def _run(list_of_contents_for_A: list, list_of_contents_for_R: list, list_of_contents_for_value: list):
     heavy_winter_precipitation, water = list_of_contents_for_R
     R = calculate_R(heavy_winter_precipitation, water)
 
     practise_factor, erodability, slope_length, pcorr, p_ef_c1, ef_p_c2 = list_of_contents_for_A
     A = calculate_A(R, practise_factor, erodability, slope_length, pcorr, p_ef_c1, ef_p_c2)
 
-    nla_environment, N_content = list_of_contents_for_value
-    logger.debug('R=%s, A=%s, nla_environment=%s, N_content=%s', R, A, nla_environment, N_content)
-    value = A * nla_environment / 100 * 2 * N_content / 1000
+    nla_environment, P_content = list_of_contents_for_value
+    logger.debug('R=%s, A=%s, nla_environment=%s, P_content=%s', R, A, nla_environment, P_content)
+    value = A * nla_environment / 100 * 2 * P_content
     return [_emission(value)]
 
 
 def _should_run(cycle: dict):
     end_date = cycle.get('endDate')
     site = cycle.get('site', {})
     measurements = site.get('measurements', [])
 
     def _get_measurement_content(term_id: str):
         return most_relevant_measurement_value(measurements, term_id, end_date)
 
     nla_environment = list_sum(_get_measurement_content('nutrientLossToAquaticEnvironment'))
-    soil_nitrogen_content = list_sum(_get_measurement_content('soilTotalNitrogenContent'))
+    soil_phosphorus_content = list_sum(_get_measurement_content('phosphorusPerKgSoil'))
     erodability = list_sum(_get_measurement_content('erodibility'))
     slope = list_sum(_get_measurement_content('slope'))
     slope_length = list_sum(_get_measurement_content('slopeLength'))
     heavy_winter_precipitation = list_sum(_get_measurement_content('heavyWinterPrecipitation'))
 
     precipitation = list_sum(_get_measurement_content('rainfallAnnual'))
     water = get_water(cycle, precipitation)
@@ -56,15 +56,15 @@
     p_ef_c1 = get_p_ef_c1(cycle)
     ef_p_c2 = get_ef_p_c2(cycle)
 
     list_of_contents_for_A = [
         practise_factor, erodability, slope_length,
         pcorr, p_ef_c1, ef_p_c2]
     list_of_contents_for_R = [heavy_winter_precipitation, water]
-    list_of_contents_for_value = [nla_environment, soil_nitrogen_content]
+    list_of_contents_for_value = [nla_environment, soil_phosphorus_content]
 
     should_run = valid_site_type(cycle, True) \
         and all(list_of_contents_for_A) \
         and all(list_of_contents_for_R) \
         and all(list_of_contents_for_value)
     logger.info('model=%s, term=%s, should_run=%s', MODEL, TERM_ID, should_run)
     return should_run, list_of_contents_for_A, list_of_contents_for_R, list_of_contents_for_value
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pErosionAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/nErosionAllOrigins.py`

 * *Files 4% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from hestia_earth.models.log import logger
 from hestia_earth.models.utils.emission import _new_emission
 from hestia_earth.models.utils.measurement import most_relevant_measurement_value
 from hestia_earth.models.utils.cycle import valid_site_type
 from .utils import get_pcorr, get_p_ef_c1, get_ef_p_c2, get_practice_factor, get_water, calculate_R, calculate_A
 from . import MODEL
 
-TERM_ID = 'pErosionAllOrigins'
+TERM_ID = 'nErosionAllOrigins'
 
 
 def _emission(value: float):
     logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
     emission = _new_emission(TERM_ID, MODEL)
     emission['value'] = [value]
     emission['methodTier'] = EmissionMethodTier.TIER_1.value
@@ -23,30 +23,30 @@
 def _run(list_of_contents_for_A: list, list_of_contents_for_R: list, list_of_contents_for_value: list):
     heavy_winter_precipitation, water = list_of_contents_for_R
     R = calculate_R(heavy_winter_precipitation, water)
 
     practise_factor, erodability, slope_length, pcorr, p_ef_c1, ef_p_c2 = list_of_contents_for_A
     A = calculate_A(R, practise_factor, erodability, slope_length, pcorr, p_ef_c1, ef_p_c2)
 
-    nla_environment, P_content = list_of_contents_for_value
-    logger.debug('R=%s, A=%s, nla_environment=%s, P_content=%s', R, A, nla_environment, P_content)
-    value = A * nla_environment / 100 * 2 * P_content / 1000
+    nla_environment, N_content = list_of_contents_for_value
+    logger.debug('R=%s, A=%s, nla_environment=%s, N_content=%s', R, A, nla_environment, N_content)
+    value = A * nla_environment / 100 * 2 * N_content
     return [_emission(value)]
 
 
 def _should_run(cycle: dict):
     end_date = cycle.get('endDate')
     site = cycle.get('site', {})
     measurements = site.get('measurements', [])
 
     def _get_measurement_content(term_id: str):
         return most_relevant_measurement_value(measurements, term_id, end_date)
 
     nla_environment = list_sum(_get_measurement_content('nutrientLossToAquaticEnvironment'))
-    soil_phosphorus_content = list_sum(_get_measurement_content('soilPhosphorusContent'))
+    soil_nitrogen_content = list_sum(_get_measurement_content('totalNitrogenPerKgSoil'))
     erodability = list_sum(_get_measurement_content('erodibility'))
     slope = list_sum(_get_measurement_content('slope'))
     slope_length = list_sum(_get_measurement_content('slopeLength'))
     heavy_winter_precipitation = list_sum(_get_measurement_content('heavyWinterPrecipitation'))
 
     precipitation = list_sum(_get_measurement_content('rainfallAnnual'))
     water = get_water(cycle, precipitation)
@@ -56,15 +56,15 @@
     p_ef_c1 = get_p_ef_c1(cycle)
     ef_p_c2 = get_ef_p_c2(cycle)
 
     list_of_contents_for_A = [
         practise_factor, erodability, slope_length,
         pcorr, p_ef_c1, ef_p_c2]
     list_of_contents_for_R = [heavy_winter_precipitation, water]
-    list_of_contents_for_value = [nla_environment, soil_phosphorus_content]
+    list_of_contents_for_value = [nla_environment, soil_nitrogen_content]
 
     should_run = valid_site_type(cycle, True) \
         and all(list_of_contents_for_A) \
         and all(list_of_contents_for_R) \
         and all(list_of_contents_for_value)
     logger.info('model=%s, term=%s, should_run=%s', MODEL, TERM_ID, should_run)
     return should_run, list_of_contents_for_A, list_of_contents_for_R, list_of_contents_for_value
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pToDrainageWaterAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pToDrainageWaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pToGroundwaterAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pToGroundwaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/pToSurfacewaterAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/pToSurfacewaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/schererPfister2015/utils.py` & `hestia-earth-models-0.9.1/hestia_earth/models/schererPfister2015/utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/site/measurement/value.py` & `hestia-earth-models-0.9.1/hestia_earth/models/site/measurement/value.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/aware.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/aware.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/clayContent.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/clayContent.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/croppingIntensity.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/croppingIntensity.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/drainageClass.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/drainageClass.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/ecoClimateZone.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/ecoClimateZone.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/ecoregion.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/ecoregion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/erodibility.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/erodibility.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/fallowCorrection.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/fallowCorrection.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/heavyWinterPrecipitation.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/heavyWinterPrecipitation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/histosol.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/histosol.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/nutrientLossToAquaticEnvironment.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/nutrientLossToAquaticEnvironment.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/rainfallAnnual.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/rainfallAnnual.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/region.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/region.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/slope.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/slope.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/slopeLength.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/slopeLength.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilOrganicCarbonContent.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/totalNitrogenPerKgSoil.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,37 +1,39 @@
 from hestia_earth.schema import MeasurementStatsDefinition
 
 from hestia_earth.models.log import logger
 from hestia_earth.models.utils.measurement import _new_measurement
 from .utils import download, has_geospatial_data, _site_gadm_id
 from . import MODEL
 
-TERM_ID = 'soilOrganicCarbonContent'
-BIBLIO_TITLE = 'The harmonized world soil database. verson 1.0'
+TERM_ID = 'totalNitrogenPerKgSoil'
+BIBLIO_TITLE = 'Harmonized soil property values for broad-scale modelling (WISE30sec) '
+'with estimates of global soil carbon stocks'
 
 
 def _measurement(value: float):
     logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
     measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
     measurement['value'] = [value]
     measurement['depthUpper'] = 0
-    measurement['depthLower'] = 30
+    measurement['depthLower'] = 50
     measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
     return measurement
 
 
 def _run(site: dict):
     field = 'first'
-    value = download(collection='users/hestiaplatform/T_OC',
+    value = download(collection='users/hestiaplatform/T_N',
                      ee_type='raster',
                      latitude=site.get('latitude'),
                      longitude=site.get('longitude'),
                      gadm_id=_site_gadm_id(site),
                      boundary=site.get('boundary'),
-                     fields=field
+                     fields=field,
+                     scale=2
                      ).get(field, None)
 
     return [] if value is None else [_measurement(value)]
 
 
 def _should_run(site: dict):
     should_run = has_geospatial_data(site)
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilPh.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/soilPh.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilPhosphorusContent.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/phosphorusPerKgSoil.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from hestia_earth.schema import MeasurementStatsDefinition
 
 from hestia_earth.models.log import logger
 from hestia_earth.models.utils.measurement import _new_measurement
 from .utils import download, has_geospatial_data, _site_gadm_id
 from . import MODEL
 
-TERM_ID = 'soilPhosphorusContent'
+TERM_ID = 'phosphorusPerKgSoil'
 BIBLIO_TITLE = 'Modelling spatially explicit impacts from phosphorus emissions in agriculture'
 
 
 def _measurement(value: float):
     logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
     measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
     measurement['value'] = [value]
@@ -26,15 +26,15 @@
                      latitude=site.get('latitude'),
                      longitude=site.get('longitude'),
                      gadm_id=_site_gadm_id(site),
                      boundary=site.get('boundary'),
                      fields=field
                      ).get(field, None)
 
-    return [] if value is None else [_measurement(value * 1000)]
+    return [] if value is None else [_measurement(value)]
 
 
 def _should_run(site: dict):
     should_run = has_geospatial_data(site)
     logger.info('model=%s, term=%s, should_run=%s', MODEL, TERM_ID, should_run)
     return should_run
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/soilTotalNitrogenContent.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/organicCarbonPerKgSoil.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,42 +1,40 @@
 from hestia_earth.schema import MeasurementStatsDefinition
 
 from hestia_earth.models.log import logger
 from hestia_earth.models.utils.measurement import _new_measurement
 from .utils import download, has_geospatial_data, _site_gadm_id
 from . import MODEL
 
-TERM_ID = 'soilTotalNitrogenContent'
-BIBLIO_TITLE = 'Harmonized soil property values for broad-scale modelling (WISE30sec) '
-'with estimates of global soil carbon stocks'
+TERM_ID = 'organicCarbonPerKgSoil'
+BIBLIO_TITLE = 'The harmonized world soil database. verson 1.0'
 
 
 def _measurement(value: float):
     logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
     measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
     measurement['value'] = [value]
     measurement['depthUpper'] = 0
-    measurement['depthLower'] = 50
+    measurement['depthLower'] = 30
     measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
     return measurement
 
 
 def _run(site: dict):
     field = 'first'
-    value = download(collection='users/hestiaplatform/T_N',
+    value = download(collection='users/hestiaplatform/T_OC',
                      ee_type='raster',
                      latitude=site.get('latitude'),
                      longitude=site.get('longitude'),
                      gadm_id=_site_gadm_id(site),
                      boundary=site.get('boundary'),
-                     fields=field,
-                     scale=2
+                     fields=field
                      ).get(field, None)
 
-    return [] if value is None else [_measurement(value * 1000)]
+    return [] if value is None else [_measurement(value / 100000)]
 
 
 def _should_run(site: dict):
     should_run = has_geospatial_data(site)
     logger.info('model=%s, term=%s, should_run=%s', MODEL, TERM_ID, should_run)
     return should_run
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/temperatureAnnual.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/temperatureAnnual.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/spatial/utils.py` & `hestia-earth-models-0.9.1/hestia_earth/models/spatial/utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirAllOrigins.py`

 * *Files 1% similar despite different names*

```diff
@@ -32,15 +32,15 @@
 
 def _should_run(cycle: dict):
     end_date = cycle.get('endDate')
     site = cycle.get('site', {})
     measurements = site.get('measurements', [])
     clay = most_relevant_measurement_value(measurements, 'clayContent', end_date)
     sand = most_relevant_measurement_value(measurements, 'sandContent', end_date)
-    organicCarbonContent = most_relevant_measurement_value(measurements, 'soilOrganicCarbonContent', end_date)
+    organicCarbonContent = most_relevant_measurement_value(measurements, 'organicCarbonPerKgSoil', end_date)
     soilPh = most_relevant_measurement_value(measurements, 'soilPh', end_date)
     ecoClimateZone = most_relevant_measurement_value(measurements, 'ecoClimateZone', end_date)
     ecoClimateZone = str(ecoClimateZone[0]) if len(ecoClimateZone) > 0 else None
     product = find_primary_product(cycle)
     crop_grouping = _get_crop_crouping(product) if product else None
     N_total = list_sum(get_total_nitrogen(cycle.get('inputs', [])))
     content_list_of_items = [clay, sand, organicCarbonContent, soilPh, ecoClimateZone, crop_grouping]
@@ -57,15 +57,15 @@
         and all(content_list_of_items) \
         and N_total > 0 \
         and crop_grouping in N2O_FACTORS_BY_CROP
     return should_run, N_total, content_list_of_items
 
 
 def _organic_carbon_factor(organicCarbonContent: float):
-    return 0 if organicCarbonContent/100 < 0.01 else (0.0526 if organicCarbonContent/100 <= 0.03 else 0.6334)
+    return 0 if organicCarbonContent * 1000 < 0.01 else (0.0526 if organicCarbonContent * 1000 <= 0.03 else 0.6334)
 
 
 def _soilph_factor(soilPh: float):
     return 0 if soilPh < 5.5 else (-0.4836 if soilPh > 7.3 else -0.0693)
 
 
 def _sand_factor(sand: float, clay: float):
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirCropResidueDecompositionDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirCropResidueDecompositionDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirExcretaDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirExcretaDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirInorganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirInorganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/n2OToAirOrganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/n2OToAirOrganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirAllOrigins.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 
 def _should_run(cycle: dict):
     end_date = cycle.get('endDate')
     site = cycle.get('site', {})
     measurements = site.get('measurements', [])
     ecoClimateZone = most_relevant_measurement_value(measurements, 'ecoClimateZone', end_date)
     ecoClimateZone = str(ecoClimateZone[0]) if len(ecoClimateZone) > 0 else None
-    nitrogenContent = list_average(most_relevant_measurement_value(measurements, 'soilTotalNitrogenContent', end_date))
+    nitrogenContent = list_average(most_relevant_measurement_value(measurements, 'totalNitrogenPerKgSoil', end_date))
     residue = residue_nitrogen(cycle.get('products', []))
     N_total = list_sum(get_total_nitrogen(cycle.get('inputs', [])) + [residue])
 
     debugRequirements(model=MODEL, term=TERM_ID,
                       nitrogenContent=nitrogenContent,
                       residue=residue,
                       ecoClimateZone=ecoClimateZone,
@@ -36,15 +36,15 @@
         and nitrogenContent is not None \
         and N_total > 0
     return should_run, ecoClimateZone, nitrogenContent, N_total, residue
 
 
 def _get_value(ecoClimateZone: str, nitrogenContent: float, N_total: float):
     eco_factor = get_ecoClimateZone_lookup_value(ecoClimateZone, 'STEHFEST_BOUWMAN_2006_NOX-N_FACTOR')
-    n_factor = 0 if nitrogenContent / 1000000 < 0.0005 else -1.0211 if nitrogenContent / 1000000 <= 0.002 else 0.7892
+    n_factor = 0 if nitrogenContent / 1000 < 0.0005 else -1.0211 if nitrogenContent / 1000 <= 0.002 else 0.7892
     value = min(
         0.025 * N_total,
         np.exp(-0.451 + 0.0061 * N_total + n_factor + eco_factor) -
         np.exp(-0.451 + n_factor + eco_factor)
     ) * get_atomic_conversion(Units.KG_NOX, Units.TO_N)
     logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
     return value
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirExcreta.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirExcreta.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirInorganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006/noxToAirOrganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006/noxToAirOrganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirAllOrigins.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirExcreta.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirExcreta.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirInorganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirOrganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/stehfestBouwman2006GisImplementation/noxToAirOrganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/transformation/post_checks/product.py` & `hestia-earth-models-0.9.1/hestia_earth/models/transformation/post_checks/product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/__init__.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/blank_node.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/blank_node.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/constant.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/constant.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/crop.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/crop.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/cycle.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/cycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/ecoClimateZone.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/ecoClimateZone.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/impact_assessment.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/impact_assessment.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/inorganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/inorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/input.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/input.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/measurement.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/measurement.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/practice.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/practice.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/product.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/property.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/property.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/site.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/utils/term.py` & `hestia-earth-models-0.9.1/hestia_earth/models/utils/term.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/nh3ToAirOrganicFertilizer.py` & `hestia-earth-models-0.9.1/hestia_earth/models/webbEtAl2012AndSintermannEtAl2012/nh3ToAirOrganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/hestia_earth_models.egg-info/PKG-INFO` & `hestia-earth-models-0.9.1/hestia_earth_models.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hestia-earth-models
-Version: 0.9.0
+Version: 0.9.1
 Summary: Hestia's set of modules for filling gaps in the activity data using external datasets (e.g. populating soil properties with a geospatial dataset using provided coordinates) and internal lookups (e.g. populating machinery use from fuel use). Includes rules for when gaps should be filled versus not (e.g. never gap fill yield, gap fill crop residue if yield provided etc.).
 Home-page: https://gitlab.com/hestia-earth/hestia-engine-models
 Author: Hestia Team
 Author-email: guillaumeroyer.mail@gmail.com
 License: GPL
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `hestia-earth-models-0.9.0/hestia_earth_models.egg-info/SOURCES.txt` & `hestia-earth-models-0.9.1/hestia_earth_models.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -131,15 +131,15 @@
 hestia_earth/models/pooreNemecek2018/no3ToGroundwaterOrganicFertilizer.py
 hestia_earth/models/pooreNemecek2018/noxToAirAquaculturePonds.py
 hestia_earth/models/pooreNemecek2018/nurseryDuration.py
 hestia_earth/models/pooreNemecek2018/orchardDensity.py
 hestia_earth/models/pooreNemecek2018/orchardDuration.py
 hestia_earth/models/pooreNemecek2018/organicFertilizerToKgOrMass.py
 hestia_earth/models/pooreNemecek2018/saplings.py
-hestia_earth/models/pooreNemecek2018/soilTotalNitrogenContent.py
+hestia_earth/models/pooreNemecek2018/totalNitrogenPerKgSoil.py
 hestia_earth/models/schererPfister2015/__init__.py
 hestia_earth/models/schererPfister2015/nErosionAllOrigins.py
 hestia_earth/models/schererPfister2015/pErosionAllOrigins.py
 hestia_earth/models/schererPfister2015/pToDrainageWaterAllOrigins.py
 hestia_earth/models/schererPfister2015/pToGroundwaterAllOrigins.py
 hestia_earth/models/schererPfister2015/pToSurfacewaterAllOrigins.py
 hestia_earth/models/schererPfister2015/utils.py
@@ -156,23 +156,23 @@
 hestia_earth/models/spatial/ecoClimateZone.py
 hestia_earth/models/spatial/ecoregion.py
 hestia_earth/models/spatial/erodibility.py
 hestia_earth/models/spatial/fallowCorrection.py
 hestia_earth/models/spatial/heavyWinterPrecipitation.py
 hestia_earth/models/spatial/histosol.py
 hestia_earth/models/spatial/nutrientLossToAquaticEnvironment.py
+hestia_earth/models/spatial/organicCarbonPerKgSoil.py
+hestia_earth/models/spatial/phosphorusPerKgSoil.py
 hestia_earth/models/spatial/rainfallAnnual.py
 hestia_earth/models/spatial/region.py
 hestia_earth/models/spatial/slope.py
 hestia_earth/models/spatial/slopeLength.py
-hestia_earth/models/spatial/soilOrganicCarbonContent.py
 hestia_earth/models/spatial/soilPh.py
-hestia_earth/models/spatial/soilPhosphorusContent.py
-hestia_earth/models/spatial/soilTotalNitrogenContent.py
 hestia_earth/models/spatial/temperatureAnnual.py
+hestia_earth/models/spatial/totalNitrogenPerKgSoil.py
 hestia_earth/models/spatial/utils.py
 hestia_earth/models/stehfestBouwman2006/__init__.py
 hestia_earth/models/stehfestBouwman2006/n2OToAirAllOrigins.py
 hestia_earth/models/stehfestBouwman2006/n2OToAirCropResidueDecompositionDirect.py
 hestia_earth/models/stehfestBouwman2006/n2OToAirExcretaDirect.py
 hestia_earth/models/stehfestBouwman2006/n2OToAirInorganicFertilizerDirect.py
 hestia_earth/models/stehfestBouwman2006/n2OToAirOrganicFertilizerDirect.py
@@ -336,15 +336,15 @@
 tests/models/pooreNemecek2018/test_no3ToGroundwaterOrganicFertilizer.py
 tests/models/pooreNemecek2018/test_noxToAirAquaculturePonds.py
 tests/models/pooreNemecek2018/test_nurseryDuration.py
 tests/models/pooreNemecek2018/test_orchardDensity.py
 tests/models/pooreNemecek2018/test_orchardDuration.py
 tests/models/pooreNemecek2018/test_organicFertilizerToKgOrMass.py
 tests/models/pooreNemecek2018/test_saplings.py
-tests/models/pooreNemecek2018/test_soilTotalNitrogenContent.py
+tests/models/pooreNemecek2018/test_totalNitrogenPerKgSoil.py
 tests/models/schererPfister2015/__init__.py
 tests/models/schererPfister2015/test_nErosionAllOrigins.py
 tests/models/schererPfister2015/test_pErosionAllOrigins.py
 tests/models/schererPfister2015/test_pToDrainageWaterAllOrigins.py
 tests/models/schererPfister2015/test_pToGroundwaterAllOrigins.py
 tests/models/schererPfister2015/test_pToSurfacewaterAllOrigins.py
 tests/models/site/__init__.py
@@ -360,23 +360,23 @@
 tests/models/spatial/test_ecoClimateZone.py
 tests/models/spatial/test_ecoregion.py
 tests/models/spatial/test_erodibility.py
 tests/models/spatial/test_fallowCorrection.py
 tests/models/spatial/test_heavyWinterPrecipitation.py
 tests/models/spatial/test_histosol.py
 tests/models/spatial/test_nutrientLossToAquaticEnvironment.py
+tests/models/spatial/test_organicCarbonPerKgSoil.py
+tests/models/spatial/test_phosphorusPerKgSoil.py
 tests/models/spatial/test_rainfallAnnual.py
 tests/models/spatial/test_region.py
 tests/models/spatial/test_slope.py
 tests/models/spatial/test_slopeLength.py
-tests/models/spatial/test_soilOrganicCarbonContent.py
 tests/models/spatial/test_soilPh.py
-tests/models/spatial/test_soilPhosphorusContent.py
-tests/models/spatial/test_soilTotalNitrogenContent.py
 tests/models/spatial/test_temperatureAnnual.py
+tests/models/spatial/test_totalNitrogenPerKgSoil.py
 tests/models/stehfestBouwman2006/__init__.py
 tests/models/stehfestBouwman2006/test_n2OToAirAllOrigins.py
 tests/models/stehfestBouwman2006/test_n2OToAirCropResidueDecompositionDirect.py
 tests/models/stehfestBouwman2006/test_n2OToAirExcretaDirect.py
 tests/models/stehfestBouwman2006/test_n2OToAirInorganicFertilizerDirect.py
 tests/models/stehfestBouwman2006/test_n2OToAirOrganicFertilizerDirect.py
 tests/models/stehfestBouwman2006/test_noxToAirAllOrigins.py
```

### Comparing `hestia-earth-models-0.9.0/setup.py` & `hestia-earth-models-0.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/agribalyse2016/test_machineryInfrastructureDepreciatedAmountPerCycle.py` & `hestia-earth-models-0.9.1/tests/models/agribalyse2016/test_machineryInfrastructureDepreciatedAmountPerCycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_ch4ToAirCropResidueBurning.py` & `hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_ch4ToAirCropResidueBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_n2OToAirCropResidueBurningDirect.py` & `hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_n2OToAirCropResidueBurningDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_nh3ToAirCropResidueBurning.py` & `hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_nh3ToAirCropResidueBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_noxToAirCropResidueBurning.py` & `hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_noxToAirCropResidueBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/akagiEtAl2011AndIpcc2006/test_utils.py` & `hestia-earth-models-0.9.1/tests/models/akagiEtAl2011AndIpcc2006/test_utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/aware/test_freshwaterWithdrawals.py` & `hestia-earth-models-0.9.1/tests/models/aware/test_freshwaterWithdrawals.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/aware/test_scarcityWeightedWaterUse.py` & `hestia-earth-models-0.9.1/tests/models/aware/test_scarcityWeightedWaterUse.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/test_ch4ToAirNaturalVegetationBurning.py` & `hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/test_ch4ToAirNaturalVegetationBurning.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/test_co2ToAirBiomassAndSoilCarbonStockChange.py` & `hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/test_co2ToAirBiomassAndSoilCarbonStockChange.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/blonkConsultants2016/test_n2OToAirNaturalVegetationBurningDirect.py` & `hestia-earth-models-0.9.1/tests/models/blonkConsultants2016/test_n2OToAirNaturalVegetationBurningDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/test_biodiversityLossLandOccupation.py` & `hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/test_biodiversityLossLandOccupation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/test_biodiversityLossLandTransformation.py` & `hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/test_biodiversityLossLandTransformation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/chaudharyEtAl2015/test_biodiversityLossTotalLandUseEffects.py` & `hestia-earth-models-0.9.1/tests/models/chaudharyEtAl2015/test_biodiversityLossTotalLandUseEffects.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_eutrophicationPotentialExcludingFate.py` & `hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_eutrophicationPotentialExcludingFate.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_eutrophicationPotentialIncludingFateAverageEurope.py` & `hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_eutrophicationPotentialIncludingFateAverageEurope.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialExcludingFate.py` & `hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialExcludingFate.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialIncludingFateAverageEurope.py` & `hestia-earth-models-0.9.1/tests/models/cml2001NonBaseline/test_terrestrialAcidificationPotentialIncludingFateAverageEurope.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/dataCompleteness/test_cropResidue.py` & `hestia-earth-models-0.9.1/tests/models/cycle/dataCompleteness/test_cropResidue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/dataCompleteness/test_soilAmendments.py` & `hestia-earth-models-0.9.1/tests/models/cycle/dataCompleteness/test_soilAmendments.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/input/test_aggregated.py` & `hestia-earth-models-0.9.1/tests/models/cycle/input/test_aggregated.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/input/test_ecoinventV3.py` & `hestia-earth-models-0.9.1/tests/models/cycle/input/test_ecoinventV3.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/input/test_value.py` & `hestia-earth-models-0.9.1/tests/models/cycle/input/test_value.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/post_checks/test_site.py` & `hestia-earth-models-0.9.1/tests/models/cycle/post_checks/test_site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/pre_checks/test_site.py` & `hestia-earth-models-0.9.1/tests/models/cycle/pre_checks/test_site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/pre_checks/test_startDate.py` & `hestia-earth-models-0.9.1/tests/models/cycle/pre_checks/test_startDate.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/product/test_economicValueShare.py` & `hestia-earth-models-0.9.1/tests/models/cycle/product/test_economicValueShare.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/product/test_price.py` & `hestia-earth-models-0.9.1/tests/models/cycle/product/test_price.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/product/test_primary.py` & `hestia-earth-models-0.9.1/tests/models/cycle/product/test_primary.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/product/test_revenue.py` & `hestia-earth-models-0.9.1/tests/models/cycle/product/test_revenue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/product/test_value.py` & `hestia-earth-models-0.9.1/tests/models/cycle/product/test_value.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/test_dataCompleteness.py` & `hestia-earth-models-0.9.1/tests/models/cycle/test_dataCompleteness.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/test_feedConversionRatio.py` & `hestia-earth-models-0.9.1/tests/models/cycle/test_feedConversionRatio.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/test_irrigated.py` & `hestia-earth-models-0.9.1/tests/models/cycle/test_irrigated.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/cycle/test_siteDuration.py` & `hestia-earth-models-0.9.1/tests/models/cycle/test_siteDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/deRuijterEtAl2010/test_nh3ToAirCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/tests/models/deRuijterEtAl2010/test_nh3ToAirCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_co2ToAirFuelCombustion.py` & `hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_co2ToAirFuelCombustion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_n2OToAirFuelCombustionDirect.py` & `hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_n2OToAirFuelCombustionDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_nh3ToAirInorganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_nh3ToAirInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_noxToAirFuelCombustion.py` & `hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_noxToAirFuelCombustion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_so2ToAirFuelCombustion.py` & `hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_so2ToAirFuelCombustion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/emeaEea2019/test_utils.py` & `hestia-earth-models-0.9.1/tests/models/emeaEea2019/test_utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/faostat2018/test_seed.py` & `hestia-earth-models-0.9.1/tests/models/faostat2018/test_seed.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/globalCropWaterModel2008/test_rootingDepth.py` & `hestia-earth-models-0.9.1/tests/models/globalCropWaterModel2008/test_rootingDepth.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/impact_assessment/post_checks/test_cycle.py` & `hestia-earth-models-0.9.1/tests/models/impact_assessment/post_checks/test_cycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/impact_assessment/post_checks/test_site.py` & `hestia-earth-models-0.9.1/tests/models/impact_assessment/post_checks/test_site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/impact_assessment/pre_checks/test_cycle.py` & `hestia-earth-models-0.9.1/tests/models/impact_assessment/pre_checks/test_cycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/impact_assessment/pre_checks/test_site.py` & `hestia-earth-models-0.9.1/tests/models/impact_assessment/pre_checks/test_site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/impact_assessment/test_emissions.py` & `hestia-earth-models-0.9.1/tests/models/impact_assessment/test_emissions.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/impact_assessment/test_product.py` & `hestia-earth-models-0.9.1/tests/models/impact_assessment/test_product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_aboveGroundCropResidue.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_aboveGroundCropResidue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_aboveGroundCropResidueRemoved.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_aboveGroundCropResidueRemoved.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_aboveGroundCropResidueTotal.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_aboveGroundCropResidueTotal.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_belowGroundCropResidue.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_belowGroundCropResidue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_co2ToAirOrganicSoilCultivation.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_co2ToAirOrganicSoilCultivation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirCropResidueDecompositionIndirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirCropResidueDecompositionIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirExcretaDirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirExcretaDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirExcretaIndirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirExcretaIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerIndirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirInorganicFertilizerIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerIndirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirOrganicFertilizerIndirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_n2OToAirOrganicSoilCultivationDirect.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_n2OToAirOrganicSoilCultivationDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2006/test_residue.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2006/test_residue.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2013ExcludingFeedbacks/test_gwp100.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2013ExcludingFeedbacks/test_gwp100.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2013IncludingFeedbacks/test_gwp100.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2013IncludingFeedbacks/test_gwp100.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2019/test_ch4ToAirEntericFermentation.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2019/test_ch4ToAirEntericFermentation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2019/test_ch4ToAirFloodedRice.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2019/test_ch4ToAirFloodedRice.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2019/test_co2ToAirLimeHydrolysis.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2019/test_co2ToAirLimeHydrolysis.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2019/test_co2ToAirUreaHydrolysis.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2019/test_co2ToAirUreaHydrolysis.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2019/test_croppingDuration.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2019/test_croppingDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/ipcc2019/test_nitrogenContent.py` & `hestia-earth-models-0.9.1/tests/models/ipcc2019/test_nitrogenContent.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_landOccupation.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_landOccupation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_n2OToAirAquaculturePondsDirect.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_n2OToAirAquaculturePondsDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_n2ToAirAquaculturePonds.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_n2ToAirAquaculturePonds.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_netPrimaryProduction.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_netPrimaryProduction.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_nh3ToAirAquaculturePonds.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_nh3ToAirAquaculturePonds.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterExcreta.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterExcreta.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterInorganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_no3ToGroundwaterOrganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_no3ToGroundwaterOrganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_noxToAirAquaculturePonds.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_noxToAirAquaculturePonds.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_nurseryDuration.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_nurseryDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_orchardDensity.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_orchardDensity.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_orchardDuration.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_orchardDuration.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_organicFertilizerToKgOrMass.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_organicFertilizerToKgOrMass.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_saplings.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_saplings.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/pooreNemecek2018/test_soilTotalNitrogenContent.py` & `hestia-earth-models-0.9.1/tests/models/pooreNemecek2018/test_totalNitrogenPerKgSoil.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from unittest.mock import patch
 import json
 from tests.utils import fixtures_path, fake_new_measurement
 
-from hestia_earth.models.pooreNemecek2018.soilTotalNitrogenContent import TERM_ID, run, _should_run
+from hestia_earth.models.pooreNemecek2018.totalNitrogenPerKgSoil import TERM_ID, run, _should_run
 
 class_path = f"hestia_earth.models.pooreNemecek2018.{TERM_ID}"
 fixtures_folder = f"{fixtures_path}/pooreNemecek2018/{TERM_ID}"
 
 
 @patch(f"{class_path}.find_term_match")
 def test_should_run(mock_measurement):
@@ -14,15 +14,14 @@
     should_run, *args = _should_run({})
     assert not should_run
 
     mock_measurement.return_value = {'value': [10]}
     should_run, *args = _should_run({})
     assert should_run is True
 
-    # soilOrganicCarbonContent was "gap-filled" => no run
     mock_measurement.return_value = {'added': ['value']}
     should_run, *args = _should_run({})
     assert not should_run
 
 
 @patch(f"{class_path}._new_measurement", side_effect=fake_new_measurement)
 def test_run(*args):
```

### Comparing `hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_nErosionAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_nErosionAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pErosionAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pErosionAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pToDrainageWaterAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pToDrainageWaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pToGroundwaterAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pToGroundwaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/schererPfister2015/test_pToSurfacewaterAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/schererPfister2015/test_pToSurfacewaterAllOrigins.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/site/measurement/test_value.py` & `hestia-earth-models-0.9.1/tests/models/site/measurement/test_value.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_aware.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_aware.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_clayContent.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_clayContent.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_croppingIntensity.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_croppingIntensity.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_drainageClass.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_drainageClass.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_ecoClimateZone.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_ecoClimateZone.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_ecoregion.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_ecoregion.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_erodibility.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_erodibility.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_fallowCorrection.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_fallowCorrection.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_heavyWinterPrecipitation.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_heavyWinterPrecipitation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_histosol.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_histosol.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_nutrientLossToAquaticEnvironment.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_nutrientLossToAquaticEnvironment.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_rainfallAnnual.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_rainfallAnnual.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_region.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_region.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_slope.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_slope.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_slopeLength.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_slopeLength.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_soilOrganicCarbonContent.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_soilPh.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from unittest.mock import patch
 import json
 from tests.utils import fixtures_path, fake_new_measurement
 
-from hestia_earth.models.spatial.soilOrganicCarbonContent import _should_run, TERM_ID, run
+from hestia_earth.models.spatial.soilPh import _should_run, TERM_ID, run
 
 class_path = f"hestia_earth.models.spatial.{TERM_ID}"
 fixtures_folder = f"{fixtures_path}/spatial/{TERM_ID}"
 
 
 @patch(f"{class_path}.has_geospatial_data")
 def test_should_run(mock_has_geospatial_data):
```

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_soilPh.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_totalNitrogenPerKgSoil.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from unittest.mock import patch
 import json
 from tests.utils import fixtures_path, fake_new_measurement
 
-from hestia_earth.models.spatial.soilPh import _should_run, TERM_ID, run
+from hestia_earth.models.spatial.totalNitrogenPerKgSoil import _should_run, TERM_ID, run
 
 class_path = f"hestia_earth.models.spatial.{TERM_ID}"
 fixtures_folder = f"{fixtures_path}/spatial/{TERM_ID}"
 
 
 @patch(f"{class_path}.has_geospatial_data")
 def test_should_run(mock_has_geospatial_data):
```

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_soilPhosphorusContent.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_phosphorusPerKgSoil.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from unittest.mock import patch
 import json
 from tests.utils import fixtures_path, fake_new_measurement
 
-from hestia_earth.models.spatial.soilPhosphorusContent import _should_run, TERM_ID, run
+from hestia_earth.models.spatial.phosphorusPerKgSoil import _should_run, TERM_ID, run
 
 class_path = f"hestia_earth.models.spatial.{TERM_ID}"
 fixtures_folder = f"{fixtures_path}/spatial/{TERM_ID}"
 
 
 @patch(f"{class_path}.has_geospatial_data")
 def test_should_run(mock_has_geospatial_data):
```

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_soilTotalNitrogenContent.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_organicCarbonPerKgSoil.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from unittest.mock import patch
 import json
 from tests.utils import fixtures_path, fake_new_measurement
 
-from hestia_earth.models.spatial.soilTotalNitrogenContent import _should_run, TERM_ID, run
+from hestia_earth.models.spatial.organicCarbonPerKgSoil import _should_run, TERM_ID, run
 
 class_path = f"hestia_earth.models.spatial.{TERM_ID}"
 fixtures_folder = f"{fixtures_path}/spatial/{TERM_ID}"
 
 
 @patch(f"{class_path}.has_geospatial_data")
 def test_should_run(mock_has_geospatial_data):
```

### Comparing `hestia-earth-models-0.9.0/tests/models/spatial/test_temperatureAnnual.py` & `hestia-earth-models-0.9.1/tests/models/spatial/test_temperatureAnnual.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirAllOrigins.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,57 +1,43 @@
 from unittest.mock import patch
 import json
 from tests.utils import fixtures_path, fake_new_emission
 
-from hestia_earth.models.stehfestBouwman2006.n2OToAirAllOrigins import TERM_ID, run, _get_value, _should_run
+from hestia_earth.models.stehfestBouwman2006.noxToAirAllOrigins import TERM_ID, run, _should_run
 
 class_path = f"hestia_earth.models.stehfestBouwman2006.{TERM_ID}"
 fixtures_folder = f"{fixtures_path}/stehfestBouwman2006/{TERM_ID}"
 
 
 @patch(f"{class_path}.valid_site_type", return_value=True)
+@patch(f"{class_path}.residue_nitrogen", return_value=0)
 @patch(f"{class_path}.most_relevant_measurement_value", return_value=[])
-def test_should_run(mock_most_relevant_measurement_value, _m):
+def test_should_run(mock_most_relevant_measurement_value, *args):
     # no measurements => no run
-    cycle = {}
+    cycle = {'inputs': [], 'measurements': []}
     should_run, *args = _should_run(cycle)
     assert not should_run
 
     # with measurements => no run
     mock_most_relevant_measurement_value.return_value = [10]
+    cycle['measurements'] = [{}]
     should_run, *args = _should_run(cycle)
     assert not should_run
 
-    # with kg N inputs => no run
+    # with kg N inputs => run
     cycle['inputs'] = [{
         'term': {
             'units': 'kg N'
         },
         'value': [100]
     }]
     should_run, *args = _should_run(cycle)
-    assert not should_run
-
-    # with primary product => run
-    cycle['products'] = [{
-        'term': {
-            '@id': 'cerealsGrain'
-        },
-        'primary': True
-    }]
-    should_run, *args = _should_run(cycle)
     assert should_run is True
 
 
-def test_get_value():
-    content_list_of_items = [[8], [81], [0.58], [5.7], '2', 'None']
-    N_total = 100
-    assert _get_value(content_list_of_items, N_total) == 3.6132443350109704
-
-
 @patch(f"{class_path}._new_emission", side_effect=fake_new_emission)
 def test_run(*args):
     with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
         cycle = json.load(f)
 
     with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
         expected = json.load(f)
```

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirCropResidueDecompositionDirect.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirCropResidueDecompositionDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirExcretaDirect.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirExcretaDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirInorganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirInorganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_n2OToAirOrganicFertilizerDirect.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirOrganicFertilizerDirect.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirAllOrigins.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_n2OToAirAllOrigins.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,48 +1,49 @@
 from unittest.mock import patch
 import json
 from tests.utils import fixtures_path, fake_new_emission
 
-from hestia_earth.models.stehfestBouwman2006.noxToAirAllOrigins import TERM_ID, run, _get_value, _should_run
+from hestia_earth.models.stehfestBouwman2006.n2OToAirAllOrigins import TERM_ID, run, _should_run
 
 class_path = f"hestia_earth.models.stehfestBouwman2006.{TERM_ID}"
 fixtures_folder = f"{fixtures_path}/stehfestBouwman2006/{TERM_ID}"
 
 
 @patch(f"{class_path}.valid_site_type", return_value=True)
-@patch(f"{class_path}.residue_nitrogen", return_value=0)
 @patch(f"{class_path}.most_relevant_measurement_value", return_value=[])
-def test_should_run(mock_most_relevant_measurement_value, *args):
+def test_should_run(mock_most_relevant_measurement_value, _m):
     # no measurements => no run
-    cycle = {'inputs': [], 'measurements': []}
+    cycle = {}
     should_run, *args = _should_run(cycle)
     assert not should_run
 
     # with measurements => no run
     mock_most_relevant_measurement_value.return_value = [10]
-    cycle['measurements'] = [{}]
     should_run, *args = _should_run(cycle)
     assert not should_run
 
-    # with kg N inputs => run
+    # with kg N inputs => no run
     cycle['inputs'] = [{
         'term': {
             'units': 'kg N'
         },
         'value': [100]
     }]
     should_run, *args = _should_run(cycle)
-    assert should_run is True
-
+    assert not should_run
 
-def test_get_value():
-    ecoClimateZone = '5'
-    nitrogenContent = 100
-    N_total = 7
-    assert _get_value(ecoClimateZone, nitrogenContent, N_total) == 0.08456876974469733
+    # with primary product => run
+    cycle['products'] = [{
+        'term': {
+            '@id': 'cerealsGrain'
+        },
+        'primary': True
+    }]
+    should_run, *args = _should_run(cycle)
+    assert should_run is True
 
 
 @patch(f"{class_path}._new_emission", side_effect=fake_new_emission)
 def test_run(*args):
     with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
         cycle = json.load(f)
```

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirExcreta.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirExcreta.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirInorganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006/test_noxToAirOrganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006/test_noxToAirOrganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirCropResidueDecomposition.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirCropResidueDecomposition.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirExcreta.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirExcreta.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirInorganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirInorganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirOrganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/stehfestBouwman2006GisImplementation/test_noxToAirOrganicFertilizer.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/test_otherBackgroundDatabase.py` & `hestia-earth-models-0.9.1/tests/models/test_otherBackgroundDatabase.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/transformation/post_checks/test_product.py` & `hestia-earth-models-0.9.1/tests/models/transformation/post_checks/test_product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_dataCompleteness.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_dataCompleteness.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_emission.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_emission.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_impact_assessment.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_impact_assessment.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_indicator.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_indicator.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_input.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_input.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_measurement.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_measurement.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_practice.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_practice.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_product.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_property.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_property.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_site.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/utils/test_term.py` & `hestia-earth-models-0.9.1/tests/models/utils/test_term.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-models-0.9.0/tests/models/webbEtAl2012AndSintermannEtAl2012/test_nh3ToAirOrganicFertilizer.py` & `hestia-earth-models-0.9.1/tests/models/webbEtAl2012AndSintermannEtAl2012/test_nh3ToAirOrganicFertilizer.py`

 * *Files identical despite different names*

