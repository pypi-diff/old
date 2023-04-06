# Comparing `tmp/twnet_parser-0.3.0.tar.gz` & `tmp/twnet_parser-0.3.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "twnet_parser-0.3.0.tar", last modified: Fri Mar 31 08:29:36 2023, max compression
+gzip compressed data, was "twnet_parser-0.3.1.tar", last modified: Thu Apr  6 16:15:43 2023, max compression
```

## Comparing `twnet_parser-0.3.0.tar` & `twnet_parser-0.3.1.tar`

### file list

```diff
@@ -1,91 +1,92 @@
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:36.004325 twnet_parser-0.3.0/
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1324 2023-03-16 13:24:33.000000 twnet_parser-0.3.0/LICENSE.txt
--rw-r--r--   0 chiller   (1000) chiller   (1000)     5123 2023-03-31 08:29:36.004325 twnet_parser-0.3.0/PKG-INFO
--rw-r--r--   0 chiller   (1000) chiller   (1000)     3109 2023-03-31 08:17:23.000000 twnet_parser-0.3.0/README.md
--rw-r--r--   0 chiller   (1000) chiller   (1000)       85 2023-03-16 13:26:21.000000 twnet_parser-0.3.0/pyproject.toml
--rw-r--r--   0 chiller   (1000) chiller   (1000)      758 2023-03-31 08:29:36.004325 twnet_parser-0.3.0/setup.cfg
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:35.997658 twnet_parser-0.3.0/twnet_parser/
--rw-r--r--   0 chiller   (1000) chiller   (1000)        0 2023-03-25 12:29:07.000000 twnet_parser-0.3.0/twnet_parser/__init__.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      991 2023-03-25 14:50:23.000000 twnet_parser-0.3.0/twnet_parser/chunk_header.py
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:35.997658 twnet_parser-0.3.0/twnet_parser/external/
--rw-r--r--   0 chiller   (1000) chiller   (1000)     8373 2023-03-25 15:06:05.000000 twnet_parser-0.3.0/twnet_parser/external/huffman.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      629 2023-03-31 08:21:54.000000 twnet_parser-0.3.0/twnet_parser/message_parser.py
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:35.994325 twnet_parser-0.3.0/twnet_parser/messages7/
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:36.000991 twnet_parser-0.3.0/twnet_parser/messages7/game/
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1273 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_call_vote.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      982 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_command.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      854 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_emoticon.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      652 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_kill.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      667 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_ready_change.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1131 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_say.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1049 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_set_spectator_mode.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      833 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_set_team.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1335 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_skin_change.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1770 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_start_info.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      803 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/cl_vote.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1148 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/de_client_enter.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1143 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/de_client_leave.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      836 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_broadcast.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1305 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_chat.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      815 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_checkpoint.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1154 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_client_drop.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     2385 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_client_info.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1166 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_command_info.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      839 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_command_info_remove.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1011 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_emoticon.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      890 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_extra_projectile.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1528 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_game_info.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      659 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_game_msg.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1276 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_kill_msg.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      826 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_motd.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1491 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_race_finish.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      670 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_ready_to_enter.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1703 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_server_settings.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1492 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_skin_change.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1313 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_team.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     7581 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_tune_params.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      678 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_clear_options.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      866 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_option_add.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      681 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_option_list_add.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      872 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_option_remove.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1472 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_set.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1207 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_status.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      853 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/game/sv_weapon_pickup.py
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:36.004325 twnet_parser-0.3.0/twnet_parser/messages7/system/
--rw-r--r--   0 chiller   (1000) chiller   (1000)      655 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/con_ready.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      657 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/enter_game.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1242 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/info.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1349 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/input.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1024 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/input_timing.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1656 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/map_change.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      763 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/map_data.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      829 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/maplist_entry_add.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      829 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/maplist_entry_rem.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      646 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/ping.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      657 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/ping_reply.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      834 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_auth.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      662 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_auth_off.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      660 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_auth_on.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      807 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_cmd.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1109 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_cmd_add.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      819 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_cmd_rem.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      814 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_line.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      648 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/ready.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      668 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/request_map_data.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      769 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/server_info.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1507 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/snap.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      970 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/snap_empty.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1231 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/messages7/system/snap_single.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     1648 2023-03-31 08:13:33.000000 twnet_parser-0.3.0/twnet_parser/msg7.py
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:36.004325 twnet_parser-0.3.0/twnet_parser/msg_matcher/
--rw-r--r--   0 chiller   (1000) chiller   (1000)     7692 2023-03-31 08:25:11.000000 twnet_parser-0.3.0/twnet_parser/msg_matcher/game7.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     4599 2023-03-31 08:19:17.000000 twnet_parser-0.3.0/twnet_parser/msg_matcher/system7.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      275 2023-03-26 10:26:20.000000 twnet_parser-0.3.0/twnet_parser/net_message.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     3295 2023-03-26 09:17:35.000000 twnet_parser-0.3.0/twnet_parser/packer.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)     6157 2023-03-25 15:01:59.000000 twnet_parser-0.3.0/twnet_parser/packet.py
--rw-r--r--   0 chiller   (1000) chiller   (1000)      222 2023-03-25 13:17:57.000000 twnet_parser-0.3.0/twnet_parser/pretty_print.py
-drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-03-31 08:29:35.997658 twnet_parser-0.3.0/twnet_parser.egg-info/
--rw-r--r--   0 chiller   (1000) chiller   (1000)     5123 2023-03-31 08:29:35.000000 twnet_parser-0.3.0/twnet_parser.egg-info/PKG-INFO
--rw-r--r--   0 chiller   (1000) chiller   (1000)     3337 2023-03-31 08:29:35.000000 twnet_parser-0.3.0/twnet_parser.egg-info/SOURCES.txt
--rw-r--r--   0 chiller   (1000) chiller   (1000)        1 2023-03-31 08:29:35.000000 twnet_parser-0.3.0/twnet_parser.egg-info/dependency_links.txt
--rw-r--r--   0 chiller   (1000) chiller   (1000)       13 2023-03-31 08:29:35.000000 twnet_parser-0.3.0/twnet_parser.egg-info/top_level.txt
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.458241 twnet_parser-0.3.1/
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1324 2023-03-16 13:24:33.000000 twnet_parser-0.3.1/LICENSE.txt
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     3673 2023-04-06 16:15:43.458241 twnet_parser-0.3.1/PKG-INFO
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     3121 2023-04-06 16:10:36.000000 twnet_parser-0.3.1/README.md
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      678 2023-04-06 16:15:39.000000 twnet_parser-0.3.1/pyproject.toml
+-rw-r--r--   0 chiller   (1000) chiller   (1000)       38 2023-04-06 16:15:43.458241 twnet_parser-0.3.1/setup.cfg
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.448241 twnet_parser-0.3.1/twnet_parser/
+-rw-r--r--   0 chiller   (1000) chiller   (1000)        0 2023-03-25 12:29:07.000000 twnet_parser-0.3.1/twnet_parser/__init__.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      991 2023-03-25 14:50:23.000000 twnet_parser-0.3.1/twnet_parser/chunk_header.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      207 2023-04-06 15:01:21.000000 twnet_parser-0.3.1/twnet_parser/ctrl_message.py
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.448241 twnet_parser-0.3.1/twnet_parser/external/
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     8373 2023-03-25 15:06:05.000000 twnet_parser-0.3.1/twnet_parser/external/huffman.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      629 2023-03-31 08:21:54.000000 twnet_parser-0.3.1/twnet_parser/message_parser.py
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.448241 twnet_parser-0.3.1/twnet_parser/messages7/
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.454908 twnet_parser-0.3.1/twnet_parser/messages7/game/
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1273 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_call_vote.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      982 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_command.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      854 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_emoticon.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      577 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_kill.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      592 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_ready_change.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1131 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_say.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1049 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_set_spectator_mode.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      833 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_set_team.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1335 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_skin_change.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1770 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_start_info.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      803 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/cl_vote.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1148 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/de_client_enter.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1143 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/de_client_leave.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      836 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_broadcast.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1305 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_chat.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      815 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_checkpoint.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1154 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_client_drop.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     2385 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_client_info.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1166 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_command_info.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      839 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_command_info_remove.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1011 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_emoticon.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      890 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_extra_projectile.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1528 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_game_info.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      584 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_game_msg.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1276 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_kill_msg.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      826 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_motd.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1491 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_race_finish.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      595 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_ready_to_enter.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1703 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_server_settings.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1492 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_skin_change.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1313 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_team.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     7501 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_tune_params.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      603 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_clear_options.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      866 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_option_add.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      606 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_option_list_add.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      872 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_option_remove.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1472 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_set.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1207 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_status.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      853 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/game/sv_weapon_pickup.py
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.458241 twnet_parser-0.3.1/twnet_parser/messages7/system/
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      580 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/con_ready.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      582 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/enter_game.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1237 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/info.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1349 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/input.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1024 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/input_timing.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1656 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/map_change.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      763 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/map_data.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      829 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/maplist_entry_add.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      829 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/maplist_entry_rem.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      571 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/ping.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      582 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/ping_reply.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      834 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_auth.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      587 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_auth_off.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      585 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_auth_on.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      807 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_cmd.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1109 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_cmd_add.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      819 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_cmd_rem.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      814 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_line.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      573 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/ready.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      593 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/request_map_data.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      769 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/server_info.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1507 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/snap.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      970 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/snap_empty.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1231 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/messages7/system/snap_single.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     1784 2023-04-02 18:36:07.000000 twnet_parser-0.3.1/twnet_parser/msg7.py
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.458241 twnet_parser-0.3.1/twnet_parser/msg_matcher/
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     7692 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/msg_matcher/game7.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     4599 2023-04-02 18:03:38.000000 twnet_parser-0.3.1/twnet_parser/msg_matcher/system7.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      275 2023-03-26 10:26:20.000000 twnet_parser-0.3.1/twnet_parser/net_message.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     3295 2023-03-26 09:17:35.000000 twnet_parser-0.3.1/twnet_parser/packer.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     6164 2023-04-06 15:00:48.000000 twnet_parser-0.3.1/twnet_parser/packet.py
+-rw-r--r--   0 chiller   (1000) chiller   (1000)      222 2023-03-25 13:17:57.000000 twnet_parser-0.3.1/twnet_parser/pretty_print.py
+drwxr-xr-x   0 chiller   (1000) chiller   (1000)        0 2023-04-06 16:15:43.448241 twnet_parser-0.3.1/twnet_parser.egg-info/
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     3673 2023-04-06 16:15:43.000000 twnet_parser-0.3.1/twnet_parser.egg-info/PKG-INFO
+-rw-r--r--   0 chiller   (1000) chiller   (1000)     3356 2023-04-06 16:15:43.000000 twnet_parser-0.3.1/twnet_parser.egg-info/SOURCES.txt
+-rw-r--r--   0 chiller   (1000) chiller   (1000)        1 2023-04-06 16:15:43.000000 twnet_parser-0.3.1/twnet_parser.egg-info/dependency_links.txt
+-rw-r--r--   0 chiller   (1000) chiller   (1000)       13 2023-04-06 16:15:43.000000 twnet_parser-0.3.1/twnet_parser.egg-info/top_level.txt
```

### Comparing `twnet_parser-0.3.0/LICENSE.txt` & `twnet_parser-0.3.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/README.md` & `twnet_parser-0.3.1/README.md`

 * *Files 14% similar despite different names*

```diff
@@ -28,20 +28,20 @@
 ```
 
 ## Features
 
 | Feature                        | Status             |
 | ------------------------------ | ------------------ |
 | Deserialize 0.7 packet headers | :heavy_check_mark: |
-| Deserialize 0.7 chunk headers  |                    |
-| Deserialize 0.7 messages       |                    |
+| Deserialize 0.7 chunk headers  | :heavy_check_mark: |
+| Deserialize 0.7 messages       | 70%                |
 | Deserialize 0.7 snapshots      |                    |
 | Serialize 0.7 packet headers   |                    |
 | Serialize 0.7 chunk headers    |                    |
-| Serialize 0.7 messages         |                    |
+| Serialize 0.7 messages         | 70%                |
 | Deserialize 0.6 packet headers |                    |
 | Deserialize 0.6 chunk headers  |                    |
 | Deserialize 0.6 messages       |                    |
 | Deserialize 0.6 snapshots      |                    |
 | Serialize 0.6 packet headers   |                    |
 | Serialize 0.6 chunk headers    |                    |
 | Serialize 0.6 messages         |                    |
@@ -83,15 +83,15 @@
 
 ## package and release
 
 ```bash
 # manual
 pip install -r requirements/dev.txt
 version=0.0.2
-sed "s/^version =.*/version = $version/" setup.cfg
+sed -i "s/^version =.*/version = \"$version\"/" pyproject.toml
 python -m build
 git tag -a "v$version" -m "# version $version"
 python -m twine upload dist/*
 
 # or use the interactive convience script
 ./scripts/release.sh
 ```
```

### Comparing `twnet_parser-0.3.0/twnet_parser/chunk_header.py` & `twnet_parser-0.3.1/twnet_parser/chunk_header.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/external/huffman.py` & `twnet_parser-0.3.1/twnet_parser/external/huffman.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/message_parser.py` & `twnet_parser-0.3.1/twnet_parser/message_parser.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_call_vote.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_call_vote.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_command.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_command.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_emoticon.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_emoticon.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_kill.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_vote.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
+from twnet_parser.packer import pack_int
 
-class MsgClKill(PrettyPrint):
+class MsgClVote(PrettyPrint):
     def __init__(
             self,
-
+            vote: int = 0
     ) -> None:
-        self.message_name = 'cl_kill'
+        self.message_name = 'cl_vote'
         self.system_message = False
         self.header: ChunkHeader
 
+        self.vote: int = vote
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
+        self.vote = unpacker.get_int()
         return True
 
     def pack(self) -> bytes:
-        return b''
+        return pack_int(self.vote)
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_ready_change.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_auth.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
+from twnet_parser.packer import pack_str
 
-class MsgClReadyChange(PrettyPrint):
+class MsgRconAuth(PrettyPrint):
     def __init__(
             self,
-
+            password: str = 'default'
     ) -> None:
-        self.message_name = 'cl_ready_change'
-        self.system_message = False
+        self.message_name = 'rcon_auth'
+        self.system_message = True
         self.header: ChunkHeader
 
+        self.password: str = password
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
+        self.password = unpacker.get_str()
         return True
 
     def pack(self) -> bytes:
-        return b''
+        return pack_str(self.password)
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_say.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_say.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_set_spectator_mode.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_set_spectator_mode.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_set_team.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_set_team.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_skin_change.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_skin_change.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_start_info.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/cl_start_info.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/cl_vote.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_cmd_rem.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
-from twnet_parser.packer import pack_int
+from twnet_parser.packer import pack_str
 
-class MsgClVote(PrettyPrint):
+class MsgRconCmdRem(PrettyPrint):
     def __init__(
             self,
-            vote: int = 0
+            name: str = 'default'
     ) -> None:
-        self.message_name = 'cl_vote'
-        self.system_message = False
+        self.message_name = 'rcon_cmd_rem'
+        self.system_message = True
         self.header: ChunkHeader
 
-        self.vote: int = vote
+        self.name: str = name
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
-        self.vote = unpacker.get_int()
+        self.name = unpacker.get_str()
         return True
 
     def pack(self) -> bytes:
-        return pack_int(self.vote)
+        return pack_str(self.name)
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/de_client_enter.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/de_client_enter.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/de_client_leave.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/de_client_leave.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_broadcast.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_broadcast.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_chat.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_chat.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_checkpoint.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_checkpoint.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_client_drop.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_client_drop.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_client_info.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_client_info.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_command_info.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_command_info.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_command_info_remove.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_command_info_remove.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_emoticon.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_emoticon.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_extra_projectile.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_extra_projectile.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_game_info.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_game_info.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_game_msg.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/ping.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,25 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgSvGameMsg(PrettyPrint):
+class MsgPing(PrettyPrint):
     def __init__(
             self,
 
     ) -> None:
-        self.message_name = 'sv_game_msg'
-        self.system_message = False
+        self.message_name = 'ping'
+        self.system_message = True
         self.header: ChunkHeader
 
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
         return True
 
     def pack(self) -> bytes:
         return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_kill_msg.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_kill_msg.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_motd.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_motd.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_race_finish.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_race_finish.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_ready_to_enter.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_weapon_pickup.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
+from twnet_parser.packer import pack_int
 
-class MsgSvReadyToEnter(PrettyPrint):
+class MsgSvWeaponPickup(PrettyPrint):
     def __init__(
             self,
-
+            weapon: int = 0
     ) -> None:
-        self.message_name = 'sv_ready_to_enter'
+        self.message_name = 'sv_weapon_pickup'
         self.system_message = False
         self.header: ChunkHeader
 
+        self.weapon: int = weapon
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
+        self.weapon = unpacker.get_int() # TODO: this is a enum
         return True
 
     def pack(self) -> bytes:
-        return b''
+        return pack_int(self.weapon)
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_server_settings.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_server_settings.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_skin_change.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_skin_change.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_team.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_team.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_clear_options.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/map_data.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,25 +1,27 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgSvVoteClearOptions(PrettyPrint):
+class MsgMapData(PrettyPrint):
     def __init__(
             self,
-
+            data: bytes = b'\x00'
     ) -> None:
-        self.message_name = 'sv_vote_clear_options'
-        self.system_message = False
+        self.message_name = 'map_data'
+        self.system_message = True
         self.header: ChunkHeader
 
+        self.data: bytes = data
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
+        self.data = unpacker.get_raw()
         return True
 
     def pack(self) -> bytes:
-        return b''
+        return self.data
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_option_add.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_option_add.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_option_remove.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_option_remove.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_set.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_set.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_vote_status.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_status.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/game/sv_weapon_pickup.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_line.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
-from twnet_parser.packer import pack_int
+from twnet_parser.packer import pack_str
 
-class MsgSvWeaponPickup(PrettyPrint):
+class MsgRconLine(PrettyPrint):
     def __init__(
             self,
-            weapon: int = 0
+            line: str = 'default'
     ) -> None:
-        self.message_name = 'sv_weapon_pickup'
-        self.system_message = False
+        self.message_name = 'rcon_line'
+        self.system_message = True
         self.header: ChunkHeader
 
-        self.weapon: int = weapon
+        self.line: str = line
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
-        self.weapon = unpacker.get_int() # TODO: this is a enum
+        self.line = unpacker.get_str()
         return True
 
     def pack(self) -> bytes:
-        return pack_int(self.weapon)
+        return pack_str(self.line)
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/con_ready.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/maplist_entry_add.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
+from twnet_parser.packer import pack_str
 
-class MsgConReady(PrettyPrint):
+class MsgMaplistEntryAdd(PrettyPrint):
     def __init__(
             self,
-
+            name: str = 'default'
     ) -> None:
-        self.message_name = 'con_ready'
+        self.message_name = 'maplist_entry_add'
         self.system_message = True
         self.header: ChunkHeader
 
+        self.name: str = name
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
+        self.name = unpacker.get_str()
         return True
 
     def pack(self) -> bytes:
-        return b''
+        return pack_str(self.name)
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/enter_game.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/con_ready.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,25 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgEnterGame(PrettyPrint):
+class MsgConReady(PrettyPrint):
     def __init__(
             self,
 
     ) -> None:
-        self.message_name = 'enter_game'
+        self.message_name = 'con_ready'
         self.system_message = True
         self.header: ChunkHeader
 
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
         return True
 
     def pack(self) -> bytes:
         return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/info.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/info.py`

 * *Files 12% similar despite different names*

```diff
@@ -5,32 +5,32 @@
 from twnet_parser.chunk_header import ChunkHeader
 from twnet_parser.packer import pack_int, pack_str
 
 class MsgInfo(PrettyPrint):
     def __init__(
             self,
             version: str = 'default',
-            password: int = 0,
+            password: str = '',
             client_version: int = 0
     ) -> None:
         self.message_name = 'info'
         self.system_message = True
         self.header: ChunkHeader
 
         self.version: str = version
-        self.password: int = password
+        self.password: str = password
         self.client_version: int = client_version
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
         unpacker = Unpacker(data)
         self.version = unpacker.get_str()
-        self.password = unpacker.get_int() # TODO: this is a optional of type any
-        self.client_version = unpacker.get_int() # TODO: this is a optional of type any
+        self.password = unpacker.get_str() # TODO: this can fail for optionals
+        self.client_version = unpacker.get_int() # TODO: this can fail for optionals
         return True
 
     def pack(self) -> bytes:
         return pack_str(self.version) + \
-            pack_int(self.password) + \
+            pack_str(self.password) + \
             pack_int(self.client_version)
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/input.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/input.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/input_timing.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/input_timing.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/map_change.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/map_change.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/map_data.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/server_info.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgMapData(PrettyPrint):
+class MsgServerInfo(PrettyPrint):
     def __init__(
             self,
             data: bytes = b'\x00'
     ) -> None:
-        self.message_name = 'map_data'
+        self.message_name = 'server_info'
         self.system_message = True
         self.header: ChunkHeader
 
         self.data: bytes = data
 
     # first byte of data
     # has to be the first byte of the message payload
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/maplist_entry_add.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/maplist_entry_rem.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 from twnet_parser.packer import pack_str
 
-class MsgMaplistEntryAdd(PrettyPrint):
+class MsgMaplistEntryRem(PrettyPrint):
     def __init__(
             self,
             name: str = 'default'
     ) -> None:
-        self.message_name = 'maplist_entry_add'
+        self.message_name = 'maplist_entry_rem'
         self.system_message = True
         self.header: ChunkHeader
 
         self.name: str = name
 
     # first byte of data
     # has to be the first byte of the message payload
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/maplist_entry_rem.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_auth_off.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,28 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
-from twnet_parser.packer import pack_str
 
-class MsgMaplistEntryRem(PrettyPrint):
+class MsgRconAuthOff(PrettyPrint):
     def __init__(
             self,
-            name: str = 'default'
+
     ) -> None:
-        self.message_name = 'maplist_entry_rem'
+        self.message_name = 'rcon_auth_off'
         self.system_message = True
         self.header: ChunkHeader
 
-        self.name: str = name
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
-        self.name = unpacker.get_str()
         return True
 
     def pack(self) -> bytes:
-        return pack_str(self.name)
+        return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/ping.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_game_msg.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,25 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgPing(PrettyPrint):
+class MsgSvGameMsg(PrettyPrint):
     def __init__(
             self,
 
     ) -> None:
-        self.message_name = 'ping'
-        self.system_message = True
+        self.message_name = 'sv_game_msg'
+        self.system_message = False
         self.header: ChunkHeader
 
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
         return True
 
     def pack(self) -> bytes:
         return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/ping_reply.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/ready.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,25 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgPingReply(PrettyPrint):
+class MsgReady(PrettyPrint):
     def __init__(
             self,
 
     ) -> None:
-        self.message_name = 'ping_reply'
+        self.message_name = 'ready'
         self.system_message = True
         self.header: ChunkHeader
 
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
         return True
 
     def pack(self) -> bytes:
         return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_auth_off.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/ping_reply.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,25 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgRconAuthOff(PrettyPrint):
+class MsgPingReply(PrettyPrint):
     def __init__(
             self,
 
     ) -> None:
-        self.message_name = 'rcon_auth_off'
+        self.message_name = 'ping_reply'
         self.system_message = True
         self.header: ChunkHeader
 
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
         return True
 
     def pack(self) -> bytes:
         return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_auth_on.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_auth_on.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,11 +1,10 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
 class MsgRconAuthOn(PrettyPrint):
     def __init__(
             self,
 
     ) -> None:
@@ -14,12 +13,11 @@
         self.header: ChunkHeader
 
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
         return True
 
     def pack(self) -> bytes:
         return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_cmd.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_cmd.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_cmd_add.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/rcon_cmd_add.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_cmd_rem.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_clear_options.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,28 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
-from twnet_parser.packer import pack_str
 
-class MsgRconCmdRem(PrettyPrint):
+class MsgSvVoteClearOptions(PrettyPrint):
     def __init__(
             self,
-            name: str = 'default'
+
     ) -> None:
-        self.message_name = 'rcon_cmd_rem'
-        self.system_message = True
+        self.message_name = 'sv_vote_clear_options'
+        self.system_message = False
         self.header: ChunkHeader
 
-        self.name: str = name
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
-        self.name = unpacker.get_str()
         return True
 
     def pack(self) -> bytes:
-        return pack_str(self.name)
+        return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/rcon_line.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/request_map_data.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,28 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
-from twnet_parser.packer import pack_str
 
-class MsgRconLine(PrettyPrint):
+class MsgRequestMapData(PrettyPrint):
     def __init__(
             self,
-            line: str = 'default'
+
     ) -> None:
-        self.message_name = 'rcon_line'
+        self.message_name = 'request_map_data'
         self.system_message = True
         self.header: ChunkHeader
 
-        self.line: str = line
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
-        self.line = unpacker.get_str()
         return True
 
     def pack(self) -> bytes:
-        return pack_str(self.line)
+        return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/request_map_data.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_vote_option_list_add.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,25 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgRequestMapData(PrettyPrint):
+class MsgSvVoteOptionListAdd(PrettyPrint):
     def __init__(
             self,
 
     ) -> None:
-        self.message_name = 'request_map_data'
-        self.system_message = True
+        self.message_name = 'sv_vote_option_list_add'
+        self.system_message = False
         self.header: ChunkHeader
 
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
         return True
 
     def pack(self) -> bytes:
         return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/server_info.py` & `twnet_parser-0.3.1/twnet_parser/messages7/game/sv_ready_to_enter.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,27 +1,23 @@
 # generated by scripts/generate_messages.py
 
 from twnet_parser.pretty_print import PrettyPrint
-from twnet_parser.packer import Unpacker
 from twnet_parser.chunk_header import ChunkHeader
 
-class MsgServerInfo(PrettyPrint):
+class MsgSvReadyToEnter(PrettyPrint):
     def __init__(
             self,
-            data: bytes = b'\x00'
+
     ) -> None:
-        self.message_name = 'server_info'
-        self.system_message = True
+        self.message_name = 'sv_ready_to_enter'
+        self.system_message = False
         self.header: ChunkHeader
 
-        self.data: bytes = data
 
     # first byte of data
     # has to be the first byte of the message payload
     # NOT the chunk header and NOT the message id
     def unpack(self, data: bytes) -> bool:
-        unpacker = Unpacker(data)
-        self.data = unpacker.get_raw()
         return True
 
     def pack(self) -> bytes:
-        return self.data
+        return b''
```

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/snap.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/snap.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/snap_empty.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/snap_empty.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/messages7/system/snap_single.py` & `twnet_parser-0.3.1/twnet_parser/messages7/system/snap_single.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/msg7.py` & `twnet_parser-0.3.1/twnet_parser/msg7.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,7 +1,16 @@
+# control
+
+CTRL_KEEPALIVE = 0
+CTRL_CONNECT = 1
+CTRL_ACCEPT = 2
+# yes control message 3 is missing in 0.7
+CTRL_CLOSE = 4
+CTRL_TOKEN = 5
+
 # system
 NULL = 0
 INFO = 1
 MAP_CHANGE = 2 # sent when client should switch map
 MAP_DATA = 3   # map transfer, contains a chunk of the map file
 SERVER_INFO = 4
 CON_READY = 5  # connection is ready, client should send start info
```

### Comparing `twnet_parser-0.3.0/twnet_parser/msg_matcher/game7.py` & `twnet_parser-0.3.1/twnet_parser/msg_matcher/game7.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/msg_matcher/system7.py` & `twnet_parser-0.3.1/twnet_parser/msg_matcher/system7.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/packer.py` & `twnet_parser-0.3.1/twnet_parser/packer.py`

 * *Files identical despite different names*

### Comparing `twnet_parser-0.3.0/twnet_parser/packet.py` & `twnet_parser-0.3.1/twnet_parser/packet.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,15 +3,17 @@
 from typing import Union
 from typing import cast
 
 from twnet_parser import packer
 from twnet_parser.pretty_print import PrettyPrint
 from twnet_parser.message_parser import MessageParser
 from twnet_parser.net_message import NetMessage
+from twnet_parser.ctrl_message import CtrlMessage
 from twnet_parser.chunk_header import ChunkHeader, ChunkFlags
+from twnet_parser.msg_matcher.control7 import match_control7
 
 from twnet_parser.external.huffman import huffman
 
 # TODO: what is a nice pythonic way of storing those?
 #       also does some version:: namespace thing make sense?
 PACKETFLAG7_CONTROL = 1
 PACKETFLAG7_RESEND = 2
@@ -19,18 +21,14 @@
 PACKETFLAG7_CONNLESS = 8
 
 CHUNKFLAG7_VITAL = 1
 CHUNKFLAG7_RESEND = 2
 
 PACKET_HEADER7_SIZE = 7
 
-class CtrlMessage(PrettyPrint):
-    def __init__(self, name: str) -> None:
-        self.message_name: str = name
-
 class PacketFlags7(PrettyPrint):
     def __init__(self):
         self.control = False
         self.resend = False
         self.compression = False
         self.connless = False
 
@@ -144,36 +142,34 @@
         if sys:
             msg = MessageParser().parse_sys_message(msg_id, data[i:])
         else:
             msg = MessageParser().parse_game_message(msg_id, data[i:])
         msg.header = chunk_header
         return msg
 
-    def parse7(self, data: bytes) -> TwPacket:
+    def parse7(self, data: bytes, client: bool) -> TwPacket:
         pck = TwPacket()
         pck.version = '0.7'
         # TODO: what is the most performant way in python to do this?
         #       heap allocating a PacketHeaderParser7 just to bundle a bunch of
         #       methods that do not share state seems like a waste of performance
         #       would this be nicer with class methods?
         pck.header = PacketHeaderParser7().parse_header(data)
         pck.payload_raw = data[PACKET_HEADER7_SIZE:]
         pck.payload_decompressed = pck.payload_raw
         if pck.header.flags.control:
-            if data[7] == 0x04: # close
-                msg_dc = CtrlMessage('close')
-                pck.messages.append(msg_dc)
-                return pck
-        else:
-            if pck.header.flags.compression:
-                payload = bytearray(pck.payload_raw)
-                pck.payload_decompressed = huffman.decompress(payload)
-            pck.messages = cast(
-                    list[Union[CtrlMessage, NetMessage]],
-                    self.get_messages(pck.payload_decompressed))
+            ctrl_msg: CtrlMessage = match_control7(data[7], data[8:], client)
+            pck.messages.append(ctrl_msg)
+            return pck
+        if pck.header.flags.compression:
+            payload = bytearray(pck.payload_raw)
+            pck.payload_decompressed = huffman.decompress(payload)
+        pck.messages = cast(
+                list[Union[CtrlMessage, NetMessage]],
+                self.get_messages(pck.payload_decompressed))
         return pck
 
 def parse6(data: bytes) -> TwPacket:
     raise NotImplementedError()
 
-def parse7(data: bytes) -> TwPacket:
-    return PacketParser().parse7(data)
+def parse7(data: bytes, we_are_a_client: bool = False) -> TwPacket:
+    return PacketParser().parse7(data, we_are_a_client)
```

### Comparing `twnet_parser-0.3.0/twnet_parser.egg-info/SOURCES.txt` & `twnet_parser-0.3.1/twnet_parser.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 LICENSE.txt
 README.md
 pyproject.toml
-setup.cfg
 twnet_parser/__init__.py
 twnet_parser/chunk_header.py
+twnet_parser/ctrl_message.py
 twnet_parser/message_parser.py
 twnet_parser/msg7.py
 twnet_parser/net_message.py
 twnet_parser/packer.py
 twnet_parser/packet.py
 twnet_parser/pretty_print.py
 twnet_parser.egg-info/PKG-INFO
```

