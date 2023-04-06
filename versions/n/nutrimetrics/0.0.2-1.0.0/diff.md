# Comparing `tmp/nutrimetrics-0.0.2.tar.gz` & `tmp/nutrimetrics-1.0.0.tar.gz`

## Comparing `nutrimetrics-0.0.2.tar` & `nutrimetrics-1.0.0.tar`

### file list

```diff
@@ -1,88 +1,161 @@
--rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/.DS_Store
--rw-r--r--   0        0        0      725 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/.gitignore
--rw-r--r--   0        0        0     1090 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/LICENSE
--rw-r--r--   0        0        0     5398 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/README.md
--rw-r--r--   0        0        0     1171 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/pyproject.toml
--rw-r--r--   0        0        0   162074 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/report.png
--rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/.DS_Store
--rw-r--r--   0        0        0      128 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/__about__.py
--rw-r--r--   0        0        0      106 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/__init__.py
--rw-r--r--   0        0        0     2877 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/cli.py
--rw-r--r--   0        0        0     1238 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/config.py
--rw-r--r--   0        0        0     2930 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/food_data_central.py
--rw-r--r--   0        0        0     6220 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/meals.py
--rw-r--r--   0        0        0     5373 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/nutrients.py
--rw-r--r--   0        0        0     1015 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/units.py
--rw-r--r--   0        0        0    14021 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/workbook.py
--rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/.DS_Store
--rw-r--r--   0        0        0     3655 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/config.json
--rw-r--r--   0        0        0     1705 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/almond_170567.json
--rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/almond_butter_168588.json
--rw-r--r--   0        0        0     1769 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/apple_171688.json
--rw-r--r--   0        0        0     1588 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/apple_cider_vinegar_173469.json
--rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/apricot_171697.json
--rw-r--r--   0        0        0     1761 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/asparagus_168389.json
--rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/avocado_171705.json
--rw-r--r--   0        0        0     1726 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/banana_173944.json
--rw-r--r--   0        0        0     1789 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/beef_ground_80-20_174036.json
--rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/beef_ground_90-10_174030.json
--rw-r--r--   0        0        0     1699 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/beetroot_169145.json
--rw-r--r--   0        0        0     1608 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_green_2258588.json
--rw-r--r--   0        0        0     1638 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_orange_2258591.json
--rw-r--r--   0        0        0     1653 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_red_2258590.json
--rw-r--r--   0        0        0     1616 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_yellow_2258589.json
--rw-r--r--   0        0        0     1733 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/blueberry_171711.json
--rw-r--r--   0        0        0     1696 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/brewed_coffee_171890.json
--rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/broccoli_170379.json
--rw-r--r--   0        0        0     1744 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/brussels_sprout_170383.json
--rw-r--r--   0        0        0     1742 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/butter_173430.json
--rw-r--r--   0        0        0     1784 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/carrot_170393.json
--rw-r--r--   0        0        0     1708 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/cauliflower_169986.json
--rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/cheddar_cheese_173414.json
--rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/chicken_breast_171077.json
--rw-r--r--   0        0        0     1639 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/clementine_168195.json
--rw-r--r--   0        0        0     1727 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/cocoa_powder_169593.json
--rw-r--r--   0        0        0     1676 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/coconut_meat_170169.json
--rw-r--r--   0        0        0     1691 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/coconut_water_170174.json
--rw-r--r--   0        0        0     1668 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/egg_white_172183.json
--rw-r--r--   0        0        0     1752 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/egg_yolk_172184.json
--rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/flaxseed_169414.json
--rw-r--r--   0        0        0     1697 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/garlic_169230.json
--rw-r--r--   0        0        0     1605 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/grape_tomato_321360.json
--rw-r--r--   0        0        0     1655 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/greek_yogurt_whole_milk_2259794.json
--rw-r--r--   0        0        0     1662 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/green_olive_169096.json
--rw-r--r--   0        0        0     1756 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/heavy_cream_170859.json
--rw-r--r--   0        0        0     1659 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/honey_169640.json
--rw-r--r--   0        0        0     1600 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/lemon_167746.json
--rw-r--r--   0        0        0     1750 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/lettuce_romaine_169247.json
--rw-r--r--   0        0        0     1696 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/macadamia_nut_170178.json
--rw-r--r--   0        0        0     1680 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/oat_rolled_2346396.json
--rw-r--r--   0        0        0     1656 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/oat_steel_cut_2346397.json
--rw-r--r--   0        0        0     1599 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/olive_oil_171413.json
--rw-r--r--   0        0        0     1815 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/oyster_eastern_171978.json
--rw-r--r--   0        0        0     1767 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/oyster_pacific_174219.json
--rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/pecan_nut_170182.json
--rw-r--r--   0        0        0     1714 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/pistachio_170184.json
--rw-r--r--   0        0        0     1744 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/pork_bacon_167914.json
--rw-r--r--   0        0        0     1702 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/salmon_atlantic_173686.json
--rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/salmon_sockeye_173691.json
--rw-r--r--   0        0        0     1553 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/salt_173468.json
--rw-r--r--   0        0        0     1814 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/sardine_175139.json
--rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/sauerkraut_169279.json
--rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/scallion_170005.json
--rw-r--r--   0        0        0     1772 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/spinach_168462.json
--rw-r--r--   0        0        0     1722 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/strawberry_167762.json
--rw-r--r--   0        0        0     1806 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/sweet_potato_168482.json
--rw-r--r--   0        0        0     1708 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/tuna_bluefin_173706.json
--rw-r--r--   0        0        0     1700 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/tuna_skipjack_175156.json
--rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/tuna_yellowfin_175159.json
--rw-r--r--   0        0        0     1751 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/turmeric_172231.json
--rw-r--r--   0        0        0     1713 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/wakame_seaweed_170496.json
--rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/walnut_170187.json
--rw-r--r--   0        0        0     1782 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/whole_milk_171265.json
--rw-r--r--   0        0        0     1719 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/yogurt_whole_milk_171284.json
--rw-r--r--   0        0        0     1778 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/foods/zucchini_169291.json
--rw-r--r--   0        0        0     3466 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/samples/foods.json
--rw-r--r--   0        0        0     1449 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/nutrimetrics/resources/samples/meal_plan.json
--rw-r--r--   0        0        0      725 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/.gitignore
--rw-r--r--   0        0        0     7431 2020-02-02 00:00:00.000000 nutrimetrics-0.0.2/PKG-INFO
+-rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/.DS_Store
+-rw-r--r--   0        0        0      725 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/.gitignore
+-rw-r--r--   0        0        0     1090 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/LICENSE
+-rw-r--r--   0        0        0     6226 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/README.md
+-rw-r--r--   0        0        0     1171 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/pyproject.toml
+-rw-r--r--   0        0        0   209127 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/report.png
+-rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/.DS_Store
+-rw-r--r--   0        0        0      128 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/__about__.py
+-rw-r--r--   0        0        0      106 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/__init__.py
+-rw-r--r--   0        0        0     3159 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/cli.py
+-rw-r--r--   0        0        0     2848 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/config.py
+-rw-r--r--   0        0        0     3123 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/food_data_central.py
+-rw-r--r--   0        0        0     6689 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/meals.py
+-rw-r--r--   0        0        0     5373 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/nutrients.py
+-rw-r--r--   0        0        0     1015 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/units.py
+-rw-r--r--   0        0        0    16648 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/workbook.py
+-rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/.DS_Store
+-rw-r--r--   0        0        0     3465 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/config.json
+-rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/dri/ear-female.json
+-rw-r--r--   0        0        0     1073 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/dri/ear-male.json
+-rw-r--r--   0        0        0     1075 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/dri/rda-female.json
+-rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/dri/rda-male.json
+-rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/.DS_Store
+-rw-r--r--   0        0        0     1705 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/almond_170567.json
+-rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/almond_butter_168588.json
+-rw-r--r--   0        0        0     1732 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/almond_milk_2257045.json
+-rw-r--r--   0        0        0     1690 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/apple_171689.json
+-rw-r--r--   0        0        0     1588 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/apple_cider_vinegar_173469.json
+-rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/apricot_171697.json
+-rw-r--r--   0        0        0     1761 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/asparagus_168389.json
+-rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/avocado_171705.json
+-rw-r--r--   0        0        0     1533 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/balsamic_vinegar_172241.json
+-rw-r--r--   0        0        0     1726 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/banana_173944.json
+-rw-r--r--   0        0        0     1755 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/basil_172232.json
+-rw-r--r--   0        0        0     1789 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/beef_ground_80-20_174036.json
+-rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/beef_ground_90-10_174030.json
+-rw-r--r--   0        0        0     1699 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/beetroot_169145.json
+-rw-r--r--   0        0        0     1608 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_green_2258588.json
+-rw-r--r--   0        0        0     1638 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_orange_2258591.json
+-rw-r--r--   0        0        0     1653 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_red_2258590.json
+-rw-r--r--   0        0        0     1616 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_yellow_2258589.json
+-rw-r--r--   0        0        0     1745 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/black_bean_173734.json
+-rw-r--r--   0        0        0     1648 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/blackberry_173946.json
+-rw-r--r--   0        0        0     1733 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/blueberry_171711.json
+-rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/brazil_nut_170569.json
+-rw-r--r--   0        0        0     1696 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/brewed_coffee_171890.json
+-rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/broccoli_170379.json
+-rw-r--r--   0        0        0     1744 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/brussels_sprout_170383.json
+-rw-r--r--   0        0        0     1742 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/butter_173430.json
+-rw-r--r--   0        0        0     1768 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cabbage_169975.json
+-rw-r--r--   0        0        0     1732 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cantaloupe_169092.json
+-rw-r--r--   0        0        0     1784 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/carrot_170393.json
+-rw-r--r--   0        0        0     1708 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cauliflower_169986.json
+-rw-r--r--   0        0        0     2231 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cheddar_cheese_173414.json
+-rw-r--r--   0        0        0     1768 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cherry_171719.json
+-rw-r--r--   0        0        0     1668 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/chia_seed_170554.json
+-rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/chicken_breast_171077.json
+-rw-r--r--   0        0        0     1726 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/chickpea_173756.json
+-rw-r--r--   0        0        0     1474 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/chlorella_powder_1064099.json
+-rw-r--r--   0        0        0     1646 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cilantro_169997.json
+-rw-r--r--   0        0        0     1742 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cinnamon_171320.json
+-rw-r--r--   0        0        0     1639 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/clementine_168195.json
+-rw-r--r--   0        0        0     1727 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cocoa_powder_169593.json
+-rw-r--r--   0        0        0     1676 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/coconut_meat_170169.json
+-rw-r--r--   0        0        0     1691 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/coconut_water_170174.json
+-rw-r--r--   0        0        0     1715 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cranberry_171722.json
+-rw-r--r--   0        0        0     1634 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/cumin_seed_170923.json
+-rw-r--r--   0        0        0     1681 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/dark_chocolate_170273.json
+-rw-r--r--   0        0        0     1712 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/date_deglet_171726.json
+-rw-r--r--   0        0        0     1682 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/date_medjool_168191.json
+-rw-r--r--   0        0        0     2539 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/egg_omelet_172185.json
+-rw-r--r--   0        0        0     1668 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/egg_white_172183.json
+-rw-r--r--   0        0        0     1788 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/egg_whole_171287.json
+-rw-r--r--   0        0        0     1752 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/egg_yolk_172184.json
+-rw-r--r--   0        0        0      254 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/electrolyte_powder_berg.json
+-rw-r--r--   0        0        0     1664 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/fig_173021.json
+-rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/flaxseed_169414.json
+-rw-r--r--   0        0        0     1697 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/garlic_169230.json
+-rw-r--r--   0        0        0     1770 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/ginger_root_169231.json
+-rw-r--r--   0        0        0     1579 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/grape_muscadine_173040.json
+-rw-r--r--   0        0        0     1773 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/grapefruit_red_174673.json
+-rw-r--r--   0        0        0     1773 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/grapefruit_white_174676.json
+-rw-r--r--   0        0        0     2113 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/greek_yogurt_whole_milk_2259794.json
+-rw-r--r--   0        0        0     1787 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/green_bean_169961.json
+-rw-r--r--   0        0        0     1662 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/green_olive_169096.json
+-rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/gruyere_cheese_171242.json
+-rw-r--r--   0        0        0     1756 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/heavy_cream_170859.json
+-rw-r--r--   0        0        0     1690 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/hemp_seed_170148.json
+-rw-r--r--   0        0        0     1659 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/honey_169640.json
+-rw-r--r--   0        0        0     1664 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/jalapeno_168576.json
+-rw-r--r--   0        0        0     1737 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/kale_168421.json
+-rw-r--r--   0        0        0     1757 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/kiwifruit_168153.json
+-rw-r--r--   0        0        0     1732 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/laver_seaweed_168458.json
+-rw-r--r--   0        0        0     1726 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/leek_169246.json
+-rw-r--r--   0        0        0     1600 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/lemon_167746.json
+-rw-r--r--   0        0        0     1650 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/lemon_juice_167747.json
+-rw-r--r--   0        0        0     1730 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/lentil_172420.json
+-rw-r--r--   0        0        0     1750 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/lettuce_romaine_169247.json
+-rw-r--r--   0        0        0     1661 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/lime_168155.json
+-rw-r--r--   0        0        0     1696 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/macadamia_nut_170178.json
+-rw-r--r--   0        0        0     1748 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/mango_169910.json
+-rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/mushroom_maitake_169403.json
+-rw-r--r--   0        0        0     1756 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/mushroom_portabella_169255.json
+-rw-r--r--   0        0        0     1698 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/mushroom_shiitake_169242.json
+-rw-r--r--   0        0        0     1782 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/mushroom_white_169251.json
+-rw-r--r--   0        0        0      199 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/nusalt.json
+-rw-r--r--   0        0        0     1680 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/oat_rolled_2346396.json
+-rw-r--r--   0        0        0     1656 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/oat_steel_cut_2346397.json
+-rw-r--r--   0        0        0     1599 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/olive_oil_171413.json
+-rw-r--r--   0        0        0     1717 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/onion_170000.json
+-rw-r--r--   0        0        0     1712 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/orange_florida_169918.json
+-rw-r--r--   0        0        0     1798 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/orange_navel_169917.json
+-rw-r--r--   0        0        0     1674 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/orange_valencia_169916.json
+-rw-r--r--   0        0        0     1815 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/oyster_eastern_171978.json
+-rw-r--r--   0        0        0     1767 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/oyster_pacific_174219.json
+-rw-r--r--   0        0        0     1844 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/parmesan_cheese_171247.json
+-rw-r--r--   0        0        0     1725 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/pasta_168927.json
+-rw-r--r--   0        0        0     1735 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/peach_yellow_169928.json
+-rw-r--r--   0        0        0     1732 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/pear_169118.json
+-rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/pecan_nut_170182.json
+-rw-r--r--   0        0        0     1811 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/pinto_bean_175199.json
+-rw-r--r--   0        0        0     1714 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/pistachio_170184.json
+-rw-r--r--   0        0        0     1674 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/pomegranate_juice_167787.json
+-rw-r--r--   0        0        0     1773 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/pork_bacon_pan-fried_168322.json
+-rw-r--r--   0        0        0     1489 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/protein_powder_pea_2477360.json
+-rw-r--r--   0        0        0     1679 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/protein_powder_whey_173180.json
+-rw-r--r--   0        0        0     1711 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/quinoa_168874.json
+-rw-r--r--   0        0        0     1726 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/radish_169276.json
+-rw-r--r--   0        0        0     1631 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/raspberry_167755.json
+-rw-r--r--   0        0        0     1799 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/rice_brown_169703.json
+-rw-r--r--   0        0        0     1726 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/rice_white_169756.json
+-rw-r--r--   0        0        0     1715 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/rice_wild_169726.json
+-rw-r--r--   0        0        0     1752 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/ricotta_cheese_746766.json
+-rw-r--r--   0        0        0     1702 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/salmon_atlantic_173686.json
+-rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/salmon_sockeye_173691.json
+-rw-r--r--   0        0        0     1553 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/salt_173468.json
+-rw-r--r--   0        0        0     1814 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/sardine_175139.json
+-rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/sauerkraut_169279.json
+-rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/scallion_170005.json
+-rw-r--r--   0        0        0     1647 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/shallot_170499.json
+-rw-r--r--   0        0        0     1772 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/spinach_168462.json
+-rw-r--r--   0        0        0     1722 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/strawberry_167762.json
+-rw-r--r--   0        0        0     1806 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/sweet_potato_168482.json
+-rw-r--r--   0        0        0     1605 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/tomato_grape_321360.json
+-rw-r--r--   0        0        0     1729 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/tomato_red_170457.json
+-rw-r--r--   0        0        0     1708 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/tuna_bluefin_173706.json
+-rw-r--r--   0        0        0     1700 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/tuna_skipjack_175156.json
+-rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/tuna_yellowfin_175159.json
+-rw-r--r--   0        0        0     1751 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/turmeric_172231.json
+-rw-r--r--   0        0        0     1660 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/turnip_170465.json
+-rw-r--r--   0        0        0     1713 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/wakame_seaweed_170496.json
+-rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/walnut_170187.json
+-rw-r--r--   0        0        0     1782 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/whole_milk_171265.json
+-rw-r--r--   0        0        0     1719 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/yogurt_whole_milk_171284.json
+-rw-r--r--   0        0        0     1778 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/foods/zucchini_169291.json
+-rw-r--r--   0        0        0     2822 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/samples/bryan_johnson.json
+-rw-r--r--   0        0        0     2235 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/samples/eric_berg.json
+-rw-r--r--   0        0        0     6523 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/samples/foods.json
+-rw-r--r--   0        0        0     2341 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/nutrimetrics/resources/samples/michael_b_jordan.json
+-rw-r--r--   0        0        0      725 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/.gitignore
+-rw-r--r--   0        0        0     8259 2020-02-02 00:00:00.000000 nutrimetrics-1.0.0/PKG-INFO
```

### Comparing `nutrimetrics-0.0.2/.DS_Store` & `nutrimetrics-1.0.0/.DS_Store`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/.gitignore` & `nutrimetrics-1.0.0/.gitignore`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/LICENSE` & `nutrimetrics-1.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/README.md` & `nutrimetrics-1.0.0/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 # NutriMetrics
 
 NutriMetrics is a Python package that analyzes nutrients found in foods and user-defined meal plans.
 Nutrient profile data can be imported from USDA's FoodData Central or manually entered by users.
 The package tracks 60+ nutrients including fats, proteins, carbs, all minerals and vitamins.
-It comes with 100+ nutrient profiles found in common raw food and a few sample meal plans.
+It comes with 100+ nutrient profiles found in common food and a few sample meal plans.
 User-defined meal plans consist of a set of meals, each of which consists of a set of foods
 with a specified amount. Analysis reports are generated in Excel workbooks.
 
 [![PyPI - Version](https://img.shields.io/pypi/v/nutrimetrics.svg)](https://pypi.org/project/nutrimetrics)
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nutrimetrics.svg)](https://pypi.org/project/nutrimetrics)
 
 ![Report Screenshot](https://github.com/tomcv/nutrimetrics/blob/main/report.png?raw=true)
@@ -23,25 +23,31 @@
 
 ## Quick Start
 
 Run the commands:
 ```console
 $ pip install nutrimetrics
 $ nutrimetrics-init
-$ nutrimetrics-analyze ~/.nutrimetrics/samples/meal_plan.json
+$ nutrimetrics-analyze ~/.nutrimetrics/samples/bryan_johnson.json
 ```
-Which will generate the corresponding `meal_plan.xlsx` Excel workbook in the working directory.
+Which will generate the corresponding `bryan_johnson.xlsx` Excel workbook in the working directory.
+
+The package includes 3 sample meal plans:
+
+1. `bryan_johnson.json`: a vegan meal plan estimated from Bryan Johnson's [blueprint](https://blueprint.bryanjohnson.co/).
+2. `eric_berg.json`: a low-carb ketogenic meal plan estimated from Eric Berg's [eating routine](https://www.youtube.com/watch?v=EhZK_MUPxrc).
+3. `michael_b_jordan.json`: Michael B. Jordan's high-protein meal plan [to get fit](https://www.mensjournal.com/health-fitness/how-michael-b-jordan-got-fit-for-creed-20151120) for 'Creed'.
 
 ## Installation
 
 ### PyPI
 
 The easiest way to get NutriMetrics is to use pip:
 ```console
-pip install nutrimetrics
+$ pip install nutrimetrics
 ```
 That will install the `nutrimetrics` package along with all the required dependencies.
 Pip will also install a few commands (described below) to the package's bin directory.
 
 ### From Source
 
 Alternatively you can install the latest NutriMetrics codebase from the git repo:
@@ -65,15 +71,15 @@
 All configuration parameters are set in `~/.nutrimetrics/config.json`.
 The default configuration is created  when running the `nutrimetrics-init` command.
 The only parameter that you may have to change is the API key used to access FoodData Central
 when importing data.
 
 ### Analysis Report
 
-The package provides a sample meal plan you can use to run the `nutrimetrics-analyze` command:
+Reports are generated by running the `nutrimetrics-analyze` command:
 ```console
 $ nutrimetrics-analyze ~/.nutrimetrics/samples/meal_plan.json 
 ```
 Which will generate the corresponding `meal_plan.xlsx` Excel workbook in the working directory.
 The report includes the amount of each nutrient as well as some statistical data,
 including the energy distribution, the energy/protein/fat target, and the percentage of the
 Dietary Reference Intakes (DRI) for all minerals and vitamins. The report consists of 3 spreadsheets:
@@ -87,17 +93,18 @@
 {
   "name": "Simple Meal Plan",
   "unit": "g",
   "target": {
     "body_mass": 75400.0,
     "body_fat_percent": 15.0,
     "activity_factor": 1.4,  // in [1.2, 1.6] range based on activity
-    "protein_factor": 2.0,  // minimum protein intake in [1.5, 2.3] range
+    "protein_factor": 1.8,  // minimum protein intake in [1.5, 2.3] range
     "fat_factor": 0.8  // minimum fat intake 0.7 or larger
   },
+  "dietary_reference_intakes": "rda-male", // (ear-male, ear-female, rda-male, rda-female)
   "meals": [
     {
       "name": "Breakfast [7AM]",
       "foods": [
         {"food": "Oat Rolled", "amount": 40},
         {"food": "Blueberry", "amount": 80}
       ]
@@ -111,17 +118,21 @@
       ]
     }
   ]
 }
 ```
 The `food` value must be one of the food's name defined in the `~/.nutrimetrics/foods/` directory.
 
+The Dietary Reference Intakes (DRI) included in the package are the Recommended Dietary Allowance (RDA)
+and the Estimated Average Requirement (EAR) for male and female. Users can add their own requirement profiles
+in the `~/.nutrimetrics/dri/` directory.
+
 ### Nutrient Profile Data
 
-The package comes with 100+ nutrient profiles of raw food. However, new data can be added by importing
+The package comes with 100+ nutrient profiles of common food. However, new data can be added by importing
 nutrient profiles  from USDA's FoodData Central (FDC). The `nutrimetrics-import` command reads a JSON file
 that lists all foods names and FDC IDs to be imported, looking like this:
 
 ```json
 {
   "foods": [
     {"fdc_id": 170567,  "name": "Almond"},
```

### Comparing `nutrimetrics-0.0.2/pyproject.toml` & `nutrimetrics-1.0.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/.DS_Store` & `nutrimetrics-1.0.0/nutrimetrics/.DS_Store`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/cli.py` & `nutrimetrics-1.0.0/nutrimetrics/cli.py`

 * *Files 11% similar despite different names*

```diff
@@ -14,17 +14,19 @@
 from requests import __version__ as requests_version
 from xlsxwriter import __version__ as xlsxwriter_version
 
 
 def initialize():
     """Command that initializes user's configuration."""
     cfg = config.read_config()
+    if not cfg:
+        exit()
     info = f'NutriMetrics version {nutrimetrics_version} initialized '
     info += f'(jsmin: {jsmin_version}, requests: {requests_version}, xlsxwriter: {xlsxwriter_version})\n'
-    info += f'{config.config_dir.absolute()}\n├── config.json\n├── foods\n└── samples'
+    info += config.get_config_file_tree()
     print(info)
 
 
 def analyze_meal_plan():
     """Command that analyzes a meal plan."""
     parser = argparse.ArgumentParser(
         description='NutriMetrics - Analyze nutrients in a meal plan.',
@@ -36,38 +38,53 @@
         help='Path to meal plan JSON file to be processed'
     )
     args = parser.parse_args()
     json_file = Path(vars(args)['meal_plan.json'])
     if not json_file.exists():
         print(f"Data file '{json_file}' does not exist")
         exit()
+    json_data = config.read_json(json_file)
+    if not json_data:
+        exit()
     cfg = config.read_config()
+    if not cfg:
+        exit()
     foods = load_foods()
-    meal_plan = MealPlan(json_file, foods, cfg['dietary_reference_intakes'])
-    generator = WorkbookGenerator(cfg['workbook_settings'], cfg['dietary_reference_intakes'])
+    meal_plan = MealPlan(json_data, foods)
+    generator = WorkbookGenerator(cfg['workbook_settings'])
     generator.generate(Path(json_file.name.replace('.json', '.xlsx')), meal_plan, foods)
 
 
 def import_food_data_central():
     """Command that imports nutrient profile data from FoodData Central."""
     parser = argparse.ArgumentParser(
         description='NutriMetrics - Import food data from FoodData Central.',
         epilog=f"NutriMetrics configuration files live in '{config.config_dir}' directory."
     )
     parser.add_argument(
         'food_list.json',
         type=str,
         help='Path to food list JSON file to be processed'
     )
+    parser.add_argument(
+        '-r', '--replace',
+        action="store_true",
+        help='Replace food file if it already exists')
     args = parser.parse_args()
     json_file = Path(vars(args)['food_list.json'])
     if not json_file.exists():
         print(f"Data file '{json_file}' does not exist")
         exit()
+    json_data = config.read_json(json_file)
+    if not json_data:
+        exit()
     cfg = config.read_config()
+    if not cfg:
+        exit()
     fdc = FoodDataCentral(
         cfg['food_data_central']['api_url'],
         cfg['food_data_central']['api_key'],
         cfg['food_data_central']['verbose_import'],
-        cfg['food_data_central']['nutrients_ids']
+        cfg['food_data_central']['nutrients_ids'],
+        args.replace
     )
-    fdc.import_food_list(json_file)
+    fdc.import_food_list(json_data)
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/food_data_central.py` & `nutrimetrics-1.0.0/nutrimetrics/food_data_central.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,38 +1,41 @@
 # SPDX-FileCopyrightText: 2023-present Thomas Civeit <thomas@civeit.com>
 #
 # SPDX-License-Identifier: MIT
 """Defines the FoodData Central interface to import data."""
 
-from jsmin import jsmin
 import json
 import requests
 import nutrimetrics.config as config
 from pathlib import Path
 from nutrimetrics.meals import Food
 from nutrimetrics.units import convert_amount
 
 
 class FoodDataCentral:
     """Defines the FoodData Central interface to import data."""
-    def __init__(self, api_url, api_key, verbose_import, nutrients_ids):
+    def __init__(self, api_url, api_key, verbose_import, nutrients_ids, replace_existing):
         self.api_url = api_url
         self.api_key = api_key
         self.verbose_import = verbose_import
         self.nutrients_ids = nutrients_ids
+        self.replace_existing = replace_existing
         self.session = None
 
-    def import_food_list(self, json_file):
-        with open(json_file, 'r') as file:
-            data = json.loads(jsmin(file.read()))
+    def import_food_list(self, data):
         self.session = requests.Session()
         for food in data['foods']:
-            fdc_data = self.download(food['fdc_id'], food['name'])
+            food_name, fdc_id = food['name'], food['fdc_id']
+            food_file = Path(config.foods_dir, food_name.lower().replace(' ', '_') + f'_{fdc_id}.json')
+            if food_file.exists() and not self.replace_existing:
+                print(f"> Do not import {food_name}: {food_file.absolute()} already exists")
+                continue
+            fdc_data = self.download(fdc_id, food_name)
             if fdc_data:
-                self.write_food_file(food['fdc_id'], food['name'], fdc_data)
+                self.write_food_file(fdc_id, food_name, food_file, fdc_data)
 
     def download(self, fdc_id, food_name):
         query = f'{self.api_url}/food/{fdc_id}?api_key={self.api_key}'
         print(f'Fetching {food_name} ({fdc_id}) GET {query}')
         res = self.session.get(query)
         if res.status_code != 200:
             print(f'ERROR: FoodData Central return status={res.status_code}')
@@ -42,16 +45,15 @@
 
     def get_nutrient_data_name(self, ntr_id):
         for nutrient_name, nutrient_ids in self.nutrients_ids.items():
             if ntr_id in nutrient_ids:
                 return nutrient_name
         return None
 
-    def write_food_file(self, fdc_id, food_name, fdc_data):
-        food_file = Path(config.foods_dir, food_name.lower().replace(' ', '_') + f'_{fdc_id}.json')
+    def write_food_file(self, fdc_id, food_name, food_file, fdc_data):
         # FoodData Central nutrients are always provided for 100 grams
         food = Food(food_name, fdc_data['description'], amount=100)
         for food_nutrient in fdc_data["foodNutrients"]:
             if "amount" in food_nutrient:
                 ntr_id = food_nutrient["nutrient"]["id"]
                 ntr_unit = food_nutrient["nutrient"]["unitName"]
                 ntr_amount = food_nutrient["amount"]
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/meals.py` & `nutrimetrics-1.0.0/nutrimetrics/meals.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 # SPDX-FileCopyrightText: 2023-present Thomas Civeit <thomas@civeit.com>
 #
 # SPDX-License-Identifier: MIT
 """Defines food, meal, and meal plan."""
 
 from nutrimetrics.nutrients import nutrients_list
-from jsmin import jsmin
 import json
 import os
 from pathlib import Path
 import nutrimetrics.config as config
 import copy
 from collections import OrderedDict
 from nutrimetrics.units import convert_amount
@@ -30,21 +29,22 @@
             self.nutrients[nutrient.data_name] = 0  # nutrient amount is zero by default
 
     def to_json(self, indent):
         return json.dumps(self, default=lambda obj: obj.__dict__, indent=indent)
 
     @staticmethod
     def from_json(json_file):
-        data = json.loads(jsmin(json_file.read()))
+        data = config.read_json(json_file)
         food = Food()
-        food.name = data['name']
-        food.description = data['description']
-        food.amount = data['amount']
-        for ntr, amt in data['nutrients'].items():
-            food.nutrients[ntr] = amt
+        if data:
+            food.name = data['name']
+            food.description = data['description']
+            food.amount = data['amount']
+            for ntr, amt in data['nutrients'].items():
+                food.nutrients[ntr] = amt
         return food
 
     def multiply(self, m):
         self.amount *= m
         for nutrient in nutrients_list:
             self.nutrients[nutrient.data_name] *= m
 
@@ -61,17 +61,16 @@
 
 
 def load_foods():
     """Load all foods defined in dedicated configuration directory."""
     foods = dict()
     for file in [Path(f) for f in os.listdir(config.foods_dir)]:
         if file.suffix == '.json':
-            with open(Path(config.foods_dir, file), 'r') as json_file:
-                food = Food.from_json(json_file)
-                foods[food.name] = food
+            food = Food.from_json(Path(config.foods_dir, file))
+            foods[food.name] = food
     return OrderedDict(sorted(foods.items()))
 
 
 class Meal:
     """Defines meal that consists of foods."""
     def __init__(self, unit, data, foods_dict):
         self.name = data["name"]
@@ -89,62 +88,72 @@
         self.total = FoodTotal(name='TOTAL')
         for food in self.foods:
             self.total.add(food)
 
 
 class MealPlan:
     """Defines meal plan that consists of meals."""
-    def __init__(self, json_file, foods_dict, dri_dict):
-        with open(json_file, 'r') as file:
-            data = json.loads(jsmin(file.read()))
+    def __init__(self, data, foods_dict):
         self.name = data["name"]
         self.unit = data["unit"]
         self.meals = []
         for meal_data in data["meals"]:
             self.meals.append(Meal(self.unit, meal_data, foods_dict))
         # calculate total nutrients
         self.total = FoodTotal(name='GRAND TOTAL')
         for meal in self.meals:
             self.total.add(meal.total)
         # calculate energy distribution
         self.distribution = EnergyDistribution(self.total.nutrients["protein"],
                                                self.total.nutrients["carbohydrate"],
                                                self.total.nutrients["fat"])
+        # load DRI
+        self.dri_name = data["dietary_reference_intakes"]
+        self.dri_dict = self.load_dietary_reference_intakes()
         # calculate target
         self.target = Target(
             convert_amount(data["target"]["body_mass"], self.unit),
             data["target"]["body_fat_percent"] / 100,
             data["target"]["activity_factor"],
-            data["target"]["protein_factor"],
-            data["target"]["fat_factor"],
+            data["target"]["minimum_protein_factor"],
+            data["target"]["minimum_fat_factor"],
         )
-        dri_dict['energy'] = self.target.basal_metabolic_rate
-        dri_dict['protein'] = self.target.minimum_protein
-        dri_dict['fat'] = self.target.minimum_fat
+        # add target to DRI
+        self.dri_dict['energy'] = self.target.basal_metabolic_rate
+        self.dri_dict['protein'] = self.target.minimum_protein
+        self.dri_dict['fat'] = self.target.minimum_fat
         # calculate DRI ratio
         self.dri_ratio = dict()  # key: nutrient's data_name, value: DRI ratio
         for ntr_name in [nutrient.data_name for nutrient in nutrients_list]:
-            if ntr_name in dri_dict:
-                self.dri_ratio[ntr_name] = self.total.nutrients[ntr_name] / dri_dict[ntr_name]
+            if ntr_name in self.dri_dict:
+                self.dri_ratio[ntr_name] = self.total.nutrients[ntr_name] / self.dri_dict[ntr_name]
+
+    def load_dietary_reference_intakes(self):
+        dri_file = Path(config.dri_dir, f'{self.dri_name}.json')
+        if not dri_file.exists():
+            print(f"ERROR: DRI file '{dri_file.absolute()}' does not exist")
+            return dict()
+        data = config.read_json(dri_file)
+        return data['dietary_reference_intakes'] if data else dict()
 
 
 class Target:
-    def __init__(self, body_mass, body_fat_ratio, activity_factor, protein_factor, fat_factor):
+    def __init__(self, body_mass, body_fat_ratio, activity_factor, minimum_protein_factor, minimum_fat_factor):
         self.body_mass = body_mass
         self.body_fat_ratio = body_fat_ratio
         self.activity_factor = activity_factor
-        self.protein_factor = protein_factor
-        self.fat_factor = fat_factor
+        self.minimum_protein_factor = minimum_protein_factor
+        self.minimum_fat_factor = minimum_fat_factor
         # calculate derived variables
         self.lean_body_mass = (1 - self.body_fat_ratio) * self.body_mass
         # Katch–McArdle formula: Resting Daily Energy Expenditure (RDEE)
         self.resting_energy = 370 + (21.6 * (self.lean_body_mass / 1000))
         self.basal_metabolic_rate = self.resting_energy * self.activity_factor
-        self.minimum_protein = self.lean_body_mass * self.protein_factor / 1000  # kg to g
-        self.minimum_fat = self.lean_body_mass * self.fat_factor / 1000  # kg to g
+        self.minimum_protein = self.lean_body_mass * self.minimum_protein_factor / 1000  # kg to g
+        self.minimum_fat = self.lean_body_mass * self.minimum_fat_factor / 1000  # kg to g
 
 
 class EnergyDistribution:
     """Defines an energy distribution in fats, proteins and carbs."""
     def __init__(self, protein_amount, carb_amount, fat_amount):
         self.energy_protein = protein_amount * energy_protein_factor
         self.energy_carb = carb_amount * energy_carbohydrate_factor
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/nutrients.py` & `nutrimetrics-1.0.0/nutrimetrics/nutrients.py`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/units.py` & `nutrimetrics-1.0.0/nutrimetrics/units.py`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/workbook.py` & `nutrimetrics-1.0.0/nutrimetrics/workbook.py`

 * *Files 14% similar despite different names*

```diff
@@ -5,17 +5,16 @@
 
 import xlsxwriter
 from nutrimetrics.nutrients import nutrients_list, proteins, carbohydrates, fats, minerals, vitamins, alkaloids
 
 
 class WorkbookGenerator:
     """Workbook interface to generate Excel reports."""
-    def __init__(self, settings, dri_dict):
+    def __init__(self, settings):
         self.settings = settings
-        self.dri_dict = dri_dict
         self.workbook = None
 
     def generate(self, out_file, meal_plan, foods_dict):
         self.workbook = xlsxwriter.Workbook(out_file)
         self.create_meals_worksheet(meal_plan)
         self.create_target_worksheet(meal_plan)
         self.create_foods_worksheet(foods_dict)
@@ -57,61 +56,108 @@
             border=1)
         fmt_value = self.get_format(
             font_color=self.settings['target']['font_color'],
             bg_color=None,
             bold=False,
             align='right',
             border=1)
+        fmt_body_mass_label = self.get_format(
+            font_color=self.settings['target']['font_color'],
+            bg_color=self.settings['target']['body_mass_bg_color'],
+            bold=False,
+            align='left',
+            border=1)
+        fmt_body_mass_value = self.get_format(
+            font_color=self.settings['target']['font_color'],
+            bg_color=self.settings['target']['body_mass_bg_color'],
+            bold=False,
+            align='right',
+            border=1)
+        fmt_body_fat_label = self.get_format(
+            font_color=self.settings['target']['font_color'],
+            bg_color=self.settings['target']['body_fat_bg_color'],
+            bold=False,
+            align='left',
+            border=1)
+        fmt_body_fat_value = self.get_format(
+            font_color=self.settings['target']['font_color'],
+            bg_color=self.settings['target']['body_fat_bg_color'],
+            bold=False,
+            align='right',
+            border=1)
+        fmt_lean_body_mass_label = self.get_format(
+            font_color=self.settings['target']['font_color'],
+            bg_color=self.settings['target']['lean_body_mass_bg_color'],
+            bold=False,
+            align='left',
+            border=1)
+        fmt_lean_body_mass_value = self.get_format(
+            font_color=self.settings['target']['font_color'],
+            bg_color=self.settings['target']['lean_body_mass_bg_color'],
+            bold=False,
+            align='right',
+            border=1)
         fmt_energy_label = self.get_format(
             font_color=self.settings['colors']['energy'][0],
             bg_color=self.settings['colors']['energy'][1],
             bold=False,
             align='left',
             border=1)
         fmt_energy_value = self.get_format(
             font_color=self.settings['colors']['energy'][0],
             bg_color=self.settings['colors']['energy'][1],
             bold=False,
             align='right',
             border=1)
+        fmt_annotate = self.get_format(
+            font_color=self.settings['target']['font_color'],
+            bg_color=None,
+            bold=False,
+            align='left',
+            italic=True)
         # parameters
-        worksheet.write(0, 0, 'Body Mass (g)', fmt_label)
-        worksheet.write(0, 1, meal_plan.target.body_mass, fmt_value)
-        worksheet.write(1, 0, 'Body Fat (%)', fmt_label)
-        worksheet.write(1, 1, meal_plan.target.body_fat_ratio * 100, fmt_value)
+        worksheet.write(0, 0, 'Body Mass (g)', fmt_body_mass_label)
+        worksheet.write(0, 1, meal_plan.target.body_mass, fmt_body_mass_value)
+        worksheet.write(1, 0, 'Body Fat (%)', fmt_body_fat_label)
+        worksheet.write(1, 1, meal_plan.target.body_fat_ratio * 100, fmt_body_fat_value)
         worksheet.write(2, 0, 'Activity Factor', fmt_label)
         worksheet.write(2, 1, meal_plan.target.activity_factor, fmt_value)
-        worksheet.write(3, 0, 'Protein Factor', fmt_label)
-        worksheet.write(3, 1, meal_plan.target.protein_factor, fmt_value)
-        worksheet.write(4, 0, 'Fat Factor', fmt_label)
-        worksheet.write(4, 1, meal_plan.target.fat_factor, fmt_value)
+        worksheet.write(3, 0, 'Minimum Protein Factor', fmt_label)
+        worksheet.write(3, 1, meal_plan.target.minimum_protein_factor, fmt_value)
+        worksheet.write(4, 0, 'Minimum Fat Factor', fmt_label)
+        worksheet.write(4, 1, meal_plan.target.minimum_fat_factor, fmt_value)
         # calculated values
-        worksheet.write(6, 0, 'Lean Body Mass (g)', fmt_label)
-        worksheet.write(6, 1, meal_plan.target.lean_body_mass, fmt_value)
+        worksheet.write(6, 0, 'Lean Body Mass (g)', fmt_lean_body_mass_label)
+        worksheet.write(6, 1, meal_plan.target.lean_body_mass, fmt_lean_body_mass_value)
         worksheet.write(7, 0, 'Resting Daily Energy Expenditure (kcal)', fmt_label)
         worksheet.write(7, 1, meal_plan.target.resting_energy, fmt_value)
         worksheet.write(8, 0, 'Basal Metabolic Rate (kcal)', fmt_energy_label)
         worksheet.write(8, 1, meal_plan.target.basal_metabolic_rate, fmt_energy_value)
         worksheet.write(9, 0, 'Minimum Protein (g)', fmt_label)
         worksheet.write(9, 1, meal_plan.target.minimum_protein, fmt_value)
         worksheet.write(10, 0, 'Minimum Fat (g)', fmt_label)
         worksheet.write(10, 1, meal_plan.target.minimum_fat, fmt_value)
+        # add annotations
+        worksheet.write(0, 3, "Meal plan parameters", fmt_annotate)
+        worksheet.write(7, 3, "Katch–McArdle formula", fmt_annotate)
+        worksheet.write(8, 3, "BMR based on activity factor", fmt_annotate)
         # set columns width
         worksheet.set_column_pixels(0, 0, self.settings['target']['column_pixels_label'])
         worksheet.set_column_pixels(1, 1, self.settings['target']['column_pixels_value'])
+        worksheet.set_column_pixels(2, 2, self.settings['target']['column_pixels_separator'])
 
     def create_foods_worksheet(self, foods_dict):
         worksheet = self.workbook.add_worksheet('Foods')
         self.write_headers(worksheet)
         row_i, column_i = self.write_values(worksheet, row_i=0, foods=foods_dict.values(), comment=True)
         self.write_columns_separators(worksheet, row_i)
         self.set_columns_width(worksheet, column_i)
         worksheet.freeze_panes('B2')
 
-    def get_format(self, font_color, bg_color, bold, align, border=None, rotation=None):
+    def get_format(self, font_color, bg_color, bold, align, border=None, rotation=None, italic=None):
         fmt = {
             'font_name': self.settings['font_name'],
             'font_size': self.settings['font_size'],
             'font_color': font_color,
             'bold': bold,
             'align': align,
             'valign': 'bottom',  # force bottom vertical alignment
@@ -119,14 +165,16 @@
         }
         if bg_color:
             fmt['bg_color'] = bg_color
         if border:
             fmt['border'] = border
         if rotation:
             fmt['rotation'] = rotation
+        if italic:
+            fmt['italic'] = italic
         return self.workbook.add_format(fmt)
 
     def get_colors(self, nutrient_data_name):
         if nutrient_data_name == 'energy':
             return self.settings['colors']['energy']
         elif nutrient_data_name == 'water':
             return self.settings['colors']['water']
@@ -222,15 +270,15 @@
 
     def write_energy(self, worksheet, row_i, meal_plan):
         column_i = 0
         row_i += 1
         fmt = self.get_format(
             font_color=self.settings['colors']['food'][0],
             bg_color=None,
-            bold=True,
+            bold=False,
             align='left')
         worksheet.write(row_i, column_i, 'Energy [%]', fmt)
         column_i = 1
         for nutrient in nutrients_list:
             if nutrient.data_name in self.settings['do_not_display']:
                 continue
             column_i += 1
@@ -251,62 +299,72 @@
     def write_target_and_dri(self, worksheet, row_i, meal_plan):
         # write DRI values
         row_i += 1
         column_i = 0
         fmt = self.get_format(
             font_color=self.settings['colors']['food'][0],
             bg_color=None,
-            bold=True,
+            bold=False,
             align='left')
-        worksheet.write(row_i, column_i, 'Target & DRI', fmt)
+        worksheet.write(row_i, column_i, f'Target & DRI ({meal_plan.dri_name})', fmt)
         column_i = 1
         for nutrient in nutrients_list:
             if nutrient.data_name in self.settings['do_not_display']:
                 continue
             column_i += 1
-            if nutrient.data_name in self.dri_dict:
+            if nutrient.data_name in meal_plan.dri_dict:
                 font_color, bg_color = self.get_colors(nutrient.data_name)
                 fmt = self.get_format(
                     font_color=font_color,
                     bg_color=None,
                     bold=False,
                     align='right')
-                worksheet.write(row_i, column_i, self.convert(nutrient, self.dri_dict[nutrient.data_name]), fmt)
+                worksheet.write(row_i, column_i,
+                                self.convert(nutrient, meal_plan.dri_dict[nutrient.data_name]), fmt)
         # write DRI percentage
         row_i += 1
         column_i = 0
         fmt = self.get_format(
             font_color=self.settings['colors']['food'][0],
             bg_color=None,
-            bold=True,
+            bold=False,
             align='left')
         worksheet.write(row_i, column_i, 'Target & DRI [%]', fmt)
         column_i = 1
         for nutrient in nutrients_list:
             if nutrient.data_name in self.settings['do_not_display']:
                 continue
             column_i += 1
-            if nutrient.data_name in self.dri_dict:
+            if nutrient.data_name in meal_plan.dri_dict:
                 font_color, bg_color = self.get_colors(nutrient.data_name)
                 percent = 100 * meal_plan.dri_ratio[nutrient.data_name]
-                bg_color = (self.settings['dri_negative_bg_color'] if percent < 100
-                            else self.settings['dri_positive_bg_color'])
+                if percent >= 300:
+                    bg_color = self.settings['dri_colors']['excess_3']
+                elif percent >= 200:
+                    bg_color = self.settings['dri_colors']['excess_2']
+                elif percent >= 100:
+                    bg_color = self.settings['dri_colors']['excess_1']
+                elif percent >= 80:
+                    bg_color = self.settings['dri_colors']['deficit_1']
+                elif percent >= 60:
+                    bg_color = self.settings['dri_colors']['deficit_2']
+                else:
+                    bg_color = self.settings['dri_colors']['deficit_3']
                 fmt = self.get_format(
                     font_color=font_color,
                     bg_color=bg_color,
                     bold=False,
                     align='right')
                 worksheet.write(row_i, column_i, percent, fmt)
         return row_i, column_i
 
     def write_columns_separators(self, worksheet, bottom_row):
         border_format = self.workbook.add_format({'left': 1})
         for column in self.settings['columns_separators']:
-            worksheet.conditional_format(1, column, bottom_row, column,
-                                         {'type': 'blanks', 'format': border_format})
-            worksheet.conditional_format(1, column, bottom_row, column,
-                                         {'type': 'no_blanks', 'format': border_format})
+            for cell_type in ['blanks', 'no_blanks']:
+                worksheet.conditional_format(1, column, bottom_row, column,
+                                             {'type': cell_type, 'format': border_format})
 
     def set_columns_width(self, worksheet, last_column):
         worksheet.set_column_pixels(0, 0, self.settings['column_pixels_food'])
         for i in range(last_column):
             worksheet.set_column_pixels(i+1, i+1, self.settings['column_pixels_nutrient'])
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/.DS_Store` & `nutrimetrics-1.0.0/nutrimetrics/resources/.DS_Store`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/config.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/config.json`

 * *Files 8% similar despite different names*

```diff
@@ -1,229 +1,217 @@
-00000000: 7b0a 2020 2266 6f6f 645f 6461 7461 5f63  {.  "food_data_c
-00000010: 656e 7472 616c 223a 207b 0a20 2020 2022  entral": {.    "
-00000020: 6170 695f 7572 6c22 3a20 2268 7474 7073  api_url": "https
-00000030: 3a2f 2f61 7069 2e6e 616c 2e75 7364 612e  ://api.nal.usda.
-00000040: 676f 762f 6664 632f 7631 222c 0a20 2020  gov/fdc/v1",.   
-00000050: 2022 6170 695f 6b65 7922 3a20 2245 4e54   "api_key": "ENT
-00000060: 4552 5f4b 4559 5f48 4552 4522 2c0a 2020  ER_KEY_HERE",.  
-00000070: 2020 2276 6572 626f 7365 5f69 6d70 6f72    "verbose_impor
-00000080: 7422 3a20 6661 6c73 652c 0a20 2020 2022  t": false,.    "
-00000090: 6e75 7472 6965 6e74 735f 6964 7322 3a20  nutrients_ids": 
-000000a0: 7b0a 2020 2020 2020 2265 6e65 7267 7922  {.      "energy"
-000000b0: 3a20 5b31 3030 382c 2032 3034 372c 2032  : [1008, 2047, 2
-000000c0: 3034 385d 2c0a 2020 2020 2020 2277 6174  048],.      "wat
-000000d0: 6572 223a 205b 3130 3531 5d2c 0a20 2020  er": [1051],.   
-000000e0: 2020 2022 6661 7422 3a20 5b31 3030 342c     "fat": [1004,
-000000f0: 2031 3038 355d 2c0a 2020 2020 2020 226d   1085],.      "m
-00000100: 6f6e 6f2d 756e 7361 7475 7261 7465 6422  ono-unsaturated"
-00000110: 3a20 5b31 3239 325d 2c0a 2020 2020 2020  : [1292],.      
-00000120: 2270 6f6c 792d 756e 7361 7475 7261 7465  "poly-unsaturate
-00000130: 6422 3a20 5b31 3239 335d 2c0a 2020 2020  d": [1293],.    
-00000140: 2020 2273 6174 7572 6174 6564 223a 205b    "saturated": [
-00000150: 3132 3538 5d2c 0a20 2020 2020 2022 7472  1258],.      "tr
-00000160: 616e 7322 3a20 5b31 3235 375d 2c0a 2020  ans": [1257],.  
-00000170: 2020 2020 2263 686f 6c65 7374 6572 6f6c      "cholesterol
-00000180: 223a 205b 3132 3533 5d2c 0a20 2020 2020  ": [1253],.     
-00000190: 2022 7072 6f74 6569 6e22 3a20 5b31 3030   "protein": [100
-000001a0: 335d 2c0a 2020 2020 2020 2263 6172 626f  3],.      "carbo
-000001b0: 6879 6472 6174 6522 3a20 5b31 3030 355d  hydrate": [1005]
-000001c0: 2c0a 2020 2020 2020 2266 6962 6572 223a  ,.      "fiber":
-000001d0: 205b 3130 3739 2c20 3230 3333 5d2c 0a20   [1079, 2033],. 
-000001e0: 2020 2020 2022 7375 6761 7222 3a20 5b31       "sugar": [1
-000001f0: 3036 332c 2032 3030 305d 2c0a 2020 2020  063, 2000],.    
-00000200: 2020 2273 7461 7263 6822 3a20 5b31 3030    "starch": [100
-00000210: 395d 2c0a 2020 2020 2020 2273 7563 726f  9],.      "sucro
-00000220: 7365 223a 205b 3130 3130 5d2c 0a20 2020  se": [1010],.   
-00000230: 2020 2022 676c 7563 6f73 6522 3a20 5b31     "glucose": [1
-00000240: 3031 315d 2c0a 2020 2020 2020 2266 7275  011],.      "fru
-00000250: 6374 6f73 6522 3a20 5b31 3031 325d 2c0a  ctose": [1012],.
-00000260: 2020 2020 2020 226c 6163 746f 7365 223a        "lactose":
-00000270: 205b 3130 3133 5d2c 0a20 2020 2020 2022   [1013],.      "
-00000280: 6d61 6c74 6f73 6522 3a20 5b31 3031 345d  maltose": [1014]
-00000290: 2c0a 2020 2020 2020 2267 616c 6163 746f  ,.      "galacto
-000002a0: 7365 223a 205b 3130 3735 5d2c 0a20 2020  se": [1075],.   
-000002b0: 2020 2022 6361 6c63 6975 6d22 3a20 5b31     "calcium": [1
-000002c0: 3038 375d 2c0a 2020 2020 2020 2263 6f70  087],.      "cop
-000002d0: 7065 7222 3a20 5b31 3039 385d 2c0a 2020  per": [1098],.  
-000002e0: 2020 2020 2269 726f 6e22 3a20 5b31 3038      "iron": [108
-000002f0: 395d 2c0a 2020 2020 2020 226d 6167 6e65  9],.      "magne
-00000300: 7369 756d 223a 205b 3130 3930 5d2c 0a20  sium": [1090],. 
-00000310: 2020 2020 2022 6d61 6e67 616e 6573 6522       "manganese"
-00000320: 3a20 5b31 3130 315d 2c0a 2020 2020 2020  : [1101],.      
-00000330: 226d 6f6c 7962 6465 6e75 6d22 3a20 5b31  "molybdenum": [1
-00000340: 3130 325d 2c0a 2020 2020 2020 2270 686f  102],.      "pho
-00000350: 7370 686f 7275 7322 3a20 5b31 3039 315d  sphorus": [1091]
-00000360: 2c0a 2020 2020 2020 2270 6f74 6173 7369  ,.      "potassi
-00000370: 756d 223a 205b 3130 3932 5d2c 0a20 2020  um": [1092],.   
-00000380: 2020 2022 7365 6c65 6e69 756d 223a 205b     "selenium": [
-00000390: 3131 3033 5d2c 0a20 2020 2020 2022 736f  1103],.      "so
-000003a0: 6469 756d 223a 205b 3130 3933 5d2c 0a20  dium": [1093],. 
-000003b0: 2020 2020 2022 7a69 6e63 223a 205b 3130       "zinc": [10
-000003c0: 3935 5d2c 0a20 2020 2020 2022 7669 7461  95],.      "vita
-000003d0: 6d69 6e2d 6122 3a20 5b31 3130 365d 2c0a  min-a": [1106],.
-000003e0: 2020 2020 2020 2272 6574 696e 6f6c 223a        "retinol":
-000003f0: 205b 3131 3035 5d2c 0a20 2020 2020 2022   [1105],.      "
-00000400: 7468 6961 6d69 6e22 3a20 5b31 3136 355d  thiamin": [1165]
-00000410: 2c0a 2020 2020 2020 2272 6962 6f66 6c61  ,.      "ribofla
-00000420: 7669 6e22 3a20 5b31 3136 365d 2c0a 2020  vin": [1166],.  
-00000430: 2020 2020 226e 6961 6369 6e22 3a20 5b31      "niacin": [1
-00000440: 3136 375d 2c0a 2020 2020 2020 2270 616e  167],.      "pan
-00000450: 746f 7468 656e 6963 2d61 6369 6422 3a20  tothenic-acid": 
-00000460: 5b31 3137 305d 2c0a 2020 2020 2020 2276  [1170],.      "v
-00000470: 6974 616d 696e 2d62 3622 3a20 5b31 3137  itamin-b6": [117
-00000480: 355d 2c0a 2020 2020 2020 2262 696f 7469  5],.      "bioti
-00000490: 6e22 3a20 5b31 3137 365d 2c0a 2020 2020  n": [1176],.    
-000004a0: 2020 2266 6f6c 6174 6522 3a20 5b31 3137    "folate": [117
-000004b0: 375d 2c0a 2020 2020 2020 2266 6f6c 6963  7],.      "folic
-000004c0: 2d61 6369 6422 3a20 5b31 3138 365d 2c0a  -acid": [1186],.
-000004d0: 2020 2020 2020 2276 6974 616d 696e 2d62        "vitamin-b
-000004e0: 3132 223a 205b 3131 3738 5d2c 0a20 2020  12": [1178],.   
-000004f0: 2020 2022 6368 6f6c 696e 6522 3a20 5b31     "choline": [1
-00000500: 3138 305d 2c0a 2020 2020 2020 2276 6974  180],.      "vit
-00000510: 616d 696e 2d63 223a 205b 3131 3632 5d2c  amin-c": [1162],
-00000520: 0a20 2020 2020 2022 7669 7461 6d69 6e2d  .      "vitamin-
-00000530: 6422 3a20 5b31 3131 345d 2c0a 2020 2020  d": [1114],.    
-00000540: 2020 2276 6974 616d 696e 2d65 223a 205b    "vitamin-e": [
-00000550: 3131 3039 5d2c 0a20 2020 2020 2022 7068  1109],.      "ph
-00000560: 796c 6c6f 7175 696e 6f6e 6522 3a20 5b31  ylloquinone": [1
-00000570: 3138 355d 2c0a 2020 2020 2020 226d 656e  185],.      "men
-00000580: 6171 7569 6e6f 6e65 223a 205b 3131 3833  aquinone": [1183
-00000590: 5d2c 0a20 2020 2020 2022 6869 7374 6964  ],.      "histid
-000005a0: 696e 6522 3a20 5b31 3232 315d 2c0a 2020  ine": [1221],.  
-000005b0: 2020 2020 2269 736f 6c65 7563 696e 6522      "isoleucine"
-000005c0: 3a20 5b31 3231 325d 2c0a 2020 2020 2020  : [1212],.      
-000005d0: 226c 6575 6369 6e65 223a 205b 3132 3133  "leucine": [1213
-000005e0: 5d2c 0a20 2020 2020 2022 6c79 7369 6e65  ],.      "lysine
-000005f0: 223a 205b 3132 3134 5d2c 0a20 2020 2020  ": [1214],.     
-00000600: 2022 6d65 7468 696f 6e69 6e65 223a 205b   "methionine": [
-00000610: 3132 3135 5d2c 0a20 2020 2020 2022 7068  1215],.      "ph
-00000620: 656e 796c 616c 616e 696e 6522 3a20 5b31  enylalanine": [1
-00000630: 3231 375d 2c0a 2020 2020 2020 2274 6872  217],.      "thr
-00000640: 656f 6e69 6e65 223a 205b 3132 3131 5d2c  eonine": [1211],
-00000650: 0a20 2020 2020 2022 7472 7970 746f 7068  .      "tryptoph
-00000660: 616e 223a 205b 3132 3130 5d2c 0a20 2020  an": [1210],.   
-00000670: 2020 2022 7661 6c69 6e65 223a 205b 3132     "valine": [12
-00000680: 3139 5d2c 0a20 2020 2020 2022 6172 6769  19],.      "argi
-00000690: 6e69 6e65 223a 205b 3132 3230 5d2c 0a20  nine": [1220],. 
-000006a0: 2020 2020 2022 6379 7374 696e 6522 3a20       "cystine": 
-000006b0: 5b31 3231 365d 2c0a 2020 2020 2020 2267  [1216],.      "g
-000006c0: 6c79 6369 6e65 223a 205b 3132 3235 5d2c  lycine": [1225],
-000006d0: 0a20 2020 2020 2022 7072 6f6c 696e 6522  .      "proline"
-000006e0: 3a20 5b31 3232 365d 2c0a 2020 2020 2020  : [1226],.      
-000006f0: 2274 7972 6f73 696e 6522 3a20 5b31 3231  "tyrosine": [121
-00000700: 385d 2c0a 2020 2020 2020 2261 6c61 6e69  8],.      "alani
-00000710: 6e65 223a 205b 3132 3232 5d2c 0a20 2020  ne": [1222],.   
-00000720: 2020 2022 6173 7061 7274 6963 2d61 6369     "aspartic-aci
-00000730: 6422 3a20 5b31 3232 335d 2c0a 2020 2020  d": [1223],.    
-00000740: 2020 2267 6c75 7461 6d69 632d 6163 6964    "glutamic-acid
-00000750: 223a 205b 3132 3234 5d2c 0a20 2020 2020  ": [1224],.     
-00000760: 2022 7365 7269 6e65 223a 205b 3132 3237   "serine": [1227
-00000770: 5d2c 0a20 2020 2020 2022 6879 6472 6f78  ],.      "hydrox
-00000780: 7970 726f 6c69 6e65 223a 205b 3132 3238  yproline": [1228
-00000790: 5d2c 0a20 2020 2020 2022 6361 6666 6569  ],.      "caffei
-000007a0: 6e65 223a 205b 3130 3537 5d2c 0a20 2020  ne": [1057],.   
-000007b0: 2020 2022 7468 656f 6272 6f6d 696e 6522     "theobromine"
-000007c0: 3a20 5b31 3035 385d 0a20 2020 207d 0a20  : [1058].    }. 
-000007d0: 207d 2c0a 2020 2264 6965 7461 7279 5f72   },.  "dietary_r
-000007e0: 6566 6572 656e 6365 5f69 6e74 616b 6573  eference_intakes
-000007f0: 223a 207b 0a20 2020 2022 7669 7461 6d69  ": {.    "vitami
-00000800: 6e2d 6122 3a20 302e 3030 3039 2c0a 2020  n-a": 0.0009,.  
-00000810: 2020 2274 6869 616d 696e 223a 2030 2e30    "thiamin": 0.0
-00000820: 3031 322c 0a20 2020 2022 7269 626f 666c  012,.    "ribofl
-00000830: 6176 696e 223a 2030 2e30 3031 332c 0a20  avin": 0.0013,. 
-00000840: 2020 2022 6e69 6163 696e 223a 2030 2e30     "niacin": 0.0
-00000850: 3136 2c0a 2020 2020 2270 616e 746f 7468  16,.    "pantoth
-00000860: 656e 6963 2d61 6369 6422 3a20 302e 3030  enic-acid": 0.00
-00000870: 352c 0a20 2020 2022 7669 7461 6d69 6e2d  5,.    "vitamin-
-00000880: 6236 223a 2030 2e30 3031 372c 0a20 2020  b6": 0.0017,.   
-00000890: 2022 6269 6f74 696e 223a 2033 652d 3035   "biotin": 3e-05
-000008a0: 2c0a 2020 2020 2266 6f6c 6174 6522 3a20  ,.    "folate": 
-000008b0: 302e 3030 3034 2c0a 2020 2020 2276 6974  0.0004,.    "vit
-000008c0: 616d 696e 2d62 3132 223a 2032 2e34 652d  amin-b12": 2.4e-
-000008d0: 3036 2c0a 2020 2020 2263 686f 6c69 6e65  06,.    "choline
-000008e0: 223a 2030 2e35 352c 0a20 2020 2022 7669  ": 0.55,.    "vi
-000008f0: 7461 6d69 6e2d 6322 3a20 302e 3039 2c0a  tamin-c": 0.09,.
-00000900: 2020 2020 2276 6974 616d 696e 2d64 223a      "vitamin-d":
-00000910: 2032 652d 3035 2c0a 2020 2020 2276 6974   2e-05,.    "vit
-00000920: 616d 696e 2d65 223a 2030 2e30 3135 2c0a  amin-e": 0.015,.
-00000930: 2020 2020 2270 6879 6c6c 6f71 7569 6e6f      "phylloquino
-00000940: 6e65 223a 2030 2e30 3030 3132 2c0a 2020  ne": 0.00012,.  
-00000950: 2020 2263 616c 6369 756d 223a 2031 2e33    "calcium": 1.3
-00000960: 2c0a 2020 2020 2263 6f70 7065 7222 3a20  ,.    "copper": 
-00000970: 302e 3030 3039 2c0a 2020 2020 2269 726f  0.0009,.    "iro
-00000980: 6e22 3a20 302e 3031 382c 0a20 2020 2022  n": 0.018,.    "
-00000990: 6d61 676e 6573 6975 6d22 3a20 302e 3432  magnesium": 0.42
-000009a0: 2c0a 2020 2020 226d 616e 6761 6e65 7365  ,.    "manganese
-000009b0: 223a 2030 2e30 3032 332c 0a20 2020 2022  ": 0.0023,.    "
-000009c0: 6d6f 6c79 6264 656e 756d 223a 2034 2e35  molybdenum": 4.5
-000009d0: 652d 3035 2c0a 2020 2020 2270 686f 7370  e-05,.    "phosp
-000009e0: 686f 7275 7322 3a20 312e 3235 2c0a 2020  horus": 1.25,.  
-000009f0: 2020 2270 6f74 6173 7369 756d 223a 2034    "potassium": 4
-00000a00: 2e37 2c0a 2020 2020 2273 6f64 6975 6d22  .7,.    "sodium"
-00000a10: 3a20 312e 352c 0a20 2020 2022 7365 6c65  : 1.5,.    "sele
-00000a20: 6e69 756d 223a 2035 2e35 652d 3035 2c0a  nium": 5.5e-05,.
-00000a30: 2020 2020 227a 696e 6322 3a20 302e 3031      "zinc": 0.01
-00000a40: 310a 2020 7d2c 0a20 2022 776f 726b 626f  1.  },.  "workbo
-00000a50: 6f6b 5f73 6574 7469 6e67 7322 3a20 7b0a  ok_settings": {.
-00000a60: 2020 2020 2266 6f6e 745f 6e61 6d65 223a      "font_name":
-00000a70: 2022 4865 6c76 6574 6963 6122 2c0a 2020   "Helvetica",.  
-00000a80: 2020 2266 6f6e 745f 7369 7a65 223a 2031    "font_size": 1
-00000a90: 312c 0a20 2020 2022 6e75 6d62 6572 5f66  1,.    "number_f
-00000aa0: 6f72 6d61 7422 3a20 2223 2c30 2e30 222c  ormat": "#,0.0",
-00000ab0: 0a20 2020 2022 636f 6c75 6d6e 5f70 6978  .    "column_pix
-00000ac0: 656c 735f 666f 6f64 223a 2031 3635 2c0a  els_food": 165,.
-00000ad0: 2020 2020 2263 6f6c 756d 6e5f 7069 7865      "column_pixe
-00000ae0: 6c73 5f6e 7574 7269 656e 7422 3a20 3535  ls_nutrient": 55
-00000af0: 2c0a 2020 2020 2264 6f5f 6e6f 745f 6469  ,.    "do_not_di
-00000b00: 7370 6c61 7922 3a20 5b22 7761 7465 7222  splay": ["water"
-00000b10: 2c20 2272 6574 696e 6f6c 222c 2022 666f  , "retinol", "fo
-00000b20: 6c69 632d 6163 6964 225d 2c0a 2020 2020  lic-acid"],.    
-00000b30: 2263 6f6c 6f72 7322 3a20 7b0a 2020 2020  "colors": {.    
-00000b40: 2020 2266 6f6f 6422 3a20 5b22 2330 3030    "food": ["#000
-00000b50: 3030 3022 2c20 2223 4646 4646 4646 225d  000", "#FFFFFF"]
-00000b60: 2c0a 2020 2020 2020 2261 6d6f 756e 7422  ,.      "amount"
-00000b70: 3a20 5b22 2330 4632 3433 4522 2c20 2223  : ["#0F243E", "#
-00000b80: 4443 4536 4631 225d 2c0a 2020 2020 2020  DCE6F1"],.      
-00000b90: 2265 6e65 7267 7922 3a20 5b22 2334 3033  "energy": ["#403
-00000ba0: 3135 3122 2c20 2223 4534 4446 4543 225d  151", "#E4DFEC"]
-00000bb0: 2c0a 2020 2020 2020 2277 6174 6572 223a  ,.      "water":
-00000bc0: 205b 2223 3030 3030 3030 222c 2022 2346   ["#000000", "#F
-00000bd0: 4646 4646 4622 5d2c 0a20 2020 2020 2022  FFFFF"],.      "
-00000be0: 6661 7473 223a 205b 2223 3030 3030 3030  fats": ["#000000
-00000bf0: 222c 2022 2346 4646 4646 4622 5d2c 0a20  ", "#FFFFFF"],. 
-00000c00: 2020 2020 2022 7072 6f74 6569 6e73 223a       "proteins":
-00000c10: 205b 2223 3937 3437 3141 222c 2022 2346   ["#97471A", "#F
-00000c20: 4345 3944 3922 5d2c 0a20 2020 2020 2022  CE9D9"],.      "
-00000c30: 6361 7262 6f68 7964 7261 7465 7322 3a20  carbohydrates": 
-00000c40: 5b22 2330 3030 3030 3022 2c20 2223 4646  ["#000000", "#FF
-00000c50: 4646 4646 225d 2c0a 2020 2020 2020 226d  FFFF"],.      "m
-00000c60: 696e 6572 616c 7322 3a20 5b22 2334 3934  inerals": ["#494
-00000c70: 3532 3922 2c20 2223 4444 4439 4334 225d  529", "#DDD9C4"]
-00000c80: 2c0a 2020 2020 2020 2276 6974 616d 696e  ,.      "vitamin
-00000c90: 7322 3a20 5b22 2330 3030 3030 3022 2c20  s": ["#000000", 
-00000ca0: 2223 4646 4646 4646 225d 2c0a 2020 2020  "#FFFFFF"],.    
-00000cb0: 2020 2261 6c6b 616c 6f69 6473 223a 205b    "alkaloids": [
-00000cc0: 2223 3030 3030 3030 222c 2022 2346 4646  "#000000", "#FFF
-00000cd0: 4646 4622 5d0a 2020 2020 7d2c 0a20 2020  FFF"].    },.   
-00000ce0: 2022 746f 7461 6c5f 6267 5f63 6f6c 6f72   "total_bg_color
-00000cf0: 223a 2022 2346 3246 3246 3222 2c0a 2020  ": "#F2F2F2",.  
-00000d00: 2020 2267 7261 6e64 5f74 6f74 616c 5f62    "grand_total_b
-00000d10: 675f 636f 6c6f 7222 3a20 2223 4439 4439  g_color": "#D9D9
-00000d20: 4439 222c 0a20 2020 2022 656e 6572 6779  D9",.    "energy
-00000d30: 5f62 675f 636f 6c6f 7222 3a20 2223 4636  _bg_color": "#F6
-00000d40: 4642 4337 222c 0a20 2020 2022 6472 695f  FBC7",.    "dri_
-00000d50: 706f 7369 7469 7665 5f62 675f 636f 6c6f  positive_bg_colo
-00000d60: 7222 3a20 2223 4542 4631 4445 222c 0a20  r": "#EBF1DE",. 
-00000d70: 2020 2022 6472 695f 6e65 6761 7469 7665     "dri_negative
-00000d80: 5f62 675f 636f 6c6f 7222 3a20 2223 4632  _bg_color": "#F2
-00000d90: 4443 4442 222c 0a20 2020 2022 636f 6c75  DCDB",.    "colu
-00000da0: 6d6e 735f 7365 7061 7261 746f 7273 223a  mns_separators":
-00000db0: 205b 322c 2032 302c 2033 312c 2034 362c   [2, 20, 31, 46,
-00000dc0: 2035 352c 2036 355d 2c0a 2020 2020 2274   55, 65],.    "t
-00000dd0: 6172 6765 7422 3a20 7b0a 2020 2020 2020  arget": {.      
-00000de0: 2266 6f6e 745f 636f 6c6f 7222 3a20 2223  "font_color": "#
-00000df0: 3030 3030 3030 222c 0a20 2020 2020 2022  000000",.      "
-00000e00: 636f 6c75 6d6e 5f70 6978 656c 735f 6c61  column_pixels_la
-00000e10: 6265 6c22 3a20 3236 302c 0a20 2020 2020  bel": 260,.     
-00000e20: 2022 636f 6c75 6d6e 5f70 6978 656c 735f   "column_pixels_
-00000e30: 7661 6c75 6522 3a20 3930 0a20 2020 207d  value": 90.    }
-00000e40: 0a20 207d 0a7d 0a                        .  }.}.
+00000000: 7b0a 2020 2f2f 2046 6f6f 6444 6174 6120  {.  // FoodData 
+00000010: 4365 6e74 7261 6c20 4150 4920 7061 7261  Central API para
+00000020: 6d65 7465 7273 2e20 4765 7420 4150 4920  meters. Get API 
+00000030: 6b65 7920 6865 7265 3a0a 2020 2f2f 2068  key here:.  // h
+00000040: 7474 7073 3a2f 2f66 6463 2e6e 616c 2e75  ttps://fdc.nal.u
+00000050: 7364 612e 676f 762f 6170 692d 6775 6964  sda.gov/api-guid
+00000060: 652e 6874 6d6c 0a20 2022 666f 6f64 5f64  e.html.  "food_d
+00000070: 6174 615f 6365 6e74 7261 6c22 3a20 7b0a  ata_central": {.
+00000080: 2020 2020 2261 7069 5f75 726c 223a 2022      "api_url": "
+00000090: 6874 7470 733a 2f2f 6170 692e 6e61 6c2e  https://api.nal.
+000000a0: 7573 6461 2e67 6f76 2f66 6463 2f76 3122  usda.gov/fdc/v1"
+000000b0: 2c0a 2020 2020 2261 7069 5f6b 6579 223a  ,.    "api_key":
+000000c0: 2022 454e 5445 525f 4b45 595f 4845 5245   "ENTER_KEY_HERE
+000000d0: 222c 0a20 2020 2022 7665 7262 6f73 655f  ",.    "verbose_
+000000e0: 696d 706f 7274 223a 2066 616c 7365 2c0a  import": false,.
+000000f0: 2020 2020 226e 7574 7269 656e 7473 5f69      "nutrients_i
+00000100: 6473 223a 207b 0a20 2020 2020 2022 656e  ds": {.      "en
+00000110: 6572 6779 223a 205b 3130 3038 2c20 3230  ergy": [1008, 20
+00000120: 3437 2c20 3230 3438 5d2c 0a20 2020 2020  47, 2048],.     
+00000130: 2022 7761 7465 7222 3a20 5b31 3035 315d   "water": [1051]
+00000140: 2c0a 2020 2020 2020 2266 6174 223a 205b  ,.      "fat": [
+00000150: 3130 3034 2c20 3130 3835 5d2c 0a20 2020  1004, 1085],.   
+00000160: 2020 2022 6d6f 6e6f 2d75 6e73 6174 7572     "mono-unsatur
+00000170: 6174 6564 223a 205b 3132 3932 5d2c 0a20  ated": [1292],. 
+00000180: 2020 2020 2022 706f 6c79 2d75 6e73 6174       "poly-unsat
+00000190: 7572 6174 6564 223a 205b 3132 3933 5d2c  urated": [1293],
+000001a0: 0a20 2020 2020 2022 7361 7475 7261 7465  .      "saturate
+000001b0: 6422 3a20 5b31 3235 385d 2c0a 2020 2020  d": [1258],.    
+000001c0: 2020 2274 7261 6e73 223a 205b 3132 3537    "trans": [1257
+000001d0: 5d2c 0a20 2020 2020 2022 6368 6f6c 6573  ],.      "choles
+000001e0: 7465 726f 6c22 3a20 5b31 3235 335d 2c0a  terol": [1253],.
+000001f0: 2020 2020 2020 2270 726f 7465 696e 223a        "protein":
+00000200: 205b 3130 3033 5d2c 0a20 2020 2020 2022   [1003],.      "
+00000210: 6361 7262 6f68 7964 7261 7465 223a 205b  carbohydrate": [
+00000220: 3130 3035 5d2c 0a20 2020 2020 2022 6669  1005],.      "fi
+00000230: 6265 7222 3a20 5b31 3037 392c 2032 3033  ber": [1079, 203
+00000240: 335d 2c0a 2020 2020 2020 2273 7567 6172  3],.      "sugar
+00000250: 223a 205b 3130 3633 2c20 3230 3030 5d2c  ": [1063, 2000],
+00000260: 0a20 2020 2020 2022 7374 6172 6368 223a  .      "starch":
+00000270: 205b 3130 3039 5d2c 0a20 2020 2020 2022   [1009],.      "
+00000280: 7375 6372 6f73 6522 3a20 5b31 3031 305d  sucrose": [1010]
+00000290: 2c0a 2020 2020 2020 2267 6c75 636f 7365  ,.      "glucose
+000002a0: 223a 205b 3130 3131 5d2c 0a20 2020 2020  ": [1011],.     
+000002b0: 2022 6672 7563 746f 7365 223a 205b 3130   "fructose": [10
+000002c0: 3132 5d2c 0a20 2020 2020 2022 6c61 6374  12],.      "lact
+000002d0: 6f73 6522 3a20 5b31 3031 335d 2c0a 2020  ose": [1013],.  
+000002e0: 2020 2020 226d 616c 746f 7365 223a 205b      "maltose": [
+000002f0: 3130 3134 5d2c 0a20 2020 2020 2022 6761  1014],.      "ga
+00000300: 6c61 6374 6f73 6522 3a20 5b31 3037 355d  lactose": [1075]
+00000310: 2c0a 2020 2020 2020 2263 616c 6369 756d  ,.      "calcium
+00000320: 223a 205b 3130 3837 5d2c 0a20 2020 2020  ": [1087],.     
+00000330: 2022 636f 7070 6572 223a 205b 3130 3938   "copper": [1098
+00000340: 5d2c 0a20 2020 2020 2022 6972 6f6e 223a  ],.      "iron":
+00000350: 205b 3130 3839 5d2c 0a20 2020 2020 2022   [1089],.      "
+00000360: 6d61 676e 6573 6975 6d22 3a20 5b31 3039  magnesium": [109
+00000370: 305d 2c0a 2020 2020 2020 226d 616e 6761  0],.      "manga
+00000380: 6e65 7365 223a 205b 3131 3031 5d2c 0a20  nese": [1101],. 
+00000390: 2020 2020 2022 6d6f 6c79 6264 656e 756d       "molybdenum
+000003a0: 223a 205b 3131 3032 5d2c 0a20 2020 2020  ": [1102],.     
+000003b0: 2022 7068 6f73 7068 6f72 7573 223a 205b   "phosphorus": [
+000003c0: 3130 3931 5d2c 0a20 2020 2020 2022 706f  1091],.      "po
+000003d0: 7461 7373 6975 6d22 3a20 5b31 3039 325d  tassium": [1092]
+000003e0: 2c0a 2020 2020 2020 2273 656c 656e 6975  ,.      "seleniu
+000003f0: 6d22 3a20 5b31 3130 335d 2c0a 2020 2020  m": [1103],.    
+00000400: 2020 2273 6f64 6975 6d22 3a20 5b31 3039    "sodium": [109
+00000410: 335d 2c0a 2020 2020 2020 227a 696e 6322  3],.      "zinc"
+00000420: 3a20 5b31 3039 355d 2c0a 2020 2020 2020  : [1095],.      
+00000430: 2276 6974 616d 696e 2d61 223a 205b 3131  "vitamin-a": [11
+00000440: 3036 5d2c 0a20 2020 2020 2022 7265 7469  06],.      "reti
+00000450: 6e6f 6c22 3a20 5b31 3130 355d 2c0a 2020  nol": [1105],.  
+00000460: 2020 2020 2274 6869 616d 696e 223a 205b      "thiamin": [
+00000470: 3131 3635 5d2c 0a20 2020 2020 2022 7269  1165],.      "ri
+00000480: 626f 666c 6176 696e 223a 205b 3131 3636  boflavin": [1166
+00000490: 5d2c 0a20 2020 2020 2022 6e69 6163 696e  ],.      "niacin
+000004a0: 223a 205b 3131 3637 5d2c 0a20 2020 2020  ": [1167],.     
+000004b0: 2022 7061 6e74 6f74 6865 6e69 632d 6163   "pantothenic-ac
+000004c0: 6964 223a 205b 3131 3730 5d2c 0a20 2020  id": [1170],.   
+000004d0: 2020 2022 7669 7461 6d69 6e2d 6236 223a     "vitamin-b6":
+000004e0: 205b 3131 3735 5d2c 0a20 2020 2020 2022   [1175],.      "
+000004f0: 6269 6f74 696e 223a 205b 3131 3736 5d2c  biotin": [1176],
+00000500: 0a20 2020 2020 2022 666f 6c61 7465 223a  .      "folate":
+00000510: 205b 3131 3737 5d2c 0a20 2020 2020 2022   [1177],.      "
+00000520: 666f 6c69 632d 6163 6964 223a 205b 3131  folic-acid": [11
+00000530: 3836 5d2c 0a20 2020 2020 2022 7669 7461  86],.      "vita
+00000540: 6d69 6e2d 6231 3222 3a20 5b31 3137 385d  min-b12": [1178]
+00000550: 2c0a 2020 2020 2020 2263 686f 6c69 6e65  ,.      "choline
+00000560: 223a 205b 3131 3830 5d2c 0a20 2020 2020  ": [1180],.     
+00000570: 2022 7669 7461 6d69 6e2d 6322 3a20 5b31   "vitamin-c": [1
+00000580: 3136 325d 2c0a 2020 2020 2020 2276 6974  162],.      "vit
+00000590: 616d 696e 2d64 223a 205b 3131 3134 5d2c  amin-d": [1114],
+000005a0: 0a20 2020 2020 2022 7669 7461 6d69 6e2d  .      "vitamin-
+000005b0: 6522 3a20 5b31 3130 395d 2c0a 2020 2020  e": [1109],.    
+000005c0: 2020 2270 6879 6c6c 6f71 7569 6e6f 6e65    "phylloquinone
+000005d0: 223a 205b 3131 3835 5d2c 0a20 2020 2020  ": [1185],.     
+000005e0: 2022 6d65 6e61 7175 696e 6f6e 6522 3a20   "menaquinone": 
+000005f0: 5b31 3138 335d 2c0a 2020 2020 2020 2268  [1183],.      "h
+00000600: 6973 7469 6469 6e65 223a 205b 3132 3231  istidine": [1221
+00000610: 5d2c 0a20 2020 2020 2022 6973 6f6c 6575  ],.      "isoleu
+00000620: 6369 6e65 223a 205b 3132 3132 5d2c 0a20  cine": [1212],. 
+00000630: 2020 2020 2022 6c65 7563 696e 6522 3a20       "leucine": 
+00000640: 5b31 3231 335d 2c0a 2020 2020 2020 226c  [1213],.      "l
+00000650: 7973 696e 6522 3a20 5b31 3231 345d 2c0a  ysine": [1214],.
+00000660: 2020 2020 2020 226d 6574 6869 6f6e 696e        "methionin
+00000670: 6522 3a20 5b31 3231 355d 2c0a 2020 2020  e": [1215],.    
+00000680: 2020 2270 6865 6e79 6c61 6c61 6e69 6e65    "phenylalanine
+00000690: 223a 205b 3132 3137 5d2c 0a20 2020 2020  ": [1217],.     
+000006a0: 2022 7468 7265 6f6e 696e 6522 3a20 5b31   "threonine": [1
+000006b0: 3231 315d 2c0a 2020 2020 2020 2274 7279  211],.      "try
+000006c0: 7074 6f70 6861 6e22 3a20 5b31 3231 305d  ptophan": [1210]
+000006d0: 2c0a 2020 2020 2020 2276 616c 696e 6522  ,.      "valine"
+000006e0: 3a20 5b31 3231 395d 2c0a 2020 2020 2020  : [1219],.      
+000006f0: 2261 7267 696e 696e 6522 3a20 5b31 3232  "arginine": [122
+00000700: 305d 2c0a 2020 2020 2020 2263 7973 7469  0],.      "cysti
+00000710: 6e65 223a 205b 3132 3136 5d2c 0a20 2020  ne": [1216],.   
+00000720: 2020 2022 676c 7963 696e 6522 3a20 5b31     "glycine": [1
+00000730: 3232 355d 2c0a 2020 2020 2020 2270 726f  225],.      "pro
+00000740: 6c69 6e65 223a 205b 3132 3236 5d2c 0a20  line": [1226],. 
+00000750: 2020 2020 2022 7479 726f 7369 6e65 223a       "tyrosine":
+00000760: 205b 3132 3138 5d2c 0a20 2020 2020 2022   [1218],.      "
+00000770: 616c 616e 696e 6522 3a20 5b31 3232 325d  alanine": [1222]
+00000780: 2c0a 2020 2020 2020 2261 7370 6172 7469  ,.      "asparti
+00000790: 632d 6163 6964 223a 205b 3132 3233 5d2c  c-acid": [1223],
+000007a0: 0a20 2020 2020 2022 676c 7574 616d 6963  .      "glutamic
+000007b0: 2d61 6369 6422 3a20 5b31 3232 345d 2c0a  -acid": [1224],.
+000007c0: 2020 2020 2020 2273 6572 696e 6522 3a20        "serine": 
+000007d0: 5b31 3232 375d 2c0a 2020 2020 2020 2268  [1227],.      "h
+000007e0: 7964 726f 7879 7072 6f6c 696e 6522 3a20  ydroxyproline": 
+000007f0: 5b31 3232 385d 2c0a 2020 2020 2020 2263  [1228],.      "c
+00000800: 6166 6665 696e 6522 3a20 5b31 3035 375d  affeine": [1057]
+00000810: 2c0a 2020 2020 2020 2274 6865 6f62 726f  ,.      "theobro
+00000820: 6d69 6e65 223a 205b 3130 3538 5d0a 2020  mine": [1058].  
+00000830: 2020 7d0a 2020 7d2c 0a20 202f 2f20 576f    }.  },.  // Wo
+00000840: 726b 626f 6f6b 2070 6172 616d 6574 6572  rkbook parameter
+00000850: 7320 7573 6564 2062 7920 7468 6520 2761  s used by the 'a
+00000860: 6e61 6c79 7a65 2720 636f 6d6d 616e 640a  nalyze' command.
+00000870: 2020 2277 6f72 6b62 6f6f 6b5f 7365 7474    "workbook_sett
+00000880: 696e 6773 223a 207b 0a20 2020 2022 666f  ings": {.    "fo
+00000890: 6e74 5f6e 616d 6522 3a20 2248 656c 7665  nt_name": "Helve
+000008a0: 7469 6361 222c 0a20 2020 2022 666f 6e74  tica",.    "font
+000008b0: 5f73 697a 6522 3a20 3131 2c0a 2020 2020  _size": 11,.    
+000008c0: 226e 756d 6265 725f 666f 726d 6174 223a  "number_format":
+000008d0: 2022 232c 302e 3022 2c0a 2020 2020 2263   "#,0.0",.    "c
+000008e0: 6f6c 756d 6e5f 7069 7865 6c73 5f66 6f6f  olumn_pixels_foo
+000008f0: 6422 3a20 3136 352c 0a20 2020 2022 636f  d": 165,.    "co
+00000900: 6c75 6d6e 5f70 6978 656c 735f 6e75 7472  lumn_pixels_nutr
+00000910: 6965 6e74 223a 2035 352c 0a20 2020 2022  ient": 55,.    "
+00000920: 646f 5f6e 6f74 5f64 6973 706c 6179 223a  do_not_display":
+00000930: 205b 2277 6174 6572 222c 2022 7265 7469   ["water", "reti
+00000940: 6e6f 6c22 2c20 2266 6f6c 6963 2d61 6369  nol", "folic-aci
+00000950: 6422 5d2c 0a20 2020 2022 636f 6c6f 7273  d"],.    "colors
+00000960: 223a 207b 0a20 2020 2020 2022 666f 6f64  ": {.      "food
+00000970: 223a 205b 2223 3030 3030 3030 222c 2022  ": ["#000000", "
+00000980: 2346 4646 4646 4622 5d2c 0a20 2020 2020  #FFFFFF"],.     
+00000990: 2022 616d 6f75 6e74 223a 205b 2223 3046   "amount": ["#0F
+000009a0: 3234 3345 222c 2022 2344 4345 3646 3122  243E", "#DCE6F1"
+000009b0: 5d2c 0a20 2020 2020 2022 656e 6572 6779  ],.      "energy
+000009c0: 223a 205b 2223 3430 3331 3531 222c 2022  ": ["#403151", "
+000009d0: 2345 3444 4645 4322 5d2c 0a20 2020 2020  #E4DFEC"],.     
+000009e0: 2022 7761 7465 7222 3a20 5b22 2330 3030   "water": ["#000
+000009f0: 3030 3022 2c20 2223 4646 4646 4646 225d  000", "#FFFFFF"]
+00000a00: 2c0a 2020 2020 2020 2266 6174 7322 3a20  ,.      "fats": 
+00000a10: 5b22 2330 3030 3030 3022 2c20 2223 4646  ["#000000", "#FF
+00000a20: 4646 4646 225d 2c0a 2020 2020 2020 2270  FFFF"],.      "p
+00000a30: 726f 7465 696e 7322 3a20 5b22 2339 3734  roteins": ["#974
+00000a40: 3731 4122 2c20 2223 4643 4539 4439 225d  71A", "#FCE9D9"]
+00000a50: 2c0a 2020 2020 2020 2263 6172 626f 6879  ,.      "carbohy
+00000a60: 6472 6174 6573 223a 205b 2223 3030 3030  drates": ["#0000
+00000a70: 3030 222c 2022 2346 4646 4646 4622 5d2c  00", "#FFFFFF"],
+00000a80: 0a20 2020 2020 2022 6d69 6e65 7261 6c73  .      "minerals
+00000a90: 223a 205b 2223 3439 3435 3239 222c 2022  ": ["#494529", "
+00000aa0: 2344 4444 3943 3422 5d2c 0a20 2020 2020  #DDD9C4"],.     
+00000ab0: 2022 7669 7461 6d69 6e73 223a 205b 2223   "vitamins": ["#
+00000ac0: 3030 3030 3030 222c 2022 2346 4646 4646  000000", "#FFFFF
+00000ad0: 4622 5d2c 0a20 2020 2020 2022 616c 6b61  F"],.      "alka
+00000ae0: 6c6f 6964 7322 3a20 5b22 2330 3030 3030  loids": ["#00000
+00000af0: 3022 2c20 2223 4646 4646 4646 225d 0a20  0", "#FFFFFF"]. 
+00000b00: 2020 207d 2c0a 2020 2020 2274 6f74 616c     },.    "total
+00000b10: 5f62 675f 636f 6c6f 7222 3a20 2223 4632  _bg_color": "#F2
+00000b20: 4632 4632 222c 0a20 2020 2022 6772 616e  F2F2",.    "gran
+00000b30: 645f 746f 7461 6c5f 6267 5f63 6f6c 6f72  d_total_bg_color
+00000b40: 223a 2022 2344 3944 3944 3922 2c0a 2020  ": "#D9D9D9",.  
+00000b50: 2020 2265 6e65 7267 795f 6267 5f63 6f6c    "energy_bg_col
+00000b60: 6f72 223a 2022 2346 3646 4243 3722 2c0a  or": "#F6FBC7",.
+00000b70: 2020 2020 2264 7269 5f63 6f6c 6f72 7322      "dri_colors"
+00000b80: 3a20 7b0a 2020 2020 2020 2265 7863 6573  : {.      "exces
+00000b90: 735f 3122 3a20 2223 4542 4631 4445 222c  s_1": "#EBF1DE",
+00000ba0: 0a20 2020 2020 2022 6578 6365 7373 5f32  .      "excess_2
+00000bb0: 223a 2022 2344 3845 3442 4322 2c0a 2020  ": "#D8E4BC",.  
+00000bc0: 2020 2020 2265 7863 6573 735f 3322 3a20      "excess_3": 
+00000bd0: 2223 4334 4437 3942 222c 0a20 2020 2020  "#C4D79B",.     
+00000be0: 2022 6465 6669 6369 745f 3122 3a20 2223   "deficit_1": "#
+00000bf0: 4632 4443 4442 222c 0a20 2020 2020 2022  F2DCDB",.      "
+00000c00: 6465 6669 6369 745f 3222 3a20 2223 4536  deficit_2": "#E6
+00000c10: 4238 4237 222c 0a20 2020 2020 2022 6465  B8B7",.      "de
+00000c20: 6669 6369 745f 3322 3a20 2223 4441 3936  ficit_3": "#DA96
+00000c30: 3934 220a 2020 2020 7d2c 0a20 2020 2022  94".    },.    "
+00000c40: 636f 6c75 6d6e 735f 7365 7061 7261 746f  columns_separato
+00000c50: 7273 223a 205b 322c 2032 302c 2033 312c  rs": [2, 20, 31,
+00000c60: 2034 362c 2035 352c 2036 355d 2c0a 2020   46, 55, 65],.  
+00000c70: 2020 2274 6172 6765 7422 3a20 7b0a 2020    "target": {.  
+00000c80: 2020 2020 2266 6f6e 745f 636f 6c6f 7222      "font_color"
+00000c90: 3a20 2223 3030 3030 3030 222c 0a20 2020  : "#000000",.   
+00000ca0: 2020 2022 626f 6479 5f6d 6173 735f 6267     "body_mass_bg
+00000cb0: 5f63 6f6c 6f72 223a 2022 2344 3944 3944  _color": "#D9D9D
+00000cc0: 3922 2c0a 2020 2020 2020 2262 6f64 795f  9",.      "body_
+00000cd0: 6661 745f 6267 5f63 6f6c 6f72 223a 2022  fat_bg_color": "
+00000ce0: 2346 3246 3246 3222 2c0a 2020 2020 2020  #F2F2F2",.      
+00000cf0: 226c 6561 6e5f 626f 6479 5f6d 6173 735f  "lean_body_mass_
+00000d00: 6267 5f63 6f6c 6f72 223a 2022 2344 4345  bg_color": "#DCE
+00000d10: 3646 3122 2c0a 2020 2020 2020 2263 6f6c  6F1",.      "col
+00000d20: 756d 6e5f 7069 7865 6c73 5f6c 6162 656c  umn_pixels_label
+00000d30: 223a 2032 3630 2c0a 2020 2020 2020 2263  ": 260,.      "c
+00000d40: 6f6c 756d 6e5f 7069 7865 6c73 5f76 616c  olumn_pixels_val
+00000d50: 7565 223a 2039 302c 0a20 2020 2020 2022  ue": 90,.      "
+00000d60: 636f 6c75 6d6e 5f70 6978 656c 735f 7365  column_pixels_se
+00000d70: 7061 7261 746f 7222 3a20 3230 0a20 2020  parator": 20.   
+00000d80: 207d 0a20 207d 0a7d 0a                    }.  }.}.
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/almond_170567.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/almond_170567.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/almond_butter_168588.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/almond_butter_168588.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/apple_171688.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/mushroom_portabella_169255.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6994485294117647%*

 * *Differences: {"'description'": "'Mushrooms, portabella, raw'",*

 * * "'name'": "'Mushroom Portabella'",*

 * * "'nutrients'": "{'energy': 22.0, 'water': 92.82, 'fat': 0.35, 'mono-unsaturated': 0.044, "*

 * *                "'poly-unsaturated': 0.296, 'saturated': 0.01, 'protein': 2.11, 'carbohydrate': "*

 * *                "3.87, 'fiber': 1.3, 'sugar': 2.5, 'starch': 0, 'sucrose': 0.0, 'glucose': 2.01, "*

 * *                "'fructose': 0.49, 'calcium': 0.003, 'copper': 0.00028599999999999996, 'iron': "*

 * *                "0.00031, 'magnesium': 0 […]*

```diff
@@ -1,75 +1,75 @@
 {
     "amount": 100,
-    "description": "Apples, raw, with skin (Includes foods for USDA's Food Distribution Program)",
-    "name": "Apple",
+    "description": "Mushrooms, portabella, raw",
+    "name": "Mushroom Portabella",
     "nutrients": {
-        "alanine": 0.011,
-        "arginine": 0.006,
-        "aspartic-acid": 0.07,
+        "alanine": 0.168,
+        "arginine": 0.082,
+        "aspartic-acid": 0.221,
         "biotin": 0,
         "caffeine": 0.0,
-        "calcium": 0.006,
-        "carbohydrate": 13.81,
+        "calcium": 0.003,
+        "carbohydrate": 3.87,
         "cholesterol": 0.0,
-        "choline": 0.0034,
-        "copper": 2.7e-05,
-        "cystine": 0.001,
-        "energy": 52.0,
-        "fat": 0.17,
-        "fiber": 2.4,
-        "folate": 3e-06,
+        "choline": 0.0212,
+        "copper": 0.00028599999999999996,
+        "cystine": 0.01,
+        "energy": 22.0,
+        "fat": 0.35,
+        "fiber": 1.3,
+        "folate": 2.8e-05,
         "folic-acid": 0.0,
-        "fructose": 5.9,
+        "fructose": 0.49,
         "galactose": 0.0,
-        "glucose": 2.43,
-        "glutamic-acid": 0.025,
-        "glycine": 0.009,
-        "histidine": 0.005,
+        "glucose": 2.01,
+        "glutamic-acid": 0.319,
+        "glycine": 0.096,
+        "histidine": 0.058,
         "hydroxyproline": 0,
-        "iron": 0.00012,
-        "isoleucine": 0.006,
+        "iron": 0.00031,
+        "isoleucine": 0.082,
         "lactose": 0.0,
-        "leucine": 0.013,
-        "lysine": 0.012,
-        "magnesium": 0.005,
+        "leucine": 0.13,
+        "lysine": 0.122,
+        "magnesium": 0,
         "maltose": 0.0,
-        "manganese": 3.5000000000000004e-05,
-        "menaquinone": 0,
-        "methionine": 0.001,
+        "manganese": 6.900000000000001e-05,
+        "menaquinone": 0.0,
+        "methionine": 0.029,
         "molybdenum": 0,
-        "mono-unsaturated": 0.007,
-        "niacin": 9.1e-05,
-        "pantothenic-acid": 6.1e-05,
-        "phenylalanine": 0.006,
-        "phosphorus": 0.011,
-        "phylloquinone": 2.2e-06,
-        "poly-unsaturated": 0.051,
-        "potassium": 0.107,
-        "proline": 0.006,
-        "protein": 0.26,
+        "mono-unsaturated": 0.044,
+        "niacin": 0.004494,
+        "pantothenic-acid": 0.00114,
+        "phenylalanine": 0.076,
+        "phosphorus": 0.108,
+        "phylloquinone": 0.0,
+        "poly-unsaturated": 0.296,
+        "potassium": 0.364,
+        "proline": 0.076,
+        "protein": 2.11,
         "retinol": 0.0,
-        "riboflavin": 2.6e-05,
-        "saturated": 0.028,
-        "selenium": 0.0,
-        "serine": 0.01,
-        "sodium": 0.001,
-        "starch": 0.05,
-        "sucrose": 2.07,
-        "sugar": 10.39,
+        "riboflavin": 0.00013000000000000002,
+        "saturated": 0.01,
+        "selenium": 1.86e-05,
+        "serine": 0.092,
+        "sodium": 0.009000000000000001,
+        "starch": 0,
+        "sucrose": 0.0,
+        "sugar": 2.5,
         "theobromine": 0.0,
-        "thiamin": 1.7000000000000003e-05,
-        "threonine": 0.006,
+        "thiamin": 5.9e-05,
+        "threonine": 0.101,
         "trans": 0.0,
-        "tryptophan": 0.001,
-        "tyrosine": 0.001,
-        "valine": 0.012,
-        "vitamin-a": 3e-06,
-        "vitamin-b12": 0.0,
-        "vitamin-b6": 4.1e-05,
-        "vitamin-c": 0.0046,
-        "vitamin-d": 0.0,
-        "vitamin-e": 0.00017999999999999998,
-        "water": 85.56,
-        "zinc": 4e-05
+        "tryptophan": 0.035,
+        "tyrosine": 0.014,
+        "valine": 0.076,
+        "vitamin-a": 0.0,
+        "vitamin-b12": 5e-08,
+        "vitamin-b6": 0.000148,
+        "vitamin-c": 0.0,
+        "vitamin-d": 3e-07,
+        "vitamin-e": 2e-05,
+        "water": 92.82,
+        "zinc": 0.0005300000000000001
     }
 }
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/apple_cider_vinegar_173469.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/apple_cider_vinegar_173469.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/apricot_171697.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/apricot_171697.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/asparagus_168389.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/asparagus_168389.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/avocado_171705.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/avocado_171705.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/banana_173944.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/banana_173944.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/beef_ground_80-20_174036.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/beef_ground_80-20_174036.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/beef_ground_90-10_174030.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/beef_ground_90-10_174030.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/beetroot_169145.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/beetroot_169145.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_green_2258588.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_green_2258588.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_orange_2258591.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_orange_2258591.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_red_2258590.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_red_2258590.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/bell_pepper_yellow_2258589.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/bell_pepper_yellow_2258589.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/blueberry_171711.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/blueberry_171711.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/brewed_coffee_171890.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/brewed_coffee_171890.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/broccoli_170379.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/broccoli_170379.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/brussels_sprout_170383.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/brussels_sprout_170383.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/butter_173430.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/butter_173430.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/carrot_170393.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/carrot_170393.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/cauliflower_169986.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/cauliflower_169986.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/cheddar_cheese_173414.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/pinto_bean_175199.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6957720588235294%*

 * *Differences: {"'description'": '"Beans, pinto, mature seeds, raw (Includes foods for USDA\'s Food Distribution '*

 * *                  'Program)"',*

 * * "'name'": "'Pinto Bean'",*

 * * "'nutrients'": "{'energy': 347.0, 'water': 11.33, 'fat': 1.23, 'mono-unsaturated': 0.229, "*

 * *                "'poly-unsaturated': 0.407, 'saturated': 0.235, 'cholesterol': 0.0, 'protein': "*

 * *                "21.42, 'carbohydrate': 62.55, 'fiber': 15.5, 'sugar': 2.11, 'starch': 34.17, "*

 * *                "'sucrose': 1.98, 'glucose': 0.13, 'lactose': 0.0, ' […]*

```diff
@@ -1,75 +1,75 @@
 {
     "amount": 100,
-    "description": "Cheese, cheddar (Includes foods for USDA's Food Distribution Program)",
-    "name": "Cheddar Cheese",
+    "description": "Beans, pinto, mature seeds, raw (Includes foods for USDA's Food Distribution Program)",
+    "name": "Pinto Bean",
     "nutrients": {
-        "alanine": 0.751,
-        "arginine": 0.547,
-        "aspartic-acid": 1.734,
+        "alanine": 0.872,
+        "arginine": 1.096,
+        "aspartic-acid": 2.268,
         "biotin": 0,
         "caffeine": 0.0,
-        "calcium": 0.71,
-        "carbohydrate": 3.37,
-        "cholesterol": 0.099,
-        "choline": 0.0165,
-        "copper": 3e-05,
-        "cystine": 0.123,
-        "energy": 403.0,
-        "fat": 33.31,
-        "fiber": 0.0,
-        "folate": 2.7e-05,
+        "calcium": 0.113,
+        "carbohydrate": 62.55,
+        "cholesterol": 0.0,
+        "choline": 0.06620000000000001,
+        "copper": 0.000893,
+        "cystine": 0.187,
+        "energy": 347.0,
+        "fat": 1.23,
+        "fiber": 15.5,
+        "folate": 0.000525,
         "folic-acid": 0.0,
         "fructose": 0.0,
-        "galactose": 0.1,
-        "glucose": 0.26,
-        "glutamic-acid": 4.735,
-        "glycine": 0.547,
-        "histidine": 0.547,
+        "galactose": 0.0,
+        "glucose": 0.13,
+        "glutamic-acid": 3.027,
+        "glycine": 0.796,
+        "histidine": 0.556,
         "hydroxyproline": 0,
-        "iron": 0.00014000000000000001,
-        "isoleucine": 1.206,
-        "lactose": 0.12,
-        "leucine": 1.939,
-        "lysine": 1.025,
-        "magnesium": 0.027,
+        "iron": 0.005070000000000001,
+        "isoleucine": 0.871,
+        "lactose": 0.0,
+        "leucine": 1.558,
+        "lysine": 1.356,
+        "magnesium": 0.176,
         "maltose": 0.0,
-        "manganese": 2.7e-05,
-        "menaquinone": 8.599999999999999e-06,
-        "methionine": 0.547,
+        "manganese": 0.001148,
+        "menaquinone": 0,
+        "methionine": 0.259,
         "molybdenum": 0,
-        "mono-unsaturated": 9.391,
-        "niacin": 5.9e-05,
-        "pantothenic-acid": 0.00041,
-        "phenylalanine": 1.074,
-        "phosphorus": 0.455,
-        "phylloquinone": 2.4e-06,
-        "poly-unsaturated": 0.942,
-        "potassium": 0.076,
-        "proline": 2.497,
-        "protein": 22.87,
-        "retinol": 0.00033,
-        "riboflavin": 0.000428,
-        "saturated": 18.867,
-        "selenium": 2.8499999999999998e-05,
-        "serine": 0.78,
-        "sodium": 0.653,
-        "starch": 0,
-        "sucrose": 0.0,
-        "sugar": 0.48,
+        "mono-unsaturated": 0.229,
+        "niacin": 0.001174,
+        "pantothenic-acid": 0.000785,
+        "phenylalanine": 1.095,
+        "phosphorus": 0.41100000000000003,
+        "phylloquinone": 5.6e-06,
+        "poly-unsaturated": 0.407,
+        "potassium": 1.393,
+        "proline": 1.072,
+        "protein": 21.42,
+        "retinol": 0.0,
+        "riboflavin": 0.000212,
+        "saturated": 0.235,
+        "selenium": 2.7899999999999997e-05,
+        "serine": 1.171,
+        "sodium": 0.012,
+        "starch": 34.17,
+        "sucrose": 1.98,
+        "sugar": 2.11,
         "theobromine": 0.0,
-        "thiamin": 2.9000000000000004e-05,
-        "threonine": 1.044,
-        "trans": 0,
-        "tryptophan": 0.547,
-        "tyrosine": 1.108,
-        "valine": 1.404,
-        "vitamin-a": 0.000337,
-        "vitamin-b12": 1.1e-06,
-        "vitamin-b6": 6.6e-05,
-        "vitamin-c": 0.0,
-        "vitamin-d": 6e-07,
-        "vitamin-e": 0.00071,
-        "water": 36.75,
-        "zinc": 0.00364
+        "thiamin": 0.000713,
+        "threonine": 0.81,
+        "trans": 0.0,
+        "tryptophan": 0.237,
+        "tyrosine": 0.427,
+        "valine": 0.998,
+        "vitamin-a": 0.0,
+        "vitamin-b12": 0.0,
+        "vitamin-b6": 0.000474,
+        "vitamin-c": 0.0063,
+        "vitamin-d": 0.0,
+        "vitamin-e": 0.00021,
+        "water": 11.33,
+        "zinc": 0.00228
     }
 }
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/chicken_breast_171077.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/chicken_breast_171077.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/clementine_168195.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/clementine_168195.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/cocoa_powder_169593.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/cocoa_powder_169593.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/coconut_meat_170169.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/coconut_meat_170169.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/coconut_water_170174.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/coconut_water_170174.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/egg_white_172183.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/egg_white_172183.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/egg_yolk_172184.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/egg_yolk_172184.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/flaxseed_169414.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/flaxseed_169414.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/garlic_169230.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/garlic_169230.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/grape_tomato_321360.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/tomato_grape_321360.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.875%*

 * *Differences: {"'name'": "'Tomato Grape'"}*

```diff
@@ -1,11 +1,11 @@
 {
     "amount": 100,
     "description": "Tomatoes, grape, raw",
-    "name": "Grape Tomato",
+    "name": "Tomato Grape",
     "nutrients": {
         "alanine": 0,
         "arginine": 0,
         "aspartic-acid": 0,
         "biotin": 0,
         "caffeine": 0,
         "calcium": 0.011,
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/greek_yogurt_whole_milk_2259794.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/cumin_seed_170923.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.71875%*

 * *Differences: {"'description'": "'Spices, cumin seed'",*

 * * "'name'": "'Cumin Seed'",*

 * * "'nutrients'": "{'energy': 375.0, 'water': 8.06, 'fat': 22.27, 'mono-unsaturated': 14.04, "*

 * *                "'poly-unsaturated': 3.279, 'saturated': 1.535, 'cholesterol': 0.0, 'protein': "*

 * *                "17.81, 'carbohydrate': 44.24, 'fiber': 10.5, 'sugar': 2.25, 'lactose': 0, "*

 * *                "'galactose': 0, 'calcium': 0.931, 'copper': 0.000867, 'iron': 0.06636, "*

 * *                "'magnesium': 0.366, 'manganese': 0.003333000000000000 […]*

```diff
@@ -1,75 +1,75 @@
 {
     "amount": 100,
-    "description": "Yogurt, Greek, plain, whole milk",
-    "name": "Greek Yogurt Whole Milk",
+    "description": "Spices, cumin seed",
+    "name": "Cumin Seed",
     "nutrients": {
         "alanine": 0,
         "arginine": 0,
         "aspartic-acid": 0,
-        "biotin": 0.0,
-        "caffeine": 0,
-        "calcium": 0.11090000000000001,
-        "carbohydrate": 4.75402,
-        "cholesterol": 0.01684,
-        "choline": 0,
-        "copper": 9.513e-06,
+        "biotin": 0,
+        "caffeine": 0.0,
+        "calcium": 0.931,
+        "carbohydrate": 44.24,
+        "cholesterol": 0.0,
+        "choline": 0.0247,
+        "copper": 0.000867,
         "cystine": 0,
-        "energy": 94.507135,
-        "fat": 4.394,
-        "fiber": 0,
-        "folate": 0,
-        "folic-acid": 0,
-        "fructose": 0.0,
-        "galactose": 0.6394,
-        "glucose": 0.0,
+        "energy": 375.0,
+        "fat": 22.27,
+        "fiber": 10.5,
+        "folate": 9.999999999999999e-06,
+        "folic-acid": 0.0,
+        "fructose": 0,
+        "galactose": 0,
+        "glucose": 0,
         "glutamic-acid": 0,
         "glycine": 0,
         "histidine": 0,
         "hydroxyproline": 0,
-        "iron": 0.0,
+        "iron": 0.06636,
         "isoleucine": 0,
-        "lactose": 2.608,
+        "lactose": 0,
         "leucine": 0,
         "lysine": 0,
-        "magnesium": 0.0107,
-        "maltose": 0.0,
-        "manganese": 5.738e-06,
+        "magnesium": 0.366,
+        "maltose": 0,
+        "manganese": 0.0033330000000000005,
         "menaquinone": 0,
         "methionine": 0,
         "molybdenum": 0,
-        "mono-unsaturated": 0.9575,
-        "niacin": 0.00022689999999999999,
+        "mono-unsaturated": 14.04,
+        "niacin": 0.004579,
         "pantothenic-acid": 0,
         "phenylalanine": 0,
-        "phosphorus": 0.1259,
-        "phylloquinone": 0,
-        "poly-unsaturated": 0,
-        "potassium": 0.1469,
+        "phosphorus": 0.499,
+        "phylloquinone": 5.4e-06,
+        "poly-unsaturated": 3.279,
+        "potassium": 1.788,
         "proline": 0,
-        "protein": 8.77888,
-        "retinol": 3.813e-05,
-        "riboflavin": 0.00024440000000000003,
-        "saturated": 2.393,
-        "selenium": 0,
+        "protein": 17.81,
+        "retinol": 0.0,
+        "riboflavin": 0.00032700000000000003,
+        "saturated": 1.535,
+        "selenium": 5.2e-06,
         "serine": 0,
-        "sodium": 0.03376,
+        "sodium": 0.168,
         "starch": 0,
-        "sucrose": 0.0,
-        "sugar": 3.2474,
-        "theobromine": 0,
-        "thiamin": 5.525e-05,
+        "sucrose": 0,
+        "sugar": 2.25,
+        "theobromine": 0.0,
+        "thiamin": 0.000628,
         "threonine": 0,
         "trans": 0,
         "tryptophan": 0,
         "tyrosine": 0,
         "valine": 0,
-        "vitamin-a": 0,
-        "vitamin-b12": 0,
-        "vitamin-b6": 4.394e-05,
-        "vitamin-c": 0,
+        "vitamin-a": 6.4e-05,
+        "vitamin-b12": 0.0,
+        "vitamin-b6": 0.000435,
+        "vitamin-c": 0.0077,
         "vitamin-d": 0.0,
-        "vitamin-e": 0,
-        "water": 81.32,
-        "zinc": 0.000473
+        "vitamin-e": 0.00333,
+        "water": 8.06,
+        "zinc": 0.0048
     }
 }
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/green_olive_169096.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/green_olive_169096.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/heavy_cream_170859.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/heavy_cream_170859.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/honey_169640.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/honey_169640.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/lemon_167746.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/lemon_167746.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/lettuce_romaine_169247.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/lettuce_romaine_169247.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/macadamia_nut_170178.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/macadamia_nut_170178.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/oat_rolled_2346396.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/oat_rolled_2346396.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/oat_steel_cut_2346397.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/oat_steel_cut_2346397.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/olive_oil_171413.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/olive_oil_171413.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/oyster_eastern_171978.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/oyster_eastern_171978.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/oyster_pacific_174219.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/oyster_pacific_174219.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/pecan_nut_170182.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/pecan_nut_170182.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/pistachio_170184.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/pistachio_170184.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/pork_bacon_167914.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/sardine_175139.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.703125%*

 * *Differences: {"'description'": "'Fish, sardine, Atlantic, canned in oil, drained solids with bone'",*

 * * "'name'": "'Sardine'",*

 * * "'nutrients'": "{'energy': 208.0, 'water': 59.61, 'fat': 11.45, 'mono-unsaturated': 3.869, "*

 * *                "'poly-unsaturated': 5.148, 'saturated': 1.528, 'cholesterol': "*

 * *                "0.14200000000000002, 'protein': 24.62, 'carbohydrate': 0.0, 'calcium': 0.382, "*

 * *                "'copper': 0.000186, 'iron': 0.00292, 'magnesium': 0.039, 'manganese': 0.000108, "*

 * *                "'phosphorus' […]*

```diff
@@ -1,75 +1,75 @@
 {
     "amount": 100,
-    "description": "Pork, cured, bacon, cooked, baked",
-    "name": "Pork Bacon",
+    "description": "Fish, sardine, Atlantic, canned in oil, drained solids with bone",
+    "name": "Sardine",
     "nutrients": {
-        "alanine": 2.286,
-        "arginine": 2.314,
-        "aspartic-acid": 3.362,
+        "alanine": 1.489,
+        "arginine": 1.473,
+        "aspartic-acid": 2.52,
         "biotin": 0,
         "caffeine": 0.0,
-        "calcium": 0.01,
-        "carbohydrate": 1.35,
-        "cholesterol": 0.107,
-        "choline": 0.1193,
-        "copper": 0.000182,
-        "cystine": 0.397,
-        "energy": 548.0,
-        "fat": 43.27,
+        "calcium": 0.382,
+        "carbohydrate": 0.0,
+        "cholesterol": 0.14200000000000002,
+        "choline": 0.075,
+        "copper": 0.000186,
+        "cystine": 0.264,
+        "energy": 208.0,
+        "fat": 11.45,
         "fiber": 0.0,
-        "folate": 2e-06,
+        "folate": 9.999999999999999e-06,
         "folic-acid": 0.0,
         "fructose": 0,
         "galactose": 0,
         "glucose": 0,
-        "glutamic-acid": 5.26,
-        "glycine": 2.508,
-        "histidine": 1.343,
-        "hydroxyproline": 0.628,
-        "iron": 0.00149,
-        "isoleucine": 1.676,
+        "glutamic-acid": 3.674,
+        "glycine": 1.181,
+        "histidine": 0.725,
+        "hydroxyproline": 0,
+        "iron": 0.00292,
+        "isoleucine": 1.134,
         "lactose": 0,
-        "leucine": 2.782,
-        "lysine": 2.964,
-        "magnesium": 0.03,
+        "leucine": 2.001,
+        "lysine": 2.26,
+        "magnesium": 0.039,
         "maltose": 0,
-        "manganese": 2.2e-05,
+        "manganese": 0.000108,
         "menaquinone": 0,
-        "methionine": 0.795,
+        "methionine": 0.729,
         "molybdenum": 0,
-        "mono-unsaturated": 19.065,
-        "niacin": 0.010622999999999999,
-        "pantothenic-acid": 0.0010329999999999998,
-        "phenylalanine": 1.417,
-        "phosphorus": 0.506,
-        "phylloquinone": 1e-07,
-        "poly-unsaturated": 4.859,
-        "potassium": 0.539,
-        "proline": 1.96,
-        "protein": 35.73,
-        "retinol": 1.1e-05,
-        "riboflavin": 0.00025100000000000003,
-        "saturated": 14.187,
-        "selenium": 5.9e-05,
-        "serine": 1.359,
-        "sodium": 2.193,
+        "mono-unsaturated": 3.869,
+        "niacin": 0.0052450000000000005,
+        "pantothenic-acid": 0.000642,
+        "phenylalanine": 0.961,
+        "phosphorus": 0.49,
+        "phylloquinone": 2.6e-06,
+        "poly-unsaturated": 5.148,
+        "potassium": 0.397,
+        "proline": 0.87,
+        "protein": 24.62,
+        "retinol": 3.2e-05,
+        "riboflavin": 0.00022700000000000002,
+        "saturated": 1.528,
+        "selenium": 5.27e-05,
+        "serine": 1.004,
+        "sodium": 0.307,
         "starch": 0,
         "sucrose": 0,
         "sugar": 0.0,
         "theobromine": 0.0,
-        "thiamin": 0.000348,
-        "threonine": 1.399,
-        "trans": 0.0,
-        "tryptophan": 0.299,
-        "tyrosine": 1.119,
-        "valine": 1.901,
-        "vitamin-a": 1.1e-05,
-        "vitamin-b12": 1.16e-06,
-        "vitamin-b6": 0.00030900000000000003,
+        "thiamin": 8e-05,
+        "threonine": 1.079,
+        "trans": 0,
+        "tryptophan": 0.276,
+        "tyrosine": 0.831,
+        "valine": 1.268,
+        "vitamin-a": 3.2e-05,
+        "vitamin-b12": 8.939999999999999e-06,
+        "vitamin-b6": 0.00016700000000000002,
         "vitamin-c": 0.0,
-        "vitamin-d": 0,
-        "vitamin-e": 0.00032,
-        "water": 12.52,
-        "zinc": 0.00336
+        "vitamin-d": 4.8e-06,
+        "vitamin-e": 0.00204,
+        "water": 59.61,
+        "zinc": 0.0013100000000000002
     }
 }
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/salmon_atlantic_173686.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/salmon_atlantic_173686.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/salmon_sockeye_173691.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/salmon_sockeye_173691.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/salt_173468.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/salt_173468.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/sardine_175139.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/gruyere_cheese_171242.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7040441176470589%*

 * *Differences: {"'description'": "'Cheese, gruyere'",*

 * * "'name'": "'Gruyere Cheese'",*

 * * "'nutrients'": "{'energy': 413.0, 'water': 33.19, 'fat': 32.34, 'mono-unsaturated': 10.043, "*

 * *                "'poly-unsaturated': 1.733, 'saturated': 18.913, 'cholesterol': 0.11, 'protein': "*

 * *                "29.81, 'carbohydrate': 0.36, 'sugar': 0.36, 'calcium': 1.0110000000000001, "*

 * *                "'copper': 3.2e-05, 'iron': 0.00017, 'magnesium': 0.036000000000000004, "*

 * *                "'manganese': 1.7000000000000003e-05, 'phosphoru […]*

```diff
@@ -1,75 +1,75 @@
 {
     "amount": 100,
-    "description": "Fish, sardine, Atlantic, canned in oil, drained solids with bone",
-    "name": "Sardine",
+    "description": "Cheese, gruyere",
+    "name": "Gruyere Cheese",
     "nutrients": {
-        "alanine": 1.489,
-        "arginine": 1.473,
-        "aspartic-acid": 2.52,
+        "alanine": 0.958,
+        "arginine": 0.972,
+        "aspartic-acid": 1.645,
         "biotin": 0,
         "caffeine": 0.0,
-        "calcium": 0.382,
-        "carbohydrate": 0.0,
-        "cholesterol": 0.14200000000000002,
-        "choline": 0.075,
-        "copper": 0.000186,
-        "cystine": 0.264,
-        "energy": 208.0,
-        "fat": 11.45,
+        "calcium": 1.0110000000000001,
+        "carbohydrate": 0.36,
+        "cholesterol": 0.11,
+        "choline": 0.0154,
+        "copper": 3.2e-05,
+        "cystine": 0.304,
+        "energy": 413.0,
+        "fat": 32.34,
         "fiber": 0.0,
         "folate": 9.999999999999999e-06,
         "folic-acid": 0.0,
         "fructose": 0,
         "galactose": 0,
         "glucose": 0,
-        "glutamic-acid": 3.674,
-        "glycine": 1.181,
-        "histidine": 0.725,
+        "glutamic-acid": 5.981,
+        "glycine": 0.533,
+        "histidine": 1.117,
         "hydroxyproline": 0,
-        "iron": 0.00292,
-        "isoleucine": 1.134,
+        "iron": 0.00017,
+        "isoleucine": 1.612,
         "lactose": 0,
-        "leucine": 2.001,
-        "lysine": 2.26,
-        "magnesium": 0.039,
+        "leucine": 3.102,
+        "lysine": 2.71,
+        "magnesium": 0.036000000000000004,
         "maltose": 0,
-        "manganese": 0.000108,
+        "manganese": 1.7000000000000003e-05,
         "menaquinone": 0,
-        "methionine": 0.729,
+        "methionine": 0.822,
         "molybdenum": 0,
-        "mono-unsaturated": 3.869,
-        "niacin": 0.0052450000000000005,
-        "pantothenic-acid": 0.000642,
-        "phenylalanine": 0.961,
-        "phosphorus": 0.49,
-        "phylloquinone": 2.6e-06,
-        "poly-unsaturated": 5.148,
-        "potassium": 0.397,
-        "proline": 0.87,
-        "protein": 24.62,
-        "retinol": 3.2e-05,
-        "riboflavin": 0.00022700000000000002,
-        "saturated": 1.528,
-        "selenium": 5.27e-05,
-        "serine": 1.004,
-        "sodium": 0.307,
+        "mono-unsaturated": 10.043,
+        "niacin": 0.000106,
+        "pantothenic-acid": 0.0005620000000000001,
+        "phenylalanine": 1.743,
+        "phosphorus": 0.605,
+        "phylloquinone": 2.7e-06,
+        "poly-unsaturated": 1.733,
+        "potassium": 0.081,
+        "proline": 3.869,
+        "protein": 29.81,
+        "retinol": 0.000268,
+        "riboflavin": 0.000279,
+        "saturated": 18.913,
+        "selenium": 1.45e-05,
+        "serine": 1.719,
+        "sodium": 0.714,
         "starch": 0,
         "sucrose": 0,
-        "sugar": 0.0,
+        "sugar": 0.36,
         "theobromine": 0.0,
-        "thiamin": 8e-05,
-        "threonine": 1.079,
+        "thiamin": 6e-05,
+        "threonine": 1.089,
         "trans": 0,
-        "tryptophan": 0.276,
-        "tyrosine": 0.831,
-        "valine": 1.268,
-        "vitamin-a": 3.2e-05,
-        "vitamin-b12": 8.939999999999999e-06,
-        "vitamin-b6": 0.00016700000000000002,
+        "tryptophan": 0.421,
+        "tyrosine": 1.776,
+        "valine": 2.243,
+        "vitamin-a": 0.000271,
+        "vitamin-b12": 1.6e-06,
+        "vitamin-b6": 8.1e-05,
         "vitamin-c": 0.0,
-        "vitamin-d": 4.8e-06,
-        "vitamin-e": 0.00204,
-        "water": 59.61,
-        "zinc": 0.0013100000000000002
+        "vitamin-d": 6e-07,
+        "vitamin-e": 0.00028000000000000003,
+        "water": 33.19,
+        "zinc": 0.0039
     }
 }
```

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/sauerkraut_169279.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/sauerkraut_169279.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/scallion_170005.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/scallion_170005.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/spinach_168462.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/spinach_168462.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/strawberry_167762.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/strawberry_167762.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/sweet_potato_168482.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/sweet_potato_168482.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/tuna_bluefin_173706.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/tuna_bluefin_173706.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/tuna_skipjack_175156.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/tuna_skipjack_175156.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/tuna_yellowfin_175159.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/tuna_yellowfin_175159.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/turmeric_172231.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/turmeric_172231.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/wakame_seaweed_170496.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/wakame_seaweed_170496.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/walnut_170187.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/walnut_170187.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/whole_milk_171265.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/whole_milk_171265.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/yogurt_whole_milk_171284.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/yogurt_whole_milk_171284.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/foods/zucchini_169291.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/foods/zucchini_169291.json`

 * *Files identical despite different names*

### Comparing `nutrimetrics-0.0.2/nutrimetrics/resources/samples/meal_plan.json` & `nutrimetrics-1.0.0/nutrimetrics/resources/samples/michael_b_jordan.json`

 * *Files 24% similar despite different names*

```diff
@@ -1,46 +1,67 @@
+// Meal plan estimated from the article "How Michael B. Jordan Got Fit for 'Creed'"
+// https://www.mensjournal.com/health-fitness/how-michael-b-jordan-got-fit-for-creed-20151120
+// The total amount of calories seems low given Jordan heavy workouts
+// Adjusted rice and sweet potatoes amounts to match the indicated carbs amount
 {
-  "name": "Keto Diet",
+  "name": "Michael B. Jordan",
   "unit": "g",
-    "target": {
-      "body_mass": 75000.0,
-      "body_fat_percent": 15.0,
-      "activity_factor": 1.2,  // in [1.2, 1.6] range based on activity
-      "protein_factor": 1.8,  // minimum protein intake in [1.5, 2.3] range
-      "fat_factor": 0.8  // minimum fat intake 0.7 or larger
+  "target": {
+    "body_mass": 79378.7,  // 175 pounds (5'11" height)
+    "body_fat_percent": 8, // likely very low
+    "activity_factor": 1.2,  // set to 1.2 to match ~2500 kcal, should realistically be 1.5+
+    "minimum_protein_factor": 2.0,  // likely high
+    "minimum_fat_factor": 0.7  // minimum fat intake 0.7 or larger
   },
+  "dietary_reference_intakes": "rda-male", // (ear-male, ear-female, rda-male, rda-female)
   "meals": [
     {
-      "name": "Breakfast [8:00]",
+      "name": "Meal 1",
       "foods": [
-        {"food": "Egg White", "amount": 132}, // 4 eggs
-        {"food": "Egg Yolk", "amount": 68},
-        {"food": "Cheddar Cheese", "amount": 60},
-        {"food": "Flaxseed", "amount": 10},
-        {"food": "Olive Oil", "amount": 13}
+        {"food": "Egg White", "amount": 231}, // 33 * 7 (6 whites + 1 whole egg)
+        {"food": "Egg Yolk", "amount": 17}, // 17 * 1
+        {"food": "Rice White", "amount": 56}, // target 45g carbs
+        {"food": "Salt", "amount": 0.4}
       ]
     },
     {
-      "name": "Lunch [13:00]",
+      "name": "Meal 2",
       "foods": [
-        {"food": "Chicken Breast", "amount": 150},
-        {"food": "Avocado", "amount": 135}, // 1 avocado
-        {"food": "Bell Pepper Orange", "amount": 80},
-        {"food": "Scallion", "amount": 20},
-        {"food": "Garlic", "amount": 2},
-        {"food": "Olive Oil", "amount": 13}, // 1 TBSP
-        {"food": "Apple Cider Vinegar", "amount": 13},
-        {"food": "Macadamia Nut", "amount": 30}
+        {"food": "Protein Powder Whey", "amount": 32}, // typical amount for protein shake
+        {"food": "Oat Steel Cut", "amount": 50} // target 35g carbs
+      ]
+    },
+    {
+      "name": "Meal 3",
+      "foods": [
+        {"food": "Chicken Breast", "amount": 227}, // 8 oz
+        {"food": "Rice White", "amount": 81}, // target 65g carbs
+        {"food": "Broccoli", "amount": 90}, // 1 cup
+        {"food": "Salt", "amount": 0.4}
+      ]
+    },
+    {
+      "name": "Meal 4",
+      "foods": [
+        {"food": "Chicken Breast", "amount": 227}, // 8 oz
+        {"food": "Sweet Potato", "amount": 174}, // target 35g carbs
+        {"food": "Salt", "amount": 0.4}
       ]
     },
     {
-      "name": "Dinner [19:00]",
+      "name": "Meal 5",
       "foods": [
-        {"food": "Beef Ground 80-20", "amount": 150},
-        {"food": "Sauerkraut", "amount": 100},
-        {"food": "Turmeric", "amount": 4},
-        {"food": "Cauliflower", "amount": 110},
-        {"food": "Olive Oil", "amount": 26}  // 2 TBSP
+        {"food": "Protein Powder Whey", "amount": 32}, // typical amount for protein shake
+        {"food": "Oat Steel Cut", "amount": 50} // target 35g carbs
+      ]
+    },
+    {
+      "name": "Meal 6",
+      "foods": [
+        {"food": "Chicken Breast", "amount": 227}, // 8 oz
+        {"food": "Broccoli", "amount": 90}, // 1 cup
+        {"food": "Olive Oil", "amount": 13}, // 1 TBSP
+        {"food": "Salt", "amount": 0.4}
       ]
     }
   ]
 }
```

### Comparing `nutrimetrics-0.0.2/PKG-INFO` & `nutrimetrics-1.0.0/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nutrimetrics
-Version: 0.0.2
+Version: 1.0.0
 Summary: Analyzes nutrients found in foods and user-defined meal plans.
 Project-URL: Issues, https://github.com/tomcv/nutrimetrics/issues
 Project-URL: Source, https://github.com/tomcv/nutrimetrics
 Author-email: Thomas Civeit <thomas@civeit.com>
 License: MIT License
         
         Copyright (c) 2023 Thomas Civeit <thomas@civeit.com>
@@ -39,15 +39,15 @@
 Description-Content-Type: text/markdown
 
 # NutriMetrics
 
 NutriMetrics is a Python package that analyzes nutrients found in foods and user-defined meal plans.
 Nutrient profile data can be imported from USDA's FoodData Central or manually entered by users.
 The package tracks 60+ nutrients including fats, proteins, carbs, all minerals and vitamins.
-It comes with 100+ nutrient profiles found in common raw food and a few sample meal plans.
+It comes with 100+ nutrient profiles found in common food and a few sample meal plans.
 User-defined meal plans consist of a set of meals, each of which consists of a set of foods
 with a specified amount. Analysis reports are generated in Excel workbooks.
 
 [![PyPI - Version](https://img.shields.io/pypi/v/nutrimetrics.svg)](https://pypi.org/project/nutrimetrics)
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nutrimetrics.svg)](https://pypi.org/project/nutrimetrics)
 
 ![Report Screenshot](https://github.com/tomcv/nutrimetrics/blob/main/report.png?raw=true)
@@ -63,25 +63,31 @@
 
 ## Quick Start
 
 Run the commands:
 ```console
 $ pip install nutrimetrics
 $ nutrimetrics-init
-$ nutrimetrics-analyze ~/.nutrimetrics/samples/meal_plan.json
+$ nutrimetrics-analyze ~/.nutrimetrics/samples/bryan_johnson.json
 ```
-Which will generate the corresponding `meal_plan.xlsx` Excel workbook in the working directory.
+Which will generate the corresponding `bryan_johnson.xlsx` Excel workbook in the working directory.
+
+The package includes 3 sample meal plans:
+
+1. `bryan_johnson.json`: a vegan meal plan estimated from Bryan Johnson's [blueprint](https://blueprint.bryanjohnson.co/).
+2. `eric_berg.json`: a low-carb ketogenic meal plan estimated from Eric Berg's [eating routine](https://www.youtube.com/watch?v=EhZK_MUPxrc).
+3. `michael_b_jordan.json`: Michael B. Jordan's high-protein meal plan [to get fit](https://www.mensjournal.com/health-fitness/how-michael-b-jordan-got-fit-for-creed-20151120) for 'Creed'.
 
 ## Installation
 
 ### PyPI
 
 The easiest way to get NutriMetrics is to use pip:
 ```console
-pip install nutrimetrics
+$ pip install nutrimetrics
 ```
 That will install the `nutrimetrics` package along with all the required dependencies.
 Pip will also install a few commands (described below) to the package's bin directory.
 
 ### From Source
 
 Alternatively you can install the latest NutriMetrics codebase from the git repo:
@@ -105,15 +111,15 @@
 All configuration parameters are set in `~/.nutrimetrics/config.json`.
 The default configuration is created  when running the `nutrimetrics-init` command.
 The only parameter that you may have to change is the API key used to access FoodData Central
 when importing data.
 
 ### Analysis Report
 
-The package provides a sample meal plan you can use to run the `nutrimetrics-analyze` command:
+Reports are generated by running the `nutrimetrics-analyze` command:
 ```console
 $ nutrimetrics-analyze ~/.nutrimetrics/samples/meal_plan.json 
 ```
 Which will generate the corresponding `meal_plan.xlsx` Excel workbook in the working directory.
 The report includes the amount of each nutrient as well as some statistical data,
 including the energy distribution, the energy/protein/fat target, and the percentage of the
 Dietary Reference Intakes (DRI) for all minerals and vitamins. The report consists of 3 spreadsheets:
@@ -127,17 +133,18 @@
 {
   "name": "Simple Meal Plan",
   "unit": "g",
   "target": {
     "body_mass": 75400.0,
     "body_fat_percent": 15.0,
     "activity_factor": 1.4,  // in [1.2, 1.6] range based on activity
-    "protein_factor": 2.0,  // minimum protein intake in [1.5, 2.3] range
+    "protein_factor": 1.8,  // minimum protein intake in [1.5, 2.3] range
     "fat_factor": 0.8  // minimum fat intake 0.7 or larger
   },
+  "dietary_reference_intakes": "rda-male", // (ear-male, ear-female, rda-male, rda-female)
   "meals": [
     {
       "name": "Breakfast [7AM]",
       "foods": [
         {"food": "Oat Rolled", "amount": 40},
         {"food": "Blueberry", "amount": 80}
       ]
@@ -151,17 +158,21 @@
       ]
     }
   ]
 }
 ```
 The `food` value must be one of the food's name defined in the `~/.nutrimetrics/foods/` directory.
 
+The Dietary Reference Intakes (DRI) included in the package are the Recommended Dietary Allowance (RDA)
+and the Estimated Average Requirement (EAR) for male and female. Users can add their own requirement profiles
+in the `~/.nutrimetrics/dri/` directory.
+
 ### Nutrient Profile Data
 
-The package comes with 100+ nutrient profiles of raw food. However, new data can be added by importing
+The package comes with 100+ nutrient profiles of common food. However, new data can be added by importing
 nutrient profiles  from USDA's FoodData Central (FDC). The `nutrimetrics-import` command reads a JSON file
 that lists all foods names and FDC IDs to be imported, looking like this:
 
 ```json
 {
   "foods": [
     {"fdc_id": 170567,  "name": "Almond"},
```

