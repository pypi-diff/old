# Comparing `tmp/novelai-api-0.8.tar.gz` & `tmp/novelai-api-0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "novelai-api-0.8.tar", last modified: Wed Feb  9 10:50:08 2022, max compression
+gzip compressed data, was "novelai-api-0.9.tar", last modified: Wed Mar 30 05:15:44 2022, max compression
```

## Comparing `novelai-api-0.8.tar` & `novelai-api-0.9.tar`

### file list

```diff
@@ -1,28 +1,90 @@
-drwxrwxrwx   0 arthus    (1000) arthus    (1000)        0 2022-02-09 10:50:08.660074 novelai-api-0.8/
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     2077 2022-02-09 10:50:08.656334 novelai-api-0.8/PKG-INFO
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     1145 2022-01-18 10:23:53.000000 novelai-api-0.8/README.md
-drwxrwxrwx   0 arthus    (1000) arthus    (1000)        0 2022-02-09 10:50:08.544356 novelai-api-0.8/novelai_api/
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     1480 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/BanList.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     3211 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/BiasGroup.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)      216 2022-01-14 14:54:52.000000 novelai-api-0.8/novelai_api/FakeClientSession.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     3900 2022-02-09 09:14:40.000000 novelai-api-0.8/novelai_api/GlobalSettings.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)      899 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/Idstore.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     4778 2022-01-18 10:23:53.000000 novelai-api-0.8/novelai_api/Keystore.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)      233 2022-01-12 07:46:31.000000 novelai-api-0.8/novelai_api/NovelAIError.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     2455 2022-01-14 14:54:38.000000 novelai-api-0.8/novelai_api/NovelAI_API.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     8617 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/Preset.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)      710 2022-01-12 07:46:31.000000 novelai-api-0.8/novelai_api/SchemaValidator.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     1763 2022-02-09 08:21:02.000000 novelai-api-0.8/novelai_api/Tokenizer.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)       97 2022-01-12 07:46:31.000000 novelai-api-0.8/novelai_api/__init__.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     9891 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/_high_level.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)    18672 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/_low_level.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)    14039 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/story.py
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     9625 2022-02-09 08:10:16.000000 novelai-api-0.8/novelai_api/utils.py
-drwxrwxrwx   0 arthus    (1000) arthus    (1000)        0 2022-02-09 10:50:08.640942 novelai-api-0.8/novelai_api.egg-info/
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     2077 2022-02-09 10:50:08.000000 novelai-api-0.8/novelai_api.egg-info/PKG-INFO
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)      602 2022-02-09 10:50:08.000000 novelai-api-0.8/novelai_api.egg-info/SOURCES.txt
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)        1 2022-02-09 10:50:08.000000 novelai-api-0.8/novelai_api.egg-info/dependency_links.txt
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)       60 2022-02-09 10:50:08.000000 novelai-api-0.8/novelai_api.egg-info/requires.txt
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)       12 2022-02-09 10:50:08.000000 novelai-api-0.8/novelai_api.egg-info/top_level.txt
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)       38 2022-02-09 10:50:08.661075 novelai-api-0.8/setup.cfg
--rwxrwxrwx   0 arthus    (1000) arthus    (1000)     1209 2022-02-09 08:17:34.000000 novelai-api-0.8/setup.py
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.860090 novelai-api-0.9/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1063 2022-02-09 23:14:22.000000 novelai-api-0.9/LICENSE
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       38 2021-09-27 17:39:42.000000 novelai-api-0.9/MANIFEST.in
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1896 2022-03-30 05:15:44.860090 novelai-api-0.9/PKG-INFO
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1145 2022-02-09 23:14:56.000000 novelai-api-0.9/README.md
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.850090 novelai-api-0.9/novelai_api/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1480 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/BanList.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     3211 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/BiasGroup.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     5397 2022-03-29 23:51:12.000000 novelai-api-0.9/novelai_api/GlobalSettings.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      899 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/Idstore.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     4651 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/Keystore.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      233 2022-02-09 23:14:36.000000 novelai-api-0.9/novelai_api/NovelAIError.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     2326 2022-02-14 21:35:08.000000 novelai-api-0.9/novelai_api/NovelAI_API.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     8590 2022-03-29 23:34:15.000000 novelai-api-0.9/novelai_api/Preset.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      710 2022-02-09 23:14:37.000000 novelai-api-0.9/novelai_api/SchemaValidator.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1604 2022-03-29 23:48:36.000000 novelai-api-0.9/novelai_api/Tokenizer.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       97 2022-02-09 23:14:38.000000 novelai-api-0.9/novelai_api/__init__.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    12095 2022-02-14 21:35:08.000000 novelai-api-0.9/novelai_api/_high_level.py
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    22997 2022-03-29 23:32:46.000000 novelai-api-0.9/novelai_api/_low_level.py
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.846756 novelai-api-0.9/novelai_api/presets/
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.850090 novelai-api-0.9/novelai_api/presets/presets_2.7B/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      965 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_2.7B/Storywriter.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       11 2022-02-09 23:14:40.000000 novelai-api-0.9/novelai_api/presets/presets_2.7B/default.txt
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.850090 novelai-api-0.9/novelai_api/presets/presets_6B_v4/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      962 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/Best Guess.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      972 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/Coherent Creativity.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      964 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/Emperor Moth.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      960 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/Luna Moth.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      969 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/Pleasing Results.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      960 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/Sphinx Moth.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      966 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/Storywriter.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       11 2022-02-09 23:14:42.000000 novelai-api-0.9/novelai_api/presets/presets_6B_v4/default.txt
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.853423 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      974 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/Ace of Spades.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      976 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/All-Nighter.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      975 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/Basic Coherence.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      971 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/Genesis.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      973 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/Low Rider.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      986 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/Moonlit Chronicler.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      957 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/Morpho.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      972 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/Ouroboros.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)        7 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_euterpe_v2/default.txt
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.853423 novelai-api-0.9/novelai_api/presets/presets_genji_jp_6b_v2/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      976 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_genji_jp_6b_v2/Genji Default.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       13 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_genji_jp_6b_v2/default.txt
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.853423 novelai-api-0.9/novelai_api/presets/presets_genji_python_6b/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      976 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/presets/presets_genji_python_6b/Storywriter.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       11 2022-02-09 23:14:47.000000 novelai-api-0.9/novelai_api/presets/presets_genji_python_6b/default.txt
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.853423 novelai-api-0.9/novelai_api/presets/presets_krake_v1/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    47294 2022-03-16 03:19:06.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/20BC.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    47306 2022-03-16 03:19:00.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/Adder.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    47301 2022-03-16 03:18:44.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/Astraea.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    47302 2022-03-16 03:18:51.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/Blackjack.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    47291 2022-03-16 03:19:28.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/Calypso.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    47290 2022-03-16 03:19:19.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/Iris.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    47302 2022-03-16 03:19:12.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/Ptah.preset
+-rw-r--r--   0 arthus    (1000) arthus    (1000)        7 2022-03-16 03:21:42.000000 novelai-api-0.9/novelai_api/presets/presets_krake_v1/default.txt
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.853423 novelai-api-0.9/novelai_api/schemas/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      404 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_AccountInformationResponse.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      656 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_AiModuleDto.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       74 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_AiModuleDtos.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      119 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_GetKeystoreResponse.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      154 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_ObjectsResponse.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      276 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_PriorityResponse.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1127 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_SubscriptionResponse.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      113 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_SuccessfulLoginResponse.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      459 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_UserAccountDataResponse.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      436 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/schemas/schema_UserData.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      278 2022-02-10 00:06:31.000000 novelai-api-0.9/novelai_api/schemas/schema_keystore_decrypted.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      339 2022-02-10 00:06:31.000000 novelai-api-0.9/novelai_api/schemas/schema_keystore_encrypted.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      242 2022-02-10 00:06:31.000000 novelai-api-0.9/novelai_api/schemas/schema_keystore_setter.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    14045 2022-02-14 21:35:08.000000 novelai-api-0.9/novelai_api/story.py
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.853423 novelai-api-0.9/novelai_api/templates/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      410 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/templates/template_empty_story.txt
+-rw-r--r--   0 arthus    (1000) arthus    (1000)      561 2021-12-23 11:13:01.000000 novelai-api-0.9/novelai_api/templates/template_empty_story_extended.txt
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     2728 2022-02-10 00:05:38.000000 novelai-api-0.9/novelai_api/templates/template_empty_storycontent.txt
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     6020 2021-12-23 11:22:50.000000 novelai-api-0.9/novelai_api/templates/template_empty_storycontent_extended.txt
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.856757 novelai-api-0.9/novelai_api/tokenizers/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)  1494139 2022-03-29 22:39:11.000000 novelai-api-0.9/novelai_api/tokenizers/gpt2-genji_tokenizer.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)  1355256 2022-03-29 22:22:16.000000 novelai-api-0.9/novelai_api/tokenizers/gpt2_tokenizer.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)  1357238 2022-03-29 22:48:26.000000 novelai-api-0.9/novelai_api/tokenizers/pile_tokenizer.json
+-rw-r--r--   0 arthus    (1000) arthus    (1000)    10266 2022-03-29 23:32:46.000000 novelai-api-0.9/novelai_api/utils.py
+drwxr-xr-x   0 arthus    (1000) arthus    (1000)        0 2022-03-30 05:15:44.850090 novelai-api-0.9/novelai_api.egg-info/
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1896 2022-03-30 05:15:44.000000 novelai-api-0.9/novelai_api.egg-info/PKG-INFO
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     3279 2022-03-30 05:15:44.000000 novelai-api-0.9/novelai_api.egg-info/SOURCES.txt
+-rw-r--r--   0 arthus    (1000) arthus    (1000)        1 2022-03-30 05:15:44.000000 novelai-api-0.9/novelai_api.egg-info/dependency_links.txt
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       59 2022-03-30 05:15:44.000000 novelai-api-0.9/novelai_api.egg-info/requires.txt
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       12 2022-03-30 05:15:44.000000 novelai-api-0.9/novelai_api.egg-info/top_level.txt
+-rw-r--r--   0 arthus    (1000) arthus    (1000)       38 2022-03-30 05:15:44.860090 novelai-api-0.9/setup.cfg
+-rw-r--r--   0 arthus    (1000) arthus    (1000)     1198 2022-03-30 05:13:19.000000 novelai-api-0.9/setup.py
```

### Comparing `novelai-api-0.8/PKG-INFO` & `novelai-api-0.9/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,45 +1,48 @@
 Metadata-Version: 2.1
 Name: novelai-api
-Version: 0.8
+Version: 0.9
 Summary: Python API for the NovelAI REST API
 Home-page: https://github.com/arthus-leroy/novelai-api/
 Author: Arthus Leroy
 Author-email: arthus.leroy@epita.fr
 License: MIT license
-Description: [![Python package](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml)
-        
-        # novelai-api
-        Python API for the NovelAI REST API
-        
-        The module is intended to be used by developers as a help for using NovelAI's REST API.
-        
-        
-        ## Prerequisites:
-        For loging in, credentials are needed (NAI_USERNAME and NAI_PASSWORD). They should be passed from the environment variables.
-        
-        
-        ### Examples:
-        The examples are in the example folder. Each example is working and can be used as a test.
-        Each example can be called with `python <name>.py`.
-        
-        
-        ### Tests:
-        The tests can be called with `pytest -n auto --tb=short tests`. Note that running `npm install fflate` and having node.js installed is required for test_decrypt_encrypt_integrity_check to run properly
-        
-        
-        ### Module:
-        The actual module is in the novelai-api folder.
-        This module is asynchronous, and, as such, must be run with asyncio. An example can be found in any file of the example directory.
-        The module is registered as package under [Pypi](https://pypi.org/project/novelai-api/).
 Keywords: python,NovelAI,API
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+[![Python package](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml)
+
+# novelai-api
+Python API for the NovelAI REST API
+
+The module is intended to be used by developers as a help for using NovelAI's REST API.
+
+
+## Prerequisites:
+For loging in, credentials are needed (NAI_USERNAME and NAI_PASSWORD). They should be passed from the environment variables.
+
+
+### Examples:
+The examples are in the example folder. Each example is working and can be used as a test.
+Each example can be called with `python <name>.py`.
+
+
+### Tests:
+The tests can be called with `pytest -n auto --tb=short tests`. Note that running `npm install fflate` and having node.js installed is required for test_decrypt_encrypt_integrity_check to run properly
+
+
+### Module:
+The actual module is in the novelai-api folder.
+This module is asynchronous, and, as such, must be run with asyncio. An example can be found in any file of the example directory.
+The module is registered as package under [Pypi](https://pypi.org/project/novelai-api/).
+
```

### Comparing `novelai-api-0.8/README.md` & `novelai-api-0.9/README.md`

 * *Files identical despite different names*

### Comparing `novelai-api-0.8/novelai_api/BanList.py` & `novelai-api-0.9/novelai_api/BanList.py`

 * *Files identical despite different names*

### Comparing `novelai-api-0.8/novelai_api/BiasGroup.py` & `novelai-api-0.9/novelai_api/BiasGroup.py`

 * *Files identical despite different names*

### Comparing `novelai-api-0.8/novelai_api/Idstore.py` & `novelai-api-0.9/novelai_api/Idstore.py`

 * *Files identical despite different names*

### Comparing `novelai-api-0.8/novelai_api/Keystore.py` & `novelai-api-0.9/novelai_api/Keystore.py`

 * *Files 2% similar despite different names*

```diff
@@ -83,18 +83,14 @@
             self._keystore = { }
 
             self._compressed = False
             self._decrypted = True
 
             return
 
-        SchemaValidator.validate("schema_keystore_b64", self.data)
-
-        # TODO: check if keystore is actually valid b64 ?
-
         keystore = loads(b64decode(self.data["keystore"]).decode())
         SchemaValidator.validate("schema_keystore_encrypted", keystore)
 
         self._version = keystore["version"]
         self._nonce = bytes(keystore["nonce"])
         sdata = bytes(keystore["sdata"])
```

### Comparing `novelai-api-0.8/novelai_api/Preset.py` & `novelai-api-0.9/novelai_api/Preset.py`

 * *Files 1% similar despite different names*

```diff
@@ -51,17 +51,16 @@
 
 class StrEnum(str, Enum):
     pass
 
 class Model(StrEnum):
     Calliope = "2.7B"
     Sigurd = "6B-v4"
-    Euterpe_v1 = "euterpe-v0"
     Euterpe = "euterpe-v2"
-    # TODO: add 20B
+    Krake = "krake-v1"
 
     Genji = "genji-jp-6b-v2"
     Snek = "genji-python-6b"
 
 class PresetView:
     model: Model
     _official_values: Dict[str, "Preset"]
```

### Comparing `novelai-api-0.8/novelai_api/SchemaValidator.py` & `novelai-api-0.9/novelai_api/SchemaValidator.py`

 * *Files identical despite different names*

### Comparing `novelai-api-0.8/novelai_api/_low_level.py` & `novelai-api-0.9/novelai_api/_low_level.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,58 +1,36 @@
 from aiohttp import ClientSession, ClientError
 from aiohttp.client_reqrep import ClientResponse
-from aiohttp.client import _RequestContextManager
-from aiohttp.http_exceptions import HttpProcessingError
 from aiohttp.client_exceptions import ClientConnectionError
 
-from requests import request as sync_request, Response
-from requests.exceptions import ConnectionError
-
-from enum import Enum
-
 from novelai_api.NovelAIError import NovelAIError
-from novelai_api.FakeClientSession import FakeClientSession
 from novelai_api.utils import tokens_to_b64
 from novelai_api.Tokenizer import Tokenizer
-from novelai_api.Preset import Preset, Model, StrEnum
-
-from typing import Union, Dict, Tuple, List, Iterable, Any, NoReturn, Optional, MethodDescriptorType
+from novelai_api.SchemaValidator import SchemaValidator
+from novelai_api.Preset import Model
 
-class SyncResponse():
-    _rsp: Response
+from json import loads
+from urllib.parse import urlencode, quote
 
-    def __init__(self, rsp: Response):
-        self._rsp = rsp
-        self.status = rsp.status_code
-        self.reason = rsp.reason
-        self.content_type = rsp.headers["Content-Type"].split(';')[0]
+from typing import Union, Dict, Tuple, List, Iterable, Any, NoReturn, Optional
 
-    async def text(self):
-        return self._rsp.text
-
-    async def json(self):
-        return self._rsp.json()
 
 #=== INTERNALS ===#
 #=== API ===#
 class Low_Level:
     _parent: "NovelAI_API"
-    _session: Union[ClientSession, FakeClientSession]
     _is_async: bool
 
-    def __init__(self, parent: "NovelAI_API"):
-        self._is_async = parent._is_async
-
-        assert not self._is_async or isinstance(parent._session, ClientSession), "Session must be of class ClientSession for asynchronous operations"
-        assert self._is_async or isinstance(parent._session, FakeClientSession), "Session must be of class FakeClientSession for synchronous operations"
+    is_schema_validation_enabled: bool
 
+    def __init__(self, parent: "NovelAI_API"):
         self._parent = parent
-        self._session = parent._session
+        self.is_schema_validation_enabled = True
 
-    def _treat_response_object(self, rsp: Union[ClientResponse, SyncResponse], content: Any, status: int) -> Any:
+    def _treat_response_object(self, rsp: ClientResponse, content: Any, status: int) -> Any:
         # error is an unexpected fail and usually come with a success status
         if type(content) is dict and "error" in content:
             raise NovelAIError(rsp.status, content["error"])
 
         # success
         if rsp.status == status:
             return content
@@ -61,84 +39,108 @@
         if type(content) is dict and "message" in content:    # NovelAI REST API error
             raise NovelAIError(rsp.status, content["message"])
         elif hasattr(rsp, "reason"):                        # HTTPException error
             raise NovelAIError(rsp.status, str(rsp.reason))
         else:
             raise NovelAIError(rsp.status, "Unknown error")
 
-    def _treat_response_bool(self, rsp: Union[ClientResponse, SyncResponse], content: Any, status: int) -> bool:
+    def _treat_response_bool(self, rsp: ClientResponse, content: Any, status: int) -> bool:
         if rsp.status == status:
             return True
 
         self._treat_response_object(rsp, content, status)
         return False
 
-    async def _treat_response(self, rsp: Union[ClientResponse, SyncResponse]) -> Any:
+    async def _treat_response(self, rsp: ClientResponse, data: Any) -> Any:
+        if rsp.content_type == "audio/webm":
+            return (await data.read())
         if rsp.content_type == "application/json":
-            return (await rsp.json())
+            return (await data.json())
         else:
-            return (await rsp.text())
+            return (await data.text())
 
-    async def _request_async(self, method: str, url: str, data: Optional[Union[Dict[str, Any], str]] = None) -> Tuple[ClientResponse, Any]:
-        """
-        :param url: Url of the request
-        :param method: Method of the request from ClientSession
-        :param data: Data to pass to the method if needed
-        """
+    def _parse_stream_data(self, stream_content: str) -> Dict[str, Any]:
+        stream_data = {}
 
-        timeout = self._parent._timeout
+        for line in stream_content.splitlines():
+            colon = line.find(":")
+            # TODO: replace by a meaningful error
+            assert ":" != -1, f"Malformed data stream line: {line}"
 
-        if type(data) is dict:    # data transforms dict in str
-            async with self._session.request(method, url, json = data, timeout = timeout) as rsp:
-                return (rsp, await self._treat_response(rsp))
-        else:
-            async with self._session.request(method, url, data = data, timeout = timeout) as rsp:
-                return (rsp, await self._treat_response(rsp))
+            stream_data[line[:colon]] = line[colon + 1:]
 
-    async def _request_sync(self, method: str, url: str, data: Optional[Union[Dict[str, Any], str]] = None) -> Tuple[ClientResponse, Any]:
-        """
-        :param url: Url of the request
-        :param method: Method of the request from the request library
-        :param data: Data to pass to the method if needed
-        """
+        return stream_data
 
-        timeout = self._parent._timeout.total
-        headers = self._parent._session.headers
-        cookies = self._parent._session.cookie_jar
-
-        if type(data) is dict:
-            with sync_request(method, url, headers = headers, json = data, timeout = timeout, cookies = cookies) as rsp:
-                rsp = SyncResponse(rsp)
-                return (rsp, await self._treat_response(rsp))
-        else:
-            with sync_request(method, url, headers = headers, data = data, timeout = timeout, cookies = cookies) as rsp:
-                rsp = SyncResponse(rsp)
-                return (rsp, await self._treat_response(rsp))
+    async def _treat_response_stream(self, rsp: ClientResponse, data: bytes) -> Any:
+        data = data.decode()
 
-    async def request(self, method: str, endpoint: str, data: Optional[Union[Dict[str, Any], str]] = None) -> Tuple[ClientResponse, Any]:
+        if rsp.content_type == "text/event-stream":
+            stream_data = self._parse_stream_data(data)
+
+            # TODO: replace by a meaningful error
+            assert "data" in stream_data
+            data = loads(stream_data["data"])
+
+        return data
+
+    async def _request(self, method: str, url: str, session: ClientSession,
+                             data: Union[Dict[str, Any], str], stream: bool) -> Tuple[ClientResponse, Any]:
+
+        kwargs = {
+            "timeout": self._parent._timeout,
+            "cookies": self._parent.cookies,
+            "headers": self._parent.headers,
+        }
+
+        kwargs["json" if type(data) is dict else "data"] = data
+
+        async with session.request(method, url, **kwargs) as rsp:
+            if stream:
+                async for i in rsp.content.iter_any():
+                    yield (rsp, await self._treat_response_stream(rsp, i))
+            else:
+                yield (rsp, await self._treat_response(rsp, rsp))
+
+    async def request_stream(self, method: str, endpoint: str, data: Optional[Union[Dict[str, Any], str]] = None,
+                                   stream: bool = True) -> Tuple[ClientResponse, Any]:
         """
+        Send request with support for data streaming
+
+        :param method: Method of the request (get, post, delete)
         :param endpoint: Endpoint of the request
-        :param request_method: Method of the reqest from ClientSession
         :param data: Data to pass to the method if needed
+        :param stream: Use data streaming for the response
         """
 
         url = f"{self._parent._BASE_ADDRESS}{endpoint}"
 
+        is_sync = self._parent._session is None
+        session = ClientSession() if is_sync else self._parent._session
+
         try:
-            if self._is_async:
-                return await self._request_async(method, url, data)
-            else:
-                return await self._request_sync(method, url, data)
-        except (ClientConnectionError, ConnectionError) as e:      # No internet
+            async for i in self._request(method, url, session, data, stream):
+                yield i
+        except ClientConnectionError as e:      # No internet
             raise NovelAIError(e.errno, str(e))
         # TODO: there may be other request errors to catch
+        finally:
+            if is_sync:
+                await session.close()
+
+    async def request(self, method: str, endpoint: str, data: Optional[Union[Dict[str, Any], str]] = None) -> Tuple[ClientResponse, Any]:
+        """
+        Send request
 
-    # TODO: move schema verification to low level
+        :param method: Method of the request (get, post, delete)
+        :param endpoint: Endpoint of the request
+        :param data: Data to pass to the method if needed
+        """
 
-    # TODO: Add a stream handler
+        async for i in self.request_stream(method, endpoint, data, False):
+            return i
 
     async def is_reachable(self) -> bool:
         """
         Check if the NovelAI API is reachable
 
         :return: True if reachable, False if not
         """
@@ -170,19 +172,20 @@
 
         if email is not None:
             data["email"] = email
         if giftkey is not None:
             data["giftkey"] = giftkey
 
         rsp, content = await self.request("post", "/user/register", data)
-        rsp = self._treat_response_object(rsp, content, 201)
+        self._treat_response_object(rsp, content, 201)
 
-        # FIXME: handle cases where the response is corrupted
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_SuccessfulLoginResponse", content)
 
-        return rsp
+        return content
 
     async def login(self, access_key: str) -> Dict[str, str]:
         """
         Log in to the account
 
         :param access_key: Access key of the account
 
@@ -190,98 +193,180 @@
         """
 
         assert type(access_key) is str, f"Expected type 'str' for access_key, but got type '{type(access_key)}'"
 
         assert len(access_key) == 64, f"access_key should be 64 characters, got length of {len(access_key)}"
 
         rsp, content = await self.request("post", "/user/login", { "key": access_key })
-        return self._treat_response_object(rsp, content, 201)
+        self._treat_response_object(rsp, content, 201)
 
-    async def change_access_key(self, current_key: str, new_key: str) -> bool:
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_SuccessfulLoginResponse", content)
+
+        return content
+
+    async def change_access_key(self, current_key: str, new_key: str, new_email: Optional[str] = None) -> Dict[str, str]:
         assert type(current_key) is str, f"Expected type 'str' for current_key, but got type '{type(current_key)}'"
         assert type(new_key) is str, f"Expected type 'str' for new_key, but got type '{type(new_key)}'"
+        assert new_email is None or type(new_email) is str, f"Expected None or type 'str' for new_email, but got type '{type(new_email)}'"
 
         assert len(current_key) == 64, f"Current access key should be 64 characters, got length of {len(current_key)}"
         assert len(new_key) == 64, f"New access key should be 64 characters, got length of {len(new_key)}"
 
-        rsp, content = await self.request("post", "/user/change-access-key", { "currentAccessKey": current_key, "newAccessKey": new_key })
+        data = { "currentAccessKey": current_key, "newAccessKey": new_key }
+
+        if new_email is not None:
+            data["newEmail"] = new_email
+
+        rsp, content = await self.request("post", "/user/change-access-key", data)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_SuccessfulLoginResponse", content)
+
+        return content
+
+    async def send_email_verification(self, email: str) -> bool:
+        assert type(email) is str, f"Expected type 'str' for email, but got type '{type(email)}'"
+
+        rsp, content = await self.request("post", "/user/resend-email-verification", { "email": email })
         return self._treat_response_bool(rsp, content, 200)
 
+    async def verify_email(self, verification_token: str) -> bool:
+        assert type(verification_token) is str, f"Expected type 'str' for verification_token, but got type '{type(verification_token)}'"
+
+        assert len(verification_token) == 64, f"Verification token should be 64 characters, got length of {len(verification_token)}"
+
+        rsp, content = await self.request("post", "/user/verify-email", { "verificationToken": verification_token })
+        return self._treat_response_bool(rsp, content, 200)
+
+    async def get_information(self) -> Dict[str, Any]:
+        rsp, content = await self.request("get", "/user/information")
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_AccountInformationResponse", content)
+
+        return content
+
     async def request_account_recovery(self, email: str) -> bool:
         assert type(email) is str, f"Expected type 'str' for email, but got type '{type(email)}'"
 
         rsp, content = await self.request("post", "/user/recovery/request", { "email": email })
         return self._treat_response_bool(rsp, content, 202)
 
-    async def recover_account(self, recovery_token: str, new_key: str, delete_content: bool = False) -> bool:
+    async def recover_account(self, recovery_token: str, new_key: str, delete_content: bool = False) -> Dict[str, Any]:
         assert type(recovery_token) is str, f"Expected type 'str' for recovery_token, but got type '{type(recovery_token)}'"
         assert type(new_key) is str, f"Expected type 'str' for new_key, but got type '{type(new_key)}'"
         assert type(delete_content) is bool, f"Expected type 'bool' for delete_content, but got type '{type(delete_content)}'"
 
         assert 16 <= len(recovery_token), f"Recovery token should be at least 16 characters, got length of {len(recovery_token)}"
         assert len(new_key) == 64, f"New access key should be 64 characters, got length of {len(new_key)}"
 
         rsp, content = await self.request("post", "/user/recovery/recover", { "recoveryToken": recovery_token, "newAccessKey": new_key, "deleteContent": delete_content })
-        return self._treat_response_bool(rsp, content, 201)
+        self._treat_response_object(rsp, content, 201)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_SuccessfulLoginResponse", content)
+
+        return content
 
     async def delete_account(self) -> bool:
         rsp, content = await self.request("post", "/user/delete", None)
         return self._treat_response_bool(rsp, content, 200)
 
+    async def get_data(self) -> Dict[str, Any]:
+        rsp, content = await self.request("get", "/user/data")
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_AccountInformationResponse", content)
+
+        return content
+
     async def get_priority(self) -> Dict[str, Any]:
         rsp, content = await self.request("get", "/user/priority")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_PriorityResponse", content)
+
+        return content
 
     async def get_subscription(self) -> Dict[str, Any]:
         rsp, content = await self.request("get", "/user/subscription")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_SubscriptionResponse", content)
+
+        return content
 
     async def get_keystore(self) -> Dict[str, str]:
         rsp, content = await self.request("get", "/user/keystore")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_GetKeystoreResponse", content)
+
+        return content
 
     async def set_keystore(self, keystore: Dict[str, str]) -> bool:
         assert type(keystore) is dict, f"Expected type 'dicy' for keystore, but got type '{type(keystore)}'"
 
         rsp, content = await self.request("put", "/user/keystore", keystore)
         return self._treat_response_object(rsp, content, 200)
 
     async def download_objects(self, object_type: str) -> Dict[str, List[Dict[str, Union[str, int]]]]:
         assert type(object_type) is str, f"Expected type 'str' for object_type, but got type '{type(object_type)}'"
 
         rsp, content = await self.request("get", f"/user/objects/{object_type}")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_ObjectsResponse", content)
+
+        return content
 
     async def upload_objects(self, object_type: str, meta: str, data: str) -> bool:
         assert type(object_type) is str, f"Expected type 'str' for object_type, but got type '{type(object_type)}'"
         assert type(meta) is str, f"Expected type 'str' for meta, but got type '{type(meta)}'"
         assert type(data) is str, f"Expected type 'str' for data, but got type '{type(data)}'"
 
         assert len(meta) <= 128, f"Meta should be at most 128 characters, got length of {len(meta)}"
 
         rsp, content = await self.request("put", f"/user/objects/{object_type}", { "meta": meta, "data": data })
-        return self._treat_response_bool(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        return content
 
     async def download_object(self, object_type: str, object_id: str) -> Dict[str, Union[str, int]]:
         assert type(object_type) is str, f"Expected type 'str' for object_type, but got type '{type(object_type)}'"
         assert type(object_id) is str, f"Expected type 'str' for object_id, but got type '{type(object_id)}'"
 
         rsp, content = await self.request("get", f"/user/objects/{object_type}/{object_id}")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_userData", content)
+
+        return content
 
     async def upload_object(self, object_type: str, object_id: str, meta: str, data: str) -> bool:
         assert type(object_type) is str, f"Expected type 'str' for object_type, but got type '{type(object_type)}'"
         assert type(object_id) is str, f"Expected type 'str' for object_id, but got type '{type(object_id)}'"
         assert type(meta) is str, f"Expected type 'str' for meta, but got type '{type(meta)}'"
         assert type(data) is str, f"Expected type 'str' for data, but got type '{type(data)}'"
 
         assert len(meta) <= 128, f"Meta should be at most 128 characters, got length of {len(meta)}"
 
         rsp, content = await self.request("patch", f"/user/objects/{object_type}/{object_id}", { "meta": meta, "data": data })
-        return self._treat_response_bool(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        return content
 
     async def delete_object(self, object_type: str, object_id: str) -> Dict[str, Union[str, int]]:
         assert type(object_type) is str, f"Expected type 'str' for object_type, but got type '{type(object_type)}'"
         assert type(object_id) is str, f"Expected type 'str' for object_id, but got type '{type(object_id)}'"
 
         rsp, content = await self.request("delete", f"/user/objects/{object_type}/{object_id}")
         return self._treat_response_object(rsp, content, 200)
@@ -305,88 +390,136 @@
 
     async def change_subscription(self, new_plan: str) -> bool:
         assert type(new_plan) is str, f"Expected type 'str' for new_plan, but got type '{type(new_plan)}'"
 
         rsp, content = await self.request("post", "/user/subscription/change", { "newSubscriptionPlan": new_plan })
         return self._treat_response_bool(rsp, content, 200)
 
-    async def generate(self, input: Union[List[int], str], model: Model, params: Dict[str, Any]) -> Dict[str, str]:
+    async def generate(self, input: Union[List[int], str], model: Model, params: Dict[str, Any],
+                             stream: bool = False) -> Dict[str, str]:
         """
         :param input: Input to be sent the AI
         :param model: Model of the AI
         :param params: Generation parameters
+        :param stream: Use data streaming for the response
 
         :return: Generated output
         """
 
         assert isinstance(input, (str, list)), f"Expected type 'str' or 'List[int]' for input, but got type '{type(input)}'"
         assert type(model) is Model, f"Expected type 'Model' for model, but got type '{type(model)}'"
         assert type(params) is dict, f"Expected type 'dict' for params, but got type '{type(params)}'"
+        assert type(stream) is bool, f"Expected type 'bool' for stream, but got type '{type(stream)}'"
 
         if type(input) is str:
             input = Tokenizer.encode(model, input)
 
         input = tokens_to_b64(input)
         args = { "input": input, "model": model.value, "parameters": params }
 
-        rsp, content = await self.request("post", "/ai/generate", args)
-        return self._treat_response_object(rsp, content, 201)
+        endpoint = "/ai/generate-stream" if stream else "/ai/generate"
 
-    async def generate_stream(self):
-        raise NotImplementedError("Function is not implemented yet")
+        async for rsp, content in self.request_stream("post", endpoint, args, stream):
+            self._treat_response_object(rsp, content, 201)
+
+            yield content
 
     async def classify(self):
         raise NotImplementedError("Function is not implemented yet")
 
     async def train_module(self, data: str, rate: int, steps: int, name: str, desc: str) -> Dict[str, Any]:
         """
         :param data: Dataset of the module, in one single string
         :param rate: Learning rate of the training
         :param steps: Number of steps to train the module for
         :param name: Name of the module
         :param desc: Description of the module
 
-        :return: Module being trained
+        :return: Status of the module being trained
         """
 
         assert type(data) is str, f"Expected type 'str' for data, but got type '{type(data)}'"
         assert type(rate) is int, f"Expected type 'int' for rate, but got type '{type(rate)}'"
         assert type(steps) is int, f"Expected type 'int' for steps, but got type '{type(steps)}'"
         assert type(name) is str, f"Expected type 'str' for name, but got type '{type(name)}'"
         assert type(desc) is str, f"Expected type 'str' for desc, but got type '{type(desc)}'"
 
         rsp, content = await self.request("post", "/ai/module/train", { "data": data, "lr": rate, "steps": steps, "name": name, "description": desc })
-        return self._treat_response_object(rsp, content, 201)
+        self._treat_response_object(rsp, content, 201)
+
+        # TODO: verify response ?
 
-    async def get_modules(self) -> List[Dict[str, Any]]:
+        return content
+
+    async def get_trained_modules(self) -> List[Dict[str, Any]]:
         """
-        :return: List of modules saved on the logged account
+        :return: List of modules trained or in training
         """
 
         rsp, content = await self.request("get", "/ai/module/all")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_AiModuleDto", content)
+
+        return content
 
     async def get_module(self, module_id: str) -> Dict[str, Any]:
         """
         :param module_id: Id of the module
 
-        :return: Selected module
+        :return: Selected module, trained or in training
         """
 
         assert type(module_id) is str, f"Expected type 'str' for module_id, but got type '{type(module_id)}'"
 
         rsp, content = await self.request("get", f"/ai/module/{module_id}")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        if self.is_schema_validation_enabled:
+            SchemaValidator.validate("schema_AiModuleDto", content)
+
+        return content
 
     async def delete_module(self, module_id: str) -> Dict[str, Any]:
         """
         Delete the module with id :ref: `module_id`
 
         :param module_id: Id of the module
 
         :return: Module that got deleted
         """
 
         assert type(module_id) is str, f"Expected type 'str' for module_id, but got type '{type(module_id)}'"
 
         rsp, content = await self.request("delete", f"/ai/module/{module_id}")
-        return self._treat_response_object(rsp, content, 200)
+        self._treat_response_object(rsp, content, 200)
+
+        # TODO: verify response ?
+
+        return content
+
+    async def generate_voice(self, text: str, seed: str, voice: int, opus: bool) -> Dict[str, Any]:
+        """
+        Generate the Text-to-Speech of :ref: `text` using the given seed and voice
+        
+        :param text: Text to synthetize into voice
+        :param seed: Person to use the voice of
+        :param voice: Index of the voice to use
+        :param opus: Use the Opus TTS
+
+        :return: TTS of the text
+        """
+
+        assert type(text) is str, f"Expected type 'str' for text, but got type '{type(text)}'"
+        assert type(seed) is str, f"Expected type 'str' for seed, but got type '{type(seed)}'"
+        assert type(voice) is int, f"Expected type 'int' for voice, but got type '{type(voice)}'"
+        assert type(opus) is bool, f"Expected type 'bool' for opus, but got type '{type(opus)}'"
+
+        # urlencode keeps capitalization on bool =_=
+        opus = "true" if opus else "false"
+        query = urlencode({"text": text, "seed": seed, "voice": voice, "opus": opus}, quote_via = quote)
+
+        rsp, content = await self.request("get", f"/ai/generate-voice?{query}")
+        self._treat_response_object(rsp, content, 200)
+
+        return content
```

### Comparing `novelai-api-0.8/novelai_api/story.py` & `novelai-api-0.9/novelai_api/story.py`

 * *Files 1% similar despite different names*

```diff
@@ -344,23 +344,23 @@
 
         loaded = []
         for storycontent in storycontents:
             if storycontent.get("decrypted"):
                 story_id = storycontent["id"]
 
                 if story_id not in mapping:
-                    self._api._logger.warn(f"Storycontent {story_id} has no associated story")
+                    self._api._logger.warning(f"Storycontent {story_id} has no associated story")
                 else:
                     proxy = self.load(mapping[story_id], storycontent)
                     del mapping[story_id]
 
                     loaded.append(proxy)
 
         for story_id in mapping.keys():
-            self._api._logger.warn(f"Story {story_id} has no associated storycontent")
+            self._api._logger.warning(f"Story {story_id} has no associated storycontent")
 
         return loaded
 
     async def load_from_remote(self) -> List[NovelAI_StoryProxy]:
         stories = await self._api.high_level.download_user_stories()
         storycontents = await self._api.high_level.download_user_story_contents()
```

### Comparing `novelai-api-0.8/novelai_api/utils.py` & `novelai-api-0.9/novelai_api/utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -63,15 +63,15 @@
 
 def encrypt_data(data: Union[str, bytes], key: bytes, nonce: Optional[bytes] = None, is_compressed: bool = False) -> bytes:
     box = SecretBox(key)
 
     if type(data) is not bytes:
         data = data.encode()
 
-    # FIXME: zlib results in different data than the library used by NAI, but they are fully compatible
+    # NOTE: zlib results in different data than the library used by NAI, but they are fully compatible
     if is_compressed:
         deflater = deflate_obj(Z_BEST_COMPRESSION, wbits = -MAX_WBITS)
         data = deflater.compress(data) + deflater.flush()
 
     data = bytes(box.encrypt(data, nonce))
 
     if is_compressed:
@@ -100,16 +100,24 @@
         assert "data" in item, f"Expected key 'data' in item"
 
         # skip already decompressed data
         if item.get("decrypted"):
             continue
 
         try:
-            item["data"] = json.loads(b64decode(item["data"]).decode())
+            data = b64decode(item["data"])
+
+            is_compressed = (len(data) >= 16 and data[:16] == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01")
+            if is_compressed:
+                data = data[16:]
+                data = inflate(data, -MAX_WBITS)
+
+            item["data"] = json.loads(data.decode())
             item["decrypted"] = True    # not decrypted, per say, but for genericity
+            item["compressed"] = is_compressed
         except json.JSONDecodeError:
             item["decrypted"] = False
 
 def compress_user_data(items: Union[List[Dict[str, Any]], Dict[str, Any]]) -> NoReturn:
     """
     Compress the data of each item in :ref: items
     Doesn't encrypt, but does a UTF8 to b64 translation
@@ -121,15 +129,24 @@
 
     for item in items:
         assert type(item) is dict, f"Expected type 'dict' for item of 'items', got type '{type(item)}'"
         assert "data" in item, f"Expected key 'data' in item"
 
         if "decrypted" in item:
             if item["decrypted"]:
-                item["data"] = b64encode(json.dumps(item["data"], separators = (',', ':'), ensure_ascii = False).encode()).decode()
+                data = json.dumps(item["data"], separators = (',', ':'), ensure_ascii = False).encode()
+
+                if "compressed" in item:
+                    if item["compressed"]:
+                        deflater = deflate_obj(Z_BEST_COMPRESSION, wbits = -MAX_WBITS)
+                        data = deflater.compress(data) + deflater.flush()
+                        data = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01" + data
+                    del item["compressed"]
+
+                item["data"] = b64encode(data).decode()
             del item["decrypted"]
 
 def decrypt_user_data(items: Union[List[Dict[str, Any]], Dict[str, Any]], keystore: Keystore) -> NoReturn:
     """
     Decrypt the data of each item in :ref: items
     If a item has already been decrypted, it won't be decrypted a second time
 
@@ -210,32 +227,29 @@
 
                     item["data"] = data
                     del item["nonce"]
                     del item["compressed"]
 
             del item["decrypted"]
 
-def map_meta_to_stories(stories: Union[List[Dict[str, Any]], Dict[str, Any]]) -> Dict[str, Dict[str, Union[str, int]]]:
-    data = {}
-    for story in stories:
-        data[story["meta"]] = story
-
-    return data
-
-def assign_content_to_story(stories: Dict[str, Dict[str, Union[str, int]]], story_contents: Union[List[Dict[str, Any]], Dict[str, Any]]) -> NoReturn:
-    assert type(stories) is dict, "Stories must be mapped, before being associated with their content"
+def assign_content_to_story(stories: Dict[str, Union[str, int]], story_contents: Union[List[Dict[str, Any]], Dict[str, Any]]) -> NoReturn:
+    if type(stories) is not list and type(stories) is not tuple:
+        stories = [stories]
 
     if type(story_contents) is not list and type(story_contents) is not tuple:
         story_contents = [story_contents]
 
-    for story_content in story_contents:
-        meta = story_content["meta"]
+    story_contents = {content["id"]: content for content in story_contents}
+
+    for story in stories:
+        if story.get("decrypted"):
+            remoteId = story["data"].get("remoteStoryId")
 
-        if meta in stories and story_content["decrypted"] and stories[meta]["decrypted"]:
-            stories[meta]["content"] = story_content
+            if remoteId and remoteId in story_contents and story_contents[remoteId].get("decrypted"):
+                story["content"] = story_contents[remoteId]
 
 def remove_non_decrypted_user_data(items: List[Dict[str, Any]]) -> NoReturn:
     for i in range(len(items)):
         if items[i].get("decrypted", False) is False:
             items.pop(i)
             i -= 1
```

### Comparing `novelai-api-0.8/novelai_api.egg-info/PKG-INFO` & `novelai-api-0.9/novelai_api.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,45 +1,48 @@
 Metadata-Version: 2.1
 Name: novelai-api
-Version: 0.8
+Version: 0.9
 Summary: Python API for the NovelAI REST API
 Home-page: https://github.com/arthus-leroy/novelai-api/
 Author: Arthus Leroy
 Author-email: arthus.leroy@epita.fr
 License: MIT license
-Description: [![Python package](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml)
-        
-        # novelai-api
-        Python API for the NovelAI REST API
-        
-        The module is intended to be used by developers as a help for using NovelAI's REST API.
-        
-        
-        ## Prerequisites:
-        For loging in, credentials are needed (NAI_USERNAME and NAI_PASSWORD). They should be passed from the environment variables.
-        
-        
-        ### Examples:
-        The examples are in the example folder. Each example is working and can be used as a test.
-        Each example can be called with `python <name>.py`.
-        
-        
-        ### Tests:
-        The tests can be called with `pytest -n auto --tb=short tests`. Note that running `npm install fflate` and having node.js installed is required for test_decrypt_encrypt_integrity_check to run properly
-        
-        
-        ### Module:
-        The actual module is in the novelai-api folder.
-        This module is asynchronous, and, as such, must be run with asyncio. An example can be found in any file of the example directory.
-        The module is registered as package under [Pypi](https://pypi.org/project/novelai-api/).
 Keywords: python,NovelAI,API
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+[![Python package](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/arthus-leroy/novelai-api/actions/workflows/python-package.yml)
+
+# novelai-api
+Python API for the NovelAI REST API
+
+The module is intended to be used by developers as a help for using NovelAI's REST API.
+
+
+## Prerequisites:
+For loging in, credentials are needed (NAI_USERNAME and NAI_PASSWORD). They should be passed from the environment variables.
+
+
+### Examples:
+The examples are in the example folder. Each example is working and can be used as a test.
+Each example can be called with `python <name>.py`.
+
+
+### Tests:
+The tests can be called with `pytest -n auto --tb=short tests`. Note that running `npm install fflate` and having node.js installed is required for test_decrypt_encrypt_integrity_check to run properly
+
+
+### Module:
+The actual module is in the novelai-api folder.
+This module is asynchronous, and, as such, must be run with asyncio. An example can be found in any file of the example directory.
+The module is registered as package under [Pypi](https://pypi.org/project/novelai-api/).
+
```

### Comparing `novelai-api-0.8/setup.py` & `novelai-api-0.9/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name = "novelai-api",
-    version = "0.8",
+    version = "0.9",
     author = "Arthus Leroy",
     author_email = "arthus.leroy@epita.fr",
     url = "https://github.com/arthus-leroy/novelai-api/",
     description= "Python API for the NovelAI REST API",
     long_description = long_description,
     long_description_content_type = "text/markdown",
     packages = setuptools.find_packages(),
@@ -25,15 +25,14 @@
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     package_dir = { "novelai-api": "novelai_api" },
     python_requires = '>=3.7',
     keywords = [ "python", "NovelAI", "API" ],
     install_requires = [
-		"aiohttp",
+		"aiohttp[speedups]",
 		"argon2-cffi",
 		"pynacl",
         "jsonschema",
-        "requests",
-        "transformers"
+        "tokenizers",
 	]
 )
```

