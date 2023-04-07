# Comparing `tmp/gaphor-2.9.1.tar.gz` & `tmp/gaphor-2.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gaphor-2.9.1.tar", max compression
+gzip compressed data, was "gaphor-2.9.2.tar", max compression
```

## Comparing `gaphor-2.9.1.tar` & `gaphor-2.9.2.tar`

### file list

```diff
@@ -1,730 +1,730 @@
--rw-r--r--   0        0        0    10901 2022-03-18 01:28:35.000000 gaphor-2.9.1/LICENSE.txt
--rw-r--r--   0        0        0    35606 2022-03-18 01:28:35.000000 gaphor-2.9.1/README.md
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/__init__.py
--rw-r--r--   0        0        0      138 2022-03-18 01:34:37.794625 gaphor-2.9.1/gaphor/C4Model/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     1543 2022-03-18 01:34:37.798625 gaphor-2.9.1/gaphor/C4Model/__pycache__/c4model.cpython-310.pyc
--rw-r--r--   0        0        0      723 2022-03-18 01:34:37.798625 gaphor-2.9.1/gaphor/C4Model/__pycache__/iconname.cpython-310.pyc
--rw-r--r--   0        0        0     1554 2022-03-18 01:34:37.798625 gaphor-2.9.1/gaphor/C4Model/__pycache__/modelinglanguage.cpython-310.pyc
--rw-r--r--   0        0        0     2881 2022-03-18 01:34:37.802625 gaphor-2.9.1/gaphor/C4Model/__pycache__/propertypages.cpython-310.pyc
--rw-r--r--   0        0        0     2943 2022-03-18 01:34:37.810625 gaphor-2.9.1/gaphor/C4Model/__pycache__/toolbox.cpython-310.pyc
--rw-r--r--   0        0        0     1455 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/c4model.py
--rw-r--r--   0        0        0      190 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/diagramitems/__init__.py
--rw-r--r--   0        0        0      374 2022-03-18 01:34:37.802625 gaphor-2.9.1/gaphor/C4Model/diagramitems/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2328 2022-03-18 01:34:37.806625 gaphor-2.9.1/gaphor/C4Model/diagramitems/__pycache__/container.cpython-310.pyc
--rw-r--r--   0        0        0     2671 2022-03-18 01:34:37.806625 gaphor-2.9.1/gaphor/C4Model/diagramitems/__pycache__/database.cpython-310.pyc
--rw-r--r--   0        0        0     2774 2022-03-18 01:34:37.806625 gaphor-2.9.1/gaphor/C4Model/diagramitems/__pycache__/person.cpython-310.pyc
--rw-r--r--   0        0        0     2020 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/diagramitems/container.py
--rw-r--r--   0        0        0     2243 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/diagramitems/database.py
--rw-r--r--   0        0        0     2266 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/diagramitems/person.py
--rw-r--r--   0        0        0      550 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/iconname.py
--rw-r--r--   0        0        0      970 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/modelinglanguage.py
--rw-r--r--   0        0        0     3598 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/propertypages.glade
--rw-r--r--   0        0        0     2487 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/propertypages.py
--rw-r--r--   0        0        0     2560 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/propertypages.ui
--rw-r--r--   0        0        0     4118 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/C4Model/toolbox.py
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/__init__.py
--rw-r--r--   0        0        0      136 2022-03-18 01:34:38.098625 gaphor-2.9.1/gaphor/RAAML/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0      202 2022-03-18 01:34:46.994611 gaphor-2.9.1/gaphor/RAAML/__pycache__/diagramitems.cpython-310.pyc
--rw-r--r--   0        0        0     1581 2022-03-18 01:34:48.122610 gaphor-2.9.1/gaphor/RAAML/__pycache__/modelinglanguage.cpython-310.pyc
--rw-r--r--   0        0        0    12468 2022-03-18 01:34:38.102625 gaphor-2.9.1/gaphor/RAAML/__pycache__/raaml.cpython-310.pyc
--rw-r--r--   0        0        0      686 2022-03-18 01:34:46.958611 gaphor-2.9.1/gaphor/RAAML/__pycache__/toolbox.cpython-310.pyc
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/__init__.py
--rw-r--r--   0        0        0     2385 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/and.svg
--rw-r--r--   0        0        0      474 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/basic_event.svg
--rw-r--r--   0        0        0      484 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/conditional_event.svg
--rw-r--r--   0        0        0      603 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/dormant_event.svg
--rw-r--r--   0        0        0      504 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/house_event.svg
--rw-r--r--   0        0        0      878 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/inhibit.svg
--rw-r--r--   0        0        0      983 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/majority_vote.svg
--rw-r--r--   0        0        0      738 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/not.svg
--rw-r--r--   0        0        0     2252 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/or.svg
--rw-r--r--   0        0        0      973 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/seq.svg
--rw-r--r--   0        0        0      478 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/transfer_in.svg
--rw-r--r--   0        0        0     1034 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/xor.svg
--rw-r--r--   0        0        0      689 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagram_svgs/zero_event.svg
--rw-r--r--   0        0        0       63 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/diagramitems.py
--rw-r--r--   0        0        0      927 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/__init__.py
--rw-r--r--   0        0        0     1254 2022-03-18 01:34:46.958611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2870 2022-03-18 01:34:46.962611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/andgate.cpython-310.pyc
--rw-r--r--   0        0        0     2555 2022-03-18 01:34:46.966611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/basicevent.cpython-310.pyc
--rw-r--r--   0        0        0     2160 2022-03-18 01:34:46.966611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/conditionalevent.cpython-310.pyc
--rw-r--r--   0        0        0      246 2022-03-18 01:34:46.962611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/constants.cpython-310.pyc
--rw-r--r--   0        0        0     2559 2022-03-18 01:34:46.970611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/dormantevent.cpython-310.pyc
--rw-r--r--   0        0        0     3369 2022-03-18 01:34:46.990611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/ftatoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     2654 2022-03-18 01:34:46.970611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/houseevent.cpython-310.pyc
--rw-r--r--   0        0        0     2836 2022-03-18 01:34:46.974611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/inhibitgate.cpython-310.pyc
--rw-r--r--   0        0        0     2400 2022-03-18 01:34:46.974611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/intermediateevent.cpython-310.pyc
--rw-r--r--   0        0        0     3509 2022-03-18 01:34:46.978611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/majorityvotegate.cpython-310.pyc
--rw-r--r--   0        0        0     2534 2022-03-18 01:34:46.978611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/notgate.cpython-310.pyc
--rw-r--r--   0        0        0     3236 2022-03-18 01:34:46.982611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/orgate.cpython-310.pyc
--rw-r--r--   0        0        0     2694 2022-03-18 01:34:46.982611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/seqgate.cpython-310.pyc
--rw-r--r--   0        0        0     2315 2022-03-18 01:34:46.986611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/topevent.cpython-310.pyc
--rw-r--r--   0        0        0     2522 2022-03-18 01:34:46.986611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/transferin.cpython-310.pyc
--rw-r--r--   0        0        0     2603 2022-03-18 01:34:46.986611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/transferout.cpython-310.pyc
--rw-r--r--   0        0        0     2545 2022-03-18 01:34:46.970611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/undevelopedevent.cpython-310.pyc
--rw-r--r--   0        0        0     2714 2022-03-18 01:34:46.990611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/xorgate.cpython-310.pyc
--rw-r--r--   0        0        0     2661 2022-03-18 01:34:46.990611 gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/zeroevent.cpython-310.pyc
--rw-r--r--   0        0        0     2616 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/andgate.py
--rw-r--r--   0        0        0     1951 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/basicevent.py
--rw-r--r--   0        0        0     1517 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/conditionalevent.py
--rw-r--r--   0        0        0       87 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/constants.py
--rw-r--r--   0        0        0     1900 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/dormantevent.py
--rw-r--r--   0        0        0     6880 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/ftatoolbox.py
--rw-r--r--   0        0        0     2048 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/houseevent.py
--rw-r--r--   0        0        0     2674 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/inhibitgate.py
--rw-r--r--   0        0        0     1776 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/intermediateevent.py
--rw-r--r--   0        0        0     3389 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/majorityvotegate.py
--rw-r--r--   0        0        0     1886 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/notgate.py
--rw-r--r--   0        0        0     3254 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/orgate.py
--rw-r--r--   0        0        0     2128 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/seqgate.py
--rw-r--r--   0        0        0     1676 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/topevent.py
--rw-r--r--   0        0        0     1874 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/transferin.py
--rw-r--r--   0        0        0     1921 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/transferout.py
--rw-r--r--   0        0        0     1858 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/undevelopedevent.py
--rw-r--r--   0        0        0     2139 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/xorgate.py
--rw-r--r--   0        0        0     2004 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/fta/zeroevent.py
--rw-r--r--   0        0        0      965 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/modelinglanguage.py
--rw-r--r--   0        0        0     7305 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/raaml.py
--rw-r--r--   0        0        0      481 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/stpa/__init__.py
--rw-r--r--   0        0        0      545 2022-03-18 01:34:46.994611 gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0      689 2022-03-18 01:34:46.998611 gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/connectors.cpython-310.pyc
--rw-r--r--   0        0        0     2365 2022-03-18 01:34:46.994611 gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/controlaction.cpython-310.pyc
--rw-r--r--   0        0        0     2470 2022-03-18 01:34:46.998611 gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/operationalsituation.cpython-310.pyc
--rw-r--r--   0        0        0      565 2022-03-18 01:34:46.998611 gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/relationships.cpython-310.pyc
--rw-r--r--   0        0        0     2931 2022-03-18 01:34:47.002611 gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/stpatoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     2422 2022-03-18 01:34:46.998611 gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/unsafecontrolaction.cpython-310.pyc
--rw-r--r--   0        0        0      423 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/stpa/connectors.py
--rw-r--r--   0        0        0     1752 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/stpa/controlaction.py
--rw-r--r--   0        0        0     1842 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/stpa/operationalsituation.py
--rw-r--r--   0        0        0      292 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/stpa/relationships.py
--rw-r--r--   0        0        0     4949 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/stpa/stpatoolbox.py
--rw-r--r--   0        0        0     1792 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/stpa/unsafecontrolaction.py
--rw-r--r--   0        0        0      547 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/RAAML/toolbox.py
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/__init__.py
--rw-r--r--   0        0        0      136 2022-03-18 01:34:37.926625 gaphor-2.9.1/gaphor/SysML/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0      213 2022-03-18 01:34:38.130625 gaphor-2.9.1/gaphor/SysML/__pycache__/diagramitems.cpython-310.pyc
--rw-r--r--   0        0        0     1581 2022-03-18 01:34:38.118625 gaphor-2.9.1/gaphor/SysML/__pycache__/modelinglanguage.cpython-310.pyc
--rw-r--r--   0        0        0     7867 2022-03-18 01:34:38.122624 gaphor-2.9.1/gaphor/SysML/__pycache__/propertypages.cpython-310.pyc
--rw-r--r--   0        0        0    10895 2022-03-18 01:34:37.930625 gaphor-2.9.1/gaphor/SysML/__pycache__/sysml.cpython-310.pyc
--rw-r--r--   0        0        0     1971 2022-03-18 01:34:38.134625 gaphor-2.9.1/gaphor/SysML/__pycache__/toolbox.cpython-310.pyc
--rw-r--r--   0        0        0      229 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/blocks/__init__.py
--rw-r--r--   0        0        0      421 2022-03-18 01:34:38.094625 gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     4852 2022-03-18 01:34:38.098625 gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/block.cpython-310.pyc
--rw-r--r--   0        0        0     2064 2022-03-18 01:34:38.134625 gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/blockstoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     3152 2022-03-18 01:34:38.098625 gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/connectors.cpython-310.pyc
--rw-r--r--   0        0        0      664 2022-03-18 01:34:38.114625 gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/group.cpython-310.pyc
--rw-r--r--   0        0        0     2929 2022-03-18 01:34:38.110625 gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/property.cpython-310.pyc
--rw-r--r--   0        0        0     4834 2022-03-18 01:34:38.110625 gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/proxyport.cpython-310.pyc
--rw-r--r--   0        0        0     5336 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/blocks/block.py
--rw-r--r--   0        0        0     3450 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/blocks/blockstoolbox.py
--rw-r--r--   0        0        0     2846 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/blocks/connectors.py
--rw-r--r--   0        0        0      536 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/blocks/group.py
--rw-r--r--   0        0        0     2561 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/blocks/property.py
--rw-r--r--   0        0        0     4360 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/blocks/proxyport.py
--rw-r--r--   0        0        0       74 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/diagramitems.py
--rw-r--r--   0        0        0      965 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/modelinglanguage.py
--rw-r--r--   0        0        0    11606 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/propertypages.glade
--rw-r--r--   0        0        0     8133 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/propertypages.py
--rw-r--r--   0        0        0     7685 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/propertypages.ui
--rw-r--r--   0        0        0      382 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/requirements/__init__.py
--rw-r--r--   0        0        0      495 2022-03-18 01:34:38.126624 gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2085 2022-03-18 01:34:38.126624 gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/connectors.cpython-310.pyc
--rw-r--r--   0        0        0     2252 2022-03-18 01:34:38.126624 gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/relationships.cpython-310.pyc
--rw-r--r--   0        0        0     3900 2022-03-18 01:34:38.130625 gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/requirement.cpython-310.pyc
--rw-r--r--   0        0        0     1539 2022-03-18 01:34:38.134625 gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/requirementstoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     1587 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/requirements/connectors.py
--rw-r--r--   0        0        0     1498 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/requirements/relationships.py
--rw-r--r--   0        0        0     4421 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/requirements/requirement.py
--rw-r--r--   0        0        0     2111 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/requirements/requirementstoolbox.py
--rw-r--r--   0        0        0     9055 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/sysml.py
--rw-r--r--   0        0        0     2391 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/SysML/toolbox.py
--rw-r--r--   0        0        0      161 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/__init__.py
--rw-r--r--   0        0        0      299 2022-03-18 01:34:37.646625 gaphor-2.9.1/gaphor/UML/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     1801 2022-03-18 01:34:37.942625 gaphor-2.9.1/gaphor/UML/__pycache__/copypaste.cpython-310.pyc
--rw-r--r--   0        0        0      797 2022-03-18 01:34:37.690625 gaphor-2.9.1/gaphor/UML/__pycache__/deletable.cpython-310.pyc
--rw-r--r--   0        0        0      510 2022-03-18 01:34:37.810625 gaphor-2.9.1/gaphor/UML/__pycache__/diagramitems.cpython-310.pyc
--rw-r--r--   0        0        0      662 2022-03-18 01:34:37.694625 gaphor-2.9.1/gaphor/UML/__pycache__/group.cpython-310.pyc
--rw-r--r--   0        0        0      478 2022-03-18 01:34:37.694625 gaphor-2.9.1/gaphor/UML/__pycache__/iconname.cpython-310.pyc
--rw-r--r--   0        0        0     1579 2022-03-18 01:34:38.074625 gaphor-2.9.1/gaphor/UML/__pycache__/modelinglanguage.cpython-310.pyc
--rw-r--r--   0        0        0    10526 2022-03-18 01:34:37.698625 gaphor-2.9.1/gaphor/UML/__pycache__/recipes.cpython-310.pyc
--rw-r--r--   0        0        0     5460 2022-03-18 01:34:42.006617 gaphor-2.9.1/gaphor/UML/__pycache__/sanitizerservice.cpython-310.pyc
--rw-r--r--   0        0        0     1445 2022-03-18 01:34:38.074625 gaphor-2.9.1/gaphor/UML/__pycache__/toolbox.cpython-310.pyc
--rw-r--r--   0        0        0    42640 2022-03-18 01:34:37.666625 gaphor-2.9.1/gaphor/UML/__pycache__/uml.cpython-310.pyc
--rw-r--r--   0        0        0     5508 2022-03-18 01:34:37.858625 gaphor-2.9.1/gaphor/UML/__pycache__/umlfmt.cpython-310.pyc
--rw-r--r--   0        0        0     6227 2022-03-18 01:34:37.674625 gaphor-2.9.1/gaphor/UML/__pycache__/umllex.cpython-310.pyc
--rw-r--r--   0        0        0     4759 2022-03-18 01:34:37.650625 gaphor-2.9.1/gaphor/UML/__pycache__/umloverrides.cpython-310.pyc
--rw-r--r--   0        0        0      946 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/__init__.py
--rw-r--r--   0        0        0      959 2022-03-18 01:34:37.814625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     3419 2022-03-18 01:34:37.838625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/action.cpython-310.pyc
--rw-r--r--   0        0        0     1060 2022-03-18 01:34:37.814625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionseditors.cpython-310.pyc
--rw-r--r--   0        0        0      715 2022-03-18 01:34:37.822625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionsgroup.cpython-310.pyc
--rw-r--r--   0        0        0     6339 2022-03-18 01:34:37.822625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionspropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     3777 2022-03-18 01:34:38.034625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionstoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     9633 2022-03-18 01:34:37.818625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/activitynodes.cpython-310.pyc
--rw-r--r--   0        0        0      509 2022-03-18 01:34:37.826625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/copypaste.cpython-310.pyc
--rw-r--r--   0        0        0     2690 2022-03-18 01:34:37.838625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/flow.cpython-310.pyc
--rw-r--r--   0        0        0     6220 2022-03-18 01:34:37.834625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/flowconnect.cpython-310.pyc
--rw-r--r--   0        0        0     2649 2022-03-18 01:34:37.826625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/objectnode.cpython-310.pyc
--rw-r--r--   0        0        0     3285 2022-03-18 01:34:37.830625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/partition.cpython-310.pyc
--rw-r--r--   0        0        0     4160 2022-03-18 01:34:37.842625 gaphor-2.9.1/gaphor/UML/actions/__pycache__/partitionpage.cpython-310.pyc
--rw-r--r--   0        0        0     2844 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/action.py
--rw-r--r--   0        0        0      751 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/actionseditors.py
--rw-r--r--   0        0        0      561 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/actionsgroup.py
--rw-r--r--   0        0        0     5406 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/actionspropertypages.py
--rw-r--r--   0        0        0     5796 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/actionstoolbox.py
--rw-r--r--   0        0        0     8762 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/activitynodes.py
--rw-r--r--   0        0        0      297 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/copypaste.py
--rw-r--r--   0        0        0     2168 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/flow.py
--rw-r--r--   0        0        0     8026 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/flowconnect.py
--rw-r--r--   0        0        0     2465 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/objectnode.py
--rw-r--r--   0        0        0     3409 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/partition.py
--rw-r--r--   0        0        0     4414 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/partitionpage.py
--rw-r--r--   0        0        0    11286 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/propertypages.glade
--rw-r--r--   0        0        0     8193 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/actions/propertypages.ui
--rw-r--r--   0        0        0     1156 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/__init__.py
--rw-r--r--   0        0        0     1284 2022-03-18 01:34:37.846625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0    13682 2022-03-18 01:34:37.854625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/association.cpython-310.pyc
--rw-r--r--   0        0        0     6120 2022-03-18 01:34:37.958625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/associationpropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     6562 2022-03-18 01:34:37.846625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/classconnect.cpython-310.pyc
--rw-r--r--   0        0        0     1910 2022-03-18 01:34:37.886625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/classeseditors.cpython-310.pyc
--rw-r--r--   0        0        0    15639 2022-03-18 01:34:37.922625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/classespropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     2885 2022-03-18 01:34:38.038625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/classestoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     3101 2022-03-18 01:34:37.938625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/component.cpython-310.pyc
--rw-r--r--   0        0        0     1237 2022-03-18 01:34:37.986625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/containment.cpython-310.pyc
--rw-r--r--   0        0        0     2655 2022-03-18 01:34:37.986625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/containmentconnect.cpython-310.pyc
--rw-r--r--   0        0        0     1320 2022-03-18 01:34:37.986625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/copypaste.cpython-310.pyc
--rw-r--r--   0        0        0     3291 2022-03-18 01:34:37.926625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/datatype.cpython-310.pyc
--rw-r--r--   0        0        0     4330 2022-03-18 01:34:37.858625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/dependency.cpython-310.pyc
--rw-r--r--   0        0        0     2976 2022-03-18 01:34:37.978625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/dependencypropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     4001 2022-03-18 01:34:37.982625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/enumeration.cpython-310.pyc
--rw-r--r--   0        0        0     3050 2022-03-18 01:34:37.978625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/enumerationpropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     1682 2022-03-18 01:34:37.882625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/generalization.cpython-310.pyc
--rw-r--r--   0        0        0    11874 2022-03-18 01:34:37.866625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/interface.cpython-310.pyc
--rw-r--r--   0        0        0     2786 2022-03-18 01:34:37.990625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/interfaceconnect.cpython-310.pyc
--rw-r--r--   0        0        0     2251 2022-03-18 01:34:37.882625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/interfacerealization.cpython-310.pyc
--rw-r--r--   0        0        0     6498 2022-03-18 01:34:37.870625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/klass.cpython-310.pyc
--rw-r--r--   0        0        0     2548 2022-03-18 01:34:37.990625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/package.cpython-310.pyc
--rw-r--r--   0        0        0     1906 2022-03-18 01:34:37.878625 gaphor-2.9.1/gaphor/UML/classes/__pycache__/stereotype.cpython-310.pyc
--rw-r--r--   0        0        0    15951 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/association.py
--rw-r--r--   0        0        0     6747 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/associationpropertypages.py
--rw-r--r--   0        0        0     7069 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/classconnect.py
--rw-r--r--   0        0        0     1922 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/classeseditors.py
--rw-r--r--   0        0        0    15661 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/classespropertypages.py
--rw-r--r--   0        0        0     4948 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/classestoolbox.py
--rw-r--r--   0        0        0     3046 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/component.py
--rw-r--r--   0        0        0      782 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/containment.py
--rw-r--r--   0        0        0     3279 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/containmentconnect.py
--rw-r--r--   0        0        0     1127 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/copypaste.py
--rw-r--r--   0        0        0     3458 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/datatype.py
--rw-r--r--   0        0        0     3664 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/dependency.py
--rw-r--r--   0        0        0     2570 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/dependencypropertypages.py
--rw-r--r--   0        0        0     4080 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/enumeration.py
--rw-r--r--   0        0        0     2950 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/enumerationpropertypages.py
--rw-r--r--   0        0        0     1020 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/generalization.py
--rw-r--r--   0        0        0    12329 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/interface.py
--rw-r--r--   0        0        0     2490 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/interfaceconnect.py
--rw-r--r--   0        0        0     1585 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/interfacerealization.py
--rw-r--r--   0        0        0     7026 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/klass.py
--rw-r--r--   0        0        0     2098 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/package.py
--rw-r--r--   0        0        0    39298 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/propertypages.glade
--rw-r--r--   0        0        0    32676 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/propertypages.ui
--rw-r--r--   0        0        0     1240 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/classes/stereotype.py
--rw-r--r--   0        0        0     1305 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/copypaste.py
--rw-r--r--   0        0        0      549 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deletable.py
--rw-r--r--   0        0        0      348 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/__init__.py
--rw-r--r--   0        0        0      523 2022-03-18 01:34:37.934625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2875 2022-03-18 01:34:37.950625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/artifact.cpython-310.pyc
--rw-r--r--   0        0        0     8062 2022-03-18 01:34:37.942625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/connector.cpython-310.pyc
--rw-r--r--   0        0        0     5569 2022-03-18 01:34:37.938625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/connectorconnect.cpython-310.pyc
--rw-r--r--   0        0        0      779 2022-03-18 01:34:37.942625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/copypaste.cpython-310.pyc
--rw-r--r--   0        0        0     3258 2022-03-18 01:34:37.946625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/deploymentpropertypage.cpython-310.pyc
--rw-r--r--   0        0        0     1116 2022-03-18 01:34:37.950625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/deploymentsgroup.cpython-310.pyc
--rw-r--r--   0        0        0     1012 2022-03-18 01:34:38.074625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/deploymentstoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     3268 2022-03-18 01:34:37.954625 gaphor-2.9.1/gaphor/UML/deployments/__pycache__/node.cpython-310.pyc
--rw-r--r--   0        0        0     2613 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/artifact.py
--rw-r--r--   0        0        0     7882 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/connector.py
--rw-r--r--   0        0        0     6666 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/connectorconnect.py
--rw-r--r--   0        0        0      502 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/copypaste.py
--rw-r--r--   0        0        0     3389 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/deploymentpropertypage.py
--rw-r--r--   0        0        0      977 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/deploymentsgroup.py
--rw-r--r--   0        0        0     1385 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/deploymentstoolbox.py
--rw-r--r--   0        0        0     3027 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/node.py
--rw-r--r--   0        0        0     3778 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/propertypages.glade
--rw-r--r--   0        0        0     2424 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/deployments/propertypages.ui
--rw-r--r--   0        0        0      382 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/diagramitems.py
--rw-r--r--   0        0        0      549 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/group.py
--rw-r--r--   0        0        0      302 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/iconname.py
--rw-r--r--   0        0        0      509 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/__init__.py
--rw-r--r--   0        0        0      647 2022-03-18 01:34:37.990625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0      846 2022-03-18 01:34:37.994625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/copypaste.cpython-310.pyc
--rw-r--r--   0        0        0     5650 2022-03-18 01:34:37.998625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/executionspecification.cpython-310.pyc
--rw-r--r--   0        0        0     1977 2022-03-18 01:34:38.006625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interaction.cpython-310.pyc
--rw-r--r--   0        0        0     9684 2022-03-18 01:34:37.998625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionsconnect.cpython-310.pyc
--rw-r--r--   0        0        0      709 2022-03-18 01:34:38.010625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionsgroup.cpython-310.pyc
--rw-r--r--   0        0        0     2362 2022-03-18 01:34:38.010625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionspropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     2566 2022-03-18 01:34:38.038625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionstoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     9318 2022-03-18 01:34:38.002625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/lifeline.cpython-310.pyc
--rw-r--r--   0        0        0     6981 2022-03-18 01:34:38.006625 gaphor-2.9.1/gaphor/UML/interactions/__pycache__/message.cpython-310.pyc
--rw-r--r--   0        0        0      630 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/copypaste.py
--rw-r--r--   0        0        0     4813 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/executionspecification.py
--rw-r--r--   0        0        0     1573 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/interaction.py
--rw-r--r--   0        0        0    11713 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/interactionsconnect.py
--rw-r--r--   0        0        0      512 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/interactionsgroup.py
--rw-r--r--   0        0        0     2693 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/interactionspropertypages.py
--rw-r--r--   0        0        0     3031 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/interactionstoolbox.py
--rw-r--r--   0        0        0     8595 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/lifeline.py
--rw-r--r--   0        0        0     7205 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/message.py
--rw-r--r--   0        0        0     1639 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/propertypages.glade
--rw-r--r--   0        0        0     1355 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/interactions/propertypages.ui
--rw-r--r--   0        0        0      990 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/modelinglanguage.py
--rw-r--r--   0        0        0      310 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/__init__.py
--rw-r--r--   0        0        0      471 2022-03-18 01:34:37.958625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     1816 2022-03-18 01:34:37.962625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/extension.cpython-310.pyc
--rw-r--r--   0        0        0     2440 2022-03-18 01:34:37.962625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/extensionconnect.cpython-310.pyc
--rw-r--r--   0        0        0     2414 2022-03-18 01:34:37.966625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/metaclasspropertypage.cpython-310.pyc
--rw-r--r--   0        0        0     1384 2022-03-18 01:34:37.970625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/packageimport.cpython-310.pyc
--rw-r--r--   0        0        0     1400 2022-03-18 01:34:37.966625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/packageimportconnect.cpython-310.pyc
--rw-r--r--   0        0        0     1428 2022-03-18 01:34:38.078625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/profilestoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     3872 2022-03-18 01:34:37.974625 gaphor-2.9.1/gaphor/UML/profiles/__pycache__/stereotypepropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     1177 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/extension.py
--rw-r--r--   0        0        0     3491 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/extensionconnect.py
--rw-r--r--   0        0        0     1834 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/metaclasspropertypage.py
--rw-r--r--   0        0        0      856 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/packageimport.py
--rw-r--r--   0        0        0     1183 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/packageimportconnect.py
--rw-r--r--   0        0        0     1943 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/profilestoolbox.py
--rw-r--r--   0        0        0     5616 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/propertypages.glade
--rw-r--r--   0        0        0     4409 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/propertypages.ui
--rw-r--r--   0        0        0     4700 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/profiles/stereotypepropertypages.py
--rw-r--r--   0        0        0    11709 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/recipes.py
--rw-r--r--   0        0        0     6041 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/sanitizerservice.py
--rw-r--r--   0        0        0     1236 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/__init__.py
--rw-r--r--   0        0        0     1404 2022-03-18 01:34:38.014625 gaphor-2.9.1/gaphor/UML/states/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0      796 2022-03-18 01:34:38.014625 gaphor-2.9.1/gaphor/UML/states/__pycache__/copypaste.cpython-310.pyc
--rw-r--r--   0        0        0     1928 2022-03-18 01:34:38.026625 gaphor-2.9.1/gaphor/UML/states/__pycache__/finalstate.cpython-310.pyc
--rw-r--r--   0        0        0     3708 2022-03-18 01:34:38.014625 gaphor-2.9.1/gaphor/UML/states/__pycache__/propertypages.cpython-310.pyc
--rw-r--r--   0        0        0     2685 2022-03-18 01:34:38.018625 gaphor-2.9.1/gaphor/UML/states/__pycache__/pseudostates.cpython-310.pyc
--rw-r--r--   0        0        0     3351 2022-03-18 01:34:38.022625 gaphor-2.9.1/gaphor/UML/states/__pycache__/state.cpython-310.pyc
--rw-r--r--   0        0        0     2719 2022-03-18 01:34:38.042625 gaphor-2.9.1/gaphor/UML/states/__pycache__/statestoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     1681 2022-03-18 01:34:38.022625 gaphor-2.9.1/gaphor/UML/states/__pycache__/transition.cpython-310.pyc
--rw-r--r--   0        0        0     2901 2022-03-18 01:34:38.018625 gaphor-2.9.1/gaphor/UML/states/__pycache__/vertexconnect.cpython-310.pyc
--rw-r--r--   0        0        0      595 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/copypaste.py
--rw-r--r--   0        0        0     1365 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/finalstate.py
--rw-r--r--   0        0        0     4440 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/propertypages.glade
--rw-r--r--   0        0        0     3488 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/propertypages.py
--rw-r--r--   0        0        0     2973 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/propertypages.ui
--rw-r--r--   0        0        0     2039 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/pseudostates.py
--rw-r--r--   0        0        0     2998 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/state.py
--rw-r--r--   0        0        0     3362 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/statestoolbox.py
--rw-r--r--   0        0        0     1164 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/transition.py
--rw-r--r--   0        0        0     2622 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/states/vertexconnect.py
--rw-r--r--   0        0        0     1531 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/toolbox.py
--rw-r--r--   0        0        0    64347 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/uml.py
--rw-r--r--   0        0        0     5584 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/umlfmt.py
--rw-r--r--   0        0        0     9290 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/umllex.py
--rw-r--r--   0        0        0     4971 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/umloverrides.py
--rw-r--r--   0        0        0      363 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/__init__.py
--rw-r--r--   0        0        0      523 2022-03-18 01:34:38.026625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2375 2022-03-18 01:34:38.034625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/actor.cpython-310.pyc
--rw-r--r--   0        0        0     1535 2022-03-18 01:34:38.026625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/extend.cpython-310.pyc
--rw-r--r--   0        0        0     1541 2022-03-18 01:34:38.030625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/include.cpython-310.pyc
--rw-r--r--   0        0        0     1806 2022-03-18 01:34:38.030625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecase.cpython-310.pyc
--rw-r--r--   0        0        0     1727 2022-03-18 01:34:38.026625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecaseconnect.cpython-310.pyc
--rw-r--r--   0        0        0      671 2022-03-18 01:34:38.030625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecasegroup.cpython-310.pyc
--rw-r--r--   0        0        0     1228 2022-03-18 01:34:38.078625 gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecasetoolbox.cpython-310.pyc
--rw-r--r--   0        0        0     1899 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/actor.py
--rw-r--r--   0        0        0      966 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/extend.py
--rw-r--r--   0        0        0      970 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/include.py
--rw-r--r--   0        0        0     1256 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/usecase.py
--rw-r--r--   0        0        0     1434 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/usecaseconnect.py
--rw-r--r--   0        0        0      533 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/usecasegroup.py
--rw-r--r--   0        0        0     1746 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/UML/usecases/usecasetoolbox.py
--rw-r--r--   0        0        0      738 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/__init__.py
--rw-r--r--   0        0        0       86 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/__main__.py
--rw-r--r--   0        0        0     1294 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/abc.py
--rw-r--r--   0        0        0     1553 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/action.py
--rw-r--r--   0        0        0     7333 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/application.py
--rw-r--r--   0        0        0     1575 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/babel.py
--rw-r--r--   0        0        0      290 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/codegen/__init__.py
--rw-r--r--   0        0        0      323 2022-03-18 01:34:38.214625 gaphor-2.9.1/gaphor/codegen/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0    14568 2022-03-18 01:34:42.550616 gaphor-2.9.1/gaphor/codegen/__pycache__/coder.cpython-310.pyc
--rw-r--r--   0        0        0     2852 2022-03-18 01:34:42.554616 gaphor-2.9.1/gaphor/codegen/__pycache__/override.cpython-310.pyc
--rw-r--r--   0        0        0    14906 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/codegen/coder.py
--rw-r--r--   0        0        0     3229 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/codegen/override.py
--rw-r--r--   0        0        0      311 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/__init__.py
--rw-r--r--   0        0        0      508 2022-03-18 01:34:37.466626 gaphor-2.9.1/gaphor/core/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2039 2022-03-18 01:34:37.466626 gaphor-2.9.1/gaphor/core/__pycache__/eventmanager.cpython-310.pyc
--rw-r--r--   0        0        0     1128 2022-03-18 01:34:37.674625 gaphor-2.9.1/gaphor/core/__pycache__/format.cpython-310.pyc
--rw-r--r--   0        0        0     1540 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/eventmanager.py
--rw-r--r--   0        0        0      780 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/format.py
--rw-r--r--   0        0        0      412 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/__init__.py
--rw-r--r--   0        0        0      651 2022-03-18 01:34:37.526625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     6882 2022-03-18 01:34:37.538625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/collection.cpython-310.pyc
--rw-r--r--   0        0        0     1515 2022-03-18 01:34:37.526625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/coremodel.cpython-310.pyc
--rw-r--r--   0        0        0    16413 2022-03-18 01:34:37.550625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/diagram.cpython-310.pyc
--rw-r--r--   0        0        0     8889 2022-03-18 01:34:37.546625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/element.cpython-310.pyc
--rw-r--r--   0        0        0     7849 2022-03-18 01:34:37.594625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/elementdispatcher.cpython-310.pyc
--rw-r--r--   0        0        0     8949 2022-03-18 01:34:37.590625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/elementfactory.cpython-310.pyc
--rw-r--r--   0        0        0     8372 2022-03-18 01:34:37.538625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/event.cpython-310.pyc
--rw-r--r--   0        0        0     8464 2022-03-18 01:34:37.542626 gaphor-2.9.1/gaphor/core/modeling/__pycache__/listmixins.cpython-310.pyc
--rw-r--r--   0        0        0     2424 2022-03-18 01:34:38.042625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/modelinglanguage.cpython-310.pyc
--rw-r--r--   0        0        0     5282 2022-03-18 01:34:37.554625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/presentation.cpython-310.pyc
--rw-r--r--   0        0        0    27932 2022-03-18 01:34:37.534625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/properties.cpython-310.pyc
--rw-r--r--   0        0        0     2561 2022-03-18 01:34:37.554625 gaphor-2.9.1/gaphor/core/modeling/__pycache__/stylesheet.cpython-310.pyc
--rw-r--r--   0        0        0     4730 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/collection.py
--rw-r--r--   0        0        0     2230 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/coremodel.py
--rw-r--r--   0        0        0    13175 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/diagram.py
--rw-r--r--   0        0        0     6378 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/element.py
--rw-r--r--   0        0        0     9372 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/elementdispatcher.py
--rw-r--r--   0        0        0     7511 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/elementfactory.py
--rw-r--r--   0        0        0     7232 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/event.py
--rw-r--r--   0        0        0     7735 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/listmixins.py
--rw-r--r--   0        0        0     1341 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/modelinglanguage.py
--rw-r--r--   0        0        0     4734 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/presentation.py
--rw-r--r--   0        0        0    28743 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/properties.py
--rw-r--r--   0        0        0     2007 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/modeling/stylesheet.py
--rw-r--r--   0        0        0     3398 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/styling/__init__.py
--rw-r--r--   0        0        0     4639 2022-03-18 01:34:37.558625 gaphor-2.9.1/gaphor/core/styling/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     6092 2022-03-18 01:34:37.570625 gaphor-2.9.1/gaphor/core/styling/__pycache__/declarations.cpython-310.pyc
--rw-r--r--   0        0        0    10847 2022-03-18 01:34:37.582625 gaphor-2.9.1/gaphor/core/styling/__pycache__/parser.cpython-310.pyc
--rw-r--r--   0        0        0     1779 2022-03-18 01:34:37.574625 gaphor-2.9.1/gaphor/core/styling/__pycache__/properties.cpython-310.pyc
--rw-r--r--   0        0        0     6753 2022-03-18 01:34:37.582625 gaphor-2.9.1/gaphor/core/styling/__pycache__/selectors.cpython-310.pyc
--rw-r--r--   0        0        0     5163 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/styling/declarations.py
--rw-r--r--   0        0        0    11597 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/styling/parser.py
--rw-r--r--   0        0        0     1454 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/styling/properties.py
--rw-r--r--   0        0        0     4122 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/core/styling/selectors.py
--rw-r--r--   0        0        0      252 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/__init__.py
--rw-r--r--   0        0        0      396 2022-03-18 01:34:37.510625 gaphor-2.9.1/gaphor/diagram/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0    12472 2022-03-18 01:34:37.598625 gaphor-2.9.1/gaphor/diagram/__pycache__/connectors.cpython-310.pyc
--rw-r--r--   0        0        0     7005 2022-03-18 01:34:37.602625 gaphor-2.9.1/gaphor/diagram/__pycache__/copypaste.cpython-310.pyc
--rw-r--r--   0        0        0      438 2022-03-18 01:34:37.690625 gaphor-2.9.1/gaphor/diagram/__pycache__/deletable.cpython-310.pyc
--rw-r--r--   0        0        0     4220 2022-03-18 01:34:37.622625 gaphor-2.9.1/gaphor/diagram/__pycache__/diagramtoolbox.cpython-310.pyc
--rw-r--r--   0        0        0      580 2022-03-18 01:34:37.702625 gaphor-2.9.1/gaphor/diagram/__pycache__/event.cpython-310.pyc
--rw-r--r--   0        0        0     2232 2022-03-18 01:34:44.046613 gaphor-2.9.1/gaphor/diagram/__pycache__/export.cpython-310.pyc
--rw-r--r--   0        0        0     2514 2022-03-18 01:34:37.646625 gaphor-2.9.1/gaphor/diagram/__pycache__/group.cpython-310.pyc
--rw-r--r--   0        0        0     1801 2022-03-18 01:34:37.922625 gaphor-2.9.1/gaphor/diagram/__pycache__/hoversupport.cpython-310.pyc
--rw-r--r--   0        0        0      724 2022-03-18 01:34:37.694625 gaphor-2.9.1/gaphor/diagram/__pycache__/iconname.cpython-310.pyc
--rw-r--r--   0        0        0     3382 2022-03-18 01:34:37.634625 gaphor-2.9.1/gaphor/diagram/__pycache__/inlineeditors.cpython-310.pyc
--rw-r--r--   0        0        0     3105 2022-03-18 01:34:37.714625 gaphor-2.9.1/gaphor/diagram/__pycache__/painter.cpython-310.pyc
--rw-r--r--   0        0        0    13002 2022-03-18 01:34:37.606625 gaphor-2.9.1/gaphor/diagram/__pycache__/presentation.cpython-310.pyc
--rw-r--r--   0        0        0    11944 2022-03-18 01:34:37.642625 gaphor-2.9.1/gaphor/diagram/__pycache__/propertypages.cpython-310.pyc
--rw-r--r--   0        0        0     1490 2022-03-18 01:34:37.714625 gaphor-2.9.1/gaphor/diagram/__pycache__/selection.cpython-310.pyc
--rw-r--r--   0        0        0    11181 2022-03-18 01:34:37.610625 gaphor-2.9.1/gaphor/diagram/__pycache__/shapes.cpython-310.pyc
--rw-r--r--   0        0        0     1365 2022-03-18 01:34:37.630625 gaphor-2.9.1/gaphor/diagram/__pycache__/support.cpython-310.pyc
--rw-r--r--   0        0        0     6499 2022-03-18 01:34:37.614625 gaphor-2.9.1/gaphor/diagram/__pycache__/text.cpython-310.pyc
--rw-r--r--   0        0        0    13006 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/connectors.py
--rw-r--r--   0        0        0     6218 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/copypaste.py
--rw-r--r--   0        0        0      217 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/deletable.py
--rw-r--r--   0        0        0     4230 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/diagramtoolbox.py
--rw-r--r--   0        0        0      127 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/event.py
--rw-r--r--   0        0        0     2002 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/export.py
--rw-r--r--   0        0        0      339 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/general/__init__.py
--rw-r--r--   0        0        0      539 2022-03-18 01:34:37.626625 gaphor-2.9.1/gaphor/diagram/general/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     1912 2022-03-18 01:34:37.630625 gaphor-2.9.1/gaphor/diagram/general/__pycache__/comment.cpython-310.pyc
--rw-r--r--   0        0        0     1081 2022-03-18 01:34:37.630625 gaphor-2.9.1/gaphor/diagram/general/__pycache__/commentline.cpython-310.pyc
--rw-r--r--   0        0        0     3927 2022-03-18 01:34:37.626625 gaphor-2.9.1/gaphor/diagram/general/__pycache__/connectors.cpython-310.pyc
--rw-r--r--   0        0        0     1370 2022-03-18 01:34:37.634625 gaphor-2.9.1/gaphor/diagram/general/__pycache__/generaleditors.cpython-310.pyc
--rw-r--r--   0        0        0     1809 2022-03-18 01:34:37.638625 gaphor-2.9.1/gaphor/diagram/general/__pycache__/generalpropertypages.cpython-310.pyc
--rw-r--r--   0        0        0     2039 2022-03-18 01:34:37.646625 gaphor-2.9.1/gaphor/diagram/general/__pycache__/simpleitem.cpython-310.pyc
--rw-r--r--   0        0        0     1430 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/general/comment.py
--rw-r--r--   0        0        0      622 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/general/commentline.py
--rw-r--r--   0        0        0     5759 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/general/connectors.py
--rw-r--r--   0        0        0     1126 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/general/generaleditors.py
--rw-r--r--   0        0        0     1416 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/general/generalpropertypages.py
--rw-r--r--   0        0        0     1251 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/general/simpleitem.py
--rw-r--r--   0        0        0     1911 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/group.py
--rw-r--r--   0        0        0     1606 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/hoversupport.py
--rw-r--r--   0        0        0      458 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/iconname.py
--rw-r--r--   0        0        0     2994 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/inlineeditors.py
--rw-r--r--   0        0        0     2841 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/painter.py
--rw-r--r--   0        0        0    11130 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/presentation.py
--rw-r--r--   0        0        0     5048 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/propertypages.glade
--rw-r--r--   0        0        0    10117 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/propertypages.py
--rw-r--r--   0        0        0     3797 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/propertypages.ui
--rw-r--r--   0        0        0      930 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/selection.py
--rw-r--r--   0        0        0    11144 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/shapes.py
--rw-r--r--   0        0        0      985 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/support.py
--rw-r--r--   0        0        0     7647 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/text.py
--rw-r--r--   0        0        0     2482 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/__init__.py
--rw-r--r--   0        0        0     2180 2022-03-18 01:34:37.510625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     4929 2022-03-18 01:34:37.522626 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/connector.cpython-310.pyc
--rw-r--r--   0        0        0     1007 2022-03-18 01:34:37.622625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/dnd.cpython-310.pyc
--rw-r--r--   0        0        0     4037 2022-03-18 01:34:37.706625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/dropzone.cpython-310.pyc
--rw-r--r--   0        0        0     2201 2022-03-18 01:34:37.618625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/grayout.cpython-310.pyc
--rw-r--r--   0        0        0     3729 2022-03-18 01:34:37.706625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/magnet.cpython-310.pyc
--rw-r--r--   0        0        0     3949 2022-03-18 01:34:37.702625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/placement.cpython-310.pyc
--rw-r--r--   0        0        0     1960 2022-03-18 01:34:37.622625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/segment.cpython-310.pyc
--rw-r--r--   0        0        0     1421 2022-03-18 01:34:37.710625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/shortcut.cpython-310.pyc
--rw-r--r--   0        0        0     1199 2022-03-18 01:34:37.710625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/textedit.cpython-310.pyc
--rw-r--r--   0        0        0     1522 2022-03-18 01:34:37.710625 gaphor-2.9.1/gaphor/diagram/tools/__pycache__/txtool.cpython-310.pyc
--rw-r--r--   0        0        0     5213 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/connector.py
--rw-r--r--   0        0        0      760 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/dnd.py
--rw-r--r--   0        0        0     4397 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/dropzone.py
--rw-r--r--   0        0        0     1572 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/grayout.py
--rw-r--r--   0        0        0     3871 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/magnet.py
--rw-r--r--   0        0        0     3988 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/placement.py
--rw-r--r--   0        0        0     1381 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/segment.py
--rw-r--r--   0        0        0     1231 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/shortcut.py
--rw-r--r--   0        0        0     1078 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/textedit.py
--rw-r--r--   0        0        0      891 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/diagram/tools/txtool.py
--rw-r--r--   0        0        0     2221 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/entrypoint.py
--rw-r--r--   0        0        0     2894 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/event.py
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/extensions/__init__.py
--rw-r--r--   0        0        0      141 2022-03-18 01:34:44.586612 gaphor-2.9.1/gaphor/extensions/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     4143 2022-03-18 01:34:44.586612 gaphor-2.9.1/gaphor/extensions/__pycache__/sphinx.cpython-310.pyc
--rw-r--r--   0        0        0     4048 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/extensions/sphinx.py
--rw-r--r--   0        0        0     1109 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/i18n.py
--rw-r--r--   0        0        0      217 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/locale/README
--rw-r--r--   0        0        0      431 2022-03-18 01:34:28.746635 gaphor-2.9.1/gaphor/locale/bn/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0     3183 2022-03-18 01:34:28.406635 gaphor-2.9.1/gaphor/locale/ca/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    17807 2022-03-18 01:34:27.722635 gaphor-2.9.1/gaphor/locale/de/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    33749 2022-03-18 01:34:31.842634 gaphor-2.9.1/gaphor/locale/es/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    26405 2022-03-18 01:34:29.110636 gaphor-2.9.1/gaphor/locale/fi/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0     6020 2022-03-18 01:34:31.470635 gaphor-2.9.1/gaphor/locale/fr/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    19230 2022-03-18 01:34:32.934632 gaphor-2.9.1/gaphor/locale/gl/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    32892 2022-03-18 01:34:29.942636 gaphor-2.9.1/gaphor/locale/hr/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    35166 2022-03-18 01:34:31.046635 gaphor-2.9.1/gaphor/locale/hu/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0     5691 2022-03-18 01:34:30.302636 gaphor-2.9.1/gaphor/locale/it/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    11162 2022-03-18 01:34:33.754631 gaphor-2.9.1/gaphor/locale/ja/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    13406 2022-03-18 01:34:33.322632 gaphor-2.9.1/gaphor/locale/ko/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    20605 2022-03-18 01:34:29.522636 gaphor-2.9.1/gaphor/locale/nl/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0    15309 2022-03-18 01:34:30.674636 gaphor-2.9.1/gaphor/locale/pt_BR/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0     4135 2022-03-18 01:34:28.070635 gaphor-2.9.1/gaphor/locale/ru/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0     1022 2022-03-18 01:34:32.194634 gaphor-2.9.1/gaphor/locale/sv/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0     8809 2022-03-18 01:34:32.554633 gaphor-2.9.1/gaphor/locale/zh_Hans/LC_MESSAGES/gaphor.mo
--rw-r--r--   0        0        0      605 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/__init__.py
--rw-r--r--   0        0        0      751 2022-03-18 01:34:44.638612 gaphor-2.9.1/gaphor/plugins/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/console/__init__.py
--rw-r--r--   0        0        0      146 2022-03-18 01:34:44.638612 gaphor-2.9.1/gaphor/plugins/console/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0    10345 2022-03-18 01:34:44.702612 gaphor-2.9.1/gaphor/plugins/console/__pycache__/console.cpython-310.pyc
--rw-r--r--   0        0        0     3033 2022-03-18 01:34:44.810612 gaphor-2.9.1/gaphor/plugins/console/__pycache__/consolewindow.cpython-310.pyc
--rw-r--r--   0        0        0     9940 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/console/console.py
--rw-r--r--   0        0        0     2702 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/console/consolewindow.py
--rw-r--r--   0        0        0     2247 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/diagramexport/__init__.py
--rw-r--r--   0        0        0     2316 2022-03-18 01:34:46.682611 gaphor-2.9.1/gaphor/plugins/diagramexport/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     3001 2022-03-18 01:34:46.686611 gaphor-2.9.1/gaphor/plugins/diagramexport/__pycache__/gaphorconvert.cpython-310.pyc
--rwxr-xr-x   0        0        0     3672 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/diagramexport/gaphorconvert.py
--rw-r--r--   0        0        0     1479 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/xmiexport/__init__.py
--rw-r--r--   0        0        0     1782 2022-03-18 01:34:44.850611 gaphor-2.9.1/gaphor/plugins/xmiexport/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     6968 2022-03-18 01:34:44.854611 gaphor-2.9.1/gaphor/plugins/xmiexport/__pycache__/exportmodel.cpython-310.pyc
--rw-r--r--   0        0        0     8695 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/plugins/xmiexport/exportmodel.py
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/py.typed
--rw-r--r--   0        0        0        0 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/__init__.py
--rw-r--r--   0        0        0      139 2022-03-18 01:34:37.474625 gaphor-2.9.1/gaphor/services/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2842 2022-03-18 01:34:37.474625 gaphor-2.9.1/gaphor/services/__pycache__/componentregistry.cpython-310.pyc
--rw-r--r--   0        0        0     4928 2022-03-18 01:34:44.930611 gaphor-2.9.1/gaphor/services/__pycache__/copyservice.cpython-310.pyc
--rw-r--r--   0        0        0     3985 2022-03-18 01:34:44.602612 gaphor-2.9.1/gaphor/services/__pycache__/modelinglanguage.cpython-310.pyc
--rw-r--r--   0        0        0     5505 2022-03-18 01:34:44.602612 gaphor-2.9.1/gaphor/services/__pycache__/properties.cpython-310.pyc
--rw-r--r--   0        0        0    14316 2022-03-18 01:34:38.318624 gaphor-2.9.1/gaphor/services/__pycache__/undomanager.cpython-310.pyc
--rw-r--r--   0        0        0     1568 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/componentregistry.py
--rw-r--r--   0        0        0     4817 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/copyservice.py
--rw-r--r--   0        0        0     1407 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/helpservice/__init__.py
--rw-r--r--   0        0        0     1862 2022-03-18 01:34:48.110610 gaphor-2.9.1/gaphor/services/helpservice/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     2288 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/helpservice/about.ui
--rw-r--r--   0        0        0     8276 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/helpservice/shortcuts.ui
--rw-r--r--   0        0        0     3107 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/modelinglanguage.py
--rw-r--r--   0        0        0     4795 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/properties.py
--rw-r--r--   0        0        0    14918 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/services/undomanager.py
--rw-r--r--   0        0        0       61 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/storage/__init__.py
--rw-r--r--   0        0        0      204 2022-03-18 01:34:38.046625 gaphor-2.9.1/gaphor/storage/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0    11942 2022-03-18 01:34:38.054625 gaphor-2.9.1/gaphor/storage/__pycache__/parser.cpython-310.pyc
--rw-r--r--   0        0        0    10220 2022-03-18 01:34:38.050625 gaphor-2.9.1/gaphor/storage/__pycache__/storage.cpython-310.pyc
--rw-r--r--   0        0        0     3039 2022-03-18 01:34:38.058625 gaphor-2.9.1/gaphor/storage/__pycache__/upgrade_canvasitem.cpython-310.pyc
--rw-r--r--   0        0        0     4802 2022-03-18 01:34:38.062625 gaphor-2.9.1/gaphor/storage/__pycache__/xmlwriter.cpython-310.pyc
--rw-r--r--   0        0        0    12167 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/storage/parser.py
--rw-r--r--   0        0        0    12972 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/storage/storage.py
--rw-r--r--   0        0        0     3827 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/storage/upgrade_canvasitem.py
--rw-r--r--   0        0        0     4707 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/storage/xmlwriter.py
--rw-r--r--   0        0        0      564 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/templates/blank.gaphor
--rw-r--r--   0        0        0     1933 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/templates/c4model.gaphor
--rw-r--r--   0        0        0    24556 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/templates/raaml.gaphor
--rw-r--r--   0        0        0    79653 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/templates/sysml.gaphor
--rw-r--r--   0        0        0    57894 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/templates/uml.gaphor
--rw-r--r--   0        0        0     5025 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/transaction.py
--rw-r--r--   0        0        0     5883 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/__init__.py
--rw-r--r--   0        0        0     5494 2022-03-18 01:34:37.302626 gaphor-2.9.1/gaphor/ui/__pycache__/__init__.cpython-310.pyc
--rw-r--r--   0        0        0     1130 2022-03-18 01:34:44.810612 gaphor-2.9.1/gaphor/ui/__pycache__/abc.cpython-310.pyc
--rw-r--r--   0        0        0     5144 2022-03-18 01:34:37.478626 gaphor-2.9.1/gaphor/ui/__pycache__/actiongroup.cpython-310.pyc
--rw-r--r--   0        0        0     2006 2022-03-18 01:35:12.342628 gaphor-2.9.1/gaphor/ui/__pycache__/appfilemanager.cpython-310.pyc
--rw-r--r--   0        0        0    10609 2022-03-18 01:34:46.138611 gaphor-2.9.1/gaphor/ui/__pycache__/diagrampage.cpython-310.pyc
--rw-r--r--   0        0        0    11691 2022-03-18 01:34:46.298611 gaphor-2.9.1/gaphor/ui/__pycache__/diagrams.cpython-310.pyc
--rw-r--r--   0        0        0    11505 2022-03-18 01:34:46.154611 gaphor-2.9.1/gaphor/ui/__pycache__/elementeditor.cpython-310.pyc
--rw-r--r--   0        0        0     1300 2022-03-18 01:34:46.626611 gaphor-2.9.1/gaphor/ui/__pycache__/errorhandler.cpython-310.pyc
--rw-r--r--   0        0        0     1441 2022-03-18 01:34:44.934611 gaphor-2.9.1/gaphor/ui/__pycache__/event.cpython-310.pyc
--rw-r--r--   0        0        0     2175 2022-03-18 01:34:44.854611 gaphor-2.9.1/gaphor/ui/__pycache__/filedialog.cpython-310.pyc
--rw-r--r--   0        0        0     9515 2022-03-18 01:34:46.626611 gaphor-2.9.1/gaphor/ui/__pycache__/filemanager.cpython-310.pyc
--rw-r--r--   0        0        0     6468 2022-03-18 01:34:46.174611 gaphor-2.9.1/gaphor/ui/__pycache__/greeter.cpython-310.pyc
--rw-r--r--   0        0        0     3787 2022-03-18 01:34:46.390611 gaphor-2.9.1/gaphor/ui/__pycache__/layout.cpython-310.pyc
--rw-r--r--   0        0        0      955 2022-03-18 01:34:37.482626 gaphor-2.9.1/gaphor/ui/__pycache__/macosshim.cpython-310.pyc
--rw-r--r--   0        0        0     8493 2022-03-18 01:34:46.386611 gaphor-2.9.1/gaphor/ui/__pycache__/mainwindow.cpython-310.pyc
--rw-r--r--   0        0        0     1527 2022-03-18 01:34:44.806611 gaphor-2.9.1/gaphor/ui/__pycache__/menufragment.cpython-310.pyc
--rw-r--r--   0        0        0    10671 2022-03-18 01:34:46.382611 gaphor-2.9.1/gaphor/ui/__pycache__/namespace.cpython-310.pyc
--rw-r--r--   0        0        0     9654 2022-03-18 01:34:46.394611 gaphor-2.9.1/gaphor/ui/__pycache__/namespacemodel.cpython-310.pyc
--rw-r--r--   0        0        0     4425 2022-03-18 01:34:46.402611 gaphor-2.9.1/gaphor/ui/__pycache__/namespaceview.cpython-310.pyc
--rw-r--r--   0        0        0     1353 2022-03-18 01:34:46.390611 gaphor-2.9.1/gaphor/ui/__pycache__/notification.cpython-310.pyc
--rw-r--r--   0        0        0     1515 2022-03-18 01:35:12.342628 gaphor-2.9.1/gaphor/ui/__pycache__/questiondialog.cpython-310.pyc
--rw-r--r--   0        0        0     1896 2022-03-18 01:34:46.526611 gaphor-2.9.1/gaphor/ui/__pycache__/recentfiles.cpython-310.pyc
--rw-r--r--   0        0        0     4230 2022-03-18 01:34:46.534611 gaphor-2.9.1/gaphor/ui/__pycache__/statuswindow.cpython-310.pyc
--rw-r--r--   0        0        0     1852 2022-03-18 01:34:38.402624 gaphor-2.9.1/gaphor/ui/__pycache__/styling.cpython-310.pyc
--rw-r--r--   0        0        0    10477 2022-03-18 01:34:46.306611 gaphor-2.9.1/gaphor/ui/__pycache__/toolbox.cpython-310.pyc
--rw-r--r--   0        0        0      687 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/abc.py
--rw-r--r--   0        0        0     5764 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/actiongroup.py
--rw-r--r--   0        0        0     1794 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/appfilemanager.py
--rw-r--r--   0        0        0    13061 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/diagrampage.py
--rw-r--r--   0        0        0    12665 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/diagrams.py
--rw-r--r--   0        0        0    18174 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/elementeditor.glade
--rw-r--r--   0        0        0    11364 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/elementeditor.py
--rw-r--r--   0        0        0    13309 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/elementeditor.ui
--rw-r--r--   0        0        0     1243 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/errorhandler.py
--rw-r--r--   0        0        0      614 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/event.py
--rw-r--r--   0        0        0     2358 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/filedialog.py
--rw-r--r--   0        0        0    10526 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/filemanager.py
--rw-r--r--   0        0        0     1002 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/greeter-model-template.glade
--rw-r--r--   0        0        0     1029 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/greeter-model-template.ui
--rw-r--r--   0        0        0     2466 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/greeter-recent-file.glade
--rw-r--r--   0        0        0     1925 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/greeter-recent-file.ui
--rw-r--r--   0        0        0     6053 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/greeter.glade
--rw-r--r--   0        0        0     6788 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/greeter.py
--rw-r--r--   0        0        0     5994 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/greeter.ui
--rw-r--r--   0        0        0     2214 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/Makefile
--rw-r--r--   0        0        0     2716 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-abstract-operational-situation-symbolic.svg
--rw-r--r--   0        0        0     1677 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-accept-event-action-symbolic.svg
--rw-r--r--   0        0        0     1979 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-action-symbolic.svg
--rw-r--r--   0        0        0     2220 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-final-node-symbolic.svg
--rw-r--r--   0        0        0     2185 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-partition-symbolic.svg
--rw-r--r--   0        0        0     2978 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-symbolic.svg
--rw-r--r--   0        0        0     2825 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actor-symbolic.svg
--rw-r--r--   0        0        0     1892 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actuator-symbolic.svg
--rw-r--r--   0        0        0     2772 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-and-symbolic.svg
--rw-r--r--   0        0        0     2506 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-artifact-symbolic.svg
--rw-r--r--   0        0        0     2611 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-association-symbolic.svg
--rw-r--r--   0        0        0     1659 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-basic-event-symbolic.svg
--rw-r--r--   0        0        0     2369 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-behavior-execution-specification-symbolic.svg
--rw-r--r--   0        0        0     2671 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-block-symbolic.svg
--rw-r--r--   0        0        0     1603 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-box-symbolic.svg
--rw-r--r--   0        0        0     2924 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-component-symbolic.svg
--rw-r--r--   0        0        0     2659 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-container-symbolic.svg
--rw-r--r--   0        0        0     4054 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-database-symbolic.svg
--rw-r--r--   0        0        0     3418 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-person-symbolic.svg
--rw-r--r--   0        0        0     4448 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-software-system-symbolic.svg
--rw-r--r--   0        0        0     1934 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-class-symbolic.svg
--rw-r--r--   0        0        0     1796 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-line-symbolic.svg
--rw-r--r--   0        0        0     1833 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-symbolic.svg
--rw-r--r--   0        0        0     3503 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-component-symbolic.svg
--rw-r--r--   0        0        0     2651 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-composite-association-symbolic.svg
--rw-r--r--   0        0        0     1881 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-conditional-event-symbolic.svg
--rw-r--r--   0        0        0     2508 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-connector-symbolic.svg
--rw-r--r--   0        0        0     1261 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-constraint-symbolic.svg
--rw-r--r--   0        0        0     2381 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-containment-symbolic.svg
--rw-r--r--   0        0        0     2679 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-action-symbolic.svg
--rw-r--r--   0        0        0     2313 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-flow-symbolic.svg
--rw-r--r--   0        0        0     3334 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-structure-symbolic.svg
--rw-r--r--   0        0        0     2866 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controlled-process-symbolic.svg
--rw-r--r--   0        0        0     2276 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controller-symbolic.svg
--rw-r--r--   0        0        0     2435 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-data-type-symbolic.svg
--rw-r--r--   0        0        0     1682 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-decision-node-symbolic.svg
--rw-r--r--   0        0        0     3060 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dependency-symbolic.svg
--rw-r--r--   0        0        0     3370 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-derive-symbolic.svg
--rw-r--r--   0        0        0     3694 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-device-symbolic.svg
--rw-r--r--   0        0        0     2695 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-diagram-symbolic.svg
--rw-r--r--   0        0        0     2239 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dormant-event-symbolic.svg
--rw-r--r--   0        0        0     1898 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-ellipse-symbolic.svg
--rw-r--r--   0        0        0     2268 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-enumeration-symbolic.svg
--rw-r--r--   0        0        0     2363 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-execution-specification-symbolic.svg
--rw-r--r--   0        0        0     3065 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extend-symbolic.svg
--rw-r--r--   0        0        0     1678 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extension-symbolic.svg
--rw-r--r--   0        0        0     2234 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-final-state-symbolic.svg
--rw-r--r--   0        0        0     2201 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-flow-final-node-symbolic.svg
--rw-r--r--   0        0        0     2011 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-fork-node-symbolic.svg
--rw-r--r--   0        0        0     1968 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-generalization-symbolic.svg
--rw-r--r--   0        0        0     1855 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-hazard-symbolic.svg
--rw-r--r--   0        0        0     1524 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-house-event-symbolic.svg
--rw-r--r--   0        0        0     2866 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-import-symbolic.svg
--rw-r--r--   0        0        0     2801 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-include-symbolic.svg
--rw-r--r--   0        0        0     3715 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-information-flow-symbolic.svg
--rw-r--r--   0        0        0     2975 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-inhibit-symbolic.svg
--rw-r--r--   0        0        0     1215 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-node-symbolic.svg
--rw-r--r--   0        0        0     1223 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-pseudostate-symbolic.svg
--rw-r--r--   0        0        0     2525 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interaction-symbolic.svg
--rw-r--r--   0        0        0     2218 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-realization-symbolic.svg
--rw-r--r--   0        0        0     2164 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-symbolic.svg
--rw-r--r--   0        0        0     2279 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-intermediate-event-symbolic.svg
--rw-r--r--   0        0        0     1786 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-item-flow-symbolic.svg
--rw-r--r--   0        0        0     2029 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-join-node-symbolic.svg
--rw-r--r--   0        0        0     2342 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-lifeline-symbolic.svg
--rw-r--r--   0        0        0     1234 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-line-symbolic.svg
--rw-r--r--   0        0        0     1789 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-loss-symbolic.svg
--rw-r--r--   0        0        0     2207 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-magnet-symbolic.svg
--rw-r--r--   0        0        0     3286 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-majority_vote-symbolic.svg
--rw-r--r--   0        0        0     2365 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-message-symbolic.svg
--rw-r--r--   0        0        0     2435 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-metaclass-symbolic.svg
--rw-r--r--   0        0        0     2993 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-new-diagram-symbolic.svg
--rw-r--r--   0        0        0     2922 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-node-symbolic.svg
--rw-r--r--   0        0        0     1703 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-not-symbolic.svg
--rw-r--r--   0        0        0     2357 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-flow-symbolic.svg
--rw-r--r--   0        0        0     1823 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-node-symbolic.svg
--rw-r--r--   0        0        0     2590 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-operational-situation-symbolic.svg
--rw-r--r--   0        0        0     2120 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-or-symbolic.svg
--rw-r--r--   0        0        0     2381 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-package-symbolic.svg
--rw-r--r--   0        0        0     1908 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pointer-symbolic.svg
--rw-r--r--   0        0        0     2985 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-primitive-symbolic.svg
--rw-r--r--   0        0        0     4242 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-profile-symbolic.svg
--rw-r--r--   0        0        0     2360 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-property-symbolic.svg
--rw-r--r--   0        0        0     1978 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-proxyport-symbolic.svg
--rw-r--r--   0        0        0     2542 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pseudostate-symbolic.svg
--rw-r--r--   0        0        0     2783 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-realization-symbolic.svg
--rw-r--r--   0        0        0     3379 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-refine-symbolic.svg
--rw-r--r--   0        0        0     2045 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-reflexive-message-symbolic.svg
--rw-r--r--   0        0        0     1499 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-region-symbolic.svg
--rw-r--r--   0        0        0     3353 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-relevant-to-symbolic.svg
--rw-r--r--   0        0        0     2354 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-requirement-symbolic.svg
--rw-r--r--   0        0        0     3980 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-satisfy-symbolic.svg
--rw-r--r--   0        0        0     1740 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-send-signal-action-symbolic.svg
--rw-r--r--   0        0        0     3326 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-seq-symbolic.svg
--rw-r--r--   0        0        0     2897 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-shared-association-symbolic.svg
--rw-r--r--   0        0        0     2569 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-situation-symbolic.svg
--rw-r--r--   0        0        0     2641 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-machine-symbolic.svg
--rw-r--r--   0        0        0     1443 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-symbolic.svg
--rw-r--r--   0        0        0     3656 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-stereotype-symbolic.svg
--rw-r--r--   0        0        0     2226 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-top-event-symbolic.svg
--rw-r--r--   0        0        0     3171 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-trace-symbolic.svg
--rw-r--r--   0        0        0     1392 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-in-symbolic.svg
--rw-r--r--   0        0        0     1776 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-out-symbolic.svg
--rw-r--r--   0        0        0     1662 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transition-symbolic.svg
--rw-r--r--   0        0        0     1542 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-undeveloped-event-symbolic.svg
--rw-r--r--   0        0        0     2421 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-unsafe-control-action-symbolic.svg
--rw-r--r--   0        0        0     2666 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-usage-symbolic.svg
--rw-r--r--   0        0        0     2304 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-use-case-symbolic.svg
--rw-r--r--   0        0        0     2205 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-value-type-symbolic.svg
--rw-r--r--   0        0        0     3131 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-verify-symbolic.svg
--rw-r--r--   0        0        0     2116 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-view-editor-symbolic.svg
--rw-r--r--   0        0        0     4066 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-xor-symbolic.svg
--rw-r--r--   0        0        0     2342 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-zero-event-symbolic.svg
--rw-r--r--   0        0        0     6198 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/apps/org.gaphor.Gaphor.svg
--rw-r--r--   0        0        0     3217 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/C4Model.svg
--rw-r--r--   0        0        0    39395 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/RAAML.svg
--rw-r--r--   0        0        0     6459 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/SysML.svg
--rw-r--r--   0        0        0     3846 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/UML.svg
--rw-r--r--   0        0        0   263403 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/icons/stensil.svg
--rw-r--r--   0        0        0     4052 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/layout.py
--rw-r--r--   0        0        0      455 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/layout.xml
--rw-r--r--   0        0        0      836 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/macosshim.py
--rw-r--r--   0        0        0     8211 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/mainwindow.glade
--rw-r--r--   0        0        0     9761 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/mainwindow.py
--rw-r--r--   0        0        0     3896 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/mainwindow.ui
--rw-r--r--   0        0        0      837 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/menufragment.py
--rw-r--r--   0        0        0    12389 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/namespace.py
--rw-r--r--   0        0        0    10409 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/namespacemodel.py
--rw-r--r--   0        0        0     5541 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/namespaceview.py
--rw-r--r--   0        0        0      977 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/notification.py
--rw-r--r--   0        0        0     1087 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/placement-icon-base.png
--rw-r--r--   0        0        0     1082 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/questiondialog.py
--rw-r--r--   0        0        0     1470 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/recentfiles.py
--rw-r--r--   0        0        0     4261 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/statuswindow.py
--rw-r--r--   0        0        0      151 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/styling-gtk3.css
--rw-r--r--   0        0        0       98 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/styling-gtk4.css
--rw-r--r--   0        0        0     1023 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/styling.css
--rw-r--r--   0        0        0     1800 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/styling.py
--rw-r--r--   0        0        0    12140 2022-03-18 01:28:35.000000 gaphor-2.9.1/gaphor/ui/toolbox.py
--rw-r--r--   0        0        0     7936 2022-03-18 01:28:35.000000 gaphor-2.9.1/pyproject.toml
--rw-r--r--   0        0        0    41854 2022-03-18 01:37:04.616035 gaphor-2.9.1/setup.py
--rw-r--r--   0        0        0    37731 2022-03-18 01:37:04.618330 gaphor-2.9.1/PKG-INFO
+-rw-r--r--   0        0        0    10901 2022-03-18 23:52:22.000000 gaphor-2.9.2/LICENSE.txt
+-rw-r--r--   0        0        0    35606 2022-03-18 23:52:22.000000 gaphor-2.9.2/README.md
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/__init__.py
+-rw-r--r--   0        0        0      138 2022-03-19 00:35:29.166953 gaphor-2.9.2/gaphor/C4Model/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     1543 2022-03-19 00:35:29.170953 gaphor-2.9.2/gaphor/C4Model/__pycache__/c4model.cpython-310.pyc
+-rw-r--r--   0        0        0      723 2022-03-19 00:35:29.170953 gaphor-2.9.2/gaphor/C4Model/__pycache__/iconname.cpython-310.pyc
+-rw-r--r--   0        0        0     1554 2022-03-19 00:35:29.170953 gaphor-2.9.2/gaphor/C4Model/__pycache__/modelinglanguage.cpython-310.pyc
+-rw-r--r--   0        0        0     2881 2022-03-19 00:35:29.170953 gaphor-2.9.2/gaphor/C4Model/__pycache__/propertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     2943 2022-03-19 00:35:29.178954 gaphor-2.9.2/gaphor/C4Model/__pycache__/toolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     1455 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/c4model.py
+-rw-r--r--   0        0        0      190 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/diagramitems/__init__.py
+-rw-r--r--   0        0        0      374 2022-03-19 00:35:29.174953 gaphor-2.9.2/gaphor/C4Model/diagramitems/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2328 2022-03-19 00:35:29.174953 gaphor-2.9.2/gaphor/C4Model/diagramitems/__pycache__/container.cpython-310.pyc
+-rw-r--r--   0        0        0     2671 2022-03-19 00:35:29.174953 gaphor-2.9.2/gaphor/C4Model/diagramitems/__pycache__/database.cpython-310.pyc
+-rw-r--r--   0        0        0     2774 2022-03-19 00:35:29.174953 gaphor-2.9.2/gaphor/C4Model/diagramitems/__pycache__/person.cpython-310.pyc
+-rw-r--r--   0        0        0     2020 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/diagramitems/container.py
+-rw-r--r--   0        0        0     2243 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/diagramitems/database.py
+-rw-r--r--   0        0        0     2266 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/diagramitems/person.py
+-rw-r--r--   0        0        0      550 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/iconname.py
+-rw-r--r--   0        0        0      970 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/modelinglanguage.py
+-rw-r--r--   0        0        0     3598 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/propertypages.glade
+-rw-r--r--   0        0        0     2487 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/propertypages.py
+-rw-r--r--   0        0        0     2560 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/propertypages.ui
+-rw-r--r--   0        0        0     4118 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/C4Model/toolbox.py
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/__init__.py
+-rw-r--r--   0        0        0      136 2022-03-19 00:35:29.358957 gaphor-2.9.2/gaphor/RAAML/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0      202 2022-03-19 00:35:35.067049 gaphor-2.9.2/gaphor/RAAML/__pycache__/diagramitems.cpython-310.pyc
+-rw-r--r--   0        0        0     1581 2022-03-19 00:35:35.787059 gaphor-2.9.2/gaphor/RAAML/__pycache__/modelinglanguage.cpython-310.pyc
+-rw-r--r--   0        0        0    12468 2022-03-19 00:35:29.362957 gaphor-2.9.2/gaphor/RAAML/__pycache__/raaml.cpython-310.pyc
+-rw-r--r--   0        0        0      686 2022-03-19 00:35:35.051049 gaphor-2.9.2/gaphor/RAAML/__pycache__/toolbox.cpython-310.pyc
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/__init__.py
+-rw-r--r--   0        0        0     2385 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/and.svg
+-rw-r--r--   0        0        0      474 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/basic_event.svg
+-rw-r--r--   0        0        0      484 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/conditional_event.svg
+-rw-r--r--   0        0        0      603 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/dormant_event.svg
+-rw-r--r--   0        0        0      504 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/house_event.svg
+-rw-r--r--   0        0        0      878 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/inhibit.svg
+-rw-r--r--   0        0        0      983 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/majority_vote.svg
+-rw-r--r--   0        0        0      738 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/not.svg
+-rw-r--r--   0        0        0     2252 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/or.svg
+-rw-r--r--   0        0        0      973 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/seq.svg
+-rw-r--r--   0        0        0      478 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/transfer_in.svg
+-rw-r--r--   0        0        0     1034 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/xor.svg
+-rw-r--r--   0        0        0      689 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagram_svgs/zero_event.svg
+-rw-r--r--   0        0        0       63 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/diagramitems.py
+-rw-r--r--   0        0        0      927 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/__init__.py
+-rw-r--r--   0        0        0     1254 2022-03-19 00:35:35.051049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2870 2022-03-19 00:35:35.051049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/andgate.cpython-310.pyc
+-rw-r--r--   0        0        0     2555 2022-03-19 00:35:35.051049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/basicevent.cpython-310.pyc
+-rw-r--r--   0        0        0     2160 2022-03-19 00:35:35.055049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/conditionalevent.cpython-310.pyc
+-rw-r--r--   0        0        0      246 2022-03-19 00:35:35.051049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/constants.cpython-310.pyc
+-rw-r--r--   0        0        0     2559 2022-03-19 00:35:35.055049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/dormantevent.cpython-310.pyc
+-rw-r--r--   0        0        0     3369 2022-03-19 00:35:35.067049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/ftatoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     2654 2022-03-19 00:35:35.055049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/houseevent.cpython-310.pyc
+-rw-r--r--   0        0        0     2836 2022-03-19 00:35:35.055049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/inhibitgate.cpython-310.pyc
+-rw-r--r--   0        0        0     2400 2022-03-19 00:35:35.059049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/intermediateevent.cpython-310.pyc
+-rw-r--r--   0        0        0     3509 2022-03-19 00:35:35.059049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/majorityvotegate.cpython-310.pyc
+-rw-r--r--   0        0        0     2534 2022-03-19 00:35:35.059049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/notgate.cpython-310.pyc
+-rw-r--r--   0        0        0     3236 2022-03-19 00:35:35.059049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/orgate.cpython-310.pyc
+-rw-r--r--   0        0        0     2694 2022-03-19 00:35:35.063049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/seqgate.cpython-310.pyc
+-rw-r--r--   0        0        0     2315 2022-03-19 00:35:35.063049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/topevent.cpython-310.pyc
+-rw-r--r--   0        0        0     2522 2022-03-19 00:35:35.063049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/transferin.cpython-310.pyc
+-rw-r--r--   0        0        0     2603 2022-03-19 00:35:35.063049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/transferout.cpython-310.pyc
+-rw-r--r--   0        0        0     2545 2022-03-19 00:35:35.055049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/undevelopedevent.cpython-310.pyc
+-rw-r--r--   0        0        0     2714 2022-03-19 00:35:35.067049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/xorgate.cpython-310.pyc
+-rw-r--r--   0        0        0     2661 2022-03-19 00:35:35.067049 gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/zeroevent.cpython-310.pyc
+-rw-r--r--   0        0        0     2616 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/andgate.py
+-rw-r--r--   0        0        0     1951 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/basicevent.py
+-rw-r--r--   0        0        0     1517 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/conditionalevent.py
+-rw-r--r--   0        0        0       87 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/constants.py
+-rw-r--r--   0        0        0     1900 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/dormantevent.py
+-rw-r--r--   0        0        0     6880 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/ftatoolbox.py
+-rw-r--r--   0        0        0     2048 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/houseevent.py
+-rw-r--r--   0        0        0     2674 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/inhibitgate.py
+-rw-r--r--   0        0        0     1776 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/intermediateevent.py
+-rw-r--r--   0        0        0     3389 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/majorityvotegate.py
+-rw-r--r--   0        0        0     1886 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/notgate.py
+-rw-r--r--   0        0        0     3254 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/orgate.py
+-rw-r--r--   0        0        0     2128 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/seqgate.py
+-rw-r--r--   0        0        0     1676 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/topevent.py
+-rw-r--r--   0        0        0     1874 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/transferin.py
+-rw-r--r--   0        0        0     1921 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/transferout.py
+-rw-r--r--   0        0        0     1858 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/undevelopedevent.py
+-rw-r--r--   0        0        0     2139 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/xorgate.py
+-rw-r--r--   0        0        0     2004 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/fta/zeroevent.py
+-rw-r--r--   0        0        0      965 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/modelinglanguage.py
+-rw-r--r--   0        0        0     7305 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/raaml.py
+-rw-r--r--   0        0        0      481 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/stpa/__init__.py
+-rw-r--r--   0        0        0      545 2022-03-19 00:35:35.067049 gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0      689 2022-03-19 00:35:35.071049 gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/connectors.cpython-310.pyc
+-rw-r--r--   0        0        0     2365 2022-03-19 00:35:35.067049 gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/controlaction.cpython-310.pyc
+-rw-r--r--   0        0        0     2470 2022-03-19 00:35:35.071049 gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/operationalsituation.cpython-310.pyc
+-rw-r--r--   0        0        0      565 2022-03-19 00:35:35.071049 gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/relationships.cpython-310.pyc
+-rw-r--r--   0        0        0     2931 2022-03-19 00:35:35.071049 gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/stpatoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     2422 2022-03-19 00:35:35.071049 gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/unsafecontrolaction.cpython-310.pyc
+-rw-r--r--   0        0        0      423 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/stpa/connectors.py
+-rw-r--r--   0        0        0     1752 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/stpa/controlaction.py
+-rw-r--r--   0        0        0     1842 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/stpa/operationalsituation.py
+-rw-r--r--   0        0        0      292 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/stpa/relationships.py
+-rw-r--r--   0        0        0     4949 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/stpa/stpatoolbox.py
+-rw-r--r--   0        0        0     1792 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/stpa/unsafecontrolaction.py
+-rw-r--r--   0        0        0      547 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/RAAML/toolbox.py
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/__init__.py
+-rw-r--r--   0        0        0      136 2022-03-19 00:35:29.222954 gaphor-2.9.2/gaphor/SysML/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0      213 2022-03-19 00:35:29.382958 gaphor-2.9.2/gaphor/SysML/__pycache__/diagramitems.cpython-310.pyc
+-rw-r--r--   0        0        0     1581 2022-03-19 00:35:29.374958 gaphor-2.9.2/gaphor/SysML/__pycache__/modelinglanguage.cpython-310.pyc
+-rw-r--r--   0        0        0     7867 2022-03-19 00:35:29.374958 gaphor-2.9.2/gaphor/SysML/__pycache__/propertypages.cpython-310.pyc
+-rw-r--r--   0        0        0    10895 2022-03-19 00:35:29.222954 gaphor-2.9.2/gaphor/SysML/__pycache__/sysml.cpython-310.pyc
+-rw-r--r--   0        0        0     1971 2022-03-19 00:35:29.382958 gaphor-2.9.2/gaphor/SysML/__pycache__/toolbox.cpython-310.pyc
+-rw-r--r--   0        0        0      229 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/blocks/__init__.py
+-rw-r--r--   0        0        0      421 2022-03-19 00:35:29.358957 gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     4852 2022-03-19 00:35:29.358957 gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/block.cpython-310.pyc
+-rw-r--r--   0        0        0     2064 2022-03-19 00:35:29.382958 gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/blockstoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     3152 2022-03-19 00:35:29.358957 gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/connectors.cpython-310.pyc
+-rw-r--r--   0        0        0      664 2022-03-19 00:35:29.370957 gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/group.cpython-310.pyc
+-rw-r--r--   0        0        0     2929 2022-03-19 00:35:29.366958 gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/property.cpython-310.pyc
+-rw-r--r--   0        0        0     4834 2022-03-19 00:35:29.366958 gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/proxyport.cpython-310.pyc
+-rw-r--r--   0        0        0     5336 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/blocks/block.py
+-rw-r--r--   0        0        0     3450 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/blocks/blockstoolbox.py
+-rw-r--r--   0        0        0     2846 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/blocks/connectors.py
+-rw-r--r--   0        0        0      536 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/blocks/group.py
+-rw-r--r--   0        0        0     2561 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/blocks/property.py
+-rw-r--r--   0        0        0     4360 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/blocks/proxyport.py
+-rw-r--r--   0        0        0       74 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/diagramitems.py
+-rw-r--r--   0        0        0      965 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/modelinglanguage.py
+-rw-r--r--   0        0        0    11606 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/propertypages.glade
+-rw-r--r--   0        0        0     8133 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/propertypages.py
+-rw-r--r--   0        0        0     7685 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/propertypages.ui
+-rw-r--r--   0        0        0      382 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/requirements/__init__.py
+-rw-r--r--   0        0        0      495 2022-03-19 00:35:29.374958 gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2085 2022-03-19 00:35:29.378958 gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/connectors.cpython-310.pyc
+-rw-r--r--   0        0        0     2252 2022-03-19 00:35:29.378958 gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/relationships.cpython-310.pyc
+-rw-r--r--   0        0        0     3900 2022-03-19 00:35:29.378958 gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/requirement.cpython-310.pyc
+-rw-r--r--   0        0        0     1539 2022-03-19 00:35:29.382958 gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/requirementstoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     1587 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/requirements/connectors.py
+-rw-r--r--   0        0        0     1498 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/requirements/relationships.py
+-rw-r--r--   0        0        0     4421 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/requirements/requirement.py
+-rw-r--r--   0        0        0     2111 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/requirements/requirementstoolbox.py
+-rw-r--r--   0        0        0     9055 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/sysml.py
+-rw-r--r--   0        0        0     2391 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/SysML/toolbox.py
+-rw-r--r--   0        0        0      161 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/__init__.py
+-rw-r--r--   0        0        0      299 2022-03-19 00:35:29.070951 gaphor-2.9.2/gaphor/UML/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     1801 2022-03-19 00:35:29.258955 gaphor-2.9.2/gaphor/UML/__pycache__/copypaste.cpython-310.pyc
+-rw-r--r--   0        0        0      797 2022-03-19 00:35:29.098952 gaphor-2.9.2/gaphor/UML/__pycache__/deletable.cpython-310.pyc
+-rw-r--r--   0        0        0      510 2022-03-19 00:35:29.178954 gaphor-2.9.2/gaphor/UML/__pycache__/diagramitems.cpython-310.pyc
+-rw-r--r--   0        0        0      662 2022-03-19 00:35:29.102952 gaphor-2.9.2/gaphor/UML/__pycache__/group.cpython-310.pyc
+-rw-r--r--   0        0        0      478 2022-03-19 00:35:29.102952 gaphor-2.9.2/gaphor/UML/__pycache__/iconname.cpython-310.pyc
+-rw-r--r--   0        0        0     1579 2022-03-19 00:35:29.342957 gaphor-2.9.2/gaphor/UML/__pycache__/modelinglanguage.cpython-310.pyc
+-rw-r--r--   0        0        0    10526 2022-03-19 00:35:29.106952 gaphor-2.9.2/gaphor/UML/__pycache__/recipes.cpython-310.pyc
+-rw-r--r--   0        0        0     5460 2022-03-19 00:35:31.803003 gaphor-2.9.2/gaphor/UML/__pycache__/sanitizerservice.cpython-310.pyc
+-rw-r--r--   0        0        0     1445 2022-03-19 00:35:29.342957 gaphor-2.9.2/gaphor/UML/__pycache__/toolbox.cpython-310.pyc
+-rw-r--r--   0        0        0    42640 2022-03-19 00:35:29.082951 gaphor-2.9.2/gaphor/UML/__pycache__/uml.cpython-310.pyc
+-rw-r--r--   0        0        0     5508 2022-03-19 00:35:29.202954 gaphor-2.9.2/gaphor/UML/__pycache__/umlfmt.cpython-310.pyc
+-rw-r--r--   0        0        0     6227 2022-03-19 00:35:29.086951 gaphor-2.9.2/gaphor/UML/__pycache__/umllex.cpython-310.pyc
+-rw-r--r--   0        0        0     4759 2022-03-19 00:35:29.070951 gaphor-2.9.2/gaphor/UML/__pycache__/umloverrides.cpython-310.pyc
+-rw-r--r--   0        0        0      946 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/__init__.py
+-rw-r--r--   0        0        0      959 2022-03-19 00:35:29.178954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     3419 2022-03-19 00:35:29.190954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/action.cpython-310.pyc
+-rw-r--r--   0        0        0     1060 2022-03-19 00:35:29.178954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionseditors.cpython-310.pyc
+-rw-r--r--   0        0        0      715 2022-03-19 00:35:29.182953 gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionsgroup.cpython-310.pyc
+-rw-r--r--   0        0        0     6339 2022-03-19 00:35:29.186954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionspropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     3777 2022-03-19 00:35:29.318956 gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionstoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     9633 2022-03-19 00:35:29.182953 gaphor-2.9.2/gaphor/UML/actions/__pycache__/activitynodes.cpython-310.pyc
+-rw-r--r--   0        0        0      509 2022-03-19 00:35:29.186954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/copypaste.cpython-310.pyc
+-rw-r--r--   0        0        0     2690 2022-03-19 00:35:29.194954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/flow.cpython-310.pyc
+-rw-r--r--   0        0        0     6220 2022-03-19 00:35:29.190954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/flowconnect.cpython-310.pyc
+-rw-r--r--   0        0        0     2649 2022-03-19 00:35:29.186954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/objectnode.cpython-310.pyc
+-rw-r--r--   0        0        0     3285 2022-03-19 00:35:29.186954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/partition.cpython-310.pyc
+-rw-r--r--   0        0        0     4160 2022-03-19 00:35:29.194954 gaphor-2.9.2/gaphor/UML/actions/__pycache__/partitionpage.cpython-310.pyc
+-rw-r--r--   0        0        0     2844 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/action.py
+-rw-r--r--   0        0        0      751 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/actionseditors.py
+-rw-r--r--   0        0        0      561 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/actionsgroup.py
+-rw-r--r--   0        0        0     5406 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/actionspropertypages.py
+-rw-r--r--   0        0        0     5796 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/actionstoolbox.py
+-rw-r--r--   0        0        0     8762 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/activitynodes.py
+-rw-r--r--   0        0        0      297 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/copypaste.py
+-rw-r--r--   0        0        0     2168 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/flow.py
+-rw-r--r--   0        0        0     8026 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/flowconnect.py
+-rw-r--r--   0        0        0     2465 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/objectnode.py
+-rw-r--r--   0        0        0     3409 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/partition.py
+-rw-r--r--   0        0        0     4414 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/partitionpage.py
+-rw-r--r--   0        0        0    11286 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/propertypages.glade
+-rw-r--r--   0        0        0     8193 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/actions/propertypages.ui
+-rw-r--r--   0        0        0     1156 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/__init__.py
+-rw-r--r--   0        0        0     1284 2022-03-19 00:35:29.198954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0    13682 2022-03-19 00:35:29.202954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/association.cpython-310.pyc
+-rw-r--r--   0        0        0     6120 2022-03-19 00:35:29.266955 gaphor-2.9.2/gaphor/UML/classes/__pycache__/associationpropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     6562 2022-03-19 00:35:29.198954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/classconnect.cpython-310.pyc
+-rw-r--r--   0        0        0     1910 2022-03-19 00:35:29.214954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/classeseditors.cpython-310.pyc
+-rw-r--r--   0        0        0    15639 2022-03-19 00:35:29.218954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/classespropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     2885 2022-03-19 00:35:29.318956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/classestoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     3101 2022-03-19 00:35:29.254955 gaphor-2.9.2/gaphor/UML/classes/__pycache__/component.cpython-310.pyc
+-rw-r--r--   0        0        0     1237 2022-03-19 00:35:29.282956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/containment.cpython-310.pyc
+-rw-r--r--   0        0        0     2655 2022-03-19 00:35:29.278956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/containmentconnect.cpython-310.pyc
+-rw-r--r--   0        0        0     1320 2022-03-19 00:35:29.282956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/copypaste.cpython-310.pyc
+-rw-r--r--   0        0        0     3291 2022-03-19 00:35:29.222954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/datatype.cpython-310.pyc
+-rw-r--r--   0        0        0     4330 2022-03-19 00:35:29.206954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/dependency.cpython-310.pyc
+-rw-r--r--   0        0        0     2976 2022-03-19 00:35:29.274955 gaphor-2.9.2/gaphor/UML/classes/__pycache__/dependencypropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     4001 2022-03-19 00:35:29.278956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/enumeration.cpython-310.pyc
+-rw-r--r--   0        0        0     3050 2022-03-19 00:35:29.278956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/enumerationpropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     1682 2022-03-19 00:35:29.210954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/generalization.cpython-310.pyc
+-rw-r--r--   0        0        0    11874 2022-03-19 00:35:29.206954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/interface.cpython-310.pyc
+-rw-r--r--   0        0        0     2786 2022-03-19 00:35:29.282956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/interfaceconnect.cpython-310.pyc
+-rw-r--r--   0        0        0     2251 2022-03-19 00:35:29.214954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/interfacerealization.cpython-310.pyc
+-rw-r--r--   0        0        0     6498 2022-03-19 00:35:29.210954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/klass.cpython-310.pyc
+-rw-r--r--   0        0        0     2548 2022-03-19 00:35:29.282956 gaphor-2.9.2/gaphor/UML/classes/__pycache__/package.cpython-310.pyc
+-rw-r--r--   0        0        0     1906 2022-03-19 00:35:29.210954 gaphor-2.9.2/gaphor/UML/classes/__pycache__/stereotype.cpython-310.pyc
+-rw-r--r--   0        0        0    15951 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/association.py
+-rw-r--r--   0        0        0     6747 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/associationpropertypages.py
+-rw-r--r--   0        0        0     7069 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/classconnect.py
+-rw-r--r--   0        0        0     1922 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/classeseditors.py
+-rw-r--r--   0        0        0    15661 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/classespropertypages.py
+-rw-r--r--   0        0        0     4948 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/classestoolbox.py
+-rw-r--r--   0        0        0     3046 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/component.py
+-rw-r--r--   0        0        0      782 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/containment.py
+-rw-r--r--   0        0        0     3279 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/containmentconnect.py
+-rw-r--r--   0        0        0     1127 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/copypaste.py
+-rw-r--r--   0        0        0     3458 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/datatype.py
+-rw-r--r--   0        0        0     3664 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/dependency.py
+-rw-r--r--   0        0        0     2570 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/dependencypropertypages.py
+-rw-r--r--   0        0        0     4080 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/enumeration.py
+-rw-r--r--   0        0        0     2950 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/enumerationpropertypages.py
+-rw-r--r--   0        0        0     1020 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/generalization.py
+-rw-r--r--   0        0        0    12329 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/interface.py
+-rw-r--r--   0        0        0     2490 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/interfaceconnect.py
+-rw-r--r--   0        0        0     1585 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/interfacerealization.py
+-rw-r--r--   0        0        0     7026 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/klass.py
+-rw-r--r--   0        0        0     2098 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/package.py
+-rw-r--r--   0        0        0    39298 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/propertypages.glade
+-rw-r--r--   0        0        0    32676 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/propertypages.ui
+-rw-r--r--   0        0        0     1240 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/classes/stereotype.py
+-rw-r--r--   0        0        0     1305 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/copypaste.py
+-rw-r--r--   0        0        0      549 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deletable.py
+-rw-r--r--   0        0        0      348 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/__init__.py
+-rw-r--r--   0        0        0      523 2022-03-19 00:35:29.226955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2875 2022-03-19 00:35:29.262955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/artifact.cpython-310.pyc
+-rw-r--r--   0        0        0     8062 2022-03-19 00:35:29.258955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/connector.cpython-310.pyc
+-rw-r--r--   0        0        0     5569 2022-03-19 00:35:29.226955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/connectorconnect.cpython-310.pyc
+-rw-r--r--   0        0        0      779 2022-03-19 00:35:29.258955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/copypaste.cpython-310.pyc
+-rw-r--r--   0        0        0     3258 2022-03-19 00:35:29.262955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/deploymentpropertypage.cpython-310.pyc
+-rw-r--r--   0        0        0     1116 2022-03-19 00:35:29.262955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/deploymentsgroup.cpython-310.pyc
+-rw-r--r--   0        0        0     1012 2022-03-19 00:35:29.342957 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/deploymentstoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     3268 2022-03-19 00:35:29.266955 gaphor-2.9.2/gaphor/UML/deployments/__pycache__/node.cpython-310.pyc
+-rw-r--r--   0        0        0     2613 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/artifact.py
+-rw-r--r--   0        0        0     7882 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/connector.py
+-rw-r--r--   0        0        0     6666 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/connectorconnect.py
+-rw-r--r--   0        0        0      502 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/copypaste.py
+-rw-r--r--   0        0        0     3389 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/deploymentpropertypage.py
+-rw-r--r--   0        0        0      977 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/deploymentsgroup.py
+-rw-r--r--   0        0        0     1385 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/deploymentstoolbox.py
+-rw-r--r--   0        0        0     3027 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/node.py
+-rw-r--r--   0        0        0     3778 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/propertypages.glade
+-rw-r--r--   0        0        0     2424 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/deployments/propertypages.ui
+-rw-r--r--   0        0        0      382 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/diagramitems.py
+-rw-r--r--   0        0        0      549 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/group.py
+-rw-r--r--   0        0        0      302 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/iconname.py
+-rw-r--r--   0        0        0      509 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/__init__.py
+-rw-r--r--   0        0        0      647 2022-03-19 00:35:29.286956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0      846 2022-03-19 00:35:29.286956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/copypaste.cpython-310.pyc
+-rw-r--r--   0        0        0     5650 2022-03-19 00:35:29.290956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/executionspecification.cpython-310.pyc
+-rw-r--r--   0        0        0     1977 2022-03-19 00:35:29.294956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interaction.cpython-310.pyc
+-rw-r--r--   0        0        0     9684 2022-03-19 00:35:29.290956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionsconnect.cpython-310.pyc
+-rw-r--r--   0        0        0      709 2022-03-19 00:35:29.298956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionsgroup.cpython-310.pyc
+-rw-r--r--   0        0        0     2362 2022-03-19 00:35:29.298956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionspropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     2566 2022-03-19 00:35:29.318956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionstoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     9318 2022-03-19 00:35:29.294956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/lifeline.cpython-310.pyc
+-rw-r--r--   0        0        0     6981 2022-03-19 00:35:29.294956 gaphor-2.9.2/gaphor/UML/interactions/__pycache__/message.cpython-310.pyc
+-rw-r--r--   0        0        0      630 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/copypaste.py
+-rw-r--r--   0        0        0     4813 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/executionspecification.py
+-rw-r--r--   0        0        0     1573 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/interaction.py
+-rw-r--r--   0        0        0    11713 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/interactionsconnect.py
+-rw-r--r--   0        0        0      512 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/interactionsgroup.py
+-rw-r--r--   0        0        0     2693 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/interactionspropertypages.py
+-rw-r--r--   0        0        0     3031 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/interactionstoolbox.py
+-rw-r--r--   0        0        0     8595 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/lifeline.py
+-rw-r--r--   0        0        0     7205 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/message.py
+-rw-r--r--   0        0        0     1639 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/propertypages.glade
+-rw-r--r--   0        0        0     1355 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/interactions/propertypages.ui
+-rw-r--r--   0        0        0      990 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/modelinglanguage.py
+-rw-r--r--   0        0        0      310 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/__init__.py
+-rw-r--r--   0        0        0      471 2022-03-19 00:35:29.266955 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     1816 2022-03-19 00:35:29.270955 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/extension.cpython-310.pyc
+-rw-r--r--   0        0        0     2440 2022-03-19 00:35:29.270955 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/extensionconnect.cpython-310.pyc
+-rw-r--r--   0        0        0     2414 2022-03-19 00:35:29.270955 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/metaclasspropertypage.cpython-310.pyc
+-rw-r--r--   0        0        0     1384 2022-03-19 00:35:29.274955 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/packageimport.cpython-310.pyc
+-rw-r--r--   0        0        0     1400 2022-03-19 00:35:29.270955 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/packageimportconnect.cpython-310.pyc
+-rw-r--r--   0        0        0     1428 2022-03-19 00:35:29.346957 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/profilestoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     3872 2022-03-19 00:35:29.274955 gaphor-2.9.2/gaphor/UML/profiles/__pycache__/stereotypepropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     1177 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/extension.py
+-rw-r--r--   0        0        0     3491 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/extensionconnect.py
+-rw-r--r--   0        0        0     1834 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/metaclasspropertypage.py
+-rw-r--r--   0        0        0      856 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/packageimport.py
+-rw-r--r--   0        0        0     1183 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/packageimportconnect.py
+-rw-r--r--   0        0        0     1943 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/profilestoolbox.py
+-rw-r--r--   0        0        0     5616 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/propertypages.glade
+-rw-r--r--   0        0        0     4409 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/propertypages.ui
+-rw-r--r--   0        0        0     4700 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/profiles/stereotypepropertypages.py
+-rw-r--r--   0        0        0    11709 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/recipes.py
+-rw-r--r--   0        0        0     6041 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/sanitizerservice.py
+-rw-r--r--   0        0        0     1236 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/__init__.py
+-rw-r--r--   0        0        0     1404 2022-03-19 00:35:29.298956 gaphor-2.9.2/gaphor/UML/states/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0      796 2022-03-19 00:35:29.302956 gaphor-2.9.2/gaphor/UML/states/__pycache__/copypaste.cpython-310.pyc
+-rw-r--r--   0        0        0     1928 2022-03-19 00:35:29.306956 gaphor-2.9.2/gaphor/UML/states/__pycache__/finalstate.cpython-310.pyc
+-rw-r--r--   0        0        0     3708 2022-03-19 00:35:29.302956 gaphor-2.9.2/gaphor/UML/states/__pycache__/propertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     2685 2022-03-19 00:35:29.306956 gaphor-2.9.2/gaphor/UML/states/__pycache__/pseudostates.cpython-310.pyc
+-rw-r--r--   0        0        0     3351 2022-03-19 00:35:29.306956 gaphor-2.9.2/gaphor/UML/states/__pycache__/state.cpython-310.pyc
+-rw-r--r--   0        0        0     2719 2022-03-19 00:35:29.318956 gaphor-2.9.2/gaphor/UML/states/__pycache__/statestoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     1681 2022-03-19 00:35:29.306956 gaphor-2.9.2/gaphor/UML/states/__pycache__/transition.cpython-310.pyc
+-rw-r--r--   0        0        0     2901 2022-03-19 00:35:29.302956 gaphor-2.9.2/gaphor/UML/states/__pycache__/vertexconnect.cpython-310.pyc
+-rw-r--r--   0        0        0      595 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/copypaste.py
+-rw-r--r--   0        0        0     1365 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/finalstate.py
+-rw-r--r--   0        0        0     4440 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/propertypages.glade
+-rw-r--r--   0        0        0     3488 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/propertypages.py
+-rw-r--r--   0        0        0     2973 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/propertypages.ui
+-rw-r--r--   0        0        0     2039 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/pseudostates.py
+-rw-r--r--   0        0        0     2998 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/state.py
+-rw-r--r--   0        0        0     3362 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/statestoolbox.py
+-rw-r--r--   0        0        0     1164 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/transition.py
+-rw-r--r--   0        0        0     2622 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/states/vertexconnect.py
+-rw-r--r--   0        0        0     1531 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/toolbox.py
+-rw-r--r--   0        0        0    64347 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/uml.py
+-rw-r--r--   0        0        0     5584 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/umlfmt.py
+-rw-r--r--   0        0        0     9290 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/umllex.py
+-rw-r--r--   0        0        0     4971 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/umloverrides.py
+-rw-r--r--   0        0        0      363 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/__init__.py
+-rw-r--r--   0        0        0      523 2022-03-19 00:35:29.310956 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2375 2022-03-19 00:35:29.314956 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/actor.cpython-310.pyc
+-rw-r--r--   0        0        0     1535 2022-03-19 00:35:29.310956 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/extend.cpython-310.pyc
+-rw-r--r--   0        0        0     1541 2022-03-19 00:35:29.310956 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/include.cpython-310.pyc
+-rw-r--r--   0        0        0     1806 2022-03-19 00:35:29.314956 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecase.cpython-310.pyc
+-rw-r--r--   0        0        0     1727 2022-03-19 00:35:29.310956 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecaseconnect.cpython-310.pyc
+-rw-r--r--   0        0        0      671 2022-03-19 00:35:29.314956 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecasegroup.cpython-310.pyc
+-rw-r--r--   0        0        0     1228 2022-03-19 00:35:29.346957 gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecasetoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0     1899 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/actor.py
+-rw-r--r--   0        0        0      966 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/extend.py
+-rw-r--r--   0        0        0      970 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/include.py
+-rw-r--r--   0        0        0     1256 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/usecase.py
+-rw-r--r--   0        0        0     1434 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/usecaseconnect.py
+-rw-r--r--   0        0        0      533 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/usecasegroup.py
+-rw-r--r--   0        0        0     1746 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/UML/usecases/usecasetoolbox.py
+-rw-r--r--   0        0        0      738 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/__init__.py
+-rw-r--r--   0        0        0       86 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/__main__.py
+-rw-r--r--   0        0        0     1294 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/abc.py
+-rw-r--r--   0        0        0     1553 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/action.py
+-rw-r--r--   0        0        0     7333 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/application.py
+-rw-r--r--   0        0        0     1575 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/babel.py
+-rw-r--r--   0        0        0      290 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/codegen/__init__.py
+-rw-r--r--   0        0        0      323 2022-03-19 00:35:29.430959 gaphor-2.9.2/gaphor/codegen/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0    14568 2022-03-19 00:35:32.191008 gaphor-2.9.2/gaphor/codegen/__pycache__/coder.cpython-310.pyc
+-rw-r--r--   0        0        0     2852 2022-03-19 00:35:32.191008 gaphor-2.9.2/gaphor/codegen/__pycache__/override.cpython-310.pyc
+-rw-r--r--   0        0        0    14906 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/codegen/coder.py
+-rw-r--r--   0        0        0     3229 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/codegen/override.py
+-rw-r--r--   0        0        0      311 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/__init__.py
+-rw-r--r--   0        0        0      508 2022-03-19 00:35:28.946948 gaphor-2.9.2/gaphor/core/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2039 2022-03-19 00:35:28.946948 gaphor-2.9.2/gaphor/core/__pycache__/eventmanager.cpython-310.pyc
+-rw-r--r--   0        0        0     1128 2022-03-19 00:35:29.090952 gaphor-2.9.2/gaphor/core/__pycache__/format.cpython-310.pyc
+-rw-r--r--   0        0        0     1540 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/eventmanager.py
+-rw-r--r--   0        0        0      780 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/format.py
+-rw-r--r--   0        0        0      412 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/__init__.py
+-rw-r--r--   0        0        0      651 2022-03-19 00:35:28.986949 gaphor-2.9.2/gaphor/core/modeling/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     6882 2022-03-19 00:35:28.994949 gaphor-2.9.2/gaphor/core/modeling/__pycache__/collection.cpython-310.pyc
+-rw-r--r--   0        0        0     1515 2022-03-19 00:35:28.986949 gaphor-2.9.2/gaphor/core/modeling/__pycache__/coremodel.cpython-310.pyc
+-rw-r--r--   0        0        0    16413 2022-03-19 00:35:29.002950 gaphor-2.9.2/gaphor/core/modeling/__pycache__/diagram.cpython-310.pyc
+-rw-r--r--   0        0        0     8889 2022-03-19 00:35:28.998950 gaphor-2.9.2/gaphor/core/modeling/__pycache__/element.cpython-310.pyc
+-rw-r--r--   0        0        0     7849 2022-03-19 00:35:29.034950 gaphor-2.9.2/gaphor/core/modeling/__pycache__/elementdispatcher.cpython-310.pyc
+-rw-r--r--   0        0        0     8949 2022-03-19 00:35:29.030950 gaphor-2.9.2/gaphor/core/modeling/__pycache__/elementfactory.cpython-310.pyc
+-rw-r--r--   0        0        0     8372 2022-03-19 00:35:28.994949 gaphor-2.9.2/gaphor/core/modeling/__pycache__/event.cpython-310.pyc
+-rw-r--r--   0        0        0     8464 2022-03-19 00:35:28.998950 gaphor-2.9.2/gaphor/core/modeling/__pycache__/listmixins.cpython-310.pyc
+-rw-r--r--   0        0        0     2424 2022-03-19 00:35:29.322956 gaphor-2.9.2/gaphor/core/modeling/__pycache__/modelinglanguage.cpython-310.pyc
+-rw-r--r--   0        0        0     5282 2022-03-19 00:35:29.006950 gaphor-2.9.2/gaphor/core/modeling/__pycache__/presentation.cpython-310.pyc
+-rw-r--r--   0        0        0    27932 2022-03-19 00:35:28.994949 gaphor-2.9.2/gaphor/core/modeling/__pycache__/properties.cpython-310.pyc
+-rw-r--r--   0        0        0     2561 2022-03-19 00:35:29.006950 gaphor-2.9.2/gaphor/core/modeling/__pycache__/stylesheet.cpython-310.pyc
+-rw-r--r--   0        0        0     4730 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/collection.py
+-rw-r--r--   0        0        0     2230 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/coremodel.py
+-rw-r--r--   0        0        0    13175 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/diagram.py
+-rw-r--r--   0        0        0     6378 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/element.py
+-rw-r--r--   0        0        0     9372 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/elementdispatcher.py
+-rw-r--r--   0        0        0     7511 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/elementfactory.py
+-rw-r--r--   0        0        0     7232 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/event.py
+-rw-r--r--   0        0        0     7735 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/listmixins.py
+-rw-r--r--   0        0        0     1341 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/modelinglanguage.py
+-rw-r--r--   0        0        0     4734 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/presentation.py
+-rw-r--r--   0        0        0    28743 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/properties.py
+-rw-r--r--   0        0        0     2007 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/modeling/stylesheet.py
+-rw-r--r--   0        0        0     3398 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/styling/__init__.py
+-rw-r--r--   0        0        0     4639 2022-03-19 00:35:29.006950 gaphor-2.9.2/gaphor/core/styling/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     6092 2022-03-19 00:35:29.014950 gaphor-2.9.2/gaphor/core/styling/__pycache__/declarations.cpython-310.pyc
+-rw-r--r--   0        0        0    10847 2022-03-19 00:35:29.022950 gaphor-2.9.2/gaphor/core/styling/__pycache__/parser.cpython-310.pyc
+-rw-r--r--   0        0        0     1779 2022-03-19 00:35:29.018950 gaphor-2.9.2/gaphor/core/styling/__pycache__/properties.cpython-310.pyc
+-rw-r--r--   0        0        0     6753 2022-03-19 00:35:29.026950 gaphor-2.9.2/gaphor/core/styling/__pycache__/selectors.cpython-310.pyc
+-rw-r--r--   0        0        0     5163 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/styling/declarations.py
+-rw-r--r--   0        0        0    11597 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/styling/parser.py
+-rw-r--r--   0        0        0     1454 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/styling/properties.py
+-rw-r--r--   0        0        0     4122 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/core/styling/selectors.py
+-rw-r--r--   0        0        0      252 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/__init__.py
+-rw-r--r--   0        0        0      396 2022-03-19 00:35:28.978949 gaphor-2.9.2/gaphor/diagram/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0    12472 2022-03-19 00:35:29.034950 gaphor-2.9.2/gaphor/diagram/__pycache__/connectors.cpython-310.pyc
+-rw-r--r--   0        0        0     7005 2022-03-19 00:35:29.038950 gaphor-2.9.2/gaphor/diagram/__pycache__/copypaste.cpython-310.pyc
+-rw-r--r--   0        0        0      438 2022-03-19 00:35:29.098952 gaphor-2.9.2/gaphor/diagram/__pycache__/deletable.cpython-310.pyc
+-rw-r--r--   0        0        0     4220 2022-03-19 00:35:29.054951 gaphor-2.9.2/gaphor/diagram/__pycache__/diagramtoolbox.cpython-310.pyc
+-rw-r--r--   0        0        0      580 2022-03-19 00:35:29.110952 gaphor-2.9.2/gaphor/diagram/__pycache__/event.cpython-310.pyc
+-rw-r--r--   0        0        0     2232 2022-03-19 00:35:33.199022 gaphor-2.9.2/gaphor/diagram/__pycache__/export.cpython-310.pyc
+-rw-r--r--   0        0        0     2514 2022-03-19 00:35:29.070951 gaphor-2.9.2/gaphor/diagram/__pycache__/group.cpython-310.pyc
+-rw-r--r--   0        0        0     1801 2022-03-19 00:35:29.218954 gaphor-2.9.2/gaphor/diagram/__pycache__/hoversupport.cpython-310.pyc
+-rw-r--r--   0        0        0      724 2022-03-19 00:35:29.102952 gaphor-2.9.2/gaphor/diagram/__pycache__/iconname.cpython-310.pyc
+-rw-r--r--   0        0        0     3382 2022-03-19 00:35:29.062951 gaphor-2.9.2/gaphor/diagram/__pycache__/inlineeditors.cpython-310.pyc
+-rw-r--r--   0        0        0     3105 2022-03-19 00:35:29.118952 gaphor-2.9.2/gaphor/diagram/__pycache__/painter.cpython-310.pyc
+-rw-r--r--   0        0        0    13002 2022-03-19 00:35:29.042950 gaphor-2.9.2/gaphor/diagram/__pycache__/presentation.cpython-310.pyc
+-rw-r--r--   0        0        0    11944 2022-03-19 00:35:29.066951 gaphor-2.9.2/gaphor/diagram/__pycache__/propertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     1490 2022-03-19 00:35:29.118952 gaphor-2.9.2/gaphor/diagram/__pycache__/selection.cpython-310.pyc
+-rw-r--r--   0        0        0    11181 2022-03-19 00:35:29.046951 gaphor-2.9.2/gaphor/diagram/__pycache__/shapes.cpython-310.pyc
+-rw-r--r--   0        0        0     1365 2022-03-19 00:35:29.058951 gaphor-2.9.2/gaphor/diagram/__pycache__/support.cpython-310.pyc
+-rw-r--r--   0        0        0     6499 2022-03-19 00:35:29.046951 gaphor-2.9.2/gaphor/diagram/__pycache__/text.cpython-310.pyc
+-rw-r--r--   0        0        0    13006 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/connectors.py
+-rw-r--r--   0        0        0     6218 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/copypaste.py
+-rw-r--r--   0        0        0      217 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/deletable.py
+-rw-r--r--   0        0        0     4230 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/diagramtoolbox.py
+-rw-r--r--   0        0        0      127 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/event.py
+-rw-r--r--   0        0        0     2002 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/export.py
+-rw-r--r--   0        0        0      339 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/general/__init__.py
+-rw-r--r--   0        0        0      539 2022-03-19 00:35:29.054951 gaphor-2.9.2/gaphor/diagram/general/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     1912 2022-03-19 00:35:29.058951 gaphor-2.9.2/gaphor/diagram/general/__pycache__/comment.cpython-310.pyc
+-rw-r--r--   0        0        0     1081 2022-03-19 00:35:29.058951 gaphor-2.9.2/gaphor/diagram/general/__pycache__/commentline.cpython-310.pyc
+-rw-r--r--   0        0        0     3927 2022-03-19 00:35:29.058951 gaphor-2.9.2/gaphor/diagram/general/__pycache__/connectors.cpython-310.pyc
+-rw-r--r--   0        0        0     1370 2022-03-19 00:35:29.062951 gaphor-2.9.2/gaphor/diagram/general/__pycache__/generaleditors.cpython-310.pyc
+-rw-r--r--   0        0        0     1809 2022-03-19 00:35:29.062951 gaphor-2.9.2/gaphor/diagram/general/__pycache__/generalpropertypages.cpython-310.pyc
+-rw-r--r--   0        0        0     2039 2022-03-19 00:35:29.066951 gaphor-2.9.2/gaphor/diagram/general/__pycache__/simpleitem.cpython-310.pyc
+-rw-r--r--   0        0        0     1430 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/general/comment.py
+-rw-r--r--   0        0        0      622 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/general/commentline.py
+-rw-r--r--   0        0        0     5759 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/general/connectors.py
+-rw-r--r--   0        0        0     1126 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/general/generaleditors.py
+-rw-r--r--   0        0        0     1416 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/general/generalpropertypages.py
+-rw-r--r--   0        0        0     1251 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/general/simpleitem.py
+-rw-r--r--   0        0        0     1911 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/group.py
+-rw-r--r--   0        0        0     1606 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/hoversupport.py
+-rw-r--r--   0        0        0      458 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/iconname.py
+-rw-r--r--   0        0        0     2994 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/inlineeditors.py
+-rw-r--r--   0        0        0     2841 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/painter.py
+-rw-r--r--   0        0        0    11130 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/presentation.py
+-rw-r--r--   0        0        0     5048 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/propertypages.glade
+-rw-r--r--   0        0        0    10117 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/propertypages.py
+-rw-r--r--   0        0        0     3797 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/propertypages.ui
+-rw-r--r--   0        0        0      930 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/selection.py
+-rw-r--r--   0        0        0    11144 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/shapes.py
+-rw-r--r--   0        0        0      985 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/support.py
+-rw-r--r--   0        0        0     7647 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/text.py
+-rw-r--r--   0        0        0     2482 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/__init__.py
+-rw-r--r--   0        0        0     2180 2022-03-19 00:35:28.978949 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     4929 2022-03-19 00:35:28.982949 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/connector.cpython-310.pyc
+-rw-r--r--   0        0        0     1007 2022-03-19 00:35:29.054951 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/dnd.cpython-310.pyc
+-rw-r--r--   0        0        0     4037 2022-03-19 00:35:29.110952 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/dropzone.cpython-310.pyc
+-rw-r--r--   0        0        0     2201 2022-03-19 00:35:29.050951 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/grayout.cpython-310.pyc
+-rw-r--r--   0        0        0     3729 2022-03-19 00:35:29.114952 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/magnet.cpython-310.pyc
+-rw-r--r--   0        0        0     3949 2022-03-19 00:35:29.110952 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/placement.cpython-310.pyc
+-rw-r--r--   0        0        0     1960 2022-03-19 00:35:29.050951 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/segment.cpython-310.pyc
+-rw-r--r--   0        0        0     1421 2022-03-19 00:35:29.114952 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/shortcut.cpython-310.pyc
+-rw-r--r--   0        0        0     1199 2022-03-19 00:35:29.114952 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/textedit.cpython-310.pyc
+-rw-r--r--   0        0        0     1522 2022-03-19 00:35:29.114952 gaphor-2.9.2/gaphor/diagram/tools/__pycache__/txtool.cpython-310.pyc
+-rw-r--r--   0        0        0     5213 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/connector.py
+-rw-r--r--   0        0        0      760 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/dnd.py
+-rw-r--r--   0        0        0     4397 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/dropzone.py
+-rw-r--r--   0        0        0     1572 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/grayout.py
+-rw-r--r--   0        0        0     3871 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/magnet.py
+-rw-r--r--   0        0        0     3988 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/placement.py
+-rw-r--r--   0        0        0     1381 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/segment.py
+-rw-r--r--   0        0        0     1231 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/shortcut.py
+-rw-r--r--   0        0        0     1078 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/textedit.py
+-rw-r--r--   0        0        0      891 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/diagram/tools/txtool.py
+-rw-r--r--   0        0        0     2221 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/entrypoint.py
+-rw-r--r--   0        0        0     2894 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/event.py
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/extensions/__init__.py
+-rw-r--r--   0        0        0      141 2022-03-19 00:35:33.547027 gaphor-2.9.2/gaphor/extensions/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     4143 2022-03-19 00:35:33.551027 gaphor-2.9.2/gaphor/extensions/__pycache__/sphinx.cpython-310.pyc
+-rw-r--r--   0        0        0     4048 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/extensions/sphinx.py
+-rw-r--r--   0        0        0     1109 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/i18n.py
+-rw-r--r--   0        0        0      217 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/locale/README
+-rw-r--r--   0        0        0      431 2022-03-19 00:35:23.082847 gaphor-2.9.2/gaphor/locale/bn/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0     3183 2022-03-19 00:35:22.854845 gaphor-2.9.2/gaphor/locale/ca/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    17807 2022-03-19 00:35:22.390839 gaphor-2.9.2/gaphor/locale/de/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    33749 2022-03-19 00:35:24.974869 gaphor-2.9.2/gaphor/locale/es/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    26405 2022-03-19 00:35:23.318850 gaphor-2.9.2/gaphor/locale/fi/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0     6020 2022-03-19 00:35:24.734866 gaphor-2.9.2/gaphor/locale/fr/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    19230 2022-03-19 00:35:25.678879 gaphor-2.9.2/gaphor/locale/gl/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    32892 2022-03-19 00:35:23.790855 gaphor-2.9.2/gaphor/locale/hr/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    35166 2022-03-19 00:35:24.498863 gaphor-2.9.2/gaphor/locale/hu/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0     5691 2022-03-19 00:35:24.026857 gaphor-2.9.2/gaphor/locale/it/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    11162 2022-03-19 00:35:26.150888 gaphor-2.9.2/gaphor/locale/ja/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    13406 2022-03-19 00:35:25.910883 gaphor-2.9.2/gaphor/locale/ko/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    20605 2022-03-19 00:35:23.554852 gaphor-2.9.2/gaphor/locale/nl/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0    15309 2022-03-19 00:35:24.262860 gaphor-2.9.2/gaphor/locale/pt_BR/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0     4135 2022-03-19 00:35:22.622842 gaphor-2.9.2/gaphor/locale/ru/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0     1022 2022-03-19 00:35:25.206873 gaphor-2.9.2/gaphor/locale/sv/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0     8809 2022-03-19 00:35:25.442876 gaphor-2.9.2/gaphor/locale/zh_Hans/LC_MESSAGES/gaphor.mo
+-rw-r--r--   0        0        0      605 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/__init__.py
+-rw-r--r--   0        0        0      751 2022-03-19 00:35:33.635028 gaphor-2.9.2/gaphor/plugins/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/console/__init__.py
+-rw-r--r--   0        0        0      146 2022-03-19 00:35:33.635028 gaphor-2.9.2/gaphor/plugins/console/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0    10345 2022-03-19 00:35:33.643029 gaphor-2.9.2/gaphor/plugins/console/__pycache__/console.cpython-310.pyc
+-rw-r--r--   0        0        0     3033 2022-03-19 00:35:33.719030 gaphor-2.9.2/gaphor/plugins/console/__pycache__/consolewindow.cpython-310.pyc
+-rw-r--r--   0        0        0     9940 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/console/console.py
+-rw-r--r--   0        0        0     2702 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/console/consolewindow.py
+-rw-r--r--   0        0        0     2247 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/diagramexport/__init__.py
+-rw-r--r--   0        0        0     2316 2022-03-19 00:35:34.895047 gaphor-2.9.2/gaphor/plugins/diagramexport/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     3001 2022-03-19 00:35:34.895047 gaphor-2.9.2/gaphor/plugins/diagramexport/__pycache__/gaphorconvert.cpython-310.pyc
+-rwxr-xr-x   0        0        0     3672 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/diagramexport/gaphorconvert.py
+-rw-r--r--   0        0        0     1479 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/xmiexport/__init__.py
+-rw-r--r--   0        0        0     1782 2022-03-19 00:35:33.743030 gaphor-2.9.2/gaphor/plugins/xmiexport/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     6968 2022-03-19 00:35:33.747030 gaphor-2.9.2/gaphor/plugins/xmiexport/__pycache__/exportmodel.cpython-310.pyc
+-rw-r--r--   0        0        0     8695 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/plugins/xmiexport/exportmodel.py
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/py.typed
+-rw-r--r--   0        0        0        0 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/__init__.py
+-rw-r--r--   0        0        0      139 2022-03-19 00:35:28.950949 gaphor-2.9.2/gaphor/services/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2842 2022-03-19 00:35:28.954949 gaphor-2.9.2/gaphor/services/__pycache__/componentregistry.cpython-310.pyc
+-rw-r--r--   0        0        0     4928 2022-03-19 00:35:33.791031 gaphor-2.9.2/gaphor/services/__pycache__/copyservice.cpython-310.pyc
+-rw-r--r--   0        0        0     3985 2022-03-19 00:35:33.559027 gaphor-2.9.2/gaphor/services/__pycache__/modelinglanguage.cpython-310.pyc
+-rw-r--r--   0        0        0     5505 2022-03-19 00:35:33.559027 gaphor-2.9.2/gaphor/services/__pycache__/properties.cpython-310.pyc
+-rw-r--r--   0        0        0    14316 2022-03-19 00:35:29.498960 gaphor-2.9.2/gaphor/services/__pycache__/undomanager.cpython-310.pyc
+-rw-r--r--   0        0        0     1568 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/componentregistry.py
+-rw-r--r--   0        0        0     4817 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/copyservice.py
+-rw-r--r--   0        0        0     1407 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/helpservice/__init__.py
+-rw-r--r--   0        0        0     1862 2022-03-19 00:35:35.779059 gaphor-2.9.2/gaphor/services/helpservice/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     2288 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/helpservice/about.ui
+-rw-r--r--   0        0        0     8276 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/helpservice/shortcuts.ui
+-rw-r--r--   0        0        0     3107 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/modelinglanguage.py
+-rw-r--r--   0        0        0     4795 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/properties.py
+-rw-r--r--   0        0        0    14918 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/services/undomanager.py
+-rw-r--r--   0        0        0       61 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/storage/__init__.py
+-rw-r--r--   0        0        0      204 2022-03-19 00:35:29.326957 gaphor-2.9.2/gaphor/storage/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0    11942 2022-03-19 00:35:29.330957 gaphor-2.9.2/gaphor/storage/__pycache__/parser.cpython-310.pyc
+-rw-r--r--   0        0        0    10220 2022-03-19 00:35:29.326957 gaphor-2.9.2/gaphor/storage/__pycache__/storage.cpython-310.pyc
+-rw-r--r--   0        0        0     3039 2022-03-19 00:35:29.334957 gaphor-2.9.2/gaphor/storage/__pycache__/upgrade_canvasitem.cpython-310.pyc
+-rw-r--r--   0        0        0     4802 2022-03-19 00:35:29.334957 gaphor-2.9.2/gaphor/storage/__pycache__/xmlwriter.cpython-310.pyc
+-rw-r--r--   0        0        0    12167 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/storage/parser.py
+-rw-r--r--   0        0        0    12972 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/storage/storage.py
+-rw-r--r--   0        0        0     3827 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/storage/upgrade_canvasitem.py
+-rw-r--r--   0        0        0     4707 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/storage/xmlwriter.py
+-rw-r--r--   0        0        0      564 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/templates/blank.gaphor
+-rw-r--r--   0        0        0     1933 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/templates/c4model.gaphor
+-rw-r--r--   0        0        0    24556 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/templates/raaml.gaphor
+-rw-r--r--   0        0        0    79653 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/templates/sysml.gaphor
+-rw-r--r--   0        0        0    57894 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/templates/uml.gaphor
+-rw-r--r--   0        0        0     5025 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/transaction.py
+-rw-r--r--   0        0        0     5883 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/__init__.py
+-rw-r--r--   0        0        0     5494 2022-03-19 00:35:28.838946 gaphor-2.9.2/gaphor/ui/__pycache__/__init__.cpython-310.pyc
+-rw-r--r--   0        0        0     1130 2022-03-19 00:35:33.719030 gaphor-2.9.2/gaphor/ui/__pycache__/abc.cpython-310.pyc
+-rw-r--r--   0        0        0     5144 2022-03-19 00:35:28.954949 gaphor-2.9.2/gaphor/ui/__pycache__/actiongroup.cpython-310.pyc
+-rw-r--r--   0        0        0     2006 2022-03-19 00:35:50.503272 gaphor-2.9.2/gaphor/ui/__pycache__/appfilemanager.cpython-310.pyc
+-rw-r--r--   0        0        0    10609 2022-03-19 00:35:34.555042 gaphor-2.9.2/gaphor/ui/__pycache__/diagrampage.cpython-310.pyc
+-rw-r--r--   0        0        0    11691 2022-03-19 00:35:34.663043 gaphor-2.9.2/gaphor/ui/__pycache__/diagrams.cpython-310.pyc
+-rw-r--r--   0        0        0    11505 2022-03-19 00:35:34.563042 gaphor-2.9.2/gaphor/ui/__pycache__/elementeditor.cpython-310.pyc
+-rw-r--r--   0        0        0     1300 2022-03-19 00:35:34.859046 gaphor-2.9.2/gaphor/ui/__pycache__/errorhandler.cpython-310.pyc
+-rw-r--r--   0        0        0     1441 2022-03-19 00:35:33.795031 gaphor-2.9.2/gaphor/ui/__pycache__/event.cpython-310.pyc
+-rw-r--r--   0        0        0     2175 2022-03-19 00:35:33.747030 gaphor-2.9.2/gaphor/ui/__pycache__/filedialog.cpython-310.pyc
+-rw-r--r--   0        0        0     9515 2022-03-19 00:35:34.855046 gaphor-2.9.2/gaphor/ui/__pycache__/filemanager.cpython-310.pyc
+-rw-r--r--   0        0        0     6468 2022-03-19 00:35:34.571042 gaphor-2.9.2/gaphor/ui/__pycache__/greeter.cpython-310.pyc
+-rw-r--r--   0        0        0     3787 2022-03-19 00:35:34.711044 gaphor-2.9.2/gaphor/ui/__pycache__/layout.cpython-310.pyc
+-rw-r--r--   0        0        0      955 2022-03-19 00:35:28.958949 gaphor-2.9.2/gaphor/ui/__pycache__/macosshim.cpython-310.pyc
+-rw-r--r--   0        0        0     8493 2022-03-19 00:35:34.711044 gaphor-2.9.2/gaphor/ui/__pycache__/mainwindow.cpython-310.pyc
+-rw-r--r--   0        0        0     1527 2022-03-19 00:35:33.715030 gaphor-2.9.2/gaphor/ui/__pycache__/menufragment.cpython-310.pyc
+-rw-r--r--   0        0        0    10671 2022-03-19 00:35:34.711044 gaphor-2.9.2/gaphor/ui/__pycache__/namespace.cpython-310.pyc
+-rw-r--r--   0        0        0     9654 2022-03-19 00:35:34.715044 gaphor-2.9.2/gaphor/ui/__pycache__/namespacemodel.cpython-310.pyc
+-rw-r--r--   0        0        0     4425 2022-03-19 00:35:34.719044 gaphor-2.9.2/gaphor/ui/__pycache__/namespaceview.cpython-310.pyc
+-rw-r--r--   0        0        0     1353 2022-03-19 00:35:34.715044 gaphor-2.9.2/gaphor/ui/__pycache__/notification.cpython-310.pyc
+-rw-r--r--   0        0        0     1515 2022-03-19 00:35:50.503272 gaphor-2.9.2/gaphor/ui/__pycache__/questiondialog.cpython-310.pyc
+-rw-r--r--   0        0        0     1896 2022-03-19 00:35:34.791045 gaphor-2.9.2/gaphor/ui/__pycache__/recentfiles.cpython-310.pyc
+-rw-r--r--   0        0        0     4230 2022-03-19 00:35:34.795045 gaphor-2.9.2/gaphor/ui/__pycache__/statuswindow.cpython-310.pyc
+-rw-r--r--   0        0        0     1852 2022-03-19 00:35:29.546961 gaphor-2.9.2/gaphor/ui/__pycache__/styling.cpython-310.pyc
+-rw-r--r--   0        0        0    10477 2022-03-19 00:35:34.663043 gaphor-2.9.2/gaphor/ui/__pycache__/toolbox.cpython-310.pyc
+-rw-r--r--   0        0        0      687 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/abc.py
+-rw-r--r--   0        0        0     5764 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/actiongroup.py
+-rw-r--r--   0        0        0     1794 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/appfilemanager.py
+-rw-r--r--   0        0        0    13061 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/diagrampage.py
+-rw-r--r--   0        0        0    12665 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/diagrams.py
+-rw-r--r--   0        0        0    18174 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/elementeditor.glade
+-rw-r--r--   0        0        0    11364 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/elementeditor.py
+-rw-r--r--   0        0        0    13309 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/elementeditor.ui
+-rw-r--r--   0        0        0     1243 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/errorhandler.py
+-rw-r--r--   0        0        0      614 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/event.py
+-rw-r--r--   0        0        0     2358 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/filedialog.py
+-rw-r--r--   0        0        0    10526 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/filemanager.py
+-rw-r--r--   0        0        0     1002 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/greeter-model-template.glade
+-rw-r--r--   0        0        0     1029 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/greeter-model-template.ui
+-rw-r--r--   0        0        0     2466 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/greeter-recent-file.glade
+-rw-r--r--   0        0        0     1925 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/greeter-recent-file.ui
+-rw-r--r--   0        0        0     6053 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/greeter.glade
+-rw-r--r--   0        0        0     6788 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/greeter.py
+-rw-r--r--   0        0        0     5994 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/greeter.ui
+-rw-r--r--   0        0        0     2214 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/Makefile
+-rw-r--r--   0        0        0     2716 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-abstract-operational-situation-symbolic.svg
+-rw-r--r--   0        0        0     1677 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-accept-event-action-symbolic.svg
+-rw-r--r--   0        0        0     1979 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-action-symbolic.svg
+-rw-r--r--   0        0        0     2220 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-final-node-symbolic.svg
+-rw-r--r--   0        0        0     2185 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-partition-symbolic.svg
+-rw-r--r--   0        0        0     2978 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-symbolic.svg
+-rw-r--r--   0        0        0     2825 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actor-symbolic.svg
+-rw-r--r--   0        0        0     1892 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actuator-symbolic.svg
+-rw-r--r--   0        0        0     2772 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-and-symbolic.svg
+-rw-r--r--   0        0        0     2506 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-artifact-symbolic.svg
+-rw-r--r--   0        0        0     2611 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-association-symbolic.svg
+-rw-r--r--   0        0        0     1659 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-basic-event-symbolic.svg
+-rw-r--r--   0        0        0     2369 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-behavior-execution-specification-symbolic.svg
+-rw-r--r--   0        0        0     2671 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-block-symbolic.svg
+-rw-r--r--   0        0        0     1603 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-box-symbolic.svg
+-rw-r--r--   0        0        0     2924 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-component-symbolic.svg
+-rw-r--r--   0        0        0     2659 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-container-symbolic.svg
+-rw-r--r--   0        0        0     4054 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-database-symbolic.svg
+-rw-r--r--   0        0        0     3418 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-person-symbolic.svg
+-rw-r--r--   0        0        0     4448 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-software-system-symbolic.svg
+-rw-r--r--   0        0        0     1934 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-class-symbolic.svg
+-rw-r--r--   0        0        0     1796 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-line-symbolic.svg
+-rw-r--r--   0        0        0     1833 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-symbolic.svg
+-rw-r--r--   0        0        0     3503 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-component-symbolic.svg
+-rw-r--r--   0        0        0     2651 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-composite-association-symbolic.svg
+-rw-r--r--   0        0        0     1881 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-conditional-event-symbolic.svg
+-rw-r--r--   0        0        0     2508 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-connector-symbolic.svg
+-rw-r--r--   0        0        0     1261 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-constraint-symbolic.svg
+-rw-r--r--   0        0        0     2381 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-containment-symbolic.svg
+-rw-r--r--   0        0        0     2679 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-action-symbolic.svg
+-rw-r--r--   0        0        0     2313 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-flow-symbolic.svg
+-rw-r--r--   0        0        0     3334 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-structure-symbolic.svg
+-rw-r--r--   0        0        0     2866 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controlled-process-symbolic.svg
+-rw-r--r--   0        0        0     2276 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controller-symbolic.svg
+-rw-r--r--   0        0        0     2435 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-data-type-symbolic.svg
+-rw-r--r--   0        0        0     1682 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-decision-node-symbolic.svg
+-rw-r--r--   0        0        0     3060 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dependency-symbolic.svg
+-rw-r--r--   0        0        0     3370 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-derive-symbolic.svg
+-rw-r--r--   0        0        0     3694 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-device-symbolic.svg
+-rw-r--r--   0        0        0     2695 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-diagram-symbolic.svg
+-rw-r--r--   0        0        0     2239 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dormant-event-symbolic.svg
+-rw-r--r--   0        0        0     1898 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-ellipse-symbolic.svg
+-rw-r--r--   0        0        0     2268 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-enumeration-symbolic.svg
+-rw-r--r--   0        0        0     2363 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-execution-specification-symbolic.svg
+-rw-r--r--   0        0        0     3065 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extend-symbolic.svg
+-rw-r--r--   0        0        0     1678 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extension-symbolic.svg
+-rw-r--r--   0        0        0     2234 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-final-state-symbolic.svg
+-rw-r--r--   0        0        0     2201 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-flow-final-node-symbolic.svg
+-rw-r--r--   0        0        0     2011 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-fork-node-symbolic.svg
+-rw-r--r--   0        0        0     1968 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-generalization-symbolic.svg
+-rw-r--r--   0        0        0     1855 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-hazard-symbolic.svg
+-rw-r--r--   0        0        0     1524 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-house-event-symbolic.svg
+-rw-r--r--   0        0        0     2866 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-import-symbolic.svg
+-rw-r--r--   0        0        0     2801 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-include-symbolic.svg
+-rw-r--r--   0        0        0     3715 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-information-flow-symbolic.svg
+-rw-r--r--   0        0        0     2975 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-inhibit-symbolic.svg
+-rw-r--r--   0        0        0     1215 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-node-symbolic.svg
+-rw-r--r--   0        0        0     1223 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-pseudostate-symbolic.svg
+-rw-r--r--   0        0        0     2525 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interaction-symbolic.svg
+-rw-r--r--   0        0        0     2218 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-realization-symbolic.svg
+-rw-r--r--   0        0        0     2164 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-symbolic.svg
+-rw-r--r--   0        0        0     2279 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-intermediate-event-symbolic.svg
+-rw-r--r--   0        0        0     1786 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-item-flow-symbolic.svg
+-rw-r--r--   0        0        0     2029 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-join-node-symbolic.svg
+-rw-r--r--   0        0        0     2342 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-lifeline-symbolic.svg
+-rw-r--r--   0        0        0     1234 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-line-symbolic.svg
+-rw-r--r--   0        0        0     1789 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-loss-symbolic.svg
+-rw-r--r--   0        0        0     2207 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-magnet-symbolic.svg
+-rw-r--r--   0        0        0     3286 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-majority_vote-symbolic.svg
+-rw-r--r--   0        0        0     2365 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-message-symbolic.svg
+-rw-r--r--   0        0        0     2435 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-metaclass-symbolic.svg
+-rw-r--r--   0        0        0     2993 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-new-diagram-symbolic.svg
+-rw-r--r--   0        0        0     2922 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-node-symbolic.svg
+-rw-r--r--   0        0        0     1703 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-not-symbolic.svg
+-rw-r--r--   0        0        0     2357 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-flow-symbolic.svg
+-rw-r--r--   0        0        0     1823 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-node-symbolic.svg
+-rw-r--r--   0        0        0     2590 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-operational-situation-symbolic.svg
+-rw-r--r--   0        0        0     2120 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-or-symbolic.svg
+-rw-r--r--   0        0        0     2381 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-package-symbolic.svg
+-rw-r--r--   0        0        0     1908 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pointer-symbolic.svg
+-rw-r--r--   0        0        0     2985 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-primitive-symbolic.svg
+-rw-r--r--   0        0        0     4242 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-profile-symbolic.svg
+-rw-r--r--   0        0        0     2360 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-property-symbolic.svg
+-rw-r--r--   0        0        0     1978 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-proxyport-symbolic.svg
+-rw-r--r--   0        0        0     2542 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pseudostate-symbolic.svg
+-rw-r--r--   0        0        0     2783 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-realization-symbolic.svg
+-rw-r--r--   0        0        0     3379 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-refine-symbolic.svg
+-rw-r--r--   0        0        0     2045 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-reflexive-message-symbolic.svg
+-rw-r--r--   0        0        0     1499 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-region-symbolic.svg
+-rw-r--r--   0        0        0     3353 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-relevant-to-symbolic.svg
+-rw-r--r--   0        0        0     2354 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-requirement-symbolic.svg
+-rw-r--r--   0        0        0     3980 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-satisfy-symbolic.svg
+-rw-r--r--   0        0        0     1740 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-send-signal-action-symbolic.svg
+-rw-r--r--   0        0        0     3326 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-seq-symbolic.svg
+-rw-r--r--   0        0        0     2897 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-shared-association-symbolic.svg
+-rw-r--r--   0        0        0     2569 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-situation-symbolic.svg
+-rw-r--r--   0        0        0     2641 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-machine-symbolic.svg
+-rw-r--r--   0        0        0     1443 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-symbolic.svg
+-rw-r--r--   0        0        0     3656 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-stereotype-symbolic.svg
+-rw-r--r--   0        0        0     2226 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-top-event-symbolic.svg
+-rw-r--r--   0        0        0     3171 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-trace-symbolic.svg
+-rw-r--r--   0        0        0     1392 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-in-symbolic.svg
+-rw-r--r--   0        0        0     1776 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-out-symbolic.svg
+-rw-r--r--   0        0        0     1662 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transition-symbolic.svg
+-rw-r--r--   0        0        0     1542 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-undeveloped-event-symbolic.svg
+-rw-r--r--   0        0        0     2421 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-unsafe-control-action-symbolic.svg
+-rw-r--r--   0        0        0     2666 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-usage-symbolic.svg
+-rw-r--r--   0        0        0     2304 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-use-case-symbolic.svg
+-rw-r--r--   0        0        0     2205 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-value-type-symbolic.svg
+-rw-r--r--   0        0        0     3131 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-verify-symbolic.svg
+-rw-r--r--   0        0        0     2116 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-view-editor-symbolic.svg
+-rw-r--r--   0        0        0     4066 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-xor-symbolic.svg
+-rw-r--r--   0        0        0     2342 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-zero-event-symbolic.svg
+-rw-r--r--   0        0        0     6198 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/apps/org.gaphor.Gaphor.svg
+-rw-r--r--   0        0        0     3217 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/C4Model.svg
+-rw-r--r--   0        0        0    39395 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/RAAML.svg
+-rw-r--r--   0        0        0     6459 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/SysML.svg
+-rw-r--r--   0        0        0     3846 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/UML.svg
+-rw-r--r--   0        0        0   263403 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/icons/stensil.svg
+-rw-r--r--   0        0        0     4052 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/layout.py
+-rw-r--r--   0        0        0      455 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/layout.xml
+-rw-r--r--   0        0        0      836 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/macosshim.py
+-rw-r--r--   0        0        0     8211 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/mainwindow.glade
+-rw-r--r--   0        0        0     9761 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/mainwindow.py
+-rw-r--r--   0        0        0     3896 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/mainwindow.ui
+-rw-r--r--   0        0        0      837 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/menufragment.py
+-rw-r--r--   0        0        0    12389 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/namespace.py
+-rw-r--r--   0        0        0    10409 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/namespacemodel.py
+-rw-r--r--   0        0        0     5541 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/namespaceview.py
+-rw-r--r--   0        0        0      977 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/notification.py
+-rw-r--r--   0        0        0     1087 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/placement-icon-base.png
+-rw-r--r--   0        0        0     1082 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/questiondialog.py
+-rw-r--r--   0        0        0     1470 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/recentfiles.py
+-rw-r--r--   0        0        0     4261 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/statuswindow.py
+-rw-r--r--   0        0        0      151 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/styling-gtk3.css
+-rw-r--r--   0        0        0       98 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/styling-gtk4.css
+-rw-r--r--   0        0        0     1023 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/styling.css
+-rw-r--r--   0        0        0     1800 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/styling.py
+-rw-r--r--   0        0        0    12140 2022-03-18 23:52:22.000000 gaphor-2.9.2/gaphor/ui/toolbox.py
+-rw-r--r--   0        0        0     7936 2022-03-18 23:52:22.000000 gaphor-2.9.2/pyproject.toml
+-rw-r--r--   0        0        0    41854 2022-03-19 00:37:02.641906 gaphor-2.9.2/setup.py
+-rw-r--r--   0        0        0    37731 2022-03-19 00:37:02.643689 gaphor-2.9.2/PKG-INFO
```

### Comparing `gaphor-2.9.1/LICENSE.txt` & `gaphor-2.9.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/README.md` & `gaphor-2.9.2/README.md`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/__pycache__/c4model.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/__pycache__/c4model.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1455 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 14% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 af05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 af05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0173 d800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d08 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6403 6c0d 6d0e 5a0e 0100 4700  ..d.d.l.m.Z...G.
 00000070: 6404 6405 8400 6405 650e 8303 5a0f 6400  d.d...d.e...Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/__pycache__/iconname.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/__pycache__/iconname.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 550 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 25% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2602 0000  o.......C.3b&...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2602 0000  o.......6.5b&...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 4800 0000 6400  .....@...sH...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 0100 6505  d.l.m.Z.m.Z...e.
 00000050: a006 6501 a101 6403 6404 8400 8301 5a07  ..e...d.d.....Z.
 00000060: 6505 a006 6502 a101 6405 6406 8400 8301  e...e...d.d.....
 00000070: 5a08 6407 5300 2908 e900 0000 0029 02da  Z.d.S.)......)..
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/__pycache__/modelinglanguage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/__pycache__/modelinglanguage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 970 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ca03 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ca03 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 7c00 0000 6400  .....@...s|...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a04 6401 6403 6c05 5a04 6401  d.l.Z.d.d.l.Z.d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 0100 6401 6407 6c0e  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/__pycache__/propertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/__pycache__/propertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2487 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 b709 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 b709 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 8800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 6d09 5a09 0100 6509 6405 8301 5a0a 6508  m.Z...e.d...Z.e.
 00000070: a00b 6503 6a0c a101 6508 a00b 6503 6a0d  ..e.j...e...e.j.
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/__pycache__/toolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/__pycache__/toolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4118 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1610 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1610 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0010 0000 0040 0000 0073 2402 0000 5500  .....@...s$...U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 6d04 5a04 0100 6401 6404  d.d.l.m.Z...d.d.
 00000050: 6c05 6d06 5a06 6d07 5a07 0100 6401 6405  l.m.Z.m.Z...d.d.
 00000060: 6c08 6d09 5a09 0100 6401 6406 6c0a 6d0b  l.m.Z...d.d.l.m.
 00000070: 5a0b 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f  Z.m.Z.m.Z.m.Z.m.
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/c4model.py` & `gaphor-2.9.2/gaphor/C4Model/c4model.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/diagramitems/__pycache__/container.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/diagramitems/__pycache__/container.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2020 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 e407 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 e407 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 7c00 0000 6400  .....@...s|...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 6d07 5a07 0100 6400 6404 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6400 6405 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 0100 6400  m.Z.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/diagramitems/__pycache__/database.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/diagramitems/__pycache__/database.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2243 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c308 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c308 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9000 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 6d09 5a09 0100 6400 6405 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 6d0c 5a0c 0100 6400 6406 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/diagramitems/__pycache__/person.cpython-310.pyc` & `gaphor-2.9.2/gaphor/C4Model/diagramitems/__pycache__/person.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2266 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 da08 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 da08 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9000 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 6d09 5a09 0100 6400 6405 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 6d0c 5a0c 0100 6400 6406 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/C4Model/diagramitems/container.py` & `gaphor-2.9.2/gaphor/C4Model/diagramitems/container.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/diagramitems/database.py` & `gaphor-2.9.2/gaphor/C4Model/diagramitems/database.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/diagramitems/person.py` & `gaphor-2.9.2/gaphor/C4Model/diagramitems/person.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/iconname.py` & `gaphor-2.9.2/gaphor/C4Model/iconname.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/modelinglanguage.py` & `gaphor-2.9.2/gaphor/C4Model/modelinglanguage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/propertypages.glade` & `gaphor-2.9.2/gaphor/C4Model/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/propertypages.py` & `gaphor-2.9.2/gaphor/C4Model/propertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/propertypages.ui` & `gaphor-2.9.2/gaphor/C4Model/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/C4Model/toolbox.py` & `gaphor-2.9.2/gaphor/C4Model/toolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/__pycache__/modelinglanguage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/__pycache__/modelinglanguage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 965 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c503 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c503 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 7400 0000 6400  .....@...st...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a04 6401 6404 6c05 6d06 5a06  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6401 6405 6c07 6d08 5a08 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c09 6d0a 5a0a 6d0b 5a0b 0100 6401  d.l.m.Z.m.Z...d.
 00000070: 6407 6c0c 6d0d 5a0d 6d0e 5a0e 0100 6401  d.l.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/__pycache__/raaml.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/__pycache__/raaml.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7305 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 891c 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 891c 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0173 a607 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d08 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6403 6c0d 6d0e 5a0e 0100 6400  ..d.d.l.m.Z...d.
 00000070: 6404 6c0f 6d10 5a10 0100 4700 6405 6406  d.l.m.Z...G.d.d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/__pycache__/toolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/__pycache__/toolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 547 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2302 0000  o.......C.3b#...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2302 0000  o.......6.5b#...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 8400 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 6d03  d.Z.d.d.l.m.Z.m.
 00000040: 5a03 6d04 5a04 6d05 5a05 0100 6401 6403  Z.m.Z.m.Z...d.d.
 00000050: 6c06 6d07 5a07 0100 6401 6404 6c08 6d09  l.m.Z...d.d.l.m.
 00000060: 5a09 0100 6401 6405 6c0a 6d0b 5a0b 0100  Z...d.d.l.m.Z...
 00000070: 6505 6509 650b 6603 5a0c 6504 650d 6406  e.e.e.f.Z.e.e.d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/and.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/and.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/dormant_event.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/dormant_event.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/inhibit.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/inhibit.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/majority_vote.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/majority_vote.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/not.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/not.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/or.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/or.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/seq.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/seq.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/xor.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/xor.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/diagram_svgs/zero_event.svg` & `gaphor-2.9.2/gaphor/RAAML/diagram_svgs/zero_event.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__init__.py` & `gaphor-2.9.2/gaphor/RAAML/fta/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 927 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9f03 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9f03 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 d000 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6405 6c08 6d09 5a09 0100 6400 6406 6c0a  d.l.m.Z...d.d.l.
 00000070: 6d0b 5a0b 0100 6400 6407 6c0c 6d0d 5a0d  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/andgate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/andgate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2616 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 380a 0000  o.......C.3b8...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 380a 0000  o.......6.5b8...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/basicevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/basicevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1951 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9f07 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9f07 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d200 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/conditionalevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/conditionalevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1517 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ed05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ed05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9800 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 0100 6401 6404 6c07 6d08 5a08 6d09 5a09  ..d.d.l.m.Z.m.Z.
 00000060: 6d0a 5a0a 0100 6401 6405 6c0b 6d0c 5a0c  m.Z...d.d.l.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 6d0f 5a0f  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/dormantevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/dormantevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1900 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6c07 0000  o.......C.3bl...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6c07 0000  o.......6.5bl...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 c600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/ftatoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/ftatoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 6880 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 e01a 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 e01a 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 001f 0000 0040 0000 0073 6a03 0000 6400  .....@...sj...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 6d07 5a07 0100 6401 6404 6c08 6d09 5a09  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6405 6c0a 6d0b 5a0b 6d0c 5a0c  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0b 5a0e 0100 6505  ..d.d.l.m.Z...e.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/houseevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/houseevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2048 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0008 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0008 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 ca00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/inhibitgate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/inhibitgate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2674 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 720a 0000  o.......C.3br...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 720a 0000  o.......6.5br...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 c600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/intermediateevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/intermediateevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1776 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 f006 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 f006 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 b600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 0100 6401  m.Z.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/majorityvotegate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/majorityvotegate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3389 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3d0d 0000  o.......C.3b=...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3d0d 0000  o.......6.5b=...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 e200 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6404 6c04 6d05 5a05  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a09 0100 6401 6407 6c0a  d.l.m.Z...d.d.l.
 00000070: 6d0b 5a0b 6d0c 5a0c 6d0d 5a0d 0100 6401  m.Z.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/notgate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/notgate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1886 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5e07 0000  o.......C.3b^...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5e07 0000  o.......6.5b^...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 ca00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/orgate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/orgate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3254 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 b60c 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 b60c 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/seqgate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/seqgate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2128 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5008 0000  o.......C.3bP...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5008 0000  o.......6.5bP...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/topevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/topevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1676 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8c06 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8c06 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 b600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 0100 6401  m.Z.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/transferin.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/transferin.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1874 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5207 0000  o.......C.3bR...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5207 0000  o.......6.5bR...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 c600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/transferout.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/transferout.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1921 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8107 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8107 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d200 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/undevelopedevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/undevelopedevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1858 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4207 0000  o.......C.3bB...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4207 0000  o.......6.5bB...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 ca00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/xorgate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/xorgate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2139 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5b08 0000  o.......C.3b[...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5b08 0000  o.......6.5b[...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/__pycache__/zeroevent.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/fta/__pycache__/zeroevent.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2004 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d407 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d407 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/andgate.py` & `gaphor-2.9.2/gaphor/RAAML/fta/andgate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/basicevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/basicevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/conditionalevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/conditionalevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/dormantevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/dormantevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/ftatoolbox.py` & `gaphor-2.9.2/gaphor/RAAML/fta/ftatoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/houseevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/houseevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/inhibitgate.py` & `gaphor-2.9.2/gaphor/RAAML/fta/inhibitgate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/intermediateevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/intermediateevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/majorityvotegate.py` & `gaphor-2.9.2/gaphor/RAAML/fta/majorityvotegate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/notgate.py` & `gaphor-2.9.2/gaphor/RAAML/fta/notgate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/orgate.py` & `gaphor-2.9.2/gaphor/RAAML/fta/orgate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/seqgate.py` & `gaphor-2.9.2/gaphor/RAAML/fta/seqgate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/topevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/topevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/transferin.py` & `gaphor-2.9.2/gaphor/RAAML/fta/transferin.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/transferout.py` & `gaphor-2.9.2/gaphor/RAAML/fta/transferout.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/undevelopedevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/undevelopedevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/xorgate.py` & `gaphor-2.9.2/gaphor/RAAML/fta/xorgate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/fta/zeroevent.py` & `gaphor-2.9.2/gaphor/RAAML/fta/zeroevent.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/modelinglanguage.py` & `gaphor-2.9.2/gaphor/RAAML/modelinglanguage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/raaml.py` & `gaphor-2.9.2/gaphor/RAAML/raaml.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 481 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 18% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 e101 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 e101 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 4400 0000 6400  .....@...sD...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6405 6c08 5a09 6700 6406 a201 5a0a 6405  d.l.Z.g.d...Z.d.
 00000070: 5300 2907 e900 0000 0029 01da 1143 6f6e  S.)......)...Con
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/connectors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/connectors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 423 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 14% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a701 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a701 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 5c00 0000 6400  .....@...s\...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6405 6c08 6d09 5a09 0100 6501 a00a 6503  d.l.m.Z...e...e.
 00000070: 6507 a102 4700 6406 6407 8400 6407 6509  e...G.d.d...d.e.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/controlaction.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/controlaction.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1752 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d806 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d806 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 b600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6401  m.Z.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/operationalsituation.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/operationalsituation.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1842 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3207 0000  o.......C.3b2...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3207 0000  o.......6.5b2...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 c000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6401  m.Z.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/relationships.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/relationships.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 292 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2401 0000  o.......C.3b$...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2401 0000  o.......6.5b$...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 4200 0000 6400  .....@...sB...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6501 6503 6a06 8301 4700 6404 6405  ..e.e.j...G.d.d.
 00000060: 8400 6405 6505 8303 8301 5a07 6406 5300  ..d.e.....Z.d.S.
 00000070: 2907 e900 0000 0029 01da 0a72 6570 7265  )......)...repre
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/stpatoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/stpatoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4949 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5513 0000  o.......C.3bU...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5513 0000  o.......6.5bU...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0018 0000 0040 0000 0073 1202 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 0100 6401  m.Z.m.Z.m.Z...d.
 00000050: 6403 6c07 6d08 5a08 0100 6401 6404 6c09  d.l.m.Z...d.d.l.
 00000060: 6d0a 5a0a 6d0b 5a0b 0100 6401 6405 6c0c  m.Z.m.Z...d.d.l.
 00000070: 6d0a 5a0d 0100 6401 6405 6c0e 6d0a 5a0f  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/__pycache__/unsafecontrolaction.cpython-310.pyc` & `gaphor-2.9.2/gaphor/RAAML/stpa/__pycache__/unsafecontrolaction.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1792 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0007 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0007 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 b600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6401  m.Z.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/controlaction.py` & `gaphor-2.9.2/gaphor/RAAML/stpa/controlaction.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/operationalsituation.py` & `gaphor-2.9.2/gaphor/RAAML/stpa/operationalsituation.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/stpatoolbox.py` & `gaphor-2.9.2/gaphor/RAAML/stpa/stpatoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/stpa/unsafecontrolaction.py` & `gaphor-2.9.2/gaphor/RAAML/stpa/unsafecontrolaction.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/RAAML/toolbox.py` & `gaphor-2.9.2/gaphor/RAAML/toolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/__pycache__/modelinglanguage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/__pycache__/modelinglanguage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 965 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c503 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c503 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 7400 0000 6400  .....@...st...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a04 6401 6404 6c05 6d06 5a06  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6401 6405 6c07 6d08 5a08 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c09 6d0a 5a0a 6d0b 5a0b 0100 6401  d.l.m.Z.m.Z...d.
 00000070: 6407 6c0c 6d0d 5a0d 6d0e 5a0e 0100 6401  d.l.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/__pycache__/propertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/__pycache__/propertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 8133 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c51f 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c51f 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 fa00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6400  m.Z.m.Z.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6400 6405 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6400 6406 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/__pycache__/sysml.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/__pycache__/sysml.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 9055 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5f23 0000  o.......C.3b_#..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5f23 0000  o.......6.5b_#..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0173 2607 0000 6400  .....@...s&...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d08 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6403 6c0d 6d0e 5a0e 0100 4700  ..d.d.l.m.Z...G.
 00000070: 6404 6405 8400 6405 650e 8303 5a0f 6400  d.d...d.e...Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/__pycache__/toolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/__pycache__/toolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2391 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5709 0000  o.......C.3bW...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5709 0000  o.......6.5bW...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000d 0000 0040 0000 0073 b001 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 6d04 5a04 0100 6401 6404  d.d.l.m.Z...d.d.
 00000050: 6c05 6d06 5a06 6d07 5a07 6d08 5a08 6d09  l.m.Z.m.Z.m.Z.m.
 00000060: 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c 6d0d  Z.m.Z.m.Z.m.Z.m.
 00000070: 5a0d 0100 6401 6405 6c0e 6d0f 5a10 0100  Z...d.d.l.m.Z...
```

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/block.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/block.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5336 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d814 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d814 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000a 0000 0040 0000 0073 fa00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 6d07 5a07 0100 6400 6404 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 6d0d 5a0d 6d0e 5a0e 0100 6400 6405 6c0f  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/blockstoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/blockstoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3450 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7a0d 0000  o.......C.3bz...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7a0d 0000  o.......6.5bz...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0014 0000 0040 0000 0073 a601 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0e 0100 6401 6407 6c0c  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/connectors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/connectors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2846 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1e0b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1e0b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 c600 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 0100 6400 6405 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/property.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/property.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2561 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 010a 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 010a 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 aa00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 0100 6401 6403 6c04 6d05 5a05 0100 6401  ..d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 0100 6401 6407 6c0e  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/__pycache__/proxyport.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/blocks/__pycache__/proxyport.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4360 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0811 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0811 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 dc00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 0100 6400  m.Z.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 0100 6400 6404 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6400 6405 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6400 6406 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/block.py` & `gaphor-2.9.2/gaphor/SysML/blocks/block.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/blockstoolbox.py` & `gaphor-2.9.2/gaphor/SysML/blocks/blockstoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/connectors.py` & `gaphor-2.9.2/gaphor/SysML/blocks/connectors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/group.py` & `gaphor-2.9.2/gaphor/SysML/blocks/group.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/property.py` & `gaphor-2.9.2/gaphor/SysML/blocks/property.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/blocks/proxyport.py` & `gaphor-2.9.2/gaphor/SysML/blocks/proxyport.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/modelinglanguage.py` & `gaphor-2.9.2/gaphor/SysML/modelinglanguage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/propertypages.glade` & `gaphor-2.9.2/gaphor/SysML/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/propertypages.py` & `gaphor-2.9.2/gaphor/SysML/propertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/propertypages.ui` & `gaphor-2.9.2/gaphor/SysML/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/connectors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/connectors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1587 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3306 0000  o.......C.3b3...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3306 0000  o.......6.5b3...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 0401 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 0100 6400 6405 6c0d 6d0e 5a0e 6d0f 5a0f  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/relationships.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/relationships.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1498 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 da05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 da05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 ec00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6400  m.Z.m.Z.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6400 6405 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6400 6406 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/requirement.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/requirement.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4421 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4511 0000  o.......C.3bE...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4511 0000  o.......6.5bE...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 c200 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 6d07 5a07 0100 6400 6404 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 6d0d 5a0d 6d0e 5a0e 0100 6400 6405 6c0f  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/__pycache__/requirementstoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/SysML/requirements/__pycache__/requirementstoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2111 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3f08 0000  o.......C.3b?...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3f08 0000  o.......6.5b?...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000f 0000 0040 0000 0073 1c01 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 6d09 5a09  m.Z.m.Z.m.Z.m.Z.
 00000060: 0100 6401 6405 6c0a 6d0b 5a0c 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6406 6c0a 6d0d 5a0d 0100 6401 6407 6c0e  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/connectors.py` & `gaphor-2.9.2/gaphor/SysML/requirements/connectors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/relationships.py` & `gaphor-2.9.2/gaphor/SysML/requirements/relationships.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/requirement.py` & `gaphor-2.9.2/gaphor/SysML/requirements/requirement.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/requirements/requirementstoolbox.py` & `gaphor-2.9.2/gaphor/SysML/requirements/requirementstoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/sysml.py` & `gaphor-2.9.2/gaphor/SysML/sysml.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/SysML/toolbox.py` & `gaphor-2.9.2/gaphor/SysML/toolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/copypaste.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/copypaste.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1305 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1905 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1905 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 a800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 0100 6400 6405 6c0d 6d0e 5a0e 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/deletable.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/deletable.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 549 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2502 0000  o.......C.3b%...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2502 0000  o.......6.5b%...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6c00 0000 6400  .....@...sl...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 0100 6501  m.Z.m.Z.m.Z...e.
 00000050: 6a06 6403 6503 6404 6507 6604 6405 6406  j.d.e.d.e.f.d.d.
 00000060: 8404 8301 5a08 6501 6a06 6403 6505 6404  ....Z.e.j.d.e.d.
 00000070: 6507 6604 6407 6408 8404 8301 5a09 6501  e.f.d.d.....Z.e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/group.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/group.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 549 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2502 0000  o.......C.3b%...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2502 0000  o.......6.5b%...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7c00 0000 6400  .....@...s|...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6503 a005 6501  m.Z.m.Z...e...e.
 00000050: 6a06 6501 6a07 a102 6503 a005 6501 6a06  j.e.j...e...e.j.
 00000060: 6501 6a06 a102 6403 6508 6602 6404 6405  e.j...d.e.f.d.d.
 00000070: 8404 8301 8301 5a09 6504 a005 6501 6a06  ......Z.e...e.j.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/modelinglanguage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/modelinglanguage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 990 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 de03 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 de03 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 7000 0000 6400  .....@...sp...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 6d0c 5a0c 6d0d 5a0d 0100 6401 6407 6c0e  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/recipes.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/recipes.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 11709 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 bd2d 0000  o.......C.3b.-..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 bd2d 0000  o.......6.5b.-..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 6801 0000 6400  .....@...sh...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 0100 6401  m.Z.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c 6d0d 5a0d  m.Z.m.Z.m.Z.m.Z.
 00000070: 6d0e 5a0e 6d0f 5a0f 6d10 5a10 6d11 5a11  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/sanitizerservice.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/sanitizerservice.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 6041 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9917 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9917 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 9c00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 0100 6401  m.Z.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/toolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/toolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1531 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 fb05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 fb05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000d 0000 0040 0000 0073 4a01 0000 5500  .....@...sJ...U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 6d03  d.Z.d.d.l.m.Z.m.
 00000040: 5a03 6d04 5a04 6d05 5a05 0100 6401 6403  Z.m.Z.m.Z...d.d.
 00000050: 6c06 6d07 5a07 0100 6401 6404 6c08 6d09  l.m.Z...d.d.l.m.
 00000060: 5a09 0100 6401 6405 6c0a 6d0b 5a0b 0100  Z...d.d.l.m.Z...
 00000070: 6401 6406 6c0c 6d0d 5a0d 0100 6401 6407  d.d.l.m.Z...d.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/uml.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/uml.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 64347 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5bfb 0000  o.......C.3b[...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5bfb 0000  o.......6.5b[...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0173 1c2c 0000 6400  .....@...s.,..d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d08 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6403 6c0d 6d0e 5a0e 0100 6400  ..d.d.l.m.Z...d.
 00000070: 6404 6c0f 6d10 5a10 0100 4700 6405 6406  d.l.m.Z...G.d.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/umlfmt.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/umlfmt.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5584 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d015 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d015 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7c01 0000 6400  .....@...s|...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a0a 0100 6501 a00b 6407  d.l.m.Z...e...d.
 00000070: 6501 6a0c 6501 6a0d 4200 a102 5a0e 6408  e.j.e.j.B...Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/umllex.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/umllex.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 9290 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4a24 0000  o.......C.3bJ$..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4a24 0000  o.......6.5bJ$..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 1802 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6702 5a01 6403 6404 6c02  Z.d.d.g.Z.d.d.l.
 00000040: 5a02 6403 6405 6c03 6d04 5a04 0100 6403  Z.d.d.l.m.Z...d.
 00000050: 6406 6c05 6d06 5a06 0100 6407 5a07 6408  d.l.m.Z...d.Z.d.
 00000060: 5a08 6409 5a09 640a 5a0a 640b 5a0b 640c  Z.d.Z.d.Z.d.Z.d.
 00000070: 5a0c 640d 5a0d 640e 5a0e 640f 5a0f 6410  Z.d.Z.d.Z.d.Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/__pycache__/umloverrides.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/__pycache__/umloverrides.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4971 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6b13 0000  o.......C.3bk...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6b13 0000  o.......6.5bk...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0173 0801 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6404 6c04 6d05 5a05  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 0100 6406 6407 8400 5a09 650a 6509 6509  ..d.d...Z.e.e.e.
 00000070: 6a00 6408 8d02 6507 6a0b 5f0c 6422 640d  j.d...e.j._.d"d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__init__.py` & `gaphor-2.9.2/gaphor/UML/actions/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 946 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 b203 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 b203 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 8800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 0100 6400  m.Z.m.Z.m.Z...d.
 00000050: 6402 6c07 6d08 5a08 6d09 5a09 6d0a 5a0a  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6403 6c0b 6d0c 5a0c 6d0d 5a0d  ..d.d.l.m.Z.m.Z.
 00000070: 6d0e 5a0e 6d0f 5a0f 6d10 5a10 6d11 5a11  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/action.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/action.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2844 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1c0b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1c0b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 a800 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 6d0a 5a0a 0100 6401 6405 6c0b 6d0c 5a0c  m.Z...d.d.l.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 650c  ..d.d.l.m.Z...e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionseditors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionseditors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 751 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ef02 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ef02 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 4a00 0000 6400  .....@...sJ...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 0100 6400 6402 6c04 6d05 5a05 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 0100 6501 a008 6507  d.l.m.Z...e...e.
 00000060: a101 6408 6405 6509 6602 6406 6407 8405  ..d.d.e.f.d.d...
 00000070: 8301 5a0a 6404 5300 2909 e900 0000 0029  ..Z.d.S.)......)
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionsgroup.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionsgroup.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 561 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 14% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3102 0000  o.......C.3b1...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3102 0000  o.......6.5b1...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 4c00 0000 6400  .....@...sL...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 0100 6501  d.l.m.Z.m.Z...e.
 00000050: a006 6505 6504 a102 6403 6404 8400 8301  ..e.e...d.d.....
 00000060: 5a07 6502 a006 6505 6504 a102 6405 6406  Z.e...e.e...d.d.
 00000070: 8400 8301 5a08 6407 5300 2908 e900 0000  ....Z.d.S.).....
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionspropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionspropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5406 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1e15 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1e15 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 ee00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 6d07 5a07 6d08 5a08  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6405 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 6508  ..d.d.l.m.Z...e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/actionstoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/actionstoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5796 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a416 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a416 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0019 0000 0040 0000 0073 4c02 0000 6400  .....@...sL...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/activitynodes.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/activitynodes.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 8762 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3a22 0000  o.......C.3b:"..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3a22 0000  o.......6.5b:"..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 a801 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6402 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 5a02 6401 6403 6c03 6d04 5a04 0100 6401  Z.d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 6d07 5a07 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c08 6d09 5a09 6d0a 5a0a 0100 6401  d.l.m.Z.m.Z...d.
 00000070: 6406 6c0b 6d0c 5a0c 0100 6401 6407 6c0d  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/flow.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/flow.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2168 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7808 0000  o.......C.3bx...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7808 0000  o.......6.5bx...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 8800 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6401 6405 6c0a 6d0b 5a0b 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 650b 6502 6a0e  d.l.m.Z...e.e.j.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/flowconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/flowconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 8026 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5a1f 0000  o.......C.3bZ...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5a1f 0000  o.......6.5bZ...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 5001 0000 6400  .....@...sP...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 0100 6401 6403 6c04 6d05 5a05 0100 6401  ..d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 6d0f 5a0f  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/objectnode.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/objectnode.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2465 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a109 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a109 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 aa00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/partition.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/partition.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3409 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 510d 0000  o.......C.3bQ...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 510d 0000  o.......6.5bQ...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 a000 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 6d04 5a04 0100 6401 6404  d.d.l.m.Z...d.d.
 00000050: 6c05 6d06 5a06 0100 6401 6405 6c07 6d08  l.m.Z...d.d.l.m.
 00000060: 5a08 0100 6401 6406 6c09 6d0a 5a0a 0100  Z...d.d.l.m.Z...
 00000070: 6401 6407 6c0b 6d0c 5a0c 0100 6401 6408  d.d.l.m.Z...d.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/__pycache__/partitionpage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/actions/__pycache__/partitionpage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4414 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3e11 0000  o.......C.3b>...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3e11 0000  o.......6.5b>...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7600 0000 6400  .....@...sv...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 650c  ..d.d.l.m.Z...e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/actions/action.py` & `gaphor-2.9.2/gaphor/UML/actions/action.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/actionseditors.py` & `gaphor-2.9.2/gaphor/UML/actions/actionseditors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/actionsgroup.py` & `gaphor-2.9.2/gaphor/UML/actions/actionsgroup.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/actionspropertypages.py` & `gaphor-2.9.2/gaphor/UML/actions/actionspropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/actionstoolbox.py` & `gaphor-2.9.2/gaphor/UML/actions/actionstoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/activitynodes.py` & `gaphor-2.9.2/gaphor/UML/actions/activitynodes.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/flow.py` & `gaphor-2.9.2/gaphor/UML/actions/flow.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/flowconnect.py` & `gaphor-2.9.2/gaphor/UML/actions/flowconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/objectnode.py` & `gaphor-2.9.2/gaphor/UML/actions/objectnode.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/partition.py` & `gaphor-2.9.2/gaphor/UML/actions/partition.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/partitionpage.py` & `gaphor-2.9.2/gaphor/UML/actions/partitionpage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/propertypages.glade` & `gaphor-2.9.2/gaphor/UML/actions/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/actions/propertypages.ui` & `gaphor-2.9.2/gaphor/UML/actions/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__init__.py` & `gaphor-2.9.2/gaphor/UML/classes/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1156 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8404 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8404 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 c000 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d08 5a08 6d09 5a09 0100 6400 6402 6c0a  m.Z.m.Z...d.d.l.
 00000060: 6d0b 5a0b 0100 6400 6403 6c0c 6d0d 5a0d  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6404 6c0e 6d0f 5a0f 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/association.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/association.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 15951 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4f3e 0000  o.......C.3bO>..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4f3e 0000  o.......6.5bO>..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 5601 0000 6400  .....@...sV...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 0100 6401 6403 6c04 6d05 5a05 0100 6401  ..d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/associationpropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/associationpropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 6747 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5b1a 0000  o.......C.3b[...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5b1a 0000  o.......6.5b[...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 8e00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 0100 6400 6405 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/classconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/classconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7069 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9d1b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9d1b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0173 0001 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 6d0e 5a0e 0100 6401  d.l.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/classeseditors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/classeseditors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1922 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8207 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8207 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6a00 0000 6400  .....@...sj...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 0100 6400  d.l.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6404 6c0a 6d0b 5a0b 0100 6400  ..d.d.l.m.Z...d.
 00000070: 6405 6c0c 6d0d 5a0d 0100 6507 a00e 650d  d.l.m.Z...e...e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/classespropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/classespropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 15661 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2d3d 0000  o.......C.3b-=..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2d3d 0000  o.......6.5b-=..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 c801 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 0100 6400 6405 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/classestoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/classestoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4948 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5413 0000  o.......C.3bT...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5413 0000  o.......6.5bT...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0019 0000 0040 0000 0073 3a02 0000 6400  .....@...s:...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6407 650d 6a0e  d.l.m.Z...d.e.j.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/component.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/component.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3046 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 e60b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 e60b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9400 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/containment.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/containment.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 782 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0e03 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0e03 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 4e00 0000 6400  .....@...sN...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 4700 6405 6406  m.Z.m.Z...G.d.d.
 00000060: 8400 6406 6504 8303 5a08 6407 6502 6602  ..d.e...Z.d.e.f.
 00000070: 6408 6409 8404 5a09 640a 5300 290b 7a4b  d.d...Z.d.S.).zK
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/containmentconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/containmentconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3279 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 cf0c 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 cf0c 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7400 0000 6400  .....@...st...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 0100 6401 6406 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/copypaste.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/copypaste.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1127 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 14% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6704 0000  o.......C.3bg...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6704 0000  o.......6.5bg...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 a600 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 6d05 5a05  ..d.d.l.m.Z.m.Z.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 6d09 5a09  m.Z.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6404 6c0a 6d0b 5a0b 0100 6502  ..d.d.l.m.Z...e.
 00000070: a00c 6505 a101 6502 a00c 6506 a101 6502  ..e...e...e...e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/datatype.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/datatype.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3458 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 820d 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 820d 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 e400 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 6d09 5a09 6d0a 5a0a 0100 6400  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0b 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e  d.l.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/dependency.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/dependency.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3664 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 500e 0000  o.......C.3bP...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 500e 0000  o.......6.5bP...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/dependencypropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/dependencypropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2570 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0a0a 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0a0a 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6e00 0000 6400  .....@...sn...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 0100 6400  m.Z.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 0100 6400 6404 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6400 6405 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 6505  ..d.d.l.m.Z...e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/enumeration.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/enumeration.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4080 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 f00f 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 f00f 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 d400 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 6d09 5a09 6d0a 5a0a 6d0b 5a0b  m.Z.m.Z.m.Z.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 6d0e 5a0e  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/enumerationpropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/enumerationpropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2950 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 860b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 860b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 ba00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6405 6c08 6d09 5a09 6d0a 5a0a 6d0b 5a0b  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/generalization.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/generalization.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1020 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 fc03 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 fc03 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7a00 0000 6400  .....@...sz...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6401 6407 6c0c 6d0d 5a0d 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/interface.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/interface.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 12329 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2930 0000  o.......C.3b)0..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2930 0000  o.......6.5b)0..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 3c01 0000 6400  .....@...s<...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a09 6d0a 5a0a 0100 6401  d.l.m.Z.m.Z...d.
 00000070: 6407 6c0b 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e  d.l.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/interfaceconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/interfaceconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2490 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ba09 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ba09 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 8000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6502 a00c 6509 650b a102 4700 6407  ..e...e.e...G.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/interfacerealization.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/interfacerealization.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1585 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3106 0000  o.......C.3b1...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3106 0000  o.......6.5b1...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 8800 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6401 6407 6c0e  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/klass.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/klass.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7026 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 721b 0000  o.......C.3br...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 721b 0000  o.......6.5br...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 fa00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6400 6406 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 6d0b 5a0b 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/package.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/package.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2098 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3208 0000  o.......C.3b2...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3208 0000  o.......6.5b2...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 a200 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6401  m.Z.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 6d0d 5a0d 6d0e 5a0e 0100 6401 6406 6c0f  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/__pycache__/stereotype.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/classes/__pycache__/stereotype.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1240 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d804 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d804 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 4800 0000 6400  .....@...sH...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6405 6406 8400 5a0a 6407 6408 8400  ..d.d...Z.d.d...
 00000070: 5a0b 6409 5300 290a 7a36 5375 7070 6f72  Z.d.S.).z6Suppor
```

### Comparing `gaphor-2.9.1/gaphor/UML/classes/association.py` & `gaphor-2.9.2/gaphor/UML/classes/association.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/associationpropertypages.py` & `gaphor-2.9.2/gaphor/UML/classes/associationpropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/classconnect.py` & `gaphor-2.9.2/gaphor/UML/classes/classconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/classeseditors.py` & `gaphor-2.9.2/gaphor/UML/classes/classeseditors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/classespropertypages.py` & `gaphor-2.9.2/gaphor/UML/classes/classespropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/classestoolbox.py` & `gaphor-2.9.2/gaphor/UML/classes/classestoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/component.py` & `gaphor-2.9.2/gaphor/UML/classes/component.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/containment.py` & `gaphor-2.9.2/gaphor/UML/classes/containment.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/containmentconnect.py` & `gaphor-2.9.2/gaphor/UML/classes/containmentconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/copypaste.py` & `gaphor-2.9.2/gaphor/UML/classes/copypaste.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/datatype.py` & `gaphor-2.9.2/gaphor/UML/classes/datatype.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/dependency.py` & `gaphor-2.9.2/gaphor/UML/classes/dependency.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/dependencypropertypages.py` & `gaphor-2.9.2/gaphor/UML/classes/dependencypropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/enumeration.py` & `gaphor-2.9.2/gaphor/UML/classes/enumeration.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/enumerationpropertypages.py` & `gaphor-2.9.2/gaphor/UML/classes/enumerationpropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/generalization.py` & `gaphor-2.9.2/gaphor/UML/classes/generalization.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/interface.py` & `gaphor-2.9.2/gaphor/UML/classes/interface.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/interfaceconnect.py` & `gaphor-2.9.2/gaphor/UML/classes/interfaceconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/interfacerealization.py` & `gaphor-2.9.2/gaphor/UML/classes/interfacerealization.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/klass.py` & `gaphor-2.9.2/gaphor/UML/classes/klass.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/package.py` & `gaphor-2.9.2/gaphor/UML/classes/package.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/propertypages.glade` & `gaphor-2.9.2/gaphor/UML/classes/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/propertypages.ui` & `gaphor-2.9.2/gaphor/UML/classes/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/classes/stereotype.py` & `gaphor-2.9.2/gaphor/UML/classes/stereotype.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/copypaste.py` & `gaphor-2.9.2/gaphor/UML/copypaste.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deletable.py` & `gaphor-2.9.2/gaphor/UML/deletable.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 348 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5c01 0000  o.......C.3b\...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5c01 0000  o.......6.5b\...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 4800 0000 6400  .....@...sH...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 6d04 5a04 0100 6400 6402 6c05 6d06 5a06  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6403 6c07 6d08 5a08 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6700 6405 a201  d.l.m.Z...g.d...
 00000070: 5a0b 6406 5300 2907 e900 0000 0029 04da  Z.d.S.)......)..
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/artifact.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/artifact.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2613 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 350a 0000  o.......C.3b5...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 350a 0000  o.......6.5b5...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9400 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/connector.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/connector.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7882 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ca1e 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ca1e 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9200 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6401 6407 6c0e  d.l.m.Z...d.d.l.
@@ -471,16 +471,16 @@
 00001d60: 746f 2065 6e73 7572 6520 4974 656d 466c  to ensure ItemFl
 00001d70: 6f77 2069 7320 7368 6f77 696e 6720 7072  ow is showing pr
 00001d80: 6f70 6572 2073 7465 7265 6f74 7970 6573  oper stereotypes
 00001d90: 0a20 2020 2066 6f72 2043 6f6e 7472 6f6c  .    for Control
 00001da0: 6c65 722c 2046 6565 6462 6163 6b20 616e  ler, Feedback an
 00001db0: 6420 436f 6e74 726f 6c41 6374 696f 6e20  d ControlAction 
 00001dc0: 6672 6f6d 2052 4141 4d4c 2e72 0f00 0000  from RAAML.r....
-00001dd0: 3e03 0000 005a 0846 6565 6462 6163 6b5a  >....Z.FeedbackZ
-00001de0: 0d43 6f6e 7472 6f6c 4163 7469 6f6e 5a0a  .ControlActionZ.
+00001dd0: 3e03 0000 005a 0d43 6f6e 7472 6f6c 4163  >....Z.ControlAc
+00001de0: 7469 6f6e 5a08 4665 6564 6261 636b 5a0a  tionZ.FeedbackZ.
 00001df0: 436f 6e74 726f 6c6c 6572 7201 0000 00e9  Controllerr.....
 00001e00: 0100 0000 4e29 0372 1b00 0000 723b 0000  ....N).r....r;..
 00001e10: 00da 056c 6f77 6572 2902 da07 656c 656d  ...lower)...elem
 00001e20: 656e 7472 1600 0000 720f 0000 0072 0f00  entr....r....r..
 00001e30: 0000 7212 0000 0072 1c00 0000 c400 0000  ..r....r........
 00001e40: 730c 0000 0004 0304 010a 0208 011a 0104  s...............
 00001e50: 0172 1c00 0000 4e29 1572 3e00 0000 da06  .r....N).r>.....
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/connectorconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/connectorconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 6666 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0a1a 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0a1a 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 8400 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6407 6c0b 6d0c 5a0c 0100 6401 6408 6c0d  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/copypaste.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/copypaste.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 502 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 f601 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 f601 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 5800 0000 6400  .....@...sX...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 0100 6400  d.l.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 0100 6501 6a08 6404  d.l.m.Z...e.j.d.
 00000060: 6504 6602 6405 6406 8404 8301 5a09 6501  e.f.d.d.....Z.e.
 00000070: 6a08 6404 6505 6602 6407 6408 8404 8301  j.d.e.f.d.d.....
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/deploymentpropertypage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/deploymentpropertypage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3389 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3d0d 0000  o.......C.3b=...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3d0d 0000  o.......6.5b=...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6400 0000 6400  .....@...sd...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 650a 6405 8301  m.Z.m.Z...e.d...
 00000070: 5a0b 6508 a00c 6503 6a0d a101 4700 6406  Z.e...e.j...G.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/deploymentsgroup.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/deploymentsgroup.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 977 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 24% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d103 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d103 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 8000 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6503 a008 6507  m.Z.m.Z...e...e.
 00000060: 6507 a102 6404 6405 8400 8301 5a09 6504  e...d.d.....Z.e.
 00000070: a008 6507 6507 a102 6406 6407 8400 8301  ..e.e...d.d.....
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/deploymentstoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/deploymentstoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1385 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6905 0000  o.......C.3bi...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6905 0000  o.......6.5bi...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000e 0000 0040 0000 0073 d400 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 6d04 5a04 0100 6401 6404  d.d.l.m.Z...d.d.
 00000050: 6c05 6d06 5a06 0100 6401 6405 6c07 6d08  l.m.Z...d.d.l.m.
 00000060: 5a08 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100  Z.m.Z.m.Z.m.Z...
 00000070: 6401 6406 6c0c 6d0d 5a0d 0100 6509 6506  d.d.l.m.Z...e.e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/__pycache__/node.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/deployments/__pycache__/node.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3027 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d30b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d30b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 a600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 0100 6401  m.Z.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/artifact.py` & `gaphor-2.9.2/gaphor/UML/deployments/artifact.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/connector.py` & `gaphor-2.9.2/gaphor/UML/deployments/connector.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/connectorconnect.py` & `gaphor-2.9.2/gaphor/UML/deployments/connectorconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/deploymentpropertypage.py` & `gaphor-2.9.2/gaphor/UML/deployments/deploymentpropertypage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/deploymentsgroup.py` & `gaphor-2.9.2/gaphor/UML/deployments/deploymentsgroup.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/deploymentstoolbox.py` & `gaphor-2.9.2/gaphor/UML/deployments/deploymentstoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/node.py` & `gaphor-2.9.2/gaphor/UML/deployments/node.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/propertypages.glade` & `gaphor-2.9.2/gaphor/UML/deployments/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/deployments/propertypages.ui` & `gaphor-2.9.2/gaphor/UML/deployments/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/group.py` & `gaphor-2.9.2/gaphor/UML/group.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 509 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 fd01 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 fd01 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 5400 0000 6400  .....@...sT...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 6d04 5a04 0100 6400 6402 6c05 6d06 5a06  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6403 6c07 6d08 5a08 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6400 6405 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6700 6406 a201 5a0d 6407  m.Z...g.d...Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/copypaste.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/copypaste.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 630 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 15% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7602 0000  o.......C.3bv...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7602 0000  o.......6.5bv...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 5400 0000 6400  .....@...sT...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6501 6a07 6404 6504 6602  m.Z...e.j.d.e.f.
 00000060: 6405 6406 8404 8301 5a08 6501 6a07 6404  d.d.....Z.e.j.d.
 00000070: 6503 6602 6407 6408 8404 8301 5a09 6409  e.f.d.d.....Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/executionspecification.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/executionspecification.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4813 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 cd12 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 cd12 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 cc00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a09 6d0a 5a0a 0100 6401  d.l.m.Z.m.Z...d.
 00000070: 6407 6c0b 6d0c 5a0c 0100 6401 6408 6c0d  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interaction.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interaction.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1573 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2506 0000  o.......C.3b%...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2506 0000  o.......6.5b%...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 8400 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionsconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionsconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 11713 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c12d 0000  o.......C.3b.-..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c12d 0000  o.......6.5b.-..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7001 0000 6400  .....@...sp...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 0100 6401 6406 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 0100 6401 6407 6c0e  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionsgroup.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionsgroup.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 512 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0002 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0002 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 6400 0000 6400  .....@...sd...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 6d07 5a07 0100 6501 a008 6504 6505 a102  m.Z...e...e.e...
 00000060: 6403 6404 8400 8301 5a09 6501 a008 6504  d.d.....Z.e...e.
 00000070: 6506 a102 6405 6406 8400 8301 5a0a 6501  e...d.d.....Z.e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionspropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionspropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2693 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 850a 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 850a 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6200 0000 6400  .....@...sb...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 6d06 5a06  m.Z.m.Z.m.Z.m.Z.
 00000050: 0100 6400 6403 6c07 6d08 5a08 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6506 6405 8301  d.l.m.Z...e.d...
 00000070: 5a0b 6505 a00c 650a a101 4700 6406 6407  Z.e...e...G.d.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/interactionstoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/interactionstoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3031 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d70b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d70b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000f 0000 0040 0000 0073 1e01 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 6d0d 5a0d 0100 6401 6407 6c0e  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/lifeline.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/lifeline.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 8595 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9321 0000  o.......C.3b.!..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9321 0000  o.......6.5b.!..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 2c01 0000 6400  .....@...s,...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 0100 6401 6403 6c04 6d05 5a05 6d06 5a06  ..d.d.l.m.Z.m.Z.
 00000050: 6d07 5a07 0100 6401 6404 6c08 6d09 5a09  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6405 6c0a 6d0b 5a0b 6d0c 5a0c  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 6d0f 5a0f  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/__pycache__/message.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/interactions/__pycache__/message.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7205 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 251c 0000  o.......C.3b%...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 251c 0000  o.......6.5b%...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 a600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 0100 6401 6403 6c04 6d05 5a05 0100 6401  ..d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 6d0d 5a0d 0100 6401 6406 6c0e 6d0f 5a0f  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/copypaste.py` & `gaphor-2.9.2/gaphor/UML/interactions/copypaste.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/executionspecification.py` & `gaphor-2.9.2/gaphor/UML/interactions/executionspecification.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/interaction.py` & `gaphor-2.9.2/gaphor/UML/interactions/interaction.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/interactionsconnect.py` & `gaphor-2.9.2/gaphor/UML/interactions/interactionsconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/interactionsgroup.py` & `gaphor-2.9.2/gaphor/UML/interactions/interactionsgroup.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/interactionspropertypages.py` & `gaphor-2.9.2/gaphor/UML/interactions/interactionspropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/interactionstoolbox.py` & `gaphor-2.9.2/gaphor/UML/interactions/interactionstoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/lifeline.py` & `gaphor-2.9.2/gaphor/UML/interactions/lifeline.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/message.py` & `gaphor-2.9.2/gaphor/UML/interactions/message.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/propertypages.glade` & `gaphor-2.9.2/gaphor/UML/interactions/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/interactions/propertypages.ui` & `gaphor-2.9.2/gaphor/UML/interactions/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/modelinglanguage.py` & `gaphor-2.9.2/gaphor/UML/modelinglanguage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/__pycache__/extension.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/profiles/__pycache__/extension.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1177 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9904 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9904 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 6800 0000 6400  .....@...sh...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 0100 6401 6406 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 650a 6502 6a0d 8301 4700  m.Z...e.e.j...G.
```

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/__pycache__/extensionconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/profiles/__pycache__/extensionconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3491 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a30d 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a30d 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6000 0000 6400  .....@...s`...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6400 6405 6c09 6d0a 5a0a 0100 6503  ..d.d.l.m.Z...e.
 00000070: a00b 6506 6508 a102 4700 6406 6407 8400  ..e.e...G.d.d...
```

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/__pycache__/metaclasspropertypage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/profiles/__pycache__/metaclasspropertypage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1834 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2a07 0000  o.......C.3b*...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2a07 0000  o.......6.5b*...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6000 0000 6400  .....@...s`...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6508  m.Z.m.Z.m.Z...e.
 00000060: 6404 8301 5a09 6405 6406 8400 5a0a 6506  d...Z.d.d...Z.e.
 00000070: a00b 6501 6a0c a101 4700 6407 6408 8400  ..e.j...G.d.d...
```

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/__pycache__/packageimport.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/profiles/__pycache__/packageimport.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 856 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5803 0000  o.......C.3bX...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5803 0000  o.......6.5bX...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6e00 0000 6400  .....@...sn...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6401 6407 6c0c 6d0d 5a0d 0100 650b  ..d.d.l.m.Z...e.
```

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/__pycache__/packageimportconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/profiles/__pycache__/packageimportconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1183 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9f04 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9f04 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 5800 0000 6400  .....@...sX...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6504 a00a 6507 6509 a102  m.Z...e...e.e...
 00000070: 4700 6406 6407 8400 6407 6505 8303 8301  G.d.d...d.e.....
```

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/__pycache__/profilestoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/profiles/__pycache__/profilestoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1943 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 11% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9707 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9707 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000e 0000 0040 0000 0073 1001 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 6d04 5a04 0100 6401 6404  d.d.l.m.Z...d.d.
 00000050: 6c05 6d06 5a06 0100 6401 6405 6c07 6d08  l.m.Z...d.d.l.m.
 00000060: 5a08 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100  Z.m.Z.m.Z.m.Z...
 00000070: 6401 6406 6c0c 6d0d 5a0d 0100 6407 6408  d.d.l.m.Z...d.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/__pycache__/stereotypepropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/profiles/__pycache__/stereotypepropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4700 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5c12 0000  o.......C.3b\...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5c12 0000  o.......6.5b\...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 8c00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6509 a00c 6504 6a0d a101 4700 6407  ..e...e.j...G.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/extension.py` & `gaphor-2.9.2/gaphor/UML/profiles/extension.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/extensionconnect.py` & `gaphor-2.9.2/gaphor/UML/profiles/extensionconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/metaclasspropertypage.py` & `gaphor-2.9.2/gaphor/UML/profiles/metaclasspropertypage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/packageimport.py` & `gaphor-2.9.2/gaphor/UML/profiles/packageimport.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/packageimportconnect.py` & `gaphor-2.9.2/gaphor/UML/profiles/packageimportconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/profilestoolbox.py` & `gaphor-2.9.2/gaphor/UML/profiles/profilestoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/propertypages.glade` & `gaphor-2.9.2/gaphor/UML/profiles/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/propertypages.ui` & `gaphor-2.9.2/gaphor/UML/profiles/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/profiles/stereotypepropertypages.py` & `gaphor-2.9.2/gaphor/UML/profiles/stereotypepropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/recipes.py` & `gaphor-2.9.2/gaphor/UML/recipes.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/sanitizerservice.py` & `gaphor-2.9.2/gaphor/UML/sanitizerservice.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/__init__.py` & `gaphor-2.9.2/gaphor/UML/states/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1236 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d404 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d404 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 5400 0000 6400  .....@...sT...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 6d04 5a04 0100 6401 6403 6c05 6d06 5a06  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6404 6c07 6d08 5a08 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 0100 6401 6406 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6700 6407 a201 5a0d 6408  m.Z...g.d...Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/copypaste.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/copypaste.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 595 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5302 0000  o.......C.3bS...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5302 0000  o.......6.5bS...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 5400 0000 6400  .....@...sT...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6501 6a07 6404 6503 6602  m.Z...e.j.d.e.f.
 00000060: 6405 6406 8404 8301 5a08 6501 6a07 6404  d.d.....Z.e.j.d.
 00000070: 6504 6602 6407 6408 8404 8301 5a09 6409  e.f.d.d.....Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/finalstate.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/finalstate.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1365 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5505 0000  o.......C.3bU...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5505 0000  o.......6.5bU...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 8c00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6401 6407 6c0e  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/propertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/propertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3488 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a00d 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a00d 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7400 0000 6400  .....@...st...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6508  m.Z.m.Z.m.Z...e.
 00000060: 6405 8301 5a09 6507 a00a 6502 6a0b a101  d...Z.e...e.j...
 00000070: 4700 6406 6407 8400 6407 6506 8303 8301  G.d.d...d.e.....
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/pseudostates.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/pseudostates.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2039 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 f707 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 f707 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 a000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 6d0d 5a0d 0100 6401 6407 6c0e  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/state.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/state.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2998 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 b60b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 b60b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 9e00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 6d0d 5a0d 0100 6401 6406 6c0e 6d0f 5a0f  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/statestoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/statestoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3362 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 220d 0000  o.......C.3b"...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 220d 0000  o.......6.5b"...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000e 0000 0040 0000 0073 2c01 0000 6400  .....@...s,...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/transition.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/transition.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1164 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8c04 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8c04 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 7200 0000 6400  .....@...sr...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6401 6405 6c0a 6d0b 5a0b 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 650b 6502 6a0e  d.l.m.Z...e.e.j.
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/__pycache__/vertexconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/states/__pycache__/vertexconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2622 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3e0a 0000  o.......C.3b>...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3e0a 0000  o.......6.5b>...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 9000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 4700 6407 6408 8400 6408 6505 8303  ..G.d.d...d.e...
```

### Comparing `gaphor-2.9.1/gaphor/UML/states/copypaste.py` & `gaphor-2.9.2/gaphor/UML/states/copypaste.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/finalstate.py` & `gaphor-2.9.2/gaphor/UML/states/finalstate.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/propertypages.glade` & `gaphor-2.9.2/gaphor/UML/states/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/propertypages.py` & `gaphor-2.9.2/gaphor/UML/states/propertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/propertypages.ui` & `gaphor-2.9.2/gaphor/UML/states/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/pseudostates.py` & `gaphor-2.9.2/gaphor/UML/states/pseudostates.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/state.py` & `gaphor-2.9.2/gaphor/UML/states/state.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/statestoolbox.py` & `gaphor-2.9.2/gaphor/UML/states/statestoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/transition.py` & `gaphor-2.9.2/gaphor/UML/states/transition.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/states/vertexconnect.py` & `gaphor-2.9.2/gaphor/UML/states/vertexconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/toolbox.py` & `gaphor-2.9.2/gaphor/UML/toolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/uml.py` & `gaphor-2.9.2/gaphor/UML/uml.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/umlfmt.py` & `gaphor-2.9.2/gaphor/UML/umlfmt.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/umllex.py` & `gaphor-2.9.2/gaphor/UML/umllex.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/umloverrides.py` & `gaphor-2.9.2/gaphor/UML/umloverrides.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/__pycache__/actor.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/usecases/__pycache__/actor.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1899 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6b07 0000  o.......C.3bk...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6b07 0000  o.......6.5bk...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 a000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/__pycache__/extend.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/usecases/__pycache__/extend.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 966 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c603 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c603 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 7800 0000 6400  .....@...sx...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6401 6407 6c0e  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/__pycache__/include.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/usecases/__pycache__/include.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 970 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ca03 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ca03 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 7800 0000 6400  .....@...sx...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6401 6407 6c0e  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecase.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecase.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1256 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 e804 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 e804 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 8c00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6401 6407 6c0e  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecaseconnect.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecaseconnect.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1434 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9a05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9a05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 8000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6504 a00c 650b 6509 a102 4700 6407  ..e...e.e...G.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecasegroup.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecasegroup.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 533 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1502 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1502 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 4c00 0000 6400  .....@...sL...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 0100 6501  d.l.m.Z.m.Z...e.
 00000050: a006 6504 6505 a102 6403 6404 8400 8301  ..e.e...d.d.....
 00000060: 5a07 6502 a006 6504 6505 a102 6405 6406  Z.e...e.e...d.d.
 00000070: 8400 8301 5a08 6407 5300 2908 e900 0000  ....Z.d.S.).....
```

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/__pycache__/usecasetoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/UML/usecases/__pycache__/usecasetoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1746 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d206 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d206 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000e 0000 0040 0000 0073 f600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6509 6506 6407  d.l.m.Z...e.e.d.
```

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/actor.py` & `gaphor-2.9.2/gaphor/UML/usecases/actor.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/extend.py` & `gaphor-2.9.2/gaphor/UML/usecases/extend.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/include.py` & `gaphor-2.9.2/gaphor/UML/usecases/include.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/usecase.py` & `gaphor-2.9.2/gaphor/UML/usecases/usecase.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/usecaseconnect.py` & `gaphor-2.9.2/gaphor/UML/usecases/usecaseconnect.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/usecasegroup.py` & `gaphor-2.9.2/gaphor/UML/usecases/usecasegroup.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/UML/usecases/usecasetoolbox.py` & `gaphor-2.9.2/gaphor/UML/usecases/usecasetoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/__init__.py` & `gaphor-2.9.2/gaphor/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/abc.py` & `gaphor-2.9.2/gaphor/abc.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/action.py` & `gaphor-2.9.2/gaphor/action.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/application.py` & `gaphor-2.9.2/gaphor/application.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/babel.py` & `gaphor-2.9.2/gaphor/babel.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/codegen/__pycache__/coder.cpython-310.pyc` & `gaphor-2.9.2/gaphor/codegen/__pycache__/coder.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 14906 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3a3a 0000  o.......C.3b::..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3a3a 0000  o.......6.5b::..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0173 5c02 0000 6400  .....@...s\...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6403 6c04 5a04 6401  d.l.Z.d.d.l.Z.d.
 00000050: 6403 6c05 5a05 6401 6403 6c06 5a06 6401  d.l.Z.d.d.l.Z.d.
 00000060: 6403 6c07 5a07 6401 6404 6c08 6d09 5a09  d.l.Z.d.d.l.m.Z.
 00000070: 0100 6401 6405 6c0a 6d0b 5a0b 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/codegen/__pycache__/override.cpython-310.pyc` & `gaphor-2.9.2/gaphor/codegen/__pycache__/override.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3229 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9d0c 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9d0c 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 3400 0000 6400  .....@...s4...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6501 a004 6404 a101 5a05  m.Z...e...d...Z.
 00000050: 4700 6405 6406 8400 6406 8302 5a06 6402  G.d.d...d...Z.d.
 00000060: 5300 2907 7ad8 436f 6465 2066 6f72 206c  S.).z.Code for l
 00000070: 6f61 6469 6e67 2075 7020 616e 206f 7665  oading up an ove
```

### Comparing `gaphor-2.9.1/gaphor/codegen/coder.py` & `gaphor-2.9.2/gaphor/codegen/coder.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/codegen/override.py` & `gaphor-2.9.2/gaphor/codegen/override.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/__pycache__/eventmanager.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/__pycache__/eventmanager.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1540 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0406 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0406 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 4800 0000 6400  .....@...sH...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 0100 6401 6403 6c01 6d04 5a05 0100 6401  ..d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6405 6406 8400  d.l.m.Z...d.d...
 00000060: 5a08 4700 6407 6408 8400 6408 6507 8303  Z.G.d.d...d.e...
 00000070: 5a09 6409 5300 290a 7a0e 4576 656e 7420  Z.d.S.).z.Event
```

### Comparing `gaphor-2.9.1/gaphor/core/__pycache__/format.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/__pycache__/format.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 780 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0c03 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0c03 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 8c00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6502  d.l.m.Z.m.Z...e.
 00000050: 6404 6505 6405 6506 6604 6406 6407 8404  d.e.d.e.f.d.d...
 00000060: 8301 5a07 6502 6404 6505 6408 6506 6405  ..Z.e.d.e.d.e.d.
 00000070: 6409 6606 640a 640b 8404 8301 5a08 6507  d.f.d.d.....Z.e.
```

### Comparing `gaphor-2.9.1/gaphor/core/eventmanager.py` & `gaphor-2.9.2/gaphor/core/eventmanager.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/format.py` & `gaphor-2.9.2/gaphor/core/format.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 412 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9c01 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9c01 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 6000 0000 6400  .....@...s`...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 0100 6400  m.Z.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 6d08 5a08 0100 6400  d.l.m.Z.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6400 6405 6c0b  d.l.m.Z...d.d.l.
 00000070: 5400 6400 6406 6c0c 6d0d 5a0d 0100 6400  T.d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/collection.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/collection.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4730 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7a12 0000  o.......C.3bz...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7a12 0000  o.......6.5bz...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 7800 0000 6400  .....@...sx...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 0100 6401  m.Z.m.Z.m.Z...d.
 00000050: 6403 6c07 6d08 5a08 0100 6401 6404 6c09  d.l.m.Z...d.d.l.
 00000060: 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c 0100 6505  m.Z.m.Z.m.Z...e.
 00000070: 6405 8301 5a0d 4700 6406 6407 8400 6407  d...Z.G.d.d...d.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/coremodel.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/coremodel.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2230 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 9% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 b608 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 b608 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0173 7c01 0000 6400  .....@...s|...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d08 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6403 6c0d 6d0e 5a0e 0100 6400  ..d.d.l.m.Z...d.
 00000070: 6404 6c0f 6d10 5a10 0100 6400 6405 6c11  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/diagram.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/diagram.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 13175 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7733 0000  o.......C.3bw3..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7733 0000  o.......6.5bw3..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0173 ba01 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 5a03 6401 6404 6c04 6d05  d.d.l.Z.d.d.l.m.
 00000050: 5a05 0100 6401 6405 6c06 6d07 5a07 0100  Z...d.d.l.m.Z...
 00000060: 6401 6406 6c08 6d09 5a09 6d0a 5a0a 6d0b  d.d.l.m.Z.m.Z.m.
 00000070: 5a0b 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f  Z.m.Z.m.Z.m.Z.m.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/element.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/element.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 6378 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ea18 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ea18 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 3801 0000 5500  .....@...s8...U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 5a03 6401 6404 6c04 6d05  d.d.l.Z.d.d.l.m.
 00000050: 5a05 6d06 5a06 6d07 5a07 6d08 5a08 6d09  Z.m.Z.m.Z.m.Z.m.
 00000060: 5a09 6d0a 5a0a 0100 6401 6405 6c0b 6d0c  Z.m.Z...d.d.l.m.
 00000070: 5a0c 0100 6401 6406 6c0d 6d0e 5a0e 0100  Z...d.d.l.m.Z...
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/elementdispatcher.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/elementdispatcher.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 9372 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9c24 0000  o.......C.3b.$..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9c24 0000  o.......6.5b.$..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 9400 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6404 6c04 6d05 5a05  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a09 6d0a 5a0a 0100 6401  d.l.m.Z.m.Z...d.
 00000070: 6407 6c0b 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e  d.l.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/elementfactory.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/elementfactory.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7511 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 571d 0000  o.......C.3bW...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 571d 0000  o.......6.5bW...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 0801 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  m.Z.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 6401  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/event.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/event.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7232 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 401c 0000  o.......C.3b@...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 401c 0000  o.......6.5b@...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 3601 0000 6400  .....@...s6...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 4700  Z.d.d.l.m.Z...G.
 00000040: 6403 6404 8400 6404 8302 5a03 4700 6405  d.d...d...Z.G.d.
 00000050: 6406 8400 6406 8302 5a04 4700 6407 6408  d...d...Z.G.d.d.
 00000060: 8400 6408 6504 8303 5a05 4700 6409 640a  ..d.e...Z.G.d.d.
 00000070: 8400 640a 6504 8303 5a06 4700 640b 640c  ..d.e...Z.G.d.d.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/listmixins.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/listmixins.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7735 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 371e 0000  o.......C.3b7...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 371e 0000  o.......6.5b7...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0173 8800 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 6d07 5a07 6d08 5a08 0100 6404 6405 6702  m.Z.m.Z...d.d.g.
 00000060: 5a09 6507 6406 8301 5a0a 6414 640b 640c  Z.e.d...Z.d.d.d.
 00000070: 8404 5a0b 4700 640d 6404 8400 6404 8302  ..Z.G.d.d...d...
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/modelinglanguage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/modelinglanguage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1341 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3d05 0000  o.......C.3b=...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3d05 0000  o.......6.5b=...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 4000 0000 6400  .....@...s@...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 4700 6404 6405  d.l.m.Z...G.d.d.
 00000050: 8400 6405 6502 8303 5a05 4700 6406 6407  ..d.e...Z.G.d.d.
 00000060: 8400 6407 6502 8303 5a06 6408 5300 2909  ..d.e...Z.d.S.).
 00000070: 7a1d 4334 204d 6f64 656c 204c 616e 6775  z.C4 Model Langu
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/presentation.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/presentation.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4734 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7e12 0000  o.......C.3b~...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7e12 0000  o.......6.5b~...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0173 c200 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6403 6c04 5a04 6401  d.l.Z.d.d.l.Z.d.
 00000050: 6404 6c05 6d06 5a06 6d07 5a07 6d08 5a08  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6401 6405 6c09 6d0a 5a0a 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6406 6c0b 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e  d.l.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/properties.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/properties.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 28743 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4770 0000  o.......C.3bGp..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4770 0000  o.......6.5bGp..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0173 d201 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6404 6c04 6d05 5a05  d.l.Z.d.d.l.m.Z.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 6d09 5a09  m.Z.m.Z.m.Z.m.Z.
 00000060: 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c 6d0d 5a0d  m.Z.m.Z.m.Z.m.Z.
 00000070: 6d0e 5a0e 0100 6401 6405 6c0f 6d10 5a10  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/__pycache__/stylesheet.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/modeling/__pycache__/stylesheet.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2007 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d707 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d707 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 7400 0000 6400  .....@...st...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 0100 6400  Z.d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6400 6406 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 6d0b 5a0b 6d0c 5a0c 0100 6502 a00d 6407  m.Z.m.Z...e...d.
```

### Comparing `gaphor-2.9.1/gaphor/core/modeling/collection.py` & `gaphor-2.9.2/gaphor/core/modeling/collection.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/coremodel.py` & `gaphor-2.9.2/gaphor/core/modeling/coremodel.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/diagram.py` & `gaphor-2.9.2/gaphor/core/modeling/diagram.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/element.py` & `gaphor-2.9.2/gaphor/core/modeling/element.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/elementdispatcher.py` & `gaphor-2.9.2/gaphor/core/modeling/elementdispatcher.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/elementfactory.py` & `gaphor-2.9.2/gaphor/core/modeling/elementfactory.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/event.py` & `gaphor-2.9.2/gaphor/core/modeling/event.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/listmixins.py` & `gaphor-2.9.2/gaphor/core/modeling/listmixins.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/modelinglanguage.py` & `gaphor-2.9.2/gaphor/core/modeling/modelinglanguage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/presentation.py` & `gaphor-2.9.2/gaphor/core/modeling/presentation.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/properties.py` & `gaphor-2.9.2/gaphor/core/modeling/properties.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/modeling/stylesheet.py` & `gaphor-2.9.2/gaphor/core/modeling/stylesheet.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/styling/__init__.py` & `gaphor-2.9.2/gaphor/core/styling/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/styling/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/styling/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3398 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 460d 0000  o.......C.3bF...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 460d 0000  o.......6.5bF...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0173 3001 0000 6400  .....@...s0...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 6d05 5a05  Z.d.d.l.m.Z.m.Z.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 6d09 5a09  m.Z.m.Z.m.Z.m.Z.
 00000060: 6d0a 5a0a 6d0b 5a0b 0100 6400 6402 6c0c  m.Z.m.Z...d.d.l.
 00000070: 5a0c 6400 6404 6c0d 6d0e 5a0e 6d0f 5a0f  Z.d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/core/styling/__pycache__/declarations.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/styling/__pycache__/declarations.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5163 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2b14 0000  o.......C.3b+...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2b14 0000  o.......6.5b+...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0073 1002 0000 5500  .....@...s....U.
 00000030: 6400 6401 6c00 6d01 5a01 6d02 5a02 6d03  d.d.l.m.Z.m.Z.m.
 00000040: 5a03 6d04 5a04 6d05 5a05 6d06 5a06 6d07  Z.m.Z.m.Z.m.Z.m.
 00000050: 5a07 0100 6400 6402 6c08 5a09 6400 6403  Z...d.d.l.Z.d.d.
 00000060: 6c0a 6d0b 5a0b 0100 6400 6404 6c0c 6d0d  l.m.Z...d.d.l.m.
 00000070: 5a0d 6d0e 5a0e 6d0f 5a0f 6d10 5a10 6d11  Z.m.Z.m.Z.m.Z.m.
```

### Comparing `gaphor-2.9.1/gaphor/core/styling/__pycache__/parser.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/styling/__pycache__/parser.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 11597 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4d2d 0000  o.......C.3bM-..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4d2d 0000  o.......6.5bM-..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 1201 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6403  Z.d.d.l.m.Z...d.
 00000040: 6701 5a03 642b 6405 6403 8401 5a04 6406  g.Z.d+d.d...Z.d.
 00000050: 6407 8400 5a05 6408 6409 8400 5a06 640a  d...Z.d.d...Z.d.
 00000060: 640b 8400 5a07 640c 640d 8400 5a08 640e  d...Z.d.d...Z.d.
 00000070: 640f 8400 5a09 642c 6411 6412 8401 5a0a  d...Z.d,d.d...Z.
```

### Comparing `gaphor-2.9.1/gaphor/core/styling/__pycache__/properties.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/styling/__pycache__/properties.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1454 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ae05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ae05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 3401 0000 6400  .....@...s4...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 6d07 5a07 0100 6505 6508 6508 6508 6508  m.Z...e.e.e.e.e.
 00000060: 6604 1900 5a09 6505 6508 6508 6508 6508  f...Z.e.e.e.e.e.
 00000070: 6604 1900 5a0a 6507 650b 6508 6602 1900  f...Z.e.e.e.f...
```

### Comparing `gaphor-2.9.1/gaphor/core/styling/__pycache__/selectors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/core/styling/__pycache__/selectors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4122 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1a10 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1a10 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 dc00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6501 a006 6405 a101 6a07 5a08 6406  ..e...d...j.Z.d.
 00000060: 6407 8400 5a09 6503 6408 6409 8400 8301  d...Z.e.d.d.....
 00000070: 5a0a 650a 6a0b 640a 6505 6a0c 6602 640b  Z.e.j.d.e.j.f.d.
```

### Comparing `gaphor-2.9.1/gaphor/core/styling/declarations.py` & `gaphor-2.9.2/gaphor/core/styling/declarations.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/styling/parser.py` & `gaphor-2.9.2/gaphor/core/styling/parser.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/styling/properties.py` & `gaphor-2.9.2/gaphor/core/styling/properties.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/core/styling/selectors.py` & `gaphor-2.9.2/gaphor/core/styling/selectors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/connectors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/connectors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 13006 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ce32 0000  o.......C.3b.2..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ce32 0000  o.......6.5b.2..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 3801 0000 5500  .....@...s8...U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 5a03 6401 6403 6c04 5a04  d.d.l.Z.d.d.l.Z.
 00000050: 6401 6404 6c05 6d06 5a06 6d07 5a07 6d08  d.d.l.m.Z.m.Z.m.
 00000060: 5a08 0100 6401 6405 6c09 6d0a 5a0a 0100  Z...d.d.l.m.Z...
 00000070: 6401 6406 6c0b 6d0c 5a0c 6d0d 5a0d 0100  d.d.l.m.Z.m.Z...
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/copypaste.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/copypaste.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 6218 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4a18 0000  o.......C.3bJ...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4a18 0000  o.......6.5bJ...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 7201 0000 6400  .....@...sr...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6404 6c04 6d05 5a05  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a09 6d0a 5a0a 6d0b 5a0b  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6407 6c0c 6d0d 5a0d 6d0e 5a0e  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/diagramtoolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/diagramtoolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4230 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8610 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8610 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000f 0000 0040 0000 0073 1002 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d08 5a08 6d09 5a09 0100 6401 6403 6c0a  m.Z.m.Z...d.d.l.
 00000060: 6d0b 5a0b 0100 6401 6404 6c0c 6d0d 5a0d  m.Z...d.d.l.m.Z.
 00000070: 0100 6401 6405 6c0e 6d0f 5a0f 6d10 5a10  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/event.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/event.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 127 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7f00 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7f00 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 2200 0000 4700  .....@...s"...G.
 00000030: 6400 6401 8400 6401 8302 5a00 4700 6402  d.d...d...Z.G.d.
 00000040: 6403 8400 6403 6500 8303 5a01 6404 5300  d...d.e...Z.d.S.
 00000050: 2905 6300 0000 0000 0000 0000 0000 0000  ).c.............
 00000060: 0000 0001 0000 0040 0000 0073 0c00 0000  .......@...s....
 00000070: 6500 5a01 6400 5a02 6401 5300 2902 da0d  e.Z.d.Z.d.S.)...
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/export.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/export.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2002 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d207 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d207 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 6200 0000 6400  .....@...sb...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6401 6404 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6411 6407 6408 8401 5a09 6409 640a  ..d.d.d...Z.d.d.
 00000070: 8400 5a0a 640b 640c 8400 5a0b 640d 640e  ..Z.d.d...Z.d.d.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/group.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/group.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1911 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7707 0000  o.......C.3bw...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7707 0000  o.......6.5bw...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 c600 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 5a03 6401 6404 6c04 6d05  d.d.l.Z.d.d.l.m.
 00000050: 5a05 0100 6401 6405 6c06 6d07 5a07 6d08  Z...d.d.l.m.Z.m.
 00000060: 5a08 0100 6401 6406 6c09 6d0a 5a0a 6d0b  Z...d.d.l.m.Z.m.
 00000070: 5a0b 6d0c 5a0c 0100 641b 6409 640a 8404  Z.m.Z...d.d.d...
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/hoversupport.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/hoversupport.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1606 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4606 0000  o.......C.3bF...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4606 0000  o.......6.5bF...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 4400 0000 6400  .....@...sD...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6502  d.l.m.Z.m.Z...e.
 00000040: a003 a100 6402 6b02 7218 6403 6404 8400  ....d.k.r.d.d...
 00000050: 5a04 6405 6406 8400 5a05 6409 5300 6407  Z.d.d...Z.d.S.d.
 00000060: 6404 8400 5a04 6408 6406 8400 5a05 6409  d...Z.d.d...Z.d.
 00000070: 5300 290a e900 0000 0029 02da 0347 646b  S.)......)...Gdk
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/inlineeditors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/inlineeditors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2994 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 b20b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 b20b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0173 9a00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6405 6c08 6d09 5a09 6d0a 5a0a 0100 6400  d.l.m.Z.m.Z...d.
 00000070: 6406 6c0b 6d0c 5a0c 6d0d 5a0d 0100 6400  d.l.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/painter.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/painter.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2841 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 190b 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 190b 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0173 7000 0000 6400  .....@...sp...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 6d08 5a08 0100 6401  m.Z.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c  d.l.m.Z.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 0100 4700  ..d.d.l.m.Z...G.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/presentation.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/presentation.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 11130 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7a2b 0000  o.......C.3bz+..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7a2b 0000  o.......6.5bz+..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0173 7e01 0000 6400  .....@...s~...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 0100 6400  Z.d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6402 6c07  d.l.m.Z...d.d.l.
 00000060: 5a07 6400 6405 6c08 6d09 5a09 0100 6400  Z.d.d.l.m.Z...d.
 00000070: 6406 6c08 6d0a 5a0b 0100 6400 6407 6c08  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/propertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/propertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 10117 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8527 0000  o.......C.3b.'..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8527 0000  o.......6.5b.'..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0009 0000 0040 0000 0073 5c01 0000 6400  .....@...s\...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 6d06 5a06  m.Z.m.Z.m.Z.m.Z.
 00000050: 6d07 5a07 6d08 5a08 0100 6401 6402 6c09  m.Z.m.Z...d.d.l.
 00000060: 5a0a 6401 6404 6c0b 6d0c 5a0c 0100 6401  Z.d.d.l.m.Z...d.
 00000070: 6405 6c0d 6d0e 5a0e 0100 6401 6406 6c0f  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/selection.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/selection.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 930 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a203 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a203 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 4000 0000 6400  .....@...s@...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 0100 6400 6402 6c04 6d05 5a05 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6403 6c06 6d07 5a08 0100 4700 6404 6405  d.l.m.Z...G.d.d.
 00000060: 8400 6405 6508 8303 5a07 6406 5300 2907  ..d.e...Z.d.S.).
 00000070: e900 0000 0029 03da 0849 7465 7261 626c  .....)...Iterabl
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/shapes.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/shapes.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 11144 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 882b 0000  o.......C.3b.+..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 882b 0000  o.......6.5b.+..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 fe00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6405 6c08 6d09 5a09 0100 6400 6406 6c0a  d.l.m.Z...d.d.l.
 00000070: 6d0b 5a0b 6d0c 5a0c 0100 6400 6407 6c0d  m.Z.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/support.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/support.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 985 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d903 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d903 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 5a00 0000 5500  .....@...sZ...U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 6d04 5a04 6d05 5a05 0100  d.d.l.m.Z.m.Z...
 00000050: 6404 6405 8400 5a06 6900 6107 6502 6504  d.d...Z.i.a.e.e.
 00000060: 6505 6602 1900 6508 6406 3c00 6407 6408  e.f...e.d.<.d.d.
 00000070: 8400 5a09 6409 640a 8400 5a0a 640b 640c  ..Z.d.d...Z.d.d.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/__pycache__/text.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/__pycache__/text.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 7647 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 df1d 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 df1d 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0173 9600 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 6d09 5a09 6d0a 5a0a 0100 6401 6406 6c0b  m.Z.m.Z...d.d.l.
 00000070: 6d0c 5a0c 6d0d 5a0d 6d0e 5a0e 6d0f 5a0f  m.Z.m.Z.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/connectors.py` & `gaphor-2.9.2/gaphor/diagram/connectors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/copypaste.py` & `gaphor-2.9.2/gaphor/diagram/copypaste.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/diagramtoolbox.py` & `gaphor-2.9.2/gaphor/diagram/diagramtoolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/export.py` & `gaphor-2.9.2/gaphor/diagram/export.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/general/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/general/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 339 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5301 0000  o.......C.3bS...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5301 0000  o.......6.5bS...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 4c00 0000 6400  .....@...sL...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 0100 6400 6402 6c04 6d05 5a05 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 0100 6400 6404 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6700  m.Z.m.Z.m.Z...g.
 00000070: 6405 a201 5a0c 6406 5300 2907 e900 0000  d...Z.d.S.).....
```

### Comparing `gaphor-2.9.1/gaphor/diagram/general/__pycache__/comment.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/general/__pycache__/comment.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1430 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 9605 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 9605 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6800 0000 6400  .....@...sh...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 6d0a 5a0a 6d0b 5a0b 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 650d 6502 8301  d.l.m.Z...e.e...
```

### Comparing `gaphor-2.9.1/gaphor/diagram/general/__pycache__/commentline.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/general/__pycache__/commentline.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 622 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6e02 0000  o.......C.3bn...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6e02 0000  o.......6.5bn...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 3000 0000 6400  .....@...s0...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 4700 6404 6405  d.l.m.Z...G.d.d.
 00000050: 8400 6405 6504 8303 5a05 6406 5300 2907  ..d.e...Z.d.S.).
 00000060: 7a4a 0a43 6f6d 6d65 6e74 4c69 6e65 202d  zJ.CommentLine -
 00000070: 2d20 4120 6c69 6e65 2074 6861 7420 636f  - A line that co
```

### Comparing `gaphor-2.9.1/gaphor/diagram/general/__pycache__/connectors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/general/__pycache__/connectors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5759 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7f16 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7f16 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 ae00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6407 6c0b 6d0c 5a0c 0100 6401 6408 6c0d  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/general/__pycache__/generaleditors.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/general/__pycache__/generaleditors.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1126 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6604 0000  o.......C.3bf...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6604 0000  o.......6.5bf...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 5200 0000 6400  .....@...sR...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6505 a009 6503 a101 6409 6406 650a  ..e...e...d.d.e.
 00000070: 6602 6407 6408 8405 8301 5a0b 6405 5300  f.d.d.....Z.d.S.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/general/__pycache__/generalpropertypages.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/general/__pycache__/generalpropertypages.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1416 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 9% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8805 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8805 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 5600 0000 6400  .....@...sV...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6400 6404 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 6d09 5a09 0100 6508 a00a 6505 a101 4700  m.Z...e...e...G.
 00000070: 6405 6406 8400 6406 6507 8303 8301 5a0b  d.d...d.e.....Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/general/__pycache__/simpleitem.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/general/__pycache__/simpleitem.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1251 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 e304 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 e304 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 6c00 0000 6400  .....@...sl...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 4700 6406 6407 8400 6407  m.Z...G.d.d...d.
 00000070: 6507 8303 5a0a 4700 6408 6409 8400 6409  e...Z.G.d.d...d.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/general/comment.py` & `gaphor-2.9.2/gaphor/diagram/general/comment.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/general/commentline.py` & `gaphor-2.9.2/gaphor/diagram/general/commentline.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/general/connectors.py` & `gaphor-2.9.2/gaphor/diagram/general/connectors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/general/generaleditors.py` & `gaphor-2.9.2/gaphor/diagram/general/generaleditors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/general/generalpropertypages.py` & `gaphor-2.9.2/gaphor/diagram/general/generalpropertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/general/simpleitem.py` & `gaphor-2.9.2/gaphor/diagram/general/simpleitem.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/group.py` & `gaphor-2.9.2/gaphor/diagram/group.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/hoversupport.py` & `gaphor-2.9.2/gaphor/diagram/hoversupport.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/inlineeditors.py` & `gaphor-2.9.2/gaphor/diagram/inlineeditors.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/painter.py` & `gaphor-2.9.2/gaphor/diagram/painter.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/presentation.py` & `gaphor-2.9.2/gaphor/diagram/presentation.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/propertypages.glade` & `gaphor-2.9.2/gaphor/diagram/propertypages.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/propertypages.py` & `gaphor-2.9.2/gaphor/diagram/propertypages.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/propertypages.ui` & `gaphor-2.9.2/gaphor/diagram/propertypages.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/selection.py` & `gaphor-2.9.2/gaphor/diagram/selection.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/shapes.py` & `gaphor-2.9.2/gaphor/diagram/shapes.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/support.py` & `gaphor-2.9.2/gaphor/diagram/support.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/text.py` & `gaphor-2.9.2/gaphor/diagram/text.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__init__.py` & `gaphor-2.9.2/gaphor/diagram/tools/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2482 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 b209 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 b209 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 c000 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 6d07 5a07  m.Z.m.Z.m.Z.m.Z.
 00000050: 0100 6401 6403 6c08 6d09 5a09 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6404 6c0a 5a0b 6401 6404 6c0c 5a0b 6401  d.l.Z.d.d.l.Z.d.
 00000070: 6404 6c0d 5a0b 6401 6405 6c0e 6d0f 5a0f  d.l.Z.d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/connector.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/connector.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5213 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5d14 0000  o.......C.3b]...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5d14 0000  o.......6.5b]...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 e400 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c01 6d03 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c01 6d05 5a05 6d06 5a06 0100 6400  d.l.m.Z.m.Z...d.
 00000060: 6405 6c07 6d08 5a08 0100 6400 6406 6c09  d.l.m.Z...d.d.l.
 00000070: 6d0a 5a0a 0100 6400 6403 6c0b 6d03 5a03  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/dnd.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/dnd.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 760 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 f802 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 f802 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 5400 0000 6400  .....@...sT...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 6d03 5a03  d.l.m.Z.m.Z.m.Z.
 00000040: 0100 6400 6402 6c04 6d05 5a05 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 0100 6400 6404 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6405 6503 6a0a 6602 6406  m.Z...d.e.j.f.d.
 00000070: 6407 8404 5a0b 6408 6409 8400 5a0c 640a  d...Z.d.d...Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/dropzone.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/dropzone.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4397 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2d11 0000  o.......C.3b-...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2d11 0000  o.......6.5b-...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0007 0000 0040 0000 0173 1801 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 0100 6400  Z.d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 6d09 5a09 0100 6400 6406 6c0a  m.Z.m.Z...d.d.l.
 00000070: 6d0b 5a0c 0100 6400 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/grayout.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/grayout.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1572 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2406 0000  o.......C.3b$...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2406 0000  o.......6.5b$...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 7800 0000 6400  .....@...sx...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 6d07 5a07 0100 6400 6404 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6400 6405 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 6407  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/magnet.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/magnet.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3871 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1f0f 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1f0f 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 9400 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 0100 6401 6404 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 0100 6407  ..d.d.l.m.Z...d.
 00000070: 6506 6408 6508 6a0b 6604 6409 640a 8404  e.d.e.j.f.d.d...
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/placement.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/placement.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3988 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 940f 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 940f 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 1e01 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6400 6406 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6407 6c0b 6d0c 5a0c 6d0d 5a0d  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/segment.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/segment.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1381 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6505 0000  o.......C.3be...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6505 0000  o.......6.5be...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6600 0000 6400  .....@...sf...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 0100 6400 6403 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6502 a007 6506 a101 4700  m.Z...e...e...G.
 00000060: 6404 6405 8400 6405 6501 8303 8301 5a08  d.d...d.e.....Z.
 00000070: 4700 6406 6407 8400 6407 6504 8303 5a09  G.d.d...d.e...Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/shortcut.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/shortcut.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1231 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 10% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 cf04 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 cf04 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 5600 0000 6400  .....@...sV...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6405 6406 8400 5a09 6407 6408 8400  ..d.d...Z.d.d...
 00000070: 5a0a 6409 6501 6602 640a 640b 8404 5a0b  Z.d.e.f.d.d...Z.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/textedit.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/textedit.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1078 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3604 0000  o.......C.3b6...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3604 0000  o.......6.5b6...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 3800 0000 6400  .....@...s8...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 0100 6403 6404 8400  d.l.m.Z...d.d...
 00000050: 5a05 6405 6406 8400 5a06 6407 6408 8400  Z.d.d...Z.d.d...
 00000060: 5a07 6409 5300 290a e900 0000 0029 02da  Z.d.S.)......)..
 00000070: 0347 646b da03 4774 6b29 01da 0c49 6e6c  .Gdk..Gtk)...Inl
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/__pycache__/txtool.cpython-310.pyc` & `gaphor-2.9.2/gaphor/diagram/tools/__pycache__/txtool.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 891 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7b03 0000  o.......C.3b{...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7b03 0000  o.......6.5b{...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 7a00 0000 6400  .....@...sz...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 0100 6400 6403 6c05  d.l.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 4700 6405 6406 8400 6406 8302 5a09  ..G.d.d...d...Z.
 00000070: 6407 6408 9c01 6409 6504 6a0a 640a 6506  d.d...d.e.j.d.e.
```

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/connector.py` & `gaphor-2.9.2/gaphor/diagram/tools/connector.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/dnd.py` & `gaphor-2.9.2/gaphor/diagram/tools/dnd.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/dropzone.py` & `gaphor-2.9.2/gaphor/diagram/tools/dropzone.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/grayout.py` & `gaphor-2.9.2/gaphor/diagram/tools/grayout.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/magnet.py` & `gaphor-2.9.2/gaphor/diagram/tools/magnet.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/placement.py` & `gaphor-2.9.2/gaphor/diagram/tools/placement.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/segment.py` & `gaphor-2.9.2/gaphor/diagram/tools/segment.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/shortcut.py` & `gaphor-2.9.2/gaphor/diagram/tools/shortcut.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/textedit.py` & `gaphor-2.9.2/gaphor/diagram/tools/textedit.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/diagram/tools/txtool.py` & `gaphor-2.9.2/gaphor/diagram/tools/txtool.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/entrypoint.py` & `gaphor-2.9.2/gaphor/entrypoint.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/event.py` & `gaphor-2.9.2/gaphor/event.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/extensions/__pycache__/sphinx.cpython-310.pyc` & `gaphor-2.9.2/gaphor/extensions/__pycache__/sphinx.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4048 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d00f 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d00f 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 0001 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 0100 6400  Z.d.d.l.m.Z...d.
 00000050: 6402 6c05 5a06 6400 6404 6c07 6d08 5a08  d.l.Z.d.d.l.m.Z.
 00000060: 0100 6400 6405 6c09 6d0a 5a0a 0100 6400  ..d.d.l.m.Z...d.
 00000070: 6406 6c0b 6d0c 5a0c 0100 6400 6407 6c0d  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/extensions/sphinx.py` & `gaphor-2.9.2/gaphor/extensions/sphinx.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/i18n.py` & `gaphor-2.9.2/gaphor/i18n.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/ca/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/ca/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/de/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/de/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/es/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/es/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/fi/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/fi/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/fr/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/fr/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/gl/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/gl/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/hr/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/hr/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/hu/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/hu/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/it/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/it/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/ja/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/ja/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/ko/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/ko/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/nl/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/nl/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/pt_BR/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/pt_BR/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/ru/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/ru/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/sv/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/sv/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/locale/zh_Hans/LC_MESSAGES/gaphor.mo` & `gaphor-2.9.2/gaphor/locale/zh_Hans/LC_MESSAGES/gaphor.mo`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/plugins/__init__.py` & `gaphor-2.9.2/gaphor/plugins/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/plugins/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/plugins/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 605 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 5d02 0000  o.......C.3b]...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 5d02 0000  o.......6.5b]...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0001 0000 0040 0000 0073 0800 0000 6400  .....@...s....d.
 00000030: 5a00 6401 5300 2902 6156 0200 000a 506c  Z.d.S.).aV....Pl
 00000040: 7567 696e 730a 3d3d 3d3d 3d3d 3d0a 0a54  ugins.=======..T
 00000050: 6869 7320 6d6f 6475 6c65 2063 6f6e 7461  his module conta
 00000060: 696e 7320 6120 6275 6e63 6820 6f66 2073  ins a bunch of s
 00000070: 7461 6e64 6172 6420 706c 7567 696e 732e  tandard plugins.
```

### Comparing `gaphor-2.9.1/gaphor/plugins/console/__pycache__/console.cpython-310.pyc` & `gaphor-2.9.2/gaphor/plugins/console/__pycache__/console.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 9940 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d426 0000  o.......C.3b.&..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d426 0000  o.......6.5b.&..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000b 0000 0040 0000 0073 1c01 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6401 6c02 5a02 6400 6402 6c03 6d04 5a04  d.l.Z.d.d.l.m.Z.
 00000050: 6d05 5a05 0100 6400 6401 6c06 5a06 6400  m.Z...d.d.l.Z.d.
 00000060: 6403 6c07 6d08 5a08 6d09 5a09 6d0a 5a0a  d.l.m.Z.m.Z.m.Z.
 00000070: 6d0b 5a0b 0100 6400 6404 6c0c 6d0d 5a0d  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/plugins/console/__pycache__/consolewindow.cpython-310.pyc` & `gaphor-2.9.2/gaphor/plugins/console/__pycache__/consolewindow.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2702 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8e0a 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8e0a 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 8800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6402 6c02 6d03 5a03 6d04 5a04 0100 6400  d.l.m.Z.m.Z...d.
 00000050: 6403 6c05 6d06 5a06 0100 6400 6404 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6400 6405 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6406 6c0b 6d0c 5a0c 0100 6400  ..d.d.l.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/plugins/console/console.py` & `gaphor-2.9.2/gaphor/plugins/console/console.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/plugins/console/consolewindow.py` & `gaphor-2.9.2/gaphor/plugins/console/consolewindow.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/plugins/diagramexport/__init__.py` & `gaphor-2.9.2/gaphor/plugins/diagramexport/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/plugins/diagramexport/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/plugins/diagramexport/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2247 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c708 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c708 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 5600 0000 6400  .....@...sV...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 0100 6400  d.l.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6400 6404 6c0a 6d0b 5a0b 0100 4700  ..d.d.l.m.Z...G.
 00000070: 6405 6406 8400 6406 6502 6501 8304 5a0c  d.d...d.e.e...Z.
```

### Comparing `gaphor-2.9.1/gaphor/plugins/diagramexport/__pycache__/gaphorconvert.cpython-310.pyc` & `gaphor-2.9.2/gaphor/plugins/diagramexport/__pycache__/gaphorconvert.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3672 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 580e 0000  o.......C.3bX...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 580e 0000  o.......6.5bX...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 8e00 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6401 6c02 5a02 6400 6401 6c03 5a03 6400  d.l.Z.d.d.l.Z.d.
 00000050: 6402 6c04 6d05 5a05 0100 6400 6403 6c06  d.l.m.Z...d.d.l.
 00000060: 6d07 5a07 0100 6400 6404 6c08 6d09 5a09  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6405 6c0a 6d0b 5a0b 6d0c 5a0c  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/plugins/diagramexport/gaphorconvert.py` & `gaphor-2.9.2/gaphor/plugins/diagramexport/gaphorconvert.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/plugins/xmiexport/__init__.py` & `gaphor-2.9.2/gaphor/plugins/xmiexport/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/plugins/xmiexport/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/plugins/xmiexport/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1479 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 c705 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 c705 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 6400 0000 6400  .....@...sd...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6401 6404 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 6d07 5a07 0100 6401 6405 6c08  m.Z.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 6501 a00c 650d a101 5a0e 4700 6407  ..e...e...Z.G.d.
```

### Comparing `gaphor-2.9.1/gaphor/plugins/xmiexport/__pycache__/exportmodel.cpython-310.pyc` & `gaphor-2.9.2/gaphor/plugins/xmiexport/__pycache__/exportmodel.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 8695 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 f721 0000  o.......C.3b.!..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 f721 0000  o.......6.5b.!..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 3000 0000 6400  .....@...s0...d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6500 a003 6504 a101 5a05 4700 6403  ..e...e...Z.G.d.
 00000050: 6404 8400 6404 8302 5a06 6401 5300 2905  d...d...Z.d.S.).
 00000060: e900 0000 004e 2901 da09 584d 4c57 7269  .....N)...XMLWri
 00000070: 7465 7263 0000 0000 0000 0000 0000 0000  terc............
```

### Comparing `gaphor-2.9.1/gaphor/plugins/xmiexport/exportmodel.py` & `gaphor-2.9.2/gaphor/plugins/xmiexport/exportmodel.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/services/__pycache__/componentregistry.cpython-310.pyc` & `gaphor-2.9.2/gaphor/services/__pycache__/componentregistry.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1568 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2006 0000  o.......C.3b ...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2006 0000  o.......6.5b ...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 5c00 0000 6400  .....@...s\...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 0100 6401  m.Z.m.Z.m.Z...d.
 00000050: 6403 6c07 6d08 5a08 0100 6506 6404 6508  d.l.m.Z...e.d.e.
 00000060: 6405 8d02 5a09 4700 6406 6407 8400 6407  d...Z.G.d.d...d.
 00000070: 650a 8303 5a0b 4700 6408 6409 8400 6409  e...Z.G.d.d...d.
```

### Comparing `gaphor-2.9.1/gaphor/services/__pycache__/copyservice.cpython-310.pyc` & `gaphor-2.9.2/gaphor/services/__pycache__/copyservice.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4817 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d112 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d112 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 9000 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 0100  d.Z.d.d.l.m.Z...
 00000040: 6401 6403 6c03 6d04 5a04 6d05 5a05 0100  d.d.l.m.Z.m.Z...
 00000050: 6401 6404 6c06 6d07 5a07 6d08 5a08 0100  d.d.l.m.Z.m.Z...
 00000060: 6401 6405 6c09 6d0a 5a0a 6d0b 5a0b 0100  d.d.l.m.Z.m.Z...
 00000070: 6401 6406 6c0c 6d0d 5a0d 0100 6401 6407  d.d.l.m.Z...d.d.
```

### Comparing `gaphor-2.9.1/gaphor/services/__pycache__/modelinglanguage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/services/__pycache__/modelinglanguage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3107 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 230c 0000  o.......C.3b#...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 230c 0000  o.......6.5b#...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 7a00 0000 6400  .....@...sz...d.
 00000030: 6401 6c00 6d01 5a01 6d02 5a02 0100 6400  d.l.m.Z.m.Z...d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 0100 6400 6403 6c07 6d08 5a08 0100 6400  ..d.d.l.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6400 6405 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6400 6406 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/services/__pycache__/properties.cpython-310.pyc` & `gaphor-2.9.2/gaphor/services/__pycache__/properties.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4795 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 bb12 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 bb12 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 ca00 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6402 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 5a02 6401 6402 6c03 5a03 6401 6402 6c04  Z.d.d.l.Z.d.d.l.
 00000050: 5a04 6401 6403 6c05 6d06 5a06 0100 6401  Z.d.d.l.m.Z...d.
 00000060: 6404 6c07 6d08 5a08 0100 6401 6405 6c09  d.l.m.Z...d.d.l.
 00000070: 6d0a 5a0a 0100 6401 6406 6c0b 6d0c 5a0c  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/services/__pycache__/undomanager.cpython-310.pyc` & `gaphor-2.9.2/gaphor/services/__pycache__/undomanager.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 14918 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 463a 0000  o.......C.3bF:..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 463a 0000  o.......6.5bF:..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 2e01 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 0100 6401  m.Z.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6401  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 0100 6401 6406 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/services/componentregistry.py` & `gaphor-2.9.2/gaphor/services/componentregistry.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/services/copyservice.py` & `gaphor-2.9.2/gaphor/services/copyservice.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/services/helpservice/__init__.py` & `gaphor-2.9.2/gaphor/services/helpservice/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/services/helpservice/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/services/helpservice/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1407 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7f05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7f05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 5a00 0000 6400  .....@...sZ...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 0100 6401  d.l.m.Z.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 0100 6401 6405 6c08  d.l.m.Z...d.d.l.
 00000060: 6d09 5a09 0100 6401 6406 6c0a 6d0b 5a0b  m.Z...d.d.l.m.Z.
 00000070: 0100 4700 6407 6408 8400 6408 6505 6504  ..G.d.d...d.e.e.
```

### Comparing `gaphor-2.9.1/gaphor/services/helpservice/about.ui` & `gaphor-2.9.2/gaphor/services/helpservice/about.ui`

 * *Files 1% similar despite different names*

#### Comparing `gaphor-2.9.1/gaphor/services/helpservice/about.ui` & `gaphor-2.9.2/gaphor/services/helpservice/about.ui`

```diff
@@ -2,15 +2,15 @@
 <!-- Generated with glade 3.22.2 -->
 <interface>
   <requires lib="gtk+" version="3.20"/>
   <object class="GtkAboutDialog" id="about">
     <property name="modal">true</property>
     <property name="program_name">Gaphor</property>
     <property name="title" translatable="yes">About Gaphor</property>
-    <property name="version">2.9.1</property>
+    <property name="version">2.9.2</property>
     <property name="copyright" translatable="yes">Copyright © 2001-2022 Arjan J. Molenaar and Dan Yeaw</property>
     <property name="comments" translatable="yes">Gaphor is the simple modeling tool written in Python</property>
     <property name="website">https://github.com/gaphor/gaphor</property>
     <property name="website_label" translatable="yes">Fork me on GitHub</property>
     <property name="license" translatable="yes">Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);
 you may not use this application except in compliance with the
 License. You may obtain a copy of the License at
```

### Comparing `gaphor-2.9.1/gaphor/services/helpservice/shortcuts.ui` & `gaphor-2.9.2/gaphor/services/helpservice/shortcuts.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/services/modelinglanguage.py` & `gaphor-2.9.2/gaphor/services/modelinglanguage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/services/properties.py` & `gaphor-2.9.2/gaphor/services/properties.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/services/undomanager.py` & `gaphor-2.9.2/gaphor/services/undomanager.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/storage/__pycache__/parser.cpython-310.pyc` & `gaphor-2.9.2/gaphor/storage/__pycache__/parser.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 12167 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 872f 0000  o.......C.3b./..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 872f 0000  o.......6.5b./..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000a 0000 0040 0000 0173 0a01 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6403 6c04 5a04 6401  d.l.Z.d.d.l.Z.d.
 00000050: 6403 6c05 5a05 6401 6404 6c06 6d07 5a07  d.l.Z.d.d.l.m.Z.
 00000060: 0100 6401 6405 6c08 6d09 5a09 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6406 6c0a 6d0b 5a0b 0100 6401 6407 6c0c  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/storage/__pycache__/storage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/storage/__pycache__/storage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 12972 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 ac32 0000  o.......C.3b.2..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 ac32 0000  o.......6.5b.2..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 2c01 0000 6400  .....@...s,...d.
 00000030: 5a00 6401 6402 6702 5a01 6403 6404 6c02  Z.d.d.g.Z.d.d.l.
 00000040: 5a02 6403 6404 6c03 5a03 6403 6404 6c04  Z.d.d.l.Z.d.d.l.
 00000050: 5a05 6403 6405 6c06 6d07 5a07 0100 6403  Z.d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a09 0100 6403 6407 6c0a  d.l.m.Z...d.d.l.
 00000070: 6d0b 5a0b 0100 6403 6408 6c0c 6d0d 5a0d  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/storage/__pycache__/upgrade_canvasitem.cpython-310.pyc` & `gaphor-2.9.2/gaphor/storage/__pycache__/upgrade_canvasitem.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 3827 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 f30e 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 f30e 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0002 0000 0040 0000 0073 5800 0000 6400  .....@...sX...d.
 00000030: 6401 6c00 6d01 5a01 0100 6402 6403 8400  d.l.m.Z...d.d...
 00000040: 5a02 6404 6405 8400 5a03 6406 6407 8400  Z.d.d...Z.d.d...
 00000050: 5a04 6408 6409 8400 5a05 640a 640b 8400  Z.d.d...Z.d.d...
 00000060: 5a06 640c 640d 8400 5a07 640e 640f 8400  Z.d.d...Z.d.d...
 00000070: 5a08 6410 6411 8400 5a09 6412 6413 8400  Z.d.d...Z.d.d...
```

### Comparing `gaphor-2.9.1/gaphor/storage/__pycache__/xmlwriter.cpython-310.pyc` & `gaphor-2.9.2/gaphor/storage/__pycache__/xmlwriter.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4707 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6312 0000  o.......C.3bc...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6312 0000  o.......6.5bc...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 7c00 0000 6400  .....@...s|...d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a02 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 0100 6400 6403 6c07 6d08 5a08 6d09 5a09  ..d.d.l.m.Z.m.Z.
 00000060: 0100 7a0b 6400 6404 6c0a 6d0b 5a0b 0100  ..z.d.d.l.m.Z...
 00000070: 6405 5a0c 5b0b 5700 6e0b 0400 650d 7930  d.Z.[.W.n...e.y0
```

### Comparing `gaphor-2.9.1/gaphor/storage/parser.py` & `gaphor-2.9.2/gaphor/storage/parser.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/storage/storage.py` & `gaphor-2.9.2/gaphor/storage/storage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/storage/upgrade_canvasitem.py` & `gaphor-2.9.2/gaphor/storage/upgrade_canvasitem.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/storage/xmlwriter.py` & `gaphor-2.9.2/gaphor/storage/xmlwriter.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/templates/blank.gaphor` & `gaphor-2.9.2/gaphor/templates/blank.gaphor`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/templates/c4model.gaphor` & `gaphor-2.9.2/gaphor/templates/c4model.gaphor`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/templates/raaml.gaphor` & `gaphor-2.9.2/gaphor/templates/raaml.gaphor`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/templates/sysml.gaphor` & `gaphor-2.9.2/gaphor/templates/sysml.gaphor`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/templates/uml.gaphor` & `gaphor-2.9.2/gaphor/templates/uml.gaphor`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/transaction.py` & `gaphor-2.9.2/gaphor/transaction.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/__init__.py` & `gaphor-2.9.2/gaphor/ui/__init__.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/__init__.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/__init__.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5883 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 fb16 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 fb16 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 7c01 0000 6400  .....@...s|...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6402 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 5a02 6401 6402 6c03 5a03 6401 6403 6c04  Z.d.d.l.Z.d.d.l.
 00000050: 6d05 5a05 0100 6401 6404 6c06 6d07 5a07  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6402 6c08 5a08 6401 6402 6c09  ..d.d.l.Z.d.d.l.
 00000070: 5a09 6502 a00a 6405 a101 6406 6b03 7271  Z.e...d...d.k.rq
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/abc.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/abc.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 687 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 af02 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 af02 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 3400 0000 6400  .....@...s4...d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c03 6d04 5a04 0100 4700  ..d.d.l.m.Z...G.
 00000050: 6404 6405 8400 6405 6504 8303 5a05 6401  d.d...d.e...Z.d.
 00000060: 5300 2906 e900 0000 004e 2901 da05 5475  S.)......N)...Tu
 00000070: 706c 6529 01da 0753 6572 7669 6365 6300  ple)...Servicec.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/actiongroup.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/actiongroup.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5764 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 8416 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 8416 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 0601 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 6d05 5a05 0100 6400  m.Z.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 0100 6404 6405 8400  d.l.m.Z...d.d...
 00000060: 5a08 6505 a009 a100 6406 6b02 723d 4700  Z.e.....d.k.r=G.
 00000070: 6407 6408 8400 6408 6501 8303 5a0a 6409  d.d...d.e...Z.d.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/appfilemanager.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/appfilemanager.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1794 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0207 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0207 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 7800 0000 6400  .....@...sx...d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a02 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6402 6c03 6d04 5a04 6d05 5a05 0100 6400  d.l.m.Z.m.Z...d.
 00000050: 6403 6c06 6d07 5a07 6d08 5a08 0100 6400  d.l.m.Z.m.Z...d.
 00000060: 6404 6c09 6d0a 5a0a 0100 6400 6405 6c0b  d.l.m.Z...d.d.l.
 00000070: 6d0c 5a0c 0100 6500 a00d 650e a101 5a0f  m.Z...e...e...Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/diagrampage.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/diagrampage.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 13061 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0533 0000  o.......C.3b.3..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0533 0000  o.......6.5b.3..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 e001 0000 5500  .....@...s....U.
 00000030: 6400 6401 6c00 5a00 6400 6401 6c01 5a01  d.d.l.Z.d.d.l.Z.
 00000040: 6400 6401 6c02 5a02 6400 6402 6c03 6d04  d.d.l.Z.d.d.l.m.
 00000050: 5a04 6d05 5a05 0100 6400 6403 6c06 6d07  Z.m.Z...d.d.l.m.
 00000060: 5a07 0100 6400 6404 6c08 6d09 5a09 6d0a  Z...d.d.l.m.Z.m.
 00000070: 5a0a 6d0b 5a0b 0100 6400 6405 6c0c 6d0d  Z.m.Z...d.d.l.m.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/diagrams.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/diagrams.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 12665 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 7931 0000  o.......C.3by1..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 7931 0000  o.......6.5by1..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0173 d800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 0100 6400  Z.d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6400 6406 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 6d0b 5a0b 0100 6400 6407 6c0c 6d0d 5a0d  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/elementeditor.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/elementeditor.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 11364 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 642c 0000  o.......C.3bd,..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 642c 0000  o.......6.5bd,..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 0401 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/errorhandler.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/errorhandler.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1243 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 db04 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 db04 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 3a00 0000 6400  .....@...s:...d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6402 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 5a02 6401 6403 6c03 6d04 5a04 0100 6401  Z.d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6408 6406 6407  d.l.m.Z...d.d.d.
 00000060: 8401 5a07 6402 5300 2909 7ade 4120 6765  ..Z.d.S.).z.A ge
 00000070: 6e65 7269 6320 7761 7920 746f 2068 616e  neric way to han
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/event.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/event.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 614 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6602 0000  o.......C.3bf...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6602 0000  o.......6.5bf...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 4e00 0000 6400  .....@...sN...d.
 00000030: 5a00 4700 6401 6402 8400 6402 8302 5a01  Z.G.d.d...d...Z.
 00000040: 4700 6403 6404 8400 6404 8302 5a02 4700  G.d.d...d...Z.G.
 00000050: 6405 6406 8400 6406 8302 5a03 4700 6407  d.d...d...Z.G.d.
 00000060: 6408 8400 6408 8302 5a04 4700 6409 640a  d...d...Z.G.d.d.
 00000070: 8400 640a 8302 5a05 640b 5300 290c 7a12  ..d...Z.d.S.).z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/filedialog.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/filedialog.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 2358 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3609 0000  o.......C.3b6...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3609 0000  o.......6.5b6...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 d200 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6401 6404 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6401 6405 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6508 6406 8301 6407 6408 6603 6701  ..e.d...d.d.f.g.
 00000070: 5a09 6419 6409 640a 8401 5a0a 640b 640c  Z.d.d.d...Z.d.d.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/filemanager.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/filemanager.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 10526 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 1e29 0000  o.......C.3b.)..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 1e29 0000  o.......6.5b.)..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 1e01 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a01 6401 6403 6c02  Z.d.d.l.Z.d.d.l.
 00000040: 6d03 5a03 0100 6401 6404 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 6d08 5a08  ..d.d.l.m.Z.m.Z.
 00000060: 0100 6401 6406 6c09 6d0a 5a0a 0100 6401  ..d.d.l.m.Z...d.
 00000070: 6407 6c0b 6d0c 5a0c 6d0d 5a0d 0100 6401  d.l.m.Z.m.Z...d.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/greeter.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/greeter.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 6788 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 841a 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 841a 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0009 0000 0040 0000 0073 2201 0000 6400  .....@...s"...d.
 00000030: 6401 6c00 5a01 6400 6402 6c02 6d03 5a03  d.l.Z.d.d.l.m.Z.
 00000040: 0100 6400 6403 6c04 6d05 5a05 0100 6400  ..d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 0100 6400  d.l.m.Z.m.Z...d.
 00000060: 6405 6c09 6d0a 5a0a 6d0b 5a0b 0100 6400  d.l.m.Z.m.Z...d.
 00000070: 6406 6c0c 6d0d 5a0d 0100 6400 6407 6c0e  d.l.m.Z...d.d.l.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/layout.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/layout.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4052 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d40f 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d40f 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 de00 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 6d02 5a02 6d03  d.Z.d.d.l.m.Z.m.
 00000040: 5a03 0100 6401 6403 6c04 6d05 5a05 0100  Z...d.d.l.m.Z...
 00000050: 6401 6404 6c06 6d07 5a07 6d08 5a08 0100  d.d.l.m.Z.m.Z...
 00000060: 6508 a009 a100 6405 6b02 722a 6406 6508  e.....d.k.r*d.e.
 00000070: 6a0a 6407 650b 6604 6408 6409 8404 5a0c  j.d.e.f.d.d...Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/macosshim.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/macosshim.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 836 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4403 0000  o.......C.3bD...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4403 0000  o.......6.5bD...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 8400 0000 7a1c  .....@...s....z.
 00000030: 6400 6401 6c00 5a00 6400 6402 6c01 6d02  d.d.l.Z.d.d.l.m.
 00000040: 5a02 0100 6502 a003 a100 6403 6b02 7218  Z...e.....d.k.r.
 00000050: 6500 a004 6404 6405 a102 0100 6e03 6505  e...d.d.....n.e.
 00000060: 8300 8201 5700 6e0c 0400 6505 7928 0100  ....W.n...e.y(..
 00000070: 0100 0100 6401 5a06 5900 6401 5300 7700  ....d.Z.Y.d.S.w.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/mainwindow.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/mainwindow.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 9761 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 2126 0000  o.......C.3b!&..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 2126 0000  o.......6.5b!&..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0073 2001 0000 6400  .....@...s ...d.
 00000030: 5a00 6401 6402 6c01 5a02 6401 6402 6c03  Z.d.d.l.Z.d.d.l.
 00000040: 5a03 6401 6403 6c04 6d05 5a05 0100 6401  Z.d.d.l.m.Z...d.
 00000050: 6404 6c06 6d07 5a07 6d08 5a08 6d09 5a09  d.l.m.Z.m.Z.m.Z.
 00000060: 0100 6401 6405 6c0a 6d0b 5a0b 6d0c 5a0c  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6401 6406 6c0d 6d0e 5a0e 6d0f 5a0f  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/menufragment.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/menufragment.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 837 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 4503 0000  o.......C.3bE...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 4503 0000  o.......6.5bE...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 3800 0000 6400  .....@...s8...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 4700 6404 6405 8400 6405 6503 8303  ..G.d.d...d.e...
 00000060: 5a06 6406 5300 2907 e900 0000 0029 01da  Z.d.S.)......)..
 00000070: 0347 696f 2901 da07 5365 7276 6963 6529  .Gio)...Service)
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/namespace.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/namespace.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 12389 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6530 0000  o.......C.3be0..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6530 0000  o.......6.5be0..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0005 0000 0040 0000 0173 4801 0000 6400  .....@...sH...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 5a03 6401 6404 6c04 6d05 5a05  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6401 6405 6c06 6d07 5a07 0100 6401  ..d.d.l.m.Z...d.
 00000060: 6406 6c08 6d09 5a09 6d0a 5a0a 6d0b 5a0b  d.l.m.Z.m.Z.m.Z.
 00000070: 6d0c 5a0c 0100 6401 6407 6c0d 6d0e 5a0e  m.Z...d.d.l.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/namespacemodel.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/namespacemodel.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 10409 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a928 0000  o.......C.3b.(..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a928 0000  o.......6.5b.(..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0173 1e01 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 0100 6400  Z.d.d.l.m.Z...d.
 00000050: 6404 6c05 6d06 5a06 0100 6400 6405 6c07  d.l.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6400 6406 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 0100 6400 6407 6c0b 6d0c 5a0c 6d0d 5a0d  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/namespaceview.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/namespaceview.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 5541 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a515 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a515 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0173 b400 0000 6400  .....@...s....d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 5a02 6400 6403 6c03 6d04 5a04 6d05 5a05  Z.d.d.l.m.Z.m.Z.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6400 6405 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 6d0e 5a0e  ..d.d.l.m.Z.m.Z.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/notification.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/notification.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 977 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 11% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 d103 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 d103 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 3a00 0000 6400  .....@...s:...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 6404 5a06 4700 6405 6406 8400 6406  ..d.Z.G.d.d...d.
 00000060: 8302 5a07 6407 5300 2908 e900 0000 0029  ..Z.d.S.)......)
 00000070: 01da 0447 4c69 6229 01da 0d65 7665 6e74  ...GLib)...event
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/questiondialog.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/questiondialog.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1082 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 3a04 0000  o.......C.3b:...
+00000000: 6f0d 0d0a 0000 0000 361b 3562 3a04 0000  o.......6.5b:...
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 2200 0000 6400  .....@...s"...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 4700  Z.d.d.l.m.Z...G.
 00000040: 6403 6404 8400 6404 8302 5a03 6405 5300  d.d...d...Z.d.S.
 00000050: 2906 7a4c 4465 6669 6e65 7320 6120 5175  ).zLDefines a Qu
 00000060: 6573 7469 6f6e 4469 616c 6f67 2063 6c61  estionDialog cla
 00000070: 7373 2075 7365 6420 746f 2067 6574 2061  ss used to get a
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/recentfiles.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/recentfiles.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1470 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 be05 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 be05 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 6400 0000 6400  .....@...sd...d.
 00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
 00000040: 6d03 5a03 6d04 5a04 0100 6400 6403 6c05  m.Z.m.Z...d.d.l.
 00000050: 6d06 5a06 0100 6400 6404 6c07 6d08 5a08  m.Z...d.d.l.m.Z.
 00000060: 0100 6400 6405 6c09 6d0a 5a0a 6d0b 5a0b  ..d.d.l.m.Z.m.Z.
 00000070: 0100 6400 6406 6c0c 6d0d 5a0d 0100 4700  ..d.d.l.m.Z...G.
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/statuswindow.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/statuswindow.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 4261 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 a510 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 a510 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0003 0000 0040 0000 0073 4a00 0000 6400  .....@...sJ...d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 0100 6401  Z.d.d.l.m.Z...d.
 00000040: 6403 6c03 6d04 5a04 6d05 5a05 6d06 5a06  d.l.m.Z.m.Z.m.Z.
 00000050: 6d07 5a07 0100 4700 6404 6405 8400 6405  m.Z...G.d.d...d.
 00000060: 8302 5a08 6406 6407 8400 5a09 6408 6409  ..Z.d.d...Z.d.d.
 00000070: 8400 5a0a 640a 5300 290b 7a45 4465 6669  ..Z.d.S.).zEDefi
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/styling.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/styling.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 1800 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 0807 0000  o.......C.3b....
+00000000: 6f0d 0d0a 0000 0000 361b 3562 0807 0000  o.......6.5b....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0004 0000 0040 0000 0073 3800 0000 6400  .....@...s8...d.
 00000030: 6401 6c00 5a00 6400 6402 6c01 6d02 5a02  d.l.Z.d.d.l.m.Z.
 00000040: 6d03 5a03 0100 6400 6403 6c04 6d05 5a05  m.Z...d.d.l.m.Z.
 00000050: 0100 4700 6404 6405 8400 6405 6505 8303  ..G.d.d...d.e...
 00000060: 5a06 6401 5300 2906 e900 0000 004e 2902  Z.d.S.)......N).
 00000070: da03 4764 6bda 0347 746b 2901 da07 5365  ..Gdk..Gtk)...Se
```

### Comparing `gaphor-2.9.1/gaphor/ui/__pycache__/toolbox.cpython-310.pyc` & `gaphor-2.9.2/gaphor/ui/__pycache__/toolbox.cpython-310.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.10, timestamp-based, .py timestamp: Fri Mar 18 01:28:35 2022 UTC, .py size: 12140 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 6f0d 0d0a 0000 0000 43e0 3362 6c2f 0000  o.......C.3bl/..
+00000000: 6f0d 0d0a 0000 0000 361b 3562 6c2f 0000  o.......6.5bl/..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 000c 0000 0040 0000 0073 ca01 0000 5500  .....@...s....U.
 00000030: 6400 5a00 6401 6402 6c01 5a01 6401 6402  d.Z.d.d.l.Z.d.d.
 00000040: 6c02 5a02 6401 6403 6c03 6d04 5a04 6d05  l.Z.d.d.l.m.Z.m.
 00000050: 5a05 0100 6401 6404 6c06 6d07 5a07 6d08  Z...d.d.l.m.Z.m.
 00000060: 5a08 6d09 5a09 0100 6401 6405 6c0a 6d0b  Z.m.Z...d.d.l.m.
 00000070: 5a0b 6d0c 5a0c 0100 6401 6406 6c0d 6d0e  Z.m.Z...d.d.l.m.
```

### Comparing `gaphor-2.9.1/gaphor/ui/abc.py` & `gaphor-2.9.2/gaphor/ui/abc.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/actiongroup.py` & `gaphor-2.9.2/gaphor/ui/actiongroup.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/appfilemanager.py` & `gaphor-2.9.2/gaphor/ui/appfilemanager.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/diagrampage.py` & `gaphor-2.9.2/gaphor/ui/diagrampage.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/diagrams.py` & `gaphor-2.9.2/gaphor/ui/diagrams.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/elementeditor.glade` & `gaphor-2.9.2/gaphor/ui/elementeditor.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/elementeditor.py` & `gaphor-2.9.2/gaphor/ui/elementeditor.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/elementeditor.ui` & `gaphor-2.9.2/gaphor/ui/elementeditor.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/errorhandler.py` & `gaphor-2.9.2/gaphor/ui/errorhandler.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/event.py` & `gaphor-2.9.2/gaphor/ui/event.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/filedialog.py` & `gaphor-2.9.2/gaphor/ui/filedialog.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/filemanager.py` & `gaphor-2.9.2/gaphor/ui/filemanager.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/greeter-model-template.glade` & `gaphor-2.9.2/gaphor/ui/greeter-model-template.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/greeter-model-template.ui` & `gaphor-2.9.2/gaphor/ui/greeter-model-template.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/greeter-recent-file.glade` & `gaphor-2.9.2/gaphor/ui/greeter-recent-file.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/greeter-recent-file.ui` & `gaphor-2.9.2/gaphor/ui/greeter-recent-file.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/greeter.glade` & `gaphor-2.9.2/gaphor/ui/greeter.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/greeter.py` & `gaphor-2.9.2/gaphor/ui/greeter.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/greeter.ui` & `gaphor-2.9.2/gaphor/ui/greeter.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/Makefile` & `gaphor-2.9.2/gaphor/ui/icons/Makefile`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-abstract-operational-situation-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-abstract-operational-situation-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-accept-event-action-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-accept-event-action-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-action-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-action-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-final-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-final-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-partition-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-partition-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-activity-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actor-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actor-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actuator-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-actuator-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-and-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-and-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-artifact-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-artifact-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-association-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-association-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-basic-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-basic-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-behavior-execution-specification-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-behavior-execution-specification-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-block-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-block-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-box-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-box-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-component-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-component-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-container-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-container-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-database-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-database-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-person-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-person-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-software-system-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-c4-software-system-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-class-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-class-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-line-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-line-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-comment-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-component-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-component-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-composite-association-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-composite-association-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-conditional-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-conditional-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-connector-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-connector-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-constraint-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-constraint-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-containment-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-containment-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-action-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-action-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-flow-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-flow-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-structure-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-control-structure-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controlled-process-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controlled-process-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controller-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-controller-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-data-type-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-data-type-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-decision-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-decision-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dependency-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dependency-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-derive-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-derive-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-device-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-device-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-diagram-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-diagram-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dormant-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-dormant-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-ellipse-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-ellipse-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-enumeration-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-enumeration-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-execution-specification-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-execution-specification-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extend-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extend-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extension-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-extension-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-final-state-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-final-state-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-flow-final-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-flow-final-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-fork-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-fork-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-generalization-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-generalization-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-hazard-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-hazard-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-house-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-house-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-import-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-import-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-include-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-include-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-information-flow-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-information-flow-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-inhibit-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-inhibit-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-pseudostate-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-initial-pseudostate-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interaction-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interaction-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-realization-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-realization-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-interface-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-intermediate-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-intermediate-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-item-flow-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-item-flow-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-join-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-join-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-lifeline-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-lifeline-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-line-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-line-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-loss-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-loss-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-magnet-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-magnet-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-majority_vote-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-majority_vote-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-message-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-message-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-metaclass-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-metaclass-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-new-diagram-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-new-diagram-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-not-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-not-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-flow-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-flow-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-node-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-object-node-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-operational-situation-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-operational-situation-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-or-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-or-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-package-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-package-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pointer-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pointer-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-primitive-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-primitive-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-profile-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-profile-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-property-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-property-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-proxyport-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-proxyport-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pseudostate-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-pseudostate-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-realization-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-realization-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-refine-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-refine-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-reflexive-message-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-reflexive-message-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-region-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-region-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-relevant-to-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-relevant-to-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-requirement-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-requirement-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-satisfy-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-satisfy-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-send-signal-action-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-send-signal-action-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-seq-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-seq-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-shared-association-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-shared-association-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-situation-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-situation-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-machine-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-machine-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-state-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-stereotype-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-stereotype-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-top-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-top-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-trace-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-trace-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-in-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-in-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-out-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transfer-out-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transition-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-transition-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-undeveloped-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-undeveloped-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-unsafe-control-action-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-unsafe-control-action-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-usage-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-usage-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-use-case-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-use-case-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-value-type-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-value-type-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-verify-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-verify-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-view-editor-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-view-editor-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-xor-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-xor-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/actions/gaphor-zero-event-symbolic.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/actions/gaphor-zero-event-symbolic.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/apps/org.gaphor.Gaphor.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/apps/org.gaphor.Gaphor.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/C4Model.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/C4Model.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/RAAML.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/RAAML.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/SysML.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/SysML.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/hicolor/scalable/emblems/UML.svg` & `gaphor-2.9.2/gaphor/ui/icons/hicolor/scalable/emblems/UML.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/icons/stensil.svg` & `gaphor-2.9.2/gaphor/ui/icons/stensil.svg`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/layout.py` & `gaphor-2.9.2/gaphor/ui/layout.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/macosshim.py` & `gaphor-2.9.2/gaphor/ui/macosshim.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/mainwindow.glade` & `gaphor-2.9.2/gaphor/ui/mainwindow.glade`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/mainwindow.py` & `gaphor-2.9.2/gaphor/ui/mainwindow.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/mainwindow.ui` & `gaphor-2.9.2/gaphor/ui/mainwindow.ui`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/menufragment.py` & `gaphor-2.9.2/gaphor/ui/menufragment.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/namespace.py` & `gaphor-2.9.2/gaphor/ui/namespace.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/namespacemodel.py` & `gaphor-2.9.2/gaphor/ui/namespacemodel.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/namespaceview.py` & `gaphor-2.9.2/gaphor/ui/namespaceview.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/notification.py` & `gaphor-2.9.2/gaphor/ui/notification.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/placement-icon-base.png` & `gaphor-2.9.2/gaphor/ui/placement-icon-base.png`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/questiondialog.py` & `gaphor-2.9.2/gaphor/ui/questiondialog.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/recentfiles.py` & `gaphor-2.9.2/gaphor/ui/recentfiles.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/statuswindow.py` & `gaphor-2.9.2/gaphor/ui/statuswindow.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/styling.css` & `gaphor-2.9.2/gaphor/ui/styling.css`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/styling.py` & `gaphor-2.9.2/gaphor/ui/styling.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/gaphor/ui/toolbox.py` & `gaphor-2.9.2/gaphor/ui/toolbox.py`

 * *Files identical despite different names*

### Comparing `gaphor-2.9.1/pyproject.toml` & `gaphor-2.9.2/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "gaphor"
-version = "2.9.1"
+version = "2.9.2"
 description = "Gaphor is the simple modeling tool written in Python."
 authors = [
     "Arjan J. Molenaar <gaphor@gmail.com>",
     "Dan Yeaw <dan@yeaw.me>"
 ]
 
 readme = "README.md"
```

### Comparing `gaphor-2.9.1/setup.py` & `gaphor-2.9.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -128,15 +128,15 @@
                      'toolbox = gaphor.ui.toolbox:Toolbox',
                      'tools_menu = gaphor.ui.menufragment:MenuFragment',
                      'undo_manager = gaphor.services.undomanager:UndoManager',
                      'xmi_export = gaphor.plugins.xmiexport:XMIExport']}
 
 setup_kwargs = {
     'name': 'gaphor',
-    'version': '2.9.1',
+    'version': '2.9.2',
     'description': 'Gaphor is the simple modeling tool written in Python.',
     'long_description': '<h1 align="center"><img src="https://github.com/gaphor/gaphor/blob/master/logos/gaphor-logo-full.svg?raw=true" alt="Gaphor - UML/SysML Modeling" height="96"/></h1>\n\n[![Build](https://github.com/gaphor/gaphor/actions/workflows/full-build.yml/badge.svg)](https://github.com/gaphor/gaphor/actions/workflows/full-build.yml)\n[![Docs build state](https://readthedocs.org/projects/gaphor/badge/?version=latest)](https://gaphor.readthedocs.io)\n[![PyPI](https://img.shields.io/pypi/v/gaphor.svg)](https://pypi.org/project/gaphor)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/gaphor)](https://pypistats.org/packages/gaphor)\n[![Matrix](https://img.shields.io/badge/chat-on%20Matrix-success)](https://app.element.io/#/room/#gaphor_Lobby:gitter.im)\n\n[![Maintainability](https://api.codeclimate.com/v1/badges/f00974f5d7fe69fe4ecd/maintainability)](https://codeclimate.com/github/gaphor/gaphor/maintainability)\n[![Test Coverage](https://api.codeclimate.com/v1/badges/f00974f5d7fe69fe4ecd/test_coverage)](https://codeclimate.com/github/gaphor/gaphor/test_coverage)\n[![Translation Status](https://hosted.weblate.org/widgets/gaphor/-/gaphor/svg-badge.svg)](https://hosted.weblate.org/engage/gaphor)\n[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme)\n[![All Contributors](https://img.shields.io/badge/all_contributors-32-brightgreen.svg)](#contributors)\n\n\nGaphor is a UML and SysML modeling application written in Python.\nIt is designed to be easy to use, while still being powerful. Gaphor implements a fully-compliant UML 2 data model, so it is much more than a picture drawing tool. You can use Gaphor to quickly visualize different aspects of a system as well as create complete, highly complex models.\n\n<img alt="Gaphor Demo" src="https://raw.githubusercontent.com/gaphor/gaphor/master/docs/images/gaphor-demo.gif" style="width: 68%; display: block; margin: 2em auto">\n\n## 📑 Table of Contents\n\n- [Background](#background)\n- [Install](#floppy_disk-install)\n- [Usage](#usage)\n- [Contributing](#contributing)\n- [License](#license)\n\n## 📜 Background\n\nGaphor is a UML and SysML modeling application written in Python. We designed\nit to be easy to use, while still being powerful. Gaphor implements a\nfully-compliant UML 2 data model, so it is much more than a picture drawing\ntool. You can use Gaphor to quickly visualize different aspects of a system as\nwell as create complete, highly complex models.\n\nGaphor is designed around the following principles:\n\n- Simplicity: The application should be easy to use. Only some basic knowledge of UML or SysML is required.\n- Consistency: UML is a graphical modeling language, so all modeling is done in a diagram.\n- Workability: The application should not bother the user every time they do something non-UML-ish.\n\nGaphor is a GUI application that is built on [GTK](https://gtk.org) and\n[Cairo](https://www.cairographics.org/).\n[PyGObject](https://pygobject.readthedocs.io/) and\n[PyCairo](https://pycairo.readthedocs.io/) provide Python bindings for those\nlibraries. [Gaphas](https://github.com/gaphor/gaphas) provides the foundational\ndiagramming functionality.\n\n## 💾 Install\n\nYou can find [the latest version](https://gaphor.org/download) on the\n[gaphor.org website](https://gaphor.org/download). Gaphor ships installers for\nmacOS and Windows. Those can be found there. The Python package is also\n[available on PyPI](https://pypi.org/project/gaphor/).\n\nAll releases are available on\n[GitHub](https://github.com/gaphor/gaphor/releases/).\n\nIf you want to start developing on Gaphor, have a look at the [Installation\nsection of our Tech docs](https://gaphor.readthedocs.io/en/latest/).\n\n## 🔦 Usage\n### Creating models\n\nIf using Gaphor for the first time you will be presented with a greeter dialog\nat startup in which you can select one of 5 models available to you to work in:\n- **Generic:** (or blank) template\n- **UML:** *Unified Modeling Language* template\n- **SysML:** *Systems Modeling Language* template\n- **RAAML:** *Risk Analysis and Assessment Modeling language* template\n- **C4 Model:** *a lean graphical notation technique for modelling the architecture of software systems* template\n\nAfter you select a template, the main Gaphor Window will load, and you will be\nready to start modeling. Gaphor will automatically select the correct profile\nbased on the template that you selected, but you can also select other modeling\nprofiles if needed by clicking on the button next to the Profile dropdown menu\nat the top of your window.\n\nTo select an element you want to place, for example a Class, click on the icon\nin the Toolbox and then again on the diagram. This will place a new Class item\non the diagram and add a new Class to the model (it shows up in the Navigation).\nThe selected tool will reset itself to the Pointer tool if the option \'\'Diagram\n-> Reset tool\'\' is selected.\n\nPortions of the toolbox may also be collapsed depending on the type of diagram\nyou are modeling with. You can expand the collapsed portions of the toolbox if\nneeded.\n\n### Create a New Diagram\n\n1. Use the Navigation to select an element that can contain a diagram (a\nPackage or Profile)\n2. Select the New diagram button in the upper left and select the type of\ndiagram you would like to create from the dropdown.\n\nIt is also possible to create a new diagram by right clicking on a Package or\nProfile in the Navigation and selecting New Diagram.\n\n### Copy and Paste\n\nItems in a diagram can be copied and pasted in the same diagram or other\ndiagrams.\n\nCtrl+V: The default way to paste uses a link defining elements mode. This places\nan existing item in the diagram, but the item itself is not duplicated. In other\nwords, if you paste a Class object in a diagram, the Class will be added to the\ndiagram, but there will be no new Class in the Navigation.\n\nShift+Ctrl+V: Copy defining elements. This places a new item in the model by\nfully duplicating the item that was copied.\n\n### Drag and Drop\n\nAdding an existing element to a diagram is done by dragging the element from\nthe Navigation section onto a diagram. Diagrams and attribute/operations of a\nClass show up in the Navigation but can not be added to a diagram.\n\nElements can also be dragged within the Navigation in order to rearrange them\nin to different packages.\n\n## ♥ Contributing\n\nThanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tr>\n    <td align="center"><a href="https://github.com/abjurstrom-torch"><img src="https://avatars1.githubusercontent.com/u/62608984?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adam Bjurstrom</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Aabjurstrom-torch" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="http://www.boduch.ca"><img src="https://avatars2.githubusercontent.com/u/114619?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adam Boduch</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=adamboduch" title="Code">💻</a> <a href="https://github.com/gaphor/gaphor/commits?author=adamboduch" title="Tests">⚠️</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Aadamboduch" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/Alexander-Wilms"><img src="https://avatars2.githubusercontent.com/u/3226457?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexander Wilms</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3AAlexander-Wilms" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="http://www.aejh.co.uk"><img src="https://avatars1.githubusercontent.com/u/927233?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexis Howells</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=aejh" title="Documentation">📖</a></td>\n    <td align="center"><a href="https://ayanamy.is-a.dev/"><img src="https://avatars.githubusercontent.com/u/50583248?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Amy Y</b></sub></a><br /><a href="#translation-jy1263" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/amolenaar"><img src="https://avatars0.githubusercontent.com/u/96249?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Arjan Molenaar</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=amolenaar" title="Code">💻</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Aamolenaar" title="Bug reports">🐛</a> <a href="https://github.com/gaphor/gaphor/commits?author=amolenaar" title="Documentation">📖</a> <a href="https://github.com/gaphor/gaphor/pulls?q=is%3Apr+reviewed-by%3Aamolenaar" title="Reviewed Pull Requests">👀</a> <a href="#question-amolenaar" title="Answering Questions">💬</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Aamolenaar" title="Bug reports">🐛</a> <a href="#plugin-amolenaar" title="Plugin/utility libraries">🔌</a> <a href="https://github.com/gaphor/gaphor/commits?author=amolenaar" title="Tests">⚠️</a></td>\n    <td align="center"><a href="https://github.com/Lutra-Fs"><img src="https://avatars.githubusercontent.com/u/36790218?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bill ZHANG</b></sub></a><br /><a href="#translation-Lutra-Fs" title="Translation">🌍</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/blippost"><img src="https://avatars.githubusercontent.com/u/74373678?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Blippost</b></sub></a><br /><a href="#ideas-Blippost" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="http://btibert3.github.io"><img src="https://avatars2.githubusercontent.com/u/203343?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Brock Tibert</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3ABtibert3" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/choff"><img src="https://avatars1.githubusercontent.com/u/309979?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christian Hoff</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=choff" title="Code">💻</a></td>\n    <td align="center"><a href="https://ghuser.io/danyeaw"><img src="https://avatars1.githubusercontent.com/u/10014976?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dan Yeaw</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=danyeaw" title="Code">💻</a> <a href="https://github.com/gaphor/gaphor/commits?author=danyeaw" title="Tests">⚠️</a> <a href="https://github.com/gaphor/gaphor/commits?author=danyeaw" title="Documentation">📖</a> <a href="#platform-danyeaw" title="Packaging/porting to new platform">📦</a> <a href="#infra-danyeaw" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Adanyeaw" title="Bug reports">🐛</a> <a href="#question-danyeaw" title="Answering Questions">💬</a></td>\n    <td align="center"><a href="http://www.DanielNylander.se"><img src="https://avatars.githubusercontent.com/u/1206564?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Daniel Nylander</b></sub></a><br /><a href="#translation-yeager" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/DimShadoWWW"><img src="https://avatars2.githubusercontent.com/u/25516?v=4?s=100" width="100px;" alt=""/><br /><sub><b>DimShadoWWW</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3ADimShadoWWW" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/Texopolis"><img src="https://avatars.githubusercontent.com/u/88953534?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Douglas B</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=Texopolis" title="Documentation">📖</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="http://encolpe.wordpress.com"><img src="https://avatars1.githubusercontent.com/u/124361?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Encolpe DEGOUTE</b></sub></a><br /><a href="#translation-encolpe" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/egroeper"><img src="https://avatars3.githubusercontent.com/u/535113?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Enno Gröper</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=egroeper" title="Code">💻</a></td>\n    <td align="center"><a href="https://github.com/ezickler"><img src="https://avatars3.githubusercontent.com/u/3604310?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Enno Zickler</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Aezickler" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://bousse-e.univ-nantes.io"><img src="https://avatars.githubusercontent.com/u/5868014?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Erwan Bousse</b></sub></a><br /><a href="#ideas-ebousse" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="http://www.frandieguez.dev"><img src="https://avatars.githubusercontent.com/u/4584?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Fran Diéguez</b></sub></a><br /><a href="#translation-frandieguez" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/gbrlgian"><img src="https://avatars.githubusercontent.com/u/47647695?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Gabriel Gian</b></sub></a><br /><a href="#translation-gbrlgian" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/liferooter"><img src="https://avatars.githubusercontent.com/u/54807745?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Gleb Smirnov</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Aliferooter" title="Bug reports">🐛</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="http://gjstewart.net"><img src="https://avatars.githubusercontent.com/u/7083701?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Greg Stewart</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3AGregJohnStewart" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/Gytree"><img src="https://avatars.githubusercontent.com/u/28499079?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Gytree</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3AGytree" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="http://www.gunibert.de"><img src="https://avatars.githubusercontent.com/u/373597?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Günther Wagner</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Agwutz" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://www.hamishmb.com"><img src="https://avatars.githubusercontent.com/u/16725441?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hamish Mcintyre-Bhatty</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Ahamishmb" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://bandism.net/"><img src="https://avatars.githubusercontent.com/u/22633385?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ikko Ashimine</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=eltociear" title="Code">💻</a></td>\n    <td align="center"><a href="https://github.com/jischebeck"><img src="https://avatars0.githubusercontent.com/u/3011242?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jan</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Ajischebeck" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://pfeifle.tech"><img src="https://avatars2.githubusercontent.com/u/23027708?v=4?s=100" width="100px;" alt=""/><br /><sub><b>JensPfeifle</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=JensPfeifle" title="Documentation">📖</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/vanillajonathan"><img src="https://avatars.githubusercontent.com/u/10222521?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jonathan</b></sub></a><br /><a href="#ideas-vanillajonathan" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Avanillajonathan" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://twitter.com/yonkeltron"><img src="https://avatars.githubusercontent.com/u/59451?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jonathan E. Magen</b></sub></a><br /><a href="#ideas-yonkeltron" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="https://jonnathanriquelmo.github.io/"><img src="https://avatars.githubusercontent.com/u/13298966?v=4?s=100" width="100px;" alt=""/><br /><sub><b>JonnathanRiquelmo</b></sub></a><br /><a href="#translation-JonnathanRiquelmo" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://oskuro.net/"><img src="https://avatars3.githubusercontent.com/u/929712?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jordi Mallach</b></sub></a><br /><a href="#translation-jmallach" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/dlagg"><img src="https://avatars3.githubusercontent.com/u/44321931?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jorge DLG</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Adlagg" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/h8672"><img src="https://avatars.githubusercontent.com/u/8805540?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Juha-Matti Kokkonen</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Ah8672" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="http://twitter.com/kapilvt"><img src="https://avatars3.githubusercontent.com/u/21650?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kapil Thangavelu</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Akapilt" title="Bug reports">🐛</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/KhazAkar"><img src="https://avatars.githubusercontent.com/u/12693890?v=4?s=100" width="100px;" alt=""/><br /><sub><b>KhazAkar</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3AKhazAkar" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/LordSinSentido"><img src="https://avatars.githubusercontent.com/u/57022857?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lordy</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3ALordSinSentido" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="http://monkington.github.io"><img src="https://avatars.githubusercontent.com/u/778856?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mark Kennedy</b></sub></a><br /><a href="#ideas-mrmonkington" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/gaphor/gaphor/commits?author=mrmonkington" title="Code">💻</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Amrmonkington" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/markdluethje"><img src="https://avatars.githubusercontent.com/u/31922494?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mark-Daniel Lüthje</b></sub></a><br /><a href="#translation-markdluethje" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/mathiascode"><img src="https://avatars.githubusercontent.com/u/8754153?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mat</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=mathiascode" title="Code">💻</a></td>\n    <td align="center"><a href="https://github.com/kainne44"><img src="https://avatars.githubusercontent.com/u/50899654?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matthew Maclaine</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Akainne44" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/Mek101"><img src="https://avatars.githubusercontent.com/u/34246799?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mek101</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3AMek101" title="Bug reports">🐛</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/c4tachan"><img src="https://avatars.githubusercontent.com/u/2130211?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michael Patrick Tkacik</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Ac4tachan" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/mbessonov"><img src="https://avatars2.githubusercontent.com/u/172974?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mikhail Bessonov</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Ambessonov" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="http://nedko.arnaudov.name"><img src="https://avatars2.githubusercontent.com/u/96399?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nedko Arnaudov</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Anedko" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/philwilkinson40"><img src="https://avatars.githubusercontent.com/u/27684871?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Phil_Smurf</b></sub></a><br /><a href="#ideas-philwilkinson40" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="http://www.rmunoz.net"><img src="https://avatars2.githubusercontent.com/u/23944?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rafael Muñoz Cárdenas</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3AMenda" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/ruimaciel"><img src="https://avatars3.githubusercontent.com/u/169121?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rui Maciel</b></sub></a><br /><a href="#ideas-ruimaciel" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="https://github.com/darkcircle"><img src="https://avatars.githubusercontent.com/u/1160498?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Seong-ho Cho</b></sub></a><br /><a href="#translation-darkcircle" title="Translation">🌍</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/artscoop"><img src="https://avatars.githubusercontent.com/u/1023091?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Steve Kossouho</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Aartscoop" title="Bug reports">🐛</a> <a href="https://github.com/gaphor/gaphor/commits?author=artscoop" title="Code">💻</a></td>\n    <td align="center"><a href="http://stevenliu216.github.io"><img src="https://avatars3.githubusercontent.com/u/1274417?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Steven Liu</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Astevenliu216" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/TiemenSch"><img src="https://avatars.githubusercontent.com/u/7141863?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tiemen Schuijbroek</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3ATiemenSch" title="Bug reports">🐛</a> <a href="https://github.com/gaphor/gaphor/commits?author=TiemenSch" title="Code">💻</a></td>\n    <td align="center"><a href="http://tobiasbernard.com"><img src="https://avatars3.githubusercontent.com/u/1908896?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tobias Bernard</b></sub></a><br /><a href="#design-bertob" title="Design">🎨</a> <a href="#ideas-bertob" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="https://github.com/TomBous"><img src="https://avatars.githubusercontent.com/u/10131977?v=4?s=100" width="100px;" alt=""/><br /><sub><b>TomBous</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3ATomBous" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/tomaszdrozdz"><img src="https://avatars.githubusercontent.com/u/14263613?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tomasz Drożdż</b></sub></a><br /><a href="#ideas-tomaszdrozdz" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="https://github.com/tonytheleg"><img src="https://avatars3.githubusercontent.com/u/43508092?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tony</b></sub></a><br /><a href="#maintenance-tonytheleg" title="Maintenance">🚧</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/Viicos"><img src="https://avatars.githubusercontent.com/u/65306057?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Viicos</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3AViicos" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/Xander982"><img src="https://avatars2.githubusercontent.com/u/51178927?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Xander982</b></sub></a><br /><a href="#content-Xander982" title="Content">🖋</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3AXander982" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/yantaozhao"><img src="https://avatars.githubusercontent.com/u/9587405?v=4?s=100" width="100px;" alt=""/><br /><sub><b>YantaoZhao</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Ayantaozhao" title="Bug reports">🐛</a> <a href="#ideas-yantaozhao" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="https://github.com/actionless"><img src="https://avatars1.githubusercontent.com/u/1655669?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Yauhen Kirylau</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=actionless" title="Documentation">📖</a> <a href="#platform-actionless" title="Packaging/porting to new platform">📦</a> <a href="#ideas-actionless" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Aactionless" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/sz332"><img src="https://avatars.githubusercontent.com/u/8182138?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Zsolt Sandor</b></sub></a><br /><a href="#ideas-sz332" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Asz332" title="Bug reports">🐛</a> <a href="https://github.com/gaphor/gaphor/commits?author=sz332" title="Code">💻</a> <a href="https://github.com/gaphor/gaphor/commits?author=sz332" title="Documentation">📖</a></td>\n    <td align="center"><a href="http://www.zorinos.com"><img src="https://avatars1.githubusercontent.com/u/34811668?v=4?s=100" width="100px;" alt=""/><br /><sub><b>albanobattistella</b></sub></a><br /><a href="#translation-albanobattistella" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://github.com/deifemu"><img src="https://avatars.githubusercontent.com/u/81991548?v=4?s=100" width="100px;" alt=""/><br /><sub><b>deifemu</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Adeifemu" title="Bug reports">🐛</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/freddii"><img src="https://avatars0.githubusercontent.com/u/7213207?v=4?s=100" width="100px;" alt=""/><br /><sub><b>freddii</b></sub></a><br /><a href="#ideas-freddii" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/gaphor/gaphor/commits?author=freddii" title="Documentation">📖</a></td>\n    <td align="center"><a href="https://github.com/freezed-or-frozen"><img src="https://avatars.githubusercontent.com/u/28558919?v=4?s=100" width="100px;" alt=""/><br /><sub><b>freezed-or-frozen</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Afreezed-or-frozen" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/fu7mu4"><img src="https://avatars.githubusercontent.com/u/1885537?v=4?s=100" width="100px;" alt=""/><br /><sub><b>fu7mu4</b></sub></a><br /><a href="#translation-fu7mu4" title="Translation">🌍</a></td>\n    <td align="center"><a href="https://gavr123456789.gitlab.io/hugo-test/"><img src="https://avatars3.githubusercontent.com/u/30507409?v=4?s=100" width="100px;" alt=""/><br /><sub><b>gavr123456789</b></sub></a><br /><a href="#ideas-gavr123456789" title="Ideas, Planning, & Feedback">🤔</a></td>\n    <td align="center"><a href="https://github.com/greedyj4ck"><img src="https://avatars.githubusercontent.com/u/33233389?v=4?s=100" width="100px;" alt=""/><br /><sub><b>greedyj4ck</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Agreedyj4ck" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/kellenmoura"><img src="https://avatars0.githubusercontent.com/u/69016459?v=4?s=100" width="100px;" alt=""/><br /><sub><b>kellenmoura</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Akellenmoura" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/lukman83"><img src="https://avatars.githubusercontent.com/u/69509634?v=4?s=100" width="100px;" alt=""/><br /><sub><b>lukman83</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Alukman83" title="Bug reports">🐛</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/melisdogan"><img src="https://avatars2.githubusercontent.com/u/33630433?v=4?s=100" width="100px;" alt=""/><br /><sub><b>melisdogan</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=melisdogan" title="Documentation">📖</a></td>\n    <td align="center"><a href="https://github.com/milotype"><img src="https://avatars.githubusercontent.com/u/43657314?v=4?s=100" width="100px;" alt=""/><br /><sub><b>milotype</b></sub></a><br /><a href="#translation-milotype" title="Translation">🌍</a> <a href="https://github.com/gaphor/gaphor/commits?author=milotype" title="Documentation">📖</a></td>\n    <td align="center"><a href="https://github.com/mskorkowski"><img src="https://avatars.githubusercontent.com/u/90662755?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mskorkowski</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Amskorkowski" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/ovari"><img src="https://avatars.githubusercontent.com/u/17465872?v=4?s=100" width="100px;" alt=""/><br /><sub><b>ovari</b></sub></a><br /><a href="#ideas-ovari" title="Ideas, Planning, & Feedback">🤔</a> <a href="#translation-ovari" title="Translation">🌍</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Aovari" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/samirodj"><img src="https://avatars.githubusercontent.com/u/36422980?v=4?s=100" width="100px;" alt=""/><br /><sub><b>samirodj</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Asamirodj" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/seryafarma"><img src="https://avatars0.githubusercontent.com/u/3274071?v=4?s=100" width="100px;" alt=""/><br /><sub><b>seryafarma</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=seryafarma" title="Documentation">📖</a></td>\n    <td align="center"><a href="https://github.com/icfmp"><img src="https://avatars.githubusercontent.com/u/71736258?v=4?s=100" width="100px;" alt=""/><br /><sub><b>sib@c</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Aicfmp" title="Bug reports">🐛</a> <a href="#ideas-icfmp" title="Ideas, Planning, & Feedback">🤔</a></td>\n  </tr>\n  <tr>\n    <td align="center"><a href="https://github.com/tronta"><img src="https://avatars1.githubusercontent.com/u/5135577?v=4?s=100" width="100px;" alt=""/><br /><sub><b>tronta</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/issues?q=author%3Atronta" title="Bug reports">🐛</a></td>\n    <td align="center"><a href="https://github.com/wrobell"><img src="https://avatars2.githubusercontent.com/u/105664?v=4?s=100" width="100px;" alt=""/><br /><sub><b>wrobell</b></sub></a><br /><a href="https://github.com/gaphor/gaphor/commits?author=wrobell" title="Code">💻</a> <a href="https://github.com/gaphor/gaphor/commits?author=wrobell" title="Tests">⚠️</a> <a href="https://github.com/gaphor/gaphor/issues?q=author%3Awrobell" title="Bug reports">🐛</a> <a href="#design-wrobell" title="Design">🎨</a></td>\n    <td align="center"><a href="https://github.com/oscfdezdz"><img src="https://avatars.githubusercontent.com/u/42654671?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Óscar Fernández Díaz</b></sub></a><br /><a href="#translation-oscfdezdz" title="Translation">🌍</a> <a href="https://github.com/gaphor/gaphor/commits?author=oscfdezdz" title="Code">💻</a></td>\n    <td align="center"><a href="https://github.com/zlv"><img src="https://avatars.githubusercontent.com/u/602210?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Евгений Лежнин</b></sub></a><br /><a href="#translation-zlv" title="Translation">🌍</a></td>\n  </tr>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the\n[all-contributors](https://github.com/kentcdodds/all-contributors)\nspecification. Contributions of any kind are welcome!\n\n1.  Check for open issues or open a fresh issue to start a discussion\n    around a feature idea or a bug. There is a\n    [first-timers-only](https://github.com/gaphor/gaphor/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Afirst-timers-only)\n    tag for issues that should be ideal for people who are not very\n    familiar with the codebase yet.\n2.  Fork [the repository](https://github.com/gaphor/gaphor) on\n    GitHub to start making your changes to the **master** branch (or\n    branch off of it).\n3.  Write a test which shows that the bug was fixed or that the feature\n    works as expected.\n4.  Send a pull request and bug the maintainers until it gets merged and\n    published. :smile:\n\nSee [the contributing file](CONTRIBUTING.md)!\n\n### Translations\n\nTranslation of Gaphor is mostly done using [Weblate](https://hosted.weblate.org/projects/gaphor/gaphor/).\n\nFor the Linux Flatpak, the desktop entry comment string can be translated at our [Flatpak repository](https://github.com/flathub/org.gaphor.Gaphor/blob/master/share/org.gaphor.Gaphor.desktop).\n\nThank you so much for your effort in helping us keep it available in many languages!\n\n## © License\n\nCopyright © Arjan Molenaar and Dan Yeaw\n\nLicensed under the [Apache License v2](LICENSE.txt).\n\nSummary: You can do what you like with Gaphor, as long as you include the\nrequired notices. This permissive license contains a patent license from the\ncontributors of the code.\n',
     'author': 'Arjan J. Molenaar',
     'author_email': 'gaphor@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://gaphor.org/',
```

### Comparing `gaphor-2.9.1/PKG-INFO` & `gaphor-2.9.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gaphor
-Version: 2.9.1
+Version: 2.9.2
 Summary: Gaphor is the simple modeling tool written in Python.
 Home-page: https://gaphor.org/
 Keywords: gtk+,diagram,UML,MBSE,gaphor,modeling
 Author: Arjan J. Molenaar
 Author-email: gaphor@gmail.com
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 5 - Production/Stable
```

