# Comparing `tmp/busy-3.4.0.tar.gz` & `tmp/busy-3.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "busy-3.4.0.tar", last modified: Thu Apr  6 23:57:50 2023, max compression
+gzip compressed data, was "busy-3.4.1.tar", last modified: Fri Apr  7 00:03:25 2023, max compression
```

## Comparing `busy-3.4.0.tar` & `busy-3.4.1.tar`

### file list

```diff
@@ -1,108 +1,108 @@
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.989824 busy-3.4.0/
--rw-r--r--   0 francispotter   (501) staff       (20)     1071 2023-03-30 16:53:52.000000 busy-3.4.0/LICENSE
--rw-r--r--   0 francispotter   (501) staff       (20)    21646 2023-04-06 23:57:50.988780 busy-3.4.0/PKG-INFO
--rw-r--r--   0 francispotter   (501) staff       (20)    21381 2023-03-30 16:53:52.000000 busy-3.4.0/README.md
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.880285 busy-3.4.0/busy/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/busy/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)       66 2023-03-30 16:53:52.000000 busy-3.4.0/busy/__main__.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.907671 busy-3.4.0/busy/command/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1872 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/activate_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      825 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/add_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      245 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/base_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     8907 2023-04-06 23:37:22.000000 busy-3.4.0/busy/command/command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      279 2023-04-06 23:37:22.000000 busy-3.4.0/busy/command/curses_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1643 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/defer_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      981 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/delete_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-04-06 23:37:22.000000 busy-3.4.0/busy/command/drop_and_pop_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1309 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/edit_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1908 2023-04-06 23:37:22.000000 busy-3.4.0/busy/command/finish_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      681 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/list_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      212 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/queues_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      254 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/resource_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      950 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/switch_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      196 2023-03-30 16:53:52.000000 busy-3.4.0/busy/command/tags_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)      476 2023-04-06 23:37:22.000000 busy-3.4.0/busy/command/top_command.py
--rw-r--r--   0 francispotter   (501) staff       (20)     3945 2023-04-06 23:37:22.000000 busy-3.4.0/busy/handler.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.909286 busy-3.4.0/busy/model/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/busy/model/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1931 2023-04-06 23:37:22.000000 busy-3.4.0/busy/model/item.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2598 2023-03-30 16:53:52.000000 busy-3.4.0/busy/model/task.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.911849 busy-3.4.0/busy/queue/
--rw-r--r--   0 francispotter   (501) staff       (20)      102 2023-04-06 23:37:22.000000 busy-3.4.0/busy/queue/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     5099 2023-04-06 23:37:22.000000 busy-3.4.0/busy/queue/queue.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2139 2023-04-06 23:37:22.000000 busy-3.4.0/busy/queue/todo_queue.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.913246 busy-3.4.0/busy/root/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/busy/root/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2656 2023-04-06 23:37:22.000000 busy-3.4.0/busy/root/file_system_root.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2204 2023-03-30 16:53:52.000000 busy-3.4.0/busy/selector.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.916996 busy-3.4.0/busy/ui/
--rw-r--r--   0 francispotter   (501) staff       (20)      133 2023-03-30 16:53:52.000000 busy-3.4.0/busy/ui/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     6839 2023-04-06 23:37:22.000000 busy-3.4.0/busy/ui/curses_ui.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1573 2023-04-06 23:37:22.000000 busy-3.4.0/busy/ui/shell_ui.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.922267 busy-3.4.0/busy/ui/tcl_ui/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/busy/ui/tcl_ui/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      824 2023-03-30 16:53:52.000000 busy-3.4.0/busy/ui/tcl_ui/edit_task_widget.py
--rw-r--r--   0 francispotter   (501) staff       (20)      701 2023-03-30 16:53:52.000000 busy-3.4.0/busy/ui/tcl_ui/get_item_widget.py
--rw-r--r--   0 francispotter   (501) staff       (20)     5178 2023-04-06 23:37:22.000000 busy-3.4.0/busy/ui/ui.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.929080 busy-3.4.0/busy/util/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/busy/util/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     6682 2023-04-06 23:37:22.000000 busy-3.4.0/busy/util/class_family.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2882 2023-04-06 23:37:22.000000 busy-3.4.0/busy/util/date_util.py
--rw-r--r--   0 francispotter   (501) staff       (20)      217 2023-03-30 16:53:52.000000 busy-3.4.0/busy/util/python_version.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1231 2023-04-06 23:39:24.000000 busy-3.4.0/busy/util/readline_util.py
--rw-r--r--   0 francispotter   (501) staff       (20)      973 2023-03-30 16:53:52.000000 busy-3.4.0/busy/util/super_wrapper.py
--rw-r--r--   0 francispotter   (501) staff       (20)      131 2023-03-30 16:53:52.000000 busy-3.4.0/busy/util/textbox_util.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.884343 busy-3.4.0/busy.egg-info/
--rw-r--r--   0 francispotter   (501) staff       (20)    21646 2023-04-06 23:57:50.000000 busy-3.4.0/busy.egg-info/PKG-INFO
--rw-r--r--   0 francispotter   (501) staff       (20)     2208 2023-04-06 23:57:50.000000 busy-3.4.0/busy.egg-info/SOURCES.txt
--rw-r--r--   0 francispotter   (501) staff       (20)        1 2023-04-06 23:57:50.000000 busy-3.4.0/busy.egg-info/dependency_links.txt
--rw-r--r--   0 francispotter   (501) staff       (20)       44 2023-04-06 23:57:50.000000 busy-3.4.0/busy.egg-info/entry_points.txt
--rw-r--r--   0 francispotter   (501) staff       (20)        1 2023-01-01 23:16:57.000000 busy-3.4.0/busy.egg-info/not-zip-safe
--rw-r--r--   0 francispotter   (501) staff       (20)       15 2023-04-06 23:57:50.000000 busy-3.4.0/busy.egg-info/top_level.txt
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.935935 busy-3.4.0/sand/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-02-25 16:13:53.000000 busy-3.4.0/sand/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      336 2023-02-23 13:30:28.000000 busy-3.4.0/sand/_dataclass.py
--rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-04-05 00:41:16.000000 busy-3.4.0/sand/_readline_util.py
--rw-r--r--   0 francispotter   (501) staff       (20)      676 2023-02-25 17:04:15.000000 busy-3.4.0/sand/_textpad.py
--rw-r--r--   0 francispotter   (501) staff       (20)      233 2023-03-06 16:05:27.000000 busy-3.4.0/sand/chooser.py
--rw-r--r--   0 francispotter   (501) staff       (20)      282 2023-03-01 14:38:38.000000 busy-3.4.0/sand/rl-io.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-03-01 15:07:59.000000 busy-3.4.0/sand/subprocess.py
--rw-r--r--   0 francispotter   (501) staff       (20)      806 2023-03-02 16:10:26.000000 busy-3.4.0/sand/wrapper.py
--rw-r--r--   0 francispotter   (501) staff       (20)       38 2023-04-06 23:57:50.989964 busy-3.4.0/setup.cfg
--rw-r--r--   0 francispotter   (501) staff       (20)      742 2023-03-30 16:53:52.000000 busy-3.4.0/setup.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.936619 busy-3.4.0/test/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/test/__init__.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.939882 busy-3.4.0/test/data_class_family/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/test/data_class_family/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      101 2023-03-30 16:53:52.000000 busy-3.4.0/test/data_class_family/atriarch.py
--rw-r--r--   0 francispotter   (501) staff       (20)       76 2023-03-30 16:53:52.000000 busy-3.4.0/test/data_class_family/child.py
--rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-03-30 16:53:52.000000 busy-3.4.0/test/data_class_family/grandchild.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.942750 busy-3.4.0/test/handler/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/test/handler/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1205 2023-03-30 16:53:52.000000 busy-3.4.0/test/handler/test_handler.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.962465 busy-3.4.0/test/integration/
--rw-r--r--   0 francispotter   (501) staff       (20)      150 2023-04-06 23:37:22.000000 busy-3.4.0/test/integration/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      416 2023-04-06 23:37:22.000000 busy-3.4.0/test/integration/test_integration.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.970865 busy-3.4.0/test/model/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/test/model/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      433 2023-04-06 23:37:22.000000 busy-3.4.0/test/model/test_item.py
--rw-r--r--   0 francispotter   (501) staff       (20)      845 2023-04-06 23:37:22.000000 busy-3.4.0/test/model/test_item_io.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2857 2023-04-06 23:37:22.000000 busy-3.4.0/test/model/test_queue.py
--rw-r--r--   0 francispotter   (501) staff       (20)      624 2023-04-06 23:37:22.000000 busy-3.4.0/test/model/test_queue_replace.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1778 2023-04-06 23:37:22.000000 busy-3.4.0/test/model/test_task.py
--rw-r--r--   0 francispotter   (501) staff       (20)     4056 2023-04-06 23:37:22.000000 busy-3.4.0/test/model/test_todo_queue.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.975059 busy-3.4.0/test/root/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-04-06 23:37:22.000000 busy-3.4.0/test/root/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)     1406 2023-04-06 23:37:22.000000 busy-3.4.0/test/root/test_file.py
--rw-r--r--   0 francispotter   (501) staff       (20)     2529 2023-04-06 23:37:22.000000 busy-3.4.0/test/root/test_file_system_root.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.983656 busy-3.4.0/test/ui/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/test/ui/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      357 2023-03-30 16:53:52.000000 busy-3.4.0/test/ui/test_shell_ui.py
--rw-r--r--   0 francispotter   (501) staff       (20)      790 2023-03-30 16:53:52.000000 busy-3.4.0/test/ui/test_ui_terminal_editor.py
-drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-06 23:57:50.987766 busy-3.4.0/test/util/
--rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.0/test/util/__init__.py
--rw-r--r--   0 francispotter   (501) staff       (20)      797 2023-04-06 23:37:22.000000 busy-3.4.0/test/util/test_class_families.py
--rw-r--r--   0 francispotter   (501) staff       (20)      237 2023-03-30 16:53:52.000000 busy-3.4.0/test/util/test_class_family.py
--rw-r--r--   0 francispotter   (501) staff       (20)      452 2023-03-30 16:53:52.000000 busy-3.4.0/test/util/test_date.py
--rw-r--r--   0 francispotter   (501) staff       (20)      508 2023-03-30 16:53:52.000000 busy-3.4.0/test/util/test_python_version.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.866766 busy-3.4.1/
+-rw-r--r--   0 francispotter   (501) staff       (20)     1071 2023-03-30 16:53:52.000000 busy-3.4.1/LICENSE
+-rw-r--r--   0 francispotter   (501) staff       (20)    21774 2023-04-07 00:03:25.865909 busy-3.4.1/PKG-INFO
+-rw-r--r--   0 francispotter   (501) staff       (20)    21499 2023-04-07 00:00:49.000000 busy-3.4.1/README.md
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.652227 busy-3.4.1/busy/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/busy/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       66 2023-03-30 16:53:52.000000 busy-3.4.1/busy/__main__.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.683573 busy-3.4.1/busy/command/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1872 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/activate_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      825 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/add_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      245 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/base_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     8907 2023-04-06 23:37:22.000000 busy-3.4.1/busy/command/command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      279 2023-04-06 23:37:22.000000 busy-3.4.1/busy/command/curses_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1643 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/defer_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      981 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/delete_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-04-06 23:37:22.000000 busy-3.4.1/busy/command/drop_and_pop_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1309 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/edit_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1908 2023-04-06 23:37:22.000000 busy-3.4.1/busy/command/finish_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      681 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/list_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      212 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/queues_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      254 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/resource_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      950 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/switch_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      196 2023-03-30 16:53:52.000000 busy-3.4.1/busy/command/tags_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      476 2023-04-06 23:37:22.000000 busy-3.4.1/busy/command/top_command.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     3945 2023-04-06 23:37:22.000000 busy-3.4.1/busy/handler.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.687841 busy-3.4.1/busy/model/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/busy/model/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1931 2023-04-06 23:37:22.000000 busy-3.4.1/busy/model/item.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2598 2023-03-30 16:53:52.000000 busy-3.4.1/busy/model/task.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.689895 busy-3.4.1/busy/queue/
+-rw-r--r--   0 francispotter   (501) staff       (20)      102 2023-04-06 23:37:22.000000 busy-3.4.1/busy/queue/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     5099 2023-04-06 23:37:22.000000 busy-3.4.1/busy/queue/queue.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2139 2023-04-06 23:37:22.000000 busy-3.4.1/busy/queue/todo_queue.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.690893 busy-3.4.1/busy/root/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/busy/root/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2297 2023-04-07 00:01:46.000000 busy-3.4.1/busy/root/file_system_root.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2204 2023-03-30 16:53:52.000000 busy-3.4.1/busy/selector.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.694454 busy-3.4.1/busy/ui/
+-rw-r--r--   0 francispotter   (501) staff       (20)      133 2023-03-30 16:53:52.000000 busy-3.4.1/busy/ui/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     6839 2023-04-06 23:37:22.000000 busy-3.4.1/busy/ui/curses_ui.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1573 2023-04-06 23:37:22.000000 busy-3.4.1/busy/ui/shell_ui.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.697251 busy-3.4.1/busy/ui/tcl_ui/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/busy/ui/tcl_ui/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      824 2023-03-30 16:53:52.000000 busy-3.4.1/busy/ui/tcl_ui/edit_task_widget.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      701 2023-03-30 16:53:52.000000 busy-3.4.1/busy/ui/tcl_ui/get_item_widget.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     5178 2023-04-06 23:37:22.000000 busy-3.4.1/busy/ui/ui.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.701214 busy-3.4.1/busy/util/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/busy/util/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     6682 2023-04-06 23:37:22.000000 busy-3.4.1/busy/util/class_family.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2882 2023-04-06 23:37:22.000000 busy-3.4.1/busy/util/date_util.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      217 2023-03-30 16:53:52.000000 busy-3.4.1/busy/util/python_version.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1231 2023-04-06 23:39:24.000000 busy-3.4.1/busy/util/readline_util.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      973 2023-03-30 16:53:52.000000 busy-3.4.1/busy/util/super_wrapper.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      131 2023-03-30 16:53:52.000000 busy-3.4.1/busy/util/textbox_util.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.663597 busy-3.4.1/busy.egg-info/
+-rw-r--r--   0 francispotter   (501) staff       (20)    21774 2023-04-07 00:03:25.000000 busy-3.4.1/busy.egg-info/PKG-INFO
+-rw-r--r--   0 francispotter   (501) staff       (20)     2208 2023-04-07 00:03:25.000000 busy-3.4.1/busy.egg-info/SOURCES.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)        1 2023-04-07 00:03:25.000000 busy-3.4.1/busy.egg-info/dependency_links.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)       44 2023-04-07 00:03:25.000000 busy-3.4.1/busy.egg-info/entry_points.txt
+-rw-r--r--   0 francispotter   (501) staff       (20)        1 2023-01-01 23:16:57.000000 busy-3.4.1/busy.egg-info/not-zip-safe
+-rw-r--r--   0 francispotter   (501) staff       (20)       15 2023-04-07 00:03:25.000000 busy-3.4.1/busy.egg-info/top_level.txt
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.719947 busy-3.4.1/sand/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-02-25 16:13:53.000000 busy-3.4.1/sand/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      336 2023-02-23 13:30:28.000000 busy-3.4.1/sand/_dataclass.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-04-05 00:41:16.000000 busy-3.4.1/sand/_readline_util.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      676 2023-02-25 17:04:15.000000 busy-3.4.1/sand/_textpad.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      233 2023-03-06 16:05:27.000000 busy-3.4.1/sand/chooser.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      282 2023-03-01 14:38:38.000000 busy-3.4.1/sand/rl-io.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1333 2023-03-01 15:07:59.000000 busy-3.4.1/sand/subprocess.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      806 2023-03-02 16:10:26.000000 busy-3.4.1/sand/wrapper.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       38 2023-04-07 00:03:25.867016 busy-3.4.1/setup.cfg
+-rw-r--r--   0 francispotter   (501) staff       (20)      752 2023-04-07 00:02:23.000000 busy-3.4.1/setup.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.722372 busy-3.4.1/test/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/test/__init__.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.730433 busy-3.4.1/test/data_class_family/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/test/data_class_family/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      101 2023-03-30 16:53:52.000000 busy-3.4.1/test/data_class_family/atriarch.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       76 2023-03-30 16:53:52.000000 busy-3.4.1/test/data_class_family/child.py
+-rw-r--r--   0 francispotter   (501) staff       (20)       74 2023-03-30 16:53:52.000000 busy-3.4.1/test/data_class_family/grandchild.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.734134 busy-3.4.1/test/handler/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/test/handler/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1205 2023-03-30 16:53:52.000000 busy-3.4.1/test/handler/test_handler.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.745028 busy-3.4.1/test/integration/
+-rw-r--r--   0 francispotter   (501) staff       (20)      150 2023-04-06 23:37:22.000000 busy-3.4.1/test/integration/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      416 2023-04-06 23:37:22.000000 busy-3.4.1/test/integration/test_integration.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.852752 busy-3.4.1/test/model/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/test/model/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      433 2023-04-06 23:37:22.000000 busy-3.4.1/test/model/test_item.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      845 2023-04-06 23:37:22.000000 busy-3.4.1/test/model/test_item_io.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2857 2023-04-06 23:37:22.000000 busy-3.4.1/test/model/test_queue.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      624 2023-04-06 23:37:22.000000 busy-3.4.1/test/model/test_queue_replace.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1778 2023-04-06 23:37:22.000000 busy-3.4.1/test/model/test_task.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     4056 2023-04-06 23:37:22.000000 busy-3.4.1/test/model/test_todo_queue.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.854666 busy-3.4.1/test/root/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-04-06 23:37:22.000000 busy-3.4.1/test/root/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     1406 2023-04-06 23:37:22.000000 busy-3.4.1/test/root/test_file.py
+-rw-r--r--   0 francispotter   (501) staff       (20)     2529 2023-04-06 23:37:22.000000 busy-3.4.1/test/root/test_file_system_root.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.856469 busy-3.4.1/test/ui/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/test/ui/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      357 2023-03-30 16:53:52.000000 busy-3.4.1/test/ui/test_shell_ui.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      790 2023-03-30 16:53:52.000000 busy-3.4.1/test/ui/test_ui_terminal_editor.py
+drwxr-xr-x   0 francispotter   (501) staff       (20)        0 2023-04-07 00:03:25.861964 busy-3.4.1/test/util/
+-rw-r--r--   0 francispotter   (501) staff       (20)        0 2023-03-30 16:53:52.000000 busy-3.4.1/test/util/__init__.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      797 2023-04-06 23:37:22.000000 busy-3.4.1/test/util/test_class_families.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      237 2023-03-30 16:53:52.000000 busy-3.4.1/test/util/test_class_family.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      452 2023-03-30 16:53:52.000000 busy-3.4.1/test/util/test_date.py
+-rw-r--r--   0 francispotter   (501) staff       (20)      508 2023-03-30 16:53:52.000000 busy-3.4.1/test/util/test_python_version.py
```

### Comparing `busy-3.4.0/LICENSE` & `busy-3.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/PKG-INFO` & `busy-3.4.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 Metadata-Version: 2.1
 Name: busy
-Version: 3.4.0
+Version: 3.4.1
 Summary: Personal time management tool
-Home-page: http://gitlab.com/fpotter/tools/busy
+Home-page: http://gitlab.com/steampunk-wizard/busy
 Author: Francis Potter
-Author-email: busy@fpotter.com
+Author-email: busy@steampunkwizard.ca
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 Busy
 ====
 
@@ -56,14 +56,16 @@
 
 If you don't have Python, or your version is out of date, install or upgrade it. In most cases, you'll want to do so using your system's package manager (such as Homebrew on MacOS or APT on Linux). If you're not familiar with package managers, then download Python from [the Python.org site](https://www.python.org/downloads/) directly and follow the instructions provided there. When done, use the version check above to confirm it's installed and the version is 3.6.5 or greater.
 
 Python comes with PIP, which enables installation of Python packages from a central server called PyPI.
 
 From now on, we're going to use `python3` and `pip3` in code snippets, although your system might prefer simply `python` or `pip`. Just edit them.
 
+_Windows only_ Install Python from the Microsoft store, but then use `pip install windows-curses` to install curses.
+
 Here's the command to install the latest stable version of Busy itself:
 
 ```
 sudo pip3 install busy && pip3 show busy
 ```
 
 If you have previously installed Busy, and want to upgrade to the latest version, type:
```

### Comparing `busy-3.4.0/README.md` & `busy-3.4.1/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -45,14 +45,16 @@
 
 If you don't have Python, or your version is out of date, install or upgrade it. In most cases, you'll want to do so using your system's package manager (such as Homebrew on MacOS or APT on Linux). If you're not familiar with package managers, then download Python from [the Python.org site](https://www.python.org/downloads/) directly and follow the instructions provided there. When done, use the version check above to confirm it's installed and the version is 3.6.5 or greater.
 
 Python comes with PIP, which enables installation of Python packages from a central server called PyPI.
 
 From now on, we're going to use `python3` and `pip3` in code snippets, although your system might prefer simply `python` or `pip`. Just edit them.
 
+_Windows only_ Install Python from the Microsoft store, but then use `pip install windows-curses` to install curses.
+
 Here's the command to install the latest stable version of Busy itself:
 
 ```
 sudo pip3 install busy && pip3 show busy
 ```
 
 If you have previously installed Busy, and want to upgrade to the latest version, type:
```

### Comparing `busy-3.4.0/busy/command/activate_command.py` & `busy-3.4.1/busy/command/activate_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/add_command.py` & `busy-3.4.1/busy/command/add_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/command.py` & `busy-3.4.1/busy/command/command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/defer_command.py` & `busy-3.4.1/busy/command/defer_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/delete_command.py` & `busy-3.4.1/busy/command/delete_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/drop_and_pop_command.py` & `busy-3.4.1/busy/command/drop_and_pop_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/edit_command.py` & `busy-3.4.1/busy/command/edit_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/finish_command.py` & `busy-3.4.1/busy/command/finish_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/list_command.py` & `busy-3.4.1/busy/command/list_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/command/switch_command.py` & `busy-3.4.1/busy/command/switch_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/handler.py` & `busy-3.4.1/busy/handler.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/model/item.py` & `busy-3.4.1/busy/model/item.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/model/task.py` & `busy-3.4.1/busy/model/task.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/queue/queue.py` & `busy-3.4.1/busy/queue/queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/queue/todo_queue.py` & `busy-3.4.1/busy/queue/todo_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/root/file_system_root.py` & `busy-3.4.1/busy/root/file_system_root.py`

 * *Files 5% similar despite different names*

```diff
@@ -46,27 +46,21 @@
             self._path = Path(path) if isinstance(path, str) else path
             assert isinstance(self._path, Path) and self._path.is_dir()
         else:
             env_var = os.environ.get('BUSY_ROOT')
             self._path = Path(env_var if env_var else Path.home() / '.busy')
             if not self._path.is_dir():
                 self._path.mkdir()
-        is_git = self.git('rev-parse', check=False)
-        if is_git.returncode > 0:
-            self.git('init')
         self._files = {}
         self._queues = {}
 
     @property
     def _str_path(self):
         return str(self._path.resolve())
 
-    def git(self, command, **kwargs):
-        return subprocess.run(f'git -C {self._str_path} {command}'.split(), capture_output=True, **kwargs)
-
     def get_queue(self, name):
         if name not in self._queues:
             queueclass = Queue.family_member('name', name) or Queue
             queuefile = File(self._path / f'{name}.txt')
             self._files[name] = queuefile
             items = queuefile.read(queueclass.itemclass)
             self._queues[name] = queueclass(self, items)
@@ -76,16 +70,13 @@
         changed = False
         while self._queues:
             key, queue = self._queues.popitem()
             if queue.changed:
                 items = queue.all()
                 self._files[key].save(*items)
                 changed = True
-        # if changed:
-        #     self.git('add -A')
-        #     self.git('commit -m change')
 
     @property
     def queue_names(self):
         filenames = list(self._path.glob('*.txt'))
         keys = [Path(f).stem for f in filenames]
         return keys
```

### Comparing `busy-3.4.0/busy/selector.py` & `busy-3.4.1/busy/selector.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/ui/curses_ui.py` & `busy-3.4.1/busy/ui/curses_ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/ui/shell_ui.py` & `busy-3.4.1/busy/ui/shell_ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/ui/tcl_ui/edit_task_widget.py` & `busy-3.4.1/busy/ui/tcl_ui/edit_task_widget.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/ui/tcl_ui/get_item_widget.py` & `busy-3.4.1/busy/ui/tcl_ui/get_item_widget.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/ui/ui.py` & `busy-3.4.1/busy/ui/ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/util/class_family.py` & `busy-3.4.1/busy/util/class_family.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/util/date_util.py` & `busy-3.4.1/busy/util/date_util.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/util/readline_util.py` & `busy-3.4.1/busy/util/readline_util.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy/util/super_wrapper.py` & `busy-3.4.1/busy/util/super_wrapper.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/busy.egg-info/PKG-INFO` & `busy-3.4.1/busy.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 Metadata-Version: 2.1
 Name: busy
-Version: 3.4.0
+Version: 3.4.1
 Summary: Personal time management tool
-Home-page: http://gitlab.com/fpotter/tools/busy
+Home-page: http://gitlab.com/steampunk-wizard/busy
 Author: Francis Potter
-Author-email: busy@fpotter.com
+Author-email: busy@steampunkwizard.ca
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 Busy
 ====
 
@@ -56,14 +56,16 @@
 
 If you don't have Python, or your version is out of date, install or upgrade it. In most cases, you'll want to do so using your system's package manager (such as Homebrew on MacOS or APT on Linux). If you're not familiar with package managers, then download Python from [the Python.org site](https://www.python.org/downloads/) directly and follow the instructions provided there. When done, use the version check above to confirm it's installed and the version is 3.6.5 or greater.
 
 Python comes with PIP, which enables installation of Python packages from a central server called PyPI.
 
 From now on, we're going to use `python3` and `pip3` in code snippets, although your system might prefer simply `python` or `pip`. Just edit them.
 
+_Windows only_ Install Python from the Microsoft store, but then use `pip install windows-curses` to install curses.
+
 Here's the command to install the latest stable version of Busy itself:
 
 ```
 sudo pip3 install busy && pip3 show busy
 ```
 
 If you have previously installed Busy, and want to upgrade to the latest version, type:
```

### Comparing `busy-3.4.0/busy.egg-info/SOURCES.txt` & `busy-3.4.1/busy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/sand/_textpad.py` & `busy-3.4.1/sand/_textpad.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/sand/subprocess.py` & `busy-3.4.1/sand/subprocess.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/sand/wrapper.py` & `busy-3.4.1/sand/wrapper.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/setup.py` & `busy-3.4.1/setup.py`

 * *Files 18% similar despite different names*

```diff
@@ -9,14 +9,14 @@
 long_description = (Path(__file__).parent / 'README.md').read_text()
 
 setup(name='busy',
       version=version,
       description='Personal time management tool',
       long_description=long_description,
       long_description_content_type='text/markdown',
-      url='http://gitlab.com/fpotter/tools/busy',
+      url='http://gitlab.com/steampunk-wizard/busy',
       author='Francis Potter',
-      author_email='busy@fpotter.com',
+      author_email='busy@steampunkwizard.ca',
       license='MIT',
       packages=find_packages(),
       entry_points={'console_scripts':['busy=busy.__main__:main']},
       zip_safe=False)
```

### Comparing `busy-3.4.0/test/handler/test_handler.py` & `busy-3.4.1/test/handler/test_handler.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/model/test_item_io.py` & `busy-3.4.1/test/model/test_item_io.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/model/test_queue.py` & `busy-3.4.1/test/model/test_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/model/test_queue_replace.py` & `busy-3.4.1/test/model/test_queue_replace.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/model/test_task.py` & `busy-3.4.1/test/model/test_task.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/model/test_todo_queue.py` & `busy-3.4.1/test/model/test_todo_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/root/test_file.py` & `busy-3.4.1/test/root/test_file.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/root/test_file_system_root.py` & `busy-3.4.1/test/root/test_file_system_root.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/ui/test_ui_terminal_editor.py` & `busy-3.4.1/test/ui/test_ui_terminal_editor.py`

 * *Files identical despite different names*

### Comparing `busy-3.4.0/test/util/test_class_families.py` & `busy-3.4.1/test/util/test_class_families.py`

 * *Files identical despite different names*

