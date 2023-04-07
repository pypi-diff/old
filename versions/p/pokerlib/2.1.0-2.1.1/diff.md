# Comparing `tmp/pokerlib-2.1.0.tar.gz` & `tmp/pokerlib-2.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pokerlib-2.1.0.tar", max compression
+gzip compressed data, was "pokerlib-2.1.1.tar", max compression
```

## Comparing `pokerlib-2.1.0.tar` & `pokerlib-2.1.1.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0    35147 2022-10-03 17:39:48.345471 pokerlib-2.1.0/LICENSE
--rw-r--r--   0        0        0     6833 2023-04-03 20:53:18.762679 pokerlib-2.1.0/README.md
--rw-r--r--   0        0        0      493 2023-04-03 20:56:33.372677 pokerlib-2.1.0/pokerlib/__init__.py
--rw-r--r--   0        0        0     8934 2023-02-23 20:42:05.954724 pokerlib-2.1.0/pokerlib/_handparser.py
--rw-r--r--   0        0        0     4149 2023-04-03 19:34:35.852712 pokerlib-2.1.0/pokerlib/_player.py
--rw-r--r--   0        0        0    14910 2023-04-04 14:11:02.334039 pokerlib-2.1.0/pokerlib/_round.py
--rw-r--r--   0        0        0     6936 2023-04-04 14:16:50.734040 pokerlib-2.1.0/pokerlib/_table.py
--rw-r--r--   0        0        0     1523 2023-04-04 09:05:46.153989 pokerlib-2.1.0/pokerlib/enums.py
--rw-r--r--   0        0        0      107 2023-04-03 19:58:33.722702 pokerlib-2.1.0/pokerlib/implementations/__init__.py
--rw-r--r--   0        0        0     2408 2023-04-03 19:58:33.722702 pokerlib-2.1.0/pokerlib/implementations/_table_with_choice_to_show_cards.py
--rw-r--r--   0        0        0      663 2023-04-05 10:53:51.367705 pokerlib-2.1.0/pyproject.toml
--rw-r--r--   0        0        0     7602 1970-01-01 00:00:00.000000 pokerlib-2.1.0/setup.py
--rw-r--r--   0        0        0     7558 1970-01-01 00:00:00.000000 pokerlib-2.1.0/PKG-INFO
+-rw-r--r--   0        0        0    35147 2022-10-03 17:39:48.345471 pokerlib-2.1.1/LICENSE
+-rw-r--r--   0        0        0     6833 2023-04-03 20:53:18.762679 pokerlib-2.1.1/README.md
+-rw-r--r--   0        0        0      493 2023-04-07 09:40:14.276227 pokerlib-2.1.1/pokerlib/__init__.py
+-rw-r--r--   0        0        0     8934 2023-02-23 20:42:05.954724 pokerlib-2.1.1/pokerlib/_handparser.py
+-rw-r--r--   0        0        0     4149 2023-04-03 19:34:35.852712 pokerlib-2.1.1/pokerlib/_player.py
+-rw-r--r--   0        0        0    14917 2023-04-07 09:35:55.186229 pokerlib-2.1.1/pokerlib/_round.py
+-rw-r--r--   0        0        0     6936 2023-04-07 09:33:14.596230 pokerlib-2.1.1/pokerlib/_table.py
+-rw-r--r--   0        0        0     1523 2023-04-04 09:05:46.153989 pokerlib-2.1.1/pokerlib/enums.py
+-rw-r--r--   0        0        0      107 2023-04-03 19:58:33.722702 pokerlib-2.1.1/pokerlib/implementations/__init__.py
+-rw-r--r--   0        0        0     2473 2023-04-07 09:34:44.876229 pokerlib-2.1.1/pokerlib/implementations/_table_with_choice_to_show_cards.py
+-rw-r--r--   0        0        0      663 2023-04-07 09:39:18.996227 pokerlib-2.1.1/pyproject.toml
+-rw-r--r--   0        0        0     7602 1970-01-01 00:00:00.000000 pokerlib-2.1.1/setup.py
+-rw-r--r--   0        0        0     7558 1970-01-01 00:00:00.000000 pokerlib-2.1.1/PKG-INFO
```

### Comparing `pokerlib-2.1.0/LICENSE` & `pokerlib-2.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pokerlib-2.1.0/README.md` & `pokerlib-2.1.1/README.md`

 * *Files identical despite different names*

### Comparing `pokerlib-2.1.0/pokerlib/_handparser.py` & `pokerlib-2.1.1/pokerlib/_handparser.py`

 * *Files identical despite different names*

### Comparing `pokerlib-2.1.0/pokerlib/_player.py` & `pokerlib-2.1.1/pokerlib/_player.py`

 * *Files identical despite different names*

### Comparing `pokerlib-2.1.0/pokerlib/_round.py` & `pokerlib-2.1.1/pokerlib/_round.py`

 * *Files 1% similar despite different names*

```diff
@@ -290,15 +290,15 @@
         elif self.players.allPlayedTurn() and pots_balanced:
             if self.turn == Turn.RIVER:
                 self._dealWinnings()
                 return self._close()
             else:
                 next(self._turn_generator)
                 self.current_index = self.button
-                self._moveToNextPlayer()
+                return self._moveToNextPlayer()
 
         # this function can be called after a non-current-player's
         # hand is force-folded, in which case we don't want to move
         # onto the next player
         elif not is_update_after_forcefold:
             self._moveToNextPlayer()
```

### Comparing `pokerlib-2.1.0/pokerlib/_table.py` & `pokerlib-2.1.1/pokerlib/_table.py`

 * *Files identical despite different names*

### Comparing `pokerlib-2.1.0/pokerlib/enums.py` & `pokerlib-2.1.1/pokerlib/enums.py`

 * *Files identical despite different names*

### Comparing `pokerlib-2.1.0/pokerlib/implementations/_table_with_choice_to_show_cards.py` & `pokerlib-2.1.1/pokerlib/implementations/_table_with_choice_to_show_cards.py`

 * *Files 6% similar despite different names*

```diff
@@ -7,22 +7,22 @@
 
 def extendedEnum(original, extended):
     return IntEnum(extended.__name__, [
         (x.name, x.value) for x in chain(original, extended)])
 
 # extending RoundPublicInId enum by
 class RoundWithChoiceToShowCardsPublicInId(IntEnum):
-    SHOWCARDS = 5
+    SHOWCARDS = len(RoundPublicInId) # 5
 RoundWithChoiceToShowCardsPublicInId = extendedEnum(
     RoundPublicInId, RoundWithChoiceToShowCardsPublicInId)
 
 # extending RoundPublicOutId enum by
 class RoundWithChoiceToShowCardsPublicOutId(IntEnum):
-    PLAYERCHOICEREQUIRED = 14
-    PLAYERREVEALCARDS = 15
+    PLAYERCHOICEREQUIRED = len(RoundPublicOutId) # 15
+    PLAYERREVEALCARDS = len(RoundPublicOutId) + 1 # 16
 RoundWithChoiceToShowCardsPublicOutId = extendedEnum(
     RoundPublicOutId, RoundWithChoiceToShowCardsPublicOutId)
 
 class RoundWithChoiceToShowCards(Round):
     PublicInId = RoundWithChoiceToShowCardsPublicInId
     PublicOutId = RoundWithChoiceToShowCardsPublicOutId
 
@@ -51,15 +51,15 @@
             player_id = winner.id,
             cards = winner.cards
         )
 
     def publicIn(self, player_id, action, raise_by=0, show_cards=False):
         # process all the standard inputs
         super().publicIn(player_id, action, raise_by)
-        # add card reveal options (note that caller does not have to be current winner)
+        # add card reveal options (note that caller has to be current winner)
         if (
             action is self.PublicInId.SHOWCARDS and
             self._premature_winner_id is not None and self._premature_winner_id == player_id
         ):
             if show_cards: self._showPrematureWinnerCards()
             self._premature_winner_id = None
             self._close()
```

### Comparing `pokerlib-2.1.0/pyproject.toml` & `pokerlib-2.1.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pokerlib"
-version = "2.1.0"
+version = "2.1.1"
 description = "Python poker library"
 repository = "https://github.com/kuco23/pokerlib/"
 authors = ["kuco23 <nseverkar@gmail.com>"]
 keywords = ['python', 'poker', 'library']
 readme = "README.md"
 classifiers=  [
     'Development Status :: 3 - Alpha',
```

### Comparing `pokerlib-2.1.0/setup.py` & `pokerlib-2.1.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 ['pokerlib', 'pokerlib.implementations']
 
 package_data = \
 {'': ['*']}
 
 setup_kwargs = {
     'name': 'pokerlib',
-    'version': '2.1.0',
+    'version': '2.1.1',
     'description': 'Python poker library',
     'long_description': '# pokerlib\n[![PyPI version](https://badge.fury.io/py/pokerlib.svg)](https://pypi.org/project/pokerlib)\n\nA lightweight Python poker library, focusing on simplifying a Texas hold\'em poker game implementation, when its io is supplied. It includes modules that help with hand parsing and poker game continuation.\n\nTo install, run\n```bash\npip install pokerlib\n```\n\n## Usage\nLibrary consists of a module for parsing cards, which can be used separately, and modules that aid in running a poker game.\n\n### HandParser\nThis module takes care of hand parsing. A hand usually consists of 2 dealt cards plus 5 on the board, and `HandParser` is heavily optimized to work with up to 7 cards (with more than 7 cards, this is no longer Texas hold\'em). A card is defined as a pair of two enums - Rank and Suit. All of the enums used are of `IntEnum` type, so you can also freely interchange them for integers. Below is an example of how to construct two different hands and then compare them.\n\n```python\nfrom pokerlib import HandParser\nfrom pokerib.enums import Rank, Suit\n\nhand1 = HandParser([\n    (Rank.KING, Suit.SPADE),\n    (Rank.ACE, Suit.SPADE)\n])\n\nhand2 = HandParser([\n    (Rank.NINE, Suit.SPADE),\n    (Rank.TWO, Suit.CLUB)\n])\n\nboard = [\n    (Rank.EIGHT, Suit.SPADE),\n    (Rank.TEN, Suit.SPADE),\n    (Rank.JACK, Suit.SPADE),\n    (Rank.QUEEN, Suit.SPADE),\n    (Rank.TWO, Suit.HEART)\n]\n\n# add new cards to each hand\nhand1 += board # add the board to hand1\nhand2 += board # add the board to hand2\n\nprint(hand1.handenum) # Hand.STRAIGHTFLUSH\nprint(hand2.handenum) # Hand.STRAIGHTFLUSH\nprint(hand1 > hand2) # True\n```\n\n> **note:**\n> In the previous version, each hand had to be parsed manually with `hand.parse()`, now calling any of the methods requiring the hand to be parsed, triggers parsing automatically. This only happens once, except if the cards in a given hand change. The only way cards in a hand should change is through the `__iadd__` method. If this method is called with hand already parsed, the hand is considered unparsed.\n\nIt is also possible to fetch hand\'s kickers.\n\n```python\nhand = HandParser([\n    (Rank.TWO, Suit.DIAMOND),\n    (Rank.ACE, Suit.CLUB),\n    (Rank.TWO, Suit.SPADE),\n    (Rank.THREE, Suit.DIAMOND),\n    (Rank.TEN, Suit.HEART),\n    (Rank.SIX, Suit.HEART),\n    (Rank.KING, Suit.CLUB)\n])\n\nprint(list(hand.kickercards))\n# [\n#   (<Rank.ACE: 12>, <Suit.CLUB: 1>),\n#   (<Rank.KING: 11>, <Suit.CLUB: 1>),\n#   (<Rank.TEN: 8>, <Suit.HEART: 3>)\n# ]\n```\nUsing HandParser, we can [estimate the probability](https://github.com/kuco23/pokerlib/blob/master/examples/winning_probability.py) of a given hand winning the game with given known cards on the table (as implemented in another python cli-app [here](https://github.com/cookpete/poker-odds)). We do this by repeatedly random-sampling hands, then averaging the wins. Mathematically, this process converges to the probability by the law of large numbers.\n\n\n### Poker Game\nA poker table can be established by providing its configuration.\nA poker table object responds to given input with appropriate output,\nwhich can be customized by overriding the two functions producing it.\n\n```python\nfrom pokerlib import Table, Player, PlayerSeats\n\n# table that prints outputs\nclass MyTable(Table):\n    def publicOut(self, out_id, **kwargs):\n        print(out_id, kwargs)\n    def privateOut(self, player_id, out_id, **kwargs):\n        print(out_id, kwargs)\n\n# define a new table\ntable = MyTable(\n    table_id = 0\n    seats = PlayerSeats([None] * 9)\n    buyin = 100\n    small_blind = 5\n    big_blind = 10\n)\n```\n\nWe could have seated players on the `seats` inside `MyTable` constructor,\nbut let\'s add them to the defined table.\n\n```python\nplayer1 = Player(\n    table_id = table.id,\n    _id = 1,\n    name = \'alice\',\n    money = table.buyin\n)\nplayer2 = Player(\n    table_id = table.id,\n    _id = 2,\n    name = \'bob\',\n    money = table.buyin\n)\n# seat player1 at the first seat\ntable += player1, 0\n# seat player2 at the first free seat\ntable += player2\n```\n\nCommunication with the `table` object is established through specified enums,\nwhich can be modified by overriding table\'s `publicIn` method.\nUsing enum IO identifiers, we can implement a poker game as shown below.\n\n```python\nfrom pokerlib.enums import RoundPublicInId, TablePublicInId\n\ntable.publicIn(player1.id, TablePublicInId.STARTROUND)\ntable.publicIn(player1.id, RoundPublicInId.CALL)\ntable.publicIn(player2.id, RoundPublicInId.CHECK)\ntable.publicIn(player1.id, RoundPublicInId.CHECK)\ntable.publicIn(player2.id, RoundPublicInId.RAISE, raise_by=50)\ntable.publicIn(player1.id, RoundPublicInId.CALL)\ntable.publicIn(player1.id, RoundPublicInId.CHECK)\ntable.publicIn(player2.id, RoundPublicInId.CHECK)\ntable.publicIn(player1.id, RoundPublicInId.ALLIN)\ntable.publicIn(player2.id, RoundPublicInId.CALL)\n```\n\nWrong inputs are mostly ignored, though they can produce a response, when it seems useful. As noted before, when providing input, the `table` object responds with output ids (e.g. `PLAYERACTIONREQUIRED`) along with additional data that depends on the output id. For all possible outputs, check `RoundPublicInId` and `TablePublicInId` enums.\n\nA new round has to be initiated by one of the players every time the previous one ends (or at the beginning). A simple command line game, where you respond by enum names, can be implemented as below (for working version check `tests/round_test.py`).\n\n```python\n# define a table with fixed players as before\ntable = ...\nwhile table:\n    while table and not table.round:\n        table.publicIn(\n            table.players[0].id,\n            TablePublicInId.STARTROUND\n        )\n\n    player = table.round.current_player\n    inp = input(f"require input from {player.id}: ")\n\n    if inp in RoundPublicInId.__members__:\n        action, raise_by = RoundPublicInId.__members__[inp], 0\n    elif inp.startswith(RoundPublicInId.RAISE.name):\n        raise_by = int(inp.split()[1])\n        action = RoundPublicInId.RAISE\n    else:\n        continue\n\n    table.publicIn(player.id, action, raise_by=raise_by)\n```\n\nNote that you can define your own IO identifiers for a generalized game,\nas shown in one example [here](https://github.com/kuco23/pokerlib/blob/master/pokerlib/implementations/_table_with_choice_to_show_cards.py).\n\n## Tests\nBasic tests for this library are included. You can test HandParser by running\n```bash\npython tests/handparser_reactive.py\n```\ninitiate a poker round simulation with\n```bash\npython tests/round_test.py <number_of_players>\n```\nwhich will run a poker game simulation with raw data getting printed to stdout. The HandParser functionality was also tested against another poker library [pokerface](https://github.com/AussieSeaweed/pokerface). You can run those tests with\n```bash\npython tests/handparser_against_pokerface.py\n```\n\n## License\nGNU General Public License v3.0\n',
     'author': 'kuco23',
     'author_email': 'nseverkar@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/kuco23/pokerlib/',
```

### Comparing `pokerlib-2.1.0/PKG-INFO` & `pokerlib-2.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pokerlib
-Version: 2.1.0
+Version: 2.1.1
 Summary: Python poker library
 Home-page: https://github.com/kuco23/pokerlib/
 Keywords: python,poker,library
 Author: kuco23
 Author-email: nseverkar@gmail.com
 Requires-Python: >=3.10,<4.0
 Classifier: Development Status :: 3 - Alpha
```

