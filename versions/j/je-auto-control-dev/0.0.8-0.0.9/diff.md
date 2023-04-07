# Comparing `tmp/je_auto_control_dev-0.0.8.tar.gz` & `tmp/je_auto_control_dev-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\je_auto_control_dev-0.0.8.tar", last modified: Sun Mar 20 16:00:12 2022, max compression
+gzip compressed data, was "dist\je_auto_control_dev-0.0.9.tar", last modified: Sat Mar 26 16:27:30 2022, max compression
```

## Comparing `je_auto_control_dev-0.0.8.tar` & `je_auto_control_dev-0.0.9.tar`

### file list

```diff
@@ -1,120 +1,120 @@
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/
--rw-rw-rw-   0        0        0     1085 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/LICENSE
--rw-rw-rw-   0        0        0     1461 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/PKG-INFO
--rw-rw-rw-   0        0        0      833 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/README.md
--rw-rw-rw-   0        0        0     1120 2022-03-20 16:00:02.000000 je_auto_control_dev-0.0.8/dev_setup.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/
--rw-rw-rw-   0        0        0     3086 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/__init__.py
--rw-rw-rw-   0        0        0      470 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/__main__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/__init__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/core/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/core/__init__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/core/utils/
--rw-rw-rw-   0        0        0       72 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/core/utils/__init__.py
--rw-rw-rw-   0        0        0      389 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/core/utils/x11_linux_display.py
--rw-rw-rw-   0        0        0    15472 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/keyboard/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/keyboard/__init__.py
--rw-rw-rw-   0        0        0     1015 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/listener/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/listener/__init__.py
--rw-rw-rw-   0        0        0     5651 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/listener/x11_linux_listener.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/mouse/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/mouse/__init__.py
--rw-rw-rw-   0        0        0     2267 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/record/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/record/__init__.py
--rw-rw-rw-   0        0        0     1761 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/record/x11_linux_record.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/screen/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/screen/__init__.py
--rw-rw-rw-   0        0        0      487 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/screen/x11_linux_screen.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/__init__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/core/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/core/__init__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/core/utils/
--rw-rw-rw-   0        0        0       55 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/core/utils/__init__.py
--rw-rw-rw-   0        0        0     3162 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/core/utils/osx_vk.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/keyboard/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/keyboard/__init__.py
--rw-rw-rw-   0        0        0     2999 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/keyboard/osx_keyboard.py
--rw-rw-rw-   0        0        0      439 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/keyboard/osx_keyboard_check.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/listener/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/listener/__init__.py
--rw-rw-rw-   0        0        0     1569 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/listener/osx_listener.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/mouse/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/mouse/__init__.py
--rw-rw-rw-   0        0        0     3360 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/mouse/osx_mouse.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/record/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/record/__init__.py
--rw-rw-rw-   0        0        0     1035 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/record/osx_record.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/screen/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/screen/__init__.py
--rw-rw-rw-   0        0        0      449 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/osx/screen/osx_screen.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/__init__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/critical_exit/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/critical_exit/__init__.py
--rw-rw-rw-   0        0        0     1466 2022-03-20 09:07:16.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/critical_exit/critcal_exit.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/exception/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/exception/__init__.py
--rw-rw-rw-   0        0        0     1967 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/exception/exception_tag.py
--rw-rw-rw-   0        0        0      892 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/exception/exceptions.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/executor/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/executor/__init__.py
--rw-rw-rw-   0        0        0     3192 2022-03-20 12:18:05.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/executor/action_executor.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/image/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/image/__init__.py
--rw-rw-rw-   0        0        0      440 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/image/screenshot.py
--rw-rw-rw-   0        0        0     1092 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/image/template_detection.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/json/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/json/__init__.py
--rw-rw-rw-   0        0        0     1390 2022-03-20 11:24:03.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/json/json_file.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/test_record/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/test_record/__init__.py
--rw-rw-rw-   0        0        0      271 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/test_record/record_test_result_class.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/timeout/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/timeout/__init__.py
--rw-rw-rw-   0        0        0      640 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/utils/timeout/multiprocess_timeout.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/__init__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/core/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/core/__init__.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/
--rw-rw-rw-   0        0        0       59 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/__init__.py
--rw-rw-rw-   0        0        0     2187 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/win32_ctype_input.py
--rw-rw-rw-   0        0        0      566 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/win32_keypress_check.py
--rw-rw-rw-   0        0        0     4979 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/win32_vk.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/keyboard/
--rw-rw-rw-   0        0        0        4 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/keyboard/__init__.py
--rw-rw-rw-   0        0        0     1209 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/listener/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/listener/__init__.py
--rw-rw-rw-   0        0        0     2632 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/listener/win32_keyboard_listener.py
--rw-rw-rw-   0        0        0     3154 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/listener/win32_mouse_listener.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/mouse/
--rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/mouse/__init__.py
--rw-rw-rw-   0        0        0     4098 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/mouse/win32_ctype_mouse_control.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/record/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/record/__init__.py
--rw-rw-rw-   0        0        0     2246 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/record/win32_record.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/screen/
--rw-rw-rw-   0        0        0       62 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/screen/__init__.py
--rw-rw-rw-   0        0        0      484 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/windows/screen/win32_screen.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/
--rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/__init__.py
--rw-rw-rw-   0        0        0     3889 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_image.py
--rw-rw-rw-   0        0        0     5657 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_keyboard.py
--rw-rw-rw-   0        0        0     6463 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_mouse.py
--rw-rw-rw-   0        0        0     1253 2022-03-20 12:20:26.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_record.py
--rw-rw-rw-   0        0        0     1022 2022-03-20 12:22:23.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_screen.py
--rw-rw-rw-   0        0        0    58298 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.8/je_auto_control/wrapper/platform_wrapper.py
-drwxrwxrwx   0        0        0        0 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/
--rw-rw-rw-   0        0        0     1461 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     3688 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      119 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/requires.txt
--rw-rw-rw-   0        0        0       16 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2022-03-20 16:00:11.000000 je_auto_control_dev-0.0.8/setup.cfg
--rw-rw-rw-   0        0        0     1112 2022-03-19 16:31:12.000000 je_auto_control_dev-0.0.8/setup.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/
+-rw-rw-rw-   0        0        0     1085 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/LICENSE
+-rw-rw-rw-   0        0        0     1672 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/PKG-INFO
+-rw-rw-rw-   0        0        0     1044 2022-03-20 19:17:34.000000 je_auto_control_dev-0.0.9/README.md
+-rw-rw-rw-   0        0        0     1120 2022-03-26 16:27:27.000000 je_auto_control_dev-0.0.9/dev_setup.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/
+-rw-rw-rw-   0        0        0     3079 2022-03-25 17:19:44.000000 je_auto_control_dev-0.0.9/je_auto_control/__init__.py
+-rw-rw-rw-   0        0        0      470 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/__main__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/__init__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/core/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/core/__init__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/core/utils/
+-rw-rw-rw-   0        0        0       72 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/core/utils/__init__.py
+-rw-rw-rw-   0        0        0      389 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/core/utils/x11_linux_display.py
+-rw-rw-rw-   0        0        0    15472 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/keyboard/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/keyboard/__init__.py
+-rw-rw-rw-   0        0        0     1015 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/listener/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/listener/__init__.py
+-rw-rw-rw-   0        0        0     5651 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/listener/x11_linux_listener.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/mouse/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/mouse/__init__.py
+-rw-rw-rw-   0        0        0     2267 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/record/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/record/__init__.py
+-rw-rw-rw-   0        0        0     1761 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/record/x11_linux_record.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/screen/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/screen/__init__.py
+-rw-rw-rw-   0        0        0      487 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/screen/x11_linux_screen.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/__init__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/core/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/core/__init__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/core/utils/
+-rw-rw-rw-   0        0        0       55 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/core/utils/__init__.py
+-rw-rw-rw-   0        0        0     3162 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/core/utils/osx_vk.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/keyboard/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/keyboard/__init__.py
+-rw-rw-rw-   0        0        0     2999 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/keyboard/osx_keyboard.py
+-rw-rw-rw-   0        0        0      439 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/keyboard/osx_keyboard_check.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/listener/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/listener/__init__.py
+-rw-rw-rw-   0        0        0     1569 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/listener/osx_listener.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/mouse/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/mouse/__init__.py
+-rw-rw-rw-   0        0        0     3360 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/mouse/osx_mouse.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/record/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/record/__init__.py
+-rw-rw-rw-   0        0        0     1035 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/record/osx_record.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/screen/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/screen/__init__.py
+-rw-rw-rw-   0        0        0      449 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/osx/screen/osx_screen.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/__init__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/critical_exit/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/critical_exit/__init__.py
+-rw-rw-rw-   0        0        0     1466 2022-03-20 09:07:16.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/critical_exit/critcal_exit.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/exception/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/exception/__init__.py
+-rw-rw-rw-   0        0        0     1967 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/exception/exception_tag.py
+-rw-rw-rw-   0        0        0      892 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/exception/exceptions.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/executor/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/executor/__init__.py
+-rw-rw-rw-   0        0        0     3466 2022-03-26 16:19:48.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/executor/action_executor.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/image/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/image/__init__.py
+-rw-rw-rw-   0        0        0      440 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/image/screenshot.py
+-rw-rw-rw-   0        0        0     1092 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/image/template_detection.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/json/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/json/__init__.py
+-rw-rw-rw-   0        0        0     1390 2022-03-20 11:24:03.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/json/json_file.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/test_record/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/test_record/__init__.py
+-rw-rw-rw-   0        0        0      680 2022-03-26 15:30:37.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/test_record/record_test_class.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/timeout/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/timeout/__init__.py
+-rw-rw-rw-   0        0        0      640 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/utils/timeout/multiprocess_timeout.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/__init__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/core/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/core/__init__.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/
+-rw-rw-rw-   0        0        0       59 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/__init__.py
+-rw-rw-rw-   0        0        0     2187 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/win32_ctype_input.py
+-rw-rw-rw-   0        0        0      566 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/win32_keypress_check.py
+-rw-rw-rw-   0        0        0     4979 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/win32_vk.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/keyboard/
+-rw-rw-rw-   0        0        0        4 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/keyboard/__init__.py
+-rw-rw-rw-   0        0        0     1209 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/listener/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/listener/__init__.py
+-rw-rw-rw-   0        0        0     2632 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/listener/win32_keyboard_listener.py
+-rw-rw-rw-   0        0        0     3154 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/listener/win32_mouse_listener.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/mouse/
+-rw-rw-rw-   0        0        0        0 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/mouse/__init__.py
+-rw-rw-rw-   0        0        0     4098 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/mouse/win32_ctype_mouse_control.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/record/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/record/__init__.py
+-rw-rw-rw-   0        0        0     2246 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/record/win32_record.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/screen/
+-rw-rw-rw-   0        0        0       62 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/screen/__init__.py
+-rw-rw-rw-   0        0        0      484 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/windows/screen/win32_screen.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/
+-rw-rw-rw-   0        0        0        2 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/__init__.py
+-rw-rw-rw-   0        0        0     5007 2022-03-26 15:03:54.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_image.py
+-rw-rw-rw-   0        0        0     7269 2022-03-26 16:22:17.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_keyboard.py
+-rw-rw-rw-   0        0        0     8077 2022-03-26 16:27:27.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_mouse.py
+-rw-rw-rw-   0        0        0     1757 2022-03-26 16:27:27.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_record.py
+-rw-rw-rw-   0        0        0     1533 2022-03-26 16:27:27.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_screen.py
+-rw-rw-rw-   0        0        0    58298 2022-03-19 16:29:14.000000 je_auto_control_dev-0.0.9/je_auto_control/wrapper/platform_wrapper.py
+drwxrwxrwx   0        0        0        0 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/
+-rw-rw-rw-   0        0        0     1672 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     3681 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      119 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       16 2022-03-26 16:27:29.000000 je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2022-03-26 16:27:30.000000 je_auto_control_dev-0.0.9/setup.cfg
+-rw-rw-rw-   0        0        0     1112 2022-03-20 16:04:14.000000 je_auto_control_dev-0.0.9/setup.py
```

### Comparing `je_auto_control_dev-0.0.8/LICENSE` & `je_auto_control_dev-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/PKG-INFO` & `je_auto_control_dev-0.0.9/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: je_auto_control_dev
-Version: 0.0.8
+Version: 0.0.9
 Summary: auto testing
 Home-page: https://github.com/JE-Chen/AutoControl
 Author: JE-Chen
 Author-email: zenmailman@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.5
@@ -17,14 +17,27 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # je_auto_control
 
 ---
 
+### JE Auto Control as a tool for GUI Testing 
+#### Features
+* Image Detect
+* Keyboard Event
+* Mouse Event
+* Screen 
+* Action file and executor
+* Record Event
+* CLI with action file
+* timeout
+
+---
+
 [![CircleCI](https://circleci.com/gh/JE-Chen/AutoControl/tree/main.svg?style=svg)](https://circleci.com/gh/JE-Chen/AutoControl/tree/main)
 
 ### Documentation
 
 [![Documentation Status](https://readthedocs.org/projects/python-jeautocontrol/badge/?version=latest)](https://python-jeautocontrol.readthedocs.io/en/latest/?badge=latest)
 
 documentation available at [https://python-jeautocontrol.readthedocs.io/en/latest/](https://python-jeautocontrol.readthedocs.io/en/latest/)
```

### Comparing `je_auto_control_dev-0.0.8/dev_setup.py` & `je_auto_control_dev-0.0.9/dev_setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as README:
     long_description = README.read()
 
 setuptools.setup(
     name="je_auto_control_dev",
-    version="0.0.08",
+    version="0.0.09",
     author="JE-Chen",
     author_email="zenmailman@gmail.com",
     description="auto testing",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/JE-Chen/AutoControl",
     packages=setuptools.find_packages(),
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/__init__.py` & `je_auto_control_dev-0.0.9/je_auto_control/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -53,12 +53,12 @@
 from je_auto_control.utils.executor.action_executor import execute_action
 from je_auto_control.utils.json.json_file import read_action_json
 from je_auto_control.utils.json.json_file import write_action_json
 
 # timeout
 from je_auto_control.utils.timeout.multiprocess_timeout import multiprocess_timeout
 # test record
-from je_auto_control.utils.test_record.record_test_result_class import test_record
+from je_auto_control.utils.test_record.record_test_class import test_record
 
 # utils image
 from je_auto_control.wrapper.auto_control_image import screenshot
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py` & `je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/core/utils/x11_linux_vk.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py` & `je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/keyboard/x11_linux_keyboard_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/listener/x11_linux_listener.py` & `je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/listener/x11_linux_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py` & `je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/mouse/x11_linux_mouse_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/linux_with_x11/record/x11_linux_record.py` & `je_auto_control_dev-0.0.9/je_auto_control/linux_with_x11/record/x11_linux_record.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/osx/core/utils/osx_vk.py` & `je_auto_control_dev-0.0.9/je_auto_control/osx/core/utils/osx_vk.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/osx/keyboard/osx_keyboard.py` & `je_auto_control_dev-0.0.9/je_auto_control/osx/keyboard/osx_keyboard.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/osx/listener/osx_listener.py` & `je_auto_control_dev-0.0.9/je_auto_control/osx/listener/osx_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/osx/mouse/osx_mouse.py` & `je_auto_control_dev-0.0.9/je_auto_control/osx/mouse/osx_mouse.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/osx/record/osx_record.py` & `je_auto_control_dev-0.0.9/je_auto_control/osx/record/osx_record.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/utils/critical_exit/critcal_exit.py` & `je_auto_control_dev-0.0.9/je_auto_control/utils/critical_exit/critcal_exit.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/utils/exception/exception_tag.py` & `je_auto_control_dev-0.0.9/je_auto_control/utils/exception/exception_tag.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/utils/exception/exceptions.py` & `je_auto_control_dev-0.0.9/je_auto_control/utils/exception/exceptions.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/utils/executor/action_executor.py` & `je_auto_control_dev-0.0.9/je_auto_control/utils/executor/action_executor.py`

 * *Files 6% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 from je_auto_control import special_table
 from je_auto_control import type_key
 from je_auto_control import write
 from je_auto_control.utils.exception.exception_tag import action_is_null_error
 from je_auto_control.utils.exception.exception_tag import cant_execute_action_error
 from je_auto_control.utils.exception.exceptions import AutoControlActionException
 
-from je_auto_control.utils.test_record.record_test_result_class import test_record
+from je_auto_control.utils.test_record.record_test_class import test_record
 
 event_dict = {
     # mouse
     "mouse_left": click_mouse,
     "mouse_right": click_mouse,
     "mouse_middle": click_mouse,
     "mouse_table": mouse_table,
@@ -56,34 +56,43 @@
     "screenshot": screenshot
 }
 
 
 def execute_event(action: list):
     event = event_dict.get(action[0])
     if len(action) == 2:
-        event(**action[1])
+        return event(**action[1])
     elif len(action) == 1:
-        event()
+        return event()
     else:
         raise AutoControlActionException(cant_execute_action_error)
 
 
 def execute_action(action_list: list):
     """
     use to execute all action on action list(action file or program list)
     :param action_list the list include action
     for loop the list and execute action
     """
+    flag = test_record.init_total_record
+    """
+    if init_total_record original is True
+    make it False and then make it return
+    """
+    if flag:
+        test_record.init_total_record = False
     execute_record_string = ""
     if action_list is None:
         raise AutoControlActionNullException(action_is_null_error)
     for action in action_list:
         try:
             execute_event(action)
             temp_string = "execute: " + str(action)
             print(temp_string)
             test_record.record_list.append(temp_string)
             execute_record_string = "".join([execute_record_string, temp_string + "\n"])
         except Exception as error:
             print(repr(error), file=sys.stderr)
             test_record.error_record_list.append([action, repr(error)])
+    if flag:
+        test_record.init_total_record = True
     return execute_record_string
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/utils/image/template_detection.py` & `je_auto_control_dev-0.0.9/je_auto_control/utils/image/template_detection.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/utils/json/json_file.py` & `je_auto_control_dev-0.0.9/je_auto_control/utils/json/json_file.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/utils/timeout/multiprocess_timeout.py` & `je_auto_control_dev-0.0.9/je_auto_control/utils/timeout/multiprocess_timeout.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/win32_ctype_input.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/win32_ctype_input.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/win32_keypress_check.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/win32_keypress_check.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/core/utils/win32_vk.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/core/utils/win32_vk.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/keyboard/win32_ctype_keyboard_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/listener/win32_keyboard_listener.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/listener/win32_keyboard_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/listener/win32_mouse_listener.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/listener/win32_mouse_listener.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/mouse/win32_ctype_mouse_control.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/mouse/win32_ctype_mouse_control.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/windows/record/win32_record.py` & `je_auto_control_dev-0.0.9/je_auto_control/windows/record/win32_record.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_image.py` & `je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_image.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,78 +1,105 @@
+import sys
+
 from je_auto_control.utils.image import template_detection
 from je_auto_control.utils.exception.exception_tag import cant_find_image
 from je_auto_control.utils.exception.exception_tag import find_image_error_variable
 from je_auto_control.utils.exception.exceptions import ImageNotFoundException
 from je_auto_control.wrapper.auto_control_mouse import click_mouse
 from je_auto_control.wrapper.auto_control_mouse import set_position
 from je_auto_control.utils.image.screenshot import pil_screenshot
+from je_auto_control.utils.test_record.record_test_class import record_total
 
 
 def locate_all_image(image, detect_threshold: [float, int] = 1, draw_image: bool = False):
     """
      use to locate all image that detected and then return detected images list
     :param image which image we want to find on screen (png or PIL ImageGrab.grab())
     :param detect_threshold detect precision 0.0 ~ 1.0; 1 is absolute equal (float or int)
     :param draw_image draw detect tag on return image (bool)
     """
+    param = locals()
     try:
-        image_data_array = template_detection.find_image_multi(image, detect_threshold, draw_image)
-    except ImageNotFoundException:
-        raise ImageNotFoundException(find_image_error_variable)
-    if image_data_array[0] is True:
-        return image_data_array[1]
-    else:
-        raise ImageNotFoundException(cant_find_image)
+        try:
+            image_data_array = template_detection.find_image_multi(image, detect_threshold, draw_image)
+        except ImageNotFoundException:
+            raise ImageNotFoundException(find_image_error_variable)
+        if image_data_array[0] is True:
+            record_total("locate_all_image", param)
+            return image_data_array[1]
+        else:
+            raise ImageNotFoundException(cant_find_image)
+    except Exception as error:
+        record_total("locate_all_image", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def locate_image_center(image, detect_threshold: [float, int] = 1, draw_image: bool = False):
     """
     use to locate image and return image center position
     :param image which image we want to find on screen (png or PIL ImageGrab.grab())
     :param detect_threshold detect precision 0.0 ~ 1.0; 1 is absolute equal (float or int)
     :param draw_image draw detect tag on return image (bool)
     """
+    param = locals()
     try:
-        image_data_array = template_detection.find_image(image, detect_threshold, draw_image)
-    except ImageNotFoundException:
-        raise ImageNotFoundException(find_image_error_variable)
-    if image_data_array[0] is True:
-        height = image_data_array[1][2] - image_data_array[1][0]
-        width = image_data_array[1][3] - image_data_array[1][1]
-        center = [int(height / 2), int(width / 2)]
-        return [image_data_array[1][0] + center[0], image_data_array[1][1] + center[1]]
-    else:
-        raise ImageNotFoundException(cant_find_image)
+        try:
+            image_data_array = template_detection.find_image(image, detect_threshold, draw_image)
+        except ImageNotFoundException:
+            raise ImageNotFoundException(find_image_error_variable)
+        if image_data_array[0] is True:
+            height = image_data_array[1][2] - image_data_array[1][0]
+            width = image_data_array[1][3] - image_data_array[1][1]
+            center = [int(height / 2), int(width / 2)]
+            record_total("locate_image_center", param)
+            return [image_data_array[1][0] + center[0], image_data_array[1][1] + center[1]]
+        else:
+            raise ImageNotFoundException(cant_find_image)
+    except Exception as error:
+        record_total("locate_image_center", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def locate_and_click(image, mouse_keycode: [int, str], detect_threshold: [float, int] = 1, draw_image: bool = False):
     """
     use to locate image and click image center position and the return image center position
     :param image which image we want to find on screen (png or PIL ImageGrab.grab())
     :param mouse_keycode which mouse keycode we want to click
     :param detect_threshold detect precision 0.0 ~ 1.0; 1 is absolute equal (float or int)
     :param draw_image draw detect tag on return image (bool)
     """
+    param = locals()
     try:
-        image_data_array = template_detection.find_image(image, detect_threshold, draw_image)
-    except ImageNotFoundException:
-        raise ImageNotFoundException(find_image_error_variable)
-    if image_data_array[0] is True:
-        height = image_data_array[1][2] - image_data_array[1][0]
-        width = image_data_array[1][3] - image_data_array[1][1]
-        center = [int(height / 2), int(width / 2)]
-        image_center_x = image_data_array[1][0] + center[0]
-        image_center_y = image_data_array[1][1] + center[1]
-        set_position(int(image_center_x), int(image_center_y))
-        click_mouse(mouse_keycode)
-        return [image_center_x, image_center_y]
-    else:
-        raise ImageNotFoundException(cant_find_image)
+        try:
+            image_data_array = template_detection.find_image(image, detect_threshold, draw_image)
+        except ImageNotFoundException:
+            raise ImageNotFoundException(find_image_error_variable)
+        if image_data_array[0] is True:
+            height = image_data_array[1][2] - image_data_array[1][0]
+            width = image_data_array[1][3] - image_data_array[1][1]
+            center = [int(height / 2), int(width / 2)]
+            image_center_x = image_data_array[1][0] + center[0]
+            image_center_y = image_data_array[1][1] + center[1]
+            set_position(int(image_center_x), int(image_center_y))
+            click_mouse(mouse_keycode)
+            record_total("locate_and_click", param)
+            return [image_center_x, image_center_y]
+        else:
+            raise ImageNotFoundException(cant_find_image)
+    except Exception as error:
+        record_total("locate_and_click", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def screenshot(file_path: str = None, region: list = None):
     """
     use to get now screen image return image
     :param file_path save screenshot path (None is no save)
     :param region screenshot region (screenshot region on screen)
     """
-    return pil_screenshot(file_path, region)
+    param = locals()
+    try:
+        record_total("screenshot", param)
+        return pil_screenshot(file_path, region)
+    except Exception as error:
+        print(repr(error), file=sys.stderr)
+        record_total("screenshot", param, repr(error))
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_keyboard.py` & `je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_keyboard.py`

 * *Files 15% similar despite different names*

```diff
@@ -8,127 +8,164 @@
 from je_auto_control.utils.exception.exception_tag import keyboard_write_cant_find
 from je_auto_control.utils.exception.exception_tag import table_cant_find_key
 from je_auto_control.utils.exception.exceptions import AutoControlCantFindKeyException
 from je_auto_control.utils.exception.exceptions import AutoControlKeyboardException
 from je_auto_control.wrapper.platform_wrapper import keyboard
 from je_auto_control.wrapper.platform_wrapper import keyboard_check
 from je_auto_control.wrapper.platform_wrapper import keys_table
+from je_auto_control.utils.test_record.record_test_class import record_total
 
 
 def press_key(keycode: [int, str], is_shift: bool = False):
     """
     use to press a key still press to use release key
     or use critical exit
     return keycode
     :param keycode which keycode we want to press
     :param is_shift press shift True or False
     """
-    if type(keycode) is not int:
+    param = locals()
+    try:
+        if type(keycode) is not int:
+            try:
+                keycode = keys_table.get(keycode)
+            except AutoControlCantFindKeyException:
+                raise AutoControlCantFindKeyException(table_cant_find_key)
         try:
-            keycode = keys_table.get(keycode)
-        except AutoControlCantFindKeyException:
-            raise AutoControlCantFindKeyException(table_cant_find_key)
-    try:
-        if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
-            keyboard.press_key(keycode)
-        elif sys.platform in ["darwin"]:
-            keyboard.press_key(keycode, is_shift=is_shift)
-        return str(keycode)
-    except AutoControlKeyboardException:
-        raise AutoControlKeyboardException(keyboard_press_key)
-    except TypeError as error:
-        raise AutoControlKeyboardException(repr(error))
+            if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
+                keyboard.press_key(keycode)
+            elif sys.platform in ["darwin"]:
+                keyboard.press_key(keycode, is_shift=is_shift)
+            record_total("press_key", param)
+            return str(keycode)
+        except AutoControlKeyboardException:
+            raise AutoControlKeyboardException(keyboard_press_key)
+        except TypeError as error:
+            raise AutoControlKeyboardException(repr(error))
+    except Exception as error:
+        record_total("press_key", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def release_key(keycode: [int, str], is_shift: bool = False):
     """
     use to release pressed key return keycode
     :param keycode which keycode we want to release
     :param is_shift press shift True or False
     """
-    if type(keycode) is not int:
+    param = locals()
+    try:
+        if type(keycode) is not int:
+            try:
+                keycode = keys_table.get(keycode)
+            except AutoControlCantFindKeyException:
+                raise AutoControlCantFindKeyException(table_cant_find_key)
         try:
-            keycode = keys_table.get(keycode)
-        except AutoControlCantFindKeyException:
-            raise AutoControlCantFindKeyException(table_cant_find_key)
-    try:
-        if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
-            keyboard.release_key(keycode)
-        elif sys.platform in ["darwin"]:
-            keyboard.release_key(keycode, is_shift=is_shift)
-        return str(keycode)
-    except AutoControlKeyboardException:
-        raise AutoControlKeyboardException(keyboard_release_key)
-    except TypeError as error:
-        raise AutoControlKeyboardException(repr(error))
+            if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
+                keyboard.release_key(keycode)
+            elif sys.platform in ["darwin"]:
+                keyboard.release_key(keycode, is_shift=is_shift)
+            record_total("release_key", param)
+            return str(keycode)
+        except AutoControlKeyboardException:
+            raise AutoControlKeyboardException(keyboard_release_key)
+        except TypeError as error:
+            raise AutoControlKeyboardException(repr(error))
+    except Exception as error:
+        record_total("release_key", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def type_key(keycode: [int, str], is_shift: bool = False):
     """
     press and release key return keycode
     :param keycode which keycode we want to type
     :param is_shift press shift True or False
     """
+    param = locals()
     try:
-        press_key(keycode, is_shift)
-        release_key(keycode, is_shift)
-        return str(keycode)
-    except AutoControlKeyboardException:
-        raise AutoControlKeyboardException(keyboard_type_key)
-    except TypeError as error:
-        raise AutoControlKeyboardException(repr(error))
+        try:
+            press_key(keycode, is_shift)
+            release_key(keycode, is_shift)
+            record_total("type_key", param)
+            return str(keycode)
+        except AutoControlKeyboardException:
+            raise AutoControlKeyboardException(keyboard_type_key)
+        except TypeError as error:
+            raise AutoControlKeyboardException(repr(error))
+    except Exception as error:
+        record_total("type_key", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def check_key_is_press(keycode: [int, str]):
     """
     use to check key is press return True or False
     :param keycode check key is press or not
     """
-    if type(keycode) is int:
-        get_key_code = keycode
-    else:
-        get_key_code = keys_table.get(keycode)
-    return keyboard_check.check_key_is_press(keycode=get_key_code)
+    param = locals()
+    try:
+        if type(keycode) is int:
+            get_key_code = keycode
+        else:
+            get_key_code = keys_table.get(keycode)
+        record_total("check_key_is_press", param)
+        return keyboard_check.check_key_is_press(keycode=get_key_code)
+    except Exception as error:
+        record_total("check_key_is_press", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def write(write_string: str, is_shift: bool = False):
     """
     use to press and release whole we get this function str
     return all press and release str
     :param write_string while string not on write_string+1 type_key(string)
     :param is_shift press shift True or False
     """
+    param = locals()
     try:
-        record_write_string = ""
-        for single_string in write_string:
-            try:
-                if keys_table.get(single_string) is not None:
-                    record_write_string = "".join([record_write_string, type_key(single_string, is_shift)])
-                else:
+        try:
+            record_write_string = ""
+            for single_string in write_string:
+                try:
+                    if keys_table.get(single_string) is not None:
+                        record_write_string = "".join([record_write_string, type_key(single_string, is_shift)])
+                    else:
+                        raise AutoControlKeyboardException(keyboard_write_cant_find)
+                except AutoControlKeyboardException:
+                    print(keyboard_write_cant_find, single_string, sep="\t", file=sys.stderr)
                     raise AutoControlKeyboardException(keyboard_write_cant_find)
-            except AutoControlKeyboardException:
-                print(keyboard_write_cant_find, single_string, sep="\t", file=sys.stderr)
-                raise AutoControlKeyboardException(keyboard_write_cant_find)
-        return record_write_string
-    except AutoControlKeyboardException:
-        raise AutoControlKeyboardException(keyboard_write)
+            record_total("write", param)
+            return record_write_string
+        except AutoControlKeyboardException:
+            raise AutoControlKeyboardException(keyboard_write)
+    except Exception as error:
+        record_total("write", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def hotkey(key_code_list: list, is_shift: bool = False):
     """
     use to press and release all key on key_code_list
     then reverse list press and release again
     return [press_str_list, release_str_list]
     :param key_code_list press and release all key on list and reverse
     :param is_shift press shift True or False
     """
+    param = locals()
     try:
-        record_hotkey_press_string = ""
-        record_hotkey_release_string = ""
-        for key in key_code_list:
-            record_hotkey_press_string = ",".join([record_hotkey_press_string, press_key(key, is_shift)])
-        key_code_list.reverse()
-        for key in key_code_list:
-            record_hotkey_release_string = ",".join([record_hotkey_release_string, release_key(key, is_shift)])
-        return record_hotkey_press_string, record_hotkey_release_string
-    except AutoControlKeyboardException:
-        raise AutoControlKeyboardException(keyboard_hotkey)
+        try:
+            record_hotkey_press_string = ""
+            record_hotkey_release_string = ""
+            for key in key_code_list:
+                record_hotkey_press_string = ",".join([record_hotkey_press_string, press_key(key, is_shift)])
+            key_code_list.reverse()
+            for key in key_code_list:
+                record_hotkey_release_string = ",".join([record_hotkey_release_string, release_key(key, is_shift)])
+            record_total("hotkey", param)
+            return record_hotkey_press_string, record_hotkey_release_string
+        except AutoControlKeyboardException:
+            raise AutoControlKeyboardException(keyboard_hotkey)
+    except Exception as error:
+        record_total("hotkey", param, repr(error))
+        print(repr(error), file=sys.stderr)
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_mouse.py` & `je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_mouse.py`

 * *Files 18% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 from je_auto_control.utils.exception.exception_tag import mouse_wrong_value
 from je_auto_control.utils.exception.exceptions import AutoControlCantFindKeyException
 from je_auto_control.utils.exception.exceptions import AutoControlMouseException
 from je_auto_control.wrapper.auto_control_screen import size
 from je_auto_control.wrapper.platform_wrapper import mouse
 from je_auto_control.wrapper.platform_wrapper import mouse_table
 from je_auto_control.wrapper.platform_wrapper import special_table
+from je_auto_control.utils.test_record.record_test_class import record_total
 
 
 def mouse_preprocess(mouse_keycode: [int, str], x: int, y: int):
     """
     check mouse keycode is verified or not
     and then check current mouse position
     if x or y is None set x, y is current position
@@ -46,130 +47,165 @@
 
 def position():
     """
     get mouse current position
     return mouse_x, mouse_y
     """
     try:
-        return mouse.position()
-    except AutoControlMouseException:
-        raise AutoControlMouseException(mouse_get_position)
+        try:
+            record_total("position", None)
+            return mouse.position()
+        except AutoControlMouseException:
+            raise AutoControlMouseException(mouse_get_position)
+    except Exception as error:
+        record_total("position", None, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def set_position(x: int, y: int):
     """
     :param x set mouse position x
     :param y set mouse position y
     return x, y
     """
+    param = locals()
     try:
-        mouse.set_position(x=x, y=y)
-        return x, y
-    except AutoControlMouseException:
-        raise AutoControlMouseException(mouse_set_position)
-    except ctypes.ArgumentError:
-        raise AutoControlMouseException(mouse_wrong_value)
+        try:
+            mouse.set_position(x=x, y=y)
+            record_total("position", param)
+            return x, y
+        except AutoControlMouseException:
+            raise AutoControlMouseException(mouse_set_position)
+        except ctypes.ArgumentError:
+            raise AutoControlMouseException(mouse_wrong_value)
+    except Exception as error:
+        record_total("set_position", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def press_mouse(mouse_keycode: [int, str], x: int = None, y: int = None):
     """
     press mouse keycode on x, y
     return keycode, x, y
     :param mouse_keycode which mouse keycode we want to press
     :param x mouse click x position
     :param y mouse click y position
     """
-    mouse_keycode, x, y = mouse_preprocess(mouse_keycode, x, y)
+    param = locals()
     try:
-        if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
-            mouse.press_mouse(mouse_keycode)
-        elif sys.platform in ["darwin"]:
-            mouse.press_mouse(x, y, mouse_keycode)
-        return mouse_keycode, x, y
-    except AutoControlMouseException:
-        raise AutoControlMouseException(mouse_press_mouse)
-    except TypeError as error:
-        raise AutoControlMouseException(repr(error))
+        mouse_keycode, x, y = mouse_preprocess(mouse_keycode, x, y)
+        try:
+            if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
+                mouse.press_mouse(mouse_keycode)
+            elif sys.platform in ["darwin"]:
+                mouse.press_mouse(x, y, mouse_keycode)
+            record_total("press_mouse", param)
+            return mouse_keycode, x, y
+        except AutoControlMouseException:
+            raise AutoControlMouseException(mouse_press_mouse)
+        except TypeError as error:
+            raise AutoControlMouseException(repr(error))
+    except Exception as error:
+        record_total("press_mouse", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def release_mouse(mouse_keycode: [int, str], x: int = None, y: int = None):
     """
     release mouse keycode on x, y
     return keycode, x, y
     :param mouse_keycode which mouse keycode we want to release
     :param x mouse click x position
     :param y mouse click y position
     """
-    mouse_keycode, x, y = mouse_preprocess(mouse_keycode, x, y)
+    param = locals()
     try:
-        if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
-            mouse.release_mouse(mouse_keycode)
-        elif sys.platform in ["darwin"]:
-            mouse.release_mouse(x, y, mouse_keycode)
-        return mouse_keycode, x, y
-    except AutoControlMouseException:
-        raise AutoControlMouseException(mouse_release_mouse)
-    except TypeError as error:
-        raise AutoControlMouseException(repr(error))
+        mouse_keycode, x, y = mouse_preprocess(mouse_keycode, x, y)
+        try:
+            if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
+                mouse.release_mouse(mouse_keycode)
+            elif sys.platform in ["darwin"]:
+                mouse.release_mouse(x, y, mouse_keycode)
+            record_total("press_mouse", param)
+            return mouse_keycode, x, y
+        except AutoControlMouseException:
+            raise AutoControlMouseException(mouse_release_mouse)
+        except TypeError as error:
+            raise AutoControlMouseException(repr(error))
+    except Exception as error:
+        record_total("release_mouse", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def click_mouse(mouse_keycode: [int, str], x: int = None, y: int = None):
     """
     press and release mouse keycode on x, y
     return keycode, x, y
     :param mouse_keycode which mouse keycode we want to click
     :param x mouse click x position
     :param y mouse click y position
     """
-    mouse_keycode, x, y = mouse_preprocess(mouse_keycode, x, y)
+    param = locals()
     try:
-        mouse.click_mouse(mouse_keycode, x, y)
-        return mouse_keycode, x, y
-    except AutoControlMouseException:
-        raise AutoControlMouseException(mouse_click_mouse)
-    except TypeError as error:
-        raise AutoControlMouseException(repr(error))
+        mouse_keycode, x, y = mouse_preprocess(mouse_keycode, x, y)
+        try:
+            mouse.click_mouse(mouse_keycode, x, y)
+            record_total("click_mouse", param)
+            return mouse_keycode, x, y
+        except AutoControlMouseException:
+            raise AutoControlMouseException(mouse_click_mouse)
+        except TypeError as error:
+            raise AutoControlMouseException(repr(error))
+    except Exception as error:
+        record_total("click_mouse", param, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def scroll(scroll_value: int, x: int = None, y: int = None, scroll_direction: str = "scroll_down"):
     """"
     :param scroll_value scroll count
     :param x mouse click x position
     :param y mouse click y position
     :param scroll_direction which direction we want
     scroll_direction = scroll_up : direction up
     scroll_direction = scroll_down : direction down
     scroll_direction = scroll_left : direction left
     scroll_direction = scroll_right : direction right
     """
+    param = locals()
     try:
-        now_cursor_x, now_cursor_y = position()
-    except AutoControlMouseException:
-        raise AutoControlMouseException(mouse_get_position)
-    width, height = size()
-    if x is None:
-        x = now_cursor_x
-    else:
-        if x < 0:
-            x = 0
-        elif x >= width:
-            x = width - 1
-    if y is None:
-        y = now_cursor_y
-    else:
-        if y < 0:
-            y = 0
-        elif y >= height:
-            y = height - 1
-    try:
-        if sys.platform in ["win32", "cygwin", "msys"]:
-            mouse.scroll(scroll_value, x, y)
-        elif sys.platform in ["darwin"]:
-            mouse.scroll(scroll_value)
-        elif sys.platform in ["linux", "linux2"]:
-            scroll_direction = special_table.get(scroll_direction)
-            mouse.scroll(scroll_value, scroll_direction)
-        return scroll_value, scroll_direction
-    except AutoControlMouseException:
-        raise AutoControlMouseException(mouse_scroll)
-    except TypeError as error:
-        raise AutoControlMouseException(repr(error))
+        try:
+            now_cursor_x, now_cursor_y = position()
+        except AutoControlMouseException:
+            raise AutoControlMouseException(mouse_get_position)
+        width, height = size()
+        if x is None:
+            x = now_cursor_x
+        else:
+            if x < 0:
+                x = 0
+            elif x >= width:
+                x = width - 1
+        if y is None:
+            y = now_cursor_y
+        else:
+            if y < 0:
+                y = 0
+            elif y >= height:
+                y = height - 1
+        try:
+            if sys.platform in ["win32", "cygwin", "msys"]:
+                mouse.scroll(scroll_value, x, y)
+            elif sys.platform in ["darwin"]:
+                mouse.scroll(scroll_value)
+            elif sys.platform in ["linux", "linux2"]:
+                scroll_direction = special_table.get(scroll_direction)
+                mouse.scroll(scroll_value, scroll_direction)
+            record_total("scroll", param)
+            return scroll_value, scroll_direction
+        except AutoControlMouseException:
+            raise AutoControlMouseException(mouse_scroll)
+        except TypeError as error:
+            raise AutoControlMouseException(repr(error))
+    except Exception as error:
+        record_total("scroll", param, repr(error))
+        print(repr(error), file=sys.stderr)
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_record.py` & `je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_record.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,36 +1,47 @@
 import sys
 
 from je_auto_control.utils.executor.action_executor import execute_action
 from je_auto_control.utils.exception.exception_tag import macos_record_error
 from je_auto_control.utils.exception.exceptions import AutoControlException
 from je_auto_control.utils.exception.exceptions import AutoControlJsonActionException
 from je_auto_control.wrapper.platform_wrapper import recorder
+from je_auto_control.utils.test_record.record_test_class import record_total
 
 
 def record():
     """
     start record keyboard and mouse event until stop_record
     """
-    if sys.platform == "darwin":
-        raise AutoControlException(macos_record_error)
-    return recorder.record()
+    try:
+        if sys.platform == "darwin":
+            raise AutoControlException(macos_record_error)
+        record_total("record", None)
+        return recorder.record()
+    except Exception as error:
+        record_total("record", None, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def stop_record():
     """
     stop current record
     """
-    if sys.platform == "darwin":
-        raise AutoControlException(macos_record_error)
-    action_queue = recorder.stop_record()
-    if action_queue is None:
-        raise AutoControlJsonActionException
-    action_list = list(action_queue.queue)
-    new_list = list()
-    for action in action_list:
-        if action[0] == "type_key":
-            new_list.append([action[0], dict([["keycode", action[1]]])])
-        else:
-            new_list.append([action[0], dict(zip(["mouse_keycode", "x", "y"], [action[0], action[1], action[2]]))])
-    return new_list
+    try:
+        if sys.platform == "darwin":
+            raise AutoControlException(macos_record_error)
+        action_queue = recorder.stop_record()
+        if action_queue is None:
+            raise AutoControlJsonActionException
+        action_list = list(action_queue.queue)
+        new_list = list()
+        for action in action_list:
+            if action[0] == "type_key":
+                new_list.append([action[0], dict([["keycode", action[1]]])])
+            else:
+                new_list.append([action[0], dict(zip(["mouse_keycode", "x", "y"], [action[0], action[1], action[2]]))])
+        record_total("stop_record", None)
+        return new_list
+    except Exception as error:
+        record_total("stop_record", None, repr(error))
+        print(repr(error), file=sys.stderr)
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/wrapper/auto_control_screen.py` & `je_auto_control_dev-0.0.9/je_auto_control/wrapper/auto_control_screen.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,30 +1,44 @@
+import sys
+
 import cv2
 import numpy as np
 
 from je_auto_control.utils.image.screenshot import pil_screenshot
 from je_auto_control.utils.exception.exception_tag import screen_get_size
 from je_auto_control.utils.exception.exception_tag import screen_screenshot
 from je_auto_control.utils.exception.exceptions import AutoControlScreenException
 from je_auto_control.wrapper.platform_wrapper import screen
+from je_auto_control.utils.test_record.record_test_class import record_total
 
 
 def size():
     """
     get screen size
     """
     try:
-        return screen.size()
-    except AutoControlScreenException:
-        raise AutoControlScreenException(screen_get_size)
+        try:
+            record_total("size", None)
+            return screen.size()
+        except AutoControlScreenException:
+            raise AutoControlScreenException(screen_get_size)
+    except Exception as error:
+        record_total("size", None, repr(error))
+        print(repr(error), file=sys.stderr)
 
 
 def screenshot(file_path: str = None, region: list = None):
     """
     use to capture current screen image
     :param file_path screenshot file save path
     :param region screenshot region
     """
+    param = locals()
     try:
-        return cv2.cvtColor(np.array(pil_screenshot(file_path=file_path, region=region)), cv2.COLOR_RGB2BGR)
-    except AutoControlScreenException:
-        raise AutoControlScreenException(screen_screenshot)
+        try:
+            record_total("screenshot", param)
+            return cv2.cvtColor(np.array(pil_screenshot(file_path=file_path, region=region)), cv2.COLOR_RGB2BGR)
+        except AutoControlScreenException:
+            raise AutoControlScreenException(screen_screenshot)
+    except Exception as error:
+        record_total("screenshot", None, repr(error))
+        print(repr(error), file=sys.stderr)
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control/wrapper/platform_wrapper.py` & `je_auto_control_dev-0.0.9/je_auto_control/wrapper/platform_wrapper.py`

 * *Files identical despite different names*

### Comparing `je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/PKG-INFO` & `je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: je-auto-control-dev
-Version: 0.0.8
+Version: 0.0.9
 Summary: auto testing
 Home-page: https://github.com/JE-Chen/AutoControl
 Author: JE-Chen
 Author-email: zenmailman@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.5
@@ -17,14 +17,27 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # je_auto_control
 
 ---
 
+### JE Auto Control as a tool for GUI Testing 
+#### Features
+* Image Detect
+* Keyboard Event
+* Mouse Event
+* Screen 
+* Action file and executor
+* Record Event
+* CLI with action file
+* timeout
+
+---
+
 [![CircleCI](https://circleci.com/gh/JE-Chen/AutoControl/tree/main.svg?style=svg)](https://circleci.com/gh/JE-Chen/AutoControl/tree/main)
 
 ### Documentation
 
 [![Documentation Status](https://readthedocs.org/projects/python-jeautocontrol/badge/?version=latest)](https://python-jeautocontrol.readthedocs.io/en/latest/?badge=latest)
 
 documentation available at [https://python-jeautocontrol.readthedocs.io/en/latest/](https://python-jeautocontrol.readthedocs.io/en/latest/)
```

### Comparing `je_auto_control_dev-0.0.8/je_auto_control_dev.egg-info/SOURCES.txt` & `je_auto_control_dev-0.0.9/je_auto_control_dev.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -44,15 +44,15 @@
 je_auto_control/utils/executor/action_executor.py
 je_auto_control/utils/image/__init__.py
 je_auto_control/utils/image/screenshot.py
 je_auto_control/utils/image/template_detection.py
 je_auto_control/utils/json/__init__.py
 je_auto_control/utils/json/json_file.py
 je_auto_control/utils/test_record/__init__.py
-je_auto_control/utils/test_record/record_test_result_class.py
+je_auto_control/utils/test_record/record_test_class.py
 je_auto_control/utils/timeout/__init__.py
 je_auto_control/utils/timeout/multiprocess_timeout.py
 je_auto_control/windows/__init__.py
 je_auto_control/windows/core/__init__.py
 je_auto_control/windows/core/utils/__init__.py
 je_auto_control/windows/core/utils/win32_ctype_input.py
 je_auto_control/windows/core/utils/win32_keypress_check.py
```

### Comparing `je_auto_control_dev-0.0.8/setup.py` & `je_auto_control_dev-0.0.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as README:
     long_description = README.read()
 
 setuptools.setup(
     name="je_auto_control",
-    version="0.0.80",
+    version="0.0.81",
     author="JE-Chen",
     author_email="zenmailman@gmail.com",
     description="auto testing",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/JE-Chen/AutoControl",
     packages=setuptools.find_packages(),
```

