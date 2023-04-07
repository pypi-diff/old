# Comparing `tmp/gpt3discord-9.0.4.tar.gz` & `tmp/gpt3discord-9.1.tar.gz`

## Comparing `gpt3discord-9.0.4.tar` & `gpt3discord-9.1.tar`

### file list

```diff
@@ -1,32 +1,32 @@
--rw-r--r--   0        0        0     8129 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/gpt3discord.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/__init__.py
--rw-r--r--   0        0        0    20332 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/commands.py
--rw-r--r--   0        0        0     3559 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/image_service_cog.py
--rw-r--r--   0        0        0    12514 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/moderations_service_cog.py
--rw-r--r--   0        0        0    10462 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/prompt_optimizer_cog.py
--rw-r--r--   0        0        0      870 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/search_service_cog.py
--rw-r--r--   0        0        0    47119 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/text_service_cog.py
--rw-r--r--   0        0        0     8491 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/cogs/translation_service_cog.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/__init__.py
--rw-r--r--   0        0        0     5095 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/autocomplete_model.py
--rw-r--r--   0        0        0     2781 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/check_model.py
--rw-r--r--   0        0        0     3247 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/deepl_model.py
--rw-r--r--   0        0        0     2607 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/embed_statics_model.py
--rw-r--r--   0        0        0    37072 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/openai_model.py
--rw-r--r--   0        0        0     3949 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/search_model.py
--rw-r--r--   0        0        0     4176 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/models/user_model.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/__init__.py
--rw-r--r--   0        0        0     1701 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/deletion_service.py
--rw-r--r--   0        0        0    11863 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/environment_service.py
--rw-r--r--   0        0        0     1081 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/health_service.py
--rw-r--r--   0        0        0    14517 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/image_service.py
--rw-r--r--   0        0        0     1075 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/message_queue_service.py
--rw-r--r--   0        0        0    17241 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/moderations_service.py
--rw-r--r--   0        0        0     2447 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/pinecone_service.py
--rw-r--r--   0        0        0    40195 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/text_service.py
--rw-r--r--   0        0        0     2300 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/services/usage_service.py
--rw-r--r--   0        0        0      129 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/.gitignore
--rw-r--r--   0        0        0     1076 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/LICENSE
--rw-r--r--   0        0        0    26098 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/README.md
--rw-r--r--   0        0        0     1304 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/pyproject.toml
--rw-r--r--   0        0        0    26563 2020-02-02 00:00:00.000000 gpt3discord-9.0.4/PKG-INFO
+-rw-r--r--   0        0        0     8127 2020-02-02 00:00:00.000000 gpt3discord-9.1/gpt3discord.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/__init__.py
+-rw-r--r--   0        0        0    20933 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/commands.py
+-rw-r--r--   0        0        0     3559 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/image_service_cog.py
+-rw-r--r--   0        0        0    12514 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/moderations_service_cog.py
+-rw-r--r--   0        0        0    10462 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/prompt_optimizer_cog.py
+-rw-r--r--   0        0        0      870 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/search_service_cog.py
+-rw-r--r--   0        0        0    47335 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/text_service_cog.py
+-rw-r--r--   0        0        0     8491 2020-02-02 00:00:00.000000 gpt3discord-9.1/cogs/translation_service_cog.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/__init__.py
+-rw-r--r--   0        0        0     5317 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/autocomplete_model.py
+-rw-r--r--   0        0        0     2781 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/check_model.py
+-rw-r--r--   0        0        0     3247 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/deepl_model.py
+-rw-r--r--   0        0        0     2607 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/embed_statics_model.py
+-rw-r--r--   0        0        0    37460 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/openai_model.py
+-rw-r--r--   0        0        0     3949 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/search_model.py
+-rw-r--r--   0        0        0     4176 2020-02-02 00:00:00.000000 gpt3discord-9.1/models/user_model.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/__init__.py
+-rw-r--r--   0        0        0     1701 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/deletion_service.py
+-rw-r--r--   0        0        0    11863 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/environment_service.py
+-rw-r--r--   0        0        0     1081 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/health_service.py
+-rw-r--r--   0        0        0    14517 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/image_service.py
+-rw-r--r--   0        0        0     1075 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/message_queue_service.py
+-rw-r--r--   0        0        0    17241 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/moderations_service.py
+-rw-r--r--   0        0        0     2447 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/pinecone_service.py
+-rw-r--r--   0        0        0    40195 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/text_service.py
+-rw-r--r--   0        0        0     2300 2020-02-02 00:00:00.000000 gpt3discord-9.1/services/usage_service.py
+-rw-r--r--   0        0        0      129 2020-02-02 00:00:00.000000 gpt3discord-9.1/.gitignore
+-rw-r--r--   0        0        0     1076 2020-02-02 00:00:00.000000 gpt3discord-9.1/LICENSE
+-rw-r--r--   0        0        0    26098 2020-02-02 00:00:00.000000 gpt3discord-9.1/README.md
+-rw-r--r--   0        0        0     1304 2020-02-02 00:00:00.000000 gpt3discord-9.1/pyproject.toml
+-rw-r--r--   0        0        0    26561 2020-02-02 00:00:00.000000 gpt3discord-9.1/PKG-INFO
```

### Comparing `gpt3discord-9.0.4/gpt3discord.py` & `gpt3discord-9.1/gpt3discord.py`

 * *Files 0% similar despite different names*

```diff
@@ -26,15 +26,15 @@
 from services.message_queue_service import Message
 from services.usage_service import UsageService
 from services.environment_service import EnvService
 
 from models.openai_model import Model
 
 
-__version__ = "9.0.4"
+__version__ = "9.1"
 
 
 PID_FILE = Path("bot.pid")
 PROCESS = None
 
 if sys.platform == "win32":
     separator = "\\"
```

### Comparing `gpt3discord-9.0.4/cogs/commands.py` & `gpt3discord-9.1/cogs/commands.py`

 * *Files 2% similar despite different names*

```diff
@@ -298,14 +298,17 @@
         description="Ask GPT3 something!",
         guild_ids=ALLOWED_GUILDS,
     )
     @discord.option(
         name="prompt", description="The prompt to send to GPT3", required=True
     )
     @discord.option(
+        name="private", description="Will only be visible to you", required=False
+    )
+    @discord.option(
         name="temperature",
         description="Higher values means the model will take more risks",
         required=False,
         min_value=0,
         max_value=2,
     )
     @discord.option(
@@ -330,21 +333,28 @@
         max_value=2,
     )
     @discord.guild_only()
     async def ask(
         self,
         ctx: discord.ApplicationContext,
         prompt: str,
+        private: bool,
         temperature: float,
         top_p: float,
         frequency_penalty: float,
         presence_penalty: float,
     ):
         await self.converser_cog.ask_command(
-            ctx, prompt, temperature, top_p, frequency_penalty, presence_penalty
+            ctx,
+            prompt,
+            private,
+            temperature,
+            top_p,
+            frequency_penalty,
+            presence_penalty,
         )
 
     @add_to_group("gpt")
     @discord.slash_command(
         name="edit",
         description="Ask GPT3 to edit some text!",
         guild_ids=ALLOWED_GUILDS,
@@ -357,14 +367,17 @@
     @discord.option(
         name="text",
         description="The text you want to edit, can be empty",
         required=False,
         default="",
     )
     @discord.option(
+        name="private", description="Will only be visible to you", required=False
+    )
+    @discord.option(
         name="temperature",
         description="Higher values means the model will take more risks",
         required=False,
         input_type=float,
         min_value=0,
         max_value=2,
     )
@@ -381,20 +394,21 @@
     )
     @discord.guild_only()
     async def edit(
         self,
         ctx: discord.ApplicationContext,
         instruction: str,
         text: str,
+        private: bool,
         temperature: float,
         top_p: float,
         codex: bool,
     ):
         await self.converser_cog.edit_command(
-            ctx, instruction, text, temperature, top_p, codex
+            ctx, instruction, text, private, temperature, top_p, codex
         )
 
     @add_to_group("gpt")
     @discord.slash_command(
         name="converse",
         description="Have a conversation with GPT3",
         guild_ids=ALLOWED_GUILDS,
@@ -419,14 +433,21 @@
     @discord.option(
         name="minimal",
         description="Use minimal starter text, saves tokens and has a more open personality",
         required=False,
         default=False,
     )
     @discord.option(
+        name="model",
+        description="Which model to use with the bot",
+        required=False,
+        default=False,
+        autocomplete=Settings_autocompleter.get_models,
+    )
+    @discord.option(
         name="temperature",
         description="Higher values means the model will take more risks",
         required=False,
         input_type=float,
         min_value=0,
         max_value=2,
     )
@@ -458,25 +479,27 @@
     async def converse(
         self,
         ctx: discord.ApplicationContext,
         opener: str,
         opener_file: str,
         private: bool,
         minimal: bool,
+        model: str,
         temperature: float,
         top_p: float,
         frequency_penalty: float,
         presence_penalty: float,
     ):
         await self.converser_cog.converse_command(
             ctx,
             opener,
             opener_file,
             private,
             minimal,
+            model,
             temperature,
             top_p,
             frequency_penalty,
             presence_penalty,
         )
 
     @add_to_group("gpt")
```

### Comparing `gpt3discord-9.0.4/cogs/image_service_cog.py` & `gpt3discord-9.1/cogs/image_service_cog.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/cogs/moderations_service_cog.py` & `gpt3discord-9.1/cogs/moderations_service_cog.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/cogs/prompt_optimizer_cog.py` & `gpt3discord-9.1/cogs/prompt_optimizer_cog.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/cogs/search_service_cog.py` & `gpt3discord-9.1/cogs/search_service_cog.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/cogs/text_service_cog.py` & `gpt3discord-9.1/cogs/text_service_cog.py`

 * *Files 1% similar despite different names*

```diff
@@ -689,14 +689,15 @@
         )
         await ctx.respond(embed=embed)
 
     async def ask_command(
         self,
         ctx: discord.ApplicationContext,
         prompt: str,
+        private: bool,
         temperature: float,
         top_p: float,
         frequency_penalty: float,
         presence_penalty: float,
         from_ask_action=None,
         from_other_action=None,
     ):
@@ -716,15 +717,15 @@
 
         user_api_key = None
         if USER_INPUT_API_KEYS:
             user_api_key = await TextService.get_user_api_key(user.id, ctx, USER_KEY_DB)
             if not user_api_key:
                 return
 
-        await ctx.defer()
+        await ctx.defer(ephemeral=private)
 
         overrides = Override(temperature, top_p, frequency_penalty, presence_penalty)
 
         await TextService.encapsulated_send(
             self,
             user.id,
             prompt,
@@ -737,14 +738,15 @@
         )
 
     async def edit_command(
         self,
         ctx: discord.ApplicationContext,
         instruction: str,
         text: str,
+        private: bool,
         temperature: float,
         top_p: float,
         codex: bool,
     ):
         """Command handler. Requests and returns a generation with no extras to the edit endpoint
 
         Args:
@@ -762,15 +764,15 @@
 
         user_api_key = None
         if USER_INPUT_API_KEYS:
             user_api_key = await TextService.get_user_api_key(user.id, ctx, USER_KEY_DB)
             if not user_api_key:
                 return
 
-        await ctx.defer()
+        await ctx.defer(ephemeral=private)
 
         overrides = Override(temperature, top_p, 0, 0)
 
         await TextService.encapsulated_send(
             self,
             user.id,
             prompt=text,
@@ -797,27 +799,29 @@
     async def converse_command(
         self,
         ctx: discord.ApplicationContext,
         opener: str,
         opener_file: str,
         private: bool,
         minimal: bool,
+        model: str,
         temperature: float,
         top_p: float,
         frequency_penalty: float,
         presence_penalty: float,
     ):
         """Command handler. Starts a conversation with the bot
 
         Args:
             ctx (discord.ApplicationContext): Command interaction
             opener (str): The first prompt to send in the conversation
             opener_file (str): A .txt or .json file which is appended before the opener
             private (bool): If the thread should be private
             minimal (bool): If a minimal starter should be used
+            model (str): The openai model that should be used
             temperature (float): Sets the temperature override
             top_p (float): Sets the top p override
             frequency_penalty (float): Sets the frequency penalty override
             presence_penalty (float): Sets the presence penalty override
         """
 
         user = ctx.user
@@ -862,15 +866,17 @@
             message_thread_real = await ctx.fetch_message(message_thread.id)
             thread = await message_thread_real.create_thread(
                 name=user.name + "'s conversation with GPT3",
                 auto_archive_duration=60,
             )
 
         self.conversation_threads[thread.id] = Thread(thread.id)
-        self.conversation_threads[thread.id].model = self.model.model
+        self.conversation_threads[thread.id].model = (
+            self.model.model if not model else model
+        )
 
         # Set the overrides for the conversation
         self.conversation_threads[thread.id].set_overrides(
             temperature, top_p, frequency_penalty, presence_penalty
         )
 
         if opener:
```

### Comparing `gpt3discord-9.0.4/cogs/translation_service_cog.py` & `gpt3discord-9.1/cogs/translation_service_cog.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/models/autocomplete_model.py` & `gpt3discord-9.1/models/autocomplete_model.py`

 * *Files 8% similar despite different names*

```diff
@@ -82,14 +82,22 @@
         options = values.get(ctx.options["parameter"], [])
         if options:
             return [value for value in options if value.startswith(ctx.value.lower())]
 
         await ctx.interaction.response.defer()  # defer so the autocomplete in int values doesn't error but rather just says not found
         return []
 
+    async def get_models(
+        ctx: discord.AutocompleteContext,
+    ):
+        """Gets all models"""
+        return [
+            value for value in Models.TEXT_MODELS if value.startswith(ctx.value.lower())
+        ]
+
     async def get_value_moderations(
         ctx: discord.AutocompleteContext,
     ):  # Behaves a bit weird if you go back and edit the parameter without typing in a new command
         """gets valid values for the type option"""
         print(f"The value is {ctx.value}")
         return [
             value
```

### Comparing `gpt3discord-9.0.4/models/check_model.py` & `gpt3discord-9.1/models/check_model.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/models/deepl_model.py` & `gpt3discord-9.1/models/deepl_model.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/models/embed_statics_model.py` & `gpt3discord-9.1/models/embed_statics_model.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/models/openai_model.py` & `gpt3discord-9.1/models/openai_model.py`

 * *Files 1% similar despite different names*

```diff
@@ -74,15 +74,15 @@
         "text-ada-001": 2024,
         "code-davinci-002": 7900,
         "code-cushman-001": 2024,
     }
 
     @staticmethod
     def get_max_tokens(model: str) -> int:
-        return Models.TOKEN_MAPPING.get(model, 4024)
+        return Models.TOKEN_MAPPING.get(model, 2024)
 
 
 class ImageSize:
     SMALL = "256x256"
     MEDIUM = "512x512"
     LARGE = "1024x1024"
 
@@ -572,20 +572,26 @@
         ):
             raise ValueError(
                 f"Minimal prompt length must be between {ModelLimits.MIN_PROMPT_MIN_LENGTH} and {ModelLimits.MAX_PROMPT_MIN_LENGTH}, it is currently: {value}"
             )
         self._prompt_min_length = value
         SETTINGS_DB["prompt_min_length"] = value
 
-    def backoff_handler(details):
+    def backoff_handler_http(details):
         print(
             f"Backing off {details['wait']:0.1f} seconds after {details['tries']} tries calling function {details['target']} | "
             f"{details['exception'].status}: {details['exception'].message}"
         )
 
+    def backoff_handler_request(details):
+        print(
+            f"Backing off {details['wait']:0.1f} seconds after {details['tries']} tries calling function {details['target']} | "
+            f"{details['exception'].args[0]}"
+        )
+
     async def valid_text_request(self, response):
         try:
             tokens_used = int(response["usage"]["total_tokens"])
             await self.usage_service.update_usage(tokens_used)
         except Exception as e:
             raise ValueError(
                 "The API returned an invalid response: "
@@ -594,15 +600,15 @@
 
     @backoff.on_exception(
         backoff.expo,
         aiohttp.ClientResponseError,
         factor=3,
         base=5,
         max_tries=4,
-        on_backoff=backoff_handler,
+        on_backoff=backoff_handler_http,
     )
     async def send_embedding_request(self, text, custom_api_key=None):
         async with aiohttp.ClientSession(raise_for_status=True) as session:
             payload = {
                 "model": Models.EMBEDDINGS,
                 "input": text,
             }
@@ -620,19 +626,19 @@
                 except Exception:
                     print(response)
                     traceback.print_exc()
                     return
 
     @backoff.on_exception(
         backoff.expo,
-        aiohttp.ClientResponseError,
+        ValueError,
         factor=3,
         base=5,
-        max_tries=6,
-        on_backoff=backoff_handler,
+        max_tries=4,
+        on_backoff=backoff_handler_request,
     )
     async def send_edit_request(
         self,
         instruction,
         text=None,
         temp_override=None,
         top_p_override=None,
@@ -647,15 +653,15 @@
             )
 
         print(
             f"The text about to be edited is [{text}] with instructions [{instruction}] codex [{codex}]"
         )
         print(f"Overrides -> temp:{temp_override}, top_p:{top_p_override}")
 
-        async with aiohttp.ClientSession(raise_for_status=True) as session:
+        async with aiohttp.ClientSession(raise_for_status=False) as session:
             payload = {
                 "model": Models.EDIT if codex is False else Models.CODE_EDIT,
                 "input": "" if text is None else text,
                 "instruction": instruction,
                 "temperature": self.temp if temp_override is None else temp_override,
                 "top_p": self.top_p if top_p_override is None else top_p_override,
             }
@@ -672,15 +678,15 @@
 
     @backoff.on_exception(
         backoff.expo,
         aiohttp.ClientResponseError,
         factor=3,
         base=5,
         max_tries=6,
-        on_backoff=backoff_handler,
+        on_backoff=backoff_handler_http,
     )
     async def send_moderations_request(self, text):
         # Use aiohttp to send the above request:
         async with aiohttp.ClientSession(raise_for_status=True) as session:
             headers = {
                 "Content-Type": "application/json",
                 "Authorization": f"Bearer {self.openai_key}",
@@ -691,19 +697,19 @@
                 headers=headers,
                 json=payload,
             ) as response:
                 return await response.json()
 
     @backoff.on_exception(
         backoff.expo,
-        aiohttp.ClientResponseError,
+        ValueError,
         factor=3,
         base=5,
         max_tries=4,
-        on_backoff=backoff_handler,
+        on_backoff=backoff_handler_request,
     )
     async def send_summary_request(self, prompt, custom_api_key=None):
         """
         Sends a summary request to the OpenAI API
         """
         summary_request_text = []
         summary_request_text.append(
@@ -714,15 +720,15 @@
         )
         summary_request_text.append(prompt + "\nDetailed summary of conversation: \n")
 
         summary_request_text = "".join(summary_request_text)
 
         tokens = self.usage_service.count_tokens(summary_request_text)
 
-        async with aiohttp.ClientSession(raise_for_status=True) as session:
+        async with aiohttp.ClientSession(raise_for_status=False) as session:
             payload = {
                 "model": Models.DAVINCI,
                 "prompt": summary_request_text,
                 "temperature": 0.5,
                 "top_p": 1,
                 "max_tokens": self.max_tokens - tokens,
                 "presence_penalty": self.presence_penalty,
@@ -742,19 +748,19 @@
 
                 # print(response["choices"][0]["text"])
 
                 return response
 
     @backoff.on_exception(
         backoff.expo,
-        aiohttp.ClientResponseError,
+        ValueError,
         factor=3,
         base=5,
         max_tries=4,
-        on_backoff=backoff_handler,
+        on_backoff=backoff_handler_request,
     )
     async def send_request(
         self,
         prompt,
         tokens,
         temp_override=None,
         top_p_override=None,
@@ -770,28 +776,32 @@
     ):  # The response, and a boolean indicating whether or not the context limit was reached.
         # Validate that  all the parameters are in a good state before we send the request
         if len(prompt) < self.prompt_min_length:
             raise ValueError(
                 f"Prompt must be greater than {self.prompt_min_length} characters, it is currently: {len(prompt)} characters"
             )
 
+        if not max_tokens_override:
+            if model:
+                max_tokens_override = Models.get_max_tokens(model) - tokens
+
         print(f"The prompt about to be sent is {prompt}")
         print(
             f"Overrides -> temp:{temp_override}, top_p:{top_p_override} frequency:{frequency_penalty_override}, presence:{presence_penalty_override}"
         )
 
-        async with aiohttp.ClientSession(raise_for_status=True) as session:
+        async with aiohttp.ClientSession(raise_for_status=False) as session:
             payload = {
                 "model": self.model if model is None else model,
                 "prompt": prompt,
                 "stop": "" if stop is None else stop,
                 "temperature": self.temp if temp_override is None else temp_override,
                 "top_p": self.top_p if top_p_override is None else top_p_override,
                 "max_tokens": self.max_tokens - tokens
-                if not max_tokens_override
+                if max_tokens_override is None
                 else max_tokens_override,
                 "presence_penalty": self.presence_penalty
                 if presence_penalty_override is None
                 else presence_penalty_override,
                 "frequency_penalty": self.frequency_penalty
                 if frequency_penalty_override is None
                 else frequency_penalty_override,
@@ -835,15 +845,15 @@
 
     @backoff.on_exception(
         backoff.expo,
         aiohttp.ClientResponseError,
         factor=3,
         base=5,
         max_tries=4,
-        on_backoff=backoff_handler,
+        on_backoff=backoff_handler_http,
     )
     async def send_image_request(
         self, ctx, prompt, vary=None, custom_api_key=None
     ) -> tuple[File, list[Any]]:
         # Validate that  all the parameters are in a good state before we send the request
         words = len(prompt.split(" "))
         if words < 3 or words > 75:
```

### Comparing `gpt3discord-9.0.4/models/search_model.py` & `gpt3discord-9.1/models/search_model.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/models/user_model.py` & `gpt3discord-9.1/models/user_model.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/deletion_service.py` & `gpt3discord-9.1/services/deletion_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/environment_service.py` & `gpt3discord-9.1/services/environment_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/health_service.py` & `gpt3discord-9.1/services/health_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/image_service.py` & `gpt3discord-9.1/services/image_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/message_queue_service.py` & `gpt3discord-9.1/services/message_queue_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/moderations_service.py` & `gpt3discord-9.1/services/moderations_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/pinecone_service.py` & `gpt3discord-9.1/services/pinecone_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/text_service.py` & `gpt3discord-9.1/services/text_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/services/usage_service.py` & `gpt3discord-9.1/services/usage_service.py`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/LICENSE` & `gpt3discord-9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/README.md` & `gpt3discord-9.1/README.md`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/pyproject.toml` & `gpt3discord-9.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `gpt3discord-9.0.4/PKG-INFO` & `gpt3discord-9.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpt3discord
-Version: 9.0.4
+Version: 9.1
 Summary: A Chat GPT Discord bot
 Project-URL: Documentation, https://github.com/Kav-K/GPT3Discord/#readme
 Project-URL: Issues, https://github.com/Kav-K/GPT3Discord/issues
 Project-URL: Source, https://github.com/Kav-K/GPT3Discord
 Author-email: Kaveen Kumarasinghe <contact@kaveenk.com>
 License-Expression: MIT
 License-File: LICENSE
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: gpt3discord Version: 9.0.4 Summary: A Chat GPT
+Metadata-Version: 2.1 Name: gpt3discord Version: 9.1 Summary: A Chat GPT
 Discord bot Project-URL: Documentation, https://github.com/Kav-K/GPT3Discord/
 #readme Project-URL: Issues, https://github.com/Kav-K/GPT3Discord/issues
 Project-URL: Source, https://github.com/Kav-K/GPT3Discord Author-email: Kaveen
 Kumarasinghe
 kaveenk.com> License-Expression: MIT License-File: LICENSE Classifier:
 Development Status :: 4 - Beta Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.9 Requires-Python: >=3.9
```

