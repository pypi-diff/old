# Comparing `tmp/vmas-1.2.8.tar.gz` & `tmp/vmas-1.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vmas-1.2.8.tar", last modified: Mon Mar 20 13:33:53 2023, max compression
+gzip compressed data, was "vmas-1.2.9.tar", last modified: Thu Apr  6 08:30:25 2023, max compression
```

## Comparing `vmas-1.2.8.tar` & `vmas-1.2.9.tar`

### file list

```diff
@@ -1,78 +1,78 @@
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.744927 vmas-1.2.8/
--rw-r--r--   0 Matteo     (501) staff       (20)    35149 2022-11-19 11:21:06.000000 vmas-1.2.8/LICENSE
--rw-r--r--   0 Matteo     (501) staff       (20)       35 2023-01-23 16:01:21.000000 vmas-1.2.8/MANIFEST.in
--rw-r--r--   0 Matteo     (501) staff       (20)      254 2023-03-20 13:33:53.745007 vmas-1.2.8/PKG-INFO
--rw-r--r--   0 Matteo     (501) staff       (20)    59944 2023-03-20 13:22:40.000000 vmas-1.2.8/README.md
--rw-r--r--   0 Matteo     (501) staff       (20)      103 2023-03-20 13:33:53.745249 vmas-1.2.8/setup.cfg
--rw-r--r--   0 Matteo     (501) staff       (20)      533 2023-03-20 13:33:44.000000 vmas-1.2.8/setup.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.726994 vmas-1.2.8/vmas/
--rw-r--r--   0 Matteo     (501) staff       (20)     1357 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/__init__.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.728420 vmas-1.2.8/vmas/examples/
--rw-r--r--   0 Matteo     (501) staff       (20)       89 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/examples/__init__.py
--rw-r--r--   0 Matteo     (501) staff       (20)     5731 2023-03-10 08:34:41.000000 vmas-1.2.8/vmas/examples/rllib.py
--rw-r--r--   0 Matteo     (501) staff       (20)     2374 2023-03-20 12:34:04.000000 vmas-1.2.8/vmas/examples/run_heuristic.py
--rw-r--r--   0 Matteo     (501) staff       (20)     2768 2023-03-20 11:43:23.000000 vmas-1.2.8/vmas/examples/use_vmas_env.py
--rw-r--r--   0 Matteo     (501) staff       (20)    10389 2023-03-10 08:34:41.000000 vmas-1.2.8/vmas/interactive_rendering.py
--rw-r--r--   0 Matteo     (501) staff       (20)     1946 2023-03-20 12:40:41.000000 vmas-1.2.8/vmas/make_env.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.733080 vmas-1.2.8/vmas/scenarios/
--rw-r--r--   0 Matteo     (501) staff       (20)      775 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/__init__.py
--rw-r--r--   0 Matteo     (501) staff       (20)     9490 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/balance.py
--rw-r--r--   0 Matteo     (501) staff       (20)    13749 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/ball_passage.py
--rw-r--r--   0 Matteo     (501) staff       (20)     7901 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/ball_trajectory.py
--rw-r--r--   0 Matteo     (501) staff       (20)     9931 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/buzz_wire.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.734233 vmas-1.2.8/vmas/scenarios/debug/
--rw-r--r--   0 Matteo     (501) staff       (20)       89 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/debug/__init__.py
--rw-r--r--   0 Matteo     (501) staff       (20)    10109 2023-02-06 14:26:05.000000 vmas-1.2.8/vmas/scenarios/debug/asym_joint.py
--rw-r--r--   0 Matteo     (501) staff       (20)     6879 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/debug/circle_trajectory.py
--rw-r--r--   0 Matteo     (501) staff       (20)     8819 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/debug/goal.py
--rw-r--r--   0 Matteo     (501) staff       (20)     3775 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/debug/het_mass.py
--rw-r--r--   0 Matteo     (501) staff       (20)     4577 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/debug/line_trajectory.py
--rw-r--r--   0 Matteo     (501) staff       (20)     5513 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/debug/vel_control.py
--rw-r--r--   0 Matteo     (501) staff       (20)     5164 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/debug/waterfall.py
--rw-r--r--   0 Matteo     (501) staff       (20)    13511 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/discovery.py
--rw-r--r--   0 Matteo     (501) staff       (20)     5315 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/dispersion.py
--rw-r--r--   0 Matteo     (501) staff       (20)     4858 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/dropout.py
--rw-r--r--   0 Matteo     (501) staff       (20)     6197 2023-03-20 09:57:19.000000 vmas-1.2.8/vmas/scenarios/flocking.py
--rw-r--r--   0 Matteo     (501) staff       (20)    64259 2023-03-10 08:34:41.000000 vmas-1.2.8/vmas/scenarios/football.py
--rw-r--r--   0 Matteo     (501) staff       (20)    19240 2023-03-20 09:57:19.000000 vmas-1.2.8/vmas/scenarios/give_way.py
--rw-r--r--   0 Matteo     (501) staff       (20)    27794 2023-03-20 09:57:19.000000 vmas-1.2.8/vmas/scenarios/joint_passage.py
--rw-r--r--   0 Matteo     (501) staff       (20)    26899 2023-03-20 09:57:19.000000 vmas-1.2.8/vmas/scenarios/joint_passage_size.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.741236 vmas-1.2.8/vmas/scenarios/mpe/
--rw-r--r--   0 Matteo     (501) staff       (20)       89 2022-11-19 11:21:06.000000 vmas-1.2.8/vmas/scenarios/mpe/__init__.py
--rwxr-xr-x   0 Matteo     (501) staff       (20)     2082 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/mpe/simple.py
--rw-r--r--   0 Matteo     (501) staff       (20)     7829 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_adversary.py
--rw-r--r--   0 Matteo     (501) staff       (20)     6042 2022-11-19 11:21:06.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_crypto.py
--rw-r--r--   0 Matteo     (501) staff       (20)     5355 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_push.py
--rwxr-xr-x   0 Matteo     (501) staff       (20)     4289 2023-01-03 15:45:45.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_reference.py
--rwxr-xr-x   0 Matteo     (501) staff       (20)     4432 2022-11-19 11:21:06.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_speaker_listener.py
--rw-r--r--   0 Matteo     (501) staff       (20)     3580 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_spread.py
--rw-r--r--   0 Matteo     (501) staff       (20)     5859 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_tag.py
--rw-r--r--   0 Matteo     (501) staff       (20)    12438 2022-11-19 11:21:06.000000 vmas-1.2.8/vmas/scenarios/mpe/simple_world_comm.py
--rw-r--r--   0 Matteo     (501) staff       (20)    15532 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/multi_give_way.py
--rw-r--r--   0 Matteo     (501) staff       (20)     8209 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/navigation.py
--rw-r--r--   0 Matteo     (501) staff       (20)    11439 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/passage.py
--rw-r--r--   0 Matteo     (501) staff       (20)     6334 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/reverse_transport.py
--rw-r--r--   0 Matteo     (501) staff       (20)    13062 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/transport.py
--rw-r--r--   0 Matteo     (501) staff       (20)     4467 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/scenarios/wheel.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.743689 vmas-1.2.8/vmas/simulator/
--rw-r--r--   0 Matteo     (501) staff       (20)       89 2022-11-19 11:21:06.000000 vmas-1.2.8/vmas/simulator/__init__.py
--rw-r--r--   0 Matteo     (501) staff       (20)    73052 2023-03-20 09:57:19.000000 vmas-1.2.8/vmas/simulator/core.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.744694 vmas-1.2.8/vmas/simulator/environment/
--rw-r--r--   0 Matteo     (501) staff       (20)      546 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/simulator/environment/__init__.py
--rw-r--r--   0 Matteo     (501) staff       (20)    25542 2023-03-20 13:12:38.000000 vmas-1.2.8/vmas/simulator/environment/environment.py
--rw-r--r--   0 Matteo     (501) staff       (20)     3139 2023-03-20 11:43:23.000000 vmas-1.2.8/vmas/simulator/environment/gym.py
--rw-r--r--   0 Matteo     (501) staff       (20)     6907 2023-03-20 12:30:04.000000 vmas-1.2.8/vmas/simulator/environment/rllib.py
--rw-r--r--   0 Matteo     (501) staff       (20)      658 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/simulator/heuristic_policy.py
--rw-r--r--   0 Matteo     (501) staff       (20)     6198 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/simulator/joints.py
--rw-r--r--   0 Matteo     (501) staff       (20)    15821 2023-03-01 21:18:04.000000 vmas-1.2.8/vmas/simulator/rendering.py
--rw-r--r--   0 Matteo     (501) staff       (20)    11442 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/simulator/scenario.py
--rw-r--r--   0 Matteo     (501) staff       (20)     7780 2022-11-19 11:21:06.000000 vmas-1.2.8/vmas/simulator/secrcode.ttf
--rw-r--r--   0 Matteo     (501) staff       (20)     4097 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/simulator/sensors.py
--rw-r--r--   0 Matteo     (501) staff       (20)     6706 2023-03-18 10:04:58.000000 vmas-1.2.8/vmas/simulator/utils.py
--rw-r--r--   0 Matteo     (501) staff       (20)     4701 2023-01-23 16:01:21.000000 vmas-1.2.8/vmas/simulator/velocity_controller.py
-drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-03-20 13:33:53.727645 vmas-1.2.8/vmas.egg-info/
--rw-r--r--   0 Matteo     (501) staff       (20)      254 2023-03-20 13:33:53.000000 vmas-1.2.8/vmas.egg-info/PKG-INFO
--rw-r--r--   0 Matteo     (501) staff       (20)     1993 2023-03-20 13:33:53.000000 vmas-1.2.8/vmas.egg-info/SOURCES.txt
--rw-r--r--   0 Matteo     (501) staff       (20)        1 2023-03-20 13:33:53.000000 vmas-1.2.8/vmas.egg-info/dependency_links.txt
--rw-r--r--   0 Matteo     (501) staff       (20)       35 2023-03-20 13:33:53.000000 vmas-1.2.8/vmas.egg-info/requires.txt
--rw-r--r--   0 Matteo     (501) staff       (20)        5 2023-03-20 13:33:53.000000 vmas-1.2.8/vmas.egg-info/top_level.txt
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.497734 vmas-1.2.9/
+-rw-r--r--   0 Matteo     (501) staff       (20)    35149 2022-11-19 11:21:06.000000 vmas-1.2.9/LICENSE
+-rw-r--r--   0 Matteo     (501) staff       (20)       35 2023-01-23 16:01:21.000000 vmas-1.2.9/MANIFEST.in
+-rw-r--r--   0 Matteo     (501) staff       (20)      254 2023-04-06 08:30:25.497829 vmas-1.2.9/PKG-INFO
+-rw-r--r--   0 Matteo     (501) staff       (20)    59944 2023-03-27 15:44:12.000000 vmas-1.2.9/README.md
+-rw-r--r--   0 Matteo     (501) staff       (20)      103 2023-04-06 08:30:25.498080 vmas-1.2.9/setup.cfg
+-rw-r--r--   0 Matteo     (501) staff       (20)      533 2023-04-06 08:30:11.000000 vmas-1.2.9/setup.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.483481 vmas-1.2.9/vmas/
+-rw-r--r--   0 Matteo     (501) staff       (20)     1357 2023-04-06 08:01:36.000000 vmas-1.2.9/vmas/__init__.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.485385 vmas-1.2.9/vmas/examples/
+-rw-r--r--   0 Matteo     (501) staff       (20)       89 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/examples/__init__.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     5731 2023-03-10 08:34:41.000000 vmas-1.2.9/vmas/examples/rllib.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     2374 2023-03-20 12:34:04.000000 vmas-1.2.9/vmas/examples/run_heuristic.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     2768 2023-03-30 10:54:03.000000 vmas-1.2.9/vmas/examples/use_vmas_env.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    10389 2023-03-10 08:34:41.000000 vmas-1.2.9/vmas/interactive_rendering.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     1946 2023-03-27 15:44:12.000000 vmas-1.2.9/vmas/make_env.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.490995 vmas-1.2.9/vmas/scenarios/
+-rw-r--r--   0 Matteo     (501) staff       (20)      775 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/__init__.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     9651 2023-04-06 08:03:55.000000 vmas-1.2.9/vmas/scenarios/balance.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    13749 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/ball_passage.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     7901 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/ball_trajectory.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     9998 2023-04-06 08:03:55.000000 vmas-1.2.9/vmas/scenarios/buzz_wire.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.492478 vmas-1.2.9/vmas/scenarios/debug/
+-rw-r--r--   0 Matteo     (501) staff       (20)       89 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/debug/__init__.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    10109 2023-02-06 14:26:05.000000 vmas-1.2.9/vmas/scenarios/debug/asym_joint.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     6879 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/debug/circle_trajectory.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     8819 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/debug/goal.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     3775 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/debug/het_mass.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     4577 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/debug/line_trajectory.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     5513 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/debug/vel_control.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     5164 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/debug/waterfall.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    13511 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/discovery.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     5315 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/dispersion.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     5018 2023-04-06 08:17:07.000000 vmas-1.2.9/vmas/scenarios/dropout.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     6197 2023-04-06 07:40:00.000000 vmas-1.2.9/vmas/scenarios/flocking.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    64455 2023-04-06 08:13:31.000000 vmas-1.2.9/vmas/scenarios/football.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    19240 2023-04-06 07:40:00.000000 vmas-1.2.9/vmas/scenarios/give_way.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    27794 2023-04-06 07:40:00.000000 vmas-1.2.9/vmas/scenarios/joint_passage.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    26899 2023-04-06 07:40:00.000000 vmas-1.2.9/vmas/scenarios/joint_passage_size.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.494555 vmas-1.2.9/vmas/scenarios/mpe/
+-rw-r--r--   0 Matteo     (501) staff       (20)       89 2022-11-19 11:21:06.000000 vmas-1.2.9/vmas/scenarios/mpe/__init__.py
+-rwxr-xr-x   0 Matteo     (501) staff       (20)     2082 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/mpe/simple.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     7829 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_adversary.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     6042 2022-11-19 11:21:06.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_crypto.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     5355 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_push.py
+-rwxr-xr-x   0 Matteo     (501) staff       (20)     4289 2023-01-03 15:45:45.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_reference.py
+-rwxr-xr-x   0 Matteo     (501) staff       (20)     4432 2022-11-19 11:21:06.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_speaker_listener.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     3580 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_spread.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     5859 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_tag.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    12438 2022-11-19 11:21:06.000000 vmas-1.2.9/vmas/scenarios/mpe/simple_world_comm.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    15532 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/multi_give_way.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     8209 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/navigation.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    11439 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/passage.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     6534 2023-04-06 08:03:55.000000 vmas-1.2.9/vmas/scenarios/reverse_transport.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    13062 2023-04-06 07:39:41.000000 vmas-1.2.9/vmas/scenarios/transport.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     4467 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/scenarios/wheel.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.496610 vmas-1.2.9/vmas/simulator/
+-rw-r--r--   0 Matteo     (501) staff       (20)       89 2022-11-19 11:21:06.000000 vmas-1.2.9/vmas/simulator/__init__.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    73052 2023-04-06 07:40:00.000000 vmas-1.2.9/vmas/simulator/core.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.497428 vmas-1.2.9/vmas/simulator/environment/
+-rw-r--r--   0 Matteo     (501) staff       (20)      546 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/simulator/environment/__init__.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    25731 2023-04-06 08:18:17.000000 vmas-1.2.9/vmas/simulator/environment/environment.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     3139 2023-03-27 15:44:12.000000 vmas-1.2.9/vmas/simulator/environment/gym.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     6907 2023-03-27 15:44:12.000000 vmas-1.2.9/vmas/simulator/environment/rllib.py
+-rw-r--r--   0 Matteo     (501) staff       (20)      658 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/simulator/heuristic_policy.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     6198 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/simulator/joints.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    15817 2023-03-27 15:44:12.000000 vmas-1.2.9/vmas/simulator/rendering.py
+-rw-r--r--   0 Matteo     (501) staff       (20)    11442 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/simulator/scenario.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     7780 2022-11-19 11:21:06.000000 vmas-1.2.9/vmas/simulator/secrcode.ttf
+-rw-r--r--   0 Matteo     (501) staff       (20)     4097 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/simulator/sensors.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     6706 2023-03-18 10:04:58.000000 vmas-1.2.9/vmas/simulator/utils.py
+-rw-r--r--   0 Matteo     (501) staff       (20)     4701 2023-01-23 16:01:21.000000 vmas-1.2.9/vmas/simulator/velocity_controller.py
+drwxr-xr-x   0 Matteo     (501) staff       (20)        0 2023-04-06 08:30:25.484233 vmas-1.2.9/vmas.egg-info/
+-rw-r--r--   0 Matteo     (501) staff       (20)      254 2023-04-06 08:30:25.000000 vmas-1.2.9/vmas.egg-info/PKG-INFO
+-rw-r--r--   0 Matteo     (501) staff       (20)     1993 2023-04-06 08:30:25.000000 vmas-1.2.9/vmas.egg-info/SOURCES.txt
+-rw-r--r--   0 Matteo     (501) staff       (20)        1 2023-04-06 08:30:25.000000 vmas-1.2.9/vmas.egg-info/dependency_links.txt
+-rw-r--r--   0 Matteo     (501) staff       (20)       35 2023-04-06 08:30:25.000000 vmas-1.2.9/vmas.egg-info/requires.txt
+-rw-r--r--   0 Matteo     (501) staff       (20)        5 2023-04-06 08:30:25.000000 vmas-1.2.9/vmas.egg-info/top_level.txt
```

### Comparing `vmas-1.2.8/LICENSE` & `vmas-1.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/README.md` & `vmas-1.2.9/README.md`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/setup.py` & `vmas-1.2.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 #  ProrokLab (https://www.proroklab.org/)
 #  All rights reserved.
 
 from setuptools import setup, find_packages
 
 setup(
     name="vmas",
-    version="1.2.8",
+    version="1.2.9",
     description="Vectorized Multi-Agent Simulator",
     url="https://github.com/proroklab/VectorizedMultiAgentSimulator",
     license="GPLv3",
     author="Matteo Bettini",
     author_email="mb2389@cl.cam.ac.uk",
     packages=find_packages(),
     install_requires=["numpy", "torch", "pyglet<=1.5.27", "gym", "six"],
```

### Comparing `vmas-1.2.8/vmas/__init__.py` & `vmas-1.2.9/vmas/__init__.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/examples/rllib.py` & `vmas-1.2.9/vmas/examples/rllib.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/examples/run_heuristic.py` & `vmas-1.2.9/vmas/examples/run_heuristic.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/examples/use_vmas_env.py` & `vmas-1.2.9/vmas/examples/use_vmas_env.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/interactive_rendering.py` & `vmas-1.2.9/vmas/interactive_rendering.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/make_env.py` & `vmas-1.2.9/vmas/make_env.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/__init__.py` & `vmas-1.2.9/vmas/scenarios/__init__.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/balance.py` & `vmas-1.2.9/vmas/scenarios/balance.py`

 * *Files 2% similar despite different names*

```diff
@@ -74,15 +74,14 @@
 
         self.pos_rew = torch.zeros(batch_dim, device=device, dtype=torch.float32)
         self.ground_rew = self.pos_rew.clone()
 
         return world
 
     def reset_world_at(self, env_index: int = None):
-
         goal_pos = torch.cat(
             [
                 torch.zeros(
                     (1, 1) if env_index is not None else (self.world.batch_dim, 1),
                     device=self.world.device,
                     dtype=torch.float32,
                 ).uniform_(
@@ -180,14 +179,17 @@
         floor.set_pos(
             torch.tensor(
                 [0, -self.world.y_semidim - floor.shape.width / 2 - self.agent_radius],
                 device=self.world.device,
             ),
             batch_index=env_index,
         )
+        self.on_the_ground = (self.package.state.pos[:, Y] <= -self.world.y_semidim) + (
+            self.line.state.pos[:, Y] <= -self.world.y_semidim
+        )
         if env_index is None:
             self.global_shaping = (
                 torch.linalg.vector_norm(
                     self.package.state.pos - self.package.goal.state.pos, dim=1
                 )
                 * self.shaping_factor
             )
```

### Comparing `vmas-1.2.8/vmas/scenarios/ball_passage.py` & `vmas-1.2.9/vmas/scenarios/ball_passage.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/ball_trajectory.py` & `vmas-1.2.9/vmas/scenarios/ball_trajectory.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/buzz_wire.py` & `vmas-1.2.9/vmas/scenarios/buzz_wire.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 #  Copyright (c) 2022-2023.
 #  ProrokLab (https://www.proroklab.org/)
 #  All rights reserved.
 from typing import Dict
 
 import torch
 from torch import Tensor
-
 from vmas import render_interactively
 from vmas.simulator.core import Agent, Landmark, Sphere, World, Line
 from vmas.simulator.joints import Joint
 from vmas.simulator.scenario import BaseScenario
 from vmas.simulator.utils import Color
 
 
@@ -88,19 +87,19 @@
             )
             world.add_joint(self.joints[i])
 
         self.build_path_line(world)
 
         self.pos_rew = torch.zeros(batch_dim, device=device, dtype=torch.float32)
         self.collision_rew = self.pos_rew.clone()
+        self.collided = torch.full((world.batch_dim,), False, device=device)
 
         return world
 
     def reset_world_at(self, env_index: int = None):
-
         start_angle = torch.zeros(
             (1, 1) if env_index is not None else (self.world.batch_dim, 1),
             device=self.world.device,
             dtype=torch.float32,
         ).uniform_(
             -torch.pi / 2 + torch.pi / 3 if self.random_start_angle else 0,
             torch.pi / 2 - torch.pi / 3 if self.random_start_angle else 0,
@@ -188,34 +187,34 @@
         if env_index is None:
             self.pos_shaping = (
                 torch.linalg.vector_norm(
                     self.ball.state.pos - self.goal.state.pos, dim=1
                 )
                 * self.pos_shaping_factor
             )
+            self.collided[:] = False
         else:
             self.pos_shaping[env_index] = (
                 torch.linalg.vector_norm(
                     self.ball.state.pos[env_index] - self.goal.state.pos[env_index],
                 )
                 * self.pos_shaping_factor
             )
+            self.collided[env_index] = False
 
     def reward(self, agent: Agent):
         is_first = agent == self.world.agents[0]
 
         if is_first:
             self.rew = torch.zeros(
                 self.world.batch_dim, device=self.world.device, dtype=torch.float32
             )
             self.pos_rew[:] = 0
             self.collision_rew[:] = 0
-            self.collided = torch.full(
-                (self.world.batch_dim,), False, device=self.world.device
-            )
+            self.collided[:] = False
 
             dist_to_goal = torch.linalg.vector_norm(
                 self.ball.state.pos - self.goal.state.pos,
                 dim=1,
             )
             pos_shaping = dist_to_goal * self.pos_shaping_factor
             self.pos_rew += self.pos_shaping - pos_shaping
```

### Comparing `vmas-1.2.8/vmas/scenarios/debug/asym_joint.py` & `vmas-1.2.9/vmas/scenarios/debug/asym_joint.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/debug/circle_trajectory.py` & `vmas-1.2.9/vmas/scenarios/debug/circle_trajectory.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/debug/goal.py` & `vmas-1.2.9/vmas/scenarios/debug/goal.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/debug/het_mass.py` & `vmas-1.2.9/vmas/scenarios/debug/het_mass.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/debug/line_trajectory.py` & `vmas-1.2.9/vmas/scenarios/debug/line_trajectory.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/debug/vel_control.py` & `vmas-1.2.9/vmas/scenarios/debug/vel_control.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/debug/waterfall.py` & `vmas-1.2.9/vmas/scenarios/debug/waterfall.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/discovery.py` & `vmas-1.2.9/vmas/scenarios/discovery.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/dispersion.py` & `vmas-1.2.9/vmas/scenarios/dispersion.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/dropout.py` & `vmas-1.2.9/vmas/scenarios/dropout.py`

 * *Files 3% similar despite different names*

```diff
@@ -2,15 +2,14 @@
 #  ProrokLab (https://www.proroklab.org/)
 #  All rights reserved.
 import math
 from typing import Dict
 
 import torch
 from torch import Tensor
-
 from vmas import render_interactively
 from vmas.simulator.core import Agent, Landmark, Sphere, World
 from vmas.simulator.scenario import BaseScenario
 from vmas.simulator.utils import Color
 
 DEFAULT_ENERGY_COEFF = 0.02
 
@@ -36,14 +35,15 @@
             shape=Sphere(radius=0.03),
             color=Color.GREEN,
         )
         world.add_landmark(goal)
 
         self.pos_rew = torch.zeros(batch_dim, device=device)
         self.energy_rew = self.pos_rew.clone()
+        self._done = torch.zeros(batch_dim, device=device, dtype=torch.bool)
 
         return world
 
     def reset_world_at(self, env_index: int = None):
         for agent in self.world.agents:
             # Random pos between -1 and 1
             agent.set_pos(
@@ -75,17 +75,19 @@
                 batch_index=env_index,
             )
             if env_index is None:
                 landmark.eaten = torch.full(
                     (self.world.batch_dim,), False, device=self.world.device
                 )
                 landmark.reset_render()
+                self._done[:] = False
             else:
                 landmark.eaten[env_index] = False
                 landmark.is_rendering[env_index] = True
+                self._done[env_index] = False
 
     def reward(self, agent: Agent):
         is_first = agent == self.world.agents[0]
         is_last = agent == self.world.agents[-1]
 
         if is_first:
             self.any_eaten = self._done = torch.any(
```

### Comparing `vmas-1.2.8/vmas/scenarios/flocking.py` & `vmas-1.2.9/vmas/scenarios/flocking.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/football.py` & `vmas-1.2.9/vmas/scenarios/football.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,23 +19,28 @@
         world = self.init_world(batch_dim, device)
         self.init_agents(world)
         self.init_ball(world)
         self.init_background(world)
         self.init_walls(world)
         self.init_goals(world)
         # self.init_traj_pts(world)
+        self._done = torch.zeros(batch_dim, device=device, dtype=torch.bool)
         return world
 
     def reset_world_at(self, env_index: int = None):
         self.reset_ball(env_index)
         self.reset_agents(env_index)
         self.reset_background(env_index)
         self.reset_walls(env_index)
         self.reset_goals(env_index)
         self.reset_controllers(env_index)
+        if env_index is None:
+            self._done[:] = False
+        else:
+            self._done[env_index] = False
 
     def init_params(self, **kwargs):
         self.viewer_size = kwargs.get("viewer_size", (1200, 800))
         self.ai_red_agents = kwargs.get("ai_red_agents", True)
         self.ai_blue_agents = kwargs.get("ai_blue_agents", False)
         self.n_blue_agents = kwargs.get("n_blue_agents", 3)
         self.n_red_agents = kwargs.get("n_red_agents", 3)
@@ -309,15 +314,14 @@
                         dtype=torch.float32,
                         device=self.world.device,
                     ),
                     batch_index=env_index,
                 )
 
     def init_walls(self, world):
-
         right_top_wall = Landmark(
             name="Right Top Wall",
             collide=True,
             movable=False,
             shape=Line(
                 length=self.pitch_width / 2 - self.agent_size - self.goal_size / 2,
             ),
```

### Comparing `vmas-1.2.8/vmas/scenarios/give_way.py` & `vmas-1.2.9/vmas/scenarios/give_way.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/joint_passage.py` & `vmas-1.2.9/vmas/scenarios/joint_passage.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/joint_passage_size.py` & `vmas-1.2.9/vmas/scenarios/joint_passage_size.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_adversary.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_adversary.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_crypto.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_crypto.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_push.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_push.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_reference.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_reference.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_speaker_listener.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_speaker_listener.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_spread.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_spread.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_tag.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_tag.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/mpe/simple_world_comm.py` & `vmas-1.2.9/vmas/scenarios/mpe/simple_world_comm.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/multi_give_way.py` & `vmas-1.2.9/vmas/scenarios/multi_give_way.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/navigation.py` & `vmas-1.2.9/vmas/scenarios/navigation.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/passage.py` & `vmas-1.2.9/vmas/scenarios/passage.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/reverse_transport.py` & `vmas-1.2.9/vmas/scenarios/reverse_transport.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright (c) 2022.
+#  Copyright (c) 2022-2023.
 #  ProrokLab (https://www.proroklab.org/)
 #  All rights reserved.
 
 
 import torch
 
 from vmas import render_interactively
@@ -47,15 +47,14 @@
         )
         self.package.goal = goal
         world.add_landmark(self.package)
 
         return world
 
     def reset_world_at(self, env_index: int = None):
-
         package_pos = torch.zeros(
             (1, self.world.dim_p)
             if env_index is not None
             else (self.world.batch_dim, self.world.dim_p),
             device=self.world.device,
             dtype=torch.float32,
         ).uniform_(
@@ -107,29 +106,34 @@
                 dtype=torch.float32,
             ).uniform_(
                 -1.0,
                 1.0,
             ),
             batch_index=env_index,
         )
+
         if env_index is None:
             self.package.global_shaping = (
                 torch.linalg.vector_norm(
                     self.package.state.pos - self.package.goal.state.pos, dim=1
                 )
                 * self.shaping_factor
             )
+            self.package.on_goal = torch.zeros(
+                self.world.batch_dim, dtype=torch.bool, device=self.world.device
+            )
         else:
             self.package.global_shaping[env_index] = (
                 torch.linalg.vector_norm(
                     self.package.state.pos[env_index]
                     - self.package.goal.state.pos[env_index]
                 )
                 * self.shaping_factor
             )
+            self.package.on_goal[env_index] = False
 
     def reward(self, agent: Agent):
         is_first = agent == self.world.agents[0]
 
         if is_first:
             self.rew = torch.zeros(
                 self.world.batch_dim, device=self.world.device, dtype=torch.float32
```

### Comparing `vmas-1.2.8/vmas/scenarios/transport.py` & `vmas-1.2.9/vmas/scenarios/transport.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/scenarios/wheel.py` & `vmas-1.2.9/vmas/scenarios/wheel.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/core.py` & `vmas-1.2.9/vmas/simulator/core.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/environment/__init__.py` & `vmas-1.2.9/vmas/simulator/environment/__init__.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/environment/environment.py` & `vmas-1.2.9/vmas/simulator/environment/environment.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,15 +31,14 @@
         device: DEVICE_TYPING = "cpu",
         max_steps: Optional[int] = None,
         continuous_actions: bool = True,
         seed: Optional[int] = None,
         dict_spaces: bool = False,
         **kwargs,
     ):
-
         self.scenario = scenario
         self.num_envs = num_envs
         TorchVectorizedObject.__init__(self, num_envs, torch.device(device))
         self.world = self.scenario.env_make_world(self.num_envs, self.device, **kwargs)
 
         self.agents = self.world.policy_agents
         self.n_agents = len(self.agents)
@@ -129,34 +128,35 @@
         if get_rewards:
             rewards = {} if dict_agent_names else []
         if get_infos:
             infos = {} if dict_agent_names else []
 
         for agent in self.agents:
             if get_rewards:
-                reward = self.scenario.reward(agent)
+                reward = self.scenario.reward(agent).clone()
                 if dict_agent_names:
                     rewards.update({agent.name: reward})
                 else:
                     rewards.append(reward)
             if get_observations:
-                observation = self.scenario.observation(agent)
+                observation = self.scenario.observation(agent).clone()
                 if dict_agent_names:
                     obs.update({agent.name: observation})
                 else:
                     obs.append(observation)
             if get_infos:
                 info = self.scenario.info(agent)
+                info = {key: val.clone() for key, val in info.items()}
                 if dict_agent_names:
                     infos.update({agent.name: info})
                 else:
                     infos.append(info)
 
         if get_dones:
-            dones = self.done()
+            dones = self.done().clone()
 
         result = [obs, rewards, dones, infos]
         return [data for data in result if data is not None]
 
     def seed(self, seed=None):
         if seed is None:
             seed = 0
@@ -240,15 +240,15 @@
         #     f"rewards[0][0] (agent 0 env 0): {rewards[0][0]}"
         # )
         # print(f"Dones len (n_envs): {len(dones)}, dones[0] (done env 0): {dones[0]}")
         # print(f"Info len (n_agents): {len(infos)}, info[0] (infos agent 0): {infos[0]}")
         return obs, rewards, dones, infos
 
     def done(self):
-        dones = self.scenario.done()
+        dones = self.scenario.done().clone()
         if self.max_steps is not None:
             dones += self.steps >= self.max_steps
         return dones
 
     def get_action_space(self):
         if not self.dict_spaces:
             return spaces.Tuple(
@@ -616,14 +616,15 @@
         # render to display or array
         return self.viewer.render(return_rgb_array=mode == "rgb_array")
 
     def plot_function(self, f, precision, plot_range, cmap_range, cmap_alpha):
         from vmas.simulator.rendering import render_function_util
 
         if plot_range is None:
+            assert self.viewer.bounds is not None, "Set viewer bounds before plotting"
             x_min, x_max, y_min, y_max = self.viewer.bounds.tolist()
             plot_range = [x_min - precision, x_max - precision], [
                 y_min - precision,
                 y_max + precision,
             ]
 
         geoms = render_function_util(
```

### Comparing `vmas-1.2.8/vmas/simulator/environment/gym.py` & `vmas-1.2.9/vmas/simulator/environment/gym.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/environment/rllib.py` & `vmas-1.2.9/vmas/simulator/environment/rllib.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/heuristic_policy.py` & `vmas-1.2.9/vmas/simulator/heuristic_policy.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/joints.py` & `vmas-1.2.9/vmas/simulator/joints.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/rendering.py` & `vmas-1.2.9/vmas/simulator/rendering.py`

 * *Files 0% similar despite different names*

```diff
@@ -87,30 +87,29 @@
                 spec
             )
         )
 
 
 class Viewer(object):
     def __init__(self, width, height, display=None, visible=True):
-
         display = get_display(display)
 
         self.width = width
         self.height = height
 
         self.window = pyglet.window.Window(
             width=width, height=height, display=display, visible=visible
         )
         self.window.on_close = self.window_closed_by_user
 
         self.geoms = []
         self.text_lines = []
         self.onetime_geoms = []
         self.transform = Transform()
-        self.bounds = np.array([0.0, 0.0, 0.0, 0.0])
+        self.bounds = None
 
         glEnable(GL_BLEND)
         # glEnable(GL_MULTISAMPLE)
         glEnable(GL_LINE_SMOOTH)
         # glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
         glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
         glLineWidth(2.0)
@@ -120,15 +119,15 @@
         self.window.close()
 
     def window_closed_by_user(self):
         self.close()
 
     def set_bounds(self, left, right, bottom, top):
         assert right > left and top > bottom
-        self.bounds = np.array([left, right, bottom, top])
+        self.bounds = torch.tensor([left, right, bottom, top], device=left.device)
         scalex = self.width / (right - left)
         scaley = self.height / (top - bottom)
         self.transform = Transform(
             translation=(-left * scalex, -bottom * scaley), scale=(scalex, scaley)
         )
 
     def add_geom(self, geom):
@@ -412,15 +411,14 @@
     plot_range: Union[
         float, Tuple[float, float], Tuple[Tuple[float, float], Tuple[float, float]]
     ],
     precision: float = 0.01,
     cmap_range: Optional[Tuple[float, float]] = None,
     cmap_alpha: float = 1.0,
 ):
-
     geoms = []
 
     if isinstance(plot_range, int) or isinstance(plot_range, float):
         x_min = -plot_range
         y_min = -plot_range
         x_max = plot_range
         y_max = plot_range
```

### Comparing `vmas-1.2.8/vmas/simulator/scenario.py` & `vmas-1.2.9/vmas/simulator/scenario.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/secrcode.ttf` & `vmas-1.2.9/vmas/simulator/secrcode.ttf`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/sensors.py` & `vmas-1.2.9/vmas/simulator/sensors.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/utils.py` & `vmas-1.2.9/vmas/simulator/utils.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas/simulator/velocity_controller.py` & `vmas-1.2.9/vmas/simulator/velocity_controller.py`

 * *Files identical despite different names*

### Comparing `vmas-1.2.8/vmas.egg-info/SOURCES.txt` & `vmas-1.2.9/vmas.egg-info/SOURCES.txt`

 * *Files identical despite different names*

