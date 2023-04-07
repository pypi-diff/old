# Comparing `tmp/browserpilot-0.2.8.tar.gz` & `tmp/browserpilot-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "browserpilot-0.2.8.tar", max compression
+gzip compressed data, was "browserpilot-0.2.9.tar", max compression
```

## Comparing `browserpilot-0.2.8.tar` & `browserpilot-0.2.9.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0     9898 2023-03-10 06:47:46.704243 browserpilot-0.2.8/README.md
--rw-r--r--   0        0        0    17420 2023-03-11 07:04:21.786394 browserpilot-0.2.8/browserpilot/agents/compilers/instruction_compiler.py
--rw-r--r--   0        0        0    25845 2023-03-10 07:05:43.245791 browserpilot-0.2.8/browserpilot/agents/gpt_selenium_agent.py
--rw-r--r--   0        0        0     1421 2023-03-11 07:06:37.532499 browserpilot-0.2.8/browserpilot/agents/memories/__init__.py
--rw-r--r--   0        0        0     7086 2023-03-10 07:05:43.169989 browserpilot-0.2.8/browserpilot/studio.py
--rw-r--r--   0        0        0      485 2023-03-11 07:07:08.312203 browserpilot-0.2.8/pyproject.toml
--rw-r--r--   0        0        0    11007 1970-01-01 00:00:00.000000 browserpilot-0.2.8/setup.py
--rw-r--r--   0        0        0    10644 1970-01-01 00:00:00.000000 browserpilot-0.2.8/PKG-INFO
+-rw-r--r--   0        0        0     9911 2023-03-11 07:16:43.299471 browserpilot-0.2.9/README.md
+-rw-r--r--   0        0        0    17423 2023-03-11 20:41:21.064491 browserpilot-0.2.9/browserpilot/agents/compilers/instruction_compiler.py
+-rw-r--r--   0        0        0    25848 2023-03-11 20:44:30.972335 browserpilot-0.2.9/browserpilot/agents/gpt_selenium_agent.py
+-rw-r--r--   0        0        0     1421 2023-03-11 07:19:20.684759 browserpilot-0.2.9/browserpilot/agents/memories/__init__.py
+-rw-r--r--   0        0        0     7086 2023-03-10 07:05:43.169989 browserpilot-0.2.9/browserpilot/studio.py
+-rw-r--r--   0        0        0      485 2023-03-11 20:41:45.270938 browserpilot-0.2.9/pyproject.toml
+-rw-r--r--   0        0        0    11020 1970-01-01 00:00:00.000000 browserpilot-0.2.9/setup.py
+-rw-r--r--   0        0        0    10657 1970-01-01 00:00:00.000000 browserpilot-0.2.9/PKG-INFO
```

### Comparing `browserpilot-0.2.8/README.md` & `browserpilot-0.2.9/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -98,15 +98,15 @@
 - **Adding to the Prompt Library**: Read "Writing Prompts" above and simply make a pull request to add something to `prompts/`! At some point, I will figure out a protocol for folder naming conventions and the evaluation of submitted code (for security, accuracy, etc). This would be a particularly attractive option for those who aren't as familiar with coding.
 - **Contributing code**: I am happy to take suggestions! The main way to add to the repository is to extend the capabilities of the agent, or to create new agents entirely. The best way to do this is to familiarize yourself with "Architecture and Prompt Patterns" above, and to (a) expand the list of capabilities in the base prompt in `InstructionCompiler` and (b) write the corresponding method in `GPTSeleniumAgent`. 
 
 ## ⛩️ Architecture and Prompt Patterns
 
 This repo was inspired by the work of [Yihui He](https://github.com/yihui-he/ActGPT), [Adept.ai](https://adept.ai/), and [Nat Friedman](https://github.com/nat/natbot). In particular, the basic abstractions and prompts used were built off of Yihui's hackathon code. The idea to preprocess HTML and use GPT-3 to intelligently pick elements out is from Nat. 
 
-- The prompts used can be found in [instruction compiler](agents/compilers/instruction_compiler.py). The base prompt describes in plain English a set of actions that the browsing agent can take, some general conventions on how to write code, and some constraints on its behavior. **These actions correspond one-for-one with methods in `GPTSeleniumAgent`**. Those actions, to-date, include:
+- The prompts used can be found in [instruction compiler](browserpilot/agents/compilers/instruction_compiler.py). The base prompt describes in plain English a set of actions that the browsing agent can take, some general conventions on how to write code, and some constraints on its behavior. **These actions correspond one-for-one with methods in `GPTSeleniumAgent`**. Those actions, to-date, include:
     - `env.driver`, the Selenium webdriver.
     - `env.find_elements(by='id', value=None)` finds and returns list of elements.
     - `env.find_element(by='id', value=None)` is similar to `env.find_elements()` except it only returns the first element.
     - `env.find_nearest(e, xpath)` can be used to locate an element near another one.
     - `env.send_keys(element, text)` sends `text` to element.
     - `env.get(url)` goes to url.
     - `env.click(element)` clicks the element.
```

### Comparing `browserpilot-0.2.8/browserpilot/agents/compilers/instruction_compiler.py` & `browserpilot-0.2.9/browserpilot/agents/compilers/instruction_compiler.py`

 * *Files 0% similar despite different names*

```diff
@@ -75,15 +75,15 @@
 
 
 class InstructionCompiler:
     def __init__(
         self,
         instructions=None,
         base_prompt=BASE_PROMPT,
-        model="gpt-3.5-turbo",
+        model="text-davinci-003",
         use_compiled=True,
     ):
         """Initialize the compiler. The compiler handles the sequencing of
         each set of instructions which are injected into the base prompt.
 
         The primary entrypoint is step(). At each step, the compiler will take
         the current instruction and inject it into the base prompt, asking
```

### Comparing `browserpilot-0.2.8/browserpilot/agents/gpt_selenium_agent.py` & `browserpilot-0.2.9/browserpilot/agents/gpt_selenium_agent.py`

 * *Files 0% similar despite different names*

```diff
@@ -49,15 +49,15 @@
         self,
         instructions,
         chromedriver_path,
         chrome_options={},
         user_data_dir="user_data",
         headless=False,
         retry=False,
-        model_for_instructions="gpt-3.5-turbo",
+        model_for_instructions="text-davinci-003",
         model_for_responses="gpt-3.5-turbo",
         enable_memory=False,
         debug=False,
         debug_html_folder="",
         instruction_output_file=None,
     ):
         """Initialize the agent.
```

### Comparing `browserpilot-0.2.8/browserpilot/agents/memories/__init__.py` & `browserpilot-0.2.9/browserpilot/agents/memories/__init__.py`

 * *Files identical despite different names*

### Comparing `browserpilot-0.2.8/browserpilot/studio.py` & `browserpilot-0.2.9/browserpilot/studio.py`

 * *Files identical despite different names*

### Comparing `browserpilot-0.2.8/setup.py` & `browserpilot-0.2.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -19,17 +19,17 @@
  'openai>=0.27.1,<0.28.0',
  'pyyaml>=6.0,<7.0',
  'selenium>=4.8.2,<5.0.0',
  'tqdm>=4.64.1,<5.0.0']
 
 setup_kwargs = {
     'name': 'browserpilot',
-    'version': '0.2.8',
+    'version': '0.2.9',
     'description': 'Natural language browser automation',
-    'long_description': '# 🛫 BrowserPilot\n\nAn intelligent web browsing agent controlled by natural language.\n\n![demo](assets/demo_buffalo.gif)\n\nLanguage is the most natural interface through which humans give and receive instructions. Instead of writing bespoke automation or scraping code which is brittle to changes, creating and adding agents should be as simple as writing plain English.\n\n## 🏗️ Installation\n\n1. `pip install browserpilot`\n2. Download Chromedriver (latest stable release) from [here](https://sites.google.com/chromium.org/driver/) and place it in the same folder as this file. Unzip. In Finder, right click the unpacked chromedriver and click "Open". This will remove the restrictive default permissions and allow Python to access it.\n3. Create an environment variable in your favorite manner setting OPENAI_API_KEY to your API key.\n\n\n## 🦭 Usage\n### 🗺️ API\nThe form factor is fairly simple (see below).\n\n```python\nfrom browserpilot.agents.gpt_selenium_agent import GPTSeleniumAgent\n\ninstructions = """Go to Google.com\nFind all text boxes.\nFind the first visible text box.\nClick on the first visible text box.\nType in "buffalo buffalo buffalo buffalo buffalo" and press enter.\nWait 2 seconds.\nFind all anchor elements that link to Wikipedia.\nClick on the first one.\nWait for 10 seconds."""\n\nagent = GPTSeleniumAgent(instructions, "/path/to/chromedriver")\nagent.run()\n```\n\nThe harder (but funner) part is writing the natural language prompts.\n\n\n### 📑 Writing Prompts\n\nIt helps if you are familiar with how Selenium works and programming in general. This is because this project uses GPT-3 to translate natural language into code, so you should be as precise as you can. In this way, it is more like writing code with Copilot than it is talking to a friend; for instance, it helps to refer to things as text boxes (vs. "search box") or "button which says \'Log in\'" rather than "the login button". Sometimes, it will also not pick up on specific words that are important, so it helps to break them out into separate lines. Instead of "find all the visible text boxes", you do "find all the text boxes" and then "find the first visible text box".\n\nYou can look at some examples in `prompts/examples` to get started.\n\nCreate "functions" by enclosing instructions in `BEGIN_FUNCTION func_name` and `END_FUNCTION`, and then call them by starting a line with `RUN_FUNCTION` or `INJECT_FUNCTION`. Below is an example: \n\n```\nBEGIN_FUNCTION search_buffalo\nGo to Google.com\nFind all text boxes.\nFind the first visible text box.\nClick on the first visible text box.\nType in "buffalo buffalo buffalo buffalo buffalo" and press enter.\nWait 2 seconds.\nGet all anchors on the page that contain the word "buffalo".\nClick on the first link.\nEND_FUNCTION\n\nRUN_FUNCTION search_buffalo\nWait for 10 seconds.\n```\n\nYou may also choose to create a yaml or json file with a list of instructions. In general, it needs to have an `instructions` field, and optionally a `compiled` field which has the processed code.\n\nSee [buffalo wikipedia example](prompts/examples/buffalo_wikipedia.yaml).\n\nYou may pass a `instruction_output_file` to the constructor of GPTSeleniumAgent which will output a yaml file with the compiled instructions from GPT-3, to avoid having to pay API costs. \n\n### 🎬 Using the Studio CLI\n\nThe BrowserPilot studio is a CLI that is meant to make it easier to iteratively generate prompts. See `run_studio.py` to see how to run the studio class.\n\n```json\n    "clear": "Clears the routine.",\n    "compile": "Compiles the routine.",\n    "delete": "Deletes the last line.",\n    "edit": "Will prompt user to ask them what line to edit.",\n    "exit": "Exits the Studio.",\n    "help": "Shows this message.",\n    "list": "Shows the routine so far.",\n    "run": "Compiles and runs the routine.",\n    "run last": "Replay last compiled routine.",\n    "save": "Saves the routine to a yaml file.",\n```\n\nThe flow could look something like this:\n1. Add natural language commands line by line.\n2. Run `compile` when you are ready, and it will ask the LLM to translate it into Selenium code.\n3. Use `run last` to run that Selenium code (without any additional API calls!) Or simply use `run` to compile AND run.\n4. Watch the Selenium browser come up and work its magic! You can eyeball it to see if it works, or see the stack trace printed to console if it doesn\'t.\n5. Use `list` to see the natural language commands so far. Use `delete` to remove the last line of the prompt, `edit` to select a line to replace, or `clear` to wipe it entirely. \n6. Finally, when you are done, `save` can save it to yaml or `exit` to simply leave. \n\n## ✋🏼 Contributing\nThere are two ways I envision folks contributing.\n\n- **Adding to the Prompt Library**: Read "Writing Prompts" above and simply make a pull request to add something to `prompts/`! At some point, I will figure out a protocol for folder naming conventions and the evaluation of submitted code (for security, accuracy, etc). This would be a particularly attractive option for those who aren\'t as familiar with coding.\n- **Contributing code**: I am happy to take suggestions! The main way to add to the repository is to extend the capabilities of the agent, or to create new agents entirely. The best way to do this is to familiarize yourself with "Architecture and Prompt Patterns" above, and to (a) expand the list of capabilities in the base prompt in `InstructionCompiler` and (b) write the corresponding method in `GPTSeleniumAgent`. \n\n## ⛩️ Architecture and Prompt Patterns\n\nThis repo was inspired by the work of [Yihui He](https://github.com/yihui-he/ActGPT), [Adept.ai](https://adept.ai/), and [Nat Friedman](https://github.com/nat/natbot). In particular, the basic abstractions and prompts used were built off of Yihui\'s hackathon code. The idea to preprocess HTML and use GPT-3 to intelligently pick elements out is from Nat. \n\n- The prompts used can be found in [instruction compiler](agents/compilers/instruction_compiler.py). The base prompt describes in plain English a set of actions that the browsing agent can take, some general conventions on how to write code, and some constraints on its behavior. **These actions correspond one-for-one with methods in `GPTSeleniumAgent`**. Those actions, to-date, include:\n    - `env.driver`, the Selenium webdriver.\n    - `env.find_elements(by=\'id\', value=None)` finds and returns list of elements.\n    - `env.find_element(by=\'id\', value=None)` is similar to `env.find_elements()` except it only returns the first element.\n    - `env.find_nearest(e, xpath)` can be used to locate an element near another one.\n    - `env.send_keys(element, text)` sends `text` to element.\n    - `env.get(url)` goes to url.\n    - `env.click(element)` clicks the element.\n    - `env.wait(seconds)` waits for `seconds` seconds.\n    - `env.scroll(direction, iframe=None)` scrolls the page. Will switch to `iframe` if given. `direction` can be "up", "down", "left", or "right". \n    - `env.get_llm_response(text)` asks AI about a string `text`.\n    - `env.retrieve_information(prompt, entire_page=False)` returns a string, information from a page given a prompt. Use prompt="Summarize:" for summaries. Uses all the text if entire_page=True and only visible text if False. Invoked with commands like "retrieve", "find in the page", or similar.\n    - `env.ask_llm_to_find_element(description)` asks AI to find an element that matches the description.\n    - `env.query_memory(prompt)` asks AI with a prompt to query its memory (an embeddings index) of the web pages it has browsed. Invoked with "Query memory".\n    - `env.save(text, filename)` saves the string `text` to a file `filename`.\n    - `env.get_text_from_page(entire_page)` returns the free text from the page. If entire_page is True, it returns all the text from HTML doc. If False, returns only visible text.\n- The rest of the code is basically middleware which exposes a Selenium object to GPT-3. **For each action mentioned in the base prompt, there is a corresponding method in GPTSeleniumAgent.**\n    - An `InstructionCompiler` is used to parse user input into semantically cogent blocks of actions.\n- The agent has a `Memory` which enables it to synthesize what it sees.\n\n\n## 🎉 Finished\n0.2.6\n- Give the agent a memory (still very experimental and not very good). Add capability to screenshot elements.\n\n0.2.4 and 0.2.5\n- Bug fixes around versioning and prompt injection.\n\n0.2.3\n- Move `chrome_options` to somewhere more sensible. Just keep the yaml clean, you know?\n\n0.2.2\n- ChatGPT support.\n\n0.2.1\n- Dict support for loading instructions.\n\n0.2.0\n- 🎬 a `Studio` CLI which helps iteratively test prompts!\n- JSON loading.\n- Basic iframe support.\n\n<0.2.0\n- GPTSeleniumAgent should be able to load prompts and cached successful runs in the form of yaml files. InstructionCompiler should be able to save instructions to yaml.\n- 💭 Add a summarization capability to the agent.\n- Demo/test something where it has to ask the LLM to synthesize something it reads online.\n- 🚨 Figured out how to feed the content of the HTML page into the GPT-3 context window and have it reliably pick out specific elements from it, that would be great!\n\n## 🚨 Disclaimer 🚨\n\nThis package runs code output from the OpenAI API in Python using `exec`. 🚨 **This is not considered a safe convention** 🚨. Accordingly, you should be extra careful when using this package. The standard disclaimer follows.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n',
+    'long_description': '# 🛫 BrowserPilot\n\nAn intelligent web browsing agent controlled by natural language.\n\n![demo](assets/demo_buffalo.gif)\n\nLanguage is the most natural interface through which humans give and receive instructions. Instead of writing bespoke automation or scraping code which is brittle to changes, creating and adding agents should be as simple as writing plain English.\n\n## 🏗️ Installation\n\n1. `pip install browserpilot`\n2. Download Chromedriver (latest stable release) from [here](https://sites.google.com/chromium.org/driver/) and place it in the same folder as this file. Unzip. In Finder, right click the unpacked chromedriver and click "Open". This will remove the restrictive default permissions and allow Python to access it.\n3. Create an environment variable in your favorite manner setting OPENAI_API_KEY to your API key.\n\n\n## 🦭 Usage\n### 🗺️ API\nThe form factor is fairly simple (see below).\n\n```python\nfrom browserpilot.agents.gpt_selenium_agent import GPTSeleniumAgent\n\ninstructions = """Go to Google.com\nFind all text boxes.\nFind the first visible text box.\nClick on the first visible text box.\nType in "buffalo buffalo buffalo buffalo buffalo" and press enter.\nWait 2 seconds.\nFind all anchor elements that link to Wikipedia.\nClick on the first one.\nWait for 10 seconds."""\n\nagent = GPTSeleniumAgent(instructions, "/path/to/chromedriver")\nagent.run()\n```\n\nThe harder (but funner) part is writing the natural language prompts.\n\n\n### 📑 Writing Prompts\n\nIt helps if you are familiar with how Selenium works and programming in general. This is because this project uses GPT-3 to translate natural language into code, so you should be as precise as you can. In this way, it is more like writing code with Copilot than it is talking to a friend; for instance, it helps to refer to things as text boxes (vs. "search box") or "button which says \'Log in\'" rather than "the login button". Sometimes, it will also not pick up on specific words that are important, so it helps to break them out into separate lines. Instead of "find all the visible text boxes", you do "find all the text boxes" and then "find the first visible text box".\n\nYou can look at some examples in `prompts/examples` to get started.\n\nCreate "functions" by enclosing instructions in `BEGIN_FUNCTION func_name` and `END_FUNCTION`, and then call them by starting a line with `RUN_FUNCTION` or `INJECT_FUNCTION`. Below is an example: \n\n```\nBEGIN_FUNCTION search_buffalo\nGo to Google.com\nFind all text boxes.\nFind the first visible text box.\nClick on the first visible text box.\nType in "buffalo buffalo buffalo buffalo buffalo" and press enter.\nWait 2 seconds.\nGet all anchors on the page that contain the word "buffalo".\nClick on the first link.\nEND_FUNCTION\n\nRUN_FUNCTION search_buffalo\nWait for 10 seconds.\n```\n\nYou may also choose to create a yaml or json file with a list of instructions. In general, it needs to have an `instructions` field, and optionally a `compiled` field which has the processed code.\n\nSee [buffalo wikipedia example](prompts/examples/buffalo_wikipedia.yaml).\n\nYou may pass a `instruction_output_file` to the constructor of GPTSeleniumAgent which will output a yaml file with the compiled instructions from GPT-3, to avoid having to pay API costs. \n\n### 🎬 Using the Studio CLI\n\nThe BrowserPilot studio is a CLI that is meant to make it easier to iteratively generate prompts. See `run_studio.py` to see how to run the studio class.\n\n```json\n    "clear": "Clears the routine.",\n    "compile": "Compiles the routine.",\n    "delete": "Deletes the last line.",\n    "edit": "Will prompt user to ask them what line to edit.",\n    "exit": "Exits the Studio.",\n    "help": "Shows this message.",\n    "list": "Shows the routine so far.",\n    "run": "Compiles and runs the routine.",\n    "run last": "Replay last compiled routine.",\n    "save": "Saves the routine to a yaml file.",\n```\n\nThe flow could look something like this:\n1. Add natural language commands line by line.\n2. Run `compile` when you are ready, and it will ask the LLM to translate it into Selenium code.\n3. Use `run last` to run that Selenium code (without any additional API calls!) Or simply use `run` to compile AND run.\n4. Watch the Selenium browser come up and work its magic! You can eyeball it to see if it works, or see the stack trace printed to console if it doesn\'t.\n5. Use `list` to see the natural language commands so far. Use `delete` to remove the last line of the prompt, `edit` to select a line to replace, or `clear` to wipe it entirely. \n6. Finally, when you are done, `save` can save it to yaml or `exit` to simply leave. \n\n## ✋🏼 Contributing\nThere are two ways I envision folks contributing.\n\n- **Adding to the Prompt Library**: Read "Writing Prompts" above and simply make a pull request to add something to `prompts/`! At some point, I will figure out a protocol for folder naming conventions and the evaluation of submitted code (for security, accuracy, etc). This would be a particularly attractive option for those who aren\'t as familiar with coding.\n- **Contributing code**: I am happy to take suggestions! The main way to add to the repository is to extend the capabilities of the agent, or to create new agents entirely. The best way to do this is to familiarize yourself with "Architecture and Prompt Patterns" above, and to (a) expand the list of capabilities in the base prompt in `InstructionCompiler` and (b) write the corresponding method in `GPTSeleniumAgent`. \n\n## ⛩️ Architecture and Prompt Patterns\n\nThis repo was inspired by the work of [Yihui He](https://github.com/yihui-he/ActGPT), [Adept.ai](https://adept.ai/), and [Nat Friedman](https://github.com/nat/natbot). In particular, the basic abstractions and prompts used were built off of Yihui\'s hackathon code. The idea to preprocess HTML and use GPT-3 to intelligently pick elements out is from Nat. \n\n- The prompts used can be found in [instruction compiler](browserpilot/agents/compilers/instruction_compiler.py). The base prompt describes in plain English a set of actions that the browsing agent can take, some general conventions on how to write code, and some constraints on its behavior. **These actions correspond one-for-one with methods in `GPTSeleniumAgent`**. Those actions, to-date, include:\n    - `env.driver`, the Selenium webdriver.\n    - `env.find_elements(by=\'id\', value=None)` finds and returns list of elements.\n    - `env.find_element(by=\'id\', value=None)` is similar to `env.find_elements()` except it only returns the first element.\n    - `env.find_nearest(e, xpath)` can be used to locate an element near another one.\n    - `env.send_keys(element, text)` sends `text` to element.\n    - `env.get(url)` goes to url.\n    - `env.click(element)` clicks the element.\n    - `env.wait(seconds)` waits for `seconds` seconds.\n    - `env.scroll(direction, iframe=None)` scrolls the page. Will switch to `iframe` if given. `direction` can be "up", "down", "left", or "right". \n    - `env.get_llm_response(text)` asks AI about a string `text`.\n    - `env.retrieve_information(prompt, entire_page=False)` returns a string, information from a page given a prompt. Use prompt="Summarize:" for summaries. Uses all the text if entire_page=True and only visible text if False. Invoked with commands like "retrieve", "find in the page", or similar.\n    - `env.ask_llm_to_find_element(description)` asks AI to find an element that matches the description.\n    - `env.query_memory(prompt)` asks AI with a prompt to query its memory (an embeddings index) of the web pages it has browsed. Invoked with "Query memory".\n    - `env.save(text, filename)` saves the string `text` to a file `filename`.\n    - `env.get_text_from_page(entire_page)` returns the free text from the page. If entire_page is True, it returns all the text from HTML doc. If False, returns only visible text.\n- The rest of the code is basically middleware which exposes a Selenium object to GPT-3. **For each action mentioned in the base prompt, there is a corresponding method in GPTSeleniumAgent.**\n    - An `InstructionCompiler` is used to parse user input into semantically cogent blocks of actions.\n- The agent has a `Memory` which enables it to synthesize what it sees.\n\n\n## 🎉 Finished\n0.2.6\n- Give the agent a memory (still very experimental and not very good). Add capability to screenshot elements.\n\n0.2.4 and 0.2.5\n- Bug fixes around versioning and prompt injection.\n\n0.2.3\n- Move `chrome_options` to somewhere more sensible. Just keep the yaml clean, you know?\n\n0.2.2\n- ChatGPT support.\n\n0.2.1\n- Dict support for loading instructions.\n\n0.2.0\n- 🎬 a `Studio` CLI which helps iteratively test prompts!\n- JSON loading.\n- Basic iframe support.\n\n<0.2.0\n- GPTSeleniumAgent should be able to load prompts and cached successful runs in the form of yaml files. InstructionCompiler should be able to save instructions to yaml.\n- 💭 Add a summarization capability to the agent.\n- Demo/test something where it has to ask the LLM to synthesize something it reads online.\n- 🚨 Figured out how to feed the content of the HTML page into the GPT-3 context window and have it reliably pick out specific elements from it, that would be great!\n\n## 🚨 Disclaimer 🚨\n\nThis package runs code output from the OpenAI API in Python using `exec`. 🚨 **This is not considered a safe convention** 🚨. Accordingly, you should be extra careful when using this package. The standard disclaimer follows.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n',
     'author': 'Andrew Han',
     'author_email': 'handrew11@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `browserpilot-0.2.8/PKG-INFO` & `browserpilot-0.2.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: browserpilot
-Version: 0.2.8
+Version: 0.2.9
 Summary: Natural language browser automation
 Author: Andrew Han
 Author-email: handrew11@gmail.com
 Requires-Python: >=3.10,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
@@ -119,15 +119,15 @@
 - **Adding to the Prompt Library**: Read "Writing Prompts" above and simply make a pull request to add something to `prompts/`! At some point, I will figure out a protocol for folder naming conventions and the evaluation of submitted code (for security, accuracy, etc). This would be a particularly attractive option for those who aren't as familiar with coding.
 - **Contributing code**: I am happy to take suggestions! The main way to add to the repository is to extend the capabilities of the agent, or to create new agents entirely. The best way to do this is to familiarize yourself with "Architecture and Prompt Patterns" above, and to (a) expand the list of capabilities in the base prompt in `InstructionCompiler` and (b) write the corresponding method in `GPTSeleniumAgent`. 
 
 ## ⛩️ Architecture and Prompt Patterns
 
 This repo was inspired by the work of [Yihui He](https://github.com/yihui-he/ActGPT), [Adept.ai](https://adept.ai/), and [Nat Friedman](https://github.com/nat/natbot). In particular, the basic abstractions and prompts used were built off of Yihui's hackathon code. The idea to preprocess HTML and use GPT-3 to intelligently pick elements out is from Nat. 
 
-- The prompts used can be found in [instruction compiler](agents/compilers/instruction_compiler.py). The base prompt describes in plain English a set of actions that the browsing agent can take, some general conventions on how to write code, and some constraints on its behavior. **These actions correspond one-for-one with methods in `GPTSeleniumAgent`**. Those actions, to-date, include:
+- The prompts used can be found in [instruction compiler](browserpilot/agents/compilers/instruction_compiler.py). The base prompt describes in plain English a set of actions that the browsing agent can take, some general conventions on how to write code, and some constraints on its behavior. **These actions correspond one-for-one with methods in `GPTSeleniumAgent`**. Those actions, to-date, include:
     - `env.driver`, the Selenium webdriver.
     - `env.find_elements(by='id', value=None)` finds and returns list of elements.
     - `env.find_element(by='id', value=None)` is similar to `env.find_elements()` except it only returns the first element.
     - `env.find_nearest(e, xpath)` can be used to locate an element near another one.
     - `env.send_keys(element, text)` sends `text` to element.
     - `env.get(url)` goes to url.
     - `env.click(element)` clicks the element.
```

