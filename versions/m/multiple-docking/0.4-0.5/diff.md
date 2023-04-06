# Comparing `tmp/multiple_docking-0.4-py3-none-any.whl.zip` & `tmp/multiple_docking-0.5-py3-none-any.whl.zip`

## zipinfo -v {}

 * *Differences in extra fields detected; using output from zipinfo -v*

```diff
@@ -1,191 +1,401 @@
 There is no zipfile comment.
 
 End-of-central-directory record:
 -------------------------------
 
-  Zip archive file size:                      2735 (0000000000000AAFh)
-  Actual end-cent-dir record offset:          2713 (0000000000000A99h)
-  Expected end-cent-dir record offset:        2713 (0000000000000A99h)
+  Zip archive file size:                      4565 (00000000000011D5h)
+  Actual end-cent-dir record offset:          4543 (00000000000011BFh)
+  Expected end-cent-dir record offset:        4543 (00000000000011BFh)
   (based on the length of the central directory and its expected offset)
 
   This zipfile constitutes the sole disk of a single-part archive; its
-  central directory contains 6 entries.
-  The central directory is 487 (00000000000001E7h) bytes long,
+  central directory contains 10 entries.
+  The central directory is 1385 (0000000000000569h) bytes long,
   and its (expected) offset in bytes from the beginning of the zipfile
-  is 2226 (00000000000008B2h).
+  is 3158 (0000000000000C56h).
 
 
 Central directory entry #1:
 ---------------------------
 
-  multiple_docking/__init__.py
+  multiple_docking-0.5-py3-none-any/
 
   offset of local header from start of archive:   0
                                                   (0000000000000000h) bytes
   file system or operating system of origin:      Unix
   version of encoding software:                   2.0
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
+  compression method:                             none (stored)
+  file security status:                           not encrypted
+  extended local header:                          no
+  file last modified on (DOS date/time):          2023 Apr 7 01:46:40
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:16:40 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:16:40 UTC
+  32-bit CRC value (hex):                         00000000
+  compressed size:                                0 bytes
+  uncompressed size:                              0 bytes
+  length of filename:                             34 characters
+  length of extra field:                          32 bytes
+  length of file comment:                         0 characters
+  disk number on which file begins:               disk 1
+  apparent file type:                             binary
+  Unix file attributes (040775 octal):            drwxrwxr-x
+  MS-DOS file attributes (00 hex):                none
+
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
+  There is no file comment.
+
+Central directory entry #2:
+---------------------------
+
+  There are an extra -8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/multiple_docking/
+
+  offset of local header from start of archive:   96
+                                                  (0000000000000060h) bytes
+  file system or operating system of origin:      Unix
+  version of encoding software:                   2.0
+  minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
+  minimum software version required to extract:   2.0
+  compression method:                             none (stored)
+  file security status:                           not encrypted
+  extended local header:                          no
+  file last modified on (DOS date/time):          2023 Apr 7 01:45:44
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:15:45 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:15:45 UTC
+  32-bit CRC value (hex):                         00000000
+  compressed size:                                0 bytes
+  uncompressed size:                              0 bytes
+  length of filename:                             51 characters
+  length of extra field:                          32 bytes
+  length of file comment:                         0 characters
+  disk number on which file begins:               disk 1
+  apparent file type:                             binary
+  Unix file attributes (040775 octal):            drwxrwxr-x
+  MS-DOS file attributes (00 hex):                none
+
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
+  There is no file comment.
+
+Central directory entry #3:
+---------------------------
+
+  There are an extra -8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/multiple_docking/__init__.py
+
+  offset of local header from start of archive:   209
+                                                  (00000000000000D1h) bytes
+  file system or operating system of origin:      Unix
+  version of encoding software:                   2.0
+  minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
+  minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
-  extended local header:                          no
+  extended local header:                          yes
   file last modified on (DOS date/time):          2023 Apr 6 18:13:08
+  file last modified on (UT extra field modtime): 2023 Apr 6 12:43:08 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 12:43:08 UTC
   32-bit CRC value (hex):                         00000000
   compressed size:                                2 bytes
   uncompressed size:                              0 bytes
-  length of filename:                             28 characters
-  length of extra field:                          0 bytes
+  length of filename:                             62 characters
+  length of extra field:                          32 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   Unix file attributes (100664 octal):            -rw-rw-r--
   MS-DOS file attributes (00 hex):                none
 
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
   There is no file comment.
 
-Central directory entry #2:
+Central directory entry #4:
 ---------------------------
 
-  multiple_docking/docking.py
+  There are an extra 8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/multiple_docking/docking.py
 
-  offset of local header from start of archive:   60
-                                                  (000000000000003Ch) bytes
+  offset of local header from start of archive:   351
+                                                  (000000000000015Fh) bytes
   file system or operating system of origin:      Unix
   version of encoding software:                   2.0
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
-  extended local header:                          no
+  extended local header:                          yes
   file last modified on (DOS date/time):          2023 Jan 30 05:55:24
+  file last modified on (UT extra field modtime): 2023 Jan 30 00:25:24 local
+  file last modified on (UT extra field modtime): 2023 Jan 30 00:25:24 UTC
   32-bit CRC value (hex):                         a601a45d
   compressed size:                                1253 bytes
   uncompressed size:                              4956 bytes
-  length of filename:                             27 characters
-  length of extra field:                          0 bytes
+  length of filename:                             61 characters
+  length of extra field:                          32 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   Unix file attributes (100664 octal):            -rw-rw-r--
   MS-DOS file attributes (00 hex):                none
 
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
   There is no file comment.
 
-Central directory entry #3:
+Central directory entry #5:
 ---------------------------
 
-  multiple_docking-0.4.dist-info/METADATA
+  There are an extra 8 bytes preceding this file.
 
-  offset of local header from start of archive:   1370
-                                                  (000000000000055Ah) bytes
+  multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/
+
+  offset of local header from start of archive:   1743
+                                                  (00000000000006CFh) bytes
+  file system or operating system of origin:      Unix
+  version of encoding software:                   2.0
+  minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
+  minimum software version required to extract:   2.0
+  compression method:                             none (stored)
+  file security status:                           not encrypted
+  extended local header:                          no
+  file last modified on (DOS date/time):          2023 Apr 7 01:45:08
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:15:08 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:15:08 UTC
+  32-bit CRC value (hex):                         00000000
+  compressed size:                                0 bytes
+  uncompressed size:                              0 bytes
+  length of filename:                             65 characters
+  length of extra field:                          32 bytes
+  length of file comment:                         0 characters
+  disk number on which file begins:               disk 1
+  apparent file type:                             binary
+  Unix file attributes (040775 octal):            drwxrwxr-x
+  MS-DOS file attributes (00 hex):                none
+
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
+  There is no file comment.
+
+Central directory entry #6:
+---------------------------
+
+  There are an extra -8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/METADATA
+
+  offset of local header from start of archive:   1870
+                                                  (000000000000074Eh) bytes
   file system or operating system of origin:      Unix
   version of encoding software:                   2.0
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
-  extended local header:                          no
-  file last modified on (DOS date/time):          2023 Apr 6 19:46:38
-  32-bit CRC value (hex):                         78521b2a
-  compressed size:                                167 bytes
+  extended local header:                          yes
+  file last modified on (DOS date/time):          2023 Apr 6 20:14:22
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 UTC
+  32-bit CRC value (hex):                         931ac97d
+  compressed size:                                168 bytes
   uncompressed size:                              239 bytes
-  length of filename:                             39 characters
-  length of extra field:                          0 bytes
+  length of filename:                             73 characters
+  length of extra field:                          32 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   Unix file attributes (100664 octal):            -rw-rw-r--
   MS-DOS file attributes (00 hex):                none
 
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
   There is no file comment.
 
-Central directory entry #4:
+Central directory entry #7:
 ---------------------------
 
-  multiple_docking-0.4.dist-info/WHEEL
+  There are an extra 8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/WHEEL
 
-  offset of local header from start of archive:   1606
-                                                  (0000000000000646h) bytes
+  offset of local header from start of archive:   2189
+                                                  (000000000000088Dh) bytes
   file system or operating system of origin:      Unix
   version of encoding software:                   2.0
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
-  extended local header:                          no
-  file last modified on (DOS date/time):          2023 Apr 6 19:46:38
-  32-bit CRC value (hex):                         cb21a249
+  extended local header:                          yes
+  file last modified on (DOS date/time):          2023 Apr 6 20:14:22
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 UTC
+  32-bit CRC value (hex):                         801a68e9
   compressed size:                                92 bytes
   uncompressed size:                              92 bytes
-  length of filename:                             36 characters
-  length of extra field:                          0 bytes
+  length of filename:                             70 characters
+  length of extra field:                          32 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   Unix file attributes (100664 octal):            -rw-rw-r--
   MS-DOS file attributes (00 hex):                none
 
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
   There is no file comment.
 
-Central directory entry #5:
+Central directory entry #8:
 ---------------------------
 
-  multiple_docking-0.4.dist-info/top_level.txt
+  There are an extra 8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/top_level.txt
 
-  offset of local header from start of archive:   1764
-                                                  (00000000000006E4h) bytes
+  offset of local header from start of archive:   2429
+                                                  (000000000000097Dh) bytes
   file system or operating system of origin:      Unix
   version of encoding software:                   2.0
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
-  extended local header:                          no
-  file last modified on (DOS date/time):          2023 Apr 6 19:46:38
+  extended local header:                          yes
+  file last modified on (DOS date/time):          2023 Apr 6 20:14:22
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 UTC
   32-bit CRC value (hex):                         13974ce1
   compressed size:                                19 bytes
   uncompressed size:                              17 bytes
-  length of filename:                             44 characters
-  length of extra field:                          0 bytes
+  length of filename:                             78 characters
+  length of extra field:                          32 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   Unix file attributes (100664 octal):            -rw-rw-r--
   MS-DOS file attributes (00 hex):                none
 
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
   There is no file comment.
 
-Central directory entry #6:
+Central directory entry #9:
 ---------------------------
 
-  multiple_docking-0.4.dist-info/RECORD
+  There are an extra 8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/RECORD
 
-  offset of local header from start of archive:   1857
-                                                  (0000000000000741h) bytes
+  offset of local header from start of archive:   2604
+                                                  (0000000000000A2Ch) bytes
   file system or operating system of origin:      Unix
   version of encoding software:                   2.0
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
-  extended local header:                          no
-  file last modified on (DOS date/time):          2023 Apr 6 19:46:38
-  32-bit CRC value (hex):                         f3158ada
-  compressed size:                                302 bytes
+  extended local header:                          yes
+  file last modified on (DOS date/time):          2023 Apr 6 20:14:22
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 14:44:22 UTC
+  32-bit CRC value (hex):                         ffbf1ec2
+  compressed size:                                303 bytes
   uncompressed size:                              491 bytes
-  length of filename:                             37 characters
-  length of extra field:                          0 bytes
+  length of filename:                             71 characters
+  length of extra field:                          32 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   Unix file attributes (100664 octal):            -rw-rw-r--
   MS-DOS file attributes (00 hex):                none
 
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
+  There is no file comment.
+
+Central directory entry #10:
+---------------------------
+
+  There are an extra 8 bytes preceding this file.
+
+  multiple_docking-0.5-py3-none-any/grids/
+
+  offset of local header from start of archive:   3056
+                                                  (0000000000000BF0h) bytes
+  file system or operating system of origin:      Unix
+  version of encoding software:                   2.0
+  minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
+  minimum software version required to extract:   2.0
+  compression method:                             none (stored)
+  file security status:                           not encrypted
+  extended local header:                          no
+  file last modified on (DOS date/time):          2023 Apr 7 01:46:26
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:16:26 local
+  file last modified on (UT extra field modtime): 2023 Apr 6 20:16:26 UTC
+  32-bit CRC value (hex):                         00000000
+  compressed size:                                0 bytes
+  uncompressed size:                              0 bytes
+  length of filename:                             40 characters
+  length of extra field:                          32 bytes
+  length of file comment:                         0 characters
+  disk number on which file begins:               disk 1
+  apparent file type:                             binary
+  Unix file attributes (040775 octal):            drwxrwxr-x
+  MS-DOS file attributes (00 hex):                none
+
+  The central-directory extra field contains:
+  - A subfield with ID 0x5455 (universal time) and 13 data bytes.
+    The local extra field has UTC/GMT modification/access/creation times.
+  - A subfield with ID 0x7875 (Unix UID/GID (any size)) and 11 data bytes:
+    01 04 e8 03 00 00 04 e8 03 00 00.
+
   There is no file comment.
```

## zipnote {}

```diff
@@ -1,19 +1,31 @@
-Filename: multiple_docking/__init__.py
+Filename: multiple_docking-0.5-py3-none-any/
 Comment: 
 
-Filename: multiple_docking/docking.py
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking/
 Comment: 
 
-Filename: multiple_docking-0.4.dist-info/METADATA
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking/__init__.py
 Comment: 
 
-Filename: multiple_docking-0.4.dist-info/WHEEL
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking/docking.py
 Comment: 
 
-Filename: multiple_docking-0.4.dist-info/top_level.txt
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/
 Comment: 
 
-Filename: multiple_docking-0.4.dist-info/RECORD
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/METADATA
+Comment: 
+
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/WHEEL
+Comment: 
+
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/top_level.txt
+Comment: 
+
+Filename: multiple_docking-0.5-py3-none-any/multiple_docking-0.5.dist-info/RECORD
+Comment: 
+
+Filename: multiple_docking-0.5-py3-none-any/grids/
 Comment: 
 
 Zip file comment:
```

## filetype from file(1)

```diff
@@ -1 +1 @@
-Zip archive data, at least v2.0 to extract, compression method=deflate
+Zip archive data, at least v2.0 to extract, compression method=store
```

## Comparing `multiple_docking/docking.py` & `multiple_docking-0.5-py3-none-any/multiple_docking/docking.py`

 * *Files identical despite different names*

