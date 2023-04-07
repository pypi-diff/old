# Comparing `tmp/ecs_composex-0.8.9.tar.gz` & `tmp/ecs_composex-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/ecs_composex-0.8.9.tar", last modified: Wed Nov 18 23:42:33 2020, max compression
+gzip compressed data, was "dist/ecs_composex-0.9.2.tar", last modified: Sat Dec  5 18:54:17 2020, max compression
```

## Comparing `ecs_composex-0.8.9.tar` & `ecs_composex-0.9.2.tar`

### file list

```diff
@@ -1,252 +1,273 @@
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/
--rw-rw-r--   0 john      (1000) john      (1000)      489 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/AUTHORS.rst
--rw-rw-r--   0 john      (1000) john      (1000)     3382 2020-07-20 07:32:44.000000 ecs_composex-0.8.9/CONTRIBUTING.rst
--rw-rw-r--   0 john      (1000) john      (1000)    10572 2020-11-10 22:49:40.000000 ecs_composex-0.8.9/HISTORY.rst
--rw-rw-r--   0 john      (1000) john      (1000)    35149 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/LICENSE
--rw-rw-r--   0 john      (1000) john      (1000)      343 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/MANIFEST.in
--rw-rw-r--   0 john      (1000) john      (1000)    17958 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/PKG-INFO
--rw-rw-r--   0 john      (1000) john      (1000)    14465 2020-11-14 00:13:46.000000 ecs_composex-0.8.9/README.rst
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/
--rw-rw-r--   0 john      (1000) john      (1000)     2640 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/docs/INGRESS_LOGIC.rst
--rw-rw-r--   0 john      (1000) john      (1000)      613 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/docs/Makefile
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/_build/
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/_build/html/
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/_build/html/_static/
--rw-rw-r--   0 john      (1000) john      (1000)      286 2020-09-30 07:05:06.000000 ecs_composex-0.8.9/docs/_build/html/_static/file.png
--rw-rw-r--   0 john      (1000) john      (1000)       90 2020-09-30 07:05:06.000000 ecs_composex-0.8.9/docs/_build/html/_static/minus.png
--rw-rw-r--   0 john      (1000) john      (1000)       90 2020-09-30 07:05:06.000000 ecs_composex-0.8.9/docs/_build/html/_static/plus.png
--rw-rw-r--   0 john      (1000) john      (1000)       28 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/docs/authors.rst
--rw-rw-r--   0 john      (1000) john      (1000)       28 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/docs/changelog.rst
--rwxrwxr-x   0 john      (1000) john      (1000)     5292 2020-11-08 18:27:57.000000 ecs_composex-0.8.9/docs/conf.py
--rw-rw-r--   0 john      (1000) john      (1000)       33 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/docs/contributing.rst
--rw-rw-r--   0 john      (1000) john      (1000)      678 2020-07-20 07:32:44.000000 ecs_composex-0.8.9/docs/credits.rst
--rw-rw-r--   0 john      (1000) john      (1000)      706 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.acm.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1588 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.appmesh.rst
--rw-rw-r--   0 john      (1000) john      (1000)     2733 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.common.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1399 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.compute.rst
--rw-rw-r--   0 john      (1000) john      (1000)      730 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.dns.rst
--rw-rw-r--   0 john      (1000) john      (1000)      940 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.docdb.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1618 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.dynamodb.rst
--rw-rw-r--   0 john      (1000) john      (1000)     2038 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.ecs.rst
--rw-rw-r--   0 john      (1000) john      (1000)      748 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.elbv2.rst
--rw-rw-r--   0 john      (1000) john      (1000)      173 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.iam.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1222 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.kms.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1657 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.rds.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1495 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1183 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.s3.rst
--rw-rw-r--   0 john      (1000) john      (1000)      796 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.secrets.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1225 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.sns.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1222 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.sqs.rst
--rw-rw-r--   0 john      (1000) john      (1000)      547 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.utils.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1751 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/ecs_composex.vpc.rst
--rw-rw-r--   0 john      (1000) john      (1000)    11226 2020-11-18 23:38:55.000000 ecs_composex-0.8.9/docs/extras.rst
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/features/
--rw-rw-r--   0 john      (1000) john      (1000)       54 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/appmesh.rst
--rw-rw-r--   0 john      (1000) john      (1000)       52 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/docs/features/docdb.rst
--rw-rw-r--   0 john      (1000) john      (1000)       55 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/dyndb.rst
--rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/ecs.rst
--rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/kms.rst
--rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/rds.rst
--rw-rw-r--   0 john      (1000) john      (1000)       49 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/s3.rst
--rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/sqs.rst
--rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/features/vpc.rst
--rw-rw-r--   0 john      (1000) john      (1000)      210 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/features.rst
--rw-rw-r--   0 john      (1000) john      (1000)      821 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/index.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1174 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/docs/installation.rst
--rw-rw-r--   0 john      (1000) john      (1000)      774 2020-05-25 20:48:28.000000 ecs_composex-0.8.9/docs/make.bat
--rw-rw-r--   0 john      (1000) john      (1000)       73 2020-11-18 15:06:34.000000 ecs_composex-0.8.9/docs/modules.rst
--rw-rw-r--   0 john      (1000) john      (1000)      865 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/modules_syntax.rst
--rw-rw-r--   0 john      (1000) john      (1000)    11515 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/readme.rst
--rw-rw-r--   0 john      (1000) john      (1000)     2861 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/requisites.rst
--rw-rw-r--   0 john      (1000) john      (1000)    10105 2020-07-20 07:32:44.000000 ecs_composex-0.8.9/docs/story.rst
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/syntax/
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/syntax/composex/
--rw-rw-r--   0 john      (1000) john      (1000)     3065 2020-11-15 17:22:06.000000 ecs_composex-0.8.9/docs/syntax/composex/acm.rst
--rw-rw-r--   0 john      (1000) john      (1000)     5178 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/appmesh.rst
--rw-rw-r--   0 john      (1000) john      (1000)     3498 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/common.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1607 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/compute.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1367 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/docs/syntax/composex/dns.rst
--rw-rw-r--   0 john      (1000) john      (1000)     3660 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/docs/syntax/composex/docdb.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1266 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/dynamodb.rst
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.details/
--rw-rw-r--   0 john      (1000) john      (1000)     3656 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.details/deploy.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1717 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.details/iam.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1014 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.details/logging.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1922 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.details/network.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1397 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.details/scaling.rst
--rw-rw-r--   0 john      (1000) john      (1000)      424 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.details/xray.rst
--rw-rw-r--   0 john      (1000) john      (1000)      690 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1430 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/ecs_cluster.rst
--rw-rw-r--   0 john      (1000) john      (1000)     6740 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/elbv2.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1568 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/kms.rst
--rw-rw-r--   0 john      (1000) john      (1000)     3921 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/rds.rst
--rw-rw-r--   0 john      (1000) john      (1000)     2992 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/s3.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1106 2020-11-18 15:50:33.000000 ecs_composex-0.8.9/docs/syntax/composex/sns.rst
--rw-rw-r--   0 john      (1000) john      (1000)     3766 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/sqs.rst
--rw-rw-r--   0 john      (1000) john      (1000)     2899 2020-11-10 07:47:27.000000 ecs_composex-0.8.9/docs/syntax/composex/vpc.rst
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/docs/syntax/docker-compose/
--rw-rw-r--   0 john      (1000) john      (1000)     3335 2020-11-16 15:11:47.000000 ecs_composex-0.8.9/docs/syntax/docker-compose/secrets.rst
--rw-rw-r--   0 john      (1000) john      (1000)     1194 2020-11-18 13:08:14.000000 ecs_composex-0.8.9/docs/syntax/docker-compose/services.rst
--rw-rw-r--   0 john      (1000) john      (1000)     3008 2020-07-20 07:32:44.000000 ecs_composex-0.8.9/docs/walkthrough.rst
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/
--rw-rw-r--   0 john      (1000) john      (1000)      927 2020-11-18 23:42:12.000000 ecs_composex-0.8.9/ecs_composex/__init__.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/acm/
--rw-rw-r--   0 john      (1000) john      (1000)      846 2020-07-13 22:22:29.000000 ecs_composex-0.8.9/ecs_composex/acm/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     3198 2020-11-15 17:22:06.000000 ecs_composex-0.8.9/ecs_composex/acm/acm_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     2169 2020-11-15 17:22:06.000000 ecs_composex-0.8.9/ecs_composex/acm/acm_params.py
--rw-rw-r--   0 john      (1000) john      (1000)     6869 2020-11-15 17:22:06.000000 ecs_composex-0.8.9/ecs_composex/acm/acm_stack.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/appmesh/
--rw-rw-r--   0 john      (1000) john      (1000)      994 2020-07-28 18:44:30.000000 ecs_composex-0.8.9/ecs_composex/appmesh/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     2943 2020-07-31 10:24:13.000000 ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     2621 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_conditions.py
--rw-rw-r--   0 john      (1000) john      (1000)     9868 2020-11-17 17:11:01.000000 ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_mesh.py
--rw-rw-r--   0 john      (1000) john      (1000)    12875 2020-11-17 17:11:01.000000 ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_node.py
--rw-rw-r--   0 john      (1000) john      (1000)     1812 2020-11-17 17:11:01.000000 ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_params.py
--rw-rw-r--   0 john      (1000) john      (1000)    10703 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_router.py
--rw-rw-r--   0 john      (1000) john      (1000)     5689 2020-11-17 17:11:01.000000 ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_service.py
--rw-rw-r--   0 john      (1000) john      (1000)     6405 2020-11-06 08:18:10.000000 ecs_composex-0.8.9/ecs_composex/cli.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/common/
--rw-rw-r--   0 john      (1000) john      (1000)     9764 2020-11-15 17:22:06.000000 ecs_composex-0.8.9/ecs_composex/common/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)    11253 2020-11-18 10:39:21.000000 ecs_composex-0.8.9/ecs_composex/common/aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     2981 2020-07-31 10:24:13.000000 ecs_composex-0.8.9/ecs_composex/common/cfn_conditions.py
--rw-rw-r--   0 john      (1000) john      (1000)     2850 2020-10-29 07:58:54.000000 ecs_composex-0.8.9/ecs_composex/common/cfn_params.py
--rw-rw-r--   0 john      (1000) john      (1000)    13646 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/common/compose_resources.py
--rw-rw-r--   0 john      (1000) john      (1000)    40860 2020-11-18 23:38:55.000000 ecs_composex-0.8.9/ecs_composex/common/compose_services.py
--rw-rw-r--   0 john      (1000) john      (1000)     4521 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/common/compose_volumes.py
--rw-rw-r--   0 john      (1000) john      (1000)     2488 2020-07-15 07:19:19.000000 ecs_composex-0.8.9/ecs_composex/common/config.py
--rw-rw-r--   0 john      (1000) john      (1000)      960 2020-07-13 22:22:29.000000 ecs_composex-0.8.9/ecs_composex/common/ecs_composex.py
--rw-rw-r--   0 john      (1000) john      (1000)     2131 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/common/envsubst.py
--rw-rw-r--   0 john      (1000) john      (1000)     8333 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/common/files.py
--rw-rw-r--   0 john      (1000) john      (1000)     5247 2020-07-31 10:24:13.000000 ecs_composex-0.8.9/ecs_composex/common/outputs.py
--rw-rw-r--   0 john      (1000) john      (1000)    25218 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/common/settings.py
--rw-rw-r--   0 john      (1000) john      (1000)    10811 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/common/stacks.py
--rw-rw-r--   0 john      (1000) john      (1000)     8988 2020-07-31 15:42:46.000000 ecs_composex-0.8.9/ecs_composex/common/tagging.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/compute/
--rw-rw-r--   0 john      (1000) john      (1000)      792 2020-07-13 22:22:29.000000 ecs_composex-0.8.9/ecs_composex/compute/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     1029 2020-05-25 20:48:29.000000 ecs_composex-0.8.9/ecs_composex/compute/compute_conditions.py
--rw-rw-r--   0 john      (1000) john      (1000)     2306 2020-05-25 20:48:29.000000 ecs_composex-0.8.9/ecs_composex/compute/compute_params.py
--rw-rw-r--   0 john      (1000) john      (1000)     2010 2020-07-13 22:22:29.000000 ecs_composex-0.8.9/ecs_composex/compute/compute_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     4034 2020-07-13 22:22:29.000000 ecs_composex-0.8.9/ecs_composex/compute/compute_template.py
--rw-rw-r--   0 john      (1000) john      (1000)    12107 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/compute/hosts_template.py
--rw-rw-r--   0 john      (1000) john      (1000)    10174 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/compute/spot_fleet.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/dns/
--rw-rw-r--   0 john      (1000) john      (1000)    12755 2020-11-08 18:27:57.000000 ecs_composex-0.8.9/ecs_composex/dns/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     1691 2020-10-29 07:58:54.000000 ecs_composex-0.8.9/ecs_composex/dns/dns_conditions.py
--rw-rw-r--   0 john      (1000) john      (1000)     3408 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/dns/dns_lookup.py
--rw-rw-r--   0 john      (1000) john      (1000)     1792 2020-11-08 18:27:57.000000 ecs_composex-0.8.9/ecs_composex/dns/dns_params.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/docdb/
--rw-rw-r--   0 john      (1000) john      (1000)      817 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/docdb/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     3563 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/docdb/docdb_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     1673 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/docdb/docdb_params.py
--rw-rw-r--   0 john      (1000) john      (1000)     2995 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/docdb/docdb_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     6978 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/docdb/docdb_template.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/
--rw-rw-r--   0 john      (1000) john      (1000)      995 2020-07-28 18:44:30.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     2798 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     2284 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     1219 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_params.py
--rw-rw-r--   0 john      (1000) john      (1000)      757 2020-10-16 07:49:39.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_perms.json
--rw-rw-r--   0 john      (1000) john      (1000)     1201 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_perms.py
--rw-rw-r--   0 john      (1000) john      (1000)     2578 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     8152 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_table.py
--rw-rw-r--   0 john      (1000) john      (1000)     2476 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_template.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/ecs/
--rw-rw-r--   0 john      (1000) john      (1000)     3025 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     4311 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/ecs/docker_tools.py
--rw-rw-r--   0 john      (1000) john      (1000)     7091 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_cluster.py
--rw-rw-r--   0 john      (1000) john      (1000)     2986 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_conditions.py
--rw-rw-r--   0 john      (1000) john      (1000)     5208 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_iam.py
--rw-rw-r--   0 john      (1000) john      (1000)     5524 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_params.py
--rw-rw-r--   0 john      (1000) john      (1000)    11751 2020-11-18 23:38:55.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_scaling.py
--rw-rw-r--   0 john      (1000) john      (1000)    14905 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_service.py
--rw-rw-r--   0 john      (1000) john      (1000)     2679 2020-11-18 23:38:55.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_service_config.py
--rw-rw-r--   0 john      (1000) john      (1000)     8526 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_service_network_config.py
--rw-rw-r--   0 john      (1000) john      (1000)    11448 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs/ecs_template.py
--rw-rw-r--   0 john      (1000) john      (1000)    13150 2020-11-18 13:25:28.000000 ecs_composex-0.8.9/ecs_composex/ecs_composex.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/elbv2/
--rw-rw-r--   0 john      (1000) john      (1000)      846 2020-10-29 07:58:54.000000 ecs_composex-0.8.9/ecs_composex/elbv2/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)    14754 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/elbv2/elbv2_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     1271 2020-11-08 18:27:57.000000 ecs_composex-0.8.9/ecs_composex/elbv2/elbv2_params.py
--rw-rw-r--   0 john      (1000) john      (1000)    33988 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/elbv2/elbv2_stack.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/iam/
--rw-rw-r--   0 john      (1000) john      (1000)     3428 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/iam/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)    11218 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/ingress_settings.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/kms/
--rw-rw-r--   0 john      (1000) john      (1000)      990 2020-07-29 17:22:31.000000 ecs_composex-0.8.9/ecs_composex/kms/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     3219 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/kms/kms_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     2470 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/kms/kms_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     1519 2020-11-16 15:11:47.000000 ecs_composex-0.8.9/ecs_composex/kms/kms_params.py
--rw-rw-r--   0 john      (1000) john      (1000)      701 2020-10-16 07:49:39.000000 ecs_composex-0.8.9/ecs_composex/kms/kms_perms.json
--rw-rw-r--   0 john      (1000) john      (1000)     1196 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/kms/kms_perms.py
--rw-rw-r--   0 john      (1000) john      (1000)     5197 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/kms/kms_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     2382 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/kms/kms_template.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/rds/
--rw-rw-r--   0 john      (1000) john      (1000)      849 2020-07-13 22:22:29.000000 ecs_composex-0.8.9/ecs_composex/rds/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     7052 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     2406 2020-05-25 20:48:29.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_conditions.py
--rw-rw-r--   0 john      (1000) john      (1000)    10957 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_db_template.py
--rw-rw-r--   0 john      (1000) john      (1000)     5536 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     3619 2020-07-13 22:22:29.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_parameter_groups_helper.py
--rw-rw-r--   0 john      (1000) john      (1000)     3064 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_params.py
--rw-rw-r--   0 john      (1000) john      (1000)     3575 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     3786 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/rds/rds_template.py
--rw-rw-r--   0 john      (1000) john      (1000)    10168 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/resource_settings.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/s3/
--rw-rw-r--   0 john      (1000) john      (1000)      989 2020-11-11 16:18:08.000000 ecs_composex-0.8.9/ecs_composex/s3/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     3098 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/s3/s3_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)    10807 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/s3/s3_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     1308 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/s3/s3_params.py
--rw-rw-r--   0 john      (1000) john      (1000)     1669 2020-11-11 16:18:08.000000 ecs_composex-0.8.9/ecs_composex/s3/s3_perms.json
--rw-rw-r--   0 john      (1000) john      (1000)     1103 2020-11-11 16:18:08.000000 ecs_composex-0.8.9/ecs_composex/s3/s3_perms.py
--rw-rw-r--   0 john      (1000) john      (1000)     3836 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/s3/s3_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     9298 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/s3/s3_template.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/secrets/
--rw-rw-r--   0 john      (1000) john      (1000)     3649 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/secrets/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)    10902 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/secrets/compose_secrets.py
--rw-rw-r--   0 john      (1000) john      (1000)     2547 2020-11-16 15:11:47.000000 ecs_composex-0.8.9/ecs_composex/secrets/secrets_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     1203 2020-11-16 15:11:47.000000 ecs_composex-0.8.9/ecs_composex/secrets/secrets_params.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/sns/
--rw-rw-r--   0 john      (1000) john      (1000)      990 2020-07-28 18:44:30.000000 ecs_composex-0.8.9/ecs_composex/sns/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     3332 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/sns/sns_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     2544 2020-11-12 09:49:16.000000 ecs_composex-0.8.9/ecs_composex/sns/sns_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     1216 2020-10-29 07:58:54.000000 ecs_composex-0.8.9/ecs_composex/sns/sns_params.py
--rw-rw-r--   0 john      (1000) john      (1000)      940 2020-07-28 18:44:30.000000 ecs_composex-0.8.9/ecs_composex/sns/sns_perms.py
--rw-rw-r--   0 john      (1000) john      (1000)     4683 2020-11-15 17:22:06.000000 ecs_composex-0.8.9/ecs_composex/sns/sns_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     7138 2020-11-15 17:22:06.000000 ecs_composex-0.8.9/ecs_composex/sns/sns_templates.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/sqs/
--rw-rw-r--   0 john      (1000) john      (1000)      965 2020-07-28 18:44:30.000000 ecs_composex-0.8.9/ecs_composex/sqs/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     3842 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/sqs/sqs_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)     5702 2020-11-18 16:31:44.000000 ecs_composex-0.8.9/ecs_composex/sqs/sqs_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     1429 2020-10-29 07:58:54.000000 ecs_composex-0.8.9/ecs_composex/sqs/sqs_params.py
--rw-rw-r--   0 john      (1000) john      (1000)      532 2020-10-16 07:49:39.000000 ecs_composex-0.8.9/ecs_composex/sqs/sqs_perms.json
--rw-rw-r--   0 john      (1000) john      (1000)     1194 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/sqs/sqs_perms.py
--rw-rw-r--   0 john      (1000) john      (1000)     3308 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/sqs/sqs_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     6476 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/sqs/sqs_template.py
--rw-rw-r--   0 john      (1000) john      (1000)     7816 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/tcp_resources_settings.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/utils/
--rw-rw-r--   0 john      (1000) john      (1000)      817 2020-07-31 14:06:09.000000 ecs_composex-0.8.9/ecs_composex/utils/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     1541 2020-10-14 06:30:56.000000 ecs_composex-0.8.9/ecs_composex/utils/init_ecs.py
--rw-rw-r--   0 john      (1000) john      (1000)     2054 2020-07-31 14:06:09.000000 ecs_composex-0.8.9/ecs_composex/utils/init_s3.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex/vpc/
--rw-rw-r--   0 john      (1000) john      (1000)      965 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/__init__.py
--rw-rw-r--   0 john      (1000) john      (1000)     1320 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/aws_mappings.py
--rw-rw-r--   0 john      (1000) john      (1000)     1634 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/cli.py
--rw-rw-r--   0 john      (1000) john      (1000)     3007 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/vpc_aws.py
--rw-rw-r--   0 john      (1000) john      (1000)      792 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/vpc_conditions.py
--rw-rw-r--   0 john      (1000) john      (1000)     3129 2020-11-13 23:55:38.000000 ecs_composex-0.8.9/ecs_composex/vpc/vpc_maths.py
--rw-rw-r--   0 john      (1000) john      (1000)     2681 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/vpc_params.py
--rw-rw-r--   0 john      (1000) john      (1000)     6749 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/vpc_stack.py
--rw-rw-r--   0 john      (1000) john      (1000)     9866 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/vpc_subnets.py
--rw-rw-r--   0 john      (1000) john      (1000)     7572 2020-11-11 16:18:55.000000 ecs_composex-0.8.9/ecs_composex/vpc/vpc_template.py
-drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/ecs_composex.egg-info/
--rw-rw-r--   0 john      (1000) john      (1000)    17958 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/ecs_composex.egg-info/PKG-INFO
--rw-rw-r--   0 john      (1000) john      (1000)     6675 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/ecs_composex.egg-info/SOURCES.txt
--rw-rw-r--   0 john      (1000) john      (1000)        1 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/ecs_composex.egg-info/dependency_links.txt
--rw-rw-r--   0 john      (1000) john      (1000)      126 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/ecs_composex.egg-info/entry_points.txt
--rw-rw-r--   0 john      (1000) john      (1000)        1 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/ecs_composex.egg-info/not-zip-safe
--rw-rw-r--   0 john      (1000) john      (1000)       33 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/ecs_composex.egg-info/requires.txt
--rw-rw-r--   0 john      (1000) john      (1000)       13 2020-11-18 23:42:32.000000 ecs_composex-0.8.9/ecs_composex.egg-info/top_level.txt
--rw-rw-r--   0 john      (1000) john      (1000)       33 2020-10-20 08:28:59.000000 ecs_composex-0.8.9/requirements.txt
--rw-rw-r--   0 john      (1000) john      (1000)      290 2020-10-14 06:30:57.000000 ecs_composex-0.8.9/requirements_dev.txt
--rw-rw-r--   0 john      (1000) john      (1000)      551 2020-11-18 23:42:33.000000 ecs_composex-0.8.9/setup.cfg
--rw-rw-r--   0 john      (1000) john      (1000)     3065 2020-11-18 23:42:12.000000 ecs_composex-0.8.9/setup.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/
+-rw-rw-r--   0 john      (1000) john      (1000)      493 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/AUTHORS.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     3382 2020-07-20 07:32:44.000000 ecs_composex-0.9.2/CONTRIBUTING.rst
+-rw-rw-r--   0 john      (1000) john      (1000)    12006 2020-11-26 10:22:41.000000 ecs_composex-0.9.2/HISTORY.rst
+-rw-rw-r--   0 john      (1000) john      (1000)    35149 2020-05-25 20:48:28.000000 ecs_composex-0.9.2/LICENSE
+-rw-rw-r--   0 john      (1000) john      (1000)      343 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/MANIFEST.in
+-rw-rw-r--   0 john      (1000) john      (1000)    17588 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/PKG-INFO
+-rw-rw-r--   0 john      (1000) john      (1000)    14135 2020-12-05 18:54:13.000000 ecs_composex-0.9.2/README.rst
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/
+-rw-rw-r--   0 john      (1000) john      (1000)     2640 2020-11-22 14:54:43.000000 ecs_composex-0.9.2/docs/INGRESS_LOGIC.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      613 2020-05-25 20:48:28.000000 ecs_composex-0.9.2/docs/Makefile
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/_build/
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/_build/html/
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/_build/html/_static/
+-rw-rw-r--   0 john      (1000) john      (1000)      286 2020-11-19 10:38:32.000000 ecs_composex-0.9.2/docs/_build/html/_static/file.png
+-rw-rw-r--   0 john      (1000) john      (1000)       90 2020-11-19 10:38:32.000000 ecs_composex-0.9.2/docs/_build/html/_static/minus.png
+-rw-rw-r--   0 john      (1000) john      (1000)       90 2020-11-19 10:38:32.000000 ecs_composex-0.9.2/docs/_build/html/_static/plus.png
+-rw-rw-r--   0 john      (1000) john      (1000)       28 2020-05-25 20:48:28.000000 ecs_composex-0.9.2/docs/authors.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       28 2020-05-25 20:48:28.000000 ecs_composex-0.9.2/docs/changelog.rst
+-rwxrwxr-x   0 john      (1000) john      (1000)     5214 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/conf.py
+-rw-rw-r--   0 john      (1000) john      (1000)       33 2020-05-25 20:48:28.000000 ecs_composex-0.9.2/docs/contributing.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      678 2020-07-20 07:32:44.000000 ecs_composex-0.9.2/docs/credits.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      706 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.acm.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1588 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.appmesh.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     2934 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.common.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1399 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.compute.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      730 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.dns.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      940 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.docdb.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1618 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.dynamodb.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     2038 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.ecs.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      748 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.elbv2.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      173 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.iam.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1222 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.kms.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1657 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.rds.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1495 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1183 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.s3.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      796 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.secrets.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1225 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.sns.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1222 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.sqs.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      547 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.utils.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1751 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/ecs_composex.vpc.rst
+-rw-rw-r--   0 john      (1000) john      (1000)    10943 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/extras.rst
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/features/
+-rw-rw-r--   0 john      (1000) john      (1000)       54 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/appmesh.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       52 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/docdb.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       55 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/dyndb.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/ecs.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/kms.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/rds.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       49 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/s3.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/sqs.rst
+-rw-rw-r--   0 john      (1000) john      (1000)       50 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features/vpc.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      210 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/features.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      822 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/index.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1174 2020-05-25 20:48:28.000000 ecs_composex-0.9.2/docs/installation.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      774 2020-05-25 20:48:28.000000 ecs_composex-0.9.2/docs/make.bat
+-rw-rw-r--   0 john      (1000) john      (1000)       73 2020-11-26 08:16:27.000000 ecs_composex-0.9.2/docs/modules.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      983 2020-11-26 09:39:32.000000 ecs_composex-0.9.2/docs/modules_syntax.rst
+-rw-rw-r--   0 john      (1000) john      (1000)    11121 2020-11-26 08:58:08.000000 ecs_composex-0.9.2/docs/readme.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     2861 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/requisites.rst
+-rw-rw-r--   0 john      (1000) john      (1000)    10105 2020-07-20 07:32:44.000000 ecs_composex-0.9.2/docs/story.rst
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/syntax/
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/syntax/composex/
+-rw-rw-r--   0 john      (1000) john      (1000)     3065 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/acm.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     5178 2020-11-28 15:02:29.000000 ecs_composex-0.9.2/docs/syntax/composex/appmesh.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     3498 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/common.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1607 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/compute.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1367 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/dns.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     3660 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/docdb.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1266 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/dynamodb.rst
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.details/
+-rw-rw-r--   0 john      (1000) john      (1000)     3683 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.details/deploy.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1717 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.details/iam.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1014 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.details/logging.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1921 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.details/network.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1397 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.details/scaling.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1230 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.details/xray.rst
+-rw-rw-r--   0 john      (1000) john      (1000)      690 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1427 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/syntax/composex/ecs_cluster.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     6740 2020-11-28 15:02:29.000000 ecs_composex-0.9.2/docs/syntax/composex/elbv2.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1778 2020-11-26 08:58:08.000000 ecs_composex-0.9.2/docs/syntax/composex/events.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1568 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/kms.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     3921 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/rds.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     2992 2020-11-28 15:02:29.000000 ecs_composex-0.9.2/docs/syntax/composex/s3.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1106 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/sns.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     3766 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/composex/sqs.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     4089 2020-12-03 22:49:55.000000 ecs_composex-0.9.2/docs/syntax/composex/vpc.rst
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/docs/syntax/docker-compose/
+-rw-rw-r--   0 john      (1000) john      (1000)     1491 2020-11-26 09:39:32.000000 ecs_composex-0.9.2/docs/syntax/docker-compose/networks.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     3335 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/docker-compose/secrets.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     1194 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/docs/syntax/docker-compose/services.rst
+-rw-rw-r--   0 john      (1000) john      (1000)     3960 2020-11-22 15:13:55.000000 ecs_composex-0.9.2/docs/walkthrough.rst
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/
+-rw-rw-r--   0 john      (1000) john      (1000)      927 2020-12-05 18:53:38.000000 ecs_composex-0.9.2/ecs_composex/__init__.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/acm/
+-rw-rw-r--   0 john      (1000) john      (1000)      846 2020-07-13 22:22:29.000000 ecs_composex-0.9.2/ecs_composex/acm/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3187 2020-11-27 12:45:30.000000 ecs_composex-0.9.2/ecs_composex/acm/acm_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2169 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/ecs_composex/acm/acm_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5857 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/acm/acm_stack.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/appmesh/
+-rw-rw-r--   0 john      (1000) john      (1000)      994 2020-07-28 18:44:30.000000 ecs_composex-0.9.2/ecs_composex/appmesh/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2943 2020-07-31 10:24:13.000000 ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2621 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_conditions.py
+-rw-rw-r--   0 john      (1000) john      (1000)     9416 2020-11-30 18:28:31.000000 ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_mesh.py
+-rw-rw-r--   0 john      (1000) john      (1000)    12815 2020-11-27 12:45:30.000000 ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_node.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1812 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)    10689 2020-11-27 12:45:30.000000 ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_router.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5689 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_service.py
+-rw-rw-r--   0 john      (1000) john      (1000)     6215 2020-12-05 18:24:29.000000 ecs_composex-0.9.2/ecs_composex/cli.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/common/
+-rw-rw-r--   0 john      (1000) john      (1000)    10313 2020-11-30 11:27:37.000000 ecs_composex-0.9.2/ecs_composex/common/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)    11253 2020-11-19 07:56:33.000000 ecs_composex-0.9.2/ecs_composex/common/aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2981 2020-07-31 10:24:13.000000 ecs_composex-0.9.2/ecs_composex/common/cfn_conditions.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2850 2020-10-29 07:58:54.000000 ecs_composex-0.9.2/ecs_composex/common/cfn_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2438 2020-11-27 12:45:30.000000 ecs_composex-0.9.2/ecs_composex/common/compose_networks.py
+-rw-rw-r--   0 john      (1000) john      (1000)    13947 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/common/compose_resources.py
+-rw-rw-r--   0 john      (1000) john      (1000)    43741 2020-12-05 18:28:07.000000 ecs_composex-0.9.2/ecs_composex/common/compose_services.py
+-rw-rw-r--   0 john      (1000) john      (1000)     4521 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/common/compose_volumes.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2488 2020-07-15 07:19:19.000000 ecs_composex-0.9.2/ecs_composex/common/config.py
+-rw-rw-r--   0 john      (1000) john      (1000)      960 2020-07-13 22:22:29.000000 ecs_composex-0.9.2/ecs_composex/common/ecs_composex.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2131 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/common/envsubst.py
+-rw-rw-r--   0 john      (1000) john      (1000)     8333 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/common/files.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5247 2020-07-31 10:24:13.000000 ecs_composex-0.9.2/ecs_composex/common/outputs.py
+-rw-rw-r--   0 john      (1000) john      (1000)    27287 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/common/settings.py
+-rw-rw-r--   0 john      (1000) john      (1000)    10811 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/common/stacks.py
+-rw-rw-r--   0 john      (1000) john      (1000)     8988 2020-07-31 15:42:46.000000 ecs_composex-0.9.2/ecs_composex/common/tagging.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/compute/
+-rw-rw-r--   0 john      (1000) john      (1000)      792 2020-07-13 22:22:29.000000 ecs_composex-0.9.2/ecs_composex/compute/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1029 2020-05-25 20:48:29.000000 ecs_composex-0.9.2/ecs_composex/compute/compute_conditions.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2306 2020-05-25 20:48:29.000000 ecs_composex-0.9.2/ecs_composex/compute/compute_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2010 2020-07-13 22:22:29.000000 ecs_composex-0.9.2/ecs_composex/compute/compute_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     4034 2020-07-13 22:22:29.000000 ecs_composex-0.9.2/ecs_composex/compute/compute_template.py
+-rw-rw-r--   0 john      (1000) john      (1000)    12107 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/compute/hosts_template.py
+-rw-rw-r--   0 john      (1000) john      (1000)    10174 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/compute/spot_fleet.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/dns/
+-rw-rw-r--   0 john      (1000) john      (1000)    12755 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/dns/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1691 2020-10-29 07:58:54.000000 ecs_composex-0.9.2/ecs_composex/dns/dns_conditions.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3408 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/dns/dns_lookup.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1945 2020-11-30 11:27:37.000000 ecs_composex-0.9.2/ecs_composex/dns/dns_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     8294 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/dns/dns_records.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/docdb/
+-rw-rw-r--   0 john      (1000) john      (1000)      817 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/docdb/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3563 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/docdb/docdb_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1673 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/docdb/docdb_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3020 2020-11-19 10:31:27.000000 ecs_composex-0.9.2/ecs_composex/docdb/docdb_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     6116 2020-11-30 18:28:31.000000 ecs_composex-0.9.2/ecs_composex/docdb/docdb_template.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/
+-rw-rw-r--   0 john      (1000) john      (1000)      995 2020-07-28 18:44:30.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2798 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2284 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1219 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)      757 2020-10-16 07:49:39.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_perms.json
+-rw-rw-r--   0 john      (1000) john      (1000)     1201 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_perms.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2578 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2250 2020-11-30 18:28:31.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_table.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2476 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_template.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/ecs/
+-rw-rw-r--   0 john      (1000) john      (1000)     1387 2020-12-04 07:38:30.000000 ecs_composex-0.9.2/ecs_composex/ecs/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     4604 2020-12-04 07:38:30.000000 ecs_composex-0.9.2/ecs_composex/ecs/docker_tools.py
+-rw-rw-r--   0 john      (1000) john      (1000)     6424 2020-12-05 17:28:40.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_cluster.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2986 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_conditions.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5174 2020-11-26 08:58:08.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_iam.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5548 2020-12-04 10:19:57.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)    11673 2020-12-01 11:12:15.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_scaling.py
+-rw-rw-r--   0 john      (1000) john      (1000)    15183 2020-12-01 09:27:52.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_service.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2679 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_service_config.py
+-rw-rw-r--   0 john      (1000) john      (1000)    13199 2020-12-04 08:45:20.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_service_network_config.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3070 2020-12-04 07:38:30.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)    11481 2020-12-04 07:38:30.000000 ecs_composex-0.9.2/ecs_composex/ecs/ecs_template.py
+-rw-rw-r--   0 john      (1000) john      (1000)    13032 2020-12-04 07:38:30.000000 ecs_composex-0.9.2/ecs_composex/ecs_composex.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/elbv2/
+-rw-rw-r--   0 john      (1000) john      (1000)      846 2020-10-29 07:58:54.000000 ecs_composex-0.9.2/ecs_composex/elbv2/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)    14754 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/elbv2/elbv2_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1492 2020-11-30 11:27:37.000000 ecs_composex-0.9.2/ecs_composex/elbv2/elbv2_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)    34559 2020-11-30 11:27:37.000000 ecs_composex-0.9.2/ecs_composex/elbv2/elbv2_stack.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/events/
+-rw-rw-r--   0 john      (1000) john      (1000)      817 2020-11-26 08:58:08.000000 ecs_composex-0.9.2/ecs_composex/events/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     8234 2020-12-01 11:12:15.000000 ecs_composex-0.9.2/ecs_composex/events/events_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)      908 2020-11-27 12:45:30.000000 ecs_composex-0.9.2/ecs_composex/events/events_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5022 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/events/events_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2049 2020-11-30 18:28:31.000000 ecs_composex-0.9.2/ecs_composex/events/events_template.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/iam/
+-rw-rw-r--   0 john      (1000) john      (1000)     3428 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/iam/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)    11678 2020-12-04 09:50:36.000000 ecs_composex-0.9.2/ecs_composex/ingress_settings.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/kinesis/
+-rw-rw-r--   0 john      (1000) john      (1000)      880 2020-11-27 18:43:26.000000 ecs_composex-0.9.2/ecs_composex/kinesis/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2907 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2758 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1241 2020-11-27 18:43:26.000000 ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)      431 2020-11-27 18:43:26.000000 ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_perms.json
+-rw-rw-r--   0 john      (1000) john      (1000)     1108 2020-11-27 18:43:26.000000 ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_perms.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2549 2020-11-27 18:43:26.000000 ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2507 2020-11-30 18:28:31.000000 ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_template.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/kms/
+-rw-rw-r--   0 john      (1000) john      (1000)      990 2020-07-29 17:22:31.000000 ecs_composex-0.9.2/ecs_composex/kms/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3219 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/kms/kms_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2470 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/kms/kms_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1519 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/kms/kms_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)      701 2020-10-16 07:49:39.000000 ecs_composex-0.9.2/ecs_composex/kms/kms_perms.json
+-rw-rw-r--   0 john      (1000) john      (1000)     1196 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/kms/kms_perms.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5287 2020-11-30 18:28:31.000000 ecs_composex-0.9.2/ecs_composex/kms/kms_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2382 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/kms/kms_template.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/rds/
+-rw-rw-r--   0 john      (1000) john      (1000)      849 2020-07-13 22:22:29.000000 ecs_composex-0.9.2/ecs_composex/rds/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     7052 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2406 2020-05-25 20:48:29.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_conditions.py
+-rw-rw-r--   0 john      (1000) john      (1000)    11167 2020-12-05 17:28:40.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_db_template.py
+-rw-rw-r--   0 john      (1000) john      (1000)     5536 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3619 2020-07-13 22:22:29.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_parameter_groups_helper.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3166 2020-12-05 17:28:40.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3412 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     4267 2020-12-04 16:32:44.000000 ecs_composex-0.9.2/ecs_composex/rds/rds_template.py
+-rw-rw-r--   0 john      (1000) john      (1000)    10232 2020-11-27 18:43:26.000000 ecs_composex-0.9.2/ecs_composex/resource_settings.py
+-rw-rw-r--   0 john      (1000) john      (1000)     4695 2020-11-30 18:28:31.000000 ecs_composex-0.9.2/ecs_composex/resources_import.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/s3/
+-rw-rw-r--   0 john      (1000) john      (1000)      989 2020-11-11 16:18:08.000000 ecs_composex-0.9.2/ecs_composex/s3/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3098 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/s3/s3_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)    10807 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/s3/s3_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1308 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/s3/s3_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1669 2020-11-11 16:18:08.000000 ecs_composex-0.9.2/ecs_composex/s3/s3_perms.json
+-rw-rw-r--   0 john      (1000) john      (1000)     1103 2020-11-11 16:18:08.000000 ecs_composex-0.9.2/ecs_composex/s3/s3_perms.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3836 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/s3/s3_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     8610 2020-12-05 18:46:29.000000 ecs_composex-0.9.2/ecs_composex/s3/s3_template.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/secrets/
+-rw-rw-r--   0 john      (1000) john      (1000)     3649 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/secrets/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)    11186 2020-12-04 09:50:36.000000 ecs_composex-0.9.2/ecs_composex/secrets/compose_secrets.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2681 2020-11-27 12:45:30.000000 ecs_composex-0.9.2/ecs_composex/secrets/secrets_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1203 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/secrets/secrets_params.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/sns/
+-rw-rw-r--   0 john      (1000) john      (1000)      990 2020-07-28 18:44:30.000000 ecs_composex-0.9.2/ecs_composex/sns/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3332 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/sns/sns_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2544 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/sns/sns_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1216 2020-10-29 07:58:54.000000 ecs_composex-0.9.2/ecs_composex/sns/sns_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)      940 2020-07-28 18:44:30.000000 ecs_composex-0.9.2/ecs_composex/sns/sns_perms.py
+-rw-rw-r--   0 john      (1000) john      (1000)     4683 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/sns/sns_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     7138 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/sns/sns_templates.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/sqs/
+-rw-rw-r--   0 john      (1000) john      (1000)      965 2020-07-28 18:44:30.000000 ecs_composex-0.9.2/ecs_composex/sqs/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3876 2020-12-01 11:12:15.000000 ecs_composex-0.9.2/ecs_composex/sqs/sqs_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)     6754 2020-12-01 11:12:15.000000 ecs_composex-0.9.2/ecs_composex/sqs/sqs_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1452 2020-12-01 11:12:15.000000 ecs_composex-0.9.2/ecs_composex/sqs/sqs_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)      532 2020-10-16 07:49:39.000000 ecs_composex-0.9.2/ecs_composex/sqs/sqs_perms.json
+-rw-rw-r--   0 john      (1000) john      (1000)     1194 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/sqs/sqs_perms.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3161 2020-11-27 18:43:26.000000 ecs_composex-0.9.2/ecs_composex/sqs/sqs_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     6476 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/sqs/sqs_template.py
+-rw-rw-r--   0 john      (1000) john      (1000)     7875 2020-12-05 17:28:40.000000 ecs_composex-0.9.2/ecs_composex/tcp_resources_settings.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/utils/
+-rw-rw-r--   0 john      (1000) john      (1000)      817 2020-07-31 14:06:09.000000 ecs_composex-0.9.2/ecs_composex/utils/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1541 2020-10-14 06:30:56.000000 ecs_composex-0.9.2/ecs_composex/utils/init_ecs.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2054 2020-07-31 14:06:09.000000 ecs_composex-0.9.2/ecs_composex/utils/init_s3.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex/vpc/
+-rw-rw-r--   0 john      (1000) john      (1000)      965 2020-11-11 16:18:55.000000 ecs_composex-0.9.2/ecs_composex/vpc/__init__.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1320 2020-11-11 16:18:55.000000 ecs_composex-0.9.2/ecs_composex/vpc/aws_mappings.py
+-rw-rw-r--   0 john      (1000) john      (1000)     1634 2020-11-11 16:18:55.000000 ecs_composex-0.9.2/ecs_composex/vpc/cli.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3507 2020-11-27 12:45:30.000000 ecs_composex-0.9.2/ecs_composex/vpc/vpc_aws.py
+-rw-rw-r--   0 john      (1000) john      (1000)      792 2020-11-11 16:18:55.000000 ecs_composex-0.9.2/ecs_composex/vpc/vpc_conditions.py
+-rw-rw-r--   0 john      (1000) john      (1000)     3129 2020-11-19 07:56:34.000000 ecs_composex-0.9.2/ecs_composex/vpc/vpc_maths.py
+-rw-rw-r--   0 john      (1000) john      (1000)     2681 2020-11-11 16:18:55.000000 ecs_composex-0.9.2/ecs_composex/vpc/vpc_params.py
+-rw-rw-r--   0 john      (1000) john      (1000)     9890 2020-12-03 22:50:27.000000 ecs_composex-0.9.2/ecs_composex/vpc/vpc_stack.py
+-rw-rw-r--   0 john      (1000) john      (1000)     9866 2020-11-11 16:18:55.000000 ecs_composex-0.9.2/ecs_composex/vpc/vpc_subnets.py
+-rw-rw-r--   0 john      (1000) john      (1000)     7970 2020-12-03 22:49:55.000000 ecs_composex-0.9.2/ecs_composex/vpc/vpc_template.py
+drwxrwxr-x   0 john      (1000) john      (1000)        0 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/
+-rw-rw-r--   0 john      (1000) john      (1000)    17588 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/PKG-INFO
+-rw-rw-r--   0 john      (1000) john      (1000)     7361 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/SOURCES.txt
+-rw-rw-r--   0 john      (1000) john      (1000)        1 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/dependency_links.txt
+-rw-rw-r--   0 john      (1000) john      (1000)      126 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/entry_points.txt
+-rw-rw-r--   0 john      (1000) john      (1000)        1 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/not-zip-safe
+-rw-rw-r--   0 john      (1000) john      (1000)       33 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/requires.txt
+-rw-rw-r--   0 john      (1000) john      (1000)       13 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/ecs_composex.egg-info/top_level.txt
+-rw-rw-r--   0 john      (1000) john      (1000)       33 2020-10-20 08:28:59.000000 ecs_composex-0.9.2/requirements.txt
+-rw-rw-r--   0 john      (1000) john      (1000)      290 2020-10-14 06:30:57.000000 ecs_composex-0.9.2/requirements_dev.txt
+-rw-rw-r--   0 john      (1000) john      (1000)      551 2020-12-05 18:54:17.000000 ecs_composex-0.9.2/setup.cfg
+-rw-rw-r--   0 john      (1000) john      (1000)     3065 2020-12-05 18:53:38.000000 ecs_composex-0.9.2/setup.py
```

### Comparing `ecs_composex-0.8.9/CONTRIBUTING.rst` & `ecs_composex-0.9.2/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/LICENSE` & `ecs_composex-0.9.2/LICENSE`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/PKG-INFO` & `ecs_composex-0.9.2/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: ecs_composex
-Version: 0.8.9
+Version: 0.9.2
 Summary: Implement for AWS ECS and Docker Compose what SAM is to Serverless for AWS Lambda
 Home-page: https://github.com/lambda-my-aws/ecs_composex
 Author: John Preston
 Author-email: john@lambda-my-aws.io
 License: GPLv3+
 Description: ============
         ECS ComposeX
         ============
         
         |PYPI_VERSION| |PYPI_LICENSE|
         
         |CODE_STYLE| |TDD| |BDD|
         
-        |CODECOV| |QUALITY|
+        |QUALITY|
         
         |BUILD|
         
         ----------------------------------------------------------------------------------------------------
         Be for AWS ECS and docker-compose what AWS SAM is to Lambda
         ----------------------------------------------------------------------------------------------------
         
@@ -259,46 +259,41 @@
         .. _Docker Compose: https://docs.docker.com/compose/
         .. _ECS ComposeX: https://docs.ecs-composex.lambda-my-aws.io
         .. _YAML Specifications: https://yaml.org/spec/
         .. _Extensions fields:  https://docs.docker.com/compose/compose-file/#extension-fields
         .. _ECS ComposeX Project: https://github.com/orgs/lambda-my-aws/projects/3
         .. _CICD Pipeline for multiple services on AWS ECS with ECS ComposeX: https://blog.ecs-composex.lambda-my-aws.io/posts/cicd-pipeline-for-multiple-services-on-aws-ecs-with-ecs-composex/
         
-        .. _AWS ECS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.html
-        .. _AWS VPC: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/vpc.html
-        .. _AWS RDS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/rds.html
-        .. _AWS SQS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/sqs.html
-        .. _AWS KMS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/kms.html
-        .. _AWS DynamoDB: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/dynamodb.html
-        .. _AWS ACM: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/acm.html
-        .. _AWS ELBv2: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/elbv2.html
-        .. _AWS S3: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/s3.html
-        .. _AWS IAM: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.details/iam.html
-        .. _AWS SNS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/sns.html
-        .. _AWS DocumentDB: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/docdb.html
+        .. _AWS ECS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.html
+        .. _AWS VPC: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/vpc.html
+        .. _AWS RDS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/rds.html
+        .. _AWS SQS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/sqs.html
+        .. _AWS KMS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/kms.html
+        .. _AWS DynamoDB: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/dynamodb.html
+        .. _AWS ACM: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/acm.html
+        .. _AWS ELBv2: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/elbv2.html
+        .. _AWS S3: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/s3.html
+        .. _AWS IAM: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.details/iam.html
+        .. _AWS SNS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/sns.html
+        .. _AWS DocumentDB: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/docdb.html
         
-        .. _AWS EC2: https://nightly.docs.ecs-composex.lambda-my-aws.io/features.html#ec2-resources-for-ecs-cluster
-        .. _AWS AppMesh: https://nightly.docs.ecs-composex.lambda-my-aws.io/readme/appmesh.html
+        .. _AWS EC2: https://docs.ecs-composex.lambda-my-aws.io/features.html#ec2-resources-for-ecs-cluster
+        .. _AWS AppMesh: https://docs.ecs-composex.lambda-my-aws.io/readme/appmesh.html
         
-        .. _Lookup: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/common.html#lookup
+        .. _Lookup: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/common.html#lookup
         
         .. |BUILD| image:: https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoidThwNXVIKzVvSnlXcUNVRzVlNE5wN0FiWE4rYzYvaHRNMEM0ZHMxeXRLMytSanhsckozVEN3L1Y5Szl5ZEdJVGxXVElyalZmaFVzR2tSbDBHeFI5cHBRPSIsIml2UGFyYW1ldGVyU3BlYyI6IlZkaml2d28wSGR1YU1xb2ciLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master
         
         .. |DOCS_BUILD| image:: https://readthedocs.org/projects/ecs-composex/badge/?version=latest
                 :target: https://ecs-composex.readthedocs.io/en/latest/?badge=latest
                 :alt: Documentation Status
         
         .. |PYPI_VERSION| image:: https://img.shields.io/pypi/v/ecs_composex.svg
                 :target: https://pypi.python.org/pypi/ecs_composex
         
-        
-        .. |CODECOV| image:: https://img.shields.io/codecov/c/github/lambda-my-aws/ecs_composex?color=black&style=flat-square
-            :alt: Codecov
-            :target: https://codecov.io/gh/lambda-my-aws/ecs_composex
-        
         .. |PYPI_DL| image:: https://img.shields.io/pypi/dm/ecs_composex
             :alt: PyPI - Downloads
             :target: https://pypi.python.org/pypi/ecs_composex
         
         .. |PYPI_LICENSE| image:: https://img.shields.io/github/license/lambda-my-aws/ecs_composex
             :alt: GitHub
             :target: https://github.com/lambda-my-aws/ecs_composex/blob/master/LICENSE
```

### Comparing `ecs_composex-0.8.9/README.rst` & `ecs_composex-0.9.2/README.rst`

 * *Files 6% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 ECS ComposeX
 ============
 
 |PYPI_VERSION| |PYPI_LICENSE|
 
 |CODE_STYLE| |TDD| |BDD|
 
-|CODECOV| |QUALITY|
+|QUALITY|
 
 |BUILD|
 
 ----------------------------------------------------------------------------------------------------
 Be for AWS ECS and docker-compose what AWS SAM is to Lambda
 ----------------------------------------------------------------------------------------------------
 
@@ -251,46 +251,41 @@
 .. _Docker Compose: https://docs.docker.com/compose/
 .. _ECS ComposeX: https://docs.ecs-composex.lambda-my-aws.io
 .. _YAML Specifications: https://yaml.org/spec/
 .. _Extensions fields:  https://docs.docker.com/compose/compose-file/#extension-fields
 .. _ECS ComposeX Project: https://github.com/orgs/lambda-my-aws/projects/3
 .. _CICD Pipeline for multiple services on AWS ECS with ECS ComposeX: https://blog.ecs-composex.lambda-my-aws.io/posts/cicd-pipeline-for-multiple-services-on-aws-ecs-with-ecs-composex/
 
-.. _AWS ECS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.html
-.. _AWS VPC: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/vpc.html
-.. _AWS RDS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/rds.html
-.. _AWS SQS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/sqs.html
-.. _AWS KMS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/kms.html
-.. _AWS DynamoDB: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/dynamodb.html
-.. _AWS ACM: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/acm.html
-.. _AWS ELBv2: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/elbv2.html
-.. _AWS S3: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/s3.html
-.. _AWS IAM: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.details/iam.html
-.. _AWS SNS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/sns.html
-.. _AWS DocumentDB: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/docdb.html
+.. _AWS ECS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.html
+.. _AWS VPC: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/vpc.html
+.. _AWS RDS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/rds.html
+.. _AWS SQS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/sqs.html
+.. _AWS KMS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/kms.html
+.. _AWS DynamoDB: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/dynamodb.html
+.. _AWS ACM: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/acm.html
+.. _AWS ELBv2: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/elbv2.html
+.. _AWS S3: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/s3.html
+.. _AWS IAM: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.details/iam.html
+.. _AWS SNS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/sns.html
+.. _AWS DocumentDB: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/docdb.html
 
-.. _AWS EC2: https://nightly.docs.ecs-composex.lambda-my-aws.io/features.html#ec2-resources-for-ecs-cluster
-.. _AWS AppMesh: https://nightly.docs.ecs-composex.lambda-my-aws.io/readme/appmesh.html
+.. _AWS EC2: https://docs.ecs-composex.lambda-my-aws.io/features.html#ec2-resources-for-ecs-cluster
+.. _AWS AppMesh: https://docs.ecs-composex.lambda-my-aws.io/readme/appmesh.html
 
-.. _Lookup: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/common.html#lookup
+.. _Lookup: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/common.html#lookup
 
 .. |BUILD| image:: https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoidThwNXVIKzVvSnlXcUNVRzVlNE5wN0FiWE4rYzYvaHRNMEM0ZHMxeXRLMytSanhsckozVEN3L1Y5Szl5ZEdJVGxXVElyalZmaFVzR2tSbDBHeFI5cHBRPSIsIml2UGFyYW1ldGVyU3BlYyI6IlZkaml2d28wSGR1YU1xb2ciLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master
 
 .. |DOCS_BUILD| image:: https://readthedocs.org/projects/ecs-composex/badge/?version=latest
         :target: https://ecs-composex.readthedocs.io/en/latest/?badge=latest
         :alt: Documentation Status
 
 .. |PYPI_VERSION| image:: https://img.shields.io/pypi/v/ecs_composex.svg
         :target: https://pypi.python.org/pypi/ecs_composex
 
-
-.. |CODECOV| image:: https://img.shields.io/codecov/c/github/lambda-my-aws/ecs_composex?color=black&style=flat-square
-    :alt: Codecov
-    :target: https://codecov.io/gh/lambda-my-aws/ecs_composex
-
 .. |PYPI_DL| image:: https://img.shields.io/pypi/dm/ecs_composex
     :alt: PyPI - Downloads
     :target: https://pypi.python.org/pypi/ecs_composex
 
 .. |PYPI_LICENSE| image:: https://img.shields.io/github/license/lambda-my-aws/ecs_composex
     :alt: GitHub
     :target: https://github.com/lambda-my-aws/ecs_composex/blob/master/LICENSE
```

### Comparing `ecs_composex-0.8.9/docs/INGRESS_LOGIC.rst` & `ecs_composex-0.9.2/docs/INGRESS_LOGIC.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/Makefile` & `ecs_composex-0.9.2/docs/Makefile`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/conf.py` & `ecs_composex-0.9.2/docs/conf.py`

 * *Files 2% similar despite different names*

```diff
@@ -92,22 +92,21 @@
 extensions += [
     "sphinx.ext.todo",
     "sphinx.ext.viewcode",
     "sphinx.ext.autodoc",
     "sphinx_rtd_theme",
 ]
 
-# html_theme = "karma_sphinx_theme"
 html_theme = "sphinx_rtd_theme"
+
 # Theme options are theme-specific and customize the look and feel of a
 # theme further.  For a list of options available for each theme, see the
 # documentation.
 #
 html_theme_options = {
-    "vcs_pageview_mode": "display_github",
     "collapse_navigation": False,
 }
 
 # Add any paths that contain custom static files (such as style sheets) here,
 # relative to this directory. They are copied after the builtin static files,
 # so a file named "default.css" will overwrite the builtin "default.css".
 html_static_path = ["_static"]
```

### Comparing `ecs_composex-0.8.9/docs/credits.rst` & `ecs_composex-0.9.2/docs/credits.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.acm.rst` & `ecs_composex-0.9.2/docs/ecs_composex.acm.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.appmesh.rst` & `ecs_composex-0.9.2/docs/ecs_composex.appmesh.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.common.rst` & `ecs_composex-0.9.2/docs/ecs_composex.common.rst`

 * *Files 2% similar despite different names*

```diff
@@ -24,14 +24,22 @@
 ---------------------------------------
 
 .. automodule:: ecs_composex.common.cfn_params
    :members:
    :undoc-members:
    :show-inheritance:
 
+ecs\_composex.common.compose\_networks module
+---------------------------------------------
+
+.. automodule:: ecs_composex.common.compose_networks
+   :members:
+   :undoc-members:
+   :show-inheritance:
+
 ecs\_composex.common.compose\_resources module
 ----------------------------------------------
 
 .. automodule:: ecs_composex.common.compose_resources
    :members:
    :undoc-members:
    :show-inheritance:
```

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.compute.rst` & `ecs_composex-0.9.2/docs/ecs_composex.compute.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.dns.rst` & `ecs_composex-0.9.2/docs/ecs_composex.dns.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.docdb.rst` & `ecs_composex-0.9.2/docs/ecs_composex.docdb.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.dynamodb.rst` & `ecs_composex-0.9.2/docs/ecs_composex.dynamodb.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.ecs.rst` & `ecs_composex-0.9.2/docs/ecs_composex.ecs.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.elbv2.rst` & `ecs_composex-0.9.2/docs/ecs_composex.elbv2.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.kms.rst` & `ecs_composex-0.9.2/docs/ecs_composex.kms.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.rds.rst` & `ecs_composex-0.9.2/docs/ecs_composex.rds.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.rst` & `ecs_composex-0.9.2/docs/ecs_composex.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.s3.rst` & `ecs_composex-0.9.2/docs/ecs_composex.s3.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.secrets.rst` & `ecs_composex-0.9.2/docs/ecs_composex.secrets.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.sns.rst` & `ecs_composex-0.9.2/docs/ecs_composex.sns.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.sqs.rst` & `ecs_composex-0.9.2/docs/ecs_composex.sqs.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.utils.rst` & `ecs_composex-0.9.2/docs/ecs_composex.utils.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/ecs_composex.vpc.rst` & `ecs_composex-0.9.2/docs/ecs_composex.vpc.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/extras.rst` & `ecs_composex-0.9.2/docs/extras.rst`

 * *Files 2% similar despite different names*

```diff
@@ -227,21 +227,14 @@
 
 The deploy labels are ignored on a container level, therefore, none of these tags will show when you deploy the services.
 
 .. hint::
 
     The labels can be either a list of strings, or a "document" (dictionary).
 
-Here is an example where we use the label, both as a string (**requires the `=` to be present to define key/value) and
-a dictionary. The family for this case is **app01**
-
-.. literalinclude:: ../use-cases/blog-all-features.yml
-    :language: yaml
-    :emphasize-lines: 25-26, 45-46
-
 But then you might wonder, how come are the permissions going to work for the services?
 
 Remember, the permissions are set at the **Task definition** level. So any container within that service, will get the
 same permissions.
 
 **However**, for the database as an example, which creates a Secret in AWS Secrets Manager, which we would then expose
 to the service with the *Secrets* attribute of the **Container Definition**, ECS ComposeX will specifically add that
```

### Comparing `ecs_composex-0.8.9/docs/index.rst` & `ecs_composex-0.9.2/docs/index.rst`

 * *Files 3% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 
 .. toctree::
     :maxdepth: 1
     :caption: ECS ComposeX
     :titlesonly:
 
     readme
-    getstarted
+    walkthrough
     story
 
 .. toctree::
     :maxdepth: 1
     :caption: Installation
 
     requisites
```

### Comparing `ecs_composex-0.8.9/docs/installation.rst` & `ecs_composex-0.9.2/docs/installation.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/make.bat` & `ecs_composex-0.9.2/docs/make.bat`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/modules_syntax.rst` & `ecs_composex-0.9.2/docs/modules_syntax.rst`

 * *Files 13% similar despite different names*

```diff
@@ -3,14 +3,15 @@
 .. toctree::
     :caption: docker-compose syntax
     :maxdepth: 1
 
     syntax/docker-compose/services
     syntax/docker-compose/volumes
     syntax/docker-compose/secrets
+    syntax/docker-compose/networks
 
 .. toctree::
     :caption: Services Extension Fields
     :maxdepth: 1
 
     syntax/composex/ecs
     syntax/composex/ecs.details/scaling
@@ -31,8 +32,11 @@
     syntax/composex/docdb
     syntax/composex/s3
     syntax/composex/sqs
     syntax/composex/sns
     syntax/composex/acm
     syntax/composex/kms
     syntax/composex/vpc
+    syntax/composex/events
+    syntax/composex/ecs_cluster
+    syntax/composex/dns
     syntax/composex/compute
```

### Comparing `ecs_composex-0.8.9/docs/readme.rst` & `ecs_composex-0.9.2/docs/readme.rst`

 * *Files 5% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 ECS ComposeX
 ============
 
 |PYPI_VERSION| |PYPI_LICENSE|
 
 |CODE_STYLE| |TDD| |BDD|
 
-|CODECOV| |QUALITY|
+|QUALITY|
 
 |BUILD|
 
 ----------------------------------------------------------------------------------------------------
 Build your infrastructure and deploy your services to AWS services using docker-compose file format.
 ----------------------------------------------------------------------------------------------------
 
@@ -161,22 +161,21 @@
 However the original deployments and work on this project was done using EC2 instances (using SpotFleet), everything
 is now implemented to work on AWS Fargate First (2020-06-06).
 
 .. note::
 
     | :ref:`vpc_network_design`
     | :ref:`vpc_syntax_reference`
-    | :ref:`ec2_compute_design`
     | :ref:`syntax_reference`
 
 .. note::
 
-    If you do not need extra AWS resources such as SQS queues to be created as part of these microservices deployments, I would recommend to use `AWS ECS CLI`_ which does already a lot of the work for the services.
-    Alternatively, use the AWS CLI v2. It is absolutely smashing-ly awesome and might be just what you need
-    This tool aims to reproduce the original ECS CLI behaviour whilst adding logic for non ECS resources that you want to create in your environment.
+    If you do not need extra AWS resources such as SQS queues to be created as part of these microservices deployments,
+    I would recommend to use `AWS ECS CLI`_ which does already a lot of the work for the services.
+    Alternatively, use Copilot (the AWS CLI v2). It is very developer friendly to start new projects.
 
 License
 =======
 
 * Free software: GPLv3+
 
 The Blog
@@ -214,19 +213,14 @@
 .. |DOCS_BUILD| image:: https://readthedocs.org/projects/ecs-composex/badge/?version=latest
         :target: https://ecs-composex.readthedocs.io/en/latest/?badge=latest
         :alt: Documentation Status
 
 .. |PYPI_VERSION| image:: https://img.shields.io/pypi/v/ecs_composex.svg
         :target: https://pypi.python.org/pypi/ecs_composex
 
-
-.. |CODECOV| image:: https://img.shields.io/codecov/c/github/lambda-my-aws/ecs_composex?color=black&style=flat-square
-    :alt: Codecov
-    :target: https://codecov.io/gh/lambda-my-aws/ecs_composex
-
 .. |PYPI_DL| image:: https://img.shields.io/pypi/dm/ecs_composex
     :alt: PyPI - Downloads
     :target: https://pypi.python.org/pypi/ecs_composex
 
 .. |PYPI_LICENSE| image:: https://img.shields.io/github/license/lambda-my-aws/ecs_composex
     :alt: GitHub
     :target: https://github.com/lambda-my-aws/ecs_composex/blob/master/LICENSE
```

### Comparing `ecs_composex-0.8.9/docs/requisites.rst` & `ecs_composex-0.9.2/docs/requisites.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/story.rst` & `ecs_composex-0.9.2/docs/story.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/acm.rst` & `ecs_composex-0.9.2/docs/syntax/composex/acm.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/appmesh.rst` & `ecs_composex-0.9.2/docs/syntax/composex/appmesh.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/common.rst` & `ecs_composex-0.9.2/docs/syntax/composex/common.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/compute.rst` & `ecs_composex-0.9.2/docs/syntax/composex/compute.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/dns.rst` & `ecs_composex-0.9.2/docs/syntax/composex/dns.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/docdb.rst` & `ecs_composex-0.9.2/docs/syntax/composex/docdb.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/dynamodb.rst` & `ecs_composex-0.9.2/docs/syntax/composex/dynamodb.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/ecs.details/deploy.rst` & `ecs_composex-0.9.2/docs/syntax/composex/ecs.details/deploy.rst`

 * *Files 5% similar despite different names*

```diff
@@ -63,17 +63,17 @@
 your web application:
 
 ecs.task.family
 ++++++++++++++++
 
 For example, you would have:
 
-.. literalinclude:: ../use-cases/blog.yml
+.. literalinclude:: ../../../../use-cases/blog.features.yml
     :language: yaml
-    :emphasize-lines: 25-26, 45-46
+    :emphasize-lines: 25-26, 68-70, 147-149
 
 .. warning::
 
     The example above illustrates that you can either use, for deploy labels
 
     * a list of strings
```

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/ecs.details/iam.rst` & `ecs_composex-0.9.2/docs/syntax/composex/ecs.details/iam.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/ecs.details/logging.rst` & `ecs_composex-0.9.2/docs/syntax/composex/ecs.details/logging.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/ecs.details/network.rst` & `ecs_composex-0.9.2/docs/syntax/composex/ecs.details/network.rst`

 * *Files 0% similar despite different names*

```diff
@@ -64,14 +64,14 @@
 .. hint::
 
     The protocol is automatically detected based on the port definition.
     By default, it is TCP
 
 .. hint::
 
-    To see details about the Ingress for Load Balancers, refer to :ref:`_load_balancers_ingress_syntax_ref`
+    To see details about the Ingress for Load Balancers, refer to :ref:`load_balancers_ingress_syntax_ref`
 
 
 .. hint::
 
     When using an ALB, you do not need to define that ALB security group etc., all inbound rules will be defined automatically
     to allow the ALB to communicate with your service!
```

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/ecs.details/scaling.rst` & `ecs_composex-0.9.2/docs/syntax/composex/ecs.details/scaling.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/ecs.rst` & `ecs_composex-0.9.2/docs/syntax/composex/ecs.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/ecs_cluster.rst` & `ecs_composex-0.9.2/docs/syntax/composex/ecs_cluster.rst`

 * *Files 23% similar despite different names*

```diff
@@ -5,16 +5,15 @@
 ==========
 
 This section allows you to define how you would like the ECS Cluster to be configured.
 It also allows you to define `Lookup` to use an existing ECS Cluster.
 
 
 Properties
-----------
-
+==========
 Refer to the `AWS CFN reference for ECS Cluster`_
 
 .. code-block:: yaml
     :caption: Override default settings
 
     x-cluster:
       Properties:
@@ -26,16 +25,15 @@
           - CapacityProvider: FARGATE_SPOT
             Weight: 4
             Base: 2
           - CapacityProvider: FARGATE
             Weight: 1
 
 Lookup
-------
-
+======
 Allows you to enter the name of an existing ECS Cluster that you want to deploy your services to.
 
 .. code-block:: yaml
     :caption: Lookup existing cluster example.
 
     x-cluster:
       Lookup:
@@ -45,14 +43,14 @@
 
 
 .. warning::
 
     If the cluster name is not found, by default, a new cluster will be created with the default settings.
 
 Use
-----
+===
 
 This key allows you to set a cluster to use, that you do not wish to lookup, you just know the name you want to use.
 (Useful for multi-account where you can't lookup cross-account).
 
 
 .. _AWS CFN reference for ECS Cluster: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html
```

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/elbv2.rst` & `ecs_composex-0.9.2/docs/syntax/composex/elbv2.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/kms.rst` & `ecs_composex-0.9.2/docs/syntax/composex/kms.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/rds.rst` & `ecs_composex-0.9.2/docs/syntax/composex/rds.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/s3.rst` & `ecs_composex-0.9.2/docs/syntax/composex/s3.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/sns.rst` & `ecs_composex-0.9.2/docs/syntax/composex/sns.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/composex/sqs.rst` & `ecs_composex-0.9.2/docs/syntax/composex/sqs.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/docker-compose/secrets.rst` & `ecs_composex-0.9.2/docs/syntax/docker-compose/secrets.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/syntax/docker-compose/services.rst` & `ecs_composex-0.9.2/docs/syntax/docker-compose/services.rst`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/docs/walkthrough.rst` & `ecs_composex-0.9.2/docs/walkthrough.rst`

 * *Files 18% similar despite different names*

```diff
@@ -83,40 +83,69 @@
 
 .. code-block::
 
     services:
       serviceA:
         image: link_to_image_a
         ports:
-          - 8080:80
-          - 8443:443
+          - 8080
+          - 80
         environment:
-          description: reverse-proxy
+          description: front-app
         links:
           - serviceB
 
       serviceB:
         image: link_to_image_b
         ports:
-          - 8081:80
-          - 8444:443
+          - 80
+          - 8080
         environment:
-          description: BackendApp
+          description: auth-app
     x-rds:
       db:
         Properties:
           Engine: aurora-mysql
           EngineVersion: 5.7.12
         Settings: {}
         Services:
           - name: serviceB
             access: RW
 
-    x-configs:
-      serviceA:
-        network:
-          lb_type: application
-          is_public: True
-          ext_sources:
-            - ipv4: 0.0.0.0/0
-              protocol: tcp
-              source_name: all
+    x-elbv2:
+      public-lb:
+        Properties:
+          Scheme: public-facing
+          Type: application
+        Settings:
+         http2: True
+         cross_zone: True
+        MacroParameters:
+          Ingress:
+            ExtSources:
+              - Ipv4: "0.0.0.0/0"
+                Description: ANY
+              - Ipv4: "1.1.1.1/32"
+                Description: CLOUDFLARE
+                Name: CLOUDFLARE
+        Listeners:
+          - Port: 80
+            Protocol: HTTP
+            DefaultActions:
+              - Redirect: HTTP_TO_HTTPS
+          - Port: 443
+            Protocol: HTTP
+            Certificates:
+              - x-acm: public-acm-01
+              - CertificateArn: arn:aws:acm:eu-west-1:012345678912:certificate/102402a1-d0d2-46ff-b26b-33008f072ee8
+            Targets:
+              - name: serviceA:serviceA
+                access: /
+              - name: serviceB:serviceB
+                access: /login
+        Services:
+          - name: serviceA:serviceA
+            port: 80
+            healthcheck: 8080:HTTP:5:2:15:3:/ping.This.Method:200,201
+          - name: serviceB:serviceB
+            port: 80
+            healthcheck: 8080:HTTP:5:2:15:3:/health
```

### Comparing `ecs_composex-0.8.9/ecs_composex/__init__.py` & `ecs_composex-0.9.2/ecs_composex/rds/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -11,13 +11,10 @@
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
-
-"""Top-level package for ECS ComposeX."""
-
-__author__ = """John Preston"""
-__email__ = "john@lambda-my-aws.io"
-__version__ = "0.8.9"
+"""
+Module to handle AWS RDS CFN Templates creation
+"""
```

### Comparing `ecs_composex-0.8.9/ecs_composex/acm/__init__.py` & `ecs_composex-0.9.2/ecs_composex/acm/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/acm/acm_aws.py` & `ecs_composex-0.9.2/ecs_composex/acm/acm_aws.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,16 +15,14 @@
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 Module to import existing ACM Certificates just as for other resources.
 """
 
-import re
-
 from botocore.exceptions import ClientError
 
 from ecs_composex.common import LOG, keyisset
 from ecs_composex.common.aws import (
     find_aws_resource_arn_from_tags_api,
     define_lookup_role_from_info,
 )
```

### Comparing `ecs_composex-0.8.9/ecs_composex/acm/acm_params.py` & `ecs_composex-0.9.2/ecs_composex/acm/acm_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/acm/acm_stack.py` & `ecs_composex-0.9.2/ecs_composex/acm/acm_stack.py`

 * *Files 14% similar despite different names*

```diff
@@ -18,29 +18,29 @@
 """
 Main module for ACM
 """
 
 from copy import deepcopy
 from warnings import warn
 
-from troposphere import Ref, AWS_NO_VALUE, Tags
+from troposphere import Ref, Tags
 from troposphere.certificatemanager import (
     Certificate as AcmCert,
     DomainValidationOption,
 )
 
-from ecs_composex.common import no_value_if_not_set
-from ecs_composex.acm.acm_params import RES_KEY, MOD_KEY
 from ecs_composex.acm.acm_aws import lookup_cert_config
+from ecs_composex.acm.acm_params import RES_KEY, MOD_KEY
 from ecs_composex.common import (
     NONALPHANUM,
     keyisset,
 )
 from ecs_composex.common.compose_resources import set_resources
 from ecs_composex.dns.dns_params import PUBLIC_DNS_ZONE_ID
+from ecs_composex.resources_import import import_record_properties
 
 
 class Certificate(object):
     """
     Class specifically for ACM Certificate
     """
 
@@ -73,41 +73,14 @@
             {}
             if not keyisset("MacroParameters", self.definition)
             else self.definition["MacroParameters"]
         )
 
         self.cfn_resource = None
 
-    def import_properties(self):
-        """
-        Method to define the properties from the Properties section
-        """
-        validations = []
-        if keyisset("DomainValidationOptions", self.properties):
-            validations = [
-                DomainValidationOption(
-                    DomainName=opt["DomainName"], HostedZoneId=opt["HostedZoneId"]
-                )
-                for opt in self.properties["DomainValidationOptions"]
-            ]
-        props = {
-            "DomainName": no_value_if_not_set(self.properties, "DomainName"),
-            "SubjectAlternativeNames": no_value_if_not_set(
-                self.properties, "SubjectAlternativeNames"
-            ),
-            "ValidationMethod": self.properties["ValidationMethod"],
-            "DomainValidationOptions": Ref(AWS_NO_VALUE)
-            if not validations
-            else validations,
-            "Tags": Tags(
-                Name=self.properties["DomainName"],
-            ),
-        }
-        return props
-
     def define_parameters_props(self):
         if not keyisset("DomainNames", self.parameters):
             raise KeyError(
                 "For MacroParameters, you need to define at least DomainNames"
             )
         validations = [
             DomainValidationOption(
@@ -130,16 +103,15 @@
         return props
 
     def create_acm_cert(self):
         """
         Method to set the ACM Certificate definition
         """
         if self.properties:
-            props = self.import_properties()
-
+            props = import_record_properties(self.properties, AcmCert)
         elif self.parameters:
             props = self.define_parameters_props()
         else:
             raise ValueError(
                 "Failed to determine how to create the ACM certificate",
                 self.logical_name,
             )
@@ -194,8 +166,7 @@
             "Validation via DNS can only work if the zone is functional and you cannot associate a pending cert."
             "CFN Will fail if the ACM cert validation is not complete."
         )
     if lookup_resources:
         mappings = create_acm_mappings(lookup_resources, settings)
         if mappings:
             root_stack.stack_template.add_mapping(MOD_KEY, mappings)
-            print(mappings)
```

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/__init__.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_aws.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_aws.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_conditions.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_conditions.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_mesh.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_mesh.py`

 * *Files 6% similar despite different names*

```diff
@@ -20,22 +20,24 @@
 
 Once all services have been deployed and their VirtualNodes are setup, we deploy the Mesh for it.
 """
 
 from troposphere import Ref, GetAtt, AWS_ACCOUNT_ID, AWS_STACK_NAME
 from troposphere import appmesh
 
+from ecs_composex.resources_import import import_record_properties
 from ecs_composex.common import (
     keyisset,
     add_parameters,
     LOG,
 )
 from ecs_composex.common.cfn_params import ROOT_STACK_NAME
 from ecs_composex.common.stacks import ComposeXStack
 from ecs_composex.ecs import ecs_params
+
 from ecs_composex.appmesh import appmesh_params, appmesh_conditions
 from ecs_composex.appmesh import metadata
 from ecs_composex.appmesh.appmesh_aws import lookup_mesh_by_name
 from ecs_composex.appmesh.appmesh_conditions import add_appmesh_conditions
 from ecs_composex.appmesh.appmesh_node import MeshNode
 from ecs_composex.appmesh.appmesh_params import MESH_NAME, MESH_OWNER_ID
 from ecs_composex.appmesh.appmesh_router import MeshRouter
@@ -90,39 +92,27 @@
             services_root_stack.Parameters.update(
                 {
                     appmesh_params.MESH_NAME_T: mesh_info[MESH_NAME.title],
                     appmesh_params.MESH_OWNER_ID_T: mesh_info[MESH_OWNER_ID.title],
                 }
             )
         else:
-            self.mesh_name = MESH_NAME.Default
-            allowed_values = ["ALLOW_ALL", "DROP_ALL"]
-            egress_type = "DROP_ALL"
-            if (
-                keyisset("EgressFilter", self.mesh_properties)
-                and self.mesh_properties["EgressFilter"] in allowed_values
-            ):
-                egress_type = self.mesh_properties["EgressFilter"]
-            elif (
-                keyisset("EgressFilter", self.mesh_properties)
-                and self.mesh_properties["EgressFilter"] not in allowed_values
-            ):
-                LOG.warning(
-                    f"Invalid EgressFilter value {self.mesh_properties['EgressFilter']}."
-                    f" Allowed values: {allowed_values} "
-                    "Setting to default: DROP_ALL"
-                )
+            if self.mesh_properties:
+                props = import_record_properties(self.mesh_properties, appmesh.Mesh)
+                props["Metadata"] = metadata
+                props["MeshName"] = appmesh_conditions.set_mesh_name()
+            else:
+                props = {
+                    "Spec": appmesh.MeshSpec(
+                        EgressFilter=appmesh.EgressFilter(Type="DENY_ALL")
+                    ),
+                    "MeshName": appmesh_conditions.set_mesh_name(),
+                }
             self.appmesh = appmesh.Mesh(
-                self.mesh_title,
-                template=services_root_stack.stack_template,
-                MeshName=appmesh_conditions.set_mesh_name(),
-                Spec=appmesh.MeshSpec(
-                    EgressFilter=appmesh.EgressFilter(Type=egress_type)
-                ),
-                Metadata=metadata,
+                self.mesh_title, template=services_root_stack.stack_template, **props
             )
             services_root_stack.Parameters.update(
                 {
                     appmesh_params.MESH_NAME_T: Ref(AWS_STACK_NAME),
                     appmesh_params.MESH_OWNER_ID_T: Ref(AWS_ACCOUNT_ID),
                 }
             )
```

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_node.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_node.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,28 +26,24 @@
     ContainerDefinition,
     Ulimit,
     ProxyConfiguration,
     HealthCheck,
 )
 from troposphere.iam import Policy
 
-from ecs_composex.common import LOG, add_parameters
-from ecs_composex.common.outputs import ComposeXOutput
-from ecs_composex.dns.dns_params import PRIVATE_DNS_ZONE_NAME
-from ecs_composex.ecs import ecs_params
-from ecs_composex.common.compose_services import extend_container_envvars
 from ecs_composex.appmesh import appmesh_params, appmesh_conditions, metadata
 from ecs_composex.appmesh.appmesh_params import (
-    NODE_KEY,
-    NODES_KEY,
-    ROUTES_KEY,
-    MATCH_KEY,
     NAME_KEY,
     BACKENDS_KEY,
 )
+from ecs_composex.common import LOG, add_parameters
+from ecs_composex.common.compose_services import extend_container_envvars
+from ecs_composex.common.outputs import ComposeXOutput
+from ecs_composex.dns.dns_params import PRIVATE_DNS_ZONE_NAME
+from ecs_composex.ecs import ecs_params
 
 
 class MeshNode(object):
     """
     Class representing an AppMesh Node.
     """
```

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_params.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_router.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_router.py`

 * *Files 1% similar despite different names*

```diff
@@ -30,15 +30,14 @@
     SCHEME_KEY,
     LISTENER_KEY,
     PROTOCOL_KEY,
     ROUTES_KEY,
     MATCH_KEY,
     NAME_KEY,
     NODES_KEY,
-    NODE_KEY,
     PORT_KEY,
 )
 from ecs_composex.common import NONALPHANUM, keyisset, LOG
 
 
 def define_http_route(route_match, route_nodes):
     route = appmesh.HttpRoute(
```

### Comparing `ecs_composex-0.8.9/ecs_composex/appmesh/appmesh_service.py` & `ecs_composex-0.9.2/ecs_composex/appmesh/appmesh_service.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/cli.py` & `ecs_composex-0.9.2/ecs_composex/cli.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,15 +12,17 @@
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
-"""Console script for ecs_composex."""
+"""
+Console script for ecs_composex.
+"""
 
 import argparse
 import sys
 
 from ecs_composex.common import LOG
 from ecs_composex.common.aws import deploy
 from ecs_composex.common.settings import ComposeXSettings
@@ -28,19 +30,14 @@
 from ecs_composex.ecs_composex import generate_full_template
 
 
 class ArgparseHelper(argparse._HelpAction):
     """
     Used to help print top level '--help' arguments from argparse
     when used with subparsers
-
-    Usage:
-    parser = argparse.ArgumentParser(add_help=False)
-    parser.add_argument('-h', '--help', action=ArgparseHelper,
-                        help='show this help message and exit')
     """
 
     def __call__(self, parser, namespace, values, option_string=None):
         parser.print_help()
         print()
         subparsers_actions = [
             action
```

### Comparing `ecs_composex-0.8.9/ecs_composex/common/__init__.py` & `ecs_composex-0.9.2/ecs_composex/common/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -25,22 +25,23 @@
 import re
 import sys
 from uuid import uuid4
 from datetime import datetime as dt
 from os import environ
 
 import yaml
-from troposphere import Template, Parameter
 
 try:
     from yaml import CLoader as Loader
 except ImportError:
     from yaml import Loader
 
 from troposphere import Ref, AWS_NO_VALUE
+from troposphere import Template, Parameter, Output
+
 from ecs_composex.common import cfn_params
 from ecs_composex.common import cfn_conditions
 
 from ecs_composex import __version__ as version
 
 DATE = dt.utcnow().isoformat()
 FILE_PREFIX = f'{dt.utcnow().strftime("%Y/%m/%d/%H%M")}/{str(uuid4().hex)[:6]}'
@@ -129,14 +130,29 @@
     for param in parameters:
         if not isinstance(param, Parameter):
             raise TypeError("Parameter must be of type", Parameter)
         if template and param.title not in template.parameters:
             template.add_parameter(param)
 
 
+def add_outputs(template, outputs):
+    """Function to add parameters to the template
+
+    :param template: the template to add the parameters to
+    :type template: troposphere.Template
+    :param outputs: list of parameters to add to the template
+    :type outputs: list<troposphere.Output>
+    """
+    for output in outputs:
+        if not isinstance(output, Output):
+            raise TypeError("Parameter must be of type", Output)
+        if template and output.title not in template.outputs:
+            template.add_output(output)
+
+
 def add_defaults(template):
     """Function to CFN parameters and conditions to the template whhich are used
     across ECS ComposeX
 
     :param template: source template to add the params and conditions to
     :type template: Template
     """
```

### Comparing `ecs_composex-0.8.9/ecs_composex/common/aws.py` & `ecs_composex-0.9.2/ecs_composex/common/aws.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/cfn_conditions.py` & `ecs_composex-0.9.2/ecs_composex/common/cfn_conditions.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/cfn_params.py` & `ecs_composex-0.9.2/ecs_composex/common/cfn_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/compose_resources.py` & `ecs_composex-0.9.2/ecs_composex/common/compose_resources.py`

 * *Files 9% similar despite different names*

```diff
@@ -109,20 +109,22 @@
             {}
             if not keyisset("MacroParameters", self.definition)
             else self.definition["MacroParameters"]
         )
         self.cfn_resource = None
         self.output_properties = {}
         self.outputs = []
+        self.attributes_outputs = {}
         self.families_targets = []
         self.families_scaling = []
         self.arn_attr = None
         self.arn_parameter = None
         self.arn_value = None
         self.ref_value = None
+        self.is_nested = False
         self.ref_parameter = Parameter(self.logical_name, Type="String")
         self.set_services_targets(settings)
         self.set_services_scaling(settings)
 
     def __repr__(self):
         return self.logical_name
 
@@ -141,14 +143,15 @@
             if family_name not in [f[0].name for f in self.families_targets]:
                 self.families_targets.append(
                     (
                         settings.families[family_name],
                         False,
                         [the_service],
                         service["access"],
+                        service,
                     )
                 )
 
     def set_services_targets(self, settings):
         """
         Method to map services and families targets of the services defined.
         TargetStructure:
@@ -168,14 +171,15 @@
             ]:
                 self.families_targets.append(
                     (
                         settings.families[service_name],
                         True,
                         settings.families[service_name].services,
                         service["access"],
+                        service,
                     )
                 )
             elif service_name in settings.families and service_name in [
                 f[0].name for f in self.families_targets
             ]:
                 LOG.warning(
                     f"The family {service_name} has already been added. Skipping"
@@ -282,15 +286,21 @@
             else:
                 raise TypeError(
                     f"3rd argument for {definition[0]} must be one of",
                     (Ref, GetAtt),
                     "Got",
                     definition[2],
                 )
-            self.outputs.append(Output(NONALPHANUM.sub("", definition[0]), Value=value))
+            name = NONALPHANUM.sub("", definition[0])
+            self.attributes_outputs[output_prop_name] = {
+                "Name": name,
+                "Output": Output(name, Value=value),
+            }
+        for attr in self.attributes_outputs.values():
+            self.outputs.append(attr["Output"])
 
     def set_resource_arn(self, root_stack_name):
         """
         Method to set the arn value the resource arn to use from root stack to another
         """
         if not isinstance(self.arn_attr, Parameter) or not keyisset(
             self.arn_attr.title, self.output_properties
@@ -322,35 +332,31 @@
         Method to set the value for the default attribute (Ref)
         """
         self.ref_value = GetAtt(root_stack_name, f"Outputs.{self.logical_name}")
 
     def get_resource_attribute_parameter(self, parameter):
         title = parameter.title if isinstance(parameter, Parameter) else parameter
         if not isinstance(parameter, (str, Parameter)) or not keyisset(
-            title, self.output_properties
+            title, self.attributes_outputs
         ):
             raise KeyError(
                 "There is no Output attribute defined for",
                 self.logical_name,
                 "with parameter named",
                 parameter.title if isinstance(parameter, Parameter) else parameter,
             )
-        return Parameter(
-            f"{self.logical_name}{NONALPHANUM.sub('', title)}", Type="String"
-        )
+        return Parameter(f"{self.attributes_outputs[title]['Name']}", Type="String")
 
     def get_resource_attribute_value(self, parameter, stack_name):
         title = parameter.title if isinstance(parameter, Parameter) else parameter
         if not isinstance(parameter, (str, Parameter)) or not keyisset(
-            title, self.output_properties
+            title, self.attributes_outputs
         ):
             raise KeyError(
                 "There is no Output attribute value defined for",
                 self.logical_name,
                 "with parameter named",
                 title,
                 "Existing ones are",
-                self.output_properties.keys(),
+                self.attributes_outputs.keys(),
             )
-        return GetAtt(
-            stack_name, f"Outputs.{self.logical_name}{NONALPHANUM.sub('', title)}"
-        )
+        return GetAtt(stack_name, f"Outputs.{self.attributes_outputs[title]['Name']}")
```

### Comparing `ecs_composex-0.8.9/ecs_composex/common/compose_services.py` & `ecs_composex-0.9.2/ecs_composex/common/compose_services.py`

 * *Files 3% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 
 from troposphere import (
     AWS_NO_VALUE,
     AWS_REGION,
     AWS_STACK_NAME,
 )
 from troposphere import Parameter, Tags
-from troposphere import Sub, Ref, GetAtt, ImportValue
+from troposphere import Sub, Ref, GetAtt, ImportValue, Join
 from troposphere.ecs import (
     HealthCheck,
     Environment,
     PortMapping,
     LogConfiguration,
     ContainerDefinition,
     TaskDefinition,
@@ -54,14 +54,15 @@
 from ecs_composex.ecs.ecs_params import LOG_GROUP_RETENTION
 from ecs_composex.ecs.ecs_params import NETWORK_MODE, EXEC_ROLE_T, TASK_ROLE_T, TASK_T
 from ecs_composex.iam import define_iam_policy, add_role_boundaries
 from ecs_composex.secrets.compose_secrets import (
     ComposeSecret,
     match_secrets_services_config,
 )
+from ecs_composex.vpc.vpc_params import APP_SUBNETS
 
 NUMBERS_REG = r"[^0-9.]"
 MINIMUM_SUPPORTED = 4
 
 
 def import_secrets(template, service, container, settings):
     """
@@ -258,15 +259,15 @@
         ("healthcheck", dict),
         ("hostname", str),
         ("labels", dict),
         ("labels", (dict, list)),
         ("logging", dict),
         ("links", list),
         ("network_mode", str),
-        ("networks", list),
+        ("networks", (list, dict)),
         ("image", str),
         ("init", bool),
         ("isolation", str),
         ("pid", str),
         ("ports", list),
         ("restart", str),
         ("security_opt", str),
@@ -328,15 +329,15 @@
         self.x_configs = set_else_none("x-configs", self.definition)
         self.x_scaling = set_else_none("x-scaling", self.definition, None, False)
         self.x_network = set_else_none("x-network", self.definition, None, False)
         self.x_iam = set_else_none("x-iam", self.definition)
         self.x_logging = {"RetentionInDays": 14, "CreateLogGroup": True}
 
         self.import_x_aws_settings()
-
+        self.networks = {}
         self.replicas = 1
         self.container = None
         self.volumes = []
         self.secrets = []
         self.environment = set_else_none("environment", self.definition, None, False)
         self.cfn_environment = (
             import_env_variables(self.environment)
@@ -358,27 +359,30 @@
         self.ingress_mappings = define_ingress_mappings(self.ports)
         self.mem_alloc = None
         self.mem_resa = None
         self.cpu_amount = None
         self.logging = None
         self.families = []
         self.my_family = None
+        self.is_aws_sidecar = False
+        self.is_essential = True
         self.container_definition = None
 
         self.container_start_condition = "START"
         self.healthcheck = set_else_none("healthcheck", self.definition, None)
         self.ecs_healthcheck = Ref(AWS_NO_VALUE)
         self.set_ecs_healthcheck()
         self.define_logging()
         self.container_parameters = {}
 
         self.map_volumes(volumes)
         self.map_secrets(secrets)
         self.set_service_deploy()
         self.set_container_definition()
+        self.set_networks()
 
     def set_container_definition(self):
         """
         Function to define the container definition matching the service definition
         """
         secrets = [secret for secrets in self.secrets for secret in secrets.ecs_secret]
         self.container_definition = ContainerDefinition(
@@ -401,19 +405,28 @@
                     "awslogs-region": Ref(AWS_REGION),
                     "awslogs-stream-prefix": self.name,
                 },
             ),
             Command=self.command,
             HealthCheck=self.ecs_healthcheck,
             DependsOn=Ref(AWS_NO_VALUE),
-            Essential=True,
+            Essential=self.is_essential,
             Secrets=secrets,
         )
         self.container_parameters.update({self.image_param.title: self.image})
 
+    def set_networks(self):
+        if not keyisset("networks", self.definition):
+            return
+        if isinstance(self.definition["networks"], list):
+            for name in self.definition["networks"]:
+                self.networks[name] = None
+        elif isinstance(self.definition["networks"], dict):
+            self.networks.update(self.definition["networks"])
+
     def merge_x_aws_role(self, key):
         """
         Method to update the service definition with the x-aws-role information if NOT defined in the composex
         definition.
 
         :param str key:
         """
@@ -575,14 +588,40 @@
     def set_replicas(self, deployment):
         """
         Function to set the service deployment settings.
         """
         if keyisset("replicas", deployment):
             self.replicas = int(deployment["replicas"])
 
+    def define_essential(self, deployment):
+        """
+        Method to define whether the container is essential.
+        :param dict deployment:
+        """
+        essential_key = "ecs.essential"
+        labels = "labels"
+        positive_values = [True, "yes", "True"]
+        negative_values = [False, "no", "False"]
+        if keyisset(labels, deployment) and keyisset(essential_key, deployment[labels]):
+            if (
+                deployment[labels][essential_key] not in positive_values
+                or deployment[labels][essential_key] not in negative_values
+            ):
+                raise ValueError(
+                    "The values allowed for",
+                    essential_key,
+                    "are",
+                    positive_values,
+                    negative_values,
+                    "Got",
+                    deployment[labels][essential_key],
+                )
+            if deployment[labels][essential_key] in negative_values:
+                self.is_essential = False
+
     def define_start_condition(self, deployment):
         """
         Method to define the start condition success for the container
 
         :param deployment:
         :return:
         """
@@ -590,14 +629,16 @@
         labels = "labels"
         allowed_values = ["START", "COMPLETE", "SUCCESS", "HEALTHY"]
         if not isinstance(self.ecs_healthcheck, Ref):
             LOG.warning(
                 f"Healthcheck was defined on {self.name}. Overriding to HEALTHY"
             )
             self.container_start_condition = "HEALTHY"
+            if not self.is_essential:
+                self.is_essential = True
         elif keyisset(labels, deployment) and keyisset(depends_key, deployment[labels]):
             if deployment[labels][depends_key] not in allowed_values:
                 raise ValueError(
                     f"Attribute {depends_key} is invalid. Must be one of",
                     allowed_values,
                 )
             self.container_start_condition = deployment[labels][depends_key]
@@ -632,14 +673,15 @@
         deploy = "deploy"
         if not keyisset("deploy", self.definition):
             return
         self.define_families(self.definition[deploy])
         self.set_compute_resources(self.definition[deploy])
         self.set_replicas(self.definition[deploy])
         self.define_start_condition(self.definition[deploy])
+        self.define_essential(self.definition[deploy])
 
 
 def handle_same_task_services_dependencies(services_config):
     """
     Function to define inter-tasks dependencies
 
     :param list services_config:
@@ -838,14 +880,15 @@
                     "x-iam": {
                         "ManagedPolicyArns": [
                             "arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess"
                         ]
                     },
                 },
             )
+            xray_service.is_aws_sidecar = True
             for service in self.services:
                 service.depends_on.append(xray_service.name)
                 LOG.debug(f"Adding xray-daemon as dependency to {service.name}")
             self.add_service(xray_service)
             if xray_service.name not in self.ignored_services:
                 self.ignored_services.append(xray_service)
 
@@ -904,28 +947,40 @@
         :return:
         """
         service_configs = [[0, service] for service in self.services]
         handle_same_task_services_dependencies(service_configs)
         ordered_containers_config = sorted(service_configs, key=lambda i: i[0])
         self.ordered_services = [s[1] for s in ordered_containers_config]
         for service in self.ordered_services:
-            service.container_definition.Essential = False
-        ordered_containers_config[0][1].container_definition.Essential = True
+            if (
+                service.container_start_condition == "SUCCESS"
+                or service.container_start_condition == "COMPLETE"
+                or service.is_aws_sidecar
+                or not service.is_essential
+            ):
+                service.container_definition.Essential = False
+            else:
+                service.container_definition.Essential = True
+
         LOG.debug(service_configs, ordered_containers_config)
         LOG.debug(
             "Essentially",
             ordered_containers_config[0][1].name,
             ordered_containers_config[0][1].container_definition.Essential,
         )
         LOG.debug(
             dumps(
                 [service.container_definition.to_dict() for service in self.services],
                 indent=4,
             )
         )
+        if len(ordered_containers_config) == 1:
+            LOG.debug("There is only one service, we need to ensure it is essential")
+            ordered_containers_config[0][1].container_definition.Essential = True
+
         for service in self.services:
             self.stack_parameters.update(service.container_parameters)
 
     def sort_iam_settings(self, key, setting):
         """
         Method to sort out iam configuration
 
@@ -948,14 +1003,15 @@
             ("Policies", list, add_policies),
             ("PermissionsBoundary", (str, Sub), handle_iam_boundary),
         ]
         iam_settings = [service.x_iam for service in self.services if service.x_iam]
         for setting in iam_settings:
             for key in valid_keys:
                 self.sort_iam_settings(key, setting)
+
         self.set_secrets_access()
 
     def handle_permission_boundary(self, prop_key):
         if keyisset("PermissionsBoundary", self.iam) and self.template:
             if EXEC_ROLE_T in self.template.resources:
                 add_role_boundaries(
                     self.template.resources[EXEC_ROLE_T], self.iam[prop_key]
@@ -1122,7 +1178,23 @@
             logging_def.Options.update(self.task_logging_options)
 
     def init_task_definition(self):
         add_service_roles(self.template)
         self.set_task_compute_parameter()
         self.set_task_definition()
         self.refresh_container_logging_definition()
+
+    def update_family_subnets(self, settings):
+        """
+        Method to update the stack parameters
+
+        :param ecs_composex.common.settings.ComposeXSettings settings:
+        """
+        network_names = list(self.service_config.network.networks.keys())
+        for network in settings.networks:
+            if network.name in network_names:
+                self.stack_parameters.update(
+                    {APP_SUBNETS.title: Join(",", Ref(network.subnet_name))}
+                )
+                LOG.info(
+                    f"Set {network.subnet_name} as {APP_SUBNETS.title} for {self.name}"
+                )
```

### Comparing `ecs_composex-0.8.9/ecs_composex/common/compose_volumes.py` & `ecs_composex-0.9.2/ecs_composex/common/compose_volumes.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/config.py` & `ecs_composex-0.9.2/ecs_composex/common/config.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/ecs_composex.py` & `ecs_composex-0.9.2/ecs_composex/common/ecs_composex.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/envsubst.py` & `ecs_composex-0.9.2/ecs_composex/common/envsubst.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/files.py` & `ecs_composex-0.9.2/ecs_composex/common/files.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/outputs.py` & `ecs_composex-0.9.2/ecs_composex/common/outputs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/settings.py` & `ecs_composex-0.9.2/ecs_composex/common/settings.py`

 * *Files 3% similar despite different names*

```diff
@@ -35,14 +35,15 @@
 from ecs_composex.common.cfn_params import USE_FLEET_T
 from ecs_composex.secrets.compose_secrets import ComposeSecret
 from ecs_composex.common.compose_services import (
     ComposeService,
     ComposeFamily,
 )
 from ecs_composex.common.compose_volumes import ComposeVolume
+from ecs_composex.common.compose_networks import ComposeNetwork
 from ecs_composex.common.envsubst import expandvars
 from ecs_composex.iam import ROLE_ARN_ARG
 from ecs_composex.iam import validate_iam_role_arn
 from ecs_composex.utils.init_ecs import set_ecs_settings
 from ecs_composex.utils.init_s3 import create_bucket
 
 
@@ -119,16 +120,17 @@
             )
         elif (
             isinstance(override_def[key], list)
             and key in original_def.keys()
             and key == "ports"
         ):
             original_def[key] = merge_ports(original_def[key], override_def[key])
-
-        elif not isinstance(override_def[key], (list, dict)):
+        elif isinstance(override_def[key], str):
+            original_def[key] = expandvars(override_def[key])
+        else:
             original_def[key] = override_def[key]
     return original_def
 
 
 def interpolate_env_vars(content):
     """
     Function to interpolate env vars from content
@@ -144,15 +146,15 @@
         elif isinstance(content[key], list):
             for count, item in enumerate(content[key]):
                 if isinstance(item, dict):
                     interpolate_env_vars(item)
                 elif isinstance(item, str):
                     content[key][count] = expandvars(item)
         elif isinstance(content[key], str):
-            content[key] = expandvars(content[key])
+            content[key] = expandvars(content[key], default="")
 
 
 def merge_services_from_files(original_services, override_services):
     """
     Function to merge two docker compose files content.
 
     """
@@ -166,26 +168,29 @@
                     )
                 }
             )
         else:
             original_services.update({service_name: override_services[service_name]})
 
 
-def handle_lists_merges(original_list, override_list):
+def handle_lists_merges(original_list, override_list, uniqfy=False):
     """
 
-    :param list original_list:
-    :param list override_list:
-    :return:
+    :param list original_list: The original list to add the override ones to
+    :param list override_list: The lost of items to add up
+    :param bool uniqfy: Whether you are expecting identical dicts which should be filtered to be uniqu based on values.
+    :return: The merged list
+    :rtype: list
     """
     final_list = []
 
     final_list += [item for item in original_list if isinstance(item, dict)]
     final_list += [item for item in override_list if isinstance(item, dict)]
-
+    if uniqfy:
+        final_list = [dict(y) for y in set(tuple(x.items()) for x in final_list)]
     original_str_items = [item for item in original_list if isinstance(item, list)]
     final_list += list(
         set(
             original_str_items
             + [item for item in override_list if isinstance(item, list)]
         )
     )
@@ -199,54 +204,72 @@
     elif origin_list_items and not override_list_items:
         final_list += origin_list_items
     elif not origin_list_items and override_list_items:
         final_list += override_list_items
     return final_list
 
 
+def handle_lists_merge_conditions(original_def, override_def, key):
+    """
+    Function to handle lists merging and whether some additional handling is necessary for duplicates
+
+    :param dict original_def: The src definition
+    :param dict override_def: The override definition to merge to src.
+    :param str key: The key name of the list object
+    """
+    keys_to_uniqfy = ["Tags", "volumes", "secrets"]
+    if not isinstance(original_def[key], list):
+        raise TypeError(
+            "Cannot merge",
+            key,
+            "from",
+            type(original_def[key]),
+            "with",
+            type(override_def[key]),
+        )
+    if key in keys_to_uniqfy:
+        original_def[key] = handle_lists_merges(
+            original_def[key], override_def[key], uniqfy=True
+        )
+    else:
+        original_def[key] = handle_lists_merges(
+            original_def[key], override_def[key], uniqfy=False
+        )
+
+
 def merge_definitions(original_def, override_def, nested=False):
     """
     Merges two services definitions if service exists in both compose files.
 
     :param bool nested:
     :param dict original_def:
     :param dict override_def:
     :return:
     """
-
     if not nested:
         original_def = deepcopy(original_def)
     elif not isinstance(override_def, dict):
         raise TypeError("Expected", dict, "got", type(override_def))
     for key in override_def.keys():
         if (
             isinstance(override_def[key], dict)
             and keyisset(key, original_def)
             and isinstance(original_def[key], dict)
         ):
             merge_definitions(original_def[key], override_def[key], nested=True)
         elif key not in original_def:
             original_def[key] = override_def[key]
         elif isinstance(override_def[key], list) and key in original_def.keys():
-            if not isinstance(original_def[key], list):
-                raise TypeError(
-                    "Cannot merge",
-                    key,
-                    "from",
-                    type(original_def[key]),
-                    "with",
-                    type(override_def[key]),
-                )
-            original_def[key] = handle_lists_merges(
-                original_def[key], override_def[key]
-            )
+            handle_lists_merge_conditions(original_def, override_def, key)
         elif isinstance(override_def[key], list) and key not in original_def.keys():
             original_def[key] = override_def[key]
 
-        elif not isinstance(override_def[key], (list, dict)):
+        elif isinstance(override_def[key], str):
+            original_def[key] = expandvars(override_def[key])
+        else:
             original_def[key] = override_def[key]
     return original_def
 
 
 def merge_config_files(original_content, override_content):
     """
     Function to merge everything that is not services
@@ -372,14 +395,16 @@
 
         self.bucket_name = (
             None if not keyisset(self.bucket_arg, kwargs) else kwargs[self.bucket_arg]
         )
         self.volumes = []
         self.services = []
         self.secrets = []
+        self.networks = []
+        self.subnets_parameters = []
         self.secrets_mappings = {}
         self.families = {}
         self.account_id = None
         self.output_dir = self.default_output_dir
         self.format = self.default_format
 
         self.create_vpc = False
@@ -431,14 +456,36 @@
         for volume_name in self.compose_content[ComposeVolume.main_key]:
             volume = ComposeVolume(
                 volume_name, self.compose_content[ComposeVolume.main_key][volume_name]
             )
             self.compose_content[ComposeVolume.main_key][volume_name] = volume
             self.volumes.append(volume)
 
+    def set_networks(self, vpc_stack, root_stack):
+        """
+        Method configuring the networks defined at root level
+        :return:
+        """
+        if not keyisset(ComposeNetwork.main_key, self.compose_content):
+            LOG.debug("No networks detected at the root level of compose file")
+            return
+        elif vpc_stack:
+            LOG.info(
+                "ComposeX will be creating the VPC, therefore networks are ignored!"
+            )
+            return
+        for network_name in self.compose_content[ComposeNetwork.main_key]:
+            network = ComposeNetwork(
+                network_name,
+                self.compose_content[ComposeNetwork.main_key][network_name],
+                self.subnets_parameters,
+            )
+            self.compose_content[ComposeNetwork.main_key][network_name] = network
+            self.networks.append(network)
+
     def set_services(self):
         """
         Method to define the ComposeXResource for each service.
         :return:
         """
         if not keyisset(ComposeService.main_key, self.compose_content):
             return
```

### Comparing `ecs_composex-0.8.9/ecs_composex/common/stacks.py` & `ecs_composex-0.9.2/ecs_composex/common/stacks.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/common/tagging.py` & `ecs_composex-0.9.2/ecs_composex/common/tagging.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/compute/__init__.py` & `ecs_composex-0.9.2/ecs_composex/compute/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/compute/compute_conditions.py` & `ecs_composex-0.9.2/ecs_composex/compute/compute_conditions.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/compute/compute_params.py` & `ecs_composex-0.9.2/ecs_composex/compute/compute_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/compute/compute_stack.py` & `ecs_composex-0.9.2/ecs_composex/compute/compute_stack.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/compute/compute_template.py` & `ecs_composex-0.9.2/ecs_composex/compute/compute_template.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/compute/hosts_template.py` & `ecs_composex-0.9.2/ecs_composex/compute/hosts_template.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/compute/spot_fleet.py` & `ecs_composex-0.9.2/ecs_composex/compute/spot_fleet.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dns/__init__.py` & `ecs_composex-0.9.2/ecs_composex/dns/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dns/dns_conditions.py` & `ecs_composex-0.9.2/ecs_composex/dns/dns_conditions.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dns/dns_lookup.py` & `ecs_composex-0.9.2/ecs_composex/dns/dns_lookup.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dns/dns_params.py` & `ecs_composex-0.9.2/ecs_composex/dns/dns_params.py`

 * *Files 13% similar despite different names*

```diff
@@ -15,16 +15,21 @@
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 Module for DNS parameters
 """
 
+from os import path
 from troposphere import Parameter, Sub
 
+MOD_KEY = path.basename(path.dirname(path.abspath(__file__)))
+RES_KEY = f"x-{path.basename(path.dirname(path.abspath(__file__)))}"
+
+
 ZONES_PATTERN = r"^none$|^ns-[a-z0-9]{6,24}$|^Z[0-9A-Z]+$"
 
 PUBLIC_DNS_ZONE_NAME_T = "PublicDnsZoneName"
 PUBLIC_DNS_ZONE_NAME = Parameter(
     PUBLIC_DNS_ZONE_NAME_T, Type="String", Default="none.existant"
 )
```

### Comparing `ecs_composex-0.8.9/ecs_composex/docdb/__init__.py` & `ecs_composex-0.9.2/ecs_composex/docdb/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/docdb/docdb_ecs.py` & `ecs_composex-0.9.2/ecs_composex/docdb/docdb_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/docdb/docdb_params.py` & `ecs_composex-0.9.2/ecs_composex/docdb/docdb_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/docdb/docdb_stack.py` & `ecs_composex-0.9.2/ecs_composex/docdb/docdb_stack.py`

 * *Files 3% similar despite different names*

```diff
@@ -47,15 +47,17 @@
         """
         self.db_secret = None
         self.db_sg = None
         super().__init__(name, definition, settings)
         self.arn_attr = DOCDB_SECRET
 
     def init_outputs(self):
-        print(self.arn_attr, type(self.arn_attr))
+        """
+        Method to init the DocDB output attributes
+        """
         self.output_properties = {
             DOCDB_NAME.title: (self.logical_name, self.cfn_resource, Ref, None),
             DOCDB_PORT.title: (
                 f"{self.logical_name}{DOCDB_PORT.title}",
                 self.cfn_resource,
                 GetAtt,
                 DOCDB_PORT.title,
```

### Comparing `ecs_composex-0.8.9/ecs_composex/docdb/docdb_template.py` & `ecs_composex-0.9.2/ecs_composex/docdb/docdb_template.py`

 * *Files 15% similar despite different names*

```diff
@@ -20,14 +20,15 @@
 """
 
 from troposphere import AWS_NO_VALUE, AWS_STACK_NAME
 from troposphere import Sub, Ref, GetAtt, Tags
 from troposphere import docdb
 from troposphere.ec2 import SecurityGroup
 
+from ecs_composex.resources_import import import_record_properties
 from ecs_composex.common import (
     keyisset,
     keypresent,
     build_template,
 )
 from ecs_composex.docdb.docdb_params import DOCDB_SUBNET_GROUP_T
 from ecs_composex.secrets import (
@@ -68,43 +69,28 @@
     """
     Function to parse and transform yaml definition to Troposphere
 
     :param ecs_composex.docdb.docdb_stack.DocDb db:
     :param troposphere.secretsmanager.Secret secret:
     :param list<roposphere.ec2.SecurityGroup> sgs:
     """
-
-    props = {
-        "AvailabilityZones": Ref(AWS_NO_VALUE),
-        "DBClusterIdentifier": Ref(AWS_NO_VALUE),
-        "DBSubnetGroupName": Ref(DOCDB_SUBNET_GROUP_T),
-        "EngineVersion": no_value_if_not_set("EngineVersion", db.properties),
-        "Port": no_value_if_not_set("Port", db.properties),
-        "PreferredMaintenanceWindow": no_value_if_not_set(
-            "PreferredMaintenanceWindow", db.properties
-        ),
-        "PreferredBackupWindow": no_value_if_not_set(
-            "PreferredBackupWindow", db.properties
-        ),
-        "SnapshotIdentifier": Ref(AWS_NO_VALUE),
-        "StorageEncrypted": True
-        if not keypresent("StorageEncrypted", db.properties)
-        else db.properties["StorageEncrypted"],
-        "Tags": Tags(Name=Sub(f"docdb.{db.logical_name}")),
-        "VpcSecurityGroupIds": sgs,
-        "MasterUsername": Sub(
-            f"{{{{resolve:secretsmanager:${{{secret.title}}}:SecretString:username}}}}"
-        ),
-        "MasterUserPassword": Sub(
-            f"{{{{resolve:secretsmanager:${{{secret.title}}}:SecretString:password}}}}"
-        ),
-        "EnableCloudwatchLogsExports": no_value_if_not_set(
-            db.properties, "EnableCloudwatchLogsExports"
-        ),
-    }
+    props = import_record_properties(db.properties, docdb.DBCluster)
+    if not keypresent("StorageEncrypted", props):
+        props["StorageEncrypted"] = True
+    props.update(
+        {
+            "VpcSecurityGroupIds": sgs,
+            "MasterUsername": Sub(
+                f"{{{{resolve:secretsmanager:${{{secret.title}}}:SecretString:username}}}}"
+            ),
+            "MasterUserPassword": Sub(
+                f"{{{{resolve:secretsmanager:${{{secret.title}}}:SecretString:password}}}}"
+            ),
+        }
+    )
     db.cfn_resource = docdb.DBCluster(db.logical_name, **props)
 
 
 def add_db_instances(template, db):
     """
     Function to add DB Instances either based on properties or default.
     Default is to add one DB Instance, the smallest size there is.
@@ -127,28 +113,25 @@
         for count, instance in enumerate(db.parameters["Instances"]):
             if not isinstance(instance, dict):
                 raise TypeError("Instances definition should be all objects/dict")
             if not keyisset("DBInstanceClass", instance):
                 raise KeyError(
                     "You must specify at least the DBInstanceClass", instance.keys()
                 )
+            instance.update(
+                {
+                    "DBClusterIdentifier": Ref(db.cfn_resource),
+                    "Tags": Tags(DocDbCluster=Ref(db.cfn_resource)),
+                }
+            )
+            instance_props = import_record_properties(
+                instance, docdb.DBInstance, ignore_missing_required=True
+            )
             template.add_resource(
-                docdb.DBInstance(
-                    f"{db.logical_name}Instance{count}",
-                    DBClusterIdentifier=Ref(db.cfn_resource),
-                    DBInstanceClass=instance["DBInstanceClass"],
-                    DBInstanceIdentifier=Ref(AWS_NO_VALUE),
-                    PreferredMaintenanceWindow=no_value_if_not_set(
-                        instance, "PreferredMaintenanceWindow"
-                    ),
-                    AutoMinorVersionUpgrade=no_value_if_not_set(
-                        instance, "AutoMinorVersionUpgrade", True
-                    ),
-                    Tags=Tags(DocDbCluster=Ref(db.cfn_resource)),
-                )
+                docdb.DBInstance(f"{db.logical_name}Instance{count}", **instance_props)
             )
 
 
 def create_docdb_template(new_resources, settings):
     """
     Function to create the root template for DocDB and associate the new resources to it.
```

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/__init__.py` & `ecs_composex-0.9.2/ecs_composex/dynamodb/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_aws.py` & `ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_aws.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_ecs.py` & `ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_params.py` & `ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_perms.json` & `ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_perms.json`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_perms.py` & `ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_perms.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_stack.py` & `ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_stack.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/dynamodb/dynamodb_template.py` & `ecs_composex-0.9.2/ecs_composex/dynamodb/dynamodb_template.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/__init__.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_service_config.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,87 +1,58 @@
-# -*- coding: utf-8 -*-
-#  ECS ComposeX <https://github.com/lambda-my-aws/ecs_composex>
-#  Copyright (C) 2020  John Mille <john@lambda-my-aws.io>
-#
-#  This program is free software: you can redistribute it and/or modify
-#  it under the terms of the GNU General Public License as published by
-#  the Free Software Foundation, either version 3 of the License, or
-#  (at your option) any later version.
-#
-#  This program is distributed in the hope that it will be useful,
-#  but WITHOUT ANY WARRANTY; without even the implied warranty of
-#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-#  GNU General Public License for more details.
-#
-#  You should have received a copy of the GNU General Public License
-#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
+﻿#  -*- coding: utf-8 -*-
+#   ECS ComposeX <https://github.com/lambda-my-aws/ecs_composex>
+#   Copyright (C) 2020  John Mille <john@lambda-my-aws.io>
+#  #
+#   This program is free software: you can redistribute it and/or modify
+#   it under the terms of the GNU General Public License as published by
+#   the Free Software Foundation, either version 3 of the License, or
+#   (at your option) any later version.
+#  #
+#   This program is distributed in the hope that it will be useful,
+#   but WITHOUT ANY WARRANTY; without even the implied warranty of
+#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
+#   GNU General Public License for more details.
+#  #
+#   You should have received a copy of the GNU General Public License
+#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
-Core module for ECS ComposeX.
-
-This module is going to parse each ecs_service and each x-resource key from the compose file
-(hence ComposeX) and determine its
-
-* ServiceDefinition
-* TaskDefinition
-* TaskRole
-* ExecutionRole
-
-It is going to also, based on the labels set in the compose file
-
-* Add the ecs_service to Service Discovery via AWS CloudMap
-* Add load-balancers to dispatch traffic to the microservice
-
+Module for the ServiceConfig Class which is used for Container, Task and Service definitions.
 """
 
-from troposphere import Ref, If
-
-from ecs_composex import __version__ as version
-from ecs_composex.common.stacks import ComposeXStack
-from ecs_composex.ecs import ecs_params
-from ecs_composex.ecs.ecs_conditions import CREATE_CLUSTER_CON_T
-from ecs_composex.ecs.ecs_params import CLUSTER_NAME, CLUSTER_T
-from ecs_composex.ecs.ecs_template import generate_services
-
-metadata = {
-    "Type": "ComposeX",
-    "Properties": {"ecs_composex::module": "ecs_composex.ecs", "Version": version},
-}
+from ecs_composex.common import keyisset
+from ecs_composex.ecs.ecs_params import SERVICE_COUNT
+from ecs_composex.ecs.ecs_scaling import ServiceScaling
+from ecs_composex.ecs.ecs_service_network_config import ServiceNetworking
 
 
-class ServiceStack(ComposeXStack):
+class ServiceConfig(object):
     """
-    Class to identify specifically a service stack
-    """
-
+    Class specifically dealing with the configuration and settings of the ecs_service from how it was defined in
+    the compose file
 
-def associate_services_to_root_stack(root_stack, settings, dns_params, vpc_stack=None):
+    :cvar list keys: List of valid settings for a service in Docker compose syntax reference
+    :cvar list service_config_keys: list of extra configuration that apply to services.
+    :cvar bool use_cloudmap: Indicates whether or not the service will be added to the VPC CloudMap
+    :cvar bool use_alb: Indicates to use an AWS Application LoadBalancer (ELBv2, type application)
+    :cvar bool use_nlb: Indicates to use an AWS Application LoadBalancer (ELBv2, type network)
+    :cvar bool is_public: Indicates whether the service should be accessible publicly
     """
-    Function to generate all services and associate their stack to the root stack
 
-    :param ecs_composex.common.stacks.ComposeXStack root_stack:
-    :param ecs_composex.common.settings.ComposeXSettings settings:
-    :param ecs_composex.common.stacks.ComposeXStack vpc_stack:
-    :return:
-    """
-    generate_services(settings)
-    for family_name in settings.families:
-        family = settings.families[family_name]
-        family.stack = ServiceStack(
-            family.logical_name,
-            stack_template=family.template,
-            stack_parameters=family.stack_parameters,
+    def __init__(self, family, settings):
+        """
+        Function to initialize the ecs_service configuration
+
+        :param ecs_composex.common.compose_services.ComposeFamily family:
+        :param ecs_composex.common.settings.ComposeXSettings settings:
+        """
+        self.network = ServiceNetworking(family)
+        self.scaling = ServiceScaling(family.ordered_services)
+        self.use_appmesh = (
+            False if not keyisset("x-appmesh", settings.compose_content) else True
         )
-        family.stack_parameters.update(
-            {
-                ecs_params.CLUSTER_NAME.title: If(
-                    CREATE_CLUSTER_CON_T, Ref(CLUSTER_T), Ref(CLUSTER_NAME)
-                ),
-            }
-        )
-        family.stack_parameters.update(dns_params)
-        if not vpc_stack:
-            family.stack.no_vpc_parameters()
-        else:
-            family.stack.get_from_vpc_stack(vpc_stack)
-        family.template.set_metadata(metadata)
-        root_stack.stack_template.add_resource(family.stack)
+        self.replicas = max([service.replicas for service in family.services])
+        if self.replicas != SERVICE_COUNT.Default:
+            family.stack_parameters[SERVICE_COUNT.title] = self.replicas
+
+    def debug(self):
+        print(self.replicas, self.network, self.scaling)
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/docker_tools.py` & `ecs_composex-0.9.2/ecs_composex/ecs/docker_tools.py`

 * *Files 5% similar despite different names*

```diff
@@ -30,15 +30,25 @@
 
 
 def handle_bytes_units(value, factor):
     """
     Function to handle KB use-case
     """
     amount = float(re.sub(NUMBERS_REG, "", value))
-    unit = "KBytes"
+    if factor == pow(2, 10):
+        unit = "KBytes"
+    elif factor == pow(pow(2, 10), 2):
+        unit = "Bytes"
+    else:
+        raise ValueError(
+            "Factor is not valid.",
+            factor,
+            "Must be one of",
+            [pow(2, 10), pow(pow(2, 10), 2)],
+        )
     if amount < (MINIMUM_SUPPORTED * factor):
         LOG.warning(
             f"You set unit to {unit} and value is lower than {MINIMUM_SUPPORTED}MB. "
             "Setting to minimum supported by Docker"
         )
         return MINIMUM_SUPPORTED * factor
     else:
@@ -55,22 +65,22 @@
     b_pat = re.compile(r"(^[0-9.]+(b|B)$)")
     kb_pat = re.compile(r"(^[0-9.]+(k|kb|kB|Kb|K|KB)$)")
     mb_pat = re.compile(r"(^[0-9.]+(m|mb|mB|Mb|M|MB)$)")
     gb_pat = re.compile(r"(^[0-9.]+(g|gb|gB|Gb|G|GB)$)")
     amount = float(re.sub(NUMBERS_REG, "", value))
     unit = "MBytes"
     if b_pat.findall(value):
-        final_amount = handle_bytes_units(value, (1024 ^ 2))
+        final_amount = handle_bytes_units(value, pow(pow(2, 10), 2))
     elif kb_pat.findall(value):
-        final_amount = handle_bytes_units(value, 1024)
+        final_amount = handle_bytes_units(value, pow(2, 10))
     elif mb_pat.findall(value):
         final_amount = int(amount)
     elif gb_pat.findall(value):
         unit = "GBytes"
-        final_amount = int(amount) * 1024
+        final_amount = int(amount) * pow(2, 10)
     else:
         raise ValueError(f"Could not parse {value} to units")
     LOG.debug(f"Computed unit for {value}: {unit}. Results into {final_amount}MB")
     return int(final_amount)
 
 
 def find_closest_ram_config(ram, ram_range):
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_cluster.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_cluster.py`

 * *Files 11% similar despite different names*

```diff
@@ -13,29 +13,27 @@
 #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #   GNU General Public License for more details.
 #  #
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 from botocore.exceptions import ClientError
-
-from troposphere import If, Ref, Not, Equals
 from troposphere import AWS_STACK_NAME
+from troposphere import If, Ref
 from troposphere.ecs import Cluster, CapacityProviderStrategyItem
 
+from ecs_composex.resources_import import import_record_properties
 from ecs_composex.common import LOG, keyisset
-
-from ecs_composex.ecs.ecs_params import CLUSTER_NAME, CLUSTER_T, CREATE_CLUSTER
+from ecs_composex.ecs import metadata
 from ecs_composex.ecs.ecs_conditions import (
     GENERATED_CLUSTER_NAME_CON_T,
     CREATE_CLUSTER_CON_T,
     GENERATED_CLUSTER_NAME_CON,
 )
-from ecs_composex.ecs import metadata
-
+from ecs_composex.ecs.ecs_params import CLUSTER_NAME, CLUSTER_T, CREATE_CLUSTER
 
 RES_KEY = "x-cluster"
 FARGATE_PROVIDER = "FARGATE"
 FARGATE_SPOT_PROVIDER = "FARGATE_SPOT"
 DEFAULT_PROVIDERS = [FARGATE_PROVIDER, FARGATE_SPOT_PROVIDER]
 DEFAULT_STRATEGY = [
     CapacityProviderStrategyItem(
@@ -94,59 +92,29 @@
             )
             return cluster_r["clusters"][0]["clusterName"]
     except ClientError as error:
         LOG.error(error)
         raise
 
 
-def import_capacity_strategy(strategy_def):
-    """
-    Function to create the Capacity Provider strategies.
-
-    :param strategy_def:
-    :return:
-    """
-    strategies = []
-    if not isinstance(strategy_def, list):
-        raise ValueError("DefaultCapacityProviderStrategy must be a list")
-    for strategy in strategy_def:
-        strategies.append(CapacityProviderStrategyItem(**strategy))
-    return strategies
-
-
-def define_cluster(root_stack, cluster_def):
+def define_cluster(cluster_def):
     """
     Function to create the cluster from provided properties.
 
     :param dict cluster_def:
-    :param ecs_composex.common.stacks.ComposeXStack root_stack:
     :return: cluster
     :rtype: troposphere.ecs.Cluster
     """
-    cluster_params = {}
-    props = cluster_def["Properties"]
-    if not keyisset("CapacityProviders", props):
-        LOG.warning("No capacity providers defined. Setting it to default.")
-        cluster_params["CapacityProviders"] = DEFAULT_PROVIDERS
-    else:
-        cluster_params["CapacityProviders"] = props["CapacityProviders"]
-    if not keyisset("DefaultCapacityProviderStrategy", props):
-        LOG.warning("No Default Strategy set. Setting to default.")
-        cluster_params["DefaultCapacityProviderStrategy"] = DEFAULT_STRATEGY
-    else:
-        cluster_params["DefaultCapacityProviderStrategy"] = import_capacity_strategy(
-            props["DefaultCapacityProviderStrategy"]
-        )
-    cluster_params["Metadata"] = metadata
-    cluster_params["ClusterName"] = (
-        Ref(AWS_STACK_NAME)
-        if not keyisset("ClusterName", props)
-        else props["ClusterName"]
+    compose_props = cluster_def["Properties"]
+    props = import_record_properties(compose_props, Cluster)
+    props["Metadata"] = metadata
+    props["ClusterName"] = (
+        Ref(AWS_STACK_NAME) if not keyisset("ClusterName", props) else Ref(CLUSTER_NAME)
     )
-    cluster = Cluster(CLUSTER_T, Condition=CREATE_CLUSTER_CON_T, **cluster_params)
+    cluster = Cluster(CLUSTER_T, Condition=CREATE_CLUSTER_CON_T, **props)
     return cluster
 
 
 def handle_cluster_settings(root_stack, settings):
     """
     Function to create the ECS Cluster.
 
@@ -171,16 +139,25 @@
                 settings.session, settings.compose_content[RES_KEY]["Lookup"]
             )
             if cluster_name:
                 root_stack.Parameters.update(
                     {CLUSTER_NAME.title: cluster_name, CREATE_CLUSTER.title: "False"}
                 )
         elif keyisset("Properties", settings.compose_content[RES_KEY]):
-            cluster = define_cluster(root_stack, settings.compose_content[RES_KEY])
+            cluster = define_cluster(settings.compose_content[RES_KEY])
             root_stack.stack_template.add_resource(cluster)
+            root_stack.Parameters.update({CREATE_CLUSTER.title: "True"})
+            if keyisset("ClusterName", settings.compose_content[RES_KEY]["Properties"]):
+                root_stack.Parameters.update(
+                    {
+                        CLUSTER_NAME.title: settings.compose_content[RES_KEY][
+                            "Properties"
+                        ]["ClusterName"]
+                    }
+                )
     if CLUSTER_T not in root_stack.stack_template.resources:
         root_stack.stack_template.add_resource(get_default_cluster_config())
 
 
 def add_ecs_cluster(settings, root_stack):
     """
     Function to add the cluster to the root template.
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_conditions.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_conditions.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_iam.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_iam.py`

 * *Files 2% similar despite different names*

```diff
@@ -40,14 +40,15 @@
     Role(
         EXEC_ROLE_T,
         template=template,
         AssumeRolePolicyDocument=service_role_trust_policy("ecs-tasks"),
         Description=Sub(
             f"Execution role for ${{{SERVICE_NAME_T}}} in ${{{CLUSTER_NAME_T}}}"
         ),
+        ManagedPolicyArns=[],
         Policies=[
             Policy(
                 PolicyName=Sub("EcsExecRole"),
                 PolicyDocument={
                     "Version": "2012-10-17",
                     "Statement": [
                         {
@@ -95,23 +96,21 @@
                             "Resource": ["*"],
                         },
                     ],
                 },
             )
         ],
     )
-    policies = []
-    managed_policies = []
     Role(
         TASK_ROLE_T,
         template=template,
         AssumeRolePolicyDocument=service_role_trust_policy("ecs-tasks"),
         Description=Sub(f"TaskRole - ${{{SERVICE_NAME_T}}} in ${{{CLUSTER_NAME_T}}}"),
-        ManagedPolicyArns=managed_policies,
-        Policies=policies,
+        ManagedPolicyArns=[],
+        Policies=[],
     )
 
 
 def define_service_containers(service_template):
     """Function to set the containers list from the service_task definition object
 
     :param service_template: the task definition
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_params.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_params.py`

 * *Files 1% similar despite different names*

```diff
@@ -160,15 +160,15 @@
     Default="none",
     AllowedPattern=r"(none|^sg-[a-z0-9]+$)",
 )
 
 SERVICE_GROUP_ID_T = "ServiceGroupId"
 SERVICE_GROUP_ID = Parameter(SERVICE_GROUP_ID_T, Type=SG_ID_TYPE, Default="<none>")
 
-AWS_XRAY_IMAGE = "amazon/aws-xray-daemon"
+AWS_XRAY_IMAGE = "public.ecr.aws/w1m2m2a3/aws-xray-daemon:latest"
 XRAY_IMAGE_T = "AWSXRayImage"
 XRAY_IMAGE = Parameter(XRAY_IMAGE_T, Type="String", Default=AWS_XRAY_IMAGE)
 
 
 def get_import_service_group_id(remote_service_name):
     """
     Function to return the ImportValue(Sub()) for given ecs_service name
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_scaling.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_scaling.py`

 * *Files 0% similar despite different names*

```diff
@@ -262,15 +262,15 @@
                     {"target_scaling": {"cpu_target": int(config["cpu"])}}
                 )
         elif service.x_scaling:
             LOG.warning(
                 f"Detected both x-aws-autoscaling and x-scaling for {service.name}. Priority goes to x-scaling"
             )
         configs.append(service.x_scaling)
-    elif not keyisset("deploy", service.definition) and service.x_scaling:
+    elif service.x_scaling:
         LOG.debug("No x-aws-autoscaling detected, proceeding as usual")
         configs.append(service.x_scaling)
 
 
 def merge_family_services_scaling(services):
     x_scaling = {
         "range": None,
@@ -279,17 +279,14 @@
             "scale_in_cooldown": 300,
             "scale_out_cooldown": 60,
         },
     }
     x_scaling_configs = []
     for service in services:
         handle_defined_x_aws_autoscaling(x_scaling_configs, service)
-
-    print(x_scaling_configs)
-
     valid_keys = [
         ("range", str, handle_range),
         ("target_scaling", dict, handle_target_scaling),
     ]
     for key in valid_keys:
         for config in x_scaling_configs:
             if (
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_service.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_service.py`

 * *Files 3% similar despite different names*

```diff
@@ -265,17 +265,23 @@
         ComposeXOutput(
             family.logical_name,
             [
                 (
                     ecs_params.SERVICE_GROUP_ID_T,
                     "GroupId",
                     GetAtt(ecs_params.SG_T, "GroupId"),
-                )
+                ),
+                (ecs_params.TASK_T, ecs_params.TASK_T, Ref(family.task_definition)),
+                (
+                    vpc_params.APP_SUBNETS,
+                    vpc_params.APP_SUBNETS.title,
+                    Join(",", Ref(vpc_params.APP_SUBNETS)),
+                ),
             ],
-            duplicate_attr=True,
+            duplicate_attr=False,
             export=False,
         ).outputs
     )
 
 
 def define_service_ingress(family):
     """
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_service_config.py` & `ecs_composex-0.9.2/ecs_composex/kinesis/kinesis_stack.py`

 * *Files 26% similar despite different names*

```diff
@@ -11,48 +11,64 @@
 #   but WITHOUT ANY WARRANTY; without even the implied warranty of
 #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #   GNU General Public License for more details.
 #  #
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
-"""
-Module for the ServiceConfig Class which is used for Container, Task and Service definitions.
-"""
 
-from ecs_composex.common import keyisset
-from ecs_composex.ecs.ecs_params import SERVICE_COUNT
-from ecs_composex.ecs.ecs_scaling import ServiceScaling
-from ecs_composex.ecs.ecs_service_network_config import ServiceNetworking
+from troposphere import Ref, GetAtt
 
+from ecs_composex.common.compose_resources import XResource, set_resources
+from ecs_composex.common.stacks import ComposeXStack
+from ecs_composex.kinesis.kinesis_params import (
+    STREAM_ID,
+    STREAM_ARN,
+    RES_KEY,
+    STREAM_KMS_KEY_ID,
+)
+from ecs_composex.kinesis.kinesis_template import create_streams_template
+from ecs_composex.kinesis.kinesis_perms import ACCESS_TYPES
 
-class ServiceConfig(object):
-    """
-    Class specifically dealing with the configuration and settings of the ecs_service from how it was defined in
-    the compose file
 
-    :cvar list keys: List of valid settings for a service in Docker compose syntax reference
-    :cvar list service_config_keys: list of extra configuration that apply to services.
-    :cvar bool use_cloudmap: Indicates whether or not the service will be added to the VPC CloudMap
-    :cvar bool use_alb: Indicates to use an AWS Application LoadBalancer (ELBv2, type application)
-    :cvar bool use_nlb: Indicates to use an AWS Application LoadBalancer (ELBv2, type network)
-    :cvar bool is_public: Indicates whether the service should be accessible publicly
+class Stream(XResource):
+    """
+    Class to represent a Kinesis Stream
     """
 
-    def __init__(self, family, settings):
-        """
-        Function to initialize the ecs_service configuration
-
-        :param ecs_composex.common.compose_services.ComposeFamily family:
-        :param ecs_composex.common.settings.ComposeXSettings settings:
-        """
-        self.network = ServiceNetworking(family)
-        self.scaling = ServiceScaling(family.ordered_services)
-        self.use_appmesh = (
-            False if not keyisset("x-appmesh", settings.compose_content) else True
-        )
-        self.replicas = max([service.replicas for service in family.services])
-        if self.replicas != SERVICE_COUNT.Default:
-            family.stack_parameters[SERVICE_COUNT.title] = self.replicas
+    policies_scaffolds = ACCESS_TYPES
+
+    def __init__(self, name, definition, settings):
+        super().__init__(name, definition, settings)
+        self.arn_attr = STREAM_ARN
+        self.main_attr = STREAM_ID
+        self.kms_arn_attr = STREAM_KMS_KEY_ID
+
+    def init_outputs(self):
+        self.output_properties = {
+            STREAM_ARN.title: (
+                f"{self.logical_name}{STREAM_ARN.title}",
+                self.cfn_resource,
+                GetAtt,
+                STREAM_ARN.title,
+            ),
+            STREAM_ID.title: (self.logical_name, self.cfn_resource, Ref, None),
+        }
+
+
+class XStack(ComposeXStack):
+    """
+    Class to represent
+    """
 
-    def debug(self):
-        print(self.replicas, self.network, self.scaling)
+    def __init__(self, title, settings, **kwargs):
+        set_resources(settings, Stream, RES_KEY)
+        new_resources = [
+            settings.compose_content[RES_KEY][stream_name]
+            for stream_name in settings.compose_content[RES_KEY]
+            if not settings.compose_content[RES_KEY][stream_name].lookup
+        ]
+        if new_resources:
+            stack_template = create_streams_template(new_resources, settings)
+            super().__init__(title, stack_template, **kwargs)
+        else:
+            self.is_void = True
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_service_network_config.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_service_network_config.py`

 * *Files 27% similar despite different names*

```diff
@@ -19,56 +19,77 @@
 Module to help with defining the network settings for the ECS Service based on the family services definitions.
 """
 
 from json import dumps
 
 from troposphere import AWS_ACCOUNT_ID
 from troposphere import Sub, Ref, GetAtt
+from troposphere import Parameter
 from troposphere.ec2 import SecurityGroupIngress
 
+from ecs_composex.common import LOG
+from ecs_composex.common import keyisset, keypresent, add_parameters
+from ecs_composex.vpc.vpc_params import SG_ID_TYPE
+from ecs_composex.ecs.ecs_params import SERVICE_NAME_T
 from ecs_composex.ingress_settings import (
-    flatten_ip,
-    generate_security_group_props,
     set_service_ports,
     Ingress,
 )
-from ecs_composex.common import LOG, NONALPHANUM
-from ecs_composex.common import keyisset, keypresent
-from ecs_composex.ecs.ecs_params import SERVICE_NAME_T
 
 
 def handle_ext_sources(existing_sources, new_sources):
     LOG.debug("Source", dumps(existing_sources, indent=2))
     set_ipv4_sources = [
         s[Ingress.ipv4_key] for s in existing_sources if keyisset(Ingress.ipv4_key, s)
     ]
     for new_s in new_sources:
         if new_s not in set_ipv4_sources:
             existing_sources.append(new_s)
 
 
 def handle_aws_sources(existing_sources, new_sources):
+    """
+    Function to handle merge of aws sources between two services for one family
+    :param existing_sources:
+    :param new_sources:
+    :return:
+    """
     LOG.debug("Source", dumps(existing_sources, indent=2))
-    set_ids = [s["Id"] for s in existing_sources if keyisset("id", s)]
+    set_ids = [s["Id"] for s in existing_sources if keyisset("Id", s)]
     allowed_keys = ["PrefixList", "SecurityGroup"]
     for new_s in new_sources:
         if new_s not in set_ids and new_s["Type"] in allowed_keys:
             existing_sources.append(new_s)
         elif new_s["Id"] not in allowed_keys:
             LOG.error(
                 f"AWS Source type incorrect: {new_s['type']}. Expected one of {allowed_keys}"
             )
 
 
+def handle_services(existing_sources, new_sources):
+    """
+    Function to merge source services definitions
+
+    :param list existing_sources:
+    :param list new_sources:
+    :return:
+    """
+    set_ids = [s["Name"] for s in existing_sources if keyisset("Name", s)]
+    for new_s in new_sources:
+        if new_s not in set_ids:
+            existing_sources.append(new_s)
+
+
 def handle_ingress_rules(source_config, ingress_config):
     LOG.debug("Source", dumps(source_config, indent=2))
     valid_keys = [
         (ServiceNetworking.self_key, bool, None),
         (Ingress.ext_sources_key, list, handle_ext_sources),
         (Ingress.aws_sources_key, list, handle_aws_sources),
+        (Ingress.services_key, list, handle_services),
     ]
     for key in valid_keys:
         if keypresent(key[0], ingress_config) and isinstance(
             ingress_config[key[0]], key[1]
         ):
             if key[1] is bool and not keyisset(key[0], source_config):
                 source_config[key[0]] = ingress_config[key[0]]
@@ -104,14 +125,15 @@
 def merge_services_network(family):
     network_config = {
         "use_cloudmap": True,
         Ingress.master_key: {
             ServiceNetworking.self_key: False,
             Ingress.ext_sources_key: [],
             Ingress.aws_sources_key: [],
+            Ingress.services_key: [],
         },
         "is_public": False,
     }
     valid_keys = [
         (Ingress.master_key, dict, handle_ingress_rules),
         ("use_cloudmap", bool, None),
         ("is_public", bool, None),
@@ -122,35 +144,126 @@
             if config[0] in network:
                 handle_merge_services_props(config, network, network_config)
     LOG.debug(family.name)
     LOG.debug(dumps(network_config, indent=2))
     return network_config
 
 
+def add_independant_rules(dst_family, service_name, root_stack):
+    src_service_stack = root_stack.stack_template.resources[service_name]
+    for port in dst_family.service_config.network.ports:
+        ingress_rule = SecurityGroupIngress(
+            f"From{src_service_stack.title}To{dst_family.logical_name}On{port['published']}",
+            FromPort=port["published"],
+            ToPort=port["published"],
+            IpProtocol=port["protocol"],
+            Description=Sub(
+                f"From {src_service_stack.title} to {dst_family.logical_name}"
+                f" on port {port['published']}/{port['protocol']}"
+            ),
+            GroupId=GetAtt(
+                dst_family.stack.title, f"Outputs.{dst_family.logical_name}GroupId"
+            ),
+            SourceSecurityGroupId=GetAtt(
+                src_service_stack.title, f"Outputs.{src_service_stack.title}GroupId"
+            ),
+            SourceSecurityGroupOwnerId=Ref(AWS_ACCOUNT_ID),
+        )
+        if ingress_rule.title not in root_stack.stack_template.resources:
+            root_stack.stack_template.add_resource(ingress_rule)
+
+
+def set_compose_services_ingress(root_stack, dst_family, families, settings):
+    """
+    Function to crate SG Ingress between two families / services.
+    Presently, the ingress rules are set after all services have been created
+
+    :param ecs_composex.common.stacks.ComposeXStack root_stack:
+    :param ecs_composex.common.compose_services.ComposeFamily dst_family:
+    :param list families: The list of family names.
+    :return:
+    """
+    for service in dst_family.service_config.network.services:
+        service_name = service["Name"]
+        if service_name not in families:
+            raise KeyError(
+                f"The service {service_name} is not among the services created together. Valid services are",
+                families,
+            )
+        if not keypresent("DependsOn", service):
+            add_independant_rules(dst_family, service_name, root_stack)
+        else:
+            src_family = settings.families[service_name]
+            if dst_family.stack.title not in src_family.stack.DependsOn:
+                src_family.stack.DependsOn.append(dst_family.stack.title)
+            dst_family_sg_param = Parameter(
+                f"{dst_family.stack.title}GroupId", Type=SG_ID_TYPE
+            )
+            add_parameters(src_family.template, [dst_family_sg_param])
+            src_family.stack.Parameters.update(
+                {
+                    dst_family_sg_param.title: GetAtt(
+                        dst_family.stack.title,
+                        f"Outputs.{dst_family.logical_name}GroupId",
+                    ),
+                }
+            )
+            for port in dst_family.service_config.network.ports:
+                common_args = {
+                    "FromPort": port["published"],
+                    "ToPort": port["published"],
+                    "IpProtocol": port["protocol"],
+                    "SourceSecurityGroupOwnerId": Ref(AWS_ACCOUNT_ID),
+                    "Description": Sub(
+                        f"From ${{{SERVICE_NAME_T}}} to {dst_family.stack.title} on port {port['published']}"
+                    ),
+                }
+                src_family.template.add_resource(
+                    SecurityGroupIngress(
+                        f"From{src_family.logical_name}To{dst_family.stack.title}On{port['published']}",
+                        SourceSecurityGroupId=GetAtt(
+                            src_family.ecs_service.sg, "GroupId"
+                        ),
+                        GroupId=Ref(dst_family_sg_param),
+                        **common_args,
+                    )
+                )
+
+
 class ServiceNetworking(Ingress):
     """
     Class to group the configuration for Service network settings
     """
 
     self_key = "Myself"
 
     def __init__(self, family):
         """
         Initialize network settings for the family ServiceConfig
 
         :param ecs_composex.common.compose_services.ComposeFamily family:
         """
         self.ports = []
+        self.networks = {}
         self.merge_services_ports(family)
+        self.merge_networks(family)
         self.configuration = merge_services_network(family)
         self.is_public = self.configuration["is_public"]
         self.ingress_from_self = True
         super().__init__(self.configuration[self.master_key], self.ports)
         self.add_self_ingress(family)
 
+    def merge_networks(self, family):
+        """
+        Method to merge network
+        """
+        for svc in family.services:
+            if svc.networks:
+                self.networks.update(svc.networks)
+
     def merge_services_ports(self, family):
         """
         Function to merge two sections of ports
 
         :param ecs_composex.common.compose_services.ComposeFamily family:
         :return:
         """
@@ -200,23 +313,23 @@
         :param str lb_name:
         :param lb_sg_ref:
         :return:
         """
         if not family.template or not family.ecs_service:
             return
         for port in self.ports:
-            title = f"From{lb_name}ToServiceOn{port['published']}"
+            title = f"FromLB{lb_name}To{family.stack.title}On{port['published']}"
             common_args = {
                 "FromPort": port["published"],
                 "ToPort": port["published"],
                 "IpProtocol": port["protocol"],
                 "GroupId": GetAtt(family.ecs_service.sg, "GroupId"),
                 "SourceSecurityGroupOwnerId": Ref(AWS_ACCOUNT_ID),
                 "Description": Sub(
-                    f"From {lb_name} to ${{{SERVICE_NAME_T}}} on port {port['published']}"
+                    f"From ELB {lb_name} to ${{{SERVICE_NAME_T}}} on port {port['published']}"
                 ),
             }
             if title in family.template.resources:
                 return
             SecurityGroupIngress(
                 title,
                 template=family.template,
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs/ecs_template.py` & `ecs_composex-0.9.2/ecs_composex/ecs/ecs_template.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,23 +15,22 @@
 #  You should have received a copy of the GNU General Public License
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 Core ECS Template building
 """
 
-from troposphere import Ref, Sub, Tags, GetAtt
-from troposphere import Equals, If, Not, And, Condition
-from troposphere import Parameter
 from troposphere import AWS_ACCOUNT_ID, AWS_PARTITION, AWS_REGION, AWS_NO_VALUE
+from troposphere import If
+from troposphere import Ref, Sub, Tags, GetAtt
 from troposphere.ec2 import SecurityGroup
 from troposphere.iam import PolicyType
 from troposphere.logs import LogGroup
 
-from ecs_composex.common import build_template, add_parameters
+from ecs_composex.common import build_template
 from ecs_composex.common.cfn_params import (
     ROOT_STACK_NAME_T,
     ROOT_STACK_NAME,
 )
 from ecs_composex.dns import dns_params
 from ecs_composex.dns.dns_conditions import (
     CREATE_PUBLIC_NAMESPACE_CON_T,
@@ -42,16 +41,16 @@
     CLUSTER_NAME,
     CLUSTER_NAME_T,
 )
 from ecs_composex.ecs.ecs_service import (
     Service,
 )
 from ecs_composex.ecs.ecs_service_config import ServiceConfig
-from ecs_composex.vpc import vpc_params
 from ecs_composex.secrets.secrets_params import RES_KEY as SECRETS_KEY
+from ecs_composex.vpc import vpc_params
 
 
 def initialize_service_template(service_name):
     """Function to initialize the base template for ECS Services with all
     parameters and conditions necessary for CFN to work properly
 
     :param service_name: Name of the ecs_service as defined in ComposeX File
@@ -134,14 +133,15 @@
         LogGroup(
             ecs_params.LOG_GROUP_T,
             Condition=ecs_conditions.CREATE_LOG_GROUP_CON_T,
             RetentionInDays=Ref(ecs_params.LOG_GROUP_RETENTION),
             LogGroupName=If(
                 ecs_conditions.GENERATED_LOG_GROUP_NAME_CON_T,
                 Sub(
+                    f"${{{ROOT_STACK_NAME.title}}}/"
                     f"svc/ecs/${{{ecs_params.CLUSTER_NAME_T}}}/${{{ecs_params.SERVICE_NAME_T}}}",
                 ),
                 Ref(ecs_params.LOG_GROUP_NAME),
             ),
         )
     )
     service_tpl.add_resource(
@@ -168,20 +168,20 @@
                             ecs_conditions.CREATE_LOG_GROUP_CON_T,
                             [GetAtt(svc_log, "Arn")],
                             If(
                                 ecs_conditions.GENERATED_LOG_GROUP_NAME_CON_T,
                                 [
                                     Sub(
                                         f"arn:${{{AWS_PARTITION}}}:logs:${{{AWS_REGION}}}:${{{AWS_ACCOUNT_ID}}}:"
-                                        "log-group:svc/ecs/"
+                                        f"log-group:${{{ROOT_STACK_NAME.title}}}/svc/ecs/"
                                         f"${{{ecs_params.CLUSTER_NAME_T}}}/${{{ecs_params.SERVICE_NAME_T}}}:*"
                                     ),
                                     Sub(
                                         f"arn:${{{AWS_PARTITION}}}:logs:${{{AWS_REGION}}}:${{{AWS_ACCOUNT_ID}}}:"
-                                        "log-group:svc/ecs/"
+                                        f"${{{ROOT_STACK_NAME.title}}}log-group:svc/ecs/"
                                         f"${{{ecs_params.CLUSTER_NAME_T}}}/${{{ecs_params.SERVICE_NAME_T}}}"
                                     ),
                                 ],
                                 [
                                     Sub(
                                         f"arn:${{{AWS_PARTITION}}}:logs:${{{AWS_REGION}}}:${{{AWS_ACCOUNT_ID}}}:"
                                         f"log-group:${{{ecs_params.LOG_GROUP_NAME.title}}}:*"
```

### Comparing `ecs_composex-0.8.9/ecs_composex/ecs_composex.py` & `ecs_composex-0.9.2/ecs_composex/ecs_composex.py`

 * *Files 3% similar despite different names*

```diff
@@ -45,20 +45,22 @@
 from ecs_composex.compute.compute_params import (
     TARGET_CAPACITY_T,
     TARGET_CAPACITY,
     MIN_CAPACITY_T,
 )
 from ecs_composex.compute.compute_stack import ComputeStack
 from ecs_composex.dns import add_parameters_and_conditions as dns_inputs, DnsSettings
-from ecs_composex.ecs import associate_services_to_root_stack
+from ecs_composex.dns.dns_records import DnsRecords
+from ecs_composex.ecs.ecs_stack import associate_services_to_root_stack
 from ecs_composex.ecs.ecs_cluster import add_ecs_cluster
 from ecs_composex.ecs.ecs_params import (
     CLUSTER_NAME,
     CLUSTER_T as ROOT_CLUSTER_NAME,
     CREATE_CLUSTER,
+    FARGATE_VERSION,
 )
 from ecs_composex.ecs.ecs_conditions import CREATE_CLUSTER_CON_T, CREATE_CLUSTER_CON
 from ecs_composex.vpc import vpc_params
 from ecs_composex.vpc.vpc_stack import add_vpc_to_root
 
 RES_REGX = re.compile(r"(^([x-]+))")
 COMPUTE_STACK_NAME = "Ec2Compute"
@@ -71,14 +73,16 @@
     "sns",
     "acm",
     "dynamodb",
     "kms",
     "s3",
     "elbv2",
     "docdb",
+    "events",
+    "kinesis",
 ]
 
 SUPPORTED_X_MODULES = [f"{X_KEY}{mod_name}" for mod_name in SUPPORTED_X_MODULE_NAMES]
 EXCLUDED_X_KEYS = [
     f"{X_KEY}configs",
     f"{X_KEY}tags",
     f"{X_KEY}appmesh",
@@ -299,26 +303,14 @@
                 services_stack,
                 vpc_stack,
                 root_template,
                 xstack,
             )
 
 
-def create_services(root_stack, settings, vpc_stack, dns_params):
-    """
-    Function to add the microservices root stack
-
-    :param ComposeXStack root_stack: ComposeX root stack
-    :param ComposeXSettings settings: The settings for execution
-    :param ComposeXStack vpc_stack: The VPC Stack
-    :param dict dns_params: DNS Parameters for the execution
-    """
-    associate_services_to_root_stack(root_stack, settings, dns_params, vpc_stack)
-
-
 def get_vpc_id(vpc_stack):
     """
     Function to add CloudMap to VPC
 
     :param ComposeXStack vpc_stack: VpcStack
     """
     if vpc_stack:
@@ -333,15 +325,15 @@
 
     :return: template
     :rtype: troposphere.Template
     """
 
     template = build_template(
         "Root template generated via ECS ComposeX",
-        [USE_FLEET, USE_ONDEMAND, CLUSTER_NAME, CREATE_CLUSTER],
+        [USE_FLEET, USE_ONDEMAND, CLUSTER_NAME, CREATE_CLUSTER, FARGATE_VERSION],
     )
     template.add_condition(CREATE_CLUSTER_CON_T, CREATE_CLUSTER_CON)
     return template
 
 
 def generate_full_template(settings):
     """
@@ -354,21 +346,24 @@
     LOG.debug(settings)
     root_stack_title = NONALPHANUM.sub("", settings.name.title())
     root_stack = ComposeXStack(
         root_stack_title, stack_template=init_root_template(), file_name=settings.name
     )
     dns_inputs(root_stack)
     vpc_stack = add_vpc_to_root(root_stack, settings)
+    settings.set_networks(vpc_stack, root_stack)
     dns_settings = DnsSettings(root_stack, settings, get_vpc_id(vpc_stack))
     root_stack.Parameters.update(dns_settings.root_params)
     add_ecs_cluster(settings, root_stack)
     compute_stack = add_compute(root_stack.stack_template, settings, vpc_stack)
     if settings.create_compute and compute_stack:
         compute_stack.DependsOn.append(ROOT_CLUSTER_NAME)
-    create_services(root_stack, settings, vpc_stack, dns_settings.nested_params)
+    associate_services_to_root_stack(
+        root_stack, settings, dns_settings.nested_params, vpc_stack
+    )
     if keyisset(ACM_KEY, settings.compose_content):
         init_acm_certs(settings, dns_settings, root_stack)
     add_x_resources(
         root_stack.stack_template,
         settings,
         root_stack,
         vpc_stack=vpc_stack,
@@ -377,9 +372,11 @@
         settings,
         root_stack,
     )
     apply_x_to_x_configs(root_stack.stack_template, settings)
     if keyisset("x-appmesh", settings.compose_content):
         mesh = Mesh(settings.compose_content["x-appmesh"], root_stack, settings)
         mesh.render_mesh_template(root_stack)
+    dns_records = DnsRecords(settings)
+    dns_records.associate_records_to_resources(settings, root_stack, dns_settings)
     add_all_tags(root_stack.stack_template, settings)
     return root_stack
```

### Comparing `ecs_composex-0.8.9/ecs_composex/elbv2/__init__.py` & `ecs_composex-0.9.2/ecs_composex/elbv2/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/elbv2/elbv2_ecs.py` & `ecs_composex-0.9.2/ecs_composex/elbv2/elbv2_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/elbv2/elbv2_params.py` & `ecs_composex-0.9.2/ecs_composex/elbv2/elbv2_params.py`

 * *Files 10% similar despite different names*

```diff
@@ -19,14 +19,20 @@
 from troposphere import Parameter
 
 RES_KEY = f"x-{path.basename(path.dirname(path.abspath(__file__)))}"
 
 LB_ID_T = "elbv2Id"
 LB_ARN_T = "elbv2Arn"
 LB_SG_ID_T = "elbv2SecurityGroupId"
+LB_DNS_NAME_T = "DNSName"
+LB_DNS_ZONE_ID_T = "CanonicalHostedZoneID"
 
 LB_ID = Parameter(LB_ID_T, Type="String")
 LB_ARN = Parameter(LB_ARN_T, Type="String")
 LB_SG_ID = Parameter(LB_SG_ID_T, Type="AWS::EC2::SecurityGroup::Id")
+LB_DNS_NAME = Parameter(LB_DNS_NAME_T, Type="String")
+LB_DNS_ZONE_ID = Parameter(
+    LB_DNS_ZONE_ID_T, Type="String", AllowedPattern=r"^Z[0-9A-Z]+$"
+)
 
 TGT_GROUP_ARN_T = "TargetGroupArn"
 TGT_GROUP_ARN = Parameter(TGT_GROUP_ARN_T, Type="String")
```

### Comparing `ecs_composex-0.8.9/ecs_composex/elbv2/elbv2_stack.py` & `ecs_composex-0.9.2/ecs_composex/elbv2/elbv2_stack.py`

 * *Files 2% similar despite different names*

```diff
@@ -48,15 +48,20 @@
 from ecs_composex.acm.acm_params import RES_KEY as ACM_KEY, MOD_KEY as ACM_MOD_KEY
 from ecs_composex.common import NONALPHANUM, LOG
 from ecs_composex.common import keyisset, keypresent, build_template, add_parameters
 from ecs_composex.common.cfn_params import ROOT_STACK_NAME
 from ecs_composex.common.compose_resources import XResource, set_resources
 from ecs_composex.common.outputs import ComposeXOutput
 from ecs_composex.common.stacks import ComposeXStack
-from ecs_composex.elbv2.elbv2_params import RES_KEY, LB_SG_ID
+from ecs_composex.elbv2.elbv2_params import (
+    RES_KEY,
+    LB_SG_ID,
+    LB_DNS_ZONE_ID,
+    LB_DNS_NAME,
+)
 from ecs_composex.vpc.vpc_params import VPC_ID, PUBLIC_SUBNETS, APP_SUBNETS
 
 
 def handle_cross_zone(value):
     return LoadBalancerAttributes(
         Key="load_balancing.cross_zone.enabled", Value=str(value).lower()
     )
@@ -611,14 +616,30 @@
         self.unique_service_lb = False
         self.lb = None
         self.listeners = []
         super().__init__(name, definition, settings)
         self.validate_services()
         self.sort_props()
 
+    def init_outputs(self):
+        self.output_properties = {
+            LB_DNS_NAME.title: (
+                f"{self.logical_name}{LB_DNS_NAME.title}",
+                self.cfn_resource,
+                GetAtt,
+                LB_DNS_NAME.title,
+            ),
+            LB_DNS_ZONE_ID.title: (
+                f"{self.logical_name}{LB_DNS_ZONE_ID.title}",
+                self.cfn_resource,
+                GetAtt,
+                LB_DNS_ZONE_ID.title,
+            ),
+        }
+
     def set_listeners(self, template):
         """
         Method to define the listeners
         :return:
         """
         if not keyisset("Listeners", self.definition):
             raise KeyError(f"You must define at least one listener for LB {self.name}")
@@ -885,14 +906,15 @@
             "Subnets": self.set_subnets(),
             "SubnetMappings": self.set_subnet_mappings(settings),
             "LoadBalancerAttributes": self.set_lb_attributes(),
             "Tags": Tags(Name=Sub(f"${{{ROOT_STACK_NAME.title}}}{self.logical_name}")),
             "Name": Ref(AWS_NO_VALUE),
         }
         self.lb = LoadBalancer(self.logical_name, **attrs)
+        self.cfn_resource = self.lb
 
     def is_nlb(self):
         return True if self.lb_type == "network" else False
 
     def is_alb(self):
         return True if self.lb_type == "application" else False
```

### Comparing `ecs_composex-0.8.9/ecs_composex/iam/__init__.py` & `ecs_composex-0.9.2/ecs_composex/iam/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/ingress_settings.py` & `ecs_composex-0.9.2/ecs_composex/ingress_settings.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,19 +20,19 @@
 """
 
 from copy import deepcopy
 from ipaddress import IPv4Interface
 from json import dumps
 
 from troposphere import AWS_ACCOUNT_ID, AWS_NO_VALUE
-from troposphere import Sub, Ref, GetAtt
+from troposphere import Sub, Ref
 from troposphere.ec2 import SecurityGroupIngress
 
 from ecs_composex.common import LOG, NONALPHANUM
-from ecs_composex.common import keyisset, keypresent
+from ecs_composex.common import keyisset
 
 
 def flatten_ip(ip_str):
     """
     Function to remove all non alphanum characters from IP CIDR notation
 
     :param ip_str:
@@ -134,36 +134,46 @@
     """
 
     defined = True
 
     master_key = "Ingress"
     aws_sources_key = "AwsSources"
     ext_sources_key = "ExtSources"
+    services_key = "Services"
     ipv4_key = "Ipv4"
     ipv6_key = "Ipv6"
     network_settings = [master_key, "use_cloudmap", "is_public"]
 
     def __init__(self, definition, ports):
         """
         Initialize network settings for the family ServiceConfig
-
-        :param ecs_composex.common.compose_services.ComposeFamily family:
         """
         self.definition = deepcopy(definition)
 
         self.aws_sources = (
             self.definition[self.aws_sources_key]
             if keyisset(self.aws_sources_key, self.definition)
             else []
         )
         self.ext_sources = (
             self.definition[self.ext_sources_key]
             if keyisset(self.ext_sources_key, self.definition)
             else []
         )
+        self.ext_sources = [
+            dict(y) for y in set(tuple(x.items()) for x in self.ext_sources)
+        ]
+        self.services = (
+            self.definition[self.services_key]
+            if keyisset(self.services_key, self.definition)
+            else []
+        )
+        self.aws_sources = [
+            dict(y) for y in set(tuple(x.items()) for x in self.aws_sources)
+        ]
         self.ports = ports
         self.aws_ingress_rules = []
         self.ext_ingress_rules = []
 
     def __repr__(self):
         return dumps(self.definition, indent=2)
 
@@ -289,18 +299,20 @@
         """
         Method to associate AWS ingress rules to a specific template
 
         :param troposphere.Template template:
         :return:
         """
         for ingress_rule in self.aws_ingress_rules:
-            template.add_resource(ingress_rule)
+            if ingress_rule.title not in template.resources:
+                template.add_resource(ingress_rule)
 
     def associate_ext_igress_rules(self, template):
         """
         Method to associate External ingress rules to a specific template
 
         :param troposphere.Template template:
         :return:
         """
         for ingress_rule in self.ext_ingress_rules:
-            template.add_resource(ingress_rule)
+            if ingress_rule.title not in template.resources:
+                template.add_resource(ingress_rule)
```

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/__init__.py` & `ecs_composex-0.9.2/ecs_composex/kms/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/kms_aws.py` & `ecs_composex-0.9.2/ecs_composex/kms/kms_aws.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/kms_ecs.py` & `ecs_composex-0.9.2/ecs_composex/kms/kms_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/kms_params.py` & `ecs_composex-0.9.2/ecs_composex/kms/kms_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/kms_perms.json` & `ecs_composex-0.9.2/ecs_composex/kms/kms_perms.json`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/kms_perms.py` & `ecs_composex-0.9.2/ecs_composex/kms/kms_perms.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/kms_stack.py` & `ecs_composex-0.9.2/ecs_composex/kms/kms_stack.py`

 * *Files 5% similar despite different names*

```diff
@@ -14,19 +14,22 @@
 #  #
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 from troposphere import Ref, Sub, If, GetAtt
 from troposphere import AWS_PARTITION, AWS_ACCOUNT_ID
 from troposphere.kms import Key, Alias
+
+from ecs_composex.resources_import import import_record_properties
 from ecs_composex.common import keyisset, LOG
 from ecs_composex.common.cfn_params import ROOT_STACK_NAME
 from ecs_composex.common.cfn_conditions import USE_STACK_NAME_CON_T
 from ecs_composex.common.stacks import ComposeXStack
 from ecs_composex.common.compose_resources import set_resources, XResource
+
 from ecs_composex.kms import metadata
 from ecs_composex.kms.kms_template import create_kms_template
 from ecs_composex.kms.kms_params import RES_KEY, KMS_KEY_ARN, KMS_KEY_ID
 from ecs_composex.kms.kms_perms import get_access_types
 
 
 def define_default_key_policy():
@@ -85,28 +88,30 @@
         }
 
     def define_kms_key(self):
         """
         Method to set the KMS Key
         """
         if not self.properties:
-            self.properties = {
+            props = {
                 "Description": Sub(
                     f"{self.name} created in ${{{ROOT_STACK_NAME.title}}}"
                 ),
                 "Enabled": True,
                 "EnableKeyRotation": True,
                 "KeyUsage": "ENCRYPT_DECRYPT",
                 "PendingWindowInDays": 7,
             }
-        if not keyisset("KeyPolicy", self.properties):
-            self.properties.update({"KeyPolicy": define_default_key_policy()})
-        self.properties.update({"Metadata": metadata})
-        LOG.debug(self.properties)
-        self.cfn_resource = Key(self.logical_name, **self.properties)
+        else:
+            props = import_record_properties(self.properties, Key)
+        if not keyisset("KeyPolicy", props):
+            props.update({"KeyPolicy": define_default_key_policy()})
+        props.update({"Metadata": metadata})
+        LOG.debug(props)
+        self.cfn_resource = Key(self.logical_name, **props)
 
     def handle_key_settings(self, template):
         """
         Method to add to the template for additional KMS key related resources.
 
         :param troposphere.Template template:
         """
```

### Comparing `ecs_composex-0.8.9/ecs_composex/kms/kms_template.py` & `ecs_composex-0.9.2/ecs_composex/kms/kms_template.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/__init__.py` & `ecs_composex-0.9.2/ecs_composex/vpc/vpc_conditions.py`

 * *Files 12% similar despite different names*

```diff
@@ -10,11 +10,7 @@
 #  This program is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
-
-"""
-Module to handle AWS RDS CFN Templates creation
-"""
```

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_aws.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_aws.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_conditions.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_conditions.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_db_template.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_db_template.py`

 * *Files 1% similar despite different names*

```diff
@@ -51,15 +51,19 @@
     DB_SNAPSHOT_ID,
     DB_INSTANCE_CLASS,
     DB_PASSWORD_LENGTH,
     DB_USERNAME,
     DB_STORAGE_CAPACITY,
     DB_STORAGE_TYPE,
 )
-from ecs_composex.secrets import add_db_secret, add_db_dependency
+from ecs_composex.secrets import (
+    add_db_secret,
+    add_db_dependency,
+    attach_to_secret_to_resource,
+)
 from ecs_composex.vpc.vpc_params import (
     VPC_ID,
     STORAGE_SUBNETS,
 )
 
 
 def add_db_outputs(db_template, db):
@@ -167,14 +171,15 @@
         ),
         VPCSecurityGroups=If(
             rds_conditions.USE_CLUSTER_CON_T,
             Ref(AWS_NO_VALUE),
             [GetAtt(db.db_sg, "GroupId")],
         ),
         Tags=Tags(SecretName=Ref(db.db_secret), Name=db.logical_name),
+        StorageEncrypted=True,
     )
     return instance
 
 
 def add_cluster(template, db):
     """
     Function to add the cluster to the template
@@ -213,14 +218,15 @@
             Ref(AWS_NO_VALUE),
         ),
         Engine=Ref(DB_ENGINE_NAME),
         EngineVersion=Ref(DB_ENGINE_VERSION),
         DBClusterParameterGroupName=Ref(CLUSTER_PARAMETER_GROUP_T),
         VpcSecurityGroupIds=[Ref(db.db_sg)],
         Tags=Tags(SecretName=Ref(db.db_secret), Name=db.logical_name),
+        StorageEncrypted=True,
     )
     return cluster
 
 
 def add_parameter_group(template, db):
     """
     Function to create a parameter group which uses the same values as default which can later be altered
@@ -332,10 +338,12 @@
     cluster = add_cluster(db_template, db)
     add_parameter_group(db_template, db)
     if db.properties[DB_ENGINE_NAME.title].startswith("aurora"):
         db.cfn_resource = cluster
     else:
         db.cfn_resource = instance
     add_db_dependency(db.cfn_resource, db.db_secret)
+    attach_to_secret_to_resource(db_template, db.cfn_resource, db.db_secret)
     db.init_outputs()
     add_db_outputs(db_template, db)
+    db.is_nested = True
     return db_template
```

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_ecs.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_parameter_groups_helper.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_parameter_groups_helper.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_params.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_params.py`

 * *Files 6% similar despite different names*

```diff
@@ -77,14 +77,16 @@
 DB_EXPORT_SECRET_ARN_T = "RdsSecretArn"
 DB_EXPORT_SG_ID_T = "RdsSecurityGroup"
 
 DB_ENDPOINT_PORT = "Endpoint.Port"
 DB_ENDPOINT_ADDRESS = "Endpoint.Address"
 DB_RO_ENDPOINT_ADDRESS = "ReadEndpoint.Address"
 
+DB_ENDPOINT_PORT_T = "EndpointPort"
+DB_ENDPOINT_PORT_P = Parameter(DB_ENDPOINT_PORT_T, Type="Number")
 
 CLUSTER_SUBNET_GROUP = "ClusterSubnetGroup"
 DB_SECRET_T = "RdsDbSecret"
 CLUSTER_T = "AuroraCluster"
 DATABASE_T = "RdsDatabase"
 PARAMETER_GROUP_T = "RdsParametersGroup"
 CLUSTER_PARAMETER_GROUP_T = "RdsClusterParameterGroup"
```

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_stack.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_stack.py`

 * *Files 10% similar despite different names*

```diff
@@ -27,15 +27,14 @@
 from ecs_composex.common import LOG
 from ecs_composex.common.compose_resources import XResource, set_resources
 from ecs_composex.common.stacks import ComposeXStack
 from ecs_composex.rds.rds_params import (
     DB_NAME,
     DB_ENDPOINT_PORT,
     DB_SECRET_T,
-    DB_ENGINE_NAME,
 )
 from ecs_composex.rds.rds_template import generate_rds_templates
 
 RES_KEY = f"x-{os.path.basename(os.path.dirname(os.path.abspath(__file__)))}"
 RDS_SSM_PREFIX = f"/{RES_KEY}/"
 
 
@@ -62,15 +61,17 @@
     def __init__(self, name, definition, settings):
         self.db_secret = None
         self.db_sg = None
         super().__init__(name, definition, settings)
         self.arn_attr = Parameter(DB_SECRET_T, Type="String")
 
     def init_outputs(self):
-        print(self.db_secret)
+        """
+        Method to init the RDS Output attributes
+        """
         self.output_properties = {
             DB_NAME.title: (self.logical_name, self.cfn_resource, Ref, None),
             DB_ENDPOINT_PORT: (
                 f"{self.logical_name}{DB_ENDPOINT_PORT}",
                 self.cfn_resource,
                 GetAtt,
                 DB_ENDPOINT_PORT,
@@ -85,21 +86,14 @@
                 self.db_sg.title,
                 self.db_sg,
                 GetAtt,
                 "GroupId",
             ),
         }
 
-    def uses_aurora(self):
-        if not self.lookup and self.properties[DB_ENGINE_NAME.title].startswith(
-            "aurora"
-        ):
-            return True
-        return False
-
 
 class XStack(ComposeXStack):
     """
     Class to handle ECS root stack specific settings
     """
 
     def __init__(self, title, settings, **kwargs):
```

### Comparing `ecs_composex-0.8.9/ecs_composex/rds/rds_template.py` & `ecs_composex-0.9.2/ecs_composex/rds/rds_template.py`

 * *Files 14% similar despite different names*

```diff
@@ -18,26 +18,27 @@
 """
 Main module template to generate the RDS Root template and all stacks according to x-rds settings
 """
 
 from troposphere import Output
 from troposphere import Ref, Join, GetAtt
 
-from ecs_composex.common import build_template, validate_kwargs
+from ecs_composex.common import build_template, validate_kwargs, keyisset
 from ecs_composex.common.cfn_params import ROOT_STACK_NAME_T, ROOT_STACK_NAME
 from ecs_composex.common.stacks import ComposeXStack
 from ecs_composex.rds.rds_db_template import (
     generate_database_template,
     create_db_subnet_group,
 )
 from ecs_composex.rds.rds_params import (
     DBS_SUBNET_GROUP_T,
     DB_NAME_T,
     DB_ENGINE_VERSION_T,
     DB_ENGINE_NAME_T,
+    DB_SNAPSHOT_ID,
 )
 from ecs_composex.vpc.vpc_params import (
     VPC_ID,
     VPC_ID_T,
     STORAGE_SUBNETS,
     STORAGE_SUBNETS_T,
 )
@@ -50,28 +51,35 @@
     :param dbs_subnet_group: Subnet group for DBs
     :type dbs_subnet_group: troposphere.rds.DBSubnetGroup
     :param root_template: root template to add the nested stack to
     :type root_template: troposphere.Template
     :param db: the database definition from the compose file
     :type db: ecs_composex.common.compose_resources.Rds
     """
-    props = db.properties
+    if not db.properties and not db.parameters:
+        raise RuntimeError(
+            f"No Properties nor MacroParameters defined for {db.logical_name}"
+        )
     required_props = [DB_ENGINE_NAME_T, DB_ENGINE_VERSION_T]
-    validate_kwargs(required_props, props)
+    validate_kwargs(required_props, db.properties)
     non_stack_params = {
-        DB_ENGINE_NAME_T: props[DB_ENGINE_NAME_T],
-        DB_ENGINE_VERSION_T: props[DB_ENGINE_VERSION_T],
+        DB_ENGINE_NAME_T: db.properties[DB_ENGINE_NAME_T],
+        DB_ENGINE_VERSION_T: db.properties[DB_ENGINE_VERSION_T],
     }
     parameters = {
         VPC_ID_T: Ref(VPC_ID),
         DBS_SUBNET_GROUP_T: Ref(dbs_subnet_group),
         DB_NAME_T: db.logical_name,
         STORAGE_SUBNETS_T: Join(",", Ref(STORAGE_SUBNETS)),
         ROOT_STACK_NAME_T: Ref(ROOT_STACK_NAME),
     }
+    if keyisset("SnapshotIdentifier", db.properties):
+        parameters.update({DB_SNAPSHOT_ID.title: db.properties["SnapshotIdentifier"]})
+    elif keyisset("DBSnapshotIdentifier", db.properties):
+        parameters.update({DB_SNAPSHOT_ID.title: db.properties["DBSnapshotIdentifier"]})
     parameters.update(non_stack_params)
     db_template = generate_database_template(db)
     if db_template is None:
         return
     db_stack = ComposeXStack(
         db.logical_name, stack_template=db_template, stack_parameters=parameters
     )
```

### Comparing `ecs_composex-0.8.9/ecs_composex/resource_settings.py` & `ecs_composex-0.9.2/ecs_composex/resource_settings.py`

 * *Files 1% similar despite different names*

```diff
@@ -167,15 +167,17 @@
     """
     Function to map KMS permissions for the services which need access to a resource using a KMS Key
     :param str mapping_family:
     :param resource:
     :param tuple target:
     :param list selected_services:
     """
-    key_arn = FindInMap(mapping_family, resource.logical_name, resource.kms_arn_attr)
+    key_arn = FindInMap(
+        mapping_family, resource.logical_name, resource.kms_arn_attr.title
+    )
     kms_perms = generate_resource_permissions(
         f"{resource.logical_name}KmsKey", KMS_ACCESS_TYPES, arn=key_arn
     )
     add_iam_policy_to_service_task_role(
         target[0].template, resource, kms_perms, "EncryptDecrypt", selected_services
     )
 
@@ -210,15 +212,17 @@
                 target[3],
                 arn=arn_attr_value,
                 value=main_attr_value,
             )
             if (
                 hasattr(resource, "kms_arn_attr")
                 and resource.kms_arn_attr
-                and keyisset(resource.kms_arn_attr, mapping[resource.logical_name])
+                and keyisset(
+                    resource.kms_arn_attr.title, mapping[resource.logical_name]
+                )
             ):
                 handle_kms_access(mapping_family, resource, target, selected_services)
 
 
 def assign_new_resource_to_service(resource, res_root_stack):
     """
     Function to assign the new resource to the service/family using it.
```

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/__init__.py` & `ecs_composex-0.9.2/ecs_composex/s3/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/s3_aws.py` & `ecs_composex-0.9.2/ecs_composex/s3/s3_aws.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/s3_ecs.py` & `ecs_composex-0.9.2/ecs_composex/s3/s3_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/s3_params.py` & `ecs_composex-0.9.2/ecs_composex/s3/s3_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/s3_perms.json` & `ecs_composex-0.9.2/ecs_composex/s3/s3_perms.json`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/s3_perms.py` & `ecs_composex-0.9.2/ecs_composex/s3/s3_perms.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/s3_stack.py` & `ecs_composex-0.9.2/ecs_composex/s3/s3_stack.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/s3/s3_template.py` & `ecs_composex-0.9.2/ecs_composex/s3/s3_template.py`

 * *Files 18% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 #  #
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 from troposphere import Ref, Sub, s3, AWS_NO_VALUE, AWS_ACCOUNT_ID, AWS_REGION
 
 from ecs_composex.common import keyisset, keypresent, LOG
-from ecs_composex.s3 import metadata
+from ecs_composex.resources_import import import_record_properties
 
 
 def create_bucket_encryption_default(props=None):
     if props is None:
         props = {"SSEAlgorithm": "AES256"}
     default_encryption = s3.ServerSideEncryptionByDefault(**props)
     return s3.BucketEncryption(
@@ -254,26 +254,10 @@
         Sub(bucket_name)
         if isinstance(bucket_name, str)
         and (bucket_name.find(AWS_REGION) >= 0 or bucket_name.find(AWS_ACCOUNT_ID) >= 0)
         else bucket_name
     )
     LOG.debug(bucket_name)
     LOG.debug(final_bucket_name)
-    props = {
-        "AccelerateConfiguration": define_accelerate_config(
-            bucket.properties, bucket.settings, bucket_name
-        ),
-        "BucketEncryption": handle_bucket_encryption(
-            bucket.properties, bucket.settings
-        ),
-        "AccessControl": define_access_control(bucket.properties),
-        "BucketName": final_bucket_name,
-        "ObjectLockEnabled": define_objects_locking(bucket.properties),
-        "PublicAccessBlockConfiguration": define_public_block_access(bucket.properties),
-        "VersioningConfiguration": define_bucket_versioning(bucket.properties),
-        "Metadata": metadata,
-        "DeletionPolicy": "Retain"
-        if not keyisset("DeletionPolicy", bucket.settings)
-        else bucket.settings["DeletionPolicy"],
-    }
+    props = import_record_properties(bucket.properties, s3.Bucket)
     bucket.cfn_resource = s3.Bucket(bucket.logical_name, **props)
     return bucket
```

### Comparing `ecs_composex-0.8.9/ecs_composex/secrets/__init__.py` & `ecs_composex-0.9.2/ecs_composex/secrets/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/secrets/compose_secrets.py` & `ecs_composex-0.9.2/ecs_composex/secrets/compose_secrets.py`

 * *Files 2% similar despite different names*

```diff
@@ -92,15 +92,15 @@
         :param str name:
         :param dict definition:
         :param ecs_composex.common.settings.ComposeXSettings settings:
         """
         self.services = []
         if not any(key in definition[self.x_key].keys() for key in self.allowed_keys):
             raise KeyError(
-                f"You must define at least one of",
+                "You must define at least one of",
                 self.allowed_keys,
                 "Got",
                 definition.keys(),
             )
         elif not all(key in self.valid_keys for key in definition[self.x_key].keys()):
             raise KeyError(
                 "Only valid keys are",
@@ -133,15 +133,21 @@
     def add_json_keys(self):
         """
         Method to add secrets definitions based on JSON secret keys
         """
         if not keyisset(self.json_keys_key, self.definition[self.x_key]):
             return
         required_keys = ["Name", "Key"]
-        for secret_key in self.definition[self.x_key][self.json_keys_key]:
+        unfiltered_secrets = self.definition[self.x_key][self.json_keys_key]
+        LOG.debug(f"UN-FILTERED SECRETS {unfiltered_secrets}")
+        filtered_secrets = [
+            dict(y) for y in set(tuple(x.items()) for x in unfiltered_secrets)
+        ]
+        LOG.debug(f"FILTERED SECRETS {filtered_secrets}")
+        for secret_key in filtered_secrets:
             if not all(key in required_keys for key in secret_key):
                 raise KeyError(
                     "For Secrets JSON Key support, you must specify",
                     required_keys,
                     "Got",
                     secret_key.keys(),
                 )
```

### Comparing `ecs_composex-0.8.9/ecs_composex/secrets/secrets_aws.py` & `ecs_composex-0.9.2/ecs_composex/secrets/secrets_aws.py`

 * *Files 11% similar despite different names*

```diff
@@ -15,28 +15,28 @@
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 Module to find the Secrets from AWS Tags
 """
 
-import re
-
 from botocore.exceptions import ClientError
 
 from ecs_composex.common import LOG, keyisset
 from ecs_composex.common.aws import (
     find_aws_resource_arn_from_tags_api,
     define_lookup_role_from_info,
 )
 
 
 def get_secret_config(logical_name, secret_arn, session):
     """
+    Function to get the secret config used to define its mapping
 
+    :param str logical_name:
     :param str secret_arn:
     :param boto3.session.Session session:
     :return:
     """
 
     secret_config = {}
     client = session.client("secretsmanager")
@@ -53,15 +53,16 @@
         raise
 
 
 def lookup_secret_config(logical_name, lookup, session):
     """
     Function to find the DB in AWS account
 
-    :param dict lookup: The Lookup definition for DB
+    :param str logical_name: Logical name of the resource
+    :param dict lookup: The Lookup definition
     :param boto3.session.Session session: Boto3 session for clients
     :return:
     """
     secrets_types = {
         "secretsmanager:secret": {
             "regexp": r"(?:^arn:aws(?:-[a-z]+)?:secretsmanager:[\w-]+:[0-9]{12}:secret:)([\S]+)(?:-[A-Za-z0-9]+)$"
         },
```

### Comparing `ecs_composex-0.8.9/ecs_composex/secrets/secrets_params.py` & `ecs_composex-0.9.2/ecs_composex/secrets/secrets_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sns/__init__.py` & `ecs_composex-0.9.2/ecs_composex/sns/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sns/sns_aws.py` & `ecs_composex-0.9.2/ecs_composex/sns/sns_aws.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sns/sns_ecs.py` & `ecs_composex-0.9.2/ecs_composex/sns/sns_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sns/sns_params.py` & `ecs_composex-0.9.2/ecs_composex/sns/sns_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sns/sns_perms.py` & `ecs_composex-0.9.2/ecs_composex/sns/sns_perms.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sns/sns_stack.py` & `ecs_composex-0.9.2/ecs_composex/sns/sns_stack.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sns/sns_templates.py` & `ecs_composex-0.9.2/ecs_composex/sns/sns_templates.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/__init__.py` & `ecs_composex-0.9.2/ecs_composex/sqs/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/sqs_aws.py` & `ecs_composex-0.9.2/ecs_composex/sqs/sqs_aws.py`

 * *Files 4% similar despite different names*

```diff
@@ -24,34 +24,36 @@
 from botocore.exceptions import ClientError
 
 from ecs_composex.common import LOG, keyisset
 from ecs_composex.common.aws import (
     find_aws_resource_arn_from_tags_api,
     define_lookup_role_from_info,
 )
-from ecs_composex.sqs.sqs_params import SQS_ARN, SQS_KMS_KEY_T
+from ecs_composex.sqs.sqs_params import SQS_ARN, SQS_KMS_KEY_T, SQS_NAME
 
 
 def get_queue_config(logical_name, queue_arn, session):
     """
 
     :param str queue_arn:
     :param boto3.session.Session session:
     :return:
     """
     queue_parts = re.compile(r"(?:^arn:aws(?:-[a-z]+)?:sqs:)([\S]+):([0-9]+):([\S]+)$")
     queue_name = queue_parts.match(queue_arn).groups()[2]
     queue_owner = queue_parts.match(queue_arn).groups()[1]
-    queue_config = {logical_name: queue_name, SQS_ARN.title: queue_arn}
+    queue_config = {SQS_ARN.title: queue_arn}
     client = session.client("sqs")
     try:
         url_r = client.get_queue_url(
             QueueName=queue_name, QueueOwnerAWSAccountId=queue_owner
         )
-        queue_config.update({logical_name: url_r["QueueUrl"]})
+        queue_config.update(
+            {logical_name: url_r["QueueUrl"], SQS_NAME.title: queue_name}
+        )
         try:
             encryption_config_r = client.get_queue_attributes(
                 QueueUrl=url_r["QueueUrl"], AttributeNames=["KmsMasterKeyId"]
             )
             if keyisset("Attributes", encryption_config_r) and keyisset(
                 "KmsMasterKeyId", encryption_config_r["Attributes"]
             ):
```

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/sqs_ecs.py` & `ecs_composex-0.9.2/ecs_composex/sqs/sqs_ecs.py`

 * *Files 6% similar despite different names*

```diff
@@ -16,94 +16,129 @@
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 Module to apply SQS settings onto ECS Services
 """
 
 from troposphere import Parameter
-from troposphere import Ref, GetAtt
+from troposphere import Ref, GetAtt, FindInMap
 from troposphere.cloudwatch import Alarm, MetricDimension
 
 from ecs_composex.common import LOG, keyisset, add_parameters
 from ecs_composex.ecs.ecs_params import SERVICE_SCALING_TARGET
 from ecs_composex.ecs.ecs_scaling import (
     generate_alarm_scaling_out_policy,
     reset_to_zero_policy,
 )
 from ecs_composex.resource_settings import (
     handle_resource_to_services,
     handle_lookup_resource,
 )
 from ecs_composex.sqs.sqs_aws import lookup_queue_config
-from ecs_composex.sqs.sqs_params import SQS_NAME, SQS_KMS_KEY_T
+from ecs_composex.sqs.sqs_params import SQS_NAME, SQS_KMS_KEY_T, MOD_KEY
 
 
 def handle_service_scaling(resource, res_root_stack):
     """
-    Function to assign resource to services stack
+    Function to define and prepare settings for scaling rules based for SQS Queues discovered through lookup
 
-    :param resource:
-    :type resource: ecs_composex.common.compose_resources.XResource
-    :param res_root_stack:
-    :type res_root_stack: ecs_composex.common.stacks.ComposeXStack
+    :param ecs_composex.common.compose_resources.XResource resource:
+    :param ecs_composex.common.stacks.ComposeXStack res_root_stack:
     :raises KeyError: if the service name is not a listed service in docker-compose.
+    :return:
     """
     resource_attribute = SQS_NAME.title
-    resource_parameter = Parameter(
-        f"{resource.logical_name}{resource_attribute}", Type="String"
-    )
-    resource_value = GetAtt(
-        res_root_stack.title, f"Outputs.{resource.logical_name}{SQS_NAME.title}"
-    )
+    if not resource.lookup:
+        resource_value = GetAtt(
+            res_root_stack.title, f"Outputs.{resource.logical_name}{SQS_NAME.title}"
+        )
+    else:
+        resource_value = FindInMap(MOD_KEY, resource.logical_name, resource_attribute)
     for target in resource.families_scaling:
         if SERVICE_SCALING_TARGET not in target[0].template.resources:
             LOG.warning(
                 f"No Scalable target defined for {target[0].name}."
                 " You need to define `scaling.range` in x-configs first. No scaling applied"
             )
             return
-        add_parameters(target[0].template, [resource_parameter])
-        target[0].stack.Parameters.update({resource_parameter.title: resource_value})
         scaling_out_policy = generate_alarm_scaling_out_policy(
             target[0].logical_name,
             target[0].template,
             target[1],
             scaling_source=resource.logical_name,
         )
         scaling_in_policy = reset_to_zero_policy(
             target[0].logical_name,
             target[0].template,
             target[1],
             scaling_source=resource.logical_name,
         )
-        Alarm(
-            f"SqsScalingAlarm{resource.logical_name}To{target[0].logical_name}",
-            template=target[0].template,
-            ActionsEnabled=True,
-            AlarmActions=[Ref(scaling_out_policy)],
-            AlarmDescription=f"MessagesProcessingWatchFor{resource.logical_name}To{target[0].logical_name}",
-            ComparisonOperator="GreaterThanOrEqualToThreshold",
-            DatapointsToAlarm=1,
-            Dimensions=[
-                MetricDimension(Name="QueueName", Value=Ref(resource_parameter)),
-            ],
-            EvaluationPeriods=1,
-            InsufficientDataActions=[Ref(scaling_in_policy)],
-            MetricName="ApproximateNumberOfMessagesVisible",
-            Namespace="AWS/SQS",
-            OKActions=[Ref(scaling_in_policy)],
-            Period="60",
-            Statistic="Sum",
-            TreatMissingData="notBreaching",
-            Threshold=float(
-                scaling_out_policy.StepScalingPolicyConfiguration.StepAdjustments[
-                    0
-                ].MetricIntervalLowerBound
-            ),
-        )
+        if not resource.lookup:
+            resource_parameter = Parameter(
+                f"{resource.logical_name}{resource_attribute}", Type="String"
+            )
+            add_parameters(target[0].template, [resource_parameter])
+            target[0].stack.Parameters.update(
+                {resource_parameter.title: resource_value}
+            )
+            add_alarm_for_resource(
+                resource,
+                target,
+                scaling_out_policy,
+                scaling_in_policy,
+                Ref(resource_parameter),
+            )
+        else:
+            add_alarm_for_resource(
+                resource,
+                target,
+                scaling_out_policy,
+                scaling_in_policy,
+                resource_value,
+            )
+
+
+def add_alarm_for_resource(
+    resource, target, scaling_out_policy, scaling_in_policy, resource_parameter
+):
+    """
+    Function to add the Alarm for SQS resource to the service template
+
+    :param ecs_composex.common.compose_resources.XResource resource:
+    :param tuple target:
+    :param scaling_out_policy:
+    :param scaling_in_policy:
+    :param resource_parameter:
+    :return:
+    """
+    Alarm(
+        f"SqsScalingAlarm{resource.logical_name}To{target[0].logical_name}",
+        template=target[0].template,
+        ActionsEnabled=True,
+        AlarmActions=[Ref(scaling_out_policy)],
+        AlarmDescription=f"MessagesProcessingWatchFor{resource.logical_name}To{target[0].logical_name}",
+        ComparisonOperator="GreaterThanOrEqualToThreshold",
+        DatapointsToAlarm=1,
+        Dimensions=[
+            MetricDimension(Name="QueueName", Value=resource_parameter),
+        ],
+        EvaluationPeriods=1,
+        InsufficientDataActions=[Ref(scaling_in_policy)],
+        MetricName="ApproximateNumberOfMessagesVisible",
+        Namespace="AWS/SQS",
+        OKActions=[Ref(scaling_in_policy)],
+        Period="60",
+        Statistic="Sum",
+        TreatMissingData="notBreaching",
+        Threshold=float(
+            scaling_out_policy.StepScalingPolicyConfiguration.StepAdjustments[
+                0
+            ].MetricIntervalLowerBound
+        ),
+    )
 
 
 def create_sqs_mappings(mapping, resources, settings):
     """
     Function to create the resource mapping for SQS Queues.
 
     :param dict mapping:
@@ -136,8 +171,9 @@
         services_stack.DependsOn.append(res_root_stack.title)
         LOG.info(f"Added dependency between services and {res_root_stack.title}")
     for new_res in new_resources:
         handle_resource_to_services(new_res, services_stack, res_root_stack, settings)
         handle_service_scaling(new_res, res_root_stack)
     create_sqs_mappings(resource_mappings, lookup_resources, settings)
     for lookup_res in lookup_resources:
-        handle_lookup_resource(resource_mappings, "sqs", lookup_res)
+        handle_lookup_resource(resource_mappings, MOD_KEY, lookup_res)
+        handle_service_scaling(lookup_res, None)
```

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/sqs_params.py` & `ecs_composex-0.9.2/ecs_composex/sqs/sqs_params.py`

 * *Files 10% similar despite different names*

```diff
@@ -34,9 +34,10 @@
 
 DLQ_ARN_T = "DeadLetterQueueArn"
 DLQ_ARN = Parameter(DLQ_ARN_T, Type="String")
 
 SQS_KMS_KEY_T = "QueueKmsKey"
 SQS_KMS_KEY = Parameter(SQS_KMS_KEY_T, Type="String")
 
-RES_KEY = f"x-{path.basename(path.dirname(path.abspath(__file__)))}"
+MOD_KEY = f"{path.basename(path.dirname(path.abspath(__file__)))}"
+RES_KEY = f"x-{MOD_KEY}"
 SQS_SSM_PREFIX = f"/{RES_KEY}/"
```

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/sqs_perms.json` & `ecs_composex-0.9.2/ecs_composex/sqs/sqs_perms.json`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/sqs_perms.py` & `ecs_composex-0.9.2/ecs_composex/sqs/sqs_perms.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/sqs_stack.py` & `ecs_composex-0.9.2/ecs_composex/sqs/sqs_stack.py`

 * *Files 8% similar despite different names*

```diff
@@ -26,15 +26,15 @@
 from ecs_composex.common import validate_input, keyisset, LOG, EXIT_CODES
 from ecs_composex.common.compose_resources import set_resources, XResource
 from ecs_composex.common.stacks import ComposeXStack
 from ecs_composex.sqs.sqs_params import (
     RES_KEY,
     SQS_ARN,
     SQS_URL,
-    SQS_KMS_KEY_T,
+    SQS_KMS_KEY,
     SQS_NAME,
 )
 from ecs_composex.sqs.sqs_perms import get_access_types
 from ecs_composex.sqs.sqs_template import generate_sqs_root_template
 
 
 def create_sqs_template(settings):
@@ -62,20 +62,16 @@
     """
 
     policies_scaffolds = get_access_types()
 
     def __init__(self, name, definition, settings):
         super().__init__(name, definition, settings)
         self.main_attr = SQS_URL
-        self.kms_arn_attr = SQS_KMS_KEY_T
-
+        self.kms_arn_attr = SQS_KMS_KEY
         self.arn_attr = SQS_ARN
-        self.arn_attr_value = self.arn_attr
-        self.main_attr_value = self.main_attr
-        self.kms_arn_attr_value = self.kms_arn_attr
 
     def init_outputs(self):
         self.output_properties = {
             SQS_URL.title: (self.logical_name, self.cfn_resource, Ref, None),
             SQS_ARN.title: (
                 f"{self.logical_name}{SQS_ARN.title}",
                 self.cfn_resource,
```

### Comparing `ecs_composex-0.8.9/ecs_composex/sqs/sqs_template.py` & `ecs_composex-0.9.2/ecs_composex/sqs/sqs_template.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/tcp_resources_settings.py` & `ecs_composex-0.9.2/ecs_composex/tcp_resources_settings.py`

 * *Files 1% similar despite different names*

```diff
@@ -49,16 +49,15 @@
         attr_name = attribute.title
     else:
         raise TypeError(
             "Attribute must be a of type", str, Parameter, "Got", type(attribute)
         )
     imported = resource.get_resource_attribute_value(attr_name, root_stack_title)
     parameter = resource.get_resource_attribute_parameter(attr_name)
-
-    return (imported, parameter)
+    return imported, parameter
 
 
 def db_secrets_names(db):
     """
     Function to return the list of env vars set for the DB to use as env vars for the Secret.
 
     :return: list of names to use.
@@ -180,16 +179,24 @@
     :param res_root_stack:
     :param port_parameter:
     :return:
     """
     if resource.logical_name not in res_root_stack.stack_template.resources:
         raise KeyError(f"DB {resource.logical_name} not defined in DocDB Root template")
 
-    port_settings = get_param_and_value(resource, port_parameter, res_root_stack.title)
-    sg_settings = get_param_and_value(resource, resource.db_sg, res_root_stack.title)
+    port_settings = get_param_and_value(
+        resource,
+        port_parameter,
+        res_root_stack.title,
+    )
+    sg_settings = get_param_and_value(
+        resource,
+        resource.db_sg,
+        res_root_stack.title,
+    )
     for target in resource.families_targets:
         add_parameters(target[0].template, [sg_settings[1], port_settings[1]])
         target[0].stack.Parameters.update(
             {
                 sg_settings[1].title: sg_settings[0],
                 port_settings[1].title: port_settings[0],
             }
```

### Comparing `ecs_composex-0.8.9/ecs_composex/utils/__init__.py` & `ecs_composex-0.9.2/ecs_composex/events/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/utils/init_ecs.py` & `ecs_composex-0.9.2/ecs_composex/utils/init_ecs.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/utils/init_s3.py` & `ecs_composex-0.9.2/ecs_composex/utils/init_s3.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/__init__.py` & `ecs_composex-0.9.2/ecs_composex/vpc/__init__.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/aws_mappings.py` & `ecs_composex-0.9.2/ecs_composex/vpc/aws_mappings.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/cli.py` & `ecs_composex-0.9.2/ecs_composex/vpc/cli.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/vpc_aws.py` & `ecs_composex-0.9.2/ecs_composex/vpc/vpc_aws.py`

 * *Files 13% similar despite different names*

```diff
@@ -88,8 +88,21 @@
             types=vpc_types,
             allow_multi=True,
         )
         vpc_settings[subnet_key] = [
             re.match(vpc_types[subnet_type]["regexp"], subnet_arn).groups()[0]
             for subnet_arn in subnet_arns
         ]
+    extra_subnets = [key for key in lookup.keys() if key not in required_keys]
+    for subnet_name in extra_subnets:
+        subnet_arns = find_aws_resource_arn_from_tags_api(
+            lookup[subnet_name],
+            lookup_session,
+            subnet_type,
+            types=vpc_types,
+            allow_multi=True,
+        )
+        vpc_settings[subnet_name] = [
+            re.match(vpc_types[subnet_type]["regexp"], subnet_arn).groups()[0]
+            for subnet_arn in subnet_arns
+        ]
     return vpc_settings
```

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/vpc_conditions.py` & `ecs_composex-0.9.2/ecs_composex/__init__.py`

 * *Files 8% similar despite different names*

```diff
@@ -10,7 +10,14 @@
 #  This program is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
+
+
+"""Top-level package for ECS ComposeX."""
+
+__author__ = """John Preston"""
+__email__ = "john@lambda-my-aws.io"
+__version__ = "0.9.2"
```

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/vpc_maths.py` & `ecs_composex-0.9.2/ecs_composex/vpc/vpc_maths.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/vpc_params.py` & `ecs_composex-0.9.2/ecs_composex/vpc/vpc_params.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/vpc_stack.py` & `ecs_composex-0.9.2/ecs_composex/vpc/vpc_stack.py`

 * *Files 24% similar despite different names*

```diff
@@ -15,49 +15,113 @@
 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 Module for VpcStack
 """
 
+import re
+
+from troposphere import Parameter
 from troposphere import Ref, If
 
-from ecs_composex.common.ecs_composex import X_KEY
-from ecs_composex.common import add_parameters, LOG
+from ecs_composex.common import add_parameters, LOG, build_template
 from ecs_composex.common import keyisset
+from ecs_composex.common.ecs_composex import X_KEY
 from ecs_composex.common.stacks import ComposeXStack
-from ecs_composex.vpc.vpc_template import generate_vpc_template
+from ecs_composex.dns import dns_params, dns_conditions
+from ecs_composex.vpc import aws_mappings
+from ecs_composex.vpc.vpc_aws import lookup_x_vpc_settings
+from ecs_composex.vpc.vpc_maths import get_subnet_layers
 from ecs_composex.vpc.vpc_params import (
     RES_KEY,
     VPC_ID,
     APP_SUBNETS,
     STORAGE_SUBNETS,
     PUBLIC_SUBNETS,
     DEFAULT_VPC_CIDR,
     VPC_CIDR,
     VPC_SINGLE_NAT,
+    SUBNETS_TYPE,
 )
-from ecs_composex.dns import dns_params, dns_conditions
-from ecs_composex.vpc.vpc_aws import lookup_x_vpc_settings
+from ecs_composex.vpc.vpc_subnets import (
+    add_apps_subnets,
+    add_public_subnets,
+    add_storage_subnets,
+)
+from ecs_composex.vpc.vpc_template import (
+    add_vpc_core,
+    add_vpc_flow,
+    add_template_outputs,
+    add_vpc_cidrs_outputs,
+)
+
+AZ_INDEX_PATTERN = r"(([a-z0-9-]+)([a-z]{1}$))"
+AZ_INDEX_RE = re.compile(AZ_INDEX_PATTERN)
 
 
 class VpcStack(ComposeXStack):
     """
     Class to create the VPC Stack
     """
 
     def __init__(self, title, settings, vpc_settings, **kwargs):
-        template = generate_vpc_template(
-            cidr_block=vpc_settings[VPC_CIDR.title],
-            azs=settings.aws_azs,
-            single_nat=vpc_settings[VPC_SINGLE_NAT.title],
-            endpoints=vpc_settings["Endpoints"]
-            if keyisset("Endpoints", vpc_settings)
-            else None,
+
+        if not keyisset("Endpoints", vpc_settings):
+            endpoints = []
+        else:
+            endpoints = vpc_settings["Endpoints"]
+
+        if endpoints is None:
+            endpoints = []
+        curated_azs = []
+        for az in settings.aws_azs:
+            if isinstance(az, dict):
+                curated_azs.append(az["ZoneName"])
+            elif isinstance(az, str):
+                curated_azs.append(az)
+        azs_index = [AZ_INDEX_RE.match(az).groups()[-1] for az in curated_azs]
+        layers = get_subnet_layers(vpc_settings[VPC_CIDR.title], len(curated_azs))
+        template = build_template(
+            "VpcTemplate generated via ECS ComposeX",
+            [dns_params.PRIVATE_DNS_ZONE_NAME],
+        )
+        LOG.debug(azs_index)
+        template.add_mapping("AwsLbAccounts", aws_mappings.AWS_LB_ACCOUNTS)
+        vpc_core = add_vpc_core(template, vpc_settings[VPC_CIDR.title])
+        self.vpc = vpc_core[0]
+        storage_subnets = add_storage_subnets(template, self.vpc, azs_index, layers)
+        public_subnets = add_public_subnets(
+            template,
+            self.vpc,
+            azs_index,
+            layers,
+            vpc_core[-1],
+            vpc_settings[VPC_SINGLE_NAT.title],
+        )
+        app_subnets = add_apps_subnets(
+            template, self.vpc, azs_index, layers, public_subnets[-1], endpoints
         )
+        add_template_outputs(
+            template,
+            self.vpc,
+            storage_subnets[1],
+            public_subnets[1],
+            app_subnets[1],
+        )
+        if keyisset("EnableFlowLogs", vpc_settings):
+            print("ADDING FLOW LOGS")
+            add_vpc_flow(
+                template,
+                self.vpc,
+                boundary=vpc_settings["FlowLogsRoleBoundary"]
+                if keyisset("FlowLogsRoleBoundary", vpc_settings)
+                else None,
+            )
+        add_vpc_cidrs_outputs(template, self.vpc, layers)
         super().__init__(title, stack_template=template, **kwargs)
 
 
 def define_create_settings(create_def):
     """
     Function to create the VPC creation settings
 
@@ -71,15 +135,16 @@
         VPC_SINGLE_NAT.title: True
         if not keyisset(VPC_SINGLE_NAT.title, create_def)
         else create_def[VPC_SINGLE_NAT.title],
         "Endpoints": create_def["Endpoints"]
         if keyisset("Endpoints", create_def)
         else [],
     }
-    return create_settings
+    create_def.update(create_settings)
+    return create_def
 
 
 def create_new_vpc(vpc_xkey, settings, default=False):
     if not default:
         create_settings = define_create_settings(
             settings.compose_content[vpc_xkey]["Create"]
         )
@@ -100,59 +165,78 @@
                 Ref(dns_params.PRIVATE_DNS_ZONE_NAME),
             ),
         }
     )
     return vpc_stack
 
 
+def set_subnets_from_use(subnets_list, vpc_settings, subnets_def):
+    for subnet_name in subnets_list:
+        if not isinstance(vpc_settings[subnet_name], (list, str)):
+            raise TypeError(
+                "The subnet_name must be of type", str, list, "Got", type(subnet_name)
+            )
+        subnets = (
+            vpc_settings[subnet_name].split(",")
+            if isinstance(vpc_settings[subnet_name], str)
+            else vpc_settings[subnet_name]
+        )
+        subnets_def[subnet_name] = subnets
+
+
 def import_vpc_settings(vpc_settings):
     """
     Function to import settings set "in-stone" from docker-compose definition
 
     :param dict vpc_settings:
     :return: settings
     :rtype dict:
     """
     if not keyisset(VPC_ID.title, vpc_settings):
         raise KeyError("You must specify the VPC ID to use for deployment")
     settings = {VPC_ID.title: vpc_settings[VPC_ID.title]}
     required_subnets = [APP_SUBNETS.title, PUBLIC_SUBNETS.title, STORAGE_SUBNETS.title]
     if not all(subnet in vpc_settings.keys() for subnet in required_subnets):
         raise KeyError("All subnets must be indicated", required_subnets)
-    for subnet_name in required_subnets:
-        if not isinstance(vpc_settings[subnet_name], (list, str)):
-            raise TypeError(
-                "The subnet_name must be of type", str, list, "Got", type(subnet_name)
-            )
-        subnets = (
-            vpc_settings[subnet_name].split(",")
-            if isinstance(vpc_settings[subnet_name], str)
-            else vpc_settings[subnet_name]
-        )
-        settings[subnet_name] = subnets
+    extra_subnets = [key for key in vpc_settings.keys() if key not in required_subnets]
+    set_subnets_from_use(required_subnets, vpc_settings, settings)
+    set_subnets_from_use(extra_subnets, vpc_settings, settings)
+
     return settings
 
 
 def apply_vpc_settings(x_settings, root_stack, settings):
     """
 
     :param x_settings:
     :param root_stack:
+    :param ecs_composex.common.settings.ComposeXSettings settings:
     :return:
     """
     add_parameters(
         root_stack.stack_template,
         [VPC_ID, APP_SUBNETS, STORAGE_SUBNETS, PUBLIC_SUBNETS],
     )
     settings_params = {
         VPC_ID.title: x_settings[VPC_ID.title],
         APP_SUBNETS.title: x_settings[APP_SUBNETS.title],
         STORAGE_SUBNETS.title: x_settings[STORAGE_SUBNETS.title],
         PUBLIC_SUBNETS.title: x_settings[PUBLIC_SUBNETS.title],
     }
+    settings.subnets_parameters.append(APP_SUBNETS)
+    settings.subnets_parameters.append(PUBLIC_SUBNETS)
+    settings.subnets_parameters.append(STORAGE_SUBNETS)
+    for setting_name in x_settings:
+        if setting_name not in settings_params.keys():
+            param = root_stack.stack_template.add_parameter(
+                Parameter(setting_name, Type=SUBNETS_TYPE)
+            )
+            settings_params[param.title] = x_settings[param.title]
+            settings.subnets_parameters.append(param)
+
     root_stack.Parameters.update(settings_params)
     settings.set_azs_from_vpc_import(
         public_subnets=x_settings[PUBLIC_SUBNETS.title],
         app_subnets=x_settings[APP_SUBNETS.title],
         storage_subnets=x_settings[STORAGE_SUBNETS.title],
     )
 
@@ -167,28 +251,32 @@
     :rtype: VpcStack
     """
     vpc_stack = None
     vpc_xkey = f"{X_KEY}{RES_KEY}"
 
     if keyisset(vpc_xkey, settings.compose_content):
         if keyisset("Lookup", settings.compose_content[vpc_xkey]):
+            settings.create_vpc = False
             x_settings = lookup_x_vpc_settings(
                 settings.compose_content[vpc_xkey]["Lookup"], settings.session
             )
             apply_vpc_settings(x_settings, root_stack, settings)
         elif keyisset("Use", settings.compose_content[vpc_xkey]):
             x_settings = import_vpc_settings(settings.compose_content[vpc_xkey]["Use"])
             apply_vpc_settings(x_settings, root_stack, settings)
         else:
             if keyisset("Create", settings.compose_content[vpc_xkey]) and keyisset(
                 "Lookup", settings.compose_content[vpc_xkey]
             ):
+                settings.create_vpc = True
                 LOG.warning(
                     "We have both Create and Lookup set for x-vpc." "Creating a new VPC"
                 )
             vpc_stack = create_new_vpc(vpc_xkey, settings)
+            settings.create_vpc = True
     else:
         LOG.info(f"No {vpc_xkey} detected. Creating a new VPC.")
         vpc_stack = create_new_vpc(vpc_xkey, settings, default=True)
+        settings.create_vpc = True
     if isinstance(vpc_stack, VpcStack):
         root_stack.stack_template.add_resource(vpc_stack)
     return vpc_stack
```

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/vpc_subnets.py` & `ecs_composex-0.9.2/ecs_composex/vpc/vpc_subnets.py`

 * *Files identical despite different names*

### Comparing `ecs_composex-0.8.9/ecs_composex/vpc/vpc_template.py` & `ecs_composex-0.9.2/ecs_composex/vpc/vpc_template.py`

 * *Files 25% similar despite different names*

```diff
@@ -13,42 +13,39 @@
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """
 Create the VPC template and its associated resources
-TODO : Implement VPC Endpoints, NetworkACLs, VPC Flow logging to S3.
 """
 
 import re
 
-from troposphere import Tags, Join, Ref, Sub, If
+from troposphere import AWS_ACCOUNT_ID, AWS_PARTITION, AWS_REGION, AWS_NO_VALUE
+from troposphere import Tags, Join, Ref, Sub, If, GetAtt
 from troposphere.ec2 import (
     VPC as VPCType,
     VPCGatewayAttachment,
     InternetGateway,
     DHCPOptions,
     VPCDHCPOptionsAssociation,
+    FlowLog,
 )
+from troposphere.iam import Role, Policy
+from troposphere.logs import LogGroup
 
-from ecs_composex.common import build_template, LOG
 from ecs_composex.common.cfn_conditions import USE_STACK_NAME_CON_T
 from ecs_composex.common.cfn_params import ROOT_STACK_NAME, ROOT_STACK_NAME_T
 from ecs_composex.common.outputs import ComposeXOutput
 from ecs_composex.dns.dns_params import PRIVATE_DNS_ZONE_NAME
-from ecs_composex.vpc import vpc_params, aws_mappings
-from ecs_composex.vpc.vpc_params import VPC_T, IGW_T
-from ecs_composex.vpc.vpc_maths import get_subnet_layers
-from ecs_composex.vpc.vpc_subnets import (
-    add_public_subnets,
-    add_storage_subnets,
-    add_apps_subnets,
-)
+from ecs_composex.iam import service_role_trust_policy
 from ecs_composex.vpc import metadata
+from ecs_composex.vpc import vpc_params
+from ecs_composex.vpc.vpc_params import VPC_T, IGW_T
 
 AZ_INDEX_PATTERN = r"(([a-z0-9-]+)([a-z]{1}$))"
 AZ_INDEX_RE = re.compile(AZ_INDEX_PATTERN)
 
 
 def add_template_outputs(template, vpc, storage_subnets, public_subnets, app_subnets):
     """
@@ -173,54 +170,71 @@
     VPCDHCPOptionsAssociation(
         "VpcDhcpOptionsAssociate",
         template=template,
         DhcpOptionsId=Ref(dhcp_opts),
         VpcId=Ref(vpc),
         Metadata=metadata,
     )
-    return (vpc, igw)
+    return vpc, igw
 
 
-def generate_vpc_template(cidr_block, azs, endpoints=None, single_nat=False):
+def add_vpc_flow(template, vpc, boundary=None):
     """
-    Function to generate a new VPC template for CFN
+    Function to add VPC Flow Log to log VPC
 
-    :param cidr_block: str of the CIDR used for this VPC
-    :param azs: list of AWS Azs i.e. ['eu-west-1a', 'eu-west-1b']
-    :param single_nat: True/False if you want a single NAT for the Application Subnets
-    :type single_nat: bool
-
-    :return: Template() representing the VPC and associated resources
-    """
-    if endpoints is None:
-        endpoints = []
-    curated_azs = []
-    for az in azs:
-        if isinstance(az, dict):
-            curated_azs.append(az["ZoneName"])
-        elif isinstance(az, str):
-            curated_azs.append(az)
-    azs_index = [AZ_INDEX_RE.match(az).groups()[-1] for az in curated_azs]
-    layers = get_subnet_layers(cidr_block, len(curated_azs))
-    template = build_template(
-        "VpcTemplate generated via ECS Compose X",
-        [PRIVATE_DNS_ZONE_NAME],
-    )
-    LOG.debug(azs_index)
-    template.add_mapping("AwsLbAccounts", aws_mappings.AWS_LB_ACCOUNTS)
-    vpc = add_vpc_core(template, cidr_block)
-    storage_subnets = add_storage_subnets(template, vpc[0], azs_index, layers)
-    public_subnets = add_public_subnets(
-        template, vpc[0], azs_index, layers, vpc[-1], single_nat
-    )
-    app_subnets = add_apps_subnets(
-        template, vpc[0], azs_index, layers, public_subnets[-1], endpoints
-    )
-    add_template_outputs(
-        template,
-        vpc[0],
-        storage_subnets[1],
-        public_subnets[1],
-        app_subnets[1],
+    :param troposphere.Template template:
+    :param vpc: The VPC Object
+    :param str boundary:
+    """
+    if boundary and boundary.startswith("arn:aws"):
+        perm_boundary = boundary
+    elif boundary and not boundary.startswith("arn:aws"):
+        perm_boundary = Sub(
+            f"arn:${{{AWS_PARTITION}}}:iam:${{{AWS_REGION}}}:${{{AWS_ACCOUNT_ID}}}:policy/{boundary}"
+        )
+    else:
+        perm_boundary = Ref(AWS_NO_VALUE)
+    log_group = template.add_resource(
+        LogGroup(
+            "FlowLogsGroup",
+            RetentionInDays=14,
+            LogGroupName=Sub(f"flowlogs/vpc/${{{vpc.title}}}"),
+        )
+    )
+    role = template.add_resource(
+        Role(
+            "FlowLogsRole",
+            AssumeRolePolicyDocument=service_role_trust_policy("ec2"),
+            PermissionsBoundary=perm_boundary,
+            Policies=[
+                Policy(
+                    PolicyName="CloudWatchAccess",
+                    PolicyDocument={
+                        "Version": "2012-10-17",
+                        "Statement": [
+                            {
+                                "Sid": "AllowCloudWatchLoggingToSpecificLogGroup",
+                                "Effect": "Allow",
+                                "Action": [
+                                    "logs:CreateLogStream",
+                                    "logs:PutLogEvents",
+                                ],
+                                "Resource": GetAtt(log_group, "Arn"),
+                            }
+                        ],
+                    },
+                )
+            ],
+        )
+    )
+    template.add_resource(
+        FlowLog(
+            "VpcFlowLogs",
+            DeliverLogsPermissionArn=GetAtt(role, "Arn"),
+            LogGroupName=Ref(log_group),
+            LogDestinationType="cloud-watch-logs",
+            MaxAggregationInterval=600,
+            ResourceId=Ref(vpc),
+            ResourceType="VPC",
+            TrafficType="ALL",
+        )
     )
-    add_vpc_cidrs_outputs(template, vpc[0], layers)
-    return template
```

### Comparing `ecs_composex-0.8.9/ecs_composex.egg-info/PKG-INFO` & `ecs_composex-0.9.2/ecs_composex.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: ecs-composex
-Version: 0.8.9
+Version: 0.9.2
 Summary: Implement for AWS ECS and Docker Compose what SAM is to Serverless for AWS Lambda
 Home-page: https://github.com/lambda-my-aws/ecs_composex
 Author: John Preston
 Author-email: john@lambda-my-aws.io
 License: GPLv3+
 Description: ============
         ECS ComposeX
         ============
         
         |PYPI_VERSION| |PYPI_LICENSE|
         
         |CODE_STYLE| |TDD| |BDD|
         
-        |CODECOV| |QUALITY|
+        |QUALITY|
         
         |BUILD|
         
         ----------------------------------------------------------------------------------------------------
         Be for AWS ECS and docker-compose what AWS SAM is to Lambda
         ----------------------------------------------------------------------------------------------------
         
@@ -259,46 +259,41 @@
         .. _Docker Compose: https://docs.docker.com/compose/
         .. _ECS ComposeX: https://docs.ecs-composex.lambda-my-aws.io
         .. _YAML Specifications: https://yaml.org/spec/
         .. _Extensions fields:  https://docs.docker.com/compose/compose-file/#extension-fields
         .. _ECS ComposeX Project: https://github.com/orgs/lambda-my-aws/projects/3
         .. _CICD Pipeline for multiple services on AWS ECS with ECS ComposeX: https://blog.ecs-composex.lambda-my-aws.io/posts/cicd-pipeline-for-multiple-services-on-aws-ecs-with-ecs-composex/
         
-        .. _AWS ECS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.html
-        .. _AWS VPC: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/vpc.html
-        .. _AWS RDS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/rds.html
-        .. _AWS SQS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/sqs.html
-        .. _AWS KMS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/kms.html
-        .. _AWS DynamoDB: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/dynamodb.html
-        .. _AWS ACM: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/acm.html
-        .. _AWS ELBv2: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/elbv2.html
-        .. _AWS S3: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/s3.html
-        .. _AWS IAM: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.details/iam.html
-        .. _AWS SNS: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/sns.html
-        .. _AWS DocumentDB: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/docdb.html
+        .. _AWS ECS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.html
+        .. _AWS VPC: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/vpc.html
+        .. _AWS RDS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/rds.html
+        .. _AWS SQS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/sqs.html
+        .. _AWS KMS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/kms.html
+        .. _AWS DynamoDB: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/dynamodb.html
+        .. _AWS ACM: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/acm.html
+        .. _AWS ELBv2: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/elbv2.html
+        .. _AWS S3: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/s3.html
+        .. _AWS IAM: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/ecs.details/iam.html
+        .. _AWS SNS: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/sns.html
+        .. _AWS DocumentDB: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/docdb.html
         
-        .. _AWS EC2: https://nightly.docs.ecs-composex.lambda-my-aws.io/features.html#ec2-resources-for-ecs-cluster
-        .. _AWS AppMesh: https://nightly.docs.ecs-composex.lambda-my-aws.io/readme/appmesh.html
+        .. _AWS EC2: https://docs.ecs-composex.lambda-my-aws.io/features.html#ec2-resources-for-ecs-cluster
+        .. _AWS AppMesh: https://docs.ecs-composex.lambda-my-aws.io/readme/appmesh.html
         
-        .. _Lookup: https://nightly.docs.ecs-composex.lambda-my-aws.io/syntax/composex/common.html#lookup
+        .. _Lookup: https://docs.ecs-composex.lambda-my-aws.io/syntax/composex/common.html#lookup
         
         .. |BUILD| image:: https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoidThwNXVIKzVvSnlXcUNVRzVlNE5wN0FiWE4rYzYvaHRNMEM0ZHMxeXRLMytSanhsckozVEN3L1Y5Szl5ZEdJVGxXVElyalZmaFVzR2tSbDBHeFI5cHBRPSIsIml2UGFyYW1ldGVyU3BlYyI6IlZkaml2d28wSGR1YU1xb2ciLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master
         
         .. |DOCS_BUILD| image:: https://readthedocs.org/projects/ecs-composex/badge/?version=latest
                 :target: https://ecs-composex.readthedocs.io/en/latest/?badge=latest
                 :alt: Documentation Status
         
         .. |PYPI_VERSION| image:: https://img.shields.io/pypi/v/ecs_composex.svg
                 :target: https://pypi.python.org/pypi/ecs_composex
         
-        
-        .. |CODECOV| image:: https://img.shields.io/codecov/c/github/lambda-my-aws/ecs_composex?color=black&style=flat-square
-            :alt: Codecov
-            :target: https://codecov.io/gh/lambda-my-aws/ecs_composex
-        
         .. |PYPI_DL| image:: https://img.shields.io/pypi/dm/ecs_composex
             :alt: PyPI - Downloads
             :target: https://pypi.python.org/pypi/ecs_composex
         
         .. |PYPI_LICENSE| image:: https://img.shields.io/github/license/lambda-my-aws/ecs_composex
             :alt: GitHub
             :target: https://github.com/lambda-my-aws/ecs_composex/blob/master/LICENSE
```

### Comparing `ecs_composex-0.8.9/ecs_composex.egg-info/SOURCES.txt` & `ecs_composex-0.9.2/ecs_composex.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -63,33 +63,36 @@
 docs/syntax/composex/compute.rst
 docs/syntax/composex/dns.rst
 docs/syntax/composex/docdb.rst
 docs/syntax/composex/dynamodb.rst
 docs/syntax/composex/ecs.rst
 docs/syntax/composex/ecs_cluster.rst
 docs/syntax/composex/elbv2.rst
+docs/syntax/composex/events.rst
 docs/syntax/composex/kms.rst
 docs/syntax/composex/rds.rst
 docs/syntax/composex/s3.rst
 docs/syntax/composex/sns.rst
 docs/syntax/composex/sqs.rst
 docs/syntax/composex/vpc.rst
 docs/syntax/composex/ecs.details/deploy.rst
 docs/syntax/composex/ecs.details/iam.rst
 docs/syntax/composex/ecs.details/logging.rst
 docs/syntax/composex/ecs.details/network.rst
 docs/syntax/composex/ecs.details/scaling.rst
 docs/syntax/composex/ecs.details/xray.rst
+docs/syntax/docker-compose/networks.rst
 docs/syntax/docker-compose/secrets.rst
 docs/syntax/docker-compose/services.rst
 ecs_composex/__init__.py
 ecs_composex/cli.py
 ecs_composex/ecs_composex.py
 ecs_composex/ingress_settings.py
 ecs_composex/resource_settings.py
+ecs_composex/resources_import.py
 ecs_composex/tcp_resources_settings.py
 ecs_composex.egg-info/PKG-INFO
 ecs_composex.egg-info/SOURCES.txt
 ecs_composex.egg-info/dependency_links.txt
 ecs_composex.egg-info/entry_points.txt
 ecs_composex.egg-info/not-zip-safe
 ecs_composex.egg-info/requires.txt
@@ -106,14 +109,15 @@
 ecs_composex/appmesh/appmesh_params.py
 ecs_composex/appmesh/appmesh_router.py
 ecs_composex/appmesh/appmesh_service.py
 ecs_composex/common/__init__.py
 ecs_composex/common/aws.py
 ecs_composex/common/cfn_conditions.py
 ecs_composex/common/cfn_params.py
+ecs_composex/common/compose_networks.py
 ecs_composex/common/compose_resources.py
 ecs_composex/common/compose_services.py
 ecs_composex/common/compose_volumes.py
 ecs_composex/common/config.py
 ecs_composex/common/ecs_composex.py
 ecs_composex/common/envsubst.py
 ecs_composex/common/files.py
@@ -128,14 +132,15 @@
 ecs_composex/compute/compute_template.py
 ecs_composex/compute/hosts_template.py
 ecs_composex/compute/spot_fleet.py
 ecs_composex/dns/__init__.py
 ecs_composex/dns/dns_conditions.py
 ecs_composex/dns/dns_lookup.py
 ecs_composex/dns/dns_params.py
+ecs_composex/dns/dns_records.py
 ecs_composex/docdb/__init__.py
 ecs_composex/docdb/docdb_ecs.py
 ecs_composex/docdb/docdb_params.py
 ecs_composex/docdb/docdb_stack.py
 ecs_composex/docdb/docdb_template.py
 ecs_composex/dynamodb/__init__.py
 ecs_composex/dynamodb/dynamodb_aws.py
@@ -152,20 +157,34 @@
 ecs_composex/ecs/ecs_conditions.py
 ecs_composex/ecs/ecs_iam.py
 ecs_composex/ecs/ecs_params.py
 ecs_composex/ecs/ecs_scaling.py
 ecs_composex/ecs/ecs_service.py
 ecs_composex/ecs/ecs_service_config.py
 ecs_composex/ecs/ecs_service_network_config.py
+ecs_composex/ecs/ecs_stack.py
 ecs_composex/ecs/ecs_template.py
 ecs_composex/elbv2/__init__.py
 ecs_composex/elbv2/elbv2_ecs.py
 ecs_composex/elbv2/elbv2_params.py
 ecs_composex/elbv2/elbv2_stack.py
+ecs_composex/events/__init__.py
+ecs_composex/events/events_ecs.py
+ecs_composex/events/events_params.py
+ecs_composex/events/events_stack.py
+ecs_composex/events/events_template.py
 ecs_composex/iam/__init__.py
+ecs_composex/kinesis/__init__.py
+ecs_composex/kinesis/kinesis_aws.py
+ecs_composex/kinesis/kinesis_ecs.py
+ecs_composex/kinesis/kinesis_params.py
+ecs_composex/kinesis/kinesis_perms.json
+ecs_composex/kinesis/kinesis_perms.py
+ecs_composex/kinesis/kinesis_stack.py
+ecs_composex/kinesis/kinesis_template.py
 ecs_composex/kms/__init__.py
 ecs_composex/kms/kms_aws.py
 ecs_composex/kms/kms_ecs.py
 ecs_composex/kms/kms_params.py
 ecs_composex/kms/kms_perms.json
 ecs_composex/kms/kms_perms.py
 ecs_composex/kms/kms_stack.py
```

### Comparing `ecs_composex-0.8.9/setup.cfg` & `ecs_composex-0.9.2/setup.cfg`

 * *Files 22% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 [bumpversion]
-current_version = 0.8.9
+current_version = 0.9.2
 commit = True
 tag = True
 
 [bumpversion:file:setup.py]
 search = version="{current_version}"
 replace = version="{new_version}"
```

### Comparing `ecs_composex-0.8.9/setup.py` & `ecs_composex-0.9.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -77,10 +77,10 @@
     keywords="ecs_composex",
     name="ecs_composex",
     packages=find_packages(include=["ecs_composex", "ecs_composex.*"]),
     setup_requires=setup_requirements,
     test_suite="tests",
     tests_require=test_requirements,
     url="https://github.com/lambda-my-aws/ecs_composex",
-    version="0.8.9",
+    version="0.9.2",
     zip_safe=False,
 )
```

