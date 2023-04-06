# Comparing `tmp/manim-0.8.0.tar.gz` & `tmp/manim-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "manim-0.8.0.tar", max compression
+gzip compressed data, was "manim-0.9.0.tar", max compression
```

## Comparing `manim-0.8.0.tar` & `manim-0.9.0.tar`

### file list

```diff
@@ -1,207 +1,209 @@
--rw-r--r--   0        0        0     1072 2021-07-02 15:09:00.440911 manim-0.8.0/LICENSE
--rw-r--r--   0        0        0     1088 2021-07-02 15:09:00.440911 manim-0.8.0/LICENSE.community
--rw-r--r--   0        0        0    10089 2021-07-02 15:09:00.440911 manim-0.8.0/README.md
--rw-r--r--   0        0        0     3835 2021-07-02 15:09:00.448911 manim-0.8.0/manim/__init__.py
--rw-r--r--   0        0        0     1013 2021-07-02 15:09:00.448911 manim-0.8.0/manim/__main__.py
--rw-r--r--   0        0        0     2518 2021-07-02 15:09:00.448911 manim-0.8.0/manim/_config/__init__.py
--rw-r--r--   0        0        0     4509 2021-07-02 15:09:00.448911 manim-0.8.0/manim/_config/default.cfg
--rw-r--r--   0        0        0     5868 2021-07-02 15:09:00.448911 manim-0.8.0/manim/_config/logger_utils.py
--rw-r--r--   0        0        0    52768 2021-07-02 15:09:00.448911 manim-0.8.0/manim/_config/utils.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/__init__.py
--rw-r--r--   0        0        0    15844 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/animation.py
--rw-r--r--   0        0        0     6632 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/composition.py
--rw-r--r--   0        0        0    14978 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/creation.py
--rw-r--r--   0        0        0     8374 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/fading.py
--rw-r--r--   0        0        0     2058 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/growing.py
--rw-r--r--   0        0        0    25160 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/indication.py
--rw-r--r--   0        0        0     4184 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/movement.py
--rw-r--r--   0        0        0     1593 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/numbers.py
--rw-r--r--   0        0        0     2163 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/rotation.py
--rw-r--r--   0        0        0    19581 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/transform.py
--rw-r--r--   0        0        0     9718 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/transform_matching_parts.py
--rw-r--r--   0        0        0     1680 2021-07-02 15:09:00.448911 manim-0.8.0/manim/animation/update.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/camera/__init__.py
--rw-r--r--   0        0        0    43514 2021-07-02 15:09:00.448911 manim-0.8.0/manim/camera/camera.py
--rw-r--r--   0        0        0     5019 2021-07-02 15:09:00.448911 manim-0.8.0/manim/camera/mapping_camera.py
--rw-r--r--   0        0        0     4934 2021-07-02 15:09:00.448911 manim-0.8.0/manim/camera/moving_camera.py
--rw-r--r--   0        0        0     3309 2021-07-02 15:09:00.448911 manim-0.8.0/manim/camera/multi_camera.py
--rw-r--r--   0        0        0    13926 2021-07-02 15:09:00.448911 manim-0.8.0/manim/camera/three_d_camera.py
--rw-r--r--   0        0        0     1076 2021-07-02 15:09:00.448911 manim-0.8.0/manim/camera/webgl_camera.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/__init__.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/cfg/__init__.py
--rw-r--r--   0        0        0     9658 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/cfg/group.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/init/__init__.py
--rw-r--r--   0        0        0      796 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/init/commands.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/new/__init__.py
--rw-r--r--   0        0        0     5721 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/new/group.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/plugins/__init__.py
--rw-r--r--   0        0        0      633 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/plugins/commands.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/render/__init__.py
--rw-r--r--   0        0        0     5543 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/render/commands.py
--rw-r--r--   0        0        0      890 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/render/ease_of_access_options.py
--rw-r--r--   0        0        0     1907 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/render/global_options.py
--rw-r--r--   0        0        0      690 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/render/output_options.py
--rw-r--r--   0        0        0     3577 2021-07-02 15:09:00.448911 manim-0.8.0/manim/cli/render/render_options.py
--rw-r--r--   0        0        0      151 2021-07-02 15:09:00.448911 manim-0.8.0/manim/communitycolors.py
--rw-r--r--   0        0        0     6604 2021-07-02 15:09:00.448911 manim-0.8.0/manim/constants.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/__init__.py
--rw-r--r--   0        0        0      163 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/gen/__init__.py
--rw-r--r--   0        0        0    52283 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/gen/frameserver_pb2.py
--rw-r--r--   0        0        0     5744 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/gen/frameserver_pb2_grpc.py
--rw-r--r--   0        0        0    11419 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/gen/renderserver_pb2.py
--rw-r--r--   0        0        0     2587 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/gen/renderserver_pb2_grpc.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/impl/__init__.py
--rw-r--r--   0        0        0    17007 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/impl/frame_server_impl.py
--rw-r--r--   0        0        0     2551 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/proto/frameserver.proto
--rw-r--r--   0        0        0      546 2021-07-02 15:09:00.448911 manim-0.8.0/manim/grpc/proto/renderserver.proto
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/gui/__init__.py
--rw-r--r--   0        0        0     2586 2021-07-02 15:09:00.448911 manim-0.8.0/manim/gui/gui.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.448911 manim-0.8.0/manim/mobject/__init__.py
--rw-r--r--   0        0        0     4863 2021-07-02 15:09:00.448911 manim-0.8.0/manim/mobject/changing.py
--rw-r--r--   0        0        0    71378 2021-07-02 15:09:00.448911 manim-0.8.0/manim/mobject/coordinate_systems.py
--rw-r--r--   0        0        0     1834 2021-07-02 15:09:00.448911 manim-0.8.0/manim/mobject/frame.py
--rw-r--r--   0        0        0     4689 2021-07-02 15:09:00.448911 manim-0.8.0/manim/mobject/functions.py
--rw-r--r--   0        0        0    98975 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/geometry.py
--rw-r--r--   0        0        0    33327 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/graph.py
--rw-r--r--   0        0        0     9068 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/logo.py
--rw-r--r--   0        0        0    18802 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/matrix.py
--rw-r--r--   0        0        0    91319 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/mobject.py
--rw-r--r--   0        0        0     2830 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/mobject_update_utils.py
--rw-r--r--   0        0        0    20564 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/number_line.py
--rw-r--r--   0        0        0    12406 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/numbers.py
--rw-r--r--   0        0        0     1099 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/opengl_compatibility.py
--rw-r--r--   0        0        0    27335 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/opengl_geometry.py
--rw-r--r--   0        0        0    57157 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/opengl_mobject.py
--rw-r--r--   0        0        0     2865 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/opengl_three_dimensions.py
--rw-r--r--   0        0        0    12505 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/polyhedra.py
--rw-r--r--   0        0        0    10928 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/probability.py
--rw-r--r--   0        0        0     4431 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/shape_matchers.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/__init__.py
--rw-r--r--   0        0        0    11296 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/brace.py
--rw-r--r--   0        0        0    23222 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/code_mobject.py
--rw-r--r--   0        0        0     1459 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/opengl_svg_mobject.py
--rw-r--r--   0        0        0      821 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/opengl_svg_path.py
--rw-r--r--   0        0        0    20703 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/opengl_tex_mobject.py
--rw-r--r--   0        0        0    45106 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/opengl_text_mobject.py
--rw-r--r--   0        0        0     5761 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/style_utils.py
--rw-r--r--   0        0        0    20599 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/svg_mobject.py
--rw-r--r--   0        0        0    16917 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/svg_path.py
--rw-r--r--   0        0        0    17025 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/tex_mobject.py
--rw-r--r--   0        0        0    47946 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/svg/text_mobject.py
--rw-r--r--   0        0        0     1835 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/three_d_utils.py
--rw-r--r--   0        0        0    22148 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/three_dimensions.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/types/__init__.py
--rw-r--r--   0        0        0    11600 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/types/image_mobject.py
--rw-r--r--   0        0        0    10939 2021-07-02 15:09:00.452911 manim-0.8.0/manim/mobject/types/opengl_surface.py
--rw-r--r--   0        0        0    43125 2021-07-02 15:09:00.456911 manim-0.8.0/manim/mobject/types/opengl_vectorized_mobject.py
--rw-r--r--   0        0        0    10913 2021-07-02 15:09:00.456911 manim-0.8.0/manim/mobject/types/point_cloud_mobject.py
--rw-r--r--   0        0        0    71590 2021-07-02 15:09:00.456911 manim-0.8.0/manim/mobject/types/vectorized_mobject.py
--rw-r--r--   0        0        0     6319 2021-07-02 15:09:00.456911 manim-0.8.0/manim/mobject/value_tracker.py
--rw-r--r--   0        0        0    35170 2021-07-02 15:09:00.456911 manim-0.8.0/manim/mobject/vector_field.py
--rw-r--r--   0        0        0      504 2021-07-02 15:09:00.456911 manim-0.8.0/manim/opengl/__init__.py
--rw-r--r--   0        0        0       30 2021-07-02 15:09:00.456911 manim-0.8.0/manim/plugins/__init__.py
--rw-r--r--   0        0        0     1468 2021-07-02 15:09:00.456911 manim-0.8.0/manim/plugins/import_plugins.py
--rw-r--r--   0        0        0      513 2021-07-02 15:09:00.456911 manim-0.8.0/manim/plugins/plugins_flags.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/__init__.py
--rw-r--r--   0        0        0     9560 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/cairo_renderer.py
--rw-r--r--   0        0        0    16176 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/opengl_renderer.py
--rw-r--r--   0        0        0     4384 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/opengl_renderer_window.py
--rw-r--r--   0        0        0    14098 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shader.py
--rw-r--r--   0        0        0     5965 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shader_wrapper.py
--rw-r--r--   0        0        0       98 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/default/frag.glsl
--rw-r--r--   0        0        0      232 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/default/vert.glsl
--rw-r--r--   0        0        0      216 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/design.frag
--rw-r--r--   0        0        0      961 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/design_2.frag
--rw-r--r--   0        0        0     1301 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/design_3.frag
--rw-r--r--   0        0        0      200 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/image/frag.glsl
--rw-r--r--   0        0        0      459 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/image/vert.glsl
--rw-r--r--   0        0        0      583 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/NOTE.md
--rw-r--r--   0        0        0     1602 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/add_light.glsl
--rw-r--r--   0        0        0      179 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/camera_uniform_declarations.glsl
--rw-r--r--   0        0        0     1866 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/finalize_color.glsl
--rw-r--r--   0        0        0      998 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/get_gl_Position.glsl
--rw-r--r--   0        0        0      551 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/get_rotated_surface_unit_normal_vector.glsl
--rw-r--r--   0        0        0      773 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/get_unit_normal.glsl
--rw-r--r--   0        0        0      478 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/position_point_into_frame.glsl
--rw-r--r--   0        0        0     2856 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/quadratic_bezier_distance.glsl
--rw-r--r--   0        0        0     2747 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/include/quadratic_bezier_geometry_functions.glsl
--rw-r--r--   0        0        0      583 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/NOTE.md
--rw-r--r--   0        0        0     1602 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/add_light.glsl
--rw-r--r--   0        0        0      179 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/camera_uniform_declarations.glsl
--rw-r--r--   0        0        0     1866 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/finalize_color.glsl
--rw-r--r--   0        0        0      998 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/get_gl_Position.glsl
--rw-r--r--   0        0        0      551 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/get_rotated_surface_unit_normal_vector.glsl
--rw-r--r--   0        0        0      773 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/get_unit_normal.glsl
--rw-r--r--   0        0        0      478 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/position_point_into_frame.glsl
--rw-r--r--   0        0        0     2856 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/quadratic_bezier_distance.glsl
--rw-r--r--   0        0        0     2747 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/inserts/quadratic_bezier_geometry_functions.glsl
--rw-r--r--   0        0        0       98 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/manim_coords/frag.glsl
--rw-r--r--   0        0        0      287 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/manim_coords/vert.glsl
--rw-r--r--   0        0        0     1836 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/quadratic_bezier_fill/frag.glsl
--rw-r--r--   0        0        0     3470 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/quadratic_bezier_fill/geom.glsl
--rw-r--r--   0        0        0      523 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/quadratic_bezier_fill/vert.glsl
--rw-r--r--   0        0        0     2683 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/quadratic_bezier_stroke/frag.glsl
--rw-r--r--   0        0        0     8984 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/quadratic_bezier_stroke/geom.glsl
--rw-r--r--   0        0        0      743 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/quadratic_bezier_stroke/vert.glsl
--rw-r--r--   0        0        0      296 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/simple_vert.glsl
--rw-r--r--   0        0        0      396 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/surface/frag.glsl
--rw-r--r--   0        0        0      567 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/surface/vert.glsl
--rw-r--r--   0        0        0       96 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/test/frag.glsl
--rw-r--r--   0        0        0      152 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/test/vert.glsl
--rw-r--r--   0        0        0      956 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/textured_surface/frag.glsl
--rw-r--r--   0        0        0      647 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/textured_surface/vert.glsl
--rw-r--r--   0        0        0      761 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/true_dot/frag.glsl
--rw-r--r--   0        0        0      988 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/true_dot/geom.glsl
--rw-r--r--   0        0        0      332 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/true_dot/vert.glsl
--rw-r--r--   0        0        0      324 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/vectorized_mobject_fill/frag.glsl
--rw-r--r--   0        0        0      423 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/vectorized_mobject_fill/vert.glsl
--rw-r--r--   0        0        0     2737 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/vectorized_mobject_stroke/frag.glsl
--rw-r--r--   0        0        0     4434 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/vectorized_mobject_stroke/vert.glsl
--rw-r--r--   0        0        0       93 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/vertex_colors/frag.glsl
--rw-r--r--   0        0        0      281 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/shaders/vertex_colors/vert.glsl
--rw-r--r--   0        0        0     6951 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/vectorized_mobject_rendering.py
--rw-r--r--   0        0        0     1786 2021-07-02 15:09:00.456911 manim-0.8.0/manim/renderer/webgl_renderer.py
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/__init__.py
--rw-r--r--   0        0        0    40446 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/graph_scene.py
--rw-r--r--   0        0        0     3694 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/moving_camera_scene.py
--rw-r--r--   0        0        0     2072 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/reconfigurable_scene.py
--rw-r--r--   0        0        0     5191 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/sample_space_scene.py
--rw-r--r--   0        0        0    46956 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/scene.py
--rw-r--r--   0        0        0    21381 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/scene_file_writer.py
--rw-r--r--   0        0        0    14354 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/three_d_scene.py
--rw-r--r--   0        0        0    37603 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/vector_space_scene.py
--rw-r--r--   0        0        0     7028 2021-07-02 15:09:00.456911 manim-0.8.0/manim/scene/zoomed_scene.py
--rw-r--r--   0        0        0      312 2021-07-02 15:09:00.460911 manim-0.8.0/manim/templates/Axes.mtp
--rw-r--r--   0        0        0      547 2021-07-02 15:09:00.460911 manim-0.8.0/manim/templates/Default.mtp
--rw-r--r--   0        0        0      327 2021-07-02 15:09:00.460911 manim-0.8.0/manim/templates/MovingCamera.mtp
--rw-r--r--   0        0        0      134 2021-07-02 15:09:00.460911 manim-0.8.0/manim/templates/template.cfg
--rw-r--r--   0        0        0        0 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/__init__.py
--rw-r--r--   0        0        0    11321 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/bezier.py
--rw-r--r--   0        0        0     2598 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/caching.py
--rw-r--r--   0        0        0    11950 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/color.py
--rw-r--r--   0        0        0     1237 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/config_ops.py
--rw-r--r--   0        0        0      750 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/debug.py
--rw-r--r--   0        0        0    14580 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/deprecation.py
--rw-r--r--   0        0        0      160 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/exceptions.py
--rw-r--r--   0        0        0     1102 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/family.py
--rw-r--r--   0        0        0     1410 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/family_ops.py
--rw-r--r--   0        0        0     6785 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/file_ops.py
--rw-r--r--   0        0        0    12399 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/hashing.py
--rw-r--r--   0        0        0      817 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/images.py
--rw-r--r--   0        0        0     5610 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/ipython_magic.py
--rw-r--r--   0        0        0     4388 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/iterables.py
--rw-r--r--   0        0        0     4359 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/module_ops.py
--rw-r--r--   0        0        0     3283 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/opengl.py
--rw-r--r--   0        0        0     1554 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/paths.py
--rw-r--r--   0        0        0    11649 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/rate_functions.py
--rw-r--r--   0        0        0     2557 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/simple_functions.py
--rw-r--r--   0        0        0      439 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/sounds.py
--rw-r--r--   0        0        0    21255 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/space_ops.py
--rw-r--r--   0        0        0     2289 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/strings.py
--rw-r--r--   0        0        0    10094 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/tex.py
--rw-r--r--   0        0        0    10356 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/tex_file_writing.py
--rw-r--r--   0        0        0    28452 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/tex_templates.py
--rw-r--r--   0        0        0      905 2021-07-02 15:09:00.460911 manim-0.8.0/manim/utils/unit.py
--rw-r--r--   0        0        0     3231 2021-07-02 15:09:00.460911 manim-0.8.0/pyproject.toml
--rw-r--r--   0        0        0    12902 2021-07-02 15:09:12.344070 manim-0.8.0/setup.py
--rw-r--r--   0        0        0    12374 2021-07-02 15:09:12.344925 manim-0.8.0/PKG-INFO
+-rw-r--r--   0        0        0     1072 2021-08-02 10:25:53.783140 manim-0.9.0/LICENSE
+-rw-r--r--   0        0        0     1088 2021-08-02 10:25:53.783140 manim-0.9.0/LICENSE.community
+-rw-r--r--   0        0        0    10397 2021-08-02 10:25:53.783140 manim-0.9.0/README.md
+-rw-r--r--   0        0        0     3901 2021-08-02 10:25:53.791141 manim-0.9.0/manim/__init__.py
+-rw-r--r--   0        0        0     1013 2021-08-02 10:25:53.791141 manim-0.9.0/manim/__main__.py
+-rw-r--r--   0        0        0     2518 2021-08-02 10:25:53.791141 manim-0.9.0/manim/_config/__init__.py
+-rw-r--r--   0        0        0     4625 2021-08-02 10:25:53.791141 manim-0.9.0/manim/_config/default.cfg
+-rw-r--r--   0        0        0     5868 2021-08-02 10:25:53.791141 manim-0.9.0/manim/_config/logger_utils.py
+-rw-r--r--   0        0        0    53331 2021-08-02 10:25:53.791141 manim-0.9.0/manim/_config/utils.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/__init__.py
+-rw-r--r--   0        0        0    16203 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/animation.py
+-rw-r--r--   0        0        0     6705 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/composition.py
+-rw-r--r--   0        0        0    15329 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/creation.py
+-rw-r--r--   0        0        0     5811 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/fading.py
+-rw-r--r--   0        0        0     2058 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/growing.py
+-rw-r--r--   0        0        0    20968 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/indication.py
+-rw-r--r--   0        0        0     4184 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/movement.py
+-rw-r--r--   0        0        0     1593 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/numbers.py
+-rw-r--r--   0        0        0     2163 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/rotation.py
+-rw-r--r--   0        0        0     2886 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/specialized.py
+-rw-r--r--   0        0        0    19581 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/transform.py
+-rw-r--r--   0        0        0     9718 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/transform_matching_parts.py
+-rw-r--r--   0        0        0     1680 2021-08-02 10:25:53.791141 manim-0.9.0/manim/animation/update.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/camera/__init__.py
+-rw-r--r--   0        0        0    43514 2021-08-02 10:25:53.791141 manim-0.9.0/manim/camera/camera.py
+-rw-r--r--   0        0        0     5019 2021-08-02 10:25:53.791141 manim-0.9.0/manim/camera/mapping_camera.py
+-rw-r--r--   0        0        0     4934 2021-08-02 10:25:53.791141 manim-0.9.0/manim/camera/moving_camera.py
+-rw-r--r--   0        0        0     3309 2021-08-02 10:25:53.791141 manim-0.9.0/manim/camera/multi_camera.py
+-rw-r--r--   0        0        0    13893 2021-08-02 10:25:53.791141 manim-0.9.0/manim/camera/three_d_camera.py
+-rw-r--r--   0        0        0     1076 2021-08-02 10:25:53.791141 manim-0.9.0/manim/camera/webgl_camera.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/__init__.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/cfg/__init__.py
+-rw-r--r--   0        0        0     9658 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/cfg/group.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/init/__init__.py
+-rw-r--r--   0        0        0      796 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/init/commands.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/new/__init__.py
+-rw-r--r--   0        0        0     5721 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/new/group.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/plugins/__init__.py
+-rw-r--r--   0        0        0      633 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/plugins/commands.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/render/__init__.py
+-rw-r--r--   0        0        0     5543 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/render/commands.py
+-rw-r--r--   0        0        0      983 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/render/ease_of_access_options.py
+-rw-r--r--   0        0        0     2105 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/render/global_options.py
+-rw-r--r--   0        0        0      784 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/render/output_options.py
+-rw-r--r--   0        0        0     3837 2021-08-02 10:25:53.791141 manim-0.9.0/manim/cli/render/render_options.py
+-rw-r--r--   0        0        0      151 2021-08-02 10:25:53.791141 manim-0.9.0/manim/communitycolors.py
+-rw-r--r--   0        0        0     6604 2021-08-02 10:25:53.791141 manim-0.9.0/manim/constants.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.791141 manim-0.9.0/manim/grpc/__init__.py
+-rw-r--r--   0        0        0      163 2021-08-02 10:25:53.791141 manim-0.9.0/manim/grpc/gen/__init__.py
+-rw-r--r--   0        0        0    52283 2021-08-02 10:25:53.791141 manim-0.9.0/manim/grpc/gen/frameserver_pb2.py
+-rw-r--r--   0        0        0     5744 2021-08-02 10:25:53.795141 manim-0.9.0/manim/grpc/gen/frameserver_pb2_grpc.py
+-rw-r--r--   0        0        0    11419 2021-08-02 10:25:53.795141 manim-0.9.0/manim/grpc/gen/renderserver_pb2.py
+-rw-r--r--   0        0        0     2587 2021-08-02 10:25:53.795141 manim-0.9.0/manim/grpc/gen/renderserver_pb2_grpc.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.795141 manim-0.9.0/manim/grpc/impl/__init__.py
+-rw-r--r--   0        0        0    17007 2021-08-02 10:25:53.795141 manim-0.9.0/manim/grpc/impl/frame_server_impl.py
+-rw-r--r--   0        0        0     2551 2021-08-02 10:25:53.795141 manim-0.9.0/manim/grpc/proto/frameserver.proto
+-rw-r--r--   0        0        0      546 2021-08-02 10:25:53.795141 manim-0.9.0/manim/grpc/proto/renderserver.proto
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.795141 manim-0.9.0/manim/gui/__init__.py
+-rw-r--r--   0        0        0     2586 2021-08-02 10:25:53.795141 manim-0.9.0/manim/gui/gui.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/__init__.py
+-rw-r--r--   0        0        0     4863 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/changing.py
+-rw-r--r--   0        0        0    72208 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/coordinate_systems.py
+-rw-r--r--   0        0        0     1834 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/frame.py
+-rw-r--r--   0        0        0     4689 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/functions.py
+-rw-r--r--   0        0        0   100001 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/geometry.py
+-rw-r--r--   0        0        0    33327 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/graph.py
+-rw-r--r--   0        0        0     9068 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/logo.py
+-rw-r--r--   0        0        0    18802 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/matrix.py
+-rw-r--r--   0        0        0    92371 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/mobject.py
+-rw-r--r--   0        0        0     2830 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/mobject_update_utils.py
+-rw-r--r--   0        0        0    22105 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/number_line.py
+-rw-r--r--   0        0        0    13137 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/numbers.py
+-rw-r--r--   0        0        0     1099 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/opengl_compatibility.py
+-rw-r--r--   0        0        0    27413 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/opengl_geometry.py
+-rw-r--r--   0        0        0    67843 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/opengl_mobject.py
+-rw-r--r--   0        0        0     2865 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/opengl_three_dimensions.py
+-rw-r--r--   0        0        0    12505 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/polyhedra.py
+-rw-r--r--   0        0        0    11031 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/probability.py
+-rw-r--r--   0        0        0     4431 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/shape_matchers.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/svg/__init__.py
+-rw-r--r--   0        0        0    11296 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/svg/brace.py
+-rw-r--r--   0        0        0    23223 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/svg/code_mobject.py
+-rw-r--r--   0        0        0     1459 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/svg/opengl_svg_mobject.py
+-rw-r--r--   0        0        0      821 2021-08-02 10:25:53.795141 manim-0.9.0/manim/mobject/svg/opengl_svg_path.py
+-rw-r--r--   0        0        0    20277 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/svg/opengl_tex_mobject.py
+-rw-r--r--   0        0        0    45106 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/svg/opengl_text_mobject.py
+-rw-r--r--   0        0        0     5761 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/svg/style_utils.py
+-rw-r--r--   0        0        0    20602 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/svg/svg_mobject.py
+-rw-r--r--   0        0        0    16690 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/svg/svg_path.py
+-rw-r--r--   0        0        0    16734 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/svg/tex_mobject.py
+-rw-r--r--   0        0        0    48067 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/svg/text_mobject.py
+-rw-r--r--   0        0        0    40431 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/table.py
+-rw-r--r--   0        0        0     1835 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/three_d_utils.py
+-rw-r--r--   0        0        0    25916 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/three_dimensions.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/types/__init__.py
+-rw-r--r--   0        0        0    11575 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/types/image_mobject.py
+-rw-r--r--   0        0        0    10939 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/types/opengl_surface.py
+-rw-r--r--   0        0        0    43624 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/types/opengl_vectorized_mobject.py
+-rw-r--r--   0        0        0    10913 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/types/point_cloud_mobject.py
+-rw-r--r--   0        0        0    72820 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/types/vectorized_mobject.py
+-rw-r--r--   0        0        0     6319 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/value_tracker.py
+-rw-r--r--   0        0        0    35170 2021-08-02 10:25:53.799141 manim-0.9.0/manim/mobject/vector_field.py
+-rw-r--r--   0        0        0      504 2021-08-02 10:25:53.799141 manim-0.9.0/manim/opengl/__init__.py
+-rw-r--r--   0        0        0       30 2021-08-02 10:25:53.799141 manim-0.9.0/manim/plugins/__init__.py
+-rw-r--r--   0        0        0     1468 2021-08-02 10:25:53.799141 manim-0.9.0/manim/plugins/import_plugins.py
+-rw-r--r--   0        0        0      513 2021-08-02 10:25:53.799141 manim-0.9.0/manim/plugins/plugins_flags.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/__init__.py
+-rw-r--r--   0        0        0     9698 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/cairo_renderer.py
+-rw-r--r--   0        0        0    16534 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/opengl_renderer.py
+-rw-r--r--   0        0        0     4862 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/opengl_renderer_window.py
+-rw-r--r--   0        0        0    14645 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shader.py
+-rw-r--r--   0        0        0     5860 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shader_wrapper.py
+-rw-r--r--   0        0        0       98 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/default/frag.glsl
+-rw-r--r--   0        0        0      232 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/default/vert.glsl
+-rw-r--r--   0        0        0      216 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/design.frag
+-rw-r--r--   0        0        0      961 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/design_2.frag
+-rw-r--r--   0        0        0     1301 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/design_3.frag
+-rw-r--r--   0        0        0      200 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/image/frag.glsl
+-rw-r--r--   0        0        0      459 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/image/vert.glsl
+-rw-r--r--   0        0        0      583 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/NOTE.md
+-rw-r--r--   0        0        0     1602 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/add_light.glsl
+-rw-r--r--   0        0        0      179 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/camera_uniform_declarations.glsl
+-rw-r--r--   0        0        0     1866 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/finalize_color.glsl
+-rw-r--r--   0        0        0      998 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/get_gl_Position.glsl
+-rw-r--r--   0        0        0      551 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/get_rotated_surface_unit_normal_vector.glsl
+-rw-r--r--   0        0        0      773 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/get_unit_normal.glsl
+-rw-r--r--   0        0        0      478 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/position_point_into_frame.glsl
+-rw-r--r--   0        0        0     2856 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/quadratic_bezier_distance.glsl
+-rw-r--r--   0        0        0     2747 2021-08-02 10:25:53.799141 manim-0.9.0/manim/renderer/shaders/include/quadratic_bezier_geometry_functions.glsl
+-rw-r--r--   0        0        0      583 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/NOTE.md
+-rw-r--r--   0        0        0     1602 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/add_light.glsl
+-rw-r--r--   0        0        0      179 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/camera_uniform_declarations.glsl
+-rw-r--r--   0        0        0     1866 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/finalize_color.glsl
+-rw-r--r--   0        0        0      998 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/get_gl_Position.glsl
+-rw-r--r--   0        0        0      551 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/get_rotated_surface_unit_normal_vector.glsl
+-rw-r--r--   0        0        0      773 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/get_unit_normal.glsl
+-rw-r--r--   0        0        0      478 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/position_point_into_frame.glsl
+-rw-r--r--   0        0        0     2856 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/quadratic_bezier_distance.glsl
+-rw-r--r--   0        0        0     2747 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/inserts/quadratic_bezier_geometry_functions.glsl
+-rw-r--r--   0        0        0       98 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/manim_coords/frag.glsl
+-rw-r--r--   0        0        0      287 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/manim_coords/vert.glsl
+-rw-r--r--   0        0        0     1836 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/quadratic_bezier_fill/frag.glsl
+-rw-r--r--   0        0        0     3470 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/quadratic_bezier_fill/geom.glsl
+-rw-r--r--   0        0        0      523 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/quadratic_bezier_fill/vert.glsl
+-rw-r--r--   0        0        0     2683 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/quadratic_bezier_stroke/frag.glsl
+-rw-r--r--   0        0        0     8984 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/quadratic_bezier_stroke/geom.glsl
+-rw-r--r--   0        0        0      743 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/quadratic_bezier_stroke/vert.glsl
+-rw-r--r--   0        0        0      296 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/simple_vert.glsl
+-rw-r--r--   0        0        0      396 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/surface/frag.glsl
+-rw-r--r--   0        0        0      567 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/surface/vert.glsl
+-rw-r--r--   0        0        0       96 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/test/frag.glsl
+-rw-r--r--   0        0        0      152 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/test/vert.glsl
+-rw-r--r--   0        0        0      956 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/textured_surface/frag.glsl
+-rw-r--r--   0        0        0      647 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/textured_surface/vert.glsl
+-rw-r--r--   0        0        0      761 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/true_dot/frag.glsl
+-rw-r--r--   0        0        0      988 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/true_dot/geom.glsl
+-rw-r--r--   0        0        0      332 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/true_dot/vert.glsl
+-rw-r--r--   0        0        0      324 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/vectorized_mobject_fill/frag.glsl
+-rw-r--r--   0        0        0      435 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/vectorized_mobject_fill/vert.glsl
+-rw-r--r--   0        0        0     2737 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/vectorized_mobject_stroke/frag.glsl
+-rw-r--r--   0        0        0     4434 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/vectorized_mobject_stroke/vert.glsl
+-rw-r--r--   0        0        0       93 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/vertex_colors/frag.glsl
+-rw-r--r--   0        0        0      281 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/shaders/vertex_colors/vert.glsl
+-rw-r--r--   0        0        0     9120 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/vectorized_mobject_rendering.py
+-rw-r--r--   0        0        0     1786 2021-08-02 10:25:53.803141 manim-0.9.0/manim/renderer/webgl_renderer.py
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/__init__.py
+-rw-r--r--   0        0        0    40446 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/graph_scene.py
+-rw-r--r--   0        0        0     3694 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/moving_camera_scene.py
+-rw-r--r--   0        0        0     2072 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/reconfigurable_scene.py
+-rw-r--r--   0        0        0     5191 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/sample_space_scene.py
+-rw-r--r--   0        0        0    48313 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/scene.py
+-rw-r--r--   0        0        0    21403 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/scene_file_writer.py
+-rw-r--r--   0        0        0    15661 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/three_d_scene.py
+-rw-r--r--   0        0        0    37603 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/vector_space_scene.py
+-rw-r--r--   0        0        0     7028 2021-08-02 10:25:53.803141 manim-0.9.0/manim/scene/zoomed_scene.py
+-rw-r--r--   0        0        0      312 2021-08-02 10:25:53.803141 manim-0.9.0/manim/templates/Axes.mtp
+-rw-r--r--   0        0        0      547 2021-08-02 10:25:53.803141 manim-0.9.0/manim/templates/Default.mtp
+-rw-r--r--   0        0        0      327 2021-08-02 10:25:53.803141 manim-0.9.0/manim/templates/MovingCamera.mtp
+-rw-r--r--   0        0        0      134 2021-08-02 10:25:53.803141 manim-0.9.0/manim/templates/template.cfg
+-rw-r--r--   0        0        0        0 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/__init__.py
+-rw-r--r--   0        0        0    11321 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/bezier.py
+-rw-r--r--   0        0        0     2598 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/caching.py
+-rw-r--r--   0        0        0    11950 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/color.py
+-rw-r--r--   0        0        0     1237 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/config_ops.py
+-rw-r--r--   0        0        0      750 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/debug.py
+-rw-r--r--   0        0        0    14580 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/deprecation.py
+-rw-r--r--   0        0        0      160 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/exceptions.py
+-rw-r--r--   0        0        0     1102 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/family.py
+-rw-r--r--   0        0        0     1410 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/family_ops.py
+-rw-r--r--   0        0        0     6785 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/file_ops.py
+-rw-r--r--   0        0        0    13167 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/hashing.py
+-rw-r--r--   0        0        0      817 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/images.py
+-rw-r--r--   0        0        0     5610 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/ipython_magic.py
+-rw-r--r--   0        0        0     4388 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/iterables.py
+-rw-r--r--   0        0        0     4359 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/module_ops.py
+-rw-r--r--   0        0        0     3283 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/opengl.py
+-rw-r--r--   0        0        0     1554 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/paths.py
+-rw-r--r--   0        0        0    11649 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/rate_functions.py
+-rw-r--r--   0        0        0     2557 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/simple_functions.py
+-rw-r--r--   0        0        0      439 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/sounds.py
+-rw-r--r--   0        0        0    21833 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/space_ops.py
+-rw-r--r--   0        0        0     2289 2021-08-02 10:25:53.803141 manim-0.9.0/manim/utils/strings.py
+-rw-r--r--   0        0        0    10094 2021-08-02 10:25:53.807142 manim-0.9.0/manim/utils/tex.py
+-rw-r--r--   0        0        0    10356 2021-08-02 10:25:53.807142 manim-0.9.0/manim/utils/tex_file_writing.py
+-rw-r--r--   0        0        0    28452 2021-08-02 10:25:53.807142 manim-0.9.0/manim/utils/tex_templates.py
+-rw-r--r--   0        0        0      905 2021-08-02 10:25:53.807142 manim-0.9.0/manim/utils/unit.py
+-rw-r--r--   0        0        0     3135 2021-08-02 10:25:53.807142 manim-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0    13193 2021-08-02 10:26:05.305168 manim-0.9.0/setup.py
+-rw-r--r--   0        0        0    12667 2021-08-02 10:26:05.306326 manim-0.9.0/PKG-INFO
```

### Comparing `manim-0.8.0/LICENSE` & `manim-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/LICENSE.community` & `manim-0.9.0/LICENSE.community`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/README.md` & `manim-0.9.0/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -30,28 +30,23 @@
 -  [Documentation](#documentation)
 -  [Docker](#docker)
 -  [Help with Manim](#help-with-manim)
 -  [Contributing](#contributing)
 -  [License](#license)
 
 ## Installation
-
+> **WARNING:** These instructions are for the community version _only_. Trying to use these instructions to install [3b1b/manim](https://github.com/3b1b/manim) or instructions there to install this version will cause problems. Read [this](https://docs.manim.community/en/stable/installation/versions.html) and decide which version you wish to install, then only follow the instructions for your desired version.
+        
 Manim requires a few dependencies that must be installed prior to using it. If you
 want to try it out first before installing it locally, you can do so
 [in our online Jupyter environment](https://mybinder.org/v2/gist/behackl/725d956ec80969226b7bf9b4aef40b78/HEAD?filepath=basic%20example%20scenes.ipynb).
 
-For the local installation, please visit the [Documentation](https://docs.manim.community/en/stable/installation.html)
+For local installation, please visit the [Documentation](https://docs.manim.community/en/stable/installation.html)
 and follow the appropriate instructions for your operating system.
-
-Once the dependencies have been installed, run the following in a terminal window:
-
-```bash
-pip install manim
-```
-
+       
 ## Usage
 
 Manim is an extremely versatile package. The following is an example `Scene` you can construct:
 
 ```python
 from manim import *
 
@@ -160,30 +155,30 @@
 ## How to Cite Manim
 
 We acknowledge the importance of good software to support research, and we note
 that research becomes more valuable when it is communicated effectively. To
 demonstrate the value of Manim, we ask that you cite Manim in your work.
 Currently, the best way to cite Manim is to reference the
 [Manim home page](https://www.manim.community) using this BibTeX entry (the
-entry is for release `v0.6.0`, but can be adapted easily):
+entry is for release `v0.9.0`, but can be adapted easily):
 
 ```
-@Manual{Manim:v0.6.0,
+@Manual{Manim:v0.9.0,
   key =          {Manim},
   author =       {{The Manim Community Developers}},
-  title =        {{Manim} -- {M}athematical {A}nimation {F}ramework ({V}ersion v0.6.0)},
+  title =        {{Manim} -- {M}athematical {A}nimation {F}ramework ({V}ersion v0.9.0)},
   note =         {\url{https://www.manim.community}},
   year =         2021,
 }
 ```
 
 This should render a reference that looks more or less like this:
 
 42. The Manim Community Developers,
-    [Manim – Mathematical Animation Framework (Version v0.6.0)](https://www.manim.community).
+    [Manim – Mathematical Animation Framework (Version v0.9.0)](https://www.manim.community).
     2021.
 
 ## Code of Conduct
 
 Our full code of conduct, and how we enforce it, can be read on [our website](https://docs.manim.community/en/stable/conduct.html).
 
 ## License
```

### Comparing `manim-0.8.0/manim/__init__.py` & `manim-0.9.0/manim/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -38,14 +38,15 @@
 from .animation.creation import *
 from .animation.fading import *
 from .animation.growing import *
 from .animation.indication import *
 from .animation.movement import *
 from .animation.numbers import *
 from .animation.rotation import *
+from .animation.specialized import *
 from .animation.transform import *
 from .animation.transform_matching_parts import *
 from .animation.update import *
 from .camera.camera import *
 from .camera.mapping_camera import *
 from .camera.moving_camera import *
 from .camera.multi_camera import *
@@ -69,14 +70,15 @@
 from .mobject.svg.brace import *
 from .mobject.svg.code_mobject import *
 from .mobject.svg.style_utils import *
 from .mobject.svg.svg_mobject import *
 from .mobject.svg.svg_path import *
 from .mobject.svg.tex_mobject import *
 from .mobject.svg.text_mobject import *
+from .mobject.table import *
 from .mobject.three_d_utils import *
 from .mobject.three_dimensions import *
 from .mobject.types.image_mobject import *
 from .mobject.types.point_cloud_mobject import *
 from .mobject.types.vectorized_mobject import *
 from .mobject.value_tracker import *
 from .mobject.vector_field import *
```

### Comparing `manim-0.8.0/manim/__main__.py` & `manim-0.9.0/manim/__main__.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/_config/__init__.py` & `manim-0.9.0/manim/_config/__init__.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/_config/default.cfg` & `manim-0.9.0/manim/_config/default.cfg`

 * *Files 6% similar despite different names*

```diff
@@ -108,37 +108,42 @@
 fullscreen = False
 
 # "Set the position of preview window. You can use directions, e.g. UL/DR/LEFT/ORIGIN
 # or the position (pixel) of the upper left corner of the window, e.g. '960,540'",
 # --window_position
 window_position = UR
 
+# Manually adjust the size of the window, or use default to automatically scale the window based on
+# the dimensions of the monitor. 
+# --window_size
+window_size = default
+
 # --window_monitor
 window_monitor = 0
+
 # --use_projection_fill_shaders
 use_projection_fill_shaders = False
 
 # --use_projection_stroke_shaders
 use_projection_stroke_shaders = False
 
-# If the -t (--transparent) flag is used, these will be replaced with the
-# values specified in the [TRANSPARENT] section later in this file.
-png_mode = RGB
 movie_file_extension = .mp4
 
 # These now override the --quality option.
 frame_rate = 60
 pixel_height = 1080
 pixel_width = 1920
 
 # Use -1 to set max_files_cached to infinity.
 max_files_cached = 100
 #Flush cache will delete all the cached partial-movie-files.
 flush_cache = False
 disable_caching = False
+# Disable the warning when there are too much submobjects to hash.
+disable_caching_warning = False
 
 # Default tex_template
 # --tex_template
 tex_template =
 
 # specify the plugins as comma separated values
 # manim will load that plugin if it specified here.
```

### Comparing `manim-0.8.0/manim/_config/logger_utils.py` & `manim-0.9.0/manim/_config/logger_utils.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/_config/utils.py` & `manim-0.9.0/manim/_config/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -240,14 +240,15 @@
 
     _OPTS = {
         "assets_dir",
         "background_color",
         "background_opacity",
         "custom_folders",
         "disable_caching",
+        "disable_caching_warning",
         "ffmpeg_loglevel",
         "format",
         "flush_cache",
         "frame_height",
         "frame_rate",
         "frame_width",
         "frame_x_radius",
@@ -264,15 +265,14 @@
         "movie_file_extension",
         "notify_outdated_version",
         "output_file",
         "partial_movie_dir",
         "pixel_height",
         "pixel_width",
         "plugins",
-        "png_mode",
         "preview",
         "progress_bar",
         "save_as_gif",
         "save_last_frame",
         "save_pngs",
         "scene_names",
         "show_in_file_browser",
@@ -287,14 +287,15 @@
         "gui_location",
         "use_projection_fill_shaders",
         "use_projection_stroke_shaders",
         "verbosity",
         "video_dir",
         "fullscreen",
         "window_position",
+        "window_size",
         "window_monitor",
         "write_all",
         "write_to_movie",
     }
 
     def __init__(self) -> None:
         self._d = {k: None for k in self._OPTS}
@@ -515,14 +516,15 @@
             "write_all",
             "save_pngs",
             "save_as_gif",
             "preview",
             "show_in_file_browser",
             "log_to_file",
             "disable_caching",
+            "disable_caching_warning",
             "flush_cache",
             "custom_folders",
             "use_opengl_renderer",
             "use_webgl_renderer",
             "enable_gui",
             "fullscreen",
             "use_projection_fill_shaders",
@@ -551,15 +553,14 @@
             "video_dir",
             "images_dir",
             "text_dir",
             "tex_dir",
             "partial_movie_dir",
             "input_file",
             "output_file",
-            "png_mode",
             "movie_file_extension",
             "background_color",
             "renderer",
             "webgl_renderer_path",
             "window_position",
         ]:
             setattr(self, key, parser["CLI"].get(key, fallback="", raw=True))
@@ -574,14 +575,21 @@
         ]:
             setattr(self, key, parser["CLI"].getfloat(key))
 
         # tuple keys
         gui_location = tuple(map(int, re.split(";|,|-", parser["CLI"]["gui_location"])))
         setattr(self, "gui_location", gui_location)
 
+        window_size = parser["CLI"][
+            "window_size"
+        ]  # if not "default", get a tuple of the position
+        if window_size != "default":
+            window_size = tuple(map(int, re.split(";|,|-", window_size)))
+        setattr(self, "window_size", window_size)
+
         # plugins
         self.plugins = parser["CLI"].get("plugins", fallback="", raw=True).split(",")
         # the next two must be set AFTER digesting pixel_width and pixel_height
         self["frame_height"] = parser["CLI"].getfloat("frame_height", 8.0)
         width = parser["CLI"].getfloat("frame_width", None)
         if width is None:
             self["frame_width"] = self["frame_height"] * self["aspect_ratio"]
@@ -741,15 +749,16 @@
 
         if self.renderer == "opengl":
             if getattr(args, "write_to_movie") is None:
                 # --write_to_movie was not passed on the command line, so don't generate video.
                 self["write_to_movie"] = False
 
         # Handle --gui_location flag.
-        self.gui_location = args.gui_location
+        if getattr(args, "gui_location") is not None:
+            self.gui_location = args.gui_location
 
         return self
 
     def digest_file(self, filename: str) -> "ManimConfig":
         """Process the config options present in a ``.cfg`` file.
 
         This method processes a single ``.cfg`` file, whereas
@@ -1018,18 +1027,18 @@
 
     disable_caching = property(
         lambda self: self._d["disable_caching"],
         lambda self, val: self._set_boolean("disable_caching", val),
         doc="Whether to use scene caching.",
     )
 
-    png_mode = property(
-        lambda self: self._d["png_mode"],
-        lambda self, val: self._set_from_list("png_mode", val, ["RGB", "RGBA"]),
-        doc="Either RGA (no transparency) or RGBA (with transparency) (no flag).",
+    disable_caching_warning = property(
+        lambda self: self._d["disable_caching_warning"],
+        lambda self, val: self._set_boolean("disable_caching_warning", val),
+        doc="Whether a warning is raised if there are too much submobjects to hash.",
     )
 
     movie_file_extension = property(
         lambda self: self._d["movie_file_extension"],
         lambda self, val: self._set_from_list(
             "movie_file_extension", val, [".mp4", ".mov", ".webm"]
         ),
@@ -1073,20 +1082,15 @@
     @property
     def transparent(self):
         """Whether the background opacity is 0.0 (-t)."""
         return self._d["background_opacity"] == 0.0
 
     @transparent.setter
     def transparent(self, val: bool) -> None:
-        if val:
-            self.png_mode = "RGBA"
-            self.background_opacity = 0.0
-        else:
-            self.png_mode = "RGB"
-            self.background_opacity = 1.0
+        self._d["background_opacity"] = float(not val)
         self.resolve_movie_file_extension(val)
 
     @property
     def dry_run(self):
         """Whether dry run is enabled."""
         return (
             self.write_to_movie is False
@@ -1171,14 +1175,20 @@
 
     window_position = property(
         lambda self: self._d["window_position"],
         lambda self, val: self._d.__setitem__("window_position", val),
         doc="Set the position of preview window. You can use directions, e.g. UL/DR/ORIGIN/LEFT...or the position(pixel) of the upper left corner of the window, e.g. '960,540'",
     )
 
+    window_size = property(
+        lambda self: self._d["window_size"],
+        lambda self, val: self._d.__setitem__("window_size", val),
+        doc="The size of the opengl window. 'default' to automatically scale the window based on the display monitor.",
+    )
+
     def resolve_movie_file_extension(self, is_transparent):
         if is_transparent:
             self.movie_file_extension = ".webm" if self.format == "webm" else ".mov"
         elif self.format == "webm":
             self.movie_file_extension = ".webm"
         elif self.format == "mov":
             self.movie_file_extension = ".mov"
```

### Comparing `manim-0.8.0/manim/animation/animation.py` & `manim-0.9.0/manim/animation/animation.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,17 @@
 """Animate mobjects."""
 
 
+from .. import logger
+from ..mobject import mobject, opengl_mobject
+from ..mobject.mobject import Mobject
+from ..mobject.opengl_mobject import OpenGLMobject
+from ..utils.deprecation import deprecated
+from ..utils.rate_functions import smooth
+
 __all__ = ["Animation", "Wait", "override_animation"]
 
 
 from copy import deepcopy
 from typing import (
     TYPE_CHECKING,
     Callable,
@@ -16,20 +23,14 @@
     Type,
     Union,
 )
 
 if TYPE_CHECKING:
     from manim.scene.scene import Scene
 
-from .. import logger
-from ..mobject import mobject, opengl_mobject
-from ..mobject.mobject import Mobject
-from ..mobject.opengl_mobject import OpenGLMobject
-from ..utils.deprecation import deprecated
-from ..utils.rate_functions import smooth
 
 DEFAULT_ANIMATION_RUN_TIME: float = 1.0
 DEFAULT_ANIMATION_LAG_RATIO: float = 0.0
 
 
 class Animation:
     """An animation.
@@ -92,17 +93,17 @@
                 # lag_ratio also works recursively on nested submobjects:
                 self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))
 
     """
 
     def __new__(
         cls,
-        mobject: Optional[Mobject] = None,
+        mobject=None,
         *args,
-        use_override: bool = True,
+        use_override=True,
         **kwargs,
     ):
         if isinstance(mobject, Mobject) and use_override:
             func = mobject.animation_override_for(cls)
             if func is not None:
                 anim = func(mobject, *args, **kwargs)
                 logger.debug(
@@ -274,14 +275,23 @@
         alpha
             The relative time to set the aniamtion to, 0 meaning the start, 1 meaning
             the end.
         """
         self.interpolate_mobject(alpha)
 
     def interpolate_mobject(self, alpha: float) -> None:
+        """Interpolates the mobject of the :class:`Animation` based on alpha value.
+
+        Parameters
+        ----------
+        alpha
+            A float between 0 and 1 expressing the ratio to which the animation
+            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
+            to the animation being completed 0%, 50%, and 100%, respectively.
+        """
         families = list(self.get_all_families_zipped())
         for i, mobs in enumerate(families):
             sub_alpha = self.get_sub_alpha(alpha, i, len(families))
             self.interpolate_submobject(*mobs, sub_alpha)
 
     def interpolate_submobject(
         self,
```

### Comparing `manim-0.8.0/manim/animation/composition.py` & `manim-0.9.0/manim/animation/composition.py`

 * *Files 4% similar despite different names*

```diff
@@ -55,14 +55,16 @@
 
     def finish(self) -> None:
         for anim in self.animations:
             anim.finish()
 
     def clean_up_from_scene(self, scene: Scene) -> None:
         for anim in self.animations:
+            if self.remover:
+                anim.remover = self.remover
             anim.clean_up_from_scene(scene)
 
     def update_mobjects(self, dt: float) -> None:
         for anim in self.animations:
             anim.update_mobjects(dt)
 
     def init_run_time(self, run_time) -> float:
```

### Comparing `manim-0.8.0/manim/animation/creation.py` & `manim-0.9.0/manim/animation/creation.py`

 * *Files 2% similar despite different names*

```diff
@@ -88,14 +88,15 @@
 
 if TYPE_CHECKING:
     from manim.mobject.svg.text_mobject import Text
 
 from ..animation.animation import Animation
 from ..animation.composition import Succession
 from ..mobject.mobject import Group, Mobject
+from ..mobject.types.opengl_surface import OpenGLSurface
 from ..mobject.types.opengl_vectorized_mobject import OpenGLVMobject
 from ..mobject.types.vectorized_mobject import VMobject
 from ..utils.bezier import integer_interpolate
 from ..utils.deprecation import deprecated
 from ..utils.rate_functions import double_smooth, linear, smooth
 
 
@@ -109,17 +110,20 @@
 
     See Also
     --------
     :class:`Create`, :class:`~.ShowPassingFlash`
 
     """
 
-    def __init__(self, mobject: Union[Mobject, OpenGLVMobject, None], **kwargs):
-        if not isinstance(mobject, (VMobject, OpenGLVMobject)):
-            raise TypeError("This Animation only works on vectorized mobjects")
+    def __init__(
+        self, mobject: Union[VMobject, OpenGLVMobject, OpenGLSurface, None], **kwargs
+    ):
+        pointwise = getattr(mobject, "pointwise_become_partial", None)
+        if not callable(pointwise):
+            raise NotImplementedError("This animation is not defined for this Mobject.")
         super().__init__(mobject, **kwargs)
 
     def interpolate_submobject(
         self, submobject: Mobject, starting_submobject: Mobject, alpha: float
     ) -> None:
         submobject.pointwise_become_partial(
             starting_submobject, *self._get_bounds(alpha)
@@ -154,15 +158,15 @@
     --------
     :class:`~.ShowPassingFlash`
 
     """
 
     def __init__(
         self,
-        mobject: Union[VMobject, OpenGLVMobject],
+        mobject: Union[VMobject, OpenGLVMobject, OpenGLSurface],
         lag_ratio: float = 1.0,
         **kwargs,
     ) -> None:
         super().__init__(mobject, lag_ratio=lag_ratio, **kwargs)
 
     def _get_bounds(self, alpha: float) -> Tuple[int, float]:
         return (0, alpha)
@@ -270,27 +274,35 @@
     Examples
     --------
     .. manim:: ShowWrite
 
         class ShowWrite(Scene):
             def construct(self):
                 self.play(Write(Text("Hello").scale(3)))
+
+    .. manim:: ShowWriteReversed
+
+        class ShowWriteReversed(Scene):
+            def construct(self):
+                self.play(Write(Text("Hello").scale(3), reverse=True))
     """
 
     def __init__(
         self,
         vmobject: Union[VMobject, OpenGLVMobject],
         rate_func: Callable[[float], float] = linear,
+        reverse: bool = False,
         **kwargs,
     ) -> None:
         run_time: Optional[float] = kwargs.pop("run_time", None)
         lag_ratio: Optional[float] = kwargs.pop("lag_ratio", None)
         run_time, lag_ratio = self._set_default_config_from_length(
             vmobject, run_time, lag_ratio
         )
+        self.reverse = reverse
         super().__init__(
             vmobject,
             rate_func=rate_func,
             run_time=run_time,
             lag_ratio=lag_ratio,
             **kwargs,
         )
@@ -307,80 +319,78 @@
                 run_time = 1
             else:
                 run_time = 2
         if lag_ratio is None:
             lag_ratio = min(4.0 / length, 0.2)
         return run_time, lag_ratio
 
+    def reverse_submobjects(self) -> None:
+        self.mobject.invert(recursive=True)
+
+    def begin(self) -> None:
+        if self.reverse:
+            self.reverse_submobjects()
+        super().begin()
+
+    def finish(self) -> None:
+        super().finish()
+        if self.reverse:
+            self.reverse_submobjects()
+
 
 class Unwrite(Write):
     """Simulate erasing by hand a :class:`~.Text` or a :class:`~.VMobject`.
 
     Parameters
     ----------
     reverse : :class:`bool`
         Set True to have the animation start erasing from the last submobject first.
 
     Examples
     --------
 
-    .. manim:: UnwriteReverseFalse
+    .. manim :: UnwriteReverseTrue
 
-        class UnwriteReverseFalse(Scene):
+        class UnwriteReverseTrue(Scene):
             def construct(self):
                 text = Tex("Alice and Bob").scale(3)
                 self.add(text)
                 self.play(Unwrite(text))
 
-    .. manim :: UnwriteReverseTrue
+    .. manim:: UnwriteReverseFalse
 
-        class UnwriteReverseTrue(Scene):
+        class UnwriteReverseFalse(Scene):
             def construct(self):
                 text = Tex("Alice and Bob").scale(3)
                 self.add(text)
-                self.play(Unwrite(text,reverse=True))
-
+                self.play(Unwrite(text, reverse=False))
     """
 
     def __init__(
         self,
         vmobject: VMobject,
         rate_func: Callable[[float], float] = linear,
-        reverse: bool = False,
+        reverse: bool = True,
         **kwargs,
     ) -> None:
 
-        self.vmobject = vmobject
-        self.reverse = reverse
         run_time: Optional[float] = kwargs.pop("run_time", None)
         lag_ratio: Optional[float] = kwargs.pop("lag_ratio", None)
         run_time, lag_ratio = self._set_default_config_from_length(
             vmobject, run_time, lag_ratio
         )
         super().__init__(
             vmobject,
             run_time=run_time,
             lag_ratio=lag_ratio,
             rate_func=lambda t: -rate_func(t) + 1,
+            reverse=reverse,
             **kwargs,
         )
 
-    def begin(self) -> None:
-        if not self.reverse:
-            self.reverse_submobjects()
-        super().begin()
-
-    def finish(self) -> None:
-        if not self.reverse:
-            self.reverse_submobjects()
-        super().finish()
-
-    def reverse_submobjects(self) -> None:
-        self.vmobject.invert(recursive=True)
-
 
 class ShowIncreasingSubsets(Animation):
     """Show one submobject at a time, leaving all previous ones displayed on screen.
 
     Examples
     --------
```

### Comparing `manim-0.8.0/manim/animation/growing.py` & `manim-0.9.0/manim/animation/growing.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/animation/indication.py` & `manim-0.9.0/manim/animation/indication.py`

 * *Files 10% similar despite different names*

```diff
@@ -25,26 +25,18 @@
 
 """
 
 __all__ = [
     "FocusOn",
     "Indicate",
     "Flash",
-    "CircleIndicate",
     "ShowPassingFlash",
     "ShowPassingFlashWithThinningStrokeWidth",
-    "ShowCreationThenDestruction",
     "ShowCreationThenFadeOut",
-    "AnimationOnSurroundingRectangle",
-    "ShowPassingFlashAround",
-    "ShowCreationThenDestructionAround",
-    "ShowCreationThenFadeAround",
     "ApplyWave",
-    "WiggleOutThenIn",
-    "TurnInsideOut",
     "Circumscribe",
     "Wiggle",
 ]
 
 import typing
 from typing import Callable, Type, Union
 
@@ -108,15 +100,15 @@
     ) -> None:
         self.focus_point = focus_point
         self.color = color
         self.opacity = opacity
         remover = True
         # Initialize with blank mobject, while create_target
         # and create_starting_mobject handle the meat
-        super().__init__(VMobject(), run_time=run_time, remover=remover, **kwargs)
+        super().__init__(VGroup(), run_time=run_time, remover=remover, **kwargs)
 
     def create_target(self) -> "Dot":
         little_dot = Dot(radius=0)
         little_dot.set_fill(self.color, opacity=self.opacity)
         little_dot.add_updater(lambda d: d.move_to(self.focus_point))
         return little_dot
 
@@ -274,40 +266,14 @@
                 run_time=self.run_time,
                 **self.animation_config,
             )
             for line in self.lines
         ]
 
 
-@deprecated(since="v0.5.0", until="v0.7.0", replacement="Circumscribe")
-class CircleIndicate(Indicate):
-    def __init__(
-        self,
-        mobject: "Mobject",
-        circle_config: typing.Dict[str, typing.Any] = {"color": YELLOW},
-        rate_func: typing.Callable[
-            [float, typing.Optional[float]], np.ndarray
-        ] = there_and_back,
-        remover: bool = True,
-        **kwargs
-    ) -> None:
-        self.circle_config = circle_config
-        circle = self.get_circle(mobject)
-        super().__init__(circle, rate_func=rate_func, remover=remover, **kwargs)
-
-    def get_circle(self, mobject: "Mobject") -> Circle:
-        circle = Circle(**self.circle_config)
-        circle.add_updater(lambda c: c.surround(mobject))
-        return circle
-
-    def interpolate_mobject(self, alpha: float) -> None:
-        super().interpolate_mobject(alpha)
-        self.mobject.set_stroke(opacity=alpha)
-
-
 class ShowPassingFlash(ShowPartial):
     """Show only a sliver of the VMobject each frame.
 
     Parameters
     ----------
     mobject
         The mobject whose stroke is animated.
@@ -375,89 +341,23 @@
                     np.linspace(0, max_stroke_width, self.n_segments),
                     np.linspace(max_time_width, 0, self.n_segments),
                 )
             ],
         )
 
 
-@deprecated(since="v0.5.0", until="v0.7.0", replacement="ShowPassingFlash")
-class ShowCreationThenDestruction(ShowPassingFlash):
-    def __init__(
-        self, mobject: "Mobject", time_width: float = 2.0, run_time: float = 1, **kwargs
-    ) -> None:
-        super().__init__(mobject, time_width=time_width, run_time=run_time, **kwargs)
-
-
 # TODO Decide what to do with this class:
 #   Remove?
 #   Deprecate?
 #   Keep and add docs?
 class ShowCreationThenFadeOut(Succession):
     def __init__(self, mobject: "Mobject", remover: bool = True, **kwargs) -> None:
         super().__init__(Create(mobject), FadeOut(mobject), remover=remover, **kwargs)
 
 
-@deprecated(since="v0.5.0", until="v0.7.0", replacement="Circumscribe")
-class AnimationOnSurroundingRectangle(AnimationGroup):
-    def __init__(
-        self,
-        mobject: "Mobject",
-        rect_animation: Animation = Animation,
-        surrounding_rectangle_config: typing.Dict[str, typing.Any] = {},
-        **kwargs
-    ) -> None:
-        # Callable which takes in a rectangle, and spits out some animation.  Could be
-        # some animation class, could be something more
-        self.rect_animation = rect_animation
-        self.surrounding_rectangle_config = surrounding_rectangle_config
-        self.mobject_to_surround = mobject
-
-        rect = self.get_rect()
-        rect.add_updater(lambda r: r.move_to(mobject))
-
-        super().__init__(
-            self.rect_animation(rect, **kwargs),
-        )
-
-    def get_rect(self) -> SurroundingRectangle:
-        return SurroundingRectangle(
-            self.mobject_to_surround, **self.surrounding_rectangle_config
-        )
-
-
-@deprecated(since="v0.5.0", until="v0.7.0", replacement="Circumscribe")
-class ShowPassingFlashAround(AnimationOnSurroundingRectangle):
-    def __init__(
-        self, mobject: "Mobject", rect_animation: Animation = ShowPassingFlash, **kwargs
-    ) -> None:
-        super().__init__(mobject, rect_animation=rect_animation, **kwargs)
-
-
-@deprecated(since="v0.5.0", until="v0.7.0", replacement="Circumscribe")
-class ShowCreationThenDestructionAround(AnimationOnSurroundingRectangle):
-    def __init__(
-        self,
-        mobject: "Mobject",
-        rect_animation: Animation = ShowCreationThenDestruction,
-        **kwargs
-    ) -> None:
-        super().__init__(mobject, rect_animation=rect_animation, **kwargs)
-
-
-@deprecated(since="v0.5.0", until="v0.7.0", replacement="Circumscribe")
-class ShowCreationThenFadeAround(AnimationOnSurroundingRectangle):
-    def __init__(
-        self,
-        mobject: "Mobject",
-        rect_animation: Animation = ShowCreationThenFadeOut,
-        **kwargs
-    ) -> None:
-        super().__init__(mobject, rect_animation=rect_animation, **kwargs)
-
-
 class ApplyWave(Homotopy):
     """Send a wave through the Mobject distorting it temporarily.
 
     Parameters
     ----------
     mobject
         The mobject to be distorted.
@@ -649,33 +549,14 @@
         )
         submobject.rotate(
             wiggle(alpha, self.n_wiggles) * self.rotation_angle,
             about_point=self.get_rotate_about_point(),
         )
 
 
-@deprecated(since="v0.5.0", until="v0.7.0", replacement="Wiggle")
-class WiggleOutThenIn(Wiggle):
-    def __init__(*args, **kwargs):
-        super().__init(*args, **kwargs)
-
-
-@deprecated(
-    since="v0.5.0",
-    until="v0.7.0",
-    message="Use :code:`mobject.animate.become(mobject.copy().reverse_points())` instead if you have to.",
-)
-class TurnInsideOut(Transform):
-    def __init__(self, mobject: "Mobject", path_arc: float = TAU / 4, **kwargs) -> None:
-        super().__init__(mobject, path_arc=path_arc, **kwargs)
-
-    def create_target(self) -> "Mobject":
-        return self.mobject.copy().reverse_points()
-
-
 class Circumscribe(Succession):
     """Draw a temporary line surrounding the mobject.
 
     Parameters
     ----------
     mobject
         The mobject to be circumscribed.
```

### Comparing `manim-0.8.0/manim/animation/movement.py` & `manim-0.9.0/manim/animation/movement.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/animation/numbers.py` & `manim-0.9.0/manim/animation/numbers.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/animation/rotation.py` & `manim-0.9.0/manim/animation/rotation.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/animation/transform.py` & `manim-0.9.0/manim/animation/transform.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/animation/transform_matching_parts.py` & `manim-0.9.0/manim/animation/transform_matching_parts.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/animation/update.py` & `manim-0.9.0/manim/animation/update.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/camera/camera.py` & `manim-0.9.0/manim/camera/camera.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/camera/mapping_camera.py` & `manim-0.9.0/manim/camera/mapping_camera.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/camera/moving_camera.py` & `manim-0.9.0/manim/camera/moving_camera.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/camera/multi_camera.py` & `manim-0.9.0/manim/camera/multi_camera.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/camera/three_d_camera.py` & `manim-0.9.0/manim/camera/three_d_camera.py`

 * *Files 2% similar despite different names*

```diff
@@ -40,15 +40,15 @@
         Parameters
         ----------
         *args
             Any argument of Camera
         *kwargs
             Any keyword argument of Camera.
         """
-        self._frame_center = Point(kwargs.get("frame_center", ORIGIN))
+        self._frame_center = Point(kwargs.get("frame_center", ORIGIN), stroke_width=0)
         super().__init__(**kwargs)
         self.distance = distance
         self.phi = phi
         self.theta = theta
         self.gamma = gamma
         self.shading_factor = shading_factor
         self.default_distance = default_distance
@@ -285,15 +285,14 @@
                 factor = np.exp(zs / distance)
                 lt0 = zs < 0
                 factor[lt0] = distance / (distance - zs[lt0])
             else:
                 factor = distance / (distance - zs)
                 factor[(distance - zs) < 0] = 10 ** 6
             points[:, i] *= factor
-        points = points + frame_center
         return points
 
     def project_point(self, point):
         """Applies the current rotation_matrix as a projection
         matrix to the passed point.
 
         Parameters
@@ -383,24 +382,24 @@
         The Mobject will no longer have a fixed orientation.
 
         Parameters
         ----------
         mobjects : :class:`Mobject`
             The mobjects whose orientation need not be fixed any longer.
         """
-        for mobject in self.extract_mobject_family_members(mobjects):
+        for mobject in extract_mobject_family_members(mobjects):
             if mobject in self.fixed_orientation_mobjects:
                 self.fixed_orientation_mobjects.remove(mobject)
 
     def remove_fixed_in_frame_mobjects(self, *mobjects):
         """If a mobject was fixed in frame by passing it through
         :meth:`.add_fixed_in_frame_mobjects`, then this undoes that fixing.
         The Mobject will no longer be fixed in frame.
 
         Parameters
         ----------
         mobjects : :class:`Mobject`
             The mobjects which need not be fixed in frame any longer.
         """
-        for mobject in self.extract_mobject_family_members(mobjects):
+        for mobject in extract_mobject_family_members(mobjects):
             if mobject in self.fixed_in_frame_mobjects:
                 self.fixed_in_frame_mobjects.remove(mobject)
```

### Comparing `manim-0.8.0/manim/camera/webgl_camera.py` & `manim-0.9.0/manim/camera/webgl_camera.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/cli/cfg/group.py` & `manim-0.9.0/manim/cli/cfg/group.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/cli/init/commands.py` & `manim-0.9.0/manim/cli/init/commands.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/cli/new/group.py` & `manim-0.9.0/manim/cli/new/group.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/cli/plugins/commands.py` & `manim-0.9.0/manim/cli/plugins/commands.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/cli/render/commands.py` & `manim-0.9.0/manim/cli/render/commands.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/cli/render/ease_of_access_options.py` & `manim-0.9.0/manim/cli/render/ease_of_access_options.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,31 +1,38 @@
 import click
 from cloup import option, option_group
 
 ease_of_access_options = option_group(
     "Ease of access options",
     option(
         "--progress_bar",
-        default="display",
-        show_default=True,
+        default=None,
+        show_default=False,
         type=click.Choice(
             ["display", "leave", "none"],
             case_sensitive=False,
         ),
         help="Display progress bars and/or keep them displayed.",
     ),
     option(
         "-p",
         "--preview",
         is_flag=True,
         help="Preview the Scene's animation. OpenGL does a live preview in a "
         "popup window. Cairo opens the rendered video file in the system "
         "default media player.",
+        default=None,
     ),
     option(
         "-f",
         "--show_in_file_browser",
         is_flag=True,
         help="Show the output file in the file browser.",
+        default=None,
+    ),
+    option(
+        "--jupyter",
+        is_flag=True,
+        help="Using jupyter notebook magic.",
+        default=None,
     ),
-    option("--jupyter", is_flag=True, help="Using jupyter notebook magic."),
 )
```

### Comparing `manim-0.8.0/manim/cli/render/global_options.py` & `manim-0.9.0/manim/cli/render/global_options.py`

 * *Files 8% similar despite different names*

```diff
@@ -18,53 +18,64 @@
 
 global_options = option_group(
     "Global options",
     option(
         "-c",
         "--config_file",
         help="Specify the configuration file to use for render settings.",
+        default=None,
     ),
     option(
         "--custom_folders",
         is_flag=True,
+        default=None,
         help="Use the folders defined in the [custom_folders] section of the "
         "config file to define the output folder structure.",
     ),
     option(
         "--disable_caching",
         is_flag=True,
+        default=None,
         help="Disable the use of the cache (still generates cache files).",
     ),
-    option("--flush_cache", is_flag=True, help="Remove cached partial movie files."),
-    option("--tex_template", help="Specify a custom TeX template file."),
+    option(
+        "--flush_cache",
+        is_flag=True,
+        help="Remove cached partial movie files.",
+        default=None,
+    ),
+    option("--tex_template", help="Specify a custom TeX template file.", default=None),
     option(
         "-v",
         "--verbosity",
         type=click.Choice(
             ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
             case_sensitive=False,
         ),
         help="Verbosity of CLI output. Changes ffmpeg log level unless 5+.",
+        default=None,
     ),
     option(
         "--notify_outdated_version/--silent",
         is_flag=True,
         default=None,
         help="Display warnings for outdated installation.",
     ),
     option(
         "--enable_gui",
         is_flag=True,
         help="Enable GUI interaction.",
+        default=None,
     ),
     option(
         "--gui_location",
-        default="0,0",
+        default=None,
         callback=validate_gui_location,
         help="Starting location for the GUI.",
     ),
     option(
         "--fullscreen",
         is_flag=True,
         help="Expand the window to its maximum possible size.",
+        default=None,
     ),
 )
```

### Comparing `manim-0.8.0/manim/cli/render/output_options.py` & `manim-0.9.0/manim/cli/render/output_options.py`

 * *Files 9% similar despite different names*

```diff
@@ -3,27 +3,32 @@
 
 output_options = option_group(
     "Output options",
     option(
         "-o",
         "--output_file",
         type=str,
+        default=None,
         help="Specify the filename(s) of the rendered scene(s).",
     ),
     option(
         "--write_to_movie",
         is_flag=True,
         default=None,
         help="Write to a file.",
     ),
     option(
         "--media_dir",
         type=click.Path(),
+        default=None,
         help="Path to store rendered videos and latex.",
     ),
-    option("--log_dir", type=click.Path(), help="Path to store render logs."),
+    option(
+        "--log_dir", type=click.Path(), help="Path to store render logs.", default=None
+    ),
     option(
         "--log_to_file",
         is_flag=True,
+        default=None,
         help="Log terminal output to file.",
     ),
 )
```

### Comparing `manim-0.8.0/manim/cli/render/render_options.py` & `manim-0.9.0/manim/cli/render/render_options.py`

 * *Files 14% similar despite different names*

```diff
@@ -36,67 +36,75 @@
     "Render Options",
     option(
         "-n",
         "--from_animation_number",
         callback=validate_scene_range,
         help="Start rendering from n_0 until n_1. If n_1 is left unspecified, "
         "renders all scenes after n_0.",
+        default=None,
     ),
     option(
         "-a",
         "--write_all",
         is_flag=True,
         help="Render all scenes in the input file.",
+        default=None,
     ),
     option(
         "--format",
         type=click.Choice(["png", "gif", "mp4", "webm", "mov"], case_sensitive=False),
+        default=None,
     ),
-    option("-s", "--save_last_frame", is_flag=True),
+    option("-s", "--save_last_frame", is_flag=True, default=None),
     option(
         "-q",
         "--quality",
-        default="h",
+        default=None,
         type=click.Choice(["l", "m", "h", "p", "k"], case_sensitive=False),
         help="""
             Render quality at the follow resolution framerates, respectively:
             854x480 30FPS,
             1280x720 30FPS,
             1920x1080 60FPS,
             2560x1440 60FPS,
             3840x2160 60FPS
             """,
     ),
     option(
         "-r",
         "--resolution",
         callback=validate_resolution,
+        default=None,
         help="Resolution in (W,H) for when 16:9 aspect ratio isn't possible.",
     ),
     option(
         "--fps",
         "--frame_rate",
         "frame_rate",
         type=float,
+        default=None,
         help="Render at this frame rate.",
     ),
     option(
         "--renderer",
         type=click.Choice(["cairo", "opengl", "webgl"], case_sensitive=False),
         help="Select a renderer for your Scene.",
+        default=None,
     ),
     option(
         "--use_opengl_renderer",
         is_flag=True,
         help="Render scenes using OpenGL (Deprecated).",
+        default=None,
     ),
     option(
         "--use_webgl_renderer",
         is_flag=True,
         help="Render scenes using the WebGL frontend (Deprecated).",
+        default=None,
     ),
     option(
         "--webgl_renderer_path",
         default=None,
         type=click.Path(),
         help="The path to the WebGL frontend.",
     ),
@@ -118,20 +126,25 @@
         "-s",
         "--save_last_frame",
         default=None,
         is_flag=True,
         help="Save last frame as png (Deprecated).",
     ),
     option(
-        "-t", "--transparent", is_flag=True, help="Render scenes with alpha channel."
+        "-t",
+        "--transparent",
+        is_flag=True,
+        help="Render scenes with alpha channel.",
     ),
     option(
         "--use_projection_fill_shaders",
         is_flag=True,
         help="Use shaders for OpenGLVMobject fill which are compatible with transformation matrices.",
+        default=None,
     ),
     option(
         "--use_projection_stroke_shaders",
         is_flag=True,
         help="Use shaders for OpenGLVMobject stroke which are compatible with transformation matrices.",
+        default=None,
     ),
 )
```

### Comparing `manim-0.8.0/manim/constants.py` & `manim-0.9.0/manim/constants.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/grpc/gen/frameserver_pb2.py` & `manim-0.9.0/manim/grpc/gen/frameserver_pb2.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/grpc/gen/frameserver_pb2_grpc.py` & `manim-0.9.0/manim/grpc/gen/frameserver_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/grpc/gen/renderserver_pb2.py` & `manim-0.9.0/manim/grpc/gen/renderserver_pb2.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/grpc/gen/renderserver_pb2_grpc.py` & `manim-0.9.0/manim/grpc/gen/renderserver_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/grpc/impl/frame_server_impl.py` & `manim-0.9.0/manim/grpc/impl/frame_server_impl.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/grpc/proto/frameserver.proto` & `manim-0.9.0/manim/grpc/proto/frameserver.proto`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/grpc/proto/renderserver.proto` & `manim-0.9.0/manim/grpc/proto/renderserver.proto`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/gui/gui.py` & `manim-0.9.0/manim/gui/gui.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/changing.py` & `manim-0.9.0/manim/mobject/changing.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/coordinate_systems.py` & `manim-0.9.0/manim/mobject/coordinate_systems.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
     "NumberPlane",
     "PolarPlane",
     "ComplexPlane",
 ]
 
 import fractions as fr
 import numbers
-from typing import Callable, Iterable, Optional, Sequence, Tuple, Union
+from typing import Callable, Dict, Iterable, Optional, Sequence, Tuple, Union
 
 import numpy as np
 from colour import Color
 
 from manim.mobject.opengl_compatibility import ConvertToOpenGL
 
 from .. import config
@@ -272,48 +272,64 @@
         self.axis_labels = VGroup(
             self.get_x_axis_label(x_label),
             self.get_y_axis_label(y_label),
         )
         return self.axis_labels
 
     def add_coordinates(
-        self, *axes_numbers: Optional[Iterable[float]], **kwargs
-    ) -> VGroup:
+        self,
+        *axes_numbers: Union[
+            Optional[Iterable[float]], Union[Dict[float, Union[str, float, "Mobject"]]]
+        ],
+        **kwargs,
+    ):
         """Adds labels to the axes.
 
+        Parameters
+        ----------
+
         axes_numbers
             The numbers to be added to the axes. Use ``None`` to represent an axis with default labels.
 
         Examples
         --------
 
         .. code-block:: python
 
             ax = ThreeDAxes()
             x_labels = range(-4, 5)
             z_labels = range(-4, 4, 2)
             ax.add_coordinates(x_labels, None, z_labels)  # default y labels, custom x & z labels
             ax.add_coordinates(x_labels)  # only x labels
 
-        Returns
-        -------
-        VGroup
-            A :class:`VGroup` of the number mobjects.
+        .. code-block:: python
+
+            # specifically control the position and value of the labels using a dict
+            ax = Axes(x_range=[0, 7])
+            x_pos = [x for x in range(1, 8)]
+
+            # strings are automatically converted into a `Tex` mobject.
+            x_vals = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
+            x_dict = dict(zip(x_pos, x_vals))
+            ax.add_coordinates(x_dict)
         """
 
         self.coordinate_labels = VGroup()
         # if nothing is passed to axes_numbers, produce axes with default labelling
         if not axes_numbers:
             axes_numbers = [None for _ in range(self.dimension)]
 
         for axis, values in zip(self.axes, axes_numbers):
-            labels = axis.add_numbers(values, **kwargs)
+            if isinstance(values, dict):
+                labels = axis.add_labels(values, **kwargs)
+            else:
+                labels = axis.add_numbers(values, **kwargs)
             self.coordinate_labels.add(labels)
 
-        return self.coordinate_labels
+        return self
 
     def get_line_from_axis_to_point(
         self,
         index: int,
         point: Sequence[float],
         line_func: Line = DashedLine,
         color: Color = LIGHT_GREY,
@@ -603,15 +619,20 @@
         -------
         :class:`~.VGroup`
             A :class:`~.VGroup` containing the Riemann Rectangles.
         """
 
         # setting up x_range, overwrite user's third input
         if x_range is None:
-            x_range = self.x_range
+            if bounded_graph is None:
+                x_range = [graph.t_min, graph.t_max]
+            else:
+                x_min = max(graph.t_min, bounded_graph.t_min)
+                x_max = min(graph.t_max, bounded_graph.t_max)
+                x_range = [x_min, x_max]
 
         x_range = [*x_range[:2], dx]
 
         rectangles = VGroup()
         x_range = np.arange(*x_range)
 
         # allows passing a string to color the graph
@@ -1233,15 +1254,16 @@
                     self.add(plane, line_graph)
         """
         x_values, y_values = map(np.array, (x_values, y_values))
         if z_values is None:
             z_values = np.zeros(x_values.shape)
 
         line_graph = VDict()
-        graph = VMobject(color=line_color, **kwargs)
+        graph = VGroup(color=line_color, **kwargs)
+
         vertices = [
             self.coords_to_point(x, y, z)
             for x, y, z in zip(x_values, y_values, z_values)
         ]
         graph.set_points_as_corners(vertices)
         graph.z_index = -1
         line_graph["line_graph"] = graph
```

### Comparing `manim-0.8.0/manim/mobject/frame.py` & `manim-0.9.0/manim/mobject/frame.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/functions.py` & `manim-0.9.0/manim/mobject/functions.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/geometry.py` & `manim-0.9.0/manim/mobject/geometry.py`

 * *Files 0% similar despite different names*

```diff
@@ -75,22 +75,24 @@
 from manim.mobject.opengl_mobject import OpenGLMobject
 
 from .. import config, logger
 from ..constants import *
 from ..mobject.mobject import Mobject
 from ..mobject.types.vectorized_mobject import DashedVMobject, VGroup, VMobject
 from ..utils.color import *
+from ..utils.deprecation import deprecated_params
 from ..utils.iterables import adjacent_n_tuples, adjacent_pairs
 from ..utils.simple_functions import fdiv
 from ..utils.space_ops import (
     angle_between_vectors,
     angle_of_vector,
     compass_directions,
     line_intersection,
     normalize,
+    perpendicular_bisector,
     regular_vertices,
     rotate_vector,
 )
 from .opengl_compatibility import ConvertToOpenGL
 
 
 class TipableVMobject(VMobject, metaclass=ConvertToOpenGL):
@@ -579,14 +581,44 @@
         :class:`numpy.ndarray`
             The location of the point along the circle's circumference.
         """
 
         start_angle = angle_of_vector(self.get_points()[0] - self.get_center())
         return self.point_from_proportion((angle - start_angle) / TAU)
 
+    @staticmethod
+    def from_three_points(
+        p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], **kwargs
+    ):
+        """Returns a circle passing through the specified
+        three points.
+
+        Example
+        -------
+
+        .. manim:: CircleFromPointsExample
+            :save_last_frame:
+
+            class CircleFromPointsExample(Scene):
+                def construct(self):
+                    circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
+                    dots = VGroup(
+                        Dot(LEFT),
+                        Dot(LEFT + UP),
+                        Dot(UP * 2),
+                    )
+                    self.add(NumberPlane(), circle, dots)
+        """
+        center = line_intersection(
+            perpendicular_bisector([p1, p2]),
+            perpendicular_bisector([p2, p3]),
+        )
+        radius = np.linalg.norm(p1 - center)
+        return Circle(radius=radius, **kwargs).shift(center)
+
 
 class Dot(Circle):
     """A circle with a very small radius.
 
     Parameters
     ----------
     point : Union[:class:`list`, :class:`numpy.ndarray`], optional
@@ -1054,57 +1086,62 @@
 
     Parameters
     ----------
     args : Any
         Arguments to be passed to :class:`Line`
     dash_length : :class:`float`, optional
         The length of each individual dash of the line.
-    dash_spacing : Optional[:class:`float`]
-        The spacing between the dashes.
-    positive_space_ratio : :class:`float`, optional
-        The ratio of empty space to dash space. Range of 0-1.
+    dashed_ratio : :class:`float`, optional
+        The ratio of dash space to empty space. Range of 0-1.
     kwargs : Any
         Additional arguments to be passed to :class:`Line`
 
     Examples
     --------
     .. manim:: DashedLineExample
         :save_last_frame:
 
         class DashedLineExample(Scene):
             def construct(self):
                 # dash_length increased
                 dashed_1 = DashedLine(config.left_side, config.right_side, dash_length=2.0).shift(UP*2)
                 # normal
                 dashed_2 = DashedLine(config.left_side, config.right_side)
-                # positive_space_ratio decreased
-                dashed_3 = DashedLine(config.left_side, config.right_side, positive_space_ratio=0.1).shift(DOWN*2)
+                # dashed_ratio decreased
+                dashed_3 = DashedLine(config.left_side, config.right_side, dashed_ratio=0.1).shift(DOWN*2)
                 self.add(dashed_1, dashed_2, dashed_3)
 
     See Also
     --------
     :class:`~.DashedVMobject`
     """
 
+    @deprecated_params(
+        params="positive_space_ratio dash_spacing",
+        since="v0.9.0",
+        message="Use dashed_ratio instead of positive_space_ratio.",
+        redirections=[("positive_space_ratio", "dashed_ratio")],
+    )
     def __init__(
         self,
         *args,
         dash_length=DEFAULT_DASH_LENGTH,
-        dash_spacing=None,
-        positive_space_ratio=0.5,
+        dashed_ratio=0.5,
         **kwargs,
     ):
+        self.dash_spacing = kwargs.pop(
+            "dash_spacing", None
+        )  # Unused param, remove with deprecation warning
         self.dash_length = dash_length
-        self.dash_spacing = (dash_spacing,)
-        self.positive_space_ratio = positive_space_ratio
+        self.dashed_ratio = dashed_ratio
         super().__init__(*args, **kwargs)
         dashes = DashedVMobject(
             self,
             num_dashes=self.calculate_num_dashes(),
-            positive_space_ratio=positive_space_ratio,
+            dashed_ratio=dashed_ratio,
         )
         self.clear_points()
         self.add(*dashes)
 
     def calculate_num_dashes(self) -> int:
         """Returns the number of dashes in the dashed line.
 
@@ -1112,22 +1149,18 @@
         --------
         ::
 
             >>> DashedLine().calculate_num_dashes()
             20
         """
 
-        try:
-            full_length = self.dash_length / self.positive_space_ratio
-            return int(np.ceil(self.get_length() / full_length))
-        except ZeroDivisionError:
-            return 1
-
-    def calculate_positive_space_ratio(self):
-        return fdiv(self.dash_length, self.dash_length + self.dash_spacing)
+        # Minimum number of dashes has to be 2
+        return max(
+            2, int(np.ceil((self.get_length() / self.dash_length) * self.dashed_ratio))
+        )
 
     def get_start(self) -> np.ndarray:
         """Returns the start point of the line.
 
         Examples
         --------
         ::
@@ -1145,15 +1178,15 @@
         """Returns the end point of the line.
 
         Examples
         --------
         ::
 
             >>> DashedLine().get_end()
-            array([0.99871795, 0.        , 0.        ])
+            array([1., 0., 0.])
         """
 
         if len(self.submobjects) > 0:
             return self.submobjects[-1].get_end()
         else:
             return super().get_end()
 
@@ -1174,15 +1207,15 @@
         """Returns the point of the last handle.
 
         Examples
         --------
         ::
 
             >>> DashedLine().get_last_handle()
-            array([0.98205128, 0.        , 0.        ])
+            array([0.98333333, 0.        , 0.        ])
         """
 
         return self.submobjects[-1].get_points()[-2]
 
 
 class TangentLine(Line):
     """Constructs a line tangent to a :class:`~.VMobject` at a specific point.
```

### Comparing `manim-0.8.0/manim/mobject/graph.py` & `manim-0.9.0/manim/mobject/graph.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/logo.py` & `manim-0.9.0/manim/mobject/logo.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/matrix.py` & `manim-0.9.0/manim/mobject/matrix.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/mobject.py` & `manim-0.9.0/manim/mobject/mobject.py`

 * *Files 1% similar despite different names*

```diff
@@ -2429,23 +2429,28 @@
             for submob in self.submobjects:
                 submob.shuffle(recursive=True)
         random.shuffle(self.submobjects)
 
     def invert(self, recursive=False):
         """Inverts the list of :attr:`submobjects`.
 
+        Parameters
+        ----------
+        recursive
+            If ``True``, all submobject lists of this mobject's family are inverted.
+
         Examples
         --------
 
         .. manim:: InvertSumobjectsExample
 
             class InvertSumobjectsExample(Scene):
                 def construct(self):
-                    s= VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
-                    s2= s.copy()
+                    s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
+                    s2 = s.copy()
                     s2.invert()
                     s2.shift(DOWN)
                     self.play(Write(s), Write(s2))
         """
         if recursive:
             for submob in self.submobjects:
                 submob.invert(recursive=True)
@@ -2605,17 +2610,14 @@
             self.points = path_func(mobject1.points, mobject2.points, alpha)
         self.interpolate_color(mobject1, mobject2, alpha)
         return self
 
     def interpolate_color(self, mobject1, mobject2, alpha):
         raise NotImplementedError("Please override in a child class.")
 
-    def pointwise_become_partial(self, mobject, a, b):
-        raise NotImplementedError("Please override in a child class.")
-
     def become(self, mobject: "Mobject", copy_submobjects: bool = True):
         """Edit points, colors and submobjects to be identical
         to another :class:`~.Mobject`
 
         Examples
         --------
         .. manim:: BecomeScene
@@ -2669,27 +2671,54 @@
             if self.has_no_points():
                 caller_name = sys._getframe(1).f_code.co_name
                 raise Exception(
                     f"Cannot call Mobject.{caller_name} for a Mobject with no points"
                 )
 
     # About z-index
-    def set_z_index(self, z_index_value: Union[int, float]):
+    def set_z_index(
+        self,
+        z_index_value: float,
+        family: bool = True,
+    ) -> "VMobject":
         """Sets the :class:`~.Mobject`'s :attr:`z_index` to the value specified in `z_index_value`.
 
         Parameters
         ----------
         z_index_value
             The new value of :attr:`z_index` set.
+        family
+            If ``True``, the :attr:`z_index` value of all submobjects is also set.
 
         Returns
         -------
         :class:`Mobject`
-            The Mobject itself, after :attr:`z_index` is set. (Returns `self`.)
+            The Mobject itself, after :attr:`z_index` is set. For chaining purposes. (Returns `self`.)
+
+        Examples
+        --------
+        .. manim:: SetZIndex
+            :save_last_frame:
+
+            class SetZIndex(Scene):
+                def construct(self):
+                    text = Text('z_index = 3', color = PURE_RED).shift(UP).set_z_index(3)
+                    square = Square(2, fill_opacity=1).set_z_index(2)
+                    tex = Tex(r'zIndex = 1', color = PURE_BLUE).shift(DOWN).set_z_index(1)
+                    circle = Circle(radius = 1.7, color = GREEN, fill_opacity = 1) # z_index = 0
+
+                    # Displaying order is now defined by z_index values
+                    self.add(text)
+                    self.add(square)
+                    self.add(tex)
+                    self.add(circle)
         """
+        if family:
+            for submob in self.submobjects:
+                submob.set_z_index(z_index_value, family=family)
         self.z_index = z_index_value
         return self
 
     def set_z_index_by_z_coordinate(self):
         """Sets the :class:`~.Mobject`'s z coordinate to the value of :attr:`z_index`.
 
         Returns
```

### Comparing `manim-0.8.0/manim/mobject/mobject_update_utils.py` & `manim-0.9.0/manim/mobject/mobject_update_utils.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/number_line.py` & `manim-0.9.0/manim/mobject/number_line.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,27 +1,33 @@
 """Mobject representing a number line."""
 
 __all__ = ["NumberLine", "UnitInterval", "NumberLineOld"]
 
 import operator as op
+from typing import TYPE_CHECKING, Dict, Union
 
 import numpy as np
 
+from manim.mobject.svg.tex_mobject import MathTex, Tex
+
 from .. import config
 from ..constants import *
 from ..mobject.geometry import Line
 from ..mobject.numbers import DecimalNumber
 from ..mobject.types.vectorized_mobject import VGroup
 from ..utils.bezier import interpolate
 from ..utils.color import LIGHT_GREY
 from ..utils.config_ops import merge_dicts_recursively
 from ..utils.deprecation import deprecated
 from ..utils.simple_functions import fdiv
 from ..utils.space_ops import normalize
 
+if TYPE_CHECKING:
+    from manim.mobject.mobject import Mobject
+
 
 class NumberLine(Line):
     """Creates a number line with tick marks. Number ranges that include both negative and
     positive values will be generated from the 0 point, and may not include a tick at the min / max
     values as the tick locations are dependent on the step size.
 
     Parameters
@@ -336,15 +342,59 @@
         numbers = VGroup()
         for x in x_values:
             if x in excluding:
                 continue
             numbers.add(self.get_number_mobject(x, **kwargs))
         self.add(numbers)
         self.numbers = numbers
-        return numbers
+        return self
+
+    def add_labels(
+        self,
+        dict_values: Dict[float, Union[str, float, "Mobject"]],
+        direction=None,
+        buff=None,
+    ):
+        """Adds specifically positioned labels to the :class:`~.NumberLine` using a ``dict``."""
+        if direction is None:
+            direction = self.label_direction
+        if buff is None:
+            buff = self.line_to_number_buff
+
+        labels = VGroup()
+        for x, label in dict_values.items():
+
+            label = self.create_label_tex(label)
+            label.scale(self.number_scale_value)
+            label.next_to(self.number_to_point(x), direction=direction, buff=buff)
+            labels.add(label)
+
+        self.labels = labels
+        self.add(labels)
+        return self
+
+    @staticmethod
+    def create_label_tex(label_tex) -> "Mobject":
+        """Checks if the label is a ``float``, ``int`` or a ``str`` and creates a :class:`~.MathTex`/:class:`~.Tex` label accordingly.
+
+        Parameters
+        ----------
+        label_tex : The label to be compared against the above types.
+
+        Returns
+        -------
+        :class:`~.Mobject`
+            The label.
+        """
+
+        if isinstance(label_tex, float) or isinstance(label_tex, int):
+            label_tex = MathTex(label_tex)
+        elif isinstance(label_tex, str):
+            label_tex = Tex(label_tex)
+        return label_tex
 
     def decimal_places_from_step(self):
         step_as_str = str(self.x_step)
         if "." not in step_as_str:
             return 0
         return len(step_as_str.split(".")[-1])
```

### Comparing `manim-0.8.0/manim/mobject/numbers.py` & `manim-0.9.0/manim/mobject/numbers.py`

 * *Files 3% similar despite different names*

```diff
@@ -95,15 +95,15 @@
             else:
                 num_string = num_string[1:]
 
         self.add(*[SingleStringMathTex(char, **kwargs) for char in num_string])
 
         # Add non-numerical bits
         if self.show_ellipsis:
-            self.add(SingleStringMathTex("\\dots"))
+            self.add(SingleStringMathTex("\\dots", color=self.color))
 
         if num_string.startswith("-"):
             minus = self.submobjects[0]
             minus.next_to(self.submobjects[1], LEFT, buff=self.digit_to_digit_buff)
 
         if self.unit is not None:
             self.unit_sign = SingleStringMathTex(self.unit, color=self.color)
@@ -186,15 +186,18 @@
             ):
                 new_submobject.original_id = generated_id
 
         # Make sure last digit has constant height
         new_decimal.scale(self[-1].height / new_decimal[-1].height)
         new_decimal.move_to(self, self.edge_to_fix)
         new_decimal.match_style(self)
-        self.become(new_decimal)
+        old_family = self.get_family()
+        self.set_submobjects(new_decimal.submobjects)
+        for mobj in old_family:
+            mobj.clear_points()
 
         self.number = number
         return self
 
     def get_value(self):
         return self.number
 
@@ -311,14 +314,30 @@
                 subscript_label_var = 10
                 on_screen_subscript_var = Variable(subscript_label_var, "{a}_{i}").next_to(
                     on_screen_int_var, DOWN
                 )
                 self.play(Write(on_screen_subscript_var))
                 self.wait()
 
+    .. manim:: VariableExample
+
+        class VariableExample(Scene):
+            def construct(self):
+                start = 2.0
+
+                x_var = Variable(start, 'x', num_decimal_places=3)
+                sqr_var = Variable(start**2, 'x^2', num_decimal_places=3)
+                Group(x_var, sqr_var).arrange(DOWN)
+
+                sqr_var.add_updater(lambda v: v.tracker.set_value(x_var.tracker.get_value()**2))
+
+                self.add(x_var, sqr_var)
+                self.play(x_var.tracker.animate.set_value(5), run_time=2, rate_func=linear)
+                self.wait(0.1)
+
     """
 
     def __init__(
         self, var, label, var_type=DecimalNumber, num_decimal_places=2, **kwargs
     ):
 
         self.label = MathTex(label) if isinstance(label, str) else label
```

### Comparing `manim-0.8.0/manim/mobject/opengl_compatibility.py` & `manim-0.9.0/manim/mobject/opengl_compatibility.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/opengl_geometry.py` & `manim-0.9.0/manim/mobject/opengl_geometry.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 from ..mobject.mobject import Mobject
 from ..mobject.types.opengl_vectorized_mobject import (
     OpenGLDashedVMobject,
     OpenGLVGroup,
     OpenGLVMobject,
 )
 from ..utils.color import *
-from ..utils.deprecation import deprecated
+from ..utils.deprecation import deprecated_params
 from ..utils.iterables import adjacent_n_tuples, adjacent_pairs
 from ..utils.simple_functions import clip, fdiv
 from ..utils.space_ops import (
     angle_between_vectors,
     angle_of_vector,
     compass_directions,
     find_intersection,
@@ -521,39 +521,38 @@
         return self
 
     def set_length(self, length):
         self.scale(length / self.get_length())
 
 
 class OpenGLDashedLine(OpenGLLine):
+    @deprecated_params(
+        params="positive_space_ratio dash_spacing",
+        since="v0.9.0",
+        message="Use dashed_ratio instead of positive_space_ratio.",
+    )
     def __init__(
-        self, *args, dash_length=DEFAULT_DASH_LENGTH, positive_space_ratio=0.5, **kwargs
+        self, *args, dash_length=DEFAULT_DASH_LENGTH, dashed_ratio=0.5, **kwargs
     ):
+        # Simplify with removal of deprecation warning
+        self.dash_spacing = kwargs.pop("dash_spacing", None)  # Unused param
+        self.dashed_ratio = kwargs.pop("positive_space_ratio", None) or dashed_ratio
         self.dash_length = dash_length
-        self.positive_space_ratio = positive_space_ratio
         super().__init__(*args, **kwargs)
-        ps_ratio = self.positive_space_ratio
-        num_dashes = self.calculate_num_dashes(ps_ratio)
+        dashed_ratio = self.dashed_ratio
+        num_dashes = self.calculate_num_dashes(dashed_ratio)
         dashes = OpenGLDashedVMobject(
-            self, num_dashes=num_dashes, positive_space_ratio=ps_ratio
+            self, num_dashes=num_dashes, dashed_ratio=dashed_ratio
         )
         self.clear_points()
         self.add(*dashes)
 
-    def calculate_num_dashes(self, positive_space_ratio):
-        try:
-            full_length = self.dash_length / positive_space_ratio
-            return int(np.ceil(self.get_length() / full_length))
-        except ZeroDivisionError:
-            return 1
-
-    def calculate_positive_space_ratio(self):
-        return fdiv(
-            self.dash_length,
-            self.dash_length + self.dash_spacing,
+    def calculate_num_dashes(self, dashed_ratio):
+        return max(
+            2, int(np.ceil((self.get_length() / self.dash_length) * dashed_ratio))
         )
 
     def get_start(self):
         if len(self.submobjects) > 0:
             return self.submobjects[0].get_start()
         else:
             return OpenGLLine.get_start(self)
```

### Comparing `manim-0.8.0/manim/mobject/opengl_mobject.py` & `manim-0.9.0/manim/mobject/opengl_mobject.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,12 +1,14 @@
 import copy
 import itertools as it
 import random
 import sys
 from functools import wraps
+from math import ceil
+from typing import Iterable, Optional, Tuple, Union
 
 import moderngl
 import numpy as np
 from colour import Color
 
 from .. import config
 from ..constants import *
@@ -21,15 +23,20 @@
     make_even,
     resize_array,
     resize_preserving_order,
     resize_with_interpolation,
 )
 from ..utils.paths import straight_path
 from ..utils.simple_functions import get_parameters
-from ..utils.space_ops import angle_of_vector, rotation_matrix_transpose
+from ..utils.space_ops import (
+    angle_between_vectors,
+    angle_of_vector,
+    normalize,
+    rotation_matrix_transpose,
+)
 
 
 class OpenGLMobject:
     """
     Mathematical Object
     """
 
@@ -53,14 +60,15 @@
         texture_paths=None,
         depth_test=False,
         # If true, the mobject will not get rotated according to camera position
         is_fixed_in_frame=False,
         # Must match in attributes of vert shader
         # Event listener
         listen_to_events=False,
+        model_matrix=None,
         **kwargs,
     ):
 
         self.color = Color(color)
         self.opacity = opacity
         self.dim = dim  # TODO, get rid of this
         # Lighting parameters
@@ -76,17 +84,22 @@
         self.is_fixed_in_frame = is_fixed_in_frame
         # Must match in attributes of vert shader
         # Event listener
         self.listen_to_events = listen_to_events
 
         self.submobjects = []
         self.parents = []
+        self.parent = None
         self.family = [self]
         self.locked_data_keys = set()
         self.needs_new_bounding_box = True
+        if model_matrix is None:
+            self.model_matrix = np.eye(4)
+        else:
+            self.model_matrix = model_matrix
 
         self.init_data()
         self.init_uniforms()
         self.init_updaters()
         # self.init_event_listners()
         self.init_points()
         self.init_colors()
@@ -378,26 +391,34 @@
             return self.family
         else:
             return [self]
 
     def family_members_with_points(self):
         return [m for m in self.get_family() if m.has_points()]
 
-    def add(self, *mobjects):
+    def add(self, *mobjects, update_parent=False):
+        if update_parent:
+            assert len(mobjects) == 1, "Can't set multiple parents."
+            mobjects[0].parent = self
+
         if self in mobjects:
             raise Exception("Mobject cannot contain self")
         for mobject in mobjects:
             if mobject not in self.submobjects:
                 self.submobjects.append(mobject)
             if self not in mobject.parents:
                 mobject.parents.append(self)
         self.assemble_family()
         return self
 
-    def remove(self, *mobjects):
+    def remove(self, *mobjects, update_parent=False):
+        if update_parent:
+            assert len(mobjects) == 1, "Can't remove multiple parents."
+            mobjects[0].parent = None
+
         for mobject in mobjects:
             if mobject in self.submobjects:
                 self.submobjects.remove(mobject)
             if self in mobject.parents:
                 mobject.parents.remove(self)
         self.assemble_family()
         return self
@@ -415,14 +436,41 @@
         return self
 
     def set_submobjects(self, submobject_list):
         self.remove(*self.submobjects)
         self.add(*submobject_list)
         return self
 
+    def invert(self, recursive=False):
+        """Inverts the list of :attr:`submobjects`.
+
+        Parameters
+        ----------
+        recursive
+            If ``True``, all submobject lists of this mobject's family are inverted.
+
+        Examples
+        --------
+
+        .. manim:: InvertSumobjectsExample
+
+            class InvertSumobjectsExample(Scene):
+                def construct(self):
+                    s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
+                    s2 = s.copy()
+                    s2.invert()
+                    s2.shift(DOWN)
+                    self.play(Write(s), Write(s2))
+        """
+        if recursive:
+            for submob in self.submobjects:
+                submob.invert(recursive=True)
+        list.reverse(self.submobjects)
+        self.assemble_family()
+
     def digest_mobject_attrs(self):
         """
         Ensures all attributes which are mobjects are included
         in the submobjects list.
         """
         mobject_attrs = [
             x for x in list(self.__dict__.values()) if isinstance(x, OpenGLMobject)
@@ -437,56 +485,246 @@
             m2.next_to(m1, direction, **kwargs)
         if center:
             self.center()
         return self
 
     def arrange_in_grid(
         self,
-        n_rows=None,
-        n_cols=None,
-        buff=None,
-        h_buff=None,
-        v_buff=None,
-        buff_ratio=None,
-        h_buff_ratio=0.5,
-        v_buff_ratio=0.5,
-        aligned_edge=ORIGIN,
-        fill_rows_first=True,
-    ):
-        submobs = self.submobjects
-        if n_rows is None and n_cols is None:
-            n_rows = int(np.sqrt(len(submobs)))
-        if n_rows is None:
-            n_rows = len(submobs) // n_cols
-        if n_cols is None:
-            n_cols = len(submobs) // n_rows
-
-        if buff is not None:
-            h_buff = buff
-            v_buff = buff
+        rows: Optional[int] = None,
+        cols: Optional[int] = None,
+        buff: Union[float, Tuple[float, float]] = MED_SMALL_BUFF,
+        cell_alignment: np.ndarray = ORIGIN,
+        row_alignments: Optional[str] = None,  # "ucd"
+        col_alignments: Optional[str] = None,  # "lcr"
+        row_heights: Optional[Iterable[Optional[float]]] = None,
+        col_widths: Optional[Iterable[Optional[float]]] = None,
+        flow_order: str = "rd",
+        **kwargs,
+    ) -> "OpenGLMobject":
+        """Arrange submobjects in a grid.
+
+        Parameters
+        ----------
+        rows
+            The number of rows in the grid.
+        cols
+            The number of columns in the grid.
+        buff
+            The gap between grid cells. To specify a different buffer in the horizontal and
+            vertical directions, a tuple of two values can be given - ``(row, col)``.
+        cell_alignment
+            The way each submobject is aligned in its grid cell.
+        row_alignments
+            The vertical alignment for each row (top to bottom). Accepts the following characters: ``"u"`` -
+            up, ``"c"`` - center, ``"d"`` - down.
+        col_alignments
+            The horizontal alignment for each column (left to right). Accepts the following characters ``"l"`` - left,
+            ``"c"`` - center, ``"r"`` - right.
+        row_heights
+            Defines a list of heights for certain rows (top to bottom). If the list contains
+            ``None``, the corresponding row will fit its height automatically based
+            on the highest element in that row.
+        col_widths
+            Defines a list of widths for certain columns (left to right). If the list contains ``None``, the
+            corresponding column will fit its width automatically based on the widest element in that column.
+        flow_order
+            The order in which submobjects fill the grid. Can be one of the following values:
+            "rd", "dr", "ld", "dl", "ru", "ur", "lu", "ul". ("rd" -> fill rightwards then downwards)
+
+        Returns
+        -------
+        Mobject
+            The mobject.
+
+        NOTES
+        -----
+
+        If only one of ``cols`` and ``rows`` is set implicitly, the other one will be chosen big
+        enough to fit all submobjects. If neither is set, they will be chosen to be about the same,
+        tending towards ``cols`` > ``rows`` (simply because videos are wider than they are high).
+
+        If both ``cell_alignment`` and ``row_alignments`` / ``col_alignments`` are
+        defined, the latter has higher priority.
+
+
+        Raises
+        ------
+        ValueError
+            If ``rows`` and ``cols`` are too small to fit all submobjects.
+        ValueError
+            If :code:`cols`, :code:`col_alignments` and :code:`col_widths` or :code:`rows`,
+            :code:`row_alignments` and :code:`row_heights` have mismatching sizes.
+
+        Examples
+        --------
+        .. manim:: ExampleBoxes
+            :save_last_frame:
+
+            class ExampleBoxes(Scene):
+                def construct(self):
+                    boxes=VGroup(*[Square() for s in range(0,6)])
+                    boxes.arrange_in_grid(rows=2, buff=0.1)
+                    self.add(boxes)
+
+
+        .. manim:: ArrangeInGrid
+            :save_last_frame:
+
+            class ArrangeInGrid(Scene):
+                def construct(self):
+                    #Add some numbered boxes:
+                    np.random.seed(3)
+                    boxes = VGroup(*[
+                        Rectangle(WHITE, np.random.random()+.5, np.random.random()+.5).add(Text(str(i+1)).scale(0.5))
+                        for i in range(22)
+                    ])
+                    self.add(boxes)
+
+                    boxes.arrange_in_grid(
+                        buff=(0.25,0.5),
+                        col_alignments="lccccr",
+                        row_alignments="uccd",
+                        col_widths=[2, *[None]*4, 2],
+                        flow_order="dr"
+                    )
+
+
+        """
+        from .geometry import Line
+
+        mobs = self.submobjects.copy()
+        start_pos = self.get_center()
+
+        # get cols / rows values if given (implicitly)
+        def init_size(num, alignments, sizes):
+            if num is not None:
+                return num
+            if alignments is not None:
+                return len(alignments)
+            if sizes is not None:
+                return len(sizes)
+
+        cols = init_size(cols, col_alignments, col_widths)
+        rows = init_size(rows, row_alignments, row_heights)
+
+        # calculate rows cols
+        if rows is None and cols is None:
+            cols = ceil(np.sqrt(len(mobs)))
+            # make the grid as close to quadratic as possible.
+            # choosing cols first can results in cols>rows.
+            # This is favored over rows>cols since in general
+            # the sceene is wider than high.
+        if rows is None:
+            rows = ceil(len(mobs) / cols)
+        if cols is None:
+            cols = ceil(len(mobs) / rows)
+        if rows * cols < len(mobs):
+            raise ValueError("Too few rows and columns to fit all submobjetcs.")
+        # rows and cols are now finally valid.
+
+        if isinstance(buff, tuple):
+            buff_x = buff[0]
+            buff_y = buff[1]
         else:
-            if buff_ratio is not None:
-                v_buff_ratio = buff_ratio
-                h_buff_ratio = buff_ratio
-            if h_buff is None:
-                h_buff = h_buff_ratio * self[0].get_width()
-            if v_buff is None:
-                v_buff = v_buff_ratio * self[0].get_height()
-
-        x_unit = h_buff + max([sm.get_width() for sm in submobs])
-        y_unit = v_buff + max([sm.get_height() for sm in submobs])
-
-        for index, sm in enumerate(submobs):
-            if fill_rows_first:
-                x, y = index % n_cols, index // n_cols
-            else:
-                x, y = index // n_rows, index % n_rows
-            sm.move_to(ORIGIN, aligned_edge)
-            sm.shift(x * x_unit * RIGHT + y * y_unit * DOWN)
-        self.center()
+            buff_x = buff_y = buff
+
+        # Initialize alignments correctly
+        def init_alignments(alignments, num, mapping, name, dir):
+            if alignments is None:
+                # Use cell_alignment as fallback
+                return [cell_alignment * dir] * num
+            if len(alignments) != num:
+                raise ValueError("{}_alignments has a mismatching size.".format(name))
+            alignments = list(alignments)
+            for i in range(num):
+                alignments[i] = mapping[alignments[i]]
+            return alignments
+
+        row_alignments = init_alignments(
+            row_alignments, rows, {"u": UP, "c": ORIGIN, "d": DOWN}, "row", RIGHT
+        )
+        col_alignments = init_alignments(
+            col_alignments, cols, {"l": LEFT, "c": ORIGIN, "r": RIGHT}, "col", UP
+        )
+        # Now row_alignment[r] + col_alignment[c] is the alignment in cell [r][c]
+
+        mapper = {
+            "dr": lambda r, c: (rows - r - 1) + c * rows,
+            "dl": lambda r, c: (rows - r - 1) + (cols - c - 1) * rows,
+            "ur": lambda r, c: r + c * rows,
+            "ul": lambda r, c: r + (cols - c - 1) * rows,
+            "rd": lambda r, c: (rows - r - 1) * cols + c,
+            "ld": lambda r, c: (rows - r - 1) * cols + (cols - c - 1),
+            "ru": lambda r, c: r * cols + c,
+            "lu": lambda r, c: r * cols + (cols - c - 1),
+        }
+        if flow_order not in mapper:
+            raise ValueError(
+                'flow_order must be one of the following values: "dr", "rd", "ld" "dl", "ru", "ur", "lu", "ul".'
+            )
+        flow_order = mapper[flow_order]
+
+        # Reverse row_alignments and row_heights. Necessary since the
+        # grid filling is handled bottom up for simplicity reasons.
+        def reverse(maybe_list):
+            if maybe_list is not None:
+                maybe_list = list(row_alignments)
+                maybe_list.reverse()
+                return maybe_list
+
+        row_alignments = reverse(row_alignments)
+        row_heights = reverse(row_heights)
+
+        placeholder = OpenGLMobject()
+        # Used to fill up the grid temporarily, doesn't get added to the scene.
+        # In this case a Mobject is better than None since it has width and height
+        # properties of 0.
+
+        mobs.extend([placeholder] * (rows * cols - len(mobs)))
+        grid = [[mobs[flow_order(r, c)] for c in range(cols)] for r in range(rows)]
+
+        measured_heigths = [
+            max([grid[r][c].height for c in range(cols)]) for r in range(rows)
+        ]
+        measured_widths = [
+            max([grid[r][c].width for r in range(rows)]) for c in range(cols)
+        ]
+
+        # Initialize row_heights / col_widths correctly using measurements as fallback
+        def init_sizes(sizes, num, measures, name):
+            if sizes is None:
+                sizes = [None] * num
+            if len(sizes) != num:
+                raise ValueError("{} has a mismatching size.".format(name))
+            return [
+                sizes[i] if sizes[i] is not None else measures[i] for i in range(num)
+            ]
+
+        heights = init_sizes(row_heights, rows, measured_heigths, "row_heights")
+        widths = init_sizes(col_widths, cols, measured_widths, "col_widths")
+
+        x, y = 0, 0
+        for r in range(rows):
+            x = 0
+            for c in range(cols):
+                if grid[r][c] is not placeholder:
+                    alignment = row_alignments[r] + col_alignments[c]
+                    line = Line(
+                        x * RIGHT + y * UP,
+                        (x + widths[c]) * RIGHT + (y + heights[r]) * UP,
+                    )
+                    # Use a mobject to avoid rewriting align inside
+                    # box code that Mobject.move_to(Mobject) already
+                    # includes.
+
+                    grid[r][c].move_to(line, alignment)
+                x += widths[c] + buff_x
+            y += heights[r] + buff_y
+
+        self.move_to(start_pos)
         return self
 
     def get_grid(self, n_rows, n_cols, height=None, **kwargs):
         """
         Returns a new mobject containing multiple copies of this one
         arranged in a grid
         """
@@ -504,14 +742,15 @@
         return self
 
     def shuffle(self, recurse=False):
         if recurse:
             for submob in self.submobjects:
                 submob.shuffle(recurse=True)
         random.shuffle(self.submobjects)
+        self.assemble_family()
         return self
 
     # Copying
 
     def copy(self, shallow: bool = False):
         """Copies the mobject.
 
@@ -768,14 +1007,25 @@
         def R3_func(point):
             x, y, z = point
             xy_complex = function(complex(x, y))
             return [xy_complex.real, xy_complex.imag, z]
 
         return self.apply_function(R3_func)
 
+    def hierarchical_model_matrix(self):
+        if self.parent is None:
+            return self.model_matrix
+
+        model_matrices = [self.model_matrix]
+        current_object = self
+        while current_object.parent is not None:
+            model_matrices.append(current_object.parent.model_matrix)
+            current_object = current_object.parent
+        return np.linalg.multi_dot(list(reversed(model_matrices)))
+
     def wag(self, direction=RIGHT, axis=DOWN, wag_factor=1.0):
         for mob in self.family_members_with_points():
             alphas = np.dot(mob.get_points(), np.transpose(axis))
             alphas -= min(alphas)
             alphas /= max(alphas)
             alphas = alphas ** wag_factor
             mob.set_points(
@@ -957,27 +1207,32 @@
     def surround(self, mobject, dim_to_match=0, stretch=False, buff=MED_SMALL_BUFF):
         self.replace(mobject, dim_to_match, stretch)
         length = mobject.length_over_dim(dim_to_match)
         self.scale((length + buff) / length)
         return self
 
     def put_start_and_end_on(self, start, end):
-        # TODO, this doesn't currently work in 3d
         curr_start, curr_end = self.get_start_and_end()
         curr_vect = curr_end - curr_start
         if np.all(curr_vect == 0):
             raise Exception("Cannot position endpoints of closed loop")
-        target_vect = end - start
+        target_vect = np.array(end) - np.array(start)
+        axis = (
+            normalize(np.cross(curr_vect, target_vect))
+            if np.linalg.norm(np.cross(curr_vect, target_vect)) != 0
+            else OUT
+        )
         self.scale(
             np.linalg.norm(target_vect) / np.linalg.norm(curr_vect),
             about_point=curr_start,
         )
         self.rotate(
-            angle_of_vector(target_vect) - angle_of_vector(curr_vect),
+            angle_between_vectors(curr_vect, target_vect),
             about_point=curr_start,
+            axis=axis,
         )
         self.shift(start - curr_start)
         return self
 
     # Color functions
 
     def set_rgba_array(self, color=None, opacity=None, name="rgbas", recurse=True):
@@ -1065,15 +1320,15 @@
         return self
 
     # Background rectangle
 
     def add_background_rectangle(self, color=None, opacity=0.75, **kwargs):
         # TODO, this does not behave well when the mobject has points,
         # since it gets displayed on top
-        from manimlib.mobject.shape_matchers import BackgroundRectangle
+        from ..mobject.shape_matchers import BackgroundRectangle
 
         self.background_rectangle = BackgroundRectangle(
             self, color=color, fill_opacity=opacity, **kwargs
         )
         self.add_to_back(self.background_rectangle)
         return self
 
@@ -1696,49 +1951,75 @@
     def set_location(self, new_loc):
         self.set_points(np.array(new_loc, ndmin=2, dtype=float))
 
 
 class _AnimationBuilder:
     def __init__(self, mobject):
         self.mobject = mobject
-        self.overridden_animation = None
         self.mobject.generate_target()
+
+        self.overridden_animation = None
         self.is_chaining = False
         self.methods = []
 
+        # Whether animation args can be passed
+        self.cannot_pass_args = False
+        self.anim_args = {}
+
+    def __call__(self, **kwargs):
+        if self.cannot_pass_args:
+            raise ValueError(
+                "Animation arguments must be passed before accessing methods and can only be passed once"
+            )
+
+        self.anim_args = kwargs
+        self.cannot_pass_args = True
+
+        return self
+
     def __getattr__(self, method_name):
         method = getattr(self.mobject.target, method_name)
         self.methods.append(method)
         has_overridden_animation = hasattr(method, "_override_animate")
 
         if (self.is_chaining and has_overridden_animation) or self.overridden_animation:
             raise NotImplementedError(
                 "Method chaining is currently not supported for "
                 "overridden animations"
             )
 
         def update_target(*method_args, **method_kwargs):
             if has_overridden_animation:
                 self.overridden_animation = method._override_animate(
-                    self.mobject, *method_args, **method_kwargs
+                    self.mobject,
+                    *method_args,
+                    anim_args=self.anim_args,
+                    **method_kwargs,
                 )
             else:
                 method(*method_args, **method_kwargs)
             return self
 
         self.is_chaining = True
+        self.cannot_pass_args = True
+
         return update_target
 
     def build(self):
         from ..animation.transform import _MethodAnimation
 
         if self.overridden_animation:
-            return self.overridden_animation
+            anim = self.overridden_animation
+        else:
+            anim = _MethodAnimation(self.mobject, self.methods)
+
+        for attr, value in self.anim_args.items():
+            setattr(anim, attr, value)
 
-        return _MethodAnimation(self.mobject, self.methods)
+        return anim
 
 
 def override_animate(method):
     def decorator(animation_method):
         method._override_animate = animation_method
         return animation_method
```

### Comparing `manim-0.8.0/manim/mobject/opengl_three_dimensions.py` & `manim-0.9.0/manim/mobject/opengl_three_dimensions.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/polyhedra.py` & `manim-0.9.0/manim/mobject/polyhedra.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/probability.py` & `manim-0.9.0/manim/mobject/probability.py`

 * *Files 6% similar despite different names*

```diff
@@ -263,27 +263,29 @@
         self.y_axis_label_height = y_axis_label_height
         self.max_value = max_value
         self.bar_colors = bar_colors
         self.bar_fill_opacity = bar_fill_opacity
         self.bar_stroke_width = bar_stroke_width
         self.bar_names = bar_names
         self.bar_label_scale_val = bar_label_scale_val
+        self.total_bar_width = width
+        self.total_bar_height = height
 
         if self.max_value is None:
             self.max_value = max(values)
 
-        self.add_axes(width, height)
-        self.add_bars(values, width, height)
+        self.add_axes()
+        self.add_bars(values)
         self.center()
 
-    def add_axes(self, width, height):
-        x_axis = Line(self.tick_width * LEFT / 2, width * RIGHT)
-        y_axis = Line(MED_LARGE_BUFF * DOWN, height * UP)
+    def add_axes(self):
+        x_axis = Line(self.tick_width * LEFT / 2, self.total_bar_width * RIGHT)
+        y_axis = Line(MED_LARGE_BUFF * DOWN, self.total_bar_height * UP)
         ticks = VGroup()
-        heights = np.linspace(0, height, self.n_ticks + 1)
+        heights = np.linspace(0, self.total_bar_height, self.n_ticks + 1)
         values = np.linspace(0, self.max_value, self.n_ticks + 1)
         for y, _value in zip(heights, values):
             tick = Line(LEFT, RIGHT)
             tick.width = self.tick_width
             tick.move_to(y * UP)
             ticks.add(tick)
         y_axis.add(ticks)
@@ -297,20 +299,20 @@
                 label = MathTex(str(np.round(value, 2)))
                 label.height = self.y_axis_label_height
                 label.next_to(tick, LEFT, SMALL_BUFF)
                 labels.add(label)
             self.y_axis_labels = labels
             self.add(labels)
 
-    def add_bars(self, values, width, height):
-        buff = float(width) / (2 * len(values) + 1)
+    def add_bars(self, values):
+        buff = float(self.total_bar_width) / (2 * len(values) + 1)
         bars = VGroup()
         for i, value in enumerate(values):
             bar = Rectangle(
-                height=(value / self.max_value) * height,
+                height=(value / self.max_value) * self.total_bar_height,
                 width=buff,
                 stroke_width=self.bar_stroke_width,
                 fill_opacity=self.bar_fill_opacity,
             )
             bar.move_to((2 * i + 1) * buff * RIGHT, DOWN + LEFT)
             bars.add(bar)
         bars.set_color_by_gradient(*self.bar_colors)
@@ -325,9 +327,9 @@
         self.add(bars, bar_labels)
         self.bars = bars
         self.bar_labels = bar_labels
 
     def change_bar_values(self, values):
         for bar, value in zip(self.bars, values):
             bar_bottom = bar.get_bottom()
-            bar.stretch_to_fit_height((value / self.max_value) * self.height)
+            bar.stretch_to_fit_height((value / self.max_value) * self.total_bar_height)
             bar.move_to(bar_bottom, DOWN)
```

### Comparing `manim-0.8.0/manim/mobject/shape_matchers.py` & `manim-0.9.0/manim/mobject/shape_matchers.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/svg/brace.py` & `manim-0.9.0/manim/mobject/svg/brace.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/svg/code_mobject.py` & `manim-0.9.0/manim/mobject/svg/code_mobject.py`

 * *Files 0% similar despite different names*

```diff
@@ -42,14 +42,51 @@
     .. WARNING::
 
         Using a :class:`.Transform` on text with leading whitespace (and in
         this particular case: code) can look
         `weird <https://github.com/3b1b/manim/issues/1067>`_. Consider using
         :meth:`remove_invisible_chars` to resolve this issue.
 
+    Examples
+    --------
+
+    Normal usage::
+
+        listing = Code(
+            "helloworldcpp.cpp",
+            tab_width=4,
+            background_stroke_width=1,
+            background_stroke_color=WHITE,
+            insert_line_no=True,
+            style=Code.styles_list[15],
+            background="window",
+            language="cpp",
+        )
+
+    We can also render code passed as a string (but note that
+    the language has to be specified in this case):
+
+    .. manim:: CodeFromString
+        :save_last_frame:
+
+        class CodeFromString(Scene):
+            def construct(self):
+                code = '''from manim import Scene, Square
+
+        class FadeInSquare(Scene):
+            def construct(self):
+                s = Square()
+                self.play(FadeIn(s))
+                self.play(s.animate.scale(2))
+                self.wait()
+        '''
+                rendered_code = Code(code=code, tab_width=4, background="window",
+                                    language="Python", font="Monospace")
+                self.add(rendered_code)
+
     Parameters
     ----------
     file_name : :class:`str`
         Name of the code file to display.
     code : :class:`str`
         If ``file_name`` is not specified, a code string can be
         passed directly.
@@ -97,50 +134,14 @@
         The background of the code listing.
     line_numbers : :class:`~.Paragraph`
         The line numbers for the code listing. Empty, if
         ``insert_line_no=False`` has been specified.
     code : :class:`~.Paragraph`
         The highlighted code.
 
-    Examples
-    --------
-    Normal usage::
-
-        listing = Code(
-            "helloworldcpp.cpp",
-            tab_width=4,
-            background_stroke_width=1,
-            background_stroke_color=WHITE,
-            insert_line_no=True,
-            style=Code.styles_list[15],
-            background="window",
-            language="cpp",
-        )
-
-    We can also render code passed as a string (but note that
-    the language has to be specified in this case):
-
-    .. manim:: CodeFromString
-        :save_last_frame:
-
-        class CodeFromString(Scene):
-            def construct(self):
-                code = '''from manim import Scene, Square
-
-        class FadeInSquare(Scene):
-            def construct(self):
-                s = Square()
-                self.play(FadeIn(s))
-                self.play(s.animate.scale(2))
-                self.wait()
-        '''
-                rendered_code = Code(code=code, tab_width=4, background="window",
-                                    language="Python", font="Monospace")
-                self.add(rendered_code)
-
     """
 
     # tuples in the form (name, aliases, filetypes, mimetypes)
     # 'language' is aliases or short names
     # For more information about pygments.lexers visit https://pygments.org/docs/lexers/
     # from pygments.lexers import get_all_lexers
     # all_lexers = get_all_lexers()
```

### Comparing `manim-0.8.0/manim/mobject/svg/opengl_svg_mobject.py` & `manim-0.9.0/manim/mobject/svg/opengl_svg_mobject.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/svg/opengl_svg_path.py` & `manim-0.9.0/manim/mobject/svg/opengl_svg_path.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/svg/opengl_tex_mobject.py` & `manim-0.9.0/manim/mobject/svg/opengl_tex_mobject.py`

 * *Files 2% similar despite different names*

```diff
@@ -159,16 +159,14 @@
 __all__ = [
     "OpenGLTexSymbol",
     "OpenGLSingleStringMathTex",
     "OpenGLMathTex",
     "OpenGLTex",
     "OpenGLBulletedList",
     "OpenGLTitle",
-    "OpenGLTexMobject",
-    "OpenGLTextMobject",
 ]
 
 
 import operator as op
 from functools import reduce
 
 from ... import config
@@ -595,19 +593,7 @@
             underline.next_to(self, DOWN, buff=self.underline_buff)
             if self.match_underline_width_to_text:
                 underline.match_width(self)
             else:
                 underline.width = underline_width
             self.add(underline)
             self.underline = underline
-
-
-@deprecated(until="v0.7.0", replacement="MathTex")
-class OpenGLTexMobject(OpenGLMathTex):
-    def __init__(self, *tex_strings, **kwargs):
-        MathTex.__init__(self, *tex_strings, **kwargs)
-
-
-@deprecated(until="v0.7.0", replacement="Tex")
-class OpenGLTextMobject(OpenGLTex):
-    def __init__(self, *text_parts, **kwargs):
-        Tex.__init__(self, *text_parts, **kwargs)
```

### Comparing `manim-0.8.0/manim/mobject/svg/opengl_text_mobject.py` & `manim-0.9.0/manim/mobject/svg/opengl_text_mobject.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/svg/style_utils.py` & `manim-0.9.0/manim/mobject/svg/style_utils.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/svg/svg_mobject.py` & `manim-0.9.0/manim/mobject/svg/svg_mobject.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 import string
 import warnings
 from typing import Dict, List
 from xml.dom.minidom import Element as MinidomElement
 from xml.dom.minidom import parse as minidom_parse
 
 import numpy as np
+from colour import Color
 
 from ... import config, logger
 from ...constants import *
 from ...mobject.geometry import Circle, Line, Rectangle, RoundedRectangle
 from ...mobject.types.vectorized_mobject import VMobject
 from ..opengl_compatibility import ConvertToOpenGL
 from .style_utils import cascade_element_style, parse_style
@@ -247,15 +248,15 @@
             A path with potentially multiple path commands to create a shape.
 
         style : :class:`dict`
             Style specification, using the SVG names for properties.
 
         Returns
         -------
-        VMobjectFromSVGPathstring
+        SVGPathMobject
             A VMobject from the given path string, or d attribute.
         """
         return SVGPathMobject(
             path_string, **self.path_string_config, **parse_style(style)
         )
 
     def attribute_to_float(self, attr):
@@ -450,15 +451,15 @@
             An SVG polygon element.
 
         style : :class:`dict`
             Style specification, using the SVG names for properties.
 
         Returns
         -------
-        VMobjectFromSVGPathstring
+        SVGPathMobject
             A VMobject representing the polygon.
         """
         # This seems hacky... yes it is.
         path_string = polygon_element.getAttribute("points").lstrip()
         for digit in string.digits:
             path_string = path_string.replace(" " + digit, " L" + digit)
         path_string = "M" + path_string
```

### Comparing `manim-0.8.0/manim/mobject/svg/svg_path.py` & `manim-0.9.0/manim/mobject/svg/svg_path.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 """Mobjects generated from an SVG pathstring."""
 
 
-__all__ = ["SVGPathMobject", "string_to_numbers", "VMobjectFromSVGPathstring"]
+__all__ = ["SVGPathMobject", "string_to_numbers"]
 
 
 import re
 from math import *
 from typing import List
 
 import numpy as np
@@ -463,13 +463,7 @@
         """A simple getter for the path's ``d`` attribute."""
         return self.path_string
 
     def start_new_path(self, point):
         self.current_path_start = point
         super().start_new_path(point)
         return self
-
-
-@deprecated(until="v0.7.0", replacement="SVGPathMobject")
-class VMobjectFromSVGPathstring(SVGPathMobject):
-    def __init__(self, *args, **kwargs):
-        super().__init__(self, *args, **kwargs)
```

### Comparing `manim-0.8.0/manim/mobject/svg/tex_mobject.py` & `manim-0.9.0/manim/mobject/svg/tex_mobject.py`

 * *Files 3% similar despite different names*

```diff
@@ -249,20 +249,19 @@
             [] if substrings_to_isolate is None else substrings_to_isolate
         )
         self.tex_to_color_map = tex_to_color_map
         if self.tex_to_color_map is None:
             self.tex_to_color_map = {}
         self.tex_environment = tex_environment
         self.brace_notation_split_occurred = False
-        tex_strings = self.break_up_tex_strings(tex_strings)
-        self.tex_strings = tex_strings
+        self.tex_strings = self.break_up_tex_strings(tex_strings)
         try:
             SingleStringMathTex.__init__(
                 self,
-                self.arg_separator.join(tex_strings),
+                self.arg_separator.join(self.tex_strings),
                 tex_environment=self.tex_environment,
                 tex_template=self.tex_template,
                 **kwargs,
             )
             self.break_up_by_substrings()
         except ValueError as compilation_error:
             if self.brace_notation_split_occurred:
@@ -330,28 +329,22 @@
             new_index = (
                 curr_index + num_submobs + len("".join(self.arg_separator.split()))
             )
             if num_submobs == 0:
                 # For cases like empty tex_strings, we want the corresponding
                 # part of the whole MathTex to be a VectorizedPoint
                 # positioned in the right part of the MathTex
-                sub_tex_mob.submobjects = [VectorizedPoint()]
-                if config.renderer == "opengl":
-                    sub_tex_mob.assemble_family()
+                sub_tex_mob.set_submobjects([VectorizedPoint()])
                 last_submob_index = min(curr_index, len(self.submobjects) - 1)
                 sub_tex_mob.move_to(self.submobjects[last_submob_index], RIGHT)
             else:
-                sub_tex_mob.submobjects = self.submobjects[curr_index:new_index]
-                if config.renderer == "opengl":
-                    sub_tex_mob.assemble_family()
+                sub_tex_mob.set_submobjects(self.submobjects[curr_index:new_index])
             new_submobjects.append(sub_tex_mob)
             curr_index = new_index
-        self.submobjects = new_submobjects
-        if config.renderer == "opengl":
-            self.assemble_family()
+        self.set_submobjects(new_submobjects)
         return self
 
     def get_parts_by_tex(self, tex, substring=True, case_sensitive=True):
         def test(tex1, tex2):
             if not case_sensitive:
                 tex1 = tex1.lower()
                 tex2 = tex2.lower()
```

### Comparing `manim-0.8.0/manim/mobject/svg/text_mobject.py` & `manim-0.9.0/manim/mobject/svg/text_mobject.py`

 * *Files 0% similar despite different names*

```diff
@@ -471,15 +471,18 @@
             width=width,
             should_center=should_center,
             unpack_groups=unpack_groups,
             **kwargs,
         )
         self.text = text
         if self.disable_ligatures:
-            self.submobjects = [*self.gen_chars()]
+            if config.renderer == "opengl":
+                self.set_submobjects(self.gen_chars())
+            else:
+                self.submobjects = [*self.gen_chars()]
         self.chars = self.get_group_class()(*self.submobjects)
         self.text = text_without_tabs.replace(" ", "").replace("\n", "")
         if config.renderer == "opengl":
             nppc = self.n_points_per_curve
         else:
             nppc = self.n_points_per_cubic_curve
         for each in self:
```

### Comparing `manim-0.8.0/manim/mobject/three_d_utils.py` & `manim-0.9.0/manim/mobject/three_d_utils.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/three_dimensions.py` & `manim-0.9.0/manim/mobject/three_dimensions.py`

 * *Files 14% similar despite different names*

```diff
@@ -10,81 +10,101 @@
     "Cone",
     "Arrow3D",
     "Cylinder",
     "Line3D",
     "Torus",
 ]
 
+
+from typing import *
+
 import numpy as np
+from colour import Color
 
 from manim.mobject.opengl_compatibility import ConvertToOpenGL
 
 from ..constants import *
 from ..mobject.geometry import Circle, Square
 from ..mobject.mobject import *
 from ..mobject.opengl_mobject import OpenGLMobject
 from ..mobject.types.vectorized_mobject import VGroup, VMobject
 from ..utils.color import *
+from ..utils.deprecation import deprecated_params
 from ..utils.iterables import tuplify
 from ..utils.space_ops import normalize, z_to_vector
 
 
 class ThreeDVMobject(VMobject, metaclass=ConvertToOpenGL):
     def __init__(self, shade_in_3d=True, **kwargs):
         super().__init__(shade_in_3d=shade_in_3d, **kwargs)
 
 
 class ParametricSurface(VGroup):
     """Creates a Parametric Surface
 
+    Parameters
+    ----------
+    func :
+        The function that defines the surface.
+    u_range :
+        The range of the ``u`` variable: ``(u_min, u_max)``.
+    v_range :
+        The range of the ``v`` variable: ``(v_min, v_max)``.
+    resolution :
+        The number of samples taken of the surface. A tuple
+        can be used to define different resolutions for ``u`` and
+        ``v`` respectively.
+
     Examples
     --------
     .. manim:: ParaSurface
         :save_last_frame:
 
         class ParaSurface(ThreeDScene):
             def func(self, u, v):
                 return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])
 
             def construct(self):
                 axes = ThreeDAxes(x_range=[-4,4], x_length=8)
                 surface = ParametricSurface(
                     lambda u, v: axes.c2p(*self.func(u, v)),
-                    u_min=-PI,
-                    u_max=PI,
-                    v_min=0,
-                    v_max=TAU,
+                    u_range=[-PI, PI],
+                    v_range=[0, TAU]
                 )
                 self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
                 self.add(axes, surface)
     """
 
+    @deprecated_params(
+        params="u_min,u_max,v_min,v_max",
+        since="v0.9.0",
+        until="v0.10.0",
+        message="Use u_range and v_range instead.",
+    )
     def __init__(
         self,
-        func,
-        u_min=0,
-        u_max=1,
-        v_min=0,
-        v_max=1,
-        resolution=32,
-        surface_piece_config={},
-        fill_color=BLUE_D,
-        fill_opacity=1.0,
-        checkerboard_colors=[BLUE_D, BLUE_E],
-        stroke_color=LIGHT_GREY,
-        stroke_width=0.5,
-        should_make_jagged=False,
-        pre_function_handle_to_anchor_scale_factor=0.00001,
+        func: Callable[[float, float], np.ndarray],
+        u_range: Sequence[float] = [0, 1],
+        v_range: Sequence[float] = [0, 1],
+        resolution: Sequence[int] = 32,
+        surface_piece_config: dict = {},
+        fill_color: "Color" = BLUE_D,
+        fill_opacity: float = 1.0,
+        checkerboard_colors: Sequence["Color"] = [BLUE_D, BLUE_E],
+        stroke_color: "Color" = LIGHT_GREY,
+        stroke_width: float = 0.5,
+        should_make_jagged: bool = False,
+        pre_function_handle_to_anchor_scale_factor: float = 0.00001,
         **kwargs
-    ):
+    ) -> None:
+        self.u_min = kwargs.pop("u_min", None) or u_range[0]
+        self.u_max = kwargs.pop("u_max", None) or u_range[1]
+        self.v_min = kwargs.pop("v_min", None) or v_range[0]
+        self.v_max = kwargs.pop("v_max", None) or v_range[1]
         super().__init__(**kwargs)
-        self.u_min = u_min
-        self.u_max = u_max
-        self.v_min = v_min
-        self.v_max = v_max
         self.resolution = resolution
         self.surface_piece_config = surface_piece_config
         self.fill_color = fill_color
         self.fill_opacity = fill_opacity
         self.checkerboard_colors = checkerboard_colors
         self.stroke_color = stroke_color
         self.stroke_width = stroke_width
@@ -151,14 +171,89 @@
     def set_fill_by_checkerboard(self, *colors, opacity=None):
         n_colors = len(colors)
         for face in self:
             c_index = (face.u_index + face.v_index) % n_colors
             face.set_fill(colors[c_index], opacity=opacity)
         return self
 
+    def set_fill_by_value(self, axes: "Mobject", colors: Union[Iterable[Color], Color]):
+        """Sets the color of each mobject of a parametric surface to a color relative to its z-value
+
+        Parameters
+        ----------
+        axes :
+            The axes for the parametric surface, which will be used to map z-values to colors.
+        colors :
+            A list of colors, ordered from lower z-values to higher z-values. If a list of tuples is passed
+            containing colors paired with numbers, then those numbers will be used as the pivots.
+
+        Returns
+        -------
+        :class:`~.ParametricSurface`
+            The parametric surface with a gradient applied by value. For chaining.
+
+        Examples
+        --------
+        .. manim:: FillByValueExample
+            :save_last_frame:
+
+            class FillByValueExample(ThreeDScene):
+                def construct(self):
+                    resolution_fa = 42
+                    self.set_camera_orientation(phi=75 * DEGREES, theta=-120 * DEGREES)
+                    axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
+                    def param_surface(u, v):
+                        x = u
+                        y = v
+                        z = np.sin(x) * np.cos(y)
+                        return z
+                    surface_plane = ParametricSurface(
+                        lambda u, v: axes.c2p(u, v, param_surface(u, v)),
+                        resolution=(resolution_fa, resolution_fa),
+                        v_min=0,
+                        v_max=5,
+                        u_min=0,
+                        u_max=5)
+                    surface_plane.set_style(fill_opacity=1)
+                    surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.4), (YELLOW, 0), (GREEN, 0.4)])
+                    self.add(axes, surface_plane)
+        """
+        if type(colors[0]) is tuple:
+            new_colors, pivots = [[i for i, j in colors], [j for i, j in colors]]
+        else:
+            new_colors = colors
+
+            pivot_min = axes.z_range[0]
+            pivot_max = axes.z_range[1]
+            pivot_frequency = (pivot_max - pivot_min) / (len(new_colors) - 1)
+            pivots = np.arange(
+                start=pivot_min, stop=pivot_max + pivot_frequency, step=pivot_frequency
+            )
+
+        for mob in self.family_members_with_points():
+            z_value = axes.point_to_coords(mob.get_midpoint())[2]
+            if z_value <= pivots[0]:
+                mob.set_color(new_colors[0])
+            elif z_value >= pivots[-1]:
+                mob.set_color(new_colors[-1])
+            else:
+                for i, pivot in enumerate(pivots):
+                    if pivot > z_value:
+                        color_index = (z_value - pivots[i - 1]) / (
+                            pivots[i] - pivots[i - 1]
+                        )
+                        color_index = min(color_index, 1)
+                        mob_color = interpolate_color(
+                            new_colors[i - 1], new_colors[i], color_index
+                        )
+                        mob.set_color(mob_color, family=False)
+                        break
+
+        return self
+
 
 # Specific shapes
 
 
 class Sphere(ParametricSurface):
     """A mobject representing a three-dimensional sphere.
 
@@ -171,18 +266,16 @@
         class ExampleSphere(ThreeDScene):
             def construct(self):
                 self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
                 sphere1 = Sphere(
                     center=(3, 0, 0),
                     radius=1,
                     resolution=(20, 20),
-                    u_min=0.001,
-                    u_max=PI - 0.001,
-                    v_min=0,
-                    v_max=TAU,
+                    u_range=[0.001, PI - 0.001],
+                    v_range=[0, TAU]
                 )
                 sphere1.set_color(RED)
                 self.add(sphere1)
                 sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
                 sphere2.set_color(GREEN)
                 self.add(sphere2)
                 sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
@@ -191,28 +284,24 @@
     """
 
     def __init__(
         self,
         center=ORIGIN,
         radius=1,
         resolution=(12, 24),
-        u_min=0.001,
-        u_max=PI - 0.001,
-        v_min=0,
-        v_max=TAU,
+        u_range=[0.001, PI - 0.001],
+        v_range=[0, TAU],
         **kwargs
     ):
         ParametricSurface.__init__(
             self,
             self.func,
             resolution=resolution,
-            u_min=u_min,
-            u_max=u_max,
-            v_min=v_min,
-            v_max=v_max,
+            u_range=u_range,
+            v_range=v_range,
             **kwargs,
         )
         self.radius = radius
         self.scale(self.radius)
         self.shift(center)
 
     def func(
@@ -337,46 +426,41 @@
         The base radius from which the cone tapers.
     height : :class:`float`
         The height measured from the plane formed by the base_radius to the apex of the cone.
     direction : :class:`numpy.array`
         The direction of the apex.
     show_base : :class:`bool`
         Whether to show the base plane or not.
-    v_min : :class:`float`
-        The azimuthal angle to start at.
-    v_max : :class:`float`
-        The azimuthal angle to end at.
+    v_range : :class:`Sequence[float]`
+        The azimuthal angle to start and end at.
     u_min : :class:`float`
         The radius at the apex.
     checkerboard_colors : :class:`bool`
         Show checkerboard grid texture on the cone.
     """
 
     def __init__(
         self,
         base_radius=1,
         height=1,
         direction=Z_AXIS,
         show_base=False,
-        v_min=0,
-        v_max=TAU,
+        v_range=[0, TAU],
         u_min=0,
         checkerboard_colors=False,
         **kwargs
     ):
         self.direction = direction
         self.theta = PI - np.arctan(base_radius / height)
 
         ParametricSurface.__init__(
             self,
             self.func,
-            v_min=v_min,
-            v_max=v_max,
-            u_min=u_min,
-            u_max=np.sqrt(base_radius ** 2 + height ** 2),
+            v_range=v_range,
+            u_range=[u_min, np.sqrt(base_radius ** 2 + height ** 2)],
             checkerboard_colors=checkerboard_colors,
             **kwargs,
         )
         # used for rotations
         self._current_theta = 0
         self._current_phi = 0
 
@@ -468,43 +552,38 @@
     ---------
     radius : :class:`float`
         The radius of the cylinder.
     height : :class:`float`
         The height of the cylinder.
     direction : :class:`numpy.array`
         The direction of the central axis of the cylinder.
-    v_min : :class:`float`
-        The height along the height axis (given by direction) to start on.
-    v_max : :class:`float`
-        The height along the height axis (given by direction) to end on.
+    v_range : :class:`Sequence[float]`
+        The height along the height axis (given by direction) to start and end on.
     show_ends : :class:`bool`
         Whether to show the end caps or not.
     """
 
     def __init__(
         self,
         radius=1,
         height=2,
         direction=Z_AXIS,
-        v_min=0,
-        v_max=TAU,
+        v_range=[0, TAU],
         show_ends=True,
         resolution=24,
         **kwargs
     ):
         self._height = height
         self.radius = radius
         ParametricSurface.__init__(
             self,
             self.func,
             resolution=resolution,
-            u_min=-self._height / 2,
-            u_max=self._height / 2,
-            v_min=v_min,
-            v_max=v_max,
+            u_range=[-self._height / 2, self._height / 2],
+            v_range=v_range,
             **kwargs,
         )
         if show_ends:
             self.add_bases()
         self._current_phi = 0
         self._current_theta = 0
         self.set_direction(direction)
@@ -735,30 +814,26 @@
         Radius of the tube.
     """
 
     def __init__(
         self,
         major_radius=3,
         minor_radius=1,
-        u_min=0,
-        u_max=TAU,
-        v_min=0,
-        v_max=TAU,
+        u_range=[0, TAU],
+        v_range=[0, TAU],
         resolution=24,
         **kwargs
     ):
         self.R = major_radius
         self.r = minor_radius
         ParametricSurface.__init__(
             self,
             self.func,
-            u_min=u_min,
-            u_max=u_max,
-            v_min=v_min,
-            v_max=v_max,
+            u_range=u_range,
+            v_range=v_range,
             resolution=resolution,
             **kwargs,
         )
 
     def func(self, u, v):
         P = np.array([np.cos(u), np.sin(u), 0])
         return (self.R - self.r * np.cos(v)) * P - self.r * np.sin(v) * OUT
```

### Comparing `manim-0.8.0/manim/mobject/types/image_mobject.py` & `manim-0.9.0/manim/mobject/types/image_mobject.py`

 * *Files 1% similar despite different names*

```diff
@@ -36,15 +36,15 @@
         pixel_array_dtype="uint8",
         resampling_algorithm=Image.BICUBIC,
         **kwargs,
     ):
         self.pixel_array_dtype = pixel_array_dtype
         self.scale_to_resolution = scale_to_resolution
         self.set_resampling_algorithm(resampling_algorithm)
-        Mobject.__init__(self, **kwargs)
+        super().__init__(**kwargs)
 
     def get_pixel_array(self):
         raise NotImplementedError()
 
     def set_color(self, color, alpha=None, family=True):
         # Likely to be implemented in subclasses, but no obligation
         pass
@@ -280,15 +280,15 @@
             default_display_frame_config = {
                 "stroke_width": 3,
                 "stroke_color": WHITE,
                 "buff": 0,
             }
         self.default_display_frame_config = default_display_frame_config
         self.pixel_array = self.camera.pixel_array
-        AbstractImageMobject.__init__(self, scale_to_resolution=False, **kwargs)
+        super().__init__(scale_to_resolution=False, **kwargs)
 
     # TODO: Get rid of this.
     def get_pixel_array(self):
         self.pixel_array = self.camera.pixel_array
         return self.pixel_array
 
     def add_display_frame(self, **kwargs):
```

### Comparing `manim-0.8.0/manim/mobject/types/opengl_surface.py` & `manim-0.9.0/manim/mobject/types/opengl_surface.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/types/opengl_vectorized_mobject.py` & `manim-0.9.0/manim/mobject/types/opengl_vectorized_mobject.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,28 +6,24 @@
 
 import moderngl
 import numpy as np
 
 from ... import config
 from ...constants import *
 from ...mobject.opengl_mobject import OpenGLMobject, OpenGLPoint
-
-# from manimlib.utils.bezier import get_smooth_quadratic_bezier_handle_points
 from ...utils.bezier import (
     bezier,
     get_quadratic_approximation_of_cubic,
     get_smooth_cubic_bezier_handle_points,
     integer_interpolate,
     interpolate,
     partial_quadratic_bezier_points,
 )
 from ...utils.color import *
-
-# from manimlib.utils.iterables import resize_array
-# from manimlib.utils.color import rgb_to_hex
+from ...utils.deprecation import deprecated_params
 from ...utils.iterables import listify, make_even, resize_with_interpolation
 from ...utils.space_ops import (
     angle_between_vectors,
     cross2d,
     earclip_triangulation,
     get_unit_normal,
     shoelace_direction,
@@ -218,15 +214,18 @@
             "stroke_rgba": self.data["stroke_rgba"],
             "stroke_width": self.data["stroke_width"],
             "gloss": self.get_gloss(),
             "shadow": self.get_shadow(),
         }
 
     def match_style(self, vmobject, recurse=True):
-        self.set_style(**vmobject.get_style(), recurse=False)
+        vmobject_style = vmobject.get_style()
+        if config.renderer == "opengl":
+            vmobject_style["stroke_width"] = vmobject_style["stroke_width"][0][0]
+        self.set_style(**vmobject_style, recurse=False)
         if recurse:
             # Does its best to match up submobject lists, and
             # match styles accordingly
             submobs1, submobs2 = self.submobjects, vmobject.submobjects
             if len(submobs1) == 0:
                 return self
             elif len(submobs2) == 0:
@@ -1019,17 +1018,22 @@
         self.triangulation = tri_indices
         self.needs_new_triangulation = False
         return tri_indices
 
     def triggers_refreshed_triangulation(func):
         @wraps(func)
         def wrapper(self, *args, **kwargs):
-            old_points = self.get_points().copy()
+            old_points = np.empty((0, 3))
+            for mob in self.family_members_with_points():
+                old_points = np.concatenate((old_points, mob.get_points()), axis=0)
             func(self, *args, **kwargs)
-            if not np.all(self.get_points() == old_points):
+            new_points = np.empty((0, 3))
+            for mob in self.family_members_with_points():
+                new_points = np.concatenate((new_points, mob.get_points()), axis=0)
+            if not np.all(new_points == old_points):
                 self.refresh_triangulation()
                 self.refresh_unit_normal()
 
         return wrapper
 
     @triggers_refreshed_triangulation
     def set_points(self, points):
@@ -1220,36 +1224,41 @@
             part = OpenGLVMobject()
             part.set_points(tup)
             part.match_style(vmobject)
             self.add(part)
 
 
 class OpenGLDashedVMobject(OpenGLVMobject):
+    @deprecated_params(
+        params="positive_space_ratio dash_spacing",
+        since="v0.9.0",
+        message="Use dashed_ratio instead of positive_space_ratio.",
+    )
     def __init__(
-        self, vmobject, num_dashes=15, positive_space_ratio=0.5, color=WHITE, **kwargs
+        self, vmobject, num_dashes=15, dashed_ratio=0.5, color=WHITE, **kwargs
     ):
+        # Simplify with removal of deprecation warning
+        self.dash_spacing = kwargs.pop("dash_spacing", None)  # Unused param
+        self.dashed_ratio = kwargs.pop("positive_space_ratio", None) or dashed_ratio
         self.num_dashes = num_dashes
-        self.positive_space_ratio = positive_space_ratio
         super().__init__(color=color, **kwargs)
-        num_dashes = self.num_dashes
-        ps_ratio = self.positive_space_ratio
+        r = self.dashed_ratio
+        n = self.num_dashes
         if num_dashes > 0:
-            # End points of the unit interval for division
-            alphas = np.linspace(0, 1, num_dashes + 1)
-
-            # This determines the length of each "dash"
-            full_d_alpha = 1.0 / num_dashes
-            partial_d_alpha = full_d_alpha * ps_ratio
-
-            # Rescale so that the last point of vmobject will
-            # be the end of the last dash
-            alphas /= 1 - full_d_alpha + partial_d_alpha
+            # Assuming total length is 1
+            dash_len = r / n
+            if vmobject.is_closed():
+                void_len = (1 - r) / n
+            else:
+                void_len = (1 - r) / (n - 1)
 
             self.add(
                 *[
-                    vmobject.get_subcurve(alpha, alpha + partial_d_alpha)
-                    for alpha in alphas[:-1]
+                    vmobject.get_subcurve(
+                        i * (dash_len + void_len), i * (dash_len + void_len) + dash_len
+                    )
+                    for i in range(n)
                 ]
             )
         # Family is already taken care of by get_subcurve
         # implementation
         self.match_style(vmobject, recurse=False)
```

### Comparing `manim-0.8.0/manim/mobject/types/point_cloud_mobject.py` & `manim-0.9.0/manim/mobject/types/point_cloud_mobject.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/types/vectorized_mobject.py` & `manim-0.9.0/manim/mobject/types/vectorized_mobject.py`

 * *Files 1% similar despite different names*

```diff
@@ -29,14 +29,15 @@
     bezier,
     get_smooth_handle_points,
     integer_interpolate,
     interpolate,
     partial_bezier_points,
 )
 from ...utils.color import BLACK, WHITE, color_to_rgba
+from ...utils.deprecation import deprecated_params
 from ...utils.iterables import make_even, stretch_array_to_length, tuplify
 from ...utils.simple_functions import clip_in_place
 from ...utils.space_ops import rotate_vector, shoelace_direction
 from ..opengl_compatibility import ConvertToOpenGL
 from .opengl_vectorized_mobject import OpenGLVMobject
 
 # TODO
@@ -45,14 +46,16 @@
 # - No more mark_paths_closed, instead have the camera test
 #   if last point in close to first point
 # - Think about length of self.points.  Always 0 or 1 mod 4?
 #   That's kind of weird.
 
 
 class VMobject(Mobject):
+    """A vectorized mobject."""
+
     def __init__(
         self,
         fill_color=None,
         fill_opacity=0.0,
         stroke_color=None,
         stroke_opacity=1.0,
         stroke_width=DEFAULT_STROKE_WIDTH,
@@ -178,15 +181,55 @@
         # update alpha channel if opacity was passed in
         if color is not None:
             curr_rgbas[:, :3] = rgbas[:, :3]
         if opacity is not None:
             curr_rgbas[:, 3] = rgbas[:, 3]
         return self
 
-    def set_fill(self, color=None, opacity=None, family=True):
+    def set_fill(
+        self,
+        color: Optional[str] = None,
+        opacity: Optional[float] = None,
+        family: bool = True,
+    ) -> "VMobject":
+        """Set the fill color and fill opacity of a :class:`VMobject`.
+
+        Parameters
+        ----------
+        color
+            Fill color of the :class:`VMobject`.
+        opacity
+            Fill opacity of the :class:`VMobject`.
+        family
+            If ``True``, the fill color of all submobjects is also set.
+
+        Returns
+        -------
+        VMobject
+            self. For chaining purposes.
+
+        Examples
+        --------
+        .. manim:: SetFill
+            :save_last_frame:
+
+            class SetFill(Scene):
+                def construct(self):
+                    square = Square().scale(2).set_fill(WHITE,1)
+                    circle1 = Circle().set_fill(GREEN,0.8)
+                    circle2 = Circle().set_fill(YELLOW) # No fill_opacity
+                    circle3 = Circle().set_fill(color = '#FF2135', opacity = 0.2)
+                    group = Group(circle1,circle2,circle3).arrange()
+                    self.add(square)
+                    self.add(group)
+
+        See Also
+        --------
+        :meth:`~.VMobject.set_style`
+        """
         if family:
             for submobject in self.submobjects:
                 submobject.set_fill(color, opacity, family)
         self.update_rgbas_array("fill_rgbas", color, opacity)
         if opacity is not None:
             self.fill_opacity = opacity
         if color is not None:
@@ -1628,15 +1671,15 @@
             >>> vgroup[0] = new_obj
         """
         if not all(isinstance(m, (VMobject, OpenGLVMobject)) for m in value):
             raise TypeError("All submobjects must be of type VMobject")
         self.submobjects[key] = value
 
 
-class VDict(VMobject):
+class VDict(VMobject, metaclass=ConvertToOpenGL):
     """A VGroup-like class, also offering submobject access by
     key, like a python dict
 
     Parameters
     ----------
     mapping_or_iterable : Union[:class:`Mapping`, Iterable[Tuple[Hashable, :class:`~.VMobject`]]], optional
             The parameter specifying the key-value mapping of keys and mobjects.
@@ -1727,15 +1770,15 @@
                 vdict_using_zip = VDict(zip(["s", "c", "r"], [Square(), Circle(), Rectangle()]))
                 vdict_using_zip.shift(1.5 * RIGHT)
                 self.play(Create(vdict_using_zip))
                 self.wait()
     """
 
     def __init__(self, mapping_or_iterable={}, show_keys=False, **kwargs):
-        VMobject.__init__(self, **kwargs)
+        super().__init__(**kwargs)
         self.show_keys = show_keys
         self.submob_dict = {}
         self.add(mapping_or_iterable)
 
     def __repr__(self):
         return __class__.__name__ + "(" + repr(self.submob_dict) + ")"
 
@@ -1940,15 +1983,15 @@
         --------
         Normal usage::
 
             square_obj = Square()
             self.add_key_value_pair('s', square_obj)
 
         """
-        if not isinstance(value, VMobject):
+        if not isinstance(value, (VMobject, OpenGLVMobject)):
             raise TypeError("All submobjects must be of type VMobject")
         mob = value
         if self.show_keys:
             # This import is here and not at the top to avoid circular import
             from ...mobject.svg.tex_mobject import Tex
 
             key_text = Tex(str(key)).next_to(value, LEFT)
@@ -2036,18 +2079,18 @@
                 r = 0.5
 
                 top_row = VGroup()  # Increasing num_dashes
                 for dashes in range(2, 12):
                     circ = DashedVMobject(Circle(radius=r, color=WHITE), num_dashes=dashes)
                     top_row.add(circ)
 
-                middle_row = VGroup()  # Increasing positive_space_ratio
+                middle_row = VGroup()  # Increasing dashed_ratio
                 for ratio in np.arange(1 / 11, 1, 1 / 11):
                     circ = DashedVMobject(
-                        Circle(radius=r, color=WHITE), positive_space_ratio=ratio
+                        Circle(radius=r, color=WHITE), dashed_ratio=ratio
                     )
                     middle_row.add(circ)
 
                 sq = DashedVMobject(Square(1.5, color=RED))
                 penta = DashedVMobject(RegularPolygon(5, color=BLUE))
                 bottom_row = VGroup(sq, penta)
 
@@ -2055,44 +2098,43 @@
                 middle_row.arrange()
                 bottom_row.arrange(buff=1)
                 everything = VGroup(top_row, middle_row, bottom_row).arrange(DOWN, buff=1)
                 self.add(everything)
 
     """
 
+    @deprecated_params(
+        params="positive_space_ratio dash_spacing",
+        since="v0.9.0",
+        message="Use dashed_ratio instead of positive_space_ratio.",
+    )
     def __init__(
-        self, vmobject, num_dashes=15, positive_space_ratio=0.5, color=WHITE, **kwargs
+        self, vmobject, num_dashes=15, dashed_ratio=0.5, color=WHITE, **kwargs
     ):
+        # Simplify with removal of deprecation warning
+        self.dash_spacing = kwargs.pop("dash_spacing", None)  # Unused param
+        self.dashed_ratio = kwargs.pop("positive_space_ratio", None) or dashed_ratio
         self.num_dashes = num_dashes
-        self.positive_space_ratio = positive_space_ratio
         super().__init__(color=color, **kwargs)
-        ps_ratio = self.positive_space_ratio
+        r = self.dashed_ratio
+        n = self.num_dashes
         if num_dashes > 0:
-            # End points of the unit interval for division
-            alphas = np.linspace(0, 1, num_dashes + 1)
-
-            # This determines the length of each "dash"
-            full_d_alpha = 1.0 / num_dashes
-            partial_d_alpha = full_d_alpha * ps_ratio
-
-            # Shifts the alphas and removes the last dash
-            # to give closed shapes even spacing
+            # Assuming total length is 1
+            dash_len = r / n
             if vmobject.is_closed():
-                alphas += partial_d_alpha / 2
-                np.delete(alphas, -1)
-
-            # Rescale so that the last point of vmobject will
-            # be the end of the last dash
+                void_len = (1 - r) / n
             else:
-                alphas /= 1 - full_d_alpha + partial_d_alpha
+                void_len = (1 - r) / (n - 1)
 
             self.add(
                 *[
-                    vmobject.get_subcurve(alpha, alpha + partial_d_alpha)
-                    for alpha in alphas[:-1]
+                    vmobject.get_subcurve(
+                        i * (dash_len + void_len), i * (dash_len + void_len) + dash_len
+                    )
+                    for i in range(n)
                 ]
             )
         # Family is already taken care of by get_subcurve
         # implementation
         if config.renderer == "opengl":
             self.match_style(vmobject, recurse=False)
         else:
```

### Comparing `manim-0.8.0/manim/mobject/value_tracker.py` & `manim-0.9.0/manim/mobject/value_tracker.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/mobject/vector_field.py` & `manim-0.9.0/manim/mobject/vector_field.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/plugins/import_plugins.py` & `manim-0.9.0/manim/plugins/import_plugins.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/plugins/plugins_flags.py` & `manim-0.9.0/manim/plugins/plugins_flags.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/cairo_renderer.py` & `manim-0.9.0/manim/renderer/cairo_renderer.py`

 * *Files 3% similar despite different names*

```diff
@@ -53,30 +53,37 @@
 class CairoRenderer:
     """A renderer using Cairo.
 
     num_plays : Number of play() functions in the scene.
     time: time elapsed since initialisation of scene.
     """
 
-    def __init__(self, camera_class=None, skip_animations=False, **kwargs):
+    def __init__(
+        self,
+        file_writer_class=SceneFileWriter,
+        camera_class=None,
+        skip_animations=False,
+        **kwargs,
+    ):
         # All of the following are set to EITHER the value passed via kwargs,
         # OR the value stored in the global config dict at the time of
         # _instance construction_.
         self.file_writer = None
+        self._file_writer_class = file_writer_class
         camera_cls = camera_class if camera_class is not None else Camera
         self.camera = camera_cls()
         self._original_skipping_status = skip_animations
         self.skip_animations = skip_animations
         self.animations_hashes = []
         self.num_plays = 0
         self.time = 0
         self.static_image = None
 
     def init_scene(self, scene):
-        self.file_writer = SceneFileWriter(
+        self.file_writer = self._file_writer_class(
             self,
             scene.__class__.__name__,
         )
 
     def play(self, scene, *args, **kwargs):
         # Reset skip_animations to the original state.
         # Needed when rendering only some animations, and skipping others.
@@ -149,15 +156,15 @@
         ignore_skipping : bool, optional
 
         **kwargs
 
         """
         if self.skip_animations and not ignore_skipping:
             return
-        if mobjects is None:
+        if not mobjects:
             mobjects = list_update(
                 scene.mobjects,
                 scene.foreground_mobjects,
             )
         if self.static_image is not None:
             self.camera.set_frame_to_background(self.static_image)
         else:
```

### Comparing `manim-0.8.0/manim/renderer/opengl_renderer.py` & `manim-0.9.0/manim/renderer/opengl_renderer.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 import itertools as it
-import re
 import time
 
 import moderngl
 import numpy as np
 from PIL import Image
 
 from manim import config
 from manim.renderer.cairo_renderer import handle_play_like_call
 from manim.utils.caching import handle_caching_play
-from manim.utils.color import color_to_rgb, color_to_rgba
+from manim.utils.color import color_to_rgba
 from manim.utils.exceptions import EndSceneEarlyException
 
 from ..constants import *
 from ..mobject.opengl_mobject import OpenGLMobject, OpenGLPoint
 from ..mobject.types.opengl_vectorized_mobject import OpenGLVMobject
 from ..scene.scene_file_writer import SceneFileWriter
 from ..utils import opengl
@@ -39,23 +38,34 @@
         frame_shape=None,
         center_point=None,
         # Theta, phi, gamma
         euler_angles=[0, 0, 0],
         focal_distance=2,
         light_source_position=[-10, 10, 10],
         orthographic=False,
+        minimum_polar_angle=-PI / 2,
+        maximum_polar_angle=PI / 2,
+        model_matrix=None,
         **kwargs,
     ):
         self.use_z_index = True
         self.frame_rate = 60
         self.orthographic = orthographic
+        self.minimum_polar_angle = minimum_polar_angle
+        self.maximum_polar_angle = maximum_polar_angle
         if self.orthographic:
             self.projection_matrix = opengl.orthographic_projection_matrix()
+            self.unformatted_projection_matrix = opengl.orthographic_projection_matrix(
+                format=False
+            )
         else:
             self.projection_matrix = opengl.perspective_projection_matrix()
+            self.unformatted_projection_matrix = opengl.perspective_projection_matrix(
+                format=False
+            )
 
         if frame_shape is None:
             self.frame_shape = (config["frame_width"], config["frame_height"])
         else:
             self.frame_shape = frame_shape
 
         if center_point is None:
@@ -72,22 +82,28 @@
 
         if light_source_position is None:
             self.light_source_position = [-10, 10, 10]
         else:
             self.light_source_position = light_source_position
         self.light_source = OpenGLPoint(self.light_source_position)
 
-        self.model_matrix = opengl.translation_matrix(0, 0, 11)
-        self.default_model_matrix = opengl.translation_matrix(0, 0, 11)
+        if model_matrix is None:
+            model_matrix = opengl.translation_matrix(0, 0, 11)
+
+        super().__init__(model_matrix=model_matrix, **kwargs)
 
-        super().__init__(**kwargs)
+        self.default_model_matrix = model_matrix
 
     def get_position(self):
         return self.model_matrix[:, 3][:3]
 
+    def set_position(self, position):
+        self.model_matrix[:, 3][:3] = position
+        return self
+
     def get_view_matrix(self, format=True):
         if format:
             return opengl.matrix_to_shader_input(np.linalg.inv(self.model_matrix))
         else:
             return np.linalg.inv(self.model_matrix)
 
     def init_data(self):
@@ -199,32 +215,33 @@
     "round": 1,
     "bevel": 2,
     "miter": 3,
 }
 
 
 class OpenGLRenderer:
-    def __init__(self, skip_animations=False):
+    def __init__(self, file_writer_class=SceneFileWriter, skip_animations=False):
         # Measured in pixel widths, used for vector graphics
         self.anti_alias_width = 1.5
+        self._file_writer_class = file_writer_class
 
         self._original_skipping_status = skip_animations
         self.skip_animations = skip_animations
         self.animations_hashes = []
         self.num_plays = 0
 
         self.camera = OpenGLCamera()
         self.pressed_keys = set()
 
         # Initialize texture map.
         self.path_to_texture_id = {}
 
     def init_scene(self, scene):
         self.partial_movie_files = []
-        self.file_writer = SceneFileWriter(
+        self.file_writer = self._file_writer_class(
             self,
             scene.__class__.__name__,
         )
         self.scene = scene
         if not hasattr(self, "window"):
             if config["preview"]:
                 self.window = Window(self)
@@ -240,15 +257,18 @@
                 moderngl.SRC_ALPHA,
                 moderngl.ONE_MINUS_SRC_ALPHA,
                 moderngl.ONE,
                 moderngl.ONE,
             )
 
     def get_pixel_shape(self):
-        return self.frame_buffer_object.viewport[2:4]
+        if hasattr(self, "frame_buffer_object"):
+            return self.frame_buffer_object.viewport[2:4]
+        else:
+            return None
 
     def refresh_perspective_uniforms(self, camera):
         pw, ph = self.get_pixel_shape()
         fw, fh = camera.get_shape()
         # TODO, this should probably be a mobject uniform, with
         # the camera taking care of the conversion factor
         anti_alias_width = self.anti_alias_width / (ph / fh)
@@ -310,14 +330,15 @@
             # Render.
             mesh = Mesh(
                 shader,
                 shader_wrapper.vert_data,
                 indices=shader_wrapper.vert_indices,
                 use_depth_test=shader_wrapper.depth_test,
             )
+            mesh.set_uniforms(self)
             mesh.render()
 
     def get_texture_id(self, path):
         if path not in self.path_to_texture_id:
             # A way to increase tid's sequentially
             tid = len(self.path_to_texture_id)
             im = Image.open(path)
@@ -378,28 +399,17 @@
         window_background_color = color_to_rgba(config["background_color"])
         self.frame_buffer_object.clear(*window_background_color)
         self.refresh_perspective_uniforms(scene.camera)
 
         for mobject in scene.mobjects:
             self.render_mobject(mobject)
 
-        view_matrix = scene.camera.get_view_matrix(format=False)
-        opengl_view_matrix = opengl.matrix_to_shader_input(view_matrix)
-        from moderngl.program_members.uniform import Uniform
-
         for obj in scene.meshes:
             for mesh in obj.get_meshes():
-                mesh.shader.set_uniform(
-                    "u_model_matrix", opengl.matrix_to_shader_input(mesh.model_matrix)
-                )
-                mesh.shader.set_uniform("u_view_matrix", opengl_view_matrix)
-                mesh.shader.set_uniform(
-                    "u_projection_matrix",
-                    scene.camera.projection_matrix,
-                )
+                mesh.set_uniforms(self)
                 mesh.render()
 
         self.animation_elapsed_time = time.time() - self.animation_start_time
 
     def scene_finished(self, scene):
         self.file_writer.finish()
 
@@ -443,15 +453,18 @@
         result_dimensions = (config["pixel_height"], config["pixel_width"], 4)
         np_buf = np.frombuffer(raw, dtype="uint8").reshape(result_dimensions)
         np_buf = np.flipud(np_buf)
         return np_buf
 
     # Returns offset from the bottom left corner in pixels.
     def pixel_coords_to_space_coords(self, px, py, relative=False):
-        pw, ph = config["pixel_width"], config["pixel_height"]
+        pixel_shape = self.get_pixel_shape()
+        if pixel_shape is None:
+            return np.array([0, 0, 0])
+        pw, ph = pixel_shape
         fw, fh = config["frame_width"], config["frame_height"]
         fc = self.camera.get_center()
         if relative:
             return 2 * np.array([px / pw, py / ph, 0])
         else:
             # Only scale wrt one axis
             scale = fh / ph
```

### Comparing `manim-0.8.0/manim/renderer/opengl_renderer_window.py` & `manim-0.9.0/manim/renderer/opengl_renderer_window.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,30 +9,34 @@
 class Window(PygletWindow):
     fullscreen = False
     resizable = True
     gl_version = (3, 3)
     vsync = True
     cursor = True
 
-    def __init__(self, renderer, size=None, **kwargs):
-        if size is None:
-            # Default to making window half the screen size
-            # but make it full screen if --fullscreen is passed in
-            monitors = get_monitors()
-            mon_index = config.window_monitor
-            monitor = monitors[min(mon_index, len(monitors) - 1)]
-            window_width = monitor.width
+    def __init__(self, renderer, size=config.window_size, **kwargs):
+        monitors = get_monitors()
+        mon_index = config.window_monitor
+        monitor = monitors[min(mon_index, len(monitors) - 1)]
+
+        if size == "default":
+            # make window_width half the width of the monitor
+            # but make it full screen if --fullscreen
 
+            window_width = monitor.width
             if not config.fullscreen:
                 window_width //= 2
 
+            #  by default window_height = 9/16 * window_width
             window_height = int(
                 window_width * config.frame_height // config.frame_width
             )
             size = (window_width, window_height)
+        else:
+            size = tuple(size)
 
         super().__init__(size=size)
 
         self.title = f"Manim Community {__version__}"
         self.size = size
         self.renderer = renderer
 
@@ -103,7 +107,17 @@
         width_diff = monitor.width - window_width
         height_diff = monitor.height - window_height
 
         return (
             monitor.x + char_to_n[custom_position[1]] * width_diff // 2,
             -monitor.y + char_to_n[custom_position[0]] * height_diff // 2,
         )
+
+    def on_mouse_press(self, x, y, button, modifiers):
+        super().on_mouse_press(x, y, button, modifiers)
+        point = self.renderer.pixel_coords_to_space_coords(x, y)
+        mouse_button_map = {
+            1: "LEFT",
+            2: "MOUSE",
+            4: "RIGHT",
+        }
+        self.renderer.scene.on_mouse_press(point, mouse_button_map[button], modifiers)
```

### Comparing `manim-0.8.0/manim/renderer/shader.py` & `manim-0.9.0/manim/renderer/shader.py`

 * *Files 4% similar despite different names*

```diff
@@ -121,14 +121,21 @@
                     raise Exception(
                         "Attempt to remove child that isn't added to this Object3D"
                     )
         self.children = list(filter(lambda child: child not in children, self.children))
         for child in children:
             child.parent = None
 
+    def get_position(self):
+        return self.model_matrix[:, 3][:3]
+
+    def set_position(self, position):
+        self.model_matrix[:, 3][:3] = position
+        return self
+
     def get_meshes(self):
         dfs = [self]
         while dfs:
             parent = dfs.pop()
             if isinstance(parent, Mesh):
                 yield parent
             dfs.extend(parent.children)
@@ -157,15 +164,15 @@
     def hierarchical_normal_matrix(self):
         if self.parent is None:
             return self.normal_matrix[:3, :3]
 
         normal_matrices = [self.normal_matrix]
         current_object = self
         while current_object.parent is not None:
-            normal_matrices.append(current_object.parent.normal_matrix)
+            normal_matrices.append(current_object.parent.model_matrix)
             current_object = current_object.parent
         return np.linalg.multi_dot(list(reversed(normal_matrices)))[:3, :3]
 
     def init_updaters(self):
         self.time_based_updaters = []
         self.non_time_updaters = []
         self.has_updaters = False
@@ -279,14 +286,24 @@
         )
         copy.skip_render = self.skip_render
         copy.model_matrix = self.model_matrix.copy()
         copy.normal_matrix = self.normal_matrix.copy()
         # TODO: Copy updaters?
         return copy
 
+    def set_uniforms(self, renderer):
+        self.shader.set_uniform(
+            "u_model_matrix", opengl.matrix_to_shader_input(self.model_matrix)
+        )
+        self.shader.set_uniform("u_view_matrix", renderer.camera.get_view_matrix())
+        self.shader.set_uniform(
+            "u_projection_matrix",
+            renderer.camera.projection_matrix,
+        )
+
     def render(self):
         if self.skip_render:
             return
 
         if self.use_depth_test:
             self.shader.context.enable(moderngl.DEPTH_TEST)
         else:
```

### Comparing `manim-0.8.0/manim/renderer/shader_wrapper.py` & `manim-0.9.0/manim/renderer/shader_wrapper.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,17 +4,14 @@
 from pathlib import Path
 
 import moderngl
 import numpy as np
 
 from .. import logger
 
-# from manimlib.utils.directories import get_shader_dir
-# from manimlib.utils.file_ops import find_file
-
 # Mobjects that should be rendered with
 # the same shader will be organized and
 # clumped together based on keeping track
 # of a dict holding all the relevant information
 # to that shader
```

### Comparing `manim-0.8.0/manim/renderer/shaders/design_2.frag` & `manim-0.9.0/manim/renderer/shaders/design_2.frag`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/design_3.frag` & `manim-0.9.0/manim/renderer/shaders/design_3.frag`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/NOTE.md` & `manim-0.9.0/manim/renderer/shaders/include/NOTE.md`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/add_light.glsl` & `manim-0.9.0/manim/renderer/shaders/include/add_light.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/finalize_color.glsl` & `manim-0.9.0/manim/renderer/shaders/include/finalize_color.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/get_gl_Position.glsl` & `manim-0.9.0/manim/renderer/shaders/include/get_gl_Position.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/get_rotated_surface_unit_normal_vector.glsl` & `manim-0.9.0/manim/renderer/shaders/include/get_rotated_surface_unit_normal_vector.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/get_unit_normal.glsl` & `manim-0.9.0/manim/renderer/shaders/include/get_unit_normal.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/quadratic_bezier_distance.glsl` & `manim-0.9.0/manim/renderer/shaders/include/quadratic_bezier_distance.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/include/quadratic_bezier_geometry_functions.glsl` & `manim-0.9.0/manim/renderer/shaders/include/quadratic_bezier_geometry_functions.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/NOTE.md` & `manim-0.9.0/manim/renderer/shaders/inserts/NOTE.md`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/add_light.glsl` & `manim-0.9.0/manim/renderer/shaders/inserts/add_light.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/finalize_color.glsl` & `manim-0.9.0/manim/renderer/shaders/inserts/finalize_color.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/get_gl_Position.glsl` & `manim-0.9.0/manim/renderer/shaders/inserts/get_gl_Position.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/get_rotated_surface_unit_normal_vector.glsl` & `manim-0.9.0/manim/renderer/shaders/inserts/get_rotated_surface_unit_normal_vector.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/get_unit_normal.glsl` & `manim-0.9.0/manim/renderer/shaders/inserts/get_unit_normal.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/quadratic_bezier_distance.glsl` & `manim-0.9.0/manim/renderer/shaders/inserts/quadratic_bezier_distance.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/inserts/quadratic_bezier_geometry_functions.glsl` & `manim-0.9.0/manim/renderer/shaders/inserts/quadratic_bezier_geometry_functions.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/quadratic_bezier_fill/frag.glsl` & `manim-0.9.0/manim/renderer/shaders/quadratic_bezier_fill/frag.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/quadratic_bezier_fill/geom.glsl` & `manim-0.9.0/manim/renderer/shaders/quadratic_bezier_fill/geom.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/quadratic_bezier_fill/vert.glsl` & `manim-0.9.0/manim/renderer/shaders/quadratic_bezier_fill/vert.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/quadratic_bezier_stroke/frag.glsl` & `manim-0.9.0/manim/renderer/shaders/quadratic_bezier_stroke/frag.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/quadratic_bezier_stroke/geom.glsl` & `manim-0.9.0/manim/renderer/shaders/quadratic_bezier_stroke/geom.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/quadratic_bezier_stroke/vert.glsl` & `manim-0.9.0/manim/renderer/shaders/quadratic_bezier_stroke/vert.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/surface/vert.glsl` & `manim-0.9.0/manim/renderer/shaders/surface/vert.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/textured_surface/frag.glsl` & `manim-0.9.0/manim/renderer/shaders/textured_surface/frag.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/textured_surface/vert.glsl` & `manim-0.9.0/manim/renderer/shaders/textured_surface/vert.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/true_dot/frag.glsl` & `manim-0.9.0/manim/renderer/shaders/true_dot/frag.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/true_dot/geom.glsl` & `manim-0.9.0/manim/renderer/shaders/true_dot/geom.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/vectorized_mobject_stroke/frag.glsl` & `manim-0.9.0/manim/renderer/shaders/vectorized_mobject_stroke/frag.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/shaders/vectorized_mobject_stroke/vert.glsl` & `manim-0.9.0/manim/renderer/shaders/vectorized_mobject_stroke/vert.glsl`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/renderer/webgl_renderer.py` & `manim-0.9.0/manim/renderer/webgl_renderer.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/scene/graph_scene.py` & `manim-0.9.0/manim/scene/graph_scene.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/scene/moving_camera_scene.py` & `manim-0.9.0/manim/scene/moving_camera_scene.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/scene/reconfigurable_scene.py` & `manim-0.9.0/manim/scene/reconfigurable_scene.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/scene/sample_space_scene.py` & `manim-0.9.0/manim/scene/sample_space_scene.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/scene/scene.py` & `manim-0.9.0/manim/scene/scene.py`

 * *Files 3% similar despite different names*

```diff
@@ -97,25 +97,30 @@
         self.camera_class = camera_class
         self.always_update_mobjects = always_update_mobjects
         self.random_seed = random_seed
         self.skip_animations = skip_animations
 
         self.animations = None
         self.stop_condition = None
-        self.moving_mobjects = None
-        self.static_mobjects = None
+        self.moving_mobjects = []
+        self.static_mobjects = []
         self.time_progression = None
         self.duration = None
         self.last_t = None
         self.queue = Queue()
         self.skip_animation_preview = False
         self.meshes = []
         self.camera_target = ORIGIN
         self.widgets = []
         self.dearpygui_imported = dearpygui_imported
+        self.updaters = []
+        self.point_lights = []
+        self.ambient_light = None
+        self.key_to_function_map = {}
+        self.mouse_press_callbacks = []
 
         if config.renderer == "opengl":
             # Items associated with interaction
             self.mouse_point = OpenGLPoint()
             self.mouse_drag_point = OpenGLPoint()
 
         if renderer is None:
@@ -317,14 +322,18 @@
             mobject.update(dt)
 
     def update_meshes(self, dt):
         for obj in self.meshes:
             for mesh in obj.get_family():
                 mesh.update(dt)
 
+    def update_self(self, dt):
+        for func in self.updaters:
+            func(dt)
+
     def should_update_mobjects(self):
         """
         Returns True if any mobject in Scene is being updated
         or if the scene has always_update_mobjects set to true.
 
         Returns
         -------
@@ -451,14 +460,20 @@
             )
             return self
         else:
             for list_name in "mobjects", "foreground_mobjects":
                 self.restructure_mobjects(mobjects, list_name, False)
             return self
 
+    def add_updater(self, func):
+        self.updaters.append(func)
+
+    def remove_updater(self, func):
+        self.updaters = [f for f in self.updaters if f is not func]
+
     def restructure_mobjects(
         self, to_remove, mobject_list_name="mobjects", extract_families=True
     ):
         """
         tl:wr
             If your scene has a Group(), and you removed a mobject from the Group,
             this dissolves the group and puts the rest of the mobjects directly
@@ -902,16 +917,16 @@
             raise ValueError("Called Scene.play with no animations")
 
         self.animations = self.compile_animations(*animations, **play_kwargs)
         self.add_mobjects_from_animations(self.animations)
 
         self.last_t = 0
         self.stop_condition = None
-        self.moving_mobjects = None
-        self.static_mobjects = None
+        self.moving_mobjects = []
+        self.static_mobjects = []
 
         if not config.renderer == "opengl":
             if len(self.animations) == 1 and isinstance(self.animations[0], Wait):
                 self.update_mobjects(dt=0)  # Any problems with this?
                 if self.should_update_mobjects():
                     self.stop_condition = self.animations[0].stop_condition
                 else:
@@ -1020,14 +1035,17 @@
         cfg.TerminalInteractiveShell.confirm_exit = False
         shell = InteractiveShellEmbed(config=cfg)
 
         keyboard_thread = threading.Thread(
             target=ipython,
             args=(shell, local_namespace),
         )
+        # run as daemon to kill thread when main thread exits
+        if not shell.pt_app:
+            keyboard_thread.daemon = True
         keyboard_thread.start()
 
         if self.dearpygui_imported and config["enable_gui"]:
             if not dearpygui.core.is_dearpygui_running():
                 gui_thread = threading.Thread(
                     target=configure_pygui,
                     args=(self.renderer, self.widgets),
@@ -1044,25 +1062,28 @@
     def interact(self, shell, keyboard_thread):
         event_handler = RerunSceneHandler(self.queue)
         file_observer = Observer()
         file_observer.schedule(event_handler, config["input_file"], recursive=True)
         file_observer.start()
 
         self.quit_interaction = False
-        keyboard_thread_needs_join = True
+        keyboard_thread_needs_join = shell.pt_app is not None
         assert self.queue.qsize() == 0
 
         last_time = time.time()
         while not (self.renderer.window.is_closing or self.quit_interaction):
             if not self.queue.empty():
                 tup = self.queue.get_nowait()
                 if tup[0].startswith("rerun"):
                     # Intentionally skip calling join() on the file thread to save time.
                     if not tup[0].endswith("keyboard"):
-                        shell.pt_app.app.exit(exception=EOFError)
+                        if shell.pt_app:
+                            shell.pt_app.app.exit(exception=EOFError)
+                        file_observer.unschedule_all()
+                        raise RerunSceneException
                     keyboard_thread.join()
 
                     kwargs = tup[2]
                     if "from_animation_number" in kwargs:
                         config["from_animation_number"] = kwargs[
                             "from_animation_number"
                         ]
@@ -1070,44 +1091,49 @@
                     # # end of a scene by default.
                     # if "upto_animation_number" in kwargs:
                     #     config["upto_animation_number"] = kwargs[
                     #         "upto_animation_number"
                     #     ]
 
                     keyboard_thread.join()
+                    file_observer.unschedule_all()
                     raise RerunSceneException
                 elif tup[0].startswith("exit"):
                     # Intentionally skip calling join() on the file thread to save time.
-                    if not tup[0].endswith("keyboard"):
+                    if not tup[0].endswith("keyboard") and shell.pt_app:
                         shell.pt_app.app.exit(exception=EOFError)
                     keyboard_thread.join()
                     # Remove exit_keyboard from the queue if necessary.
                     while self.queue.qsize() > 0:
                         self.queue.get()
                     keyboard_thread_needs_join = False
                     break
                 else:
                     method, args, kwargs = tup
                     getattr(self, method)(*args, **kwargs)
             else:
                 self.renderer.animation_start_time = 0
-                dt = last_time - time.time()
+                dt = time.time() - last_time
                 last_time = time.time()
                 self.renderer.render(self, dt, self.moving_mobjects)
                 self.update_mobjects(dt)
                 self.update_meshes(dt)
+                self.update_self(dt)
 
         # Join the keyboard thread if necessary.
         if shell is not None and keyboard_thread_needs_join:
             shell.pt_app.app.exit(exception=EOFError)
             keyboard_thread.join()
             # Remove exit_keyboard from the queue if necessary.
             while self.queue.qsize() > 0:
                 self.queue.get()
 
+        file_observer.stop()
+        file_observer.join()
+
         if self.dearpygui_imported and config["enable_gui"]:
             dearpygui.core.stop_dearpygui()
 
         if self.renderer.window.is_closing:
             self.renderer.window.destroy()
 
     def embed(self):
@@ -1157,14 +1183,15 @@
         self.last_t = t
         for animation in self.animations:
             animation.update_mobjects(dt)
             alpha = t / animation.run_time
             animation.interpolate(alpha)
         self.update_mobjects(dt)
         self.update_meshes(dt)
+        self.update_self(dt)
 
     def add_sound(self, sound_file, time_offset=0, gain=None, **kwargs):
         """
         This method is used to add a sound to the animation.
 
         Parameters
         ----------
@@ -1209,30 +1236,34 @@
             shift[0] *= self.camera.get_width() / 2
             shift[1] *= self.camera.get_height() / 2
             transform = self.camera.inverse_rotation_matrix
             shift = np.dot(np.transpose(transform), shift)
             self.camera.shift(shift)
 
     def on_mouse_scroll(self, point, offset):
-        factor = 1 + np.arctan(-2.1 * offset[1])
-        self.camera.scale(factor, about_point=self.camera_target)
+        if not config.use_projection_stroke_shaders:
+            factor = 1 + np.arctan(-2.1 * offset[1])
+            self.camera.scale(factor, about_point=self.camera_target)
         self.mouse_scroll_orbit_controls(point, offset)
 
     def on_key_press(self, symbol, modifiers):
         try:
             char = chr(symbol)
         except OverflowError:
             logger.warning("The value of the pressed key is too large.")
             return
 
         if char == "r":
             self.camera.to_default_state()
             self.camera_target = np.array([0, 0, 0], dtype=np.float32)
         elif char == "q":
             self.quit_interaction = True
+        else:
+            if char in self.key_to_function_map:
+                self.key_to_function_map[char]()
 
     def on_key_release(self, symbol, modifiers):
         pass
 
     def on_mouse_drag(self, point, d_point, buttons, modifiers):
         self.mouse_drag_point.move_to(point)
         if buttons == 1:
@@ -1271,16 +1302,16 @@
             axis_of_rotation = space_ops.normalize(
                 np.cross(camera_y_axis, camera_position)
             )
             rotation_matrix = space_ops.rotation_matrix(
                 d_point[1], axis_of_rotation, homogeneous=True
             )
 
-            maximum_polar_angle = PI / 2
-            minimum_polar_angle = -PI / 2
+            maximum_polar_angle = self.camera.maximum_polar_angle
+            minimum_polar_angle = self.camera.minimum_polar_angle
 
             potential_camera_model_matrix = rotation_matrix @ self.camera.model_matrix
             potential_camera_location = potential_camera_model_matrix[:3, 3]
             potential_camera_y_axis = potential_camera_model_matrix[:3, 1]
             sign = (
                 np.sign(potential_camera_y_axis[2])
                 if potential_camera_y_axis[2] != 0
@@ -1318,7 +1349,14 @@
             total_shift_vector = horizontal_shift_vector + vertical_shift_vector
 
             self.camera.model_matrix = (
                 opengl.translation_matrix(*total_shift_vector)
                 @ self.camera.model_matrix
             )
             self.camera_target += total_shift_vector
+
+    def set_key_function(self, char, func):
+        self.key_to_function_map[char] = func
+
+    def on_mouse_press(self, point, button, modifiers):
+        for func in self.mouse_press_callbacks:
+            func()
```

### Comparing `manim-0.8.0/manim/scene/scene_file_writer.py` & `manim-0.9.0/manim/scene/scene_file_writer.py`

 * *Files 1% similar despite different names*

```diff
@@ -37,16 +37,14 @@
     This is mostly for Manim's internal use. You will rarely, if ever,
     have to use the methods for this class, unless tinkering with the very
     fabric of Manim's reality.
 
     Some useful attributes are:
         "write_to_movie" (bool=False)
             Whether or not to write the animations into a video file.
-        "png_mode" (str="RGBA")
-            The PIL image mode to use when outputting PNGs
         "movie_file_extension" (str=".mp4")
             The file-type extension of the outputted video.
         "partial_movie_files"
             List of all the partial-movie files.
 
     """
 
@@ -81,17 +79,17 @@
         else:
             default_name = Path(scene_name)
 
         if config["media_dir"]:
             image_dir = guarantee_existence(
                 config.get_dir("images_dir", module_name=module_name)
             )
-        self.image_file_path = os.path.join(
-            image_dir, add_extension_if_not_present(default_name, ".png")
-        )
+            self.image_file_path = os.path.join(
+                image_dir, add_extension_if_not_present(default_name, ".png")
+            )
 
         if write_to_movie():
             movie_dir = guarantee_existence(
                 config.get_dir("video_dir", module_name=module_name)
             )
 
             self.movie_file_path = os.path.join(
@@ -286,15 +284,15 @@
             self.writing_process.stdin.write(
                 renderer.get_raw_frame_buffer_object_data()
             )
         else:
             frame = frame_or_renderer
             if write_to_movie():
                 self.writing_process.stdin.write(frame.tobytes())
-            if is_png_format():
+            if is_png_format() and not config["dry_run"]:
                 target_dir, extension = os.path.splitext(self.image_file_path)
                 Image.fromarray(frame).save(
                     f"{target_dir}{self.frame_count}{extension}"
                 )
                 self.frame_count += 1
 
     def save_final_image(self, image):
@@ -303,14 +301,16 @@
         passed to it as an in the default image directory.
 
         Parameters
         ----------
         image : np.array
             The pixel array of the image to save.
         """
+        if config["dry_run"]:
+            return
         if not config["output_file"]:
             self.image_file_path = add_version_before_extension(self.image_file_path)
 
         image.save(self.image_file_path)
         self.print_file_ready_message(self.image_file_path)
 
     def idle_stream(self):
@@ -345,15 +345,15 @@
             if hasattr(self, "writing_process"):
                 self.writing_process.terminate()
             self.combine_movie_files(partial_movie_files=partial_movie_files)
             if config["flush_cache"]:
                 self.flush_cache_directory()
             else:
                 self.clean_cache()
-        elif is_png_format():
+        elif is_png_format() and not config["dry_run"]:
             target_dir, _ = os.path.splitext(self.image_file_path)
             logger.info("\n%i images ready at %s\n", self.frame_count, target_dir)
 
     def open_movie_pipe(self, file_path=None):
         """
         Used internally by Manim to initialise
         FFMPEG and begin writing to FFMPEG's input
```

### Comparing `manim-0.8.0/manim/scene/three_d_scene.py` & `manim-0.9.0/manim/scene/three_d_scene.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,20 +1,24 @@
 """A scene suitable for rendering three-dimensional objects and animations."""
 
 __all__ = ["ThreeDScene", "SpecialThreeDScene"]
 
 
+from typing import Iterable, Optional, Sequence, Union
+
 import numpy as np
 
 from .. import config
+from ..animation.animation import Animation
 from ..animation.transform import ApplyMethod
 from ..camera.three_d_camera import ThreeDCamera
 from ..constants import DEGREES
 from ..mobject.coordinate_systems import ThreeDAxes
 from ..mobject.geometry import Line
+from ..mobject.mobject import Mobject
 from ..mobject.three_dimensions import Sphere
 from ..mobject.types.vectorized_mobject import VectorizedPoint, VGroup
 from ..mobject.value_tracker import ValueTracker
 from ..scene.scene import Scene
 from ..utils.config_ops import merge_dicts_recursively
 
 
@@ -38,15 +42,22 @@
                 "theta": -135 * DEGREES,
             }
         self.default_angled_camera_orientation_kwargs = (
             default_angled_camera_orientation_kwargs
         )
         super().__init__(camera_class=camera_class, **kwargs)
 
-    def set_camera_orientation(self, phi=None, theta=None, distance=None, gamma=None):
+    def set_camera_orientation(
+        self,
+        phi: Optional[float] = None,
+        theta: Optional[float] = None,
+        gamma: Optional[float] = None,
+        distance: Optional[float] = None,
+        frame_center: Optional[Union["Mobject", Sequence[float]]] = None,
+    ):
         """
         This method sets the orientation of the camera in the scene.
 
         Parameters
         ----------
         phi : int or float, optional
             The polar angle i.e the angle between Z_AXIS and Camera through ORIGIN in radians.
@@ -55,23 +66,29 @@
             The azimuthal angle i.e the angle that spins the camera around the Z_AXIS.
 
         distance : int or float, optional
             The radial distance between ORIGIN and Camera.
 
         gamma : int or float, optional
             The rotation of the camera about the vector from the ORIGIN to the Camera.
+
+        frame_center : list, tuple or np.array, optional
+            The new center of the camera frame in cartesian coordinates.
+
         """
         if phi is not None:
             self.renderer.camera.set_phi(phi)
         if theta is not None:
             self.renderer.camera.set_theta(theta)
         if distance is not None:
             self.renderer.camera.set_distance(distance)
         if gamma is not None:
             self.renderer.camera.set_gamma(gamma)
+        if frame_center is not None:
+            self.renderer.camera._frame_center.move_to(frame_center)
 
     def begin_ambient_camera_rotation(self, rate=0.02, about="theta"):
         """
         This method begins an ambient rotation of the camera about the Z_AXIS,
         in the anticlockwise direction
 
         Parameters
@@ -142,20 +159,20 @@
         self.renderer.camera.theta_tracker.clear_updaters()
         self.remove(self.renderer.camera.theta_tracker)
         self.renderer.camera.phi_tracker.clear_updaters()
         self.remove(self.renderer.camera.phi_tracker)
 
     def move_camera(
         self,
-        phi=None,
-        theta=None,
-        distance=None,
-        gamma=None,
-        frame_center=None,
-        added_anims=[],
+        phi: Optional[float] = None,
+        theta: Optional[float] = None,
+        gamma: Optional[float] = None,
+        distance: Optional[float] = None,
+        frame_center: Optional[Union["Mobject", Sequence[float]]] = None,
+        added_anims: Iterable["Animation"] = [],
         **kwargs,
     ):
         """
         This method animates the movement of the camera
         to the given spherical coordinates.
 
         Parameters
@@ -169,15 +186,15 @@
         distance : int or float, optional
             The radial distance between ORIGIN and Camera.
 
         gamma : int or float, optional
             The rotation of the camera about the vector from the ORIGIN to the Camera.
 
         frame_center : list, tuple or np.array, optional
-            The new center of the camera frame in cartesian coordinates
+            The new center of the camera frame in cartesian coordinates.
 
         added_anims : list, optional
             Any other animations to be played at the same time.
 
         """
         anims = []
         value_tracker_pairs = [
@@ -187,31 +204,42 @@
             (gamma, self.renderer.camera.gamma_tracker),
         ]
         for value, tracker in value_tracker_pairs:
             if value is not None:
                 anims.append(ApplyMethod(tracker.set_value, value, **kwargs))
         if frame_center is not None:
             anims.append(
-                ApplyMethod(self.renderer.camera._frame_center.move_to, frame_center)
+                ApplyMethod(
+                    self.renderer.camera._frame_center.move_to, frame_center, **kwargs
+                )
             )
 
         self.play(*anims + added_anims)
 
+        # These lines are added to improve performance. If manim thinks that frame_center is moving,
+        # it is required to redraw every object. These lines remove frame_center from the Scene once
+        # its animation is done, ensuring that manim does not think that it is moving. Since the
+        # frame_center is never actually drawn, this shouldn't break anything.
+        if frame_center is not None:
+            self.remove(self.renderer.camera._frame_center)
+
     def get_moving_mobjects(self, *animations):
         """
         This method returns a list of all of the Mobjects in the Scene that
         are moving, that are also in the animations passed.
 
         Parameters
         ----------
         *animations : Animation
             The animations whose mobjects will be checked.
         """
         moving_mobjects = Scene.get_moving_mobjects(self, *animations)
-        camera_mobjects = self.renderer.camera.get_value_trackers()
+        camera_mobjects = self.renderer.camera.get_value_trackers() + [
+            self.renderer.camera._frame_center
+        ]
         if any([cm in moving_mobjects for cm in camera_mobjects]):
             return self.mobjects
         return moving_mobjects
 
     def add_fixed_orientation_mobjects(self, *mobjects, **kwargs):
         """
         This method is used to prevent the rotation and tilting
```

### Comparing `manim-0.8.0/manim/scene/vector_space_scene.py` & `manim-0.9.0/manim/scene/vector_space_scene.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/scene/zoomed_scene.py` & `manim-0.9.0/manim/scene/zoomed_scene.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/templates/Default.mtp` & `manim-0.9.0/manim/templates/Default.mtp`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/bezier.py` & `manim-0.9.0/manim/utils/bezier.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/caching.py` & `manim-0.9.0/manim/utils/caching.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/color.py` & `manim-0.9.0/manim/utils/color.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/config_ops.py` & `manim-0.9.0/manim/utils/config_ops.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/debug.py` & `manim-0.9.0/manim/utils/debug.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/deprecation.py` & `manim-0.9.0/manim/utils/deprecation.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/family.py` & `manim-0.9.0/manim/utils/family.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/family_ops.py` & `manim-0.9.0/manim/utils/family_ops.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/file_ops.py` & `manim-0.9.0/manim/utils/file_ops.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/hashing.py` & `manim-0.9.0/manim/utils/hashing.py`

 * *Files 5% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 import zlib
 from time import perf_counter
 from types import FunctionType, MappingProxyType, MethodType, ModuleType
 from typing import Any
 
 import numpy as np
 
-from .. import logger
+from .. import config, logger
 
 # Sometimes there are elements that are not suitable for hashing (too long or run-dependent)
 # This is used to filter them out.
 KEYS_TO_FILTER_OUT = set(
     ["original_id", "background", "pixel_array", "pixel_array_to_cairo_context"]
 )
 
@@ -29,15 +29,16 @@
 
     This class uses two signatures functions to keep a track of processed objects : hash or id. Whenever possible, hash is used to ensure a broader object content-equality detection.
     """
 
     _already_processed = set()
 
     # Can be changed to whatever string to help debugging the JSon generation.
-    ALREADY_PROCESSED_PLACEHOLDER = "ALREADY PROCESSED"
+    ALREADY_PROCESSED_PLACEHOLDER = "AP"
+    THRESHOLD_WARNING = 170_000
 
     @classmethod
     def reset_already_processed(cls):
         cls._already_processed.clear()
 
     @classmethod
     def check_already_processed_decorator(cls: "_Memoizer", is_method=False):
@@ -121,19 +122,30 @@
     def _return(
         cls,
         obj: typing.Any,
         obj_to_membership_sign: typing.Callable[[Any], int],
         default_func,
         memoizing=True,
     ) -> typing.Union[str, Any]:
-
         obj_membership_sign = obj_to_membership_sign(obj)
         if obj_membership_sign in cls._already_processed:
             return cls.ALREADY_PROCESSED_PLACEHOLDER
         if memoizing:
+            if (
+                not config.disable_caching_warning
+                and len(cls._already_processed) == cls.THRESHOLD_WARNING
+            ):
+                logger.warning(
+                    "It looks like the scene contains a lot of sub-mobjects. Caching is sometimes not suited to handle such large scenes, you might consider disabling caching with\
+                            --disable_caching to potentially speed up the rendering process."
+                )
+                logger.warning(
+                    "You can disable this warning by setting disable_caching_warning to True in your config file."
+                )
+
             cls._already_processed.add(obj_membership_sign)
         return default_func(obj)
 
 
 class _CustomEncoder(json.JSONEncoder):
     def default(self, obj):
         """
@@ -184,15 +196,16 @@
             # MappingProxy is scene-caching nightmare. It contains all of the object methods and attributes. We skip it as the mechanism will at some point process the object, but instantiated.
             # Indeed, there is certainly no case where scene-caching will receive only a non instancied object, as this is never used in the library or encouraged to be used user-side.
             if isinstance(temp, MappingProxyType):
                 return "MappingProxy"
             return self._cleaned_iterable(temp)
         elif isinstance(obj, np.uint8):
             return int(obj)
-        return f"Unsupported type for serializing -> {str(type(obj))}"
+        # Serialize it with only the type of the object. You can change this to whatever string when debugging the serialization process.
+        return str(type(obj))
 
     def _cleaned_iterable(self, iterable):
         """Check for circular reference at each iterable that will go through the JSONEncoder, as well as key of the wrong format.
 
         If a key with a bad format is found (i.e not a int, string, or float), it gets replaced byt its hash using the same process implemented here.
         If a circular reference is found within the iterable, it will be replaced by the string "already processed".
```

### Comparing `manim-0.8.0/manim/utils/images.py` & `manim-0.9.0/manim/utils/images.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/ipython_magic.py` & `manim-0.9.0/manim/utils/ipython_magic.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/iterables.py` & `manim-0.9.0/manim/utils/iterables.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/module_ops.py` & `manim-0.9.0/manim/utils/module_ops.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/opengl.py` & `manim-0.9.0/manim/utils/opengl.py`

 * *Files 1% similar despite different names*

```diff
@@ -27,15 +27,15 @@
     )
     if format:
         return matrix_to_shader_input(projection_matrix)
     else:
         return projection_matrix
 
 
-def perspective_projection_matrix(width=None, height=None, near=2, far=30, format=True):
+def perspective_projection_matrix(width=None, height=None, near=2, far=50, format=True):
     if width is None:
         width = config["frame_width"] / 6
     if height is None:
         height = config["frame_height"] / 6
     projection_matrix = np.array(
         [
             [2 * near / width, 0, 0, 0],
```

### Comparing `manim-0.8.0/manim/utils/paths.py` & `manim-0.9.0/manim/utils/paths.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/rate_functions.py` & `manim-0.9.0/manim/utils/rate_functions.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/simple_functions.py` & `manim-0.9.0/manim/utils/simple_functions.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/space_ops.py` & `manim-0.9.0/manim/utils/space_ops.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,39 +1,37 @@
 """Utility functions for two- and three-dimensional vectors."""
 
 __all__ = [
-    "get_norm",
     "quaternion_mult",
     "quaternion_from_angle_axis",
     "angle_axis_from_quaternion",
     "quaternion_conjugate",
     "rotate_vector",
     "thick_diagonal",
     "rotation_matrix",
     "rotation_about_z",
     "z_to_vector",
-    "angle_between",
     "angle_of_vector",
     "angle_between_vectors",
     "project_along_vector",
     "normalize",
-    "cross",
     "get_unit_normal",
     "compass_directions",
     "regular_vertices",
     "complex_to_R3",
     "R3_to_complex",
     "complex_func_to_R3_func",
     "center_of_mass",
     "midpoint",
     "find_intersection",
     "line_intersection",
     "get_winding_number",
     "cross2d",
     "earclip_triangulation",
+    "perpendicular_bisector",
 ]
 
 
 import itertools as it
 import math
 from functools import reduce
 from typing import List, Optional, Sequence, Tuple, Union
@@ -43,19 +41,14 @@
 
 from .. import config
 from ..constants import DOWN, OUT, PI, RIGHT, TAU
 from ..utils.deprecation import deprecated
 from ..utils.iterables import adjacent_pairs
 
 
-@deprecated(since="v0.6.0", until="v0.8.0", replacement="np.linalg.norm")
-def get_norm(vect):
-    return np.linalg.norm(vect)
-
-
 def norm_squared(v: float) -> float:
     return np.dot(v, v)
 
 
 # Quaternions
 # TODO, implement quaternion type
 
@@ -317,19 +310,14 @@
         theta = 0
     phi_down = np.array(
         [[np.cos(phi), 0, np.sin(phi)], [0, 1, 0], [-np.sin(phi), 0, np.cos(phi)]]
     )
     return np.dot(rotation_about_z(theta), phi_down)
 
 
-@deprecated(since="v0.6.0", until="v0.8.0", replacement="angle_between_vectors")
-def angle_between(v1, v2):
-    return np.arccos(np.dot(v1 / np.linalg.norm(v1), v2 / np.linalg.norm(v2)))
-
-
 def angle_of_vector(vector: Sequence[float]) -> float:
     """Returns polar coordinate theta when vector is projected on xy plane.
 
     Parameters
     ----------
     vector
         The vector to find the angle for.
@@ -360,22 +348,19 @@
         The second vector.
 
     Returns
     -------
     np.ndarray
         The angle between the vectors.
     """
-    if config["renderer"] == "opengl":
-        diff = (angle_of_vector(v2) - angle_of_vector(v1)) % TAU
-        return min(diff, TAU - diff)
-    else:
-        return 2 * np.arctan2(
-            np.linalg.norm(normalize(v1) - normalize(v2)),
-            np.linalg.norm(normalize(v1) + normalize(v2)),
-        )
+
+    return 2 * np.arctan2(
+        np.linalg.norm(normalize(v1) - normalize(v2)),
+        np.linalg.norm(normalize(v1) + normalize(v2)),
+    )
 
 
 def project_along_vector(point: float, vector: np.ndarray) -> np.ndarray:
     """Projects a vector along a point.
 
     Parameters
     ----------
@@ -422,19 +407,14 @@
     norms = np.sqrt((array * array).sum(axis))
     norms[norms == 0] = 1
     buffed_norms = np.repeat(norms, array.shape[axis]).reshape(array.shape)
     array /= buffed_norms
     return array
 
 
-@deprecated(since="v0.6.0", until="v0.8.0", replacement="np.cross")
-def cross(v1, v2):
-    return np.cross(v1, v2)
-
-
 def get_unit_normal(v1: np.ndarray, v2: np.ndarray, tol: float = 1e-6) -> np.ndarray:
     """Gets the unit normal of the vectors.
 
     Parameters
     ----------
     v1
         The first vector.
@@ -762,7 +742,56 @@
             indices.append(i)
             i = after[i]
         if i == 0:
             break
 
     meta_indices = earcut(verts[indices, :2], [len(indices)])
     return [indices[mi] for mi in meta_indices]
+
+
+def cartesian_to_spherical(vec):
+    norm = np.linalg.norm(vec)
+    if norm == 0:
+        return 0, 0, 0
+    r = norm
+    theta = np.arccos(vec[2] / r)
+    phi = np.arctan2(vec[1], vec[0])
+    return r, theta, phi
+
+
+def spherical_to_cartesian(r, theta, phi):
+    return np.array(
+        [
+            r * np.cos(phi) * np.sin(theta),
+            r * np.sin(phi) * np.sin(theta),
+            r * np.cos(theta),
+        ]
+    )
+
+
+def perpendicular_bisector(
+    line: Sequence[np.ndarray], norm_vector=OUT
+) -> Sequence[np.ndarray]:
+    """Returns a list of two points that correspond
+    to the ends of the perpendicular bisector of the
+    two points given.
+
+    Parameters
+    ----------
+    line
+        a list of two numpy array points (corresponding
+        to the ends of a line).
+    norm_vector
+        the vector perpendicular to both the line given
+        and the perpendicular bisector.
+
+    Returns
+    -------
+    list
+        A list of two numpy array points that correspond
+        to the ends of the perpendicular bisector
+    """
+    p1 = line[0]
+    p2 = line[1]
+    direction = np.cross(p1 - p2, norm_vector)
+    m = midpoint(p1, p2)
+    return [m + direction, m - direction]
```

### Comparing `manim-0.8.0/manim/utils/strings.py` & `manim-0.9.0/manim/utils/strings.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/tex.py` & `manim-0.9.0/manim/utils/tex.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/tex_file_writing.py` & `manim-0.9.0/manim/utils/tex_file_writing.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/tex_templates.py` & `manim-0.9.0/manim/utils/tex_templates.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/manim/utils/unit.py` & `manim-0.9.0/manim/utils/unit.py`

 * *Files identical despite different names*

### Comparing `manim-0.8.0/pyproject.toml` & `manim-0.9.0/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "manim"
-version = "0.8.0"
+version = "0.9.0"
 description = "Animation engine for explanatory math videos."
 authors = ["The Manim Community Developers","3b1b <grant@3blue1brown.com>"]
 license="MIT"
 readme="README.md"
 repository="https://github.com/manimcommunity/manim"
 documentation="https://docs.manim.community/"
 homepage="https://www.manim.community/"
@@ -26,15 +26,15 @@
 
 [tool.poetry.dependencies]
 python = "^3.7"
 click = ">=7.1<=9.0"
 click-default-group = "*"
 colour = "*"
 numpy = "^1.9"
-Pillow = "<8.3.0"  # can be removed when https://github.com/python-pillow/Pillow/issues/5571 is resolved
+Pillow = "*"
 scipy = "*"
 tqdm = "*"
 pydub = "*"
 pygments = "*"
 rich = ">=6.0"
 pycairo = "^1.19"
 manimpango = "^0.3.0"
@@ -47,15 +47,15 @@
 watchdog = "*"
 jupyterlab = { version = "^3.0", optional = true }
 moderngl = "^5.6.3"
 moderngl-window = "^2.3.0"
 mapbox-earcut = "^0.12.10"
 cloup = "^0.7.0"
 requests = "*"
-dearpygui = { version = "^0.6.415", optional = true }
+dearpygui = { version = "^0.8", optional = true }
 screeninfo = "^0.6.7"
 
 [tool.poetry.extras]
 webgl_renderer = ["grpcio","grpcio-tools"]
 jupyterlab = ["jupyterlab"]
 gui = ["dearpygui"]
```

### Comparing `manim-0.8.0/setup.py` & `manim-0.9.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -42,15 +42,15 @@
                     'shaders/textured_surface/*',
                     'shaders/true_dot/*',
                     'shaders/vectorized_mobject_fill/*',
                     'shaders/vectorized_mobject_stroke/*',
                     'shaders/vertex_colors/*']}
 
 install_requires = \
-['Pillow<8.3.0',
+['Pillow',
  'click-default-group',
  'click>=7.1',
  'cloup>=0.7.0,<0.8.0',
  'colour',
  'decorator>=5.0.7,<6.0.0',
  'manimpango>=0.3.0,<0.4.0',
  'mapbox-earcut>=0.12.10,<0.13.0',
@@ -67,27 +67,27 @@
  'screeninfo>=0.6.7,<0.7.0',
  'setuptools',
  'tqdm',
  'watchdog']
 
 extras_require = \
 {':python_version < "3.8"': ['importlib-metadata'],
- 'gui': ['dearpygui>=0.6.415,<0.7.0'],
+ 'gui': ['dearpygui>=0.8,<0.9'],
  'jupyterlab': ['jupyterlab>=3.0,<4.0'],
  'webgl_renderer': ['grpcio>=1.33.0,<1.34.0', 'grpcio-tools>=1.33.0,<1.34.0']}
 
 entry_points = \
 {'console_scripts': ['manim = manim.__main__:main',
                      'manimce = manim.__main__:main']}
 
 setup_kwargs = {
     'name': 'manim',
-    'version': '0.8.0',
+    'version': '0.9.0',
     'description': 'Animation engine for explanatory math videos.',
-    'long_description': '<p align="center">\n    <a href="https://www.manim.community/"><img src="https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png"></a>\n    <br />\n    <br />\n    <a href="https://pypi.org/project/manim/"><img src="https://img.shields.io/pypi/v/manim.svg?style=flat&logo=pypi" alt="PyPI Latest Release"></a>\n    <a href="https://hub.docker.com/r/manimcommunity/manim"><img src="https://img.shields.io/docker/v/manimcommunity/manim?color=%23099cec&label=docker%20image&logo=docker" alt="Docker image"> </a>\n    <a href="https://mybinder.org/v2/gh/ManimCommunity/jupyter_examples/HEAD?filepath=basic_example_scenes.ipynb"><img src="https://mybinder.org/badge_logo.svg"></a>\n    <a href="http://choosealicense.com/licenses/mit/"><img src="https://img.shields.io/badge/license-MIT-red.svg?style=flat" alt="MIT License"></a>\n    <a href="https://www.reddit.com/r/manim/"><img src="https://img.shields.io/reddit/subreddit-subscribers/manim.svg?color=orange&label=reddit&logo=reddit" alt="Reddit" href=></a>\n    <a href="https://twitter.com/manim_community/"><img src="https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40manim_community" alt="Twitter">\n    <a href="https://www.manim.community/discord/"><img src="https://img.shields.io/discord/581738731934056449.svg?label=discord&color=yellow&logo=discord" alt="Discord"></a>\n    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">\n    <a href="https://docs.manim.community/"><img src="https://readthedocs.org/projects/manimce/badge/?version=latest" alt="Documentation Status"></a>\n    <a href="https://pepy.tech/project/manim"><img src="https://pepy.tech/badge/manim/month?" alt="Downloads"> </a>\n    <img src="https://github.com/ManimCommunity/manim/workflows/CI/badge.svg" alt="CI">\n    <br />\n    <br />\n    <i>An animation engine for explanatory math videos</i>\n</p>\n<hr />\n\nManim is an animation engine for explanatory math videos. It\'s used to create precise animations programmatically, as demonstrated in the videos of [3Blue1Brown](https://www.3blue1brown.com/).\n\n> NOTE: This repository is maintained by the Manim Community, and is not associated with Grant Sanderson or 3Blue1Brown in any way (although we are definitely indebted to him for providing his work to the world). If you would like to study how Grant makes his videos, head over to his repository ([3b1b/manim](https://github.com/3b1b/manim)). This fork is updated more frequently than his, and it\'s recommended to use this fork if you\'d like to use Manim for your own projects.\n\n## Table of Contents:\n\n-  [Installation](#installation)\n-  [Usage](#usage)\n-  [Documentation](#documentation)\n-  [Docker](#docker)\n-  [Help with Manim](#help-with-manim)\n-  [Contributing](#contributing)\n-  [License](#license)\n\n## Installation\n\nManim requires a few dependencies that must be installed prior to using it. If you\nwant to try it out first before installing it locally, you can do so\n[in our online Jupyter environment](https://mybinder.org/v2/gist/behackl/725d956ec80969226b7bf9b4aef40b78/HEAD?filepath=basic%20example%20scenes.ipynb).\n\nFor the local installation, please visit the [Documentation](https://docs.manim.community/en/stable/installation.html)\nand follow the appropriate instructions for your operating system.\n\nOnce the dependencies have been installed, run the following in a terminal window:\n\n```bash\npip install manim\n```\n\n## Usage\n\nManim is an extremely versatile package. The following is an example `Scene` you can construct:\n\n```python\nfrom manim import *\n\n\nclass SquareToCircle(Scene):\n    def construct(self):\n        circle = Circle()\n        square = Square()\n        square.flip(RIGHT)\n        square.rotate(-3 * TAU / 8)\n        circle.set_fill(PINK, opacity=0.5)\n\n        self.play(Create(square))\n        self.play(Transform(square, circle))\n        self.play(FadeOut(square))\n```\n\nIn order to view the output of this scene, save the code in a file called `example.py`. Then, run the following in a terminal window:\n\n```sh\nmanim -p -ql example.py SquareToCircle\n```\n\nYou should see your native video player program pop up and play a simple scene in which a square is transformed into a circle. You may find some more simple examples within this\n[GitHub repository](example_scenes). You can also visit the [official gallery](https://docs.manim.community/en/stable/examples.html) for more advanced examples.\n\nManim also ships with a `%%manim` IPython magic which allows to use it conveniently in JupyterLab (as well as classic Jupyter) notebooks. See the\n\n[corresponding documentation](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html) for some guidance and\n[try it out online](https://mybinder.org/v2/gh/ManimCommunity/jupyter_examples/HEAD?filepath=basic_example_scenes.ipynb).\n\n## Command line arguments\n\nThe general usage of Manim is as follows:\n\n![manim-illustration](https://raw.githubusercontent.com/ManimCommunity/manim/main/docs/source/_static/command.png)\n\nThe `-p` flag in the command above is for previewing, meaning the video file will automatically open when it is done rendering. The `-ql` flag is for a faster rendering at a lower quality.\n\nSome other useful flags include:\n\n-  `-s` to skip to the end and just show the final frame.\n-  `-n <number>` to skip ahead to the `n`\'th animation of a scene.\n-  `-f` show the file in the file browser.\n\nFor a thorough list of command line arguments, visit the [documentation](https://docs.manim.community/en/stable/tutorials/configuration.html).\n\n## Documentation\n\nDocumentation is in progress at [ReadTheDocs](https://docs.manim.community/).\n\n## Docker\n\nThe community also maintains a docker image (`manimcommunity/manim`), which can be found [on DockerHub](https://hub.docker.com/r/manimcommunity/manim). The following tags are supported:\n\n- `latest` -- the most recent version corresponding to [the main branch](https://github.com/ManimCommunity/manim)\n- `stable` -- the latest released version (according to [the releases page](https://github.com/ManimCommunity/manim/releases))\n- `vX.Y.Z` -- any particular released version (according to [the releases page](https://github.com/ManimCommunity/manim/releases))\n\n### Instructions for running the docker image\n\n#### Quick Example\nTo render a scene `CircleToSquare` in a file `test_scenes.py` contained in your current working directory while preserving your user and group ID, use\n```\ndocker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/manim manimcommunity/manim manim test_scenes.py CircleToSquare -qm\n```\n\n#### Running the image in the background\nInstead of using the "throwaway container" approach sketched above, you can also create a named container that you can also modify to your liking. First, run\n```\ndocker run -it --name my-manim-container -v "$(pwd):/manim" manimcommunity/manim /bin/bash\n```\nto obtain an interactive shell inside your container allowing you to, e.g., install further dependencies (like texlive packages using `tlmgr`). Exit the container as soon as you are satisfied. Then, before using it, start the container by running\n```\ndocker start my-manim-container\n```\nThen, to render a scene `CircleToSquare` in a file `test_scenes.py`, call\n```\ndocker exec -it --user="$(id -u):$(id -g)" my-manim-container manim test.py CircleToSquare -qm\n```\n\n#### Jupyterlab\nAnother alternative is to use the docker image to spin up a local webserver running\nJupyterLab in whose Python kernel manim is installed and can be accessed via the `%%manim` cell magic.\nTo use JupyterLab, run\n```\ndocker run -it -p 8888:8888 manimcommunity/manim jupyter lab --ip=0.0.0.0\n```\nand then follow the instructions in the terminal.\n\n#### Important notes\n\nWhen executing `manim` within a Docker container, several command line flags (in particular `-p` (preview file) and `-f` (show output file in the file browser)) are not supported.\n\n## Help with Manim\n\nIf you need help installing or using Manim, feel free to reach out to our [Discord\nServer](https://www.manim.community/discord/) or [Reddit Community](https://www.reddit.com/r/manim). If you would like to submit a bug report or feature request, please open an issue.\n\n## Contributing\n\nContributions to Manim are always welcome. In particular, there is a dire need for tests and documentation. For contribution guidelines, please see the [documentation](https://docs.manim.community/en/stable/contributing.html).\n\nMost developers on the project use [Poetry](https://python-poetry.org/docs/) for management. You\'ll want to have poetry installed and available in your environment. You can learn more about `poetry` and how to use it at its [documentation](https://docs.manim.community/en/stable/installation/for_dev.html).\n\n## How to Cite Manim\n\nWe acknowledge the importance of good software to support research, and we note\nthat research becomes more valuable when it is communicated effectively. To\ndemonstrate the value of Manim, we ask that you cite Manim in your work.\nCurrently, the best way to cite Manim is to reference the\n[Manim home page](https://www.manim.community) using this BibTeX entry (the\nentry is for release `v0.6.0`, but can be adapted easily):\n\n```\n@Manual{Manim:v0.6.0,\n  key =          {Manim},\n  author =       {{The Manim Community Developers}},\n  title =        {{Manim} -- {M}athematical {A}nimation {F}ramework ({V}ersion v0.6.0)},\n  note =         {\\url{https://www.manim.community}},\n  year =         2021,\n}\n```\n\nThis should render a reference that looks more or less like this:\n\n42. The Manim Community Developers,\n    [Manim – Mathematical Animation Framework (Version v0.6.0)](https://www.manim.community).\n    2021.\n\n## Code of Conduct\n\nOur full code of conduct, and how we enforce it, can be read on [our website](https://docs.manim.community/en/stable/conduct.html).\n\n## License\n\nThe software is double-licensed under the MIT license, with copyright by 3blue1brown LLC (see LICENSE), and copyright by Manim Community Developers (see LICENSE.community).\n',
+    'long_description': '<p align="center">\n    <a href="https://www.manim.community/"><img src="https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png"></a>\n    <br />\n    <br />\n    <a href="https://pypi.org/project/manim/"><img src="https://img.shields.io/pypi/v/manim.svg?style=flat&logo=pypi" alt="PyPI Latest Release"></a>\n    <a href="https://hub.docker.com/r/manimcommunity/manim"><img src="https://img.shields.io/docker/v/manimcommunity/manim?color=%23099cec&label=docker%20image&logo=docker" alt="Docker image"> </a>\n    <a href="https://mybinder.org/v2/gh/ManimCommunity/jupyter_examples/HEAD?filepath=basic_example_scenes.ipynb"><img src="https://mybinder.org/badge_logo.svg"></a>\n    <a href="http://choosealicense.com/licenses/mit/"><img src="https://img.shields.io/badge/license-MIT-red.svg?style=flat" alt="MIT License"></a>\n    <a href="https://www.reddit.com/r/manim/"><img src="https://img.shields.io/reddit/subreddit-subscribers/manim.svg?color=orange&label=reddit&logo=reddit" alt="Reddit" href=></a>\n    <a href="https://twitter.com/manim_community/"><img src="https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40manim_community" alt="Twitter">\n    <a href="https://www.manim.community/discord/"><img src="https://img.shields.io/discord/581738731934056449.svg?label=discord&color=yellow&logo=discord" alt="Discord"></a>\n    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">\n    <a href="https://docs.manim.community/"><img src="https://readthedocs.org/projects/manimce/badge/?version=latest" alt="Documentation Status"></a>\n    <a href="https://pepy.tech/project/manim"><img src="https://pepy.tech/badge/manim/month?" alt="Downloads"> </a>\n    <img src="https://github.com/ManimCommunity/manim/workflows/CI/badge.svg" alt="CI">\n    <br />\n    <br />\n    <i>An animation engine for explanatory math videos</i>\n</p>\n<hr />\n\nManim is an animation engine for explanatory math videos. It\'s used to create precise animations programmatically, as demonstrated in the videos of [3Blue1Brown](https://www.3blue1brown.com/).\n\n> NOTE: This repository is maintained by the Manim Community, and is not associated with Grant Sanderson or 3Blue1Brown in any way (although we are definitely indebted to him for providing his work to the world). If you would like to study how Grant makes his videos, head over to his repository ([3b1b/manim](https://github.com/3b1b/manim)). This fork is updated more frequently than his, and it\'s recommended to use this fork if you\'d like to use Manim for your own projects.\n\n## Table of Contents:\n\n-  [Installation](#installation)\n-  [Usage](#usage)\n-  [Documentation](#documentation)\n-  [Docker](#docker)\n-  [Help with Manim](#help-with-manim)\n-  [Contributing](#contributing)\n-  [License](#license)\n\n## Installation\n> **WARNING:** These instructions are for the community version _only_. Trying to use these instructions to install [3b1b/manim](https://github.com/3b1b/manim) or instructions there to install this version will cause problems. Read [this](https://docs.manim.community/en/stable/installation/versions.html) and decide which version you wish to install, then only follow the instructions for your desired version.\n        \nManim requires a few dependencies that must be installed prior to using it. If you\nwant to try it out first before installing it locally, you can do so\n[in our online Jupyter environment](https://mybinder.org/v2/gist/behackl/725d956ec80969226b7bf9b4aef40b78/HEAD?filepath=basic%20example%20scenes.ipynb).\n\nFor local installation, please visit the [Documentation](https://docs.manim.community/en/stable/installation.html)\nand follow the appropriate instructions for your operating system.\n       \n## Usage\n\nManim is an extremely versatile package. The following is an example `Scene` you can construct:\n\n```python\nfrom manim import *\n\n\nclass SquareToCircle(Scene):\n    def construct(self):\n        circle = Circle()\n        square = Square()\n        square.flip(RIGHT)\n        square.rotate(-3 * TAU / 8)\n        circle.set_fill(PINK, opacity=0.5)\n\n        self.play(Create(square))\n        self.play(Transform(square, circle))\n        self.play(FadeOut(square))\n```\n\nIn order to view the output of this scene, save the code in a file called `example.py`. Then, run the following in a terminal window:\n\n```sh\nmanim -p -ql example.py SquareToCircle\n```\n\nYou should see your native video player program pop up and play a simple scene in which a square is transformed into a circle. You may find some more simple examples within this\n[GitHub repository](example_scenes). You can also visit the [official gallery](https://docs.manim.community/en/stable/examples.html) for more advanced examples.\n\nManim also ships with a `%%manim` IPython magic which allows to use it conveniently in JupyterLab (as well as classic Jupyter) notebooks. See the\n\n[corresponding documentation](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html) for some guidance and\n[try it out online](https://mybinder.org/v2/gh/ManimCommunity/jupyter_examples/HEAD?filepath=basic_example_scenes.ipynb).\n\n## Command line arguments\n\nThe general usage of Manim is as follows:\n\n![manim-illustration](https://raw.githubusercontent.com/ManimCommunity/manim/main/docs/source/_static/command.png)\n\nThe `-p` flag in the command above is for previewing, meaning the video file will automatically open when it is done rendering. The `-ql` flag is for a faster rendering at a lower quality.\n\nSome other useful flags include:\n\n-  `-s` to skip to the end and just show the final frame.\n-  `-n <number>` to skip ahead to the `n`\'th animation of a scene.\n-  `-f` show the file in the file browser.\n\nFor a thorough list of command line arguments, visit the [documentation](https://docs.manim.community/en/stable/tutorials/configuration.html).\n\n## Documentation\n\nDocumentation is in progress at [ReadTheDocs](https://docs.manim.community/).\n\n## Docker\n\nThe community also maintains a docker image (`manimcommunity/manim`), which can be found [on DockerHub](https://hub.docker.com/r/manimcommunity/manim). The following tags are supported:\n\n- `latest` -- the most recent version corresponding to [the main branch](https://github.com/ManimCommunity/manim)\n- `stable` -- the latest released version (according to [the releases page](https://github.com/ManimCommunity/manim/releases))\n- `vX.Y.Z` -- any particular released version (according to [the releases page](https://github.com/ManimCommunity/manim/releases))\n\n### Instructions for running the docker image\n\n#### Quick Example\nTo render a scene `CircleToSquare` in a file `test_scenes.py` contained in your current working directory while preserving your user and group ID, use\n```\ndocker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/manim manimcommunity/manim manim test_scenes.py CircleToSquare -qm\n```\n\n#### Running the image in the background\nInstead of using the "throwaway container" approach sketched above, you can also create a named container that you can also modify to your liking. First, run\n```\ndocker run -it --name my-manim-container -v "$(pwd):/manim" manimcommunity/manim /bin/bash\n```\nto obtain an interactive shell inside your container allowing you to, e.g., install further dependencies (like texlive packages using `tlmgr`). Exit the container as soon as you are satisfied. Then, before using it, start the container by running\n```\ndocker start my-manim-container\n```\nThen, to render a scene `CircleToSquare` in a file `test_scenes.py`, call\n```\ndocker exec -it --user="$(id -u):$(id -g)" my-manim-container manim test.py CircleToSquare -qm\n```\n\n#### Jupyterlab\nAnother alternative is to use the docker image to spin up a local webserver running\nJupyterLab in whose Python kernel manim is installed and can be accessed via the `%%manim` cell magic.\nTo use JupyterLab, run\n```\ndocker run -it -p 8888:8888 manimcommunity/manim jupyter lab --ip=0.0.0.0\n```\nand then follow the instructions in the terminal.\n\n#### Important notes\n\nWhen executing `manim` within a Docker container, several command line flags (in particular `-p` (preview file) and `-f` (show output file in the file browser)) are not supported.\n\n## Help with Manim\n\nIf you need help installing or using Manim, feel free to reach out to our [Discord\nServer](https://www.manim.community/discord/) or [Reddit Community](https://www.reddit.com/r/manim). If you would like to submit a bug report or feature request, please open an issue.\n\n## Contributing\n\nContributions to Manim are always welcome. In particular, there is a dire need for tests and documentation. For contribution guidelines, please see the [documentation](https://docs.manim.community/en/stable/contributing.html).\n\nMost developers on the project use [Poetry](https://python-poetry.org/docs/) for management. You\'ll want to have poetry installed and available in your environment. You can learn more about `poetry` and how to use it at its [documentation](https://docs.manim.community/en/stable/installation/for_dev.html).\n\n## How to Cite Manim\n\nWe acknowledge the importance of good software to support research, and we note\nthat research becomes more valuable when it is communicated effectively. To\ndemonstrate the value of Manim, we ask that you cite Manim in your work.\nCurrently, the best way to cite Manim is to reference the\n[Manim home page](https://www.manim.community) using this BibTeX entry (the\nentry is for release `v0.9.0`, but can be adapted easily):\n\n```\n@Manual{Manim:v0.9.0,\n  key =          {Manim},\n  author =       {{The Manim Community Developers}},\n  title =        {{Manim} -- {M}athematical {A}nimation {F}ramework ({V}ersion v0.9.0)},\n  note =         {\\url{https://www.manim.community}},\n  year =         2021,\n}\n```\n\nThis should render a reference that looks more or less like this:\n\n42. The Manim Community Developers,\n    [Manim – Mathematical Animation Framework (Version v0.9.0)](https://www.manim.community).\n    2021.\n\n## Code of Conduct\n\nOur full code of conduct, and how we enforce it, can be read on [our website](https://docs.manim.community/en/stable/conduct.html).\n\n## License\n\nThe software is double-licensed under the MIT license, with copyright by 3blue1brown LLC (see LICENSE), and copyright by Manim Community Developers (see LICENSE.community).\n',
     'author': 'The Manim Community Developers',
     'author_email': None,
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://www.manim.community/',
     'packages': packages,
     'package_data': package_data,
```

#### html2text {}

```diff
@@ -7,26 +7,26 @@
 'manim.utils'] package_data = \ {'': ['*'], 'manim': ['templates/*'],
 'manim.grpc': ['proto/*'], 'manim.renderer': ['shaders/*', 'shaders/default/*',
 'shaders/image/*', 'shaders/include/*', 'shaders/inserts/*', 'shaders/
 manim_coords/*', 'shaders/quadratic_bezier_fill/*', 'shaders/
 quadratic_bezier_stroke/*', 'shaders/surface/*', 'shaders/test/*', 'shaders/
 textured_surface/*', 'shaders/true_dot/*', 'shaders/vectorized_mobject_fill/*',
 'shaders/vectorized_mobject_stroke/*', 'shaders/vertex_colors/*']}
-install_requires = \ ['Pillow<8.3.0', 'click-default-group', 'click>=7.1',
+install_requires = \ ['Pillow', 'click-default-group', 'click>=7.1',
 'cloup>=0.7.0,<0.8.0', 'colour', 'decorator>=5.0.7,<6.0.0',
 'manimpango>=0.3.0,<0.4.0', 'mapbox-earcut>=0.12.10,<0.13.0', 'moderngl-
 window>=2.3.0,<3.0.0', 'moderngl>=5.6.3,<6.0.0', 'networkx>=2.5,<3.0',
 'numpy>=1.9,<2.0', 'pycairo>=1.19,<2.0', 'pydub', 'pygments', 'requests',
 'rich>=6.0', 'scipy', 'screeninfo>=0.6.7,<0.7.0', 'setuptools', 'tqdm',
 'watchdog'] extras_require = \ {':python_version < "3.8"': ['importlib-
-metadata'], 'gui': ['dearpygui>=0.6.415,<0.7.0'], 'jupyterlab':
+metadata'], 'gui': ['dearpygui>=0.8,<0.9'], 'jupyterlab':
 ['jupyterlab>=3.0,<4.0'], 'webgl_renderer': ['grpcio>=1.33.0,<1.34.0', 'grpcio-
 tools>=1.33.0,<1.34.0']} entry_points = \ {'console_scripts': ['manim =
 manim.__main__:main', 'manimce = manim.__main__:main']} setup_kwargs =
-{ 'name': 'manim', 'version': '0.8.0', 'description': 'Animation engine for
+{ 'name': 'manim', 'version': '0.9.0', 'description': 'Animation engine for
 explanatory math videos.', 'long_description': '
      \n [https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/
                                 cropped.png]\n
                                       \n
       \n [PyPI_Latest_Release]\n [Docker_image]\n [https://mybinder.org/
   badge_logo.svg]\n [MIT_License]\n [Reddit]\n [Twitter]\n_[Discord]\n_[Code
         style:_black]\n_[Documentation_Status]\n_[Downloads]\n_[CI]\n_
@@ -42,41 +42,45 @@
 providing his work to the world). If you would like to study how Grant makes
 his videos, head over to his repository ([3b1b/manim](https://github.com/3b1b/
 manim)). This fork is updated more frequently than his, and it\'s recommended
 to use this fork if you\'d like to use Manim for your own projects.\n\n## Table
 of Contents:\n\n- [Installation](#installation)\n- [Usage](#usage)\n-
 [Documentation](#documentation)\n- [Docker](#docker)\n- [Help with Manim]
 (#help-with-manim)\n- [Contributing](#contributing)\n- [License]
-(#license)\n\n## Installation\n\nManim requires a few dependencies that must be
-installed prior to using it. If you\nwant to try it out first before installing
-it locally, you can do so\n[in our online Jupyter environment](https://
-mybinder.org/v2/gist/behackl/725d956ec80969226b7bf9b4aef40b78/
-HEAD?filepath=basic%20example%20scenes.ipynb).\n\nFor the local installation,
+(#license)\n\n## Installation\n> **WARNING:** These instructions are for the
+community version _only_. Trying to use these instructions to install [3b1b/
+manim](https://github.com/3b1b/manim) or instructions there to install this
+version will cause problems. Read [this](https://docs.manim.community/en/
+stable/installation/versions.html) and decide which version you wish to
+install, then only follow the instructions for your desired version.\n \nManim
+requires a few dependencies that must be installed prior to using it. If
+you\nwant to try it out first before installing it locally, you can do so\n[in
+our online Jupyter environment](https://mybinder.org/v2/gist/behackl/
+725d956ec80969226b7bf9b4aef40b78/
+HEAD?filepath=basic%20example%20scenes.ipynb).\n\nFor local installation,
 please visit the [Documentation](https://docs.manim.community/en/stable/
 installation.html)\nand follow the appropriate instructions for your operating
-system.\n\nOnce the dependencies have been installed, run the following in a
-terminal window:\n\n```bash\npip install manim\n```\n\n## Usage\n\nManim is an
-extremely versatile package. The following is an example `Scene` you can
-construct:\n\n```python\nfrom manim import *\n\n\nclass SquareToCircle(Scene):
-\n def construct(self):\n circle = Circle()\n square = Square()\n square.flip
-(RIGHT)\n square.rotate(-3 * TAU / 8)\n circle.set_fill(PINK, opacity=0.5)\n\n
-self.play(Create(square))\n self.play(Transform(square, circle))\n self.play
-(FadeOut(square))\n```\n\nIn order to view the output of this scene, save the
-code in a file called `example.py`. Then, run the following in a terminal
-window:\n\n```sh\nmanim -p -ql example.py SquareToCircle\n```\n\nYou should see
-your native video player program pop up and play a simple scene in which a
-square is transformed into a circle. You may find some more simple examples
-within this\n[GitHub repository](example_scenes). You can also visit the
-[official gallery](https://docs.manim.community/en/stable/examples.html) for
-more advanced examples.\n\nManim also ships with a `%%manim` IPython magic
-which allows to use it conveniently in JupyterLab (as well as classic Jupyter)
-notebooks. See the\n\n[corresponding documentation](https://
-docs.manim.community/en/stable/reference/
-manim.utils.ipython_magic.ManimMagic.html) for some guidance and\n[try it out
-online](https://mybinder.org/v2/gh/ManimCommunity/jupyter_examples/
+system.\n \n## Usage\n\nManim is an extremely versatile package. The following
+is an example `Scene` you can construct:\n\n```python\nfrom manim import
+*\n\n\nclass SquareToCircle(Scene):\n def construct(self):\n circle = Circle
+()\n square = Square()\n square.flip(RIGHT)\n square.rotate(-3 * TAU / 8)\n
+circle.set_fill(PINK, opacity=0.5)\n\n self.play(Create(square))\n self.play
+(Transform(square, circle))\n self.play(FadeOut(square))\n```\n\nIn order to
+view the output of this scene, save the code in a file called `example.py`.
+Then, run the following in a terminal window:\n\n```sh\nmanim -p -ql example.py
+SquareToCircle\n```\n\nYou should see your native video player program pop up
+and play a simple scene in which a square is transformed into a circle. You may
+find some more simple examples within this\n[GitHub repository]
+(example_scenes). You can also visit the [official gallery](https://
+docs.manim.community/en/stable/examples.html) for more advanced
+examples.\n\nManim also ships with a `%%manim` IPython magic which allows to
+use it conveniently in JupyterLab (as well as classic Jupyter) notebooks. See
+the\n\n[corresponding documentation](https://docs.manim.community/en/stable/
+reference/manim.utils.ipython_magic.ManimMagic.html) for some guidance and\n
+[try it out online](https://mybinder.org/v2/gh/ManimCommunity/jupyter_examples/
 HEAD?filepath=basic_example_scenes.ipynb).\n\n## Command line arguments\n\nThe
 general usage of Manim is as follows:\n\n![manim-illustration](https://
 raw.githubusercontent.com/ManimCommunity/manim/main/docs/source/_static/
 command.png)\n\nThe `-p` flag in the command above is for previewing, meaning
 the video file will automatically open when it is done rendering. The `-ql`
 flag is for a faster rendering at a lower quality.\n\nSome other useful flags
 include:\n\n- `-s` to skip to the end and just show the final frame.\n- `-n `
@@ -128,20 +132,20 @@
 use it at its [documentation](https://docs.manim.community/en/stable/
 installation/for_dev.html).\n\n## How to Cite Manim\n\nWe acknowledge the
 importance of good software to support research, and we note\nthat research
 becomes more valuable when it is communicated effectively. To\ndemonstrate the
 value of Manim, we ask that you cite Manim in your work.\nCurrently, the best
 way to cite Manim is to reference the\n[Manim home page](https://
 www.manim.community) using this BibTeX entry (the\nentry is for release
-`v0.6.0`, but can be adapted easily):\n\n```\n@Manual{Manim:v0.6.0,\n key =
+`v0.9.0`, but can be adapted easily):\n\n```\n@Manual{Manim:v0.9.0,\n key =
 {Manim},\n author = {{The Manim Community Developers}},\n title = {{Manim} --
-{M}athematical {A}nimation {F}ramework ({V}ersion v0.6.0)},\n note = {\\url
+{M}athematical {A}nimation {F}ramework ({V}ersion v0.9.0)},\n note = {\\url
 {https://www.manim.community}},\n year = 2021,\n}\n```\n\nThis should render a
 reference that looks more or less like this:\n\n42. The Manim Community
-Developers,\n [Manim â Mathematical Animation Framework (Version v0.6.0)]
+Developers,\n [Manim â Mathematical Animation Framework (Version v0.9.0)]
 (https://www.manim.community).\n 2021.\n\n## Code of Conduct\n\nOur full code
 of conduct, and how we enforce it, can be read on [our website](https://
 docs.manim.community/en/stable/conduct.html).\n\n## License\n\nThe software is
 double-licensed under the MIT license, with copyright by 3blue1brown LLC (see
 LICENSE), and copyright by Manim Community Developers (see
 LICENSE.community).\n', 'author': 'The Manim Community Developers',
 'author_email': None, 'maintainer': None, 'maintainer_email': None, 'url':
```

### Comparing `manim-0.8.0/PKG-INFO` & `manim-0.9.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manim
-Version: 0.8.0
+Version: 0.9.0
 Summary: Animation engine for explanatory math videos.
 Home-page: https://www.manim.community/
 License: MIT
 Author: The Manim Community Developers
 Requires-Python: >=3.7,<4.0
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: MIT License
@@ -16,20 +16,20 @@
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Multimedia :: Graphics
 Classifier: Topic :: Multimedia :: Video
 Classifier: Topic :: Scientific/Engineering
 Provides-Extra: gui
 Provides-Extra: jupyterlab
 Provides-Extra: webgl_renderer
-Requires-Dist: Pillow (<8.3.0)
+Requires-Dist: Pillow
 Requires-Dist: click (>=7.1)
 Requires-Dist: click-default-group
 Requires-Dist: cloup (>=0.7.0,<0.8.0)
 Requires-Dist: colour
-Requires-Dist: dearpygui (>=0.6.415,<0.7.0); extra == "gui"
+Requires-Dist: dearpygui (>=0.8,<0.9); extra == "gui"
 Requires-Dist: decorator (>=5.0.7,<6.0.0)
 Requires-Dist: grpcio (>=1.33.0,<1.34.0); extra == "webgl_renderer"
 Requires-Dist: grpcio-tools (>=1.33.0,<1.34.0); extra == "webgl_renderer"
 Requires-Dist: importlib-metadata; python_version < "3.8"
 Requires-Dist: jupyterlab (>=3.0,<4.0); extra == "jupyterlab"
 Requires-Dist: manimpango (>=0.3.0,<0.4.0)
 Requires-Dist: mapbox-earcut (>=0.12.10,<0.13.0)
@@ -87,28 +87,23 @@
 -  [Documentation](#documentation)
 -  [Docker](#docker)
 -  [Help with Manim](#help-with-manim)
 -  [Contributing](#contributing)
 -  [License](#license)
 
 ## Installation
-
+> **WARNING:** These instructions are for the community version _only_. Trying to use these instructions to install [3b1b/manim](https://github.com/3b1b/manim) or instructions there to install this version will cause problems. Read [this](https://docs.manim.community/en/stable/installation/versions.html) and decide which version you wish to install, then only follow the instructions for your desired version.
+        
 Manim requires a few dependencies that must be installed prior to using it. If you
 want to try it out first before installing it locally, you can do so
 [in our online Jupyter environment](https://mybinder.org/v2/gist/behackl/725d956ec80969226b7bf9b4aef40b78/HEAD?filepath=basic%20example%20scenes.ipynb).
 
-For the local installation, please visit the [Documentation](https://docs.manim.community/en/stable/installation.html)
+For local installation, please visit the [Documentation](https://docs.manim.community/en/stable/installation.html)
 and follow the appropriate instructions for your operating system.
-
-Once the dependencies have been installed, run the following in a terminal window:
-
-```bash
-pip install manim
-```
-
+       
 ## Usage
 
 Manim is an extremely versatile package. The following is an example `Scene` you can construct:
 
 ```python
 from manim import *
 
@@ -217,30 +212,30 @@
 ## How to Cite Manim
 
 We acknowledge the importance of good software to support research, and we note
 that research becomes more valuable when it is communicated effectively. To
 demonstrate the value of Manim, we ask that you cite Manim in your work.
 Currently, the best way to cite Manim is to reference the
 [Manim home page](https://www.manim.community) using this BibTeX entry (the
-entry is for release `v0.6.0`, but can be adapted easily):
+entry is for release `v0.9.0`, but can be adapted easily):
 
 ```
-@Manual{Manim:v0.6.0,
+@Manual{Manim:v0.9.0,
   key =          {Manim},
   author =       {{The Manim Community Developers}},
-  title =        {{Manim} -- {M}athematical {A}nimation {F}ramework ({V}ersion v0.6.0)},
+  title =        {{Manim} -- {M}athematical {A}nimation {F}ramework ({V}ersion v0.9.0)},
   note =         {\url{https://www.manim.community}},
   year =         2021,
 }
 ```
 
 This should render a reference that looks more or less like this:
 
 42. The Manim Community Developers,
-    [Manim – Mathematical Animation Framework (Version v0.6.0)](https://www.manim.community).
+    [Manim – Mathematical Animation Framework (Version v0.9.0)](https://www.manim.community).
     2021.
 
 ## Code of Conduct
 
 Our full code of conduct, and how we enforce it, can be read on [our website](https://docs.manim.community/en/stable/conduct.html).
 
 ## License
```

