# Comparing `tmp/ds_caselaw_utils-0.4.4.tar.gz` & `tmp/ds_caselaw_utils-0.4.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ds_caselaw_utils-0.4.4.tar", max compression
+gzip compressed data, was "ds_caselaw_utils-0.4.5.tar", max compression
```

## Comparing `ds_caselaw_utils-0.4.4.tar` & `ds_caselaw_utils-0.4.5.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0     1108 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/LICENSE.md
--rw-r--r--   0        0        0     4106 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/README.md
--rw-r--r--   0        0        0      617 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/pyproject.toml
--rw-r--r--   0        0        0       12 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/.gitignore
--rw-r--r--   0        0        0       75 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/__init__.py
--rw-r--r--   0        0        0     2604 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/courts.py
--rw-r--r--   0        0        0      709 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/data/README.md
--rw-r--r--   0        0        0    12788 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/data/court_names.yaml
--rw-r--r--   0        0        0      615 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/data/neutral_citation_regex.yaml
--rw-r--r--   0        0        0      656 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/neutral.py
--rw-r--r--   0        0        0     5496 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/test_courts.py
--rw-r--r--   0        0        0     1395 2023-01-03 14:28:18.790703 ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/test_neutral.py
--rw-r--r--   0        0        0     5022 2023-01-03 14:28:28.055227 ds_caselaw_utils-0.4.4/setup.py
--rw-r--r--   0        0        0     4705 2023-01-03 14:28:28.055812 ds_caselaw_utils-0.4.4/PKG-INFO
+-rw-r--r--   0        0        0     1108 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/LICENSE.md
+-rw-r--r--   0        0        0     4132 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/README.md
+-rw-r--r--   0        0        0      617 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/pyproject.toml
+-rw-r--r--   0        0        0       12 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/.gitignore
+-rw-r--r--   0        0        0       75 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/__init__.py
+-rw-r--r--   0        0        0     2604 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/courts.py
+-rw-r--r--   0        0        0      709 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/data/README.md
+-rw-r--r--   0        0        0    12780 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/data/court_names.yaml
+-rw-r--r--   0        0        0      615 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/data/neutral_citation_regex.yaml
+-rw-r--r--   0        0        0      656 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/neutral.py
+-rw-r--r--   0        0        0     5494 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/test_courts.py
+-rw-r--r--   0        0        0     1395 2023-04-06 11:20:23.755903 ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/test_neutral.py
+-rw-r--r--   0        0        0     5048 2023-04-06 11:20:33.980973 ds_caselaw_utils-0.4.5/setup.py
+-rw-r--r--   0        0        0     4731 2023-04-06 11:20:33.981520 ds_caselaw_utils-0.4.5/PKG-INFO
```

### Comparing `ds_caselaw_utils-0.4.4/LICENSE.md` & `ds_caselaw_utils-0.4.5/LICENSE.md`

 * *Files identical despite different names*

### Comparing `ds_caselaw_utils-0.4.4/README.md` & `ds_caselaw_utils-0.4.5/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -95,14 +95,14 @@
 The package will **only** be released to PyPI if the branch is tagged. A merge
 to main alone will **not** trigger a release to PyPI.
 
 To create a release:
 
 0. Update the version number in `pyproject.toml`
 1. Create a branch `release/v{major}.{minor}.{patch}`
-2. Update changelog for the release
+2. Update `CHANGELOG.md` and `pyproject.toml` for the release
 3. Commit and push
 4. Open a PR from that branch to main
 5. Get approval on the PR
 6. Tag the HEAD of the PR `v{major}.{minor}.{patch}` and push the tag
 7. Merge the PR to main and push
 8. Add a new release to Github for that tag for consistency's sake
```

### Comparing `ds_caselaw_utils-0.4.4/pyproject.toml` & `ds_caselaw_utils-0.4.5/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "ds_caselaw_utils"
-version = "0.4.4"
+version = "0.4.5"
 description = "Utilities for the National Archives Caselaw project"
 authors = ["Nick Jackson <nick@dxw.com>", "David McKee <dragon@dxw.com>", "Tim Cowlishaw <tim@timcowlishaw.co.uk>", "Laura Porter <laura@dxw.com>"]
 license = "MIT"
 homepage = "https://github.com/nationalarchives/ds-caselaw-utils"
 keywords = ["national archives", "caselaw"]
 readme = "README.md"
```

### Comparing `ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/courts.py` & `ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/courts.py`

 * *Files identical despite different names*

### Comparing `ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/data/README.md` & `ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/data/README.md`

 * *Files identical despite different names*

### Comparing `ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/data/court_names.yaml` & `ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/data/court_names.yaml`

 * *Files 0% similar despite different names*

```diff
@@ -4,55 +4,55 @@
   courts:
     -
         code: UKSC
         name: United Kingdom Supreme Court
         link: https://www.supremecourt.uk/
         ncn: \[(\d{4})\] (UKSC) (\d+)
         param: 'uksc'
-        start_year: '2014'
+        start_year: 2014
         end_year: 2022
         selectable: true
         listable: true
 - name: privy_council
   display_name: ~
   is_tribunal: false
   courts:
     -
         code: UKPC
         name: Privy Council
         link: https://www.jcpc.uk/
         ncn: \[(\d{4})\] (UKPC) \d+
         param: 'ukpc'
-        start_year: '2014'
+        start_year: 2014
         end_year: 2022
         selectable: true
         listable: true
 - name: court_of_appeal
   display_name: "Court of Appeal"
   is_tribunal: false
   courts:
     -
         code: EWCA-Civil
         name: Court of Appeal Civil Division
         list_name: "Court of Appeal (Civil Division)"
         link: https://www.gov.uk/courts-tribunals/court-of-appeal-civil-division
         ncn: \[(\d{4})\] (EWCA) (Civ) (\d+)
         param: 'ewca/civ'
-        start_year: '2003'
+        start_year: 2003
         end_year: 2022
         selectable: true
         listable: true
     -
         code: EWCA-Criminal
         name: Court of Appeal Criminal Division
         list_name: Court of Appeal (Criminal Division)
         link: https://www.gov.uk/courts-tribunals/court-of-appeal-criminal-division
         ncn: \[(\d{4})\] (EWCA) (Crim) (\d+)
         param: 'ewca/crim'
-        start_year: '2003'
+        start_year: 2003
         end_year: 2022
         selectable: true
         listable: true
 - name: high_court
   display_name: "High Court"
   is_tribunal: false
   courts:
```

### Comparing `ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/data/neutral_citation_regex.yaml` & `ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/data/neutral_citation_regex.yaml`

 * *Files identical despite different names*

### Comparing `ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/neutral.py` & `ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/neutral.py`

 * *Files identical despite different names*

### Comparing `ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/test_courts.py` & `ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/test_courts.py`

 * *Files 1% similar despite different names*

```diff
@@ -150,9 +150,9 @@
         datafile = pathlib.Path(__file__).parent / "data/court_names.yaml"
         with open(datafile) as f:
             court_data = yaml.load(f)
         courts_from_yaml = []
         for group in court_data:
             for court in group.get("courts"):
                 courts_from_yaml.append(court)
-        for (court, data) in zip(courts.get_all(), courts_from_yaml):
+        for court, data in zip(courts.get_all(), courts_from_yaml):
             self.assertEqual(court.name, data["name"])
```

### Comparing `ds_caselaw_utils-0.4.4/src/ds_caselaw_utils/test_neutral.py` & `ds_caselaw_utils-0.4.5/src/ds_caselaw_utils/test_neutral.py`

 * *Files identical despite different names*

### Comparing `ds_caselaw_utils-0.4.4/setup.py` & `ds_caselaw_utils-0.4.5/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,17 +11,17 @@
 {'': ['*'], 'ds_caselaw_utils': ['data/*']}
 
 install_requires = \
 ['ruamel.yaml>=0.17.21,<0.18.0']
 
 setup_kwargs = {
     'name': 'ds-caselaw-utils',
-    'version': '0.4.4',
+    'version': '0.4.5',
     'description': 'Utilities for the National Archives Caselaw project',
-    'long_description': '# The National Archives: Find Case Law\n\nThis repository is part of the [Find Case Law](https://caselaw.nationalarchives.gov.uk/) project at [The National Archives](https://www.nationalarchives.gov.uk/). For more information on the project, check [the documentation](https://github.com/nationalarchives/ds-find-caselaw-docs).\n\n# Python Utilities\n\n![PyPI](https://img.shields.io/pypi/v/ds-caselaw-utils) ![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/ds-caselaw-utils)\n\nThis repository contains common functions used throughout the National Archives Caselaw project, reducing duplication and complexity.\n\npypi name: [ds-caselaw-utils](https://pypi.org/project/ds-caselaw-utils)\npython import name: `ds_caselaw_utils`\n\n## Examples\n\n```\nfrom ds_caselaw_utils import neutral_url\nneutral_url("[2022] EAT 1")  # \'/eat/2022/4\'\n\nfrom ds_caselaw_utils import courts\n\ncourts.get_all() # return a list of all courts\n\ncourts.get_by_param("ewhc/ch") # get a court by its parameter value\n\ncourts.get_selectable() # returns a list of all courts that are whitelisted to\n                        # appear as searchable options\n\ncourts.get_listable_groups() # returns a grouped list of courts that are whitelisted to\n                             # be listed publicly\n\ncourts.get_listable_courts() # returns a list of all *courts* (ie not tribunals)\n                             # which are whitelisted to be listed publicly\n\ncourts.get_listable_tribunals() # return a list of all *tribunals*  which are\n                                # whitelisted to be listed publicly\n\n\n```\n\nThe list of courts is defined in `src/ds_caselaw_utils/data/court_names.yml`. The format is as follows:\n\n```\n- name: high_court # Internal name of a group of courts to be displayed together\n  display_name: "High Court" # An optional public facing name for this group.\n  is_tribunal: false # Whether this group contains courts or tribunals\n  courts: # List of courts to be displayed under this group\n    -\n        # An internal code for this court:\n        code: EWHC-SeniorCourtsCosts\n         # The public facing name of the court:\n        name: Senior Courts Costs Office\n        # An alternative wording for use in listings (optional, defaults to `name`)\n        list_name: High Court (Senior Court Costs Office)\n        # A URL to link to for more information on this court:\n        link: https://www.gov.uk/courts-tribunals/senior-courts-costs-office\n        # A regex matching neutral citations for this court\'s judgments:\n        ncn: \\[(\\d{4})\\] (EWHC) (\\d+) \\((SCCO)\\)\n        # The canonical parameter value used in searches for this court:\n        param: \'ewhc/scco\'\n        # Any additional parameter aliases which display judgments from this court:\n        extra_params: [\'ewhc/costs\']\n        # The year of the first judgment we have on file for this court:\n        start_year: 2003\n        # The year of the last judgment we have on file for this court\n        # (optional, defaults to current year):\n        end_year: ~\n        # Whether to expose this court publicly as selectable in search filters:\n        selectable: true\n        # Whether to expose this court publicly in listings:\n        listable: true\n```\n\n## Testing\n\n```bash\n$ poetry shell\n$ cd src/ds_caselaw_utils\n$ python -m unittest\n```\n\n## Building\n\n```bash\n$ rm -rf dist\n$ poetry build\n$ python3 -m twine upload --repository testpypi dist/* --verbose\n```\n\n## Releasing\n\nWhen making a new release, update the [changelog](CHANGELOG.md) in the release\npull request.\n\nThe package will **only** be released to PyPI if the branch is tagged. A merge\nto main alone will **not** trigger a release to PyPI.\n\nTo create a release:\n\n0. Update the version number in `pyproject.toml`\n1. Create a branch `release/v{major}.{minor}.{patch}`\n2. Update changelog for the release\n3. Commit and push\n4. Open a PR from that branch to main\n5. Get approval on the PR\n6. Tag the HEAD of the PR `v{major}.{minor}.{patch}` and push the tag\n7. Merge the PR to main and push\n8. Add a new release to Github for that tag for consistency\'s sake\n',
+    'long_description': '# The National Archives: Find Case Law\n\nThis repository is part of the [Find Case Law](https://caselaw.nationalarchives.gov.uk/) project at [The National Archives](https://www.nationalarchives.gov.uk/). For more information on the project, check [the documentation](https://github.com/nationalarchives/ds-find-caselaw-docs).\n\n# Python Utilities\n\n![PyPI](https://img.shields.io/pypi/v/ds-caselaw-utils) ![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/ds-caselaw-utils)\n\nThis repository contains common functions used throughout the National Archives Caselaw project, reducing duplication and complexity.\n\npypi name: [ds-caselaw-utils](https://pypi.org/project/ds-caselaw-utils)\npython import name: `ds_caselaw_utils`\n\n## Examples\n\n```\nfrom ds_caselaw_utils import neutral_url\nneutral_url("[2022] EAT 1")  # \'/eat/2022/4\'\n\nfrom ds_caselaw_utils import courts\n\ncourts.get_all() # return a list of all courts\n\ncourts.get_by_param("ewhc/ch") # get a court by its parameter value\n\ncourts.get_selectable() # returns a list of all courts that are whitelisted to\n                        # appear as searchable options\n\ncourts.get_listable_groups() # returns a grouped list of courts that are whitelisted to\n                             # be listed publicly\n\ncourts.get_listable_courts() # returns a list of all *courts* (ie not tribunals)\n                             # which are whitelisted to be listed publicly\n\ncourts.get_listable_tribunals() # return a list of all *tribunals*  which are\n                                # whitelisted to be listed publicly\n\n\n```\n\nThe list of courts is defined in `src/ds_caselaw_utils/data/court_names.yml`. The format is as follows:\n\n```\n- name: high_court # Internal name of a group of courts to be displayed together\n  display_name: "High Court" # An optional public facing name for this group.\n  is_tribunal: false # Whether this group contains courts or tribunals\n  courts: # List of courts to be displayed under this group\n    -\n        # An internal code for this court:\n        code: EWHC-SeniorCourtsCosts\n         # The public facing name of the court:\n        name: Senior Courts Costs Office\n        # An alternative wording for use in listings (optional, defaults to `name`)\n        list_name: High Court (Senior Court Costs Office)\n        # A URL to link to for more information on this court:\n        link: https://www.gov.uk/courts-tribunals/senior-courts-costs-office\n        # A regex matching neutral citations for this court\'s judgments:\n        ncn: \\[(\\d{4})\\] (EWHC) (\\d+) \\((SCCO)\\)\n        # The canonical parameter value used in searches for this court:\n        param: \'ewhc/scco\'\n        # Any additional parameter aliases which display judgments from this court:\n        extra_params: [\'ewhc/costs\']\n        # The year of the first judgment we have on file for this court:\n        start_year: 2003\n        # The year of the last judgment we have on file for this court\n        # (optional, defaults to current year):\n        end_year: ~\n        # Whether to expose this court publicly as selectable in search filters:\n        selectable: true\n        # Whether to expose this court publicly in listings:\n        listable: true\n```\n\n## Testing\n\n```bash\n$ poetry shell\n$ cd src/ds_caselaw_utils\n$ python -m unittest\n```\n\n## Building\n\n```bash\n$ rm -rf dist\n$ poetry build\n$ python3 -m twine upload --repository testpypi dist/* --verbose\n```\n\n## Releasing\n\nWhen making a new release, update the [changelog](CHANGELOG.md) in the release\npull request.\n\nThe package will **only** be released to PyPI if the branch is tagged. A merge\nto main alone will **not** trigger a release to PyPI.\n\nTo create a release:\n\n0. Update the version number in `pyproject.toml`\n1. Create a branch `release/v{major}.{minor}.{patch}`\n2. Update `CHANGELOG.md` and `pyproject.toml` for the release\n3. Commit and push\n4. Open a PR from that branch to main\n5. Get approval on the PR\n6. Tag the HEAD of the PR `v{major}.{minor}.{patch}` and push the tag\n7. Merge the PR to main and push\n8. Add a new release to Github for that tag for consistency\'s sake\n',
     'author': 'Nick Jackson',
     'author_email': 'nick@dxw.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/nationalarchives/ds-caselaw-utils',
     'package_dir': package_dir,
     'packages': packages,
```

### Comparing `ds_caselaw_utils-0.4.4/PKG-INFO` & `ds_caselaw_utils-0.4.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ds-caselaw-utils
-Version: 0.4.4
+Version: 0.4.5
 Summary: Utilities for the National Archives Caselaw project
 Home-page: https://github.com/nationalarchives/ds-caselaw-utils
 License: MIT
 Keywords: national archives,caselaw
 Author: Nick Jackson
 Author-email: nick@dxw.com
 Requires-Python: >=3.9,<4.0
@@ -112,15 +112,15 @@
 The package will **only** be released to PyPI if the branch is tagged. A merge
 to main alone will **not** trigger a release to PyPI.
 
 To create a release:
 
 0. Update the version number in `pyproject.toml`
 1. Create a branch `release/v{major}.{minor}.{patch}`
-2. Update changelog for the release
+2. Update `CHANGELOG.md` and `pyproject.toml` for the release
 3. Commit and push
 4. Open a PR from that branch to main
 5. Get approval on the PR
 6. Tag the HEAD of the PR `v{major}.{minor}.{patch}` and push the tag
 7. Merge the PR to main and push
 8. Add a new release to Github for that tag for consistency's sake
```

