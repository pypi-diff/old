# Comparing `tmp/kor-0.6.1.tar.gz` & `tmp/kor-0.7.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kor-0.6.1.tar", max compression
+gzip compressed data, was "kor-0.7.0.tar", max compression
```

## Comparing `kor-0.6.1.tar` & `kor-0.7.0.tar`

### file list

```diff
@@ -1,24 +1,24 @@
--rw-r--r--   0        0        0     1071 2023-04-04 17:58:16.932065 kor-0.6.1/LICENSE
--rw-r--r--   0        0        0     4273 2023-04-04 17:58:16.932065 kor-0.6.1/README.md
--rw-r--r--   0        0        0      632 2023-04-04 17:58:16.936065 kor-0.6.1/kor/__init__.py
--rw-r--r--   0        0        0     5123 2023-04-04 17:58:16.936065 kor-0.6.1/kor/adapters.py
--rw-r--r--   0        0        0      578 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/__init__.py
--rw-r--r--   0        0        0     4744 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/csv_data.py
--rw-r--r--   0        0        0     3513 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/encode.py
--rw-r--r--   0        0        0     2815 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/json_data.py
--rw-r--r--   0        0        0     2133 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/parser.py
--rw-r--r--   0        0        0     1515 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/typedefs.py
--rw-r--r--   0        0        0      514 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/utils.py
--rw-r--r--   0        0        0     6093 2023-04-04 17:58:16.936065 kor-0.6.1/kor/encoders/xml.py
--rw-r--r--   0        0        0     4103 2023-04-04 17:58:16.936065 kor-0.6.1/kor/examples.py
--rw-r--r--   0        0        0      225 2023-04-04 17:58:16.936065 kor-0.6.1/kor/exceptions.py
--rw-r--r--   0        0        0     2721 2023-04-04 17:58:16.936065 kor-0.6.1/kor/extraction.py
--rw-r--r--   0        0        0     9553 2023-04-04 17:58:16.936065 kor-0.6.1/kor/nodes.py
--rw-r--r--   0        0        0     5132 2023-04-04 17:58:16.936065 kor-0.6.1/kor/prompts.py
--rw-r--r--   0        0        0        0 2023-04-04 17:58:16.936065 kor-0.6.1/kor/py.typed
--rw-r--r--   0        0        0     4493 2023-04-04 17:58:16.936065 kor-0.6.1/kor/type_descriptors.py
--rw-r--r--   0        0        0     2055 2023-04-04 17:58:16.936065 kor-0.6.1/kor/validators.py
--rw-r--r--   0        0        0      181 2023-04-04 17:58:16.936065 kor-0.6.1/kor/version.py
--rw-r--r--   0        0        0     1935 2023-04-04 17:58:16.936065 kor-0.6.1/pyproject.toml
--rw-r--r--   0        0        0     5148 1970-01-01 00:00:00.000000 kor-0.6.1/setup.py
--rw-r--r--   0        0        0     4984 1970-01-01 00:00:00.000000 kor-0.6.1/PKG-INFO
+-rw-r--r--   0        0        0     1071 2023-04-06 13:54:36.507368 kor-0.7.0/LICENSE
+-rw-r--r--   0        0        0     4273 2023-04-06 13:54:36.507368 kor-0.7.0/README.md
+-rw-r--r--   0        0        0      632 2023-04-06 13:54:36.511369 kor-0.7.0/kor/__init__.py
+-rw-r--r--   0        0        0     5123 2023-04-06 13:54:36.511369 kor-0.7.0/kor/adapters.py
+-rw-r--r--   0        0        0      578 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/__init__.py
+-rw-r--r--   0        0        0     4744 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/csv_data.py
+-rw-r--r--   0        0        0     3513 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/encode.py
+-rw-r--r--   0        0        0     2815 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/json_data.py
+-rw-r--r--   0        0        0     2133 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/parser.py
+-rw-r--r--   0        0        0     1515 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/typedefs.py
+-rw-r--r--   0        0        0      514 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/utils.py
+-rw-r--r--   0        0        0     6093 2023-04-06 13:54:36.511369 kor-0.7.0/kor/encoders/xml.py
+-rw-r--r--   0        0        0     4103 2023-04-06 13:54:36.511369 kor-0.7.0/kor/examples.py
+-rw-r--r--   0        0        0      225 2023-04-06 13:54:36.511369 kor-0.7.0/kor/exceptions.py
+-rw-r--r--   0        0        0     3261 2023-04-06 13:54:36.511369 kor-0.7.0/kor/extraction.py
+-rw-r--r--   0        0        0     6884 2023-04-06 13:54:36.511369 kor-0.7.0/kor/nodes.py
+-rw-r--r--   0        0        0     5756 2023-04-06 13:54:36.511369 kor-0.7.0/kor/prompts.py
+-rw-r--r--   0        0        0        0 2023-04-06 13:54:36.511369 kor-0.7.0/kor/py.typed
+-rw-r--r--   0        0        0     4493 2023-04-06 13:54:36.511369 kor-0.7.0/kor/type_descriptors.py
+-rw-r--r--   0        0        0     2055 2023-04-06 13:54:36.511369 kor-0.7.0/kor/validators.py
+-rw-r--r--   0        0        0      181 2023-04-06 13:54:36.511369 kor-0.7.0/kor/version.py
+-rw-r--r--   0        0        0     1935 2023-04-06 13:54:36.511369 kor-0.7.0/pyproject.toml
+-rw-r--r--   0        0        0     5148 1970-01-01 00:00:00.000000 kor-0.7.0/setup.py
+-rw-r--r--   0        0        0     4984 1970-01-01 00:00:00.000000 kor-0.7.0/PKG-INFO
```

### Comparing `kor-0.6.1/LICENSE` & `kor-0.7.0/LICENSE`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/README.md` & `kor-0.7.0/README.md`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/__init__.py` & `kor-0.7.0/kor/__init__.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/adapters.py` & `kor-0.7.0/kor/adapters.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/__init__.py` & `kor-0.7.0/kor/encoders/__init__.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/csv_data.py` & `kor-0.7.0/kor/encoders/csv_data.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/encode.py` & `kor-0.7.0/kor/encoders/encode.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/json_data.py` & `kor-0.7.0/kor/encoders/json_data.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/parser.py` & `kor-0.7.0/kor/encoders/parser.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/typedefs.py` & `kor-0.7.0/kor/encoders/typedefs.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/utils.py` & `kor-0.7.0/kor/encoders/utils.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/encoders/xml.py` & `kor-0.7.0/kor/encoders/xml.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/examples.py` & `kor-0.7.0/kor/examples.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/extraction.py` & `kor-0.7.0/kor/extraction.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 from typing import Any, Optional, Type, Union
 
+from langchain import PromptTemplate
 from langchain.chains import LLMChain
 from langchain.schema import BaseLanguageModel
 
 from kor.encoders import Encoder, InputFormatter, initialize_encoder
 from kor.nodes import Object
 from kor.prompts import create_langchain_prompt
 from kor.type_descriptors import TypeDescriptor, initialize_type_descriptors
@@ -16,33 +17,39 @@
     llm: BaseLanguageModel,
     node: Object,
     *,
     encoder_or_encoder_class: Union[Type[Encoder], Encoder, str] = "csv",
     type_descriptor: Union[TypeDescriptor, str] = "typescript",
     validator: Optional[Validator] = None,
     input_formatter: InputFormatter = None,
+    instruction_template: Optional[PromptTemplate] = None,
     **encoder_kwargs: Any,
 ) -> LLMChain:
     """Create an extraction chain.
     
     Args:
         llm: the language model used for extraction
         node: the schematic description of what to extract from text
         encoder_or_encoder_class: Either an encoder instance, an encoder class
                                   or a string representing the encoder class
         type_descriptor: either a TypeDescriptor or a string representing the type \
                          descriptor name
         validator: optional validator to use for validation
         input_formatter: the formatter to use for encoding the input. Used for \
                          both input examples and the text to be analyzed.
-                         
             * `None`: use for single sentences or single paragraph, no formatting
             * `triple_quotes`: for long text, surround input with \"\"\"
             * `text_prefix`: for long text, triple_quote with `TEXT: ` prefix
             * `Callable`: user provided function
+        instruction_template: optional prompt template to use, use to over-ride prompt
+             used for generating the instruction section of the prompt.
+             It accepts 2 optional input variables:
+             * "type_description": type description of the node (from TypeDescriptor)
+             * "format_instructions": information on how to format the output
+               (from Encoder)
         encoder_kwargs: Keyword arguments to pass to the encoder class
 
     Returns:
         A langchain chain
         
         
     Examples:
@@ -62,11 +69,12 @@
     type_descriptor_to_use = initialize_type_descriptors(type_descriptor)
     return LLMChain(
         llm=llm,
         prompt=create_langchain_prompt(
             node,
             encoder,
             type_descriptor_to_use,
-            validator,
+            validator=validator,
+            instruction_template=instruction_template,
             input_formatter=input_formatter,
         ),
     )
```

### Comparing `kor-0.6.1/kor/nodes.py` & `kor-0.7.0/kor/nodes.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,46 +1,36 @@
 """Definitions of input elements."""
 import abc
 import copy
-import inspect
-import operator
 import re
 from typing import (
     Any,
     Generic,
-    List,
     Mapping,
     Optional,
     Sequence,
     Tuple,
     TypeVar,
     Union,
 )
 
+from pydantic import BaseModel, validator
+
 # For now, limit what's allowed for identifiers.
 # The main constraints
 # 1) Relying on HTML parser to parse output
 # 2) One of the type descriptors is TypeScript, so we want
 #    to produce valid TypeScript identifiers.
 # We can lift the constraints later if it becomes important,
 # not worth the effort for a v0.
 VALID_IDENTIFIER_PATTERN = re.compile(r"^[a-z_][0-9a-z_]*$")
 
 T = TypeVar("T")
 
 
-def _get_all_slots(node: "AbstractSchemaNode") -> List[str]:
-    """Get a list of all slots."""
-    slots: List[str] = []
-    for class_ in inspect.getmro(type(node)):
-        if hasattr(class_, "__slots__"):
-            slots.extend(class_.__slots__)
-    return sorted(slots)
-
-
 # Visitor is defined here for now, to avoid circular imports.
 class AbstractVisitor(Generic[T], abc.ABC):
     """An abstract visitor."""
 
     def visit_text(self, node: "Text", **kwargs: Any) -> T:
         """Visit text node."""
         return self.visit_default(node, **kwargs)
@@ -62,39 +52,40 @@
         return self.visit_default(node, **kwargs)
 
     def visit_default(self, node: "AbstractSchemaNode", **kwargs: Any) -> T:
         """Default node implementation."""
         raise NotImplementedError()
 
 
-class AbstractSchemaNode(abc.ABC):
+class AbstractSchemaNode(BaseModel):
     """Abstract schema node.
 
     Each node is expected to have a unique ID, and should
     only use alphanumeric characters.
 
     The ID should be unique across all inputs that belong
     to a given form.
 
     The description should describe what the node represents.
     It is used during prompt generation.
     """
 
-    __slots__ = "id", "description", "many"
-
-    def __init__(self, *, id: str, description: str = "", many: bool = False) -> None:
-        self.id = id
-        self.description = description
-        self.many = many
-
-        if not VALID_IDENTIFIER_PATTERN.match(self.id):
+    id: str
+    description: str = ""
+    many: bool = False
+
+    @validator("id")
+    def ensure_valid_uid(cls, uid: str) -> str:
+        """Validate that using a valid identifier."""
+        if not VALID_IDENTIFIER_PATTERN.match(uid):
             raise ValueError(
-                f"`{self.id}` is not a valid identifier. "
-                "Please only use lower cased a-z, _ or the digits 0-9"
+                f"`{id}` is not a valid identifier. "
+                f"Please only use lower cased a-z, _ or the digits 0-9"
             )
+        return uid
 
     @abc.abstractmethod
     def accept(self, visitor: AbstractVisitor[T], **kwargs: Any) -> T:
         """Accept a visitor."""
         raise NotImplementedError()
 
     # Update return type to `Self` when bumping python version.
@@ -107,62 +98,34 @@
         new_object = copy.copy(self)
         if id:
             new_object.id = id
         if description:
             new_object.description = description
         return new_object
 
-    def __repr__(self) -> str:
-        """Get representation of the node."""
-        return f"{type(self).__name__}({self.id})"
-
-    def __eq__(self: Any, other: Any) -> bool:
-        """Equality check"""
-        if not isinstance(self, AbstractSchemaNode):
-            raise AssertionError(f"Cannot compare {type(self)} with {type(other)}")
-        if type(self) != type(other):
-            return False
-
-        if _get_all_slots(self) == _get_all_slots(other):
-            attr_getters = [operator.attrgetter(attr) for attr in self.__slots__]
-            return all(getter(self) == getter(other) for getter in attr_getters)
-
-        return False
-
 
 class ExtractionSchemaNode(AbstractSchemaNode, abc.ABC):
     """An abstract definition for inputs that involve extraction.
 
     An extraction input can be associated with extraction examples.
 
     An extraction example is a 2-tuple composed of a text segment and the expected
     extraction.
 
     For example:
 
     .. code-block:: python
+
         [
             ("I bought this cookie for $10", "$10"),
             ("Eggs cost twelve dollars", "twelve dollars"),
         ]
     """
 
-    __slots__ = ("examples",)
-
-    def __init__(
-        self,
-        *,
-        id: str,
-        description: str = "",
-        many: bool = False,
-        examples: Sequence[Tuple[str, Union[str, Sequence[str]]]] = tuple(),
-    ) -> None:
-        """Initialize for extraction input."""
-        super().__init__(id=id, description=description, many=many)
-        self.examples = examples
+    examples: Sequence[Tuple[str, Union[str, Sequence[str]]]] = tuple()
 
 
 class Number(ExtractionSchemaNode):
     """Built-in number input."""
 
     def accept(self, visitor: AbstractVisitor[T], **kwargs: Any) -> T:
         """Accept a visitor."""
@@ -176,31 +139,15 @@
         """Accept a visitor."""
         return visitor.visit_text(self, **kwargs)
 
 
 class Option(AbstractSchemaNode):
     """Built-in option input must be part of a selection input."""
 
-    __slots__ = ("examples",)
-
-    def __init__(
-        self,
-        *,
-        id: str,
-        description: str = "",
-        many: bool = False,
-        examples: Sequence[str] = tuple(),
-    ) -> None:
-        """Initialize for extraction input."""
-        if many:
-            # TODO: Fix the type hierarchy so that `many` isn't provided to option.
-            raise ValueError("Option inputs cannot be many.")
-
-        super().__init__(id=id, description=description, many=many)
-        self.examples = examples
+    examples: Sequence[str] = tuple()
 
     def accept(self, visitor: AbstractVisitor[T], **kwargs: Any) -> T:
         """Accept a visitor."""
         return visitor.visit_option(self, **kwargs)
 
 
 class Selection(AbstractSchemaNode):
@@ -232,34 +179,17 @@
             null_examples=[
                 "I like flowers",
             ],
             many=False
         )
     """
 
-    __slots__ = "options", "examples", "null_examples"
-
-    def __init__(
-        self,
-        *,
-        id: str,
-        description: str = "",
-        many: bool = False,
-        options: Sequence[Option],
-        examples: Sequence[Tuple[str, Union[str, Sequence[str]]]] = tuple(),
-        null_examples: Sequence[str] = tuple(),
-    ) -> None:
-        """Initialize for extraction input."""
-        super().__init__(id=id, description=description, many=many)
-
-        if not options:
-            raise ValueError("Selection inputs must have at least one option.")
-        self.options = options
-        self.examples = examples
-        self.null_examples = null_examples
+    options: Sequence[Option]
+    examples: Sequence[Tuple[str, Union[str, Sequence[str]]]] = tuple()
+    null_examples: Sequence[str] = tuple()
 
     def accept(self, visitor: AbstractVisitor[T], **kwargs: Any) -> T:
         """Accept a visitor."""
         return visitor.visit_selection(self, **kwargs)
 
 
 class Object(AbstractSchemaNode):
@@ -285,30 +215,22 @@
                     {"name": "Big Cookie", "price": "$10"}),
                 ("Eggs cost twelve dollars", {}), # Not a cookie
             ],
         )
 
     """
 
-    __slots__ = ("attributes", "examples")
+    attributes: Sequence[Union[ExtractionSchemaNode, Selection, "Object"]]
 
-    def __init__(
-        self,
-        *,
-        id: str,
-        description: str = "",
-        many: bool = False,
-        # All attributes but Option are OK.
-        # May could clean up the type system to simplify this.
-        attributes: Sequence[Union[ExtractionSchemaNode, Selection, "Object"]],
-        examples: Sequence[
-            Tuple[str, Mapping[str, Union[str, Sequence[str]]]]
-        ] = tuple(),
-    ) -> None:
-        """Initialize for extraction input."""
-        super().__init__(id=id, description=description, many=many)
-        self.attributes = attributes
-        self.examples = examples
+    examples: Sequence[
+        Tuple[
+            str,
+            Union[
+                Mapping[str, Any],
+                Sequence[Mapping[str, Any]],
+            ],
+        ]
+    ] = tuple()
 
     def accept(self, visitor: AbstractVisitor[T], **kwargs: Any) -> T:
         """Accept a visitor."""
         return visitor.visit_object(self, **kwargs)
```

### Comparing `kor-0.6.1/kor/prompts.py` & `kor-0.7.0/kor/prompts.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 """Code to dynamically generate appropriate LLM prompts."""
 from __future__ import annotations
 
 from typing import Any, List, Optional, Tuple
 
 from langchain import BasePromptTemplate
+from langchain.prompts import PromptTemplate
 from langchain.schema import (
     AIMessage,
     BaseMessage,
     HumanMessage,
     PromptValue,
     SystemMessage,
 )
@@ -18,140 +19,157 @@
 from kor.encoders.parser import KorParser
 from kor.examples import generate_examples
 from kor.nodes import Object
 from kor.type_descriptors import TypeDescriptor
 
 from .validators import Validator
 
+DEFAULT_INSTRUCTION_TEMPLATE = PromptTemplate(
+    input_variables=["type_description", "format_instructions"],
+    template=(
+        "Your goal is to extract structured information from the user's input that"
+        " matches the form described below. When extracting information please make"
+        " sure it matches the type information exactly. Do not add any attributes that"
+        " do not appear in the schema shown below.\n\n"
+        "{type_description}\n\n"
+        "{format_instructions}\n\n"
+    ),
+)
+
 
 class ExtractionPromptValue(PromptValue):
     """Integration with langchain prompt format."""
 
-    text: str
+    string: str
+    messages: List[BaseMessage]
+
+    class Config:
+        """Configuration for this pydantic object."""
+
+        extra = Extra.forbid
+        arbitrary_types_allowed = True
+
+    def to_string(self) -> str:
+        """Format the prompt to a string."""
+        return self.string
+
+    def to_messages(self) -> List[BaseMessage]:
+        """Get materialized messages."""
+        return self.messages
+
+
+class ExtractionPromptTemplate(BasePromptTemplate):
+    """Extraction prompt template."""
+
     encoder: Encoder
     node: Object
     type_descriptor: TypeDescriptor
     input_formatter: InputFormatter
-    prefix: str = (
-        "Your goal is to extract structured information from the user's input that"
-        " matches the form described below. When extracting information please make"
-        " sure it matches the type information exactly. Do not add any attributes that"
-        " do not appear in the schema shown below."
-    )
+    instruction_template: PromptTemplate
 
     class Config:
         """Configuration for this pydantic object."""
 
         extra = Extra.forbid
         arbitrary_types_allowed = True
 
-    def get_formatted_text(self) -> str:
-        """Get the text encoded if needed."""
-        return format_text(self.text, input_formatter=self.input_formatter)
+    def format_prompt(  # type: ignore[override]
+        self,
+        text: str,
+    ) -> PromptValue:
+        """Format the prompt."""
+        text = format_text(text, input_formatter=self.input_formatter)
+        return ExtractionPromptValue(
+            string=self.to_string(text), messages=self.to_messages(text)
+        )
 
-    def to_string(self) -> str:
+    def format(self, **kwargs: Any) -> str:
+        """Implementation of deprecated format method."""
+        raise NotImplementedError()
+
+    @property
+    def _prompt_type(self) -> str:
+        """Prompt type."""
+        return "ExtractionPromptTemplate"
+
+    def to_string(self, text: str) -> str:
         """Format the template to a string."""
-        instruction_segment = self.generate_instruction_segment(self.node)
+        instruction_segment = self.format_instruction_segment(self.node)
         encoded_examples = self.generate_encoded_examples(self.node)
         formatted_examples: List[str] = []
 
         for in_example, output in encoded_examples:
             formatted_examples.extend(
                 [
                     f"Input: {in_example}",
                     f"Output: {output}",
                 ]
             )
 
-        text = self.get_formatted_text()
         formatted_examples.append(f"Input: {text}\nOutput:")
         input_output_block = "\n".join(formatted_examples)
         return f"{instruction_segment}\n\n{input_output_block}"
 
-    def to_messages(self) -> List[BaseMessage]:
+    def to_messages(self, text: str) -> List[BaseMessage]:
         """Format the template to chat messages."""
-        instruction_segment = self.generate_instruction_segment(self.node)
+        instruction_segment = self.format_instruction_segment(self.node)
 
         messages: List[BaseMessage] = [SystemMessage(content=instruction_segment)]
         encoded_examples = self.generate_encoded_examples(self.node)
 
         for example_input, example_output in encoded_examples:
             messages.extend(
                 [
                     HumanMessage(content=example_input),
                     AIMessage(content=example_output),
                 ]
             )
 
-        content = self.get_formatted_text()
-        messages.append(HumanMessage(content=content))
+        messages.append(HumanMessage(content=text))
         return messages
 
     def generate_encoded_examples(self, node: Object) -> List[Tuple[str, str]]:
         """Generate encoded examples."""
         examples = generate_examples(node)
         return encode_examples(
             examples, self.encoder, input_formatter=self.input_formatter
         )
 
-    def generate_instruction_segment(self, node: Object) -> str:
+    def format_instruction_segment(self, node: Object) -> str:
         """Generate the instruction segment of the extraction."""
         type_description = self.type_descriptor.describe(node)
-        instruction_segment = self.encoder.get_instruction_segment()
-        return f"{self.prefix}\n\n{type_description}\n\n{instruction_segment}"
+        format_instructions = self.encoder.get_instruction_segment()
+        input_variables = self.instruction_template.input_variables
 
+        formatting_kwargs = {}
 
-class ExtractionPromptTemplate(BasePromptTemplate):
-    """Extraction prompt template."""
+        if "type_description" in input_variables:
+            formatting_kwargs["type_description"] = type_description
 
-    encoder: Encoder
-    node: Object
-    type_descriptor: TypeDescriptor
-    input_formatter: InputFormatter
+        if "format_instructions" in input_variables:
+            formatting_kwargs["format_instructions"] = format_instructions
 
-    class Config:
-        """Configuration for this pydantic object."""
-
-        extra = Extra.forbid
-        arbitrary_types_allowed = True
-
-    def format_prompt(  # type: ignore[override]
-        self, text: str, **kwargs: Any
-    ) -> PromptValue:
-        """Format the prompt."""
-        return ExtractionPromptValue(
-            text=text,
-            encoder=self.encoder,
-            node=self.node,
-            type_descriptor=self.type_descriptor,
-            input_formatter=self.input_formatter,
-        )
-
-    def format(self, **kwargs: Any) -> str:
-        """Implementation of deprecated format method."""
-        raise NotImplementedError()
-
-    @property
-    def _prompt_type(self) -> str:
-        """Prompt type."""
-        return "ExtractionPromptTemplate"
+        return self.instruction_template.format(**formatting_kwargs)
 
 
 # PUBLIC API
 
 
 def create_langchain_prompt(
     schema: Object,
     encoder: Encoder,
     type_descriptor: TypeDescriptor,
+    *,
     validator: Optional[Validator] = None,
     input_formatter: InputFormatter = None,
+    instruction_template: Optional[PromptTemplate] = None,
 ) -> ExtractionPromptTemplate:
     """Create a langchain style prompt with specified encoder."""
     return ExtractionPromptTemplate(
         input_variables=["text"],
         output_parser=KorParser(encoder=encoder, validator=validator, schema_=schema),
         encoder=encoder,
         node=schema,
         input_formatter=input_formatter,
         type_descriptor=type_descriptor,
+        instruction_template=instruction_template or DEFAULT_INSTRUCTION_TEMPLATE,
     )
```

### Comparing `kor-0.6.1/kor/type_descriptors.py` & `kor-0.7.0/kor/type_descriptors.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/kor/validators.py` & `kor-0.7.0/kor/validators.py`

 * *Files identical despite different names*

### Comparing `kor-0.6.1/pyproject.toml` & `kor-0.7.0/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "kor"
-version = "0.6.1"
+version = "0.7.0"
 description = "Extract information with LLMs from text"
 authors = ["Eugene Yurtsev <eyurtsev@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 repository = "https://www.github.com/eyurtsev/kor"
 
 [tool.poetry.dependencies]
```

### Comparing `kor-0.6.1/setup.py` & `kor-0.7.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 {'': ['*']}
 
 install_requires = \
 ['langchain>=0.0.110', 'openai>=0.27,<0.28', 'pandas>=1.5.3,<2.0.0']
 
 setup_kwargs = {
     'name': 'kor',
-    'version': '0.6.1',
+    'version': '0.7.0',
     'description': 'Extract information with LLMs from text',
     'long_description': '**⚠ WARNING: Prototype with unstable API. 🚧**  \n\n[![Unit Tests](https://github.com/eyurtsev/kor/actions/workflows/test.yml/badge.svg?branch=main&event=push)](https://github.com/eyurtsev/kor/actions/workflows/test.yml)\n[![Test Docs](https://github.com/eyurtsev/kor/actions/workflows/doc_test.yaml/badge.svg?branch=main&event=push)](https://github.com/eyurtsev/kor/actions/workflows/doc_test.yaml)\n\n# Kor\n\n\nThis is a half-baked prototype that "helps" you extract structured data from text using LLMs 🧩.\n\nSpecify the schema of what should be extracted and provide some examples.\n\nKor will generate a prompt, send it to the specified LLM and parse out the\noutput. \n\nYou might even get results back.\n\nSee [documentation](https://eyurtsev.github.io/kor/).\n\n## Version >=0.4.0\n\n* Integrated with langchain framework.\n* The code below uses Kor style schema, but you can also use [pydantic](https://eyurtsev.github.io/kor/validation.html).\n\n\n```python\n\n  from langchain.chat_models import ChatOpenAI\n  from kor import create_extraction_chain, Object, Text, Number\n\n  llm = ChatOpenAI(\n      model_name="gpt-3.5-turbo",\n      temperature=0,\n      max_tokens=2000,\n      frequency_penalty=0,\n      presence_penalty=0,\n      top_p=1.0,\n  )\n\n  schema = Object(\n    id="player",\n    description=(\n        "User is controling a music player to select songs, pause or start them or play"\n        " music by a particular artist."\n    ),\n    attributes=[\n        Text(\n            id="song",\n            description="User wants to play this song",\n            examples=[],\n            many=True,\n        ),\n        Text(\n            id="album",\n            description="User wants to play this album",\n            examples=[],\n            many=True,\n        ),\n        Text(\n            id="artist",\n            description="Music by the given artist",\n            examples=[("Songs by paul simon", "paul simon")],\n            many=True,\n        ),\n        Text(\n            id="action",\n            description="Action to take one of: `play`, `stop`, `next`, `previous`.",\n            examples=[\n                ("Please stop the music", "stop"),\n                ("play something", "play"),\n                ("play a song", "play"),\n                ("next song", "next"),\n            ],\n        ),\n    ],\n    many=False,\n)\n\n  chain = create_extraction_chain(llm, schema, encoder_or_encoder_class=\'json\')\n  chain.predict_and_parse(text="play songs by paul simon and led zeppelin and the doors")[\'data\']\n```\n\n```python\n  {\'player\': {\'artist\': [\'paul simon\', \'led zeppelin\', \'the doors\']}}\n```\n\n## Compatibility\n\n`Kor` is tested against python 3.8, 3.9, 3.10, 3.11.\n\n## Installaton \n\n```sh\npip install kor\n```\n\n## 💡 Ideas\n\nIdeas of some things that could be done with Kor.\n\n* Extract data from text that matches an extraction schema.\n* Power an AI assistant with skills by precisely understanding a user request.\n* Provide natural language access to an existing API.\n\n## 🚧 Prototype\n\nPrototype! So the API is not expected to be stable!\n\n##  ✨ What does Kor excel at?  🌟 \n\n* Making mistakes! Plenty of them!\n* Slow! It uses large prompts with examples, and works best with the larger slower LLMs.\n* Crashing for long enough pieces of text! Context length window could become\n  limiting when working with large forms or long text inputs.\n\nThe expectation is that as LLMs improve some of these issues will be mitigated.\n\n## Limtations\n\nNo limitations whatsoever. Do take a look at the section directly above as well\nas at the section about compatibility.\n\n## Potential Changes\n\n* Adding validators\n* Built-in components to quickly assemble schema with examples\n* Add routing layer to select appropriate extraction schema for a use case when\n  many schema exist\n\n## 🎶 Why the name?\n\nFast to type and sufficiently unique.\n\n## Contributing\n\nIf you have any ideas or feature requests, please open an issue and share!\n\nSee [CONTRIBUTING.md](https://github.com/eyurtsev/kor/blob/main/CONTRIBUTING.md) for more information.\n\n## Other packages\n\nProbabilistically speaking this package is unlikely to work for your use case.\n\nSo here are some great alternatives:\n\n* [Promptify](https://github.com/promptslab/Promptify)\n* [MiniChain](https://srush.github.io/MiniChain/examples/stats/)\n',
     'author': 'Eugene Yurtsev',
     'author_email': 'eyurtsev@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://www.github.com/eyurtsev/kor',
```

### Comparing `kor-0.6.1/PKG-INFO` & `kor-0.7.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kor
-Version: 0.6.1
+Version: 0.7.0
 Summary: Extract information with LLMs from text
 Home-page: https://www.github.com/eyurtsev/kor
 License: MIT
 Author: Eugene Yurtsev
 Author-email: eyurtsev@gmail.com
 Requires-Python: >=3.8.1,<4.0.0
 Classifier: License :: OSI Approved :: MIT License
```

