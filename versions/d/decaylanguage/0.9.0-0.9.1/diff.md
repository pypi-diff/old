# Comparing `tmp/DecayLanguage-0.9.0.tar.gz` & `tmp/DecayLanguage-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/DecayLanguage-0.9.0.tar", last modified: Sat Oct 31 09:03:33 2020, max compression
+gzip compressed data, was "dist/DecayLanguage-0.9.1.tar", last modified: Wed Nov  4 23:15:57 2020, max compression
```

## Comparing `DecayLanguage-0.9.0.tar` & `DecayLanguage-0.9.1.tar`

### file list

```diff
@@ -1,162 +1,163 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.428049 DecayLanguage-0.9.0/
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.412049 DecayLanguage-0.9.0/.ci/
--rw-r--r--   0 runner    (1001) docker     (116)      690 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/.ci/azure-steps.yml
--rw-r--r--   0 runner    (1001) docker     (116)      257 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/.coveragerc
--rw-r--r--   0 runner    (1001) docker     (116)      215 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/.editorconfig
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.408049 DecayLanguage-0.9.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.412049 DecayLanguage-0.9.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (116)      618 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/.github/workflows/ci.yml
--rw-r--r--   0 runner    (1001) docker     (116)     1092 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/.github/workflows/wheel.yml
--rw-r--r--   0 runner    (1001) docker     (116)      612 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/.gitignore
--rw-r--r--   0 runner    (1001) docker     (116)      139 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/AUTHORS.rst
--rw-r--r--   0 runner    (1001) docker     (116)     4290 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (116)     2752 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/CONTRIBUTING.rst
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.412049 DecayLanguage-0.9.0/DecayLanguage.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)    17987 2020-10-31 09:03:32.000000 DecayLanguage-0.9.0/DecayLanguage.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     4317 2020-10-31 09:03:33.000000 DecayLanguage-0.9.0/DecayLanguage.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2020-10-31 09:03:32.000000 DecayLanguage-0.9.0/DecayLanguage.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)      317 2020-10-31 09:03:32.000000 DecayLanguage-0.9.0/DecayLanguage.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (116)       14 2020-10-31 09:03:32.000000 DecayLanguage-0.9.0/DecayLanguage.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (116)     1537 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (116)      677 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (116)    17987 2020-10-31 09:03:33.428049 DecayLanguage-0.9.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)    10816 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/README.md
--rw-r--r--   0 runner    (1001) docker     (116)      506 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/README_dev.md
--rw-r--r--   0 runner    (1001) docker     (116)     1031 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/azure-pipelines.yml
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.412049 DecayLanguage-0.9.0/decaylanguage/
--rw-r--r--   0 runner    (1001) docker     (116)      559 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (116)      766 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/__main__.py
--rw-r--r--   0 runner    (1001) docker     (116)      291 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.416049 DecayLanguage-0.9.0/decaylanguage/data/
--rw-r--r--   0 runner    (1001) docker     (116)   513973 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/DECAY_BELLE2.DEC
--rw-r--r--   0 runner    (1001) docker     (116)   559864 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/DECAY_LHCB.DEC
--rw-r--r--   0 runner    (1001) docker     (116)     3050 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/MintDalitzSpecialParticles.csv
--rw-r--r--   0 runner    (1001) docker     (116)     4331 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/MintDalitzSpecialParticles.fwf
--rw-r--r--   0 runner    (1001) docker     (116)      631 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv
--rw-r--r--   0 runner    (1001) docker     (116)     1675 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/README.rst
--rw-r--r--   0 runner    (1001) docker     (116)    24526 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/WorkingOutModel.ipynb
--rw-r--r--   0 runner    (1001) docker     (116)      117 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     1662 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/ampgen.lark
--rw-r--r--   0 runner    (1001) docker     (116)     2271 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/decfile.lark
--rw-r--r--   0 runner    (1001) docker     (116)      568 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/data/particle.lark
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.416049 DecayLanguage-0.9.0/decaylanguage/dec/
--rw-r--r--   0 runner    (1001) docker     (116)       70 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/dec/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)    45445 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/dec/dec.py
--rw-r--r--   0 runner    (1001) docker     (116)    13348 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/dec/decparser.py
--rw-r--r--   0 runner    (1001) docker     (116)     1323 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/dec/enums.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.416049 DecayLanguage-0.9.0/decaylanguage/decay/
--rw-r--r--   0 runner    (1001) docker     (116)       95 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/decay/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)    21101 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/decay/decay.py
--rw-r--r--   0 runner    (1001) docker     (116)     8183 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/decay/viewer.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.416049 DecayLanguage-0.9.0/decaylanguage/modeling/
--rw-r--r--   0 runner    (1001) docker     (116)    95683 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/modeling/AmpGenReader.ipynb
--rw-r--r--   0 runner    (1001) docker     (116)      106 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/modeling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     2699 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/modeling/ampgen2goofit.py
--rw-r--r--   0 runner    (1001) docker     (116)     1868 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/modeling/ampgentransform.py
--rw-r--r--   0 runner    (1001) docker     (116)     9116 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/modeling/amplitudechain.py
--rw-r--r--   0 runner    (1001) docker     (116)     3417 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/modeling/decay.py
--rw-r--r--   0 runner    (1001) docker     (116)    13659 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/modeling/goofit.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.416049 DecayLanguage-0.9.0/decaylanguage/utils/
--rw-r--r--   0 runner    (1001) docker     (116)      282 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)      500 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/utils/errors.py
--rw-r--r--   0 runner    (1001) docker     (116)     2247 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/utils/particleutils.py
--rw-r--r--   0 runner    (1001) docker     (116)     1447 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/decaylanguage/utils/utilities.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.416049 DecayLanguage-0.9.0/docs/
--rw-r--r--   0 runner    (1001) docker     (116)       28 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/authors.rst
--rw-r--r--   0 runner    (1001) docker     (116)       31 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/changelog.rst
--rw-r--r--   0 runner    (1001) docker     (116)     1393 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (116)       33 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/contributing.rst
--rw-r--r--   0 runner    (1001) docker     (116)      245 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (116)      166 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/installation.rst
--rw-r--r--   0 runner    (1001) docker     (116)       28 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/readme.rst
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.420049 DecayLanguage-0.9.0/docs/reference/
--rw-r--r--   0 runner    (1001) docker     (116)      789 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/reference/decaylanguage.decay.rst
--rw-r--r--   0 runner    (1001) docker     (116)      122 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/reference/decaylanguage.rst
--rw-r--r--   0 runner    (1001) docker     (116)       65 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/reference/index.rst
--rw-r--r--   0 runner    (1001) docker     (116)       34 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (116)      109 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/spelling_wordlist.txt
--rw-r--r--   0 runner    (1001) docker     (116)      761 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/docs/usage.rst
--rw-r--r--   0 runner    (1001) docker     (116)      300 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/environment.yml
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.420049 DecayLanguage-0.9.0/images/
--rw-r--r--   0 runner    (1001) docker     (116)    30187 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/images/DecayChain_Dst_stable-D0-and-D+.png
--rw-r--r--   0 runner    (1001) docker     (116)     3990 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/images/DecayLanguage.ink.svg
--rw-r--r--   0 runner    (1001) docker     (116)     3412 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/images/DecayLanguage.pdf
--rw-r--r--   0 runner    (1001) docker     (116)    47780 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/images/DecayLanguage.png
--rw-r--r--   0 runner    (1001) docker     (116)     2705 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/images/DecayLanguage.svg
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.420049 DecayLanguage-0.9.0/models/
--rw-r--r--   0 runner    (1001) docker     (116)    21024 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/models/DtoKpipipi_v2.txt
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.420049 DecayLanguage-0.9.0/notebooks/
--rw-r--r--   0 runner    (1001) docker     (116)   117126 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/AmpGen2GooFit D2K3p.ipynb
--rw-r--r--   0 runner    (1001) docker     (116)    23973 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/DecReader.ipynb
--rw-r--r--   0 runner    (1001) docker     (116)     7952 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/DecayLanguageDemo.ipynb
--rw-r--r--   0 runner    (1001) docker     (116)    76451 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/DtoKpipipi_v2.cu
--rw-r--r--   0 runner    (1001) docker     (116)   254543 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/ExampleDecFileParsingWithLark.ipynb
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.420049 DecayLanguage-0.9.0/notebooks/decaylanguage/
--rw-r--r--   0 runner    (1001) docker     (116)      559 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (116)      766 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/__main__.py
--rw-r--r--   0 runner    (1001) docker     (116)      291 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.424049 DecayLanguage-0.9.0/notebooks/decaylanguage/data/
--rw-r--r--   0 runner    (1001) docker     (116)   513973 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/DECAY_BELLE2.DEC
--rw-r--r--   0 runner    (1001) docker     (116)   559864 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/DECAY_LHCB.DEC
--rw-r--r--   0 runner    (1001) docker     (116)     3050 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/MintDalitzSpecialParticles.csv
--rw-r--r--   0 runner    (1001) docker     (116)     4331 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/MintDalitzSpecialParticles.fwf
--rw-r--r--   0 runner    (1001) docker     (116)      631 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv
--rw-r--r--   0 runner    (1001) docker     (116)     1675 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/README.rst
--rw-r--r--   0 runner    (1001) docker     (116)    24526 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/WorkingOutModel.ipynb
--rw-r--r--   0 runner    (1001) docker     (116)      117 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     1662 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/ampgen.lark
--rw-r--r--   0 runner    (1001) docker     (116)     2271 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/decfile.lark
--rw-r--r--   0 runner    (1001) docker     (116)      568 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/data/particle.lark
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.424049 DecayLanguage-0.9.0/notebooks/decaylanguage/dec/
--rw-r--r--   0 runner    (1001) docker     (116)       70 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/dec/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)    45445 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/dec/dec.py
--rw-r--r--   0 runner    (1001) docker     (116)    13348 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/dec/decparser.py
--rw-r--r--   0 runner    (1001) docker     (116)     1323 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/dec/enums.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.424049 DecayLanguage-0.9.0/notebooks/decaylanguage/decay/
--rw-r--r--   0 runner    (1001) docker     (116)       95 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/decay/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)    21101 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/decay/decay.py
--rw-r--r--   0 runner    (1001) docker     (116)     8183 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/decay/viewer.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.424049 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/
--rw-r--r--   0 runner    (1001) docker     (116)    95683 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/AmpGenReader.ipynb
--rw-r--r--   0 runner    (1001) docker     (116)      106 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     2699 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/ampgen2goofit.py
--rw-r--r--   0 runner    (1001) docker     (116)     1868 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/ampgentransform.py
--rw-r--r--   0 runner    (1001) docker     (116)     9116 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/amplitudechain.py
--rw-r--r--   0 runner    (1001) docker     (116)     3417 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/decay.py
--rw-r--r--   0 runner    (1001) docker     (116)    13659 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/goofit.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.424049 DecayLanguage-0.9.0/notebooks/decaylanguage/utils/
--rw-r--r--   0 runner    (1001) docker     (116)      282 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)      500 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/utils/errors.py
--rw-r--r--   0 runner    (1001) docker     (116)     2247 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/utils/particleutils.py
--rw-r--r--   0 runner    (1001) docker     (116)     1447 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/decaylanguage/utils/utilities.py
--rw-r--r--   0 runner    (1001) docker     (116)      578 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/notebooks/simple_model.txt
--rw-r--r--   0 runner    (1001) docker     (116)      532 2020-10-31 09:03:33.428049 DecayLanguage-0.9.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)     3269 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.424049 DecayLanguage-0.9.0/tests/
--rw-r--r--   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.428049 DecayLanguage-0.9.0/tests/data/
--rw-r--r--   0 runner    (1001) docker     (116)      222 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/README.rst
--rw-r--r--   0 runner    (1001) docker     (116)     9854 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/defs-aliases-chargeconj.dec
--rw-r--r--   0 runner    (1001) docker     (116)     1415 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/duplicate-decays.dec
--rw-r--r--   0 runner    (1001) docker     (116)      485 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Bc2BsPi_Bs2KK.dec
--rw-r--r--   0 runner    (1001) docker     (116)     1228 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Bd2DDst_Ds2DmPi0.dec
--rw-r--r--   0 runner    (1001) docker     (116)     3584 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Bd2DMuNu.dec
--rw-r--r--   0 runner    (1001) docker     (116)     1001 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Bd2DmTauNu_Dm23PiPi0_Tau2MuNu.dec
--rw-r--r--   0 runner    (1001) docker     (116)     4244 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Bd2Dst0X_D02KPi.dec
--rw-r--r--   0 runner    (1001) docker     (116)     2392 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Bd2DstDst.dec
--rw-r--r--   0 runner    (1001) docker     (116)      195 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Upsilon4S2B0B0bar.dec
--rw-r--r--   0 runner    (1001) docker     (116)      305 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_Xicc2XicPiPi.dec
--rw-r--r--   0 runner    (1001) docker     (116)      827 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_example_Dst.dec
--rw-r--r--   0 runner    (1001) docker     (116)     2219 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/data/test_issue90.dec
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.428049 DecayLanguage-0.9.0/tests/dec/
--rw-r--r--   0 runner    (1001) docker     (116)    16766 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/dec/test_dec.py
--rw-r--r--   0 runner    (1001) docker     (116)      565 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/dec/test_issues.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.428049 DecayLanguage-0.9.0/tests/decay/
--rw-r--r--   0 runner    (1001) docker     (116)     7240 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/decay/test_decay.py
--rw-r--r--   0 runner    (1001) docker     (116)     3954 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/decay/test_viewer.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-10-31 09:03:33.428049 DecayLanguage-0.9.0/tests/output/
--rw-r--r--   0 runner    (1001) docker     (116)    76475 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/output/DtoKpipipi_v2.cu
--rw-r--r--   0 runner    (1001) docker     (116)      760 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (116)     1871 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/test_dec_full.py
--rw-r--r--   0 runner    (1001) docker     (116)      284 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/test_decaylanguage.py
--rw-r--r--   0 runner    (1001) docker     (116)      896 2020-10-31 09:03:26.000000 DecayLanguage-0.9.0/tests/test_goofit.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.989664 DecayLanguage-0.9.1/
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.977664 DecayLanguage-0.9.1/.ci/
+-rw-r--r--   0 runner    (1001) docker     (116)      690 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/.ci/azure-steps.yml
+-rw-r--r--   0 runner    (1001) docker     (116)      257 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/.coveragerc
+-rw-r--r--   0 runner    (1001) docker     (116)      215 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/.editorconfig
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.973664 DecayLanguage-0.9.1/.github/
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.977664 DecayLanguage-0.9.1/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (116)      618 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/.github/workflows/ci.yml
+-rw-r--r--   0 runner    (1001) docker     (116)     1092 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/.github/workflows/wheel.yml
+-rw-r--r--   0 runner    (1001) docker     (116)      612 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (116)      139 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/AUTHORS.rst
+-rw-r--r--   0 runner    (1001) docker     (116)     4593 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (116)     2752 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/CONTRIBUTING.rst
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.977664 DecayLanguage-0.9.1/DecayLanguage.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (116)    18362 2020-11-04 23:15:57.000000 DecayLanguage-0.9.1/DecayLanguage.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)     4359 2020-11-04 23:15:57.000000 DecayLanguage-0.9.1/DecayLanguage.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (116)        1 2020-11-04 23:15:57.000000 DecayLanguage-0.9.1/DecayLanguage.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (116)      317 2020-11-04 23:15:57.000000 DecayLanguage-0.9.1/DecayLanguage.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       14 2020-11-04 23:15:57.000000 DecayLanguage-0.9.1/DecayLanguage.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (116)     1537 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (116)      677 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (116)    18362 2020-11-04 23:15:57.989664 DecayLanguage-0.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)    10953 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (116)      506 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/README_dev.md
+-rw-r--r--   0 runner    (1001) docker     (116)     1121 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/azure-pipelines.yml
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.977664 DecayLanguage-0.9.1/decaylanguage/
+-rw-r--r--   0 runner    (1001) docker     (116)      559 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (116)      766 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (116)      291 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.977664 DecayLanguage-0.9.1/decaylanguage/data/
+-rw-r--r--   0 runner    (1001) docker     (116)   513973 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/DECAY_BELLE2.DEC
+-rw-r--r--   0 runner    (1001) docker     (116)   559864 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/DECAY_LHCB.DEC
+-rw-r--r--   0 runner    (1001) docker     (116)     3050 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/MintDalitzSpecialParticles.csv
+-rw-r--r--   0 runner    (1001) docker     (116)     4331 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/MintDalitzSpecialParticles.fwf
+-rw-r--r--   0 runner    (1001) docker     (116)      631 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv
+-rw-r--r--   0 runner    (1001) docker     (116)     1675 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/README.rst
+-rw-r--r--   0 runner    (1001) docker     (116)    24526 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/WorkingOutModel.ipynb
+-rw-r--r--   0 runner    (1001) docker     (116)      117 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1662 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/ampgen.lark
+-rw-r--r--   0 runner    (1001) docker     (116)     2320 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/decfile.lark
+-rw-r--r--   0 runner    (1001) docker     (116)      568 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/data/particle.lark
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.977664 DecayLanguage-0.9.1/decaylanguage/dec/
+-rw-r--r--   0 runner    (1001) docker     (116)       70 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/dec/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)    48879 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/dec/dec.py
+-rw-r--r--   0 runner    (1001) docker     (116)    13348 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/dec/decparser.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1323 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/dec/enums.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.977664 DecayLanguage-0.9.1/decaylanguage/decay/
+-rw-r--r--   0 runner    (1001) docker     (116)       95 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/decay/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)    21101 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/decay/decay.py
+-rw-r--r--   0 runner    (1001) docker     (116)     8183 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/decay/viewer.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/decaylanguage/modeling/
+-rw-r--r--   0 runner    (1001) docker     (116)    95683 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/modeling/AmpGenReader.ipynb
+-rw-r--r--   0 runner    (1001) docker     (116)      106 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/modeling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2699 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/modeling/ampgen2goofit.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1868 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/modeling/ampgentransform.py
+-rw-r--r--   0 runner    (1001) docker     (116)     9116 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/modeling/amplitudechain.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3417 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/modeling/decay.py
+-rw-r--r--   0 runner    (1001) docker     (116)    13659 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/modeling/goofit.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/decaylanguage/utils/
+-rw-r--r--   0 runner    (1001) docker     (116)      282 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)      500 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/utils/errors.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2247 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/utils/particleutils.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1447 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/decaylanguage/utils/utilities.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/docs/
+-rw-r--r--   0 runner    (1001) docker     (116)       28 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/authors.rst
+-rw-r--r--   0 runner    (1001) docker     (116)       31 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/changelog.rst
+-rw-r--r--   0 runner    (1001) docker     (116)     1393 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (116)       33 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/contributing.rst
+-rw-r--r--   0 runner    (1001) docker     (116)      245 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/index.rst
+-rw-r--r--   0 runner    (1001) docker     (116)      166 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (116)       28 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/readme.rst
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/docs/reference/
+-rw-r--r--   0 runner    (1001) docker     (116)      789 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/reference/decaylanguage.decay.rst
+-rw-r--r--   0 runner    (1001) docker     (116)      122 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/reference/decaylanguage.rst
+-rw-r--r--   0 runner    (1001) docker     (116)       65 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/reference/index.rst
+-rw-r--r--   0 runner    (1001) docker     (116)       34 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (116)      109 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/spelling_wordlist.txt
+-rw-r--r--   0 runner    (1001) docker     (116)      761 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/docs/usage.rst
+-rw-r--r--   0 runner    (1001) docker     (116)      300 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/environment.yml
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/images/
+-rw-r--r--   0 runner    (1001) docker     (116)    30187 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/images/DecayChain_Dst_stable-D0-and-D+.png
+-rw-r--r--   0 runner    (1001) docker     (116)     3990 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/images/DecayLanguage.ink.svg
+-rw-r--r--   0 runner    (1001) docker     (116)     3412 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/images/DecayLanguage.pdf
+-rw-r--r--   0 runner    (1001) docker     (116)    47780 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/images/DecayLanguage.png
+-rw-r--r--   0 runner    (1001) docker     (116)     2705 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/images/DecayLanguage.svg
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/models/
+-rw-r--r--   0 runner    (1001) docker     (116)    21024 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/models/DtoKpipipi_v2.txt
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/notebooks/
+-rw-r--r--   0 runner    (1001) docker     (116)   117126 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/AmpGen2GooFit D2K3p.ipynb
+-rw-r--r--   0 runner    (1001) docker     (116)    23973 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/DecReader.ipynb
+-rw-r--r--   0 runner    (1001) docker     (116)     7952 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/DecayLanguageDemo.ipynb
+-rw-r--r--   0 runner    (1001) docker     (116)    76451 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/DtoKpipipi_v2.cu
+-rw-r--r--   0 runner    (1001) docker     (116)   254543 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/ExampleDecFileParsingWithLark.ipynb
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.981664 DecayLanguage-0.9.1/notebooks/decaylanguage/
+-rw-r--r--   0 runner    (1001) docker     (116)      559 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (116)      766 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (116)      291 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/notebooks/decaylanguage/data/
+-rw-r--r--   0 runner    (1001) docker     (116)   513973 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/DECAY_BELLE2.DEC
+-rw-r--r--   0 runner    (1001) docker     (116)   559864 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/DECAY_LHCB.DEC
+-rw-r--r--   0 runner    (1001) docker     (116)     3050 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/MintDalitzSpecialParticles.csv
+-rw-r--r--   0 runner    (1001) docker     (116)     4331 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/MintDalitzSpecialParticles.fwf
+-rw-r--r--   0 runner    (1001) docker     (116)      631 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv
+-rw-r--r--   0 runner    (1001) docker     (116)     1675 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/README.rst
+-rw-r--r--   0 runner    (1001) docker     (116)    24526 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/WorkingOutModel.ipynb
+-rw-r--r--   0 runner    (1001) docker     (116)      117 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1662 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/ampgen.lark
+-rw-r--r--   0 runner    (1001) docker     (116)     2320 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/decfile.lark
+-rw-r--r--   0 runner    (1001) docker     (116)      568 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/data/particle.lark
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/notebooks/decaylanguage/dec/
+-rw-r--r--   0 runner    (1001) docker     (116)       70 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/dec/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)    48879 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/dec/dec.py
+-rw-r--r--   0 runner    (1001) docker     (116)    13348 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/dec/decparser.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1323 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/dec/enums.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/notebooks/decaylanguage/decay/
+-rw-r--r--   0 runner    (1001) docker     (116)       95 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/decay/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)    21101 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/decay/decay.py
+-rw-r--r--   0 runner    (1001) docker     (116)     8183 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/decay/viewer.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/
+-rw-r--r--   0 runner    (1001) docker     (116)    95683 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/AmpGenReader.ipynb
+-rw-r--r--   0 runner    (1001) docker     (116)      106 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2699 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/ampgen2goofit.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1868 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/ampgentransform.py
+-rw-r--r--   0 runner    (1001) docker     (116)     9116 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/amplitudechain.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3417 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/decay.py
+-rw-r--r--   0 runner    (1001) docker     (116)    13659 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/goofit.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/notebooks/decaylanguage/utils/
+-rw-r--r--   0 runner    (1001) docker     (116)      282 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)      500 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/utils/errors.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2247 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/utils/particleutils.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1447 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/decaylanguage/utils/utilities.py
+-rw-r--r--   0 runner    (1001) docker     (116)      578 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/notebooks/simple_model.txt
+-rw-r--r--   0 runner    (1001) docker     (116)      532 2020-11-04 23:15:57.989664 DecayLanguage-0.9.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (116)     3269 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/tests/
+-rw-r--r--   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/tests/data/
+-rw-r--r--   0 runner    (1001) docker     (116)      222 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/README.rst
+-rw-r--r--   0 runner    (1001) docker     (116)     9854 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/defs-aliases-chargeconj.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     1415 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/duplicate-decays.dec
+-rw-r--r--   0 runner    (1001) docker     (116)      485 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Bc2BsPi_Bs2KK.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     1228 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Bd2DDst_Ds2DmPi0.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     3584 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Bd2DMuNu.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     1001 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Bd2DmTauNu_Dm23PiPi0_Tau2MuNu.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     4244 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Bd2Dst0X_D02KPi.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     2392 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Bd2DstDst.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     2366 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_CopyDecay_RemoveDecay.dec
+-rw-r--r--   0 runner    (1001) docker     (116)      195 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Upsilon4S2B0B0bar.dec
+-rw-r--r--   0 runner    (1001) docker     (116)      305 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_Xicc2XicPiPi.dec
+-rw-r--r--   0 runner    (1001) docker     (116)      827 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_example_Dst.dec
+-rw-r--r--   0 runner    (1001) docker     (116)     2219 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/data/test_issue90.dec
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.985664 DecayLanguage-0.9.1/tests/dec/
+-rw-r--r--   0 runner    (1001) docker     (116)    17066 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/dec/test_dec.py
+-rw-r--r--   0 runner    (1001) docker     (116)      565 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/dec/test_issues.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.989664 DecayLanguage-0.9.1/tests/decay/
+-rw-r--r--   0 runner    (1001) docker     (116)     7240 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/decay/test_decay.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3954 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/decay/test_viewer.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-11-04 23:15:57.989664 DecayLanguage-0.9.1/tests/output/
+-rw-r--r--   0 runner    (1001) docker     (116)    76475 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/output/DtoKpipipi_v2.cu
+-rw-r--r--   0 runner    (1001) docker     (116)      760 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1871 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/test_dec_full.py
+-rw-r--r--   0 runner    (1001) docker     (116)      284 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/test_decaylanguage.py
+-rw-r--r--   0 runner    (1001) docker     (116)      896 2020-11-04 23:15:55.000000 DecayLanguage-0.9.1/tests/test_goofit.py
```

### Comparing `DecayLanguage-0.9.0/.ci/azure-steps.yml` & `DecayLanguage-0.9.1/.ci/azure-steps.yml`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/.github/workflows/ci.yml` & `DecayLanguage-0.9.1/.github/workflows/ci.yml`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/.github/workflows/wheel.yml` & `DecayLanguage-0.9.1/.github/workflows/wheel.yml`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/.gitignore` & `DecayLanguage-0.9.1/.gitignore`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/CHANGELOG.md` & `DecayLanguage-0.9.1/CHANGELOG.md`

 * *Files 9% similar despite different names*

```diff
@@ -1,9 +1,18 @@
 # Changelog
 
+## Version 0.9.1 (2020-11-04)
+
+* Parsing of decay files (aka .dec files):
+  - ``DecFileParser`` class enhanced to understand the CopyDecay statement.
+* Tests:
+  - Added tests for Python 3.8 and 3.9 on Windows.
+* Miscellaneous:
+  - Conda badge added to the README, since package now available in Conda.
+
 ## Version 0.9.0 (2020-10-31)
 
 * Dependencies and Python version support:
   - Package dependent on ``Particle`` version 0.13.
   - Support for Python 3.9 added.
 
 ## Version 0.8.0 (2020-09-29)
```

### Comparing `DecayLanguage-0.9.0/CONTRIBUTING.rst` & `DecayLanguage-0.9.1/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/DecayLanguage.egg-info/PKG-INFO` & `DecayLanguage-0.9.1/DecayLanguage.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DecayLanguage
-Version: 0.9.0
+Version: 0.9.1
 Summary: A language to describe particle decays, and tools to work with them.
 Home-page: https://github.com/scikit-hep/decaylanguage
 Author: Henry Fredrick Schreiner III, Eduardo Rodrigues
 Author-email: henry.schreiner@cern.ch, eduardo.rodrigues@cern.ch
 Maintainer: The Scikit-HEP admins
 Maintainer-email: scikit-hep-admins@googlegroups.com
 License: BSD 3-Clause License
@@ -271,14 +271,23 @@
         
         [AmpGen]: https://gitlab.cern.ch/lhcb/Gauss/tree/LHCBGAUSS-1058.AmpGenDev/Gen/AmpGen
         [GooFit]: https://GooFit.github.io
         
         
         # Changelog
         
+        ## Version 0.9.1 (2020-11-04)
+        
+        * Parsing of decay files (aka .dec files):
+          - ``DecFileParser`` class enhanced to understand the CopyDecay statement.
+        * Tests:
+          - Added tests for Python 3.8 and 3.9 on Windows.
+        * Miscellaneous:
+          - Conda badge added to the README, since package now available in Conda.
+        
         ## Version 0.9.0 (2020-10-31)
         
         * Dependencies and Python version support:
           - Package dependent on ``Particle`` version 0.13.
           - Support for Python 3.9 added.
         
         ## Version 0.8.0 (2020-09-29)
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: DecayLanguage Version: 0.9.0 Summary: A language to
+Metadata-Version: 2.1 Name: DecayLanguage Version: 0.9.1 Summary: A language to
 describe particle decays, and tools to work with them. Home-page: https://
 github.com/scikit-hep/decaylanguage Author: Henry Fredrick Schreiner III,
 Eduardo Rodrigues Author-email: henry.schreiner@cern.ch,
 eduardo.rodrigues@cern.ch Maintainer: The Scikit-HEP admins Maintainer-email:
 scikit-hep-admins@googlegroups.com License: BSD 3-Clause License Description:
 [https://raw.githubusercontent.com/scikit-hep/decaylanguage/master/images/
 DecayLanguage.png]
@@ -116,40 +116,44 @@
 the [GooFit] output, type from the shell: ```bash python -m decaylanguage -
 G goofit myinput.opts ``` ## Acknowledgements Support for this work was
 provided by the National Science Foundation cooperative agreement OAC-1450377
 (DIANA/HEP) and OAC-1836650 (IRIS-HEP). Any opinions, findings, conclusions or
 recommendations expressed in this material are those of the authors and do not
 necessarily reflect the views of the National Science Foundation. [AmpGen]:
 https://gitlab.cern.ch/lhcb/Gauss/tree/LHCBGAUSS-1058.AmpGenDev/Gen/AmpGen
-[GooFit]: https://GooFit.github.io # Changelog ## Version 0.9.0 (2020-10-31) *
-Dependencies and Python version support: - Package dependent on ``Particle``
-version 0.13. - Support for Python 3.9 added. ## Version 0.8.0 (2020-09-29) *
-Dependencies: - Package dependent on ``Particle`` version 0.12. ## Version
-0.7.0 (2020-08-13) * Dependencies: - Package dependent on ``Particle`` version
-0.11. - Dependencies on `lark-parser` and others upgraded. ## Version 0.6.2
-(2020-06-05) * Dependencies: - Package dependency on ``pydot`` made a
-requirement. ## Version 0.6.1 (2020-01-15) * Parsing of decay files (aka .dec
-files): - Simpifications in various methods of class ``DecFileParser``. - A
-couple more tests added. * Minor fixes. ## Version 0.6.0 (2020-01-10) * Parsing
-of decay files (aka .dec files): - Master Belle II DECAY.DEC file added to the
-package. - Certain ``DecFileParser`` class methods made more versatile. -
-``Lark`` parsing grammar file improved. * Universal representation of decay
-chains: - Classes ``DecayChain``, ``DecayMode``, ``DaughtersDict`` and
-``DecayChainViewer`` enhanced. * Dependencies and Python version support: -
-Package dependent on ``Particle`` versions 0.9.*. - Support for Python 3.8
-added. ## Version 0.5.3 (2019-10-28) * Dict-like representation of particle
-decay chains improved. * Documentation added to README. ## Version 0.5.2 (2019-
-10-23) * Parsing of decay files (aka .dec files): - New Belle II decay models
-added. * README updated to provide basic coverage of recent new features. *
-Clean-up of obsolete files. ## Version 0.5.1 (2019-10-14) * Universal
-representation of decay chains: - Classes ``DecayChain`` and ``DecayMode``
-enhanced. - Tests for class ``DecayChain`` added. * Parsing of decay files (aka
-.dec files): - ``DecFileParser`` class extended. ## Version 0.5.0 (2019-10-11)
-* Universal representation of decay chains: - Class ``DecayChain`` introduced.
-- Classes ``DaughtersDict`` and ``DecayMode`` enhanced. * Changes in API: -
+[GooFit]: https://GooFit.github.io # Changelog ## Version 0.9.1 (2020-11-04) *
+Parsing of decay files (aka .dec files): - ``DecFileParser`` class enhanced to
+understand the CopyDecay statement. * Tests: - Added tests for Python 3.8 and
+3.9 on Windows. * Miscellaneous: - Conda badge added to the README, since
+package now available in Conda. ## Version 0.9.0 (2020-10-31) * Dependencies
+and Python version support: - Package dependent on ``Particle`` version 0.13. -
+Support for Python 3.9 added. ## Version 0.8.0 (2020-09-29) * Dependencies: -
+Package dependent on ``Particle`` version 0.12. ## Version 0.7.0 (2020-08-13) *
+Dependencies: - Package dependent on ``Particle`` version 0.11. - Dependencies
+on `lark-parser` and others upgraded. ## Version 0.6.2 (2020-06-05) *
+Dependencies: - Package dependency on ``pydot`` made a requirement. ## Version
+0.6.1 (2020-01-15) * Parsing of decay files (aka .dec files): - Simpifications
+in various methods of class ``DecFileParser``. - A couple more tests added. *
+Minor fixes. ## Version 0.6.0 (2020-01-10) * Parsing of decay files (aka .dec
+files): - Master Belle II DECAY.DEC file added to the package. - Certain
+``DecFileParser`` class methods made more versatile. - ``Lark`` parsing grammar
+file improved. * Universal representation of decay chains: - Classes
+``DecayChain``, ``DecayMode``, ``DaughtersDict`` and ``DecayChainViewer``
+enhanced. * Dependencies and Python version support: - Package dependent on
+``Particle`` versions 0.9.*. - Support for Python 3.8 added. ## Version 0.5.3
+(2019-10-28) * Dict-like representation of particle decay chains improved. *
+Documentation added to README. ## Version 0.5.2 (2019-10-23) * Parsing of decay
+files (aka .dec files): - New Belle II decay models added. * README updated to
+provide basic coverage of recent new features. * Clean-up of obsolete files. ##
+Version 0.5.1 (2019-10-14) * Universal representation of decay chains: -
+Classes ``DecayChain`` and ``DecayMode`` enhanced. - Tests for class
+``DecayChain`` added. * Parsing of decay files (aka .dec files): -
+``DecFileParser`` class extended. ## Version 0.5.0 (2019-10-11) * Universal
+representation of decay chains: - Class ``DecayChain`` introduced. - Classes
+``DaughtersDict`` and ``DecayMode`` enhanced. * Changes in API: -
 ``DecFileParser.build_decay_chain()`` renamed to
 ``DecFileParser.build_decay_chains()``. * Package dependent on ``Particle``
 package version 0.6. ## Version 0.4.0 (2019-09-02) * Package dependent on
 ``Particle`` version 0.6.0. Otherwise identical to version 0.3.2. ## Version
 0.3.2 (2019-08-29) * Parsing of decay files (aka .dec files): -
 ``DecFileParser`` class extended to understand JETSET definitions. *
 Visualisation of decay chains: - ``DecayChainViewer`` class simplified and
```

### Comparing `DecayLanguage-0.9.0/DecayLanguage.egg-info/SOURCES.txt` & `DecayLanguage-0.9.1/DecayLanguage.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -120,14 +120,15 @@
 tests/data/duplicate-decays.dec
 tests/data/test_Bc2BsPi_Bs2KK.dec
 tests/data/test_Bd2DDst_Ds2DmPi0.dec
 tests/data/test_Bd2DMuNu.dec
 tests/data/test_Bd2DmTauNu_Dm23PiPi0_Tau2MuNu.dec
 tests/data/test_Bd2Dst0X_D02KPi.dec
 tests/data/test_Bd2DstDst.dec
+tests/data/test_CopyDecay_RemoveDecay.dec
 tests/data/test_Upsilon4S2B0B0bar.dec
 tests/data/test_Xicc2XicPiPi.dec
 tests/data/test_example_Dst.dec
 tests/data/test_issue90.dec
 tests/dec/test_dec.py
 tests/dec/test_issues.py
 tests/decay/test_decay.py
```

### Comparing `DecayLanguage-0.9.0/LICENSE` & `DecayLanguage-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/MANIFEST.in` & `DecayLanguage-0.9.1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/PKG-INFO` & `DecayLanguage-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DecayLanguage
-Version: 0.9.0
+Version: 0.9.1
 Summary: A language to describe particle decays, and tools to work with them.
 Home-page: https://github.com/scikit-hep/decaylanguage
 Author: Henry Fredrick Schreiner III, Eduardo Rodrigues
 Author-email: henry.schreiner@cern.ch, eduardo.rodrigues@cern.ch
 Maintainer: The Scikit-HEP admins
 Maintainer-email: scikit-hep-admins@googlegroups.com
 License: BSD 3-Clause License
@@ -271,14 +271,23 @@
         
         [AmpGen]: https://gitlab.cern.ch/lhcb/Gauss/tree/LHCBGAUSS-1058.AmpGenDev/Gen/AmpGen
         [GooFit]: https://GooFit.github.io
         
         
         # Changelog
         
+        ## Version 0.9.1 (2020-11-04)
+        
+        * Parsing of decay files (aka .dec files):
+          - ``DecFileParser`` class enhanced to understand the CopyDecay statement.
+        * Tests:
+          - Added tests for Python 3.8 and 3.9 on Windows.
+        * Miscellaneous:
+          - Conda badge added to the README, since package now available in Conda.
+        
         ## Version 0.9.0 (2020-10-31)
         
         * Dependencies and Python version support:
           - Package dependent on ``Particle`` version 0.13.
           - Support for Python 3.9 added.
         
         ## Version 0.8.0 (2020-09-29)
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: DecayLanguage Version: 0.9.0 Summary: A language to
+Metadata-Version: 2.1 Name: DecayLanguage Version: 0.9.1 Summary: A language to
 describe particle decays, and tools to work with them. Home-page: https://
 github.com/scikit-hep/decaylanguage Author: Henry Fredrick Schreiner III,
 Eduardo Rodrigues Author-email: henry.schreiner@cern.ch,
 eduardo.rodrigues@cern.ch Maintainer: The Scikit-HEP admins Maintainer-email:
 scikit-hep-admins@googlegroups.com License: BSD 3-Clause License Description:
 [https://raw.githubusercontent.com/scikit-hep/decaylanguage/master/images/
 DecayLanguage.png]
@@ -116,40 +116,44 @@
 the [GooFit] output, type from the shell: ```bash python -m decaylanguage -
 G goofit myinput.opts ``` ## Acknowledgements Support for this work was
 provided by the National Science Foundation cooperative agreement OAC-1450377
 (DIANA/HEP) and OAC-1836650 (IRIS-HEP). Any opinions, findings, conclusions or
 recommendations expressed in this material are those of the authors and do not
 necessarily reflect the views of the National Science Foundation. [AmpGen]:
 https://gitlab.cern.ch/lhcb/Gauss/tree/LHCBGAUSS-1058.AmpGenDev/Gen/AmpGen
-[GooFit]: https://GooFit.github.io # Changelog ## Version 0.9.0 (2020-10-31) *
-Dependencies and Python version support: - Package dependent on ``Particle``
-version 0.13. - Support for Python 3.9 added. ## Version 0.8.0 (2020-09-29) *
-Dependencies: - Package dependent on ``Particle`` version 0.12. ## Version
-0.7.0 (2020-08-13) * Dependencies: - Package dependent on ``Particle`` version
-0.11. - Dependencies on `lark-parser` and others upgraded. ## Version 0.6.2
-(2020-06-05) * Dependencies: - Package dependency on ``pydot`` made a
-requirement. ## Version 0.6.1 (2020-01-15) * Parsing of decay files (aka .dec
-files): - Simpifications in various methods of class ``DecFileParser``. - A
-couple more tests added. * Minor fixes. ## Version 0.6.0 (2020-01-10) * Parsing
-of decay files (aka .dec files): - Master Belle II DECAY.DEC file added to the
-package. - Certain ``DecFileParser`` class methods made more versatile. -
-``Lark`` parsing grammar file improved. * Universal representation of decay
-chains: - Classes ``DecayChain``, ``DecayMode``, ``DaughtersDict`` and
-``DecayChainViewer`` enhanced. * Dependencies and Python version support: -
-Package dependent on ``Particle`` versions 0.9.*. - Support for Python 3.8
-added. ## Version 0.5.3 (2019-10-28) * Dict-like representation of particle
-decay chains improved. * Documentation added to README. ## Version 0.5.2 (2019-
-10-23) * Parsing of decay files (aka .dec files): - New Belle II decay models
-added. * README updated to provide basic coverage of recent new features. *
-Clean-up of obsolete files. ## Version 0.5.1 (2019-10-14) * Universal
-representation of decay chains: - Classes ``DecayChain`` and ``DecayMode``
-enhanced. - Tests for class ``DecayChain`` added. * Parsing of decay files (aka
-.dec files): - ``DecFileParser`` class extended. ## Version 0.5.0 (2019-10-11)
-* Universal representation of decay chains: - Class ``DecayChain`` introduced.
-- Classes ``DaughtersDict`` and ``DecayMode`` enhanced. * Changes in API: -
+[GooFit]: https://GooFit.github.io # Changelog ## Version 0.9.1 (2020-11-04) *
+Parsing of decay files (aka .dec files): - ``DecFileParser`` class enhanced to
+understand the CopyDecay statement. * Tests: - Added tests for Python 3.8 and
+3.9 on Windows. * Miscellaneous: - Conda badge added to the README, since
+package now available in Conda. ## Version 0.9.0 (2020-10-31) * Dependencies
+and Python version support: - Package dependent on ``Particle`` version 0.13. -
+Support for Python 3.9 added. ## Version 0.8.0 (2020-09-29) * Dependencies: -
+Package dependent on ``Particle`` version 0.12. ## Version 0.7.0 (2020-08-13) *
+Dependencies: - Package dependent on ``Particle`` version 0.11. - Dependencies
+on `lark-parser` and others upgraded. ## Version 0.6.2 (2020-06-05) *
+Dependencies: - Package dependency on ``pydot`` made a requirement. ## Version
+0.6.1 (2020-01-15) * Parsing of decay files (aka .dec files): - Simpifications
+in various methods of class ``DecFileParser``. - A couple more tests added. *
+Minor fixes. ## Version 0.6.0 (2020-01-10) * Parsing of decay files (aka .dec
+files): - Master Belle II DECAY.DEC file added to the package. - Certain
+``DecFileParser`` class methods made more versatile. - ``Lark`` parsing grammar
+file improved. * Universal representation of decay chains: - Classes
+``DecayChain``, ``DecayMode``, ``DaughtersDict`` and ``DecayChainViewer``
+enhanced. * Dependencies and Python version support: - Package dependent on
+``Particle`` versions 0.9.*. - Support for Python 3.8 added. ## Version 0.5.3
+(2019-10-28) * Dict-like representation of particle decay chains improved. *
+Documentation added to README. ## Version 0.5.2 (2019-10-23) * Parsing of decay
+files (aka .dec files): - New Belle II decay models added. * README updated to
+provide basic coverage of recent new features. * Clean-up of obsolete files. ##
+Version 0.5.1 (2019-10-14) * Universal representation of decay chains: -
+Classes ``DecayChain`` and ``DecayMode`` enhanced. - Tests for class
+``DecayChain`` added. * Parsing of decay files (aka .dec files): -
+``DecFileParser`` class extended. ## Version 0.5.0 (2019-10-11) * Universal
+representation of decay chains: - Class ``DecayChain`` introduced. - Classes
+``DaughtersDict`` and ``DecayMode`` enhanced. * Changes in API: -
 ``DecFileParser.build_decay_chain()`` renamed to
 ``DecFileParser.build_decay_chains()``. * Package dependent on ``Particle``
 package version 0.6. ## Version 0.4.0 (2019-09-02) * Package dependent on
 ``Particle`` version 0.6.0. Otherwise identical to version 0.3.2. ## Version
 0.3.2 (2019-08-29) * Parsing of decay files (aka .dec files): -
 ``DecFileParser`` class extended to understand JETSET definitions. *
 Visualisation of decay chains: - ``DecayChainViewer`` class simplified and
```

### Comparing `DecayLanguage-0.9.0/README.md` & `DecayLanguage-0.9.1/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 [![DecayLanguage](https://raw.githubusercontent.com/scikit-hep/decaylanguage/master/images/DecayLanguage.png)](https://decaylanguage.readthedocs.io/en/latest/)
 
 # DecayLanguage: describe, manipulate and convert particle decays
 
 [![Scikit-HEP](https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg)](https://scikit-hep.org/)
 [![PyPI Package latest release](https://img.shields.io/pypi/v/decaylanguage.svg)](https://pypi.python.org/pypi/decaylanguage)
+[![Conda latest release](https://img.shields.io/conda/vn/conda-forge/decaylanguage.svg)](https://anaconda.org/conda-forge/decaylanguage)
 [![Supported versions](https://img.shields.io/pypi/pyversions/decaylanguage.svg)](https://pypi.python.org/pypi/decaylanguage)
 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3257423.svg)](https://doi.org/10.5281/zenodo.3257423)
 
 [![CI](https://github.com/scikit-hep/decaylanguage/workflows/CI/badge.svg)](https://github.com/scikit-hep/decaylanguage/actions)
 [![Azure Build Status](https://dev.azure.com/scikit-hep/decaylanguage/_apis/build/status/scikit-hep.decaylanguage?branchName=master)](https://dev.azure.com/scikit-hep/decaylanguage/_build/latest?definitionId=3?branchName=master)
 [![Coverage Status](https://img.shields.io/azure-devops/coverage/scikit-hep/decaylanguage/3.svg)](https://dev.azure.com/scikit-hep/decaylanguage/_build/latest?definitionId=3?branchName=master)
 [![Tests Status](https://img.shields.io/azure-devops/tests/scikit-hep/decaylanguage/3.svg)](https://dev.azure.com/scikit-hep/decaylanguage/_build/latest?definitionId=3?branchName=master)
```

### Comparing `DecayLanguage-0.9.0/azure-pipelines.yml` & `DecayLanguage-0.9.1/azure-pipelines.yml`

 * *Files 4% similar despite different names*

```diff
@@ -9,16 +9,16 @@
 jobs:
 
 - job: 'Linux'
   pool:
     vmImage: 'ubuntu-latest'
   strategy:
     matrix:
-#      Python27:
-#        python.version: '2.7'
+      Python27:
+        python.version: '2.7'
       Python35:
         python.version: '3.5'
       Python36:
         python.version: '3.6'
       Python37:
         python.version: '3.7'
 
@@ -30,14 +30,18 @@
     vmImage: 'vs2017-win2016'
   strategy:
     matrix:
       Python27:
         python.version: '2.7'
       Python37:
         python.version: '3.7'
+      Python38:
+        python.version: '3.8'
+      Python39:
+        python.version: '3.9'
 
   steps:
     - template: .ci/azure-steps.yml
 
 - job: 'macOS'
   pool:
     vmImage: 'macOS-latest'
```

### Comparing `DecayLanguage-0.9.0/decaylanguage/__init__.py` & `DecayLanguage-0.9.1/decaylanguage/__init__.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/__main__.py` & `DecayLanguage-0.9.1/decaylanguage/__main__.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/DECAY_BELLE2.DEC` & `DecayLanguage-0.9.1/decaylanguage/data/DECAY_BELLE2.DEC`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/DECAY_LHCB.DEC` & `DecayLanguage-0.9.1/decaylanguage/data/DECAY_LHCB.DEC`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/MintDalitzSpecialParticles.csv` & `DecayLanguage-0.9.1/decaylanguage/data/MintDalitzSpecialParticles.csv`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/MintDalitzSpecialParticles.fwf` & `DecayLanguage-0.9.1/decaylanguage/data/MintDalitzSpecialParticles.fwf`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv` & `DecayLanguage-0.9.1/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/README.rst` & `DecayLanguage-0.9.1/decaylanguage/data/README.rst`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/WorkingOutModel.ipynb` & `DecayLanguage-0.9.1/decaylanguage/data/WorkingOutModel.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/ampgen.lark` & `DecayLanguage-0.9.1/decaylanguage/data/ampgen.lark`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/decfile.lark` & `DecayLanguage-0.9.1/decaylanguage/data/decfile.lark`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 // Copyright (c) 2018-2020, Eduardo Rodrigues and Henry Schreiner.
 //
 // Distributed under the 3-clause BSD license, see accompanying file LICENSE
 // or https://github.com/scikit-hep/decaylanguage for details.
 
 start : _NEWLINE* (line _NEWLINE+)+ ("End" _NEWLINE+)?
-?line : define | pythia_def | jetset_def | alias | chargeconj | commands | decay | cdecay | setlspw
+?line : define | pythia_def | jetset_def | alias | chargeconj | commands | decay | cdecay | copydecay | setlspw
 
 pythia_def : "PythiaBothParam" LABEL ":" LABEL "=" (LABEL | SIGNED_NUMBER)
 
 jetset_def : "JetSetPar" LABEL "=" SIGNED_NUMBER
 
 setlspw : "SetLineshapePW" label label label value
 
@@ -28,14 +28,16 @@
                 | "noPhotos"  -> no
 
 decay : "Decay" particle _NEWLINE+ decayline+ "Enddecay"
 decayline : value particle* photos? model (_NEWLINE | _SEMICOLON)+ // There is always a ; here
 value : SIGNED_NUMBER
 photos : "PHOTOS"
 
+copydecay : "CopyDecay" label label
+
 label : LABEL
 particle : LABEL // Add full particle parsing here
 
 model : MODEL_NAME model_options?
 model_options : (value | LABEL | _NEWLINE)+
 
 // model : model_generic
```

### Comparing `DecayLanguage-0.9.0/decaylanguage/data/particle.lark` & `DecayLanguage-0.9.1/decaylanguage/data/particle.lark`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/dec/dec.py` & `DecayLanguage-0.9.1/decaylanguage/dec/dec.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,18 +5,19 @@
 
 """
 Submodule with classes and utilities to deal with and parse .dec decay files.
 
 Basic assumptions
 -----------------
 
-1) For standard (non-alias) particle (names):
+1) For standard particle names *not defined* via aliases:
     - Decay modes defined via a 'Decay' statement.
     - Related antiparticle decay modes either defined via a 'CDecay' statement
       or via a 'Decay' statement. The latter option is often used if CP matters.
+
 2) For particle names defined via aliases:
     - Particle decay modes defined as above.
     - Related antiparticle decay modes defined with either options above,
       *but* there needs to be a 'ChargeConj' statement specifying the
       particle-antiparticle match. Typically::
 
         Alias MyP+ P+
@@ -25,14 +26,18 @@
         Decay MyP+
         ...
         Enddecay
         CDecay MyP-
 
 3) As a consequence, particles that are self-conjugate should not be used
    in 'CDecay' statements, obviously.
+
+ 4) Decays defined via a 'CopyDecay' statement are simply (deep) copied
+    and no copy of the corresponding antiparticle is performed unless explicitly requested
+    with another 'CopyDecay' statement.
 """
 
 from __future__ import absolute_import, division, print_function
 
 import os
 import warnings
 import re
@@ -71,15 +76,16 @@
 
 class DecFileParser(object):
     """
     The class to parse a .dec decay file.
 
     Example
     -------
-    >>> parsed_file = DecFileParser('my-decay-file.dec')
+    >>> dfp = DecFileParser('my-decay-file.dec')
+    >>> dfp.parse()
     """
 
     __slots__ = ("_grammar",
                  "_grammar_info",
                  "_dec_file_names",
                  "_dec_file",
                  "_parsed_dec_file",
@@ -149,21 +155,20 @@
         _cls._dec_file_names = '<dec file input as a string>'
         _cls._dec_file = stream.read()
 
         return _cls
 
     def parse(self, include_ccdecays=True):
         """
-        Parse the given .dec decay file according to default Lark parser
-        and specified options, i.e.,
-            parser = 'lalr',
-            lexer = 'standard'.
+        Parse the given .dec decay file(s) according to the default Lark parser
+        and specified options.
 
         See method 'load_grammar' for how to explicitly define the grammar
-        and set the Lark parsing options.
+        and set the Lark parsing options. This method needs to be called
+        before 'parse' to override the parser and its options.
 
         Parameters
         ----------
         include_ccdecays: boolean, optional, default=True
             Choose whether or not to consider charge-conjugate decays,
             which are specified via "CDecay <MOTHER>".
             Make sure you understand the consequences of ignoring
@@ -194,37 +199,43 @@
         # variable names with actual values provided via 'Define' statements,
         # and perform the replacements name -> value where relevant.
         # Do also a replacement of 'a_float' with a_float.
         dict_define_defs = self.dict_definitions()
         for tree in self._parsed_decays:
             DecayModelParamValueReplacement(define_defs=dict_define_defs).visit(tree)
 
-        # ... and create on the fly the charge conjugate decays, if requested
+        # Create on the fly the decays to be copied, if requested
+        if self.dict_decays2copy():
+            self._add_decays_to_be_copied()
+
+        # Create on the fly the charge conjugate decays, if requested
         if self._include_ccdecays:
             self._add_charge_conjugate_decays()
 
     def grammar(self):
         """
         Access the internal Lark grammar definition file,
-        loading it from the default location if needed.
+        effectively loading the default grammar with default parsing options
+        if no grammar has been loaded before.
 
         Returns
         -------
         out: str
             The Lark grammar definition file.
         """
         if not self.grammar_loaded:
             self.load_grammar()
 
         return self._grammar
 
     def grammar_info(self):
         """
         Access the internal Lark grammar definition file name and
-        parser options, loading the grammar from the default location if needed.
+        parser options, effectively loading the default grammar
+        with default parsing options if no grammar has been loaded before.
 
         Returns
         -------
         out: dict
             The Lark grammar definition file name and parser options.
         """
         if not self.grammar_loaded:
@@ -262,17 +273,28 @@
 
             self._grammar = open(filename).read()
 
         self._grammar_info = dict(lark_file=filename, parser=parser, lexer=lexer, **options)
 
     @property
     def grammar_loaded(self):
-        """Check to see if the Lark grammar definition file is loaded."""
+        """
+        Check to see if the Lark grammar definition file is loaded.
+        """
         return self._grammar is not None
 
+    def dict_decays2copy(self):
+        """
+        Return a dictionary of all statements in the input parsed file
+        defining a decay to be copied, of the form
+        "CopyDecay <NAME> <DECAY_TO_COPY>",
+        as {'NAME1': DECAY_TO_COPY1, 'NAME2': DECAY_TO_COPY2, ...}.
+        """
+        return get_decays2copy_statements(self._parsed_dec_file)
+
     def dict_definitions(self):
         """
         Return a dictionary of all definitions in the input parsed file,
         of the form "Define <NAME> <VALUE>",
         as {'NAME1': VALUE1, 'NAME2': VALUE2, ...}.
         """
         return get_definitions(self._parsed_dec_file)
@@ -314,15 +336,15 @@
             'PARAM2': {...},
             ...}.
         """
         return get_jetset_definitions(self._parsed_dec_file)
 
     def list_lineshape_definitions(self):
         """
-        Return a dictionary of all SetLineshapePW definitions in the input parsed file,
+        Return a list of all SetLineshapePW definitions in the input parsed file,
         of the form
         "SetLineshapePW <MOTHER> <DAUGHTER1> <DAUGHTER2> <VALUE>",
         as
         [(['MOTHER1', 'DAUGHTER1-1', 'DAUGHTER1-2'], VALUE1),
         (['MOTHER2', 'DAUGHTER2-1', 'DAUGHTER2-2'], VALUE2),
         ...]
         """
@@ -349,35 +371,73 @@
         in the input parsed file, of the form "CDecay <MOTHER>", as
         ['MOTHER1', 'MOTHER2', ...].
         """
         return get_charge_conjugate_decays(self._parsed_dec_file)
 
     def _find_parsed_decays(self):
         """
-        Return a tuple of all decay definitions in the input parsed file,
-        of the form
-        "Decay <MOTHER>",
-        as a tuple of Lark Tree instances with Tree.data=='decay', i.e.,
-        (Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER1>]), ...),
-        Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER2>]), ...)).
+        Find all decay definitions in the input parsed file,
+        which are of the form "Decay <MOTHER>", and save them internally
+        as a list of Lark Tree instances with Tree.data=='decay', i.e.,
+        [Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER1>]), ...),
+        Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER2>]), ...)].
 
         Duplicate definitions (a bug, of course) are removed, issuing a warning.
 
         Note
         ----
         1) Method not meant to be used directly!
-        2) charge conjugates need to be dealt with differently,
+        2) Charge conjugates need to be dealt with differently,
         see 'self._add_charge_conjugate_decays()'.
         """
         if self._parsed_dec_file is not None:
             self._parsed_decays = get_decays(self._parsed_dec_file)
 
         # Check for duplicates - should be considered a bug in the .dec file!
         self._check_parsed_decays()
 
+    def _add_decays_to_be_copied(self):
+        """
+        Create the copies of the Lark Tree instances of decays specified
+        in the input parsed file via the statements of the form
+        "CopyDecay <NAME> <DECAY_TO_COPY>".
+        These are added to the internal list of decays stored in the class
+        in variable 'self._parsed_decays'.
+
+        Note
+        ----
+        1) There is no check that for a requested copy of non self-conjugate decay
+           the copy of the corresponding antiparticle is also requested in the file!
+           In other terms, only explicit copies are performed.
+        2) Method not meant to be used directly!
+        """
+        decays2copy = self.dict_decays2copy()
+
+        # match name -> position in list self._parsed_decays
+        name2treepos = {t.children[0].children[0].value:i for i, t in enumerate(self._parsed_decays)}
+
+        # Make the copies taking care to change the name of the mother particle
+        copied_decays = []
+        misses = []
+        for decay2copy, decay2becopied in decays2copy.items():
+            try:
+                match = self._parsed_decays[name2treepos[decay2becopied]]
+                copied_decay = match.__deepcopy__(None)
+                copied_decay.children[0].children[0].value = decay2copy
+                copied_decays.append(copied_decay)
+            except:
+                misses.append(decay2copy)
+        if len(misses) > 0:
+            msg = """\nCorresponding 'Decay' statement for 'CopyDecay' statement(s) of following particle(s) not found:\n{0}.
+Skipping creation of these copied decay trees.""".format('\n'.join([m for m in misses]))
+            warnings.warn(msg)
+
+        # Actually add all these copied decays to the list of decays!
+        self._parsed_decays.extend(copied_decays)
+
     def _add_charge_conjugate_decays(self):
         """
         If requested (see the 'self._include_ccdecays' class attribute),
         create the Lark Tree instances describing the charge conjugate decays
         specified in the input parsed file via the statements of the form
         "CDecay <MOTHER>".
         These are added to the internal list of decays stored in the class
@@ -987,16 +1047,15 @@
 
     return [_value(tree) for tree in lmo[0].children] if len(lmo) == 1 else ''
 
 
 def get_decays(parsed_file):
     """
     Return a list of all decay definitions in the input parsed file,
-    of the form
-    "Decay <MOTHER>",
+    of the form "Decay <MOTHER>",
     as a tuple of Lark Tree instances with Tree.data=='decay', i.e.,
     [Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER1>]), ...),
      Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER2>]), ...)].
 
     Parameters
     ----------
     parsed_file: Lark Tree instance
@@ -1027,14 +1086,36 @@
 
     try:
         return sorted([tree.children[0].children[0].value for tree in parsed_file.find_data('cdecay')])
     except:
         RuntimeError("Input parsed file does not seem to have the expected structure.")
 
 
+def get_decays2copy_statements(parsed_file):
+    """
+    Return a dictionary of all statements in the input parsed file
+    defining a decay to be copied, of the form
+    "CopyDecay <NAME> <DECAY_TO_COPY>",
+    as {'NAME1': DECAY_TO_COPY1, 'NAME2': DECAY_TO_COPY2, ...}.
+
+    Parameters
+    ----------
+    parsed_file: Lark Tree instance
+        Input parsed file.
+    """
+    if not isinstance(parsed_file, Tree) :
+        raise RuntimeError("Input not an instance of a Tree!")
+
+    try:
+        return {tree.children[0].children[0].value:tree.children[1].children[0].value
+            for tree in parsed_file.find_data('copydecay')}
+    except:
+        RuntimeError("Input parsed file does not seem to have the expected structure.")
+
+
 def get_definitions(parsed_file):
     """
     Return a dictionary of all definitions in the input parsed file, of the form
     "Define <NAME> <VALUE>", as {'NAME1': VALUE1, 'NAME2': VALUE2, ...}.
 
     Parameters
     ----------
@@ -1172,15 +1253,15 @@
         return dict_params
     except:
         RuntimeError("Input parsed file does not seem to have the expected structure.")
 
 
 def get_lineshape_definitions(parsed_file):
     """
-    Return a dictionary of all SetLineshapePW definitions in the input parsed file,
+    Return a list of all SetLineshapePW definitions in the input parsed file,
     of the form
     "SetLineshapePW <MOTHER> <DAUGHTER1> <DAUGHTER2> <VALUE>",
     as
     [(['MOTHER1', 'DAUGHTER1-1', 'DAUGHTER1-2'], VALUE1),
      (['MOTHER2', 'DAUGHTER2-1', 'DAUGHTER2-2'], VALUE2),
      ...]
```

### Comparing `DecayLanguage-0.9.0/decaylanguage/dec/decparser.py` & `DecayLanguage-0.9.1/decaylanguage/dec/decparser.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/dec/enums.py` & `DecayLanguage-0.9.1/decaylanguage/dec/enums.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/decay/decay.py` & `DecayLanguage-0.9.1/decaylanguage/decay/decay.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/decay/viewer.py` & `DecayLanguage-0.9.1/decaylanguage/decay/viewer.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/modeling/AmpGenReader.ipynb` & `DecayLanguage-0.9.1/decaylanguage/modeling/AmpGenReader.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/modeling/ampgen2goofit.py` & `DecayLanguage-0.9.1/decaylanguage/modeling/ampgen2goofit.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/modeling/ampgentransform.py` & `DecayLanguage-0.9.1/decaylanguage/modeling/ampgentransform.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/modeling/amplitudechain.py` & `DecayLanguage-0.9.1/decaylanguage/modeling/amplitudechain.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/modeling/decay.py` & `DecayLanguage-0.9.1/decaylanguage/modeling/decay.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/modeling/goofit.py` & `DecayLanguage-0.9.1/decaylanguage/modeling/goofit.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/utils/particleutils.py` & `DecayLanguage-0.9.1/decaylanguage/utils/particleutils.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/decaylanguage/utils/utilities.py` & `DecayLanguage-0.9.1/decaylanguage/utils/utilities.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/docs/conf.py` & `DecayLanguage-0.9.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/docs/reference/decaylanguage.decay.rst` & `DecayLanguage-0.9.1/docs/reference/decaylanguage.decay.rst`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/docs/usage.rst` & `DecayLanguage-0.9.1/docs/usage.rst`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/images/DecayChain_Dst_stable-D0-and-D+.png` & `DecayLanguage-0.9.1/images/DecayChain_Dst_stable-D0-and-D+.png`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/images/DecayLanguage.ink.svg` & `DecayLanguage-0.9.1/images/DecayLanguage.ink.svg`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/images/DecayLanguage.pdf` & `DecayLanguage-0.9.1/images/DecayLanguage.pdf`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/images/DecayLanguage.png` & `DecayLanguage-0.9.1/images/DecayLanguage.png`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/images/DecayLanguage.svg` & `DecayLanguage-0.9.1/images/DecayLanguage.svg`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/models/DtoKpipipi_v2.txt` & `DecayLanguage-0.9.1/models/DtoKpipipi_v2.txt`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/AmpGen2GooFit D2K3p.ipynb` & `DecayLanguage-0.9.1/notebooks/AmpGen2GooFit D2K3p.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/DecReader.ipynb` & `DecayLanguage-0.9.1/notebooks/DecReader.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/DecayLanguageDemo.ipynb` & `DecayLanguage-0.9.1/notebooks/DecayLanguageDemo.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/DtoKpipipi_v2.cu` & `DecayLanguage-0.9.1/notebooks/DtoKpipipi_v2.cu`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/ExampleDecFileParsingWithLark.ipynb` & `DecayLanguage-0.9.1/notebooks/ExampleDecFileParsingWithLark.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/__init__.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/__init__.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/__main__.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/__main__.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/DECAY_BELLE2.DEC` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/DECAY_BELLE2.DEC`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/DECAY_LHCB.DEC` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/DECAY_LHCB.DEC`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/MintDalitzSpecialParticles.csv` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/MintDalitzSpecialParticles.csv`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/MintDalitzSpecialParticles.fwf` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/MintDalitzSpecialParticles.fwf`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/MintDalitzSpecialParticlesLatex.csv`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/README.rst` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/README.rst`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/WorkingOutModel.ipynb` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/WorkingOutModel.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/ampgen.lark` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/ampgen.lark`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/decfile.lark` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/decfile.lark`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 // Copyright (c) 2018-2020, Eduardo Rodrigues and Henry Schreiner.
 //
 // Distributed under the 3-clause BSD license, see accompanying file LICENSE
 // or https://github.com/scikit-hep/decaylanguage for details.
 
 start : _NEWLINE* (line _NEWLINE+)+ ("End" _NEWLINE+)?
-?line : define | pythia_def | jetset_def | alias | chargeconj | commands | decay | cdecay | setlspw
+?line : define | pythia_def | jetset_def | alias | chargeconj | commands | decay | cdecay | copydecay | setlspw
 
 pythia_def : "PythiaBothParam" LABEL ":" LABEL "=" (LABEL | SIGNED_NUMBER)
 
 jetset_def : "JetSetPar" LABEL "=" SIGNED_NUMBER
 
 setlspw : "SetLineshapePW" label label label value
 
@@ -28,14 +28,16 @@
                 | "noPhotos"  -> no
 
 decay : "Decay" particle _NEWLINE+ decayline+ "Enddecay"
 decayline : value particle* photos? model (_NEWLINE | _SEMICOLON)+ // There is always a ; here
 value : SIGNED_NUMBER
 photos : "PHOTOS"
 
+copydecay : "CopyDecay" label label
+
 label : LABEL
 particle : LABEL // Add full particle parsing here
 
 model : MODEL_NAME model_options?
 model_options : (value | LABEL | _NEWLINE)+
 
 // model : model_generic
```

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/data/particle.lark` & `DecayLanguage-0.9.1/notebooks/decaylanguage/data/particle.lark`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/dec/dec.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/dec/dec.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,18 +5,19 @@
 
 """
 Submodule with classes and utilities to deal with and parse .dec decay files.
 
 Basic assumptions
 -----------------
 
-1) For standard (non-alias) particle (names):
+1) For standard particle names *not defined* via aliases:
     - Decay modes defined via a 'Decay' statement.
     - Related antiparticle decay modes either defined via a 'CDecay' statement
       or via a 'Decay' statement. The latter option is often used if CP matters.
+
 2) For particle names defined via aliases:
     - Particle decay modes defined as above.
     - Related antiparticle decay modes defined with either options above,
       *but* there needs to be a 'ChargeConj' statement specifying the
       particle-antiparticle match. Typically::
 
         Alias MyP+ P+
@@ -25,14 +26,18 @@
         Decay MyP+
         ...
         Enddecay
         CDecay MyP-
 
 3) As a consequence, particles that are self-conjugate should not be used
    in 'CDecay' statements, obviously.
+
+ 4) Decays defined via a 'CopyDecay' statement are simply (deep) copied
+    and no copy of the corresponding antiparticle is performed unless explicitly requested
+    with another 'CopyDecay' statement.
 """
 
 from __future__ import absolute_import, division, print_function
 
 import os
 import warnings
 import re
@@ -71,15 +76,16 @@
 
 class DecFileParser(object):
     """
     The class to parse a .dec decay file.
 
     Example
     -------
-    >>> parsed_file = DecFileParser('my-decay-file.dec')
+    >>> dfp = DecFileParser('my-decay-file.dec')
+    >>> dfp.parse()
     """
 
     __slots__ = ("_grammar",
                  "_grammar_info",
                  "_dec_file_names",
                  "_dec_file",
                  "_parsed_dec_file",
@@ -149,21 +155,20 @@
         _cls._dec_file_names = '<dec file input as a string>'
         _cls._dec_file = stream.read()
 
         return _cls
 
     def parse(self, include_ccdecays=True):
         """
-        Parse the given .dec decay file according to default Lark parser
-        and specified options, i.e.,
-            parser = 'lalr',
-            lexer = 'standard'.
+        Parse the given .dec decay file(s) according to the default Lark parser
+        and specified options.
 
         See method 'load_grammar' for how to explicitly define the grammar
-        and set the Lark parsing options.
+        and set the Lark parsing options. This method needs to be called
+        before 'parse' to override the parser and its options.
 
         Parameters
         ----------
         include_ccdecays: boolean, optional, default=True
             Choose whether or not to consider charge-conjugate decays,
             which are specified via "CDecay <MOTHER>".
             Make sure you understand the consequences of ignoring
@@ -194,37 +199,43 @@
         # variable names with actual values provided via 'Define' statements,
         # and perform the replacements name -> value where relevant.
         # Do also a replacement of 'a_float' with a_float.
         dict_define_defs = self.dict_definitions()
         for tree in self._parsed_decays:
             DecayModelParamValueReplacement(define_defs=dict_define_defs).visit(tree)
 
-        # ... and create on the fly the charge conjugate decays, if requested
+        # Create on the fly the decays to be copied, if requested
+        if self.dict_decays2copy():
+            self._add_decays_to_be_copied()
+
+        # Create on the fly the charge conjugate decays, if requested
         if self._include_ccdecays:
             self._add_charge_conjugate_decays()
 
     def grammar(self):
         """
         Access the internal Lark grammar definition file,
-        loading it from the default location if needed.
+        effectively loading the default grammar with default parsing options
+        if no grammar has been loaded before.
 
         Returns
         -------
         out: str
             The Lark grammar definition file.
         """
         if not self.grammar_loaded:
             self.load_grammar()
 
         return self._grammar
 
     def grammar_info(self):
         """
         Access the internal Lark grammar definition file name and
-        parser options, loading the grammar from the default location if needed.
+        parser options, effectively loading the default grammar
+        with default parsing options if no grammar has been loaded before.
 
         Returns
         -------
         out: dict
             The Lark grammar definition file name and parser options.
         """
         if not self.grammar_loaded:
@@ -262,17 +273,28 @@
 
             self._grammar = open(filename).read()
 
         self._grammar_info = dict(lark_file=filename, parser=parser, lexer=lexer, **options)
 
     @property
     def grammar_loaded(self):
-        """Check to see if the Lark grammar definition file is loaded."""
+        """
+        Check to see if the Lark grammar definition file is loaded.
+        """
         return self._grammar is not None
 
+    def dict_decays2copy(self):
+        """
+        Return a dictionary of all statements in the input parsed file
+        defining a decay to be copied, of the form
+        "CopyDecay <NAME> <DECAY_TO_COPY>",
+        as {'NAME1': DECAY_TO_COPY1, 'NAME2': DECAY_TO_COPY2, ...}.
+        """
+        return get_decays2copy_statements(self._parsed_dec_file)
+
     def dict_definitions(self):
         """
         Return a dictionary of all definitions in the input parsed file,
         of the form "Define <NAME> <VALUE>",
         as {'NAME1': VALUE1, 'NAME2': VALUE2, ...}.
         """
         return get_definitions(self._parsed_dec_file)
@@ -314,15 +336,15 @@
             'PARAM2': {...},
             ...}.
         """
         return get_jetset_definitions(self._parsed_dec_file)
 
     def list_lineshape_definitions(self):
         """
-        Return a dictionary of all SetLineshapePW definitions in the input parsed file,
+        Return a list of all SetLineshapePW definitions in the input parsed file,
         of the form
         "SetLineshapePW <MOTHER> <DAUGHTER1> <DAUGHTER2> <VALUE>",
         as
         [(['MOTHER1', 'DAUGHTER1-1', 'DAUGHTER1-2'], VALUE1),
         (['MOTHER2', 'DAUGHTER2-1', 'DAUGHTER2-2'], VALUE2),
         ...]
         """
@@ -349,35 +371,73 @@
         in the input parsed file, of the form "CDecay <MOTHER>", as
         ['MOTHER1', 'MOTHER2', ...].
         """
         return get_charge_conjugate_decays(self._parsed_dec_file)
 
     def _find_parsed_decays(self):
         """
-        Return a tuple of all decay definitions in the input parsed file,
-        of the form
-        "Decay <MOTHER>",
-        as a tuple of Lark Tree instances with Tree.data=='decay', i.e.,
-        (Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER1>]), ...),
-        Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER2>]), ...)).
+        Find all decay definitions in the input parsed file,
+        which are of the form "Decay <MOTHER>", and save them internally
+        as a list of Lark Tree instances with Tree.data=='decay', i.e.,
+        [Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER1>]), ...),
+        Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER2>]), ...)].
 
         Duplicate definitions (a bug, of course) are removed, issuing a warning.
 
         Note
         ----
         1) Method not meant to be used directly!
-        2) charge conjugates need to be dealt with differently,
+        2) Charge conjugates need to be dealt with differently,
         see 'self._add_charge_conjugate_decays()'.
         """
         if self._parsed_dec_file is not None:
             self._parsed_decays = get_decays(self._parsed_dec_file)
 
         # Check for duplicates - should be considered a bug in the .dec file!
         self._check_parsed_decays()
 
+    def _add_decays_to_be_copied(self):
+        """
+        Create the copies of the Lark Tree instances of decays specified
+        in the input parsed file via the statements of the form
+        "CopyDecay <NAME> <DECAY_TO_COPY>".
+        These are added to the internal list of decays stored in the class
+        in variable 'self._parsed_decays'.
+
+        Note
+        ----
+        1) There is no check that for a requested copy of non self-conjugate decay
+           the copy of the corresponding antiparticle is also requested in the file!
+           In other terms, only explicit copies are performed.
+        2) Method not meant to be used directly!
+        """
+        decays2copy = self.dict_decays2copy()
+
+        # match name -> position in list self._parsed_decays
+        name2treepos = {t.children[0].children[0].value:i for i, t in enumerate(self._parsed_decays)}
+
+        # Make the copies taking care to change the name of the mother particle
+        copied_decays = []
+        misses = []
+        for decay2copy, decay2becopied in decays2copy.items():
+            try:
+                match = self._parsed_decays[name2treepos[decay2becopied]]
+                copied_decay = match.__deepcopy__(None)
+                copied_decay.children[0].children[0].value = decay2copy
+                copied_decays.append(copied_decay)
+            except:
+                misses.append(decay2copy)
+        if len(misses) > 0:
+            msg = """\nCorresponding 'Decay' statement for 'CopyDecay' statement(s) of following particle(s) not found:\n{0}.
+Skipping creation of these copied decay trees.""".format('\n'.join([m for m in misses]))
+            warnings.warn(msg)
+
+        # Actually add all these copied decays to the list of decays!
+        self._parsed_decays.extend(copied_decays)
+
     def _add_charge_conjugate_decays(self):
         """
         If requested (see the 'self._include_ccdecays' class attribute),
         create the Lark Tree instances describing the charge conjugate decays
         specified in the input parsed file via the statements of the form
         "CDecay <MOTHER>".
         These are added to the internal list of decays stored in the class
@@ -987,16 +1047,15 @@
 
     return [_value(tree) for tree in lmo[0].children] if len(lmo) == 1 else ''
 
 
 def get_decays(parsed_file):
     """
     Return a list of all decay definitions in the input parsed file,
-    of the form
-    "Decay <MOTHER>",
+    of the form "Decay <MOTHER>",
     as a tuple of Lark Tree instances with Tree.data=='decay', i.e.,
     [Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER1>]), ...),
      Tree(decay, [Tree(particle, [Token(LABEL, <MOTHER2>]), ...)].
 
     Parameters
     ----------
     parsed_file: Lark Tree instance
@@ -1027,14 +1086,36 @@
 
     try:
         return sorted([tree.children[0].children[0].value for tree in parsed_file.find_data('cdecay')])
     except:
         RuntimeError("Input parsed file does not seem to have the expected structure.")
 
 
+def get_decays2copy_statements(parsed_file):
+    """
+    Return a dictionary of all statements in the input parsed file
+    defining a decay to be copied, of the form
+    "CopyDecay <NAME> <DECAY_TO_COPY>",
+    as {'NAME1': DECAY_TO_COPY1, 'NAME2': DECAY_TO_COPY2, ...}.
+
+    Parameters
+    ----------
+    parsed_file: Lark Tree instance
+        Input parsed file.
+    """
+    if not isinstance(parsed_file, Tree) :
+        raise RuntimeError("Input not an instance of a Tree!")
+
+    try:
+        return {tree.children[0].children[0].value:tree.children[1].children[0].value
+            for tree in parsed_file.find_data('copydecay')}
+    except:
+        RuntimeError("Input parsed file does not seem to have the expected structure.")
+
+
 def get_definitions(parsed_file):
     """
     Return a dictionary of all definitions in the input parsed file, of the form
     "Define <NAME> <VALUE>", as {'NAME1': VALUE1, 'NAME2': VALUE2, ...}.
 
     Parameters
     ----------
@@ -1172,15 +1253,15 @@
         return dict_params
     except:
         RuntimeError("Input parsed file does not seem to have the expected structure.")
 
 
 def get_lineshape_definitions(parsed_file):
     """
-    Return a dictionary of all SetLineshapePW definitions in the input parsed file,
+    Return a list of all SetLineshapePW definitions in the input parsed file,
     of the form
     "SetLineshapePW <MOTHER> <DAUGHTER1> <DAUGHTER2> <VALUE>",
     as
     [(['MOTHER1', 'DAUGHTER1-1', 'DAUGHTER1-2'], VALUE1),
      (['MOTHER2', 'DAUGHTER2-1', 'DAUGHTER2-2'], VALUE2),
      ...]
```

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/dec/decparser.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/dec/decparser.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/dec/enums.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/dec/enums.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/decay/decay.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/decay/decay.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/decay/viewer.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/decay/viewer.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/AmpGenReader.ipynb` & `DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/AmpGenReader.ipynb`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/ampgen2goofit.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/ampgen2goofit.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/ampgentransform.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/ampgentransform.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/amplitudechain.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/amplitudechain.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/decay.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/decay.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/modeling/goofit.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/modeling/goofit.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/utils/particleutils.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/utils/particleutils.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/decaylanguage/utils/utilities.py` & `DecayLanguage-0.9.1/notebooks/decaylanguage/utils/utilities.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/notebooks/simple_model.txt` & `DecayLanguage-0.9.1/notebooks/simple_model.txt`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/setup.cfg` & `DecayLanguage-0.9.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/setup.py` & `DecayLanguage-0.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/defs-aliases-chargeconj.dec` & `DecayLanguage-0.9.1/tests/data/defs-aliases-chargeconj.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/duplicate-decays.dec` & `DecayLanguage-0.9.1/tests/data/duplicate-decays.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/test_Bd2DDst_Ds2DmPi0.dec` & `DecayLanguage-0.9.1/tests/data/test_Bd2DDst_Ds2DmPi0.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/test_Bd2DMuNu.dec` & `DecayLanguage-0.9.1/tests/data/test_Bd2DMuNu.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/test_Bd2DmTauNu_Dm23PiPi0_Tau2MuNu.dec` & `DecayLanguage-0.9.1/tests/data/test_Bd2DmTauNu_Dm23PiPi0_Tau2MuNu.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/test_Bd2Dst0X_D02KPi.dec` & `DecayLanguage-0.9.1/tests/data/test_Bd2Dst0X_D02KPi.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/test_Bd2DstDst.dec` & `DecayLanguage-0.9.1/tests/data/test_Bd2DstDst.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/test_example_Dst.dec` & `DecayLanguage-0.9.1/tests/data/test_example_Dst.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/data/test_issue90.dec` & `DecayLanguage-0.9.1/tests/data/test_issue90.dec`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/dec/test_dec.py` & `DecayLanguage-0.9.1/tests/dec/test_dec.py`

 * *Files 2% similar despite different names*

```diff
@@ -105,14 +105,23 @@
 
         assert "n_decays" not in p.__str__()
 
         p.parse()
         assert "n_decays=5" in p.__str__()
 
 
+def test_copydecay_statement_parsing():
+    p = DecFileParser(DIR / '../data/test_CopyDecay_RemoveDecay.dec')
+    p.parse()
+
+    assert len(p.dict_decays2copy()) == 2
+    assert p.number_of_decays == 4  # 2 original + 2 copied
+    assert p.list_decay_modes('phi_copy') == p.list_decay_modes('phi')
+
+
 def test_definitions_parsing():
     p = DecFileParser(DIR / '../data/defs-aliases-chargeconj.dec')
     p.parse()
 
     assert len(p.dict_definitions()) == 24
```

### Comparing `DecayLanguage-0.9.0/tests/dec/test_issues.py` & `DecayLanguage-0.9.1/tests/dec/test_issues.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/decay/test_decay.py` & `DecayLanguage-0.9.1/tests/decay/test_decay.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/decay/test_viewer.py` & `DecayLanguage-0.9.1/tests/decay/test_viewer.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/output/DtoKpipipi_v2.cu` & `DecayLanguage-0.9.1/tests/output/DtoKpipipi_v2.cu`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/test_convert.py` & `DecayLanguage-0.9.1/tests/test_convert.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/test_dec_full.py` & `DecayLanguage-0.9.1/tests/test_dec_full.py`

 * *Files identical despite different names*

### Comparing `DecayLanguage-0.9.0/tests/test_goofit.py` & `DecayLanguage-0.9.1/tests/test_goofit.py`

 * *Files identical despite different names*

