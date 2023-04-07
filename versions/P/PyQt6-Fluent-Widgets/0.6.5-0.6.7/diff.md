# Comparing `tmp/PyQt6-Fluent-Widgets-0.6.5.tar.gz` & `tmp/PyQt6-Fluent-Widgets-0.6.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\PyQt6-Fluent-Widgets-0.6.5.tar", last modified: Fri Apr  7 07:44:16 2023, max compression
+gzip compressed data, was "dist\PyQt6-Fluent-Widgets-0.6.7.tar", last modified: Fri Apr  7 12:01:16 2023, max compression
```

## Comparing `PyQt6-Fluent-Widgets-0.6.5.tar` & `PyQt6-Fluent-Widgets-0.6.7.tar`

### file list

```diff
@@ -1,72 +1,72 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:16.033986 PyQt6-Fluent-Widgets-0.6.5/
--rw-rw-rw-   0        0        0    35823 2023-04-05 14:53:55.000000 PyQt6-Fluent-Widgets-0.6.5/LICENSE
--rw-rw-rw-   0        0        0     3565 2023-04-07 07:44:16.032980 PyQt6-Fluent-Widgets-0.6.5/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.931982 PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/
--rw-rw-rw-   0        0        0     3565 2023-04-07 07:44:15.000000 PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     2653 2023-04-07 07:44:15.000000 PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 07:44:15.000000 PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       79 2023-04-07 07:44:15.000000 PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-04-07 07:44:15.000000 PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     2765 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.933494 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/
--rw-rw-rw-   0        0        0      493 2023-04-07 07:43:31.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.936539 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/_rc/
--rw-rw-rw-   0        0        0        0 2023-01-17 07:40:20.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/_rc/__init__.py
--rw-rw-rw-   0        0        0  3453874 2023-04-07 07:35:35.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/_rc/resource.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.955953 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/
--rw-rw-rw-   0        0        0      390 2023-04-05 13:34:28.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/__init__.py
--rw-rw-rw-   0        0        0     3193 2023-01-27 14:07:06.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/auto_wrap.py
--rw-rw-rw-   0        0        0    10546 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/config.py
--rw-rw-rw-   0        0        0      675 2023-01-16 13:18:33.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/exception_handler.py
--rw-rw-rw-   0        0        0     7281 2023-04-07 07:32:34.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/icon.py
--rw-rw-rw-   0        0        0     4775 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/image_utils.py
--rw-rw-rw-   0        0        0     4672 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/smooth_scroll.py
--rw-rw-rw-   0        0        0     6977 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/style_sheet.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.958190 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/
--rw-rw-rw-   0        0        0      124 2023-03-26 10:38:38.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.968804 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/
--rw-rw-rw-   0        0        0      170 2023-03-14 08:29:15.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/__init__.py
--rw-rw-rw-   0        0        0    11953 2023-04-07 07:32:34.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/color_dialog.py
--rw-rw-rw-   0        0        0     5361 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/dialog.py
--rw-rw-rw-   0        0        0    11761 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/folder_list_dialog.py
--rw-rw-rw-   0        0        0     3227 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/mask_dialog_base.py
--rw-rw-rw-   0        0        0     2424 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/message_dialog.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.976715 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/
--rw-rw-rw-   0        0        0      114 2023-01-16 13:10:58.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/__init__.py
--rw-rw-rw-   0        0        0     2669 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/expand_layout.py
--rw-rw-rw-   0        0        0     5438 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/flow_layout.py
--rw-rw-rw-   0        0        0     1262 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/v_box_layout.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.984444 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/
--rw-rw-rw-   0        0        0      260 2023-03-18 06:45:47.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/__init__.py
--rw-rw-rw-   0        0        0     4277 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/navigation_interface.py
--rw-rw-rw-   0        0        0    14650 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/navigation_panel.py
--rw-rw-rw-   0        0        0     4931 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/navigation_widget.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:15.996795 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/
--rw-rw-rw-   0        0        0      550 2023-03-24 06:13:50.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/__init__.py
--rw-rw-rw-   0        0        0     5269 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/custom_color_setting_card.py
--rw-rw-rw-   0        0        0     8152 2023-04-07 07:32:34.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/expand_setting_card.py
--rw-rw-rw-   0        0        0     6102 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/folder_list_setting_card.py
--rw-rw-rw-   0        0        0     2840 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/options_setting_card.py
--rw-rw-rw-   0        0        0    13044 2023-04-07 07:32:34.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/setting_card.py
--rw-rw-rw-   0        0        0     1470 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/setting_card_group.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:44:16.030891 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/
--rw-rw-rw-   0        0        0      882 2023-04-07 07:32:34.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/__init__.py
--rw-rw-rw-   0        0        0     4656 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/acrylic_label.py
--rw-rw-rw-   0        0        0     4732 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/button.py
--rw-rw-rw-   0        0        0      304 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/check_box.py
--rw-rw-rw-   0        0        0    10943 2023-04-07 07:36:43.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/combo_box.py
--rw-rw-rw-   0        0        0      757 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/icon_widget.py
--rw-rw-rw-   0        0        0    19137 2023-04-07 07:32:34.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/info_bar.py
--rw-rw-rw-   0        0        0      870 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/label.py
--rw-rw-rw-   0        0        0     6639 2023-04-07 07:32:34.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/line_edit.py
--rw-rw-rw-   0        0        0    24081 2023-04-07 07:40:35.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/menu.py
--rw-rw-rw-   0        0        0     4540 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/scroll_area.py
--rw-rw-rw-   0        0        0     4848 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/slider.py
--rw-rw-rw-   0        0        0     4554 2023-04-07 07:31:01.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/spin_box.py
--rw-rw-rw-   0        0        0     6343 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/stacked_widget.py
--rw-rw-rw-   0        0        0     5923 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/state_tool_tip.py
--rw-rw-rw-   0        0        0     6719 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/switch_button.py
--rw-rw-rw-   0        0        0     1686 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/three_state_button.py
--rw-rw-rw-   0        0        0     5263 2023-04-07 07:30:40.000000 PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/tool_tip.py
--rw-rw-rw-   0        0        0       42 2023-04-07 07:44:16.033986 PyQt6-Fluent-Widgets-0.6.5/setup.cfg
--rw-rw-rw-   0        0        0     1245 2023-04-07 07:43:26.000000 PyQt6-Fluent-Widgets-0.6.5/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.875492 PyQt6-Fluent-Widgets-0.6.7/
+-rw-rw-rw-   0        0        0    35823 2023-04-07 08:57:25.000000 PyQt6-Fluent-Widgets-0.6.7/LICENSE
+-rw-rw-rw-   0        0        0     3565 2023-04-07 12:01:16.875492 PyQt6-Fluent-Widgets-0.6.7/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.774235 PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/
+-rw-rw-rw-   0        0        0     3565 2023-04-07 12:01:16.000000 PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     2653 2023-04-07 12:01:16.000000 PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 12:01:16.000000 PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       79 2023-04-07 12:01:16.000000 PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-07 12:01:16.000000 PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     2765 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.776377 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/
+-rw-rw-rw-   0        0        0      493 2023-04-07 11:59:33.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.778896 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/_rc/
+-rw-rw-rw-   0        0        0        0 2023-01-17 07:40:20.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/_rc/__init__.py
+-rw-rw-rw-   0        0        0  3453874 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/_rc/resource.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.800654 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/
+-rw-rw-rw-   0        0        0      390 2023-04-05 13:34:28.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/__init__.py
+-rw-rw-rw-   0        0        0     3193 2023-01-27 14:07:06.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/auto_wrap.py
+-rw-rw-rw-   0        0        0    10546 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/config.py
+-rw-rw-rw-   0        0        0      675 2023-01-16 13:18:33.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/exception_handler.py
+-rw-rw-rw-   0        0        0     7281 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/icon.py
+-rw-rw-rw-   0        0        0     4775 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/image_utils.py
+-rw-rw-rw-   0        0        0     4672 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/smooth_scroll.py
+-rw-rw-rw-   0        0        0     6977 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/style_sheet.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.801651 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/
+-rw-rw-rw-   0        0        0      124 2023-03-26 10:38:38.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.814096 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/
+-rw-rw-rw-   0        0        0      170 2023-03-14 08:29:15.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/__init__.py
+-rw-rw-rw-   0        0        0    11953 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/color_dialog.py
+-rw-rw-rw-   0        0        0     5361 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/dialog.py
+-rw-rw-rw-   0        0        0    11761 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/folder_list_dialog.py
+-rw-rw-rw-   0        0        0     3227 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/mask_dialog_base.py
+-rw-rw-rw-   0        0        0     2424 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/message_dialog.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.820796 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/
+-rw-rw-rw-   0        0        0      114 2023-01-16 13:10:58.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/__init__.py
+-rw-rw-rw-   0        0        0     2669 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/expand_layout.py
+-rw-rw-rw-   0        0        0     5438 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/flow_layout.py
+-rw-rw-rw-   0        0        0     1262 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/v_box_layout.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.827835 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/
+-rw-rw-rw-   0        0        0      260 2023-03-18 06:45:47.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/__init__.py
+-rw-rw-rw-   0        0        0     4277 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/navigation_interface.py
+-rw-rw-rw-   0        0        0    14650 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/navigation_panel.py
+-rw-rw-rw-   0        0        0     4931 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/navigation_widget.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.841140 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/
+-rw-rw-rw-   0        0        0      550 2023-03-24 06:13:50.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/__init__.py
+-rw-rw-rw-   0        0        0     5269 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/custom_color_setting_card.py
+-rw-rw-rw-   0        0        0     8152 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/expand_setting_card.py
+-rw-rw-rw-   0        0        0     6102 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/folder_list_setting_card.py
+-rw-rw-rw-   0        0        0     2840 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/options_setting_card.py
+-rw-rw-rw-   0        0        0    13044 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/setting_card.py
+-rw-rw-rw-   0        0        0     1470 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/setting_card_group.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:01:16.873485 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/
+-rw-rw-rw-   0        0        0      882 2023-04-07 08:57:25.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/__init__.py
+-rw-rw-rw-   0        0        0     4656 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/acrylic_label.py
+-rw-rw-rw-   0        0        0     4732 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/button.py
+-rw-rw-rw-   0        0        0      304 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/check_box.py
+-rw-rw-rw-   0        0        0    13162 2023-04-07 11:59:17.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/combo_box.py
+-rw-rw-rw-   0        0        0      757 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/icon_widget.py
+-rw-rw-rw-   0        0        0    19137 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/info_bar.py
+-rw-rw-rw-   0        0        0      870 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/label.py
+-rw-rw-rw-   0        0        0     6639 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/line_edit.py
+-rw-rw-rw-   0        0        0    24081 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/menu.py
+-rw-rw-rw-   0        0        0     4540 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/scroll_area.py
+-rw-rw-rw-   0        0        0     4848 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/slider.py
+-rw-rw-rw-   0        0        0     4554 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/spin_box.py
+-rw-rw-rw-   0        0        0     6343 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/stacked_widget.py
+-rw-rw-rw-   0        0        0     5923 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/state_tool_tip.py
+-rw-rw-rw-   0        0        0     6719 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/switch_button.py
+-rw-rw-rw-   0        0        0     1686 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/three_state_button.py
+-rw-rw-rw-   0        0        0     5263 2023-04-07 11:55:55.000000 PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/tool_tip.py
+-rw-rw-rw-   0        0        0       42 2023-04-07 12:01:16.875492 PyQt6-Fluent-Widgets-0.6.7/setup.cfg
+-rw-rw-rw-   0        0        0     1245 2023-04-07 11:59:29.000000 PyQt6-Fluent-Widgets-0.6.7/setup.py
```

### Comparing `PyQt6-Fluent-Widgets-0.6.5/LICENSE` & `PyQt6-Fluent-Widgets-0.6.7/LICENSE`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/PKG-INFO` & `PyQt6-Fluent-Widgets-0.6.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyQt6-Fluent-Widgets
-Version: 0.6.5
+Version: 0.6.7
 Summary: A fluent design widgets library based on PyQt6
 Home-page: https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6
 Author: zhiyiYo
 Author-email: shokokawaii@outlook.com
 License: GPLv3
 Project-URL: Documentation, https://pyqt-fluent-widgets.readthedocs.io/
 Project-URL: Source Code, https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6
```

### Comparing `PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/PKG-INFO` & `PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyQt6-Fluent-Widgets
-Version: 0.6.5
+Version: 0.6.7
 Summary: A fluent design widgets library based on PyQt6
 Home-page: https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6
 Author: zhiyiYo
 Author-email: shokokawaii@outlook.com
 License: GPLv3
 Project-URL: Documentation, https://pyqt-fluent-widgets.readthedocs.io/
 Project-URL: Source Code, https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6
```

### Comparing `PyQt6-Fluent-Widgets-0.6.5/PyQt6_Fluent_Widgets.egg-info/SOURCES.txt` & `PyQt6-Fluent-Widgets-0.6.7/PyQt6_Fluent_Widgets.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/README.md` & `PyQt6-Fluent-Widgets-0.6.7/README.md`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/_rc/resource.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/_rc/resource.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/auto_wrap.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/auto_wrap.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/config.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/config.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/exception_handler.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/exception_handler.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/icon.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/icon.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/image_utils.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/image_utils.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/smooth_scroll.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/smooth_scroll.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/common/style_sheet.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/common/style_sheet.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/color_dialog.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/color_dialog.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/dialog.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/dialog.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/folder_list_dialog.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/folder_list_dialog.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/mask_dialog_base.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/mask_dialog_base.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/dialog_box/message_dialog.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/dialog_box/message_dialog.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/expand_layout.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/expand_layout.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/flow_layout.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/flow_layout.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/layout/v_box_layout.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/layout/v_box_layout.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/navigation_interface.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/navigation_interface.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/navigation_panel.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/navigation_panel.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/navigation/navigation_widget.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/navigation/navigation_widget.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/__init__.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/__init__.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/custom_color_setting_card.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/custom_color_setting_card.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/expand_setting_card.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/expand_setting_card.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/folder_list_setting_card.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/folder_list_setting_card.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/options_setting_card.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/options_setting_card.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/setting_card.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/setting_card.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/settings/setting_card_group.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/settings/setting_card_group.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/__init__.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/__init__.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/acrylic_label.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/acrylic_label.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/button.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/button.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/combo_box.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/combo_box.py`

 * *Files 13% similar despite different names*

```diff
@@ -27,26 +27,30 @@
             the icon of item
 
         userData: Any
             user data
         """
         self.text = text
         self.userData = userData
-        if icon:
-            self._icon = QIcon(icon) if isinstance(icon, str) else icon
-        else:
-            self._icon = QIcon()
+        self.icon = icon
 
     @property
     def icon(self):
         if isinstance(self._icon, QIcon):
             return self._icon
 
         return self._icon.icon()
 
+    @icon.setter
+    def icon(self, ico: Union[str, QIcon, FluentIconBase]):
+        if ico:
+            self._icon = QIcon(ico) if isinstance(ico, str) else ico
+        else:
+            self._icon = QIcon()
+
 
 class ComboBoxBase(QObject):
     """ Combo box base """
 
     currentIndexChanged = pyqtSignal(int)
     currentTextChanged = pyqtSignal(str)
 
@@ -71,15 +75,15 @@
             elif e.type() == QEvent.Type.Enter:
                 self.isHover = True
             elif e.type() == QEvent.Type.Leave:
                 self.isHover = False
 
         return super().eventFilter(obj, e)
 
-    def addItem(self, text, icon: Union[str, QIcon, FluentIconBase] = None, userData=None):
+    def addItem(self, text: str, icon: Union[str, QIcon, FluentIconBase] = None, userData=None):
         """ add item
 
         Parameters
         ----------
         text: str
             the text of item
 
@@ -123,15 +127,15 @@
                 self.setCurrentIndex(0)
                 self.currentTextChanged.emit(self.currentText())
                 self.currentIndexChanged.emit(0)
 
     def currentIndex(self):
         return self._currentIndex
 
-    def setCurrentIndex(self, index):
+    def setCurrentIndex(self, index: int):
         """ set current index
 
         Parameters
         ----------
         index: int
             current index
         """
@@ -147,14 +151,20 @@
 
     def currentText(self):
         if not 0 <= self.currentIndex() < len(self.items):
             return ''
 
         return self.items[self.currentIndex()].text
 
+    def currentData(self):
+        if not 0 <= self.currentIndex() < len(self.items):
+            return None
+
+        return self.items[self.currentIndex()].userData
+
     def setCurrentText(self, text):
         """ set the current text displayed in combo box,
         text should be in the item list
 
         Parameters
         ----------
         text: str
@@ -182,25 +192,44 @@
         item = self.itemMap.pop()
         item.text = text
         self.itemMap[text] = item
         if self.currentIndex() == index:
             self.setText(text)
 
     def itemData(self, index: int):
-        """ Returns the data for the given role in the given index in the combobox """
+        """ Returns the data in the given index """
         if not 0 <= index < len(self.items):
             return None
 
         return self.items[index].userData
 
+    def itemText(self, index: int):
+        """ Returns the text in the given index """
+        if not 0 <= index < len(self.items):
+            return ''
+
+        return self.items[index].text
+
+    def itemIcon(self, index: int):
+        """ Returns the icon in the given index """
+        if not 0 <= index < len(self.items):
+            return QIcon()
+
+        return self.items[index].icon
+
     def setItemData(self, index: int, value):
-        """ Sets the data role for the item on the given index in the combobox to the specified value """
+        """ Sets the data role for the item on the given index """
         if 0 <= index < len(self.items):
             self.items[index].userData = value
 
+    def setItemIcon(self, index: int, icon: Union[str, QIcon, FluentIconBase]):
+        """ Sets the data role for the item on the given index """
+        if 0 <= index < len(self.items):
+            self.items[index].icon = icon
+
     def findData(self, data):
         """ Returns the index of the item containing the given data, otherwise returns -1 """
         for i, item in enumerate(self.items):
             if item.userData == data:
                 return i
 
         return -1
@@ -208,14 +237,54 @@
     def findText(self, text: str):
         """ Returns the index of the item containing the given text; otherwise returns -1. """
         if text not in self.itemMap:
             return -1
 
         return self.items.index(self.itemMap[text])
 
+    def clear(self):
+        """ Clears the combobox, removing all items. """
+        if self.currentIndex() >= 0:
+            self.setText('')
+
+        self.items.clear()
+        self.itemMap.clear()
+        self._currentIndex = -1
+
+    def count(self):
+        """ Returns the number of items in the combobox """
+        return len(self.items)
+
+    def insertItem(self, index: int, text: str, icon: Union[str, QIcon, FluentIconBase] = None, userData=None):
+        """ Inserts item into the combobox at the given index. """
+        if not text or text in self.itemMap:
+            return
+
+        item = ComboItem(text, icon, userData)
+        self.items.insert(index, item)
+        self.itemMap[text] = item
+
+        if index <= self.currentIndex():
+            self._onItemClicked(self.currentIndex() + 1)
+
+    def insertItems(self, index: int, texts: Iterable[str]):
+        """ Inserts items into the combobox, starting at the index specified. """
+        pos = index
+        for text in texts:
+            if not text or text in self.itemMap:
+                continue
+
+            item = ComboItem(text)
+            self.items.insert(pos, item)
+            self.itemMap[text] = item
+            pos += 1
+
+        if index <= self.currentIndex():
+            self._onItemClicked(self.currentIndex() + pos - index)
+
     def _closeComboMenu(self):
         if not self.dropMenu:
             return
 
         self.dropMenu.close()
         self.dropMenu = None
```

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/icon_widget.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/icon_widget.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/info_bar.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/info_bar.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/label.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/label.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/line_edit.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/line_edit.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/menu.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/menu.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/scroll_area.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/scroll_area.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/slider.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/slider.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/spin_box.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/spin_box.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/stacked_widget.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/stacked_widget.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/state_tool_tip.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/state_tool_tip.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/switch_button.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/switch_button.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/three_state_button.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/three_state_button.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/qfluentwidgets/components/widgets/tool_tip.py` & `PyQt6-Fluent-Widgets-0.6.7/qfluentwidgets/components/widgets/tool_tip.py`

 * *Files identical despite different names*

### Comparing `PyQt6-Fluent-Widgets-0.6.5/setup.py` & `PyQt6-Fluent-Widgets-0.6.7/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 
 with open('README.md', encoding='utf-8') as f:
     long_description = f.read()
 
 setuptools.setup(
     name="PyQt6-Fluent-Widgets",
-    version="0.6.5",
+    version="0.6.7",
     keywords="pyqt6 fluent widgets",
     author="zhiyiYo",
     author_email="shokokawaii@outlook.com",
     description="A fluent design widgets library based on PyQt6",
     long_description=long_description,
     long_description_content_type='text/markdown',
     license="GPLv3",
```

