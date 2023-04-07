# Comparing `tmp/temperature_sensor_reader_xzf8971-1.3.0.tar.gz` & `tmp/temperature_sensor_reader_xzf8971-1.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "C:\Users\zifeng\Documents\zifengCode\temperature_sensor_reader\dist\.tmp-3okre7g_\temperature_sensor_reader_xzf8971-1.3.0.tar", last modified: Fri Dec  2 08:55:31 2022, max compression
+gzip compressed data, was "temperature_sensor_reader_xzf8971-1.4.0.tar", last modified: Fri Apr  7 03:35:12 2023, max compression
```

## Comparing `temperature_sensor_reader_xzf8971-1.3.0.tar` & `temperature_sensor_reader_xzf8971-1.4.0.tar`

### file list

```diff
@@ -1,37 +1,37 @@
-drwxrwxrwx   0        0        0        0 2022-12-02 08:55:31.616485 temperature_sensor_reader_xzf8971-1.3.0/
--rw-rw-rw-   0        0        0     1935 2022-12-02 08:07:32.000000 temperature_sensor_reader_xzf8971-1.3.0/.gitignore
--rw-rw-rw-   0        0        0      105 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/.gitmodules
--rw-rw-rw-   0        0        0     1088 2022-10-30 06:36:02.000000 temperature_sensor_reader_xzf8971-1.3.0/LICENSE
--rw-rw-rw-   0        0        0     3224 2022-12-02 08:55:31.614490 temperature_sensor_reader_xzf8971-1.3.0/PKG-INFO
--rw-rw-rw-   0        0        0     2612 2022-11-21 02:47:55.000000 temperature_sensor_reader_xzf8971-1.3.0/README.md
--rw-rw-rw-   0        0        0      109 2022-12-02 08:07:32.000000 temperature_sensor_reader_xzf8971-1.3.0/__init__.py
--rw-rw-rw-   0        0        0       67 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/build_and_install_locally.sh
--rw-rw-rw-   0        0        0      124 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/build_and_upload.sh
-drwxrwxrwx   0        0        0        0 2022-12-02 08:55:31.476232 temperature_sensor_reader_xzf8971-1.3.0/examples/
--rw-rw-rw-   0        0        0      560 2022-12-02 08:07:32.000000 temperature_sensor_reader_xzf8971-1.3.0/examples/JDRK_data_analysis.py
--rw-rw-rw-   0        0        0     2195 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/examples/JDRK_sensor.py
-drwxrwxrwx   0        0        0        0 2022-12-02 08:55:31.483230 temperature_sensor_reader_xzf8971-1.3.0/graphtec_reader/
--rw-rw-rw-   0        0        0       31 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/graphtec_reader/__init__.py
--rw-rw-rw-   0        0        0      963 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/graphtec_reader/__main__.py
--rw-rw-rw-   0        0        0     6271 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/graphtec_reader/helper_function.py
-drwxrwxrwx   0        0        0        0 2022-12-02 08:55:31.492308 temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/
--rw-rw-rw-   0        0        0      136 2022-10-30 09:20:01.000000 temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/__init__.py
--rw-rw-rw-   0        0        0     2498 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/derived_modbus_wrapper.py
--rw-rw-rw-   0        0        0     3642 2022-11-11 03:20:34.000000 temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/helper_function.py
--rw-rw-rw-   0        0        0     1322 2022-10-30 06:36:02.000000 temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/modbus_wrapper.py
--rw-rw-rw-   0        0        0     8045 2022-12-02 08:17:36.000000 temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/temperature_sensor.py
--rw-rw-rw-   0        0        0      842 2022-12-02 08:54:58.000000 temperature_sensor_reader_xzf8971-1.3.0/pyproject.toml
--rw-rw-rw-   0        0        0       42 2022-12-02 08:55:31.616485 temperature_sensor_reader_xzf8971-1.3.0/setup.cfg
--rw-rw-rw-   0        0        0      137 2022-11-14 04:11:07.000000 temperature_sensor_reader_xzf8971-1.3.0/setup.py
-drwxrwxrwx   0        0        0        0 2022-12-02 08:55:31.500814 temperature_sensor_reader_xzf8971-1.3.0/temperature_data_analysis/
--rw-rw-rw-   0        0        0       85 2022-12-02 08:07:32.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_data_analysis/__init__.py
--rw-rw-rw-   0        0        0     3552 2022-12-02 08:07:32.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_data_analysis/data_wrapper.py
--rw-rw-rw-   0        0        0        0 2022-12-02 08:07:32.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_data_analysis/helper_function.py
--rw-rw-rw-   0        0        0     1867 2022-12-02 08:54:20.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_data_analysis/plot_wrapper.py
-drwxrwxrwx   0        0        0        0 2022-12-02 08:55:31.611495 temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/
--rw-rw-rw-   0        0        0     3224 2022-12-02 08:55:31.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      985 2022-12-02 08:55:31.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-12-02 08:55:31.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2022-12-02 08:08:05.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       74 2022-12-02 08:55:31.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/requires.txt
--rw-rw-rw-   0        0        0       64 2022-12-02 08:55:31.000000 temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/top_level.txt
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:35:12.523575 temperature_sensor_reader_xzf8971-1.4.0/
+-rw-rw-r--   0 user      (1000) user      (1000)     1805 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.4.0/.gitignore
+-rw-rw-r--   0 user      (1000) user      (1000)      102 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.4.0/.gitmodules
+-rw-rw-r--   0 user      (1000) user      (1000)     1067 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.4.0/LICENSE
+-rw-rw-r--   0 user      (1000) user      (1000)     3138 2023-04-07 03:35:12.523575 temperature_sensor_reader_xzf8971-1.4.0/PKG-INFO
+-rw-rw-r--   0 user      (1000) user      (1000)     2540 2022-11-17 06:34:54.000000 temperature_sensor_reader_xzf8971-1.4.0/README.md
+-rw-rw-r--   0 user      (1000) user      (1000)      106 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.4.0/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)       64 2022-11-14 03:16:03.000000 temperature_sensor_reader_xzf8971-1.4.0/build_and_install_locally.sh
+-rw-rw-r--   0 user      (1000) user      (1000)      121 2022-11-14 03:13:15.000000 temperature_sensor_reader_xzf8971-1.4.0/build_and_upload.sh
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:35:12.515575 temperature_sensor_reader_xzf8971-1.4.0/examples/
+-rw-rw-r--   0 user      (1000) user      (1000)      552 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.4.0/examples/JDRK_data_analysis.py
+-rw-rw-r--   0 user      (1000) user      (1000)     2139 2022-11-11 06:37:07.000000 temperature_sensor_reader_xzf8971-1.4.0/examples/JDRK_sensor.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:35:12.515575 temperature_sensor_reader_xzf8971-1.4.0/graphtec_reader/
+-rw-rw-r--   0 user      (1000) user      (1000)       30 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.4.0/graphtec_reader/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      939 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.4.0/graphtec_reader/__main__.py
+-rw-rw-r--   0 user      (1000) user      (1000)     6451 2023-04-07 03:30:03.000000 temperature_sensor_reader_xzf8971-1.4.0/graphtec_reader/helper_function.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:35:12.517575 temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/
+-rw-rw-r--   0 user      (1000) user      (1000)      132 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)     2438 2022-11-14 03:35:17.000000 temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/derived_modbus_wrapper.py
+-rw-rw-r--   0 user      (1000) user      (1000)     3547 2022-11-14 03:28:25.000000 temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/helper_function.py
+-rw-rw-r--   0 user      (1000) user      (1000)     1279 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/modbus_wrapper.py
+-rw-rw-r--   0 user      (1000) user      (1000)     7852 2022-11-14 03:44:06.000000 temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/temperature_sensor.py
+-rw-rw-r--   0 user      (1000) user      (1000)      820 2023-04-07 03:31:09.000000 temperature_sensor_reader_xzf8971-1.4.0/pyproject.toml
+-rw-rw-r--   0 user      (1000) user      (1000)       38 2023-04-07 03:35:12.523575 temperature_sensor_reader_xzf8971-1.4.0/setup.cfg
+-rw-rw-r--   0 user      (1000) user      (1000)      128 2022-11-11 06:28:45.000000 temperature_sensor_reader_xzf8971-1.4.0/setup.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:35:12.520575 temperature_sensor_reader_xzf8971-1.4.0/temperature_data_analysis/
+-rw-rw-r--   0 user      (1000) user      (1000)       83 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_data_analysis/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)     3448 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_data_analysis/data_wrapper.py
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_data_analysis/helper_function.py
+-rw-rw-r--   0 user      (1000) user      (1000)     1813 2023-04-07 03:30:03.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_data_analysis/plot_wrapper.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:35:12.522575 temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/
+-rw-rw-r--   0 user      (1000) user      (1000)     3138 2023-04-07 03:35:12.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO
+-rw-rw-r--   0 user      (1000) user      (1000)      985 2023-04-07 03:35:12.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt
+-rw-rw-r--   0 user      (1000) user      (1000)        1 2023-04-07 03:35:12.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/dependency_links.txt
+-rw-rw-r--   0 user      (1000) user      (1000)        1 2022-11-17 06:29:21.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/not-zip-safe
+-rw-rw-r--   0 user      (1000) user      (1000)       74 2023-04-07 03:35:12.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/requires.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       64 2023-04-07 03:35:12.000000 temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/top_level.txt
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/.gitignore` & `temperature_sensor_reader_xzf8971-1.4.0/.gitignore`

 * *Ordering differences only*

 * *Files 22% similar despite different names*

```diff
@@ -1,130 +1,130 @@
-# Byte-compiled / optimized / DLL files
-__pycache__/
-*.py[cod]
-*$py.class
-
-# C extensions
-*.so
-
-# Distribution / packaging
-.Python
-build/
-develop-eggs/
-dist/
-downloads/
-eggs/
-.eggs/
-lib/
-lib64/
-parts/
-sdist/
-var/
-wheels/
-pip-wheel-metadata/
-share/python-wheels/
-*.egg-info/
-.installed.cfg
-*.egg
-MANIFEST
-
-# PyInstaller
-#  Usually these files are written by a python script from a template
-#  before PyInstaller builds the exe, so as to inject date/other infos into it.
-*.manifest
-*.spec
-
-# Installer logs
-pip-log.txt
-pip-delete-this-directory.txt
-
-# Unit test / coverage reports
-htmlcov/
-.tox/
-.nox/
-.coverage
-.coverage.*
-.cache
-nosetests.xml
-coverage.xml
-*.cover
-*.py,cover
-.hypothesis/
-.pytest_cache/
-
-# Translations
-*.mo
-*.pot
-
-# Django stuff:
-*.log
-local_settings.py
-db.sqlite3
-db.sqlite3-journal
-
-# Flask stuff:
-instance/
-.webassets-cache
-
-# Scrapy stuff:
-.scrapy
-
-# Sphinx documentation
-docs/_build/
-
-# PyBuilder
-target/
-
-# Jupyter Notebook
-.ipynb_checkpoints
-
-# IPython
-profile_default/
-ipython_config.py
-
-# pyenv
-.python-version
-
-# pipenv
-#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
-#   However, in case of collaboration, if having platform-specific dependencies or dependencies
-#   having no cross-platform support, pipenv may install dependencies that don't work, or not
-#   install all needed dependencies.
-#Pipfile.lock
-
-# PEP 582; used by e.g. github.com/David-OConnor/pyflow
-__pypackages__/
-
-# Celery stuff
-celerybeat-schedule
-celerybeat.pid
-
-# SageMath parsed files
-*.sage.py
-
-# Environments
-.env
-.venv
-env/
-venv/
-ENV/
-env.bak/
-venv.bak/
-
-# Spyder project settings
-.spyderproject
-.spyproject
-
-# Rope project settings
-.ropeproject
-
-# mkdocs documentation
-/site
-
-# mypy
-.mypy_cache/
-.dmypy.json
-dmypy.json
-
-# Pyre type checker
-.pyre/
-*.png
+# Byte-compiled / optimized / DLL files
+__pycache__/
+*.py[cod]
+*$py.class
+
+# C extensions
+*.so
+
+# Distribution / packaging
+.Python
+build/
+develop-eggs/
+dist/
+downloads/
+eggs/
+.eggs/
+lib/
+lib64/
+parts/
+sdist/
+var/
+wheels/
+pip-wheel-metadata/
+share/python-wheels/
+*.egg-info/
+.installed.cfg
+*.egg
+MANIFEST
+
+# PyInstaller
+#  Usually these files are written by a python script from a template
+#  before PyInstaller builds the exe, so as to inject date/other infos into it.
+*.manifest
+*.spec
+
+# Installer logs
+pip-log.txt
+pip-delete-this-directory.txt
+
+# Unit test / coverage reports
+htmlcov/
+.tox/
+.nox/
+.coverage
+.coverage.*
+.cache
+nosetests.xml
+coverage.xml
+*.cover
+*.py,cover
+.hypothesis/
+.pytest_cache/
+
+# Translations
+*.mo
+*.pot
+
+# Django stuff:
+*.log
+local_settings.py
+db.sqlite3
+db.sqlite3-journal
+
+# Flask stuff:
+instance/
+.webassets-cache
+
+# Scrapy stuff:
+.scrapy
+
+# Sphinx documentation
+docs/_build/
+
+# PyBuilder
+target/
+
+# Jupyter Notebook
+.ipynb_checkpoints
+
+# IPython
+profile_default/
+ipython_config.py
+
+# pyenv
+.python-version
+
+# pipenv
+#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
+#   However, in case of collaboration, if having platform-specific dependencies or dependencies
+#   having no cross-platform support, pipenv may install dependencies that don't work, or not
+#   install all needed dependencies.
+#Pipfile.lock
+
+# PEP 582; used by e.g. github.com/David-OConnor/pyflow
+__pypackages__/
+
+# Celery stuff
+celerybeat-schedule
+celerybeat.pid
+
+# SageMath parsed files
+*.sage.py
+
+# Environments
+.env
+.venv
+env/
+venv/
+ENV/
+env.bak/
+venv.bak/
+
+# Spyder project settings
+.spyderproject
+.spyproject
+
+# Rope project settings
+.ropeproject
+
+# mkdocs documentation
+/site
+
+# mypy
+.mypy_cache/
+.dmypy.json
+dmypy.json
+
+# Pyre type checker
+.pyre/
+*.png
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/PKG-INFO` & `temperature_sensor_reader_xzf8971-1.4.0/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,86 +1,86 @@
-Metadata-Version: 2.1
-Name: temperature_sensor_reader_xzf8971
-Version: 1.3.0
-Summary: A package to read/write registers on a temperature sensor with python.
-Author-email: Zifeng <zifeng.xu@foxmail.com>
-Project-URL: Homepage, https://github.com/xzf89718/temperature_sensor_reader
-Project-URL: Bug Tracker, https://github.com/xzf89718/temperature_sensor_reader/issues
-Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: OS Independent
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
-# temperature_sensor_reader
-This is a temperature sensor package designed for modbus. Implemented in pymodbus only. PyPI website: https://pypi.org/project/temperature-sensor-reader-xzf8971/
-## Install
-from pypi:  
-```bash
-pip install temperature-sensor-reader-xzf8971  
-```
-from github:  
-```bahs
-pip install git+https://github.com/xzf89718/temperature_sensor_reader
-```
-## Jiandarenke modbus RS485 as example  
-### Before run scripts
-Check the COM and chmod  
-```bash
-chmod 666 \dev\ttyUSBx
-```
-### Import modules  
-```python
-from modbus_configuretools import temperature_sensor.RS485_Jiandarenke as RS485_JDRK  
-from modbus_configuretools import temperature_sensor.JDRKAddressConfig as Config
-```
-### Configure parameters for Jiandarenke RS485 sensor
-It's OK to set None for unkown value
-```python
-# Modify these config values 
-# Please configure these value in temperature_sensor before read or write values  
-# SLAVEID must be specified. If SLAVEID is none, set to 1  
-# ADDRESS_HUMIDITY = 0x0000  
-# ADDRESS_TEMPERATURE_DEW_POINT = 0x0001  
-# ADDRESS_TEMPERATURE = 0x0002  
-# ADDRESS_TEMPERATURE_CALI = 0x0050  
-# ADDRESS_HUMUDITY_CALI = 0x0051  
-# ADDRESS_SLAVEID = 0x07D0  
-# ADDRESS_BAUDRATE = 0x07D1  
-# TEMPERATURE_CALI = 164  
-# HUMIDITY_CALI = 7  
-# SLAVEID = 1
-# BAUDRATE = 1
-myconfig = Config(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID, ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
-```
-### Calibration of sensor. Not necessary calibration every time  
-```python
-sensor.CalibrationJiandarenke(myconfig)  
-```
-### Set slaveID and baudrate
-Please make sure only 1 sensor connect to the modbus bus
-```python
-sensor.WriteSlaveIDAndBaudrate(myconfig)
-```
-### Init and read measured values from sensor  
-```python
-# Create a wrapper for JDRK sensor  
-sensor = RS485_JDRK(port="/dev/ttyUSB0")  
-# Init and connect client
-sensor.InitClient()  
-# Read slaveID and baudrate  
-slaveID, baudrate = sensor.ReadSalveIDAndBaudrate(myconfig)  
-# Read temperature, dew point, humidity in one request  
-# Only correct for specified sensor
-temperature, dew_point_temperature, humidity = sensor.ReadTemperatureAndHumidity(myconfig)  
-# Read temperature only  
-temperature = sensor.ReadTemperature(myconfig)  
-# Read dew point temperature  
-dew_point_temperature = sensor.ReadTemperatureDewPoint(myconfig)  
-# Read humidity only  
-humidity = sensor.ReadTemperature(myconfig)  
-```
-### Close the sensor
-```python
-sensor.close()
-```
+Metadata-Version: 2.1
+Name: temperature_sensor_reader_xzf8971
+Version: 1.4.0
+Summary: A package to read/write registers on a temperature sensor with python.
+Author-email: Zifeng <zifeng.xu@foxmail.com>
+Project-URL: Homepage, https://github.com/xzf89718/temperature_sensor_reader
+Project-URL: Bug Tracker, https://github.com/xzf89718/temperature_sensor_reader/issues
+Classifier: Programming Language :: Python :: 3
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# temperature_sensor_reader
+This is a temperature sensor package designed for modbus. Implemented in pymodbus only. PyPI website: https://pypi.org/project/temperature-sensor-reader-xzf8971/
+## Install
+from pypi:  
+```bash
+pip install temperature-sensor-reader-xzf8971  
+```
+from github:  
+```bahs
+pip install git+https://github.com/xzf89718/temperature_sensor_reader
+```
+## Jiandarenke modbus RS485 as example  
+### Before run scripts
+Check the COM and chmod  
+```bash
+chmod 666 \dev\ttyUSBx
+```
+### Import modules  
+```python
+from modbus_configuretools import temperature_sensor.RS485_Jiandarenke as RS485_JDRK  
+from modbus_configuretools import temperature_sensor.JDRKAddressConfig as Config
+```
+### Configure parameters for Jiandarenke RS485 sensor
+It's OK to set None for unkown value
+```python
+# Modify these config values 
+# Please configure these value in temperature_sensor before read or write values  
+# SLAVEID must be specified. If SLAVEID is none, set to 1  
+# ADDRESS_HUMIDITY = 0x0000  
+# ADDRESS_TEMPERATURE_DEW_POINT = 0x0001  
+# ADDRESS_TEMPERATURE = 0x0002  
+# ADDRESS_TEMPERATURE_CALI = 0x0050  
+# ADDRESS_HUMUDITY_CALI = 0x0051  
+# ADDRESS_SLAVEID = 0x07D0  
+# ADDRESS_BAUDRATE = 0x07D1  
+# TEMPERATURE_CALI = 164  
+# HUMIDITY_CALI = 7  
+# SLAVEID = 1
+# BAUDRATE = 1
+myconfig = Config(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID, ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
+```
+### Calibration of sensor. Not necessary calibration every time  
+```python
+sensor.CalibrationJiandarenke(myconfig)  
+```
+### Set slaveID and baudrate
+Please make sure only 1 sensor connect to the modbus bus
+```python
+sensor.WriteSlaveIDAndBaudrate(myconfig)
+```
+### Init and read measured values from sensor  
+```python
+# Create a wrapper for JDRK sensor  
+sensor = RS485_JDRK(port="/dev/ttyUSB0")  
+# Init and connect client
+sensor.InitClient()  
+# Read slaveID and baudrate  
+slaveID, baudrate = sensor.ReadSalveIDAndBaudrate(myconfig)  
+# Read temperature, dew point, humidity in one request  
+# Only correct for specified sensor
+temperature, dew_point_temperature, humidity = sensor.ReadTemperatureAndHumidity(myconfig)  
+# Read temperature only  
+temperature = sensor.ReadTemperature(myconfig)  
+# Read dew point temperature  
+dew_point_temperature = sensor.ReadTemperatureDewPoint(myconfig)  
+# Read humidity only  
+humidity = sensor.ReadTemperature(myconfig)  
+```
+### Close the sensor
+```python
+sensor.close()
+```
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/README.md` & `temperature_sensor_reader_xzf8971-1.4.0/README.md`

 * *Ordering differences only*

 * *Files 14% similar despite different names*

```diff
@@ -1,72 +1,72 @@
-# temperature_sensor_reader
-This is a temperature sensor package designed for modbus. Implemented in pymodbus only. PyPI website: https://pypi.org/project/temperature-sensor-reader-xzf8971/
-## Install
-from pypi:  
-```bash
-pip install temperature-sensor-reader-xzf8971  
-```
-from github:  
-```bahs
-pip install git+https://github.com/xzf89718/temperature_sensor_reader
-```
-## Jiandarenke modbus RS485 as example  
-### Before run scripts
-Check the COM and chmod  
-```bash
-chmod 666 \dev\ttyUSBx
-```
-### Import modules  
-```python
-from modbus_configuretools import temperature_sensor.RS485_Jiandarenke as RS485_JDRK  
-from modbus_configuretools import temperature_sensor.JDRKAddressConfig as Config
-```
-### Configure parameters for Jiandarenke RS485 sensor
-It's OK to set None for unkown value
-```python
-# Modify these config values 
-# Please configure these value in temperature_sensor before read or write values  
-# SLAVEID must be specified. If SLAVEID is none, set to 1  
-# ADDRESS_HUMIDITY = 0x0000  
-# ADDRESS_TEMPERATURE_DEW_POINT = 0x0001  
-# ADDRESS_TEMPERATURE = 0x0002  
-# ADDRESS_TEMPERATURE_CALI = 0x0050  
-# ADDRESS_HUMUDITY_CALI = 0x0051  
-# ADDRESS_SLAVEID = 0x07D0  
-# ADDRESS_BAUDRATE = 0x07D1  
-# TEMPERATURE_CALI = 164  
-# HUMIDITY_CALI = 7  
-# SLAVEID = 1
-# BAUDRATE = 1
-myconfig = Config(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID, ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
-```
-### Calibration of sensor. Not necessary calibration every time  
-```python
-sensor.CalibrationJiandarenke(myconfig)  
-```
-### Set slaveID and baudrate
-Please make sure only 1 sensor connect to the modbus bus
-```python
-sensor.WriteSlaveIDAndBaudrate(myconfig)
-```
-### Init and read measured values from sensor  
-```python
-# Create a wrapper for JDRK sensor  
-sensor = RS485_JDRK(port="/dev/ttyUSB0")  
-# Init and connect client
-sensor.InitClient()  
-# Read slaveID and baudrate  
-slaveID, baudrate = sensor.ReadSalveIDAndBaudrate(myconfig)  
-# Read temperature, dew point, humidity in one request  
-# Only correct for specified sensor
-temperature, dew_point_temperature, humidity = sensor.ReadTemperatureAndHumidity(myconfig)  
-# Read temperature only  
-temperature = sensor.ReadTemperature(myconfig)  
-# Read dew point temperature  
-dew_point_temperature = sensor.ReadTemperatureDewPoint(myconfig)  
-# Read humidity only  
-humidity = sensor.ReadTemperature(myconfig)  
-```
-### Close the sensor
-```python
-sensor.close()
-```
+# temperature_sensor_reader
+This is a temperature sensor package designed for modbus. Implemented in pymodbus only. PyPI website: https://pypi.org/project/temperature-sensor-reader-xzf8971/
+## Install
+from pypi:  
+```bash
+pip install temperature-sensor-reader-xzf8971  
+```
+from github:  
+```bahs
+pip install git+https://github.com/xzf89718/temperature_sensor_reader
+```
+## Jiandarenke modbus RS485 as example  
+### Before run scripts
+Check the COM and chmod  
+```bash
+chmod 666 \dev\ttyUSBx
+```
+### Import modules  
+```python
+from modbus_configuretools import temperature_sensor.RS485_Jiandarenke as RS485_JDRK  
+from modbus_configuretools import temperature_sensor.JDRKAddressConfig as Config
+```
+### Configure parameters for Jiandarenke RS485 sensor
+It's OK to set None for unkown value
+```python
+# Modify these config values 
+# Please configure these value in temperature_sensor before read or write values  
+# SLAVEID must be specified. If SLAVEID is none, set to 1  
+# ADDRESS_HUMIDITY = 0x0000  
+# ADDRESS_TEMPERATURE_DEW_POINT = 0x0001  
+# ADDRESS_TEMPERATURE = 0x0002  
+# ADDRESS_TEMPERATURE_CALI = 0x0050  
+# ADDRESS_HUMUDITY_CALI = 0x0051  
+# ADDRESS_SLAVEID = 0x07D0  
+# ADDRESS_BAUDRATE = 0x07D1  
+# TEMPERATURE_CALI = 164  
+# HUMIDITY_CALI = 7  
+# SLAVEID = 1
+# BAUDRATE = 1
+myconfig = Config(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID, ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
+```
+### Calibration of sensor. Not necessary calibration every time  
+```python
+sensor.CalibrationJiandarenke(myconfig)  
+```
+### Set slaveID and baudrate
+Please make sure only 1 sensor connect to the modbus bus
+```python
+sensor.WriteSlaveIDAndBaudrate(myconfig)
+```
+### Init and read measured values from sensor  
+```python
+# Create a wrapper for JDRK sensor  
+sensor = RS485_JDRK(port="/dev/ttyUSB0")  
+# Init and connect client
+sensor.InitClient()  
+# Read slaveID and baudrate  
+slaveID, baudrate = sensor.ReadSalveIDAndBaudrate(myconfig)  
+# Read temperature, dew point, humidity in one request  
+# Only correct for specified sensor
+temperature, dew_point_temperature, humidity = sensor.ReadTemperatureAndHumidity(myconfig)  
+# Read temperature only  
+temperature = sensor.ReadTemperature(myconfig)  
+# Read dew point temperature  
+dew_point_temperature = sensor.ReadTemperatureDewPoint(myconfig)  
+# Read humidity only  
+humidity = sensor.ReadTemperature(myconfig)  
+```
+### Close the sensor
+```python
+sensor.close()
+```
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/examples/JDRK_data_analysis.py` & `temperature_sensor_reader_xzf8971-1.4.0/examples/JDRK_data_analysis.py`

 * *Ordering differences only*

 * *Files 20% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-from temperature_data_analysis.data_wrapper import JDRKDataWrapper
-from temperature_data_analysis.plot_wrapper import makeTemperatureAndHumidity
-
-# Init a wrapper
-data_wrapper = JDRKDataWrapper()
-# Read data from a file
-data_wrapper.ReadDataFile(r"C:\Users\zifeng\Documents\zifengCode\hgtd-peb\Demonstration\MUX64_QFN88_TEST\script\MUX64_reliability\MUX64_TC_test_temperature_log\MUX64_TC_test_Nov14_Nov28.log")
-measure_time, measure_temp, measure_humi = data_wrapper.GetDataToPlot()
+from temperature_data_analysis.data_wrapper import JDRKDataWrapper
+from temperature_data_analysis.plot_wrapper import makeTemperatureAndHumidity
+
+# Init a wrapper
+data_wrapper = JDRKDataWrapper()
+# Read data from a file
+data_wrapper.ReadDataFile(r"C:\Users\zifeng\Documents\zifengCode\hgtd-peb\Demonstration\MUX64_QFN88_TEST\script\MUX64_reliability\MUX64_TC_test_temperature_log\MUX64_TC_test_Nov14_Nov28.log")
+measure_time, measure_temp, measure_humi = data_wrapper.GetDataToPlot()
 makeTemperatureAndHumidity(measure_time, measure_temp, measure_humi)
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/examples/JDRK_sensor.py` & `temperature_sensor_reader_xzf8971-1.4.0/examples/JDRK_sensor.py`

 * *Ordering differences only*

 * *Files 17% similar despite different names*

```diff
@@ -1,56 +1,56 @@
-from modbus_configuretools.temperature_sensor import JDRKAddressConfig, RS485_Jiandarenke
-import time
-from custom_logger import CustomLoggerWrapper
-logger_wrapper = CustomLoggerWrapper("JDRK_sensor", log_filename="MUX64_TC_test.log")
-logger_wrapper.InitLogger()
-JDRK_sensor_logger = logger_wrapper.GetInitedLogger()
-
-ADDRESS_HUMIDITY = 0x0000
-ADDRESS_TEMPERATURE_DEW_POINT = 0x0001
-ADDRESS_TEMPERATURE = 0x0002
-ADDRESS_TEMPERATURE_CALI = 0x0050
-ADDRESS_HUMUDITY_CALI = 0x0051
-ADDRESS_SLAVEID = 0x07D0
-ADDRESS_BAUDRATE = 0x07D1
-
-TEMPERATURE_CALI = 164
-HUMIDITY_CALI = 7
-SLAVEID = 1
-BAUDRATE = 1
-
-JDRK_RS485_wangzike_config = JDRKAddressConfig(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID,
-                                               ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
-
-JDRK_RS485_box_config = JDRKAddressConfig(0x0000, None, 0x0001, ADDRESS_SLAVEID,
-                                               ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
-
-
-PORT_NUMBER = "/dev/ttyUSB0"
-PORT_BAUDRATE = 4800
-PORT_TIMEOUT = 1
-mysensor = RS485_Jiandarenke(
-    port=PORT_NUMBER, baudrate=PORT_BAUDRATE, timeout=PORT_TIMEOUT)
-mysensor.InitClient()
-
-try:
-    while True:
-        temperature = mysensor.ReadTemperature(JDRK_RS485_box_config)
-        # Check if read temperature success
-        if (len(temperature) > 0):
-            temperature = temperature[0]
-        else:
-            temperature = "NULL"
-        humidity = mysensor.ReadHumidity(JDRK_RS485_box_config)
-        # Check if read humidity success
-        if (len(humidity) > 0):
-            humidity = humidity[0]
-        else:
-            humidity = "NULL"
-        _message_to_write = "{0}\t{1}".format(
-            temperature, humidity)
-        JDRK_sensor_logger.info(_message_to_write)
-        # Get temperature and humidity every 30s
-        time.sleep(30)
-except KeyboardInterrupt as error:
-    JDRK_sensor_logger.warning("End write temperature into log")
-    mysensor.CloseClient()
+from modbus_configuretools.temperature_sensor import JDRKAddressConfig, RS485_Jiandarenke
+import time
+from custom_logger import CustomLoggerWrapper
+logger_wrapper = CustomLoggerWrapper("JDRK_sensor", log_filename="MUX64_TC_test.log")
+logger_wrapper.InitLogger()
+JDRK_sensor_logger = logger_wrapper.GetInitedLogger()
+
+ADDRESS_HUMIDITY = 0x0000
+ADDRESS_TEMPERATURE_DEW_POINT = 0x0001
+ADDRESS_TEMPERATURE = 0x0002
+ADDRESS_TEMPERATURE_CALI = 0x0050
+ADDRESS_HUMUDITY_CALI = 0x0051
+ADDRESS_SLAVEID = 0x07D0
+ADDRESS_BAUDRATE = 0x07D1
+
+TEMPERATURE_CALI = 164
+HUMIDITY_CALI = 7
+SLAVEID = 1
+BAUDRATE = 1
+
+JDRK_RS485_wangzike_config = JDRKAddressConfig(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID,
+                                               ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
+
+JDRK_RS485_box_config = JDRKAddressConfig(0x0000, None, 0x0001, ADDRESS_SLAVEID,
+                                               ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
+
+
+PORT_NUMBER = "/dev/ttyUSB0"
+PORT_BAUDRATE = 4800
+PORT_TIMEOUT = 1
+mysensor = RS485_Jiandarenke(
+    port=PORT_NUMBER, baudrate=PORT_BAUDRATE, timeout=PORT_TIMEOUT)
+mysensor.InitClient()
+
+try:
+    while True:
+        temperature = mysensor.ReadTemperature(JDRK_RS485_box_config)
+        # Check if read temperature success
+        if (len(temperature) > 0):
+            temperature = temperature[0]
+        else:
+            temperature = "NULL"
+        humidity = mysensor.ReadHumidity(JDRK_RS485_box_config)
+        # Check if read humidity success
+        if (len(humidity) > 0):
+            humidity = humidity[0]
+        else:
+            humidity = "NULL"
+        _message_to_write = "{0}\t{1}".format(
+            temperature, humidity)
+        JDRK_sensor_logger.info(_message_to_write)
+        # Get temperature and humidity every 30s
+        time.sleep(30)
+except KeyboardInterrupt as error:
+    JDRK_sensor_logger.warning("End write temperature into log")
+    mysensor.CloseClient()
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/graphtec_reader/__main__.py` & `temperature_sensor_reader_xzf8971-1.4.0/graphtec_reader/__main__.py`

 * *Ordering differences only*

 * *Files 20% similar despite different names*

```diff
@@ -1,24 +1,24 @@
-# ref: https://github.com/HaralDev/GraphtecPython
-from graphtec_reader.helper_function import readFromGraphtec
-import argparse
-
-
-if __name__ == "__main__":
-    parser = argparse.ArgumentParser(
-        description="Graphtec reader in python. Author: Zifeng XU, email: zifeng.xu@cern.ch.")
-    parser.add_argument(
-        "-p", "--port", help="Port for Graphtec.", required=True)
-    parser.add_argument("-t", "--time-interval",
-                        help="Baudrate for monitoring serial.", required=True)
-    parser.add_argument("-o", "--outfile-name",
-                        help="Timeout for monitoring serial.", required=True)
-    args = parser.parse_args()
-    print("All parameters get from commandline are:")
-    print(args)
-
-    PORT = args.port
-    TIMEINTERVAL = args.time_interval
-    OUTFILENAME = args.outfile_name
-
-    readFromGraphtec(port=PORT, time_interval=TIMEINTERVAL,
-                     logfile_name=OUTFILENAME)
+# ref: https://github.com/HaralDev/GraphtecPython
+from graphtec_reader.helper_function import readFromGraphtec
+import argparse
+
+
+if __name__ == "__main__":
+    parser = argparse.ArgumentParser(
+        description="Graphtec reader in python. Author: Zifeng XU, email: zifeng.xu@cern.ch.")
+    parser.add_argument(
+        "-p", "--port", help="Port for Graphtec.", required=True)
+    parser.add_argument("-t", "--time-interval",
+                        help="Baudrate for monitoring serial.", required=True)
+    parser.add_argument("-o", "--outfile-name",
+                        help="Timeout for monitoring serial.", required=True)
+    args = parser.parse_args()
+    print("All parameters get from commandline are:")
+    print(args)
+
+    PORT = args.port
+    TIMEINTERVAL = args.time_interval
+    OUTFILENAME = args.outfile_name
+
+    readFromGraphtec(port=PORT, time_interval=TIMEINTERVAL,
+                     logfile_name=OUTFILENAME)
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/graphtec_reader/helper_function.py` & `temperature_sensor_reader_xzf8971-1.4.0/graphtec_reader/helper_function.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,142 +1,151 @@
-import numpy as np
-from bs4 import BeautifulSoup
-from requests import get
-from pandas import DataFrame
-from pyvisa import ResourceManager
-from datetime import datetime as dt
-import pytz
-import glob
-import time
-from custom_logger import CustomLoggerWrapper
-
-
-class Graphtec():
-
-    # -----------------------------------
-    def __init__(self, address, resource_manager):
-        self.address = address
-        # TCPIP adress to contact
-        # self.tcpip_gl = f"TCPIP::{self.address}::8023::SOCKET"
-        # self.instrument = resource_manager.open_resource(self.tcpip_gl,
-                                                        #  write_termination='\n',
-                                                        #  read_termination='\r\n')
-        #self.query_id = self.get_graphtec_idn()
-        # Holds measurement data
-        self.data = []
-
-    # -----------------------------------
-    def append_graphtec_readings(self):
-        """Find all the measurements of the channels and append to self.data list"""
-        # Format URL
-        address_channel_data = f"http://{self.address}/digital.cgi?chgrp=13"
-
-        # Get http response
-        # Get response from the channel data page
-        response = get(address_channel_data)
-
-        # Create response table
-        # Create a soup object from this, which is used to create a table
-        soup_object = BeautifulSoup(response.text, 'html.parser')
-        # Holds all the found data > in format: [('CH 1', '+  10', 'degC'), (CH2 ....]
-        channels_data = []
-        # Table with all the channels as subtables > based on the HTML table class > example: [table: [table, table, table]]
-        for table in soup_object.find_all(border="1"):
-            # Tables of all the individual channels > Search for table again to get: [table, table, table], each one corresponds to one channel
-            channel_readings_html = table.findAll('table')
-
-        # Loop over table to yield formatted data
-
-            for channel_read_html in channel_readings_html:
-                # Returns a row for each measurement channel with relevant data > [<b> CH 1</b>, <b> -------</b>, <b> degC</b>]
-                reading_html = channel_read_html.find_all('b')
-
-                # Strips the string of its unicode characters and puts it into a list > ['CH 1', '-------', 'degC']
-                reading_list = [read_tag.get_text(
-                    strip=True) for read_tag in reading_html]
-                channels_data.append(reading_list)
-
-        # Append the data to the list
-        self.data.append(channels_data)
-
-    # -----------------------------------
-    def get_graphtec_idn(self):
-        pass
-        # """SCPI command to get IDN"""
-        # idn = self.instrument.query("*IDN?")
-        # return idn
-
-    # -----------------------------------
-    def add_channel_data_to_df(self):
-        """Post processing method to format self.data list into a Pandas DataFrame"""
-
-        name_index = 0      # Format is ['CH 1', '23.56', 'degC']
-        # so index 0, 1 and 2 are, respectively channel name, value reading and unit.
-        reading_index = 1
-        unit_index = 2
-
-        # Amount of channels to loop over, might depend on Graphtec device (I have 20)
-        channel_count = len(self.data[0])
-        df = DataFrame()
-
-        # Loop over each channel
-        for channel_ind in range(channel_count):
-
-            # get the channel name
-            channel_name = self.data[0][channel_ind][name_index]
-            channel_unit = self.data[0][channel_ind][unit_index]    # and unit
-            # Format column name "GRPH CH1 [degC]"
-            column_name = f"GRPH {channel_name} [{channel_unit}]"
-
-            # Stores the channel data > [0.0, 0.1, 0.0 ....]
-            channel_readings = []
-            channel_name_del = []
-            # only save open channels
-            if "CH 1 [degC]" in column_name or "CH 2 [degC]" in column_name or "CH 3 [degC]" in column_name or "GS 2" in column_name:
-                # Loop over each row and retrieve channel data
-                for row in self.data:
-                    # Read the data of channel for this row
-                    channel_reading = row[channel_ind][reading_index]
-
-                    # Value formatting
-                    if channel_reading == '' or channel_reading == 'BURNOUT' or channel_reading == 'Off':
-                        channel_reading = 0
-                        channel_name_del.append(channel_name)
-                    else:
-                        # Float for other values, remove spaces in order to have +/-
-                        channel_reading = float(
-                            channel_reading.replace(' ', ''))
-                    channel_readings.append(channel_reading)
-                # Add a new column with data
-                df[column_name] = channel_readings
-        return df
-
-
-class GraphtecWithLogger(Graphtec):
-
-    def __init__(self, address, resource_manager):
-        super().__init__(address, resource_manager)
-    
-    def append_graphtec_readings(self):
-        _data = super().append_graphtec_readings()()
-        print(_data)
-
-def readFromGraphtec(port, time_interval, logfile_name):
-    logger_wrapper = CustomLoggerWrapper(
-        "Graphtec_logger", log_filename=logfile_name)
-    logger_wrapper.InitLogger()
-    mylogger = logger_wrapper.GetInitedLogger()
-    # Need a resourcemanager to communicate with Graphtec via PyVisa
-    rm = ResourceManager("@py")
-    # Can be setup on Graphtec with "Menu > I/F > IP ADDRESS" (change with buttons)
-    # ip_graphtec = "192.168.10.20"
-    # Sometimes errors arise here if you can not connect, restarting the Graphtec or doing "Menu > I/F > Apply Setting" Sometimes helps. Also, try if you can visit the ip address in browser directly.
-    graphtec = GraphtecWithLogger(port, rm)
-
-    try:
-        while True:
-            graphtec.append_graphtec_readings()  # Measure and append to data list
-            # Reading every 0.2 seconds
-            time.sleep(time_interval)
-    except KeyboardInterrupt as error:
-        print(error)
-        mylogger.warning("End temperature recoding from keyboard")
+import numpy as np
+from bs4 import BeautifulSoup
+from requests import get
+from pandas import DataFrame
+from pyvisa import ResourceManager
+from datetime import datetime as dt
+import pytz
+import glob
+import time
+from custom_logger import CustomLoggerWrapper
+
+
+class Graphtec():
+
+    # -----------------------------------
+    def __init__(self, address, resource_manager):
+        self.address = address
+        # TCPIP adress to contact
+        # self.tcpip_gl = f"TCPIP::{self.address}::8023::SOCKET"
+        # self.instrument = resource_manager.open_resource(self.tcpip_gl,
+                                                        #  write_termination='\n',
+                                                        #  read_termination='\r\n')
+        #self.query_id = self.get_graphtec_idn()
+        # Holds measurement data
+        self.data = []
+
+    # -----------------------------------
+    def append_graphtec_readings(self):
+        """Find all the measurements of the channels and append to self.data list"""
+        # Format URL
+        address_channel_data = f"http://{self.address}/digital.cgi?chgrp=13"
+
+        # Get http response
+        # Get response from the channel data page
+        response = get(address_channel_data)
+
+        # Create response table
+        # Create a soup object from this, which is used to create a table
+        soup_object = BeautifulSoup(response.text, 'html.parser')
+        # Holds all the found data > in format: [('CH 1', '+  10', 'degC'), (CH2 ....]
+        channels_data = []
+        # Table with all the channels as subtables > based on the HTML table class > example: [table: [table, table, table]]
+        for table in soup_object.find_all(border="1"):
+            # Tables of all the individual channels > Search for table again to get: [table, table, table], each one corresponds to one channel
+            channel_readings_html = table.findAll('table')
+
+        # Loop over table to yield formatted data
+
+            for channel_read_html in channel_readings_html:
+                # Returns a row for each measurement channel with relevant data > [<b> CH 1</b>, <b> -------</b>, <b> degC</b>]
+                reading_html = channel_read_html.find_all('b')
+
+                # Strips the string of its unicode characters and puts it into a list > ['CH 1', '-------', 'degC']
+                reading_list = [read_tag.get_text(
+                    strip=True) for read_tag in reading_html]
+                channels_data.append(reading_list)
+
+        # Append the data to the list
+        # self.data.append(channels_data)
+        self.data = [channels_data]
+
+    # -----------------------------------
+    def get_graphtec_idn(self):
+        pass
+        # """SCPI command to get IDN"""
+        # idn = self.instrument.query("*IDN?")
+        # return idn
+
+    # -----------------------------------
+    def add_channel_data_to_df(self):
+        """Post processing method to format self.data list into a Pandas DataFrame"""
+
+        name_index = 0      # Format is ['CH 1', '23.56', 'degC']
+        # so index 0, 1 and 2 are, respectively channel name, value reading and unit.
+        reading_index = 1
+        unit_index = 2
+
+        # Amount of channels to loop over, might depend on Graphtec device (I have 20)
+        channel_count = len(self.data[0])
+        df = DataFrame()
+
+        # Loop over each channel
+        for channel_ind in range(channel_count):
+
+            # get the channel name
+            channel_name = self.data[0][channel_ind][name_index]
+            channel_unit = self.data[0][channel_ind][unit_index]    # and unit
+            # Format column name "GRPH CH1 [degC]"
+            column_name = f"GRPH {channel_name} [{channel_unit}]"
+
+            # Stores the channel data > [0.0, 0.1, 0.0 ....]
+            channel_readings = []
+            channel_name_del = []
+            # only save open channels
+            if "CH 1 [degC]" in column_name or "CH 2 [degC]" in column_name or "CH 3 [degC]" in column_name or "GS 2" in column_name:
+                # Loop over each row and retrieve channel data
+                for row in self.data:
+                    # Read the data of channel for this row
+                    channel_reading = row[channel_ind][reading_index]
+
+                    # Value formatting
+                    if channel_reading == '' or channel_reading == 'BURNOUT' or channel_reading == 'Off':
+                        channel_reading = 0
+                        channel_name_del.append(channel_name)
+                    else:
+                        # Float for other values, remove spaces in order to have +/-
+                        channel_reading = float(
+                            channel_reading.replace(' ', ''))
+                    channel_readings.append(channel_reading)
+                # Add a new column with data
+                df[column_name] = channel_readings
+        return df
+
+
+class GraphtecWithLogger(Graphtec):
+
+    def __init__(self, address, resource_manager, my_logger):
+        super().__init__(address, resource_manager)
+        self.my_logger = my_logger
+    
+    def add_channel_data_to_df(self):
+        _df =  super().add_channel_data_to_df()
+        message = ""
+        for _CH in _df.columns.values:
+            message = message + "\t" + str(_CH) + str(_df[_CH][0])
+        self.my_logger.info(message)
+            
+
+
+def readFromGraphtec(port, time_interval, logfile_name):
+    logger_wrapper = CustomLoggerWrapper(
+        "Graphtec_logger", log_filename=logfile_name)
+    logger_wrapper.InitLogger()
+    mylogger = logger_wrapper.GetInitedLogger()
+    # Need a resourcemanager to communicate with Graphtec via PyVisa
+    rm = ResourceManager("@py")
+    # Can be setup on Graphtec with "Menu > I/F > IP ADDRESS" (change with buttons)
+    # ip_graphtec = "192.168.10.20"
+    # Sometimes errors arise here if you can not connect, restarting the Graphtec or doing "Menu > I/F > Apply Setting" Sometimes helps. Also, try if you can visit the ip address in browser directly.
+    graphtec = GraphtecWithLogger(port, rm, mylogger)
+
+    try:
+        while True:
+            graphtec.append_graphtec_readings()
+            graphtec.add_channel_data_to_df()  # Measure and append to data list
+            # mylogger.info("")
+            # Reading every 0.2 seconds
+            time.sleep(time_interval)
+    except KeyboardInterrupt as error:
+        print(error)
+        mylogger.warning("End temperature recoding from keyboard")
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/derived_modbus_wrapper.py` & `temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/derived_modbus_wrapper.py`

 * *Ordering differences only*

 * *Files 15% similar despite different names*

```diff
@@ -1,61 +1,61 @@
-# This file implement ModbusWrapper in pymodbus
-# These decorators are designed for PyModbusWrapper
-
-from modbus_configuretools.modbus_wrapper import ModbusWrapper
-from pymodbus.client import ModbusSerialClient as ModbusClient
-from pymodbus.exceptions import ModbusIOException
-from modbus_configuretools.helper_function import check_is_port_connected, check_result
-from custom_logger import CustomLoggerWrapper, FMT_WITH_MODULENAME
-import logging
-
-logger_wrapper = CustomLoggerWrapper("derived_modbus_wrapper", logger_level=logging.WARNING, logger_fmt=FMT_WITH_MODULENAME, log_filename="derived_modbus_wrapper.log")
-logger_wrapper.InitLogger()
-mylogger = logger_wrapper.GetInitedLogger()
-
-class PyModbusWrapper(ModbusWrapper):
-
-    def __init__(self, method, port, parity, stopbits, bytesize, baudrate, timeout):
-        super().__init__(method, port, parity, stopbits, bytesize, baudrate, timeout)
-
-    def InitClient(self):
-        self._client = ModbusClient(method=self.method, port=self.port,
-                                    parity=self.parity, stopbits=self.stopbits, bytesize=self.bytesize, baudrate=self.baudrate, timeout=self.timeout)
-        self.is_port_connected = self._client.connect()
-        if (self.is_port_connected is False):
-            mylogger.error("Fail to connect client in InitClient().")
-
-        return self.is_port_connected
-
-    @check_is_port_connected
-    def CloseClient(self):
-        self._client.close()
-        self.is_port_connected = False
-
-    def GetValueInResult(self):
-        return self._result.registers
-
-    @check_result
-    @check_is_port_connected
-    def ReadHoldingRegisters(self, address, count, slaveID):
-        self._result = self._client.read_holding_registers(
-            address, count, slaveID)
-
-    @check_result
-    @check_is_port_connected
-    def WriteRegisgers(self, address, list_of_values, slaveID):
-        self._result = self._client.write_registers(
-            address, list_of_values, slaveID)
-
-    def CheckResult(self):
-        if (isinstance(self._result, ModbusIOException)):
-            mylogger.error("Modbus IOException occurs.")
-            return False
-        if (self._result is None):
-            mylogger.warning("self._result is None")
-            return None
-        else:
-            if self._result.isError():
-                mylogger.warning("isError() check failed")
-                return False
-            else:
+# This file implement ModbusWrapper in pymodbus
+# These decorators are designed for PyModbusWrapper
+
+from modbus_configuretools.modbus_wrapper import ModbusWrapper
+from pymodbus.client import ModbusSerialClient as ModbusClient
+from pymodbus.exceptions import ModbusIOException
+from modbus_configuretools.helper_function import check_is_port_connected, check_result
+from custom_logger import CustomLoggerWrapper, FMT_WITH_MODULENAME
+import logging
+
+logger_wrapper = CustomLoggerWrapper("derived_modbus_wrapper", logger_level=logging.WARNING, logger_fmt=FMT_WITH_MODULENAME, log_filename="derived_modbus_wrapper.log")
+logger_wrapper.InitLogger()
+mylogger = logger_wrapper.GetInitedLogger()
+
+class PyModbusWrapper(ModbusWrapper):
+
+    def __init__(self, method, port, parity, stopbits, bytesize, baudrate, timeout):
+        super().__init__(method, port, parity, stopbits, bytesize, baudrate, timeout)
+
+    def InitClient(self):
+        self._client = ModbusClient(method=self.method, port=self.port,
+                                    parity=self.parity, stopbits=self.stopbits, bytesize=self.bytesize, baudrate=self.baudrate, timeout=self.timeout)
+        self.is_port_connected = self._client.connect()
+        if (self.is_port_connected is False):
+            mylogger.error("Fail to connect client in InitClient().")
+
+        return self.is_port_connected
+
+    @check_is_port_connected
+    def CloseClient(self):
+        self._client.close()
+        self.is_port_connected = False
+
+    def GetValueInResult(self):
+        return self._result.registers
+
+    @check_result
+    @check_is_port_connected
+    def ReadHoldingRegisters(self, address, count, slaveID):
+        self._result = self._client.read_holding_registers(
+            address, count, slaveID)
+
+    @check_result
+    @check_is_port_connected
+    def WriteRegisgers(self, address, list_of_values, slaveID):
+        self._result = self._client.write_registers(
+            address, list_of_values, slaveID)
+
+    def CheckResult(self):
+        if (isinstance(self._result, ModbusIOException)):
+            mylogger.error("Modbus IOException occurs.")
+            return False
+        if (self._result is None):
+            mylogger.warning("self._result is None")
+            return None
+        else:
+            if self._result.isError():
+                mylogger.warning("isError() check failed")
+                return False
+            else:
                 return True
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/helper_function.py` & `temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/helper_function.py`

 * *Ordering differences only*

 * *Files 17% similar despite different names*

```diff
@@ -1,95 +1,95 @@
-# helper function for modbus_configuretools
-import numpy as np
-# logging setting
-import logging
-
-modbus_configuretools_logger = logging.getLogger("modbus_configuretools")
-modbus_configuretools_logger.propagate = False
-modbus_configuretools_logger.setLevel(level=logging.WARNING)
-logger_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
-handler_console = logging.StreamHandler()
-handler_console.setFormatter(logger_fmt)
-modbus_configuretools_logger.addHandler(handler_console)
-handler_file = logging.FileHandler("./modbus_configuretools.log")
-handler_file.setFormatter(logger_fmt)
-modbus_configuretools_logger.addHandler(handler_file)
-
-# helper function for derived_modbus_wrapper
-def check_is_port_connected(func):
-    def wrapper(self, *args, **kwargs):
-        if (self.is_port_connected == False):
-            modbus_configuretools_logger.warning(
-                "The port {0} is not connected. The program will continue, but the sensor is not connected.".format(self.port))
-            return False
-        else:
-            func(self, *args, **kwargs)
-            return True
-    return wrapper
-
-
-def check_result(func):
-    def wrapper(self, *args, **kwargs):
-        func(self, *args, **kwargs)
-        if (self.CheckResult() is None):
-            modbus_configuretools_logger.warning(
-                "_result is None. Read/Write registers first before check_isError. The program will continue, but the temperature and humidity is not correct.")
-            return False
-        if (self.CheckResult() == False):
-            modbus_configuretools_logger.warning(
-                "Read/Write registers is not correct.\nThe program will continue, but the temperature and humidity can't be recorded.")
-            return False
-        else:
-            return True
-    return wrapper
-
-# helper function for temperature_sensor
-
-
-def decode_16bit_complemental_code(func):
-    def wrapper(self, *args, **kwargs):
-        # This values shoud be a list
-        values_in_registers = func(self, *args, **kwargs)
-        values_in_registers_decoded = []
-        for value in values_in_registers:
-            values_in_registers_decoded.append(decodeint16(value))
-        return values_in_registers_decoded
-    return wrapper
-
-
-def calculate_temperature_and_humidity(func):
-    def wrapper(self, *args, **kwargs):
-        # This values shoud be a list
-        values_in_registers = func(self, *args, **kwargs)
-        values_in_registers_decoded = []
-        for value in values_in_registers:
-            values_in_registers_decoded.append(float(value)/10)
-        return values_in_registers_decoded
-    return wrapper
-
-
-def decodeint16(value):
-    return np.int16(value)
-
-
-def encodeint16(value):
-
-    if (value > 32767 or value < -32768):
-        return None
-    if value >= 0:
-        return value
-    if value < 0:
-        value = abs(value)
-        value_in_bits = bin(value).replace("0b", "")
-        print(value_in_bits)
-        _decode_buffers = ["1"] * 15
-        for index, _value in enumerate(value_in_bits):
-            if _value == "0":
-                _decode_buffers[14 + index - len(value_in_bits) + 1] = "1"
-            elif _value == "1":
-                _decode_buffers[14 + index - len(value_in_bits) + 1] = "0"
-        _decode_value = "0b1"
-        for _value in _decode_buffers:
-            _decode_value = _decode_value + _value
-        # only on system with more than 16 bits
-        decode_value = int("0b1" + bin(int(_decode_value, 2) + 1)[-15:], 2)
-        return decode_value
+# helper function for modbus_configuretools
+import numpy as np
+# logging setting
+import logging
+
+modbus_configuretools_logger = logging.getLogger("modbus_configuretools")
+modbus_configuretools_logger.propagate = False
+modbus_configuretools_logger.setLevel(level=logging.WARNING)
+logger_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
+handler_console = logging.StreamHandler()
+handler_console.setFormatter(logger_fmt)
+modbus_configuretools_logger.addHandler(handler_console)
+handler_file = logging.FileHandler("./modbus_configuretools.log")
+handler_file.setFormatter(logger_fmt)
+modbus_configuretools_logger.addHandler(handler_file)
+
+# helper function for derived_modbus_wrapper
+def check_is_port_connected(func):
+    def wrapper(self, *args, **kwargs):
+        if (self.is_port_connected == False):
+            modbus_configuretools_logger.warning(
+                "The port {0} is not connected. The program will continue, but the sensor is not connected.".format(self.port))
+            return False
+        else:
+            func(self, *args, **kwargs)
+            return True
+    return wrapper
+
+
+def check_result(func):
+    def wrapper(self, *args, **kwargs):
+        func(self, *args, **kwargs)
+        if (self.CheckResult() is None):
+            modbus_configuretools_logger.warning(
+                "_result is None. Read/Write registers first before check_isError. The program will continue, but the temperature and humidity is not correct.")
+            return False
+        if (self.CheckResult() == False):
+            modbus_configuretools_logger.warning(
+                "Read/Write registers is not correct.\nThe program will continue, but the temperature and humidity can't be recorded.")
+            return False
+        else:
+            return True
+    return wrapper
+
+# helper function for temperature_sensor
+
+
+def decode_16bit_complemental_code(func):
+    def wrapper(self, *args, **kwargs):
+        # This values shoud be a list
+        values_in_registers = func(self, *args, **kwargs)
+        values_in_registers_decoded = []
+        for value in values_in_registers:
+            values_in_registers_decoded.append(decodeint16(value))
+        return values_in_registers_decoded
+    return wrapper
+
+
+def calculate_temperature_and_humidity(func):
+    def wrapper(self, *args, **kwargs):
+        # This values shoud be a list
+        values_in_registers = func(self, *args, **kwargs)
+        values_in_registers_decoded = []
+        for value in values_in_registers:
+            values_in_registers_decoded.append(float(value)/10)
+        return values_in_registers_decoded
+    return wrapper
+
+
+def decodeint16(value):
+    return np.int16(value)
+
+
+def encodeint16(value):
+
+    if (value > 32767 or value < -32768):
+        return None
+    if value >= 0:
+        return value
+    if value < 0:
+        value = abs(value)
+        value_in_bits = bin(value).replace("0b", "")
+        print(value_in_bits)
+        _decode_buffers = ["1"] * 15
+        for index, _value in enumerate(value_in_bits):
+            if _value == "0":
+                _decode_buffers[14 + index - len(value_in_bits) + 1] = "1"
+            elif _value == "1":
+                _decode_buffers[14 + index - len(value_in_bits) + 1] = "0"
+        _decode_value = "0b1"
+        for _value in _decode_buffers:
+            _decode_value = _decode_value + _value
+        # only on system with more than 16 bits
+        decode_value = int("0b1" + bin(int(_decode_value, 2) + 1)[-15:], 2)
+        return decode_value
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/modbus_configuretools/temperature_sensor.py` & `temperature_sensor_reader_xzf8971-1.4.0/modbus_configuretools/temperature_sensor.py`

 * *Ordering differences only*

 * *Files 22% similar despite different names*

```diff
@@ -1,193 +1,193 @@
-import numpy as np
-import time
-from modbus_configuretools.derived_modbus_wrapper import PyModbusWrapper
-from modbus_configuretools.helper_function import encodeint16, decodeint16, decode_16bit_complemental_code, calculate_temperature_and_humidity, modbus_configuretools_logger
-
-# JDRK config
-ADDRESS_HUMIDITY = 0x0000
-ADDRESS_TEMPERATURE_DEW_POINT = 0x0001
-ADDRESS_TEMPERATURE = 0x0002
-ADDRESS_TEMPERATURE_CALI = 0x0050
-ADDRESS_HUMUDITY_CALI = 0x0051
-ADDRESS_SLAVEID = 0x07D0
-ADDRESS_BAUDRATE = 0x07D1
-
-TEMPERATURE_CALI = 164
-HUMIDITY_CALI = 7
-SLAVEID = 1
-BAUDRATE = 1
-
-# For retry check
-RETRY_TIME = 10
-# Normal sleep
-JDRK_NORMAL_DELAY = 1
-
-
-class JDRKAddressConfig():
-    """
-    It's OK to set None for unknown value. SLAVEID must specified.
-    """
-
-    def __init__(self, add_humidity, add_temperature_dew_point, add_temperature,  add_salveid, add_baudrate, add_temperature_cali, add_humidity_cali, temperature_cali, humidity_cali, slaveID, baudrate):
-        self.ADDRESS_HUMIDITY = add_humidity
-        self.ADDRESS_TEMPERATURE_DEW_POINT = add_temperature_dew_point
-        self.ADDRESS_TEMPERATURE = add_temperature
-        self.ADDRESS_TEMPERATURE_CALI = add_temperature_cali
-        self.ADDRESS_HUMUDITY_CALI = add_humidity_cali
-        self.ADDRESS_SLAVEID = add_salveid
-        self.ADDRESS_BAUDRATE = add_baudrate
-
-        self.TEMPERATURE_CALI = temperature_cali
-        self.HUMIDITY_CALI = humidity_cali
-        if (slaveID < 256 and slaveID > 0):
-            self.SLAVEID = slaveID
-        else:
-            print(
-                "JDRKAddressConfig WARNING slaveID must < 256 and < 0. Specified to default value 1")
-            self.SLAVEID = 1
-        self.BAUDRATE = baudrate
-
-
-jdrk_config = JDRKAddressConfig(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID,
-                                ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
-
-
-def check_and_retry_Jiandarenke(func):
-    def wrapper(self, *args, **kwargs):
-        result = func(self, *args, **kwargs)
-        if (len(result) > 0):
-            return result
-        else:
-            time.sleep(JDRK_NORMAL_DELAY)
-            for i_retry in range(0, RETRY_TIME):
-                result = func(self, *args, **kwargs)
-                time.sleep(JDRK_NORMAL_DELAY)
-                if (len(result) > 0):
-                    return result
-        modbus_configuretools_logger.warning(
-            "Fail read or write JDRK register after {0} times retry".format(RETRY_TIME))
-        return []
-    return wrapper
-
-
-class RS485_Jiandarenke(PyModbusWrapper):
-
-    def __init__(self, port, baudrate=4800, timeout=1):
-        super().__init__(method='rtu', port=port, parity='N',
-                         stopbits=1, bytesize=8, baudrate=baudrate, timeout=timeout)
-
-    # temperature_cali and humidity_cali should be 10 times, and integer
-
-    def CalibrationJiandarenke(self, JDRK_config=jdrk_config):
-        is_success = self.WriteRegisgers(JDRK_config.ADDRESS_TEMPERATURE_CALI, [
-                                         encodeint16(JDRK_config.TEMPERATURE_CALI)], JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to write Temperture Calibtration register")
-        is_success = self.WriteRegisgers(
-            JDRK_config.ADDRESS_HUMUDITY_CALI, [encodeint16(JDRK_config.ADDRESS_HUMUDITY_CALI)], JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to write Humidity Calibtration register")
-
-    def DumpNonZeroRegisters(self, output_filename, begin_address, end_address, JDRK_config=jdrk_config):
-        read_address = begin_address
-        pass
-
-    @calculate_temperature_and_humidity
-    @decode_16bit_complemental_code
-    @check_and_retry_Jiandarenke
-    def ReadTemperatureAndHumidity(self, JDRK_config=jdrk_config):
-        is_success = self.ReadHoldingRegisters(
-            JDRK_config.ADDRESS_HUMIDITY, 3, JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to read Temperature and Humidity register")
-            return []
-        else:
-            return [self.GetValueInResult()[2], self.GetValueInResult()[1], self.GetValueInResult()[0]]
-
-    @calculate_temperature_and_humidity
-    @decode_16bit_complemental_code
-    @check_and_retry_Jiandarenke
-    def ReadTemperature(self, JDRK_config=jdrk_config):
-        is_success = self.ReadHoldingRegisters(
-            JDRK_config.ADDRESS_TEMPERATURE, 1, JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to read Temperature register")
-            return []
-        else:
-            return self.GetValueInResult()
-
-    @calculate_temperature_and_humidity
-    @decode_16bit_complemental_code
-    @check_and_retry_Jiandarenke
-    def ReadTemperatureDewPoint(self, JDRK_config=jdrk_config):
-        is_success = self.ReadHoldingRegisters(
-            JDRK_config.ADDRESS_TEMPERATURE_DEW_POINT, 1, JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to read Temperature Dew Point register")
-            return []
-        else:
-            return self.GetValueInResult()
-
-    @calculate_temperature_and_humidity
-    @decode_16bit_complemental_code
-    @check_and_retry_Jiandarenke
-    def ReadHumidity(self, JDRK_config=jdrk_config):
-        is_success = self.ReadHoldingRegisters(
-            JDRK_config.ADDRESS_HUMIDITY, 1, JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to read Humidity register")
-            return []
-        else:
-            return self.GetValueInResult()
-
-    @calculate_temperature_and_humidity
-    @decode_16bit_complemental_code
-    @check_and_retry_Jiandarenke
-    def ReadTemperatureAndHumidityCalibration(self, JDRK_config=jdrk_config):
-        is_success = self.ReadHoldingRegisters(
-            JDRK_config.ADDRESS_TEMPERATURE_CALI, 2, JDRK_config)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to read Temperature and Humidity register")
-            return []
-        else:
-            return self.GetValueInResult()
-
-    @check_and_retry_Jiandarenke
-    def ReadSlaveIDAndBaudrate(self, JDRK_config=jdrk_config):
-        is_success = self.ReadHoldingRegisters(
-            JDRK_config.ADDRESS_SLAVEID, 2, JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to read SlaveID and Baudrate register")
-            return []
-        else:
-            return self.GetValueInResult()
-
-    # Only usable for sepecified sensor. Like Jiandarenke 485
-    def WriteSlaveIDAndBaudrate(self, JDRK_config=jdrk_config):
-        is_success = self.WriteRegisgers(
-            JDRK_config.ADDRESS_SLAVEID, [JDRK_config.SLAVEID, JDRK_config.BAUDRATE], JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to write SlaveID and Baudrate register")
-
-    def WriteSlaveID(self, JDRK_config=jdrk_config):
-        is_success = self.WriteRegisgers(
-            JDRK_config.ADDRESS_SLAVEID, [JDRK_config.SLAVEID], JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to write SlaveID register")
-
-    def WriteBaudrate(self, JDRK_config=jdrk_config):
-        is_success = self.WriteRegisgers(
-            JDRK_config.ADDRESS_BAUDRATE, [JDRK_config.BAUDRATE], JDRK_config.SLAVEID)
-        if (not is_success):
-            modbus_configuretools_logger.warning(
-                "Fail to write Baudrate register")
+import numpy as np
+import time
+from modbus_configuretools.derived_modbus_wrapper import PyModbusWrapper
+from modbus_configuretools.helper_function import encodeint16, decodeint16, decode_16bit_complemental_code, calculate_temperature_and_humidity, modbus_configuretools_logger
+
+# JDRK config
+ADDRESS_HUMIDITY = 0x0000
+ADDRESS_TEMPERATURE_DEW_POINT = 0x0001
+ADDRESS_TEMPERATURE = 0x0002
+ADDRESS_TEMPERATURE_CALI = 0x0050
+ADDRESS_HUMUDITY_CALI = 0x0051
+ADDRESS_SLAVEID = 0x07D0
+ADDRESS_BAUDRATE = 0x07D1
+
+TEMPERATURE_CALI = 164
+HUMIDITY_CALI = 7
+SLAVEID = 1
+BAUDRATE = 1
+
+# For retry check
+RETRY_TIME = 10
+# Normal sleep
+JDRK_NORMAL_DELAY = 1
+
+
+class JDRKAddressConfig():
+    """
+    It's OK to set None for unknown value. SLAVEID must specified.
+    """
+
+    def __init__(self, add_humidity, add_temperature_dew_point, add_temperature,  add_salveid, add_baudrate, add_temperature_cali, add_humidity_cali, temperature_cali, humidity_cali, slaveID, baudrate):
+        self.ADDRESS_HUMIDITY = add_humidity
+        self.ADDRESS_TEMPERATURE_DEW_POINT = add_temperature_dew_point
+        self.ADDRESS_TEMPERATURE = add_temperature
+        self.ADDRESS_TEMPERATURE_CALI = add_temperature_cali
+        self.ADDRESS_HUMUDITY_CALI = add_humidity_cali
+        self.ADDRESS_SLAVEID = add_salveid
+        self.ADDRESS_BAUDRATE = add_baudrate
+
+        self.TEMPERATURE_CALI = temperature_cali
+        self.HUMIDITY_CALI = humidity_cali
+        if (slaveID < 256 and slaveID > 0):
+            self.SLAVEID = slaveID
+        else:
+            print(
+                "JDRKAddressConfig WARNING slaveID must < 256 and < 0. Specified to default value 1")
+            self.SLAVEID = 1
+        self.BAUDRATE = baudrate
+
+
+jdrk_config = JDRKAddressConfig(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID,
+                                ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
+
+
+def check_and_retry_Jiandarenke(func):
+    def wrapper(self, *args, **kwargs):
+        result = func(self, *args, **kwargs)
+        if (len(result) > 0):
+            return result
+        else:
+            time.sleep(JDRK_NORMAL_DELAY)
+            for i_retry in range(0, RETRY_TIME):
+                result = func(self, *args, **kwargs)
+                time.sleep(JDRK_NORMAL_DELAY)
+                if (len(result) > 0):
+                    return result
+        modbus_configuretools_logger.warning(
+            "Fail read or write JDRK register after {0} times retry".format(RETRY_TIME))
+        return []
+    return wrapper
+
+
+class RS485_Jiandarenke(PyModbusWrapper):
+
+    def __init__(self, port, baudrate=4800, timeout=1):
+        super().__init__(method='rtu', port=port, parity='N',
+                         stopbits=1, bytesize=8, baudrate=baudrate, timeout=timeout)
+
+    # temperature_cali and humidity_cali should be 10 times, and integer
+
+    def CalibrationJiandarenke(self, JDRK_config=jdrk_config):
+        is_success = self.WriteRegisgers(JDRK_config.ADDRESS_TEMPERATURE_CALI, [
+                                         encodeint16(JDRK_config.TEMPERATURE_CALI)], JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to write Temperture Calibtration register")
+        is_success = self.WriteRegisgers(
+            JDRK_config.ADDRESS_HUMUDITY_CALI, [encodeint16(JDRK_config.ADDRESS_HUMUDITY_CALI)], JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to write Humidity Calibtration register")
+
+    def DumpNonZeroRegisters(self, output_filename, begin_address, end_address, JDRK_config=jdrk_config):
+        read_address = begin_address
+        pass
+
+    @calculate_temperature_and_humidity
+    @decode_16bit_complemental_code
+    @check_and_retry_Jiandarenke
+    def ReadTemperatureAndHumidity(self, JDRK_config=jdrk_config):
+        is_success = self.ReadHoldingRegisters(
+            JDRK_config.ADDRESS_HUMIDITY, 3, JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to read Temperature and Humidity register")
+            return []
+        else:
+            return [self.GetValueInResult()[2], self.GetValueInResult()[1], self.GetValueInResult()[0]]
+
+    @calculate_temperature_and_humidity
+    @decode_16bit_complemental_code
+    @check_and_retry_Jiandarenke
+    def ReadTemperature(self, JDRK_config=jdrk_config):
+        is_success = self.ReadHoldingRegisters(
+            JDRK_config.ADDRESS_TEMPERATURE, 1, JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to read Temperature register")
+            return []
+        else:
+            return self.GetValueInResult()
+
+    @calculate_temperature_and_humidity
+    @decode_16bit_complemental_code
+    @check_and_retry_Jiandarenke
+    def ReadTemperatureDewPoint(self, JDRK_config=jdrk_config):
+        is_success = self.ReadHoldingRegisters(
+            JDRK_config.ADDRESS_TEMPERATURE_DEW_POINT, 1, JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to read Temperature Dew Point register")
+            return []
+        else:
+            return self.GetValueInResult()
+
+    @calculate_temperature_and_humidity
+    @decode_16bit_complemental_code
+    @check_and_retry_Jiandarenke
+    def ReadHumidity(self, JDRK_config=jdrk_config):
+        is_success = self.ReadHoldingRegisters(
+            JDRK_config.ADDRESS_HUMIDITY, 1, JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to read Humidity register")
+            return []
+        else:
+            return self.GetValueInResult()
+
+    @calculate_temperature_and_humidity
+    @decode_16bit_complemental_code
+    @check_and_retry_Jiandarenke
+    def ReadTemperatureAndHumidityCalibration(self, JDRK_config=jdrk_config):
+        is_success = self.ReadHoldingRegisters(
+            JDRK_config.ADDRESS_TEMPERATURE_CALI, 2, JDRK_config)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to read Temperature and Humidity register")
+            return []
+        else:
+            return self.GetValueInResult()
+
+    @check_and_retry_Jiandarenke
+    def ReadSlaveIDAndBaudrate(self, JDRK_config=jdrk_config):
+        is_success = self.ReadHoldingRegisters(
+            JDRK_config.ADDRESS_SLAVEID, 2, JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to read SlaveID and Baudrate register")
+            return []
+        else:
+            return self.GetValueInResult()
+
+    # Only usable for sepecified sensor. Like Jiandarenke 485
+    def WriteSlaveIDAndBaudrate(self, JDRK_config=jdrk_config):
+        is_success = self.WriteRegisgers(
+            JDRK_config.ADDRESS_SLAVEID, [JDRK_config.SLAVEID, JDRK_config.BAUDRATE], JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to write SlaveID and Baudrate register")
+
+    def WriteSlaveID(self, JDRK_config=jdrk_config):
+        is_success = self.WriteRegisgers(
+            JDRK_config.ADDRESS_SLAVEID, [JDRK_config.SLAVEID], JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to write SlaveID register")
+
+    def WriteBaudrate(self, JDRK_config=jdrk_config):
+        is_success = self.WriteRegisgers(
+            JDRK_config.ADDRESS_BAUDRATE, [JDRK_config.BAUDRATE], JDRK_config.SLAVEID)
+        if (not is_success):
+            modbus_configuretools_logger.warning(
+                "Fail to write Baudrate register")
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/pyproject.toml` & `temperature_sensor_reader_xzf8971-1.4.0/pyproject.toml`

 * *Files 20% similar despite different names*

```diff
@@ -1,22 +1,22 @@
-[build-system]
-requires = ["setuptools>=61.0", "setuptools-scm", "cython ~= 0.29.0"]
-build-backend = "setuptools.build_meta"
-
-[project]
-name = "temperature_sensor_reader_xzf8971"
-version = "1.3.0"
-authors = [
-  { name="Zifeng", email="zifeng.xu@foxmail.com" },
-]
-description = "A package to read/write registers on a temperature sensor with python."
-readme = "README.md"
-requires-python = ">=3.7"
-classifiers = [
-    "Programming Language :: Python :: 3",
-    "License :: OSI Approved :: MIT License",
-    "Operating System :: OS Independent",
-]
-dependencies = ["numpy", "pyserial", "pyserial-asyncio", "pymodbus", "pandas", "bs4", "custom-logger-xzf8971"]
-[project.urls]
-"Homepage" = "https://github.com/xzf89718/temperature_sensor_reader"
-"Bug Tracker" = "https://github.com/xzf89718/temperature_sensor_reader/issues"
+[build-system]
+requires = ["setuptools>=61.0", "setuptools-scm", "cython ~= 0.29.0"]
+build-backend = "setuptools.build_meta"
+
+[project]
+name = "temperature_sensor_reader_xzf8971"
+version = "1.4.0"
+authors = [
+  { name="Zifeng", email="zifeng.xu@foxmail.com" },
+]
+description = "A package to read/write registers on a temperature sensor with python."
+readme = "README.md"
+requires-python = ">=3.7"
+classifiers = [
+    "Programming Language :: Python :: 3",
+    "License :: OSI Approved :: MIT License",
+    "Operating System :: OS Independent",
+]
+dependencies = ["numpy", "pyserial", "pyserial-asyncio", "pymodbus", "pandas", "bs4", "custom-logger-xzf8971"]
+[project.urls]
+"Homepage" = "https://github.com/xzf89718/temperature_sensor_reader"
+"Bug Tracker" = "https://github.com/xzf89718/temperature_sensor_reader/issues"
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/temperature_data_analysis/data_wrapper.py` & `temperature_sensor_reader_xzf8971-1.4.0/temperature_data_analysis/data_wrapper.py`

 * *Ordering differences only*

 * *Files 14% similar despite different names*

```diff
@@ -1,104 +1,104 @@
-import re
-import time
-import datetime
-DATETIME_FMT = "%Y-%m-%d %H:%M:%S"
-
-
-class DataCell():
-    def __init__(self, measure_time, temp, humidity):
-        self.measure_time = measure_time
-        self.temp = temp
-        self.humidity = humidity
-
-
-class DataWrapperBase():
-
-    def __init__(self):
-        # self.re_measure_time = re.compile(re_measure_time)
-        # self.re_temp = re.compile(re_temp)
-        # self.re_humidity = re.compile(re_humidity)
-        self.all_data = []
-        self._line = None
-
-    def ReadDataFile(self, filename):
-        pass
-
-    def ReadTimeFromLine(self):
-        pass
-
-    def ReadTempAndHumidityFromLine(self):
-        pass
-
-    def GetHumidityAndTemperature(self, measure_time):
-        pass
-
-    def GetDataToPlot(self):
-        _data_measure_time = []
-        _data_temp = []
-        _data_humidity = []
-
-        for _data in self.all_data:
-            _data_measure_time.append(_data.measure_time)
-            _data_temp.append(_data.temp)
-            _data_humidity.append(_data.humidity)
-        return _data_measure_time, _data_temp, _data_humidity
-
-
-class JDRKDataWrapper(DataWrapperBase):
-
-    def __init__(self):
-        super().__init__()
-
-    def ReadDataFile(self, filename):
-        with open(filename, "r") as file_object:
-            self._line = "DEFAULT"
-            while (self._line != ""):
-                self._line = file_object.readline()
-                measure_measure_time = self.ReadTimeFromLine()
-                # print(measure_measure_time)
-                measure_temp, measure_humidity = self.ReadTempAndHumidityFromLine()
-                # print(measure_temp, measure_humidity)
-                if (measure_measure_time is None):
-                    continue
-                if (not(measure_temp or measure_humidity)):
-                    continue
-                self.all_data.append(
-                    DataCell(measure_measure_time, measure_temp, measure_humidity))
-
-    def ReadTimeFromLine(self):
-        re_measure_time = re.compile(
-            "\d{4}-\d{1,2}-\d{1,2} \d{1,2}\:\d{1,2}\:\d{1,2}")
-        str_measure_time = re_measure_time.findall(self._line)
-
-        if (len(str_measure_time) > 0):
-            return datetime.datetime.strptime(str_measure_time[0], DATETIME_FMT)
-        else:
-            return None
-
-    def ReadTempAndHumidityFromLine(self):
-        re_temperature = re.compile("[-+]*\d{1,}\.\d{1,2}")
-        re_humidity = re.compile("[-+]*\d{1,}\.\d{1,2}")
-        str_temperature = re_temperature.findall(self._line)
-        str_humidity = re_humidity.findall(self._line)
-
-        _temp = None
-        _humi = None
-        if (len(str_temperature) == 0):
-            pass
-        if (len(str_temperature) == 2):
-            _temp = float(str_temperature[0])
-            _humi = float(str_temperature[1])
-
-        return _temp, _humi
-
-    def GetHumidityAndTemperature(self, measure_time):
-        if (not isinstance(measure_time, datetime.datetime)):
-            raise NotImplementedError("time must be datetime.datetime")
-        data_index = None
-        for index, data in enumerate(self.all_data[:-1]):
-            if (measure_time > data.measure_time and measure_time < self.all_data[index + 1].measure_time):
-                data_index = index
-        if (data_index is None):
-            print("Fail find a suitable time interval.")
-            return None, None
-        return self.all_data[data_index], self.all_data[data_index + 1]
+import re
+import time
+import datetime
+DATETIME_FMT = "%Y-%m-%d %H:%M:%S"
+
+
+class DataCell():
+    def __init__(self, measure_time, temp, humidity):
+        self.measure_time = measure_time
+        self.temp = temp
+        self.humidity = humidity
+
+
+class DataWrapperBase():
+
+    def __init__(self):
+        # self.re_measure_time = re.compile(re_measure_time)
+        # self.re_temp = re.compile(re_temp)
+        # self.re_humidity = re.compile(re_humidity)
+        self.all_data = []
+        self._line = None
+
+    def ReadDataFile(self, filename):
+        pass
+
+    def ReadTimeFromLine(self):
+        pass
+
+    def ReadTempAndHumidityFromLine(self):
+        pass
+
+    def GetHumidityAndTemperature(self, measure_time):
+        pass
+
+    def GetDataToPlot(self):
+        _data_measure_time = []
+        _data_temp = []
+        _data_humidity = []
+
+        for _data in self.all_data:
+            _data_measure_time.append(_data.measure_time)
+            _data_temp.append(_data.temp)
+            _data_humidity.append(_data.humidity)
+        return _data_measure_time, _data_temp, _data_humidity
+
+
+class JDRKDataWrapper(DataWrapperBase):
+
+    def __init__(self):
+        super().__init__()
+
+    def ReadDataFile(self, filename):
+        with open(filename, "r") as file_object:
+            self._line = "DEFAULT"
+            while (self._line != ""):
+                self._line = file_object.readline()
+                measure_measure_time = self.ReadTimeFromLine()
+                # print(measure_measure_time)
+                measure_temp, measure_humidity = self.ReadTempAndHumidityFromLine()
+                # print(measure_temp, measure_humidity)
+                if (measure_measure_time is None):
+                    continue
+                if (not(measure_temp or measure_humidity)):
+                    continue
+                self.all_data.append(
+                    DataCell(measure_measure_time, measure_temp, measure_humidity))
+
+    def ReadTimeFromLine(self):
+        re_measure_time = re.compile(
+            "\d{4}-\d{1,2}-\d{1,2} \d{1,2}\:\d{1,2}\:\d{1,2}")
+        str_measure_time = re_measure_time.findall(self._line)
+
+        if (len(str_measure_time) > 0):
+            return datetime.datetime.strptime(str_measure_time[0], DATETIME_FMT)
+        else:
+            return None
+
+    def ReadTempAndHumidityFromLine(self):
+        re_temperature = re.compile("[-+]*\d{1,}\.\d{1,2}")
+        re_humidity = re.compile("[-+]*\d{1,}\.\d{1,2}")
+        str_temperature = re_temperature.findall(self._line)
+        str_humidity = re_humidity.findall(self._line)
+
+        _temp = None
+        _humi = None
+        if (len(str_temperature) == 0):
+            pass
+        if (len(str_temperature) == 2):
+            _temp = float(str_temperature[0])
+            _humi = float(str_temperature[1])
+
+        return _temp, _humi
+
+    def GetHumidityAndTemperature(self, measure_time):
+        if (not isinstance(measure_time, datetime.datetime)):
+            raise NotImplementedError("time must be datetime.datetime")
+        data_index = None
+        for index, data in enumerate(self.all_data[:-1]):
+            if (measure_time > data.measure_time and measure_time < self.all_data[index + 1].measure_time):
+                data_index = index
+        if (data_index is None):
+            print("Fail find a suitable time interval.")
+            return None, None
+        return self.all_data[data_index], self.all_data[data_index + 1]
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO` & `temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,86 +1,86 @@
-Metadata-Version: 2.1
-Name: temperature-sensor-reader-xzf8971
-Version: 1.3.0
-Summary: A package to read/write registers on a temperature sensor with python.
-Author-email: Zifeng <zifeng.xu@foxmail.com>
-Project-URL: Homepage, https://github.com/xzf89718/temperature_sensor_reader
-Project-URL: Bug Tracker, https://github.com/xzf89718/temperature_sensor_reader/issues
-Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: OS Independent
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
-# temperature_sensor_reader
-This is a temperature sensor package designed for modbus. Implemented in pymodbus only. PyPI website: https://pypi.org/project/temperature-sensor-reader-xzf8971/
-## Install
-from pypi:  
-```bash
-pip install temperature-sensor-reader-xzf8971  
-```
-from github:  
-```bahs
-pip install git+https://github.com/xzf89718/temperature_sensor_reader
-```
-## Jiandarenke modbus RS485 as example  
-### Before run scripts
-Check the COM and chmod  
-```bash
-chmod 666 \dev\ttyUSBx
-```
-### Import modules  
-```python
-from modbus_configuretools import temperature_sensor.RS485_Jiandarenke as RS485_JDRK  
-from modbus_configuretools import temperature_sensor.JDRKAddressConfig as Config
-```
-### Configure parameters for Jiandarenke RS485 sensor
-It's OK to set None for unkown value
-```python
-# Modify these config values 
-# Please configure these value in temperature_sensor before read or write values  
-# SLAVEID must be specified. If SLAVEID is none, set to 1  
-# ADDRESS_HUMIDITY = 0x0000  
-# ADDRESS_TEMPERATURE_DEW_POINT = 0x0001  
-# ADDRESS_TEMPERATURE = 0x0002  
-# ADDRESS_TEMPERATURE_CALI = 0x0050  
-# ADDRESS_HUMUDITY_CALI = 0x0051  
-# ADDRESS_SLAVEID = 0x07D0  
-# ADDRESS_BAUDRATE = 0x07D1  
-# TEMPERATURE_CALI = 164  
-# HUMIDITY_CALI = 7  
-# SLAVEID = 1
-# BAUDRATE = 1
-myconfig = Config(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID, ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
-```
-### Calibration of sensor. Not necessary calibration every time  
-```python
-sensor.CalibrationJiandarenke(myconfig)  
-```
-### Set slaveID and baudrate
-Please make sure only 1 sensor connect to the modbus bus
-```python
-sensor.WriteSlaveIDAndBaudrate(myconfig)
-```
-### Init and read measured values from sensor  
-```python
-# Create a wrapper for JDRK sensor  
-sensor = RS485_JDRK(port="/dev/ttyUSB0")  
-# Init and connect client
-sensor.InitClient()  
-# Read slaveID and baudrate  
-slaveID, baudrate = sensor.ReadSalveIDAndBaudrate(myconfig)  
-# Read temperature, dew point, humidity in one request  
-# Only correct for specified sensor
-temperature, dew_point_temperature, humidity = sensor.ReadTemperatureAndHumidity(myconfig)  
-# Read temperature only  
-temperature = sensor.ReadTemperature(myconfig)  
-# Read dew point temperature  
-dew_point_temperature = sensor.ReadTemperatureDewPoint(myconfig)  
-# Read humidity only  
-humidity = sensor.ReadTemperature(myconfig)  
-```
-### Close the sensor
-```python
-sensor.close()
-```
+Metadata-Version: 2.1
+Name: temperature-sensor-reader-xzf8971
+Version: 1.4.0
+Summary: A package to read/write registers on a temperature sensor with python.
+Author-email: Zifeng <zifeng.xu@foxmail.com>
+Project-URL: Homepage, https://github.com/xzf89718/temperature_sensor_reader
+Project-URL: Bug Tracker, https://github.com/xzf89718/temperature_sensor_reader/issues
+Classifier: Programming Language :: Python :: 3
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# temperature_sensor_reader
+This is a temperature sensor package designed for modbus. Implemented in pymodbus only. PyPI website: https://pypi.org/project/temperature-sensor-reader-xzf8971/
+## Install
+from pypi:  
+```bash
+pip install temperature-sensor-reader-xzf8971  
+```
+from github:  
+```bahs
+pip install git+https://github.com/xzf89718/temperature_sensor_reader
+```
+## Jiandarenke modbus RS485 as example  
+### Before run scripts
+Check the COM and chmod  
+```bash
+chmod 666 \dev\ttyUSBx
+```
+### Import modules  
+```python
+from modbus_configuretools import temperature_sensor.RS485_Jiandarenke as RS485_JDRK  
+from modbus_configuretools import temperature_sensor.JDRKAddressConfig as Config
+```
+### Configure parameters for Jiandarenke RS485 sensor
+It's OK to set None for unkown value
+```python
+# Modify these config values 
+# Please configure these value in temperature_sensor before read or write values  
+# SLAVEID must be specified. If SLAVEID is none, set to 1  
+# ADDRESS_HUMIDITY = 0x0000  
+# ADDRESS_TEMPERATURE_DEW_POINT = 0x0001  
+# ADDRESS_TEMPERATURE = 0x0002  
+# ADDRESS_TEMPERATURE_CALI = 0x0050  
+# ADDRESS_HUMUDITY_CALI = 0x0051  
+# ADDRESS_SLAVEID = 0x07D0  
+# ADDRESS_BAUDRATE = 0x07D1  
+# TEMPERATURE_CALI = 164  
+# HUMIDITY_CALI = 7  
+# SLAVEID = 1
+# BAUDRATE = 1
+myconfig = Config(ADDRESS_HUMIDITY, ADDRESS_TEMPERATURE_DEW_POINT, ADDRESS_TEMPERATURE, ADDRESS_SLAVEID, ADDRESS_BAUDRATE, ADDRESS_TEMPERATURE_CALI, ADDRESS_HUMUDITY_CALI, TEMPERATURE_CALI, HUMIDITY_CALI, SLAVEID, BAUDRATE)
+```
+### Calibration of sensor. Not necessary calibration every time  
+```python
+sensor.CalibrationJiandarenke(myconfig)  
+```
+### Set slaveID and baudrate
+Please make sure only 1 sensor connect to the modbus bus
+```python
+sensor.WriteSlaveIDAndBaudrate(myconfig)
+```
+### Init and read measured values from sensor  
+```python
+# Create a wrapper for JDRK sensor  
+sensor = RS485_JDRK(port="/dev/ttyUSB0")  
+# Init and connect client
+sensor.InitClient()  
+# Read slaveID and baudrate  
+slaveID, baudrate = sensor.ReadSalveIDAndBaudrate(myconfig)  
+# Read temperature, dew point, humidity in one request  
+# Only correct for specified sensor
+temperature, dew_point_temperature, humidity = sensor.ReadTemperatureAndHumidity(myconfig)  
+# Read temperature only  
+temperature = sensor.ReadTemperature(myconfig)  
+# Read dew point temperature  
+dew_point_temperature = sensor.ReadTemperatureDewPoint(myconfig)  
+# Read humidity only  
+humidity = sensor.ReadTemperature(myconfig)  
+```
+### Close the sensor
+```python
+sensor.close()
+```
```

### Comparing `temperature_sensor_reader_xzf8971-1.3.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt` & `temperature_sensor_reader_xzf8971-1.4.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt`

 * *Files identical despite different names*

