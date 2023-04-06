# Comparing `tmp/pyeasee-0.7.50.tar.gz` & `tmp/pyeasee-0.7.51.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyeasee-0.7.50.tar", last modified: Sun Dec 18 22:40:46 2022, max compression
+gzip compressed data, was "pyeasee-0.7.51.tar", last modified: Thu Apr  6 21:35:25 2023, max compression
```

## Comparing `pyeasee-0.7.50.tar` & `pyeasee-0.7.51.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxrwxr-x   0 olal      (1000) olal      (1000)        0 2022-12-18 22:40:46.712321 pyeasee-0.7.50/
--rw-rw-r--   0 olal      (1000) olal      (1000)     3319 2022-12-18 22:40:46.716321 pyeasee-0.7.50/PKG-INFO
--rw-rw-r--   0 olal      (1000) olal      (1000)     2299 2022-10-12 21:10:32.000000 pyeasee-0.7.50/README.md
-drwxrwxr-x   0 olal      (1000) olal      (1000)        0 2022-12-18 22:40:46.712321 pyeasee-0.7.50/pyeasee/
--rw-rw-r--   0 olal      (1000) olal      (1000)      185 2022-12-18 22:29:13.000000 pyeasee-0.7.50/pyeasee/__init__.py
--rw-rw-r--   0 olal      (1000) olal      (1000)    13282 2022-12-18 22:29:13.000000 pyeasee-0.7.50/pyeasee/__main__.py
--rw-rw-r--   0 olal      (1000) olal      (1000)    18410 2022-12-18 22:38:53.000000 pyeasee-0.7.50/pyeasee/charger.py
--rw-rw-r--   0 olal      (1000) olal      (1000)     6919 2022-12-18 22:24:07.000000 pyeasee-0.7.50/pyeasee/const.py
--rw-rw-r--   0 olal      (1000) olal      (1000)    16669 2022-12-18 22:39:23.000000 pyeasee-0.7.50/pyeasee/easee.py
--rw-rw-r--   0 olal      (1000) olal      (1000)      776 2022-12-17 23:49:14.000000 pyeasee-0.7.50/pyeasee/exceptions.py
--rw-rw-r--   0 olal      (1000) olal      (1000)     7536 2022-12-18 22:29:13.000000 pyeasee-0.7.50/pyeasee/site.py
--rw-rw-r--   0 olal      (1000) olal      (1000)     2130 2022-12-18 22:29:13.000000 pyeasee-0.7.50/pyeasee/utils.py
-drwxrwxr-x   0 olal      (1000) olal      (1000)        0 2022-12-18 22:40:46.712321 pyeasee-0.7.50/pyeasee.egg-info/
--rw-rw-r--   0 olal      (1000) olal      (1000)     3319 2022-12-18 22:40:46.000000 pyeasee-0.7.50/pyeasee.egg-info/PKG-INFO
--rw-rw-r--   0 olal      (1000) olal      (1000)      364 2022-12-18 22:40:46.000000 pyeasee-0.7.50/pyeasee.egg-info/SOURCES.txt
--rw-rw-r--   0 olal      (1000) olal      (1000)        1 2022-12-18 22:40:46.000000 pyeasee-0.7.50/pyeasee.egg-info/dependency_links.txt
--rw-rw-r--   0 olal      (1000) olal      (1000)       51 2022-12-18 22:40:46.000000 pyeasee-0.7.50/pyeasee.egg-info/entry_points.txt
--rw-rw-r--   0 olal      (1000) olal      (1000)       27 2022-12-18 22:40:46.000000 pyeasee-0.7.50/pyeasee.egg-info/requires.txt
--rw-rw-r--   0 olal      (1000) olal      (1000)        8 2022-12-18 22:40:46.000000 pyeasee-0.7.50/pyeasee.egg-info/top_level.txt
--rw-rw-r--   0 olal      (1000) olal      (1000)      169 2022-12-18 22:40:46.716321 pyeasee-0.7.50/setup.cfg
--rw-rw-r--   0 olal      (1000) olal      (1000)      805 2022-12-18 22:39:23.000000 pyeasee-0.7.50/setup.py
+drwxrwxr-x   0 olal      (1000) olal      (1000)        0 2023-04-06 21:35:25.435674 pyeasee-0.7.51/
+-rw-rw-r--   0 olal      (1000) olal      (1000)     3319 2023-04-06 21:35:25.435674 pyeasee-0.7.51/PKG-INFO
+-rw-rw-r--   0 olal      (1000) olal      (1000)     2299 2022-10-12 21:10:32.000000 pyeasee-0.7.51/README.md
+drwxrwxr-x   0 olal      (1000) olal      (1000)        0 2023-04-06 21:35:25.431674 pyeasee-0.7.51/pyeasee/
+-rw-rw-r--   0 olal      (1000) olal      (1000)      185 2022-12-18 22:29:13.000000 pyeasee-0.7.51/pyeasee/__init__.py
+-rw-rw-r--   0 olal      (1000) olal      (1000)    13505 2023-04-06 21:27:23.000000 pyeasee-0.7.51/pyeasee/__main__.py
+-rw-rw-r--   0 olal      (1000) olal      (1000)    19443 2023-04-06 21:27:23.000000 pyeasee-0.7.51/pyeasee/charger.py
+-rw-rw-r--   0 olal      (1000) olal      (1000)    29599 2023-04-06 21:27:23.000000 pyeasee-0.7.51/pyeasee/const.py
+-rw-rw-r--   0 olal      (1000) olal      (1000)    16783 2023-04-06 21:28:11.000000 pyeasee-0.7.51/pyeasee/easee.py
+-rw-rw-r--   0 olal      (1000) olal      (1000)      776 2022-12-17 23:49:14.000000 pyeasee-0.7.51/pyeasee/exceptions.py
+-rw-rw-r--   0 olal      (1000) olal      (1000)     8707 2023-04-06 21:27:23.000000 pyeasee-0.7.51/pyeasee/site.py
+-rw-rw-r--   0 olal      (1000) olal      (1000)     2130 2022-12-18 22:29:13.000000 pyeasee-0.7.51/pyeasee/utils.py
+drwxrwxr-x   0 olal      (1000) olal      (1000)        0 2023-04-06 21:35:25.435674 pyeasee-0.7.51/pyeasee.egg-info/
+-rw-rw-r--   0 olal      (1000) olal      (1000)     3319 2023-04-06 21:35:24.000000 pyeasee-0.7.51/pyeasee.egg-info/PKG-INFO
+-rw-rw-r--   0 olal      (1000) olal      (1000)      364 2023-04-06 21:35:24.000000 pyeasee-0.7.51/pyeasee.egg-info/SOURCES.txt
+-rw-rw-r--   0 olal      (1000) olal      (1000)        1 2023-04-06 21:35:24.000000 pyeasee-0.7.51/pyeasee.egg-info/dependency_links.txt
+-rw-rw-r--   0 olal      (1000) olal      (1000)       51 2023-04-06 21:35:24.000000 pyeasee-0.7.51/pyeasee.egg-info/entry_points.txt
+-rw-rw-r--   0 olal      (1000) olal      (1000)       27 2023-04-06 21:35:24.000000 pyeasee-0.7.51/pyeasee.egg-info/requires.txt
+-rw-rw-r--   0 olal      (1000) olal      (1000)        8 2023-04-06 21:35:24.000000 pyeasee-0.7.51/pyeasee.egg-info/top_level.txt
+-rw-rw-r--   0 olal      (1000) olal      (1000)      169 2023-04-06 21:35:25.435674 pyeasee-0.7.51/setup.cfg
+-rw-rw-r--   0 olal      (1000) olal      (1000)      805 2023-04-06 21:28:11.000000 pyeasee-0.7.51/setup.py
```

### Comparing `pyeasee-0.7.50/PKG-INFO` & `pyeasee-0.7.51/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyeasee
-Version: 0.7.50
+Version: 0.7.51
 Summary: Easee EV charger API library
 Home-page: https://github.com/fondberg/pyeasee
 Author: Niklas Fondberg
 Author-email: niklas.fondberg@gmail.com
 License: MIT
 Description: ![Maintenance](https://img.shields.io/maintenance/yes/2022.svg) ![Easee library](https://github.com/fondberg/easee/workflows/Easee%20library/badge.svg)
```

### Comparing `pyeasee-0.7.50/README.md` & `pyeasee-0.7.51/README.md`

 * *Files identical despite different names*

### Comparing `pyeasee-0.7.50/pyeasee/__main__.py` & `pyeasee-0.7.51/pyeasee/__main__.py`

 * *Files 0% similar despite different names*

```diff
@@ -98,15 +98,15 @@
     _LOGGER.debug("args: %s", args)
     easee = Easee(args.username, args.password)
     if args.chargers:
         chargers: List[Charger] = await easee.get_chargers()
         await chargers_info(chargers)
 
     if args.sites:
-        sites: List[Site] = await easee.get_sites()
+        sites: List[Site] = await easee.get_account_products()
         await sites_info(sites)
 
     if args.circuits:
         sites: List[Site] = await easee.get_sites()
         for site in sites:
             await circuits_info(circuits=site.get_circuits())
 
@@ -245,17 +245,21 @@
     print("\n\n****************\nCHARGERS\n****************")
     data = []
     for charger in chargers:
         state = await charger.get_state()
         config = await charger.get_config()
         schedule = await charger.get_basic_charge_plan()
         week_schedule = await charger.get_weekly_charge_plan()
+        observation_test = await charger.get_observations(30, 31, 35, 36, 45)
+        firmware = await charger.get_latest_firmware()
         ch = charger.get_data()
         ch["state"] = state.get_data()
         ch["config"] = config.get_data()
+        ch["firmware"] = firmware
+        ch["observation"] = observation_test
         if schedule is not None:
             ch["schedule"] = schedule.get_data()
         if week_schedule is not None:
             ch["week_schedule"] = week_schedule.get_data()
         data.append(ch)
 
     print(json.dumps(data, indent=2))
```

### Comparing `pyeasee-0.7.50/pyeasee/charger.py` & `pyeasee-0.7.51/pyeasee/charger.py`

 * *Files 2% similar despite different names*

```diff
@@ -186,14 +186,22 @@
         super().__init__(entries)
         self.id: str = entries["id"]
         self.name: str = entries["name"]
         self.site = site
         self.circuit = circuit
         self.easee = easee
 
+    async def get_observations(self, *args):
+        """Gets observation IDs"""
+        observation_ids = ",".join(str(s) for s in args)
+        try:
+            return await (await self.easee.get(f"/state/{self.id}/observations?ids={observation_ids}", base=1)).json()
+        except (ServerFailureException):
+            return None
+
     async def get_consumption_between_dates(self, from_date: datetime, to_date):
         """Gets consumption between two dates"""
         try:
             value = await (
                 await self.easee.get(
                     f"/api/sessions/charger/{self.id}/total/{from_date.isoformat()}/{to_date.isoformat()}"
                 )
@@ -228,14 +236,27 @@
         """get state for charger"""
         try:
             state = await (await self.easee.get(f"/api/chargers/{self.id}/state")).json()
             return ChargerState(state, raw)
         except (ServerFailureException):
             return None
 
+    async def empty_config(self, raw=False) -> ChargerConfig:
+        """Create an empty config data structure"""
+        config = {}
+        return ChargerConfig(config, raw)
+
+    async def empty_state(self, raw=False) -> ChargerConfig:
+        """Create an empty config data structure"""
+        state = {
+            "chargerOpMode": 0,
+            "reasonForNoCurrent": 0,
+        }
+        return ChargerState(state, raw)
+
     async def start(self):
         """Start charging session"""
         try:
             return await self.easee.post(f"/api/chargers/{self.id}/commands/start_charging")
         except (ServerFailureException):
             return None
 
@@ -411,14 +432,21 @@
     async def update_firmware(self):
         """Update charger firmware"""
         try:
             return await self.easee.post(f"/api/chargers/{self.id}/commands/update_firmware")
         except (ServerFailureException):
             return None
 
+    async def get_latest_firmware(self):
+        """Get the latest released firmeware version"""
+        try:
+            return await (await self.easee.get(f"/firmware/{self.id}/latest", base=1)).json()
+        except (ServerFailureException):
+            return None
+
     async def set_dynamic_charger_circuit_current(
         self, currentP1: int, currentP2: int = None, currentP3: int = None, timeToLive: int = 0
     ):
         """Set dynamic current on circuit level. timeToLive specifies, in minutes, for how long the new dynamic current is valid. timeToLive = 0 means that the new dynamic current is valid until changed the next time. The dynamic current is always reset to default when the charger is restarted."""
         if self.circuit is not None:
             return await self.circuit.set_dynamic_current(currentP1, currentP2, currentP3, timeToLive)
         else:
```

### Comparing `pyeasee-0.7.50/pyeasee/easee.py` & `pyeasee-0.7.51/pyeasee/easee.py`

 * *Files 2% similar despite different names*

```diff
@@ -18,15 +18,15 @@
     NotFoundException,
     ServerFailureException,
     TooManyRequestsException,
 )
 from .site import Site, SiteState
 from .utils import convert_stream_data
 
-__VERSION__ = "0.7.50"
+__VERSION__ = "0.7.51"
 
 _LOGGER = logging.getLogger(__name__)
 
 SR_MIN_BACKOFF = 0
 SR_MAX_BACKOFF = 300
 SR_INC_BACKOFF = 30
 
@@ -77,15 +77,15 @@
     def __init__(self, username, password, session: aiohttp.ClientSession = None):
         self.username = username
         self.password = password
         self.external_session = True if session else False
 
         _LOGGER.info("Easee python library version: %s", __VERSION__)
 
-        self.base = "https://api.easee.cloud"
+        self.base = ["https://api.easee.cloud", "https://api.easee.com"]
         self.sr_base = "https://api.easee.cloud/hubs/chargers"
         self.token = {}
         self.headers = {
             "User-Agent": f"pyeasee/{__VERSION__} REST client",
             "Accept": "application/json",
             "Content-Type": "application/json;charset=UTF-8",
         }
@@ -105,41 +105,41 @@
         self.sr_connected = False
         self.sr_connect_in_progress = False
         self.running_loop = None
         self.event_loop = None
         self._sr_backoff = SR_MIN_BACKOFF
 
     def base_uri(self):
-        return self.base
+        return self.base[0]
 
-    async def post(self, url, **kwargs):
+    async def post(self, url, base=0, **kwargs):
         _LOGGER.debug("POST: %s (%s)", url, kwargs)
         await self._verify_updated_token()
-        response = await self.session.post(f"{self.base}{url}", headers=self.headers, **kwargs)
+        response = await self.session.post(f"{self.base[base]}{url}", headers=self.headers, **kwargs)
         await self.check_status(response)
         return response
 
-    async def put(self, url, **kwargs):
+    async def put(self, url, base=0, **kwargs):
         _LOGGER.debug("PUT: %s (%s)", url, kwargs)
         await self._verify_updated_token()
-        response = await self.session.put(f"{self.base}{url}", headers=self.headers, **kwargs)
+        response = await self.session.put(f"{self.base[base]}{url}", headers=self.headers, **kwargs)
         await self.check_status(response)
         return response
 
-    async def get(self, url, **kwargs):
+    async def get(self, url, base=0, **kwargs):
         _LOGGER.debug("GET: %s (%s)", url, kwargs)
         await self._verify_updated_token()
-        response = await self.session.get(f"{self.base}{url}", headers=self.headers, **kwargs)
+        response = await self.session.get(f"{self.base[base]}{url}", headers=self.headers, **kwargs)
         await self.check_status(response)
         return response
 
-    async def delete(self, url, **kwargs):
+    async def delete(self, url, base=0, **kwargs):
         _LOGGER.debug("DELETE: %s (%s)", url, kwargs)
         await self._verify_updated_token()
-        response = await self.session.delete(f"{self.base}{url}", headers=self.headers, **kwargs)
+        response = await self.session.delete(f"{self.base[base]}{url}", headers=self.headers, **kwargs)
         await self.check_status(response)
         return response
 
     # TODO: Quick fix for the auth fail errors due to something wrong with refresh token logic
     async def check_status(self, response):
         try:
             await raise_for_status(response)
@@ -183,30 +183,32 @@
 
     async def connect(self):
         """
         Connect and gets initial token
         """
         data = {"userName": self.username, "password": self.password}
         _LOGGER.debug("getting token for user: %s", self.username)
-        response = await self.session.post(f"{self.base}/api/accounts/login", headers=self.minimal_headers, json=data)
+        response = await self.session.post(
+            f"{self.base[0]}/api/accounts/login", headers=self.minimal_headers, json=data
+        )
         await raise_for_status(response)
         await self._handle_token_response(response)
 
     async def _refresh_token(self):
         """
         Refresh token
         """
         data = {
             "accessToken": self.token["accessToken"],
             "refreshToken": self.token["refreshToken"],
         }
         _LOGGER.debug("Refreshing access token")
         try:
             res = await self.session.post(
-                f"{self.base}/api/accounts/refresh_token", headers=self.minimal_headers, json=data
+                f"{self.base[0]}/api/accounts/refresh_token", headers=self.minimal_headers, json=data
             )
             await self._handle_token_response(res)
         except (AuthorizationFailedException, BadRequestException):
             _LOGGER.debug("Could not get new access token from refresh token, getting new one")
             await self.connect()
 
     async def close(self):
```

### Comparing `pyeasee-0.7.50/pyeasee/exceptions.py` & `pyeasee-0.7.51/pyeasee/exceptions.py`

 * *Files identical despite different names*

### Comparing `pyeasee-0.7.50/pyeasee/site.py` & `pyeasee-0.7.51/pyeasee/site.py`

 * *Files 5% similar despite different names*

```diff
@@ -25,14 +25,22 @@
     def __init__(self, data: Dict[str, Any], site: Any, easee: Any):
         super().__init__(data)
         self.id: str = data["id"]
         self.name: str = data["name"]
         self.site = site
         self.easee = easee
 
+    async def get_observations(self, *args):
+        """Gets observation IDs"""
+        observation_ids = ",".join(str(s) for s in args)
+        try:
+            return await (await self.easee.get(f"/state/{self.id}/observations?ids={observation_ids}", base=1)).json()
+        except (ServerFailureException):
+            return None
+
     async def get_state(self):
         """Get Equalizer state"""
         try:
             state = await (await self.easee.get(f"/api/equalizers/{self.id}/state")).json()
             return EqualizerState(state)
         except (ServerFailureException):
             return None
@@ -41,14 +49,31 @@
         """Get Equalizer config"""
         try:
             config = await (await self.easee.get(f"/api/equalizers/{self.id}/config")).json()
             return EqualizerConfig(config)
         except (ServerFailureException):
             return None
 
+    async def empty_state(self, raw=False):
+        """Create an empty state data structyre"""
+        state = {}
+        return EqualizerState(state)
+
+    async def empty_config(self, raw=False):
+        """Crate an empty config data structure"""
+        config = {}
+        return EqualizerConfig(config)
+
+    async def get_latest_firmware(self):
+        """Get the latest released firmeware version"""
+        try:
+            return await (await self.easee.get(f"/firmware/{self.id}/latest", base=1)).json()
+        except (ServerFailureException):
+            return None
+
 
 class Circuit(BaseDict):
     """Represents a Circuit"""
 
     def __init__(self, data: Dict[str, Any], site: Any, easee: Any):
         super().__init__(data)
         self.id: int = data["id"]
@@ -152,15 +177,17 @@
         """Set name for the site"""
         json = {**self.get_data(), "name": name}
         return await self.easee.put(f"/api/sites/{self.id}", json=json)
 
     async def set_currency(self, currency: str):
         """Set currency for the site"""
         json = {**self.get_data(), "currencyId": currency}
-        return await self.easee.put(f"/api/sites/{self.id}", json=json)
+        val = await self.easee.put(f"/api/sites/{self.id}", json=json)
+        self["currencyId"] = currency
+        return val
 
     async def set_price(
         self,
         costPerKWh: float,
         vat: float = None,
         currency: str = None,
         costPerKwhExcludeVat: float = None,
@@ -182,15 +209,20 @@
             "currencyId": currency,
             "costPerKWh": costPerKWh,
             "vat": vat,
             "costPerKwhExcludeVat": costPerKwhExcludeVat,
         }
 
         try:
-            return await self.easee.post(f"/api/sites/{self.id}/price", json=json)
+            val = await self.easee.post(f"/api/sites/{self.id}/price", json=json)
+            self["vat"] = vat
+            self["currencyId"] = currency
+            self["costPerKWh"] = costPerKWh
+            self["costPerKwhExcludeVat"] = costPerKwhExcludeVat
+            return val
         except (ServerFailureException):
             return None
 
     async def get_cost_between_dates(self, from_date: datetime, to_date: datetime):
         """Get the charging cost between from_datetime and to_datetime"""
 
         try:
```

### Comparing `pyeasee-0.7.50/pyeasee/utils.py` & `pyeasee-0.7.51/pyeasee/utils.py`

 * *Files identical despite different names*

### Comparing `pyeasee-0.7.50/pyeasee.egg-info/PKG-INFO` & `pyeasee-0.7.51/pyeasee.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyeasee
-Version: 0.7.50
+Version: 0.7.51
 Summary: Easee EV charger API library
 Home-page: https://github.com/fondberg/pyeasee
 Author: Niklas Fondberg
 Author-email: niklas.fondberg@gmail.com
 License: MIT
 Description: ![Maintenance](https://img.shields.io/maintenance/yes/2022.svg) ![Easee library](https://github.com/fondberg/easee/workflows/Easee%20library/badge.svg)
```

### Comparing `pyeasee-0.7.50/setup.py` & `pyeasee-0.7.51/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 import os.path
 from setuptools import setup
 
 # This call to setup() does all the work
 setup(
     name="pyeasee",
-    version="0.7.50",
+    version="0.7.51",
     description="Easee EV charger API library",
     long_description=open("README.md").read(),
     long_description_content_type="text/markdown",
     url="https://github.com/fondberg/pyeasee",
     author="Niklas Fondberg",
     author_email="niklas.fondberg@gmail.com",
     license="MIT",
```

