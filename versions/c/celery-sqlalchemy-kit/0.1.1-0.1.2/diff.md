# Comparing `tmp/celery_sqlalchemy_kit-0.1.1.tar.gz` & `tmp/celery_sqlalchemy_kit-0.1.2.tar.gz`

## Comparing `celery_sqlalchemy_kit-0.1.1.tar` & `celery_sqlalchemy_kit-0.1.2.tar`

### file list

```diff
@@ -1,32 +1,26 @@
--rw-r--r--   0        0        0     1369 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/docker-compose.yml
--rw-r--r--   0        0        0      478 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/__init__.py
--rw-r--r--   0        0        0     3551 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/base_task.py
--rw-r--r--   0        0        0     9954 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/scheduler.py
--rw-r--r--   0        0        0       37 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/.pytest_cache/.gitignore
--rw-r--r--   0        0        0      191 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/.pytest_cache/CACHEDIR.TAG
--rw-r--r--   0        0        0      302 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/.pytest_cache/README.md
--rw-r--r--   0        0        0      129 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/.pytest_cache/v/cache/nodeids
--rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/.pytest_cache/v/cache/stepwise
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/db/__init__.py
--rw-r--r--   0        0        0     3393 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/db/crud.py
--rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/db/model.py
--rw-r--r--   0        0        0      951 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/db/session.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/__init__.py
--rw-r--r--   0        0        0     1764 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/celery_test_instance.py
--rw-r--r--   0        0        0     5049 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/test_celery_scheduler.py
--rw-r--r--   0        0        0      830 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/build/dockerfile
--rw-r--r--   0        0        0       92 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/build/requirements.dev.txt
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/__init__.py
--rw-r--r--   0        0        0     1079 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/prestart.py
--rw-r--r--   0        0        0     2028 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/setup_routines_table.py
--rw-r--r--   0        0        0      128 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/start_celery.sh
--rw-r--r--   0        0        0      153 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/start_celery_beat.sh
--rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/start_tests.sh
--rw-r--r--   0        0        0      363 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/example/.env.example
--rw-r--r--   0        0        0      881 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/example/celery_app.py
--rw-r--r--   0        0        0     1130 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/example/custom_tasks.py
--rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/.gitignore
--rw-r--r--   0        0        0     1083 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/LICENSE
--rw-r--r--   0        0        0     7946 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/README.md
--rw-r--r--   0        0        0     1079 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/pyproject.toml
--rw-r--r--   0        0        0     8923 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0     1304 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/docker-compose.yml
+-rw-r--r--   0        0        0      270 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/__init__.py
+-rw-r--r--   0        0        0     3551 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/base_task.py
+-rw-r--r--   0        0        0     9938 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/scheduler.py
+-rw-r--r--   0        0        0      235 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/db/__init__.py
+-rw-r--r--   0        0        0     3386 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/db/crud.py
+-rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/db/model.py
+-rw-r--r--   0        0        0      951 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/db/session.py
+-rw-r--r--   0        0        0      363 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/example/.env.example
+-rw-r--r--   0        0        0      881 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/example/celery_app.py
+-rw-r--r--   0        0        0     1130 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/example/custom_tasks.py
+-rw-r--r--   0        0        0     1786 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/celery_test_instance.py
+-rw-r--r--   0        0        0     5066 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/test_celery_scheduler.py
+-rw-r--r--   0        0        0      799 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/build/dockerfile
+-rw-r--r--   0        0        0       92 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/build/requirements.dev.txt
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/scripts/__init__.py
+-rw-r--r--   0        0        0     1037 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/scripts/prestart.py
+-rw-r--r--   0        0        0     2075 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/scripts/setup_routines_table.py
+-rw-r--r--   0        0        0      128 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/scripts/start_celery.sh
+-rw-r--r--   0        0        0      165 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/scripts/start_celery_beat.sh
+-rw-r--r--   0        0        0      178 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/tests/scripts/start_tests.sh
+-rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/.gitignore
+-rw-r--r--   0        0        0     1083 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/LICENSE
+-rw-r--r--   0        0        0     7946 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/README.md
+-rw-r--r--   0        0        0     1079 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0     8923 2020-02-02 00:00:00.000000 celery_sqlalchemy_kit-0.1.2/PKG-INFO
```

### Comparing `celery_sqlalchemy_kit-0.1.1/docker-compose.yml` & `celery_sqlalchemy_kit-0.1.2/docker-compose.yml`

 * *Files 10% similar despite different names*

```diff
@@ -25,36 +25,36 @@
     env_file:
       - .env
 
   celery:
     container_name: celery_worker
     image: celery-sqlalchemy-kit:latest
     build:
-      context: celery_sqlalchemy_kit
+      context: .
       dockerfile: ./tests/build/dockerfile
     volumes:
       - ./celery_sqlalchemy_kit/:/celery_sqlalchemy_kit
     env_file:
       - .env
-    command: bash -c "sleep 8 && sh ./tests/scripts/start_celery.sh"
+    command: bash -c "sleep 8 && sh /start_celery.sh"
 
   celery_beat:
     container_name: celery_beat
     image: celery-sqlalchemy-kit:latest
     volumes:
       - ./celery_sqlalchemy_kit/:/celery_sqlalchemy_kit
     env_file:
       - .env
-    command: bash -c "sleep 10 && sh ./tests/scripts/start_celery_beat.sh"
+    command: bash -c "sleep 10 && sh /start_celery_beat.sh"
 
   run_tests:
     container_name: run_tests
     image: celery-sqlalchemy-kit:latest
     volumes:
       - ./celery_sqlalchemy_kit/:/celery_sqlalchemy_kit
     env_file:
       - .env
-    command: sh ./tests/scripts/start_tests.sh
+    command: sh /start_tests.sh
 
 volumes:
     postgres_data:
     postgres_backup:
```

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/base_task.py` & `celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/base_task.py`

 * *Files identical despite different names*

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/scheduler.py` & `celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/scheduler.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,19 +4,19 @@
 from celery import Celery
 from celery.schedules import crontab
 from celery.utils.log import get_logger
 from celery.beat import Scheduler
 
 from sqlalchemy.exc import SQLAlchemyError
 
-from db.model import Routine, Base
 from sqlalchemy.orm import Session
 
-from db.crud import crud
-from db.session import SessionWrapper
+from .db import crud
+from .db import Routine, Base
+from .db import SessionWrapper
 
 DEFAULT_SCHEDULER_SYNC_DB_URI = "postgresql+psycopg2:///schedule.db"
 
 logger = get_logger(__name__)
 
 
 class RoutineScheduler(Scheduler):
```

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/db/crud.py` & `celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/db/crud.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 from typing import List, Dict, Any, Type
 from uuid import UUID, uuid4
 
 from sqlalchemy import select, delete
 from sqlalchemy.orm import Session
 
-from db.model import Routine
+from . import Routine
 
 
 class CRUDRoutine:
     def __init__(self, model: Type[Routine]) -> None:
         """
         CRUD object with default methods to Create, Read, Update, Delete (CRUD).
```

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/db/model.py` & `celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/db/model.py`

 * *Files identical despite different names*

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/db/session.py` & `celery_sqlalchemy_kit-0.1.2/celery_sqlalchemy_kit/db/session.py`

 * *Files identical despite different names*

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/celery_test_instance.py` & `celery_sqlalchemy_kit-0.1.2/tests/celery_test_instance.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import json
 import os
 
 from celery import Celery
-from base_task import AsyncTask
+from celery_sqlalchemy_kit.base_task import AsyncTask
 
 celeryTest = Celery(
     "celeryTest",
     broker=os.getenv("CELERY_BROKER_URL"),
     backend=os.getenv("CELERY_RESULT_BACKEND"),
 )
```

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/test_celery_scheduler.py` & `celery_sqlalchemy_kit-0.1.2/tests/test_celery_scheduler.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import time
 import os
 
 import pytest
 from sqlalchemy.orm import Session
 from sqlalchemy import create_engine
 
-from db.crud import crud
+from celery_sqlalchemy_kit.db import crud
 
 
 @pytest.fixture(scope="function")
 def ac_session() -> Session:
     """An auto-committing session, this means all changes are directly committed to the DB.
     The changes are thus readable by other Connections."""
     engine = create_engine(
@@ -39,15 +39,15 @@
     """
     This tests our RoutineScheduler by using the celery_test_instance in celery_test_instance.py.
     In the first part it is being tested, if the scheduler sets up the routines in the DB correctly. Since this only
     happens on startup, this part of the test only works correctly the first time after starting the scheduler.
     Also, the files 'scripts/prestart.py' and 'tests/setup_routines_table.py' must be executed in advance.
     Before the test is being run again, the scheduler needs to be restarted.
     """
-    time.sleep(5)
+    time.sleep(7)
 
     # this part checks if the schedule is set up correctly (merge db entries and celery routines correctly)
     # and only works when docker when no other tests have been executed yet
 
     # check if routine that is in db but not in code was correctly deleted in db
     routine = crud.find_by_name(db=ac_session, name="test routine")
     assert not routine
```

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/build/dockerfile` & `celery_sqlalchemy_kit-0.1.2/tests/build/dockerfile`

 * *Files 9% similar despite different names*

```diff
@@ -5,25 +5,26 @@
 # install system dependencies
 RUN apt-get update \
   && apt-get -y install netcat gcc libpq-dev build-essential curl \
   && apt-get clean
 
 # install python dependencies
 RUN mkdir -p /celery_sqlalchemy_kit
-WORKDIR /celery_sqlalchemy_kit/
-COPY /tests/build/requirements.dev.txt /celery_sqlalchemy_kit/
+WORKDIR /
+COPY /tests/build/requirements.dev.txt /
 RUN pip install --upgrade pip
 RUN pip install -r requirements.dev.txt
 
 # Copy starting scripts and make them executable
 COPY /tests/scripts/start_celery.sh /start_celery.sh
 RUN chmod +x /start_celery.sh
 
 COPY /tests/scripts/start_celery_beat.sh /start_celery_beat.sh
 RUN chmod +x /start_celery_beat.sh
 
 COPY /tests/scripts/start_tests.sh /start_tests.sh
 RUN chmod +x /start_tests.sh
 
-COPY ../.. /celery_sqlalchemy_kit
+COPY celery_sqlalchemy_kit /celery_sqlalchemy_kit
+COPY tests /tests
 
-ENV PYTHONPATH=/celery_sqlalchemy_kit
+ENV PYTHONPATH=/
```

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/prestart.py` & `celery_sqlalchemy_kit-0.1.2/tests/scripts/prestart.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import logging
 import os
 
 from sqlalchemy import text, create_engine
 from sqlalchemy.orm import sessionmaker, Session
 from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
 
+
 logging.basicConfig(level=logging.INFO)
 logger = logging.getLogger(__name__)
 
 max_tries = 60 * 5  # 5 minutes
 wait_seconds = 1
 
 
@@ -33,12 +34,11 @@
         logger.error(e)
         raise e
 
 
 def main() -> None:
     print("Initializing service (waiting for DB)")
     init()
-    print("Service finished initializing")
 
 
 if __name__ == "__main__":
     main()
```

### Comparing `celery_sqlalchemy_kit-0.1.1/celery_sqlalchemy_kit/tests/scripts/setup_routines_table.py` & `celery_sqlalchemy_kit-0.1.2/tests/scripts/setup_routines_table.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import logging
 import os
 import string
 from random import choices
 
-from db.crud import crud
-from db.model import Base, Routine
-from db.session import SessionWrapper
+from celery_sqlalchemy_kit.db import crud
+from celery_sqlalchemy_kit.db import Base, Routine
+from celery_sqlalchemy_kit.db import SessionWrapper
 
 
 logging.basicConfig(level=logging.DEBUG)
 logger = logging.getLogger(__name__)
 
 
 def setup_db_for_celery_test() -> None:
```

### Comparing `celery_sqlalchemy_kit-0.1.1/example/celery_app.py` & `celery_sqlalchemy_kit-0.1.2/example/celery_app.py`

 * *Files identical despite different names*

### Comparing `celery_sqlalchemy_kit-0.1.1/example/custom_tasks.py` & `celery_sqlalchemy_kit-0.1.2/example/custom_tasks.py`

 * *Files identical despite different names*

### Comparing `celery_sqlalchemy_kit-0.1.1/LICENSE` & `celery_sqlalchemy_kit-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `celery_sqlalchemy_kit-0.1.1/README.md` & `celery_sqlalchemy_kit-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `celery_sqlalchemy_kit-0.1.1/pyproject.toml` & `celery_sqlalchemy_kit-0.1.2/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "celery-sqlalchemy-kit"
-version = "0.1.1"
+version = "0.1.2"
 authors = [
   { name="Amelie Luecke", email="amelie.luecke@cap-on.de" }, { name="Philipp Ratz", email="philipp.ratz@cap-on.de" }
 ]
 description = "Schedule tasks in an SQL Database and define Async Celery Tasks."
 readme = "README.md"
 requires-python = ">=3.10"
 classifiers = [
```

### Comparing `celery_sqlalchemy_kit-0.1.1/PKG-INFO` & `celery_sqlalchemy_kit-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: celery-sqlalchemy-kit
-Version: 0.1.1
+Version: 0.1.2
 Summary: Schedule tasks in an SQL Database and define Async Celery Tasks.
 Project-URL: Homepage, https://github.com/cap-on/celery-sqlalchemy-kit
 Project-URL: Bug Tracker, https://github.com/cap-on/celery-sqlalchemy-kit/issues
 Author-email: Amelie Luecke <amelie.luecke@cap-on.de>, Philipp Ratz <philipp.ratz@cap-on.de>
 License-File: LICENSE
 Classifier: Development Status :: 3 - Alpha
 Classifier: License :: OSI Approved :: MIT License
```

