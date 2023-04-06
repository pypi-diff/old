# Comparing `tmp/pss_scrambler-0.0.1.4400830929-py2.py3-none-any.whl.zip` & `tmp/pss_scrambler-0.0.2.4632135087-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,13 +1,13 @@
-Zip file size: 31343 bytes, number of entries: 11
--rw-r--r--  2.0 unx     1829 b- defN 23-Mar-13 02:33 pss_scrambler/__main__.py
--rw-r--r--  2.0 unx    59296 b- defN 23-Mar-13 02:33 pss_scrambler/dictionary.py
--rw-r--r--  2.0 unx     2228 b- defN 23-Mar-13 02:33 pss_scrambler/pss_keywords.py
--rw-r--r--  2.0 unx     3930 b- defN 23-Mar-13 02:33 pss_scrambler/translator.py
--rw-r--r--  2.0 unx     1195 b- defN 23-Mar-13 02:33 pss_scrambler/cmds/cmd_encode.py
--rw-r--r--  2.0 unx    11357 b- defN 23-Mar-13 02:34 pss_scrambler-0.0.1.4400830929.dist-info/LICENSE
--rw-r--r--  2.0 unx      476 b- defN 23-Mar-13 02:34 pss_scrambler-0.0.1.4400830929.dist-info/METADATA
--rw-r--r--  2.0 unx      110 b- defN 23-Mar-13 02:34 pss_scrambler-0.0.1.4400830929.dist-info/WHEEL
--rw-r--r--  2.0 unx       62 b- defN 23-Mar-13 02:34 pss_scrambler-0.0.1.4400830929.dist-info/entry_points.txt
--rw-r--r--  2.0 unx       14 b- defN 23-Mar-13 02:34 pss_scrambler-0.0.1.4400830929.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1010 b- defN 23-Mar-13 02:34 pss_scrambler-0.0.1.4400830929.dist-info/RECORD
-11 files, 81507 bytes uncompressed, 29603 bytes compressed:  63.7%
+Zip file size: 31484 bytes, number of entries: 11
+-rw-r--r--  2.0 unx     1829 b- defN 23-Apr-06 18:57 pss_scrambler/__main__.py
+-rw-r--r--  2.0 unx    59296 b- defN 23-Apr-06 18:57 pss_scrambler/dictionary.py
+-rw-r--r--  2.0 unx     2236 b- defN 23-Apr-06 18:57 pss_scrambler/pss_keywords.py
+-rw-r--r--  2.0 unx     4328 b- defN 23-Apr-06 18:57 pss_scrambler/translator.py
+-rw-r--r--  2.0 unx     1195 b- defN 23-Apr-06 18:57 pss_scrambler/cmds/cmd_encode.py
+-rw-r--r--  2.0 unx    11357 b- defN 23-Apr-06 18:58 pss_scrambler-0.0.2.4632135087.dist-info/LICENSE
+-rw-r--r--  2.0 unx      476 b- defN 23-Apr-06 18:58 pss_scrambler-0.0.2.4632135087.dist-info/METADATA
+-rw-r--r--  2.0 unx      110 b- defN 23-Apr-06 18:58 pss_scrambler-0.0.2.4632135087.dist-info/WHEEL
+-rw-r--r--  2.0 unx       62 b- defN 23-Apr-06 18:58 pss_scrambler-0.0.2.4632135087.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx       14 b- defN 23-Apr-06 18:58 pss_scrambler-0.0.2.4632135087.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx     1010 b- defN 23-Apr-06 18:58 pss_scrambler-0.0.2.4632135087.dist-info/RECORD
+11 files, 81913 bytes uncompressed, 29744 bytes compressed:  63.7%
```

## zipnote {}

```diff
@@ -9,26 +9,26 @@
 
 Filename: pss_scrambler/translator.py
 Comment: 
 
 Filename: pss_scrambler/cmds/cmd_encode.py
 Comment: 
 
-Filename: pss_scrambler-0.0.1.4400830929.dist-info/LICENSE
+Filename: pss_scrambler-0.0.2.4632135087.dist-info/LICENSE
 Comment: 
 
-Filename: pss_scrambler-0.0.1.4400830929.dist-info/METADATA
+Filename: pss_scrambler-0.0.2.4632135087.dist-info/METADATA
 Comment: 
 
-Filename: pss_scrambler-0.0.1.4400830929.dist-info/WHEEL
+Filename: pss_scrambler-0.0.2.4632135087.dist-info/WHEEL
 Comment: 
 
-Filename: pss_scrambler-0.0.1.4400830929.dist-info/entry_points.txt
+Filename: pss_scrambler-0.0.2.4632135087.dist-info/entry_points.txt
 Comment: 
 
-Filename: pss_scrambler-0.0.1.4400830929.dist-info/top_level.txt
+Filename: pss_scrambler-0.0.2.4632135087.dist-info/top_level.txt
 Comment: 
 
-Filename: pss_scrambler-0.0.1.4400830929.dist-info/RECORD
+Filename: pss_scrambler-0.0.2.4632135087.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## pss_scrambler/pss_keywords.py

```diff
@@ -11,15 +11,15 @@
 "init_up", "inout", "input", "instance", "int", "join_branch",
 "join_first", "join_none", "join_select", "list", "lock", "map",
 "match", "null", "output", "override", "package", "parallel",
 "pool", "post_solve", "pre_solve", "private", "protected", "public",
 "pure", "rand", "ref", "repeat", "replicate", "resource", "instance_id"
 "return", "run_end", "run_start", "schedule", "select", "sequence",
 "set", "share", "solve", "state", "static", "stream",
-"string", "struct", "super", "symbol", "target", "true",
+"string", "struct", "super", "symbol", "target", "this", "true",
 "type", "typedef", "unique", "void", "while", "with",
 
 # Built-in types from the core library
 "executor_pkg", "executor_trait_s", "empty_executor_trait_s",
 "executor_base_c", "executor_c", "trait",
 "executor_group_c", "add_executor", "executor_claim_s",
 "executor",
```

## pss_scrambler/translator.py

```diff
@@ -105,22 +105,31 @@
     
     def _ungetc(self, c):
         self._c = c
 
     def map_token(self, token):
         remap_i = len(token)-1
 
+        # Find the word category that is closest to the length
+        # of the identifier to be replaced that still has available replacements
         while remap_i < len(self.new_mapping_dict) and len(self.new_mapping_dict[remap_i]) == 0:
             remap_i += 1
 
+        while remap_i >= len(self.new_mapping_dict) or len(self.new_mapping_dict[remap_i]) == 0:
+            remap_i -= 1 
+
         token_xl_i = self.rand.randint(0, len(self.new_mapping_dict[remap_i])-1)
         token_xl = self.new_mapping_dict[remap_i][token_xl_i]
         self.new_mapping_dict[remap_i].pop(token_xl_i)
 
         for s in self.suffixes:
             if token.endswith(s):
                 token_xl += s
                 break
+
+        # If the word to replace is all-uppercase, copy that
+        if token.isupper():
+            token_xl = token_xl.upper()
         
         self.defined_mappings[token] = token_xl
 
         return token_xl
```

## Comparing `pss_scrambler-0.0.1.4400830929.dist-info/LICENSE` & `pss_scrambler-0.0.2.4632135087.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `pss_scrambler-0.0.1.4400830929.dist-info/RECORD` & `pss_scrambler-0.0.2.4632135087.dist-info/RECORD`

 * *Files 21% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 pss_scrambler/__main__.py,sha256=1SudeRWlXTa_zxzSEbAdm9mYFYsouJw5qMMsbFNGpzQ,1829
 pss_scrambler/dictionary.py,sha256=-DeOqEmXZBiACdCIMk2qEb3quoqzslfpdmUP8z1ReWM,59296
-pss_scrambler/pss_keywords.py,sha256=ELkToLU9gDZ5lItBl4GfzPJZ_-ry9CtNks2Tkj91IhE,2228
-pss_scrambler/translator.py,sha256=L4zhbUxaYyJ9mZrPug99u0M-ed_XG9kO1kXadsLYfzk,3930
+pss_scrambler/pss_keywords.py,sha256=bb2_l4QYDl_OClYTJe85DbVCO4j21ouZsKyugqnqwok,2236
+pss_scrambler/translator.py,sha256=Np01A6jrnuK8r2P569Suc9FS4rvmR-hIk29-CBKswDk,4328
 pss_scrambler/cmds/cmd_encode.py,sha256=F3NqFg9xFsIBBpET9Uge0niDId3O5kRfGHHE58gFkFo,1195
-pss_scrambler-0.0.1.4400830929.dist-info/LICENSE,sha256=xx0jnfkXJvxRnG63LTGOxlggYnIysveWIZ6H3PNdCrQ,11357
-pss_scrambler-0.0.1.4400830929.dist-info/METADATA,sha256=HD7BIImTr5obfEF2GyA8QKuP_Nv1as72fGOZ_DI2pIE,476
-pss_scrambler-0.0.1.4400830929.dist-info/WHEEL,sha256=bb2Ot9scclHKMOLDEHY6B2sicWOgugjFKaJsT7vwMQo,110
-pss_scrambler-0.0.1.4400830929.dist-info/entry_points.txt,sha256=zGCNazvFLmPFQeF4kws1Q7Au-eNZmXT-zKNotqH1p20,62
-pss_scrambler-0.0.1.4400830929.dist-info/top_level.txt,sha256=_sUnAKWBK6trQB3OY_t7exQYlUSa_6XG7rgioIBScyg,14
-pss_scrambler-0.0.1.4400830929.dist-info/RECORD,,
+pss_scrambler-0.0.2.4632135087.dist-info/LICENSE,sha256=xx0jnfkXJvxRnG63LTGOxlggYnIysveWIZ6H3PNdCrQ,11357
+pss_scrambler-0.0.2.4632135087.dist-info/METADATA,sha256=cMRPGGIlA1O0iYG8HMUpMLnDobldgAeutZ0-_oS804I,476
+pss_scrambler-0.0.2.4632135087.dist-info/WHEEL,sha256=a-zpFRIJzOq5QfuhBzbhiA1eHTzNCJn8OdRvhdNX0Rk,110
+pss_scrambler-0.0.2.4632135087.dist-info/entry_points.txt,sha256=zGCNazvFLmPFQeF4kws1Q7Au-eNZmXT-zKNotqH1p20,62
+pss_scrambler-0.0.2.4632135087.dist-info/top_level.txt,sha256=_sUnAKWBK6trQB3OY_t7exQYlUSa_6XG7rgioIBScyg,14
+pss_scrambler-0.0.2.4632135087.dist-info/RECORD,,
```

