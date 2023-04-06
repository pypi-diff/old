# Comparing `tmp/headless-2.0.0a8.tar.gz` & `tmp/headless-2.0.0a9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "headless-2.0.0a8.tar", last modified: Mon Mar 13 22:16:00 2023, max compression
+gzip compressed data, was "headless-2.0.0a9.tar", last modified: Tue Mar 14 00:42:54 2023, max compression
```

## Comparing `headless-2.0.0a8.tar` & `headless-2.0.0a9.tar`

### file list

```diff
@@ -1,169 +1,169 @@
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.752635 headless-2.0.0a8/
--rw-r--r--   0 cochise    (501) staff       (20)      312 2022-04-18 13:38:41.000000 headless-2.0.0a8/MANIFEST.in
--rw-r--r--   0 cochise    (501) staff       (20)     1024 2023-03-13 22:16:00.752484 headless-2.0.0a8/PKG-INFO
--rw-r--r--   0 cochise    (501) staff       (20)        8 2023-03-13 22:09:35.000000 headless-2.0.0a8/VERSION
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.712043 headless-2.0.0a8/docs/
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.713874 headless-2.0.0a8/docs/source/
--rw-r--r--   0 cochise    (501) staff       (20)     2420 2023-02-15 18:22:20.000000 headless-2.0.0a8/docs/source/conf.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.717296 headless-2.0.0a8/examples/
--rw-r--r--   0 cochise    (501) staff       (20)     2294 2023-02-16 21:27:22.000000 headless-2.0.0a8/examples/oauth2-callback.py
--rw-r--r--   0 cochise    (501) staff       (20)     1199 2023-03-05 09:40:25.000000 headless-2.0.0a8/examples/picqer-create-receipt.py
--rw-r--r--   0 cochise    (501) staff       (20)     1175 2023-02-25 11:09:13.000000 headless-2.0.0a8/examples/picqer-list-products.py
--rw-r--r--   0 cochise    (501) staff       (20)     1021 2023-03-05 11:13:19.000000 headless-2.0.0a8/examples/picqer-list-receipts.py
--rw-r--r--   0 cochise    (501) staff       (20)      962 2023-02-25 02:40:51.000000 headless-2.0.0a8/examples/picqer-list-webhooks.py
--rw-r--r--   0 cochise    (501) staff       (20)     1037 2023-02-15 18:43:26.000000 headless-2.0.0a8/examples/picqer-ratelimit.py
--rw-r--r--   0 cochise    (501) staff       (20)     1454 2023-02-15 18:49:26.000000 headless-2.0.0a8/examples/picqer-traverse-api.py
--rw-r--r--   0 cochise    (501) staff       (20)     1410 2023-02-25 11:07:22.000000 headless-2.0.0a8/examples/piqcer-list-picklist-products.py
--rw-r--r--   0 cochise    (501) staff       (20)     1013 2023-02-15 18:37:30.000000 headless-2.0.0a8/examples/shopify-get-orders.py
--rw-r--r--   0 cochise    (501) staff       (20)     1345 2023-02-15 13:53:15.000000 headless-2.0.0a8/examples/shopify-inspect-catalog.py
--rw-r--r--   0 cochise    (501) staff       (20)     1347 2023-02-15 18:40:52.000000 headless-2.0.0a8/examples/shopify-ratelimit.py
--rw-r--r--   0 cochise    (501) staff       (20)     1263 2023-02-15 14:24:51.000000 headless-2.0.0a8/examples/shopify-set-inventory.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.717643 headless-2.0.0a8/headless/
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.720358 headless-2.0.0a8/headless/core/
--rw-r--r--   0 cochise    (501) staff       (20)      953 2023-02-15 17:12:49.000000 headless-2.0.0a8/headless/core/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     1853 2023-02-15 17:38:48.000000 headless-2.0.0a8/headless/core/deferredresource.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.721222 headless-2.0.0a8/headless/core/httpx/
--rw-r--r--   0 cochise    (501) staff       (20)      552 2023-02-14 23:49:28.000000 headless-2.0.0a8/headless/core/httpx/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     2822 2023-03-13 22:09:16.000000 headless-2.0.0a8/headless/core/httpx/client.py
--rw-r--r--   0 cochise    (501) staff       (20)     1665 2023-02-24 08:45:08.000000 headless-2.0.0a8/headless/core/httpx/request.py
--rw-r--r--   0 cochise    (501) staff       (20)     1056 2023-02-16 17:12:22.000000 headless-2.0.0a8/headless/core/httpx/response.py
--rw-r--r--   0 cochise    (501) staff       (20)     2351 2023-02-15 15:00:27.000000 headless-2.0.0a8/headless/core/linearbackoff.py
--rw-r--r--   0 cochise    (501) staff       (20)     2559 2023-03-07 12:18:10.000000 headless-2.0.0a8/headless/core/resource.py
--rw-r--r--   0 cochise    (501) staff       (20)     3489 2023-03-04 17:44:52.000000 headless-2.0.0a8/headless/core/resourcemeta.py
--rw-r--r--   0 cochise    (501) staff       (20)     2010 2023-02-15 17:10:28.000000 headless-2.0.0a8/headless/core/resourcemetaclass.py
--rw-r--r--   0 cochise    (501) staff       (20)     1577 2023-02-15 17:33:26.000000 headless-2.0.0a8/headless/core/resourcereference.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.712907 headless-2.0.0a8/headless/ext/
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.723056 headless-2.0.0a8/headless/ext/oauth2/
--rw-r--r--   0 cochise    (501) staff       (20)      762 2023-02-22 22:42:27.000000 headless-2.0.0a8/headless/ext/oauth2/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)    11061 2023-03-13 11:57:19.000000 headless-2.0.0a8/headless/ext/oauth2/client.py
--rw-r--r--   0 cochise    (501) staff       (20)     4758 2023-03-13 11:12:02.000000 headless-2.0.0a8/headless/ext/oauth2/clientcredential.py
--rw-r--r--   0 cochise    (501) staff       (20)      508 2023-02-23 23:40:03.000000 headless-2.0.0a8/headless/ext/oauth2/const.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.729026 headless-2.0.0a8/headless/ext/oauth2/models/
--rw-r--r--   0 cochise    (501) staff       (20)     1279 2023-02-23 01:55:37.000000 headless-2.0.0a8/headless/ext/oauth2/models/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     3082 2023-03-10 22:17:19.000000 headless-2.0.0a8/headless/ext/oauth2/models/address.py
--rw-r--r--   0 cochise    (501) staff       (20)      486 2023-02-16 19:06:21.000000 headless-2.0.0a8/headless/ext/oauth2/models/authorizationcode.py
--rw-r--r--   0 cochise    (501) staff       (20)      867 2023-02-16 19:14:27.000000 headless-2.0.0a8/headless/ext/oauth2/models/authorizationendpointresponse.py
--rw-r--r--   0 cochise    (501) staff       (20)      410 2023-02-16 17:43:39.000000 headless-2.0.0a8/headless/ext/oauth2/models/authorizationrequest.py
--rw-r--r--   0 cochise    (501) staff       (20)     1374 2023-02-16 19:45:29.000000 headless-2.0.0a8/headless/ext/oauth2/models/bearertokencredential.py
--rw-r--r--   0 cochise    (501) staff       (20)    11062 2023-03-13 17:15:45.000000 headless-2.0.0a8/headless/ext/oauth2/models/claimset.py
--rw-r--r--   0 cochise    (501) staff       (20)      758 2023-02-16 18:23:04.000000 headless-2.0.0a8/headless/ext/oauth2/models/clientauthenticationmethod.py
--rw-r--r--   0 cochise    (501) staff       (20)     1460 2023-02-17 21:55:41.000000 headless-2.0.0a8/headless/ext/oauth2/models/clientcredentialsrequest.py
--rw-r--r--   0 cochise    (501) staff       (20)     1238 2023-03-12 12:00:13.000000 headless-2.0.0a8/headless/ext/oauth2/models/encodedidtoken.py
--rw-r--r--   0 cochise    (501) staff       (20)      969 2023-02-17 22:00:21.000000 headless-2.0.0a8/headless/ext/oauth2/models/error.py
--rw-r--r--   0 cochise    (501) staff       (20)      771 2023-02-17 21:44:52.000000 headless-2.0.0a8/headless/ext/oauth2/models/iobtainable.py
--rw-r--r--   0 cochise    (501) staff       (20)     1537 2023-02-22 22:45:49.000000 headless-2.0.0a8/headless/ext/oauth2/models/jsonwebtoken.py
--rw-r--r--   0 cochise    (501) staff       (20)     1434 2023-03-12 12:09:01.000000 headless-2.0.0a8/headless/ext/oauth2/models/oidctoken.py
--rw-r--r--   0 cochise    (501) staff       (20)    22960 2023-02-16 18:33:24.000000 headless-2.0.0a8/headless/ext/oauth2/models/servermetadata.py
--rw-r--r--   0 cochise    (501) staff       (20)      527 2023-02-23 02:59:59.000000 headless-2.0.0a8/headless/ext/oauth2/models/subjectidentifier.py
--rw-r--r--   0 cochise    (501) staff       (20)      756 2023-03-12 11:49:38.000000 headless-2.0.0a8/headless/ext/oauth2/models/tokenresponse.py
--rw-r--r--   0 cochise    (501) staff       (20)      496 2023-02-20 14:24:14.000000 headless-2.0.0a8/headless/ext/oauth2/nullcredential.py
--rw-r--r--   0 cochise    (501) staff       (20)     2888 2023-02-20 14:46:35.000000 headless-2.0.0a8/headless/ext/oauth2/server.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.729498 headless-2.0.0a8/headless/ext/oauth2/test/
--rw-r--r--   0 cochise    (501) staff       (20)     1025 2023-02-16 17:38:32.000000 headless-2.0.0a8/headless/ext/oauth2/test/discovery.py
--rw-r--r--   0 cochise    (501) staff       (20)     1141 2023-02-16 18:47:29.000000 headless-2.0.0a8/headless/ext/oauth2/test/manual.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.730496 headless-2.0.0a8/headless/ext/oauth2/types/
--rw-r--r--   0 cochise    (501) staff       (20)      593 2023-02-23 23:55:51.000000 headless-2.0.0a8/headless/ext/oauth2/types/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     1002 2023-02-23 23:55:08.000000 headless-2.0.0a8/headless/ext/oauth2/types/granttype.py
--rw-r--r--   0 cochise    (501) staff       (20)      688 2023-02-23 23:41:08.000000 headless-2.0.0a8/headless/ext/oauth2/types/responsemode.py
--rw-r--r--   0 cochise    (501) staff       (20)      721 2023-02-23 23:34:47.000000 headless-2.0.0a8/headless/ext/oauth2/types/responsetype.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.731737 headless-2.0.0a8/headless/ext/picqer/
--rw-r--r--   0 cochise    (501) staff       (20)      904 2023-03-04 17:15:23.000000 headless-2.0.0a8/headless/ext/picqer/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)      852 2023-02-15 16:21:24.000000 headless-2.0.0a8/headless/ext/picqer/client.py
--rw-r--r--   0 cochise    (501) staff       (20)      933 2023-02-24 08:28:55.000000 headless-2.0.0a8/headless/ext/picqer/credential.py
--rw-r--r--   0 cochise    (501) staff       (20)      751 2023-02-25 02:56:53.000000 headless-2.0.0a8/headless/ext/picqer/defaultclient.py
--rw-r--r--   0 cochise    (501) staff       (20)      794 2023-02-24 00:17:46.000000 headless-2.0.0a8/headless/ext/picqer/environmentcredential.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.738556 headless-2.0.0a8/headless/ext/picqer/v1/
--rw-r--r--   0 cochise    (501) staff       (20)      897 2023-03-04 17:15:11.000000 headless-2.0.0a8/headless/ext/picqer/v1/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     2169 2023-02-25 02:43:12.000000 headless-2.0.0a8/headless/ext/picqer/v1/order.py
--rw-r--r--   0 cochise    (501) staff       (20)      502 2023-02-15 01:04:25.000000 headless-2.0.0a8/headless/ext/picqer/v1/orderfield.py
--rw-r--r--   0 cochise    (501) staff       (20)      598 2023-02-15 01:02:52.000000 headless-2.0.0a8/headless/ext/picqer/v1/orderproduct.py
--rw-r--r--   0 cochise    (501) staff       (20)     1819 2023-02-25 11:39:07.000000 headless-2.0.0a8/headless/ext/picqer/v1/picklist.py
--rw-r--r--   0 cochise    (501) staff       (20)      754 2023-02-25 11:37:45.000000 headless-2.0.0a8/headless/ext/picqer/v1/picklistproduct.py
--rw-r--r--   0 cochise    (501) staff       (20)      541 2023-02-25 11:38:27.000000 headless-2.0.0a8/headless/ext/picqer/v1/pickliststatus.py
--rw-r--r--   0 cochise    (501) staff       (20)      900 2023-02-15 01:00:54.000000 headless-2.0.0a8/headless/ext/picqer/v1/pickuppointdata.py
--rw-r--r--   0 cochise    (501) staff       (20)      863 2023-02-25 10:44:25.000000 headless-2.0.0a8/headless/ext/picqer/v1/picqerresource.py
--rw-r--r--   0 cochise    (501) staff       (20)     2379 2023-03-05 11:53:49.000000 headless-2.0.0a8/headless/ext/picqer/v1/product.py
--rw-r--r--   0 cochise    (501) staff       (20)      506 2023-02-25 10:47:37.000000 headless-2.0.0a8/headless/ext/picqer/v1/productfield.py
--rw-r--r--   0 cochise    (501) staff       (20)      494 2023-02-25 10:38:10.000000 headless-2.0.0a8/headless/ext/picqer/v1/productpricelist.py
--rw-r--r--   0 cochise    (501) staff       (20)      609 2023-02-25 10:49:16.000000 headless-2.0.0a8/headless/ext/picqer/v1/productstock.py
--rw-r--r--   0 cochise    (501) staff       (20)     2719 2023-03-05 12:55:57.000000 headless-2.0.0a8/headless/ext/picqer/v1/purchaseorder.py
--rw-r--r--   0 cochise    (501) staff       (20)      670 2023-02-14 22:38:36.000000 headless-2.0.0a8/headless/ext/picqer/v1/purchaseorderproduct.py
--rw-r--r--   0 cochise    (501) staff       (20)     4582 2023-03-05 13:06:33.000000 headless-2.0.0a8/headless/ext/picqer/v1/receipt.py
--rw-r--r--   0 cochise    (501) staff       (20)     1011 2023-03-05 09:34:07.000000 headless-2.0.0a8/headless/ext/picqer/v1/receiptproduct.py
--rw-r--r--   0 cochise    (501) staff       (20)      510 2023-03-04 17:12:15.000000 headless-2.0.0a8/headless/ext/picqer/v1/receiptpurchaseorder.py
--rw-r--r--   0 cochise    (501) staff       (20)      496 2023-03-04 17:19:54.000000 headless-2.0.0a8/headless/ext/picqer/v1/receiptsupplier.py
--rw-r--r--   0 cochise    (501) staff       (20)      864 2023-02-25 02:43:53.000000 headless-2.0.0a8/headless/ext/picqer/v1/supplier.py
--rw-r--r--   0 cochise    (501) staff       (20)      567 2023-02-15 00:54:45.000000 headless-2.0.0a8/headless/ext/picqer/v1/tag.py
--rw-r--r--   0 cochise    (501) staff       (20)     1288 2023-02-25 02:44:05.000000 headless-2.0.0a8/headless/ext/picqer/v1/user.py
--rw-r--r--   0 cochise    (501) staff       (20)      483 2023-03-04 17:14:15.000000 headless-2.0.0a8/headless/ext/picqer/v1/userreference.py
--rw-r--r--   0 cochise    (501) staff       (20)      664 2023-02-25 02:44:16.000000 headless-2.0.0a8/headless/ext/picqer/v1/warehouse.py
--rw-r--r--   0 cochise    (501) staff       (20)      624 2023-02-25 02:44:24.000000 headless-2.0.0a8/headless/ext/picqer/v1/webhook.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.739861 headless-2.0.0a8/headless/ext/shopify/
--rw-r--r--   0 cochise    (501) staff       (20)      491 2023-02-15 11:20:07.000000 headless-2.0.0a8/headless/ext/shopify/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     1143 2023-02-15 21:15:35.000000 headless-2.0.0a8/headless/ext/shopify/adminclient.py
--rw-r--r--   0 cochise    (501) staff       (20)      781 2023-02-15 11:27:57.000000 headless-2.0.0a8/headless/ext/shopify/credential.py
--rw-r--r--   0 cochise    (501) staff       (20)     2157 2023-03-07 12:31:36.000000 headless-2.0.0a8/headless/ext/shopify/resource.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.744163 headless-2.0.0a8/headless/ext/shopify/v2023_1/
--rw-r--r--   0 cochise    (501) staff       (20)      627 2023-03-07 11:53:32.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)      623 2023-02-15 11:36:40.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/clientdetails.py
--rw-r--r--   0 cochise    (501) staff       (20)      550 2023-02-15 11:41:45.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/customer.py
--rw-r--r--   0 cochise    (501) staff       (20)      795 2023-02-15 12:01:14.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/customeraddress.py
--rw-r--r--   0 cochise    (501) staff       (20)      885 2023-02-15 14:19:15.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/inventorylevel.py
--rw-r--r--   0 cochise    (501) staff       (20)     3411 2023-02-15 16:45:56.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/order.py
--rw-r--r--   0 cochise    (501) staff       (20)      671 2023-02-15 11:44:33.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/orderfinancialstatus.py
--rw-r--r--   0 cochise    (501) staff       (20)      567 2023-02-15 11:45:59.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/orderfulfillmentstatus.py
--rw-r--r--   0 cochise    (501) staff       (20)      502 2023-02-15 11:48:41.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/ordernoteattribute.py
--rw-r--r--   0 cochise    (501) staff       (20)      640 2023-02-15 11:52:32.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/orderprocessingmethod.py
--rw-r--r--   0 cochise    (501) staff       (20)      784 2023-02-15 12:41:30.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/product.py
--rw-r--r--   0 cochise    (501) staff       (20)     1164 2023-02-15 14:12:27.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/productvariant.py
--rw-r--r--   0 cochise    (501) staff       (20)     1420 2023-03-07 12:31:45.000000 headless-2.0.0a8/headless/ext/shopify/v2023_1/webhook.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.745001 headless-2.0.0a8/headless/ext/teamleader/
--rw-r--r--   0 cochise    (501) staff       (20)      585 2023-02-16 21:54:07.000000 headless-2.0.0a8/headless/ext/teamleader/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     1155 2023-02-16 22:00:41.000000 headless-2.0.0a8/headless/ext/teamleader/client.py
--rw-r--r--   0 cochise    (501) staff       (20)     1291 2023-02-16 21:53:52.000000 headless-2.0.0a8/headless/ext/teamleader/resource.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.746558 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/
--rw-r--r--   0 cochise    (501) staff       (20)      641 2023-02-16 21:26:31.000000 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)      847 2023-02-16 21:46:45.000000 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/currentuser.py
--rw-r--r--   0 cochise    (501) staff       (20)      492 2023-02-16 21:26:07.000000 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/customfieldconfiguration.py
--rw-r--r--   0 cochise    (501) staff       (20)      939 2023-02-16 21:46:00.000000 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/customfielddefinition.py
--rw-r--r--   0 cochise    (501) staff       (20)      749 2023-02-16 21:46:13.000000 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/product.py
--rw-r--r--   0 cochise    (501) staff       (20)      488 2023-02-16 21:00:37.000000 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/productprice.py
--rw-r--r--   0 cochise    (501) staff       (20)      754 2023-02-16 21:46:53.000000 headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/user.py
--rw-r--r--   0 cochise    (501) staff       (20)     1194 2023-03-13 11:54:18.000000 headless-2.0.0a8/headless/package.json
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.751120 headless-2.0.0a8/headless/types/
--rw-r--r--   0 cochise    (501) staff       (20)     1406 2023-03-05 11:37:13.000000 headless-2.0.0a8/headless/types/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)     1465 2023-02-14 23:36:57.000000 headless-2.0.0a8/headless/types/basicauth.py
--rw-r--r--   0 cochise    (501) staff       (20)    10143 2023-02-14 23:09:17.000000 headless-2.0.0a8/headless/types/headers.py
--rw-r--r--   0 cochise    (501) staff       (20)      662 2023-02-25 04:09:35.000000 headless-2.0.0a8/headless/types/hints.py
--rw-r--r--   0 cochise    (501) staff       (20)      901 2023-02-15 10:36:26.000000 headless-2.0.0a8/headless/types/ibackoff.py
--rw-r--r--   0 cochise    (501) staff       (20)    11485 2023-03-13 11:45:18.000000 headless-2.0.0a8/headless/types/iclient.py
--rw-r--r--   0 cochise    (501) staff       (20)      537 2023-02-15 10:36:12.000000 headless-2.0.0a8/headless/types/iclientlogger.py
--rw-r--r--   0 cochise    (501) staff       (20)     1708 2023-02-16 19:24:56.000000 headless-2.0.0a8/headless/types/icredential.py
--rw-r--r--   0 cochise    (501) staff       (20)     1716 2023-02-24 08:45:16.000000 headless-2.0.0a8/headless/types/irequest.py
--rw-r--r--   0 cochise    (501) staff       (20)     1093 2023-02-16 20:35:54.000000 headless-2.0.0a8/headless/types/iresource.py
--rw-r--r--   0 cochise    (501) staff       (20)      774 2023-02-25 03:18:09.000000 headless-2.0.0a8/headless/types/iresourcemeta.py
--rw-r--r--   0 cochise    (501) staff       (20)     2036 2023-02-16 17:12:22.000000 headless-2.0.0a8/headless/types/iresponse.py
--rw-r--r--   0 cochise    (501) staff       (20)      870 2023-02-15 10:34:22.000000 headless-2.0.0a8/headless/types/nullbackoff.py
--rw-r--r--   0 cochise    (501) staff       (20)      507 2023-02-14 23:21:41.000000 headless-2.0.0a8/headless/types/nullcredential.py
--rw-r--r--   0 cochise    (501) staff       (20)     1132 2023-02-18 23:07:39.000000 headless-2.0.0a8/headless/types/optionsresponse.py
--rw-r--r--   0 cochise    (501) staff       (20)      803 2023-02-15 16:35:27.000000 headless-2.0.0a8/headless/types/ratelimited.py
--rw-r--r--   0 cochise    (501) staff       (20)      465 2023-03-04 17:21:04.000000 headless-2.0.0a8/headless/types/readtimeout.py
--rw-r--r--   0 cochise    (501) staff       (20)     1619 2023-03-05 11:46:42.000000 headless-2.0.0a8/headless/types/resourcexception.py
--rw-r--r--   0 cochise    (501) staff       (20)      827 2023-03-05 11:46:32.000000 headless-2.0.0a8/headless/types/resourcexceptiontype.py
--rw-r--r--   0 cochise    (501) staff       (20)      824 2023-02-15 16:35:21.000000 headless-2.0.0a8/headless/types/serverdoesnotexist.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.718525 headless-2.0.0a8/headless.egg-info/
--rw-r--r--   0 cochise    (501) staff       (20)     1024 2023-03-13 22:16:00.000000 headless-2.0.0a8/headless.egg-info/PKG-INFO
--rw-r--r--   0 cochise    (501) staff       (20)     5298 2023-03-13 22:16:00.000000 headless-2.0.0a8/headless.egg-info/SOURCES.txt
--rw-r--r--   0 cochise    (501) staff       (20)        1 2023-03-13 22:16:00.000000 headless-2.0.0a8/headless.egg-info/dependency_links.txt
--rw-r--r--   0 cochise    (501) staff       (20)      152 2023-03-13 22:16:00.000000 headless-2.0.0a8/headless.egg-info/requires.txt
--rw-r--r--   0 cochise    (501) staff       (20)       50 2023-03-13 22:16:00.000000 headless-2.0.0a8/headless.egg-info/top_level.txt
--rw-r--r--   0 cochise    (501) staff       (20)       38 2023-03-13 22:16:00.752673 headless-2.0.0a8/setup.cfg
--rw-r--r--   0 cochise    (501) staff       (20)     1282 2022-04-18 13:48:19.000000 headless-2.0.0a8/setup.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.751353 headless-2.0.0a8/tests/
--rw-r--r--   0 cochise    (501) staff       (20)      394 2023-02-16 17:13:07.000000 headless-2.0.0a8/tests/__init__.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.751561 headless-2.0.0a8/tests/ext/
--rw-r--r--   0 cochise    (501) staff       (20)      394 2023-02-16 17:13:04.000000 headless-2.0.0a8/tests/ext/__init__.py
-drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-13 22:16:00.752183 headless-2.0.0a8/tests/ext/oauth2/
--rw-r--r--   0 cochise    (501) staff       (20)      394 2023-02-16 17:13:13.000000 headless-2.0.0a8/tests/ext/oauth2/__init__.py
--rw-r--r--   0 cochise    (501) staff       (20)      542 2023-02-16 17:34:30.000000 headless-2.0.0a8/tests/ext/oauth2/test_system_discover_google.py
--rw-r--r--   0 cochise    (501) staff       (20)     1144 2023-02-16 19:27:27.000000 headless-2.0.0a8/tests/ext/oauth2/test_system_discover_teamleader.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.796362 headless-2.0.0a9/
+-rw-r--r--   0 cochise    (501) staff       (20)      312 2022-04-18 13:38:41.000000 headless-2.0.0a9/MANIFEST.in
+-rw-r--r--   0 cochise    (501) staff       (20)     1024 2023-03-14 00:42:54.796208 headless-2.0.0a9/PKG-INFO
+-rw-r--r--   0 cochise    (501) staff       (20)        8 2023-03-14 00:42:35.000000 headless-2.0.0a9/VERSION
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.749734 headless-2.0.0a9/docs/
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.751443 headless-2.0.0a9/docs/source/
+-rw-r--r--   0 cochise    (501) staff       (20)     2420 2023-02-15 18:22:20.000000 headless-2.0.0a9/docs/source/conf.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.754967 headless-2.0.0a9/examples/
+-rw-r--r--   0 cochise    (501) staff       (20)     2294 2023-02-16 21:27:22.000000 headless-2.0.0a9/examples/oauth2-callback.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1199 2023-03-05 09:40:25.000000 headless-2.0.0a9/examples/picqer-create-receipt.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1175 2023-02-25 11:09:13.000000 headless-2.0.0a9/examples/picqer-list-products.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1021 2023-03-05 11:13:19.000000 headless-2.0.0a9/examples/picqer-list-receipts.py
+-rw-r--r--   0 cochise    (501) staff       (20)      962 2023-02-25 02:40:51.000000 headless-2.0.0a9/examples/picqer-list-webhooks.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1037 2023-02-15 18:43:26.000000 headless-2.0.0a9/examples/picqer-ratelimit.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1454 2023-02-15 18:49:26.000000 headless-2.0.0a9/examples/picqer-traverse-api.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1410 2023-02-25 11:07:22.000000 headless-2.0.0a9/examples/piqcer-list-picklist-products.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1013 2023-02-15 18:37:30.000000 headless-2.0.0a9/examples/shopify-get-orders.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1345 2023-02-15 13:53:15.000000 headless-2.0.0a9/examples/shopify-inspect-catalog.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1347 2023-02-15 18:40:52.000000 headless-2.0.0a9/examples/shopify-ratelimit.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1263 2023-02-15 14:24:51.000000 headless-2.0.0a9/examples/shopify-set-inventory.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.755325 headless-2.0.0a9/headless/
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.758229 headless-2.0.0a9/headless/core/
+-rw-r--r--   0 cochise    (501) staff       (20)      953 2023-02-15 17:12:49.000000 headless-2.0.0a9/headless/core/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1853 2023-02-15 17:38:48.000000 headless-2.0.0a9/headless/core/deferredresource.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.759392 headless-2.0.0a9/headless/core/httpx/
+-rw-r--r--   0 cochise    (501) staff       (20)      552 2023-02-14 23:49:28.000000 headless-2.0.0a9/headless/core/httpx/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2822 2023-03-13 22:09:16.000000 headless-2.0.0a9/headless/core/httpx/client.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1665 2023-02-24 08:45:08.000000 headless-2.0.0a9/headless/core/httpx/request.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1056 2023-02-16 17:12:22.000000 headless-2.0.0a9/headless/core/httpx/response.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2351 2023-02-15 15:00:27.000000 headless-2.0.0a9/headless/core/linearbackoff.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2559 2023-03-07 12:18:10.000000 headless-2.0.0a9/headless/core/resource.py
+-rw-r--r--   0 cochise    (501) staff       (20)     3489 2023-03-04 17:44:52.000000 headless-2.0.0a9/headless/core/resourcemeta.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2010 2023-02-15 17:10:28.000000 headless-2.0.0a9/headless/core/resourcemetaclass.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1577 2023-02-15 17:33:26.000000 headless-2.0.0a9/headless/core/resourcereference.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.750581 headless-2.0.0a9/headless/ext/
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.761260 headless-2.0.0a9/headless/ext/oauth2/
+-rw-r--r--   0 cochise    (501) staff       (20)      762 2023-02-22 22:42:27.000000 headless-2.0.0a9/headless/ext/oauth2/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)    11061 2023-03-13 11:57:19.000000 headless-2.0.0a9/headless/ext/oauth2/client.py
+-rw-r--r--   0 cochise    (501) staff       (20)     4758 2023-03-13 11:12:02.000000 headless-2.0.0a9/headless/ext/oauth2/clientcredential.py
+-rw-r--r--   0 cochise    (501) staff       (20)      508 2023-02-23 23:40:03.000000 headless-2.0.0a9/headless/ext/oauth2/const.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.766950 headless-2.0.0a9/headless/ext/oauth2/models/
+-rw-r--r--   0 cochise    (501) staff       (20)     1279 2023-02-23 01:55:37.000000 headless-2.0.0a9/headless/ext/oauth2/models/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     3082 2023-03-10 22:17:19.000000 headless-2.0.0a9/headless/ext/oauth2/models/address.py
+-rw-r--r--   0 cochise    (501) staff       (20)      486 2023-02-16 19:06:21.000000 headless-2.0.0a9/headless/ext/oauth2/models/authorizationcode.py
+-rw-r--r--   0 cochise    (501) staff       (20)      867 2023-02-16 19:14:27.000000 headless-2.0.0a9/headless/ext/oauth2/models/authorizationendpointresponse.py
+-rw-r--r--   0 cochise    (501) staff       (20)      410 2023-02-16 17:43:39.000000 headless-2.0.0a9/headless/ext/oauth2/models/authorizationrequest.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1374 2023-02-16 19:45:29.000000 headless-2.0.0a9/headless/ext/oauth2/models/bearertokencredential.py
+-rw-r--r--   0 cochise    (501) staff       (20)    11067 2023-03-13 22:41:33.000000 headless-2.0.0a9/headless/ext/oauth2/models/claimset.py
+-rw-r--r--   0 cochise    (501) staff       (20)      758 2023-02-16 18:23:04.000000 headless-2.0.0a9/headless/ext/oauth2/models/clientauthenticationmethod.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1460 2023-02-17 21:55:41.000000 headless-2.0.0a9/headless/ext/oauth2/models/clientcredentialsrequest.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1238 2023-03-12 12:00:13.000000 headless-2.0.0a9/headless/ext/oauth2/models/encodedidtoken.py
+-rw-r--r--   0 cochise    (501) staff       (20)      969 2023-02-17 22:00:21.000000 headless-2.0.0a9/headless/ext/oauth2/models/error.py
+-rw-r--r--   0 cochise    (501) staff       (20)      771 2023-02-17 21:44:52.000000 headless-2.0.0a9/headless/ext/oauth2/models/iobtainable.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1537 2023-02-22 22:45:49.000000 headless-2.0.0a9/headless/ext/oauth2/models/jsonwebtoken.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1434 2023-03-12 12:09:01.000000 headless-2.0.0a9/headless/ext/oauth2/models/oidctoken.py
+-rw-r--r--   0 cochise    (501) staff       (20)    22960 2023-02-16 18:33:24.000000 headless-2.0.0a9/headless/ext/oauth2/models/servermetadata.py
+-rw-r--r--   0 cochise    (501) staff       (20)      527 2023-02-23 02:59:59.000000 headless-2.0.0a9/headless/ext/oauth2/models/subjectidentifier.py
+-rw-r--r--   0 cochise    (501) staff       (20)      756 2023-03-12 11:49:38.000000 headless-2.0.0a9/headless/ext/oauth2/models/tokenresponse.py
+-rw-r--r--   0 cochise    (501) staff       (20)      496 2023-02-20 14:24:14.000000 headless-2.0.0a9/headless/ext/oauth2/nullcredential.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2888 2023-02-20 14:46:35.000000 headless-2.0.0a9/headless/ext/oauth2/server.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.767495 headless-2.0.0a9/headless/ext/oauth2/test/
+-rw-r--r--   0 cochise    (501) staff       (20)     1025 2023-02-16 17:38:32.000000 headless-2.0.0a9/headless/ext/oauth2/test/discovery.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1141 2023-02-16 18:47:29.000000 headless-2.0.0a9/headless/ext/oauth2/test/manual.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.768482 headless-2.0.0a9/headless/ext/oauth2/types/
+-rw-r--r--   0 cochise    (501) staff       (20)      593 2023-02-23 23:55:51.000000 headless-2.0.0a9/headless/ext/oauth2/types/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1002 2023-02-23 23:55:08.000000 headless-2.0.0a9/headless/ext/oauth2/types/granttype.py
+-rw-r--r--   0 cochise    (501) staff       (20)      688 2023-02-23 23:41:08.000000 headless-2.0.0a9/headless/ext/oauth2/types/responsemode.py
+-rw-r--r--   0 cochise    (501) staff       (20)      721 2023-02-23 23:34:47.000000 headless-2.0.0a9/headless/ext/oauth2/types/responsetype.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.769994 headless-2.0.0a9/headless/ext/picqer/
+-rw-r--r--   0 cochise    (501) staff       (20)      904 2023-03-04 17:15:23.000000 headless-2.0.0a9/headless/ext/picqer/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)      852 2023-02-15 16:21:24.000000 headless-2.0.0a9/headless/ext/picqer/client.py
+-rw-r--r--   0 cochise    (501) staff       (20)      933 2023-02-24 08:28:55.000000 headless-2.0.0a9/headless/ext/picqer/credential.py
+-rw-r--r--   0 cochise    (501) staff       (20)      751 2023-02-25 02:56:53.000000 headless-2.0.0a9/headless/ext/picqer/defaultclient.py
+-rw-r--r--   0 cochise    (501) staff       (20)      794 2023-02-24 00:17:46.000000 headless-2.0.0a9/headless/ext/picqer/environmentcredential.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.779133 headless-2.0.0a9/headless/ext/picqer/v1/
+-rw-r--r--   0 cochise    (501) staff       (20)      897 2023-03-04 17:15:11.000000 headless-2.0.0a9/headless/ext/picqer/v1/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2169 2023-02-25 02:43:12.000000 headless-2.0.0a9/headless/ext/picqer/v1/order.py
+-rw-r--r--   0 cochise    (501) staff       (20)      502 2023-02-15 01:04:25.000000 headless-2.0.0a9/headless/ext/picqer/v1/orderfield.py
+-rw-r--r--   0 cochise    (501) staff       (20)      598 2023-02-15 01:02:52.000000 headless-2.0.0a9/headless/ext/picqer/v1/orderproduct.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1819 2023-02-25 11:39:07.000000 headless-2.0.0a9/headless/ext/picqer/v1/picklist.py
+-rw-r--r--   0 cochise    (501) staff       (20)      754 2023-02-25 11:37:45.000000 headless-2.0.0a9/headless/ext/picqer/v1/picklistproduct.py
+-rw-r--r--   0 cochise    (501) staff       (20)      541 2023-02-25 11:38:27.000000 headless-2.0.0a9/headless/ext/picqer/v1/pickliststatus.py
+-rw-r--r--   0 cochise    (501) staff       (20)      900 2023-02-15 01:00:54.000000 headless-2.0.0a9/headless/ext/picqer/v1/pickuppointdata.py
+-rw-r--r--   0 cochise    (501) staff       (20)      863 2023-02-25 10:44:25.000000 headless-2.0.0a9/headless/ext/picqer/v1/picqerresource.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2379 2023-03-05 11:53:49.000000 headless-2.0.0a9/headless/ext/picqer/v1/product.py
+-rw-r--r--   0 cochise    (501) staff       (20)      506 2023-02-25 10:47:37.000000 headless-2.0.0a9/headless/ext/picqer/v1/productfield.py
+-rw-r--r--   0 cochise    (501) staff       (20)      494 2023-02-25 10:38:10.000000 headless-2.0.0a9/headless/ext/picqer/v1/productpricelist.py
+-rw-r--r--   0 cochise    (501) staff       (20)      609 2023-02-25 10:49:16.000000 headless-2.0.0a9/headless/ext/picqer/v1/productstock.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2719 2023-03-05 12:55:57.000000 headless-2.0.0a9/headless/ext/picqer/v1/purchaseorder.py
+-rw-r--r--   0 cochise    (501) staff       (20)      670 2023-02-14 22:38:36.000000 headless-2.0.0a9/headless/ext/picqer/v1/purchaseorderproduct.py
+-rw-r--r--   0 cochise    (501) staff       (20)     4582 2023-03-05 13:06:33.000000 headless-2.0.0a9/headless/ext/picqer/v1/receipt.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1011 2023-03-05 09:34:07.000000 headless-2.0.0a9/headless/ext/picqer/v1/receiptproduct.py
+-rw-r--r--   0 cochise    (501) staff       (20)      510 2023-03-04 17:12:15.000000 headless-2.0.0a9/headless/ext/picqer/v1/receiptpurchaseorder.py
+-rw-r--r--   0 cochise    (501) staff       (20)      496 2023-03-04 17:19:54.000000 headless-2.0.0a9/headless/ext/picqer/v1/receiptsupplier.py
+-rw-r--r--   0 cochise    (501) staff       (20)      864 2023-02-25 02:43:53.000000 headless-2.0.0a9/headless/ext/picqer/v1/supplier.py
+-rw-r--r--   0 cochise    (501) staff       (20)      567 2023-02-15 00:54:45.000000 headless-2.0.0a9/headless/ext/picqer/v1/tag.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1288 2023-02-25 02:44:05.000000 headless-2.0.0a9/headless/ext/picqer/v1/user.py
+-rw-r--r--   0 cochise    (501) staff       (20)      483 2023-03-04 17:14:15.000000 headless-2.0.0a9/headless/ext/picqer/v1/userreference.py
+-rw-r--r--   0 cochise    (501) staff       (20)      664 2023-02-25 02:44:16.000000 headless-2.0.0a9/headless/ext/picqer/v1/warehouse.py
+-rw-r--r--   0 cochise    (501) staff       (20)      624 2023-02-25 02:44:24.000000 headless-2.0.0a9/headless/ext/picqer/v1/webhook.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.780227 headless-2.0.0a9/headless/ext/shopify/
+-rw-r--r--   0 cochise    (501) staff       (20)      491 2023-02-15 11:20:07.000000 headless-2.0.0a9/headless/ext/shopify/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1143 2023-02-15 21:15:35.000000 headless-2.0.0a9/headless/ext/shopify/adminclient.py
+-rw-r--r--   0 cochise    (501) staff       (20)      781 2023-02-15 11:27:57.000000 headless-2.0.0a9/headless/ext/shopify/credential.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2157 2023-03-07 12:31:36.000000 headless-2.0.0a9/headless/ext/shopify/resource.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.784095 headless-2.0.0a9/headless/ext/shopify/v2023_1/
+-rw-r--r--   0 cochise    (501) staff       (20)      627 2023-03-07 11:53:32.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)      623 2023-02-15 11:36:40.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/clientdetails.py
+-rw-r--r--   0 cochise    (501) staff       (20)      550 2023-02-15 11:41:45.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/customer.py
+-rw-r--r--   0 cochise    (501) staff       (20)      795 2023-02-15 12:01:14.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/customeraddress.py
+-rw-r--r--   0 cochise    (501) staff       (20)      885 2023-02-15 14:19:15.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/inventorylevel.py
+-rw-r--r--   0 cochise    (501) staff       (20)     3411 2023-02-15 16:45:56.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/order.py
+-rw-r--r--   0 cochise    (501) staff       (20)      671 2023-02-15 11:44:33.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/orderfinancialstatus.py
+-rw-r--r--   0 cochise    (501) staff       (20)      567 2023-02-15 11:45:59.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/orderfulfillmentstatus.py
+-rw-r--r--   0 cochise    (501) staff       (20)      502 2023-02-15 11:48:41.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/ordernoteattribute.py
+-rw-r--r--   0 cochise    (501) staff       (20)      640 2023-02-15 11:52:32.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/orderprocessingmethod.py
+-rw-r--r--   0 cochise    (501) staff       (20)      784 2023-02-15 12:41:30.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/product.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1164 2023-02-15 14:12:27.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/productvariant.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1420 2023-03-07 12:31:45.000000 headless-2.0.0a9/headless/ext/shopify/v2023_1/webhook.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.785089 headless-2.0.0a9/headless/ext/teamleader/
+-rw-r--r--   0 cochise    (501) staff       (20)      585 2023-02-16 21:54:07.000000 headless-2.0.0a9/headless/ext/teamleader/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1155 2023-02-16 22:00:41.000000 headless-2.0.0a9/headless/ext/teamleader/client.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1291 2023-02-16 21:53:52.000000 headless-2.0.0a9/headless/ext/teamleader/resource.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.786902 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/
+-rw-r--r--   0 cochise    (501) staff       (20)      641 2023-02-16 21:26:31.000000 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)      847 2023-02-16 21:46:45.000000 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/currentuser.py
+-rw-r--r--   0 cochise    (501) staff       (20)      492 2023-02-16 21:26:07.000000 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/customfieldconfiguration.py
+-rw-r--r--   0 cochise    (501) staff       (20)      939 2023-02-16 21:46:00.000000 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/customfielddefinition.py
+-rw-r--r--   0 cochise    (501) staff       (20)      749 2023-02-16 21:46:13.000000 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/product.py
+-rw-r--r--   0 cochise    (501) staff       (20)      488 2023-02-16 21:00:37.000000 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/productprice.py
+-rw-r--r--   0 cochise    (501) staff       (20)      754 2023-02-16 21:46:53.000000 headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/user.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1194 2023-03-13 22:40:50.000000 headless-2.0.0a9/headless/package.json
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.794648 headless-2.0.0a9/headless/types/
+-rw-r--r--   0 cochise    (501) staff       (20)     1406 2023-03-05 11:37:13.000000 headless-2.0.0a9/headless/types/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1465 2023-02-14 23:36:57.000000 headless-2.0.0a9/headless/types/basicauth.py
+-rw-r--r--   0 cochise    (501) staff       (20)    10143 2023-02-14 23:09:17.000000 headless-2.0.0a9/headless/types/headers.py
+-rw-r--r--   0 cochise    (501) staff       (20)      662 2023-02-25 04:09:35.000000 headless-2.0.0a9/headless/types/hints.py
+-rw-r--r--   0 cochise    (501) staff       (20)      901 2023-02-15 10:36:26.000000 headless-2.0.0a9/headless/types/ibackoff.py
+-rw-r--r--   0 cochise    (501) staff       (20)    11485 2023-03-13 11:45:18.000000 headless-2.0.0a9/headless/types/iclient.py
+-rw-r--r--   0 cochise    (501) staff       (20)      537 2023-02-15 10:36:12.000000 headless-2.0.0a9/headless/types/iclientlogger.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1708 2023-02-16 19:24:56.000000 headless-2.0.0a9/headless/types/icredential.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1716 2023-02-24 08:45:16.000000 headless-2.0.0a9/headless/types/irequest.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1093 2023-02-16 20:35:54.000000 headless-2.0.0a9/headless/types/iresource.py
+-rw-r--r--   0 cochise    (501) staff       (20)      774 2023-02-25 03:18:09.000000 headless-2.0.0a9/headless/types/iresourcemeta.py
+-rw-r--r--   0 cochise    (501) staff       (20)     2036 2023-02-16 17:12:22.000000 headless-2.0.0a9/headless/types/iresponse.py
+-rw-r--r--   0 cochise    (501) staff       (20)      870 2023-02-15 10:34:22.000000 headless-2.0.0a9/headless/types/nullbackoff.py
+-rw-r--r--   0 cochise    (501) staff       (20)      507 2023-02-14 23:21:41.000000 headless-2.0.0a9/headless/types/nullcredential.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1132 2023-02-18 23:07:39.000000 headless-2.0.0a9/headless/types/optionsresponse.py
+-rw-r--r--   0 cochise    (501) staff       (20)      803 2023-02-15 16:35:27.000000 headless-2.0.0a9/headless/types/ratelimited.py
+-rw-r--r--   0 cochise    (501) staff       (20)      465 2023-03-04 17:21:04.000000 headless-2.0.0a9/headless/types/readtimeout.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1619 2023-03-05 11:46:42.000000 headless-2.0.0a9/headless/types/resourcexception.py
+-rw-r--r--   0 cochise    (501) staff       (20)      827 2023-03-05 11:46:32.000000 headless-2.0.0a9/headless/types/resourcexceptiontype.py
+-rw-r--r--   0 cochise    (501) staff       (20)      824 2023-02-15 16:35:21.000000 headless-2.0.0a9/headless/types/serverdoesnotexist.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.756264 headless-2.0.0a9/headless.egg-info/
+-rw-r--r--   0 cochise    (501) staff       (20)     1024 2023-03-14 00:42:54.000000 headless-2.0.0a9/headless.egg-info/PKG-INFO
+-rw-r--r--   0 cochise    (501) staff       (20)     5298 2023-03-14 00:42:54.000000 headless-2.0.0a9/headless.egg-info/SOURCES.txt
+-rw-r--r--   0 cochise    (501) staff       (20)        1 2023-03-14 00:42:54.000000 headless-2.0.0a9/headless.egg-info/dependency_links.txt
+-rw-r--r--   0 cochise    (501) staff       (20)      152 2023-03-14 00:42:54.000000 headless-2.0.0a9/headless.egg-info/requires.txt
+-rw-r--r--   0 cochise    (501) staff       (20)       50 2023-03-14 00:42:54.000000 headless-2.0.0a9/headless.egg-info/top_level.txt
+-rw-r--r--   0 cochise    (501) staff       (20)       38 2023-03-14 00:42:54.796404 headless-2.0.0a9/setup.cfg
+-rw-r--r--   0 cochise    (501) staff       (20)     1282 2022-04-18 13:48:19.000000 headless-2.0.0a9/setup.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.794986 headless-2.0.0a9/tests/
+-rw-r--r--   0 cochise    (501) staff       (20)      394 2023-02-16 17:13:07.000000 headless-2.0.0a9/tests/__init__.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.795206 headless-2.0.0a9/tests/ext/
+-rw-r--r--   0 cochise    (501) staff       (20)      394 2023-02-16 17:13:04.000000 headless-2.0.0a9/tests/ext/__init__.py
+drwxr-xr-x   0 cochise    (501) staff       (20)        0 2023-03-14 00:42:54.795889 headless-2.0.0a9/tests/ext/oauth2/
+-rw-r--r--   0 cochise    (501) staff       (20)      394 2023-02-16 17:13:13.000000 headless-2.0.0a9/tests/ext/oauth2/__init__.py
+-rw-r--r--   0 cochise    (501) staff       (20)      542 2023-02-16 17:34:30.000000 headless-2.0.0a9/tests/ext/oauth2/test_system_discover_google.py
+-rw-r--r--   0 cochise    (501) staff       (20)     1144 2023-02-16 19:27:27.000000 headless-2.0.0a9/tests/ext/oauth2/test_system_discover_teamleader.py
```

### Comparing `headless-2.0.0a8/PKG-INFO` & `headless-2.0.0a9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: headless
-Version: 2.0.0a8
+Version: 2.0.0a9
 Summary: Headless - API client framework
 Home-page: https://gitlab.com/unimatrixone/libraries/python-unimatrix/headless
 Author: Cochise Ruhulessin
 Author-email: cochise.ruhulessin@unimatrixone.io
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

### Comparing `headless-2.0.0a8/docs/source/conf.py` & `headless-2.0.0a9/docs/source/conf.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/oauth2-callback.py` & `headless-2.0.0a9/examples/oauth2-callback.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/picqer-create-receipt.py` & `headless-2.0.0a9/examples/picqer-create-receipt.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/picqer-list-products.py` & `headless-2.0.0a9/examples/picqer-list-products.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/picqer-list-receipts.py` & `headless-2.0.0a9/examples/picqer-list-receipts.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/picqer-list-webhooks.py` & `headless-2.0.0a9/examples/picqer-list-webhooks.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/picqer-ratelimit.py` & `headless-2.0.0a9/examples/picqer-ratelimit.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/picqer-traverse-api.py` & `headless-2.0.0a9/examples/picqer-traverse-api.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/piqcer-list-picklist-products.py` & `headless-2.0.0a9/examples/piqcer-list-picklist-products.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/shopify-get-orders.py` & `headless-2.0.0a9/examples/shopify-get-orders.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/shopify-inspect-catalog.py` & `headless-2.0.0a9/examples/shopify-inspect-catalog.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/shopify-ratelimit.py` & `headless-2.0.0a9/examples/shopify-ratelimit.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/examples/shopify-set-inventory.py` & `headless-2.0.0a9/examples/shopify-set-inventory.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/__init__.py` & `headless-2.0.0a9/headless/core/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/deferredresource.py` & `headless-2.0.0a9/headless/core/deferredresource.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/httpx/__init__.py` & `headless-2.0.0a9/headless/core/httpx/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/httpx/client.py` & `headless-2.0.0a9/headless/core/httpx/client.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/httpx/request.py` & `headless-2.0.0a9/headless/core/httpx/request.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/httpx/response.py` & `headless-2.0.0a9/headless/core/httpx/response.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/linearbackoff.py` & `headless-2.0.0a9/headless/core/linearbackoff.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/resource.py` & `headless-2.0.0a9/headless/core/resource.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/resourcemeta.py` & `headless-2.0.0a9/headless/core/resourcemeta.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/resourcemetaclass.py` & `headless-2.0.0a9/headless/core/resourcemetaclass.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/core/resourcereference.py` & `headless-2.0.0a9/headless/core/resourcereference.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/__init__.py` & `headless-2.0.0a9/headless/ext/oauth2/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/client.py` & `headless-2.0.0a9/headless/ext/oauth2/client.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/clientcredential.py` & `headless-2.0.0a9/headless/ext/oauth2/clientcredential.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/__init__.py` & `headless-2.0.0a9/headless/ext/oauth2/models/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/address.py` & `headless-2.0.0a9/headless/ext/oauth2/models/address.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/authorizationendpointresponse.py` & `headless-2.0.0a9/headless/ext/oauth2/models/authorizationendpointresponse.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/bearertokencredential.py` & `headless-2.0.0a9/headless/ext/oauth2/models/bearertokencredential.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/claimset.py` & `headless-2.0.0a9/headless/ext/oauth2/models/claimset.py`

 * *Files 0% similar despite different names*

```diff
@@ -268,15 +268,15 @@
         email_verified = values.setdefault('email_verified', False)
         iss: str | None = values.get('iss')
         if email and iss is not None:
             assert isinstance(email, EmailAddress)
             if email_verified:
                 values['email_verified'] = iss in TRUSTED_ISSUERS
             else:
-                p = urllib.parse.urlparse(iss)
+                p = urllib.parse.urlparse(str(iss))
                 values['email_verified'] = email.domain in TRUSTED_DOMAINS[p.netloc]
 
         return values
 
     @pydantic.validator('locale')
     def preprocess_locale(cls, value: str | None) -> str | None:
         if value is not None:
```

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/clientauthenticationmethod.py` & `headless-2.0.0a9/headless/ext/oauth2/models/clientauthenticationmethod.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/clientcredentialsrequest.py` & `headless-2.0.0a9/headless/ext/oauth2/models/clientcredentialsrequest.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/encodedidtoken.py` & `headless-2.0.0a9/headless/ext/oauth2/models/encodedidtoken.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/error.py` & `headless-2.0.0a9/headless/ext/oauth2/models/error.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/iobtainable.py` & `headless-2.0.0a9/headless/ext/oauth2/models/iobtainable.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/jsonwebtoken.py` & `headless-2.0.0a9/headless/ext/oauth2/models/jsonwebtoken.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/oidctoken.py` & `headless-2.0.0a9/headless/ext/oauth2/models/oidctoken.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/servermetadata.py` & `headless-2.0.0a9/headless/ext/oauth2/models/servermetadata.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/subjectidentifier.py` & `headless-2.0.0a9/headless/ext/oauth2/models/subjectidentifier.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/models/tokenresponse.py` & `headless-2.0.0a9/headless/ext/oauth2/models/tokenresponse.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/server.py` & `headless-2.0.0a9/headless/ext/oauth2/server.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/test/discovery.py` & `headless-2.0.0a9/headless/ext/oauth2/test/discovery.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/test/manual.py` & `headless-2.0.0a9/headless/ext/oauth2/test/manual.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/types/__init__.py` & `headless-2.0.0a9/headless/ext/oauth2/types/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/types/granttype.py` & `headless-2.0.0a9/headless/ext/oauth2/types/granttype.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/types/responsemode.py` & `headless-2.0.0a9/headless/ext/oauth2/types/responsemode.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/oauth2/types/responsetype.py` & `headless-2.0.0a9/headless/ext/oauth2/types/responsetype.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/__init__.py` & `headless-2.0.0a9/headless/ext/picqer/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/client.py` & `headless-2.0.0a9/headless/ext/picqer/client.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/credential.py` & `headless-2.0.0a9/headless/ext/picqer/credential.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/defaultclient.py` & `headless-2.0.0a9/headless/ext/picqer/defaultclient.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/environmentcredential.py` & `headless-2.0.0a9/headless/ext/picqer/environmentcredential.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/__init__.py` & `headless-2.0.0a9/headless/ext/picqer/v1/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/order.py` & `headless-2.0.0a9/headless/ext/picqer/v1/order.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/orderproduct.py` & `headless-2.0.0a9/headless/ext/picqer/v1/orderproduct.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/picklist.py` & `headless-2.0.0a9/headless/ext/picqer/v1/picklist.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/picklistproduct.py` & `headless-2.0.0a9/headless/ext/picqer/v1/picklistproduct.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/pickliststatus.py` & `headless-2.0.0a9/headless/ext/picqer/v1/pickliststatus.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/pickuppointdata.py` & `headless-2.0.0a9/headless/ext/picqer/v1/pickuppointdata.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/picqerresource.py` & `headless-2.0.0a9/headless/ext/picqer/v1/picqerresource.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/product.py` & `headless-2.0.0a9/headless/ext/picqer/v1/product.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/productstock.py` & `headless-2.0.0a9/headless/ext/picqer/v1/productstock.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/purchaseorder.py` & `headless-2.0.0a9/headless/ext/picqer/v1/purchaseorder.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/purchaseorderproduct.py` & `headless-2.0.0a9/headless/ext/picqer/v1/purchaseorderproduct.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/receipt.py` & `headless-2.0.0a9/headless/ext/picqer/v1/receipt.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/receiptproduct.py` & `headless-2.0.0a9/headless/ext/picqer/v1/receiptproduct.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/supplier.py` & `headless-2.0.0a9/headless/ext/picqer/v1/supplier.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/tag.py` & `headless-2.0.0a9/headless/ext/picqer/v1/tag.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/user.py` & `headless-2.0.0a9/headless/ext/picqer/v1/user.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/warehouse.py` & `headless-2.0.0a9/headless/ext/picqer/v1/warehouse.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/picqer/v1/webhook.py` & `headless-2.0.0a9/headless/ext/picqer/v1/webhook.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/adminclient.py` & `headless-2.0.0a9/headless/ext/shopify/adminclient.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/credential.py` & `headless-2.0.0a9/headless/ext/shopify/credential.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/resource.py` & `headless-2.0.0a9/headless/ext/shopify/resource.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/__init__.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/clientdetails.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/clientdetails.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/customer.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/customer.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/customeraddress.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/customeraddress.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/inventorylevel.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/inventorylevel.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/order.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/order.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/orderfinancialstatus.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/orderfinancialstatus.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/orderfulfillmentstatus.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/orderfulfillmentstatus.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/orderprocessingmethod.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/orderprocessingmethod.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/product.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/product.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/productvariant.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/productvariant.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/shopify/v2023_1/webhook.py` & `headless-2.0.0a9/headless/ext/shopify/v2023_1/webhook.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/__init__.py` & `headless-2.0.0a9/headless/ext/teamleader/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/client.py` & `headless-2.0.0a9/headless/ext/teamleader/client.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/resource.py` & `headless-2.0.0a9/headless/ext/teamleader/resource.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/__init__.py` & `headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/currentuser.py` & `headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/currentuser.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/customfielddefinition.py` & `headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/customfielddefinition.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/product.py` & `headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/product.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/ext/teamleader/v2022_09_15/user.py` & `headless-2.0.0a9/headless/ext/teamleader/v2022_09_15/user.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/package.json` & `headless-2.0.0a9/headless/package.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.96875%*

 * *Differences: {"'install_requires'": "{insert: [(0, 'canonical>=0.29.0')], delete: [0]}"}*

```diff
@@ -37,14 +37,14 @@
             "httpx"
         ],
         "xml": [
             "lxml"
         ]
     },
     "install_requires": [
-        "canonical>=0.24.1",
+        "canonical>=0.29.0",
         "ckms>=0.61.0",
         "inflect"
     ],
     "licenses": "Proprietary",
     "url": "https://gitlab.com/unimatrixone/libraries/python-unimatrix/headless"
 }
```

### Comparing `headless-2.0.0a8/headless/types/__init__.py` & `headless-2.0.0a9/headless/types/__init__.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/basicauth.py` & `headless-2.0.0a9/headless/types/basicauth.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/headers.py` & `headless-2.0.0a9/headless/types/headers.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/hints.py` & `headless-2.0.0a9/headless/types/hints.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/ibackoff.py` & `headless-2.0.0a9/headless/types/ibackoff.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/iclient.py` & `headless-2.0.0a9/headless/types/iclient.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/iclientlogger.py` & `headless-2.0.0a9/headless/types/iclientlogger.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/icredential.py` & `headless-2.0.0a9/headless/types/icredential.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/irequest.py` & `headless-2.0.0a9/headless/types/irequest.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/iresource.py` & `headless-2.0.0a9/headless/types/iresource.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/iresourcemeta.py` & `headless-2.0.0a9/headless/types/iresourcemeta.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/iresponse.py` & `headless-2.0.0a9/headless/types/iresponse.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/nullbackoff.py` & `headless-2.0.0a9/headless/types/nullbackoff.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/optionsresponse.py` & `headless-2.0.0a9/headless/types/optionsresponse.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/ratelimited.py` & `headless-2.0.0a9/headless/types/ratelimited.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/resourcexception.py` & `headless-2.0.0a9/headless/types/resourcexception.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/resourcexceptiontype.py` & `headless-2.0.0a9/headless/types/resourcexceptiontype.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless/types/serverdoesnotexist.py` & `headless-2.0.0a9/headless/types/serverdoesnotexist.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/headless.egg-info/PKG-INFO` & `headless-2.0.0a9/headless.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: headless
-Version: 2.0.0a8
+Version: 2.0.0a9
 Summary: Headless - API client framework
 Home-page: https://gitlab.com/unimatrixone/libraries/python-unimatrix/headless
 Author: Cochise Ruhulessin
 Author-email: cochise.ruhulessin@unimatrixone.io
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

### Comparing `headless-2.0.0a8/headless.egg-info/SOURCES.txt` & `headless-2.0.0a9/headless.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/setup.py` & `headless-2.0.0a9/setup.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/tests/ext/oauth2/test_system_discover_google.py` & `headless-2.0.0a9/tests/ext/oauth2/test_system_discover_google.py`

 * *Files identical despite different names*

### Comparing `headless-2.0.0a8/tests/ext/oauth2/test_system_discover_teamleader.py` & `headless-2.0.0a9/tests/ext/oauth2/test_system_discover_teamleader.py`

 * *Files identical despite different names*

