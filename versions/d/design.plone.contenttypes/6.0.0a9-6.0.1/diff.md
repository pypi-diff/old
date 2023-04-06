# Comparing `tmp/design.plone.contenttypes-6.0.0a9.tar.gz` & `tmp/design.plone.contenttypes-6.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "design.plone.contenttypes-6.0.0a9.tar", last modified: Thu Feb  2 09:16:25 2023, max compression
+gzip compressed data, was "design.plone.contenttypes-6.0.1.tar", last modified: Thu Apr  6 12:56:11 2023, max compression
```

## Comparing `design.plone.contenttypes-6.0.0a9.tar` & `design.plone.contenttypes-6.0.1.tar`

### file list

```diff
@@ -1,354 +1,362 @@
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.501050 design.plone.contenttypes-6.0.0a9/
--rw-r--r--   0 filippocampi   (501) staff       (20)    12552 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/CHANGES.rst
--rw-r--r--   0 filippocampi   (501) staff       (20)       67 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/CONTRIBUTORS.rst
--rw-r--r--   0 filippocampi   (501) staff       (20)      585 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/DEVELOP.rst
--rw-r--r--   0 filippocampi   (501) staff       (20)    18092 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/LICENSE.GPL
--rw-r--r--   0 filippocampi   (501) staff       (20)      665 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/LICENSE.rst
--rw-r--r--   0 filippocampi   (501) staff       (20)      126 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/MANIFEST.in
--rw-r--r--   0 filippocampi   (501) staff       (20)    28175 2023-02-02 09:16:25.501241 design.plone.contenttypes-6.0.0a9/PKG-INFO
--rw-r--r--   0 filippocampi   (501) staff       (20)    14374 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/README.md
--rw-r--r--   0 filippocampi   (501) staff       (20)       27 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/constraints.txt
--rw-r--r--   0 filippocampi   (501) staff       (20)      105 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/constraints_plone60.txt
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.410029 design.plone.contenttypes-6.0.0a9/docs/
--rw-r--r--   0 filippocampi   (501) staff       (20)     7993 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/docs/conf.py
--rw-r--r--   0 filippocampi   (501) staff       (20)       98 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/docs/index.rst
--rw-r--r--   0 filippocampi   (501) staff       (20)       50 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/requirements.txt
--rw-r--r--   0 filippocampi   (501) staff       (20)      376 2023-02-02 09:16:25.501915 design.plone.contenttypes-6.0.0a9/setup.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     2888 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/setup.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.395254 design.plone.contenttypes-6.0.0a9/src/
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.410386 design.plone.contenttypes-6.0.0a9/src/design/
--rw-r--r--   0 filippocampi   (501) staff       (20)       80 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/__init__.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.414033 design.plone.contenttypes-6.0.0a9/src/design/plone/
--rw-r--r--   0 filippocampi   (501) staff       (20)       80 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/__init__.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.417089 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/
--rw-r--r--   0 filippocampi   (501) staff       (20)      668 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/__init__.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.418938 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      828 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)      421 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/interfaces.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1755 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/searchabletext_indexers.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      231 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/servizi_correlati.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.426754 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1355 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/additional_help_infos.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3091 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/address.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     7281 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/argomenti.py
--rw-r--r--   0 filippocampi   (501) staff       (20)    11761 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     6217 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/contatti.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1630 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/dataset_correlati.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2679 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/descrizione_estesa.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     6637 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/evento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1660 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/geolocation.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2388 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/info_testata.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2734 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/luoghi_correlati.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     6580 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/luogo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1606 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/multi_file.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4408 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/news_additional_fields.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1828 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/servizi_correlati.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1358 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/show_modified.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1689 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/strutture_correlate.py
--rw-r--r--   0 filippocampi   (501) staff       (20)    10532 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/trasparenza.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1164 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/update_note.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.427796 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1342 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/configure.zcml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.429610 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3676 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/change_news_type.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2739 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/check_servizi.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      603 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     2772 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/move_news_items.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.430757 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/templates/
--rw-r--r--   0 filippocampi   (501) staff       (20)     2973 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/templates/change_news_type.pt
--rw-r--r--   0 filippocampi   (501) staff       (20)     6252 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/templates/check_servizi.pt
--rw-r--r--   0 filippocampi   (501) staff       (20)     4075 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/templates/move_news_items.pt
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.431430 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/overrides/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/overrides/.gitkeep
--rw-r--r--   0 filippocampi   (501) staff       (20)      993 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/overrides/plone.app.contenttypes.browser.templates.newsitem.pt
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.397429 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/static/
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.431822 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/static/js/
--rw-r--r--   0 filippocampi   (501) staff       (20)      262 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/static/js/move_content.js
--rw-r--r--   0 filippocampi   (501) staff       (20)      469 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/trasparenza.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2661 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/configure.zcml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.437368 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      315 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/cartella_modulistica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      238 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/dataset.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      246 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/documento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      283 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/documento_personale.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      210 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/evento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      242 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/incarico.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      215 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/luogo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      275 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/messaggio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      229 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/modulo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      271 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/pagina_argomento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      238 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/persona.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      238 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/pratica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      272 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/punto_di_contatto.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      279 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/ricevuta_pagamento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      242 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/servizio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      283 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/content/unita_organizzativa.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.438494 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      737 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1382 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/geolocation_defaults.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3441 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/settings.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.442659 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      540 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/bando.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      277 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/common.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2865 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)      618 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/document.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1265 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/documento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3024 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/evento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1660 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/incarico.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      848 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/luogo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1268 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/notizie_e_comunicati_stampa.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      969 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/pagina_argomento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1886 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/persona.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      631 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/pratica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1053 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/servizio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1078 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/unita_organizzativa.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.445737 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      459 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/bando.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      989 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/common.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1605 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)      411 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/events.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      921 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/news.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      621 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/pagina_argomento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      829 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/persona.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      741 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/punto_di_contatto.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      327 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/servizio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      445 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/uo.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.450201 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/
--rw-r--r--   0 filippocampi   (501) staff       (20)      419 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     6263 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/bando.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      232 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/cartella_modulistica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      857 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/dataset.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     8681 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/documento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4702 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/documento_personale.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5442 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/incarico.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1483 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/messaggio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      205 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/modulo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2600 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/pagina_argomento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4773 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/persona.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1781 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/pratica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2522 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/punto_di_contatto.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1838 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/ricevuta_pagamento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)    18191 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/servizio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     8198 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/unita_organizzativa.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.451835 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/
--rw-r--r--   0 filippocampi   (501) staff       (20)      611 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/README.rst
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/__init__.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.399150 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/__pycache__/
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.452107 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/__pycache__/LC_MESSAGES/
--rw-r--r--   0 filippocampi   (501) staff       (20)    83688 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/__pycache__/LC_MESSAGES/design.plone.contenttypes.po
--rw-r--r--   0 filippocampi   (501) staff       (20)    83643 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/design.plone.contenttypes.pot
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.399566 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/en/
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.452484 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/en/LC_MESSAGES/
--rw-r--r--   0 filippocampi   (501) staff       (20)    83808 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/en/LC_MESSAGES/design.plone.contenttypes.po
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.399965 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.453575 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/LC_MESSAGES/
--rw-r--r--   0 filippocampi   (501) staff       (20)     1243 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/LC_MESSAGES/collective.geolocationbehavior.po
--rw-r--r--   0 filippocampi   (501) staff       (20)    84783 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/LC_MESSAGES/design.plone.contenttypes.po
--rw-r--r--   0 filippocampi   (501) staff       (20)     7287 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/LC_MESSAGES/plone.po
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/plone.pot
--rw-r--r--   0 filippocampi   (501) staff       (20)     1597 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/update.py
--rwxr-xr-x   0 filippocampi   (501) staff       (20)      512 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/update.sh
--rw-r--r--   0 filippocampi   (501) staff       (20)      712 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/overrides.zcml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.454741 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/patches/
--rw-r--r--   0 filippocampi   (501) staff       (20)      516 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/patches/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3395 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/patches/baseserializer.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      483 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/patches/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)      320 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/patches/patches.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2751 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/permissions.zcml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.401859 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.400742 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.462881 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/
--rw-r--r--   0 filippocampi   (501) staff       (20)      314 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/business_events.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     3401 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/business_events.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      331 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/person_life_events.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     4370 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/person_life_events.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      286 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/temi_dataset.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     2870 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/temi_dataset.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      372 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documenti_albopretorio.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     8078 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documenti_albopretorio.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      300 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     2155 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      313 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_evento.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)    13733 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_evento.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      398 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_frequenza_aggiornamento.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     5133 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_frequenza_aggiornamento.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      292 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_incarico.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     1042 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_incarico.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      303 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_licenze.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     2196 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_licenze.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      265 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_luogo.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)    15346 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_luogo.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      322 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     1050 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      355 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_organizzazione.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     3138 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_organizzazione.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      342 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_pdc.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     2275 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_pdc.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      344 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_stati_pratica.cfg
--rw-r--r--   0 filippocampi   (501) staff       (20)     2275 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_stati_pratica.xml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.465724 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/
--rw-r--r--   0 filippocampi   (501) staff       (20)      193 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/browserlayer.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     2682 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/catalog.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1040 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/controlpanel.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1219 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/diff_tool.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      519 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/metadata.xml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.466344 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/registry/
--rw-r--r--   0 filippocampi   (501) staff       (20)    19192 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/registry/criteria.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      618 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/registry/settings.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1139 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/repositorytool.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     4491 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/rolemap.xml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.472295 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/
--rw-r--r--   0 filippocampi   (501) staff       (20)     1155 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Bando.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      503 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Bando_Folder_Deepening.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3563 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/CartellaModulistica.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3327 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Dataset.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      921 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Document.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3747 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Documento.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3321 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Documento_Personale.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     2500 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Event.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3427 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Incarico.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      432 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Link.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3199 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Messaggio.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     2855 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Modulo.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1073 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/News_Item.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3456 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Pagina_Argomento.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3430 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Persona.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3178 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Pratica.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3342 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/PuntoDiContatto.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3149 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/RicevutaPagamento.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3800 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Servizio.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3713 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/UnitaOrganizzativa.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     2160 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Venue.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1194 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types.xml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.472864 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/to_3000/
--rw-r--r--   0 filippocampi   (501) staff       (20)      377 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/to_3000/controlpanel.xml
--rw-r--r--   0 filippocampi   (501) staff       (20)      275 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/to_3000/registry.xml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.473149 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/uninstall/
--rw-r--r--   0 filippocampi   (501) staff       (20)      128 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/uninstall/browserlayer.xml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.474177 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      663 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)      504 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/converters.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      702 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/correlati.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.476652 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      696 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     5362 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/documento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5373 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/dxfields.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5309 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/news.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1659 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/persona.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5410 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/servizio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5456 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/unitaorganizzativa.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     6018 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/venue.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.481589 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1254 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/bando.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2086 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/cartella_modulistica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1508 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     2102 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/documento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2568 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/dxcontent.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4220 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/dxfields.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1452 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/modulo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2190 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/persona.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3771 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/punto_di_contatto.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1763 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/related_news_serializer.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2395 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/relationfield.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1452 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/servizio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     8381 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/summary.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5369 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/unita_organizzativa.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3637 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/venue.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.482396 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      515 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/configure.zcml
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.483307 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/content/
--rw-r--r--   0 filippocampi   (501) staff       (20)       24 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/content/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      664 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/content/add.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      368 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/content/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)      653 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/controlpanel.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.484198 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/modulistica_items/
--rw-r--r--   0 filippocampi   (501) staff       (20)       24 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/modulistica_items/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      605 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/modulistica_items/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     2881 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/modulistica_items/get.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.484968 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/scadenziario/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/scadenziario/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1200 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/scadenziario/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)    10380 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/scadenziario/post.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.485834 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/trasparenza/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/trasparenza/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      884 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/trasparenza/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     3352 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/trasparenza/get.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.486650 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/types/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/types/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      404 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/types/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)    10415 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/types/get.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.487416 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/types/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/types/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3196 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/types/adapters.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      334 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/types/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1629 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/schema_overrides.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2315 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/setuphandlers.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3521 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/testing.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.496360 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)    11218 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/example.pdf
--rw-r--r--   0 filippocampi   (501) staff       (20)     1997 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_argomenti.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2296 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_base_serializer.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1547 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_descrizione_estesa.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     3151 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_luogo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2547 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_show_modified.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1738 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_update_note.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1740 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_change_news_type.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1680 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_bando.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1462 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_cartella_modulistica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1342 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_document.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4723 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_documento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1294 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_documento_personale.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4564 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_event.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     6368 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_luogo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      982 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_modulo.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4770 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_news.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1296 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_pagina_argomento.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     4331 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_persona.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     7076 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_servizio.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     9499 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_unita_organizzativa.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2420 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_move_news_items_view.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     6634 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_relateditems_with_dates.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1382 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_settings_controlpanel_api.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2788 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_setup.py
--rw-r--r--   0 filippocampi   (501) staff       (20)    11038 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_summary_serializer.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1235 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_uo_summary_serializer.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5630 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_vocabularies.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.497625 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)    20047 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     5033 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/draftjs_converter.py
--rw-r--r--   0 filippocampi   (501) staff       (20)    57520 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/upgrades.py
--rw-r--r--   0 filippocampi   (501) staff       (20)      862 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/utils.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.500787 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/
--rw-r--r--   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/__init__.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1308 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/argomenti_vocabulary.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1573 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/available_services_vocabulary.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1824 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/configure.zcml
--rw-r--r--   0 filippocampi   (501) staff       (20)     1468 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/controlapanel_vocabularies.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1895 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/lista_azioni_pratica.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1704 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/mockup.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     2223 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/people_vocabulary.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     1537 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/reference_vocabularies.py
--rw-r--r--   0 filippocampi   (501) staff       (20)     5199 2023-02-02 09:16:24.000000 design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/tags_vocabulary.py
-drwxr-xr-x   0 filippocampi   (501) staff       (20)        0 2023-02-02 09:16:25.413661 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/
--rw-r--r--   0 filippocampi   (501) staff       (20)    28175 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/PKG-INFO
--rw-r--r--   0 filippocampi   (501) staff       (20)    18155 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/SOURCES.txt
--rw-r--r--   0 filippocampi   (501) staff       (20)        1 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/dependency_links.txt
--rw-r--r--   0 filippocampi   (501) staff       (20)      130 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/entry_points.txt
--rw-r--r--   0 filippocampi   (501) staff       (20)       20 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/namespace_packages.txt
--rw-r--r--   0 filippocampi   (501) staff       (20)        1 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/not-zip-safe
--rw-r--r--   0 filippocampi   (501) staff       (20)      404 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/requires.txt
--rw-r--r--   0 filippocampi   (501) staff       (20)        7 2023-02-02 09:16:25.000000 design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/top_level.txt
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.987204 design.plone.contenttypes-6.0.1/
+-rw-r--r--   0 roman      (502) staff       (20)    15692 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/CHANGES.rst
+-rw-r--r--   0 roman      (502) staff       (20)       67 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/CONTRIBUTORS.rst
+-rw-r--r--   0 roman      (502) staff       (20)      585 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/DEVELOP.rst
+-rw-r--r--   0 roman      (502) staff       (20)    18092 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/LICENSE.GPL
+-rw-r--r--   0 roman      (502) staff       (20)      665 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/LICENSE.rst
+-rw-r--r--   0 roman      (502) staff       (20)      158 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/MANIFEST.in
+-rw-r--r--   0 roman      (502) staff       (20)    42597 2023-04-06 12:56:11.987528 design.plone.contenttypes-6.0.1/PKG-INFO
+-rw-r--r--   0 roman      (502) staff       (20)    15519 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/README.md
+-rw-r--r--   0 roman      (502) staff       (20)       27 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/constraints.txt
+-rw-r--r--   0 roman      (502) staff       (20)      105 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/constraints_plone60.txt
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.916762 design.plone.contenttypes-6.0.1/docs/
+-rw-r--r--   0 roman      (502) staff       (20)     7993 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/docs/conf.py
+-rw-r--r--   0 roman      (502) staff       (20)       98 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/docs/index.rst
+-rw-r--r--   0 roman      (502) staff       (20)       50 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/requirements.txt
+-rw-r--r--   0 roman      (502) staff       (20)      383 2023-04-06 12:56:11.988008 design.plone.contenttypes-6.0.1/setup.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     3002 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/setup.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.906792 design.plone.contenttypes-6.0.1/src/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.917034 design.plone.contenttypes-6.0.1/src/design/
+-rw-r--r--   0 roman      (502) staff       (20)       80 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.919473 design.plone.contenttypes-6.0.1/src/design/plone/
+-rw-r--r--   0 roman      (502) staff       (20)       80 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.921522 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/
+-rw-r--r--   0 roman      (502) staff       (20)      668 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.922760 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      828 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      421 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/interfaces.py
+-rw-r--r--   0 roman      (502) staff       (20)     1755 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/searchabletext_indexers.py
+-rw-r--r--   0 roman      (502) staff       (20)      231 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/servizi_correlati.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.927843 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     1354 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/additional_help_infos.py
+-rw-r--r--   0 roman      (502) staff       (20)     2403 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/address.py
+-rw-r--r--   0 roman      (502) staff       (20)     7942 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/argomenti.py
+-rw-r--r--   0 roman      (502) staff       (20)    11450 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     6669 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/contatti.py
+-rw-r--r--   0 roman      (502) staff       (20)     1629 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/dataset_correlati.py
+-rw-r--r--   0 roman      (502) staff       (20)     2679 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/descrizione_estesa.py
+-rw-r--r--   0 roman      (502) staff       (20)     6334 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/evento.py
+-rw-r--r--   0 roman      (502) staff       (20)     1657 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/geolocation.py
+-rw-r--r--   0 roman      (502) staff       (20)     2388 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/info_testata.py
+-rw-r--r--   0 roman      (502) staff       (20)     2733 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/luoghi_correlati.py
+-rw-r--r--   0 roman      (502) staff       (20)     6580 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/luogo.py
+-rw-r--r--   0 roman      (502) staff       (20)     1606 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/multi_file.py
+-rw-r--r--   0 roman      (502) staff       (20)     4559 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/news_additional_fields.py
+-rw-r--r--   0 roman      (502) staff       (20)     1827 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/servizi_correlati.py
+-rw-r--r--   0 roman      (502) staff       (20)     1357 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/show_modified.py
+-rw-r--r--   0 roman      (502) staff       (20)     1688 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/strutture_correlate.py
+-rw-r--r--   0 roman      (502) staff       (20)    10532 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/trasparenza.py
+-rw-r--r--   0 roman      (502) staff       (20)     1164 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/update_note.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.928555 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     1342 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/configure.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.929768 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     3813 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/change_news_type.py
+-rw-r--r--   0 roman      (502) staff       (20)     4601 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/check_servizi.py
+-rw-r--r--   0 roman      (502) staff       (20)      787 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     2796 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/move_news_items.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.930505 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/templates/
+-rw-r--r--   0 roman      (502) staff       (20)     3360 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/templates/change_news_type.pt
+-rw-r--r--   0 roman      (502) staff       (20)     5531 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/templates/check_servizi.pt
+-rw-r--r--   0 roman      (502) staff       (20)     4760 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/templates/move_news_items.pt
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.930934 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/overrides/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/overrides/.gitkeep
+-rw-r--r--   0 roman      (502) staff       (20)      993 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/overrides/plone.app.contenttypes.browser.templates.newsitem.pt
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.908199 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/static/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.931187 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/static/js/
+-rw-r--r--   0 roman      (502) staff       (20)      262 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/static/js/move_content.js
+-rw-r--r--   0 roman      (502) staff       (20)      469 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/trasparenza.py
+-rw-r--r--   0 roman      (502) staff       (20)     2464 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/configure.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.935025 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      315 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/cartella_modulistica.py
+-rw-r--r--   0 roman      (502) staff       (20)      238 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/dataset.py
+-rw-r--r--   0 roman      (502) staff       (20)      246 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/documento.py
+-rw-r--r--   0 roman      (502) staff       (20)      283 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/documento_personale.py
+-rw-r--r--   0 roman      (502) staff       (20)      210 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/evento.py
+-rw-r--r--   0 roman      (502) staff       (20)      242 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/incarico.py
+-rw-r--r--   0 roman      (502) staff       (20)      215 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/luogo.py
+-rw-r--r--   0 roman      (502) staff       (20)      275 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/messaggio.py
+-rw-r--r--   0 roman      (502) staff       (20)      229 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/modulo.py
+-rw-r--r--   0 roman      (502) staff       (20)      271 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/pagina_argomento.py
+-rw-r--r--   0 roman      (502) staff       (20)      238 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/persona.py
+-rw-r--r--   0 roman      (502) staff       (20)      238 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/pratica.py
+-rw-r--r--   0 roman      (502) staff       (20)      272 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/punto_di_contatto.py
+-rw-r--r--   0 roman      (502) staff       (20)      279 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/ricevuta_pagamento.py
+-rw-r--r--   0 roman      (502) staff       (20)      242 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)      283 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/content/unita_organizzativa.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.935917 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      737 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     1382 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/geolocation_defaults.py
+-rw-r--r--   0 roman      (502) staff       (20)     3441 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/settings.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.939289 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      540 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/bando.py
+-rw-r--r--   0 roman      (502) staff       (20)      276 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/common.py
+-rw-r--r--   0 roman      (502) staff       (20)     3259 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      618 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/document.py
+-rw-r--r--   0 roman      (502) staff       (20)     1265 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/documento.py
+-rw-r--r--   0 roman      (502) staff       (20)     3024 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/evento.py
+-rw-r--r--   0 roman      (502) staff       (20)     1660 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/incarico.py
+-rw-r--r--   0 roman      (502) staff       (20)      848 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/luogo.py
+-rw-r--r--   0 roman      (502) staff       (20)     1268 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/notizie_e_comunicati_stampa.py
+-rw-r--r--   0 roman      (502) staff       (20)      969 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/pagina_argomento.py
+-rw-r--r--   0 roman      (502) staff       (20)     1886 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/persona.py
+-rw-r--r--   0 roman      (502) staff       (20)      631 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/pratica.py
+-rw-r--r--   0 roman      (502) staff       (20)     1842 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)     1078 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/unita_organizzativa.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.941710 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      458 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/bando.py
+-rw-r--r--   0 roman      (502) staff       (20)      989 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/common.py
+-rw-r--r--   0 roman      (502) staff       (20)     1605 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      411 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/events.py
+-rw-r--r--   0 roman      (502) staff       (20)      921 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/news.py
+-rw-r--r--   0 roman      (502) staff       (20)      621 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/pagina_argomento.py
+-rw-r--r--   0 roman      (502) staff       (20)      829 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/persona.py
+-rw-r--r--   0 roman      (502) staff       (20)      741 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/punto_di_contatto.py
+-rw-r--r--   0 roman      (502) staff       (20)      327 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)      445 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/uo.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.945433 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/
+-rw-r--r--   0 roman      (502) staff       (20)      419 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     6263 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/bando.py
+-rw-r--r--   0 roman      (502) staff       (20)      699 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/cartella_modulistica.py
+-rw-r--r--   0 roman      (502) staff       (20)      857 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/dataset.py
+-rw-r--r--   0 roman      (502) staff       (20)     8681 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/documento.py
+-rw-r--r--   0 roman      (502) staff       (20)     4702 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/documento_personale.py
+-rw-r--r--   0 roman      (502) staff       (20)     5442 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/incarico.py
+-rw-r--r--   0 roman      (502) staff       (20)     1483 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/messaggio.py
+-rw-r--r--   0 roman      (502) staff       (20)      205 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/modulo.py
+-rw-r--r--   0 roman      (502) staff       (20)     2600 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/pagina_argomento.py
+-rw-r--r--   0 roman      (502) staff       (20)     4773 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/persona.py
+-rw-r--r--   0 roman      (502) staff       (20)     1781 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/pratica.py
+-rw-r--r--   0 roman      (502) staff       (20)     2522 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/punto_di_contatto.py
+-rw-r--r--   0 roman      (502) staff       (20)     1838 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/ricevuta_pagamento.py
+-rw-r--r--   0 roman      (502) staff       (20)    18281 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)     8198 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/unita_organizzativa.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.946820 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/
+-rw-r--r--   0 roman      (502) staff       (20)      611 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/README.rst
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.909396 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/__pycache__/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.947055 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/__pycache__/LC_MESSAGES/
+-rw-r--r--   0 roman      (502) staff       (20)    83688 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/__pycache__/LC_MESSAGES/design.plone.contenttypes.po
+-rw-r--r--   0 roman      (502) staff       (20)    83643 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/design.plone.contenttypes.pot
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.909634 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/en/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.947510 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/en/LC_MESSAGES/
+-rw-r--r--   0 roman      (502) staff       (20)    83808 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/en/LC_MESSAGES/design.plone.contenttypes.po
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.909867 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.948521 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/LC_MESSAGES/
+-rw-r--r--   0 roman      (502) staff       (20)     1243 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/LC_MESSAGES/collective.geolocationbehavior.po
+-rw-r--r--   0 roman      (502) staff       (20)    84783 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/LC_MESSAGES/design.plone.contenttypes.po
+-rw-r--r--   0 roman      (502) staff       (20)     7287 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/LC_MESSAGES/plone.po
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/plone.pot
+-rw-r--r--   0 roman      (502) staff       (20)     1597 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/update.py
+-rwxr-xr-x   0 roman      (502) staff       (20)      512 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/update.sh
+-rw-r--r--   0 roman      (502) staff       (20)      712 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/overrides.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.949448 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/patches/
+-rw-r--r--   0 roman      (502) staff       (20)      516 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/patches/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     3700 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/patches/baseserializer.py
+-rw-r--r--   0 roman      (502) staff       (20)      483 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/patches/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      319 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/patches/patches.py
+-rw-r--r--   0 roman      (502) staff       (20)     2751 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/permissions.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.911062 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.910363 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.956052 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/
+-rw-r--r--   0 roman      (502) staff       (20)      314 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/business_events.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     3401 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/business_events.xml
+-rw-r--r--   0 roman      (502) staff       (20)      331 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/person_life_events.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     4370 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/person_life_events.xml
+-rw-r--r--   0 roman      (502) staff       (20)      286 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/temi_dataset.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     2870 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/temi_dataset.xml
+-rw-r--r--   0 roman      (502) staff       (20)      372 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documenti_albopretorio.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     8078 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documenti_albopretorio.xml
+-rw-r--r--   0 roman      (502) staff       (20)      300 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     2156 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.xml
+-rw-r--r--   0 roman      (502) staff       (20)      313 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_evento.cfg
+-rw-r--r--   0 roman      (502) staff       (20)    13733 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_evento.xml
+-rw-r--r--   0 roman      (502) staff       (20)      398 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_frequenza_aggiornamento.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     5133 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_frequenza_aggiornamento.xml
+-rw-r--r--   0 roman      (502) staff       (20)      292 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_incarico.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     1042 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_incarico.xml
+-rw-r--r--   0 roman      (502) staff       (20)      303 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_licenze.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     2196 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_licenze.xml
+-rw-r--r--   0 roman      (502) staff       (20)      265 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_luogo.cfg
+-rw-r--r--   0 roman      (502) staff       (20)    15346 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_luogo.xml
+-rw-r--r--   0 roman      (502) staff       (20)      322 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     1015 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.xml
+-rw-r--r--   0 roman      (502) staff       (20)      355 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_organizzazione.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     3138 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_organizzazione.xml
+-rw-r--r--   0 roman      (502) staff       (20)      342 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_pdc.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     2275 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_pdc.xml
+-rw-r--r--   0 roman      (502) staff       (20)      344 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_stati_pratica.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     2275 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_stati_pratica.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.957944 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/
+-rw-r--r--   0 roman      (502) staff       (20)      193 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/browserlayer.xml
+-rw-r--r--   0 roman      (502) staff       (20)     2681 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/catalog.xml
+-rw-r--r--   0 roman      (502) staff       (20)     1040 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/controlpanel.xml
+-rw-r--r--   0 roman      (502) staff       (20)     1219 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/diff_tool.xml
+-rw-r--r--   0 roman      (502) staff       (20)      519 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/metadata.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.958519 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/registry/
+-rw-r--r--   0 roman      (502) staff       (20)    19192 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/registry/criteria.xml
+-rw-r--r--   0 roman      (502) staff       (20)      618 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/registry/settings.xml
+-rw-r--r--   0 roman      (502) staff       (20)     1139 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/repositorytool.xml
+-rw-r--r--   0 roman      (502) staff       (20)     4491 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/rolemap.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.963739 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/
+-rw-r--r--   0 roman      (502) staff       (20)     1155 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Bando.xml
+-rw-r--r--   0 roman      (502) staff       (20)      503 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Bando_Folder_Deepening.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3563 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/CartellaModulistica.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3327 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Dataset.xml
+-rw-r--r--   0 roman      (502) staff       (20)      921 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Document.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3747 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Documento.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3321 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Documento_Personale.xml
+-rw-r--r--   0 roman      (502) staff       (20)     2500 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Event.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3427 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Incarico.xml
+-rw-r--r--   0 roman      (502) staff       (20)      432 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Link.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3199 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Messaggio.xml
+-rw-r--r--   0 roman      (502) staff       (20)     2855 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Modulo.xml
+-rw-r--r--   0 roman      (502) staff       (20)     1007 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/News_Item.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3456 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Pagina_Argomento.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3430 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Persona.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3178 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Pratica.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3342 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/PuntoDiContatto.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3149 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/RicevutaPagamento.xml
+-rw-r--r--   0 roman      (502) staff       (20)     4084 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Servizio.xml
+-rw-r--r--   0 roman      (502) staff       (20)     3775 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/UnitaOrganizzativa.xml
+-rw-r--r--   0 roman      (502) staff       (20)     2212 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Venue.xml
+-rw-r--r--   0 roman      (502) staff       (20)     1194 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.964184 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/to_3000/
+-rw-r--r--   0 roman      (502) staff       (20)      377 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/to_3000/controlpanel.xml
+-rw-r--r--   0 roman      (502) staff       (20)      275 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/to_3000/registry.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.964415 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/uninstall/
+-rw-r--r--   0 roman      (502) staff       (20)      128 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/uninstall/browserlayer.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.965239 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      663 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      504 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/converters.py
+-rw-r--r--   0 roman      (502) staff       (20)      702 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/correlati.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.967245 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      760 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     5795 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/documento.py
+-rw-r--r--   0 roman      (502) staff       (20)     6300 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/dxfields.py
+-rw-r--r--   0 roman      (502) staff       (20)     5743 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/news.py
+-rw-r--r--   0 roman      (502) staff       (20)     1658 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/persona.py
+-rw-r--r--   0 roman      (502) staff       (20)     5844 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)     5999 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/unitaorganizzativa.py
+-rw-r--r--   0 roman      (502) staff       (20)     6016 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/venue.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.971003 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     1254 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/bando.py
+-rw-r--r--   0 roman      (502) staff       (20)     2086 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/cartella_modulistica.py
+-rw-r--r--   0 roman      (502) staff       (20)     1858 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     2102 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/documento.py
+-rw-r--r--   0 roman      (502) staff       (20)     3377 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/dxcontent.py
+-rw-r--r--   0 roman      (502) staff       (20)     5307 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/dxfields.py
+-rw-r--r--   0 roman      (502) staff       (20)     1452 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/modulo.py
+-rw-r--r--   0 roman      (502) staff       (20)     2190 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/persona.py
+-rw-r--r--   0 roman      (502) staff       (20)     3771 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/punto_di_contatto.py
+-rw-r--r--   0 roman      (502) staff       (20)     1763 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/related_news_serializer.py
+-rw-r--r--   0 roman      (502) staff       (20)     2401 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/relationfield.py
+-rw-r--r--   0 roman      (502) staff       (20)     1705 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)    13976 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/summary.py
+-rw-r--r--   0 roman      (502) staff       (20)     5523 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/unita_organizzativa.py
+-rw-r--r--   0 roman      (502) staff       (20)     3814 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/venue.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.971660 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      685 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/configure.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.972407 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/content/
+-rw-r--r--   0 roman      (502) staff       (20)       24 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/content/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      664 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/content/add.py
+-rw-r--r--   0 roman      (502) staff       (20)      368 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/content/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      653 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/controlpanel.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.973063 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/modulistica_items/
+-rw-r--r--   0 roman      (502) staff       (20)       24 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/modulistica_items/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      605 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/modulistica_items/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     2915 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/modulistica_items/get.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.973714 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/prenotazioni_folders_list/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/prenotazioni_folders_list/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      556 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/prenotazioni_folders_list/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      834 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/prenotazioni_folders_list/get.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.974357 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/scadenziario/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/scadenziario/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     1200 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/scadenziario/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)    10380 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/scadenziario/post.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.975000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/trasparenza/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/trasparenza/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      884 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/trasparenza/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     3351 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/trasparenza/get.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.975620 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/types/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/types/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      404 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/types/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)    10630 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/types/get.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.976246 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/types/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/types/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     3804 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/types/adapters.py
+-rw-r--r--   0 roman      (502) staff       (20)      394 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/types/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     1628 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/schema_overrides.py
+-rw-r--r--   0 roman      (502) staff       (20)     2315 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/setuphandlers.py
+-rw-r--r--   0 roman      (502) staff       (20)     4341 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/testing.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.983357 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)    11218 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/example.pdf
+-rw-r--r--   0 roman      (502) staff       (20)     1997 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_argomenti.py
+-rw-r--r--   0 roman      (502) staff       (20)     2330 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_base_serializer.py
+-rw-r--r--   0 roman      (502) staff       (20)     1564 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_descrizione_estesa.py
+-rw-r--r--   0 roman      (502) staff       (20)     3169 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_luogo.py
+-rw-r--r--   0 roman      (502) staff       (20)     2563 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_show_modified.py
+-rw-r--r--   0 roman      (502) staff       (20)     1755 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_update_note.py
+-rw-r--r--   0 roman      (502) staff       (20)     1893 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_change_news_type.py
+-rw-r--r--   0 roman      (502) staff       (20)     1679 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_bando.py
+-rw-r--r--   0 roman      (502) staff       (20)     1462 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_cartella_modulistica.py
+-rw-r--r--   0 roman      (502) staff       (20)     1342 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_document.py
+-rw-r--r--   0 roman      (502) staff       (20)     6365 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_documento.py
+-rw-r--r--   0 roman      (502) staff       (20)     1294 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_documento_personale.py
+-rw-r--r--   0 roman      (502) staff       (20)     4924 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_event.py
+-rw-r--r--   0 roman      (502) staff       (20)     7744 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_luogo.py
+-rw-r--r--   0 roman      (502) staff       (20)      982 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_modulo.py
+-rw-r--r--   0 roman      (502) staff       (20)     8019 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_news.py
+-rw-r--r--   0 roman      (502) staff       (20)     1296 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_pagina_argomento.py
+-rw-r--r--   0 roman      (502) staff       (20)     5271 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_persona.py
+-rw-r--r--   0 roman      (502) staff       (20)    11188 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)    10788 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_unita_organizzativa.py
+-rw-r--r--   0 roman      (502) staff       (20)     2164 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_filefield_view_mode_serializer.py
+-rw-r--r--   0 roman      (502) staff       (20)     2526 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_move_news_items_view.py
+-rw-r--r--   0 roman      (502) staff       (20)     6638 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_relateditems_with_dates.py
+-rw-r--r--   0 roman      (502) staff       (20)     2063 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_service_prenotazioni_folders_list.py
+-rw-r--r--   0 roman      (502) staff       (20)     1381 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_settings_controlpanel_api.py
+-rw-r--r--   0 roman      (502) staff       (20)     3533 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_setup.py
+-rw-r--r--   0 roman      (502) staff       (20)    11257 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_summary_serializer.py
+-rw-r--r--   0 roman      (502) staff       (20)     1234 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_uo_summary_serializer.py
+-rw-r--r--   0 roman      (502) staff       (20)     6351 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_vocabularies.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.984723 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)    21651 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     5033 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/draftjs_converter.py
+-rw-r--r--   0 roman      (502) staff       (20)    11792 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/to_7001.py
+-rw-r--r--   0 roman      (502) staff       (20)     5975 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/to_7002.py
+-rw-r--r--   0 roman      (502) staff       (20)    48753 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/upgrades.py
+-rw-r--r--   0 roman      (502) staff       (20)      862 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/utils.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.986999 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     1308 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/argomenti_vocabulary.py
+-rw-r--r--   0 roman      (502) staff       (20)     1573 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/available_services_vocabulary.py
+-rw-r--r--   0 roman      (502) staff       (20)     1824 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     1466 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/controlapanel_vocabularies.py
+-rw-r--r--   0 roman      (502) staff       (20)     1895 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/lista_azioni_pratica.py
+-rw-r--r--   0 roman      (502) staff       (20)     1704 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/mockup.py
+-rw-r--r--   0 roman      (502) staff       (20)     2223 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/people_vocabulary.py
+-rw-r--r--   0 roman      (502) staff       (20)     1533 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/reference_vocabularies.py
+-rw-r--r--   0 roman      (502) staff       (20)     5199 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/tags_vocabulary.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 12:56:11.919214 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/
+-rw-r--r--   0 roman      (502) staff       (20)    42597 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/PKG-INFO
+-rw-r--r--   0 roman      (502) staff       (20)    18661 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/SOURCES.txt
+-rw-r--r--   0 roman      (502) staff       (20)        1 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/dependency_links.txt
+-rw-r--r--   0 roman      (502) staff       (20)      150 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/entry_points.txt
+-rw-r--r--   0 roman      (502) staff       (20)       20 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/namespace_packages.txt
+-rw-r--r--   0 roman      (502) staff       (20)        1 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/not-zip-safe
+-rw-r--r--   0 roman      (502) staff       (20)      470 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/requires.txt
+-rw-r--r--   0 roman      (502) staff       (20)        7 2023-04-06 12:56:11.000000 design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/top_level.txt
```

### Comparing `design.plone.contenttypes-6.0.0a9/CHANGES.rst` & `design.plone.contenttypes-6.0.1/CHANGES.rst`

 * *Files 11% similar despite different names*

```diff
@@ -1,11 +1,134 @@
 Changelog
 =========
 
 
+6.0.1 (2023-04-06)
+------------------
+
+- Fix None type itereation attempt in relation field adapter
+  [foxtrot-dfm1]
+- Add serializer/deserializer for canale_digitale_link to handle internal/external links like remoteURL field.
+  [cekk]
+- Force canale_digitale_link return `url` widget in Servizio schema.
+  [cekk]
+- Do not purge allowed_content_types filter for Servizio.
+  [cekk]
+
+- Fix patch/post validations for required fields: do not return errors when sorting items.
+  [cekk]
+- Add "Atto di nomina" link in incarico summary serializer
+  [lucabel]
+
+6.0.0 (2023-03-23)
+------------------
+- improve upgrade step
+  [lucabel]
+
+6.0.0a22 (2023-03-07)
+---------------------
+
+- timeline_tempi_scadenze non più obbligatorio
+  [pnicolli]
+
+
+6.0.0a21 (2023-03-01)
+---------------------
+
+- Better handle default language in upgrade-step
+  [cekk]
+
+
+6.0.0a20 (2023-02-27)
+---------------------
+
+- Add a new upgrade step to rename "multimedia" in "immagini"
+  under an event and add the new "video" folder.
+  [lucabel]
+
+
+6.0.0a19 (2023-02-27)
+---------------------
+
+- Change event schema: "patrocinato da"  right now is a
+  rich text
+  [lucabel]
+
+
+6.0.0a18 (2023-02-22)
+---------------------
+
+- First release of check_service view; need to test on
+  a staging
+  [lucabel]
+
+
+6.0.0a17 (2023-02-20)
+---------------------
+
+- Start implement a view to check service for new data
+  [lucabel]
+- Improved check for taxonomy data.
+  [sabrina-bongiovanni]
+
+
+6.0.0a16 (2023-02-08)
+---------------------
+
+- Improved github action for automatic deploy.
+- Fixed tipologia_notizia in serializer.
+  [eikichi18]
+
+
+6.0.0a15 (2023-02-08)
+---------------------
+
+- Fixed tipologia_notizia in serializer.
+  [eikichi18]
+
+
+6.0.0a14 (2023-02-08)
+---------------------
+
+- Fixed design_italia_meta_type data in summary for News Item.
+  [eikichi18]
+
+
+6.0.0a13 (2023-02-06)
+---------------------
+
+- Fix field description
+  Fix bug with taxonomies for old contenttypes
+  Change field fieldset
+  [lucabel]
+
+
+6.0.0a12 (2023-02-06)
+---------------------
+
+- Cambiato descrizione tempi e scadenze
+  [lucabel]
+
+
+6.0.0a11 (2023-02-03)
+---------------------
+
+- Fix upgrade step.
+
+
+6.0.0a10 (2023-02-03)
+---------------------
+
+- Update some tickets to show or hide fields
+  in Servizo and UO.
+  Fix problems with taxonomies
+  upgrade steps to clean catalog
+  [lucabel]
+
+
 6.0.0a9 (2023-02-02)
 --------------------
 - New view 'change_news_type'
   [foxtrot-dfm1]
 -  New view 'move_news_items'
   [foxtrot-dfm1]
 
@@ -73,14 +196,56 @@
 --------------------
 
 - Remove collective.dexteritytextindexer dependency (it's in core).
   [cekk]
 - Adjustments to the pnrr.
   [deodorhunter, lucabel, eikichi18]
 
+5.1.7 (unreleased)
+------------------
+
+- Optional integration with redturtle.prenotazioni
+  [foxtrot-dfm1]
+- Update upgrade step after some more use case [lucabel]
+
+5.1.6 (2023-03-16)
+------------------
+
+- Enable plone.excludefromnavigation for Venue ct.
+  [cekk]
+
+
+5.1.5 (2023-02-15)
+------------------
+
+- @modulistica-items honors the currently logged-in user roles to access inactive contents (expired and not yet published).
+  [cekk]
+
+
+5.1.4 (2023-02-07)
+------------------
+
+- Fix lables.
+  [foxtrot-dfm1]
+
+5.1.3 (2023-02-06)
+------------------
+
+- Fix label of CartellaModulisitica visualize_files field.
+  [foxtrot-dfm1]
+
+
+5.1.2 (2023-02-06)
+------------------
+
+- All the file fields download link view method of child contents depends
+  on the CartellaModulistica c.t. visualize_files field.
+  [foxtrot-dfm1]
+
+
 5.1.1 (2023-01-18)
 ------------------
 
 - New view 'change_news_type'.
   [foxtrot-dfm1]
 - New view 'move_news_items'.
   [foxtrot-dfm1]
```

### Comparing `design.plone.contenttypes-6.0.0a9/DEVELOP.rst` & `design.plone.contenttypes-6.0.1/DEVELOP.rst`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/LICENSE.GPL` & `design.plone.contenttypes-6.0.1/LICENSE.GPL`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/LICENSE.rst` & `design.plone.contenttypes-6.0.1/LICENSE.rst`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/README.md` & `design.plone.contenttypes-6.0.1/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,20 @@
+[![Latest Version](https://img.shields.io/pypi/v/design.plone.contenttypes.svg)](https://pypi.python.org/pypi/design.plone.contenttypes/)
+[![Supported - Python Versions](https://img.shields.io/pypi/pyversions/design.plone.contenttypes.svg?style=plastic)](https://pypi.python.org/pypi/design.plone.contenttypes/)
+[![Number of PyPI downloads](https://img.shields.io/pypi/dm/design.plone.contenttypes.svg)](https://pypi.python.org/pypi/design.plone.contenttypes/)
+[![License](https://img.shields.io/pypi/l/design.plone.contenttypes.svg)](https://pypi.python.org/pypi/design.plone.contenttypes/)
+[![Tests](https://github.com/RedTurtle/design.plone.contenttypes/actions/workflows/test.yml/badge.svg)](https://github.com/RedTurtle/design.plone.contenttypes/actions)
+[![Coverage](https://coveralls.io/repos/github/RedTurtle/design.plone.contenttypes/badge.svg?branch=main)](https://coveralls.io/github/RedTurtle/design.plone.contenttypes?branch=main)
+
 <!-- START doctoc generated TOC please keep comment here to allow auto update -->
 <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
 
 - [Design Plone Content-types](#design-plone-content-types)
 - [Features](#features)
+- [Compatibilità](#compatibilit%C3%A0)
 - [Tipi di contenuto](#tipi-di-contenuto)
   - [Elenco tipi implementati](#elenco-tipi-implementati)
   - [Bando](#bando)
   - [Cartella Modulistica](#cartella-modulistica)
   - [Documento](#documento)
     - [Campi indicizzati nel SearchableText](#campi-indicizzati-nel-searchabletext)
     - [Evento di creazione](#evento-di-creazione)
@@ -18,15 +26,15 @@
     - [Evento di modifica](#evento-di-modifica)
     - [Campi indicizzati nel SearchableText](#campi-indicizzati-nel-searchabletext-1)
   - [Persona](#persona)
     - [Evento di creazione](#evento-di-creazione-1)
     - [Campi indicizzati nel SearchableText](#campi-indicizzati-nel-searchabletext-2)
   - [Servizio](#servizio)
     - [Campi indicizzati nel SearchableText](#campi-indicizzati-nel-searchabletext-3)
-  - [Unità Organizzativa](#unità-organizzativa)
+  - [Unità Organizzativa](#unit%C3%A0-organizzativa)
     - [Campi indicizzati nel SearchableText](#campi-indicizzati-nel-searchabletext-4)
 - [Pannello di controllo](#pannello-di-controllo)
 - [Gestione modulistica](#gestione-modulistica)
 - [Data di modifica](#data-di-modifica)
 - [Endpoint restapi](#endpoint-restapi)
   - [Customizzazione dati relation field](#customizzazione-dati-relation-field)
   - [Serializer summary](#serializer-summary)
@@ -43,14 +51,20 @@
 Pacchetto per la gestione dei content-type per un sito Agid con Plone.
 
 # Features
 
 Installando questo pacchetto, si rendono disponibili diversi content-type per la
 gestione di un sito Agid con Plone e Volto.
 
+
+# Compatibilità
+
+- Plone 6.0, design.plone.policy 5.*, design.plone.contenttypes 6.*
+- Plone 5.2, design.plone.policy 4.*, design.plone.contenttypes 5.*
+
 # Tipi di contenuto
 
 ## Elenco tipi implementati
 
 - [x] **Cartella Modulistica**
 
   - [x] Definizione campi
```

### Comparing `design.plone.contenttypes-6.0.0a9/docs/conf.py` & `design.plone.contenttypes-6.0.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/setup.py` & `design.plone.contenttypes-6.0.1/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -12,15 +12,15 @@
         open("CHANGES.rst").read(),
     ]
 )
 
 
 setup(
     name="design.plone.contenttypes",
-    version="6.0.0a9",
+    version="6.0.1",
     description="DesignItalia contenty types",
     long_description=long_description,
     long_description_content_type="text/markdown",
     # Get more from https://pypi.org/classifiers/
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Environment :: Web Environment",
@@ -36,16 +36,16 @@
     ],
     keywords="Python Plone",
     author="RedTurtle",
     author_email="sviluppoplone@redturtle.it",
     url="https://github.com/collective/design.plone.contenttypes",
     project_urls={
         "PyPI": "https://pypi.python.org/pypi/design.plone.contenttypes",
-        "Source": "https://github.com/collective/design.plone.contenttypes",
-        "Tracker": "https://github.com/collective/design.plone.contenttypes/issues",
+        "Source": "https://github.com/RedTurtle/design.plone.contenttypes",
+        "Tracker": "https://github.com/RedTurtle/design.plone.contenttypes/issues",
     },
     license="GPL version 2",
     packages=find_packages("src", exclude=["ez_setup"]),
     namespace_packages=["design", "design.plone"],
     package_dir={"": "src"},
     include_package_data=True,
     zip_safe=False,
@@ -56,15 +56,15 @@
         "z3c.jbot",
         "plone.api>=1.8.4",
         "plone.app.dexterity>2.6.9",
         "collective.venue[geolocation]",
         "collective.volto.blocksfield",
         "collective.z3cform.datagridfield",
         "plone.formwidget.geolocation",
-        "redturtle.volto",
+        "redturtle.volto>=5.0.0",
         "redturtle.bandi",
         "z3c.unconfigure",
         "eea.api.taxonomy",
     ],
     extras_require={
         "test": [
             "plone.app.testing",
@@ -72,15 +72,19 @@
             # Remove if your package shall be part of coredev.
             # plone_coredev tests as of 2016-04-01.
             "collective.volto.blocksfield",
             "plone.testing>=5.0.0",
             "plone.app.contenttypes",
             "plone.app.robotframework[debug]",
             "collective.MockMailHost",
-        ]
+            "redturtle.prenotazioni",
+        ],
+        "ioprenoto": [
+            "redturtle.prenotazioni",
+        ],
     },
     entry_points="""
     [z3c.autoinclude.plugin]
     target = plone
     [console_scripts]
     update_locale = design.plone.contenttypes.locales.update:update_locale
     """,
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/__init__.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/__init__.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/adapters/searchabletext_indexers.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/adapters/searchabletext_indexers.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/additional_help_infos.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/additional_help_infos.py`

 * *Files 8% similar despite different names*

```diff
@@ -10,15 +10,14 @@
 from zope.interface import provider
 
 
 # TODO: valutare se aggiungere 'box_aiuto', in alcuni CT e' obbligatorio
 # e bisognerebbe metterlo unifrme per tutti in barba alle linee guida
 @provider(IFormFieldProvider)
 class IAdditionalHelpInfos(model.Schema):
-
     ulteriori_informazioni = BlocksField(
         title=_("ulteriori_informazioni", default="Ulteriori informazioni"),
         description=_(
             "ulteriori_informazioni_help",
             default="Ulteriori informazioni non contemplate" " dai campi precedenti.",
         ),
         required=False,
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/address.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/address.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,10 @@
 # -*- coding: utf-8 -*-
 from collective.address.behaviors import IAddress
 from design.plone.contenttypes import _
-from design.plone.contenttypes.interfaces.unita_organizzativa import IUnitaOrganizzativa
 from plone.app.dexterity import textindexer
 from plone.autoform.interfaces import IFormFieldProvider
 from plone.dexterity.interfaces import IDexterityContent
 from plone.supermodel import model
 from zope import schema
 from zope.component import adapter
 from zope.interface import implementer
@@ -42,32 +41,14 @@
 
     # searchabletext indexer
     textindexer.searchable("quartiere")
     textindexer.searchable("circoscrizione")
 
 
 @provider(IFormFieldProvider)
-class IAddressUnitaOrganizzativa(IAddress, IAddressNomeSede, IAddressLocal):
-
-    model.fieldset(
-        "contatti",
-        label=_("contatti_label", default="Contatti"),
-        fields=[
-            "nome_sede",
-            "street",
-            "zip_code",
-            "city",
-            "quartiere",
-            "circoscrizione",
-            "country",
-        ],
-    )
-
-
-@provider(IFormFieldProvider)
 class IAddressVenue(IAddress, IAddressLocal):
     """"""
 
     model.fieldset(
         "dove",
         label=_("dove_label", default="Dove"),
         fields=[
@@ -96,23 +77,14 @@
             "quartiere",
             "circoscrizione",
             "country",
         ],
     )
 
 
-@implementer(IAddressUnitaOrganizzativa)
-@adapter(IUnitaOrganizzativa)
-class AddressUnitaOrganizzativa(object):
-    """ """
-
-    def __init__(self, context):
-        self.context = context
-
-
 @implementer(IAddressVenue)
 @adapter(IDexterityContent)
 class AddressVenue(object):
     """ """
 
     def __init__(self, context):
         self.context = context
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/argomenti.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/argomenti.py`

 * *Files 6% similar despite different names*

```diff
@@ -95,14 +95,35 @@
             title=_("Argomenti correlati"),
             vocabulary="plone.app.vocabularies.Catalog",
         ),
         required=True,
         default=[],
     )
 
+    correlato_in_evidenza = RelationList(
+        title=_("correlato_in_evidenza_label", default="Correlato in evidenza"),
+        description=_(
+            "correlato_in_evidenza_help",
+            default="Seleziona un correlato da mettere in evidenza per questo"
+            " contenuto.",
+        ),
+        value_type=RelationChoice(
+            title=_("Correlato in evidenza"),
+            vocabulary="plone.app.vocabularies.Catalog",
+        ),
+        required=False,
+        default=[],
+    )
+
+    model.fieldset(
+        "correlati",
+        label=_("correlati_label", default="Contenuti collegati"),
+        fields=["correlato_in_evidenza"],
+    )
+
 
 @provider(IFormFieldProvider)
 class IArgomentiEvento(IArgomentiSchema):
     """ """
 
     tassonomia_argomenti = RelationList(
         title=_("tassonomia_argomenti_label", default="Argomenti"),
@@ -118,15 +139,14 @@
         required=True,
         default=[],
     )
 
 
 @provider(IFormFieldProvider)
 class IArgomentiServizio(IArgomentiSchema):
-
     tassonomia_argomenti = RelationList(
         title=_("tassonomia_argomenti_label", default="Argomenti"),
         description=_(
             "tassonomia_argomenti_help",
             default="Seleziona una lista di argomenti d'interesse per questo"
             " contenuto.",
         ),
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/configure.zcml`

 * *Files 2% similar despite different names*

```diff
@@ -192,22 +192,14 @@
       description=""
       factory=".info_testata.InfoTestata"
       provides=".info_testata.IInfoTestata"
       for="plone.dexterity.interfaces.IDexterityContent"
       marker=".info_testata.IInfoTestata"
       />
   <plone:behavior
-      name="design.plone.contenttypes.behavior.address_uo"
-      title="Address UO"
-      description="Behavior address per UO."
-      factory=".address.AddressUnitaOrganizzativa"
-      provides=".address.IAddressUnitaOrganizzativa"
-      marker=".address.IAddressUnitaOrganizzativa"
-      />
-  <plone:behavior
       name="design.plone.contenttypes.behavior.address_venue"
       title="Address Venue"
       description="Behavior address per Venue."
       factory=".address.AddressVenue"
       provides=".address.IAddressVenue"
       marker=".address.IAddressVenue"
       />
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/contatti.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/contatti.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,13 +1,15 @@
 # -*- coding: utf-8 -*-
 from collective.venue.interfaces import IVenue
+from collective.volto.blocksfield.field import BlocksField
 from design.plone.contenttypes import _
 from design.plone.contenttypes.interfaces.persona import IPersona
 from design.plone.contenttypes.interfaces.servizio import IServizio
 from design.plone.contenttypes.interfaces.unita_organizzativa import IUnitaOrganizzativa
+from plone.app.dexterity import textindexer
 from plone.app.z3cform.widget import RelatedItemsFieldWidget
 from plone.autoform import directives as form
 from plone.autoform.interfaces import IFormFieldProvider
 from plone.supermodel import model
 from z3c.relationfield.schema import RelationChoice
 from z3c.relationfield.schema import RelationList
 from zope.component import adapter
@@ -29,29 +31,40 @@
         required=True,
         default=[],
         value_type=RelationChoice(
             title=_("Informazioni di contatto"),
             vocabulary="plone.app.vocabularies.Catalog",
         ),
     )
+    orario_pubblico = BlocksField(
+        title=_("orario_pubblico_label", default="Orario per il pubblico"),
+        description=_(
+            "orario_pubblico_help",
+            default="Indicare eventuali orari di accesso al pubblico",
+        ),
+        required=False,
+    )
+
     form.widget(
         "contact_info",
         RelatedItemsFieldWidget,
         vocabulary="plone.app.vocabularies.Catalog",
         pattern_options={
             "maximumSelectionSize": 10,
             "selectableTypes": ["PuntoDiContatto"],
         },
     )
     model.fieldset(
         "contatti",
         label=_("contatti_label", default="Contatti"),
-        fields=["contact_info"],
+        fields=["contact_info", "orario_pubblico"],
     )
 
+    textindexer.searchable("orario_pubblico")
+
 
 @provider(IFormFieldProvider)
 class IContattiPersona(model.Schema):
     contact_info = RelationList(
         title=_(
             "contact_info_label",
             default="Punti di contatto",
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/dataset_correlati.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/dataset_correlati.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,15 +11,14 @@
 from zope.interface import implementer
 from zope.interface import provider
 
 
 # TODO: merge with NEWS
 @provider(IFormFieldProvider)
 class IDatasetCorrelati(model.Schema):
-
     dataset_correlati = RelationList(
         title=_("dataset_correlati_label", default="Dataset correlati"),
         description=_(
             "dataset_correlati_help",
             default="Seleziona una lista di schede dataset collegate a questo"
             " contenuto.",
         ),
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/descrizione_estesa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/descrizione_estesa.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/evento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/evento.py`

 * *Files 5% similar despite different names*

```diff
@@ -34,19 +34,19 @@
         description=_(
             "descrizione_estesa_help",
             default="Descrizione dettagliata e completa.",
         ),
     )
 
     descrizione_destinatari = BlocksField(
-        title=_("descrizione_destinatari", default="Descrizione destinatari"),
-        required=False,
+        title=_("a_chi_si_rivolge_label", default="A chi è rivolto"),
+        required=True,
         description=_(
-            "descrizione_destinatari_help",
-            default="Descrizione dei principali interlocutori dell'evento.",
+            "a_chi_si_rivolge_help",
+            default="Descrizione testuale dei principali destinatari dell'Evento",
         ),
     )
 
     orari = BlocksField(
         title=_("orari", default="Informazioni sugli orari"),
         required=False,
         description=_(
@@ -96,16 +96,16 @@
         value_type=RelationChoice(vocabulary="plone.app.vocabularies.Catalog"),
         description=_(
             "supportato_da_help",
             default="Indicare gli uffici/enti che supportano l'evento.",
         ),
     )
 
-    # campi aggiunti con il pnrr
-    patrocinato_da = schema.TextLine(
+    #  campi aggiunti con il pnrr
+    patrocinato_da = BlocksField(
         title=_("patrocinato_da_label", default="Patrocinato da"),
         required=False,
         description=_(
             "patrocinato_da_help",
             default="Indicare l'ente che supporta l'evento, se presente.",
         ),
     )
@@ -117,23 +117,14 @@
         value_type=RelationChoice(vocabulary="plone.app.vocabularies.Catalog"),
         description=_(
             "parteciperanno_help",
             default="Link a persone dell'amministrazione che interverranno all'evento",
         ),
     )
 
-    a_chi_si_rivolge = BlocksField(
-        title=_("a_chi_si_rivolge_label", default="A chi è rivolto"),
-        required=True,
-        description=_(
-            "a_chi_si_rivolge_help",
-            default="Descrizione testuale dei principali destinatari dell'Evento",
-        ),
-    )
-
     # custom widgets
     form.widget(
         "supportato_da",
         RelatedItemsFieldWidget,
         vocabulary="plone.app.vocabularies.Catalog",
         pattern_options={
             "maximumSelectionSize": 10,
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/geolocation.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/geolocation.py`

 * *Files 2% similar despite different names*

```diff
@@ -9,33 +9,30 @@
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import provider
 
 
 @provider(IFormFieldProvider)
 class IGeolocatableUnitaOrganizzativa(IGeolocatable):
-
     model.fieldset(
         "contatti",
         label=_("contatti_label", default="Contatti"),
         fields=["geolocation"],
     )
 
 
 @provider(IFormFieldProvider)
 class IGeolocatableVenue(IGeolocatable):
-
     model.fieldset(
         "dove", label=_("dove_label", default="Dove"), fields=["geolocation"]
     )
 
 
 @provider(IFormFieldProvider)
 class IGeolocatableEvent(IGeolocatable):
-
     model.fieldset(
         "luogo",
         label=_("luogo_label", default="Luogo"),
         fields=["geolocation"],
     )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/info_testata.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/info_testata.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/luoghi_correlati.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/luoghi_correlati.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,14 @@
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import provider
 
 
 # TODO: merge with NEWS
 class ILuoghiCorrelatiSchema(model.Schema):
-
     luoghi_correlati = RelationList(
         title=_("luoghi_correlati_label", default="Luoghi correlati"),
         description=_(
             "luoghi_correlati_help",
             default="Seleziona una lista di luoghi citati.",
         ),
         default=[],
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/luogo.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/luogo.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/multi_file.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/multi_file.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/news_additional_fields.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/news_additional_fields.py`

 * *Files 3% similar despite different names*

```diff
@@ -114,15 +114,19 @@
         RelatedItemsFieldWidget,
         vocabulary="plone.app.vocabularies.Catalog",
         pattern_options={
             "selectableTypes": ["Venue"],
             "maximumSelectionSize": 50,
         },
     )
-
+    model.fieldset(
+        "correlati",
+        label=_("correlati_label", default="Contenuti collegati"),
+        fields=["notizie_correlate"],
+    )
     # custom fieldsets and order
     form.order_before(descrizione_estesa="ILeadImageBehavior.image")
     form.order_before(numero_progressivo_cs="ILeadImageBehavior.image")
     form.order_before(a_cura_di="ILeadImageBehavior.image")
 
     textindexer.searchable("descrizione_estesa")
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/servizi_correlati.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/servizi_correlati.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,15 +11,14 @@
 from zope.interface import implementer
 from zope.interface import provider
 
 
 # TODO: merge with NEWS
 @provider(IFormFieldProvider)
 class IServiziCorrelati(model.Schema):
-
     servizi_correlati = RelationList(
         title=_("servizi_correlati_label", default="Servizi correlati"),
         description=_(
             "servizi_correlati_description",
             default="Questi servizi non verranno mostrati nel contenuto, ma"
             " permetteranno di vedere questo contenuto associato quando si"
             " visita il servizio",
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/show_modified.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/show_modified.py`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,14 @@
     return api.portal.get_registry_record(
         "show_modified_default", interface=IDesignPloneSettings, default=False
     )
 
 
 @provider(IFormFieldProvider)
 class IShowModified(model.Schema):
-
     show_modified = schema.Bool(
         title=_("show_modified_label", default="Mostra la data di ultima modifica"),
         description=_(
             "show_modified_help",
             default="Se attivo, verrà mostrata la data di ultima modifica in "
             "visualizzazione del contenuto.",
         ),
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/strutture_correlate.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/strutture_correlate.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,14 @@
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import provider
 
 
 @provider(IFormFieldProvider)
 class IStruttureCorrelate(model.Schema):
-
     strutture_politiche = RelationList(
         title="Strutture politiche coinvolte",
         default=[],
         value_type=RelationChoice(
             title=_("Struttura politica coinvolta"),
             vocabulary="plone.app.vocabularies.Catalog",
         ),
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/trasparenza.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/trasparenza.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/behaviors/update_note.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/behaviors/update_note.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/change_news_type.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/change_news_type.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,17 +1,20 @@
+# -*- coding: utf-8 -*-
 from Acquisition import aq_base
 from collective.taxonomy.interfaces import ITaxonomy
 from copy import deepcopy
 from design.plone.contenttypes import _
 from logging import getLogger
 from plone import api
 from Products.Five.browser import BrowserView
 from zope.component import getUtility
 from zope.interface.interfaces import ComponentLookupError
 
+import json
+
 
 logger = getLogger(__name__)
 
 
 class View(BrowserView):
     """This view is needed to change the news type on the existent content"""
 
@@ -79,14 +82,16 @@
         for brain in api.portal.get_tool("portal_catalog")():
             item = aq_base(brain.getObject())
 
             if getattr(item, "blocks", {}):
                 blocks = deepcopy(item.blocks)
 
                 if blocks:
+                    if isinstance(blocks, str):
+                        blocks = json.loads(blocks)
                     for block in blocks.values():
                         if block.get("@type", "") == "listing":
                             for query in block.get("querystring", {}).get("query", []):
                                 if query["i"] == "tipologia_notizia":
                                     new_values = []
                                     for v in query["v"]:
                                         if v == old_news_type:
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/check_servizi.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/cartella_modulistica.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,88 +1,55 @@
-from design.plone.contenttypes import _
-from plone import api
-from plone.z3cform.layout import wrap_form
-from z3c.form import button
-from z3c.form import field
-from z3c.form import form
-from zope import schema
+# -*- coding: utf-8 -*-
+from .related_news_serializer import SerializeFolderToJson as RelatedNewsSerializer
+from Acquisition import aq_inner
+from design.plone.contenttypes.interfaces.cartella_modulistica import (
+    ICartellaModulistica,
+)
+from plone.restapi.interfaces import ISerializeToJson
+from plone.restapi.interfaces import ISerializeToJsonSummary
+from zc.relation.interfaces import ICatalog
+from zope.component import adapter
 from zope.component import getMultiAdapter
+from zope.component import getUtility
+from zope.globalrequest import getRequest
 from zope.interface import implementer
 from zope.interface import Interface
+from zope.intid.interfaces import IIntIds
+from zope.security import checkPermission
 
 
-class ISearchForm(Interface):
-    """
-    Form to search Servizio by path
-    """
-
-    path = schema.TextLine(
-        title=_(
-            "licenza_distribuzione_label",
-            default="Seleziona il percorso sotto il quale cercare",
-        ),
-        required=False,
-    )
-
-
-@implementer(ISearchForm)
-class CheckServizi(form.Form):
-
-    ignoreContext = True
-    # template = ViewPageTemplateFile("templates/check_servizi.pt")
-    prefix = ""
-    brains = []
-    fields = field.Fields(ISearchForm)
-    method = "GET"
-
-    def search_servizi(self):
-        pc = api.portal.get_tool("portal_catalog")
-        query = {"portal_type": "Servizio", "sort_on": "sortable_title"}
-        if self.request.form.get("widgets.path") and self.request.form.get(
-            "buttons.action_search"
-        ):
-            path = self.request.form.get("widgets.path")
-            prefix = api.portal.get().getId()
-            if not path.startswith(f"/{prefix}"):
-                path = f"/{prefix}/{path}"
-            query["path"] = {"query": path}
-        brains = pc(**query)
-        servizi = [brain.getObject() for brain in brains]
-        results = []
-        for servizio in servizi:
-            results.append(
-                {
-                    "title": servizio.title,
-                    "url": "/".join(servizio.getPhysicalPath()),
-                    "breadcrumbs": getMultiAdapter(
-                        (servizio, self.request), name="breadcrumbs_view"
-                    ).breadcrumbs(),
-                }
+@implementer(ISerializeToJson)
+@adapter(ICartellaModulistica, Interface)
+class CartellaModulisticaSerializer(RelatedNewsSerializer):
+    def get_services(self):
+        """ """
+        catalog = getUtility(ICatalog)
+        intids = getUtility(IIntIds)
+        services = []
+        for attr in ["altri_documenti"]:
+            relations = catalog.findRelations(
+                dict(
+                    to_id=intids.getId(aq_inner(self.context)),
+                    from_attribute=attr,
+                )
             )
-        return results
-
-    def updateWidgets(self):
-        super(CheckServizi, self).updateWidgets()
-        for k, v in self.request.form.items():
-            if k in self.widgets:
-                self.widgets[k].value = v
-
-    @button.buttonAndHandler(_("action_search", default="Cerca"))
-    def action_search(self, action):
-        """
-        Search in prenotazioni SearchableText
-        """
-        data, errors = self.extractData()
-        if errors:
-            self.status = self.formErrorsMessage
-            return
-
-    @button.buttonAndHandler(_("move_back_message", default="Reset"))
-    def action_cancel(self, action):
-        """
-        Cancel and go back to the week view
-        """
-        target = self.context.absolute_url() + "/check_servizi"
-        return self.request.response.redirect(target)
-
 
-WrappedCheckServiziForm = wrap_form(CheckServizi)
+            for rel in relations:
+                obj = intids.queryObject(rel.from_id)
+                if (
+                    obj is not None
+                    and checkPermission("zope2.View", obj)  # noqa
+                    and obj.portal_type == "Servizio"  # noqa
+                ):
+                    summary = getMultiAdapter(
+                        (obj, getRequest()), ISerializeToJsonSummary
+                    )()
+                    services.append(summary)
+        return sorted(services, key=lambda k: k["title"])
+
+    def __call__(self, version=None, include_items=True):
+        self.index = "news_uo"
+        result = super(CartellaModulisticaSerializer, self).__call__(
+            version=version, include_items=include_items
+        )
+        result["servizi_collegati"] = self.get_services()
+        return result
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/configure.zcml`

 * *Files 22% similar despite different names*

```diff
@@ -16,9 +16,16 @@
   <browser:page
       name="move_news_items"
       for="*"
       class=".move_news_items.View"
       template="templates/move_news_items.pt"
       permission="cmf.ManagePortal"
       />
+  <browser:page
+      name="check_servizi"
+      for="*"
+      class=".check_servizi.CheckServizi"
+      template="templates/check_servizi.pt"
+      permission="zope2.Public"
+      />
 
 </configure>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/move_news_items.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/move_news_items.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+# -*- coding: utf-8 -*-
 from collective.taxonomy.interfaces import ITaxonomy
 from design.plone.contenttypes import _
 from plone import api
 from plone.memoize import ram
 from Products.Five import BrowserView
 from zope.component import getUtility
 from zope.interface.interfaces import ComponentLookupError
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/templates/change_news_type.pt` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/templates/change_news_type.pt`

 * *Files 12% similar despite different names*

```diff
@@ -1,54 +1,87 @@
-<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
-      xmlns:tal="http://xml.zope.org/namespaces/tal"
-      xmlns:metal="http://xml.zope.org/namespaces/metal"
+<html xmlns="http://www.w3.org/1999/xhtml"
       xmlns:i18n="http://xml.zope.org/namespaces/i18n"
+      xmlns:metal="http://xml.zope.org/namespaces/metal"
+      xmlns:tal="http://xml.zope.org/namespaces/tal"
       lang="en"
       metal:use-macro="here/main_template/macros/master"
-      i18n:domain="design.plone.contenttypes">
+      xml:lang="en"
+      i18n:domain="design.plone.contenttypes"
+>
 
-<body>
+  <body>
     <metal:content-title fill-slot="content-title">
-        <h1 i18n:translate="">Change News Type</h1>
+      <h1 i18n:translate="">Change News Type</h1>
     </metal:content-title>
-    <metal:content-description fill-slot="content-description" i18n:translate="">
+    <metal:content-description fill-slot="content-description"
+                               i18n:translate=""
+    >
       Questo tool viene usato per cambiare il valore del campo 'Tipologia Notizia' in tutte le notizie che hanno il valore del campo selezionato.
       Fa anche il giro su tutti i blocchi elenco
     </metal:content-description>
     <metal:content-core fill-slot="content-core">
-       <div class="form">
-            <form action="${context/portal_url}/change_news_type" method="POST">
-                <div class="field">
-                    <label for="news_type_in_catalog" i18n:translate="">News Type</label>
-                    <div class="formHelp" i18n:translate="">
+      <div class="form">
+        <form action="${context/portal_url}/change_news_type"
+              method="POST"
+        >
+          <div class="field">
+            <label for="news_type_in_catalog"
+                   i18n:translate=""
+            >News Type</label>
+            <div class="formHelp"
+                 i18n:translate=""
+            >
                         All the already existing News Types
-                    </div>
-                    <select name="news_type_in_catalog" tal:define="news_types python: view.news_types_in_catalog()">
-                      <option tal:repeat="news_type_in_catalog news_types"
-                              tal:content="news_type_in_catalog"
-                              tal:attributes="selected python: request.form.get('news_type_in_catalog', '') == news_type_in_catalog; value news_type_in_catalog"/>
-                    </select><br>
-                    <label for="news_type_portal" style="margin-top: 1em;" i18n:translate="">News Type to substitute</label>
-                    <div class="formHelp" i18n:translate="">
+            </div>
+            <select name="news_type_in_catalog"
+                    tal:define="
+                      news_types python: view.news_types_in_catalog();
+                    "
+            >
+              <option tal:repeat="news_type_in_catalog news_types"
+                      tal:content="news_type_in_catalog"
+                      tal:attributes="
+                        selected python: request.form.get('news_type_in_catalog', '') == news_type_in_catalog;
+                        value news_type_in_catalog;
+                      "
+              ></option>
+            </select><br />
+            <label for="news_type_portal"
+                   style="margin-top: 1em;"
+                   i18n:translate=""
+            >News Type to substitute</label>
+            <div class="formHelp"
+                 i18n:translate=""
+            >
                        The News Type selected above will be substituted by the selected value
-                    </div>
-                    <select name="news_type_portal" tal:define="news_types python: view.news_types()">
-                      <tal tal:repeat="news_type_portal news_types">
-                        <option tal:condition="python: news_type_portal.value"
-                                tal:content="news_type_portal/title"
-                                tal:attributes="selected python: request.form.get('news_type_portal', '') == news_type_portal.value; value news_type_portal/value"/>
-                      </tal>
-                    </select>
-                </div>
-                <div class="formControls">
-                    <button id="substitute"
-                           name="substitute"
-                           value="true"
-                           class="submit-widget button-field context"
-                           type="submit" i18n:translate="">Substitute</button>
-                </div>
-            </form>
-        </div>
+            </div>
+            <select name="news_type_portal"
+                    tal:define="
+                      news_types python: view.news_types();
+                    "
+            >
+              <tal tal:repeat="news_type_portal news_types">
+                <option tal:condition="python: news_type_portal.value"
+                        tal:content="news_type_portal/title"
+                        tal:attributes="
+                          selected python: request.form.get('news_type_portal', '') == news_type_portal.value;
+                          value news_type_portal/value;
+                        "
+                ></option>
+              </tal>
+            </select>
+          </div>
+          <div class="formControls">
+            <button class="submit-widget button-field context"
+                    id="substitute"
+                    name="substitute"
+                    type="submit"
+                    value="true"
+                    i18n:translate=""
+            >Substitute</button>
+          </div>
+        </form>
+      </div>
     </metal:content-core>
-</body>
+  </body>
 
 </html>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/manage_content/templates/move_news_items.pt` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/manage_content/templates/move_news_items.pt`

 * *Files 20% similar despite different names*

```diff
@@ -1,83 +1,138 @@
-<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
-      xmlns:tal="http://xml.zope.org/namespaces/tal"
-      xmlns:metal="http://xml.zope.org/namespaces/metal"
+<html xmlns="http://www.w3.org/1999/xhtml"
       xmlns:i18n="http://xml.zope.org/namespaces/i18n"
+      xmlns:metal="http://xml.zope.org/namespaces/metal"
+      xmlns:tal="http://xml.zope.org/namespaces/tal"
       lang="en"
       metal:use-macro="here/main_template/macros/master"
-      i18n:domain="design.plone.contenttypes">
+      xml:lang="en"
+      i18n:domain="design.plone.contenttypes"
+>
 
-<body>
+  <body>
     <metal:content-title fill-slot="content-title">
-        <h1 i18n:translate="">Move News Items</h1>
+      <h1 i18n:translate="">Move News Items</h1>
     </metal:content-title>
-    <metal:content-description fill-slot="content-description" i18n:translate="">
+    <metal:content-description fill-slot="content-description"
+                               i18n:translate=""
+    >
       Questo tool viene usato per trovare e spostare le Notizie con una Tipologia Notizia determinata.
     </metal:content-description>
     <metal:content-core fill-slot="content-core">
-       <div class="form">
-            <form action="${context/portal_url}/move_news_items" method="POST">
-                <div class="field">
-                    <label for="news_type" i18n:translate="">News Type</label>
-                    <div class="formHelp" i18n:translate="">
+      <div class="form">
+        <form action="${context/portal_url}/move_news_items"
+              method="POST"
+        >
+          <div class="field">
+            <label for="news_type"
+                   i18n:translate=""
+            >News Type</label>
+            <div class="formHelp"
+                 i18n:translate=""
+            >
                         Find news with this News Type
-                    </div>
-                    <select name="news_type" tal:define="news_types view/news_types">
-                      <option tal:repeat="news_type news_types" tal:content="news_type/title" tal:attributes="selected python: request.form.get('news_type', '') == news_type.value; value news_type/value"/>
-                    </select><br>
-		    <label for="news_type" style="margin-top: 2em;" i18n:translate="">Search Path</label>
-                    <div class="formHelp" i18n:translate="" >
+            </div>
+            <select name="news_type"
+                    tal:define="
+                      news_types view/news_types;
+                    "
+            >
+              <option tal:repeat="news_type news_types"
+                      tal:content="news_type/title"
+                      tal:attributes="
+                        selected python: request.form.get('news_type', '') == news_type.value;
+                        value news_type/value;
+                      "
+              ></option>
+            </select><br />
+            <label for="news_type"
+                   style="margin-top: 2em;"
+                   i18n:translate=""
+            >Search Path</label>
+            <div class="formHelp"
+                 i18n:translate=""
+            >
                       Find news with the indicated Path, put attention than generaly sites have the root name "/Plone/"
-                    </div>
-                    <input type="text" name="path" tal:attributes="value python: view.request.form.get('path', '')">
+            </div>
+            <input name="path"
+                   type="text"
+                   tal:attributes="
+                     value python: view.request.form.get('path', '');
+                   "
+            />
+          </div>
+          <div class="formControls">
+            <input class="submit-widget button-field context"
+                   id="search"
+                   name="search"
+                   type="submit"
+                   value="Search"
+            />
+          </div>
+        </form>
+      </div>
+      <div class="form"
+           tal:define="
+             results python:view.news_results();
+             tot_results python: results and len(results) or 0;
+           "
+           tal:condition="results"
+      >
+        <form action="${context/portal_url}/move_news_items"
+              method="POST"
+        >
+          <div>
+            <h2>Found ${tot_results} items</h2>
+            <ul style="list-style-type: none;">
+              <li>
+                <div class="field">
+                  <input id="select_all"
+                         type="checkbox"
+                  />
+                  <h4 style="display: inline">Select all</h4>
                 </div>
-                <div class="formControls">
-                    <input id="search"
-                           name="search"
-                           class="submit-widget button-field context"
-                           value="Search"
-                           type="submit">
+              </li>
+              <li tal:repeat="item results">
+                <div class="field">
+                  <input type="checkbox"
+                         tal:attributes="
+                           name item/UID;
+                         "
+                  />
+                  <a href="${item/getURL}"
+                     tal:content="item/Title"
+                  ></a><br />
+                  <p><span i18n:translate="">Contained by</span>
+                    ${python: '/'.join(item.getPath().split('/')[:-1])}</p>
                 </div>
-            </form>
-        </div>
-        <div class="form" tal:define="results python:view.news_results();tot_results python: results and len(results) or 0" tal:condition="results">
-          <form action="${context/portal_url}/move_news_items" method="POST" >
-            <div>
-                <h2>Found ${tot_results} items</h2>
-                <ul style="list-style-type: none;">
-                    <li>
-                      <div class="field">
-                        <input id="select_all" type="checkbox"/>
-                        <h4 style="display: inline">Select all</h4>
-                      </div>
-                      </li>
-                    <li tal:repeat="item results">
-                        <div class="field">
-                            <input type="checkbox" tal:attributes="name item/UID">
-                            <a href="${item/getURL}" tal:content="item/Title"></a><br>
-                            <p><span i18n:translate="">Contained by</span> ${python: '/'.join(item.getPath().split('/')[:-1])}</p>
-                        </div>
-                    </li>
-                </ul>
-              <div class="field">
-                <label for="to_url" i18n:translate="">Move to Path</label>
-		<div class="formHelp" i18n:translate="">
+              </li>
+            </ul>
+            <div class="field">
+              <label for="to_url"
+                     i18n:translate=""
+              >Move to Path</label>
+              <div class="formHelp"
+                   i18n:translate=""
+              >
                   All the selected items will be moved to indicated path
-                 </div>
-                <input type="text" name="to_path"/>
               </div>
+              <input name="to_path"
+                     type="text"
+              />
             </div>
-            <div class="formControls">
-              <button id="move"
-                     name="move"
-                     class="submit-widget button-field context"
-                     type="submit"
-                     value="move"
-                     i18n:translate="">Move</button>
-            </div>
-          </form>
-        </div>
+          </div>
+          <div class="formControls">
+            <button class="submit-widget button-field context"
+                    id="move"
+                    name="move"
+                    type="submit"
+                    value="move"
+                    i18n:translate=""
+            >Move</button>
+          </div>
+        </form>
+      </div>
       <script src="${view/get_resource_js}"></script>
     </metal:content-core>
-</body>
+  </body>
 
 </html>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/browser/overrides/plone.app.contenttypes.browser.templates.newsitem.pt` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/browser/overrides/plone.app.contenttypes.browser.templates.newsitem.pt`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/configure.zcml`

 * *Files 7% similar despite different names*

```diff
@@ -4,19 +4,14 @@
     xmlns:i18n="http://namespaces.zope.org/i18n"
     xmlns:plone="http://namespaces.plone.org/plone"
     i18n_domain="design.plone.contenttypes"
     >
 
   <i18n:registerTranslations directory="locales" />
 
-  <!--
-    Be careful if you use general includeDependencies, it can have sideffects!
-    Better import explicite packages or configurations ;)
-  -->
-  <!-- <includeDependencies package="." /> -->
   <include package="plone.app.caching" />
 
   <include file="permissions.zcml" />
   <include package=".adapters" />
   <include package=".behaviors" />
   <include package=".browser" />
   <include package=".controlpanels" />
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/geolocation_defaults.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/geolocation_defaults.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/controlpanels/settings.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/controlpanels/settings.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/bando.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/bando.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/configure.zcml`

 * *Files 7% similar despite different names*

```diff
@@ -1,9 +1,11 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
+    xmlns:plone="http://namespaces.zope.org/plone"
+    xmlns:zcml="http://namespaces.zope.org/zcml"
     i18n_domain="design.plone.contenttypes"
     >
 
   <subscriber
       for="design.plone.contenttypes.interfaces.pratica.IPratica
            zope.lifecycleevent.interfaces.IObjectAddedEvent"
       handler=".pratica.praticaCreateHandler"
@@ -71,9 +73,17 @@
   <!-- common -->
   <subscriber
       for="plone.dexterity.interfaces.IDexterityContent
            zope.lifecycleevent.interfaces.IObjectModifiedEvent"
       handler=".common.onModify"
       />
 
+  <configure zcml:condition="installed redturtle.prenotazioni">
+    <subscriber
+        for="design.plone.contenttypes.interfaces.servizio.IServizio
+             zope.lifecycleevent.interfaces.IObjectAddedEvent"
+        handler=".servizio.prenotazioni_folder_create"
+        />
+  </configure>
+
 
 </configure>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/document.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/document.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/documento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/documento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/evento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/evento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/incarico.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/incarico.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/luogo.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/luogo.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/notizie_e_comunicati_stampa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/notizie_e_comunicati_stampa.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/pagina_argomento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/pagina_argomento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/persona.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/persona.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/pratica.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/pratica.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/events/unita_organizzativa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/events/unita_organizzativa.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/common.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/common.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/news.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/news.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/pagina_argomento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/pagina_argomento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/persona.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/persona.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/indexers/punto_di_contatto.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/indexers/punto_di_contatto.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/bando.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/bando.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/dataset.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/dataset.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/documento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/documento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/documento_personale.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/documento_personale.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/incarico.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/incarico.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/messaggio.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/messaggio.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/pagina_argomento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/pagina_argomento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/persona.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/persona.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/pratica.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/pratica.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/punto_di_contatto.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/punto_di_contatto.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/ricevuta_pagamento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/ricevuta_pagamento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/servizio.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/servizio.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,66 +3,55 @@
 from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
 from collective.z3cform.datagridfield.row import DictRow
 from design.plone.contenttypes import _
 from design.plone.contenttypes.interfaces import IDesignPloneContentType
 from plone.app.dexterity import textindexer
 from plone.app.z3cform.widget import DateFieldWidget
 from plone.app.z3cform.widget import RelatedItemsFieldWidget
+from plone.app.z3cform.widget import LinkFieldWidget
 from plone.autoform import directives as form
 from plone.namedfile import field
 from plone.supermodel import model
 from z3c.relationfield.schema import RelationChoice
 from z3c.relationfield.schema import RelationList
 from zope import schema
 
 
 class ITempiEScadenzeValueSchema(model.Schema):
-    data_scadenza = schema.Date(
-        title=_("data_scadenza_label", default="Data scadenza"),
-        description=_(
-            "data_scadenza_help",
-            default="Data di scadenza della fase",
-        ),
-        required=False,
-    )
     milestone = schema.TextLine(
         title=_("milestone_label", default="Titolo"),
-        description=_(
-            "milestone_help",
-            default="Titolo della fase",
-        ),
-        required=True,
+        required=False,
+        default="",
+    )
+    milestone_description = schema.TextLine(
+        title=_("milestone_description_label", default="Sottotitolo"),
+        required=False,
         default="",
     )
     interval_qt = schema.TextLine(
         title=_("interval_qt_label", default="Intervallo"),
         description=_(
             "interval_qt_help",
-            default="Intervallo della fase",
+            default="Intervallo della fase (es. 1)",
         ),
         required=False,
         default="",
     )
     interval_type = schema.TextLine(
         title=_("interval_type_label", default="Tipo intervallo"),
         description=_(
             "interval_type_help",
             default="Ad esempio: " "ore, giorni, settimane, mesi.",
         ),
         required=False,
         default="",
     )
-    milestone_description = schema.TextLine(
-        title=_("milestone_description_label", default="Sottotitolo"),
-        description=_(
-            "milestone_description_help",
-            default="Sottotitolo della fase",
-        ),
+    data_scadenza = schema.Date(
+        title=_("data_scadenza_label", default="Data scadenza"),
         required=False,
-        default="",
     )
 
     form.widget(
         "data_scadenza",
         DateFieldWidget,
     )
 
@@ -168,15 +157,15 @@
         description=_(
             "canale_digitale_help",
             default="Testo di introduzione del canale digitale",
         ),
         required=False,
     )
 
-    canale_digitale_link = schema.URI(
+    canale_digitale_link = schema.TextLine(
         title=_("canale_digitale_link", default="Link al canale digitale"),
         description=_(
             "canale_digitale_link_help",
             default="Collegamento con l'eventuale canale digitale di"
             " attivazione del servizio.",
         ),
         required=False,
@@ -192,23 +181,24 @@
         default=[],
         value_type=RelationChoice(
             title=_("Canale fisico"),
             vocabulary="plone.app.vocabularies.Catalog",
         ),
     )
 
-    autenticazione = BlocksField(
-        title=_("autenticazione", default="Autenticazione"),
-        description=_(
-            "autenticazione_help",
-            default="Indicare, se previste, le modalità di autenticazione"
-            " necessarie per poter accedere al servizio.",
-        ),
-        required=False,
-    )
+    # US38344 rimuovere
+    # autenticazione = BlocksField(
+    #     title=_("autenticazione", default="Autenticazione"),
+    #     description=_(
+    #         "autenticazione_help",
+    #         default="Indicare, se previste, le modalità di autenticazione"
+    #         " necessarie per poter accedere al servizio.",
+    #     ),
+    #     required=False,
+    # )
 
     dove_rivolgersi = RelationList(
         title="Dove rivolgersi",
         default=[],
         value_type=RelationChoice(vocabulary="plone.app.vocabularies.Catalog"),
         required=False,
         description=_(
@@ -255,17 +245,20 @@
     timeline_tempi_scadenze = schema.List(
         title=_("timeline_tempi_scadenze", default="Timeline tempi e scadenze"),
         default=[],
         value_type=DictRow(schema=ITempiEScadenzeValueSchema),
         description=_(
             "timeline_tempi_scadenze_help",
             default="Timeline tempi e scadenze del servizio: indicare per ogni "
-            "scadenza un titolo descritttivo di tale scadenza e, opzionalmente,"
-            " informazioni sulle date o gli intervalli di tempo che "
-            "intercorrono tra una fase e la successiva.",
+            "scadenza un titolo descrittivo ed un eventuale sottotitolo. "
+            "Per ogni scadenza, selezionare opzionalmente o l'intervallo (Campi"
+            ' "Intervallo" e "Tipo Intervallo", es. "1" e "settimana"),'
+            ' oppure direttamente una data di scadenza (campo: "Data Scadenza"'
+            ", esempio 31/12/2023). "
+            'Se vengono compilati entrambi, ha priorità il campo "Data Scadenza".',
         ),
         required=False,
     )
 
     cosa_serve = BlocksField(
         title=_("cosa_serve", default="Cosa serve"),
         required=True,
@@ -469,14 +462,15 @@
         },
     )
     form.widget(
         "timeline_tempi_scadenze",
         DataGridFieldFactory,
         frontendOptions={"widget": "data_grid"},
     )
+    form.widget("canale_digitale_link", LinkFieldWidget)
 
     # custom fieldset and order
     model.fieldset(
         "a_chi_si_rivolge",
         label=_("a_chi_si_rivolge_label", default="A chi si rivolge"),
         fields=["a_chi_si_rivolge", "chi_puo_presentare", "copertura_geografica"],
     )
@@ -487,15 +481,15 @@
         fields=[
             "come_si_fa",
             "cosa_si_ottiene",
             "procedure_collegate",
             "canale_digitale",
             "canale_digitale_link",
             "canale_fisico",
-            "autenticazione",
+            # "autenticazione",
             "dove_rivolgersi",
             "dove_rivolgersi_extra",
             "prenota_appuntamento",
         ],
     )
     model.fieldset(
         "cosa_serve",
@@ -540,17 +534,19 @@
         "correlati",
         label=_("correlati_label", default="Contenuti collegati"),
         fields=["servizi_collegati"],
     )
 
     model.fieldset(
         "categorization",
-        fields=["codice_ipa", "settore_merceologico", "identificativo"],
+        fields=["identificativo"],
     )
 
+    model.fieldset("informazioni", fields=["codice_ipa", "settore_merceologico"])
+
     # SearchableText fields
     textindexer.searchable("sottotitolo")
     textindexer.searchable("a_chi_si_rivolge")
     textindexer.searchable("chi_puo_presentare")
     textindexer.searchable("come_si_fa")
     textindexer.searchable("cosa_si_ottiene")
     textindexer.searchable("cosa_serve")
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/interfaces/unita_organizzativa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/interfaces/unita_organizzativa.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/README.rst` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/README.rst`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/__pycache__/LC_MESSAGES/design.plone.contenttypes.po` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/__pycache__/LC_MESSAGES/design.plone.contenttypes.po`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/design.plone.contenttypes.pot` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/design.plone.contenttypes.pot`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/en/LC_MESSAGES/design.plone.contenttypes.po` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/en/LC_MESSAGES/design.plone.contenttypes.po`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/LC_MESSAGES/collective.geolocationbehavior.po` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/LC_MESSAGES/collective.geolocationbehavior.po`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/LC_MESSAGES/design.plone.contenttypes.po` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/LC_MESSAGES/design.plone.contenttypes.po`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/it/LC_MESSAGES/plone.po` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/it/LC_MESSAGES/plone.po`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/update.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/update.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/locales/update.sh` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/locales/update.sh`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/overrides.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/overrides.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/patches/__init__.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/patches/__init__.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/patches/baseserializer.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/patches/baseserializer.py`

 * *Files 18% similar despite different names*

```diff
@@ -6,46 +6,51 @@
    information, we need to override SerializeFolderToJson copying the whole
    code otherwise it will use the code from original SerializeToJson due to
    inheritance
  * Using a monkey patch is the easiest way to include future changes on base
    SerializeToJson and SerializeFolderToJson classes
 """
 
+from collective.taxonomy import PATH_SEPARATOR
+from collective.taxonomy.interfaces import ITaxonomy
 from plone import api
 from plone.restapi.batching import HypermediaBatch
 from plone.restapi.deserializer import boolean_value
 from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from plone.restapi.serializer.dxcontent import SerializeFolderToJson
 from plone.restapi.serializer.dxcontent import SerializeToJson
 from Products.CMFCore.utils import getToolByName
 from zope.component import getMultiAdapter
+from zope.component import getUtility
 from zope.i18n import translate
 
 
 original_serialize_to_json__call__ = SerializeToJson.__call__
 
 
 def design_italia_serialize_to_json_call(self, version=None, include_items=True):
     ttool = api.portal.get_tool("portal_types")
     result = original_serialize_to_json__call__(
         self, version=version, include_items=include_items
     )
+    result["design_italia_meta_type"] = translate(
+        ttool[self.context.portal_type].Title(), context=self.request
+    )
     if self.context.portal_type == "News Item":
-        try:
-            tipologia_news = self.context.tipologia_notizia
-        except AttributeError:
-            # fallback if we don't have c.taxonomy configured yet
-            tipologia_news = self.context.tipologia_notizia
-        result["design_italia_meta_type"] = tipologia_news
-    else:
-        result["design_italia_meta_type"] = translate(
-            ttool[self.context.portal_type].Title(), context=self.request
-        )
+        if self.context.tipologia_notizia:
+            taxonomy = getUtility(
+                ITaxonomy, name="collective.taxonomy.tipologia_notizia"
+            )
+            taxonomy_voc = taxonomy.makeVocabulary(self.request.get("LANGUAGE"))
+
+            title = taxonomy_voc.inv_data.get(self.context.tipologia_notizia, None)
 
+            if title and title.startswith(PATH_SEPARATOR):
+                result["design_italia_meta_type"] = title.replace(PATH_SEPARATOR, "", 1)
     return result
 
 
 def patch_base_serializer():
     SerializeToJson.__call__ = design_italia_serialize_to_json_call
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/permissions.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/permissions.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/business_events.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/business_events.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/person_life_events.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/person_life_events.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/temi_dataset.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/temi_dataset.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documenti_albopretorio.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documenti_albopretorio.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.xml`

 * *Files 0% similar despite different names*

#### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_documento.xml`

```diff
@@ -33,15 +33,15 @@
     <caption>
       <langstring language="it">Accordo tra enti</langstring>
     </caption>
   </term>
   <term>
     <termIdentifier>documento_attivita_politica</termIdentifier>
     <caption>
-      <langstring language="it">Documento attivita politica</langstring>
+      <langstring language="it">Documento attività politica</langstring>
     </caption>
   </term>
   <term>
     <termIdentifier>documento_tecnico_di_supporto</termIdentifier>
     <caption>
       <langstring language="it">Documento (tecnico) di supporto</langstring>
     </caption>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_evento.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_evento.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_frequenza_aggiornamento.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_frequenza_aggiornamento.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_incarico.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_incarico.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_licenze.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_licenze.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_luogo.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_luogo.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.xml`

 * *Files 1% similar despite different names*

#### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_notizia.xml`

```diff
@@ -15,12 +15,11 @@
     <caption>
       <langstring language="it">Comunicato (stampa)</langstring>
     </caption>
   </term>
   <term>
     <termIdentifier>avviso</termIdentifier>
     <caption>
-      <langstring language="en"/>
       <langstring language="it">Avviso</langstring>
     </caption>
   </term>
 </vdex>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_organizzazione.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_organizzazione.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_pdc.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_pdc.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_stati_pratica.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/behaviors/taxonomies/tipologia_stati_pratica.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/catalog.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/catalog.xml`

 * *Format-specific differences are supported for XML files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: XML 1.0 document, ASCII text*

 * *Files 0% similar despite different names*

```diff
@@ -66,103 +66,103 @@
 00000410: 5f75 6964 222f 3e0a 203c 2f69 6e64 6578  _uid"/>. </index
 00000420: 3e0a 203c 696e 6465 7820 6e61 6d65 3d22  >. <index name="
 00000430: 7469 706f 6c6f 6769 615f 646f 6375 6d65  tipologia_docume
 00000440: 6e74 6f22 206d 6574 615f 7479 7065 3d22  nto" meta_type="
 00000450: 4b65 7977 6f72 6449 6e64 6578 223e 0a20  KeywordIndex">. 
 00000460: 203c 696e 6465 7865 645f 6174 7472 2076   <indexed_attr v
 00000470: 616c 7565 3d22 7469 706f 6c6f 6769 615f  alue="tipologia_
-00000480: 646f 6375 6d65 6e74 6f22 2f3e 200a 203c  documento"/> . <
-00000490: 2f69 6e64 6578 3e0a 203c 696e 6465 7820  /index>. <index 
-000004a0: 6e61 6d65 3d22 7566 6669 6369 6f5f 7265  name="ufficio_re
-000004b0: 7370 6f6e 7361 6269 6c65 2220 6d65 7461  sponsabile" meta
-000004c0: 5f74 7970 653d 224b 6579 776f 7264 496e  _type="KeywordIn
-000004d0: 6465 7822 3e0a 2020 3c69 6e64 6578 6564  dex">.  <indexed
-000004e0: 5f61 7474 7220 7661 6c75 653d 2275 6666  _attr value="uff
-000004f0: 6963 696f 5f72 6573 706f 6e73 6162 696c  icio_responsabil
-00000500: 6522 2f3e 0a20 3c2f 696e 6465 783e 0a20  e"/>. </index>. 
-00000510: 3c69 6e64 6578 206e 616d 653d 2275 6666  <index name="uff
-00000520: 6963 696f 5f72 6573 706f 6e73 6162 696c  icio_responsabil
-00000530: 655f 6261 6e64 6f22 206d 6574 615f 7479  e_bando" meta_ty
-00000540: 7065 3d22 4b65 7977 6f72 6449 6e64 6578  pe="KeywordIndex
-00000550: 223e 0a20 203c 696e 6465 7865 645f 6174  ">.  <indexed_at
-00000560: 7472 2076 616c 7565 3d22 7566 6669 6369  tr value="uffici
-00000570: 6f5f 7265 7370 6f6e 7361 6269 6c65 5f62  o_responsabile_b
-00000580: 616e 646f 222f 3e0a 203c 2f69 6e64 6578  ando"/>. </index
-00000590: 3e0a 203c 696e 6465 7820 6e61 6d65 3d22  >. <index name="
-000005a0: 5375 626a 6563 745f 6261 6e64 6f22 206d  Subject_bando" m
-000005b0: 6574 615f 7479 7065 3d22 4b65 7977 6f72  eta_type="Keywor
-000005c0: 6449 6e64 6578 223e 0a20 203c 696e 6465  dIndex">.  <inde
-000005d0: 7865 645f 6174 7472 2076 616c 7565 3d22  xed_attr value="
-000005e0: 5375 626a 6563 745f 6261 6e64 6f22 2f3e  Subject_bando"/>
-000005f0: 0a20 3c2f 696e 6465 783e 0a20 3c69 6e64  . </index>. <ind
-00000600: 6578 206e 616d 653d 2265 7665 6e74 5f6c  ex name="event_l
-00000610: 6f63 6174 696f 6e22 206d 6574 615f 7479  ocation" meta_ty
-00000620: 7065 3d22 4b65 7977 6f72 6449 6e64 6578  pe="KeywordIndex
-00000630: 223e 0a20 203c 696e 6465 7865 645f 6174  ">.  <indexed_at
-00000640: 7472 2076 616c 7565 3d22 6576 656e 745f  tr value="event_
-00000650: 6c6f 6361 7469 6f6e 222f 3e0a 203c 2f69  location"/>. </i
-00000660: 6e64 6578 3e0a 203c 696e 6465 7820 6e61  ndex>. <index na
-00000670: 6d65 3d22 7469 706f 6c6f 6769 615f 6f72  me="tipologia_or
-00000680: 6761 6e69 7a7a 617a 696f 6e65 2220 6d65  ganizzazione" me
-00000690: 7461 5f74 7970 653d 224b 6579 776f 7264  ta_type="Keyword
-000006a0: 496e 6465 7822 3e0a 2020 3c69 6e64 6578  Index">.  <index
-000006b0: 6564 5f61 7474 7220 7661 6c75 653d 2274  ed_attr value="t
-000006c0: 6970 6f6c 6f67 6961 5f6f 7267 616e 697a  ipologia_organiz
-000006d0: 7a61 7a69 6f6e 6522 2f3e 0a20 3c2f 696e  zazione"/>. </in
-000006e0: 6465 783e 0a20 3c69 6e64 6578 206e 616d  dex>. <index nam
-000006f0: 653d 2272 756f 6c6f 2220 6d65 7461 5f74  e="ruolo" meta_t
-00000700: 7970 653d 224b 6579 776f 7264 496e 6465  ype="KeywordInde
-00000710: 7822 3e0a 2020 3c69 6e64 6578 6564 5f61  x">.  <indexed_a
-00000720: 7474 7220 7661 6c75 653d 2272 756f 6c6f  ttr value="ruolo
-00000730: 222f 3e0a 203c 2f69 6e64 6578 3e0a 203c  "/>. </index>. <
-00000740: 696e 6465 7820 6e61 6d65 3d22 6461 7461  index name="data
-00000750: 5f63 6f6e 636c 7573 696f 6e65 5f69 6e63  _conclusione_inc
-00000760: 6172 6963 6f22 206d 6574 615f 7479 7065  arico" meta_type
-00000770: 3d22 4461 7465 496e 6465 7822 3e0a 2020  ="DateIndex">.  
-00000780: 3c69 6e64 6578 6564 5f61 7474 7220 7661  <indexed_attr va
-00000790: 6c75 653d 2264 6174 615f 636f 6e63 6c75  lue="data_conclu
-000007a0: 7369 6f6e 655f 696e 6361 7269 636f 222f  sione_incarico"/
-000007b0: 3e0a 203c 2f69 6e64 6578 3e0a 0a20 203c  >. </index>..  <
-000007c0: 212d 2d20 6d65 7461 6461 7461 202d 2d3e  !-- metadata -->
-000007d0: 0a20 203c 636f 6c75 6d6e 2076 616c 7565  .  <column value
-000007e0: 3d22 7469 706f 6c6f 6769 615f 6e6f 7469  ="tipologia_noti
-000007f0: 7a69 6122 202f 3e0a 2020 3c63 6f6c 756d  zia" />.  <colum
-00000800: 6e20 7661 6c75 653d 2274 6970 6f6c 6f67  n value="tipolog
-00000810: 6961 5f64 6f63 756d 656e 746f 2220 2f3e  ia_documento" />
-00000820: 0a20 203c 636f 6c75 6d6e 2076 616c 7565  .  <column value
-00000830: 3d22 7461 7373 6f6e 6f6d 6961 5f61 7267  ="tassonomia_arg
-00000840: 6f6d 656e 7469 2220 2f3e 0a20 203c 636f  omenti" />.  <co
-00000850: 6c75 6d6e 2076 616c 7565 3d22 6576 656e  lumn value="even
-00000860: 745f 6c6f 6361 7469 6f6e 2220 2f3e 0a20  t_location" />. 
-00000870: 203c 636f 6c75 6d6e 2076 616c 7565 3d22   <column value="
-00000880: 5375 626a 6563 745f 6261 6e64 6f22 202f  Subject_bando" /
-00000890: 3e0a 2020 3c63 6f6c 756d 6e20 7661 6c75  >.  <column valu
-000008a0: 653d 2275 6666 6963 696f 5f72 6573 706f  e="ufficio_respo
-000008b0: 6e73 6162 696c 655f 6261 6e64 6f22 202f  nsabile_bando" /
-000008c0: 3e0a 2020 3c63 6f6c 756d 6e20 7661 6c75  >.  <column valu
-000008d0: 653d 2264 6174 615f 636f 6e63 6c75 7369  e="data_conclusi
-000008e0: 6f6e 655f 696e 6361 7269 636f 2220 2f3e  one_incarico" />
-000008f0: 0a20 203c 636f 6c75 6d6e 2076 616c 7565  .  <column value
-00000900: 3d22 7061 7265 6e74 2220 2f3e 0a20 203c  ="parent" />.  <
-00000910: 636f 6c75 6d6e 2076 616c 7565 3d22 656e  column value="en
-00000920: 7465 5f62 616e 646f 2220 2f3e 0a20 203c  te_bando" />.  <
-00000930: 636f 6c75 6d6e 2076 616c 7565 3d22 6963  column value="ic
-00000940: 6f6e 6122 202f 3e0a 2020 3c63 6f6c 756d  ona" />.  <colum
-00000950: 6e20 7661 6c75 653d 2275 7064 6174 655f  n value="update_
-00000960: 6e6f 7465 2220 2f3e 0a0a 2020 3c21 2d2d  note" />..  <!--
-00000970: 2063 6c65 616e 7570 202d 2d3e 0a20 203c   cleanup -->.  <
-00000980: 696e 6465 7820 6e61 6d65 3d22 6172 676f  index name="argo
-00000990: 6d65 6e74 695f 636f 7272 656c 6174 6922  menti_correlati"
-000009a0: 0a20 2020 2020 2020 2020 7265 6d6f 7665  .         remove
-000009b0: 3d22 5472 7565 220a 2020 2f3e 0a20 203c  ="True".  />.  <
-000009c0: 636f 6c75 6d6e 2072 656d 6f76 653d 2254  column remove="T
-000009d0: 7275 6522 0a20 2020 2020 2020 2020 2076  rue".          v
-000009e0: 616c 7565 3d22 6172 676f 6d65 6e74 695f  alue="argomenti_
-000009f0: 636f 7272 656c 6174 6922 0a20 202f 3e0a  correlati".  />.
-00000a00: 2020 3c69 6e64 6578 206e 616d 653d 2261    <index name="a
-00000a10: 7267 6f6d 656e 7469 220a 2020 2020 2020  rgomenti".      
-00000a20: 2020 2072 656d 6f76 653d 2254 7275 6522     remove="True"
-00000a30: 0a20 202f 3e0a 2020 3c63 6f6c 756d 6e20  .  />.  <column 
-00000a40: 7265 6d6f 7665 3d22 5472 7565 220a 2020  remove="True".  
-00000a50: 2020 2020 2020 2020 7661 6c75 653d 2261          value="a
-00000a60: 7267 6f6d 656e 7469 220a 2020 2f3e 0a0a  rgomenti".  />..
-00000a70: 3c2f 6f62 6a65 6374 3e0a                 </object>.
+00000480: 646f 6375 6d65 6e74 6f22 2f3e 0a20 3c2f  documento"/>. </
+00000490: 696e 6465 783e 0a20 3c69 6e64 6578 206e  index>. <index n
+000004a0: 616d 653d 2275 6666 6963 696f 5f72 6573  ame="ufficio_res
+000004b0: 706f 6e73 6162 696c 6522 206d 6574 615f  ponsabile" meta_
+000004c0: 7479 7065 3d22 4b65 7977 6f72 6449 6e64  type="KeywordInd
+000004d0: 6578 223e 0a20 203c 696e 6465 7865 645f  ex">.  <indexed_
+000004e0: 6174 7472 2076 616c 7565 3d22 7566 6669  attr value="uffi
+000004f0: 6369 6f5f 7265 7370 6f6e 7361 6269 6c65  cio_responsabile
+00000500: 222f 3e0a 203c 2f69 6e64 6578 3e0a 203c  "/>. </index>. <
+00000510: 696e 6465 7820 6e61 6d65 3d22 7566 6669  index name="uffi
+00000520: 6369 6f5f 7265 7370 6f6e 7361 6269 6c65  cio_responsabile
+00000530: 5f62 616e 646f 2220 6d65 7461 5f74 7970  _bando" meta_typ
+00000540: 653d 224b 6579 776f 7264 496e 6465 7822  e="KeywordIndex"
+00000550: 3e0a 2020 3c69 6e64 6578 6564 5f61 7474  >.  <indexed_att
+00000560: 7220 7661 6c75 653d 2275 6666 6963 696f  r value="ufficio
+00000570: 5f72 6573 706f 6e73 6162 696c 655f 6261  _responsabile_ba
+00000580: 6e64 6f22 2f3e 0a20 3c2f 696e 6465 783e  ndo"/>. </index>
+00000590: 0a20 3c69 6e64 6578 206e 616d 653d 2253  . <index name="S
+000005a0: 7562 6a65 6374 5f62 616e 646f 2220 6d65  ubject_bando" me
+000005b0: 7461 5f74 7970 653d 224b 6579 776f 7264  ta_type="Keyword
+000005c0: 496e 6465 7822 3e0a 2020 3c69 6e64 6578  Index">.  <index
+000005d0: 6564 5f61 7474 7220 7661 6c75 653d 2253  ed_attr value="S
+000005e0: 7562 6a65 6374 5f62 616e 646f 222f 3e0a  ubject_bando"/>.
+000005f0: 203c 2f69 6e64 6578 3e0a 203c 696e 6465   </index>. <inde
+00000600: 7820 6e61 6d65 3d22 6576 656e 745f 6c6f  x name="event_lo
+00000610: 6361 7469 6f6e 2220 6d65 7461 5f74 7970  cation" meta_typ
+00000620: 653d 224b 6579 776f 7264 496e 6465 7822  e="KeywordIndex"
+00000630: 3e0a 2020 3c69 6e64 6578 6564 5f61 7474  >.  <indexed_att
+00000640: 7220 7661 6c75 653d 2265 7665 6e74 5f6c  r value="event_l
+00000650: 6f63 6174 696f 6e22 2f3e 0a20 3c2f 696e  ocation"/>. </in
+00000660: 6465 783e 0a20 3c69 6e64 6578 206e 616d  dex>. <index nam
+00000670: 653d 2274 6970 6f6c 6f67 6961 5f6f 7267  e="tipologia_org
+00000680: 616e 697a 7a61 7a69 6f6e 6522 206d 6574  anizzazione" met
+00000690: 615f 7479 7065 3d22 4b65 7977 6f72 6449  a_type="KeywordI
+000006a0: 6e64 6578 223e 0a20 203c 696e 6465 7865  ndex">.  <indexe
+000006b0: 645f 6174 7472 2076 616c 7565 3d22 7469  d_attr value="ti
+000006c0: 706f 6c6f 6769 615f 6f72 6761 6e69 7a7a  pologia_organizz
+000006d0: 617a 696f 6e65 222f 3e0a 203c 2f69 6e64  azione"/>. </ind
+000006e0: 6578 3e0a 203c 696e 6465 7820 6e61 6d65  ex>. <index name
+000006f0: 3d22 7275 6f6c 6f22 206d 6574 615f 7479  ="ruolo" meta_ty
+00000700: 7065 3d22 4b65 7977 6f72 6449 6e64 6578  pe="KeywordIndex
+00000710: 223e 0a20 203c 696e 6465 7865 645f 6174  ">.  <indexed_at
+00000720: 7472 2076 616c 7565 3d22 7275 6f6c 6f22  tr value="ruolo"
+00000730: 2f3e 0a20 3c2f 696e 6465 783e 0a20 3c69  />. </index>. <i
+00000740: 6e64 6578 206e 616d 653d 2264 6174 615f  ndex name="data_
+00000750: 636f 6e63 6c75 7369 6f6e 655f 696e 6361  conclusione_inca
+00000760: 7269 636f 2220 6d65 7461 5f74 7970 653d  rico" meta_type=
+00000770: 2244 6174 6549 6e64 6578 223e 0a20 203c  "DateIndex">.  <
+00000780: 696e 6465 7865 645f 6174 7472 2076 616c  indexed_attr val
+00000790: 7565 3d22 6461 7461 5f63 6f6e 636c 7573  ue="data_conclus
+000007a0: 696f 6e65 5f69 6e63 6172 6963 6f22 2f3e  ione_incarico"/>
+000007b0: 0a20 3c2f 696e 6465 783e 0a0a 2020 3c21  . </index>..  <!
+000007c0: 2d2d 206d 6574 6164 6174 6120 2d2d 3e0a  -- metadata -->.
+000007d0: 2020 3c63 6f6c 756d 6e20 7661 6c75 653d    <column value=
+000007e0: 2274 6970 6f6c 6f67 6961 5f6e 6f74 697a  "tipologia_notiz
+000007f0: 6961 2220 2f3e 0a20 203c 636f 6c75 6d6e  ia" />.  <column
+00000800: 2076 616c 7565 3d22 7469 706f 6c6f 6769   value="tipologi
+00000810: 615f 646f 6375 6d65 6e74 6f22 202f 3e0a  a_documento" />.
+00000820: 2020 3c63 6f6c 756d 6e20 7661 6c75 653d    <column value=
+00000830: 2274 6173 736f 6e6f 6d69 615f 6172 676f  "tassonomia_argo
+00000840: 6d65 6e74 6922 202f 3e0a 2020 3c63 6f6c  menti" />.  <col
+00000850: 756d 6e20 7661 6c75 653d 2265 7665 6e74  umn value="event
+00000860: 5f6c 6f63 6174 696f 6e22 202f 3e0a 2020  _location" />.  
+00000870: 3c63 6f6c 756d 6e20 7661 6c75 653d 2253  <column value="S
+00000880: 7562 6a65 6374 5f62 616e 646f 2220 2f3e  ubject_bando" />
+00000890: 0a20 203c 636f 6c75 6d6e 2076 616c 7565  .  <column value
+000008a0: 3d22 7566 6669 6369 6f5f 7265 7370 6f6e  ="ufficio_respon
+000008b0: 7361 6269 6c65 5f62 616e 646f 2220 2f3e  sabile_bando" />
+000008c0: 0a20 203c 636f 6c75 6d6e 2076 616c 7565  .  <column value
+000008d0: 3d22 6461 7461 5f63 6f6e 636c 7573 696f  ="data_conclusio
+000008e0: 6e65 5f69 6e63 6172 6963 6f22 202f 3e0a  ne_incarico" />.
+000008f0: 2020 3c63 6f6c 756d 6e20 7661 6c75 653d    <column value=
+00000900: 2270 6172 656e 7422 202f 3e0a 2020 3c63  "parent" />.  <c
+00000910: 6f6c 756d 6e20 7661 6c75 653d 2265 6e74  olumn value="ent
+00000920: 655f 6261 6e64 6f22 202f 3e0a 2020 3c63  e_bando" />.  <c
+00000930: 6f6c 756d 6e20 7661 6c75 653d 2269 636f  olumn value="ico
+00000940: 6e61 2220 2f3e 0a20 203c 636f 6c75 6d6e  na" />.  <column
+00000950: 2076 616c 7565 3d22 7570 6461 7465 5f6e   value="update_n
+00000960: 6f74 6522 202f 3e0a 0a20 203c 212d 2d20  ote" />..  <!-- 
+00000970: 636c 6561 6e75 7020 2d2d 3e0a 2020 3c69  cleanup -->.  <i
+00000980: 6e64 6578 206e 616d 653d 2261 7267 6f6d  ndex name="argom
+00000990: 656e 7469 5f63 6f72 7265 6c61 7469 220a  enti_correlati".
+000009a0: 2020 2020 2020 2020 2072 656d 6f76 653d           remove=
+000009b0: 2254 7275 6522 0a20 202f 3e0a 2020 3c63  "True".  />.  <c
+000009c0: 6f6c 756d 6e20 7265 6d6f 7665 3d22 5472  olumn remove="Tr
+000009d0: 7565 220a 2020 2020 2020 2020 2020 7661  ue".          va
+000009e0: 6c75 653d 2261 7267 6f6d 656e 7469 5f63  lue="argomenti_c
+000009f0: 6f72 7265 6c61 7469 220a 2020 2f3e 0a20  orrelati".  />. 
+00000a00: 203c 696e 6465 7820 6e61 6d65 3d22 6172   <index name="ar
+00000a10: 676f 6d65 6e74 6922 0a20 2020 2020 2020  gomenti".       
+00000a20: 2020 7265 6d6f 7665 3d22 5472 7565 220a    remove="True".
+00000a30: 2020 2f3e 0a20 203c 636f 6c75 6d6e 2072    />.  <column r
+00000a40: 656d 6f76 653d 2254 7275 6522 0a20 2020  emove="True".   
+00000a50: 2020 2020 2020 2076 616c 7565 3d22 6172         value="ar
+00000a60: 676f 6d65 6e74 6922 0a20 202f 3e0a 0a3c  gomenti".  />..<
+00000a70: 2f6f 626a 6563 743e 0a                   /object>.
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/controlpanel.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/controlpanel.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/diff_tool.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/diff_tool.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/metadata.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/metadata.xml`

 * *Files 0% similar despite different names*

#### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/metadata.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/metadata.xml`

```diff
@@ -1,10 +1,10 @@
 <?xml version="1.0" encoding="utf-8"?>
 <metadata>
-  <version>7003</version>
+  <version>7009</version>
   <dependencies>
     <dependency>profile-redturtle.bandi:default</dependency>
     <dependency>profile-collective.venue:default</dependency>
     <dependency>profile-redturtle.volto:default</dependency>
     <dependency>profile-eea.api.taxonomy:default</dependency>
     <dependency>profile-collective.z3cform.datagridfield:default</dependency>
     <dependency>profile-design.plone.contenttypes:taxonomy</dependency>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/registry/criteria.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/registry/criteria.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/registry/settings.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/registry/settings.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/repositorytool.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/repositorytool.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/rolemap.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/rolemap.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Bando.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Bando.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/CartellaModulistica.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/CartellaModulistica.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Dataset.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Dataset.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Document.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Document.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Documento.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Documento.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Documento_Personale.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Documento_Personale.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Event.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Event.xml`

 * *Files 4% similar despite different names*

#### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Event.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Event.xml`

```diff
@@ -7,15 +7,15 @@
     <element value="Image"/>
     <element value="File"/>
   </property>
   <property name="behaviors" purge="False">
     <element value="plone.eventbasic"/>
     <element value="plone.leadimage"/>
     <element value="volto.preview_image"/>
-    <element remote="True" value="design.plone.contenttypes.behavior.argomenti"/>
+    <element remove="True" value="design.plone.contenttypes.behavior.argomenti"/>
     <element value="design.plone.contenttypes.behavior.argomenti_evento"/>
     <element value="plone.eventrecurrence"/>
     <element value="design.plone.contenttypes.behavior.additional_help_infos"/>
     <element value="design.plone.contenttypes.behavior.evento"/>
     <element value="design.plone.contenttypes.behavior.luoghi_correlati_evento"/>
     <element value="design.plone.contenttypes.behavior.address_event"/>
     <element value="design.plone.contenttypes.behavior.geolocation_event"/>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Incarico.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Incarico.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Messaggio.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Messaggio.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Modulo.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Modulo.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/News_Item.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/News_Item.xml`

 * *Format-specific differences are supported for XML files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: XML 1.0 document, ASCII text*

 * *Files 12% similar despite different names*

```diff
@@ -7,62 +7,57 @@
 00000060: 2020 2020 2020 2020 6d65 7461 5f74 7970          meta_typ
 00000070: 653d 2244 6578 7465 7269 7479 2046 5449  e="Dexterity FTI
 00000080: 220a 2020 2020 2020 2020 6e61 6d65 3d22  ".        name="
 00000090: 4e65 7773 2049 7465 6d22 0a20 2020 2020  News Item".     
 000000a0: 2020 2069 3138 6e3a 646f 6d61 696e 3d22     i18n:domain="
 000000b0: 706c 6f6e 6522 0a3e 0a0a 2020 3c70 726f  plone".>..  <pro
 000000c0: 7065 7274 7920 6e61 6d65 3d22 7469 746c  perty name="titl
-000000d0: 6522 0a20 2020 2020 2020 2020 2020 2069  e".            i
-000000e0: 3138 6e3a 7472 616e 736c 6174 653d 2222  18n:translate=""
-000000f0: 0a20 203e 0a20 204e 6f74 697a 6965 2065  .  >.  Notizie e
-00000100: 2063 6f6d 756e 6963 6174 6920 7374 616d   comunicati stam
-00000110: 7061 0a3c 2f70 726f 7065 7274 793e 0a0a  pa.</property>..
-00000120: 2020 3c70 726f 7065 7274 7920 6e61 6d65    <property name
-00000130: 3d22 616c 6c6f 7765 645f 636f 6e74 656e  ="allowed_conten
-00000140: 745f 7479 7065 7322 0a20 2020 2020 2020  t_types".       
-00000150: 2020 2020 2070 7572 6765 3d22 4661 6c73       purge="Fals
-00000160: 6522 0a20 203e 0a20 2020 203c 656c 656d  e".  >.    <elem
-00000170: 656e 7420 7661 6c75 653d 2244 6f63 756d  ent value="Docum
-00000180: 656e 7422 202f 3e0a 2020 2020 3c65 6c65  ent" />.    <ele
-00000190: 6d65 6e74 2076 616c 7565 3d22 496d 6167  ment value="Imag
-000001a0: 6522 202f 3e0a 2020 2020 3c65 6c65 6d65  e" />.    <eleme
-000001b0: 6e74 2076 616c 7565 3d22 4669 6c65 2220  nt value="File" 
-000001c0: 2f3e 0a20 203c 2f70 726f 7065 7274 793e  />.  </property>
-000001d0: 0a0a 2020 3c70 726f 7065 7274 7920 6e61  ..  <property na
-000001e0: 6d65 3d22 6265 6861 7669 6f72 7322 0a20  me="behaviors". 
-000001f0: 2020 2020 2020 2020 2020 2070 7572 6765             purge
-00000200: 3d22 4661 6c73 6522 0a20 203e 0a20 2020  ="False".  >.   
-00000210: 203c 656c 656d 656e 7420 7661 6c75 653d   <element value=
-00000220: 2276 6f6c 746f 2e70 7265 7669 6577 5f69  "volto.preview_i
-00000230: 6d61 6765 2220 2f3e 0a20 2020 203c 656c  mage" />.    <el
-00000240: 656d 656e 7420 7661 6c75 653d 2264 6573  ement value="des
-00000250: 6967 6e2e 706c 6f6e 652e 636f 6e74 656e  ign.plone.conten
-00000260: 7474 7970 6573 2e62 6568 6176 696f 722e  ttypes.behavior.
-00000270: 6e65 7773 2220 2f3e 0a20 2020 203c 656c  news" />.    <el
-00000280: 656d 656e 7420 7661 6c75 653d 2264 6573  ement value="des
-00000290: 6967 6e2e 706c 6f6e 652e 636f 6e74 656e  ign.plone.conten
-000002a0: 7474 7970 6573 2e62 6568 6176 696f 722e  ttypes.behavior.
-000002b0: 6172 676f 6d65 6e74 695f 6e65 7773 2220  argomenti_news" 
-000002c0: 2f3e 0a20 2020 203c 656c 656d 656e 7420  />.    <element 
-000002d0: 7661 6c75 653d 2270 6c6f 6e65 2e63 6f6e  value="plone.con
-000002e0: 7374 7261 696e 7479 7065 7322 202f 3e0a  straintypes" />.
-000002f0: 2020 2020 3c65 6c65 6d65 6e74 2076 616c      <element val
-00000300: 7565 3d22 706c 6f6e 652e 7465 7874 696e  ue="plone.textin
-00000310: 6465 7865 7222 202f 3e0a 2020 2020 3c65  dexer" />.    <e
-00000320: 6c65 6d65 6e74 2076 616c 7565 3d22 706c  lement value="pl
-00000330: 6f6e 652e 7472 616e 736c 6174 6162 6c65  one.translatable
-00000340: 2220 2f3e 0a20 2020 203c 656c 656d 656e  " />.    <elemen
-00000350: 7420 7661 6c75 653d 226b 6974 636f 6e63  t value="kitconc
-00000360: 6570 742e 7365 6f22 202f 3e0a 2020 2020  ept.seo" />.    
-00000370: 3c65 6c65 6d65 6e74 2076 616c 7565 3d22  <element value="
-00000380: 636f 6c6c 6563 7469 7665 2e74 6178 6f6e  collective.taxon
-00000390: 6f6d 792e 6765 6e65 7261 7465 642e 7469  omy.generated.ti
-000003a0: 706f 6c6f 6769 615f 6e6f 7469 7a69 6122  pologia_notizia"
-000003b0: 202f 3e0a 2020 2020 3c65 6c65 6d65 6e74   />.    <element
-000003c0: 2072 656d 6f76 653d 2254 7275 6522 0a20   remove="True". 
-000003d0: 2020 2020 2020 2020 2020 2020 7661 6c75              valu
-000003e0: 653d 2264 6573 6967 6e2e 706c 6f6e 652e  e="design.plone.
-000003f0: 636f 6e74 656e 7474 7970 6573 2e62 6568  contenttypes.beh
-00000400: 6176 696f 722e 6172 676f 6d65 6e74 6922  avior.argomenti"
-00000410: 0a20 2020 202f 3e0a 2020 3c2f 7072 6f70  .    />.  </prop
-00000420: 6572 7479 3e0a 0a3c 2f6f 626a 6563 743e  erty>..</object>
-00000430: 0a                                       .
+000000d0: 6522 2069 3138 6e3a 7472 616e 736c 6174  e" i18n:translat
+000000e0: 653d 2222 3e4e 6f74 697a 6965 2065 2063  e="">Notizie e c
+000000f0: 6f6d 756e 6963 6174 6920 7374 616d 7061  omunicati stampa
+00000100: 3c2f 7072 6f70 6572 7479 3e0a 0a20 203c  </property>..  <
+00000110: 7072 6f70 6572 7479 206e 616d 653d 2261  property name="a
+00000120: 6c6c 6f77 6564 5f63 6f6e 7465 6e74 5f74  llowed_content_t
+00000130: 7970 6573 2220 7075 7267 653d 2246 616c  ypes" purge="Fal
+00000140: 7365 223e 0a20 2020 203c 656c 656d 656e  se">.    <elemen
+00000150: 7420 7661 6c75 653d 2244 6f63 756d 656e  t value="Documen
+00000160: 7422 202f 3e0a 2020 2020 3c65 6c65 6d65  t" />.    <eleme
+00000170: 6e74 2076 616c 7565 3d22 496d 6167 6522  nt value="Image"
+00000180: 202f 3e0a 2020 2020 3c65 6c65 6d65 6e74   />.    <element
+00000190: 2076 616c 7565 3d22 4669 6c65 2220 2f3e   value="File" />
+000001a0: 0a20 203c 2f70 726f 7065 7274 793e 0a0a  .  </property>..
+000001b0: 2020 3c70 726f 7065 7274 7920 6e61 6d65    <property name
+000001c0: 3d22 6265 6861 7669 6f72 7322 2070 7572  ="behaviors" pur
+000001d0: 6765 3d22 4661 6c73 6522 3e0a 2020 2020  ge="False">.    
+000001e0: 3c65 6c65 6d65 6e74 2076 616c 7565 3d22  <element value="
+000001f0: 766f 6c74 6f2e 7072 6576 6965 775f 696d  volto.preview_im
+00000200: 6167 6522 202f 3e0a 2020 2020 3c65 6c65  age" />.    <ele
+00000210: 6d65 6e74 2076 616c 7565 3d22 6465 7369  ment value="desi
+00000220: 676e 2e70 6c6f 6e65 2e63 6f6e 7465 6e74  gn.plone.content
+00000230: 7479 7065 732e 6265 6861 7669 6f72 2e6e  types.behavior.n
+00000240: 6577 7322 202f 3e0a 2020 2020 3c65 6c65  ews" />.    <ele
+00000250: 6d65 6e74 2076 616c 7565 3d22 6465 7369  ment value="desi
+00000260: 676e 2e70 6c6f 6e65 2e63 6f6e 7465 6e74  gn.plone.content
+00000270: 7479 7065 732e 6265 6861 7669 6f72 2e61  types.behavior.a
+00000280: 7267 6f6d 656e 7469 5f6e 6577 7322 202f  rgomenti_news" /
+00000290: 3e0a 2020 2020 3c65 6c65 6d65 6e74 2076  >.    <element v
+000002a0: 616c 7565 3d22 706c 6f6e 652e 636f 6e73  alue="plone.cons
+000002b0: 7472 6169 6e74 7970 6573 2220 2f3e 0a20  traintypes" />. 
+000002c0: 2020 203c 656c 656d 656e 7420 7661 6c75     <element valu
+000002d0: 653d 2270 6c6f 6e65 2e74 6578 7469 6e64  e="plone.textind
+000002e0: 6578 6572 2220 2f3e 0a20 2020 203c 656c  exer" />.    <el
+000002f0: 656d 656e 7420 7661 6c75 653d 2270 6c6f  ement value="plo
+00000300: 6e65 2e74 7261 6e73 6c61 7461 626c 6522  ne.translatable"
+00000310: 202f 3e0a 2020 2020 3c65 6c65 6d65 6e74   />.    <element
+00000320: 2076 616c 7565 3d22 6b69 7463 6f6e 6365   value="kitconce
+00000330: 7074 2e73 656f 2220 2f3e 0a20 2020 203c  pt.seo" />.    <
+00000340: 656c 656d 656e 7420 7661 6c75 653d 2263  element value="c
+00000350: 6f6c 6c65 6374 6976 652e 7461 786f 6e6f  ollective.taxono
+00000360: 6d79 2e67 656e 6572 6174 6564 2e74 6970  my.generated.tip
+00000370: 6f6c 6f67 6961 5f6e 6f74 697a 6961 2220  ologia_notizia" 
+00000380: 2f3e 0a20 2020 203c 656c 656d 656e 7420  />.    <element 
+00000390: 7265 6d6f 7665 3d22 5472 7565 2220 7661  remove="True" va
+000003a0: 6c75 653d 2264 6573 6967 6e2e 706c 6f6e  lue="design.plon
+000003b0: 652e 636f 6e74 656e 7474 7970 6573 2e62  e.contenttypes.b
+000003c0: 6568 6176 696f 722e 6172 676f 6d65 6e74  ehavior.argoment
+000003d0: 6922 202f 3e0a 2020 3c2f 7072 6f70 6572  i" />.  </proper
+000003e0: 7479 3e0a 0a3c 2f6f 626a 6563 743e 0a    ty>..</object>.
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Pagina_Argomento.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Pagina_Argomento.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Persona.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Persona.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Pratica.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Pratica.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/PuntoDiContatto.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/PuntoDiContatto.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/RicevutaPagamento.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/RicevutaPagamento.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Servizio.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Servizio.xml`

 * *Files 7% similar despite different names*

#### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Servizio.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Servizio.xml`

```diff
@@ -6,19 +6,25 @@
   <property name="allow_discussion">False</property>
   <property name="factory">Servizio</property>
   <property name="icon_expr"/>
   <property name="link_target"/>
   <!-- Hierarchy control -->
   <property name="global_allow">True</property>
   <property name="filter_content_types">True</property>
-  <property name="allowed_content_types">
+  <property name="allowed_content_types" purge="False">
     <element value="CartellaModulistica"/>
     <element value="Document"/>
     <element value="Image"/>
     <element value="File"/>
+    <!-- 
+      * integration btw design.plone.contenttypes and redturtle.prenotazioni
+        TODO: rivalutare se è necessario, o se i folder e i folder delle prenotazioni
+              vanno creati manualmente al di fuori del servizio
+    -->
+    <element value="PrenotazioniFolderContainer"/>
   </property>
   <!-- Schema, class and security -->
   <property name="add_permission">design.plone.contenttypes.AddServizio</property>
   <property name="klass">design.plone.contenttypes.content.servizio.Servizio</property>
   <property name="model_file"/>
   <property name="model_source"/>
   <property name="schema">design.plone.contenttypes.interfaces.servizio.IServizio</property>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/UnitaOrganizzativa.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/UnitaOrganizzativa.xml`

 * *Files 4% similar despite different names*

#### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/UnitaOrganizzativa.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/UnitaOrganizzativa.xml`

```diff
@@ -32,16 +32,16 @@
     <element value="plone.publication"/>
     <element value="plone.categorization"/>
     <element value="plone.basic"/>
     <element value="plone.locking"/>
     <element value="plone.leadimage"/>
     <element value="volto.preview_image"/>
     <element value="plone.relateditems"/>
-    <element value="design.plone.contenttypes.behavior.address_uo"/>
-    <element value="design.plone.contenttypes.behavior.geolocation_uo"/>
+    <element remove="True" value="design.plone.contenttypes.behavior.address_uo"/>
+    <element remove="True" value="design.plone.contenttypes.behavior.geolocation_uo"/>
     <element value="design.plone.contenttypes.behavior.contatti_uo"/>
     <element value="design.plone.contenttypes.behavior.argomenti"/>
     <element value="plone.textindexer"/>
     <element value="design.plone.contenttypes.behavior.additional_help_infos"/>
     <element value="plone.translatable"/>
     <element value="kitconcept.seo"/>
     <element value="plone.versioning"/>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Venue.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Venue.xml`

 * *Files 7% similar despite different names*

#### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types/Venue.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types/Venue.xml`

```diff
@@ -10,14 +10,15 @@
     <element value="File"/>
   </property>
   <property name="behaviors" purge="True">
     <element value="plone.app.content.interfaces.INameFromTitle"/>
     <element value="plone.app.dexterity.behaviors.id.IShortName"/>
     <element value="plone.app.dexterity.behaviors.metadata.IBasic"/>
     <element value="plone.app.dexterity.behaviors.metadata.ICategorization"/>
+    <element value="plone.excludefromnavigation"/>
     <element value="plone.relateditems"/>
     <element value="plone.leadimage"/>
     <element value="volto.preview_image"/>
     <element value="design.plone.contenttypes.behavior.contatti_venue"/>
     <element value="design.plone.contenttypes.behavior.luogo"/>
     <element value="design.plone.contenttypes.behavior.argomenti"/>
     <element value="design.plone.contenttypes.behavior.address_venue"/>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/profiles/default/types.xml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/profiles/default/types.xml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/correlati.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/correlati.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/configure.zcml`

 * *Files 2% similar despite different names*

```diff
@@ -3,13 +3,14 @@
     xmlns:zcml="http://namespaces.zope.org/zcml"
     >
 
   <adapter factory=".persona.DeserializePersonaFromJson" />
   <adapter factory=".servizio.DeserializeServizioFromJson" />
   <adapter factory=".unitaorganizzativa.DeserializeUnitaOrganizzativaFromJson" />
   <adapter factory=".dxfields.GeolocationFieldDeserializer" />
+  <adapter factory=".dxfields.LinkTextLineFieldDeserializer" />
   <adapter factory=".venue.DeserializeLuogoFromJson" />
   <adapter factory=".dxfields.SourceTextDeserializer" />
   <adapter factory=".dxfields.TimelineTempiEScadenzeFieldDeserializer" />
   <adapter factory=".news.DeserializeNewsFromJson" />
   <adapter factory=".documento.DeserializeDocumentoFromJson" />
 </configure>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/documento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/news.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,26 +1,25 @@
 # -*- coding: utf-8 -*-
-from design.plone.contenttypes.interfaces.documento import IDocumento
+from plone.app.contenttypes.interfaces import INewsItem
 from plone.restapi.behaviors import IBlocks
 from plone.restapi.deserializer import json_body
 from plone.restapi.deserializer.dxcontent import DeserializeFromJson
 from plone.restapi.indexers import SearchableText_blocks
 from plone.restapi.interfaces import IDeserializeFromJson
 from zExceptions import BadRequest
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import Interface
 
 
-TITLE_MAX_LEN = 160
-DESCRIPTION_MAX_LEN = 160
+TITLE_MAX_LEN = 255
+DESCRIPTION_MAX_LEN = 255
 EMPTY_BLOCK_MARKER = {"@type": "text"}
 MANDATORY_RICH_TEXT_FIELDS = [
-    # "descrizione_estesa",
-    "formati_disponibili",
+    "descrizione_estesa",
 ]
 
 
 def new_error(message):
     return {"error": "ValidationError", "message": message}
 
 
@@ -45,98 +44,107 @@
         return None
 
     fakeObj = FakeObject(blocks.get("blocks", ""), blocks.get("blocks_layout", ""))
     return SearchableText_blocks(fakeObj)()
 
 
 @implementer(IDeserializeFromJson)
-@adapter(IDocumento, Interface)
-class DeserializeDocumentoFromJson(DeserializeFromJson):
+@adapter(INewsItem, Interface)
+class DeserializeNewsFromJson(DeserializeFromJson):
     def __call__(
         self, validate_all=False, data=None, create=False
     ):  # noqa: ignore=C901
-
         if data is None:
             data = json_body(self.request)
 
         method = self.request.get("method")
         is_post = method == "POST"
         is_patch = method == "PATCH"
         errors = []
 
-        title = data.get("title")
-        description = data.get("description")
-
-        if is_post:
-            # Title validation
-            if not title:
-                errors.append(new_error("Il titolo del servizio è obbligatorio"))
-            elif len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
+        if list(data.keys()) != ["ordering"]:
+            title = data.get("title")
+            description = data.get("description")
+
+            if is_post:
+                # Title validation
+                if not title:
+                    errors.append(new_error("Il titolo è obbligatorio"))
+                elif len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
                         )
                     )
-                )
 
-            # description validation
-            if not description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-            elif len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione del servizio deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
+                # description validation
+                if not description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+                elif len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
                         )
                     )
-                )
 
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field not in data:
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-                elif field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-
-        if is_patch:
-            # Title validation
-            if "title" in data and not title:
-                errors.append(new_error("Il titolo del servizio è obbligatorio"))
-            if title and len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field not in data:
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+                    elif field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+
+            if is_patch:
+                # Title validation
+                if "title" in data and not title:
+                    errors.append(new_error("Il titolo è obbligatorio"))
+                if title and len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
                         )
                     )
-                )
-            # description validation
-            if "description" in data and not description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-            if description and len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione del servizio deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
+                # description validation
+                if "description" in data and not description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+                if description and len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
                         )
                     )
-                )
-            if "description" not in data and not self.context.description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-                # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
-                # su un sito che ha avuto upgrade alla versione pnrr può essere che
-                # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
-                # fino a qui
-                if field not in data and not text_in_block(
-                    getattr(self.context, field)
-                ):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
+                if "description" not in data and not self.context.description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+                    # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
+                    # su un sito che ha avuto upgrade alla versione pnrr può essere che
+                    # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
+                    # fino a qui
+                    if field not in data and not text_in_block(
+                        getattr(self.context, field)
+                    ):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
 
         if errors:
             raise BadRequest(errors)
-        return super(DeserializeDocumentoFromJson, self).__call__(
+
+        return super(DeserializeNewsFromJson, self).__call__(
             validate_all=False, data=data, create=False
         )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/dxfields.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/dxfields.py`

 * *Files 11% similar despite different names*

```diff
@@ -2,25 +2,31 @@
 from datetime import datetime
 from design.plone.contenttypes import _
 from design.plone.contenttypes.interfaces import IDesignPloneContenttypesLayer
 from design.plone.contenttypes.interfaces.servizio import IServizio
 from plone.dexterity.interfaces import IDexterityContent
 from plone.formwidget.geolocation.geolocation import Geolocation
 from plone.formwidget.geolocation.interfaces import IGeolocationField
+from plone.restapi.deserializer.blocks import path2uid
 from plone.restapi.deserializer.dxfields import CollectionFieldDeserializer
 from plone.restapi.deserializer.dxfields import DefaultFieldDeserializer
+from plone.restapi.deserializer.dxfields import (
+    TextLineFieldDeserializer as BaseTextLineDeserializer,
+)
 from plone.restapi.interfaces import IBlockFieldDeserializationTransformer
 from plone.restapi.interfaces import IFieldDeserializer
 from zExceptions import BadRequest
 from zope.component import adapter
+from zope.component import getMultiAdapter
 from zope.component import subscribers
 from zope.i18n import translate
 from zope.interface import implementer
 from zope.schema.interfaces import IList
 from zope.schema.interfaces import ISourceText
+from zope.schema.interfaces import ITextLine
 
 import json
 
 
 KEYS_WITH_URL = ["linkUrl", "navigationRoot", "showMoreLink"]
 
 
@@ -121,7 +127,23 @@
                 else None,  # noqa
             }
 
             timeline.append(entry)
 
         self.field.validate(timeline)
         return timeline
+
+
+@implementer(IFieldDeserializer)
+@adapter(ITextLine, IServizio, IDesignPloneContenttypesLayer)
+class LinkTextLineFieldDeserializer(BaseTextLineDeserializer):
+    def __call__(self, value):
+        value = super().__call__(value)
+        if self.field.getName() == "canale_digitale_link":
+            portal = getMultiAdapter(
+                (self.context, self.context.REQUEST), name="plone_portal_state"
+            ).portal()
+
+            transformed_url = path2uid(context=portal, link=value)
+            if transformed_url != value and "resolveuid" in transformed_url:
+                value = "${{portal_url}}/{uid}".format(uid=transformed_url)
+        return value
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/news.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/documento.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 # -*- coding: utf-8 -*-
-from plone.app.contenttypes.interfaces import INewsItem
+from design.plone.contenttypes.interfaces.documento import IDocumento
 from plone.restapi.behaviors import IBlocks
 from plone.restapi.deserializer import json_body
 from plone.restapi.deserializer.dxcontent import DeserializeFromJson
 from plone.restapi.indexers import SearchableText_blocks
 from plone.restapi.interfaces import IDeserializeFromJson
 from zExceptions import BadRequest
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import Interface
 
 
-TITLE_MAX_LEN = 160
-DESCRIPTION_MAX_LEN = 160
+TITLE_MAX_LEN = 255
+DESCRIPTION_MAX_LEN = 255
 EMPTY_BLOCK_MARKER = {"@type": "text"}
 MANDATORY_RICH_TEXT_FIELDS = [
-    "descrizione_estesa",
+    # "descrizione_estesa",
+    "formati_disponibili",
 ]
 
 
 def new_error(message):
     return {"error": "ValidationError", "message": message}
 
 
@@ -44,99 +45,105 @@
         return None
 
     fakeObj = FakeObject(blocks.get("blocks", ""), blocks.get("blocks_layout", ""))
     return SearchableText_blocks(fakeObj)()
 
 
 @implementer(IDeserializeFromJson)
-@adapter(INewsItem, Interface)
-class DeserializeNewsFromJson(DeserializeFromJson):
+@adapter(IDocumento, Interface)
+class DeserializeDocumentoFromJson(DeserializeFromJson):
     def __call__(
         self, validate_all=False, data=None, create=False
     ):  # noqa: ignore=C901
-
         if data is None:
             data = json_body(self.request)
 
         method = self.request.get("method")
         is_post = method == "POST"
         is_patch = method == "PATCH"
         errors = []
 
-        title = data.get("title")
-        description = data.get("description")
-
-        if is_post:
-            # Title validation
-            if not title:
-                errors.append(new_error("Il titolo del servizio è obbligatorio"))
-            elif len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
+        if list(data.keys()) != ["ordering"]:
+            title = data.get("title")
+            description = data.get("description")
+            if is_post:
+                # Title validation
+                if not title:
+                    errors.append(new_error("Il titolo è obbligatorio"))
+                elif len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
                         )
                     )
-                )
 
-            # description validation
-            if not description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-            elif len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione del servizio deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
+                # description validation
+                if not description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+                elif len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
                         )
                     )
-                )
 
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field not in data:
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-                elif field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-
-        if is_patch:
-            # Title validation
-            if "title" in data and not title:
-                errors.append(new_error("Il titolo del servizio è obbligatorio"))
-            if title and len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field not in data:
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+                    elif field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+
+            if is_patch:
+                # Title validation
+                if "title" in data and not title:
+                    errors.append(new_error("Il titolo è obbligatorio"))
+                if title and len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
                         )
                     )
-                )
-            # description validation
-            if "description" in data and not description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-            if description and len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione del servizio deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
+                # description validation
+                if "description" in data and not description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+                if description and len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
                         )
                     )
-                )
-            if "description" not in data and not self.context.description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-                # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
-                # su un sito che ha avuto upgrade alla versione pnrr può essere che
-                # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
-                # fino a qui
-                if field not in data and not text_in_block(
-                    getattr(self.context, field)
-                ):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
+                if "description" not in data and not self.context.description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+                    # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
+                    # su un sito che ha avuto upgrade alla versione pnrr può essere che
+                    # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
+                    # fino a qui
+                    if field not in data and not text_in_block(
+                        getattr(self.context, field)
+                    ):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
 
         if errors:
             raise BadRequest(errors)
-
-        return super(DeserializeNewsFromJson, self).__call__(
+        return super(DeserializeDocumentoFromJson, self).__call__(
             validate_all=False, data=data, create=False
         )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/persona.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/persona.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,15 +19,14 @@
         self.sm = getSecurityManager()
         self.permission_cache = {}
         self.modified = {}
 
     def __call__(
         self, validate_all=False, data=None, create=False
     ):  # noqa: ignore=C901
-
         if data is None:
             data = json_body(self.request)
         if data:
             if (
                 "data_insediamento" in data
                 and data["data_insediamento"]
                 and len(data["data_insediamento"]) > 10
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/servizio.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/servizio.py`

 * *Files 12% similar despite different names*

```diff
@@ -7,16 +7,16 @@
 from plone.restapi.interfaces import IDeserializeFromJson
 from zExceptions import BadRequest
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import Interface
 
 
-TITLE_MAX_LEN = 160
-DESCRIPTION_MAX_LEN = 160
+TITLE_MAX_LEN = 255
+DESCRIPTION_MAX_LEN = 255
 EMPTY_BLOCK_MARKER = {"@type": "text"}
 MANDATORY_RICH_TEXT_FIELDS = [
     "a_chi_si_rivolge",
     "come_si_fa",
     "cosa_serve",
     "cosa_si_ottiene",
     "tempi_e_scadenze",
@@ -53,94 +53,102 @@
 
 @implementer(IDeserializeFromJson)
 @adapter(IServizio, Interface)
 class DeserializeServizioFromJson(DeserializeFromJson):
     def __call__(
         self, validate_all=False, data=None, create=False
     ):  # noqa: ignore=C901
-
         if data is None:
             data = json_body(self.request)
 
         method = self.request.get("method")
         is_post = method == "POST"
         is_patch = method == "PATCH"
         errors = []
 
-        title = data.get("title")
-        description = data.get("description")
-
-        if is_post:
-            # Title validation
-            if not title:
-                errors.append(new_error("Il titolo del servizio è obbligatorio"))
-            elif len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
+        if list(data.keys()) != ["ordering"]:
+            title = data.get("title")
+            description = data.get("description")
+
+            if is_post:
+                # Title validation
+                if not title:
+                    errors.append(new_error("Il titolo è obbligatorio"))
+                elif len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
                         )
                     )
-                )
 
-            # description validation
-            if not description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-            elif len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione del servizio deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
+                # description validation
+                if not description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+                elif len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
                         )
                     )
-                )
 
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field not in data:
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-                elif field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-
-        if is_patch:
-            # Title validation
-            if "title" in data and not title:
-                errors.append(new_error("Il titolo del servizio è obbligatorio"))
-            if title and len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field not in data:
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+                    elif field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+
+            if is_patch:
+                # Title validation
+                if "title" in data and not title:
+                    errors.append(new_error("Il titolo è obbligatorio"))
+                if title and len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
                         )
                     )
-                )
-            # description validation
-            if "description" in data and not description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-            if description and len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione del servizio deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
+                # description validation
+                if "description" in data and not description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+                if description and len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
                         )
                     )
-                )
-            if "description" not in data and not self.context.description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-                # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
-                # su un sito che ha avuto upgrade alla versione pnrr può essere che
-                # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
-                # fino a qui
-                if field not in data and not text_in_block(
-                    getattr(self.context, field)
-                ):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
+                if "description" not in data and not self.context.description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+                    # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
+                    # su un sito che ha avuto upgrade alla versione pnrr può essere che
+                    # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
+                    # fino a qui
+                    if field not in data and not text_in_block(
+                        getattr(self.context, field)
+                    ):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
 
         if errors:
             raise BadRequest(errors)
 
         return super(DeserializeServizioFromJson, self).__call__(
             validate_all=False, data=data, create=False
         )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/unitaorganizzativa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/unitaorganizzativa.py`

 * *Files 4% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from plone.restapi.interfaces import IDeserializeFromJson
 from zExceptions import BadRequest
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import Interface
 
 
-TITLE_MAX_LEN = 160
+TITLE_MAX_LEN = 255
 DESCRIPTION_MAX_LEN = 255
 EMPTY_BLOCK_MARKER = {"@type": "text"}
 MANDATORY_RICH_TEXT_FIELDS = ["competenze"]
 
 
 def new_error(message):
     return {"error": "ValidationError", "message": message}
@@ -47,100 +47,110 @@
 
 @implementer(IDeserializeFromJson)
 @adapter(IUnitaOrganizzativa, Interface)
 class DeserializeUnitaOrganizzativaFromJson(DeserializeFromJson):
     def __call__(
         self, validate_all=False, data=None, create=False
     ):  # noqa: ignore=C901
-
         if data is None:
             data = json_body(self.request)
 
         method = self.request.get("method")
         is_post = method == "POST"
         is_patch = method == "PATCH"
         errors = []
 
-        title = data.get("title")
-        description = data.get("description")
+        if list(data.keys()) != ["ordering"]:
+            title = data.get("title")
+            description = data.get("description")
+
+            if is_post:
+                # Title validation
+                if not title:
+                    errors.append(
+                        new_error("Il titolo dell'unità organizzativa è obbligatorio")
+                    )
+                elif len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
+                        )
+                    )
 
-        if is_post:
-            # Title validation
-            if not title:
-                errors.append(
-                    new_error("Il titolo dell'unità organizzativa è obbligatorio")
-                )
-            elif len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
-                        )
-                    )
-                )
-
-            # description validation
-            if not description:
-                errors.append(
-                    new_error("La descrizione dell'unità organizzativa è obbligatorio")
-                )
-            elif len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
-                        )
-                    )
-                )
-
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field not in data:
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-                elif field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-
-        if is_patch:
-            # Title validation
-            if "title" in data and not title:
-                errors.append(new_error("Il titolo del servizio è obbligatorio"))
-
-            if title and len(title) > TITLE_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            TITLE_MAX_LEN
-                        )
-                    )
-                )
-            # description validation
-            if "description" in data and not description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-            if description and len(description) > DESCRIPTION_MAX_LEN:
-                errors.append(
-                    new_error(
-                        "La descrizione del servizio deve avere una lunghezza di massimo {} caratteri".format(  # noqa
-                            DESCRIPTION_MAX_LEN
-                        )
-                    )
-                )
-
-            if "description" not in data and not self.context.description:
-                errors.append(new_error("La descrizione del servizio è obbligatorio"))
-
-            for field in MANDATORY_RICH_TEXT_FIELDS:
-                if field in data and not text_in_block(data.get(field)):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
-
-                # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
-                # su un sito che ha avuto upgrade alla versione pnrr può essere che
-                # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
-                # fino a qui
-                if field not in data and not text_in_block(
-                    getattr(self.context, field)
-                ):
-                    errors.append(new_error("Il campo {} è obbligatorio".format(field)))
+                # description validation
+                if not description:
+                    errors.append(
+                        new_error(
+                            "La descrizione dell'unità organizzativa è obbligatorio"
+                        )
+                    )
+                elif len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
+                        )
+                    )
+
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field not in data:
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+                    elif field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+
+            if is_patch:
+                # Title validation
+                if "title" in data and not title:
+                    errors.append(new_error("Il titolo è obbligatorio"))
+
+                if title and len(title) > TITLE_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                TITLE_MAX_LEN
+                            )
+                        )
+                    )
+                # description validation
+                if "description" in data and not description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+                if description and len(description) > DESCRIPTION_MAX_LEN:
+                    errors.append(
+                        new_error(
+                            "La descrizione deve avere una lunghezza di massimo {} caratteri".format(  # noqa
+                                DESCRIPTION_MAX_LEN
+                            )
+                        )
+                    )
+
+                if "description" not in data and not self.context.description:
+                    errors.append(new_error("La descrizione è obbligatoria"))
+
+                for field in MANDATORY_RICH_TEXT_FIELDS:
+                    if field in data and not text_in_block(data.get(field)):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
+
+                    # Se siamo nella patch siamo in modifica. Se siamo in modifica e siamo
+                    # su un sito che ha avuto upgrade alla versione pnrr può essere che
+                    # dei campi obbligatori un tempo non lo fossero e quindi arriviamo
+                    # fino a qui
+                    if field not in data and not text_in_block(
+                        getattr(self.context, field)
+                    ):
+                        errors.append(
+                            new_error("Il campo {} è obbligatorio".format(field))
+                        )
 
         if errors:
             raise BadRequest(errors)
         return super(DeserializeUnitaOrganizzativaFromJson, self).__call__(
             validate_all=False, data=data, create=False
         )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/deserializers/venue.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/deserializers/venue.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,16 +7,16 @@
 from plone.restapi.interfaces import IDeserializeFromJson
 from zExceptions import BadRequest
 from zope.component import adapter
 from zope.interface import implementer
 from zope.interface import Interface
 
 
-TITLE_MAX_LEN = 160
-DESCRIPTION_MAX_LEN = 160
+TITLE_MAX_LEN = 255
+DESCRIPTION_MAX_LEN = 255
 EMPTY_BLOCK_MARKER = {"@type": "text"}
 MANDATORY_RICH_TEXT_FIELDS = ["modalita_accesso"]
 
 
 def new_error(message):
     return {"error": "ValidationError", "message": message}
 
@@ -47,15 +47,14 @@
 
 @implementer(IDeserializeFromJson)
 @adapter(IVenue, Interface)
 class DeserializeLuogoFromJson(DeserializeFromJson):
     def __call__(
         self, validate_all=False, data=None, create=False
     ):  # noqa: ignore=C901
-
         if data is None:
             data = json_body(self.request)
 
         method = self.request.get("method")
         is_post = method == "POST"
         is_patch = method == "PATCH"
         errors = []
@@ -101,15 +100,14 @@
             for field in MANDATORY_RICH_TEXT_FIELDS:
                 if field not in data:
                     errors.append(new_error("Il campo {} è obbligatorio".format(field)))
                 elif field in data and not text_in_block(data.get(field)):
                     errors.append(new_error("Il campo {} è obbligatorio".format(field)))
 
         if is_patch:
-
             # Title validation
             if "title" in data and not title:
                 errors.append(new_error("Il titolo del luogo è obbligatorio"))
             if title and len(title) > TITLE_MAX_LEN:
                 errors.append(
                     new_error(
                         "Il titolo può avere una lunghezza di massimo {} caratteri".format(  # noqa
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/bando.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/bando.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/cartella_modulistica.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/documento.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # -*- coding: utf-8 -*-
-from .related_news_serializer import SerializeFolderToJson as RelatedNewsSerializer
 from Acquisition import aq_inner
-from design.plone.contenttypes.interfaces.cartella_modulistica import (
-    ICartellaModulistica,
+from design.plone.contenttypes.interfaces.documento import IDocumento
+from design.plone.contenttypes.restapi.serializers.dxcontent import (
+    SerializeFolderToJson,
 )
 from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from zc.relation.interfaces import ICatalog
 from zope.component import adapter
 from zope.component import getMultiAdapter
 from zope.component import getUtility
@@ -14,16 +14,16 @@
 from zope.interface import implementer
 from zope.interface import Interface
 from zope.intid.interfaces import IIntIds
 from zope.security import checkPermission
 
 
 @implementer(ISerializeToJson)
-@adapter(ICartellaModulistica, Interface)
-class CartellaModulisticaSerializer(RelatedNewsSerializer):
+@adapter(IDocumento, Interface)
+class DocumentoSerializer(SerializeFolderToJson):
     def get_services(self):
         """ """
         catalog = getUtility(ICatalog)
         intids = getUtility(IIntIds)
         services = []
         for attr in ["altri_documenti"]:
             relations = catalog.findRelations(
@@ -43,13 +43,14 @@
                     summary = getMultiAdapter(
                         (obj, getRequest()), ISerializeToJsonSummary
                     )()
                     services.append(summary)
         return sorted(services, key=lambda k: k["title"])
 
     def __call__(self, version=None, include_items=True):
-        self.index = "news_uo"
-        result = super(CartellaModulisticaSerializer, self).__call__(
+        if "b_size" not in self.request.form:
+            self.request.form["b_size"] = 200
+        result = super(DocumentoSerializer, self).__call__(
             version=version, include_items=include_items
         )
         result["servizi_collegati"] = self.get_services()
         return result
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/configure.zcml`

 * *Files 6% similar despite different names*

```diff
@@ -5,26 +5,32 @@
 
   <!-- summary -->
   <adapter factory=".summary.DefaultJSONSummarySerializer" />
   <adapter factory=".summary.IncaricoDefaultJSONSummarySerializer" />
   <adapter factory=".summary.PersonaDefaultJSONSummarySerializer" />
   <adapter factory=".summary.PuntoDiContattoDefaultJSONSummarySerializer" />
   <adapter factory=".summary.EventDefaultJSONSummarySerializer" />
+  <adapter factory=".summary.NewsDefaultJSONSummarySerializer" />
+  <adapter factory=".summary.DatasetDefaultJSONSummarySerializer" />
+  <adapter factory=".summary.DocumentoPubblicoDefaultJSONSummarySerializer" />
+  <adapter factory=".summary.PraticaDefaultJSONSummarySerializer" />
+  <adapter factory=".modulo.SerializeModuloToJsonSummary" />
+  <adapter factory=".servizio.SerializeServizioToJsonSummary" />
+  <adapter factory=".unita_organizzativa.UOJSONSummarySerializer" />
+  <adapter factory=".venue.SerializeVenueToJsonSummary" />
+
 
   <adapter factory=".dxcontent.SerializeFolderToJson" />
   <adapter factory=".dxcontent.SerializeToJson" />
   <adapter factory=".dxfields.SourceTextSerializer" />
   <adapter factory=".dxfields.TempiEScadenzeValueSerializer" />
-  <adapter factory=".modulo.SerializeModuloToJsonSummary" />
+  <adapter factory=".dxfields.ServizioTextLineFieldSerializer" />
   <adapter factory=".persona.PersonaSerializer" />
   <adapter factory=".related_news_serializer.ServizioSerializer" />
   <adapter factory=".relationfield.RelationListFieldSerializer" />
-  <adapter factory=".servizio.SerializeServizioToJsonSummary" />
   <adapter factory=".unita_organizzativa.UOSerializer" />
-  <adapter factory=".unita_organizzativa.UOJSONSummarySerializer" />
-  <adapter factory=".venue.SerializeVenueToJsonSummary" />
   <adapter factory=".venue.VenueSerializer" />
   <adapter factory=".bando.BandoSerializer" />
   <adapter factory=".documento.DocumentoSerializer" />
   <adapter factory=".cartella_modulistica.CartellaModulisticaSerializer" />
   <adapter factory=".punto_di_contatto.PuntoDiContattoSerializer" />
 </configure>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/documento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/persona.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,56 +1,58 @@
 # -*- coding: utf-8 -*-
+from .related_news_serializer import SerializeFolderToJson
 from Acquisition import aq_inner
-from design.plone.contenttypes.interfaces.documento import IDocumento
-from design.plone.contenttypes.restapi.serializers.dxcontent import (
-    SerializeFolderToJson,
-)
+from design.plone.contenttypes.interfaces.persona import IPersona
 from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from zc.relation.interfaces import ICatalog
 from zope.component import adapter
 from zope.component import getMultiAdapter
 from zope.component import getUtility
 from zope.globalrequest import getRequest
 from zope.interface import implementer
 from zope.interface import Interface
 from zope.intid.interfaces import IIntIds
 from zope.security import checkPermission
 
 
 @implementer(ISerializeToJson)
-@adapter(IDocumento, Interface)
-class DocumentoSerializer(SerializeFolderToJson):
-    def get_services(self):
+@adapter(IPersona, Interface)
+class PersonaSerializer(SerializeFolderToJson):
+    index = "news_people"
+
+    def related_contents(self, field):
         """ """
         catalog = getUtility(ICatalog)
         intids = getUtility(IIntIds)
-        services = []
-        for attr in ["altri_documenti"]:
-            relations = catalog.findRelations(
-                dict(
-                    to_id=intids.getId(aq_inner(self.context)),
-                    from_attribute=attr,
-                )
+        items = []
+        relations = catalog.findRelations(
+            dict(
+                to_id=intids.getId(aq_inner(self.context)),
+                from_attribute=field,
             )
+        )
 
-            for rel in relations:
-                obj = intids.queryObject(rel.from_id)
-                if (
-                    obj is not None
-                    and checkPermission("zope2.View", obj)  # noqa
-                    and obj.portal_type == "Servizio"  # noqa
-                ):
-                    summary = getMultiAdapter(
-                        (obj, getRequest()), ISerializeToJsonSummary
-                    )()
-                    services.append(summary)
-        return sorted(services, key=lambda k: k["title"])
+        for rel in relations:
+            obj = intids.queryObject(rel.from_id)
+            if obj is not None and checkPermission("zope2.View", obj):
+                summary = getMultiAdapter(
+                    (obj, getRequest()), ISerializeToJsonSummary
+                )()
+                items.append(summary)
+        return sorted(items, key=lambda k: k["title"])
 
     def __call__(self, version=None, include_items=True):
-        if "b_size" not in self.request.form:
-            self.request.form["b_size"] = 200
-        result = super(DocumentoSerializer, self).__call__(
+        result = super(PersonaSerializer, self).__call__(
             version=version, include_items=include_items
         )
-        result["servizi_collegati"] = self.get_services()
+        strutture_correlate = self.related_contents(field="persone_struttura")
+        responsabile_di = self.related_contents(field="responsabile")
+        assessore_di = self.related_contents(field="assessore_riferimento")
+
+        if strutture_correlate:
+            result["strutture_correlate"] = strutture_correlate
+        if responsabile_di:
+            result["responsabile_di"] = responsabile_di
+        if assessore_di:
+            result["assessore_di"] = assessore_di
         return result
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/dxcontent.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/dxcontent.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,58 +1,77 @@
 # -*- coding: utf-8 -*-
+from collective.taxonomy import PATH_SEPARATOR
+from collective.taxonomy.interfaces import ITaxonomy
 from design.plone.contenttypes.interfaces import IDesignPloneContenttypesLayer
 from plone import api
 from plone.dexterity.interfaces import IDexterityContainer
 from plone.dexterity.interfaces import IDexterityContent
 from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.serializer.dxcontent import (
     SerializeFolderToJson as BaseFolderSerializer,
 )
 from plone.restapi.serializer.dxcontent import SerializeToJson as BaseSerializer
 from zope.component import adapter
+from zope.component import getUtility
 from zope.i18n import translate
 from zope.interface import implementer
 
 
 @implementer(ISerializeToJson)
 @adapter(IDexterityContent, IDesignPloneContenttypesLayer)
 class SerializeToJson(BaseSerializer):
     def __call__(self, version=None, include_items=True):
         result = super(SerializeToJson, self).__call__(
             version=version, include_items=include_items
         )
         ttool = api.portal.get_tool("portal_types")
+        result["design_italia_meta_type"] = translate(
+            ttool[self.context.portal_type].Title(), context=self.request
+        )
         if self.context.portal_type == "News Item":
-            result["design_italia_meta_type"] = self.context.tipologia_notizia
-        else:
-            result["design_italia_meta_type"] = translate(
-                ttool[self.context.portal_type].Title(), context=self.request
-            )
+            if self.context.tipologia_notizia:
+                taxonomy = getUtility(
+                    ITaxonomy, name="collective.taxonomy.tipologia_notizia"
+                )
+                taxonomy_voc = taxonomy.makeVocabulary(self.request.get("LANGUAGE"))
+
+                title = taxonomy_voc.inv_data.get(self.context.tipologia_notizia, None)
+
+                if title and title.startswith(PATH_SEPARATOR):
+                    result["design_italia_meta_type"] = title.replace(
+                        PATH_SEPARATOR, "", 1
+                    )
         return result
 
 
 @implementer(ISerializeToJson)
 @adapter(IDexterityContainer, IDesignPloneContenttypesLayer)
 class SerializeFolderToJson(BaseFolderSerializer):
     def __call__(self, version=None, include_items=True):
         result = super(SerializeFolderToJson, self).__call__(
             version=version, include_items=include_items
         )
         result["@id"] = self.context.absolute_url()
         ttool = api.portal.get_tool("portal_types")
+
+        result["design_italia_meta_type"] = translate(
+            ttool[self.context.portal_type].Title(), context=self.request
+        )
         if self.context.portal_type == "News Item":
-            try:
-                tipologia_news = self.context.tipologia_notizia
-            except AttributeError:
-                # fallback if we don't have c.taxonomy configured yet
-                tipologia_news = self.context.tipologia_notizia
-            result["design_italia_meta_type"] = tipologia_news
-        else:
-            result["design_italia_meta_type"] = translate(
-                ttool[self.context.portal_type].Title(), context=self.request
-            )
+            if self.context.tipologia_notizia:
+                taxonomy = getUtility(
+                    ITaxonomy, name="collective.taxonomy.tipologia_notizia"
+                )
+                taxonomy_voc = taxonomy.makeVocabulary(self.request.get("LANGUAGE"))
+
+                title = taxonomy_voc.inv_data.get(self.context.tipologia_notizia, None)
+
+                if title and title.startswith(PATH_SEPARATOR):
+                    result["design_italia_meta_type"] = title.replace(
+                        PATH_SEPARATOR, "", 1
+                    )
         if "items_total" not in result:
             # siamo in un sotto-elemento di quello richiesto dalla query.
             #  ritorniamo il numero di elementi totale, senza doverli ritornare
             # effettivamente.
             result["items_total"] = self.context.getFolderContents().actual_result_count
         return result
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/dxfields.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/dxfields.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,29 +1,33 @@
 # -*- coding: utf-8 -*-
 from AccessControl.unauthorized import Unauthorized
 from design.plone.contenttypes.interfaces import IDesignPloneContenttypesLayer
 from design.plone.contenttypes.interfaces.servizio import IServizio
 from plone import api
+from plone.app.contenttypes.utils import replace_link_variables_by_paths
 from plone.dexterity.interfaces import IDexterityContent
+from plone.outputfilters.browser.resolveuid import uuidToURL
 from plone.restapi.interfaces import IBlockFieldSerializationTransformer
 from plone.restapi.interfaces import IFieldSerializer
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from plone.restapi.serializer.converters import json_compatible
 from plone.restapi.serializer.dxfields import DefaultFieldSerializer
 from zope.component import adapter
 from zope.component import getMultiAdapter
 from zope.component import subscribers
 from zope.globalrequest import getRequest
 from zope.interface import implementer
 from zope.schema.interfaces import IList
 from zope.schema.interfaces import ISourceText
+from zope.schema.interfaces import ITextLine
 
 import json
+import re
 
-
+RESOLVEUID_RE = re.compile(".*?/resolve[Uu]id/([^/]*)/?(.*)$")
 KEYS_WITH_URL = ["linkUrl", "navigationRoot", "showMoreLink"]
 
 
 @implementer(IFieldSerializer)
 @adapter(ISourceText, IDexterityContent, IDesignPloneContenttypesLayer)
 class SourceTextSerializer(DefaultFieldSerializer):
     def __call__(self):
@@ -107,7 +111,30 @@
         "exclude_from_nav": False,
     }
     brains = api.content.find(**query)
     return [
         getMultiAdapter((brain, getRequest()), ISerializeToJsonSummary)()
         for brain in brains
     ]
+
+
+@adapter(ITextLine, IServizio, IDesignPloneContenttypesLayer)
+class ServizioTextLineFieldSerializer(DefaultFieldSerializer):
+    def __call__(self):
+        value = self.get_value()
+        if self.field.getName() != "canale_digitale_link" or not value:
+            return super().__call__()
+
+        path = replace_link_variables_by_paths(context=self.context, url=value)
+        match = RESOLVEUID_RE.match(path)
+        if match:
+            uid, suffix = match.groups()
+            value = uuidToURL(uid)
+        else:
+            portal = getMultiAdapter(
+                (self.context, self.context.REQUEST), name="plone_portal_state"
+            ).portal()
+            ref_obj = portal.restrictedTraverse(path, None)
+            if ref_obj:
+                value = ref_obj.absolute_url()
+
+        return json_compatible(value)
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/modulo.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/modulo.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/persona.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/modulistica_items/get.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,58 +1,79 @@
 # -*- coding: utf-8 -*-
-from .related_news_serializer import SerializeFolderToJson
-from Acquisition import aq_inner
-from design.plone.contenttypes.interfaces.persona import IPersona
-from plone.restapi.interfaces import ISerializeToJson
+from design.plone.contenttypes.interfaces.cartella_modulistica import (
+    ICartellaModulistica,
+)
+from plone.dexterity.utils import iterSchemata
+from plone.restapi.interfaces import IExpandableElement
+from plone.restapi.interfaces import IFieldSerializer
 from plone.restapi.interfaces import ISerializeToJsonSummary
-from zc.relation.interfaces import ICatalog
+from plone.restapi.serializer.converters import json_compatible
+from plone.restapi.services import Service
+from Products.CMFCore.interfaces import IFolderish
 from zope.component import adapter
-from zope.component import getMultiAdapter
-from zope.component import getUtility
-from zope.globalrequest import getRequest
+from zope.component import queryMultiAdapter
 from zope.interface import implementer
 from zope.interface import Interface
-from zope.intid.interfaces import IIntIds
-from zope.security import checkPermission
+from zope.schema import getFields
 
 
-@implementer(ISerializeToJson)
-@adapter(IPersona, Interface)
-class PersonaSerializer(SerializeFolderToJson):
-    index = "news_people"
-
-    def related_contents(self, field):
-        """ """
-        catalog = getUtility(ICatalog)
-        intids = getUtility(IIntIds)
-        items = []
-        relations = catalog.findRelations(
-            dict(
-                to_id=intids.getId(aq_inner(self.context)),
-                from_attribute=field,
-            )
-        )
-
-        for rel in relations:
-            obj = intids.queryObject(rel.from_id)
-            if obj is not None and checkPermission("zope2.View", obj):
-                summary = getMultiAdapter(
-                    (obj, getRequest()), ISerializeToJsonSummary
-                )()
-                items.append(summary)
-        return sorted(items, key=lambda k: k["title"])
-
-    def __call__(self, version=None, include_items=True):
-        result = super(PersonaSerializer, self).__call__(
-            version=version, include_items=include_items
-        )
-        strutture_correlate = self.related_contents(field="persone_struttura")
-        responsabile_di = self.related_contents(field="responsabile")
-        assessore_di = self.related_contents(field="assessore_riferimento")
-
-        if strutture_correlate:
-            result["strutture_correlate"] = strutture_correlate
-        if responsabile_di:
-            result["responsabile_di"] = responsabile_di
-        if assessore_di:
-            result["assessore_di"] = assessore_di
+@implementer(IExpandableElement)
+@adapter(ICartellaModulistica, Interface)
+class ModulisticaItems(object):
+    def __init__(self, context, request):
+        self.context = context
+        self.request = request
+
+    def __call__(self, expand=False):
+        result = {
+            "modulistica-items": {
+                "@id": "{}/@modulistica-items".format(self.context.absolute_url())
+            }
+        }
+        if not expand:
+            return result
+
+        data = self.get_modulistica_data()
+        if data:
+            result["modulistica-items"] = {"items": data}
         return result
+
+    def get_modulistica_data(self, context=None):
+        if context is None:
+            context = self.context
+        res = []
+        for brain in context.getFolderContents():
+            if brain.portal_type == "Document" and brain.getId == "multimedia":
+                continue
+            child = brain.getObject()
+            serializer = queryMultiAdapter(
+                (child, self.request), ISerializeToJsonSummary
+            )
+            data = serializer()
+            if child.portal_type == "Document":
+                for schema in iterSchemata(context):
+                    for name, field in getFields(schema).items():
+                        if name not in ["blocks", "blocks_layout"]:
+                            continue
+
+                        # serialize the field
+                        serializer = queryMultiAdapter(
+                            (field, child, self.request), IFieldSerializer
+                        )
+                        value = serializer()
+                        data[json_compatible(name)] = value
+            if IFolderish.providedBy(child):
+                children = [
+                    x
+                    for x in self.get_modulistica_data(context=child)
+                    if x.get("@type", "") not in ["Document", "CartellaModulistica"]
+                ]
+                if children:
+                    data["items"] = children
+            res.append(data)
+        return res
+
+
+class ModulisticaItemsGet(Service):
+    def reply(self):
+        data = ModulisticaItems(self.context, self.request)
+        return data(expand=True)["modulistica-items"]
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/punto_di_contatto.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/punto_di_contatto.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/related_news_serializer.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/related_news_serializer.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/relationfield.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/relationfield.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 
 
 @adapter(IRelationList, IDexterityContent, IDesignPloneContenttypesLayer)
 @implementer(IFieldSerializer)
 class RelationListFieldSerializer(DefaultRelationListFieldSerializer):
     def __call__(self):
         data = []
-        for value in self.get_value():
+        for value in self.get_value() or ():
             if not value:
                 continue
             try:
                 content = value.to_object
             except AttributeError:
                 # we'll migrate to PDC, right now we have Blocks
                 continue
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/servizio.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/servizio.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,12 +1,15 @@
 # -*- coding: utf-8 -*-
 from design.plone.contenttypes.interfaces.servizio import IServizio
 from design.plone.contenttypes.restapi.serializers.summary import (
     DefaultJSONSummarySerializer,
 )
+from design.plone.contenttypes.restapi.serializers.summary import (
+    get_taxonomy_information,
+)
 from plone.dexterity.utils import iterSchemata
 from plone.restapi.interfaces import IFieldSerializer
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from zope.component import adapter
 from zope.component import queryMultiAdapter
 from zope.interface import implementer
 from zope.interface import Interface
@@ -30,8 +33,10 @@
                 )
                 value = serializer()
                 summary[name] = value
 
         parent = self.context.aq_inner.aq_parent
         summary["parent_title"] = parent.title
         summary["parent_url"] = parent.absolute_url()
+        get_taxonomy_information("person_life_events", self.context, summary)
+        get_taxonomy_information("business_events", self.context, summary)
         return summary
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/unita_organizzativa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/unita_organizzativa.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,17 @@
 # -*- coding: utf-8 -*-
-from .related_news_serializer import SerializeFolderToJson as RelatedNewsSerializer
+from .dxcontent import SerializeFolderToJson as BaseSerializer
 from Acquisition import aq_inner
 from design.plone.contenttypes.interfaces.unita_organizzativa import IUnitaOrganizzativa
 from design.plone.contenttypes.restapi.serializers.summary import (
     DefaultJSONSummarySerializer,
 )
+from design.plone.contenttypes.restapi.serializers.summary import (
+    get_taxonomy_information,
+)
 from plone import api
 from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from plone.restapi.serializer.converters import json_compatible
 from zc.relation.interfaces import ICatalog
 from zope.component import adapter
 from zope.component import getMultiAdapter
@@ -18,15 +21,15 @@
 from zope.interface import Interface
 from zope.intid.interfaces import IIntIds
 from zope.security import checkPermission
 
 
 @implementer(ISerializeToJson)
 @adapter(IUnitaOrganizzativa, Interface)
-class UOSerializer(RelatedNewsSerializer):
+class UOSerializer(BaseSerializer):
     def get_services(self):
         """ """
         catalog = getUtility(ICatalog)
         intids = getUtility(IIntIds)
         services = []
         for attr in ["ufficio_responsabile", "area"]:
             relations = catalog.findRelations(
@@ -135,14 +138,16 @@
             if field == "contact_info":
                 data[field] = json_compatible(getattr(self.context, field, ""))
             else:
                 data[field] = getattr(self.context, field, "")
 
         data["geolocation"] = self.getGeolocation()
 
+        get_taxonomy_information("tipologia_organizzazione", self.context, data)
+
         return data
 
     def getGeolocation(self):
         longitude = 0
         latitude = 0
 
         if getattr(self.context, "geolocation", None):
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/serializers/venue.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/serializers/venue.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,14 +1,17 @@
 # -*- coding: utf-8 -*-
 from .related_news_serializer import SerializeFolderToJson as RelatedNewsSerializer
 from Acquisition import aq_inner
 from collective.venue.interfaces import IVenue
 from design.plone.contenttypes.restapi.serializers.summary import (
     DefaultJSONSummarySerializer,
 )
+from design.plone.contenttypes.restapi.serializers.summary import (
+    get_taxonomy_information,
+)
 from plone import api
 from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from plone.restapi.serializer.converters import json_compatible
 from zc.relation.interfaces import ICatalog
 from zope.component import adapter
 from zope.component import getMultiAdapter
@@ -98,8 +101,11 @@
         ]
 
         for field in fields:
             value = getattr(self.context, field, None)
             if callable(value):
                 value = value()
             summary[field] = json_compatible(value)
+
+        get_taxonomy_information("tipologia_luogo", self.context, summary)
+
         return summary
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/content/add.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/content/add.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/controlpanel.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/controlpanel.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/modulistica_items/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/modulistica_items/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/modulistica_items/get.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/trasparenza/get.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,79 +1,108 @@
 # -*- coding: utf-8 -*-
-from design.plone.contenttypes.interfaces.cartella_modulistica import (
-    ICartellaModulistica,
-)
-from plone.dexterity.utils import iterSchemata
+from plone import api
 from plone.restapi.interfaces import IExpandableElement
-from plone.restapi.interfaces import IFieldSerializer
+from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.interfaces import ISerializeToJsonSummary
-from plone.restapi.serializer.converters import json_compatible
 from plone.restapi.services import Service
 from Products.CMFCore.interfaces import IFolderish
 from zope.component import adapter
+from zope.component import getMultiAdapter
 from zope.component import queryMultiAdapter
+from zope.globalrequest import getRequest
 from zope.interface import implementer
 from zope.interface import Interface
-from zope.schema import getFields
+
+
+TRASPARENZA_FIELDS = [
+    "modalita_avvio",
+    "descrizione",
+    "soggetti_esterni",
+    "decorrenza_termine",
+    "dove_rivolgersi",
+    "dove_rivolgersi_extra",
+    "fine_termine",
+    "silenzio_assenso",
+    "ufficio_responsabile",
+    "provvedimento_finale",
+    "organo_competente_provvedimento_finale",
+    "modalita_richiesta_informazioni",
+    "procedura_online",
+    "altre_modalita_invio",
+    "atti_documenti_corredo",
+    "reperimento_modulistica",
+    "pagamenti",
+    "strumenti_tutela",
+    "titolare_potere_sostitutivo",
+    "customer_satisfaction",
+    "riferimenti_normativi",
+    "tempo_medio",
+    "file_correlato",
+    "responsabile_procedimento",
+    "dirigente",
+]
+
+
+class TrasparenzaService(Service):
+    def reply(self):
+        catalog = api.portal.get_tool("portal_catalog")
+        brains = catalog(**{"UID": self.request.uid})[0]
+        obj = getMultiAdapter((brains.getObject(), getRequest()), ISerializeToJson)()
+        result = {}
+        for field in TRASPARENZA_FIELDS:
+            result[field] = obj.get(field)
+        return result
 
 
 @implementer(IExpandableElement)
-@adapter(ICartellaModulistica, Interface)
-class ModulisticaItems(object):
+@adapter(Interface, Interface)
+class TrasparenzaItems(object):
     def __init__(self, context, request):
         self.context = context
         self.request = request
 
     def __call__(self, expand=False):
+        if "amministrazione-trasparente" not in self.context.absolute_url():
+            return {}
+
         result = {
-            "modulistica-items": {
-                "@id": "{}/@modulistica-items".format(self.context.absolute_url())
+            "trasparenza-items": {
+                "@id": "{}/@trasparenza-items".format(self.context.absolute_url())
             }
         }
         if not expand:
             return result
-
-        data = self.get_modulistica_data()
+        data = self.get_trasparenza_data()
         if data:
-            result["modulistica-items"] = {"items": data}
+            result["trasparenza-items"] = {"items": data}
         return result
 
-    def get_modulistica_data(self, context=None):
+    def get_trasparenza_data(self, context=None):
         if context is None:
             context = self.context
         res = []
-        for child in context.listFolderContents():
-            if child.portal_type == "Document" and child.getId() == "multimedia":
-                continue
 
+        for child in context.listFolderContents():
             serializer = queryMultiAdapter(
                 (child, self.request), ISerializeToJsonSummary
             )
             data = serializer()
             if child.portal_type == "Document":
-                for schema in iterSchemata(context):
-                    for name, field in getFields(schema).items():
-                        if name not in ["blocks", "blocks_layout"]:
-                            continue
-
-                        # serialize the field
-                        serializer = queryMultiAdapter(
-                            (field, child, self.request), IFieldSerializer
-                        )
-                        value = serializer()
-                        data[json_compatible(name)] = value
-            if IFolderish.providedBy(child):
-                children = [
-                    x
-                    for x in self.get_modulistica_data(context=child)
-                    if x.get("@type", "") not in ["Document", "CartellaModulistica"]
-                ]
-                if children:
-                    data["items"] = children
+                if IFolderish.providedBy(child):
+                    children = [
+                        x
+                        for x in self.get_trasparenza_data(context=child)
+                        if x.get("@type", "")
+                        in [
+                            "Document",
+                        ]
+                    ]
+                    if children:
+                        data["items"] = children
             res.append(data)
         return res
 
 
-class ModulisticaItemsGet(Service):
+class TrasparenzaItemsGet(Service):
     def reply(self):
-        data = ModulisticaItems(self.context, self.request)
-        return data(expand=True)["modulistica-items"]
+        data = TrasparenzaItems(self.context, self.request)
+        return data(expand=True)["trasparenza-items"]
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/scadenziario/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/scadenziario/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/scadenziario/post.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/scadenziario/post.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/trasparenza/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/trasparenza/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/services/types/get.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/services/types/get.py`

 * *Files 4% similar despite different names*

```diff
@@ -237,14 +237,18 @@
 
         return result
 
     def customize_servizio_schema(self, result):
         result.get("required").append("description")
         return result
 
+    def customize_evento_schema(self, result):
+        result.get("required").append("description")
+        return result
+
     def customize_uo_schema(self, result):
         result.get("required").append("description")
         versioning_fields = ["contact_info"]
         for field in versioning_fields:
             for fieldset in result["fieldsets"]:
                 if fieldset.get("id") == "contatti" and field in fieldset["fields"]:
                     fieldset["fields"].remove(field)
@@ -289,14 +293,16 @@
                 result = self.customize_servizio_schema(result)
             if pt == "UnitaOrganizzativa":
                 result = self.customize_uo_schema(result)
             if pt == "News Item":
                 result = self.customize_news_schema(result)
             if pt == "Documento":
                 result = self.customize_documento_schema(result)
+            if pt == "Event":
+                result = self.customize_evento_schema(result)
             result = self.customize_versioning_fields_fieldset(result)
         return result
 
     def get_order_by_type(self, portal_type):
         return [x for x in FIELDSETS_ORDER.get(portal_type, [])]
 
     def reorder_fieldsets(self, original):
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/restapi/types/adapters.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/restapi/types/adapters.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,32 +1,35 @@
 # -*- coding: utf-8 -*-
 from collective.z3cform.datagridfield.interfaces import IRow
 from design.plone.contenttypes import _
+from design.plone.contenttypes.interfaces import IDesignPloneContenttypesLayer
 from plone.restapi.types.adapters import ObjectJsonSchemaProvider
+from redturtle.volto.types.adapters import (
+    TextLineJsonSchemaProvider as BaseTextLineJsonSchemaProvider,
+)
 from plone.restapi.types.interfaces import IJsonSchemaProvider
 from plone.restapi.types.utils import get_fieldsets
 from plone.restapi.types.utils import get_jsonschema_properties
 from plone.restapi.types.utils import iter_fields
 from zope.component import adapter
 from zope.component import getUtility
 from zope.i18n import translate
 from zope.interface import implementer
 from zope.interface import Interface
 from zope.schema.interfaces import IField
+from zope.schema.interfaces import ITextLine
 from zope.schema.interfaces import IVocabularyFactory
 
-
 DATAGRID_FIELDS = ["value_punto_contatto", "timeline_tempi_scadenze"]
 
 
 @adapter(IField, Interface, Interface)
 @implementer(IJsonSchemaProvider)
 class LeadImageJsonSchemaProvider(ObjectJsonSchemaProvider):
     def get_size_vocabulary(self):
-
         factory = getUtility(
             IVocabularyFactory, "design.plone.vocabularies.leadimage_dimension"
         )
 
         vocabulary = factory(self.context)._terms
         return {term.token: term.title for term in vocabulary if term.token}
 
@@ -86,7 +89,19 @@
                 "title": "Default",
                 "fields": [x for x in properties.keys()],
             },
         ]
         info["required"] = required
         info["properties"] = properties
         return info
+
+
+@adapter(ITextLine, Interface, IDesignPloneContenttypesLayer)
+@implementer(IJsonSchemaProvider)
+class TextLineJsonSchemaProvider(BaseTextLineJsonSchemaProvider):
+    def get_widget(self):
+        """
+        Force url widget to some fields
+        """
+        if self.field.__name__ == "canale_digitale_link":
+            return "url"
+        return super().get_widget()
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/schema_overrides.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/schema_overrides.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,14 @@
 
     order = 999999
 
     def __init__(self, schema):
         self.schema = schema
 
     def __call__(self):
-
         if self.schema.getName() == "IRelatedItems":
             fieldset = Fieldset(
                 "correlati",
                 label=_("correlati_label", default="Contenuti collegati"),
                 fields=["relatedItems"],
             )
             self.schema._Element__tagged_values["plone.supermodel.fieldsets"] = [
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/setuphandlers.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/setuphandlers.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/testing.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/testing.py`

 * *Files 17% similar despite different names*

```diff
@@ -4,24 +4,29 @@
 from plone.app.testing import IntegrationTesting
 from plone.testing import z2
 from redturtle.volto.testing import RedturtleVoltoLayer
 from redturtle.volto.testing import RedturtleVoltoRestApiLayer
 from zope.configuration import xmlconfig
 
 import collective.address
-import collective.folderishtypes
+import collective.contentrules.mailfromfield
+import collective.taxonomy
+
+# import collective.folderishtypes
 import collective.venue
 import collective.volto.blocksfield
 import collective.volto.cookieconsent
+import collective.z3cform.datagridfield
 import design.plone.contenttypes
+import eea.api.taxonomy
 import kitconcept.seo
 import plone.app.caching
 import plone.formwidget.geolocation
-import plone.restapi
 import redturtle.bandi
+import redturtle.prenotazioni
 import redturtle.volto
 
 
 class DesignPloneContenttypesLayer(RedturtleVoltoLayer):
     def setUpZope(self, app, configurationContext):
         # Load any other ZCML that is required for your tests.
         # The z3c.autoinclude feature is disabled in the Plone fixture base
@@ -35,14 +40,17 @@
         xmlconfig.file(
             "configure.zcml",
             design.plone.contenttypes,
             context=configurationContext,
         )
         self.loadZCML(package=redturtle.bandi)
         self.loadZCML(package=kitconcept.seo)
+        self.loadZCML(package=eea.api.taxonomy)
+        self.loadZCML(package=collective.taxonomy)
+        self.loadZCML(package=collective.z3cform.datagridfield)
 
     def setUpPloneSite(self, portal):
         super().setUpPloneSite(portal)
         applyProfile(portal, "design.plone.contenttypes:default")
 
 
 DESIGN_PLONE_CONTENTTYPES_FIXTURE = DesignPloneContenttypesLayer()
@@ -63,26 +71,36 @@
 class DesignPloneContenttypesRestApiLayer(RedturtleVoltoRestApiLayer):
     def setUpZope(self, app, configurationContext):
         super().setUpZope(app, configurationContext)
         self.loadZCML(package=collective.venue)
         self.loadZCML(package=collective.volto.blocksfield)
         self.loadZCML(package=design.plone.contenttypes, context=configurationContext)
         self.loadZCML(package=plone.formwidget.geolocation)
-        self.loadZCML(name="overrides.zcml", package=design.plone.contenttypes)
+        self.loadZCML(package=eea.api.taxonomy)
+        self.loadZCML(package=collective.taxonomy)
         xmlconfig.file(
             "configure.zcml",
             design.plone.contenttypes,
             context=configurationContext,
         )
         self.loadZCML(package=redturtle.bandi)
         self.loadZCML(package=kitconcept.seo)
 
+        # TODO: valutare un layer a parte per i test di redturtle.prenotazioni
+        self.loadZCML(package=redturtle.prenotazioni)
+        self.loadZCML(package=collective.z3cform.datagridfield)
+        self.loadZCML(package=collective.contentrules.mailfromfield)
+
+        self.loadZCML(name="overrides.zcml", package=design.plone.contenttypes)
+
     def setUpPloneSite(self, portal):
         super().setUpPloneSite(portal)
         applyProfile(portal, "design.plone.contenttypes:default")
+        # TODO: valutare un layer a parte per i test di redturtle.prenotazioni
+        applyProfile(portal, "redturtle.prenotazioni:default")
 
 
 DESIGN_PLONE_CONTENTTYPES_API_FIXTURE = DesignPloneContenttypesRestApiLayer()
 DESIGN_PLONE_CONTENTTYPES_API_INTEGRATION_TESTING = IntegrationTesting(
     bases=(DESIGN_PLONE_CONTENTTYPES_API_FIXTURE,),
     name="DesignPloneContenttypesRestApiLayer:Integration",
 )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/example.pdf` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/example.pdf`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_argomenti.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_argomenti.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_base_serializer.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_base_serializer.py`

 * *Files 12% similar despite different names*

```diff
@@ -44,22 +44,24 @@
 
     def test_design_italia_meta_type_with_news(self):
         """
         News should return the news type (tipologia_notizia field)
         Other types shoule return their own portal_type.
         """
         response_news = self.api_session.get(self.news.absolute_url() + "?fullobjects")
-        self.assertTrue(
-            response_news.json()["design_italia_meta_type"] == "Comunicati stampa"
+        self.assertEqual(
+            response_news.json()["design_italia_meta_type"],
+            "Notizie e comunicati stampa",
         )
 
     def test_design_italia_meta_type_with_type_different_from_news(self):
         """
         News should return the news type (tipologia_notizia field)
         Other types shoule return their own portal_type.
         """
         response_service = self.api_session.get(
             self.service.absolute_url() + "?fullobjects"
         )
-        self.assertTrue(
-            response_service.json()["design_italia_meta_type"] == "Servizio"
+        self.assertEqual(
+            response_service.json()["design_italia_meta_type"],
+            "Servizio",
         )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_descrizione_estesa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_descrizione_estesa.py`

 * *Files 6% similar despite different names*

```diff
@@ -11,16 +11,16 @@
 from plone.app.testing import TEST_USER_ID
 from plone.restapi.testing import RelativeSession
 
 import unittest
 
 
 class TestDescrizioneEstesaBehavior(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
+    maxDiff = None
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
 
@@ -28,15 +28,14 @@
         self.api_session.headers.update({"Accept": "application/json"})
         self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
 
     def tearDown(self):
         self.api_session.close()
 
     def test_descrizione_estesa_indexed(self):
-
         # Servizio have design.plone.contenttypes.behavior.descrizione_estesa
         # behavior
         servizio = api.content.create(
             container=self.portal,
             type="Servizio",
             title="Test servizio",
             descrizione_estesa={"blocks": {"12345": {"searchableText": "foo"}}},
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_luogo.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_luogo.py`

 * *Files 2% similar despite different names*

```diff
@@ -8,16 +8,16 @@
 from plone.dexterity.fti import DexterityFTI
 from transaction import commit
 
 import unittest
 
 
 class LuogoBehaviorIndexerFunctionalTest(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_FUNCTIONAL_TESTING
+    maxDiff = None
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
         self.catalog = api.portal.get_tool("portal_catalog")
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
         fti = DexterityFTI("venueitem")
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_show_modified.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_show_modified.py`

 * *Files 4% similar despite different names*

```diff
@@ -13,16 +13,16 @@
 from plone.restapi.testing import RelativeSession
 
 import transaction
 import unittest
 
 
 class TestShowModifiedBehavior(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
+    maxDiff = None
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
 
@@ -37,15 +37,14 @@
             "show_modified_default",
             False,
             interface=IDesignPloneSettings,
         )
         transaction.commit()
 
     def test_if_not_set_return_site_default(self):
-
         page = api.content.create(
             container=self.portal,
             type="Document",
             title="Test document",
         )
         transaction.commit()
         resp = self.api_session.get(page.absolute_url())
@@ -61,15 +60,14 @@
         transaction.commit()
 
         resp = self.api_session.get(page.absolute_url())
         self.assertFalse(getattr(page, "show_modified", None))
         self.assertFalse(resp.json().get("show_modified", None))
 
     def test_if_set_will_override_default(self):
-
         page = api.content.create(
             container=self.portal,
             type="Document",
             title="Test document",
             show_modified=False,
         )
         transaction.commit()
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_behavior_update_note.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_behavior_update_note.py`

 * *Files 5% similar despite different names*

```diff
@@ -12,16 +12,16 @@
 from plone.restapi.testing import RelativeSession
 
 import transaction
 import unittest
 
 
 class TestUpdateNoteBehavior(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
+    maxDiff = None
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
 
@@ -29,15 +29,14 @@
         self.api_session.headers.update({"Accept": "application/json"})
         self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
 
     def tearDown(self):
         self.api_session.close()
 
     def test_is_enabled_in_bando(self):
-
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertIn(
             "design.plone.contenttypes.behavior.update_note",
             portal_types["Bando"].behaviors,
         )
 
     def test_if_compiled_is_stored_in_metadata(self):
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_change_news_type.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_change_news_type.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,55 +1,57 @@
-from plone.app.testing import setRoles
-from plone.app.testing import TEST_USER_ID
-from plone import api
-
+# -*- coding: utf-8 -*-
 from design.plone.contenttypes.testing import (
     DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING,
 )
+from plone import api
+from plone.app.testing import setRoles
+from plone.app.testing import TEST_USER_ID
 
 import unittest
 
 
 class MoveNewsItemView(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
+        # default values are set in italian
+        self.request["LANGUAGE"] = "it"
         self.view = api.content.get_view(
             "change_news_type", context=self.portal, request=self.request
         )
 
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
 
         self.news_container = api.content.create(
             type="Folder",
             title="News container",
             container=self.portal,
         )
         self.news_item = api.content.create(
             type="News Item",
             title="news item",
-            tipologia_notizia="Notizia",
+            tipologia_notizia=["notizia"],
             container=self.portal,
         )
         self.news_item1 = api.content.create(
             type="News Item",
             title="news item1",
-            tipologia_notizia="Notizia",
+            tipologia_notizia=["notizia"],
             container=self.news_container,
         )
 
     def test_substitute_news_type(self):
-        new_news_type = "New news type"
-        self.view.request.form["news_type_in_catalog"] = "Notizia"
-        self.view.request.form["news_type_portal"] = "New news type"
+        new_news_type = "comunicato_stampa"
+        self.view.request.form["news_type_in_catalog"] = "notizia"
+        self.view.request.form["news_type_portal"] = new_news_type
         self.view.request.form["substitute"] = "true"
 
         # mock the helper methods of our view
         self.view.news_types = lambda: [new_news_type]
 
+        # self.portal.portal_catalog(ti)
         self.view.substitute_news_type()
 
         self.assertEqual(new_news_type, self.news_item.tipologia_notizia)
         self.assertEqual(new_news_type, self.news_item1.tipologia_notizia)
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_bando.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_bando.py`

 * *Files 1% similar despite different names*

```diff
@@ -35,13 +35,12 @@
     def test_disabled_default_ente(self):
         default_ente = api.portal.get_registry_record(
             "default_ente", interface=IBandoSettings
         )
         self.assertEqual(default_ente, ())
 
     def test_bando_substructure_created(self):
-
         bando = api.content.create(container=self.portal, type="Bando", title="Bando")
 
         self.assertIn("documenti", bando.keys())
         self.assertIn("comunicazioni", bando.keys())
         self.assertIn("esiti", bando.keys())
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_cartella_modulistica.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_cartella_modulistica.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_document.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_document.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_documento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_persona.py`

 * *Files 12% similar despite different names*

```diff
@@ -7,130 +7,141 @@
     DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING,
 )
 from plone import api
 from plone.app.testing import setRoles
 from plone.app.testing import SITE_OWNER_NAME
 from plone.app.testing import SITE_OWNER_PASSWORD
 from plone.app.testing import TEST_USER_ID
-from plone.namedfile.file import NamedBlobFile
 from plone.restapi.testing import RelativeSession
+from transaction import commit
+from z3c.relationfield import RelationValue
+from zope.component import getUtility
+from zope.intid.interfaces import IIntIds
 
-import os
-import transaction
 import unittest
 
 
-class TestDocument(unittest.TestCase):
+class TestPersona(unittest.TestCase):
     layer = DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING
 
     def setUp(self):
         """Custom shared utility setup for tests."""
         self.portal = self.layer["portal"]
 
-    def test_behaviors_enabled_for_documento(self):
+    def test_behaviors_enabled_for_persona(self):
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertEqual(
-            portal_types["Documento"].behaviors,
+            portal_types["Persona"].behaviors,
             (
                 "plone.namefromtitle",
                 "plone.allowdiscussion",
                 "plone.excludefromnavigation",
                 "plone.shortname",
-                "plone.dublincore",
+                "plone.ownership",
+                "plone.publication",
                 "plone.relateditems",
+                "plone.categorization",
+                "plone.basic",
                 "plone.locking",
-                "plone.constraintypes",
-                "plone.leadimage",
-                "volto.preview_image",
-                "design.plone.contenttypes.behavior.argomenti_documento",
-                "design.plone.contenttypes.behavior.descrizione_estesa_documento",  # noqa
                 "design.plone.contenttypes.behavior.additional_help_infos",
+                "design.plone.contenttypes.behavior.contatti_persona",
                 "plone.textindexer",
                 "plone.translatable",
                 "kitconcept.seo",
                 "plone.versioning",
             ),
         )
 
-    def test_event_addable_types(self):
+    def test_persona_ct_title(self):
         portal_types = api.portal.get_tool(name="portal_types")
-        self.assertEqual(
-            ("Document", "Modulo", "Link"),
-            portal_types["Documento"].allowed_content_types,
-        )
+        self.assertEqual("Persona pubblica", portal_types["Persona"].title)
 
 
-class TestDocumentoApi(unittest.TestCase):
+class TestPersonaEndpoint(unittest.TestCase):
+    """"""
 
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
 
         self.api_session = RelativeSession(self.portal_url)
         self.api_session.headers.update({"Accept": "application/json"})
         self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
-        self.documento = api.content.create(
-            container=self.portal, type="Documento", title="Documento"
+
+        self.persona = api.content.create(
+            container=self.portal, type="Persona", title="John Doe"
         )
+        intids = getUtility(IIntIds)
 
-        transaction.commit()
+        self.persona_ref = RelationValue(intids.getId(self.persona))
+        commit()
 
     def tearDown(self):
         self.api_session.close()
 
-    def test_document_get_return_more_than_25_results_by_default(self):
-        for i in range(50):
-            child = api.content.create(
-                container=self.documento,
-                type="Modulo",
-                title="File {}".format(i),
-            )
-            filename = os.path.join(os.path.dirname(__file__), "example.pdf")
-            child.file = NamedBlobFile(
-                data=open(filename, "rb").read(),
-                filename="example.pdf",
-                contentType="application/pdf",
-            )
-        transaction.commit()
-        response = self.api_session.get(self.documento.absolute_url())
+    def test_persona_strutture_correlate(self):
+        uo = api.content.create(
+            container=self.portal,
+            type="UnitaOrganizzativa",
+            title="UO 1",
+            persone_struttura=[self.persona_ref],
+        )
+        commit()
+        response = self.api_session.get(self.persona.absolute_url())
         res = response.json()
-        self.assertEqual(len(res["items"]), len(self.documento.listFolderContents()))
 
-    def test_post_file_will_convert_into_modulo(self):
-        response = self.api_session.post(
-            self.documento.absolute_url(),
-            json={
-                "@type": "File",
-                "title": "My File",
-                "file": {
-                    "filename": "test.txt",
-                    "data": "Spam and Eggs",
-                    "content_type": "text/plain",
-                },
-            },
-        )
-        self.assertEqual(201, response.status_code)
-        transaction.commit()
-
-        self.assertEqual(self.documento["my-file"].portal_type, "Modulo")
-
-    def test_post_image_will_convert_into_modulo(self):
-        response = self.api_session.post(
-            self.documento.absolute_url(),
-            json={
-                "@type": "Image",
-                "title": "My Image",
-                "image": {
-                    "filename": "image.jpg",
-                    "data": "Spam and Eggs",
-                    "content_type": "image/jpeg",
-                },
-            },
+        self.assertIn("strutture_correlate", list(res.keys()))
+        self.assertEqual(len(res["strutture_correlate"]), 1)
+        self.assertEqual(res["strutture_correlate"][0]["title"], uo.title)
+
+    def test_persona_responsabile_di(self):
+        uo = api.content.create(
+            container=self.portal,
+            type="UnitaOrganizzativa",
+            title="UO 1",
+            responsabile=[self.persona_ref],
         )
-        self.assertEqual(201, response.status_code)
-        transaction.commit()
+        commit()
+        response = self.api_session.get(self.persona.absolute_url())
+        res = response.json()
 
-        self.assertEqual(self.documento["my-image"].portal_type, "Modulo")
+        self.assertIn("responsabile_di", list(res.keys()))
+        self.assertEqual(len(res["responsabile_di"]), 1)
+        self.assertEqual(res["responsabile_di"][0]["title"], uo.title)
+
+    def test_persona_assessore_di(self):
+        uo = api.content.create(
+            container=self.portal,
+            type="UnitaOrganizzativa",
+            title="UO 1",
+            assessore_riferimento=[self.persona_ref],
+        )
+        commit()
+        response = self.api_session.get(self.persona.absolute_url())
+        res = response.json()
+
+        self.assertIn("assessore_di", list(res.keys()))
+        self.assertEqual(len(res["assessore_di"]), 1)
+        self.assertEqual(res["assessore_di"][0]["title"], uo.title)
+
+    def test_atto_di_nomina_incarico(self):
+        incarico = api.content.create(
+            container=self.persona.incarichi, type="Incarico", title="Sindaco"
+        )
+        commit()
+        atto_nomina = api.content.create(
+            container=incarico, type="Documento", title="Atto di nomina"
+        )
+        commit()
+        intids = getUtility(IIntIds)
+        self.persona.incarichi_persona = [RelationValue(intids.getId(incarico))]
+        incarico.atto_nomina = [RelationValue(intids.getId(atto_nomina))]
+        commit()
+        response = self.api_session.get(self.persona.absolute_url())
+        res = response.json()
+        self.assertEqual(len(res["incarichi_persona"]), 1)
+        self.assertEqual(res["incarichi_persona"][0]["title"], incarico.title)
+        self.assertIn("atto_di_nomina", list(res["incarichi_persona"][0].keys()))
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_documento_personale.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_documento_personale.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_event.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_event.py`

 * *Files 16% similar despite different names*

```diff
@@ -17,60 +17,62 @@
 
 import transaction
 import unittest
 
 
 class TestEvent(unittest.TestCase):
     layer = DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING
+    maxDiff = None
 
     def setUp(self):
         """Custom shared utility setup for tests."""
         self.portal = self.layer["portal"]
 
     def test_behaviors_enabled_for_event(self):
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertEqual(
             portal_types["Event"].behaviors,
             (
                 "plone.eventbasic",
                 "plone.leadimage",
                 "volto.preview_image",
-                "design.plone.contenttypes.behavior.argomenti",
+                "design.plone.contenttypes.behavior.argomenti_evento",
                 "plone.eventrecurrence",
                 "design.plone.contenttypes.behavior.additional_help_infos",
                 "design.plone.contenttypes.behavior.evento",
                 "design.plone.contenttypes.behavior.luoghi_correlati_evento",
                 "design.plone.contenttypes.behavior.address_event",
                 "design.plone.contenttypes.behavior.geolocation_event",
                 "design.plone.contenttypes.behavior.strutture_correlate",
+                "design.plone.contenttypes.behavior.contatti_event",
                 "plone.dublincore",
                 "plone.namefromtitle",
                 "plone.allowdiscussion",
                 "plone.excludefromnavigation",
                 "plone.shortname",
                 "plone.relateditems",
                 "plone.versioning",
                 "plone.locking",
                 "plone.constraintypes",
                 "plone.textindexer",
                 "plone.translatable",
                 "kitconcept.seo",
+                "collective.taxonomy.generated.tipologia_evento",
             ),
         )
 
     def test_event_addable_types(self):
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertEqual(
             sorted(("Image", "File", "Link", "Event", "Document")),
             sorted(portal_types["Event"].allowed_content_types),
         )
 
 
 class TestEventApi(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
@@ -87,30 +89,33 @@
     def tearDown(self):
         self.api_session.close()
 
     def test_event_substructure_created(self):
         event = self.portal["evento"]
 
         self.assertEqual(
-            sorted(["multimedia", "documenti", "sponsor_evento"]),
+            sorted(["documenti", "immagini", "sponsor_evento", "video"]),
             sorted(event.keys()),
         )
 
-        self.assertEqual(event["multimedia"].portal_type, "Document")
-        self.assertEqual(event["multimedia"].constrain_types_mode, 1)
-        self.assertEqual(event["multimedia"].locally_allowed_types, ("Image", "Link"))
+        self.assertEqual(event["immagini"].portal_type, "Document")
+        self.assertEqual(event["immagini"].constrain_types_mode, 1)
+        self.assertEqual(event["immagini"].locally_allowed_types, ("Image", "Link"))
 
         self.assertEqual(event["sponsor_evento"].portal_type, "Document")
         self.assertEqual(event["sponsor_evento"].constrain_types_mode, 1)
         self.assertEqual(event["sponsor_evento"].locally_allowed_types, ("Link",))
 
         self.assertEqual(event["documenti"].portal_type, "Document")
         self.assertEqual(event["documenti"].constrain_types_mode, 1)
         self.assertEqual(event["documenti"].locally_allowed_types, ("File",))
 
-        multimedia_wf = api.content.get_state(obj=event["multimedia"])
-        sponsor_wf = api.content.get_state(obj=event["sponsor_evento"])
-        documenti_wf = api.content.get_state(obj=event["documenti"])
-
-        self.assertEqual(multimedia_wf, "published")
-        self.assertEqual(sponsor_wf, "published")
-        self.assertEqual(documenti_wf, "published")
+        self.assertEqual(event["video"].portal_type, "Document")
+        self.assertEqual(event["video"].constrain_types_mode, 1)
+        self.assertEqual(event["video"].locally_allowed_types, ("Link",))
+
+        self.assertEqual(api.content.get_state(obj=event["immagini"]), "published")
+        self.assertEqual(api.content.get_state(obj=event["video"]), "published")
+        self.assertEqual(
+            api.content.get_state(obj=event["sponsor_evento"]), "published"
+        )
+        self.assertEqual(api.content.get_state(obj=event["documenti"]), "published")
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_luogo.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_luogo.py`

 * *Files 10% similar despite different names*

```diff
@@ -10,60 +10,64 @@
 from plone.app.testing import setRoles
 from plone.app.testing import SITE_OWNER_NAME
 from plone.app.testing import SITE_OWNER_PASSWORD
 from plone.app.testing import TEST_USER_ID
 from plone.restapi.testing import RelativeSession
 from Products.CMFPlone.utils import getToolByName
 from transaction import commit
+from uuid import uuid4
 from z3c.relationfield import RelationValue
 from zope.component import getUtility
 from zope.intid.interfaces import IIntIds
 
 import unittest
 
 
 class TestLuogo(unittest.TestCase):
     layer = DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING
+    maxDiff = None
 
     def setUp(self):
         """Custom shared utility setup for tests."""
         self.portal = self.layer["portal"]
 
     def test_behaviors_enabled_for_luogo(self):
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertEqual(
             portal_types["Venue"].behaviors,
             (
                 "plone.app.content.interfaces.INameFromTitle",
                 "plone.app.dexterity.behaviors.id.IShortName",
                 "plone.app.dexterity.behaviors.metadata.IBasic",
                 "plone.app.dexterity.behaviors.metadata.ICategorization",
+                "plone.excludefromnavigation",
                 "plone.relateditems",
                 "plone.leadimage",
                 "volto.preview_image",
                 "design.plone.contenttypes.behavior.contatti_venue",
                 "design.plone.contenttypes.behavior.luogo",
                 "design.plone.contenttypes.behavior.argomenti",
                 "design.plone.contenttypes.behavior.address_venue",
                 "design.plone.contenttypes.behavior.geolocation_venue",
                 "design.plone.contenttypes.behavior.additional_help_infos",
+                "design.plone.contenttypes.behavior.luoghi_correlati",
                 "plone.textindexer",
                 "plone.translatable",
                 "kitconcept.seo",
                 "plone.versioning",
+                "collective.taxonomy.generated.tipologia_luogo",
             ),
         )
 
     def test_luogo_ct_title(self):
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertEqual("Luogo", portal_types["Venue"].title)
 
 
 class TestLuogoApi(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
@@ -122,19 +126,22 @@
         commit()
         self.assertEqual(venue.geolocation, None)
 
         response = self.api_session.patch(
             venue.absolute_url(),
             json={"@type": "Venue", "title": "Foo", "geolocation": {"foo": "bar"}},
         )
-        message = response.json()["message"]
+        # message = response.json()["message"]
 
         self.assertEqual(400, response.status_code)
-        self.assertIn("Invalid geolocation data", message)
-        self.assertEqual(venue.geolocation, None)
+        # TODO: anzichè `invalid geolocation data` ritorna
+        #       `Il campo geolocation è obbligatorio`
+        # self.assertIn("Invalid geolocation data", message)
+        # TODO: i dati vanno verificati con una chiamata alla api_session
+        # self.assertEqual(venue.geolocation, None)
 
     def test_venue_geolocation_deserializer_right_structure(self):
         venue = api.content.create(
             container=self.portal, type="Venue", title="Example venue"
         )
 
         commit()
@@ -144,19 +151,44 @@
             venue.absolute_url(),
             json={
                 "@type": "Venue",
                 "title": "Foo",
                 "geolocation": {"latitude": 11.0, "longitude": 10.0},
             },
         )
-        commit()
 
-        self.assertEqual(204, response.status_code)
-        self.assertEqual(venue.geolocation.latitude, 11.0)
-        self.assertEqual(venue.geolocation.longitude, 10.0)
+        self.assertEqual(response.status_code, 400)
+        self.assertEqual(
+            response.json()["message"],
+            "[{'error': 'ValidationError', "
+            "'message': 'Il campo modalita_accesso è obbligatorio'}]",
+        )
+
+        text_uuid = str(uuid4())
+        response = self.api_session.patch(
+            venue.absolute_url(),
+            json={
+                "@type": "Venue",
+                "title": "Foo",
+                "geolocation": {"latitude": 11.0, "longitude": 10.0},
+                "modalita_accesso": {
+                    "blocks": {
+                        text_uuid: {
+                            "@type": "text",
+                            "text": {"blocks": [{"text": "Test", "type": "paragraph"}]},
+                        }
+                    },
+                    "blocks_layout": {"items": [text_uuid]},
+                },
+            },
+        )
+        self.assertEqual(response.status_code, 204)
+        # TODO: i dati vanno verificati con una chiamata alla api_session
+        # self.assertEqual(venue.geolocation.longitude, 10.0)
+        # self.assert ... (venue.modalita_accesso)
 
     def test_venue_services(self):
         response = self.api_session.get(self.venue.absolute_url() + "?fullobjects")
         self.assertTrue(
             response.json()["venue_services"][0]["@id"],
             self.service.absolute_url(),
         )
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_modulo.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_modulo.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_news.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_news.py`

 * *Files 26% similar despite different names*

```diff
@@ -8,22 +8,24 @@
 )
 from plone import api
 from plone.app.testing import setRoles
 from plone.app.testing import SITE_OWNER_NAME
 from plone.app.testing import SITE_OWNER_PASSWORD
 from plone.app.testing import TEST_USER_ID
 from plone.restapi.testing import RelativeSession
+from uuid import uuid4
 
 import json
 import transaction
 import unittest
 
 
 class TestNews(unittest.TestCase):
     layer = DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING
+    maxDiff = None
 
     def setUp(self):
         """Custom shared utility setup for tests."""
         self.portal = self.layer["portal"]
 
     def test_behaviors_enabled_for_news(self):
         portal_types = api.portal.get_tool(name="portal_types")
@@ -38,19 +40,20 @@
                 "plone.excludefromnavigation",
                 "plone.relateditems",
                 "plone.leadimage",
                 "plone.versioning",
                 "plone.locking",
                 "volto.preview_image",
                 "design.plone.contenttypes.behavior.news",
-                "design.plone.contenttypes.behavior.argomenti",
+                "design.plone.contenttypes.behavior.argomenti_news",
                 "plone.constraintypes",
                 "plone.textindexer",
                 "plone.translatable",
                 "kitconcept.seo",
+                "collective.taxonomy.generated.tipologia_notizia",
             ),
         )
 
     def test_news_item_ct_title(self):
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertEqual("Notizie e comunicati stampa", portal_types["News Item"].title)
 
@@ -59,15 +62,14 @@
         self.assertEqual(
             sorted(("Image", "File", "Link", "Document")),
             sorted(portal_types["News Item"].allowed_content_types),
         )
 
 
 class TestNewsApi(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
         self.portal_url = self.portal.absolute_url()
@@ -93,47 +95,122 @@
         self.api_session.close()
 
     def test_newsitem_required_fields(self):
         response = self.api_session.post(
             self.portal_url, json={"@type": "News Item", "title": "Foo"}
         )
 
-        self.assertEqual(400, response.status_code)
+        self.assertEqual(response.status_code, 400)
         message = response.json()["message"]
-        self.assertIn("tipologia_notizia", message)
+        # TODO: anche `tipologia_notizia` è obbligatorio ?
+        # self.assertIn("tipologia_notizia", message)
+        self.assertIn("descrizione_estesa", message)
 
+        text_uuid = str(uuid4())
         response = self.api_session.post(
             self.portal_url,
             json={
                 "@type": "News Item",
                 "title": "Foo",
-                "tipologia_notizia": "foo",
+                # TODO: se la tipologia non è nel vocabolario della
+                # tassonomia, il server restituisce un errore 500
+                # "tipologia_notizia": "foo",
+                "tipologia_notizia": "avviso",
                 "a_cura_di": self.document.UID(),
+                # campo obbligatorio
+                "description": "Test",
+                # campo obbligatorio
+                "descrizione_estesa": {
+                    "blocks": {
+                        text_uuid: {
+                            "@type": "text",
+                            "text": {"blocks": [{"text": "Test", "type": "paragraph"}]},
+                        },
+                    },
+                    "blocks_layout": {"items": [text_uuid]},
+                },
             },
         )
-        self.assertEqual(201, response.status_code)
+        self.assertEqual(response.status_code, 201)
 
     def test_newsitem_substructure_created(self):
-        self.api_session.post(
+        text_uuid = str(uuid4())
+        response = self.api_session.post(
             self.portal_url,
             json={
                 "@type": "News Item",
                 "title": "Foo",
-                "tipologia_notizia": "foo",
+                # TODO: se la tipologia non è nel vocabolario della
+                # tassonomia, il server restituisce un errore 500
+                # "tipologia_notizia": "foo",
+                "tipologia_notizia": "avviso",
                 "a_cura_di": self.document.UID(),
+                # campo obbligatorio
+                "description": "Test",
+                # campo obbligatorio
+                "descrizione_estesa": {
+                    "blocks": {
+                        text_uuid: {
+                            "@type": "text",
+                            "text": {"blocks": [{"text": "Test", "type": "paragraph"}]},
+                        },
+                    },
+                    "blocks_layout": {"items": [text_uuid]},
+                },
             },
         )
+        self.assertEqual(response.status_code, 201)
+
+        response = self.api_session.get(
+            f"{self.portal_url}/foo", params={"fullobjects": 1}
+        )
+        self.assertEqual(response.status_code, 200)
+        news = response.json()
 
+        self.assertEqual(
+            set([i["id"] for i in news["items"]]),
+            set(["multimedia", "documenti-allegati"]),
+        )
+        self.assertEqual(news["description"], "Test")
+        self.assertIn(
+            '"text": "Test"',
+            json.dumps(news["descrizione_estesa"]),
+        )
+
+        # self.assertEqual(news["multimedia"].portal_type, "Document")
+        # self.assertEqual(news["multimedia"].constrain_types_mode, 1)
+        # self.assertEqual(news["multimedia"].locally_allowed_types, ("Link", "Image"))
+
+        # self.assertEqual(news["documenti-allegati"].portal_type, "Document")
+        # self.assertEqual(news["documenti-allegati"].constrain_types_mode, 1)
+        # self.assertEqual(
+        #     news["documenti-allegati"].locally_allowed_types, ("File", "Image")
+        # )
+
+    def test_cant_patch_news_that_has_no_required_fields(self):
+        news = api.content.create(container=self.portal, type="News Item", title="Foo")
         transaction.commit()
-        news = self.portal["foo"]
+        resp = self.api_session.patch(
+            news.absolute_url(),
+            json={
+                "title": "Foo modified",
+            },
+        )
+        self.assertEqual(resp.status_code, 400)
+        self.assertIn("La descrizione è obbligatoria", resp.json()["message"])
 
-        self.assertEqual(["multimedia", "documenti-allegati"], news.keys())
+    def test_can_sort_news_that_has_no_required_fields(self):
+        news = api.content.create(container=self.portal, type="News Item", title="News")
+        transaction.commit()
 
-        self.assertEqual(news["multimedia"].portal_type, "Document")
-        self.assertEqual(news["multimedia"].constrain_types_mode, 1)
-        self.assertEqual(news["multimedia"].locally_allowed_types, ("Link", "Image"))
+        self.assertEqual(self.document, self.portal.listFolderContents()[0])
+        self.assertEqual(news, self.portal.listFolderContents()[1])
 
-        self.assertEqual(news["documenti-allegati"].portal_type, "Document")
-        self.assertEqual(news["documenti-allegati"].constrain_types_mode, 1)
-        self.assertEqual(
-            news["documenti-allegati"].locally_allowed_types, ("File", "Image")
+        resp = self.api_session.patch(
+            self.portal_url,
+            json={"ordering": {"delta": -1, "obj_id": news.getId()}},
         )
+        transaction.commit()
+
+        self.assertEqual(resp.status_code, 204)
+        self.assertEqual(self.document, self.portal.listFolderContents()[1])
+        self.assertEqual(news, self.portal.listFolderContents()[0])
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_pagina_argomento.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_pagina_argomento.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_ct_unita_organizzativa.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_ct_unita_organizzativa.py`

 * *Files 8% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 import unittest
 
 
 class TestUO(unittest.TestCase):
     """Test that design.plone.contenttypes is properly installed."""
 
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
+    maxDiff = None
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
 
@@ -103,38 +104,33 @@
                 "plone.publication",
                 "plone.categorization",
                 "plone.basic",
                 "plone.locking",
                 "plone.leadimage",
                 "volto.preview_image",
                 "plone.relateditems",
-                "design.plone.contenttypes.behavior.address_uo",
-                "design.plone.contenttypes.behavior.geolocation_uo",
+                # "design.plone.contenttypes.behavior.address_uo",
+                # "design.plone.contenttypes.behavior.geolocation_uo",
                 "design.plone.contenttypes.behavior.contatti_uo",
                 "design.plone.contenttypes.behavior.argomenti",
                 "plone.textindexer",
                 "design.plone.contenttypes.behavior.additional_help_infos",
                 "plone.translatable",
                 "kitconcept.seo",
                 "plone.versioning",
+                "collective.taxonomy.generated.tipologia_organizzazione",
             ),
         )
 
     def test_uo_ct_title(self):
         portal_types = api.portal.get_tool(name="portal_types")
         self.assertEqual(
             "Unita Organizzativa", portal_types["UnitaOrganizzativa"].title
         )
 
-    def test_uo_service_related_news(self):
-        response = self.api_session.get(self.uo.absolute_url() + "?fullobjects")
-        self.assertTrue(
-            response.json()["related_news"][0]["@id"], self.news.absolute_url()
-        )
-
     def test_uo_service_related_service_show_only_services(self):
         response = self.api_session.get(self.uo.absolute_url() + "?fullobjects")
         self.assertEqual(
             len(response.json()["servizi_offerti"]),
             1,
         )
         self.assertTrue(
@@ -156,15 +152,15 @@
             "pec",
             "web",
             "riferimento_telefonico_struttura",
             "riferimento_mail_struttura",
             "riferimento_pec_struttura",
         ]
         for field in fields:
-            self.assertEqual(sede[field], getattr(self.luogo, field, ""))
+            self.assertEqual(sede[field], getattr(self.luogo, field, None))
 
     def test_uo_location_indexer_populated(self):
         pc = api.portal.get_tool(name="portal_catalog")
         self.assertEqual((self.luogo.UID(),), pc.uniqueValuesFor("uo_location"))
 
         # create another uo and a venue
         luogo_bis = api.content.create(
@@ -209,37 +205,41 @@
         self.assertIn(luogo_bis.UID(), vocabulary)
         self.assertEqual(len(vocabulary), 2)
         self.assertEqual(vocabulary.getTerm(self.luogo.UID()).title, self.luogo.Title())
         self.assertEqual(vocabulary.getTerm(luogo_bis.UID()).title, luogo_bis.Title())
 
     def test_do_not_show_parent_uo_if_not_present(self):
         response = self.api_session.get(self.uo.absolute_url())
+        self.assertEqual(response.status_code, 200)
         uo_parent = response.json()["uo_parent"]
 
         self.assertIsNone(uo_parent)
 
     def test_show_parent_uo_if_present(self):
         response = self.api_session.get(self.uo_child.absolute_url())
+        self.assertEqual(response.status_code, 200)
         uo_parent = response.json()["uo_parent"]
 
         self.assertIsNotNone(uo_parent)
         self.assertEqual(uo_parent["id"], self.uo.getId())
         self.assertEqual(uo_parent["zip_code"], self.uo.zip_code)
         self.assertEqual(uo_parent["city"], self.uo.city)
         self.assertEqual(uo_parent["contact_info"], self.uo.contact_info)
         self.assertEqual(uo_parent["street"], self.uo.street)
 
     def test_do_not_show_children_uo_if_not_present(self):
         response = self.api_session.get(self.uo_child.absolute_url())
+        self.assertEqual(response.status_code, 200)
         uo_children = response.json()["uo_children"]
 
         self.assertEqual(uo_children, [])
 
     def test_show_children_uo_if_present(self):
         response = self.api_session.get(self.uo.absolute_url())
+        self.assertEqual(response.status_code, 200)
         uo_children = response.json()["uo_children"]
 
         self.assertEqual(len(uo_children), 1)
         self.assertEqual(uo_children[0]["id"], self.uo_child.getId())
         self.assertEqual(uo_children[0]["zip_code"], self.uo_child.zip_code)
         self.assertEqual(uo_children[0]["city"], self.uo_child.city)
         self.assertEqual(uo_children[0]["contact_info"], self.uo_child.contact_info)
@@ -251,12 +251,44 @@
 
         self.service.dove_rivolgersi = [RelationValue(self.intids.getId(self.uo))]
 
         self.service.reindexObject()
         transaction.commit()
 
         response = self.api_session.get(self.uo.absolute_url())
-
+        self.assertEqual(response.status_code, 200)
         self.assertIn(
             self.service.absolute_url(),
             [i["@id"] for i in response.json()["prestazioni"]],
         )
+
+    def test_cant_patch_uo_that_has_no_required_fields(self):
+        uo = api.content.create(
+            container=self.portal, type="UnitaOrganizzativa", title="Foo"
+        )
+        commit()
+        resp = self.api_session.patch(
+            uo.absolute_url(),
+            json={
+                "title": "Foo modified",
+            },
+        )
+        self.assertEqual(resp.status_code, 400)
+        self.assertIn("La descrizione è obbligatoria", resp.json()["message"])
+
+    def test_can_sort_uo_that_has_no_required_fields(self):
+        uo = api.content.create(
+            container=self.portal, type="UnitaOrganizzativa", title="Foo"
+        )
+        commit()
+        self.assertEqual(self.bando, self.portal.listFolderContents()[-2])
+        self.assertEqual(uo, self.portal.listFolderContents()[-1])
+
+        resp = self.api_session.patch(
+            self.portal_url,
+            json={"ordering": {"delta": -1, "obj_id": uo.getId()}},
+        )
+        commit()
+
+        self.assertEqual(resp.status_code, 204)
+        self.assertEqual(self.bando, self.portal.listFolderContents()[-1])
+        self.assertEqual(uo, self.portal.listFolderContents()[-2])
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_move_news_items_view.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_move_news_items_view.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,51 +1,52 @@
-from plone.app.testing import setRoles
-from plone.app.testing import TEST_USER_ID
-from plone import api
-
+# -*- coding: utf-8 -*-
 from design.plone.contenttypes.testing import (
     DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING,
 )
+from plone import api
+from plone.app.testing import setRoles
+from plone.app.testing import TEST_USER_ID
 
 import unittest
 
 
 class MoveNewsItemView(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
+        # default values are set in italian
+        self.request["LANGUAGE"] = "it"
         self.view = api.content.get_view(
             "move_news_items", context=self.portal, request=self.request
         )
 
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
 
         self.news_container = api.content.create(
             type="Folder",
             title="News container",
             container=self.portal,
         )
         self.news_item = api.content.create(
             type="News Item",
             title="news item",
-            tipologia_notizia="Notizia",
+            tipologia_notizia="notizia",
             container=self.portal,
         )
         self.news_item1 = api.content.create(
             type="News Item",
             title="news item1",
-            tipologia_notizia="Notizia",
+            tipologia_notizia="notizia",
             container=self.news_container,
         )
 
     def test_news_result(self):
-        self.view.request.form["news_type"] = "Notizia"
+        self.view.request.form["news_type"] = "notizia"
 
         result = self.view.news_results()
 
         self.assertIn(self.news_item.UID(), [i.UID for i in result])
         self.assertIn(self.news_item1.UID(), [i.UID for i in result])
 
     def test_move_data(self):
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_relateditems_with_dates.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_relateditems_with_dates.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,14 @@
 from zope.component import getUtility
 from zope.intid.interfaces import IIntIds
 
 import unittest
 
 
 class VocabulariesControlpanelTest(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
 
@@ -106,15 +105,14 @@
         # event
         self.assertIn("start", relatedItems[2])
         self.assertIn("end", relatedItems[2])
 
     def test_api_do_not_return_related_items_with_effective_date_in_future_for_anon(
         self,
     ):
-
         present = api.content.create(
             container=self.portal, type="Document", title="present"
         )
         future = api.content.create(
             container=self.portal, type="Document", title="future"
         )
         present.setEffectiveDate(DateTime())
@@ -143,20 +141,20 @@
 
     def test_api_do_not_return_related_items_with_effective_date_in_future_for_users_that_cant_edit_context(  # noqa
         self,
     ):
         api.user.create(
             email="foo@example.com",
             username="foo",
-            password="secret",
+            password="secret!!!",
         )
 
         api_session = RelativeSession(self.portal_url)
         api_session.headers.update({"Accept": "application/json"})
-        api_session.auth = ("foo", "secret")
+        api_session.auth = ("foo", "secret!!!")
 
         present = api.content.create(
             container=self.portal, type="Document", title="present"
         )
         future = api.content.create(
             container=self.portal, type="Document", title="future"
         )
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_settings_controlpanel_api.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_settings_controlpanel_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -8,15 +8,14 @@
 from plone.app.testing import TEST_USER_ID
 from plone.restapi.testing import RelativeSession
 
 import unittest
 
 
 class SettingsControlpanelTest(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.portal_url = self.portal.absolute_url()
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_setup.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_setup.py`

 * *Files 22% similar despite different names*

```diff
@@ -28,15 +28,24 @@
         if get_installer:
             self.installer = get_installer(self.portal, self.layer["request"])
         else:
             self.installer = api.portal.get_tool("portal_quickinstaller")
 
     def test_product_installed(self):
         """Test if design.plone.contenttypes is installed."""
-        self.assertTrue(self.installer.isProductInstalled("design.plone.contenttypes"))
+        if hasattr(self.installer, "is_product_installed"):
+            # Plone 6
+            self.assertTrue(
+                self.installer.is_product_installed("design.plone.contenttypes")
+            )
+        else:
+            # Plone 5
+            self.assertTrue(
+                self.installer.isProductInstalled("design.plone.contenttypes")
+            )
 
     def test_browserlayer(self):
         """Test that IDesignPloneContenttypesLayer is registered."""
         from design.plone.contenttypes.interfaces import IDesignPloneContenttypesLayer
         from plone.browserlayer import utils
 
         self.assertIn(IDesignPloneContenttypesLayer, utils.registered_layers())
@@ -45,31 +54,44 @@
         value = api.portal.get_registry_record(
             "show_modified_default", interface=IDesignPloneSettings
         )
         self.assertTrue(value)
 
 
 class TestUninstall(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         if get_installer:
             self.installer = get_installer(self.portal, self.layer["request"])
         else:
             self.installer = api.portal.get_tool("portal_quickinstaller")
         roles_before = api.user.get_roles(TEST_USER_ID)
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
-        self.installer.uninstallProducts(["design.plone.contenttypes"])
+        if hasattr(self.installer, "uninstall_product"):
+            # Plone 6
+            self.installer.uninstall_product("design.plone.contenttypes")
+        else:
+            # Plone 5
+            self.installer.uninstallProducts(["design.plone.contenttypes"])
         setRoles(self.portal, TEST_USER_ID, roles_before)
 
     def test_product_uninstalled(self):
         """Test if design.plone.contenttypes is cleanly uninstalled."""
-        self.assertFalse(self.installer.isProductInstalled("design.plone.contenttypes"))
+        if hasattr(self.installer, "is_product_installed"):
+            # Plone 6
+            self.assertFalse(
+                self.installer.is_product_installed("design.plone.contenttypes")
+            )
+        else:
+            # Plone 5
+            self.assertFalse(
+                self.installer.isProductInstalled("design.plone.contenttypes")
+            )
 
     def test_browserlayer_removed(self):
         """Test that IDesignPloneContenttypesLayer is removed."""
         from design.plone.contenttypes.interfaces import IDesignPloneContenttypesLayer
         from plone.browserlayer import utils
 
         self.assertNotIn(IDesignPloneContenttypesLayer, utils.registered_layers())
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_summary_serializer.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_summary_serializer.py`

 * *Files 10% similar despite different names*

```diff
@@ -3,28 +3,26 @@
     DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING,
 )
 from plone import api
 from plone.app.testing import setRoles
 from plone.app.testing import SITE_OWNER_NAME
 from plone.app.testing import SITE_OWNER_PASSWORD
 from plone.app.testing import TEST_USER_ID
-from plone.restapi.interfaces import ISerializeToJson
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from plone.restapi.testing import RelativeSession
 from transaction import commit
 from z3c.relationfield import RelationValue
 from zope.component import getMultiAdapter
 from zope.component import getUtility
 from zope.intid.interfaces import IIntIds
 
 import unittest
 
 
 class SummarySerializerTest(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
         self.portal_url = self.portal.absolute_url()
@@ -40,15 +38,14 @@
         )
         commit()
 
     def tearDown(self):
         self.api_session.close()
 
     def test_has_children_returned_in_get_content(self):
-
         api.content.create(container=self.document, type="Document", title="empty")
         api.content.create(container=self.document, type="Document", title="filled")
 
         api.content.create(
             container=self.document["filled"], type="Document", title="Example"
         )
         commit()
@@ -61,15 +58,14 @@
         self.assertEqual(len(items), 2)
         self.assertEqual(items[0]["title"], "empty")
         self.assertFalse(items[0]["has_children"])
         self.assertEqual(items[1]["title"], "filled")
         self.assertTrue(items[1]["has_children"])
 
     def test_has_children_not_returned_in_searches(self):
-
         api.content.create(container=self.document, type="Document", title="empty")
         api.content.create(container=self.document, type="Document", title="filled")
 
         api.content.create(
             container=self.document["filled"], type="Document", title="Example"
         )
         commit()
@@ -84,15 +80,14 @@
         self.assertEqual(len(items), 2)
         self.assertEqual(items[0]["title"], "empty")
         self.assertNotIn("has_children", items[0])
         self.assertEqual(items[1]["title"], "filled")
         self.assertNotIn("has_children", items[1])
 
     def test_has_children_not_returned_in_backend_serialization(self):
-
         empty = api.content.create(
             container=self.document, type="Document", title="empty"
         )
         filled = api.content.create(
             container=self.document, type="Document", title="filled"
         )
 
@@ -146,78 +141,81 @@
 
         self.assertEqual(len(items), 1)
         self.assertEqual(items[0]["remoteUrl"], self.document.absolute_url())
 
         serializer = getMultiAdapter((link, self.request), ISerializeToJsonSummary)()
         self.assertEqual(serializer["remoteUrl"], self.document.absolute_url())
 
-    def test_summary_return_persona_role(self):
-
-        api.content.create(
-            container=self.portal, type="Persona", title="John Doe", ruolo="unknown"
-        )
-        api.content.create(container=self.portal, type="Persona", title="Mario Rossi")
-
-        commit()
-
-        brains = api.content.find(portal_type="Persona", id="mario-rossi")
-        results = getMultiAdapter((brains, self.request), ISerializeToJson)(
-            fullobjects=False
-        )
-
-        self.assertEqual(results["items"][0]["ruolo"], None)
-        self.assertEqual(results["items"][0]["title"], "Mario Rossi")
-
-        brains = api.content.find(portal_type="Persona", id="john-doe")
-        results = getMultiAdapter((brains, self.request), ISerializeToJson)(
-            fullobjects=False
-        )
-
-        self.assertEqual(results["items"][0]["ruolo"], "unknown")
-        self.assertEqual(results["items"][0]["title"], "John Doe")
+    # il campo `ruolo` non è più presente nel tipo Persona
+    # def test_summary_return_persona_role(self):
+    #     api.content.create(
+    #         container=self.portal, type="Persona", title="John Doe", ruolo="unknown"
+    #     )
+    #     api.content.create(container=self.portal, type="Persona", title="Mario Rossi")
+
+    #     commit()
+
+    #     brains = api.content.find(portal_type="Persona", id="mario-rossi")
+    #     results = getMultiAdapter((brains, self.request), ISerializeToJson)(
+    #         fullobjects=False
+    #     )
+
+    #     self.assertEqual(results["items"][0]["ruolo"], None)
+    #     self.assertEqual(results["items"][0]["title"], "Mario Rossi")
+
+    #     brains = api.content.find(portal_type="Persona", id="john-doe")
+    #     results = getMultiAdapter((brains, self.request), ISerializeToJson)(
+    #         fullobjects=False
+    #     )
+
+    #     self.assertEqual(results["items"][0]["ruolo"], "unknown")
+    #     self.assertEqual(results["items"][0]["title"], "John Doe")
+
+    #     # test also with restapi call
+    #     response = self.api_session.get(
+    #         "{}/@search?portal_type=Persona&id=mario-rossi".format(self.portal_url)
+    #     )
+
+    #     result = response.json()
+    #     items = result.get("items", [])
+
+    #     self.assertEqual(items[0]["title"], "Mario Rossi")
+    #     self.assertEqual(items[0]["ruolo"], None)
+
+    #     response = self.api_session.get(
+    #         "{}/@search?portal_type=Persona&id=john-doe".format(self.portal_url)
+    #     )
 
-        # test also with restapi call
-        response = self.api_session.get(
-            "{}/@search?portal_type=Persona&id=mario-rossi".format(self.portal_url)
-        )
-
-        result = response.json()
-        items = result.get("items", [])
-
-        self.assertEqual(items[0]["title"], "Mario Rossi")
-        self.assertEqual(items[0]["ruolo"], None)
+    #     result = response.json()
+    #     items = result.get("items", [])
 
-        response = self.api_session.get(
-            "{}/@search?portal_type=Persona&id=john-doe".format(self.portal_url)
-        )
-
-        result = response.json()
-        items = result.get("items", [])
-
-        self.assertEqual(items[0]["title"], "John Doe")
-        self.assertEqual(items[0]["ruolo"], "unknown")
+    #     self.assertEqual(items[0]["title"], "John Doe")
+    #     self.assertEqual(items[0]["ruolo"], "unknown")
 
     def test_summary_return_design_meta_type(self):
-        news = api.content.create(
+        api.content.create(
             container=self.portal,
             type="News Item",
             title="News",
             tipologia_notizia="foo",
         )
         commit()
 
         response = self.api_session.get("@search?portal_type=News Item")
         result = response.json()
         items = result.get("items", [])
 
-        self.assertEqual(len(items), 1)
-        self.assertEqual(items[0]["design_italia_meta_type"], "foo")
+        # TODO: non basta che `foo` sia una tipologia di notizia, serve che sia presente
+        # anche nella tassonomia delle tipologie di notizia
+
+        # self.assertEqual(len(items), 1)
+        # self.assertEqual(items[0]["design_italia_meta_type"], "foo")
 
-        serializer = getMultiAdapter((news, self.request), ISerializeToJsonSummary)()
-        self.assertEqual(serializer["design_italia_meta_type"], "foo")
+        # serializer = getMultiAdapter((news, self.request), ISerializeToJsonSummary)()
+        # self.assertEqual(serializer["design_italia_meta_type"], "foo")
 
         # other contents return their name
         response = self.api_session.get("@search?UID={}".format(self.document.UID()))
         result = response.json()
         items = result.get("items", [])
 
         self.assertEqual(len(items), 1)
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/tests/test_uo_summary_serializer.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/tests/test_uo_summary_serializer.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,15 +9,14 @@
 from plone.restapi.interfaces import ISerializeToJsonSummary
 from zope.component import getMultiAdapter
 
 import unittest
 
 
 class UOSummarySerializerTest(unittest.TestCase):
-
     layer = DESIGN_PLONE_CONTENTTYPES_API_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.app = self.layer["app"]
         self.portal = self.layer["portal"]
 
     def test_geolocation_injected(self):
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/configure.zcml`

 * *Files 3% similar despite different names*

```diff
@@ -598,64 +598,68 @@
       destination="6010"
       >
     <genericsetup:upgradeStep
         title="Add CTs Incarico and PuntoDiContatto"
         handler=".upgrades.to_6010"
         />
   </genericsetup:upgradeSteps>
+
   <genericsetup:upgradeStep
       title="Update servizio"
       description=""
       profile="design.plone.contenttypes:default"
       source="6010"
       destination="6011"
       handler=".upgrades.to_6011"
       />
+
   <genericsetup:upgradeSteps
       profile="design.plone.contenttypes:default"
       source="6011"
       destination="7001"
       >
     <genericsetup:upgradeStep
         title="Persone: Update for PNRR"
         description="Create Incarichi folder"
-        handler=".upgrades.to_7001"
+        handler=".to_7001.to_7001"
         />
     <genericsetup:upgradeStep
         title="Persone: Update for PNRR"
         description="Create Incarichi folder"
-        handler=".upgrades.create_incarichi_folder"
+        handler=".to_7001.create_incarichi_folder"
         />
     <genericsetup:upgradeStep
         title="Persone: Update for PNRR"
         description="Create incarichi objects"
-        handler=".upgrades.create_incarico_for_persona"
+        handler=".to_7001.create_incarico_for_persona"
         />
     <genericsetup:upgradeStep
         title="Persone: Update for PNRR"
         description="Create PDC objects"
-        handler=".upgrades.create_pdc"
+        handler=".to_7001.create_pdc"
         />
   </genericsetup:upgradeSteps>
+
   <genericsetup:upgradeSteps
       profile="design.plone.contenttypes:default"
       source="7001"
       destination="7002"
       >
     <genericsetup:upgradeStep
         title="Persone: Update for PNRR - migrazione Tassonomie"
         description="Migrazione delle tassonomie sui contenttypes"
-        handler=".upgrades.update_taxonomies"
+        handler=".to_7002.update_taxonomies"
         />
     <genericsetup:upgradeStep
         title="Persone: Update for PNRR - migrazione Tassonomie"
         description="Migrazione delle tassonomie sui blocchi"
-        handler=".upgrades.update_taxonomies_on_blocks"
+        handler=".to_7002.update_taxonomies_on_blocks"
         />
   </genericsetup:upgradeSteps>
+
   <genericsetup:upgradeSteps
       profile="design.plone.contenttypes:default"
       source="7002"
       destination="7003"
       >
     <genericsetup:upgradeStep
         title="Persone: Update for PNRR - pulizia contact_info delle UO"
@@ -664,19 +668,80 @@
         />
     <genericsetup:upgradeStep
         title="Argomenti: Reintrodotto indice per uid"
         description=""
         handler=".upgrades.readd_tassonomia_argomenti_uid"
         />
   </genericsetup:upgradeSteps>
+
   <genericsetup:upgradeSteps
       profile="design.plone.contenttypes:default"
       source="7003"
       destination="7004"
       >
     <genericsetup:upgradeStep
         title="Persone: update ruolo indexing"
         description=""
         handler=".upgrades.update_ruolo_indexing"
         />
   </genericsetup:upgradeSteps>
+
+  <genericsetup:upgradeSteps
+      profile="design.plone.contenttypes:default"
+      source="7004"
+      destination="7005"
+      >
+    <genericsetup:upgradeStep
+        title="Fix eventual taxonomy mess"
+        description=""
+        handler=".upgrades.fix_ctaxonomy_indexes_and_metadata"
+        />
+  </genericsetup:upgradeSteps>
+
+  <genericsetup:upgradeSteps
+      profile="design.plone.contenttypes:default"
+      source="7005"
+      destination="7006"
+      >
+    <genericsetup:upgradeStep
+        title="Persone: update ruolo indexing"
+        description=""
+        handler=".upgrades.update_types"
+        />
+  </genericsetup:upgradeSteps>
+
+  <genericsetup:upgradeSteps
+      profile="design.plone.contenttypes:default"
+      source="7006"
+      destination="7007"
+      >
+    <genericsetup:upgradeStep
+        title="Evento: update patrocinato da"
+        description=""
+        handler=".upgrades.update_patrocinato_da"
+        />
+  </genericsetup:upgradeSteps>
+
+  <genericsetup:upgradeSteps
+      profile="design.plone.contenttypes:default"
+      source="7007"
+      destination="7008"
+      >
+
+    <genericsetup:upgradeStep
+        title="Evento: update folder for gallery"
+        description=""
+        handler=".upgrades.update_folder_for_gallery"
+        />
+  </genericsetup:upgradeSteps>
+
+  <genericsetup:upgradeSteps
+      profile="design.plone.contenttypes:default"
+      source="7008"
+      destination="7009"
+      >
+    <genericsetup:upgradeStep
+        title="Add plone.excludefromnavigation to Venue"
+        handler=".upgrades.to_7009"
+        />
+  </genericsetup:upgradeSteps>
 </configure>
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/draftjs_converter.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/draftjs_converter.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/upgrades/upgrades.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/upgrades/upgrades.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,27 +1,23 @@
 # -*- coding: utf-8 -*-
 from Acquisition import aq_base
-from collective.taxonomy.interfaces import ITaxonomy
 from collective.volto.blocksfield.field import BlocksField
 from copy import deepcopy
 from design.plone.contenttypes.controlpanels.settings import IDesignPloneSettings
 from design.plone.contenttypes.setuphandlers import remove_blocks_behavior
 from design.plone.contenttypes.upgrades.draftjs_converter import to_draftjs
+from design.plone.contenttypes.utils import create_default_blocks
 from plone import api
 from plone.app.textfield.value import RichTextValue
 from plone.app.upgrade.utils import installOrReinstallProduct
-from plone.base.utils import get_installer
 from plone.dexterity.utils import iterSchemata
-from plone.namedfile.file import NamedBlobFile
 from Products.CMFPlone.interfaces import ISelectableConstrainTypes
-from Products.CMFPlone.utils import safe_hasattr
 from redturtle.bandi.interfaces.settings import IBandoSettings
 from transaction import commit
 from z3c.relationfield import RelationValue
-from zope.component import getUtilitiesFor
 from zope.component import getUtility
 from zope.event import notify
 from zope.intid.interfaces import IIntIds
 from zope.lifecycleevent import ObjectModifiedEvent
 from zope.schema import getFields
 
 import json
@@ -91,15 +87,14 @@
                 delattr(item, old)
 
 
 # custom ones #
 
 
 def to_1001(context):
-
     update_types(context)
 
     # cleanup event behaviors
     portal_types = api.portal.get_tool(name="portal_types")
     behaviors = portal_types["Event"].behaviors
     to_remove = [
         "design.plone.contenttypes.behavior.luoghi_correlati",
@@ -120,15 +115,14 @@
         "riferimento_telefonico_luogo": "telefono",
         "riferimento_mail_luogo": "email",
     }
     remap_fields(mapping=mapping)
 
 
 def to_1003(context):
-
     update_types(context)
 
     mapping = {
         "unita_amministrativa_responsabile": "unita_amministrative_responsabili",  # noqa
         "sedi": "sede",
         "contatto_reperibilita": "reperibilita",
         "evento_supportato_da": "supportato_da",
@@ -512,17 +506,14 @@
 
     logger.info("### START CONVERSION TO VOLTO 13: default => simpleCard ###")
 
     def fix_listing(blocks, url):
         for block in blocks.values():
             if block.get("@type", "") == "listing":
                 if block.get("template", False) and not block.get("variation", False):
-                    # import pdb
-
-                    # pdb.set_trace()
                     logger.error("- {}".format(url))
                 if block.get("template", False) and block.get("variation", False):
                     logger.error("- {}".format(url))
                 if block.get("variation", "") == "default":
                     block["variation"] = "simpleCard"
                     logger.info("- {}".format(url))
 
@@ -953,15 +944,14 @@
 
 def to_5400(context):
     logger.info('Remove "volto.blocks" behavior from News Item and Event.')
     remove_blocks_behavior(context)
 
 
 def to_5410(context):
-
     # cleanup Document behaviors
     portal_types = api.portal.get_tool(name="portal_types")
     behaviors = portal_types["Document"].behaviors
     to_remove = [
         "plone.tableofcontents",
     ]
     portal_types["Document"].behaviors = tuple(
@@ -1192,17 +1182,14 @@
             new_pdc = api.content.create(
                 type="PuntoDiContatto",
                 title=f"Punto di Contatto {item.id}",
                 container=item,
                 **kwargs,
             )
             intids = getUtility(IIntIds)
-            # import pdb
-
-            # pdb.set_trace()
             item.contact_info = [RelationValue(intids.getId(new_pdc))]
             fixed_total += 1
             commit()
 
         logger.info(f"Fixing Punto di Contatto for '{portal_type}: DONE")
         logger.info("Updated {} objects".format(fixed_total))
 
@@ -1218,442 +1205,224 @@
     GREEN = "\033[92m"
     ENDC = "\033[0m"
     RED = "\033[91m"
     DARKCYAN = "\033[36m"
     YELLOW = "\033[93m"
 
 
-def to_7001(context):
-
-    installer = get_installer(context=api.portal.get())
-    installer.install_product("eea.api.taxonomy")
-    logger.info(
-        f"{colors.DARKCYAN} eea.api.taxonomy and collective.taxonomy installed {colors.ENDC}"  # noqa
-    )
-    # delete actual index from portal_catalog
-    for index in [
-        "tipologia_notizia",
-        "tipologia_documento",
-        "tipologia_organizzazione",
-    ]:
-        api.portal.get_tool("portal_catalog").delIndex(index)
-
-    context.runImportStepFromProfile(
-        "design.plone.contenttypes:taxonomy", "collective.taxonomy"
-    )
-    for utility_name, utility in list(getUtilitiesFor(ITaxonomy)):
-        utility.updateBehavior(**{"field_prefix": ""})
-        logger.info(
-            f"{colors.DARKCYAN} Change taxonomy prefix for {utility_name} {colors.ENDC}"  # noqa
-        )
-    logger.info(
-        f"{colors.DARKCYAN} design.plone.contentypes taxonomies imported {colors.ENDC}"  # noqa
-    )
-    update_types(context)
-    update_registry(context)
-    update_catalog(context)
-    update_rolemap(context)
-    logger.info(
-        f"{colors.DARKCYAN} Upgraded types, registry, catalog and rolemap {colors.ENDC}"  # noqa
-    )
+# XXX: le prenotazioni non sono necessariamente all'interno del servizio
+# def add_ioprenoto_folder(context):
+#     """Adds PrenotazioniFoldersContainer object to Servizio c.t. object"""
+#     catalog = api.portal.get_tool("portal_catalog")
+#     for servizio in catalog(portal_type="Servizio"):
+#         if not catalog(
+#             portal_type="PrenotazioniFolderContainer", path=servizio.getPath()
+#         ):
+#             container = servizio.getObject()
+#             if "PrenotazioniFolderContainer" in getattr(
+#                 context, "allowedContentTypes", None
+#             ):
+#                 api.content.create(
+#                     type="PrenotazioniFolderContainer",
+#                     title="Cartella delle prenotazioni",
+#                     container=container,
+#                 )
+#             else:
+#                 raise Exception(
+#                     "Can not mirgate so as PrenotazioniFolderContainer is not allowed"
+#                 )
 
 
-def create_incarichi_folder(context):
+def update_uo_contact_info(context):
+    brains = api.portal.get_tool("portal_catalog")(portal_type="UnitaOrganizzativa")
     logger.info(
-        f"{colors.DARKCYAN} Inizio a creare la cartella Incarichi nelle persone {colors.ENDC}"  # noqa
+        f"{colors.DARKCYAN} Inizio la pulzia delle {len(brains)} UO campo contact_info {colors.ENDC}"  # noqa
     )
-    pc = api.portal.get_tool(name="portal_catalog")
-    wftool = api.portal.get_tool(name="portal_workflow")
-    brains = pc({"portal_type": "Persona"})
-    target = {"id": "incarichi", "title": "Incarichi", "contains": ("Incarico",)}
     for brain in brains:
-        persona = brain.getObject()
-        if target["id"] in persona:
+        obj = brain.getObject()
+        if type(obj.contact_info) == dict:
+            del obj.contact_info
             logger.info(
-                f"{colors.YELLOW} {persona.title} contiene già la cartella incarichi {colors.ENDC}"  # noqa
+                f"{colors.GREEN} Modifica della UO senza punto di contatto {colors.ENDC}"  # noqa
             )
-            continue
-        suboject = api.content.create(
-            type="Document", id=target["id"], title=target["title"], container=persona
-        )
-        subobjectConstraints = ISelectableConstrainTypes(suboject)
-        subobjectConstraints.setConstrainTypesMode(1)
-        subobjectConstraints.setLocallyAllowedTypes(target["contains"])
 
-        if api.content.get_state(obj=persona) == "published":
-            wftool.doActionFor(suboject, "publish")
 
-        logger.info(
-            f"{colors.GREEN} Creato la cartella incarichi per {persona.title}{colors.ENDC}"  # noqa
-        )
+def readd_tassonomia_argomenti_uid(context):
     logger.info(
-        f"{colors.DARKCYAN} Finito di creare la cartella Incarichi{colors.ENDC}"
+        f"{colors.DARKCYAN} Aggiungo la tassonomia_argomenti_uid e reindicizzo{colors.ENDC}"  # noqa
     )
+    update_catalog(context)
+    update_registry(context)
+    idxs = ["tassonomia_argomenti_uid", "tassonomia_argomenti"]
+    reindex_catalog(context, idxs)
 
 
-def create_incarico_for_persona(context):
+def update_ruolo_indexing(context):
     logger.info(
-        f"{colors.DARKCYAN} Inizio a creare gli incarichi delle persone {colors.ENDC}"
+        f"{colors.DARKCYAN} Reindex del ruolo nelle persone {colors.ENDC}"  # noqa
     )
-    # intids = getUtility(IIntIds)
-    pc = api.portal.get_tool(name="portal_catalog")
-    wftool = api.portal.get_tool(name="portal_workflow")
-    brains = pc({"portal_type": "Persona"})
-    MAPPING_TIPO = {
-        "Amministrativa": "amministrativo",
-        "Politica": "politico",
-        "Altro tipo": "altro",
-    }
+    idxs = ["ruolo"]
+    pc = api.portal.get_tool("portal_catalog")
+    brains = pc(portal_type="Persona")
     for brain in brains:
-
         persona = brain.getObject()
+        persona.reindexObject(idxs=idxs)
 
-        incarichi_folder = persona["incarichi"]
-
-        if incarichi_folder.values():
-            logger.info(
-                f"{colors.RED}{persona.title} ha già un incarico creato {colors.ENDC}"
-            )  # noqa
-            continue
-
-        if safe_hasattr(persona, "ruolo"):
-            incarico_title = persona.ruolo
-        else:
-            logger.info(
-                f"{colors.RED} Attenzione: {persona.title} non ha un ruolo {colors.ENDC}"  # noqa
-            )
-            incarico_title = f"Incarico di {persona.title}"
 
-        incarico = api.content.create(
-            type="Incarico", title=incarico_title, container=incarichi_folder
-        )
-        # incarico.persona = [RelationValue(intids.getId(persona))]
-        api.relation.create(source=incarico, target=persona, relationship="persona")
-        if safe_hasattr(persona, "organizzazione_riferimento"):
-            incarico.unita_organizzativa = persona.organizzazione_riferimento
-
-        if safe_hasattr(persona, "data_insediamento"):
-            incarico.data_inizio_incarico = persona.data_insediamento
-            incarico.data_insediamento = persona.data_insediamento
-
-        if safe_hasattr(persona, "data_conclusione_incarico"):
-            incarico.data_conclusione_incarico = persona.data_conclusione_incarico
-
-        atto_nomina = None
-        if safe_hasattr(persona, "atto_nomina"):
-            atto_nomina = api.content.create(
-                type="Documento",
-                id="atto-di-nomina",
-                title="Atto di nomina",
-                container=incarico,
-            )
-            atto_nomina.description = f"Atto di nomina di {persona.title} per il ruolo di {incarico_title}"  # noqa
-            atto_nomina.file_correlato = NamedBlobFile(
-                data=persona.atto_nomina.data,
-                filename=persona.atto_nomina.filename,
-                contentType="application/pdf",
-            )
-            atto_nomina.tipologia_documento = ["documento_attivita_politica"]
-            # incarico.atto_nomina = [RelationValue(intids.getId(atto_nomina))]
-            api.relation.create(
-                source=incarico, target=atto_nomina, relationship="atto_nomina"
-            )
+def fix_ctaxonomy_indexes_and_metadata(context):
+    logger.info(f"{colors.DARKCYAN} Fix taxonomy indexes {colors.ENDC}")  # noqa
+    bad_names = [
+        "taxonomy_person_life_events",
+        "taxonomy_business_events",
+        "taxonomy_temi_dataset",
+        "taxonomy_tipologia_documenti_albopretorio",
+        "taxonomy_tipologia_documento",
+        "taxonomy_tipologia_evento",
+        "taxonomy_tipologia_frequenza_aggiornamento",
+        "taxonomy_tipologia_incarico",
+        "taxonomy_tipologia_licenze",
+        "taxonomy_tipologia_luogo",
+        "taxonomy_tipologia_notizia",
+        "taxonomy_tipologia_organizzazione",
+        "taxonomy_tipologia_pdc",
+        "taxonomy_tipologia_stati_pratica",
+    ]
 
-        if safe_hasattr(persona, "tipologia_persona"):
-            incarico.tipologia_incarico = MAPPING_TIPO[persona.tipologia_persona]
+    good_names = [name.replace("taxonomy_", "") for name in bad_names]
+    catalog = api.portal.get_tool(name="portal_catalog")
+    catalog_metadata = catalog.schema()
+    catalog_indexes = catalog.indexes()
 
-        # persona.incarichi_persona = [RelationValue(intids.getId(incarico))]
-        api.relation.create(
-            source=persona, target=incarico, relationship="incarichi_persona"
-        )
+    for name in bad_names:
+        # metadata
+        if name in catalog_metadata:
+            catalog.delColumn(name)
+            logger.info(f"{colors.GREEN} Remove {name} from metadata {colors.ENDC}")
+
+        # indexes
+        if name in catalog_indexes:
+            catalog.delIndex(name)
+            logger.info(f"{colors.GREEN} Remove {name} from indexes {colors.ENDC}")
 
-        if api.content.get_state(obj=persona) == "published":
-            wftool.doActionFor(incarico, "publish")
-            wftool.doActionFor(incarico["compensi-file"], "publish")
-            wftool.doActionFor(incarico["importi-di-viaggio-e-o-servizi"], "publish")
-            if atto_nomina:
-                wftool.doActionFor(atto_nomina, "publish")
+    context.runImportStepFromProfile(
+        "design.plone.contenttypes:taxonomy", "collective.taxonomy"
+    )
+    brains = catalog(
+        portal_type=[
+            "News Item",
+            "Event",
+            "Venue",
+            "Servizio",
+            "Documento",
+            "Dataset",
+            "UnitaOrganizzativa",
+            "Incarico",
+            "Pratica",
+        ]
+    )
+    logger.info(f"{colors.GREEN} Reindex contents with taxonomies {colors.ENDC}")
+    for brain in brains:
+        obj = brain.getObject()
+        obj.reindexObject(idxs=good_names)
+    logger.info(f"{colors.GREEN} End of update {colors.ENDC}")
 
-        logger.info(f"{colors.GREEN} Creato incarico per {persona.title}{colors.ENDC}")
 
+def update_patrocinato_da(self):
+    EMPTY_BLOCKS_FIELD = {"blocks": {}, "blocks_layout": {"items": []}}
     logger.info(
-        f"{colors.DARKCYAN} Finito di creare gli incarichi delle persone{colors.ENDC}"
+        f"{colors.DARKCYAN} Change patrocinato_da field in events {colors.ENDC}"
     )
-
-
-def create_pdc(context):
-    portal_types = ["UnitaOrganizzativa", "Persona", "Event", "Venue"]
-    MAPPINGS = {
-        "Persona": {
-            "telefono": "telefono",
-            "fax": "fax",
-            "email": "email",
-            "pec": "pec",
-        },
-        "UnitaOrganizzativa": {
-            "telefono": "telefono",
-            "fax": "fax",
-            "email": "email",
-            "pec": "pec",
-            "web": "url",
-        },
-        "Event": {
-            "telefono": "telefono",
-            "fax": "fax",
-            "email": "email",
-            "web": "url",
-        },
-        "Venue": {
-            "telefono": "telefono",
-            "fax": "fax",
-            "email": "email",
-            "pec": "pec",
-            "web": "url",
-        },
-    }
-
-    def migrated_contact_info(source):
-        # we check if we have attribute, if it's a list and no more a json (block field)
-        # finally we check if we have at least a value.
-        if (
-            safe_hasattr(source, "contact_info")
-            and type(obj.contact_info) == list
-            and len(obj.contact_info) > 0
-        ):
-            return True
-
     pc = api.portal.get_tool(name="portal_catalog")
-    wftool = api.portal.get_tool(name="portal_workflow")
-    portal = api.portal.get()
-    punti_contatto_id = "punti-di-contatto"
-    punti_contatto_title = "Punti di contatto"
-    if "punti-di-contatto" not in portal:
-        punti_contatto = api.content.create(
-            type="Document",
-            id=punti_contatto_id,
-            title=punti_contatto_title,
-            container=portal,
-        )
-        punti_contatto.exclude_from_nav = True
-        punti_contatto.reindexObject()
-        wftool.doActionFor(punti_contatto, "publish")
-        logger.info(
-            f"{colors.GREEN} Creato cartella punti di contatto nella radice del portal{colors.ENDC}"  # noqa
-        )
-    else:
-        punti_contatto = portal[punti_contatto_id]
-
-    for portal_type in portal_types:
-        brains = pc(**{"portal_type": portal_type})
-        logger.info(
-            f"{colors.YELLOW} Stiamo per creare i PDC per {len(brains)} oggetti di tipo {portal_type}{colors.ENDC}"  # noqa
-        )
-        for brain in brains:
-            obj = brain.getObject()
-            mapping = MAPPINGS[portal_type]
-            data = []
-            for field in mapping:
-                field_value = getattr(obj, field, None)
-                if not field_value:
-                    continue
-                if type(field_value) != list:
-                    # in some case we have a f*****g list
-                    field_value = [
-                        field_value,
-                    ]
-                for value in field_value:
-                    data.append({"pdc_type": mapping[field], "pdc_value": value})
-
-            if not data:
-                continue
-
-            if not migrated_contact_info(obj):
-                obj.old_contact_info = obj.contact_info
-                if obj.portal_type == "UnitaOrganizzativa":
-                    del obj.contact_info
-            else:
-                logger.info(
-                    f"{colors.RED} Esiste già un punto di contatto per {obj.title}({obj.absolute_url()}){colors.ENDC}"  # noqa
-                )
-                continue
-
-            pdc = api.content.create(
-                type="PuntoDiContatto",
-                title=f"Punto di contatto per: {obj.title}",
-                container=punti_contatto,
-            )
-
-            api.relation.create(source=obj, target=pdc, relationship="contact_info")
-
-            pdc.value_punto_contatto = data
-            # publish
-            wftool.doActionFor(pdc, "publish")
-
+    for brain in pc(portal_type="Event"):
+        obj = brain.getObject()
+        patrocinato_da = getattr(obj, "patrocinato_da")
+        if patrocinato_da == EMPTY_BLOCKS_FIELD:
             logger.info(
-                f"{colors.GREEN} Creato il punto di contatto per {obj.title}({obj.absolute_url()}){colors.ENDC}"  # noqa
+                f"{colors.YELLOW} Nessuna informazione da modificare{colors.ENDC}"
             )
+            continue
+        url = obj.absolute_url()
+        logger.info(f"{colors.GREEN} patrocinato_da ({url}){colors.ENDC}")
 
-
-TYPE_TO_TAXONOMIES_MAPPING = {
-    "News Item": {
-        "tipologia_notizia": {
-            "it": {
-                "Avviso": "avviso",
-                "Comunicato stampa": "comunicato_stampa",
-                "Novit\u00e0": "notizia",
-            }
-        }
-    },
-    "Documento": {
-        "tipologia_documento": {
-            "it": {
-                "Accordi tra enti": "accordo_tra_enti",
-                "Atti normativi": "atto_normativo",
-                "Dataset": "Dataset",
-                "Documenti (tecnici) di supporto": "documento_tecnico_di_supporto",
-                "Documenti albo pretorio": "documenti_albo_pretorio",
-                "Documenti attivit\u00e0 politica": "documento_attivita_politica",
-                "Documenti funzionamento interno": "documento_funzionamento_interno",
-                "Istanze": "istanza",
-                "Modulistica": "modulistica",
-            }
-        }
-    },
-    "UnitaOrganizzativa": {
-        "tipologia_organizzazione": {
-            "it": {
-                "Politica": "struttura_politica",
-                "Amministrativa": "struttura_amministrativa",
-                "Altro": "altra_struttura",
-            }
-        }
-    },
-}
-
-TAXONOMIES_MAPPING = {}
-for portal_type in TYPE_TO_TAXONOMIES_MAPPING:
-    for TAXONOMY in TYPE_TO_TAXONOMIES_MAPPING[portal_type]:
-        TAXONOMIES_MAPPING[TAXONOMY] = TYPE_TO_TAXONOMIES_MAPPING[portal_type][TAXONOMY]
-
-
-def update_taxonomies(context):
-    # delete actual index from portal_catalog
-    logger.info(
-        f"{colors.DARKCYAN} Migrazione delle tassonomie dai vecchi ai nuovi valori {colors.ENDC}"  # noqa
-    )
-    pc = api.portal.get_tool("portal_catalog")
-    for portal_type in TYPE_TO_TAXONOMIES_MAPPING:
-        brains = pc(**{"portal_type": portal_type})
-        logger.info(
-            f"{colors.DARKCYAN} Modifica delle tassonomie per {len(brains)} {portal_type}{colors.ENDC}"  # noqa
+        setattr(
+            obj,
+            "patrocinato_da",
+            {
+                "blocks": {
+                    "d252fe92-ce88-4866-b77d-501e7275cfc0": {
+                        "@type": "text",
+                        "text": {
+                            "blocks": [
+                                {
+                                    "data": {},
+                                    "depth": 0,
+                                    "entityRanges": [],
+                                    "inlineStyleRanges": [],
+                                    "key": "e23it",
+                                    "text": patrocinato_da,
+                                    "type": "unstyled",
+                                }
+                            ],
+                            "entityMap": {},
+                        },
+                    }
+                },
+                "blocks_layout": {"items": ["d252fe92-ce88-4866-b77d-501e7275cfc0"]},
+            },
         )
-        for brain in brains:
-            obj = brain.getObject()
-            obj_language = getattr(obj, "language", "it")
-            for taxonomy in TYPE_TO_TAXONOMIES_MAPPING[portal_type]:
-                old_value = getattr(obj, taxonomy)
-                if (
-                    old_value
-                    and old_value
-                    in TYPE_TO_TAXONOMIES_MAPPING[portal_type][taxonomy][obj_language]
-                ):
-                    new_value = TYPE_TO_TAXONOMIES_MAPPING[portal_type][taxonomy][
-                        obj_language
-                    ][old_value]
-                    if taxonomy == "tipologia_documento":
-                        new_value = [
-                            new_value,
-                        ]
-                    setattr(obj, taxonomy, new_value)
-                    logger.info(
-                        f"{colors.GREEN} Modifica della tassonomia '{taxonomy}' di {obj.title} da {old_value} a {new_value}{colors.ENDC}"  # noqa
-                    )
-
-            obj.reindexObject()
+        obj.reindexObject()
+    logger.info(f"{colors.DARKCYAN} End of update {colors.ENDC}")
 
 
-def update_taxonomies_on_blocks(context):
-    """
-    Code from
-    https://github.com/RedTurtle/design.plone.contenttypes/pull/139/files#diff-330d75e9be6e5193ab4622582fe7031d05094784e08aa3ada201a4e3d1642632R33
-    """
-    # https://www.comune.novellara.re.it/novita/notizie/archivio-notizie
+def update_folder_for_gallery(self):
+    logger.info(f"{colors.DARKCYAN} Update events {colors.ENDC}")
+    pc = api.portal.get_tool(name="portal_catalog")
+    for brain in pc(portal_type="Event"):
+        evento = brain.getObject()
 
-    logger.info(
-        f"{colors.DARKCYAN} Update dei blocchi listing basati sulle nuove tassonomie {colors.ENDC}"  # noqa
-    )
-    brains = api.portal.get_tool("portal_catalog")()
-    for index, brain in list(enumerate(brains)):
-        item = aq_base(brain.getObject())
-        item_language = item.language or "it"
-        if not index % 500:
-            logger.info(
-                f"{colors.DARKCYAN} ({index}/{len(brains)}) Proseguo l'analisi delle pagine {colors.ENDC}"  # noqa
+        logger.info(f"{colors.DARKCYAN} Event: {evento.absolute_url()} {colors.ENDC}")
+        if "multimedia" in evento.keys():
+            renamed_event = api.content.rename(evento["multimedia"], new_id="immagini")
+            renamed_event.title = "Immagini"
+            renamed_event.reindexObject(idxs=["id", "title"])
+            logger.info(f"{colors.GREEN} Rename multimedia {colors.ENDC}")
+
+        if "video" not in evento.keys():
+            galleria_video = api.content.create(
+                container=evento,
+                type="Document",
+                title="Video",
+                id="video",
             )
-        if getattr(item, "blocks", {}):
-            blocks = deepcopy(item.blocks)
+            create_default_blocks(context=galleria_video)
 
-            if blocks:
-                for block in blocks.values():
-                    if block.get("@type", "") == "listing":
-                        for query in block.get("querystring", {}).get("query", []):
-
-                            if query["i"] in [
-                                "tipologia_notizia",
-                                "tipologia_documento",
-                                "tipologia_organizzazione",
-                            ]:
-                                new_values = []
-                                for v in query["v"]:
-                                    old_value = query["v"]
-                                    if (
-                                        v
-                                        in TAXONOMIES_MAPPING[query["i"]][item_language]
-                                    ):
-                                        v = TAXONOMIES_MAPPING[query["i"]][
-                                            item_language
-                                        ][v]
-                                    new_values.append(v)
-                                query["v"] = new_values
-                                logger.info(
-                                    f"{colors.GREEN} Modifica della query per '{query['i']}' di {item.title} da {old_value} a {query['v']}{colors.ENDC}"  # noqa
-                                )
-                item.blocks = blocks
-    logger.info(
-        f"{colors.DARKCYAN} Terminato l'update dei blocchi {colors.ENDC}"  # noqa
-    )
-
-
-def update_uo_contact_info(context):
-    brains = api.portal.get_tool("portal_catalog")(portal_type="UnitaOrganizzativa")
-    logger.info(
-        f"{colors.DARKCYAN} Inizio la pulzia delle {len(brains)} UO campo contact_info {colors.ENDC}"  # noqa
-    )
-    for brain in brains:
-        obj = brain.getObject()
-        if type(obj.contact_info) == dict:
-            del obj.contact_info
-            logger.info(
-                f"{colors.GREEN} Modifica della UO senza punto di contatto {colors.ENDC}"  # noqa
-            )
+            # select  constraints
+            constraintsGalleriaVideo = ISelectableConstrainTypes(galleria_video)
+            constraintsGalleriaVideo.setConstrainTypesMode(1)
+            constraintsGalleriaVideo.setLocallyAllowedTypes(("Link",))
 
+            with api.env.adopt_roles(["Reviewer"]):
+                api.content.transition(obj=galleria_video, transition="publish")
 
-def readd_tassonomia_argomenti_uid(context):
-    logger.info(
-        f"{colors.DARKCYAN} Aggiungo la tassonomia_argomenti_uid e reindicizzo{colors.ENDC}"  # noqa
-    )
-    update_catalog(context)
-    update_registry(context)
-    idxs = ["tassonomia_argomenti_uid", "tassonomia_argomenti"]
-    reindex_catalog(context, idxs)
+            logger.info(f"{colors.GREEN} Create video {colors.ENDC}")
 
 
-def update_ruolo_indexing(context):
-    logger.info(
-        f"{colors.DARKCYAN} Reindex del ruolo nelle persone {colors.ENDC}"  # noqa
-    )
-    idxs = ["ruolo"]
-    pc = api.portal.get_tool("portal_catalog")
-    brains = pc(portal_type="Persona")
+def to_7009(context):
+    portal_types = api.portal.get_tool(name="portal_types")
+    behaviors = list(portal_types["Venue"].behaviors)
+    if "plone.excludefromnavigation" in behaviors:
+        return
+    logger.info("Enable plone.excludefromnavigation behavior")
+    behaviors.append("plone.excludefromnavigation")
+    portal_types["Venue"].behaviors = tuple(behaviors)
+    logger.info("Reindex Venue objects")
+    brains = api.content.find(portal_type="Venue")
+    tot = len(brains)
+    i = 0
     for brain in brains:
-        persona = brain.getObject()
-        persona.reindexObject(idxs=idxs)
+        i += 1
+        if i % 100 == 0:
+            logger.info("Progress: {}/{}".format(i, tot))
+        venue = brain.getObject()
+        if not getattr(venue, "exclude_from_nav", None):
+            setattr(venue, "exclude_from_nav", False)
+            venue.reindexObject(idxs=["exclude_from_nav"])
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/utils.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/utils.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/argomenti_vocabulary.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/argomenti_vocabulary.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/available_services_vocabulary.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/available_services_vocabulary.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/configure.zcml` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/controlapanel_vocabularies.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/controlapanel_vocabularies.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,15 +11,14 @@
 
 
 logger = logging.getLogger(__name__)
 
 
 class BaseVocabulary(object):
     def __call__(self, context):
-
         values = get_settings_for_language(field=self.field)
         if not values:
             return SimpleVocabulary([])
 
         terms = [SimpleTerm(value=x, token=x, title=x) for x in values]
         terms.insert(
             0,
@@ -30,15 +29,14 @@
 
 
 @implementer(IVocabularyFactory)
 class LeadImageDimension(BaseVocabulary):
     field = "lead_image_dimension"
 
     def __call__(self, context):
-
         values = api.portal.get_registry_record(
             self.field, interface=IDesignPloneSettings, default=[]
         )
         if not values:
             return SimpleVocabulary([])
 
         terms = []
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/lista_azioni_pratica.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/lista_azioni_pratica.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/mockup.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/mockup.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/people_vocabulary.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/people_vocabulary.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/reference_vocabularies.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/reference_vocabularies.py`

 * *Files 6% similar despite different names*

```diff
@@ -6,15 +6,14 @@
 from zope.schema.interfaces import IVocabularyFactory
 from zope.schema.vocabulary import SimpleTerm
 from zope.schema.vocabulary import SimpleVocabulary
 from zope.site.hooks import getSite
 
 
 class ReferencesVocabulary(object):
-
     INDEX = ""
 
     def get_all_index_values(self):
         index = self.catalog._catalog.getIndex(self.INDEX)
         return list(index.uniqueValues())
 
     def __call__(self, registry=None):
@@ -28,26 +27,23 @@
         for brain in brains:
             terms.append(SimpleTerm(brain.UID, brain.UID, safe_unicode(brain.Title)))
         return SimpleVocabulary(terms)
 
 
 @implementer(IVocabularyFactory)
 class EventLocationVocabulary(ReferencesVocabulary):
-
     INDEX = "event_location"
 
 
 @implementer(IVocabularyFactory)
 class OfficeLocationVocabulary(ReferencesVocabulary):
-
     INDEX = "ufficio_responsabile"
 
 
 @implementer(IVocabularyFactory)
 class UOLocationVocabulary(ReferencesVocabulary):
-
     INDEX = "uo_location"
 
 
 EventLocationVocabularyFactory = EventLocationVocabulary()
 OfficeLocationVocabularyFactory = OfficeLocationVocabulary()
 UOLocationVocabularyFactory = UOLocationVocabulary()
```

### Comparing `design.plone.contenttypes-6.0.0a9/src/design/plone/contenttypes/vocabularies/tags_vocabulary.py` & `design.plone.contenttypes-6.0.1/src/design/plone/contenttypes/vocabularies/tags_vocabulary.py`

 * *Files identical despite different names*

### Comparing `design.plone.contenttypes-6.0.0a9/src/design.plone.contenttypes.egg-info/SOURCES.txt` & `design.plone.contenttypes-6.0.1/src/design.plone.contenttypes.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -243,14 +243,17 @@
 src/design/plone/contenttypes/restapi/services/controlpanel.py
 src/design/plone/contenttypes/restapi/services/content/__init__.py
 src/design/plone/contenttypes/restapi/services/content/add.py
 src/design/plone/contenttypes/restapi/services/content/configure.zcml
 src/design/plone/contenttypes/restapi/services/modulistica_items/__init__.py
 src/design/plone/contenttypes/restapi/services/modulistica_items/configure.zcml
 src/design/plone/contenttypes/restapi/services/modulistica_items/get.py
+src/design/plone/contenttypes/restapi/services/prenotazioni_folders_list/__init__.py
+src/design/plone/contenttypes/restapi/services/prenotazioni_folders_list/configure.zcml
+src/design/plone/contenttypes/restapi/services/prenotazioni_folders_list/get.py
 src/design/plone/contenttypes/restapi/services/scadenziario/__init__.py
 src/design/plone/contenttypes/restapi/services/scadenziario/configure.zcml
 src/design/plone/contenttypes/restapi/services/scadenziario/post.py
 src/design/plone/contenttypes/restapi/services/trasparenza/__init__.py
 src/design/plone/contenttypes/restapi/services/trasparenza/configure.zcml
 src/design/plone/contenttypes/restapi/services/trasparenza/get.py
 src/design/plone/contenttypes/restapi/services/types/__init__.py
@@ -277,24 +280,28 @@
 src/design/plone/contenttypes/tests/test_ct_luogo.py
 src/design/plone/contenttypes/tests/test_ct_modulo.py
 src/design/plone/contenttypes/tests/test_ct_news.py
 src/design/plone/contenttypes/tests/test_ct_pagina_argomento.py
 src/design/plone/contenttypes/tests/test_ct_persona.py
 src/design/plone/contenttypes/tests/test_ct_servizio.py
 src/design/plone/contenttypes/tests/test_ct_unita_organizzativa.py
+src/design/plone/contenttypes/tests/test_filefield_view_mode_serializer.py
 src/design/plone/contenttypes/tests/test_move_news_items_view.py
 src/design/plone/contenttypes/tests/test_relateditems_with_dates.py
+src/design/plone/contenttypes/tests/test_service_prenotazioni_folders_list.py
 src/design/plone/contenttypes/tests/test_settings_controlpanel_api.py
 src/design/plone/contenttypes/tests/test_setup.py
 src/design/plone/contenttypes/tests/test_summary_serializer.py
 src/design/plone/contenttypes/tests/test_uo_summary_serializer.py
 src/design/plone/contenttypes/tests/test_vocabularies.py
 src/design/plone/contenttypes/upgrades/__init__.py
 src/design/plone/contenttypes/upgrades/configure.zcml
 src/design/plone/contenttypes/upgrades/draftjs_converter.py
+src/design/plone/contenttypes/upgrades/to_7001.py
+src/design/plone/contenttypes/upgrades/to_7002.py
 src/design/plone/contenttypes/upgrades/upgrades.py
 src/design/plone/contenttypes/vocabularies/__init__.py
 src/design/plone/contenttypes/vocabularies/argomenti_vocabulary.py
 src/design/plone/contenttypes/vocabularies/available_services_vocabulary.py
 src/design/plone/contenttypes/vocabularies/configure.zcml
 src/design/plone/contenttypes/vocabularies/controlapanel_vocabularies.py
 src/design/plone/contenttypes/vocabularies/lista_azioni_pratica.py
```

