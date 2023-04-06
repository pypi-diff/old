# Comparing `tmp/pulumi_kubernetes-3.8.3.tar.gz` & `tmp/pulumi_kubernetes-3.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pulumi_kubernetes-3.8.3.tar", last modified: Fri Oct 29 18:44:08 2021, max compression
+gzip compressed data, was "dist/pulumi_kubernetes-3.9.0.tar", last modified: Fri Nov  5 16:18:53 2021, max compression
```

## Comparing `pulumi_kubernetes-3.8.3.tar` & `pulumi_kubernetes-3.9.0.tar`

### file list

```diff
@@ -1,496 +1,496 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/
--rw-r--r--   0 runner    (1001) docker     (121)    10975 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     8773 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/
--rw-r--r--   0 runner    (1001) docker     (121)    26559 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7256 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    40823 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/_tables.py
--rw-r--r--   0 runner    (1001) docker     (121)     7545 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/_utilities.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/
--rw-r--r--   0 runner    (1001) docker     (121)      595 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    11913 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfiguration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11535 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfigurationList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11983 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfiguration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11605 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfigurationList.py
--rw-r--r--   0 runner    (1001) docker     (121)      472 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    57921 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    55644 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    12173 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfiguration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11550 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfigurationList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12247 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfiguration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11620 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfigurationList.py
--rw-r--r--   0 runner    (1001) docker     (121)      472 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    58349 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    56284 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/
--rw-r--r--   0 runner    (1001) docker     (121)     5024 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/CustomResource.py
--rw-r--r--   0 runner    (1001) docker     (121)      637 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    12001 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinition.py
--rw-r--r--   0 runner    (1001) docker     (121)    11471 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinitionList.py
--rw-r--r--   0 runner    (1001) docker     (121)      368 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    90847 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    82987 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    11501 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinition.py
--rw-r--r--   0 runner    (1001) docker     (121)    10754 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinitionList.py
--rw-r--r--   0 runner    (1001) docker     (121)      368 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    96600 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    88183 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/
--rw-r--r--   0 runner    (1001) docker     (121)      571 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    11651 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/APIService.py
--rw-r--r--   0 runner    (1001) docker     (121)    11119 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/APIServiceList.py
--rw-r--r--   0 runner    (1001) docker     (121)      340 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19754 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18610 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    10921 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/APIService.py
--rw-r--r--   0 runner    (1001) docker     (121)    10059 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/APIServiceList.py
--rw-r--r--   0 runner    (1001) docker     (121)      340 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19323 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18203 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/
--rw-r--r--   0 runner    (1001) docker     (121)      677 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    13327 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ControllerRevision.py
--rw-r--r--   0 runner    (1001) docker     (121)    11117 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ControllerRevisionList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11945 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/DaemonSet.py
--rw-r--r--   0 runner    (1001) docker     (121)    10848 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/DaemonSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)    14527 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/Deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    10493 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/DeploymentList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12671 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ReplicaSet.py
--rw-r--r--   0 runner    (1001) docker     (121)    11245 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ReplicaSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)    13545 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/StatefulSet.py
--rw-r--r--   0 runner    (1001) docker     (121)    10968 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/StatefulSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)      580 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   113221 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)   112522 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    13337 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/ControllerRevision.py
--rw-r--r--   0 runner    (1001) docker     (121)    11132 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/ControllerRevisionList.py
--rw-r--r--   0 runner    (1001) docker     (121)    14113 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/Deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    10508 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/DeploymentList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12815 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/StatefulSet.py
--rw-r--r--   0 runner    (1001) docker     (121)     9873 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/StatefulSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)      470 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    64726 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    65242 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/
--rw-r--r--   0 runner    (1001) docker     (121)    13337 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ControllerRevision.py
--rw-r--r--   0 runner    (1001) docker     (121)    11132 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ControllerRevisionList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11955 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/DaemonSet.py
--rw-r--r--   0 runner    (1001) docker     (121)    10863 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/DaemonSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)    14113 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/Deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    10508 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/DeploymentList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12681 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ReplicaSet.py
--rw-r--r--   0 runner    (1001) docker     (121)    11260 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ReplicaSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12815 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/StatefulSet.py
--rw-r--r--   0 runner    (1001) docker     (121)     9873 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/StatefulSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)      580 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   107241 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)   106925 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/
--rw-r--r--   0 runner    (1001) docker     (121)      439 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)    10046 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/AuditSink.py
--rw-r--r--   0 runner    (1001) docker     (121)    10200 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/AuditSinkList.py
--rw-r--r--   0 runner    (1001) docker     (121)      338 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    16958 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16042 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/
--rw-r--r--   0 runner    (1001) docker     (121)      567 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    11270 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/TokenRequest.py
--rw-r--r--   0 runner    (1001) docker     (121)    11654 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/TokenReview.py
--rw-r--r--   0 runner    (1001) docker     (121)      339 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8426 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15448 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    10924 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/TokenReview.py
--rw-r--r--   0 runner    (1001) docker     (121)      311 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2298 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7512 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/
--rw-r--r--   0 runner    (1001) docker     (121)      563 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    12514 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/LocalSubjectAccessReview.py
--rw-r--r--   0 runner    (1001) docker     (121)    12260 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/SelfSubjectAccessReview.py
--rw-r--r--   0 runner    (1001) docker     (121)    12912 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/SelfSubjectRulesReview.py
--rw-r--r--   0 runner    (1001) docker     (121)    11688 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/SubjectAccessReview.py
--rw-r--r--   0 runner    (1001) docker     (121)      436 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14726 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    27762 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    11800 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/LocalSubjectAccessReview.py
--rw-r--r--   0 runner    (1001) docker     (121)    11546 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/SelfSubjectAccessReview.py
--rw-r--r--   0 runner    (1001) docker     (121)    12198 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/SelfSubjectRulesReview.py
--rw-r--r--   0 runner    (1001) docker     (121)    10974 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/SubjectAccessReview.py
--rw-r--r--   0 runner    (1001) docker     (121)      436 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14625 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    27563 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/
--rw-r--r--   0 runner    (1001) docker     (121)      719 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    12079 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscaler.py
--rw-r--r--   0 runner    (1001) docker     (121)    10875 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscalerList.py
--rw-r--r--   0 runner    (1001) docker     (121)      366 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15439 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15659 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    12641 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscaler.py
--rw-r--r--   0 runner    (1001) docker     (121)    11064 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscalerList.py
--rw-r--r--   0 runner    (1001) docker     (121)      366 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    68633 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    70973 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/
--rw-r--r--   0 runner    (1001) docker     (121)    12641 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscaler.py
--rw-r--r--   0 runner    (1001) docker     (121)    11072 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscalerList.py
--rw-r--r--   0 runner    (1001) docker     (121)      366 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    68777 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    69047 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/
--rw-r--r--   0 runner    (1001) docker     (121)      689 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    11937 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/CronJob.py
--rw-r--r--   0 runner    (1001) docker     (121)    10821 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/CronJobList.py
--rw-r--r--   0 runner    (1001) docker     (121)    14037 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/Job.py
--rw-r--r--   0 runner    (1001) docker     (121)    10679 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/JobList.py
--rw-r--r--   0 runner    (1001) docker     (121)      376 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    51359 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    49446 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    11979 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/CronJob.py
--rw-r--r--   0 runner    (1001) docker     (121)    10868 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/CronJobList.py
--rw-r--r--   0 runner    (1001) docker     (121)      334 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    16060 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15366 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)    11981 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/CronJob.py
--rw-r--r--   0 runner    (1001) docker     (121)    10871 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/CronJobList.py
--rw-r--r--   0 runner    (1001) docker     (121)      334 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15235 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14658 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/
--rw-r--r--   0 runner    (1001) docker     (121)      559 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    13239 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/CertificateSigningRequest.py
--rw-r--r--   0 runner    (1001) docker     (121)    10793 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/CertificateSigningRequestList.py
--rw-r--r--   0 runner    (1001) docker     (121)      370 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30590 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29777 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    11058 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequest.py
--rw-r--r--   0 runner    (1001) docker     (121)    10330 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequestList.py
--rw-r--r--   0 runner    (1001) docker     (121)      370 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    16931 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15390 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/
--rw-r--r--   0 runner    (1001) docker     (121)      559 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    11071 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/Lease.py
--rw-r--r--   0 runner    (1001) docker     (121)    10787 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/LeaseList.py
--rw-r--r--   0 runner    (1001) docker     (121)      330 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8155 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8067 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    11081 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/Lease.py
--rw-r--r--   0 runner    (1001) docker     (121)    10802 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/LeaseList.py
--rw-r--r--   0 runner    (1001) docker     (121)      330 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8160 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8072 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/
--rw-r--r--   0 runner    (1001) docker     (121)      377 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    11011 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Binding.py
--rw-r--r--   0 runner    (1001) docker     (121)    16129 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ConfigMap.py
--rw-r--r--   0 runner    (1001) docker     (121)    10796 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ConfigMapList.py
--rw-r--r--   0 runner    (1001) docker     (121)    13534 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Endpoints.py
--rw-r--r--   0 runner    (1001) docker     (121)    10788 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/EndpointsList.py
--rw-r--r--   0 runner    (1001) docker     (121)    28655 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Event.py
--rw-r--r--   0 runner    (1001) docker     (121)    10650 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/EventList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11201 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/LimitRange.py
--rw-r--r--   0 runner    (1001) docker     (121)    11271 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/LimitRangeList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11649 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)    11278 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/NamespaceList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11520 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Node.py
--rw-r--r--   0 runner    (1001) docker     (121)    10717 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/NodeList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12267 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolume.py
--rw-r--r--   0 runner    (1001) docker     (121)    12099 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolumeClaim.py
--rw-r--r--   0 runner    (1001) docker     (121)    11628 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolumeClaimList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11349 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolumeList.py
--rw-r--r--   0 runner    (1001) docker     (121)    13454 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Pod.py
--rw-r--r--   0 runner    (1001) docker     (121)    10964 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PodList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11392 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PodTemplate.py
--rw-r--r--   0 runner    (1001) docker     (121)    10864 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PodTemplateList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12833 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ReplicationController.py
--rw-r--r--   0 runner    (1001) docker     (121)    11596 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ReplicationControllerList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11656 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ResourceQuota.py
--rw-r--r--   0 runner    (1001) docker     (121)    11300 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ResourceQuotaList.py
--rw-r--r--   0 runner    (1001) docker     (121)    18491 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Secret.py
--rw-r--r--   0 runner    (1001) docker     (121)    11031 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/SecretList.py
--rw-r--r--   0 runner    (1001) docker     (121)    14899 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Service.py
--rw-r--r--   0 runner    (1001) docker     (121)    17021 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ServiceAccount.py
--rw-r--r--   0 runner    (1001) docker     (121)    11361 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ServiceAccountList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10748 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ServiceList.py
--rw-r--r--   0 runner    (1001) docker     (121)     1185 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      376 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   783884 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)   755062 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/
--rw-r--r--   0 runner    (1001) docker     (121)      547 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    16343 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/EndpointSlice.py
--rw-r--r--   0 runner    (1001) docker     (121)    10598 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/EndpointSliceList.py
--rw-r--r--   0 runner    (1001) docker     (121)      346 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    23463 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22370 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    16353 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/EndpointSlice.py
--rw-r--r--   0 runner    (1001) docker     (121)    10613 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/EndpointSliceList.py
--rw-r--r--   0 runner    (1001) docker     (121)      346 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    23905 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22915 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/
--rw-r--r--   0 runner    (1001) docker     (121)      535 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    33518 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/Event.py
--rw-r--r--   0 runner    (1001) docker     (121)    10799 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/EventList.py
--rw-r--r--   0 runner    (1001) docker     (121)      330 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    17392 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16520 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    33052 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/Event.py
--rw-r--r--   0 runner    (1001) docker     (121)    10814 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/EventList.py
--rw-r--r--   0 runner    (1001) docker     (121)      330 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    17553 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16275 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/
--rw-r--r--   0 runner    (1001) docker     (121)      419 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    11967 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/DaemonSet.py
--rw-r--r--   0 runner    (1001) docker     (121)    10881 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/DaemonSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)    14125 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/Deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    10526 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/DeploymentList.py
--rw-r--r--   0 runner    (1001) docker     (121)    13819 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/Ingress.py
--rw-r--r--   0 runner    (1001) docker     (121)    10859 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/IngressList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11364 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/NetworkPolicy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11241 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/NetworkPolicyList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11438 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11315 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicyList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12693 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/ReplicaSet.py
--rw-r--r--   0 runner    (1001) docker     (121)    11278 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/ReplicaSetList.py
--rw-r--r--   0 runner    (1001) docker     (121)      632 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   173774 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)   172182 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/
--rw-r--r--   0 runner    (1001) docker     (121)      591 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)    12449 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchema.py
--rw-r--r--   0 runner    (1001) docker     (121)    11055 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchemaList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12645 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfiguration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11595 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfigurationList.py
--rw-r--r--   0 runner    (1001) docker     (121)      428 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    55970 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    55866 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    12447 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchema.py
--rw-r--r--   0 runner    (1001) docker     (121)    11052 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchemaList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12643 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfiguration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11592 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfigurationList.py
--rw-r--r--   0 runner    (1001) docker     (121)      428 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    56602 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    56456 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/
--rw-r--r--   0 runner    (1001) docker     (121)      497 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v2/
--rw-r--r--   0 runner    (1001) docker     (121)      259 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    26621 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v2/helm.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/
--rw-r--r--   0 runner    (1001) docker     (121)    48370 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/Release.py
--rw-r--r--   0 runner    (1001) docker     (121)      327 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3987 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25927 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/helm.py
--rw-r--r--   0 runner    (1001) docker     (121)     7175 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6488 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/kustomize.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/
--rw-r--r--   0 runner    (1001) docker     (121)      377 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    15641 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/Status.py
--rw-r--r--   0 runner    (1001) docker     (121)      306 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    60033 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    57187 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/
--rw-r--r--   0 runner    (1001) docker     (121)      551 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    13823 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/Ingress.py
--rw-r--r--   0 runner    (1001) docker     (121)    12129 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/IngressClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    10590 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/IngressClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10865 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/IngressList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11170 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/NetworkPolicy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11029 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/NetworkPolicyList.py
--rw-r--r--   0 runner    (1001) docker     (121)      456 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    66515 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    67834 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    13833 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/Ingress.py
--rw-r--r--   0 runner    (1001) docker     (121)    12169 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/IngressClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    10635 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/IngressClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10880 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/IngressList.py
--rw-r--r--   0 runner    (1001) docker     (121)      394 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    32522 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34112 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/
--rw-r--r--   0 runner    (1001) docker     (121)      683 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    18091 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/RuntimeClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11010 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/RuntimeClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)      344 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11166 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11752 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)    12272 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/RuntimeClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11028 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/RuntimeClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)      344 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12470 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13782 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    18093 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/RuntimeClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11025 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/RuntimeClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)      344 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11167 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11767 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     1685 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/
--rw-r--r--   0 runner    (1001) docker     (121)      535 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    11723 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/PodDisruptionBudget.py
--rw-r--r--   0 runner    (1001) docker     (121)    11216 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/PodDisruptionBudgetList.py
--rw-r--r--   0 runner    (1001) docker     (121)      358 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    17029 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16738 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    11733 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudget.py
--rw-r--r--   0 runner    (1001) docker     (121)    11271 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudgetList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11340 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11165 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicyList.py
--rw-r--r--   0 runner    (1001) docker     (121)      428 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    63293 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    59584 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18562 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/provider.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/
--rw-r--r--   0 runner    (1001) docker     (121)      683 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    13278 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRole.py
--rw-r--r--   0 runner    (1001) docker     (121)    12986 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRoleBinding.py
--rw-r--r--   0 runner    (1001) docker     (121)    10820 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRoleBindingList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10575 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRoleList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10825 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/Role.py
--rw-r--r--   0 runner    (1001) docker     (121)    13263 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/RoleBinding.py
--rw-r--r--   0 runner    (1001) docker     (121)    10575 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/RoleBindingList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10330 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/RoleList.py
--rw-r--r--   0 runner    (1001) docker     (121)      516 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    29899 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29985 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)    13516 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRole.py
--rw-r--r--   0 runner    (1001) docker     (121)    13238 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBinding.py
--rw-r--r--   0 runner    (1001) docker     (121)    11082 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBindingList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10823 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11049 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/Role.py
--rw-r--r--   0 runner    (1001) docker     (121)    13501 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/RoleBinding.py
--rw-r--r--   0 runner    (1001) docker     (121)    10827 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/RoleBindingList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10570 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/RoleList.py
--rw-r--r--   0 runner    (1001) docker     (121)      516 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30447 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    30983 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    13514 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRole.py
--rw-r--r--   0 runner    (1001) docker     (121)    13236 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBinding.py
--rw-r--r--   0 runner    (1001) docker     (121)    11085 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBindingList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10820 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRoleList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11047 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/Role.py
--rw-r--r--   0 runner    (1001) docker     (121)    13499 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/RoleBinding.py
--rw-r--r--   0 runner    (1001) docker     (121)    10824 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/RoleBindingList.py
--rw-r--r--   0 runner    (1001) docker     (121)    10565 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/RoleList.py
--rw-r--r--   0 runner    (1001) docker     (121)      516 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30611 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    31149 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/
--rw-r--r--   0 runner    (1001) docker     (121)      719 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    17523 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/PriorityClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11035 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/PriorityClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)      346 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7406 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7043 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)    17739 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/PriorityClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11053 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/PriorityClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)      346 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7514 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7253 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    17853 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/PriorityClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11050 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/PriorityClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)      346 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7571 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7310 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/
--rw-r--r--   0 runner    (1001) docker     (121)      421 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)     9767 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/PodPreset.py
--rw-r--r--   0 runner    (1001) docker     (121)    10947 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/PodPresetList.py
--rw-r--r--   0 runner    (1001) docker     (121)      338 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7830 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7378 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/
--rw-r--r--   0 runner    (1001) docker     (121)      701 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/
--rw-r--r--   0 runner    (1001) docker     (121)    12784 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSIDriver.py
--rw-r--r--   0 runner    (1001) docker     (121)    10888 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSIDriverList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11612 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSINode.py
--rw-r--r--   0 runner    (1001) docker     (121)    10818 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSINodeList.py
--rw-r--r--   0 runner    (1001) docker     (121)    22862 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/StorageClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11021 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/StorageClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12089 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/VolumeAttachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    11167 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/VolumeAttachmentList.py
--rw-r--r--   0 runner    (1001) docker     (121)      516 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    59027 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    59018 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/
--rw-r--r--   0 runner    (1001) docker     (121)    23707 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacity.py
--rw-r--r--   0 runner    (1001) docker     (121)    11257 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacityList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12101 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/VolumeAttachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    11185 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/VolumeAttachmentList.py
--rw-r--r--   0 runner    (1001) docker     (121)      424 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    25441 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    26398 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/
--rw-r--r--   0 runner    (1001) docker     (121)    13264 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIDriver.py
--rw-r--r--   0 runner    (1001) docker     (121)    10903 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIDriverList.py
--rw-r--r--   0 runner    (1001) docker     (121)    11622 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSINode.py
--rw-r--r--   0 runner    (1001) docker     (121)    10833 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSINodeList.py
--rw-r--r--   0 runner    (1001) docker     (121)    23705 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacity.py
--rw-r--r--   0 runner    (1001) docker     (121)    11254 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacityList.py
--rw-r--r--   0 runner    (1001) docker     (121)    22872 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/StorageClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    11036 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/StorageClassList.py
--rw-r--r--   0 runner    (1001) docker     (121)    12099 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/VolumeAttachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    11182 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/VolumeAttachmentList.py
--rw-r--r--   0 runner    (1001) docker     (121)      588 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    68708 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    69504 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    90525 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes/yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    10975 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    19735 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       83 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       18 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-10-29 18:44:07.000000 pulumi_kubernetes-3.8.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2111 2021-10-29 18:44:06.000000 pulumi_kubernetes-3.8.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/
+-rw-r--r--   0 runner    (1001) docker     (121)    11002 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     8773 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/
+-rw-r--r--   0 runner    (1001) docker     (121)    26559 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7256 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40823 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/_tables.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7636 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/_utilities.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/
+-rw-r--r--   0 runner    (1001) docker     (121)      595 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11913 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfiguration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11535 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfigurationList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11983 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfiguration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11605 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfigurationList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      472 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57921 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55644 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12173 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfiguration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11550 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfigurationList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12247 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfiguration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11620 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfigurationList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      472 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58349 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    56284 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/
+-rw-r--r--   0 runner    (1001) docker     (121)     9255 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/CustomResource.py
+-rw-r--r--   0 runner    (1001) docker     (121)      637 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12001 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11471 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinitionList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      368 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    90847 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    82987 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11501 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10754 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinitionList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      368 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    96600 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    88183 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/
+-rw-r--r--   0 runner    (1001) docker     (121)      571 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11651 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/APIService.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11119 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/APIServiceList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      340 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19754 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18610 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    10921 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/APIService.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10059 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/APIServiceList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      340 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19323 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18203 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/
+-rw-r--r--   0 runner    (1001) docker     (121)      677 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13327 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ControllerRevision.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11117 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ControllerRevisionList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11945 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/DaemonSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10848 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/DaemonSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14527 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/Deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10493 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/DeploymentList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12671 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ReplicaSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11245 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ReplicaSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13545 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/StatefulSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10968 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/StatefulSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      580 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   113221 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)   112522 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13337 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/ControllerRevision.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11132 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/ControllerRevisionList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14113 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/Deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10508 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/DeploymentList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12815 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/StatefulSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9873 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/StatefulSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      470 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64726 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    65242 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/
+-rw-r--r--   0 runner    (1001) docker     (121)    13337 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ControllerRevision.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11132 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ControllerRevisionList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11955 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/DaemonSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10863 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/DaemonSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14113 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/Deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10508 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/DeploymentList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12681 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ReplicaSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11260 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ReplicaSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12815 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/StatefulSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9873 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/StatefulSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      580 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   107241 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)   106925 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/
+-rw-r--r--   0 runner    (1001) docker     (121)      439 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)    10046 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/AuditSink.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10200 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/AuditSinkList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      338 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16958 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16042 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/
+-rw-r--r--   0 runner    (1001) docker     (121)      567 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11270 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/TokenRequest.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11654 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/TokenReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)      339 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8426 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15448 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    10924 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/TokenReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)      311 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2298 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7512 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/
+-rw-r--r--   0 runner    (1001) docker     (121)      563 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12514 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/LocalSubjectAccessReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12260 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/SelfSubjectAccessReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12912 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/SelfSubjectRulesReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11688 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/SubjectAccessReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)      436 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14726 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27762 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11800 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/LocalSubjectAccessReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11546 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/SelfSubjectAccessReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12198 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/SelfSubjectRulesReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10974 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/SubjectAccessReview.py
+-rw-r--r--   0 runner    (1001) docker     (121)      436 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14625 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27563 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/
+-rw-r--r--   0 runner    (1001) docker     (121)      719 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12079 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscaler.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10875 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscalerList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      366 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15439 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15659 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12641 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscaler.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11064 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscalerList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      366 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    68633 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70973 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/
+-rw-r--r--   0 runner    (1001) docker     (121)    12641 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscaler.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11072 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscalerList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      366 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    68777 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69047 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/
+-rw-r--r--   0 runner    (1001) docker     (121)      689 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11937 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/CronJob.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10821 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/CronJobList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14037 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/Job.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10679 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/JobList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      376 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51359 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49446 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11979 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/CronJob.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10868 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/CronJobList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      334 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16060 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15366 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11981 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/CronJob.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10871 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/CronJobList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      334 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15235 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14658 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/
+-rw-r--r--   0 runner    (1001) docker     (121)      559 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13239 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/CertificateSigningRequest.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10793 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/CertificateSigningRequestList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      370 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30590 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29777 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11058 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequest.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10330 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequestList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      370 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16931 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15390 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/
+-rw-r--r--   0 runner    (1001) docker     (121)      559 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11071 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/Lease.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10787 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/LeaseList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      330 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8155 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8067 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11081 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/Lease.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10802 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/LeaseList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      330 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8160 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8072 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/
+-rw-r--r--   0 runner    (1001) docker     (121)      377 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11011 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Binding.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16129 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ConfigMap.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10796 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ConfigMapList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13534 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Endpoints.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10788 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/EndpointsList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28655 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Event.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10650 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/EventList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11201 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/LimitRange.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11271 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/LimitRangeList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11649 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11278 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/NamespaceList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11520 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Node.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10717 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/NodeList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12267 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolume.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12099 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolumeClaim.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11628 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolumeClaimList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11349 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolumeList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13454 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Pod.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10964 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PodList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11392 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PodTemplate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10864 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PodTemplateList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12833 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ReplicationController.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11596 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ReplicationControllerList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11656 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ResourceQuota.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11300 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ResourceQuotaList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18491 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Secret.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11031 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/SecretList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14899 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17021 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ServiceAccount.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11361 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ServiceAccountList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10748 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ServiceList.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1185 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      376 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   783884 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)   755062 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/
+-rw-r--r--   0 runner    (1001) docker     (121)      547 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    16343 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/EndpointSlice.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10598 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/EndpointSliceList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23463 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22370 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    16353 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/EndpointSlice.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10613 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/EndpointSliceList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23905 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22915 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/
+-rw-r--r--   0 runner    (1001) docker     (121)      535 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    33518 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/Event.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10799 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/EventList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      330 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17392 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16520 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    33052 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/Event.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10814 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/EventList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      330 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17553 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16275 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/
+-rw-r--r--   0 runner    (1001) docker     (121)      419 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11967 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/DaemonSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10881 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/DaemonSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14125 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/Deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10526 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/DeploymentList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13819 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/Ingress.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10859 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/IngressList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11364 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/NetworkPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11241 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/NetworkPolicyList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11438 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11315 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicyList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12693 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/ReplicaSet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11278 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/ReplicaSetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      632 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   173774 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)   172182 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/
+-rw-r--r--   0 runner    (1001) docker     (121)      591 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12449 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchema.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11055 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchemaList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12645 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfiguration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11595 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfigurationList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      428 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55970 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55866 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12447 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchema.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11052 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchemaList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12643 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfiguration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11592 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfigurationList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      428 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    56602 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    56456 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/
+-rw-r--r--   0 runner    (1001) docker     (121)      497 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v2/
+-rw-r--r--   0 runner    (1001) docker     (121)      259 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27358 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v2/helm.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/
+-rw-r--r--   0 runner    (1001) docker     (121)    48370 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/Release.py
+-rw-r--r--   0 runner    (1001) docker     (121)      327 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3987 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26664 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/helm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7175 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6488 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/kustomize.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/
+-rw-r--r--   0 runner    (1001) docker     (121)      377 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    15641 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/Status.py
+-rw-r--r--   0 runner    (1001) docker     (121)      306 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    60033 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57187 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/
+-rw-r--r--   0 runner    (1001) docker     (121)      551 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13823 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/Ingress.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12129 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/IngressClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10590 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/IngressClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10865 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/IngressList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11170 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/NetworkPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11029 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/NetworkPolicyList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      456 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    66515 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    67834 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13833 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/Ingress.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12169 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/IngressClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10635 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/IngressClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10880 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/IngressList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      394 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32522 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34112 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/
+-rw-r--r--   0 runner    (1001) docker     (121)      683 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    18091 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/RuntimeClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11010 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/RuntimeClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      344 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11166 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11752 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12272 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/RuntimeClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11028 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/RuntimeClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      344 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12470 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13782 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    18093 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/RuntimeClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11025 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/RuntimeClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      344 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11167 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11767 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1685 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/
+-rw-r--r--   0 runner    (1001) docker     (121)      535 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11723 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/PodDisruptionBudget.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11216 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/PodDisruptionBudgetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      358 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17029 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16738 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11733 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudget.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11271 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudgetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11340 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11165 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicyList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      428 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    63293 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59584 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18562 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/
+-rw-r--r--   0 runner    (1001) docker     (121)      683 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13278 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRole.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12986 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRoleBinding.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10820 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRoleBindingList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10575 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRoleList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10825 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/Role.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13263 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/RoleBinding.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10575 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/RoleBindingList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10330 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/RoleList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      516 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29899 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29985 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13516 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRole.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13238 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBinding.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11082 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBindingList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10823 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11049 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/Role.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13501 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/RoleBinding.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10827 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/RoleBindingList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10570 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/RoleList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      516 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30447 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30983 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13514 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRole.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13236 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBinding.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11085 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBindingList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10820 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRoleList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11047 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/Role.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13499 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/RoleBinding.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10824 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/RoleBindingList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10565 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/RoleList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      516 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30611 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31149 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/
+-rw-r--r--   0 runner    (1001) docker     (121)      719 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    17523 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/PriorityClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11035 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/PriorityClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7406 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7043 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)    17739 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/PriorityClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11053 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/PriorityClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7514 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7253 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    17853 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/PriorityClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11050 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/PriorityClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7571 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7310 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/
+-rw-r--r--   0 runner    (1001) docker     (121)      421 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)     9767 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/PodPreset.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10947 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/PodPresetList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      338 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7830 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7378 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/
+-rw-r--r--   0 runner    (1001) docker     (121)      701 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/
+-rw-r--r--   0 runner    (1001) docker     (121)    12784 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSIDriver.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10888 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSIDriverList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11612 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSINode.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10818 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSINodeList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22862 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/StorageClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11021 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/StorageClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12089 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/VolumeAttachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11167 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/VolumeAttachmentList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      516 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59027 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59018 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/
+-rw-r--r--   0 runner    (1001) docker     (121)    23707 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacity.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11257 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacityList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12101 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/VolumeAttachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11185 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/VolumeAttachmentList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25441 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26398 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/
+-rw-r--r--   0 runner    (1001) docker     (121)    13264 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIDriver.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10903 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIDriverList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11622 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSINode.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10833 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSINodeList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23705 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacity.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11254 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacityList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22872 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/StorageClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11036 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/StorageClassList.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12099 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/VolumeAttachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11182 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/VolumeAttachmentList.py
+-rw-r--r--   0 runner    (1001) docker     (121)      588 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    68708 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69504 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    90525 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes/yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    11002 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    19735 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       83 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2021-11-05 16:18:53.000000 pulumi_kubernetes-3.9.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2138 2021-11-05 16:18:51.000000 pulumi_kubernetes-3.9.0/setup.py
```

### Comparing `pulumi_kubernetes-3.8.3/PKG-INFO` & `pulumi_kubernetes-3.9.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi_kubernetes
-Version: 3.8.3
+Version: 3.9.0
 Summary: A Pulumi package for creating and managing Kubernetes resources.
 Home-page: https://pulumi.com
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-kubernetes
 Description: [![Build Status](https://travis-ci.com/pulumi/pulumi-kubernetes.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/pulumi-kubernetes)
         [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
         [![NPM version](https://badge.fury.io/js/%40pulumi%2Fkubernetes.svg)](https://www.npmjs.com/package/@pulumi/kubernetes)
@@ -233,10 +233,10 @@
         
         [pulumi-kubernetes]: https://github.com/pulumi/pulumi-kubernetes
         [contributing]: CONTRIBUTING.md
         [code-of-conduct]: CODE-OF-CONDUCT.md
         [workload-example]: #deploying-a-workload-on-aws-eks
         [how-pulumi-works]: https://www.pulumi.com/docs/intro/concepts/how-pulumi-works
         
-Keywords: pulumi kubernetes
+Keywords: pulumi kubernetes category/cloud kind/native
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pulumi_kubernetes Version: 3.8.3 Summary: A Pulumi
+Metadata-Version: 2.1 Name: pulumi_kubernetes Version: 3.9.0 Summary: A Pulumi
 package for creating and managing Kubernetes resources. Home-page: https://
 pulumi.com License: Apache-2.0 Project-URL: Repository, https://github.com/
 pulumi/pulumi-kubernetes Description: [![Build Status](https://travis-ci.com/
 pulumi/pulumi-kubernetes.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https:/
 /travis-ci.com/pulumi/pulumi-kubernetes) [![Slack](http://www.pulumi.com/
 images/docs/badges/slack.svg)](https://slack.pulumi.com) [![NPM version](https:
 //badge.fury.io/js/%40pulumi%2Fkubernetes.svg)](https://www.npmjs.com/package/
@@ -107,9 +107,9 @@
 cluster's kubeconfig. export const kubeconfig = cluster.kubeconfig; ``` ##
 Contributing If you are interested in contributing, please see the
 [contributing docs][contributing]. ## Code of Conduct You can read the code of
 conduct [here][code-of-conduct]. [pulumi-kubernetes]: https://github.com/
 pulumi/pulumi-kubernetes [contributing]: CONTRIBUTING.md [code-of-conduct]:
 CODE-OF-CONDUCT.md [workload-example]: #deploying-a-workload-on-aws-eks [how-
 pulumi-works]: https://www.pulumi.com/docs/intro/concepts/how-pulumi-works
-Keywords: pulumi kubernetes Platform: UNKNOWN Description-Content-Type: text/
-markdown
+Keywords: pulumi kubernetes category/cloud kind/native Platform: UNKNOWN
+Description-Content-Type: text/markdown
```

### Comparing `pulumi_kubernetes-3.8.3/README.md` & `pulumi_kubernetes-3.9.0/README.md`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/_tables.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/_tables.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/_utilities.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/_utilities.py`

 * *Files 2% similar despite different names*

```diff
@@ -220,16 +220,17 @@
     """Decorator internally used on {fn}_output lifted function versions
     to implement them automatically from the un-lifted function."""
 
     func_sig = inspect.signature(func)
 
     def lifted_func(*args, opts=None, **kwargs):
         bound_args = func_sig.bind(*args, **kwargs)
-
+        # Convert tuple to list, see pulumi/pulumi#8172
+        args_list = list(bound_args.args)
         return pulumi.Output.from_input({
-            'args': bound_args.args,
+            'args': args_list,
             'kwargs': bound_args.kwargs
         }).apply(lambda resolved_args: func(*resolved_args['args'],
                                             opts=opts,
                                             **resolved_args['kwargs']))
 
     return (lambda _: lifted_func)
```

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfiguration.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfiguration.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfigurationList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/MutatingWebhookConfigurationList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfiguration.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfiguration.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfigurationList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/ValidatingWebhookConfigurationList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfiguration.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfiguration.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfigurationList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/MutatingWebhookConfigurationList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfiguration.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfiguration.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfigurationList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/ValidatingWebhookConfigurationList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/admissionregistration/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/admissionregistration/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinition.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinition.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinitionList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/CustomResourceDefinitionList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinition.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinition.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinitionList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/CustomResourceDefinitionList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiextensions/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiextensions/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/APIService.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/APIService.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/APIServiceList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/APIServiceList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/APIService.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/APIService.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/APIServiceList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/APIServiceList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apiregistration/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apiregistration/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ControllerRevision.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ControllerRevision.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ControllerRevisionList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ControllerRevisionList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/DaemonSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/DaemonSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/DaemonSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/DaemonSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/Deployment.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/Deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/DeploymentList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/DeploymentList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ReplicaSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ReplicaSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/ReplicaSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/ReplicaSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/StatefulSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/StatefulSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/StatefulSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/StatefulSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/ControllerRevision.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/ControllerRevision.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/ControllerRevisionList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/ControllerRevisionList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/Deployment.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/Deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/DeploymentList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/DeploymentList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/StatefulSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/StatefulSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/StatefulSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/StatefulSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ControllerRevision.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ControllerRevision.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ControllerRevisionList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ControllerRevisionList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/DaemonSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/DaemonSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/DaemonSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/DaemonSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/Deployment.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/Deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/DeploymentList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/DeploymentList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ReplicaSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ReplicaSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/ReplicaSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/ReplicaSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/StatefulSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/StatefulSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/StatefulSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/StatefulSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/apps/v1beta2/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/apps/v1beta2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/AuditSink.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/AuditSink.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/AuditSinkList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/AuditSinkList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/auditregistration/v1alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/auditregistration/v1alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/TokenRequest.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/TokenRequest.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/TokenReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/TokenReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/TokenReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/TokenReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authentication/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authentication/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/LocalSubjectAccessReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/LocalSubjectAccessReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/SelfSubjectAccessReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/SelfSubjectAccessReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/SelfSubjectRulesReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/SelfSubjectRulesReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/SubjectAccessReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/SubjectAccessReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/LocalSubjectAccessReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/LocalSubjectAccessReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/SelfSubjectAccessReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/SelfSubjectAccessReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/SelfSubjectRulesReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/SelfSubjectRulesReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/SubjectAccessReview.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/SubjectAccessReview.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/authorization/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/authorization/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscaler.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscaler.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscalerList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/HorizontalPodAutoscalerList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscaler.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscaler.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscalerList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/HorizontalPodAutoscalerList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscaler.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscaler.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscalerList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/HorizontalPodAutoscalerList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/autoscaling/v2beta2/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/autoscaling/v2beta2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/CronJob.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/CronJob.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/CronJobList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/CronJobList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/Job.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/Job.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/JobList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/JobList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/CronJob.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/CronJob.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/CronJobList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/CronJobList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/CronJob.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/CronJob.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/CronJobList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/CronJobList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/batch/v2alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/batch/v2alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/CertificateSigningRequest.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/CertificateSigningRequest.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/CertificateSigningRequestList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/CertificateSigningRequestList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequest.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequest.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequestList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/CertificateSigningRequestList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/certificates/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/certificates/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/Lease.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/Lease.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/LeaseList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/LeaseList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/Lease.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/Lease.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/LeaseList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/LeaseList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/coordination/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/coordination/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Binding.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Binding.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ConfigMap.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ConfigMap.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ConfigMapList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ConfigMapList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Endpoints.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Endpoints.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/EndpointsList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/EndpointsList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Event.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Event.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/EventList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/EventList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/LimitRange.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/LimitRange.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/LimitRangeList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/LimitRangeList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Namespace.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/NamespaceList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/NamespaceList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Node.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Node.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/NodeList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/NodeList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolume.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolume.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolumeClaim.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolumeClaim.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolumeClaimList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolumeClaimList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PersistentVolumeList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PersistentVolumeList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Pod.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Pod.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PodList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PodList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PodTemplate.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PodTemplate.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/PodTemplateList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/PodTemplateList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ReplicationController.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ReplicationController.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ReplicationControllerList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ReplicationControllerList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ResourceQuota.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ResourceQuota.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ResourceQuotaList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ResourceQuotaList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Secret.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/SecretList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/SecretList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/Service.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/Service.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ServiceAccount.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ServiceAccount.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ServiceAccountList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ServiceAccountList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/ServiceList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/ServiceList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/core/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/core/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/EndpointSlice.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/EndpointSlice.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/EndpointSliceList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/EndpointSliceList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/EndpointSlice.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/EndpointSlice.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/EndpointSliceList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/EndpointSliceList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/discovery/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/discovery/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/Event.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/Event.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/EventList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/EventList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/Event.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/Event.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/EventList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/EventList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/events/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/events/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/DaemonSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/DaemonSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/DaemonSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/DaemonSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/Deployment.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/Deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/DeploymentList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/DeploymentList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/Ingress.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/Ingress.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/IngressList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/IngressList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/NetworkPolicy.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/NetworkPolicy.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/NetworkPolicyList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/NetworkPolicyList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicy.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicy.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicyList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/PodSecurityPolicyList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/ReplicaSet.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/ReplicaSet.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/ReplicaSetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/ReplicaSetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/extensions/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/extensions/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchema.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchema.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchemaList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/FlowSchemaList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfiguration.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfiguration.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfigurationList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/PriorityLevelConfigurationList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchema.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchema.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchemaList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/FlowSchemaList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfiguration.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfiguration.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfigurationList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/PriorityLevelConfigurationList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/flowcontrol/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/flowcontrol/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v2/helm.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v2/helm.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,21 @@
+#  Copyright 2016-2021, Pulumi Corporation.
+#
+#  Licensed under the Apache License, Version 2.0 (the "License");
+#  you may not use this file except in compliance with the License.
+#  You may obtain a copy of the License at
+#
+#      http://www.apache.org/licenses/LICENSE-2.0
+#
+#  Unless required by applicable law or agreed to in writing, software
+#  distributed under the License is distributed on an "AS IS" BASIS,
+#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
+#  See the License for the specific language governing permissions and
+#  limitations under the License.
+
 # *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
 # *** Do not edit by hand unless you're certain you know what you are doing! ***
 
 import json
 import os.path
 import re
 import shutil
@@ -16,14 +30,15 @@
 
 
 class Chart(pulumi.ComponentResource):
     resources: pulumi.Output[dict]
     """
     Kubernetes resources contained in this Chart.
     """
+    ready: pulumi.Output[Sequence[pulumi.Output[pulumi.Resource]]]
 
     def __init__(self,
                  release_name: str,
                  config: Union['ChartOpts', 'LocalChartOpts'],
                  opts: Optional[pulumi.ResourceOptions] = None):
         """
         Chart is a component representing a collection of resources described by an arbitrary Helm
@@ -176,14 +191,15 @@
         all_config = pulumi.Output.from_input((release_name, config, pulumi.ResourceOptions(parent=self)))
 
         # Note: Unlike NodeJS, Python requires that we "pull" on our futures in order to get them scheduled for
         # execution. In order to do this, we leverage the engine's RegisterResourceOutputs to wait for the
         # resolution of all resources that this Helm chart created.
         self.resources = all_config.apply(_parse_chart)
         self.register_outputs({"resources": self.resources})
+        self.ready = self.resources.apply(lambda x: list(x.values()))
 
     def get_resource(self,
                      group_version_kind: str,
                      name: str,
                      namespace: Optional[str] = None) -> pulumi.Output[pulumi.CustomResource]:
         """
         get_resource returns a resource defined by a built-in Kubernetes group/version/kind and
```

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/Release.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/Release.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/helm.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/helm.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,7 +1,21 @@
+#  Copyright 2016-2021, Pulumi Corporation.
+#
+#  Licensed under the Apache License, Version 2.0 (the "License");
+#  you may not use this file except in compliance with the License.
+#  You may obtain a copy of the License at
+#
+#      http://www.apache.org/licenses/LICENSE-2.0
+#
+#  Unless required by applicable law or agreed to in writing, software
+#  distributed under the License is distributed on an "AS IS" BASIS,
+#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
+#  See the License for the specific language governing permissions and
+#  limitations under the License.
+
 # *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
 # *** Do not edit by hand unless you're certain you know what you are doing! ***
 
 import json
 from typing import Any, Callable, Optional, Sequence, Tuple, Union
 
 import pulumi.runtime
@@ -11,14 +25,15 @@
 
 
 class Chart(pulumi.ComponentResource):
     resources: pulumi.Output[dict]
     """
     Kubernetes resources contained in this Chart.
     """
+    ready: pulumi.Output[Sequence[pulumi.Output[pulumi.Resource]]]
 
     def __init__(self,
                  release_name: str,
                  config: Union['ChartOpts', 'LocalChartOpts'],
                  opts: Optional[pulumi.ResourceOptions] = None):
         """
         Chart is a component representing a collection of resources described by an arbitrary Helm
@@ -177,14 +192,15 @@
         all_config = pulumi.Output.from_input((config, pulumi.ResourceOptions(parent=self)))
 
         # Note: Unlike NodeJS, Python requires that we "pull" on our futures in order to get them scheduled for
         # execution. In order to do this, we leverage the engine's RegisterResourceOutputs to wait for the
         # resolution of all resources that this Helm chart created.
         self.resources = all_config.apply(_parse_chart)
         self.register_outputs({"resources": self.resources})
+        self.ready = self.resources.apply(lambda x: list(x.values()))
 
     def get_resource(self,
                      group_version_kind: str,
                      name: str,
                      namespace: Optional[str] = None) -> pulumi.Output[pulumi.CustomResource]:
         """
         get_resource returns a resource defined by a built-in Kubernetes group/version/kind and
```

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/helm/v3/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/helm/v3/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/kustomize.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/kustomize.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/Status.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/Status.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/meta/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/meta/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/Ingress.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/Ingress.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/IngressClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/IngressClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/IngressClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/IngressClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/IngressList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/IngressList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/NetworkPolicy.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/NetworkPolicy.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/NetworkPolicyList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/NetworkPolicyList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/Ingress.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/Ingress.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/IngressClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/IngressClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/IngressClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/IngressClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/IngressList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/IngressList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/networking/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/networking/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/RuntimeClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/RuntimeClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/RuntimeClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/RuntimeClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/RuntimeClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/RuntimeClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/RuntimeClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/RuntimeClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/RuntimeClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/RuntimeClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/RuntimeClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/RuntimeClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/node/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/node/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/PodDisruptionBudget.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/PodDisruptionBudget.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/PodDisruptionBudgetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/PodDisruptionBudgetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudget.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudget.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudgetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodDisruptionBudgetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicy.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicy.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicyList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/PodSecurityPolicyList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/policy/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/policy/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/provider.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRole.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRole.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRoleBinding.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRoleBinding.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRoleBindingList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRoleBindingList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/ClusterRoleList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/ClusterRoleList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/Role.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/Role.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/RoleBinding.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/RoleBinding.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/RoleBindingList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/RoleBindingList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/RoleList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/RoleList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRole.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRole.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBinding.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBinding.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBindingList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleBindingList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/ClusterRoleList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/Role.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/Role.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/RoleBinding.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/RoleBinding.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/RoleBindingList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/RoleBindingList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/RoleList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/RoleList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRole.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRole.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBinding.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBinding.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBindingList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRoleBindingList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/ClusterRoleList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/ClusterRoleList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/Role.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/Role.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/RoleBinding.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/RoleBinding.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/RoleBindingList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/RoleBindingList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/RoleList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/RoleList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/rbac/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/rbac/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/PriorityClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/PriorityClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/PriorityClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/PriorityClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/PriorityClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/PriorityClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/PriorityClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/PriorityClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/PriorityClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/PriorityClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/PriorityClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/PriorityClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/scheduling/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/scheduling/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/PodPreset.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/PodPreset.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/PodPresetList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/PodPresetList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/settings/v1alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/settings/v1alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSIDriver.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSIDriver.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSIDriverList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSIDriverList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSINode.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSINode.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/CSINodeList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/CSINodeList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/StorageClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/StorageClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/StorageClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/StorageClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/VolumeAttachment.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/VolumeAttachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/VolumeAttachmentList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/VolumeAttachmentList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacity.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacity.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacityList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/CSIStorageCapacityList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/VolumeAttachment.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/VolumeAttachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/VolumeAttachmentList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/VolumeAttachmentList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1alpha1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1alpha1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIDriver.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIDriver.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIDriverList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIDriverList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSINode.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSINode.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSINodeList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSINodeList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacity.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacity.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacityList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/CSIStorageCapacityList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/StorageClass.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/StorageClass.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/StorageClassList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/StorageClassList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/VolumeAttachment.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/VolumeAttachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/VolumeAttachmentList.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/VolumeAttachmentList.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/__init__.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/_inputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/storage/v1beta1/outputs.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/storage/v1beta1/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes/yaml.py` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes/yaml.py`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/PKG-INFO` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi-kubernetes
-Version: 3.8.3
+Version: 3.9.0
 Summary: A Pulumi package for creating and managing Kubernetes resources.
 Home-page: https://pulumi.com
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-kubernetes
 Description: [![Build Status](https://travis-ci.com/pulumi/pulumi-kubernetes.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/pulumi-kubernetes)
         [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
         [![NPM version](https://badge.fury.io/js/%40pulumi%2Fkubernetes.svg)](https://www.npmjs.com/package/@pulumi/kubernetes)
@@ -233,10 +233,10 @@
         
         [pulumi-kubernetes]: https://github.com/pulumi/pulumi-kubernetes
         [contributing]: CONTRIBUTING.md
         [code-of-conduct]: CODE-OF-CONDUCT.md
         [workload-example]: #deploying-a-workload-on-aws-eks
         [how-pulumi-works]: https://www.pulumi.com/docs/intro/concepts/how-pulumi-works
         
-Keywords: pulumi kubernetes
+Keywords: pulumi kubernetes category/cloud kind/native
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pulumi-kubernetes Version: 3.8.3 Summary: A Pulumi
+Metadata-Version: 2.1 Name: pulumi-kubernetes Version: 3.9.0 Summary: A Pulumi
 package for creating and managing Kubernetes resources. Home-page: https://
 pulumi.com License: Apache-2.0 Project-URL: Repository, https://github.com/
 pulumi/pulumi-kubernetes Description: [![Build Status](https://travis-ci.com/
 pulumi/pulumi-kubernetes.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https:/
 /travis-ci.com/pulumi/pulumi-kubernetes) [![Slack](http://www.pulumi.com/
 images/docs/badges/slack.svg)](https://slack.pulumi.com) [![NPM version](https:
 //badge.fury.io/js/%40pulumi%2Fkubernetes.svg)](https://www.npmjs.com/package/
@@ -107,9 +107,9 @@
 cluster's kubeconfig. export const kubeconfig = cluster.kubeconfig; ``` ##
 Contributing If you are interested in contributing, please see the
 [contributing docs][contributing]. ## Code of Conduct You can read the code of
 conduct [here][code-of-conduct]. [pulumi-kubernetes]: https://github.com/
 pulumi/pulumi-kubernetes [contributing]: CONTRIBUTING.md [code-of-conduct]:
 CODE-OF-CONDUCT.md [workload-example]: #deploying-a-workload-on-aws-eks [how-
 pulumi-works]: https://www.pulumi.com/docs/intro/concepts/how-pulumi-works
-Keywords: pulumi kubernetes Platform: UNKNOWN Description-Content-Type: text/
-markdown
+Keywords: pulumi kubernetes category/cloud kind/native Platform: UNKNOWN
+Description-Content-Type: text/markdown
```

### Comparing `pulumi_kubernetes-3.8.3/pulumi_kubernetes.egg-info/SOURCES.txt` & `pulumi_kubernetes-3.9.0/pulumi_kubernetes.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pulumi_kubernetes-3.8.3/setup.py` & `pulumi_kubernetes-3.9.0/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -4,16 +4,16 @@
 
 import errno
 from setuptools import setup, find_packages
 from setuptools.command.install import install
 from subprocess import check_call
 
 
-VERSION = "3.8.3"
-PLUGIN_VERSION = "3.8.3"
+VERSION = "3.9.0"
+PLUGIN_VERSION = "3.9.0"
 
 class InstallPluginCommand(install):
     def run(self):
         install.run(self)
         try:
             check_call(['pulumi', 'plugin', 'install', 'resource', 'kubernetes', PLUGIN_VERSION])
         except OSError as error:
@@ -41,27 +41,27 @@
       version=VERSION,
       description="A Pulumi package for creating and managing Kubernetes resources.",
       long_description=readme(),
       long_description_content_type='text/markdown',
       cmdclass={
           'install': InstallPluginCommand,
       },
-      keywords='pulumi kubernetes',
+      keywords='pulumi kubernetes category/cloud kind/native',
       url='https://pulumi.com',
       project_urls={
           'Repository': 'https://github.com/pulumi/pulumi-kubernetes'
       },
       license='Apache-2.0',
       packages=find_packages(),
       package_data={
           'pulumi_kubernetes': [
               'py.typed',
           ]
       },
       install_requires=[
           'parver>=0.2.1',
-          'pulumi>=3.0.0,<4.0.0',
+          'pulumi>=3.9.0,<4.0.0',
           'pyyaml>=5.3.1',
           'requests>=2.21,<3.0',
           'semver>=2.8.1'
       ],
       zip_safe=False)
```

