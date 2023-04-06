# Comparing `tmp/busy-3.2.0.tar.gz` & `tmp/busy-3.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "busy-3.2.0.tar", last modified: Wed Mar  8 14:56:31 2023, max compression
+gzip compressed data, was "busy-3.3.0.tar", last modified: Thu Apr  6 23:42:10 2023, max compression
```

## Comparing `busy-3.2.0.tar` & `busy-3.3.0.tar`

### file list

```diff
@@ -1,99 +1,99 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.088001 busy-3.2.0/
--rw-rw-rw-   0 root         (0) root         (0)     1071 2023-03-08 14:56:21.000000 busy-3.2.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)    21646 2023-03-08 14:56:31.087001 busy-3.2.0/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)    21381 2023-03-08 14:56:21.000000 busy-3.2.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.064999 busy-3.2.0/busy/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/busy/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)       66 2023-03-08 14:56:21.000000 busy-3.2.0/busy/__main__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.071999 busy-3.2.0/busy/command/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1872 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/activate_command.py
--rw-rw-rw-   0 root         (0) root         (0)      825 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/add_command.py
--rw-rw-rw-   0 root         (0) root         (0)      245 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/base_command.py
--rw-rw-rw-   0 root         (0) root         (0)     8907 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/command.py
--rw-rw-rw-   0 root         (0) root         (0)      279 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/curses_command.py
--rw-rw-rw-   0 root         (0) root         (0)     1643 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/defer_command.py
--rw-rw-rw-   0 root         (0) root         (0)      981 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/delete_command.py
--rw-rw-rw-   0 root         (0) root         (0)     1333 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/drop_and_pop_command.py
--rw-rw-rw-   0 root         (0) root         (0)     1309 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/edit_command.py
--rw-rw-rw-   0 root         (0) root         (0)     1908 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/finish_command.py
--rw-rw-rw-   0 root         (0) root         (0)      681 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/list_command.py
--rw-rw-rw-   0 root         (0) root         (0)      212 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/queues_command.py
--rw-rw-rw-   0 root         (0) root         (0)      254 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/resource_command.py
--rw-rw-rw-   0 root         (0) root         (0)      950 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/switch_command.py
--rw-rw-rw-   0 root         (0) root         (0)      196 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/tags_command.py
--rw-rw-rw-   0 root         (0) root         (0)      476 2023-03-08 14:56:21.000000 busy-3.2.0/busy/command/top_command.py
--rw-rw-rw-   0 root         (0) root         (0)     3945 2023-03-08 14:56:21.000000 busy-3.2.0/busy/handler.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.073000 busy-3.2.0/busy/model/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/busy/model/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1931 2023-03-08 14:56:21.000000 busy-3.2.0/busy/model/item.py
--rw-rw-rw-   0 root         (0) root         (0)     2598 2023-03-08 14:56:21.000000 busy-3.2.0/busy/model/task.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.074000 busy-3.2.0/busy/queue/
--rw-rw-rw-   0 root         (0) root         (0)      102 2023-03-08 14:56:21.000000 busy-3.2.0/busy/queue/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     5099 2023-03-08 14:56:21.000000 busy-3.2.0/busy/queue/queue.py
--rw-rw-rw-   0 root         (0) root         (0)     2139 2023-03-08 14:56:21.000000 busy-3.2.0/busy/queue/todo_queue.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.075000 busy-3.2.0/busy/root/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/busy/root/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2656 2023-03-08 14:56:21.000000 busy-3.2.0/busy/root/file_system_root.py
--rw-rw-rw-   0 root         (0) root         (0)     2204 2023-03-08 14:56:21.000000 busy-3.2.0/busy/selector.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.076000 busy-3.2.0/busy/ui/
--rw-rw-rw-   0 root         (0) root         (0)      133 2023-03-08 14:56:21.000000 busy-3.2.0/busy/ui/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     6839 2023-03-08 14:56:21.000000 busy-3.2.0/busy/ui/curses_ui.py
--rw-rw-rw-   0 root         (0) root         (0)     1573 2023-03-08 14:56:21.000000 busy-3.2.0/busy/ui/shell_ui.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.077000 busy-3.2.0/busy/ui/tcl_ui/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/busy/ui/tcl_ui/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      824 2023-03-08 14:56:21.000000 busy-3.2.0/busy/ui/tcl_ui/edit_task_widget.py
--rw-rw-rw-   0 root         (0) root         (0)      701 2023-03-08 14:56:21.000000 busy-3.2.0/busy/ui/tcl_ui/get_item_widget.py
--rw-rw-rw-   0 root         (0) root         (0)     5178 2023-03-08 14:56:21.000000 busy-3.2.0/busy/ui/ui.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.079000 busy-3.2.0/busy/util/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/busy/util/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     6682 2023-03-08 14:56:21.000000 busy-3.2.0/busy/util/class_family.py
--rw-rw-rw-   0 root         (0) root         (0)     2882 2023-03-08 14:56:21.000000 busy-3.2.0/busy/util/date_util.py
--rw-rw-rw-   0 root         (0) root         (0)      217 2023-03-08 14:56:21.000000 busy-3.2.0/busy/util/python_version.py
--rw-rw-rw-   0 root         (0) root         (0)     1231 2023-03-08 14:56:21.000000 busy-3.2.0/busy/util/readline_util.py
--rw-rw-rw-   0 root         (0) root         (0)      973 2023-03-08 14:56:21.000000 busy-3.2.0/busy/util/super_wrapper.py
--rw-rw-rw-   0 root         (0) root         (0)      131 2023-03-08 14:56:21.000000 busy-3.2.0/busy/util/textbox_util.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.066999 busy-3.2.0/busy.egg-info/
--rw-r--r--   0 root         (0) root         (0)    21646 2023-03-08 14:56:31.000000 busy-3.2.0/busy.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2067 2023-03-08 14:56:31.000000 busy-3.2.0/busy.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-08 14:56:31.000000 busy-3.2.0/busy.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       44 2023-03-08 14:56:31.000000 busy-3.2.0/busy.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-08 14:56:31.000000 busy-3.2.0/busy.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       10 2023-03-08 14:56:31.000000 busy-3.2.0/busy.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-08 14:56:31.088001 busy-3.2.0/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      742 2023-03-08 14:56:21.000000 busy-3.2.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.079000 busy-3.2.0/test/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/test/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.080000 busy-3.2.0/test/data_class_family/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/test/data_class_family/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      101 2023-03-08 14:56:21.000000 busy-3.2.0/test/data_class_family/atriarch.py
--rw-rw-rw-   0 root         (0) root         (0)       76 2023-03-08 14:56:21.000000 busy-3.2.0/test/data_class_family/child.py
--rw-rw-rw-   0 root         (0) root         (0)       74 2023-03-08 14:56:21.000000 busy-3.2.0/test/data_class_family/grandchild.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.081000 busy-3.2.0/test/handler/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/test/handler/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1205 2023-03-08 14:56:21.000000 busy-3.2.0/test/handler/test_handler.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.082000 busy-3.2.0/test/integration/
--rw-rw-rw-   0 root         (0) root         (0)      150 2023-03-08 14:56:21.000000 busy-3.2.0/test/integration/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      416 2023-03-08 14:56:21.000000 busy-3.2.0/test/integration/test_integration.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.084000 busy-3.2.0/test/model/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/test/model/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      433 2023-03-08 14:56:21.000000 busy-3.2.0/test/model/test_item.py
--rw-rw-rw-   0 root         (0) root         (0)      845 2023-03-08 14:56:21.000000 busy-3.2.0/test/model/test_item_io.py
--rw-rw-rw-   0 root         (0) root         (0)     2857 2023-03-08 14:56:21.000000 busy-3.2.0/test/model/test_queue.py
--rw-rw-rw-   0 root         (0) root         (0)      624 2023-03-08 14:56:21.000000 busy-3.2.0/test/model/test_queue_replace.py
--rw-rw-rw-   0 root         (0) root         (0)     1778 2023-03-08 14:56:21.000000 busy-3.2.0/test/model/test_task.py
--rw-rw-rw-   0 root         (0) root         (0)     4056 2023-03-08 14:56:21.000000 busy-3.2.0/test/model/test_todo_queue.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.085001 busy-3.2.0/test/root/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/test/root/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1406 2023-03-08 14:56:21.000000 busy-3.2.0/test/root/test_file.py
--rw-rw-rw-   0 root         (0) root         (0)     2529 2023-03-08 14:56:21.000000 busy-3.2.0/test/root/test_file_system_root.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.086001 busy-3.2.0/test/ui/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/test/ui/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      357 2023-03-08 14:56:21.000000 busy-3.2.0/test/ui/test_shell_ui.py
--rw-rw-rw-   0 root         (0) root         (0)      790 2023-03-08 14:56:21.000000 busy-3.2.0/test/ui/test_ui_terminal_editor.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-08 14:56:31.087001 busy-3.2.0/test/util/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-08 14:56:21.000000 busy-3.2.0/test/util/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      797 2023-03-08 14:56:21.000000 busy-3.2.0/test/util/test_class_families.py
--rw-rw-rw-   0 root         (0) root         (0)      237 2023-03-08 14:56:21.000000 busy-3.2.0/test/util/test_class_family.py
--rw-rw-rw-   0 root         (0) root         (0)      452 2023-03-08 14:56:21.000000 busy-3.2.0/test/util/test_date.py
--rw-rw-rw-   0 root         (0) root         (0)      508 2023-03-08 14:56:21.000000 busy-3.2.0/test/util/test_python_version.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.328209 busy-3.3.0/
+-rw-rw-rw-   0 root         (0) root         (0)     1071 2023-04-06 23:41:59.000000 busy-3.3.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)    21646 2023-04-06 23:42:10.327209 busy-3.3.0/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)    21381 2023-04-06 23:41:59.000000 busy-3.3.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.304207 busy-3.3.0/busy/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/busy/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)       66 2023-04-06 23:41:59.000000 busy-3.3.0/busy/__main__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.311208 busy-3.3.0/busy/command/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1872 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/activate_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      825 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/add_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      245 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/base_command.py
+-rw-rw-rw-   0 root         (0) root         (0)     8907 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/command.py
+-rw-rw-rw-   0 root         (0) root         (0)      279 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/curses_command.py
+-rw-rw-rw-   0 root         (0) root         (0)     1643 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/defer_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      981 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/delete_command.py
+-rw-rw-rw-   0 root         (0) root         (0)     1333 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/drop_and_pop_command.py
+-rw-rw-rw-   0 root         (0) root         (0)     1309 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/edit_command.py
+-rw-rw-rw-   0 root         (0) root         (0)     1908 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/finish_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      681 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/list_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      212 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/queues_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      254 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/resource_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      950 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/switch_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      196 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/tags_command.py
+-rw-rw-rw-   0 root         (0) root         (0)      476 2023-04-06 23:41:59.000000 busy-3.3.0/busy/command/top_command.py
+-rw-rw-rw-   0 root         (0) root         (0)     3945 2023-04-06 23:41:59.000000 busy-3.3.0/busy/handler.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.312208 busy-3.3.0/busy/model/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/busy/model/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1931 2023-04-06 23:41:59.000000 busy-3.3.0/busy/model/item.py
+-rw-rw-rw-   0 root         (0) root         (0)     2598 2023-04-06 23:41:59.000000 busy-3.3.0/busy/model/task.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.313208 busy-3.3.0/busy/queue/
+-rw-rw-rw-   0 root         (0) root         (0)      102 2023-04-06 23:41:59.000000 busy-3.3.0/busy/queue/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     5099 2023-04-06 23:41:59.000000 busy-3.3.0/busy/queue/queue.py
+-rw-rw-rw-   0 root         (0) root         (0)     2139 2023-04-06 23:41:59.000000 busy-3.3.0/busy/queue/todo_queue.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.314208 busy-3.3.0/busy/root/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/busy/root/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2656 2023-04-06 23:41:59.000000 busy-3.3.0/busy/root/file_system_root.py
+-rw-rw-rw-   0 root         (0) root         (0)     2204 2023-04-06 23:41:59.000000 busy-3.3.0/busy/selector.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.315208 busy-3.3.0/busy/ui/
+-rw-rw-rw-   0 root         (0) root         (0)      133 2023-04-06 23:41:59.000000 busy-3.3.0/busy/ui/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     6839 2023-04-06 23:41:59.000000 busy-3.3.0/busy/ui/curses_ui.py
+-rw-rw-rw-   0 root         (0) root         (0)     1573 2023-04-06 23:41:59.000000 busy-3.3.0/busy/ui/shell_ui.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.316208 busy-3.3.0/busy/ui/tcl_ui/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/busy/ui/tcl_ui/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      824 2023-04-06 23:41:59.000000 busy-3.3.0/busy/ui/tcl_ui/edit_task_widget.py
+-rw-rw-rw-   0 root         (0) root         (0)      701 2023-04-06 23:41:59.000000 busy-3.3.0/busy/ui/tcl_ui/get_item_widget.py
+-rw-rw-rw-   0 root         (0) root         (0)     5178 2023-04-06 23:41:59.000000 busy-3.3.0/busy/ui/ui.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.318208 busy-3.3.0/busy/util/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/busy/util/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     6682 2023-04-06 23:41:59.000000 busy-3.3.0/busy/util/class_family.py
+-rw-rw-rw-   0 root         (0) root         (0)     2882 2023-04-06 23:41:59.000000 busy-3.3.0/busy/util/date_util.py
+-rw-rw-rw-   0 root         (0) root         (0)      217 2023-04-06 23:41:59.000000 busy-3.3.0/busy/util/python_version.py
+-rw-rw-rw-   0 root         (0) root         (0)     1231 2023-04-06 23:41:59.000000 busy-3.3.0/busy/util/readline_util.py
+-rw-rw-rw-   0 root         (0) root         (0)      973 2023-04-06 23:41:59.000000 busy-3.3.0/busy/util/super_wrapper.py
+-rw-rw-rw-   0 root         (0) root         (0)      131 2023-04-06 23:41:59.000000 busy-3.3.0/busy/util/textbox_util.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.306208 busy-3.3.0/busy.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    21646 2023-04-06 23:42:10.000000 busy-3.3.0/busy.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2067 2023-04-06 23:42:10.000000 busy-3.3.0/busy.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 23:42:10.000000 busy-3.3.0/busy.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       44 2023-04-06 23:42:10.000000 busy-3.3.0/busy.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 23:42:10.000000 busy-3.3.0/busy.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       10 2023-04-06 23:42:10.000000 busy-3.3.0/busy.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 23:42:10.328209 busy-3.3.0/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      742 2023-04-06 23:41:59.000000 busy-3.3.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.319208 busy-3.3.0/test/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/test/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.320208 busy-3.3.0/test/data_class_family/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/test/data_class_family/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      101 2023-04-06 23:41:59.000000 busy-3.3.0/test/data_class_family/atriarch.py
+-rw-rw-rw-   0 root         (0) root         (0)       76 2023-04-06 23:41:59.000000 busy-3.3.0/test/data_class_family/child.py
+-rw-rw-rw-   0 root         (0) root         (0)       74 2023-04-06 23:41:59.000000 busy-3.3.0/test/data_class_family/grandchild.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.321209 busy-3.3.0/test/handler/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/test/handler/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1205 2023-04-06 23:41:59.000000 busy-3.3.0/test/handler/test_handler.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.321209 busy-3.3.0/test/integration/
+-rw-rw-rw-   0 root         (0) root         (0)      150 2023-04-06 23:41:59.000000 busy-3.3.0/test/integration/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      416 2023-04-06 23:41:59.000000 busy-3.3.0/test/integration/test_integration.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.323209 busy-3.3.0/test/model/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/test/model/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      433 2023-04-06 23:41:59.000000 busy-3.3.0/test/model/test_item.py
+-rw-rw-rw-   0 root         (0) root         (0)      845 2023-04-06 23:41:59.000000 busy-3.3.0/test/model/test_item_io.py
+-rw-rw-rw-   0 root         (0) root         (0)     2857 2023-04-06 23:41:59.000000 busy-3.3.0/test/model/test_queue.py
+-rw-rw-rw-   0 root         (0) root         (0)      624 2023-04-06 23:41:59.000000 busy-3.3.0/test/model/test_queue_replace.py
+-rw-rw-rw-   0 root         (0) root         (0)     1778 2023-04-06 23:41:59.000000 busy-3.3.0/test/model/test_task.py
+-rw-rw-rw-   0 root         (0) root         (0)     4056 2023-04-06 23:41:59.000000 busy-3.3.0/test/model/test_todo_queue.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.324209 busy-3.3.0/test/root/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/test/root/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1406 2023-04-06 23:41:59.000000 busy-3.3.0/test/root/test_file.py
+-rw-rw-rw-   0 root         (0) root         (0)     2529 2023-04-06 23:41:59.000000 busy-3.3.0/test/root/test_file_system_root.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.325209 busy-3.3.0/test/ui/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/test/ui/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      357 2023-04-06 23:41:59.000000 busy-3.3.0/test/ui/test_shell_ui.py
+-rw-rw-rw-   0 root         (0) root         (0)      790 2023-04-06 23:41:59.000000 busy-3.3.0/test/ui/test_ui_terminal_editor.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:42:10.327209 busy-3.3.0/test/util/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:41:59.000000 busy-3.3.0/test/util/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      797 2023-04-06 23:41:59.000000 busy-3.3.0/test/util/test_class_families.py
+-rw-rw-rw-   0 root         (0) root         (0)      237 2023-04-06 23:41:59.000000 busy-3.3.0/test/util/test_class_family.py
+-rw-rw-rw-   0 root         (0) root         (0)      452 2023-04-06 23:41:59.000000 busy-3.3.0/test/util/test_date.py
+-rw-rw-rw-   0 root         (0) root         (0)      508 2023-04-06 23:41:59.000000 busy-3.3.0/test/util/test_python_version.py
```

### Comparing `busy-3.2.0/LICENSE` & `busy-3.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/PKG-INFO` & `busy-3.3.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: busy
-Version: 3.2.0
+Version: 3.3.0
 Summary: Personal time management tool
 Home-page: http://gitlab.com/fpotter/tools/busy
 Author: Francis Potter
 Author-email: busy@fpotter.com
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `busy-3.2.0/README.md` & `busy-3.3.0/README.md`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/activate_command.py` & `busy-3.3.0/busy/command/activate_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/add_command.py` & `busy-3.3.0/busy/command/add_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/command.py` & `busy-3.3.0/busy/command/command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/defer_command.py` & `busy-3.3.0/busy/command/defer_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/delete_command.py` & `busy-3.3.0/busy/command/delete_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/drop_and_pop_command.py` & `busy-3.3.0/busy/command/drop_and_pop_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/edit_command.py` & `busy-3.3.0/busy/command/edit_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/finish_command.py` & `busy-3.3.0/busy/command/finish_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/list_command.py` & `busy-3.3.0/busy/command/list_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/command/switch_command.py` & `busy-3.3.0/busy/command/switch_command.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/handler.py` & `busy-3.3.0/busy/handler.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/model/item.py` & `busy-3.3.0/busy/model/item.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/model/task.py` & `busy-3.3.0/busy/model/task.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/queue/queue.py` & `busy-3.3.0/busy/queue/queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/queue/todo_queue.py` & `busy-3.3.0/busy/queue/todo_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/root/file_system_root.py` & `busy-3.3.0/busy/root/file_system_root.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/selector.py` & `busy-3.3.0/busy/selector.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/ui/curses_ui.py` & `busy-3.3.0/busy/ui/curses_ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/ui/shell_ui.py` & `busy-3.3.0/busy/ui/shell_ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/ui/tcl_ui/edit_task_widget.py` & `busy-3.3.0/busy/ui/tcl_ui/edit_task_widget.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/ui/tcl_ui/get_item_widget.py` & `busy-3.3.0/busy/ui/tcl_ui/get_item_widget.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/ui/ui.py` & `busy-3.3.0/busy/ui/ui.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/util/class_family.py` & `busy-3.3.0/busy/util/class_family.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/util/date_util.py` & `busy-3.3.0/busy/util/date_util.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/util/readline_util.py` & `busy-3.3.0/busy/util/readline_util.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy/util/super_wrapper.py` & `busy-3.3.0/busy/util/super_wrapper.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/busy.egg-info/PKG-INFO` & `busy-3.3.0/busy.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: busy
-Version: 3.2.0
+Version: 3.3.0
 Summary: Personal time management tool
 Home-page: http://gitlab.com/fpotter/tools/busy
 Author: Francis Potter
 Author-email: busy@fpotter.com
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `busy-3.2.0/busy.egg-info/SOURCES.txt` & `busy-3.3.0/busy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/setup.py` & `busy-3.3.0/setup.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/handler/test_handler.py` & `busy-3.3.0/test/handler/test_handler.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/model/test_item_io.py` & `busy-3.3.0/test/model/test_item_io.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/model/test_queue.py` & `busy-3.3.0/test/model/test_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/model/test_queue_replace.py` & `busy-3.3.0/test/model/test_queue_replace.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/model/test_task.py` & `busy-3.3.0/test/model/test_task.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/model/test_todo_queue.py` & `busy-3.3.0/test/model/test_todo_queue.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/root/test_file.py` & `busy-3.3.0/test/root/test_file.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/root/test_file_system_root.py` & `busy-3.3.0/test/root/test_file_system_root.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/ui/test_ui_terminal_editor.py` & `busy-3.3.0/test/ui/test_ui_terminal_editor.py`

 * *Files identical despite different names*

### Comparing `busy-3.2.0/test/util/test_class_families.py` & `busy-3.3.0/test/util/test_class_families.py`

 * *Files identical despite different names*

