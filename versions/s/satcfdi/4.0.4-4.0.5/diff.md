# Comparing `tmp/satcfdi-4.0.4.tar.gz` & `tmp/satcfdi-4.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "satcfdi-4.0.4.tar", last modified: Wed Apr  5 06:49:03 2023, max compression
+gzip compressed data, was "satcfdi-4.0.5.tar", last modified: Fri Apr  7 05:56:57 2023, max compression
```

## Comparing `satcfdi-4.0.4.tar` & `satcfdi-4.0.5.tar`

### file list

```diff
@@ -1,538 +1,538 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.807290 satcfdi-4.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)     6576 2023-04-05 06:49:03.807290 satcfdi-4.0.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/
--rw-r--r--   0 runner    (1001) docker     (123)      356 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      689 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/__version__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/accounting/
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/accounting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/accounting/_ansi_colors.py
--rw-r--r--   0 runner    (1001) docker     (123)     4419 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/accounting/email.py
--rw-r--r--   0 runner    (1001) docker     (123)     3177 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/accounting/formatters.py
--rw-r--r--   0 runner    (1001) docker     (123)     8922 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/accounting/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/accounting/process.py
--rw-r--r--   0 runner    (1001) docker     (123)     5083 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/ans1e.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/apis/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/apis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5877 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/apis/banxico.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.731289 satcfdi-4.0.4/satcfdi/certifica/
--rw-r--r--   0 runner    (1001) docker     (123)     9036 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/certifica/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3550 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/cfdi.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.731289 satcfdi-4.0.4/satcfdi/cli/
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2419 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/cli/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.731289 satcfdi-4.0.4/satcfdi/create/
--rw-r--r--   0 runner    (1001) docker     (123)     1018 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.731289 satcfdi-4.0.4/satcfdi/create/addendas/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/addendas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19252 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/addendas/dvz11.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.731289 satcfdi-4.0.4/satcfdi/create/cancela/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cancela/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2075 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cancela/aceptacionrechazo.py
--rw-r--r--   0 runner    (1001) docker     (123)     2444 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cancela/cancelacion.py
--rw-r--r--   0 runner    (1001) docker     (123)     2523 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cancela/cancelacionretencion.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.735289 satcfdi-4.0.4/satcfdi/create/cfd/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2073 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/aerolineas10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/aieps10.py
--rw-r--r--   0 runner    (1001) docker     (123)    58811 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/cartaporte10.py
--rw-r--r--   0 runner    (1001) docker     (123)    51849 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/cartaporte20.py
--rw-r--r--   0 runner    (1001) docker     (123)    12583 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/cce10.py
--rw-r--r--   0 runner    (1001) docker     (123)    15000 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/cce11.py
--rw-r--r--   0 runner    (1001) docker     (123)    23020 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/cfdi32.py
--rw-r--r--   0 runner    (1001) docker     (123)    13578 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/cfdi33.py
--rw-r--r--   0 runner    (1001) docker     (123)    41560 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/cfdi40.py
--rw-r--r--   0 runner    (1001) docker     (123)     4680 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/consumodecombustibles10.py
--rw-r--r--   0 runner    (1001) docker     (123)     4898 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/consumodecombustibles11.py
--rw-r--r--   0 runner    (1001) docker     (123)    14756 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/decreto10.py
--rw-r--r--   0 runner    (1001) docker     (123)     4567 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/destruccion10.py
--rw-r--r--   0 runner    (1001) docker     (123)    37481 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/detallista.py
--rw-r--r--   0 runner    (1001) docker     (123)     1002 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/divisas10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/donat11.py
--rw-r--r--   0 runner    (1001) docker     (123)     6338 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ecb10.py
--rw-r--r--   0 runner    (1001) docker     (123)     4765 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ecc.py
--rw-r--r--   0 runner    (1001) docker     (123)     5729 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ecc11.py
--rw-r--r--   0 runner    (1001) docker     (123)     5307 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ecc12.py
--rw-r--r--   0 runner    (1001) docker     (123)    16192 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/gceh10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1783 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/iedu10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2917 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ieeh10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2803 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/implocal10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2634 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ine10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2693 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ine11.py
--rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/leyendasFisc10.py
--rw-r--r--   0 runner    (1001) docker     (123)    12439 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/nomina11.py
--rw-r--r--   0 runner    (1001) docker     (123)    27896 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/nomina12.py
--rw-r--r--   0 runner    (1001) docker     (123)    16117 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/notariospublicos10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2638 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/obrasarte10.py
--rw-r--r--   0 runner    (1001) docker     (123)    13577 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/pago10.py
--rw-r--r--   0 runner    (1001) docker     (123)    14817 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/pago20.py
--rw-r--r--   0 runner    (1001) docker     (123)     1499 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/pagoenespecie10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/pfic10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/psgecfd.py
--rw-r--r--   0 runner    (1001) docker     (123)      767 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/registrofiscal10.py
--rw-r--r--   0 runner    (1001) docker     (123)     3467 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/servicioparcial10.py
--rw-r--r--   0 runner    (1001) docker     (123)     5255 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/spei.py
--rw-r--r--   0 runner    (1001) docker     (123)     9920 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/terceros11.py
--rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/tfd10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1559 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/tfd11.py
--rw-r--r--   0 runner    (1001) docker     (123)     2748 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/tpe10.py
--rw-r--r--   0 runner    (1001) docker     (123)     3424 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/valesdedespensa10.py
--rw-r--r--   0 runner    (1001) docker     (123)     4113 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/vehiculousado10.py
--rw-r--r--   0 runner    (1001) docker     (123)     4796 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/cfd/ventavehiculos11.py
--rw-r--r--   0 runner    (1001) docker     (123)     6644 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/compute.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.739289 satcfdi-4.0.4/satcfdi/create/contabilidad/
--rw-r--r--   0 runner    (1001) docker     (123)     6321 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/AuxiliarCtas11.py
--rw-r--r--   0 runner    (1001) docker     (123)     6335 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/AuxiliarCtas13.py
--rw-r--r--   0 runner    (1001) docker     (123)     4386 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/BCE11.py
--rw-r--r--   0 runner    (1001) docker     (123)     4346 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/BCE13.py
--rw-r--r--   0 runner    (1001) docker     (123)    23055 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/PLZ11.py
--rw-r--r--   0 runner    (1001) docker     (123)    23175 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/PLZ13.py
--rw-r--r--   0 runner    (1001) docker     (123)    12981 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/RepAux12.py
--rw-r--r--   0 runner    (1001) docker     (123)    12995 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/RepAux13.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3866 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/catalogocuentas11.py
--rw-r--r--   0 runner    (1001) docker     (123)     3996 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/catalogocuentas13.py
--rw-r--r--   0 runner    (1001) docker     (123)     2043 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/sellodigital11.py
--rw-r--r--   0 runner    (1001) docker     (123)     2177 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/contabilidad/sellodigital13.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.739289 satcfdi-4.0.4/satcfdi/create/pld/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16444 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/ari.py
--rw-r--r--   0 runner    (1001) docker     (123)    28791 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/avi.py
--rw-r--r--   0 runner    (1001) docker     (123)    17532 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/bli.py
--rw-r--r--   0 runner    (1001) docker     (123)    15640 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/chv.py
--rw-r--r--   0 runner    (1001) docker     (123)    27759 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/din.py
--rw-r--r--   0 runner    (1001) docker     (123)    17674 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/don.py
--rw-r--r--   0 runner    (1001) docker     (123)    44314 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/fep.py
--rw-r--r--   0 runner    (1001) docker     (123)    37185 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/fes.py
--rw-r--r--   0 runner    (1001) docker     (123)    19120 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/inm.py
--rw-r--r--   0 runner    (1001) docker     (123)    18872 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/jys.py
--rw-r--r--   0 runner    (1001) docker     (123)    15870 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/mjr.py
--rw-r--r--   0 runner    (1001) docker     (123)    19497 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/mpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    15958 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/oba.py
--rw-r--r--   0 runner    (1001) docker     (123)    55617 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/spr.py
--rw-r--r--   0 runner    (1001) docker     (123)    23092 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/tcv.py
--rw-r--r--   0 runner    (1001) docker     (123)    14962 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/tdr.py
--rw-r--r--   0 runner    (1001) docker     (123)    15191 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/tpp.py
--rw-r--r--   0 runner    (1001) docker     (123)    14550 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/tsc.py
--rw-r--r--   0 runner    (1001) docker     (123)    18502 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/pld/veh.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.743289 satcfdi-4.0.4/satcfdi/create/retencion/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2478 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/arrendamientoenfideicomiso10.py
--rw-r--r--   0 runner    (1001) docker     (123)     3963 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/dividendos10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1305 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/enajenaciondeacciones10.py
--rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/fideicomisonoempresarial10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2022 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/intereses10.py
--rw-r--r--   0 runner    (1001) docker     (123)     2463 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/intereseshipotecarios10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/operacionesconderivados10.py
--rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/pagosaextranjeros10.py
--rw-r--r--   0 runner    (1001) docker     (123)     3358 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/planesderetiro10.py
--rw-r--r--   0 runner    (1001) docker     (123)     5360 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/planesderetiro11.py
--rw-r--r--   0 runner    (1001) docker     (123)     9823 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/plataformasTecnologicas10.py
--rw-r--r--   0 runner    (1001) docker     (123)     1481 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/premios10.py
--rw-r--r--   0 runner    (1001) docker     (123)    11728 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/retenciones10.py
--rw-r--r--   0 runner    (1001) docker     (123)    16317 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/retenciones20.py
--rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/retencion/sectorfinanciero10.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.743289 satcfdi-4.0.4/satcfdi/create/w3/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/w3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11956 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/w3/ds.py
--rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/create/w3/signature.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.743289 satcfdi-4.0.4/satcfdi/csf/
--rw-r--r--   0 runner    (1001) docker     (123)     1927 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/csf/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.743289 satcfdi-4.0.4/satcfdi/diot/
--rw-r--r--   0 runner    (1001) docker     (123)      983 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/diot/De_srv_x509.CER
--rw-r--r--   0 runner    (1001) docker     (123)    17234 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/diot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8002 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/diot/catalog.py
--rw-r--r--   0 runner    (1001) docker     (123)     7076 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/diot/code.py
--rw-r--r--   0 runner    (1001) docker     (123)     1476 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/diot/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      720 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/help.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.743289 satcfdi-4.0.4/satcfdi/models/
--rw-r--r--   0 runner    (1001) docker     (123)      294 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6371 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/certificate.py
--rw-r--r--   0 runner    (1001) docker     (123)      490 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/certificate_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     2544 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/certificate_store.py
--rw-r--r--   0 runner    (1001) docker     (123)     1111 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/code.py
--rw-r--r--   0 runner    (1001) docker     (123)      898 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/curp.py
--rw-r--r--   0 runner    (1001) docker     (123)     2043 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/date_period.py
--rw-r--r--   0 runner    (1001) docker     (123)     4722 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/py2html.py
--rw-r--r--   0 runner    (1001) docker     (123)     1482 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/rfc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3671 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/models/signer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.747289 satcfdi-4.0.4/satcfdi/pacs/
--rw-r--r--   0 runner    (1001) docker     (123)     7124 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2789 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/comerciodigital.py
--rw-r--r--   0 runner    (1001) docker     (123)     7227 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/diverza.py
--rw-r--r--   0 runner    (1001) docker     (123)     7558 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/mysuite.py
--rw-r--r--   0 runner    (1001) docker     (123)     3188 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/prodigia.py
--rw-r--r--   0 runner    (1001) docker     (123)    34641 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.747289 satcfdi-4.0.4/satcfdi/pacs/sat_templates/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/aceptacionrechazo.xml
--rw-r--r--   0 runner    (1001) docker     (123)     1985 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/autentica.xml
--rw-r--r--   0 runner    (1001) docker     (123)     3823 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/cancela.bck.xml
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/cancela.xml
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/consulta.xml
--rw-r--r--   0 runner    (1001) docker     (123)      320 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/descarga.xml
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/relacionados.xml
--rw-r--r--   0 runner    (1001) docker     (123)      831 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/signature.xml
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/solicita.xml
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/sat_templates/verifica.xml
--rw-r--r--   0 runner    (1001) docker     (123)     7281 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/pacs/swsapien.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.747289 satcfdi-4.0.4/satcfdi/portal/
--rw-r--r--   0 runner    (1001) docker     (123)     6799 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/portal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2221 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/portal/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2135 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/printer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.767290 satcfdi-4.0.4/satcfdi/transform/
--rw-r--r--   0 runner    (1001) docker     (123)    21080 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/CertsProd.zip
--rw-r--r--   0 runner    (1001) docker     (123)     3283 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123) 15507681 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/catalog.py
--rw-r--r--   0 runner    (1001) docker     (123)     5072 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)   735368 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/objectify.py
--rw-r--r--   0 runner    (1001) docker     (123)     4578 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_environment.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.767290 satcfdi-4.0.4/satcfdi/transform/pdf_templates/
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/CFDIRegistroFiscal.html
--rw-r--r--   0 runner    (1001) docker     (123)     2289 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/CartaPorte.html
--rw-r--r--   0 runner    (1001) docker     (123)      300 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/CfdiRelacionados.html
--rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/Comprobante.html
--rw-r--r--   0 runner    (1001) docker     (123)     3134 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/Conceptos.html
--rw-r--r--   0 runner    (1001) docker     (123)     1436 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/ConsumoDeCombustibles.html
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/DIOT.html
--rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/Nomina.html
--rw-r--r--   0 runner    (1001) docker     (123)     4964 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/Pagos.html
--rw-r--r--   0 runner    (1001) docker     (123)     1260 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/Retenciones.html
--rw-r--r--   0 runner    (1001) docker     (123)     1174 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/TimbreFiscalDigital.html
--rw-r--r--   0 runner    (1001) docker     (123)      731 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/ValesDeDespensa.html
--rw-r--r--   0 runner    (1001) docker     (123)      444 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/_init.html
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/_multiple.html
--rw-r--r--   0 runner    (1001) docker     (123)     2594 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/_style.css
--rw-r--r--   0 runner    (1001) docker     (123)      801 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/pdf_templates/archivo.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/transform/schemas/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.diverza.com/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.diverza.com/schema/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.767290 satcfdi-4.0.4/satcfdi/transform/schemas/www.diverza.com/schema/xsd/
--rw-r--r--   0 runner    (1001) docker     (123)    10151 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.diverza.com/schema/xsd/Addenda_Diverza_v1.1.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.771290 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/
--rw-r--r--   0 runner    (1001) docker     (123)    16498 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/ari.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    25823 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/avi.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    17870 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/bli.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    15997 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/chv.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    24714 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/din.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    17183 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/don.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    31827 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fep.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    28686 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fes.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    18866 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/inm.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    17835 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/jys.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    15908 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mjr.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    18226 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mpc.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    16244 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/oba.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    38880 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    38880 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd.bck
--rw-r--r--   0 runner    (1001) docker     (123)    40966 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr2.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    20552 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tcv.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    15279 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tdr.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    15594 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tpp.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    15384 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tsc.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    18854 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/veh.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.723289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.771290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.771290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/
--rw-r--r--   0 runner    (1001) docker     (123)     4134 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     4381 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.771290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/
--rw-r--r--   0 runner    (1001) docker     (123)     7301 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_1.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     6822 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_2.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.771290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/
--rw-r--r--   0 runner    (1001) docker     (123)     3078 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/
--rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     3069 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogosParaEsqContE/
--rw-r--r--   0 runner    (1001) docker     (123)    43101 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/
--rw-r--r--   0 runner    (1001) docker     (123)    12367 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    12215 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/
--rw-r--r--   0 runner    (1001) docker     (123)     1749 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2081 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/
--rw-r--r--   0 runner    (1001) docker     (123)     2364 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_2.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     4162 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_3.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/
--rw-r--r--   0 runner    (1001) docker     (123)     3822 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_2.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     6864 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_3.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/
--rw-r--r--   0 runner    (1001) docker     (123)     1765 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_2.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_3.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/
--rw-r--r--   0 runner    (1001) docker     (123)     1709 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_2.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     3269 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_3.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogosParaEsqContE/
--rw-r--r--   0 runner    (1001) docker     (123)    82326 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/
--rw-r--r--   0 runner    (1001) docker     (123)     6275 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_2.xslt
--rw-r--r--   0 runner    (1001) docker     (123)    12409 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_3.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/
--rw-r--r--   0 runner    (1001) docker     (123)     1749 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2081 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.719289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/
--rw-r--r--   0 runner    (1001) docker     (123)     4582 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/catalogos/
--rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/catalogos/CatPlataformasTecnologicas.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/
--rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.775290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/catalogos/
--rw-r--r--   0 runner    (1001) docker     (123)    12431 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/catalogos/catRetenciones.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/
--rw-r--r--   0 runner    (1001) docker     (123)     2070 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1761 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/
--rw-r--r--   0 runner    (1001) docker     (123)     1001 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      880 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/
--rw-r--r--   0 runner    (1001) docker     (123)     2689 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2398 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/
--rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1172 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/
--rw-r--r--   0 runner    (1001) docker     (123)     1581 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1365 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/
--rw-r--r--   0 runner    (1001) docker     (123)      875 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      774 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/
--rw-r--r--   0 runner    (1001) docker     (123)     2855 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1814 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/
--rw-r--r--   0 runner    (1001) docker     (123)     1873 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1627 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/catalogos/
--rw-r--r--   0 runner    (1001) docker     (123)      545 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/catalogos/CatPlanesderetiro.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     3062 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2279 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/
--rw-r--r--   0 runner    (1001) docker     (123)     1108 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      945 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     6480 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retenciones.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     6872 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retencionpagov1.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/
--rw-r--r--   0 runner    (1001) docker     (123)     1033 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      858 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/
--rw-r--r--   0 runner    (1001) docker     (123)     7106 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retenciones.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     6594 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retencionpagov2.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/utilerias.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.723289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/cadenaoriginal_2_0/
--rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/cadenaoriginal_2_0/utilerias.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_2/
--rw-r--r--   0 runner    (1001) docker     (123)    12699 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_2/cadenaoriginal_3_2.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.779290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_3/
--rw-r--r--   0 runner    (1001) docker     (123)    12996 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_3/cadenaoriginal_3_3.xslt
--rw-r--r--   0 runner    (1001) docker     (123)    15121 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    13049 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cadenaoriginal_4_0/
--rw-r--r--   0 runner    (1001) docker     (123)    14334 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cadenaoriginal_4_0/cadenaoriginal_4_0.xslt
--rw-r--r--   0 runner    (1001) docker     (123)    15079 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/
--rw-r--r--   0 runner    (1001) docker     (123)    34743 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    24901 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xslt
--rw-r--r--   0 runner    (1001) docker     (123)    29336 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    19813 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/
--rw-r--r--   0 runner    (1001) docker     (123)   428623 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     5238 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/
--rw-r--r--   0 runner    (1001) docker     (123)    10257 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     5628 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/
--rw-r--r--   0 runner    (1001) docker     (123)     8049 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     3023 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     5280 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2923 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/
--rw-r--r--   0 runner    (1001) docker     (123)     6335 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     4562 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/
--rw-r--r--   0 runner    (1001) docker     (123)     2357 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.783290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/
--rw-r--r--   0 runner    (1001) docker     (123)     7022 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     4935 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     9923 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     7560 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.787290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/
--rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigital.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_0.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_1.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.787290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/
--rw-r--r--   0 runner    (1001) docker     (123)     2009 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.787290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/
--rw-r--r--   0 runner    (1001) docker     (123)     2913 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/AcreditamientoIEPS10.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      511 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/AcreditamientoIEPS10.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.787290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/
--rw-r--r--   0 runner    (1001) docker     (123)     1199 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.787290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/
--rw-r--r--   0 runner    (1001) docker     (123)     2642 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.787290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.791290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte/
--rw-r--r--   0 runner    (1001) docker     (123)  2127463 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte/catCartaPorte.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/ComExt/
--rw-r--r--   0 runner    (1001) docker     (123)   910932 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/ComExt/catComExt.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Combustible/
--rw-r--r--   0 runner    (1001) docker     (123)      544 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Combustible/catCombustible.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Nomina/
--rw-r--r--   0 runner    (1001) docker     (123)    11524 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Nomina/catNomina.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Pagos/
--rw-r--r--   0 runner    (1001) docker     (123)      450 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Pagos/catPagos.xsd
--rw-r--r--   0 runner    (1001) docker     (123)  5172181 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/hidrocarburos/
--rw-r--r--   0 runner    (1001) docker     (123)    10013 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/hidrocarburos/catHidrocarburos.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/
--rw-r--r--   0 runner    (1001) docker     (123)     3687 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2184 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/
--rw-r--r--   0 runner    (1001) docker     (123)      575 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      601 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/
--rw-r--r--   0 runner    (1001) docker     (123)     4717 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2994 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2892 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/
--rw-r--r--   0 runner    (1001) docker     (123)    26183 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/
--rw-r--r--   0 runner    (1001) docker     (123)      583 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/divisas.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      507 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/divisas.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.795290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/
--rw-r--r--   0 runner    (1001) docker     (123)      683 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/
--rw-r--r--   0 runner    (1001) docker     (123)     4570 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1091 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/
--rw-r--r--   0 runner    (1001) docker     (123)     4081 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2588 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/
--rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1001 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/
--rw-r--r--   0 runner    (1001) docker     (123)     1879 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1506 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/
--rw-r--r--   0 runner    (1001) docker     (123)     3342 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xslt
--rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/
--rw-r--r--   0 runner    (1001) docker     (123)     1105 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      974 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/
--rw-r--r--   0 runner    (1001) docker     (123)     6944 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     7646 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xslt
--rw-r--r--   0 runner    (1001) docker     (123)    12718 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xsd
--rw-r--r--   0 runner    (1001) docker     (123)    11708 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/
--rw-r--r--   0 runner    (1001) docker     (123)    10305 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     7245 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/
--rw-r--r--   0 runner    (1001) docker     (123)     1602 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/
--rw-r--r--   0 runner    (1001) docker     (123)     1103 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      791 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/
--rw-r--r--   0 runner    (1001) docker     (123)     1487 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xsd
--rw-r--r--   0 runner    (1001) docker     (123)      857 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/
--rw-r--r--   0 runner    (1001) docker     (123)     9917 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     5340 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/
--rw-r--r--   0 runner    (1001) docker     (123)     3597 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1641 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/
--rw-r--r--   0 runner    (1001) docker     (123)     4143 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2635 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.799290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/
--rw-r--r--   0 runner    (1001) docker     (123)     6719 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     3509 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.803290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/
--rw-r--r--   0 runner    (1001) docker     (123)     3935 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.803290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/
--rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1900 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.803290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/
--rw-r--r--   0 runner    (1001) docker     (123)     3222 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     2120 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.803290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/
--rw-r--r--   0 runner    (1001) docker     (123)     2894 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1243 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.803290 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/
--rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/TimbreFiscalDigital.xsd
--rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/cadenaoriginal_TFD_1_0.xslt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/transform/schemas/www.w3.org/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi/transform/schemas/www.w3.org/TR/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.803290 satcfdi-4.0.4/satcfdi/transform/schemas/www.w3.org/TR/xmldsig-core/
--rw-r--r--   0 runner    (1001) docker     (123)     7736 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas/www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd
--rw-r--r--   0 runner    (1001) docker     (123)   253767 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)   957389 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/xmlify.py
--rw-r--r--   0 runner    (1001) docker     (123)     4049 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/transform/xslt.py
--rw-r--r--   0 runner    (1001) docker     (123)      448 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3152 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/xelement.py
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-04-05 06:48:54.000000 satcfdi-4.0.4/satcfdi/zip.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.727289 satcfdi-4.0.4/satcfdi.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6576 2023-04-05 06:49:03.000000 satcfdi-4.0.4/satcfdi.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    25165 2023-04-05 06:49:03.000000 satcfdi-4.0.4/satcfdi.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 06:49:03.000000 satcfdi-4.0.4/satcfdi.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-05 06:49:03.000000 satcfdi-4.0.4/satcfdi.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-05 06:49:03.000000 satcfdi-4.0.4/satcfdi.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-05 06:49:03.000000 satcfdi-4.0.4/satcfdi.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 06:49:03.807290 satcfdi-4.0.4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2920 2023-04-05 06:48:54.000000 satcfdi-4.0.4/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:49:03.807290 satcfdi-4.0.4/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     4144 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_accounting.py
--rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_api_banxico.py
--rw-r--r--   0 runner    (1001) docker     (123)     7636 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_certifica.py
--rw-r--r--   0 runner    (1001) docker     (123)     1811 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_cfdi.py
--rw-r--r--   0 runner    (1001) docker     (123)     1503 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create.py
--rw-r--r--   0 runner    (1001) docker     (123)     3993 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create_addenda.py
--rw-r--r--   0 runner    (1001) docker     (123)     1712 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create_cancelacion.py
--rw-r--r--   0 runner    (1001) docker     (123)    10551 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create_cfdi33.py
--rw-r--r--   0 runner    (1001) docker     (123)    15061 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create_cfdi40.py
--rw-r--r--   0 runner    (1001) docker     (123)     3619 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create_cfdi40_raw.py
--rw-r--r--   0 runner    (1001) docker     (123)     5241 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create_pld.py
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_create_retenciones.py
--rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_csf.py
--rw-r--r--   0 runner    (1001) docker     (123)      578 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_custom_template.py
--rw-r--r--   0 runner    (1001) docker     (123)    17132 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_diot.py
--rw-r--r--   0 runner    (1001) docker     (123)     9139 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2373 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_pac_comerciodigital.py
--rw-r--r--   0 runner    (1001) docker     (123)     8566 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_pac_diverza.py
--rw-r--r--   0 runner    (1001) docker     (123)     6361 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_pac_mysuite.py
--rw-r--r--   0 runner    (1001) docker     (123)     3219 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_pac_prodigia.py
--rw-r--r--   0 runner    (1001) docker     (123)     5332 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_pac_sat.py
--rw-r--r--   0 runner    (1001) docker     (123)    16448 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_pac_swsapien.py
--rw-r--r--   0 runner    (1001) docker     (123)     1652 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_portal.py
--rw-r--r--   0 runner    (1001) docker     (123)      387 2023-04-05 06:48:54.000000 satcfdi-4.0.4/tests/test_satcfdi.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.946853 satcfdi-4.0.5/
+-rw-r--r--   0 runner    (1001) docker     (123)     6576 2023-04-07 05:56:57.946853 satcfdi-4.0.5/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.854850 satcfdi-4.0.5/satcfdi/
+-rw-r--r--   0 runner    (1001) docker     (123)      356 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      689 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/__version__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.854850 satcfdi-4.0.5/satcfdi/accounting/
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/accounting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/accounting/_ansi_colors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4419 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/accounting/email.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3177 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/accounting/formatters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8922 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/accounting/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/accounting/process.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5083 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/ans1e.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.854850 satcfdi-4.0.5/satcfdi/apis/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/apis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5877 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/apis/banxico.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.854850 satcfdi-4.0.5/satcfdi/certifica/
+-rw-r--r--   0 runner    (1001) docker     (123)     9036 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/certifica/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3550 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/cfdi.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.854850 satcfdi-4.0.5/satcfdi/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2419 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/cli/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.854850 satcfdi-4.0.5/satcfdi/create/
+-rw-r--r--   0 runner    (1001) docker     (123)     1018 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.858850 satcfdi-4.0.5/satcfdi/create/addendas/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/addendas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19252 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/addendas/dvz11.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.858850 satcfdi-4.0.5/satcfdi/create/cancela/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cancela/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2075 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cancela/aceptacionrechazo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2444 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cancela/cancelacion.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2523 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cancela/cancelacionretencion.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.862851 satcfdi-4.0.5/satcfdi/create/cfd/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2073 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/aerolineas10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/aieps10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    58811 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/cartaporte10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51849 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/cartaporte20.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12583 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/cce10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15000 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/cce11.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23020 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/cfdi32.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13578 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/cfdi33.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41560 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/cfdi40.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4680 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/consumodecombustibles10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4898 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/consumodecombustibles11.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14756 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/decreto10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4567 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/destruccion10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37481 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/detallista.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1002 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/divisas10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/donat11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6338 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ecb10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4765 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ecc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5729 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ecc11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5307 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ecc12.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16192 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/gceh10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1783 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/iedu10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2917 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ieeh10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2803 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/implocal10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2634 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ine10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2693 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ine11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/leyendasFisc10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12439 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/nomina11.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27896 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/nomina12.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16117 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/notariospublicos10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2638 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/obrasarte10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13577 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/pago10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14817 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/pago20.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1499 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/pagoenespecie10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/pfic10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/psgecfd.py
+-rw-r--r--   0 runner    (1001) docker     (123)      767 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/registrofiscal10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3467 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/servicioparcial10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5255 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/spei.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9920 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/terceros11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/tfd10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1559 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/tfd11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2748 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/tpe10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3424 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/valesdedespensa10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4113 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/vehiculousado10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4796 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/cfd/ventavehiculos11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6644 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/compute.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.866851 satcfdi-4.0.5/satcfdi/create/contabilidad/
+-rw-r--r--   0 runner    (1001) docker     (123)     6321 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/AuxiliarCtas11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6335 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/AuxiliarCtas13.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4386 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/BCE11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4346 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/BCE13.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23055 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/PLZ11.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23175 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/PLZ13.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12981 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/RepAux12.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12995 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/RepAux13.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3866 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/catalogocuentas11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3996 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/catalogocuentas13.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2043 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/sellodigital11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2177 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/contabilidad/sellodigital13.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.870851 satcfdi-4.0.5/satcfdi/create/pld/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16444 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/ari.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28791 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/avi.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17532 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/bli.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15640 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/chv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27759 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/din.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17674 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/don.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44314 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/fep.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37185 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/fes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19120 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/inm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18872 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/jys.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15870 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/mjr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19497 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/mpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15958 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/oba.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55617 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/spr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23092 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/tcv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14962 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/tdr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15191 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/tpp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14550 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/tsc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18502 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/pld/veh.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.870851 satcfdi-4.0.5/satcfdi/create/retencion/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2478 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/arrendamientoenfideicomiso10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3963 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/dividendos10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1305 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/enajenaciondeacciones10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/fideicomisonoempresarial10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2022 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/intereses10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2463 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/intereseshipotecarios10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/operacionesconderivados10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/pagosaextranjeros10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3358 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/planesderetiro10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5360 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/planesderetiro11.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9823 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/plataformasTecnologicas10.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1481 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/premios10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11728 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/retenciones10.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16317 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/retenciones20.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/retencion/sectorfinanciero10.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.870851 satcfdi-4.0.5/satcfdi/create/w3/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/w3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11956 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/w3/ds.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/create/w3/signature.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.870851 satcfdi-4.0.5/satcfdi/csf/
+-rw-r--r--   0 runner    (1001) docker     (123)     1927 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/csf/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.874851 satcfdi-4.0.5/satcfdi/diot/
+-rw-r--r--   0 runner    (1001) docker     (123)      983 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/diot/De_srv_x509.CER
+-rw-r--r--   0 runner    (1001) docker     (123)    17234 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/diot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8002 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/diot/catalog.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7076 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/diot/code.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1476 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/diot/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      720 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/help.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.874851 satcfdi-4.0.5/satcfdi/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      294 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6371 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      490 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/certificate_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2544 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/certificate_store.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1111 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/code.py
+-rw-r--r--   0 runner    (1001) docker     (123)      898 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/curp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2043 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/date_period.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4722 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/py2html.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1482 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/rfc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3671 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/models/signer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.874851 satcfdi-4.0.5/satcfdi/pacs/
+-rw-r--r--   0 runner    (1001) docker     (123)     7124 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2789 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/comerciodigital.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7227 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/diverza.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7558 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/mysuite.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3188 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/prodigia.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34641 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.878851 satcfdi-4.0.5/satcfdi/pacs/sat_templates/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/aceptacionrechazo.xml
+-rw-r--r--   0 runner    (1001) docker     (123)     1985 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/autentica.xml
+-rw-r--r--   0 runner    (1001) docker     (123)     3823 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/cancela.bck.xml
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/cancela.xml
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/consulta.xml
+-rw-r--r--   0 runner    (1001) docker     (123)      320 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/descarga.xml
+-rw-r--r--   0 runner    (1001) docker     (123)      416 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/relacionados.xml
+-rw-r--r--   0 runner    (1001) docker     (123)      831 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/signature.xml
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/solicita.xml
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/sat_templates/verifica.xml
+-rw-r--r--   0 runner    (1001) docker     (123)     7281 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/pacs/swsapien.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.878851 satcfdi-4.0.5/satcfdi/portal/
+-rw-r--r--   0 runner    (1001) docker     (123)     6799 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/portal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2221 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/portal/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2135 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/printer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.898852 satcfdi-4.0.5/satcfdi/transform/
+-rw-r--r--   0 runner    (1001) docker     (123)    21080 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/CertsProd.zip
+-rw-r--r--   0 runner    (1001) docker     (123)     3283 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123) 15507681 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/catalog.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5072 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)   735368 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/objectify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4578 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_environment.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.902852 satcfdi-4.0.5/satcfdi/transform/pdf_templates/
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/CFDIRegistroFiscal.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2289 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/CartaPorte.html
+-rw-r--r--   0 runner    (1001) docker     (123)      300 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/CfdiRelacionados.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/Comprobante.html
+-rw-r--r--   0 runner    (1001) docker     (123)     3154 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/Conceptos.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1436 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/ConsumoDeCombustibles.html
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/DIOT.html
+-rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/Nomina.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4964 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/Pagos.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1260 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/Retenciones.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1174 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/TimbreFiscalDigital.html
+-rw-r--r--   0 runner    (1001) docker     (123)      731 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/ValesDeDespensa.html
+-rw-r--r--   0 runner    (1001) docker     (123)      444 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/_init.html
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/_multiple.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2594 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/_style.css
+-rw-r--r--   0 runner    (1001) docker     (123)      801 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/pdf_templates/archivo.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.850850 satcfdi-4.0.5/satcfdi/transform/schemas/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.diverza.com/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.diverza.com/schema/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.902852 satcfdi-4.0.5/satcfdi/transform/schemas/www.diverza.com/schema/xsd/
+-rw-r--r--   0 runner    (1001) docker     (123)    10151 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.diverza.com/schema/xsd/Addenda_Diverza_v1.1.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.906852 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/
+-rw-r--r--   0 runner    (1001) docker     (123)    16498 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/ari.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    25823 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/avi.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    17870 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/bli.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    15997 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/chv.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    24714 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/din.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    17183 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/don.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    31827 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fep.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    28686 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fes.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    18866 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/inm.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    17835 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/jys.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    15908 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mjr.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    18226 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mpc.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    16244 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/oba.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    38880 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    38880 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd.bck
+-rw-r--r--   0 runner    (1001) docker     (123)    40966 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr2.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    20552 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tcv.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    15279 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tdr.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    15594 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tpp.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    15384 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tsc.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    18854 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/veh.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.846850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.906852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.842850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.906852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/
+-rw-r--r--   0 runner    (1001) docker     (123)     4134 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     4381 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.906852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/
+-rw-r--r--   0 runner    (1001) docker     (123)     7301 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_1.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     6822 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_2.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.906852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/
+-rw-r--r--   0 runner    (1001) docker     (123)     3078 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.906852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/
+-rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     3069 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogosParaEsqContE/
+-rw-r--r--   0 runner    (1001) docker     (123)    43101 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/
+-rw-r--r--   0 runner    (1001) docker     (123)    12367 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    12215 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/
+-rw-r--r--   0 runner    (1001) docker     (123)     1749 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2081 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.846850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/
+-rw-r--r--   0 runner    (1001) docker     (123)     2364 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_2.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     4162 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_3.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/
+-rw-r--r--   0 runner    (1001) docker     (123)     3822 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_2.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     6864 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_3.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/
+-rw-r--r--   0 runner    (1001) docker     (123)     1765 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_2.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_3.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/
+-rw-r--r--   0 runner    (1001) docker     (123)     1709 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_2.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     3269 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_3.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogosParaEsqContE/
+-rw-r--r--   0 runner    (1001) docker     (123)    82326 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/
+-rw-r--r--   0 runner    (1001) docker     (123)     6275 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_2.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)    12409 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_3.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/
+-rw-r--r--   0 runner    (1001) docker     (123)     1749 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2081 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.846850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/
+-rw-r--r--   0 runner    (1001) docker     (123)     4582 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/catalogos/
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/catalogos/CatPlataformasTecnologicas.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.910852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/
+-rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/catalogos/
+-rw-r--r--   0 runner    (1001) docker     (123)    12431 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/catalogos/catRetenciones.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/
+-rw-r--r--   0 runner    (1001) docker     (123)     2070 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1761 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/
+-rw-r--r--   0 runner    (1001) docker     (123)     1001 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      880 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/
+-rw-r--r--   0 runner    (1001) docker     (123)     2689 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2398 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/
+-rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1172 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/
+-rw-r--r--   0 runner    (1001) docker     (123)     1581 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1365 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/
+-rw-r--r--   0 runner    (1001) docker     (123)      875 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      774 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/
+-rw-r--r--   0 runner    (1001) docker     (123)     2855 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1814 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/
+-rw-r--r--   0 runner    (1001) docker     (123)     1873 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1627 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/catalogos/
+-rw-r--r--   0 runner    (1001) docker     (123)      545 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/catalogos/CatPlanesderetiro.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     3062 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2279 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/
+-rw-r--r--   0 runner    (1001) docker     (123)     1108 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      945 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     6480 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retenciones.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     6872 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retencionpagov1.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/
+-rw-r--r--   0 runner    (1001) docker     (123)     1033 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/
+-rw-r--r--   0 runner    (1001) docker     (123)     7106 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retenciones.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     6594 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retencionpagov2.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/utilerias.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.850850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.850850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.846850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.914852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/cadenaoriginal_2_0/
+-rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/cadenaoriginal_2_0/utilerias.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_2/
+-rw-r--r--   0 runner    (1001) docker     (123)    12699 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_2/cadenaoriginal_3_2.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_3/
+-rw-r--r--   0 runner    (1001) docker     (123)    12996 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_3/cadenaoriginal_3_3.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)    15121 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    13049 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cadenaoriginal_4_0/
+-rw-r--r--   0 runner    (1001) docker     (123)    14334 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cadenaoriginal_4_0/cadenaoriginal_4_0.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)    15079 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/
+-rw-r--r--   0 runner    (1001) docker     (123)    34743 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    24901 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)    29336 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    19813 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/
+-rw-r--r--   0 runner    (1001) docker     (123)   428623 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     5238 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/
+-rw-r--r--   0 runner    (1001) docker     (123)    10257 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     5628 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/
+-rw-r--r--   0 runner    (1001) docker     (123)     8049 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     3023 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     5280 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2923 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/
+-rw-r--r--   0 runner    (1001) docker     (123)     6335 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     4562 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.918852 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/
+-rw-r--r--   0 runner    (1001) docker     (123)     2357 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.922853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/
+-rw-r--r--   0 runner    (1001) docker     (123)     7022 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     4935 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     9923 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     7560 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.922853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/
+-rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigital.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_0.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_1.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.922853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/
+-rw-r--r--   0 runner    (1001) docker     (123)     2009 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.922853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/
+-rw-r--r--   0 runner    (1001) docker     (123)     2913 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/AcreditamientoIEPS10.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      511 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/AcreditamientoIEPS10.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.922853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/
+-rw-r--r--   0 runner    (1001) docker     (123)     1199 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.922853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/
+-rw-r--r--   0 runner    (1001) docker     (123)     2642 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.922853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.930853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte/
+-rw-r--r--   0 runner    (1001) docker     (123)  2127463 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte/catCartaPorte.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.930853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/ComExt/
+-rw-r--r--   0 runner    (1001) docker     (123)   910932 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/ComExt/catComExt.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Combustible/
+-rw-r--r--   0 runner    (1001) docker     (123)      544 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Combustible/catCombustible.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Nomina/
+-rw-r--r--   0 runner    (1001) docker     (123)    11524 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Nomina/catNomina.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Pagos/
+-rw-r--r--   0 runner    (1001) docker     (123)      450 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Pagos/catPagos.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)  5172181 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/hidrocarburos/
+-rw-r--r--   0 runner    (1001) docker     (123)    10013 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/hidrocarburos/catHidrocarburos.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/
+-rw-r--r--   0 runner    (1001) docker     (123)     3687 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2184 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/
+-rw-r--r--   0 runner    (1001) docker     (123)      575 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      601 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/
+-rw-r--r--   0 runner    (1001) docker     (123)     4717 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2994 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2892 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/
+-rw-r--r--   0 runner    (1001) docker     (123)    26183 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/
+-rw-r--r--   0 runner    (1001) docker     (123)      583 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/divisas.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      507 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/divisas.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/
+-rw-r--r--   0 runner    (1001) docker     (123)      683 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/
+-rw-r--r--   0 runner    (1001) docker     (123)     4570 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1091 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/
+-rw-r--r--   0 runner    (1001) docker     (123)     4081 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2588 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/
+-rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1001 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.934853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/
+-rw-r--r--   0 runner    (1001) docker     (123)     1879 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1506 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/
+-rw-r--r--   0 runner    (1001) docker     (123)     3342 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/
+-rw-r--r--   0 runner    (1001) docker     (123)     1105 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      974 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/
+-rw-r--r--   0 runner    (1001) docker     (123)     6944 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     7646 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xslt
+-rw-r--r--   0 runner    (1001) docker     (123)    12718 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)    11708 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/
+-rw-r--r--   0 runner    (1001) docker     (123)    10305 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     7245 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/
+-rw-r--r--   0 runner    (1001) docker     (123)     1602 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/
+-rw-r--r--   0 runner    (1001) docker     (123)     1103 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      791 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/
+-rw-r--r--   0 runner    (1001) docker     (123)     1487 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)      857 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/
+-rw-r--r--   0 runner    (1001) docker     (123)     9917 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     5340 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/
+-rw-r--r--   0 runner    (1001) docker     (123)     3597 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1641 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/
+-rw-r--r--   0 runner    (1001) docker     (123)     4143 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2635 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.938853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/
+-rw-r--r--   0 runner    (1001) docker     (123)     6719 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     3509 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.850850 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.942853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/
+-rw-r--r--   0 runner    (1001) docker     (123)     3935 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.942853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/
+-rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1900 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.942853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/
+-rw-r--r--   0 runner    (1001) docker     (123)     3222 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     2120 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.942853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/
+-rw-r--r--   0 runner    (1001) docker     (123)     2894 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1243 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.942853 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/
+-rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/TimbreFiscalDigital.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/cadenaoriginal_TFD_1_0.xslt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.850850 satcfdi-4.0.5/satcfdi/transform/schemas/www.w3.org/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.850850 satcfdi-4.0.5/satcfdi/transform/schemas/www.w3.org/TR/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.942853 satcfdi-4.0.5/satcfdi/transform/schemas/www.w3.org/TR/xmldsig-core/
+-rw-r--r--   0 runner    (1001) docker     (123)     7736 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas/www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd
+-rw-r--r--   0 runner    (1001) docker     (123)   253767 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)   957389 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/xmlify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4049 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/transform/xslt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      448 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3152 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/xelement.py
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-04-07 05:56:46.000000 satcfdi-4.0.5/satcfdi/zip.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.854850 satcfdi-4.0.5/satcfdi.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     6576 2023-04-07 05:56:57.000000 satcfdi-4.0.5/satcfdi.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    25165 2023-04-07 05:56:57.000000 satcfdi-4.0.5/satcfdi.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 05:56:57.000000 satcfdi-4.0.5/satcfdi.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-07 05:56:57.000000 satcfdi-4.0.5/satcfdi.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-07 05:56:57.000000 satcfdi-4.0.5/satcfdi.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 05:56:57.000000 satcfdi-4.0.5/satcfdi.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 05:56:57.946853 satcfdi-4.0.5/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2920 2023-04-07 05:56:46.000000 satcfdi-4.0.5/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:56:57.946853 satcfdi-4.0.5/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     4144 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_accounting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_api_banxico.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7636 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_certifica.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1811 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_cfdi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1503 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3993 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create_addenda.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1712 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create_cancelacion.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10551 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create_cfdi33.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15061 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create_cfdi40.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3619 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create_cfdi40_raw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5241 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create_pld.py
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_create_retenciones.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_csf.py
+-rw-r--r--   0 runner    (1001) docker     (123)      578 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_custom_template.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17132 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_diot.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9139 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2373 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_pac_comerciodigital.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8566 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_pac_diverza.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6361 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_pac_mysuite.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3219 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_pac_prodigia.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5332 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_pac_sat.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16448 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_pac_swsapien.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1652 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_portal.py
+-rw-r--r--   0 runner    (1001) docker     (123)      387 2023-04-07 05:56:46.000000 satcfdi-4.0.5/tests/test_satcfdi.py
```

### Comparing `satcfdi-4.0.4/PKG-INFO` & `satcfdi-4.0.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: satcfdi
-Version: 4.0.4
+Version: 4.0.5
 Summary: The best open-source python library to generate and process SAT's CFDI
 Home-page: https://github.com/SAT-CFDI/python-satcfdi
 Author: satcfdi@outlook.com
 Author-email: satcfdi@outlook.com
 License: MIT License
 Project-URL: Documentation, https://satcfdi.readthedocs.io
 Project-URL: Source, https://github.com/SAT-CFDI/python-satcfdi
```

### Comparing `satcfdi-4.0.4/satcfdi/__version__.py` & `satcfdi-4.0.5/satcfdi/__version__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/accounting/_ansi_colors.py` & `satcfdi-4.0.5/satcfdi/accounting/_ansi_colors.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/accounting/email.py` & `satcfdi-4.0.5/satcfdi/accounting/email.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/accounting/formatters.py` & `satcfdi-4.0.5/satcfdi/accounting/formatters.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/accounting/models.py` & `satcfdi-4.0.5/satcfdi/accounting/models.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/accounting/process.py` & `satcfdi-4.0.5/satcfdi/accounting/process.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/ans1e.py` & `satcfdi-4.0.5/satcfdi/ans1e.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/apis/banxico.py` & `satcfdi-4.0.5/satcfdi/apis/banxico.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/certifica/__init__.py` & `satcfdi-4.0.5/satcfdi/certifica/__init__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/cfdi.py` & `satcfdi-4.0.5/satcfdi/cfdi.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/cli/main.py` & `satcfdi-4.0.5/satcfdi/cli/main.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/__init__.py` & `satcfdi-4.0.5/satcfdi/create/__init__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/addendas/dvz11.py` & `satcfdi-4.0.5/satcfdi/create/addendas/dvz11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cancela/aceptacionrechazo.py` & `satcfdi-4.0.5/satcfdi/create/cancela/aceptacionrechazo.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cancela/cancelacion.py` & `satcfdi-4.0.5/satcfdi/create/cancela/cancelacion.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cancela/cancelacionretencion.py` & `satcfdi-4.0.5/satcfdi/create/cancela/cancelacionretencion.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/aerolineas10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/aerolineas10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/aieps10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/aieps10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/cartaporte10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/cartaporte10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/cartaporte20.py` & `satcfdi-4.0.5/satcfdi/create/cfd/cartaporte20.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/cce10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/cce10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/cce11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/cce11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/cfdi32.py` & `satcfdi-4.0.5/satcfdi/create/cfd/cfdi32.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/cfdi33.py` & `satcfdi-4.0.5/satcfdi/create/cfd/cfdi33.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/cfdi40.py` & `satcfdi-4.0.5/satcfdi/create/cfd/cfdi40.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/consumodecombustibles10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/consumodecombustibles10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/consumodecombustibles11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/consumodecombustibles11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/decreto10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/decreto10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/destruccion10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/destruccion10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/detallista.py` & `satcfdi-4.0.5/satcfdi/create/cfd/detallista.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/divisas10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/divisas10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/donat11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/donat11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ecb10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ecb10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ecc.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ecc.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ecc11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ecc11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ecc12.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ecc12.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/gceh10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/gceh10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/iedu10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/iedu10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ieeh10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ieeh10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/implocal10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/implocal10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ine10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ine10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ine11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ine11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/leyendasFisc10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/leyendasFisc10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/nomina11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/nomina11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/nomina12.py` & `satcfdi-4.0.5/satcfdi/create/cfd/nomina12.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/notariospublicos10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/notariospublicos10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/obrasarte10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/obrasarte10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/pago10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/pago10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/pago20.py` & `satcfdi-4.0.5/satcfdi/create/cfd/pago20.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/pagoenespecie10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/pagoenespecie10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/pfic10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/pfic10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/psgecfd.py` & `satcfdi-4.0.5/satcfdi/create/cfd/psgecfd.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/registrofiscal10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/registrofiscal10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/servicioparcial10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/servicioparcial10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/spei.py` & `satcfdi-4.0.5/satcfdi/create/cfd/spei.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/terceros11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/terceros11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/tfd10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/tfd10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/tfd11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/tfd11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/tpe10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/tpe10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/valesdedespensa10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/valesdedespensa10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/vehiculousado10.py` & `satcfdi-4.0.5/satcfdi/create/cfd/vehiculousado10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/cfd/ventavehiculos11.py` & `satcfdi-4.0.5/satcfdi/create/cfd/ventavehiculos11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/compute.py` & `satcfdi-4.0.5/satcfdi/create/compute.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/AuxiliarCtas11.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/AuxiliarCtas11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/AuxiliarCtas13.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/AuxiliarCtas13.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/BCE11.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/BCE11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/BCE13.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/BCE13.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/PLZ11.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/PLZ11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/PLZ13.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/PLZ13.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/RepAux12.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/RepAux12.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/RepAux13.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/RepAux13.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/catalogocuentas11.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/catalogocuentas11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/catalogocuentas13.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/catalogocuentas13.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/sellodigital11.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/sellodigital11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/contabilidad/sellodigital13.py` & `satcfdi-4.0.5/satcfdi/create/contabilidad/sellodigital13.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/ari.py` & `satcfdi-4.0.5/satcfdi/create/pld/ari.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/avi.py` & `satcfdi-4.0.5/satcfdi/create/pld/avi.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/bli.py` & `satcfdi-4.0.5/satcfdi/create/pld/bli.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/chv.py` & `satcfdi-4.0.5/satcfdi/create/pld/chv.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/din.py` & `satcfdi-4.0.5/satcfdi/create/pld/din.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/don.py` & `satcfdi-4.0.5/satcfdi/create/pld/don.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/fep.py` & `satcfdi-4.0.5/satcfdi/create/pld/fep.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/fes.py` & `satcfdi-4.0.5/satcfdi/create/pld/fes.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/inm.py` & `satcfdi-4.0.5/satcfdi/create/pld/inm.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/jys.py` & `satcfdi-4.0.5/satcfdi/create/pld/jys.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/mjr.py` & `satcfdi-4.0.5/satcfdi/create/pld/mjr.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/mpc.py` & `satcfdi-4.0.5/satcfdi/create/pld/mpc.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/oba.py` & `satcfdi-4.0.5/satcfdi/create/pld/oba.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/spr.py` & `satcfdi-4.0.5/satcfdi/create/pld/spr.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/tcv.py` & `satcfdi-4.0.5/satcfdi/create/pld/tcv.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/tdr.py` & `satcfdi-4.0.5/satcfdi/create/pld/tdr.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/tpp.py` & `satcfdi-4.0.5/satcfdi/create/pld/tpp.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/tsc.py` & `satcfdi-4.0.5/satcfdi/create/pld/tsc.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/pld/veh.py` & `satcfdi-4.0.5/satcfdi/create/pld/veh.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/arrendamientoenfideicomiso10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/arrendamientoenfideicomiso10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/dividendos10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/dividendos10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/enajenaciondeacciones10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/enajenaciondeacciones10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/fideicomisonoempresarial10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/fideicomisonoempresarial10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/intereses10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/intereses10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/intereseshipotecarios10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/intereseshipotecarios10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/operacionesconderivados10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/operacionesconderivados10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/pagosaextranjeros10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/pagosaextranjeros10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/planesderetiro10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/planesderetiro10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/planesderetiro11.py` & `satcfdi-4.0.5/satcfdi/create/retencion/planesderetiro11.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/plataformasTecnologicas10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/plataformasTecnologicas10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/premios10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/premios10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/retenciones10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/retenciones10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/retenciones20.py` & `satcfdi-4.0.5/satcfdi/create/retencion/retenciones20.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/retencion/sectorfinanciero10.py` & `satcfdi-4.0.5/satcfdi/create/retencion/sectorfinanciero10.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/w3/ds.py` & `satcfdi-4.0.5/satcfdi/create/w3/ds.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/create/w3/signature.py` & `satcfdi-4.0.5/satcfdi/create/w3/signature.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/csf/__init__.py` & `satcfdi-4.0.5/satcfdi/csf/__init__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/diot/De_srv_x509.CER` & `satcfdi-4.0.5/satcfdi/diot/De_srv_x509.CER`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/diot/__init__.py` & `satcfdi-4.0.5/satcfdi/diot/__init__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/diot/catalog.py` & `satcfdi-4.0.5/satcfdi/diot/catalog.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/diot/code.py` & `satcfdi-4.0.5/satcfdi/diot/code.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/diot/utils.py` & `satcfdi-4.0.5/satcfdi/diot/utils.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/exceptions.py` & `satcfdi-4.0.5/satcfdi/exceptions.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/certificate.py` & `satcfdi-4.0.5/satcfdi/models/certificate.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/certificate_store.py` & `satcfdi-4.0.5/satcfdi/models/certificate_store.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/code.py` & `satcfdi-4.0.5/satcfdi/models/code.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/curp.py` & `satcfdi-4.0.5/satcfdi/models/curp.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/date_period.py` & `satcfdi-4.0.5/satcfdi/models/date_period.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/py2html.py` & `satcfdi-4.0.5/satcfdi/models/py2html.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/rfc.py` & `satcfdi-4.0.5/satcfdi/models/rfc.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/models/signer.py` & `satcfdi-4.0.5/satcfdi/models/signer.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/__init__.py` & `satcfdi-4.0.5/satcfdi/pacs/__init__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/comerciodigital.py` & `satcfdi-4.0.5/satcfdi/pacs/comerciodigital.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/diverza.py` & `satcfdi-4.0.5/satcfdi/pacs/diverza.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/mysuite.py` & `satcfdi-4.0.5/satcfdi/pacs/mysuite.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/prodigia.py` & `satcfdi-4.0.5/satcfdi/pacs/prodigia.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/sat.py` & `satcfdi-4.0.5/satcfdi/pacs/sat.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/sat_templates/autentica.xml` & `satcfdi-4.0.5/satcfdi/pacs/sat_templates/autentica.xml`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/sat_templates/cancela.bck.xml` & `satcfdi-4.0.5/satcfdi/pacs/sat_templates/cancela.bck.xml`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/sat_templates/signature.xml` & `satcfdi-4.0.5/satcfdi/pacs/sat_templates/signature.xml`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/pacs/swsapien.py` & `satcfdi-4.0.5/satcfdi/pacs/swsapien.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/portal/__init__.py` & `satcfdi-4.0.5/satcfdi/portal/__init__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/portal/utils.py` & `satcfdi-4.0.5/satcfdi/portal/utils.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/printer.py` & `satcfdi-4.0.5/satcfdi/printer.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/CertsProd.zip` & `satcfdi-4.0.5/satcfdi/transform/CertsProd.zip`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/__init__.py` & `satcfdi-4.0.5/satcfdi/transform/__init__.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/catalog.py` & `satcfdi-4.0.5/satcfdi/transform/catalog.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/helpers.py` & `satcfdi-4.0.5/satcfdi/transform/helpers.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/objectify.py` & `satcfdi-4.0.5/satcfdi/transform/objectify.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_environment.py` & `satcfdi-4.0.5/satcfdi/transform/pdf_environment.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/CartaPorte.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/CartaPorte.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/Comprobante.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/Comprobante.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/Conceptos.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/Conceptos.html`

 * *Files 9% similar despite different names*

```diff
@@ -44,26 +44,26 @@
 						<th style="width: 20%;">Impuesto</th>
 						<th style="width: 20%;">Tasa o Cuota</th>
 						<th style="width: 20%;">Importe</th>
 					</tr>
 					{% if c.Impuestos.Traslados %}
 					{% for v in iterate(c.Impuestos.Traslados) %}
 					<tr>
-						<td>{% if loop.first %}+ <b>Translados</b>{% endif %}</td>
+						<td>{% if loop.first %}<b>+&nbsp;Translados</b>{% endif %}</td>
 						<td>{{ v.Base }}</td>
 						<td>{{ v.Impuesto | desc }}</td>
 						<td>{{ tasa_cuota( v.TipoFactor, v.TasaOCuota) }}</td>
 						<td>{{ v.Importe }}</td>
 					</tr>
 					{% endfor %}
 					{% endif %}
 					{% if c.Impuestos.Retenciones %}
 					{% for v in iterate(c.Impuestos.Retenciones) %}
 					<tr>
-						<td>{% if loop.first %}- <b>Retenciones</b>{% endif %}</td>
+						<td>{% if loop.first %}<b>-&nbsp;Retenciones</b>{% endif %}</td>
 						<td>{{ v.Base }}</td>
 						<td>{{ v.Impuesto | desc }}</td>
 						<td>{{ tasa_cuota( v.TipoFactor, v.TasaOCuota) }}</td>
 						<td>{{ v.Importe }}</td>
 					</tr>
 					{% endfor %}
 					<tr></tr>
@@ -92,29 +92,29 @@
 	{% endif %}
 	{% if c.Impuestos %}
 	{% if c.Impuestos.Traslados %}
 	{% for v in iterate(c.Impuestos.Traslados) %}
 	<tr class="r">
 		<td>
 			{% if loop.first %}
-			+ <b>Translados</b>
+			<b>+&nbsp;Translados</b>
 			{% endif %}
 		</td>
 		<td>{{ v.Impuesto | desc }}</td>
 		<td>{{ tasa_cuota( v.TipoFactor, v.TasaOCuota) }}</td>
 		<td>{{ v.Importe }}</td>
 	</tr>
 	{% endfor %}
 	{% endif %}
 	{% if c.Impuestos.Retenciones %}
 	{% for v in iterate(c.Impuestos.Retenciones) %}
 	<tr class="r">
 		<td>
 			{% if loop.first %}
-			- <b>Retenciones</b>
+			<b>-&nbsp;Retenciones</b>
 			{% endif %}
 		</td>
 		<td>{{ v.Impuesto | desc }}</td>
 		<td></td>
 		<td>{{ v.Importe }}</td>
 	</tr>
 	{% endfor %}
```

#### html2text {}

```diff
@@ -8,23 +8,37 @@
 'CuentaPredial',        {             {               {           {{ c.Importe
 'Parte',                c.ClaveUnidad c.ValorUnitario c.Descuento }}
 'instEducativas',       }}            }}              }}
 'ObjetoImp') }} {       {{ c.Unidad
 { complements           }}
 (c.ComplementoConcepto)
 }}
-                 Base         Impuesto        Tasa o Cuota     Importe
-{% if loop.first              {{ v.Impuesto | {{ tasa_cuota
-%}+ Translados{% {{ v.Base }} desc }}         ( v.TipoFactor,  {{ v.Importe }}
-endif %}                                      v.TasaOCuota) }}
-{% if loop.first              {{ v.Impuesto | {{ tasa_cuota
-%}- Retenciones  {{ v.Base }} desc }}         ( v.TipoFactor,  {{ v.Importe }}
-{% endif %}                                   v.TasaOCuota) }}
-Subtotal                                                     {{ c.SubTotal }}
-Descuento                                                    {{ c.Descuento }}
-{% if loop.first %} +  {{ v.Impuesto | desc {{ tasa_cuota
-Translados {% endif %} }}                   ( v.TipoFactor,  {{ v.Importe }}
-                                            v.TasaOCuota) }}
-{% if loop.first %} -  {{ v.Impuesto | desc
-Retenciones {% endif   }}                                    {{ v.Importe }}
-%}
-Total                                                        {{ c.Total }}
+                                          Base   Impuesto   Tasa o Cuota  Importe
+                                          {      {          {{ tasa_cuota {
+{% if loop.first %}+ Translados{% endif  {      {          (             {
+%}                                        v.Base v.Impuesto v.TipoFactor, v.Importe
+                                          }}     | desc }}  v.TasaOCuota) }}
+                                                            }}
+                                          {      {          {{ tasa_cuota {
+{% if loop.first %}- Retenciones{% endif {      {          (             {
+%}                                        v.Base v.Impuesto v.TipoFactor, v.Importe
+                                          }}     | desc }}  v.TasaOCuota) }}
+                                                            }}
+                                                                     {
+Subtotal                                                             {
+                                                                     c.SubTotal
+                                                                     }}
+                                                                     {
+Descuento                                                            {
+                                                                     c.Descuento
+                                                                     }}
+                                            {          {{ tasa_cuota
+{% if loop.first %} + Translados {% endif  {          (             {
+%}                                          v.Impuesto v.TipoFactor, { v.Importe
+                                            | desc }}  v.TasaOCuota) }}
+                                                       }}
+                                            {                        {
+{% if loop.first %} - Retenciones {% endif {                        { v.Importe
+%}                                          v.Impuesto               }}
+                                            | desc }}
+Total                                                                {{ c.Total
+                                                                     }}
```

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/ConsumoDeCombustibles.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/ConsumoDeCombustibles.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/Nomina.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/Nomina.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/Pagos.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/Pagos.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/Retenciones.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/Retenciones.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/TimbreFiscalDigital.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/TimbreFiscalDigital.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/ValesDeDespensa.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/ValesDeDespensa.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/_style.css` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/_style.css`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/pdf_templates/archivo.html` & `satcfdi-4.0.5/satcfdi/transform/pdf_templates/archivo.html`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.diverza.com/schema/xsd/Addenda_Diverza_v1.1.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.diverza.com/schema/xsd/Addenda_Diverza_v1.1.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/ari.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/ari.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/avi.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/avi.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/bli.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/bli.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/chv.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/chv.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/din.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/din.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/don.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/don.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fep.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fep.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fes.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/fes.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/inm.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/inm.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/jys.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/jys.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mjr.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mjr.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mpc.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/mpc.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/oba.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/oba.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd.bck` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr.xsd.bck`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr2.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/spr2.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tcv.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tcv.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tdr.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tdr.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tpp.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tpp.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tsc.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/tsc.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/veh.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.pld.hacienda.gob.mx/work/models/PLD/documentos/xsd/veh.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarCtas/AuxiliarCtas_1_1.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_1.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_1.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_2.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/AuxiliarFolios/AuxiliarFolios_1_2.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/PolizasPeriodo/PolizasPeriodo_1_1.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_1/SelloDigitalContElec/SelloDigitalContElec.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_2.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_2.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_3.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_3.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_2.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_2.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_3.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_3.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_2.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_2.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_3.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/BalanzaComprobacion/BalanzaComprobacion_1_3.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_2.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_2.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_3.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogoCuentas/CatalogoCuentas_1_3.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/CatalogosParaEsqContE/CatalogosParaEsqContE.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_2.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_2.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_3.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_3.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/ContabilidadE/1_3/SelloDigitalContElec/SelloDigitalContElec.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/ServiciosPlataformasTecnologicas10.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/catalogos/CatPlataformasTecnologicas.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/PlataformasTecnologicas10/catalogos/CatPlataformasTecnologicas.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/arrendamientoenfideicomiso/arrendamientoenfideicomiso.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/catalogos/catRetenciones.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/catalogos/catRetenciones.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/dividendos/dividendos.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/enajenaciondeacciones/enajenaciondeacciones.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/fideicomisonoempresarial/fideicomisonoempresarial.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereses/intereses.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/intereseshipotecarios/intereseshipotecarios.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/operacionesconderivados/operacionesconderivados.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/pagosaextranjeros/pagosaextranjeros.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro/planesderetiro.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/catalogos/CatPlanesderetiro.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/catalogos/CatPlanesderetiro.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/planesderetiro11/planesderetiro11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/premios/premios.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retenciones.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retenciones.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retencionpagov1.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/retencionpagov1.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/1/sectorfinanciero/sectorfinanciero.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retenciones.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retenciones.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retencionpagov2.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/retencionpago/2/retencionpagov2.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/utilerias.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/esquemas/utilerias.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/cadenaoriginal_2_0/utilerias.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/2/cadenaoriginal_2_0/utilerias.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_2/cadenaoriginal_3_2.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_2/cadenaoriginal_3_2.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_3/cadenaoriginal_3_3.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_3/cadenaoriginal_3_3.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cadenaoriginal_4_0/cadenaoriginal_4_0.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cadenaoriginal_4_0/cadenaoriginal_4_0.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior/ComercioExterior10.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/EstadoDeCuentaCombustible/ecc12.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/GastosHidrocarburos10/GastosHidrocarburos10.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/IngresosHidrocarburos10/IngresosHidrocarburos.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigital.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigital.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_0.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_0.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_1.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/cadenaoriginal_TFD_1_1.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/TuristaPasajeroExtranjero/TuristaPasajeroExtranjero.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/AcreditamientoIEPS10.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/acreditamiento/AcreditamientoIEPS10.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/arteantiguedades/obrasarteantiguedades.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte/catCartaPorte.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte/catCartaPorte.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/ComExt/catComExt.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/ComExt/catComExt.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Combustible/catCombustible.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Combustible/catCombustible.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Nomina/catNomina.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/Nomina/catNomina.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/hidrocarburos/catHidrocarburos.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/catalogos/hidrocarburos/catHidrocarburos.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/cfdiregistrofiscal/cfdiregistrofiscal.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodeCombustibles11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/consumodecombustibles/consumodecombustibles.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/detallista/detallista.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/divisas.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/divisas/divisas.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecb/ecb.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ecc/ecc.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/iedu/iedu.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine10.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ine/ine11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/pfic/pfic.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/psgecfd/psgecfd.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/renovacionysustitucionvehiculos/renovacionysustitucionvehiculos.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/servicioparcialconstruccion/servicioparcialconstruccion.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/spei/spei.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/terceros/terceros11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/vehiculousado/vehiculousado.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/cfd/ventavehiculos/ventavehiculos11.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/TimbreFiscalDigital.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/TimbreFiscalDigital.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/cadenaoriginal_TFD_1_0.xslt` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.sat.gob.mx/sitio_internet/timbrefiscaldigital/cadenaoriginal_TFD_1_0.xslt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas/www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd` & `satcfdi-4.0.5/satcfdi/transform/schemas/www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/schemas.py` & `satcfdi-4.0.5/satcfdi/transform/schemas.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/xmlify.py` & `satcfdi-4.0.5/satcfdi/transform/xmlify.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/transform/xslt.py` & `satcfdi-4.0.5/satcfdi/transform/xslt.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/xelement.py` & `satcfdi-4.0.5/satcfdi/xelement.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi/zip.py` & `satcfdi-4.0.5/satcfdi/zip.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/satcfdi.egg-info/PKG-INFO` & `satcfdi-4.0.5/satcfdi.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: satcfdi
-Version: 4.0.4
+Version: 4.0.5
 Summary: The best open-source python library to generate and process SAT's CFDI
 Home-page: https://github.com/SAT-CFDI/python-satcfdi
 Author: satcfdi@outlook.com
 Author-email: satcfdi@outlook.com
 License: MIT License
 Project-URL: Documentation, https://satcfdi.readthedocs.io
 Project-URL: Source, https://github.com/SAT-CFDI/python-satcfdi
```

### Comparing `satcfdi-4.0.4/satcfdi.egg-info/SOURCES.txt` & `satcfdi-4.0.5/satcfdi.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/setup.py` & `satcfdi-4.0.5/setup.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_accounting.py` & `satcfdi-4.0.5/tests/test_accounting.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_api_banxico.py` & `satcfdi-4.0.5/tests/test_api_banxico.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_certifica.py` & `satcfdi-4.0.5/tests/test_certifica.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_cfdi.py` & `satcfdi-4.0.5/tests/test_cfdi.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_create.py` & `satcfdi-4.0.5/tests/test_create.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_create_addenda.py` & `satcfdi-4.0.5/tests/test_create_addenda.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_create_cancelacion.py` & `satcfdi-4.0.5/tests/test_create_cancelacion.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_create_cfdi33.py` & `satcfdi-4.0.5/tests/test_create_cfdi33.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_create_cfdi40.py` & `satcfdi-4.0.5/tests/test_create_cfdi40.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_create_cfdi40_raw.py` & `satcfdi-4.0.5/tests/test_create_cfdi40_raw.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_create_pld.py` & `satcfdi-4.0.5/tests/test_create_pld.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_csf.py` & `satcfdi-4.0.5/tests/test_csf.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_custom_template.py` & `satcfdi-4.0.5/tests/test_custom_template.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_diot.py` & `satcfdi-4.0.5/tests/test_diot.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_models.py` & `satcfdi-4.0.5/tests/test_models.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_pac_comerciodigital.py` & `satcfdi-4.0.5/tests/test_pac_comerciodigital.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_pac_diverza.py` & `satcfdi-4.0.5/tests/test_pac_diverza.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_pac_mysuite.py` & `satcfdi-4.0.5/tests/test_pac_mysuite.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_pac_prodigia.py` & `satcfdi-4.0.5/tests/test_pac_prodigia.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_pac_sat.py` & `satcfdi-4.0.5/tests/test_pac_sat.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_pac_swsapien.py` & `satcfdi-4.0.5/tests/test_pac_swsapien.py`

 * *Files identical despite different names*

### Comparing `satcfdi-4.0.4/tests/test_portal.py` & `satcfdi-4.0.5/tests/test_portal.py`

 * *Files identical despite different names*

