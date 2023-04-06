# Comparing `tmp/pontos-23.4.0.tar.gz` & `tmp/pontos-23.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pontos-23.4.0.tar", max compression
+gzip compressed data, was "pontos-23.4.1.tar", max compression
```

## Comparing `pontos-23.4.0.tar` & `pontos-23.4.1.tar`

### file list

```diff
@@ -1,246 +1,248 @@
--rw-r--r--   0        0        0    35149 2023-04-05 12:29:11.369273 pontos-23.4.0/LICENSE
--rw-r--r--   0        0        0     3349 2023-04-05 12:29:11.369273 pontos-23.4.0/README.md
--rw-r--r--   0        0        0    97720 2023-04-05 12:29:11.373273 pontos-23.4.0/poetry.lock
--rw-r--r--   0        0        0       32 2023-04-05 12:29:11.373273 pontos-23.4.0/poetry.toml
--rw-r--r--   0        0        0      791 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/__init__.py
--rw-r--r--   0        0        0      968 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/changelog/__init__.py
--rw-r--r--   0        0        0     9455 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/changelog/conventional_commits.py
--rw-r--r--   0        0        0      965 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/changelog/errors.py
--rw-r--r--   0        0        0     4427 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/changelog/main.py
--rw-r--r--   0        0        0      806 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/errors.py
--rw-r--r--   0        0        0      882 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/git/__init__.py
--rw-r--r--   0        0        0    14927 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/git/git.py
--rw-r--r--   0        0        0      760 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/__init__.py
--rw-r--r--   0        0        0     1154 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/__init__.py
--rw-r--r--   0        0        0     2239 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/argparser.py
--rw-r--r--   0        0        0     1472 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/cmds.py
--rw-r--r--   0        0        0     6158 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/core.py
--rw-r--r--   0        0        0     2426 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/env.py
--rw-r--r--   0        0        0      861 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/errors.py
--rw-r--r--   0        0        0     4173 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/event.py
--rw-r--r--   0        0        0     1100 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/actions/main.py
--rw-r--r--   0        0        0     2047 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/__init__.py
--rw-r--r--   0        0        0     5531 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/api.py
--rw-r--r--   0        0        0     6196 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/artifacts.py
--rw-r--r--   0        0        0    34561 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/branch.py
--rw-r--r--   0        0        0     9395 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/client.py
--rw-r--r--   0        0        0     1844 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/contents.py
--rw-r--r--   0        0        0      845 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/errors.py
--rw-r--r--   0        0        0     1320 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/helper.py
--rw-r--r--   0        0        0     2813 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/labels.py
--rw-r--r--   0        0        0    10311 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/organizations.py
--rw-r--r--   0        0        0    10519 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/pull_requests.py
--rw-r--r--   0        0        0    11942 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/release.py
--rw-r--r--   0        0        0    21512 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/repositories.py
--rw-r--r--   0        0        0     3276 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/search.py
--rw-r--r--   0        0        0     5079 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/tags.py
--rw-r--r--   0        0        0    15207 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/teams.py
--rw-r--r--   0        0        0     9182 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/api/workflows.py
--rw-r--r--   0        0        0    11128 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/argparser.py
--rw-r--r--   0        0        0     8863 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/cmds.py
--rw-r--r--   0        0        0     1347 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/main.py
--rw-r--r--   0        0        0     1114 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/__init__.py
--rw-r--r--   0        0        0     2336 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/artifact.py
--rw-r--r--   0        0        0     7508 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/base.py
--rw-r--r--   0        0        0     6915 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/branch.py
--rw-r--r--   0        0        0    16573 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/organization.py
--rw-r--r--   0        0        0    12937 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/pull_request.py
--rw-r--r--   0        0        0     4607 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/release.py
--rw-r--r--   0        0        0     4299 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/search.py
--rw-r--r--   0        0        0     3922 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/tag.py
--rw-r--r--   0        0        0    11477 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/models/workflow.py
--rw-r--r--   0        0        0      790 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/pr_template.md
--rw-r--r--   0        0        0     3207 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/script/__init__.py
--rw-r--r--   0        0        0      835 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/script/errors.py
--rw-r--r--   0        0        0     4854 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/script/load.py
--rw-r--r--   0        0        0     1495 2023-04-05 12:29:11.373273 pontos-23.4.0/pontos/github/script/parser.py
--rw-r--r--   0        0        0    14685 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/helper.py
--rw-r--r--   0        0        0     6211 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/models/__init__.py
--rw-r--r--   0        0        0      821 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/__init__.py
--rw-r--r--   0        0        0     4660 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/api.py
--rw-r--r--   0        0        0     2149 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/cpe/__init__.py
--rw-r--r--   0        0        0     6708 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/cpe/api.py
--rw-r--r--   0        0        0     2618 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/cve/__init__.py
--rw-r--r--   0        0        0    10802 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/cve/api.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/models/__init__.py
--rw-r--r--   0        0        0     2973 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/models/cpe.py
--rw-r--r--   0        0        0     7250 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/models/cve.py
--rw-r--r--   0        0        0     3254 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/models/cvss_v2.py
--rw-r--r--   0        0        0     4471 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/nvd/models/cvss_v3.py
--rw-r--r--   0        0        0     3400 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/pontos.py
--rw-r--r--   0        0        0        0 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/py.typed
--rw-r--r--   0        0        0     1164 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/release/__init__.py
--rw-r--r--   0        0        0     2472 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/release/helper.py
--rw-r--r--   0        0        0     2127 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/release/main.py
--rw-r--r--   0        0        0     7440 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/release/parser.py
--rw-r--r--   0        0        0    12114 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/release/release.py
--rw-r--r--   0        0        0    12039 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/release/sign.py
--rw-r--r--   0        0        0      886 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/terminal/__init__.py
--rw-r--r--   0        0        0     1770 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/terminal/null.py
--rw-r--r--   0        0        0     4717 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/terminal/rich.py
--rw-r--r--   0        0        0     9416 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/terminal/terminal.py
--rw-r--r--   0        0        0     7231 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/testing/__init__.py
--rw-r--r--   0        0        0      773 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/__init__.py
--rw-r--r--   0        0        0      838 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/__main__.py
--rw-r--r--   0        0        0      749 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.bash
--rw-r--r--   0        0        0      757 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.c
--rw-r--r--   0        0        0      737 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.cmake
--rw-r--r--   0        0        0      753 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.go
--rw-r--r--   0        0        0      757 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.h
--rw-r--r--   0        0        0      757 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.js
--rw-r--r--   0        0        0      871 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.nasl
--rw-r--r--   0        0        0      737 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.po
--rw-r--r--   0        0        0      737 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.py
--rw-r--r--   0        0        0      747 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.sh
--rw-r--r--   0        0        0      709 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.txt
--rw-r--r--   0        0        0      741 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.xml
--rw-r--r--   0        0        0      741 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.xsl
--rw-r--r--   0        0        0      733 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-only/template.c
--rw-r--r--   0        0        0      733 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-only/template.h
--rw-r--r--   0        0        0      793 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.bash
--rw-r--r--   0        0        0      802 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.c
--rw-r--r--   0        0        0      781 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.cmake
--rw-r--r--   0        0        0      802 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.h
--rw-r--r--   0        0        0      802 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.js
--rw-r--r--   0        0        0      915 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.nasl
--rw-r--r--   0        0        0      781 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.po
--rw-r--r--   0        0        0      781 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.py
--rw-r--r--   0        0        0      791 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.sh
--rw-r--r--   0        0        0      751 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.txt
--rw-r--r--   0        0        0      783 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.xml
--rw-r--r--   0        0        0      783 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.xsl
--rw-r--r--   0        0        0      727 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.bash
--rw-r--r--   0        0        0      735 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.c
--rw-r--r--   0        0        0      715 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.cmake
--rw-r--r--   0        0        0      731 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.go
--rw-r--r--   0        0        0      735 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.h
--rw-r--r--   0        0        0      735 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.js
--rw-r--r--   0        0        0      849 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.nasl
--rw-r--r--   0        0        0      715 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.po
--rw-r--r--   0        0        0      715 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.py
--rw-r--r--   0        0        0      725 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.sh
--rw-r--r--   0        0        0      687 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.txt
--rw-r--r--   0        0        0      720 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.xml
--rw-r--r--   0        0        0      720 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.xsl
--rw-r--r--   0        0        0    12050 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/updateheader/updateheader.py
--rw-r--r--   0        0        0     1067 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/__init__.py
--rw-r--r--   0        0        0      816 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/__main__.py
--rw-r--r--   0        0        0      103 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/__version__.py
--rw-r--r--   0        0        0     8837 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/_calculator.py
--rw-r--r--   0        0        0     1416 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/commands/__init__.py
--rw-r--r--   0        0        0     7752 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/commands/_cmake.py
--rw-r--r--   0        0        0     2553 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/commands/_command.py
--rw-r--r--   0        0        0     3905 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/commands/_go.py
--rw-r--r--   0        0        0     6263 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/commands/_javascript.py
--rw-r--r--   0        0        0     7786 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/commands/_python.py
--rw-r--r--   0        0        0      961 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/errors.py
--rw-r--r--   0        0        0     2018 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/helper.py
--rw-r--r--   0        0        0     3692 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/main.py
--rw-r--r--   0        0        0     4163 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/parser.py
--rw-r--r--   0        0        0     3750 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/project.py
--rw-r--r--   0        0        0     2163 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/schemes/__init__.py
--rw-r--r--   0        0        0    13016 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/schemes/_pep440.py
--rw-r--r--   0        0        0     2145 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/schemes/_scheme.py
--rw-r--r--   0        0        0    14400 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/schemes/_semantic.py
--rw-r--r--   0        0        0     5042 2023-04-05 12:29:11.377273 pontos-23.4.0/pontos/version/version.py
--rw-r--r--   0        0        0     2890 2023-04-05 12:29:11.377273 pontos-23.4.0/pyproject.toml
--rw-r--r--   0        0        0     1872 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/artifacts-download.py
--rw-r--r--   0        0        0     1862 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/artifacts.py
--rw-r--r--   0        0        0     1605 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/branchprotection.py
--rw-r--r--   0        0        0     5606 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/create-repository.py
--rw-r--r--   0        0        0     2212 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/enforce-admins.py
--rw-r--r--   0        0        0     1834 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/lock-branch.py
--rw-r--r--   0        0        0     2577 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/members.py
--rw-r--r--   0        0        0     2179 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/release-assets-download.py
--rw-r--r--   0        0        0     2294 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/repositories.py
--rw-r--r--   0        0        0     6717 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/search-repositories.py
--rw-r--r--   0        0        0     3689 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/team-repositories.py
--rw-r--r--   0        0        0     1654 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/teams.py
--rw-r--r--   0        0        0     2789 2023-04-05 12:29:11.377273 pontos-23.4.0/scripts/github/workflow-runs.py
--rw-r--r--   0        0        0     1518 2023-04-05 12:29:11.377273 pontos-23.4.0/tests/__init__.py
--rw-r--r--   0        0        0     1031 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/changelog/__init__.py
--rw-r--r--   0        0        0      375 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/changelog/changelog.toml
--rw-r--r--   0        0        0    16629 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/changelog/test_conventional_commits.py
--rw-r--r--   0        0        0     1925 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/changelog/test_parser.py
--rw-r--r--   0        0        0       69 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/fake_pyproject.toml
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/git/__init__.py
--rw-r--r--   0        0        0    23162 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/git/test_git.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/__init__.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/actions/__init__.py
--rw-r--r--   0        0        0    29628 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/actions/test-pull-request-event.json
--rw-r--r--   0        0        0     4385 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/actions/test_core.py
--rw-r--r--   0        0        0     3534 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/actions/test_env.py
--rw-r--r--   0        0        0     2086 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/actions/test_event.py
--rw-r--r--   0        0        0     1232 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/__init__.py
--rw-r--r--   0        0        0    20021 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/pr-files.json
--rw-r--r--   0        0        0     5624 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/release-response.json
--rw-r--r--   0        0        0    12076 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_artifacts.py
--rw-r--r--   0        0        0    20096 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_branch.py
--rw-r--r--   0        0        0     9619 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_client.py
--rw-r--r--   0        0        0     2087 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_contents.py
--rw-r--r--   0        0        0     2801 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_labels.py
--rw-r--r--   0        0        0    71096 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_organizations.py
--rw-r--r--   0        0        0    52500 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_pull_requests.py
--rw-r--r--   0        0        0    17774 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_release.py
--rw-r--r--   0        0        0    37847 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_repositories.py
--rw-r--r--   0        0        0    24490 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_search.py
--rw-r--r--   0        0        0     7383 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_tags.py
--rw-r--r--   0        0        0    39045 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_teams.py
--rw-r--r--   0        0        0   129346 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/api/test_workflows.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/__init__.py
--rw-r--r--   0        0        0     3210 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_artifact.py
--rw-r--r--   0        0        0     9831 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_base.py
--rw-r--r--   0        0        0    31873 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_branch.py
--rw-r--r--   0        0        0    19874 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_organization.py
--rw-r--r--   0        0        0    76541 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_pull_request.py
--rw-r--r--   0        0        0    12062 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_release.py
--rw-r--r--   0        0        0     2216 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_search.py
--rw-r--r--   0        0        0     3400 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_tag.py
--rw-r--r--   0        0        0    41463 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/models/test_workflow.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/script/__init__.py
--rw-r--r--   0        0        0     3520 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/script/test_load.py
--rw-r--r--   0        0        0     2052 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/script/test_parser.py
--rw-r--r--   0        0        0     6098 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/test_argparser.py
--rw-r--r--   0        0        0     9562 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/github/test_cmds.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/models/__init__.py
--rw-r--r--   0        0        0     6424 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/models/test_models.py
--rw-r--r--   0        0        0     2505 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/nvd/__init__.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/nvd/cpe/__init__.py
--rw-r--r--   0        0        0    11271 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/nvd/cpe/test_api.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/nvd/cve/__init__.py
--rw-r--r--   0        0        0    26602 2023-04-05 12:29:11.381273 pontos-23.4.0/tests/nvd/cve/test_api.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/nvd/models/__init__.py
--rw-r--r--   0        0        0     3706 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/nvd/models/test_cpe.py
--rw-r--r--   0        0        0    25911 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/nvd/models/test_cve.py
--rw-r--r--   0        0        0     3994 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/nvd/test_api.py
--rw-r--r--   0        0        0      721 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/release/__init__.py
--rw-r--r--   0        0        0     3190 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/release/test_helper.py
--rw-r--r--   0        0        0     8223 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/release/test_parser.py
--rw-r--r--   0        0        0    59154 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/release/test_release.py
--rw-r--r--   0        0        0    21452 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/release/test_sign.py
--rw-r--r--   0        0        0      345 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/release/v1.2.3.md
--rw-r--r--   0        0        0      745 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/terminal/__init__.py
--rw-r--r--   0        0        0     6653 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/terminal/test_terminal.py
--rw-r--r--   0        0        0    19355 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/test_helper.py
--rw-r--r--   0        0        0     1373 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/test_pontos.py
--rw-r--r--   0        0        0      716 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/testing/__init__.py
--rw-r--r--   0        0        0     7785 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/testing/test_testing.py
--rw-r--r--   0        0        0      721 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/updateheader/__init__.py
--rw-r--r--   0        0        0    15227 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/updateheader/test_header.py
--rw-r--r--   0        0        0     1031 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/__init__.py
--rw-r--r--   0        0        0      727 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/commands/__init__.py
--rw-r--r--   0        0        0    11322 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/commands/test_cmake.py
--rw-r--r--   0        0        0    10742 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/commands/test_go.py
--rw-r--r--   0        0        0    15371 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/commands/test_javascript.py
--rw-r--r--   0        0        0    16667 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/commands/test_python.py
--rw-r--r--   0        0        0      727 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/schemes/__init__.py
--rw-r--r--   0        0        0    22759 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/schemes/test_pep440.py
--rw-r--r--   0        0        0    24942 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/schemes/test_semantic.py
--rw-r--r--   0        0        0      919 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/test_commands.py
--rw-r--r--   0        0        0     1096 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/test_errors.py
--rw-r--r--   0        0        0     3385 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/test_helper.py
--rw-r--r--   0        0        0    10908 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/test_main.py
--rw-r--r--   0        0        0     1131 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/test_parser.py
--rw-r--r--   0        0        0     6187 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/test_project.py
--rw-r--r--   0        0        0     1791 2023-04-05 12:29:11.385273 pontos-23.4.0/tests/version/test_version.py
--rw-r--r--   0        0        0     4820 1970-01-01 00:00:00.000000 pontos-23.4.0/PKG-INFO
+-rw-r--r--   0        0        0    35149 2023-04-06 10:54:40.732158 pontos-23.4.1/LICENSE
+-rw-r--r--   0        0        0     3349 2023-04-06 10:54:40.732158 pontos-23.4.1/README.md
+-rw-r--r--   0        0        0    97720 2023-04-06 10:54:40.736158 pontos-23.4.1/poetry.lock
+-rw-r--r--   0        0        0       32 2023-04-06 10:54:40.736158 pontos-23.4.1/poetry.toml
+-rw-r--r--   0        0        0      791 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/__init__.py
+-rw-r--r--   0        0        0      968 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/changelog/__init__.py
+-rw-r--r--   0        0        0     9914 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/changelog/conventional_commits.py
+-rw-r--r--   0        0        0      965 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/changelog/errors.py
+-rw-r--r--   0        0        0     4427 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/changelog/main.py
+-rw-r--r--   0        0        0      806 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/errors.py
+-rw-r--r--   0        0        0      882 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/git/__init__.py
+-rw-r--r--   0        0        0    16117 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/git/git.py
+-rw-r--r--   0        0        0     2538 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/git/status.py
+-rw-r--r--   0        0        0      760 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/__init__.py
+-rw-r--r--   0        0        0     1154 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/__init__.py
+-rw-r--r--   0        0        0     2239 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/argparser.py
+-rw-r--r--   0        0        0     1472 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/cmds.py
+-rw-r--r--   0        0        0     6158 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/core.py
+-rw-r--r--   0        0        0     2426 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/env.py
+-rw-r--r--   0        0        0      861 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/errors.py
+-rw-r--r--   0        0        0     4173 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/event.py
+-rw-r--r--   0        0        0     1100 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/actions/main.py
+-rw-r--r--   0        0        0     2047 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/api/__init__.py
+-rw-r--r--   0        0        0     5531 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/api/api.py
+-rw-r--r--   0        0        0     6196 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/api/artifacts.py
+-rw-r--r--   0        0        0    34561 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/api/branch.py
+-rw-r--r--   0        0        0     9395 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/api/client.py
+-rw-r--r--   0        0        0     1844 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/api/contents.py
+-rw-r--r--   0        0        0      845 2023-04-06 10:54:40.736158 pontos-23.4.1/pontos/github/api/errors.py
+-rw-r--r--   0        0        0     1320 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/helper.py
+-rw-r--r--   0        0        0     2813 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/labels.py
+-rw-r--r--   0        0        0    10311 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/organizations.py
+-rw-r--r--   0        0        0    10519 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/pull_requests.py
+-rw-r--r--   0        0        0    11942 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/release.py
+-rw-r--r--   0        0        0    21512 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/repositories.py
+-rw-r--r--   0        0        0     3276 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/search.py
+-rw-r--r--   0        0        0     5079 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/tags.py
+-rw-r--r--   0        0        0    15207 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/teams.py
+-rw-r--r--   0        0        0     9182 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/api/workflows.py
+-rw-r--r--   0        0        0    11128 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/argparser.py
+-rw-r--r--   0        0        0     8863 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/cmds.py
+-rw-r--r--   0        0        0     1347 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/main.py
+-rw-r--r--   0        0        0     1114 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/__init__.py
+-rw-r--r--   0        0        0     2336 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/artifact.py
+-rw-r--r--   0        0        0     7508 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/base.py
+-rw-r--r--   0        0        0     6915 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/branch.py
+-rw-r--r--   0        0        0    16573 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/organization.py
+-rw-r--r--   0        0        0    12937 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/pull_request.py
+-rw-r--r--   0        0        0     4607 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/release.py
+-rw-r--r--   0        0        0     4299 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/search.py
+-rw-r--r--   0        0        0     3922 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/tag.py
+-rw-r--r--   0        0        0    11477 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/models/workflow.py
+-rw-r--r--   0        0        0      790 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/pr_template.md
+-rw-r--r--   0        0        0     3207 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/script/__init__.py
+-rw-r--r--   0        0        0      835 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/script/errors.py
+-rw-r--r--   0        0        0     4854 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/script/load.py
+-rw-r--r--   0        0        0     1495 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/github/script/parser.py
+-rw-r--r--   0        0        0    14685 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/helper.py
+-rw-r--r--   0        0        0     6211 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/models/__init__.py
+-rw-r--r--   0        0        0      821 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/__init__.py
+-rw-r--r--   0        0        0     4660 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/api.py
+-rw-r--r--   0        0        0     2149 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/cpe/__init__.py
+-rw-r--r--   0        0        0     6708 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/cpe/api.py
+-rw-r--r--   0        0        0     2618 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/cve/__init__.py
+-rw-r--r--   0        0        0    10802 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/cve/api.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/models/__init__.py
+-rw-r--r--   0        0        0     2973 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/models/cpe.py
+-rw-r--r--   0        0        0     7250 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/models/cve.py
+-rw-r--r--   0        0        0     3254 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/models/cvss_v2.py
+-rw-r--r--   0        0        0     4471 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/nvd/models/cvss_v3.py
+-rw-r--r--   0        0        0     3400 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/pontos.py
+-rw-r--r--   0        0        0        0 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/py.typed
+-rw-r--r--   0        0        0     1164 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/release/__init__.py
+-rw-r--r--   0        0        0     2472 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/release/helper.py
+-rw-r--r--   0        0        0     2127 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/release/main.py
+-rw-r--r--   0        0        0     7440 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/release/parser.py
+-rw-r--r--   0        0        0    12114 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/release/release.py
+-rw-r--r--   0        0        0    12039 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/release/sign.py
+-rw-r--r--   0        0        0      886 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/terminal/__init__.py
+-rw-r--r--   0        0        0     1770 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/terminal/null.py
+-rw-r--r--   0        0        0     4717 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/terminal/rich.py
+-rw-r--r--   0        0        0     9416 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/terminal/terminal.py
+-rw-r--r--   0        0        0     7231 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/testing/__init__.py
+-rw-r--r--   0        0        0      773 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/updateheader/__init__.py
+-rw-r--r--   0        0        0      838 2023-04-06 10:54:40.740158 pontos-23.4.1/pontos/updateheader/__main__.py
+-rw-r--r--   0        0        0      749 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.bash
+-rw-r--r--   0        0        0      757 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.c
+-rw-r--r--   0        0        0      737 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.cmake
+-rw-r--r--   0        0        0      753 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.go
+-rw-r--r--   0        0        0      757 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.h
+-rw-r--r--   0        0        0      757 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.js
+-rw-r--r--   0        0        0      871 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.nasl
+-rw-r--r--   0        0        0      737 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.po
+-rw-r--r--   0        0        0      737 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.py
+-rw-r--r--   0        0        0      747 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.sh
+-rw-r--r--   0        0        0      709 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.txt
+-rw-r--r--   0        0        0      741 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.xml
+-rw-r--r--   0        0        0      741 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.xsl
+-rw-r--r--   0        0        0      733 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-only/template.c
+-rw-r--r--   0        0        0      733 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-only/template.h
+-rw-r--r--   0        0        0      793 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.bash
+-rw-r--r--   0        0        0      802 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.c
+-rw-r--r--   0        0        0      781 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.cmake
+-rw-r--r--   0        0        0      802 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.h
+-rw-r--r--   0        0        0      802 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.js
+-rw-r--r--   0        0        0      915 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.nasl
+-rw-r--r--   0        0        0      781 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.po
+-rw-r--r--   0        0        0      781 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.py
+-rw-r--r--   0        0        0      791 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.sh
+-rw-r--r--   0        0        0      751 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.txt
+-rw-r--r--   0        0        0      783 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.xml
+-rw-r--r--   0        0        0      783 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.xsl
+-rw-r--r--   0        0        0      727 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.bash
+-rw-r--r--   0        0        0      735 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.c
+-rw-r--r--   0        0        0      715 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.cmake
+-rw-r--r--   0        0        0      731 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.go
+-rw-r--r--   0        0        0      735 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.h
+-rw-r--r--   0        0        0      735 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.js
+-rw-r--r--   0        0        0      849 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.nasl
+-rw-r--r--   0        0        0      715 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.po
+-rw-r--r--   0        0        0      715 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.py
+-rw-r--r--   0        0        0      725 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.sh
+-rw-r--r--   0        0        0      687 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.txt
+-rw-r--r--   0        0        0      720 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.xml
+-rw-r--r--   0        0        0      720 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.xsl
+-rw-r--r--   0        0        0    12050 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/updateheader/updateheader.py
+-rw-r--r--   0        0        0     1067 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/__init__.py
+-rw-r--r--   0        0        0      816 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/__main__.py
+-rw-r--r--   0        0        0      103 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/__version__.py
+-rw-r--r--   0        0        0     8837 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/_calculator.py
+-rw-r--r--   0        0        0     1416 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/commands/__init__.py
+-rw-r--r--   0        0        0     7752 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/commands/_cmake.py
+-rw-r--r--   0        0        0     2553 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/commands/_command.py
+-rw-r--r--   0        0        0     3792 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/commands/_go.py
+-rw-r--r--   0        0        0     6263 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/commands/_javascript.py
+-rw-r--r--   0        0        0     7786 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/commands/_python.py
+-rw-r--r--   0        0        0      961 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/errors.py
+-rw-r--r--   0        0        0     2018 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/helper.py
+-rw-r--r--   0        0        0     3692 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/main.py
+-rw-r--r--   0        0        0     4163 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/parser.py
+-rw-r--r--   0        0        0     3750 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/project.py
+-rw-r--r--   0        0        0     2163 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/schemes/__init__.py
+-rw-r--r--   0        0        0    13117 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/schemes/_pep440.py
+-rw-r--r--   0        0        0     2145 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/schemes/_scheme.py
+-rw-r--r--   0        0        0    14501 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/schemes/_semantic.py
+-rw-r--r--   0        0        0     5241 2023-04-06 10:54:40.744158 pontos-23.4.1/pontos/version/version.py
+-rw-r--r--   0        0        0     2890 2023-04-06 10:54:40.744158 pontos-23.4.1/pyproject.toml
+-rw-r--r--   0        0        0     1872 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/artifacts-download.py
+-rw-r--r--   0        0        0     1862 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/artifacts.py
+-rw-r--r--   0        0        0     1605 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/branchprotection.py
+-rw-r--r--   0        0        0     5606 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/create-repository.py
+-rw-r--r--   0        0        0     2212 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/enforce-admins.py
+-rw-r--r--   0        0        0     1834 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/lock-branch.py
+-rw-r--r--   0        0        0     2577 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/members.py
+-rw-r--r--   0        0        0     2179 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/release-assets-download.py
+-rw-r--r--   0        0        0     2294 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/repositories.py
+-rw-r--r--   0        0        0     6717 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/search-repositories.py
+-rw-r--r--   0        0        0     3689 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/team-repositories.py
+-rw-r--r--   0        0        0     1654 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/teams.py
+-rw-r--r--   0        0        0     2789 2023-04-06 10:54:40.744158 pontos-23.4.1/scripts/github/workflow-runs.py
+-rw-r--r--   0        0        0     1518 2023-04-06 10:54:40.744158 pontos-23.4.1/tests/__init__.py
+-rw-r--r--   0        0        0     1031 2023-04-06 10:54:40.744158 pontos-23.4.1/tests/changelog/__init__.py
+-rw-r--r--   0        0        0      375 2023-04-06 10:54:40.744158 pontos-23.4.1/tests/changelog/changelog.toml
+-rw-r--r--   0        0        0    17750 2023-04-06 10:54:40.744158 pontos-23.4.1/tests/changelog/test_conventional_commits.py
+-rw-r--r--   0        0        0     1925 2023-04-06 10:54:40.744158 pontos-23.4.1/tests/changelog/test_parser.py
+-rw-r--r--   0        0        0       69 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/fake_pyproject.toml
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/git/__init__.py
+-rw-r--r--   0        0        0    27772 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/git/test_git.py
+-rw-r--r--   0        0        0     4215 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/git/test_status.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/__init__.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/actions/__init__.py
+-rw-r--r--   0        0        0    29628 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/actions/test-pull-request-event.json
+-rw-r--r--   0        0        0     4385 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/actions/test_core.py
+-rw-r--r--   0        0        0     3534 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/actions/test_env.py
+-rw-r--r--   0        0        0     2086 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/actions/test_event.py
+-rw-r--r--   0        0        0     1232 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/__init__.py
+-rw-r--r--   0        0        0    20021 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/pr-files.json
+-rw-r--r--   0        0        0     5624 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/release-response.json
+-rw-r--r--   0        0        0    12076 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_artifacts.py
+-rw-r--r--   0        0        0    20096 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_branch.py
+-rw-r--r--   0        0        0     9619 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_client.py
+-rw-r--r--   0        0        0     2087 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_contents.py
+-rw-r--r--   0        0        0     2801 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_labels.py
+-rw-r--r--   0        0        0    71096 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_organizations.py
+-rw-r--r--   0        0        0    52500 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_pull_requests.py
+-rw-r--r--   0        0        0    17774 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_release.py
+-rw-r--r--   0        0        0    37847 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_repositories.py
+-rw-r--r--   0        0        0    24490 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_search.py
+-rw-r--r--   0        0        0     7383 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_tags.py
+-rw-r--r--   0        0        0    39045 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_teams.py
+-rw-r--r--   0        0        0   129346 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/api/test_workflows.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/models/__init__.py
+-rw-r--r--   0        0        0     3210 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/models/test_artifact.py
+-rw-r--r--   0        0        0     9831 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/models/test_base.py
+-rw-r--r--   0        0        0    31873 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/models/test_branch.py
+-rw-r--r--   0        0        0    19874 2023-04-06 10:54:40.748158 pontos-23.4.1/tests/github/models/test_organization.py
+-rw-r--r--   0        0        0    76541 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/models/test_pull_request.py
+-rw-r--r--   0        0        0    12062 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/models/test_release.py
+-rw-r--r--   0        0        0     2216 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/models/test_search.py
+-rw-r--r--   0        0        0     3400 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/models/test_tag.py
+-rw-r--r--   0        0        0    41463 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/models/test_workflow.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/script/__init__.py
+-rw-r--r--   0        0        0     3520 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/script/test_load.py
+-rw-r--r--   0        0        0     2052 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/script/test_parser.py
+-rw-r--r--   0        0        0     6098 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/test_argparser.py
+-rw-r--r--   0        0        0     9562 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/github/test_cmds.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/models/__init__.py
+-rw-r--r--   0        0        0     6424 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/models/test_models.py
+-rw-r--r--   0        0        0     2505 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/__init__.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/cpe/__init__.py
+-rw-r--r--   0        0        0    11271 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/cpe/test_api.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/cve/__init__.py
+-rw-r--r--   0        0        0    26602 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/cve/test_api.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/models/__init__.py
+-rw-r--r--   0        0        0     3706 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/models/test_cpe.py
+-rw-r--r--   0        0        0    25911 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/models/test_cve.py
+-rw-r--r--   0        0        0     3994 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/nvd/test_api.py
+-rw-r--r--   0        0        0      721 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/release/__init__.py
+-rw-r--r--   0        0        0     3190 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/release/test_helper.py
+-rw-r--r--   0        0        0     8223 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/release/test_parser.py
+-rw-r--r--   0        0        0    59154 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/release/test_release.py
+-rw-r--r--   0        0        0    21452 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/release/test_sign.py
+-rw-r--r--   0        0        0      345 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/release/v1.2.3.md
+-rw-r--r--   0        0        0      745 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/terminal/__init__.py
+-rw-r--r--   0        0        0     6653 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/terminal/test_terminal.py
+-rw-r--r--   0        0        0    19355 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/test_helper.py
+-rw-r--r--   0        0        0     1373 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/test_pontos.py
+-rw-r--r--   0        0        0      716 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/testing/__init__.py
+-rw-r--r--   0        0        0     7785 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/testing/test_testing.py
+-rw-r--r--   0        0        0      721 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/updateheader/__init__.py
+-rw-r--r--   0        0        0    15227 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/updateheader/test_header.py
+-rw-r--r--   0        0        0     1031 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/__init__.py
+-rw-r--r--   0        0        0      727 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/commands/__init__.py
+-rw-r--r--   0        0        0    11322 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/commands/test_cmake.py
+-rw-r--r--   0        0        0    10400 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/commands/test_go.py
+-rw-r--r--   0        0        0    15371 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/commands/test_javascript.py
+-rw-r--r--   0        0        0    16667 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/commands/test_python.py
+-rw-r--r--   0        0        0      727 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/schemes/__init__.py
+-rw-r--r--   0        0        0    22817 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/schemes/test_pep440.py
+-rw-r--r--   0        0        0    25027 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/schemes/test_semantic.py
+-rw-r--r--   0        0        0      919 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/test_commands.py
+-rw-r--r--   0        0        0     1096 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/test_errors.py
+-rw-r--r--   0        0        0     3385 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/test_helper.py
+-rw-r--r--   0        0        0    10908 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/test_main.py
+-rw-r--r--   0        0        0     1131 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/test_parser.py
+-rw-r--r--   0        0        0     6187 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/test_project.py
+-rw-r--r--   0        0        0     1791 2023-04-06 10:54:40.752158 pontos-23.4.1/tests/version/test_version.py
+-rw-r--r--   0        0        0     4820 1970-01-01 00:00:00.000000 pontos-23.4.1/PKG-INFO
```

### Comparing `pontos-23.4.0/LICENSE` & `pontos-23.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/README.md` & `pontos-23.4.1/README.md`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/poetry.lock` & `pontos-23.4.1/poetry.lock`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/__init__.py` & `pontos-23.4.1/pontos/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/changelog/__init__.py` & `pontos-23.4.1/pontos/changelog/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/changelog/conventional_commits.py` & `pontos-23.4.1/pontos/changelog/conventional_commits.py`

 * *Files 2% similar despite different names*

```diff
@@ -112,16 +112,15 @@
             next_version: Version of the to be created release the changelog
                 corresponds to. If None a changelog for an unrelease version
                 will be created.
 
         Returns:
             The created changelog content.
         """
-        commit_list = self._get_git_log(last_version)
-        commit_dict = self._sort_commits(commit_list)
+        commit_dict = self.get_commits(last_version)
         return self._build_changelog(last_version, next_version, commit_dict)
 
     def create_changelog_file(
         self,
         output: Union[str, Path],
         *,
         last_version: Optional[SupportsStr] = None,
@@ -139,14 +138,31 @@
                 will be created.
         """
         changelog = self.create_changelog(
             last_version=last_version, next_version=next_version
         )
         self._write_changelog_file(changelog, output)
 
+    def get_commits(
+        self,
+        last_version: Optional[SupportsStr] = None,
+    ) -> Dict[str, List[str]]:
+        """
+        Get all commits by conventional commit type
+
+        Args:
+            last_version: Version of the last release. If None it is considered
+                as the first release.
+
+        Returns:
+            A dict containing the grouped commit messages
+        """
+        commit_list = self._get_git_log(last_version)
+        return self._sort_commits(commit_list)
+
     def _get_first_commit(self) -> str:
         """
         Git the first commit ID for the current branch
         """
         git = Git()
         return git.rev_list("HEAD", max_parents=0, abbrev_commit=True)[0]
 
@@ -181,15 +197,16 @@
             'Fixed:': [
                 ...
             ],
         }
         ```
 
         Returns
-            The dict containing the commit messages"""
+            The dict containing the commit messages
+        """
         # get the commit types from the toml
         commit_types = self.config.get("commit_types")
 
         commit_link = f"{ADDRESS}{self.space}/{self.project}/commit/"
 
         commit_dict = {}
         if commits and len(commits) > 0:
```

### Comparing `pontos-23.4.0/pontos/changelog/errors.py` & `pontos-23.4.1/pontos/changelog/errors.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/changelog/main.py` & `pontos-23.4.1/pontos/changelog/main.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/errors.py` & `pontos-23.4.1/pontos/errors.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/git/__init__.py` & `pontos-23.4.1/pontos/git/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/git/git.py` & `pontos-23.4.1/pontos/git/git.py`

 * *Files 5% similar despite different names*

```diff
@@ -15,17 +15,18 @@
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 import subprocess
 from enum import Enum
 from os import PathLike, fspath
 from pathlib import Path
-from typing import List, Optional, Union
+from typing import Iterable, Iterator, List, Optional, Union
 
 from pontos.errors import PontosError
+from pontos.git.status import StatusEntry, parse_git_status
 
 DEFAULT_TAG_SORT_SUFFIX = [
     "-alpha",
     "a",
     "-beta",
     "b",
     "-rc",
@@ -571,7 +572,47 @@
         if max_parents is not None:
             args.append(f"--max-parents={max_parents}")
         if abbrev_commit:
             args.append("--abbrev-commit")
 
         args.extend(commit)
         return self.exec(*args).splitlines()
+
+    def move(self, old: PathLike, new: PathLike) -> None:
+        """
+        Move a file from old to new
+        """
+        return self.exec("mv", fspath(old), fspath(new))
+
+    def remove(self, to_remove: PathLike) -> None:
+        """
+        Remove a file from git
+        """
+        return self.exec("rm", fspath(to_remove))
+
+    def status(
+        self,
+        files: Optional[Iterable[PathLike]] = None,
+    ) -> Iterator[StatusEntry]:
+        """Get information about the current git status.
+
+        Args:
+            files: specify an iterable of :py:class:`os.PathLike` and
+                exclude all other paths for the status.
+
+        Returns:
+            An iterator of :py:class:`StatusEntry` instances that contain the
+            status of the specific files.
+        """
+        args = [
+            "status",
+            "-z",
+            "--ignore-submodules",
+            "--untracked-files=no",
+        ]
+
+        if files:
+            args.append("--")
+            args.extend([fspath(f) for f in files])
+
+        output = self.exec(*args)
+        return parse_git_status(output)
```

### Comparing `pontos-23.4.0/pontos/github/__init__.py` & `pontos-23.4.1/pontos/github/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/__init__.py` & `pontos-23.4.1/pontos/github/actions/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/argparser.py` & `pontos-23.4.1/pontos/github/actions/argparser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/cmds.py` & `pontos-23.4.1/pontos/github/actions/cmds.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/core.py` & `pontos-23.4.1/pontos/github/actions/core.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/env.py` & `pontos-23.4.1/pontos/github/actions/env.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/errors.py` & `pontos-23.4.1/pontos/github/actions/errors.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/event.py` & `pontos-23.4.1/pontos/github/actions/event.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/actions/main.py` & `pontos-23.4.1/pontos/github/actions/main.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/__init__.py` & `pontos-23.4.1/pontos/github/api/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/api.py` & `pontos-23.4.1/pontos/github/api/api.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/artifacts.py` & `pontos-23.4.1/pontos/github/api/artifacts.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/branch.py` & `pontos-23.4.1/pontos/github/api/branch.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/client.py` & `pontos-23.4.1/pontos/github/api/client.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/contents.py` & `pontos-23.4.1/pontos/github/api/contents.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/errors.py` & `pontos-23.4.1/pontos/github/api/errors.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/helper.py` & `pontos-23.4.1/pontos/github/api/helper.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/labels.py` & `pontos-23.4.1/pontos/github/api/labels.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/organizations.py` & `pontos-23.4.1/pontos/github/api/organizations.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/pull_requests.py` & `pontos-23.4.1/pontos/github/api/pull_requests.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/release.py` & `pontos-23.4.1/pontos/github/api/release.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/repositories.py` & `pontos-23.4.1/pontos/github/api/repositories.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/search.py` & `pontos-23.4.1/pontos/github/api/search.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/tags.py` & `pontos-23.4.1/pontos/github/api/tags.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/teams.py` & `pontos-23.4.1/pontos/github/api/teams.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/api/workflows.py` & `pontos-23.4.1/pontos/github/api/workflows.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/argparser.py` & `pontos-23.4.1/pontos/github/argparser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/cmds.py` & `pontos-23.4.1/pontos/github/cmds.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/main.py` & `pontos-23.4.1/pontos/github/main.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/__init__.py` & `pontos-23.4.1/pontos/github/models/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/artifact.py` & `pontos-23.4.1/pontos/github/models/artifact.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/base.py` & `pontos-23.4.1/pontos/github/models/base.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/branch.py` & `pontos-23.4.1/pontos/github/models/branch.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/organization.py` & `pontos-23.4.1/pontos/github/models/organization.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/pull_request.py` & `pontos-23.4.1/pontos/github/models/pull_request.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/release.py` & `pontos-23.4.1/pontos/github/models/release.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/search.py` & `pontos-23.4.1/pontos/github/models/search.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/tag.py` & `pontos-23.4.1/pontos/github/models/tag.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/models/workflow.py` & `pontos-23.4.1/pontos/github/models/workflow.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/pr_template.md` & `pontos-23.4.1/pontos/github/pr_template.md`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/script/__init__.py` & `pontos-23.4.1/pontos/github/script/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/script/errors.py` & `pontos-23.4.1/pontos/github/script/errors.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/script/load.py` & `pontos-23.4.1/pontos/github/script/load.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/github/script/parser.py` & `pontos-23.4.1/pontos/github/script/parser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/helper.py` & `pontos-23.4.1/pontos/helper.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/models/__init__.py` & `pontos-23.4.1/pontos/models/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/__init__.py` & `pontos-23.4.1/pontos/nvd/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/api.py` & `pontos-23.4.1/pontos/nvd/api.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/cpe/__init__.py` & `pontos-23.4.1/pontos/nvd/cpe/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/cpe/api.py` & `pontos-23.4.1/pontos/nvd/cpe/api.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/cve/__init__.py` & `pontos-23.4.1/pontos/nvd/cve/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/cve/api.py` & `pontos-23.4.1/pontos/nvd/cve/api.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/models/__init__.py` & `pontos-23.4.1/pontos/nvd/models/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/models/cpe.py` & `pontos-23.4.1/pontos/nvd/models/cpe.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/models/cve.py` & `pontos-23.4.1/pontos/nvd/models/cve.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/models/cvss_v2.py` & `pontos-23.4.1/pontos/nvd/models/cvss_v2.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/nvd/models/cvss_v3.py` & `pontos-23.4.1/pontos/nvd/models/cvss_v3.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/pontos.py` & `pontos-23.4.1/pontos/pontos.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/release/__init__.py` & `pontos-23.4.1/pontos/release/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/release/helper.py` & `pontos-23.4.1/pontos/release/helper.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/release/main.py` & `pontos-23.4.1/pontos/release/main.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/release/parser.py` & `pontos-23.4.1/pontos/release/parser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/release/release.py` & `pontos-23.4.1/pontos/release/release.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/release/sign.py` & `pontos-23.4.1/pontos/release/sign.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/terminal/__init__.py` & `pontos-23.4.1/pontos/terminal/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/terminal/null.py` & `pontos-23.4.1/pontos/terminal/null.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/terminal/rich.py` & `pontos-23.4.1/pontos/terminal/rich.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/terminal/terminal.py` & `pontos-23.4.1/pontos/terminal/terminal.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/testing/__init__.py` & `pontos-23.4.1/pontos/testing/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/__init__.py` & `pontos-23.4.1/pontos/updateheader/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/__main__.py` & `pontos-23.4.1/pontos/updateheader/__main__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.bash` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.bash`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.c` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.c`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.cmake` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.cmake`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.go` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.go`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.h` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.h`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.js` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.js`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.nasl` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.nasl`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.po` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.po`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.py` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.sh` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.sh`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.txt` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.txt`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.xml` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.xml`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/AGPL-3.0-or-later/template.xsl` & `pontos-23.4.1/pontos/updateheader/templates/AGPL-3.0-or-later/template.xsl`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-only/template.c` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-only/template.c`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-only/template.h` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-only/template.h`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.bash` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.bash`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.c` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.c`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.cmake` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.cmake`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.h` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.h`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.js` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.js`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.nasl` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.nasl`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.po` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.po`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.py` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.sh` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.sh`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.txt` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.txt`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.xml` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.xml`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-2.0-or-later/template.xsl` & `pontos-23.4.1/pontos/updateheader/templates/GPL-2.0-or-later/template.xsl`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.bash` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.bash`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.c` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.c`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.cmake` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.cmake`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.go` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.go`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.h` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.h`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.js` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.js`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.nasl` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.nasl`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.po` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.po`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.py` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.sh` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.sh`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.txt` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.txt`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.xml` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.xml`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/templates/GPL-3.0-or-later/template.xsl` & `pontos-23.4.1/pontos/updateheader/templates/GPL-3.0-or-later/template.xsl`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/updateheader/updateheader.py` & `pontos-23.4.1/pontos/updateheader/updateheader.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/__init__.py` & `pontos-23.4.1/pontos/version/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/__main__.py` & `pontos-23.4.1/pontos/version/__main__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/_calculator.py` & `pontos-23.4.1/pontos/version/_calculator.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/commands/__init__.py` & `pontos-23.4.1/pontos/version/commands/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/commands/_cmake.py` & `pontos-23.4.1/pontos/version/commands/_cmake.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/commands/_command.py` & `pontos-23.4.1/pontos/version/commands/_command.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/commands/_go.py` & `pontos-23.4.1/pontos/version/commands/_go.py`

 * *Files 2% similar despite different names*

```diff
@@ -16,15 +16,14 @@
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 import re
 from pathlib import Path
 from typing import Literal, Union
 
 from ..errors import VersionError
-from ..helper import get_last_release_version
 from ..version import Version, VersionUpdate
 from ._command import VersionCommand
 
 VERSION_MATCH = r'var [Vv]ersion = "(.+)"'
 TEMPLATE = """package main
 
 // THIS IS AN AUTOGENERATED FILE. DO NOT TOUCH!
@@ -90,17 +89,16 @@
     def update_version(
         self, new_version: Version, *, force: bool = False
     ) -> VersionUpdate:
         """Update the current version of this project"""
         try:
             current_version = self.get_current_version()
         except VersionError:
-            current_version = get_last_release_version(
-                self.versioning_scheme.parse_version, git_tag_prefix="v"
-            )
+            # likely the initial release
+            current_version = None
 
         if not force and new_version == current_version:
             return VersionUpdate(previous=current_version, new=new_version)
 
         self._update_version_file(new_version=new_version)
 
         return VersionUpdate(
```

### Comparing `pontos-23.4.0/pontos/version/commands/_javascript.py` & `pontos-23.4.1/pontos/version/commands/_javascript.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/commands/_python.py` & `pontos-23.4.1/pontos/version/commands/_python.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/errors.py` & `pontos-23.4.1/pontos/version/errors.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/helper.py` & `pontos-23.4.1/pontos/version/helper.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/main.py` & `pontos-23.4.1/pontos/version/main.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/parser.py` & `pontos-23.4.1/pontos/version/parser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/project.py` & `pontos-23.4.1/pontos/version/project.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/schemes/__init__.py` & `pontos-23.4.1/pontos/version/schemes/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/schemes/_pep440.py` & `pontos-23.4.1/pontos/version/schemes/_pep440.py`

 * *Files 1% similar despite different names*

```diff
@@ -180,24 +180,28 @@
                 f"-{version.pre[0]}{version.pre[1]}"
                 f"{version_local}"
             )
 
         return cls.from_string(str(version))
 
     def __eq__(self, other: Any) -> bool:
+        if other is None:
+            return False
         if isinstance(other, str):
             # allow to compare against "current" for now
             return False
         if not isinstance(other, Version):
             raise ValueError(f"Can't compare {type(self)} with {type(other)}")
         if not isinstance(other, type(self)):
             other = self.from_version(other)
         return self._version == other._version
 
     def __ne__(self, other: Any) -> bool:
+        if other is None:
+            return True
         if isinstance(other, str):
             # allow to compare against "current" for now
             return True
         if not isinstance(other, Version):
             raise ValueError(f"Can't compare {type(self)} with {type(other)}")
         if not isinstance(other, type(self)):
             other = self.from_version(other)
```

### Comparing `pontos-23.4.0/pontos/version/schemes/_scheme.py` & `pontos-23.4.1/pontos/version/schemes/_scheme.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/pontos/version/schemes/_semantic.py` & `pontos-23.4.1/pontos/version/schemes/_semantic.py`

 * *Files 1% similar despite different names*

```diff
@@ -143,28 +143,32 @@
 
     @property
     def patch(self) -> int:
         """The third item of :attr:`release` or ``0`` if unavailable."""
         return self._version_info.patch
 
     def __eq__(self, other: Any) -> bool:
+        if other is None:
+            return False
         if isinstance(other, str):
             # allow to compare against "current" for now
             return False
         if not isinstance(other, Version):
             raise ValueError(f"Can't compare {type(self)} with {type(other)}")
         if not isinstance(other, type(self)):
             other = self.from_version(other)
 
         return (
             self._version_info == other._version_info
             and self._version_info.build == other._version_info.build
         )
 
     def __ne__(self, other: Any) -> bool:
+        if other is None:
+            return True
         if isinstance(other, str):
             # allow to compare against "current" for now
             return True
         if not isinstance(other, Version):
             raise ValueError(f"Can't compare {type(self)} with {type(other)}")
         if not isinstance(other, type(self)):
             other = self.from_version(other)
```

### Comparing `pontos-23.4.0/pontos/version/version.py` & `pontos-23.4.1/pontos/version/version.py`

 * *Files 2% similar despite different names*

```diff
@@ -148,23 +148,30 @@
 class VersionUpdate:
     """
     Represents a version update from a previous version to a new version.
 
     If previous and new are equal the version was not updated and changed_files
     should be empty.
 
+    If there is no previous version for example in an initial release previous
+    should be None.
+
     Example:
         .. code-block:: python
 
             from pathlib import Path
             from python.version import Version, VersionUpdate
 
             update = VersionUpdate(
                 previous=Version("1.2.3"),
                 new=Version("2.0.0"),
                 changed_files=[Path("package.json"), Path("version.js")],
             )
     """
 
-    previous: Version
+    previous: Optional[Version]
     new: Version
     changed_files: list[Path] = field(default_factory=list)
+
+    @property
+    def is_update(self) -> bool:
+        return self.previous != self.new
```

### Comparing `pontos-23.4.0/pyproject.toml` & `pontos-23.4.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pontos"
-version = "23.4.0"
+version = "23.4.1"
 description = "Common utilities and tools maintained by Greenbone Networks"
 authors = ["Greenbone AG <info@greenbone.net>"]
 license = "GPL-3.0-or-later"
 readme = "README.md"
 homepage = "https://github.com/greenbone/pontos/"
 repository = "https://github.com/greenbone/pontos/"
 documentation = "https://greenbone.github.io/pontos/"
```

### Comparing `pontos-23.4.0/scripts/github/artifacts-download.py` & `pontos-23.4.1/scripts/github/artifacts-download.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/artifacts.py` & `pontos-23.4.1/scripts/github/artifacts.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/branchprotection.py` & `pontos-23.4.1/scripts/github/branchprotection.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/create-repository.py` & `pontos-23.4.1/scripts/github/create-repository.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/enforce-admins.py` & `pontos-23.4.1/scripts/github/enforce-admins.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/lock-branch.py` & `pontos-23.4.1/scripts/github/lock-branch.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/members.py` & `pontos-23.4.1/scripts/github/members.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/release-assets-download.py` & `pontos-23.4.1/scripts/github/release-assets-download.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/repositories.py` & `pontos-23.4.1/scripts/github/repositories.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/search-repositories.py` & `pontos-23.4.1/scripts/github/search-repositories.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/team-repositories.py` & `pontos-23.4.1/scripts/github/team-repositories.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/teams.py` & `pontos-23.4.1/scripts/github/teams.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/scripts/github/workflow-runs.py` & `pontos-23.4.1/scripts/github/workflow-runs.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/__init__.py` & `pontos-23.4.1/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/changelog/__init__.py` & `pontos-23.4.1/tests/changelog/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/changelog/test_conventional_commits.py` & `pontos-23.4.1/tests/changelog/test_conventional_commits.py`

 * *Files 2% similar despite different names*

```diff
@@ -501,7 +501,36 @@
             changelog = changelog_file.read_text(encoding="utf8")
 
         self.assertEqual(changelog, expected_output)
 
         git_mock.return_value.log.assert_called_once_with(
             "v0.0.1..HEAD", oneline=True
         )
+
+    @patch("pontos.changelog.conventional_commits.Git", autospec=True)
+    def test_get_commits(self, git_mock: MagicMock):
+        git_mock.return_value.list_tags.return_value = ["v0.0.1"]
+        git_mock.return_value.log.return_value = [
+            "1234567 Add: foo bar",
+            "8abcdef Add: bar baz",
+            "8abcd3f Add bar baz",
+            "8abcd3d Adding bar baz",
+            "1337abc Change: bar to baz",
+            "42a42a4 Remove: foo bar again",
+            "fedcba8 Test: bar baz testing",
+            "dead901 Refactor: bar baz ref",
+            "fedcba8 Fix: bar baz fixing",
+            "d0c4d0c Doc: bar baz documenting",
+        ]
+
+        changelog_builder = ChangelogBuilder(
+            space="foo",
+            project="bar",
+        )
+        commits = changelog_builder.get_commits(last_version="0.0.1")
+
+        self.assertEqual(len(commits), 4)  # four commit types
+
+        self.assertEqual(len(commits["Added"]), 2)
+        self.assertEqual(len(commits["Changed"]), 1)
+        self.assertEqual(len(commits["Removed"]), 1)
+        self.assertEqual(len(commits["Bug Fixes"]), 1)
```

### Comparing `pontos-23.4.0/tests/changelog/test_parser.py` & `pontos-23.4.1/tests/changelog/test_parser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/git/__init__.py` & `pontos-23.4.1/tests/git/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/git/test_git.py` & `pontos-23.4.1/tests/git/test_git.py`

 * *Files 24% similar despite different names*

```diff
@@ -22,14 +22,15 @@
 from pontos.git import Git
 from pontos.git.git import (
     DEFAULT_TAG_SORT_SUFFIX,
     ConfigScope,
     MergeStrategy,
     TagSort,
 )
+from pontos.git.status import Status
 from pontos.testing import temp_git_repository
 
 
 class GitTestCase(unittest.TestCase):
     @patch("pontos.git.git.exec_git")
     def test_exec(self, exec_git_mock):
         git = Git()
@@ -565,14 +566,67 @@
             "--abbrev-commit",
             "foo",
             "bar",
             "baz",
             cwd=None,
         )
 
+    @patch("pontos.git.git.exec_git")
+    def test_move(self, exec_git_mock):
+        git = Git()
+        git.move("foo", "bar")
+
+        exec_git_mock.assert_called_once_with(
+            "mv",
+            "foo",
+            "bar",
+            cwd=None,
+        )
+
+    @patch("pontos.git.git.exec_git")
+    def test_remove(self, exec_git_mock):
+        git = Git()
+        git.remove("foo")
+
+        exec_git_mock.assert_called_once_with(
+            "rm",
+            "foo",
+            cwd=None,
+        )
+
+    @patch("pontos.git.git.exec_git")
+    def test_status(self, exec_git_mock):
+        git = Git()
+        git.status()
+
+        exec_git_mock.assert_called_once_with(
+            "status",
+            "-z",
+            "--ignore-submodules",
+            "--untracked-files=no",
+            cwd=None,
+        )
+
+    @patch("pontos.git.git.exec_git")
+    def test_status_with_files(self, exec_git_mock):
+        git = Git()
+        git.status(["foo", "bar", "baz"])
+
+        exec_git_mock.assert_called_once_with(
+            "status",
+            "-z",
+            "--ignore-submodules",
+            "--untracked-files=no",
+            "--",
+            "foo",
+            "bar",
+            "baz",
+            cwd=None,
+        )
+
 
 class GitExtendedTestCase(unittest.TestCase):
     def test_semantic_list_tags(self):
         with temp_git_repository() as tmp_git:
             tags = [
                 "v0.6.5-alpha3",
                 "v0.6.5-beta1",
@@ -763,7 +817,94 @@
                     "v0.6.5a3",
                     "v0.6.5b1",
                     "v0.6.5rc1",
                     "v0.6.5",
                     "v1.0.0",
                 ],
             )
+
+    def test_git_status(self):
+        with temp_git_repository() as tmp_git:
+            tracked_file = tmp_git / "foo.json"
+            tracked_file.write_text("sed diam nonumy eirmod", encoding="utf8")
+            changed_file = tmp_git / "bar.json"
+            changed_file.touch()
+            staged_changed_file = tmp_git / "ipsum.json"
+            staged_changed_file.write_text("tempor invidunt ut labore")
+            removed_file = tmp_git / "lorem.json"
+            removed_file.write_text(
+                "consetetur sadipscing elitr", encoding="utf8"
+            )
+            renamed_file = tmp_git / "foo.md"
+            renamed_file.write_text(
+                "et dolore magna aliquyam erat", encoding="utf8"
+            )
+
+            git = Git(tmp_git)
+            git.config("commit.gpgSign", "false", scope=ConfigScope.LOCAL)
+            git.add(
+                [
+                    tracked_file,
+                    changed_file,
+                    staged_changed_file,
+                    removed_file,
+                    renamed_file,
+                ]
+            )
+            git.commit("Some commit")
+
+            changed_file.write_text("Lorem Ipsum", encoding="utf8")
+            staged_changed_file.write_text("Lorem Ipsum", encoding="utf8")
+
+            added_file = tmp_git / "foo.txt"
+            added_file.touch()
+
+            added_modified_file = tmp_git / "ipsum.txt"
+            added_modified_file.touch()
+
+            git.add([added_file, staged_changed_file, added_modified_file])
+
+            staged_changed_file.write_text("Dolor sit", encoding="utf8")
+
+            added_modified_file.write_text("Lorem Ipsum", encoding="utf8")
+
+            git.move(renamed_file, "foo.rst")
+            git.remove(removed_file)
+
+            untracked_file = tmp_git / "bar.txt"
+            untracked_file.touch()
+
+            it = git.status()
+
+            status = next(it)
+            self.assertEqual(status.index, Status.UNMODIFIED)
+            self.assertEqual(status.working_tree, Status.MODIFIED)
+            self.assertEqual(status.path, Path("bar.json"))
+
+            status = next(it)
+            self.assertEqual(status.index, Status.RENAMED)
+            self.assertEqual(status.working_tree, Status.UNMODIFIED)
+            self.assertEqual(status.path, Path("foo.rst"))
+            self.assertEqual(status.old_path, Path("foo.md"))
+
+            status = next(it)
+            self.assertEqual(status.index, Status.ADDED)
+            self.assertEqual(status.working_tree, Status.UNMODIFIED)
+            self.assertEqual(status.path, Path("foo.txt"))
+
+            status = next(it)
+            self.assertEqual(status.index, Status.MODIFIED)
+            self.assertEqual(status.working_tree, Status.MODIFIED)
+            self.assertEqual(status.path, Path("ipsum.json"))
+
+            status = next(it)
+            self.assertEqual(status.index, Status.ADDED)
+            self.assertEqual(status.working_tree, Status.MODIFIED)
+            self.assertEqual(status.path, Path("ipsum.txt"))
+
+            status = next(it)
+            self.assertEqual(status.index, Status.DELETED)
+            self.assertEqual(status.working_tree, Status.UNMODIFIED)
+            self.assertEqual(status.path, Path("lorem.json"))
+
+            with self.assertRaises(StopIteration):
+                next(it)
```

### Comparing `pontos-23.4.0/tests/github/__init__.py` & `pontos-23.4.1/tests/github/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/actions/__init__.py` & `pontos-23.4.1/tests/github/actions/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/actions/test-pull-request-event.json` & `pontos-23.4.1/tests/github/actions/test-pull-request-event.json`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/actions/test_core.py` & `pontos-23.4.1/tests/github/actions/test_core.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/actions/test_env.py` & `pontos-23.4.1/tests/github/actions/test_env.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/actions/test_event.py` & `pontos-23.4.1/tests/github/actions/test_event.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/__init__.py` & `pontos-23.4.1/tests/github/api/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/pr-files.json` & `pontos-23.4.1/tests/github/api/pr-files.json`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/release-response.json` & `pontos-23.4.1/tests/github/api/release-response.json`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_artifacts.py` & `pontos-23.4.1/tests/github/api/test_artifacts.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_branch.py` & `pontos-23.4.1/tests/github/api/test_branch.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_client.py` & `pontos-23.4.1/tests/github/api/test_client.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_contents.py` & `pontos-23.4.1/tests/github/api/test_contents.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_labels.py` & `pontos-23.4.1/tests/github/api/test_labels.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_organizations.py` & `pontos-23.4.1/tests/github/api/test_organizations.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_pull_requests.py` & `pontos-23.4.1/tests/github/api/test_pull_requests.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_release.py` & `pontos-23.4.1/tests/github/api/test_release.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_repositories.py` & `pontos-23.4.1/tests/github/api/test_repositories.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_search.py` & `pontos-23.4.1/tests/github/api/test_search.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_tags.py` & `pontos-23.4.1/tests/github/api/test_tags.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_teams.py` & `pontos-23.4.1/tests/github/api/test_teams.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/api/test_workflows.py` & `pontos-23.4.1/tests/github/api/test_workflows.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/__init__.py` & `pontos-23.4.1/tests/github/models/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_artifact.py` & `pontos-23.4.1/tests/github/models/test_artifact.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_base.py` & `pontos-23.4.1/tests/github/models/test_base.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_branch.py` & `pontos-23.4.1/tests/github/models/test_branch.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_organization.py` & `pontos-23.4.1/tests/github/models/test_organization.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_pull_request.py` & `pontos-23.4.1/tests/github/models/test_pull_request.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_release.py` & `pontos-23.4.1/tests/github/models/test_release.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_search.py` & `pontos-23.4.1/tests/github/models/test_search.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_tag.py` & `pontos-23.4.1/tests/github/models/test_tag.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/models/test_workflow.py` & `pontos-23.4.1/tests/github/models/test_workflow.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/script/__init__.py` & `pontos-23.4.1/tests/github/script/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/script/test_load.py` & `pontos-23.4.1/tests/github/script/test_load.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/script/test_parser.py` & `pontos-23.4.1/tests/github/script/test_parser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/test_argparser.py` & `pontos-23.4.1/tests/github/test_argparser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/github/test_cmds.py` & `pontos-23.4.1/tests/github/test_cmds.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/models/__init__.py` & `pontos-23.4.1/tests/models/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/models/test_models.py` & `pontos-23.4.1/tests/models/test_models.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/__init__.py` & `pontos-23.4.1/tests/nvd/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/cpe/__init__.py` & `pontos-23.4.1/tests/nvd/cpe/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/cpe/test_api.py` & `pontos-23.4.1/tests/nvd/cpe/test_api.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/cve/__init__.py` & `pontos-23.4.1/tests/nvd/cve/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/cve/test_api.py` & `pontos-23.4.1/tests/nvd/cve/test_api.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/models/__init__.py` & `pontos-23.4.1/tests/nvd/models/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/models/test_cpe.py` & `pontos-23.4.1/tests/nvd/models/test_cpe.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/models/test_cve.py` & `pontos-23.4.1/tests/nvd/models/test_cve.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/nvd/test_api.py` & `pontos-23.4.1/tests/nvd/test_api.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/release/__init__.py` & `pontos-23.4.1/tests/release/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/release/test_helper.py` & `pontos-23.4.1/tests/release/test_helper.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/release/test_parser.py` & `pontos-23.4.1/tests/release/test_parser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/release/test_release.py` & `pontos-23.4.1/tests/release/test_release.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/release/test_sign.py` & `pontos-23.4.1/tests/release/test_sign.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/terminal/__init__.py` & `pontos-23.4.1/tests/terminal/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/terminal/test_terminal.py` & `pontos-23.4.1/tests/terminal/test_terminal.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/test_helper.py` & `pontos-23.4.1/tests/test_helper.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/test_pontos.py` & `pontos-23.4.1/tests/test_pontos.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/testing/__init__.py` & `pontos-23.4.1/tests/testing/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/testing/test_testing.py` & `pontos-23.4.1/tests/testing/test_testing.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/updateheader/__init__.py` & `pontos-23.4.1/tests/updateheader/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/updateheader/test_header.py` & `pontos-23.4.1/tests/updateheader/test_header.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/__init__.py` & `pontos-23.4.1/tests/version/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/commands/__init__.py` & `pontos-23.4.1/tests/version/commands/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/commands/test_cmake.py` & `pontos-23.4.1/tests/version/commands/test_cmake.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/commands/test_go.py` & `pontos-23.4.1/tests/version/commands/test_go.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,15 +17,14 @@
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 import unittest
 from dataclasses import dataclass
 from pathlib import Path
 from unittest.mock import MagicMock, patch
 
-from pontos.git.git import Git
 from pontos.testing import temp_directory, temp_file
 from pontos.version import VersionError
 from pontos.version.commands._go import GoVersionCommand
 from pontos.version.schemes import SemanticVersioningScheme
 
 
 @dataclass
@@ -167,40 +166,33 @@
                 VersionError,
                 "^No version.go file found. This file is required for pontos",
             ):
                 cmd.verify_version(version=None)
 
 
 class UpdateGoVersionCommandTestCase(unittest.TestCase):
-    def test_no_file_but_tag_update_version(self):
+    def test_no_file_update_version(self):
         with temp_directory(change_into=True) as temp:
             go_mod = temp / "go.mod"
             go_mod.touch()
-            with patch.object(
-                Git,
-                "list_tags",
-                MagicMock(return_value=["21.0.1"]),
-            ):
-                version = SemanticVersioningScheme.parse_version("22.2.2")
-                updated_version_obj = GoVersionCommand(
-                    SemanticVersioningScheme
-                ).update_version(version)
-                version_file_path = Path(VERSION_FILE_PATH)
-                content = version_file_path.read_text(encoding="utf-8")
-
-                self.assertIn(str(version), content)
-
-                self.assertEqual(
-                    updated_version_obj.previous,
-                    SemanticVersioningScheme.parse_version("21.0.1"),
-                )
-                self.assertEqual(updated_version_obj.new, version)
-                self.assertEqual(
-                    updated_version_obj.changed_files, [version_file_path]
-                )
+
+            version = SemanticVersioningScheme.parse_version("22.2.2")
+            updated_version_obj = GoVersionCommand(
+                SemanticVersioningScheme
+            ).update_version(version)
+            version_file_path = Path(VERSION_FILE_PATH)
+            content = version_file_path.read_text(encoding="utf-8")
+
+            self.assertIn(str(version), content)
+
+            self.assertIsNone(updated_version_obj.previous)
+            self.assertEqual(updated_version_obj.new, version)
+            self.assertEqual(
+                updated_version_obj.changed_files, [version_file_path]
+            )
 
     def test_update_version(self):
         with temp_file(name="go.mod", change_into=True):
             cmd = GoVersionCommand(SemanticVersioningScheme)
             version = SemanticVersioningScheme.parse_version("22.2.2")
             version_file_path = Path(VERSION_FILE_PATH)
             version_file_path.write_text(
```

### Comparing `pontos-23.4.0/tests/version/commands/test_javascript.py` & `pontos-23.4.1/tests/version/commands/test_javascript.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/commands/test_python.py` & `pontos-23.4.1/tests/version/commands/test_python.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/schemes/__init__.py` & `pontos-23.4.1/tests/version/schemes/__init__.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/schemes/test_pep440.py` & `pontos-23.4.1/tests/version/schemes/test_pep440.py`

 * *Files 1% similar despite different names*

```diff
@@ -119,14 +119,15 @@
             self.assertFalse(
                 Version.from_string(version1) == Version.from_string(version2),
                 f"{version1} equals {version2}",
             )
 
         versions = [
             ("1.0.0", "abc"),
+            ("1.0.0", None),
         ]
         for version1, version2 in versions:
             self.assertFalse(Version.from_string(version1) == version2)
 
         versions = [
             ("1.0.0", object()),
             ("1.0.0", 1),
@@ -215,14 +216,15 @@
             self.assertTrue(
                 Version.from_string(version1) != Version.from_string(version2),
                 f"{version1} equals {version2}",
             )
 
         versions = [
             ("1.0.0", "abc"),
+            ("1.0.0", None),
         ]
         for version1, version2 in versions:
             self.assertTrue(Version.from_string(version1) != version2)
 
         versions = [
             ("1.0.0", object()),
             ("1.0.0", 1),
```

### Comparing `pontos-23.4.0/tests/version/schemes/test_semantic.py` & `pontos-23.4.1/tests/version/schemes/test_semantic.py`

 * *Files 0% similar despite different names*

```diff
@@ -101,15 +101,15 @@
 
         versions = [
             ("1.0.0", "1.0.1"),
             ("1.0.0", "1.0.0+dev1"),
             ("1.0.0", "1.0.0-alpha1"),
             ("1.0.0", "1.0.0-alpha1"),
             ("1.0.0", "1.0.0-beta1"),
-            ("1.0.0+dev1", "1.0.0-dev1"),  # maybe both should be equal
+            ("1.0.0+dev1", "1.0.0-dev1"),
             ("1.0.0+dev1", "1.0.0+dev2"),
             ("1.0.0-alpha1", "1.0.0-beta1"),
             ("1.0.0-alpha1", "1.0.0-alpha1+dev1"),
             ("1.0.0-alpha1+dev1", "1.0.0-alpha1+dev2"),
             ("1.0.0-beta1", "1.0.0-beta1+dev1"),
             ("1.0.0-beta1+dev1", "1.0.0-beta1+dev2"),
             ("1.0.0-rc1", "1.0.0-rc1+dev1"),
@@ -117,14 +117,17 @@
         ]
         for version1, version2 in versions:
             self.assertFalse(
                 Version.from_string(version1) == Version.from_string(version2),
                 f"{version1} equals {version2}",
             )
 
+        other = None
+        self.assertFalse(Version.from_string("1.0.0") == other)
+
         versions = [
             ("1.0.0", object()),
             ("1.0.0", 1),
             ("1.0.0", True),
         ]
         for version1, version2 in versions:
             with self.assertRaisesRegex(ValueError, "Can't compare"):
@@ -189,14 +192,15 @@
             self.assertTrue(
                 Version.from_string(version1) != Version.from_string(version2),
                 f"{version1} equals {version2}",
             )
 
         versions = [
             ("1.0.0", "abc"),
+            ("1.0.0", None),
         ]
         for version1, version2 in versions:
             self.assertTrue(Version.from_string(version1) != version2)
 
         versions = [
             ("1.0.0", object()),
             ("1.0.0", 1),
```

### Comparing `pontos-23.4.0/tests/version/test_commands.py` & `pontos-23.4.1/tests/version/test_commands.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/test_errors.py` & `pontos-23.4.1/tests/version/test_errors.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/test_helper.py` & `pontos-23.4.1/tests/version/test_helper.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/test_main.py` & `pontos-23.4.1/tests/version/test_main.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/test_parser.py` & `pontos-23.4.1/tests/version/test_parser.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/test_project.py` & `pontos-23.4.1/tests/version/test_project.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/tests/version/test_version.py` & `pontos-23.4.1/tests/version/test_version.py`

 * *Files identical despite different names*

### Comparing `pontos-23.4.0/PKG-INFO` & `pontos-23.4.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pontos
-Version: 23.4.0
+Version: 23.4.1
 Summary: Common utilities and tools maintained by Greenbone Networks
 Home-page: https://github.com/greenbone/pontos/
 License: GPL-3.0-or-later
 Author: Greenbone AG
 Author-email: info@greenbone.net
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 4 - Beta
```

