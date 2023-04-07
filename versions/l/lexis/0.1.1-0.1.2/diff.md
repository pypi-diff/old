# Comparing `tmp/lexis-0.1.1.tar.gz` & `tmp/lexis-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lexis-0.1.1.tar", last modified: Wed Oct 26 14:21:42 2022, max compression
+gzip compressed data, was "lexis-0.1.2.tar", last modified: Fri Apr  7 09:18:02 2023, max compression
```

## Comparing `lexis-0.1.1.tar` & `lexis-0.1.2.tar`

### file list

```diff
@@ -1,15 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 14:21:42.991392 lexis-0.1.1/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-10-26 14:21:17.000000 lexis-0.1.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)    23815 2022-10-26 14:21:42.991392 lexis-0.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    17707 2022-10-26 14:21:17.000000 lexis-0.1.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 14:21:42.987392 lexis-0.1.1/lexis/
--rw-r--r--   0 runner    (1001) docker     (121)    16589 2022-10-26 14:21:17.000000 lexis-0.1.1/lexis/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 14:21:42.991392 lexis-0.1.1/lexis.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    23815 2022-10-26 14:21:42.000000 lexis-0.1.1/lexis.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      226 2022-10-26 14:21:42.000000 lexis-0.1.1/lexis.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-26 14:21:42.000000 lexis-0.1.1/lexis.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-26 14:21:42.000000 lexis-0.1.1/lexis.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-10-26 14:21:42.000000 lexis-0.1.1/lexis.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        6 2022-10-26 14:21:42.000000 lexis-0.1.1/lexis.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      633 2022-10-26 14:21:42.991392 lexis-0.1.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)       91 2022-10-26 14:21:17.000000 lexis-0.1.1/setup.py
+drwxr-xr-x   0 thorwhalen   (501) staff       (20)        0 2023-04-07 09:18:02.050221 lexis-0.1.2/
+-rw-r--r--   0 thorwhalen   (501) staff       (20)    11357 2022-10-25 12:59:01.000000 lexis-0.1.2/LICENSE
+-rw-r--r--   0 thorwhalen   (501) staff       (20)    18080 2023-04-07 09:18:02.051095 lexis-0.1.2/PKG-INFO
+-rw-r--r--   0 thorwhalen   (501) staff       (20)    17707 2022-10-25 12:59:01.000000 lexis-0.1.2/README.md
+drwxr-xr-x   0 thorwhalen   (501) staff       (20)        0 2023-04-07 09:18:01.811113 lexis-0.1.2/lexis/
+-rw-r--r--   0 thorwhalen   (501) staff       (20)    18660 2023-04-07 09:16:47.000000 lexis-0.1.2/lexis/__init__.py
+drwxr-xr-x   0 thorwhalen   (501) staff       (20)        0 2023-04-07 09:18:02.030134 lexis-0.1.2/lexis/examples/
+-rw-r--r--   0 thorwhalen   (501) staff       (20)       85 2023-04-07 08:56:52.000000 lexis-0.1.2/lexis/examples/__init__.py
+-rw-r--r--   0 thorwhalen   (501) staff       (20)     2675 2023-04-07 09:16:47.000000 lexis-0.1.2/lexis/examples/drawing_games.py
+drwxr-xr-x   0 thorwhalen   (501) staff       (20)        0 2023-04-07 09:18:02.004335 lexis-0.1.2/lexis.egg-info/
+-rw-r--r--   0 thorwhalen   (501) staff       (20)    18080 2023-04-07 09:18:01.000000 lexis-0.1.2/lexis.egg-info/PKG-INFO
+-rw-r--r--   0 thorwhalen   (501) staff       (20)      285 2023-04-07 09:18:01.000000 lexis-0.1.2/lexis.egg-info/SOURCES.txt
+-rw-r--r--   0 thorwhalen   (501) staff       (20)        1 2023-04-07 09:18:01.000000 lexis-0.1.2/lexis.egg-info/dependency_links.txt
+-rw-r--r--   0 thorwhalen   (501) staff       (20)        1 2023-04-07 09:18:01.000000 lexis-0.1.2/lexis.egg-info/not-zip-safe
+-rw-r--r--   0 thorwhalen   (501) staff       (20)       12 2023-04-07 09:18:01.000000 lexis-0.1.2/lexis.egg-info/requires.txt
+-rw-r--r--   0 thorwhalen   (501) staff       (20)        6 2023-04-07 09:18:01.000000 lexis-0.1.2/lexis.egg-info/top_level.txt
+-rw-r--r--   0 thorwhalen   (501) staff       (20)      633 2023-04-07 09:18:02.056835 lexis-0.1.2/setup.cfg
+-rw-r--r--   0 thorwhalen   (501) staff       (20)       91 2022-10-25 12:59:01.000000 lexis-0.1.2/setup.py
```

### Comparing `lexis-0.1.1/LICENSE` & `lexis-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `lexis-0.1.1/PKG-INFO` & `lexis-0.1.2/PKG-INFO`

 * *Files 22% similar despite different names*

```diff
@@ -1,729 +1,730 @@
 Metadata-Version: 2.1
 Name: lexis
-Version: 0.1.1
+Version: 0.1.2
 Summary: Wordnet wrapper - Easy access to words and their relationships
 Home-page: https://github.com/thorwhalen/lexis
 Author: Thor Whalen
 License: apache-2.0
-Description: 
-        # lexis
-        Wordnet wrapper - Easy access to words and their relationships
-        
-        To install:	```pip install lexis```
-        
-        The key-value (i.e. dict-list) wrapper to nltk.corpus.wordnet.
-        
-        Your no fuss gateway to (English) words.
-        
-        The easiest way to get nltk.corpus.wordnet is
-        
-        The `nltk` dependency is installed for you when installing 
-        `lexis`, but the wordnet data is not downloaded automatically.
-        To do so (only once), go to a python console and do:
-        ```
-        >>> import nltk; nltk.download('wordnet')  # doctest: +SKIP
-        ```
-        
-        If you don't like that way, [see here](https://www.nltk.org/install.html) 
-        for other ways to get wordnet.
-        
-        The central construct of this module is the Synset 
-        (a set of synonyms that share a common meaning).
-        To see a few things you can do with Synsets, naked, 
-        [see here](https://www.nltk.org/howto/wordnet.html).
-        
-        Here we put a py2store wrapper around this stuff.
-        
-        What is WordNet? https://wordnet.princeton.edu/
-        
-        
-        # A little peek at Lemmas
-        
-        
-        ```python
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        len(lm)
-        ```
-        
-        
-        
-        
-            147306
-        
-        
-        
-        `lm` is a `Mapping` (think "acts like a (read-only) dict")
-        
-        
-        ```python
-        from typing import Mapping
-        
-        isinstance(lm, Mapping)
-        ```
-        
-        
-        
-        
-            True
-        
-        
-        
-        Let's have a look at a few keys
-        
-        
-        ```python
-        list(lm)[44630:44635]
-        ```
-        
-        
-        
-        
-            ['blond', 'kaunda', 'peacetime', 'intolerantly', "'hood"]
-        
-        
-        
-        And the value of a `lm` item?
-        
-        
-        ```python
-        lm['blond']
-        ```
-        
-        
-        
-        
-            {'blond.n.01': WordnetElement('blond.n.01'),
-             'blond.n.02': WordnetElement('blond.n.02'),
-             'blond.a.01': WordnetElement('blond.a.01')}
-        
-        
-        
-        Okay, it looks like it's different meanings of "blond". The middle letter tells us its grammatical role it's a noun (`n`) or an adjective (`a`). More on that later. 
-        
-        And what's a `WordnetElement`?
-        
-        Well, it's another Mapping, apparently:
-        
-        
-        ```python
-        isinstance(lm['blond']['blond.n.01'], Mapping)
-        ```
-        
-        
-        
-        
-            True
-        
-        
-        
-        
-        ```python
-        list(lm['blond']['blond.n.01'])
-        ```
-        
-        
-        
-        
-            ['also_sees',
-             'instance_hypernyms',
-             'verb_groups',
-             'entailments',
-             'region_domains',
-             'substance_holonyms',
-             'part_holonyms',
-             'examples',
-             'part_meronyms',
-             'hyponyms',
-             'member_meronyms',
-             'offset',
-             'causes',
-             'definition',
-             'lemma_names',
-             'lexname',
-             'member_holonyms',
-             'in_topic_domains',
-             'lemmas',
-             'topic_domains',
-             'max_depth',
-             'hypernym_distances',
-             'name',
-             'attributes',
-             'hypernyms',
-             'min_depth',
-             'usage_domains',
-             'in_region_domains',
-             'instance_hyponyms',
-             'in_usage_domains',
-             'similar_tos',
-             'root_hypernyms',
-             'pos',
-             'frame_ids',
-             'hypernym_paths',
-             'substance_meronyms']
-        
-        
-        
-        Wow! That's a lot of information! 
-        
-        Let's look at what the definition of `'blond.n.01'` is:
-        
-        
-        ```python
-        print(lm['blond']['blond.n.01']['definition'])
-        ```
-        
-            a person with fair skin and hair
-        
-        
-        ... actually, let's just poke at all of them (at least those that are non-empty)
-        
-        
-        ```python
-        meaning = 'blond.n.01'
-        print(f"Values for meaning: {meaning}")
-        for k, v in lm['blond'][meaning].items():
-            if v:
-                print(f"- {k}: {v}")
-        ```
-        
-            Values for meaning: blond.n.01
-            - hyponyms: [WordnetElement('peroxide_blond.n.01'), WordnetElement('platinum_blond.n.01'), WordnetElement('towhead.n.01')]
-            - offset: 9860506
-            - definition: a person with fair skin and hair
-            - lemma_names: ['blond', 'blonde']
-            - lexname: noun.person
-            - lemmas: [KvLemma('blond.n.01.blond'), KvLemma('blond.n.01.blonde')]
-            - max_depth: 7
-            - hypernym_distances: {(WordnetElement('physical_entity.n.01'), 6), (WordnetElement('entity.n.01'), 7), (WordnetElement('physical_entity.n.01'), 3), (WordnetElement('entity.n.01'), 4), (WordnetElement('living_thing.n.01'), 3), (WordnetElement('object.n.01'), 5), (WordnetElement('blond.n.01'), 0), (WordnetElement('organism.n.01'), 2), (WordnetElement('causal_agent.n.01'), 2), (WordnetElement('whole.n.02'), 4), (WordnetElement('person.n.01'), 1)}
-            - name: blond.n.01
-            - hypernyms: [WordnetElement('person.n.01')]
-            - min_depth: 4
-            - root_hypernyms: [Synset('entity.n.01')]
-            - pos: n
-            - hypernym_paths: [[WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('causal_agent.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')], [WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('object.n.01'), WordnetElement('whole.n.02'), WordnetElement('living_thing.n.01'), WordnetElement('organism.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')]]
-        
-        
-        ## You can get meaning information directly
-        
-        What if you made a list of these strings like `'blond.n.01'`, `'blond.a.01'`... and you wanted to access the `WordnetElement` instances with all that cool information about those specifics meanings?
-        
-        You could do `lm['blond']['blond.n.01']`, `lm['blond']['blond.a.01']`... But then you'd have to remember the full references `('blond', 'blond.n.01')`, `('blond', 'blond.a.01')`... 
-        
-        You don't need to go through `lm['blond']` to get to the `WordnetElement` instance that gives you access to the meaning information -- you can use the `Synsets` store (i.e. Mapping). 
-        
-        Note: "synset" is what Wordnet calls this. We'll just call is meaning for simplicity. I hope the purists won't mind.
-        
-        
-        
-        ```python
-        from lexis import Synsets
-        ```
-        
-        
-        ```python
-        meanings = Synsets()
-        meanings['blond.n.01']
-        ```
-        
-        
-        
-        
-            WordnetElement('blond.n.01')
-        
-        
-        
-        We saw earlier that we had `147306` lemmas (i.e. "words" or more precisely "terms"... but really precisely, "lemmas"). 
-        
-        Well, we have `117659` synsets (i.e. "meanings") in the `Synsets` instance.
-        
-        
-        ```python
-        len(meanings)
-        ```
-        
-        
-        
-        
-            117659
-        
-        
-        
-        ## Multiple lemma names
-        
-        `'lemma_names'` are different ways that the same meaning can be written. 
-        
-        
-        ```python
-        lm['blond']['blond.n.01']['lemma_names']
-        ```
-        
-        
-        
-        
-            ['blond', 'blonde']
-        
-        
-        
-        Indeed, `lm['blond']` and `lm['blonde']` really point to the same thing.
-        
-        
-        ```python
-        lm['blond']
-        ```
-        
-        
-        
-        
-            {'blond.n.01': WordnetElement('blond.n.01'),
-             'blond.n.02': WordnetElement('blond.n.02'),
-             'blond.a.01': WordnetElement('blond.a.01')}
-        
-        
-        
-        
-        ```python
-        lm['blonde']
-        ```
-        
-        
-        
-        
-            {'blond.n.01': WordnetElement('blond.n.01'),
-             'blond.n.02': WordnetElement('blond.n.02'),
-             'blond.a.01': WordnetElement('blond.a.01')}
-        
-        
-        
-        ## Grammatical roles
-        
-        What are the different grammatical roles that are used in the meaning identifiers (aka synset keys) of our lemmas?
-        
-        
-        ```python
-        from collections import Counter
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
-        
-        def extract_grammatical_role_from_meaning(meaning):
-            m = p_middle_of_dot_path.match(meaning)
-            if m:
-                return m.groupdict().get('middle', None) 
-            else:
-                return None
-            
-        
-        c = Counter()
-        for meanings in lm.values():
-            for meaning in meanings:
-                c.update(extract_grammatical_role_from_meaning(meaning))
-                
-        c.most_common()
-        ```
-        
-        
-        
-        
-            [('n', 148478),
-             ('v', 42751),
-             ('s', 20895),
-             ('a', 9846),
-             ('r', 5619),
-             ('_', 29),
-             ('e', 28),
-             ('u', 17),
-             ('g', 17),
-             ('i', 15),
-             ('t', 14),
-             ('p', 8),
-             ('b', 7),
-             ('o', 7),
-             ('l', 6),
-             ('d', 4),
-             ('c', 2),
-             ('m', 1),
-             ('k', 1)]
-        
-        
-        
-        
-        # Miscellaneous explorations
-        
-        ```python
-        from py2store import filt_iter, cached_keys, add_ipython_key_completions
-        from py2store import kvhead
-        from lexis import Lemmas
-        ```
-        
-        
-        ```python
-        lm = Lemmas()
-        
-        def print_definitions(words):
-            for word in words:
-                print(f"- {word}")
-                for k, v in lm[word].items():
-                    print(f"    {'.'.join(k.split('.')[1:])}: {v['definition']}")
-        
-        ```
-        
-        ## Find words containing some substring
-        
-        
-        ```python
-        from lexis import print_word_definitions
-        ```
-        
-        
-        ```python
-        substr = 'iep'
-        words = list(filter(lambda w: substr in w, lm))
-        len(words)
-        ```
-        
-        
-            12
-        
-        
-        ```python
-        print_definitions(words)
-        ```
-        
-            - hemiepiphyte
-                n.01: a plant that is an epiphyte for part of its life
-            - antiepileptic
-                n.01: a drug used to treat or prevent convulsions (as in epilepsy)
-            - pieplant
-                n.01: long pinkish sour leafstalks usually eaten cooked and sweetened
-            - liepaja
-                n.01: a city of southwestern Latvia on the Baltic Sea
-            - semiepiphyte
-                n.01: a plant that is an epiphyte for part of its life
-            - archiepiscopal
-                a.01: of or associated with an archbishop
-            - tiepin
-                n.01: a pin used to hold the tie in place
-            - giovanni_battista_tiepolo
-                n.01: Italian painter (1696-1770)
-            - tiepolo
-                n.01: Italian painter (1696-1770)
-            - antiepileptic_drug
-                n.01: a drug used to treat or prevent convulsions (as in epilepsy)
-            - dnieper
-                n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
-            - dnieper_river
-                n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
-        
-        ## Find palindrome
-        
-        ```python
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        is_palendrome_with_at_least_3_letters = lambda w: len(w) >= 3 and w == w[::-1]
-        print(*filter(is_palendrome_with_at_least_3_letters, lm), sep=', ')
-        ```
-        
-            ono, waw, tot, kkk, ldl, anna, tenet, mom, igigi, sus, hallah, sls, pcp, mam, ofo, ene, alula, oto, civic, cfc, 101, tet, kazak, sss, ctc, aba, tevet, ara, wnw, mum, siris, tebet, tut-tut, ccc, naan, xix, tnt, peep, tut, kook, xanax, ala, eve, level, xxx, dud, aaa, dad, tdt, odo, pip, tibit, iii, sas, wow, radar, madam, yay, dmd, poop, ana, sos, bib, pop, isi, eye, gag, gig, cdc, dod, nun, pep, mym, bob, malayalam, sis, www, utu, non, ewe, aga, akka, noon, ese, rotor, ded, ppp, kayak, pap, wsw, pup, minim, nan, tat, ada, boob, mem, deed, nauruan, ma'am, succus, seles, cbc, tit, dvd, refer, toot
-        
-        
-        Wait a minute... Where's racecar?!? Isn't that a palindrome?
-        ```python
-        # 
-        assert 'racecar' not in lm
-        assert 'race_car' in lm
-        ```
-        
-        ### Which of these are (or rather "can be") a verb?
-        
-        What are the keys of the lemmas? 
-        
-        Answer: Synset keys -- that is, an id that references a unit of meaning
-        
-        
-        ```python
-        # what do are the values of the lemmas?
-        list(lm['eat'])
-        ```
-        
-        
-        
-        
-            ['eat.v.01',
-             'eat.v.02',
-             'feed.v.06',
-             'eat.v.04',
-             'consume.v.05',
-             'corrode.v.01']
-        
-        
-        
-        That little `v` seems to be indicating that the meaning is... verbal?
-        
-        Let's make a function to grab that middle part of the dot path and use it to make a `is_a_verb` (more like "can be a verb"). 
-        
-        
-        ```python
-        from collections import Counter
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
-        
-        def _extract_middle(string):
-            m = p_middle_of_dot_path.match(string)
-            if m:
-                return m.groupdict().get('middle', None) 
-            else:
-                return None
-            
-        def grammatical_roles(lemma):
-            return Counter(map(_extract_middle, lm[lemma]))
-            
-        
-        assert grammatical_roles('go') == Counter({'n': 4, 'v': 30, 'a': 1})  # the lemma "go" can be a verb, noun, or adjective
-        
-        def is_a_verb(lemma):
-            return 'v' in grammatical_roles(lemma)
-            
-        assert is_a_verb('go')
-        assert not is_a_verb('chess')  # unlike go, chess cannot be used as a verb, apparently
-        ```
-        
-        Palendromes that are verbs
-        
-        
-        ```python
-        list(filter(lambda x: is_a_verb(x) and is_palendrome_with_at_least_3_letters(x), lm))
-        ```
-        
-        
-        
-        
-            ['tot',
-             'tut-tut',
-             'peep',
-             'tut',
-             'level',
-             'pip',
-             'wow',
-             'bib',
-             'pop',
-             'eye',
-             'gag',
-             'bob',
-             'kayak',
-             'pup',
-             'tat',
-             'boob',
-             'refer',
-             'toot']
-        
-        
-        
-        
-        ## Only p, q, b, d, and vowels
-        
-        
-        ```python
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        consonants = 'pqbd'
-        vowels = 'aeiou'  # 'aeiouy'
-        filt = re.compile(f'[{vowels}{consonants}]+$').match  # the pattern
-        
-        words = list(filter(lambda w: 2 <= len(w)  <= 7, # number of letters constraing
-                            filter(filt, lm)))  # filter for iep pattern
-        len(words)
-        ```
-        
-        
-        
-        
-            249
-        
-        
-        
-        
-        ```python
-        print(*words, sep='\t')
-        ```
-        
-            bod	aaa	add	poa	pop	beaded	aqua	pib	edda	doob	boa	doi	padded	iodide	bop	edo	bide	eb	bai	quid	de	ade	daba	pid	baba	paba	bi	abb	bebop	pa	poop	pb	dea	odo	pope	dad	pup	bode	quad	bb	be	ea	epee	bid	pu	pique	iii	pod	bee	pub	ddi	id	baobab	equid	padua	pipidae	opaque	pappa	uppp	uub	qepiq	bibbed	adp	ada	pied	aoudad	qed	pupa	bedaub	bd	dba	bopeep	oboe	ado	eq	bpi	aid	bud	dodo	abo	qaeda	aa	pad	papua	baa	abode	bad	adad	adapid	papaia	db	bede	ai	po	doei	pep	eib	dubai	epi	boob	uuq	io	beep	quip	ad	babu	ded	ia	dud	da	qi	paid	peep	doodad	beda	eddo	boo	padda	ipidae	deep	dope	ied	doped	dopa	ii	iaea	uda	dd	baud	dido	ebb	epa	bodied	pap	ed	peba	bed	audio	deed	idea	apoidea	beau	up	pda	iud	ip	diode	bida	pi	apidae	bead	odd	od	dia	baddie	iaa	ape	ipo	dod	idp	ee	ie	daub	duo	boidae	poe	abed	adobe	pea	dude	do	aided	obi	ido	pipe	pe	doe	aiai	pd	baboo	quipu	pood	papio	equidae	iop	qadi	ab	dado	dub	adobo	bap	pei	baeda	equip	dupe	aqaba	bob	ba	dead	dada	adapa	pee	opepe	pob	iou	duad	doodia	dab	aide	pip	dipped	bubo	pipa	poi	apia	ode	upupa	iq	aba	abbe	edp	edd	pia	due	pud	ob	audad	dp	deb	pie	oed	die	ppp	queue	papa	adieu	biped	babe	ida	dubuque	dip	uup	eu	ipod	bade	au	abide	bib	bedded
-        
-        
-        
-        ```python
-        print_definitions(['adapa'])
-        ```
-        
-            - adapa
-                n.01: a Babylonian demigod or first man (sometimes identified with Adam)
-        
-        
-        ### Containing i, e, p in that order, with other letters in between
-        
-        
-        ```python
-        filt = re.compile('\w{0,2}i\w{0,2}e\w{0,2}p\w{0,2}$').match  # The *i*e*p* pattern
-        
-        words = list(filter(lambda w: len(w) <= 6, # no more than 6 letters
-                            filter(filt, lm)))  # filter for iep pattern
-        print_definitions(words)
-        ```
-        
-        
-        
-        
-            9
-        
-        
-        
-        
-        ```python
-        print(*words, sep=', ')
-        ```
-        
-            tie_up, ginep, lineup, inept, pileup, tiepin, biceps, icecap, ice_up
-        
-        
-        
-        ```python
-        print_definitions(words)
-        ```
-        
-            - tie_up
-                v.01: secure with or as if with ropes
-                v.02: invest so as to make unavailable for other purposes
-                v.03: restrain from moving or operating normally
-                v.01: secure in or as if in a berth or dock
-                v.05: finish the last row
-            - ginep
-                n.01: tropical American tree bearing a small edible fruit with green leathery skin and sweet juicy translucent pulp
-            - lineup
-                n.01: (baseball) a list of batters in the order in which they will bat
-                n.02: a line of persons arranged by police for inspection or identification
-            - inept
-                s.04: not elegant or graceful in expression
-                s.02: generally incompetent and ineffectual
-                s.03: revealing lack of perceptiveness or judgment or finesse
-            - pileup
-                n.01: multiple collisions of vehicles
-            - tiepin
-                n.01: a pin used to hold the tie in place
-            - biceps
-                n.01: any skeletal muscle having two origins (but especially the muscle that flexes the forearm)
-            - icecap
-                n.01: a mass of ice and snow that permanently covers a large area of land (e.g., the polar regions or a mountain peak)
-            - ice_up
-                v.01: become covered with a layer of ice; of a surface such as a window
-        
-        
-        
-        ## S-words
-        
-        
-        Words that start with `s` but if you remove `s`, it's still a word.
-        
-        ```python
-        from lexis import Lemmas  # pip install py2store
-        lm = Lemmas()
-        swords = list(filter(lambda x: x.startswith('s') and x[1:] in lm, lm))  # one line!
-        ```
-        
-        
-        ```python
-        print(len(t))
-        print(*t[:40], sep=', ')
-        ```
-        
-            711
-            softener, spock, scent, spark, sbe, stickweed, screaky, salt, salp, sec, strap, sliver, slack, swish, sebs, sarawak, scuttle, stripping, swell, stole, spine, space, scar, sass, sewer, spitting, serving, sew, stalk, smite, sniffy, stripe, slake, stone, slit, sea, shoe, sweeper, swear_off, swan
-        
-        
-        
-        ```python
-        from py2store import filt_iter, wrap_kvs, KvReader
-        from lexis import Lemmas  # pip install py2store
-        lm = Lemmas()
-        
-        @filt_iter(filt=lambda x: x.startswith('s') and x[1:] in lm)
-        class Swords(Lemmas):
-            def __getitem__(self, k):
-                v = super().__getitem__(k)
-                for kk, vv in v.items():
-                    yield f"    {'.'.join(kk.split('.')[1:])}: {vv['definition']}"
-                    
-        s = Swords()
-        len(s)
-        ```
-        
-        
-        
-        
-            711
-        
-        
-        
-        
-        ```python
-        k, v = s.head()
-        list(v)
-        ```
-        
-        
-        
-        
-            ['    n.01: a substance added to another to make it less hard']
-        
-        
-        
-        
-        ```python
-        from itertools import islice
-        for k, v in islice(s.items(), 5):
-            print(f"------------ {k} -------------")
-            print(*v, sep='\n')
-        
-        ```
-        
-            ------------ softener -------------
-                n.01: a substance added to another to make it less hard
-            ------------ spock -------------
-                n.01: United States pediatrician whose many books on child care influenced the upbringing of children around the world (1903-1998)
-            ------------ scent -------------
-                n.02: a distinctive odor that is pleasant
-                n.02: an odor left in passing by which a person or animal can be traced
-                n.01: any property detected by the olfactory system
-                v.01: cause to smell or be smelly
-                v.02: catch the scent of; get wind of
-                v.02: apply perfume to
-            ------------ spark -------------
-                n.01: a momentary flash of light
-                n.01: merriment expressed by a brightness or gleam or animation of countenance
-                n.05: electrical conduction through a gas in an applied electric field
-                n.04: a small but noticeable trace of some quality that might become stronger
-                n.05: Scottish writer of satirical novels (born in 1918)
-                n.06: a small fragment of a burning substance thrown out by burning material or by friction
-                v.04: put in motion or move to act
-                v.02: emit or produce sparks
-            ------------ sbe -------------
-                n.01: the compass point that is one point east of due south
-        
-        
-        
 Keywords: words,definitions,lexicon,wordnet,NLP,Natural Language Processing,text mining
 Platform: any
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+
+# lexis
+Wordnet wrapper - Easy access to words and their relationships
+
+To install:	```pip install lexis```
+
+The key-value (i.e. dict-list) wrapper to nltk.corpus.wordnet.
+
+Your no fuss gateway to (English) words.
+
+The easiest way to get nltk.corpus.wordnet is
+
+The `nltk` dependency is installed for you when installing 
+`lexis`, but the wordnet data is not downloaded automatically.
+To do so (only once), go to a python console and do:
+```
+>>> import nltk; nltk.download('wordnet')  # doctest: +SKIP
+```
+
+If you don't like that way, [see here](https://www.nltk.org/install.html) 
+for other ways to get wordnet.
+
+The central construct of this module is the Synset 
+(a set of synonyms that share a common meaning).
+To see a few things you can do with Synsets, naked, 
+[see here](https://www.nltk.org/howto/wordnet.html).
+
+Here we put a py2store wrapper around this stuff.
+
+What is WordNet? https://wordnet.princeton.edu/
+
+
+# A little peek at Lemmas
+
+
+```python
+from lexis import Lemmas
+
+lm = Lemmas()
+len(lm)
+```
+
+
+
+
+    147306
+
+
+
+`lm` is a `Mapping` (think "acts like a (read-only) dict")
+
+
+```python
+from typing import Mapping
+
+isinstance(lm, Mapping)
+```
+
+
+
+
+    True
+
+
+
+Let's have a look at a few keys
+
+
+```python
+list(lm)[44630:44635]
+```
+
+
+
+
+    ['blond', 'kaunda', 'peacetime', 'intolerantly', "'hood"]
+
+
+
+And the value of a `lm` item?
+
+
+```python
+lm['blond']
+```
+
+
+
+
+    {'blond.n.01': WordnetElement('blond.n.01'),
+     'blond.n.02': WordnetElement('blond.n.02'),
+     'blond.a.01': WordnetElement('blond.a.01')}
+
+
+
+Okay, it looks like it's different meanings of "blond". The middle letter tells us its grammatical role it's a noun (`n`) or an adjective (`a`). More on that later. 
+
+And what's a `WordnetElement`?
+
+Well, it's another Mapping, apparently:
+
+
+```python
+isinstance(lm['blond']['blond.n.01'], Mapping)
+```
+
+
+
+
+    True
+
+
+
+
+```python
+list(lm['blond']['blond.n.01'])
+```
+
+
+
+
+    ['also_sees',
+     'instance_hypernyms',
+     'verb_groups',
+     'entailments',
+     'region_domains',
+     'substance_holonyms',
+     'part_holonyms',
+     'examples',
+     'part_meronyms',
+     'hyponyms',
+     'member_meronyms',
+     'offset',
+     'causes',
+     'definition',
+     'lemma_names',
+     'lexname',
+     'member_holonyms',
+     'in_topic_domains',
+     'lemmas',
+     'topic_domains',
+     'max_depth',
+     'hypernym_distances',
+     'name',
+     'attributes',
+     'hypernyms',
+     'min_depth',
+     'usage_domains',
+     'in_region_domains',
+     'instance_hyponyms',
+     'in_usage_domains',
+     'similar_tos',
+     'root_hypernyms',
+     'pos',
+     'frame_ids',
+     'hypernym_paths',
+     'substance_meronyms']
+
+
+
+Wow! That's a lot of information! 
+
+Let's look at what the definition of `'blond.n.01'` is:
+
+
+```python
+print(lm['blond']['blond.n.01']['definition'])
+```
+
+    a person with fair skin and hair
+
+
+... actually, let's just poke at all of them (at least those that are non-empty)
+
+
+```python
+meaning = 'blond.n.01'
+print(f"Values for meaning: {meaning}")
+for k, v in lm['blond'][meaning].items():
+    if v:
+        print(f"- {k}: {v}")
+```
+
+    Values for meaning: blond.n.01
+    - hyponyms: [WordnetElement('peroxide_blond.n.01'), WordnetElement('platinum_blond.n.01'), WordnetElement('towhead.n.01')]
+    - offset: 9860506
+    - definition: a person with fair skin and hair
+    - lemma_names: ['blond', 'blonde']
+    - lexname: noun.person
+    - lemmas: [KvLemma('blond.n.01.blond'), KvLemma('blond.n.01.blonde')]
+    - max_depth: 7
+    - hypernym_distances: {(WordnetElement('physical_entity.n.01'), 6), (WordnetElement('entity.n.01'), 7), (WordnetElement('physical_entity.n.01'), 3), (WordnetElement('entity.n.01'), 4), (WordnetElement('living_thing.n.01'), 3), (WordnetElement('object.n.01'), 5), (WordnetElement('blond.n.01'), 0), (WordnetElement('organism.n.01'), 2), (WordnetElement('causal_agent.n.01'), 2), (WordnetElement('whole.n.02'), 4), (WordnetElement('person.n.01'), 1)}
+    - name: blond.n.01
+    - hypernyms: [WordnetElement('person.n.01')]
+    - min_depth: 4
+    - root_hypernyms: [Synset('entity.n.01')]
+    - pos: n
+    - hypernym_paths: [[WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('causal_agent.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')], [WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('object.n.01'), WordnetElement('whole.n.02'), WordnetElement('living_thing.n.01'), WordnetElement('organism.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')]]
+
+
+## You can get meaning information directly
+
+What if you made a list of these strings like `'blond.n.01'`, `'blond.a.01'`... and you wanted to access the `WordnetElement` instances with all that cool information about those specifics meanings?
+
+You could do `lm['blond']['blond.n.01']`, `lm['blond']['blond.a.01']`... But then you'd have to remember the full references `('blond', 'blond.n.01')`, `('blond', 'blond.a.01')`... 
+
+You don't need to go through `lm['blond']` to get to the `WordnetElement` instance that gives you access to the meaning information -- you can use the `Synsets` store (i.e. Mapping). 
+
+Note: "synset" is what Wordnet calls this. We'll just call is meaning for simplicity. I hope the purists won't mind.
+
+
+
+```python
+from lexis import Synsets
+```
+
+
+```python
+meanings = Synsets()
+meanings['blond.n.01']
+```
+
+
+
+
+    WordnetElement('blond.n.01')
+
+
+
+We saw earlier that we had `147306` lemmas (i.e. "words" or more precisely "terms"... but really precisely, "lemmas"). 
+
+Well, we have `117659` synsets (i.e. "meanings") in the `Synsets` instance.
+
+
+```python
+len(meanings)
+```
+
+
+
+
+    117659
+
+
+
+## Multiple lemma names
+
+`'lemma_names'` are different ways that the same meaning can be written. 
+
+
+```python
+lm['blond']['blond.n.01']['lemma_names']
+```
+
+
+
+
+    ['blond', 'blonde']
+
+
+
+Indeed, `lm['blond']` and `lm['blonde']` really point to the same thing.
+
+
+```python
+lm['blond']
+```
+
+
+
+
+    {'blond.n.01': WordnetElement('blond.n.01'),
+     'blond.n.02': WordnetElement('blond.n.02'),
+     'blond.a.01': WordnetElement('blond.a.01')}
+
+
+
+
+```python
+lm['blonde']
+```
+
+
+
+
+    {'blond.n.01': WordnetElement('blond.n.01'),
+     'blond.n.02': WordnetElement('blond.n.02'),
+     'blond.a.01': WordnetElement('blond.a.01')}
+
+
+
+## Grammatical roles
+
+What are the different grammatical roles that are used in the meaning identifiers (aka synset keys) of our lemmas?
+
+
+```python
+from collections import Counter
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
+
+def extract_grammatical_role_from_meaning(meaning):
+    m = p_middle_of_dot_path.match(meaning)
+    if m:
+        return m.groupdict().get('middle', None) 
+    else:
+        return None
+    
+
+c = Counter()
+for meanings in lm.values():
+    for meaning in meanings:
+        c.update(extract_grammatical_role_from_meaning(meaning))
+        
+c.most_common()
+```
+
+
+
+
+    [('n', 148478),
+     ('v', 42751),
+     ('s', 20895),
+     ('a', 9846),
+     ('r', 5619),
+     ('_', 29),
+     ('e', 28),
+     ('u', 17),
+     ('g', 17),
+     ('i', 15),
+     ('t', 14),
+     ('p', 8),
+     ('b', 7),
+     ('o', 7),
+     ('l', 6),
+     ('d', 4),
+     ('c', 2),
+     ('m', 1),
+     ('k', 1)]
+
+
+
+
+# Miscellaneous explorations
+
+```python
+from py2store import filt_iter, cached_keys, add_ipython_key_completions
+from py2store import kvhead
+from lexis import Lemmas
+```
+
+
+```python
+lm = Lemmas()
+
+def print_definitions(words):
+    for word in words:
+        print(f"- {word}")
+        for k, v in lm[word].items():
+            print(f"    {'.'.join(k.split('.')[1:])}: {v['definition']}")
+
+```
+
+## Find words containing some substring
+
+
+```python
+from lexis import print_word_definitions
+```
+
+
+```python
+substr = 'iep'
+words = list(filter(lambda w: substr in w, lm))
+len(words)
+```
+
+
+    12
+
+
+```python
+print_definitions(words)
+```
+
+    - hemiepiphyte
+        n.01: a plant that is an epiphyte for part of its life
+    - antiepileptic
+        n.01: a drug used to treat or prevent convulsions (as in epilepsy)
+    - pieplant
+        n.01: long pinkish sour leafstalks usually eaten cooked and sweetened
+    - liepaja
+        n.01: a city of southwestern Latvia on the Baltic Sea
+    - semiepiphyte
+        n.01: a plant that is an epiphyte for part of its life
+    - archiepiscopal
+        a.01: of or associated with an archbishop
+    - tiepin
+        n.01: a pin used to hold the tie in place
+    - giovanni_battista_tiepolo
+        n.01: Italian painter (1696-1770)
+    - tiepolo
+        n.01: Italian painter (1696-1770)
+    - antiepileptic_drug
+        n.01: a drug used to treat or prevent convulsions (as in epilepsy)
+    - dnieper
+        n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
+    - dnieper_river
+        n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
+
+## Find palindrome
+
+```python
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+is_palendrome_with_at_least_3_letters = lambda w: len(w) >= 3 and w == w[::-1]
+print(*filter(is_palendrome_with_at_least_3_letters, lm), sep=', ')
+```
+
+    ono, waw, tot, kkk, ldl, anna, tenet, mom, igigi, sus, hallah, sls, pcp, mam, ofo, ene, alula, oto, civic, cfc, 101, tet, kazak, sss, ctc, aba, tevet, ara, wnw, mum, siris, tebet, tut-tut, ccc, naan, xix, tnt, peep, tut, kook, xanax, ala, eve, level, xxx, dud, aaa, dad, tdt, odo, pip, tibit, iii, sas, wow, radar, madam, yay, dmd, poop, ana, sos, bib, pop, isi, eye, gag, gig, cdc, dod, nun, pep, mym, bob, malayalam, sis, www, utu, non, ewe, aga, akka, noon, ese, rotor, ded, ppp, kayak, pap, wsw, pup, minim, nan, tat, ada, boob, mem, deed, nauruan, ma'am, succus, seles, cbc, tit, dvd, refer, toot
+
+
+Wait a minute... Where's racecar?!? Isn't that a palindrome?
+```python
+# 
+assert 'racecar' not in lm
+assert 'race_car' in lm
+```
+
+### Which of these are (or rather "can be") a verb?
+
+What are the keys of the lemmas? 
+
+Answer: Synset keys -- that is, an id that references a unit of meaning
+
+
+```python
+# what do are the values of the lemmas?
+list(lm['eat'])
+```
+
+
+
+
+    ['eat.v.01',
+     'eat.v.02',
+     'feed.v.06',
+     'eat.v.04',
+     'consume.v.05',
+     'corrode.v.01']
+
+
+
+That little `v` seems to be indicating that the meaning is... verbal?
+
+Let's make a function to grab that middle part of the dot path and use it to make a `is_a_verb` (more like "can be a verb"). 
+
+
+```python
+from collections import Counter
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
+
+def _extract_middle(string):
+    m = p_middle_of_dot_path.match(string)
+    if m:
+        return m.groupdict().get('middle', None) 
+    else:
+        return None
+    
+def grammatical_roles(lemma):
+    return Counter(map(_extract_middle, lm[lemma]))
+    
+
+assert grammatical_roles('go') == Counter({'n': 4, 'v': 30, 'a': 1})  # the lemma "go" can be a verb, noun, or adjective
+
+def is_a_verb(lemma):
+    return 'v' in grammatical_roles(lemma)
+    
+assert is_a_verb('go')
+assert not is_a_verb('chess')  # unlike go, chess cannot be used as a verb, apparently
+```
+
+Palendromes that are verbs
+
+
+```python
+list(filter(lambda x: is_a_verb(x) and is_palendrome_with_at_least_3_letters(x), lm))
+```
+
+
+
+
+    ['tot',
+     'tut-tut',
+     'peep',
+     'tut',
+     'level',
+     'pip',
+     'wow',
+     'bib',
+     'pop',
+     'eye',
+     'gag',
+     'bob',
+     'kayak',
+     'pup',
+     'tat',
+     'boob',
+     'refer',
+     'toot']
+
+
+
+
+## Only p, q, b, d, and vowels
+
+
+```python
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+consonants = 'pqbd'
+vowels = 'aeiou'  # 'aeiouy'
+filt = re.compile(f'[{vowels}{consonants}]+$').match  # the pattern
+
+words = list(filter(lambda w: 2 <= len(w)  <= 7, # number of letters constraing
+                    filter(filt, lm)))  # filter for iep pattern
+len(words)
+```
+
+
+
+
+    249
+
+
+
+
+```python
+print(*words, sep='\t')
+```
+
+    bod	aaa	add	poa	pop	beaded	aqua	pib	edda	doob	boa	doi	padded	iodide	bop	edo	bide	eb	bai	quid	de	ade	daba	pid	baba	paba	bi	abb	bebop	pa	poop	pb	dea	odo	pope	dad	pup	bode	quad	bb	be	ea	epee	bid	pu	pique	iii	pod	bee	pub	ddi	id	baobab	equid	padua	pipidae	opaque	pappa	uppp	uub	qepiq	bibbed	adp	ada	pied	aoudad	qed	pupa	bedaub	bd	dba	bopeep	oboe	ado	eq	bpi	aid	bud	dodo	abo	qaeda	aa	pad	papua	baa	abode	bad	adad	adapid	papaia	db	bede	ai	po	doei	pep	eib	dubai	epi	boob	uuq	io	beep	quip	ad	babu	ded	ia	dud	da	qi	paid	peep	doodad	beda	eddo	boo	padda	ipidae	deep	dope	ied	doped	dopa	ii	iaea	uda	dd	baud	dido	ebb	epa	bodied	pap	ed	peba	bed	audio	deed	idea	apoidea	beau	up	pda	iud	ip	diode	bida	pi	apidae	bead	odd	od	dia	baddie	iaa	ape	ipo	dod	idp	ee	ie	daub	duo	boidae	poe	abed	adobe	pea	dude	do	aided	obi	ido	pipe	pe	doe	aiai	pd	baboo	quipu	pood	papio	equidae	iop	qadi	ab	dado	dub	adobo	bap	pei	baeda	equip	dupe	aqaba	bob	ba	dead	dada	adapa	pee	opepe	pob	iou	duad	doodia	dab	aide	pip	dipped	bubo	pipa	poi	apia	ode	upupa	iq	aba	abbe	edp	edd	pia	due	pud	ob	audad	dp	deb	pie	oed	die	ppp	queue	papa	adieu	biped	babe	ida	dubuque	dip	uup	eu	ipod	bade	au	abide	bib	bedded
+
+
+
+```python
+print_definitions(['adapa'])
+```
+
+    - adapa
+        n.01: a Babylonian demigod or first man (sometimes identified with Adam)
+
+
+### Containing i, e, p in that order, with other letters in between
+
+
+```python
+filt = re.compile('\w{0,2}i\w{0,2}e\w{0,2}p\w{0,2}$').match  # The *i*e*p* pattern
+
+words = list(filter(lambda w: len(w) <= 6, # no more than 6 letters
+                    filter(filt, lm)))  # filter for iep pattern
+print_definitions(words)
+```
+
+
+
+
+    9
+
+
+
+
+```python
+print(*words, sep=', ')
+```
+
+    tie_up, ginep, lineup, inept, pileup, tiepin, biceps, icecap, ice_up
+
+
+
+```python
+print_definitions(words)
+```
+
+    - tie_up
+        v.01: secure with or as if with ropes
+        v.02: invest so as to make unavailable for other purposes
+        v.03: restrain from moving or operating normally
+        v.01: secure in or as if in a berth or dock
+        v.05: finish the last row
+    - ginep
+        n.01: tropical American tree bearing a small edible fruit with green leathery skin and sweet juicy translucent pulp
+    - lineup
+        n.01: (baseball) a list of batters in the order in which they will bat
+        n.02: a line of persons arranged by police for inspection or identification
+    - inept
+        s.04: not elegant or graceful in expression
+        s.02: generally incompetent and ineffectual
+        s.03: revealing lack of perceptiveness or judgment or finesse
+    - pileup
+        n.01: multiple collisions of vehicles
+    - tiepin
+        n.01: a pin used to hold the tie in place
+    - biceps
+        n.01: any skeletal muscle having two origins (but especially the muscle that flexes the forearm)
+    - icecap
+        n.01: a mass of ice and snow that permanently covers a large area of land (e.g., the polar regions or a mountain peak)
+    - ice_up
+        v.01: become covered with a layer of ice; of a surface such as a window
+
+
+
+## S-words
+
+
+Words that start with `s` but if you remove `s`, it's still a word.
+
+```python
+from lexis import Lemmas  # pip install py2store
+lm = Lemmas()
+swords = list(filter(lambda x: x.startswith('s') and x[1:] in lm, lm))  # one line!
+```
+
+
+```python
+print(len(t))
+print(*t[:40], sep=', ')
+```
+
+    711
+    softener, spock, scent, spark, sbe, stickweed, screaky, salt, salp, sec, strap, sliver, slack, swish, sebs, sarawak, scuttle, stripping, swell, stole, spine, space, scar, sass, sewer, spitting, serving, sew, stalk, smite, sniffy, stripe, slake, stone, slit, sea, shoe, sweeper, swear_off, swan
+
+
+
+```python
+from py2store import filt_iter, wrap_kvs, KvReader
+from lexis import Lemmas  # pip install py2store
+lm = Lemmas()
+
+@filt_iter(filt=lambda x: x.startswith('s') and x[1:] in lm)
+class Swords(Lemmas):
+    def __getitem__(self, k):
+        v = super().__getitem__(k)
+        for kk, vv in v.items():
+            yield f"    {'.'.join(kk.split('.')[1:])}: {vv['definition']}"
+            
+s = Swords()
+len(s)
+```
+
+
+
+
+    711
+
+
+
+
+```python
+k, v = s.head()
+list(v)
+```
+
+
+
+
+    ['    n.01: a substance added to another to make it less hard']
+
+
+
+
+```python
+from itertools import islice
+for k, v in islice(s.items(), 5):
+    print(f"------------ {k} -------------")
+    print(*v, sep='\n')
+
+```
+
+    ------------ softener -------------
+        n.01: a substance added to another to make it less hard
+    ------------ spock -------------
+        n.01: United States pediatrician whose many books on child care influenced the upbringing of children around the world (1903-1998)
+    ------------ scent -------------
+        n.02: a distinctive odor that is pleasant
+        n.02: an odor left in passing by which a person or animal can be traced
+        n.01: any property detected by the olfactory system
+        v.01: cause to smell or be smelly
+        v.02: catch the scent of; get wind of
+        v.02: apply perfume to
+    ------------ spark -------------
+        n.01: a momentary flash of light
+        n.01: merriment expressed by a brightness or gleam or animation of countenance
+        n.05: electrical conduction through a gas in an applied electric field
+        n.04: a small but noticeable trace of some quality that might become stronger
+        n.05: Scottish writer of satirical novels (born in 1918)
+        n.06: a small fragment of a burning substance thrown out by burning material or by friction
+        v.04: put in motion or move to act
+        v.02: emit or produce sparks
+    ------------ sbe -------------
+        n.01: the compass point that is one point east of due south
+
+
```

### Comparing `lexis-0.1.1/README.md` & `lexis-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `lexis-0.1.1/lexis/__init__.py` & `lexis-0.1.2/lexis/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -42,14 +42,15 @@
 
 with ModuleNotFoundErrorNiceMessage(
     '''You don't seem to have nltk.corpus.wordnet. 
 If you don't have nltk already, do ``pip install nltk``, and if it's that 
 you don't have wordnet downloaded, do ``import nltk; nltk.download('wordnet');``
 '''
 ):
+    import nltk
     from nltk.corpus import wordnet as wn
     from nltk.corpus.reader.wordnet import Synset, Lemma
 
 
 def callable_attr_names(obj):
     """Set of attributes that are not callable"""
     return {name for name, a in Attrs(obj).items() if not callable(a.src)}
@@ -515,7 +516,90 @@
     ):
         d = pd.DataFrame()
         for dd in self.tree_list:
             d = pd.concat(
                 [d, dd._df_for_excel_export(method=method, method_args=method_args),]
             )
         d.to_excel(filepath, sheet_name=sheet_name, header=False, index=False)
+
+
+def is_noun(word):
+    """Returns True iff word is a noun.
+
+    Warning
+
+    >>> is_noun('dog')
+    True
+    >>> is_noun('run')
+    False
+    >>> is_noun('dogs')
+    True
+    >>> is_noun('doggy')
+    True
+    >>> is_noun('doggies')
+    True
+
+    But:
+
+    >>> is_noun('eat')  # should be False
+    True
+
+    """
+
+    tagged_word = nltk.pos_tag([word])
+    pos = tagged_word[0][1]
+    return pos == 'NN' or pos == 'NNS'
+
+
+def is_drawable(word):
+    """Returns True if the word is a physical entity that can be drawn.
+
+    >>> is_drawable('dog')
+    True
+    >>> is_drawable('doggies')
+    True
+    >>> is_drawable('happy')
+    False
+    >>> is_drawable('eat')
+    False
+
+    """
+    # Define a set of part-of-speech tags that correspond to physical objects
+    physical_tags = {'NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VBG'}
+
+    # Get the part of speech tag for the word
+    tagged_word = nltk.pos_tag([word])
+    pos_tag = tagged_word[0][1]
+
+    # Check if the tag is in the set of physical tags
+    if pos_tag in physical_tags:
+        # Check if the word is a real-world object or concept
+        synsets = nltk.corpus.wordnet.synsets(word)
+        for synset in synsets:
+            if synset.pos() == 'n' and not synset.lexname().startswith('verb'):
+                return True
+
+    # Return False if the word is not a physical entity that can be drawn
+    return False
+
+
+def get_singular(word: str) -> str:
+    """Get the singular form of a word using nltk's wordnet
+
+    See Also
+    --------
+
+    :func:`get_singular_w_inflect`, in the `idiom` package, which creates plurals
+    through a different method, (a rule-based approach).
+    Once the data is loaded, the present ``nltk`` is faster than the one made
+    with ``inflect``, but gives less accurate results, since it's idea of singular is
+    "the base concept".
+
+    """
+    from nltk.corpus import wordnet
+
+    singular = word
+    synsets = wordnet.synsets(word, pos='n')
+    if synsets:
+        lemma = synsets[0].lemmas()[0]
+        singular = lemma.name()
+    return singular
```

### Comparing `lexis-0.1.1/lexis.egg-info/PKG-INFO` & `lexis-0.1.2/lexis.egg-info/PKG-INFO`

 * *Files 22% similar despite different names*

```diff
@@ -1,729 +1,730 @@
 Metadata-Version: 2.1
 Name: lexis
-Version: 0.1.1
+Version: 0.1.2
 Summary: Wordnet wrapper - Easy access to words and their relationships
 Home-page: https://github.com/thorwhalen/lexis
 Author: Thor Whalen
 License: apache-2.0
-Description: 
-        # lexis
-        Wordnet wrapper - Easy access to words and their relationships
-        
-        To install:	```pip install lexis```
-        
-        The key-value (i.e. dict-list) wrapper to nltk.corpus.wordnet.
-        
-        Your no fuss gateway to (English) words.
-        
-        The easiest way to get nltk.corpus.wordnet is
-        
-        The `nltk` dependency is installed for you when installing 
-        `lexis`, but the wordnet data is not downloaded automatically.
-        To do so (only once), go to a python console and do:
-        ```
-        >>> import nltk; nltk.download('wordnet')  # doctest: +SKIP
-        ```
-        
-        If you don't like that way, [see here](https://www.nltk.org/install.html) 
-        for other ways to get wordnet.
-        
-        The central construct of this module is the Synset 
-        (a set of synonyms that share a common meaning).
-        To see a few things you can do with Synsets, naked, 
-        [see here](https://www.nltk.org/howto/wordnet.html).
-        
-        Here we put a py2store wrapper around this stuff.
-        
-        What is WordNet? https://wordnet.princeton.edu/
-        
-        
-        # A little peek at Lemmas
-        
-        
-        ```python
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        len(lm)
-        ```
-        
-        
-        
-        
-            147306
-        
-        
-        
-        `lm` is a `Mapping` (think "acts like a (read-only) dict")
-        
-        
-        ```python
-        from typing import Mapping
-        
-        isinstance(lm, Mapping)
-        ```
-        
-        
-        
-        
-            True
-        
-        
-        
-        Let's have a look at a few keys
-        
-        
-        ```python
-        list(lm)[44630:44635]
-        ```
-        
-        
-        
-        
-            ['blond', 'kaunda', 'peacetime', 'intolerantly', "'hood"]
-        
-        
-        
-        And the value of a `lm` item?
-        
-        
-        ```python
-        lm['blond']
-        ```
-        
-        
-        
-        
-            {'blond.n.01': WordnetElement('blond.n.01'),
-             'blond.n.02': WordnetElement('blond.n.02'),
-             'blond.a.01': WordnetElement('blond.a.01')}
-        
-        
-        
-        Okay, it looks like it's different meanings of "blond". The middle letter tells us its grammatical role it's a noun (`n`) or an adjective (`a`). More on that later. 
-        
-        And what's a `WordnetElement`?
-        
-        Well, it's another Mapping, apparently:
-        
-        
-        ```python
-        isinstance(lm['blond']['blond.n.01'], Mapping)
-        ```
-        
-        
-        
-        
-            True
-        
-        
-        
-        
-        ```python
-        list(lm['blond']['blond.n.01'])
-        ```
-        
-        
-        
-        
-            ['also_sees',
-             'instance_hypernyms',
-             'verb_groups',
-             'entailments',
-             'region_domains',
-             'substance_holonyms',
-             'part_holonyms',
-             'examples',
-             'part_meronyms',
-             'hyponyms',
-             'member_meronyms',
-             'offset',
-             'causes',
-             'definition',
-             'lemma_names',
-             'lexname',
-             'member_holonyms',
-             'in_topic_domains',
-             'lemmas',
-             'topic_domains',
-             'max_depth',
-             'hypernym_distances',
-             'name',
-             'attributes',
-             'hypernyms',
-             'min_depth',
-             'usage_domains',
-             'in_region_domains',
-             'instance_hyponyms',
-             'in_usage_domains',
-             'similar_tos',
-             'root_hypernyms',
-             'pos',
-             'frame_ids',
-             'hypernym_paths',
-             'substance_meronyms']
-        
-        
-        
-        Wow! That's a lot of information! 
-        
-        Let's look at what the definition of `'blond.n.01'` is:
-        
-        
-        ```python
-        print(lm['blond']['blond.n.01']['definition'])
-        ```
-        
-            a person with fair skin and hair
-        
-        
-        ... actually, let's just poke at all of them (at least those that are non-empty)
-        
-        
-        ```python
-        meaning = 'blond.n.01'
-        print(f"Values for meaning: {meaning}")
-        for k, v in lm['blond'][meaning].items():
-            if v:
-                print(f"- {k}: {v}")
-        ```
-        
-            Values for meaning: blond.n.01
-            - hyponyms: [WordnetElement('peroxide_blond.n.01'), WordnetElement('platinum_blond.n.01'), WordnetElement('towhead.n.01')]
-            - offset: 9860506
-            - definition: a person with fair skin and hair
-            - lemma_names: ['blond', 'blonde']
-            - lexname: noun.person
-            - lemmas: [KvLemma('blond.n.01.blond'), KvLemma('blond.n.01.blonde')]
-            - max_depth: 7
-            - hypernym_distances: {(WordnetElement('physical_entity.n.01'), 6), (WordnetElement('entity.n.01'), 7), (WordnetElement('physical_entity.n.01'), 3), (WordnetElement('entity.n.01'), 4), (WordnetElement('living_thing.n.01'), 3), (WordnetElement('object.n.01'), 5), (WordnetElement('blond.n.01'), 0), (WordnetElement('organism.n.01'), 2), (WordnetElement('causal_agent.n.01'), 2), (WordnetElement('whole.n.02'), 4), (WordnetElement('person.n.01'), 1)}
-            - name: blond.n.01
-            - hypernyms: [WordnetElement('person.n.01')]
-            - min_depth: 4
-            - root_hypernyms: [Synset('entity.n.01')]
-            - pos: n
-            - hypernym_paths: [[WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('causal_agent.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')], [WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('object.n.01'), WordnetElement('whole.n.02'), WordnetElement('living_thing.n.01'), WordnetElement('organism.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')]]
-        
-        
-        ## You can get meaning information directly
-        
-        What if you made a list of these strings like `'blond.n.01'`, `'blond.a.01'`... and you wanted to access the `WordnetElement` instances with all that cool information about those specifics meanings?
-        
-        You could do `lm['blond']['blond.n.01']`, `lm['blond']['blond.a.01']`... But then you'd have to remember the full references `('blond', 'blond.n.01')`, `('blond', 'blond.a.01')`... 
-        
-        You don't need to go through `lm['blond']` to get to the `WordnetElement` instance that gives you access to the meaning information -- you can use the `Synsets` store (i.e. Mapping). 
-        
-        Note: "synset" is what Wordnet calls this. We'll just call is meaning for simplicity. I hope the purists won't mind.
-        
-        
-        
-        ```python
-        from lexis import Synsets
-        ```
-        
-        
-        ```python
-        meanings = Synsets()
-        meanings['blond.n.01']
-        ```
-        
-        
-        
-        
-            WordnetElement('blond.n.01')
-        
-        
-        
-        We saw earlier that we had `147306` lemmas (i.e. "words" or more precisely "terms"... but really precisely, "lemmas"). 
-        
-        Well, we have `117659` synsets (i.e. "meanings") in the `Synsets` instance.
-        
-        
-        ```python
-        len(meanings)
-        ```
-        
-        
-        
-        
-            117659
-        
-        
-        
-        ## Multiple lemma names
-        
-        `'lemma_names'` are different ways that the same meaning can be written. 
-        
-        
-        ```python
-        lm['blond']['blond.n.01']['lemma_names']
-        ```
-        
-        
-        
-        
-            ['blond', 'blonde']
-        
-        
-        
-        Indeed, `lm['blond']` and `lm['blonde']` really point to the same thing.
-        
-        
-        ```python
-        lm['blond']
-        ```
-        
-        
-        
-        
-            {'blond.n.01': WordnetElement('blond.n.01'),
-             'blond.n.02': WordnetElement('blond.n.02'),
-             'blond.a.01': WordnetElement('blond.a.01')}
-        
-        
-        
-        
-        ```python
-        lm['blonde']
-        ```
-        
-        
-        
-        
-            {'blond.n.01': WordnetElement('blond.n.01'),
-             'blond.n.02': WordnetElement('blond.n.02'),
-             'blond.a.01': WordnetElement('blond.a.01')}
-        
-        
-        
-        ## Grammatical roles
-        
-        What are the different grammatical roles that are used in the meaning identifiers (aka synset keys) of our lemmas?
-        
-        
-        ```python
-        from collections import Counter
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
-        
-        def extract_grammatical_role_from_meaning(meaning):
-            m = p_middle_of_dot_path.match(meaning)
-            if m:
-                return m.groupdict().get('middle', None) 
-            else:
-                return None
-            
-        
-        c = Counter()
-        for meanings in lm.values():
-            for meaning in meanings:
-                c.update(extract_grammatical_role_from_meaning(meaning))
-                
-        c.most_common()
-        ```
-        
-        
-        
-        
-            [('n', 148478),
-             ('v', 42751),
-             ('s', 20895),
-             ('a', 9846),
-             ('r', 5619),
-             ('_', 29),
-             ('e', 28),
-             ('u', 17),
-             ('g', 17),
-             ('i', 15),
-             ('t', 14),
-             ('p', 8),
-             ('b', 7),
-             ('o', 7),
-             ('l', 6),
-             ('d', 4),
-             ('c', 2),
-             ('m', 1),
-             ('k', 1)]
-        
-        
-        
-        
-        # Miscellaneous explorations
-        
-        ```python
-        from py2store import filt_iter, cached_keys, add_ipython_key_completions
-        from py2store import kvhead
-        from lexis import Lemmas
-        ```
-        
-        
-        ```python
-        lm = Lemmas()
-        
-        def print_definitions(words):
-            for word in words:
-                print(f"- {word}")
-                for k, v in lm[word].items():
-                    print(f"    {'.'.join(k.split('.')[1:])}: {v['definition']}")
-        
-        ```
-        
-        ## Find words containing some substring
-        
-        
-        ```python
-        from lexis import print_word_definitions
-        ```
-        
-        
-        ```python
-        substr = 'iep'
-        words = list(filter(lambda w: substr in w, lm))
-        len(words)
-        ```
-        
-        
-            12
-        
-        
-        ```python
-        print_definitions(words)
-        ```
-        
-            - hemiepiphyte
-                n.01: a plant that is an epiphyte for part of its life
-            - antiepileptic
-                n.01: a drug used to treat or prevent convulsions (as in epilepsy)
-            - pieplant
-                n.01: long pinkish sour leafstalks usually eaten cooked and sweetened
-            - liepaja
-                n.01: a city of southwestern Latvia on the Baltic Sea
-            - semiepiphyte
-                n.01: a plant that is an epiphyte for part of its life
-            - archiepiscopal
-                a.01: of or associated with an archbishop
-            - tiepin
-                n.01: a pin used to hold the tie in place
-            - giovanni_battista_tiepolo
-                n.01: Italian painter (1696-1770)
-            - tiepolo
-                n.01: Italian painter (1696-1770)
-            - antiepileptic_drug
-                n.01: a drug used to treat or prevent convulsions (as in epilepsy)
-            - dnieper
-                n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
-            - dnieper_river
-                n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
-        
-        ## Find palindrome
-        
-        ```python
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        is_palendrome_with_at_least_3_letters = lambda w: len(w) >= 3 and w == w[::-1]
-        print(*filter(is_palendrome_with_at_least_3_letters, lm), sep=', ')
-        ```
-        
-            ono, waw, tot, kkk, ldl, anna, tenet, mom, igigi, sus, hallah, sls, pcp, mam, ofo, ene, alula, oto, civic, cfc, 101, tet, kazak, sss, ctc, aba, tevet, ara, wnw, mum, siris, tebet, tut-tut, ccc, naan, xix, tnt, peep, tut, kook, xanax, ala, eve, level, xxx, dud, aaa, dad, tdt, odo, pip, tibit, iii, sas, wow, radar, madam, yay, dmd, poop, ana, sos, bib, pop, isi, eye, gag, gig, cdc, dod, nun, pep, mym, bob, malayalam, sis, www, utu, non, ewe, aga, akka, noon, ese, rotor, ded, ppp, kayak, pap, wsw, pup, minim, nan, tat, ada, boob, mem, deed, nauruan, ma'am, succus, seles, cbc, tit, dvd, refer, toot
-        
-        
-        Wait a minute... Where's racecar?!? Isn't that a palindrome?
-        ```python
-        # 
-        assert 'racecar' not in lm
-        assert 'race_car' in lm
-        ```
-        
-        ### Which of these are (or rather "can be") a verb?
-        
-        What are the keys of the lemmas? 
-        
-        Answer: Synset keys -- that is, an id that references a unit of meaning
-        
-        
-        ```python
-        # what do are the values of the lemmas?
-        list(lm['eat'])
-        ```
-        
-        
-        
-        
-            ['eat.v.01',
-             'eat.v.02',
-             'feed.v.06',
-             'eat.v.04',
-             'consume.v.05',
-             'corrode.v.01']
-        
-        
-        
-        That little `v` seems to be indicating that the meaning is... verbal?
-        
-        Let's make a function to grab that middle part of the dot path and use it to make a `is_a_verb` (more like "can be a verb"). 
-        
-        
-        ```python
-        from collections import Counter
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
-        
-        def _extract_middle(string):
-            m = p_middle_of_dot_path.match(string)
-            if m:
-                return m.groupdict().get('middle', None) 
-            else:
-                return None
-            
-        def grammatical_roles(lemma):
-            return Counter(map(_extract_middle, lm[lemma]))
-            
-        
-        assert grammatical_roles('go') == Counter({'n': 4, 'v': 30, 'a': 1})  # the lemma "go" can be a verb, noun, or adjective
-        
-        def is_a_verb(lemma):
-            return 'v' in grammatical_roles(lemma)
-            
-        assert is_a_verb('go')
-        assert not is_a_verb('chess')  # unlike go, chess cannot be used as a verb, apparently
-        ```
-        
-        Palendromes that are verbs
-        
-        
-        ```python
-        list(filter(lambda x: is_a_verb(x) and is_palendrome_with_at_least_3_letters(x), lm))
-        ```
-        
-        
-        
-        
-            ['tot',
-             'tut-tut',
-             'peep',
-             'tut',
-             'level',
-             'pip',
-             'wow',
-             'bib',
-             'pop',
-             'eye',
-             'gag',
-             'bob',
-             'kayak',
-             'pup',
-             'tat',
-             'boob',
-             'refer',
-             'toot']
-        
-        
-        
-        
-        ## Only p, q, b, d, and vowels
-        
-        
-        ```python
-        import re
-        from lexis import Lemmas
-        
-        lm = Lemmas()
-        
-        consonants = 'pqbd'
-        vowels = 'aeiou'  # 'aeiouy'
-        filt = re.compile(f'[{vowels}{consonants}]+$').match  # the pattern
-        
-        words = list(filter(lambda w: 2 <= len(w)  <= 7, # number of letters constraing
-                            filter(filt, lm)))  # filter for iep pattern
-        len(words)
-        ```
-        
-        
-        
-        
-            249
-        
-        
-        
-        
-        ```python
-        print(*words, sep='\t')
-        ```
-        
-            bod	aaa	add	poa	pop	beaded	aqua	pib	edda	doob	boa	doi	padded	iodide	bop	edo	bide	eb	bai	quid	de	ade	daba	pid	baba	paba	bi	abb	bebop	pa	poop	pb	dea	odo	pope	dad	pup	bode	quad	bb	be	ea	epee	bid	pu	pique	iii	pod	bee	pub	ddi	id	baobab	equid	padua	pipidae	opaque	pappa	uppp	uub	qepiq	bibbed	adp	ada	pied	aoudad	qed	pupa	bedaub	bd	dba	bopeep	oboe	ado	eq	bpi	aid	bud	dodo	abo	qaeda	aa	pad	papua	baa	abode	bad	adad	adapid	papaia	db	bede	ai	po	doei	pep	eib	dubai	epi	boob	uuq	io	beep	quip	ad	babu	ded	ia	dud	da	qi	paid	peep	doodad	beda	eddo	boo	padda	ipidae	deep	dope	ied	doped	dopa	ii	iaea	uda	dd	baud	dido	ebb	epa	bodied	pap	ed	peba	bed	audio	deed	idea	apoidea	beau	up	pda	iud	ip	diode	bida	pi	apidae	bead	odd	od	dia	baddie	iaa	ape	ipo	dod	idp	ee	ie	daub	duo	boidae	poe	abed	adobe	pea	dude	do	aided	obi	ido	pipe	pe	doe	aiai	pd	baboo	quipu	pood	papio	equidae	iop	qadi	ab	dado	dub	adobo	bap	pei	baeda	equip	dupe	aqaba	bob	ba	dead	dada	adapa	pee	opepe	pob	iou	duad	doodia	dab	aide	pip	dipped	bubo	pipa	poi	apia	ode	upupa	iq	aba	abbe	edp	edd	pia	due	pud	ob	audad	dp	deb	pie	oed	die	ppp	queue	papa	adieu	biped	babe	ida	dubuque	dip	uup	eu	ipod	bade	au	abide	bib	bedded
-        
-        
-        
-        ```python
-        print_definitions(['adapa'])
-        ```
-        
-            - adapa
-                n.01: a Babylonian demigod or first man (sometimes identified with Adam)
-        
-        
-        ### Containing i, e, p in that order, with other letters in between
-        
-        
-        ```python
-        filt = re.compile('\w{0,2}i\w{0,2}e\w{0,2}p\w{0,2}$').match  # The *i*e*p* pattern
-        
-        words = list(filter(lambda w: len(w) <= 6, # no more than 6 letters
-                            filter(filt, lm)))  # filter for iep pattern
-        print_definitions(words)
-        ```
-        
-        
-        
-        
-            9
-        
-        
-        
-        
-        ```python
-        print(*words, sep=', ')
-        ```
-        
-            tie_up, ginep, lineup, inept, pileup, tiepin, biceps, icecap, ice_up
-        
-        
-        
-        ```python
-        print_definitions(words)
-        ```
-        
-            - tie_up
-                v.01: secure with or as if with ropes
-                v.02: invest so as to make unavailable for other purposes
-                v.03: restrain from moving or operating normally
-                v.01: secure in or as if in a berth or dock
-                v.05: finish the last row
-            - ginep
-                n.01: tropical American tree bearing a small edible fruit with green leathery skin and sweet juicy translucent pulp
-            - lineup
-                n.01: (baseball) a list of batters in the order in which they will bat
-                n.02: a line of persons arranged by police for inspection or identification
-            - inept
-                s.04: not elegant or graceful in expression
-                s.02: generally incompetent and ineffectual
-                s.03: revealing lack of perceptiveness or judgment or finesse
-            - pileup
-                n.01: multiple collisions of vehicles
-            - tiepin
-                n.01: a pin used to hold the tie in place
-            - biceps
-                n.01: any skeletal muscle having two origins (but especially the muscle that flexes the forearm)
-            - icecap
-                n.01: a mass of ice and snow that permanently covers a large area of land (e.g., the polar regions or a mountain peak)
-            - ice_up
-                v.01: become covered with a layer of ice; of a surface such as a window
-        
-        
-        
-        ## S-words
-        
-        
-        Words that start with `s` but if you remove `s`, it's still a word.
-        
-        ```python
-        from lexis import Lemmas  # pip install py2store
-        lm = Lemmas()
-        swords = list(filter(lambda x: x.startswith('s') and x[1:] in lm, lm))  # one line!
-        ```
-        
-        
-        ```python
-        print(len(t))
-        print(*t[:40], sep=', ')
-        ```
-        
-            711
-            softener, spock, scent, spark, sbe, stickweed, screaky, salt, salp, sec, strap, sliver, slack, swish, sebs, sarawak, scuttle, stripping, swell, stole, spine, space, scar, sass, sewer, spitting, serving, sew, stalk, smite, sniffy, stripe, slake, stone, slit, sea, shoe, sweeper, swear_off, swan
-        
-        
-        
-        ```python
-        from py2store import filt_iter, wrap_kvs, KvReader
-        from lexis import Lemmas  # pip install py2store
-        lm = Lemmas()
-        
-        @filt_iter(filt=lambda x: x.startswith('s') and x[1:] in lm)
-        class Swords(Lemmas):
-            def __getitem__(self, k):
-                v = super().__getitem__(k)
-                for kk, vv in v.items():
-                    yield f"    {'.'.join(kk.split('.')[1:])}: {vv['definition']}"
-                    
-        s = Swords()
-        len(s)
-        ```
-        
-        
-        
-        
-            711
-        
-        
-        
-        
-        ```python
-        k, v = s.head()
-        list(v)
-        ```
-        
-        
-        
-        
-            ['    n.01: a substance added to another to make it less hard']
-        
-        
-        
-        
-        ```python
-        from itertools import islice
-        for k, v in islice(s.items(), 5):
-            print(f"------------ {k} -------------")
-            print(*v, sep='\n')
-        
-        ```
-        
-            ------------ softener -------------
-                n.01: a substance added to another to make it less hard
-            ------------ spock -------------
-                n.01: United States pediatrician whose many books on child care influenced the upbringing of children around the world (1903-1998)
-            ------------ scent -------------
-                n.02: a distinctive odor that is pleasant
-                n.02: an odor left in passing by which a person or animal can be traced
-                n.01: any property detected by the olfactory system
-                v.01: cause to smell or be smelly
-                v.02: catch the scent of; get wind of
-                v.02: apply perfume to
-            ------------ spark -------------
-                n.01: a momentary flash of light
-                n.01: merriment expressed by a brightness or gleam or animation of countenance
-                n.05: electrical conduction through a gas in an applied electric field
-                n.04: a small but noticeable trace of some quality that might become stronger
-                n.05: Scottish writer of satirical novels (born in 1918)
-                n.06: a small fragment of a burning substance thrown out by burning material or by friction
-                v.04: put in motion or move to act
-                v.02: emit or produce sparks
-            ------------ sbe -------------
-                n.01: the compass point that is one point east of due south
-        
-        
-        
 Keywords: words,definitions,lexicon,wordnet,NLP,Natural Language Processing,text mining
 Platform: any
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+
+# lexis
+Wordnet wrapper - Easy access to words and their relationships
+
+To install:	```pip install lexis```
+
+The key-value (i.e. dict-list) wrapper to nltk.corpus.wordnet.
+
+Your no fuss gateway to (English) words.
+
+The easiest way to get nltk.corpus.wordnet is
+
+The `nltk` dependency is installed for you when installing 
+`lexis`, but the wordnet data is not downloaded automatically.
+To do so (only once), go to a python console and do:
+```
+>>> import nltk; nltk.download('wordnet')  # doctest: +SKIP
+```
+
+If you don't like that way, [see here](https://www.nltk.org/install.html) 
+for other ways to get wordnet.
+
+The central construct of this module is the Synset 
+(a set of synonyms that share a common meaning).
+To see a few things you can do with Synsets, naked, 
+[see here](https://www.nltk.org/howto/wordnet.html).
+
+Here we put a py2store wrapper around this stuff.
+
+What is WordNet? https://wordnet.princeton.edu/
+
+
+# A little peek at Lemmas
+
+
+```python
+from lexis import Lemmas
+
+lm = Lemmas()
+len(lm)
+```
+
+
+
+
+    147306
+
+
+
+`lm` is a `Mapping` (think "acts like a (read-only) dict")
+
+
+```python
+from typing import Mapping
+
+isinstance(lm, Mapping)
+```
+
+
+
+
+    True
+
+
+
+Let's have a look at a few keys
+
+
+```python
+list(lm)[44630:44635]
+```
+
+
+
+
+    ['blond', 'kaunda', 'peacetime', 'intolerantly', "'hood"]
+
+
+
+And the value of a `lm` item?
+
+
+```python
+lm['blond']
+```
+
+
+
+
+    {'blond.n.01': WordnetElement('blond.n.01'),
+     'blond.n.02': WordnetElement('blond.n.02'),
+     'blond.a.01': WordnetElement('blond.a.01')}
+
+
+
+Okay, it looks like it's different meanings of "blond". The middle letter tells us its grammatical role it's a noun (`n`) or an adjective (`a`). More on that later. 
+
+And what's a `WordnetElement`?
+
+Well, it's another Mapping, apparently:
+
+
+```python
+isinstance(lm['blond']['blond.n.01'], Mapping)
+```
+
+
+
+
+    True
+
+
+
+
+```python
+list(lm['blond']['blond.n.01'])
+```
+
+
+
+
+    ['also_sees',
+     'instance_hypernyms',
+     'verb_groups',
+     'entailments',
+     'region_domains',
+     'substance_holonyms',
+     'part_holonyms',
+     'examples',
+     'part_meronyms',
+     'hyponyms',
+     'member_meronyms',
+     'offset',
+     'causes',
+     'definition',
+     'lemma_names',
+     'lexname',
+     'member_holonyms',
+     'in_topic_domains',
+     'lemmas',
+     'topic_domains',
+     'max_depth',
+     'hypernym_distances',
+     'name',
+     'attributes',
+     'hypernyms',
+     'min_depth',
+     'usage_domains',
+     'in_region_domains',
+     'instance_hyponyms',
+     'in_usage_domains',
+     'similar_tos',
+     'root_hypernyms',
+     'pos',
+     'frame_ids',
+     'hypernym_paths',
+     'substance_meronyms']
+
+
+
+Wow! That's a lot of information! 
+
+Let's look at what the definition of `'blond.n.01'` is:
+
+
+```python
+print(lm['blond']['blond.n.01']['definition'])
+```
+
+    a person with fair skin and hair
+
+
+... actually, let's just poke at all of them (at least those that are non-empty)
+
+
+```python
+meaning = 'blond.n.01'
+print(f"Values for meaning: {meaning}")
+for k, v in lm['blond'][meaning].items():
+    if v:
+        print(f"- {k}: {v}")
+```
+
+    Values for meaning: blond.n.01
+    - hyponyms: [WordnetElement('peroxide_blond.n.01'), WordnetElement('platinum_blond.n.01'), WordnetElement('towhead.n.01')]
+    - offset: 9860506
+    - definition: a person with fair skin and hair
+    - lemma_names: ['blond', 'blonde']
+    - lexname: noun.person
+    - lemmas: [KvLemma('blond.n.01.blond'), KvLemma('blond.n.01.blonde')]
+    - max_depth: 7
+    - hypernym_distances: {(WordnetElement('physical_entity.n.01'), 6), (WordnetElement('entity.n.01'), 7), (WordnetElement('physical_entity.n.01'), 3), (WordnetElement('entity.n.01'), 4), (WordnetElement('living_thing.n.01'), 3), (WordnetElement('object.n.01'), 5), (WordnetElement('blond.n.01'), 0), (WordnetElement('organism.n.01'), 2), (WordnetElement('causal_agent.n.01'), 2), (WordnetElement('whole.n.02'), 4), (WordnetElement('person.n.01'), 1)}
+    - name: blond.n.01
+    - hypernyms: [WordnetElement('person.n.01')]
+    - min_depth: 4
+    - root_hypernyms: [Synset('entity.n.01')]
+    - pos: n
+    - hypernym_paths: [[WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('causal_agent.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')], [WordnetElement('entity.n.01'), WordnetElement('physical_entity.n.01'), WordnetElement('object.n.01'), WordnetElement('whole.n.02'), WordnetElement('living_thing.n.01'), WordnetElement('organism.n.01'), WordnetElement('person.n.01'), WordnetElement('blond.n.01')]]
+
+
+## You can get meaning information directly
+
+What if you made a list of these strings like `'blond.n.01'`, `'blond.a.01'`... and you wanted to access the `WordnetElement` instances with all that cool information about those specifics meanings?
+
+You could do `lm['blond']['blond.n.01']`, `lm['blond']['blond.a.01']`... But then you'd have to remember the full references `('blond', 'blond.n.01')`, `('blond', 'blond.a.01')`... 
+
+You don't need to go through `lm['blond']` to get to the `WordnetElement` instance that gives you access to the meaning information -- you can use the `Synsets` store (i.e. Mapping). 
+
+Note: "synset" is what Wordnet calls this. We'll just call is meaning for simplicity. I hope the purists won't mind.
+
+
+
+```python
+from lexis import Synsets
+```
+
+
+```python
+meanings = Synsets()
+meanings['blond.n.01']
+```
+
+
+
+
+    WordnetElement('blond.n.01')
+
+
+
+We saw earlier that we had `147306` lemmas (i.e. "words" or more precisely "terms"... but really precisely, "lemmas"). 
+
+Well, we have `117659` synsets (i.e. "meanings") in the `Synsets` instance.
+
+
+```python
+len(meanings)
+```
+
+
+
+
+    117659
+
+
+
+## Multiple lemma names
+
+`'lemma_names'` are different ways that the same meaning can be written. 
+
+
+```python
+lm['blond']['blond.n.01']['lemma_names']
+```
+
+
+
+
+    ['blond', 'blonde']
+
+
+
+Indeed, `lm['blond']` and `lm['blonde']` really point to the same thing.
+
+
+```python
+lm['blond']
+```
+
+
+
+
+    {'blond.n.01': WordnetElement('blond.n.01'),
+     'blond.n.02': WordnetElement('blond.n.02'),
+     'blond.a.01': WordnetElement('blond.a.01')}
+
+
+
+
+```python
+lm['blonde']
+```
+
+
+
+
+    {'blond.n.01': WordnetElement('blond.n.01'),
+     'blond.n.02': WordnetElement('blond.n.02'),
+     'blond.a.01': WordnetElement('blond.a.01')}
+
+
+
+## Grammatical roles
+
+What are the different grammatical roles that are used in the meaning identifiers (aka synset keys) of our lemmas?
+
+
+```python
+from collections import Counter
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
+
+def extract_grammatical_role_from_meaning(meaning):
+    m = p_middle_of_dot_path.match(meaning)
+    if m:
+        return m.groupdict().get('middle', None) 
+    else:
+        return None
+    
+
+c = Counter()
+for meanings in lm.values():
+    for meaning in meanings:
+        c.update(extract_grammatical_role_from_meaning(meaning))
+        
+c.most_common()
+```
+
+
+
+
+    [('n', 148478),
+     ('v', 42751),
+     ('s', 20895),
+     ('a', 9846),
+     ('r', 5619),
+     ('_', 29),
+     ('e', 28),
+     ('u', 17),
+     ('g', 17),
+     ('i', 15),
+     ('t', 14),
+     ('p', 8),
+     ('b', 7),
+     ('o', 7),
+     ('l', 6),
+     ('d', 4),
+     ('c', 2),
+     ('m', 1),
+     ('k', 1)]
+
+
+
+
+# Miscellaneous explorations
+
+```python
+from py2store import filt_iter, cached_keys, add_ipython_key_completions
+from py2store import kvhead
+from lexis import Lemmas
+```
+
+
+```python
+lm = Lemmas()
+
+def print_definitions(words):
+    for word in words:
+        print(f"- {word}")
+        for k, v in lm[word].items():
+            print(f"    {'.'.join(k.split('.')[1:])}: {v['definition']}")
+
+```
+
+## Find words containing some substring
+
+
+```python
+from lexis import print_word_definitions
+```
+
+
+```python
+substr = 'iep'
+words = list(filter(lambda w: substr in w, lm))
+len(words)
+```
+
+
+    12
+
+
+```python
+print_definitions(words)
+```
+
+    - hemiepiphyte
+        n.01: a plant that is an epiphyte for part of its life
+    - antiepileptic
+        n.01: a drug used to treat or prevent convulsions (as in epilepsy)
+    - pieplant
+        n.01: long pinkish sour leafstalks usually eaten cooked and sweetened
+    - liepaja
+        n.01: a city of southwestern Latvia on the Baltic Sea
+    - semiepiphyte
+        n.01: a plant that is an epiphyte for part of its life
+    - archiepiscopal
+        a.01: of or associated with an archbishop
+    - tiepin
+        n.01: a pin used to hold the tie in place
+    - giovanni_battista_tiepolo
+        n.01: Italian painter (1696-1770)
+    - tiepolo
+        n.01: Italian painter (1696-1770)
+    - antiepileptic_drug
+        n.01: a drug used to treat or prevent convulsions (as in epilepsy)
+    - dnieper
+        n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
+    - dnieper_river
+        n.01: a river that rises in Russia near Smolensk and flowing south through Belarus and Ukraine to empty into the Black Sea
+
+## Find palindrome
+
+```python
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+is_palendrome_with_at_least_3_letters = lambda w: len(w) >= 3 and w == w[::-1]
+print(*filter(is_palendrome_with_at_least_3_letters, lm), sep=', ')
+```
+
+    ono, waw, tot, kkk, ldl, anna, tenet, mom, igigi, sus, hallah, sls, pcp, mam, ofo, ene, alula, oto, civic, cfc, 101, tet, kazak, sss, ctc, aba, tevet, ara, wnw, mum, siris, tebet, tut-tut, ccc, naan, xix, tnt, peep, tut, kook, xanax, ala, eve, level, xxx, dud, aaa, dad, tdt, odo, pip, tibit, iii, sas, wow, radar, madam, yay, dmd, poop, ana, sos, bib, pop, isi, eye, gag, gig, cdc, dod, nun, pep, mym, bob, malayalam, sis, www, utu, non, ewe, aga, akka, noon, ese, rotor, ded, ppp, kayak, pap, wsw, pup, minim, nan, tat, ada, boob, mem, deed, nauruan, ma'am, succus, seles, cbc, tit, dvd, refer, toot
+
+
+Wait a minute... Where's racecar?!? Isn't that a palindrome?
+```python
+# 
+assert 'racecar' not in lm
+assert 'race_car' in lm
+```
+
+### Which of these are (or rather "can be") a verb?
+
+What are the keys of the lemmas? 
+
+Answer: Synset keys -- that is, an id that references a unit of meaning
+
+
+```python
+# what do are the values of the lemmas?
+list(lm['eat'])
+```
+
+
+
+
+    ['eat.v.01',
+     'eat.v.02',
+     'feed.v.06',
+     'eat.v.04',
+     'consume.v.05',
+     'corrode.v.01']
+
+
+
+That little `v` seems to be indicating that the meaning is... verbal?
+
+Let's make a function to grab that middle part of the dot path and use it to make a `is_a_verb` (more like "can be a verb"). 
+
+
+```python
+from collections import Counter
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+p_middle_of_dot_path = re.compile('(?P<first>[^\.]+)\.(?P<middle>\w+)\.(?P<last>[^\.]+)')
+
+def _extract_middle(string):
+    m = p_middle_of_dot_path.match(string)
+    if m:
+        return m.groupdict().get('middle', None) 
+    else:
+        return None
+    
+def grammatical_roles(lemma):
+    return Counter(map(_extract_middle, lm[lemma]))
+    
+
+assert grammatical_roles('go') == Counter({'n': 4, 'v': 30, 'a': 1})  # the lemma "go" can be a verb, noun, or adjective
+
+def is_a_verb(lemma):
+    return 'v' in grammatical_roles(lemma)
+    
+assert is_a_verb('go')
+assert not is_a_verb('chess')  # unlike go, chess cannot be used as a verb, apparently
+```
+
+Palendromes that are verbs
+
+
+```python
+list(filter(lambda x: is_a_verb(x) and is_palendrome_with_at_least_3_letters(x), lm))
+```
+
+
+
+
+    ['tot',
+     'tut-tut',
+     'peep',
+     'tut',
+     'level',
+     'pip',
+     'wow',
+     'bib',
+     'pop',
+     'eye',
+     'gag',
+     'bob',
+     'kayak',
+     'pup',
+     'tat',
+     'boob',
+     'refer',
+     'toot']
+
+
+
+
+## Only p, q, b, d, and vowels
+
+
+```python
+import re
+from lexis import Lemmas
+
+lm = Lemmas()
+
+consonants = 'pqbd'
+vowels = 'aeiou'  # 'aeiouy'
+filt = re.compile(f'[{vowels}{consonants}]+$').match  # the pattern
+
+words = list(filter(lambda w: 2 <= len(w)  <= 7, # number of letters constraing
+                    filter(filt, lm)))  # filter for iep pattern
+len(words)
+```
+
+
+
+
+    249
+
+
+
+
+```python
+print(*words, sep='\t')
+```
+
+    bod	aaa	add	poa	pop	beaded	aqua	pib	edda	doob	boa	doi	padded	iodide	bop	edo	bide	eb	bai	quid	de	ade	daba	pid	baba	paba	bi	abb	bebop	pa	poop	pb	dea	odo	pope	dad	pup	bode	quad	bb	be	ea	epee	bid	pu	pique	iii	pod	bee	pub	ddi	id	baobab	equid	padua	pipidae	opaque	pappa	uppp	uub	qepiq	bibbed	adp	ada	pied	aoudad	qed	pupa	bedaub	bd	dba	bopeep	oboe	ado	eq	bpi	aid	bud	dodo	abo	qaeda	aa	pad	papua	baa	abode	bad	adad	adapid	papaia	db	bede	ai	po	doei	pep	eib	dubai	epi	boob	uuq	io	beep	quip	ad	babu	ded	ia	dud	da	qi	paid	peep	doodad	beda	eddo	boo	padda	ipidae	deep	dope	ied	doped	dopa	ii	iaea	uda	dd	baud	dido	ebb	epa	bodied	pap	ed	peba	bed	audio	deed	idea	apoidea	beau	up	pda	iud	ip	diode	bida	pi	apidae	bead	odd	od	dia	baddie	iaa	ape	ipo	dod	idp	ee	ie	daub	duo	boidae	poe	abed	adobe	pea	dude	do	aided	obi	ido	pipe	pe	doe	aiai	pd	baboo	quipu	pood	papio	equidae	iop	qadi	ab	dado	dub	adobo	bap	pei	baeda	equip	dupe	aqaba	bob	ba	dead	dada	adapa	pee	opepe	pob	iou	duad	doodia	dab	aide	pip	dipped	bubo	pipa	poi	apia	ode	upupa	iq	aba	abbe	edp	edd	pia	due	pud	ob	audad	dp	deb	pie	oed	die	ppp	queue	papa	adieu	biped	babe	ida	dubuque	dip	uup	eu	ipod	bade	au	abide	bib	bedded
+
+
+
+```python
+print_definitions(['adapa'])
+```
+
+    - adapa
+        n.01: a Babylonian demigod or first man (sometimes identified with Adam)
+
+
+### Containing i, e, p in that order, with other letters in between
+
+
+```python
+filt = re.compile('\w{0,2}i\w{0,2}e\w{0,2}p\w{0,2}$').match  # The *i*e*p* pattern
+
+words = list(filter(lambda w: len(w) <= 6, # no more than 6 letters
+                    filter(filt, lm)))  # filter for iep pattern
+print_definitions(words)
+```
+
+
+
+
+    9
+
+
+
+
+```python
+print(*words, sep=', ')
+```
+
+    tie_up, ginep, lineup, inept, pileup, tiepin, biceps, icecap, ice_up
+
+
+
+```python
+print_definitions(words)
+```
+
+    - tie_up
+        v.01: secure with or as if with ropes
+        v.02: invest so as to make unavailable for other purposes
+        v.03: restrain from moving or operating normally
+        v.01: secure in or as if in a berth or dock
+        v.05: finish the last row
+    - ginep
+        n.01: tropical American tree bearing a small edible fruit with green leathery skin and sweet juicy translucent pulp
+    - lineup
+        n.01: (baseball) a list of batters in the order in which they will bat
+        n.02: a line of persons arranged by police for inspection or identification
+    - inept
+        s.04: not elegant or graceful in expression
+        s.02: generally incompetent and ineffectual
+        s.03: revealing lack of perceptiveness or judgment or finesse
+    - pileup
+        n.01: multiple collisions of vehicles
+    - tiepin
+        n.01: a pin used to hold the tie in place
+    - biceps
+        n.01: any skeletal muscle having two origins (but especially the muscle that flexes the forearm)
+    - icecap
+        n.01: a mass of ice and snow that permanently covers a large area of land (e.g., the polar regions or a mountain peak)
+    - ice_up
+        v.01: become covered with a layer of ice; of a surface such as a window
+
+
+
+## S-words
+
+
+Words that start with `s` but if you remove `s`, it's still a word.
+
+```python
+from lexis import Lemmas  # pip install py2store
+lm = Lemmas()
+swords = list(filter(lambda x: x.startswith('s') and x[1:] in lm, lm))  # one line!
+```
+
+
+```python
+print(len(t))
+print(*t[:40], sep=', ')
+```
+
+    711
+    softener, spock, scent, spark, sbe, stickweed, screaky, salt, salp, sec, strap, sliver, slack, swish, sebs, sarawak, scuttle, stripping, swell, stole, spine, space, scar, sass, sewer, spitting, serving, sew, stalk, smite, sniffy, stripe, slake, stone, slit, sea, shoe, sweeper, swear_off, swan
+
+
+
+```python
+from py2store import filt_iter, wrap_kvs, KvReader
+from lexis import Lemmas  # pip install py2store
+lm = Lemmas()
+
+@filt_iter(filt=lambda x: x.startswith('s') and x[1:] in lm)
+class Swords(Lemmas):
+    def __getitem__(self, k):
+        v = super().__getitem__(k)
+        for kk, vv in v.items():
+            yield f"    {'.'.join(kk.split('.')[1:])}: {vv['definition']}"
+            
+s = Swords()
+len(s)
+```
+
+
+
+
+    711
+
+
+
+
+```python
+k, v = s.head()
+list(v)
+```
+
+
+
+
+    ['    n.01: a substance added to another to make it less hard']
+
+
+
+
+```python
+from itertools import islice
+for k, v in islice(s.items(), 5):
+    print(f"------------ {k} -------------")
+    print(*v, sep='\n')
+
+```
+
+    ------------ softener -------------
+        n.01: a substance added to another to make it less hard
+    ------------ spock -------------
+        n.01: United States pediatrician whose many books on child care influenced the upbringing of children around the world (1903-1998)
+    ------------ scent -------------
+        n.02: a distinctive odor that is pleasant
+        n.02: an odor left in passing by which a person or animal can be traced
+        n.01: any property detected by the olfactory system
+        v.01: cause to smell or be smelly
+        v.02: catch the scent of; get wind of
+        v.02: apply perfume to
+    ------------ spark -------------
+        n.01: a momentary flash of light
+        n.01: merriment expressed by a brightness or gleam or animation of countenance
+        n.05: electrical conduction through a gas in an applied electric field
+        n.04: a small but noticeable trace of some quality that might become stronger
+        n.05: Scottish writer of satirical novels (born in 1918)
+        n.06: a small fragment of a burning substance thrown out by burning material or by friction
+        v.04: put in motion or move to act
+        v.02: emit or produce sparks
+    ------------ sbe -------------
+        n.01: the compass point that is one point east of due south
+
+
```

### Comparing `lexis-0.1.1/setup.cfg` & `lexis-0.1.2/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = lexis
-version = 0.1.1
+version = 0.1.2
 url = https://github.com/thorwhalen/lexis
 platforms = any
 description_file = README.md
 root_url = https://github.com/thorwhalen/
 license = apache-2.0
 author = Thor Whalen
 description = Wordnet wrapper - Easy access to words and their relationships
```

