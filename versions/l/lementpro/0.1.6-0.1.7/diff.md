# Comparing `tmp/lementpro-0.1.6.tar.gz` & `tmp/lementpro-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lementpro-0.1.6.tar", last modified: Mon Apr  3 10:50:17 2023, max compression
+gzip compressed data, was "lementpro-0.1.7.tar", last modified: Thu Apr  6 10:59:56 2023, max compression
```

## Comparing `lementpro-0.1.6.tar` & `lementpro-0.1.7.tar`

### file list

```diff
@@ -1,380 +1,380 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:17.620984 lementpro-0.1.6/
--rw-rw-rw-   0        0        0      583 2023-04-03 10:50:17.620984 lementpro-0.1.6/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:13.739354 lementpro-0.1.6/lementpro/
--rw-rw-rw-   0        0        0      647 2023-04-03 10:22:22.000000 lementpro-0.1.6/lementpro/__init__.py
--rw-rw-rw-   0        0        0     1559 2023-04-03 08:14:39.000000 lementpro-0.1.6/lementpro/builders.py
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:17.312445 lementpro-0.1.6/lementpro/data/
--rw-rw-rw-   0        0        0        0 2023-04-03 07:58:25.000000 lementpro-0.1.6/lementpro/data/__init__.py
--rw-rw-rw-   0        0        0      206 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/accesstokenmodel.py
--rw-rw-rw-   0        0        0      349 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/actionlogentryinfomodel.py
--rw-rw-rw-   0        0        0      594 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributeaddmodel.py
--rw-rw-rw-   0        0        0      613 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributeaddrelationmodel.py
--rw-rw-rw-   0        0        0      147 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributeaddresultmodel.py
--rw-rw-rw-   0        0        0      682 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributeextendedmodel.py
--rw-rw-rw-   0        0        0      547 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributeinfomodel.py
--rw-rw-rw-   0        0        0      254 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributepagingmodel.py
--rw-rw-rw-   0        0        0      577 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributepatchmodel.py
--rw-rw-rw-   0        0        0      700 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributepatchrelationmodel.py
--rw-rw-rw-   0        0        0      699 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/attributerelationinfomodel.py
--rw-rw-rw-   0        0        0      181 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/changepasswordmodel.py
--rw-rw-rw-   0        0        0      277 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/checkconnectionmodel.py
--rw-rw-rw-   0        0        0      202 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/checkconnectionresultmodel.py
--rw-rw-rw-   0        0        0      399 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/commentaddbyusermodel.py
--rw-rw-rw-   0        0        0      145 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/data/commentaddresultmodel.py
--rw-rw-rw-   0        0        0      378 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/commentemailextensionmodel.py
--rw-rw-rw-   0        0        0      391 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/commentextensionmodel.py
--rw-rw-rw-   0        0        0      315 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/commentpatchmodel.py
--rw-rw-rw-   0        0        0      245 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companycontactdetailsmodel.py
--rw-rw-rw-   0        0        0      250 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companycontactdetailspatchmodel.py
--rw-rw-rw-   0        0        0      211 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companyextensionmodel.py
--rw-rw-rw-   0        0        0      227 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companyinfodetailedmodel.py
--rw-rw-rw-   0        0        0     1157 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companyinfoextendedmodel.py
--rw-rw-rw-   0        0        0      374 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companyinfomodel.py
--rw-rw-rw-   0        0        0      213 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companylicensemodel.py
--rw-rw-rw-   0        0        0      308 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companymailboxaddmodel.py
--rw-rw-rw-   0        0        0      152 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companymailboxaddresultmodel.py
--rw-rw-rw-   0        0        0      334 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companymailboxextendedmodel.py
--rw-rw-rw-   0        0        0      310 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companymailboxpatchmodel.py
--rw-rw-rw-   0        0        0      286 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companypasswordpolicymodel.py
--rw-rw-rw-   0        0        0      291 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companypasswordpolicypatchmodel.py
--rw-rw-rw-   0        0        0      747 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/companypatchmodel.py
--rw-rw-rw-   0        0        0      276 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentaddmodel.py
--rw-rw-rw-   0        0        0      148 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentaddresultmodel.py
--rw-rw-rw-   0        0        0      150 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentbosssetmodel.py
--rw-rw-rw-   0        0        0      683 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentbossuserinfomodel.py
--rw-rw-rw-   0        0        0      679 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentinfoextendedmodel.py
--rw-rw-rw-   0        0        0      548 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentinfomodel.py
--rw-rw-rw-   0        0        0      255 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentpagingmodel.py
--rw-rw-rw-   0        0        0      279 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmenttreemodel.py
--rw-rw-rw-   0        0        0      307 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/departmentupdatemodel.py
--rw-rw-rw-   0        0        0      369 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/emailaddressmodel.py
--rw-rw-rw-   0        0        0      187 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/errorresponse.py
--rw-rw-rw-   0        0        0      139 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/etaginfomodel.py
--rw-rw-rw-   0        0        0      457 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/fileinfomodel.py
--rw-rw-rw-   0        0        0      253 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/fileinfopagingmodel.py
--rw-rw-rw-   0        0        0      465 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/fileuploadresultmodel.py
--rw-rw-rw-   0        0        0      183 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderaddobjectstatefilter.py
--rw-rw-rw-   0        0        0      205 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderaddobjectstatusfilter.py
--rw-rw-rw-   0        0        0      296 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderaddobjectuserfilter.py
--rw-rw-rw-   0        0        0      144 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderaddresultmodel.py
--rw-rw-rw-   0        0        0      281 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderattributepredicatemodel.py
--rw-rw-rw-   0        0        0      325 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderfilterbyattributemodel.py
--rw-rw-rw-   0        0        0      223 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldergroupbyattributemodel.py
--rw-rw-rw-   0        0        0      169 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldergroupinfomodel.py
--rw-rw-rw-   0        0        0      428 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderinfomodel.py
--rw-rw-rw-   0        0        0      225 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderjoinbyattributemodel.py
--rw-rw-rw-   0        0        0      207 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderobjecttypeinfomodel.py
--rw-rw-rw-   0        0        0      183 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderobjecttypemodel.py
--rw-rw-rw-   0        0        0      246 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderorderbyattributemodel.py
--rw-rw-rw-   0        0        0      251 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderpagingmodel.py
--rw-rw-rw-   0        0        0      150 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderpatchgroupmodel.py
--rw-rw-rw-   0        0        0      185 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderpatchobjectstatefilter.py
--rw-rw-rw-   0        0        0      207 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderpatchobjectstatusfilter.py
--rw-rw-rw-   0        0        0      298 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderpatchobjectuserfilter.py
--rw-rw-rw-   0        0        0      301 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderpatchreset.py
--rw-rw-rw-   0        0        0      156 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldertemplateaddgroupmodel.py
--rw-rw-rw-   0        0        0     1118 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldertemplateaddmodel.py
--rw-rw-rw-   0        0        0     1254 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldertemplateextendedmodel.py
--rw-rw-rw-   0        0        0     1176 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldertemplatepatchmodel.py
--rw-rw-rw-   0        0        0      419 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldertemplatesmenuproxymodel.py
--rw-rw-rw-   0        0        0      379 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/foldertemplatestreeproxymodel.py
--rw-rw-rw-   0        0        0      177 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/folderusertreecountmodel.py
--rw-rw-rw-   0        0        0      198 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupaddmodel.py
--rw-rw-rw-   0        0        0      143 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupaddresultmodel.py
--rw-rw-rw-   0        0        0      644 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupinfoextendedproxymodel.py
--rw-rw-rw-   0        0        0      357 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupinfomodel.py
--rw-rw-rw-   0        0        0      210 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupobjectexpirationaddmodel.py
--rw-rw-rw-   0        0        0      159 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupobjectexpirationaddresultmodel.py
--rw-rw-rw-   0        0        0      258 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupobjectexpirationinfomodel.py
--rw-rw-rw-   0        0        0      187 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupobjectexpirationpatchmodel.py
--rw-rw-rw-   0        0        0      254 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupobjecttypeinfomodel.py
--rw-rw-rw-   0        0        0      260 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupobjecttypepagingmodel.py
--rw-rw-rw-   0        0        0      184 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupobjecttypeupsertmodel.py
--rw-rw-rw-   0        0        0      250 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/grouppagingmodel.py
--rw-rw-rw-   0        0        0      360 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/groupupdateproxymodel.py
--rw-rw-rw-   0        0        0      319 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxactionaddmodel.py
--rw-rw-rw-   0        0        0      200 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxactionaddresultmodel.py
--rw-rw-rw-   0        0        0      344 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxactionextendedmodel.py
--rw-rw-rw-   0        0        0      283 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxactionpatchmodel.py
--rw-rw-rw-   0        0        0      311 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxaddmodel.py
--rw-rw-rw-   0        0        0      156 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxaddresultmodel.py
--rw-rw-rw-   0        0        0      337 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxextendedmodel.py
--rw-rw-rw-   0        0        0      333 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxinfomodel.py
--rw-rw-rw-   0        0        0      263 2023-04-03 08:20:46.000000 lementpro-0.1.6/lementpro/data/integrationmailboxpagingmodel.py
--rw-rw-rw-   0        0        0      313 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/integrationmailboxpatchmodel.py
--rw-rw-rw-   0        0        0      186 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/integrationmailboxrulemodel.py
--rw-rw-rw-   0        0        0      160 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/languagemodel.py
--rw-rw-rw-   0        0        0      284 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphgetschemaresponse.py
--rw-rw-rw-   0        0        0      315 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemaadddraftrequest.py
--rw-rw-rw-   0        0        0      283 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemaaddrequest.py
--rw-rw-rw-   0        0        0      350 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemaaddrequesttransitionactionmodel.py
--rw-rw-rw-   0        0        0      428 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemaaddrequesttransitionconditionmodel.py
--rw-rw-rw-   0        0        0      320 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemaaddrequesttransitionconditionpredicatemodel.py
--rw-rw-rw-   0        0        0      588 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemaelementmodel.py
--rw-rw-rw-   0        0        0      217 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemaline.py
--rw-rw-rw-   0        0        0      160 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemapoint.py
--rw-rw-rw-   0        0        0      301 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemarelatedproperty.py
--rw-rw-rw-   0        0        0      820 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschematransitionmodel.py
--rw-rw-rw-   0        0        0      172 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemauserreference.py
--rw-rw-rw-   0        0        0      345 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/mxgraphschemavariablemodel.py
--rw-rw-rw-   0        0        0      144 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objectaddresultmodel.py
--rw-rw-rw-   0        0        0      210 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objectattributemodel.py
--rw-rw-rw-   0        0        0      223 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeaddcountermodel.py
--rw-rw-rw-   0        0        0      175 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeaddextensionmodel.py
--rw-rw-rw-   0        0        0      622 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeaddmodel.py
--rw-rw-rw-   0        0        0      148 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeaddresultmodel.py
--rw-rw-rw-   0        0        0      256 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeaddformulamodel.py
--rw-rw-rw-   0        0        0      536 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeaddproxymodel.py
--rw-rw-rw-   0        0        0      157 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeaddresultmodel.py
--rw-rw-rw-   0        0        0      674 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeaddsettingsmodel.py
--rw-rw-rw-   0        0        0      915 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeextendedmodel.py
--rw-rw-rw-   0        0        0      720 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeinfoattributemodel.py
--rw-rw-rw-   0        0        0      312 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeinfoattributerelationmodel.py
--rw-rw-rw-   0        0        0      257 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeinfoformulamodel.py
--rw-rw-rw-   0        0        0      754 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeinfomodel.py
--rw-rw-rw-   0        0        0      675 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeinfosettingsmodel.py
--rw-rw-rw-   0        0        0      191 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeinfovaluelistentrymodel.py
--rw-rw-rw-   0        0        0      186 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributeinfovaluelistmodel.py
--rw-rw-rw-   0        0        0      264 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributepagingmodel.py
--rw-rw-rw-   0        0        0      258 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributepatchformulamodel.py
--rw-rw-rw-   0        0        0      516 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributepatchmodel.py
--rw-rw-rw-   0        0        0      676 2023-04-03 08:20:47.000000 lementpro-0.1.6/lementpro/data/objecttypeattributepatchsettingsmodel.py
--rw-rw-rw-   0        0        0      241 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypebimaddproxymodel.py
--rw-rw-rw-   0        0        0      151 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypebimaddresultmodel.py
--rw-rw-rw-   0        0        0      295 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypebiminfoextendedmodel.py
--rw-rw-rw-   0        0        0      238 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypebimpatchmodel.py
--rw-rw-rw-   0        0        0      178 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypebreadcrumbmodel.py
--rw-rw-rw-   0        0        0      237 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypecheckpointaddproxymodel.py
--rw-rw-rw-   0        0        0      158 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypecheckpointaddresultmodel.py
--rw-rw-rw-   0        0        0      291 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypecheckpointinfoextendedmodel.py
--rw-rw-rw-   0        0        0      289 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypecheckpointinfopagingmodel.py
--rw-rw-rw-   0        0        0      265 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypecheckpointpagingmodel.py
--rw-rw-rw-   0        0        0      234 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypecheckpointpatchmodel.py
--rw-rw-rw-   0        0        0      202 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeextensionmodel.py
--rw-rw-rw-   0        0        0      207 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypefileinfopagingmodel.py
--rw-rw-rw-   0        0        0      259 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypefilepagingmodel.py
--rw-rw-rw-   0        0        0      155 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypefileupsertmodel.py
--rw-rw-rw-   0        0        0      265 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeinfodetailedbimmodel.py
--rw-rw-rw-   0        0        0      252 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeinfodetailedcountermodel.py
--rw-rw-rw-   0        0        0      179 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeinfodetailedfilemodel.py
--rw-rw-rw-   0        0        0      365 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeinfodetailedmenumodel.py
--rw-rw-rw-   0        0        0      603 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeinfodetailedmodel.py
--rw-rw-rw-   0        0        0      767 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeinfoextendedmodel.py
--rw-rw-rw-   0        0        0      595 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeinfopagingmodel.py
--rw-rw-rw-   0        0        0      258 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypemenuaddproxymodel.py
--rw-rw-rw-   0        0        0      152 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypemenuaddresultmodel.py
--rw-rw-rw-   0        0        0      422 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypemenuinfoextendedmodel.py
--rw-rw-rw-   0        0        0      420 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypemenuinfopagingmodel.py
--rw-rw-rw-   0        0        0      283 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypemenupatchmodel.py
--rw-rw-rw-   0        0        0      255 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypepagingmodel.py
--rw-rw-rw-   0        0        0      225 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypepatchcountermodel.py
--rw-rw-rw-   0        0        0      177 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypepatchextensionmodel.py
--rw-rw-rw-   0        0        0      638 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypepatchmodel.py
--rw-rw-rw-   0        0        0      257 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypetreenodeproxymodel.py
--rw-rw-rw-   0        0        0     1045 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponse.py
--rw-rw-rw-   0        0        0      172 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponsecreatepage.py
--rw-rw-rw-   0        0        0      268 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponsecreatepageattribute.py
--rw-rw-rw-   0        0        0      197 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponsedetailedpage.py
--rw-rw-rw-   0        0        0      306 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponsedetailedpageattribute.py
--rw-rw-rw-   0        0        0      264 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponsedetailedpagetab.py
--rw-rw-rw-   0        0        0      170 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponseeditpage.py
--rw-rw-rw-   0        0        0      266 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponseeditpageattribute.py
--rw-rw-rw-   0        0        0      172 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponselistview.py
--rw-rw-rw-   0        0        0      293 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponselistviewattribute.py
--rw-rw-rw-   0        0        0      172 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponsetableview.py
--rw-rw-rw-   0        0        0      267 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponsetableviewattribute.py
--rw-rw-rw-   0        0        0      184 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objectuserfavoritemodel.py
--rw-rw-rw-   0        0        0      151 2023-04-03 08:20:48.000000 lementpro-0.1.6/lementpro/data/objectuserreadmodel.py
--rw-rw-rw-   0        0        0      153 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/objectuserunreadmodel.py
--rw-rw-rw-   0        0        0      252 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/pagingmodel.py
--rw-rw-rw-   0        0        0      151 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/refreshtokenmodel.py
--rw-rw-rw-   0        0        0      522 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/relatedobjectmodel.py
--rw-rw-rw-   0        0        0      273 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/relationvalue.py
--rw-rw-rw-   0        0        0      174 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/restorepasswordmodel.py
--rw-rw-rw-   0        0        0      160 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeactivitybuttonrequest.py
--rw-rw-rw-   0        0        0      222 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeextendedresponseactivityelement.py
--rw-rw-rw-   0        0        0      501 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeextendedresponseactivityvariable.py
--rw-rw-rw-   0        0        0      220 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeextendedresponsereferenceobject.py
--rw-rw-rw-   0        0        0      252 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeextendedresponsereferenceobjectproperty.py
--rw-rw-rw-   0        0        0      460 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeinforesponse.py
--rw-rw-rw-   0        0        0      255 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeinforesponseschema.py
--rw-rw-rw-   0        0        0      359 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routeinforesponseschemaversion.py
--rw-rw-rw-   0        0        0      253 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/routepagingresponse.py
--rw-rw-rw-   0        0        0      220 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/schemaaddresponse.py
--rw-rw-rw-   0        0        0      327 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/schemaextendedresponse.py
--rw-rw-rw-   0        0        0      278 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/schemainforesponse.py
--rw-rw-rw-   0        0        0      260 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/schemainforesponseversion.py
--rw-rw-rw-   0        0        0      254 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/schemapagingresponse.py
--rw-rw-rw-   0        0        0      259 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationaddmodel.py
--rw-rw-rw-   0        0        0      156 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationaddresultmodel.py
--rw-rw-rw-   0        0        0      196 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationinfodetailedmodel.py
--rw-rw-rw-   0        0        0      473 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationinfoextendedmodel.py
--rw-rw-rw-   0        0        0      313 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationinfopagingmodel.py
--rw-rw-rw-   0        0        0      209 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationinfoparammodel.py
--rw-rw-rw-   0        0        0      208 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationobjecttypeaddmodel.py
--rw-rw-rw-   0        0        0      166 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationobjecttypeaddresultmodel.py
--rw-rw-rw-   0        0        0      237 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationobjecttypeinfoextendedmodel.py
--rw-rw-rw-   0        0        0      235 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationobjecttypeinfopagingmodel.py
--rw-rw-rw-   0        0        0      273 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationobjecttypepagingmodel.py
--rw-rw-rw-   0        0        0      172 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationobjecttypepatchmodel.py
--rw-rw-rw-   0        0        0      263 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationpagingmodel.py
--rw-rw-rw-   0        0        0      246 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationparamaddmodel.py
--rw-rw-rw-   0        0        0      161 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationparamaddresultmodel.py
--rw-rw-rw-   0        0        0      275 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationparaminfoextendedmodel.py
--rw-rw-rw-   0        0        0      273 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationparaminfopagingmodel.py
--rw-rw-rw-   0        0        0      268 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationparampagingmodel.py
--rw-rw-rw-   0        0        0      210 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationparampatchmodel.py
--rw-rw-rw-   0        0        0      261 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/serviceintegrationpatchmodel.py
--rw-rw-rw-   0        0        0      199 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/setobjecttyperequest.py
--rw-rw-rw-   0        0        0      190 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/setsortweightmodel.py
--rw-rw-rw-   0        0        0      169 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/signinproxymodel.py
--rw-rw-rw-   0        0        0      258 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/statisticspagingresponse.py
--rw-rw-rw-   0        0        0      453 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/statisticsrecordinforesponse.py
--rw-rw-rw-   0        0        0      163 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/timezoneinfomodel.py
--rw-rw-rw-   0        0        0      253 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/timezonepagingmodel.py
--rw-rw-rw-   0        0        0      138 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/tobccmodel.py
--rw-rw-rw-   0        0        0      137 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/toccmodel.py
--rw-rw-rw-   0        0        0      141 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/toemailsmodel.py
--rw-rw-rw-   0        0        0      270 2023-04-03 07:58:25.000000 lementpro-0.1.6/lementpro/data/user.py
--rw-rw-rw-   0        0        0      669 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/useraddmodel.py
--rw-rw-rw-   0        0        0      142 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/useraddresultmodel.py
--rw-rw-rw-   0        0        0      151 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/userassistantaddresultmodel.py
--rw-rw-rw-   0        0        0      156 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/userdepartmentmoveproxymodel.py
--rw-rw-rw-   0        0        0      254 2023-04-03 08:20:49.000000 lementpro-0.1.6/lementpro/data/userdetailedmodeldepartment.py
--rw-rw-rw-   0        0        0      195 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userdetailedmodelgroup.py
--rw-rw-rw-   0        0        0      464 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userdetailedmodelnotification.py
--rw-rw-rw-   0        0        0     1144 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userfolderaddmodel.py
--rw-rw-rw-   0        0        0     1306 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userfolderextendedmodel.py
--rw-rw-rw-   0        0        0      458 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userfolderinfomodel.py
--rw-rw-rw-   0        0        0      255 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userfolderpagingmodel.py
--rw-rw-rw-   0        0        0     1202 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userfolderpatchmodel.py
--rw-rw-rw-   0        0        0      146 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userfoldertreemodel.py
--rw-rw-rw-   0        0        0      632 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/userfoldertreenodemodel.py
--rw-rw-rw-   0        0        0      158 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateassistantaddmodel.py
--rw-rw-rw-   0        0        0      342 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateassistantmodel.py
--rw-rw-rw-   0        0        0      661 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateattributeinfomodel.py
--rw-rw-rw-   0        0        0      295 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateattributeobjecttypetreenode.py
--rw-rw-rw-   0        0        0      325 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatecategoryaddrequest.py
--rw-rw-rw-   0        0        0      151 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatecategoryaddresponse.py
--rw-rw-rw-   0        0        0      335 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatecategorypartialupdaterequest.py
--rw-rw-rw-   0        0        0      240 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatecommentmessageinfofilemodel.py
--rw-rw-rw-   0        0        0      878 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatecommentmessageinfomodel.py
--rw-rw-rw-   0        0        0      264 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatecommentmessageinfousermodel.py
--rw-rw-rw-   0        0        0      268 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatecommentmessagespagingmodel.py
--rw-rw-rw-   0        0        0      409 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateexecuteobjectactionmodel.py
--rw-rw-rw-   0        0        0      194 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateexecuteobjectactionresultmodel.py
--rw-rw-rw-   0        0        0      710 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatefolderobjectinfoattributemodel.py
--rw-rw-rw-   0        0        0      690 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatefolderobjectinfomodel.py
--rw-rw-rw-   0        0        0      370 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatefolderobjectinfomodelcommentinfo.py
--rw-rw-rw-   0        0        0      674 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatefolderobjectinfomodellastcomment.py
--rw-rw-rw-   0        0        0      273 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatefolderobjectinfomodellastcommentuser.py
--rw-rw-rw-   0        0        0      385 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatefolderobjectspagingmodel.py
--rw-rw-rw-   0        0        0      199 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergategetobjecttemplateresultmodel.py
--rw-rw-rw-   0        0        0      363 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatementioninfocommentmodel.py
--rw-rw-rw-   0        0        0      458 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatementioninfomodel.py
--rw-rw-rw-   0        0        0      197 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatementioninfoobjectmodel.py
--rw-rw-rw-   0        0        0      261 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergatementionspagingmodel.py
--rw-rw-rw-   0        0        0      282 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectaddmodel.py
--rw-rw-rw-   0        0        0      667 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfoattributemodel.py
--rw-rw-rw-   0        0        0      263 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfochunkitemmodel.py
--rw-rw-rw-   0        0        0      176 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfochunkmodel.py
--rw-rw-rw-   0        0        0      813 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfoextendedattributemodel.py
--rw-rw-rw-   0        0        0      686 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfoextendedmodel.py
--rw-rw-rw-   0        0        0      198 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfoextendedmodelroutebutton.py
--rw-rw-rw-   0        0        0      218 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfoextendedmodelroutedata.py
--rw-rw-rw-   0        0        0      305 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfomodel.py
--rw-rw-rw-   0        0        0      382 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectinfopagingmodel.py
--rw-rw-rw-   0        0        0      250 2023-04-03 08:20:50.000000 lementpro-0.1.6/lementpro/data/usergateobjectmodelattribute.py
--rw-rw-rw-   0        0        0      200 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergateobjectpatchmodel.py
--rw-rw-rw-   0        0        0      494 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergateobjecttypeobjectinfomodel.py
--rw-rw-rw-   0        0        0      389 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergateobjecttypeobjectspagingmodel.py
--rw-rw-rw-   0        0        0      290 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergateobjecttypetreemodel.py
--rw-rw-rw-   0        0        0      152 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatepagingmetadata.py
--rw-rw-rw-   0        0        0      231 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatepagingmetadatacolumn.py
--rw-rw-rw-   0        0        0      160 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatequicksearchresultmodel.py
--rw-rw-rw-   0        0        0      203 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatequicksearchresultobjectmodel.py
--rw-rw-rw-   0        0        0      552 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergaterouteinstanceextendedmodel.py
--rw-rw-rw-   0        0        0      574 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergaterouteinstanceextendedmodelactivity.py
--rw-rw-rw-   0        0        0      673 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatesearchobjectinfoattributemodel.py
--rw-rw-rw-   0        0        0      463 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatesearchobjectinfomodel.py
--rw-rw-rw-   0        0        0      384 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatesearchresultpagingmodel.py
--rw-rw-rw-   0        0        0      257 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergatesubstitutionmodel.py
--rw-rw-rw-   0        0        0      377 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergateuserspagingmodel.py
--rw-rw-rw-   0        0        0      150 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergroupaddproxymodel.py
--rw-rw-rw-   0        0        0      147 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usergroupaddresultmodel.py
--rw-rw-rw-   0        0        0      870 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userinfobysystemadminmodel.py
--rw-rw-rw-   0        0        0      234 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userinfobysystemadminmodeldepartment.py
--rw-rw-rw-   0        0        0      204 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userinfobysystemadminmodelgroup.py
--rw-rw-rw-   0        0        0     1158 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userinfoextendedmodel.py
--rw-rw-rw-   0        0        0      290 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userinfoextensionmodel.py
--rw-rw-rw-   0        0        0      669 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userinfomodel.py
--rw-rw-rw-   0        0        0      332 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usermailboxaddmodel.py
--rw-rw-rw-   0        0        0      149 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usermailboxaddresultmodel.py
--rw-rw-rw-   0        0        0      412 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usermailboxextendedmodel.py
--rw-rw-rw-   0        0        0      334 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usermailboxpatchmodel.py
--rw-rw-rw-   0        0        0      155 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usermentiondeletemodel.py
--rw-rw-rw-   0        0        0      286 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usermodelextension.py
--rw-rw-rw-   0        0        0      436 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usermodelnotification.py
--rw-rw-rw-   0        0        0      440 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usernotificationinfomodel.py
--rw-rw-rw-   0        0        0      442 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usernotificationupdatemodel.py
--rw-rw-rw-   0        0        0      262 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userpagingbysystemadminmodel.py
--rw-rw-rw-   0        0        0      180 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userpasswordupdatemodel.py
--rw-rw-rw-   0        0        0      671 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userpatchmodel.py
--rw-rw-rw-   0        0        0      153 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usersgroupaddproxymodel.py
--rw-rw-rw-   0        0        0      150 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/usersgroupaddresultmodel.py
--rw-rw-rw-   0        0        0      149 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userviewaddmodel.py
--rw-rw-rw-   0        0        0      148 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userviewaddresultmodel.py
--rw-rw-rw-   0        0        0      221 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userviewinfomodel.py
--rw-rw-rw-   0        0        0      253 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/userviewpagingmodel.py
--rw-rw-rw-   0        0        0      172 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/validationresponse.py
--rw-rw-rw-   0        0        0      174 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/validationresponseitem.py
--rw-rw-rw-   0        0        0      171 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistaddentrymodel.py
--rw-rw-rw-   0        0        0      226 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistaddmodel.py
--rw-rw-rw-   0        0        0      147 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistaddresultmodel.py
--rw-rw-rw-   0        0        0      176 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistentryaddproxymodel.py
--rw-rw-rw-   0        0        0      152 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistentryaddresultmodel.py
--rw-rw-rw-   0        0        0      221 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistentryinfomodel.py
--rw-rw-rw-   0        0        0      259 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistentrypagingmodel.py
--rw-rw-rw-   0        0        0      150 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistentrypatchmodel.py
--rw-rw-rw-   0        0        0      305 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistextendedmodel.py
--rw-rw-rw-   0        0        0      276 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistinfomodel.py
--rw-rw-rw-   0        0        0      254 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistpagingmodel.py
--rw-rw-rw-   0        0        0      174 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/valuelistpatchmodel.py
--rw-rw-rw-   0        0        0      169 2023-04-03 08:20:51.000000 lementpro-0.1.6/lementpro/data/virtualfolderpath.py
--rw-rw-rw-   0        0        0      353 2023-04-03 07:58:25.000000 lementpro-0.1.6/lementpro/logger.py
--rw-rw-rw-   0        0        0     1849 2023-04-03 07:58:25.000000 lementpro-0.1.6/lementpro/sender.py
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:17.472442 lementpro-0.1.6/lementpro/services/
--rw-rw-rw-   0        0        0        0 2023-04-03 07:58:25.000000 lementpro-0.1.6/lementpro/services/__init__.py
--rw-rw-rw-   0        0        0     4445 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/accounts.py
--rw-rw-rw-   0        0        0    66898 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/admin.py
--rw-rw-rw-   0        0        0     3901 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/comments.py
--rw-rw-rw-   0        0        0      466 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/companies.py
--rw-rw-rw-   0        0        0      708 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/connections.py
--rw-rw-rw-   0        0        0     1200 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/departments.py
--rw-rw-rw-   0        0        0     2543 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/files.py
--rw-rw-rw-   0        0        0     5861 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/folder.py
--rw-rw-rw-   0        0        0      771 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/groups.py
--rw-rw-rw-   0        0        0     1179 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/localization.py
--rw-rw-rw-   0        0        0     3959 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/objects.py
--rw-rw-rw-   0        0        0     2376 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/objecttypes.py
--rw-rw-rw-   0        0        0      561 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/routes.py
--rw-rw-rw-   0        0        0     1153 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/search.py
--rw-rw-rw-   0        0        0      630 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/timezones.py
--rw-rw-rw-   0        0        0     5821 2023-04-03 08:20:45.000000 lementpro-0.1.6/lementpro/services/users.py
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:13.771356 lementpro-0.1.6/lementpro.egg-info/
--rw-rw-rw-   0        0        0      583 2023-04-03 10:50:13.000000 lementpro-0.1.6/lementpro.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0    16392 2023-04-03 10:50:13.000000 lementpro-0.1.6/lementpro.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 10:50:13.000000 lementpro-0.1.6/lementpro.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       16 2023-04-03 10:50:13.000000 lementpro-0.1.6/lementpro.egg-info/requires.txt
--rw-rw-rw-   0        0        0       14 2023-04-03 10:50:13.000000 lementpro-0.1.6/lementpro.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-03 10:50:17.620984 lementpro-0.1.6/setup.cfg
--rw-rw-rw-   0        0        0      831 2023-04-03 10:49:23.000000 lementpro-0.1.6/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:13.707379 lementpro-0.1.6/src/
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:17.576441 lementpro-0.1.6/src/templates/
--rw-rw-rw-   0        0        0        0 2023-04-03 07:58:25.000000 lementpro-0.1.6/src/templates/__init__.py
--rw-rw-rw-   0        0        0     1559 2023-04-03 08:14:39.000000 lementpro-0.1.6/src/templates/builders.py
--rw-rw-rw-   0        0        0      353 2023-04-03 07:58:25.000000 lementpro-0.1.6/src/templates/logger.py
--rw-rw-rw-   0        0        0     1849 2023-04-03 07:58:25.000000 lementpro-0.1.6/src/templates/sender.py
--rw-rw-rw-   0        0        0      270 2023-04-03 07:58:25.000000 lementpro-0.1.6/src/templates/user.py
-drwxrwxrwx   0        0        0        0 2023-04-03 10:50:17.596984 lementpro-0.1.6/tests/
--rw-rw-rw-   0        0        0      863 2023-04-03 07:58:25.000000 lementpro-0.1.6/tests/test_sdk.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:56.525635 lementpro-0.1.7/
+-rw-rw-rw-   0        0        0      583 2023-04-06 10:59:56.520632 lementpro-0.1.7/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:46.816477 lementpro-0.1.7/lementpro/
+-rw-rw-rw-   0        0        0      647 2023-04-03 10:22:22.000000 lementpro-0.1.7/lementpro/__init__.py
+-rw-rw-rw-   0        0        0     1559 2023-04-03 08:14:39.000000 lementpro-0.1.7/lementpro/builders.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:56.244580 lementpro-0.1.7/lementpro/data/
+-rw-rw-rw-   0        0        0    14775 2023-04-06 10:54:59.000000 lementpro-0.1.7/lementpro/data/__init__.py
+-rw-rw-rw-   0        0        0      206 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/accesstokenmodel.py
+-rw-rw-rw-   0        0        0      349 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/actionlogentryinfomodel.py
+-rw-rw-rw-   0        0        0      594 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributeaddmodel.py
+-rw-rw-rw-   0        0        0      613 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributeaddrelationmodel.py
+-rw-rw-rw-   0        0        0      147 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributeaddresultmodel.py
+-rw-rw-rw-   0        0        0      682 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributeextendedmodel.py
+-rw-rw-rw-   0        0        0      547 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributeinfomodel.py
+-rw-rw-rw-   0        0        0      254 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributepagingmodel.py
+-rw-rw-rw-   0        0        0      577 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributepatchmodel.py
+-rw-rw-rw-   0        0        0      700 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributepatchrelationmodel.py
+-rw-rw-rw-   0        0        0      699 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/attributerelationinfomodel.py
+-rw-rw-rw-   0        0        0      181 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/changepasswordmodel.py
+-rw-rw-rw-   0        0        0      277 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/checkconnectionmodel.py
+-rw-rw-rw-   0        0        0      202 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/checkconnectionresultmodel.py
+-rw-rw-rw-   0        0        0      399 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/commentaddbyusermodel.py
+-rw-rw-rw-   0        0        0      145 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/data/commentaddresultmodel.py
+-rw-rw-rw-   0        0        0      378 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/commentemailextensionmodel.py
+-rw-rw-rw-   0        0        0      391 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/commentextensionmodel.py
+-rw-rw-rw-   0        0        0      315 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/commentpatchmodel.py
+-rw-rw-rw-   0        0        0      245 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companycontactdetailsmodel.py
+-rw-rw-rw-   0        0        0      250 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companycontactdetailspatchmodel.py
+-rw-rw-rw-   0        0        0      211 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companyextensionmodel.py
+-rw-rw-rw-   0        0        0      227 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companyinfodetailedmodel.py
+-rw-rw-rw-   0        0        0     1157 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companyinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      374 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companyinfomodel.py
+-rw-rw-rw-   0        0        0      213 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companylicensemodel.py
+-rw-rw-rw-   0        0        0      308 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companymailboxaddmodel.py
+-rw-rw-rw-   0        0        0      152 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companymailboxaddresultmodel.py
+-rw-rw-rw-   0        0        0      334 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companymailboxextendedmodel.py
+-rw-rw-rw-   0        0        0      310 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companymailboxpatchmodel.py
+-rw-rw-rw-   0        0        0      286 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companypasswordpolicymodel.py
+-rw-rw-rw-   0        0        0      291 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companypasswordpolicypatchmodel.py
+-rw-rw-rw-   0        0        0      747 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/companypatchmodel.py
+-rw-rw-rw-   0        0        0      276 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentaddmodel.py
+-rw-rw-rw-   0        0        0      148 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentaddresultmodel.py
+-rw-rw-rw-   0        0        0      150 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentbosssetmodel.py
+-rw-rw-rw-   0        0        0      683 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentbossuserinfomodel.py
+-rw-rw-rw-   0        0        0      679 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      548 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentinfomodel.py
+-rw-rw-rw-   0        0        0      255 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentpagingmodel.py
+-rw-rw-rw-   0        0        0      279 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmenttreemodel.py
+-rw-rw-rw-   0        0        0      307 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/departmentupdatemodel.py
+-rw-rw-rw-   0        0        0      369 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/emailaddressmodel.py
+-rw-rw-rw-   0        0        0      187 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/errorresponse.py
+-rw-rw-rw-   0        0        0      139 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/etaginfomodel.py
+-rw-rw-rw-   0        0        0      457 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/fileinfomodel.py
+-rw-rw-rw-   0        0        0      253 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/fileinfopagingmodel.py
+-rw-rw-rw-   0        0        0      465 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/fileuploadresultmodel.py
+-rw-rw-rw-   0        0        0      183 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderaddobjectstatefilter.py
+-rw-rw-rw-   0        0        0      205 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderaddobjectstatusfilter.py
+-rw-rw-rw-   0        0        0      296 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderaddobjectuserfilter.py
+-rw-rw-rw-   0        0        0      144 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderaddresultmodel.py
+-rw-rw-rw-   0        0        0      281 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderattributepredicatemodel.py
+-rw-rw-rw-   0        0        0      325 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderfilterbyattributemodel.py
+-rw-rw-rw-   0        0        0      223 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldergroupbyattributemodel.py
+-rw-rw-rw-   0        0        0      169 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldergroupinfomodel.py
+-rw-rw-rw-   0        0        0      428 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderinfomodel.py
+-rw-rw-rw-   0        0        0      225 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderjoinbyattributemodel.py
+-rw-rw-rw-   0        0        0      207 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderobjecttypeinfomodel.py
+-rw-rw-rw-   0        0        0      183 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderobjecttypemodel.py
+-rw-rw-rw-   0        0        0      246 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderorderbyattributemodel.py
+-rw-rw-rw-   0        0        0      251 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderpagingmodel.py
+-rw-rw-rw-   0        0        0      150 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderpatchgroupmodel.py
+-rw-rw-rw-   0        0        0      185 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderpatchobjectstatefilter.py
+-rw-rw-rw-   0        0        0      207 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderpatchobjectstatusfilter.py
+-rw-rw-rw-   0        0        0      298 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderpatchobjectuserfilter.py
+-rw-rw-rw-   0        0        0      301 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderpatchreset.py
+-rw-rw-rw-   0        0        0      156 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldertemplateaddgroupmodel.py
+-rw-rw-rw-   0        0        0     1118 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldertemplateaddmodel.py
+-rw-rw-rw-   0        0        0     1254 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldertemplateextendedmodel.py
+-rw-rw-rw-   0        0        0     1176 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldertemplatepatchmodel.py
+-rw-rw-rw-   0        0        0      419 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldertemplatesmenuproxymodel.py
+-rw-rw-rw-   0        0        0      379 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/foldertemplatestreeproxymodel.py
+-rw-rw-rw-   0        0        0      177 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/folderusertreecountmodel.py
+-rw-rw-rw-   0        0        0      198 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupaddmodel.py
+-rw-rw-rw-   0        0        0      143 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupaddresultmodel.py
+-rw-rw-rw-   0        0        0      644 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupinfoextendedproxymodel.py
+-rw-rw-rw-   0        0        0      357 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupinfomodel.py
+-rw-rw-rw-   0        0        0      210 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupobjectexpirationaddmodel.py
+-rw-rw-rw-   0        0        0      159 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupobjectexpirationaddresultmodel.py
+-rw-rw-rw-   0        0        0      258 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupobjectexpirationinfomodel.py
+-rw-rw-rw-   0        0        0      187 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupobjectexpirationpatchmodel.py
+-rw-rw-rw-   0        0        0      254 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupobjecttypeinfomodel.py
+-rw-rw-rw-   0        0        0      260 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupobjecttypepagingmodel.py
+-rw-rw-rw-   0        0        0      184 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupobjecttypeupsertmodel.py
+-rw-rw-rw-   0        0        0      250 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/grouppagingmodel.py
+-rw-rw-rw-   0        0        0      360 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/groupupdateproxymodel.py
+-rw-rw-rw-   0        0        0      319 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxactionaddmodel.py
+-rw-rw-rw-   0        0        0      200 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxactionaddresultmodel.py
+-rw-rw-rw-   0        0        0      344 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxactionextendedmodel.py
+-rw-rw-rw-   0        0        0      283 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxactionpatchmodel.py
+-rw-rw-rw-   0        0        0      311 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxaddmodel.py
+-rw-rw-rw-   0        0        0      156 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxaddresultmodel.py
+-rw-rw-rw-   0        0        0      337 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxextendedmodel.py
+-rw-rw-rw-   0        0        0      333 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxinfomodel.py
+-rw-rw-rw-   0        0        0      263 2023-04-03 08:20:46.000000 lementpro-0.1.7/lementpro/data/integrationmailboxpagingmodel.py
+-rw-rw-rw-   0        0        0      313 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/integrationmailboxpatchmodel.py
+-rw-rw-rw-   0        0        0      186 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/integrationmailboxrulemodel.py
+-rw-rw-rw-   0        0        0      160 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/languagemodel.py
+-rw-rw-rw-   0        0        0      284 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphgetschemaresponse.py
+-rw-rw-rw-   0        0        0      315 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemaadddraftrequest.py
+-rw-rw-rw-   0        0        0      283 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemaaddrequest.py
+-rw-rw-rw-   0        0        0      350 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemaaddrequesttransitionactionmodel.py
+-rw-rw-rw-   0        0        0      428 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemaaddrequesttransitionconditionmodel.py
+-rw-rw-rw-   0        0        0      320 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemaaddrequesttransitionconditionpredicatemodel.py
+-rw-rw-rw-   0        0        0      588 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemaelementmodel.py
+-rw-rw-rw-   0        0        0      217 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemaline.py
+-rw-rw-rw-   0        0        0      160 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemapoint.py
+-rw-rw-rw-   0        0        0      301 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemarelatedproperty.py
+-rw-rw-rw-   0        0        0      820 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschematransitionmodel.py
+-rw-rw-rw-   0        0        0      172 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemauserreference.py
+-rw-rw-rw-   0        0        0      345 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/mxgraphschemavariablemodel.py
+-rw-rw-rw-   0        0        0      144 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objectaddresultmodel.py
+-rw-rw-rw-   0        0        0      210 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objectattributemodel.py
+-rw-rw-rw-   0        0        0      223 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeaddcountermodel.py
+-rw-rw-rw-   0        0        0      175 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeaddextensionmodel.py
+-rw-rw-rw-   0        0        0      622 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeaddmodel.py
+-rw-rw-rw-   0        0        0      148 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeaddresultmodel.py
+-rw-rw-rw-   0        0        0      256 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeaddformulamodel.py
+-rw-rw-rw-   0        0        0      536 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeaddproxymodel.py
+-rw-rw-rw-   0        0        0      157 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeaddresultmodel.py
+-rw-rw-rw-   0        0        0      674 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeaddsettingsmodel.py
+-rw-rw-rw-   0        0        0      915 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeextendedmodel.py
+-rw-rw-rw-   0        0        0      720 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeinfoattributemodel.py
+-rw-rw-rw-   0        0        0      312 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeinfoattributerelationmodel.py
+-rw-rw-rw-   0        0        0      257 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeinfoformulamodel.py
+-rw-rw-rw-   0        0        0      754 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeinfomodel.py
+-rw-rw-rw-   0        0        0      675 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeinfosettingsmodel.py
+-rw-rw-rw-   0        0        0      191 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeinfovaluelistentrymodel.py
+-rw-rw-rw-   0        0        0      186 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributeinfovaluelistmodel.py
+-rw-rw-rw-   0        0        0      264 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributepagingmodel.py
+-rw-rw-rw-   0        0        0      258 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributepatchformulamodel.py
+-rw-rw-rw-   0        0        0      516 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributepatchmodel.py
+-rw-rw-rw-   0        0        0      676 2023-04-03 08:20:47.000000 lementpro-0.1.7/lementpro/data/objecttypeattributepatchsettingsmodel.py
+-rw-rw-rw-   0        0        0      241 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypebimaddproxymodel.py
+-rw-rw-rw-   0        0        0      151 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypebimaddresultmodel.py
+-rw-rw-rw-   0        0        0      295 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypebiminfoextendedmodel.py
+-rw-rw-rw-   0        0        0      238 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypebimpatchmodel.py
+-rw-rw-rw-   0        0        0      178 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypebreadcrumbmodel.py
+-rw-rw-rw-   0        0        0      237 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypecheckpointaddproxymodel.py
+-rw-rw-rw-   0        0        0      158 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypecheckpointaddresultmodel.py
+-rw-rw-rw-   0        0        0      291 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypecheckpointinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      289 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypecheckpointinfopagingmodel.py
+-rw-rw-rw-   0        0        0      265 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypecheckpointpagingmodel.py
+-rw-rw-rw-   0        0        0      234 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypecheckpointpatchmodel.py
+-rw-rw-rw-   0        0        0      202 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeextensionmodel.py
+-rw-rw-rw-   0        0        0      207 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypefileinfopagingmodel.py
+-rw-rw-rw-   0        0        0      259 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypefilepagingmodel.py
+-rw-rw-rw-   0        0        0      155 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypefileupsertmodel.py
+-rw-rw-rw-   0        0        0      265 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeinfodetailedbimmodel.py
+-rw-rw-rw-   0        0        0      252 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeinfodetailedcountermodel.py
+-rw-rw-rw-   0        0        0      179 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeinfodetailedfilemodel.py
+-rw-rw-rw-   0        0        0      365 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeinfodetailedmenumodel.py
+-rw-rw-rw-   0        0        0      603 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeinfodetailedmodel.py
+-rw-rw-rw-   0        0        0      767 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      595 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeinfopagingmodel.py
+-rw-rw-rw-   0        0        0      258 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypemenuaddproxymodel.py
+-rw-rw-rw-   0        0        0      152 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypemenuaddresultmodel.py
+-rw-rw-rw-   0        0        0      422 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypemenuinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      420 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypemenuinfopagingmodel.py
+-rw-rw-rw-   0        0        0      283 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypemenupatchmodel.py
+-rw-rw-rw-   0        0        0      255 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypepagingmodel.py
+-rw-rw-rw-   0        0        0      225 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypepatchcountermodel.py
+-rw-rw-rw-   0        0        0      177 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypepatchextensionmodel.py
+-rw-rw-rw-   0        0        0      638 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypepatchmodel.py
+-rw-rw-rw-   0        0        0      257 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypetreenodeproxymodel.py
+-rw-rw-rw-   0        0        0     1045 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponse.py
+-rw-rw-rw-   0        0        0      172 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponsecreatepage.py
+-rw-rw-rw-   0        0        0      268 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponsecreatepageattribute.py
+-rw-rw-rw-   0        0        0      197 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponsedetailedpage.py
+-rw-rw-rw-   0        0        0      306 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponsedetailedpageattribute.py
+-rw-rw-rw-   0        0        0      264 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponsedetailedpagetab.py
+-rw-rw-rw-   0        0        0      170 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponseeditpage.py
+-rw-rw-rw-   0        0        0      266 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponseeditpageattribute.py
+-rw-rw-rw-   0        0        0      172 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponselistview.py
+-rw-rw-rw-   0        0        0      293 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponselistviewattribute.py
+-rw-rw-rw-   0        0        0      172 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponsetableview.py
+-rw-rw-rw-   0        0        0      267 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponsetableviewattribute.py
+-rw-rw-rw-   0        0        0      184 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objectuserfavoritemodel.py
+-rw-rw-rw-   0        0        0      151 2023-04-03 08:20:48.000000 lementpro-0.1.7/lementpro/data/objectuserreadmodel.py
+-rw-rw-rw-   0        0        0      153 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/objectuserunreadmodel.py
+-rw-rw-rw-   0        0        0      252 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/pagingmodel.py
+-rw-rw-rw-   0        0        0      151 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/refreshtokenmodel.py
+-rw-rw-rw-   0        0        0      441 2023-04-06 10:58:49.000000 lementpro-0.1.7/lementpro/data/relatedobjectmodel.py
+-rw-rw-rw-   0        0        0      273 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/relationvalue.py
+-rw-rw-rw-   0        0        0      174 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/restorepasswordmodel.py
+-rw-rw-rw-   0        0        0      160 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeactivitybuttonrequest.py
+-rw-rw-rw-   0        0        0      222 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeextendedresponseactivityelement.py
+-rw-rw-rw-   0        0        0      501 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeextendedresponseactivityvariable.py
+-rw-rw-rw-   0        0        0      220 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeextendedresponsereferenceobject.py
+-rw-rw-rw-   0        0        0      252 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeextendedresponsereferenceobjectproperty.py
+-rw-rw-rw-   0        0        0      460 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeinforesponse.py
+-rw-rw-rw-   0        0        0      255 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeinforesponseschema.py
+-rw-rw-rw-   0        0        0      359 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routeinforesponseschemaversion.py
+-rw-rw-rw-   0        0        0      253 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/routepagingresponse.py
+-rw-rw-rw-   0        0        0      220 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/schemaaddresponse.py
+-rw-rw-rw-   0        0        0      327 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/schemaextendedresponse.py
+-rw-rw-rw-   0        0        0      278 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/schemainforesponse.py
+-rw-rw-rw-   0        0        0      260 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/schemainforesponseversion.py
+-rw-rw-rw-   0        0        0      254 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/schemapagingresponse.py
+-rw-rw-rw-   0        0        0      259 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationaddmodel.py
+-rw-rw-rw-   0        0        0      156 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationaddresultmodel.py
+-rw-rw-rw-   0        0        0      196 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationinfodetailedmodel.py
+-rw-rw-rw-   0        0        0      473 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      313 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationinfopagingmodel.py
+-rw-rw-rw-   0        0        0      209 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationinfoparammodel.py
+-rw-rw-rw-   0        0        0      208 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationobjecttypeaddmodel.py
+-rw-rw-rw-   0        0        0      166 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationobjecttypeaddresultmodel.py
+-rw-rw-rw-   0        0        0      237 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationobjecttypeinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      235 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationobjecttypeinfopagingmodel.py
+-rw-rw-rw-   0        0        0      273 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationobjecttypepagingmodel.py
+-rw-rw-rw-   0        0        0      172 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationobjecttypepatchmodel.py
+-rw-rw-rw-   0        0        0      263 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationpagingmodel.py
+-rw-rw-rw-   0        0        0      246 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationparamaddmodel.py
+-rw-rw-rw-   0        0        0      161 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationparamaddresultmodel.py
+-rw-rw-rw-   0        0        0      275 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationparaminfoextendedmodel.py
+-rw-rw-rw-   0        0        0      273 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationparaminfopagingmodel.py
+-rw-rw-rw-   0        0        0      268 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationparampagingmodel.py
+-rw-rw-rw-   0        0        0      210 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationparampatchmodel.py
+-rw-rw-rw-   0        0        0      261 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/serviceintegrationpatchmodel.py
+-rw-rw-rw-   0        0        0      199 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/setobjecttyperequest.py
+-rw-rw-rw-   0        0        0      190 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/setsortweightmodel.py
+-rw-rw-rw-   0        0        0      169 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/signinproxymodel.py
+-rw-rw-rw-   0        0        0      258 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/statisticspagingresponse.py
+-rw-rw-rw-   0        0        0      453 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/statisticsrecordinforesponse.py
+-rw-rw-rw-   0        0        0      163 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/timezoneinfomodel.py
+-rw-rw-rw-   0        0        0      253 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/timezonepagingmodel.py
+-rw-rw-rw-   0        0        0      138 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/tobccmodel.py
+-rw-rw-rw-   0        0        0      137 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/toccmodel.py
+-rw-rw-rw-   0        0        0      141 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/toemailsmodel.py
+-rw-rw-rw-   0        0        0      270 2023-04-03 07:58:25.000000 lementpro-0.1.7/lementpro/data/user.py
+-rw-rw-rw-   0        0        0      669 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/useraddmodel.py
+-rw-rw-rw-   0        0        0      142 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/useraddresultmodel.py
+-rw-rw-rw-   0        0        0      151 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/userassistantaddresultmodel.py
+-rw-rw-rw-   0        0        0      156 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/userdepartmentmoveproxymodel.py
+-rw-rw-rw-   0        0        0      254 2023-04-03 08:20:49.000000 lementpro-0.1.7/lementpro/data/userdetailedmodeldepartment.py
+-rw-rw-rw-   0        0        0      195 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userdetailedmodelgroup.py
+-rw-rw-rw-   0        0        0      464 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userdetailedmodelnotification.py
+-rw-rw-rw-   0        0        0     1144 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userfolderaddmodel.py
+-rw-rw-rw-   0        0        0     1306 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userfolderextendedmodel.py
+-rw-rw-rw-   0        0        0      458 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userfolderinfomodel.py
+-rw-rw-rw-   0        0        0      255 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userfolderpagingmodel.py
+-rw-rw-rw-   0        0        0     1202 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userfolderpatchmodel.py
+-rw-rw-rw-   0        0        0      146 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userfoldertreemodel.py
+-rw-rw-rw-   0        0        0      632 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/userfoldertreenodemodel.py
+-rw-rw-rw-   0        0        0      158 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateassistantaddmodel.py
+-rw-rw-rw-   0        0        0      342 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateassistantmodel.py
+-rw-rw-rw-   0        0        0      661 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateattributeinfomodel.py
+-rw-rw-rw-   0        0        0      295 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateattributeobjecttypetreenode.py
+-rw-rw-rw-   0        0        0      325 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatecategoryaddrequest.py
+-rw-rw-rw-   0        0        0      151 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatecategoryaddresponse.py
+-rw-rw-rw-   0        0        0      335 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatecategorypartialupdaterequest.py
+-rw-rw-rw-   0        0        0      240 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatecommentmessageinfofilemodel.py
+-rw-rw-rw-   0        0        0      878 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatecommentmessageinfomodel.py
+-rw-rw-rw-   0        0        0      264 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatecommentmessageinfousermodel.py
+-rw-rw-rw-   0        0        0      268 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatecommentmessagespagingmodel.py
+-rw-rw-rw-   0        0        0      409 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateexecuteobjectactionmodel.py
+-rw-rw-rw-   0        0        0      194 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateexecuteobjectactionresultmodel.py
+-rw-rw-rw-   0        0        0      710 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatefolderobjectinfoattributemodel.py
+-rw-rw-rw-   0        0        0      690 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatefolderobjectinfomodel.py
+-rw-rw-rw-   0        0        0      370 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatefolderobjectinfomodelcommentinfo.py
+-rw-rw-rw-   0        0        0      674 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatefolderobjectinfomodellastcomment.py
+-rw-rw-rw-   0        0        0      273 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatefolderobjectinfomodellastcommentuser.py
+-rw-rw-rw-   0        0        0      385 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatefolderobjectspagingmodel.py
+-rw-rw-rw-   0        0        0      199 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergategetobjecttemplateresultmodel.py
+-rw-rw-rw-   0        0        0      363 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatementioninfocommentmodel.py
+-rw-rw-rw-   0        0        0      458 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatementioninfomodel.py
+-rw-rw-rw-   0        0        0      197 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatementioninfoobjectmodel.py
+-rw-rw-rw-   0        0        0      261 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergatementionspagingmodel.py
+-rw-rw-rw-   0        0        0      282 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectaddmodel.py
+-rw-rw-rw-   0        0        0      667 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfoattributemodel.py
+-rw-rw-rw-   0        0        0      263 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfochunkitemmodel.py
+-rw-rw-rw-   0        0        0      176 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfochunkmodel.py
+-rw-rw-rw-   0        0        0      813 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfoextendedattributemodel.py
+-rw-rw-rw-   0        0        0      686 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      198 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfoextendedmodelroutebutton.py
+-rw-rw-rw-   0        0        0      218 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfoextendedmodelroutedata.py
+-rw-rw-rw-   0        0        0      305 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfomodel.py
+-rw-rw-rw-   0        0        0      382 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectinfopagingmodel.py
+-rw-rw-rw-   0        0        0      250 2023-04-03 08:20:50.000000 lementpro-0.1.7/lementpro/data/usergateobjectmodelattribute.py
+-rw-rw-rw-   0        0        0      200 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergateobjectpatchmodel.py
+-rw-rw-rw-   0        0        0      494 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergateobjecttypeobjectinfomodel.py
+-rw-rw-rw-   0        0        0      389 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergateobjecttypeobjectspagingmodel.py
+-rw-rw-rw-   0        0        0      290 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergateobjecttypetreemodel.py
+-rw-rw-rw-   0        0        0      152 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatepagingmetadata.py
+-rw-rw-rw-   0        0        0      231 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatepagingmetadatacolumn.py
+-rw-rw-rw-   0        0        0      160 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatequicksearchresultmodel.py
+-rw-rw-rw-   0        0        0      203 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatequicksearchresultobjectmodel.py
+-rw-rw-rw-   0        0        0      552 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergaterouteinstanceextendedmodel.py
+-rw-rw-rw-   0        0        0      574 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergaterouteinstanceextendedmodelactivity.py
+-rw-rw-rw-   0        0        0      673 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatesearchobjectinfoattributemodel.py
+-rw-rw-rw-   0        0        0      463 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatesearchobjectinfomodel.py
+-rw-rw-rw-   0        0        0      384 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatesearchresultpagingmodel.py
+-rw-rw-rw-   0        0        0      257 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergatesubstitutionmodel.py
+-rw-rw-rw-   0        0        0      377 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergateuserspagingmodel.py
+-rw-rw-rw-   0        0        0      150 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergroupaddproxymodel.py
+-rw-rw-rw-   0        0        0      147 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usergroupaddresultmodel.py
+-rw-rw-rw-   0        0        0      870 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userinfobysystemadminmodel.py
+-rw-rw-rw-   0        0        0      234 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userinfobysystemadminmodeldepartment.py
+-rw-rw-rw-   0        0        0      204 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userinfobysystemadminmodelgroup.py
+-rw-rw-rw-   0        0        0     1158 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userinfoextendedmodel.py
+-rw-rw-rw-   0        0        0      290 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userinfoextensionmodel.py
+-rw-rw-rw-   0        0        0      669 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userinfomodel.py
+-rw-rw-rw-   0        0        0      332 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usermailboxaddmodel.py
+-rw-rw-rw-   0        0        0      149 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usermailboxaddresultmodel.py
+-rw-rw-rw-   0        0        0      412 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usermailboxextendedmodel.py
+-rw-rw-rw-   0        0        0      334 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usermailboxpatchmodel.py
+-rw-rw-rw-   0        0        0      155 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usermentiondeletemodel.py
+-rw-rw-rw-   0        0        0      286 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usermodelextension.py
+-rw-rw-rw-   0        0        0      436 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usermodelnotification.py
+-rw-rw-rw-   0        0        0      440 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usernotificationinfomodel.py
+-rw-rw-rw-   0        0        0      442 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usernotificationupdatemodel.py
+-rw-rw-rw-   0        0        0      262 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userpagingbysystemadminmodel.py
+-rw-rw-rw-   0        0        0      180 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userpasswordupdatemodel.py
+-rw-rw-rw-   0        0        0      671 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userpatchmodel.py
+-rw-rw-rw-   0        0        0      153 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usersgroupaddproxymodel.py
+-rw-rw-rw-   0        0        0      150 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/usersgroupaddresultmodel.py
+-rw-rw-rw-   0        0        0      149 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userviewaddmodel.py
+-rw-rw-rw-   0        0        0      148 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userviewaddresultmodel.py
+-rw-rw-rw-   0        0        0      221 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userviewinfomodel.py
+-rw-rw-rw-   0        0        0      253 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/userviewpagingmodel.py
+-rw-rw-rw-   0        0        0      172 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/validationresponse.py
+-rw-rw-rw-   0        0        0      174 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/validationresponseitem.py
+-rw-rw-rw-   0        0        0      171 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistaddentrymodel.py
+-rw-rw-rw-   0        0        0      226 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistaddmodel.py
+-rw-rw-rw-   0        0        0      147 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistaddresultmodel.py
+-rw-rw-rw-   0        0        0      176 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistentryaddproxymodel.py
+-rw-rw-rw-   0        0        0      152 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistentryaddresultmodel.py
+-rw-rw-rw-   0        0        0      221 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistentryinfomodel.py
+-rw-rw-rw-   0        0        0      259 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistentrypagingmodel.py
+-rw-rw-rw-   0        0        0      150 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistentrypatchmodel.py
+-rw-rw-rw-   0        0        0      305 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistextendedmodel.py
+-rw-rw-rw-   0        0        0      276 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistinfomodel.py
+-rw-rw-rw-   0        0        0      254 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistpagingmodel.py
+-rw-rw-rw-   0        0        0      174 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/valuelistpatchmodel.py
+-rw-rw-rw-   0        0        0      169 2023-04-03 08:20:51.000000 lementpro-0.1.7/lementpro/data/virtualfolderpath.py
+-rw-rw-rw-   0        0        0      353 2023-04-03 07:58:25.000000 lementpro-0.1.7/lementpro/logger.py
+-rw-rw-rw-   0        0        0     1849 2023-04-03 07:58:25.000000 lementpro-0.1.7/lementpro/sender.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:56.444279 lementpro-0.1.7/lementpro/services/
+-rw-rw-rw-   0        0        0      504 2023-04-06 10:55:50.000000 lementpro-0.1.7/lementpro/services/__init__.py
+-rw-rw-rw-   0        0        0     4515 2023-04-04 13:53:40.000000 lementpro-0.1.7/lementpro/services/accounts.py
+-rw-rw-rw-   0        0        0    66898 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/admin.py
+-rw-rw-rw-   0        0        0     3901 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/comments.py
+-rw-rw-rw-   0        0        0      466 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/companies.py
+-rw-rw-rw-   0        0        0      708 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/connections.py
+-rw-rw-rw-   0        0        0     1200 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/departments.py
+-rw-rw-rw-   0        0        0     2543 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/files.py
+-rw-rw-rw-   0        0        0     5861 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/folder.py
+-rw-rw-rw-   0        0        0      771 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/groups.py
+-rw-rw-rw-   0        0        0     1179 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/localization.py
+-rw-rw-rw-   0        0        0     3959 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/objects.py
+-rw-rw-rw-   0        0        0     2376 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/objecttypes.py
+-rw-rw-rw-   0        0        0      561 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/routes.py
+-rw-rw-rw-   0        0        0     1153 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/search.py
+-rw-rw-rw-   0        0        0      630 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/timezones.py
+-rw-rw-rw-   0        0        0     5821 2023-04-03 08:20:45.000000 lementpro-0.1.7/lementpro/services/users.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:46.857555 lementpro-0.1.7/lementpro.egg-info/
+-rw-rw-rw-   0        0        0      583 2023-04-06 10:59:46.000000 lementpro-0.1.7/lementpro.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0    16392 2023-04-06 10:59:46.000000 lementpro-0.1.7/lementpro.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 10:59:46.000000 lementpro-0.1.7/lementpro.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       16 2023-04-06 10:59:46.000000 lementpro-0.1.7/lementpro.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       14 2023-04-06 10:59:46.000000 lementpro-0.1.7/lementpro.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 10:59:56.526634 lementpro-0.1.7/setup.cfg
+-rw-rw-rw-   0        0        0      831 2023-04-06 10:59:23.000000 lementpro-0.1.7/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:46.781483 lementpro-0.1.7/src/
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:56.487734 lementpro-0.1.7/src/templates/
+-rw-rw-rw-   0        0        0        0 2023-04-03 07:58:25.000000 lementpro-0.1.7/src/templates/__init__.py
+-rw-rw-rw-   0        0        0     1559 2023-04-03 08:14:39.000000 lementpro-0.1.7/src/templates/builders.py
+-rw-rw-rw-   0        0        0      353 2023-04-03 07:58:25.000000 lementpro-0.1.7/src/templates/logger.py
+-rw-rw-rw-   0        0        0     1849 2023-04-03 07:58:25.000000 lementpro-0.1.7/src/templates/sender.py
+-rw-rw-rw-   0        0        0      270 2023-04-03 07:58:25.000000 lementpro-0.1.7/src/templates/user.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:59:56.501635 lementpro-0.1.7/tests/
+-rw-rw-rw-   0        0        0      863 2023-04-03 07:58:25.000000 lementpro-0.1.7/tests/test_sdk.py
```

### Comparing `lementpro-0.1.6/PKG-INFO` & `lementpro-0.1.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lementpro
-Version: 0.1.6
+Version: 0.1.7
 Summary: Description of package
 Home-page: https://github.com/your_username/your_package_name
 Author: Author
 Author-email: your_email@example.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `lementpro-0.1.6/lementpro/__init__.py` & `lementpro-0.1.7/lementpro/__init__.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/builders.py` & `lementpro-0.1.7/lementpro/builders.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/attributeaddmodel.py` & `lementpro-0.1.7/lementpro/data/attributeaddmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/attributeaddrelationmodel.py` & `lementpro-0.1.7/lementpro/data/attributeaddrelationmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/attributeextendedmodel.py` & `lementpro-0.1.7/lementpro/data/attributeextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/attributeinfomodel.py` & `lementpro-0.1.7/lementpro/data/attributeinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/attributepatchmodel.py` & `lementpro-0.1.7/lementpro/data/attributepatchmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/attributepatchrelationmodel.py` & `lementpro-0.1.7/lementpro/data/attributepatchrelationmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/attributerelationinfomodel.py` & `lementpro-0.1.7/lementpro/data/attributerelationinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/companyinfoextendedmodel.py` & `lementpro-0.1.7/lementpro/data/companyinfoextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/companypatchmodel.py` & `lementpro-0.1.7/lementpro/data/companypatchmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/departmentbossuserinfomodel.py` & `lementpro-0.1.7/lementpro/data/departmentbossuserinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/departmentinfoextendedmodel.py` & `lementpro-0.1.7/lementpro/data/departmentinfoextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/departmentinfomodel.py` & `lementpro-0.1.7/lementpro/data/departmentinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/foldertemplateaddmodel.py` & `lementpro-0.1.7/lementpro/data/foldertemplateaddmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/foldertemplateextendedmodel.py` & `lementpro-0.1.7/lementpro/data/foldertemplateextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/foldertemplatepatchmodel.py` & `lementpro-0.1.7/lementpro/data/foldertemplatepatchmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/groupinfoextendedproxymodel.py` & `lementpro-0.1.7/lementpro/data/groupinfoextendedproxymodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/mxgraphschemaelementmodel.py` & `lementpro-0.1.7/lementpro/data/mxgraphschemaelementmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/mxgraphschematransitionmodel.py` & `lementpro-0.1.7/lementpro/data/mxgraphschematransitionmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeaddmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeaddmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributeaddproxymodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributeaddproxymodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributeaddsettingsmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributeaddsettingsmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributeextendedmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributeextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributeinfoattributemodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributeinfoattributemodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributeinfomodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributeinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributeinfosettingsmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributeinfosettingsmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributepatchmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributepatchmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeattributepatchsettingsmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeattributepatchsettingsmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeinfodetailedmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeinfodetailedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeinfoextendedmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeinfoextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeinfopagingmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypeinfopagingmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypepatchmodel.py` & `lementpro-0.1.7/lementpro/data/objecttypepatchmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/objecttypeuisettingsproxyresponse.py` & `lementpro-0.1.7/lementpro/data/objecttypeuisettingsproxyresponse.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/relatedobjectmodel.py` & `lementpro-0.1.7/lementpro/data/usergateobjectinfoattributemodel.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 from dataclasses import dataclass
-from lementpro.data.relatedobjectmodel import RelatedObjectModel
+from lementpro.data.objecttypeattributeinfovaluelistmodel import ObjectTypeAttributeInfoValueListModel
+from lementpro.data.relationvalue import RelationValue
 @dataclass
-class RelatedObjectModel:
+class UserGateObjectInfoAttributeModel:
     id: int = None
+    knownId: str = None
     name: str = None
     isSystem: bool = None
-    iconClass: str = None
-    url: str = None
-    userAvatarFileId: int = None
-    userEmail: str = None
-    userPhone: str = None
-    fileSize: int = None
-    fileDateCreated: str = None
-    fileVersion: int = None
-    fileUser: RelatedObjectModel = None
+    value: str = None
+    valueList: ObjectTypeAttributeInfoValueListModel = None
+    relationValue: RelationValue = None
+    attributeTypeId: str = None
+    valueTypeId: str = None
+    relationTypeId: str = None
+    isRequired: bool = None
+    isEditable: bool = None
```

### Comparing `lementpro-0.1.6/lementpro/data/useraddmodel.py` & `lementpro-0.1.7/lementpro/data/useraddmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userfolderaddmodel.py` & `lementpro-0.1.7/lementpro/data/userfolderaddmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userfolderextendedmodel.py` & `lementpro-0.1.7/lementpro/data/userfolderextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userfolderpatchmodel.py` & `lementpro-0.1.7/lementpro/data/userfolderpatchmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userfoldertreenodemodel.py` & `lementpro-0.1.7/lementpro/data/userfoldertreenodemodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergateattributeinfomodel.py` & `lementpro-0.1.7/lementpro/data/usergateattributeinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergatecommentmessageinfomodel.py` & `lementpro-0.1.7/lementpro/data/usergatecommentmessageinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergatefolderobjectinfoattributemodel.py` & `lementpro-0.1.7/lementpro/data/usergatefolderobjectinfoattributemodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergatefolderobjectinfomodel.py` & `lementpro-0.1.7/lementpro/data/usergatefolderobjectinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergatefolderobjectinfomodellastcomment.py` & `lementpro-0.1.7/lementpro/data/usergatefolderobjectinfomodellastcomment.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergateobjectinfoattributemodel.py` & `lementpro-0.1.7/lementpro/data/usergatesearchobjectinfoattributemodel.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 from dataclasses import dataclass
 from lementpro.data.objecttypeattributeinfovaluelistmodel import ObjectTypeAttributeInfoValueListModel
 from lementpro.data.relationvalue import RelationValue
 @dataclass
-class UserGateObjectInfoAttributeModel:
+class UserGateSearchObjectInfoAttributeModel:
     id: int = None
     knownId: str = None
     name: str = None
     isSystem: bool = None
     value: str = None
     valueList: ObjectTypeAttributeInfoValueListModel = None
     relationValue: RelationValue = None
```

### Comparing `lementpro-0.1.6/lementpro/data/usergateobjectinfoextendedattributemodel.py` & `lementpro-0.1.7/lementpro/data/usergateobjectinfoextendedattributemodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergateobjectinfoextendedmodel.py` & `lementpro-0.1.7/lementpro/data/usergateobjectinfoextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergaterouteinstanceextendedmodel.py` & `lementpro-0.1.7/lementpro/data/usergaterouteinstanceextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/usergaterouteinstanceextendedmodelactivity.py` & `lementpro-0.1.7/lementpro/data/usergaterouteinstanceextendedmodelactivity.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userinfobysystemadminmodel.py` & `lementpro-0.1.7/lementpro/data/userinfobysystemadminmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userinfoextendedmodel.py` & `lementpro-0.1.7/lementpro/data/userinfoextendedmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userinfomodel.py` & `lementpro-0.1.7/lementpro/data/userinfomodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/data/userpatchmodel.py` & `lementpro-0.1.7/lementpro/data/userpatchmodel.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/sender.py` & `lementpro-0.1.7/lementpro/sender.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/accounts.py` & `lementpro-0.1.7/lementpro/services/accounts.py`

 * *Files 15% similar despite different names*

```diff
@@ -2,92 +2,98 @@
 from lementpro.data.user import User
 from lementpro.sender import Sender
 from lementpro.data.usermodelextension import UserModelExtension
 from lementpro.data.usermodelnotification import UserModelNotification
 
 
 class Accounts:
-    """Service for working with Accounts in UserGate Public API"""  
-    def login(self, by_user: User, login: str=None, password: str=None):
+    """Service for working with Accounts in UserGate Public API"""
+
+    def login(self, by_user: User, login: str = None, password: str = None):
         """Sign in by login
         :return: Access token model
         """
-        request_data = Build(url="/api/accounts/login").post(login=login,password=password,)
+        request_data = Build(
+            url="/api/accounts/login").post(login=login, password=password,)
         return Sender().send_request(request_data, by_user=by_user)
-          
-    def refresh_token(self, by_user: User, refreshToken: str=None):
+
+    def refresh_token(self, by_user: User, refreshToken: str = None):
         """Refresh token
         :return: Access token model
         """
-        request_data = Build(url="/api/accounts/refresh_token").post(refreshToken=refreshToken,)
+        request_data = Build(
+            url="/api/accounts/refresh_token").post(refreshToken=refreshToken,)
         return Sender().send_request(request_data, by_user=by_user)
-          
+
     def logout(self, by_user: User):
         """Sign out
         :return: No Content
         """
         request_data = Build(url="/api/accounts/logout").post()
         return Sender().send_request(request_data, by_user=by_user)
-          
-    def restore_password(self, by_user: User, login: str=None, companyId: int=None):
+
+    def restore_password(self, by_user: User, login: str = None, companyId: int = None):
         """Restore password
         :return: No Content
         """
-        request_data = Build(url="/api/accounts/restore_password").post(login=login,companyId=companyId,)
+        request_data = Build(
+            url="/api/accounts/restore_password").post(login=login, companyId=companyId,)
         return Sender().send_request(request_data, by_user=by_user)
-          
+
     def get_me(self, by_user: User):
         """Get me
         :return: Created BlockWork identifier
         """
         request_data = Build(url="/api/accounts/me").get()
         return Sender().send_request(request_data, by_user=by_user)
-          
-    def patch_me(self, by_user: User, userName: str=None, password: str=None, email: str=None, firstName: str=None, middleName: str=None, lastName: str=None, phoneNumber: str=None, preferredLocale: str=None, isDismissed: bool=None, isDisabled: bool=None, position: str=None, extension: UserModelExtension=None, role: str=None, notification: UserModelNotification=None):
+
+    def patch_me(self, by_user: User, userName: str = None, password: str = None, email: str = None, firstName: str = None, middleName: str = None, lastName: str = None, phoneNumber: str = None, preferredLocale: str = None, isDismissed: bool = None, isDisabled: bool = None, position: str = None, extension: UserModelExtension = None, role: str = None, notification: UserModelNotification = None):
         """Partial update user
         :return: No Content
         """
-        request_data = Build(url="/api/accounts/me").patch(userName=userName,password=password,email=email,firstName=firstName,middleName=middleName,lastName=lastName,phoneNumber=phoneNumber,preferredLocale=preferredLocale,isDismissed=isDismissed,isDisabled=isDisabled,position=position,extension=extension,role=role,notification=notification,)
+        request_data = Build(url="/api/accounts/me").patch(userName=userName, password=password, email=email, firstName=firstName, middleName=middleName, lastName=lastName, phoneNumber=phoneNumber,
+                                                           preferredLocale=preferredLocale, isDismissed=isDismissed, isDisabled=isDisabled, position=position, extension=extension, role=role, notification=notification,)
         return Sender().send_request(request_data, by_user=by_user)
-          
-    def change_password(self, by_user: User, oldPassword: str=None, newPassword: str=None):
+
+    def change_password(self, by_user: User, oldPassword: str = None, newPassword: str = None):
         """Change password
         :return: No Content
         """
-        request_data = Build(url="/api/accounts/change_password").put(oldPassword=oldPassword,newPassword=newPassword,)
+        request_data = Build(url="/api/accounts/change_password").put(
+            oldPassword=oldPassword, newPassword=newPassword,)
         return Sender().send_request(request_data, by_user=by_user)
-          
+
     def substitutionId(self, by_user: User):
         """Impersonate
         :return: Access token model
         """
-        request_data = Build(url="/api/accounts/impersonate/{substitutionId}").post()
+        request_data = Build(
+            url="/api/accounts/impersonate/{substitutionId}").post()
         return Sender().send_request(request_data, by_user=by_user)
-          
+
     def unimpersonate(self, by_user: User):
         """Unimpersonate
         :return: Access token model
         """
         request_data = Build(url="/api/accounts/unimpersonate").post()
         return Sender().send_request(request_data, by_user=by_user)
-          
+
     def debug_start(self, by_user: User):
         """Debug start
         :return: No Content
         """
         request_data = Build(url="/api/accounts/debug_start").post()
         return Sender().send_request(request_data, by_user=by_user)
-          
+
     def debug_end(self, by_user: User):
         """Debug end
         :return: No Content
         """
         request_data = Build(url="/api/accounts/debug_end").post()
         return Sender().send_request(request_data, by_user=by_user)
-          
+
     def substitutions(self, by_user: User):
         """Get account substitutions
         :return: User paging extended info
         """
         request_data = Build(url="/api/accounts/substitutions").get()
         return Sender().send_request(request_data, by_user=by_user)
-
```

### Comparing `lementpro-0.1.6/lementpro/services/admin.py` & `lementpro-0.1.7/lementpro/services/admin.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/comments.py` & `lementpro-0.1.7/lementpro/services/comments.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/connections.py` & `lementpro-0.1.7/lementpro/services/connections.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/departments.py` & `lementpro-0.1.7/lementpro/services/departments.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/files.py` & `lementpro-0.1.7/lementpro/services/files.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/folder.py` & `lementpro-0.1.7/lementpro/services/folder.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/groups.py` & `lementpro-0.1.7/lementpro/services/groups.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/localization.py` & `lementpro-0.1.7/lementpro/services/localization.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/objects.py` & `lementpro-0.1.7/lementpro/services/objects.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/objecttypes.py` & `lementpro-0.1.7/lementpro/services/objecttypes.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/routes.py` & `lementpro-0.1.7/lementpro/services/routes.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/search.py` & `lementpro-0.1.7/lementpro/services/search.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/timezones.py` & `lementpro-0.1.7/lementpro/services/timezones.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro/services/users.py` & `lementpro-0.1.7/lementpro/services/users.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/lementpro.egg-info/PKG-INFO` & `lementpro-0.1.7/lementpro.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lementpro
-Version: 0.1.6
+Version: 0.1.7
 Summary: Description of package
 Home-page: https://github.com/your_username/your_package_name
 Author: Author
 Author-email: your_email@example.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `lementpro-0.1.6/lementpro.egg-info/SOURCES.txt` & `lementpro-0.1.7/lementpro.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/setup.py` & `lementpro-0.1.7/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from setuptools import setup, find_packages
 
 with open("lementpro/readme.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setup(
     name="lementpro",
-    version="0.1.6",
+    version="0.1.7",
     author="Author",
     author_email="your_email@example.com",
     description="Description of package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/your_username/your_package_name",
     packages=find_packages(exclude=["src", "tests", "update_checker"]),
```

### Comparing `lementpro-0.1.6/src/templates/builders.py` & `lementpro-0.1.7/src/templates/builders.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/src/templates/sender.py` & `lementpro-0.1.7/src/templates/sender.py`

 * *Files identical despite different names*

### Comparing `lementpro-0.1.6/tests/test_sdk.py` & `lementpro-0.1.7/tests/test_sdk.py`

 * *Files identical despite different names*

