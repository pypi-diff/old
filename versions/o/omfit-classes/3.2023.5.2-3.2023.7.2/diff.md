# Comparing `tmp/omfit_classes-3.2023.5.2.tar.gz` & `tmp/omfit_classes-3.2023.7.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/omfit_classes-3.2023.5.2.tar", last modified: Sun Jan 29 21:36:27 2023, max compression
+gzip compressed data, was "dist/omfit_classes-3.2023.7.2.tar", last modified: Sun Feb 12 13:41:25 2023, max compression
```

## Comparing `omfit_classes-3.2023.5.2.tar` & `omfit_classes-3.2023.7.2.tar`

### file list

```diff
@@ -1,719 +1,719 @@
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/
--rw-r--r--   0 fusionbot   (505) staff       (20)     1067 2023-01-28 03:10:14.000000 omfit_classes-3.2023.5.2/LICENSE.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)     1178 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/PKG-INFO
--rw-r--r--   0 fusionbot   (505) staff       (20)      942 2023-01-28 03:10:14.000000 omfit_classes-3.2023.5.2/README.rst
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:14.000000 omfit_classes-3.2023.5.2/__init__.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/classes/
--rw-r--r--   0 fusionbot   (505) staff       (20)      290 2023-01-28 03:10:14.000000 omfit_classes-3.2023.5.2/classes/__init__.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    27149 2023-01-28 03:10:14.000000 omfit_classes-3.2023.5.2/externalImports.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:14.000000 omfit_classes-3.2023.5.2/extras/__init__.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/
--rw-r--r--   0 fusionbot   (505) staff       (20)   385815 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/LOM.png
--rw-r--r--   0 fusionbot   (505) staff       (20)     6335 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_font.bf
--rw-r--r--   0 fusionbot   (505) staff       (20)     3044 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_font.ttf
--rw-r--r--   0 fusionbot   (505) staff       (20)     2087 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)    56012 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo.pdf
--rw-r--r--   0 fusionbot   (505) staff       (20)     3187 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_color.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)    59634 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_color.pdf
--rw-r--r--   0 fusionbot   (505) staff       (20)     6504 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_olympics.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)   179267 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_olympics.pdf
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/__init__.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/autoX.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/autoY.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/bookmark.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     8760 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/colors.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/copy.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/crosshair.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1512 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/error.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      277 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/events.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/
--rw-r--r--   0 fusionbot   (505) staff       (20)    25832 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Humor-Sans.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    52836 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Bold.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    53512 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-BoldItalic.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    48220 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-ExtraLight.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    49204 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-ExtraLightItalic.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    49760 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Italic.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    48856 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Light.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    49552 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-LightItalic.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    49488 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Semi-BoldItalic.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    49272 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-SemiBold.ttf
--rwxr-xr-x   0 fusionbot   (505) staff       (20)    49008 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli.ttf
--rw-r--r--   0 fusionbot   (505) staff       (20)     2334 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/fonts.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/help.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     2507 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/info.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/legend.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/linked.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/mail.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)      631 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/matplotlib_backends.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/paste.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/pdf.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     5370 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/pin.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     2472 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/question.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/select.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/settings.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/storage.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/text.ppm
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/
--rw-r--r--   0 fusionbot   (505) staff       (20)      600 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/CreateImageLib.def
--rw-r--r--   0 fusionbot   (505) staff       (20)    41722 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/ImageLib.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/LICENSE
--rw-r--r--   0 fusionbot   (505) staff       (20)     6971 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/aquativo.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)   112011 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/images.tgz
--rw-r--r--   0 fusionbot   (505) staff       (20)       95 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/black/
--rw-r--r--   0 fusionbot   (505) staff       (20)     2123 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/black/LICENSE
--rw-r--r--   0 fusionbot   (505) staff       (20)     4066 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/black/black.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)      209 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/black/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/
--rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/LICENSE
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/
--rw-r--r--   0 fusionbot   (505) staff       (20)      315 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowdown-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      312 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowdown-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      313 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowdown.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      329 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowleft-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      327 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowleft-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      323 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowleft.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowright-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      327 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowright-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      324 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowright.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      309 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowup-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      313 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowup-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      314 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/arrowup.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      696 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/button-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      770 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/button-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      769 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/button-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      254 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/check-hc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/check-hu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      249 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/check-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      229 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/check-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1098 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/radio-hc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      626 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/radio-hu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      389 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/radio-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      401 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/radio-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      343 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/sb-thumb-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      316 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/sb-thumb.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      333 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/sb-vthumb-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      308 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/sb-vthumb.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      182 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/slider-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      182 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/slider.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      183 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/vslider-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      283 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/vslider.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     4714 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)      188 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/blue/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/
--rw-r--r--   0 fusionbot   (505) staff       (20)     2226 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/LICENSE
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/
--rw-r--r--   0 fusionbot   (505) staff       (20)      245 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      230 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      246 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      248 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      248 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      252 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      251 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      250 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      235 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      252 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      251 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      244 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      228 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      248 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      247 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       63 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/blank.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      661 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      590 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      656 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      519 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      394 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-pa.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      331 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-ac.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-au.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-dc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-du.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      331 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      332 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-pc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/check-pu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      100 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      527 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-ra.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      512 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-rd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      550 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-rf.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      533 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-rn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      402 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-rp.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      441 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      432 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      451 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      450 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      281 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/progress-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      304 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/progress-v.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      356 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-ac.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-au.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      362 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-dc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-du.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      359 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      359 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-pc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      225 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/radio-pu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      276 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-ha.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      263 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-hd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      278 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-hn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      278 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-hp.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      266 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-va.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      262 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-vd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      271 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-vn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      271 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-vp.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      474 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scale-ha.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      336 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scale-hd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      477 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scale-hn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      526 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scale-va.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      342 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scale-vd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      511 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scale-vn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       87 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scaletrough-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      111 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scaletrough-v.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sep-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sep-v.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       77 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/sizegrip.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      536 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tab-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      549 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tab-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      554 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      499 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      557 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      527 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      333 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-pa.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      509 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tree-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      519 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tree-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      528 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tree-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      420 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tree-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)    11637 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)      406 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/
--rw-r--r--   0 fusionbot   (505) staff       (20)     2226 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/LICENSE
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/
--rw-r--r--   0 fusionbot   (505) staff       (20)       70 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/arrow-optionmenu-disabled.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       79 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/arrow-optionmenu-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       79 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/arrow-optionmenu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1954 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-active-disabled.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1953 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-active-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      872 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-active.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1267 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-default.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     2001 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      138 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/check1.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      145 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/check2.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/combo-active.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/entry-active.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/entry-inactive.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/grip-horiz-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/grip-horiz.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       59 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/grip-vert-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       59 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/grip-vert.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      700 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/list-header-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      706 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/list-header.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/option1.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      363 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/option2.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      995 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/progressbar-horiz.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      966 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/progressbar-vert.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/scale-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      320 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/scale.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      651 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-horiz-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      673 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-horiz.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      666 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-vert-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      722 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-vert.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      542 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-down-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      555 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-down.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      555 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-left-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      556 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-left.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      555 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-right-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      560 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-right.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      542 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-up-prelight.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      549 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-up.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      544 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/tab-top-active.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      583 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/tab-top.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       97 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-horiz.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      664 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-progressbar-horiz.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      677 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-progressbar-vert.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      803 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-horiz.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      871 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-vert.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      133 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-vert.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     9054 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)      154 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/
--rw-r--r--   0 fusionbot   (505) staff       (20)      203 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/arrow-down-insens.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      200 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/arrow-down-prelight.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      202 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/arrow-down.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      128 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/arrow-up-small-insens.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      127 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/arrow-up-small-prelight.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      132 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/arrow-up-small.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      201 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/arrow-up.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      370 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/button-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      156 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/button-empty.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      365 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/button-hover.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      210 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/button-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      347 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/button.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      321 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/checkbox-checked-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      334 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/checkbox-checked.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      227 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/checkbox-unchecked-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      216 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/checkbox-unchecked.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      197 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/combo-entry-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      285 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/combo-entry-button-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      289 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/combo-entry-button-hover.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      203 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/combo-entry-button-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      274 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/combo-entry-button.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/combo-entry-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      236 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/combo-entry.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      221 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/down-background-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      183 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/down-background-disable.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/down-background-hover.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      218 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/down-background.png
--rw-r--r--   0 fusionbot   (505) staff       (20)       71 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/empty.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/entry-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      265 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/entry-border-bg.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      258 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/entry-border-disabled.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      202 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/focus.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      157 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/frame.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      264 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/labelframe.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      307 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/minus.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      264 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/notebook.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      148 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/null.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      294 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/plus.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      140 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/progressbar-horiz.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      141 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/progressbar-vert.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      588 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/radio-checked-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      667 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/radio-checked.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      476 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/radio-unchecked-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      567 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/radio-unchecked.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      181 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-horiz-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      183 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-horiz-insens.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      185 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-horiz-prelight.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      185 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-horiz.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      386 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-insensitive.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      385 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-prelight.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      177 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-vert-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      203 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-vert-insens.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      184 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-vert-prelight.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      184 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider-vert.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      338 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/slider.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      213 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/tab-top-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      227 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/tab-top-hover.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/tab-top.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      129 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/treeview.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      177 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-horizontal-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      177 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-horizontal.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      429 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-progressbar-horiz.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      405 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-progressbar-vert.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      429 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-progressbar.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      405 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-progressbar_v.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      143 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-scrollbar-horiz.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      142 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-scrollbar-vert.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      277 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-vertical-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      176 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/trough-vertical.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/up-background-active.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      195 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/up-background-disable.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/up-background-hover.png
--rw-r--r--   0 fusionbot   (505) staff       (20)      224 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/up-background.png
--rw-r--r--   0 fusionbot   (505) staff       (20)    14336 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)      441 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/
--rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/LICENSE
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/
--rw-r--r--   0 fusionbot   (505) staff       (20)      273 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowdown-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      258 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowdown-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      292 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowleft-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      272 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowleft-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      274 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowright-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      258 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowright-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      286 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowup-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      271 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/arrowup-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1266 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      896 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      881 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      625 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      859 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-s.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1110 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/cbox-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1076 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/cbox-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1097 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/cbox-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      434 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/check-c.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      423 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/check-u.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hsb-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hsb-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      401 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hsb-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      395 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hsb-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      119 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hsb-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      592 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hslider-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      579 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hslider-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/indicator-c.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       64 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/indicator-o.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1116 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/mbut-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       61 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/mbut-arrow-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1057 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/mbut-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1095 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/mbut-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      712 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/progress-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      713 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/progress-v.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      695 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/radio-c.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      686 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/radio-u.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      409 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/spinbox-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       56 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/spindown-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      207 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/spindown-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       56 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/spinup-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/spinup-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      871 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tab-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      383 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tab-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      878 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tab-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      907 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tbar-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      238 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tbar-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      927 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tbar-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tree-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      688 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tree-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      373 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vsb-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      240 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vsb-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      405 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vsb-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      399 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vsb-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      124 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vsb-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      587 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vslider-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      581 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vslider-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)    13334 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik_alt/
--rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik_alt/hsb-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik_alt/hsb-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      373 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik_alt/vsb-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      240 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik_alt/vsb-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      314 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/pkgIndex.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)      650 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/
--rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/LICENSE
--rw-r--r--   0 fusionbot   (505) staff       (20)      219 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/
--rw-r--r--   0 fusionbot   (505) staff       (20)       49 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrow-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       49 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrow-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      218 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowdown-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      225 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowdown-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      353 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowleft-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      242 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowleft-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowright-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      242 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowright-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      219 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowup-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/arrowup-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       88 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/border.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1209 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/button-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1221 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/button-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      302 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/button-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      141 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/check-hc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      145 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/check-hu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      198 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/check-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      197 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/check-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      144 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/check-pc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      320 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      453 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      463 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-f.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-fa.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      446 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      728 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-r.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      721 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-ra.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      111 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/entry-f.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      106 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/entry-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      446 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/hprogress-b.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      124 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/hprogress-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      139 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/hsb-g.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      348 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/hsb-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       85 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/hsb-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      319 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/hslider-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       63 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/hslider-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       99 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/notebook-c.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      376 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/notebook-ta.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      378 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/notebook-tn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      156 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/notebook-ts.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      120 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/radio-hc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      154 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/radio-hu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      208 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/radio-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      151 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/radio-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      121 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/radio-pc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      201 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spinbox-f.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      160 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spinbox-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      130 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spinbut-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       60 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spinbut-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      144 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spindown-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      189 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spindown-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      202 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spindown-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      147 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spinup-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      192 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spinup-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      206 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/spinup-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      691 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/tbutton-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       58 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/tbutton-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      450 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/tbutton-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      357 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/tree-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      227 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/tree-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      427 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/vprogress-b.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      146 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/vsb-g.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      220 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/vsb-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       80 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/vsb-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      208 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/vslider-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/vslider-t.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     9617 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/
--rw-r--r--   0 fusionbot   (505) staff       (20)     2226 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/LICENSE.ORIG
--rw-r--r--   0 fusionbot   (505) staff       (20)      396 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/pkgIndex.tcl
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/
--rw-r--r--   0 fusionbot   (505) staff       (20)      357 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowdown-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      361 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowdown-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowdown-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowdown-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowleft-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      569 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowleft-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      355 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowleft-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      356 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowleft-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowright-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      364 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowright-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowright-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      355 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowright-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      355 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowup-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      363 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowup-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      356 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowup-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowup-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       63 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/blank.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1026 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      734 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      742 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      996 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1441 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-s.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1022 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-sa.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      645 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/check-dc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      337 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/check-du.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      630 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/check-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      389 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/check-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      247 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      442 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-ra.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      451 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-rd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      672 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-rf.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      452 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-rn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      679 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-rp.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      381 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/comboarrow-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      389 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/comboarrow-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      381 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/comboarrow-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      381 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/comboarrow-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      743 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/progress-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      733 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/progress-v.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      630 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/radio-dc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      364 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/radio-du.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)     1035 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/radio-nc.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      564 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/radio-nu.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      221 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-ha.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      333 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-hd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-hn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-hp.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-va.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      335 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-vd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-vn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sbthumb-vp.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      369 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scale-ha.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      365 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scale-hd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scale-hn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      367 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scale-va.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      364 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scale-vd.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      367 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scale-vn.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      209 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scaletrough-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/scaletrough-v.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sep-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sep-v.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)       78 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/sizegrip.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      454 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/tab-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      409 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/tab-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      453 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-a.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      689 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      672 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      691 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      683 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-pa.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/tree-d.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      257 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/tree-h.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      362 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/tree-n.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)      363 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/tree-p.gif
--rw-r--r--   0 fusionbot   (505) staff       (20)    12159 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance.tcl
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/trash.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/unlinked.ppm
--rw-r--r--   0 fusionbot   (505) staff       (20)     2267 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/graphics/warning.gif
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/extras/styles/
--rw-r--r--   0 fusionbot   (505) staff       (20)      342 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/styles/DIII-D.mplstyle
--rw-r--r--   0 fusionbot   (505) staff       (20)      770 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/styles/DIII-D_beamer.mplstyle
--rw-r--r--   0 fusionbot   (505) staff       (20)      769 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/styles/DIII-D_beamer_half.mplstyle
--rw-r--r--   0 fusionbot   (505) staff       (20)      770 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/styles/DIII-D_beamer_multifig.mplstyle
--rw-r--r--   0 fusionbot   (505) staff       (20)      859 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/extras/styles/DIII-D_paper_one_of_two_columns.mplstyle
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/framework_guis/
--rw-r--r--   0 fusionbot   (505) staff       (20)     3423 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/developerModeGUI.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    44586 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/efitviewer_gui.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     6805 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/efitviewer_settings.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)    18806 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/efitviewer_support_gui.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3147 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/imasActorGUI.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3703 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/imasGUI.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2121 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/latexGUI.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    10662 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/machine_mappings.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3399 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/moduleSetupGUI.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2316 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/namelistGUI.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     9067 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/preferencesGUI.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     6189 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/spruceUpFigures.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     7497 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/framework_guis/styleGUI.py
--rwxr-xr-x   0 fusionbot   (505) staff       (20)     4309 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/
--rw-r--r--   0 fusionbot   (505) staff       (20)   302749 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/OMFITx.py
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/__init__.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    76415 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/adaptors.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    42383 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/atomic_elements.json
--rw-r--r--   0 fusionbot   (505) staff       (20)     9475 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/brainfuse.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     9710 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/brainfusetf.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2368 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/exceptions_omfit.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   144663 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/fluxSurface.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    12090 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/gapy.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     9302 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/harvest_lib.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    64521 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/namelist.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     4953 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_accome.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1941 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_ascii.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     4580 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_asciitable.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2346 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_aurora.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   203427 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_base.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    10776 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_bibtex.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    24974 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_boundary.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     5916 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_bout.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    12867 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_brainfuse.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     6416 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_cdb.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    33172 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_chease.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2867 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_chombo.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    25707 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_coils.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     6311 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_cotsim.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     7018 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_csv.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   140223 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_ctrl_analysis.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    31200 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_data.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     5059 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_dir.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    11080 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_dmp.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     6926 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_efit.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    97543 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_efitviewer.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    56343 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_efund.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    14430 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_elite.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   181297 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_elm.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1594 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_environment.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     6065 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_eped.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   321077 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_eqdsk.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1759 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_error.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1273 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_fastran.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    16304 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_focus.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     4212 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_formatter.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    54185 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gacode.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1428 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gaprofiles.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   122944 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gapy.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    18828 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gato.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     8576 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_genray.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1728 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gingred.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    46693 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_github.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     4243 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gks.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2592 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gnuplot.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    57394 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_google_sheet.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    51592 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gpec.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1616 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_gptools.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    17339 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_harvest.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     8303 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_hdf5.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    47204 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_helena.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1507 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_idl.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     5034 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_idlSav.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     5022 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_ini.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    13082 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_interface.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     5481 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_ionorb.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     5154 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_jscope.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1774 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_jsolver.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     7459 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_json.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2877 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_kepler.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    29701 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_latex.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    84031 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_mars.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2352 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_matlab.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     6709 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_matrix.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    84087 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_mds.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1724 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_mmm.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3425 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_namelist.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    21157 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_nc.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    33491 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_nimrod.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    56023 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_oedge.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    19309 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_omas.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    53177 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_d3d.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    11705 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_east.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    12148 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_kstar.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   158360 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_utils.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   113555 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_onetwo.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    49393 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_osborne.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    51257 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_patch.py
--rw-r--r--   0 fusionbot   (505) staff       (20)      784 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_path.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3078 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_pdb.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    46886 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_profiles.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    84237 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_python.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    33627 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_rabbit.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    39597 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_rdb.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2366 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_reviewplus.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   114264 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_solps.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3423 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_spider.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    98563 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_testing.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    68556 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_tglf.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   118309 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_thomson.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     7856 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_timcon.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    21853 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_toksearch.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     7617 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_toq.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    71772 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_transp.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    48768 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_trip3d.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    13791 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_tsc.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2695 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_uda.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    11728 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_uedge.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    18800 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_ufile.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2146 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_weblink.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3451 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/omfit_xml.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/GUIS/
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/GUIS/__init__.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/INPUTS/
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/INPUTS/__init__.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/LIB/
--rw-r--r--   0 fusionbot   (505) staff       (20)       15 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/LIB/OMFITlib_startup.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     2627 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/OMFITsave.txt
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/OUTPUTS/
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/OUTPUTS/__init__.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/PLOTS/
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/PLOTS/__init__.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/SCRIPTS/
--rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/SCRIPTS/__init__.py
--rw-r--r--   0 fusionbot   (505) staff       (20)      478 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/SettingsNamelist.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)     1589 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/help.rst
--rw-r--r--   0 fusionbot   (505) staff       (20)    38436 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettings.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)     7145 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettingsNamelist.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)       92 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettingsNamelistOSX.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)      141 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettingsNamelistUNIX.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)       89 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettingsOSX.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)       90 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettingsUNIX.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)    57188 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/sortedDict.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     1032 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/startup_choice.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    12200 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/startup_classes.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    55211 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/startup_framework.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   734548 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/uedge_common_map.json
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes/unix_os/
--rw-r--r--   0 fusionbot   (505) staff       (20)      139 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/unix_os/__init__.py
--rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/unix_os/path.py
--rw-r--r--   0 fusionbot   (505) staff       (20)      761 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/unix_os/setup.py
--rw-r--r--   0 fusionbot   (505) staff       (20)        3 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/unix_os/version
--rw-r--r--   0 fusionbot   (505) staff       (20)   157547 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/utils_base.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   128692 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/utils_fit.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   148484 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/utils_fusion.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   235426 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/utils_math.py
--rw-r--r--   0 fusionbot   (505) staff       (20)   166642 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/utils_plot.py
--rw-r--r--   0 fusionbot   (505) staff       (20)       10 2023-01-29 21:36:14.000000 omfit_classes-3.2023.5.2/omfit_classes/version
--rw-r--r--   0 fusionbot   (505) staff       (20)     3549 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_classes/zdata.py
-drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/omfit_classes.egg-info/
--rw-r--r--   0 fusionbot   (505) staff       (20)     1178 2023-01-29 21:36:25.000000 omfit_classes-3.2023.5.2/omfit_classes.egg-info/PKG-INFO
--rw-r--r--   0 fusionbot   (505) staff       (20)    32110 2023-01-29 21:36:26.000000 omfit_classes-3.2023.5.2/omfit_classes.egg-info/SOURCES.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)        1 2023-01-29 21:36:25.000000 omfit_classes-3.2023.5.2/omfit_classes.egg-info/dependency_links.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)       14 2023-01-29 21:36:25.000000 omfit_classes-3.2023.5.2/omfit_classes.egg-info/top_level.txt
--rw-r--r--   0 fusionbot   (505) staff       (20)   370340 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_gui.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     3236 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_halt.py
--rw-r--r--   0 fusionbot   (505) staff       (20)     4957 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_parse_args.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    82099 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_plot.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    12707 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_setup.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    83386 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/omfit_tree.py
--rw-r--r--   0 fusionbot   (505) staff       (20)       38 2023-01-29 21:36:27.000000 omfit_classes-3.2023.5.2/setup.cfg
--rw-r--r--   0 fusionbot   (505) staff       (20)     1314 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/setup.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    26589 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/utils.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    62680 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/utils_tk.py
--rw-r--r--   0 fusionbot   (505) staff       (20)    32773 2023-01-28 03:10:15.000000 omfit_classes-3.2023.5.2/utils_widgets.py
--rw-r--r--   0 fusionbot   (505) staff       (20)       10 2023-01-29 21:36:14.000000 omfit_classes-3.2023.5.2/version
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1067 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/LICENSE.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1178 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/PKG-INFO
+-rw-r--r--   0 fusionbot   (505) staff       (20)      942 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/README.rst
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/__init__.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/classes/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      290 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/classes/__init__.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    27149 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/externalImports.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/__init__.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/
+-rw-r--r--   0 fusionbot   (505) staff       (20)   385815 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/LOM.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6335 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_font.bf
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3044 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_font.ttf
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2087 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)    56012 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo.pdf
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3187 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_color.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)    59634 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_color.pdf
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6504 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_olympics.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)   179267 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_olympics.pdf
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/__init__.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/autoX.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/autoY.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/bookmark.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     8760 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/colors.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/copy.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/crosshair.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1512 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/error.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      277 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/events.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/
+-rw-r--r--   0 fusionbot   (505) staff       (20)    25832 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Humor-Sans.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    52836 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Bold.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    53512 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-BoldItalic.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    48220 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-ExtraLight.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    49204 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-ExtraLightItalic.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    49760 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Italic.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    48856 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Light.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    49552 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-LightItalic.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    49488 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Semi-BoldItalic.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    49272 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-SemiBold.ttf
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)    49008 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli.ttf
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2334 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/fonts.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/help.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2507 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/info.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/legend.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/linked.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/mail.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)      631 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/matplotlib_backends.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/paste.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/pdf.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     5370 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/pin.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2472 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/question.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/select.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/settings.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/storage.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/text.ppm
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      600 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/CreateImageLib.def
+-rw-r--r--   0 fusionbot   (505) staff       (20)    41722 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/ImageLib.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/LICENSE
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6971 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/aquativo.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)   112011 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/images.tgz
+-rw-r--r--   0 fusionbot   (505) staff       (20)       95 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/black/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2123 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/black/LICENSE
+-rw-r--r--   0 fusionbot   (505) staff       (20)     4066 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/black/black.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)      209 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/black/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/LICENSE
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      315 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowdown-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      312 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowdown-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      313 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowdown.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      329 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowleft-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      327 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowleft-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      323 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowleft.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowright-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      327 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowright-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      324 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowright.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      309 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowup-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      313 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowup-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      314 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/arrowup.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      696 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/button-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      770 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/button-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      769 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/button-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      254 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/check-hc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/check-hu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      249 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/check-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      229 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/check-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1098 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/radio-hc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      626 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/radio-hu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      389 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/radio-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      401 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/radio-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      343 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/sb-thumb-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      316 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/sb-thumb.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      333 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/sb-vthumb-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      308 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/sb-vthumb.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      182 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/slider-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      182 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/slider.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      183 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/vslider-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      283 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/vslider.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     4714 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)      188 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/blue/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2226 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/LICENSE
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      245 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      230 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      246 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      248 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowdown-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      248 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      252 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      251 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowleft-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      250 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      235 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      252 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      251 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowright-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      244 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      228 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      248 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      247 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/arrowup-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       63 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/blank.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      661 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      590 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      656 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      519 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      394 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-pa.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      331 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-ac.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-au.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-dc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-du.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      331 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      332 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-pc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       96 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/check-pu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      100 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      527 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-ra.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      512 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-rd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      550 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-rf.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      533 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-rn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      402 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-rp.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      441 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      432 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      451 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      450 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/comboarrow-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      281 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/progress-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      304 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/progress-v.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      356 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-ac.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-au.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      362 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-dc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-du.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      359 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      359 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-pc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      225 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/radio-pu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      276 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-ha.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      263 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-hd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      278 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-hn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      278 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-hp.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      266 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-va.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      262 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-vd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      271 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-vn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      271 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sbthumb-vp.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      474 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scale-ha.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      336 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scale-hd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      477 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scale-hn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      526 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scale-va.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      342 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scale-vd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      511 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scale-vn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       87 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scaletrough-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      111 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scaletrough-v.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sep-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sep-v.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       77 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/sizegrip.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      536 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tab-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      549 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tab-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      554 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      499 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      557 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      527 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      333 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-pa.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      509 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tree-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      519 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tree-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      528 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tree-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      420 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tree-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)    11637 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)      406 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2226 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/LICENSE
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/
+-rw-r--r--   0 fusionbot   (505) staff       (20)       70 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/arrow-optionmenu-disabled.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       79 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/arrow-optionmenu-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       79 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/arrow-optionmenu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1954 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-active-disabled.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1953 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-active-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      872 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-active.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1267 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-default.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2001 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      138 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/check1.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      145 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/check2.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/combo-active.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/entry-active.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/entry-inactive.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/grip-horiz-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/grip-horiz.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       59 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/grip-vert-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       59 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/grip-vert.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      700 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/list-header-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      706 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/list-header.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/option1.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      363 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/option2.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      995 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/progressbar-horiz.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      966 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/progressbar-vert.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/scale-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      320 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/scale.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      651 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-horiz-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      673 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-horiz.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      666 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-vert-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      722 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-vert.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      542 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-down-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      555 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-down.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      555 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-left-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      556 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-left.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      555 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-right-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      560 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-right.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      542 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-up-prelight.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      549 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-up.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      544 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/tab-top-active.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      583 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/tab-top.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       97 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-horiz.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      664 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-progressbar-horiz.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      677 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-progressbar-vert.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      803 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-horiz.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      871 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-vert.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      133 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-vert.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     9054 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)      154 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      203 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/arrow-down-insens.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      200 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/arrow-down-prelight.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      202 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/arrow-down.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      128 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/arrow-up-small-insens.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      127 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/arrow-up-small-prelight.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      132 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/arrow-up-small.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      201 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/arrow-up.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      370 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/button-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      156 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/button-empty.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      365 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/button-hover.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      210 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/button-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      347 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/button.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      321 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/checkbox-checked-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      334 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/checkbox-checked.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      227 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/checkbox-unchecked-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      216 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/checkbox-unchecked.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      197 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/combo-entry-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      285 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/combo-entry-button-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      289 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/combo-entry-button-hover.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      203 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/combo-entry-button-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      274 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/combo-entry-button.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/combo-entry-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      236 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/combo-entry.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      221 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/down-background-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      183 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/down-background-disable.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/down-background-hover.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      218 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/down-background.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)       71 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/empty.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      223 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/entry-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      265 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/entry-border-bg.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      258 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/entry-border-disabled.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      202 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/focus.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      157 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/frame.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      264 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/labelframe.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      307 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/minus.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      264 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/notebook.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      148 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/null.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      294 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/plus.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      140 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/progressbar-horiz.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      141 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/progressbar-vert.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      588 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/radio-checked-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      667 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/radio-checked.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      476 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/radio-unchecked-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      567 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/radio-unchecked.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      181 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-horiz-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      183 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-horiz-insens.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      185 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-horiz-prelight.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      185 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-horiz.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      386 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-insensitive.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      385 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-prelight.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      177 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-vert-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      203 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-vert-insens.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      184 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-vert-prelight.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      184 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider-vert.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      338 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/slider.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      213 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/tab-top-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      227 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/tab-top-hover.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/tab-top.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      129 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/treeview.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      177 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-horizontal-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      177 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-horizontal.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      429 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-progressbar-horiz.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      405 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-progressbar-vert.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      429 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-progressbar.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      405 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-progressbar_v.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      143 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-scrollbar-horiz.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      142 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-scrollbar-vert.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      277 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-vertical-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      176 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/trough-vertical.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      234 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/up-background-active.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      195 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/up-background-disable.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/up-background-hover.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)      224 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/up-background.png
+-rw-r--r--   0 fusionbot   (505) staff       (20)    14336 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)      441 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/LICENSE
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      273 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowdown-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      258 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowdown-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      292 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowleft-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      272 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowleft-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      274 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowright-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      258 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowright-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      286 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowup-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      271 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/arrowup-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1266 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      896 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      881 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      625 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      859 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-s.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1110 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/cbox-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1076 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/cbox-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1097 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/cbox-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      434 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/check-c.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      423 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/check-u.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hsb-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hsb-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      401 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hsb-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      395 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hsb-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      119 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hsb-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      592 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hslider-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      579 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hslider-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/indicator-c.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       64 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/indicator-o.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1116 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/mbut-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       61 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/mbut-arrow-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1057 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/mbut-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1095 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/mbut-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      712 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/progress-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      713 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/progress-v.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      695 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/radio-c.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      686 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/radio-u.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      409 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/spinbox-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       56 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/spindown-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      207 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/spindown-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       56 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/spinup-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      190 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/spinup-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      871 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tab-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      383 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tab-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      878 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tab-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      907 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tbar-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      238 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tbar-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      927 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tbar-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tree-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      688 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tree-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      373 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vsb-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      240 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vsb-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      405 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vsb-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      399 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vsb-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      124 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vsb-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      587 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vslider-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      581 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vslider-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)    13334 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik_alt/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik_alt/hsb-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik_alt/hsb-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      373 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik_alt/vsb-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      240 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik_alt/vsb-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      314 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/pkgIndex.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)      650 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2147 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/LICENSE
+-rw-r--r--   0 fusionbot   (505) staff       (20)      219 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/
+-rw-r--r--   0 fusionbot   (505) staff       (20)       49 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrow-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       49 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrow-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      218 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowdown-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      225 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowdown-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      353 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowleft-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      242 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowleft-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowright-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      242 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowright-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      219 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowup-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/arrowup-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       88 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/border.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1209 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/button-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1221 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/button-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      302 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/button-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      141 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/check-hc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      145 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/check-hu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      198 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/check-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      197 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/check-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      144 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/check-pc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      320 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      453 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      463 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-f.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-fa.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      446 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      728 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-r.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      721 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-ra.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      111 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/entry-f.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      106 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/entry-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      446 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/hprogress-b.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      124 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/hprogress-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      139 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/hsb-g.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      348 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/hsb-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       85 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/hsb-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      319 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/hslider-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       63 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/hslider-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       99 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/notebook-c.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      376 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/notebook-ta.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      378 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/notebook-tn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      156 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/notebook-ts.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      120 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/radio-hc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      154 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/radio-hu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      208 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/radio-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      151 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/radio-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      121 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/radio-pc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      201 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spinbox-f.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      160 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spinbox-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      130 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spinbut-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       60 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spinbut-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      144 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spindown-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      189 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spindown-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      202 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spindown-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      147 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spinup-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      192 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spinup-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      206 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/spinup-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      691 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/tbutton-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       58 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/tbutton-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      450 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/tbutton-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      357 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/tree-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      227 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/tree-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      427 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/vprogress-b.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      146 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/vsb-g.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      220 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/vsb-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       80 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/vsb-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      208 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/vslider-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       67 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/vslider-t.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     9617 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2226 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/LICENSE.ORIG
+-rw-r--r--   0 fusionbot   (505) staff       (20)      396 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/pkgIndex.tcl
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      357 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowdown-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      361 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowdown-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowdown-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowdown-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowleft-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      569 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowleft-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      355 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowleft-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      356 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowleft-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowright-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      364 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowright-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      354 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowright-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      355 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowright-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      355 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowup-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      363 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowup-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      356 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowup-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      358 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowup-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       63 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/blank.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1026 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      734 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      742 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      996 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1441 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-s.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1022 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-sa.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      645 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/check-dc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      337 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/check-du.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      630 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/check-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      389 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/check-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      247 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      442 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-ra.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      451 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-rd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      672 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-rf.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      452 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-rn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      679 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-rp.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      381 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/comboarrow-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      389 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/comboarrow-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      381 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/comboarrow-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      381 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/comboarrow-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      743 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/progress-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      733 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/progress-v.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      630 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/radio-dc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      364 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/radio-du.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1035 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/radio-nc.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      564 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/radio-nu.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      221 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-ha.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      333 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-hd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-hn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-hp.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      226 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-va.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      335 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-vd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-vn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      330 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sbthumb-vp.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      369 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scale-ha.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      365 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scale-hd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scale-hn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      367 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scale-va.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      364 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scale-vd.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      367 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scale-vn.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      209 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scaletrough-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      233 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/scaletrough-v.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sep-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       40 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sep-v.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)       78 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/sizegrip.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      454 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/tab-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      409 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/tab-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      453 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-a.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      689 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      672 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      691 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      683 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-pa.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      366 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/tree-d.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      257 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/tree-h.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      362 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/tree-n.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)      363 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/tree-p.gif
+-rw-r--r--   0 fusionbot   (505) staff       (20)    12159 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance.tcl
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/trash.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1741 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/unlinked.ppm
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2267 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/graphics/warning.gif
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/extras/styles/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      342 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/styles/DIII-D.mplstyle
+-rw-r--r--   0 fusionbot   (505) staff       (20)      770 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/styles/DIII-D_beamer.mplstyle
+-rw-r--r--   0 fusionbot   (505) staff       (20)      769 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/styles/DIII-D_beamer_half.mplstyle
+-rw-r--r--   0 fusionbot   (505) staff       (20)      770 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/styles/DIII-D_beamer_multifig.mplstyle
+-rw-r--r--   0 fusionbot   (505) staff       (20)      859 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/extras/styles/DIII-D_paper_one_of_two_columns.mplstyle
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/framework_guis/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3423 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/developerModeGUI.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    44586 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/efitviewer_gui.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6805 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/efitviewer_settings.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)    18806 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/efitviewer_support_gui.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3147 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/imasActorGUI.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3703 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/imasGUI.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2121 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/latexGUI.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    10662 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/machine_mappings.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3399 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/moduleSetupGUI.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2316 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/namelistGUI.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     9067 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/preferencesGUI.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6189 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/spruceUpFigures.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     7497 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/framework_guis/styleGUI.py
+-rwxr-xr-x   0 fusionbot   (505) staff       (20)     4309 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/
+-rw-r--r--   0 fusionbot   (505) staff       (20)   302749 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/OMFITx.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/__init__.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    76415 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/adaptors.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    42383 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/atomic_elements.json
+-rw-r--r--   0 fusionbot   (505) staff       (20)     9475 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/brainfuse.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     9710 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/brainfusetf.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2368 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/exceptions_omfit.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   144663 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/fluxSurface.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    12090 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/gapy.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     9302 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/harvest_lib.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    64521 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/namelist.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     4953 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_accome.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1941 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_ascii.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     4580 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_asciitable.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2346 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_aurora.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   203427 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_base.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    10776 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_bibtex.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    24974 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_boundary.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     5916 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_bout.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    12867 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_brainfuse.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6416 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_cdb.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    33172 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_chease.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2867 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_chombo.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    25707 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_coils.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6311 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_cotsim.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     7018 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_csv.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   140223 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_ctrl_analysis.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    31200 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_data.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     5059 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_dir.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    11080 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_dmp.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6926 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_efit.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    97543 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_efitviewer.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    56343 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_efund.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    14430 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_elite.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   181065 2023-02-12 13:41:13.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_elm.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1594 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_environment.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6065 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_eped.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   321077 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_eqdsk.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1759 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_error.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1273 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_fastran.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    16304 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_focus.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     4212 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_formatter.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    54185 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gacode.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1428 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gaprofiles.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   122944 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gapy.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    18828 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gato.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     8576 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_genray.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1728 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gingred.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    46693 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_github.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     4243 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gks.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2592 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gnuplot.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    57394 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_google_sheet.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    51592 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gpec.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1616 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_gptools.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    17339 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_harvest.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     8303 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_hdf5.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    47204 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_helena.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1507 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_idl.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     5034 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_idlSav.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     5022 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_ini.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    13082 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_interface.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     5481 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_ionorb.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     5154 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_jscope.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1774 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_jsolver.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     7459 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_json.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2877 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_kepler.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    29701 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_latex.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    84031 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_mars.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2352 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_matlab.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     6709 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_matrix.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    84087 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_mds.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1724 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_mmm.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3425 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_namelist.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    21157 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_nc.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    33491 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_nimrod.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    56023 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_oedge.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    19309 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_omas.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    53177 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_d3d.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    11705 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_east.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    12148 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_kstar.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   158360 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_utils.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   113555 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_onetwo.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    49393 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_osborne.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    51257 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_patch.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)      784 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_path.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3078 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_pdb.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    46886 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_profiles.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    84237 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_python.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    33627 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_rabbit.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    39597 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_rdb.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2366 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_reviewplus.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   114264 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_solps.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3423 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_spider.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    98563 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_testing.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    68556 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_tglf.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   115517 2023-02-12 13:41:13.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_thomson.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     7856 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_timcon.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    21853 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_toksearch.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     7617 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_toq.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    71772 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_transp.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    48768 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_trip3d.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    13791 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_tsc.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2695 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_uda.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    11728 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_uedge.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    18800 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_ufile.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2146 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_weblink.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3451 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/omfit_xml.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/GUIS/
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/GUIS/__init__.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/INPUTS/
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/INPUTS/__init__.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/LIB/
+-rw-r--r--   0 fusionbot   (505) staff       (20)       15 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/LIB/OMFITlib_startup.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     2627 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/OMFITsave.txt
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/OUTPUTS/
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/OUTPUTS/__init__.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/PLOTS/
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/PLOTS/__init__.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/SCRIPTS/
+-rw-r--r--   0 fusionbot   (505) staff       (20)        0 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/SCRIPTS/__init__.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)      478 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/SettingsNamelist.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1589 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/help.rst
+-rw-r--r--   0 fusionbot   (505) staff       (20)    38436 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettings.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)     7145 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettingsNamelist.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)       92 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettingsNamelistOSX.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)      141 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettingsNamelistUNIX.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)       89 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettingsOSX.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)       90 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettingsUNIX.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)    57188 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/sortedDict.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1032 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/startup_choice.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    12200 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/startup_classes.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    55211 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/startup_framework.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   734548 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/uedge_common_map.json
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes/unix_os/
+-rw-r--r--   0 fusionbot   (505) staff       (20)      139 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/unix_os/__init__.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)      325 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/unix_os/path.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)      761 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/unix_os/setup.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)        3 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/unix_os/version
+-rw-r--r--   0 fusionbot   (505) staff       (20)   157547 2023-02-12 13:41:13.000000 omfit_classes-3.2023.7.2/omfit_classes/utils_base.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   128692 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/utils_fit.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   148484 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/utils_fusion.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   235426 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/utils_math.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)   166642 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/utils_plot.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)       10 2023-02-12 13:41:13.000000 omfit_classes-3.2023.7.2/omfit_classes/version
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3549 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_classes/zdata.py
+drwxr-xr-x   0 fusionbot   (505) staff       (20)        0 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes.egg-info/
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1178 2023-02-12 13:41:23.000000 omfit_classes-3.2023.7.2/omfit_classes.egg-info/PKG-INFO
+-rw-r--r--   0 fusionbot   (505) staff       (20)    32110 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/omfit_classes.egg-info/SOURCES.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)        1 2023-02-12 13:41:23.000000 omfit_classes-3.2023.7.2/omfit_classes.egg-info/dependency_links.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)       14 2023-02-12 13:41:23.000000 omfit_classes-3.2023.7.2/omfit_classes.egg-info/top_level.txt
+-rw-r--r--   0 fusionbot   (505) staff       (20)   370340 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_gui.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     3236 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_halt.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)     4949 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_parse_args.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    82099 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_plot.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    12707 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_setup.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    83386 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/omfit_tree.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)       38 2023-02-12 13:41:25.000000 omfit_classes-3.2023.7.2/setup.cfg
+-rw-r--r--   0 fusionbot   (505) staff       (20)     1314 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/setup.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    26589 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/utils.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    62680 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/utils_tk.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)    32773 2023-02-12 06:10:27.000000 omfit_classes-3.2023.7.2/utils_widgets.py
+-rw-r--r--   0 fusionbot   (505) staff       (20)       10 2023-02-12 13:41:13.000000 omfit_classes-3.2023.7.2/version
```

### Comparing `omfit_classes-3.2023.5.2/LICENSE.txt` & `omfit_classes-3.2023.7.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/PKG-INFO` & `omfit_classes-3.2023.7.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: omfit_classes
-Version: 3.2023.5.2
+Version: 3.2023.7.2
 Summary: Classes of OMFIT (One Modeling Framework For Integrated Tasks)
 Home-page: https://omfit.io
 Author: OMFIT developers
 Author-email: meneghini@fusion.gat.com
 License: MIT
 Keywords: integrated modeling plasma framework
 Platform: UNKNOWN
```

### Comparing `omfit_classes-3.2023.5.2/README.rst` & `omfit_classes-3.2023.7.2/README.rst`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/externalImports.py` & `omfit_classes-3.2023.7.2/externalImports.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/LOM.png` & `omfit_classes-3.2023.7.2/extras/graphics/LOM.png`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_font.bf` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_font.bf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_font.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_font.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo.gif` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo.pdf` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo.pdf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_color.gif` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_color.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_color.pdf` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_color.pdf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_olympics.gif` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_olympics.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/OMFIT_logo_olympics.pdf` & `omfit_classes-3.2023.7.2/extras/graphics/OMFIT_logo_olympics.pdf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/bookmark.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/bookmark.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/colors.py` & `omfit_classes-3.2023.7.2/extras/graphics/colors.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/copy.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/copy.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/crosshair.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/crosshair.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/error.gif` & `omfit_classes-3.2023.7.2/extras/graphics/error.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Humor-Sans.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Humor-Sans.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Bold.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Bold.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-BoldItalic.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-BoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-ExtraLight.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-ExtraLight.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-ExtraLightItalic.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-ExtraLightItalic.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Italic.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Italic.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Light.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Light.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-LightItalic.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-LightItalic.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-Semi-BoldItalic.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-Semi-BoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli-SemiBold.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli-SemiBold.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts/Muli.ttf` & `omfit_classes-3.2023.7.2/extras/graphics/fonts/Muli.ttf`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/fonts.py` & `omfit_classes-3.2023.7.2/extras/graphics/fonts.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/help.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/help.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/info.gif` & `omfit_classes-3.2023.7.2/extras/graphics/info.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/legend.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/legend.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/linked.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/linked.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/mail.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/mail.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/matplotlib_backends.py` & `omfit_classes-3.2023.7.2/extras/graphics/matplotlib_backends.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/paste.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/paste.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/pdf.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/pdf.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/pin.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/pin.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/question.gif` & `omfit_classes-3.2023.7.2/extras/graphics/question.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/select.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/select.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/settings.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/settings.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/storage.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/storage.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/text.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/text.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/CreateImageLib.def` & `omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/CreateImageLib.def`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/ImageLib.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/ImageLib.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/LICENSE` & `omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/LICENSE`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/aquativo.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/aquativo.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/aquativo/images.tgz` & `omfit_classes-3.2023.7.2/extras/graphics/themes/aquativo/images.tgz`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/black/LICENSE` & `omfit_classes-3.2023.7.2/extras/graphics/themes/black/LICENSE`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/black/black.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/black/black.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/blue/LICENSE` & `omfit_classes-3.2023.7.2/extras/graphics/themes/blue/LICENSE`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/button-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/button-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/button-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/button-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/button-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/button-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/radio-hc.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/radio-hc.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue/radio-hu.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue/radio-hu.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/blue/blue.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/blue/blue.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/LICENSE` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/LICENSE`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-a.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-a.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-d.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-d.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/button-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/button-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-ra.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-ra.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-rd.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-rd.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-rf.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-rf.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/combo-rn.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/combo-rn.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/scale-va.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/scale-va.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tab-a.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tab-a.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tab-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tab-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-a.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-a.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/toolbutton-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tree-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tree-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks/tree-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks/tree-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/clearlooks/clearlooks.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/clearlooks/clearlooks.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/LICENSE` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/LICENSE`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-active-disabled.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-active-disabled.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-active-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-active-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-active.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-active.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-default.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-default.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/button-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/button-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/list-header-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/list-header-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/list-header.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/list-header.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/progressbar-horiz.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/progressbar-horiz.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/progressbar-vert.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/progressbar-vert.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-horiz-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-horiz-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-horiz.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-horiz.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-vert-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-vert-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/slider-vert.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/slider-vert.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-down-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-down-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-down.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-down.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-left-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-left-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-left.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-left.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-right-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-right-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-right.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-right.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-up-prelight.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-up-prelight.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/stepper-up.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/stepper-up.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/tab-top-active.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/tab-top-active.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/tab-top.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/tab-top.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-progressbar-horiz.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-progressbar-horiz.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-progressbar-vert.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-progressbar-vert.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-horiz.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-horiz.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-vert.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance/trough-scrollbar-vert.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/elegance/elegance.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/elegance/elegance.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/radio-checked-insensitive.png` & `omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/radio-checked-insensitive.png`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/radio-checked.png` & `omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/radio-checked.png`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux/radio-unchecked.png` & `omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux/radio-unchecked.png`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/equilux/equilux.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/equilux/equilux.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/LICENSE` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/LICENSE`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-d.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-d.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/button-s.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/button-s.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/cbox-a.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/cbox-a.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/cbox-d.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/cbox-d.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/cbox-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/cbox-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hslider-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hslider-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/hslider-t.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/hslider-t.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/mbut-a.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/mbut-a.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/mbut-d.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/mbut-d.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/mbut-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/mbut-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/progress-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/progress-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/progress-v.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/progress-v.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/radio-c.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/radio-c.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/radio-u.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/radio-u.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tab-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tab-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tab-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tab-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tbar-a.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tbar-a.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tbar-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tbar-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/tree-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/tree-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vslider-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vslider-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik/vslider-t.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik/vslider-t.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/keramik/keramik.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/keramik/keramik.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/pkgIndex.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/pkgIndex.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/LICENSE` & `omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/LICENSE`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/button-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/button-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/button-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/button-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-r.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-r.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/combo-ra.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/combo-ra.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik/tbutton-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik/tbutton-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/plastik/plastik.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/plastik/plastik.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/LICENSE.ORIG` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/LICENSE.ORIG`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/arrowleft-d.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/arrowleft-d.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-a.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-a.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-d.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-d.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-s.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-s.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/button-sa.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/button-sa.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/check-dc.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/check-dc.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/check-nc.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/check-nc.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-rf.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-rf.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/combo-rp.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/combo-rp.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/progress-h.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/progress-h.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/progress-v.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/progress-v.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/radio-dc.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/radio-dc.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/radio-nc.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/radio-nc.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/radio-nu.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/radio-nu.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-d.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-d.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-n.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-n.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-p.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-p.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance/toolbutton-pa.gif` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance/toolbutton-pa.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/themes/radiance/radiance.tcl` & `omfit_classes-3.2023.7.2/extras/graphics/themes/radiance/radiance.tcl`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/trash.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/trash.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/unlinked.ppm` & `omfit_classes-3.2023.7.2/extras/graphics/unlinked.ppm`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/graphics/warning.gif` & `omfit_classes-3.2023.7.2/extras/graphics/warning.gif`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/styles/DIII-D_beamer.mplstyle` & `omfit_classes-3.2023.7.2/extras/styles/DIII-D_beamer.mplstyle`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/styles/DIII-D_beamer_half.mplstyle` & `omfit_classes-3.2023.7.2/extras/styles/DIII-D_beamer_half.mplstyle`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/styles/DIII-D_beamer_multifig.mplstyle` & `omfit_classes-3.2023.7.2/extras/styles/DIII-D_beamer_multifig.mplstyle`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/extras/styles/DIII-D_paper_one_of_two_columns.mplstyle` & `omfit_classes-3.2023.7.2/extras/styles/DIII-D_paper_one_of_two_columns.mplstyle`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/developerModeGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/developerModeGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/efitviewer_gui.py` & `omfit_classes-3.2023.7.2/framework_guis/efitviewer_gui.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/efitviewer_settings.txt` & `omfit_classes-3.2023.7.2/framework_guis/efitviewer_settings.txt`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/efitviewer_support_gui.py` & `omfit_classes-3.2023.7.2/framework_guis/efitviewer_support_gui.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/imasActorGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/imasActorGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/imasGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/imasGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/latexGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/latexGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/machine_mappings.py` & `omfit_classes-3.2023.7.2/framework_guis/machine_mappings.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/moduleSetupGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/moduleSetupGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/namelistGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/namelistGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/preferencesGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/preferencesGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/spruceUpFigures.py` & `omfit_classes-3.2023.7.2/framework_guis/spruceUpFigures.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/framework_guis/styleGUI.py` & `omfit_classes-3.2023.7.2/framework_guis/styleGUI.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit.py` & `omfit_classes-3.2023.7.2/omfit.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/OMFITx.py` & `omfit_classes-3.2023.7.2/omfit_classes/OMFITx.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/adaptors.py` & `omfit_classes-3.2023.7.2/omfit_classes/adaptors.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/atomic_elements.json` & `omfit_classes-3.2023.7.2/omfit_classes/atomic_elements.json`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/brainfuse.py` & `omfit_classes-3.2023.7.2/omfit_classes/brainfuse.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/brainfusetf.py` & `omfit_classes-3.2023.7.2/omfit_classes/brainfusetf.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/exceptions_omfit.py` & `omfit_classes-3.2023.7.2/omfit_classes/exceptions_omfit.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/fluxSurface.py` & `omfit_classes-3.2023.7.2/omfit_classes/fluxSurface.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/gapy.py` & `omfit_classes-3.2023.7.2/omfit_classes/gapy.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/harvest_lib.py` & `omfit_classes-3.2023.7.2/omfit_classes/harvest_lib.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/namelist.py` & `omfit_classes-3.2023.7.2/omfit_classes/namelist.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_accome.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_accome.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_ascii.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_ascii.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_asciitable.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_asciitable.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_aurora.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_aurora.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_base.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_base.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_bibtex.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_bibtex.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_boundary.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_boundary.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_bout.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_bout.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_brainfuse.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_brainfuse.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_cdb.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_cdb.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_chease.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_chease.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_chombo.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_chombo.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_coils.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_coils.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_cotsim.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_cotsim.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_csv.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_csv.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_ctrl_analysis.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_ctrl_analysis.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_data.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_data.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_dir.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_dir.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_dmp.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_dmp.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_efit.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_efit.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_efitviewer.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_efitviewer.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_efund.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_efund.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_elite.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_elite.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_elm.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_elm.py`

 * *Files 0% similar despite different names*

```diff
@@ -53,15 +53,15 @@
 
 try:
     # This should work if launched from the command line in the right path
     from omfit.omfit_plot import cornernote
     from omfit.utils_plot import contrasting_color
     from omfit.utils_math import array_info
 
-except ImportError:
+except (ImportError, OSError):
     pass
 
 __all__ = []
 
 
 try:
     scratch = OMFIT['scratch'].setdefault('OMFITelm', SortedDict())
@@ -441,19 +441,15 @@
                         'PASSIVESPEC.FILTERED_VIS.BAYE_BOTTOM.DALF_FSCOPE',
                         'PASSIVESPEC.FILTERED_VIS.BAYE_BOTTOM.DALF_EIES',
                     ]
                 },
             },
             'KSTAR': {
                 'mds_tree': 'KSTAR',
-                'filterscope_data': {
-                    'names': [
-                        r'\pol_ha02',
-                    ]
-                },
+                'filterscope_data': {'names': [r'\pol_ha02']},
                 'ip_ptname': r'\rc02',
                 'rvsout_ptname': r'\KSTAR::TOP.EFIT.EFIT01.RESULTS.AEQDSK.RVSOUT',
                 'zvsout_ptname': r'\KSTAR::TOP.EFIT.EFIT01.RESULTS.AEQDSK.ZVSOUT',
                 'rvsin_ptname': r'\KSTAR::TOP.EFIT.EFIT01.RESULTS.AEQDSK.RVSIN',
             },
         }
 
@@ -564,25 +560,16 @@
                     'elm_since_reject_below': 0.1,
                     'elm_since_accept_above': 25.0,
                     'CER_entire_window_must_pass_ELM_filter': False,
                 },
                 'misc': {'elm_freq_method': 3},
             },
             'DIII-D': {},
-            'EAST': {
-                'detection': {
-                    'time_factor': 1e3,
-                }
-            },
-            'KSTAR': {
-                'detection': {
-                    'time_factor': 1e3,
-                    'find_jump_threshold': 0.05,
-                }
-            },
+            'EAST': {'detection': {'time_factor': 1e3}},
+            'KSTAR': {'detection': {'time_factor': 1e3, 'find_jump_threshold': 0.05}},
             'NSTX': {
                 'detection': {
                     'time_factor': 1e3,
                     'jump_hold_max_dt': 0.21,  # ms  # TODO: check this setting
                     'gauss_smooth_tuning': {
                         'mild_smooth': 1.5,
                         'threshold_on_difference_of_smooths': 0.16,
```

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_environment.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_environment.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_eped.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_eped.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_eqdsk.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_eqdsk.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_error.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_error.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_fastran.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_fastran.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_focus.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_focus.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_formatter.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_formatter.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gacode.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gacode.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gaprofiles.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gaprofiles.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gapy.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gapy.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gato.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gato.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_genray.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_genray.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gingred.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gingred.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_github.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_github.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gks.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gks.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gnuplot.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gnuplot.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_google_sheet.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_google_sheet.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gpec.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gpec.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_gptools.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_gptools.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_harvest.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_harvest.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_hdf5.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_hdf5.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_helena.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_helena.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_idl.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_idl.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_idlSav.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_idlSav.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_ini.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_ini.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_interface.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_interface.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_ionorb.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_ionorb.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_jscope.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_jscope.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_jsolver.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_jsolver.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_json.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_json.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_kepler.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_kepler.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_latex.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_latex.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_mars.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_mars.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_matlab.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_matlab.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_matrix.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_matrix.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_mds.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_mds.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_mmm.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_mmm.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_namelist.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_namelist.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_nc.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_nc.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_nimrod.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_nimrod.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_oedge.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_oedge.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_omas.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_omas.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_d3d.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_d3d.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_east.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_east.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_kstar.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_kstar.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_omas_utils.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_omas_utils.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_onetwo.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_onetwo.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_osborne.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_osborne.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_patch.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_patch.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_path.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_path.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_pdb.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_pdb.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_profiles.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_profiles.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_python.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_python.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_rabbit.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_rabbit.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_rdb.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_rdb.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_reviewplus.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_reviewplus.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_solps.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_solps.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_spider.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_spider.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_testing.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_testing.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_tglf.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_tglf.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_thomson.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_thomson.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 try:
     # framework is running
     from .startup_choice import *
-except ImportError as _excp:
+except (ImportError, OSError) as _excp:
     # class is imported by itself
     if (
         'attempted relative import with no known parent package' in str(_excp)
         or 'No module named \'omfit_classes\'' in str(_excp)
         or "No module named '__main__.startup_choice'" in str(_excp)
     ):
         from startup_choice import *
     else:
         raise
 
 from omfit_classes.omfit_error import OMFITerror
-from omfit_classes.omfit_elm import OMFITelm
 from omfit_classes.utils_base import printd, tolist
 from omfit_classes.utils_fusion import is_device, tokamak, lambda_debye
 from omfit_classes.utils_math import closestIndex
 from omfit_classes.omfit_mds import OMFITmdsValue
 from omfit_classes.omfit_rdb import OMFITrdb
 from omfit_classes.omfit_eqdsk import read_basic_eq_from_mds
 
@@ -238,59 +237,51 @@
                 'frac_temp_err_cold_max': 0.95,
                 'hot_cold_boundary': 15.0,
                 'frac_dens_err_max': 0.5,
             },
         }
         self.quality_filters = self.default_quality_filters
         if quality_filters == 'default':
-            self.printdq(
-                '  Using default quality filters',
-            )
+            self.printdq('  Using default quality filters')
         elif isinstance(quality_filters, dict):
-            self.printdq(
-                '  Got dictionary of quality filters',
-            )
+            self.printdq('  Got dictionary of quality filters')
             sub_keys = ['core', 'tangential', 'divertor', 'global_override']
             non_sub_keys = [k for k in list(self.default_quality_filters.keys()) if k not in sub_keys]
             for k in non_sub_keys:
                 qf = quality_filters.get(k, None)
                 if qf is None:
-                    self.printdq(
-                        '  {} not found in quality filter spec. Using default value for {}'.format(k, k),
-                    )
+                    self.printdq('  {} not found in quality filter spec. Using default value for {}'.format(k, k))
                     qf = self.default_quality_filters[k]
                 else:
-                    self.printdq(
-                        '  {} found in quality filters specified in input!'.format(k),
-                    )
+                    self.printdq('  {} found in quality filters specified in input!'.format(k))
                 self.quality_filters[k] = qf
             for sk in sub_keys:
                 if sk in quality_filters:
-                    self.printdq(
-                        '  Input quality filter spec has data for {} subsystem, updating values...'.format(sk),
-                    )
+                    self.printdq('  Input quality filter spec has data for {} subsystem, updating values...'.format(sk))
                     keys = list(qualit_filters[sk].keys())
                     for k in keys:
                         qf = quality_filters[sk].get(k, None)
                         if qf is None:
                             self.printdq(
                                 '    {} not found in quality filter spec for {} subsystem. '
-                                'Using default value for {}/{}'.format(k, sk, sk, k),
+                                'Using default value for {}/{}'.format(k, sk, sk, k)
                             )
                             qf = self.default_quality_filters[sk][k]
                         else:
-                            self.printdq(
-                                '    {}/{} found in quality filters specified in input!'.format(sk, k),
-                            )
+                            self.printdq('    {}/{} found in quality filters specified in input!'.format(sk, k))
                         self.quality_filters[sk][k] = qf
         else:
             printw('  Did not understand what to do with quality filter specification. Using defaults instead.')
 
         # Handle ELM filter
         self.elm_filter = False  # This would be an instance of the ELM filtering module if it were in use.
+
+        # Put here so not always imported - requires framework
+        from omfit_classes.omfit_elm import OMFITelm
+
         if elm_filter is None:
             self.elm_filter = OMFITelm(shot=shot, device=device)
         elif elm_filter in ['disabled', 'off', 'no']:
             print('  ELM filter disabled')
         elif isinstance(elm_filter, OMFITelm):
             self.elm_filter = elm_filter
         else:
@@ -497,75 +488,59 @@
 
         elm_settings = {}  # Not hooked up yet, sorry.
 
         print('  OMFITthomson: Checking filtered data...')
         # Check saved settings from the TS group vs. the settings namelist; they should match
         for i in check_elm:
             try:
-                self.printdq(
-                    '    elm check: {}'.format(i),
-                )
-                self.printdq(
-                    '    saved: {}'.format(self['filtered']['settings'][i]),
-                )
-                self.printdq(
-                    '    settings: {}'.format(elm_settings['ELM_filter'][i]),
-                )
+                self.printdq('    elm check: {}'.format(i))
+                self.printdq('    saved: {}'.format(self['filtered']['settings'][i]))
+                self.printdq('    settings: {}'.format(elm_settings['ELM_filter'][i]))
                 if np.any(np.atleast_1d(self['filtered']['settings'][i] != elm_settings['ELM_filter'][i])):
                     filter_settings_okay = False
                     print(
                         'ELM filter settings do not match: saved {:} = {:} vs. tree settings {:} = {:}. Need to '
                         're-filter...'.format(i, self['filtered']['settings'][i] + 0, i, elm_settings['ELM_filter'][i] + 0)
                     )
             except KeyError:
                 filter_settings_okay = False
 
         # Check saved settings from the ELM group vs. the settings namelist; they should match
         for subsys in self.subsystems:
-            self.printdq(
-                '  OMFITthomson: Checking TS sys: {}'.format(subsys),
-            )
+            self.printdq('  OMFITthomson: Checking TS sys: {}'.format(subsys))
             if subsys in self['filtered']:
                 for i in check_ts:
                     try:
-                        self.printdq(
-                            'TS check: {}'.format(i),
-                        )
+                        self.printdq('TS check: {}'.format(i))
                         if i in self.quality_filters['global_override']:
                             set_tmp = self.quality_filters['global_override'][i]
                         else:
                             set_tmp = None
-                        self.printdq(
-                            '    {} = {}'.format(i, set_tmp),
-                        )
+                        self.printdq('    {} = {}'.format(i, set_tmp))
                         if set_tmp is None:
                             set_tmp = self.quality_filters[subsys][i]
                             self.printdq(
                                 '    > {} = {}   (None as a global setting is code for use the subsys '
-                                'specific setting)'.format(i, set_tmp),
-                            )
-                            self.printdq(
-                                '       {}'.format(self['filtered'][subsys]['settings'][i]),
+                                'specific setting)'.format(i, set_tmp)
                             )
+                            self.printdq('       {}'.format(self['filtered'][subsys]['settings'][i]))
                         if self['filtered'][subsys]['settings'][i] != set_tmp:
                             filter_settings_okay = False
                             print(
                                 'TS quality filter settings do not match: saved {:} = {:} vs current tree setting {:}'
                                 ' = {:}. Need to refilter...'.format(i, self['filtered'][subsys]['settings'][i], i, set_tmp)
                             )
                     except KeyError:
                         filter_settings_okay = False
                         print(
                             'Failed when checking {} filter settings for consistency in subsys {}. '
                             'Need to re-filter...'.format(i, subsys)
                         )
             else:
-                self.printdq(
-                    '    subsys {} not in filtered output',
-                )
+                self.printdq('    subsys {} not in filtered output')
 
         self.status['filtered'] *= filter_settings_okay
         return filter_settings_okay
 
     def check_efit_info(self):
         """
         Checks for consistency of any currently loaded EFIT data
@@ -574,23 +549,19 @@
         """
         need_new_efit_data = False
         check_if_match = {'shot': [self.shot], 'efitID': [self.efitid, 'CAKE']}
         for check_name, check_values in list(check_if_match.items()):
             try:
                 match = self['efit_data'][check_name] in check_values
             except KeyError:
-                self.printdq(
-                    '  KeyError when checking {}: need to gather new EFIT data'.format(check_name),
-                )
+                self.printdq('  KeyError when checking {}: need to gather new EFIT data'.format(check_name))
                 need_new_efit_data = True
             else:
                 need_new_efit_data *= not match
-                self.printdq(
-                    '   {} matches = {};  need_new_efit = {}'.format(check_name, match, need_new_efit_data),
-                )
+                self.printdq('   {} matches = {};  need_new_efit = {}'.format(check_name, match, need_new_efit_data))
         return need_new_efit_data
 
     def to_dataset(self):
         """
         Packs data into a list of xarray Dataset instances, one per subsystem
 
         :return: dictionary with one Dataset instance for each subsystem
@@ -693,17 +664,15 @@
             if is_device(self.device, 'DIII-D'):
                 # Handle DIII-D version, which has subsystems.
 
                 # Loop through TS subsystems
                 for subsys in self.subsystems:
                     # Build the base of the call so we can add just the measurement to the end of it later
                     basecall = '.ts.{:}.{:}.'.format(revision, subsys)
-                    self.printdq(
-                        '  sys = {}, basecall = {}'.format(subsys, basecall),
-                    )
+                    self.printdq('  sys = {}, basecall = {}'.format(subsys, basecall))
 
                     out[subsys] = SortedDict()  # Make sure the output location exists
 
                     # Loop through quantities to gather
                     for meas in self.measurements:
                         call = basecall + meas
                         data = OMFITmdsValue(server=self.device, treename=treename, shot=self.shot, TDI=call)
@@ -714,36 +683,30 @@
                             # We don't even have to bother covering for a case where the time dimensions within a TS
                             # subsystem don't match because the case is probably un-salvageable and horribly corrupted.
                             out[subsys]['time'] = data.dim_of(0)
 
             elif is_device(self.device, ('NSTX', 'NSTX-U')):
                 # Handle NSTX/U version, which does not have subsystems.
                 basecall = '.mpts.output_data.{:}.'.format(revision)
-                self.printdq(
-                    '  basecall = {}'.format(basecall),
-                )
+                self.printdq('  basecall = {}'.format(basecall))
                 subsys = tolist(self.subsystems)[0]
                 print(
                     'NSTX/NSTX-U do not have sub-systems like at DIII-D, so we will pretend that all data are from '
                     'the first subsystem in the list, which is {}'.format(subsys)
                 )
                 out[subsys] = SortedDict()  # Make sure the output location exists
                 data = None
 
-                self.printdq(
-                    '  Starting loop through measurements: {}'.format(measurements),
-                )
+                self.printdq('  Starting loop through measurements: {}'.format(measurements))
                 for meas_ in measurements:
                     meas = measurement_translations.get(server, {}).get(meas_, None)
                     ucf = unit_conversion_factors.get(server, {}).get(meas_, 1)
                     if meas is not None:
                         call = basecall + meas
-                        self.printdq(
-                            '   call = {}, shot = {}, server = {}, treename = {}'.format(call, self.shot, self.device, treename),
-                        )
+                        self.printdq('   call = {}, shot = {}, server = {}, treename = {}'.format(call, self.shot, self.device, treename))
                         data = OMFITmdsValue(server=self.device, treename=treename, shot=self.shot, TDI=call)
                         out[subsys][meas_] = data.data() * ucf
 
                     # These signals better have the same time dimension, or else something is very wrong. We don't
                     # even have to bother covering for a case where the time dimensions don't match because the case
                     # is probably un-salvageable and horribly corrupted.
                     ucf = unit_conversion_factors.get(self.device, {}).get('time', 1)
@@ -873,17 +836,15 @@
         if is_device(self.device, ['NSTX', 'NSTXU']) and self.efitid.upper().startswith('EFIT'):
             printw(
                 'WARNING: Mapping of NSTX/U data to basic EFITs typically produces inaccurate results! '
                 'Watch out for double valued profiles in the pedestal. Properly tuning psi_N mapping of NSTX '
                 'Thomson data is complicated.'
             )
 
-        self.printdq(
-            'map_TS systems = {}'.format(self.subsystems),
-        )
+        self.printdq('map_TS systems = {}'.format(self.subsystems))
 
         # Make sure the tree is set to accept processed data (psin for TS)
         self['processed'] = SortedDict()
 
         # Gather data
         need_to_gather = False  # For Thomson
         try:  # The recorded shot for gathered data should match the shot in the settings tree. Otherwise, gather.
@@ -904,22 +865,18 @@
                 need_to_gather_efit = True
             if self['efit_data']['efitid'] != self.efitid:
                 need_to_gather_efit = True
         except KeyError:
             need_to_gather_efit = True
 
         if need_to_gather_efit:
-            self.printdq(
-                '  map_TS: need to gather EFIT info again',
-            )
+            self.printdq('  map_TS: need to gather EFIT info again')
             self.gather_efit_info()
 
-        self.printdq(
-            '  map_TS: done dealing with gathering stuff',
-        )
+        self.printdq('  map_TS: done dealing with gathering stuff')
         # At this point, data should be available.
 
         # Get some info out of EFIT
         efit_r = self['efit_data']['r']
         efit_z = self['efit_data']['z']
         if len(np.atleast_1d(np.shape(efit_r))) == 2:
             # Oh great, someone decided to save R as being time dependent, even though it probably isn't.
@@ -941,28 +898,24 @@
                 while efit_r[:, ii].max() == 0:
                     ii += 1
                 efit_r = efit_r[:, ii]
                 efit_z = efit_z[:, ii]
             else:
                 raise ValueError('Problem finding which axis to deal with when collapsing EFIT R grid.')
         elif len(np.atleast_1d(np.shape(efit_r))) == 1:
-            self.printdq(
-                '  EFIT R grid is 1D, which is how we like it. Good.',
-            )
+            self.printdq('  EFIT R grid is 1D, which is how we like it. Good.')
         else:
             raise ValueError('EFIT R grid has too many dimensions! np.shape(efit_r) = {}'.format(np.shape(efit_r)))
 
         # We have to make sure we get the best EFIT slice for each Thomson slice. We will compare timings.
         efit_time = self['efit_data']['time']
         # Filter EFIT slices to remove slices that are full of all zeros
         psin = self['efit_data']['psin']  # This psin is a function of efit_time, efit_r, and efit_z
         maxpsin = np.max(psin, axis=(1, 2))  # Maximum value at any point in space for each time slice
-        self.printdq(
-            '  map_TS: max value in space at each time slice maxpsin: np.shape(maxpsin) = {}'.format(np.shape(maxpsin)),
-        )
+        self.printdq('  map_TS: max value in space at each time slice maxpsin: np.shape(maxpsin) = {}'.format(np.shape(maxpsin)))
 
         if remove_efits_with_large_changes:
             # Fine idea, but it doesn't seem to reliably get rid of EFITs where the innermost TS point jumps really far,
             # so the plot still looks stupid. Maybe we just need a better plot than tricontourf.
             sm = self['efit_data']['ssimag']  # un-normalized pSI values at the MAGnetic axis and at the BoundaRY
             bm = self['efit_data']['ssibry']
             #                             Sorry, I don't know what's up with the first s or why it's ssi instead of psi.
@@ -1015,61 +968,51 @@
                 slice_to_use[w] = 0
                 first_ts = max(w) + 1
             else:
                 first_ts = 0
             self.printdq(
                 '  OMFITthomson.map: first_ts = {:}   (first TS time-slice that is within EFIT time range; '
                 'earlier TS slices use the first available EFIT although it '
-                'happens later than the early TS data)'.format(first_ts),
+                'happens later than the early TS data)'.format(first_ts)
             )
 
             # If Thomson ends after EFIT (also often happens), then use the last valid EFIt slice for late Thomson data.
             # Thomson after EFIT probably happened after the flattop and you don't care, anyway. It should be apparent
             # that the same EFIT is being used if you look at a contour.
             w = np.where(ts_time > max(efit_time))[0]
             if len(w) > 0:
                 slice_to_use[w] = len(efit_time) - 1
                 last_ts = min(w) - 1
             else:
                 last_ts = len(ts_time) - 1
             self.printdq(
                 '  map_TS: last_ts = {:}  (last TS time-slice that is within EFIT time range; '
-                'any slice later than this will use the last EFIT available)'.format(last_ts),
+                'any slice later than this will use the last EFIT available)'.format(last_ts)
             )
 
             # Now go slice by slice and find the closest EFIT slice to each TS slice.
             ts_slices = np.arange(first_ts, last_ts + 1)  # This is a list of indices of TS slices that are within the
             #                                               EFIT time range and we should bother to find them the
             #                                               closest EFIT.
-            self.printdq(
-                '     ts_slices = {}    (indices of TS slices that are within EFIT time range)'.format(ts_slices),
-            )
-            self.printdq(
-                '     len(ts_slices) = {}'.format(len(ts_slices)),
-            )
-            self.printdq(
-                '     ts_time[ts_slices] = {}'.format(ts_time[ts_slices]),
-            )
+            self.printdq('     ts_slices = {}    (indices of TS slices that are within EFIT time range)'.format(ts_slices))
+            self.printdq('     len(ts_slices) = {}'.format(len(ts_slices)))
+            self.printdq('     ts_time[ts_slices] = {}'.format(ts_time[ts_slices]))
 
             for i in ts_slices:
                 # For each TS time slice, find index of the EFIT slice to use
                 slice_to_use[i] = closestIndex(efit_time, ts_time[i])
 
             slice_to_use = slice_to_use.astype(int)
 
             if self.debug:
                 self['debugging']['slice_to_use'] = slice_to_use
+            self.printdq('     np.shape(slice_to_use) = {}'.format(np.shape(slice_to_use)))
+            self.printdq('     np.shape(efit_time) = {}   (this is after the wefg filter)'.format(np.shape(efit_time)))
             self.printdq(
-                '     np.shape(slice_to_use) = {}'.format(np.shape(slice_to_use)),
-            )
-            self.printdq(
-                '     np.shape(efit_time) = {}   (this is after the wefg filter)'.format(np.shape(efit_time)),
-            )
-            self.printdq(
-                '     np.shape(psin) = {}   (this is the psin from the EFIT after filtering out bad slices)'.format(np.shape(psin)),
+                '     np.shape(psin) = {}   (this is the psin from the EFIT after filtering out bad slices)'.format(np.shape(psin))
             )
 
             # #############---------------------------------
             # Okay, great. We should know which EFIT slice is best for each TS slice. You could interpolate the EFIT in
             # time to be fancier, but this probably doesn't matter. It's fine. Let's go!
 
             # We're going to do a fast spatial interpolation.
@@ -1198,21 +1141,19 @@
             #                                               Global filter settings take precedence if not ==None
             selected_filters = {}
             # Things where the global should be able to take over
             for thing in ['redchisq_limit', 'frac_temp_err_hot_max', 'frac_temp_err_cold_max', 'frac_dens_err_max', 'hot_cold_boundary']:
                 if fg[thing] is not None:
                     self.printdq(
                         '  Using GLOBAL OVERRIDE setting for {:} filter setting {:}, value = {:}  '
-                        '<<<< OVERRIDE'.format(subsys, thing, fg[thing]),
+                        '<<<< OVERRIDE'.format(subsys, thing, fg[thing])
                     )
                     selected_filters[thing] = fg[thing]
                 else:
-                    self.printdq(
-                        'Using system specific setting for {:} filter setting {:}, value = {:}'.format(subsys, thing, fs[thing]),
-                    )
+                    self.printdq('Using system specific setting for {:} filter setting {:}, value = {:}'.format(subsys, thing, fs[thing]))
                     selected_filters[thing] = fs[thing]
             # Things which are system-specific only
             for thing in ['bad_chords']:
                 selected_filters[thing] = fs[thing]
 
             # Unpack (not all of them need to be unpacked because I put in selected_filters[''] around them
             redchisq_limit = selected_filters['redchisq_limit']
@@ -1358,17 +1299,15 @@
             filt['two_d_okay'] = two_d_okay
 
             # Save filtered data
             if self.quality_filters['remove_bad_slices']:
                 for tag in ['temp', 'temp_e', 'density', 'density_e', 'redchisq']:
                     # These get bad slices & chords removed. Remaining bad points are set to 0 by multiplying by `okay`.
                     if self['raw'][subsys].get(tag, None) is None:
-                        self.printdq(
-                            '  {} was None in system {}! Copying `None` across without filtering.'.format(tag, sys),
-                        )
+                        self.printdq('  {} was None in system {}! Copying `None` across without filtering.'.format(tag, sys))
                         fsys[tag] = None
                     else:
                         fsys[tag] = self['raw'][subsys][tag][wc, :][:, wt]
                 for tag in ['psin_TS']:
                     # This is like the above entry for temp, etc.,
                     # but separate because it's in a different place than raw data.
                     fsys[tag] = self['processed'][subsys][tag][wc, :][:, wt]
@@ -1502,85 +1441,67 @@
             dictionary containing x, y, e, and other information. x, y, and e are sorted by psi_N.
         """
         from operator import itemgetter
 
         if systems == 'all':
             systems = self.subsystems
 
-        self.printdq(
-            'OMFITthomson: select_time_window...',
-        )
+        self.printdq('OMFITthomson: select_time_window...')
         if comment is not None:
-            self.printdq(
-                'OMFITthomson: {}'.format(comment),
-            )
+            self.printdq('OMFITthomson: {}'.format(comment))
 
         if realtime:
             ts_src = 'filtered_RTTS'
         else:
             ts_src = 'filtered'
 
         # Minor notifications (tell user not to try to put real values in the unused keywords (uk)
         for ukn, uk in list({'strict': strict}.items()):
             if uk is not None:
-                self.printdq(
-                    '   {} keyword is ignored by fastTS version of select_time_window(), but its value was not None!'.format(ukn),
-                )
+                self.printdq('   {} keyword is ignored by fastTS version of select_time_window(), but its value was not None!'.format(ukn))
 
         results = self
 
         if ts_src not in results:
             if ts_src == 'filtered_RTTS':
-                self.printdq(
-                    "fastTS: filtered realtime Thomson data missing in INPUTS! Executing RT gather+filter...",
-                )
+                self.printdq("fastTS: filtered realtime Thomson data missing in INPUTS! Executing RT gather+filter...")
                 raise NotImplementedError("Realtime data handling not ready yet")
             else:
-                self.printdq(
-                    "fastTS: filtered Thomson data missing in INPUTS! Executing gather+filter...",
-                )
+                self.printdq("fastTS: filtered Thomson data missing in INPUTS! Executing gather+filter...")
                 self.__call__()
 
         if systems is None:
             systems = [k for k in list(results[ts_src].keys()) if isinstance(results[ts_src][k], dict) and k != 'settings']
-            self.printdq(
-                'Auto-assigned systems to based on filtered data availability: {:}'.format(systems),
-            )
+            self.printdq('Auto-assigned systems to based on filtered data availability: {:}'.format(systems))
 
         # Sanitize inputs
         parameters = tolist(parameters)
         systems = tolist(systems)
         psi_n_range = np.atleast_1d(psi_n_range)
         t0 = np.atleast_1d(t0)[0]
 
         result = {}
         for par in parameters:
-            self.printdq(
-                'Loop through parameters: {:}'.format(par),
-            )
+            self.printdq('Loop through parameters: {:}'.format(par))
             time_slices_used = np.array([])
             systems_used = []
             system_okay = np.zeros(len(systems), bool)
             x1 = np.array([])
             y1 = np.array([])
             e1 = np.array([])
             t1 = np.array([])
             c1 = np.array([])
             sys1 = np.array([])
             chords_used = []
 
             for i_sys, sys in enumerate(systems):
-                self.printdq(
-                    'Loop through systems: {:}'.format(sys),
-                )
+                self.printdq('Loop through systems: {:}'.format(sys))
                 # Make sure this system & parameter were gathered
                 if sys not in results[ts_src]:
-                    self.printdq(
-                        ' No data for subsystem {:}'.format(sys),
-                    )
+                    self.printdq(' No data for subsystem {:}'.format(sys))
                     continue
 
                 if par not in results[ts_src][sys] or results[ts_src][sys][par] is None:
                     printw(' fastTS select_time_window(): No data for this parameter: {:}'.format(par))
                     continue
 
                 if use_shifted_psi:
@@ -1588,40 +1509,32 @@
                         if isinstance(alt_x_path, str):
                             alt_x_path = eval(alt_x_path)
                         else:
                             alt_x_path = alt_x_path
                         x = alt_x_path[sys]['psin_corrected']
                     except (KeyError, TypeError):
                         x = results[ts_src][sys]['psin_TS']
-                        self.printdq(
-                            ' Got psi_N values from filtered_TS (not using shifted profiles)',
-                        )
+                        self.printdq(' Got psi_N values from filtered_TS (not using shifted profiles)')
                     else:
                         self.printdq(
                             ' Got psi_N values from alt_x_path (probably using shifted profiles) (path = {})'.format(
                                 treeLocation(alt_x_path)[-1]
-                            ),
-                        )
-                        self.printdq(
-                            '   psi_N values: min = {}, max = {}, average = {}'.format(x.min(), x.max(), x.mean()),
+                            )
                         )
+                        self.printdq('   psi_N values: min = {}, max = {}, average = {}'.format(x.min(), x.max(), x.mean()))
                 else:
                     x = results[ts_src][sys]['psin_TS']
-                    self.printdq(
-                        ' Got psi_N values from filtered_TS (not using shifted profiles)',
-                    )
+                    self.printdq(' Got psi_N values from filtered_TS (not using shifted profiles)')
 
                 y = results[ts_src][sys][par]
 
                 try:
                     e = results[ts_src][sys]['{:}_e'.format(par)]
                 except KeyError:
-                    self.printdq(
-                        ' Could not find uncertainties for this parameter: {:}'.format(par),
-                    )
+                    self.printdq(' Could not find uncertainties for this parameter: {:}'.format(par))
                     # User is allowed to request r and z as parameters, but these do not have uncertainties.
                     e = np.zeros(len(np.atleast_1d(x)), type(np.atleast_1d(x)[0]))
                 okay = results[ts_src][sys]['filters']['okay']
                 t = results[ts_src][sys]['time']
                 ch = results[ts_src][sys]['chord_index']
                 ch2 = ch[:, np.newaxis] + np.zeros(np.shape(x))  # 2D version of chord index for tracking chords used
                 sys_num = {'core': 0, 'divertor': 1000, 'tangential': 2000}[sys]
@@ -1635,17 +1548,15 @@
                 wx = (x >= min(psi_n_range)) & (x <= max(psi_n_range))
 
                 # Overall filter
                 w = wt * wx * okay
 
                 # Make sure the filter doesn't delete everything
                 if w.max() < 1:
-                    self.printdq(
-                        ' No data within this time window for this subsystem: {:}+/-{:}, {:}'.format(t0, dt, sys),
-                    )
+                    self.printdq(' No data within this time window for this subsystem: {:}+/-{:}, {:}'.format(t0, dt, sys))
                     continue
 
                 x1 = np.append(x1, x[w])
                 y1 = np.append(y1, y[w])
                 e1 = np.append(e1, e[w])
                 t1 = np.append(t1, t2[w])
                 c1 = np.append(c1, ch2[w])
@@ -1657,24 +1568,20 @@
                 # chords_used0 = ['{}{:02d}'.format(sys[0], int(ch_)) for ch_ in chords_used0]
                 chords_used = np.append(chords_used, chords_used0)
 
                 sys1 = np.append(sys1, [sys] * len(x[w]))
                 systems_used += [sys]
 
                 system_okay[i_sys] = True  # Any error will abort the loop, so we won't get to here unless things are okay.
-                self.printdq(
-                    '  {:} {:} looks okay'.format(par, sys),
-                )
+                self.printdq('  {:} {:} looks okay'.format(par, sys))
                 # Done with system loop
 
             # Finish working on this parameter
             if system_okay.max() < 1:
-                self.printdq(
-                    ' Failed to gather parameter {:} from any subsystem'.format(par),
-                )
+                self.printdq(' Failed to gather parameter {:} from any subsystem'.format(par))
                 continue
 
             # Sort by x
             seq = list(zip(x1, y1, e1, t1, c1, sys1))
             seq2 = sorted(seq, key=itemgetter(0))
             x2, y2, e2, t22, c22, sys2 = list(zip(*seq2))
 
@@ -1711,33 +1618,25 @@
 
             :param data: result dictionary containing data to be perturbed.
 
             :param pert: Instructions for applying perturbations.
 
             :return: result dictionary with perturbations added.
             """
-            self.printdq(
-                'Adding perturbations to Thomson data returned by select_time_window()...',
-            )
+            self.printdq('Adding perturbations to Thomson data returned by select_time_window()...')
             try:
-                self.printdq(
-                    '  pert.keys() = {}'.format(list(pert.keys())),
-                )
+                self.printdq('  pert.keys() = {}'.format(list(pert.keys())))
             except AttributeError:
                 pass
             else:
                 if 'data_mask' in list(pert.keys()):
                     try:
-                        self.printdq(
-                            "    pert['data_mask'].keys() = {}".format(list(pert['data_mask'].keys())),
-                        )
+                        self.printdq("    pert['data_mask'].keys() = {}".format(list(pert['data_mask'].keys())))
                     except AttributeError:
-                        self.printdq(
-                            "    pert['data_mask'] = {}".format(pert['data_mask']),
-                        )
+                        self.printdq("    pert['data_mask'] = {}".format(pert['data_mask']))
 
             # Figure out perturbation type
             if isinstance(pert, dict):
                 # Normally, the user should pass in a dictionary for pert with pert['type'] = the type they want.
                 randomize = pert.get('random', True)
                 sigma = pert.get('sigma', 1)
                 step_size = pert.get('step_size', None)
@@ -1754,71 +1653,53 @@
                     channel_mask = None
                     time_mask = None
                     data_mask = None
                 else:
                     # Perturbations turned off
                     return data
             elif pert is None:
-                self.printdq(
-                    'pert is None: perturbations disabled',
-                )
+                self.printdq('pert is None: perturbations disabled')
                 return data
             else:
                 # Could not figure it out
                 printe('Could not figure out perturbation type. Aborting perturb_data() and returning unperturbed data.')
                 print('  pert = {}'.format(pert))
                 return data
 
             if data_mask:
-                self.printdq(
-                    '  Data mask detected; disabling channel_mask and time_mask.',
-                )
+                self.printdq('  Data mask detected; disabling channel_mask and time_mask.')
                 time_mask = None
                 channel_mask = None
 
             for par_ in list(data.keys()):
-                self.printdq(
-                    ' Perturbing {}...'.format(par_),
-                )
+                self.printdq(' Perturbing {}...'.format(par_))
                 p = data[par_]
 
                 def setup_mask(mask_, xx, is_data=False, label=''):
-                    self.printdq(
-                        '   Mask setup... ({})'.format(label),
-                    )
+                    self.printdq('   Mask setup... ({})'.format(label))
                     n = len(xx)
                     if not (len(np.atleast_1d(mask_)) > 5 or isinstance(mask_, dict)):
-                        self.printdq(
-                            '     Input mask = {}'.format(mask_),
-                        )
+                        self.printdq('     Input mask = {}'.format(mask_))
                     elif isinstance(mask_, dict):
-                        self.printdq(
-                            '     Input mask is a dictionary with mask_.keys() = {}'.format(list(mask_.keys())),
-                        )
+                        self.printdq('     Input mask is a dictionary with mask_.keys() = {}'.format(list(mask_.keys())))
                         for key in list(mask_.keys()):
                             self.printdq("         len(mask_['{}']) = {}".format(key, len(mask_[key])))
                     elif len(np.atleast_1d(mask_)) > 5:
-                        self.printdq(
-                            '     Input mask is type {} with length {}'.format(type(mask_), len(np.atleast_1d(mask_))),
-                        )
+                        self.printdq('     Input mask is type {} with length {}'.format(type(mask_), len(np.atleast_1d(mask_))))
                     else:
-                        self.printdq(
-                            '     Input mask is type {}'.format(type(mask_)),
-                        )
+                        self.printdq('     Input mask is type {}'.format(type(mask_)))
                     mask_g = copy.deepcopy(mask_)
                     if mask_g is not None:
                         # Try to get out the mask
                         mask = mask_g.get(par_, None)
                     else:
                         mask = None
                     if mask is None:
                         # Make up the default mask, which passes everything
-                        self.printdq(
-                            '        Input mask was replaced with all True because it was None.',
-                        )
+                        self.printdq('        Input mask was replaced with all True because it was None.')
                         mask = np.ones(n, bool)
                     # Try to detect a mask which has been input as a list of channels or slices to pass.
                     mask_okay = (type(tolist(mask)[0]) in [bool, bool_]) and (len(mask) == n)
 
                     if not mask_okay:
                         if is_data:
                             # The normal mask transformations for channel & time don't work for data, so fail everything
@@ -1835,17 +1716,15 @@
                                     '        Improperly formed {} MASK detected for {}; len(mask) = {} vs. '
                                     'len(xx) = {}. Cancelling perturbations...'.format(label, par_, len(mask), len(xx))
                                 )
                                 mask = (xx * 0).astype(bool)
                             else:
                                 # Assume that mask is a list of time slices or channels to use. Loop through each
                                 # channel or time in the list and flag every datum which matches.
-                                self.printdq(
-                                    '     mask needs additional processing...',
-                                )
+                                self.printdq('     mask needs additional processing...')
                                 if not (
                                     (isinstance(mask[0], type(xx[0])))
                                     or (isinstance(mask[0], str) and isinstance(xx[0]), str)
                                     or (is_numeric(mask[0]) and is_numeric(xx[0]))
                                 ):
                                     raise ValueError(
                                         'Incompatible types between mask and data or coordinate to be masked '
@@ -1858,21 +1737,19 @@
                                     if len(np.atleast_1d(xx == m)) != len(mask):
                                         raise ValueError(
                                             'An error occurred while masking data for perturbations: '
                                             'length of mask did not match length of match adjustment.'
                                         )
                                     mask[xx == m] = True
                     else:
-                        self.printdq(
-                            '    Mask is a list of bools of the correct length ({}); No more processing!'.format(len(mask)),
-                        )
+                        self.printdq('    Mask is a list of bools of the correct length ({}); No more processing!'.format(len(mask)))
                         self.printdq(
                             '   Done processing mask. len(mask) = {}, len(xx) = {}, label = {}, is_data = {}.'.format(
                                 len(mask), len(xx), label, is_data
-                            ),
+                            )
                         )
 
                     return mask
 
                 # Resolve masks into lists of T/F flags matching the lengths of time_slices_used, channels_used, and x
                 tm_ = setup_mask(time_mask, p['time_slices_used'], label='time')
                 cm_ = setup_mask(channel_mask, p['channels_used'], label='channel')
@@ -1887,29 +1764,23 @@
                 # Combine masks into base perturbation
                 final_mask = dm_ & cm_ & tm_
                 perturbation_ = copy.copy(final_mask).astype(float)
 
                 # Scale the perturbation by sigma*e or by step_size
                 if step_size:
                     perturbation_ *= step_size
-                    self.printdq(
-                        '  Scaled perturbations by absolute step_size {}'.format(step_size),
-                    )
+                    self.printdq('  Scaled perturbations by absolute step_size {}'.format(step_size))
                 else:
                     perturbation_ *= sigma * p['e']
-                    self.printdq(
-                        '  Scaled perturbations by some number of standard deviations ({})'.format(sigma),
-                    )
+                    self.printdq('  Scaled perturbations by some number of standard deviations ({})'.format(sigma))
 
                 if randomize:
                     # Scale the perturbation by normally distributed random numbers
                     perturbation_ *= np.random.normal(0, 1, len(perturbation_))
-                    self.printdq(
-                        '  Randomized perturbations',
-                    )
+                    self.printdq('  Randomized perturbations')
 
                 p['perturbation'] = perturbation_
                 p['perturbation_added'] = np.any(perturbation_)
                 p['y'] += perturbation_
                 p['final_perturbation_mask'] = final_mask
                 p['perturbation_masks'] = {'time': tm_, 'channel': cm_, 'data': dm_, 'valid_lists': {'t': valid_t, 'ch': valid_ch}}
             return data
@@ -1919,17 +1790,15 @@
             result = perturb_data(result, perturbation)
             result['_perturbation_added'] = False
             for par in parameters:
                 if par in result:
                     if result[par].setdefault('perturbation_added', False):
                         result['_perturbation_added'] = True
         else:
-            self.printdq(
-                'No perturbations added to Thomson data',
-            )
+            self.printdq('No perturbations added to Thomson data')
             for par in parameters:
                 if par in result:
                     result[par]['perturbation'] = None
                     result[par]['perturbation_added'] = False
             result['_perturbation_added'] = False
 
         # Record instructions for perturbations
@@ -2042,17 +1911,17 @@
 
         :return: lnLambda, lnLambda_e
         """
 
         # General? lnLambda; Source: Callen 2006 book: Fundamentals of plasma physics chapter 2
         ee = 4.8032e-10  # Elementary charge in statcoulomb
         te_erg = te * constants.eV * 1e7
-        r_c = ee ** 2 / te_erg  # cm
+        r_c = ee**2 / te_erg  # cm
         r_c /= 100.0  # (m) Classical distance of closest approach
-        r_qm = 1.1e-10 / te ** 0.5  # m Quantum Mechanical distance of closest approach
+        r_qm = 1.1e-10 / te**0.5  # m Quantum Mechanical distance of closest approach
         r_min = np.maximum(r_c, r_qm)
         ln_lambda = np.log(nominal_values(debye / r_min))
 
         # lnLambda for electron-electron collisions; Source: NRL Plasma Formulary 2009
         ln_lambda_e = (
             23.5
             - np.log((nominal_values(ne) / 1e6) ** 0.5 * nominal_values(te) ** (-5.0 / 4.0))
@@ -2094,27 +1963,25 @@
         :param m_b: Atomic mass of beam species (normally deuterium) in atomic mass units
 
         :param z_b: Atomic number of beam species (normally deuterium) in elementary charges
 
         :return: Fast ion slowing down time in ms.
         """
 
-        self.printdq(
-            'fastTS: OMFITlib_slowdown_time...',
-        )
+        self.printdq('fastTS: OMFITlib_slowdown_time...')
 
-        c = 6.3e8 * m_b / z_b ** 2  # Collect constants
+        c = 6.3e8 * m_b / z_b**2  # Collect constants
 
         ne2 = ne * 1e-6  # Convert from m^-3 to cm^-3
 
         bottom = ne2 * ln_lambda_e
         recip = bottom * 0
         recip[bottom > 0] = 1.0 / bottom[bottom > 0]  # Avoid divide by zero
 
-        tau_se = c * te ** 1.5 * recip  # Seconds
+        tau_se = c * te**1.5 * recip  # Seconds
 
         return tau_se * 1000  # ms
 
     @staticmethod
     def data_filter(*args, **kwargs):
         """
         Removes bad values from arrays to avoid math errors, for use when calculating Thomson derived quantities
```

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_timcon.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_timcon.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_toksearch.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_toksearch.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_toq.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_toq.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_transp.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_transp.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_trip3d.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_trip3d.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_tsc.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_tsc.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_uda.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_uda.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_uedge.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_uedge.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_ufile.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_ufile.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_weblink.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_weblink.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/omfit_xml.py` & `omfit_classes-3.2023.7.2/omfit_classes/omfit_xml.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/OMFITsave.txt` & `omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/OMFITsave.txt`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/skeleton/NEW_MODULE/help.rst` & `omfit_classes-3.2023.7.2/omfit_classes/skeleton/NEW_MODULE/help.rst`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettings.txt` & `omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettings.txt`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/skeleton/skeletonMainSettingsNamelist.txt` & `omfit_classes-3.2023.7.2/omfit_classes/skeleton/skeletonMainSettingsNamelist.txt`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/sortedDict.py` & `omfit_classes-3.2023.7.2/omfit_classes/sortedDict.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/startup_choice.py` & `omfit_classes-3.2023.7.2/omfit_classes/startup_choice.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/startup_classes.py` & `omfit_classes-3.2023.7.2/omfit_classes/startup_classes.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/startup_framework.py` & `omfit_classes-3.2023.7.2/omfit_classes/startup_framework.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/uedge_common_map.json` & `omfit_classes-3.2023.7.2/omfit_classes/uedge_common_map.json`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/unix_os/setup.py` & `omfit_classes-3.2023.7.2/omfit_classes/unix_os/setup.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/utils_base.py` & `omfit_classes-3.2023.7.2/omfit_classes/utils_base.py`

 * *Files 0% similar despite different names*

```diff
@@ -246,15 +246,15 @@
         if "OMAS_ROOT" not in os.environ:
             print(f"$OMAS_ROOT not found: {msg_submodule}")
         else:
             print(f"$OMAS_ROOT: {os.environ['OMAS_ROOT']} does not exist: {msg_submodule}")
     else:
         print(f"$OMAS_ROOT: {os.environ['OMAS_ROOT']}")
         if os.environ['OMAS_ROOT'] in sys.path:
-            sys.path.delete(os.environ['OMAS_ROOT'])
+            sys.path.remove(os.environ['OMAS_ROOT'])
         sys.path.insert(0, os.environ['OMAS_ROOT'])
 
 # Keep track of original environment versions before they get modified within OMFIT
 for k in ['PATH', 'LD_LIBRARY_PATH', 'DYLD_LIBRARY_PATH']:
     if f'ORIGINAL_{k}' not in os.environ and k in os.environ:
         os.environ[f'ORIGINAL_{k}'] = os.environ[k]
 # Add directory of python executable to PATH
```

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/utils_fit.py` & `omfit_classes-3.2023.7.2/omfit_classes/utils_fit.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/utils_fusion.py` & `omfit_classes-3.2023.7.2/omfit_classes/utils_fusion.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/utils_math.py` & `omfit_classes-3.2023.7.2/omfit_classes/utils_math.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/utils_plot.py` & `omfit_classes-3.2023.7.2/omfit_classes/utils_plot.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes/zdata.py` & `omfit_classes-3.2023.7.2/omfit_classes/zdata.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_classes.egg-info/PKG-INFO` & `omfit_classes-3.2023.7.2/omfit_classes.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: omfit-classes
-Version: 3.2023.5.2
+Version: 3.2023.7.2
 Summary: Classes of OMFIT (One Modeling Framework For Integrated Tasks)
 Home-page: https://omfit.io
 Author: OMFIT developers
 Author-email: meneghini@fusion.gat.com
 License: MIT
 Keywords: integrated modeling plasma framework
 Platform: UNKNOWN
```

### Comparing `omfit_classes-3.2023.5.2/omfit_classes.egg-info/SOURCES.txt` & `omfit_classes-3.2023.7.2/omfit_classes.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_gui.py` & `omfit_classes-3.2023.7.2/omfit_gui.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_halt.py` & `omfit_classes-3.2023.7.2/omfit_halt.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_parse_args.py` & `omfit_classes-3.2023.7.2/omfit_parse_args.py`

 * *Files 0% similar despite different names*

```diff
@@ -25,15 +25,15 @@
     parser = argparse.ArgumentParser(description='OMFIT (One Modeling Framework for Integrated Tasks)')
 
     parser.add_argument('-s', '--setup', action='store_true', help='Helper setup for SSH authentication and dependencies')
     parser.add_argument('--purge', action='store_true', help='Purge all files in temporary OMFIT locations')
     parser.add_argument('--reset', action='store_true', help='Reset OMFIT SSH/MDS/SQL connections')
     parser.add_argument('--packages', action='store_true', help='List versions of OMFIT required packages')
     if show_omfit_launch_options:
-        parser.add_argument('-cwd', '--cwd', action='store_true', help='use current working directory as $OMFIT_ROOT')
+        parser.add_argument('--cwd', action='store_true', help='use current working directory as $OMFIT_ROOT')
         parser.add_argument('-P', '--Python', action='store_true', help='Python major/minor release of executable to use (python[3, 3.x])')
     parser.add_argument('-g', '--scriptGui', action='store_true', help='Run the specified script in the GUI')
     parser.add_argument('-p', '--project', action='store', help='Open the specified project (`-1` for most recent project)')
     parser.add_argument('-m', '--module', action='store', nargs='*', help='Load the specified module(s)', metavar='REMOTE/BRANCH:MODULE')
     parser.add_argument(
         '-M', '--Module', action='store', nargs='*', help='Load the specified module(s) in developer mode', metavar='REMOTE/BRANCH:MODULE'
     )
```

### Comparing `omfit_classes-3.2023.5.2/omfit_plot.py` & `omfit_classes-3.2023.7.2/omfit_plot.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_setup.py` & `omfit_classes-3.2023.7.2/omfit_setup.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/omfit_tree.py` & `omfit_classes-3.2023.7.2/omfit_tree.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/setup.py` & `omfit_classes-3.2023.7.2/setup.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/utils.py` & `omfit_classes-3.2023.7.2/utils.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/utils_tk.py` & `omfit_classes-3.2023.7.2/utils_tk.py`

 * *Files identical despite different names*

### Comparing `omfit_classes-3.2023.5.2/utils_widgets.py` & `omfit_classes-3.2023.7.2/utils_widgets.py`

 * *Files identical despite different names*

