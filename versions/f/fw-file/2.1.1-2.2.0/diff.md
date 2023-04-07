# Comparing `tmp/fw_file-2.1.1-py3-none-any.whl.zip` & `tmp/fw_file-2.2.0-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,26 +1,33 @@
-Zip file size: 64154 bytes, number of entries: 24
+Zip file size: 211221 bytes, number of entries: 31
 -rw-r--r--  2.0 unx      229 b- defN 80-Jan-01 00:00 fw_file/__init__.py
--rw-r--r--  2.0 unx     8409 b- defN 80-Jan-01 00:00 fw_file/base.py
+-rw-r--r--  2.0 unx     8377 b- defN 80-Jan-01 00:00 fw_file/base.py
 -rw-r--r--  2.0 unx     3184 b- defN 80-Jan-01 00:00 fw_file/bruker.py
 -rw-r--r--  2.0 unx     1515 b- defN 80-Jan-01 00:00 fw_file/dicom/__init__.py
--rw-r--r--  2.0 unx     4875 b- defN 80-Jan-01 00:00 fw_file/dicom/config.py
+-rw-r--r--  2.0 unx     4912 b- defN 80-Jan-01 00:00 fw_file/dicom/config.py
 -rw-r--r--  2.0 unx    44285 b- defN 80-Jan-01 00:00 fw_file/dicom/dcmdict.py
--rw-r--r--  2.0 unx    17678 b- defN 80-Jan-01 00:00 fw_file/dicom/dicom.py
--rw-r--r--  2.0 unx    17087 b- defN 80-Jan-01 00:00 fw_file/dicom/fixers.py
--rw-r--r--  2.0 unx    17451 b- defN 80-Jan-01 00:00 fw_file/dicom/reader.py
--rw-r--r--  2.0 unx    27684 b- defN 80-Jan-01 00:00 fw_file/dicom/series.py
+-rw-r--r--  2.0 unx    17527 b- defN 80-Jan-01 00:00 fw_file/dicom/dicom.py
+-rw-r--r--  2.0 unx    16940 b- defN 80-Jan-01 00:00 fw_file/dicom/fixers.py
+-rw-r--r--  2.0 unx    17330 b- defN 80-Jan-01 00:00 fw_file/dicom/reader.py
+-rw-r--r--  2.0 unx    27641 b- defN 80-Jan-01 00:00 fw_file/dicom/series.py
+-rw-r--r--  2.0 unx   421033 b- defN 80-Jan-01 00:00 fw_file/dicom/standard/2023b/json/dict_info.json
+-rw-r--r--  2.0 unx   188832 b- defN 80-Jan-01 00:00 fw_file/dicom/standard/2023b/json/iod_info.json
+-rw-r--r--  2.0 unx   528709 b- defN 80-Jan-01 00:00 fw_file/dicom/standard/2023b/json/module_info.json
+-rw-r--r--  2.0 unx    31221 b- defN 80-Jan-01 00:00 fw_file/dicom/standard/2023b/json/uid_info.json
+-rw-r--r--  2.0 unx        5 b- defN 80-Jan-01 00:00 fw_file/dicom/standard/2023b/json/version
+-rw-r--r--  2.0 unx      345 b- defN 80-Jan-01 00:00 fw_file/dicom/standard/editions.json
 -rw-r--r--  2.0 unx     9047 b- defN 80-Jan-01 00:00 fw_file/dicom/utils.py
--rw-r--r--  2.0 unx     5547 b- defN 80-Jan-01 00:00 fw_file/dicom/validation.py
+-rw-r--r--  2.0 unx     6620 b- defN 80-Jan-01 00:00 fw_file/dicom/validation.py
 -rw-r--r--  2.0 unx     3103 b- defN 80-Jan-01 00:00 fw_file/exif.py
 -rw-r--r--  2.0 unx    12581 b- defN 80-Jan-01 00:00 fw_file/ge.py
 -rw-r--r--  2.0 unx      778 b- defN 80-Jan-01 00:00 fw_file/jpg.py
+-rw-r--r--  2.0 unx     2186 b- defN 80-Jan-01 00:00 fw_file/json.py
 -rw-r--r--  2.0 unx     1440 b- defN 80-Jan-01 00:00 fw_file/nifti.py
 -rw-r--r--  2.0 unx     5265 b- defN 80-Jan-01 00:00 fw_file/philips.py
--rw-r--r--  2.0 unx     8407 b- defN 80-Jan-01 00:00 fw_file/png.py
+-rw-r--r--  2.0 unx     8385 b- defN 80-Jan-01 00:00 fw_file/png.py
 -rw-r--r--  2.0 unx        0 b- defN 80-Jan-01 00:00 fw_file/py.typed
--rw-r--r--  2.0 unx    10562 b- defN 80-Jan-01 00:00 fw_file/siemens.py
--rw-r--r--  2.0 unx     8386 b- defN 80-Jan-01 00:00 fw_file-2.1.1.dist-info/METADATA
--rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 fw_file-2.1.1.dist-info/WHEEL
--rw-r--r--  2.0 unx     1078 b- defN 80-Jan-01 00:00 fw_file-2.1.1.dist-info/LICENSE
-?rw-r--r--  2.0 unx     1823 b- defN 16-Jan-01 00:00 fw_file-2.1.1.dist-info/RECORD
-24 files, 210502 bytes uncompressed, 61290 bytes compressed:  70.9%
+-rw-r--r--  2.0 unx    10521 b- defN 80-Jan-01 00:00 fw_file/siemens.py
+-rw-r--r--  2.0 unx     1078 b- defN 80-Jan-01 00:00 fw_file-2.2.0.dist-info/LICENSE
+-rw-r--r--  2.0 unx     8486 b- defN 80-Jan-01 00:00 fw_file-2.2.0.dist-info/METADATA
+-rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 fw_file-2.2.0.dist-info/WHEEL
+?rw-r--r--  2.0 unx     2509 b- defN 16-Jan-01 00:00 fw_file-2.2.0.dist-info/RECORD
+31 files, 1384172 bytes uncompressed, 207257 bytes compressed:  85.0%
```

## zipnote {}

```diff
@@ -24,14 +24,32 @@
 
 Filename: fw_file/dicom/reader.py
 Comment: 
 
 Filename: fw_file/dicom/series.py
 Comment: 
 
+Filename: fw_file/dicom/standard/2023b/json/dict_info.json
+Comment: 
+
+Filename: fw_file/dicom/standard/2023b/json/iod_info.json
+Comment: 
+
+Filename: fw_file/dicom/standard/2023b/json/module_info.json
+Comment: 
+
+Filename: fw_file/dicom/standard/2023b/json/uid_info.json
+Comment: 
+
+Filename: fw_file/dicom/standard/2023b/json/version
+Comment: 
+
+Filename: fw_file/dicom/standard/editions.json
+Comment: 
+
 Filename: fw_file/dicom/utils.py
 Comment: 
 
 Filename: fw_file/dicom/validation.py
 Comment: 
 
 Filename: fw_file/exif.py
@@ -39,14 +57,17 @@
 
 Filename: fw_file/ge.py
 Comment: 
 
 Filename: fw_file/jpg.py
 Comment: 
 
+Filename: fw_file/json.py
+Comment: 
+
 Filename: fw_file/nifti.py
 Comment: 
 
 Filename: fw_file/philips.py
 Comment: 
 
 Filename: fw_file/png.py
@@ -54,20 +75,20 @@
 
 Filename: fw_file/py.typed
 Comment: 
 
 Filename: fw_file/siemens.py
 Comment: 
 
-Filename: fw_file-2.1.1.dist-info/METADATA
+Filename: fw_file-2.2.0.dist-info/LICENSE
 Comment: 
 
-Filename: fw_file-2.1.1.dist-info/WHEEL
+Filename: fw_file-2.2.0.dist-info/METADATA
 Comment: 
 
-Filename: fw_file-2.1.1.dist-info/LICENSE
+Filename: fw_file-2.2.0.dist-info/WHEEL
 Comment: 
 
-Filename: fw_file-2.1.1.dist-info/RECORD
+Filename: fw_file-2.2.0.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## fw_file/base.py

```diff
@@ -30,15 +30,15 @@
 
 
 @functools.lru_cache(maxsize=4096)
 def parse_yaml_value(value: str):
     """Return field value parsed with YAML syntax."""
     try:
         return yaml.safe_load(value)
-    except Exception:  # pylint: disable=broad-except
+    except Exception:
         return value
 
 
 class AttrMixin:
     """Mixin for exposing dictionary keys as attributes.
 
     The magic methods `__getattr__`, `__setattr__` and `__delattr__` are simply
```

## fw_file/dicom/config.py

```diff
@@ -59,15 +59,16 @@
 
     # data element loader / fixer config
     fix_VR_mismatch: bool = False
     fix_VR_mismatch_with_VRs: t.List[str] = ["PN", "DS", "IS"]
     track: bool = False
 
     # dicom standard
-    standard: Path = Path(__file__).parent / "standard"
+    standard_path: Path = Path(__file__).parent / "standard"
+    standard_rev: str = "2023b"
 
     # List of raw data element fixer functions
     raw_elem_fixers: t.List[t.Union[str, t.Callable]] = [
         "fw_file.dicom.fixers.tag_specific_fixer",
         "fw_file.dicom.fixers.apply_dictionary_VR",
         "fw_file.dicom.fixers.replace_backslash_in_VM1_str",
         "fw_file.dicom.fixers.convert_exception_fixer",
```

## fw_file/dicom/dicom.py

```diff
@@ -31,15 +31,15 @@
 # stop_when callback signature
 StopWhen = t.Callable[[TagType, str, int], bool]
 
 
 class DICOM(File):
     """DICOM file class."""
 
-    def __init__(  # pylint: disable=too-many-arguments
+    def __init__(  # noqa PLR0913
         self,
         file: AnyFile,
         force: bool = False,
         defer_size: t.Union[int, str] = None,
         specific_tags: t.List[TagType] = None,
         stop_when: t.Union[TagType, StopWhen] = None,
         decode: bool = False,
@@ -134,15 +134,15 @@
         meta = self.get_meta()
         return (
             meta.get("session.uid") or meta.get("session.label") or "",
             meta.get("acquisition.uid") or meta.get("acquisition.label") or "",
             self.get("SOPInstanceUID") or "",
         )
 
-    def save(  # pylint: disable=arguments-differ
+    def save(
         self,
         file: AnyFile = None,
         write_like_original: bool = True,
     ) -> None:
         """Save the dataset to the specified file (default to the original)."""
         bytesio = io.BytesIO()
         self.update_orig_attrs()
@@ -269,15 +269,15 @@
         return iter(self.raw)
 
     def __len__(self) -> int:
         """Return the number of elements in the dataset."""
         return len(self.raw)
 
 
-class PrivateTag:  # pylint: disable=too-few-public-methods
+class PrivateTag:
     """Private tag with creator."""
 
     def __init__(self, group: int, creator: str, element_offset: int):
         """Init a private tag."""
         self.group = group
         self.creator = creator
         self.element_offset = element_offset
@@ -427,15 +427,14 @@
     return dictionary_VR(tag)
 
 
 def stop_at_tag(tag: TagType) -> StopWhen:
     """Return stop_when function for given tag."""
     stop_tag = Tag(tag)  # type: ignore
 
-    # pylint: disable=invalid-name,unused-argument
     def stop_when(current_tag: TagType, VR: str, length: int) -> bool:
         """Return True if the current tag equals the stop_tag."""
         return current_tag == stop_tag
 
     return stop_when
```

## fw_file/dicom/fixers.py

```diff
@@ -20,15 +20,15 @@
 )
 from pydicom.values import convert_value, validate_value
 
 from .utils import generate_uid
 
 log = logging.getLogger(__name__)
 
-# pylint: disable=protected-access
+
 private_vr_for_tag = pydicom_dataelem._private_vr_for_tag
 LUT_DESCRIPTOR_TAGS = pydicom_dataelem._LUT_DESCRIPTOR_TAGS
 VM_RANGE_RE = re.compile(r"^(\w+)-(\w+)$")
 # pylint: enable=protected-access
 
 
 def char_range(a: str, b: str) -> t.List[str]:
@@ -141,15 +141,15 @@
             # and add to Nonconforming modified attributes sseuqnece
             cropped = value[:max_len]
             raw = raw._replace(value=cropped, length=len(cropped))
             return raw
     return raw
 
 
-def convert_exception_fixer(  # pylint: disable=too-many-locals
+def convert_exception_fixer(
     raw: RawDataElement,
     encoding: t.Optional[t.Union[str, t.List[str]]] = None,
     dataset: t.Optional[Dataset] = None,
     **_kwargs,
 ) -> RawDataElement:
     """FW File convert_value handler.
 
@@ -207,15 +207,15 @@
                 if len(fixed_val or b"") != len(raw.value or b""):
                     raw = raw._replace(length=len(fixed_val or b""))
                 raw = raw._replace(value=fixed_val)
         except ValueError:
             # If we still get an error after using fixed value, bail.
             return empty()
         return convert_exception_fixer(raw, encoding, dataset)
-    except Exception:  # pylint: disable=broad-except
+    except Exception:
         log.exception("Unhandled exception.", exc_info=True)
         # Any other unforeseen exception in conversion
         return empty()
     return raw
 
 
 def fix_uids(
@@ -398,15 +398,15 @@
     "LT": (fix_invalid_char, {}),
     "UC": (fix_invalid_char, {}),
     "UT": (fix_invalid_char, {}),
     "CS": (fix_invalid_char, {"upper": True}),
 }
 
 
-def fix_invalid_VR_value(  # pylint: disable=too-many-return-statements
+def fix_invalid_VR_value(
     VR: str,
     raw: RawDataElement,
     dataset: t.Optional[Dataset] = None,
     encoding: t.Optional[t.Union[str, t.List[str]]] = None,
 ) -> t.Optional[bytes]:
     """Try to fix an invalid value for the given VR.
```

## fw_file/dicom/reader.py

```diff
@@ -12,28 +12,28 @@
 from pydicom.dataset import Dataset
 from pydicom.filebase import DicomBytesIO
 from pydicom.filewriter import write_data_element
 from pydicom.sequence import Sequence
 from pydicom.tag import BaseTag, Tag
 from pydicom.values import convert_value, validate_value
 
-from .. import NAME, __version__
+from .. import NAME
 from .config import get_config
 from .validation import get_required_tags, get_standard
 
 log = logging.getLogger(__name__)
 
 OAS: str = "OriginalAttributesSequence"
 NAS: str = "NonconformingModifiedAttributesSequence"
 MAS: str = "ModifiedAttributesSequence"
 
 READER: str = "ReadContext"
 
 
-def DataElement_from_raw(  # pylint: disable=too-many-branches
+def DataElement_from_raw(
     raw: RawDataElement,
     encoding: t.Optional[t.Union[str, t.List[str]]] = None,
     dataset: t.Optional[Dataset] = None,
 ) -> DataElement:
     """Override pydicom's DataElement_from_raw.
 
     This implementation separates the existing (as of pydicom 2.2.x)
@@ -122,15 +122,14 @@
         """Return a new TrackedRawDataElement instance."""
         tracked = super().__new__(cls, *args, **kwargs)
         tracked.id_ = id_
         tracked.original = RawDataElement(*args, **kwargs)
         tracked.events = []
         return tracked
 
-    # pylint: disable=arguments-differ
     def _replace(self, **kwargs) -> "TrackedRawDataElement":
         """Extend namedtuple _replace with change event tracking."""
         for key, val in kwargs.items():
             old = getattr(self, key)
             event = ReplaceEvent(field=key, old=old, new=val)
             self.events.append(event)
         raw = super()._replace(**kwargs)  # calls new
@@ -369,15 +368,15 @@
                 # before we bailed out (removed the value) will be lost,
                 # only the original Value from the dicom will be written
                 # back if it can be
                 VR = t.cast(str, elem.VR)
                 out = DataElement(elem.tag, VR, elem.original.value)
                 write_data_element(buffer, out)
                 dataset[out.tag] = out
-            except Exception as exc:  # pylint: disable=broad-except
+            except Exception as exc:
                 # Writing will fail but we want to warn the user on all DEs that
                 # fall into this category
                 warnings.warn(
                     (
                         "Could not write original element. Original element "
                         "is required but invalid and cannot be written.\n\n"
                         f"VR: {elem.original.VR}\t value: {elem.original.value!r}\n\n"
```

## fw_file/dicom/series.py

```diff
@@ -22,15 +22,15 @@
 from .dicom import DICOM, TagType
 
 try:
     from fw_storage import StorageError
 except ImportError:  # pragma: no cover
 
     class StorageError(Exception):  # type: ignore
-        pass
+        """Storage error stub."""
 
 
 __all__ = ["DICOMCollection", "DICOMSeries", "build_dicom_tree"]
 
 log = logging.getLogger(__name__)
 
 AnyDICOM = t.Union[AnyFile, DICOM]
@@ -583,24 +583,24 @@
         return len(self) >= get_config().instance_cache_size
 
 
 DICOMTree = t.Dict[str, t.Dict[str, t.Dict[str, AnyPath]]]
 
 
 @dataclass
-class DICOMError:  # pylint: disable=too-few-public-methods
+class DICOMError:
     """DICOM error class capturing any issues from build_dicom_tree."""
 
     __slots__ = ("file", "message")
 
     file: str
     message: str
 
 
-def build_dicom_tree(
+def build_dicom_tree(  # noqa PLR0915
     files: t.Iterable[AnyPath],
     open_fn: t.Optional[t.Callable] = None,
     validate_meta_fn: t.Optional[t.Callable] = None,
     natural_sort: bool = True,
     **dcm_kw,
 ) -> t.Tuple[DICOMTree, t.List[DICOMError]]:
     """Build DICOM hierarchy from DICOM files.
@@ -611,15 +611,14 @@
             Default: BinFile (expecting files on the local filesystem).
         validate_meta_fn (callable, optional): Function to build and validate
             series meta with instance by instance. Default: validate_series_meta
         natural_sort (bool, optional): Toggle to disable natural sorting on the
             UIDs in the returned DICOM tree. Default: True.
         **dcm_kw: Keyword arguments to use when reading files.
     """
-    # pylint: disable=too-many-locals
     open_file = open_fn or BinFile
     validate_meta = validate_meta_fn or validate_series_meta
     dcm_kw.setdefault("force", True)
     dcm_kw.setdefault("defer_size", 512)
     dcm_kw.setdefault("stop_when", "PixelData")
     tree: DICOMTree = {}
     series_to_study: t.Dict[str, str] = {}
```

## fw_file/dicom/validation.py

```diff
@@ -1,9 +1,11 @@
 """Functions to handle validation of DICOMs."""
+import json
 import logging
+import re
 import typing as t
 from dataclasses import dataclass
 from functools import lru_cache
 from pathlib import Path
 
 from dicom_validator.spec_reader.edition_reader import EditionReader
 from dicom_validator.validator.iod_validator import IODValidator
@@ -31,23 +33,43 @@
 def get_standard() -> Standard:
     """Get the dicom standard.
 
     Returns:
         dicom standard representation.
     """
     config = get_config()
-    standard_path = config.standard
-    standard_path.mkdir(parents=True, exist_ok=True)
-    edition_reader = EditionReader(standard_path)
-    destination = edition_reader.get_revision("current")
-    json_path = Path(destination) / "json"
-    dict_info = EditionReader.load_dict_info(json_path)
-    iod_info = EditionReader.load_iod_info(json_path)
-    mod_info = EditionReader.load_module_info(json_path)
-    return Standard(iod_info, mod_info, dict_info)
+    standard_path = config.standard_path
+    revision_path = config.standard_path / config.standard_rev
+    if not revision_path.exists():  # pragma: no cover
+        # pull revs at runtime if not using the shipped default
+        try:
+            standard_path.mkdir(parents=True, exist_ok=True)
+            standard_path.touch()
+        except PermissionError:
+            # fallback to /tmp if the default path is not writable
+            standard_path = Path("/tmp/dicom_standard")  # noqa S108
+            standard_path.mkdir(parents=True, exist_ok=True)
+        # pull the dicom standard xml's and transform them to json
+        edition_reader = EditionReader(standard_path)
+        edition_reader.get_revision(revision=config.standard_rev)
+        json_nl_re = re.compile(r'\},(?!"(cond|include|index|items|name|ref|title)")')
+        for file in standard_path.rglob("*.*"):
+            # minify the jsons while keeping them git and human-friendly
+            if file.suffix == ".json":
+                data = json.loads(file.read_text())
+                data_str = json.dumps(data, sort_keys=True, separators=(",", ":"))
+                file.write_text(json_nl_re.sub("},\n", data_str))
+            # delete all other files to minimize git/pypi/network overhead
+            else:
+                file.unlink()
+    return Standard(
+        json.loads((revision_path / "json/iod_info.json").read_text()),
+        json.loads((revision_path / "json/module_info.json").read_text()),
+        json.loads((revision_path / "json/dict_info.json").read_text()),
+    )
 
 
 def validate_dicom(
     standard: Standard, dcm: t.Union["DICOM", Dataset], log_level: int = logging.INFO
 ):
     """Validate a given dicom.
 
@@ -70,29 +92,28 @@
         standard.mod_info,
         standard.dict_info,
         log_level,
     )
     return validator.validate()
 
 
-def get_tag_dict(
+def get_tag_dict(  # noqa PLR0912
     standard: Standard, dcm: t.Union["DICOM", Dataset]
 ) -> t.Dict[int, bool]:
     """Get dictionary of tags and whether their value can be removed.
 
     Args:
         standard: Dicom standard
         dcm: Input dicom
 
     Returns:
         Output tag dict, keys are tag ints, value is True if
             tags value can be removed, False otherwise.
             If output is None, tag_dict could not be generated
     """
-    # pylint: disable=protected-access,too-many-locals,too-many-branches
     tag_dict: t.Dict[int, bool] = {}
     validator = IODValidator(
         t.cast(Dataset, dcm),
         standard.iod_info,
         standard.mod_info,
         standard.dict_info,
         log_level=logging.WARNING,
```

## fw_file/png.py

```diff
@@ -176,15 +176,15 @@
     type = "iTXt"
     key: str
     t_key: str
     lang: str
     zip: bool
 
     @staticmethod
-    def __new__(  # pylint: disable=too-many-arguments
+    def __new__(  # noqa PLR0913
         cls, key, text, t_key: str = "", lang: str = "", zip_: bool = False
     ) -> "iTXt":
         """Create iTXt chunk object."""
         self = str.__new__(cls, text)
         self.key = key
         self.t_key = t_key
         self.lang = lang
```

## fw_file/siemens.py

```diff
@@ -210,15 +210,14 @@
         super().__init__(file)
         with self.file as rfile:
             object.__setattr__(self, "fields", load_rda(rfile))
             object.__setattr__(self, "offset", rfile.tell())
 
     def get_default_meta(self) -> t.Dict[str, t.Any]:
         """Return the default Flywheel metadata for the RDA file."""
-        # pylint: disable=duplicate-code
         firstname, lastname = utils.get_patient_name(self)
         meta: t.Dict[str, t.Any] = {
             "subject.label": self.get("PatientID"),
             "subject.firstname": firstname,
             "subject.lastname": lastname,
             "subject.sex": self.get("PatientSex"),
             "session.label": utils.get_session_label(self),
```

## Comparing `fw_file-2.1.1.dist-info/METADATA` & `fw_file-2.2.0.dist-info/METADATA`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fw-file
-Version: 2.1.1
+Version: 2.2.0
 Summary: Unified data-file interface
 Home-page: https://gitlab.com/flywheel-io/tools/lib/fw-file
 License: MIT
 Keywords: Flywheel,parse,medical,file,metadata,extract,DICOM,RAW,MR,CT,PET,NIfTI,JPG,JPEG,PNG,Bruker,ParaVision,GE,PFile,Philips,PARREC,Siemens,PTD
 Author: Flywheel
 Author-email: support@flywheel.io
 Requires-Python: >=3.8,<4.0
@@ -14,17 +14,19 @@
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Scientific/Engineering :: Medical Science Apps.
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Provides-Extra: all
 Provides-Extra: jpg
+Provides-Extra: json
 Provides-Extra: nifti
 Provides-Extra: png
 Requires-Dist: dicom-validator (>=0,<1)
+Requires-Dist: dotty-dict (>=1.3.1,<2.0.0) ; extra == "all" or extra == "json"
 Requires-Dist: fw-meta (>=3.1,<4.0)
 Requires-Dist: fw-utils (>=3,<5)
 Requires-Dist: importlib-metadata (>=4.8.2,<5.0.0) ; python_version < "3.8"
 Requires-Dist: memoization (>=0,<1)
 Requires-Dist: natsort (>=8.0.0,<9.0.0)
 Requires-Dist: nibabel (>=4.0.2,<5.0.0) ; extra == "all" or extra == "nifti"
 Requires-Dist: piexif (>=1.1.3,<2.0.0) ; extra == "all" or extra == "jpg" or extra == "png"
```

## Comparing `fw_file-2.1.1.dist-info/LICENSE` & `fw_file-2.2.0.dist-info/LICENSE`

 * *Files identical despite different names*

