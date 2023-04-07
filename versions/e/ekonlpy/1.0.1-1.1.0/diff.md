# Comparing `tmp/ekonlpy-1.0.1.tar.gz` & `tmp/ekonlpy-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ekonlpy-1.0.1.tar", max compression
+gzip compressed data, was "ekonlpy-1.1.0.tar", max compression
```

## Comparing `ekonlpy-1.0.1.tar` & `ekonlpy-1.1.0.tar`

### file list

```diff
@@ -1,75 +1,76 @@
--rw-r--r--   0        0        0     1071 2023-04-07 09:55:46.263839 ekonlpy-1.0.1/LICENSE
--rw-r--r--   0        0        0     6544 2023-04-07 09:55:46.263839 ekonlpy-1.0.1/README.md
--rw-r--r--   0        0        0     3542 2023-04-07 09:55:47.859851 ekonlpy-1.0.1/pyproject.toml
--rw-r--r--   0        0        0      265 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/__init__.py
--rw-r--r--   0        0        0       46 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/_version.py
--rw-r--r--   0        0        0       31 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/__init__.py
--rw-r--r--   0        0        0      514 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ADJECTIVES.txt
--rw-r--r--   0        0        0      108 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ADVERBS.txt
--rw-r--r--   0        0        0     2583 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/COUNTRY.txt
--rw-r--r--   0        0        0       17 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/CURRENCY.txt
--rw-r--r--   0        0        0    47727 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_PHRASES.txt
--rw-r--r--   0        0        0   475773 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_TERMS.txt
--rwxr-xr-x   0        0        0    77542 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ENTITY.txt
--rw-r--r--   0        0        0     9629 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt
--rw-r--r--   0        0        0     2077 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/GENERIC.txt
--rw-r--r--   0        0        0    35442 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt
--rw-r--r--   0        0        0    69192 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INSTITUTION.txt
--rw-r--r--   0        0        0    20594 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/LEMMA.txt
--rw-r--r--   0        0        0     2072 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NAMES.txt
--rw-r--r--   0        0        0      687 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NOUNS.txt
--rw-r--r--   0        0        0    10396 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt
--rw-r--r--   0        0        0    12378 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt
--rw-r--r--   0        0        0    14928 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SECTOR.txt
--rw-r--r--   0        0        0     6456 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS.txt
--rwxr-xr-x   0        0        0      260 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_CUST.txt
--rw-r--r--   0        0        0     5788 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt
--rwxr-xr-x   0        0        0      598 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt
--rw-r--r--   0        0        0    33685 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM.txt
--rw-r--r--   0        0        0      300 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_MAG.txt
--rw-r--r--   0        0        0     5329 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt
--rw-r--r--   0        0        0    27207 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt
--rw-r--r--   0        0        0       87 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_VA.txt
--rw-r--r--   0        0        0       69 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/UNIT.txt
--rw-r--r--   0        0        0       40 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/VERBS.txt
--rwxr-xr-x   0        0        0     1677 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Currencies.txt
--rwxr-xr-x   0        0        0      724 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/DatesandNumbers.txt
--rwxr-xr-x   0        0        0     1798 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Generic.txt
--rwxr-xr-x   0        0        0     1622 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Geographic.txt
--rwxr-xr-x   0        0        0  2903900 2023-04-07 09:55:46.363840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/HIV-4.csv
--rwxr-xr-x   0        0        0  8373373 2023-04-07 09:55:46.399840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/LM.csv
--rwxr-xr-x   0        0        0    93474 2023-04-07 09:55:46.399840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Names.txt
--rw-r--r--   0        0        0  3047832 2023-04-07 09:55:46.415840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv
--rw-r--r--   0        0        0  2362210 2023-04-07 09:55:46.427840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv
--rwxr-xr-x   0        0        0   778128 2023-04-07 09:55:46.431840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/expressive-type.csv
--rwxr-xr-x   0        0        0   661841 2023-04-07 09:55:46.431840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/intensity.csv
--rwxr-xr-x   0        0        0   659879 2023-04-07 09:55:46.435840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/polarity.csv
--rw-r--r--   0        0        0  3226022 2023-04-07 09:55:46.451840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv
--rw-r--r--   0        0        0  3832440 2023-04-07 09:55:46.467841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv
--rw-r--r--   0        0        0  2735025 2023-04-07 09:55:46.479841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv
--rw-r--r--   0        0        0  3749409 2023-04-07 09:55:46.499841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv
--rw-r--r--   0        0        0  2835691 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt
--rw-r--r--   0        0        0    36419 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt
--rw-r--r--   0        0        0   281858 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/model/MPKC.nbc
--rw-r--r--   0        0        0    15644 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/tagset.py
--rw-r--r--   0        0        0       33 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/etag/__init__.py
--rw-r--r--   0        0        0     4210 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/etag/_template.py
--rw-r--r--   0        0        0        0 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/py.typed
--rwxr-xr-x   0        0        0      236 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/__init__.py
--rwxr-xr-x   0        0        0     4149 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/base.py
--rwxr-xr-x   0        0        0     1741 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/euko.py
--rwxr-xr-x   0        0        0     1010 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/hiv4.py
--rw-r--r--   0        0        0     5936 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/kosac.py
--rwxr-xr-x   0        0        0     1054 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/lm.py
--rw-r--r--   0        0        0    16118 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/sentiment/mpck.py
--rwxr-xr-x   0        0        0     1840 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/sentiment/mpko.py
--rwxr-xr-x   0        0        0     9268 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/sentiment/utils.py
--rw-r--r--   0        0        0      102 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/__init__.py
--rw-r--r--   0        0        0     7221 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/_mecab.py
--rw-r--r--   0        0        0     2171 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/_postprocess.py
--rw-r--r--   0        0        0     4529 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/_userdic.py
--rw-r--r--   0        0        0    10630 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/mecab.py
--rwxr-xr-x   0        0        0        0 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/utils/__init__.py
--rw-r--r--   0        0        0     3520 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/utils/dictionary.py
--rw-r--r--   0        0        0     6668 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/utils/io.py
--rw-r--r--   0        0        0     7487 1970-01-01 00:00:00.000000 ekonlpy-1.0.1/PKG-INFO
+-rw-r--r--   0        0        0     1071 2023-04-07 11:23:17.805942 ekonlpy-1.1.0/LICENSE
+-rw-r--r--   0        0        0     8101 2023-04-07 11:23:17.805942 ekonlpy-1.1.0/README.md
+-rw-r--r--   0        0        0     3603 2023-04-07 11:23:19.129955 ekonlpy-1.1.0/pyproject.toml
+-rw-r--r--   0        0        0      265 2023-04-07 11:23:17.881943 ekonlpy-1.1.0/src/ekonlpy/__init__.py
+-rw-r--r--   0        0        0       46 2023-04-07 11:23:19.069954 ekonlpy-1.1.0/src/ekonlpy/_version.py
+-rw-r--r--   0        0        0       31 2023-04-07 11:23:17.881943 ekonlpy-1.1.0/src/ekonlpy/data/__init__.py
+-rw-r--r--   0        0        0      514 2023-04-07 11:23:17.881943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ADJECTIVES.txt
+-rw-r--r--   0        0        0      108 2023-04-07 11:23:17.881943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ADVERBS.txt
+-rw-r--r--   0        0        0     2583 2023-04-07 11:23:17.881943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/COUNTRY.txt
+-rw-r--r--   0        0        0       17 2023-04-07 11:23:17.881943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/CURRENCY.txt
+-rw-r--r--   0        0        0    47727 2023-04-07 11:23:17.881943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ECON_PHRASES.txt
+-rw-r--r--   0        0        0   475773 2023-04-07 11:23:17.889943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ECON_TERMS.txt
+-rwxr-xr-x   0        0        0    77542 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ENTITY.txt
+-rw-r--r--   0        0        0     9629 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt
+-rw-r--r--   0        0        0     2077 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/GENERIC.txt
+-rw-r--r--   0        0        0    35442 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt
+-rw-r--r--   0        0        0    69192 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/INSTITUTION.txt
+-rw-r--r--   0        0        0    20594 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/LEMMA.txt
+-rw-r--r--   0        0        0     2072 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/NAMES.txt
+-rw-r--r--   0        0        0      687 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/NOUNS.txt
+-rw-r--r--   0        0        0    10396 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt
+-rw-r--r--   0        0        0    12378 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt
+-rw-r--r--   0        0        0    14928 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SECTOR.txt
+-rw-r--r--   0        0        0     6456 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/STOPWORDS.txt
+-rwxr-xr-x   0        0        0      260 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/STOPWORDS_CUST.txt
+-rw-r--r--   0        0        0     5788 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt
+-rwxr-xr-x   0        0        0      598 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt
+-rw-r--r--   0        0        0    33685 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM.txt
+-rw-r--r--   0        0        0      300 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM_MAG.txt
+-rw-r--r--   0        0        0     5329 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt
+-rw-r--r--   0        0        0    27207 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt
+-rw-r--r--   0        0        0       87 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM_VA.txt
+-rw-r--r--   0        0        0       69 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/UNIT.txt
+-rw-r--r--   0        0        0       40 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/dictionary/VERBS.txt
+-rwxr-xr-x   0        0        0     1677 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Currencies.txt
+-rwxr-xr-x   0        0        0      724 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/DatesandNumbers.txt
+-rwxr-xr-x   0        0        0     1798 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Generic.txt
+-rwxr-xr-x   0        0        0     1622 2023-04-07 11:23:17.893943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Geographic.txt
+-rwxr-xr-x   0        0        0  2903900 2023-04-07 11:23:17.901943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/HIV-4.csv
+-rwxr-xr-x   0        0        0  8373373 2023-04-07 11:23:17.941943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/LM.csv
+-rwxr-xr-x   0        0        0    93474 2023-04-07 11:23:17.945943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Names.txt
+-rw-r--r--   0        0        0  3047832 2023-04-07 11:23:17.957943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv
+-rw-r--r--   0        0        0  2362210 2023-04-07 11:23:17.969943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv
+-rwxr-xr-x   0        0        0   778128 2023-04-07 11:23:17.973943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/kosac/expressive-type.csv
+-rwxr-xr-x   0        0        0   661841 2023-04-07 11:23:17.973943 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/kosac/intensity.csv
+-rwxr-xr-x   0        0        0   659879 2023-04-07 11:23:17.977944 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/kosac/polarity.csv
+-rw-r--r--   0        0        0  3226022 2023-04-07 11:23:17.993944 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv
+-rw-r--r--   0        0        0  3832440 2023-04-07 11:23:18.009944 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv
+-rw-r--r--   0        0        0  2735025 2023-04-07 11:23:18.021944 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv
+-rw-r--r--   0        0        0  3749409 2023-04-07 11:23:18.041944 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv
+-rw-r--r--   0        0        0  2835691 2023-04-07 11:23:18.049944 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt
+-rw-r--r--   0        0        0    36419 2023-04-07 11:23:18.049944 ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt
+-rw-r--r--   0        0        0   281858 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/data/model/MPKC.nbc
+-rw-r--r--   0        0        0    15644 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/data/tagset.py
+-rw-r--r--   0        0        0       33 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/etag/__init__.py
+-rw-r--r--   0        0        0     4210 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/etag/_template.py
+-rwxr-xr-x   0        0        0       63 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/mecab/__init__.py
+-rw-r--r--   0        0        0     5687 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/mecab/_mecab.py
+-rw-r--r--   0        0        0     4529 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/mecab/_userdic.py
+-rw-r--r--   0        0        0        0 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/py.typed
+-rwxr-xr-x   0        0        0      236 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/__init__.py
+-rwxr-xr-x   0        0        0     4149 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/base.py
+-rwxr-xr-x   0        0        0     1741 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/euko.py
+-rwxr-xr-x   0        0        0     1010 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/hiv4.py
+-rw-r--r--   0        0        0     5936 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/kosac.py
+-rwxr-xr-x   0        0        0     1054 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/lm.py
+-rw-r--r--   0        0        0    16118 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/mpck.py
+-rwxr-xr-x   0        0        0     1840 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/mpko.py
+-rwxr-xr-x   0        0        0     9268 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/sentiment/utils.py
+-rw-r--r--   0        0        0       66 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/tag/__init__.py
+-rw-r--r--   0        0        0    10630 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/tag/_mecab.py
+-rw-r--r--   0        0        0     2172 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/tag/_postprocess.py
+-rwxr-xr-x   0        0        0        0 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/utils/__init__.py
+-rw-r--r--   0        0        0     3520 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/utils/dictionary.py
+-rw-r--r--   0        0        0     6668 2023-04-07 11:23:18.053944 ekonlpy-1.1.0/src/ekonlpy/utils/io.py
+-rw-r--r--   0        0        0     8998 1970-01-01 00:00:00.000000 ekonlpy-1.1.0/PKG-INFO
```

### Comparing `ekonlpy-1.0.1/LICENSE` & `ekonlpy-1.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/README.md` & `ekonlpy-1.1.0/README.md`

 * *Files 18% similar despite different names*

```diff
@@ -1,35 +1,46 @@
 # eKoNLPy: Korean NLP Python Library for Economic Analysis
 
 [![pypi-image]][pypi-url]
 [![version-image]][release-url]
 [![release-date-image]][release-url]
 [![license-image]][license-url]
+[![codecov](https://codecov.io/gh/entelecheia/eKoNLPy/branch/master/graph/badge.svg)](https://codecov.io/gh/entelecheia/eKoNLPy)
 
 <!-- Links: -->
 
 [pypi-image]: https://badge.fury.io/py/ekonlpy.svg
 [pypi-url]: https://badge.fury.io/py/ekonlpy
 [license-image]: https://img.shields.io/github/license/entelecheia/eKoNLPy
 [license-url]: https://github.com/entelecheia/eKoNLPy/blob/master/LICENSE
 [version-image]: https://img.shields.io/github/v/release/entelecheia/eKoNLPy?sort=semver
 [release-date-image]: https://img.shields.io/github/release-date/entelecheia/eKoNLPy
 [release-url]: https://github.com/entelecheia/eKoNLPy/releases
+[codecov-image]: https://codecov.io/gh/entelecheia/eKoNLPy/branch/master/graph/badge.svg?token=8I4ORHRREL
+[codecov-url]: https://codecov.io/gh/entelecheia/eKoNLPy
 [conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
 [conventional commits]: https://conventionalcommits.org
 [repo-url]: https://github.com/entelecheia/eKoNLPy
 [pypi-url]: https://pypi.org/project/ekonlpy
 [docs-url]: https://ekonlpy.entelecheia.ai
 [changelog]: https://github.com/entelecheia/eKoNLPy/blob/master/CHANGELOG.md
 [contributing guidelines]: https://github.com/entelecheia/eKoNLPy/blob/master/CONTRIBUTING.md
 
 <!-- Links: -->
 
 `eKoNLPy` is a Korean Natural Language Processing (NLP) Python library specifically designed for economic analysis. It extends the functionality of the `MeCab` tagger from KoNLPy to improve the handling of economic terms, financial institutions, and company names, classifying them as single nouns. Additionally, it incorporates sentiment analysis features to determine the tone of monetary policy statements, such as Hawkish or Dovish.
 
+**Important Note:**
+
+eKoNLPy is built on the [fugashi](https://github.com/polm/fugashi) and [mecab-ko-dic](https://github.com/LuminosoInsight/mecab-ko-dic) libraries. For more information on using the `Mecab` tagger, please refer to the [fugashi documentation](https://github.com/polm/fugashi). As eKoNLPy no longer relies on the [KoNLPy](https://konlpy.org) library, Java is not required for its use. This makes eKoNLPy compatible with Windows, Linux, and Mac OS, without the need for Java installation. You can also use eKoNLPy on Google Colab.
+
+If you wish to tokenize general Korean text with eKoNLPy, you do not need to install the `KoNLPy` library. Instead, utilize `ekonlpy.mecab.MeCab` as a replacement for `ekonlpy.tag.Mecab`.
+
+However, if you plan to use the [Korean Sentiment Analyzer (KSA)](#korean-sentiment-analyzer-ksa), which employs the `Kkma` morpheme analyzer, you will need to install the [KoNLPy](https://konlpy.org) library.
+
 ## Installation
 
 To install eKoNLPy, run the following command:
 
 ```bash
 pip install ekonlpy
 ```
@@ -38,30 +49,41 @@
 
 ### Part of Speech Tagging
 
 To use the part of speech tagging feature, input `Mecab.pos(phrase)` just like KoNLPy. First, the input is processed using KoNLPy's Mecab morpheme analyzer. Then, if a combination of consecutive tokens matches a term in the user dictionary, the phrase is separated into compound nouns.
 
 ```python
 from ekonlpy.tag import Mecab
+
 mecab = Mecab()
 mecab.pos('금통위는 따라서 물가안정과 병행, 경기상황에 유의하는 금리정책을 펼쳐나가기로 했다고 밝혔다.')
 ```
 
-> [('금통위', 'NNG'), ('는', 'JX'), ('따라서', 'MAJ'), ('물가', 'NNG'), ('안정', 'NNG'), ('과', 'JC'), ('병행', 'NNG'), (',', 'SC'), ('경기', 'NNG'), ('상황', 'NNG'), ('에', 'JKB'), ('유의', 'NNG'), ('하', 'XSV'), ('는', 'ETM'), ('금리정책', 'NNG'), ('을', 'JKO'), ('펼쳐', 'VV+EC'), ('나가', 'VX'), ('기', 'ETN'), ('로', 'JKB'), ('했', 'VV+EP'), ('다고', 'EC'), ('밝혔', 'VV+EP'), ('다', 'EF'), ('.', 'SF')]
+> [('금', 'MAJ'), ('통', 'MAG'), ('위', 'NNG'), ('는', 'JX'), ('따라서', 'MAJ'), ('물가', 'NNG'), ('안정', 'NNG'), ('과', 'JC'), ('병행', 'NNG'), (',', 'SC'), ('경기', 'NNG'), ('상황', 'NNG'), ('에', 'JKB'), ('유의', 'NNG'), ('하', 'XSV'), ('는', 'ETM'), ('금리', 'NNG'), ('정책', 'NNG'), ('을', 'JKO'), ('펼쳐', 'VV+EC'), ('나가', 'VX'), ('기', 'ETN'), ('로', 'JKB'), ('했', 'VV+EP'), ('다고', 'EC'), ('밝혔', 'VV+EP'), ('다', 'EF'), ('.', 'SF')]
+
+### cf. MeCab POS Tagging (fugashi)
+
+```python
+from ekonlpy.mecab import MeCab # Be careful! `C` is capital.
+
+mecab = MeCab()
+mecab.pos('금통위는 따라서 물가안정과 병행, 경기상황에 유의하는 금리정책을 펼쳐나가기로 했다고 밝혔다.')
+```
 
 ### Lemmatization and Synonyms
 
 To enhance the accuracy of sentiment analysis, eKoNLPy offers lemmatization and synonym handling features.
 
 ### Adding Words to Dictionary
 
 You can add words to the dictionary in the `ekonlpy.tag` module's Mecab class, either as a string or a list of strings, using the `add_dictionary` method.
 
 ```python
 from ekonlpy.tag import Mecab
+
 mecab = Mecab()
 mecab.add_dictionary('금통위', 'NNG')
 ```
 
 ## Sentiment Analysis
 
 ### Korean Monetary Policy Dictionary (MPKO)
```

### Comparing `ekonlpy-1.0.1/pyproject.toml` & `ekonlpy-1.1.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "eKoNLPy"
-version = "1.0.1"
+version = "1.1.0"
 description = "A Korean natural language processing toolkit for economic analysis"
 authors = ["Young Joon Lee <entelecheia@hotmail.com>"]
 license = "MIT"
 readme = "README.md"
 packages = [{ include = "ekonlpy", from = "src" }]
 homepage = "https://ekonlpy.entelecheia.ai/"
 repository = "https://github.com/entelecheia/eKoNLPy"
@@ -19,15 +19,14 @@
 
 [tool.poetry.dependencies]
 python = ">=3.8.1,<3.12"
 fugashi = "^1.2.1"
 mecab-ko-dic = "^1.0.0"
 nltk = "^3.8.1"
 scipy = "^1.10.1"
-mecab-python3 = "^1.0.6"
 pandas = "^2.0.0"
 
 [tool.poetry.group.dev.dependencies]
 python-semantic-release = "^7.33.1"
 setuptools-scm = "^7.1.0"
 isort = "^5.12.0"
 black = "^23.1.0"
@@ -127,24 +126,25 @@
 
 [tool.setuptools_scm]
 write_to = "src/ekonlpy/_version.py"
 write_to_template = '__version__ = "{version}"'
 tag_regex = '^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$'
 
 [tool.semantic_release]
-branch = "main"
+branch = "master"
 version_toml = "pyproject.toml:tool.poetry.version"
+version_pattern = "src/ekonlpy/_version.py:__version__ = \"{version}\""
 version_source = "tag"
-commit_version_number = true                                    # required for version_source = "tag"
+commit_version_number = true                                          # required for version_source = "tag"
 commit_subject = "chore(release): :rocket: {version} [skip ci]"
 prerelease_tag = "rc"
 major_on_zero = true
 tag_commit = true
 changelog_file = "CHANGELOG.md"
 upload_to_repository = true
 upload_to_release = true
 build_command = "pip install poetry && poetry build"
-hvcs = "github"                                                 # hosting version control system, gitlab is also supported
+hvcs = "github"                                                       # hosting version control system, gitlab is also supported
 
 [build-system]
 requires = ["poetry-core>=1.0.0", "setuptools>=45", "setuptools_scm[toml]>=6.2"]
 build-backend = 'setuptools.build_meta'
```

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ADJECTIVES.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ADJECTIVES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/COUNTRY.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/COUNTRY.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_PHRASES.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ECON_PHRASES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_TERMS.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ECON_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ENTITY.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/ENTITY.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/GENERIC.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/GENERIC.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INSTITUTION.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/INSTITUTION.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/LEMMA.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/LEMMA.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NAMES.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/NAMES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NOUNS.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/NOUNS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SECTOR.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SECTOR.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/STOPWORDS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Currencies.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Currencies.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/DatesandNumbers.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/DatesandNumbers.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Generic.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Generic.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Geographic.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Geographic.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/HIV-4.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/HIV-4.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/LM.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/LM.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Names.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/Names.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/expressive-type.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/kosac/expressive-type.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/intensity.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/kosac/intensity.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/polarity.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/kosac/polarity.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt` & `ekonlpy-1.1.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/model/MPKC.nbc` & `ekonlpy-1.1.0/src/ekonlpy/data/model/MPKC.nbc`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/data/tagset.py` & `ekonlpy-1.1.0/src/ekonlpy/data/tagset.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/etag/_template.py` & `ekonlpy-1.1.0/src/ekonlpy/etag/_template.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/base.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/base.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/euko.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/euko.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/hiv4.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/hiv4.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/kosac.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/kosac.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/lm.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/lm.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/mpck.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/mpck.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/mpko.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/mpko.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/sentiment/utils.py` & `ekonlpy-1.1.0/src/ekonlpy/sentiment/utils.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/tag/_postprocess.py` & `ekonlpy-1.1.0/src/ekonlpy/tag/_postprocess.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from typing import Dict, List, Optional, Tuple, Union
 
-from .mecab import Mecab
+from ._mecab import Mecab
 
 
 class Postprocessor:
     def __init__(
         self,
         base_tagger: Mecab,
         stopwords: Optional[List[str]] = None,
```

### Comparing `ekonlpy-1.0.1/src/ekonlpy/tag/_userdic.py` & `ekonlpy-1.1.0/src/ekonlpy/mecab/_userdic.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/tag/mecab.py` & `ekonlpy-1.1.0/src/ekonlpy/tag/_mecab.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from ..data.tagset import lemma_tags
 from ..data.tagset import mecab_tags as tagset
 from ..data.tagset import mecab_tags_en as tagset_en
 from ..data.tagset import nouns_tags, sent_tags, stop_tags, topic_tags
 from ..etag import ExtTagger
 from ..utils.dictionary import TermDictionary, term_tags
 from ..utils.io import installpath, load_dictionary, load_txt, load_vocab, save_vocab
-from ._mecab import MeCab as _MeCab
+from ..mecab import MeCab as _MeCab
 
 
 class Mecab:
     def __init__(
         self,
         use_default_dictionary: bool = True,
         use_polarity_phrase: bool = False,
```

### Comparing `ekonlpy-1.0.1/src/ekonlpy/utils/dictionary.py` & `ekonlpy-1.1.0/src/ekonlpy/utils/dictionary.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/src/ekonlpy/utils/io.py` & `ekonlpy-1.1.0/src/ekonlpy/utils/io.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.1/PKG-INFO` & `ekonlpy-1.1.0/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,59 +1,69 @@
 Metadata-Version: 2.1
 Name: ekonlpy
-Version: 1.0.1
+Version: 1.1.0
 Summary: A Korean natural language processing toolkit for economic analysis
 Home-page: https://ekonlpy.entelecheia.ai/
 License: MIT
 Keywords: KoNLPy,Tokenization,Sentiment analysis,Monetary policy
 Author: Young Joon Lee
 Author-email: entelecheia@hotmail.com
 Requires-Python: >=3.8.1,<3.12
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: fugashi (>=1.2.1,<2.0.0)
 Requires-Dist: mecab-ko-dic (>=1.0.0,<2.0.0)
-Requires-Dist: mecab-python3 (>=1.0.6,<2.0.0)
 Requires-Dist: nltk (>=3.8.1,<4.0.0)
 Requires-Dist: pandas (>=2.0.0,<3.0.0)
 Requires-Dist: scipy (>=1.10.1,<2.0.0)
 Project-URL: Repository, https://github.com/entelecheia/eKoNLPy
 Description-Content-Type: text/markdown
 
 # eKoNLPy: Korean NLP Python Library for Economic Analysis
 
 [![pypi-image]][pypi-url]
 [![version-image]][release-url]
 [![release-date-image]][release-url]
 [![license-image]][license-url]
+[![codecov](https://codecov.io/gh/entelecheia/eKoNLPy/branch/master/graph/badge.svg)](https://codecov.io/gh/entelecheia/eKoNLPy)
 
 <!-- Links: -->
 
 [pypi-image]: https://badge.fury.io/py/ekonlpy.svg
 [pypi-url]: https://badge.fury.io/py/ekonlpy
 [license-image]: https://img.shields.io/github/license/entelecheia/eKoNLPy
 [license-url]: https://github.com/entelecheia/eKoNLPy/blob/master/LICENSE
 [version-image]: https://img.shields.io/github/v/release/entelecheia/eKoNLPy?sort=semver
 [release-date-image]: https://img.shields.io/github/release-date/entelecheia/eKoNLPy
 [release-url]: https://github.com/entelecheia/eKoNLPy/releases
+[codecov-image]: https://codecov.io/gh/entelecheia/eKoNLPy/branch/master/graph/badge.svg?token=8I4ORHRREL
+[codecov-url]: https://codecov.io/gh/entelecheia/eKoNLPy
 [conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
 [conventional commits]: https://conventionalcommits.org
 [repo-url]: https://github.com/entelecheia/eKoNLPy
 [pypi-url]: https://pypi.org/project/ekonlpy
 [docs-url]: https://ekonlpy.entelecheia.ai
 [changelog]: https://github.com/entelecheia/eKoNLPy/blob/master/CHANGELOG.md
 [contributing guidelines]: https://github.com/entelecheia/eKoNLPy/blob/master/CONTRIBUTING.md
 
 <!-- Links: -->
 
 `eKoNLPy` is a Korean Natural Language Processing (NLP) Python library specifically designed for economic analysis. It extends the functionality of the `MeCab` tagger from KoNLPy to improve the handling of economic terms, financial institutions, and company names, classifying them as single nouns. Additionally, it incorporates sentiment analysis features to determine the tone of monetary policy statements, such as Hawkish or Dovish.
 
+**Important Note:**
+
+eKoNLPy is built on the [fugashi](https://github.com/polm/fugashi) and [mecab-ko-dic](https://github.com/LuminosoInsight/mecab-ko-dic) libraries. For more information on using the `Mecab` tagger, please refer to the [fugashi documentation](https://github.com/polm/fugashi). As eKoNLPy no longer relies on the [KoNLPy](https://konlpy.org) library, Java is not required for its use. This makes eKoNLPy compatible with Windows, Linux, and Mac OS, without the need for Java installation. You can also use eKoNLPy on Google Colab.
+
+If you wish to tokenize general Korean text with eKoNLPy, you do not need to install the `KoNLPy` library. Instead, utilize `ekonlpy.mecab.MeCab` as a replacement for `ekonlpy.tag.Mecab`.
+
+However, if you plan to use the [Korean Sentiment Analyzer (KSA)](#korean-sentiment-analyzer-ksa), which employs the `Kkma` morpheme analyzer, you will need to install the [KoNLPy](https://konlpy.org) library.
+
 ## Installation
 
 To install eKoNLPy, run the following command:
 
 ```bash
 pip install ekonlpy
 ```
@@ -62,30 +72,41 @@
 
 ### Part of Speech Tagging
 
 To use the part of speech tagging feature, input `Mecab.pos(phrase)` just like KoNLPy. First, the input is processed using KoNLPy's Mecab morpheme analyzer. Then, if a combination of consecutive tokens matches a term in the user dictionary, the phrase is separated into compound nouns.
 
 ```python
 from ekonlpy.tag import Mecab
+
 mecab = Mecab()
 mecab.pos('금통위는 따라서 물가안정과 병행, 경기상황에 유의하는 금리정책을 펼쳐나가기로 했다고 밝혔다.')
 ```
 
-> [('금통위', 'NNG'), ('는', 'JX'), ('따라서', 'MAJ'), ('물가', 'NNG'), ('안정', 'NNG'), ('과', 'JC'), ('병행', 'NNG'), (',', 'SC'), ('경기', 'NNG'), ('상황', 'NNG'), ('에', 'JKB'), ('유의', 'NNG'), ('하', 'XSV'), ('는', 'ETM'), ('금리정책', 'NNG'), ('을', 'JKO'), ('펼쳐', 'VV+EC'), ('나가', 'VX'), ('기', 'ETN'), ('로', 'JKB'), ('했', 'VV+EP'), ('다고', 'EC'), ('밝혔', 'VV+EP'), ('다', 'EF'), ('.', 'SF')]
+> [('금', 'MAJ'), ('통', 'MAG'), ('위', 'NNG'), ('는', 'JX'), ('따라서', 'MAJ'), ('물가', 'NNG'), ('안정', 'NNG'), ('과', 'JC'), ('병행', 'NNG'), (',', 'SC'), ('경기', 'NNG'), ('상황', 'NNG'), ('에', 'JKB'), ('유의', 'NNG'), ('하', 'XSV'), ('는', 'ETM'), ('금리', 'NNG'), ('정책', 'NNG'), ('을', 'JKO'), ('펼쳐', 'VV+EC'), ('나가', 'VX'), ('기', 'ETN'), ('로', 'JKB'), ('했', 'VV+EP'), ('다고', 'EC'), ('밝혔', 'VV+EP'), ('다', 'EF'), ('.', 'SF')]
+
+### cf. MeCab POS Tagging (fugashi)
+
+```python
+from ekonlpy.mecab import MeCab # Be careful! `C` is capital.
+
+mecab = MeCab()
+mecab.pos('금통위는 따라서 물가안정과 병행, 경기상황에 유의하는 금리정책을 펼쳐나가기로 했다고 밝혔다.')
+```
 
 ### Lemmatization and Synonyms
 
 To enhance the accuracy of sentiment analysis, eKoNLPy offers lemmatization and synonym handling features.
 
 ### Adding Words to Dictionary
 
 You can add words to the dictionary in the `ekonlpy.tag` module's Mecab class, either as a string or a list of strings, using the `add_dictionary` method.
 
 ```python
 from ekonlpy.tag import Mecab
+
 mecab = Mecab()
 mecab.add_dictionary('금통위', 'NNG')
 ```
 
 ## Sentiment Analysis
 
 ### Korean Monetary Policy Dictionary (MPKO)
```

