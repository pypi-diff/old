# Comparing `tmp/naludaq-0.17.0.tar.gz` & `tmp/naludaq-0.17.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "naludaq-0.17.0.tar", last modified: Thu Apr  6 21:26:43 2023, max compression
+gzip compressed data, was "naludaq-0.17.1.tar", last modified: Fri Apr  7 07:19:02 2023, max compression
```

## Comparing `naludaq-0.17.0.tar` & `naludaq-0.17.1.tar`

### file list

```diff
@@ -1,245 +1,245 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.328112 naludaq-0.17.0/
--rw-r--r--   0 runner    (1001) docker     (123)     7652 2023-04-06 21:26:23.000000 naludaq-0.17.0/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)    15635 2023-04-06 21:26:43.328112 naludaq-0.17.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    14785 2023-04-06 21:26:23.000000 naludaq-0.17.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-04-06 21:26:23.000000 naludaq-0.17.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 21:26:43.328112 naludaq-0.17.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-04-06 21:26:23.000000 naludaq-0.17.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.260112 naludaq-0.17.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.272112 naludaq-0.17.0/src/naludaq/
--rw-r--r--   0 runner    (1001) docker     (123)      251 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.276112 naludaq-0.17.0/src/naludaq/backend/
--rw-r--r--   0 runner    (1001) docker     (123)      401 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4484 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/client.py
--rw-r--r--   0 runner    (1001) docker     (123)     1413 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/context.py
--rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.276112 naludaq-0.17.0/src/naludaq/backend/managers/
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/managers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4403 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/managers/acquisitions.py
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/managers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1160 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/managers/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     8082 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/managers/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)     1999 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/managers/io.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.276112 naludaq-0.17.0/src/naludaq/backend/models/
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    30392 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/models/acquisition.py
--rw-r--r--   0 runner    (1001) docker     (123)     7066 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/backend/models/device.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.276112 naludaq-0.17.0/src/naludaq/board/
--rw-r--r--   0 runner    (1001) docker     (123)    28790 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    23941 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/board_inits.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.280112 naludaq-0.17.0/src/naludaq/board/connections/
--rw-r--r--   0 runner    (1001) docker     (123)    18932 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/_FTDI.py
--rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/_MockUART.py
--rw-r--r--   0 runner    (1001) docker     (123)    14633 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/_UART.py
--rw-r--r--   0 runner    (1001) docker     (123)    10093 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/_USB.py
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      943 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/base_connection.py
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/base_ethernet.py
--rw-r--r--   0 runner    (1001) docker     (123)      319 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/base_serial.py
--rw-r--r--   0 runner    (1001) docker     (123)     5372 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/connection_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     4928 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/tcp.py
--rw-r--r--   0 runner    (1001) docker     (123)     8486 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/connections/udp.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.284112 naludaq-0.17.0/src/naludaq/board/initializers/
--rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/aardvarcv3.py
--rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/aodsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4250 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/init_aodsv2_eval.py
--rw-r--r--   0 runner    (1001) docker     (123)     4277 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/init_hdsocv1.py
--rw-r--r--   0 runner    (1001) docker     (123)     4680 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/init_udc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6241 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/init_upac96.py
--rw-r--r--   0 runner    (1001) docker     (123)     1111 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/initializers/trbhm.py
--rw-r--r--   0 runner    (1001) docker     (123)    17669 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/board/params.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.284112 naludaq-0.17.0/src/naludaq/communication/
--rw-r--r--   0 runner    (1001) docker     (123)     2323 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/communication/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3774 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/communication/analog_registers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/communication/control_registers.py
--rw-r--r--   0 runner    (1001) docker     (123)     3262 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/communication/digital_registers.py
--rw-r--r--   0 runner    (1001) docker     (123)     6110 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/communication/i2c.py
--rw-r--r--   0 runner    (1001) docker     (123)     1614 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/communication/i2c_registers.py
--rw-r--r--   0 runner    (1001) docker     (123)    28991 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/communication/registers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.288112 naludaq-0.17.0/src/naludaq/controllers/
--rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1875 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/analog_debug_controller.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.288112 naludaq-0.17.0/src/naludaq/controllers/biasing_mode/
--rw-r--r--   0 runner    (1001) docker     (123)     1235 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/biasing_mode/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/biasing_mode/udc16.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.288112 naludaq-0.17.0/src/naludaq/controllers/board/
--rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2146 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/aodsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)    15185 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/default.py
--rw-r--r--   0 runner    (1001) docker     (123)     7392 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/hdsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2205 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/oleas.py
--rw-r--r--   0 runner    (1001) docker     (123)     3541 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/trbhm.py
--rw-r--r--   0 runner    (1001) docker     (123)     6484 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/udc.py
--rw-r--r--   0 runner    (1001) docker     (123)    10214 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/upac.py
--rw-r--r--   0 runner    (1001) docker     (123)     9258 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/board/upac96.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.292112 naludaq-0.17.0/src/naludaq/controllers/connection/
--rw-r--r--   0 runner    (1001) docker     (123)      936 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/connection/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21072 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/connection/connection_controller.py
--rw-r--r--   0 runner    (1001) docker     (123)     3027 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/connection/upac.py
--rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/connection/upac96.py
--rw-r--r--   0 runner    (1001) docker     (123)      307 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/controller.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.292112 naludaq-0.17.0/src/naludaq/controllers/external_dac/
--rw-r--r--   0 runner    (1001) docker     (123)     2284 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/ad5671.py
--rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/ad5675.py
--rw-r--r--   0 runner    (1001) docker     (123)    11125 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4211 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/dac7578.py
--rw-r--r--   0 runner    (1001) docker     (123)     4687 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/hdsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4585 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/i2c_dac.py
--rw-r--r--   0 runner    (1001) docker     (123)     6141 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/trbhm.py
--rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/external_dac/upac32.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.296112 naludaq-0.17.0/src/naludaq/controllers/gainstages/
--rw-r--r--   0 runner    (1001) docker     (123)      569 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/gainstages/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8224 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/gainstages/aodsv2.py
--rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/gainstages/oddsock_aods.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.296112 naludaq-0.17.0/src/naludaq/controllers/peripherals/
--rw-r--r--   0 runner    (1001) docker     (123)     1087 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/peripherals/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3940 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/peripherals/aodsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     5123 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/peripherals/hdsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6985 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/peripherals/peripherals_controller.py
--rw-r--r--   0 runner    (1001) docker     (123)     5842 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/peripherals/upac.py
--rw-r--r--   0 runner    (1001) docker     (123)    16209 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/project_controller.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.296112 naludaq-0.17.0/src/naludaq/controllers/readout/
--rw-r--r--   0 runner    (1001) docker     (123)      954 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/readout/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/readout/aardvarcv3.py
--rw-r--r--   0 runner    (1001) docker     (123)    11462 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/readout/default.py
--rw-r--r--   0 runner    (1001) docker     (123)     4172 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/readout/hdsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1515 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/readout/trbhm.py
--rw-r--r--   0 runner    (1001) docker     (123)     4579 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/si5341_controller.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.296112 naludaq-0.17.0/src/naludaq/controllers/tia/
--rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/tia/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/tia/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    11997 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/tia/hdsoc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.300112 naludaq-0.17.0/src/naludaq/controllers/trigger/
--rw-r--r--   0 runner    (1001) docker     (123)     1133 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/aodsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     7455 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/default.py
--rw-r--r--   0 runner    (1001) docker     (123)     8881 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/hdsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)      214 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/siread.py
--rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/trbhm.py
--rw-r--r--   0 runner    (1001) docker     (123)     3627 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/upac.py
--rw-r--r--   0 runner    (1001) docker     (123)    16384 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/controllers/trigger/upac96.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.300112 naludaq-0.17.0/src/naludaq/daq/
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7254 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/debugdaq.py
--rw-r--r--   0 runner    (1001) docker     (123)    20482 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/lightdaq.py
--rw-r--r--   0 runner    (1001) docker     (123)     5086 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/preprocess.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.304112 naludaq-0.17.0/src/naludaq/daq/workers/
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2149 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/answer_parser_worker.py
--rw-r--r--   0 runner    (1001) docker     (123)    10475 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/csv_storage_worker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.304112 naludaq-0.17.0/src/naludaq/daq/workers/packager/
--rw-r--r--   0 runner    (1001) docker     (123)      612 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/packager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12720 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/packager/worker_packager.py
--rw-r--r--   0 runner    (1001) docker     (123)     2403 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/packager/worker_packager_debug.py
--rw-r--r--   0 runner    (1001) docker     (123)    10754 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/packager/worker_packager_hdsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     7986 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/postprocessing.py
--rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/worker_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     3918 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/worker_serial_reader.py
--rw-r--r--   0 runner    (1001) docker     (123)     2281 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/daq/workers/worker_usb_reader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.304112 naludaq-0.17.0/src/naludaq/devices/
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/devices/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       72 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/devices/device.py
--rw-r--r--   0 runner    (1001) docker     (123)     9913 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/devices/eeprom.py
--rw-r--r--   0 runner    (1001) docker     (123)    12292 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/devices/i2c_device.py
--rw-r--r--   0 runner    (1001) docker     (123)     8695 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/devices/ltc2990.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.308112 naludaq-0.17.0/src/naludaq/helpers/
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/helpers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      828 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/helpers/decorators.py
--rw-r--r--   0 runner    (1001) docker     (123)     3654 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/helpers/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6681 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/helpers/helper_functions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6125 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/helpers/register_cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     3952 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/helpers/semiton.py
--rw-r--r--   0 runner    (1001) docker     (123)      461 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/helpers/validations.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.308112 naludaq-0.17.0/src/naludaq/io/
--rw-r--r--   0 runner    (1001) docker     (123)     4227 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22403 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/io/csv_writer.py
--rw-r--r--   0 runner    (1001) docker     (123)    35939 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/io/hdf5.py
--rw-r--r--   0 runner    (1001) docker     (123)    12900 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/io/io_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.308112 naludaq-0.17.0/src/naludaq/models/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10980 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/models/acq_converters.py
--rw-r--r--   0 runner    (1001) docker     (123)     9728 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/models/acquisition.py
--rw-r--r--   0 runner    (1001) docker     (123)    15839 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/naludaq.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.312112 naludaq-0.17.0/src/naludaq/parsers/
--rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10831 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/aardvarcv3_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1544 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/answer_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     5722 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/aodsoc_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     4555 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/asocv3_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     8271 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/hdsoc_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.316112 naludaq-0.17.0/src/naludaq/parsers/headers/
--rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/headers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      636 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/headers/asoc.py
--rw-r--r--   0 runner    (1001) docker     (123)      932 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/headers/asocv2.py
--rw-r--r--   0 runner    (1001) docker     (123)      832 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/headers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/headers/siread.py
--rw-r--r--   0 runner    (1001) docker     (123)     1206 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/headers/trbhm.py
--rw-r--r--   0 runner    (1001) docker     (123)      650 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/headers/upac32.py
--rw-r--r--   0 runner    (1001) docker     (123)    11956 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     8877 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/trbhm_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     5569 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/udc_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     9347 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/upac96_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     4675 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/parsers/upac_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.316112 naludaq-0.17.0/src/naludaq/tools/
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.320112 naludaq-0.17.0/src/naludaq/tools/adc2mv/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/adc2mv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4732 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/adc2mv/adc_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)    16214 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/adc2mv/adc_linear_regression.py
--rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/adc2mv/generate.py
--rw-r--r--   0 runner    (1001) docker     (123)     2911 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/adc2mv/pre_adc2mv.py
--rw-r--r--   0 runner    (1001) docker     (123)     7642 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/autoaction.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.320112 naludaq-0.17.0/src/naludaq/tools/autotrigger/
--rw-r--r--   0 runner    (1001) docker     (123)      389 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/autotrigger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6790 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/autotrigger/default.py
--rw-r--r--   0 runner    (1001) docker     (123)     1683 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/board_backup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.320112 naludaq-0.17.0/src/naludaq/tools/dac_sweep/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/dac_sweep/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6871 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/dac_sweep/dac_sweep_controller.py
--rw-r--r--   0 runner    (1001) docker     (123)    11823 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/data_collector.py
--rw-r--r--   0 runner    (1001) docker     (123)     4670 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/features.py
--rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/ft60x.py
--rw-r--r--   0 runner    (1001) docker     (123)     6445 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/ftdi.py
--rw-r--r--   0 runner    (1001) docker     (123)     4239 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/metadata.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.320112 naludaq-0.17.0/src/naludaq/tools/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/optimizers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4302 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/optimizers/bayesian_optimizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     8833 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/optimizers/gainstagetuner.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.324112 naludaq-0.17.0/src/naludaq/tools/pedestals/
--rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.324112 naludaq-0.17.0/src/naludaq/tools/pedestals/_new/
--rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/_new/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/_new/aav3.py
--rw-r--r--   0 runner    (1001) docker     (123)    25345 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/_new/default.py
--rw-r--r--   0 runner    (1001) docker     (123)     5483 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/_new/hdsoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3821 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/aardvarcv3_pedestals_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    10430 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/hdsoc_pedestals_controller.py
--rw-r--r--   0 runner    (1001) docker     (123)      873 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_acq.py
--rw-r--r--   0 runner    (1001) docker     (123)    34274 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_controller.py
--rw-r--r--   0 runner    (1001) docker     (123)     4774 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_correcter.py
--rw-r--r--   0 runner    (1001) docker     (123)     3985 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_processor.py
--rw-r--r--   0 runner    (1001) docker     (123)    10912 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/udc16_pedestals_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     7917 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/upac32_pedestals_controller.py
--rw-r--r--   0 runner    (1001) docker     (123)    12497 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/pedestals/upac96_pedestals_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.324112 naludaq-0.17.0/src/naludaq/tools/threshold_scan/
--rw-r--r--   0 runner    (1001) docker     (123)      806 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/threshold_scan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7101 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/threshold_scan/hdsoc_thresholdscan.py
--rw-r--r--   0 runner    (1001) docker     (123)     6829 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/threshold_scan/threshold_scan.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.324112 naludaq-0.17.0/src/naludaq/tools/timing_cal/
--rw-r--r--   0 runner    (1001) docker     (123)      828 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/timing_cal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10911 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/timing_cal/calibration.py
--rw-r--r--   0 runner    (1001) docker     (123)     2330 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/timing_cal/correcter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.328112 naludaq-0.17.0/src/naludaq/tools/waiter/
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/waiter/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2063 2023-04-06 21:26:23.000000 naludaq-0.17.0/src/naludaq/tools/waiter/eventwaiter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.272112 naludaq-0.17.0/src/naludaq.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    15635 2023-04-06 21:26:43.000000 naludaq-0.17.0/src/naludaq.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8064 2023-04-06 21:26:43.000000 naludaq-0.17.0/src/naludaq.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:26:43.000000 naludaq-0.17.0/src/naludaq.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-04-06 21:26:43.000000 naludaq-0.17.0/src/naludaq.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-06 21:26:43.000000 naludaq-0.17.0/src/naludaq.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:43.328112 naludaq-0.17.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-06 21:26:23.000000 naludaq-0.17.0/tests/test_naludaq.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.210160 naludaq-0.17.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     7652 2023-04-07 07:18:44.000000 naludaq-0.17.1/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    15635 2023-04-07 07:19:02.210160 naludaq-0.17.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    14785 2023-04-07 07:18:44.000000 naludaq-0.17.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-04-07 07:18:44.000000 naludaq-0.17.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 07:19:02.210160 naludaq-0.17.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-04-07 07:18:44.000000 naludaq-0.17.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.182160 naludaq-0.17.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.186159 naludaq-0.17.1/src/naludaq/
+-rw-r--r--   0 runner    (1001) docker     (123)      251 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.190160 naludaq-0.17.1/src/naludaq/backend/
+-rw-r--r--   0 runner    (1001) docker     (123)      401 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4484 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1413 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.190160 naludaq-0.17.1/src/naludaq/backend/managers/
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/managers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4403 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/managers/acquisitions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/managers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1160 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/managers/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8082 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/managers/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1999 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/managers/io.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.190160 naludaq-0.17.1/src/naludaq/backend/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30392 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/models/acquisition.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7066 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/backend/models/device.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.190160 naludaq-0.17.1/src/naludaq/board/
+-rw-r--r--   0 runner    (1001) docker     (123)    28790 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23941 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/board_inits.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.190160 naludaq-0.17.1/src/naludaq/board/connections/
+-rw-r--r--   0 runner    (1001) docker     (123)    18932 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/_FTDI.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/_MockUART.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14633 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/_UART.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10093 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/_USB.py
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      943 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/base_connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/base_ethernet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      319 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/base_serial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5372 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/connection_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4928 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/tcp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8486 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/connections/udp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.190160 naludaq-0.17.1/src/naludaq/board/initializers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/aardvarcv3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/aodsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4250 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/init_aodsv2_eval.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4277 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/init_hdsocv1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4680 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/init_udc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6241 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/init_upac96.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1111 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/initializers/trbhm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17669 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/board/params.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.194160 naludaq-0.17.1/src/naludaq/communication/
+-rw-r--r--   0 runner    (1001) docker     (123)     2323 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/communication/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3774 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/communication/analog_registers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/communication/control_registers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3262 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/communication/digital_registers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6110 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/communication/i2c.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1614 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/communication/i2c_registers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28991 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/communication/registers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.194160 naludaq-0.17.1/src/naludaq/controllers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1875 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/analog_debug_controller.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.194160 naludaq-0.17.1/src/naludaq/controllers/biasing_mode/
+-rw-r--r--   0 runner    (1001) docker     (123)     1235 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/biasing_mode/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/biasing_mode/udc16.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.194160 naludaq-0.17.1/src/naludaq/controllers/board/
+-rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2146 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/aodsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15185 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7392 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/hdsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2205 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/oleas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3541 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/trbhm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6484 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/udc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10214 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/upac.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9258 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/board/upac96.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.194160 naludaq-0.17.1/src/naludaq/controllers/connection/
+-rw-r--r--   0 runner    (1001) docker     (123)      936 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/connection/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21072 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/connection/connection_controller.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3027 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/connection/upac.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/connection/upac96.py
+-rw-r--r--   0 runner    (1001) docker     (123)      307 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/controller.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.198160 naludaq-0.17.1/src/naludaq/controllers/external_dac/
+-rw-r--r--   0 runner    (1001) docker     (123)     2284 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/ad5671.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/ad5675.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11125 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4211 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/dac7578.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4687 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/hdsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4585 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/i2c_dac.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6141 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/trbhm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/external_dac/upac32.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.198160 naludaq-0.17.1/src/naludaq/controllers/gainstages/
+-rw-r--r--   0 runner    (1001) docker     (123)      569 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/gainstages/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8224 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/gainstages/aodsv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/gainstages/oddsock_aods.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.198160 naludaq-0.17.1/src/naludaq/controllers/peripherals/
+-rw-r--r--   0 runner    (1001) docker     (123)     1087 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/peripherals/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3940 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/peripherals/aodsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5123 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/peripherals/hdsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6985 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/peripherals/peripherals_controller.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5842 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/peripherals/upac.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16209 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/project_controller.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.198160 naludaq-0.17.1/src/naludaq/controllers/readout/
+-rw-r--r--   0 runner    (1001) docker     (123)      954 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/readout/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/readout/aardvarcv3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11462 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/readout/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4172 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/readout/hdsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1515 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/readout/trbhm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4579 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/si5341_controller.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.198160 naludaq-0.17.1/src/naludaq/controllers/tia/
+-rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/tia/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/tia/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11997 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/tia/hdsoc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.198160 naludaq-0.17.1/src/naludaq/controllers/trigger/
+-rw-r--r--   0 runner    (1001) docker     (123)     1133 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/aodsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7455 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8881 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/hdsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      214 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/siread.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/trbhm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3627 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/upac.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16384 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/controllers/trigger/upac96.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.198160 naludaq-0.17.1/src/naludaq/daq/
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7254 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/debugdaq.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20482 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/lightdaq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5086 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/preprocess.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.202160 naludaq-0.17.1/src/naludaq/daq/workers/
+-rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2149 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/answer_parser_worker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10475 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/csv_storage_worker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.202160 naludaq-0.17.1/src/naludaq/daq/workers/packager/
+-rw-r--r--   0 runner    (1001) docker     (123)      612 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/packager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12720 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/packager/worker_packager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2403 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/packager/worker_packager_debug.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10754 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/packager/worker_packager_hdsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7986 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/postprocessing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/worker_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3918 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/worker_serial_reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2281 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/daq/workers/worker_usb_reader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.202160 naludaq-0.17.1/src/naludaq/devices/
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/devices/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       72 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/devices/device.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9913 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/devices/eeprom.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12292 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/devices/i2c_device.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8695 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/devices/ltc2990.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.202160 naludaq-0.17.1/src/naludaq/helpers/
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/helpers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      828 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/helpers/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3654 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/helpers/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6681 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/helpers/helper_functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6125 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/helpers/register_cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3952 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/helpers/semiton.py
+-rw-r--r--   0 runner    (1001) docker     (123)      461 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/helpers/validations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.202160 naludaq-0.17.1/src/naludaq/io/
+-rw-r--r--   0 runner    (1001) docker     (123)     4227 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22403 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/io/csv_writer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35939 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/io/hdf5.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12900 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/io/io_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.202160 naludaq-0.17.1/src/naludaq/models/
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10980 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/models/acq_converters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9728 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/models/acquisition.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15839 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/naludaq.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.206160 naludaq-0.17.1/src/naludaq/parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10831 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/aardvarcv3_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1544 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/answer_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5722 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/aodsoc_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4555 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/asocv3_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8271 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/hdsoc_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.206160 naludaq-0.17.1/src/naludaq/parsers/headers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/headers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      636 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/headers/asoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      932 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/headers/asocv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      832 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/headers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/headers/siread.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1206 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/headers/trbhm.py
+-rw-r--r--   0 runner    (1001) docker     (123)      650 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/headers/upac32.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11956 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8877 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/trbhm_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5569 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/udc_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9347 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/upac96_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4675 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/parsers/upac_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.206160 naludaq-0.17.1/src/naludaq/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.206160 naludaq-0.17.1/src/naludaq/tools/adc2mv/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/adc2mv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4732 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/adc2mv/adc_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16214 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/adc2mv/adc_linear_regression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/adc2mv/generate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2911 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/adc2mv/pre_adc2mv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7642 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/autoaction.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.206160 naludaq-0.17.1/src/naludaq/tools/autotrigger/
+-rw-r--r--   0 runner    (1001) docker     (123)      389 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/autotrigger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6790 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/autotrigger/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1683 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/board_backup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.206160 naludaq-0.17.1/src/naludaq/tools/dac_sweep/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/dac_sweep/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6871 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/dac_sweep/dac_sweep_controller.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11823 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/data_collector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4670 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/features.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/ft60x.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6445 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/ftdi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4239 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/metadata.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.206160 naludaq-0.17.1/src/naludaq/tools/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/optimizers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4302 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/optimizers/bayesian_optimizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8833 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/optimizers/gainstagetuner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.210160 naludaq-0.17.1/src/naludaq/tools/pedestals/
+-rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.210160 naludaq-0.17.1/src/naludaq/tools/pedestals/_new/
+-rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/_new/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/_new/aav3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25345 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/_new/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5483 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/_new/hdsoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3821 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/aardvarcv3_pedestals_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10430 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/hdsoc_pedestals_controller.py
+-rw-r--r--   0 runner    (1001) docker     (123)      873 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_acq.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34274 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_controller.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4774 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_correcter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4132 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_processor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10912 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/udc16_pedestals_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7917 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/upac32_pedestals_controller.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12497 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/pedestals/upac96_pedestals_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.210160 naludaq-0.17.1/src/naludaq/tools/threshold_scan/
+-rw-r--r--   0 runner    (1001) docker     (123)      806 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/threshold_scan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7101 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/threshold_scan/hdsoc_thresholdscan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6829 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/threshold_scan/threshold_scan.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.210160 naludaq-0.17.1/src/naludaq/tools/timing_cal/
+-rw-r--r--   0 runner    (1001) docker     (123)      828 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/timing_cal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10911 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/timing_cal/calibration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2330 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/timing_cal/correcter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.210160 naludaq-0.17.1/src/naludaq/tools/waiter/
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/waiter/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2063 2023-04-07 07:18:44.000000 naludaq-0.17.1/src/naludaq/tools/waiter/eventwaiter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.186159 naludaq-0.17.1/src/naludaq.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    15635 2023-04-07 07:19:02.000000 naludaq-0.17.1/src/naludaq.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8064 2023-04-07 07:19:02.000000 naludaq-0.17.1/src/naludaq.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:19:02.000000 naludaq-0.17.1/src/naludaq.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-04-07 07:19:02.000000 naludaq-0.17.1/src/naludaq.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 07:19:02.000000 naludaq-0.17.1/src/naludaq.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:19:02.210160 naludaq-0.17.1/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-07 07:18:44.000000 naludaq-0.17.1/tests/test_naludaq.py
```

### Comparing `naludaq-0.17.0/LICENSE.txt` & `naludaq-0.17.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/PKG-INFO` & `naludaq-0.17.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: naludaq
-Version: 0.17.0
+Version: 0.17.1
 Summary: Backend package for Nalu Scientific hardware
 Home-page: 
 Author: Thomas Yang, Emily Lum, Terry Pham
 Author-email: Marcus Luck <marcus@naluscientific.com>, Mitchell Matsumori-Kelly <mitchell@naluscientific.com>, Alvin Yang <alvin@naluscientific.com>, Kenneth Lauritzen <kenneth@naluscientific.com>, Ben Rotter <ben@naluscientific.com>
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Programming Language :: Python :: 3
```

### Comparing `naludaq-0.17.0/README.md` & `naludaq-0.17.1/README.md`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/pyproject.toml` & `naludaq-0.17.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/setup.py` & `naludaq-0.17.1/setup.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/client.py` & `naludaq-0.17.1/src/naludaq/backend/client.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/context.py` & `naludaq-0.17.1/src/naludaq/backend/context.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/exceptions.py` & `naludaq-0.17.1/src/naludaq/backend/exceptions.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/managers/acquisitions.py` & `naludaq-0.17.1/src/naludaq/backend/managers/acquisitions.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/managers/config.py` & `naludaq-0.17.1/src/naludaq/backend/managers/config.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/managers/connection.py` & `naludaq-0.17.1/src/naludaq/backend/managers/connection.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/managers/io.py` & `naludaq-0.17.1/src/naludaq/backend/managers/io.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/models/acquisition.py` & `naludaq-0.17.1/src/naludaq/backend/models/acquisition.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/backend/models/device.py` & `naludaq-0.17.1/src/naludaq/backend/models/device.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/__init__.py` & `naludaq-0.17.1/src/naludaq/board/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/board_inits.py` & `naludaq-0.17.1/src/naludaq/board/board_inits.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/_FTDI.py` & `naludaq-0.17.1/src/naludaq/board/connections/_FTDI.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/_MockUART.py` & `naludaq-0.17.1/src/naludaq/board/connections/_MockUART.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/_UART.py` & `naludaq-0.17.1/src/naludaq/board/connections/_UART.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/_USB.py` & `naludaq-0.17.1/src/naludaq/board/connections/_USB.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/base_connection.py` & `naludaq-0.17.1/src/naludaq/board/connections/base_connection.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/connection_factory.py` & `naludaq-0.17.1/src/naludaq/board/connections/connection_factory.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/tcp.py` & `naludaq-0.17.1/src/naludaq/board/connections/tcp.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/connections/udp.py` & `naludaq-0.17.1/src/naludaq/board/connections/udp.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/__init__.py` & `naludaq-0.17.1/src/naludaq/board/initializers/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/aardvarcv3.py` & `naludaq-0.17.1/src/naludaq/board/initializers/aardvarcv3.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/aodsoc.py` & `naludaq-0.17.1/src/naludaq/board/initializers/aodsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/init_aodsv2_eval.py` & `naludaq-0.17.1/src/naludaq/board/initializers/init_aodsv2_eval.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/init_hdsocv1.py` & `naludaq-0.17.1/src/naludaq/board/initializers/init_hdsocv1.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/init_udc.py` & `naludaq-0.17.1/src/naludaq/board/initializers/init_udc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/init_upac96.py` & `naludaq-0.17.1/src/naludaq/board/initializers/init_upac96.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/initializers/trbhm.py` & `naludaq-0.17.1/src/naludaq/board/initializers/trbhm.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/board/params.py` & `naludaq-0.17.1/src/naludaq/board/params.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/communication/__init__.py` & `naludaq-0.17.1/src/naludaq/communication/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/communication/analog_registers.py` & `naludaq-0.17.1/src/naludaq/communication/analog_registers.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/communication/control_registers.py` & `naludaq-0.17.1/src/naludaq/communication/control_registers.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/communication/digital_registers.py` & `naludaq-0.17.1/src/naludaq/communication/digital_registers.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/communication/i2c.py` & `naludaq-0.17.1/src/naludaq/communication/i2c.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/communication/i2c_registers.py` & `naludaq-0.17.1/src/naludaq/communication/i2c_registers.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/communication/registers.py` & `naludaq-0.17.1/src/naludaq/communication/registers.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/analog_debug_controller.py` & `naludaq-0.17.1/src/naludaq/controllers/analog_debug_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/biasing_mode/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/biasing_mode/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/biasing_mode/udc16.py` & `naludaq-0.17.1/src/naludaq/controllers/biasing_mode/udc16.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/board/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/aodsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/board/aodsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/default.py` & `naludaq-0.17.1/src/naludaq/controllers/board/default.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/hdsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/board/hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/oleas.py` & `naludaq-0.17.1/src/naludaq/controllers/board/oleas.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/trbhm.py` & `naludaq-0.17.1/src/naludaq/controllers/board/trbhm.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/udc.py` & `naludaq-0.17.1/src/naludaq/controllers/board/udc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/upac.py` & `naludaq-0.17.1/src/naludaq/controllers/board/upac.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/board/upac96.py` & `naludaq-0.17.1/src/naludaq/controllers/board/upac96.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/connection/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/connection/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/connection/connection_controller.py` & `naludaq-0.17.1/src/naludaq/controllers/connection/connection_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/connection/upac.py` & `naludaq-0.17.1/src/naludaq/controllers/connection/upac.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/connection/upac96.py` & `naludaq-0.17.1/src/naludaq/controllers/connection/upac96.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/ad5671.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/ad5671.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/ad5675.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/ad5675.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/base.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/base.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/dac7578.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/dac7578.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/hdsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/i2c_dac.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/i2c_dac.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/trbhm.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/trbhm.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/external_dac/upac32.py` & `naludaq-0.17.1/src/naludaq/controllers/external_dac/upac32.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/gainstages/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/gainstages/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/gainstages/aodsv2.py` & `naludaq-0.17.1/src/naludaq/controllers/gainstages/aodsv2.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/gainstages/oddsock_aods.py` & `naludaq-0.17.1/src/naludaq/controllers/gainstages/oddsock_aods.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/peripherals/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/peripherals/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/peripherals/aodsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/peripherals/aodsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/peripherals/hdsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/peripherals/hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/peripherals/peripherals_controller.py` & `naludaq-0.17.1/src/naludaq/controllers/peripherals/peripherals_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/peripherals/upac.py` & `naludaq-0.17.1/src/naludaq/controllers/peripherals/upac.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/project_controller.py` & `naludaq-0.17.1/src/naludaq/controllers/project_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/readout/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/readout/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/readout/aardvarcv3.py` & `naludaq-0.17.1/src/naludaq/controllers/readout/aardvarcv3.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/readout/default.py` & `naludaq-0.17.1/src/naludaq/controllers/readout/default.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/readout/hdsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/readout/hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/readout/trbhm.py` & `naludaq-0.17.1/src/naludaq/controllers/readout/trbhm.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/si5341_controller.py` & `naludaq-0.17.1/src/naludaq/controllers/si5341_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/tia/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/tia/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/tia/base.py` & `naludaq-0.17.1/src/naludaq/controllers/tia/base.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/tia/hdsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/tia/hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/trigger/__init__.py` & `naludaq-0.17.1/src/naludaq/controllers/trigger/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/trigger/aodsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/trigger/aodsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/trigger/default.py` & `naludaq-0.17.1/src/naludaq/controllers/trigger/default.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/trigger/hdsoc.py` & `naludaq-0.17.1/src/naludaq/controllers/trigger/hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/trigger/trbhm.py` & `naludaq-0.17.1/src/naludaq/controllers/trigger/trbhm.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/trigger/upac.py` & `naludaq-0.17.1/src/naludaq/controllers/trigger/upac.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/controllers/trigger/upac96.py` & `naludaq-0.17.1/src/naludaq/controllers/trigger/upac96.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/__init__.py` & `naludaq-0.17.1/src/naludaq/daq/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/debugdaq.py` & `naludaq-0.17.1/src/naludaq/daq/debugdaq.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/lightdaq.py` & `naludaq-0.17.1/src/naludaq/daq/lightdaq.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/preprocess.py` & `naludaq-0.17.1/src/naludaq/daq/preprocess.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/__init__.py` & `naludaq-0.17.1/src/naludaq/daq/workers/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/answer_parser_worker.py` & `naludaq-0.17.1/src/naludaq/daq/workers/answer_parser_worker.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/csv_storage_worker.py` & `naludaq-0.17.1/src/naludaq/daq/workers/csv_storage_worker.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/packager/__init__.py` & `naludaq-0.17.1/src/naludaq/daq/workers/packager/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/packager/worker_packager.py` & `naludaq-0.17.1/src/naludaq/daq/workers/packager/worker_packager.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/packager/worker_packager_debug.py` & `naludaq-0.17.1/src/naludaq/daq/workers/packager/worker_packager_debug.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/packager/worker_packager_hdsoc.py` & `naludaq-0.17.1/src/naludaq/daq/workers/packager/worker_packager_hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/postprocessing.py` & `naludaq-0.17.1/src/naludaq/daq/workers/postprocessing.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/worker_parser.py` & `naludaq-0.17.1/src/naludaq/daq/workers/worker_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/worker_serial_reader.py` & `naludaq-0.17.1/src/naludaq/daq/workers/worker_serial_reader.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/daq/workers/worker_usb_reader.py` & `naludaq-0.17.1/src/naludaq/daq/workers/worker_usb_reader.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/devices/eeprom.py` & `naludaq-0.17.1/src/naludaq/devices/eeprom.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/devices/i2c_device.py` & `naludaq-0.17.1/src/naludaq/devices/i2c_device.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/devices/ltc2990.py` & `naludaq-0.17.1/src/naludaq/devices/ltc2990.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/helpers/decorators.py` & `naludaq-0.17.1/src/naludaq/helpers/decorators.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/helpers/exceptions.py` & `naludaq-0.17.1/src/naludaq/helpers/exceptions.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/helpers/helper_functions.py` & `naludaq-0.17.1/src/naludaq/helpers/helper_functions.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/helpers/register_cache.py` & `naludaq-0.17.1/src/naludaq/helpers/register_cache.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/helpers/semiton.py` & `naludaq-0.17.1/src/naludaq/helpers/semiton.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/io/__init__.py` & `naludaq-0.17.1/src/naludaq/io/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/io/csv_writer.py` & `naludaq-0.17.1/src/naludaq/io/csv_writer.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/io/hdf5.py` & `naludaq-0.17.1/src/naludaq/io/hdf5.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/io/io_manager.py` & `naludaq-0.17.1/src/naludaq/io/io_manager.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/models/acq_converters.py` & `naludaq-0.17.1/src/naludaq/models/acq_converters.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/models/acquisition.py` & `naludaq-0.17.1/src/naludaq/models/acquisition.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/naludaq.py` & `naludaq-0.17.1/src/naludaq/naludaq.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/__init__.py` & `naludaq-0.17.1/src/naludaq/parsers/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/aardvarcv3_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/aardvarcv3_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/answer_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/answer_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/aodsoc_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/aodsoc_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/asocv3_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/asocv3_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/hdsoc_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/hdsoc_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/headers/__init__.py` & `naludaq-0.17.1/src/naludaq/parsers/headers/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/headers/asoc.py` & `naludaq-0.17.1/src/naludaq/parsers/headers/asoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/headers/asocv2.py` & `naludaq-0.17.1/src/naludaq/parsers/headers/asocv2.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/headers/base.py` & `naludaq-0.17.1/src/naludaq/parsers/headers/base.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/headers/siread.py` & `naludaq-0.17.1/src/naludaq/parsers/headers/siread.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/headers/trbhm.py` & `naludaq-0.17.1/src/naludaq/parsers/headers/trbhm.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/headers/upac32.py` & `naludaq-0.17.1/src/naludaq/parsers/headers/upac32.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/parser.py` & `naludaq-0.17.1/src/naludaq/parsers/parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/trbhm_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/trbhm_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/udc_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/udc_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/upac96_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/upac96_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/parsers/upac_parser.py` & `naludaq-0.17.1/src/naludaq/parsers/upac_parser.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/adc2mv/adc_converter.py` & `naludaq-0.17.1/src/naludaq/tools/adc2mv/adc_converter.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/adc2mv/adc_linear_regression.py` & `naludaq-0.17.1/src/naludaq/tools/adc2mv/adc_linear_regression.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/adc2mv/generate.py` & `naludaq-0.17.1/src/naludaq/tools/adc2mv/generate.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/adc2mv/pre_adc2mv.py` & `naludaq-0.17.1/src/naludaq/tools/adc2mv/pre_adc2mv.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/autoaction.py` & `naludaq-0.17.1/src/naludaq/tools/autoaction.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/autotrigger/default.py` & `naludaq-0.17.1/src/naludaq/tools/autotrigger/default.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/board_backup.py` & `naludaq-0.17.1/src/naludaq/tools/board_backup.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/dac_sweep/dac_sweep_controller.py` & `naludaq-0.17.1/src/naludaq/tools/dac_sweep/dac_sweep_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/data_collector.py` & `naludaq-0.17.1/src/naludaq/tools/data_collector.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/features.py` & `naludaq-0.17.1/src/naludaq/tools/features.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/ft60x.py` & `naludaq-0.17.1/src/naludaq/tools/ft60x.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/ftdi.py` & `naludaq-0.17.1/src/naludaq/tools/ftdi.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/metadata.py` & `naludaq-0.17.1/src/naludaq/tools/metadata.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/optimizers/bayesian_optimizer.py` & `naludaq-0.17.1/src/naludaq/tools/optimizers/bayesian_optimizer.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/optimizers/gainstagetuner.py` & `naludaq-0.17.1/src/naludaq/tools/optimizers/gainstagetuner.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/__init__.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/_new/__init__.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/_new/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/_new/aav3.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/_new/aav3.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/_new/default.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/_new/default.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/_new/hdsoc.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/_new/hdsoc.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/aardvarcv3_pedestals_generator.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/aardvarcv3_pedestals_generator.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/hdsoc_pedestals_controller.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/hdsoc_pedestals_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_acq.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_acq.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_controller.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_correcter.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_correcter.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/pedestals_processor.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/pedestals_processor.py`

 * *Files 22% similar despite different names*

```diff
@@ -15,25 +15,28 @@
 
     Returns:
         ped (dict):
             Processed pedestal data with keys: "data" & "std_data" and
             "num_removed" if filter_outlier is enabled, with channels in
             the order of the channels argument.
     """
+    num_channels = pedestals["params"]["channels"]
     return_ped = {
-        "data": [],
-        "std_data": [],
+        "data": [[] for _ in range(num_channels)],
+        "std_data": [[] for _ in range(num_channels)],
     }
+
+    if channels is None:
+        channels = range(0, pedestals["params"]["channels"])
     if filter_outlier:
         return_ped["num_removed"] = {
-            "data": [],
-            "std_data": [],
+            "data": [0] * num_channels,
+            "std_data": [0] * num_channels,
         }
-    if channels == None:
-        channels = range(0, pedestals["params"]["channels"])
+
     for chan in channels:
         ped_data = np.hstack(pedestals["data"][chan])
         if pedestals["params"]["model"] == "hdsocv1":
             stitched_rawpeds = []
             lengths = [len(p) for p in pedestals["rawdata"][chan]]
 
             for i in range(min(lengths)):
@@ -46,20 +49,20 @@
         if filter_outlier and not np.all(
             ped_data == ped_data[0]
         ):  # Filter outliers utilizing a modified z-score
             data_length = len(ped_data)
             stddata_length = len(ped_stddata)
             ped_data = filter_outliers(ped_data, filter_threshold)
             ped_stddata = filter_outliers(ped_stddata, filter_threshold)
-            return_ped["num_removed"]["data"].append(data_length - len(ped_data))
-            return_ped["num_removed"]["std_data"].append(
-                stddata_length - len(ped_stddata)
+            return_ped["num_removed"]["data"][chan] = data_length - len(ped_data)
+            return_ped["num_removed"]["std_data"][chan] = stddata_length - len(
+                ped_stddata
             )
-        return_ped["data"].append(ped_data)
-        return_ped["std_data"].append(ped_stddata)
+        return_ped["data"][chan] = ped_data
+        return_ped["std_data"][chan] = ped_stddata
 
     return return_ped
 
 
 def is_outlier(data, thresh=3.5):
     """Using a modified Z-score to detect outliers.
```

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/udc16_pedestals_generator.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/udc16_pedestals_generator.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/upac32_pedestals_controller.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/upac32_pedestals_controller.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/pedestals/upac96_pedestals_generator.py` & `naludaq-0.17.1/src/naludaq/tools/pedestals/upac96_pedestals_generator.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/threshold_scan/__init__.py` & `naludaq-0.17.1/src/naludaq/tools/threshold_scan/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/threshold_scan/hdsoc_thresholdscan.py` & `naludaq-0.17.1/src/naludaq/tools/threshold_scan/hdsoc_thresholdscan.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/threshold_scan/threshold_scan.py` & `naludaq-0.17.1/src/naludaq/tools/threshold_scan/threshold_scan.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/timing_cal/__init__.py` & `naludaq-0.17.1/src/naludaq/tools/timing_cal/__init__.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/timing_cal/calibration.py` & `naludaq-0.17.1/src/naludaq/tools/timing_cal/calibration.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/timing_cal/correcter.py` & `naludaq-0.17.1/src/naludaq/tools/timing_cal/correcter.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq/tools/waiter/eventwaiter.py` & `naludaq-0.17.1/src/naludaq/tools/waiter/eventwaiter.py`

 * *Files identical despite different names*

### Comparing `naludaq-0.17.0/src/naludaq.egg-info/PKG-INFO` & `naludaq-0.17.1/src/naludaq.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: naludaq
-Version: 0.17.0
+Version: 0.17.1
 Summary: Backend package for Nalu Scientific hardware
 Home-page: 
 Author: Thomas Yang, Emily Lum, Terry Pham
 Author-email: Marcus Luck <marcus@naluscientific.com>, Mitchell Matsumori-Kelly <mitchell@naluscientific.com>, Alvin Yang <alvin@naluscientific.com>, Kenneth Lauritzen <kenneth@naluscientific.com>, Ben Rotter <ben@naluscientific.com>
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Programming Language :: Python :: 3
```

### Comparing `naludaq-0.17.0/src/naludaq.egg-info/SOURCES.txt` & `naludaq-0.17.1/src/naludaq.egg-info/SOURCES.txt`

 * *Files identical despite different names*

