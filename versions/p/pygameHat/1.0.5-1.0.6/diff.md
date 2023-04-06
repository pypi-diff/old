# Comparing `tmp/pygameHat-1.0.5.tar.gz` & `tmp/pygameHat-1.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pygameHat-1.0.5.tar", last modified: Tue Mar 28 20:14:44 2023, max compression
+gzip compressed data, was "pygameHat-1.0.6.tar", last modified: Thu Apr  6 20:15:03 2023, max compression
```

## Comparing `pygameHat-1.0.5.tar` & `pygameHat-1.0.6.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-03-28 20:14:44.406873 pygameHat-1.0.5/
--rw-rw-rw-   0        0        0       78 2023-03-19 17:10:47.000000 pygameHat-1.0.5/MANIFEST.in
--rw-rw-rw-   0        0        0      541 2023-03-28 20:14:44.399851 pygameHat-1.0.5/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-03-28 20:14:44.331898 pygameHat-1.0.5/pygameHat/
--rw-rw-rw-   0        0        0     8723 2023-03-28 20:11:45.000000 pygameHat-1.0.5/pygameHat/__init__.py
--rw-rw-rw-   0        0        0       41 2023-03-19 17:43:54.000000 pygameHat-1.0.5/pygameHat/pygameHat.py
-drwxrwxrwx   0        0        0        0 2023-03-28 20:14:44.389851 pygameHat-1.0.5/pygameHat.egg-info/
--rw-rw-rw-   0        0        0      541 2023-03-28 20:14:43.000000 pygameHat-1.0.5/pygameHat.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      229 2023-03-28 20:14:43.000000 pygameHat-1.0.5/pygameHat.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-28 20:14:43.000000 pygameHat-1.0.5/pygameHat.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        7 2023-03-28 20:14:43.000000 pygameHat-1.0.5/pygameHat.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2023-03-28 20:14:43.000000 pygameHat-1.0.5/pygameHat.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-28 20:14:44.406873 pygameHat-1.0.5/setup.cfg
--rw-rw-rw-   0        0        0      719 2023-03-28 20:10:42.000000 pygameHat-1.0.5/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 20:15:03.449497 pygameHat-1.0.6/
+-rw-rw-rw-   0        0        0       78 2023-03-19 17:10:47.000000 pygameHat-1.0.6/MANIFEST.in
+-rw-rw-rw-   0        0        0      541 2023-04-06 20:15:03.445500 pygameHat-1.0.6/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 20:15:03.377514 pygameHat-1.0.6/pygameHat/
+-rw-rw-rw-   0        0        0    10333 2023-04-06 20:11:58.000000 pygameHat-1.0.6/pygameHat/__init__.py
+-rw-rw-rw-   0        0        0       41 2023-03-19 17:43:54.000000 pygameHat-1.0.6/pygameHat/pygameHat.py
+drwxrwxrwx   0        0        0        0 2023-04-06 20:15:03.437497 pygameHat-1.0.6/pygameHat.egg-info/
+-rw-rw-rw-   0        0        0      541 2023-04-06 20:15:02.000000 pygameHat-1.0.6/pygameHat.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      229 2023-04-06 20:15:02.000000 pygameHat-1.0.6/pygameHat.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 20:15:02.000000 pygameHat-1.0.6/pygameHat.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        7 2023-04-06 20:15:02.000000 pygameHat-1.0.6/pygameHat.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2023-04-06 20:15:02.000000 pygameHat-1.0.6/pygameHat.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 20:15:03.449497 pygameHat-1.0.6/setup.cfg
+-rw-rw-rw-   0        0        0      719 2023-04-06 20:11:13.000000 pygameHat-1.0.6/setup.py
```

### Comparing `pygameHat-1.0.5/PKG-INFO` & `pygameHat-1.0.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: pygameHat
-Version: 1.0.5
+Version: 1.0.6
 Summary: Pygame game-making engine
 Home-page: UNKNOWN
 Author: Wojciech Błajda
 Author-email: <mail@mail.com>
 License: UNKNOWN
 Description: UNKNOWN
 Keywords: python,engine,pygame
```

### Comparing `pygameHat-1.0.5/pygameHat/__init__.py` & `pygameHat-1.0.6/pygameHat/__init__.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,32 +1,21 @@
 import pygame, sys, time
 
-
 #pygame initialization
-print("Additional hello from pygameHat :D")
-print("This version is not backwards compatible with pygameHat <= 1.0.4")
+version = "Alpha 1.0.6"
+print(f"\nAdditional hello from pygameHat {version} :D")
+print("\nThis version is not backwards compatible with pygameHat <= 1.0.5")
+
 pygame.init()
 pygame.font.init()
 try:
     pygame.mixer.init()
 except:
     print("WARNING: Failed to initialize audio!")
 
-
-class TextFormat:
-    def __init__(self):
-        self.text = ""
-    
-    def clear(self):
-        self.text = ""
-    def delete_from_end(self):
-        if len(self.text) > 0:
-            self.text = self.text[:-2]
-
-
 #main objects
 class Object:
     def __init__(self):
         self.x = 0
         self.y = 0
         self.sprite = None
     
@@ -45,159 +34,230 @@
 class Room():
     def __init__(self, background=(50, 50, 50), layers={"default": []}, instances=[]):
         self.background = background
         self.layers = layers
         self.instances = instances
 
 class Sprite():
-    def __init__(self, index, spritesheet_data, speed=60, collision=False):
+    def __init__(self, index, spritesheet_data, speed=60, collision=False, offset="middle-center"):
         self.index = pygame.image.load(index).convert_alpha()
         self.speed = speed
         self.x_frames, self.y_frames = spritesheet_data
         self.x_frames -= 1
         self.y_frames -= 1
         self.x_size, self.y_size = self.index.get_width()/(self.x_frames+1), self.index.get_height()/(self.y_frames+1)
         self.current_x_frame = 0
         self.current_y_frame = 0
         self.timer = 1/self.speed
 
         self.collision = collision
         self.collision_shape = self.index.get_rect(width=self.index.get_width()/(self.x_frames+1), height=self.index.get_height()/(self.y_frames+1))
     
+        #Setting sprite offset
+        if offset == "middle-center":
+            self.x_offset, self.y_offset = self.x_size/2, self.y_size/2
+        elif offset == "upper-left":
+            self.x_offset, self.y_offset = 0, 0
+        elif offset == "upper-center":
+            self.x_offset, self.y_offset = self.x_size/2, 0
+        elif offset == "upper-right":
+            self.x_offset, self.y_offset = self.x_size, 0
+        elif offset == "middle-left":
+            self.x_offset, self.y_offset = 0, self.y_size/2
+        elif offset == "middle-right":
+            self.x_offset, self.y_offset = self.x_size, self.y_size/2
+        elif offset == "lower-left":
+            self.x_offset, self.y_offset = 0, self.y_size
+        elif offset == "lower-center":
+            self.x_offset, self.y_offset = self.x_size/2, self.y_size
+        elif offset == "lower-right":
+            self.x_offset, self.y_offset = self.x_size, self.y_size
+        elif offset == "":
+            self.x_offset, self.y_offset = self.x_size, self.y_size
+        else:
+            self.x_offset, self.y_offset = offset
+
+        self.collision_shape.x = self.x_offset
+        self.collision_shape.y = self.y_offset
+
     def animate(self):
         self.timer -= delta_time
         if self.timer <= 0:
             if self.current_x_frame < self.x_frames:
                 self.current_x_frame += 1
             elif self.current_y_frame < self.y_frames:
                 self.current_x_frame = 0
                 self.current_y_frame += 1
             else:
                 self.current_y_frame = 0
                 self.current_x_frame = 0
             self.timer = 1/self.speed
+    
+    def update_collision_shape(self, x, y):
+        self.collision_shape.x = x-self.x_offset
+        self.collision_shape.y = y-self.y_offset
+
+        return self.collision_shape
 
 class Camera():
     def __init__(self):
         self.x = 0
         self.y = 0
 
+class Console():
+    def __init__(self):
+        self.text = ""
+        self.opened = False
+    
+    def display(self):
+        if self.opened:
+            screen.blit(debug_font.render(">>"+self.text, True, (255, 255, 255)), (0, 0))
+    
+    def switch(self):
+        if self.opened:
+            self.opened = False
+            self.text = ""
+        else:
+            self.opened = True
+    
+    def input(self, key, unicode):
+
+        if key == pygame.K_F10 and settings["enable_console"]:
+            self.switch()
+            key = ""
+        
+        if self.opened:
+            self.text += unicode
+        if key == pygame.K_RETURN:
+            try:
+                exec(self.text)
+                self.text = ""
+            except:
+                print("Something went wrong")
+        elif key == pygame.K_BACKSPACE:
+            self.delete_from_end()
+    
+    def delete_from_end(self):
+        if len(self.text) > 0:
+            self.text = self.text[:-2]
+        
+
 #game settings
-version = "Alpha 1.0.5" #nie gotowa
 settings = {
-    "screen_size": (1200, 700),
+    "window_size": (1200, 700),
+    #"screen_size": None,
     "window_title": "pygameHat "+version,
     "fullscreen": False,
     "icon": None,
     "enable_console": True,
     "fps": 60,
 
     "shameless_ad": True,
 }
 
+#pygame.surfarray.make_surface()
 temp_icon = pygame.surface.Surface((10, 10))
 temp_icon.fill((255, 0, 255))
 
 #first initializations
 debug_font = pygame.font.Font(None, 25)
 title_font = pygame.font.Font(None, 100)
 console_opened = False
-console = TextFormat()
+console = Console()
 delta_time = 0
 
-screen = pygame.surface.Surface(settings["screen_size"])
+
+screen_size = settings["window_size"]
+screen = pygame.surface.Surface(screen_size)
 camera = Camera()
 
 current_room = Room()
 
 def init():
-    #TODO: Set camera focal length
-    global screen
+    global screen, screen_size
 
-    monitor = pygame.display.set_mode(settings["screen_size"])
+    monitor = pygame.display.set_mode(settings["window_size"])
+    screen_size = settings["window_size"]
 
     if settings["shameless_ad"]:
         pygame.display.set_icon(temp_icon)
         pygame.display.set_caption(settings["window_title"])
         screen.blit(title_font.render("Made with Pygame Hat", True, (255, 255, 255)), (100, 100))
         screen.blit(title_font.render(version, True, (255, 255, 255)), (100, 200))
         screen.blit(title_font.render("OWO", True, (255, 255, 255)), (100, 400))
     
-        screen = pygame.transform.scale(screen, settings["screen_size"]).convert()
+        screen = pygame.transform.scale(screen, screen_size).convert()
         monitor.blit(screen, (0, 0))
         pygame.display.flip()
         time.sleep(1.5)
+    screen = pygame.surface.Surface(screen_size)
 
 def close():
     pygame.quit()
     sys.exit(0)
 
 def add_object_instance(x, y, object, layer):
     object.x = x
     object.y = y
     current_room.layers[layer].append(object)
 
 def collide_objects(object1, object2):
     if object1 != object2 and object1.sprite and object1.sprite.collision and object2.sprite and object2.sprite.collision:
-        object1_shape = object1.sprite.collision_shape
-        object1_shape.x = object1.x
-        object1_shape.y = object1.y
-        object2_shape = object2.sprite.collision_shape
-        object2_shape.x = object2.x
-        object2_shape.y = object2.y
+        object1_shape = object1.sprite.update_collision_shape(object1.x, object1.y)
+        object2_shape = object2.sprite.update_collision_shape(object2.x, object2.y)
         if object1_shape.colliderect(object2_shape):
             return object2
+
 def collide_point(point, object):
     pointX, pointY = point
     pointX += camera.x
     pointY += camera.y
 
     if object.sprite and object.sprite.collision:
         object_shape = object.sprite.collision_shape
         object_shape.x = object.x
         object_shape.y = object.y
 
         if object_shape.collidepoint((pointX, pointY)):
             return object
 
+def screen_position_to_ingame_position(position):
+    pX, pY = position
+
+    pX += camera.x
+    pY += camera.y
+
+    return (pX, pY)
+
 def destroy_object(object):
     for layer in current_room.layers:
         for instance in current_room.layers[layer]:
             if object == instance:
                 current_room.layers[layer].remove(instance)
 
 def draw_sprite(sprite, x, y):
         if sprite:
-            screen.blit(sprite.index, (x-camera.x, y-camera.y), (sprite.x_size*sprite.current_x_frame, sprite.y_size*sprite.current_y_frame, sprite.x_size, sprite.y_size))
+            screen.blit(sprite.index, (x-camera.x-sprite.x_offset, y-camera.y-sprite.y_offset), (sprite.x_size*sprite.current_x_frame, sprite.y_size*sprite.current_y_frame, sprite.x_size, sprite.y_size))
             sprite.animate()
 
 def change_room(room):
     global current_room
 
     current_room = room
 
-#debug fuctions
-def switch_console():
-    global console_opened
-    
-    if console_opened:
-        console_opened = False
-        console.clear()
-    else:
-        console_opened = True
 
 def start():
     timeB = 0
     global delta_time
-    global screen
+    global screen, screen_size
 
     if settings["fullscreen"]:
-        monitor = pygame.display.set_mode(settings["screen_size"], pygame.FULLSCREEN)
+        monitor = pygame.display.set_mode(settings["window_size"], pygame.FULLSCREEN)
     else:
-        monitor = pygame.display.set_mode(settings["screen_size"], pygame.RESIZABLE)
+        monitor = pygame.display.set_mode(settings["window_size"], pygame.RESIZABLE)
 
     pygame.display.set_caption(settings["window_title"])
     if settings["icon"]:
         pygame.display.set_icon(pygame.image.load(settings["icon"]))
     else:
         pygame.display.set_icon(temp_icon)
 
@@ -211,39 +271,29 @@
 
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 quit()
             
             elif event.type == pygame.KEYDOWN:
                 #console management
-                if console_opened:
-                    console.text += event.unicode
-                    if event.key == pygame.K_RETURN:
-                        try:
-                            exec(console.text)
-                            console.clear()
-                        except:
-                            print("Something went wrong")
-                    elif event.key == pygame.K_BACKSPACE:
-                        console.delete_from_end()
-                if event.key == pygame.K_F10 and settings["enable_console"]:
-                    switch_console()
+                console.input(event.key, event.unicode)
+
                 #handling keypresses for objects
                 for layer in current_room.layers:
                     for instance in current_room.layers[layer]:
                         instance.key_just_pressed(event.key)
 
             elif event.type == pygame.KEYUP:
                 #handling keyups for objects
                 for layer in current_room.layers:
                     for instance in current_room.layers[layer]:
                         instance.key_just_released(event.key)
             
             elif event.type == pygame.VIDEORESIZE:
-                settings["screen_size"] = (event.w, event.h)
+                screen_size = (event.w, event.h)
 
         #background                
         if type(current_room.background) == Sprite:
             draw_sprite(current_room.background, 0, 0)
         else:
             screen.fill(current_room.background)
     
@@ -255,13 +305,12 @@
                 instance.step()
                 #collision processing
                 for layer2 in current_room.layers:
                     for instance2 in current_room.layers[layer2]:
                         obj = collide_objects(instance, instance2)
                         if obj:
                             instance.is_colliding(obj)
-        #console rendering
-        if console_opened:
-            screen.blit(debug_font.render(">>"+console.text, True, (255, 255, 255)), (0, 0))
+        
+        console.display()
 
-        monitor.blit(pygame.transform.scale(screen, settings["screen_size"]), (0, 0))
+        monitor.blit(pygame.transform.scale(screen, screen_size), (0, 0))
         pygame.display.flip()
```

### Comparing `pygameHat-1.0.5/pygameHat.egg-info/PKG-INFO` & `pygameHat-1.0.6/pygameHat.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: pygameHat
-Version: 1.0.5
+Version: 1.0.6
 Summary: Pygame game-making engine
 Home-page: UNKNOWN
 Author: Wojciech Błajda
 Author-email: <mail@mail.com>
 License: UNKNOWN
 Description: UNKNOWN
 Keywords: python,engine,pygame
```

### Comparing `pygameHat-1.0.5/setup.py` & `pygameHat-1.0.6/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 import codecs
 import os
 
-VERSION = '1.0.5'
+VERSION = '1.0.6'
 DESCRIPTION = 'Pygame game-making engine'
 
 # Setting up
 setup(
     name="pygameHat",
     version=VERSION,
     author="Wojciech Błajda",
```

