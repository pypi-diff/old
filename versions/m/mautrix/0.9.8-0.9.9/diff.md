# Comparing `tmp/mautrix-0.9.8.tar.gz` & `tmp/mautrix-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mautrix-0.9.8.tar", last modified: Thu Jun 24 12:30:30 2021, max compression
+gzip compressed data, was "mautrix-0.9.9.tar", last modified: Fri Jul 16 19:22:03 2021, max compression
```

## Comparing `mautrix-0.9.8.tar` & `mautrix-0.9.9.tar`

### file list

```diff
@@ -1,206 +1,207 @@
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    16727 2021-04-22 21:33:42.000000 mautrix-0.9.8/LICENSE
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       94 2021-04-22 21:33:42.000000 mautrix-0.9.8/MANIFEST.in
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3070 2021-06-24 12:30:30.920225 mautrix-0.9.8/PKG-INFO
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2296 2021-04-22 21:33:42.000000 mautrix-0.9.8/README.rst
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      159 2021-06-24 12:28:54.000000 mautrix-0.9.8/mautrix/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    11471 2021-06-11 07:48:49.000000 mautrix-0.9.8/mautrix/api.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/appservice/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      311 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/__init__.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/appservice/api/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       88 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/api/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     9046 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/api/appservice.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    18184 2021-05-17 11:44:09.000000 mautrix-0.9.8/mautrix/appservice/api/intent.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6464 2021-06-18 17:21:53.000000 mautrix-0.9.8/mautrix/appservice/appservice.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6999 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/as_handler.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/appservice/state_store/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       68 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/state_store/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      580 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/state_store/asyncpg.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1057 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/state_store/file.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2406 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/state_store/memory.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      527 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/appservice/state_store/sqlalchemy.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/bridge/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      547 2021-06-22 07:19:03.000000 mautrix-0.9.8/mautrix/bridge/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3489 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/_community.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      564 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/async_getter_lock.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     7976 2021-06-09 14:42:25.000000 mautrix-0.9.8/mautrix/bridge/bridge.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/bridge/commands/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      543 2021-06-22 07:10:52.000000 mautrix-0.9.8/mautrix/bridge/commands/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6450 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/commands/admin.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     8141 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/commands/clean_rooms.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      836 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/commands/crypto.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    17266 2021-06-22 07:07:14.000000 mautrix-0.9.8/mautrix/bridge/commands/handler.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     4006 2021-06-22 07:34:21.000000 mautrix-0.9.8/mautrix/bridge/commands/login_matrix.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2976 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/commands/meta.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5004 2021-06-03 13:10:03.000000 mautrix-0.9.8/mautrix/bridge/config.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2681 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/crypto_state_store.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    16451 2021-06-22 07:16:27.000000 mautrix-0.9.8/mautrix/bridge/custom_puppet.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    10692 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/e2ee.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    22605 2021-06-21 12:28:25.000000 mautrix-0.9.8/mautrix/bridge/matrix.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2619 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/notification_disabler.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5793 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/portal.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1180 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/puppet.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2687 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/bridge/state.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/bridge/state_store/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)        0 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/state_store/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1478 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/state_store/asyncpg.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1408 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/bridge/state_store/sqlalchemy.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5219 2021-06-23 16:43:11.000000 mautrix-0.9.8/mautrix/bridge/user.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix/client/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      408 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/__init__.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/client/api/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      265 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     7152 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/authentication.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6174 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/base.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      767 2021-05-21 15:35:22.000000 mautrix-0.9.8/mautrix/client/api/client.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    25493 2021-05-13 13:10:56.000000 mautrix-0.9.8/mautrix/client/api/events.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2180 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/filtering.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/client/api/modules/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      851 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/modules/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2769 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/modules/account_data.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6945 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/modules/crypto.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6896 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/modules/media_repository.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5619 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/modules/misc.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3519 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/modules/push_rules.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3113 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/modules/room_tag.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    27130 2021-05-21 15:37:19.000000 mautrix-0.9.8/mautrix/client/api/rooms.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6360 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/api/user_data.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1549 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/client.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2389 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/dispatcher.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     4930 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/encryption_manager.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/client/state_store/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      148 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5258 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/abstract.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/client/state_store/asyncpg/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       32 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/asyncpg/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6499 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/asyncpg/store.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1826 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/asyncpg/upgrade.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1842 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/file.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5564 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/memory.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      137 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2076 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/mx_room_state.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2871 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/mx_user_profile.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5953 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/sqlstatestore.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1084 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/state_store/sync.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3152 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/store_updater.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    16438 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/client/syncer.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/crypto/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      336 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3963 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/account.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/crypto/attachments/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      179 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/attachments/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3804 2021-05-21 10:28:06.000000 mautrix-0.9.8/mautrix/crypto/attachments/async_attachments.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5041 2021-05-21 10:27:36.000000 mautrix-0.9.8/mautrix/crypto/attachments/attachments.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2913 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/base.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3980 2021-06-22 16:20:29.000000 mautrix-0.9.8/mautrix/crypto/decrypt_megolm.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5044 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/decrypt_olm.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     4986 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/device_lists.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    13803 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/encrypt_megolm.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3992 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/encrypt_olm.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5328 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/key_request.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     9056 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/key_share.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     8345 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/machine.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6162 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/sessions.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/crypto/store/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      211 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/store/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    11770 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/store/abstract.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/crypto/store/asyncpg/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       33 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/store/asyncpg/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    15416 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/store/asyncpg/store.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5194 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/store/asyncpg/upgrade.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5262 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/store/memory.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6845 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/crypto/store/pickle.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1098 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/crypto/types.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/errors/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1383 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/errors/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      723 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/errors/base.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1627 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/errors/crypto.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     4892 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/errors/request.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1530 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/errors/well_known.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.916226 mautrix-0.9.8/mautrix/types/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3723 2021-06-18 18:21:51.000000 mautrix-0.9.8/mautrix/types/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5726 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/auth.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1654 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/crypto.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/types/event/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2611 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/types/event/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1750 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/account_data.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1500 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/base.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3270 2021-06-18 17:50:20.000000 mautrix-0.9.8/mautrix/types/event/encrypted.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2102 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/ephemeral.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2747 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/types/event/generic.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    15270 2021-06-18 17:50:20.000000 mautrix-0.9.8/mautrix/types/event/message.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1393 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/reaction.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1072 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/redaction.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     8574 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/state.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3620 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/to_device.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5535 2021-05-12 10:08:42.000000 mautrix-0.9.8/mautrix/types/event/type.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2377 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/types/event/type.pyi
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3338 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/event/voip.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     6814 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/filter.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2421 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/media.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2909 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/misc.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      810 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/types/primitive.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2172 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/push_rules.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      760 2021-06-18 17:17:46.000000 mautrix-0.9.8/mautrix/types/users.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/types/util/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      216 2021-06-18 18:21:51.000000 mautrix-0.9.8/mautrix/types/util/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     4082 2021-06-18 17:48:10.000000 mautrix-0.9.8/mautrix/types/util/enum.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1928 2021-06-20 17:31:11.000000 mautrix-0.9.8/mautrix/types/util/enum_test.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2229 2021-06-18 17:50:20.000000 mautrix-0.9.8/mautrix/types/util/obj.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3226 2021-06-18 17:53:55.000000 mautrix-0.9.8/mautrix/types/util/serializable.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    13061 2021-06-21 07:50:44.000000 mautrix-0.9.8/mautrix/types/util/serializable_attrs.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     7371 2021-06-21 08:08:57.000000 mautrix-0.9.8/mautrix/types/util/serializable_attrs_test.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/util/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      223 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/__init__.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/util/async_db/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       83 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/async_db/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3798 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/async_db/database.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5384 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/async_db/upgrade.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       95 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/color_log.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/util/config/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      316 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/config/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2129 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/config/base.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1623 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/config/file.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1099 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/config/proxy.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3506 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/config/recursive_dict.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      981 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/config/string.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1518 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/config/validation.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/util/db/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       34 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/db/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     8082 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/db/base.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2327 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/file_store.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/util/formatter/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      567 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5211 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/entity_string.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     4452 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/formatted_string.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      374 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/html_reader.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      413 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/html_reader.pyi
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1993 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/html_reader_htmlparser.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      359 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/html_reader_lxml.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2573 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/formatter/markdown_string.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     9314 2021-06-11 13:37:07.000000 mautrix-0.9.8/mautrix/util/formatter/parser.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.920225 mautrix-0.9.8/mautrix/util/logging/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       72 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/logging/__init__.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1827 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/logging/color.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      875 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/logging/trace.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      799 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/magic.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)    12258 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/manhole.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1093 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/markdown.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1572 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/opt_prometheus.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     2957 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/opt_prometheus.pyi
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     9907 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/program.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1335 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/signed_token.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1259 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/simple_lock.py
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1568 2021-04-22 21:33:42.000000 mautrix-0.9.8/mautrix/util/simple_template.py
-drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-06-24 12:30:30.912225 mautrix-0.9.8/mautrix.egg-info/
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     3070 2021-06-24 12:30:30.000000 mautrix-0.9.8/mautrix.egg-info/PKG-INFO
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     5605 2021-06-24 12:30:30.000000 mautrix-0.9.8/mautrix.egg-info/SOURCES.txt
--rw-rw-r--   0 tulir     (1000) tulir     (1000)        1 2021-06-24 12:30:30.000000 mautrix-0.9.8/mautrix.egg-info/dependency_links.txt
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       99 2021-06-24 12:30:30.000000 mautrix-0.9.8/mautrix.egg-info/requires.txt
--rw-rw-r--   0 tulir     (1000) tulir     (1000)        8 2021-06-24 12:30:30.000000 mautrix-0.9.8/mautrix.egg-info/top_level.txt
--rw-rw-r--   0 tulir     (1000) tulir     (1000)      135 2021-04-22 21:33:42.000000 mautrix-0.9.8/optional-requirements.txt
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       19 2021-04-22 21:33:42.000000 mautrix-0.9.8/requirements.txt
--rw-rw-r--   0 tulir     (1000) tulir     (1000)       38 2021-06-24 12:30:30.924226 mautrix-0.9.8/setup.cfg
--rw-rw-r--   0 tulir     (1000) tulir     (1000)     1256 2021-06-20 17:40:37.000000 mautrix-0.9.8/setup.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.525864 mautrix-0.9.9/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    16727 2021-04-22 21:33:42.000000 mautrix-0.9.9/LICENSE
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       94 2021-04-22 21:33:42.000000 mautrix-0.9.9/MANIFEST.in
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3070 2021-07-16 19:22:03.525864 mautrix-0.9.9/PKG-INFO
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2296 2021-04-22 21:33:42.000000 mautrix-0.9.9/README.rst
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.501864 mautrix-0.9.9/mautrix/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      159 2021-07-15 10:39:20.000000 mautrix-0.9.9/mautrix/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    11471 2021-06-11 07:48:49.000000 mautrix-0.9.9/mautrix/api.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.501864 mautrix-0.9.9/mautrix/appservice/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      311 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/__init__.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.501864 mautrix-0.9.9/mautrix/appservice/api/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       88 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/api/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     9046 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/api/appservice.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    18184 2021-05-17 11:44:09.000000 mautrix-0.9.9/mautrix/appservice/api/intent.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6464 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/appservice/appservice.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     8118 2021-07-16 19:04:00.000000 mautrix-0.9.9/mautrix/appservice/as_handler.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.501864 mautrix-0.9.9/mautrix/appservice/state_store/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       68 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/state_store/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      580 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/state_store/asyncpg.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1057 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/state_store/file.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2406 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/state_store/memory.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      527 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/appservice/state_store/sqlalchemy.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.501864 mautrix-0.9.9/mautrix/bridge/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      566 2021-07-14 13:10:00.000000 mautrix-0.9.9/mautrix/bridge/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3489 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/_community.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      564 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/async_getter_lock.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     7976 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/bridge.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.505864 mautrix-0.9.9/mautrix/bridge/commands/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      543 2021-06-22 07:10:52.000000 mautrix-0.9.9/mautrix/bridge/commands/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6450 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/commands/admin.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     8141 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/commands/clean_rooms.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      836 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/commands/crypto.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    17266 2021-06-22 07:07:14.000000 mautrix-0.9.9/mautrix/bridge/commands/handler.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     4006 2021-06-22 07:34:21.000000 mautrix-0.9.9/mautrix/bridge/commands/login_matrix.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2976 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/commands/meta.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5004 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/config.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2681 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/crypto_state_store.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    16451 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/custom_puppet.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    10787 2021-07-16 07:27:49.000000 mautrix-0.9.9/mautrix/bridge/e2ee.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    22824 2021-07-16 07:35:51.000000 mautrix-0.9.9/mautrix/bridge/matrix.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2619 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/notification_disabler.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5793 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/portal.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1180 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/puppet.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.505864 mautrix-0.9.9/mautrix/bridge/state_store/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)        0 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/state_store/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1478 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/state_store/asyncpg.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1408 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/bridge/state_store/sqlalchemy.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5238 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/bridge/user.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.505864 mautrix-0.9.9/mautrix/client/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      408 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/__init__.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.509864 mautrix-0.9.9/mautrix/client/api/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      265 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     7152 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/authentication.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6174 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/base.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      767 2021-05-21 15:35:22.000000 mautrix-0.9.9/mautrix/client/api/client.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    25493 2021-05-13 13:10:56.000000 mautrix-0.9.9/mautrix/client/api/events.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2180 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/filtering.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.509864 mautrix-0.9.9/mautrix/client/api/modules/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      851 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/modules/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2769 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/modules/account_data.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6945 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/modules/crypto.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6896 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/modules/media_repository.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5619 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/modules/misc.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3519 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/modules/push_rules.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3113 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/modules/room_tag.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    27130 2021-05-21 15:37:19.000000 mautrix-0.9.9/mautrix/client/api/rooms.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6360 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/api/user_data.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1549 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/client/client.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2389 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/dispatcher.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     4930 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/client/encryption_manager.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.509864 mautrix-0.9.9/mautrix/client/state_store/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      148 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5258 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/abstract.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.509864 mautrix-0.9.9/mautrix/client/state_store/asyncpg/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       32 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/asyncpg/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6499 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/asyncpg/store.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1826 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/asyncpg/upgrade.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1842 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/file.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5564 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/memory.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.509864 mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      137 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2076 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/mx_room_state.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2871 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/mx_user_profile.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5953 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/sqlstatestore.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1084 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/client/state_store/sync.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3152 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/client/store_updater.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    16438 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/client/syncer.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.513864 mautrix-0.9.9/mautrix/crypto/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      336 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3963 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/account.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.513864 mautrix-0.9.9/mautrix/crypto/attachments/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      179 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/attachments/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3804 2021-05-21 10:28:06.000000 mautrix-0.9.9/mautrix/crypto/attachments/async_attachments.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5041 2021-05-21 10:27:36.000000 mautrix-0.9.9/mautrix/crypto/attachments/attachments.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2913 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/base.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3980 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/decrypt_megolm.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5044 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/decrypt_olm.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     4986 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/device_lists.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    13803 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/encrypt_megolm.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3992 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/encrypt_olm.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5328 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/key_request.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     9056 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/key_share.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     8345 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/machine.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6162 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/sessions.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.513864 mautrix-0.9.9/mautrix/crypto/store/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      211 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/store/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    11770 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/store/abstract.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.513864 mautrix-0.9.9/mautrix/crypto/store/asyncpg/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       33 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/store/asyncpg/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    15416 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/store/asyncpg/store.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5194 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/store/asyncpg/upgrade.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5262 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/store/memory.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6845 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/crypto/store/pickle.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1098 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/crypto/types.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.513864 mautrix-0.9.9/mautrix/errors/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1383 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/errors/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      723 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/errors/base.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1627 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/errors/crypto.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     4892 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/errors/request.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1530 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/errors/well_known.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)        0 2021-07-14 13:10:00.000000 mautrix-0.9.9/mautrix/py.typed
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.513864 mautrix-0.9.9/mautrix/types/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3723 2021-06-18 18:21:51.000000 mautrix-0.9.9/mautrix/types/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5726 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/types/auth.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1654 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/types/crypto.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.517864 mautrix-0.9.9/mautrix/types/event/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2611 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/types/event/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1750 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/account_data.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1500 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/base.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3270 2021-06-18 17:50:20.000000 mautrix-0.9.9/mautrix/types/event/encrypted.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2102 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/ephemeral.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2747 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/types/event/generic.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    15270 2021-06-18 17:50:20.000000 mautrix-0.9.9/mautrix/types/event/message.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1393 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/reaction.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1072 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/redaction.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     8574 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/state.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3620 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/to_device.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5535 2021-05-12 10:08:42.000000 mautrix-0.9.9/mautrix/types/event/type.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2377 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/types/event/type.pyi
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3338 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/event/voip.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     6814 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/types/filter.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2421 2021-06-18 17:17:46.000000 mautrix-0.9.9/mautrix/types/media.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3003 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/types/misc.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      810 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/types/primitive.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2172 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/types/push_rules.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      760 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/types/users.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.517864 mautrix-0.9.9/mautrix/types/util/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      216 2021-06-18 18:21:51.000000 mautrix-0.9.9/mautrix/types/util/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     4082 2021-06-18 17:48:10.000000 mautrix-0.9.9/mautrix/types/util/enum.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1928 2021-06-20 17:31:11.000000 mautrix-0.9.9/mautrix/types/util/enum_test.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2229 2021-06-18 17:50:20.000000 mautrix-0.9.9/mautrix/types/util/obj.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3226 2021-06-18 17:53:55.000000 mautrix-0.9.9/mautrix/types/util/serializable.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    13061 2021-06-21 07:50:44.000000 mautrix-0.9.9/mautrix/types/util/serializable_attrs.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     7371 2021-06-21 08:08:57.000000 mautrix-0.9.9/mautrix/types/util/serializable_attrs_test.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.521864 mautrix-0.9.9/mautrix/util/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      239 2021-07-14 13:10:00.000000 mautrix-0.9.9/mautrix/util/__init__.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.521864 mautrix-0.9.9/mautrix/util/async_db/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       83 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/async_db/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3798 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/async_db/database.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5384 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/async_db/upgrade.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2947 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/bridge_state.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       95 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/color_log.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.521864 mautrix-0.9.9/mautrix/util/config/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      316 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/config/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2129 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/config/base.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1623 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/config/file.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1099 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/config/proxy.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3506 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/config/recursive_dict.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      981 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/config/string.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1518 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/config/validation.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.521864 mautrix-0.9.9/mautrix/util/db/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       34 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/db/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     8082 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/db/base.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2327 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/file_store.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.525864 mautrix-0.9.9/mautrix/util/formatter/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      567 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5211 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/entity_string.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     4452 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/formatted_string.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      374 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/html_reader.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      413 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/html_reader.pyi
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1993 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/html_reader_htmlparser.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      359 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/html_reader_lxml.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2573 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/formatter/markdown_string.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     9314 2021-06-11 13:37:07.000000 mautrix-0.9.9/mautrix/util/formatter/parser.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.525864 mautrix-0.9.9/mautrix/util/logging/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       72 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/logging/__init__.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1827 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/logging/color.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      875 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/logging/trace.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      799 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/magic.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)    12258 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/manhole.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1093 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/markdown.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1572 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/opt_prometheus.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     2957 2021-04-22 21:33:42.000000 mautrix-0.9.9/mautrix/util/opt_prometheus.pyi
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     9907 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/program.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1335 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/signed_token.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1259 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/simple_lock.py
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1568 2021-07-15 10:39:16.000000 mautrix-0.9.9/mautrix/util/simple_template.py
+drwxrwxr-x   0 tulir     (1000) tulir     (1000)        0 2021-07-16 19:22:03.501864 mautrix-0.9.9/mautrix.egg-info/
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     3070 2021-07-16 19:22:03.000000 mautrix-0.9.9/mautrix.egg-info/PKG-INFO
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     5627 2021-07-16 19:22:03.000000 mautrix-0.9.9/mautrix.egg-info/SOURCES.txt
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)        1 2021-07-16 19:22:03.000000 mautrix-0.9.9/mautrix.egg-info/dependency_links.txt
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       99 2021-07-16 19:22:03.000000 mautrix-0.9.9/mautrix.egg-info/requires.txt
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)        8 2021-07-16 19:22:03.000000 mautrix-0.9.9/mautrix.egg-info/top_level.txt
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)      135 2021-04-22 21:33:42.000000 mautrix-0.9.9/optional-requirements.txt
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       19 2021-04-22 21:33:42.000000 mautrix-0.9.9/requirements.txt
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)       38 2021-07-16 19:22:03.525864 mautrix-0.9.9/setup.cfg
+-rw-rw-r--   0 tulir     (1000) tulir     (1000)     1289 2021-07-14 13:10:00.000000 mautrix-0.9.9/setup.py
```

### Comparing `mautrix-0.9.8/LICENSE` & `mautrix-0.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/PKG-INFO` & `mautrix-0.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mautrix
-Version: 0.9.8
+Version: 0.9.9
 Summary: A Python 3 asyncio Matrix framework.
 Home-page: https://github.com/tulir/mautrix-python
 Author: Tulir Asokan
 Author-email: tulir@maunium.net
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

### Comparing `mautrix-0.9.8/README.rst` & `mautrix-0.9.9/README.rst`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/api.py` & `mautrix-0.9.9/mautrix/api.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/appservice/api/appservice.py` & `mautrix-0.9.9/mautrix/appservice/api/appservice.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/appservice/api/intent.py` & `mautrix-0.9.9/mautrix/appservice/api/intent.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/appservice/appservice.py` & `mautrix-0.9.9/mautrix/appservice/appservice.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/appservice/as_handler.py` & `mautrix-0.9.9/mautrix/appservice/as_handler.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 # Copyright (c) 2020 Tulir Asokan
 #
 # This Source Code Form is subject to the terms of the Mozilla Public
 # License, v. 2.0. If a copy of the MPL was not distributed with this
 # file, You can obtain one at http://mozilla.org/MPL/2.0/.
 # Partly based on github.com/Cadair/python-appservice-framework (MIT license)
-from typing import Optional, Callable, Awaitable, List, Set
+from typing import Optional, Callable, Awaitable, List, Set, Dict, Any
 from json import JSONDecodeError
 from aiohttp import web
 import asyncio
 import logging
 
-from mautrix.types import JSON, UserID, RoomAlias, Event, EphemeralEvent, SerializerError
+from mautrix.types import (JSON, UserID, RoomAlias, Event, EphemeralEvent, SerializerError,
+                           DeviceOTKCount, DeviceLists)
 
 QueryFunc = Callable[[web.Request], Awaitable[Optional[web.Response]]]
 HandlerFunc = Callable[[Event], Awaitable]
 
 
 class AppServiceServerMixin:
     loop: asyncio.AbstractEventLoop
@@ -51,15 +52,15 @@
         app.router.add_route("GET", "/_matrix/app/v1/users/{user_id}", self._http_query_user)
 
     def _check_token(self, request: web.Request) -> bool:
         try:
             token = request.rel_url.query["access_token"]
         except KeyError:
             try:
-                token = request.headers["Authorization"].lstrip("Bearer ")
+                token = request.headers["Authorization"].removeprefix("Bearer ")
             except (KeyError, AttributeError):
                 return False
 
         if token != self.hs_token:
             return False
 
         return True
@@ -98,64 +99,78 @@
             self.log.exception("Exception in alias query handler")
             return web.json_response({"error": "Internal appservice error"}, status=500)
 
         if not response:
             return web.json_response({}, status=404)
         return web.json_response(response)
 
+    @staticmethod
+    def _get_with_fallback(json: Dict[str, Any], field: str, unstable_prefix: str,
+                           default: Any = None) -> Any:
+        try:
+            return json.pop(field)
+        except KeyError:
+            try:
+                return json.pop(f"{unstable_prefix}.{field}")
+            except KeyError:
+                return default
+
     async def _http_handle_transaction(self, request: web.Request) -> web.Response:
         if not self._check_token(request):
             return web.json_response({"error": "Invalid auth token"}, status=401)
 
         transaction_id = request.match_info["transaction_id"]
         if transaction_id in self.transactions:
             return web.json_response({})
 
         try:
             json = await request.json()
         except JSONDecodeError:
             return web.json_response({"error": "Body is not JSON"}, status=400)
 
         try:
-            events = json["events"]
+            events = json.pop("events")
         except KeyError:
             return web.json_response({"error": "Missing events object in body"}, status=400)
 
-        if self.ephemeral_events:
-            try:
-                ephemeral = json["ephemeral"]
-            except KeyError:
-                try:
-                    ephemeral = json["de.sorunome.msc2409.ephemeral"]
-                except KeyError:
-                    ephemeral = None
-        else:
-            ephemeral = None
+        ephemeral = (self._get_with_fallback(json, "ephemeral", "de.sorunome.msc2409")
+                     if self.ephemeral_events else None)
+        device_lists = DeviceLists.deserialize(
+            self._get_with_fallback(json, "device_lists", "org.matrix.msc3202"))
+        otk_counts = {user_id: DeviceOTKCount.deserialize(count)
+                      for user_id, count
+                      in self._get_with_fallback(json, "device_one_time_keys_count",
+                                                 "org.matrix.msc3202", default={}).items()}
 
         try:
-            await self.handle_transaction(transaction_id, events=events, ephemeral=ephemeral)
+            output = await self.handle_transaction(transaction_id, events=events, extra_data=json,
+                                                   ephemeral=ephemeral, device_lists=device_lists,
+                                                   device_otk_count=otk_counts)
         except Exception:
             self.log.exception("Exception in transaction handler")
+            output = None
 
         self.transactions.add(transaction_id)
 
-        return web.json_response({})
+        return web.json_response(output or {})
 
     @staticmethod
     def _fix_prev_content(raw_event: JSON) -> None:
         try:
             raw_event["unsigned"]["prev_content"]
         except KeyError:
             try:
                 raw_event.setdefault("unsigned", {})["prev_content"] = raw_event["prev_content"]
             except KeyError:
                 pass
 
-    async def handle_transaction(self, txn_id: str, events: List[JSON],
-                                 ephemeral: Optional[List[JSON]] = None) -> None:
+    async def handle_transaction(self, txn_id: str, *, events: List[JSON], extra_data: JSON,
+                                 ephemeral: Optional[List[JSON]] = None,
+                                 device_otk_count: Optional[Dict[UserID, DeviceOTKCount]] = None,
+                                 device_lists: Optional[DeviceLists] = None) -> Optional[JSON]:
         for raw_edu in ephemeral or []:
             try:
                 edu = EphemeralEvent.deserialize(raw_edu)
             except SerializerError:
                 self.log.exception("Failed to deserialize ephemeral event %s", raw_edu)
             else:
                 self.handle_matrix_event(edu)
@@ -163,14 +178,15 @@
             try:
                 self._fix_prev_content(raw_event)
                 event = Event.deserialize(raw_event)
             except SerializerError:
                 self.log.exception("Failed to deserialize event %s", raw_event)
             else:
                 self.handle_matrix_event(event)
+        return {}
 
     def handle_matrix_event(self, event: Event) -> None:
         if event.type.is_state and event.state_key is None:
             self.log.debug(f"Not sending {event.event_id} to handlers: expected state_key.")
             return
 
         async def try_handle(handler_func: HandlerFunc):
```

### Comparing `mautrix-0.9.8/mautrix/appservice/state_store/asyncpg.py` & `mautrix-0.9.9/mautrix/appservice/state_store/asyncpg.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/appservice/state_store/file.py` & `mautrix-0.9.9/mautrix/appservice/state_store/file.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/appservice/state_store/memory.py` & `mautrix-0.9.9/mautrix/appservice/state_store/memory.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/appservice/state_store/sqlalchemy.py` & `mautrix-0.9.9/mautrix/appservice/state_store/sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/__init__.py` & `mautrix-0.9.9/mautrix/bridge/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -5,8 +5,8 @@
 from .matrix import BaseMatrixHandler
 from .portal import BasePortal
 from .user import BaseUser
 from .puppet import BasePuppet
 from .bridge import Bridge
 from .notification_disabler import NotificationDisabler
 from .async_getter_lock import async_getter_lock
-from .state import BridgeState
+from mautrix.util.bridge_state import BridgeState
```

### Comparing `mautrix-0.9.8/mautrix/bridge/_community.py` & `mautrix-0.9.9/mautrix/bridge/_community.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/async_getter_lock.py` & `mautrix-0.9.9/mautrix/bridge/async_getter_lock.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/bridge.py` & `mautrix-0.9.9/mautrix/bridge/bridge.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/commands/__init__.py` & `mautrix-0.9.9/mautrix/bridge/commands/__init__.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/commands/admin.py` & `mautrix-0.9.9/mautrix/bridge/commands/admin.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/commands/clean_rooms.py` & `mautrix-0.9.9/mautrix/bridge/commands/clean_rooms.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/commands/crypto.py` & `mautrix-0.9.9/mautrix/bridge/commands/crypto.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/commands/handler.py` & `mautrix-0.9.9/mautrix/bridge/commands/handler.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/commands/login_matrix.py` & `mautrix-0.9.9/mautrix/bridge/commands/login_matrix.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/commands/meta.py` & `mautrix-0.9.9/mautrix/bridge/commands/meta.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/config.py` & `mautrix-0.9.9/mautrix/bridge/config.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/crypto_state_store.py` & `mautrix-0.9.9/mautrix/bridge/crypto_state_store.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/custom_puppet.py` & `mautrix-0.9.9/mautrix/bridge/custom_puppet.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/e2ee.py` & `mautrix-0.9.9/mautrix/bridge/e2ee.py`

 * *Files 2% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 
 try:
     from mautrix.util.async_db import Database
 except ImportError:
     Database = None
 
 if TYPE_CHECKING:
-    from mautrix.bridge import Bridge
+    from mautrix.util.bridge_state import Bridge
 
 
 class EncryptionManager:
     loop: asyncio.AbstractEventLoop
     log: TraceLogger = logging.getLogger("mau.bridge.e2ee")
 
     client: Client
@@ -45,15 +45,14 @@
     state_store: StateStore
 
     bridge: 'Bridge'
     az: AppService
     _id_prefix: str
     _id_suffix: str
 
-    sync_task: asyncio.Future
     _share_session_events: Dict[RoomID, asyncio.Event]
 
     def __init__(self, bridge: 'Bridge', homeserver_address: str, user_id_prefix: str,
                  user_id_suffix: str, db_url: str, key_sharing_config: Dict[str, bool] = None
                  ) -> None:
         self.loop = bridge.loop or asyncio.get_event_loop()
         self.bridge = bridge
@@ -157,19 +156,20 @@
 
     async def decrypt(self, evt: EncryptedEvent, wait_session_timeout: int = 5) -> MessageEvent:
         try:
             decrypted = await self.crypto.decrypt_megolm_event(evt)
         except SessionNotFound as e:
             if not wait_session_timeout:
                 raise
-            self.log.debug(f"Didn't find session {e.session_id},"
-                           f" waiting {wait_session_timeout} seconds for session to arrive")
+            self.log.debug(f"Couldn't find session {e.session_id} trying to decrypt {evt.event_id},"
+                           f" waiting {wait_session_timeout} seconds...")
             got_keys = await self.crypto.wait_for_session(evt.room_id, e.sender_key, e.session_id,
                                                           timeout=wait_session_timeout)
             if got_keys:
+                self.log.debug(f"Got session {e.session_id} after waiting, trying to decrypt {evt.event_id} again")
                 decrypted = await self.crypto.decrypt_megolm_event(evt)
             else:
                 raise
         self.log.trace("Decrypted event %s: %s", evt.event_id, decrypted)
         return decrypted
 
     async def check_server_support(self) -> bool:
@@ -189,19 +189,19 @@
         self.client.api.token = self.az.as_token
         await self.client.login(login_type=LoginType.APPSERVICE, device_name=self.device_name,
                                 device_id=device_id, store_access_token=True, update_hs_url=False)
         await self.crypto.load()
         if not device_id:
             await self.crypto_store.put_device_id(self.client.device_id)
             self.log.debug(f"Logged in with new device ID {self.client.device_id}")
-        self.sync_task = self.client.start(self._filter)
+        _ = self.client.start(self._filter)
         self.log.info("End-to-bridge encryption support is enabled")
 
     async def stop(self) -> None:
-        self.sync_task.cancel()
+        self.client.stop()
         await self.crypto_store.close()
         if self.crypto_db:
             await self.crypto_db.stop()
 
     @property
     def _filter(self) -> Filter:
         all_events = EventType.find("*")
```

### Comparing `mautrix-0.9.8/mautrix/bridge/matrix.py` & `mautrix-0.9.9/mautrix/bridge/matrix.py`

 * *Files 2% similar despite different names*

```diff
@@ -371,60 +371,62 @@
             await self.handle_encrypted_unsupported(evt)
             return
         try:
             decrypted = await self.e2ee.decrypt(evt, wait_session_timeout=5)
         except SessionNotFound as e:
             await self._handle_encrypted_wait(evt, e, wait=10)
         except DecryptionError as e:
-            self.log.warning("Failed to decrypt event %s: %s", evt.event_id, e)
+            self.log.warning(f"Failed to decrypt {evt.event_id}: {e}")
             self.log.trace("%s decryption traceback:", evt.event_id, exc_info=True)
             await self.send_encryption_error_notice(evt, e)
         else:
             await self.int_handle_event(decrypted)
 
     async def handle_encrypted_unsupported(self, evt: EncryptedEvent) -> None:
         self.log.debug("Got encrypted message %s from %s, but encryption is not enabled",
                        evt.event_id, evt.sender)
         await self.az.intent.send_notice(evt.room_id, "🔒️ This bridge has not been configured "
                                                       "to support encryption")
 
     async def _handle_encrypted_wait(self, evt: EncryptedEvent, err: SessionNotFound, wait: int
                                      ) -> None:
-        self.log.warning(f"Didn't find session {err.session_id}, waiting even longer")
+        self.log.debug(f"Couldn't find session {err.session_id} trying to decrypt {evt.event_id}, waiting even longer")
         msg = ("\u26a0 Your message was not bridged: the bridge hasn't received the decryption "
                f"keys. The bridge will retry for {wait} seconds. If this error keeps happening, "
                "try restarting your client.")
         event_id = await self.az.intent.send_notice(evt.room_id, msg)
         got_keys = await self.e2ee.crypto.wait_for_session(evt.room_id, err.sender_key,
                                                            err.session_id, timeout=wait)
         if got_keys:
+            self.log.debug(f"Got session {err.session_id} after waiting more, trying to decrypt {evt.event_id} again")
             try:
                 decrypted = await self.e2ee.decrypt(evt, wait_session_timeout=0)
             except DecryptionError as e:
-                self.log.warning(f"Didn't get {err.session_id}, giving up on {evt.event_id}")
+                self.log.warning(f"Failed to decrypt {evt.event_id}: {e}")
+                self.log.trace("%s decryption traceback:", evt.event_id, exc_info=True)
                 msg = f"\u26a0 Your message was not bridged: {e}"
             else:
                 await self.az.intent.redact(evt.room_id, event_id)
                 await self.int_handle_event(decrypted)
                 return
         else:
+            self.log.warning(f"Didn't get {err.session_id}, giving up on {evt.event_id}")
             msg = ("\u26a0 Your message was not bridged: the bridge hasn't received the decryption "
                    "keys. If this error keeps happening, try restarting your client.")
         content = TextMessageEventContent(msgtype=MessageType.NOTICE, body=msg)
         content.set_edit(event_id)
         await self.az.intent.send_message(evt.room_id, content)
 
     async def handle_encryption(self, evt: StateEvent) -> None:
         await self.az.state_store.set_encryption_info(evt.room_id, evt.content)
         portal = await self.bridge.get_portal(evt.room_id)
         if portal:
             portal.encrypted = True
             await portal.save()
-            # TODO replace with normal attribute access in v0.9
-            if getattr(portal, "is_direct", False):
+            if portal.is_direct:
                 portal.log.debug("Received encryption event in direct portal: %s", evt.content)
                 await portal.enable_dm_encryption()
 
     async def int_handle_event(self, evt: Event) -> None:
         if isinstance(evt, StateEvent) and evt.type == EventType.ROOM_MEMBER and self.e2ee:
             await self.e2ee.handle_member_event(evt)
         if self.filter_matrix_event(evt):
```

### Comparing `mautrix-0.9.8/mautrix/bridge/notification_disabler.py` & `mautrix-0.9.9/mautrix/bridge/notification_disabler.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/portal.py` & `mautrix-0.9.9/mautrix/bridge/portal.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/puppet.py` & `mautrix-0.9.9/mautrix/bridge/puppet.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/state.py` & `mautrix-0.9.9/mautrix/util/bridge_state.py`

 * *Files 17% similar despite different names*

```diff
@@ -12,14 +12,17 @@
 
 from mautrix.types import SerializableAttrs, UserID
 
 
 @dataclass(kw_only=True)
 class BridgeState(SerializableAttrs):
     human_readable_errors: ClassVar[Dict[str, str]] = {}
+    default_error_source: ClassVar[str] = "bridge"
+    default_error_ttl: ClassVar[int] = 60
+    default_ok_ttl: ClassVar[int] = 240
 
     user_id: UserID = None
     remote_id: str = None
     remote_name: str = None
     ok: bool
     timestamp: int = None
     ttl: int = 0
@@ -27,46 +30,47 @@
     error: Optional[str] = None
     message: Optional[str] = None
 
     def fill(self) -> 'BridgeState':
         if not self.timestamp:
             self.timestamp = int(time.time())
         if not self.ok:
-            self.error_source = "bridge"
+            if not self.error_source:
+                self.error_source = self.default_error_source
             try:
                 msg = self.human_readable_errors[self.error]
             except KeyError:
                 pass
             else:
                 self.message = msg.format(message=self.message) if self.message else msg
             if not self.ttl:
-                self.ttl = 60
+                self.ttl = self.default_error_ttl
         else:
             self.error = None
             self.error_source = None
             if not self.ttl:
-                self.ttl = 240
+                self.ttl = self.default_ok_ttl
         return self
 
     def should_deduplicate(self, prev_state: 'BridgeState') -> bool:
         if not prev_state or prev_state.ok != self.ok or prev_state.error != self.error:
             # If there's no previous state or the state was different, send this one.
             return False
         # If there's more than ⅘ of the previous pong's time-to-live left, drop this one
         return prev_state.timestamp + (prev_state.ttl / 5) > self.timestamp
 
-    async def send(self, url: str, token: str, log: logging.Logger) -> None:
+    async def send(self, url: str, token: str, log: logging.Logger, log_sent: bool = True) -> None:
         if not url:
             return
         headers = {"Authorization": f"Bearer {token}"}
         try:
             async with aiohttp.ClientSession() as sess, sess.post(url, json=self.serialize(),
                                                                   headers=headers) as resp:
                 if not 200 <= resp.status < 300:
                     text = await resp.text()
                     text = text.replace("\n", "\\n")
                     log.warning(f"Unexpected status code {resp.status} "
                                 f"sending bridge state update: {text}")
-                else:
+                elif log_sent:
                     log.debug(f"Sent new bridge state {self}")
         except Exception as e:
             log.warning(f"Failed to send updated bridge state: {e}")
```

### Comparing `mautrix-0.9.8/mautrix/bridge/state_store/asyncpg.py` & `mautrix-0.9.9/mautrix/bridge/state_store/asyncpg.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/state_store/sqlalchemy.py` & `mautrix-0.9.9/mautrix/bridge/state_store/sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/bridge/user.py` & `mautrix-0.9.9/mautrix/bridge/user.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,18 +11,18 @@
 
 from mautrix.api import Method, UnstableClientPath
 from mautrix.appservice import AppService
 from mautrix.types import UserID, RoomID, EventType, Membership
 from mautrix.errors import MNotFound
 from mautrix.util.logging import TraceLogger
 from mautrix.util.opt_prometheus import Gauge
+from mautrix.util.bridge_state import BridgeState
 
 from .portal import BasePortal
 from .puppet import BasePuppet
-from .state import BridgeState
 
 if TYPE_CHECKING:
     from .bridge import Bridge
 
 AsmuxPath = UnstableClientPath["com.beeper.asmux"]
```

### Comparing `mautrix-0.9.8/mautrix/client/api/authentication.py` & `mautrix-0.9.9/mautrix/client/api/authentication.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/base.py` & `mautrix-0.9.9/mautrix/client/api/base.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/client.py` & `mautrix-0.9.9/mautrix/client/api/client.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/events.py` & `mautrix-0.9.9/mautrix/client/api/events.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/filtering.py` & `mautrix-0.9.9/mautrix/client/api/filtering.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/modules/__init__.py` & `mautrix-0.9.9/mautrix/client/api/modules/__init__.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/modules/account_data.py` & `mautrix-0.9.9/mautrix/client/api/modules/account_data.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/modules/crypto.py` & `mautrix-0.9.9/mautrix/client/api/modules/crypto.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/modules/media_repository.py` & `mautrix-0.9.9/mautrix/client/api/modules/media_repository.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/modules/misc.py` & `mautrix-0.9.9/mautrix/client/api/modules/misc.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/modules/push_rules.py` & `mautrix-0.9.9/mautrix/client/api/modules/push_rules.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/modules/room_tag.py` & `mautrix-0.9.9/mautrix/client/api/modules/room_tag.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/rooms.py` & `mautrix-0.9.9/mautrix/client/api/rooms.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/api/user_data.py` & `mautrix-0.9.9/mautrix/client/api/user_data.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/client.py` & `mautrix-0.9.9/mautrix/client/client.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/dispatcher.py` & `mautrix-0.9.9/mautrix/client/dispatcher.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/encryption_manager.py` & `mautrix-0.9.9/mautrix/client/encryption_manager.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/abstract.py` & `mautrix-0.9.9/mautrix/client/state_store/abstract.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/asyncpg/store.py` & `mautrix-0.9.9/mautrix/client/state_store/asyncpg/store.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/asyncpg/upgrade.py` & `mautrix-0.9.9/mautrix/client/state_store/asyncpg/upgrade.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/file.py` & `mautrix-0.9.9/mautrix/client/state_store/file.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/memory.py` & `mautrix-0.9.9/mautrix/client/state_store/memory.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/mx_room_state.py` & `mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/mx_room_state.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/mx_user_profile.py` & `mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/mx_user_profile.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/sqlalchemy/sqlstatestore.py` & `mautrix-0.9.9/mautrix/client/state_store/sqlalchemy/sqlstatestore.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/state_store/sync.py` & `mautrix-0.9.9/mautrix/client/state_store/sync.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/store_updater.py` & `mautrix-0.9.9/mautrix/client/store_updater.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/client/syncer.py` & `mautrix-0.9.9/mautrix/client/syncer.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/account.py` & `mautrix-0.9.9/mautrix/crypto/account.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/attachments/async_attachments.py` & `mautrix-0.9.9/mautrix/crypto/attachments/async_attachments.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/attachments/attachments.py` & `mautrix-0.9.9/mautrix/crypto/attachments/attachments.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/base.py` & `mautrix-0.9.9/mautrix/crypto/base.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/decrypt_megolm.py` & `mautrix-0.9.9/mautrix/crypto/decrypt_megolm.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/decrypt_olm.py` & `mautrix-0.9.9/mautrix/crypto/decrypt_olm.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/device_lists.py` & `mautrix-0.9.9/mautrix/crypto/device_lists.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/encrypt_megolm.py` & `mautrix-0.9.9/mautrix/crypto/encrypt_megolm.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/encrypt_olm.py` & `mautrix-0.9.9/mautrix/crypto/encrypt_olm.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/key_request.py` & `mautrix-0.9.9/mautrix/crypto/key_request.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/key_share.py` & `mautrix-0.9.9/mautrix/crypto/key_share.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/machine.py` & `mautrix-0.9.9/mautrix/crypto/machine.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/sessions.py` & `mautrix-0.9.9/mautrix/crypto/sessions.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/store/abstract.py` & `mautrix-0.9.9/mautrix/crypto/store/abstract.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/store/asyncpg/store.py` & `mautrix-0.9.9/mautrix/crypto/store/asyncpg/store.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/store/asyncpg/upgrade.py` & `mautrix-0.9.9/mautrix/crypto/store/asyncpg/upgrade.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/store/memory.py` & `mautrix-0.9.9/mautrix/crypto/store/memory.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/store/pickle.py` & `mautrix-0.9.9/mautrix/crypto/store/pickle.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/crypto/types.py` & `mautrix-0.9.9/mautrix/crypto/types.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/errors/__init__.py` & `mautrix-0.9.9/mautrix/errors/__init__.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/errors/base.py` & `mautrix-0.9.9/mautrix/errors/base.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/errors/crypto.py` & `mautrix-0.9.9/mautrix/errors/crypto.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/errors/request.py` & `mautrix-0.9.9/mautrix/errors/request.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/errors/well_known.py` & `mautrix-0.9.9/mautrix/errors/well_known.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/__init__.py` & `mautrix-0.9.9/mautrix/types/__init__.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/auth.py` & `mautrix-0.9.9/mautrix/types/auth.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/crypto.py` & `mautrix-0.9.9/mautrix/types/crypto.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/__init__.py` & `mautrix-0.9.9/mautrix/types/event/__init__.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/account_data.py` & `mautrix-0.9.9/mautrix/types/event/account_data.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/base.py` & `mautrix-0.9.9/mautrix/types/event/base.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/encrypted.py` & `mautrix-0.9.9/mautrix/types/event/encrypted.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/ephemeral.py` & `mautrix-0.9.9/mautrix/types/event/ephemeral.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/generic.py` & `mautrix-0.9.9/mautrix/types/event/generic.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/message.py` & `mautrix-0.9.9/mautrix/types/event/message.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/reaction.py` & `mautrix-0.9.9/mautrix/types/event/reaction.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/redaction.py` & `mautrix-0.9.9/mautrix/types/event/redaction.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/state.py` & `mautrix-0.9.9/mautrix/types/event/state.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/to_device.py` & `mautrix-0.9.9/mautrix/types/event/to_device.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/type.py` & `mautrix-0.9.9/mautrix/types/event/type.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/type.pyi` & `mautrix-0.9.9/mautrix/types/event/type.pyi`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/event/voip.py` & `mautrix-0.9.9/mautrix/types/event/voip.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/filter.py` & `mautrix-0.9.9/mautrix/types/filter.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/media.py` & `mautrix-0.9.9/mautrix/types/media.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/misc.py` & `mautrix-0.9.9/mautrix/types/misc.py`

 * *Files 7% similar despite different names*

```diff
@@ -9,16 +9,25 @@
 from attr import dataclass
 import attr
 
 from .primitive import RoomID, RoomAlias, SyncToken, ContentURI, UserID
 from .util import SerializableAttrs
 from .event import Event
 
-DeviceLists = NamedTuple("DeviceLists", changed=List[UserID], left=List[UserID])
-DeviceOTKCount = NamedTuple("DeviceOTKCount", curve25519=int, signed_curve25519=int)
+
+@dataclass
+class DeviceLists(SerializableAttrs):
+    changed: List[UserID] = attr.ib(factory=lambda: [])
+    left: List[UserID] = attr.ib(factory=lambda: [])
+
+
+@dataclass
+class DeviceOTKCount(SerializableAttrs):
+    curve25519: int
+    signed_curve25519: int
 
 
 class RoomCreatePreset(Enum):
     """
     Room creation preset, as specified in the `createRoom endpoint`_
 
     .. _createRoom endpoint:
```

### Comparing `mautrix-0.9.8/mautrix/types/primitive.py` & `mautrix-0.9.9/mautrix/types/primitive.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/push_rules.py` & `mautrix-0.9.9/mautrix/types/push_rules.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/users.py` & `mautrix-0.9.9/mautrix/types/users.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/util/enum.py` & `mautrix-0.9.9/mautrix/types/util/enum.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/util/enum_test.py` & `mautrix-0.9.9/mautrix/types/util/enum_test.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/util/obj.py` & `mautrix-0.9.9/mautrix/types/util/obj.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/util/serializable.py` & `mautrix-0.9.9/mautrix/types/util/serializable.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/util/serializable_attrs.py` & `mautrix-0.9.9/mautrix/types/util/serializable_attrs.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/types/util/serializable_attrs_test.py` & `mautrix-0.9.9/mautrix/types/util/serializable_attrs_test.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/async_db/database.py` & `mautrix-0.9.9/mautrix/util/async_db/database.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/async_db/upgrade.py` & `mautrix-0.9.9/mautrix/util/async_db/upgrade.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/config/base.py` & `mautrix-0.9.9/mautrix/util/config/base.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/config/file.py` & `mautrix-0.9.9/mautrix/util/config/file.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/config/proxy.py` & `mautrix-0.9.9/mautrix/util/config/proxy.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/config/recursive_dict.py` & `mautrix-0.9.9/mautrix/util/config/recursive_dict.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/config/string.py` & `mautrix-0.9.9/mautrix/util/config/string.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/config/validation.py` & `mautrix-0.9.9/mautrix/util/config/validation.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/db/base.py` & `mautrix-0.9.9/mautrix/util/db/base.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/file_store.py` & `mautrix-0.9.9/mautrix/util/file_store.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/formatter/__init__.py` & `mautrix-0.9.9/mautrix/util/formatter/__init__.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/formatter/entity_string.py` & `mautrix-0.9.9/mautrix/util/formatter/entity_string.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/formatter/formatted_string.py` & `mautrix-0.9.9/mautrix/util/formatter/formatted_string.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/formatter/html_reader_htmlparser.py` & `mautrix-0.9.9/mautrix/util/formatter/html_reader_htmlparser.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/formatter/markdown_string.py` & `mautrix-0.9.9/mautrix/util/formatter/markdown_string.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/formatter/parser.py` & `mautrix-0.9.9/mautrix/util/formatter/parser.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/logging/color.py` & `mautrix-0.9.9/mautrix/util/logging/color.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/logging/trace.py` & `mautrix-0.9.9/mautrix/util/logging/trace.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/magic.py` & `mautrix-0.9.9/mautrix/util/magic.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/manhole.py` & `mautrix-0.9.9/mautrix/util/manhole.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/markdown.py` & `mautrix-0.9.9/mautrix/util/markdown.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/opt_prometheus.py` & `mautrix-0.9.9/mautrix/util/opt_prometheus.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/opt_prometheus.pyi` & `mautrix-0.9.9/mautrix/util/opt_prometheus.pyi`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/program.py` & `mautrix-0.9.9/mautrix/util/program.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/signed_token.py` & `mautrix-0.9.9/mautrix/util/signed_token.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/simple_lock.py` & `mautrix-0.9.9/mautrix/util/simple_lock.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix/util/simple_template.py` & `mautrix-0.9.9/mautrix/util/simple_template.py`

 * *Files identical despite different names*

### Comparing `mautrix-0.9.8/mautrix.egg-info/PKG-INFO` & `mautrix-0.9.9/mautrix.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mautrix
-Version: 0.9.8
+Version: 0.9.9
 Summary: A Python 3 asyncio Matrix framework.
 Home-page: https://github.com/tulir/mautrix-python
 Author: Tulir Asokan
 Author-email: tulir@maunium.net
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

### Comparing `mautrix-0.9.8/mautrix.egg-info/SOURCES.txt` & `mautrix-0.9.9/mautrix.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 MANIFEST.in
 README.rst
 optional-requirements.txt
 requirements.txt
 setup.py
 mautrix/__init__.py
 mautrix/api.py
+mautrix/py.typed
 mautrix.egg-info/PKG-INFO
 mautrix.egg-info/SOURCES.txt
 mautrix.egg-info/dependency_links.txt
 mautrix.egg-info/requires.txt
 mautrix.egg-info/top_level.txt
 mautrix/appservice/__init__.py
 mautrix/appservice/appservice.py
@@ -30,15 +31,14 @@
 mautrix/bridge/crypto_state_store.py
 mautrix/bridge/custom_puppet.py
 mautrix/bridge/e2ee.py
 mautrix/bridge/matrix.py
 mautrix/bridge/notification_disabler.py
 mautrix/bridge/portal.py
 mautrix/bridge/puppet.py
-mautrix/bridge/state.py
 mautrix/bridge/user.py
 mautrix/bridge/commands/__init__.py
 mautrix/bridge/commands/admin.py
 mautrix/bridge/commands/clean_rooms.py
 mautrix/bridge/commands/crypto.py
 mautrix/bridge/commands/handler.py
 mautrix/bridge/commands/login_matrix.py
@@ -134,14 +134,15 @@
 mautrix/types/util/enum.py
 mautrix/types/util/enum_test.py
 mautrix/types/util/obj.py
 mautrix/types/util/serializable.py
 mautrix/types/util/serializable_attrs.py
 mautrix/types/util/serializable_attrs_test.py
 mautrix/util/__init__.py
+mautrix/util/bridge_state.py
 mautrix/util/color_log.py
 mautrix/util/file_store.py
 mautrix/util/magic.py
 mautrix/util/manhole.py
 mautrix/util/markdown.py
 mautrix/util/opt_prometheus.py
 mautrix/util/opt_prometheus.pyi
```

### Comparing `mautrix-0.9.8/setup.py` & `mautrix-0.9.9/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -35,12 +35,13 @@
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
     ],
 
     package_data={
+        "mautrix": ["py.typed"],
         "mautrix.types.event": ["type.pyi"],
         "mautrix.util": ["opt_prometheus.pyi"],
         "mautrix.util.formatter": ["html_reader.pyi"],
     },
 )
```

