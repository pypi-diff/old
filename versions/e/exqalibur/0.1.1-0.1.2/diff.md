# Comparing `tmp/exqalibur-0.1.1-cp39-cp39-win_amd64.whl.zip` & `tmp/exqalibur-0.1.2-cp39-cp39-win_amd64.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 1156481 bytes, number of entries: 6
--rw-rw-rw-  2.0 fat  2607616 b- defN 23-Apr-05 09:37 exqalibur.cp39-win_amd64.pyd
--rw-rw-rw-  2.0 fat    13628 b- defN 23-Apr-05 09:37 exqalibur-0.1.1.dist-info/LICENSE.md
--rw-rw-rw-  2.0 fat      634 b- defN 23-Apr-05 09:37 exqalibur-0.1.1.dist-info/METADATA
--rw-rw-rw-  2.0 fat      100 b- defN 23-Apr-05 09:37 exqalibur-0.1.1.dist-info/WHEEL
--rw-rw-rw-  2.0 fat       10 b- defN 23-Apr-05 09:37 exqalibur-0.1.1.dist-info/top_level.txt
--rw-rw-r--  2.0 fat      488 b- defN 23-Apr-05 09:37 exqalibur-0.1.1.dist-info/RECORD
-6 files, 2622476 bytes uncompressed, 1155603 bytes compressed:  55.9%
+Zip file size: 1156484 bytes, number of entries: 6
+-rw-rw-rw-  2.0 fat  2607616 b- defN 23-Apr-07 13:14 exqalibur.cp39-win_amd64.pyd
+-rw-rw-rw-  2.0 fat    13628 b- defN 23-Apr-07 13:14 exqalibur-0.1.2.dist-info/LICENSE.md
+-rw-rw-rw-  2.0 fat      634 b- defN 23-Apr-07 13:14 exqalibur-0.1.2.dist-info/METADATA
+-rw-rw-rw-  2.0 fat      100 b- defN 23-Apr-07 13:14 exqalibur-0.1.2.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat       10 b- defN 23-Apr-07 13:14 exqalibur-0.1.2.dist-info/top_level.txt
+-rw-rw-r--  2.0 fat      488 b- defN 23-Apr-07 13:14 exqalibur-0.1.2.dist-info/RECORD
+6 files, 2622476 bytes uncompressed, 1155606 bytes compressed:  55.9%
```

## zipnote {}

```diff
@@ -1,19 +1,19 @@
 Filename: exqalibur.cp39-win_amd64.pyd
 Comment: 
 
-Filename: exqalibur-0.1.1.dist-info/LICENSE.md
+Filename: exqalibur-0.1.2.dist-info/LICENSE.md
 Comment: 
 
-Filename: exqalibur-0.1.1.dist-info/METADATA
+Filename: exqalibur-0.1.2.dist-info/METADATA
 Comment: 
 
-Filename: exqalibur-0.1.1.dist-info/WHEEL
+Filename: exqalibur-0.1.2.dist-info/WHEEL
 Comment: 
 
-Filename: exqalibur-0.1.1.dist-info/top_level.txt
+Filename: exqalibur-0.1.2.dist-info/top_level.txt
 Comment: 
 
-Filename: exqalibur-0.1.1.dist-info/RECORD
+Filename: exqalibur-0.1.2.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## exqalibur.cp39-win_amd64.pyd

### objdump

```diff
@@ -4,15 +4,15 @@
 start address 0x00000001801a77e8
 
 Characteristics 0x2022
 	executable
 	large address aware
 	DLL
 
-Time/Date		Wed Apr  5 09:37:32 2023
+Time/Date		Fri Apr  7 13:14:22 2023
 Magic			020b	(PE32+)
 MajorLinkerVersion	14
 MinorLinkerVersion	29
 SizeOfCode		00000000001e0600
 SizeOfInitializedData	000000000009e800
 SizeOfUninitializedData	0000000000000000
 AddressOfEntryPoint	00000000001a77e8
@@ -725380,15 +725380,15 @@
    1802357b5:	imul   $0x0,0x0(%rcx,%rdi,2),%esi
    1802357bd:	add    %al,(%rax)
    1802357bf:	add    %bl,0x5f(%rdi)
    1802357c2:	jbe    0x180235829
    1802357c4:	jb     0x180235839
    1802357c6:	imul   $0x30005f5f,0x6e(%rdi),%ebp
    1802357cd:	cs xor %ebp,(%rsi)
-   1802357d0:	xor    %eax,(%rax)
+   1802357d0:	xor    (%rax),%al
    1802357d2:	add    %al,(%rax)
    1802357d4:	add    %al,(%rax)
    1802357d6:	add    %al,(%rax)
    1802357d8:	imul   $0x64696c61,0x76(%rsi),%ebp
    1802357df:	and    %ch,0x61(%rbp)
    1802357e2:	jo     0x180235820
    1802357e4:	rex.WXB sub $0x20,%al
@@ -725785,17 +725785,18 @@
    180235b9f:	(bad)
    180235ba0:	insl   (%dx),%es:(%rdi)
    180235ba1:	imul   $0x74736163,0x5f(%rbx),%esp
    180235ba8:	and    %eax,(%rax)
    180235baa:	add    %al,(%rax)
    180235bac:	add    %al,(%rax)
    180235bae:	add    %al,(%rax)
-   180235bb0:	pop    %rsp
-   180235bb1:	rex.B sub $0x64,%eax
-   180235bb7:	add    %cl,0x0(%rip)        # 0x180235bbd
+   180235bb0:	cs (bad)
+   180235bb2:	xor    %ah,0x0(%rax,%rax,1)
+   180235bb6:	add    %al,(%rax)
+   180235bb8:	or     $0x0,%eax
    180235bbd:	add    $0x0,%al
    180235bbf:	add    %bh,%ah
    180235bc1:	in     (%dx),%al
    180235bc2:	and    (%rax),%eax
    180235bc4:	cld
    180235bc5:	(bad)
    180235bc6:	and    (%rax),%eax
```

## Comparing `exqalibur-0.1.1.dist-info/LICENSE.md` & `exqalibur-0.1.2.dist-info/LICENSE.md`

 * *Files identical despite different names*

## Comparing `exqalibur-0.1.1.dist-info/METADATA` & `exqalibur-0.1.2.dist-info/METADATA`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: exqalibur
-Version: 0.1.1
+Version: 0.1.2
 Summary: Cutting-edge optimization for Perceval
 Home-page: https://perceval.quandela.net
 Author: Perceval.OSS@Quandela.com
 Author-email: Perceval.OSS@Quandela.com
 License: CC BY-NC-ND 4.0
 Project-URL: Documentation, https://perceval.quandela.net/docs-quandelibc/
 Classifier: Programming Language :: Python :: 3
```

