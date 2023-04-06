# Comparing `tmp/djangocms_xliff-1.0.0.tar.gz` & `tmp/djangocms_xliff-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "djangocms_xliff-1.0.0.tar", max compression
+gzip compressed data, was "djangocms_xliff-1.1.0.tar", max compression
```

## Comparing `djangocms_xliff-1.0.0.tar` & `djangocms_xliff-1.1.0.tar`

### file list

```diff
@@ -1,34 +1,33 @@
--rw-r--r--   0        0        0     1073 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/LICENSE
--rw-r--r--   0        0        0     6351 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/README.md
--rw-r--r--   0        0        0       22 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/__init__.py
--rw-r--r--   0        0        0      216 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/apps.py
--rw-r--r--   0        0        0     1885 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/cms_toolbars.py
--rw-r--r--   0        0        0      186 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/exceptions.py
--rw-r--r--   0        0        0     1166 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/exports.py
--rw-r--r--   0        0        0     4298 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/extractors.py
--rw-r--r--   0        0        0      801 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/forms.py
--rw-r--r--   0        0        0     3031 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/imports.py
--rw-r--r--   0        0        0     4022 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/locale/de/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     5560 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/locale/de/LC_MESSAGES/django.po
--rw-r--r--   0        0        0        0 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/management/__init__.py
--rw-r--r--   0        0        0        0 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/management/commands/__init__.py
--rw-r--r--   0        0        0     1602 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/management/commands/xliff_export.py
--rw-r--r--   0        0        0     1657 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/management/commands/xliff_import.py
--rw-r--r--   0        0        0     1515 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/management/commands/xliff_page_plugins.py
--rw-r--r--   0        0        0     3480 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/parsers.py
--rw-r--r--   0        0        0     1148 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/renderer.py
--rw-r--r--   0        0        0     1012 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/settings.py
--rw-r--r--   0        0        0      193 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/base.html
--rw-r--r--   0        0        0      151 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/error.html
--rw-r--r--   0        0        0      522 2022-11-10 12:15:15.813585 djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/export/index.html
--rw-r--r--   0        0        0     1005 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/export/v1.2.xliff
--rw-r--r--   0        0        0     1389 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/import/preview.html
--rw-r--r--   0        0        0     1116 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/import/success.html
--rw-r--r--   0        0        0      447 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/import/upload.html
--rw-r--r--   0        0        0     1739 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/types.py
--rw-r--r--   0        0        0      526 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/urls.py
--rw-r--r--   0        0        0     2437 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/utils.py
--rw-r--r--   0        0        0     7852 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/djangocms_xliff/views.py
--rw-r--r--   0        0        0     1364 2022-11-10 12:15:15.817585 djangocms_xliff-1.0.0/pyproject.toml
--rw-r--r--   0        0        0     7572 1970-01-01 00:00:00.000000 djangocms_xliff-1.0.0/setup.py
--rw-r--r--   0        0        0     7618 1970-01-01 00:00:00.000000 djangocms_xliff-1.0.0/PKG-INFO
+-rw-r--r--   0        0        0     1073 2023-04-06 11:16:57.480252 djangocms_xliff-1.1.0/LICENSE
+-rw-r--r--   0        0        0     6356 2023-04-06 11:16:57.480252 djangocms_xliff-1.1.0/README.md
+-rw-r--r--   0        0        0       22 2023-04-06 11:16:57.480252 djangocms_xliff-1.1.0/djangocms_xliff/__init__.py
+-rw-r--r--   0        0        0      216 2023-04-06 11:16:57.480252 djangocms_xliff-1.1.0/djangocms_xliff/apps.py
+-rw-r--r--   0        0        0     1885 2023-04-06 11:16:57.480252 djangocms_xliff-1.1.0/djangocms_xliff/cms_toolbars.py
+-rw-r--r--   0        0        0      186 2023-04-06 11:16:57.480252 djangocms_xliff-1.1.0/djangocms_xliff/exceptions.py
+-rw-r--r--   0        0        0     1166 2023-04-06 11:16:57.480252 djangocms_xliff-1.1.0/djangocms_xliff/exports.py
+-rw-r--r--   0        0        0     5792 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/extractors.py
+-rw-r--r--   0        0        0      801 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/forms.py
+-rw-r--r--   0        0        0     3596 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/imports.py
+-rw-r--r--   0        0        0     4022 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/locale/de/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     5560 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/locale/de/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0        0 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/management/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/management/commands/__init__.py
+-rw-r--r--   0        0        0     1602 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/management/commands/xliff_export.py
+-rw-r--r--   0        0        0     1657 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/management/commands/xliff_import.py
+-rw-r--r--   0        0        0     1515 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/management/commands/xliff_page_plugins.py
+-rw-r--r--   0        0        0     3648 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/parsers.py
+-rw-r--r--   0        0        0     1148 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/renderer.py
+-rw-r--r--   0        0        0     1071 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/settings.py
+-rw-r--r--   0        0        0      193 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/base.html
+-rw-r--r--   0        0        0      151 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/error.html
+-rw-r--r--   0        0        0      522 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/export/index.html
+-rw-r--r--   0        0        0     1005 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/export/v1.2.xliff
+-rw-r--r--   0        0        0     1389 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/import/preview.html
+-rw-r--r--   0        0        0     1116 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/import/success.html
+-rw-r--r--   0        0        0      447 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/import/upload.html
+-rw-r--r--   0        0        0     1769 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/types.py
+-rw-r--r--   0        0        0      526 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/urls.py
+-rw-r--r--   0        0        0     2437 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/utils.py
+-rw-r--r--   0        0        0     6694 2023-04-06 11:16:57.484252 djangocms_xliff-1.1.0/djangocms_xliff/views.py
+-rw-r--r--   0        0        0     1364 2023-04-06 11:16:57.488252 djangocms_xliff-1.1.0/pyproject.toml
+-rw-r--r--   0        0        0     7623 1970-01-01 00:00:00.000000 djangocms_xliff-1.1.0/PKG-INFO
```

### Comparing `djangocms_xliff-1.0.0/LICENSE` & `djangocms_xliff-1.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/README.md` & `djangocms_xliff-1.1.0/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -135,15 +135,15 @@
 def link_field_extractor(instance: CMSPlugin, field: LinkField, source: Any) -> List[djangocms_xliff.types.Unit]:
     # example:
     from djangocms_xliff.utils import get_type_with_path
 
     text = source.find_text()
     return [
         Unit(
-            plugin_id=instance.id,
+            plugin_id=str(instance.pk),
             plugin_type=instance.plugin_type,
             plugin_name=instance.get_plugin_name(),
             field_name=field.name,
             field_type=get_type_with_path(field),
             field_verbose_name=field.verbose_name,
             source=text,
             max_length=field.max_length,
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/cms_toolbars.py` & `djangocms_xliff-1.1.0/djangocms_xliff/cms_toolbars.py`

 * *Files 8% similar despite different names*

```diff
@@ -35,15 +35,15 @@
             if not language_menu:
                 return None
 
             if len(self.draft_page.get_languages()) > 1:
                 reverse_xliff = partial(
                     reverse,
                     kwargs={
-                        "page_id": self.draft_page.id,
+                        "page_id": self.draft_page.pk,
                         "current_language": self.current_lang,
                     },
                 )
 
                 language_menu.add_break(XLIFF_LANGUAGE_BREAK)
                 language_menu.add_modal_item(
                     _("Export as XLIFF"),
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/exports.py` & `djangocms_xliff-1.1.0/djangocms_xliff/exports.py`

 * *Files 5% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 )
 
 
 def convert_page_to_xliff_context(page: Page, source_language: str, target_language: str) -> XliffContext:
     return XliffContext(
         source_language=source_language,
         target_language=target_language,
-        page_id=page.id,
+        page_id=page.pk,
         page_path=page.get_path(target_language),
         units=extract_units_from_page(page, target_language),
     )
 
 
 def export_page_as_xliff(
     page_id: int,
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/forms.py` & `djangocms_xliff-1.1.0/djangocms_xliff/forms.py`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/imports.py` & `djangocms_xliff-1.1.0/djangocms_xliff/imports.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,45 +1,65 @@
 import logging
 from typing import List
 
-from cms.models import CMSPlugin, Page
+from cms.models import CMSPlugin, Page, Title
 from django.utils.translation import gettext as _
 
 from djangocms_xliff.exceptions import XliffImportError
-from djangocms_xliff.settings import FIELD_IMPORTERS
+from djangocms_xliff.settings import FIELD_IMPORTERS, UNIT_ID_METADATA_ID
 from djangocms_xliff.types import Unit, XliffContext
-from djangocms_xliff.utils import get_lang_name, group_units_by_plugin_id
+from djangocms_xliff.utils import get_lang_name
 
 logger = logging.getLogger(__name__)
 
 
+def save_xliff_units_for_page(units: List[Unit], target_title_obj: Title) -> None:
+    for unit in units:
+        field_name = unit.field_name
+        target = unit.target
+
+        setattr(target_title_obj, field_name, target)
+
+    target_title_obj.save()
+
+
+def save_xliff_units_for_cms_plugins(units: List[Unit], plugin_id: str) -> None:
+    try:
+        cms_plugin = CMSPlugin.objects.get(pk=plugin_id)
+    except CMSPlugin.DoesNotExist:
+        logger.debug(f"Found plugin with id: {plugin_id} in xliff, but not in database")
+        return
+
+    instance, plugin = cms_plugin.get_plugin_instance()
+
+    for unit in units:
+        field_name = unit.field_name
+        target = unit.target
+
+        if unit.field_type in FIELD_IMPORTERS:
+            instance = FIELD_IMPORTERS[unit.field_type](instance=instance, unit=unit)
+        else:
+            setattr(instance, field_name, target)
+
+    instance.save()
+
+
 def save_xliff_context(xliff_context: XliffContext) -> None:
-    for plugin_id, units in group_units_by_plugin_id(xliff_context.units):
-        try:
-            cms_plugin = CMSPlugin.objects.get(pk=plugin_id)
-        except CMSPlugin.DoesNotExist:
-            logger.debug(f"Found plugin with id: {plugin_id} in xliff, but not in database")
-            continue
-
-        instance, plugin = cms_plugin.get_plugin_instance()
-
-        for unit in units:
-            field_name = unit.field_name
-            target = unit.target
-
-            if unit.field_type in FIELD_IMPORTERS:
-                instance = FIELD_IMPORTERS[unit.field_type](instance=instance, unit=unit)
-            else:
-                setattr(instance, field_name, target)
+    page = xliff_context.page
+    target_title_obj = page.get_title_obj(language=xliff_context.target_language)
 
-        instance.save()
+    for plugin_id, units in xliff_context.grouped_units:
+        if plugin_id == UNIT_ID_METADATA_ID:
+            save_xliff_units_for_page(units, target_title_obj)
+        else:
+            save_xliff_units_for_cms_plugins(units, plugin_id)
 
 
 def validate_page_with_xliff_context(page: Page, xliff_context: XliffContext, current_language: str):
-    page_id = page.id
+    page_id = page.pk
     xliff_page_id = xliff_context.page_id
     if page_id != xliff_page_id:
         error_message = _('Selected page id: "%(page_id)s" is not the same as xliff page id: "%(xliff_page_id)s"')
         error_params = {
             "page_id": page_id,
             "xliff_page_id": xliff_page_id,
         }
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/locale/de/LC_MESSAGES/django.mo` & `djangocms_xliff-1.1.0/djangocms_xliff/locale/de/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/locale/de/LC_MESSAGES/django.po` & `djangocms_xliff-1.1.0/djangocms_xliff/locale/de/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/management/commands/xliff_export.py` & `djangocms_xliff-1.1.0/djangocms_xliff/management/commands/xliff_export.py`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/management/commands/xliff_import.py` & `djangocms_xliff-1.1.0/djangocms_xliff/management/commands/xliff_import.py`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/management/commands/xliff_page_plugins.py` & `djangocms_xliff-1.1.0/djangocms_xliff/management/commands/xliff_page_plugins.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,15 +25,15 @@
             current_language = options["current_language"]
 
             page = get_draft_page(page_id)
             units = extract_units_from_page(page, current_language)
 
             self.stdout.write(
                 self.style.SUCCESS(
-                    f"Found {len(units)} xliff units on page with id: {page.id} and language: {current_language}"
+                    f"Found {len(units)} xliff units on page with id: {page.pk} and language: {current_language}"
                 )
             )
             self.stdout.write()
 
             for plugin_id, units in group_units_by_plugin_id(units):
                 self.stdout.write(f"Plugin: {plugin_id}")
                 self.stdout.write()
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/parsers.py` & `djangocms_xliff-1.1.0/djangocms_xliff/parsers.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,40 +1,20 @@
 from html import unescape
 from xml.etree.ElementTree import Element, ParseError
 
 from defusedxml.ElementTree import parse
 from django.utils.translation import gettext as _
 
 from djangocms_xliff.exceptions import XliffConfigurationError, XliffError
-from djangocms_xliff.settings import XliffVersion
-from djangocms_xliff.types import UNIT_ID_DELIMITER, Unit, XliffContext
+from djangocms_xliff.settings import UNIT_ID_DELIMITER, XliffVersion
+from djangocms_xliff.types import Unit, XliffContext
 from djangocms_xliff.utils import get_xliff_namespaces, get_xliff_version
 
 
-def parse_xliff_version_1_2(version: XliffVersion, xliff_element: Element) -> XliffContext:
-    xml_namespaces = get_xliff_namespaces(version)
-
-    file_element = xliff_element.find("file", namespaces=xml_namespaces)
-    if file_element is None:
-        raise XliffError("XLIFF Error: Missing file tag")
-
-    source_language = file_element.attrib["source-language"]
-    target_language = file_element.attrib["target-language"]
-    page_path = file_element.attrib["original"]
-
-    tool_element = file_element.find("tool", namespaces=xml_namespaces)
-    if tool_element is None:
-        raise XliffError("XLIFF Error: Missing <tool> in <file>")
-
-    page_id = tool_element.attrib["tool-id"]
-
-    body_element = file_element.find("body", namespaces=xml_namespaces)
-    if body_element is None:
-        raise XliffError("XLIFF Error: Missing <body> in <file>")
-
+def _parse_xliff_units_version_1_2(xml_namespaces: dict, body_element: Element):
     units = []
     for trans_unit in body_element.findall("trans-unit", namespaces=xml_namespaces):
         unit_id = trans_unit.attrib["id"]
         plugin_id, field_name = unit_id.split(UNIT_ID_DELIMITER, 1)
 
         field_type = trans_unit.attrib["extype"]
 
@@ -53,25 +33,50 @@
 
         notes = trans_unit.iterfind("note", namespaces=xml_namespaces)
         plugin_type = next(notes).text
         plugin_name = next(notes).text
         field_verbose_name = next(notes).text
 
         unit = Unit(
-            plugin_id=int(plugin_id),
+            plugin_id=plugin_id,
             plugin_type=plugin_type if plugin_type else "",
             plugin_name=plugin_name if plugin_name else "",
             field_name=field_name,
             field_type=field_type,
             field_verbose_name=field_verbose_name,
             source=source,
             target=target,
             max_length=int(max_length) if max_length else None,
         )
         units.append(unit)
+    return units
+
+
+def parse_xliff_version_1_2(version: XliffVersion, xliff_element: Element) -> XliffContext:
+    xml_namespaces = get_xliff_namespaces(version)
+
+    file_element = xliff_element.find("file", namespaces=xml_namespaces)
+    if file_element is None:
+        raise XliffError("XLIFF Error: Missing file tag")
+
+    source_language = file_element.attrib["source-language"]
+    target_language = file_element.attrib["target-language"]
+    page_path = file_element.attrib["original"]
+
+    tool_element = file_element.find("tool", namespaces=xml_namespaces)
+    if tool_element is None:
+        raise XliffError("XLIFF Error: Missing <tool> in <file>")
+
+    page_id = tool_element.attrib["tool-id"]
+
+    body_element = file_element.find("body", namespaces=xml_namespaces)
+    if body_element is None:
+        raise XliffError("XLIFF Error: Missing <body> in <file>")
+
+    units = _parse_xliff_units_version_1_2(xml_namespaces, body_element)
 
     return XliffContext(
         source_language=source_language,
         target_language=target_language,
         page_id=int(page_id),
         page_path=page_path,
         units=units,
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/renderer.py` & `djangocms_xliff-1.1.0/djangocms_xliff/renderer.py`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/settings.py` & `djangocms_xliff-1.1.0/djangocms_xliff/settings.py`

 * *Files 8% similar despite different names*

```diff
@@ -7,14 +7,17 @@
 @unique
 class XliffVersion(Enum):
     V1_2 = "1.2"
 
 
 XLIFF_NAMESPACES = {XliffVersion.V1_2: {"": "urn:oasis:names:tc:xliff:document:1.2"}}
 
+UNIT_ID_DELIMITER = "__"
+UNIT_ID_METADATA_ID = "METADATA"
+
 TEMPLATES_FOLDER = "djangocms_xliff"
 TEMPLATES_FOLDER_EXPORT = f"{TEMPLATES_FOLDER}/export"
 TEMPLATES_FOLDER_IMPORT = f"{TEMPLATES_FOLDER}/import"
 
 FIELDS = [import_string(field_class) for field_class in getattr(settings, "DJANGOCMS_XLIFF_FIELDS", ())]
 
 FIELD_EXTRACTORS = {
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/export/index.html` & `djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/export/index.html`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/export/v1.2.xliff` & `djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/export/v1.2.xliff`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/import/preview.html` & `djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/import/preview.html`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/templates/djangocms_xliff/import/success.html` & `djangocms_xliff-1.1.0/djangocms_xliff/templates/djangocms_xliff/import/success.html`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/types.py` & `djangocms_xliff-1.1.0/djangocms_xliff/types.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 from dataclasses import dataclass
 from typing import List, Optional, Tuple
 
 from cms.models import Page
 from django.utils.translation import gettext as _
 
-UNIT_ID_DELIMITER = "__"
+from djangocms_xliff.settings import UNIT_ID_DELIMITER
 
 ExportContent = str
 ExportFileName = str
 ExportPage = Tuple[ExportContent, ExportFileName]
 
 
 @dataclass
 class Unit:
-    plugin_id: int
+    plugin_id: str
     plugin_type: str
     plugin_name: str
 
     field_name: str
     field_type: str
 
     source: str
@@ -58,15 +58,15 @@
     source_language: str
     target_language: str
     page_id: int
     page_path: str
     units: List[Unit]
 
     @property
-    def grouped_units(self) -> List[Tuple[int, List[Unit]]]:
+    def grouped_units(self) -> List[Tuple[str, List[Unit]]]:
         from djangocms_xliff.utils import group_units_by_plugin_id
 
         return group_units_by_plugin_id(self.units)
 
     @property
     def page(self) -> Page:
         from djangocms_xliff.utils import get_draft_page
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/urls.py` & `djangocms_xliff-1.1.0/djangocms_xliff/urls.py`

 * *Files identical despite different names*

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/utils.py` & `djangocms_xliff-1.1.0/djangocms_xliff/utils.py`

 * *Files 9% similar despite different names*

```diff
@@ -49,22 +49,22 @@
 
 def get_draft_page(page_id: int) -> Page:
     try:
         page = Page.objects.get(id=page_id)
         if not page.publisher_is_draft:
             raise XliffError(
                 "Page is not a draft. You probably want to use a draft instead of a published page. "
-                f"Draft page id would be: {page.publisher_public.id}"
+                f"Draft page id would be: {page.publisher_public.pk}"
             )
         return page
     except Page.DoesNotExist:
         raise XliffError(f"Page with id: {page_id} does not exist")
 
 
-def group_units_by_plugin_id(units: List[Unit]) -> List[Tuple[int, List[Unit]]]:
+def group_units_by_plugin_id(units: List[Unit]) -> List[Tuple[str, List[Unit]]]:
     return [(plugin_id, list(units)) for plugin_id, units in groupby(units, lambda u: u.plugin_id)]
 
 
 def get_type_with_path(cls: Type) -> str:
     typ = type(cls)
     return f"{typ.__module__}.{typ.__name__}"
```

### Comparing `djangocms_xliff-1.0.0/djangocms_xliff/views.py` & `djangocms_xliff-1.1.0/djangocms_xliff/views.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 import json
 from dataclasses import asdict
 from typing import Type
 
-import requests
-from cms.admin.forms import ChangePageForm
-from cms.utils.urlutils import admin_reverse
+from cms.models import Page
+from django.contrib.admin import site
 from django.contrib.admin.views.decorators import staff_member_required
 from django.forms import Form
 from django.http import HttpResponse
 from django.shortcuts import render
 from django.urls import reverse
 from django.utils.decorators import method_decorator
 from django.utils.translation import gettext as _
@@ -159,44 +158,19 @@
             "xliff_json": json.dumps(asdict(xliff_context)),
         }
         return render(self.request, self.template_success, context)
 
 
 @method_decorator(staff_member_required, name="dispatch")
 class ImportView(XliffView):
-    @staticmethod
-    def trigger_cms_change_page(request, page_id, current_language):
-        """
-        This is a trick to trigger the cms, that we changed a page
-        It calls the admin api, the same way, as the "Change Page" Toolbar option
-        It basically just saves the page with the existing data
-        """
-        page = get_draft_page(page_id)
-        title_obj = page.get_title_obj(current_language)
-
-        fields = {field: getattr(title_obj, field, "") for field in ChangePageForm.translation_fields}
-        cms_admin_change_page_url = f'{admin_reverse("cms_page_change", args=[page_id])}?language={current_language}'
-        data = {
-            "csrfmiddlewaretoken": request.POST["csrfmiddlewaretoken"],
-            "language": current_language,
-            **fields,
-        }
-        headers = {"Referer": request.build_absolute_uri(request.get_full_path())}
-        response = requests.post(
-            url=request.build_absolute_uri(cms_admin_change_page_url),
-            data=data,
-            cookies=request.COOKIES,
-            headers=headers,
-        )
-        return HttpResponse(content=response.content)
-
     def post(self, request, page_id, current_language, *args, **kwargs):
         try:
             data = json.loads(request.POST["xliff_json"])
             units = data.pop("units", [])
 
             xliff_context = XliffContext(**data, units=[Unit(**u) for u in units])
             save_xliff_context(xliff_context)
 
-            return self.trigger_cms_change_page(request, page_id, current_language)
+            admin = site._registry[Page]
+            return admin.response_change(request, xliff_context.page)
         except XliffError as e:
             return self.error_response(e)
```

### Comparing `djangocms_xliff-1.0.0/pyproject.toml` & `djangocms_xliff-1.1.0/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "djangocms-xliff"
-version = "1.0.0"
+version = "1.1.0"
 description = "XLIFF Import and Export for the Django CMS"
 authors = ["Energie 360 <onlineservice@energie360.ch>"]
 maintainers = ["Energie 360 <onlineservice@energie360.ch>"]
 license = "MIT"
 readme = "README.md"
 homepage = "https://energie360.ch"
 repository = "https://github.com/energie360/djangocms-xliff"
```

### Comparing `djangocms_xliff-1.0.0/setup.py` & `djangocms_xliff-1.1.0/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,36 +1,219 @@
-# -*- coding: utf-8 -*-
-from setuptools import setup
+Metadata-Version: 2.1
+Name: djangocms-xliff
+Version: 1.1.0
+Summary: XLIFF Import and Export for the Django CMS
+Home-page: https://energie360.ch
+License: MIT
+Keywords: django,django-cms,xliff,import,export
+Author: Energie 360
+Author-email: onlineservice@energie360.ch
+Maintainer: Energie 360
+Maintainer-email: onlineservice@energie360.ch
+Requires-Python: >=3.9
+Classifier: Environment :: Web Environment
+Classifier: Framework :: Django
+Classifier: Framework :: Django CMS
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Classifier: Programming Language :: Python
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3
+Classifier: Topic :: Internet :: WWW/HTTP
+Classifier: Topic :: Internet :: WWW/HTTP :: Dynamic Content
+Classifier: Topic :: Software Development :: Libraries
+Requires-Dist: Django (>=3.2,<4.1)
+Requires-Dist: defusedxml (>=0.7)
+Requires-Dist: django-cms (>=3.9)
+Requires-Dist: requests (>=2.20)
+Project-URL: Repository, https://github.com/energie360/djangocms-xliff
+Description-Content-Type: text/markdown
+
+# djangocms-xliff
+
+[![Tests](https://github.com/energie360/djangocms-xliff/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/energie360/djangocms-xliff/actions/workflows/tests.yaml)
+
+XLIFF (XML Localization Interchange File Format) is an XML-based format created
+to standardize the way localizable data are passed between and among tools during a localization process.
+
+With djangocms-xliff it is possible to export all text objects from a page into an XLIFF-compatible file and re-import
+the file at the end of the translation process.
+
+## Installation
+
+Before the installation you need to make sure, that your
+localization / internalization are set up properly
+for [Django](https://docs.djangoproject.com/en/dev/topics/i18n/translation/)
+and [Django-CMS](https://docs.django-cms.org/en/latest/topics/i18n.html)
+
+### Setup
+
+djangocms-xliff is available on [PyPI](https://pypi.org/project/djangocms-xliff/):
+
+```shell
+$ pip install djangocms-xliff
+```
+
+Add `djangocms_xliff` to your `INSTALLED_APPS`.
+
+```python
+INSTALLED_APPS = (
+    ...,
+    "djangocms_xliff"
+)
+```
+
+Add the views for `djangocms_xliff` to your `urls.py`
+
+```python
+urlpatterns = [
+    path("xliff/", include("djangocms_xliff.urls"))
+]
+```
+
+## Documentation
+
+To make the process fail-safe there are some Django CMS related restrictions:
+
+* You can only import the file to the same page and language that you exported from before.
+* It is not possible to export a file for one language and import it to another language.
+* It is not possible to add fields during the translation process. (Missing fields will be ignored.)
+
+This is because the reference for an entity is the unique ID of the Django CMS plugin, and each plugin has its own
+unique ID for each page and language.
+
+Therefore, you need to follow these steps to work with djangocms-xliff.
+
+### Step-by-step
+
+If the page does not exist yet in the target language, create it and copy the plugins from the page with the source
+plugins.
+
+Go to the page in the target language.
+
+Export the XLIFF file at Language > Export as XLIFF…
+
+![Export](docs/screenshots/export.png)
+
+This will generate an XLIFF file in the following format:
+
+```xml
+<?xml version="1.0" encoding="utf-8" standalone="no"?>
+<xliff xmlns="urn:oasis:names:tc:xliff:document:1.2" version="1.2">
+    <file original="verbund/meilen/projekt" datatype="plaintext" source-language="fr" target-language="en">
+        <tool tool-id="96" tool-name="djangocms_xliff" tool-company-name="Energie 360°"/>
+        <body>
+            <trans-unit id="5872__title" resname="5872__title" maxwidth="60" size-unit="char"
+                        extype="django.db.models.fields.CharField">
+                <source><![CDATA[The project in short]]></source>
+                <target><![CDATA[]]></target>
+                <note>CarouselTripleBlockWrapperPlugin</note>
+                <note>Carousel Triple Block</note>
+                <note>Titel</note>
+                <note>Max characters: 60</note>
+            </trans-unit>
+            <trans-unit id="5874__title" resname="5874__title" maxwidth="35" size-unit="char"
+                        extype="django.db.models.fields.CharField">
+                <source><![CDATA[Practical Solution]]></source>
+                <target><![CDATA[]]></target>
+                <note>CarouselTripleBlockSlidePlugin</note>
+                <note>Slide</note>
+                <note>Titel</note>
+                <note>Max characters: 35</note>
+            </trans-unit>
+        </body>
+    </file>
+</xliff>
+```
+
+Edit the file in the XLIFF editor of your choice.
+
+Import the XLIFF to the same page in the same language you exported from with Languages > Import from XLIFF
+
+![Import](docs/screenshots/import.png)
+
+You will get a preview of the import that needs to be confirmed.
+
+![Preview](docs/screenshots/preview.png)
+
+The translations are now imported, and you can publish the page.
+
+## Settings
+
+By default, djangocms-xliff searches for the following django model fields: `CharField, TextField, URLField` in your
+plugins.
+The texts from these fields will be used for the XLIFF import and export.
+
+If you want to add additional or 3rd party app fields, you can define the following settings in your `settings.py`,
+to integrate them into the XLIFF package:
+
+```python
+# A list of fields, that will be searched for while exporting.
+DJANGOCMS_XLIFF_FIELDS = (
+    "djangocms_text_ckeditor.fields.HTMLField",
+)
+```
+
+```python
+# List of tuples with field and custom function for the export
+DJANGOCMS_XLIFF_FIELD_EXTRACTORS = (
+    ("third_party.models.LinkField", "your_module.xliff.link_field_extractor"),
+)
+
+
+# The signature of the extractor function must be the following:
+# The source parameter is the same as getattr(instance, field.name)
+def link_field_extractor(instance: CMSPlugin, field: LinkField, source: Any) -> List[djangocms_xliff.types.Unit]:
+    # example:
+    from djangocms_xliff.utils import get_type_with_path
+
+    text = source.find_text()
+    return [
+        Unit(
+            plugin_id=str(instance.pk),
+            plugin_type=instance.plugin_type,
+            plugin_name=instance.get_plugin_name(),
+            field_name=field.name,
+            field_type=get_type_with_path(field),
+            field_verbose_name=field.verbose_name,
+            source=text,
+            max_length=field.max_length,
+        )
+    ]
+```
+
+```python
+# List of tuples with field and custom function for the import
+DJANGOCMS_XLIFF_FIELD_IMPORTERS = (
+    ("third_party.models.LinkField", "your_module.xliff.link_field_importer"),
+)
+
+
+# The signature of the importer function must be the following:
+def link_field_importer(instance: CMSPlugin, unit: djangocms_xliff.types.Unit) -> CMSPlugin:
+    # example:
+    field = getattr(instance, unit.field_name)
+    field.body = unit.target
+    return instance
+```
+
+```python
+# List of custom validators for fields that need to be ignored or included in the export
+DJANGOCMS_XLIFF_VALIDATORS = ("your_module.xliff.is_not_background",)
+
+
+# The signature of the validator function must be the following:
+def is_not_background(field: django.db.models.Field, instance: CMSPlugin) -> bool:
+    # example:
+    return field.name != "background"
+```
 
-packages = \
-['djangocms_xliff',
- 'djangocms_xliff.management',
- 'djangocms_xliff.management.commands']
-
-package_data = \
-{'': ['*'],
- 'djangocms_xliff': ['locale/de/LC_MESSAGES/*',
-                     'templates/djangocms_xliff/*',
-                     'templates/djangocms_xliff/export/*',
-                     'templates/djangocms_xliff/import/*']}
-
-install_requires = \
-['Django>=3.2,<4.1', 'defusedxml>=0.7', 'django-cms>=3.9', 'requests>=2.20']
-
-setup_kwargs = {
-    'name': 'djangocms-xliff',
-    'version': '1.0.0',
-    'description': 'XLIFF Import and Export for the Django CMS',
-    'long_description': '# djangocms-xliff\n\n[![Tests](https://github.com/energie360/djangocms-xliff/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/energie360/djangocms-xliff/actions/workflows/tests.yaml)\n\nXLIFF (XML Localization Interchange File Format) is an XML-based format created\nto standardize the way localizable data are passed between and among tools during a localization process.\n\nWith djangocms-xliff it is possible to export all text objects from a page into an XLIFF-compatible file and re-import\nthe file at the end of the translation process.\n\n## Installation\n\nBefore the installation you need to make sure, that your\nlocalization / internalization are set up properly\nfor [Django](https://docs.djangoproject.com/en/dev/topics/i18n/translation/)\nand [Django-CMS](https://docs.django-cms.org/en/latest/topics/i18n.html)\n\n### Setup\n\ndjangocms-xliff is available on [PyPI](https://pypi.org/project/djangocms-xliff/):\n\n```shell\n$ pip install djangocms-xliff\n```\n\nAdd `djangocms_xliff` to your `INSTALLED_APPS`.\n\n```python\nINSTALLED_APPS = (\n    ...,\n    "djangocms_xliff"\n)\n```\n\nAdd the views for `djangocms_xliff` to your `urls.py`\n\n```python\nurlpatterns = [\n    path("xliff/", include("djangocms_xliff.urls"))\n]\n```\n\n## Documentation\n\nTo make the process fail-safe there are some Django CMS related restrictions:\n\n* You can only import the file to the same page and language that you exported from before.\n* It is not possible to export a file for one language and import it to another language.\n* It is not possible to add fields during the translation process. (Missing fields will be ignored.)\n\nThis is because the reference for an entity is the unique ID of the Django CMS plugin, and each plugin has its own\nunique ID for each page and language.\n\nTherefore, you need to follow these steps to work with djangocms-xliff.\n\n### Step-by-step\n\nIf the page does not exist yet in the target language, create it and copy the plugins from the page with the source\nplugins.\n\nGo to the page in the target language.\n\nExport the XLIFF file at Language > Export as XLIFF…\n\n![Export](docs/screenshots/export.png)\n\nThis will generate an XLIFF file in the following format:\n\n```xml\n<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<xliff xmlns="urn:oasis:names:tc:xliff:document:1.2" version="1.2">\n    <file original="verbund/meilen/projekt" datatype="plaintext" source-language="fr" target-language="en">\n        <tool tool-id="96" tool-name="djangocms_xliff" tool-company-name="Energie 360°"/>\n        <body>\n            <trans-unit id="5872__title" resname="5872__title" maxwidth="60" size-unit="char"\n                        extype="django.db.models.fields.CharField">\n                <source><![CDATA[The project in short]]></source>\n                <target><![CDATA[]]></target>\n                <note>CarouselTripleBlockWrapperPlugin</note>\n                <note>Carousel Triple Block</note>\n                <note>Titel</note>\n                <note>Max characters: 60</note>\n            </trans-unit>\n            <trans-unit id="5874__title" resname="5874__title" maxwidth="35" size-unit="char"\n                        extype="django.db.models.fields.CharField">\n                <source><![CDATA[Practical Solution]]></source>\n                <target><![CDATA[]]></target>\n                <note>CarouselTripleBlockSlidePlugin</note>\n                <note>Slide</note>\n                <note>Titel</note>\n                <note>Max characters: 35</note>\n            </trans-unit>\n        </body>\n    </file>\n</xliff>\n```\n\nEdit the file in the XLIFF editor of your choice.\n\nImport the XLIFF to the same page in the same language you exported from with Languages > Import from XLIFF\n\n![Import](docs/screenshots/import.png)\n\nYou will get a preview of the import that needs to be confirmed.\n\n![Preview](docs/screenshots/preview.png)\n\nThe translations are now imported, and you can publish the page.\n\n## Settings\n\nBy default, djangocms-xliff searches for the following django model fields: `CharField, TextField, URLField` in your\nplugins.\nThe texts from these fields will be used for the XLIFF import and export.\n\nIf you want to add additional or 3rd party app fields, you can define the following settings in your `settings.py`,\nto integrate them into the XLIFF package:\n\n```python\n# A list of fields, that will be searched for while exporting.\nDJANGOCMS_XLIFF_FIELDS = (\n    "djangocms_text_ckeditor.fields.HTMLField",\n)\n```\n\n```python\n# List of tuples with field and custom function for the export\nDJANGOCMS_XLIFF_FIELD_EXTRACTORS = (\n    ("third_party.models.LinkField", "your_module.xliff.link_field_extractor"),\n)\n\n\n# The signature of the extractor function must be the following:\n# The source parameter is the same as getattr(instance, field.name)\ndef link_field_extractor(instance: CMSPlugin, field: LinkField, source: Any) -> List[djangocms_xliff.types.Unit]:\n    # example:\n    from djangocms_xliff.utils import get_type_with_path\n\n    text = source.find_text()\n    return [\n        Unit(\n            plugin_id=instance.id,\n            plugin_type=instance.plugin_type,\n            plugin_name=instance.get_plugin_name(),\n            field_name=field.name,\n            field_type=get_type_with_path(field),\n            field_verbose_name=field.verbose_name,\n            source=text,\n            max_length=field.max_length,\n        )\n    ]\n```\n\n```python\n# List of tuples with field and custom function for the import\nDJANGOCMS_XLIFF_FIELD_IMPORTERS = (\n    ("third_party.models.LinkField", "your_module.xliff.link_field_importer"),\n)\n\n\n# The signature of the importer function must be the following:\ndef link_field_importer(instance: CMSPlugin, unit: djangocms_xliff.types.Unit) -> CMSPlugin:\n    # example:\n    field = getattr(instance, unit.field_name)\n    field.body = unit.target\n    return instance\n```\n\n```python\n# List of custom validators for fields that need to be ignored or included in the export\nDJANGOCMS_XLIFF_VALIDATORS = ("your_module.xliff.is_not_background",)\n\n\n# The signature of the validator function must be the following:\ndef is_not_background(field: django.db.models.Field, instance: CMSPlugin) -> bool:\n    # example:\n    return field.name != "background"\n```\n\n## Contribute\n\nIssues and pull requests are welcomed.\n\nYou can find a documentation on how to set up your project\nin [here](docs/contribute.md)\n',
-    'author': 'Energie 360',
-    'author_email': 'onlineservice@energie360.ch',
-    'maintainer': 'Energie 360',
-    'maintainer_email': 'onlineservice@energie360.ch',
-    'url': 'https://energie360.ch',
-    'packages': packages,
-    'package_data': package_data,
-    'install_requires': install_requires,
-    'python_requires': '>=3.9',
-}
+## Contribute
 
+Issues and pull requests are welcomed.
+
+You can find a documentation on how to set up your project
+in [here](docs/contribute.md)
 
-setup(**setup_kwargs)
```

