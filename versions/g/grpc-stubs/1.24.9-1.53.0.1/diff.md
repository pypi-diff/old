# Comparing `tmp/grpc-stubs-1.24.9.tar.gz` & `tmp/grpc-stubs-1.53.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "grpc-stubs-1.24.9.tar", last modified: Sun Apr 10 01:12:57 2022, max compression
+gzip compressed data, was "grpc-stubs-1.53.0.1.tar", last modified: Fri Apr  7 10:12:31 2023, max compression
```

## Comparing `grpc-stubs-1.24.9.tar` & `grpc-stubs-1.53.0.1.tar`

### file list

```diff
@@ -1,39 +1,41 @@
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.247257 grpc-stubs-1.24.9/
--rw-rw-r--   0 bl        (1000) bl        (1000)     1330 2022-04-10 01:12:57.247257 grpc-stubs-1.24.9/PKG-INFO
--rw-rw-r--   0 bl        (1000) bl        (1000)      595 2021-07-29 11:55:26.000000 grpc-stubs-1.24.9/README.rst
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.243257 grpc-stubs-1.24.9/grpc-stubs/
--rw-rw-r--   0 bl        (1000) bl        (1000)    23117 2022-04-10 01:11:06.000000 grpc-stubs-1.24.9/grpc-stubs/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc-stubs/py.typed
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.243257 grpc-stubs-1.24.9/grpc_channelz-stubs/
--rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_channelz-stubs/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_channelz-stubs/py.typed
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.243257 grpc-stubs-1.24.9/grpc_channelz-stubs/v1/
--rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_channelz-stubs/v1/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)     1330 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_channelz-stubs/v1/_servicer.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)       84 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_channelz-stubs/v1/channelz.pyi
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.243257 grpc-stubs-1.24.9/grpc_health-stubs/
--rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_health-stubs/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_health-stubs/py.typed
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.243257 grpc-stubs-1.24.9/grpc_health-stubs/v1/
--rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_health-stubs/v1/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)     1332 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_health-stubs/v1/health.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)     2101 2022-04-10 01:11:06.000000 grpc-stubs-1.24.9/grpc_health-stubs/v1/health_pb2.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)     1090 2022-04-10 01:11:06.000000 grpc-stubs-1.24.9/grpc_health-stubs/v1/health_pb2_grpc.pyi
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.243257 grpc-stubs-1.24.9/grpc_reflection-stubs/
--rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_reflection-stubs/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_reflection-stubs/py.typed
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.243257 grpc-stubs-1.24.9/grpc_reflection-stubs/v1alpha/
--rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_reflection-stubs/v1alpha/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)      633 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_reflection-stubs/v1alpha/reflection.pyi
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.247257 grpc-stubs-1.24.9/grpc_status-stubs/
--rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_status-stubs/__init__.pyi
--rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_status-stubs/py.typed
--rw-rw-r--   0 bl        (1000) bl        (1000)      455 2020-06-11 15:14:53.000000 grpc-stubs-1.24.9/grpc_status-stubs/rpc_status.pyi
-drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2022-04-10 01:12:57.247257 grpc-stubs-1.24.9/grpc_stubs.egg-info/
--rw-rw-r--   0 bl        (1000) bl        (1000)     1330 2022-04-10 01:12:57.000000 grpc-stubs-1.24.9/grpc_stubs.egg-info/PKG-INFO
--rw-rw-r--   0 bl        (1000) bl        (1000)      859 2022-04-10 01:12:57.000000 grpc-stubs-1.24.9/grpc_stubs.egg-info/SOURCES.txt
--rw-rw-r--   0 bl        (1000) bl        (1000)        1 2022-04-10 01:12:57.000000 grpc-stubs-1.24.9/grpc_stubs.egg-info/dependency_links.txt
--rw-rw-r--   0 bl        (1000) bl        (1000)       52 2022-04-10 01:12:57.000000 grpc-stubs-1.24.9/grpc_stubs.egg-info/requires.txt
--rw-rw-r--   0 bl        (1000) bl        (1000)       89 2022-04-10 01:12:57.000000 grpc-stubs-1.24.9/grpc_stubs.egg-info/top_level.txt
--rw-rw-r--   0 bl        (1000) bl        (1000)      194 2022-04-10 01:12:57.247257 grpc-stubs-1.24.9/setup.cfg
--rw-rw-r--   0 bl        (1000) bl        (1000)     1910 2022-04-10 01:12:20.000000 grpc-stubs-1.24.9/setup.py
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/
+-rw-rw-r--   0 bl        (1000) bl        (1000)     1080 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/LICENSE
+-rw-rw-r--   0 bl        (1000) bl        (1000)     3428 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/PKG-INFO
+-rw-rw-r--   0 bl        (1000) bl        (1000)     2872 2023-04-07 10:11:59.000000 grpc-stubs-1.53.0.1/README.md
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.657166 grpc-stubs-1.53.0.1/grpc-stubs/
+-rw-rw-r--   0 bl        (1000) bl        (1000)    24256 2023-04-07 10:11:11.000000 grpc-stubs-1.53.0.1/grpc-stubs/__init__.pyi
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.657166 grpc-stubs-1.53.0.1/grpc-stubs/aio/
+-rw-rw-r--   0 bl        (1000) bl        (1000)    16499 2023-04-07 10:11:11.000000 grpc-stubs-1.53.0.1/grpc-stubs/aio/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)        8 2023-04-07 10:11:11.000000 grpc-stubs-1.53.0.1/grpc-stubs/aio/py.typed
+-rw-rw-r--   0 bl        (1000) bl        (1000)        8 2023-03-05 04:14:41.000000 grpc-stubs-1.53.0.1/grpc-stubs/py.typed
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_channelz-stubs/
+-rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_channelz-stubs/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_channelz-stubs/py.typed
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_channelz-stubs/v1/
+-rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_channelz-stubs/v1/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)     1330 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_channelz-stubs/v1/_servicer.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)       84 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_channelz-stubs/v1/channelz.pyi
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_health-stubs/
+-rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_health-stubs/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_health-stubs/py.typed
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_health-stubs/v1/
+-rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_health-stubs/v1/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)     1332 2022-04-16 02:10:26.000000 grpc-stubs-1.53.0.1/grpc_health-stubs/v1/health.pyi
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_reflection-stubs/
+-rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_reflection-stubs/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_reflection-stubs/py.typed
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_reflection-stubs/v1alpha/
+-rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_reflection-stubs/v1alpha/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)      628 2023-01-14 22:59:05.000000 grpc-stubs-1.53.0.1/grpc_reflection-stubs/v1alpha/reflection.pyi
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_status-stubs/
+-rw-rw-r--   0 bl        (1000) bl        (1000)       56 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_status-stubs/__init__.pyi
+-rw-rw-r--   0 bl        (1000) bl        (1000)        0 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_status-stubs/py.typed
+-rw-rw-r--   0 bl        (1000) bl        (1000)      455 2020-06-11 15:14:53.000000 grpc-stubs-1.53.0.1/grpc_status-stubs/rpc_status.pyi
+drwxrwxr-x   0 bl        (1000) bl        (1000)        0 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/grpc_stubs.egg-info/
+-rw-rw-r--   0 bl        (1000) bl        (1000)     3428 2023-04-07 10:12:31.000000 grpc-stubs-1.53.0.1/grpc_stubs.egg-info/PKG-INFO
+-rw-rw-r--   0 bl        (1000) bl        (1000)      841 2023-04-07 10:12:31.000000 grpc-stubs-1.53.0.1/grpc_stubs.egg-info/SOURCES.txt
+-rw-rw-r--   0 bl        (1000) bl        (1000)        1 2023-04-07 10:12:31.000000 grpc-stubs-1.53.0.1/grpc_stubs.egg-info/dependency_links.txt
+-rw-rw-r--   0 bl        (1000) bl        (1000)        7 2023-04-07 10:12:31.000000 grpc-stubs-1.53.0.1/grpc_stubs.egg-info/requires.txt
+-rw-rw-r--   0 bl        (1000) bl        (1000)       89 2023-04-07 10:12:31.000000 grpc-stubs-1.53.0.1/grpc_stubs.egg-info/top_level.txt
+-rw-rw-r--   0 bl        (1000) bl        (1000)      194 2023-04-07 10:12:31.661166 grpc-stubs-1.53.0.1/setup.cfg
+-rw-rw-r--   0 bl        (1000) bl        (1000)     1864 2023-04-07 10:12:12.000000 grpc-stubs-1.53.0.1/setup.py
```

### Comparing `grpc-stubs-1.24.9/grpc-stubs/__init__.pyi` & `grpc-stubs-1.53.0.1/grpc-stubs/__init__.pyi`

 * *Files 3% similar despite different names*

```diff
@@ -1,21 +1,24 @@
 import enum
 import threading
 import typing
-import sys
 from concurrent import futures
-from types import TracebackType
-if sys.version_info[:2] >= (3, 8):
-    from typing import Literal
-else:
-    # Python 3.7 and earlier
-    from typing_extensions import Literal
+from types import ModuleType, TracebackType
 
 __version__: str
 
+# This class encodes an uninhabited type, requiring use of explicit casts or ignores
+# in order to satisfy type checkers. This allows grpc-stubs to add proper stubs
+# later, allowing those overrides to be removed.
+# The alternative is typing.Any, but a future replacement of Any with a proper type
+# would result in type errors where previously the type checker was happy, which
+# we want to avoid. Forcing the user to use overrides provides forwards-compatibility.
+class _PartialStubMustCastOrIgnore:
+    pass
+
 
 # XXX: Early attempts to tame this used literals for all the keys (gRPC is
 # a bit segfaulty and doesn't adequately validate the option keys), but that
 # didn't quite work out. Maybe it's something we can come back to?
 _OptionKeyValue = typing.Tuple[str, typing.Any]
 _Options = typing.Sequence[_OptionKeyValue]
 
@@ -78,49 +81,46 @@
 def ssl_channel_credentials(
     root_certificates: typing.Optional[bytes] = None,
     private_key: typing.Optional[bytes] = None,
     certificate_chain: typing.Optional[bytes] = None,
 ) -> ChannelCredentials:
     ...
 
-
 def local_channel_credentials(
     local_connect_type: LocalConnectionType = LocalConnectionType.LOCAL_TCP,
 ) -> ChannelCredentials:
     ...
 
-
 def metadata_call_credentials(
     metadata_plugin: AuthMetadataPlugin,
     name: typing.Optional[str] = None,
 ) -> CallCredentials:
     ...
 
-
 def access_token_call_credentials(access_token: str) -> CallCredentials:
     ...
 
 def alts_channel_credentials(
-    service_accounts: typing.Sequence[str] = None,
+    service_accounts: typing.Optional[typing.Sequence[str]] = None,
 ) -> ChannelCredentials: ...
+
 def compute_engine_channel_credentials() -> ChannelCredentials: ...
+
 def xds_channel_credentials(
-    fallback_credentials: ChannelCredentials = None,
+    fallback_credentials: typing.Optional[ChannelCredentials] = None,
 ) -> ChannelCredentials: ...
 
 # GRPC docs say there should be at least two:
 def composite_call_credentials(
     creds1: CallCredentials,
     creds2: CallCredentials,
     *rest: CallCredentials,
 ) -> CallCredentials:
     ...
 
-
-
 # Compose a ChannelCredentials and one or more CallCredentials objects.
 def composite_channel_credentials(
     channel_credentials: ChannelCredentials,
     call_credentials: CallCredentials,
     *rest: CallCredentials,
 ) -> ChannelCredentials:
     ...
@@ -131,14 +131,15 @@
 def server(
     thread_pool: futures.ThreadPoolExecutor,
     handlers: typing.Optional[typing.List[GenericRpcHandler]] = None,
     interceptors: typing.Optional[typing.List[ServerInterceptor]] = None,
     options: typing.Optional[_Options] = None,
     maximum_concurrent_rpcs: typing.Optional[int] = None,
     compression: typing.Optional[Compression] = None,
+    xds: bool = False,
 ) -> Server:
     ...
 
 
 """Create Server Credentials"""
 
 CertificateChainPair = typing.Tuple[bytes, bytes]
@@ -168,15 +169,17 @@
     initial_certificate_configuration: ServerCertificateConfiguration,
     certificate_configuration_fetcher: typing.Callable[[], ServerCertificateConfiguration],
     require_client_authentication: bool = False,
 ) -> ServerCredentials:
     ...
 
 def alts_server_credentials() -> ServerCredentials: ...
+
 def insecure_server_credentials() -> ServerCredentials: ...
+
 def xds_server_credentials(
     fallback_credentials: ServerCredentials,
 ) -> ServerCredentials: ...
 
 """RPC Method Handlers"""
 
 # XXX: This is probably what appears in the add_FooServicer_to_server function
@@ -253,31 +256,33 @@
 
     # XXX: misnamed property, does not align with status.proto, where it is called 'message':
     details: str
 
     trailing_metadata: Metadata
 
 
+# https://grpc.github.io/grpc/core/md_doc_statuscodes.html
 class StatusCode(enum.Enum):
     OK = ...
     CANCELLED = ...
     UNKNOWN = ...
     INVALID_ARGUMENT = ...
     DEADLINE_EXCEEDED = ...
     NOT_FOUND = ...
     ALREADY_EXISTS = ...
     PERMISSION_DENIED = ...
-    UNAUTHENTICATED = ...
     RESOURCE_EXHAUSTED = ...
     FAILED_PRECONDITION = ...
     ABORTED = ...
+    OUT_OF_RANGE = ...
     UNIMPLEMENTED = ...
     INTERNAL = ...
     UNAVAILABLE = ...
     DATA_LOSS = ...
+    UNAUTHENTICATED = ...
 
 
 """Channel Object"""
 
 # XXX: These are probably the SerializeToTring/FromString pb2 methods, but
 # this needs further investigation
 RequestSerializer = typing.Callable
@@ -409,19 +414,22 @@
 """gRPC Exceptions"""
 
 class _Metadatum:
     key: str
     value: bytes
 
 
+# FIXME: There is scant documentation about what is actually available in this type.
+# The properties here are the properties observed in the wild, and may be inaccurate.
+# A better source to confirm their presence needs to be found at some point.
 class RpcError(Exception):
     def code(self) -> StatusCode: ...
 
     # misnamed property, does not align with status.proto, where it is called 'message':
-    def details(self) -> str: ...
+    def details(self) -> typing.Optional[str]: ...
 
     # XXX: This has a slightly different return type to all the other metadata:
     def trailing_metadata(self) -> typing.Tuple[_Metadatum, ...]: ...
 
 
 """Shared Context"""
 
@@ -462,15 +470,15 @@
 TResponse = typing.TypeVar("TResponse")
 
 # An object that is both a Call for the RPC and a Future. In the event of
 # RPC completion, the return Call-Future’s result value will be the
 # response message of the RPC. Should the event terminate with non-OK
 # status, the returned Call-Future’s exception value will be an RpcError.
 #
-class CallFuture(typing.Generic[TResponse], Call, Future[TResponse]):
+class CallFuture(Call, Future[TResponse], typing.Generic[TResponse]):
     pass
 
 
 class UnaryUnaryClientInterceptor(typing.Generic[TRequest, TResponse]):
     def intercept_unary_unary(
         self,
 
@@ -557,14 +565,16 @@
     def set_code(self, code: StatusCode) -> None: ...
     def set_compression(self, compression: Compression) -> None: ...
     def set_trailing_metadata(self, trailing_metadata: Metadata) -> None: ...
 
     # misnamed function 'details', does not align with status.proto, where it is called 'message':
     def set_details(self, details: str) -> None: ...
 
+    def trailing_metadata(self) -> Metadata: ...
+
 
 """Service-Side Handler"""
 
 class RpcMethodHandler(typing.Generic[TRequest, TResponse]):
     request_streaming: bool
     response_streaming: bool
 
@@ -588,15 +598,15 @@
     invocation_metadata: Metadata
 
 
 class GenericRpcHandler(typing.Generic[TRequest, TResponse]):
     def service(self, handler_call_details: HandlerCallDetails) -> typing.Optional[RpcMethodHandler[TRequest, TResponse]]:
         ...
 
-class ServiceRpcHandler:
+class ServiceRpcHandler(GenericRpcHandler[TRequest, TResponse], typing.Generic[TRequest, TResponse]):
     def service_name(self) -> str: ...
 
 
 """Service-Side Interceptor"""
 
 class ServerInterceptor(typing.Generic[TRequest, TResponse]):
     def intercept_service(
@@ -763,7 +773,19 @@
     def exception(self) -> typing.Optional[Exception]: ...
     def result(self, timeout: typing.Optional[float] = None) -> TFutureValue: ...
     def running(self) -> bool: ...
 
     # FIXME: unsure of the exact return type here. Is it a traceback.StackSummary?
     def traceback(self, timeout: typing.Optional[float] = None) -> typing.Any: ...
 
+
+"""Runtime Protobuf Parsing"""
+
+def protos(protobuf_path: str) -> ModuleType:
+    ...
+
+def services(protobuf_path: str) -> ModuleType:
+    ...
+
+def protos_and_services(protobuf_path: str) -> typing.Tuple[ModuleType, ModuleType]:
+    ...
+
```

### Comparing `grpc-stubs-1.24.9/grpc_channelz-stubs/v1/_servicer.pyi` & `grpc-stubs-1.53.0.1/grpc_channelz-stubs/v1/_servicer.pyi`

 * *Files identical despite different names*

### Comparing `grpc-stubs-1.24.9/grpc_health-stubs/v1/health.pyi` & `grpc-stubs-1.53.0.1/grpc_health-stubs/v1/health.pyi`

 * *Files identical despite different names*

### Comparing `grpc-stubs-1.24.9/grpc_reflection-stubs/v1alpha/reflection.pyi` & `grpc-stubs-1.53.0.1/grpc_reflection-stubs/v1alpha/reflection.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -6,9 +6,9 @@
 
 SERVICE_NAME: str
 
 class ReflectionServicer(BaseReflectionServicer):
     def ServerReflectionInfo(self, request_iterator: Iterable[_reflection_pb2.ServerReflectionRequest], context: ServicerContext) -> None:
         ...
 
-def enable_server_reflection(service_names: List[str], server: grpc.Server, pool: Optional[descriptor_pool.DescriptorPool] = ...) -> None:
+def enable_server_reflection(service_names: List[str], server: Server, pool: Optional[descriptor_pool.DescriptorPool] = ...) -> None:
     ...
```

### Comparing `grpc-stubs-1.24.9/grpc_stubs.egg-info/SOURCES.txt` & `grpc-stubs-1.53.0.1/grpc_stubs.egg-info/SOURCES.txt`

 * *Files 9% similar despite different names*

```diff
@@ -1,23 +1,24 @@
-README.rst
+LICENSE
+README.md
 setup.cfg
 setup.py
 grpc-stubs/__init__.pyi
 grpc-stubs/py.typed
+grpc-stubs/aio/__init__.pyi
+grpc-stubs/aio/py.typed
 grpc_channelz-stubs/__init__.pyi
 grpc_channelz-stubs/py.typed
 grpc_channelz-stubs/v1/__init__.pyi
 grpc_channelz-stubs/v1/_servicer.pyi
 grpc_channelz-stubs/v1/channelz.pyi
 grpc_health-stubs/__init__.pyi
 grpc_health-stubs/py.typed
 grpc_health-stubs/v1/__init__.pyi
 grpc_health-stubs/v1/health.pyi
-grpc_health-stubs/v1/health_pb2.pyi
-grpc_health-stubs/v1/health_pb2_grpc.pyi
 grpc_reflection-stubs/__init__.pyi
 grpc_reflection-stubs/py.typed
 grpc_reflection-stubs/v1alpha/__init__.pyi
 grpc_reflection-stubs/v1alpha/reflection.pyi
 grpc_status-stubs/__init__.pyi
 grpc_status-stubs/py.typed
 grpc_status-stubs/rpc_status.pyi
```

### Comparing `grpc-stubs-1.24.9/setup.py` & `grpc-stubs-1.53.0.1/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 import os
 from typing import List
 
 from setuptools import find_packages
 from distutils.core import setup
 
-__version__ = "1.24.9"
+__version__ = "1.53.0.1"
 
 dependencies = [
-    "typing-extensions; python_version<'3.8'",
     'grpcio',
 ]
 
 
 def find_stub_files(name: str) -> List[str]:
     result = []
     for root, dirs, files in os.walk(name):
@@ -20,15 +19,15 @@
                 if os.path.sep in root:
                     sub_root = root.split(os.path.sep, 1)[-1]
                     file = os.path.join(sub_root, file)
                 result.append(file)
     return result
 
 
-with open('README.rst', 'r') as f:
+with open('README.md', 'r') as f:
     readme = f.read()
 
 package_data = {
     'grpc-stubs': find_stub_files('grpc-stubs'),
     'grpc_channelz-stubs': find_stub_files('grpc_channelz-stubs'),
     'grpc_health-stubs': find_stub_files('grpc_health-stubs'),
     'grpc_reflection-stubs': find_stub_files('grpc_reflection-stubs'),
```

