# Comparing `tmp/wg_utilities-2.9.0.tar.gz` & `tmp/wg_utilities-3.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wg_utilities-2.9.0.tar", last modified: Wed Feb  2 20:42:44 2022, max compression
+gzip compressed data, was "wg_utilities-3.0.0.tar", max compression
```

## Comparing `wg_utilities-2.9.0.tar` & `wg_utilities-3.0.0.tar`

### file list

```diff
@@ -1,32 +1,39 @@
-drwxr-xr-x   0 will       (502) staff       (20)        0 2022-02-02 20:42:44.245964 wg_utilities-2.9.0/
--rw-r--r--   0 will       (502) staff       (20)      580 2022-02-02 20:42:44.245025 wg_utilities-2.9.0/PKG-INFO
--rw-r--r--   0 will       (502) staff       (20)      126 2021-12-23 16:07:15.000000 wg_utilities-2.9.0/README.md
--rw-r--r--   0 will       (502) staff       (20)      274 2021-12-21 14:30:49.000000 wg_utilities-2.9.0/pyproject.toml
--rw-r--r--   0 will       (502) staff       (20)       38 2022-02-02 20:42:44.246166 wg_utilities-2.9.0/setup.cfg
--rw-r--r--   0 will       (502) staff       (20)     1376 2022-02-02 20:42:41.000000 wg_utilities-2.9.0/setup.py
-drwxr-xr-x   0 will       (502) staff       (20)        0 2022-02-02 20:42:44.215263 wg_utilities-2.9.0/wg_utilities/
--rw-r--r--   0 will       (502) staff       (20)       78 2022-01-19 00:56:07.000000 wg_utilities-2.9.0/wg_utilities/__init__.py
-drwxr-xr-x   0 will       (502) staff       (20)        0 2022-02-02 20:42:44.233495 wg_utilities-2.9.0/wg_utilities/clients/
--rw-r--r--   0 will       (502) staff       (20)      196 2022-01-31 17:53:34.000000 wg_utilities-2.9.0/wg_utilities/clients/__init__.py
--rw-r--r--   0 will       (502) staff       (20)    12045 2022-01-31 17:53:34.000000 wg_utilities-2.9.0/wg_utilities/clients/_generic_oauth.py
--rw-r--r--   0 will       (502) staff       (20)    16297 2022-02-02 20:42:40.000000 wg_utilities-2.9.0/wg_utilities/clients/google.py
--rw-r--r--   0 will       (502) staff       (20)    13472 2022-01-31 17:25:59.000000 wg_utilities-2.9.0/wg_utilities/clients/monzo.py
--rw-r--r--   0 will       (502) staff       (20)    20238 2022-01-31 17:25:59.000000 wg_utilities-2.9.0/wg_utilities/clients/spotify.py
--rw-r--r--   0 will       (502) staff       (20)    29654 2022-01-31 17:25:59.000000 wg_utilities-2.9.0/wg_utilities/clients/truelayer.py
-drwxr-xr-x   0 will       (502) staff       (20)        0 2022-02-02 20:42:44.237788 wg_utilities-2.9.0/wg_utilities/epd/
--rw-r--r--   0 will       (502) staff       (20)     1020 2021-12-23 21:49:29.000000 wg_utilities-2.9.0/wg_utilities/epd/__init__.py
--rw-r--r--   0 will       (502) staff       (20)     5992 2021-12-23 21:49:29.000000 wg_utilities-2.9.0/wg_utilities/epd/epd7in5_v2.py
--rw-r--r--   0 will       (502) staff       (20)     5579 2022-01-23 17:52:40.000000 wg_utilities-2.9.0/wg_utilities/epd/epdconfig.py
-drwxr-xr-x   0 will       (502) staff       (20)        0 2022-02-02 20:42:44.242964 wg_utilities-2.9.0/wg_utilities/functions/
--rw-r--r--   0 will       (502) staff       (20)      159 2022-01-31 17:25:59.000000 wg_utilities-2.9.0/wg_utilities/functions/__init__.py
--rw-r--r--   0 will       (502) staff       (20)     1807 2022-01-31 17:25:59.000000 wg_utilities-2.9.0/wg_utilities/functions/file_management.py
--rw-r--r--   0 will       (502) staff       (20)     1232 2022-01-31 17:25:59.000000 wg_utilities-2.9.0/wg_utilities/functions/processes.py
--rw-r--r--   0 will       (502) staff       (20)      302 2022-01-31 17:25:59.000000 wg_utilities-2.9.0/wg_utilities/functions/string_manipulation.py
-drwxr-xr-x   0 will       (502) staff       (20)        0 2022-02-02 20:42:44.244033 wg_utilities-2.9.0/wg_utilities/loggers/
--rw-r--r--   0 will       (502) staff       (20)     1618 2021-12-23 21:49:29.000000 wg_utilities-2.9.0/wg_utilities/loggers/__init__.py
-drwxr-xr-x   0 will       (502) staff       (20)        0 2022-02-02 20:42:44.227673 wg_utilities-2.9.0/wg_utilities.egg-info/
--rw-r--r--   0 will       (502) staff       (20)      580 2022-02-02 20:42:43.000000 wg_utilities-2.9.0/wg_utilities.egg-info/PKG-INFO
--rw-r--r--   0 will       (502) staff       (20)      718 2022-02-02 20:42:43.000000 wg_utilities-2.9.0/wg_utilities.egg-info/SOURCES.txt
--rw-r--r--   0 will       (502) staff       (20)        1 2022-02-02 20:42:43.000000 wg_utilities-2.9.0/wg_utilities.egg-info/dependency_links.txt
--rw-r--r--   0 will       (502) staff       (20)      143 2022-02-02 20:42:43.000000 wg_utilities-2.9.0/wg_utilities.egg-info/requires.txt
--rw-r--r--   0 will       (502) staff       (20)       13 2022-02-02 20:42:43.000000 wg_utilities-2.9.0/wg_utilities.egg-info/top_level.txt
+-rw-r--r--   0        0        0     1069 2023-04-07 12:01:25.717285 wg_utilities-3.0.0/LICENSE
+-rw-r--r--   0        0        0     1024 2023-04-07 12:01:25.717285 wg_utilities-3.0.0/README.md
+-rw-r--r--   0        0        0     4807 2023-04-07 12:01:25.721284 wg_utilities-3.0.0/pyproject.toml
+-rw-r--r--   0        0        0      280 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/__init__.py
+-rw-r--r--   0        0        0      140 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/api/__init__.py
+-rw-r--r--   0        0        0     7384 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/api/temp_auth_server.py
+-rw-r--r--   0        0        0      560 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/__init__.py
+-rw-r--r--   0        0        0     4962 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/_google.py
+-rw-r--r--   0        0        0    10359 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/_spotify_types.py
+-rw-r--r--   0        0        0    24659 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/google_calendar.py
+-rw-r--r--   0        0        0    56685 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/google_drive.py
+-rw-r--r--   0        0        0     7142 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/google_fit.py
+-rw-r--r--   0        0        0    14065 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/google_photos.py
+-rw-r--r--   0        0        0    16193 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/monzo.py
+-rw-r--r--   0        0        0    24945 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/oauth_client.py
+-rw-r--r--   0        0        0    49741 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/spotify.py
+-rw-r--r--   0        0        0    21403 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/clients/truelayer.py
+-rw-r--r--   0        0        0      126 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/__init__.py
+-rw-r--r--   0        0        0      119 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/dht22/__init__.py
+-rwxr-xr-x   0        0        0     6589 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/dht22/dht22_lib.py
+-rw-r--r--   0        0        0     1129 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/epd/__init__.py
+-rw-r--r--   0        0        0     7042 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/epd/epd7in5_v2.py
+-rw-r--r--   0        0        0     5993 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/epd/epdconfig.py
+-rw-r--r--   0        0        0      138 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/yamaha_yas_209/__init__.py
+-rw-r--r--   0        0        0    35904 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/devices/yamaha_yas_209/yamaha_yas_209.py
+-rw-r--r--   0        0        0     5401 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/exceptions/__init__.py
+-rw-r--r--   0        0        0      803 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/__init__.py
+-rw-r--r--   0        0        0     4595 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/_functions.py
+-rw-r--r--   0        0        0     1287 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/datetime_helpers.py
+-rw-r--r--   0        0        0     2024 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/file_management.py
+-rw-r--r--   0        0        0     8851 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/json.py
+-rw-r--r--   0        0        0     1386 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/processes.py
+-rw-r--r--   0        0        0     1106 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/string_manipulation.py
+-rw-r--r--   0        0        0     1586 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/functions/xml.py
+-rw-r--r--   0        0        0     7258 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/loggers/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/py.typed
+-rw-r--r--   0        0        0      167 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/testing/__init__.py
+-rw-r--r--   0        0        0     5257 2023-04-07 12:01:25.789286 wg_utilities-3.0.0/wg_utilities/testing/_custom_mocks.py
+-rw-r--r--   0        0        0     2840 1970-01-01 00:00:00.000000 wg_utilities-3.0.0/PKG-INFO
```

### Comparing `wg_utilities-2.9.0/wg_utilities/clients/truelayer.py` & `wg_utilities-3.0.0/wg_utilities/devices/yamaha_yas_209/yamaha_yas_209.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,959 +1,1136 @@
-"""Custom client for interacting with TrueLayer's API"""
+"""Classes etc. for subscribing to YAS-209 updates."""
+from __future__ import annotations
+
+from asyncio import new_event_loop, run
+from asyncio import sleep as async_sleep
+from collections.abc import Callable, Coroutine, Mapping, Sequence
 from datetime import datetime, timedelta
 from enum import Enum
-from json import load, dump, dumps
-from logging import getLogger, DEBUG
-from os import getenv
-from time import time
-from webbrowser import open as open_browser
-
-from jwt import decode, DecodeError
-from requests import post, get, HTTPError
+from functools import wraps
+from logging import DEBUG, getLogger
+from textwrap import dedent
+from threading import Thread
+from time import sleep, strptime
+from typing import Any, Literal, TypedDict, TypeVar
+
+from async_upnp_client.aiohttp import AiohttpNotifyServer, AiohttpRequester
+from async_upnp_client.client import UpnpDevice, UpnpService, UpnpStateVariable
+from async_upnp_client.client_factory import UpnpFactory
+from async_upnp_client.exceptions import UpnpCommunicationError
+from async_upnp_client.utils import get_local_ip
+from pydantic import BaseModel, Extra, Field, ValidationError
+from pydantic.error_wrappers import ErrorWrapper
+from xmltodict import parse as parse_xml
 
-from wg_utilities.functions import user_data_dir, force_mkdir
+from wg_utilities.functions import traverse_dict
 from wg_utilities.loggers import add_stream_handler
 
 LOGGER = getLogger(__name__)
 LOGGER.setLevel(DEBUG)
 add_stream_handler(LOGGER)
 
-DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
-
 
-class Bank(Enum):
-    """Enum for all banks supported by TrueLayer"""
+# pylint: disable=too-few-public-methods
+class StateVariable(BaseModel, extra=Extra.allow):
+    """BaseModel for state variables in DLNA payload."""
+
+    channel: str
+    val: str
+
+
+# pylint: disable=too-few-public-methods
+class CurrentTrackMetaDataItemRes(BaseModel, extra=Extra.allow):
+    """BaseModel for part of the DLNA payload."""
+
+    protocolInfo: str  # noqa: N815
+    duration: str
+    text: str | None
+
+
+# pylint: disable=too-few-public-methods
+class TrackMetaDataItem(BaseModel, extra=Extra.allow):
+    """BaseModel for part of the DLNA payload."""
+
+    id: str
+    song_subid: str | None = Field("", alias="song:subid")
+    song_description: str | None = Field("", alias="song:description")
+    song_skiplimit: str = Field("", alias="song:skiplimit")
+    song_id: str | None = Field("", alias="song:id")
+    song_like: str = Field("", alias="song:like")
+    song_singerid: str = Field("", alias="song:singerid")
+    song_albumid: str = Field("", alias="song:albumid")
+    res: CurrentTrackMetaDataItemRes
+    dc_title: str | None = Field(..., alias="dc:title")
+    dc_creator: str | None = Field("", alias="dc:creator")
+    upnp_artist: str | None = Field(..., alias="upnp:artist")
+    upnp_album: str | None = Field(..., alias="upnp:album")
+    upnp_albumArtURI: str = Field(..., alias="upnp:albumArtURI")  # noqa: N815
+
+
+# pylint: disable=too-few-public-methods
+class TrackMetaData(BaseModel, extra=Extra.allow):
+    """BaseModel for part of the DLNA payload."""
+
+    item: TrackMetaDataItem
+
+
+class InstanceIDAVTransport(BaseModel, extra=Extra.allow):
+    """BaseModel for part of the DLNA payload."""
+
+    val: str
+    TransportState: str
+    TransportStatus: str | None
+    NumberOfTracks: str | None
+    CurrentTrack: str | None
+    CurrentTrackDuration: str | None
+    CurrentMediaDuration: str | None
+    CurrentTrackURI: str | None
+    AVTransportURI: str | None
+    TrackSource: str | None
+    CurrentTrackMetaData: TrackMetaData | None
+    AVTransportURIMetaData: TrackMetaData | None
+    PlaybackStorageMedium: str | None
+    PossiblePlaybackStorageMedia: str | None
+    PossibleRecordStorageMedia: str | None
+    RecordStorageMedium: str | None
+    CurrentPlayMode: str | None
+    TransportPlaySpeed: str | None
+    RecordMediumWriteStatus: str | None
+    CurrentRecordQualityMode: str | None
+    PossibleRecordQualityModes: str | None
+    RelativeTimePosition: str | None
+    AbsoluteTimePosition: str | None
+    RelativeCounterPosition: str | None
+    AbsoluteCounterPosition: str | None
+    CurrentTransportActions: str | None
+
+
+class InstanceIDRenderingControl(BaseModel, extra=Extra.allow):
+    """BaseModel for part of the DLNA payload."""
+
+    val: str
+    Mute: StateVariable
+    Channel: StateVariable | None
+    Equalizer: StateVariable | None
+    # There's a typo in the schema, this is correct for some payloads -.-
+    Equaluzer: StateVariable | None
+    Volume: StateVariable
+    PresetNameList: str | None
+    TimeStamp: str | None
+
+
+class EventAVTransport(BaseModel, extra=Extra.allow):
+    """BaseModel for part of the DLNA payload."""
+
+    xmlns: Literal["urn:schemas-upnp-org:metadata-1-0/AVT/"]
+    InstanceID: InstanceIDAVTransport
+
+
+class EventRenderingControl(BaseModel, extra=Extra.allow):
+    """BaseModel for part of the DLNA payload."""
+
+    xmlns: Literal["urn:schemas-upnp-org:metadata-1-0/RCS/"]
+    InstanceID: InstanceIDRenderingControl
+
+
+class LastChange(BaseModel, extra=Extra.allow):
+    """BaseModel for the DLNA payload."""
+
+    Event: Any
+
+    @classmethod
+    def parse(cls, payload: dict[Literal["Event"], object]) -> LastChange:
+        """Parse a `LastChange` model from the payload dictionary.
 
-    ALLIED_IRISH_BANK_CORPORATE = "Allied Irish Bank Corporate"
-    AMEX = "Amex"
-    BANK_OF_SCOTLAND = "Bank of Scotland"
-    BANK_OF_SCOTLAND_BUSINESS = "Bank of Scotland Business"
-    BARCLAYCARD = "Barclaycard"
-    BARCLAYS = "Barclays"
-    BARCLAYS_BUSINESS = "Barclays Business"
-    CAPITAL_ONE = "Capital One"
-    CHELSEA_BUILDING_SOCIETY = "Chelsea Building Society"
-    DANSKE_BANK = "Danske Bank"
-    DANSKE_BANK_BUSINESS = "Danske Bank Business"
-    FIRST_DIRECT = "First Direct"
-    HALIFAX = "Halifax"
-    HSBC = "HSBC"
-    HSBC_BUSINESS = "HSBC Business"
-    LLOYDS = "Lloyds"
-    LLOYDS_BUSINESS = "Lloyds Business"
-    LLOYDS_COMMERCIAL = "Lloyds Commercial"
-    M_S_BANK = "M&S Bank"
-    MBNA = "MBNA"
-    MONZO = "Monzo"
-    NATIONWIDE = "Nationwide"
-    NATWEST = "NatWest"
-    NATWEST_BUSINESS = "NatWest Business"
-    REVOLUT = "Revolut"
-    ROYAL_BANK_OF_SCOTLAND = "Royal Bank of Scotland"
-    ROYAL_BANK_OF_SCOTLAND_BUSINESS = "Royal Bank of Scotland Business"
-    SANTANDER = "Santander"
-    STARLING = "Starling"
-    TESCO_BANK = "Tesco Bank"
-    TIDE = "Tide"
-    TSB = "TSB"
-    ULSTER_BANK = "Ulster Bank"
-    ULSTER_BUSINESS = "Ulster Business"
-    VIRGIN_MONEY = "Virgin Money"
-    WISE = "Wise"
-    YORKSHIRE_BUILDING_SOCIETY = "Yorkshire Building Society"
-
-
-class TransactionCategory(Enum):
-    """Enum for TrueLayer transaction types, including an overridden __init__
-    method for setting a description as well as the main value"""
-
-    ATM = (
-        "ATM",
-        "Deposit or withdrawal of funds using an ATM (Automated Teller Machine)",
-    )
-    BILL_PAYMENT = "Bill Payment", "Payment of a bill"
-    CASH = (
-        "Cash",
-        "Cash deposited over the branch counter or using Cash and Deposit Machines",
-    )
-    CASHBACK = (
-        "Cashback",
-        "An option retailers offer to withdraw cash while making a debit card purchase",
-    )
-    CHEQUE = (
-        "Cheque",
-        "A document ordering the payment of money from a bank account to another person"
-        " or organisation",
-    )
-    CORRECTION = "Correction", "Correction of a transaction error"
-    CREDIT = "Credit", "Funds added to your account"
-    DIRECT_DEBIT = (
-        "Direct Debit",
-        "An automatic withdrawal of funds initiated by a third party at regular"
-        " intervals",
-    )
-    DIVIDEND = "Dividend", "A payment to your account from shares you hold"
-    DEBIT = "Debit", "Funds taken out from your account, uncategorised by the bank"
-    FEE_CHARGE = "Fee Charge", "Fees or charges in relation to a transaction"
-    INTEREST = "Interest", "Credit or debit associated with interest earned or incurred"
-    OTHER = "Other", "Miscellaneous credit or debit"
-    PURCHASE = "Purchase", "A payment made with your debit or credit card"
-    STANDING_ORDER = (
-        "Standing Order",
-        "A payment instructed by the account-holder to a third party at regular"
-        " intervals",
-    )
-    TRANSFER = "Transfer", "Transfer of money between accounts"
-    UNKNOWN = "Unknown", "No classification of transaction category known"
+        Args:
+            payload (Dict[str, Any]): the DLNA DMR payload
 
-    def __init__(self, value, description):
-        self._value_ = value
-        self.description = description
+        Returns:
+            LastChange: The parsed `Case`.
 
+        Raises:
+            TypeError: if the payload isn't a dict
+            ValidationError: If any of the specified model fields are empty or of the
+             wrong type.
+            ValidationError: if more than just "Event" is in the payload
+        """
+        if not isinstance(payload, dict):
+            raise TypeError("Expected a dict")
+
+        payload = payload.copy()
+
+        event = payload.pop("Event")
+
+        if payload:
+            raise ValidationError(
+                [
+                    ErrorWrapper(ValueError("extra fields not permitted"), loc=key)
+                    for key in payload.keys()
+                ],
+                model=cls,
+            )
 
-class TrueLayerEntity:
-    """Parent class for all TrueLayer entities (accounts, cards, etc.)
+        return cls(Event=event)
 
-    Args:
-        json (dict): the JSON returned from the TrueLayer API which defines the
-         entity
-        truelayer_client (TrueLayerClient): a TrueLayer client, usually the one which
-         retrieved this entity from the API
-    """
 
-    # Default value
-    BALANCE_FIELDS = ()
+class LastChangeAVTransport(LastChange):
+    """BaseModel for an AVTransport DLNA payload."""
 
-    def __init__(self, json, truelayer_client=None, balance_update_threshold=15):
-        self.json = json
-        self._truelayer_client = truelayer_client
+    Event: EventAVTransport
 
-        self._available_balance = None
-        self._current_balance = None
-        self._overdraft = None
-        self._credit_limit = None
-        self._last_statement_balance = None
-        self._last_statement_date = None
-        self._payment_due = None
-        self._payment_due_date = None
 
-        self.entity_type = self.__class__.__name__.lower()
+class LastChangeRenderingControl(LastChange):
+    """BaseModel for a RenderingControl DLNA payload."""
 
-        self.last_balance_update = datetime(1970, 1, 1)
-        self.balance_update_threshold = balance_update_threshold
+    Event: EventRenderingControl
 
-    def get_transactions(self, from_datetime=None, to_datetime=None):
-        """Polls the TL API to get all transactions under the given entity. If
-        only one datetime parameter is provided, then the other is given a default
-        value which maximises the range of results returned
 
-        Args:
-            from_datetime (datetime): lower range of transaction date range query
-            to_datetime (datetime): upper range of transaction date range query
+LastChangeTypeVar = TypeVar("LastChangeTypeVar", bound=LastChange)
 
-        Yields:
-            Transaction: one instance per tx, including all metadata etc.
-        """
 
-        if from_datetime or to_datetime:
-            from_datetime = from_datetime or datetime.utcnow() - timedelta(days=90)
-            to_datetime = to_datetime or datetime.utcnow()
+class GetMediaInfoResponse(BaseModel):
+    """BaseModel for the response from a GetMediaInfo request."""
 
-            params = {
-                "from": from_datetime.strftime(DATETIME_FORMAT),
-                "to": to_datetime.strftime(DATETIME_FORMAT),
-            }
-        else:
-            params = None
+    NrTracks: int
+    MediaDuration: str
+    CurrentURI: str
+    CurrentURIMetaData: TrackMetaData
+    NextURI: str
+    NextURIMetaData: str
+    TrackSource: str
+    PlayMedium: str
+    RecordMedium: str
+    WriteStatus: str
 
-        results = self._truelayer_client.get_json_response(
-            f"/data/v1/{self.entity_type}s/{self.id}/transactions", params=params
-        ).get("results", [])
 
-        for result in results:
-            yield Transaction(result, self, self._truelayer_client)
+class CurrentTrack:
+    """Class for easy processing/passing of track metadata.
 
-    def update_balance_values(self):
-        """Updates the balance-related instance attributes with the latest values from
-        the API
-        """
+    Attributes:
+        album_art_uri (str): URL for album artwork
+        media_album_name (str): album name
+        media_artist (str): track's artist(s)
+        media_title (str): track's title
+    """
 
-        results = self._truelayer_client.get_json_response(
-            f"/data/v1/{self.entity_type}s/{self.id}/balance"
-        ).get("results")
+    DURATION_FORMAT = "%H:%M:%S.%f"
 
-        if len(results) != 1:
-            raise ValueError(
-                "Unexpected number of results when getting balance info:"
-                f" {len(results)}",
-            )
+    NULL_TRACK_STR = "NULL"
 
-        balance_result = results[0]
+    class Info(TypedDict):
+        """Info for the attributes of this class."""
 
-        self._available_balance = balance_result.get("available")
-        self._current_balance = balance_result.get("current")
-        self._overdraft = balance_result.get("overdraft")
-        self._credit_limit = balance_result.get("credit_limit")
-        self._last_statement_balance = balance_result.get("last_statement_balance")
-        self._last_statement_date = balance_result.get("last_statement_date")
-        self._payment_due = balance_result.get("payment_due")
-        self._payment_due_date = balance_result.get("payment_due_date")
+        album_art_uri: str | None
+        media_album_name: str | None
+        media_artist: str | None
+        media_duration: float
+        media_title: str | None
 
-        self.last_balance_update = datetime.utcnow()
-
-    def _get_balance_property(self, prop_name):
-        """Gets a value for a balance-specific property, updating the values if
-         necessary (i.e. if they don't already exist). This also has a check to see if
-         property is relevant for the given entity type and if not it just returns None
+    def __init__(
+        self,
+        *,
+        album_art_uri: str | None,
+        media_album_name: str | None,
+        media_artist: str | None,
+        media_duration: float,
+        media_title: str | None,
+    ):
+        self.album_art_uri = album_art_uri
+        self.media_album_name = media_album_name
+        self.media_artist = media_artist
+        self.media_duration = media_duration
+        self.media_title = media_title
+
+    @classmethod
+    def _create_from_metadata_item(
+        cls, metadata_item: TrackMetaDataItem
+    ) -> CurrentTrack:
+        """Create a CurrentTrack instance from a response metadata item.
 
         Args:
-            prop_name (str): the name of the property
+            metadata_item (TrackMetaDataItem): the metadata pulled from the response
 
         Returns:
-            str: the value of the balance property
+            CurrentTrack: instance containing relevant info
         """
+        duration_time = strptime(metadata_item.res.duration, cls.DURATION_FORMAT)
 
-        if prop_name not in self.BALANCE_FIELDS:
-            return None
-
-        if getattr(self, f"_{prop_name}") is None or self.last_balance_update <= (
-            datetime.utcnow() - timedelta(minutes=self.balance_update_threshold)
-        ):
-            self.update_balance_values()
-
-        return getattr(self, f"_{prop_name}")
-
-    @property
-    def available_balance(self):
-        """
-        Returns:
-            float: the amount of money available to the bank account holder
-        """
-        return self._get_balance_property("available_balance")
+        duration_delta = timedelta(
+            hours=duration_time.tm_hour,
+            minutes=duration_time.tm_min,
+            seconds=duration_time.tm_sec,
+        )
 
-    @property
-    def current_balance(self):
-        """
-        Returns:
-            float: the total amount of money in the account, including pending
-             transactions
-        """
-        return self._get_balance_property("current_balance")
+        return CurrentTrack(
+            album_art_uri=metadata_item.upnp_albumArtURI
+            if metadata_item.upnp_albumArtURI != "un_known"
+            else None,
+            media_album_name=metadata_item.upnp_album,
+            media_artist=metadata_item.dc_creator,
+            media_duration=duration_delta.total_seconds(),
+            media_title=metadata_item.dc_title,
+        )
 
-    @property
-    def overdraft(self):
-        """
-        Returns:
-            float: the overdraft limit of the account
-        """
-        return self._get_balance_property("overdraft")
+    @classmethod
+    def from_get_media_info(cls, response: GetMediaInfoResponse) -> CurrentTrack:
+        """Create a CurrentTrack instance from a GetMediaInfo response.
 
-    @property
-    def credit_limit(self):
-        """
-        Returns:
-            float: the credit limit available to the customer
-        """
-        return self._get_balance_property("credit_limit")
+        Args:
+            response (GetMediaInfoResponse): the response from a GetMediaInfo request
 
-    @property
-    def last_statement_balance(self):
-        """
         Returns:
-            float: the balance on the last statement
+            CurrentTrack: a CurrentTrack instance with relevant info
         """
-        return self._get_balance_property("last_statement_balance")
+        return cls._create_from_metadata_item(response.CurrentURIMetaData.item)
 
-    @property
-    def last_statement_date(self):
-        """
-        Returns:
-            date: the date the last statement was issued on
-        """
-        return self._get_balance_property("last_statement_date")
+    @classmethod
+    def from_last_change(cls, last_change: LastChangeTypeVar) -> CurrentTrack:
+        """Create a CurrentTrack instance from a LastChange response.
 
-    @property
-    def payment_due(self):
-        """
-        Returns:
-            float: the amount of any due payment
-        """
-        return self._get_balance_property("payment_due")
+        Args:
+            last_change (LastChangeAVTransport): the payload from the last DLNA change
 
-    @property
-    def payment_due_date(self):
-        """
         Returns:
-            date: the date on which the next payment is due
+            CurrentTrack: a CurrentTrack instance with relevant info
         """
-        return self._get_balance_property("payment_due_date")
+        return cls._create_from_metadata_item(
+            last_change.Event.InstanceID.CurrentTrackMetaData.item
+        )
 
-    @property
-    def pretty_json(self):
-        """
-        Returns:
-            str: a "pretty" version of the JSON, used for debugging etc.
-        """
-        return dumps(self.json, indent=4, default=str)
+    @classmethod
+    def null_track(cls) -> CurrentTrack:
+        """Create a null track.
 
-    @property
-    def currency(self):
-        """
         Returns:
-            str: ISO 4217 alpha-3 currency code of this entity
-        """
-        return self.json.get("currency")
+            CurrentTrack: a CurrentTrack instance with all attributes set to None
+        """
+        return cls(
+            album_art_uri=None,
+            media_album_name=None,
+            media_artist=None,
+            media_duration=0.0,
+            media_title=None,
+        )
 
     @property
-    def display_name(self):
-        """
-        Returns:
-            str: human-readable name of the entity
-        """
-        return self.json.get("display_name")
+    def json(self) -> CurrentTrack.Info:
+        """JSON representation of the current track.
 
-    @property
-    def id(self):
-        """
         Returns:
-            str: the unique ID for this entity
+            CurrentTrack.Info: info on the currently playing track
         """
-        return self.json.get("account_id")
+        return {
+            "album_art_uri": self.album_art_uri,
+            "media_album_name": self.media_album_name,
+            "media_artist": self.media_artist,
+            "media_duration": self.media_duration,
+            "media_title": self.media_title,
+        }
 
-    @property
-    def provider_name(self):
-        """
-        Returns:
-            str: the name of the account provider
-        """
-        return self.json.get("provider", {}).get("display_name")
+    def __eq__(self, other: object) -> bool:
+        """Check equality of this instance with another object.
 
-    @property
-    def provider_id(self):
-        """
-        Returns:
-            str: unique identifier for the provider
-        """
-        return self.json.get("provider", {}).get("provider_id")
+        Args:
+            other (object): the object to compare to
 
-    @property
-    def provider_logo_uri(self):
-        """
         Returns:
-            str: url for the account provider's logo
+            bool: True if the objects are equal, False otherwise
         """
-        return self.json.get("provider", {}).get("logo_uri")
+        if not isinstance(other, CurrentTrack):
+            return NotImplemented
 
-    def __str__(self):
-        return f"{self.display_name} | {self.provider_name}"
+        return self.json == other.json
 
+    def __repr__(self) -> str:
+        """Get a string representation of this instance."""
+        return f"{self.__class__.__name__}({self.__str__()!r})"
 
-class Transaction:
-    """Class for individual transactions for data manipulation etc.
+    def __str__(self) -> str:
+        """Return a string representation of the current track."""
 
-    Args:
-        parent_entity (TrueLayerEntity): the entity which this transaction was made
-         under
-    """
+        if self.media_title is None and self.media_artist is None:
+            return self.NULL_TRACK_STR
 
-    def __init__(self, json, parent_entity, truelayer_client=None):
-        self.json = json
-        self._truelayer_client = truelayer_client
-        self.parent_entity = parent_entity
+        return f"{self.media_title!r} by {self.media_artist}"
 
-    @property
-    def pretty_json(self):
-        """
-        Returns:
-            str: a "pretty" version of the JSON, used for debugging etc.
-        """
-        return dumps(self.json, indent=4, default=str)
 
-    @property
-    def id(self):
-        """
-        Returns:
-            str: unique ID for this transaction, it may change between requests
-        """
-        return self.json.get("transaction_id")
+class Yas209State(Enum):
+    """Enumeration for states as they come in the DLNA payload."""
 
-    @property
-    def currency(self):
-        """
-        Returns:
-            str: ISO 4217 alpha-3 currency code of this entity
-        """
-        return self.json.get("currency")
+    PLAYING = "playing", "Play"
+    PAUSED_PLAYBACK = "paused", "Pause"
+    STOPPED = "off", "Stop"
+    NO_MEDIA_PRESENT = "idle", None
+    UNKNOWN = "unknown", None
 
-    @property
-    def timestamp(self):
-        """
-        Returns:
-            datetime: the timestamp this transaction was made at
-        """
-        try:
-            return datetime.strptime(
-                self.json.get("timestamp"), "%Y-%m-%dT%H:%M:%S.%fZ"
-            )
-        except ValueError:
-            return datetime.strptime(self.json.get("timestamp"), "%Y-%m-%dT%H:%M:%SZ")
+    def __init__(self, value: str, action: str | None):
+        self._value_ = value
+        self.action = action
 
-    @property
-    def description(self):
-        """
-        Returns:
-            str: the description of this transaction
-        """
-        return self.json.get("description")
 
-    @property
-    def type(self):
-        """
-        Returns:
-            str: the type of transaction
-        """
-        return self.json.get("transaction_type")
+class Yas209Service(Enum):
+    """Enumeration for available YAS-209 services."""
 
-    @property
-    def category(self):
-        """
-        Returns:
-            str: the category of this transaction
-        """
-        return TransactionCategory[self.json.get("transaction_category", "UNKNOWN")]
+    AVT = (
+        "AVTransport",
+        "urn:upnp-org:serviceId:AVTransport",
+        "urn:schemas-upnp-org:service:AVTransport:1",
+        (
+            "GetCurrentTransportActions",
+            "GetDeviceCapabilities",
+            "GetInfoEx",
+            "GetMediaInfo",
+            "GetPlayType",
+            "GetPositionInfo",
+            "GetTransportInfo",
+            "GetTransportSettings",
+            "Next",
+            "Pause",
+            "Play",
+            "Previous",
+            "Seek",
+            "SeekBackward",
+            "SeekForward",
+            "SetAVTransportURI",
+            "SetPlayMode",
+            "Stop",
+        ),
+    )
+    CM = (
+        "ConnectionManager",
+        "urn:upnp-org:serviceId:ConnectionManager",
+        "urn:schemas-upnp-org:service:ConnectionManager:1",
+        (
+            "GetCurrentConnectionIDs",
+            "GetCurrentConnectionInfo",
+            "GetProtocolInfo",
+        ),
+    )
+    PQ = (
+        "PlayQueue",
+        "urn:wiimu-com:serviceId:PlayQueue",
+        "urn:schemas-wiimu-com:service:PlayQueue:1",
+        (
+            "AppendQueue",
+            "AppendTracksInQueue",
+            "AppendTracksInQueueEx",
+            "BackUpQueue",
+            "BrowseQueue",
+            "CreateQueue",
+            "DeleteActionQueue",
+            "DeleteQueue",
+            "GetKeyMapping",
+            "GetQueueIndex",
+            "GetQueueLoopMode",
+            "GetQueueOnline",
+            "GetUserAccountHistory",
+            "GetUserFavorites",
+            "GetUserInfo",
+            "PlayQueueWithIndex",
+            "RemoveTracksInQueue",
+            "ReplaceQueue",
+            "SearchQueueOnline",
+            "SetKeyMapping",
+            "SetQueueLoopMode",
+            "SetQueuePolicy",
+            "SetQueueRecord",
+            "SetSongsRecord",
+            "SetSpotifyPreset",
+            "SetUserFavorites",
+            "UserLogin",
+            "UserLogout",
+            "UserRegister",
+        ),
+    )
+    Q_PLAY = (
+        "QPlay",
+        "urn:tencent-com:serviceId:QPlay",
+        "urn:schemas-tencent-com:service:QPlay:1",
+        (
+            "GetMaxTracks",
+            "GetTracksCount",
+            "GetTracksInfo",
+            "InsertTracks",
+            "QPlayAuth",
+            "RemoveAllTracks",
+            "RemoveTracks",
+            "SetNetwork",
+            "SetTracksInfo",
+        ),
+    )
+    RC = (
+        "RenderingControl",
+        "urn:upnp-org:serviceId:RenderingControl",
+        "urn:schemas-upnp-org:service:RenderingControl:1",
+        (
+            "DeleteAlarmQueue",
+            "GetAlarmQueue",
+            "GetChannel",
+            "GetControlDeviceInfo",
+            "GetEqualizer",
+            "GetMute",
+            "GetSimpleDeviceInfo",
+            "GetVolume",
+            "ListPresets",
+            "MultiPlaySlaveMask",
+            "SelectPreset",
+            "SetAlarmQueue",
+            "SetChannel",
+            "SetDeviceName",
+            "SetEqualizer",
+            "SetMute",
+            "SetVolume",
+            "StreamServicesCapability",
+        ),
+    )
 
-    @property
-    def classifications(self):
-        """
-        Returns:
-            list: a list of classifications for this transaction
-        """
-        return self.json.get("transaction_classification")
+    def __init__(
+        self, value: str, service_id: str, service_name: str, actions: tuple[str]
+    ):
+        self._value_ = value
+        self.service_id = service_id
+        self.service_name = service_name
+        self.actions = actions
 
-    @property
-    def merchant_name(self):
-        """
-        Returns:
-            str: the name of the merchant with which this transaction was made
-        """
-        return self.json.get("merchant_name")
 
-    @property
-    def amount(self):
-        """
-        Returns:
-            float: the amount this transaction is for
-        """
-        return self.json.get("amount")
+def _needs_device(
+    func: Callable[[YamahaYas209], Coroutine[Any, Any, Mapping[str, Any] | None]]
+) -> Callable[[YamahaYas209], Any]:
+    """Use as a decorator to ensure the device is available.
 
-    @property
-    def provider_transaction_id(self):
-        """
-        Returns:
-            str: the tx ID from the provider
-        """
-        return self.json.get("provider_transaction_id")
+    This decorator is used when the DLNA device is needed and provides a clean
+    way of instantiating it lazily
 
-    @property
-    def normalised_provider_transaction_id(self):
-        """
-        Returns:
-            str: a normalised tx ID, less likely to change
-        """
-        return self.json.get("normalised_provider_transaction_id")
+    Args:
+        func (Callable): the function being wrapped
 
-    @property
-    def provider_category(self):
-        """
-        Returns:
-            str: the provider transaction category
-        """
-        return self.json.get("meta", {}).get("provider_category")
+    Returns:
+        Callable: the inner function
+    """
 
-    @property
-    def provider_transaction_type(self):
-        """
-        Returns:
-            str: the type of transaction, as seen by the provider?
-        """
-        return self.json.get("meta", {}).get("transaction_type")
+    @wraps(func)
+    def create_device(yas_209: YamahaYas209) -> Any:
+        """Create the device before executing the wrapped method.
 
-    @property
-    def counter_party_preferred_name(self):
-        """
-        Returns:
-            str: the preferred name of the merchant
-        """
-        return self.json.get("meta", {}).get("counter_party_preferred_name")
+        Args:
+            yas_209 (YamahaYas209): the YamahaYas209 instance
 
-    @property
-    def provider_id(self):
-        """
         Returns:
-            str: seems to be the same as `self.provider_transaction_id`
+            Any: the result of the wrapped function
         """
-        return self.json.get("meta", {}).get("provider_id")
+        if not hasattr(yas_209, "device"):
+            requester = AiohttpRequester()
+            factory = UpnpFactory(requester)
 
-    @property
-    def debtor_account_name(self):
-        """
-        Returns:
-            str: the account name of the debtor, if the tx is inbound
-        """
-        return self.json.get("meta", {}).get("debtor_account_name")
+            async def _create() -> None:
+                yas_209.device = await factory.async_create_device(
+                    yas_209.description_url
+                )
 
-    def __str__(self):
-        return f"{self.description} | {self.amount} | {self.merchant_name}"
+            run(_create())
 
+        return func(yas_209)
 
-class Account(TrueLayerEntity):
-    """Class for managing individual bank accounts"""
+    return create_device
 
-    BALANCE_FIELDS = ("available_balance", "current_balance", "overdraft")
 
-    def __init__(self, *args, **kwargs):
-        super().__init__(*args, **kwargs)
+class YamahaYas209:
+    """Class for consuming information from a YAS-209 in real time.
 
-    @property
-    def type(self):
-        """
-        Returns:
-            str: type of the account
-        """
-        return self.json.get("account_type")
+    Callback functions can be provided, as well as the option to start the
+    listener immediately.
 
-    @property
-    def iban(self):
-        """
-        Returns:
-            str: the International Bank Account Number for this account
-        """
-        return self.json.get("account_number", {}).get("iban")
+    Args:
+        ip (str): the IP address of the YAS-209
+        on_event (Callable[[YamahaYas209, Event], None], optional): a callback
+            function to be called when an event is received. Defaults to None.
+        start_listener (bool, optional): whether to start the listener
+        on_volume_update (Callable[[YamahaYas209, int], None], optional): a
+            callback function to be called when the volume is updated. Defaults
+            to None.
+        on_track_update (Callable[[YamahaYas209, Track], None], optional): a
+            callback function to be called when the track is updated. Defaults
+            to None.
+        on_state_update (Callable[[YamahaYas209, State], None], optional): a
+            callback function to be called when the state is updated. Defaults
+            to None.
+        logging (bool, optional): whether to log events. Defaults to False.
+        listen_ip (str, optional): the IP address to listen on. Defaults to
+            None.
+        listen_port (int, optional): the port to listen on. Defaults to None.
+        source_port (int, optional): the port to use for the source. Defaults
+            to None.
+    """
 
-    @property
-    def swift_bic(self):
-        """
-        Returns:
-            str: ISO 9362:2009 Business Identifier Codes.
-        """
-        return self.json.get("account_number", {}).get("swift_bic")
+    SUBSCRIPTION_SERVICES = (
+        Yas209Service.AVT.service_id,
+        Yas209Service.RC.service_id,
+    )
 
-    @property
-    def account_number(self):
-        """
-        Returns:
-            str: the account's account number
-        """
-        return self.json.get("account_number", {}).get("number")
+    LAST_CHANGE_PAYLOAD_PARSERS = {
+        Yas209Service.AVT.service_id: LastChangeAVTransport.parse,
+        Yas209Service.RC.service_id: LastChangeRenderingControl.parse,
+    }
+
+    class EventPayloadInfo(TypedDict):
+        """Info for the payload sent to the `on_event` callback."""
+
+        timestamp: datetime
+        service_id: str
+        service_type: str
+        last_change: LastChange
+        other_xml_payloads: dict[str, Any]
 
-    @property
-    def sort_code(self):
-        """
-        Returns:
-            str: the account's sort code
-        """
-        return self.json.get("account_number", {}).get("sort_code")
+    def __init__(
+        self,
+        ip: str,
+        *,
+        on_event: Callable[[EventPayloadInfo], None] | None = None,
+        start_listener: bool = False,
+        on_volume_update: Callable[[float], None] | None = None,
+        on_track_update: Callable[[CurrentTrack.Info], None] | None = None,
+        on_state_update: Callable[[str], None] | None = None,
+        logging: bool = True,
+        listen_ip: str | None = None,
+        listen_port: int | None = None,
+        source_port: int | None = None,
+    ):
+        self.ip = ip
+        self.on_event = on_event
 
+        # noinspection HttpUrlsUsage
+        self.description_url = f"http://{ip}:49152/description.xml"
 
-class Card(TrueLayerEntity):
-    """Class for managing individual cards"""
+        self.on_volume_update = on_volume_update
+        self.on_track_update = on_track_update
+        self.on_state_update = on_state_update
 
-    BALANCE_FIELDS = (
-        "available_balance",
-        "current_balance",
-        "credit_limit",
-        "last_statement_balance",
-        "last_statement_date",
-        "payment_due",
-        "payment_due_date",
-    )
+        self._current_track: CurrentTrack
+        self._state: Yas209State
+        self._volume_level: float
 
-    def __init__(self, *args, **kwargs):
-        super().__init__(*args, **kwargs)
+        self._listening = False
 
-    @property
-    def card_network(self):
-        """
-        Returns:
-            str: card processor. For example, VISA
-        """
-        return self.json.get("card_network")
+        self.device: UpnpDevice
 
-    @property
-    def type(self):
-        """
-        Returns:
-            str: type of card: credit, debit
-        """
-        return self.json.get("card_type")
+        self._logging = logging
+        self._listen_ip = listen_ip
+        self._listen_port = listen_port
+        self._source_port = source_port or 0
 
-    @property
-    def partial_card_number(self):
-        """
-        Returns:
-            str: last few digits of card number
-        """
-        return self.json.get("partial_card_number")
+        self._active_service_ids: list[str] = []
 
-    @property
-    def name_on_card(self):
-        """
-        Returns:
-            str: the name on the card
-        """
-        return self.json.get("name_on_card")
+        if self._listen_ip is not None and self._listen_port is None:
+            raise ValueError(
+                "Argument `listen_port` cannot be None when `listen_ip` is not None:"
+                f" {self._listen_ip!r}"
+            )
 
+        if start_listener:
+            self.listen()
 
-class TrueLayerClient:
-    """Custom client for interacting with TrueLayer's APIs, including all necessary
-    authentication functionality
+    def listen(self) -> None:
+        """Start the listener."""
+        if self._logging:
+            LOGGER.info("Starting listener")
+
+        if self._listening:
+            if self._logging:
+                LOGGER.debug(
+                    "Already listening to '%s', returning immediately",
+                    "', '".join(self._active_service_ids),
+                )
+            return
 
-    Args:
-        client_id (str): the client ID for the TrueLayer application
-        client_secret (str): the client secret
-        bank (Bank): the bank which we're working with
-        redirect_uri (str): the redirect URI for the auth flow
-        access_token_expiry_threshold (int): the number of seconds to subtract from
-         the access token's expiry when checking its expiry status
-        log_requests (bool): flag for choosing if to log all requests made
-        creds_cache_path (str): file path for where to cache credentials
-    """
+        worker_exception: BaseException | None = None
 
-    BASE_URL = "https://api.truelayer.com"
-    ACCESS_TOKEN_ENDPOINT = "https://auth.truelayer.com/connect/token"
-    CREDS_FILE_PATH = user_data_dir(file_name="truelayer_api_creds.json")
+        def _worker() -> None:
+            nonlocal worker_exception
+            try:
+                new_event_loop().run_until_complete(self._subscribe())
+            except Exception as exc:  # pylint: disable=broad-except
+                worker_exception = exc
+
+        listener_thread = Thread(target=_worker)
+        listener_thread.start()
+
+        while not self._listening and worker_exception is None:
+            sleep(0.01)
+
+        if isinstance(worker_exception, BaseException):
+            raise worker_exception  # pylint: disable=raising-bad-type
+
+        if self._logging:
+            LOGGER.debug(
+                "Listen action complete, now subscribed to '%s'",
+                "', '".join(self._active_service_ids),
+            )
 
-    def __init__(
-        self,
-        *,
-        client_id,
-        client_secret,
-        bank,
-        redirect_uri="https://console.truelayer.com/redirect-page",
-        access_token_expiry_threshold=60,
-        log_requests=False,
-        creds_cache_path=None,
-    ):
-        self.client_id = client_id
-        self.client_secret = client_secret
-        self.bank = bank
-        self.redirect_uri = redirect_uri
-        self.access_token_expiry_threshold = access_token_expiry_threshold
-        self.log_requests = log_requests
-        self.creds_cache_path = creds_cache_path or self.CREDS_FILE_PATH
+    def on_event_wrapper(
+        self, service: UpnpService, service_variables: Sequence[UpnpStateVariable[str]]
+    ) -> None:
+        """Wrap the `on_event` callback to process the XML payload(s) first.
 
-        self.auth_code_env_var = f"TRUELAYER_{self.bank.name}_AUTH_CODE"
+        Args:
+            service (UpnpService): the service which has sent an update
+            service_variables (list): a list of state variables that have updated
+        """
 
-        self._credentials = None
+        xml_payloads: dict[str, object] = {
+            sv.name: sv.value for sv in service_variables
+        }
 
-    def _get(self, url, params=None):
-        """Wrapper for GET requests which covers authentication, URL parsing, etc etc
+        # Convert any nested XML into JSON
+        self._parse_xml_dict(xml_payloads)
 
-        Args:
-            url (str): the URL path to the endpoint (not necessarily including the
-             base URL)
-            params (dict): the parameters to be passed in the HTTP request
+        last_change = self.LAST_CHANGE_PAYLOAD_PARSERS[service.service_id](
+            xml_payloads.pop("LastChange")  # type: ignore[arg-type]
+        )
 
-        Returns:
-            Response: the response from the HTTP request
-        """
+        event_payload: YamahaYas209.EventPayloadInfo = {
+            "timestamp": datetime.utcnow(),
+            "service_id": service.service_id,
+            "service_type": service.service_type,
+            "last_change": last_change,
+            "other_xml_payloads": xml_payloads,
+        }
 
-        if url.startswith("/"):
-            url = f"{self.BASE_URL}{url}"
+        if service.service_id == "urn:upnp-org:serviceId:AVTransport":
+            if last_change.Event.InstanceID.TransportState != self.state.name:
+                self.set_state(
+                    Yas209State[last_change.Event.InstanceID.TransportState],
+                    local_only=True,
+                )
+            if last_change.Event.InstanceID.CurrentTrackMetaData is None:
+                self.current_track = CurrentTrack.null_track()
+            else:
+                self.current_track = CurrentTrack.from_last_change(last_change)
+        elif service.service_id == "urn:upnp-org:serviceId:RenderingControl":
+            # The DLNA payload has volume as a string value between 0 and 100
+            self.set_volume_level(
+                float(last_change.Event.InstanceID.Volume.val) / 100, local_only=True
+            )
 
-        if self.log_requests:
-            LOGGER.debug("GET %s with params %s", url, dumps(params or {}, default=str))
+        if self.on_event is not None:
+            self.on_event(event_payload)
 
-        res = get(
-            url,
-            headers={"Authorization": f"Bearer {self.access_token}"},
-            params=params or {},
+    # noinspection PyArgumentList
+    @_needs_device
+    async def _subscribe(self) -> None:
+        # pylint: disable=too-many-branches
+        """Subscribe to service(s) and output updates."""
+        # start notify server/event handler
+        local_ip = get_local_ip(self.device.device_url)
+        source = (local_ip, self._source_port)
+
+        callback_url = (
+            None
+            if self._listen_port is None
+            else f"http://{self._listen_ip or local_ip}:{self._listen_port}/notify"
+        )
+        server = AiohttpNotifyServer(
+            self.device.requester, source=source, callback_url=callback_url
         )
+        await server.async_start_server()
 
-        res.raise_for_status()
+        if self._logging:
+            LOGGER.debug(
+                dedent(
+                    """
+            Listen IP:          %s
+            Listen Port:        %s
+            Source IP:          %s
+            Source Port:        %s
+            Callback URL:       %s
+            Server Listen IP:   %s
+            Server Listen Port: %s
+            """
+                ),
+                self._listen_ip,
+                str(self._listen_port),
+                local_ip,
+                str(self._source_port),
+                str(callback_url),
+                server.listen_ip,
+                server.listen_port,
+            )
 
-        return res
+        # create service subscriptions
+        failed_subscriptions = []
+        for service in self.device.services.values():
+            if service.service_id not in self.SUBSCRIPTION_SERVICES:
+                continue
 
-    def _get_entity_by_id(self, entity_id, entity_class, entity_instance_kwargs=None):
-        """Gets entity info based on a given ID
+            service.on_event = self.on_event_wrapper
+            try:
+                await server.event_handler.async_subscribe(service)
+                self._active_service_ids.append(service.service_id)
+                LOGGER.info("Subscribed to %s", service.service_id)
+            except UpnpCommunicationError as exc:
+                if self._logging:
+                    LOGGER.exception(
+                        "Unable to subscribe to %s: %s",
+                        service.service_id,
+                        repr(exc),
+                    )
+                failed_subscriptions.append(service)
 
-        Args:
-            entity_id (str): the unique ID for the account/card
-            entity_class (type): the class to instantiate with the returned info
-            entity_instance_kwargs (dict): any kwargs to pass to the entity instance
+        self._listening = True
 
-        Returns:
-            Union([Account, Card]): a Card instance with associated info
+        # keep the webservice running (force resubscribe)
+        while self._listening:
+            for _ in range(120):
+                if not self._listening:
+                    if self._logging:
+                        LOGGER.debug("Exiting listener loop")
+                    break
+                await async_sleep(1)
+
+            # The break above only covers the for loop, this is for the while loop
+            if not self._listening:
+                break
+
+            LOGGER.debug("Resubscribing to all services")
+            await server.event_handler.async_resubscribe_all()
+
+            services_to_remove = []
+            for service in failed_subscriptions:
+                try:
+                    if self._logging:
+                        LOGGER.debug(
+                            "Attempting to create originally failed subscription for"
+                            " %s",
+                            service.service_id,
+                        )
+                    await server.event_handler.async_subscribe(service)
+                    self._active_service_ids.append(service.service_id)
+                    services_to_remove.append(service)
+                except UpnpCommunicationError as exc:
+                    log_message = (
+                        f"Still unable to subscribe to {service.service_id}:"
+                        f" {exc!r}"
+                    )
 
-        Raises:
-            HTTPError: if a HTTPError is raised by the request, and it's not because
-             the ID wasn't found
-            ValueError: if >1 result is returned from the TrueLayer API
-        """
-        try:
-            results = self.get_json_response(
-                f"/data/v1/{entity_class.__name__.lower()}s/{entity_id}"
-            ).get("results", [])
-        except HTTPError as exc:
-            if exc.response.json().get("error") == "account_not_found":
-                return None
-            raise
+                    if self._logging:
+                        LOGGER.exception(log_message)
+                    else:
+                        # Should still log this exception, regardless
+                        LOGGER.warning(log_message)
+
+            # This needs to be separate because `.remove` is the cleanest way to remove
+            # the items, but can't be done within the loop, and I can't `deepcopy`
+            # `failed_subscriptions` and its threaded content
+            for service in services_to_remove:
+                failed_subscriptions.remove(service)
+
+        if self._logging:
+            LOGGER.debug(
+                "Exiting subscription loop, `self._listening` is `%s`",
+                str(self._listening),
+            )
 
-        if len(results) != 1:
+    def _call_service_action(
+        self,
+        service: Yas209Service,
+        action: str,
+        callback: Callable[[Mapping[str, object]], None] | None = None,
+        **call_kwargs: str | int,
+    ) -> dict[str, Any] | None:
+        if action not in service.actions:
             raise ValueError(
-                f"Unexpected number of results when getting {entity_class.__name__}:"
-                f" {len(results)}",
+                f"Unexpected action {action!r} for service {service.value!r}. "
+                f"""Must be one of '{"', '".join(service.actions)}'"""
             )
 
-        return entity_class(results[0], self, **entity_instance_kwargs or {})
+        @_needs_device
+        async def _worker(_: YamahaYas209) -> Mapping[str, Any]:
+            res: Mapping[str, Any] = (
+                await self.device.services[service.service_name]
+                .action(action)
+                .async_call(**call_kwargs)
+            )
 
-    def get_json_response(self, url, params=None):
-        """Gets a simple JSON object from a URL
+            if callback is not None:
+                callback(res)
 
-        Args:
-            url (str): the API endpoint to GET
-            params (dict): the parameters to be passed in the HTTP request
+            return res
 
-        Returns:
-            dict: the JSON from the response
-        """
-        return self._get(url, params=params).json()
+        return run(_worker(self))  # type: ignore[no-any-return]
 
-    def get_account_by_id(self, account_id, instance_kwargs=None):
-        """Get an Account instance based on the ID
+    @staticmethod
+    def _parse_xml_dict(xml_dict: dict[str, object]) -> None:
+        """Convert XML to JSON within dict in place.
 
-        Args:
-            account_id (str): the ID of the card
-            instance_kwargs (dict): any kwargs to pass to the Account instance
+        Parse a dictionary where some values are/could be XML strings, and unpack
+        the XML into JSON within the dict
 
-        Returns:
-            Account: a Account instance, with all relevant info
+        Args:
+            xml_dict (dict): the dictionary to parse
         """
-        return self._get_entity_by_id(account_id, Account, instance_kwargs)
+        traverse_dict(
+            xml_dict,
+            target_type=str,
+            target_processor_func=lambda val, dict_key=None, list_index=None: parse_xml(
+                val, attr_prefix="", cdata_key="text"
+            ),
+            single_keys_to_remove=["val", "DIDL-Lite"],
+        )
 
-    def get_card_by_id(self, card_id, instance_kwargs=None):
-        """Get a Card instance based on the ID
+    # TODO: @on_exception()
+    def pause(self) -> None:
+        """Pause the current media."""
+        self._call_service_action(Yas209Service.AVT, "Pause", InstanceID=0)
+
+    def play(self) -> None:
+        """Play the current media."""
+        self._call_service_action(Yas209Service.AVT, "Play", InstanceID=0, Speed="1")
+
+    def play_pause(self) -> None:
+        """Toggle the playing/paused state."""
+        if self.state == Yas209State.PLAYING:
+            self.pause()
+        else:
+            self.play()
 
-        Args:
-            card_id (str): the ID of the card
-            instance_kwargs (dict): any kwargs to pass to the Card instance
+    def mute(self) -> None:
+        """Mute."""
+        self._call_service_action(
+            Yas209Service.RC,
+            "SetMute",
+            InstanceID=0,
+            Channel="Master",
+            DesiredMute=True,
+        )
 
-        Returns:
-            Card: a Card instance, with all relevant info
-        """
-        return self._get_entity_by_id(card_id, Card, instance_kwargs)
+    def next_track(self) -> None:
+        """Skip to the next track."""
+        self._call_service_action(Yas209Service.AVT, "Next", InstanceID=0)
+
+    def previous_track(self) -> None:
+        """Go to the previous track."""
+        self._call_service_action(Yas209Service.AVT, "Previous", InstanceID=0)
 
-    def list_accounts(self):
-        """Lists all accounts under the given bank account
+    def set_state(self, value: Yas209State, local_only: bool = False) -> None:
+        """Set the state to the given value.
 
-        Yields:
-            Account: Account instances, containing all related info
+        Args:
+            value (Yas209State): the new state of the YAS-209
+            local_only (bool): only change the local value of the state (i.e. don't
+             update the soundbar)
 
         Raises:
-            HTTPError: if a HTTPError is raised by the _get method, but it's not a 501
+            TypeError: if the value is not a valid state
         """
-        try:
-            res = self.get_json_response(
-                "/data/v1/accounts",
-            )
-        except HTTPError as exc:
-            if exc.response.json().get("error") == "endpoint_not_supported":
-                LOGGER.warning("Accounts endpoint not supported by %s", self.bank.value)
-                res = {}
-            else:
-                raise
+        if not isinstance(value, Yas209State):
+            raise TypeError("Expected a Yas209State instance.")
+
+        self._state = value
+
+        if not local_only:
+            func = {
+                Yas209State.PLAYING: self.play,
+                Yas209State.PAUSED_PLAYBACK: self.pause,
+                Yas209State.STOPPED: self.stop,
+            }.get(value)
 
-        for result in res.get("results", []):
-            yield Account(result, self)
+            if func is not None:
+                func()
 
-    def list_cards(self):
-        """Lists all accounts under the given bank account
+        if self.on_state_update is not None:
+            self.on_state_update(self._state.value)
 
-        Yields:
-            Account: Account instances, containing all related info
+    def set_volume_level(self, value: float, local_only: bool = False) -> None:
+        """Set the soundbar's volume level.
+
+        Args:
+            value (float): the new volume level, as a float between 0 and 1
+            local_only (bool): only change the local value of the volume level (i.e.
+             don't update the soundbar)
 
         Raises:
-            HTTPError: if a HTTPError is raised by the _get method, but it's not a 501
+            ValueError: if the value is not between 0 and 1
         """
-        try:
-            res = self.get_json_response(
-                "/data/v1/cards",
-            )
-        except HTTPError as exc:
-            if exc.response.json().get("error") == "endpoint_not_supported":
-                LOGGER.warning("Cards endpoint not supported by %s", self.bank.value)
-                res = {}
-            else:
-                raise
 
-        for result in res.get("results", []):
-            yield Card(result, self)
+        if not 0 <= value <= 1:
+            raise ValueError("Volume level must be between 0 and 1")
 
-    def refresh_access_token(self):
-        """Uses the cached refresh token to submit a request to TL's API for a new
-        access token"""
-
-        LOGGER.info("Refreshing access token for %s", self.bank.value)
-
-        res = post(
-            self.ACCESS_TOKEN_ENDPOINT,
-            data={
-                "grant_type": "refresh_token",
-                "client_id": self.client_id,
-                "client_secret": self.client_secret,
-                "refresh_token": self._credentials.get("refresh_token"),
-            },
-        )
-
-        res.raise_for_status()
-
-        # Maintain any existing credential values in the dictionary whilst updating
-        # new ones
-        self.credentials = {
-            **self._credentials,
-            **res.json(),
-        }
+        self._volume_level = round(value, 2)
 
-    def authenticate_against_bank(self, code):
-        """Allows first-time (or repeated) authentication against the given bank
+        if not local_only:
+            self._call_service_action(
+                Yas209Service.RC,
+                "SetVolume",
+                InstanceID=0,
+                Channel="Master",
+                DesiredVolume=int(self._volume_level * 100),
+            )
 
-        Args:
-            code (str): the authorization code returned from the TrueLayer console
-             auth flow
-        """
+        if self.on_volume_update is not None:
+            self.on_volume_update(self._volume_level)
 
-        res = post(
-            self.ACCESS_TOKEN_ENDPOINT,
-            data={
-                "grant_type": "authorization_code",
-                "client_id": self.client_id,
-                "client_secret": self.client_secret,
-                "redirect_uri": self.redirect_uri,
-                "code": code,
-            },
+    def stop(self) -> None:
+        """Stop whatever is currently playing."""
+        self._call_service_action(Yas209Service.AVT, "Stop", InstanceID=0, Speed="1")
+
+    def stop_listening(self) -> None:
+        """Stop the event listener."""
+        if self._logging:
+            LOGGER.debug("Stopping event listener (will take <= 2 minutes)")
+
+        self._listening = False
+
+    def unmute(self) -> None:
+        """Unmute."""
+        self._call_service_action(
+            Yas209Service.RC,
+            "SetMute",
+            InstanceID=0,
+            Channel="Master",
+            DesiredMute=False,
         )
 
-        res.raise_for_status()
+    def volume_down(self) -> None:
+        """Decrease the volume by 2 points."""
+        self.set_volume_level(round(self.volume_level - 0.02, 2))
 
-        self.credentials = res.json()
+    def volume_up(self) -> None:
+        """Increase the volume by 2 points."""
+        self.set_volume_level(round(self.volume_level + 0.02, 2))
 
     @property
-    def authentication_link(self):
-        """
+    def album_art_uri(self) -> str | None:
+        """Album art URI for the currently playing media.
+
         Returns:
-            str: the authentication link, including the client ID
+            str: URL for the current album's artwork
         """
-        # pylint: disable=line-too-long
-        return f"https://auth.truelayer.com/?response_type=code&client_id={self.client_id}&scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access&redirect_uri={self.redirect_uri}&providers=uk-ob-all%20uk-oauth-all"  # noqa
+        return self.current_track.album_art_uri
 
     @property
-    def credentials(self):
-        """Attempts to retrieve credentials from local cache, creates new ones if
-        they're not found.
+    def current_track(self) -> CurrentTrack:
+        """Currently playing track.
 
         Returns:
-            dict: the credentials for the chosen bank
+            dict: the current track's info
+        """
+        if not hasattr(self, "_current_track"):
+            media_info = self.get_media_info()
+            self._current_track = CurrentTrack.from_get_media_info(
+                GetMediaInfoResponse.parse_obj(media_info)
+            )
+
+        return self._current_track
+
+    @current_track.setter
+    def current_track(self, value: CurrentTrack) -> None:
+        """Set the current track.
+
+        Args:
+            value (CurrentTrack): the new current track
 
         Raises:
-            EOFError: when no data is successfully returned for the auth code (usually
-             when running the script automatically)
-            ValueError: if no auth code is provided (manually or via env var)
+            TypeError: if the value is not a CurrentTrack instance
         """
 
-        try:
-            with open(self.creds_cache_path, encoding="UTF-8") as fin:
-                self._credentials = (
-                    load(fin).get(self.client_id, {}).get(self.bank.name)
-                )
-        except FileNotFoundError:
-            LOGGER.info("Unable to find local creds file")
-            self._credentials = {}
-
-        if not self._credentials:
-            LOGGER.info("Performing first time login for bank `%s`", self.bank.value)
-            LOGGER.debug("Opening %s", self.authentication_link)
-            open_browser(self.authentication_link)
-            try:
-                code = input(
-                    "Enter the authorization code "
-                    f"(or set as env var `{self.auth_code_env_var}`): "
-                ) or getenv(self.auth_code_env_var)
-            except EOFError:
-                if not (code := getenv(self.auth_code_env_var)):
-                    LOGGER.critical(
-                        "Unable to retrieve auth code from environment variables "
-                        "post-EOFError"
-                    )
-                    raise
+        if not isinstance(value, CurrentTrack):
+            raise TypeError("Expected a CurrentTrack instance.")
 
-            if not code:
-                raise ValueError("No auth code provided")
+        self._current_track = value
 
-            self.authenticate_against_bank(code)
+        if self.on_track_update is not None:
+            self.on_track_update(value.json)
 
-        if self.access_token_has_expired:
-            self.refresh_access_token()
+    @property
+    def is_listening(self) -> bool:
+        """Whether the event listener is running.
 
-        return self._credentials
+        Returns:
+            bool: whether the event listener is running
+        """
+        return self._listening
 
-    @credentials.setter
-    def credentials(self, value):
-        self._credentials = value
+    @property
+    def media_album_name(self) -> str | None:
+        """Name of the current album.
 
-        try:
-            with open(
-                force_mkdir(self.creds_cache_path, path_is_file=True), encoding="UTF-8"
-            ) as fin:
-                all_credentials = load(fin)
-        except FileNotFoundError:
-            all_credentials = {}
+        Returns:
+            str: the current media_title
+        """
+        return self.current_track.media_album_name
 
-        all_credentials.setdefault(self.client_id, {})[
-            self.bank.name
-        ] = self._credentials
+    @property
+    def media_artist(self) -> str | None:
+        """Currently playing artist.
 
-        with open(self.creds_cache_path, "w", encoding="UTF-8") as fout:
-            dump(all_credentials, fout)
+        Returns:
+            str: the current media_artist
+        """
+        return self.current_track.media_artist
 
     @property
-    def access_token(self):
+    def media_duration(self) -> float | None:
+        """Duration of current playing media in seconds.
+
+        Returns:
+            str: the current media_duration
         """
+        return self.current_track.media_duration
+
+    def get_media_info(self) -> dict[str, Any]:
+        """Get the current media info from the soundbar.
+
         Returns:
-            str: the access token for this bank's API
+            dict: the response in JSON form
         """
-        return self.credentials.get("access_token")
+
+        media_info = (
+            self._call_service_action(Yas209Service.AVT, "GetMediaInfo", InstanceID=0)
+            or {}
+        )
+
+        self._parse_xml_dict(media_info)
+
+        return media_info
 
     @property
-    def access_token_has_expired(self):
-        """Decodes the JWT access token and evaluates the expiry time
+    def media_title(self) -> str | None:
+        """Currently playing media title.
 
         Returns:
-            bool: has the access token expired?
+            str: the current media_album_name
         """
-        try:
-            expiry_epoch = decode(
-                # can't use self.access_token here, as that uses self.credentials,
-                # which in turn (recursively) checks if the access token has expired
-                self._credentials.get("access_token"),
-                options={"verify_signature": False},
-            ).get("exp", 0)
-
-            return (expiry_epoch - self.access_token_expiry_threshold) < int(time())
-        except DecodeError:
-            # treat invalid token as expired, so we get a new one
-            return True
+        return self.current_track.media_title
 
     @property
-    def refresh_token(self):
-        """
+    def state(self) -> Yas209State:
+        """Current state of the soundbar.
+
         Returns:
-            str: the TL API refresh token
+            Yas209State: the current state of the YAS-209 (e.g. playing, stopped)
         """
-        return self.credentials.get("refresh_token")
+        if hasattr(self, "_state"):
+            return self._state
+
+        return Yas209State.UNKNOWN
 
     @property
-    def scope(self):
-        """
+    def volume_level(self) -> float:
+        """Current volume level.
+
         Returns:
-            list: a list of active API scopes for the current application
+            float: the current volume level
         """
-        return self.credentials.get("scope", "").split()
+        if not hasattr(self, "_volume_level"):
+            res = (
+                self._call_service_action(
+                    Yas209Service.RC,
+                    "GetVolume",
+                    InstanceID=0,
+                    Channel="Master",
+                )
+                or {}
+            )
+
+            self._volume_level = float(res.get("CurrentVolume", 0) / 100)
+
+        return self._volume_level
```

### Comparing `wg_utilities-2.9.0/wg_utilities/epd/__init__.py` & `wg_utilities-3.0.0/wg_utilities/devices/epd/__init__.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,12 +1,14 @@
-"""Drivers obtained from https://github.com/waveshare/e-Paper"""
-from logging import Formatter, getLogger, DEBUG, StreamHandler
+"""Drivers obtained from https://github.com/waveshare/e-Paper/."""
+from __future__ import annotations
+
+from logging import DEBUG, Formatter, StreamHandler, getLogger
 from sys import stdout
 
-from .epd7in5_v2 import EPD_WIDTH, EPD_HEIGHT
+from .epd7in5_v2 import EPD_HEIGHT, EPD_WIDTH
 from .epdconfig import TEST_MODE, implementation
 
 _FORMATTER = Formatter(
     "%(asctime)s\t%(name)s\t[%(levelname)s]\t%(message)s", "%Y-%m-%d %H:%M:%S"
 )
 
 _SH = StreamHandler(stdout)
@@ -23,14 +25,15 @@
 else:
     from .epd7in5_v2 import EPD as EPD_ORIG
 
     _LOGGER.warning("Unable to import E-Paper Driver, running in test mode")
     FRAME_DELAY = 0
 
     # pylint: disable=too-few-public-methods
-    class EPD:
-        """Dynamically built class to mirror the functionality of the EPD on devices
-        which don't support it"""
+    class EPD:  # type: ignore[no-redef]
+        """Mirror the functionality of the EPD on devices which don't support it."""
 
     for method in dir(EPD_ORIG):
         if not method.startswith("_"):
             setattr(EPD, method, lambda *a, **k: None)
+
+__all__ = ["EPD", "EPD_HEIGHT", "EPD_WIDTH", "implementation", "FRAME_DELAY"]
```

### Comparing `wg_utilities-2.9.0/wg_utilities/epd/epd7in5_v2.py` & `wg_utilities-3.0.0/wg_utilities/devices/epd/epd7in5_v2.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,8 +1,9 @@
-"""
+"""EPD class.
+
 * | File        :	  epd7in5.py
 * | Author      :   Waveshare team
 * | Function    :   Electronic paper driver
 * | Info        :
 *----------------
 * | This version:   V4.0
 * | Date        :   2019-06-20
@@ -22,82 +23,85 @@
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS OR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
 """
-# pylint: disable=missing-function-docstring,missing-class-docstring,no-member
+from __future__ import annotations
 
+# pylint: disable=missing-function-docstring,missing-class-docstring,no-member
 from logging import debug
 
-from wg_utilities.epd import epdconfig
+from PIL.Image import Image
+
+from wg_utilities.devices.epd import epdconfig
 
 # Display resolution
 EPD_WIDTH = 800
 EPD_HEIGHT = 480
 
 
 # noinspection PyUnresolvedReferences,PyMissingOrEmptyDocstring,SpellCheckingInspection
-class EPD:
-    def __init__(self):
-        self.reset_pin = epdconfig.RST_PIN
-        self.dc_pin = epdconfig.DC_PIN
-        self.busy_pin = epdconfig.BUSY_PIN
-        self.cs_pin = epdconfig.CS_PIN
+class EPD:  # noqa: D101
+    def __init__(self) -> None:
+        self.reset_pin = epdconfig.RST_PIN  # type: ignore[attr-defined]
+        self.dc_pin = epdconfig.DC_PIN  # type: ignore[attr-defined]
+        self.busy_pin = epdconfig.BUSY_PIN  # type: ignore[attr-defined]
+        self.cs_pin = epdconfig.CS_PIN  # type: ignore[attr-defined]
         self.width = EPD_WIDTH
         self.height = EPD_HEIGHT
 
     # Hardware reset
-    def reset(self):
-        epdconfig.digital_write(self.reset_pin, 1)
-        epdconfig.delay_ms(200)
-        epdconfig.digital_write(self.reset_pin, 0)
-        epdconfig.delay_ms(2)
-        epdconfig.digital_write(self.reset_pin, 1)
-        epdconfig.delay_ms(200)
-
-    def send_command(self, command):
-        epdconfig.digital_write(self.dc_pin, 0)
-        epdconfig.digital_write(self.cs_pin, 0)
-        epdconfig.spi_writebyte([command])
-        epdconfig.digital_write(self.cs_pin, 1)
-
-    def send_data(self, data):
-        epdconfig.digital_write(self.dc_pin, 1)
-        epdconfig.digital_write(self.cs_pin, 0)
-        epdconfig.spi_writebyte([data])
-        epdconfig.digital_write(self.cs_pin, 1)
+    def reset(self) -> None:  # noqa: D102
+        epdconfig.digital_write(self.reset_pin, 1)  # type: ignore[attr-defined]
+        epdconfig.delay_ms(200)  # type: ignore[attr-defined]
+        epdconfig.digital_write(self.reset_pin, 0)  # type: ignore[attr-defined]
+        epdconfig.delay_ms(2)  # type: ignore[attr-defined]
+        epdconfig.digital_write(self.reset_pin, 1)  # type: ignore[attr-defined]
+        epdconfig.delay_ms(200)  # type: ignore[attr-defined]
+
+    def send_command(self, command: int) -> None:  # noqa: D102
+        epdconfig.digital_write(self.dc_pin, 0)  # type: ignore[attr-defined]
+        epdconfig.digital_write(self.cs_pin, 0)  # type: ignore[attr-defined]
+        epdconfig.spi_writebyte([command])  # type: ignore[attr-defined]
+        epdconfig.digital_write(self.cs_pin, 1)  # type: ignore[attr-defined]
+
+    def send_data(self, data: int) -> None:  # noqa: D102
+        epdconfig.digital_write(self.dc_pin, 1)  # type: ignore[attr-defined]
+        epdconfig.digital_write(self.cs_pin, 0)  # type: ignore[attr-defined]
+        epdconfig.spi_writebyte([data])  # type: ignore[attr-defined]
+        epdconfig.digital_write(self.cs_pin, 1)  # type: ignore[attr-defined]
 
-    def read_busy(self):
+    def read_busy(self) -> None:  # noqa: D102
         debug("e-Paper busy")
         self.send_command(0x71)
-        busy = epdconfig.digital_read(self.busy_pin)
+        busy = epdconfig.digital_read(self.busy_pin)  # type: ignore[attr-defined]
         while busy == 0:
             self.send_command(0x71)
-            busy = epdconfig.digital_read(self.busy_pin)
-        epdconfig.delay_ms(200)
+            busy = epdconfig.digital_read(self.busy_pin)  # type: ignore[attr-defined]
+        epdconfig.delay_ms(200)  # type: ignore[attr-defined]
 
-    def init(self):
-        if epdconfig.module_init() != 0:
+    def init(self) -> int:  # noqa: D102
+        if epdconfig.module_init() != 0:  # type: ignore[attr-defined]
             return -1
         # EPD hardware init start
         self.reset()
 
         self.send_command(0x01)  # POWER SETTING
         self.send_data(0x07)
         self.send_data(0x07)  # VGH=20V,VGL=-20V
         self.send_data(0x3F)  # VDH=15V
         self.send_data(0x3F)  # VDL=-15V
 
         self.send_command(0x04)  # POWER ON
-        epdconfig.delay_ms(100)
+        epdconfig.delay_ms(100)  # type: ignore[attr-defined]
         self.read_busy()
 
-        self.send_command(0x00)  # PANNEL SETTING
+        self.send_command(0x00)  # PANEL SETTING
         self.send_data(0x1F)  # KW-3f   KWR-2F	BWROTP 0f	BWOTP 1f
 
         self.send_command(0x61)  # tres
         self.send_data(0x03)  # source 800
         self.send_data(0x20)
         self.send_data(0x01)  # gate 480
         self.send_data(0xE0)
@@ -111,21 +115,19 @@
 
         self.send_command(0x60)  # TCON SETTING
         self.send_data(0x22)
 
         # EPD hardware init end
         return 0
 
-    def getbuffer(self, image):
-        # logging.debug("bufsiz = ",int(self.width/8) * self.height)
+    def getbuffer(self, image: Image) -> list[int]:  # noqa: D102
         buf = [0xFF] * (int(self.width / 8) * self.height)
         image_monocolor = image.convert("1")
         imwidth, imheight = image_monocolor.size
-        pixels = image_monocolor.load()
-        # logging.debug("imwidth = %d, imheight = %d",imwidth,imheight)
+        pixels = image_monocolor.load()  # type: ignore[func-returns-value]
         if imwidth == self.width and imheight == self.height:
             debug("Vertical")
             for y in range(imheight):
                 for x in range(imwidth):
                     # Set the bits for the column of pixels at the current position.
                     if pixels[x, y] == 0:
                         buf[int((x + y * self.width) / 8)] &= ~(0x80 >> (x % 8))
@@ -135,39 +137,39 @@
                 for x in range(imwidth):
                     new_x = y
                     new_y = self.height - x - 1
                     if pixels[x, y] == 0:
                         buf[int((new_x + new_y * self.width) / 8)] &= ~(0x80 >> (y % 8))
         return buf
 
-    def display(self, image):
+    def display(self, image: Image) -> None:  # noqa: D102
         self.send_command(0x13)
         for i in range(0, int(self.width * self.height / 8)):
-            self.send_data(~image[i])
+            self.send_data(~image[i])  # type: ignore[index]
 
         self.send_command(0x12)
-        epdconfig.delay_ms(100)
+        epdconfig.delay_ms(100)  # type: ignore[attr-defined]
         self.read_busy()
 
-    def clear(self):
+    def clear(self) -> None:  # noqa: D102
         self.send_command(0x10)
         for _ in range(0, int(self.width * self.height / 8)):
             self.send_data(0x00)
 
         self.send_command(0x13)
         for _ in range(0, int(self.width * self.height / 8)):
             self.send_data(0x00)
 
         self.send_command(0x12)
-        epdconfig.delay_ms(100)
+        epdconfig.delay_ms(100)  # type: ignore[attr-defined]
         self.read_busy()
 
-    def sleep(self):
+    def sleep(self) -> None:  # noqa: D102
         self.send_command(0x02)  # POWER_OFF
         self.read_busy()
 
         self.send_command(0x07)  # DEEP_SLEEP
         self.send_data(0xA5)
 
     @staticmethod
-    def dev_exit():
-        epdconfig.module_exit()
+    def dev_exit() -> None:  # noqa: D102
+        epdconfig.module_exit()  # type: ignore[attr-defined]
```

### Comparing `wg_utilities-2.9.0/wg_utilities/epd/epdconfig.py` & `wg_utilities-3.0.0/wg_utilities/devices/epd/epdconfig.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,8 +1,9 @@
-"""
+"""Config for the EPD.
+
 * | File        :	  epdconfig.py
 * | Author      :   Waveshare team
 * | Function    :   Hardware underlying interface
 * | Info        :
 *----------------
 * | This version:   V1.0
 * | Date        :   2019-06-21
@@ -22,90 +23,95 @@
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS OR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
 """
-# pylint: disable=missing-function-docstring,missing-class-docstring
+from __future__ import annotations
 
+# pylint: disable=missing-function-docstring,missing-class-docstring
 from logging import debug
 from os import path
-from os.path import exists, join, realpath, dirname
 from sys import modules
 from time import sleep
+from typing import Literal
 
 
 # noinspection PyMissingOrEmptyDocstring
-class RaspberryPi:
+class RaspberryPi:  # noqa: D101
     # Pin definition
     RST_PIN = 17
     DC_PIN = 25
     CS_PIN = 8
     BUSY_PIN = 24
 
     # noinspection PyUnresolvedReferences,PyPackageRequirements
     # pylint: disable=import-outside-toplevel
-    def __init__(self):
-        from spidev import SpiDev
+    def __init__(self) -> None:
         from RPi import GPIO
+        from spidev import SpiDev
 
         self.gpio = GPIO
 
         # SPI device, bus = 0, device = 0
         self.spi = SpiDev(0, 0)
 
-    def digital_write(self, pin, value):
+    def digital_write(self, pin: int, value: bool) -> None:  # noqa: D102
         self.gpio.output(pin, value)
 
-    def digital_read(self, pin):
-        return self.gpio.input(pin)
+    def digital_read(self, pin: int) -> bool:  # noqa: D102
+        return self.gpio.input(pin)  # type: ignore[no-any-return]
 
     @staticmethod
-    def delay_ms(delay_time):
+    def delay_ms(delay_time: float | int) -> None:  # noqa: D102
         sleep(delay_time / 1000.0)
 
-    def spi_writebyte(self, data):
+    def spi_writebyte(self, data: list[int]) -> None:  # noqa: D102
         self.spi.writebytes(data)
 
     # noinspection DuplicatedCode
-    def module_init(self):
+    def module_init(self) -> Literal[0]:  # noqa: D102
         self.gpio.setmode(self.gpio.BCM)
         self.gpio.setwarnings(False)
         self.gpio.setup(self.RST_PIN, self.gpio.OUT)
         self.gpio.setup(self.DC_PIN, self.gpio.OUT)
         self.gpio.setup(self.CS_PIN, self.gpio.OUT)
         self.gpio.setup(self.BUSY_PIN, self.gpio.IN)
         self.spi.max_speed_hz = 4000000
         self.spi.mode = 0b00
         return 0
 
-    def module_exit(self):
+    def module_exit(self) -> None:  # noqa: D102
         debug("spi end")
         self.spi.close()
 
         debug("close 5V, Module enters 0 power consumption ...")
         self.gpio.output(self.RST_PIN, 0)
         self.gpio.output(self.DC_PIN, 0)
 
         self.gpio.cleanup()
 
 
-# noinspection PyMissingOrEmptyDocstring
+# This is commented out because I don't have a Jetson Nano and I can't be bothered type
+# hinting it all
+
+# pylint: disable=pointless-string-statement
+"""
 class JetsonNano:
     # Pin definition
     RST_PIN = 17
     DC_PIN = 25
     CS_PIN = 8
     BUSY_PIN = 24
 
     # noinspection PyUnresolvedReferences
-    # pylint: disable=import-outside-toplevel
     def __init__(self):
         from ctypes.cdll import LoadLibrary
+
         from Jetson import GPIO
 
         self.spi = None
 
         for find_dir in [
             dirname(realpath(__file__)),
             "/usr/local/lib",
@@ -150,33 +156,33 @@
         self.spi.SYSFS_software_spi_end()
 
         debug("close 5V, Module enters 0 power consumption ...")
         self.gpio.output(self.RST_PIN, 0)
         self.gpio.output(self.DC_PIN, 0)
 
         self.gpio.cleanup()
-
+"""
 
 try:
     if path.exists("/sys/bus/platform/drivers/gpiomem-bcm2835"):
-        implementation = RaspberryPi()
+        # pylint: disable=used-before-assignment
+        implementation: RaspberryPi | FakeImplementation = RaspberryPi()
     else:
-        implementation = JetsonNano()
+        raise RuntimeError("Unsupported platform (Jetson Nano?)")
 
     for func in dir(implementation):
         if not func.startswith("_"):
             setattr(modules[__name__], func, getattr(implementation, func))
 
     TEST_MODE = False
 except (RuntimeError, ImportError):
-
     # pylint: disable=too-few-public-methods
     class FakeImplementation:
-        """Class to cover functionality of implementations on non-supporting devices"""
+        """Class to cover functionality of implementations on non-supporting devices."""
 
-    for method in set().union(dir(RaspberryPi), dir(JetsonNano)):
+    for method in dir(RaspberryPi):
         if not method.startswith("_"):
             setattr(FakeImplementation, method, lambda *a, **k: None)
 
     implementation = FakeImplementation()
 
     TEST_MODE = True
```

### Comparing `wg_utilities-2.9.0/wg_utilities/functions/file_management.py` & `wg_utilities-3.0.0/wg_utilities/functions/file_management.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,60 +1,67 @@
-"""Functions for specifically managing files and directories"""
+"""Set of functions for specifically managing files and directories."""
 
-from os import getenv
-from os.path import dirname
-from sys import platform
+from __future__ import annotations
+
+from os import environ, getenv
 from pathlib import Path
+from sys import platform
 
 
-def user_data_dir(*, project_name="WgUtilities", file_name=None):
-    """Get OS specific data directory path
+def user_data_dir(
+    *,
+    project_name: str = "WgUtilities",
+    file_name: str | None = None,
+    _platform: str = platform,
+) -> Path:
+    r"""Get OS specific data directory path.
 
     Typical user data directories are:
         macOS:    ~/Library/Application Support
         Unix:     ~/.local/share   # or in $XDG_DATA_HOME, if defined
         Win 10:   C:\\Users\\<username>\\AppData\\Local
 
     For Unix, we follow the XDG spec and support $XDG_DATA_HOME if defined.
 
     Args:
         project_name (str): the name of the project which the utils are running in
-        file_name (str): file to be fetched from the data dir
+        file_name (Optional[str]): file to be fetched from the data dir
+        _platform (str): the platform to get the data dir for
 
     Returns:
         str: full path to the user-specific data dir
     """
 
     # get os specific path
-    if platform.startswith("win"):
-        os_path = getenv("LOCALAPPDATA")
-    elif platform.startswith("darwin"):
+    if _platform.startswith("win"):
+        os_path = environ["LOCALAPPDATA"]
+    elif _platform.startswith("darwin"):
         os_path = "~/Library/Application Support"
     else:
         # linux
         os_path = getenv("XDG_DATA_HOME", "~/.local/share")
 
     path = Path(os_path) / project_name
 
     if file_name:
-        return path.expanduser() / file_name
+        return force_mkdir(path.expanduser() / file_name, path_is_file=True)
 
     return path.expanduser()
 
 
-def force_mkdir(target_path, path_is_file=False):
-    """Creates all directories needed for the given path
+def force_mkdir(target_path: Path, path_is_file: bool = False) -> Path:
+    """Create all directories needed for the given path.
 
     Args:
         target_path (str): the path to the directory which needs to be created
         path_is_file (bool): flag for whether the path is for a file, in which case
          the final part of the path will not be created
 
     Returns:
         str: directory_path that was passed in
     """
     if path_is_file:
-        Path(dirname(target_path)).mkdir(exist_ok=True, parents=True)
+        target_path.parent.mkdir(exist_ok=True, parents=True)
     else:
-        Path(target_path).mkdir(exist_ok=True, parents=True)
+        target_path.mkdir(exist_ok=True, parents=True)
 
     return target_path
```

### Comparing `wg_utilities-2.9.0/wg_utilities/functions/processes.py` & `wg_utilities-3.0.0/wg_utilities/functions/processes.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,44 +1,48 @@
-"""Functions for managing processes"""
+"""Set of functions for managing processes."""
 
-from logging import getLogger, DEBUG
-from re import compile as compile_regex
-from subprocess import Popen, PIPE
+from __future__ import annotations
 
-from wg_utilities.loggers import add_stream_handler
+from logging import DEBUG, getLogger
+from re import compile as compile_regex
+from subprocess import PIPE, Popen
 
 LOGGER = getLogger(__name__)
 LOGGER.setLevel(DEBUG)
-add_stream_handler(LOGGER)
 
 COMMAND_PATTERN = compile_regex(r"""((?:[^\s"']|"[^"]*"|'[^']*')+)""")
 
 
-def run_cmd(cmd, exit_on_error=True):
-    """Helper function for running commands on the command line
+def run_cmd(
+    cmd: str, exit_on_error: bool = True, shell: bool = False
+) -> tuple[str, str]:
+    """Run commands on the command line.
 
     Args:
         cmd (str): the command to run in the user's terminal
         exit_on_error (bool): flag for if the script should exit if the command errored
+        shell (bool): flag for running command in shell
 
     Returns:
         str: the output of the command
         str: the error from the command, if it errored
 
     Raises:
         RuntimeError: if the command has a non-zero exit code
     """
 
     LOGGER.debug("Running command `%s`", cmd)
 
-    with Popen(COMMAND_PATTERN.split(cmd)[1::2], stdout=PIPE, stderr=PIPE) as process:
+    popen_input = cmd if shell else COMMAND_PATTERN.split(cmd)[1::2]
+
+    with Popen(popen_input, stdout=PIPE, stderr=PIPE, shell=shell) as process:
         output, error = process.communicate()
 
-        error = error.decode("utf-8").strip()
+        error_str = error.decode("utf-8").strip()
 
         if process.returncode != 0:
             if exit_on_error:
-                raise RuntimeError(error)
+                raise RuntimeError(error_str)
 
-            LOGGER.error(error)
+            LOGGER.error(error_str)  # pragma: no cover
 
-    return output.decode("utf-8").strip(), error
+    return output.decode("utf-8").strip(), error_str
```

