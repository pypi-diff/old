# Comparing `tmp/textual-0.9.0.tar.gz` & `tmp/textual-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "textual-0.9.0.tar", max compression
+gzip compressed data, was "textual-0.9.1.tar", max compression
```

## Comparing `textual-0.9.0.tar` & `textual-0.9.1.tar`

### file list

```diff
@@ -1,154 +1,155 @@
--rw-r--r--   0        0        0     1069 2022-02-27 15:19:02.504488 textual-0.9.0/LICENSE
--rw-r--r--   0        0        0     3690 2022-10-23 17:46:15.174455 textual-0.9.0/README.md
--rw-r--r--   0        0        0     2139 2022-12-30 13:24:11.767441 textual-0.9.0/pyproject.toml
--rw-r--r--   0        0        0     3203 2022-12-18 22:11:26.936415 textual-0.9.0/src/textual/__init__.py
--rw-r--r--   0        0        0       89 2022-10-22 17:52:58.358007 textual-0.9.0/src/textual/__main__.py
--rw-r--r--   0        0        0    13171 2022-11-18 16:13:22.297038 textual-0.9.0/src/textual/_animator.py
--rw-r--r--   0        0        0    13096 2022-12-20 19:50:00.886936 textual-0.9.0/src/textual/_ansi_sequences.py
--rw-r--r--   0        0        0     4750 2022-12-04 11:00:07.623756 textual-0.9.0/src/textual/_arrange.py
--rw-r--r--   0        0        0     5445 2022-11-18 16:13:22.297163 textual-0.9.0/src/textual/_border.py
--rw-r--r--   0        0        0     8630 2022-12-30 09:40:38.838511 textual-0.9.0/src/textual/_cache.py
--rw-r--r--   0        0        0      754 2022-10-22 17:52:58.359064 textual-0.9.0/src/textual/_callback.py
--rw-r--r--   0        0        0      140 2022-10-22 17:52:58.359127 textual-0.9.0/src/textual/_cells.py
--rw-r--r--   0        0        0     1743 2022-10-22 17:52:58.359185 textual-0.9.0/src/textual/_clock.py
--rw-r--r--   0        0        0     5759 2022-10-22 17:52:58.359412 textual-0.9.0/src/textual/_color_constants.py
--rw-r--r--   0        0        0    28197 2022-12-30 09:40:38.838885 textual-0.9.0/src/textual/_compositor.py
--rw-r--r--   0        0        0      221 2022-10-22 17:52:58.359842 textual-0.9.0/src/textual/_context.py
--rw-r--r--   0        0        0     4096 2022-11-07 12:01:46.889498 textual-0.9.0/src/textual/_doc.py
--rw-r--r--   0        0        0     1269 2022-10-22 17:52:58.359972 textual-0.9.0/src/textual/_duration.py
--rw-r--r--   0        0        0     4101 2022-11-10 15:26:26.432170 textual-0.9.0/src/textual/_easing.py
--rw-r--r--   0        0        0      774 2022-10-22 17:52:58.360063 textual-0.9.0/src/textual/_event_broker.py
--rw-r--r--   0        0        0     1415 2022-12-30 09:40:38.839221 textual-0.9.0/src/textual/_filter.py
--rw-r--r--   0        0        0     3593 2022-11-07 12:01:46.715920 textual-0.9.0/src/textual/_import_app.py
--rw-r--r--   0        0        0     2954 2022-12-08 15:40:02.413281 textual-0.9.0/src/textual/_layout.py
--rw-r--r--   0        0        0     3551 2022-10-22 17:52:58.360490 textual-0.9.0/src/textual/_layout_resolve.py
--rw-r--r--   0        0        0      405 2022-10-22 17:52:58.360546 textual-0.9.0/src/textual/_log.py
--rw-r--r--   0        0        0     1265 2022-02-27 15:19:02.513260 textual-0.9.0/src/textual/_loop.py
--rw-r--r--   0        0        0     4415 2022-11-26 12:51:25.659028 textual-0.9.0/src/textual/_node_list.py
--rw-r--r--   0        0        0     1559 2022-10-22 17:52:58.360671 textual-0.9.0/src/textual/_opacity.py
--rw-r--r--   0        0        0     4868 2022-11-07 12:01:46.508942 textual-0.9.0/src/textual/_parser.py
--rw-r--r--   0        0        0      903 2022-10-22 17:52:58.360860 textual-0.9.0/src/textual/_partition.py
--rw-r--r--   0        0        0     1109 2022-11-07 12:01:46.472093 textual-0.9.0/src/textual/_path.py
--rw-r--r--   0        0        0      457 2022-10-22 17:52:58.361002 textual-0.9.0/src/textual/_profile.py
--rw-r--r--   0        0        0     4566 2022-11-12 16:59:33.627004 textual-0.9.0/src/textual/_resolve.py
--rw-r--r--   0        0        0     5682 2022-12-30 09:40:38.839492 textual-0.9.0/src/textual/_segment_tools.py
--rw-r--r--   0        0        0     1675 2022-12-30 09:40:38.839734 textual-0.9.0/src/textual/_sleep.py
--rw-r--r--   0        0        0    13294 2022-12-30 09:40:38.840008 textual-0.9.0/src/textual/_styles_cache.py
--rw-r--r--   0        0        0     5148 2022-10-22 17:52:58.361469 textual-0.9.0/src/textual/_text_backend.py
--rw-r--r--   0        0        0      624 2022-12-30 10:21:41.504987 textual-0.9.0/src/textual/_time.py
--rw-r--r--   0        0        0      776 2022-12-30 09:40:38.840499 textual-0.9.0/src/textual/_types.py
--rw-r--r--   0        0        0      384 2022-12-21 14:45:18.989823 textual-0.9.0/src/textual/_typing.py
--rw-r--r--   0        0        0    11136 2022-10-22 17:52:58.361749 textual-0.9.0/src/textual/_xterm_parser.py
--rw-r--r--   0        0        0     1140 2022-12-21 14:45:18.990212 textual-0.9.0/src/textual/actions.py
--rw-r--r--   0        0        0    75921 2022-12-26 21:57:23.914315 textual-0.9.0/src/textual/app.py
--rw-r--r--   0        0        0      687 2022-11-12 08:33:26.042782 textual-0.9.0/src/textual/await_remove.py
--rw-r--r--   0        0        0     5562 2022-12-21 16:18:26.891842 textual-0.9.0/src/textual/binding.py
--rw-r--r--   0        0        0     4922 2022-12-08 10:45:49.303809 textual-0.9.0/src/textual/box_model.py
--rw-r--r--   0        0        0      536 2022-11-18 16:13:22.299069 textual-0.9.0/src/textual/case.py
--rw-r--r--   0        0        0        0 2022-10-26 10:00:42.151448 textual-0.9.0/src/textual/cli/__init__.py
--rw-r--r--   0        0        0       28 2022-10-26 10:00:42.152100 textual-0.9.0/src/textual/cli/__main__.py
--rw-r--r--   0        0        0     3360 2022-12-21 16:18:26.892208 textual-0.9.0/src/textual/cli/cli.py
--rw-r--r--   0        0        0        0 2022-10-26 10:00:42.152362 textual-0.9.0/src/textual/cli/previews/__init__.py
--rw-r--r--   0        0        0     1597 2022-12-28 11:00:37.784790 textual-0.9.0/src/textual/cli/previews/borders.py
--rw-r--r--   0        0        0     5901 2022-12-08 15:40:02.413913 textual-0.9.0/src/textual/cli/previews/colors.css
--rw-r--r--   0        0        0     2210 2022-11-18 16:13:22.299367 textual-0.9.0/src/textual/cli/previews/colors.py
--rw-r--r--   0        0        0      748 2022-12-08 15:40:02.414128 textual-0.9.0/src/textual/cli/previews/easing.css
--rw-r--r--   0        0        0     3593 2022-11-18 16:13:22.299591 textual-0.9.0/src/textual/cli/previews/easing.py
--rw-r--r--   0        0        0     1468 2022-12-21 16:18:26.892612 textual-0.9.0/src/textual/cli/previews/keys.py
--rw-r--r--   0        0        0    17682 2022-12-21 14:45:18.992663 textual-0.9.0/src/textual/color.py
--rw-r--r--   0        0        0      157 2022-10-22 17:52:58.366423 textual-0.9.0/src/textual/constants.py
--rw-r--r--   0        0        0     1080 2022-12-07 15:59:15.569030 textual-0.9.0/src/textual/containers.py
--rw-r--r--   0        0        0        0 2022-10-22 17:52:58.366532 textual-0.9.0/src/textual/css/__init__.py
--rw-r--r--   0        0        0      798 2022-10-22 17:52:58.366646 textual-0.9.0/src/textual/css/_error_tools.py
--rw-r--r--   0        0        0     2751 2022-10-22 17:52:58.366876 textual-0.9.0/src/textual/css/_help_renderables.py
--rw-r--r--   0        0        0    27657 2022-11-07 12:01:46.731547 textual-0.9.0/src/textual/css/_help_text.py
--rw-r--r--   0        0        0    34929 2022-12-21 14:45:18.993236 textual-0.9.0/src/textual/css/_style_properties.py
--rw-r--r--   0        0        0    36243 2022-11-07 12:01:46.679887 textual-0.9.0/src/textual/css/_styles_builder.py
--rw-r--r--   0        0        0     1213 2022-12-21 14:45:18.993659 textual-0.9.0/src/textual/css/constants.py
--rw-r--r--   0        0        0     1287 2022-10-22 17:52:58.367863 textual-0.9.0/src/textual/css/errors.py
--rw-r--r--   0        0        0     2456 2022-12-21 14:46:04.899822 textual-0.9.0/src/textual/css/match.py
--rw-r--r--   0        0        0     7078 2022-10-31 15:40:23.860640 textual-0.9.0/src/textual/css/model.py
--rw-r--r--   0        0        0    12990 2022-12-10 11:00:36.089131 textual-0.9.0/src/textual/css/parse.py
--rw-r--r--   0        0        0    12095 2022-12-16 09:08:40.131038 textual-0.9.0/src/textual/css/query.py
--rw-r--r--   0        0        0    10355 2022-11-18 16:13:22.300441 textual-0.9.0/src/textual/css/scalar.py
--rw-r--r--   0        0        0     2388 2022-11-12 16:59:33.627539 textual-0.9.0/src/textual/css/scalar_animation.py
--rw-r--r--   0        0        0    35806 2022-12-21 16:18:26.893263 textual-0.9.0/src/textual/css/styles.py
--rw-r--r--   0        0        0    18616 2022-12-21 14:46:04.900301 textual-0.9.0/src/textual/css/stylesheet.py
--rw-r--r--   0        0        0     6486 2022-11-26 12:51:25.661742 textual-0.9.0/src/textual/css/tokenize.py
--rw-r--r--   0        0        0     7529 2022-10-22 17:52:58.369493 textual-0.9.0/src/textual/css/tokenizer.py
--rw-r--r--   0        0        0      417 2022-10-22 17:52:58.369557 textual-0.9.0/src/textual/css/transition.py
--rw-r--r--   0        0        0      988 2022-11-07 12:01:46.488961 textual-0.9.0/src/textual/css/types.py
--rw-r--r--   0        0        0     3586 2022-12-23 09:16:11.111009 textual-0.9.0/src/textual/demo.css
--rw-r--r--   0        0        0    11417 2022-12-25 13:32:38.729066 textual-0.9.0/src/textual/demo.py
--rw-r--r--   0        0        0     7096 2022-12-18 09:59:12.659903 textual-0.9.0/src/textual/design.py
--rw-r--r--   0        0        0        0 2022-10-26 10:00:42.153340 textual-0.9.0/src/textual/devtools/__init__.py
--rw-r--r--   0        0        0     9735 2022-10-26 10:00:42.153668 textual-0.9.0/src/textual/devtools/client.py
--rw-r--r--   0        0        0     4210 2022-10-26 10:00:42.160137 textual-0.9.0/src/textual/devtools/redirect_output.py
--rw-r--r--   0        0        0     4303 2022-11-07 12:01:46.489263 textual-0.9.0/src/textual/devtools/renderables.py
--rw-r--r--   0        0        0     2282 2022-10-26 10:00:42.160414 textual-0.9.0/src/textual/devtools/server.py
--rw-r--r--   0        0        0    11081 2022-10-26 10:00:42.160582 textual-0.9.0/src/textual/devtools/service.py
--rw-r--r--   0        0        0    27716 2022-12-26 17:35:30.358741 textual-0.9.0/src/textual/dom.py
--rw-r--r--   0        0        0     1665 2022-10-31 13:53:45.695176 textual-0.9.0/src/textual/driver.py
--rw-r--r--   0        0        0        0 2022-02-27 15:19:02.514106 textual-0.9.0/src/textual/drivers/__init__.py
--rw-r--r--   0        0        0     1457 2022-10-31 13:53:45.695538 textual-0.9.0/src/textual/drivers/headless_driver.py
--rw-r--r--   0        0        0     7681 2022-12-21 16:52:10.014442 textual-0.9.0/src/textual/drivers/linux_driver.py
--rw-r--r--   0        0        0     9302 2022-10-22 17:52:58.372798 textual-0.9.0/src/textual/drivers/win32.py
--rw-r--r--   0        0        0     3049 2022-11-23 13:27:56.783298 textual-0.9.0/src/textual/drivers/windows_driver.py
--rw-r--r--   0        0        0      424 2022-10-22 17:52:58.373018 textual-0.9.0/src/textual/errors.py
--rw-r--r--   0        0        0    14018 2022-12-21 16:18:26.894317 textual-0.9.0/src/textual/events.py
--rw-r--r--   0        0        0      659 2022-11-07 12:01:46.489777 textual-0.9.0/src/textual/features.py
--rw-r--r--   0        0        0     1175 2022-11-07 12:01:46.473300 textual-0.9.0/src/textual/file_monitor.py
--rw-r--r--   0        0        0    30494 2022-12-21 14:45:18.995884 textual-0.9.0/src/textual/geometry.py
--rw-r--r--   0        0        0     7187 2022-12-25 13:32:53.002814 textual-0.9.0/src/textual/keys.py
--rw-r--r--   0        0        0        0 2022-02-27 15:19:02.514972 textual-0.9.0/src/textual/layouts/__init__.py
--rw-r--r--   0        0        0      769 2022-10-22 17:52:58.374570 textual-0.9.0/src/textual/layouts/factory.py
--rw-r--r--   0        0        0     5529 2022-10-31 13:53:45.696732 textual-0.9.0/src/textual/layouts/grid.py
--rw-r--r--   0        0        0     2061 2022-12-08 15:40:02.414653 textual-0.9.0/src/textual/layouts/horizontal.py
--rw-r--r--   0        0        0     1694 2022-11-24 09:23:17.766068 textual-0.9.0/src/textual/layouts/vertical.py
--rw-r--r--   0        0        0     3550 2022-12-21 16:18:26.895096 textual-0.9.0/src/textual/message.py
--rw-r--r--   0        0        0    21677 2022-12-21 16:18:26.895399 textual-0.9.0/src/textual/message_pump.py
--rw-r--r--   0        0        0     2483 2022-10-31 13:53:45.698521 textual-0.9.0/src/textual/messages.py
--rw-r--r--   0        0        0     1382 2022-11-12 16:59:33.628215 textual-0.9.0/src/textual/pilot.py
--rw-r--r--   0        0        0        0 2022-10-06 12:43:36.712808 textual-0.9.0/src/textual/py.typed
--rw-r--r--   0        0        0    12334 2022-12-26 17:29:08.654476 textual-0.9.0/src/textual/reactive.py
--rw-r--r--   0        0        0      743 2022-10-22 17:52:58.375413 textual-0.9.0/src/textual/render.py
--rw-r--r--   0        0        0        0 2022-10-22 17:52:58.375450 textual-0.9.0/src/textual/renderables/__init__.py
--rw-r--r--   0        0        0     1330 2022-10-22 17:52:58.375547 textual-0.9.0/src/textual/renderables/_blend_colors.py
--rw-r--r--   0        0        0     1662 2022-10-22 17:52:58.375605 textual-0.9.0/src/textual/renderables/align.py
--rw-r--r--   0        0        0      779 2022-11-18 16:13:22.302833 textual-0.9.0/src/textual/renderables/blank.py
--rw-r--r--   0        0        0     1150 2022-11-18 16:13:22.302970 textual-0.9.0/src/textual/renderables/gradient.py
--rw-r--r--   0        0        0     3844 2022-10-22 17:52:58.376095 textual-0.9.0/src/textual/renderables/sparkline.py
--rw-r--r--   0        0        0     3661 2022-10-22 17:52:58.376163 textual-0.9.0/src/textual/renderables/text_opacity.py
--rw-r--r--   0        0        0     2340 2022-10-22 17:52:58.376232 textual-0.9.0/src/textual/renderables/tint.py
--rw-r--r--   0        0        0     4565 2022-10-22 17:52:58.376320 textual-0.9.0/src/textual/renderables/underline_bar.py
--rw-r--r--   0        0        0    17542 2022-10-22 17:52:58.376482 textual-0.9.0/src/textual/richreadme.md
--rw-r--r--   0        0        0    17955 2022-12-29 17:29:48.715354 textual-0.9.0/src/textual/screen.py
--rw-r--r--   0        0        0     3073 2022-12-30 09:40:38.840844 textual-0.9.0/src/textual/scroll_view.py
--rw-r--r--   0        0        0    10441 2022-12-11 13:20:31.269123 textual-0.9.0/src/textual/scrollbar.py
--rw-r--r--   0        0        0     9408 2022-12-30 09:40:38.841062 textual-0.9.0/src/textual/strip.py
--rw-r--r--   0        0        0     1482 2022-10-22 17:52:58.377130 textual-0.9.0/src/textual/suggestions.py
--rw-r--r--   0        0        0     5533 2022-12-30 09:40:38.841318 textual-0.9.0/src/textual/timer.py
--rw-r--r--   0        0        0     3455 2022-11-18 16:13:22.303686 textual-0.9.0/src/textual/walk.py
--rw-r--r--   0        0        0    84762 2022-12-30 09:40:38.841937 textual-0.9.0/src/textual/widget.py
--rw-r--r--   0        0        0     1939 2022-12-09 10:29:05.488921 textual-0.9.0/src/textual/widgets/__init__.py
--rw-r--r--   0        0        0      806 2022-12-09 10:29:05.489061 textual-0.9.0/src/textual/widgets/__init__.pyi
--rw-r--r--   0        0        0    10096 2022-12-13 09:54:36.939142 textual-0.9.0/src/textual/widgets/_button.py
--rw-r--r--   0        0        0     3782 2022-12-13 09:54:36.939396 textual-0.9.0/src/textual/widgets/_checkbox.py
--rw-r--r--   0        0        0    21230 2022-12-30 09:40:38.842331 textual-0.9.0/src/textual/widgets/_data_table.py
--rw-r--r--   0        0        0     5025 2022-12-28 11:00:37.785288 textual-0.9.0/src/textual/widgets/_directory_tree.py
--rw-r--r--   0        0        0     4040 2022-12-20 13:19:32.723070 textual-0.9.0/src/textual/widgets/_footer.py
--rw-r--r--   0        0        0     3085 2022-12-21 14:45:18.999329 textual-0.9.0/src/textual/widgets/_header.py
--rw-r--r--   0        0        0    11435 2022-12-21 16:18:26.896036 textual-0.9.0/src/textual/widgets/_input.py
--rw-r--r--   0        0        0      305 2022-12-07 13:52:34.359242 textual-0.9.0/src/textual/widgets/_label.py
--rw-r--r--   0        0        0      980 2022-12-09 10:29:05.489160 textual-0.9.0/src/textual/widgets/_list_item.py
--rw-r--r--   0        0        0     5748 2022-12-13 09:54:36.939740 textual-0.9.0/src/textual/widgets/_list_view.py
--rw-r--r--   0        0        0     6488 2022-12-11 13:20:31.270304 textual-0.9.0/src/textual/widgets/_placeholder.py
--rw-r--r--   0        0        0      778 2022-10-22 17:52:58.379703 textual-0.9.0/src/textual/widgets/_pretty.py
--rw-r--r--   0        0        0     3173 2022-12-21 14:45:18.999914 textual-0.9.0/src/textual/widgets/_static.py
--rw-r--r--   0        0        0     5718 2022-12-30 09:40:38.842942 textual-0.9.0/src/textual/widgets/_text_log.py
--rw-r--r--   0        0        0    26601 2022-12-30 09:40:38.843460 textual-0.9.0/src/textual/widgets/_tree.py
--rw-r--r--   0        0        0       40 2022-11-23 13:27:56.784859 textual-0.9.0/src/textual/widgets/_tree_node.py
--rw-r--r--   0        0        0     1287 2022-10-22 17:52:58.380149 textual-0.9.0/src/textual/widgets/_welcome.py
--rw-r--r--   0        0        0    13381 2022-11-18 16:13:22.305628 textual-0.9.0/src/textual/widgets/tabs.py
--rw-r--r--   0        0        0     5061 1970-01-01 00:00:00.000000 textual-0.9.0/setup.py
--rw-r--r--   0        0        0     5299 1970-01-01 00:00:00.000000 textual-0.9.0/PKG-INFO
+-rw-r--r--   0        0        0     1069 2022-02-27 15:19:02.504488 textual-0.9.1/LICENSE
+-rw-r--r--   0        0        0     3690 2022-10-23 17:46:15.174455 textual-0.9.1/README.md
+-rw-r--r--   0        0        0     2139 2022-12-30 17:38:05.338233 textual-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0     3203 2022-12-18 22:11:26.936415 textual-0.9.1/src/textual/__init__.py
+-rw-r--r--   0        0        0       89 2022-10-22 17:52:58.358007 textual-0.9.1/src/textual/__main__.py
+-rw-r--r--   0        0        0    13171 2022-11-18 16:13:22.297038 textual-0.9.1/src/textual/_animator.py
+-rw-r--r--   0        0        0    13096 2022-12-20 19:50:00.886936 textual-0.9.1/src/textual/_ansi_sequences.py
+-rw-r--r--   0        0        0     4750 2022-12-04 11:00:07.623756 textual-0.9.1/src/textual/_arrange.py
+-rw-r--r--   0        0        0     5445 2022-11-18 16:13:22.297163 textual-0.9.1/src/textual/_border.py
+-rw-r--r--   0        0        0     8630 2022-12-30 09:40:38.838511 textual-0.9.1/src/textual/_cache.py
+-rw-r--r--   0        0        0      754 2022-10-22 17:52:58.359064 textual-0.9.1/src/textual/_callback.py
+-rw-r--r--   0        0        0      140 2022-10-22 17:52:58.359127 textual-0.9.1/src/textual/_cells.py
+-rw-r--r--   0        0        0     1743 2022-10-22 17:52:58.359185 textual-0.9.1/src/textual/_clock.py
+-rw-r--r--   0        0        0     5759 2022-10-22 17:52:58.359412 textual-0.9.1/src/textual/_color_constants.py
+-rw-r--r--   0        0        0    28197 2022-12-30 09:40:38.838885 textual-0.9.1/src/textual/_compositor.py
+-rw-r--r--   0        0        0      221 2022-10-22 17:52:58.359842 textual-0.9.1/src/textual/_context.py
+-rw-r--r--   0        0        0     4096 2022-11-07 12:01:46.889498 textual-0.9.1/src/textual/_doc.py
+-rw-r--r--   0        0        0     1269 2022-10-22 17:52:58.359972 textual-0.9.1/src/textual/_duration.py
+-rw-r--r--   0        0        0     4101 2022-11-10 15:26:26.432170 textual-0.9.1/src/textual/_easing.py
+-rw-r--r--   0        0        0      774 2022-10-22 17:52:58.360063 textual-0.9.1/src/textual/_event_broker.py
+-rw-r--r--   0        0        0     1415 2022-12-30 09:40:38.839221 textual-0.9.1/src/textual/_filter.py
+-rw-r--r--   0        0        0     3593 2022-11-07 12:01:46.715920 textual-0.9.1/src/textual/_import_app.py
+-rw-r--r--   0        0        0     2954 2022-12-08 15:40:02.413281 textual-0.9.1/src/textual/_layout.py
+-rw-r--r--   0        0        0     3551 2022-10-22 17:52:58.360490 textual-0.9.1/src/textual/_layout_resolve.py
+-rw-r--r--   0        0        0      405 2022-10-22 17:52:58.360546 textual-0.9.1/src/textual/_log.py
+-rw-r--r--   0        0        0     1265 2022-02-27 15:19:02.513260 textual-0.9.1/src/textual/_loop.py
+-rw-r--r--   0        0        0     4415 2022-11-26 12:51:25.659028 textual-0.9.1/src/textual/_node_list.py
+-rw-r--r--   0        0        0     1559 2022-10-22 17:52:58.360671 textual-0.9.1/src/textual/_opacity.py
+-rw-r--r--   0        0        0     4868 2022-11-07 12:01:46.508942 textual-0.9.1/src/textual/_parser.py
+-rw-r--r--   0        0        0      903 2022-10-22 17:52:58.360860 textual-0.9.1/src/textual/_partition.py
+-rw-r--r--   0        0        0     1109 2022-11-07 12:01:46.472093 textual-0.9.1/src/textual/_path.py
+-rw-r--r--   0        0        0      457 2022-10-22 17:52:58.361002 textual-0.9.1/src/textual/_profile.py
+-rw-r--r--   0        0        0     4566 2022-11-12 16:59:33.627004 textual-0.9.1/src/textual/_resolve.py
+-rw-r--r--   0        0        0     5682 2022-12-30 09:40:38.839492 textual-0.9.1/src/textual/_segment_tools.py
+-rw-r--r--   0        0        0     1675 2022-12-30 09:40:38.839734 textual-0.9.1/src/textual/_sleep.py
+-rw-r--r--   0        0        0    13294 2022-12-30 09:40:38.840008 textual-0.9.1/src/textual/_styles_cache.py
+-rw-r--r--   0        0        0     5148 2022-10-22 17:52:58.361469 textual-0.9.1/src/textual/_text_backend.py
+-rw-r--r--   0        0        0      898 2022-12-30 17:38:05.338513 textual-0.9.1/src/textual/_time.py
+-rw-r--r--   0        0        0      776 2022-12-30 09:40:38.840499 textual-0.9.1/src/textual/_types.py
+-rw-r--r--   0        0        0      384 2022-12-21 14:45:18.989823 textual-0.9.1/src/textual/_typing.py
+-rw-r--r--   0        0        0     1128 2022-12-30 17:38:05.338920 textual-0.9.1/src/textual/_win_sleep.py
+-rw-r--r--   0        0        0    11136 2022-10-22 17:52:58.361749 textual-0.9.1/src/textual/_xterm_parser.py
+-rw-r--r--   0        0        0     1140 2022-12-21 14:45:18.990212 textual-0.9.1/src/textual/actions.py
+-rw-r--r--   0        0        0    75921 2022-12-26 21:57:23.914315 textual-0.9.1/src/textual/app.py
+-rw-r--r--   0        0        0      687 2022-11-12 08:33:26.042782 textual-0.9.1/src/textual/await_remove.py
+-rw-r--r--   0        0        0     5562 2022-12-21 16:18:26.891842 textual-0.9.1/src/textual/binding.py
+-rw-r--r--   0        0        0     4922 2022-12-08 10:45:49.303809 textual-0.9.1/src/textual/box_model.py
+-rw-r--r--   0        0        0      536 2022-11-18 16:13:22.299069 textual-0.9.1/src/textual/case.py
+-rw-r--r--   0        0        0        0 2022-10-26 10:00:42.151448 textual-0.9.1/src/textual/cli/__init__.py
+-rw-r--r--   0        0        0       28 2022-10-26 10:00:42.152100 textual-0.9.1/src/textual/cli/__main__.py
+-rw-r--r--   0        0        0     3360 2022-12-21 16:18:26.892208 textual-0.9.1/src/textual/cli/cli.py
+-rw-r--r--   0        0        0        0 2022-10-26 10:00:42.152362 textual-0.9.1/src/textual/cli/previews/__init__.py
+-rw-r--r--   0        0        0     1597 2022-12-28 11:00:37.784790 textual-0.9.1/src/textual/cli/previews/borders.py
+-rw-r--r--   0        0        0     5901 2022-12-08 15:40:02.413913 textual-0.9.1/src/textual/cli/previews/colors.css
+-rw-r--r--   0        0        0     2210 2022-11-18 16:13:22.299367 textual-0.9.1/src/textual/cli/previews/colors.py
+-rw-r--r--   0        0        0      748 2022-12-08 15:40:02.414128 textual-0.9.1/src/textual/cli/previews/easing.css
+-rw-r--r--   0        0        0     3593 2022-11-18 16:13:22.299591 textual-0.9.1/src/textual/cli/previews/easing.py
+-rw-r--r--   0        0        0     1468 2022-12-21 16:18:26.892612 textual-0.9.1/src/textual/cli/previews/keys.py
+-rw-r--r--   0        0        0    17682 2022-12-21 14:45:18.992663 textual-0.9.1/src/textual/color.py
+-rw-r--r--   0        0        0      157 2022-10-22 17:52:58.366423 textual-0.9.1/src/textual/constants.py
+-rw-r--r--   0        0        0     1080 2022-12-07 15:59:15.569030 textual-0.9.1/src/textual/containers.py
+-rw-r--r--   0        0        0        0 2022-10-22 17:52:58.366532 textual-0.9.1/src/textual/css/__init__.py
+-rw-r--r--   0        0        0      798 2022-10-22 17:52:58.366646 textual-0.9.1/src/textual/css/_error_tools.py
+-rw-r--r--   0        0        0     2751 2022-10-22 17:52:58.366876 textual-0.9.1/src/textual/css/_help_renderables.py
+-rw-r--r--   0        0        0    27657 2022-11-07 12:01:46.731547 textual-0.9.1/src/textual/css/_help_text.py
+-rw-r--r--   0        0        0    34929 2022-12-21 14:45:18.993236 textual-0.9.1/src/textual/css/_style_properties.py
+-rw-r--r--   0        0        0    36243 2022-11-07 12:01:46.679887 textual-0.9.1/src/textual/css/_styles_builder.py
+-rw-r--r--   0        0        0     1213 2022-12-21 14:45:18.993659 textual-0.9.1/src/textual/css/constants.py
+-rw-r--r--   0        0        0     1287 2022-10-22 17:52:58.367863 textual-0.9.1/src/textual/css/errors.py
+-rw-r--r--   0        0        0     2456 2022-12-21 14:46:04.899822 textual-0.9.1/src/textual/css/match.py
+-rw-r--r--   0        0        0     7078 2022-10-31 15:40:23.860640 textual-0.9.1/src/textual/css/model.py
+-rw-r--r--   0        0        0    12990 2022-12-10 11:00:36.089131 textual-0.9.1/src/textual/css/parse.py
+-rw-r--r--   0        0        0    12095 2022-12-16 09:08:40.131038 textual-0.9.1/src/textual/css/query.py
+-rw-r--r--   0        0        0    10355 2022-11-18 16:13:22.300441 textual-0.9.1/src/textual/css/scalar.py
+-rw-r--r--   0        0        0     2388 2022-11-12 16:59:33.627539 textual-0.9.1/src/textual/css/scalar_animation.py
+-rw-r--r--   0        0        0    35806 2022-12-21 16:18:26.893263 textual-0.9.1/src/textual/css/styles.py
+-rw-r--r--   0        0        0    18616 2022-12-21 14:46:04.900301 textual-0.9.1/src/textual/css/stylesheet.py
+-rw-r--r--   0        0        0     6486 2022-11-26 12:51:25.661742 textual-0.9.1/src/textual/css/tokenize.py
+-rw-r--r--   0        0        0     7529 2022-10-22 17:52:58.369493 textual-0.9.1/src/textual/css/tokenizer.py
+-rw-r--r--   0        0        0      417 2022-10-22 17:52:58.369557 textual-0.9.1/src/textual/css/transition.py
+-rw-r--r--   0        0        0      988 2022-11-07 12:01:46.488961 textual-0.9.1/src/textual/css/types.py
+-rw-r--r--   0        0        0     3586 2022-12-23 09:16:11.111009 textual-0.9.1/src/textual/demo.css
+-rw-r--r--   0        0        0    11417 2022-12-25 13:32:38.729066 textual-0.9.1/src/textual/demo.py
+-rw-r--r--   0        0        0     7096 2022-12-18 09:59:12.659903 textual-0.9.1/src/textual/design.py
+-rw-r--r--   0        0        0        0 2022-10-26 10:00:42.153340 textual-0.9.1/src/textual/devtools/__init__.py
+-rw-r--r--   0        0        0     9735 2022-10-26 10:00:42.153668 textual-0.9.1/src/textual/devtools/client.py
+-rw-r--r--   0        0        0     4210 2022-10-26 10:00:42.160137 textual-0.9.1/src/textual/devtools/redirect_output.py
+-rw-r--r--   0        0        0     4303 2022-11-07 12:01:46.489263 textual-0.9.1/src/textual/devtools/renderables.py
+-rw-r--r--   0        0        0     2282 2022-10-26 10:00:42.160414 textual-0.9.1/src/textual/devtools/server.py
+-rw-r--r--   0        0        0    11081 2022-10-26 10:00:42.160582 textual-0.9.1/src/textual/devtools/service.py
+-rw-r--r--   0        0        0    27716 2022-12-26 17:35:30.358741 textual-0.9.1/src/textual/dom.py
+-rw-r--r--   0        0        0     1665 2022-10-31 13:53:45.695176 textual-0.9.1/src/textual/driver.py
+-rw-r--r--   0        0        0        0 2022-02-27 15:19:02.514106 textual-0.9.1/src/textual/drivers/__init__.py
+-rw-r--r--   0        0        0     1457 2022-10-31 13:53:45.695538 textual-0.9.1/src/textual/drivers/headless_driver.py
+-rw-r--r--   0        0        0     7681 2022-12-21 16:52:10.014442 textual-0.9.1/src/textual/drivers/linux_driver.py
+-rw-r--r--   0        0        0     9302 2022-10-22 17:52:58.372798 textual-0.9.1/src/textual/drivers/win32.py
+-rw-r--r--   0        0        0     3049 2022-11-23 13:27:56.783298 textual-0.9.1/src/textual/drivers/windows_driver.py
+-rw-r--r--   0        0        0      424 2022-10-22 17:52:58.373018 textual-0.9.1/src/textual/errors.py
+-rw-r--r--   0        0        0    14018 2022-12-21 16:18:26.894317 textual-0.9.1/src/textual/events.py
+-rw-r--r--   0        0        0      659 2022-11-07 12:01:46.489777 textual-0.9.1/src/textual/features.py
+-rw-r--r--   0        0        0     1175 2022-11-07 12:01:46.473300 textual-0.9.1/src/textual/file_monitor.py
+-rw-r--r--   0        0        0    30494 2022-12-21 14:45:18.995884 textual-0.9.1/src/textual/geometry.py
+-rw-r--r--   0        0        0     7187 2022-12-25 13:32:53.002814 textual-0.9.1/src/textual/keys.py
+-rw-r--r--   0        0        0        0 2022-02-27 15:19:02.514972 textual-0.9.1/src/textual/layouts/__init__.py
+-rw-r--r--   0        0        0      769 2022-10-22 17:52:58.374570 textual-0.9.1/src/textual/layouts/factory.py
+-rw-r--r--   0        0        0     5529 2022-10-31 13:53:45.696732 textual-0.9.1/src/textual/layouts/grid.py
+-rw-r--r--   0        0        0     2061 2022-12-08 15:40:02.414653 textual-0.9.1/src/textual/layouts/horizontal.py
+-rw-r--r--   0        0        0     1694 2022-11-24 09:23:17.766068 textual-0.9.1/src/textual/layouts/vertical.py
+-rw-r--r--   0        0        0     3550 2022-12-21 16:18:26.895096 textual-0.9.1/src/textual/message.py
+-rw-r--r--   0        0        0    21677 2022-12-21 16:18:26.895399 textual-0.9.1/src/textual/message_pump.py
+-rw-r--r--   0        0        0     2483 2022-10-31 13:53:45.698521 textual-0.9.1/src/textual/messages.py
+-rw-r--r--   0        0        0     1382 2022-11-12 16:59:33.628215 textual-0.9.1/src/textual/pilot.py
+-rw-r--r--   0        0        0        0 2022-10-06 12:43:36.712808 textual-0.9.1/src/textual/py.typed
+-rw-r--r--   0        0        0    12334 2022-12-26 17:29:08.654476 textual-0.9.1/src/textual/reactive.py
+-rw-r--r--   0        0        0      743 2022-10-22 17:52:58.375413 textual-0.9.1/src/textual/render.py
+-rw-r--r--   0        0        0        0 2022-10-22 17:52:58.375450 textual-0.9.1/src/textual/renderables/__init__.py
+-rw-r--r--   0        0        0     1330 2022-10-22 17:52:58.375547 textual-0.9.1/src/textual/renderables/_blend_colors.py
+-rw-r--r--   0        0        0     1662 2022-10-22 17:52:58.375605 textual-0.9.1/src/textual/renderables/align.py
+-rw-r--r--   0        0        0      779 2022-11-18 16:13:22.302833 textual-0.9.1/src/textual/renderables/blank.py
+-rw-r--r--   0        0        0     1150 2022-11-18 16:13:22.302970 textual-0.9.1/src/textual/renderables/gradient.py
+-rw-r--r--   0        0        0     3844 2022-10-22 17:52:58.376095 textual-0.9.1/src/textual/renderables/sparkline.py
+-rw-r--r--   0        0        0     3661 2022-10-22 17:52:58.376163 textual-0.9.1/src/textual/renderables/text_opacity.py
+-rw-r--r--   0        0        0     2340 2022-10-22 17:52:58.376232 textual-0.9.1/src/textual/renderables/tint.py
+-rw-r--r--   0        0        0     4565 2022-10-22 17:52:58.376320 textual-0.9.1/src/textual/renderables/underline_bar.py
+-rw-r--r--   0        0        0    17542 2022-10-22 17:52:58.376482 textual-0.9.1/src/textual/richreadme.md
+-rw-r--r--   0        0        0    17955 2022-12-29 17:29:48.715354 textual-0.9.1/src/textual/screen.py
+-rw-r--r--   0        0        0     3073 2022-12-30 09:40:38.840844 textual-0.9.1/src/textual/scroll_view.py
+-rw-r--r--   0        0        0    10441 2022-12-11 13:20:31.269123 textual-0.9.1/src/textual/scrollbar.py
+-rw-r--r--   0        0        0     9408 2022-12-30 09:40:38.841062 textual-0.9.1/src/textual/strip.py
+-rw-r--r--   0        0        0     1482 2022-10-22 17:52:58.377130 textual-0.9.1/src/textual/suggestions.py
+-rw-r--r--   0        0        0     5533 2022-12-30 09:40:38.841318 textual-0.9.1/src/textual/timer.py
+-rw-r--r--   0        0        0     3455 2022-11-18 16:13:22.303686 textual-0.9.1/src/textual/walk.py
+-rw-r--r--   0        0        0    84762 2022-12-30 09:40:38.841937 textual-0.9.1/src/textual/widget.py
+-rw-r--r--   0        0        0     1939 2022-12-09 10:29:05.488921 textual-0.9.1/src/textual/widgets/__init__.py
+-rw-r--r--   0        0        0      806 2022-12-09 10:29:05.489061 textual-0.9.1/src/textual/widgets/__init__.pyi
+-rw-r--r--   0        0        0    10096 2022-12-13 09:54:36.939142 textual-0.9.1/src/textual/widgets/_button.py
+-rw-r--r--   0        0        0     3782 2022-12-13 09:54:36.939396 textual-0.9.1/src/textual/widgets/_checkbox.py
+-rw-r--r--   0        0        0    21230 2022-12-30 09:40:38.842331 textual-0.9.1/src/textual/widgets/_data_table.py
+-rw-r--r--   0        0        0     5025 2022-12-28 11:00:37.785288 textual-0.9.1/src/textual/widgets/_directory_tree.py
+-rw-r--r--   0        0        0     4040 2022-12-20 13:19:32.723070 textual-0.9.1/src/textual/widgets/_footer.py
+-rw-r--r--   0        0        0     3085 2022-12-21 14:45:18.999329 textual-0.9.1/src/textual/widgets/_header.py
+-rw-r--r--   0        0        0    11435 2022-12-21 16:18:26.896036 textual-0.9.1/src/textual/widgets/_input.py
+-rw-r--r--   0        0        0      305 2022-12-07 13:52:34.359242 textual-0.9.1/src/textual/widgets/_label.py
+-rw-r--r--   0        0        0      980 2022-12-09 10:29:05.489160 textual-0.9.1/src/textual/widgets/_list_item.py
+-rw-r--r--   0        0        0     5748 2022-12-13 09:54:36.939740 textual-0.9.1/src/textual/widgets/_list_view.py
+-rw-r--r--   0        0        0     6488 2022-12-11 13:20:31.270304 textual-0.9.1/src/textual/widgets/_placeholder.py
+-rw-r--r--   0        0        0      778 2022-10-22 17:52:58.379703 textual-0.9.1/src/textual/widgets/_pretty.py
+-rw-r--r--   0        0        0     3173 2022-12-21 14:45:18.999914 textual-0.9.1/src/textual/widgets/_static.py
+-rw-r--r--   0        0        0     5718 2022-12-30 09:40:38.842942 textual-0.9.1/src/textual/widgets/_text_log.py
+-rw-r--r--   0        0        0    26601 2022-12-30 09:40:38.843460 textual-0.9.1/src/textual/widgets/_tree.py
+-rw-r--r--   0        0        0       40 2022-11-23 13:27:56.784859 textual-0.9.1/src/textual/widgets/_tree_node.py
+-rw-r--r--   0        0        0     1287 2022-10-22 17:52:58.380149 textual-0.9.1/src/textual/widgets/_welcome.py
+-rw-r--r--   0        0        0    13381 2022-11-18 16:13:22.305628 textual-0.9.1/src/textual/widgets/tabs.py
+-rw-r--r--   0        0        0     5061 1970-01-01 00:00:00.000000 textual-0.9.1/setup.py
+-rw-r--r--   0        0        0     5299 1970-01-01 00:00:00.000000 textual-0.9.1/PKG-INFO
```

### Comparing `textual-0.9.0/LICENSE` & `textual-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/README.md` & `textual-0.9.1/README.md`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/pyproject.toml` & `textual-0.9.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "textual"
-version = "0.9.0"
+version = "0.9.1"
 homepage = "https://github.com/Textualize/textual"
 description = "Modern Text User Interface framework"
 authors = ["Will McGugan <will@textualize.io>"]
 license = "MIT"
 readme = "README.md"
 classifiers = [
     "Development Status :: 4 - Beta",
```

### Comparing `textual-0.9.0/src/textual/__init__.py` & `textual-0.9.1/src/textual/__init__.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_animator.py` & `textual-0.9.1/src/textual/_animator.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_ansi_sequences.py` & `textual-0.9.1/src/textual/_ansi_sequences.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_arrange.py` & `textual-0.9.1/src/textual/_arrange.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_border.py` & `textual-0.9.1/src/textual/_border.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_cache.py` & `textual-0.9.1/src/textual/_cache.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_callback.py` & `textual-0.9.1/src/textual/_callback.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_clock.py` & `textual-0.9.1/src/textual/_clock.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_color_constants.py` & `textual-0.9.1/src/textual/_color_constants.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_compositor.py` & `textual-0.9.1/src/textual/_compositor.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_doc.py` & `textual-0.9.1/src/textual/_doc.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_duration.py` & `textual-0.9.1/src/textual/_duration.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_easing.py` & `textual-0.9.1/src/textual/_easing.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_event_broker.py` & `textual-0.9.1/src/textual/_event_broker.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_filter.py` & `textual-0.9.1/src/textual/_filter.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_import_app.py` & `textual-0.9.1/src/textual/_import_app.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_layout.py` & `textual-0.9.1/src/textual/_layout.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_layout_resolve.py` & `textual-0.9.1/src/textual/_layout_resolve.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_loop.py` & `textual-0.9.1/src/textual/_loop.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_node_list.py` & `textual-0.9.1/src/textual/_node_list.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_opacity.py` & `textual-0.9.1/src/textual/_opacity.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_parser.py` & `textual-0.9.1/src/textual/_parser.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_partition.py` & `textual-0.9.1/src/textual/_partition.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_path.py` & `textual-0.9.1/src/textual/_path.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_resolve.py` & `textual-0.9.1/src/textual/_resolve.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_segment_tools.py` & `textual-0.9.1/src/textual/_segment_tools.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_sleep.py` & `textual-0.9.1/src/textual/_sleep.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_styles_cache.py` & `textual-0.9.1/src/textual/_styles_cache.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_text_backend.py` & `textual-0.9.1/src/textual/_text_backend.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_time.py` & `textual-0.9.1/src/textual/_time.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import platform
+import sys
 
 from asyncio import sleep as asyncio_sleep, get_running_loop
 from time import monotonic, perf_counter, sleep as time_sleep
 
 
 PLATFORM = platform.system()
 WINDOWS = PLATFORM == "Windows"
@@ -12,19 +13,27 @@
     time = perf_counter
 else:
     time = monotonic
 
 
 if WINDOWS:
 
-    async def sleep(sleep_for: float) -> None:
-        """An asyncio sleep.
+    if sys.version_info >= (3, 11, 0):
 
-        On Windows this achieves a better granularity that asyncio.sleep
+        async def sleep(sleep_for: float) -> None:
+            """An asyncio sleep.
 
-        Args:
-            sleep_for (float): Seconds to sleep for.
-        """
-        await get_running_loop().run_in_executor(None, time_sleep, sleep_for)
+            On Windows this achieves a better granularity that asyncio.sleep
+
+            Args:
+                sleep_for (float): Seconds to sleep for.
+            """
+            await get_running_loop().run_in_executor(None, time_sleep, sleep_for)
+
+    else:
+        from ._win_sleep import sleep as win_sleep
+
+        async def sleep(sleep_for: float) -> None:
+            await get_running_loop().run_in_executor(None, win_sleep, sleep_for)
 
 else:
     sleep = asyncio_sleep
```

### Comparing `textual-0.9.0/src/textual/_types.py` & `textual-0.9.1/src/textual/_types.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/_xterm_parser.py` & `textual-0.9.1/src/textual/_xterm_parser.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/actions.py` & `textual-0.9.1/src/textual/actions.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/app.py` & `textual-0.9.1/src/textual/app.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/await_remove.py` & `textual-0.9.1/src/textual/await_remove.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/binding.py` & `textual-0.9.1/src/textual/binding.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/box_model.py` & `textual-0.9.1/src/textual/box_model.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/case.py` & `textual-0.9.1/src/textual/case.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/cli/cli.py` & `textual-0.9.1/src/textual/cli/cli.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/cli/previews/borders.py` & `textual-0.9.1/src/textual/cli/previews/borders.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/cli/previews/colors.css` & `textual-0.9.1/src/textual/cli/previews/colors.css`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/cli/previews/colors.py` & `textual-0.9.1/src/textual/cli/previews/colors.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/cli/previews/easing.css` & `textual-0.9.1/src/textual/cli/previews/easing.css`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/cli/previews/easing.py` & `textual-0.9.1/src/textual/cli/previews/easing.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/cli/previews/keys.py` & `textual-0.9.1/src/textual/cli/previews/keys.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/color.py` & `textual-0.9.1/src/textual/color.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/containers.py` & `textual-0.9.1/src/textual/containers.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/_error_tools.py` & `textual-0.9.1/src/textual/css/_error_tools.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/_help_renderables.py` & `textual-0.9.1/src/textual/css/_help_renderables.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/_help_text.py` & `textual-0.9.1/src/textual/css/_help_text.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/_style_properties.py` & `textual-0.9.1/src/textual/css/_style_properties.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/_styles_builder.py` & `textual-0.9.1/src/textual/css/_styles_builder.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/constants.py` & `textual-0.9.1/src/textual/css/constants.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/errors.py` & `textual-0.9.1/src/textual/css/errors.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/match.py` & `textual-0.9.1/src/textual/css/match.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/model.py` & `textual-0.9.1/src/textual/css/model.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/parse.py` & `textual-0.9.1/src/textual/css/parse.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/query.py` & `textual-0.9.1/src/textual/css/query.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/scalar.py` & `textual-0.9.1/src/textual/css/scalar.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/scalar_animation.py` & `textual-0.9.1/src/textual/css/scalar_animation.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/styles.py` & `textual-0.9.1/src/textual/css/styles.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/stylesheet.py` & `textual-0.9.1/src/textual/css/stylesheet.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/tokenize.py` & `textual-0.9.1/src/textual/css/tokenize.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/tokenizer.py` & `textual-0.9.1/src/textual/css/tokenizer.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/css/types.py` & `textual-0.9.1/src/textual/css/types.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/demo.css` & `textual-0.9.1/src/textual/demo.css`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/demo.py` & `textual-0.9.1/src/textual/demo.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/design.py` & `textual-0.9.1/src/textual/design.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/devtools/client.py` & `textual-0.9.1/src/textual/devtools/client.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/devtools/redirect_output.py` & `textual-0.9.1/src/textual/devtools/redirect_output.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/devtools/renderables.py` & `textual-0.9.1/src/textual/devtools/renderables.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/devtools/server.py` & `textual-0.9.1/src/textual/devtools/server.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/devtools/service.py` & `textual-0.9.1/src/textual/devtools/service.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/dom.py` & `textual-0.9.1/src/textual/dom.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/driver.py` & `textual-0.9.1/src/textual/driver.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/drivers/headless_driver.py` & `textual-0.9.1/src/textual/drivers/headless_driver.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/drivers/linux_driver.py` & `textual-0.9.1/src/textual/drivers/linux_driver.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/drivers/win32.py` & `textual-0.9.1/src/textual/drivers/win32.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/drivers/windows_driver.py` & `textual-0.9.1/src/textual/drivers/windows_driver.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/events.py` & `textual-0.9.1/src/textual/events.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/features.py` & `textual-0.9.1/src/textual/features.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/file_monitor.py` & `textual-0.9.1/src/textual/file_monitor.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/geometry.py` & `textual-0.9.1/src/textual/geometry.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/keys.py` & `textual-0.9.1/src/textual/keys.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/layouts/factory.py` & `textual-0.9.1/src/textual/layouts/factory.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/layouts/grid.py` & `textual-0.9.1/src/textual/layouts/grid.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/layouts/horizontal.py` & `textual-0.9.1/src/textual/layouts/horizontal.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/layouts/vertical.py` & `textual-0.9.1/src/textual/layouts/vertical.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/message.py` & `textual-0.9.1/src/textual/message.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/message_pump.py` & `textual-0.9.1/src/textual/message_pump.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/messages.py` & `textual-0.9.1/src/textual/messages.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/pilot.py` & `textual-0.9.1/src/textual/pilot.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/reactive.py` & `textual-0.9.1/src/textual/reactive.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/render.py` & `textual-0.9.1/src/textual/render.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/_blend_colors.py` & `textual-0.9.1/src/textual/renderables/_blend_colors.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/align.py` & `textual-0.9.1/src/textual/renderables/align.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/blank.py` & `textual-0.9.1/src/textual/renderables/blank.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/gradient.py` & `textual-0.9.1/src/textual/renderables/gradient.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/sparkline.py` & `textual-0.9.1/src/textual/renderables/sparkline.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/text_opacity.py` & `textual-0.9.1/src/textual/renderables/text_opacity.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/tint.py` & `textual-0.9.1/src/textual/renderables/tint.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/renderables/underline_bar.py` & `textual-0.9.1/src/textual/renderables/underline_bar.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/richreadme.md` & `textual-0.9.1/src/textual/richreadme.md`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/screen.py` & `textual-0.9.1/src/textual/screen.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/scroll_view.py` & `textual-0.9.1/src/textual/scroll_view.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/scrollbar.py` & `textual-0.9.1/src/textual/scrollbar.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/strip.py` & `textual-0.9.1/src/textual/strip.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/suggestions.py` & `textual-0.9.1/src/textual/suggestions.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/timer.py` & `textual-0.9.1/src/textual/timer.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/walk.py` & `textual-0.9.1/src/textual/walk.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widget.py` & `textual-0.9.1/src/textual/widget.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/__init__.py` & `textual-0.9.1/src/textual/widgets/__init__.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/__init__.pyi` & `textual-0.9.1/src/textual/widgets/__init__.pyi`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_button.py` & `textual-0.9.1/src/textual/widgets/_button.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_checkbox.py` & `textual-0.9.1/src/textual/widgets/_checkbox.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_data_table.py` & `textual-0.9.1/src/textual/widgets/_data_table.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_directory_tree.py` & `textual-0.9.1/src/textual/widgets/_directory_tree.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_footer.py` & `textual-0.9.1/src/textual/widgets/_footer.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_header.py` & `textual-0.9.1/src/textual/widgets/_header.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_input.py` & `textual-0.9.1/src/textual/widgets/_input.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_list_item.py` & `textual-0.9.1/src/textual/widgets/_list_item.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_list_view.py` & `textual-0.9.1/src/textual/widgets/_list_view.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_placeholder.py` & `textual-0.9.1/src/textual/widgets/_placeholder.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_pretty.py` & `textual-0.9.1/src/textual/widgets/_pretty.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_static.py` & `textual-0.9.1/src/textual/widgets/_static.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_text_log.py` & `textual-0.9.1/src/textual/widgets/_text_log.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_tree.py` & `textual-0.9.1/src/textual/widgets/_tree.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/_welcome.py` & `textual-0.9.1/src/textual/widgets/_welcome.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/src/textual/widgets/tabs.py` & `textual-0.9.1/src/textual/widgets/tabs.py`

 * *Files identical despite different names*

### Comparing `textual-0.9.0/setup.py` & `textual-0.9.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,15 +26,15 @@
  'dev': ['aiohttp>=3.8.1', 'click>=8.1.2', 'msgpack>=1.0.3']}
 
 entry_points = \
 {'console_scripts': ['textual = textual.cli.cli:run']}
 
 setup_kwargs = {
     'name': 'textual',
-    'version': '0.9.0',
+    'version': '0.9.1',
     'description': 'Modern Text User Interface framework',
     'long_description': '# Textual\n\n![Textual splash image](https://raw.githubusercontent.com/Textualize/textual/main/imgs/textual.png)\n\nTextual is a Python framework for creating interactive applications that run in your terminal.\n\n<details>  \n  <summary> 🎬 Demonstration </summary>\n  <hr>\n  \nA quick run through of some Textual features.\n  \n\n\nhttps://user-images.githubusercontent.com/554369/197355913-65d3c125-493d-4c05-a590-5311f16c40ff.mov\n\n\n\n </details>\n\n\n\n## About\n\nTextual adds interactivity to [Rich](https://github.com/Textualize/rich) with a Python API inspired by modern web development.\n\nOn modern terminal software (installed by default on most systems), Textual apps can use **16.7 million** colors with mouse support and smooth flicker-free animation. A powerful layout engine and re-usable components makes it possible to build apps that rival the desktop and web experience. \n\n## Compatibility\n\nTextual runs on Linux, macOS, and Windows. Textual requires Python 3.7 or above.\n\n## Installing\n\nInstall Textual via pip:\n\n```\npip install "textual[dev]"\n```\n\nThe addition of `[dev]` installs Textual development tools. See the [docs](https://textual.textualize.io/getting_started/) if you need help getting started.\n\n## Demo\n\nRun the following command to see a little of what Textual can do:\n\n```\npython -m textual\n```\n\n![Textual demo](https://raw.githubusercontent.com/Textualize/textual/main/imgs/demo.png)\n\n## Documentation\n\nHead over to the [Textual documentation](http://textual.textualize.io/) to start building!\n\n## Examples\n\nThe Textual repository comes with a number of examples you can experiment with or use as a template for your own projects.\n\n\n<details>\n  <summary> 🎬 Code browser </summary>\n  <hr>\n\n  This is the [code_browser.py](https://github.com/Textualize/textual/blob/main/examples/code_browser.py) example which clocks in at 61 lines (*including* docstrings and blank lines).\n\nhttps://user-images.githubusercontent.com/554369/197188237-88d3f7e4-4e5f-40b5-b996-c47b19ee2f49.mov\n\n </details>\n\n\n<details>  \n  <summary> 📷 Calculator </summary>\n  <hr>\n  \nThis is [calculator.py](https://github.com/Textualize/textual/blob/main/examples/calculator.py) which demonstrates Textual grid layouts.\n  \n![calculator screenshot](https://raw.githubusercontent.com/Textualize/textual/main/imgs/calculator.png)\n</details>\n\n\n<details>\n  <summary> 🎬 Stopwatch </summary>\n  <hr>\n\n  This is the Stopwatch example from the [tutorial](https://textual.textualize.io/tutorial/).\n  \n\n\nhttps://user-images.githubusercontent.com/554369/197360718-0c834ef5-6285-4d37-85cf-23eed4aa56c5.mov\n\n\n\n</details>\n\n\n\n## Reference commands\n\nThe `textual` command has a few sub-commands to preview Textual styles.\n\n<details>  \n  <summary> 🎬 Easing reference </summary>\n  <hr>\n  \nThis is the *easing* reference which demonstrates the easing parameter on animation, with both movement and opacity. You can run it with the following command:\n  \n```bash\ntextual easing\n```\n\n\nhttps://user-images.githubusercontent.com/554369/196157100-352852a6-2b09-4dc8-a888-55b53570aff9.mov\n\n\n </details>\n\n<details>  \n  <summary> 🎬 Borders reference </summary>\n  <hr>\n  \nThis is the borders reference which demonstrates some of the borders styles in Textual. You can run it with the following command:\n  \n```bash\ntextual borders\n```\n\n\nhttps://user-images.githubusercontent.com/554369/196158235-4b45fb78-053d-4fd5-b285-e09b4f1c67a8.mov\n\n  \n</details>\n\n\n<details>  \n  <summary> 🎬 Colors reference </summary>\n  <hr>\n  \nThis is a reference for Textual\'s color design system.\n  \n```bash\ntextual colors\n```\n\n\n\nhttps://user-images.githubusercontent.com/554369/197357417-2d407aac-8969-44d3-8250-eea45df79d57.mov\n\n\n\n  \n</details>\n\n',
     'author': 'Will McGugan',
     'author_email': 'will@textualize.io',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/Textualize/textual',
```

### Comparing `textual-0.9.0/PKG-INFO` & `textual-0.9.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: textual
-Version: 0.9.0
+Version: 0.9.1
 Summary: Modern Text User Interface framework
 Home-page: https://github.com/Textualize/textual
 License: MIT
 Author: Will McGugan
 Author-email: will@textualize.io
 Requires-Python: >=3.7,<4.0
 Classifier: Development Status :: 4 - Beta
```

