# Comparing `tmp/busy-3.4.2.tar.gz` & `tmp/busy-3.4.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "busy-3.4.2.tar", last modified: Fri Apr  7 02:01:25 2023, max compression
+gzip compressed data, was "busy-3.4.4.tar", last modified: Fri Apr  7 05:38:03 2023, max compression
```

## Comparing `busy-3.4.2.tar` & `busy-3.4.4.tar`

### file list

```diff
@@ -1,108 +1,109 @@
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.270043 busy-3.4.2/
--rw-r--r--   0 francispotter   (501) staff       (20)     1071 2023-03-30 16:53:52.000000 busy-3.4.2/LICENSE
--rw-r--r--   0 francispotter   (501) staff       (20)    21774 2023-04-07 02:01:25.269718 busy-3.4.2/PKG-INFO
--rw-r--r--   0 francispotter   (501) staff       (20)    21499 2023-04-07 00:00:49.000000 busy-3.4.2/README.md
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.210960 busy-3.4.2/busy/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/busy/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)       66 2023-03-30 16:53:52.000000 busy-3.4.2/busy/__main__.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.232998 busy-3.4.2/busy/command/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1872 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/activate_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      825 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/add_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      245 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/base_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     8907 2023-04-06 23:37:22.000000 busy-3.4.2/busy/command/command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      279 2023-04-06 23:37:22.000000 busy-3.4.2/busy/command/curses_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1643 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/defer_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      981 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/delete_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-04-06 23:37:22.000000 busy-3.4.2/busy/command/drop_and_pop_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1309 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/edit_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1908 2023-04-06 23:37:22.000000 busy-3.4.2/busy/command/finish_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      681 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/list_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      212 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/queues_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      254 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/resource_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      950 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/switch_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      196 2023-03-30 16:53:52.000000 busy-3.4.2/busy/command/tags_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      476 2023-04-06 23:37:22.000000 busy-3.4.2/busy/command/top_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     3957 2023-04-07 01:59:46.000000 busy-3.4.2/busy/handler.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.234669 busy-3.4.2/busy/model/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/busy/model/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1931 2023-04-06 23:37:22.000000 busy-3.4.2/busy/model/item.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2598 2023-03-30 16:53:52.000000 busy-3.4.2/busy/model/task.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.236366 busy-3.4.2/busy/queue/
--rw-r--r--   0 francispotter   (501) staff       (20)      102 2023-04-06 23:37:22.000000 busy-3.4.2/busy/queue/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     5099 2023-04-06 23:37:22.000000 busy-3.4.2/busy/queue/queue.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2139 2023-04-06 23:37:22.000000 busy-3.4.2/busy/queue/todo_queue.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.237115 busy-3.4.2/busy/root/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/busy/root/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2297 2023-04-07 00:01:46.000000 busy-3.4.2/busy/root/file_system_root.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2204 2023-03-30 16:53:52.000000 busy-3.4.2/busy/selector.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.240364 busy-3.4.2/busy/ui/
--rw-r--r--   0 francispotter   (501) staff       (20)      133 2023-03-30 16:53:52.000000 busy-3.4.2/busy/ui/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     6839 2023-04-06 23:37:22.000000 busy-3.4.2/busy/ui/curses_ui.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1573 2023-04-06 23:37:22.000000 busy-3.4.2/busy/ui/shell_ui.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.242054 busy-3.4.2/busy/ui/tcl_ui/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/busy/ui/tcl_ui/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      824 2023-03-30 16:53:52.000000 busy-3.4.2/busy/ui/tcl_ui/edit_task_widget.py
--rw-r--r--   0 francispotter   (501) staff       (20)      701 2023-03-30 16:53:52.000000 busy-3.4.2/busy/ui/tcl_ui/get_item_widget.py
--rw-r--r--   0 francispotter   (501) staff       (20)     5178 2023-04-06 23:37:22.000000 busy-3.4.2/busy/ui/ui.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.247121 busy-3.4.2/busy/util/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/busy/util/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     6682 2023-04-06 23:37:22.000000 busy-3.4.2/busy/util/class_family.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2882 2023-04-06 23:37:22.000000 busy-3.4.2/busy/util/date_util.py
--rw-r--r--   0 francispotter   (501) staff       (20)      217 2023-03-30 16:53:52.000000 busy-3.4.2/busy/util/python_version.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1231 2023-04-06 23:39:24.000000 busy-3.4.2/busy/util/readline_util.py
--rw-r--r--   0 francispotter   (501) staff       (20)      973 2023-03-30 16:53:52.000000 busy-3.4.2/busy/util/super_wrapper.py
--rw-r--r--   0 francispotter   (501) staff       (20)      131 2023-03-30 16:53:52.000000 busy-3.4.2/busy/util/textbox_util.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.216398 busy-3.4.2/busy.egg-info/
--rw-r--r--   0 francispotter   (501) staff       (20)    21774 2023-04-07 02:01:25.000000 busy-3.4.2/busy.egg-info/PKG-INFO
--rw-r--r--   0 francispotter   (501) staff       (20)     2208 2023-04-07 02:01:25.000000 busy-3.4.2/busy.egg-info/SOURCES.txt
--rw-r--r--   0 francispotter   (501) staff       (20)        1 2023-04-07 02:01:25.000000 busy-3.4.2/busy.egg-info/dependency_links.txt
--rw-r--r--   0 francispotter   (501) staff       (20)       44 2023-04-07 02:01:25.000000 busy-3.4.2/busy.egg-info/entry_points.txt
--rw-r--r--   0 francispotter   (501) staff       (20)        1 2023-01-01 23:16:57.000000 busy-3.4.2/busy.egg-info/not-zip-safe
--rw-r--r--   0 francispotter   (501) staff       (20)       15 2023-04-07 02:01:25.000000 busy-3.4.2/busy.egg-info/top_level.txt
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.256204 busy-3.4.2/sand/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-02-25 16:13:53.000000 busy-3.4.2/sand/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      336 2023-02-23 13:30:28.000000 busy-3.4.2/sand/_dataclass.py
--rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-04-05 00:41:16.000000 busy-3.4.2/sand/_readline_util.py
--rw-r--r--   0 francispotter   (501) staff       (20)      676 2023-02-25 17:04:15.000000 busy-3.4.2/sand/_textpad.py
--rw-r--r--   0 francispotter   (501) staff       (20)      233 2023-03-06 16:05:27.000000 busy-3.4.2/sand/chooser.py
--rw-r--r--   0 francispotter   (501) staff       (20)      282 2023-03-01 14:38:38.000000 busy-3.4.2/sand/rl-io.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-03-01 15:07:59.000000 busy-3.4.2/sand/subprocess.py
--rw-r--r--   0 francispotter   (501) staff       (20)      806 2023-03-02 16:10:26.000000 busy-3.4.2/sand/wrapper.py
--rw-r--r--   0 francispotter   (501) staff       (20)       38 2023-04-07 02:01:25.270177 busy-3.4.2/setup.cfg
--rw-r--r--   0 francispotter   (501) staff       (20)      752 2023-04-07 00:02:23.000000 busy-3.4.2/setup.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.256973 busy-3.4.2/test/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/test/__init__.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.258946 busy-3.4.2/test/data_class_family/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/test/data_class_family/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      101 2023-03-30 16:53:52.000000 busy-3.4.2/test/data_class_family/atriarch.py
--rw-r--r--   0 francispotter   (501) staff       (20)       76 2023-03-30 16:53:52.000000 busy-3.4.2/test/data_class_family/child.py
--rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-03-30 16:53:52.000000 busy-3.4.2/test/data_class_family/grandchild.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.259986 busy-3.4.2/test/handler/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/test/handler/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1205 2023-03-30 16:53:52.000000 busy-3.4.2/test/handler/test_handler.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.260950 busy-3.4.2/test/integration/
--rw-r--r--   0 francispotter   (501) staff       (20)      150 2023-04-06 23:37:22.000000 busy-3.4.2/test/integration/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      416 2023-04-06 23:37:22.000000 busy-3.4.2/test/integration/test_integration.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.264132 busy-3.4.2/test/model/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/test/model/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      433 2023-04-06 23:37:22.000000 busy-3.4.2/test/model/test_item.py
--rw-r--r--   0 francispotter   (501) staff       (20)      845 2023-04-06 23:37:22.000000 busy-3.4.2/test/model/test_item_io.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2857 2023-04-06 23:37:22.000000 busy-3.4.2/test/model/test_queue.py
--rw-r--r--   0 francispotter   (501) staff       (20)      624 2023-04-06 23:37:22.000000 busy-3.4.2/test/model/test_queue_replace.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1778 2023-04-06 23:37:22.000000 busy-3.4.2/test/model/test_task.py
--rw-r--r--   0 francispotter   (501) staff       (20)     4056 2023-04-06 23:37:22.000000 busy-3.4.2/test/model/test_todo_queue.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.265407 busy-3.4.2/test/root/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-04-06 23:37:22.000000 busy-3.4.2/test/root/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1406 2023-04-06 23:37:22.000000 busy-3.4.2/test/root/test_file.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2529 2023-04-06 23:37:22.000000 busy-3.4.2/test/root/test_file_system_root.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.266778 busy-3.4.2/test/ui/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/test/ui/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      357 2023-03-30 16:53:52.000000 busy-3.4.2/test/ui/test_shell_ui.py
--rw-r--r--   0 francispotter   (501) staff       (20)      790 2023-03-30 16:53:52.000000 busy-3.4.2/test/ui/test_ui_terminal_editor.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 02:01:25.269207 busy-3.4.2/test/util/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.2/test/util/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      797 2023-04-06 23:37:22.000000 busy-3.4.2/test/util/test_class_families.py
--rw-r--r--   0 francispotter   (501) staff       (20)      237 2023-03-30 16:53:52.000000 busy-3.4.2/test/util/test_class_family.py
--rw-r--r--   0 francispotter   (501) staff       (20)      452 2023-03-30 16:53:52.000000 busy-3.4.2/test/util/test_date.py
--rw-r--r--   0 francispotter   (501) staff       (20)      508 2023-03-30 16:53:52.000000 busy-3.4.2/test/util/test_python_version.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.959057 busy-3.4.4/
+-rw-r--r--   0 francispotter   (501) staff       (20)     1071 2023-03-30 16:53:52.000000 busy-3.4.4/LICENSE
+-rw-r--r--   0 francispotter   (501) staff       (20)    21828 2023-04-07 05:38:03.958393 busy-3.4.4/PKG-INFO
+-rw-r--r--   0 francispotter   (501) staff       (20)    21583 2023-04-07 05:33:57.000000 busy-3.4.4/README.md
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.894292 busy-3.4.4/busy/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/busy/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       66 2023-03-30 16:53:52.000000 busy-3.4.4/busy/__main__.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.916758 busy-3.4.4/busy/command/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1872 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/activate_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      825 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/add_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      245 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/base_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     8907 2023-04-07 05:33:57.000000 busy-3.4.4/busy/command/command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      279 2023-04-07 05:33:57.000000 busy-3.4.4/busy/command/curses_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1643 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/defer_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      981 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/delete_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-04-07 05:33:57.000000 busy-3.4.4/busy/command/drop_and_pop_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1309 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/edit_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1908 2023-04-07 05:33:57.000000 busy-3.4.4/busy/command/finish_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      681 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/list_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      212 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/queues_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      254 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/resource_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      950 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/switch_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      196 2023-03-30 16:53:52.000000 busy-3.4.4/busy/command/tags_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      476 2023-04-07 05:33:57.000000 busy-3.4.4/busy/command/top_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     3957 2023-04-07 05:33:57.000000 busy-3.4.4/busy/handler.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.918684 busy-3.4.4/busy/model/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/busy/model/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1931 2023-04-07 05:33:57.000000 busy-3.4.4/busy/model/item.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2598 2023-03-30 16:53:52.000000 busy-3.4.4/busy/model/task.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.920899 busy-3.4.4/busy/queue/
+-rw-r--r--   0 francispotter   (501) staff       (20)      102 2023-04-07 05:33:57.000000 busy-3.4.4/busy/queue/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     5099 2023-04-07 05:33:57.000000 busy-3.4.4/busy/queue/queue.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2139 2023-04-07 05:33:57.000000 busy-3.4.4/busy/queue/todo_queue.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.921930 busy-3.4.4/busy/root/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/busy/root/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2297 2023-04-07 05:33:57.000000 busy-3.4.4/busy/root/file_system_root.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2204 2023-03-30 16:53:52.000000 busy-3.4.4/busy/selector.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.924320 busy-3.4.4/busy/ui/
+-rw-r--r--   0 francispotter   (501) staff       (20)      133 2023-03-30 16:53:52.000000 busy-3.4.4/busy/ui/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     6839 2023-04-07 05:33:57.000000 busy-3.4.4/busy/ui/curses_ui.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1573 2023-04-07 05:33:57.000000 busy-3.4.4/busy/ui/shell_ui.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.926408 busy-3.4.4/busy/ui/tcl_ui/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/busy/ui/tcl_ui/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      824 2023-03-30 16:53:52.000000 busy-3.4.4/busy/ui/tcl_ui/edit_task_widget.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      701 2023-03-30 16:53:52.000000 busy-3.4.4/busy/ui/tcl_ui/get_item_widget.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     5178 2023-04-07 05:33:57.000000 busy-3.4.4/busy/ui/ui.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.933233 busy-3.4.4/busy/util/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/busy/util/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     6682 2023-04-07 05:33:57.000000 busy-3.4.4/busy/util/class_family.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2882 2023-04-07 05:33:57.000000 busy-3.4.4/busy/util/date_util.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      217 2023-03-30 16:53:52.000000 busy-3.4.4/busy/util/python_version.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1231 2023-04-06 23:39:24.000000 busy-3.4.4/busy/util/readline_util.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      973 2023-03-30 16:53:52.000000 busy-3.4.4/busy/util/super_wrapper.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      131 2023-03-30 16:53:52.000000 busy-3.4.4/busy/util/textbox_util.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.900142 busy-3.4.4/busy.egg-info/
+-rw-r--r--   0 francispotter   (501) staff       (20)    21828 2023-04-07 05:38:03.000000 busy-3.4.4/busy.egg-info/PKG-INFO
+-rw-r--r--   0 francispotter   (501) staff       (20)     2222 2023-04-07 05:38:03.000000 busy-3.4.4/busy.egg-info/SOURCES.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)        1 2023-04-07 05:38:03.000000 busy-3.4.4/busy.egg-info/dependency_links.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)       43 2023-04-07 05:38:03.000000 busy-3.4.4/busy.egg-info/entry_points.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)       20 2023-04-07 05:38:03.000000 busy-3.4.4/busy.egg-info/requires.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)        5 2023-04-07 05:38:03.000000 busy-3.4.4/busy.egg-info/top_level.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)      524 2023-04-07 05:33:57.000000 busy-3.4.4/pyproject.toml
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.938458 busy-3.4.4/sand/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-02-25 16:13:53.000000 busy-3.4.4/sand/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      336 2023-02-23 13:30:28.000000 busy-3.4.4/sand/_dataclass.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-04-05 00:41:16.000000 busy-3.4.4/sand/_readline_util.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      676 2023-02-25 17:04:15.000000 busy-3.4.4/sand/_textpad.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      233 2023-03-06 16:05:27.000000 busy-3.4.4/sand/chooser.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      282 2023-03-01 14:38:38.000000 busy-3.4.4/sand/rl-io.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-03-01 15:07:59.000000 busy-3.4.4/sand/subprocess.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      806 2023-03-02 16:10:26.000000 busy-3.4.4/sand/wrapper.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       38 2023-04-07 05:38:03.959158 busy-3.4.4/setup.cfg
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.939166 busy-3.4.4/test/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/test/__init__.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.941154 busy-3.4.4/test/data_class_family/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/test/data_class_family/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      101 2023-03-30 16:53:52.000000 busy-3.4.4/test/data_class_family/atriarch.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       76 2023-03-30 16:53:52.000000 busy-3.4.4/test/data_class_family/child.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-03-30 16:53:52.000000 busy-3.4.4/test/data_class_family/grandchild.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.942087 busy-3.4.4/test/handler/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/test/handler/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1205 2023-03-30 16:53:52.000000 busy-3.4.4/test/handler/test_handler.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.943506 busy-3.4.4/test/integration/
+-rw-r--r--   0 francispotter   (501) staff       (20)      150 2023-04-07 05:33:57.000000 busy-3.4.4/test/integration/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      416 2023-04-07 05:33:57.000000 busy-3.4.4/test/integration/test_integration.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.948709 busy-3.4.4/test/model/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/test/model/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      433 2023-04-07 05:33:57.000000 busy-3.4.4/test/model/test_item.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      845 2023-04-07 05:33:57.000000 busy-3.4.4/test/model/test_item_io.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2857 2023-04-07 05:33:57.000000 busy-3.4.4/test/model/test_queue.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      624 2023-04-07 05:33:57.000000 busy-3.4.4/test/model/test_queue_replace.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1778 2023-04-07 05:33:57.000000 busy-3.4.4/test/model/test_task.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     4056 2023-04-07 05:33:57.000000 busy-3.4.4/test/model/test_todo_queue.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.952426 busy-3.4.4/test/root/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-04-07 05:33:57.000000 busy-3.4.4/test/root/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1406 2023-04-07 05:33:57.000000 busy-3.4.4/test/root/test_file.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2529 2023-04-07 05:33:57.000000 busy-3.4.4/test/root/test_file_system_root.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.954250 busy-3.4.4/test/ui/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/test/ui/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      357 2023-03-30 16:53:52.000000 busy-3.4.4/test/ui/test_shell_ui.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      790 2023-03-30 16:53:52.000000 busy-3.4.4/test/ui/test_ui_terminal_editor.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 05:38:03.957495 busy-3.4.4/test/util/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.4/test/util/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      797 2023-04-07 05:33:57.000000 busy-3.4.4/test/util/test_class_families.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      237 2023-03-30 16:53:52.000000 busy-3.4.4/test/util/test_class_family.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      452 2023-03-30 16:53:52.000000 busy-3.4.4/test/util/test_date.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      508 2023-03-30 16:53:52.000000 busy-3.4.4/test/util/test_python_version.py
+-rw-r--r--   0 francispotter   (501) staff       (20)        5 2023-04-07 05:35:23.000000 busy-3.4.4/version
```

### Comparing `busy-3.4.2/LICENSE` & `busy-3.4.4/LICENSE`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/PKG-INFO` & `busy-3.4.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 Metadata-Version: 2.1
 Name: busy
-Version: 3.4.2
-Summary: Personal time management tool
-Home-page: http://gitlab.com/steampunk-wizard/busy
-Author: Francis Potter
-Author-email: busy@steampunkwizard.ca
+Version: 3.4.4
+Summary: Personal time management system
+Author-email: Francis Potter <busy@steampunkwizard.ca>
 License: MIT
+Requires-Python: >=3.6.5
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 Busy
 ====
 
 Busy is a personal time management tool, designed to help us all through our crazy busy days with as little stress as possible. It's simple, fast, and fun to use.
@@ -31,19 +30,19 @@
 - *Editable data*: The data is stored in text files, which can easily be edited outside of Busy itself. (In fact, Busy started as a todo.txt type of approach and grew from there.)
 
 _The idea of Importance over Urgency comes from the book "The 7 Habits of Highly Effective People". Although we firmly disagree with Steven Covey's statements on gay rights, the book contains excellent ideas._
 
 Installation
 ------------
 
-You'll need a terminal emulator to access a Bash-type prompt. Examples include:
+You'll need a terminal emulator to access a command or shell prompt. Examples include:
 
 - iTerm2 or Terminal on MacOS
 - Gnome Terminal or XTerm on Linux
-- Bash On Ubunto on Windows
+- CMD on Windows
 - Terminator on all platforms
 
 Busy also requires Python 3.6.5 or later. To check whether you already have the right version of Python on your system, start your terminal emulator and type:
 
 ```
 python -V
 ```
@@ -58,14 +57,16 @@
 
 Python comes with PIP, which enables installation of Python packages from a central server called PyPI.
 
 From now on, we're going to use `python3` and `pip3` in code snippets, although your system might prefer simply `python` or `pip`. Just edit them.
 
 _Windows only_ Install Python from the Microsoft store, but then use `pip install windows-curses` to install curses.
 
+_Python developers only_ Busy does require other packages, so feel free to use a venv.
+
 Here's the command to install the latest stable version of Busy itself:
 
 ```
 sudo pip3 install busy && pip3 show busy
 ```
 
 If you have previously installed Busy, and want to upgrade to the latest version, type:
```

### Comparing `busy-3.4.2/README.md` & `busy-3.4.4/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -20,19 +20,19 @@
 - *Editable data*: The data is stored in text files, which can easily be edited outside of Busy itself. (In fact, Busy started as a todo.txt type of approach and grew from there.)
 
 _The idea of Importance over Urgency comes from the book "The 7 Habits of Highly Effective People". Although we firmly disagree with Steven Covey's statements on gay rights, the book contains excellent ideas._
 
 Installation
 ------------
 
-You'll need a terminal emulator to access a Bash-type prompt. Examples include:
+You'll need a terminal emulator to access a command or shell prompt. Examples include:
 
 - iTerm2 or Terminal on MacOS
 - Gnome Terminal or XTerm on Linux
-- Bash On Ubunto on Windows
+- CMD on Windows
 - Terminator on all platforms
 
 Busy also requires Python 3.6.5 or later. To check whether you already have the right version of Python on your system, start your terminal emulator and type:
 
 ```
 python -V
 ```
@@ -47,14 +47,16 @@
 
 Python comes with PIP, which enables installation of Python packages from a central server called PyPI.
 
 From now on, we're going to use `python3` and `pip3` in code snippets, although your system might prefer simply `python` or `pip`. Just edit them.
 
 _Windows only_ Install Python from the Microsoft store, but then use `pip install windows-curses` to install curses.
 
+_Python developers only_ Busy does require other packages, so feel free to use a venv.
+
 Here's the command to install the latest stable version of Busy itself:
 
 ```
 sudo pip3 install busy && pip3 show busy
 ```
 
 If you have previously installed Busy, and want to upgrade to the latest version, type:
```

### Comparing `busy-3.4.2/busy/command/activate_command.py` & `busy-3.4.4/busy/command/activate_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/add_command.py` & `busy-3.4.4/busy/command/add_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/command.py` & `busy-3.4.4/busy/command/command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/defer_command.py` & `busy-3.4.4/busy/command/defer_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/delete_command.py` & `busy-3.4.4/busy/command/delete_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/drop_and_pop_command.py` & `busy-3.4.4/busy/command/drop_and_pop_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/edit_command.py` & `busy-3.4.4/busy/command/edit_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/finish_command.py` & `busy-3.4.4/busy/command/finish_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/list_command.py` & `busy-3.4.4/busy/command/list_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/command/switch_command.py` & `busy-3.4.4/busy/command/switch_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/handler.py` & `busy-3.4.4/busy/handler.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/model/item.py` & `busy-3.4.4/busy/model/item.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/model/task.py` & `busy-3.4.4/busy/model/task.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/queue/queue.py` & `busy-3.4.4/busy/queue/queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/queue/todo_queue.py` & `busy-3.4.4/busy/queue/todo_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/root/file_system_root.py` & `busy-3.4.4/busy/root/file_system_root.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,13 +1,15 @@
 from pathlib import Path
 from tempfile import TemporaryDirectory
 import os
 import subprocess
 from pathlib import Path
 
+from platformdirs import user_data_dir
+
 from busy.model.item import Item
 from busy.queue.queue import Queue
 from busy.model.item import read_items
 from busy.model.item import write_items
 
 
 class InvalidQueueNameError(Exception):
@@ -38,22 +40,21 @@
         else:
             Path(self._path).write_text('')
 
 
 class FileSystemRoot:
 
     def __init__(self, path=None):
-        if path:
-            self._path = Path(path) if isinstance(path, str) else path
-            assert isinstance(self._path, Path) and self._path.is_dir()
-        else:
-            env_var = os.environ.get('BUSY_ROOT')
-            self._path = Path(env_var if env_var else Path.home() / '.busy')
-            if not self._path.is_dir():
-                self._path.mkdir()
+        if not path:
+            path = os.environ.get('BUSY_ROOT')
+        if not path:
+            path = user_data_dir(appname='Busy', appauthor = 'SteampunkWizard')
+        self._path = Path(path) if not isinstance(path, Path) else path                
+        if not self._path.is_dir():
+            self._path.mkdir(parents=True)
         self._files = {}
         self._queues = {}
 
     @property
     def _str_path(self):
         return str(self._path.resolve())
```

### Comparing `busy-3.4.2/busy/selector.py` & `busy-3.4.4/busy/selector.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/ui/curses_ui.py` & `busy-3.4.4/busy/ui/curses_ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/ui/shell_ui.py` & `busy-3.4.4/busy/ui/shell_ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/ui/tcl_ui/edit_task_widget.py` & `busy-3.4.4/busy/ui/tcl_ui/edit_task_widget.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/ui/tcl_ui/get_item_widget.py` & `busy-3.4.4/busy/ui/tcl_ui/get_item_widget.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/ui/ui.py` & `busy-3.4.4/busy/ui/ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/util/class_family.py` & `busy-3.4.4/busy/util/class_family.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/util/date_util.py` & `busy-3.4.4/busy/util/date_util.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/util/readline_util.py` & `busy-3.4.4/busy/util/readline_util.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy/util/super_wrapper.py` & `busy-3.4.4/busy/util/super_wrapper.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/busy.egg-info/PKG-INFO` & `busy-3.4.4/busy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 Metadata-Version: 2.1
 Name: busy
-Version: 3.4.2
-Summary: Personal time management tool
-Home-page: http://gitlab.com/steampunk-wizard/busy
-Author: Francis Potter
-Author-email: busy@steampunkwizard.ca
+Version: 3.4.4
+Summary: Personal time management system
+Author-email: Francis Potter <busy@steampunkwizard.ca>
 License: MIT
+Requires-Python: >=3.6.5
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 Busy
 ====
 
 Busy is a personal time management tool, designed to help us all through our crazy busy days with as little stress as possible. It's simple, fast, and fun to use.
@@ -31,19 +30,19 @@
 - *Editable data*: The data is stored in text files, which can easily be edited outside of Busy itself. (In fact, Busy started as a todo.txt type of approach and grew from there.)
 
 _The idea of Importance over Urgency comes from the book "The 7 Habits of Highly Effective People". Although we firmly disagree with Steven Covey's statements on gay rights, the book contains excellent ideas._
 
 Installation
 ------------
 
-You'll need a terminal emulator to access a Bash-type prompt. Examples include:
+You'll need a terminal emulator to access a command or shell prompt. Examples include:
 
 - iTerm2 or Terminal on MacOS
 - Gnome Terminal or XTerm on Linux
-- Bash On Ubunto on Windows
+- CMD on Windows
 - Terminator on all platforms
 
 Busy also requires Python 3.6.5 or later. To check whether you already have the right version of Python on your system, start your terminal emulator and type:
 
 ```
 python -V
 ```
@@ -58,14 +57,16 @@
 
 Python comes with PIP, which enables installation of Python packages from a central server called PyPI.
 
 From now on, we're going to use `python3` and `pip3` in code snippets, although your system might prefer simply `python` or `pip`. Just edit them.
 
 _Windows only_ Install Python from the Microsoft store, but then use `pip install windows-curses` to install curses.
 
+_Python developers only_ Busy does require other packages, so feel free to use a venv.
+
 Here's the command to install the latest stable version of Busy itself:
 
 ```
 sudo pip3 install busy && pip3 show busy
 ```
 
 If you have previously installed Busy, and want to upgrade to the latest version, type:
```

### Comparing `busy-3.4.2/busy.egg-info/SOURCES.txt` & `busy-3.4.4/busy.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 LICENSE
 README.md
-setup.py
+pyproject.toml
+version
 busy/__init__.py
 busy/__main__.py
 busy/handler.py
 busy/selector.py
 busy.egg-info/PKG-INFO
 busy.egg-info/SOURCES.txt
 busy.egg-info/dependency_links.txt
 busy.egg-info/entry_points.txt
-busy.egg-info/not-zip-safe
+busy.egg-info/requires.txt
 busy.egg-info/top_level.txt
 busy/command/__init__.py
 busy/command/activate_command.py
 busy/command/add_command.py
 busy/command/base_command.py
 busy/command/command.py
 busy/command/curses_command.py
```

### Comparing `busy-3.4.2/sand/_textpad.py` & `busy-3.4.4/sand/_textpad.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/sand/subprocess.py` & `busy-3.4.4/sand/subprocess.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/sand/wrapper.py` & `busy-3.4.4/sand/wrapper.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/handler/test_handler.py` & `busy-3.4.4/test/handler/test_handler.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/model/test_item_io.py` & `busy-3.4.4/test/model/test_item_io.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/model/test_queue.py` & `busy-3.4.4/test/model/test_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/model/test_queue_replace.py` & `busy-3.4.4/test/model/test_queue_replace.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/model/test_task.py` & `busy-3.4.4/test/model/test_task.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/model/test_todo_queue.py` & `busy-3.4.4/test/model/test_todo_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/root/test_file.py` & `busy-3.4.4/test/root/test_file.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/root/test_file_system_root.py` & `busy-3.4.4/test/root/test_file_system_root.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/ui/test_ui_terminal_editor.py` & `busy-3.4.4/test/ui/test_ui_terminal_editor.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.2/test/util/test_class_families.py` & `busy-3.4.4/test/util/test_class_families.py`

 * *Files identical despite different names*

