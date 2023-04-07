# Comparing `tmp/portage-3.0.45.3.tar.gz` & `tmp/portage-3.0.46.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "portage-3.0.45.3.tar", last modified: Sun Mar 19 19:18:17 2023, max compression
+gzip compressed data, was "portage-3.0.46.tar", last modified: Fri Apr  7 09:56:10 2023, max compression
```

## Comparing `portage-3.0.45.3.tar` & `portage-3.0.46.tar`

### file list

```diff
@@ -1,941 +1,941 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:35.927469 portage-3.0.45.3/.portage_not_installed
--rw-r--r--   0 root         (0) root         (0)     6944 2023-03-04 05:38:59.985059 portage-3.0.45.3/DEVELOPING
--rw-r--r--   0 root         (0) root         (0)    18092 2021-11-12 08:15:35.927469 portage-3.0.45.3/LICENSE
--rw-r--r--   0 root         (0) root         (0)     4476 2023-03-19 19:18:17.020742 portage-3.0.45.3/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1864 2021-11-12 08:15:35.927469 portage-3.0.45.3/TEST-NOTES
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.994075 portage-3.0.45.3/bin/
--rwxr-xr-x   0 root         (0) root         (0)     3186 2023-01-10 15:14:54.923158 portage-3.0.45.3/bin/archive-conf
--rwxr-xr-x   0 root         (0) root         (0)     1443 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/bashrc-functions.sh
--rwxr-xr-x   0 root         (0) root         (0)     4487 2023-01-10 15:14:54.926491 portage-3.0.45.3/bin/binhost-snapshot
--rwxr-xr-x   0 root         (0) root         (0)       51 2021-11-12 08:15:35.934136 portage-3.0.45.3/bin/cgroup-release-agent
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.934136 portage-3.0.45.3/bin/chmod-lite -> ebuild-pyhelper
--rwxr-xr-x   0 root         (0) root         (0)      951 2023-02-03 17:42:31.189179 portage-3.0.45.3/bin/chmod-lite.py
--rwxr-xr-x   0 root         (0) root         (0)     5891 2023-02-03 17:42:31.189179 portage-3.0.45.3/bin/chpathtool.py
--rwxr-xr-x   0 root         (0) root         (0)     1421 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/clean_locks
--rwxr-xr-x   0 root         (0) root         (0)    19884 2023-02-03 17:42:31.192513 portage-3.0.45.3/bin/dispatch-conf
--rwxr-xr-x   0 root         (0) root         (0)     8895 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/dohtml.py
--rwxr-xr-x   0 root         (0) root         (0)    20007 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/doins.py
--rwxr-xr-x   0 root         (0) root         (0)     6078 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/eapi.sh
--rwxr-xr-x   0 root         (0) root         (0)     4310 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/eapi7-ver-funcs.sh
--rwxr-xr-x   0 root         (0) root         (0)    15483 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/bin/ebuild-helpers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/bin/ebuild-helpers/bsd/
--rwxr-xr-x   0 root         (0) root         (0)      639 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/bsd/sed
--rwxr-xr-x   0 root         (0) root         (0)      200 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/die
--rwxr-xr-x   0 root         (0) root         (0)     1052 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/dobin
--rwxr-xr-x   0 root         (0) root         (0)      515 2022-09-10 09:45:01.063717 portage-3.0.45.3/bin/ebuild-helpers/doconfd
--rwxr-xr-x   0 root         (0) root         (0)      359 2022-09-10 09:45:01.057050 portage-3.0.45.3/bin/ebuild-helpers/dodir
--rwxr-xr-x   0 root         (0) root         (0)      888 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/dodoc
--rwxr-xr-x   0 root         (0) root         (0)      513 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/doenvd
--rwxr-xr-x   0 root         (0) root         (0)      955 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/doexe
--rwxr-xr-x   0 root         (0) root         (0)      531 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/dohard
--rwxr-xr-x   0 root         (0) root         (0)      632 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/doheader
--rwxr-xr-x   0 root         (0) root         (0)      782 2022-09-10 09:45:01.063717 portage-3.0.45.3/bin/ebuild-helpers/dohtml
--rwxr-xr-x   0 root         (0) root         (0)      722 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/doinfo
--rwxr-xr-x   0 root         (0) root         (0)      485 2022-09-10 09:45:01.063717 portage-3.0.45.3/bin/ebuild-helpers/doinitd
--rwxr-xr-x   0 root         (0) root         (0)     3034 2022-09-10 09:45:01.057050 portage-3.0.45.3/bin/ebuild-helpers/doins
--rwxr-xr-x   0 root         (0) root         (0)     1441 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/dolib
--rwxr-xr-x   0 root         (0) root         (0)      189 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/dolib.a
--rwxr-xr-x   0 root         (0) root         (0)      189 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/dolib.so
--rwxr-xr-x   0 root         (0) root         (0)     1553 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/doman
--rwxr-xr-x   0 root         (0) root         (0)     1219 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/domo
--rwxr-xr-x   0 root         (0) root         (0)     1056 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/dosbin
--rwxr-xr-x   0 root         (0) root         (0)      818 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/dosed
--rwxr-xr-x   0 root         (0) root         (0)     2366 2022-09-10 09:45:01.063717 portage-3.0.45.3/bin/ebuild-helpers/dosym
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.45.3/bin/ebuild-helpers/eerror -> elog
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.45.3/bin/ebuild-helpers/einfo -> elog
--rwxr-xr-x   0 root         (0) root         (0)      204 2022-09-10 09:45:01.053717 portage-3.0.45.3/bin/ebuild-helpers/elog
--rwxr-xr-x   0 root         (0) root         (0)      894 2022-09-10 09:45:01.053717 portage-3.0.45.3/bin/ebuild-helpers/emake
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.45.3/bin/ebuild-helpers/eqawarn -> elog
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.45.3/bin/ebuild-helpers/ewarn -> elog
--rwxr-xr-x   0 root         (0) root         (0)      792 2022-09-10 09:45:01.057050 portage-3.0.45.3/bin/ebuild-helpers/fowners
--rwxr-xr-x   0 root         (0) root         (0)      850 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/fperms
--rwxr-xr-x   0 root         (0) root         (0)      490 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/keepdir
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newbin -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newconfd -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newdoc -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newenvd -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newexe -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newheader -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newinitd -> newins
--rwxr-xr-x   0 root         (0) root         (0)     1201 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild-helpers/newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newlib.a -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newlib.so -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newman -> newins
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/newsbin -> newins
--rwxr-xr-x   0 root         (0) root         (0)      359 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/nonfatal
--rwxr-xr-x   0 root         (0) root         (0)      739 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/portageq
--rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/prepall
--rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.053717 portage-3.0.45.3/bin/ebuild-helpers/prepalldocs
--rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.053717 portage-3.0.45.3/bin/ebuild-helpers/prepallinfo
--rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.053717 portage-3.0.45.3/bin/ebuild-helpers/prepallman
--rwxr-xr-x   0 root         (0) root         (0)      383 2022-09-10 09:45:01.057050 portage-3.0.45.3/bin/ebuild-helpers/prepallstrip
--rwxr-xr-x   0 root         (0) root         (0)      779 2022-12-24 02:35:49.842656 portage-3.0.45.3/bin/ebuild-helpers/prepinfo
--rwxr-xr-x   0 root         (0) root         (0)      241 2022-09-10 09:45:01.057050 portage-3.0.45.3/bin/ebuild-helpers/prepman
--rwxr-xr-x   0 root         (0) root         (0)      375 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/prepstrip
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/bin/ebuild-helpers/unprivileged/
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-helpers/unprivileged/chgrp -> chown
--rwxr-xr-x   0 root         (0) root         (0)     1178 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/unprivileged/chown
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/bin/ebuild-helpers/xattr/
--rwxr-xr-x   0 root         (0) root         (0)     1369 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ebuild-helpers/xattr/install
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.45.3/bin/ebuild-ipc -> ebuild-pyhelper
--rwxr-xr-x   0 root         (0) root         (0)    10830 2023-02-03 17:42:31.192513 portage-3.0.45.3/bin/ebuild-ipc.py
--rwxr-xr-x   0 root         (0) root         (0)      616 2022-09-10 09:45:01.057050 portage-3.0.45.3/bin/ebuild-pyhelper
--rwxr-xr-x   0 root         (0) root         (0)    26114 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/ebuild.sh
--rwxr-xr-x   0 root         (0) root         (0)     6481 2022-12-24 02:35:49.845990 portage-3.0.45.3/bin/ecompress
--rwxr-xr-x   0 root         (0) root         (0)     1746 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/ecompress-file
--rwxr-xr-x   0 root         (0) root         (0)    54393 2023-02-03 17:42:31.189179 portage-3.0.45.3/bin/egencache
--rwxr-xr-x   0 root         (0) root         (0)     1857 2023-02-03 17:42:31.189179 portage-3.0.45.3/bin/emaint
--rwxr-xr-x   0 root         (0) root         (0)     3303 2023-02-03 17:42:31.192513 portage-3.0.45.3/bin/emerge
--rwxr-xr-x   0 root         (0) root         (0)    15950 2022-09-10 09:45:01.063717 portage-3.0.45.3/bin/emerge-webrsync
--rwxr-xr-x   0 root         (0) root         (0)      634 2022-09-10 09:45:01.053717 portage-3.0.45.3/bin/emirrordist
--rwxr-xr-x   0 root         (0) root         (0)     1048 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/env-update
--rwxr-xr-x   0 root         (0) root         (0)    17296 2023-01-10 14:04:05.114706 portage-3.0.45.3/bin/estrip
--rwxr-xr-x   0 root         (0) root         (0)    23444 2022-12-24 02:35:49.849323 portage-3.0.45.3/bin/etc-update
--rwxr-xr-x   0 root         (0) root         (0)     6045 2023-01-10 15:12:38.505765 portage-3.0.45.3/bin/filter-bash-environment.py
--rwxr-xr-x   0 root         (0) root         (0)     1601 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/fixpackages
--rwxr-xr-x   0 root         (0) root         (0)    15652 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/glsa-check
--rwxr-xr-x   0 root         (0) root         (0)     2166 2023-02-03 17:42:31.192513 portage-3.0.45.3/bin/gpkg-helper.py
--rwxr-xr-x   0 root         (0) root         (0)     2476 2022-12-24 02:35:49.845990 portage-3.0.45.3/bin/gpkg-sign
--rwxr-xr-x   0 root         (0) root         (0)     2918 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/helper-functions.sh
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/bin/install-qa-check.d/
--rwxr-xr-x   0 root         (0) root         (0)      444 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/05double-D
--rwxr-xr-x   0 root         (0) root         (0)     4302 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/05prefix
--rwxr-xr-x   0 root         (0) root         (0)     5559 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/10executable-issues
--rwxr-xr-x   0 root         (0) root         (0)     3591 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/10ignored-flags
--rwxr-xr-x   0 root         (0) root         (0)      406 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/20deprecated-directories
--rwxr-xr-x   0 root         (0) root         (0)      835 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/20runtime-directories
--rwxr-xr-x   0 root         (0) root         (0)     3306 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/60bash-completion
--rwxr-xr-x   0 root         (0) root         (0)     1443 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/60openrc
--rwxr-xr-x   0 root         (0) root         (0)     5508 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/60pkgconfig
--rwxr-xr-x   0 root         (0) root         (0)      668 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/60pngfix
--rwxr-xr-x   0 root         (0) root         (0)      687 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/60systemd
--rwxr-xr-x   0 root         (0) root         (0)      442 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/60udev
--rwxr-xr-x   0 root         (0) root         (0)     5556 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/80libraries
--rwxr-xr-x   0 root         (0) root         (0)     1417 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/80multilib-strict
--rwxr-xr-x   0 root         (0) root         (0)     1918 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/90bad-bin-group-write
--rwxr-xr-x   0 root         (0) root         (0)     1566 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/90bad-bin-owner
--rwxr-xr-x   0 root         (0) root         (0)      654 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/90cmake-warnings
--rwxr-xr-x   0 root         (0) root         (0)     3333 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/90config-impl-decl
--rwxr-xr-x   0 root         (0) root         (0)     7866 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/90gcc-warnings
--rwxr-xr-x   0 root         (0) root         (0)     1042 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/90world-writable
--rwxr-xr-x   0 root         (0) root         (0)     1518 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/install-qa-check.d/95empty-dirs
--rwxr-xr-x   0 root         (0) root         (0)     6332 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/install.py
--rwxr-xr-x   0 root         (0) root         (0)    18494 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/isolated-functions.sh
--rwxr-xr-x   0 root         (0) root         (0)      903 2023-02-03 17:42:31.189179 portage-3.0.45.3/bin/lock-helper.py
--rwxr-xr-x   0 root         (0) root         (0)    19664 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/misc-functions.sh
--rwxr-xr-x   0 root         (0) root         (0)    34584 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/phase-functions.sh
--rwxr-xr-x   0 root         (0) root         (0)    33794 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/phase-helpers.sh
--rwxr-xr-x   0 root         (0) root         (0)     5723 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/pid-ns-init
--rwxr-xr-x   0 root         (0) root         (0)    51246 2023-02-03 18:03:13.730194 portage-3.0.45.3/bin/portageq
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/bin/postinst-qa-check.d/
--rwxr-xr-x   0 root         (0) root         (0)     5236 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/postinst-qa-check.d/50xdg-utils
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/bin/preinst-qa-check.d/
-lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.947469 portage-3.0.45.3/bin/preinst-qa-check.d/50xdg-utils -> ../postinst-qa-check.d/50xdg-utils
--rwxr-xr-x   0 root         (0) root         (0)    16762 2023-01-10 15:14:54.926491 portage-3.0.45.3/bin/quickpkg
--rwxr-xr-x   0 root         (0) root         (0)     4992 2023-01-10 15:14:54.923158 portage-3.0.45.3/bin/regenworld
--rwxr-xr-x   0 root         (0) root         (0)     4524 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/save-ebuild-env.sh
--rwxr-xr-x   0 root         (0) root         (0)     1339 2022-09-10 09:45:01.060384 portage-3.0.45.3/bin/shelve-utils
--rwxr-xr-x   0 root         (0) root         (0)     8140 2023-03-11 18:51:46.315786 portage-3.0.45.3/bin/socks5-server.py
--rwxr-xr-x   0 root         (0) root         (0)     4794 2023-02-03 17:42:31.192513 portage-3.0.45.3/bin/xattr-helper.py
--rwxr-xr-x   0 root         (0) root         (0)     1825 2023-02-03 17:42:31.192513 portage-3.0.45.3/bin/xpak-helper.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.997408 portage-3.0.45.3/cnf/
--rw-r--r--   0 root         (0) root         (0)     1718 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.alpha.diff
--rw-r--r--   0 root         (0) root         (0)     2319 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.amd64-fbsd.diff
--rw-r--r--   0 root         (0) root         (0)     2309 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.amd64.diff
--rw-r--r--   0 root         (0) root         (0)     1592 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.arm.diff
--rw-r--r--   0 root         (0) root         (0)     1580 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.arm64.diff
--rw-r--r--   0 root         (0) root         (0)     2465 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.hppa.diff
--rw-r--r--   0 root         (0) root         (0)      663 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.ia64.diff
--rw-r--r--   0 root         (0) root         (0)     2192 2022-12-24 02:35:49.845990 portage-3.0.45.3/cnf/make.conf.example.loong.diff
--rw-r--r--   0 root         (0) root         (0)      900 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.m68k.diff
--rw-r--r--   0 root         (0) root         (0)     1383 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.mips.diff
--rw-r--r--   0 root         (0) root         (0)     3541 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.ppc.diff
--rw-r--r--   0 root         (0) root         (0)     2361 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.ppc64.diff
--rw-r--r--   0 root         (0) root         (0)     2332 2022-09-10 09:44:56.963689 portage-3.0.45.3/cnf/make.conf.example.riscv.diff
--rw-r--r--   0 root         (0) root         (0)      656 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.s390.diff
--rw-r--r--   0 root         (0) root         (0)     1257 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.sh.diff
--rw-r--r--   0 root         (0) root         (0)      728 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.sparc-fbsd.diff
--rw-r--r--   0 root         (0) root         (0)     2129 2021-12-09 09:19:33.760140 portage-3.0.45.3/cnf/make.conf.example.sparc.diff
--rw-r--r--   0 root         (0) root         (0)     2507 2021-12-09 09:19:33.763473 portage-3.0.45.3/cnf/make.conf.example.x86-fbsd.diff
--rw-r--r--   0 root         (0) root         (0)     3759 2021-12-09 09:19:33.763473 portage-3.0.45.3/cnf/make.conf.example.x86.diff
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.000742 portage-3.0.45.3/doc/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.000742 portage-3.0.45.3/doc/api/
--rw-r--r--   0 root         (0) root         (0)     1141 2021-11-12 08:15:35.954135 portage-3.0.45.3/doc/api/Makefile
--rw-r--r--   0 root         (0) root         (0)     2372 2022-12-24 02:35:49.845990 portage-3.0.45.3/doc/api/conf.py
--rw-r--r--   0 root         (0) root         (0)      217 2021-11-12 08:15:35.954135 portage-3.0.45.3/doc/api/index.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.000742 portage-3.0.45.3/doc/config/
--rw-r--r--   0 root         (0) root         (0)     1900 2021-11-12 08:15:35.954135 portage-3.0.45.3/doc/config/bashrc.docbook
--rw-r--r--   0 root         (0) root         (0)    26214 2021-11-12 08:15:35.954135 portage-3.0.45.3/doc/config/sets.docbook
--rw-r--r--   0 root         (0) root         (0)       85 2021-11-12 08:15:35.954135 portage-3.0.45.3/doc/config.docbook
--rw-r--r--   0 root         (0) root         (0)      257 2021-11-12 08:15:35.954135 portage-3.0.45.3/doc/custom.xsl
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.000742 portage-3.0.45.3/doc/dependency_resolution/
--rw-r--r--   0 root         (0) root         (0)     3281 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/dependency_resolution/decision_making.docbook
--rw-r--r--   0 root         (0) root         (0)     4154 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/dependency_resolution/package_modeling.docbook
--rw-r--r--   0 root         (0) root         (0)     3451 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/dependency_resolution/task_scheduling.docbook
--rw-r--r--   0 root         (0) root         (0)      200 2021-11-12 08:15:35.954135 portage-3.0.45.3/doc/dependency_resolution.docbook
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.000742 portage-3.0.45.3/doc/package/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.000742 portage-3.0.45.3/doc/package/ebuild/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.000742 portage-3.0.45.3/doc/package/ebuild/eapi/
--rw-r--r--   0 root         (0) root         (0)      487 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/eapi/0.docbook
--rw-r--r--   0 root         (0) root         (0)     1598 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/eapi/1.docbook
--rw-r--r--   0 root         (0) root         (0)     8299 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/eapi/2.docbook
--rw-r--r--   0 root         (0) root         (0)     2938 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/eapi/3.docbook
--rw-r--r--   0 root         (0) root         (0)     3112 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/eapi/4-slot-abi.docbook
--rw-r--r--   0 root         (0) root         (0)    14690 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/eapi/4.docbook
--rw-r--r--   0 root         (0) root         (0)     8044 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/eapi/5.docbook
--rw-r--r--   0 root         (0) root         (0)     1725 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/helper_functions.docbook
--rw-r--r--   0 root         (0) root         (0)     2780 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package/ebuild/phases.docbook
--rw-r--r--   0 root         (0) root         (0)      364 2022-09-10 09:45:01.060384 portage-3.0.45.3/doc/package/ebuild.docbook
--rw-r--r--   0 root         (0) root         (0)       76 2021-11-12 08:15:35.957468 portage-3.0.45.3/doc/package.docbook
--rw-r--r--   0 root         (0) root         (0)     2194 2022-09-10 09:45:01.060384 portage-3.0.45.3/doc/portage.docbook
--rw-r--r--   0 root         (0) root         (0)    19579 2021-11-12 08:15:35.960802 portage-3.0.45.3/doc/qa.docbook
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:16.987408 portage-3.0.45.3/lib/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/_emerge/
--rw-r--r--   0 root         (0) root         (0)      816 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/AbstractDepPriority.py
--rw-r--r--   0 root         (0) root         (0)    18470 2023-02-11 02:54:54.195728 portage-3.0.45.3/lib/_emerge/AbstractEbuildProcess.py
--rw-r--r--   0 root         (0) root         (0)     3723 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/AbstractPollTask.py
--rw-r--r--   0 root         (0) root         (0)    10471 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/AsynchronousLock.py
--rw-r--r--   0 root         (0) root         (0)     7090 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/AsynchronousTask.py
--rw-r--r--   0 root         (0) root         (0)      473 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/AtomArg.py
--rw-r--r--   0 root         (0) root         (0)    21241 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/Binpkg.py
--rw-r--r--   0 root         (0) root         (0)     2367 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/BinpkgEnvExtractor.py
--rw-r--r--   0 root         (0) root         (0)     5494 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/BinpkgExtractorAsync.py
--rw-r--r--   0 root         (0) root         (0)     9584 2023-02-17 01:23:14.667857 portage-3.0.45.3/lib/_emerge/BinpkgFetcher.py
--rw-r--r--   0 root         (0) root         (0)     1684 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/BinpkgPrefetcher.py
--rw-r--r--   0 root         (0) root         (0)     4414 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/BinpkgVerifier.py
--rw-r--r--   0 root         (0) root         (0)      483 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/Blocker.py
--rw-r--r--   0 root         (0) root         (0)     6827 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/BlockerCache.py
--rw-r--r--   0 root         (0) root         (0)     5325 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/BlockerDB.py
--rw-r--r--   0 root         (0) root         (0)      355 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/BlockerDepPriority.py
--rw-r--r--   0 root         (0) root         (0)     4044 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/CompositeTask.py
--rw-r--r--   0 root         (0) root         (0)     1732 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/DepPriority.py
--rw-r--r--   0 root         (0) root         (0)     1564 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/DepPriorityNormalRange.py
--rw-r--r--   0 root         (0) root         (0)     3647 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/DepPrioritySatisfiedRange.py
--rw-r--r--   0 root         (0) root         (0)      878 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/Dependency.py
--rw-r--r--   0 root         (0) root         (0)     1056 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/DependencyArg.py
--rw-r--r--   0 root         (0) root         (0)     2050 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/EbuildBinpkg.py
--rw-r--r--   0 root         (0) root         (0)    23204 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/EbuildBuild.py
--rw-r--r--   0 root         (0) root         (0)     5749 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/EbuildBuildDir.py
--rw-r--r--   0 root         (0) root         (0)     2961 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/EbuildExecuter.py
--rw-r--r--   0 root         (0) root         (0)    14395 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/EbuildFetcher.py
--rw-r--r--   0 root         (0) root         (0)     1359 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/EbuildFetchonly.py
--rw-r--r--   0 root         (0) root         (0)     4716 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/EbuildIpcDaemon.py
--rw-r--r--   0 root         (0) root         (0)     3258 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/EbuildMerge.py
--rw-r--r--   0 root         (0) root         (0)     7597 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/EbuildMetadataPhase.py
--rw-r--r--   0 root         (0) root         (0)    22622 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/EbuildPhase.py
--rw-r--r--   0 root         (0) root         (0)      872 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/EbuildProcess.py
--rw-r--r--   0 root         (0) root         (0)      679 2023-02-03 17:42:31.189179 portage-3.0.45.3/lib/_emerge/EbuildSpawnProcess.py
--rw-r--r--   0 root         (0) root         (0)    12786 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/FakeVartree.py
--rw-r--r--   0 root         (0) root         (0)     1774 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/FifoIpcDaemon.py
--rw-r--r--   0 root         (0) root         (0)     9113 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/JobStatusDisplay.py
--rw-r--r--   0 root         (0) root         (0)     4823 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/MergeListItem.py
--rw-r--r--   0 root         (0) root         (0)     6121 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/MetadataRegen.py
--rw-r--r--   0 root         (0) root         (0)     2424 2022-09-10 09:45:01.063717 portage-3.0.45.3/lib/_emerge/MiscFunctionsProcess.py
--rw-r--r--   0 root         (0) root         (0)    31019 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/Package.py
--rw-r--r--   0 root         (0) root         (0)      735 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/_emerge/PackageArg.py
--rw-r--r--   0 root         (0) root         (0)     2626 2023-02-18 00:00:12.895319 portage-3.0.45.3/lib/_emerge/PackageMerge.py
--rw-r--r--   0 root         (0) root         (0)     4333 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/_emerge/PackagePhase.py
--rw-r--r--   0 root         (0) root         (0)     5870 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/PackageUninstall.py
--rw-r--r--   0 root         (0) root         (0)     4651 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/_emerge/PackageVirtualDbapi.py
--rw-r--r--   0 root         (0) root         (0)     2681 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/PipeReader.py
--rw-r--r--   0 root         (0) root         (0)     6630 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/PollScheduler.py
--rw-r--r--   0 root         (0) root         (0)      603 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/_emerge/ProgressHandler.py
--rw-r--r--   0 root         (0) root         (0)     1227 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/_emerge/RootConfig.py
--rw-r--r--   0 root         (0) root         (0)    85615 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/Scheduler.py
--rw-r--r--   0 root         (0) root         (0)     2648 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/SequentialTaskQueue.py
--rw-r--r--   0 root         (0) root         (0)      421 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/SetArg.py
--rw-r--r--   0 root         (0) root         (0)    10190 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/SpawnProcess.py
--rw-r--r--   0 root         (0) root         (0)     3167 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/SubProcess.py
--rw-r--r--   0 root         (0) root         (0)     1456 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/_emerge/Task.py
--rw-r--r--   0 root         (0) root         (0)     1538 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/TaskSequence.py
--rw-r--r--   0 root         (0) root         (0)      455 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/UninstallFailure.py
--rw-r--r--   0 root         (0) root         (0)     1326 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/UnmergeDepPriority.py
--rw-r--r--   0 root         (0) root         (0)     3555 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/_emerge/UseFlagDisplay.py
--rw-r--r--   0 root         (0) root         (0)     2995 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/_emerge/UserQuery.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:35.977468 portage-3.0.45.3/lib/_emerge/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1165 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/_find_deep_system_runtime_deps.py
--rw-r--r--   0 root         (0) root         (0)      442 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/_flush_elog_mod_echo.py
--rw-r--r--   0 root         (0) root         (0)   149384 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/actions.py
--rw-r--r--   0 root         (0) root         (0)     1971 2023-01-10 15:12:38.505765 portage-3.0.45.3/lib/_emerge/chk_updated_cfg_files.py
--rw-r--r--   0 root         (0) root         (0)      498 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/_emerge/clear_caches.py
--rw-r--r--   0 root         (0) root         (0)      586 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/countdown.py
--rw-r--r--   0 root         (0) root         (0)     8835 2023-02-21 07:15:01.588895 portage-3.0.45.3/lib/_emerge/create_depgraph_params.py
--rw-r--r--   0 root         (0) root         (0)     5191 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/create_world_atom.py
--rw-r--r--   0 root         (0) root         (0)   499558 2023-02-21 07:15:01.588895 portage-3.0.45.3/lib/_emerge/depgraph.py
--rw-r--r--   0 root         (0) root         (0)     1814 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/emergelog.py
--rw-r--r--   0 root         (0) root         (0)      958 2022-12-24 02:35:49.849323 portage-3.0.45.3/lib/_emerge/getloadavg.py
--rw-r--r--   0 root         (0) root         (0)     3425 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/_emerge/help.py
--rw-r--r--   0 root         (0) root         (0)      785 2023-01-10 15:12:38.509099 portage-3.0.45.3/lib/_emerge/is_valid_package_atom.py
--rw-r--r--   0 root         (0) root         (0)    42164 2023-02-21 07:15:01.595562 portage-3.0.45.3/lib/_emerge/main.py
--rw-r--r--   0 root         (0) root         (0)     5614 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/post_emerge.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/_emerge/resolver/
--rw-r--r--   0 root         (0) root         (0)     3198 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/_emerge/resolver/DbapiProvidesIndex.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:35.980801 portage-3.0.45.3/lib/_emerge/resolver/__init__.py
--rw-r--r--   0 root         (0) root         (0)    11328 2023-02-11 02:54:54.195728 portage-3.0.45.3/lib/_emerge/resolver/backtracking.py
--rw-r--r--   0 root         (0) root         (0)    11932 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/resolver/circular_dependency.py
--rw-r--r--   0 root         (0) root         (0)    39548 2023-01-10 15:14:56.986502 portage-3.0.45.3/lib/_emerge/resolver/output.py
--rw-r--r--   0 root         (0) root         (0)    20756 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/resolver/output_helpers.py
--rw-r--r--   0 root         (0) root         (0)    15636 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/resolver/package_tracker.py
--rw-r--r--   0 root         (0) root         (0)    59893 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/_emerge/resolver/slot_collision.py
--rw-r--r--   0 root         (0) root         (0)    20976 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/_emerge/search.py
--rw-r--r--   0 root         (0) root         (0)     1573 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/show_invalid_depstring_notice.py
--rw-r--r--   0 root         (0) root         (0)     3196 2023-01-10 14:04:05.121373 portage-3.0.45.3/lib/_emerge/stdout_spinner.py
--rw-r--r--   0 root         (0) root         (0)    26564 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/_emerge/unmerge.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/
--rw-r--r--   0 root         (0) root         (0)    25908 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/_compat_upgrade/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.007468 portage-3.0.45.3/lib/portage/_compat_upgrade/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1666 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/_compat_upgrade/binpkg_compression.py
--rw-r--r--   0 root         (0) root         (0)     1240 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/portage/_compat_upgrade/binpkg_multi_instance.py
--rw-r--r--   0 root         (0) root         (0)     4288 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/portage/_compat_upgrade/default_locations.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/_emirrordist/
--rw-r--r--   0 root         (0) root         (0)     5376 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/_emirrordist/Config.py
--rw-r--r--   0 root         (0) root         (0)     7223 2023-01-10 15:35:29.386865 portage-3.0.45.3/lib/portage/_emirrordist/ContentDB.py
--rw-r--r--   0 root         (0) root         (0)     4631 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/_emirrordist/DeletionIterator.py
--rw-r--r--   0 root         (0) root         (0)     5079 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/_emirrordist/DeletionTask.py
--rw-r--r--   0 root         (0) root         (0)    11176 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/_emirrordist/FetchIterator.py
--rw-r--r--   0 root         (0) root         (0)    25443 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/_emirrordist/FetchTask.py
--rw-r--r--   0 root         (0) root         (0)     9145 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/_emirrordist/MirrorDistTask.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.007468 portage-3.0.45.3/lib/portage/_emirrordist/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16081 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/_emirrordist/main.py
--rw-r--r--   0 root         (0) root         (0)    10222 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/_global_updates.py
--rw-r--r--   0 root         (0) root         (0)     2550 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/_legacy_globals.py
--rw-r--r--   0 root         (0) root         (0)     4762 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/_selinux.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/_sets/
--rw-r--r--   0 root         (0) root         (0)     1719 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/_sets/ProfilePackageSet.py
--rw-r--r--   0 root         (0) root         (0)    14268 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/_sets/__init__.py
--rw-r--r--   0 root         (0) root         (0)     8205 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/_sets/base.py
--rw-r--r--   0 root         (0) root         (0)    22035 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/_sets/dbapi.py
--rw-r--r--   0 root         (0) root         (0)    15573 2023-01-10 15:14:56.986502 portage-3.0.45.3/lib/portage/_sets/files.py
--rw-r--r--   0 root         (0) root         (0)     3603 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/_sets/libs.py
--rw-r--r--   0 root         (0) root         (0)     2406 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/portage/_sets/profiles.py
--rw-r--r--   0 root         (0) root         (0)     3535 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/portage/_sets/security.py
--rw-r--r--   0 root         (0) root         (0)     1441 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/_sets/shell.py
--rw-r--r--   0 root         (0) root         (0)     2576 2023-02-17 01:23:14.047853 portage-3.0.45.3/lib/portage/binpkg.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/binrepo/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.014134 portage-3.0.45.3/lib/portage/binrepo/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4554 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/binrepo/config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/cache/
--rw-r--r--   0 root         (0) root         (0)      101 2021-11-12 08:15:36.014134 portage-3.0.45.3/lib/portage/cache/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3167 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/anydbm.py
--rw-r--r--   0 root         (0) root         (0)     2139 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/cache/cache_errors.py
--rw-r--r--   0 root         (0) root         (0)     5226 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/ebuild_xattr.py
--rw-r--r--   0 root         (0) root         (0)     5286 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/flat_hash.py
--rw-r--r--   0 root         (0) root         (0)     3197 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/fs_template.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/cache/index/
--rw-r--r--   0 root         (0) root         (0)      562 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/index/IndexStreamIterator.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.017468 portage-3.0.45.3/lib/portage/cache/index/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1394 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/index/pkg_desc_index.py
--rw-r--r--   0 root         (0) root         (0)    11957 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/mappings.py
--rw-r--r--   0 root         (0) root         (0)     5844 2022-12-24 02:35:49.842656 portage-3.0.45.3/lib/portage/cache/metadata.py
--rw-r--r--   0 root         (0) root         (0)    11820 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/sql_template.py
--rw-r--r--   0 root         (0) root         (0)    13390 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/sqlite.py
--rw-r--r--   0 root         (0) root         (0)    13272 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/template.py
--rw-r--r--   0 root         (0) root         (0)      789 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/cache/volatile.py
--rw-r--r--   0 root         (0) root         (0)    20879 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/checksum.py
--rw-r--r--   0 root         (0) root         (0)     8879 2023-03-11 18:52:27.679427 portage-3.0.45.3/lib/portage/const.py
--rw-r--r--   0 root         (0) root         (0)    11470 2022-12-24 02:35:49.842656 portage-3.0.45.3/lib/portage/cvstree.py
--rw-r--r--   0 root         (0) root         (0)    11537 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/data.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.004075 portage-3.0.45.3/lib/portage/dbapi/
--rw-r--r--   0 root         (0) root         (0)      643 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/dbapi/DummyTree.py
--rw-r--r--   0 root         (0) root         (0)     5690 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/dbapi/IndexedPortdb.py
--rw-r--r--   0 root         (0) root         (0)     3743 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/dbapi/IndexedVardb.py
--rw-r--r--   0 root         (0) root         (0)     2991 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/dbapi/_ContentsCaseSensitivityManager.py
--rw-r--r--   0 root         (0) root         (0)    10120 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/dbapi/_MergeProcess.py
--rw-r--r--   0 root         (0) root         (0)     1511 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/dbapi/_SyncfsProcess.py
--rw-r--r--   0 root         (0) root         (0)     6019 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/dbapi/_VdbMetadataDelta.py
--rw-r--r--   0 root         (0) root         (0)    16607 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/dbapi/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2545 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/dbapi/_expand_new_virt.py
--rw-r--r--   0 root         (0) root         (0)     1685 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/dbapi/_similar_name_search.py
--rw-r--r--   0 root         (0) root         (0)    90388 2023-02-17 01:23:14.511189 portage-3.0.45.3/lib/portage/dbapi/bintree.py
--rw-r--r--   0 root         (0) root         (0)     4184 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/dbapi/cpv_expand.py
--rw-r--r--   0 root         (0) root         (0)     1889 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/dbapi/dep_expand.py
--rw-r--r--   0 root         (0) root         (0)    64264 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/dbapi/porttree.py
--rw-r--r--   0 root         (0) root         (0)   252193 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/dbapi/vartree.py
--rw-r--r--   0 root         (0) root         (0)     7587 2023-02-19 19:19:33.635235 portage-3.0.45.3/lib/portage/dbapi/virtual.py
--rw-r--r--   0 root         (0) root         (0)     4029 2023-01-10 15:12:38.505765 portage-3.0.45.3/lib/portage/debug.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/dep/
--rw-r--r--   0 root         (0) root         (0)   107693 2023-02-11 02:54:54.195728 portage-3.0.45.3/lib/portage/dep/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3780 2023-01-10 15:12:38.505765 portage-3.0.45.3/lib/portage/dep/_dnf.py
--rw-r--r--   0 root         (0) root         (0)     4396 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/dep/_slot_operator.py
--rw-r--r--   0 root         (0) root         (0)    42498 2023-01-10 15:12:38.705766 portage-3.0.45.3/lib/portage/dep/dep_check.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/dep/soname/
--rw-r--r--   0 root         (0) root         (0)     1925 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/dep/soname/SonameAtom.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.030801 portage-3.0.45.3/lib/portage/dep/soname/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5080 2023-02-15 08:38:51.725606 portage-3.0.45.3/lib/portage/dep/soname/multilib_category.py
--rw-r--r--   0 root         (0) root         (0)     1491 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/dep/soname/parse.py
--rw-r--r--   0 root         (0) root         (0)    14093 2022-12-24 02:35:49.842656 portage-3.0.45.3/lib/portage/dispatch_conf.py
--rw-r--r--   0 root         (0) root         (0)     8092 2023-01-10 15:35:29.386865 portage-3.0.45.3/lib/portage/eapi.py
--rw-r--r--   0 root         (0) root         (0)     6757 2022-09-10 09:45:01.057050 portage-3.0.45.3/lib/portage/eclass_cache.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/elog/
--rw-r--r--   0 root         (0) root         (0)     6879 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/elog/__init__.py
--rw-r--r--   0 root         (0) root         (0)      613 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/elog/filtering.py
--rw-r--r--   0 root         (0) root         (0)     6065 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/elog/messages.py
--rw-r--r--   0 root         (0) root         (0)      968 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/elog/mod_custom.py
--rw-r--r--   0 root         (0) root         (0)     2204 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/elog/mod_echo.py
--rw-r--r--   0 root         (0) root         (0)     1660 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/elog/mod_mail.py
--rw-r--r--   0 root         (0) root         (0)     3183 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/elog/mod_mail_summary.py
--rw-r--r--   0 root         (0) root         (0)     3396 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/elog/mod_save.py
--rw-r--r--   0 root         (0) root         (0)     3580 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/elog/mod_save_summary.py
--rw-r--r--   0 root         (0) root         (0)      974 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/elog/mod_syslog.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/
--rw-r--r--   0 root         (0) root         (0)      163 2021-11-12 08:15:36.037467 portage-3.0.45.3/lib/portage/emaint/__init__.py
--rw-r--r--   0 root         (0) root         (0)      762 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/defaults.py
--rw-r--r--   0 root         (0) root         (0)     8691 2023-02-15 07:52:53.745569 portage-3.0.45.3/lib/portage/emaint/main.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/
--rw-r--r--   0 root         (0) root         (0)      173 2021-11-12 08:15:36.037467 portage-3.0.45.3/lib/portage/emaint/modules/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/binhost/
--rw-r--r--   0 root         (0) root         (0)      524 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/binhost/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6358 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/emaint/modules/binhost/binhost.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/config/
--rw-r--r--   0 root         (0) root         (0)      534 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/config/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2520 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/emaint/modules/config/config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/logs/
--rw-r--r--   0 root         (0) root         (0)     1629 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/logs/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3535 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/emaint/modules/logs/logs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/merges/
--rw-r--r--   0 root         (0) root         (0)     1417 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/merges/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9834 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/emaint/modules/merges/merges.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/move/
--rw-r--r--   0 root         (0) root         (0)      851 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/move/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7693 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/emaint/modules/move/move.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/resume/
--rw-r--r--   0 root         (0) root         (0)      566 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/resume/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1900 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/emaint/modules/resume/resume.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/sync/
--rw-r--r--   0 root         (0) root         (0)     2145 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/sync/__init__.py
--rw-r--r--   0 root         (0) root         (0)    18469 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/emaint/modules/sync/sync.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/emaint/modules/world/
--rw-r--r--   0 root         (0) root         (0)      502 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/emaint/modules/world/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3109 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/emaint/modules/world/world.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/env/
--rw-r--r--   0 root         (0) root         (0)       52 2021-11-12 08:15:36.044134 portage-3.0.45.3/lib/portage/env/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3054 2022-12-24 02:35:49.842656 portage-3.0.45.3/lib/portage/env/config.py
--rw-r--r--   0 root         (0) root         (0)    10311 2022-12-24 02:35:49.842656 portage-3.0.45.3/lib/portage/env/loaders.py
--rw-r--r--   0 root         (0) root         (0)      578 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/env/validators.py
--rw-r--r--   0 root         (0) root         (0)     6616 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/exception.py
--rw-r--r--   0 root         (0) root         (0)    31465 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/getbinpkg.py
--rw-r--r--   0 root         (0) root         (0)    31099 2022-12-24 02:35:49.842656 portage-3.0.45.3/lib/portage/glsa.py
--rw-r--r--   0 root         (0) root         (0)     3637 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/gpg.py
--rw-r--r--   0 root         (0) root         (0)    80663 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/gpkg.py
--rw-r--r--   0 root         (0) root         (0)     1550 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/localization.py
--rw-r--r--   0 root         (0) root         (0)    28153 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/locks.py
--rw-r--r--   0 root         (0) root         (0)     6187 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/mail.py
--rw-r--r--   0 root         (0) root         (0)    31108 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/manifest.py
--rw-r--r--   0 root         (0) root         (0)     8221 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/metadata.py
--rw-r--r--   0 root         (0) root         (0)     8568 2022-12-24 02:35:49.842656 portage-3.0.45.3/lib/portage/module.py
--rw-r--r--   0 root         (0) root         (0)    18485 2023-03-04 02:56:34.192721 portage-3.0.45.3/lib/portage/news.py
--rw-r--r--   0 root         (0) root         (0)    29784 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/output.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/package/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.047467 portage-3.0.45.3/lib/portage/package/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/package/ebuild/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.050800 portage-3.0.45.3/lib/portage/package/ebuild/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/package/ebuild/_config/
--rw-r--r--   0 root         (0) root         (0)    13005 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/_config/KeywordsManager.py
--rw-r--r--   0 root         (0) root         (0)     9192 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/package/ebuild/_config/LicenseManager.py
--rw-r--r--   0 root         (0) root         (0)    16684 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/_config/LocationsManager.py
--rw-r--r--   0 root         (0) root         (0)    13915 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/package/ebuild/_config/MaskManager.py
--rw-r--r--   0 root         (0) root         (0)    21565 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/_config/UseManager.py
--rw-r--r--   0 root         (0) root         (0)     8443 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/package/ebuild/_config/VirtualsManager.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.050800 portage-3.0.45.3/lib/portage/package/ebuild/_config/__init__.py
--rw-r--r--   0 root         (0) root         (0)      770 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/package/ebuild/_config/env_var_validation.py
--rw-r--r--   0 root         (0) root         (0)     4694 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/package/ebuild/_config/features_set.py
--rw-r--r--   0 root         (0) root         (0)     2272 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/package/ebuild/_config/helper.py
--rw-r--r--   0 root         (0) root         (0)     9421 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/package/ebuild/_config/special_env_vars.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/package/ebuild/_ipc/
--rw-r--r--   0 root         (0) root         (0)      829 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/package/ebuild/_ipc/ExitCommand.py
--rw-r--r--   0 root         (0) root         (0)      212 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/package/ebuild/_ipc/IpcCommand.py
--rw-r--r--   0 root         (0) root         (0)     5250 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/package/ebuild/_ipc/QueryCommand.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.054134 portage-3.0.45.3/lib/portage/package/ebuild/_ipc/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1405 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/package/ebuild/_metadata_invalid.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/
--rw-r--r--   0 root         (0) root         (0)     1413 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/ManifestProcess.py
--rw-r--r--   0 root         (0) root         (0)     3767 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/ManifestScheduler.py
--rw-r--r--   0 root         (0) root         (0)     7859 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/ManifestTask.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.057467 portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4987 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/package/ebuild/_spawn_nofetch.py
--rw-r--r--   0 root         (0) root         (0)   133992 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/config.py
--rw-r--r--   0 root         (0) root         (0)     4195 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/deprecated_profile_check.py
--rw-r--r--   0 root         (0) root         (0)     6732 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/digestcheck.py
--rw-r--r--   0 root         (0) root         (0)     9424 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/package/ebuild/digestgen.py
--rw-r--r--   0 root         (0) root         (0)   111662 2023-03-11 18:52:27.679427 portage-3.0.45.3/lib/portage/package/ebuild/doebuild.py
--rw-r--r--   0 root         (0) root         (0)    79658 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/package/ebuild/fetch.py
--rw-r--r--   0 root         (0) root         (0)     4689 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/package/ebuild/getmaskingreason.py
--rw-r--r--   0 root         (0) root         (0)     6556 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/package/ebuild/getmaskingstatus.py
--rw-r--r--   0 root         (0) root         (0)    19287 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/package/ebuild/prepare_build_dirs.py
--rw-r--r--   0 root         (0) root         (0)     1004 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/package/ebuild/profile_iuse.py
--rw-r--r--   0 root         (0) root         (0)    41702 2023-03-11 18:52:27.679427 portage-3.0.45.3/lib/portage/process.py
--rw-r--r--   0 root         (0) root         (0)     1573 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/progress.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/proxy/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.060800 portage-3.0.45.3/lib/portage/proxy/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7832 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/proxy/lazyimport.py
--rw-r--r--   0 root         (0) root         (0)     2857 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/proxy/objectproxy.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/repository/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.064134 portage-3.0.45.3/lib/portage/repository/__init__.py
--rw-r--r--   0 root         (0) root         (0)    62136 2023-03-19 19:13:51.046073 portage-3.0.45.3/lib/portage/repository/config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/repository/storage/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.064134 portage-3.0.45.3/lib/portage/repository/storage/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3951 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/repository/storage/hardlink_quarantine.py
--rw-r--r--   0 root         (0) root         (0)    10940 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/repository/storage/hardlink_rcu.py
--rw-r--r--   0 root         (0) root         (0)     1153 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/repository/storage/inplace.py
--rw-r--r--   0 root         (0) root         (0)     2675 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/repository/storage/interface.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/sync/
--rw-r--r--   0 root         (0) root         (0)     1589 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/sync/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3015 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/sync/config_checks.py
--rw-r--r--   0 root         (0) root         (0)    14745 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/sync/controller.py
--rw-r--r--   0 root         (0) root         (0)      696 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/sync/getaddrinfo_validate.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/sync/modules/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.067467 portage-3.0.45.3/lib/portage/sync/modules/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/sync/modules/cvs/
--rw-r--r--   0 root         (0) root         (0)     1650 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/sync/modules/cvs/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2339 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/modules/cvs/cvs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/sync/modules/git/
--rw-r--r--   0 root         (0) root         (0)     2722 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/modules/git/__init__.py
--rw-r--r--   0 root         (0) root         (0)    20049 2023-02-27 06:15:41.194157 portage-3.0.45.3/lib/portage/sync/modules/git/git.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/sync/modules/mercurial/
--rw-r--r--   0 root         (0) root         (0)     1403 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/sync/modules/mercurial/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6125 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/modules/mercurial/mercurial.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.007408 portage-3.0.45.3/lib/portage/sync/modules/rsync/
--rw-r--r--   0 root         (0) root         (0)     1287 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/sync/modules/rsync/__init__.py
--rw-r--r--   0 root         (0) root         (0)    33953 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/modules/rsync/rsync.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/sync/modules/svn/
--rw-r--r--   0 root         (0) root         (0)     1037 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/sync/modules/svn/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2759 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/modules/svn/svn.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/sync/modules/webrsync/
--rw-r--r--   0 root         (0) root         (0)     1648 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/sync/modules/webrsync/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5092 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/modules/webrsync/webrsync.py
--rw-r--r--   0 root         (0) root         (0)     2485 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/old_tree_timestamp.py
--rw-r--r--   0 root         (0) root         (0)    13139 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/sync/syncbase.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/.gnupg/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/.gnupg/openpgp-revocs.d/
--rw-r--r--   0 root         (0) root         (0)     1850 2022-09-10 09:45:01.063717 portage-3.0.45.3/lib/portage/tests/.gnupg/openpgp-revocs.d/06B3A311BD775C280D22A9305D90EA06352177F6.rev
--rw-r--r--   0 root         (0) root         (0)     1852 2022-09-10 09:45:01.063717 portage-3.0.45.3/lib/portage/tests/.gnupg/openpgp-revocs.d/8DEDA2CDED49C8809287B89D8812797DDF1DD192.rev
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/.gnupg/private-keys-v1.d/
--rw-r--r--   0 root         (0) root         (0)     2055 2022-09-10 09:45:01.057050 portage-3.0.45.3/lib/portage/tests/.gnupg/private-keys-v1.d/273B030399E7BEA66A9AD42216DE7CA17BA5D42E.key
--rw-r--r--   0 root         (0) root         (0)     2055 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/tests/.gnupg/private-keys-v1.d/C99796FB85B0C3DF03314A11B5850C51167D6282.key
--rw-r--r--   0 root         (0) root         (0)     2774 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/tests/.gnupg/pubring.kbx
--rw-r--r--   0 root         (0) root         (0)     1360 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/tests/.gnupg/trustdb.gpg
--rw-r--r--   0 root         (0) root         (0)    11861 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/bin/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.074133 portage-3.0.45.3/lib/portage/tests/bin/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.074133 portage-3.0.45.3/lib/portage/tests/bin/__test__.py
--rw-r--r--   0 root         (0) root         (0)     2658 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/bin/setup_env.py
--rw-r--r--   0 root         (0) root         (0)      547 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/bin/test_dobin.py
--rw-r--r--   0 root         (0) root         (0)      565 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/bin/test_dodir.py
--rw-r--r--   0 root         (0) root         (0)    13013 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/bin/test_doins.py
--rw-r--r--   0 root         (0) root         (0)     9192 2023-01-10 15:14:56.993169 portage-3.0.45.3/lib/portage/tests/bin/test_eapi7_ver_funcs.py
--rw-r--r--   0 root         (0) root         (0)     3075 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/bin/test_filter_bash_env.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/dbapi/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.074133 portage-3.0.45.3/lib/portage/tests/dbapi/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.074133 portage-3.0.45.3/lib/portage/tests/dbapi/__test__.py
--rw-r--r--   0 root         (0) root         (0)     3673 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/dbapi/test_auxdb.py
--rw-r--r--   0 root         (0) root         (0)     6521 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/tests/dbapi/test_bintree.py
--rw-r--r--   0 root         (0) root         (0)     3973 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/portage/tests/dbapi/test_fakedbapi.py
--rw-r--r--   0 root         (0) root         (0)     9409 2023-02-19 19:19:44.225293 portage-3.0.45.3/lib/portage/tests/dbapi/test_portdb_cache.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/dep/
--rw-r--r--   0 root         (0) root         (0)      169 2021-11-12 08:15:36.077467 portage-3.0.45.3/lib/portage/tests/dep/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.077467 portage-3.0.45.3/lib/portage/tests/dep/__test__.py
--rw-r--r--   0 root         (0) root         (0)    24520 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/testAtom.py
--rw-r--r--   0 root         (0) root         (0)     9752 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/dep/testCheckRequiredUse.py
--rw-r--r--   0 root         (0) root         (0)      779 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/dep/testExtendedAtomDict.py
--rw-r--r--   0 root         (0) root         (0)     3769 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/dep/testExtractAffectingUSE.py
--rw-r--r--   0 root         (0) root         (0)     1652 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/testStandalone.py
--rw-r--r--   0 root         (0) root         (0)     4452 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/dep/test_best_match_to_list.py
--rw-r--r--   0 root         (0) root         (0)     1149 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_dep_getcpv.py
--rw-r--r--   0 root         (0) root         (0)      988 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_dep_getrepo.py
--rw-r--r--   0 root         (0) root         (0)      934 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_dep_getslot.py
--rw-r--r--   0 root         (0) root         (0)     1402 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_dep_getusedeps.py
--rw-r--r--   0 root         (0) root         (0)     2077 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_dnf_convert.py
--rw-r--r--   0 root         (0) root         (0)     1237 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_get_operator.py
--rw-r--r--   0 root         (0) root         (0)     1778 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/dep/test_get_required_use_flags.py
--rw-r--r--   0 root         (0) root         (0)     1009 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_isjustname.py
--rw-r--r--   0 root         (0) root         (0)    11660 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_isvalidatom.py
--rw-r--r--   0 root         (0) root         (0)    11132 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/dep/test_match_from_list.py
--rw-r--r--   0 root         (0) root         (0)     1572 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_overlap_dnf.py
--rw-r--r--   0 root         (0) root         (0)     2661 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_paren_reduce.py
--rw-r--r--   0 root         (0) root         (0)      790 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_soname_atom_pickle.py
--rw-r--r--   0 root         (0) root         (0)    27656 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/dep/test_use_reduce.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/ebuild/
--rw-r--r--   0 root         (0) root         (0)      107 2021-11-12 08:15:36.080800 portage-3.0.45.3/lib/portage/tests/ebuild/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.080800 portage-3.0.45.3/lib/portage/tests/ebuild/__test__.py
--rw-r--r--   0 root         (0) root         (0)     1387 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/ebuild/test_array_fromfile_eof.py
--rw-r--r--   0 root         (0) root         (0)    14001 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/ebuild/test_config.py
--rw-r--r--   0 root         (0) root         (0)     5947 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/ebuild/test_doebuild_fd_pipes.py
--rw-r--r--   0 root         (0) root         (0)     5167 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/ebuild/test_doebuild_spawn.py
--rw-r--r--   0 root         (0) root         (0)    35283 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/ebuild/test_fetch.py
--rw-r--r--   0 root         (0) root         (0)     6852 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/ebuild/test_ipc_daemon.py
--rw-r--r--   0 root         (0) root         (0)     5211 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/ebuild/test_shell_quote.py
--rw-r--r--   0 root         (0) root         (0)     1919 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/ebuild/test_spawn.py
--rw-r--r--   0 root         (0) root         (0)     4479 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/ebuild/test_use_expand_incremental.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/emerge/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.080800 portage-3.0.45.3/lib/portage/tests/emerge/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.080800 portage-3.0.45.3/lib/portage/tests/emerge/__test__.py
--rw-r--r--   0 root         (0) root         (0)     1877 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/emerge/test_actions.py
--rw-r--r--   0 root         (0) root         (0)    10290 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/emerge/test_config_protect.py
--rw-r--r--   0 root         (0) root         (0)     6335 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/emerge/test_emerge_blocker_file_collision.py
--rw-r--r--   0 root         (0) root         (0)     6615 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/emerge/test_emerge_slot_abi.py
--rw-r--r--   0 root         (0) root         (0)     1320 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/emerge/test_global_updates.py
--rw-r--r--   0 root         (0) root         (0)    26423 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/emerge/test_simple.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/env/
--rw-r--r--   0 root         (0) root         (0)      169 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/env/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/env/__test__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/env/config/
--rw-r--r--   0 root         (0) root         (0)      176 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/env/config/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/env/config/__test__.py
--rw-r--r--   0 root         (0) root         (0)     1164 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/env/config/test_PackageKeywordsFile.py
--rw-r--r--   0 root         (0) root         (0)      818 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/env/config/test_PackageMaskFile.py
--rw-r--r--   0 root         (0) root         (0)     1077 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/env/config/test_PackageUseFile.py
--rw-r--r--   0 root         (0) root         (0)     1128 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/env/config/test_PortageModulesFile.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/glsa/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/glsa/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/glsa/__test__.py
--rw-r--r--   0 root         (0) root         (0)     7173 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/glsa/test_security_set.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/gpkg/
--rw-r--r--   0 root         (0) root         (0)      102 2022-09-10 09:45:01.057050 portage-3.0.45.3/lib/portage/tests/gpkg/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2022-09-10 09:45:01.057050 portage-3.0.45.3/lib/portage/tests/gpkg/__test__.py
--rw-r--r--   0 root         (0) root         (0)    13833 2022-09-20 03:21:13.396002 portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_checksum.py
--rw-r--r--   0 root         (0) root         (0)    15728 2022-09-20 03:21:13.396002 portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_gpg.py
--rw-r--r--   0 root         (0) root         (0)     1899 2022-09-20 03:21:13.396002 portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_metadata_update.py
--rw-r--r--   0 root         (0) root         (0)     5288 2022-09-20 03:21:13.396002 portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_metadata_url.py
--rw-r--r--   0 root         (0) root         (0)    14745 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_path.py
--rw-r--r--   0 root         (0) root         (0)     1868 2022-09-20 03:21:13.396002 portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_size.py
--rw-r--r--   0 root         (0) root         (0)     3305 2022-09-20 03:21:13.396002 portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_stream.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/lafilefixer/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/lafilefixer/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/lafilefixer/__test__.py
--rw-r--r--   0 root         (0) root         (0)     6338 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/lafilefixer/test_lafilefixer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.010742 portage-3.0.45.3/lib/portage/tests/lazyimport/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/lazyimport/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.45.3/lib/portage/tests/lazyimport/__test__.py
--rw-r--r--   0 root         (0) root         (0)     2824 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/lazyimport/test_lazy_import_portage_baseline.py
--rw-r--r--   0 root         (0) root         (0)      596 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/lazyimport/test_preload_portage_submodules.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.014075 portage-3.0.45.3/lib/portage/tests/lint/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/lint/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/lint/__test__.py
--rw-r--r--   0 root         (0) root         (0)      214 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/lint/metadata.py
--rw-r--r--   0 root         (0) root         (0)     2345 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/lint/test_bash_syntax.py
--rw-r--r--   0 root         (0) root         (0)     3031 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/lint/test_compile_modules.py
--rw-r--r--   0 root         (0) root         (0)     1516 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/lint/test_import_modules.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.014075 portage-3.0.45.3/lib/portage/tests/locks/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/locks/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/locks/__test__.py
--rw-r--r--   0 root         (0) root         (0)     7850 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/locks/test_asynchronous_lock.py
--rw-r--r--   0 root         (0) root         (0)     2763 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/locks/test_lock_nonblock.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.014075 portage-3.0.45.3/lib/portage/tests/news/
--rw-r--r--   0 root         (0) root         (0)      170 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/news/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/news/__test__.py
--rw-r--r--   0 root         (0) root         (0)    14363 2023-02-19 19:19:33.635235 portage-3.0.45.3/lib/portage/tests/news/test_NewsItem.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.014075 portage-3.0.45.3/lib/portage/tests/process/
--rw-r--r--   0 root         (0) root         (0)      107 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/process/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.45.3/lib/portage/tests/process/__test__.py
--rw-r--r--   0 root         (0) root         (0)     2016 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/process/test_AsyncFunction.py
--rw-r--r--   0 root         (0) root         (0)     2332 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/process/test_PipeLogger.py
--rw-r--r--   0 root         (0) root         (0)     3121 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/process/test_PopenProcess.py
--rw-r--r--   0 root         (0) root         (0)     2366 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/process/test_PopenProcessBlockingIO.py
--rw-r--r--   0 root         (0) root         (0)     3737 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/process/test_poll.py
--rw-r--r--   0 root         (0) root         (0)     1137 2023-01-25 07:48:52.584676 portage-3.0.45.3/lib/portage/tests/process/test_spawn_fail_e2big.py
--rw-r--r--   0 root         (0) root         (0)     1341 2023-03-11 18:52:27.682760 portage-3.0.45.3/lib/portage/tests/process/test_spawn_warn_large_env.py
--rw-r--r--   0 root         (0) root         (0)     1178 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/process/test_unshare_net.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/resolver/
--rw-r--r--   0 root         (0) root         (0)    42492 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/ResolverPlayground.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.104133 portage-3.0.45.3/lib/portage/tests/resolver/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.104133 portage-3.0.45.3/lib/portage/tests/resolver/__test__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/resolver/binpkg_multi_instance/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.104133 portage-3.0.45.3/lib/portage/tests/resolver/binpkg_multi_instance/__init__.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.104133 portage-3.0.45.3/lib/portage/tests/resolver/binpkg_multi_instance/__test__.py
--rw-r--r--   0 root         (0) root         (0)     5585 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/binpkg_multi_instance/test_build_id_profile_format.py
--rw-r--r--   0 root         (0) root         (0)     3747 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/binpkg_multi_instance/test_rebuilt_binaries.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/resolver/soname/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/resolver/soname/__init__.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/resolver/soname/__test__.py
--rw-r--r--   0 root         (0) root         (0)     3931 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_autounmask.py
--rw-r--r--   0 root         (0) root         (0)     1755 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_depclean.py
--rw-r--r--   0 root         (0) root         (0)     8528 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_downgrade.py
--rw-r--r--   0 root         (0) root         (0)     3840 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_or_choices.py
--rw-r--r--   0 root         (0) root         (0)     3305 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_reinstall.py
--rw-r--r--   0 root         (0) root         (0)     3338 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_skip_update.py
--rw-r--r--   0 root         (0) root         (0)    12877 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_slot_conflict_reinstall.py
--rw-r--r--   0 root         (0) root         (0)     3971 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_slot_conflict_update.py
--rw-r--r--   0 root         (0) root         (0)     2944 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_soname_provided.py
--rw-r--r--   0 root         (0) root         (0)     2778 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_unsatisfiable.py
--rw-r--r--   0 root         (0) root         (0)     3354 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/soname/test_unsatisfied.py
--rw-r--r--   0 root         (0) root         (0)     2824 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_aggressive_backtrack_downgrade.py
--rw-r--r--   0 root         (0) root         (0)    28432 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask.py
--rw-r--r--   0 root         (0) root         (0)     2732 2023-01-10 15:12:38.505765 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_binpkg_use.py
--rw-r--r--   0 root         (0) root         (0)     2176 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_keep_keywords.py
--rw-r--r--   0 root         (0) root         (0)     3098 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_multilib_use.py
--rw-r--r--   0 root         (0) root         (0)     1279 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_parent.py
--rw-r--r--   0 root         (0) root         (0)     2573 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_use_backtrack.py
--rw-r--r--   0 root         (0) root         (0)     3743 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_use_breakage.py
--rw-r--r--   0 root         (0) root         (0)     1830 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_use_slot_conflict.py
--rw-r--r--   0 root         (0) root         (0)     5786 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/resolver/test_backtracking.py
--rw-r--r--   0 root         (0) root         (0)     6805 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_bdeps.py
--rw-r--r--   0 root         (0) root         (0)     4927 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_binary_pkg_ebuild_visibility.py
--rw-r--r--   0 root         (0) root         (0)     4231 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/resolver/test_blocker.py
--rw-r--r--   0 root         (0) root         (0)     4330 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_changed_deps.py
--rw-r--r--   0 root         (0) root         (0)     7899 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_circular_choices.py
--rw-r--r--   0 root         (0) root         (0)     3341 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_circular_choices_rust.py
--rw-r--r--   0 root         (0) root         (0)     4832 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_circular_dependencies.py
--rw-r--r--   0 root         (0) root         (0)     4948 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_complete_graph.py
--rw-r--r--   0 root         (0) root         (0)     2910 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_complete_if_new_subslot_without_revbump.py
--rw-r--r--   0 root         (0) root         (0)     9959 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_depclean.py
--rw-r--r--   0 root         (0) root         (0)     1690 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_depclean_order.py
--rw-r--r--   0 root         (0) root         (0)     2443 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_depclean_slot_unavailable.py
--rw-r--r--   0 root         (0) root         (0)    13128 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_depth.py
--rw-r--r--   0 root         (0) root         (0)     3329 2023-01-10 15:12:38.505765 portage-3.0.45.3/lib/portage/tests/resolver/test_disjunctive_depend_order.py
--rw-r--r--   0 root         (0) root         (0)     9983 2023-02-19 19:19:44.381961 portage-3.0.45.3/lib/portage/tests/resolver/test_eapi.py
--rw-r--r--   0 root         (0) root         (0)     2658 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_features_test_use.py
--rw-r--r--   0 root         (0) root         (0)     3379 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_imagemagick_graphicsmagick.py
--rw-r--r--   0 root         (0) root         (0)     3457 2022-09-10 09:45:01.057050 portage-3.0.45.3/lib/portage/tests/resolver/test_installkernel.py
--rw-r--r--   0 root         (0) root         (0)    11063 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_keywords.py
--rw-r--r--   0 root         (0) root         (0)    31088 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_merge_order.py
--rw-r--r--   0 root         (0) root         (0)     1234 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_missing_iuse_and_evaluated_atoms.py
--rw-r--r--   0 root         (0) root         (0)    15920 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/portage/tests/resolver/test_multirepo.py
--rw-r--r--   0 root         (0) root         (0)     1772 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/resolver/test_multislot.py
--rw-r--r--   0 root         (0) root         (0)     1554 2022-09-10 09:44:56.963689 portage-3.0.45.3/lib/portage/tests/resolver/test_old_dep_chain_display.py
--rw-r--r--   0 root         (0) root         (0)     1142 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps.py
--rw-r--r--   0 root         (0) root         (0)     1527 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps_circular.py
--rw-r--r--   0 root         (0) root         (0)     5933 2023-02-17 05:49:01.495487 portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps_ideps.py
--rw-r--r--   0 root         (0) root         (0)     2552 2023-02-17 05:49:01.495487 portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps_minimal.py
--rw-r--r--   0 root         (0) root         (0)    25072 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_or_choices.py
--rw-r--r--   0 root         (0) root         (0)     2716 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_or_downgrade_installed.py
--rw-r--r--   0 root         (0) root         (0)     6850 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_or_upgrade_installed.py
--rw-r--r--   0 root         (0) root         (0)     3911 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_output.py
--rw-r--r--   0 root         (0) root         (0)     9049 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_package_tracker.py
--rw-r--r--   0 root         (0) root         (0)     4568 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_profile_default_eapi.py
--rw-r--r--   0 root         (0) root         (0)     3353 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_profile_package_set.py
--rw-r--r--   0 root         (0) root         (0)     6911 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_rebuild.py
--rw-r--r--   0 root         (0) root         (0)     2409 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_regular_slot_change_without_revbump.py
--rw-r--r--   0 root         (0) root         (0)    11792 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_required_use.py
--rw-r--r--   0 root         (0) root         (0)     2640 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_runtime_cycle_merge_order.py
--rw-r--r--   0 root         (0) root         (0)     3500 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/resolver/test_simple.py
--rw-r--r--   0 root         (0) root         (0)    18128 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_abi.py
--rw-r--r--   0 root         (0) root         (0)     8790 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_abi_downgrade.py
--rw-r--r--   0 root         (0) root         (0)     3488 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_change_without_revbump.py
--rw-r--r--   0 root         (0) root         (0)    13393 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_collisions.py
--rw-r--r--   0 root         (0) root         (0)     1990 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_force_rebuild.py
--rw-r--r--   0 root         (0) root         (0)     1432 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_mask_update.py
--rw-r--r--   0 root         (0) root         (0)    14826 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_rebuild.py
--rw-r--r--   0 root         (0) root         (0)     7910 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_unsatisfied_deep_deps.py
--rw-r--r--   0 root         (0) root         (0)     2579 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_update.py
--rw-r--r--   0 root         (0) root         (0)     2491 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_update_virt.py
--rw-r--r--   0 root         (0) root         (0)     5024 2023-01-10 15:12:38.499099 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_autounmask.py
--rw-r--r--   0 root         (0) root         (0)     7642 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_bdeps.py
--rw-r--r--   0 root         (0) root         (0)     4350 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_complete_graph.py
--rw-r--r--   0 root         (0) root         (0)     4694 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_exclusive_slots.py
--rw-r--r--   0 root         (0) root         (0)     4366 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_missed_update.py
--rw-r--r--   0 root         (0) root         (0)     3719 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_rebuild.py
--rw-r--r--   0 root         (0) root         (0)     1682 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_required_use.py
--rw-r--r--   0 root         (0) root         (0)     9190 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_reverse_deps.py
--rw-r--r--   0 root         (0) root         (0)     3974 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_runtime_pkg_mask.py
--rw-r--r--   0 root         (0) root         (0)     2103 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_unsatisfied.py
--rw-r--r--   0 root         (0) root         (0)     3518 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_unsolved.py
--rw-r--r--   0 root         (0) root         (0)     2107 2023-02-03 17:42:31.192513 portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_update_probe_parent_downgrade.py
--rw-r--r--   0 root         (0) root         (0)     1819 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_solve_non_slot_operator_slot_conflicts.py
--rw-r--r--   0 root         (0) root         (0)     3584 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/tests/resolver/test_targetroot.py
--rw-r--r--   0 root         (0) root         (0)     1571 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/tests/resolver/test_unecessary_slot_upgrade.py
--rw-r--r--   0 root         (0) root         (0)    11321 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/tests/resolver/test_unmerge_order.py
--rw-r--r--   0 root         (0) root         (0)     3843 2023-02-21 07:15:01.595562 portage-3.0.45.3/lib/portage/tests/resolver/test_update.py
--rw-r--r--   0 root         (0) root         (0)     1827 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_use_dep_defaults.py
--rw-r--r--   0 root         (0) root         (0)     5326 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/resolver/test_useflags.py
--rw-r--r--   0 root         (0) root         (0)     9976 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_virtual_minimize_children.py
--rw-r--r--   0 root         (0) root         (0)     9326 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/resolver/test_virtual_slot.py
--rw-r--r--   0 root         (0) root         (0)     2910 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/resolver/test_with_test_deps.py
--rwxr-xr-x   0 root         (0) root         (0)     2111 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/runTests.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/sets/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/__test__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/sets/base/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/base/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/base/__test__.py
--rw-r--r--   0 root         (0) root         (0)     2051 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/sets/base/testInternalPackageSet.py
--rw-r--r--   0 root         (0) root         (0)     1029 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/sets/base/testVariableSet.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/sets/files/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/files/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/files/__test__.py
--rw-r--r--   0 root         (0) root         (0)      992 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/sets/files/testConfigFileSet.py
--rw-r--r--   0 root         (0) root         (0)      829 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/sets/files/testStaticFileSet.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/sets/shell/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/shell/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sets/shell/__test__.py
--rw-r--r--   0 root         (0) root         (0)      790 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/sets/shell/testShell.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/sync/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sync/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/sync/__test__.py
--rw-r--r--   0 root         (0) root         (0)    16481 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/sync/test_sync_local.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/unicode/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/unicode/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.45.3/lib/portage/tests/unicode/__test__.py
--rw-r--r--   0 root         (0) root         (0)     2294 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/unicode/test_string_format.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/update/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.110799 portage-3.0.45.3/lib/portage/tests/update/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.110799 portage-3.0.45.3/lib/portage/tests/update/__test__.py
--rw-r--r--   0 root         (0) root         (0)     4462 2023-02-17 01:23:14.514522 portage-3.0.45.3/lib/portage/tests/update/test_move_ent.py
--rw-r--r--   0 root         (0) root         (0)     5444 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/update/test_move_slot_ent.py
--rw-r--r--   0 root         (0) root         (0)    11460 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/update/test_update_dbentry.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/util/
--rw-r--r--   0 root         (0) root         (0)      170 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/__test__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/util/dyn_libs/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/dyn_libs/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/dyn_libs/__test__.py
--rw-r--r--   0 root         (0) root         (0)     1389 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/util/dyn_libs/test_soname_deps.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/util/eventloop/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/eventloop/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/eventloop/__test__.py
--rw-r--r--   0 root         (0) root         (0)      826 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/eventloop/test_call_soon_fifo.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/util/file_copy/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/file_copy/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/file_copy/__test__.py
--rw-r--r--   0 root         (0) root         (0)     2169 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/file_copy/test_copyfile.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/util/futures/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/futures/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.45.3/lib/portage/tests/util/futures/__test__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.017408 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/__test__.py
--rw-r--r--   0 root         (0) root         (0)     1789 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_child_watcher.py
--rw-r--r--   0 root         (0) root         (0)     2025 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_event_loop_in_fork.py
--rw-r--r--   0 root         (0) root         (0)     5394 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_pipe_closed.py
--rw-r--r--   0 root         (0) root         (0)      795 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_policy_wrapper_recursion.py
--rw-r--r--   0 root         (0) root         (0)     1394 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_run_until_complete.py
--rw-r--r--   0 root         (0) root         (0)     6912 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_subprocess_exec.py
--rw-r--r--   0 root         (0) root         (0)     2344 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_wakeup_fd_sigchld.py
--rw-r--r--   0 root         (0) root         (0)     7135 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/futures/test_compat_coroutine.py
--rw-r--r--   0 root         (0) root         (0)     1274 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/futures/test_done_callback.py
--rw-r--r--   0 root         (0) root         (0)     1565 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/util/futures/test_done_callback_after_exit.py
--rw-r--r--   0 root         (0) root         (0)     2883 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/futures/test_iter_completed.py
--rw-r--r--   0 root         (0) root         (0)    10828 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/util/futures/test_retry.py
--rw-r--r--   0 root         (0) root         (0)     6953 2022-09-20 03:21:13.396002 portage-3.0.45.3/lib/portage/tests/util/test_checksum.py
--rw-r--r--   0 root         (0) root         (0)    11345 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/util/test_digraph.py
--rw-r--r--   0 root         (0) root         (0)     1824 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/test_file_copier.py
--rw-r--r--   0 root         (0) root         (0)     3534 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/util/test_getconfig.py
--rw-r--r--   0 root         (0) root         (0)      315 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/util/test_grabdict.py
--rw-r--r--   0 root         (0) root         (0)     5805 2023-01-10 15:14:56.993169 portage-3.0.45.3/lib/portage/tests/util/test_install_mask.py
--rw-r--r--   0 root         (0) root         (0)     1120 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/tests/util/test_manifest.py
--rw-r--r--   0 root         (0) root         (0)    10489 2022-09-10 09:45:01.057050 portage-3.0.45.3/lib/portage/tests/util/test_mtimedb.py
--rw-r--r--   0 root         (0) root         (0)      440 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/test_normalizedPath.py
--rw-r--r--   0 root         (0) root         (0)     1776 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/test_shelve.py
--rw-r--r--   0 root         (0) root         (0)     6638 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/test_socks5.py
--rw-r--r--   0 root         (0) root         (0)      832 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/util/test_stackDictList.py
--rw-r--r--   0 root         (0) root         (0)     1185 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/test_stackDicts.py
--rw-r--r--   0 root         (0) root         (0)      715 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/test_stackLists.py
--rw-r--r--   0 root         (0) root         (0)      897 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/tests/util/test_uniqueArray.py
--rw-r--r--   0 root         (0) root         (0)     3347 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/util/test_varExpand.py
--rw-r--r--   0 root         (0) root         (0)     1450 2022-12-31 14:17:30.306859 portage-3.0.45.3/lib/portage/tests/util/test_whirlpool.py
--rw-r--r--   0 root         (0) root         (0)     6243 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/tests/util/test_xattr.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/tests/versions/
--rw-r--r--   0 root         (0) root         (0)      174 2021-11-12 08:15:36.117466 portage-3.0.45.3/lib/portage/tests/versions/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.45.3/lib/portage/tests/versions/__test__.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/versions/test_cpv_sort_key.py
--rw-r--r--   0 root         (0) root         (0)     3026 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/versions/test_vercmp.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/tests/xpak/
--rw-r--r--   0 root         (0) root         (0)      169 2021-11-12 08:15:36.117466 portage-3.0.45.3/lib/portage/tests/xpak/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.45.3/lib/portage/tests/xpak/__test__.py
--rw-r--r--   0 root         (0) root         (0)      427 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/tests/xpak/test_decodeint.py
--rw-r--r--   0 root         (0) root         (0)    17014 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/update.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/
--rw-r--r--   0 root         (0) root         (0)     3063 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/ExtractKernelVersion.py
--rw-r--r--   0 root         (0) root         (0)     2141 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/SlotObject.py
--rw-r--r--   0 root         (0) root         (0)    68321 2023-03-04 02:56:34.192721 portage-3.0.45.3/lib/portage/util/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/_async/
--rw-r--r--   0 root         (0) root         (0)     2609 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/_async/AsyncFunction.py
--rw-r--r--   0 root         (0) root         (0)     3393 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/_async/AsyncScheduler.py
--rw-r--r--   0 root         (0) root         (0)      963 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/_async/AsyncTaskFuture.py
--rw-r--r--   0 root         (0) root         (0)     4785 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/_async/BuildLogger.py
--rw-r--r--   0 root         (0) root         (0)     1103 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/_async/FileCopier.py
--rw-r--r--   0 root         (0) root         (0)     2486 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_async/FileDigester.py
--rw-r--r--   0 root         (0) root         (0)     5953 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_async/ForkProcess.py
--rw-r--r--   0 root         (0) root         (0)     7527 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_async/PipeLogger.py
--rw-r--r--   0 root         (0) root         (0)     2676 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/_async/PipeReaderBlockingIO.py
--rw-r--r--   0 root         (0) root         (0)     1076 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_async/PopenProcess.py
--rw-r--r--   0 root         (0) root         (0)     4501 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_async/SchedulerInterface.py
--rw-r--r--   0 root         (0) root         (0)      644 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/_async/TaskScheduler.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.127466 portage-3.0.45.3/lib/portage/util/_async/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1360 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/_async/run_main_scheduler.py
--rw-r--r--   0 root         (0) root         (0)     4347 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/_compare_files.py
--rw-r--r--   0 root         (0) root         (0)     1219 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/_ctypes.py
--rw-r--r--   0 root         (0) root         (0)     2654 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/_desktop_entry.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/_dyn_libs/
--rw-r--r--   0 root         (0) root         (0)    41425 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_dyn_libs/LinkageMapELF.py
--rw-r--r--   0 root         (0) root         (0)     2877 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/_dyn_libs/NeededEntry.py
--rw-r--r--   0 root         (0) root         (0)     9385 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/util/_dyn_libs/PreservedLibsRegistry.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.130799 portage-3.0.45.3/lib/portage/util/_dyn_libs/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3834 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/util/_dyn_libs/display_preserved_libs.py
--rw-r--r--   0 root         (0) root         (0)     1070 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/_dyn_libs/dyn_libs.py
--rw-r--r--   0 root         (0) root         (0)     6203 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/_dyn_libs/soname_deps.py
--rw-r--r--   0 root         (0) root         (0)     3722 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/_dyn_libs/soname_deps_qa.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/_eventloop/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.134132 portage-3.0.45.3/lib/portage/util/_eventloop/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5849 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/_eventloop/asyncio_event_loop.py
--rw-r--r--   0 root         (0) root         (0)      213 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/_eventloop/global_event_loop.py
--rw-r--r--   0 root         (0) root         (0)     3029 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_get_vm_info.py
--rw-r--r--   0 root         (0) root         (0)     5956 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/_info_files.py
--rw-r--r--   0 root         (0) root         (0)      692 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/_path.py
--rw-r--r--   0 root         (0) root         (0)     2530 2023-01-10 15:12:38.505765 portage-3.0.45.3/lib/portage/util/_pty.py
--rw-r--r--   0 root         (0) root         (0)     4032 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/util/_urlopen.py
--rw-r--r--   0 root         (0) root         (0)     7063 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/_xattr.py
--rw-r--r--   0 root         (0) root         (0)     1528 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/backoff.py
--rw-r--r--   0 root         (0) root         (0)     1133 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/bin_entry_point.py
--rw-r--r--   0 root         (0) root         (0)     2189 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/changelog.py
--rw-r--r--   0 root         (0) root         (0)     3464 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/compression_probe.py
--rw-r--r--   0 root         (0) root         (0)     2403 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/configparser.py
--rw-r--r--   0 root         (0) root         (0)     2180 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/cpuinfo.py
--rw-r--r--   0 root         (0) root         (0)    12975 2023-01-10 15:14:56.993169 portage-3.0.45.3/lib/portage/util/digraph.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/elf/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.137466 portage-3.0.45.3/lib/portage/util/elf/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1345 2023-02-15 08:38:51.725606 portage-3.0.45.3/lib/portage/util/elf/constants.py
--rw-r--r--   0 root         (0) root         (0)     1889 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/elf/header.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/endian/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.137466 portage-3.0.45.3/lib/portage/util/endian/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1303 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/endian/decode.py
--rw-r--r--   0 root         (0) root         (0)    15592 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/util/env_update.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/file_copy/
--rw-r--r--   0 root         (0) root         (0)      909 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/file_copy/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2118 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/formatter.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/futures/
--rw-r--r--   0 root         (0) root         (0)      180 2022-09-10 09:44:56.967023 portage-3.0.45.3/lib/portage/util/futures/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/futures/_asyncio/
--rw-r--r--   0 root         (0) root         (0)     9758 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/futures/_asyncio/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3016 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/futures/_asyncio/streams.py
--rw-r--r--   0 root         (0) root         (0)     1854 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/futures/_sync_decorator.py
--rw-r--r--   0 root         (0) root         (0)     4942 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/futures/compat_coroutine.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/futures/executor/
--rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.140799 portage-3.0.45.3/lib/portage/util/futures/executor/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4306 2023-01-10 15:14:56.993169 portage-3.0.45.3/lib/portage/util/futures/executor/fork.py
--rw-r--r--   0 root         (0) root         (0)     2831 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/futures/extendedfutures.py
--rw-r--r--   0 root         (0) root         (0)      516 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/futures/futures.py
--rw-r--r--   0 root         (0) root         (0)     6868 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/futures/iter_completed.py
--rw-r--r--   0 root         (0) root         (0)     6297 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/futures/retry.py
--rw-r--r--   0 root         (0) root         (0)     2237 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/futures/unix_events.py
--rw-r--r--   0 root         (0) root         (0)     1584 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/hooks.py
--rw-r--r--   0 root         (0) root         (0)     6549 2022-09-10 09:45:01.060384 portage-3.0.45.3/lib/portage/util/install_mask.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/util/iterators/
--rw-r--r--   0 root         (0) root         (0)     2996 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/util/iterators/MultiIterGroupBy.py
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.144132 portage-3.0.45.3/lib/portage/util/iterators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7349 2022-09-10 09:45:01.063717 portage-3.0.45.3/lib/portage/util/lafilefixer.py
--rw-r--r--   0 root         (0) root         (0)     4814 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/listdir.py
--rw-r--r--   0 root         (0) root         (0)     4339 2023-02-03 18:03:13.733528 portage-3.0.45.3/lib/portage/util/locale.py
--rw-r--r--   0 root         (0) root         (0)    13909 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/util/movefile.py
--rw-r--r--   0 root         (0) root         (0)     4258 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/util/mtimedb.py
--rw-r--r--   0 root         (0) root         (0)     2990 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/netlink.py
--rw-r--r--   0 root         (0) root         (0)     1336 2022-09-10 09:44:56.970356 portage-3.0.45.3/lib/portage/util/path.py
--rw-r--r--   0 root         (0) root         (0)     1527 2022-09-10 09:45:01.057050 portage-3.0.45.3/lib/portage/util/shelve.py
--rw-r--r--   0 root         (0) root         (0)     3635 2022-12-24 02:35:49.845990 portage-3.0.45.3/lib/portage/util/socks5.py
--rw-r--r--   0 root         (0) root         (0)    58416 2023-01-10 15:12:38.502432 portage-3.0.45.3/lib/portage/util/whirlpool.py
--rw-r--r--   0 root         (0) root         (0)     4506 2023-02-03 18:03:13.730194 portage-3.0.45.3/lib/portage/util/writeable_check.py
--rw-r--r--   0 root         (0) root         (0)    19275 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/versions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/lib/portage/xml/
--rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.147466 portage-3.0.45.3/lib/portage/xml/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16789 2023-02-03 18:03:13.736861 portage-3.0.45.3/lib/portage/xml/metadata.py
--rw-r--r--   0 root         (0) root         (0)    19413 2023-02-03 17:42:31.195846 portage-3.0.45.3/lib/portage/xpak.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/misc/
--rwxr-xr-x   0 root         (0) root         (0)    24116 2023-02-03 18:03:13.736861 portage-3.0.45.3/misc/emerge-delta-webrsync
--rwxr-xr-x   0 root         (0) root         (0)    29955 2023-03-19 19:17:05.343715 portage-3.0.45.3/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-19 19:18:17.020742 portage-3.0.45.3/src/
--rw-r--r--   0 root         (0) root         (0)    71291 2022-12-31 14:17:30.306859 portage-3.0.45.3/src/portage_util__whirlpool.c
--rw-r--r--   0 root         (0) root         (0)    13384 2022-12-24 02:35:49.849323 portage-3.0.45.3/src/portage_util_file_copy_reflink_linux.c
--rw-r--r--   0 root         (0) root         (0)     1276 2022-12-24 02:35:49.849323 portage-3.0.45.3/src/portage_util_libc.c
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:35.927469 portage-3.0.46/.portage_not_installed
+-rw-r--r--   0 root         (0) root         (0)     6944 2023-03-21 03:50:18.057424 portage-3.0.46/DEVELOPING
+-rw-r--r--   0 root         (0) root         (0)    18092 2021-11-12 08:15:35.927469 portage-3.0.46/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     4474 2023-04-07 09:56:10.598322 portage-3.0.46/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1864 2021-11-12 08:15:35.927469 portage-3.0.46/TEST-NOTES
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.571655 portage-3.0.46/bin/
+-rwxr-xr-x   0 root         (0) root         (0)     3262 2023-03-21 23:52:40.754842 portage-3.0.46/bin/archive-conf
+-rwxr-xr-x   0 root         (0) root         (0)     1443 2023-03-20 03:14:35.108827 portage-3.0.46/bin/bashrc-functions.sh
+-rwxr-xr-x   0 root         (0) root         (0)     4457 2023-03-21 23:52:40.598174 portage-3.0.46/bin/binhost-snapshot
+-rwxr-xr-x   0 root         (0) root         (0)       51 2021-11-12 08:15:35.934136 portage-3.0.46/bin/cgroup-release-agent
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.934136 portage-3.0.46/bin/chmod-lite -> ebuild-pyhelper
+-rwxr-xr-x   0 root         (0) root         (0)      951 2023-03-21 03:35:23.553538 portage-3.0.46/bin/chmod-lite.py
+-rwxr-xr-x   0 root         (0) root         (0)     5891 2023-03-21 03:35:23.553538 portage-3.0.46/bin/chpathtool.py
+-rwxr-xr-x   0 root         (0) root         (0)     1421 2023-03-21 03:35:23.553538 portage-3.0.46/bin/clean_locks
+-rwxr-xr-x   0 root         (0) root         (0)    19929 2023-03-21 23:52:40.598174 portage-3.0.46/bin/dispatch-conf
+-rwxr-xr-x   0 root         (0) root         (0)     8895 2023-03-21 03:35:23.556871 portage-3.0.46/bin/dohtml.py
+-rwxr-xr-x   0 root         (0) root         (0)    20007 2023-03-21 03:35:23.550205 portage-3.0.46/bin/doins.py
+-rwxr-xr-x   0 root         (0) root         (0)     6078 2023-03-21 03:35:23.550205 portage-3.0.46/bin/eapi.sh
+-rwxr-xr-x   0 root         (0) root         (0)     4310 2023-03-20 03:14:35.108827 portage-3.0.46/bin/eapi7-ver-funcs.sh
+-rwxr-xr-x   0 root         (0) root         (0)    15468 2023-03-21 23:52:40.598174 portage-3.0.46/bin/ebuild
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.571655 portage-3.0.46/bin/ebuild-helpers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.571655 portage-3.0.46/bin/ebuild-helpers/bsd/
+-rwxr-xr-x   0 root         (0) root         (0)      639 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/bsd/sed
+-rwxr-xr-x   0 root         (0) root         (0)      200 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/die
+-rwxr-xr-x   0 root         (0) root         (0)     1052 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/dobin
+-rwxr-xr-x   0 root         (0) root         (0)      515 2022-09-10 09:45:01.063717 portage-3.0.46/bin/ebuild-helpers/doconfd
+-rwxr-xr-x   0 root         (0) root         (0)      359 2022-09-10 09:45:01.057050 portage-3.0.46/bin/ebuild-helpers/dodir
+-rwxr-xr-x   0 root         (0) root         (0)      888 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/dodoc
+-rwxr-xr-x   0 root         (0) root         (0)      513 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/doenvd
+-rwxr-xr-x   0 root         (0) root         (0)      955 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/doexe
+-rwxr-xr-x   0 root         (0) root         (0)      531 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/dohard
+-rwxr-xr-x   0 root         (0) root         (0)      632 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/doheader
+-rwxr-xr-x   0 root         (0) root         (0)      782 2022-09-10 09:45:01.063717 portage-3.0.46/bin/ebuild-helpers/dohtml
+-rwxr-xr-x   0 root         (0) root         (0)      722 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/doinfo
+-rwxr-xr-x   0 root         (0) root         (0)      485 2022-09-10 09:45:01.063717 portage-3.0.46/bin/ebuild-helpers/doinitd
+-rwxr-xr-x   0 root         (0) root         (0)     3034 2022-09-10 09:45:01.057050 portage-3.0.46/bin/ebuild-helpers/doins
+-rwxr-xr-x   0 root         (0) root         (0)     1441 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/dolib
+-rwxr-xr-x   0 root         (0) root         (0)      189 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/dolib.a
+-rwxr-xr-x   0 root         (0) root         (0)      189 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/dolib.so
+-rwxr-xr-x   0 root         (0) root         (0)     1553 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/doman
+-rwxr-xr-x   0 root         (0) root         (0)     1219 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/domo
+-rwxr-xr-x   0 root         (0) root         (0)     1056 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/dosbin
+-rwxr-xr-x   0 root         (0) root         (0)      818 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/dosed
+-rwxr-xr-x   0 root         (0) root         (0)     2366 2022-09-10 09:45:01.063717 portage-3.0.46/bin/ebuild-helpers/dosym
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.46/bin/ebuild-helpers/eerror -> elog
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.46/bin/ebuild-helpers/einfo -> elog
+-rwxr-xr-x   0 root         (0) root         (0)      204 2022-09-10 09:45:01.053717 portage-3.0.46/bin/ebuild-helpers/elog
+-rwxr-xr-x   0 root         (0) root         (0)      894 2022-09-10 09:45:01.053717 portage-3.0.46/bin/ebuild-helpers/emake
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.46/bin/ebuild-helpers/eqawarn -> elog
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.937469 portage-3.0.46/bin/ebuild-helpers/ewarn -> elog
+-rwxr-xr-x   0 root         (0) root         (0)      792 2022-09-10 09:45:01.057050 portage-3.0.46/bin/ebuild-helpers/fowners
+-rwxr-xr-x   0 root         (0) root         (0)      850 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/fperms
+-rwxr-xr-x   0 root         (0) root         (0)      490 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/keepdir
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newbin -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newconfd -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newdoc -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newenvd -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newexe -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newheader -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newinitd -> newins
+-rwxr-xr-x   0 root         (0) root         (0)     1201 2023-02-03 18:03:13.730194 portage-3.0.46/bin/ebuild-helpers/newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newlib.a -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newlib.so -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newman -> newins
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/newsbin -> newins
+-rwxr-xr-x   0 root         (0) root         (0)      359 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/nonfatal
+-rwxr-xr-x   0 root         (0) root         (0)      739 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/portageq
+-rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/prepall
+-rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.053717 portage-3.0.46/bin/ebuild-helpers/prepalldocs
+-rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.053717 portage-3.0.46/bin/ebuild-helpers/prepallinfo
+-rwxr-xr-x   0 root         (0) root         (0)      245 2022-09-10 09:45:01.053717 portage-3.0.46/bin/ebuild-helpers/prepallman
+-rwxr-xr-x   0 root         (0) root         (0)      383 2022-09-10 09:45:01.057050 portage-3.0.46/bin/ebuild-helpers/prepallstrip
+-rwxr-xr-x   0 root         (0) root         (0)      843 2023-04-07 09:45:46.551215 portage-3.0.46/bin/ebuild-helpers/prepinfo
+-rwxr-xr-x   0 root         (0) root         (0)      364 2023-04-07 09:45:46.551215 portage-3.0.46/bin/ebuild-helpers/prepman
+-rwxr-xr-x   0 root         (0) root         (0)      375 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/prepstrip
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.571655 portage-3.0.46/bin/ebuild-helpers/unprivileged/
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-helpers/unprivileged/chgrp -> chown
+-rwxr-xr-x   0 root         (0) root         (0)     1178 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/unprivileged/chown
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.571655 portage-3.0.46/bin/ebuild-helpers/xattr/
+-rwxr-xr-x   0 root         (0) root         (0)     1369 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ebuild-helpers/xattr/install
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.940802 portage-3.0.46/bin/ebuild-ipc -> ebuild-pyhelper
+-rwxr-xr-x   0 root         (0) root         (0)    10684 2023-03-21 23:52:40.598174 portage-3.0.46/bin/ebuild-ipc.py
+-rwxr-xr-x   0 root         (0) root         (0)      616 2022-09-10 09:45:01.057050 portage-3.0.46/bin/ebuild-pyhelper
+-rwxr-xr-x   0 root         (0) root         (0)    26114 2023-03-21 03:35:23.556871 portage-3.0.46/bin/ebuild.sh
+-rwxr-xr-x   0 root         (0) root         (0)     6481 2022-12-24 02:35:49.845990 portage-3.0.46/bin/ecompress
+-rwxr-xr-x   0 root         (0) root         (0)     1746 2022-09-10 09:45:01.060384 portage-3.0.46/bin/ecompress-file
+-rwxr-xr-x   0 root         (0) root         (0)    53990 2023-03-21 23:52:40.598174 portage-3.0.46/bin/egencache
+-rwxr-xr-x   0 root         (0) root         (0)     1857 2023-03-21 03:35:23.556871 portage-3.0.46/bin/emaint
+-rwxr-xr-x   0 root         (0) root         (0)     3301 2023-03-21 23:52:40.598174 portage-3.0.46/bin/emerge
+-rwxr-xr-x   0 root         (0) root         (0)    15950 2022-09-10 09:45:01.063717 portage-3.0.46/bin/emerge-webrsync
+-rwxr-xr-x   0 root         (0) root         (0)      634 2022-09-10 09:45:01.053717 portage-3.0.46/bin/emirrordist
+-rwxr-xr-x   0 root         (0) root         (0)     1048 2023-03-21 03:35:23.556871 portage-3.0.46/bin/env-update
+-rwxr-xr-x   0 root         (0) root         (0)    17296 2023-03-21 03:35:23.556871 portage-3.0.46/bin/estrip
+-rwxr-xr-x   0 root         (0) root         (0)    23454 2023-03-21 03:50:18.057424 portage-3.0.46/bin/etc-update
+-rwxr-xr-x   0 root         (0) root         (0)     6045 2023-03-21 03:35:23.556871 portage-3.0.46/bin/filter-bash-environment.py
+-rwxr-xr-x   0 root         (0) root         (0)     1601 2023-03-21 03:35:23.556871 portage-3.0.46/bin/fixpackages
+-rwxr-xr-x   0 root         (0) root         (0)    15636 2023-03-21 23:52:40.601508 portage-3.0.46/bin/glsa-check
+-rwxr-xr-x   0 root         (0) root         (0)     2166 2023-03-21 03:35:23.556871 portage-3.0.46/bin/gpkg-helper.py
+-rwxr-xr-x   0 root         (0) root         (0)     2476 2022-12-24 02:35:49.845990 portage-3.0.46/bin/gpkg-sign
+-rwxr-xr-x   0 root         (0) root         (0)     2918 2023-03-20 03:14:35.108827 portage-3.0.46/bin/helper-functions.sh
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/bin/install-qa-check.d/
+-rwxr-xr-x   0 root         (0) root         (0)      444 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/05double-D
+-rwxr-xr-x   0 root         (0) root         (0)     4302 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/05prefix
+-rwxr-xr-x   0 root         (0) root         (0)     5559 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/10executable-issues
+-rwxr-xr-x   0 root         (0) root         (0)     3591 2023-03-21 03:35:23.550205 portage-3.0.46/bin/install-qa-check.d/10ignored-flags
+-rwxr-xr-x   0 root         (0) root         (0)      406 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/20deprecated-directories
+-rwxr-xr-x   0 root         (0) root         (0)      835 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/20runtime-directories
+-rwxr-xr-x   0 root         (0) root         (0)     3306 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/60bash-completion
+-rwxr-xr-x   0 root         (0) root         (0)     1443 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/60openrc
+-rwxr-xr-x   0 root         (0) root         (0)     5508 2023-03-21 03:35:23.550205 portage-3.0.46/bin/install-qa-check.d/60pkgconfig
+-rwxr-xr-x   0 root         (0) root         (0)      668 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/60pngfix
+-rwxr-xr-x   0 root         (0) root         (0)      687 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/60systemd
+-rwxr-xr-x   0 root         (0) root         (0)      442 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/60udev
+-rwxr-xr-x   0 root         (0) root         (0)     5556 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/80libraries
+-rwxr-xr-x   0 root         (0) root         (0)     1417 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/80multilib-strict
+-rwxr-xr-x   0 root         (0) root         (0)     1918 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/90bad-bin-group-write
+-rwxr-xr-x   0 root         (0) root         (0)     1566 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/90bad-bin-owner
+-rwxr-xr-x   0 root         (0) root         (0)      654 2023-03-20 03:14:35.108827 portage-3.0.46/bin/install-qa-check.d/90cmake-warnings
+-rwxr-xr-x   0 root         (0) root         (0)     3333 2023-03-21 03:50:18.057424 portage-3.0.46/bin/install-qa-check.d/90config-impl-decl
+-rwxr-xr-x   0 root         (0) root         (0)     7866 2023-03-21 03:35:23.550205 portage-3.0.46/bin/install-qa-check.d/90gcc-warnings
+-rwxr-xr-x   0 root         (0) root         (0)     1042 2023-03-20 03:14:35.112161 portage-3.0.46/bin/install-qa-check.d/90world-writable
+-rwxr-xr-x   0 root         (0) root         (0)     1518 2023-03-20 03:14:35.112161 portage-3.0.46/bin/install-qa-check.d/95empty-dirs
+-rwxr-xr-x   0 root         (0) root         (0)     6314 2023-03-21 23:52:40.601508 portage-3.0.46/bin/install.py
+-rwxr-xr-x   0 root         (0) root         (0)    18552 2023-03-21 03:50:18.057424 portage-3.0.46/bin/isolated-functions.sh
+-rwxr-xr-x   0 root         (0) root         (0)      903 2023-03-21 03:35:23.553538 portage-3.0.46/bin/lock-helper.py
+-rwxr-xr-x   0 root         (0) root         (0)    20244 2023-04-07 09:45:46.551215 portage-3.0.46/bin/misc-functions.sh
+-rwxr-xr-x   0 root         (0) root         (0)    34584 2023-03-20 03:14:35.112161 portage-3.0.46/bin/phase-functions.sh
+-rwxr-xr-x   0 root         (0) root         (0)    33794 2023-03-21 03:35:23.553538 portage-3.0.46/bin/phase-helpers.sh
+-rwxr-xr-x   0 root         (0) root         (0)     5723 2023-03-21 03:35:23.556871 portage-3.0.46/bin/pid-ns-init
+-rwxr-xr-x   0 root         (0) root         (0)    51197 2023-03-21 23:52:40.601508 portage-3.0.46/bin/portageq
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/bin/postinst-qa-check.d/
+-rwxr-xr-x   0 root         (0) root         (0)     5236 2023-03-20 03:14:35.112161 portage-3.0.46/bin/postinst-qa-check.d/50xdg-utils
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/bin/preinst-qa-check.d/
+lrwxrwxrwx   0 root         (0) root         (0)        0 2021-11-12 08:15:35.947469 portage-3.0.46/bin/preinst-qa-check.d/50xdg-utils -> ../postinst-qa-check.d/50xdg-utils
+-rwxr-xr-x   0 root         (0) root         (0)    16731 2023-03-21 23:52:40.601508 portage-3.0.46/bin/quickpkg
+-rwxr-xr-x   0 root         (0) root         (0)     4992 2023-03-21 03:35:23.556871 portage-3.0.46/bin/regenworld
+-rwxr-xr-x   0 root         (0) root         (0)     4533 2023-03-21 03:50:18.057424 portage-3.0.46/bin/save-ebuild-env.sh
+-rwxr-xr-x   0 root         (0) root         (0)     1339 2022-09-10 09:45:01.060384 portage-3.0.46/bin/shelve-utils
+-rwxr-xr-x   0 root         (0) root         (0)     8140 2023-03-21 03:35:23.556871 portage-3.0.46/bin/socks5-server.py
+-rwxr-xr-x   0 root         (0) root         (0)     4784 2023-03-21 23:52:40.601508 portage-3.0.46/bin/xattr-helper.py
+-rwxr-xr-x   0 root         (0) root         (0)     1825 2023-03-21 03:35:23.550205 portage-3.0.46/bin/xpak-helper.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/cnf/
+-rw-r--r--   0 root         (0) root         (0)     1718 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.alpha.diff
+-rw-r--r--   0 root         (0) root         (0)     2319 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.amd64-fbsd.diff
+-rw-r--r--   0 root         (0) root         (0)     2309 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.amd64.diff
+-rw-r--r--   0 root         (0) root         (0)     1592 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.arm.diff
+-rw-r--r--   0 root         (0) root         (0)     1580 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.arm64.diff
+-rw-r--r--   0 root         (0) root         (0)     2465 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.hppa.diff
+-rw-r--r--   0 root         (0) root         (0)      663 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.ia64.diff
+-rw-r--r--   0 root         (0) root         (0)     2192 2023-03-21 03:35:23.550205 portage-3.0.46/cnf/make.conf.example.loong.diff
+-rw-r--r--   0 root         (0) root         (0)      900 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.m68k.diff
+-rw-r--r--   0 root         (0) root         (0)     1383 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.mips.diff
+-rw-r--r--   0 root         (0) root         (0)     3541 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.ppc.diff
+-rw-r--r--   0 root         (0) root         (0)     2361 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.ppc64.diff
+-rw-r--r--   0 root         (0) root         (0)     2332 2022-09-10 09:44:56.963689 portage-3.0.46/cnf/make.conf.example.riscv.diff
+-rw-r--r--   0 root         (0) root         (0)      656 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.s390.diff
+-rw-r--r--   0 root         (0) root         (0)     1257 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.sh.diff
+-rw-r--r--   0 root         (0) root         (0)      728 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.sparc-fbsd.diff
+-rw-r--r--   0 root         (0) root         (0)     2129 2021-12-09 09:19:33.760140 portage-3.0.46/cnf/make.conf.example.sparc.diff
+-rw-r--r--   0 root         (0) root         (0)     2507 2021-12-09 09:19:33.763473 portage-3.0.46/cnf/make.conf.example.x86-fbsd.diff
+-rw-r--r--   0 root         (0) root         (0)     3759 2021-12-09 09:19:33.763473 portage-3.0.46/cnf/make.conf.example.x86.diff
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/doc/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/doc/api/
+-rw-r--r--   0 root         (0) root         (0)     1141 2021-11-12 08:15:35.954135 portage-3.0.46/doc/api/Makefile
+-rw-r--r--   0 root         (0) root         (0)     2372 2023-03-21 03:35:23.550205 portage-3.0.46/doc/api/conf.py
+-rw-r--r--   0 root         (0) root         (0)      217 2021-11-12 08:15:35.954135 portage-3.0.46/doc/api/index.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/doc/config/
+-rw-r--r--   0 root         (0) root         (0)     1900 2021-11-12 08:15:35.954135 portage-3.0.46/doc/config/bashrc.docbook
+-rw-r--r--   0 root         (0) root         (0)    26214 2021-11-12 08:15:35.954135 portage-3.0.46/doc/config/sets.docbook
+-rw-r--r--   0 root         (0) root         (0)       85 2021-11-12 08:15:35.954135 portage-3.0.46/doc/config.docbook
+-rw-r--r--   0 root         (0) root         (0)      257 2021-11-12 08:15:35.954135 portage-3.0.46/doc/custom.xsl
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/doc/dependency_resolution/
+-rw-r--r--   0 root         (0) root         (0)     3281 2021-11-12 08:15:35.957468 portage-3.0.46/doc/dependency_resolution/decision_making.docbook
+-rw-r--r--   0 root         (0) root         (0)     4154 2021-11-12 08:15:35.957468 portage-3.0.46/doc/dependency_resolution/package_modeling.docbook
+-rw-r--r--   0 root         (0) root         (0)     3451 2021-11-12 08:15:35.957468 portage-3.0.46/doc/dependency_resolution/task_scheduling.docbook
+-rw-r--r--   0 root         (0) root         (0)      200 2021-11-12 08:15:35.954135 portage-3.0.46/doc/dependency_resolution.docbook
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/doc/package/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/doc/package/ebuild/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.574988 portage-3.0.46/doc/package/ebuild/eapi/
+-rw-r--r--   0 root         (0) root         (0)      487 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/eapi/0.docbook
+-rw-r--r--   0 root         (0) root         (0)     1598 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/eapi/1.docbook
+-rw-r--r--   0 root         (0) root         (0)     8299 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/eapi/2.docbook
+-rw-r--r--   0 root         (0) root         (0)     2938 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/eapi/3.docbook
+-rw-r--r--   0 root         (0) root         (0)     3112 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/eapi/4-slot-abi.docbook
+-rw-r--r--   0 root         (0) root         (0)    14690 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/eapi/4.docbook
+-rw-r--r--   0 root         (0) root         (0)     8044 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/eapi/5.docbook
+-rw-r--r--   0 root         (0) root         (0)     1725 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/helper_functions.docbook
+-rw-r--r--   0 root         (0) root         (0)     2780 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package/ebuild/phases.docbook
+-rw-r--r--   0 root         (0) root         (0)      364 2022-09-10 09:45:01.060384 portage-3.0.46/doc/package/ebuild.docbook
+-rw-r--r--   0 root         (0) root         (0)       76 2021-11-12 08:15:35.957468 portage-3.0.46/doc/package.docbook
+-rw-r--r--   0 root         (0) root         (0)     2194 2022-09-10 09:45:01.060384 portage-3.0.46/doc/portage.docbook
+-rw-r--r--   0 root         (0) root         (0)    19579 2021-11-12 08:15:35.960802 portage-3.0.46/doc/qa.docbook
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.561655 portage-3.0.46/lib/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.578322 portage-3.0.46/lib/_emerge/
+-rw-r--r--   0 root         (0) root         (0)      816 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/AbstractDepPriority.py
+-rw-r--r--   0 root         (0) root         (0)    18460 2023-03-21 03:50:18.057424 portage-3.0.46/lib/_emerge/AbstractEbuildProcess.py
+-rw-r--r--   0 root         (0) root         (0)     3723 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/AbstractPollTask.py
+-rw-r--r--   0 root         (0) root         (0)    10471 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/AsynchronousLock.py
+-rw-r--r--   0 root         (0) root         (0)     7090 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/AsynchronousTask.py
+-rw-r--r--   0 root         (0) root         (0)      473 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/AtomArg.py
+-rw-r--r--   0 root         (0) root         (0)    21241 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/Binpkg.py
+-rw-r--r--   0 root         (0) root         (0)     2367 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/BinpkgEnvExtractor.py
+-rw-r--r--   0 root         (0) root         (0)     5494 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/BinpkgExtractorAsync.py
+-rw-r--r--   0 root         (0) root         (0)     9584 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/BinpkgFetcher.py
+-rw-r--r--   0 root         (0) root         (0)     1684 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/BinpkgPrefetcher.py
+-rw-r--r--   0 root         (0) root         (0)     4414 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/BinpkgVerifier.py
+-rw-r--r--   0 root         (0) root         (0)      483 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/Blocker.py
+-rw-r--r--   0 root         (0) root         (0)     6827 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/BlockerCache.py
+-rw-r--r--   0 root         (0) root         (0)     5325 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/BlockerDB.py
+-rw-r--r--   0 root         (0) root         (0)      355 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/BlockerDepPriority.py
+-rw-r--r--   0 root         (0) root         (0)     4044 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/CompositeTask.py
+-rw-r--r--   0 root         (0) root         (0)     1732 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/DepPriority.py
+-rw-r--r--   0 root         (0) root         (0)     1564 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/DepPriorityNormalRange.py
+-rw-r--r--   0 root         (0) root         (0)     3647 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/DepPrioritySatisfiedRange.py
+-rw-r--r--   0 root         (0) root         (0)      878 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/Dependency.py
+-rw-r--r--   0 root         (0) root         (0)     1056 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/DependencyArg.py
+-rw-r--r--   0 root         (0) root         (0)     2050 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/EbuildBinpkg.py
+-rw-r--r--   0 root         (0) root         (0)    23204 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/EbuildBuild.py
+-rw-r--r--   0 root         (0) root         (0)     5749 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/EbuildBuildDir.py
+-rw-r--r--   0 root         (0) root         (0)     2961 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/EbuildExecuter.py
+-rw-r--r--   0 root         (0) root         (0)    14395 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/EbuildFetcher.py
+-rw-r--r--   0 root         (0) root         (0)     1359 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/EbuildFetchonly.py
+-rw-r--r--   0 root         (0) root         (0)     4716 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/EbuildIpcDaemon.py
+-rw-r--r--   0 root         (0) root         (0)     3258 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/EbuildMerge.py
+-rw-r--r--   0 root         (0) root         (0)     7597 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/EbuildMetadataPhase.py
+-rw-r--r--   0 root         (0) root         (0)    22622 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/EbuildPhase.py
+-rw-r--r--   0 root         (0) root         (0)      872 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/EbuildProcess.py
+-rw-r--r--   0 root         (0) root         (0)      679 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/EbuildSpawnProcess.py
+-rw-r--r--   0 root         (0) root         (0)    12786 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/FakeVartree.py
+-rw-r--r--   0 root         (0) root         (0)     1774 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/FifoIpcDaemon.py
+-rw-r--r--   0 root         (0) root         (0)     9113 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/JobStatusDisplay.py
+-rw-r--r--   0 root         (0) root         (0)     4823 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/MergeListItem.py
+-rw-r--r--   0 root         (0) root         (0)     6121 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/MetadataRegen.py
+-rw-r--r--   0 root         (0) root         (0)     2424 2022-09-10 09:45:01.063717 portage-3.0.46/lib/_emerge/MiscFunctionsProcess.py
+-rw-r--r--   0 root         (0) root         (0)    31019 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/Package.py
+-rw-r--r--   0 root         (0) root         (0)      735 2022-09-10 09:44:56.967023 portage-3.0.46/lib/_emerge/PackageArg.py
+-rw-r--r--   0 root         (0) root         (0)     2626 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/PackageMerge.py
+-rw-r--r--   0 root         (0) root         (0)     4333 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/PackagePhase.py
+-rw-r--r--   0 root         (0) root         (0)     5870 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/PackageUninstall.py
+-rw-r--r--   0 root         (0) root         (0)     4651 2022-09-10 09:44:56.967023 portage-3.0.46/lib/_emerge/PackageVirtualDbapi.py
+-rw-r--r--   0 root         (0) root         (0)     2681 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/PipeReader.py
+-rw-r--r--   0 root         (0) root         (0)     6630 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/PollScheduler.py
+-rw-r--r--   0 root         (0) root         (0)      603 2022-09-10 09:44:56.967023 portage-3.0.46/lib/_emerge/ProgressHandler.py
+-rw-r--r--   0 root         (0) root         (0)     1227 2022-09-10 09:44:56.967023 portage-3.0.46/lib/_emerge/RootConfig.py
+-rw-r--r--   0 root         (0) root         (0)    85615 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/Scheduler.py
+-rw-r--r--   0 root         (0) root         (0)     2648 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/SequentialTaskQueue.py
+-rw-r--r--   0 root         (0) root         (0)      421 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/SetArg.py
+-rw-r--r--   0 root         (0) root         (0)    10190 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/SpawnProcess.py
+-rw-r--r--   0 root         (0) root         (0)     3167 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/SubProcess.py
+-rw-r--r--   0 root         (0) root         (0)     1456 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/Task.py
+-rw-r--r--   0 root         (0) root         (0)     1538 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/TaskSequence.py
+-rw-r--r--   0 root         (0) root         (0)      455 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/UninstallFailure.py
+-rw-r--r--   0 root         (0) root         (0)     1326 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/UnmergeDepPriority.py
+-rw-r--r--   0 root         (0) root         (0)     3555 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/UseFlagDisplay.py
+-rw-r--r--   0 root         (0) root         (0)     2995 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/UserQuery.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:35.977468 portage-3.0.46/lib/_emerge/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1165 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/_find_deep_system_runtime_deps.py
+-rw-r--r--   0 root         (0) root         (0)      442 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/_flush_elog_mod_echo.py
+-rw-r--r--   0 root         (0) root         (0)   149373 2023-03-21 03:50:18.060757 portage-3.0.46/lib/_emerge/actions.py
+-rw-r--r--   0 root         (0) root         (0)     1971 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/chk_updated_cfg_files.py
+-rw-r--r--   0 root         (0) root         (0)      498 2022-09-10 09:44:56.963689 portage-3.0.46/lib/_emerge/clear_caches.py
+-rw-r--r--   0 root         (0) root         (0)      586 2023-02-03 18:03:13.733528 portage-3.0.46/lib/_emerge/countdown.py
+-rw-r--r--   0 root         (0) root         (0)     8835 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/create_depgraph_params.py
+-rw-r--r--   0 root         (0) root         (0)     5191 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/create_world_atom.py
+-rw-r--r--   0 root         (0) root         (0)   499558 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/depgraph.py
+-rw-r--r--   0 root         (0) root         (0)     1814 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/emergelog.py
+-rw-r--r--   0 root         (0) root         (0)      958 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/getloadavg.py
+-rw-r--r--   0 root         (0) root         (0)     3425 2022-09-10 09:44:56.970356 portage-3.0.46/lib/_emerge/help.py
+-rw-r--r--   0 root         (0) root         (0)      785 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/is_valid_package_atom.py
+-rw-r--r--   0 root         (0) root         (0)    42164 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/main.py
+-rw-r--r--   0 root         (0) root         (0)     5614 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/post_emerge.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.578322 portage-3.0.46/lib/_emerge/resolver/
+-rw-r--r--   0 root         (0) root         (0)     3198 2022-09-10 09:44:56.970356 portage-3.0.46/lib/_emerge/resolver/DbapiProvidesIndex.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:35.980801 portage-3.0.46/lib/_emerge/resolver/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    11328 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/resolver/backtracking.py
+-rw-r--r--   0 root         (0) root         (0)    11932 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/resolver/circular_dependency.py
+-rw-r--r--   0 root         (0) root         (0)    39548 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/resolver/output.py
+-rw-r--r--   0 root         (0) root         (0)    20756 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/resolver/output_helpers.py
+-rw-r--r--   0 root         (0) root         (0)    15636 2023-03-21 03:35:23.550205 portage-3.0.46/lib/_emerge/resolver/package_tracker.py
+-rw-r--r--   0 root         (0) root         (0)    59893 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/resolver/slot_collision.py
+-rw-r--r--   0 root         (0) root         (0)    20976 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/search.py
+-rw-r--r--   0 root         (0) root         (0)     1573 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/show_invalid_depstring_notice.py
+-rw-r--r--   0 root         (0) root         (0)     3196 2023-03-21 03:35:23.553538 portage-3.0.46/lib/_emerge/stdout_spinner.py
+-rw-r--r--   0 root         (0) root         (0)    26564 2023-03-21 03:35:23.556871 portage-3.0.46/lib/_emerge/unmerge.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.578322 portage-3.0.46/lib/portage/
+-rw-r--r--   0 root         (0) root         (0)    25908 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.578322 portage-3.0.46/lib/portage/_compat_upgrade/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.007468 portage-3.0.46/lib/portage/_compat_upgrade/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1666 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/_compat_upgrade/binpkg_compression.py
+-rw-r--r--   0 root         (0) root         (0)     1240 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_compat_upgrade/binpkg_multi_instance.py
+-rw-r--r--   0 root         (0) root         (0)     4288 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_compat_upgrade/default_locations.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.578322 portage-3.0.46/lib/portage/_emirrordist/
+-rw-r--r--   0 root         (0) root         (0)     5376 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_emirrordist/Config.py
+-rw-r--r--   0 root         (0) root         (0)     7223 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_emirrordist/ContentDB.py
+-rw-r--r--   0 root         (0) root         (0)     4631 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_emirrordist/DeletionIterator.py
+-rw-r--r--   0 root         (0) root         (0)     5079 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_emirrordist/DeletionTask.py
+-rw-r--r--   0 root         (0) root         (0)    11176 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_emirrordist/FetchIterator.py
+-rw-r--r--   0 root         (0) root         (0)    25443 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_emirrordist/FetchTask.py
+-rw-r--r--   0 root         (0) root         (0)     9145 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_emirrordist/MirrorDistTask.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.007468 portage-3.0.46/lib/portage/_emirrordist/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    16082 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/_emirrordist/main.py
+-rw-r--r--   0 root         (0) root         (0)    10222 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_global_updates.py
+-rw-r--r--   0 root         (0) root         (0)     2550 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/_legacy_globals.py
+-rw-r--r--   0 root         (0) root         (0)     4762 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_selinux.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.578322 portage-3.0.46/lib/portage/_sets/
+-rw-r--r--   0 root         (0) root         (0)     1719 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_sets/ProfilePackageSet.py
+-rw-r--r--   0 root         (0) root         (0)    14268 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/_sets/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     8205 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_sets/base.py
+-rw-r--r--   0 root         (0) root         (0)    22035 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_sets/dbapi.py
+-rw-r--r--   0 root         (0) root         (0)    15573 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_sets/files.py
+-rw-r--r--   0 root         (0) root         (0)     3603 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/_sets/libs.py
+-rw-r--r--   0 root         (0) root         (0)     2406 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_sets/profiles.py
+-rw-r--r--   0 root         (0) root         (0)     3535 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_sets/security.py
+-rw-r--r--   0 root         (0) root         (0)     1441 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/_sets/shell.py
+-rw-r--r--   0 root         (0) root         (0)     2576 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/binpkg.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.578322 portage-3.0.46/lib/portage/binrepo/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.014134 portage-3.0.46/lib/portage/binrepo/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4554 2023-02-03 18:03:13.730194 portage-3.0.46/lib/portage/binrepo/config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/cache/
+-rw-r--r--   0 root         (0) root         (0)      101 2021-11-12 08:15:36.014134 portage-3.0.46/lib/portage/cache/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3167 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/anydbm.py
+-rw-r--r--   0 root         (0) root         (0)     2139 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/cache_errors.py
+-rw-r--r--   0 root         (0) root         (0)     5226 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/ebuild_xattr.py
+-rw-r--r--   0 root         (0) root         (0)     5286 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/flat_hash.py
+-rw-r--r--   0 root         (0) root         (0)     3197 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/fs_template.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/cache/index/
+-rw-r--r--   0 root         (0) root         (0)      562 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/index/IndexStreamIterator.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.017468 portage-3.0.46/lib/portage/cache/index/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1394 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/cache/index/pkg_desc_index.py
+-rw-r--r--   0 root         (0) root         (0)    11957 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/cache/mappings.py
+-rw-r--r--   0 root         (0) root         (0)     5844 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/cache/metadata.py
+-rw-r--r--   0 root         (0) root         (0)    11820 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/cache/sql_template.py
+-rw-r--r--   0 root         (0) root         (0)    13390 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/cache/sqlite.py
+-rw-r--r--   0 root         (0) root         (0)    13272 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/template.py
+-rw-r--r--   0 root         (0) root         (0)      789 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/cache/volatile.py
+-rw-r--r--   0 root         (0) root         (0)    16566 2023-04-07 09:45:44.114534 portage-3.0.46/lib/portage/checksum.py
+-rw-r--r--   0 root         (0) root         (0)     8879 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/const.py
+-rw-r--r--   0 root         (0) root         (0)    11470 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/cvstree.py
+-rw-r--r--   0 root         (0) root         (0)    11537 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/data.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/dbapi/
+-rw-r--r--   0 root         (0) root         (0)      643 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/dbapi/DummyTree.py
+-rw-r--r--   0 root         (0) root         (0)     5690 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/dbapi/IndexedPortdb.py
+-rw-r--r--   0 root         (0) root         (0)     3743 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/dbapi/IndexedVardb.py
+-rw-r--r--   0 root         (0) root         (0)     2991 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/dbapi/_ContentsCaseSensitivityManager.py
+-rw-r--r--   0 root         (0) root         (0)    10128 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/dbapi/_MergeProcess.py
+-rw-r--r--   0 root         (0) root         (0)     1511 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/dbapi/_SyncfsProcess.py
+-rw-r--r--   0 root         (0) root         (0)     6019 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/dbapi/_VdbMetadataDelta.py
+-rw-r--r--   0 root         (0) root         (0)    16769 2023-04-07 09:45:48.221225 portage-3.0.46/lib/portage/dbapi/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2545 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/dbapi/_expand_new_virt.py
+-rw-r--r--   0 root         (0) root         (0)     1685 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/dbapi/_similar_name_search.py
+-rw-r--r--   0 root         (0) root         (0)    90388 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/dbapi/bintree.py
+-rw-r--r--   0 root         (0) root         (0)     4184 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/dbapi/cpv_expand.py
+-rw-r--r--   0 root         (0) root         (0)     1889 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/dbapi/dep_expand.py
+-rw-r--r--   0 root         (0) root         (0)    64264 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/dbapi/porttree.py
+-rw-r--r--   0 root         (0) root         (0)   252193 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/dbapi/vartree.py
+-rw-r--r--   0 root         (0) root         (0)     7587 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/dbapi/virtual.py
+-rw-r--r--   0 root         (0) root         (0)     4029 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/debug.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/dep/
+-rw-r--r--   0 root         (0) root         (0)   107693 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/dep/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3780 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/dep/_dnf.py
+-rw-r--r--   0 root         (0) root         (0)     4396 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/dep/_slot_operator.py
+-rw-r--r--   0 root         (0) root         (0)    42498 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/dep/dep_check.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/dep/soname/
+-rw-r--r--   0 root         (0) root         (0)     1925 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/dep/soname/SonameAtom.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.030801 portage-3.0.46/lib/portage/dep/soname/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5080 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/dep/soname/multilib_category.py
+-rw-r--r--   0 root         (0) root         (0)     1491 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/dep/soname/parse.py
+-rw-r--r--   0 root         (0) root         (0)    14093 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/dispatch_conf.py
+-rw-r--r--   0 root         (0) root         (0)     8092 2023-01-10 15:35:29.386865 portage-3.0.46/lib/portage/eapi.py
+-rw-r--r--   0 root         (0) root         (0)     6757 2022-09-10 09:45:01.057050 portage-3.0.46/lib/portage/eclass_cache.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/elog/
+-rw-r--r--   0 root         (0) root         (0)     6879 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/elog/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      613 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/elog/filtering.py
+-rw-r--r--   0 root         (0) root         (0)     6065 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/elog/messages.py
+-rw-r--r--   0 root         (0) root         (0)      968 2023-02-03 18:03:13.736861 portage-3.0.46/lib/portage/elog/mod_custom.py
+-rw-r--r--   0 root         (0) root         (0)     2204 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/elog/mod_echo.py
+-rw-r--r--   0 root         (0) root         (0)     1660 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/elog/mod_mail.py
+-rw-r--r--   0 root         (0) root         (0)     3183 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/elog/mod_mail_summary.py
+-rw-r--r--   0 root         (0) root         (0)     3396 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/elog/mod_save.py
+-rw-r--r--   0 root         (0) root         (0)     3580 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/elog/mod_save_summary.py
+-rw-r--r--   0 root         (0) root         (0)      974 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/elog/mod_syslog.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/
+-rw-r--r--   0 root         (0) root         (0)      163 2021-11-12 08:15:36.037467 portage-3.0.46/lib/portage/emaint/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      762 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/defaults.py
+-rw-r--r--   0 root         (0) root         (0)     8691 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/emaint/main.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/
+-rw-r--r--   0 root         (0) root         (0)      173 2021-11-12 08:15:36.037467 portage-3.0.46/lib/portage/emaint/modules/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/binhost/
+-rw-r--r--   0 root         (0) root         (0)      524 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/binhost/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6358 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/emaint/modules/binhost/binhost.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/config/
+-rw-r--r--   0 root         (0) root         (0)      534 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/config/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2520 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/emaint/modules/config/config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/logs/
+-rw-r--r--   0 root         (0) root         (0)     1629 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/logs/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3535 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/emaint/modules/logs/logs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/merges/
+-rw-r--r--   0 root         (0) root         (0)     1417 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/merges/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9834 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/emaint/modules/merges/merges.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/move/
+-rw-r--r--   0 root         (0) root         (0)      851 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/move/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7693 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/emaint/modules/move/move.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/resume/
+-rw-r--r--   0 root         (0) root         (0)      566 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/resume/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1900 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/emaint/modules/resume/resume.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/sync/
+-rw-r--r--   0 root         (0) root         (0)     2145 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/sync/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    18469 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/emaint/modules/sync/sync.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/emaint/modules/world/
+-rw-r--r--   0 root         (0) root         (0)      502 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/emaint/modules/world/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3109 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/emaint/modules/world/world.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/env/
+-rw-r--r--   0 root         (0) root         (0)       52 2021-11-12 08:15:36.044134 portage-3.0.46/lib/portage/env/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3054 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/env/config.py
+-rw-r--r--   0 root         (0) root         (0)    10311 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/env/loaders.py
+-rw-r--r--   0 root         (0) root         (0)      578 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/env/validators.py
+-rw-r--r--   0 root         (0) root         (0)     6616 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/exception.py
+-rw-r--r--   0 root         (0) root         (0)    31465 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/getbinpkg.py
+-rw-r--r--   0 root         (0) root         (0)    31099 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/glsa.py
+-rw-r--r--   0 root         (0) root         (0)     3637 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/gpg.py
+-rw-r--r--   0 root         (0) root         (0)    80663 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/gpkg.py
+-rw-r--r--   0 root         (0) root         (0)     1550 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/localization.py
+-rw-r--r--   0 root         (0) root         (0)    28153 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/locks.py
+-rw-r--r--   0 root         (0) root         (0)     6187 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/mail.py
+-rw-r--r--   0 root         (0) root         (0)    31108 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/manifest.py
+-rw-r--r--   0 root         (0) root         (0)     8221 2023-02-03 18:03:13.736861 portage-3.0.46/lib/portage/metadata.py
+-rw-r--r--   0 root         (0) root         (0)     8568 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/module.py
+-rw-r--r--   0 root         (0) root         (0)    18485 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/news.py
+-rw-r--r--   0 root         (0) root         (0)    29784 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/output.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/package/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.047467 portage-3.0.46/lib/portage/package/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/package/ebuild/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.050800 portage-3.0.46/lib/portage/package/ebuild/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/package/ebuild/_config/
+-rw-r--r--   0 root         (0) root         (0)    13005 2023-02-03 18:03:13.730194 portage-3.0.46/lib/portage/package/ebuild/_config/KeywordsManager.py
+-rw-r--r--   0 root         (0) root         (0)     9192 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_config/LicenseManager.py
+-rw-r--r--   0 root         (0) root         (0)    16684 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_config/LocationsManager.py
+-rw-r--r--   0 root         (0) root         (0)    13915 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/package/ebuild/_config/MaskManager.py
+-rw-r--r--   0 root         (0) root         (0)    21565 2023-02-03 18:03:13.730194 portage-3.0.46/lib/portage/package/ebuild/_config/UseManager.py
+-rw-r--r--   0 root         (0) root         (0)     8443 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/package/ebuild/_config/VirtualsManager.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.050800 portage-3.0.46/lib/portage/package/ebuild/_config/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      770 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/package/ebuild/_config/env_var_validation.py
+-rw-r--r--   0 root         (0) root         (0)     4694 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/package/ebuild/_config/features_set.py
+-rw-r--r--   0 root         (0) root         (0)     2272 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/package/ebuild/_config/helper.py
+-rw-r--r--   0 root         (0) root         (0)     9457 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/package/ebuild/_config/special_env_vars.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/package/ebuild/_ipc/
+-rw-r--r--   0 root         (0) root         (0)      829 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_ipc/ExitCommand.py
+-rw-r--r--   0 root         (0) root         (0)      212 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_ipc/IpcCommand.py
+-rw-r--r--   0 root         (0) root         (0)     5193 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/package/ebuild/_ipc/QueryCommand.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.054134 portage-3.0.46/lib/portage/package/ebuild/_ipc/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1405 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_metadata_invalid.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/
+-rw-r--r--   0 root         (0) root         (0)     1413 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/ManifestProcess.py
+-rw-r--r--   0 root         (0) root         (0)     3767 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/ManifestScheduler.py
+-rw-r--r--   0 root         (0) root         (0)     7859 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/ManifestTask.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.057467 portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4987 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/package/ebuild/_spawn_nofetch.py
+-rw-r--r--   0 root         (0) root         (0)   133992 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/config.py
+-rw-r--r--   0 root         (0) root         (0)     4195 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/package/ebuild/deprecated_profile_check.py
+-rw-r--r--   0 root         (0) root         (0)     6732 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/package/ebuild/digestcheck.py
+-rw-r--r--   0 root         (0) root         (0)     9424 2023-03-21 03:35:23.550205 portage-3.0.46/lib/portage/package/ebuild/digestgen.py
+-rw-r--r--   0 root         (0) root         (0)   111662 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/package/ebuild/doebuild.py
+-rw-r--r--   0 root         (0) root         (0)    79658 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/package/ebuild/fetch.py
+-rw-r--r--   0 root         (0) root         (0)     4689 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/package/ebuild/getmaskingreason.py
+-rw-r--r--   0 root         (0) root         (0)     6556 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/package/ebuild/getmaskingstatus.py
+-rw-r--r--   0 root         (0) root         (0)    19287 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/package/ebuild/prepare_build_dirs.py
+-rw-r--r--   0 root         (0) root         (0)     1004 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/package/ebuild/profile_iuse.py
+-rw-r--r--   0 root         (0) root         (0)    41702 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/process.py
+-rw-r--r--   0 root         (0) root         (0)     1573 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/progress.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.581655 portage-3.0.46/lib/portage/proxy/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.060800 portage-3.0.46/lib/portage/proxy/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7832 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/proxy/lazyimport.py
+-rw-r--r--   0 root         (0) root         (0)     2857 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/proxy/objectproxy.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/repository/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.064134 portage-3.0.46/lib/portage/repository/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    62136 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/repository/config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/repository/storage/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.064134 portage-3.0.46/lib/portage/repository/storage/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3951 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/repository/storage/hardlink_quarantine.py
+-rw-r--r--   0 root         (0) root         (0)    10940 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/repository/storage/hardlink_rcu.py
+-rw-r--r--   0 root         (0) root         (0)     1153 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/repository/storage/inplace.py
+-rw-r--r--   0 root         (0) root         (0)     2675 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/repository/storage/interface.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/
+-rw-r--r--   0 root         (0) root         (0)     1589 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/sync/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3015 2023-02-03 18:03:13.733528 portage-3.0.46/lib/portage/sync/config_checks.py
+-rw-r--r--   0 root         (0) root         (0)    14745 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/sync/controller.py
+-rw-r--r--   0 root         (0) root         (0)      696 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/sync/getaddrinfo_validate.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/modules/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.067467 portage-3.0.46/lib/portage/sync/modules/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/modules/cvs/
+-rw-r--r--   0 root         (0) root         (0)     1650 2023-02-03 18:03:13.733528 portage-3.0.46/lib/portage/sync/modules/cvs/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2339 2023-02-03 18:03:13.730194 portage-3.0.46/lib/portage/sync/modules/cvs/cvs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/modules/git/
+-rw-r--r--   0 root         (0) root         (0)     2722 2023-02-03 18:03:13.730194 portage-3.0.46/lib/portage/sync/modules/git/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    20049 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/sync/modules/git/git.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/modules/mercurial/
+-rw-r--r--   0 root         (0) root         (0)     1403 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/sync/modules/mercurial/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6125 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/sync/modules/mercurial/mercurial.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/modules/rsync/
+-rw-r--r--   0 root         (0) root         (0)     1287 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/sync/modules/rsync/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    33953 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/sync/modules/rsync/rsync.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/modules/svn/
+-rw-r--r--   0 root         (0) root         (0)     1037 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/sync/modules/svn/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2759 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/sync/modules/svn/svn.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/sync/modules/webrsync/
+-rw-r--r--   0 root         (0) root         (0)     1648 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/sync/modules/webrsync/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5092 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/sync/modules/webrsync/webrsync.py
+-rw-r--r--   0 root         (0) root         (0)     2485 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/sync/old_tree_timestamp.py
+-rw-r--r--   0 root         (0) root         (0)    13139 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/sync/syncbase.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/.gnupg/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/.gnupg/openpgp-revocs.d/
+-rw-r--r--   0 root         (0) root         (0)     1850 2022-09-10 09:45:01.063717 portage-3.0.46/lib/portage/tests/.gnupg/openpgp-revocs.d/06B3A311BD775C280D22A9305D90EA06352177F6.rev
+-rw-r--r--   0 root         (0) root         (0)     1852 2022-09-10 09:45:01.063717 portage-3.0.46/lib/portage/tests/.gnupg/openpgp-revocs.d/8DEDA2CDED49C8809287B89D8812797DDF1DD192.rev
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/.gnupg/private-keys-v1.d/
+-rw-r--r--   0 root         (0) root         (0)     2055 2022-09-10 09:45:01.057050 portage-3.0.46/lib/portage/tests/.gnupg/private-keys-v1.d/273B030399E7BEA66A9AD42216DE7CA17BA5D42E.key
+-rw-r--r--   0 root         (0) root         (0)     2055 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/tests/.gnupg/private-keys-v1.d/C99796FB85B0C3DF03314A11B5850C51167D6282.key
+-rw-r--r--   0 root         (0) root         (0)     2774 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/tests/.gnupg/pubring.kbx
+-rw-r--r--   0 root         (0) root         (0)     1360 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/tests/.gnupg/trustdb.gpg
+-rw-r--r--   0 root         (0) root         (0)    11871 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/tests/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/bin/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.074133 portage-3.0.46/lib/portage/tests/bin/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.074133 portage-3.0.46/lib/portage/tests/bin/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     2658 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/bin/setup_env.py
+-rw-r--r--   0 root         (0) root         (0)      547 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/bin/test_dobin.py
+-rw-r--r--   0 root         (0) root         (0)      565 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/bin/test_dodir.py
+-rw-r--r--   0 root         (0) root         (0)    13013 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/bin/test_doins.py
+-rw-r--r--   0 root         (0) root         (0)     9192 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/bin/test_eapi7_ver_funcs.py
+-rw-r--r--   0 root         (0) root         (0)     3075 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/bin/test_filter_bash_env.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/dbapi/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.074133 portage-3.0.46/lib/portage/tests/dbapi/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.074133 portage-3.0.46/lib/portage/tests/dbapi/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     3673 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dbapi/test_auxdb.py
+-rw-r--r--   0 root         (0) root         (0)     6521 2023-02-03 18:03:13.730194 portage-3.0.46/lib/portage/tests/dbapi/test_bintree.py
+-rw-r--r--   0 root         (0) root         (0)     3973 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/dbapi/test_fakedbapi.py
+-rw-r--r--   0 root         (0) root         (0)     9409 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/dbapi/test_portdb_cache.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/dep/
+-rw-r--r--   0 root         (0) root         (0)      169 2021-11-12 08:15:36.077467 portage-3.0.46/lib/portage/tests/dep/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.077467 portage-3.0.46/lib/portage/tests/dep/__test__.py
+-rw-r--r--   0 root         (0) root         (0)    24520 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/dep/testAtom.py
+-rw-r--r--   0 root         (0) root         (0)     9752 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/dep/testCheckRequiredUse.py
+-rw-r--r--   0 root         (0) root         (0)      779 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/dep/testExtendedAtomDict.py
+-rw-r--r--   0 root         (0) root         (0)     3769 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/dep/testExtractAffectingUSE.py
+-rw-r--r--   0 root         (0) root         (0)     1652 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/dep/testStandalone.py
+-rw-r--r--   0 root         (0) root         (0)     4452 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/dep/test_best_match_to_list.py
+-rw-r--r--   0 root         (0) root         (0)     1149 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_dep_getcpv.py
+-rw-r--r--   0 root         (0) root         (0)      988 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_dep_getrepo.py
+-rw-r--r--   0 root         (0) root         (0)      934 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_dep_getslot.py
+-rw-r--r--   0 root         (0) root         (0)     1402 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_dep_getusedeps.py
+-rw-r--r--   0 root         (0) root         (0)     2077 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_dnf_convert.py
+-rw-r--r--   0 root         (0) root         (0)     1237 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_get_operator.py
+-rw-r--r--   0 root         (0) root         (0)     1778 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_get_required_use_flags.py
+-rw-r--r--   0 root         (0) root         (0)     1009 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_isjustname.py
+-rw-r--r--   0 root         (0) root         (0)    11660 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_isvalidatom.py
+-rw-r--r--   0 root         (0) root         (0)    11132 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_match_from_list.py
+-rw-r--r--   0 root         (0) root         (0)     1572 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_overlap_dnf.py
+-rw-r--r--   0 root         (0) root         (0)     2661 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_paren_reduce.py
+-rw-r--r--   0 root         (0) root         (0)      790 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/dep/test_soname_atom_pickle.py
+-rw-r--r--   0 root         (0) root         (0)    27656 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/dep/test_use_reduce.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/ebuild/
+-rw-r--r--   0 root         (0) root         (0)      107 2021-11-12 08:15:36.080800 portage-3.0.46/lib/portage/tests/ebuild/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.080800 portage-3.0.46/lib/portage/tests/ebuild/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     1387 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/ebuild/test_array_fromfile_eof.py
+-rw-r--r--   0 root         (0) root         (0)    14001 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/ebuild/test_config.py
+-rw-r--r--   0 root         (0) root         (0)     5947 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/ebuild/test_doebuild_fd_pipes.py
+-rw-r--r--   0 root         (0) root         (0)     5167 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/ebuild/test_doebuild_spawn.py
+-rw-r--r--   0 root         (0) root         (0)    35283 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/ebuild/test_fetch.py
+-rw-r--r--   0 root         (0) root         (0)     6852 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/ebuild/test_ipc_daemon.py
+-rw-r--r--   0 root         (0) root         (0)     5211 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/ebuild/test_shell_quote.py
+-rw-r--r--   0 root         (0) root         (0)     1919 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/ebuild/test_spawn.py
+-rw-r--r--   0 root         (0) root         (0)     4479 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/ebuild/test_use_expand_incremental.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/emerge/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.080800 portage-3.0.46/lib/portage/tests/emerge/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.080800 portage-3.0.46/lib/portage/tests/emerge/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     1877 2022-12-24 02:35:49.845990 portage-3.0.46/lib/portage/tests/emerge/test_actions.py
+-rw-r--r--   0 root         (0) root         (0)    10290 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/emerge/test_config_protect.py
+-rw-r--r--   0 root         (0) root         (0)     6335 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/emerge/test_emerge_blocker_file_collision.py
+-rw-r--r--   0 root         (0) root         (0)     6615 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/emerge/test_emerge_slot_abi.py
+-rw-r--r--   0 root         (0) root         (0)     1320 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/emerge/test_global_updates.py
+-rw-r--r--   0 root         (0) root         (0)    26423 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/emerge/test_simple.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/env/
+-rw-r--r--   0 root         (0) root         (0)      169 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/env/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/env/__test__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/env/config/
+-rw-r--r--   0 root         (0) root         (0)      176 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/env/config/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/env/config/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     1164 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/env/config/test_PackageKeywordsFile.py
+-rw-r--r--   0 root         (0) root         (0)      818 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/env/config/test_PackageMaskFile.py
+-rw-r--r--   0 root         (0) root         (0)     1077 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/env/config/test_PackageUseFile.py
+-rw-r--r--   0 root         (0) root         (0)     1128 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/env/config/test_PortageModulesFile.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.584988 portage-3.0.46/lib/portage/tests/glsa/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/glsa/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/glsa/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     7173 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/glsa/test_security_set.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.588322 portage-3.0.46/lib/portage/tests/gpkg/
+-rw-r--r--   0 root         (0) root         (0)      102 2022-09-10 09:45:01.057050 portage-3.0.46/lib/portage/tests/gpkg/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2022-09-10 09:45:01.057050 portage-3.0.46/lib/portage/tests/gpkg/__test__.py
+-rw-r--r--   0 root         (0) root         (0)    13833 2022-09-20 03:21:13.396002 portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_checksum.py
+-rw-r--r--   0 root         (0) root         (0)    15728 2022-09-20 03:21:13.396002 portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_gpg.py
+-rw-r--r--   0 root         (0) root         (0)     1899 2022-09-20 03:21:13.396002 portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_metadata_update.py
+-rw-r--r--   0 root         (0) root         (0)     5288 2022-09-20 03:21:13.396002 portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_metadata_url.py
+-rw-r--r--   0 root         (0) root         (0)    14745 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_path.py
+-rw-r--r--   0 root         (0) root         (0)     1868 2022-09-20 03:21:13.396002 portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_size.py
+-rw-r--r--   0 root         (0) root         (0)     3305 2022-09-20 03:21:13.396002 portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_stream.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.588322 portage-3.0.46/lib/portage/tests/lafilefixer/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/lafilefixer/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/lafilefixer/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     6338 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/lafilefixer/test_lafilefixer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.588322 portage-3.0.46/lib/portage/tests/lazyimport/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/lazyimport/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.084133 portage-3.0.46/lib/portage/tests/lazyimport/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     2824 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/lazyimport/test_lazy_import_portage_baseline.py
+-rw-r--r--   0 root         (0) root         (0)      596 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/lazyimport/test_preload_portage_submodules.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.588322 portage-3.0.46/lib/portage/tests/lint/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/lint/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/lint/__test__.py
+-rw-r--r--   0 root         (0) root         (0)      214 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/lint/metadata.py
+-rw-r--r--   0 root         (0) root         (0)     2345 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/lint/test_bash_syntax.py
+-rw-r--r--   0 root         (0) root         (0)     3031 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/lint/test_compile_modules.py
+-rw-r--r--   0 root         (0) root         (0)     1516 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/lint/test_import_modules.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.588322 portage-3.0.46/lib/portage/tests/locks/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/locks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/locks/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     7850 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/locks/test_asynchronous_lock.py
+-rw-r--r--   0 root         (0) root         (0)     2763 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/locks/test_lock_nonblock.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.588322 portage-3.0.46/lib/portage/tests/news/
+-rw-r--r--   0 root         (0) root         (0)      170 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/news/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/news/__test__.py
+-rw-r--r--   0 root         (0) root         (0)    14363 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/news/test_NewsItem.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.588322 portage-3.0.46/lib/portage/tests/process/
+-rw-r--r--   0 root         (0) root         (0)      107 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/process/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.087467 portage-3.0.46/lib/portage/tests/process/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     2016 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/process/test_AsyncFunction.py
+-rw-r--r--   0 root         (0) root         (0)     2332 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/process/test_PipeLogger.py
+-rw-r--r--   0 root         (0) root         (0)     3121 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/process/test_PopenProcess.py
+-rw-r--r--   0 root         (0) root         (0)     2366 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/process/test_PopenProcessBlockingIO.py
+-rw-r--r--   0 root         (0) root         (0)     3737 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/process/test_poll.py
+-rw-r--r--   0 root         (0) root         (0)     1137 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/process/test_spawn_fail_e2big.py
+-rw-r--r--   0 root         (0) root         (0)     1341 2023-03-21 03:50:18.060757 portage-3.0.46/lib/portage/tests/process/test_spawn_warn_large_env.py
+-rw-r--r--   0 root         (0) root         (0)     1178 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/process/test_unshare_net.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/resolver/
+-rw-r--r--   0 root         (0) root         (0)    42502 2023-03-21 03:50:18.064091 portage-3.0.46/lib/portage/tests/resolver/ResolverPlayground.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.104133 portage-3.0.46/lib/portage/tests/resolver/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.104133 portage-3.0.46/lib/portage/tests/resolver/__test__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/resolver/binpkg_multi_instance/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.104133 portage-3.0.46/lib/portage/tests/resolver/binpkg_multi_instance/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.104133 portage-3.0.46/lib/portage/tests/resolver/binpkg_multi_instance/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     5585 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/binpkg_multi_instance/test_build_id_profile_format.py
+-rw-r--r--   0 root         (0) root         (0)     3747 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/binpkg_multi_instance/test_rebuilt_binaries.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/resolver/soname/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/resolver/soname/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/resolver/soname/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     3931 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_autounmask.py
+-rw-r--r--   0 root         (0) root         (0)     1755 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_depclean.py
+-rw-r--r--   0 root         (0) root         (0)     8528 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_downgrade.py
+-rw-r--r--   0 root         (0) root         (0)     3840 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_or_choices.py
+-rw-r--r--   0 root         (0) root         (0)     3305 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_reinstall.py
+-rw-r--r--   0 root         (0) root         (0)     3338 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_skip_update.py
+-rw-r--r--   0 root         (0) root         (0)    12877 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_slot_conflict_reinstall.py
+-rw-r--r--   0 root         (0) root         (0)     3971 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_slot_conflict_update.py
+-rw-r--r--   0 root         (0) root         (0)     2944 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_soname_provided.py
+-rw-r--r--   0 root         (0) root         (0)     2778 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/soname/test_unsatisfiable.py
+-rw-r--r--   0 root         (0) root         (0)     3354 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/soname/test_unsatisfied.py
+-rw-r--r--   0 root         (0) root         (0)     2824 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_aggressive_backtrack_downgrade.py
+-rw-r--r--   0 root         (0) root         (0)    28432 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_autounmask.py
+-rw-r--r--   0 root         (0) root         (0)     2732 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_autounmask_binpkg_use.py
+-rw-r--r--   0 root         (0) root         (0)     2176 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_autounmask_keep_keywords.py
+-rw-r--r--   0 root         (0) root         (0)     3098 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_autounmask_multilib_use.py
+-rw-r--r--   0 root         (0) root         (0)     1279 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_autounmask_parent.py
+-rw-r--r--   0 root         (0) root         (0)     2573 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_autounmask_use_backtrack.py
+-rw-r--r--   0 root         (0) root         (0)     3743 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_autounmask_use_breakage.py
+-rw-r--r--   0 root         (0) root         (0)     1830 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/resolver/test_autounmask_use_slot_conflict.py
+-rw-r--r--   0 root         (0) root         (0)     5786 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/resolver/test_backtracking.py
+-rw-r--r--   0 root         (0) root         (0)     6805 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_bdeps.py
+-rw-r--r--   0 root         (0) root         (0)     4927 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_binary_pkg_ebuild_visibility.py
+-rw-r--r--   0 root         (0) root         (0)     4231 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/resolver/test_blocker.py
+-rw-r--r--   0 root         (0) root         (0)     4330 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_changed_deps.py
+-rw-r--r--   0 root         (0) root         (0)     7899 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_circular_choices.py
+-rw-r--r--   0 root         (0) root         (0)     3341 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_circular_choices_rust.py
+-rw-r--r--   0 root         (0) root         (0)     4832 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_circular_dependencies.py
+-rw-r--r--   0 root         (0) root         (0)     4948 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_complete_graph.py
+-rw-r--r--   0 root         (0) root         (0)     2910 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_complete_if_new_subslot_without_revbump.py
+-rw-r--r--   0 root         (0) root         (0)     9959 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_depclean.py
+-rw-r--r--   0 root         (0) root         (0)     1690 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_depclean_order.py
+-rw-r--r--   0 root         (0) root         (0)     2443 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_depclean_slot_unavailable.py
+-rw-r--r--   0 root         (0) root         (0)    13128 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_depth.py
+-rw-r--r--   0 root         (0) root         (0)     3329 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_disjunctive_depend_order.py
+-rw-r--r--   0 root         (0) root         (0)     9983 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_eapi.py
+-rw-r--r--   0 root         (0) root         (0)     2658 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_features_test_use.py
+-rw-r--r--   0 root         (0) root         (0)     3379 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_imagemagick_graphicsmagick.py
+-rw-r--r--   0 root         (0) root         (0)     3457 2022-09-10 09:45:01.057050 portage-3.0.46/lib/portage/tests/resolver/test_installkernel.py
+-rw-r--r--   0 root         (0) root         (0)    11063 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_keywords.py
+-rw-r--r--   0 root         (0) root         (0)    31088 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_merge_order.py
+-rw-r--r--   0 root         (0) root         (0)     1234 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_missing_iuse_and_evaluated_atoms.py
+-rw-r--r--   0 root         (0) root         (0)    15920 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_multirepo.py
+-rw-r--r--   0 root         (0) root         (0)     1772 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/resolver/test_multislot.py
+-rw-r--r--   0 root         (0) root         (0)     1554 2022-09-10 09:44:56.963689 portage-3.0.46/lib/portage/tests/resolver/test_old_dep_chain_display.py
+-rw-r--r--   0 root         (0) root         (0)     1142 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_onlydeps.py
+-rw-r--r--   0 root         (0) root         (0)     1527 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_onlydeps_circular.py
+-rw-r--r--   0 root         (0) root         (0)     5933 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_onlydeps_ideps.py
+-rw-r--r--   0 root         (0) root         (0)     2552 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_onlydeps_minimal.py
+-rw-r--r--   0 root         (0) root         (0)    25072 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_or_choices.py
+-rw-r--r--   0 root         (0) root         (0)     2716 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_or_downgrade_installed.py
+-rw-r--r--   0 root         (0) root         (0)     6850 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_or_upgrade_installed.py
+-rw-r--r--   0 root         (0) root         (0)     3911 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_output.py
+-rw-r--r--   0 root         (0) root         (0)     9049 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_package_tracker.py
+-rw-r--r--   0 root         (0) root         (0)     4568 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_profile_default_eapi.py
+-rw-r--r--   0 root         (0) root         (0)     3353 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_profile_package_set.py
+-rw-r--r--   0 root         (0) root         (0)     6911 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_rebuild.py
+-rw-r--r--   0 root         (0) root         (0)     2409 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_regular_slot_change_without_revbump.py
+-rw-r--r--   0 root         (0) root         (0)    11792 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_required_use.py
+-rw-r--r--   0 root         (0) root         (0)     2640 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_runtime_cycle_merge_order.py
+-rw-r--r--   0 root         (0) root         (0)     3500 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_simple.py
+-rw-r--r--   0 root         (0) root         (0)    18128 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_abi.py
+-rw-r--r--   0 root         (0) root         (0)     8790 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_abi_downgrade.py
+-rw-r--r--   0 root         (0) root         (0)     3488 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_change_without_revbump.py
+-rw-r--r--   0 root         (0) root         (0)    13393 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_collisions.py
+-rw-r--r--   0 root         (0) root         (0)     1990 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_force_rebuild.py
+-rw-r--r--   0 root         (0) root         (0)     1432 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_mask_update.py
+-rw-r--r--   0 root         (0) root         (0)    14826 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_rebuild.py
+-rw-r--r--   0 root         (0) root         (0)     7910 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_unsatisfied_deep_deps.py
+-rw-r--r--   0 root         (0) root         (0)     2579 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_update.py
+-rw-r--r--   0 root         (0) root         (0)     2491 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_update_virt.py
+-rw-r--r--   0 root         (0) root         (0)     5024 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_autounmask.py
+-rw-r--r--   0 root         (0) root         (0)     7642 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_bdeps.py
+-rw-r--r--   0 root         (0) root         (0)     4350 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_complete_graph.py
+-rw-r--r--   0 root         (0) root         (0)     4694 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_exclusive_slots.py
+-rw-r--r--   0 root         (0) root         (0)     4366 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_missed_update.py
+-rw-r--r--   0 root         (0) root         (0)     3719 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_rebuild.py
+-rw-r--r--   0 root         (0) root         (0)     1682 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_required_use.py
+-rw-r--r--   0 root         (0) root         (0)     9190 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_reverse_deps.py
+-rw-r--r--   0 root         (0) root         (0)     3974 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_runtime_pkg_mask.py
+-rw-r--r--   0 root         (0) root         (0)     2103 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_unsatisfied.py
+-rw-r--r--   0 root         (0) root         (0)     3518 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_unsolved.py
+-rw-r--r--   0 root         (0) root         (0)     2107 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_update_probe_parent_downgrade.py
+-rw-r--r--   0 root         (0) root         (0)     1819 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_solve_non_slot_operator_slot_conflicts.py
+-rw-r--r--   0 root         (0) root         (0)     3584 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/tests/resolver/test_targetroot.py
+-rw-r--r--   0 root         (0) root         (0)     1571 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/tests/resolver/test_unecessary_slot_upgrade.py
+-rw-r--r--   0 root         (0) root         (0)    11321 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/tests/resolver/test_unmerge_order.py
+-rw-r--r--   0 root         (0) root         (0)     3843 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_update.py
+-rw-r--r--   0 root         (0) root         (0)     1827 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_use_dep_defaults.py
+-rw-r--r--   0 root         (0) root         (0)     5326 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_useflags.py
+-rw-r--r--   0 root         (0) root         (0)     9976 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_virtual_minimize_children.py
+-rw-r--r--   0 root         (0) root         (0)     9326 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/resolver/test_virtual_slot.py
+-rw-r--r--   0 root         (0) root         (0)     2910 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/resolver/test_with_test_deps.py
+-rwxr-xr-x   0 root         (0) root         (0)     2100 2023-03-21 03:50:18.064091 portage-3.0.46/lib/portage/tests/runTests.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/sets/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/__test__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/sets/base/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/base/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/base/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     2051 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/sets/base/testInternalPackageSet.py
+-rw-r--r--   0 root         (0) root         (0)     1029 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/sets/base/testVariableSet.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/sets/files/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/files/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/files/__test__.py
+-rw-r--r--   0 root         (0) root         (0)      992 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/sets/files/testConfigFileSet.py
+-rw-r--r--   0 root         (0) root         (0)      829 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/sets/files/testStaticFileSet.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/sets/shell/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/shell/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sets/shell/__test__.py
+-rw-r--r--   0 root         (0) root         (0)      790 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/sets/shell/testShell.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/sync/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sync/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/sync/__test__.py
+-rw-r--r--   0 root         (0) root         (0)    16481 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/sync/test_sync_local.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/unicode/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/unicode/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.107466 portage-3.0.46/lib/portage/tests/unicode/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     2294 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/unicode/test_string_format.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/update/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.110799 portage-3.0.46/lib/portage/tests/update/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.110799 portage-3.0.46/lib/portage/tests/update/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     4462 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/update/test_move_ent.py
+-rw-r--r--   0 root         (0) root         (0)     5444 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/update/test_move_slot_ent.py
+-rw-r--r--   0 root         (0) root         (0)    11460 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/update/test_update_dbentry.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/util/
+-rw-r--r--   0 root         (0) root         (0)      170 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/__test__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/util/dyn_libs/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/dyn_libs/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/dyn_libs/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     1389 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/util/dyn_libs/test_soname_deps.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/util/eventloop/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/eventloop/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/eventloop/__test__.py
+-rw-r--r--   0 root         (0) root         (0)      826 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/eventloop/test_call_soon_fifo.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/util/file_copy/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/file_copy/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/file_copy/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     2169 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/file_copy/test_copyfile.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.591655 portage-3.0.46/lib/portage/tests/util/futures/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/futures/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.114133 portage-3.0.46/lib/portage/tests/util/futures/__test__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/tests/util/futures/asyncio/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.46/lib/portage/tests/util/futures/asyncio/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.46/lib/portage/tests/util/futures/asyncio/__test__.py
+-rw-r--r--   0 root         (0) root         (0)     1789 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_child_watcher.py
+-rw-r--r--   0 root         (0) root         (0)     2025 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_event_loop_in_fork.py
+-rw-r--r--   0 root         (0) root         (0)     5394 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_pipe_closed.py
+-rw-r--r--   0 root         (0) root         (0)      795 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_policy_wrapper_recursion.py
+-rw-r--r--   0 root         (0) root         (0)     1394 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_run_until_complete.py
+-rw-r--r--   0 root         (0) root         (0)     6912 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_subprocess_exec.py
+-rw-r--r--   0 root         (0) root         (0)     2344 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_wakeup_fd_sigchld.py
+-rw-r--r--   0 root         (0) root         (0)     7135 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/futures/test_compat_coroutine.py
+-rw-r--r--   0 root         (0) root         (0)     1274 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/futures/test_done_callback.py
+-rw-r--r--   0 root         (0) root         (0)     1565 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/util/futures/test_done_callback_after_exit.py
+-rw-r--r--   0 root         (0) root         (0)     2883 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/futures/test_iter_completed.py
+-rw-r--r--   0 root         (0) root         (0)    10828 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/futures/test_retry.py
+-rw-r--r--   0 root         (0) root         (0)     5805 2023-03-21 03:50:18.064091 portage-3.0.46/lib/portage/tests/util/test_checksum.py
+-rw-r--r--   0 root         (0) root         (0)    11345 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/test_digraph.py
+-rw-r--r--   0 root         (0) root         (0)     1824 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/test_file_copier.py
+-rw-r--r--   0 root         (0) root         (0)     3534 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/test_getconfig.py
+-rw-r--r--   0 root         (0) root         (0)      315 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/util/test_grabdict.py
+-rw-r--r--   0 root         (0) root         (0)     5805 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/test_install_mask.py
+-rw-r--r--   0 root         (0) root         (0)     1120 2022-12-24 02:35:49.845990 portage-3.0.46/lib/portage/tests/util/test_manifest.py
+-rw-r--r--   0 root         (0) root         (0)    10489 2022-09-10 09:45:01.057050 portage-3.0.46/lib/portage/tests/util/test_mtimedb.py
+-rw-r--r--   0 root         (0) root         (0)      440 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/test_normalizedPath.py
+-rw-r--r--   0 root         (0) root         (0)     1735 2023-04-02 19:17:09.550903 portage-3.0.46/lib/portage/tests/util/test_shelve.py
+-rw-r--r--   0 root         (0) root         (0)     6638 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/test_socks5.py
+-rw-r--r--   0 root         (0) root         (0)      832 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/util/test_stackDictList.py
+-rw-r--r--   0 root         (0) root         (0)     1185 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/tests/util/test_stackDicts.py
+-rw-r--r--   0 root         (0) root         (0)      715 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/test_stackLists.py
+-rw-r--r--   0 root         (0) root         (0)      897 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/tests/util/test_uniqueArray.py
+-rw-r--r--   0 root         (0) root         (0)     3347 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/test_varExpand.py
+-rw-r--r--   0 root         (0) root         (0)     1450 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/test_whirlpool.py
+-rw-r--r--   0 root         (0) root         (0)     6243 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/util/test_xattr.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/tests/versions/
+-rw-r--r--   0 root         (0) root         (0)      174 2021-11-12 08:15:36.117466 portage-3.0.46/lib/portage/tests/versions/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.46/lib/portage/tests/versions/__test__.py
+-rw-r--r--   0 root         (0) root         (0)      555 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/versions/test_cpv_sort_key.py
+-rw-r--r--   0 root         (0) root         (0)     3026 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/versions/test_vercmp.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/tests/xpak/
+-rw-r--r--   0 root         (0) root         (0)      169 2021-11-12 08:15:36.117466 portage-3.0.46/lib/portage/tests/xpak/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.117466 portage-3.0.46/lib/portage/tests/xpak/__test__.py
+-rw-r--r--   0 root         (0) root         (0)      427 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/tests/xpak/test_decodeint.py
+-rw-r--r--   0 root         (0) root         (0)    17014 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/update.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/
+-rw-r--r--   0 root         (0) root         (0)     3063 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/ExtractKernelVersion.py
+-rw-r--r--   0 root         (0) root         (0)     2141 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/SlotObject.py
+-rw-r--r--   0 root         (0) root         (0)    68707 2023-03-21 03:50:18.064091 portage-3.0.46/lib/portage/util/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/_async/
+-rw-r--r--   0 root         (0) root         (0)     2609 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/_async/AsyncFunction.py
+-rw-r--r--   0 root         (0) root         (0)     3393 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/_async/AsyncScheduler.py
+-rw-r--r--   0 root         (0) root         (0)      963 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/_async/AsyncTaskFuture.py
+-rw-r--r--   0 root         (0) root         (0)     4785 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/_async/BuildLogger.py
+-rw-r--r--   0 root         (0) root         (0)     1103 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/_async/FileCopier.py
+-rw-r--r--   0 root         (0) root         (0)     2486 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/_async/FileDigester.py
+-rw-r--r--   0 root         (0) root         (0)     5953 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_async/ForkProcess.py
+-rw-r--r--   0 root         (0) root         (0)     7527 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_async/PipeLogger.py
+-rw-r--r--   0 root         (0) root         (0)     2676 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_async/PipeReaderBlockingIO.py
+-rw-r--r--   0 root         (0) root         (0)     1076 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_async/PopenProcess.py
+-rw-r--r--   0 root         (0) root         (0)     4501 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_async/SchedulerInterface.py
+-rw-r--r--   0 root         (0) root         (0)      644 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/_async/TaskScheduler.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.127466 portage-3.0.46/lib/portage/util/_async/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1360 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/_async/run_main_scheduler.py
+-rw-r--r--   0 root         (0) root         (0)     4347 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/_compare_files.py
+-rw-r--r--   0 root         (0) root         (0)     1219 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/_ctypes.py
+-rw-r--r--   0 root         (0) root         (0)     2654 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/_desktop_entry.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/_dyn_libs/
+-rw-r--r--   0 root         (0) root         (0)    41425 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_dyn_libs/LinkageMapELF.py
+-rw-r--r--   0 root         (0) root         (0)     2877 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/_dyn_libs/NeededEntry.py
+-rw-r--r--   0 root         (0) root         (0)     9385 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_dyn_libs/PreservedLibsRegistry.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.130799 portage-3.0.46/lib/portage/util/_dyn_libs/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3834 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_dyn_libs/display_preserved_libs.py
+-rw-r--r--   0 root         (0) root         (0)     1070 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/_dyn_libs/dyn_libs.py
+-rw-r--r--   0 root         (0) root         (0)     6203 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_dyn_libs/soname_deps.py
+-rw-r--r--   0 root         (0) root         (0)     3722 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_dyn_libs/soname_deps_qa.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/_eventloop/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.134132 portage-3.0.46/lib/portage/util/_eventloop/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5849 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/_eventloop/asyncio_event_loop.py
+-rw-r--r--   0 root         (0) root         (0)      213 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/_eventloop/global_event_loop.py
+-rw-r--r--   0 root         (0) root         (0)     3029 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_get_vm_info.py
+-rw-r--r--   0 root         (0) root         (0)     5956 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/_info_files.py
+-rw-r--r--   0 root         (0) root         (0)      692 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/_path.py
+-rw-r--r--   0 root         (0) root         (0)     2530 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/_pty.py
+-rw-r--r--   0 root         (0) root         (0)     4032 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/util/_urlopen.py
+-rw-r--r--   0 root         (0) root         (0)     7063 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/_xattr.py
+-rw-r--r--   0 root         (0) root         (0)     1528 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/backoff.py
+-rw-r--r--   0 root         (0) root         (0)     1133 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/bin_entry_point.py
+-rw-r--r--   0 root         (0) root         (0)     2189 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/changelog.py
+-rw-r--r--   0 root         (0) root         (0)     3464 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/compression_probe.py
+-rw-r--r--   0 root         (0) root         (0)     2403 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/configparser.py
+-rw-r--r--   0 root         (0) root         (0)     2180 2022-12-24 02:35:49.845990 portage-3.0.46/lib/portage/util/cpuinfo.py
+-rw-r--r--   0 root         (0) root         (0)    12975 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/digraph.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/elf/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.137466 portage-3.0.46/lib/portage/util/elf/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1345 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/elf/constants.py
+-rw-r--r--   0 root         (0) root         (0)     1889 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/elf/header.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/endian/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.137466 portage-3.0.46/lib/portage/util/endian/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1303 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/endian/decode.py
+-rw-r--r--   0 root         (0) root         (0)    15592 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/env_update.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/file_copy/
+-rw-r--r--   0 root         (0) root         (0)      909 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/file_copy/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2118 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/formatter.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/futures/
+-rw-r--r--   0 root         (0) root         (0)      180 2022-09-10 09:44:56.967023 portage-3.0.46/lib/portage/util/futures/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/futures/_asyncio/
+-rw-r--r--   0 root         (0) root         (0)     9758 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/futures/_asyncio/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3016 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/futures/_asyncio/streams.py
+-rw-r--r--   0 root         (0) root         (0)     1854 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/futures/_sync_decorator.py
+-rw-r--r--   0 root         (0) root         (0)     4942 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/futures/compat_coroutine.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/futures/executor/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-11-12 08:15:36.140799 portage-3.0.46/lib/portage/util/futures/executor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4306 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/futures/executor/fork.py
+-rw-r--r--   0 root         (0) root         (0)     2831 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/futures/extendedfutures.py
+-rw-r--r--   0 root         (0) root         (0)      516 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/futures/futures.py
+-rw-r--r--   0 root         (0) root         (0)     6868 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/futures/iter_completed.py
+-rw-r--r--   0 root         (0) root         (0)     6297 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/futures/retry.py
+-rw-r--r--   0 root         (0) root         (0)     2237 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/futures/unix_events.py
+-rw-r--r--   0 root         (0) root         (0)     1584 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/hooks.py
+-rw-r--r--   0 root         (0) root         (0)     6549 2022-09-10 09:45:01.060384 portage-3.0.46/lib/portage/util/install_mask.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/util/iterators/
+-rw-r--r--   0 root         (0) root         (0)     2996 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/iterators/MultiIterGroupBy.py
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.144132 portage-3.0.46/lib/portage/util/iterators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7349 2022-09-10 09:45:01.063717 portage-3.0.46/lib/portage/util/lafilefixer.py
+-rw-r--r--   0 root         (0) root         (0)     4814 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/listdir.py
+-rw-r--r--   0 root         (0) root         (0)     4339 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/locale.py
+-rw-r--r--   0 root         (0) root         (0)    13909 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/movefile.py
+-rw-r--r--   0 root         (0) root         (0)     4258 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/mtimedb.py
+-rw-r--r--   0 root         (0) root         (0)     2990 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/netlink.py
+-rw-r--r--   0 root         (0) root         (0)     1336 2022-09-10 09:44:56.970356 portage-3.0.46/lib/portage/util/path.py
+-rw-r--r--   0 root         (0) root         (0)     1527 2022-09-10 09:45:01.057050 portage-3.0.46/lib/portage/util/shelve.py
+-rw-r--r--   0 root         (0) root         (0)     3635 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/socks5.py
+-rw-r--r--   0 root         (0) root         (0)    58416 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/util/whirlpool.py
+-rw-r--r--   0 root         (0) root         (0)     4506 2023-03-21 03:35:23.553538 portage-3.0.46/lib/portage/util/writeable_check.py
+-rw-r--r--   0 root         (0) root         (0)    19275 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/versions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/lib/portage/xml/
+-rw-r--r--   0 root         (0) root         (0)      102 2021-11-12 08:15:36.147466 portage-3.0.46/lib/portage/xml/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    16789 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/xml/metadata.py
+-rw-r--r--   0 root         (0) root         (0)    19413 2023-03-21 03:35:23.556871 portage-3.0.46/lib/portage/xpak.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/misc/
+-rwxr-xr-x   0 root         (0) root         (0)    24116 2023-02-03 18:03:13.736861 portage-3.0.46/misc/emerge-delta-webrsync
+-rwxr-xr-x   0 root         (0) root         (0)    29953 2023-04-07 09:54:54.254527 portage-3.0.46/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:56:10.594988 portage-3.0.46/src/
+-rw-r--r--   0 root         (0) root         (0)    71291 2023-03-21 03:35:23.556871 portage-3.0.46/src/portage_util__whirlpool.c
+-rw-r--r--   0 root         (0) root         (0)    13384 2023-03-21 03:35:23.556871 portage-3.0.46/src/portage_util_file_copy_reflink_linux.c
+-rw-r--r--   0 root         (0) root         (0)     1276 2023-03-21 03:35:23.556871 portage-3.0.46/src/portage_util_libc.c
```

### Comparing `portage-3.0.45.3/DEVELOPING` & `portage-3.0.46/DEVELOPING`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/LICENSE` & `portage-3.0.46/LICENSE`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/PKG-INFO` & `portage-3.0.46/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: portage
-Version: 3.0.45.3
+Version: 3.0.46
 Summary: Portage is the package management and distribution system for Gentoo
 Home-page: https://wiki.gentoo.org/wiki/Project:Portage
 Author: Gentoo Portage Development Team
 Author-email: dev-portage@gentoo.org
 License: GPLV2
 Project-URL: Release Notes, https://gitweb.gentoo.org/proj/portage.git/plain/NEWS
 Project-URL: Documentation, https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage
```

### Comparing `portage-3.0.45.3/TEST-NOTES` & `portage-3.0.46/TEST-NOTES`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/archive-conf` & `portage-3.0.46/bin/archive-conf`

 * *Files 10% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 #
 # archive-conf -- save off a config file in the dispatch-conf archive dir
 #
 #  Written by Wayne Davison <gentoo@blorf.net> with code snagged from
 #  Jeremy Wohl's dispatch-conf script and the portage chkcontents script.
 #
 
+import subprocess
 import sys
 
 from os import path as osp
 
 if osp.isfile(
     osp.join(osp.dirname(osp.dirname(osp.realpath(__file__))), ".portage_not_installed")
 ):
@@ -23,16 +24,14 @@
 
 portage._internal_caller = True
 
 import portage.dispatch_conf
 from portage import os
 from portage.checksum import perform_md5
 
-FIND_EXTANT_CONTENTS = "find %s -name CONTENTS"
-
 MANDATORY_OPTS = ["archive-dir"]
 
 
 def archive_conf():
     args = []
     content_files = []
     md5_match_hash = {}
@@ -41,20 +40,22 @@
 
     for conf in sys.argv[1:]:
         if not os.path.isabs(conf):
             conf = os.path.abspath(conf)
         args += [conf]
         md5_match_hash[conf] = ""
 
-    # Find all the CONTENT files in VDB_PATH.
-    with os.popen(
-        FIND_EXTANT_CONTENTS
-        % (os.path.join(portage.settings["EROOT"], portage.VDB_PATH))
-    ) as f:
-        content_files += f.readlines()
+    # Find all the CONTENTS files in VDB_PATH.
+    eroot_vdb_path = os.path.join(portage.settings["EROOT"], portage.VDB_PATH)
+    find = subprocess.run(
+        ["find", eroot_vdb_path, "-type", "f", "-name", "CONTENTS"],
+        capture_output=True,
+        text=True,
+    )
+    content_files += find.stdout.splitlines()
 
     # Search for the saved md5 checksum of all the specified config files
     # and see if the current file is unmodified or not.
     try:
         todo_cnt = len(args)
         for filename in content_files:
             filename = filename.rstrip()
```

### Comparing `portage-3.0.45.3/bin/bashrc-functions.sh` & `portage-3.0.46/bin/bashrc-functions.sh`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/binhost-snapshot` & `portage-3.0.46/bin/binhost-snapshot`

 * *Files 16% similar despite different names*

```diff
@@ -88,23 +88,21 @@
     parse_result = urlparse(snapshot_uri)
     if not (parse_result.scheme and parse_result.netloc and parse_result.path):
         parser.error(f"snapshot_uri is not a valid URI: '{snapshot_uri}'")
 
     if os.path.isdir(snapshot_dir):
         parser.error(f"snapshot_dir already exists: '{snapshot_dir}'")
 
+    dirname_ss_dir = os.path.dirname(snapshot_dir)
     try:
-        os.makedirs(os.path.dirname(snapshot_dir))
+        os.makedirs(dirname_ss_dir)
     except OSError:
         pass
-    if not os.path.isdir(os.path.dirname(snapshot_dir)):
-        parser.error(
-            "snapshot_dir parent could not be created: '%s'"
-            % os.path.dirname(snapshot_dir)
-        )
+    if not os.path.isdir(dirname_ss_dir):
+        parser.error(f"snapshot_dir parent could not be created: '{dirname_ss_dir}'")
 
     try:
         os.makedirs(binhost_dir)
     except OSError:
         pass
     if not os.path.isdir(binhost_dir):
         parser.error(f"binhost_dir could not be created: '{binhost_dir}'")
```

### Comparing `portage-3.0.45.3/bin/chmod-lite.py` & `portage-3.0.46/bin/chmod-lite.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/chpathtool.py` & `portage-3.0.46/bin/chpathtool.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/clean_locks` & `portage-3.0.46/bin/clean_locks`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/dispatch-conf` & `portage-3.0.46/bin/dispatch-conf`

 * *Files 4% similar despite different names*

```diff
@@ -44,22 +44,16 @@
     diff_mixed_wrapper,
     perform_conf_update_hooks,
     perform_conf_update_session_hooks,
 )
 from portage.process import find_binary, spawn
 from portage.util import writemsg, writemsg_stdout
 
-FIND_EXTANT_CONFIGS = (
-    "find '%s' %s -name '._cfg????_%s' ! -name '.*~' ! -iname '.*.bak' -print"
-)
 DIFF_CONTENTS = "diff -Nu '%s' '%s'"
 
-if "case-insensitive-fs" in portage.settings.features:
-    FIND_EXTANT_CONFIGS = FIND_EXTANT_CONFIGS.replace("-name '._cfg", "-iname '._cfg")
-
 # We need a secure scratch dir and python does silly verbose errors on the use of tempnam
 oldmask = os.umask(0o077)
 SCRATCH_DIR = None
 while SCRATCH_DIR is None:
     try:
         mydir = "/tmp/dispatch-conf."
         for x in range(0, 8):
@@ -156,26 +150,37 @@
 
             # Protect files that don't exist (bug #523684). If the
             # parent directory doesn't exist, we can safely skip it.
             if not os.path.isdir(os.path.dirname(path)):
                 continue
 
             basename = "*"
-            find_opts = "-name '.*' -type d -prune -o"
+            find_opts = ["-name", ".*", "-type", "d", "-prune", "-o"]
             if not os.path.isdir(path):
                 path, basename = os.path.split(path)
-                find_opts = "-maxdepth 1"
+                find_opts = ["-maxdepth", "1"]
+            if "case-insensitive-fs" in portage.settings.features:
+                find_opts += ["-iname"]
+            else:
+                find_opts += ["-name"]
+            find_opts += [
+                f"._cfg????_{basename}",
+                "!",
+                "-name",
+                ".*~",
+                "!",
+                "-iname",
+                ".*.bak",
+                "-print",
+            ]
 
             try:
+                # Find existing configs
                 path_list = _unicode_decode(
-                    subprocess.check_output(
-                        portage.util.shlex_split(
-                            FIND_EXTANT_CONFIGS % (path, find_opts, basename)
-                        )
-                    ),
+                    subprocess.check_output(["find", path] + find_opts),
                     errors="strict",
                 ).splitlines()
             except subprocess.CalledProcessError:
                 pass
             else:
                 confs.extend(self.massage(path_list))
 
@@ -336,15 +341,15 @@
                     diff_pager(conf["new"], mrgconf)
                     show_new_diff = 0
                 else:
                     diff_pager(conf["current"], newconf)
 
                 print()
                 writemsg_stdout(
-                    ">> (%i of %i) -- %s\n" % (count, len(confs), conf["current"]),
+                    f">> ({count} of {len(confs)}) -- {conf['current']}\n",
                     noiselevel=-1,
                 )
                 print(
                     ">> q quit, h help, n next, e edit-new, z zap-new, u use-new\n   m merge, t toggle-merge, l look-merge: ",
                     end=" ",
                 )
 
@@ -440,16 +445,15 @@
 
         perform_conf_update_hooks("pre-update", curconf)
 
         try:
             os.rename(newconf, curconf)
         except (OSError, os.error) as why:
             writemsg(
-                "dispatch-conf: Error renaming %s to %s: %s; fatal\n"
-                % (newconf, curconf, str(why)),
+                f"dispatch-conf: Error renaming {newconf} to {curconf}: {str(why)}; fatal\n",
                 noiselevel=-1,
             )
             return
 
         perform_conf_update_hooks("post-update", curconf)
 
     def post_process(self, curconf):
```

### Comparing `portage-3.0.45.3/bin/dohtml.py` & `portage-3.0.46/bin/dohtml.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/doins.py` & `portage-3.0.46/bin/doins.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/eapi.sh` & `portage-3.0.46/bin/eapi.sh`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/eapi7-ver-funcs.sh` & `portage-3.0.46/bin/eapi7-ver-funcs.sh`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild` & `portage-3.0.46/bin/ebuild`

 * *Files 2% similar despite different names*

```diff
@@ -63,15 +63,14 @@
     import portage.util
     from portage.util._eventloop.global_event_loop import global_event_loop
     from _emerge.actions import apply_priorities
     from _emerge.Package import Package
     from _emerge.RootConfig import RootConfig
 
     portage.process.sanitize_fds()
-
     description = "See the ebuild(1) man page for more info"
     usage = "Usage: ebuild <ebuild file> <command> [command] ..."
     parser = argparse.ArgumentParser(description=description, usage=usage)
 
     force_help = (
         "When used together with the digest or manifest "
         + "command, this option forces regeneration of digests for all "
@@ -124,22 +123,22 @@
 
     # do this _after_ 'import portage' to prevent unnecessary tracing
     if debug and "python-trace" in portage.features:
         portage.debug.set_trace(True)
 
     if not opts.color == "y" and (
         opts.color == "n"
-        or portage.settings.get("NOCOLOR") in ("yes", "true")
+        or portage.util.no_color(portage.settings)
         or portage.settings.get("TERM") == "dumb"
         or not sys.stdout.isatty()
     ):
         portage.output.nocolor()
         portage.settings.unlock()
-        portage.settings["NOCOLOR"] = "true"
-        portage.settings.backup_changes("NOCOLOR")
+        portage.settings["NO_COLOR"] = "true"
+        portage.settings.backup_changes("NO_COLOR")
         portage.settings.lock()
 
     apply_priorities(portage.settings)
 
     ebuild = pargs.pop(0)
 
     pf = None
@@ -373,17 +372,17 @@
         ):
             portage.doebuild_environment(
                 ebuild, "setup", portage.root, tmpsettings, debug, 1, portage.portdb
             )
             env_filename = os.path.join(tmpsettings["T"], "environment")
             if os.path.exists(env_filename):
                 msg = (
-                    "Existing ${T}/environment for '%s' will be sourced. "
-                    + "Run 'clean' to start with a fresh environment."
-                ) % (tmpsettings["PF"],)
+                    f"Existing ${{T}}/environment for '{tmpsettings['PF']}' will be sourced. "
+                    "Run 'clean' to start with a fresh environment."
+                )
                 msg = textwrap.wrap(msg, 70)
                 for x in msg:
                     portage.writemsg(f">>> {x}\n")
 
                 if ebuild_changed:
                     open(
                         os.path.join(
```

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/bsd/sed` & `portage-3.0.46/bin/ebuild-helpers/bsd/sed`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dobin` & `portage-3.0.46/bin/ebuild-helpers/dobin`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/doconfd` & `portage-3.0.46/bin/ebuild-helpers/doconfd`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dodoc` & `portage-3.0.46/bin/ebuild-helpers/dodoc`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/doenvd` & `portage-3.0.46/bin/ebuild-helpers/doenvd`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/doexe` & `portage-3.0.46/bin/ebuild-helpers/doexe`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dohard` & `portage-3.0.46/bin/ebuild-helpers/dohard`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/doheader` & `portage-3.0.46/bin/ebuild-helpers/doheader`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dohtml` & `portage-3.0.46/bin/ebuild-helpers/dohtml`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/doinfo` & `portage-3.0.46/bin/ebuild-helpers/doinfo`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/doins` & `portage-3.0.46/bin/ebuild-helpers/doins`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dolib` & `portage-3.0.46/bin/ebuild-helpers/dolib`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/doman` & `portage-3.0.46/bin/ebuild-helpers/doman`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/domo` & `portage-3.0.46/bin/ebuild-helpers/domo`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dosbin` & `portage-3.0.46/bin/ebuild-helpers/dosbin`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dosed` & `portage-3.0.46/bin/ebuild-helpers/dosed`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/dosym` & `portage-3.0.46/bin/ebuild-helpers/dosym`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/emake` & `portage-3.0.46/bin/ebuild-helpers/emake`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/fowners` & `portage-3.0.46/bin/ebuild-helpers/fowners`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/fperms` & `portage-3.0.46/bin/ebuild-helpers/fperms`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/newins` & `portage-3.0.46/bin/ebuild-helpers/newins`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/portageq` & `portage-3.0.46/bin/ebuild-helpers/portageq`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/prepinfo` & `portage-3.0.46/bin/ebuild-helpers/prepinfo`

 * *Files 8% similar despite different names*

```diff
@@ -1,13 +1,15 @@
 #!/usr/bin/env bash
-# Copyright 1999-2022 Gentoo Authors
+# Copyright 1999-2023 Gentoo Authors
 # Distributed under the terms of the GNU General Public License v2
 
 source "${PORTAGE_BIN_PATH}"/isolated-functions.sh || exit 1
 
+eqawarn "QA Notice: '${0##*/}' is not allowed in ebuild scope"
+
 if ! ___eapi_has_prefix_variables ; then
 	ED=${D}
 fi
 
 if [[ -z ${1} ]] ; then
 	infodir="/usr/share/info"
 else
```

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/unprivileged/chown` & `portage-3.0.46/bin/ebuild-helpers/unprivileged/chown`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-helpers/xattr/install` & `portage-3.0.46/bin/ebuild-helpers/xattr/install`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild-ipc.py` & `portage-3.0.46/bin/ebuild-ipc.py`

 * *Files 2% similar despite different names*

```diff
@@ -159,18 +159,15 @@
                 return self._communicate(args)
             finally:
                 portage.locks.unlockfile(lock_obj)
 
         def _timeout_retry_msg(self, start_time, when):
             time_elapsed = time.time() - start_time
             portage.util.writemsg_level(
-                portage.localization._(
-                    "ebuild-ipc timed out %s after %d seconds," + " retrying...\n"
-                )
-                % (when, time_elapsed),
+                f"ebuild-ipc timed out {when} after {time_elapsed} seconds, retrying...\n",
                 level=logging.ERROR,
                 noiselevel=-1,
             )
 
         def _no_daemon_msg(self):
             portage.util.writemsg_level(
                 portage.localization._("ebuild-ipc: daemon process not detected\n"),
@@ -286,16 +283,15 @@
                     scheduler=global_event_loop(),
                 ),
                 msg,
             )
 
             if retval != os.EX_OK:
                 portage.util.writemsg_level(
-                    "ebuild-ipc: %s: %s\n"
-                    % (msg, portage.localization._("subprocess failure: %s") % retval),
+                    f"ebuild-ipc: {msg}: subprocess failure: {retval}\n",
                     level=logging.ERROR,
                     noiselevel=-1,
                 )
                 return retval
 
             if not self._daemon_is_alive():
                 self._no_daemon_msg()
```

### Comparing `portage-3.0.45.3/bin/ebuild-pyhelper` & `portage-3.0.46/bin/ebuild-pyhelper`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ebuild.sh` & `portage-3.0.46/bin/ebuild.sh`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ecompress` & `portage-3.0.46/bin/ecompress`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/ecompress-file` & `portage-3.0.46/bin/ecompress-file`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/egencache` & `portage-3.0.46/bin/egencache`

 * *Files 1% similar despite different names*

```diff
@@ -63,15 +63,15 @@
     )
     from portage.const import TIMESTAMP_FORMAT
     from portage.dep import _repo_separator
     from portage.output import colorize, EOutput
     from portage.package.ebuild._parallel_manifest.ManifestScheduler import (
         ManifestScheduler,
     )
-    from portage.util import cmp_sort_key, writemsg_level
+    from portage.util import cmp_sort_key, writemsg_level, no_color
     from portage.util._async.AsyncFunction import AsyncFunction
     from portage.util._async.run_main_scheduler import run_main_scheduler
     from portage.util._async.TaskScheduler import TaskScheduler
     from portage.util._eventloop.global_event_loop import global_event_loop
     from portage.util.changelog import ChangeLogTypeSort
     from portage import cpv_getkey
     from portage.dep import Atom, isjustname
@@ -341,16 +341,15 @@
                 self._trg_caches = tuple(
                     conf.iter_pregenerated_caches(
                         self._auxdbkeys, force=True, readonly=False
                     )
                 )
                 if not self._trg_caches:
                     raise Exception(
-                        "cache formats '%s' aren't supported"
-                        % (" ".join(conf.cache_formats),)
+                        f"cache formats '{' '.join(conf.cache_formats)}' aren't supported"
                     )
 
             if rsync:
                 for trg_cache in self._trg_caches:
                     if hasattr(trg_cache, "raise_stat_collision"):
                         trg_cache.raise_stat_collision = True
                         # Make _metadata_callback write this cache first, in case
@@ -611,22 +610,15 @@
                             color = functools.partial(colorize, "turquoise")
                             prefix1 = "U"
 
                         if masked:
                             prefix0 = "M"
 
                         print(
-                            " [%s%s] %s (%s):  %s"
-                            % (
-                                colorize("red", prefix0),
-                                color(prefix1),
-                                colorize("bold", pkg_desc.cp),
-                                color(version[len(pkg_desc.cp) + 1 :]),
-                                pkg_desc.desc,
-                            )
+                            f" [{colorize('red', prefix0)}{color(prefix1)}] {colorize('bold', pkg_desc.cp)} ({color(version[len(pkg_desc.cp) + 1 :])}):  {pkg_desc.desc}"
                         )
                         haspkgs = True
 
                 if not haspkgs:
                     out.einfo("No updates found")
 
     class GenUseLocalDesc:
@@ -831,16 +823,15 @@
                             if len(resdict) == 1:
                                 resdesc = next(iter(resdict.items()))[1]
                             else:
                                 try:
                                     reskeys = {_Atom(k): k for k in resdict}
                                 except portage.exception.InvalidAtom as e:
                                     writemsg_level(
-                                        "ERROR: failed parsing %s/metadata.xml: %s\n"
-                                        % (cp, e),
+                                        f"ERROR: failed parsing {cp}/metadata.xml: {e}\n",
                                         level=logging.ERROR,
                                         noiselevel=-1,
                                     )
                                     self.returncode |= 1
                                     resdesc = next(iter(resdict.items()))[1]
                                 else:
                                     resatoms = sorted(
@@ -934,21 +925,20 @@
                     noiselevel=-1,
                 )
                 self.returncode |= 2
                 return
 
             output.write(
                 textwrap.dedent(
-                    """\
-                # ChangeLog for %s
-                # Copyright 1999-%s Gentoo Foundation; Distributed under the GPL v2
+                    f"""\
+                # ChangeLog for {cp}
+                # Copyright 1999-{time.strftime("%Y")} Gentoo Foundation; Distributed under the GPL v2
                 # (auto-generated from git log)
 
                 """
-                    % (cp, time.strftime("%Y"))
                 )
             )
 
             # now grab all the commits
             revlist_cmd = ["git", self._work_tree, "rev-list"]
             if self._changelog_reversed:
                 revlist_cmd.append("--reverse")
@@ -1060,17 +1050,18 @@
                 # don't break filenames on hyphens
                 self._wrapper.break_on_hyphens = False
                 output.write(
                     self._wrapper.fill(f"{date}; {author} {', '.join(changed)}:")
                 )
                 # but feel free to break commit messages there
                 self._wrapper.break_on_hyphens = True
-                output.write(
-                    "\n%s\n\n" % "\n".join(self._wrapper.fill(x) for x in body)
-                )
+                # temp var needed because fstrings can not have backslashes in
+                # the expression part...
+                temp_joined = "\n".join(self._wrapper.fill(x) for x in body)
+                output.write(f"\n{temp_joined}\n\n")
 
             output.close()
             os.utime(self._changelog_output, (lmod, lmod))
 
         def _task_iter(self):
             if not os.path.isdir(
                 os.environ.get("GIT_DIR", os.path.join(self._repo_path, ".git"))
@@ -1101,20 +1092,17 @@
         # completely controlled by commandline arguments.
         env = {}
 
         # Pass through PATH to allow testing with an empty profile.env.
         if "PATH" in os.environ:
             env["PATH"] = os.environ["PATH"]
 
-        if not sys.stdout.isatty() or os.environ.get("NOCOLOR", "").lower() in (
-            "yes",
-            "true",
-        ):
+        if not sys.stdout.isatty() or no_color(os.environ):
             portage.output.nocolor()
-            env["NOCOLOR"] = "true"
+            env["NO_COLOR"] = "true"
 
         parser, options, atoms = parse_args(args)
 
         config_root = options.config_root
 
         if options.repositories_configuration is not None:
             env["PORTAGE_REPOSITORIES"] = options.repositories_configuration
@@ -1248,20 +1236,16 @@
                         gpg_dir = options.gpg_dir
                     elif "PORTAGE_GPG_DIR" not in settings:
                         gpg_dir = os.path.expanduser("~/.gnupg")
                     else:
                         gpg_dir = os.path.expanduser(settings["PORTAGE_GPG_DIR"])
                     if not os.access(gpg_dir, os.X_OK):
                         writemsg_level(
-                            (
-                                "egencache: error: "
-                                "Unable to access directory: "
-                                "PORTAGE_GPG_DIR='%s'\n"
-                            )
-                            % gpg_dir,
+                            "egencache: error: Unable to access directory: "
+                            f"PORTAGE_GPG_DIR='{gpg_dir}'\n",
                             level=logging.ERROR,
                             noiselevel=-1,
                         )
                         sign_problem = True
 
                 if sign_problem:
                     writemsg_level(
```

### Comparing `portage-3.0.45.3/bin/emaint` & `portage-3.0.46/bin/emaint`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/emerge` & `portage-3.0.46/bin/emerge`

 * *Files 2% similar despite different names*

```diff
@@ -58,17 +58,17 @@
         try:
             retval = emerge_main()
         except PermissionDenied as e:
             sys.stderr.write(f"Permission denied: '{str(e)}'\n")
             sys.exit(e.errno)
         except IsADirectory as e:
             sys.stderr.write(
-                "'%s' is a directory, but should be a file!\n"
+                f"'{str(e)}' is a directory, but should be a file!\n"
                 "See portage man page for information on "
-                "which files may be directories.\n" % str(e)
+                "which files may be directories.\n"
             )
             sys.exit(e.errno)
         except ParseError as e:
             sys.stderr.write(f"{str(e)}\n")
             sys.exit(1)
         except (KeyboardInterrupt, SystemExit):
             raise
```

### Comparing `portage-3.0.45.3/bin/emerge-webrsync` & `portage-3.0.46/bin/emerge-webrsync`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/emirrordist` & `portage-3.0.46/bin/emirrordist`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/env-update` & `portage-3.0.46/bin/env-update`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/estrip` & `portage-3.0.46/bin/estrip`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/etc-update` & `portage-3.0.46/bin/etc-update`

 * *Files 0% similar despite different names*

```diff
@@ -794,14 +794,15 @@
 	FEATURES
 	PORTAGE_CONFIGROOT
 	PORTAGE_INST_{G,U}ID
 	PORTAGE_TMPDIR
 	EROOT
 	USERLAND
 	NOCOLOR
+	NO_COLOR
 )
 
 if type -P portageq > /dev/null; then
 	eval $(${PORTAGE_PYTHON:+"${PORTAGE_PYTHON}"} "$(type -P portageq)" envvar -v "${portage_vars[@]}")
 else
 	[[ ${OS_FAMILY} == 'gentoo' ]] && die "missing portageq"
 fi
```

### Comparing `portage-3.0.45.3/bin/filter-bash-environment.py` & `portage-3.0.46/bin/filter-bash-environment.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/fixpackages` & `portage-3.0.46/bin/fixpackages`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/glsa-check` & `portage-3.0.46/bin/glsa-check`

 * *Files 0% similar despite different names*

```diff
@@ -216,16 +216,15 @@
             glsalist.append(x)
     params.remove("affected")
 
 # remove invalid parameters
 for p in params[:]:
     if not (p in completelist or os.path.exists(p)):
         sys.stderr.write(
-            "(removing %s from parameter list as it isn't a valid GLSA specification)\n"
-            % p
+            f"(removing {p} from parameter list as it isn't a valid GLSA specification)\n"
         )
         params.remove(p)
 
 glsalist.extend([g for g in params if g not in glsalist])
 
 
 def summarylist(myglsalist, fd1=sys.stdout, fd2=sys.stderr, encoding="utf-8"):
@@ -257,15 +256,15 @@
             status = "[N]"
             color = red
         else:
             status = "[U]"
             color = green
 
         if verbose:
-            access = "[%-8s] " % myglsa.access
+            access = f"[{myglsa.access:8}] "
         else:
             access = ""
 
         fd1.write(
             color(myglsa.nr)
             + " "
             + color(status)
```

### Comparing `portage-3.0.45.3/bin/gpkg-helper.py` & `portage-3.0.46/bin/gpkg-helper.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/gpkg-sign` & `portage-3.0.46/bin/gpkg-sign`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/helper-functions.sh` & `portage-3.0.46/bin/helper-functions.sh`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/05prefix` & `portage-3.0.46/bin/install-qa-check.d/05prefix`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/10executable-issues` & `portage-3.0.46/bin/install-qa-check.d/10executable-issues`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/10ignored-flags` & `portage-3.0.46/bin/install-qa-check.d/10ignored-flags`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/20runtime-directories` & `portage-3.0.46/bin/install-qa-check.d/20runtime-directories`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/60bash-completion` & `portage-3.0.46/bin/install-qa-check.d/60bash-completion`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/60openrc` & `portage-3.0.46/bin/install-qa-check.d/60openrc`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/60pkgconfig` & `portage-3.0.46/bin/install-qa-check.d/60pkgconfig`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/60pngfix` & `portage-3.0.46/bin/install-qa-check.d/60pngfix`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/60systemd` & `portage-3.0.46/bin/install-qa-check.d/60systemd`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/80libraries` & `portage-3.0.46/bin/install-qa-check.d/80libraries`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/80multilib-strict` & `portage-3.0.46/bin/install-qa-check.d/80multilib-strict`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/90bad-bin-group-write` & `portage-3.0.46/bin/install-qa-check.d/90bad-bin-group-write`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/90bad-bin-owner` & `portage-3.0.46/bin/install-qa-check.d/90bad-bin-owner`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/90cmake-warnings` & `portage-3.0.46/bin/install-qa-check.d/90cmake-warnings`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/90config-impl-decl` & `portage-3.0.46/bin/install-qa-check.d/90config-impl-decl`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/90gcc-warnings` & `portage-3.0.46/bin/install-qa-check.d/90gcc-warnings`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/90world-writable` & `portage-3.0.46/bin/install-qa-check.d/90world-writable`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install-qa-check.d/95empty-dirs` & `portage-3.0.46/bin/install-qa-check.d/95empty-dirs`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/install.py` & `portage-3.0.46/bin/install.py`

 * *Files 1% similar despite different names*

```diff
@@ -170,16 +170,15 @@
 
     returncode = subprocess.call(cmdline)
     if returncode == os.EX_OK:
         returncode = copy_xattrs(opts, files)
         if returncode != os.EX_OK:
             portage.util.writemsg(
                 "!!! install: copy_xattrs failed with the "
-                "following arguments: %s\n"
-                % " ".join(portage._shell_quote(x) for x in args),
+                f"following arguments: {' '.join(portage._shell_quote(x) for x in args)}\n",
                 noiselevel=-1,
             )
     return returncode
 
 
 if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))
```

### Comparing `portage-3.0.45.3/bin/isolated-functions.sh` & `portage-3.0.46/bin/isolated-functions.sh`

 * *Files 1% similar despite different names*

```diff
@@ -430,22 +430,29 @@
 }
 
 RC_ENDCOL="yes"
 RC_INDENTATION=''
 RC_DEFAULT_INDENT=2
 RC_DOT_PATTERN=''
 
-case "${NOCOLOR:-false}" in
+
+
+if [[ -z ${NO_COLOR} ]] ; then
+	case ${NOCOLOR:-false} in
 	yes|true)
 		__unset_colors
 		;;
 	no|false)
 		__set_colors
 		;;
-esac
+	esac
+else
+	__unset_colors
+fi
+
 
 if [[ -z ${USERLAND} ]] ; then
 	case $(uname -s) in
 	*BSD|DragonFly)
 		export USERLAND="BSD"
 		;;
 	*)
```

### Comparing `portage-3.0.45.3/bin/lock-helper.py` & `portage-3.0.46/bin/lock-helper.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/misc-functions.sh` & `portage-3.0.46/bin/misc-functions.sh`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #!/usr/bin/env bash
-# Copyright 1999-2018 Gentoo Authors
+# Copyright 1999-2023 Gentoo Authors
 # Distributed under the terms of the GNU General Public License v2
 #
 # Miscellaneous shell functions that make use of the ebuild env but don't need
 # to be included directly in ebuild.sh.
 #
 # We're sourcing ebuild.sh here so that we inherit all of it's goodness,
 # including bashrc trickery.  This approach allows us to do our miscellaneous
@@ -139,15 +139,32 @@
 		# Save all the file flags for restoration afterwards.
 		mtree -c -p "${ED}" -k flags > "${T}/bsdflags.mtree"
 		# Remove all the file flags so that we can do anything necessary.
 		chflags -R noschg,nouchg,nosappnd,nouappnd "${ED}"
 		chflags -R nosunlnk,nouunlnk "${ED}" 2>/dev/null
 	fi
 
-	[[ -d ${ED%/}/usr/share/info ]] && prepinfo
+	if [[ -d ${ED%/}/usr/share/info ]]; then
+		# Portage regenerates this on the installed system.
+		rm -f "${ED%/}"/usr/share/info/dir{,.info}{,.Z,.gz,.bz2,.lzma,.lz,.xz,.zst} \
+			|| die "rm failed"
+		# Recurse into subdirs. Remove this code after 2023-12-31. #899898
+		while read -r -d '' x; do
+			( shopt -s failglob; : "${x}"/.keepinfodir* ) 2>/dev/null \
+				&& continue
+			for f in "${x}"/dir{,.info}{,.Z,.gz,.bz2,.lzma,.lz,.xz,.zst}; do
+				if [[ -e ${f} ]]; then
+					eqawarn "QA Notice: Removing Info directory file '${f}'."
+					eqawarn "Relying on this behavior is deprecated and may"
+					eqawarn "cause file collisions in future."
+					rm -f "${f}" || die "rm failed"
+				fi
+			done
+		done < <(find "${ED%/}"/usr/share/info -mindepth 1 -type d -print0)
+	fi
 
 	# If binpkg-docompress is enabled, apply compression before creating
 	# the binary package.
 	if has binpkg-docompress ${FEATURES}; then
 		"${PORTAGE_BIN_PATH}"/ecompress --queue "${PORTAGE_DOCOMPRESS[@]}"
 		"${PORTAGE_BIN_PATH}"/ecompress --ignore "${PORTAGE_DOCOMPRESS_SKIP[@]}"
 		"${PORTAGE_BIN_PATH}"/ecompress --dequeue
@@ -247,17 +264,14 @@
 			"${PORTAGE_BIN_PATH}"/estrip --queue "${PORTAGE_DOSTRIP[@]}"
 			"${PORTAGE_BIN_PATH}"/estrip --ignore "${PORTAGE_DOSTRIP_SKIP[@]}"
 			"${PORTAGE_BIN_PATH}"/estrip --dequeue
 		else
 			prepallstrip
 		fi
 	fi
-
-	# Portage regenerates this on the installed system.
-	rm -f "${ED%/}"/usr/share/info/dir{,.Z,.gz,.bz2,.lzma,.lz,.xz,.zst} || die "rm failed!"
 }
 
 __dyn_instprep() {
 	if [[ -e ${PORTAGE_BUILDDIR}/.instprepped ]] ; then
 		__vecho ">>> It appears that '${PF}' is already instprepped; skipping."
 		__vecho ">>> Remove '${PORTAGE_BUILDDIR}/.instprepped' to force instprep."
 		return 0
```

### Comparing `portage-3.0.45.3/bin/phase-functions.sh` & `portage-3.0.46/bin/phase-functions.sh`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/phase-helpers.sh` & `portage-3.0.46/bin/phase-helpers.sh`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/pid-ns-init` & `portage-3.0.46/bin/pid-ns-init`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/portageq` & `portage-3.0.46/bin/portageq`

 * *Files 0% similar despite different names*

```diff
@@ -66,15 +66,15 @@
     del pym_paths
 
     import portage
 
     portage._internal_caller = True
     from portage import os
     from portage.eapi import eapi_has_repo_deps
-    from portage.util import writemsg, writemsg_stdout
+    from portage.util import writemsg, writemsg_stdout, no_color
 
     portage.proxy.lazyimport.lazyimport(
         globals(),
         "re",
         "subprocess",
         "_emerge.Package:Package",
         "_emerge.RootConfig:RootConfig",
@@ -867,16 +867,16 @@
             return 2
 
         exit_status = 0
 
         for arg in argv:
             if arg in ("PORTDIR", "PORTDIR_OVERLAY", "SYNC"):
                 print(
-                    "WARNING: 'portageq envvar %s' is deprecated. Use any of "
-                    "'get_repos, get_repo_path, repos_config' instead." % arg,
+                    f"WARNING: 'portageq envvar {arg}' is deprecated. Use any of "
+                    "'get_repos, get_repo_path, repos_config' instead.",
                     file=sys.stderr,
                 )
 
             value = portage.settings.get(arg)
             if value is None:
                 value = ""
                 exit_status = 1
@@ -1447,17 +1447,15 @@
     else:
 
         def elog(elog_funcname, lines):
             pass
 
     def main(argv):
         argv = portage._decode_argv(argv)
-
-        nocolor = os.environ.get("NOCOLOR")
-        if nocolor in ("yes", "true"):
+        if no_color(os.environ):
             portage.output.nocolor()
 
         parser = argparse.ArgumentParser(add_help=False)
 
         # used by envvar
         parser.add_argument("-v", dest="verbose", action="store_true")
 
@@ -1514,16 +1512,16 @@
             eroot = portage.util.normalize_path(argv[2])
 
             if eprefix:
                 if not eroot.endswith(eprefix):
                     sys.stderr.write(
                         "ERROR: This version of portageq"
                         " only supports <eroot>s ending in"
-                        " '%s'. The provided <eroot>, '%s',"
-                        " doesn't.\n" % (eprefix, eroot)
+                        f" '{eprefix}'. The provided <eroot>, '{eroot}',"
+                        " doesn't.\n"
                     )
                     sys.stderr.flush()
                     sys.exit(os.EX_USAGE)
                 root = eroot[: 1 - len(eprefix)]
             else:
                 root = eroot
```

### Comparing `portage-3.0.45.3/bin/postinst-qa-check.d/50xdg-utils` & `portage-3.0.46/bin/postinst-qa-check.d/50xdg-utils`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/quickpkg` & `portage-3.0.46/bin/quickpkg`

 * *Files 0% similar despite different names*

```diff
@@ -172,16 +172,15 @@
                     eout.eerror(
                         f"Invalid or unsupported compression method: {e.args[0]}"
                     )
                     return 1
                 if find_binary(compression_binary) is None:
                     missing_package = compression["package"]
                     eout.eerror(
-                        "File compression unsupported %s. Missing package: %s"
-                        % (binpkg_compression, missing_package)
+                        f"File compression unsupported {binpkg_compression} (missing package: {missing_package})"
                     )
                     return 1
 
                 cmd = compression["compress"].replace(
                     "{JOBS}",
                     str(makeopts_to_job_count(settings.get("MAKEOPTS", "1"))),
                 )
@@ -387,15 +386,15 @@
                     size_str = str(int(size))
                 size_str += unit
             else:
                 size_str = str(size)
         eout.einfo(f"{cpv}: {size_str}")
     if infos["config_files_excluded"]:
         print()
-        eout.ewarn("Excluded config files: %d" % infos["config_files_excluded"])
+        eout.ewarn(f"Excluded config files: {infos['config_files_excluded']}")
         eout.ewarn("See --help if you would like to include config files.")
     if infos["missing"]:
         print()
         eout.ewarn("The following packages could not be found:")
         eout.ewarn(" ".join(infos["missing"]))
         return 2
     return os.EX_OK
```

### Comparing `portage-3.0.45.3/bin/regenworld` & `portage-3.0.46/bin/regenworld`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/save-ebuild-env.sh` & `portage-3.0.46/bin/save-ebuild-env.sh`

 * *Files 0% similar despite different names*

```diff
@@ -89,15 +89,15 @@
 	# portage config variables and variables set directly by portage
 	unset ACCEPT_LICENSE BUILD_PREFIX COLS \
 		DISTDIR DOC_SYMLINKS_DIR \
 		EBUILD_FORCE_TEST EBUILD_MASTER_PID \
 		ECLASS_DEPTH ENDCOL FAKEROOTKEY \
 		HOME \
 		LAST_E_CMD LAST_E_LEN LD_PRELOAD MISC_FUNCTIONS_ARGS MOPREFIX \
-		NOCOLOR PKGDIR PKGUSE PKG_LOGDIR PKG_TMPDIR \
+		NOCOLOR NO_COLOR PKGDIR PKGUSE PKG_LOGDIR PKG_TMPDIR \
 		PORTAGE_BASHRC_FILES PORTAGE_BASHRCS_SOURCED \
 		PORTAGE_COLOR_BAD PORTAGE_COLOR_BRACKET PORTAGE_COLOR_ERR \
 		PORTAGE_COLOR_GOOD PORTAGE_COLOR_HILITE PORTAGE_COLOR_INFO \
 		PORTAGE_COLOR_LOG PORTAGE_COLOR_NORMAL PORTAGE_COLOR_QAWARN \
 		PORTAGE_COLOR_WARN \
 		PORTAGE_COMPRESS PORTAGE_COMPRESS_EXCLUDE_SUFFIXES \
 		PORTAGE_DOHTML_UNWARNED_SKIPPED_EXTENSIONS \
```

### Comparing `portage-3.0.45.3/bin/shelve-utils` & `portage-3.0.46/bin/shelve-utils`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/socks5-server.py` & `portage-3.0.46/bin/socks5-server.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/bin/xattr-helper.py` & `portage-3.0.46/bin/xattr-helper.py`

 * *Files 3% similar despite different names*

```diff
@@ -116,21 +116,21 @@
     for i, line in enumerate(file_in):
         if line.startswith(b"# file: "):
             pathname = unquote(line.rstrip(b"\n")[8:])
         else:
             parts = line.split(b"=", 1)
             if len(parts) == 2:
                 if pathname is None:
-                    raise ValueError("line %d: missing pathname" % (i + 1,))
+                    raise ValueError(f"line {i + 1}: missing pathname")
                 attr = unquote(parts[0])
                 # strip trailing newline and quotes
                 value = unquote(parts[1].rstrip(b"\n")[1:-1])
                 xattr.set(pathname, attr, value)
             elif line.strip():
-                raise ValueError("line %d: malformed entry" % (i + 1,))
+                raise ValueError(f"line {i + 1}: malformed entry")
 
 
 def main(argv):
     parser = argparse.ArgumentParser(description=doc)
     parser.add_argument("paths", nargs="*", default=[])
 
     actions = parser.add_argument_group("Actions")
```

### Comparing `portage-3.0.45.3/bin/xpak-helper.py` & `portage-3.0.46/bin/xpak-helper.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.alpha.diff` & `portage-3.0.46/cnf/make.conf.example.alpha.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.amd64-fbsd.diff` & `portage-3.0.46/cnf/make.conf.example.amd64-fbsd.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.amd64.diff` & `portage-3.0.46/cnf/make.conf.example.amd64.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.arm.diff` & `portage-3.0.46/cnf/make.conf.example.arm.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.arm64.diff` & `portage-3.0.46/cnf/make.conf.example.arm64.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.hppa.diff` & `portage-3.0.46/cnf/make.conf.example.hppa.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.ia64.diff` & `portage-3.0.46/cnf/make.conf.example.ia64.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.loong.diff` & `portage-3.0.46/cnf/make.conf.example.loong.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.m68k.diff` & `portage-3.0.46/cnf/make.conf.example.m68k.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.mips.diff` & `portage-3.0.46/cnf/make.conf.example.mips.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.ppc.diff` & `portage-3.0.46/cnf/make.conf.example.ppc.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.ppc64.diff` & `portage-3.0.46/cnf/make.conf.example.ppc64.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.riscv.diff` & `portage-3.0.46/cnf/make.conf.example.riscv.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.s390.diff` & `portage-3.0.46/cnf/make.conf.example.s390.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.sh.diff` & `portage-3.0.46/cnf/make.conf.example.sh.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.sparc-fbsd.diff` & `portage-3.0.46/cnf/make.conf.example.sparc-fbsd.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.sparc.diff` & `portage-3.0.46/cnf/make.conf.example.sparc.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.x86-fbsd.diff` & `portage-3.0.46/cnf/make.conf.example.x86-fbsd.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/cnf/make.conf.example.x86.diff` & `portage-3.0.46/cnf/make.conf.example.x86.diff`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/api/Makefile` & `portage-3.0.46/doc/api/Makefile`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/api/conf.py` & `portage-3.0.46/doc/api/conf.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/config/bashrc.docbook` & `portage-3.0.46/doc/config/bashrc.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/config/sets.docbook` & `portage-3.0.46/doc/config/sets.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/dependency_resolution/decision_making.docbook` & `portage-3.0.46/doc/dependency_resolution/decision_making.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/dependency_resolution/package_modeling.docbook` & `portage-3.0.46/doc/dependency_resolution/package_modeling.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/dependency_resolution/task_scheduling.docbook` & `portage-3.0.46/doc/dependency_resolution/task_scheduling.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/eapi/1.docbook` & `portage-3.0.46/doc/package/ebuild/eapi/1.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/eapi/2.docbook` & `portage-3.0.46/doc/package/ebuild/eapi/2.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/eapi/3.docbook` & `portage-3.0.46/doc/package/ebuild/eapi/3.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/eapi/4-slot-abi.docbook` & `portage-3.0.46/doc/package/ebuild/eapi/4-slot-abi.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/eapi/4.docbook` & `portage-3.0.46/doc/package/ebuild/eapi/4.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/eapi/5.docbook` & `portage-3.0.46/doc/package/ebuild/eapi/5.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/helper_functions.docbook` & `portage-3.0.46/doc/package/ebuild/helper_functions.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/package/ebuild/phases.docbook` & `portage-3.0.46/doc/package/ebuild/phases.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/portage.docbook` & `portage-3.0.46/doc/portage.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/doc/qa.docbook` & `portage-3.0.46/doc/qa.docbook`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/AbstractDepPriority.py` & `portage-3.0.46/lib/_emerge/AbstractDepPriority.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/AbstractEbuildProcess.py` & `portage-3.0.46/lib/_emerge/AbstractEbuildProcess.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 import portage
 from portage.elog import messages as elog_messages
 from portage.localization import _
 from portage.package.ebuild._ipc.ExitCommand import ExitCommand
 from portage.package.ebuild._ipc.QueryCommand import QueryCommand
 from portage import os
 from portage.util.futures import asyncio
-from portage.util import apply_secpass_permissions
+from portage.util import apply_secpass_permissions, no_color
 
 portage.proxy.lazyimport.lazyimport(
     globals(),
     "portage.package.ebuild.doebuild:_global_pid_phases",
 )
 
 
@@ -166,14 +166,15 @@
             else:
                 self.cgroup = cgroup_path
 
         if self.background:
             # Automatically prevent color codes from showing up in logs,
             # since we're not displaying to a terminal anyway.
             self.settings["NOCOLOR"] = "true"
+            self.settings["NO_COLOR"] = "true"
 
         start_ipc_daemon = False
         if self._enable_ipc_daemon:
             self.settings.pop("PORTAGE_EBUILD_EXIT_FILE", None)
             if self.phase not in self._phases_without_builddir:
                 start_ipc_daemon = True
                 if "PORTAGE_BUILDDIR_LOCKED" not in self.settings:
@@ -386,17 +387,15 @@
 
     def _elog(self, elog_funcname, lines):
         out = io.StringIO()
         phase = self.phase
         elog_func = getattr(elog_messages, elog_funcname)
         global_havecolor = portage.output.havecolor
         try:
-            portage.output.havecolor = self.settings.get(
-                "NOCOLOR", "false"
-            ).lower() in ("no", "false")
+            portage.output.havecolor = not no_color(self.settings)
             for line in lines:
                 elog_func(line, phase=phase, key=self.settings.mycpv, out=out)
         finally:
             portage.output.havecolor = global_havecolor
         msg = out.getvalue()
         if msg:
             log_path = None
```

### Comparing `portage-3.0.45.3/lib/_emerge/AbstractPollTask.py` & `portage-3.0.46/lib/_emerge/AbstractPollTask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/AsynchronousLock.py` & `portage-3.0.46/lib/_emerge/AsynchronousLock.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/AsynchronousTask.py` & `portage-3.0.46/lib/_emerge/AsynchronousTask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/Binpkg.py` & `portage-3.0.46/lib/_emerge/Binpkg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/BinpkgEnvExtractor.py` & `portage-3.0.46/lib/_emerge/BinpkgEnvExtractor.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/BinpkgExtractorAsync.py` & `portage-3.0.46/lib/_emerge/BinpkgExtractorAsync.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/BinpkgFetcher.py` & `portage-3.0.46/lib/_emerge/BinpkgFetcher.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/BinpkgPrefetcher.py` & `portage-3.0.46/lib/_emerge/BinpkgPrefetcher.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/BinpkgVerifier.py` & `portage-3.0.46/lib/_emerge/BinpkgVerifier.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/BlockerCache.py` & `portage-3.0.46/lib/_emerge/BlockerCache.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/BlockerDB.py` & `portage-3.0.46/lib/_emerge/BlockerDB.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/CompositeTask.py` & `portage-3.0.46/lib/_emerge/CompositeTask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/DepPriority.py` & `portage-3.0.46/lib/_emerge/DepPriority.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/DepPriorityNormalRange.py` & `portage-3.0.46/lib/_emerge/DepPriorityNormalRange.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/DepPrioritySatisfiedRange.py` & `portage-3.0.46/lib/_emerge/DepPrioritySatisfiedRange.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/Dependency.py` & `portage-3.0.46/lib/_emerge/Dependency.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/DependencyArg.py` & `portage-3.0.46/lib/_emerge/DependencyArg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildBinpkg.py` & `portage-3.0.46/lib/_emerge/EbuildBinpkg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildBuild.py` & `portage-3.0.46/lib/_emerge/EbuildBuild.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildBuildDir.py` & `portage-3.0.46/lib/_emerge/EbuildBuildDir.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildExecuter.py` & `portage-3.0.46/lib/_emerge/EbuildExecuter.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildFetcher.py` & `portage-3.0.46/lib/_emerge/EbuildFetcher.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildFetchonly.py` & `portage-3.0.46/lib/_emerge/EbuildFetchonly.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildIpcDaemon.py` & `portage-3.0.46/lib/_emerge/EbuildIpcDaemon.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildMerge.py` & `portage-3.0.46/lib/_emerge/EbuildMerge.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildMetadataPhase.py` & `portage-3.0.46/lib/_emerge/EbuildMetadataPhase.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildPhase.py` & `portage-3.0.46/lib/_emerge/EbuildPhase.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildProcess.py` & `portage-3.0.46/lib/_emerge/EbuildProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/EbuildSpawnProcess.py` & `portage-3.0.46/lib/_emerge/EbuildSpawnProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/FakeVartree.py` & `portage-3.0.46/lib/_emerge/FakeVartree.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/FifoIpcDaemon.py` & `portage-3.0.46/lib/_emerge/FifoIpcDaemon.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/JobStatusDisplay.py` & `portage-3.0.46/lib/_emerge/JobStatusDisplay.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/MergeListItem.py` & `portage-3.0.46/lib/_emerge/MergeListItem.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/MetadataRegen.py` & `portage-3.0.46/lib/_emerge/MetadataRegen.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/MiscFunctionsProcess.py` & `portage-3.0.46/lib/_emerge/MiscFunctionsProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/Package.py` & `portage-3.0.46/lib/_emerge/Package.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/PackageArg.py` & `portage-3.0.46/lib/_emerge/PackageArg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/PackageMerge.py` & `portage-3.0.46/lib/_emerge/PackageMerge.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/PackagePhase.py` & `portage-3.0.46/lib/_emerge/PackagePhase.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/PackageUninstall.py` & `portage-3.0.46/lib/_emerge/PackageUninstall.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/PackageVirtualDbapi.py` & `portage-3.0.46/lib/_emerge/PackageVirtualDbapi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/PipeReader.py` & `portage-3.0.46/lib/_emerge/PipeReader.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/PollScheduler.py` & `portage-3.0.46/lib/_emerge/PollScheduler.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/ProgressHandler.py` & `portage-3.0.46/lib/_emerge/ProgressHandler.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/RootConfig.py` & `portage-3.0.46/lib/_emerge/RootConfig.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/Scheduler.py` & `portage-3.0.46/lib/_emerge/Scheduler.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/SequentialTaskQueue.py` & `portage-3.0.46/lib/_emerge/SequentialTaskQueue.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/SpawnProcess.py` & `portage-3.0.46/lib/_emerge/SpawnProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/SubProcess.py` & `portage-3.0.46/lib/_emerge/SubProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/Task.py` & `portage-3.0.46/lib/_emerge/Task.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/TaskSequence.py` & `portage-3.0.46/lib/_emerge/TaskSequence.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/UnmergeDepPriority.py` & `portage-3.0.46/lib/_emerge/UnmergeDepPriority.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/UseFlagDisplay.py` & `portage-3.0.46/lib/_emerge/UseFlagDisplay.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/UserQuery.py` & `portage-3.0.46/lib/_emerge/UserQuery.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/_find_deep_system_runtime_deps.py` & `portage-3.0.46/lib/_emerge/_find_deep_system_runtime_deps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/actions.py` & `portage-3.0.46/lib/_emerge/actions.py`

 * *Files 0% similar despite different names*

```diff
@@ -2753,31 +2753,31 @@
         )
         del e
     if "--debug" in myopts:
         PORTAGE_DEBUG = 1
     settings["PORTAGE_DEBUG"] = str(PORTAGE_DEBUG)
     settings.backup_changes("PORTAGE_DEBUG")
 
-    if settings.get("NOCOLOR") not in ("yes", "true"):
+    if not portage.util.no_color(settings):
         portage.output.havecolor = 1
 
     # The explicit --color < y | n > option overrides the NOCOLOR environment
     # variable and stdout auto-detection.
     if "--color" in myopts:
         if "y" == myopts["--color"]:
             portage.output.havecolor = 1
-            settings["NOCOLOR"] = "false"
+            settings["NO_COLOR"] = ""
         else:
             portage.output.havecolor = 0
-            settings["NOCOLOR"] = "true"
-        settings.backup_changes("NOCOLOR")
+            settings["NO_COLOR"] = "true"
+        settings.backup_changes("NO_COLOR")
     elif settings.get("TERM") == "dumb" or not sys.stdout.isatty():
         portage.output.havecolor = 0
-        settings["NOCOLOR"] = "true"
-        settings.backup_changes("NOCOLOR")
+        settings["NO_COLOR"] = "true"
+        settings.backup_changes("NO_COLOR")
 
     if "--pkg-format" in myopts:
         settings["PORTAGE_BINPKG_FORMAT"] = myopts["--pkg-format"]
         settings.backup_changes("PORTAGE_BINPKG_FORMAT")
 
 
 def display_missing_pkg_set(root_config, set_name):
```

### Comparing `portage-3.0.45.3/lib/_emerge/chk_updated_cfg_files.py` & `portage-3.0.46/lib/_emerge/chk_updated_cfg_files.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/countdown.py` & `portage-3.0.46/lib/_emerge/countdown.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/create_depgraph_params.py` & `portage-3.0.46/lib/_emerge/create_depgraph_params.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/create_world_atom.py` & `portage-3.0.46/lib/_emerge/create_world_atom.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/depgraph.py` & `portage-3.0.46/lib/_emerge/depgraph.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/emergelog.py` & `portage-3.0.46/lib/_emerge/emergelog.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/getloadavg.py` & `portage-3.0.46/lib/_emerge/getloadavg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/help.py` & `portage-3.0.46/lib/_emerge/help.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/is_valid_package_atom.py` & `portage-3.0.46/lib/_emerge/is_valid_package_atom.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/main.py` & `portage-3.0.46/lib/_emerge/main.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/post_emerge.py` & `portage-3.0.46/lib/_emerge/post_emerge.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/resolver/DbapiProvidesIndex.py` & `portage-3.0.46/lib/_emerge/resolver/DbapiProvidesIndex.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/resolver/backtracking.py` & `portage-3.0.46/lib/_emerge/resolver/backtracking.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/resolver/circular_dependency.py` & `portage-3.0.46/lib/_emerge/resolver/circular_dependency.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/resolver/output.py` & `portage-3.0.46/lib/_emerge/resolver/output.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/resolver/output_helpers.py` & `portage-3.0.46/lib/_emerge/resolver/output_helpers.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/resolver/package_tracker.py` & `portage-3.0.46/lib/_emerge/resolver/package_tracker.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/resolver/slot_collision.py` & `portage-3.0.46/lib/_emerge/resolver/slot_collision.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/search.py` & `portage-3.0.46/lib/_emerge/search.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/show_invalid_depstring_notice.py` & `portage-3.0.46/lib/_emerge/show_invalid_depstring_notice.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/stdout_spinner.py` & `portage-3.0.46/lib/_emerge/stdout_spinner.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/_emerge/unmerge.py` & `portage-3.0.46/lib/_emerge/unmerge.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/__init__.py` & `portage-3.0.46/lib/portage/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_compat_upgrade/binpkg_compression.py` & `portage-3.0.46/lib/portage/_compat_upgrade/binpkg_compression.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_compat_upgrade/binpkg_multi_instance.py` & `portage-3.0.46/lib/portage/_compat_upgrade/binpkg_multi_instance.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_compat_upgrade/default_locations.py` & `portage-3.0.46/lib/portage/_compat_upgrade/default_locations.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/Config.py` & `portage-3.0.46/lib/portage/_emirrordist/Config.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/ContentDB.py` & `portage-3.0.46/lib/portage/_emirrordist/ContentDB.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/DeletionIterator.py` & `portage-3.0.46/lib/portage/_emirrordist/DeletionIterator.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/DeletionTask.py` & `portage-3.0.46/lib/portage/_emirrordist/DeletionTask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/FetchIterator.py` & `portage-3.0.46/lib/portage/_emirrordist/FetchIterator.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/FetchTask.py` & `portage-3.0.46/lib/portage/_emirrordist/FetchTask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/MirrorDistTask.py` & `portage-3.0.46/lib/portage/_emirrordist/MirrorDistTask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_emirrordist/main.py` & `portage-3.0.46/lib/portage/_emirrordist/main.py`

 * *Files 0% similar despite different names*

```diff
@@ -234,15 +234,15 @@
 def emirrordist_main(args):
     # The calling environment is ignored, so the program is
     # completely controlled by commandline arguments.
     env = {}
 
     if not sys.stdout.isatty():
         portage.output.nocolor()
-        env["NOCOLOR"] = "true"
+        env["NO_COLOR"] = "true"
 
     parser, options, args = parse_args(args)
 
     if options.version:
         sys.stdout.write(f"Portage {portage.VERSION}\n")
         return os.EX_OK
```

### Comparing `portage-3.0.45.3/lib/portage/_global_updates.py` & `portage-3.0.46/lib/portage/_global_updates.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_legacy_globals.py` & `portage-3.0.46/lib/portage/_legacy_globals.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_selinux.py` & `portage-3.0.46/lib/portage/_selinux.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/ProfilePackageSet.py` & `portage-3.0.46/lib/portage/_sets/ProfilePackageSet.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/__init__.py` & `portage-3.0.46/lib/portage/_sets/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/base.py` & `portage-3.0.46/lib/portage/_sets/base.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/dbapi.py` & `portage-3.0.46/lib/portage/_sets/dbapi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/files.py` & `portage-3.0.46/lib/portage/_sets/files.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/libs.py` & `portage-3.0.46/lib/portage/_sets/libs.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/profiles.py` & `portage-3.0.46/lib/portage/_sets/profiles.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/security.py` & `portage-3.0.46/lib/portage/_sets/security.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/_sets/shell.py` & `portage-3.0.46/lib/portage/_sets/shell.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/binpkg.py` & `portage-3.0.46/lib/portage/binpkg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/binrepo/config.py` & `portage-3.0.46/lib/portage/binrepo/config.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/anydbm.py` & `portage-3.0.46/lib/portage/cache/anydbm.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/cache_errors.py` & `portage-3.0.46/lib/portage/cache/cache_errors.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/ebuild_xattr.py` & `portage-3.0.46/lib/portage/cache/ebuild_xattr.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/flat_hash.py` & `portage-3.0.46/lib/portage/cache/flat_hash.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/fs_template.py` & `portage-3.0.46/lib/portage/cache/fs_template.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/index/IndexStreamIterator.py` & `portage-3.0.46/lib/portage/cache/index/IndexStreamIterator.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/index/pkg_desc_index.py` & `portage-3.0.46/lib/portage/cache/index/pkg_desc_index.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/mappings.py` & `portage-3.0.46/lib/portage/cache/mappings.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/metadata.py` & `portage-3.0.46/lib/portage/cache/metadata.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/sql_template.py` & `portage-3.0.46/lib/portage/cache/sql_template.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/sqlite.py` & `portage-3.0.46/lib/portage/cache/sqlite.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/template.py` & `portage-3.0.46/lib/portage/cache/template.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cache/volatile.py` & `portage-3.0.46/lib/portage/cache/volatile.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/checksum.py` & `portage-3.0.46/lib/portage/checksum.py`

 * *Files 19% similar despite different names*

```diff
@@ -22,19 +22,19 @@
 # ================================================================
 #
 # MD5: hashlib
 # SHA1: hashlib
 # SHA256: hashlib
 # SHA512: hashlib
 # RMD160: hashlib, pycrypto, mhash
-# WHIRLPOOL: hashlib, mhash, bundled
-# BLAKE2B (512): hashlib (3.6+), pyblake2, pycrypto
-# BLAKE2S (512): hashlib (3.6+), pyblake2, pycrypto
-# SHA3_256: hashlib (3.6+), pysha3, pycrypto
-# SHA3_512: hashlib (3.6+), pysha3, pycrypto
+# WHIRLPOOL: hashlib, bundled (C), bundled (Python)
+# BLAKE2B (512): hashlib
+# BLAKE2S (512): hashlib
+# SHA3_256: hashlib
+# SHA3_512: hashlib
 
 
 # Dict of all available hash functions
 hashfunc_map = {}
 hashorigin_map = {}
 
 
@@ -95,26 +95,30 @@
 
         return (checksum.hexdigest(), size)
 
 
 # Define hash functions, try to use the best module available. Preferred
 # modules should go first, latter ones should check if the hashes aren't
 # already defined.
-
-
-# Use hashlib from python-2.5 if available and prefer it over pycrypto and internal fallbacks.
+# Use hashlib if available and prefer it over pycrypto and internal fallbacks.
+#
 # Need special handling for RMD160/WHIRLPOOL as they may not always be provided by hashlib.
+# We keep fallbacks for RMD160/WHIRLPOOL for now as newer OpenSSLs don't expose them
+# by default.
+# See also
+# - https://github.com/python/cpython/issues/91257
+# - https://github.com/python/cpython/issues/92876
+# - https://bugs.gentoo.org/846389
 _generate_hash_function("MD5", hashlib.md5, origin="hashlib")
 _generate_hash_function("SHA1", hashlib.sha1, origin="hashlib")
 _generate_hash_function("SHA256", hashlib.sha256, origin="hashlib")
 _generate_hash_function("SHA512", hashlib.sha512, origin="hashlib")
 for local_name, hash_name in (
     ("RMD160", "ripemd160"),
     ("WHIRLPOOL", "whirlpool"),
-    # available since Python 3.6
     ("BLAKE2B", "blake2b"),
     ("BLAKE2S", "blake2s"),
     ("SHA3_256", "sha3_256"),
     ("SHA3_512", "sha3_512"),
 ):
     try:
         hashlib.new(hash_name)
@@ -122,190 +126,45 @@
         pass
     else:
         _generate_hash_function(
             local_name, functools.partial(hashlib.new, hash_name), origin="hashlib"
         )
 
 
-# Support using pyblake2 as fallback for python<3.6
-if "BLAKE2B" not in hashfunc_map or "BLAKE2S" not in hashfunc_map:
-    try:
-        import pyblake2
-
-        _generate_hash_function("BLAKE2B", pyblake2.blake2b, origin="pyblake2")
-        _generate_hash_function("BLAKE2S", pyblake2.blake2s, origin="pyblake2")
-    except ImportError:
-        pass
-
-
-# Support using pysha3 as fallback for python<3.6
-if "SHA3_256" not in hashfunc_map or "SHA3_512" not in hashfunc_map:
-    try:
-        import sha3
-
-        _generate_hash_function("SHA3_256", sha3.sha3_256, origin="pysha3")
-        _generate_hash_function("SHA3_512", sha3.sha3_512, origin="pysha3")
-    except ImportError:
-        pass
-
-
-# Support pygcrypt as fallback using optimized routines from libgcrypt
-# (GnuPG).
-gcrypt_algos = frozenset(
-    ("RMD160", "WHIRLPOOL", "SHA3_256", "SHA3_512", "STREEBOG256", "STREEBOG512")
-)
-# Note: currently disabled due to resource exhaustion bugs in pygcrypt.
-# Please do not reenable until upstream has a fix.
-# https://bugs.gentoo.org/615620
-if False:
-    # if gcrypt_algos.difference(hashfunc_map):
-    try:
-        import binascii
-        import pygcrypt.hashcontext
-
-        class GCryptHashWrapper:
-            def __init__(self, algo):
-                self._obj = pygcrypt.hashcontext.HashContext(algo=algo, secure=False)
-
-            def update(self, data):
-                self._obj.write(data)
-
-            def hexdigest(self):
-                return binascii.b2a_hex(self._obj.read()).decode()
-
-        name_mapping = {
-            "RMD160": "ripemd160",
-            "WHIRLPOOL": "whirlpool",
-            "SHA3_256": "sha3-256",
-            "SHA3_512": "sha3-512",
-            "STREEBOG256": "stribog256",
-            "STREEBOG512": "stribog512",
-        }
-
-        for local_name, gcry_name in name_mapping.items():
-            try:
-                pygcrypt.hashcontext.HashContext(algo=gcry_name)
-            except Exception:  # yes, it throws Exception...
-                pass
-            else:
-                _generate_hash_function(
-                    local_name,
-                    functools.partial(GCryptHashWrapper, gcry_name),
-                    origin="pygcrypt",
-                )
-    except ImportError:
-        pass
-
-
 # Use pycrypto when available, prefer it over the internal fallbacks
 # Check for 'new' attributes, since they can be missing if the module
 # is broken somehow.
 if "RMD160" not in hashfunc_map:
     try:
         from Crypto.Hash import RIPEMD
 
         rmd160hash_ = getattr(RIPEMD, "new", None)
         if rmd160hash_ is not None:
             _generate_hash_function("RMD160", rmd160hash_, origin="pycrypto")
     except ImportError:
-        pass
-
-# The following hashes were added in pycryptodome (pycrypto fork)
-if "BLAKE2B" not in hashfunc_map:
-    try:
-        from Crypto.Hash import BLAKE2b
-
-        blake2bhash_ = getattr(BLAKE2b, "new", None)
-        if blake2bhash_ is not None:
-            _generate_hash_function(
-                "BLAKE2B",
-                functools.partial(blake2bhash_, digest_bytes=64),
-                origin="pycrypto",
-            )
-    except ImportError:
-        pass
-
-if "BLAKE2S" not in hashfunc_map:
-    try:
-        from Crypto.Hash import BLAKE2s
-
-        blake2shash_ = getattr(BLAKE2s, "new", None)
-        if blake2shash_ is not None:
-            _generate_hash_function(
-                "BLAKE2S",
-                functools.partial(blake2shash_, digest_bytes=32),
-                origin="pycrypto",
-            )
-    except ImportError:
-        pass
-
-if "SHA3_256" not in hashfunc_map:
-    try:
-        from Crypto.Hash import SHA3_256
-
-        sha3_256hash_ = getattr(SHA3_256, "new", None)
-        if sha3_256hash_ is not None:
-            _generate_hash_function("SHA3_256", sha3_256hash_, origin="pycrypto")
-    except ImportError:
-        pass
-
-if "SHA3_512" not in hashfunc_map:
-    try:
-        from Crypto.Hash import SHA3_512
-
-        sha3_512hash_ = getattr(SHA3_512, "new", None)
-        if sha3_512hash_ is not None:
-            _generate_hash_function("SHA3_512", sha3_512hash_, origin="pycrypto")
-    except ImportError:
-        pass
-
-
-# Try to use mhash if available
-# mhash causes GIL presently, so it gets less priority than hashlib and
-# pycrypto. However, it might be the only accelerated implementation of
-# WHIRLPOOL available.
-if "RMD160" not in hashfunc_map or "WHIRLPOOL" not in hashfunc_map:
-    try:
-        import mhash
-
-        for local_name, hash_name in (
-            ("RMD160", "RIPEMD160"),
-            ("WHIRLPOOL", "WHIRLPOOL"),
-        ):
-            if local_name not in hashfunc_map and hasattr(mhash, f"MHASH_{hash_name}"):
-                _generate_hash_function(
-                    local_name,
-                    functools.partial(
-                        mhash.MHASH, getattr(mhash, f"MHASH_{hash_name}")
-                    ),
-                    origin="mhash",
-                )
-    except ImportError:
-        pass
-
-
-# Support pygost as fallback streebog provider
-# It's mostly provided as a reference implementation; it's pure Python,
-# slow and reads all data to memory (i.e. doesn't hash on update()...)
-if "STREEBOG256" not in hashfunc_map or "STREEBOG512" not in hashfunc_map:
-    try:
-        import pygost.gost34112012
-
-        _generate_hash_function(
-            "STREEBOG256",
-            functools.partial(pygost.gost34112012.GOST34112012, digest_size=32),
-            origin="pygost",
-        )
-        _generate_hash_function(
-            "STREEBOG512",
-            functools.partial(pygost.gost34112012.GOST34112012, digest_size=64),
-            origin="pygost",
-        )
-    except ImportError:
-        pass
+        # Try to use mhash if available
+        # mhash causes GIL presently, so it gets less priority than hashlib and
+        # pycrypto. However, it might be the only accelerated implementation of
+        # WHIRLPOOL available.
+        try:
+            import mhash
+
+            for local_name, hash_name in (("RMD160", "RIPEMD160"),):
+                if local_name not in hashfunc_map and hasattr(
+                    mhash, f"MHASH_{hash_name}"
+                ):
+                    _generate_hash_function(
+                        local_name,
+                        functools.partial(
+                            mhash.MHASH, getattr(mhash, f"MHASH_{hash_name}")
+                        ),
+                        origin="mhash",
+                    )
+        except ImportError:
+            pass
 
 
 _whirlpool_unaccelerated = False
 if "WHIRLPOOL" not in hashfunc_map:
     # Bundled WHIRLPOOL implementation
     from portage.util.whirlpool import CWhirlpool, PyWhirlpool
```

### Comparing `portage-3.0.45.3/lib/portage/const.py` & `portage-3.0.46/lib/portage/const.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/cvstree.py` & `portage-3.0.46/lib/portage/cvstree.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/data.py` & `portage-3.0.46/lib/portage/data.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/DummyTree.py` & `portage-3.0.46/lib/portage/dbapi/DummyTree.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/IndexedPortdb.py` & `portage-3.0.46/lib/portage/dbapi/IndexedPortdb.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/IndexedVardb.py` & `portage-3.0.46/lib/portage/dbapi/IndexedVardb.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/_ContentsCaseSensitivityManager.py` & `portage-3.0.46/lib/portage/dbapi/_ContentsCaseSensitivityManager.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/_MergeProcess.py` & `portage-3.0.46/lib/portage/dbapi/_MergeProcess.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,14 +7,15 @@
 
 import fcntl
 import portage
 from portage import os, _unicode_decode
 from portage.util._ctypes import find_library
 import portage.elog.messages
 from portage.util._async.ForkProcess import ForkProcess
+from portage.util import no_color
 
 
 class MergeProcess(ForkProcess):
     """
     Merge packages in a subprocess, so the Scheduler can run in the main
     thread while files are moved or copied asynchronously.
     """
@@ -196,17 +197,15 @@
 
         return pids
 
     def _run(self):
         os.close(self._elog_reader_fd)
         counter = self._counter
         mylink = self._dblink
-
-        portage.output.havecolor = self.settings.get("NOCOLOR") not in ("yes", "true")
-
+        portage.output.havecolor = not no_color(self.settings)
         # Avoid wastful updates of the vdb cache.
         self.vartree.dbapi._flush_cache_enabled = False
 
         # In this subprocess we don't want PORTAGE_BACKGROUND to
         # suppress stdout/stderr output since they are pipes. We
         # also don't want to open PORTAGE_LOG_FILE, since it will
         # already be opened by the parent process, so we set the
```

### Comparing `portage-3.0.45.3/lib/portage/dbapi/_SyncfsProcess.py` & `portage-3.0.46/lib/portage/dbapi/_SyncfsProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/_VdbMetadataDelta.py` & `portage-3.0.46/lib/portage/dbapi/_VdbMetadataDelta.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/__init__.py` & `portage-3.0.46/lib/portage/dbapi/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 # Copyright 1998-2020 Gentoo Authors
 # Distributed under the terms of the GNU General Public License v2
 
 __all__ = ["dbapi"]
 
 import re
+import warnings
 
 import portage
 
 portage.proxy.lazyimport.lazyimport(
     globals(),
     "portage.dbapi.dep_expand:dep_expand@_dep_expand",
     "portage.dep:Atom,match_from_list,_match_slot",
@@ -17,15 +18,15 @@
 )
 
 from portage.const import MERGING_IDENTIFIER
 
 from portage import os
 from portage import auxdbkeys
 from portage.eapi import _get_eapi_attrs
-from portage.exception import InvalidData
+from portage.exception import InvalidBinaryPackageFormat, InvalidData
 from portage.localization import _
 from _emerge.Package import Package
 
 
 class dbapi:
     _category_re = re.compile(r"^\w[-.+\w]*$", re.UNICODE)
     _categories = None
@@ -406,15 +407,18 @@
             if not updates_list:
                 continue
 
             metadata_updates = portage.update_dbentries(
                 updates_list, metadata, parent=pkg
             )
             if metadata_updates:
-                aux_update(cpv, metadata_updates)
+                try:
+                    aux_update(cpv, metadata_updates)
+                except InvalidBinaryPackageFormat as e:
+                    warnings.warn(e)
                 if onUpdate:
                     onUpdate(maxval, i + 1)
             if onProgress:
                 onProgress(maxval, i + 1)
 
     def move_slot_ent(self, mylist, repo_match=None):
         """This function takes a sequence:
```

### Comparing `portage-3.0.45.3/lib/portage/dbapi/_expand_new_virt.py` & `portage-3.0.46/lib/portage/dbapi/_expand_new_virt.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/_similar_name_search.py` & `portage-3.0.46/lib/portage/dbapi/_similar_name_search.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/bintree.py` & `portage-3.0.46/lib/portage/dbapi/bintree.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/cpv_expand.py` & `portage-3.0.46/lib/portage/dbapi/cpv_expand.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/dep_expand.py` & `portage-3.0.46/lib/portage/dbapi/dep_expand.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/porttree.py` & `portage-3.0.46/lib/portage/dbapi/porttree.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/vartree.py` & `portage-3.0.46/lib/portage/dbapi/vartree.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dbapi/virtual.py` & `portage-3.0.46/lib/portage/dbapi/virtual.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/debug.py` & `portage-3.0.46/lib/portage/debug.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dep/__init__.py` & `portage-3.0.46/lib/portage/dep/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dep/_dnf.py` & `portage-3.0.46/lib/portage/dep/_dnf.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dep/_slot_operator.py` & `portage-3.0.46/lib/portage/dep/_slot_operator.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dep/dep_check.py` & `portage-3.0.46/lib/portage/dep/dep_check.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dep/soname/SonameAtom.py` & `portage-3.0.46/lib/portage/dep/soname/SonameAtom.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dep/soname/multilib_category.py` & `portage-3.0.46/lib/portage/dep/soname/multilib_category.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dep/soname/parse.py` & `portage-3.0.46/lib/portage/dep/soname/parse.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/dispatch_conf.py` & `portage-3.0.46/lib/portage/dispatch_conf.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/eapi.py` & `portage-3.0.46/lib/portage/eapi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/eclass_cache.py` & `portage-3.0.46/lib/portage/eclass_cache.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/__init__.py` & `portage-3.0.46/lib/portage/elog/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/filtering.py` & `portage-3.0.46/lib/portage/elog/filtering.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/messages.py` & `portage-3.0.46/lib/portage/elog/messages.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/mod_custom.py` & `portage-3.0.46/lib/portage/elog/mod_custom.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/mod_echo.py` & `portage-3.0.46/lib/portage/elog/mod_echo.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/mod_mail.py` & `portage-3.0.46/lib/portage/elog/mod_mail.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/mod_mail_summary.py` & `portage-3.0.46/lib/portage/elog/mod_mail_summary.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/mod_save.py` & `portage-3.0.46/lib/portage/elog/mod_save.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/mod_save_summary.py` & `portage-3.0.46/lib/portage/elog/mod_save_summary.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/elog/mod_syslog.py` & `portage-3.0.46/lib/portage/elog/mod_syslog.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/defaults.py` & `portage-3.0.46/lib/portage/emaint/defaults.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/main.py` & `portage-3.0.46/lib/portage/emaint/main.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/binhost/__init__.py` & `portage-3.0.46/lib/portage/emaint/modules/binhost/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/binhost/binhost.py` & `portage-3.0.46/lib/portage/emaint/modules/binhost/binhost.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/config/__init__.py` & `portage-3.0.46/lib/portage/emaint/modules/config/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/config/config.py` & `portage-3.0.46/lib/portage/emaint/modules/config/config.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/logs/__init__.py` & `portage-3.0.46/lib/portage/emaint/modules/logs/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/logs/logs.py` & `portage-3.0.46/lib/portage/emaint/modules/logs/logs.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/merges/__init__.py` & `portage-3.0.46/lib/portage/emaint/modules/merges/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/merges/merges.py` & `portage-3.0.46/lib/portage/emaint/modules/merges/merges.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/move/__init__.py` & `portage-3.0.46/lib/portage/emaint/modules/move/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/move/move.py` & `portage-3.0.46/lib/portage/emaint/modules/move/move.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/resume/__init__.py` & `portage-3.0.46/lib/portage/emaint/modules/resume/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/resume/resume.py` & `portage-3.0.46/lib/portage/emaint/modules/resume/resume.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/sync/__init__.py` & `portage-3.0.46/lib/portage/emaint/modules/sync/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/sync/sync.py` & `portage-3.0.46/lib/portage/emaint/modules/sync/sync.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/emaint/modules/world/world.py` & `portage-3.0.46/lib/portage/emaint/modules/world/world.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/env/config.py` & `portage-3.0.46/lib/portage/env/config.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/env/loaders.py` & `portage-3.0.46/lib/portage/env/loaders.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/env/validators.py` & `portage-3.0.46/lib/portage/env/validators.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/exception.py` & `portage-3.0.46/lib/portage/exception.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/getbinpkg.py` & `portage-3.0.46/lib/portage/getbinpkg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/glsa.py` & `portage-3.0.46/lib/portage/glsa.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/gpg.py` & `portage-3.0.46/lib/portage/gpg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/gpkg.py` & `portage-3.0.46/lib/portage/gpkg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/localization.py` & `portage-3.0.46/lib/portage/localization.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/locks.py` & `portage-3.0.46/lib/portage/locks.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/mail.py` & `portage-3.0.46/lib/portage/mail.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/manifest.py` & `portage-3.0.46/lib/portage/manifest.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/metadata.py` & `portage-3.0.46/lib/portage/metadata.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/module.py` & `portage-3.0.46/lib/portage/module.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/news.py` & `portage-3.0.46/lib/portage/news.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/output.py` & `portage-3.0.46/lib/portage/output.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/KeywordsManager.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/KeywordsManager.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/LicenseManager.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/LicenseManager.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/LocationsManager.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/LocationsManager.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/MaskManager.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/MaskManager.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/UseManager.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/UseManager.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/VirtualsManager.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/VirtualsManager.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/env_var_validation.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/env_var_validation.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/features_set.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/features_set.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/helper.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/helper.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_config/special_env_vars.py` & `portage-3.0.46/lib/portage/package/ebuild/_config/special_env_vars.py`

 * *Files 1% similar despite different names*

```diff
@@ -110,14 +110,15 @@
         "EROOT",
         "ESYSROOT",
         "FEATURES",
         "FILESDIR",
         "HOME",
         "MERGE_TYPE",
         "NOCOLOR",
+        "NO_COLOR",
         "P",
         "PATH",
         "PF",
         "PKGDIR",
         "PKGUSE",
         "PKG_LOGDIR",
         "PKG_TMPDIR",
@@ -354,8 +355,9 @@
 )
 
 # To enhance usability, make some vars case insensitive
 # by forcing them to lower case.
 case_insensitive_vars = (
     "AUTOCLEAN",
     "NOCOLOR",
+    "NO_COLOR",
 )
```

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_ipc/ExitCommand.py` & `portage-3.0.46/lib/portage/package/ebuild/_ipc/ExitCommand.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_ipc/QueryCommand.py` & `portage-3.0.46/lib/portage/package/ebuild/_ipc/QueryCommand.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 import portage
 from portage import os
 from portage.dep import Atom, _repo_name_re
 from portage.eapi import eapi_has_repo_deps
 from portage.elog import messages as elog_messages
 from portage.exception import InvalidAtom
 from portage.package.ebuild._ipc.IpcCommand import IpcCommand
-from portage.util import normalize_path
+from portage.util import normalize_path, no_color
 from portage.versions import best
 
 
 class QueryCommand(IpcCommand):
     __slots__ = (
         "phase",
         "settings",
@@ -145,16 +145,14 @@
         compression.
         """
         out = io.StringIO()
         phase = self.phase
         elog_func = getattr(elog_messages, elog_funcname)
         global_havecolor = portage.output.havecolor
         try:
-            portage.output.havecolor = self.settings.get(
-                "NOCOLOR", "false"
-            ).lower() in ("no", "false")
+            portage.output.havecolor = not no_color(self.settings)
             for line in lines:
                 elog_func(line, phase=phase, key=self.settings.mycpv, out=out)
         finally:
             portage.output.havecolor = global_havecolor
         msg = out.getvalue()
         return msg
```

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_metadata_invalid.py` & `portage-3.0.46/lib/portage/package/ebuild/_metadata_invalid.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/ManifestProcess.py` & `portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/ManifestProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/ManifestScheduler.py` & `portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/ManifestScheduler.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_parallel_manifest/ManifestTask.py` & `portage-3.0.46/lib/portage/package/ebuild/_parallel_manifest/ManifestTask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/_spawn_nofetch.py` & `portage-3.0.46/lib/portage/package/ebuild/_spawn_nofetch.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/config.py` & `portage-3.0.46/lib/portage/package/ebuild/config.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/deprecated_profile_check.py` & `portage-3.0.46/lib/portage/package/ebuild/deprecated_profile_check.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/digestcheck.py` & `portage-3.0.46/lib/portage/package/ebuild/digestcheck.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/digestgen.py` & `portage-3.0.46/lib/portage/package/ebuild/digestgen.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/doebuild.py` & `portage-3.0.46/lib/portage/package/ebuild/doebuild.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/fetch.py` & `portage-3.0.46/lib/portage/package/ebuild/fetch.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/getmaskingreason.py` & `portage-3.0.46/lib/portage/package/ebuild/getmaskingreason.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/getmaskingstatus.py` & `portage-3.0.46/lib/portage/package/ebuild/getmaskingstatus.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/prepare_build_dirs.py` & `portage-3.0.46/lib/portage/package/ebuild/prepare_build_dirs.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/package/ebuild/profile_iuse.py` & `portage-3.0.46/lib/portage/package/ebuild/profile_iuse.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/process.py` & `portage-3.0.46/lib/portage/process.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/progress.py` & `portage-3.0.46/lib/portage/progress.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/proxy/lazyimport.py` & `portage-3.0.46/lib/portage/proxy/lazyimport.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/proxy/objectproxy.py` & `portage-3.0.46/lib/portage/proxy/objectproxy.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/repository/config.py` & `portage-3.0.46/lib/portage/repository/config.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/repository/storage/hardlink_quarantine.py` & `portage-3.0.46/lib/portage/repository/storage/hardlink_quarantine.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/repository/storage/hardlink_rcu.py` & `portage-3.0.46/lib/portage/repository/storage/hardlink_rcu.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/repository/storage/inplace.py` & `portage-3.0.46/lib/portage/repository/storage/inplace.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/repository/storage/interface.py` & `portage-3.0.46/lib/portage/repository/storage/interface.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/__init__.py` & `portage-3.0.46/lib/portage/sync/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/config_checks.py` & `portage-3.0.46/lib/portage/sync/config_checks.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/controller.py` & `portage-3.0.46/lib/portage/sync/controller.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/getaddrinfo_validate.py` & `portage-3.0.46/lib/portage/sync/getaddrinfo_validate.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/cvs/__init__.py` & `portage-3.0.46/lib/portage/sync/modules/cvs/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/cvs/cvs.py` & `portage-3.0.46/lib/portage/sync/modules/cvs/cvs.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/git/__init__.py` & `portage-3.0.46/lib/portage/sync/modules/git/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/git/git.py` & `portage-3.0.46/lib/portage/sync/modules/git/git.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/mercurial/__init__.py` & `portage-3.0.46/lib/portage/sync/modules/mercurial/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/mercurial/mercurial.py` & `portage-3.0.46/lib/portage/sync/modules/mercurial/mercurial.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/rsync/__init__.py` & `portage-3.0.46/lib/portage/sync/modules/rsync/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/rsync/rsync.py` & `portage-3.0.46/lib/portage/sync/modules/rsync/rsync.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/svn/__init__.py` & `portage-3.0.46/lib/portage/sync/modules/svn/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/svn/svn.py` & `portage-3.0.46/lib/portage/sync/modules/svn/svn.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/webrsync/__init__.py` & `portage-3.0.46/lib/portage/sync/modules/webrsync/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/modules/webrsync/webrsync.py` & `portage-3.0.46/lib/portage/sync/modules/webrsync/webrsync.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/old_tree_timestamp.py` & `portage-3.0.46/lib/portage/sync/old_tree_timestamp.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/sync/syncbase.py` & `portage-3.0.46/lib/portage/sync/syncbase.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/.gnupg/openpgp-revocs.d/06B3A311BD775C280D22A9305D90EA06352177F6.rev` & `portage-3.0.46/lib/portage/tests/.gnupg/openpgp-revocs.d/06B3A311BD775C280D22A9305D90EA06352177F6.rev`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/.gnupg/openpgp-revocs.d/8DEDA2CDED49C8809287B89D8812797DDF1DD192.rev` & `portage-3.0.46/lib/portage/tests/.gnupg/openpgp-revocs.d/8DEDA2CDED49C8809287B89D8812797DDF1DD192.rev`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/.gnupg/private-keys-v1.d/273B030399E7BEA66A9AD42216DE7CA17BA5D42E.key` & `portage-3.0.46/lib/portage/tests/.gnupg/private-keys-v1.d/273B030399E7BEA66A9AD42216DE7CA17BA5D42E.key`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/.gnupg/private-keys-v1.d/C99796FB85B0C3DF03314A11B5850C51167D6282.key` & `portage-3.0.46/lib/portage/tests/.gnupg/private-keys-v1.d/C99796FB85B0C3DF03314A11B5850C51167D6282.key`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/.gnupg/pubring.kbx` & `portage-3.0.46/lib/portage/tests/.gnupg/pubring.kbx`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/.gnupg/trustdb.gpg` & `portage-3.0.46/lib/portage/tests/.gnupg/trustdb.gpg`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/__init__.py` & `portage-3.0.46/lib/portage/tests/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,14 +8,15 @@
 import unittest
 from pathlib import Path
 
 from unittest.runner import TextTestResult as _TextTestResult
 
 import portage
 from portage import os
+from portage.util import no_color
 from portage import _encodings
 from portage import _unicode_decode
 from portage.output import colorize
 from portage.proxy.objectproxy import ObjectProxy
 
 
 # This remains constant when the real value is a mock.
@@ -74,15 +75,15 @@
     parser.add_argument(
         "-l", "--list", help="list all tests", action="store_true", dest="list_tests"
     )
     parser.add_argument("tests", nargs="*", type=Path)
     options = parser.parse_args(args=sys.argv)
 
     if (
-        os.environ.get("NOCOLOR") in ("yes", "true")
+        no_color(os.environ)
         or os.environ.get("TERM") == "dumb"
         or not sys.stdout.isatty()
     ):
         portage.output.nocolor()
 
     if options.list_tests:
         testdir = argv0.parent
```

### Comparing `portage-3.0.45.3/lib/portage/tests/bin/setup_env.py` & `portage-3.0.46/lib/portage/tests/bin/setup_env.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/bin/test_dobin.py` & `portage-3.0.46/lib/portage/tests/bin/test_dobin.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/bin/test_dodir.py` & `portage-3.0.46/lib/portage/tests/bin/test_dodir.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/bin/test_doins.py` & `portage-3.0.46/lib/portage/tests/bin/test_doins.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/bin/test_eapi7_ver_funcs.py` & `portage-3.0.46/lib/portage/tests/bin/test_eapi7_ver_funcs.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/bin/test_filter_bash_env.py` & `portage-3.0.46/lib/portage/tests/bin/test_filter_bash_env.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dbapi/test_auxdb.py` & `portage-3.0.46/lib/portage/tests/dbapi/test_auxdb.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dbapi/test_bintree.py` & `portage-3.0.46/lib/portage/tests/dbapi/test_bintree.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dbapi/test_fakedbapi.py` & `portage-3.0.46/lib/portage/tests/dbapi/test_fakedbapi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dbapi/test_portdb_cache.py` & `portage-3.0.46/lib/portage/tests/dbapi/test_portdb_cache.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/testAtom.py` & `portage-3.0.46/lib/portage/tests/dep/testAtom.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/testCheckRequiredUse.py` & `portage-3.0.46/lib/portage/tests/dep/testCheckRequiredUse.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/testExtendedAtomDict.py` & `portage-3.0.46/lib/portage/tests/dep/testExtendedAtomDict.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/testExtractAffectingUSE.py` & `portage-3.0.46/lib/portage/tests/dep/testExtractAffectingUSE.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/testStandalone.py` & `portage-3.0.46/lib/portage/tests/dep/testStandalone.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_best_match_to_list.py` & `portage-3.0.46/lib/portage/tests/dep/test_best_match_to_list.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_dep_getcpv.py` & `portage-3.0.46/lib/portage/tests/dep/test_dep_getcpv.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_dep_getrepo.py` & `portage-3.0.46/lib/portage/tests/dep/test_dep_getrepo.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_dep_getslot.py` & `portage-3.0.46/lib/portage/tests/dep/test_dep_getslot.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_dep_getusedeps.py` & `portage-3.0.46/lib/portage/tests/dep/test_dep_getusedeps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_dnf_convert.py` & `portage-3.0.46/lib/portage/tests/dep/test_dnf_convert.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_get_operator.py` & `portage-3.0.46/lib/portage/tests/dep/test_get_operator.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_get_required_use_flags.py` & `portage-3.0.46/lib/portage/tests/dep/test_get_required_use_flags.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_isjustname.py` & `portage-3.0.46/lib/portage/tests/dep/test_isjustname.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_isvalidatom.py` & `portage-3.0.46/lib/portage/tests/dep/test_isvalidatom.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_match_from_list.py` & `portage-3.0.46/lib/portage/tests/dep/test_match_from_list.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_overlap_dnf.py` & `portage-3.0.46/lib/portage/tests/dep/test_overlap_dnf.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_paren_reduce.py` & `portage-3.0.46/lib/portage/tests/dep/test_paren_reduce.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_soname_atom_pickle.py` & `portage-3.0.46/lib/portage/tests/dep/test_soname_atom_pickle.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/dep/test_use_reduce.py` & `portage-3.0.46/lib/portage/tests/dep/test_use_reduce.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_array_fromfile_eof.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_array_fromfile_eof.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_config.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_config.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_doebuild_fd_pipes.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_doebuild_fd_pipes.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_doebuild_spawn.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_doebuild_spawn.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_fetch.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_fetch.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_ipc_daemon.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_ipc_daemon.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_shell_quote.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_shell_quote.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_spawn.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_spawn.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/ebuild/test_use_expand_incremental.py` & `portage-3.0.46/lib/portage/tests/ebuild/test_use_expand_incremental.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/emerge/test_actions.py` & `portage-3.0.46/lib/portage/tests/emerge/test_actions.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/emerge/test_config_protect.py` & `portage-3.0.46/lib/portage/tests/emerge/test_config_protect.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/emerge/test_emerge_blocker_file_collision.py` & `portage-3.0.46/lib/portage/tests/emerge/test_emerge_blocker_file_collision.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/emerge/test_emerge_slot_abi.py` & `portage-3.0.46/lib/portage/tests/emerge/test_emerge_slot_abi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/emerge/test_global_updates.py` & `portage-3.0.46/lib/portage/tests/emerge/test_global_updates.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/emerge/test_simple.py` & `portage-3.0.46/lib/portage/tests/emerge/test_simple.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/env/config/test_PackageKeywordsFile.py` & `portage-3.0.46/lib/portage/tests/env/config/test_PackageKeywordsFile.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/env/config/test_PackageMaskFile.py` & `portage-3.0.46/lib/portage/tests/env/config/test_PackageMaskFile.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/env/config/test_PackageUseFile.py` & `portage-3.0.46/lib/portage/tests/env/config/test_PackageUseFile.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/env/config/test_PortageModulesFile.py` & `portage-3.0.46/lib/portage/tests/env/config/test_PortageModulesFile.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/glsa/test_security_set.py` & `portage-3.0.46/lib/portage/tests/glsa/test_security_set.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_checksum.py` & `portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_checksum.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_gpg.py` & `portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_gpg.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_metadata_update.py` & `portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_metadata_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_metadata_url.py` & `portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_metadata_url.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_path.py` & `portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_path.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_size.py` & `portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_size.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/gpkg/test_gpkg_stream.py` & `portage-3.0.46/lib/portage/tests/gpkg/test_gpkg_stream.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/lafilefixer/test_lafilefixer.py` & `portage-3.0.46/lib/portage/tests/lafilefixer/test_lafilefixer.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/lazyimport/test_lazy_import_portage_baseline.py` & `portage-3.0.46/lib/portage/tests/lazyimport/test_lazy_import_portage_baseline.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/lazyimport/test_preload_portage_submodules.py` & `portage-3.0.46/lib/portage/tests/lazyimport/test_preload_portage_submodules.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/lint/test_bash_syntax.py` & `portage-3.0.46/lib/portage/tests/lint/test_bash_syntax.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/lint/test_compile_modules.py` & `portage-3.0.46/lib/portage/tests/lint/test_compile_modules.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/lint/test_import_modules.py` & `portage-3.0.46/lib/portage/tests/lint/test_import_modules.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/locks/test_asynchronous_lock.py` & `portage-3.0.46/lib/portage/tests/locks/test_asynchronous_lock.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/locks/test_lock_nonblock.py` & `portage-3.0.46/lib/portage/tests/locks/test_lock_nonblock.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/news/test_NewsItem.py` & `portage-3.0.46/lib/portage/tests/news/test_NewsItem.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_AsyncFunction.py` & `portage-3.0.46/lib/portage/tests/process/test_AsyncFunction.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_PipeLogger.py` & `portage-3.0.46/lib/portage/tests/process/test_PipeLogger.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_PopenProcess.py` & `portage-3.0.46/lib/portage/tests/process/test_PopenProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_PopenProcessBlockingIO.py` & `portage-3.0.46/lib/portage/tests/process/test_PopenProcessBlockingIO.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_poll.py` & `portage-3.0.46/lib/portage/tests/process/test_poll.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_spawn_fail_e2big.py` & `portage-3.0.46/lib/portage/tests/process/test_spawn_fail_e2big.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_spawn_warn_large_env.py` & `portage-3.0.46/lib/portage/tests/process/test_spawn_warn_large_env.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/process/test_unshare_net.py` & `portage-3.0.46/lib/portage/tests/process/test_unshare_net.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/ResolverPlayground.py` & `portage-3.0.46/lib/portage/tests/resolver/ResolverPlayground.py`

 * *Files 1% similar despite different names*

```diff
@@ -583,16 +583,16 @@
             "FEATURES": "${FEATURES} binpkg-signing gpg-keepalive",
             "PKGDIR": self.pkgdir,
             "PORTAGE_INST_GID": str(portage.data.portage_gid),
             "PORTAGE_INST_UID": str(portage.data.portage_uid),
             "PORTAGE_TMPDIR": os.path.join(self.eroot, "var/tmp"),
         }
 
-        if os.environ.get("NOCOLOR"):
-            make_conf["NOCOLOR"] = os.environ["NOCOLOR"]
+        if portage.util.no_color(os.environ):
+            make_conf["NO_COLOR"] = os.environ["NO_COLOR"]
 
         # Pass along PORTAGE_USERNAME and PORTAGE_GRPNAME since they
         # need to be inherited by ebuild subprocesses.
         if "PORTAGE_USERNAME" in os.environ:
             make_conf["PORTAGE_USERNAME"] = os.environ["PORTAGE_USERNAME"]
         if "PORTAGE_GRPNAME" in os.environ:
             make_conf["PORTAGE_GRPNAME"] = os.environ["PORTAGE_GRPNAME"]
```

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/binpkg_multi_instance/test_build_id_profile_format.py` & `portage-3.0.46/lib/portage/tests/resolver/binpkg_multi_instance/test_build_id_profile_format.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/binpkg_multi_instance/test_rebuilt_binaries.py` & `portage-3.0.46/lib/portage/tests/resolver/binpkg_multi_instance/test_rebuilt_binaries.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_autounmask.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_autounmask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_depclean.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_depclean.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_downgrade.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_downgrade.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_or_choices.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_or_choices.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_reinstall.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_reinstall.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_skip_update.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_skip_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_slot_conflict_reinstall.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_slot_conflict_reinstall.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_slot_conflict_update.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_slot_conflict_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_soname_provided.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_soname_provided.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_unsatisfiable.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_unsatisfiable.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/soname/test_unsatisfied.py` & `portage-3.0.46/lib/portage/tests/resolver/soname/test_unsatisfied.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_aggressive_backtrack_downgrade.py` & `portage-3.0.46/lib/portage/tests/resolver/test_aggressive_backtrack_downgrade.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_binpkg_use.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask_binpkg_use.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_keep_keywords.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask_keep_keywords.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_multilib_use.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask_multilib_use.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_parent.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask_parent.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_use_backtrack.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask_use_backtrack.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_use_breakage.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask_use_breakage.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_autounmask_use_slot_conflict.py` & `portage-3.0.46/lib/portage/tests/resolver/test_autounmask_use_slot_conflict.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_backtracking.py` & `portage-3.0.46/lib/portage/tests/resolver/test_backtracking.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_bdeps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_bdeps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_binary_pkg_ebuild_visibility.py` & `portage-3.0.46/lib/portage/tests/resolver/test_binary_pkg_ebuild_visibility.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_blocker.py` & `portage-3.0.46/lib/portage/tests/resolver/test_blocker.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_changed_deps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_changed_deps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_circular_choices.py` & `portage-3.0.46/lib/portage/tests/resolver/test_circular_choices.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_circular_choices_rust.py` & `portage-3.0.46/lib/portage/tests/resolver/test_circular_choices_rust.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_circular_dependencies.py` & `portage-3.0.46/lib/portage/tests/resolver/test_circular_dependencies.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_complete_graph.py` & `portage-3.0.46/lib/portage/tests/resolver/test_complete_graph.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_complete_if_new_subslot_without_revbump.py` & `portage-3.0.46/lib/portage/tests/resolver/test_complete_if_new_subslot_without_revbump.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_depclean.py` & `portage-3.0.46/lib/portage/tests/resolver/test_depclean.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_depclean_order.py` & `portage-3.0.46/lib/portage/tests/resolver/test_depclean_order.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_depclean_slot_unavailable.py` & `portage-3.0.46/lib/portage/tests/resolver/test_depclean_slot_unavailable.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_depth.py` & `portage-3.0.46/lib/portage/tests/resolver/test_depth.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_disjunctive_depend_order.py` & `portage-3.0.46/lib/portage/tests/resolver/test_disjunctive_depend_order.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_eapi.py` & `portage-3.0.46/lib/portage/tests/resolver/test_eapi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_features_test_use.py` & `portage-3.0.46/lib/portage/tests/resolver/test_features_test_use.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_imagemagick_graphicsmagick.py` & `portage-3.0.46/lib/portage/tests/resolver/test_imagemagick_graphicsmagick.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_installkernel.py` & `portage-3.0.46/lib/portage/tests/resolver/test_installkernel.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_keywords.py` & `portage-3.0.46/lib/portage/tests/resolver/test_keywords.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_merge_order.py` & `portage-3.0.46/lib/portage/tests/resolver/test_merge_order.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_missing_iuse_and_evaluated_atoms.py` & `portage-3.0.46/lib/portage/tests/resolver/test_missing_iuse_and_evaluated_atoms.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_multirepo.py` & `portage-3.0.46/lib/portage/tests/resolver/test_multirepo.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_multislot.py` & `portage-3.0.46/lib/portage/tests/resolver/test_multislot.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_old_dep_chain_display.py` & `portage-3.0.46/lib/portage/tests/resolver/test_old_dep_chain_display.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_onlydeps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps_circular.py` & `portage-3.0.46/lib/portage/tests/resolver/test_onlydeps_circular.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps_ideps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_onlydeps_ideps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_onlydeps_minimal.py` & `portage-3.0.46/lib/portage/tests/resolver/test_onlydeps_minimal.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_or_choices.py` & `portage-3.0.46/lib/portage/tests/resolver/test_or_choices.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_or_downgrade_installed.py` & `portage-3.0.46/lib/portage/tests/resolver/test_or_downgrade_installed.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_or_upgrade_installed.py` & `portage-3.0.46/lib/portage/tests/resolver/test_or_upgrade_installed.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_output.py` & `portage-3.0.46/lib/portage/tests/resolver/test_output.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_package_tracker.py` & `portage-3.0.46/lib/portage/tests/resolver/test_package_tracker.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_profile_default_eapi.py` & `portage-3.0.46/lib/portage/tests/resolver/test_profile_default_eapi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_profile_package_set.py` & `portage-3.0.46/lib/portage/tests/resolver/test_profile_package_set.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_rebuild.py` & `portage-3.0.46/lib/portage/tests/resolver/test_rebuild.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_regular_slot_change_without_revbump.py` & `portage-3.0.46/lib/portage/tests/resolver/test_regular_slot_change_without_revbump.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_required_use.py` & `portage-3.0.46/lib/portage/tests/resolver/test_required_use.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_runtime_cycle_merge_order.py` & `portage-3.0.46/lib/portage/tests/resolver/test_runtime_cycle_merge_order.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_simple.py` & `portage-3.0.46/lib/portage/tests/resolver/test_simple.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_abi.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_abi.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_abi_downgrade.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_abi_downgrade.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_change_without_revbump.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_change_without_revbump.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_collisions.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_collisions.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_force_rebuild.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_force_rebuild.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_mask_update.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_mask_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_rebuild.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_rebuild.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_unsatisfied_deep_deps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_unsatisfied_deep_deps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_update.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_conflict_update_virt.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_conflict_update_virt.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_autounmask.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_autounmask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_bdeps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_bdeps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_complete_graph.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_complete_graph.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_exclusive_slots.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_exclusive_slots.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_missed_update.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_missed_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_rebuild.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_rebuild.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_required_use.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_required_use.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_reverse_deps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_reverse_deps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_runtime_pkg_mask.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_runtime_pkg_mask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_unsatisfied.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_unsatisfied.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_unsolved.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_unsolved.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_slot_operator_update_probe_parent_downgrade.py` & `portage-3.0.46/lib/portage/tests/resolver/test_slot_operator_update_probe_parent_downgrade.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_solve_non_slot_operator_slot_conflicts.py` & `portage-3.0.46/lib/portage/tests/resolver/test_solve_non_slot_operator_slot_conflicts.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_targetroot.py` & `portage-3.0.46/lib/portage/tests/resolver/test_targetroot.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_unecessary_slot_upgrade.py` & `portage-3.0.46/lib/portage/tests/resolver/test_unecessary_slot_upgrade.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_unmerge_order.py` & `portage-3.0.46/lib/portage/tests/resolver/test_unmerge_order.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_update.py` & `portage-3.0.46/lib/portage/tests/resolver/test_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_use_dep_defaults.py` & `portage-3.0.46/lib/portage/tests/resolver/test_use_dep_defaults.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_useflags.py` & `portage-3.0.46/lib/portage/tests/resolver/test_useflags.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_virtual_minimize_children.py` & `portage-3.0.46/lib/portage/tests/resolver/test_virtual_minimize_children.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_virtual_slot.py` & `portage-3.0.46/lib/portage/tests/resolver/test_virtual_slot.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/resolver/test_with_test_deps.py` & `portage-3.0.46/lib/portage/tests/resolver/test_with_test_deps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/runTests.py` & `portage-3.0.46/lib/portage/tests/runTests.py`

 * *Files 4% similar despite different names*

```diff
@@ -36,15 +36,15 @@
 
 portage._internal_caller = True
 
 # Ensure that we don't instantiate portage.settings, so that tests should
 # work the same regardless of global configuration file state/existence.
 portage._disable_legacy_globals()
 
-if os.environ.get("NOCOLOR") in ("yes", "true"):
+if portage.util.no_color(os.environ):
     portage.output.nocolor()
 
 import portage.tests as tests
 from portage.util._eventloop.global_event_loop import global_event_loop
 from portage.const import PORTAGE_BIN_PATH
 
 path = os.environ.get("PATH", "").split(":")
```

### Comparing `portage-3.0.45.3/lib/portage/tests/sets/base/testInternalPackageSet.py` & `portage-3.0.46/lib/portage/tests/sets/base/testInternalPackageSet.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/sets/base/testVariableSet.py` & `portage-3.0.46/lib/portage/tests/sets/base/testVariableSet.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/sets/files/testConfigFileSet.py` & `portage-3.0.46/lib/portage/tests/sets/files/testConfigFileSet.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/sets/files/testStaticFileSet.py` & `portage-3.0.46/lib/portage/tests/sets/files/testStaticFileSet.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/sets/shell/testShell.py` & `portage-3.0.46/lib/portage/tests/sets/shell/testShell.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/sync/test_sync_local.py` & `portage-3.0.46/lib/portage/tests/sync/test_sync_local.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/unicode/test_string_format.py` & `portage-3.0.46/lib/portage/tests/unicode/test_string_format.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/update/test_move_ent.py` & `portage-3.0.46/lib/portage/tests/update/test_move_ent.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/update/test_move_slot_ent.py` & `portage-3.0.46/lib/portage/tests/update/test_move_slot_ent.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/update/test_update_dbentry.py` & `portage-3.0.46/lib/portage/tests/update/test_update_dbentry.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/dyn_libs/test_soname_deps.py` & `portage-3.0.46/lib/portage/tests/util/dyn_libs/test_soname_deps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/eventloop/test_call_soon_fifo.py` & `portage-3.0.46/lib/portage/tests/util/eventloop/test_call_soon_fifo.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/file_copy/test_copyfile.py` & `portage-3.0.46/lib/portage/tests/util/file_copy/test_copyfile.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_child_watcher.py` & `portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_child_watcher.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_event_loop_in_fork.py` & `portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_event_loop_in_fork.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_pipe_closed.py` & `portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_pipe_closed.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_policy_wrapper_recursion.py` & `portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_policy_wrapper_recursion.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_run_until_complete.py` & `portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_run_until_complete.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_subprocess_exec.py` & `portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_subprocess_exec.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/asyncio/test_wakeup_fd_sigchld.py` & `portage-3.0.46/lib/portage/tests/util/futures/asyncio/test_wakeup_fd_sigchld.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/test_compat_coroutine.py` & `portage-3.0.46/lib/portage/tests/util/futures/test_compat_coroutine.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/test_done_callback.py` & `portage-3.0.46/lib/portage/tests/util/futures/test_done_callback.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/test_done_callback_after_exit.py` & `portage-3.0.46/lib/portage/tests/util/futures/test_done_callback_after_exit.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/test_iter_completed.py` & `portage-3.0.46/lib/portage/tests/util/futures/test_iter_completed.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/futures/test_retry.py` & `portage-3.0.46/lib/portage/tests/util/futures/test_retry.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_checksum.py` & `portage-3.0.46/lib/portage/tests/util/test_checksum.py`

 * *Files 15% similar despite different names*

```diff
@@ -117,40 +117,14 @@
             self.assertEqual(
                 checksum_str(self.text, "SHA3_512"),
                 "6634c004dc31822fa65c2f1e2e3bbf0cfa35085653cca1ca9ca42f8f3f13c908405e0b665918146181c9fc9a9d793fc05429d669c35a55517820dfaa071425ca",
             )
         except DigestException:
             self.skipTest("SHA3_512 implementation not available")
 
-    def test_streebog256(self):
-        try:
-            self.assertEqual(
-                checksum_str(b"", "STREEBOG256"),
-                "3f539a213e97c802cc229d474c6aa32a825a360b2a933a949fd925208d9ce1bb",
-            )
-            self.assertEqual(
-                checksum_str(self.text, "STREEBOG256"),
-                "4992f1239c46f15b89e7b83ded4d83fb5966da3692788a4a1a6d118f78c08444",
-            )
-        except DigestException:
-            self.skipTest("STREEBOG256 implementation not available")
-
-    def test_streebog512(self):
-        try:
-            self.assertEqual(
-                checksum_str(b"", "STREEBOG512"),
-                "8e945da209aa869f0455928529bcae4679e9873ab707b55315f56ceb98bef0a7362f715528356ee83cda5f2aac4c6ad2ba3a715c1bcd81cb8e9f90bf4c1c1a8a",
-            )
-            self.assertEqual(
-                checksum_str(self.text, "STREEBOG512"),
-                "330f5c26437f4e22c0163c72b12e93b8c27202f0750627355bdee43a0e0b253c90fbf0a27adbe5414019ff01ed84b7b240a1da1cbe10fae3adffc39c2d87a51f",
-            )
-        except DigestException:
-            self.skipTest("STREEBOG512 implementation not available")
-
 
 class ApplyHashFilterTestCase(TestCase):
     def test_apply_hash_filter(self):
         indict = {"MD5": "", "SHA1": "", "SHA256": "", "size": ""}
 
         self.assertEqual(
             sorted(_apply_hash_filter(indict, lambda x: True)),
```

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_digraph.py` & `portage-3.0.46/lib/portage/tests/util/test_digraph.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_file_copier.py` & `portage-3.0.46/lib/portage/tests/util/test_file_copier.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_getconfig.py` & `portage-3.0.46/lib/portage/tests/util/test_getconfig.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_install_mask.py` & `portage-3.0.46/lib/portage/tests/util/test_install_mask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_manifest.py` & `portage-3.0.46/lib/portage/tests/util/test_manifest.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_mtimedb.py` & `portage-3.0.46/lib/portage/tests/util/test_mtimedb.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_shelve.py` & `portage-3.0.46/lib/portage/tests/util/test_shelve.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Copyright 2020-2021 Gentoo Authors
+# Copyright 2020-2023 Gentoo Authors
 # Distributed under the terms of the GNU General Public License v2
 
 import argparse
 import os
 import shutil
 import tempfile
 import time
@@ -40,15 +40,14 @@
                 )
                 db = open_shelve(dump_args.src, flag="c")
                 for k, v in data.items():
                     db[k] = v
                 db.close()
                 dump(dump_args)
 
-                os.unlink(dump_args.src)
                 restore_args = argparse.Namespace(
                     dest=dump_args.src,
                     src=dump_args.dest,
                 )
                 restore(restore_args)
 
                 db = open_shelve(restore_args.dest, flag="r")
```

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_socks5.py` & `portage-3.0.46/lib/portage/tests/util/test_socks5.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_stackDictList.py` & `portage-3.0.46/lib/portage/tests/util/test_stackDictList.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_stackDicts.py` & `portage-3.0.46/lib/portage/tests/util/test_stackDicts.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_stackLists.py` & `portage-3.0.46/lib/portage/tests/util/test_stackLists.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_uniqueArray.py` & `portage-3.0.46/lib/portage/tests/util/test_uniqueArray.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_varExpand.py` & `portage-3.0.46/lib/portage/tests/util/test_varExpand.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_whirlpool.py` & `portage-3.0.46/lib/portage/tests/util/test_whirlpool.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/util/test_xattr.py` & `portage-3.0.46/lib/portage/tests/util/test_xattr.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/versions/test_cpv_sort_key.py` & `portage-3.0.46/lib/portage/tests/versions/test_cpv_sort_key.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/tests/versions/test_vercmp.py` & `portage-3.0.46/lib/portage/tests/versions/test_vercmp.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/update.py` & `portage-3.0.46/lib/portage/update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/ExtractKernelVersion.py` & `portage-3.0.46/lib/portage/util/ExtractKernelVersion.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/SlotObject.py` & `portage-3.0.46/lib/portage/util/SlotObject.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/__init__.py` & `portage-3.0.46/lib/portage/util/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -52,14 +52,15 @@
     "unique_everseen",
     "varexpand",
     "write_atomic",
     "writedict",
     "writemsg",
     "writemsg_level",
     "writemsg_stdout",
+    "no_color",
 ]
 
 from contextlib import AbstractContextManager
 from copy import deepcopy
 import errno
 import io
 from itertools import chain, filterfalse
@@ -67,14 +68,15 @@
 import re
 import shlex
 import stat
 import string
 import sys
 import traceback
 import glob
+from typing import Optional
 
 import portage
 
 portage.proxy.lazyimport.lazyimport(
     globals(),
     "pickle",
     "portage.dep:Atom",
@@ -2002,7 +2004,16 @@
     # the following is based on the information from ld.so(8)
     rval = env.get("LD_LIBRARY_PATH", "").split(":")
     rval.extend(read_ld_so_conf(os.path.join(root, "etc", "ld.so.conf")))
     rval.append("/usr/lib")
     rval.append("/lib")
 
     return [normalize_path(x) for x in rval if x]
+
+
+def no_color(settings: Optional[dict]) -> bool:
+    # In several years (2026+), we can cleanup NOCOLOR support, and just support NO_COLOR.
+    has_color: str = settings.get("NO_COLOR")
+    nocolor: str = settings.get("NOCOLOR", "false").lower()
+    if has_color is None:
+        return nocolor in ("yes", "true")
+    return bool(has_color)
```

### Comparing `portage-3.0.45.3/lib/portage/util/_async/AsyncFunction.py` & `portage-3.0.46/lib/portage/util/_async/AsyncFunction.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/AsyncScheduler.py` & `portage-3.0.46/lib/portage/util/_async/AsyncScheduler.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/AsyncTaskFuture.py` & `portage-3.0.46/lib/portage/util/_async/AsyncTaskFuture.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/BuildLogger.py` & `portage-3.0.46/lib/portage/util/_async/BuildLogger.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/FileCopier.py` & `portage-3.0.46/lib/portage/util/_async/FileCopier.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/FileDigester.py` & `portage-3.0.46/lib/portage/util/_async/FileDigester.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/ForkProcess.py` & `portage-3.0.46/lib/portage/util/_async/ForkProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/PipeLogger.py` & `portage-3.0.46/lib/portage/util/_async/PipeLogger.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/PipeReaderBlockingIO.py` & `portage-3.0.46/lib/portage/util/_async/PipeReaderBlockingIO.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/PopenProcess.py` & `portage-3.0.46/lib/portage/util/_async/PopenProcess.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/SchedulerInterface.py` & `portage-3.0.46/lib/portage/util/_async/SchedulerInterface.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/TaskScheduler.py` & `portage-3.0.46/lib/portage/util/_async/TaskScheduler.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_async/run_main_scheduler.py` & `portage-3.0.46/lib/portage/util/_async/run_main_scheduler.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_compare_files.py` & `portage-3.0.46/lib/portage/util/_compare_files.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_ctypes.py` & `portage-3.0.46/lib/portage/util/_ctypes.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_desktop_entry.py` & `portage-3.0.46/lib/portage/util/_desktop_entry.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_dyn_libs/LinkageMapELF.py` & `portage-3.0.46/lib/portage/util/_dyn_libs/LinkageMapELF.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_dyn_libs/NeededEntry.py` & `portage-3.0.46/lib/portage/util/_dyn_libs/NeededEntry.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_dyn_libs/PreservedLibsRegistry.py` & `portage-3.0.46/lib/portage/util/_dyn_libs/PreservedLibsRegistry.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_dyn_libs/display_preserved_libs.py` & `portage-3.0.46/lib/portage/util/_dyn_libs/display_preserved_libs.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_dyn_libs/dyn_libs.py` & `portage-3.0.46/lib/portage/util/_dyn_libs/dyn_libs.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_dyn_libs/soname_deps.py` & `portage-3.0.46/lib/portage/util/_dyn_libs/soname_deps.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_dyn_libs/soname_deps_qa.py` & `portage-3.0.46/lib/portage/util/_dyn_libs/soname_deps_qa.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_eventloop/asyncio_event_loop.py` & `portage-3.0.46/lib/portage/util/_eventloop/asyncio_event_loop.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_get_vm_info.py` & `portage-3.0.46/lib/portage/util/_get_vm_info.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_info_files.py` & `portage-3.0.46/lib/portage/util/_info_files.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_path.py` & `portage-3.0.46/lib/portage/util/_path.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_pty.py` & `portage-3.0.46/lib/portage/util/_pty.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_urlopen.py` & `portage-3.0.46/lib/portage/util/_urlopen.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/_xattr.py` & `portage-3.0.46/lib/portage/util/_xattr.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/backoff.py` & `portage-3.0.46/lib/portage/util/backoff.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/bin_entry_point.py` & `portage-3.0.46/lib/portage/util/bin_entry_point.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/changelog.py` & `portage-3.0.46/lib/portage/util/changelog.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/compression_probe.py` & `portage-3.0.46/lib/portage/util/compression_probe.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/configparser.py` & `portage-3.0.46/lib/portage/util/configparser.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/cpuinfo.py` & `portage-3.0.46/lib/portage/util/cpuinfo.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/digraph.py` & `portage-3.0.46/lib/portage/util/digraph.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/elf/constants.py` & `portage-3.0.46/lib/portage/util/elf/constants.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/elf/header.py` & `portage-3.0.46/lib/portage/util/elf/header.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/endian/decode.py` & `portage-3.0.46/lib/portage/util/endian/decode.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/env_update.py` & `portage-3.0.46/lib/portage/util/env_update.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/file_copy/__init__.py` & `portage-3.0.46/lib/portage/util/file_copy/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/formatter.py` & `portage-3.0.46/lib/portage/util/formatter.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/_asyncio/__init__.py` & `portage-3.0.46/lib/portage/util/futures/_asyncio/__init__.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/_asyncio/streams.py` & `portage-3.0.46/lib/portage/util/futures/_asyncio/streams.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/_sync_decorator.py` & `portage-3.0.46/lib/portage/util/futures/_sync_decorator.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/compat_coroutine.py` & `portage-3.0.46/lib/portage/util/futures/compat_coroutine.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/executor/fork.py` & `portage-3.0.46/lib/portage/util/futures/executor/fork.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/extendedfutures.py` & `portage-3.0.46/lib/portage/util/futures/extendedfutures.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/futures.py` & `portage-3.0.46/lib/portage/util/futures/futures.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/iter_completed.py` & `portage-3.0.46/lib/portage/util/futures/iter_completed.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/retry.py` & `portage-3.0.46/lib/portage/util/futures/retry.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/futures/unix_events.py` & `portage-3.0.46/lib/portage/util/futures/unix_events.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/hooks.py` & `portage-3.0.46/lib/portage/util/hooks.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/install_mask.py` & `portage-3.0.46/lib/portage/util/install_mask.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/iterators/MultiIterGroupBy.py` & `portage-3.0.46/lib/portage/util/iterators/MultiIterGroupBy.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/lafilefixer.py` & `portage-3.0.46/lib/portage/util/lafilefixer.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/listdir.py` & `portage-3.0.46/lib/portage/util/listdir.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/locale.py` & `portage-3.0.46/lib/portage/util/locale.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/movefile.py` & `portage-3.0.46/lib/portage/util/movefile.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/mtimedb.py` & `portage-3.0.46/lib/portage/util/mtimedb.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/netlink.py` & `portage-3.0.46/lib/portage/util/netlink.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/path.py` & `portage-3.0.46/lib/portage/util/path.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/shelve.py` & `portage-3.0.46/lib/portage/util/shelve.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/socks5.py` & `portage-3.0.46/lib/portage/util/socks5.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/whirlpool.py` & `portage-3.0.46/lib/portage/util/whirlpool.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/util/writeable_check.py` & `portage-3.0.46/lib/portage/util/writeable_check.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/versions.py` & `portage-3.0.46/lib/portage/versions.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/xml/metadata.py` & `portage-3.0.46/lib/portage/xml/metadata.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/lib/portage/xpak.py` & `portage-3.0.46/lib/portage/xpak.py`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/misc/emerge-delta-webrsync` & `portage-3.0.46/misc/emerge-delta-webrsync`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/setup.py` & `portage-3.0.46/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -813,15 +813,15 @@
         return list(venv_data_files(venv_files))
 
     return regular_files
 
 
 setup(
     name="portage",
-    version="3.0.45.3",
+    version="3.0.46",
     url="https://wiki.gentoo.org/wiki/Project:Portage",
     project_urls={
         "Release Notes": "https://gitweb.gentoo.org/proj/portage.git/plain/NEWS",
         "Documentation": "https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage",
     },
     author="Gentoo Portage Development Team",
     author_email="dev-portage@gentoo.org",
```

### Comparing `portage-3.0.45.3/src/portage_util__whirlpool.c` & `portage-3.0.46/src/portage_util__whirlpool.c`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/src/portage_util_file_copy_reflink_linux.c` & `portage-3.0.46/src/portage_util_file_copy_reflink_linux.c`

 * *Files identical despite different names*

### Comparing `portage-3.0.45.3/src/portage_util_libc.c` & `portage-3.0.46/src/portage_util_libc.c`

 * *Files identical despite different names*

