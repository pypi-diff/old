# Comparing `tmp/Miniengine-0.0.6.tar.gz` & `tmp/Miniengine-1.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Miniengine-0.0.6.tar", last modified: Fri Mar 31 17:59:38 2023, max compression
+gzip compressed data, was "Miniengine-1.0.0.tar", last modified: Thu Apr  6 23:21:07 2023, max compression
```

## Comparing `Miniengine-0.0.6.tar` & `Miniengine-1.0.0.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxr-xr-x   0 Rafa       (502) staff       (20)        0 2023-03-31 17:59:38.993458 Miniengine-0.0.6/
-drwxr-xr-x   0 Rafa       (502) staff       (20)        0 2023-03-31 17:59:38.992313 Miniengine-0.0.6/Miniengine/
--rw-r--r--   0 Rafa       (502) staff       (20)    15690 2023-03-31 17:57:38.000000 Miniengine-0.0.6/Miniengine/__init__.py
-drwxr-xr-x   0 Rafa       (502) staff       (20)        0 2023-03-31 17:59:38.992956 Miniengine-0.0.6/Miniengine.egg-info/
--rw-r--r--   0 Rafa       (502) staff       (20)      980 2023-03-31 17:59:38.000000 Miniengine-0.0.6/Miniengine.egg-info/PKG-INFO
--rw-r--r--   0 Rafa       (502) staff       (20)      177 2023-03-31 17:59:38.000000 Miniengine-0.0.6/Miniengine.egg-info/SOURCES.txt
--rw-r--r--   0 Rafa       (502) staff       (20)        1 2023-03-31 17:59:38.000000 Miniengine-0.0.6/Miniengine.egg-info/dependency_links.txt
--rw-r--r--   0 Rafa       (502) staff       (20)       11 2023-03-31 17:59:38.000000 Miniengine-0.0.6/Miniengine.egg-info/top_level.txt
--rw-r--r--   0 Rafa       (502) staff       (20)      980 2023-03-31 17:59:38.993177 Miniengine-0.0.6/PKG-INFO
--rw-r--r--   0 Rafa       (502) staff       (20)        0 2023-03-28 22:40:15.000000 Miniengine-0.0.6/README.md
--rw-r--r--   0 Rafa       (502) staff       (20)       38 2023-03-31 17:59:38.993520 Miniengine-0.0.6/setup.cfg
--rw-r--r--   0 Rafa       (502) staff       (20)     1202 2023-03-31 17:57:49.000000 Miniengine-0.0.6/setup.py
+drwxr-xr-x   0 Rafa       (502) staff       (20)        0 2023-04-06 23:21:07.467993 Miniengine-1.0.0/
+drwxr-xr-x   0 Rafa       (502) staff       (20)        0 2023-04-06 23:21:07.466857 Miniengine-1.0.0/Miniengine/
+-rw-r--r--   0 Rafa       (502) staff       (20)    17232 2023-04-06 23:19:59.000000 Miniengine-1.0.0/Miniengine/__init__.py
+drwxr-xr-x   0 Rafa       (502) staff       (20)        0 2023-04-06 23:21:07.467527 Miniengine-1.0.0/Miniengine.egg-info/
+-rw-r--r--   0 Rafa       (502) staff       (20)      980 2023-04-06 23:21:07.000000 Miniengine-1.0.0/Miniengine.egg-info/PKG-INFO
+-rw-r--r--   0 Rafa       (502) staff       (20)      177 2023-04-06 23:21:07.000000 Miniengine-1.0.0/Miniengine.egg-info/SOURCES.txt
+-rw-r--r--   0 Rafa       (502) staff       (20)        1 2023-04-06 23:21:07.000000 Miniengine-1.0.0/Miniengine.egg-info/dependency_links.txt
+-rw-r--r--   0 Rafa       (502) staff       (20)       11 2023-04-06 23:21:07.000000 Miniengine-1.0.0/Miniengine.egg-info/top_level.txt
+-rw-r--r--   0 Rafa       (502) staff       (20)      980 2023-04-06 23:21:07.467741 Miniengine-1.0.0/PKG-INFO
+-rw-r--r--   0 Rafa       (502) staff       (20)        0 2023-03-28 22:40:15.000000 Miniengine-1.0.0/README.md
+-rw-r--r--   0 Rafa       (502) staff       (20)       38 2023-04-06 23:21:07.468048 Miniengine-1.0.0/setup.cfg
+-rw-r--r--   0 Rafa       (502) staff       (20)     1202 2023-04-06 23:20:27.000000 Miniengine-1.0.0/setup.py
```

### Comparing `Miniengine-0.0.6/Miniengine/__init__.py` & `Miniengine-1.0.0/Miniengine/__init__.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,148 +1,141 @@
 import math
 import pygame
+import time
+
 class Simulation():
-    def __init__(self, width, height, tittle, collisions, dt, steps, speed):
+    def __init__(self, width, height, tittle, collisions = False):
         self.width = width
         self.height = height
         self.tittle = tittle
         self.objects = []
         self.positions_history = []
-        self.dt = dt
         self.collisions = collisions
-        self.steps = steps
-        self.speed = round((speed*1.7)/(dt*100))
         self.gravity_objects = []
         self.collisionLayers = []
     def add_object(self, obj):
         self.objects.append(obj)
         for object in self.objects:
             if object.collisionLayer != 0:
                 self.collisionLayers.append(object.collisionLayer)
             if object.gravity:
                 self.gravity_objects.append(object)
     def store_positions(self):
         current_positions = []
         for obj in self.objects:
             current_positions.append([obj, obj.position])
         self.positions_history.append(current_positions)
-    def run(self, fps=60, frames='all'):
+    def run(self, speed=1, fps=60, frames='all'):
         if frames == 'all': frames = len(self.positions_history)
         display = pygame.display.set_mode((self.width, self.height))
         pygame.display.set_caption(self.tittle)
         frame = 0
         clock = pygame.time.Clock()
+        tempo = time.time()
+        x = 0
         for objects in self.positions_history[:frames]:
-            display.fill('dark green')
-            for object in objects:
-                object[0].position = object[1]
-                if object[0].circle:
-                    pygame.draw.circle(display, object[0].color, object[0].position, object[0].width/2)
-                else:
-                    display.blit(object[0].body, (object[0].position))
-            pygame.display.update()
-            clock.tick(fps)
-            for event in pygame.event.get():
-                if event.type == pygame.QUIT:
-                    pygame.quit()
-            frame += 1
-    def calculate(self):
-        y =0
-        for i in range(self.steps):
+            if x == round((self.lenght/self.dt)/(fps*self.lenght/speed)):
+                x=0
+                display.fill('dark green')
+                for object in objects:
+                    object[0].position = object[1]
+                    if object[0].circle:
+                        pygame.draw.circle(display, object[0].color, object[0].position, object[0].width/2)
+                    else:
+                        display.blit(object[0].body, (object[0].position))
+                pygame.display.update()
+                clock.tick(fps)
+                for event in pygame.event.get():
+                    if event.type == pygame.QUIT:
+                        pygame.quit()
+                    frame += 1
+            x+=1
+    def calculate(self, lenght, dt):
+        self.lenght = lenght
+        self.dt = dt
+        self.steps = round(lenght/dt)
+        for q in range(self.steps):
             if self.collisions: 
                 for i in range(len(self.objects)):
                     object1 = self.objects[i]
                     for j in range(i + 1, len(self.objects)):
                         object2 = self.objects[j]
                         if object1.collisionLayer == object2.collisionLayer:
                             if checkCollision(object1, object2):
                                 Collide(object1, object2)
-            for i in range(len(self.gravity_objects)):
-                object1 = self.gravity_objects[i]
-                for j in range(i + 1, len(self.gravity_objects)):
-                    object2 = self.gravity_objects[j]
-                    if object1 != object2:
-                        gravitate(object1, object2)
-            
+            calculate_gravity(self.gravity_objects, dt)
             for object in self.objects:
                 if not object.locked:
-                    object.updatePosition()
+                    object.updatePosition(dt)
                 if object.dV != 0:
-                    print(object.position)
-                    object.accelerate()
+                    object.accelerate(dt)
                 if object.hitBorder:
                     border(object)
-            if y == self.speed:
-                self.store_positions()
-                y = 0
-            y += 1
+            self.store_positions()
+
+
+
 class Object(pygame.Surface):
-    def __init__(self, height, width, position, mass, speed, direction, color, simulation,circle=False, collisionLayer=0, hitBorder=False):
+    def __init__(self, width, height, position, mass, speed, direction, color, simulation,circle=False, COR = 1, collisionLayer=0, hitBorder=False):
         self.height = height
         self.width = width
         self.gravity = False
-        self.downGravity = False
-        self.dt = simulation.dt
         self.position = position
         self.circle = circle
         self.mass = mass
         self.speed = speed
-        self.simpleGravity = False
         self.color = color
         self.hitBorder = hitBorder
         self.collisionLayer = collisionLayer
         self.direction = direction
         self.simulation = simulation
+        self.COR = COR
         self.body = pygame.Surface((self.width, self.height))
         self.body.fill(color)
         self.dV = 0
+        simulation.add_object(self)
         self.locked = False
         self.angle = 0
     def lockPos(self):
         self.locked = True
-    def addGravity(self, g=0, downGravity=False, simpleGravity=False, lock=False):
-        if g != 0:
-            self.gravity = True
-        self.lock = lock
+    def addGravity(self, g=0):
+        self.gravity = True
         self.g = g
-        self.simpleGravity = simpleGravity
-        if downGravity:
-            self.dV = 9.8
-            self.angle =90
-    def updatePosition(self):
+    def addAceleration(self, dV, angle):
+        self.dV = dV
+        self.angle = angle
+    def updatePosition(self, dt):
         x, y = self.position
         radians = math.radians(self.direction)
         dx = self.speed * math.cos(radians)
         dy = self.speed * math.sin(radians)
-        new_x = x + dx * self.dt
-        new_y = y + dy * self.dt
+        new_x = x + dx * dt
+        new_y = y + dy * dt
         self.position = (new_x, new_y)
 
-    def accelerate(self):
+    def accelerate(self, dt):
         directionRad = math.radians(self.direction)
 
         # Calculate the object's current x and y velocity components
         speedX = self.speed * math.cos(directionRad)
         speedY = self.speed * math.sin(directionRad)
 
         # Calculate the x and y components of the speed_change
         DeltaVX = self.dV * math.cos(math.radians(self.angle - math.pi))
         DeltaVY = self.dV * math.sin(math.radians(self.angle - math.pi))
 
-        print(self.dV)
         # Add the speed_change components to the current speed components
-        new_speedX = speedX + DeltaVX*self.dt
-        new_speedY = speedY + DeltaVY*self.dt
+        new_speedX = speedX + DeltaVX*dt
+        new_speedY = speedY + DeltaVY*dt
 
         # Calculate the new speed and direction
         new_speed = math.sqrt(new_speedX ** 2 + new_speedY ** 2)
         new_direction = math.degrees(math.atan2(new_speedY, new_speedX))
 
         # Update the object's speed and direction
-        print("Speed: ", new_speed)
         self.speed = new_speed
         self.direction = new_direction
 def angle_difference(angle1, angle2):
     diff = (angle1 - angle2) % 360
     return diff if diff < 180 else 360 - diff
 def checkCollision(object1, object2):
     if object1.circle and object2.circle:
@@ -154,86 +147,127 @@
         object1.position[0] + object1.width > object2.position[0]):
         
         # Check if the rectangles are overlapping along the y-axis
             if (object1.position[1] < object2.position[1] + object2.height and object1.position[1] + object1.height > object2.position[1]):
             
             # The rectangles are overlapping
                 return True
-
     # The rectangles are not overlapping
         return False
-
 def border(object):
-    print(1)
     x, y = object.position
-    x += object.width/2
-    y += object.height/2
     if object.circle:
-        x, y = object.position
-        radius = object.width // 2
+        radius = object.width / 2
         # Check collision with left or right border
-        if x - radius <= 0 or x + radius >= object.simulation.width:
+        if x - radius < 0:
+            object.position = list(object.position)
             object.direction = 180 - object.direction
-
-        # Check collision with top or bottom border
-        if y - radius <= 0 or y + radius >= object.simulation.height:
-            object.direction = 360 - object.direction
+            object.position[0] = (object.width/2)
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
+        if x + radius > object.simulation.width:
+            object.position = list(object.position)
+            object.direction = 180 - object.direction
+            object.position[0] = (object.simulation.width -object.width/2)
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
+
+        if y - radius < 0:
+            object.position = list(object.position)
+            object.direction = -object.direction
+            object.position[1] = (object.width/2)
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
+        
+        if y+ radius > object.simulation.height:
+            object.position = list(object.position)
+            object.direction = -object.direction
+            object.position[1] = (object.simulation.height -object.width/2)-1
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
     else:
-        object_width, object_height = object.width, object.height
-        if x <= object_width/2 or x + object_width/2 >= object.simulation.width:
+        # Check collision with left or right border
+        if x < 0:
+            object.position = list(object.position)
             object.direction = 180 - object.direction
-        if y <= object_width/2 or y + object_height/2 >= object.simulation.height:
-            object.direction = 360 - object.direction
-
+            object.position[0] = 0
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
+        if x+object.width > object.simulation.width:
+            object.position = list(object.position)
+            object.direction = 180 - object.direction
+            object.position[0] = (object.simulation.width -object.width)
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
+
+        if y < 0:
+            object.position = list(object.position)
+            object.direction = -object.direction
+            object.position[1] = 0
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
+        
+        if y+object.height > object.simulation.height:
+            object.position = list(object.position)
+            object.direction = -object.direction
+            object.position[1] = (object.simulation.height -object.height)-1
+            object.speed *= object.COR
+            if abs(object.speed) < 0.1:
+                object.speed = 0
+            object.position = tuple(object.position)
+        
 
-def gravitate(object1, object2):
+def calculate_gravity(objects, dt):
+    """
+    Calculates the effect of gravity on each object and updates its speed and direction.
+    """
     
+    for i, object1 in enumerate(objects):
+        net_force_x, net_force_y = 0, 0
+        
+        for j, object2 in enumerate(objects):
+            if i == j:
+                continue
+            
+            dx = object2.position[0] - object1.position[0]
+            dy = object2.position[1] - object1.position[1]
+            dist = math.sqrt(dx ** 2 + dy ** 2)+0.000001
+            force = ((object1.g+object2.g)/2) * object1.mass * object2.mass / dist ** 2
+            
+            net_force_x += force * (dx / dist)*1000
+            net_force_y += force * (dy / dist)*1000
 
-    dx = (object2.position[0] - object2.width) - (object1.position[0] - object1.width)
-    dy = (object2.position[1] - object2.height) - (object1.position[1] - object1.height)
-
-    distance = math.sqrt(dx ** 2 + dy ** 2)
-    force = ((object1.g+object2.g)/2) * object1.mass * object2.mass / (distance ** 2)
-
-    # Calculate the unit vector in the direction from object1 to object2
-    unit_vector_x = dx / distance
-    unit_vector_y = dy / distance
-
-    # Calculate the force components acting on each object
-    force_x = force * unit_vector_x*10000
-    force_y = force * unit_vector_y*10000
-
-    # Update the velocities of both objects based on the time interval dt
-
-    if not object1.lock:
-
-        object1_speed_x = object1.speed * math.cos(math.radians(object1.direction))
-        object1_speed_y = object1.speed * math.sin(math.radians(object1.direction))
-        object1_speed_x += (force_x / object1.mass) * object1.dt
-        object1_speed_y += (force_y / object1.mass) * object1.dt
-        object1.speed = math.sqrt(object1_speed_x ** 2 + object1_speed_y ** 2)
-        object1.direction = math.degrees(math.atan2(object1_speed_y, object1_speed_x))
-
-    if not object2.lock:
-        print(force_x, force_y)
-        object2_speed_x = object2.speed * math.cos(math.radians(object2.direction))
-        object2_speed_y = object2.speed * math.sin(math.radians(object2.direction))
-        object2_speed_x -= (force_x / object2.mass) * object2.dt
-        object2_speed_y -= (force_y / object2.mass) * object2.dt
-        object2.speed = math.sqrt(object2_speed_x ** 2 + object2_speed_y ** 2)
-        object2.direction = math.degrees(math.atan2(object2_speed_y, object2_speed_x))
-
-
+            object1_speed_x = object1.speed * math.cos(math.radians(object1.direction))
+            object1_speed_y = object1.speed * math.sin(math.radians(object1.direction))
+            object1_speed_x += (net_force_x / object1.mass) * dt
+            object1_speed_y += (net_force_y / object1.mass) * dt
+            object1.speed = math.sqrt(object1_speed_x ** 2 + object1_speed_y ** 2)
+            object1.direction = math.degrees(math.atan2(object1_speed_y, object1_speed_x))
 def distance(objeto1, objeto2):
     x1, y1 = objeto1.position
     x2, y2 = objeto2.position
     dx = x2 - x1
     dy = y2 - y1
     return math.sqrt(dx ** 2 + dy ** 2)
-def Collide(object1, object2, COR=0.7):
+def Collide(object1, object2):
+    COR = object1.COR*object2.COR
     x1, y1 = object1.position
     x2, y2 = object2.position
     if not object1.circle:
         x1 += object1.width/2
         y1 += object1.height/2
     if not object2.circle:
         x2 += object2.width/2
@@ -294,27 +328,31 @@
 
         # Calculate the sum of the radii of the two circles, plus one unit of distance
         radius_sum = (object1.width / 2) + (object2.width / 2)
 
         # Check if the circles are overlapping or touching
         if distance < radius_sum:
             # Calculate the overlap distance, plus one unit of distance
-            overlap = radius_sum - distance
+            overlap = (radius_sum - distance)+0.1
 
             # Calculate the unit vector in the direction from circle1 to circle2
-            unit_vector_x = dx / distance
-            unit_vector_y = dy / distance
+            try:
+                unit_vector_x = dx / distance
+                unit_vector_y = dy / distance
+            except:
+                print("Error: object1 = {}, object2 = {}, distance = {}".format(object1.position, object2.position, distance))
+                raise
 
             # Move the circles apart by half the overlap distance each, in opposite directions
             object1.position = list(object1.position)
             object2.position = list(object2.position)
-            object1.position[0] -= (unit_vector_x * (overlap / 2)+0.0)
-            object1.position[1] -= (unit_vector_y * (overlap / 2)+0.0)
-            object2.position[0] += (unit_vector_x * (overlap / 2)+0.0)
-            object2.position[1] += (unit_vector_y * (overlap / 2)+0.0)
+            object1.position[0] -= (unit_vector_x * (overlap / 2))
+            object1.position[1] -= (unit_vector_y * (overlap / 2))
+            object2.position[0] += (unit_vector_x * (overlap / 2))
+            object2.position[1] += (unit_vector_y * (overlap / 2))
             object1.position = tuple(object1.position)
             object2.position = tuple(object2.position)
     elif object1.circle == object2.circle:
         # Check if the rectangles are overlapping along the x-axis
         if (object1.position[0] < object2.position[0] + object2.width and
             object1.position[0] + object1.width > object2.position[0]):
```

### Comparing `Miniengine-0.0.6/Miniengine.egg-info/PKG-INFO` & `Miniengine-1.0.0/Miniengine.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Miniengine
-Version: 0.0.6
+Version: 1.0.0
 Summary: Engine for pygame
 Home-page: https://github.com/rrayes3110/Mini-Engine
 Author: Rafael Rayes
 Author-email: rafa@rayes.com.br
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `Miniengine-0.0.6/PKG-INFO` & `Miniengine-1.0.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Miniengine
-Version: 0.0.6
+Version: 1.0.0
 Summary: Engine for pygame
 Home-page: https://github.com/rrayes3110/Mini-Engine
 Author: Rafael Rayes
 Author-email: rafa@rayes.com.br
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `Miniengine-0.0.6/setup.py` & `Miniengine-1.0.0/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name='Miniengine',
-    version='0.0.6',
+    version='1.0.0',
     author='Rafael Rayes',
     author_email='rafa@rayes.com.br',
     description='Engine for pygame',
     long_description='''
    # Miniengine
 
 Miniengine is a simple physics simulation library built on top of Pygame. It allows users to simulate the motion of objects, calculate collisions, and visualize the results. The library includes the `MiniEngine` module for handling physics calculations, and the `Renderer` class for rendering and displaying the simulations.
```

