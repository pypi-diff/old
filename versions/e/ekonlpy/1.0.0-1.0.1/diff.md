# Comparing `tmp/ekonlpy-1.0.0.tar.gz` & `tmp/ekonlpy-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ekonlpy-1.0.0.tar", max compression
+gzip compressed data, was "ekonlpy-1.0.1.tar", max compression
```

## Comparing `ekonlpy-1.0.0.tar` & `ekonlpy-1.0.1.tar`

### file list

```diff
@@ -1,75 +1,75 @@
--rw-r--r--   0        0        0     1071 2023-04-07 09:32:21.674900 ekonlpy-1.0.0/LICENSE
--rw-r--r--   0        0        0     5225 2023-04-07 09:32:21.674900 ekonlpy-1.0.0/README.md
--rw-r--r--   0        0        0     3542 2023-04-07 09:32:23.602930 ekonlpy-1.0.0/pyproject.toml
--rw-r--r--   0        0        0      265 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/__init__.py
--rw-r--r--   0        0        0       46 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/_version.py
--rw-r--r--   0        0        0       31 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/data/__init__.py
--rw-r--r--   0        0        0      514 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ADJECTIVES.txt
--rw-r--r--   0        0        0      108 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ADVERBS.txt
--rw-r--r--   0        0        0     2583 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/COUNTRY.txt
--rw-r--r--   0        0        0       17 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/CURRENCY.txt
--rw-r--r--   0        0        0    47727 2023-04-07 09:32:21.754901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ECON_PHRASES.txt
--rw-r--r--   0        0        0   475773 2023-04-07 09:32:21.762901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ECON_TERMS.txt
--rwxr-xr-x   0        0        0    77542 2023-04-07 09:32:21.762901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ENTITY.txt
--rw-r--r--   0        0        0     9629 2023-04-07 09:32:21.762901 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt
--rw-r--r--   0        0        0     2077 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/GENERIC.txt
--rw-r--r--   0        0        0    35442 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt
--rw-r--r--   0        0        0    69192 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/INSTITUTION.txt
--rw-r--r--   0        0        0    20594 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/LEMMA.txt
--rw-r--r--   0        0        0     2072 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/NAMES.txt
--rw-r--r--   0        0        0      687 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/NOUNS.txt
--rw-r--r--   0        0        0    10396 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt
--rw-r--r--   0        0        0    12378 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt
--rw-r--r--   0        0        0    14928 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SECTOR.txt
--rw-r--r--   0        0        0     6456 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/STOPWORDS.txt
--rwxr-xr-x   0        0        0      260 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/STOPWORDS_CUST.txt
--rw-r--r--   0        0        0     5788 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt
--rwxr-xr-x   0        0        0      598 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt
--rw-r--r--   0        0        0    33685 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM.txt
--rw-r--r--   0        0        0      300 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM_MAG.txt
--rw-r--r--   0        0        0     5329 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt
--rw-r--r--   0        0        0    27207 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt
--rw-r--r--   0        0        0       87 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM_VA.txt
--rw-r--r--   0        0        0       69 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/UNIT.txt
--rw-r--r--   0        0        0       40 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/dictionary/VERBS.txt
--rwxr-xr-x   0        0        0     1677 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Currencies.txt
--rwxr-xr-x   0        0        0      724 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/DatesandNumbers.txt
--rwxr-xr-x   0        0        0     1798 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Generic.txt
--rwxr-xr-x   0        0        0     1622 2023-04-07 09:32:21.766902 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Geographic.txt
--rwxr-xr-x   0        0        0  2903900 2023-04-07 09:32:21.778902 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/HIV-4.csv
--rwxr-xr-x   0        0        0  8373373 2023-04-07 09:32:21.818902 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/LM.csv
--rwxr-xr-x   0        0        0    93474 2023-04-07 09:32:21.818902 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Names.txt
--rw-r--r--   0        0        0  3047832 2023-04-07 09:32:21.838903 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv
--rw-r--r--   0        0        0  2362210 2023-04-07 09:32:21.846903 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv
--rwxr-xr-x   0        0        0   778128 2023-04-07 09:32:21.850903 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/kosac/expressive-type.csv
--rwxr-xr-x   0        0        0   661841 2023-04-07 09:32:21.854903 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/kosac/intensity.csv
--rwxr-xr-x   0        0        0   659879 2023-04-07 09:32:21.858903 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/kosac/polarity.csv
--rw-r--r--   0        0        0  3226022 2023-04-07 09:32:21.874903 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv
--rw-r--r--   0        0        0  3832440 2023-04-07 09:32:21.890903 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv
--rw-r--r--   0        0        0  2735025 2023-04-07 09:32:21.902904 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv
--rw-r--r--   0        0        0  3749409 2023-04-07 09:32:21.922904 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv
--rw-r--r--   0        0        0  2835691 2023-04-07 09:32:21.930904 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt
--rw-r--r--   0        0        0    36419 2023-04-07 09:32:21.930904 ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt
--rw-r--r--   0        0        0   281858 2023-04-07 09:32:21.930904 ekonlpy-1.0.0/src/ekonlpy/data/model/MPKC.nbc
--rw-r--r--   0        0        0    15644 2023-04-07 09:32:21.930904 ekonlpy-1.0.0/src/ekonlpy/data/tagset.py
--rw-r--r--   0        0        0       33 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/etag/__init__.py
--rw-r--r--   0        0        0     4210 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/etag/_template.py
--rw-r--r--   0        0        0        0 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/py.typed
--rwxr-xr-x   0        0        0      236 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/__init__.py
--rwxr-xr-x   0        0        0     4149 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/base.py
--rwxr-xr-x   0        0        0     1741 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/euko.py
--rwxr-xr-x   0        0        0     1010 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/hiv4.py
--rw-r--r--   0        0        0     5936 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/kosac.py
--rwxr-xr-x   0        0        0     1054 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/lm.py
--rw-r--r--   0        0        0    16118 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/mpck.py
--rwxr-xr-x   0        0        0     1840 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/mpko.py
--rwxr-xr-x   0        0        0     9245 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/sentiment/utils.py
--rw-r--r--   0        0        0      102 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/tag/__init__.py
--rw-r--r--   0        0        0     7221 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/tag/_mecab.py
--rw-r--r--   0        0        0     2171 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/tag/_postprocess.py
--rw-r--r--   0        0        0     4529 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/tag/_userdic.py
--rw-r--r--   0        0        0    10630 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/tag/mecab.py
--rwxr-xr-x   0        0        0        0 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/utils/__init__.py
--rw-r--r--   0        0        0     3520 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/utils/dictionary.py
--rw-r--r--   0        0        0     6668 2023-04-07 09:32:21.934904 ekonlpy-1.0.0/src/ekonlpy/utils/io.py
--rw-r--r--   0        0        0     6168 1970-01-01 00:00:00.000000 ekonlpy-1.0.0/PKG-INFO
+-rw-r--r--   0        0        0     1071 2023-04-07 09:55:46.263839 ekonlpy-1.0.1/LICENSE
+-rw-r--r--   0        0        0     6544 2023-04-07 09:55:46.263839 ekonlpy-1.0.1/README.md
+-rw-r--r--   0        0        0     3542 2023-04-07 09:55:47.859851 ekonlpy-1.0.1/pyproject.toml
+-rw-r--r--   0        0        0      265 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/__init__.py
+-rw-r--r--   0        0        0       46 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/_version.py
+-rw-r--r--   0        0        0       31 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/__init__.py
+-rw-r--r--   0        0        0      514 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ADJECTIVES.txt
+-rw-r--r--   0        0        0      108 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ADVERBS.txt
+-rw-r--r--   0        0        0     2583 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/COUNTRY.txt
+-rw-r--r--   0        0        0       17 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/CURRENCY.txt
+-rw-r--r--   0        0        0    47727 2023-04-07 09:55:46.339840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_PHRASES.txt
+-rw-r--r--   0        0        0   475773 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_TERMS.txt
+-rwxr-xr-x   0        0        0    77542 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ENTITY.txt
+-rw-r--r--   0        0        0     9629 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt
+-rw-r--r--   0        0        0     2077 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/GENERIC.txt
+-rw-r--r--   0        0        0    35442 2023-04-07 09:55:46.347840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt
+-rw-r--r--   0        0        0    69192 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INSTITUTION.txt
+-rw-r--r--   0        0        0    20594 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/LEMMA.txt
+-rw-r--r--   0        0        0     2072 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NAMES.txt
+-rw-r--r--   0        0        0      687 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NOUNS.txt
+-rw-r--r--   0        0        0    10396 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt
+-rw-r--r--   0        0        0    12378 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt
+-rw-r--r--   0        0        0    14928 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SECTOR.txt
+-rw-r--r--   0        0        0     6456 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS.txt
+-rwxr-xr-x   0        0        0      260 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_CUST.txt
+-rw-r--r--   0        0        0     5788 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt
+-rwxr-xr-x   0        0        0      598 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt
+-rw-r--r--   0        0        0    33685 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM.txt
+-rw-r--r--   0        0        0      300 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_MAG.txt
+-rw-r--r--   0        0        0     5329 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt
+-rw-r--r--   0        0        0    27207 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt
+-rw-r--r--   0        0        0       87 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_VA.txt
+-rw-r--r--   0        0        0       69 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/UNIT.txt
+-rw-r--r--   0        0        0       40 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/dictionary/VERBS.txt
+-rwxr-xr-x   0        0        0     1677 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Currencies.txt
+-rwxr-xr-x   0        0        0      724 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/DatesandNumbers.txt
+-rwxr-xr-x   0        0        0     1798 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Generic.txt
+-rwxr-xr-x   0        0        0     1622 2023-04-07 09:55:46.351840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Geographic.txt
+-rwxr-xr-x   0        0        0  2903900 2023-04-07 09:55:46.363840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/HIV-4.csv
+-rwxr-xr-x   0        0        0  8373373 2023-04-07 09:55:46.399840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/LM.csv
+-rwxr-xr-x   0        0        0    93474 2023-04-07 09:55:46.399840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Names.txt
+-rw-r--r--   0        0        0  3047832 2023-04-07 09:55:46.415840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv
+-rw-r--r--   0        0        0  2362210 2023-04-07 09:55:46.427840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv
+-rwxr-xr-x   0        0        0   778128 2023-04-07 09:55:46.431840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/expressive-type.csv
+-rwxr-xr-x   0        0        0   661841 2023-04-07 09:55:46.431840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/intensity.csv
+-rwxr-xr-x   0        0        0   659879 2023-04-07 09:55:46.435840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/polarity.csv
+-rw-r--r--   0        0        0  3226022 2023-04-07 09:55:46.451840 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv
+-rw-r--r--   0        0        0  3832440 2023-04-07 09:55:46.467841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv
+-rw-r--r--   0        0        0  2735025 2023-04-07 09:55:46.479841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv
+-rw-r--r--   0        0        0  3749409 2023-04-07 09:55:46.499841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv
+-rw-r--r--   0        0        0  2835691 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt
+-rw-r--r--   0        0        0    36419 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt
+-rw-r--r--   0        0        0   281858 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/model/MPKC.nbc
+-rw-r--r--   0        0        0    15644 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/data/tagset.py
+-rw-r--r--   0        0        0       33 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/etag/__init__.py
+-rw-r--r--   0        0        0     4210 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/etag/_template.py
+-rw-r--r--   0        0        0        0 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/py.typed
+-rwxr-xr-x   0        0        0      236 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/__init__.py
+-rwxr-xr-x   0        0        0     4149 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/base.py
+-rwxr-xr-x   0        0        0     1741 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/euko.py
+-rwxr-xr-x   0        0        0     1010 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/hiv4.py
+-rw-r--r--   0        0        0     5936 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/kosac.py
+-rwxr-xr-x   0        0        0     1054 2023-04-07 09:55:46.507841 ekonlpy-1.0.1/src/ekonlpy/sentiment/lm.py
+-rw-r--r--   0        0        0    16118 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/sentiment/mpck.py
+-rwxr-xr-x   0        0        0     1840 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/sentiment/mpko.py
+-rwxr-xr-x   0        0        0     9268 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/sentiment/utils.py
+-rw-r--r--   0        0        0      102 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/__init__.py
+-rw-r--r--   0        0        0     7221 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/_mecab.py
+-rw-r--r--   0        0        0     2171 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/_postprocess.py
+-rw-r--r--   0        0        0     4529 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/_userdic.py
+-rw-r--r--   0        0        0    10630 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/tag/mecab.py
+-rwxr-xr-x   0        0        0        0 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/utils/__init__.py
+-rw-r--r--   0        0        0     3520 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/utils/dictionary.py
+-rw-r--r--   0        0        0     6668 2023-04-07 09:55:46.511841 ekonlpy-1.0.1/src/ekonlpy/utils/io.py
+-rw-r--r--   0        0        0     7487 1970-01-01 00:00:00.000000 ekonlpy-1.0.1/PKG-INFO
```

### Comparing `ekonlpy-1.0.0/LICENSE` & `ekonlpy-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/README.md` & `ekonlpy-1.0.1/README.md`

 * *Files 19% similar despite different names*

```diff
@@ -1,9 +1,33 @@
 # eKoNLPy: Korean NLP Python Library for Economic Analysis
 
+[![pypi-image]][pypi-url]
+[![version-image]][release-url]
+[![release-date-image]][release-url]
+[![license-image]][license-url]
+
+<!-- Links: -->
+
+[pypi-image]: https://badge.fury.io/py/ekonlpy.svg
+[pypi-url]: https://badge.fury.io/py/ekonlpy
+[license-image]: https://img.shields.io/github/license/entelecheia/eKoNLPy
+[license-url]: https://github.com/entelecheia/eKoNLPy/blob/master/LICENSE
+[version-image]: https://img.shields.io/github/v/release/entelecheia/eKoNLPy?sort=semver
+[release-date-image]: https://img.shields.io/github/release-date/entelecheia/eKoNLPy
+[release-url]: https://github.com/entelecheia/eKoNLPy/releases
+[conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
+[conventional commits]: https://conventionalcommits.org
+[repo-url]: https://github.com/entelecheia/eKoNLPy
+[pypi-url]: https://pypi.org/project/ekonlpy
+[docs-url]: https://ekonlpy.entelecheia.ai
+[changelog]: https://github.com/entelecheia/eKoNLPy/blob/master/CHANGELOG.md
+[contributing guidelines]: https://github.com/entelecheia/eKoNLPy/blob/master/CONTRIBUTING.md
+
+<!-- Links: -->
+
 `eKoNLPy` is a Korean Natural Language Processing (NLP) Python library specifically designed for economic analysis. It extends the functionality of the `MeCab` tagger from KoNLPy to improve the handling of economic terms, financial institutions, and company names, classifying them as single nouns. Additionally, it incorporates sentiment analysis features to determine the tone of monetary policy statements, such as Hawkish or Dovish.
 
 ## Installation
 
 To install eKoNLPy, run the following command:
 
 ```bash
@@ -104,17 +128,25 @@
 from ekonlpy.sentiment import LM
 
 lm = LM()
 tokens = lm.tokenize(text)
 score = lm.get_score(tokens)
 ```
 
+## Changelog
+
+See the [CHANGELOG] for more information.
+
+## Contributing
+
+Contributions are welcome! Please see the [contributing guidelines] for more information.
+
 ## License
 
-eKoNLPy is an open-source software library for Korean Natural Language Processing (NLP), specifically designed for economic analysis. The library is released under the [MIT License](LICENSE), allowing developers and researchers to use, modify, and distribute the software as they see fit.
+eKoNLPy is an open-source software library for Korean Natural Language Processing (NLP), specifically designed for economic analysis. The library is released under the [MIT License][license-url], allowing developers and researchers to use, modify, and distribute the software as they see fit.
 
 ## Citation
 
 If you use eKoNLPy in your work or research, please cite the following sources:
 
 - Lee, Young Joon, eKoNLPy: A Korean NLP Python Library for Economic Analysis, 2018. Available at: https://github.com/entelecheia/eKoNLPy.
 - Lee, Young Joon, Soohyon Kim, and Ki Young Park. "Deciphering Monetary Policy Board Minutes with Text Mining: The Case of South Korea." Korean Economic Review 35 (2019): 471-511.
```

### Comparing `ekonlpy-1.0.0/pyproject.toml` & `ekonlpy-1.0.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "eKoNLPy"
-version = "1.0.0"
+version = "1.0.1"
 description = "A Korean natural language processing toolkit for economic analysis"
 authors = ["Young Joon Lee <entelecheia@hotmail.com>"]
 license = "MIT"
 readme = "README.md"
 packages = [{ include = "ekonlpy", from = "src" }]
 homepage = "https://ekonlpy.entelecheia.ai/"
 repository = "https://github.com/entelecheia/eKoNLPy"
```

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ADJECTIVES.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ADJECTIVES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/COUNTRY.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/COUNTRY.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ECON_PHRASES.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_PHRASES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ECON_TERMS.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ECON_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/ENTITY.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/ENTITY.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/FOREIGN_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/GENERIC.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/GENERIC.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INDUSTRY_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/INSTITUTION.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/INSTITUTION.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/LEMMA.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/LEMMA.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/NAMES.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NAMES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/NOUNS.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/NOUNS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/POLARITY_PHRASES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/PROPER_NOUNS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SECTOR.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SECTOR.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/STOPWORDS.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_EN.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/STOPWORDS_KOR.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_PHRASES.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/dictionary/SYNONYM_TERMS.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Currencies.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Currencies.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/DatesandNumbers.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/DatesandNumbers.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Generic.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Generic.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Geographic.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Geographic.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/HIV-4.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/HIV-4.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/LM.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/LM.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/Names.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/Names.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_lex.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/euko/mp_uncertainty_lexicon_mkt.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/kosac/expressive-type.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/expressive-type.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/kosac/intensity.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/intensity.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/kosac/polarity.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/kosac/polarity.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_lex.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n3.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_lexicon_mkt_n7.csv`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_vocab.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt` & `ekonlpy-1.0.1/src/ekonlpy/data/lexicon/mpko/mp_polarity_wordset.txt`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/model/MPKC.nbc` & `ekonlpy-1.0.1/src/ekonlpy/data/model/MPKC.nbc`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/data/tagset.py` & `ekonlpy-1.0.1/src/ekonlpy/data/tagset.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/etag/_template.py` & `ekonlpy-1.0.1/src/ekonlpy/etag/_template.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/base.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/base.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/euko.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/euko.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/hiv4.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/hiv4.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/kosac.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/kosac.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/lm.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/lm.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/mpck.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/mpck.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/mpko.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/mpko.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/sentiment/utils.py` & `ekonlpy-1.0.1/src/ekonlpy/sentiment/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -233,15 +233,15 @@
                     wordset.add(word)
             fin.close()
         return wordset
 
     def get_vocab(self, file):
         vocab = {}
         vocab_path = os.path.join(LEXICON_PATH, file)
-        with open(vocab_path) as f:
+        with open(vocab_path, "r", encoding="utf-8") as f:
             for i, line in enumerate(f):
                 w = line.strip().split()
                 if len(w[0]) > 0:
                     vocab[w[0]] = w[1]
         return vocab
```

### Comparing `ekonlpy-1.0.0/src/ekonlpy/tag/_mecab.py` & `ekonlpy-1.0.1/src/ekonlpy/tag/_mecab.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/tag/_postprocess.py` & `ekonlpy-1.0.1/src/ekonlpy/tag/_postprocess.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/tag/_userdic.py` & `ekonlpy-1.0.1/src/ekonlpy/tag/_userdic.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/tag/mecab.py` & `ekonlpy-1.0.1/src/ekonlpy/tag/mecab.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/utils/dictionary.py` & `ekonlpy-1.0.1/src/ekonlpy/utils/dictionary.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/src/ekonlpy/utils/io.py` & `ekonlpy-1.0.1/src/ekonlpy/utils/io.py`

 * *Files identical despite different names*

### Comparing `ekonlpy-1.0.0/PKG-INFO` & `ekonlpy-1.0.1/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ekonlpy
-Version: 1.0.0
+Version: 1.0.1
 Summary: A Korean natural language processing toolkit for economic analysis
 Home-page: https://ekonlpy.entelecheia.ai/
 License: MIT
 Keywords: KoNLPy,Tokenization,Sentiment analysis,Monetary policy
 Author: Young Joon Lee
 Author-email: entelecheia@hotmail.com
 Requires-Python: >=3.8.1,<3.12
@@ -20,14 +20,38 @@
 Requires-Dist: pandas (>=2.0.0,<3.0.0)
 Requires-Dist: scipy (>=1.10.1,<2.0.0)
 Project-URL: Repository, https://github.com/entelecheia/eKoNLPy
 Description-Content-Type: text/markdown
 
 # eKoNLPy: Korean NLP Python Library for Economic Analysis
 
+[![pypi-image]][pypi-url]
+[![version-image]][release-url]
+[![release-date-image]][release-url]
+[![license-image]][license-url]
+
+<!-- Links: -->
+
+[pypi-image]: https://badge.fury.io/py/ekonlpy.svg
+[pypi-url]: https://badge.fury.io/py/ekonlpy
+[license-image]: https://img.shields.io/github/license/entelecheia/eKoNLPy
+[license-url]: https://github.com/entelecheia/eKoNLPy/blob/master/LICENSE
+[version-image]: https://img.shields.io/github/v/release/entelecheia/eKoNLPy?sort=semver
+[release-date-image]: https://img.shields.io/github/release-date/entelecheia/eKoNLPy
+[release-url]: https://github.com/entelecheia/eKoNLPy/releases
+[conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
+[conventional commits]: https://conventionalcommits.org
+[repo-url]: https://github.com/entelecheia/eKoNLPy
+[pypi-url]: https://pypi.org/project/ekonlpy
+[docs-url]: https://ekonlpy.entelecheia.ai
+[changelog]: https://github.com/entelecheia/eKoNLPy/blob/master/CHANGELOG.md
+[contributing guidelines]: https://github.com/entelecheia/eKoNLPy/blob/master/CONTRIBUTING.md
+
+<!-- Links: -->
+
 `eKoNLPy` is a Korean Natural Language Processing (NLP) Python library specifically designed for economic analysis. It extends the functionality of the `MeCab` tagger from KoNLPy to improve the handling of economic terms, financial institutions, and company names, classifying them as single nouns. Additionally, it incorporates sentiment analysis features to determine the tone of monetary policy statements, such as Hawkish or Dovish.
 
 ## Installation
 
 To install eKoNLPy, run the following command:
 
 ```bash
@@ -128,17 +152,25 @@
 from ekonlpy.sentiment import LM
 
 lm = LM()
 tokens = lm.tokenize(text)
 score = lm.get_score(tokens)
 ```
 
+## Changelog
+
+See the [CHANGELOG] for more information.
+
+## Contributing
+
+Contributions are welcome! Please see the [contributing guidelines] for more information.
+
 ## License
 
-eKoNLPy is an open-source software library for Korean Natural Language Processing (NLP), specifically designed for economic analysis. The library is released under the [MIT License](LICENSE), allowing developers and researchers to use, modify, and distribute the software as they see fit.
+eKoNLPy is an open-source software library for Korean Natural Language Processing (NLP), specifically designed for economic analysis. The library is released under the [MIT License][license-url], allowing developers and researchers to use, modify, and distribute the software as they see fit.
 
 ## Citation
 
 If you use eKoNLPy in your work or research, please cite the following sources:
 
 - Lee, Young Joon, eKoNLPy: A Korean NLP Python Library for Economic Analysis, 2018. Available at: https://github.com/entelecheia/eKoNLPy.
 - Lee, Young Joon, Soohyon Kim, and Ki Young Park. "Deciphering Monetary Policy Board Minutes with Text Mining: The Case of South Korea." Korean Economic Review 35 (2019): 471-511.
```

