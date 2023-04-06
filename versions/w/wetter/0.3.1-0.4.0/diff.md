# Comparing `tmp/wetter-0.3.1.tar.gz` & `tmp/wetter-0.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wetter-0.3.1.tar", max compression
+gzip compressed data, was "wetter-0.4.0.tar", max compression
```

## Comparing `wetter-0.3.1.tar` & `wetter-0.4.0.tar`

### file list

```diff
@@ -1,8 +1,14 @@
--rw-r--r--   0        0        0     8146 2023-04-04 19:49:08.675412 wetter-0.3.1/README.md
--rw-r--r--   0        0        0     1491 2023-04-04 19:49:08.679412 wetter-0.3.1/pyproject.toml
--rw-r--r--   0        0        0     1939 2023-04-04 19:49:08.679412 wetter-0.3.1/wetter/__init__.py
--rw-r--r--   0        0        0     7262 2023-04-04 19:49:08.679412 wetter-0.3.1/wetter/cli.py
--rw-r--r--   0        0        0     5997 2023-04-04 19:49:08.679412 wetter-0.3.1/wetter/config.py
--rw-r--r--   0        0        0    11533 2023-04-04 19:49:08.679412 wetter-0.3.1/wetter/conn.py
--rw-r--r--   0        0        0     5108 2023-04-04 19:49:08.679412 wetter-0.3.1/wetter/queries.py
--rw-r--r--   0        0        0     9519 1970-01-01 00:00:00.000000 wetter-0.3.1/PKG-INFO
+-rw-r--r--   0        0        0     8538 2023-04-06 18:05:02.976247 wetter-0.4.0/README.md
+-rw-r--r--   0        0        0     1491 2023-04-06 18:05:02.976247 wetter-0.4.0/pyproject.toml
+-rw-r--r--   0        0        0     2025 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/__init__.py
+-rw-r--r--   0        0        0    10236 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/app.py
+-rw-r--r--   0        0        0     1203 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/backend/__init__.py
+-rw-r--r--   0        0        0     7117 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/backend/extern.py
+-rw-r--r--   0        0        0     5307 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/backend/local.py
+-rw-r--r--   0        0        0     5631 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/backend/queries.py
+-rw-r--r--   0        0        0      409 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/config/__init__.py
+-rw-r--r--   0        0        0     4131 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/config/config.py
+-rw-r--r--   0        0        0     1418 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/config/defaults.py
+-rw-r--r--   0        0        0     1906 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/config/parser.py
+-rw-r--r--   0        0        0     3057 2023-04-06 18:05:02.980248 wetter-0.4.0/wetter/tools.py
+-rw-r--r--   0        0        0     9911 1970-01-01 00:00:00.000000 wetter-0.4.0/PKG-INFO
```

### Comparing `wetter-0.3.1/README.md` & `wetter-0.4.0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 <h1 align="center">wetter</h1>
 <p align=center>
-  <img src="https://raw.githubusercontent.com/ucyo/wetter-py/master/assets/undraw_weather.svg" width=300px/>
+  <img src="https://raw.githubusercontent.com/ucyo/wetter-py/master/assets/undraw_weather.svg" width=500px/>
 </p>
 <p align=center>
 <img alt="PyPI" src="https://img.shields.io/pypi/v/wetter?color=blue">
 <img alt="PyPI - License" src="https://img.shields.io/pypi/l/wetter">
 <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/wetter">
 <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/wetter">
 <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/wetter">
@@ -19,14 +19,15 @@
 
 The tool provides the `wetter` command line tool with several subcommands:
 
 |command|Description|
 |-------|-----------|
 |`wetter latest`| Return latest measurement for your favourite city|
 |`wetter update`|Update datastore with latest measurements|
+|`wetter update --historical`|Update datastore with measurements from last year|
 |`wetter compare --last-week`| Compare current weather w/ last week |
 |`wetter compare --last-month`| Compare current weather w/ last month |
 |`wetter compare --last-year`| Compare current weather w/ last year |
 |`wetter compare --month`| Analyse specific month (average temperature & hottest days)|
 
 Entering nothing but the `wetter` command will return the latest measurement
 of the location similar to `wetter latest`.
@@ -61,35 +62,39 @@
     docker run -it ucyo/wetter:latest bash  # ucyo/wetter:testing for pre-releases
     ```
 
 Checking if everything is working appropriately can be done using `wetter latest`. It should return something like the following:
 
 ```bash
 > wetter latest
-Currently it is 🌡️ 12.7°C and windspeed 🌬️ 13.0 km/h.
+Currently it is 🌡️ 12.7°C and wind speed 🌬️ 13.0 km/h.
 Latest measurement on 📅 2023-01-01 @ 01:00AM.
 ```
 
 Now that we know everything is working as expected. Go ahead and update the database by executing `wetter update`.
 
 > Your mileage might vary on getting the exact same output. The timestamp of the above command adjusts to the local time zone and might be different on yours.
 
 ## Configuration
 
-I don't know why, but you might be interested in measurements from a different location. You can do this by adjusting the `wetter.toml` file. The location of the `wetter.toml` depends on your operating system. Additionally, you can find the locations of the measurement data itself i.e. `wetter.json`.
+I don't know why, but you might be interested in measurements from a different location. You can do this by adjusting the `wetter.toml` file. The location of the `wetter.toml` depends on your operating system. Additionally, you can find the locations of the measurement data itself i.e. `wetter.json` and logs i.e. `wetter.log`.
 
 |Location|Operating System|
 |--------|----------------|
 |`/home/<username>/.config/wetter/`|Linux :penguin: (config)|
 |`/home/<username>/.local/share/wetter/`|Linux :penguin: (data)|
+|`/home/<username>/.local/state/wetter/log/wetter.log`|Linux :penguin: (log)|
 |`/Users/<username>/Library/Application Support/wetter/`|macOS :apple: (config & data)|
+|`/Users/<username>/Library/Logs/wetter/`|macOS :apple: (logs)|
 |`C:\Users\<username>\AppData\Local\ucyo\wetter`|Windows :window: (config & data)|
+|`C:\Users\<username>\AppData\Local\ucyo\wetter\logs`|Windows :window: (logs)|
 
 If you have problems finding the proper location there is a gimmick that got you covered.
-The path to the configuration file is returned by `wetter configure --config`. I am using
+The path to the configuration file is returned by `wetter configure --config`.
+The logging level can be set by the `WETTER_LOG` environmental variable.
 
 ### Sample configuration
 
 ```toml
 [location]
 lat = 49
 lon = 8.41
```

### Comparing `wetter-0.3.1/pyproject.toml` & `wetter-0.4.0/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "wetter"
-version = "0.3.1"
+version = "0.4.0"
 description = "CLI tool to parse weather data"
 authors = ["Uğur Çayoğlu <cayoglu@me.com>"]
 license = "MIT"
 readme = "README.md"
 homepage = "https://github.com/ucyo/wetter-py"
 repository = "https://github.com/ucyo/wetter-py"
 documentation = "https://github.com/ucyo/wetter-py"
@@ -19,15 +19,15 @@
     "Programming Language :: Python :: 3.8",
     "Programming Language :: Python :: 3.9",
     "Programming Language :: Python :: 3.10",
     "Programming Language :: Python :: 3.11",
 ]
 
 [tool.poetry.scripts]
-wetter = "wetter.cli:main"
+wetter = "wetter.app:main"
 
 [tool.poetry.dependencies]
 python = "^3.8.1"
 pandas = "^1.5.3"
 requests = "^2.28.2"
 platformdirs = "^3.2.0"
 toml = "^0.10.2"
```

### Comparing `wetter-0.3.1/wetter/__init__.py` & `wetter-0.4.0/wetter/__init__.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,30 +1,34 @@
 """Wetter - a command line tool to gather current weather information.
 
 The goal of the application is to provide an easy command line (CLI) tool
-for getting information about the current weather situation in Karlsruhe.
-It allows for querying for the following data:
+for getting information about the current weather situation in your favourite city.
+It currently has following features:
 
 - Current/latest measurements
 - Measurements from the last week, last month and last year
 - Measurements for a specific month (either of this year if the month already
   passed or of last year)
 
-The library is split to four separate submodules.
+The library is split into two core submodules, one application module and one tools(et) module.
 Each of these submodules are responsible for different aspects of the systems.
-The [config.py](./config.py) is responsible for the configuration of the application.
-It checks for configuration files and if necessary creates them. It also
+
+The [config](./config) module is responsible for the configuration of the application,
+for sane default definitions and the (de)serialisation of the data.
+It checks configuration files and if necessary creates them. It also
 checks for changes in the configurations and if necessary redownloads the data
 from the weather API services of external resources.
-The [conn.py](./conn.py) is responsible for the backend.
-It handles the connection to the database and unifies the input and output.
-The [queries.py](./queries.py) is responsible for querying the
-database returned by [conn.py](./conn.py).
-It handles the proper selection of the data according to the requested time range.
-Finally, the [cli.py](./cli.py) module handles the interface to the user.
+
+The second big submodule is [backend](./backend).
+It handles the connection to external services to download the data,
+the connection to the local storage and the queries executed on it.
+
+The [tools.py](./tools.py) module includes helper tools for different aspects
+of the package e.g. logging. Finally, the [app.py](./app.py)
+module handles the interface to the user.
 It is responsible for parsing the user input and calling the backend.
 It additionally handles the formating of the results for a nice view by the user.
 """
 
 
 def get_version():
     """Return current version of library.
```

### Comparing `wetter-0.3.1/wetter/cli.py` & `wetter-0.4.0/wetter/app.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,85 +1,106 @@
 """Command line tool for accessing the wetter library.
 
 Setup of the command line tool (CLI) for the library.
 The user should be able to handle all necessary communication with
 the backend using this interface incl. updating of the database.
 """
-
 import argparse
+import logging
+from datetime import datetime as dt
+from datetime import timedelta
+
+from wetter import __version__
+from wetter.backend import queries as qu
+from wetter.backend.extern import OpenMeteoArchiveMeasurements
+from wetter.config import config
+from wetter.config.defaults import WETTER_LOG_VARIABLE
+from wetter.tools import get_env_logging, logio
+from wetter.tools import now as local_now
+from wetter.tools import setup_logging, utcnow
 
-from wetter import config, conn
-from wetter import queries as qu
-
-from . import __version__
+setup_logging(get_env_logging(WETTER_LOG_VARIABLE))
+log = logging.getLogger(__name__)
 
 
 def main():
     """Parse user query and and pretty print answer from the database."""
+    log.info("Starting main application")
     args = parse_args()
     current_config = config.Configuration()
     db = current_config.get_store()
-    now = conn.now()
+    now = local_now()
     latest = qu.latest_datapoint(db.df, now)
 
     if args.cmd == "update":
+        if args.historical:
+            now = utcnow()
+            start = dt(year=now.year - 1, month=1, day=1, tzinfo=now.tzinfo)
+            end = now - timedelta(days=30)
+            db.update(start=start, end=end, api=OpenMeteoArchiveMeasurements)
+        log.info("Update requested")
         db.update()
         config.to_store(db)
-        print("Update successful!")
     elif args.cmd == "compare":
+        log.info("Comparison requested")
         if args.week:
             average = qu.last_week(db.df, now)
             pretty_print_comparison(latest=latest, average=average, mode="week")
         if args.month:
             average = qu.last_month(db.df, now)
             pretty_print_comparison(latest=latest, average=average, mode="month")
         if args.year:
             average = qu.last_year(db.df, now)
             pretty_print_comparison(latest=latest, average=average, mode="year")
         if args.detailed:
             average = qu.specific_month(df=db.df, date=now, month=args.detailed)
             pretty_print_detailed_comparison(average)
     elif args.cmd == "latest":
+        log.info("Latest measurement requested")
         pretty_print_latest(latest)
     elif args.cmd == "configure":
+        log.info("Configuration information requested")
         if args.systemd:
             current_config._print_systemd_service()
         elif args.systemdtimer:
             current_config._print_systemd_timer()
         elif args.config:
             print("Configuration path:", current_config.config_path)
     else:
-        raise Exception(f"Can not understand the provided subcommand {args.cmd}")
+        log.err(f"KeyError: Can not understand the provided subcommand {args.cmd}", exc_info=True)
 
 
+@logio(log)
 def get_parser():
     """Define argument parser for CLI tool."""
     parser = argparse.ArgumentParser(
         prog="wetter",
         description="Cli tool to check the outside when you're inside",
         epilog="Have a nice day!",
     )
     parser.add_argument("-v", "--version", action="version", version=__version__)
     subparsers = parser.add_subparsers(help="Subcommands for updates and details", dest="cmd")
     subparsers.add_parser("latest", help="Latest measurment [default]")
-    subparsers.add_parser("update", help="Update DB")
+    yearcomb = subparsers.add_parser("update", help="Update DB")
+    yearcomb.add_argument("--historical", action="store_true", help="Update with historical data")
     comparison_parser = subparsers.add_parser("compare", help="Compare w/ last week, month, year")
     group = comparison_parser.add_mutually_exclusive_group(required=True)
     group.add_argument("--last-week", action="store_true", dest="week", help="Compare w/ last week")
     group.add_argument("--last-year", action="store_true", dest="year", help="Compare w/ last year")
     group.add_argument("--last-month", action="store_true", dest="month", help="Compare w/ last month")
     group.add_argument("--month", type=int, choices=range(1, 13), dest="detailed", help="Month")
     confparser = subparsers.add_parser("configure", help="Configuration of the tool")
     gconf = confparser.add_mutually_exclusive_group(required=True)
     gconf.add_argument("--systemd", action="store_true", help="Show systemd profile")
     gconf.add_argument("--systemdtimer", action="store_true", help="Show systemd timer profile")
     gconf.add_argument("--config", action="store_true", help="Show configuration path")
     return parser
 
 
+@logio(log)
 def parse_args(args=None):
     """Parse arguments from the command line.
 
     This is a wrapper around the `argparse` argument parser.
     It is necessary since `argparse` does not allow to setup a default subcommand.
     Should the subcommand be empty, this function will fill in the `latest` subcommand.
 
@@ -91,100 +112,139 @@
     parser = get_parser()
     if args is None:
         args = parser.parse_args()
     else:
         args = parser.parse_args(args)
     if args.cmd is None:
         args.cmd = "latest"
+        log.info(f"No subcommand given, setting to {args.cmd}")
     return args
 
 
 def pretty_print_latest(latest):
     """Pretty print the output of the latest measurement.
 
     :params latest: Latest measurement from database
     :type latest: pd.DataFrame
+    :raises: IndexError
     """
-    t_now = latest.temperature[0]
-    w_now = latest.wind[0]
-    msg = f"Currently it is 🌡️ {t_now:.1f}°C and windspeed 🌬️ {w_now:.1f} km/h."
-    print(msg)
-    print_disclaimer_latest(latest)
+    try:
+        t_now = latest.temperature[0]
+        w_now = latest.wind[0]
+    except IndexError as err:
+        log.error(f"IndexError: {err}", exc_info=True)
+        print("Unfortunately there are not enough data points.")
+        print("Please consider updating the database: 'wetter update'")
+    else:
+        msg = f"Currently it is 🌡️ {t_now:.1f}°C and wind speed 🌬️ {w_now:.1f} km/h."
+        print(msg)
+        log.info(msg)
+        print_disclaimer_latest(latest)
 
 
-def pretty_print_comparison(latest, average, mode):
+def pretty_print_comparison(latest, average, mode, variable="temperature"):
     """Pretty print the output of a comparison query.
 
     :params latest: Latest measurement from database
     :type latest: pd.DataFrame
     :params average: Average measurements of a certain time window
     :type average: pd.DataFrame
     :params mode: Window definition either 'week','month' or 'year'
     :type mode: str
+    :raises: AssertionError, IndexError
     """
     mode = mode.lower()
-    assert mode in ("week", "year", "month")
-    variable = "temperature"
+    assert mode in ("week", "year", "month"), f"Mode {mode} is unknown."
 
-    temp_avg = average[variable][0]
-    temp_now = latest[variable][0]
-    diff = temp_avg - temp_now
-    relation = "colder" if diff < 0 else "warmer"
-    relation = "same" if diff == 0 else relation
+    try:
+        temp_avg = average[variable][0]
+        temp_now = latest[variable][0]
+    except IndexError as err:
+        log.error(f"IndexError: {err}", exc_info=True)
+        print("Unfortunately there are not enough data points.")
+        add = "--historical" if mode == "year" else ""
+        print(f"Please consider updating the database: `wetter update {add}`")
+    else:
+        diff = temp_avg - temp_now
+        relation = "colder" if diff < 0 else "warmer"
+        relation = "same" if diff == 0 else relation
 
-    msg = f"It was on average {diff:.1f}°C {relation} last {mode} ({temp_avg:.1f}°C) then today ({temp_now:.1f}°C)"
-    print(msg)
-    # print_disclaimer_window(average)
+        msg = f"It was on average {diff:.1f}°C {relation} last {mode} ({temp_avg:.1f}°C) then today ({temp_now:.1f}°C)"
+        print(msg)
+        log.info(msg)
+        print_disclaimer_window(average)
 
 
-def pretty_print_detailed_comparison(window):
+def pretty_print_detailed_comparison(window, variable="temperature"):
     """Pretty print the output of a detailed month window comparison.
 
     :params window: Measurement within a certain month
     :type latest: pd.DataFrame
+    :raises: AssertionError, IndexError, KeyError
     """
-    window.index = window.index.map(lambda x: x.astimezone(conn.now().tzinfo))
-    variable = "temperature"
-    overall_average = window.mean()[variable]
-    daily_average = {data.index[0]: data.mean()[variable] for (day, data) in window.groupby(window.index.day)}
-    hotter_days = {k: v for k, v in daily_average.items() if v > overall_average}
-
-    month = window.index[0].strftime("%B %Y")
-    msg = f"It was on average 🌡️ {overall_average:.1f}°C in 📅 {month}."
-    print(msg)
-    print(f"The following {len(hotter_days)} days were hotter 🔥 than the average:")
-    for day, temp in hotter_days.items():
-        day_str = day.strftime("%Y-%m-%d")
-        print(f"{day_str} @ {temp:.1f}°C")
-    # print_disclaimer_window(window)
+    try:
+        assert window.index.size != 0, "Window length must be > 0."
+    except AssertionError as err:
+        log.error(f"AssertionError: {err}", exc_info=True)
+        print("Unfortunately there are not enough data points.")
+        print("Please consider updating the database: `wetter update`")
+    else:
+        window.index = window.index.map(lambda x: x.astimezone(local_now().tzinfo))
+        overall_average = window.mean()[variable]
+        daily_average = {data.index[0]: data.mean()[variable] for (day, data) in window.groupby(window.index.day)}
+        hotter_days = {k: v for k, v in daily_average.items() if v > overall_average}
+        month = window.index[0].strftime("%B %Y")
+        msg = f"It was on average 🌡️ {overall_average:.1f}°C in 📅 {month}."
+        print(msg)
+        log.info(msg)
+        print(f"The following {len(hotter_days)} days were hotter 🔥 than the average:")
+        for day, temp in hotter_days.items():
+            day_str = day.strftime("%Y-%m-%d")
+            print(f"{day_str} @ {temp:.1f}°C")
+        log.info(f"Hotter days are: {hotter_days}")
 
 
 def print_disclaimer_latest(latest):
     """Disclaimer about the data the calculations are based upon.
 
     :params latest: Latest measurement from database
     :type latest: pd.DataFrame
+    :raises: AssertionError
     """
-    latest.index = latest.index.map(lambda x: x.astimezone(conn.now().tzinfo))
-    date = latest.index[0].strftime("%Y-%m-%d")
-    time = latest.index[0].strftime("%I:%M%p")
-    disclaimer = f"Latest measurement on 📅 {date} @ {time}."
-    print(disclaimer)
+    try:
+        assert latest.index.size > 0, "There are no measurements in the database."
+    except AssertionError as err:
+        log.error(f"AssertionError: {err}", exc_info=True)
+        print("Unfortunately there are not enough data points.")
+        print("Please consider updating the database: `wetter update`")
+    else:
+        latest.index = latest.index.map(lambda x: x.astimezone(local_now().tzinfo))
+        date = latest.index[0].strftime("%Y-%m-%d")
+        time = latest.index[0].strftime("%I:%M%p")
+        disclaimer = f"Latest measurement on 📅 {date} @ {time}."
+        print(disclaimer)
 
 
 def print_disclaimer_window(window):
     """Disclaimer about the data the calculations are based upon.
 
     :params window: Measurement within a certain month
     :type latest: pd.DataFrame
     """
-    window.index = window.index.map(lambda x: x.astimezone(conn.now().tzinfo))
     num = window.index.size
-    start = window.index.min().strftime("%Y-%m-%d")
-    end = window.index.max().strftime("%Y-%m-%d")
+    try:
+        assert num > 0, "Window is not allowed to be empty."
+    except AssertionError as err:
+        log.error(f"AssertionError: {err}", exc_info=True)
+        print("Unfortunately there are not enough data points.")
+        print("Please consider updating the database: `wetter update`")
+    else:
+        window.index = window.index.map(lambda x: x.astimezone(local_now().tzinfo))
+        start = window.index.min().strftime("%Y-%m-%d")
+        end = window.index.max().strftime("%Y-%m-%d")
 
-    disclaimer = f"Average was calculated using #{num} measurements between 📅 {start} - {end}."
-    print(disclaimer)
+        disclaimer = f"Average was calculated using #{num} measurements between 📅 {start} - {end}."
+        print(disclaimer)
 
 
 if __name__ == "__main__":
     main()
```

### Comparing `wetter-0.3.1/wetter/queries.py` & `wetter-0.4.0/wetter/backend/queries.py`

 * *Files 6% similar despite different names*

```diff
@@ -2,132 +2,159 @@
 
 These functions are executing different queries on measurement datasets.
 Most of them share the same parameter space with `df` for the DataFrame used
 as `pandas` and a `date` object used for context. Some functions might define
 additional parameters for context. All of these functions share the same
 output type. This allows the chaining of queries.
 """
+import logging
 from datetime import datetime as dt
 from datetime import timedelta
 
+from wetter.tools import logio
 
+log = logging.getLogger(__name__)
+
+
+@logio(log)
 def latest_datapoint(df, date):
     """Retrieve the latest measurement not exceding a certain date.
 
     This function returns the latest measurement, which is still
     before a certain date. It will return a DataFrame which consists of
     a single row. This way it is easier
 
     :param df: Database with all measurements
     :type df: pandas.DataFrame
     :param date: Upper limit for search of latest measurement
     :type date: datetime.datetime w/ time zone information
     :return: The latest measurement
     :rtype: pandas.DataFrame
+    :raises: AssertionError
     """
     assert date.tzinfo is not None
     df = df[df.index < date]
     result = df[df.index == df.index.max()]
     return result
 
 
+@logio(log)
 def last_week(df, date):
     """Retrieve all measurements within a week before a certain date (excluding).
 
     Returns the measurements of one week earlier than a specific date.
     The date is not included in the query.
 
     :param df: Database with all measurements
     :type df: pandas.DataFrame
     :param date: Upper limit for search of latest measurement
     :type date: datetime.datetime w/ time zone information
     :return: The latest measurement
     :rtype: pandas.DataFrame
+    :raises: AssertionError
     """
     assert date.tzinfo is not None
     threshold = date - timedelta(days=7)
     result = _windowed_selection(df, threshold, date)
     return result
 
 
+@logio(log)
 def last_month(df, date):
     """Retrieve all measurements of last month.
 
     :param df: Database with all measurements
     :type df: pandas.DataFrame
     :param date: Date used as context to define last month
     :type date: datetime.datetime w/ time zone information
     :return: The latest measurement
     :rtype: pandas.DataFrame
+    :raises: AssertionError
     """
     assert date.tzinfo is not None
     if date.month != 1:
         year, month = (date.year, date.month - 1)
     else:
         year, month = (date.year - 1, 12)
     start = dt(year=year, month=month, day=1, tzinfo=date.tzinfo)
-    days_of_month = 33 - (start + timedelta(days=33)).day
+    days_of_month = _calc_days_of_month(start)
     end = start.replace(month=start.month, day=days_of_month, hour=23, minute=59, second=59)
     result = _windowed_selection(df, start, end)
     return result
 
 
 # Pandas allows for easy selection of month/year by using
 # the following syntax: `result = df[df.index.year == date.year - 1]`
 # It is very short and nice looking. But(!) it does not consider
 # time zone. The following implementation actually considers
 # timezones and selects data accordingly.
+@logio(log)
 def last_year(df, date):
     """Retrieve all measurements of last year.
 
     :param df: Database with all measurements
     :type df: pandas.DataFrame
     :param date: Date used as context to define last year
     :type date: datetime.datetime w/ time zone information
     :return: The latest measurement
     :rtype: pandas.DataFrame
+    :raises: AssertionError
     """
     assert date.tzinfo is not None
     start = dt(year=date.year - 1, month=1, day=1, tzinfo=date.tzinfo)
-    end = start.replace(year=start.year + 1) - timedelta(seconds=1)
+    end = start.replace(year=date.year) - timedelta(seconds=1)
     result = _windowed_selection(df, start, end)
     return result
 
 
+@logio(log)
 def specific_month(df, date, month):
     """Retrieve all measurements of a specific month.
 
     The month will be calculated relative to the given date. Is the month
     higher than the one defined in the date element, than the measurements
     from last year will be returned. If the month already occurred this year,
     then the data from the current year is returned.
 
     :param df: Database with all measurements
     :type df: pandas.DataFrame
     :param date: Date used as context to define if month already past this year
     :type date: datetime.datetime w/ time zone information
     :return: The latest measurement
     :rtype: pandas.DataFrame
+    :raises: AssertionError
     """
     assert date.tzinfo is not None
     year = date.year if date.month > month else date.year - 1
     start = dt(year=year, month=month, day=1, tzinfo=date.tzinfo)
-    days_of_month = 33 - (start + timedelta(days=33)).day
+    days_of_month = _calc_days_of_month(start)
     end = start.replace(month=start.month, day=days_of_month, hour=23, minute=59, second=59)
     result = _windowed_selection(df, start, end)
     return result
 
 
+@logio(log)
 def _windowed_selection(df, start, end):
     """Select a time period in database considering time zones.
 
     This function takes the timezone into consideration when selecting data.
     Both borders are included in the data selection.
 
     :param df: Database with all measurements
     :type df: pandas.DataFrame
     :param start: Start date of time period
     :type start: datetime.datetime w/ time zone information
     :param end: End date of time period
     :type end: datetime.datetime w/ time zone information
     """
     return df[(df.index <= end) & (df.index >= start)]
+
+
+@logio(log)
+def _calc_days_of_month(date):
+    """Calculate the day of the month for a specific date.
+
+    :param date: Context date
+    :type date: datetime.Datetime
+    """
+    date = date.replace(day=1)
+    return 37 - (date + timedelta(days=36)).day
```

### Comparing `wetter-0.3.1/PKG-INFO` & `wetter-0.4.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wetter
-Version: 0.3.1
+Version: 0.4.0
 Summary: CLI tool to parse weather data
 Home-page: https://github.com/ucyo/wetter-py
 License: MIT
 Author: Uğur Çayoğlu
 Author-email: cayoglu@me.com
 Requires-Python: >=3.8.1,<4.0.0
 Classifier: Development Status :: 3 - Alpha
@@ -30,15 +30,15 @@
 Requires-Dist: toml (>=0.10.2,<0.11.0)
 Project-URL: Documentation, https://github.com/ucyo/wetter-py
 Project-URL: Repository, https://github.com/ucyo/wetter-py
 Description-Content-Type: text/markdown
 
 <h1 align="center">wetter</h1>
 <p align=center>
-  <img src="https://raw.githubusercontent.com/ucyo/wetter-py/master/assets/undraw_weather.svg" width=300px/>
+  <img src="https://raw.githubusercontent.com/ucyo/wetter-py/master/assets/undraw_weather.svg" width=500px/>
 </p>
 <p align=center>
 <img alt="PyPI" src="https://img.shields.io/pypi/v/wetter?color=blue">
 <img alt="PyPI - License" src="https://img.shields.io/pypi/l/wetter">
 <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/wetter">
 <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/wetter">
 <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/wetter">
@@ -53,14 +53,15 @@
 
 The tool provides the `wetter` command line tool with several subcommands:
 
 |command|Description|
 |-------|-----------|
 |`wetter latest`| Return latest measurement for your favourite city|
 |`wetter update`|Update datastore with latest measurements|
+|`wetter update --historical`|Update datastore with measurements from last year|
 |`wetter compare --last-week`| Compare current weather w/ last week |
 |`wetter compare --last-month`| Compare current weather w/ last month |
 |`wetter compare --last-year`| Compare current weather w/ last year |
 |`wetter compare --month`| Analyse specific month (average temperature & hottest days)|
 
 Entering nothing but the `wetter` command will return the latest measurement
 of the location similar to `wetter latest`.
@@ -95,35 +96,39 @@
     docker run -it ucyo/wetter:latest bash  # ucyo/wetter:testing for pre-releases
     ```
 
 Checking if everything is working appropriately can be done using `wetter latest`. It should return something like the following:
 
 ```bash
 > wetter latest
-Currently it is 🌡️ 12.7°C and windspeed 🌬️ 13.0 km/h.
+Currently it is 🌡️ 12.7°C and wind speed 🌬️ 13.0 km/h.
 Latest measurement on 📅 2023-01-01 @ 01:00AM.
 ```
 
 Now that we know everything is working as expected. Go ahead and update the database by executing `wetter update`.
 
 > Your mileage might vary on getting the exact same output. The timestamp of the above command adjusts to the local time zone and might be different on yours.
 
 ## Configuration
 
-I don't know why, but you might be interested in measurements from a different location. You can do this by adjusting the `wetter.toml` file. The location of the `wetter.toml` depends on your operating system. Additionally, you can find the locations of the measurement data itself i.e. `wetter.json`.
+I don't know why, but you might be interested in measurements from a different location. You can do this by adjusting the `wetter.toml` file. The location of the `wetter.toml` depends on your operating system. Additionally, you can find the locations of the measurement data itself i.e. `wetter.json` and logs i.e. `wetter.log`.
 
 |Location|Operating System|
 |--------|----------------|
 |`/home/<username>/.config/wetter/`|Linux :penguin: (config)|
 |`/home/<username>/.local/share/wetter/`|Linux :penguin: (data)|
+|`/home/<username>/.local/state/wetter/log/wetter.log`|Linux :penguin: (log)|
 |`/Users/<username>/Library/Application Support/wetter/`|macOS :apple: (config & data)|
+|`/Users/<username>/Library/Logs/wetter/`|macOS :apple: (logs)|
 |`C:\Users\<username>\AppData\Local\ucyo\wetter`|Windows :window: (config & data)|
+|`C:\Users\<username>\AppData\Local\ucyo\wetter\logs`|Windows :window: (logs)|
 
 If you have problems finding the proper location there is a gimmick that got you covered.
-The path to the configuration file is returned by `wetter configure --config`. I am using
+The path to the configuration file is returned by `wetter configure --config`.
+The logging level can be set by the `WETTER_LOG` environmental variable.
 
 ### Sample configuration
 
 ```toml
 [location]
 lat = 49
 lon = 8.41
```

