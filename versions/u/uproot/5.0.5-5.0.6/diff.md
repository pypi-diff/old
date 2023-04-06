# Comparing `tmp/uproot-5.0.5.tar.gz` & `tmp/uproot-5.0.6.tar.gz`

## Comparing `uproot-5.0.5.tar` & `uproot-5.0.6.tar`

### file list

```diff
@@ -1,234 +1,236 @@
--rw-r--r--   0        0        0    13217 2020-02-02 00:00:00.000000 uproot-5.0.5/.all-contributorsrc
--rw-r--r--   0        0        0      565 2020-02-02 00:00:00.000000 uproot-5.0.5/.pre-commit-config.yaml
--rw-r--r--   0        0        0      173 2020-02-02 00:00:00.000000 uproot-5.0.5/.readthedocs.yml
--rw-r--r--   0        0        0     1858 2020-02-02 00:00:00.000000 uproot-5.0.5/CITATION.cff
--rw-r--r--   0        0        0      163 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/dependabot.yml
--rw-r--r--   0        0        0      968 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/ISSUE_TEMPLATE/bug-report.md
--rw-r--r--   0        0        0      440 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/ISSUE_TEMPLATE/config.yml
--rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/ISSUE_TEMPLATE/documentation.md
--rw-r--r--   0        0        0      606 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/ISSUE_TEMPLATE/feature-request.md
--rw-r--r--   0        0        0     2232 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/workflows/build-test.yml
--rw-r--r--   0        0        0      720 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/workflows/deploy.yml
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 uproot-5.0.5/.github/workflows/semantic-pr-title.yml
--rw-r--r--   0        0        0     4261 2020-02-02 00:00:00.000000 uproot-5.0.5/dev/example-objects.py
--rw-r--r--   0        0        0     4034 2020-02-02 00:00:00.000000 uproot-5.0.5/dev/make-models.py
--rw-r--r--   0        0        0    95009 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/diagrams/abstraction-layers.png
--rw-r--r--   0        0        0    39940 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/diagrams/abstraction-layers.svg
--rw-r--r--   0        0        0    49015 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/diagrams/example-dask-graph.png
--rw-r--r--   0        0        0    70413 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/diagrams/uproot-awkward-timeline.png
--rw-r--r--   0        0        0    28715 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/diagrams/uproot-awkward-timeline.svg
--rw-r--r--   0        0        0     6794 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/logo/logo-300px-white.png
--rw-r--r--   0        0        0     8489 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/logo/logo-300px.png
--rw-r--r--   0        0        0    17651 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/logo/logo-600px.png
--rw-r--r--   0        0        0     7695 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/logo/logo.svg
--rw-r--r--   0        0        0   223219 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-img/photos/switcheroo.jpg
--rw-r--r--   0        0        0    69252 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/basic.rst
--rw-r--r--   0        0        0     2219 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/conf.py
--rw-r--r--   0        0        0     5622 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/index.rst
--rw-r--r--   0        0        0     7678 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/make_changelog.py
--rw-r--r--   0        0        0    10359 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/prepare_docstrings.py
--rw-r--r--   0        0        0       14 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/requirements.txt
--rw-r--r--   0        0        0    22209 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/uproot3-to-4.rst
--rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 uproot-5.0.5/docs-sphinx/_templates/breadcrumbs.html
--rw-r--r--   0        0        0     6754 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/__init__.py
--rw-r--r--   0        0        0    12021 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/_awkward_forth.py
--rw-r--r--   0        0        0    31365 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/_dask.py
--rw-r--r--   0        0        0    31861 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/_util.py
--rw-r--r--   0        0        0     2965 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behavior.py
--rw-r--r--   0        0        0     7472 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/cache.py
--rw-r--r--   0        0        0    16839 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/compression.py
--rw-r--r--   0        0        0     3631 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/const.py
--rw-r--r--   0        0        0    71187 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/containers.py
--rw-r--r--   0        0        0    20423 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/deserialization.py
--rw-r--r--   0        0        0      861 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/dynamic.py
--rw-r--r--   0        0        0     2984 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/exceptions.py
--rw-r--r--   0        0        0     7824 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/extras.py
--rw-r--r--   0        0        0    65811 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/model.py
--rw-r--r--   0        0        0     9549 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/pyroot.py
--rw-r--r--   0        0        0    98192 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/reading.py
--rw-r--r--   0        0        0     3137 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/serialization.py
--rw-r--r--   0        0        0    69139 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/streamers.py
--rw-r--r--   0        0        0      475 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/version.py
--rw-r--r--   0        0        0     5615 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/RooCurve.py
--rw-r--r--   0        0        0     3580 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/RooHist.py
--rw-r--r--   0        0        0    10052 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TAxis.py
--rw-r--r--   0        0        0   130388 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TBranch.py
--rw-r--r--   0        0        0      805 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TBranchElement.py
--rw-r--r--   0        0        0      364 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TDatime.py
--rw-r--r--   0        0        0     1324 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TGraph.py
--rw-r--r--   0        0        0     3451 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TGraphAsymmErrors.py
--rw-r--r--   0        0        0      271 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TGraphErrors.py
--rw-r--r--   0        0        0    12171 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TH1.py
--rw-r--r--   0        0        0     3477 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TH2.py
--rw-r--r--   0        0        0      749 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TH2Poly.py
--rw-r--r--   0        0        0     3804 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TH3.py
--rw-r--r--   0        0        0     1857 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TParameter.py
--rw-r--r--   0        0        0    12351 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TProfile.py
--rw-r--r--   0        0        0     3916 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TProfile2D.py
--rw-r--r--   0        0        0     4378 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TProfile3D.py
--rw-r--r--   0        0        0     5407 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/TTree.py
--rw-r--r--   0        0        0     1078 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/behaviors/__init__.py
--rw-r--r--   0        0        0     8270 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/__init__.py
--rw-r--r--   0        0        0     4427 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/grouped.py
--rw-r--r--   0        0        0    40728 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/identify.py
--rw-r--r--   0        0        0    14973 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/jagged.py
--rw-r--r--   0        0        0    37252 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/library.py
--rw-r--r--   0        0        0    23026 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/numerical.py
--rw-r--r--   0        0        0    31567 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/objects.py
--rw-r--r--   0        0        0    18835 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/interpretation/strings.py
--rw-r--r--   0        0        0      620 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/language/__init__.py
--rw-r--r--   0        0        0    16777 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/language/python.py
--rw-r--r--   0        0        0    25744 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/RNTuple.py
--rw-r--r--   0        0        0     4824 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TArray.py
--rw-r--r--   0        0        0    25229 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TAtt.py
--rw-r--r--   0        0        0    11179 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TBasket.py
--rw-r--r--   0        0        0    37043 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TBranch.py
--rw-r--r--   0        0        0     2594 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TClonesArray.py
--rw-r--r--   0        0        0     3214 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TDatime.py
--rw-r--r--   0        0        0    35460 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TGraph.py
--rw-r--r--   0        0        0   212692 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TH.py
--rw-r--r--   0        0        0     1743 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/THashList.py
--rw-r--r--   0        0        0    33898 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TLeaf.py
--rw-r--r--   0        0        0     3456 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TList.py
--rw-r--r--   0        0        0     2641 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TMatrixT.py
--rw-r--r--   0        0        0     3085 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TNamed.py
--rw-r--r--   0        0        0     5789 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TObjArray.py
--rw-r--r--   0        0        0     3942 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TObjString.py
--rw-r--r--   0        0        0     4504 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TObject.py
--rw-r--r--   0        0        0     8134 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TRef.py
--rw-r--r--   0        0        0     4070 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TString.py
--rw-r--r--   0        0        0     7255 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TTable.py
--rw-r--r--   0        0        0    46935 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/TTree.py
--rw-r--r--   0        0        0     1821 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/models/__init__.py
--rw-r--r--   0        0        0      704 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/sink/__init__.py
--rw-r--r--   0        0        0     6277 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/sink/file.py
--rw-r--r--   0        0        0      903 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/__init__.py
--rw-r--r--   0        0        0    16003 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/chunk.py
--rw-r--r--   0        0        0    23120 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/cursor.py
--rw-r--r--   0        0        0     8307 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/file.py
--rw-r--r--   0        0        0    12587 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/futures.py
--rw-r--r--   0        0        0    25395 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/http.py
--rw-r--r--   0        0        0     3785 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/object.py
--rw-r--r--   0        0        0    15697 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/source/xrootd.py
--rw-r--r--   0        0        0     1185 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/writing/__init__.py
--rw-r--r--   0        0        0    82851 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/writing/_cascade.py
--rw-r--r--   0        0        0    31855 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/writing/_cascadentuple.py
--rw-r--r--   0        0        0    55672 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/writing/_cascadetree.py
--rw-r--r--   0        0        0    79618 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/writing/identify.py
--rw-r--r--   0        0        0    80263 2020-02-02 00:00:00.000000 uproot-5.0.5/src/uproot/writing/writable.py
--rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/__init__.py
--rw-r--r--   0        0        0      230 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/conftest.py
--rw-r--r--   0        0        0    15805 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0001-source-class.py
--rw-r--r--   0        0        0     7352 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0006-notify-when-downloaded.py
--rw-r--r--   0        0        0     5591 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0007-single-chunk-interface.py
--rw-r--r--   0        0        0     1331 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0008-start-interpretation.py
--rw-r--r--   0        0        0      906 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0009-nested-directories.py
--rw-r--r--   0        0        0    29196 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0010-start-streamers.py
--rw-r--r--   0        0        0     4207 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0011-generate-classes-from-streamers.py
--rw-r--r--   0        0        0     3530 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0013-rntuple-anchor.py
--rw-r--r--   0        0        0     9305 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0014-all-ttree-versions.py
--rw-r--r--   0        0        0     3760 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0016-interpretations.py
--rw-r--r--   0        0        0     9682 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0017-multi-basket-multi-branch-fetch.py
--rw-r--r--   0        0        0    33935 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0018-array-fetching-interface.py
--rw-r--r--   0        0        0     8813 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0022-number-of-branches.py
--rw-r--r--   0        0        0    13960 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0023-more-interpretations-1.py
--rw-r--r--   0        0        0    24165 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0023-ttree-versions.py
--rw-r--r--   0        0        0      360 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0028-fallback-to-read-streamer.py
--rw-r--r--   0        0        0     7639 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0029-more-string-types.py
--rw-r--r--   0        0        0    23329 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0031-test-stl-containers.py
--rw-r--r--   0        0        0     4534 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0033-more-interpretations-2.py
--rw-r--r--   0        0        0    46572 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0034-generic-objects-in-ttrees.py
--rw-r--r--   0        0        0     1766 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0035-datatype-generality.py
--rw-r--r--   0        0        0     1220 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0038-memberwise-serialization.py
--rw-r--r--   0        0        0     8188 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0043-iterate-function.py
--rw-r--r--   0        0        0     1263 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0044-concatenate-function.py
--rw-r--r--   0        0        0    68981 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0046-histograms-bh-hist.py
--rw-r--r--   0        0        0     8605 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0053-parents-should-not-be-bases.py
--rw-r--r--   0        0        0     2336 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0058-detach-model-objects-from-files.py
--rw-r--r--   0        0        0      346 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0066-fix-http-fallback-freeze.py
--rw-r--r--   0        0        0     1175 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0067-common-entry-offsets.py
--rw-r--r--   0        0        0     2682 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0081-dont-parse-colons.py
--rw-r--r--   0        0        0      876 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0087-memberwise-splitting-not-implemented-messages.py
--rw-r--r--   0        0        0      937 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0088-read-with-http.py
--rw-r--r--   0        0        0      595 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0099-read-from-file-object.py
--rw-r--r--   0        0        0      529 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0112-fix-pandas-with-cut.py
--rw-r--r--   0        0        0     7914 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0118-fix-name-fetch-again.py
--rw-r--r--   0        0        0      482 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0123-atlas-issues.py
--rw-r--r--   0        0        0      409 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0126-turn-unknown-emptyarrays-into-known-types.py
--rw-r--r--   0        0        0     6118 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0167-use-the-common-histogram-interface.py
--rw-r--r--   0        0        0      442 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0172-allow-allocators-in-vector-typenames.py
--rw-r--r--   0        0        0      963 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0173-empty-and-multiprocessing-bugs.py
--rw-r--r--   0        0        0      746 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0182-complain-about-missing-files.py
--rw-r--r--   0        0        0      402 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0194-fix-lost-cuts-in-iterate.py
--rw-r--r--   0        0        0      625 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0220-contiguous-byte-ranges-in-http.py
--rw-r--r--   0        0        0     1331 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0228_read-TProfiles.py
--rw-r--r--   0        0        0     1986 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0240-read_TGraphAsymmErrors.py
--rw-r--r--   0        0        0      607 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0278-specializations-for-TParameter.py
--rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0302-pickle.py
--rw-r--r--   0        0        0      719 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0303-empty-jagged-array.py
--rw-r--r--   0        0        0    14234 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0320-start-working-on-ROOT-writing.py
--rw-r--r--   0        0        0     2919 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0322-writablefile-infrastructure.py
--rw-r--r--   0        0        0     2395 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0325-fix-windows-file-uris.py
--rw-r--r--   0        0        0      987 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0329-update-existing-root-files.py
--rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0335-empty-ttree-division-by-zero.py
--rw-r--r--   0        0        0     7571 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0341-manipulate-streamer-info.py
--rw-r--r--   0        0        0     2821 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0344-writabledirectory-can-read.py
--rw-r--r--   0        0        0     1591 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0345-bulk-copy-method.py
--rw-r--r--   0        0        0     2951 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0349-write-TObjString.py
--rw-r--r--   0        0        0     6943 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0350-read-RooCurve-RooHist.py
--rw-r--r--   0        0        0     1858 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0351-write-TList.py
--rw-r--r--   0        0        0     1175 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0352-write-THashList.py
--rw-r--r--   0        0        0      696 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0384-move-behavior_of-and-fix-383.py
--rw-r--r--   0        0        0     1527 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0398-dimensions-in-leaflist.py
--rw-r--r--   0        0        0    26536 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0405-write-a-histogram.py
--rw-r--r--   0        0        0    11518 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0406-write-a-ttree.py
--rw-r--r--   0        0        0      865 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0407-read-TDatime.py
--rw-r--r--   0        0        0    17062 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0412-write-multidimensional-numpy-to-ttree.py
--rw-r--r--   0        0        0    15363 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0414-write-jagged-arrays.py
--rw-r--r--   0        0        0    16674 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0416-writing-compressed-data.py
--rw-r--r--   0        0        0     1695 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0418-read-TTable.py
--rw-r--r--   0        0        0     3568 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0420-pyroot-uproot-interoperability.py
--rw-r--r--   0        0        0    17479 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0422-hist-integration.py
--rw-r--r--   0        0        0      439 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0430-global_index-for-tuples-of-DataFrames.py
--rw-r--r--   0        0        0      514 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0438-TClonesArray-is-not-AsGrouped.py
--rw-r--r--   0        0        0      496 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0439-check-awkward-before-numpy.py
--rw-r--r--   0        0        0     1222 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0442-regular-TClonesArray.py
--rw-r--r--   0        0        0      742 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0472-tstreamerinfo-for-ttree.py
--rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0475-remember-to-update-freesegments.py
--rw-r--r--   0        0        0      460 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0484-manually-add-model-for-TMatrixTSym_double_.py
--rw-r--r--   0        0        0     1741 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0487-implement-asdtypeinplace.py
--rw-r--r--   0        0        0     4527 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0498-create-leaf-branch-in-extend.py
--rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0519-remove-memmap-copy.py
--rw-r--r--   0        0        0      428 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0520-dynamic-classes-cant-be-abc-subclasses.py
--rw-r--r--   0        0        0      371 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0569-fBits-is-4-bytes.py
--rw-r--r--   0        0        0      550 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0576-unicode-in-names.py
--rw-r--r--   0        0        0    25906 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0578-dask-for-numpy.py
--rw-r--r--   0        0        0     1231 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0580-round-trip-for-no-flow-histograms.py
--rw-r--r--   0        0        0      747 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0589-explicitly-interpret-RVec-type.py
--rw-r--r--   0        0        0     1217 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0603-dask-delayed-open.py
--rw-r--r--   0        0        0     1839 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0609-num-enteries-func.py
--rw-r--r--   0        0        0    18214 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0610-awkward-form.py
--rw-r--r--   0        0        0     1529 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0630-rntuple-basics.py
--rw-r--r--   0        0        0    58430 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0637-setup-tests-for-AwkwardForth.py
--rw-r--r--   0        0        0      792 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0643-reading-vector-pair-TLorentzVector-int.py
--rw-r--r--   0        0        0     1442 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0651-implement-transformed-axis.py
--rw-r--r--   0        0        0     3167 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0652_dask-for-awkward.py
--rw-r--r--   0        0        0     3277 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0662-rntuple-stl-containers.py
--rw-r--r--   0        0        0     2467 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0700-dask-empty-arrays.py
--rw-r--r--   0        0        0     2528 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0705-rntuple-writing-metadata.py
--rw-r--r--   0        0        0      340 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0750-avoid-empty-TBasket-issue.py
--rw-r--r--   0        0        0      634 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0755-dask-awkward-column-projection.py
--rw-r--r--   0        0        0      546 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0791-protect-uproot-project_columns-from-dask-node-names.py
--rw-r--r--   0        0        0     4565 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0798_DAOD_PHYSLITE.py
--rw-r--r--   0        0        0     2365 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0808-fix_awkward_form_for_AsStridedObjects.py
--rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0816-separate-AwkwardForth-machines-by-TBranch.py
--rw-r--r--   0        0        0     1172 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0832-ak_add_doc-should-also-add-to-typetracer.py
--rw-r--r--   0        0        0     1249 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0840-support-tleafG.py
--rw-r--r--   0        0        0      947 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0841-fix-814.py
--rw-r--r--   0        0        0     2390 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/test_0844-fix-delete-hist-from-root.py
--rw-r--r--   0        0        0   128147 2020-02-02 00:00:00.000000 uproot-5.0.5/tests/samples/h_dynamic.pkl
--rw-r--r--   0        0        0     1914 2020-02-02 00:00:00.000000 uproot-5.0.5/.gitignore
--rw-r--r--   0        0        0     1526 2020-02-02 00:00:00.000000 uproot-5.0.5/LICENSE
--rw-r--r--   0        0        0    25899 2020-02-02 00:00:00.000000 uproot-5.0.5/README.md
--rw-r--r--   0        0        0     3602 2020-02-02 00:00:00.000000 uproot-5.0.5/pyproject.toml
--rw-r--r--   0        0        0    28208 2020-02-02 00:00:00.000000 uproot-5.0.5/PKG-INFO
+-rw-r--r--   0        0        0    13217 2020-02-02 00:00:00.000000 uproot-5.0.6/.all-contributorsrc
+-rw-r--r--   0        0        0      565 2020-02-02 00:00:00.000000 uproot-5.0.6/.pre-commit-config.yaml
+-rw-r--r--   0        0        0      173 2020-02-02 00:00:00.000000 uproot-5.0.6/.readthedocs.yml
+-rw-r--r--   0        0        0     1858 2020-02-02 00:00:00.000000 uproot-5.0.6/CITATION.cff
+-rw-r--r--   0        0        0      163 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/dependabot.yml
+-rw-r--r--   0        0        0      968 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/ISSUE_TEMPLATE/bug-report.md
+-rw-r--r--   0        0        0      440 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/ISSUE_TEMPLATE/config.yml
+-rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/ISSUE_TEMPLATE/documentation.md
+-rw-r--r--   0        0        0      606 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/ISSUE_TEMPLATE/feature-request.md
+-rw-r--r--   0        0        0     2232 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/workflows/build-test.yml
+-rw-r--r--   0        0        0      720 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/workflows/deploy.yml
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 uproot-5.0.6/.github/workflows/semantic-pr-title.yml
+-rw-r--r--   0        0        0     4261 2020-02-02 00:00:00.000000 uproot-5.0.6/dev/example-objects.py
+-rw-r--r--   0        0        0     4097 2020-02-02 00:00:00.000000 uproot-5.0.6/dev/make-models.py
+-rw-r--r--   0        0        0    95009 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/diagrams/abstraction-layers.png
+-rw-r--r--   0        0        0    39940 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/diagrams/abstraction-layers.svg
+-rw-r--r--   0        0        0    49015 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/diagrams/example-dask-graph.png
+-rw-r--r--   0        0        0    70413 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/diagrams/uproot-awkward-timeline.png
+-rw-r--r--   0        0        0    28715 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/diagrams/uproot-awkward-timeline.svg
+-rw-r--r--   0        0        0     6794 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/logo/logo-300px-white.png
+-rw-r--r--   0        0        0     8489 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/logo/logo-300px.png
+-rw-r--r--   0        0        0    17651 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/logo/logo-600px.png
+-rw-r--r--   0        0        0     7695 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/logo/logo.svg
+-rw-r--r--   0        0        0   223219 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-img/photos/switcheroo.jpg
+-rw-r--r--   0        0        0    69252 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/basic.rst
+-rw-r--r--   0        0        0     2219 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/conf.py
+-rw-r--r--   0        0        0     5622 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/index.rst
+-rw-r--r--   0        0        0     7678 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/make_changelog.py
+-rw-r--r--   0        0        0    10359 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/prepare_docstrings.py
+-rw-r--r--   0        0        0       14 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/requirements.txt
+-rw-r--r--   0        0        0    22209 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/uproot3-to-4.rst
+-rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 uproot-5.0.6/docs-sphinx/_templates/breadcrumbs.html
+-rw-r--r--   0        0        0     6754 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/__init__.py
+-rw-r--r--   0        0        0    12021 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/_awkward_forth.py
+-rw-r--r--   0        0        0    31365 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/_dask.py
+-rw-r--r--   0        0        0    32080 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/_util.py
+-rw-r--r--   0        0        0     2965 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behavior.py
+-rw-r--r--   0        0        0     7472 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/cache.py
+-rw-r--r--   0        0        0    16839 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/compression.py
+-rw-r--r--   0        0        0     3631 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/const.py
+-rw-r--r--   0        0        0    71187 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/containers.py
+-rw-r--r--   0        0        0    20423 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/deserialization.py
+-rw-r--r--   0        0        0      861 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/dynamic.py
+-rw-r--r--   0        0        0     2984 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/exceptions.py
+-rw-r--r--   0        0        0     7852 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/extras.py
+-rw-r--r--   0        0        0    65811 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/model.py
+-rw-r--r--   0        0        0     9549 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/pyroot.py
+-rw-r--r--   0        0        0    98269 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/reading.py
+-rw-r--r--   0        0        0     3137 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/serialization.py
+-rw-r--r--   0        0        0    69151 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/streamers.py
+-rw-r--r--   0        0        0      475 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/version.py
+-rw-r--r--   0        0        0     5615 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/RooCurve.py
+-rw-r--r--   0        0        0     3580 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/RooHist.py
+-rw-r--r--   0        0        0    10052 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TAxis.py
+-rw-r--r--   0        0        0   130388 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TBranch.py
+-rw-r--r--   0        0        0      805 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TBranchElement.py
+-rw-r--r--   0        0        0      364 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TDatime.py
+-rw-r--r--   0        0        0     1324 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TGraph.py
+-rw-r--r--   0        0        0     3451 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TGraphAsymmErrors.py
+-rw-r--r--   0        0        0      271 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TGraphErrors.py
+-rw-r--r--   0        0        0    12171 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TH1.py
+-rw-r--r--   0        0        0     3477 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TH2.py
+-rw-r--r--   0        0        0      749 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TH2Poly.py
+-rw-r--r--   0        0        0     3804 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TH3.py
+-rw-r--r--   0        0        0     1857 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TParameter.py
+-rw-r--r--   0        0        0    12351 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TProfile.py
+-rw-r--r--   0        0        0     3916 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TProfile2D.py
+-rw-r--r--   0        0        0     4378 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TProfile3D.py
+-rw-r--r--   0        0        0     5407 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/TTree.py
+-rw-r--r--   0        0        0     1078 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/behaviors/__init__.py
+-rw-r--r--   0        0        0     8270 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/__init__.py
+-rw-r--r--   0        0        0     4427 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/grouped.py
+-rw-r--r--   0        0        0    40728 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/identify.py
+-rw-r--r--   0        0        0    14973 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/jagged.py
+-rw-r--r--   0        0        0    37252 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/library.py
+-rw-r--r--   0        0        0    23068 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/numerical.py
+-rw-r--r--   0        0        0    34143 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/objects.py
+-rw-r--r--   0        0        0    18835 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/interpretation/strings.py
+-rw-r--r--   0        0        0      620 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/language/__init__.py
+-rw-r--r--   0        0        0    16811 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/language/python.py
+-rw-r--r--   0        0        0    25744 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/RNTuple.py
+-rw-r--r--   0        0        0     4824 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TArray.py
+-rw-r--r--   0        0        0    25313 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TAtt.py
+-rw-r--r--   0        0        0    11179 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TBasket.py
+-rw-r--r--   0        0        0    37043 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TBranch.py
+-rw-r--r--   0        0        0     2594 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TClonesArray.py
+-rw-r--r--   0        0        0     3226 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TDatime.py
+-rw-r--r--   0        0        0    35496 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TGraph.py
+-rw-r--r--   0        0        0   212956 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TH.py
+-rw-r--r--   0        0        0     1743 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/THashList.py
+-rw-r--r--   0        0        0    33898 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TLeaf.py
+-rw-r--r--   0        0        0     3456 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TList.py
+-rw-r--r--   0        0        0     2641 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TMatrixT.py
+-rw-r--r--   0        0        0     3085 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TNamed.py
+-rw-r--r--   0        0        0     5789 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TObjArray.py
+-rw-r--r--   0        0        0     3942 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TObjString.py
+-rw-r--r--   0        0        0     4516 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TObject.py
+-rw-r--r--   0        0        0     8146 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TRef.py
+-rw-r--r--   0        0        0     4070 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TString.py
+-rw-r--r--   0        0        0     7255 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TTable.py
+-rw-r--r--   0        0        0    46935 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/TTree.py
+-rw-r--r--   0        0        0     1821 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/models/__init__.py
+-rw-r--r--   0        0        0      704 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/sink/__init__.py
+-rw-r--r--   0        0        0     6277 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/sink/file.py
+-rw-r--r--   0        0        0      903 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/__init__.py
+-rw-r--r--   0        0        0    16003 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/chunk.py
+-rw-r--r--   0        0        0    23120 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/cursor.py
+-rw-r--r--   0        0        0     8307 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/file.py
+-rw-r--r--   0        0        0    14154 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/futures.py
+-rw-r--r--   0        0        0    25910 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/http.py
+-rw-r--r--   0        0        0     3785 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/object.py
+-rw-r--r--   0        0        0    15697 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/source/xrootd.py
+-rw-r--r--   0        0        0     1185 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/writing/__init__.py
+-rw-r--r--   0        0        0    82851 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/writing/_cascade.py
+-rw-r--r--   0        0        0    31855 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/writing/_cascadentuple.py
+-rw-r--r--   0        0        0    55862 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/writing/_cascadetree.py
+-rw-r--r--   0        0        0    79676 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/writing/identify.py
+-rw-r--r--   0        0        0    80263 2020-02-02 00:00:00.000000 uproot-5.0.6/src/uproot/writing/writable.py
+-rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/__init__.py
+-rw-r--r--   0        0        0      230 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/conftest.py
+-rw-r--r--   0        0        0    15805 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0001-source-class.py
+-rw-r--r--   0        0        0     7352 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0006-notify-when-downloaded.py
+-rw-r--r--   0        0        0     5591 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0007-single-chunk-interface.py
+-rw-r--r--   0        0        0     1331 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0008-start-interpretation.py
+-rw-r--r--   0        0        0      906 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0009-nested-directories.py
+-rw-r--r--   0        0        0    29196 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0010-start-streamers.py
+-rw-r--r--   0        0        0     4207 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0011-generate-classes-from-streamers.py
+-rw-r--r--   0        0        0     3530 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0013-rntuple-anchor.py
+-rw-r--r--   0        0        0     9305 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0014-all-ttree-versions.py
+-rw-r--r--   0        0        0     3760 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0016-interpretations.py
+-rw-r--r--   0        0        0     9682 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0017-multi-basket-multi-branch-fetch.py
+-rw-r--r--   0        0        0    33935 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0018-array-fetching-interface.py
+-rw-r--r--   0        0        0     8813 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0022-number-of-branches.py
+-rw-r--r--   0        0        0    13960 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0023-more-interpretations-1.py
+-rw-r--r--   0        0        0    24165 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0023-ttree-versions.py
+-rw-r--r--   0        0        0      360 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0028-fallback-to-read-streamer.py
+-rw-r--r--   0        0        0     7639 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0029-more-string-types.py
+-rw-r--r--   0        0        0    23329 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0031-test-stl-containers.py
+-rw-r--r--   0        0        0     4534 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0033-more-interpretations-2.py
+-rw-r--r--   0        0        0    46572 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0034-generic-objects-in-ttrees.py
+-rw-r--r--   0        0        0     1766 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0035-datatype-generality.py
+-rw-r--r--   0        0        0     1220 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0038-memberwise-serialization.py
+-rw-r--r--   0        0        0     8188 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0043-iterate-function.py
+-rw-r--r--   0        0        0     1263 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0044-concatenate-function.py
+-rw-r--r--   0        0        0    68981 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0046-histograms-bh-hist.py
+-rw-r--r--   0        0        0     8605 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0053-parents-should-not-be-bases.py
+-rw-r--r--   0        0        0     2336 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0058-detach-model-objects-from-files.py
+-rw-r--r--   0        0        0      346 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0066-fix-http-fallback-freeze.py
+-rw-r--r--   0        0        0     1175 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0067-common-entry-offsets.py
+-rw-r--r--   0        0        0     2682 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0081-dont-parse-colons.py
+-rw-r--r--   0        0        0      876 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0087-memberwise-splitting-not-implemented-messages.py
+-rw-r--r--   0        0        0      937 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0088-read-with-http.py
+-rw-r--r--   0        0        0      595 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0099-read-from-file-object.py
+-rw-r--r--   0        0        0      529 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0112-fix-pandas-with-cut.py
+-rw-r--r--   0        0        0     7914 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0118-fix-name-fetch-again.py
+-rw-r--r--   0        0        0      482 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0123-atlas-issues.py
+-rw-r--r--   0        0        0      409 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0126-turn-unknown-emptyarrays-into-known-types.py
+-rw-r--r--   0        0        0     6118 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0167-use-the-common-histogram-interface.py
+-rw-r--r--   0        0        0      442 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0172-allow-allocators-in-vector-typenames.py
+-rw-r--r--   0        0        0      963 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0173-empty-and-multiprocessing-bugs.py
+-rw-r--r--   0        0        0      746 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0182-complain-about-missing-files.py
+-rw-r--r--   0        0        0      402 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0194-fix-lost-cuts-in-iterate.py
+-rw-r--r--   0        0        0      625 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0220-contiguous-byte-ranges-in-http.py
+-rw-r--r--   0        0        0     1331 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0228_read-TProfiles.py
+-rw-r--r--   0        0        0     1986 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0240-read_TGraphAsymmErrors.py
+-rw-r--r--   0        0        0      607 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0278-specializations-for-TParameter.py
+-rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0302-pickle.py
+-rw-r--r--   0        0        0      719 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0303-empty-jagged-array.py
+-rw-r--r--   0        0        0    14234 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0320-start-working-on-ROOT-writing.py
+-rw-r--r--   0        0        0     2919 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0322-writablefile-infrastructure.py
+-rw-r--r--   0        0        0     2395 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0325-fix-windows-file-uris.py
+-rw-r--r--   0        0        0      987 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0329-update-existing-root-files.py
+-rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0335-empty-ttree-division-by-zero.py
+-rw-r--r--   0        0        0     7571 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0341-manipulate-streamer-info.py
+-rw-r--r--   0        0        0     2821 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0344-writabledirectory-can-read.py
+-rw-r--r--   0        0        0     1591 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0345-bulk-copy-method.py
+-rw-r--r--   0        0        0     2951 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0349-write-TObjString.py
+-rw-r--r--   0        0        0     6943 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0350-read-RooCurve-RooHist.py
+-rw-r--r--   0        0        0     1858 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0351-write-TList.py
+-rw-r--r--   0        0        0     1175 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0352-write-THashList.py
+-rw-r--r--   0        0        0      696 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0384-move-behavior_of-and-fix-383.py
+-rw-r--r--   0        0        0     1527 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0398-dimensions-in-leaflist.py
+-rw-r--r--   0        0        0    26536 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0405-write-a-histogram.py
+-rw-r--r--   0        0        0    11518 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0406-write-a-ttree.py
+-rw-r--r--   0        0        0      865 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0407-read-TDatime.py
+-rw-r--r--   0        0        0    17062 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0412-write-multidimensional-numpy-to-ttree.py
+-rw-r--r--   0        0        0    15363 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0414-write-jagged-arrays.py
+-rw-r--r--   0        0        0    16674 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0416-writing-compressed-data.py
+-rw-r--r--   0        0        0     1695 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0418-read-TTable.py
+-rw-r--r--   0        0        0     3568 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0420-pyroot-uproot-interoperability.py
+-rw-r--r--   0        0        0    17479 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0422-hist-integration.py
+-rw-r--r--   0        0        0      439 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0430-global_index-for-tuples-of-DataFrames.py
+-rw-r--r--   0        0        0      514 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0438-TClonesArray-is-not-AsGrouped.py
+-rw-r--r--   0        0        0      496 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0439-check-awkward-before-numpy.py
+-rw-r--r--   0        0        0     1222 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0442-regular-TClonesArray.py
+-rw-r--r--   0        0        0      742 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0472-tstreamerinfo-for-ttree.py
+-rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0475-remember-to-update-freesegments.py
+-rw-r--r--   0        0        0      460 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0484-manually-add-model-for-TMatrixTSym_double_.py
+-rw-r--r--   0        0        0     1741 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0487-implement-asdtypeinplace.py
+-rw-r--r--   0        0        0     4527 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0498-create-leaf-branch-in-extend.py
+-rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0519-remove-memmap-copy.py
+-rw-r--r--   0        0        0      428 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0520-dynamic-classes-cant-be-abc-subclasses.py
+-rw-r--r--   0        0        0      371 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0569-fBits-is-4-bytes.py
+-rw-r--r--   0        0        0      550 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0576-unicode-in-names.py
+-rw-r--r--   0        0        0    25906 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0578-dask-for-numpy.py
+-rw-r--r--   0        0        0     1231 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0580-round-trip-for-no-flow-histograms.py
+-rw-r--r--   0        0        0      747 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0589-explicitly-interpret-RVec-type.py
+-rw-r--r--   0        0        0     1217 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0603-dask-delayed-open.py
+-rw-r--r--   0        0        0     1839 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0609-num-enteries-func.py
+-rw-r--r--   0        0        0    18214 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0610-awkward-form.py
+-rw-r--r--   0        0        0     1529 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0630-rntuple-basics.py
+-rw-r--r--   0        0        0    58430 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0637-setup-tests-for-AwkwardForth.py
+-rw-r--r--   0        0        0      792 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0643-reading-vector-pair-TLorentzVector-int.py
+-rw-r--r--   0        0        0     1442 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0651-implement-transformed-axis.py
+-rw-r--r--   0        0        0     3167 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0652_dask-for-awkward.py
+-rw-r--r--   0        0        0     3277 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0662-rntuple-stl-containers.py
+-rw-r--r--   0        0        0     2467 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0700-dask-empty-arrays.py
+-rw-r--r--   0        0        0     2528 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0705-rntuple-writing-metadata.py
+-rw-r--r--   0        0        0      340 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0750-avoid-empty-TBasket-issue.py
+-rw-r--r--   0        0        0      634 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0755-dask-awkward-column-projection.py
+-rw-r--r--   0        0        0      546 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0791-protect-uproot-project_columns-from-dask-node-names.py
+-rw-r--r--   0        0        0     4565 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0798_DAOD_PHYSLITE.py
+-rw-r--r--   0        0        0     2365 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0808-fix_awkward_form_for_AsStridedObjects.py
+-rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0816-separate-AwkwardForth-machines-by-TBranch.py
+-rw-r--r--   0        0        0     1172 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0832-ak_add_doc-should-also-add-to-typetracer.py
+-rw-r--r--   0        0        0     1249 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0840-support-tleafG.py
+-rw-r--r--   0        0        0      947 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0841-fix-814.py
+-rw-r--r--   0        0        0     2390 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0844-fix-delete-hist-from-root.py
+-rw-r--r--   0        0        0      320 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0852-fix-strided-interp-extra-offsets.py
+-rw-r--r--   0        0        0      494 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/test_0870-writing-arrays-of-type-unknown-fix-822.py
+-rw-r--r--   0        0        0   128147 2020-02-02 00:00:00.000000 uproot-5.0.6/tests/samples/h_dynamic.pkl
+-rw-r--r--   0        0        0     1914 2020-02-02 00:00:00.000000 uproot-5.0.6/.gitignore
+-rw-r--r--   0        0        0     1526 2020-02-02 00:00:00.000000 uproot-5.0.6/LICENSE
+-rw-r--r--   0        0        0    25899 2020-02-02 00:00:00.000000 uproot-5.0.6/README.md
+-rw-r--r--   0        0        0     3602 2020-02-02 00:00:00.000000 uproot-5.0.6/pyproject.toml
+-rw-r--r--   0        0        0    28208 2020-02-02 00:00:00.000000 uproot-5.0.6/PKG-INFO
```

### Comparing `uproot-5.0.5/.all-contributorsrc` & `uproot-5.0.6/.all-contributorsrc`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/.pre-commit-config.yaml` & `uproot-5.0.6/.pre-commit-config.yaml`

 * *Files 18% similar despite different names*

```diff
@@ -10,16 +10,16 @@
   - id: debug-statements
   - id: end-of-file-fixer
   - id: mixed-line-ending
   - id: requirements-txt-fixer
   - id: trailing-whitespace
 
 - repo: https://github.com/psf/black
-  rev: 23.1.0
+  rev: 23.3.0
   hooks:
   - id: black
 
 - repo: https://github.com/charliermarsh/ruff-pre-commit
-  rev: "v0.0.255"
+  rev: "v0.0.260"
   hooks:
     - id: ruff
       args: ["--fix", "--show-fixes"]
```

### Comparing `uproot-5.0.5/CITATION.cff` & `uproot-5.0.6/CITATION.cff`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/.github/ISSUE_TEMPLATE/bug-report.md` & `uproot-5.0.6/.github/ISSUE_TEMPLATE/bug-report.md`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/.github/ISSUE_TEMPLATE/feature-request.md` & `uproot-5.0.6/.github/ISSUE_TEMPLATE/feature-request.md`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/.github/workflows/build-test.yml` & `uproot-5.0.6/.github/workflows/build-test.yml`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/.github/workflows/deploy.yml` & `uproot-5.0.6/.github/workflows/deploy.yml`

 * *Files 14% similar despite different names*

```diff
@@ -30,10 +30,10 @@
 
     steps:
     - uses: actions/download-artifact@v3
       with:
         name: artifact
         path: dist
 
-    - uses: pypa/gh-action-pypi-publish@v1.7.1
+    - uses: pypa/gh-action-pypi-publish@v1.8.4
       with:
         password: ${{ secrets.pypi_password }}
```

### Comparing `uproot-5.0.5/dev/example-objects.py` & `uproot-5.0.6/dev/example-objects.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/dev/make-models.py` & `uproot-5.0.6/dev/make-models.py`

 * *Files 5% similar despite different names*

```diff
@@ -59,15 +59,15 @@
 #             if pair not in pairs and pair[0].lower() not in keys:
 #                 pairs.append(pair)
 #     for streamer_name, streamer_version in pairs:
 #         print(streamer_name, streamer_version)
 
 
 with uproot.open("example-objects.root") as f:
-    f.file.streamers
+    f.file.streamers  # noqa: B018 (this is not a useless expression; it runs code)
 
     for classname, class_version in superclasses:
         cls = f.file.class_named(classname, class_version)
         print(cls.class_code)
         print(
             f"""
     writable = True
```

### Comparing `uproot-5.0.5/docs-img/diagrams/abstraction-layers.png` & `uproot-5.0.6/docs-img/diagrams/abstraction-layers.png`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/diagrams/abstraction-layers.svg` & `uproot-5.0.6/docs-img/diagrams/abstraction-layers.svg`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/diagrams/example-dask-graph.png` & `uproot-5.0.6/docs-img/diagrams/example-dask-graph.png`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/diagrams/uproot-awkward-timeline.png` & `uproot-5.0.6/docs-img/diagrams/uproot-awkward-timeline.png`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/diagrams/uproot-awkward-timeline.svg` & `uproot-5.0.6/docs-img/diagrams/uproot-awkward-timeline.svg`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/logo/logo-300px-white.png` & `uproot-5.0.6/docs-img/logo/logo-300px-white.png`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/logo/logo-300px.png` & `uproot-5.0.6/docs-img/logo/logo-300px.png`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/logo/logo-600px.png` & `uproot-5.0.6/docs-img/logo/logo-600px.png`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/logo/logo.svg` & `uproot-5.0.6/docs-img/logo/logo.svg`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-img/photos/switcheroo.jpg` & `uproot-5.0.6/docs-img/photos/switcheroo.jpg`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-sphinx/basic.rst` & `uproot-5.0.6/docs-sphinx/basic.rst`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-sphinx/conf.py` & `uproot-5.0.6/docs-sphinx/conf.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-sphinx/index.rst` & `uproot-5.0.6/docs-sphinx/index.rst`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-sphinx/make_changelog.py` & `uproot-5.0.6/docs-sphinx/make_changelog.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-sphinx/prepare_docstrings.py` & `uproot-5.0.6/docs-sphinx/prepare_docstrings.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/docs-sphinx/uproot3-to-4.rst` & `uproot-5.0.6/docs-sphinx/uproot3-to-4.rst`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/__init__.py` & `uproot-5.0.6/src/uproot/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/_awkward_forth.py` & `uproot-5.0.6/src/uproot/_awkward_forth.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/_dask.py` & `uproot-5.0.6/src/uproot/_dask.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/_util.py` & `uproot-5.0.6/src/uproot/_util.py`

 * *Files 1% similar despite different names*

```diff
@@ -958,7 +958,18 @@
     elif name.endswith("U32"):
         name = name[-3:]
     elif name.endswith(("8_32", "8_64")):
         name = name[-4:]
     elif name.endswith("8_U32"):
         name = name[-5:]
     return getattr(awkward.contents, name)
+
+
+def pandas_has_attr_is_numeric(pandas):
+    try:
+        function = pandas.api.types.is_any_real_numeric_dtype
+    except AttributeError:
+
+        def function(x):
+            return x.is_numeric
+
+    return function
```

### Comparing `uproot-5.0.5/src/uproot/behavior.py` & `uproot-5.0.6/src/uproot/behavior.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/cache.py` & `uproot-5.0.6/src/uproot/cache.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/compression.py` & `uproot-5.0.6/src/uproot/compression.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/const.py` & `uproot-5.0.6/src/uproot/const.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/containers.py` & `uproot-5.0.6/src/uproot/containers.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/deserialization.py` & `uproot-5.0.6/src/uproot/deserialization.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/dynamic.py` & `uproot-5.0.6/src/uproot/dynamic.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/exceptions.py` & `uproot-5.0.6/src/uproot/exceptions.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/extras.py` & `uproot-5.0.6/src/uproot/extras.py`

 * *Files 0% similar despite different names*

```diff
@@ -159,15 +159,15 @@
     """
     Imports and returns ``lz4``.
 
     Attempts to import ``xxhash`` as well.
     """
     try:
         import lz4.block
-        import xxhash
+        import xxhash  # noqa: F401
     except ModuleNotFoundError as err:
         raise ModuleNotFoundError(
             """install the 'lz4' and `xxhash` packages with:
 
     pip install lz4 xxhash
 
 or
@@ -181,15 +181,15 @@
 def xxhash():
     """
     Imports and returns ``xxhash``.
 
     Attempts to import ``lz4`` as well.
     """
     try:
-        import lz4.block
+        import lz4.block  # noqa: F401
         import xxhash
     except ModuleNotFoundError as err:
         raise ModuleNotFoundError(
             """install the 'lz4' and `xxhash` packages with:
 
     pip install lz4 xxhash
```

### Comparing `uproot-5.0.5/src/uproot/model.py` & `uproot-5.0.6/src/uproot/model.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/pyroot.py` & `uproot-5.0.6/src/uproot/pyroot.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/reading.py` & `uproot-5.0.6/src/uproot/reading.py`

 * *Files 0% similar despite different names*

```diff
@@ -164,15 +164,15 @@
                         uproot.extras.xrootd_version()
                     )
                     + """either upgrade to 5.2.0+ or set
 
     open.defaults["xrootd_handler"] = uproot.MultithreadedXRootDSource
 """
                 )
-                warnings.warn(message, FutureWarning)
+                warnings.warn(message, FutureWarning, stacklevel=1)
 
             # The key should still be set, regardless of whether we see the warning.
             self["xrootd_handler"] = uproot.source.xrootd.XRootDSource
 
         return dict.__getitem__(self, where)
 
 
@@ -945,15 +945,15 @@
         Uproot does not evaluate these rules because they are written in C++ and
         Uproot does not have access to a C++ compiler.
 
         These rules are read in the same pass that produces
         :ref:`uproot.reading.ReadOnlyFile.streamers`.
         """
         if self._streamer_rules is None:
-            self.streamers
+            self.streamers  # noqa: B018 (this is not a useless expression; it runs code)
         return self._streamer_rules
 
     def streamers_named(self, classname):
         """
         Returns a list of :doc:`uproot.streamers.Model_TStreamerInfo` objects
         that match C++ (decoded) ``classname``.
```

### Comparing `uproot-5.0.5/src/uproot/serialization.py` & `uproot-5.0.6/src/uproot/serialization.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/streamers.py` & `uproot-5.0.6/src/uproot/streamers.py`

 * *Files 0% similar despite different names*

```diff
@@ -227,15 +227,15 @@
         ]
         strided_interpretation = [
             "    @classmethod",
             "    def strided_interpretation(cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None):",
             "        if cls in breadcrumbs:",
             "            raise uproot.interpretation.objects.CannotBeStrided('classes that can contain members of the same type cannot be strided because the depth of instances is unbounded')",
             "        breadcrumbs = breadcrumbs + (cls,)",
-            "        members = []",
+            "        members = [(None, None)]",
             "        if header:",
             "            members.append(('@num_bytes', numpy.dtype('>u4')))",
             "            members.append(('@instance_version', numpy.dtype('>u2')))",
         ]
         awkward_form = [
             "    @classmethod",
             "    def awkward_form(cls, file, context):",
```

### Comparing `uproot-5.0.5/src/uproot/behaviors/RooCurve.py` & `uproot-5.0.6/src/uproot/behaviors/RooCurve.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/RooHist.py` & `uproot-5.0.6/src/uproot/behaviors/RooHist.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TAxis.py` & `uproot-5.0.6/src/uproot/behaviors/TAxis.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TBranch.py` & `uproot-5.0.6/src/uproot/behaviors/TBranch.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TBranchElement.py` & `uproot-5.0.6/src/uproot/behaviors/TBranchElement.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TGraph.py` & `uproot-5.0.6/src/uproot/behaviors/TGraph.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TGraphAsymmErrors.py` & `uproot-5.0.6/src/uproot/behaviors/TGraphAsymmErrors.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TH1.py` & `uproot-5.0.6/src/uproot/behaviors/TH1.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TH2.py` & `uproot-5.0.6/src/uproot/behaviors/TH2.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TH2Poly.py` & `uproot-5.0.6/src/uproot/behaviors/TH2Poly.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TH3.py` & `uproot-5.0.6/src/uproot/behaviors/TH3.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TParameter.py` & `uproot-5.0.6/src/uproot/behaviors/TParameter.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TProfile.py` & `uproot-5.0.6/src/uproot/behaviors/TProfile.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TProfile2D.py` & `uproot-5.0.6/src/uproot/behaviors/TProfile2D.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TProfile3D.py` & `uproot-5.0.6/src/uproot/behaviors/TProfile3D.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/TTree.py` & `uproot-5.0.6/src/uproot/behaviors/TTree.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/behaviors/__init__.py` & `uproot-5.0.6/src/uproot/behaviors/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/interpretation/__init__.py` & `uproot-5.0.6/src/uproot/interpretation/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/interpretation/grouped.py` & `uproot-5.0.6/src/uproot/interpretation/grouped.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/interpretation/identify.py` & `uproot-5.0.6/src/uproot/interpretation/identify.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/interpretation/jagged.py` & `uproot-5.0.6/src/uproot/interpretation/jagged.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/interpretation/library.py` & `uproot-5.0.6/src/uproot/interpretation/library.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/interpretation/numerical.py` & `uproot-5.0.6/src/uproot/interpretation/numerical.py`

 * *Files 1% similar despite different names*

```diff
@@ -102,14 +102,15 @@
 
                 elif entry_start < stop and start <= entry_stop:
                     basket_array = basket_arrays[basket_num]
                     output[start - entry_start : stop - entry_start] = basket_array
 
                 start = stop
 
+        output = output.newbyteorder("=")
         self.hook_before_library_finalize(
             basket_arrays=basket_arrays,
             entry_start=entry_start,
             entry_stop=entry_stop,
             entry_offsets=entry_offsets,
             library=library,
             branch=branch,
```

### Comparing `uproot-5.0.5/src/uproot/interpretation/objects.py` & `uproot-5.0.6/src/uproot/interpretation/objects.py`

 * *Files 4% similar despite different names*

```diff
@@ -535,14 +535,15 @@
 
 def _strided_awkward_form(awkward, classname, members, file, context):
     contents = {}
     for name, member in members:
         if not context["header"] and name in ("@num_bytes", "@instance_version"):
             pass
         elif not context["tobject_header"] and name in (
+            None,
             "@num_bytes",
             "@instance_version",
             "@fUniqueID",
             "@fBits",
             "@pidf",
         ):
             pass
@@ -590,18 +591,32 @@
     are instantiated as Python objects (slow); if
     :doc:`uproot.interpretation.library.Awkward`, they are behaviors passed to
     the Awkward Array's local
     `behavior <https://awkward-array.readthedocs.io/en/latest/ak.behavior.html>`__.
     """
 
     def __init__(self, model, members, original=None):
+        all_headers_prepended = False
+        first_value_loc = 0
+        while members[first_value_loc] == (None, None):
+            first_value_loc += 1
+
+        for i in range(first_value_loc, len(members)):
+            member, value = members[i]
+            if member is not None and not all_headers_prepended:
+                all_headers_prepended = True
+            if member is None and all_headers_prepended:
+                all_headers_prepended = False
+                del members[i]
+
         self._model = model
-        self._members = members
+        self._members = members[first_value_loc:]
         self._original = original
-        super().__init__(_unravel_members(members))
+        self._all_headers_prepended = all_headers_prepended
+        super().__init__(_unravel_members(self._members))
 
     @property
     def model(self):
         """
         The full Uproot deserialization model for the data
         (:doc:`uproot.model.Model` or :doc:`uproot.containers.AsContainer`).
         """
@@ -637,14 +652,18 @@
     def __eq__(self, other):
         return isinstance(other, AsStridedObjects) and self._model == other._model
 
     @property
     def numpy_dtype(self):
         return numpy.dtype(object)
 
+    @property
+    def all_headers_prepended(self):
+        return self._all_headers_prepended
+
     def awkward_form(
         self,
         file,
         context=None,
         index_format="i64",
         header=False,
         tobject_header=False,
@@ -667,14 +686,78 @@
     @property
     def typename(self):
         return uproot.model.classname_decode(self._model.__name__)[0]
 
     def _wrap_almost_finalized(self, array):
         return StridedObjectArray(self, array)
 
+    def basket_array(
+        self,
+        data,
+        byte_offsets,
+        basket,
+        branch,
+        context,
+        cursor_offset,
+        library,
+        options,
+    ):
+        self.hook_before_basket_array(
+            data=data,
+            byte_offsets=byte_offsets,
+            basket=basket,
+            branch=branch,
+            context=context,
+            cursor_offset=cursor_offset,
+            library=library,
+            options=options,
+        )
+
+        dtype, shape = uproot.interpretation.numerical._dtype_shape(self._from_dtype)
+
+        if (
+            byte_offsets is not None
+            and dtype.itemsize != byte_offsets[1] - byte_offsets[0]
+            and self.all_headers_prepended
+        ):
+            dtype = [
+                ("@headers", "u1", byte_offsets[1] - byte_offsets[0] - dtype.itemsize)
+            ] + [
+                (x, str(y[0]))
+                for x, y in sorted(dtype.fields.items(), key=lambda k: k[1])
+            ]
+            self._to_dtype = numpy.dtype(dtype)
+        try:
+            output = data.view(dtype).reshape((-1, *shape))
+
+        except ValueError as err:
+            raise ValueError(
+                """basket {} in tree/branch {} has the wrong number of bytes ({}) """
+                """for interpretation {}
+in file {}""".format(
+                    basket.basket_num,
+                    branch.object_path,
+                    len(data),
+                    self,
+                    branch.file.file_path,
+                )
+            ) from err
+        self.hook_after_basket_array(
+            data=data,
+            byte_offsets=byte_offsets,
+            basket=basket,
+            branch=branch,
+            context=context,
+            output=output,
+            cursor_offset=cursor_offset,
+            library=library,
+            options=options,
+        )
+        return output
+
 
 class CannotBeStrided(Exception):
     """
     Exception used to stop recursion over
     :ref:`uproot.model.Model.strided_interpretation` and
     :ref:`uproot.containers.AsContainer.strided_interpretation` as soon as a
     non-conforming type is found.
```

### Comparing `uproot-5.0.5/src/uproot/interpretation/strings.py` & `uproot-5.0.6/src/uproot/interpretation/strings.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/language/__init__.py` & `uproot-5.0.6/src/uproot/language/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/language/python.py` & `uproot-5.0.6/src/uproot/language/python.py`

 * *Files 0% similar despite different names*

```diff
@@ -418,14 +418,15 @@
         else:
             shorter, longer = keys, aliases
         for x in shorter:
             if x in longer:
                 warnings.warn(
                     f"{x!r} is both an alias and a branch name",
                     uproot.exceptions.NameConflictWarning,
+                    stacklevel=1,
                 )
 
         def getter(name):
             if name not in values:
                 values[name] = _expression_to_function(
                     aliases[name],
                     keys,
```

### Comparing `uproot-5.0.5/src/uproot/models/RNTuple.py` & `uproot-5.0.6/src/uproot/models/RNTuple.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TArray.py` & `uproot-5.0.6/src/uproot/models/TArray.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TAtt.py` & `uproot-5.0.6/src/uproot/models/TAtt.py`

 * *Files 4% similar despite different names*

```diff
@@ -34,15 +34,15 @@
             self._members["fLineWidth"],
         ) = cursor.fields(chunk, _tattline1_format1, context)
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.append(("fLineColor", numpy.dtype(">i2")))
         members.append(("fLineStyle", numpy.dtype(">i2")))
         members.append(("fLineWidth", numpy.dtype(">i2")))
         return uproot.interpretation.objects.AsStridedObjects(
@@ -100,15 +100,15 @@
             self._members["fLineWidth"],
         ) = cursor.fields(chunk, _tattline1_format1, context)
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.append(("fLineColor", numpy.dtype(">i2")))
         members.append(("fLineStyle", numpy.dtype(">i2")))
         members.append(("fLineWidth", numpy.dtype(">i2")))
         return uproot.interpretation.objects.AsStridedObjects(
@@ -194,15 +194,15 @@
             chunk, _tattfill1_format1, context
         )
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.append(("fFillColor", numpy.dtype(">i2")))
         members.append(("fFillStyle", numpy.dtype(">i2")))
         return uproot.interpretation.objects.AsStridedObjects(
             cls, members, original=original
@@ -254,15 +254,15 @@
             chunk, _tattfill2_format1, context
         )
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.append(("fFillColor", numpy.dtype(">i2")))
         members.append(("fFillStyle", numpy.dtype(">i2")))
         return uproot.interpretation.objects.AsStridedObjects(
             cls, members, original=original
@@ -344,15 +344,15 @@
             self._members["fMarkerSize"],
         ) = cursor.fields(chunk, _tattmarker2_format1, context)
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.append(("fMarkerColor", numpy.dtype(">i2")))
         members.append(("fMarkerStyle", numpy.dtype(">i2")))
         members.append(("fMarkerSize", numpy.dtype(">f4")))
         return uproot.interpretation.objects.AsStridedObjects(
@@ -495,15 +495,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.append(("fNdivisions", numpy.dtype(">i4")))
         members.append(("fAxisColor", numpy.dtype(">i2")))
         members.append(("fLabelColor", numpy.dtype(">i2")))
         members.append(("fLabelFont", numpy.dtype(">i2")))
@@ -659,15 +659,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         return uproot.interpretation.objects.AsStridedObjects(
             cls, members, original=original
         )
```

### Comparing `uproot-5.0.5/src/uproot/models/TBasket.py` & `uproot-5.0.6/src/uproot/models/TBasket.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TBranch.py` & `uproot-5.0.6/src/uproot/models/TBranch.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TClonesArray.py` & `uproot-5.0.6/src/uproot/models/TClonesArray.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TDatime.py` & `uproot-5.0.6/src/uproot/models/TDatime.py`

 * *Files 2% similar despite different names*

```diff
@@ -57,15 +57,15 @@
             forth_obj.go_to(temp_form)
         self._members["fDatime"] = cursor.field(chunk, _tdatime_format1, context)
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.append(("fDatime", numpy.dtype(">u4")))
         return uproot.interpretation.objects.AsStridedObjects(
             cls, members, original=original
         )
```

### Comparing `uproot-5.0.5/src/uproot/models/TGraph.py` & `uproot-5.0.6/src/uproot/models/TGraph.py`

 * *Files 1% similar despite different names*

```diff
@@ -194,15 +194,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TNamed", 1)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -424,15 +424,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TGraph", 4)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -629,15 +629,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TGraph", 4)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
```

### Comparing `uproot-5.0.5/src/uproot/models/TH.py` & `uproot-5.0.6/src/uproot/models/TH.py`

 * *Files 1% similar despite different names*

```diff
@@ -279,15 +279,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TNamed", 1)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -701,15 +701,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TNamed", 1)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -1090,15 +1090,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1", 8)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -1291,15 +1291,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1", 8)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -1487,15 +1487,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1", 8)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -1649,15 +1649,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1", 8)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -1806,15 +1806,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1", 8)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -1963,15 +1963,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1", 8)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -2125,15 +2125,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1", 8)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -2287,15 +2287,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH2", 5)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -2450,15 +2450,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH2", 5)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -2608,15 +2608,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH2", 5)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -2771,15 +2771,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH2", 5)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -2934,15 +2934,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH2", 5)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -3097,15 +3097,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH3", 6)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -3261,15 +3261,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH3", 6)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -3420,15 +3420,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH3", 6)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -3584,15 +3584,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH3", 6)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -3748,15 +3748,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH3", 6)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -3932,15 +3932,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH1D", 3)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -4171,15 +4171,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH2D", 4)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
@@ -4412,15 +4412,15 @@
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
         if cls in breadcrumbs:
             raise uproot.interpretation.objects.CannotBeStrided(
                 "classes that can contain members of the same type cannot be strided because the depth of instances is unbounded"
             )
         breadcrumbs = (*breadcrumbs, cls)
-        members = []
+        members = [(None, None)]
         if header:
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@instance_version", numpy.dtype(">u2")))
         members.extend(
             file.class_named("TH3D", 4)
             .strided_interpretation(file, header, tobject_header, breadcrumbs)
             .members
```

### Comparing `uproot-5.0.5/src/uproot/models/THashList.py` & `uproot-5.0.6/src/uproot/models/THashList.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TLeaf.py` & `uproot-5.0.6/src/uproot/models/TLeaf.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TList.py` & `uproot-5.0.6/src/uproot/models/TList.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TMatrixT.py` & `uproot-5.0.6/src/uproot/models/TMatrixT.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TNamed.py` & `uproot-5.0.6/src/uproot/models/TNamed.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TObjArray.py` & `uproot-5.0.6/src/uproot/models/TObjArray.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TObjString.py` & `uproot-5.0.6/src/uproot/models/TObjString.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TObject.py` & `uproot-5.0.6/src/uproot/models/TObject.py`

 * *Files 0% similar despite different names*

```diff
@@ -71,15 +71,15 @@
             + _tobject_format2.pack(self.member("@fUniqueID"), tobject_flags)
         )
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         if tobject_header:
             members.append(("@instance_version", numpy.dtype(">u2")))
             members.append(("@num_bytes", numpy.dtype(">u4")))
             members.append(("@fUniqueID", numpy.dtype(">u4")))
             members.append(("@fBits", numpy.dtype(">u4")))
             members.append(("@pidf", numpy.dtype(">u2")))
         return uproot.interpretation.objects.AsStridedObjects(
```

### Comparing `uproot-5.0.5/src/uproot/models/TRef.py` & `uproot-5.0.6/src/uproot/models/TRef.py`

 * *Files 1% similar despite different names*

```diff
@@ -49,15 +49,15 @@
     def __repr__(self):
         return f"<TRef {self._ref}>"
 
     @classmethod
     def strided_interpretation(
         cls, file, header=False, tobject_header=True, breadcrumbs=(), original=None
     ):
-        members = []
+        members = [(None, None)]
         members.append(("@pidf", numpy.dtype(">u2")))
         members.append(("ref", numpy.dtype(">u4")))
         members.append(("@other1", numpy.dtype(">u2")))
         members.append(("@other2", numpy.dtype(">u4")))
 
         return uproot.interpretation.objects.AsStridedObjects(
             cls, members, original=original
```

### Comparing `uproot-5.0.5/src/uproot/models/TString.py` & `uproot-5.0.6/src/uproot/models/TString.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TTable.py` & `uproot-5.0.6/src/uproot/models/TTable.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/TTree.py` & `uproot-5.0.6/src/uproot/models/TTree.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/models/__init__.py` & `uproot-5.0.6/src/uproot/models/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/sink/__init__.py` & `uproot-5.0.6/src/uproot/sink/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/sink/file.py` & `uproot-5.0.6/src/uproot/sink/file.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/source/__init__.py` & `uproot-5.0.6/src/uproot/source/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/source/chunk.py` & `uproot-5.0.6/src/uproot/source/chunk.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/source/cursor.py` & `uproot-5.0.6/src/uproot/source/cursor.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/source/file.py` & `uproot-5.0.6/src/uproot/source/file.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/source/futures.py` & `uproot-5.0.6/src/uproot/source/futures.py`

 * *Files 3% similar despite different names*

```diff
@@ -394,7 +394,62 @@
             worker.resource.__enter__()
 
     def __exit__(self, exception_type, exception_value, traceback):
         self.shutdown()
         for worker in self._workers:
             worker.resource.__exit__(exception_type, exception_value, traceback)
         self._closed = True
+
+
+##################### use-case 4: resources for I/O with trivial executor
+
+
+class ResourceTrivialExecutor(TrivialExecutor):
+    """
+    Args:
+        resource (:doc:`uproot.source.chunk.Resource`): Resource to
+            wrap as :doc:`uproot.source.futures.ResourceFuture` object.
+
+    A :doc:`uproot.source.futures.ResourceTrivialExecutor` is bound
+    to a resource, such as a file handle.
+    """
+
+    def __init__(self, resource):
+        self._resource = resource
+        self._closed = False
+
+    def __repr__(self):
+        return f"<ResourceTrivialExecutor at 0x{id(self):012x}>"
+
+    def submit(self, future):
+        """
+        Pass the ``task`` as a
+        :doc:`uproot.source.futures.ResourceFuture` so that it will be
+        executed with its :ref:`self._resource`.
+        """
+        assert isinstance(future, ResourceFuture)
+        if self.closed:
+            raise OSError(
+                "resource is closed for file {}".format(
+                    self._workers[0].resource.file_path
+                )
+            )
+        future._run(self._resource)
+        return future
+
+    def close(self):
+        """
+        Stops the :doc:`uproot.source.futures.ResourceTrivialExecutor`
+        """
+        self.__exit__(None, None, None)
+
+    @property
+    def closed(self):
+        """
+        True if the :doc:`uproot.source.futures.ResourceTrivialExecutor` has
+        been stopped.
+        """
+        return self._closed
+
+    def __exit__(self, exception_type, exception_value, traceback):
+        self.shutdown()
+        self._closed = True
```

### Comparing `uproot-5.0.5/src/uproot/source/http.py` & `uproot-5.0.6/src/uproot/source/http.py`

 * *Files 2% similar despite different names*

```diff
@@ -560,17 +560,23 @@
 
         self._fallback = None
         self._fallback_options = options.copy()
         self._fallback_options["num_workers"] = self._num_fallback_workers
         self._open()
 
     def _open(self):
-        self._executor = uproot.source.futures.ResourceThreadPoolExecutor(
-            [HTTPResource(self._file_path, self._timeout)]
-        )
+        # if running in a jupyter lite environment, then use a TrivialExecutor
+        if sys.platform == "emscripten":
+            self._executor = uproot.source.futures.ResourceTrivialExecutor(
+                HTTPResource(self._file_path, self._timeout)
+            )
+        else:
+            self._executor = uproot.source.futures.ResourceThreadPoolExecutor(
+                [HTTPResource(self._file_path, self._timeout)]
+            )
 
     def __getstate__(self):
         state = dict(self.__dict__)
         state.pop("_executor")
         return state
 
     def __setstate__(self, state):
@@ -661,22 +667,28 @@
         return self._num_bytes
 
     @property
     def parsed_url(self):
         """
         A ``urllib.parse.ParseResult`` version of the ``file_path``.
         """
-        return self._executor.workers[0].resource.parsed_url
+        if sys.platform == "emscripten":
+            return urlparse(self._file_path)
+        else:
+            return self._executor.workers[0].resource.parsed_url
 
     @property
     def auth_headers(self):
         """
         Dict containing auth headers, if any
         """
-        return self._executor.workers[0].resource.auth_headers
+        if sys.platform == "emscripten":
+            return basic_auth_headers(self.parsed_url)
+        else:
+            return self._executor.workers[0].resource.auth_headers
 
     @property
     def fallback(self):
         """
         If None, the source has not encountered an unsuccessful multipart GET
         and no fallback is needed yet.
```

### Comparing `uproot-5.0.5/src/uproot/source/object.py` & `uproot-5.0.6/src/uproot/source/object.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/source/xrootd.py` & `uproot-5.0.6/src/uproot/source/xrootd.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/writing/__init__.py` & `uproot-5.0.6/src/uproot/writing/__init__.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/writing/_cascade.py` & `uproot-5.0.6/src/uproot/writing/_cascade.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/writing/_cascadentuple.py` & `uproot-5.0.6/src/uproot/writing/_cascadentuple.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/src/uproot/writing/_cascadetree.py` & `uproot-5.0.6/src/uproot/writing/_cascadetree.py`

 * *Files 1% similar despite different names*

```diff
@@ -320,15 +320,17 @@
             "fAutoSave": -300000000,
             "fAutoFlush": -30000000,
             "fEstimate": 1000000,
         }
         self._key = None
 
     def _branch_ak_to_np(self, branch_datashape):
-        if type(branch_datashape).__name__ == "NumpyType":
+        if type(branch_datashape).__name__ == "UnknownType":
+            return numpy.dtype("float64")
+        elif type(branch_datashape).__name__ == "NumpyType":
             return numpy.dtype(branch_datashape.primitive)
         elif type(branch_datashape).__name__ == "PrimitiveType":
             return numpy.dtype(branch_datashape.dtype)
         elif type(branch_datashape).__name__ == "RegularType":
             content = self._branch_ak_to_np(branch_datashape.content)
             if content is None:
                 return None
@@ -504,15 +506,17 @@
             sink.flush()
 
         provided = None
 
         if uproot._util.from_module(data, "pandas"):
             import pandas
 
-            if isinstance(data, pandas.DataFrame) and data.index.is_numeric():
+            if isinstance(
+                data, pandas.DataFrame
+            ) and uproot._util.pandas_has_attr_is_numeric(pandas)(data.index):
                 provided = dataframe_to_dict(data)
 
         if uproot._util.from_module(data, "awkward"):
             try:
                 awkward = uproot.extras.awkward()
             except ModuleNotFoundError as err:
                 raise TypeError(
@@ -714,15 +718,15 @@
 
                 shape = [len(content)]
                 while not isinstance(content, awkward.contents.NumpyArray):
                     if isinstance(content, awkward.contents.IndexedArray):
                         content = content.project()
 
                     elif isinstance(content, awkward.contents.EmptyArray):
-                        content = content.to_NumpyArray()
+                        content = content.to_NumpyArray(dtype=numpy.float64)
 
                     elif isinstance(content, awkward.contents.RegularArray):
                         shape.append(content.size)
                         content = content.content
 
                     else:
                         raise AssertionError(
```

### Comparing `uproot-5.0.5/src/uproot/writing/identify.py` & `uproot-5.0.6/src/uproot/writing/identify.py`

 * *Files 0% similar despite different names*

```diff
@@ -49,15 +49,17 @@
     Raises ``TypeError`` if ``obj`` is not recognized as writable data.
     """
     is_ttree = False
 
     if uproot._util.from_module(obj, "pandas"):
         import pandas
 
-        if isinstance(obj, pandas.DataFrame) and obj.index.is_numeric():
+        if isinstance(
+            obj, pandas.DataFrame
+        ) and uproot._util.pandas_has_attr_is_numeric(pandas)(obj.index):
             obj = uproot.writing._cascadetree.dataframe_to_dict(obj)
 
     if uproot._util.from_module(obj, "awkward"):
         import awkward
 
         if isinstance(obj, awkward.Array):
             obj = {"": obj}
```

### Comparing `uproot-5.0.5/src/uproot/writing/writable.py` & `uproot-5.0.6/src/uproot/writing/writable.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0001-source-class.py` & `uproot-5.0.6/tests/test_0001-source-class.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0006-notify-when-downloaded.py` & `uproot-5.0.6/tests/test_0006-notify-when-downloaded.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0007-single-chunk-interface.py` & `uproot-5.0.6/tests/test_0007-single-chunk-interface.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0008-start-interpretation.py` & `uproot-5.0.6/tests/test_0008-start-interpretation.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0009-nested-directories.py` & `uproot-5.0.6/tests/test_0009-nested-directories.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0010-start-streamers.py` & `uproot-5.0.6/tests/test_0010-start-streamers.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0011-generate-classes-from-streamers.py` & `uproot-5.0.6/tests/test_0011-generate-classes-from-streamers.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0013-rntuple-anchor.py` & `uproot-5.0.6/tests/test_0013-rntuple-anchor.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0014-all-ttree-versions.py` & `uproot-5.0.6/tests/test_0014-all-ttree-versions.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0016-interpretations.py` & `uproot-5.0.6/tests/test_0016-interpretations.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0017-multi-basket-multi-branch-fetch.py` & `uproot-5.0.6/tests/test_0017-multi-basket-multi-branch-fetch.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0018-array-fetching-interface.py` & `uproot-5.0.6/tests/test_0018-array-fetching-interface.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0022-number-of-branches.py` & `uproot-5.0.6/tests/test_0022-number-of-branches.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0023-more-interpretations-1.py` & `uproot-5.0.6/tests/test_0023-more-interpretations-1.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0023-ttree-versions.py` & `uproot-5.0.6/tests/test_0023-ttree-versions.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0029-more-string-types.py` & `uproot-5.0.6/tests/test_0029-more-string-types.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0031-test-stl-containers.py` & `uproot-5.0.6/tests/test_0031-test-stl-containers.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0033-more-interpretations-2.py` & `uproot-5.0.6/tests/test_0033-more-interpretations-2.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0034-generic-objects-in-ttrees.py` & `uproot-5.0.6/tests/test_0034-generic-objects-in-ttrees.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0035-datatype-generality.py` & `uproot-5.0.6/tests/test_0035-datatype-generality.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0038-memberwise-serialization.py` & `uproot-5.0.6/tests/test_0038-memberwise-serialization.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0043-iterate-function.py` & `uproot-5.0.6/tests/test_0043-iterate-function.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0044-concatenate-function.py` & `uproot-5.0.6/tests/test_0044-concatenate-function.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0046-histograms-bh-hist.py` & `uproot-5.0.6/tests/test_0046-histograms-bh-hist.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0053-parents-should-not-be-bases.py` & `uproot-5.0.6/tests/test_0053-parents-should-not-be-bases.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0058-detach-model-objects-from-files.py` & `uproot-5.0.6/tests/test_0058-detach-model-objects-from-files.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0067-common-entry-offsets.py` & `uproot-5.0.6/tests/test_0067-common-entry-offsets.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0081-dont-parse-colons.py` & `uproot-5.0.6/tests/test_0081-dont-parse-colons.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0087-memberwise-splitting-not-implemented-messages.py` & `uproot-5.0.6/tests/test_0087-memberwise-splitting-not-implemented-messages.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0088-read-with-http.py` & `uproot-5.0.6/tests/test_0088-read-with-http.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0099-read-from-file-object.py` & `uproot-5.0.6/tests/test_0099-read-from-file-object.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0112-fix-pandas-with-cut.py` & `uproot-5.0.6/tests/test_0112-fix-pandas-with-cut.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0118-fix-name-fetch-again.py` & `uproot-5.0.6/tests/test_0118-fix-name-fetch-again.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0167-use-the-common-histogram-interface.py` & `uproot-5.0.6/tests/test_0167-use-the-common-histogram-interface.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0173-empty-and-multiprocessing-bugs.py` & `uproot-5.0.6/tests/test_0173-empty-and-multiprocessing-bugs.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0182-complain-about-missing-files.py` & `uproot-5.0.6/tests/test_0182-complain-about-missing-files.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0220-contiguous-byte-ranges-in-http.py` & `uproot-5.0.6/tests/test_0220-contiguous-byte-ranges-in-http.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0228_read-TProfiles.py` & `uproot-5.0.6/tests/test_0228_read-TProfiles.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0240-read_TGraphAsymmErrors.py` & `uproot-5.0.6/tests/test_0240-read_TGraphAsymmErrors.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0278-specializations-for-TParameter.py` & `uproot-5.0.6/tests/test_0278-specializations-for-TParameter.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0302-pickle.py` & `uproot-5.0.6/tests/test_0302-pickle.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0303-empty-jagged-array.py` & `uproot-5.0.6/tests/test_0303-empty-jagged-array.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0320-start-working-on-ROOT-writing.py` & `uproot-5.0.6/tests/test_0320-start-working-on-ROOT-writing.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0322-writablefile-infrastructure.py` & `uproot-5.0.6/tests/test_0322-writablefile-infrastructure.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0325-fix-windows-file-uris.py` & `uproot-5.0.6/tests/test_0325-fix-windows-file-uris.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0329-update-existing-root-files.py` & `uproot-5.0.6/tests/test_0329-update-existing-root-files.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0341-manipulate-streamer-info.py` & `uproot-5.0.6/tests/test_0341-manipulate-streamer-info.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0344-writabledirectory-can-read.py` & `uproot-5.0.6/tests/test_0344-writabledirectory-can-read.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0345-bulk-copy-method.py` & `uproot-5.0.6/tests/test_0345-bulk-copy-method.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0349-write-TObjString.py` & `uproot-5.0.6/tests/test_0349-write-TObjString.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0350-read-RooCurve-RooHist.py` & `uproot-5.0.6/tests/test_0350-read-RooCurve-RooHist.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0351-write-TList.py` & `uproot-5.0.6/tests/test_0351-write-TList.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0352-write-THashList.py` & `uproot-5.0.6/tests/test_0352-write-THashList.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0384-move-behavior_of-and-fix-383.py` & `uproot-5.0.6/tests/test_0384-move-behavior_of-and-fix-383.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0398-dimensions-in-leaflist.py` & `uproot-5.0.6/tests/test_0398-dimensions-in-leaflist.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0405-write-a-histogram.py` & `uproot-5.0.6/tests/test_0405-write-a-histogram.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0406-write-a-ttree.py` & `uproot-5.0.6/tests/test_0406-write-a-ttree.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0407-read-TDatime.py` & `uproot-5.0.6/tests/test_0407-read-TDatime.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0412-write-multidimensional-numpy-to-ttree.py` & `uproot-5.0.6/tests/test_0412-write-multidimensional-numpy-to-ttree.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0414-write-jagged-arrays.py` & `uproot-5.0.6/tests/test_0414-write-jagged-arrays.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0416-writing-compressed-data.py` & `uproot-5.0.6/tests/test_0416-writing-compressed-data.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0418-read-TTable.py` & `uproot-5.0.6/tests/test_0418-read-TTable.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0420-pyroot-uproot-interoperability.py` & `uproot-5.0.6/tests/test_0420-pyroot-uproot-interoperability.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0422-hist-integration.py` & `uproot-5.0.6/tests/test_0422-hist-integration.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0438-TClonesArray-is-not-AsGrouped.py` & `uproot-5.0.6/tests/test_0438-TClonesArray-is-not-AsGrouped.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0442-regular-TClonesArray.py` & `uproot-5.0.6/tests/test_0442-regular-TClonesArray.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0472-tstreamerinfo-for-ttree.py` & `uproot-5.0.6/tests/test_0472-tstreamerinfo-for-ttree.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0475-remember-to-update-freesegments.py` & `uproot-5.0.6/tests/test_0475-remember-to-update-freesegments.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0487-implement-asdtypeinplace.py` & `uproot-5.0.6/tests/test_0487-implement-asdtypeinplace.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0498-create-leaf-branch-in-extend.py` & `uproot-5.0.6/tests/test_0498-create-leaf-branch-in-extend.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0576-unicode-in-names.py` & `uproot-5.0.6/tests/test_0576-unicode-in-names.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0578-dask-for-numpy.py` & `uproot-5.0.6/tests/test_0578-dask-for-numpy.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0580-round-trip-for-no-flow-histograms.py` & `uproot-5.0.6/tests/test_0580-round-trip-for-no-flow-histograms.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0589-explicitly-interpret-RVec-type.py` & `uproot-5.0.6/tests/test_0589-explicitly-interpret-RVec-type.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0603-dask-delayed-open.py` & `uproot-5.0.6/tests/test_0603-dask-delayed-open.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0609-num-enteries-func.py` & `uproot-5.0.6/tests/test_0609-num-enteries-func.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0610-awkward-form.py` & `uproot-5.0.6/tests/test_0610-awkward-form.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0630-rntuple-basics.py` & `uproot-5.0.6/tests/test_0630-rntuple-basics.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0637-setup-tests-for-AwkwardForth.py` & `uproot-5.0.6/tests/test_0637-setup-tests-for-AwkwardForth.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0643-reading-vector-pair-TLorentzVector-int.py` & `uproot-5.0.6/tests/test_0643-reading-vector-pair-TLorentzVector-int.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0651-implement-transformed-axis.py` & `uproot-5.0.6/tests/test_0651-implement-transformed-axis.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0652_dask-for-awkward.py` & `uproot-5.0.6/tests/test_0652_dask-for-awkward.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0662-rntuple-stl-containers.py` & `uproot-5.0.6/tests/test_0662-rntuple-stl-containers.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0700-dask-empty-arrays.py` & `uproot-5.0.6/tests/test_0700-dask-empty-arrays.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0705-rntuple-writing-metadata.py` & `uproot-5.0.6/tests/test_0705-rntuple-writing-metadata.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0755-dask-awkward-column-projection.py` & `uproot-5.0.6/tests/test_0755-dask-awkward-column-projection.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0791-protect-uproot-project_columns-from-dask-node-names.py` & `uproot-5.0.6/tests/test_0791-protect-uproot-project_columns-from-dask-node-names.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0798_DAOD_PHYSLITE.py` & `uproot-5.0.6/tests/test_0798_DAOD_PHYSLITE.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0808-fix_awkward_form_for_AsStridedObjects.py` & `uproot-5.0.6/tests/test_0808-fix_awkward_form_for_AsStridedObjects.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0816-separate-AwkwardForth-machines-by-TBranch.py` & `uproot-5.0.6/tests/test_0816-separate-AwkwardForth-machines-by-TBranch.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0832-ak_add_doc-should-also-add-to-typetracer.py` & `uproot-5.0.6/tests/test_0832-ak_add_doc-should-also-add-to-typetracer.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0840-support-tleafG.py` & `uproot-5.0.6/tests/test_0840-support-tleafG.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0841-fix-814.py` & `uproot-5.0.6/tests/test_0841-fix-814.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/test_0844-fix-delete-hist-from-root.py` & `uproot-5.0.6/tests/test_0844-fix-delete-hist-from-root.py`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/tests/samples/h_dynamic.pkl` & `uproot-5.0.6/tests/samples/h_dynamic.pkl`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/.gitignore` & `uproot-5.0.6/.gitignore`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/LICENSE` & `uproot-5.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/README.md` & `uproot-5.0.6/README.md`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/pyproject.toml` & `uproot-5.0.6/pyproject.toml`

 * *Files identical despite different names*

### Comparing `uproot-5.0.5/PKG-INFO` & `uproot-5.0.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: uproot
-Version: 5.0.5
+Version: 5.0.6
 Summary: ROOT I/O in pure Python and NumPy.
 Project-URL: Download, https://github.com/scikit-hep/uproot5/releases
 Project-URL: Homepage, https://github.com/scikit-hep/uproot5
 Author-email: Jim Pivarski <pivarski@princeton.edu>
 License-Expression: BSD-3-Clause
 License-File: LICENSE
 Classifier: Development Status :: 5 - Production/Stable
```

