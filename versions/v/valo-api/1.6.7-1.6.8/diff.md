# Comparing `tmp/valo_api-1.6.7.tar.gz` & `tmp/valo_api-1.6.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "valo_api-1.6.7.tar", max compression
+gzip compressed data, was "valo_api-1.6.8.tar", max compression
```

## Comparing `valo_api-1.6.7.tar` & `valo_api-1.6.8.tar`

### file list

```diff
@@ -1,45 +1,45 @@
--rw-r--r--   0        0        0     1074 2023-04-05 13:42:59.902720 valo_api-1.6.7/LICENSE
--rw-r--r--   0        0        0     2451 2023-04-05 13:42:59.902720 valo_api-1.6.7/README.md
--rw-r--r--   0        0        0     3135 2023-04-05 13:42:59.906720 valo_api-1.6.7/pyproject.toml
--rw-r--r--   0        0        0      388 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/__init__.py
--rw-r--r--   0        0        0      793 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/config.py
--rw-r--r--   0        0        0     6793 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/endpoints/__init__.py
--rw-r--r--   0        0        0     8990 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/endpoints/account_details.py
--rw-r--r--   0        0        0     3369 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/endpoints/content.py
--rw-r--r--   0        0        0     3508 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/endpoints/crosshair.py
--rw-r--r--   0        0        0    11005 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/endpoints/leaderboard.py
--rw-r--r--   0        0        0     3787 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/endpoints/match_details.py
--rw-r--r--   0        0        0    13292 2023-04-05 13:43:00.078721 valo_api-1.6.7/valo_api/endpoints/match_history.py
--rw-r--r--   0        0        0    17609 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/mmr_details.py
--rw-r--r--   0        0        0     9551 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/mmr_history.py
--rw-r--r--   0        0        0     8985 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/raw.py
--rw-r--r--   0        0        0     3961 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/status.py
--rw-r--r--   0        0        0     4828 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/store_featured.py
--rw-r--r--   0        0        0     4659 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/store_offers.py
--rw-r--r--   0        0        0     3578 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/version_info.py
--rw-r--r--   0        0        0     3782 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints/website.py
--rw-r--r--   0        0        0     1185 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/endpoints_config.py
--rw-r--r--   0        0        0        0 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/exceptions/__init__.py
--rw-r--r--   0        0        0     1088 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/exceptions/rate_limit.py
--rw-r--r--   0        0        0     2069 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/exceptions/valo_api_exception.py
--rw-r--r--   0        0        0        0 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/__init__.py
--rw-r--r--   0        0        0      410 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/account_details.py
--rw-r--r--   0        0        0      541 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/competitive_updates_raw.py
--rw-r--r--   0        0        0      858 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/content.py
--rw-r--r--   0        0        0      371 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/error_response.py
--rw-r--r--   0        0        0      917 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/leaderboard.py
--rw-r--r--   0        0        0     5550 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/match_details_raw.py
--rw-r--r--   0        0        0     5996 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/match_history.py
--rw-r--r--   0        0        0      299 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/match_history_raw.py
--rw-r--r--   0        0        0     1317 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/mmr_details.py
--rw-r--r--   0        0        0      241 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/mmr_history.py
--rw-r--r--   0        0        0     1306 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/mmr_raw.py
--rw-r--r--   0        0        0      817 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/status.py
--rw-r--r--   0        0        0     1093 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/store_featured.py
--rw-r--r--   0        0        0      853 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/store_offers.py
--rw-r--r--   0        0        0      157 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/version_info.py
--rw-r--r--   0        0        0      236 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/responses/website.py
--rw-r--r--   0        0        0        0 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/utils/__init__.py
--rw-r--r--   0        0        0      216 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/utils/dict_struct.py
--rw-r--r--   0        0        0     3821 2023-04-05 13:43:00.082721 valo_api-1.6.7/valo_api/utils/fetch_endpoint.py
--rw-r--r--   0        0        0     3838 1970-01-01 00:00:00.000000 valo_api-1.6.7/PKG-INFO
+-rw-r--r--   0        0        0     1074 2023-04-06 20:59:56.331739 valo_api-1.6.8/LICENSE
+-rw-r--r--   0        0        0     2451 2023-04-06 20:59:56.331739 valo_api-1.6.8/README.md
+-rw-r--r--   0        0        0     3135 2023-04-06 20:59:56.335739 valo_api-1.6.8/pyproject.toml
+-rw-r--r--   0        0        0      388 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/__init__.py
+-rw-r--r--   0        0        0      793 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/config.py
+-rw-r--r--   0        0        0     6793 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/__init__.py
+-rw-r--r--   0        0        0     8990 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/account_details.py
+-rw-r--r--   0        0        0     3369 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/content.py
+-rw-r--r--   0        0        0     3508 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/crosshair.py
+-rw-r--r--   0        0        0    11005 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/leaderboard.py
+-rw-r--r--   0        0        0     3787 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/match_details.py
+-rw-r--r--   0        0        0    14140 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/match_history.py
+-rw-r--r--   0        0        0    17609 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/mmr_details.py
+-rw-r--r--   0        0        0     9551 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/mmr_history.py
+-rw-r--r--   0        0        0     8985 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/raw.py
+-rw-r--r--   0        0        0     3961 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/status.py
+-rw-r--r--   0        0        0     4828 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/store_featured.py
+-rw-r--r--   0        0        0     4659 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/store_offers.py
+-rw-r--r--   0        0        0     3578 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/version_info.py
+-rw-r--r--   0        0        0     3782 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints/website.py
+-rw-r--r--   0        0        0     1185 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/endpoints_config.py
+-rw-r--r--   0        0        0        0 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/exceptions/__init__.py
+-rw-r--r--   0        0        0     1088 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/exceptions/rate_limit.py
+-rw-r--r--   0        0        0     2069 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/exceptions/valo_api_exception.py
+-rw-r--r--   0        0        0        0 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/__init__.py
+-rw-r--r--   0        0        0      410 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/account_details.py
+-rw-r--r--   0        0        0      541 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/competitive_updates_raw.py
+-rw-r--r--   0        0        0      858 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/content.py
+-rw-r--r--   0        0        0      371 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/error_response.py
+-rw-r--r--   0        0        0      917 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/leaderboard.py
+-rw-r--r--   0        0        0     5550 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/match_details_raw.py
+-rw-r--r--   0        0        0     5996 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/match_history.py
+-rw-r--r--   0        0        0      299 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/match_history_raw.py
+-rw-r--r--   0        0        0     1317 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/mmr_details.py
+-rw-r--r--   0        0        0      628 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/mmr_history.py
+-rw-r--r--   0        0        0     1306 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/mmr_raw.py
+-rw-r--r--   0        0        0      817 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/status.py
+-rw-r--r--   0        0        0     1093 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/store_featured.py
+-rw-r--r--   0        0        0      853 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/store_offers.py
+-rw-r--r--   0        0        0      157 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/version_info.py
+-rw-r--r--   0        0        0      236 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/responses/website.py
+-rw-r--r--   0        0        0        0 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/utils/__init__.py
+-rw-r--r--   0        0        0      216 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/utils/dict_struct.py
+-rw-r--r--   0        0        0     3821 2023-04-06 20:59:56.467741 valo_api-1.6.8/valo_api/utils/fetch_endpoint.py
+-rw-r--r--   0        0        0     3838 1970-01-01 00:00:00.000000 valo_api-1.6.8/PKG-INFO
```

### Comparing `valo_api-1.6.7/LICENSE` & `valo_api-1.6.8/LICENSE`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/README.md` & `valo_api-1.6.8/README.md`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/pyproject.toml` & `valo_api-1.6.8/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry_core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "valo_api"
-version = "1.6.7"
+version = "1.6.8"
 description = "Valorant API Wrapper for https://github.com/Henrik-3/unofficial-valorant-api"
 readme = "README.md"
 authors = ["Manuel Raimann <raimannma@outlook.de>"]
 license = "MIT"
 repository = "https://github.com/raimannma/ValorantAPI"
 homepage = "https://github.com/raimannma/ValorantAPI"
 
@@ -27,24 +27,24 @@
 [tool.poetry.scripts]
 "valo_api" = "valo_api.__main__:app"
 
 [tool.poetry.dependencies]
 python = "^3.8"
 requests = "^2.28.1"
 Pillow = "^9.2.0"
-msgspec = ">=0.12,<0.14"
+msgspec = ">=0.12,<0.15"
 asyncio = {version = "^3.4.3", optional = true, extras = ["speedups"]}
 aiohttp = {version = "^3.8.3", optional = true}
 
 [tool.poetry.group.dev.dependencies]
 bandit = "^1.7.5"
 black = {version = "^23.1.0", allow-prereleases = true}
 darglint = "^1.8.1"
 isort = "^5.12.0"
-mypy = ">=0.991,<1.2"
+mypy = ">=0.991,<1.3"
 mypy-extensions = ">=0.4.3,<1.1.0"
 pre-commit = "^3.2.0"
 pydocstyle = "^6.3.0"
 pylint = "^2.17.0"
 pytest = "^7.2.2"
 hypothesis = "^6.61.0"
 pyupgrade = "^3.3.1"
```

### Comparing `valo_api-1.6.7/valo_api/config.py` & `valo_api-1.6.8/valo_api/config.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/__init__.py` & `valo_api-1.6.8/valo_api/endpoints/__init__.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/account_details.py` & `valo_api-1.6.8/valo_api/endpoints/account_details.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/content.py` & `valo_api-1.6.8/valo_api/endpoints/content.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/crosshair.py` & `valo_api-1.6.8/valo_api/endpoints/crosshair.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/leaderboard.py` & `valo_api-1.6.8/valo_api/endpoints/leaderboard.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/match_details.py` & `valo_api-1.6.8/valo_api/endpoints/match_details.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/match_history.py` & `valo_api-1.6.8/valo_api/endpoints/match_history.py`

 * *Files 7% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 
 
 def get_match_history_by_name_v3(
     region: str,
     name: str,
     tag: str,
     size: Optional[int] = None,
+    map: Optional[str] = None,
     game_mode: Optional[str] = None,
     **kwargs,
 ) -> List[MatchHistoryPointV3]:
     """Get the match history for a player by name and tag using version 3 of the endpoint.
 
     This is the same as :py:meth:`get_match_history_by_name(version="v3", region=region, name=name, tag=tag,
     size=size, game_mode=game_mode, **kwargs) <get_match_history_by_name>`
@@ -27,56 +28,64 @@
     Args:
         region: The region of the player.
             One of the following:
             eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
         name: The name of the player.
         tag: The tag of the player.
         size: The number of matches to return. Maximum is 10.
+        map: The map to filter by.
         game_mode: The game mode to filter by.
         **kwargs: Any additional arguments to pass to the endpoint.
 
     Returns:
         A list of :class:`.MatchHistoryPointV3` objects.
     """
-    return get_match_history_by_name("v3", region, name, tag, size, game_mode, **kwargs)
+    return get_match_history_by_name(
+        "v3", region, name, tag, size, map, game_mode, **kwargs
+    )
 
 
 def get_match_history_by_puuid_v3(
     region: str,
     puuid: str,
     size: Optional[int] = None,
+    map: Optional[str] = None,
     game_mode: Optional[str] = None,
     **kwargs,
 ) -> List[MatchHistoryPointV3]:
     """Get the match history for a player by puuid using version 3 of the endpoint.
 
     This is the same as :py:meth:`get_match_history_by_puuid(version="v3", region=region, puuid=puuid, size=size,
     game_mode=game_mode, **kwargs) <get_match_history_by_puuid>`
 
     Args:
         region: The region of the player.
             One of the following:
             eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
         puuid: The puuid of the player.
         size: The number of matches to return. Maximum is 10.
+        map: The map to filter by.
         game_mode: The game mode to filter by.
         **kwargs: Any additional arguments to pass to the endpoint.
 
     Returns:
         A list of :class:`.MatchHistoryPointV3` objects.
     """
-    return get_match_history_by_puuid("v3", region, puuid, size, game_mode, **kwargs)
+    return get_match_history_by_puuid(
+        "v3", region, puuid, size, map, game_mode, **kwargs
+    )
 
 
 def get_match_history_by_name(
     version: str,
     region: str,
     name: str,
     tag: str,
     size: Optional[int] = None,
+    map: Optional[str] = None,
     game_mode: Optional[str] = None,
     **kwargs,
 ) -> List[MatchHistoryPointV3]:
     """Get the match history for a player by name and tag using a specific version of the endpoint.
 
     Args:
         version: The version of the endpoint to use.
@@ -84,14 +93,15 @@
             v3 (Version 3)
         region: The region of the player.
             One of the following:
             eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
         name: The name of the player.
         tag: The tag of the player.
         size: The number of matches to return. Maximum is 10.
+        map: The map to filter by.
         game_mode: The game mode to filter by.
         **kwargs: Any additional arguments to pass to the endpoint.
 
     Returns:
         A list of :class:`.MatchHistoryPointV3` objects.
 
     Raises:
@@ -104,14 +114,16 @@
                 "You cannot fetch more then 10 matches with this endpoint. "
                 "Size will be reduced to 10. "
                 "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
             )
         query_args["size"] = str(size).lower()
     if game_mode:
         query_args["filter"] = game_mode.lower()
+    if map:
+        query_args["map"] = map.capitalize()
     response = fetch_endpoint(
         EndpointsConfig.MATCH_HISTORY_BY_NAME,
         version=version,
         region=region,
         name=name,
         tag=tag,
         query_args=query_args,
@@ -129,28 +141,30 @@
 
 
 def get_match_history_by_puuid(
     version: str,
     region: str,
     puuid: str,
     size: Optional[int] = None,
+    map: Optional[str] = None,
     game_mode: Optional[str] = None,
     **kwargs,
 ) -> List[MatchHistoryPointV3]:
     """Get the match history for a player by puuid using a specific version of the endpoint.
 
     Args:
         version: The version of the endpoint to use.
             One of the following:
             v3 (Version 3)
         region: The region of the player.
             One of the following:
             eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
         puuid: The puuid of the player.
         size: The number of matches to return. Maximum is 10.
+        map: The map to filter by.
         game_mode: The game mode to filter by.
         **kwargs: Any additional arguments to pass to the endpoint.
 
     Returns:
         A list of :class:`.MatchHistoryPointV3` objects.
 
     Raises:
@@ -164,14 +178,16 @@
                 "Size will be reduced to 10. "
                 "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
             )
             size = 10
         query_args["size"] = str(size).lower()
     if game_mode:
         query_args["filter"] = game_mode.lower()
+    if map:
+        query_args["map"] = map.capitalize()
     response = fetch_endpoint(
         EndpointsConfig.MATCH_HISTORY_BY_PUUID,
         version=version,
         region=region,
         puuid=puuid,
         query_args=query_args,
         **kwargs,
@@ -191,14 +207,15 @@
     from valo_api.utils.fetch_endpoint import fetch_endpoint_async
 
     async def get_match_history_by_name_v3_async(
         region: str,
         name: str,
         tag: str,
         size: Optional[int] = None,
+        map: Optional[str] = None,
         game_mode: Optional[str] = None,
         **kwargs,
     ) -> List[MatchHistoryPointV3]:
         """Get the match history for a player by name and tag using version 3 of the endpoint.
 
         This is the same as :py:meth:`get_match_history_by_name_async(version="v3", region=region, name=name, tag=tag,
         size=size, game_mode=game_mode, **kwargs) <get_match_history_by_name_async>`
@@ -206,58 +223,62 @@
         Args:
             region: The region of the player.
                 One of the following:
                 eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
             name: The name of the player.
             tag: The tag of the player.
             size: The number of matches to return. Maximum is 10.
+            map: The map to filter by.
             game_mode: The game mode to filter by.
             **kwargs: Any additional arguments to pass to the endpoint.
 
         Returns:
             A list of :class:`.MatchHistoryPointV3` objects.
         """
         return await get_match_history_by_name_async(
-            "v3", region, name, tag, size, game_mode, **kwargs
+            "v3", region, name, tag, size, map, game_mode, **kwargs
         )
 
     async def get_match_history_by_puuid_v3_async(
         region: str,
         puuid: str,
         size: Optional[int] = None,
+        map: Optional[str] = None,
         game_mode: Optional[str] = None,
         **kwargs,
     ) -> List[MatchHistoryPointV3]:
         """Get the match history for a player by puuid using version 3 of the endpoint.
 
         This is the same as :py:meth:`get_match_history_by_puuid_async(version="v3", region=region, puuid=puuid,
         size=size, game_mode=game_mode, **kwargs) <get_match_history_by_puuid_async>`
 
         Args:
             region: The region of the player.
                 One of the following:
                 eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
             puuid: The puuid of the player.
             size: The number of matches to return. Maximum is 10.
+            map: The map to filter by.
             game_mode: The game mode to filter by.
             **kwargs: Any additional arguments to pass to the endpoint.
 
         Returns:
             A list of :class:`.MatchHistoryPointV3` objects.
         """
         return await get_match_history_by_puuid_async(
-            "v3", region, puuid, size, game_mode, **kwargs
+            "v3", region, puuid, size, map, game_mode, **kwargs
         )
 
     async def get_match_history_by_name_async(
         version: str,
         region: str,
         name: str,
         tag: str,
         size: Optional[int] = None,
+        map: Optional[str] = None,
         game_mode: Optional[str] = None,
         **kwargs,
     ) -> List[MatchHistoryPointV3]:
         """Get the match history for a player by name and tag using a specific version of the endpoint.
 
         Args:
             version: The version of the endpoint to use.
@@ -265,14 +286,15 @@
                 v3 (Version 3)
             region: The region of the player.
                 One of the following:
                 eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
             name: The name of the player.
             tag: The tag of the player.
             size: The number of matches to return. Maximum is 10.
+            map: The map to filter by.
             game_mode: The game mode to filter by.
             **kwargs: Any additional arguments to pass to the endpoint.
 
         Returns:
             A list of :class:`.MatchHistoryPointV3` objects.
 
         Raises:
@@ -286,14 +308,16 @@
                     "Size will be reduced to 10. "
                     "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
                 )
                 size = 10
             query_args["size"] = str(size).lower()
         if game_mode:
             query_args["filter"] = game_mode.lower()
+        if map:
+            query_args["map"] = map.lower()
         response, content = await fetch_endpoint_async(
             EndpointsConfig.MATCH_HISTORY_BY_NAME,
             version=version,
             region=region,
             name=name,
             tag=tag,
             query_args=query_args,
@@ -310,28 +334,30 @@
         ).data
 
     async def get_match_history_by_puuid_async(
         version: str,
         region: str,
         puuid: str,
         size: Optional[int] = None,
+        map: Optional[str] = None,
         game_mode: Optional[str] = None,
         **kwargs,
     ) -> List[MatchHistoryPointV3]:
         """Get the match history for a player by puuid using a specific version of the endpoint.
 
         Args:
             version: The version of the endpoint to use.
                 One of the following:
                 v3 (Version 3)
             region: The region of the player.
                 One of the following:
                 eu (Europe), na (North America), ap (Asia Pacific), kr (Korea), latam (Latin America), br (Brazil)
             puuid: The puuid of the player.
             size: The number of matches to return. Maximum is 10.
+            map: The game mode to filter by.
             game_mode: The game mode to filter by.
             **kwargs: Any additional arguments to pass to the endpoint.
 
         Returns:
             A list of :class:`.MatchHistoryPointV3` objects.
 
         Raises:
@@ -345,14 +371,16 @@
                     "Size will be reduced to 10. "
                     "See https://github.com/raimannma/ValorantAPI/issues/181 for a workaround."
                 )
                 size = 10
             query_args["size"] = str(size).lower()
         if game_mode:
             query_args["filter"] = game_mode.lower()
+        if map:
+            query_args["map"] = map.lower()
         response, content = await fetch_endpoint_async(
             EndpointsConfig.MATCH_HISTORY_BY_PUUID,
             version=version,
             region=region,
             puuid=puuid,
             query_args=query_args,
             **kwargs,
```

### Comparing `valo_api-1.6.7/valo_api/endpoints/mmr_details.py` & `valo_api-1.6.8/valo_api/endpoints/mmr_details.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/mmr_history.py` & `valo_api-1.6.8/valo_api/endpoints/mmr_history.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/raw.py` & `valo_api-1.6.8/valo_api/endpoints/raw.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/status.py` & `valo_api-1.6.8/valo_api/endpoints/status.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/store_featured.py` & `valo_api-1.6.8/valo_api/endpoints/store_featured.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/store_offers.py` & `valo_api-1.6.8/valo_api/endpoints/store_offers.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/version_info.py` & `valo_api-1.6.8/valo_api/endpoints/version_info.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints/website.py` & `valo_api-1.6.8/valo_api/endpoints/website.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/endpoints_config.py` & `valo_api-1.6.8/valo_api/endpoints_config.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/exceptions/rate_limit.py` & `valo_api-1.6.8/valo_api/exceptions/rate_limit.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/exceptions/valo_api_exception.py` & `valo_api-1.6.8/valo_api/exceptions/valo_api_exception.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/competitive_updates_raw.py` & `valo_api-1.6.8/valo_api/responses/competitive_updates_raw.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/content.py` & `valo_api-1.6.8/valo_api/responses/content.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/leaderboard.py` & `valo_api-1.6.8/valo_api/responses/leaderboard.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/match_details_raw.py` & `valo_api-1.6.8/valo_api/responses/match_details_raw.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/match_history.py` & `valo_api-1.6.8/valo_api/responses/match_history.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/mmr_details.py` & `valo_api-1.6.8/valo_api/responses/mmr_details.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/mmr_raw.py` & `valo_api-1.6.8/valo_api/responses/mmr_raw.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/status.py` & `valo_api-1.6.8/valo_api/responses/status.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/store_featured.py` & `valo_api-1.6.8/valo_api/responses/store_featured.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/responses/store_offers.py` & `valo_api-1.6.8/valo_api/responses/store_offers.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/valo_api/utils/fetch_endpoint.py` & `valo_api-1.6.8/valo_api/utils/fetch_endpoint.py`

 * *Files identical despite different names*

### Comparing `valo_api-1.6.7/PKG-INFO` & `valo_api-1.6.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: valo-api
-Version: 1.6.7
+Version: 1.6.8
 Summary: Valorant API Wrapper for https://github.com/Henrik-3/unofficial-valorant-api
 Home-page: https://github.com/raimannma/ValorantAPI
 License: MIT
 Author: Manuel Raimann
 Author-email: raimannma@outlook.de
 Requires-Python: >=3.8,<4.0
 Classifier: Development Status :: 5 - Production/Stable
@@ -21,15 +21,15 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Provides-Extra: async
 Requires-Dist: Pillow (>=9.2.0,<10.0.0)
 Requires-Dist: aiohttp (>=3.8.3,<4.0.0) ; extra == "async"
 Requires-Dist: asyncio[speedups] (>=3.4.3,<4.0.0) ; extra == "async"
-Requires-Dist: msgspec (>=0.12,<0.14)
+Requires-Dist: msgspec (>=0.12,<0.15)
 Requires-Dist: requests (>=2.28.1,<3.0.0)
 Project-URL: Repository, https://github.com/raimannma/ValorantAPI
 Description-Content-Type: text/markdown
 
 # valo_api
 
 <div align="center">
```

