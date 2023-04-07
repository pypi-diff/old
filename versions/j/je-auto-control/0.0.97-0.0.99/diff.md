# Comparing `tmp/je_auto_control-0.0.97.tar.gz` & `tmp/je_auto_control-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\je_auto_control-0.0.97.tar", last modified: Mon Jul 18 07:11:21 2022, max compression
+gzip compressed data, was "dist\je_auto_control-0.0.99.tar", last modified: Tue Sep  6 01:24:30 2022, max compression
```

## Comparing `je_auto_control-0.0.97.tar` & `je_auto_control-0.0.99.tar`

### file list

```diff
@@ -1,125 +1,125 @@
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:20.000000 je_auto_control-0.0.97/je_auto_control/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/core/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/core/utils/
--rw-rw-rw-   0        0        0      389 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/core/utils/x11_linux_display.py
--rw-rw-rw-   0        0        0    15472 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py
--rw-rw-rw-   0        0        0       72 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/core/utils/__init__.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/core/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/keyboard/
--rw-rw-rw-   0        0        0     1031 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/keyboard/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/listener/
--rw-rw-rw-   0        0        0     5598 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/listener/x11_linux_listener.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/listener/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/mouse/
--rw-rw-rw-   0        0        0     2352 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/mouse/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/record/
--rw-rw-rw-   0        0        0     1551 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/record/x11_linux_record.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/record/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/screen/
--rw-rw-rw-   0        0        0      532 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/screen/x11_linux_screen.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/screen/__init__.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/linux_with_x11/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/core/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/core/utils/
--rw-rw-rw-   0        0        0     3162 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/core/utils/osx_vk.py
--rw-rw-rw-   0        0        0       55 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/core/utils/__init__.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/core/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/keyboard/
--rw-rw-rw-   0        0        0     3018 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/keyboard/osx_keyboard.py
--rw-rw-rw-   0        0        0      447 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/keyboard/osx_keyboard_check.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/keyboard/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/listener/
--rw-rw-rw-   0        0        0     1549 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/listener/osx_listener.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/listener/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/mouse/
--rw-rw-rw-   0        0        0     3451 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/mouse/osx_mouse.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/mouse/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/record/
--rw-rw-rw-   0        0        0      828 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/record/osx_record.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/record/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/osx/screen/
--rw-rw-rw-   0        0        0      494 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/screen/osx_screen.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/screen/__init__.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/osx/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/critical_exit/
--rw-rw-rw-   0        0        0     1490 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/critical_exit/critcal_exit.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/critical_exit/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/exception/
--rw-rw-rw-   0        0        0     1133 2022-07-17 10:09:11.000000 je_auto_control-0.0.97/je_auto_control/utils/exception/exceptions.py
--rw-rw-rw-   0        0        0     2270 2022-07-17 10:09:11.000000 je_auto_control-0.0.97/je_auto_control/utils/exception/exception_tag.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/exception/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/executor/
--rw-rw-rw-   0        0        0     5207 2022-07-18 07:04:10.000000 je_auto_control-0.0.97/je_auto_control/utils/executor/action_executor.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/executor/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/file_process/
--rw-rw-rw-   0        0        0      314 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/file_process/create_project_structure.py
--rw-rw-rw-   0        0        0      758 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/file_process/get_dir_file_list.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/file_process/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/html_report/
--rw-rw-rw-   0        0        0     4617 2022-06-28 14:09:50.000000 je_auto_control-0.0.97/je_auto_control/utils/html_report/html_report_generate.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/html_report/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/image/
--rw-rw-rw-   0        0        0      456 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/image/screenshot.py
--rw-rw-rw-   0        0        0     1151 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/image/template_detection.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/image/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/json/
--rw-rw-rw-   0        0        0     1411 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/json/json_file.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/json/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/test_record/
--rw-rw-rw-   0        0        0      884 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/test_record/record_test_class.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/test_record/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/utils/timeout/
--rw-rw-rw-   0        0        0      640 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/timeout/multiprocess_timeout.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/timeout/__init__.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/utils/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/core/
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/core/utils/
--rw-rw-rw-   0        0        0     2193 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/core/utils/win32_ctype_input.py
--rw-rw-rw-   0        0        0      574 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/core/utils/win32_keypress_check.py
--rw-rw-rw-   0        0        0     4979 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/core/utils/win32_vk.py
--rw-rw-rw-   0        0        0       59 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/core/utils/__init__.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/core/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/keyboard/
--rw-rw-rw-   0        0        0     1225 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py
--rw-rw-rw-   0        0        0        4 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/keyboard/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/listener/
--rw-rw-rw-   0        0        0     2430 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/listener/win32_keyboard_listener.py
--rw-rw-rw-   0        0        0     2971 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/listener/win32_mouse_listener.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/listener/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/mouse/
--rw-rw-rw-   0        0        0     4199 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/mouse/win32_ctype_mouse_control.py
--rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/mouse/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/record/
--rw-rw-rw-   0        0        0     2094 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/record/win32_record.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/record/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/windows/screen/
--rw-rw-rw-   0        0        0      545 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/screen/win32_screen.py
--rw-rw-rw-   0        0        0       62 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/screen/__init__.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/windows/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control/wrapper/
--rw-rw-rw-   0        0        0     5316 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_image.py
--rw-rw-rw-   0        0        0     9438 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_keyboard.py
--rw-rw-rw-   0        0        0     8848 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_mouse.py
--rw-rw-rw-   0        0        0     1743 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_record.py
--rw-rw-rw-   0        0        0     1671 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_screen.py
--rw-rw-rw-   0        0        0    58298 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/wrapper/platform_wrapper.py
--rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/je_auto_control/wrapper/__init__.py
--rw-rw-rw-   0        0        0     3625 2022-06-28 14:49:23.000000 je_auto_control-0.0.97/je_auto_control/__init__.py
--rw-rw-rw-   0        0        0     1943 2022-07-17 10:09:11.000000 je_auto_control-0.0.97/je_auto_control/__main__.py
-drwxrwxrwx   0        0        0        0 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/je_auto_control.egg-info/
--rw-rw-rw-   0        0        0        1 2022-07-18 07:11:20.000000 je_auto_control-0.0.97/je_auto_control.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0     2618 2022-07-18 07:11:20.000000 je_auto_control-0.0.97/je_auto_control.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      119 2022-07-18 07:11:20.000000 je_auto_control-0.0.97/je_auto_control.egg-info/requires.txt
--rw-rw-rw-   0        0        0     3910 2022-07-18 07:11:20.000000 je_auto_control-0.0.97/je_auto_control.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0       16 2022-07-18 07:11:20.000000 je_auto_control-0.0.97/je_auto_control.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     2618 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/PKG-INFO
--rw-rw-rw-   0        0        0     1583 2022-06-28 13:59:18.000000 je_auto_control-0.0.97/README.md
--rw-rw-rw-   0        0        0       42 2022-07-18 07:11:21.000000 je_auto_control-0.0.97/setup.cfg
--rw-rw-rw-   0        0        0     1112 2022-07-18 07:11:13.000000 je_auto_control-0.0.97/setup.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:30.000000 je_auto_control-0.0.99/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/core/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/core/utils/
+-rw-rw-rw-   0        0        0      389 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/core/utils/x11_linux_display.py
+-rw-rw-rw-   0        0        0    15472 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py
+-rw-rw-rw-   0        0        0       72 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/core/utils/__init__.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/core/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/keyboard/
+-rw-rw-rw-   0        0        0     1031 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/keyboard/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/listener/
+-rw-rw-rw-   0        0        0     5598 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/listener/x11_linux_listener.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/listener/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/mouse/
+-rw-rw-rw-   0        0        0     2352 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/mouse/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/record/
+-rw-rw-rw-   0        0        0     1551 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/record/x11_linux_record.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/record/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/screen/
+-rw-rw-rw-   0        0        0      532 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/screen/x11_linux_screen.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/screen/__init__.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/linux_with_x11/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/core/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/core/utils/
+-rw-rw-rw-   0        0        0     3162 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/core/utils/osx_vk.py
+-rw-rw-rw-   0        0        0       55 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/core/utils/__init__.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/core/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/keyboard/
+-rw-rw-rw-   0        0        0     3018 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/keyboard/osx_keyboard.py
+-rw-rw-rw-   0        0        0      447 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/keyboard/osx_keyboard_check.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/keyboard/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/listener/
+-rw-rw-rw-   0        0        0     1549 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/listener/osx_listener.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/listener/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/mouse/
+-rw-rw-rw-   0        0        0     3451 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/mouse/osx_mouse.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/mouse/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/record/
+-rw-rw-rw-   0        0        0      828 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/record/osx_record.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/record/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/osx/screen/
+-rw-rw-rw-   0        0        0      494 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/screen/osx_screen.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/screen/__init__.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/osx/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/critical_exit/
+-rw-rw-rw-   0        0        0     1490 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/critical_exit/critcal_exit.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/critical_exit/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/exception/
+-rw-rw-rw-   0        0        0     1133 2022-07-17 10:09:11.000000 je_auto_control-0.0.99/je_auto_control/utils/exception/exceptions.py
+-rw-rw-rw-   0        0        0     2270 2022-07-17 10:09:11.000000 je_auto_control-0.0.99/je_auto_control/utils/exception/exception_tag.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/exception/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/executor/
+-rw-rw-rw-   0        0        0     5207 2022-07-18 07:04:10.000000 je_auto_control-0.0.99/je_auto_control/utils/executor/action_executor.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/executor/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/file_process/
+-rw-rw-rw-   0        0        0      314 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/file_process/create_project_structure.py
+-rw-rw-rw-   0        0        0      758 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/file_process/get_dir_file_list.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/file_process/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/html_report/
+-rw-rw-rw-   0        0        0     4617 2022-06-28 14:09:50.000000 je_auto_control-0.0.99/je_auto_control/utils/html_report/html_report_generate.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/html_report/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/image/
+-rw-rw-rw-   0        0        0      490 2022-09-03 06:30:37.000000 je_auto_control-0.0.99/je_auto_control/utils/image/screenshot.py
+-rw-rw-rw-   0        0        0     1151 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/image/template_detection.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/image/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/json/
+-rw-rw-rw-   0        0        0     1411 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/json/json_file.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/json/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/test_record/
+-rw-rw-rw-   0        0        0      884 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/test_record/record_test_class.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/test_record/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/utils/timeout/
+-rw-rw-rw-   0        0        0      640 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/timeout/multiprocess_timeout.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/timeout/__init__.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/utils/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/windows/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/windows/core/
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/windows/core/utils/
+-rw-rw-rw-   0        0        0     2193 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/core/utils/win32_ctype_input.py
+-rw-rw-rw-   0        0        0      574 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/core/utils/win32_keypress_check.py
+-rw-rw-rw-   0        0        0     4979 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/core/utils/win32_vk.py
+-rw-rw-rw-   0        0        0       59 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/core/utils/__init__.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/core/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/windows/keyboard/
+-rw-rw-rw-   0        0        0     1225 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py
+-rw-rw-rw-   0        0        0        4 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/keyboard/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/windows/listener/
+-rw-rw-rw-   0        0        0     2430 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/listener/win32_keyboard_listener.py
+-rw-rw-rw-   0        0        0     2971 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/listener/win32_mouse_listener.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/listener/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/windows/mouse/
+-rw-rw-rw-   0        0        0     4199 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/mouse/win32_ctype_mouse_control.py
+-rw-rw-rw-   0        0        0        0 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/mouse/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control/windows/record/
+-rw-rw-rw-   0        0        0     2094 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/record/win32_record.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/record/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:30.000000 je_auto_control-0.0.99/je_auto_control/windows/screen/
+-rw-rw-rw-   0        0        0      545 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/screen/win32_screen.py
+-rw-rw-rw-   0        0        0       62 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/screen/__init__.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/windows/__init__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:30.000000 je_auto_control-0.0.99/je_auto_control/wrapper/
+-rw-rw-rw-   0        0        0     5316 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_image.py
+-rw-rw-rw-   0        0        0     9438 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_keyboard.py
+-rw-rw-rw-   0        0        0     8848 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_mouse.py
+-rw-rw-rw-   0        0        0     1743 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_record.py
+-rw-rw-rw-   0        0        0     1671 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_screen.py
+-rw-rw-rw-   0        0        0    58298 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/wrapper/platform_wrapper.py
+-rw-rw-rw-   0        0        0        2 2022-06-28 13:59:18.000000 je_auto_control-0.0.99/je_auto_control/wrapper/__init__.py
+-rw-rw-rw-   0        0        0     3627 2022-08-20 18:50:13.000000 je_auto_control-0.0.99/je_auto_control/__init__.py
+-rw-rw-rw-   0        0        0     1943 2022-07-17 10:09:11.000000 je_auto_control-0.0.99/je_auto_control/__main__.py
+drwxrwxrwx   0        0        0        0 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control.egg-info/
+-rw-rw-rw-   0        0        0        1 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0     2650 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      119 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control.egg-info/requires.txt
+-rw-rw-rw-   0        0        0     3910 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0       16 2022-09-06 01:24:29.000000 je_auto_control-0.0.99/je_auto_control.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     2650 2022-09-06 01:24:30.000000 je_auto_control-0.0.99/PKG-INFO
+-rw-rw-rw-   0        0        0     1607 2022-09-05 09:37:14.000000 je_auto_control-0.0.99/README.md
+-rw-rw-rw-   0        0        0       42 2022-09-06 01:24:30.000000 je_auto_control-0.0.99/setup.cfg
+-rw-rw-rw-   0        0        0     1112 2022-09-06 01:24:08.000000 je_auto_control-0.0.99/setup.py
```

### Comparing `je_auto_control-0.0.97/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py` & `je_auto_control-0.0.99/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py` & `je_auto_control-0.0.99/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/linux_with_x11/listener/x11_linux_listener.py` & `je_auto_control-0.0.99/je_auto_control/linux_with_x11/listener/x11_linux_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py` & `je_auto_control-0.0.99/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/linux_with_x11/record/x11_linux_record.py` & `je_auto_control-0.0.99/je_auto_control/linux_with_x11/record/x11_linux_record.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/linux_with_x11/screen/x11_linux_screen.py` & `je_auto_control-0.0.99/je_auto_control/linux_with_x11/screen/x11_linux_screen.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/osx/core/utils/osx_vk.py` & `je_auto_control-0.0.99/je_auto_control/osx/core/utils/osx_vk.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/osx/keyboard/osx_keyboard.py` & `je_auto_control-0.0.99/je_auto_control/osx/keyboard/osx_keyboard.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/osx/listener/osx_listener.py` & `je_auto_control-0.0.99/je_auto_control/osx/listener/osx_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/osx/mouse/osx_mouse.py` & `je_auto_control-0.0.99/je_auto_control/osx/mouse/osx_mouse.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/osx/record/osx_record.py` & `je_auto_control-0.0.99/je_auto_control/osx/record/osx_record.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/critical_exit/critcal_exit.py` & `je_auto_control-0.0.99/je_auto_control/utils/critical_exit/critcal_exit.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/exception/exceptions.py` & `je_auto_control-0.0.99/je_auto_control/utils/exception/exceptions.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/exception/exception_tag.py` & `je_auto_control-0.0.99/je_auto_control/utils/exception/exception_tag.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/executor/action_executor.py` & `je_auto_control-0.0.99/je_auto_control/utils/executor/action_executor.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/file_process/get_dir_file_list.py` & `je_auto_control-0.0.99/je_auto_control/utils/file_process/get_dir_file_list.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/html_report/html_report_generate.py` & `je_auto_control-0.0.99/je_auto_control/utils/html_report/html_report_generate.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/image/template_detection.py` & `je_auto_control-0.0.99/je_auto_control/utils/image/template_detection.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/json/json_file.py` & `je_auto_control-0.0.99/je_auto_control/utils/json/json_file.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/test_record/record_test_class.py` & `je_auto_control-0.0.99/je_auto_control/utils/test_record/record_test_class.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/utils/timeout/multiprocess_timeout.py` & `je_auto_control-0.0.99/je_auto_control/utils/timeout/multiprocess_timeout.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/core/utils/win32_ctype_input.py` & `je_auto_control-0.0.99/je_auto_control/windows/core/utils/win32_ctype_input.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/core/utils/win32_keypress_check.py` & `je_auto_control-0.0.99/je_auto_control/windows/core/utils/win32_keypress_check.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/core/utils/win32_vk.py` & `je_auto_control-0.0.99/je_auto_control/windows/core/utils/win32_vk.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py` & `je_auto_control-0.0.99/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/listener/win32_keyboard_listener.py` & `je_auto_control-0.0.99/je_auto_control/windows/listener/win32_keyboard_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/listener/win32_mouse_listener.py` & `je_auto_control-0.0.99/je_auto_control/windows/listener/win32_mouse_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/mouse/win32_ctype_mouse_control.py` & `je_auto_control-0.0.99/je_auto_control/windows/mouse/win32_ctype_mouse_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/record/win32_record.py` & `je_auto_control-0.0.99/je_auto_control/windows/record/win32_record.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/windows/screen/win32_screen.py` & `je_auto_control-0.0.99/je_auto_control/windows/screen/win32_screen.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_image.py` & `je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_image.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_keyboard.py` & `je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_keyboard.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_mouse.py` & `je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_mouse.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_record.py` & `je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_record.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/wrapper/auto_control_screen.py` & `je_auto_control-0.0.99/je_auto_control/wrapper/auto_control_screen.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/wrapper/platform_wrapper.py` & `je_auto_control-0.0.99/je_auto_control/wrapper/platform_wrapper.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control/__init__.py` & `je_auto_control-0.0.99/je_auto_control/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 """
 import all wrapper function
 """
 
+
 # import mouse
 from je_auto_control.wrapper.auto_control_mouse import click_mouse
 from je_auto_control.wrapper.auto_control_mouse import mouse_table
 from je_auto_control.wrapper.auto_control_mouse import position
 from je_auto_control.wrapper.auto_control_mouse import press_mouse
 from je_auto_control.wrapper.auto_control_mouse import release_mouse
 from je_auto_control.wrapper.auto_control_mouse import scroll
```

### Comparing `je_auto_control-0.0.97/je_auto_control/__main__.py` & `je_auto_control-0.0.99/je_auto_control/__main__.py`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/je_auto_control.egg-info/PKG-INFO` & `je_auto_control-0.0.99/je_auto_control.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: je-auto-control
-Version: 0.0.97
+Version: 0.0.99
 Summary: auto testing
 Home-page: https://github.com/JE-Chen/AutoControl
 Author: JE-Chen
 Author-email: zenmailman@gmail.com
 License: UNKNOWN
 Description: # je_auto_control
         
@@ -15,15 +15,16 @@
         * Image Detect
         * Keyboard Event
         * Mouse Event
         * Screen 
         * Action file and executor
         * Record Event
         * CLI with action file
-        * timeout
+        * Generate HTML Report
+        * Timeout
         
         ---
         
         [![CircleCI](https://circleci.com/gh/JE-Chen/AutoControl/tree/main.svg?style=svg)](https://circleci.com/gh/JE-Chen/AutoControl/tree/main)
         
         [![AutoControl GitHub Actions Dev](https://github.com/JE-Chen/AutoControl/actions/workflows/auto-control-github-actions_dev.yml/badge.svg)](https://github.com/JE-Chen/AutoControl/actions/workflows/auto-control-github-actions_dev.yml)
         
@@ -40,15 +41,15 @@
         # make sure you have install cmake libssl-dev (on linux)
         pip install je_auto_control
         ```
         
         ## Info
         
         * requirement
-            * Python 3.5 & later
+            * Python 3.7 & later
             * pip 19.3 & later
         
         
         * Dev env
             * windows 11
             * osx 11 big sur
             * ubuntu 20.0.4
@@ -57,15 +58,15 @@
         * Test on
             * windows 10 ~ 11
             * osx 10.5 ~ 11 big sur
             * ubuntu 20.0.4
             * raspberry pi 3B and 4B
         
 Platform: UNKNOWN
-Classifier: Programming Language :: Python :: 3.5
+Classifier: Programming Language :: Python :: 3.7
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Environment :: Win32 (MS Windows)
 Classifier: Environment :: MacOS X
 Classifier: Environment :: X11 Applications
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
```

### Comparing `je_auto_control-0.0.97/je_auto_control.egg-info/SOURCES.txt` & `je_auto_control-0.0.99/je_auto_control.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `je_auto_control-0.0.97/PKG-INFO` & `je_auto_control-0.0.99/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: je_auto_control
-Version: 0.0.97
+Version: 0.0.99
 Summary: auto testing
 Home-page: https://github.com/JE-Chen/AutoControl
 Author: JE-Chen
 Author-email: zenmailman@gmail.com
 License: UNKNOWN
 Description: # je_auto_control
         
@@ -15,15 +15,16 @@
         * Image Detect
         * Keyboard Event
         * Mouse Event
         * Screen 
         * Action file and executor
         * Record Event
         * CLI with action file
-        * timeout
+        * Generate HTML Report
+        * Timeout
         
         ---
         
         [![CircleCI](https://circleci.com/gh/JE-Chen/AutoControl/tree/main.svg?style=svg)](https://circleci.com/gh/JE-Chen/AutoControl/tree/main)
         
         [![AutoControl GitHub Actions Dev](https://github.com/JE-Chen/AutoControl/actions/workflows/auto-control-github-actions_dev.yml/badge.svg)](https://github.com/JE-Chen/AutoControl/actions/workflows/auto-control-github-actions_dev.yml)
         
@@ -40,15 +41,15 @@
         # make sure you have install cmake libssl-dev (on linux)
         pip install je_auto_control
         ```
         
         ## Info
         
         * requirement
-            * Python 3.5 & later
+            * Python 3.7 & later
             * pip 19.3 & later
         
         
         * Dev env
             * windows 11
             * osx 11 big sur
             * ubuntu 20.0.4
@@ -57,15 +58,15 @@
         * Test on
             * windows 10 ~ 11
             * osx 10.5 ~ 11 big sur
             * ubuntu 20.0.4
             * raspberry pi 3B and 4B
         
 Platform: UNKNOWN
-Classifier: Programming Language :: Python :: 3.5
+Classifier: Programming Language :: Python :: 3.7
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Environment :: Win32 (MS Windows)
 Classifier: Environment :: MacOS X
 Classifier: Environment :: X11 Applications
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
```

### Comparing `je_auto_control-0.0.97/README.md` & `je_auto_control-0.0.99/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -7,15 +7,16 @@
 * Image Detect
 * Keyboard Event
 * Mouse Event
 * Screen 
 * Action file and executor
 * Record Event
 * CLI with action file
-* timeout
+* Generate HTML Report
+* Timeout
 
 ---
 
 [![CircleCI](https://circleci.com/gh/JE-Chen/AutoControl/tree/main.svg?style=svg)](https://circleci.com/gh/JE-Chen/AutoControl/tree/main)
 
 [![AutoControl GitHub Actions Dev](https://github.com/JE-Chen/AutoControl/actions/workflows/auto-control-github-actions_dev.yml/badge.svg)](https://github.com/JE-Chen/AutoControl/actions/workflows/auto-control-github-actions_dev.yml)
 
@@ -32,15 +33,15 @@
 # make sure you have install cmake libssl-dev (on linux)
 pip install je_auto_control
 ```
 
 ## Info
 
 * requirement
-    * Python 3.5 & later
+    * Python 3.7 & later
     * pip 19.3 & later
 
 
 * Dev env
     * windows 11
     * osx 11 big sur
     * ubuntu 20.0.4
```

### Comparing `je_auto_control-0.0.97/setup.py` & `je_auto_control-0.0.99/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as README:
     long_description = README.read()
 
 setuptools.setup(
     name="je_auto_control",
-    version="0.0.97",
+    version="0.0.99",
     author="JE-Chen",
     author_email="zenmailman@gmail.com",
     description="auto testing",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/JE-Chen/AutoControl",
     packages=setuptools.find_packages(),
@@ -18,15 +18,15 @@
         "pillow",
         "numpy",
         "pyobjc-core;platform_system=='Darwin'",
         "pyobjc;platform_system=='Darwin'",
         "python3-Xlib;platform_system=='Linux'"
     ],
     classifiers=[
-        "Programming Language :: Python :: 3.5",
+        "Programming Language :: Python :: 3.7",
         "Development Status :: 2 - Pre-Alpha",
         "Environment :: Win32 (MS Windows)",
         "Environment :: MacOS X",
         "Environment :: X11 Applications",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
     ]
```

