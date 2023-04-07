# Comparing `tmp/wodoo-0.3.96.tar.gz` & `tmp/wodoo-0.3.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wodoo-0.3.96.tar", last modified: Mon Jan 23 10:17:07 2023, max compression
+gzip compressed data, was "wodoo-0.3.99.tar", last modified: Mon Jan 30 10:10:18 2023, max compression
```

## Comparing `wodoo-0.3.96.tar` & `wodoo-0.3.99.tar`

### file list

```diff
@@ -1,118 +1,118 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.614851 wodoo-0.3.96/
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-01-23 10:16:50.000000 wodoo-0.3.96/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-01-23 10:17:07.614851 wodoo-0.3.96/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4692 2023-01-23 10:16:50.000000 wodoo-0.3.96/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-01-23 10:17:07.614851 wodoo-0.3.96/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2156 2023-01-23 10:16:50.000000 wodoo-0.3.96/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/
--rw-r--r--   0 runner    (1001) docker     (123)     1265 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3372 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     8126 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/click_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      624 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/click_global_commands.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/config/
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/config/cicd_network_for_project.yml
--rw-r--r--   0 runner    (1001) docker     (123)       53 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/config/default_network
--rw-r--r--   0 runner    (1001) docker     (123)      121 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/config/template_onlyloop.yml
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/config/template_withports.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2600 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/consts.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     7012 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/daddy_cleanup.py
--rw-r--r--   0 runner    (1001) docker     (123)     1087 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/defaults
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.602851 wodoo-0.3.96/wodoo/extra_install/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.602851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/
--rw-r--r--   0 runner    (1001) docker     (123)      428 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/Dockerfile
--rw-r--r--   0 runner    (1001) docker     (123)      939 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/README.txt
--rwxr-xr-x   0 runner    (1001) docker     (123)       81 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/debug.sh
--rw-r--r--   0 runner    (1001) docker     (123)     1217 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/docker-compose.yml
--rw-r--r--   0 runner    (1001) docker     (123)      182 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/entrypoint.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)       72 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/interactive.sh
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/
--rw-r--r--   0 runner    (1001) docker     (123)      158 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/config
--rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/id_rsa
--rw-r--r--   0 runner    (1001) docker     (123)      400 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/id_rsa.pub
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/
--rw-r--r--   0 runner    (1001) docker     (123)      537 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/ANPASSUNGEN.txt
--rw-r--r--   0 runner    (1001) docker     (123)     9680 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/Dockerfile
--rw-r--r--   0 runner    (1001) docker     (123)      822 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/docker-compose.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/
--rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/11-setup-config-files
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/config/
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/config/ari_additional_custom.conf.appendix
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/config/manager_custom.conf.appendix
--rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/default_extensions.csv
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/asterisk/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/asterisk/freepbx_chown.conf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-finish.d/
--rwxr-xr-x   0 runner    (1001) docker     (123)      349 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-finish.d/10-freepbx
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-init.d/
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-init.d/10-start
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/
--rw-r--r--   0 runner    (1001) docker     (123)      301 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/apache2
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/asterisk
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/fail2ban
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/fop
--rw-r--r--   0 runner    (1001) docker     (123)      202 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/odbc.ini
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/odbcinst.ini
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/08-ssh
--rwxr-xr-x   0 runner    (1001) docker     (123)      567 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/09-mariadb
--rwxr-xr-x   0 runner    (1001) docker     (123)    17011 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/10-freepbx
--rwxr-xr-x   0 runner    (1001) docker     (123)      475 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/13-extra-modules
--rw-r--r--   0 runner    (1001) docker     (123)      679 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/14-mysql-settings
--rw-r--r--   0 runner    (1001) docker     (123)      157 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/15-permissions
--rw-r--r--   0 runner    (1001) docker     (123)      383 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/16-soundlang
--rw-r--r--   0 runner    (1001) docker     (123)      348 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/20-load-default-extensions
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.602851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/root/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/root/.ssh/
--rw-r--r--   0 runner    (1001) docker     (123)      391 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/root/.ssh/authorized_keys
--rwxr-xr-x   0 runner    (1001) docker     (123)      423 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/run_freepbx.sh
--rw-r--r--   0 runner    (1001) docker     (123)    21607 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_backup.py
--rw-r--r--   0 runner    (1001) docker     (123)     2029 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_clickhelpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    29246 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_composer.py
--rw-r--r--   0 runner    (1001) docker     (123)    12987 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_control.py
--rw-r--r--   0 runner    (1001) docker     (123)     9713 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_control_with_docker.py
--rw-r--r--   0 runner    (1001) docker     (123)    15508 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_db.py
--rw-r--r--   0 runner    (1001) docker     (123)     4378 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_db_snapshots.py
--rw-r--r--   0 runner    (1001) docker     (123)     6049 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_db_snapshots_docker_btrfs.py
--rw-r--r--   0 runner    (1001) docker     (123)    10185 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_db_snapshots_docker_zfs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1735 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_db_snapshots_plain_postgres.py
--rw-r--r--   0 runner    (1001) docker     (123)     4937 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_docker_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     1112 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_lang.py
--rw-r--r--   0 runner    (1001) docker     (123)    47957 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_module.py
--rw-r--r--   0 runner    (1001) docker     (123)     2317 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_setup.py
--rw-r--r--   0 runner    (1001) docker     (123)    15669 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_src.py
--rw-r--r--   0 runner    (1001) docker     (123)     1630 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_talk.py
--rw-r--r--   0 runner    (1001) docker     (123)     5740 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/lib_turnintodev.py
--rw-r--r--   0 runner    (1001) docker     (123)    51388 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/module_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)     4554 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/myconfigparser.py
--rw-r--r--   0 runner    (1001) docker     (123)     6400 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/odoo_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    25337 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/odoo_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      320 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/pudb.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      347 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)     7418 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/robo_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     3942 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.614851 wodoo-0.3.96/wodoo/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/tests/MANIFEST
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/tests/gimera.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.614851 wodoo-0.3.96/wodoo/tests/module_respartner_dummyfield1/
--rw-r--r--   0 runner    (1001) docker     (123)      347 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/tests/module_respartner_dummyfield1/partnerview.xml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.614851 wodoo-0.3.96/wodoo/tests/module_respartner_dummyfield2/
--rw-r--r--   0 runner    (1001) docker     (123)      348 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/tests/module_respartner_dummyfield2/partnerview.xml
--rwxr-xr-x   0 runner    (1001) docker     (123)      801 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/testzfs.sh
--rw-r--r--   0 runner    (1001) docker     (123)    40552 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/tools.py
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-23 10:17:04.000000 wodoo-0.3.96/wodoo/version.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.614851 wodoo-0.3.96/wodoo/wait/
--rw-r--r--   0 runner    (1001) docker     (123)      114 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/wait/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/wait/decorator.py
--rw-r--r--   0 runner    (1001) docker     (123)     1928 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/wait/log.py
--rw-r--r--   0 runner    (1001) docker     (123)      520 2023-01-23 10:16:50.000000 wodoo-0.3.96/wodoo/wait/tcp.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 10:17:07.610851 wodoo-0.3.96/wodoo.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-01-23 10:17:07.000000 wodoo-0.3.96/wodoo.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4305 2023-01-23 10:17:07.000000 wodoo-0.3.96/wodoo.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-23 10:17:07.000000 wodoo-0.3.96/wodoo.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-01-23 10:17:07.000000 wodoo-0.3.96/wodoo.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      348 2023-01-23 10:17:07.000000 wodoo-0.3.96/wodoo.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-23 10:17:07.000000 wodoo-0.3.96/wodoo.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-01-30 10:10:00.000000 wodoo-0.3.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-01-30 10:10:18.253246 wodoo-0.3.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4692 2023-01-30 10:10:00.000000 wodoo-0.3.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      349 2023-01-30 10:10:18.253246 wodoo-0.3.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2156 2023-01-30 10:10:00.000000 wodoo-0.3.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.245247 wodoo-0.3.99/wodoo/
+-rw-r--r--   0 runner    (1001) docker     (123)     1265 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3372 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8126 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/click_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      624 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/click_global_commands.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/config/
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/config/cicd_network_for_project.yml
+-rw-r--r--   0 runner    (1001) docker     (123)       53 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/config/default_network
+-rw-r--r--   0 runner    (1001) docker     (123)      121 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/config/template_onlyloop.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/config/template_withports.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2600 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/consts.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     7012 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/daddy_cleanup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1087 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/defaults
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.237247 wodoo-0.3.99/wodoo/extra_install/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.241247 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/
+-rw-r--r--   0 runner    (1001) docker     (123)      428 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/Dockerfile
+-rw-r--r--   0 runner    (1001) docker     (123)      939 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/README.txt
+-rwxr-xr-x   0 runner    (1001) docker     (123)       81 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/debug.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     1217 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/docker-compose.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      182 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/entrypoint.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)       72 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/interactive.sh
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/
+-rw-r--r--   0 runner    (1001) docker     (123)      158 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/config
+-rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/id_rsa
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/id_rsa.pub
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/
+-rw-r--r--   0 runner    (1001) docker     (123)      537 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/ANPASSUNGEN.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     9680 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/Dockerfile
+-rw-r--r--   0 runner    (1001) docker     (123)      822 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/docker-compose.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/
+-rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/11-setup-config-files
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/config/
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/config/ari_additional_custom.conf.appendix
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/config/manager_custom.conf.appendix
+-rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/default_extensions.csv
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/asterisk/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/asterisk/freepbx_chown.conf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-finish.d/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      349 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-finish.d/10-freepbx
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-init.d/
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/cont-init.d/10-start
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/
+-rw-r--r--   0 runner    (1001) docker     (123)      301 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/apache2
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/asterisk
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/fail2ban
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/logrotate.d/fop
+-rw-r--r--   0 runner    (1001) docker     (123)      202 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/odbc.ini
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/etc/odbcinst.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/08-ssh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      567 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/09-mariadb
+-rwxr-xr-x   0 runner    (1001) docker     (123)    17011 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/10-freepbx
+-rwxr-xr-x   0 runner    (1001) docker     (123)      475 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/13-extra-modules
+-rw-r--r--   0 runner    (1001) docker     (123)      679 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/14-mysql-settings
+-rw-r--r--   0 runner    (1001) docker     (123)      157 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/15-permissions
+-rw-r--r--   0 runner    (1001) docker     (123)      383 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/16-soundlang
+-rw-r--r--   0 runner    (1001) docker     (123)      348 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/20-load-default-extensions
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.241247 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/root/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/root/.ssh/
+-rw-r--r--   0 runner    (1001) docker     (123)      391 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/root/.ssh/authorized_keys
+-rwxr-xr-x   0 runner    (1001) docker     (123)      423 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/run_freepbx.sh
+-rw-r--r--   0 runner    (1001) docker     (123)    21607 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_backup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2029 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_clickhelpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29246 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_composer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12987 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9713 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_control_with_docker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15508 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_db.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4378 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_db_snapshots.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6049 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_db_snapshots_docker_btrfs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10185 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_db_snapshots_docker_zfs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1735 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_db_snapshots_plain_postgres.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4937 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_docker_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1112 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_lang.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45384 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2317 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15600 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_src.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4230 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_talk.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5740 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/lib_turnintodev.py
+-rw-r--r--   0 runner    (1001) docker     (123)    53179 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/module_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4554 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/myconfigparser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6400 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/odoo_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25337 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/odoo_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      320 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/pudb.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      354 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     7418 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/robo_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3942 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/tests/MANIFEST
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/tests/gimera.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/tests/module_respartner_dummyfield1/
+-rw-r--r--   0 runner    (1001) docker     (123)      347 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/tests/module_respartner_dummyfield1/partnerview.xml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/tests/module_respartner_dummyfield2/
+-rw-r--r--   0 runner    (1001) docker     (123)      348 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/tests/module_respartner_dummyfield2/partnerview.xml
+-rwxr-xr-x   0 runner    (1001) docker     (123)      801 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/testzfs.sh
+-rw-r--r--   0 runner    (1001) docker     (123)    40552 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-30 10:10:13.000000 wodoo-0.3.99/wodoo/version.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo/wait/
+-rw-r--r--   0 runner    (1001) docker     (123)      114 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/wait/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/wait/decorator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1928 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/wait/log.py
+-rw-r--r--   0 runner    (1001) docker     (123)      520 2023-01-30 10:10:00.000000 wodoo-0.3.99/wodoo/wait/tcp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 10:10:18.249246 wodoo-0.3.99/wodoo.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-01-30 10:10:18.000000 wodoo-0.3.99/wodoo.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4305 2023-01-30 10:10:18.000000 wodoo-0.3.99/wodoo.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 10:10:18.000000 wodoo-0.3.99/wodoo.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-01-30 10:10:18.000000 wodoo-0.3.99/wodoo.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      355 2023-01-30 10:10:18.000000 wodoo-0.3.99/wodoo.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-30 10:10:18.000000 wodoo-0.3.99/wodoo.egg-info/top_level.txt
```

### Comparing `wodoo-0.3.96/LICENSE` & `wodoo-0.3.99/LICENSE`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/PKG-INFO` & `wodoo-0.3.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wodoo
-Version: 0.3.96
+Version: 0.3.99
 Summary: Odoo Framework
 Home-page: https://github.com/marcwimmer/wodoo
 Author: Marc-Christian Wimmer
 License: MIT
 Requires-Python: >=3.6.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `wodoo-0.3.96/README.md` & `wodoo-0.3.99/README.md`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/setup.py` & `wodoo-0.3.99/setup.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/__init__.py` & `wodoo-0.3.99/wodoo/__init__.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/cli.py` & `wodoo-0.3.99/wodoo/cli.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/click_config.py` & `wodoo-0.3.99/wodoo/click_config.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/click_global_commands.py` & `wodoo-0.3.99/wodoo/click_global_commands.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/consts.py` & `wodoo-0.3.99/wodoo/consts.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/daddy_cleanup.py` & `wodoo-0.3.99/wodoo/daddy_cleanup.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/defaults` & `wodoo-0.3.99/wodoo/defaults`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/README.txt` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/README.txt`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/docker-compose.yml` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/docker-compose.yml`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/id_rsa` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/connector_mqtt_asterisk/ssh/id_rsa`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/ANPASSUNGEN.txt` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/ANPASSUNGEN.txt`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/Dockerfile` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/Dockerfile`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/docker-compose.yml` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/docker-compose.yml`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/11-setup-config-files` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/11-setup-config-files`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/default_extensions.csv` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/default_extensions.csv`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/09-mariadb` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/09-mariadb`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/10-freepbx` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/10-freepbx`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/14-mysql-settings` & `wodoo-0.3.99/wodoo/extra_install/asterisk_customs/docker-freepbx/install/init.custom/14-mysql-settings`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_backup.py` & `wodoo-0.3.99/wodoo/lib_backup.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_clickhelpers.py` & `wodoo-0.3.99/wodoo/lib_clickhelpers.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_composer.py` & `wodoo-0.3.99/wodoo/lib_composer.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_control.py` & `wodoo-0.3.99/wodoo/lib_control.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_control_with_docker.py` & `wodoo-0.3.99/wodoo/lib_control_with_docker.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_db.py` & `wodoo-0.3.99/wodoo/lib_db.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_db_snapshots.py` & `wodoo-0.3.99/wodoo/lib_db_snapshots.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_db_snapshots_docker_btrfs.py` & `wodoo-0.3.99/wodoo/lib_db_snapshots_docker_btrfs.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_db_snapshots_docker_zfs.py` & `wodoo-0.3.99/wodoo/lib_db_snapshots_docker_zfs.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_db_snapshots_plain_postgres.py` & `wodoo-0.3.99/wodoo/lib_db_snapshots_plain_postgres.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_docker_registry.py` & `wodoo-0.3.99/wodoo/lib_docker_registry.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_lang.py` & `wodoo-0.3.99/wodoo/lib_lang.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_module.py` & `wodoo-0.3.99/wodoo/lib_module.py`

 * *Files 2% similar despite different names*

```diff
@@ -261,64 +261,14 @@
                 new_version = tuple(list(map(int, odoo_version)) + list(new_version))
                 del odoo_version
 
             if new_version > version:
                 yield dep
 
 
-@odoo_module.command(
-    help=("If menu items are missing, then recomputing the parent store" "can help")
-)
-@pass_config
-@click.pass_context
-def recompute_parent_store(ctx, config):
-    if config.use_docker:
-        from .lib_control_with_docker import shell as lib_shell
-
-    click.secho("Recomputing parent store...", fg="blue")
-    lib_shell(
-        config,
-        (
-            "for model in self.env['ir.model'].search([]):\n"
-            "   try:\n"
-            "       obj = self.env[model.model]\n"
-            "   except KeyError: pass\n"
-            "   else:\n"
-            "       obj._parent_store_compute()\n"
-            "       env.cr.commit()\n"
-        ),
-    )
-    click.secho("Recompute parent store done.", fg="green")
-
-
-@odoo_module.command(
-    help=(
-        "As the name says: if db was transferred, web-icons are restored"
-        " on missing assets"
-    )
-)
-@pass_config
-@click.pass_context
-def restore_web_icons(ctx, config):
-    if config.use_docker:
-        from .lib_control_with_docker import shell as lib_shell
-
-    click.secho("Restoring web icons...", fg="blue")
-    lib_shell(
-        config,
-        (
-            "for x in self.env['ir.ui.menu'].search([]):\n"
-            "   if not x.web_icon: continue\n"
-            "   x.web_icon_data = x._compute_web_icon_data(x.web_icon)\n"
-            "   env.cr.commit()\n"
-        ),
-    )
-    click.secho("Restored web icons.", fg="green")
-
-
 def _get_available_modules(ctx, param, incomplete):
     from .odoo_config import MANIFEST
 
     try:
         manifest = MANIFEST()
         if not manifest:
             raise Exception("no manifest")
@@ -872,28 +822,14 @@
         ctx.invoke(show_install_state, suppress_error=True)
         raise Exception("Error at /update_modules.py - aborting update process.")
 
     if not no_restart:
         Commands.invoke(ctx, "restart", machines=["odoo"])
 
 
-@odoo_module.command()
-@pass_config
-def progress(config):
-    """
-    Displays installation progress
-    """
-    for row in _execute_sql(
-        config.get_odoo_conn(),
-        "select state, count(*) from ir_module_module group by state;",
-        fetchall=True,
-    ):
-        click.echo("{}: {}".format(row[0], row[1]))
-
-
 @odoo_module.command(name="show-install-state")
 @pass_config
 def show_install_state(config, suppress_error=False, missing_as_error=False):
     from .module_tools import DBModules
 
     dangling = list(DBModules.get_dangling_modules())
     if dangling:
@@ -923,21 +859,14 @@
     from .odoo_config import get_odoo_addons_paths
 
     paths = get_odoo_addons_paths()
     for path in paths:
         click.echo(path)
 
 
-@odoo_module.command(name="pretty-print-manifest")
-def pretty_print_manifest():
-    from .odoo_config import MANIFEST
-
-    MANIFEST().rewrite()
-
-
 @odoo_module.command(name="show-conflicting-modules")
 def show_conflicting_modules():
     from .odoo_config import get_odoo_addons_paths
 
     get_odoo_addons_paths()
 
 
@@ -1293,44 +1222,14 @@
             click.secho(
                 tabulate(errors, headers="keys", tablefmt="fancy_grid"), fg="red"
             )
     if errors:
         sys.exit(-1)
 
 
-@odoo_module.command()
-@click.argument("name", required=True)
-@click.option("-Q", "--quick", is_flag=True)
-@pass_config
-@click.pass_context
-def set_ribbon(ctx, config, name, quick):
-    if not quick:
-        SQL = """
-            Select state from ir_module_module where name = 'web_environment_ribbon';
-        """
-        res = _execute_sql(config.get_odoo_conn(), SQL, fetchone=True)
-        if not (res and res[0] == "installed"):
-            Commands.invoke(
-                ctx, "update", module=["web_environment_ribbon"], no_dangling_check=True
-            )
-
-    _execute_sql(
-        config.get_odoo_conn(),
-        """
-        UPDATE
-            ir_config_parameter
-        SET
-            value = %s
-        WHERE
-            key = 'ribbon.name';
-    """,
-        params=(name,),
-    )
-
-
 @odoo_module.command(help="For directly installed odoos.")
 @pass_config
 @click.pass_context
 def generate_update_command(ctx, config):
     modules = _get_default_modules_to_update()
     click.secho(f"-u {','.join(modules)}")
 
@@ -1461,14 +1360,15 @@
 @pass_config
 @click.pass_context
 def list_deps(ctx, config, module, no_cache):
     import arrow
 
     started = arrow.get()
     from .module_tools import Modules, DBModules, Module
+    from .module_tools import NotInAddonsPath
     from .odoo_config import customs_dir
     from .consts import FILE_DIRHASHES
 
     _clean_customs(ctx, config)
 
     click.secho("Loading Modules...", fg="yellow")
     modules = Modules()
@@ -1499,15 +1399,19 @@
         started = arrow.get()
         if config.verbose:
             print(f"part1: {part1.total_seconds()}")
 
         # get some hashes:
         paths = _get_global_hash_paths(True)
         for mod in data["modules"]:
-            paths.append(Module.get_by_name(mod).path)
+            try:
+                objmod = Module.get_by_name(mod)
+                paths.append(objmod.path)
+            except NotInAddonsPath:
+                pass
         for mod in data["auto_install"]:
             paths.append(Module.get_by_name(mod).path)
 
         # hash python version
         python_version = config.ODOO_PYTHON_VERSION
         to_hash = str(python_version) + ";"
         for path in list(sorted(set(paths))):
@@ -1571,10 +1475,9 @@
     mods = Modules()
     modules = list(sorted(mods.get_all_modules_installed_by_manifest()))
     print("---")
     for m in modules:
         print(m)
 
 
-Commands.register(progress)
 Commands.register(update)
 Commands.register(show_install_state)
```

### Comparing `wodoo-0.3.96/wodoo/lib_setup.py` & `wodoo-0.3.99/wodoo/lib_setup.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/lib_src.py` & `wodoo-0.3.99/wodoo/lib_src.py`

 * *Files 2% similar despite different names*

```diff
@@ -389,15 +389,14 @@
     Fetches from odoo-ninjas/odoo.sh
     """
     manifest = MANIFEST()
 
     from .tools import rsync
     from .odoo_config import customs_dir
     from .module_tools import Modules, Module
-    from .module_tools import ModulesCache
 
     modules = Modules()
     odoosh = OdooShRepo(current_version())
 
     def transfer_module(module):
         destination = customs_dir() / ADDONS_OCA / module
         if not destination.parent.exists():
@@ -410,16 +409,14 @@
         if not [x for x in addons_paths if x == ADDONS_OCA]:
             addons_paths.append(ADDONS_OCA)
         manifest["addons_paths"] = addons_paths
         manifest["install"] += [module]
         manifest.rewrite()
 
     for module in module:
-        ModulesCache.reset_cache()
-
         oca_module = odoosh.find_module(module)
         todos = [oca_module.name]
         for dep in odoosh.find_dependant_modules(oca_module):
             todos.append(dep.name)
 
         for todo in todos:
             transfer_module(todo)
@@ -441,15 +438,18 @@
 
     src = customs_dir()
     ignore_paths = []
     for x in ["odoo", "enterprise", "themes"]:
         ignore_paths.append((src / x).resolve().absolute())
 
     all_dirs = list(
-        filter(lambda x: ".git" not in x.parts, bashfind(path=src, type="d"), )
+        filter(
+            lambda x: ".git" not in x.parts,
+            bashfind(path=src, type="d"),
+        )
     )
 
     for x in sorted(check):
         dirs = filter(lambda dir: dir.name == x, all_dirs)
         for y in dirs:
             if not (y / "__manifest__.py").exists():
                 continue
@@ -469,22 +469,14 @@
                         "Not clear which module gets installed: \n"
                         f"{module.path}\n"
                         f"{y}"
                     )
 
 
 @src.command
-@pass_config
-def clear_cache(config):
-    from .module_tools import ModulesCache
-
-    ModulesCache._clear_cache()
-
-
-@src.command
 @click.option("-f", "--fix-not-in-manifest", is_flag=True)
 @pass_config
 def show_installed_modules(config, fix_not_in_manifest):
     from .module_tools import DBModules, Module
     from .odoo_config import customs_dir
 
     path = customs_dir()
@@ -512,8 +504,13 @@
         click.secho(f"Not in filesystem: {module}", fg="red")
 
     if fix_not_in_manifest:
         manifest["install"] = setinstall
         manifest.rewrite()
 
 
-Commands.register(clear_cache)
+@src.command(name="pretty-print-manifest")
+def pretty_print_manifest():
+    from .odoo_config import MANIFEST
+
+    MANIFEST().rewrite()
+
```

### Comparing `wodoo-0.3.96/wodoo/lib_turnintodev.py` & `wodoo-0.3.99/wodoo/lib_turnintodev.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/module_tools.py` & `wodoo-0.3.99/wodoo/module_tools.py`

 * *Files 2% similar despite different names*

```diff
@@ -626,27 +626,24 @@
                         except Exception:
                             cr.connection.rollback()
 
                     if res:
                         exe("ir.ui.view", "write", view_ids, {"arch_db": arch})
 
 
-
-
-
 class Modules(object):
     def __init__(self):
         pass
 
     @property
     def modules(self):
-        if 'modules' not in Modules_Cache:
+        if "modules" not in Modules_Cache:
             modules = self._get_modules()
-            Modules_Cache['modules'] = modules
-        return Modules_Cache['modules']
+            Modules_Cache["modules"] = modules
+        return Modules_Cache["modules"]
 
     @classmethod
     @measure_time
     def _get_modules(self, no_deptree=False):
         modnames = set()
         from .odoo_config import get_odoo_addons_paths
 
@@ -729,14 +726,15 @@
         'stock_prod_lot_unique': {
             'stock': {
                 'base':
             },
             'product': {},
         }
         """
+
         def append_deps(mod, depth):
             result = set()
             if depth > 1000:
                 raise Exception("Recursive loop perhaps - to depth")
             if not mod.exists:
                 return set()
             for dep in list(mod.manifest_dict.get("depends", [])):
@@ -799,15 +797,15 @@
                     all_modules.add(auto_install_module.name)
             if len_modules == len(all_modules):
                 break
         return list(all_modules)
 
     @classmethod
     def get_module_flat_dependency_tree(self, module):
-        deps= self._get_module_dependency_tree(module)
+        deps = self._get_module_dependency_tree(module)
         return sorted(list(deps))
 
     def get_all_auto_install_modules(self):
         auto_install_modules = []
         for module in sorted(Modules().modules):
             try:
                 module = Module.get_by_name(module)
@@ -815,30 +813,37 @@
                 continue
             if module.manifest_dict.get("auto_install", False):
                 auto_install_modules.append(module)
         return list(sorted(set(auto_install_modules)))
 
     @measure_time
     def get_filtered_auto_install_modules_based_on_module_list(self, module_list):
-        module_list = list(map(lambda x: Module.get_by_name(x), module_list))
+        def _transform_modulelist(module_list):
+            for mod in module_list:
+                try:
+                    objmod = Module.get_by_name(mod)
+                    yield objmod
+                except NotInAddonsPath:
+                    pass
+        module_list = list(_transform_modulelist(module_list))
 
         complete_modules = set()
         for mod in module_list:
             complete_modules |= set(list(self.get_module_flat_dependency_tree(mod)))
 
         def _get(all_modules):
             for auto_install_module in all_modules:
                 dependencies = set(
                     list(self.get_module_flat_dependency_tree(auto_install_module))
                 )
                 installed_dependencies = set(
                     [
                         x
                         for x in sorted(dependencies)
-                        if x.exists  
+                        if x.exists
                         if x.manifest_dict.get("auto_install") or x in complete_modules
                     ]
                 )
                 if dependencies == installed_dependencies:
                     yield auto_install_module
 
                     if all(x in module_list for x in dependencies):
@@ -1049,15 +1054,17 @@
                     path = path.relative_to(customs_dir())
                     os.chdir(customs_dir())
                 except:
                     try:
                         path = path.relative_to(cwd)
                     except ValueError:
                         path = path.relative_to(customs_dir())
-                        os.chdir(customs_dir())  # reset later; required that parents works
+                        os.chdir(
+                            customs_dir()
+                        )  # reset later; required that parents works
             p = path if path.is_dir() else path.parent
 
             for p in [p] + list(p.parents):
                 if (p / manifest_file_names()).exists():
                     if ".git" in p.parts:
                         continue
                     self._manifest_path = p / manifest_file_names()
@@ -1127,16 +1134,19 @@
             return name
         mod = cls.__get_by_name_cached(name, nocache=nocache, no_deptree=no_deptree)
         return mod
 
     @classmethod
     def _get_by_name(cls, name, nocache=False, no_deptree=False):
         from .odoo_config import get_odoo_addons_paths
+
         if not name:
-            import pudb;pudb.set_trace()
+            import pudb
+
+            pudb.set_trace()
 
         if isinstance(name, Module):
             name = name.name
         path = None
         for addon_path in get_odoo_addons_paths():
             dir = addon_path / name
             if dir.exists():
@@ -1333,18 +1343,54 @@
             if file.name.startswith("."):
                 continue
             if ".git" in file.parts:
                 continue
             # relative to module path
             yield file
 
+    def update_init_imports(self):
+        def _remove_all_instruction(content):
+            if "__all__ =" not in content:
+                return content
+            content = content.replace("import os", "")
+            content = content.replace("import glob", "")
+            content = "\n".join(
+                filter(lambda x: "__all__ =" not in x, content.splitlines())
+            ).strip() + "\n"
+            return content
+
+        for path in self.path.glob("*"):
+            if not path.is_dir():
+                continue
+            if not path.name in ["models", "tests", "controller", "controllers"]:
+                continue
+            init_file = path / "__init__.py"
+            if not init_file.exists():
+                continue
+            content = _remove_all_instruction(init_file.read_text()).splitlines()
+
+            for file in path.glob("*"):
+                if file.suffix == ".py" and file.stem not in ["__init__"]:
+                    importinstruction = f"from . import {file.stem}"
+                    if importinstruction not in content:
+                        content += [importinstruction]
+
+            # remove if py does not exist anymore:
+            for line in list(content):
+                if line.startswith("from . import "):
+                    if not (path / (line.split(" ")[-1] + ".py")).exists():
+                        content.remove(line)
+
+            init_file.write_text('\n'.join(content))
+
     def update_module_file(self):
         # updates __openerp__.py the update-section to point to all xml files in the module;
         # except if there is a directory test; those files are ignored;
         self.update_assets_file()
+        self.update_init_imports()
         mod = self.manifest_dict
 
         all_files = list(self.get_all_files_of_module())
         # first collect all xml files and ignore test and static
         DATA_NAME = "data"
         if current_version() <= 7.0:
             DATA_NAME = "update_xml"
```

### Comparing `wodoo-0.3.96/wodoo/myconfigparser.py` & `wodoo-0.3.99/wodoo/myconfigparser.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/odoo_config.py` & `wodoo-0.3.99/wodoo/odoo_config.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/odoo_parser.py` & `wodoo-0.3.99/wodoo/odoo_parser.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/robo_helpers.py` & `wodoo-0.3.99/wodoo/robo_helpers.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/settings.py` & `wodoo-0.3.99/wodoo/settings.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/testzfs.sh` & `wodoo-0.3.99/wodoo/testzfs.sh`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/tools.py` & `wodoo-0.3.99/wodoo/tools.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/wait/decorator.py` & `wodoo-0.3.99/wodoo/wait/decorator.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/wait/log.py` & `wodoo-0.3.99/wodoo/wait/log.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo/wait/tcp.py` & `wodoo-0.3.99/wodoo/wait/tcp.py`

 * *Files identical despite different names*

### Comparing `wodoo-0.3.96/wodoo.egg-info/PKG-INFO` & `wodoo-0.3.99/wodoo.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wodoo
-Version: 0.3.96
+Version: 0.3.99
 Summary: Odoo Framework
 Home-page: https://github.com/marcwimmer/wodoo
 Author: Marc-Christian Wimmer
 License: MIT
 Requires-Python: >=3.6.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `wodoo-0.3.96/wodoo.egg-info/SOURCES.txt` & `wodoo-0.3.99/wodoo.egg-info/SOURCES.txt`

 * *Files identical despite different names*

