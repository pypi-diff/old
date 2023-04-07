# Comparing `tmp/DLMS_SPODES-0.8.3.tar.gz` & `tmp/DLMS_SPODES-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "DLMS_SPODES-0.8.3.tar", last modified: Fri Mar  3 11:26:43 2023, max compression
+gzip compressed data, was "DLMS_SPODES-0.9.0.tar", last modified: Mon Mar  6 08:39:06 2023, max compression
```

## Comparing `DLMS_SPODES-0.8.3.tar` & `DLMS_SPODES-0.9.0.tar`

### file list

```diff
@@ -1,122 +1,124 @@
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.283578 DLMS_SPODES-0.8.3/
--rw-rw-rw-   0        0        0      640 2023-03-03 11:26:43.283578 DLMS_SPODES-0.8.3/PKG-INFO
--rw-rw-rw-   0        0        0      187 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/README.md
--rw-rw-rw-   0        0        0      421 2023-03-03 11:25:54.000000 DLMS_SPODES-0.8.3/pyproject.toml
--rw-rw-rw-   0        0        0      137 2023-03-03 11:26:43.287576 DLMS_SPODES-0.8.3/setup.cfg
--rw-rw-rw-   0        0        0      850 2023-02-15 13:05:52.000000 DLMS_SPODES-0.8.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:42.724496 DLMS_SPODES-0.8.3/src/
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:42.778573 DLMS_SPODES-0.8.3/src/DLMS_SPODES/
--rw-rw-rw-   0        0        0     3079 2023-02-16 06:47:26.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/ITE_exceptions.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:42.922306 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:42.979304 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/
--rw-rw-rw-   0        0        0       98 2023-02-16 06:07:54.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/__init__.py
--rw-rw-rw-   0        0        0      261 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/actors.py
--rw-rw-rw-   0        0        0     4538 2023-02-16 10:45:24.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/attr_names.py
--rw-rw-rw-   0        0        0      618 2023-02-16 10:45:24.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/cdt.py
--rw-rw-rw-   0        0        0      931 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/class_names.py
--rw-rw-rw-   0        0        0    11425 2023-02-16 09:51:18.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/enum_names.py
--rw-rw-rw-   0        0        0      272 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/errors.py
--rw-rw-rw-   0        0        0    19828 2023-02-21 05:23:31.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/events.py
--rw-rw-rw-   0        0        0     1294 2023-02-16 10:45:24.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/meth.py
--rw-rw-rw-   0        0        0    20338 2023-03-03 06:47:39.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/relation_to_obis_names.py
--rw-rw-rw-   0        0        0     5260 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/se.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.053337 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/
--rw-rw-rw-   0        0        0       98 2023-02-16 06:07:54.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/__init__.py
--rw-rw-rw-   0        0        0      446 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/actors.py
--rw-rw-rw-   0        0        0     6957 2023-02-16 10:45:24.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/attr_names.py
--rw-rw-rw-   0        0        0     1434 2023-02-16 10:45:24.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/cdt.py
--rw-rw-rw-   0        0        0     1460 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/class_names.py
--rw-rw-rw-   0        0        0    15887 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/enum_names.py
--rw-rw-rw-   0        0        0      482 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/errors.py
--rw-rw-rw-   0        0        0    30646 2023-02-21 05:23:31.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/events.py
--rw-rw-rw-   0        0        0     2085 2023-02-16 10:45:25.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/meth.py
--rw-rw-rw-   0        0        0    31549 2023-03-03 06:47:39.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/relation_to_obis_names.py
--rw-rw-rw-   0        0        0     7799 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/se.py
--rw-rw-rw-   0        0        0        0 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/__init__.py
--rw-rw-rw-   0        0        0      313 2023-02-20 08:17:07.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/__init__.py
--rw-rw-rw-   0        0        0     2288 2023-03-03 05:19:24.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/client.py
--rw-rw-rw-   0        0        0     7817 2023-02-17 12:41:52.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/configure.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.175400 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/
--rw-rw-rw-   0        0        0      515 2023-02-16 06:33:15.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/__class_init__.py
--rw-rw-rw-   0        0        0       83 2023-03-03 09:10:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/__init__.py
--rw-rw-rw-   0        0        0    21427 2023-02-17 11:00:36.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/activity_calendar.py
--rw-rw-rw-   0        0        0     3759 2023-02-17 11:00:54.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/arbitrator.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.187401 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/
--rw-rw-rw-   0        0        0        0 2023-02-17 08:14:19.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/__init__.py
--rw-rw-rw-   0        0        0    34856 2023-03-03 09:26:19.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver0.py
--rw-rw-rw-   0        0        0     6649 2023-02-16 07:28:21.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver1.py
--rw-rw-rw-   0        0        0     1195 2023-02-16 07:29:03.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver2.py
--rw-rw-rw-   0        0        0      328 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/attr_indexes.py
--rw-rw-rw-   0        0        0     2177 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/class_id.py
--rw-rw-rw-   0        0        0     1871 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/client_setup.py
--rw-rw-rw-   0        0        0     7561 2023-02-17 11:01:56.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/clock.py
--rw-rw-rw-   0        0        0    58425 2023-03-03 11:25:41.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/collection.py
--rw-rw-rw-   0        0        0    11873 2023-02-21 06:06:28.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/cosem_interface_class.py
--rw-rw-rw-   0        0        0      772 2023-02-16 07:33:10.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/data.py
--rw-rw-rw-   0        0        0     6700 2023-02-17 11:02:07.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/disconnect_control.py
--rw-rw-rw-   0        0        0     4578 2023-02-20 08:11:52.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/events.py
--rw-rw-rw-   0        0        0     1168 2023-02-16 07:37:00.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/extended_register.py
--rw-rw-rw-   0        0        0     2517 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/gprs_modem_setup.py
--rw-rw-rw-   0        0        0     4743 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/gsm_diagnostic.py
--rw-rw-rw-   0        0        0     4970 2023-02-17 11:02:29.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/iec_hdlc_setup.py
--rw-rw-rw-   0        0        0      461 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/iec_local_port_setup.py
--rw-rw-rw-   0        0        0     9626 2023-02-17 11:02:38.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/image_transfer.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.192397 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/implementations/
--rw-rw-rw-   0        0        0       20 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/implementations/__init__.py
--rw-rw-rw-   0        0        0     4085 2023-02-22 10:18:16.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/implementations/data.py
--rw-rw-rw-   0        0        0     2278 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/ipv4_setup.py
--rw-rw-rw-   0        0        0     7922 2023-02-17 11:03:52.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/limiter.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.199398 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/
--rw-rw-rw-   0        0        0        0 2023-02-17 08:12:28.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/__init__.py
--rw-rw-rw-   0        0        0     3535 2023-02-17 11:02:52.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver0.py
--rw-rw-rw-   0        0        0     2261 2023-02-16 07:39:59.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver1.py
--rw-rw-rw-   0        0        0      157 2023-02-25 10:53:40.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/obis.py
--rw-rw-rw-   0        0        0    21051 2023-02-17 11:04:05.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/profile_generic.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.205402 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/push_setup/
--rw-rw-rw-   0        0        0        0 2023-02-17 08:12:45.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/push_setup/__init__.py
--rw-rw-rw-   0        0        0    13427 2023-02-17 12:02:10.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/push_setup/ver2.py
--rw-rw-rw-   0        0        0     3155 2023-02-17 11:02:18.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/register.py
--rw-rw-rw-   0        0        0     2702 2023-02-17 11:04:15.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/register_monitor.py
--rw-rw-rw-   0        0        0    13629 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/schedule.py
--rw-rw-rw-   0        0        0     5131 2023-02-16 07:52:43.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/script_table.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.212400 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/security_setup/
--rw-rw-rw-   0        0        0        0 2023-02-17 08:12:53.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/security_setup/__init__.py
--rw-rw-rw-   0        0        0     4327 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver0.py
--rw-rw-rw-   0        0        0     9350 2023-02-16 07:52:25.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver1.py
--rw-rw-rw-   0        0        0     2255 2023-02-17 11:04:24.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/single_action_schedule.py
--rw-rw-rw-   0        0        0     5273 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/special_days_table.py
--rw-rw-rw-   0        0        0     2271 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/tcp_udp_setup.py
--rw-rw-rw-   0        0        0     2408 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_pdu.py
--rw-rw-rw-   0        0        0     6224 2023-02-21 06:22:15.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/enums.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.226400 DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/
--rw-rw-rw-   0        0        0        0 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/__init__.py
--rw-rw-rw-   0        0        0     4522 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/control_field.py
--rw-rw-rw-   0        0        0    33460 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/frame.py
--rw-rw-rw-   0        0        0     3132 2023-02-17 11:50:11.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/snrm.py
--rw-rw-rw-   0        0        0     2147 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/sub_layer.py
--rw-rw-rw-   0        0        0     2276 2023-03-03 06:27:12.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/pdu_enums.py
--rw-rw-rw-   0        0        0    35176 2023-03-03 06:44:48.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/relation_to_OBIS.py
--rw-rw-rw-   0        0        0      477 2023-02-16 10:46:23.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/settings.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.251951 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/
--rw-rw-rw-   0        0        0      118 2023-02-17 10:58:16.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/__init__.py
--rw-rw-rw-   0        0        0      324 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/arrays.py
--rw-rw-rw-   0        0        0     5745 2023-02-22 09:29:53.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/choices.py
--rw-rw-rw-   0        0        0   110323 2023-02-16 06:06:43.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/common_data_types.py
--rw-rw-rw-   0        0        0     6511 2023-02-22 08:38:32.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/cosem_service_types.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.265485 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/
--rw-rw-rw-   0        0        0        0 2023-02-17 10:47:36.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/__init__.py
--rw-rw-rw-   0        0        0      478 2023-02-16 07:27:13.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/arrays.py
--rw-rw-rw-   0        0        0     2692 2023-02-16 07:30:36.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/emuns.py
--rw-rw-rw-   0        0        0      337 2023-02-16 06:33:58.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/integers.py
--rw-rw-rw-   0        0        0      325 2023-02-16 07:26:51.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/long_unsigneds.py
--rw-rw-rw-   0        0        0     4450 2023-02-16 06:35:19.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/structs.py
--rw-rw-rw-   0        0        0    25241 2023-02-25 06:45:26.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/useful_types.py
--rw-rw-rw-   0        0        0     3316 2023-02-15 13:00:09.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES/version.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:42.918305 DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/
--rw-rw-rw-   0        0        0      640 2023-03-03 11:26:42.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     4713 2023-03-03 11:26:42.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-03 11:26:42.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       58 2023-03-03 11:26:42.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       12 2023-03-03 11:26:42.000000 DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-03-03 11:26:43.281576 DLMS_SPODES-0.8.3/test/
--rw-rw-rw-   0        0        0     6405 2023-03-03 09:16:00.000000 DLMS_SPODES-0.8.3/test/test_cdt.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.778349 DLMS_SPODES-0.9.0/
+-rw-rw-rw-   0        0        0      640 2023-03-06 08:39:06.778349 DLMS_SPODES-0.9.0/PKG-INFO
+-rw-rw-rw-   0        0        0      187 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/README.md
+-rw-rw-rw-   0        0        0      421 2023-03-06 08:35:21.000000 DLMS_SPODES-0.9.0/pyproject.toml
+-rw-rw-rw-   0        0        0      137 2023-03-06 08:39:06.778349 DLMS_SPODES-0.9.0/setup.cfg
+-rw-rw-rw-   0        0        0      850 2023-02-15 13:05:52.000000 DLMS_SPODES-0.9.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.519083 DLMS_SPODES-0.9.0/src/
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.592969 DLMS_SPODES-0.9.0/src/DLMS_SPODES/
+-rw-rw-rw-   0        0        0     3079 2023-02-16 06:47:26.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/ITE_exceptions.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.592969 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.624189 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/
+-rw-rw-rw-   0        0        0       98 2023-02-16 06:07:54.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/__init__.py
+-rw-rw-rw-   0        0        0      261 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/actors.py
+-rw-rw-rw-   0        0        0     4538 2023-02-16 10:45:24.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/attr_names.py
+-rw-rw-rw-   0        0        0      618 2023-02-16 10:45:24.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/cdt.py
+-rw-rw-rw-   0        0        0      931 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/class_names.py
+-rw-rw-rw-   0        0        0    11568 2023-03-06 07:57:12.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/enum_names.py
+-rw-rw-rw-   0        0        0      272 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/errors.py
+-rw-rw-rw-   0        0        0    19828 2023-02-21 05:23:31.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/events.py
+-rw-rw-rw-   0        0        0     1294 2023-02-16 10:45:24.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/meth.py
+-rw-rw-rw-   0        0        0    20338 2023-03-03 06:47:39.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/relation_to_obis_names.py
+-rw-rw-rw-   0        0        0     5260 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/se.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.646823 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/
+-rw-rw-rw-   0        0        0       98 2023-02-16 06:07:54.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/__init__.py
+-rw-rw-rw-   0        0        0      446 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/actors.py
+-rw-rw-rw-   0        0        0     6957 2023-02-16 10:45:24.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/attr_names.py
+-rw-rw-rw-   0        0        0     1434 2023-02-16 10:45:24.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/cdt.py
+-rw-rw-rw-   0        0        0     1460 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/class_names.py
+-rw-rw-rw-   0        0        0    16072 2023-03-06 07:57:12.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/enum_names.py
+-rw-rw-rw-   0        0        0      482 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/errors.py
+-rw-rw-rw-   0        0        0    30646 2023-02-21 05:23:31.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/events.py
+-rw-rw-rw-   0        0        0     2085 2023-02-16 10:45:25.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/meth.py
+-rw-rw-rw-   0        0        0    31549 2023-03-03 06:47:39.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/relation_to_obis_names.py
+-rw-rw-rw-   0        0        0     7799 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/se.py
+-rw-rw-rw-   0        0        0        0 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/__init__.py
+-rw-rw-rw-   0        0        0      313 2023-02-20 08:17:07.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/__init__.py
+-rw-rw-rw-   0        0        0     2288 2023-03-03 05:19:24.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/client.py
+-rw-rw-rw-   0        0        0     7817 2023-02-17 12:41:52.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/configure.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.709334 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/
+-rw-rw-rw-   0        0        0      515 2023-02-16 06:33:15.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/__class_init__.py
+-rw-rw-rw-   0        0        0       83 2023-03-03 09:10:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/__init__.py
+-rw-rw-rw-   0        0        0    21427 2023-02-17 11:00:36.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/activity_calendar.py
+-rw-rw-rw-   0        0        0     3759 2023-02-17 11:00:54.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/arbitrator.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.724959 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/
+-rw-rw-rw-   0        0        0        0 2023-02-17 08:14:19.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/__init__.py
+-rw-rw-rw-   0        0        0    34856 2023-03-03 09:26:19.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver0.py
+-rw-rw-rw-   0        0        0     6649 2023-02-16 07:28:21.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver1.py
+-rw-rw-rw-   0        0        0     1195 2023-02-16 07:29:03.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver2.py
+-rw-rw-rw-   0        0        0      328 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/attr_indexes.py
+-rw-rw-rw-   0        0        0     2177 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/class_id.py
+-rw-rw-rw-   0        0        0     1871 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/client_setup.py
+-rw-rw-rw-   0        0        0     7561 2023-02-17 11:01:56.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/clock.py
+-rw-rw-rw-   0        0        0    58425 2023-03-03 11:25:41.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/collection.py
+-rw-rw-rw-   0        0        0    11873 2023-02-21 06:06:28.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/cosem_interface_class.py
+-rw-rw-rw-   0        0        0      772 2023-02-16 07:33:10.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/data.py
+-rw-rw-rw-   0        0        0     6700 2023-02-17 11:02:07.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/disconnect_control.py
+-rw-rw-rw-   0        0        0     4578 2023-02-20 08:11:52.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/events.py
+-rw-rw-rw-   0        0        0     1168 2023-02-16 07:37:00.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/extended_register.py
+-rw-rw-rw-   0        0        0     2517 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/gprs_modem_setup.py
+-rw-rw-rw-   0        0        0     5168 2023-03-06 08:30:43.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/gsm_diagnostic.py
+-rw-rw-rw-   0        0        0     4970 2023-02-17 11:02:29.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/iec_hdlc_setup.py
+-rw-rw-rw-   0        0        0      461 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/iec_local_port_setup.py
+-rw-rw-rw-   0        0        0     9626 2023-02-17 11:02:38.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/image_transfer.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.724959 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/implementations/
+-rw-rw-rw-   0        0        0       20 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/implementations/__init__.py
+-rw-rw-rw-   0        0        0     4085 2023-02-22 10:18:16.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/implementations/data.py
+-rw-rw-rw-   0        0        0     2278 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/ipv4_setup.py
+-rw-rw-rw-   0        0        0     7922 2023-02-17 11:03:52.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/limiter.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.740582 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/
+-rw-rw-rw-   0        0        0        0 2023-02-17 08:12:28.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/__init__.py
+-rw-rw-rw-   0        0        0     3535 2023-02-17 11:02:52.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver0.py
+-rw-rw-rw-   0        0        0     2261 2023-02-16 07:39:59.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver1.py
+-rw-rw-rw-   0        0        0      157 2023-02-25 10:53:40.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/obis.py
+-rw-rw-rw-   0        0        0    21840 2023-03-06 07:07:29.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/profile_generic.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.740582 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/push_setup/
+-rw-rw-rw-   0        0        0        0 2023-02-17 08:12:45.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/push_setup/__init__.py
+-rw-rw-rw-   0        0        0    13427 2023-02-17 12:02:10.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/push_setup/ver2.py
+-rw-rw-rw-   0        0        0     3155 2023-02-17 11:02:18.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/register.py
+-rw-rw-rw-   0        0        0     2702 2023-02-17 11:04:15.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/register_monitor.py
+-rw-rw-rw-   0        0        0    13629 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/schedule.py
+-rw-rw-rw-   0        0        0     5131 2023-02-16 07:52:43.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/script_table.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.747091 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/security_setup/
+-rw-rw-rw-   0        0        0        0 2023-02-17 08:12:53.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/security_setup/__init__.py
+-rw-rw-rw-   0        0        0     4327 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver0.py
+-rw-rw-rw-   0        0        0     9350 2023-02-16 07:52:25.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver1.py
+-rw-rw-rw-   0        0        0     2255 2023-02-17 11:04:24.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/single_action_schedule.py
+-rw-rw-rw-   0        0        0     5273 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/special_days_table.py
+-rw-rw-rw-   0        0        0     2271 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/tcp_udp_setup.py
+-rw-rw-rw-   0        0        0     2408 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_pdu.py
+-rw-rw-rw-   0        0        0     6224 2023-02-21 06:22:15.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/enums.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.747091 DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/
+-rw-rw-rw-   0        0        0        0 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/__init__.py
+-rw-rw-rw-   0        0        0     4522 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/control_field.py
+-rw-rw-rw-   0        0        0    33460 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/frame.py
+-rw-rw-rw-   0        0        0     3132 2023-02-17 11:50:11.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/snrm.py
+-rw-rw-rw-   0        0        0     2147 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/sub_layer.py
+-rw-rw-rw-   0        0        0     2276 2023-03-03 06:27:12.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/pdu_enums.py
+-rw-rw-rw-   0        0        0    35176 2023-03-03 06:44:48.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/relation_to_OBIS.py
+-rw-rw-rw-   0        0        0      477 2023-02-16 10:46:23.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/settings.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.762724 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/
+-rw-rw-rw-   0        0        0      118 2023-02-17 10:58:16.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/__init__.py
+-rw-rw-rw-   0        0        0      324 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/arrays.py
+-rw-rw-rw-   0        0        0     5745 2023-02-22 09:29:53.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/choices.py
+-rw-rw-rw-   0        0        0   110323 2023-02-16 06:06:43.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/common_data_types.py
+-rw-rw-rw-   0        0        0     6511 2023-02-22 08:38:32.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/cosem_service_types.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.778349 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/
+-rw-rw-rw-   0        0        0        0 2023-02-17 10:47:36.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/__init__.py
+-rw-rw-rw-   0        0        0      478 2023-02-16 07:27:13.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/arrays.py
+-rw-rw-rw-   0        0        0     2692 2023-02-16 07:30:36.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/emuns.py
+-rw-rw-rw-   0        0        0      337 2023-02-16 06:33:58.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/integers.py
+-rw-rw-rw-   0        0        0      325 2023-02-16 07:26:51.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/long_unsigneds.py
+-rw-rw-rw-   0        0        0     4450 2023-02-16 06:35:19.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/structs.py
+-rw-rw-rw-   0        0        0    25241 2023-02-25 06:45:26.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/useful_types.py
+-rw-rw-rw-   0        0        0     3316 2023-02-15 13:00:09.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES/version.py
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.592969 DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/
+-rw-rw-rw-   0        0        0      640 2023-03-06 08:39:06.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     4768 2023-03-06 08:39:06.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-06 08:39:06.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       58 2023-03-06 08:39:06.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       12 2023-03-06 08:39:06.000000 DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-06 08:39:06.778349 DLMS_SPODES-0.9.0/test/
+-rw-rw-rw-   0        0        0      466 2023-03-06 08:30:43.000000 DLMS_SPODES-0.9.0/test/test_GSMDiagnostic.py
+-rw-rw-rw-   0        0        0     2375 2023-03-06 08:04:57.000000 DLMS_SPODES-0.9.0/test/test_ProfileGeneric.py
+-rw-rw-rw-   0        0        0     6405 2023-03-03 09:16:00.000000 DLMS_SPODES-0.9.0/test/test_cdt.py
```

### Comparing `DLMS_SPODES-0.8.3/PKG-INFO` & `DLMS_SPODES-0.9.0/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DLMS_SPODES
-Version: 0.8.3
+Version: 0.9.0
 Summary: dlms-spodes
 Home-page: https://github.com/youserj/DlmsSPODES
 Author: Serj Kotilevski
 Author-email: Serj <youserj@outlook.com>
 Keywords: dlms,string,constant,values
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `DLMS_SPODES-0.8.3/setup.py` & `DLMS_SPODES-0.9.0/setup.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/ITE_exceptions.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/ITE_exceptions.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/attr_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/attr_names.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/cdt.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/cdt.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/class_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/class_names.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/enum_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/enum_names.py`

 * *Files 1% similar despite different names*

```diff
@@ -266,7 +266,12 @@
 CONFIRMED = "confirmed, retry on missing confirmation"
 MASTER_KEY = "master key"
 GLOB_UNI_ENCR_KEY = "global unicast encryption key"
 GLOB_BROAD_ENCR_KEY = "global broadcast encryption key"
 IDENTIFIED_KEY = "identified key"
 WRAPPED_KEY = "wrapped key"
 AGREED_KEY = "agreed key"
+
+# for GSM_diagnostic.cell_info
+OR_LESS = "or less"
+OR_GREATER = "or greater"
+NOT_KNOWN_OR_NOT_DETECTABLE = "not known or not detectable"
```

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/events.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/events.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/meth.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/meth.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/relation_to_obis_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/relation_to_obis_names.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/EN/se.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/EN/se.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/attr_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/attr_names.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/cdt.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/cdt.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/class_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/class_names.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/enum_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/enum_names.py`

 * *Files 0% similar despite different names*

```diff
@@ -265,8 +265,13 @@
 UNCONFIRMED_MISSING = "Неподтверждено, повторение пропущенного подтверждения протокола"
 CONFIRMED = "подтверждено, повторите пропущенное подтверждение"
 MASTER_KEY = "мастер ключ"
 GLOB_UNI_ENCR_KEY = "Глобальный ключ шифрования одноадресный"
 GLOB_BROAD_ENCR_KEY = "Глобальный ключ шифрования широковещательный"
 IDENTIFIED_KEY = "Идентификационный ключ"
 WRAPPED_KEY = "Обернутый ключ"
-AGREED_KEY = "Согласованный ключ"
+AGREED_KEY = "Согласованный ключ"
+
+# for GSM_diagnostic.cell_info
+OR_LESS = "или менее"
+OR_GREATER = "или более"
+NOT_KNOWN_OR_NOT_DETECTABLE = "не известно или не опознано"
```

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/events.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/events.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/meth.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/meth.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/relation_to_obis_names.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/relation_to_obis_names.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/Values/RU/se.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/Values/RU/se.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/client.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/client.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/configure.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/configure.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/__class_init__.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/__class_init__.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/activity_calendar.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/activity_calendar.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/arbitrator.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/arbitrator.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver0.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver0.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver1.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver1.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver2.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/association_ln/ver2.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/class_id.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/class_id.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/client_setup.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/client_setup.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/clock.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/clock.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/collection.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/collection.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/cosem_interface_class.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/cosem_interface_class.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/data.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/data.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/disconnect_control.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/disconnect_control.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/events.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/events.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/extended_register.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/extended_register.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/gprs_modem_setup.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/gprs_modem_setup.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/gsm_diagnostic.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/gsm_diagnostic.py`

 * *Files 5% similar despite different names*

```diff
@@ -23,40 +23,54 @@
     ELEMENTS = {b'\x00': en.INACTIVE,
                 b'\x01': en.GPRS,
                 b'\x02': en.EDGE,
                 b'\x03': en.UMTS,
                 b'\x04': en.HSDPA}
 
 
+class SignalQuality(cdt.Unsigned):
+    """for string report"""
+    @property
+    def report(self) -> str:
+        value = int(self)
+        if value == 0:
+            return F"–113 dBm {en.OR_LESS}(0)"
+        elif value == 1:
+            return F"–111 dBm(1)"
+        elif value < 31:
+            return F"{-109+(value-2)*2} dBm({value})"
+        elif value == 31:
+            return F"–51 dBm {en.OR_GREATER}(31)"
+        elif value == 99:
+            return F"{en.NOT_KNOWN_OR_NOT_DETECTABLE}"
+        else:
+            return F"wrong {value=}"
+
+
 class CellInfoType(cdt.Structure):
     """ Params of element """
-    values: tuple[cdt.LongUnsigned, cdt.LongUnsigned, cdt.Unsigned, cdt.Unsigned]
+    values: tuple[cdt.LongUnsigned, cdt.LongUnsigned, SignalQuality, cdt.Unsigned]
     ELEMENTS = (cdt.StructElement(cdt.se.CELL_ID, cdt.LongUnsigned),
                 cdt.StructElement(cdt.se.LOCATION_ID, cdt.LongUnsigned),
-                cdt.StructElement(cdt.se.SIGNAL_QUALITY, cdt.Unsigned),
+                cdt.StructElement(cdt.se.SIGNAL_QUALITY, SignalQuality),
                 cdt.StructElement(cdt.se.BER, cdt.Unsigned))
 
     @property
     def cell_ID(self) -> cdt.LongUnsigned:
         """Two-byte cell ID in hexadecimal format"""
         return self.values[0]
 
     @property
     def location_ID(self) -> cdt.LongUnsigned:
         """Two-byte location area code (LAC) in hexadecimal format"""
         return self.values[1]
 
     @property
-    def signal_quality(self) -> cdt.Unsigned:
-        """represents the signal quality:
-        0: -113 dBm or less,
-        1: -11q dBm,
-        2..30: -109...53 dBm,
-        31: -51 or greater,
-        99 not known or not detectable"""
+    def signal_quality(self) -> SignalQuality:
+        """represents the signal quality"""
         return self.values[2]
 
     @property
     def ber(self) -> cdt.Unsigned:
         """Bit error (BER) measurement in percent:
         (0...7) as RXQUAL_n values specified in ETSI GSM 05.08 8.2.4
         (99) not known or not detectable."""
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/iec_hdlc_setup.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/iec_hdlc_setup.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/image_transfer.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/image_transfer.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/implementations/data.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/implementations/data.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/ipv4_setup.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/ipv4_setup.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/limiter.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/limiter.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver0.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver0.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver1.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/modem_configuration/ver1.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/profile_generic.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/profile_generic.py`

 * *Files 7% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from .. import cosem_interface_classes
 from .register import Register
 from .clock import Clock
 from ..relation_to_OBIS import get_name
 from .. import ITE_exceptions as exc
 from .__class_init__ import *
 from ..types.implementations import integers, arrays, structs
-
+from ..types import cdt
 
 BUFFER = 2
 CAPTURE_OBJECTS = 3
 CAPTURE_PERIOD = 4
 SORT_METHOD = 5
 SORT_OBJECT = 6
 ENTRIES_IN_USE = 7
@@ -254,18 +254,30 @@
         for element_value in self.__buffer_capture_objects:
             element_value: structs.CaptureObjectDefinition
             # TODO HERE NEED FIX
             obj = self.collection.add_if_missing(class_id=ut.CosemClassId(element_value.class_id.contents),
                                                  version=None,
                                                  logical_name=element_value.logical_name)
             self.collection.raise_before(obj, self)
-            attr_index = element_value.attribute_index.decode()
+            attr_index = int(element_value.attribute_index)
+            data_index = int(element_value.data_index)
+            data_type: Type[cdt.CommonDataType] = obj.get_attr_data_type(attr_index)
+            if data_index == 0:
+                name = obj.get_attr_element(attr_index).NAME
+            elif issubclass(data_type, cdt.Structure):
+                if len(data_type.ELEMENTS) < data_index:
+                    raise ValueError(F"can't create buffer_struct_type for {self}, got {data_index=} in struct {data_type.__name__}, expected 1..{len(data_type.ELEMENTS)}")
+                else:
+                    name = data_type.ELEMENTS[data_index-1].NAME
+                    data_type: Type[cdt.CommonDataType] = data_type.ELEMENTS[data_index-1].TYPE
+            else:
+                raise ValueError(F"for {data_type.__name__} got {data_index=}, expected only 0")
             # TODO: make func(obj, index) -> str: return new Name for struct element
-            buffer_elements.append(cdt.StructElement(NAME=F'{get_name(obj.logical_name)}:{obj.get_attr_element(attr_index).NAME}',
-                                                     TYPE=obj.get_attr_data_type(attr_index)))
+            buffer_elements.append(cdt.StructElement(NAME=F'{get_name(obj.logical_name)}:{name}',
+                                                     TYPE=data_type))
 
         class Entry(cdt.Structure):
             """ The number and the order of the elements of the structure holding the entries is the same as in the definition of the capture_objects.
                 The buffer is filled by auto captures or by subsequent calls of the method (capture). The sequence of the entries within the array is ordered
                 according to the sort method specified. Default: The buffer is empty after reset.
                 REMARK 1 Reading the entire buffer delivers only those entries, which are “in use”.
                 REMARK 2 The value of a captured object may be replaced by “null-data” if it can be unambiguously recovered from the previous value
```

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/push_setup/ver2.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/push_setup/ver2.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/register.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/register.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/register_monitor.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/register_monitor.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/schedule.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/schedule.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/script_table.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/script_table.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver0.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver0.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver1.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/security_setup/ver1.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/single_action_schedule.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/single_action_schedule.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/special_days_table.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/special_days_table.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_interface_classes/tcp_udp_setup.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_interface_classes/tcp_udp_setup.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/cosem_pdu.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/cosem_pdu.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/enums.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/enums.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/control_field.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/control_field.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/frame.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/frame.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/snrm.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/snrm.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/hdlc/sub_layer.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/hdlc/sub_layer.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/pdu_enums.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/pdu_enums.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/relation_to_OBIS.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/relation_to_OBIS.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/choices.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/choices.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/common_data_types.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/common_data_types.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/cosem_service_types.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/cosem_service_types.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/emuns.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/emuns.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/implementations/structs.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/implementations/structs.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/types/useful_types.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/types/useful_types.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES/version.py` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES/version.py`

 * *Files identical despite different names*

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/PKG-INFO` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DLMS-SPODES
-Version: 0.8.3
+Version: 0.9.0
 Summary: dlms-spodes
 Home-page: https://github.com/youserj/DlmsSPODES
 Author: Serj Kotilevski
 Author-email: Serj <youserj@outlook.com>
 Keywords: dlms,string,constant,values
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `DLMS_SPODES-0.8.3/src/DLMS_SPODES.egg-info/SOURCES.txt` & `DLMS_SPODES-0.9.0/src/DLMS_SPODES.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -97,8 +97,10 @@
 src/DLMS_SPODES/types/useful_types.py
 src/DLMS_SPODES/types/implementations/__init__.py
 src/DLMS_SPODES/types/implementations/arrays.py
 src/DLMS_SPODES/types/implementations/emuns.py
 src/DLMS_SPODES/types/implementations/integers.py
 src/DLMS_SPODES/types/implementations/long_unsigneds.py
 src/DLMS_SPODES/types/implementations/structs.py
+test/test_GSMDiagnostic.py
+test/test_ProfileGeneric.py
 test/test_cdt.py
```

### Comparing `DLMS_SPODES-0.8.3/test/test_cdt.py` & `DLMS_SPODES-0.9.0/test/test_cdt.py`

 * *Files identical despite different names*

