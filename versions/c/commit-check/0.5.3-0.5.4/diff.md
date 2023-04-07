# Comparing `tmp/commit_check-0.5.3-py3-none-any.whl.zip` & `tmp/commit_check-0.5.4-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,15 +1,15 @@
-Zip file size: 11136 bytes, number of entries: 13
--rw-r--r--  2.0 unx     1735 b- defN 23-Feb-24 14:23 commit_check/__init__.py
--rw-r--r--  2.0 unx     1117 b- defN 23-Feb-24 14:23 commit_check/author.py
--rw-r--r--  2.0 unx      926 b- defN 23-Feb-24 14:23 commit_check/branch.py
--rw-r--r--  2.0 unx     1407 b- defN 23-Feb-24 14:23 commit_check/commit.py
--rw-r--r--  2.0 unx     2675 b- defN 23-Feb-24 14:23 commit_check/error.py
--rw-r--r--  2.0 unx     2919 b- defN 23-Feb-24 14:23 commit_check/main.py
--rw-r--r--  2.0 unx     4748 b- defN 23-Feb-24 14:23 commit_check/util.py
--rw-r--r--  2.0 unx     1095 b- defN 23-Feb-24 14:23 commit_check-0.5.3.dist-info/LICENSE
--rw-r--r--  2.0 unx     8605 b- defN 23-Feb-24 14:23 commit_check-0.5.3.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Feb-24 14:23 commit_check-0.5.3.dist-info/WHEEL
--rw-r--r--  2.0 unx       56 b- defN 23-Feb-24 14:23 commit_check-0.5.3.dist-info/entry_points.txt
--rw-r--r--  2.0 unx       13 b- defN 23-Feb-24 14:23 commit_check-0.5.3.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1060 b- defN 23-Feb-24 14:23 commit_check-0.5.3.dist-info/RECORD
-13 files, 26448 bytes uncompressed, 9366 bytes compressed:  64.6%
+Zip file size: 11162 bytes, number of entries: 13
+-rw-r--r--  2.0 unx     1735 b- defN 23-Apr-07 04:57 commit_check/__init__.py
+-rw-r--r--  2.0 unx     1117 b- defN 23-Apr-07 04:57 commit_check/author.py
+-rw-r--r--  2.0 unx      926 b- defN 23-Apr-07 04:57 commit_check/branch.py
+-rw-r--r--  2.0 unx     1407 b- defN 23-Apr-07 04:57 commit_check/commit.py
+-rw-r--r--  2.0 unx     2675 b- defN 23-Apr-07 04:57 commit_check/error.py
+-rw-r--r--  2.0 unx     2919 b- defN 23-Apr-07 04:57 commit_check/main.py
+-rw-r--r--  2.0 unx     4748 b- defN 23-Apr-07 04:57 commit_check/util.py
+-rw-r--r--  2.0 unx     1095 b- defN 23-Apr-07 04:57 commit_check-0.5.4.dist-info/LICENSE
+-rw-r--r--  2.0 unx     8716 b- defN 23-Apr-07 04:57 commit_check-0.5.4.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 04:57 commit_check-0.5.4.dist-info/WHEEL
+-rw-r--r--  2.0 unx       56 b- defN 23-Apr-07 04:57 commit_check-0.5.4.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx       13 b- defN 23-Apr-07 04:57 commit_check-0.5.4.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx     1060 b- defN 23-Apr-07 04:57 commit_check-0.5.4.dist-info/RECORD
+13 files, 26559 bytes uncompressed, 9392 bytes compressed:  64.6%
```

## zipnote {}

```diff
@@ -15,26 +15,26 @@
 
 Filename: commit_check/main.py
 Comment: 
 
 Filename: commit_check/util.py
 Comment: 
 
-Filename: commit_check-0.5.3.dist-info/LICENSE
+Filename: commit_check-0.5.4.dist-info/LICENSE
 Comment: 
 
-Filename: commit_check-0.5.3.dist-info/METADATA
+Filename: commit_check-0.5.4.dist-info/METADATA
 Comment: 
 
-Filename: commit_check-0.5.3.dist-info/WHEEL
+Filename: commit_check-0.5.4.dist-info/WHEEL
 Comment: 
 
-Filename: commit_check-0.5.3.dist-info/entry_points.txt
+Filename: commit_check-0.5.4.dist-info/entry_points.txt
 Comment: 
 
-Filename: commit_check-0.5.3.dist-info/top_level.txt
+Filename: commit_check-0.5.4.dist-info/top_level.txt
 Comment: 
 
-Filename: commit_check-0.5.3.dist-info/RECORD
+Filename: commit_check-0.5.4.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `commit_check-0.5.3.dist-info/LICENSE` & `commit_check-0.5.4.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `commit_check-0.5.3.dist-info/METADATA` & `commit_check-0.5.4.dist-info/METADATA`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: commit-check
-Version: 0.5.3
+Version: 0.5.4
 Summary: Check commit message formatting, branch naming, commit author, email, and more.
 Author-email: Peter Shen <xianpeng.shen@gmail.com>
 License: MIT License
 Project-URL: source, https://github.com/commit-check/commit-check
 Project-URL: tracker, https://github.com/commit-check/commit-check/issues
 Keywords: commit conventions,conventional commits,branch naming,commit-check,message,lint message
 Classifier: Development Status :: 4 - Beta
@@ -107,17 +107,19 @@
 
     Make sure ``pre-commit`` is `installed <https://pre-commit.com/#install>`_.
 
 .. code-block:: yaml
 
     -   repo: https://github.com/commit-check/commit-check
         rev: the tag or revision
-        hooks:
+        hooks: # support hooks
         -   id: check-message
         -   id: check-branch
+        -   id: check-author-name
+        -   id: check-author-email
 
 Running as CLI
 ~~~~~~~~~~~~~~
 
 Global installation
 
 .. code-block:: bash
@@ -182,15 +184,15 @@
     The commit message should be structured as follows:
 
     <type>[optional scope]: <description>
     [optional body]
     [optional footer(s)]
 
     More details please refer to https://www.conventionalcommits.org
-    Suggest to run => git commit --amend --no-verify
+    Suggest: please check your commit message whether matches above regex
 
 
 Check branch naming failed
 
 .. code-block:: text
 
     Commit rejected by Commit-Check.
@@ -206,15 +208,15 @@
 
     Commit rejected.
 
     Invalid branch name => test
     It doesn't match regex: ^(bugfix|feature|release|hotfix|task)\/.+|(master)|(main)|(HEAD)|(PR-.+)
 
     Branches must begin with these types: bugfix/ feature/ release/ hotfix/ task/
-    Suggest to run => git checkout -b type/branch_name
+    Suggest: run command `git checkout -b type/branch_name`
 
 
 Badging your repository
 -----------------------
 
 You can add a badge to your repository to show your contributors / users that you use commit-check!
```

## Comparing `commit_check-0.5.3.dist-info/RECORD` & `commit_check-0.5.4.dist-info/RECORD`

 * *Files 10% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 commit_check/__init__.py,sha256=kTDjVl3aBz6rp3HHv10dhOm7B1_ZmTMHzNg_0earx0k,1735
 commit_check/author.py,sha256=Vo642jgwY_4Y9Ea48dFd_Dvfr5uzzBW9yVNTETFHnCA,1117
 commit_check/branch.py,sha256=4Vt5qf3NniQdMA5x19kE3xLClyLDGFKRZhP_veXn7y0,926
 commit_check/commit.py,sha256=NXVEGT6u9sziXgtcD0PYKihAksugi8sS9xJJUfFTyqA,1407
 commit_check/error.py,sha256=z3WQRKII6WPqEBgBQVeclg8AYqwr4lqX1ssQs3bKZLQ,2675
 commit_check/main.py,sha256=mSC05heXp0ZDGWT-yQKVa8WyuXVAnwO0aRN7xs51P5I,2919
 commit_check/util.py,sha256=bWnRFp7G-OBBxEmn_xe0laVbFEJzOMPAcclIZKITROU,4748
-commit_check-0.5.3.dist-info/LICENSE,sha256=VAJ9TE1ov8aUKmeoBRYqciMs0CXag1TeDCoLhwbeQmA,1095
-commit_check-0.5.3.dist-info/METADATA,sha256=hvGxx5WwIKvA5REd-VFBTTv0I3hIEDyZkVAv8nuEhYQ,8605
-commit_check-0.5.3.dist-info/WHEEL,sha256=2wepM1nk4DS4eFpYrW1TTqPcoGNfHhhO_i5m4cOimbo,92
-commit_check-0.5.3.dist-info/entry_points.txt,sha256=2IMogDXLAFnwmH_-_EFBwYixY9sTvcwxze59OFs8ybA,56
-commit_check-0.5.3.dist-info/top_level.txt,sha256=Wf46u-ooHBMJNHbhfrBNQw3wC5_m8wt-o_Lfbc4QpRg,13
-commit_check-0.5.3.dist-info/RECORD,,
+commit_check-0.5.4.dist-info/LICENSE,sha256=VAJ9TE1ov8aUKmeoBRYqciMs0CXag1TeDCoLhwbeQmA,1095
+commit_check-0.5.4.dist-info/METADATA,sha256=6X-6yxLsKL_kytZ5jlTpFEfgQBAjAUcml0taBeCLiDo,8716
+commit_check-0.5.4.dist-info/WHEEL,sha256=pkctZYzUS4AYVn6dJ-7367OJZivF2e8RA9b_ZBjif18,92
+commit_check-0.5.4.dist-info/entry_points.txt,sha256=2IMogDXLAFnwmH_-_EFBwYixY9sTvcwxze59OFs8ybA,56
+commit_check-0.5.4.dist-info/top_level.txt,sha256=Wf46u-ooHBMJNHbhfrBNQw3wC5_m8wt-o_Lfbc4QpRg,13
+commit_check-0.5.4.dist-info/RECORD,,
```

