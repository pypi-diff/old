# Comparing `tmp/gradio_client-0.0.7.tar.gz` & `tmp/gradio_client-0.0.8.tar.gz`

## Comparing `gradio_client-0.0.7.tar` & `gradio_client-0.0.8.tar`

### file list

```diff
@@ -1,10 +1,11 @@
--rwxr-xr-x   0        0        0     3059 2020-02-02 00:00:00.000000 gradio_client-0.0.7/README.md
--rwxr-xr-x   0        0        0       83 2020-02-02 00:00:00.000000 gradio_client-0.0.7/requirements.txt
--rwxr-xr-x   0        0        0      139 2020-02-02 00:00:00.000000 gradio_client-0.0.7/gradio_client/__init__.py
--rwxr-xr-x   0        0        0    25114 2020-02-02 00:00:00.000000 gradio_client-0.0.7/gradio_client/client.py
--rwxr-xr-x   0        0        0    11748 2020-02-02 00:00:00.000000 gradio_client-0.0.7/gradio_client/serializing.py
--rwxr-xr-x   0        0        0    10502 2020-02-02 00:00:00.000000 gradio_client-0.0.7/gradio_client/utils.py
--rwxr-xr-x   0        0        0        5 2020-02-02 00:00:00.000000 gradio_client-0.0.7/gradio_client/version.txt
--rwxr-xr-x   0        0        0      730 2020-02-02 00:00:00.000000 gradio_client-0.0.7/.gitignore
--rwxr-xr-x   0        0        0     1418 2020-02-02 00:00:00.000000 gradio_client-0.0.7/pyproject.toml
--rw-r--r--   0        0        0     3691 2020-02-02 00:00:00.000000 gradio_client-0.0.7/PKG-INFO
+-rw-r--r--   0        0        0     7251 2020-02-02 00:00:00.000000 gradio_client-0.0.8/README.md
+-rw-r--r--   0        0        0       78 2020-02-02 00:00:00.000000 gradio_client-0.0.8/requirements.txt
+-rw-r--r--   0        0        0      132 2020-02-02 00:00:00.000000 gradio_client-0.0.8/gradio_client/__init__.py
+-rw-r--r--   0        0        0    33173 2020-02-02 00:00:00.000000 gradio_client-0.0.8/gradio_client/client.py
+-rw-r--r--   0        0        0    10499 2020-02-02 00:00:00.000000 gradio_client-0.0.8/gradio_client/documentation.py
+-rw-r--r--   0        0        0    11484 2020-02-02 00:00:00.000000 gradio_client-0.0.8/gradio_client/serializing.py
+-rw-r--r--   0        0        0    10534 2020-02-02 00:00:00.000000 gradio_client-0.0.8/gradio_client/utils.py
+-rw-r--r--   0        0        0        6 2020-02-02 00:00:00.000000 gradio_client-0.0.8/gradio_client/version.txt
+-rw-r--r--   0        0        0      670 2020-02-02 00:00:00.000000 gradio_client-0.0.8/.gitignore
+-rw-r--r--   0        0        0     1367 2020-02-02 00:00:00.000000 gradio_client-0.0.8/pyproject.toml
+-rw-r--r--   0        0        0     7986 2020-02-02 00:00:00.000000 gradio_client-0.0.8/PKG-INFO
```

### Comparing `gradio_client-0.0.7/gradio_client/serializing.py` & `gradio_client-0.0.8/gradio_client/serializing.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,342 +1,345 @@
-from __future__ import annotations
-
-import json
-import os
-import uuid
-from abc import ABC, abstractmethod
-from pathlib import Path
-from typing import Any, Dict, List, Tuple
-
-from gradio_client import utils
-
-
-class Serializable(ABC):
-    @abstractmethod
-    def input_api_info(self) -> Tuple[str, str]:
-        """
-        Get the type of input that should be provided via API, and a human-readable description of the input as a tuple (for documentation generation).
-        """
-        pass
-
-    @abstractmethod
-    def output_api_info(self) -> Tuple[str, str]:
-        """
-        Get the type of output that should be returned via API, and a human-readable description of the output as a tuple (for documentation generation).
-        """
-        pass
-
-    def serialize(self, x: Any, load_dir: str | Path = ""):
-        """
-        Convert data from human-readable format to serialized format for a browser.
-        """
-        return x
-
-    def deserialize(
-        self,
-        x: Any,
-        save_dir: str | Path | None = None,
-        root_url: str | None = None,
-        hf_token: str | None = None,
-    ):
-        """
-        Convert data from serialized format for a browser to human-readable format.
-        """
-        return x
-
-
-class SimpleSerializable(Serializable):
-    """General class that does not perform any serialization or deserialization."""
-
-    def input_api_info(self) -> Tuple[str, str]:
-        return "Any", ""
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "Any", ""
-
-
-class StringSerializable(Serializable):
-    """Expects a string as input/output but performs no serialization."""
-
-    def input_api_info(self) -> Tuple[str, str]:
-        return "str", "value"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "str", "value"
-
-
-class ListStringSerializable(Serializable):
-    """Expects a list of strings as input/output but performs no serialization."""
-
-    def input_api_info(self) -> Tuple[str, str]:
-        return "List[str]", "values"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "List[str]", "values"
-
-
-class BooleanSerializable(Serializable):
-    """Expects a boolean as input/output but performs no serialization."""
-
-    def input_api_info(self) -> Tuple[str, str]:
-        return "bool", "value"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "bool", "value"
-
-
-class NumberSerializable(Serializable):
-    """Expects a number (int/float) as input/output but performs no serialization."""
-
-    def input_api_info(self) -> Tuple[str, str]:
-        return "int | float", "value"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "int | float", "value"
-
-
-class ImgSerializable(Serializable):
-    """Expects a base64 string as input/output which is ."""
-
-    def input_api_info(self) -> Tuple[str, str]:
-        return "str", "filepath or URL"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "str", "filepath or URL"
-
-    def serialize(
-        self,
-        x: str | None,
-        load_dir: str | Path = "",
-    ) -> str | None:
-        """
-        Convert from human-friendly version of a file (string filepath) to a seralized
-        representation (base64).
-        Parameters:
-            x: String path to file to serialize
-            load_dir: Path to directory containing x
-        """
-        if x is None or x == "":
-            return None
-        is_url = utils.is_valid_url(x)
-        path = x if is_url else Path(load_dir) / x
-        return utils.encode_url_or_file_to_base64(path)
-
-    def deserialize(
-        self,
-        x: str | None,
-        save_dir: str | Path | None = None,
-        root_url: str | None = None,
-        hf_token: str | None = None,
-    ) -> str | None:
-        """
-        Convert from serialized representation of a file (base64) to a human-friendly
-        version (string filepath). Optionally, save the file to the directory specified by save_dir
-        Parameters:
-            x: Base64 representation of image to deserialize into a string filepath
-            save_dir: Path to directory to save the deserialized image to
-            root_url: Ignored
-            hf_token: Ignored
-        """
-        if x is None or x == "":
-            return None
-        file = utils.decode_base64_to_file(x, dir=save_dir)
-        return file.name
-
-
-class FileSerializable(Serializable):
-    def input_api_info(self) -> Tuple[str, str]:
-        return "str", "filepath or URL"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "str", "filepath or URL"
-
-    def serialize(
-        self,
-        x: str | None,
-        load_dir: str | Path = "",
-    ) -> Dict | None:
-        """
-        Convert from human-friendly version of a file (string filepath) to a
-        seralized representation (base64)
-        Parameters:
-            x: String path to file to serialize
-            load_dir: Path to directory containing x
-        """
-        if x is None or x == "":
-            return None
-        filename = str(Path(load_dir) / x)
-        return {
-            "name": filename,
-            "data": utils.encode_url_or_file_to_base64(filename),
-            "orig_name": Path(filename).name,
-            "is_file": False,
-        }
-
-    def deserialize(
-        self,
-        x: str | Dict | None,
-        save_dir: Path | str | None = None,
-        root_url: str | None = None,
-        hf_token: str | None = None,
-    ) -> str | None:
-        """
-        Convert from serialized representation of a file (base64) to a human-friendly
-        version (string filepath). Optionally, save the file to the directory specified by `save_dir`
-        Parameters:
-            x: Base64 representation of file to deserialize into a string filepath
-            save_dir: Path to directory to save the deserialized file to
-            root_url: If this component is loaded from an external Space, this is the URL of the Space
-            hf_token: If this component is loaded from an external private Space, this is the access token for the Space
-        """
-        if x is None:
-            return None
-        if isinstance(save_dir, Path):
-            save_dir = str(save_dir)
-        if isinstance(x, str):
-            file_name = utils.decode_base64_to_file(x, dir=save_dir).name
-        elif isinstance(x, dict):
-            if x.get("is_file", False):
-                if root_url is not None:
-                    file_name = utils.download_tmp_copy_of_file(
-                        root_url + "file=" + x["name"],
-                        hf_token=hf_token,
-                        dir=save_dir,
-                    ).name
-                else:
-                    file_name = utils.create_tmp_copy_of_file(
-                        x["name"], dir=save_dir
-                    ).name
-            else:
-                file_name = utils.decode_base64_to_file(x["data"], dir=save_dir).name
-        else:
-            raise ValueError(
-                f"A FileSerializable component can only deserialize a string or a dict, not a: {type(x)}"
-            )
-        return file_name
-
-
-class JSONSerializable(Serializable):
-    def input_api_info(self) -> Tuple[str, str]:
-        return "str", "filepath to json file"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "str", "filepath to json file"
-
-    def serialize(
-        self,
-        x: str | None,
-        load_dir: str | Path = "",
-    ) -> Dict | None:
-        """
-        Convert from a a human-friendly version (string path to json file) to a
-        serialized representation (json string)
-        Parameters:
-            x: String path to json file to read to get json string
-            load_dir: Path to directory containing x
-        """
-        if x is None or x == "":
-            return None
-        return utils.file_to_json(Path(load_dir) / x)
-
-    def deserialize(
-        self,
-        x: str | Dict,
-        save_dir: str | Path | None = None,
-        root_url: str | None = None,
-        hf_token: str | None = None,
-    ) -> str | None:
-        """
-        Convert from serialized representation (json string) to a human-friendly
-        version (string path to json file).  Optionally, save the file to the directory specified by `save_dir`
-        Parameters:
-            x: Json string
-            save_dir: Path to save the deserialized json file to
-            root_url: Ignored
-            hf_token: Ignored
-        """
-        if x is None:
-            return None
-        return utils.dict_or_str_to_json_file(x, dir=save_dir).name
-
-
-class GallerySerializable(Serializable):
-    def input_api_info(self) -> Tuple[str, str]:
-        return "str", "path to directory with images and captions.json"
-
-    def output_api_info(self) -> Tuple[str, str]:
-        return "str", "path to directory with images and captions.json"
-
-    def serialize(
-        self, x: str | None, load_dir: str | Path = ""
-    ) -> List[List[str]] | None:
-        if x is None or x == "":
-            return None
-        files = []
-        captions_file = Path(x) / "captions.json"
-        with captions_file.open("r") as captions_json:
-            captions = json.load(captions_json)
-        for file_name, caption in captions.items():
-            img = FileSerializable().serialize(file_name)
-            files.append([img, caption])
-        return files
-
-    def deserialize(
-        self,
-        x: Any,
-        save_dir: str = "",
-        root_url: str | None = None,
-        hf_token: str | None = None,
-    ) -> None | str:
-        if x is None:
-            return None
-        gallery_path = Path(save_dir) / str(uuid.uuid4())
-        gallery_path.mkdir(exist_ok=True, parents=True)
-        captions = {}
-        for img_data in x:
-            if isinstance(img_data, list) or isinstance(img_data, tuple):
-                img_data, caption = img_data
-            else:
-                caption = None
-            name = FileSerializable().deserialize(
-                img_data, gallery_path, root_url=root_url, hf_token=hf_token
-            )
-            captions[name] = caption
-            captions_file = gallery_path / "captions.json"
-            with captions_file.open("w") as captions_json:
-                json.dump(captions, captions_json)
-        return os.path.abspath(gallery_path)
-
-
-SERIALIZER_MAPPING = {cls.__name__: cls for cls in Serializable.__subclasses__()}
-SERIALIZER_MAPPING["Serializable"] = SimpleSerializable
-
-COMPONENT_MAPPING: Dict[str, type] = {
-    "textbox": StringSerializable,
-    "number": NumberSerializable,
-    "slider": NumberSerializable,
-    "checkbox": BooleanSerializable,
-    "checkboxgroup": ListStringSerializable,
-    "radio": StringSerializable,
-    "dropdown": SimpleSerializable,
-    "image": ImgSerializable,
-    "video": FileSerializable,
-    "audio": FileSerializable,
-    "file": FileSerializable,
-    "dataframe": JSONSerializable,
-    "timeseries": JSONSerializable,
-    "state": SimpleSerializable,
-    "button": StringSerializable,
-    "uploadbutton": FileSerializable,
-    "colorpicker": StringSerializable,
-    "label": JSONSerializable,
-    "highlightedtext": JSONSerializable,
-    "json": JSONSerializable,
-    "html": StringSerializable,
-    "gallery": GallerySerializable,
-    "chatbot": JSONSerializable,
-    "model3d": FileSerializable,
-    "plot": JSONSerializable,
-    "markdown": StringSerializable,
-    "dataset": StringSerializable,
-    "code": StringSerializable,
-}
+from __future__ import annotations
+
+import json
+import os
+import uuid
+from abc import ABC, abstractmethod
+from pathlib import Path
+from typing import Any, Dict, List, Tuple
+
+from gradio_client import utils
+
+
+class Serializable(ABC):
+    @abstractmethod
+    def input_api_info(self) -> Tuple[str, str]:
+        """
+        Get the type of input that should be provided via API, and a human-readable description of the input as a tuple (for documentation generation).
+        """
+        pass
+
+    @abstractmethod
+    def output_api_info(self) -> Tuple[str, str]:
+        """
+        Get the type of output that should be returned via API, and a human-readable description of the output as a tuple (for documentation generation).
+        """
+        pass
+
+    def serialize(self, x: Any, load_dir: str | Path = ""):
+        """
+        Convert data from human-readable format to serialized format for a browser.
+        """
+        return x
+
+    def deserialize(
+        self,
+        x: Any,
+        save_dir: str | Path | None = None,
+        root_url: str | None = None,
+        hf_token: str | None = None,
+    ):
+        """
+        Convert data from serialized format for a browser to human-readable format.
+        """
+        return x
+
+
+class SimpleSerializable(Serializable):
+    """General class that does not perform any serialization or deserialization."""
+
+    def input_api_info(self) -> Tuple[str, str]:
+        return "Any", ""
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "Any", ""
+
+
+class StringSerializable(Serializable):
+    """Expects a string as input/output but performs no serialization."""
+
+    def input_api_info(self) -> Tuple[str, str]:
+        return "str", "value"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "str", "value"
+
+
+class ListStringSerializable(Serializable):
+    """Expects a list of strings as input/output but performs no serialization."""
+
+    def input_api_info(self) -> Tuple[str, str]:
+        return "List[str]", "values"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "List[str]", "values"
+
+
+class BooleanSerializable(Serializable):
+    """Expects a boolean as input/output but performs no serialization."""
+
+    def input_api_info(self) -> Tuple[str, str]:
+        return "bool", "value"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "bool", "value"
+
+
+class NumberSerializable(Serializable):
+    """Expects a number (int/float) as input/output but performs no serialization."""
+
+    def input_api_info(self) -> Tuple[str, str]:
+        return "int | float", "value"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "int | float", "value"
+
+
+class ImgSerializable(Serializable):
+    """Expects a base64 string as input/output which is ."""
+
+    def input_api_info(self) -> Tuple[str, str]:
+        return "str", "filepath or URL"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "str", "filepath or URL"
+
+    def serialize(
+        self,
+        x: str | None,
+        load_dir: str | Path = "",
+    ) -> str | None:
+        """
+        Convert from human-friendly version of a file (string filepath) to a seralized
+        representation (base64).
+        Parameters:
+            x: String path to file to serialize
+            load_dir: Path to directory containing x
+        """
+        if x is None or x == "":
+            return None
+        is_url = utils.is_valid_url(x)
+        path = x if is_url else Path(load_dir) / x
+        return utils.encode_url_or_file_to_base64(path)
+
+    def deserialize(
+        self,
+        x: str | None,
+        save_dir: str | Path | None = None,
+        root_url: str | None = None,
+        hf_token: str | None = None,
+    ) -> str | None:
+        """
+        Convert from serialized representation of a file (base64) to a human-friendly
+        version (string filepath). Optionally, save the file to the directory specified by save_dir
+        Parameters:
+            x: Base64 representation of image to deserialize into a string filepath
+            save_dir: Path to directory to save the deserialized image to
+            root_url: Ignored
+            hf_token: Ignored
+        """
+        if x is None or x == "":
+            return None
+        file = utils.decode_base64_to_file(x, dir=save_dir)
+        return file.name
+
+
+class FileSerializable(Serializable):
+    def input_api_info(self) -> Tuple[str, str]:
+        return "str", "filepath or URL"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "str", "filepath or URL"
+
+    def serialize(
+        self,
+        x: str | None,
+        load_dir: str | Path = "",
+    ) -> Dict | None:
+        """
+        Convert from human-friendly version of a file (string filepath) to a
+        seralized representation (base64)
+        Parameters:
+            x: String path to file to serialize
+            load_dir: Path to directory containing x
+        """
+        if x is None or x == "":
+            return None
+        if utils.is_valid_url(x):
+            filename = x
+        else:
+            filename = str(Path(load_dir) / x)
+        return {
+            "name": filename,
+            "data": utils.encode_url_or_file_to_base64(filename),
+            "orig_name": Path(filename).name,
+            "is_file": False,
+        }
+
+    def deserialize(
+        self,
+        x: str | Dict | None,
+        save_dir: Path | str | None = None,
+        root_url: str | None = None,
+        hf_token: str | None = None,
+    ) -> str | None:
+        """
+        Convert from serialized representation of a file (base64) to a human-friendly
+        version (string filepath). Optionally, save the file to the directory specified by `save_dir`
+        Parameters:
+            x: Base64 representation of file to deserialize into a string filepath
+            save_dir: Path to directory to save the deserialized file to
+            root_url: If this component is loaded from an external Space, this is the URL of the Space.
+            hf_token: If this component is loaded from an external private Space, this is the access token for the Space
+        """
+        if x is None:
+            return None
+        if isinstance(save_dir, Path):
+            save_dir = str(save_dir)
+        if isinstance(x, str):
+            file_name = utils.decode_base64_to_file(x, dir=save_dir).name
+        elif isinstance(x, dict):
+            if x.get("is_file", False):
+                if root_url is not None:
+                    file_name = utils.download_tmp_copy_of_file(
+                        root_url + "file=" + x["name"],
+                        hf_token=hf_token,
+                        dir=save_dir,
+                    ).name
+                else:
+                    file_name = utils.create_tmp_copy_of_file(
+                        x["name"], dir=save_dir
+                    ).name
+            else:
+                file_name = utils.decode_base64_to_file(x["data"], dir=save_dir).name
+        else:
+            raise ValueError(
+                f"A FileSerializable component can only deserialize a string or a dict, not a: {type(x)}"
+            )
+        return file_name
+
+
+class JSONSerializable(Serializable):
+    def input_api_info(self) -> Tuple[str, str]:
+        return "str", "filepath to json file"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "str", "filepath to json file"
+
+    def serialize(
+        self,
+        x: str | None,
+        load_dir: str | Path = "",
+    ) -> Dict | None:
+        """
+        Convert from a a human-friendly version (string path to json file) to a
+        serialized representation (json string)
+        Parameters:
+            x: String path to json file to read to get json string
+            load_dir: Path to directory containing x
+        """
+        if x is None or x == "":
+            return None
+        return utils.file_to_json(Path(load_dir) / x)
+
+    def deserialize(
+        self,
+        x: str | Dict,
+        save_dir: str | Path | None = None,
+        root_url: str | None = None,
+        hf_token: str | None = None,
+    ) -> str | None:
+        """
+        Convert from serialized representation (json string) to a human-friendly
+        version (string path to json file).  Optionally, save the file to the directory specified by `save_dir`
+        Parameters:
+            x: Json string
+            save_dir: Path to save the deserialized json file to
+            root_url: Ignored
+            hf_token: Ignored
+        """
+        if x is None:
+            return None
+        return utils.dict_or_str_to_json_file(x, dir=save_dir).name
+
+
+class GallerySerializable(Serializable):
+    def input_api_info(self) -> Tuple[str, str]:
+        return "str", "path to directory with images and captions.json"
+
+    def output_api_info(self) -> Tuple[str, str]:
+        return "str", "path to directory with images and captions.json"
+
+    def serialize(
+        self, x: str | None, load_dir: str | Path = ""
+    ) -> List[List[str]] | None:
+        if x is None or x == "":
+            return None
+        files = []
+        captions_file = Path(x) / "captions.json"
+        with captions_file.open("r") as captions_json:
+            captions = json.load(captions_json)
+        for file_name, caption in captions.items():
+            img = FileSerializable().serialize(file_name)
+            files.append([img, caption])
+        return files
+
+    def deserialize(
+        self,
+        x: Any,
+        save_dir: str = "",
+        root_url: str | None = None,
+        hf_token: str | None = None,
+    ) -> None | str:
+        if x is None:
+            return None
+        gallery_path = Path(save_dir) / str(uuid.uuid4())
+        gallery_path.mkdir(exist_ok=True, parents=True)
+        captions = {}
+        for img_data in x:
+            if isinstance(img_data, list) or isinstance(img_data, tuple):
+                img_data, caption = img_data
+            else:
+                caption = None
+            name = FileSerializable().deserialize(
+                img_data, gallery_path, root_url=root_url, hf_token=hf_token
+            )
+            captions[name] = caption
+            captions_file = gallery_path / "captions.json"
+            with captions_file.open("w") as captions_json:
+                json.dump(captions, captions_json)
+        return os.path.abspath(gallery_path)
+
+
+SERIALIZER_MAPPING = {cls.__name__: cls for cls in Serializable.__subclasses__()}
+SERIALIZER_MAPPING["Serializable"] = SimpleSerializable
+
+COMPONENT_MAPPING: Dict[str, type] = {
+    "textbox": StringSerializable,
+    "number": NumberSerializable,
+    "slider": NumberSerializable,
+    "checkbox": BooleanSerializable,
+    "checkboxgroup": ListStringSerializable,
+    "radio": StringSerializable,
+    "dropdown": SimpleSerializable,
+    "image": ImgSerializable,
+    "video": FileSerializable,
+    "audio": FileSerializable,
+    "file": FileSerializable,
+    "dataframe": JSONSerializable,
+    "timeseries": JSONSerializable,
+    "state": SimpleSerializable,
+    "button": StringSerializable,
+    "uploadbutton": FileSerializable,
+    "colorpicker": StringSerializable,
+    "label": JSONSerializable,
+    "highlightedtext": JSONSerializable,
+    "json": JSONSerializable,
+    "html": StringSerializable,
+    "gallery": GallerySerializable,
+    "chatbot": JSONSerializable,
+    "model3d": FileSerializable,
+    "plot": JSONSerializable,
+    "markdown": StringSerializable,
+    "dataset": StringSerializable,
+    "code": StringSerializable,
+}
```

### Comparing `gradio_client-0.0.7/gradio_client/utils.py` & `gradio_client-0.0.8/gradio_client/utils.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,359 +1,367 @@
-from __future__ import annotations
-
-import base64
-import json
-import mimetypes
-import os
-import pkgutil
-import shutil
-import tempfile
-from dataclasses import dataclass, field
-from datetime import datetime
-from enum import Enum
-from pathlib import Path
-from threading import Lock
-from typing import Any, Callable, Dict, List, Tuple
-
-import fsspec.asyn
-import requests
-from websockets.legacy.protocol import WebSocketCommonProtocol
-
-API_URL = "{}/api/predict/"
-WS_URL = "{}/queue/join"
-STATE_COMPONENT = "state"
-
-__version__ = (pkgutil.get_data(__name__, "version.txt") or b"").decode("ascii").strip()
-
-
-class TooManyRequestsError(Exception):
-    """Raised when the API returns a 429 status code."""
-
-    pass
-
-
-class QueueError(Exception):
-    """Raised when the queue is full or there is an issue adding a job to the queue."""
-
-    pass
-
-
-class InvalidAPIEndpointError(Exception):
-    """Raised when the API endpoint is invalid."""
-
-    pass
-
-
-class Status(Enum):
-    """Status codes presented to client users."""
-
-    STARTING = "STARTING"
-    JOINING_QUEUE = "JOINING_QUEUE"
-    QUEUE_FULL = "QUEUE_FULL"
-    IN_QUEUE = "IN_QUEUE"
-    SENDING_DATA = "SENDING_DATA"
-    PROCESSING = "PROCESSSING"
-    ITERATING = "ITERATING"
-    FINISHED = "FINISHED"
-
-    @staticmethod
-    def ordering(status: "Status") -> int:
-        """Order of messages. Helpful for testing."""
-        order = [
-            Status.STARTING,
-            Status.JOINING_QUEUE,
-            Status.QUEUE_FULL,
-            Status.IN_QUEUE,
-            Status.SENDING_DATA,
-            Status.PROCESSING,
-            Status.ITERATING,
-            Status.FINISHED,
-        ]
-        return order.index(status)
-
-    def __lt__(self, other: "Status"):
-        return self.ordering(self) < self.ordering(other)
-
-    @staticmethod
-    def msg_to_status(msg: str) -> "Status":
-        """Map the raw message from the backend to the status code presented to users."""
-        return {
-            "send_hash": Status.JOINING_QUEUE,
-            "queue_full": Status.QUEUE_FULL,
-            "estimation": Status.IN_QUEUE,
-            "send_data": Status.SENDING_DATA,
-            "process_starts": Status.PROCESSING,
-            "process_generating": Status.ITERATING,
-            "process_completed": Status.FINISHED,
-        }[msg]
-
-
-@dataclass
-class StatusUpdate:
-    """Update message sent from the worker thread to the Job on the main thread."""
-
-    code: Status
-    rank: int | None
-    queue_size: int | None
-    eta: float | None
-    success: bool | None
-    time: datetime | None
-
-
-def create_initial_status_update():
-    return StatusUpdate(
-        code=Status.STARTING,
-        rank=None,
-        queue_size=None,
-        eta=None,
-        success=None,
-        time=datetime.now(),
-    )
-
-
-@dataclass
-class JobStatus:
-    """The job status.
-
-    Keeps strack of the latest status update and intermediate outputs (not yet implements).
-    """
-
-    latest_status: StatusUpdate = field(default_factory=create_initial_status_update)
-    outputs: List[Any] = field(default_factory=list)
-
-
-@dataclass
-class Communicator:
-    """Helper class to help communicate between the worker thread and main thread."""
-
-    lock: Lock
-    job: JobStatus
-
-
-########################
-# Network utils
-########################
-
-
-def is_valid_url(possible_url: str) -> bool:
-    headers = {"User-Agent": "gradio (https://gradio.app/; team@gradio.app)"}
-    try:
-        head_request = requests.head(possible_url, headers=headers)
-        if head_request.status_code == 405:
-            return requests.get(possible_url, headers=headers).ok
-        return head_request.ok
-    except Exception:
-        return False
-
-
-async def get_pred_from_ws(
-    websocket: WebSocketCommonProtocol,
-    data: str,
-    hash_data: str,
-    helper: Communicator | None = None,
-) -> Dict[str, Any]:
-    completed = False
-    resp = {}
-    while not completed:
-        msg = await websocket.recv()
-        resp = json.loads(msg)
-        if helper:
-            with helper.lock:
-                status_update = StatusUpdate(
-                    code=Status.msg_to_status(resp["msg"]),
-                    queue_size=resp.get("queue_size"),
-                    rank=resp.get("rank", None),
-                    success=resp.get("success"),
-                    time=datetime.now(),
-                    eta=resp.get("rank_eta"),
-                )
-                helper.job.latest_status = status_update
-        if resp["msg"] == "queue_full":
-            raise QueueError("Queue is full! Please try again.")
-        if resp["msg"] == "send_hash":
-            await websocket.send(hash_data)
-        elif resp["msg"] == "send_data":
-            await websocket.send(data)
-        completed = resp["msg"] == "process_completed"
-    return resp["output"]
-
-
-########################
-# Data processing utils
-########################
-
-
-def download_tmp_copy_of_file(
-    url_path: str, hf_token: str | None = None, dir: str | None = None
-) -> tempfile._TemporaryFileWrapper:
-    if dir is not None:
-        os.makedirs(dir, exist_ok=True)
-    headers = {"Authorization": "Bearer " + hf_token} if hf_token else {}
-    prefix = Path(url_path).stem
-    suffix = Path(url_path).suffix
-    file_obj = tempfile.NamedTemporaryFile(
-        delete=False,
-        prefix=prefix,
-        suffix=suffix,
-        dir=dir,
-    )
-    with requests.get(url_path, headers=headers, stream=True) as r:
-        with open(file_obj.name, "wb") as f:
-            shutil.copyfileobj(r.raw, f)
-    return file_obj
-
-
-def create_tmp_copy_of_file(
-    file_path: str, dir: str | None = None
-) -> tempfile._TemporaryFileWrapper:
-    if dir is not None:
-        os.makedirs(dir, exist_ok=True)
-    prefix = Path(file_path).stem
-    suffix = Path(file_path).suffix
-    file_obj = tempfile.NamedTemporaryFile(
-        delete=False,
-        prefix=prefix,
-        suffix=suffix,
-        dir=dir,
-    )
-    shutil.copy2(file_path, file_obj.name)
-    return file_obj
-
-
-def get_mimetype(filename: str) -> str | None:
-    mimetype = mimetypes.guess_type(filename)[0]
-    if mimetype is not None:
-        mimetype = mimetype.replace("x-wav", "wav").replace("x-flac", "flac")
-    return mimetype
-
-
-def get_extension(encoding: str) -> str | None:
-    encoding = encoding.replace("audio/wav", "audio/x-wav")
-    type = mimetypes.guess_type(encoding)[0]
-    if type == "audio/flac":  # flac is not supported by mimetypes
-        return "flac"
-    elif type is None:
-        return None
-    extension = mimetypes.guess_extension(type)
-    if extension is not None and extension.startswith("."):
-        extension = extension[1:]
-    return extension
-
-
-def encode_file_to_base64(f):
-    with open(f, "rb") as file:
-        encoded_string = base64.b64encode(file.read())
-        base64_str = str(encoded_string, "utf-8")
-        mimetype = get_mimetype(f)
-        return (
-            "data:"
-            + (mimetype if mimetype is not None else "")
-            + ";base64,"
-            + base64_str
-        )
-
-
-def encode_url_to_base64(url):
-    encoded_string = base64.b64encode(requests.get(url).content)
-    base64_str = str(encoded_string, "utf-8")
-    mimetype = get_mimetype(url)
-    return (
-        "data:" + (mimetype if mimetype is not None else "") + ";base64," + base64_str
-    )
-
-
-def encode_url_or_file_to_base64(path: str | Path):
-    path = str(path)
-    if is_valid_url(path):
-        return encode_url_to_base64(path)
-    else:
-        return encode_file_to_base64(path)
-
-
-def decode_base64_to_binary(encoding) -> Tuple[bytes, str | None]:
-    extension = get_extension(encoding)
-    try:
-        data = encoding.split(",")[1]
-    except IndexError:
-        data = ""
-    return base64.b64decode(data), extension
-
-
-def strip_invalid_filename_characters(filename: str, max_bytes: int = 200) -> str:
-    """Strips invalid characters from a filename and ensures that the file_length is less than `max_bytes` bytes."""
-    filename = "".join([char for char in filename if char.isalnum() or char in "._- "])
-    filename_len = len(filename.encode())
-    if filename_len > max_bytes:
-        while filename_len > max_bytes:
-            if len(filename) == 0:
-                break
-            filename = filename[:-1]
-            filename_len = len(filename.encode())
-    return filename
-
-
-def decode_base64_to_file(encoding, file_path=None, dir=None, prefix=None):
-    if dir is not None:
-        os.makedirs(dir, exist_ok=True)
-    data, extension = decode_base64_to_binary(encoding)
-    if file_path is not None and prefix is None:
-        filename = Path(file_path).name
-        prefix = filename
-        if "." in filename:
-            prefix = filename[0 : filename.index(".")]
-            extension = filename[filename.index(".") + 1 :]
-
-    if prefix is not None:
-        prefix = strip_invalid_filename_characters(prefix)
-
-    if extension is None:
-        file_obj = tempfile.NamedTemporaryFile(delete=False, prefix=prefix, dir=dir)
-    else:
-        file_obj = tempfile.NamedTemporaryFile(
-            delete=False,
-            prefix=prefix,
-            suffix="." + extension,
-            dir=dir,
-        )
-    file_obj.write(data)
-    file_obj.flush()
-    return file_obj
-
-
-def dict_or_str_to_json_file(jsn, dir=None):
-    if dir is not None:
-        os.makedirs(dir, exist_ok=True)
-
-    file_obj = tempfile.NamedTemporaryFile(
-        delete=False, suffix=".json", dir=dir, mode="w+"
-    )
-    if isinstance(jsn, str):
-        jsn = json.loads(jsn)
-    json.dump(jsn, file_obj)
-    file_obj.flush()
-    return file_obj
-
-
-def file_to_json(file_path: str | Path) -> Dict:
-    with open(file_path) as f:
-        return json.load(f)
-
-
-########################
-# Misc utils
-########################
-
-
-def synchronize_async(func: Callable, *args, **kwargs) -> Any:
-    """
-    Runs async functions in sync scopes. Can be used in any scope.
-
-    Example:
-        if inspect.iscoroutinefunction(block_fn.fn):
-            predictions = utils.synchronize_async(block_fn.fn, *processed_input)
-
-    Args:
-        func:
-        *args:
-        **kwargs:
-    """
-    return fsspec.asyn.sync(fsspec.asyn.get_loop(), func, *args, **kwargs)  # type: ignore
+from __future__ import annotations
+
+import base64
+import json
+import mimetypes
+import os
+import pkgutil
+import shutil
+import tempfile
+from dataclasses import dataclass, field
+from datetime import datetime
+from enum import Enum
+from pathlib import Path
+from threading import Lock
+from typing import Any, Callable, Dict, List, Tuple
+
+import fsspec.asyn
+import requests
+from websockets.legacy.protocol import WebSocketCommonProtocol
+
+API_URL = "{}/api/predict/"
+WS_URL = "{}/queue/join"
+STATE_COMPONENT = "state"
+
+__version__ = (pkgutil.get_data(__name__, "version.txt") or b"").decode("ascii").strip()
+
+
+class TooManyRequestsError(Exception):
+    """Raised when the API returns a 429 status code."""
+
+    pass
+
+
+class QueueError(Exception):
+    """Raised when the queue is full or there is an issue adding a job to the queue."""
+
+    pass
+
+
+class InvalidAPIEndpointError(Exception):
+    """Raised when the API endpoint is invalid."""
+
+    pass
+
+
+class Status(Enum):
+    """Status codes presented to client users."""
+
+    STARTING = "STARTING"
+    JOINING_QUEUE = "JOINING_QUEUE"
+    QUEUE_FULL = "QUEUE_FULL"
+    IN_QUEUE = "IN_QUEUE"
+    SENDING_DATA = "SENDING_DATA"
+    PROCESSING = "PROCESSSING"
+    ITERATING = "ITERATING"
+    FINISHED = "FINISHED"
+
+    @staticmethod
+    def ordering(status: "Status") -> int:
+        """Order of messages. Helpful for testing."""
+        order = [
+            Status.STARTING,
+            Status.JOINING_QUEUE,
+            Status.QUEUE_FULL,
+            Status.IN_QUEUE,
+            Status.SENDING_DATA,
+            Status.PROCESSING,
+            Status.ITERATING,
+            Status.FINISHED,
+        ]
+        return order.index(status)
+
+    def __lt__(self, other: "Status"):
+        return self.ordering(self) < self.ordering(other)
+
+    @staticmethod
+    def msg_to_status(msg: str) -> "Status":
+        """Map the raw message from the backend to the status code presented to users."""
+        return {
+            "send_hash": Status.JOINING_QUEUE,
+            "queue_full": Status.QUEUE_FULL,
+            "estimation": Status.IN_QUEUE,
+            "send_data": Status.SENDING_DATA,
+            "process_starts": Status.PROCESSING,
+            "process_generating": Status.ITERATING,
+            "process_completed": Status.FINISHED,
+        }[msg]
+
+
+@dataclass
+class StatusUpdate:
+    """Update message sent from the worker thread to the Job on the main thread."""
+
+    code: Status
+    rank: int | None
+    queue_size: int | None
+    eta: float | None
+    success: bool | None
+    time: datetime | None
+
+
+def create_initial_status_update():
+    return StatusUpdate(
+        code=Status.STARTING,
+        rank=None,
+        queue_size=None,
+        eta=None,
+        success=None,
+        time=datetime.now(),
+    )
+
+
+@dataclass
+class JobStatus:
+    """The job status.
+
+    Keeps strack of the latest status update and intermediate outputs (not yet implements).
+    """
+
+    latest_status: StatusUpdate = field(default_factory=create_initial_status_update)
+    outputs: List[Any] = field(default_factory=list)
+
+
+@dataclass
+class Communicator:
+    """Helper class to help communicate between the worker thread and main thread."""
+
+    lock: Lock
+    job: JobStatus
+    deserialize: Callable[..., Tuple]
+
+
+########################
+# Network utils
+########################
+
+
+def is_valid_url(possible_url: str) -> bool:
+    headers = {"User-Agent": "gradio (https://gradio.app/; team@gradio.app)"}
+    try:
+        head_request = requests.head(possible_url, headers=headers)
+        if head_request.status_code == 405:
+            return requests.get(possible_url, headers=headers).ok
+        return head_request.ok
+    except Exception:
+        return False
+
+
+async def get_pred_from_ws(
+    websocket: WebSocketCommonProtocol,
+    data: str,
+    hash_data: str,
+    helper: Communicator | None = None,
+) -> Dict[str, Any]:
+    completed = False
+    resp = {}
+    while not completed:
+        msg = await websocket.recv()
+        resp = json.loads(msg)
+        if helper:
+            with helper.lock:
+                status_update = StatusUpdate(
+                    code=Status.msg_to_status(resp["msg"]),
+                    queue_size=resp.get("queue_size"),
+                    rank=resp.get("rank", None),
+                    success=resp.get("success"),
+                    time=datetime.now(),
+                    eta=resp.get("rank_eta"),
+                )
+                output = resp.get("output", {}).get("data", [])
+                if output and status_update.code != Status.FINISHED:
+                    try:
+                        result = helper.deserialize(*output)
+                    except Exception as e:
+                        result = [e]
+                    helper.job.outputs.append(result)
+                helper.job.latest_status = status_update
+        if resp["msg"] == "queue_full":
+            raise QueueError("Queue is full! Please try again.")
+        if resp["msg"] == "send_hash":
+            await websocket.send(hash_data)
+        elif resp["msg"] == "send_data":
+            await websocket.send(data)
+        completed = resp["msg"] == "process_completed"
+    return resp["output"]
+
+
+########################
+# Data processing utils
+########################
+
+
+def download_tmp_copy_of_file(
+    url_path: str, hf_token: str | None = None, dir: str | None = None
+) -> tempfile._TemporaryFileWrapper:
+    if dir is not None:
+        os.makedirs(dir, exist_ok=True)
+    headers = {"Authorization": "Bearer " + hf_token} if hf_token else {}
+    prefix = Path(url_path).stem
+    suffix = Path(url_path).suffix
+    file_obj = tempfile.NamedTemporaryFile(
+        delete=False,
+        prefix=prefix,
+        suffix=suffix,
+        dir=dir,
+    )
+    with requests.get(url_path, headers=headers, stream=True) as r:
+        with open(file_obj.name, "wb") as f:
+            shutil.copyfileobj(r.raw, f)
+    return file_obj
+
+
+def create_tmp_copy_of_file(
+    file_path: str, dir: str | None = None
+) -> tempfile._TemporaryFileWrapper:
+    if dir is not None:
+        os.makedirs(dir, exist_ok=True)
+    prefix = Path(file_path).stem
+    suffix = Path(file_path).suffix
+    file_obj = tempfile.NamedTemporaryFile(
+        delete=False,
+        prefix=prefix,
+        suffix=suffix,
+        dir=dir,
+    )
+    shutil.copy2(file_path, file_obj.name)
+    return file_obj
+
+
+def get_mimetype(filename: str) -> str | None:
+    mimetype = mimetypes.guess_type(filename)[0]
+    if mimetype is not None:
+        mimetype = mimetype.replace("x-wav", "wav").replace("x-flac", "flac")
+    return mimetype
+
+
+def get_extension(encoding: str) -> str | None:
+    encoding = encoding.replace("audio/wav", "audio/x-wav")
+    type = mimetypes.guess_type(encoding)[0]
+    if type == "audio/flac":  # flac is not supported by mimetypes
+        return "flac"
+    elif type is None:
+        return None
+    extension = mimetypes.guess_extension(type)
+    if extension is not None and extension.startswith("."):
+        extension = extension[1:]
+    return extension
+
+
+def encode_file_to_base64(f):
+    with open(f, "rb") as file:
+        encoded_string = base64.b64encode(file.read())
+        base64_str = str(encoded_string, "utf-8")
+        mimetype = get_mimetype(f)
+        return (
+            "data:"
+            + (mimetype if mimetype is not None else "")
+            + ";base64,"
+            + base64_str
+        )
+
+
+def encode_url_to_base64(url):
+    encoded_string = base64.b64encode(requests.get(url).content)
+    base64_str = str(encoded_string, "utf-8")
+    mimetype = get_mimetype(url)
+    return (
+        "data:" + (mimetype if mimetype is not None else "") + ";base64," + base64_str
+    )
+
+
+def encode_url_or_file_to_base64(path: str | Path):
+    path = str(path)
+    if is_valid_url(path):
+        return encode_url_to_base64(path)
+    else:
+        return encode_file_to_base64(path)
+
+
+def decode_base64_to_binary(encoding) -> Tuple[bytes, str | None]:
+    extension = get_extension(encoding)
+    try:
+        data = encoding.split(",")[1]
+    except IndexError:
+        data = ""
+    return base64.b64decode(data), extension
+
+
+def strip_invalid_filename_characters(filename: str, max_bytes: int = 200) -> str:
+    """Strips invalid characters from a filename and ensures that the file_length is less than `max_bytes` bytes."""
+    filename = "".join([char for char in filename if char.isalnum() or char in "._- "])
+    filename_len = len(filename.encode())
+    if filename_len > max_bytes:
+        while filename_len > max_bytes:
+            if len(filename) == 0:
+                break
+            filename = filename[:-1]
+            filename_len = len(filename.encode())
+    return filename
+
+
+def decode_base64_to_file(encoding, file_path=None, dir=None, prefix=None):
+    if dir is not None:
+        os.makedirs(dir, exist_ok=True)
+    data, extension = decode_base64_to_binary(encoding)
+    if file_path is not None and prefix is None:
+        filename = Path(file_path).name
+        prefix = filename
+        if "." in filename:
+            prefix = filename[0 : filename.index(".")]
+            extension = filename[filename.index(".") + 1 :]
+
+    if prefix is not None:
+        prefix = strip_invalid_filename_characters(prefix)
+
+    if extension is None:
+        file_obj = tempfile.NamedTemporaryFile(delete=False, prefix=prefix, dir=dir)
+    else:
+        file_obj = tempfile.NamedTemporaryFile(
+            delete=False,
+            prefix=prefix,
+            suffix="." + extension,
+            dir=dir,
+        )
+    file_obj.write(data)
+    file_obj.flush()
+    return file_obj
+
+
+def dict_or_str_to_json_file(jsn, dir=None):
+    if dir is not None:
+        os.makedirs(dir, exist_ok=True)
+
+    file_obj = tempfile.NamedTemporaryFile(
+        delete=False, suffix=".json", dir=dir, mode="w+"
+    )
+    if isinstance(jsn, str):
+        jsn = json.loads(jsn)
+    json.dump(jsn, file_obj)
+    file_obj.flush()
+    return file_obj
+
+
+def file_to_json(file_path: str | Path) -> Dict:
+    with open(file_path) as f:
+        return json.load(f)
+
+
+########################
+# Misc utils
+########################
+
+
+def synchronize_async(func: Callable, *args, **kwargs) -> Any:
+    """
+    Runs async functions in sync scopes. Can be used in any scope.
+
+    Example:
+        if inspect.iscoroutinefunction(block_fn.fn):
+            predictions = utils.synchronize_async(block_fn.fn, *processed_input)
+
+    Args:
+        func:
+        *args:
+        **kwargs:
+    """
+    return fsspec.asyn.sync(fsspec.asyn.get_loop(), func, *args, **kwargs)  # type: ignore
```

### Comparing `gradio_client-0.0.7/pyproject.toml` & `gradio_client-0.0.8/pyproject.toml`

 * *Ordering differences only*

 * *Files 26% similar despite different names*

```diff
@@ -1,51 +1,51 @@
-[build-system]
-requires = ["hatchling", "hatch-requirements-txt", "hatch-fancy-pypi-readme>=22.5.0"]
-build-backend = "hatchling.build"
-
-[project]
-name = "gradio_client"
-dynamic = ["version", "dependencies", "readme"]
-description = "Python library for easily interacting with trained machine learning models"
-license = "Apache-2.0"
-requires-python = ">=3.7"
-authors = [
-  { name = "Abubakar Abid", email = "team@gradio.app" },
-  { name = "Ali Abid", email = "team@gradio.app" },
-  { name = "Ali Abdalla", email = "team@gradio.app" },
-  { name = "Dawood Khan", email = "team@gradio.app" },
-  { name = "Ahsen Khaliq", email = "team@gradio.app" },
-  { name = "Pete Allen", email = "team@gradio.app" },
-  { name = "Freddy Boulton", email = "team@gradio.app" },
-]
-keywords = ["machine learning", "client", "API"]
-
-[project.urls]
-Homepage = "https://github.com/gradio-app/gradio"
-
-[tool.hatch.version]
-path = "gradio_client/version.txt"
-pattern = "(?P<version>.+)"
-
-[tool.hatch.metadata.hooks.requirements_txt]
-filename = "requirements.txt"
-
-[tool.hatch.metadata.hooks.fancy-pypi-readme]
-content-type = "text/markdown"
-fragments = [
-  { path = "README.md" },
-]
-
-[tool.hatch.build.targets.sdist]
-include = [
-  "/gradio_client",
-  "/README.md",
-  "/requirements.txt",
-]
-
-[tool.ruff]
-extend = "../../pyproject.toml"
-
-[tool.ruff.isort]
-known-first-party = [
-  "gradio_client"
-]
+[build-system]
+requires = ["hatchling", "hatch-requirements-txt", "hatch-fancy-pypi-readme>=22.5.0"]
+build-backend = "hatchling.build"
+
+[project]
+name = "gradio_client"
+dynamic = ["version", "dependencies", "readme"]
+description = "Python library for easily interacting with trained machine learning models"
+license = "Apache-2.0"
+requires-python = ">=3.7"
+authors = [
+  { name = "Abubakar Abid", email = "team@gradio.app" },
+  { name = "Ali Abid", email = "team@gradio.app" },
+  { name = "Ali Abdalla", email = "team@gradio.app" },
+  { name = "Dawood Khan", email = "team@gradio.app" },
+  { name = "Ahsen Khaliq", email = "team@gradio.app" },
+  { name = "Pete Allen", email = "team@gradio.app" },
+  { name = "Freddy Boulton", email = "team@gradio.app" },
+]
+keywords = ["machine learning", "client", "API"]
+
+[project.urls]
+Homepage = "https://github.com/gradio-app/gradio"
+
+[tool.hatch.version]
+path = "gradio_client/version.txt"
+pattern = "(?P<version>.+)"
+
+[tool.hatch.metadata.hooks.requirements_txt]
+filename = "requirements.txt"
+
+[tool.hatch.metadata.hooks.fancy-pypi-readme]
+content-type = "text/markdown"
+fragments = [
+  { path = "README.md" },
+]
+
+[tool.hatch.build.targets.sdist]
+include = [
+  "/gradio_client",
+  "/README.md",
+  "/requirements.txt",
+]
+
+[tool.ruff]
+extend = "../../pyproject.toml"
+
+[tool.ruff.isort]
+known-first-party = [
+  "gradio_client"
+]
```

