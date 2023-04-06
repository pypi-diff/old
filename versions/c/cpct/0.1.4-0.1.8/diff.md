# Comparing `tmp/cpct-0.1.4.tar.gz` & `tmp/cpct-0.1.8.tar.gz`

## Comparing `cpct-0.1.4.tar` & `cpct-0.1.8.tar`

### file list

```diff
@@ -1,20 +1,21 @@
--rwxr-xr-x   0        0        0      131 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/_START_HERE.cmd
--rw-r--r--   0        0        0      169 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/__about__.py
--rw-r--r--   0        0        0      102 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/__init__.py
--rw-r--r--   0        0        0     2152 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/_install_requirements.py
--rw-r--r--   0        0        0     1224 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/base_types.py
--rw-r--r--   0        0        0    19410 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/cpct.py
--rw-r--r--   0        0        0      182 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/discord.py
--rw-r--r--   0        0        0    19989 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/poepy.py
--rw-r--r--   0        0        0     2053 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/user_info.py
--rw-r--r--   0        0        0    25296 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/img/ChipyLogo.png
--rw-r--r--   0        0        0     4116 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/img/dropper.png
--rw-r--r--   0        0        0   678371 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/img/poe.png
--rwxr-xr-x   0        0        0       38 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/qt/build_gui.bat
--rw-r--r--   0        0        0    33527 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/qt/main_gui.py
--rw-r--r--   0        0        0    34751 2020-02-02 00:00:00.000000 cpct-0.1.4/cpct/qt/main_gui.ui
--rw-r--r--   0        0        0     1975 2020-02-02 00:00:00.000000 cpct-0.1.4/.gitignore
--rw-r--r--   0        0        0     1100 2020-02-02 00:00:00.000000 cpct-0.1.4/LICENSE.txt
--rw-r--r--   0        0        0      652 2020-02-02 00:00:00.000000 cpct-0.1.4/README.md
--rw-r--r--   0        0        0     1801 2020-02-02 00:00:00.000000 cpct-0.1.4/pyproject.toml
--rw-r--r--   0        0        0     1643 2020-02-02 00:00:00.000000 cpct-0.1.4/PKG-INFO
+-rwxr-xr-x   0        0        0      111 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/_START_HERE.cmd
+-rw-r--r--   0        0        0      169 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/__about__.py
+-rw-r--r--   0        0        0      102 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/__init__.py
+-rw-r--r--   0        0        0     2152 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/_install_requirements.py
+-rw-r--r--   0        0        0     1225 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/base_types.py
+-rw-r--r--   0        0        0    21073 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/cpct.py
+-rw-r--r--   0        0        0      182 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/discord.py
+-rw-r--r--   0        0        0    20925 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/poepy.py
+-rw-r--r--   0        0        0     2053 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/user_info.py
+-rw-r--r--   0        0        0    25296 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/img/ChipyLogo.png
+-rw-r--r--   0        0        0    31307 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/img/ctcp_gui.png
+-rw-r--r--   0        0        0     4116 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/img/dropper.png
+-rw-r--r--   0        0        0   678371 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/img/poe.png
+-rwxr-xr-x   0        0        0       38 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/qt/build_gui.bat
+-rw-r--r--   0        0        0    33527 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/qt/main_gui.py
+-rw-r--r--   0        0        0    34751 2020-02-02 00:00:00.000000 cpct-0.1.8/cpct/qt/main_gui.ui
+-rw-r--r--   0        0        0     1975 2020-02-02 00:00:00.000000 cpct-0.1.8/.gitignore
+-rw-r--r--   0        0        0     1100 2020-02-02 00:00:00.000000 cpct-0.1.8/LICENSE.txt
+-rw-r--r--   0        0        0     4707 2020-02-02 00:00:00.000000 cpct-0.1.8/README.md
+-rw-r--r--   0        0        0     1801 2020-02-02 00:00:00.000000 cpct-0.1.8/pyproject.toml
+-rw-r--r--   0        0        0     5628 2020-02-02 00:00:00.000000 cpct-0.1.8/PKG-INFO
```

### Comparing `cpct-0.1.4/cpct/_install_requirements.py` & `cpct-0.1.8/cpct/_install_requirements.py`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/cpct/base_types.py` & `cpct-0.1.8/cpct/base_types.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,19 +16,20 @@
 
 # fetch basetypes
 r = requests.get(ITEM_BASE_TYPES_URL)
 base_type_dict = dict(json.loads(r.content))
 
 # concat into list of basetype&class
 BASE_TYPES = dict([[base_type_dict[base_type]["name"],base_type_dict[base_type]["item_class"]] for base_type in base_type_dict if base_type_dict[base_type]["domain"] == "item"])
+
 # build slot list
 SLOT_LOOKUP = dict([slot_sub(k,v) for k,v in BASE_TYPES.items()])
 
 # TODO reduce excess string check by narrowing down this list 
-"""Body Armours"""
+"""Body Armour"""
 WEAPON_CLASSES = [v for v in BASE_TYPES.items() if any(item in v for item in WEAPON_LIST)]
 
 print("done")
 
 if __name__ == "__main__":
     # print(SLOT_LOOKUP)
     # print(base_type_dict)
```

### Comparing `cpct-0.1.4/cpct/cpct.py` & `cpct-0.1.8/cpct/cpct.py`

 * *Files 5% similar despite different names*

```diff
@@ -9,14 +9,19 @@
 from PyQt5.QtCore import QTimer
 import qt.main_gui
 import ctypes
 import poepy
 import user_info
 from __about__ import __version__
 
+# PoE dev Docs for ref
+# https://www.pathofexile.com/developer/docs
+# TYPE/Structures
+# https://www.pathofexile.com/developer/docs/reference#type-Item
+
 # type checking block (AND RUFF INFO)
 # https://www.youtube.com/watch?v=bcAqceZkZRQ
 if typing.TYPE_CHECKING:
     ...
 
 # set statics
 ASYNC_INTERVAL_MS = 1000
@@ -107,15 +112,15 @@
     
 def apply_ui_connections():
     """Overlay that connects up the GUI so that we can modularly replace the gui.py from QT5
     https://www.geeksforgeeks.org/function-wrappers-in-python/
     Args:
         gui_obj (gui.Ui_MainWindow): Main window GUI object
     """
-    global gui_main, MainWindow
+    global gui_main, MainWindow, parser
 
     # set window Icons
     app.setWindowIcon(QtGui.QIcon('./cpct/cpct/img/ChipyLogo.png'))
     MainWindow.setWindowTitle(f"Chipy's PoE Chaos Tool (v{__version__})")
     
     # set login icon (this is to fix the image path issue)
     icon = QtGui.QIcon()
@@ -128,22 +133,22 @@
     gui_main.color_link_bodies.setIcon(icon)
     gui_main.color_link_boots.setIcon(icon)
     gui_main.color_link_helmets.setIcon(icon)
     gui_main.color_link_weapons.setIcon(icon)
     gui_main.color_link_gloves.setIcon(icon)
 
     # Link ColorPickers
-    gui_main.color_link_amulets.clicked.connect(lambda: pick_color( gui_main.count_amulets, "color_amulets"))
-    gui_main.color_link_belts.clicked.connect(lambda: pick_color( gui_main.count_belts, "color_belts"))
-    gui_main.color_link_bodies.clicked.connect(lambda: pick_color( gui_main.count_bodies, "color_bodies"))
-    gui_main.color_link_boots.clicked.connect(lambda: pick_color( gui_main.count_boots, "color_boots"))
-    gui_main.color_link_gloves.clicked.connect(lambda: pick_color( gui_main.count_gloves, "color_gloves"))
-    gui_main.color_link_helmets.clicked.connect(lambda: pick_color( gui_main.count_helmets, "color_helmets"))
-    gui_main.color_link_rings.clicked.connect(lambda: pick_color( gui_main.count_rings, "color_rings"))
-    gui_main.color_link_weapons.clicked.connect(lambda: pick_color( gui_main.count_weapons, "color_weapons"))
+    gui_main.color_link_amulets.clicked.connect(lambda: pick_color(gui_main, gui_main.count_amulets, "color_amulets"))
+    gui_main.color_link_belts.clicked.connect(lambda: pick_color(gui_main, gui_main.count_belts, "color_belts"))
+    gui_main.color_link_bodies.clicked.connect(lambda: pick_color(gui_main, gui_main.count_bodies, "color_bodies"))
+    gui_main.color_link_boots.clicked.connect(lambda: pick_color(gui_main, gui_main.count_boots, "color_boots"))
+    gui_main.color_link_gloves.clicked.connect(lambda: pick_color(gui_main, gui_main.count_gloves, "color_gloves"))
+    gui_main.color_link_helmets.clicked.connect(lambda: pick_color(gui_main, gui_main.count_helmets, "color_helmets"))
+    gui_main.color_link_rings.clicked.connect(lambda: pick_color(gui_main, gui_main.count_rings, "color_rings"))
+    gui_main.color_link_weapons.clicked.connect(lambda: pick_color(gui_main, gui_main.count_weapons, "color_weapons"))
 
     # # link menus
     gui_main.actionChipy_dev.triggered.connect(lambda: webbrowser.open("www.chipy.dev/me.html"))
     gui_main.actionGitHub.triggered.connect(lambda: webbrowser.open("https://github.com/iamchipy/chipys-pathofexile-chaos-tool/tree/main/cpct"))
     gui_main.actionFilterblade_xyz.triggered.connect(lambda: webbrowser.open("https://www.filterblade.xyz/") )
     gui_main.actionCraftOfExile_com.triggered.connect(lambda: webbrowser.open("https://www.craftofexile.com/en/") )
     gui_main.actionMap_RegEx.triggered.connect(lambda: webbrowser.open("https://poe.re/#/maps") )
@@ -157,15 +162,15 @@
     gui_main.actionInput_ClientSecret.triggered.connect(lambda: request_client_secret() )
     
     #ClientSecrect Menu
     # gui_main.actionInput_ClientSecret.triggered.connect(lambda: receive_client_secret(gui_main) )
 
     # # link buttons
     gui_main.login_link.clicked.connect(lambda: action_login_link(gui_main))
-    gui_main.refresh_link.clicked.connect(lambda: update_unid_counts(gui_main, True))
+    gui_main.refresh_link.clicked.connect(lambda: count_unid_rares(gui_main, True))
     gui_main.item_filter_browse.clicked.connect(lambda: browser_item_filters(gui_main))
     gui_main.client_path_browse.clicked.connect(lambda: browser_client_folder(gui_main))
 
     # Link ComboBoxes
     gui_main.select_league.currentIndexChanged.connect(lambda: action_set_league(gui_main))
     gui_main.select_tab.currentIndexChanged.connect(lambda: action_set_tab(gui_main))
     gui_main.filter_mode.currentIndexChanged.connect(lambda: update_item_filter(gui_main))
@@ -196,14 +201,17 @@
     gui.login_link.setText(user_info.get("form","username"))
     gui.login_link.setDisabled(True)
     gui.select_league.setCurrentText( user_info.get("form","league"))
     gui.select_tab.setCurrentText( user_info.get("form","tab"))
 
     # continue the loading chain
     action_load_leagues(gui)
+    
+    # report completion
+    gui.count_report_string.setText("Successful PathOfExile.com sign-in!")
 
 @timed_try_wrapper
 def action_load_leagues(gui):
     global parser
     leagues = parser.get_leagues()
 
     # clear the box and repop
@@ -239,54 +247,69 @@
     
 @timed_try_wrapper
 def action_set_tab(gui, force_recache:bool=False):
     global parser, gui_main
     user_info.set("form", "tab", gui.select_tab.currentText())
   
 @timed_try_wrapper
-def update_unid_counts(gui, force_recache:bool=False):
-    global parser, gui_main, refresh_off_cooldown
+def count_unid_rares(gui, force_recache:bool=False)->list[list, int]:
+    global refresh_off_cooldown, parser
     league_of_interest = gui.select_league.currentText()
+
+    # put the manual refresh button on cooldown
     refresh_off_cooldown = False
     gui_main.refresh_link.setEnabled(refresh_off_cooldown)
 
     # TODO Auto filter reload "/itemfilter 0PKKgH0"
 
     try:
         # tab_of_interes
         tabs_of_interest = poepy.validate_tab(parser, league_of_interest, gui.select_tab.currentText())
+        print("tabs_of_interest>",type(tabs_of_interest))
 
         # list of items
         items_of_interest = parser.get_items(tabs_of_interest, league_of_interest, force_recache)
+        print("items_of_interest>",type(items_of_interest))
 
         # filter for unid
         items_unidentified = parser.filter_identified(items_of_interest)
+        print("items_unidentified>",items_unidentified)
 
         # filter for ilevel
         items_unidentified_ilvl = parser.filter_ilvl(items_unidentified)
+        print("items_unidentified_ilvl>",items_unidentified_ilvl)
+
+        # filter for rares
+        items_unidentified_ilvl_rare = parser.filter_rarity(items_unidentified_ilvl, rarity="rare")
+        print("items_unidentified_ilvl_rare>",items_unidentified_ilvl_rare)
         
         # loop and count unids
-        count = poepy.count_slots(parser, items_unidentified_ilvl)
+        count = poepy.count_slots(parser, items_unidentified_ilvl_rare)
         # gui_main.count_report_string.setText(f"Count Total: {count['Total']}")
 
         # Set scales and mutlipliers
         target = gui.sets_target.value()
         multiplier = 100//target
 
         # set GUI element values
         gui_main.count_weapons.setValue(count["Weapon"]*multiplier)
         gui_main.count_helmets.setValue(count["Helmet"]*multiplier)
-        gui_main.count_bodies.setValue(count["Body"]*multiplier)
-        gui_main.count_boots.setValue(count["Boots"]*multiplier)
-        gui_main.count_gloves.setValue(count["Gloves"]*multiplier)
+        gui_main.count_bodies.setValue(count["Body Armor"]*multiplier)
+        gui_main.count_boots.setValue(count["Boot"]*multiplier)
+        gui_main.count_gloves.setValue(count["Glove"]*multiplier)
         gui_main.count_belts.setValue(count["Belt"]*multiplier)
         gui_main.count_amulets.setValue(count["Amulet"]*multiplier)
         gui_main.count_rings.setValue((count["Ring"]*multiplier)//2)
+        
+        # report
+        return [count, target]
     except Exception as e:
-        gui.count_report_string.setText("ERR:"+str(e))
+        t = str(time.time())[-1:]
+        gui.count_report_string.setText("ERR:"+str(e)+f"[{t}]")
+        return [False, False]
 
 def async_two():
     global refresh_off_cooldown, gui_main, async_time
     elapsed = time.time() - async_time
     # Entry point to secondary exec chain
     log_search()
     # Trigger only every 5 sec
@@ -296,15 +319,15 @@
     if elapsed > 10:
         async_time = time.time()
 
 @try_wrapper
 def log_search():
     """Checks the ClientLog for a maching zone change with timestamp in the current minute
     """
-    global modified, previous, gui_main
+    global modified, previous, gui_main, parser
     # 2023/03/30 09:11     
     # 2023/03/30 09:26:41 1117798968 cffb0734 [INFO Client 31504] : You have entered Aspirants' Plaza.     
     snippet = " : You have entered"
     path = user_info.get("form","client_path") + "\logs\Client.txt"
     if not os.path.exists(path):
         return False
     modified = os.path.getmtime(path)
@@ -314,15 +337,15 @@
         # gui_main.count_report_string.setText("Reading...")
         stamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
         with open(path, "r", encoding="utf-8") as file:
             for line in file:
                 if stamp in line and snippet in line:
                         print(line)
                         gui_main.count_report_string.setText(line[78:])
-                        update_unid_counts(gui_main)
+                        count_unid_rares(gui_main)
                         return
         # gui_main.count_report_string.setText("Reading... Done")
 
 @timed_try_wrapper
 def browser_item_filters(gui):
     global MainWindow, gui_main
     #C:\Users\chipy\Documents\My Games\Path of Exile\
@@ -345,66 +368,81 @@
     gui_main.client_path_browse.setText(path[0:22]+"..."+path[-13:])
     
 def receive_client_secret(gui):
     global gui_main
     user_info.set("api","client_secret",gui_main.client_secret_input.text())
 
 @timed_try_wrapper
-def pick_color(target_object, save_name):
+def pick_color(gui, target_object, save_name):
     current_color = QtGui.QColor(user_info.get("form", save_name))
     new_color = QColorDialog.getColor(current_color, title=f"Pick a new color for {save_name}")
     if new_color.isValid():
         user_info.set("form", save_name, new_color.name())
         user_info.set("form", save_name+"_rgb", str(list(new_color.getRgb())))
         target_object.setStyleSheet(style_sheet_new_color(PROGRESS_BAR_STYLE,new_color.name()))
-        update_item_filter()
+        update_item_filter(gui)
 
 def style_sheet_new_color(base_style:str,new_color:str) -> str:
     return_string = ""
     i = base_style.find("background-color: ")
     current_color = base_style[i+18:i+25]
     return_string = base_style.replace(current_color, new_color) 
     return return_string
 
 @timed_try_wrapper
-def update_item_filter(gui=None):
+def update_item_filter(gui):
     global gui_main
     header = poepy.ITEM_FILTER_TITLE_START
     footer = poepy.ITEM_FILTER_TITLE_END
     path = user_info.cfg.get("form","filter_name")
     mode = gui_main.filter_mode.currentText()
+    slot_count, target = count_unid_rares(gui)
+
+    # exit case for when counts could not be found
+    if not slot_count:
+        return False
 
-    # read data
+    # read data without mod section
     current_filter = ""
     is_section_to_replace=False
     with open(path, "r") as f:
         for line in f:
             if header in line:
                 is_section_to_replace = True
             elif footer in line:
                 is_section_to_replace = False
             if not is_section_to_replace and footer not in line:
                 current_filter += line
 
-    # append
-   
+    # rebuild filter text adding back in slots as needed   
     prefix = header
     if "Disabled" not in mode:
-        prefix += poepy.ItemFilterEntry("Weapons",user_info.cfg.get("form","color_weapons_rgb"),width="= 1").to_str()
-        prefix += poepy.ItemFilterEntry("Helmets",user_info.cfg.get("form","color_helmets_rgb")).to_str()
-        prefix += poepy.ItemFilterEntry("Body Armours",user_info.cfg.get("form","color_bodies_rgb")).to_str()   
-        prefix += poepy.ItemFilterEntry("Boots",user_info.cfg.get("form","color_boots_rgb")).to_str()
-        prefix += poepy.ItemFilterEntry("Gloves",user_info.cfg.get("form","color_gloves_rgb")).to_str()
-        prefix += poepy.ItemFilterEntry("Amulets",user_info.cfg.get("form","color_amulets_rgb")).to_str()
-        prefix += poepy.ItemFilterEntry("Rings",user_info.cfg.get("form","color_rings_rgb")).to_str()
+        print(slot_count)
+        if slot_count["Weapon"] >= target:
+            prefix += poepy.ItemFilterEntry("Weapon",user_info.cfg.get("form","color_weapons_rgb"),width="= 1").to_str()
+        if slot_count["Helmet"] >= target:
+            prefix += poepy.ItemFilterEntry("Helmet",user_info.cfg.get("form","color_helmets_rgb")).to_str()
+        if slot_count["Body Armor"] >= target:
+            prefix += poepy.ItemFilterEntry("Body Armour",user_info.cfg.get("form","color_bodies_rgb")).to_str()   
+        if slot_count["Boot"] >= target:
+            prefix += poepy.ItemFilterEntry("Boot",user_info.cfg.get("form","color_boots_rgb")).to_str()
+        if slot_count["Glove"] >= target:
+            prefix += poepy.ItemFilterEntry("Glove",user_info.cfg.get("form","color_gloves_rgb")).to_str()
+        if slot_count["Amulet"] >= target:
+            prefix += poepy.ItemFilterEntry("Amulet",user_info.cfg.get("form","color_amulets_rgb")).to_str()
+        if slot_count["Ring"] >= target:
+            prefix += poepy.ItemFilterEntry("Ring",user_info.cfg.get("form","color_rings_rgb")).to_str()
     prefix += footer
 
     # write
     with open(path, "w") as f:
         f.write(prefix+current_filter)
+    
+    # announce update
+    gui_main.count_report_string.setText("Filter updated . . .")
             
 @timed_try_wrapper
 def request_client_secret():
     global gui_main
     promt_obj = QWidget()
     discord_name, ok = QInputDialog.getText(promt_obj, 'Send Discord Request?', 'Please provide the Discord name (including full "name#1234") to send the secret to')
     if ok:
```

### Comparing `cpct-0.1.4/cpct/poepy.py` & `cpct-0.1.8/cpct/poepy.py`

 * *Files 4% similar despite different names*

```diff
@@ -25,14 +25,26 @@
 
 DEPTH_ITEMS = 2
 DEPTH_STASH_NAMES = 1
 
 ITEM_FILTER_TITLE_START = "# START -- Chipy's PoE Chaos Tool\n"
 ITEM_FILTER_TITLE_END = "# END -- Chipy's PoE Chaos Tool\n"
 
+FRAMETYPE_NORMAL = 0
+FRAMETYPE_MAGIC = 1
+FRAMETYPE_RARE = 2
+FRAMETYPE_UNIQUE = 3
+FRAMETYPE_GEM = 4
+FRAMETYPE_CURRENCY = 5
+FRAMETYPE_DIVINATIONCARD = 6
+FRAMETYPE_QUEST = 7
+FRAMETYPE_PROPHECY = 8
+FRAMETYPE_FOIL = 9
+FRAMETYPE_SUPPORTERFOIL = 10
+
 """
 PROCESS
 - Connection handler
 - - Calls
 - - - Output data
 - Data handler
 - - processer
@@ -230,14 +242,15 @@
             'index': 0, 
             'metadata': {'colour': '7c5436'}}
 
         Args:
             league (str): league name as 
         """
         if league+"_stash_response" not in self.cached or force_recache:
+            print("Caching "+league+"_stash")
             self.cached[league+"_stash_response"] = self.api_handler.get_stash(league)
             self.cached[league+"_stash"] = json.loads(self.cached[league+"_stash_response"].content)["stashes"]
     
     def _parse_tab_names(self, stash:dict, filter_remove_only=True) -> dict:
         result = [[i["name"],i["id"]] for i in stash]
         if filter_remove_only:
             result = [i for i in result if "Remove-only" not in i[0]]
@@ -289,14 +302,15 @@
     def get_tab_names(self, league="standard") -> dict:
         self._cache_stash(league)
         self.cached[league+"_tab_names"] = self._parse_tab_names(stash=self.cached[league+"_stash"])
         return self.cached[league+"_tab_names"]
         
     def _cache_tab(self, league:str, stash_id:str, force_recache:bool=False) -> dict:
         if league+"_"+stash_id not in self.cached or force_recache:
+            print("Caching "+league+"_"+stash_id)
             self.cached[league+"_"+stash_id+"_response"] = self.api_handler.get_tab(league, stash_id)
             raw=json.loads(self.cached[league+"_"+stash_id+"_response"].content)
             # print(type(raw))
             # print(type(raw["stash"]))
             # print(type(raw["stash"]["items"]))
             assert "children" not in raw["stash"]  # assert not a parent/nested tab
             self.cached[league+"_"+stash_id] = raw
@@ -343,39 +357,50 @@
             return False
     
     def filter_identified(self, list_of_items:list) -> list:
         return [i for i in list_of_items if i["identified"] is False]
     
     def filter_ilvl(self, list_of_items:list, ilvl:int=60) -> list:
         return [i for i in list_of_items if i["ilvl"] >= 60]
+    
+    def filter_rarity(self, list_of_items:list, rarity:str="rare") -> list:
+        # TODO build the rest of the frametypes
+        # print([i["frameType"] for i in list_of_items ])
+        if rarity == "rare":
+            return [i for i in list_of_items if i["frameType"] == FRAMETYPE_RARE]
+        print("Filtering for rarity '{rarity}' isn't supported yet")
+        return [i for i in list_of_items if i["frameType"] == FRAMETYPE_MAGIC]        
 
     def _cache_profile(self):
         if "profile" not in self.cached:
+            print("Caching Profile")
             self.cached["profile_response"] = self.api_handler.get_profile()
             self.cached["profile_name"] = json.loads(self.cached["profile_response"].content)["name"]
     
     def get_username(self) -> str:
         self._cache_profile()
         return self.cached["profile_name"]
 
     def _cache_characters(self):
         if "characters" not in self.cached:
+            print("Caching Characters")
             self.cached["characters_response"] = self.api_handler.get_characters()
             self.cached["characters"] = json.loads(self.cached["characters_response"].content)["characters"]
 
     def _parse_character_names(self, characters):
         result = [[i["name"],i["league"]] for i in characters]
         return result      
     
     def get_characters(self) -> list:
         self._cache_characters()
         return self._parse_character_names(self.cached["characters"])   
 
     def _cache_leagues(self):
         if "leagues" not in self.cached:
+            print("Caching Leagues")
             self.cached["leagues_response"] = self.api_handler.get_leagues()
             self.cached["leagues"] = json.loads(self.cached["leagues_response"].content)["leagues"]
 
     def _parse_league_names(self, characters):
         result = [i["id"] for i in characters if i["realm"] == "pc"]
         return result  
 
@@ -477,17 +502,17 @@
         return tab
     return False
 
 def count_slots(parser:DataParser, list_of_items:list, include_all_unid:bool=False):
     counts={"Total":0,
             "Weapon":0,
             "Helmet":0,
-            "Body":0,
-            "Boots":0,
-            "Gloves":0,
+            "Body Armor":0,
+            "Boot":0,
+            "Glove":0,
             "Belt":0,
             "Amulet":0,
             "Ring":0}
     for item in list_of_items:
         slot = SLOT_LOOKUP.get(item["baseType"], "Unknown")
         if slot in counts or include_all_unid:
             counts[slot] +=1
```

### Comparing `cpct-0.1.4/cpct/user_info.py` & `cpct-0.1.8/cpct/user_info.py`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/cpct/img/ChipyLogo.png` & `cpct-0.1.8/cpct/img/ChipyLogo.png`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/cpct/img/dropper.png` & `cpct-0.1.8/cpct/img/dropper.png`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/cpct/img/poe.png` & `cpct-0.1.8/cpct/img/poe.png`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/cpct/qt/main_gui.py` & `cpct-0.1.8/cpct/qt/main_gui.py`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/cpct/qt/main_gui.ui` & `cpct-0.1.8/cpct/qt/main_gui.ui`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/.gitignore` & `cpct-0.1.8/.gitignore`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/LICENSE.txt` & `cpct-0.1.8/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `cpct-0.1.4/pyproject.toml` & `cpct-0.1.8/pyproject.toml`

 * *Files identical despite different names*

