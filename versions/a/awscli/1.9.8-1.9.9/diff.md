# Comparing `tmp/awscli-1.9.8.tar.gz` & `tmp/awscli-1.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/awscli-1.9.8.tar", last modified: Thu Nov 19 21:34:11 2015, max compression
+gzip compressed data, was "dist/awscli-1.9.9.tar", last modified: Tue Nov 24 01:59:34 2015, max compression
```

## Comparing `awscli-1.9.8.tar` & `awscli-1.9.9.tar`

### file list

```diff
@@ -1,1028 +1,1028 @@
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli.egg-info/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        1 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli.egg-info/dependency_links.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    17249 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli.egg-info/PKG-INFO
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    44946 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli.egg-info/SOURCES.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      113 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli.egg-info/requires.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        7 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli.egg-info/top_level.txt
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/bin/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1411 2015-11-19 21:34:09.000000 awscli-1.9.8/bin/aws.cmd
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      818 2015-11-19 21:34:09.000000 awscli-1.9.8/bin/aws
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1139 2015-11-19 21:34:09.000000 awscli-1.9.8/bin/aws_completer
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1915 2015-11-19 21:34:09.000000 awscli-1.9.8/bin/aws_zsh_completer.sh
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    26286 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/clidriver.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/data/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2637 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/data/cli.json
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4284 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/text.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    26233 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/clidocs.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4339 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/utils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2265 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/plugin.py
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     6948 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/completer.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3027 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/errorhandler.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13200 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/help.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12651 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/topictags.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    14729 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/table.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3731 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/compat.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    27221 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/testutils.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/elb/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      611 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/describe-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      231 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/add-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      349 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/create-app-cookie-stickiness-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      390 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/enable-availability-zones-for-load-balancer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      166 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/delete-load-balancer.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      405 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/disable-availability-zones-for-load-balancer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      729 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/set-load-balancer-policies-of-listener.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      370 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/create-lb-cookie-stickiness-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      581 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/describe-load-balancer-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      305 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/delete-load-balancer-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      497 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/register-instances-with-load-balancer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      737 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/set-load-balancer-policies-for-backend-server.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      320 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/detach-load-balancer-from-subnets.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      990 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/modify-load-balancer-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      317 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/create-load-balancer-listeners.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      371 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/attach-load-balancer-to-subnets.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      460 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/deregister-instances-from-load-balancer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3090 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/describe-load-balancers.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1902 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/describe-load-balancer-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1561 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/describe-instance-health.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2303 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/create-load-balancer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      261 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/delete-load-balancer-listeners.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3454 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/describe-load-balancer-policy-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      365 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/set-load-balancer-listener-ssl-certificate.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/configure-health-check.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      189 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/remove-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2670 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/create-load-balancer-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      356 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elb/apply-security-groups-to-load-balancer.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/dynamodb/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1470 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/batch-get-item.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1373 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/create-table.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      593 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/put-item.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      288 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/list-tables.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1047 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/query.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/get-item.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      512 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/delete-item.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1310 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/update-table.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1109 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/describe-table.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      507 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/delete-table.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1423 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/scan.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1443 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/update-item.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1337 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/dynamodb/batch-write-item.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/codepipeline/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      609 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/delete-custom-action-type.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2415 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/get-pipeline.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      423 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/acknowledge-job.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3584 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/update-pipeline.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3246 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/poll-for-jobs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      314 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/disable-stage-transition.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2122 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/create-pipeline.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1472 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/create-custom-action-type.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2364 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/list-action-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      326 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/start-pipeline-execution.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1391 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/get-pipeline-state.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      311 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/enable-stage-transition.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      536 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/list-pipelines.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2730 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/get-job-details.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      287 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codepipeline/delete-pipeline.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/kms/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      777 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/kms/decrypt.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/kms/create-alias.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      690 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/kms/encrypt.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/autoscaling/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1780 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-tags.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      846 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/exit-standby.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      464 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/execute-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      249 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/attach-load-balancers.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2053 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-notification-configurations.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      417 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/delete-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      504 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/suspend-processes.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      358 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-lifecycle-hook-types.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      893 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/detach-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1031 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/put-scheduled-update-group-action.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2025 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-auto-scaling-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      674 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/delete-notification-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1306 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-auto-scaling-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      579 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/disable-metrics-collection.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1772 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-scaling-activities.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      250 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/attach-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1323 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/put-scaling-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      822 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-termination-policy-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/enable-metrics-collection.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      410 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/complete-lifecycle-action.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      642 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-adjustment-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      722 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/delete-auto-scaling-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      491 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/set-desired-capacity.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      595 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-account-limits.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      720 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/terminate-instance-in-auto-scaling-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2149 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-launch-configurations.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1625 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/create-auto-scaling-group.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      204 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/delete-lifecycle-hook.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      412 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/delete-launch-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      695 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/put-notification-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      412 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-load-balancers.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      770 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-lifecycle-hooks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      481 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/delete-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1078 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-metric-collection-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      973 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/update-auto-scaling-group.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      600 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/put-lifecycle-hook.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      510 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/resume-processes.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      330 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/record-lifecycle-action-heartbeat.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      502 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/delete-scheduled-action.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      401 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/create-or-update-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2164 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/create-launch-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2668 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-scheduled-actions.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      218 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/set-instance-health.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      257 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/detach-load-balancers.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      919 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-scaling-process-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      999 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-auto-scaling-notification-types.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      867 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/enter-standby.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2562 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/autoscaling/describe-policies.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2712 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/validate-configuration-settings.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2095 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-configuration-settings.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      210 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/abort-environment-update.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      163 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/delete-application.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1106 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-environments.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1586 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-events.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      408 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/request-environment-info.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1916 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-configuration-options.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      199 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/rebuild-environment.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      236 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/delete-environment-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      210 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/restart-app-server.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      226 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/create-storage-location.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      592 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/create-configuration-template.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1499 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-environment-health.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      938 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/retrieve-environment-info.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      855 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/terminate-environment.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      263 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/delete-configuration-template.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1276 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-applications.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      282 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/delete-application-version.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      915 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/update-configuration-template.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1186 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-application-versions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      781 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/update-application-version.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1737 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/create-environment.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      932 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/create-application-version.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3234 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/update-environment.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      236 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/swap-environment-cnames.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2560 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/list-available-solution-stacks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      317 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/check-dns-availability.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      986 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-environment-resources.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2052 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-instances-health.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      766 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/update-application.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      832 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/elasticbeanstalk/create-application.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/redshift/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      488 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-resize.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      945 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/modify-cluster.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      603 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/revoke-cluster-security-group-ingress.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      994 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-reserved-nodes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      937 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-events.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1446 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/create-cluster.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      865 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/create-cluster-subnet-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      184 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/delete-cluster-snapshot.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1268 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/create-cluster-security-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/create-cluster-parameter-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      329 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/delete-cluster-subnet-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2217 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-cluster-parameters.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      603 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/delete-cluster.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1459 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/reboot-cluster.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1499 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-reserved-node-offerings.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1310 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-default-cluster-parameters.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      930 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-cluster-subnet-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1351 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/revoke-snapshot-access.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1096 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/purchase-reserved-node-offering.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      556 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-cluster-versions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1806 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-orderable-cluster-options.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      222 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/delete-cluster-parameter-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      282 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/reset-cluster-parameter-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      939 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/create-cluster-snapshot.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1049 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/copy-cluster-snapshot.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1301 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/authorize-snapshot-access.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      626 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/authorize-cluster-security-group-ingress.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1152 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/modify-cluster-subnet-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      981 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-cluster-parameter-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1010 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-cluster-security-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      840 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/modify-cluster-parameter-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2445 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-cluster-snapshots.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/delete-cluster-security-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2005 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/describe-clusters.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1281 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/redshift/restore-from-cluster-snapshot.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/deploy/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      651 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/get-on-premises-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      904 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/deregister.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      292 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/delete-deployment-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      511 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/list-on-premises-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      389 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/list-deployment-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      209 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/delete-application.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      605 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/get-deployment-config.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1175 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/get-deployment.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      372 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/list-deployment-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      928 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/push.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      384 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/create-deployment-config.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      452 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/get-application.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1133 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/batch-get-on-premises-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      460 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/register-on-premises-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      442 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/list-deployment-configs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      473 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/uninstall.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      507 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/list-deployments.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      983 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/list-application-revisions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      964 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/register.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      641 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/remove-tags-from-on-premises-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      293 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/list-applications.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      259 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/delete-deployment-config.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      360 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/stop-deployment.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      588 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/update-deployment-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2009 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/get-deployment-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      543 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/deregister-on-premises-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      766 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/install.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      911 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/get-deployment-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      468 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/register-application-revision.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      745 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/batch-get-applications.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      585 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/create-deployment-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      279 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/update-application.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      419 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/add-tags-to-on-premises-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2361 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/batch-get-deployments.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      975 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/get-application-revision.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/create-application.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      481 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/deploy/create-deployment.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/ssm/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      709 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/create-document.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      862 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/list-associations.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      698 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/get-document.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      569 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/create-association.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      747 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/update-association-status.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      392 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/describe-document.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      332 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/list-documents.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      213 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/delete-document.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      842 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/describe-association.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      281 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/delete-association.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1042 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ssm/create-association-batch.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/ecs/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3569 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/create-service.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1550 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/describe-task-definition.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      484 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/update-service.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      498 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/create-cluster.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      636 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/update-container-agent.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      513 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/list-container-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      613 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/list-task-definition-families.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1732 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/describe-tasks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      497 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/delete-cluster.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1621 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/describe-services.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      238 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/delete-service.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1287 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/run-task.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2838 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/describe-container-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      263 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/list-services.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1107 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/deregister-task-definition.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      416 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/deregister-container-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2849 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/register-task-definition.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      331 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/list-clusters.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      586 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/describe-clusters.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      794 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/list-tasks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1257 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ecs/list-task-definitions.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/rds/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      778 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/rds/create-option-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      696 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/rds/download-db-log-file-portion.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      780 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/rds/add-tag-to-resource.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      546 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/rds/describe-db-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2028 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/rds/create-db-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      695 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/rds/create-db-security-group.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/cloudwatch/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1898 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/describe-alarm-history.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4200 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/get-metric-statistics.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1751 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/describe-alarms.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/disable-alarm-actions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      401 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/set-alarm-state.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3562 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/describe-alarms-for-metric.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      253 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/delete-alarms.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      803 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/put-metric-alarm.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/enable-alarm-actions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      755 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/put-metric-data.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2527 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudwatch/list-metrics.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/cloudformation/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      843 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudformation/list-stacks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1432 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudformation/create-stack.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1435 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudformation/describe-stacks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1266 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudformation/update-stack.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1077 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudformation/get-template.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudformation/cancel-update-stack.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      834 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudformation/validate-template.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/iam/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      492 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-user-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      369 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-login-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      852 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      789 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-role.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      733 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-policy-version.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      513 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/generate-credential-report.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      628 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-virtual-mfa-devices.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      446 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-saml-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1166 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/upload-server-certificate.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      525 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-user-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      506 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-group-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      399 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      784 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-virtual-mfa-device.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      586 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-signing-certificate.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      471 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-policy-version.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      824 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/put-role-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      340 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      705 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/resync-mfa-device.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      403 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-account-alias.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      715 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-access-key.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      846 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-policy-version.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      709 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/add-client-id-to-open-id-connect-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-saml-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      579 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-saml-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      659 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-attached-role-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      484 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/detach-group-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2139 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-login-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      393 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-user.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      896 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-groups-for-user.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      698 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-open-id-connect-provider-thumbprint.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1135 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-instance-profiles-for-role.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      820 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-account-password-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      592 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/put-user-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1003 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-access-keys.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      618 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-open-id-connect-providers.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1641 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/change-password.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      409 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-role-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      394 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-account-alias.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      877 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-group-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      842 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-access-key.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      873 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-user-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      510 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/attach-user-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      727 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/remove-client-id-from-open-id-connect-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      527 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/set-default-policy-version.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      403 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-instance-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      519 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-group-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      526 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-open-id-connect-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      710 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-assume-role-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      548 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/put-group-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      509 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/attach-group-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/add-role-to-instance-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      788 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-signing-certificates.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      634 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-role.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      981 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-role.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      895 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-login-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      454 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/detach-user-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      514 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/attach-role-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-mfa-devices.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      891 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-login-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2338 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-instance-profiles.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      491 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-credential-report.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      414 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-account-aliases.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      594 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      928 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-role-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      751 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-attached-user-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      802 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-policy-versions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      622 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-user.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      755 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-users.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1285 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-account-summary.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      394 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      619 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-access-key-last-used.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      580 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-saml-providers.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      772 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-entities-for-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      898 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/upload-signing-certificate.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      574 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-user.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      808 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-open-id-connect-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1283 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1336 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      597 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-role-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2405 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-open-id-connect-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      446 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-virtual-mfa-device.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      419 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-account-password-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      543 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/deactivate-mfa-device.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      803 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/enable-mfa-device.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-account-password-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      921 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/create-instance-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      445 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/add-user-to-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1491 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-roles.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1136 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-instance-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      620 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-access-key.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      612 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-signing-certificate.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      390 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/delete-user.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      778 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/list-attached-group-policies.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      676 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/update-saml-provider.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      474 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/remove-user-from-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9183 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/get-account-authorization-details.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      491 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/remove-role-from-instance-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      511 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iam/detach-role-policy.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/iot/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1532 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/iot/create-certificate-from-csr.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/s3/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4763 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3/sync.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      525 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3/mb.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      641 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3/rb.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1414 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3/rm.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7036 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/examples/s3/_concepts.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4809 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3/cp.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2832 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3/mv.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      883 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3/website.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2846 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/examples/s3/ls.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/workspaces/
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      735 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/workspaces/create-workspaces.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      920 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/workspaces/describe-workspaces.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/workspaces/terminate-workspaces.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1755 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/workspaces/describe-workspace-directories.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     3556 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/workspaces/describe-workspace-bundles.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/route53/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7633 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/change-resource-record-sets.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      193 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/delete-hosted-zone.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      293 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/get-health-check.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1434 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/list-hosted-zones-by-name.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      602 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/create-hosted-zone.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      804 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/list-health-checks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1390 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/create-health-check.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      264 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/delete-health-check.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      288 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/get-change.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      789 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/list-hosted-zones.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      215 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/get-hosted-zone.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      955 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/route53/list-resource-record-sets.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/emr/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      648 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/add-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      151 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/list-steps.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      196 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/modify-cluster-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1146 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/describe-step.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1462 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/ssh.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6239 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/describe-cluster.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19103 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/create-cluster-examples.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      287 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/put.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      258 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/get.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4477 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/add-steps.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/create-cluster-synopsis.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      526 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/schedule-hbase-backup.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      165 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/wait.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      670 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/list-clusters.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      184 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/remove-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5688 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/create-default-roles.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      273 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/socks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2182 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/emr/list-instances.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/storagegateway/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/storagegateway/describe-gateway-information.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      260 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/storagegateway/list-gateways.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      547 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/storagegateway/list-volumes.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/sns/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      587 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/create-topic.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      552 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/list-subscriptions-by-topic.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1304 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/get-topic-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      758 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/get-subscription-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      353 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/publish.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      173 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/unsubscribe.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      484 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/list-subscriptions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      220 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/list-topics.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      146 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/delete-topic.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/subscribe.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      651 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sns/confirm-subscription.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/opsworks/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2117 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/create-app.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      903 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/deregister-rds-db-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      637 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/delete-app.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      870 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/update-rds-db-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1030 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/register-rds-db-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1017 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/assign-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/update-layer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      608 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/associate-elastic-ip.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      720 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-elastic-ips.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1194 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/set-time-based-auto-scaling.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      877 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/delete-user-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1825 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-deployments.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      529 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/update-app.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      635 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/attach-elastic-load-balancer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      566 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/disassociate-elastic-ip.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1193 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/create-stack.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2379 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-stacks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/deregister-elastic-ip.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      845 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/delete-stack.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      809 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/register-elastic-ip.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      870 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/update-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1379 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/set-permission.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1462 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/set-load-based-auto-scaling.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1178 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-apps.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      882 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-stack-summary.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      874 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/stop-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      643 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/deregister-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1204 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/delete-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      947 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-volumes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1340 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-timebased-auto-scaling.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2100 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-commands.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/stop-stack.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      824 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/delete-layer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1365 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-load-based-auto-scaling.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1285 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/create-user-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      959 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/start-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/start-stack.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      835 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/update-my-user-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1015 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-permissions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7115 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/register.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/unassign-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      548 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/update-elastic-ip.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      831 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/unassign-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      698 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/create-layer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      950 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-my-user-profile.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      807 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/get-hostname-suggestion.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      597 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/update-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      560 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/reboot-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1154 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/create-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1247 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-elastic-load-balancers.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      750 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/deregister-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5885 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-layers.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      751 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/register-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      633 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/detach-elastic-load-balancer.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      665 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/assign-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1125 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-rds-db-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3512 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1034 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-user-profiles.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1185 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/describe-raid-arrays.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2623 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/opsworks/create-deployment.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/s3api/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      701 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-cors.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      144 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-bucket-tagging.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      531 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-acl.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      845 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/upload-part.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      489 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-notification-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1327 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/list-parts.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      596 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/create-multipart-upload.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1109 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-notification-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-lifecycle.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      417 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/head-object.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      790 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-object-acl.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      171 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-versioning.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      148 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-bucket-lifecycle.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1405 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-lifecycle-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      386 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/copy-object.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      880 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-lifecycle-configuration.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      434 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-website.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1035 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/list-multipart-uploads.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      391 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-object-torrent.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      483 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/list-buckets.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      285 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-tagging.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      553 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-object.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      558 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-objects.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      582 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-acl.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      300 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-website.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      960 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-cors.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1318 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-logging.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      152 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-bucket-replication.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      647 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-object.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1075 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      468 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-notification.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      195 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-versioning.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      372 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-tagging.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      554 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-object-acl.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      463 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/abort-multipart-upload.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1247 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-replication.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      538 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-object.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      560 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/list-objects.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      176 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/create-bucket.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1007 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1019 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-notification.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      135 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-bucket-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1598 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/put-bucket-lifecycle.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      225 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-location.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      667 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/get-bucket-replication.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2584 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/list-object-versions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      163 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-bucket-cors.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      126 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-bucket.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      144 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/delete-bucket-website.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      326 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/head-bucket.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1550 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/s3api/complete-multipart-upload.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/ses/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      820 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/verify-domain-dkim.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      498 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/set-identity-dkim-enabled.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1188 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/get-send-statistics.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1369 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/get-identity-notification-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1260 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/get-send-quota.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      630 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/verify-domain-identity.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      970 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/verify-email-identity.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2308 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/send-email.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      529 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/delete-identity.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1152 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/get-identity-dkim-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      890 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/set-identity-feedback-forwarding-enabled.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      997 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/get-identity-verification-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      728 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/set-identity-notification-topic.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      906 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/list-identities.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2043 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ses/send-raw-email.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/importexport/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      237 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/importexport/cancel-job.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      408 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/importexport/list-jobs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1539 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/importexport/create-job.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      936 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/importexport/get-shipping-label.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1210 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/importexport/get-status.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      482 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/importexport/update-job.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/glacier/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      799 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/upload-archive.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1307 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/list-parts.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      939 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/describe-job.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      647 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/get-vault-notifications.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      851 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/initiate-multipart-upload.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      259 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/create-vault.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1869 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/initiate-job.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      620 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/set-vault-notifications.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1866 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/list-jobs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      377 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/list-tags-for-vault.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      546 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/list-multipart-uploads.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      837 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/abort-multipart-upload.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      639 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/list-vaults.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      315 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/remove-tags-from-vault.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      965 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/set-data-retrieval-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      468 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/get-data-retrieval-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      297 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/delete-vault.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/describe-vault.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1020 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/upload-multipart-part.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1007 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/complete-multipart-upload.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1201 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/get-job-output.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      299 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/glacier/add-tags-to-vault.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/sqs/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      679 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/create-queue.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2011 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/receive-message.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2185 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/send-message-batch.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      789 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/list-queues.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      989 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/set-queue-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      859 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/send-message.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      192 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/delete-queue.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      594 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/delete-message-batch.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      274 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/remove-permission.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1270 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/get-queue-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      359 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/change-message-visibility.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      793 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/change-message-visibility-batch.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      429 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/list-dead-letter-source-queues.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      211 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/get-queue-url.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      204 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/purge-queue.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      230 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/delete-message.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      333 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/sqs/add-permission.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/configure/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/configure/get/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      807 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/configure/get/_examples.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1936 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/configure/get/_description.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/configure/set/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      864 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/configure/set/_examples.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      896 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/configure/set/_description.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2027 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/configure/_description.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/ec2/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3645 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4931 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-spot-fleet-requests.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      802 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-availability-zones.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      275 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-volume-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      349 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/replace-network-acl-association.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      239 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/reject-vpc-peering-connection.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      277 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/detach-internet-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      377 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/replace-route.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      318 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/attach-network-interface.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      244 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-route.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      290 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-vpn-connection-route.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1729 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-spot-fleet-request-history.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      311 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/disable-vgw-route-propagation.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      283 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/confirm-product-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      200 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-placement-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6201 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/request-spot-fleet.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3560 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-reserved-instances-offerings.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      274 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/cancel-conversion-task.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      662 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-flow-logs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      286 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/associate-route-table.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-internet-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      619 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-snapshot-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      245 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/disassociate-route-table.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1144 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/import-key-pair.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      350 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-prefix-lists.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      195 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/disable-vpc-classic-link.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      811 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-route.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      627 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-subnet.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1438 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpcs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      930 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-vpc-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      244 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpc-endpoint-services.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      757 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/stop-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      999 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/register-image.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      846 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpn-gateways.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      241 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/report-instance-status.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      411 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/unmonitor-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      426 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/purchase-reserved-instances-offering.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      265 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-network-acl-entry.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      622 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/authorize-security-group-egress.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1229 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      346 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/attach-vpn-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      626 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpc-endpoints.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      373 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-vpc-endpoints.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      723 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-security-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      545 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-subnet-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      272 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/attach-internet-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      164 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-vpc.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      285 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/detach-vpn-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      577 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-spot-fleet-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9440 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/examples/ec2/run-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1252 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-vpc-peering-connection.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      304 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-vpn-connection-route.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2187 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-account-attributes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      691 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/accept-vpc-peering-connection.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      636 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/revoke-security-group-egress.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1161 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-internet-gateways.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      527 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-dhcp-options.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      220 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-network-interface.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      844 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-network-acl.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      268 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/detach-network-interface.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      336 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/unassign-private-ip-addresses.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      377 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-key-pair.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1376 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-conversion-tasks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      557 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-key-pairs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1273 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpn-connections.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4107 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-security-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      758 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/start-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      169 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-placement-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1440 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-instance-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      435 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-key-pair.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      220 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-vpn-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      179 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-flow-logs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      276 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/reset-snapshot-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1672 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3186 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-volumes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      413 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-spot-datafeed-subscription.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      505 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/cancel-bundle-task.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      368 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/cancel-spot-instance-requests.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      699 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-image-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      196 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-route-table.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1024 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-instance-status.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1981 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-regions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1476 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-subnets.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      323 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/copy-image.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      447 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/attach-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      581 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-snapshot.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1029 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-image.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      557 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/associate-dhcp-options.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      290 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/get-console-output.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1108 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-image-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      393 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-spot-datafeed-subscription.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      253 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/detach-classic-link-vpc.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      209 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-dhcp-options.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      403 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/reboot-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3624 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-network-interfaces.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2121 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-spot-price-history.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      856 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-dhcp-options.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1658 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-reserved-instances-modifications.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      354 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-placement-groups.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      866 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/assign-private-ip-addresses.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-route-table.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2029 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-network-interface-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      814 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-vpc.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      659 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpc-classic-link.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1199 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-tags.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      282 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/restore-address-to-classic.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      798 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-export-tasks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      777 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-vpc-endpoint.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1911 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-images.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      455 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-customer-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1787 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-snapshots.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      232 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-vpc-peering-connection.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      304 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/enable-vgw-route-propagation.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      216 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-customer-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      448 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-snapshot-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1090 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-customer-gateways.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      555 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-bundle-tasks.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      704 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-flow-logs.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      895 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/reset-instance-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      196 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-network-acl.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2801 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/authorize-security-group-ingress.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      887 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/bundle-instance.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      319 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/reset-image-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      225 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/move-address-to-vpc.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      179 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-subnet.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      382 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-volume-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      349 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/replace-route-table-association.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2553 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpc-peering-connections.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      395 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/detach-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1788 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-route-tables.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      405 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/replace-network-acl-entry.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1221 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-classic-link-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      515 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/disassociate-address.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      222 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-volume.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2320 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-reserved-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2442 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-spot-instance-requests.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      234 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-spot-datafeed-subscription.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      560 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/allocate-address.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1480 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-volume-status.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      274 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-internet-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2045 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-reserved-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      309 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/attach-classic-link-vpc.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1044 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/revoke-security-group-ingress.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      192 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/enable-vpc-classic-link.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1106 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-network-interface.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      405 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/monitor-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      894 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-instance-export-task.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      943 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/get-password-data.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1251 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-network-interface-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      498 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/release-address.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1627 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-instance-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4991 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/request-spot-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      727 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/terminate-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      775 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-security-group.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      688 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-spot-fleet-request.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3896 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-network-acls.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      441 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-network-acl-entry.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1548 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-vpn-connection.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1325 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-instances.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      181 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/deregister-image.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      223 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-snapshot.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2611 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-addresses.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      996 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/associate-address.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      469 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-moving-addresses.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1140 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/cancel-spot-fleet-requests.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1045 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/describe-vpc-attribute.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      327 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/modify-vpc-endpoint.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      435 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/copy-snapshot.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      208 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/delete-vpn-connection.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      327 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/create-vpn-gateway.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      240 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/ec2/cancel-export-task.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/logs/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1095 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/put-log-events.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      731 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/describe-log-streams.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      180 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/delete-retention-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      175 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/create-log-stream.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      116 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/create-log-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      167 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/put-retention-policy.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      181 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/delete-log-stream.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      879 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/get-log-events.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      116 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/delete-log-group.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      472 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/logs/describe-log-groups.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/codecommit/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      660 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/update-repository-name.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      336 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/update-repository-description.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      259 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/list-branches.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      329 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/get-branch.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      799 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/create-repository.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1756 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/batch-get-repositories.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      868 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/get-repository.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      286 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/create-branch.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      483 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/list-repositories.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      312 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/update-default-branch.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      244 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/delete-repository.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      312 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/codecommit/delete-branch.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/swf/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2720 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/list-domains.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1938 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/register-domain.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1759 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/deprecate-domain.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1321 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/count-open-workflow-executions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      948 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/register-workflow-type.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1462 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/count-closed-workflow-executions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1175 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/list-workflow-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7143 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/list-activity-types.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1094 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/swf/describe-domain.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/cloudfront/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3207 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/list-distributions.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2733 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/get-distribution-config.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      666 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/list-invalidations.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      528 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/delete-distribution.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3379 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/get-distribution.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1180 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/create-invalidation.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      913 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/get-invalidation.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6076 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/update-distribution.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4475 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/cloudfront/create-distribution.rst
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/examples/datapipeline/
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      689 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/add-tags.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      361 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/activate-pipeline.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      367 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/deactivate-pipeline.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1186 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/list-runs.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      399 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/put-pipeline-definition.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      250 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/create-pipeline.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     2935 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/get-pipeline-definition.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      606 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/list-pipelines.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      205 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/remove-tags.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      152 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/delete-pipeline.rst
--rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1625 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/examples/datapipeline/describe-pipelines.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4888 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/paramfile.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    14650 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/shorthand.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/topics/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5817 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/topics/s3-config.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9617 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/topics/config-vars.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1966 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/topics/return-codes.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1208 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/topics/topic-tags.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3135 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/globalargs.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2626 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/removals.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4291 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/cloudsearch.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3278 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/iamvirtmfa.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3897 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/streamingoutputarg.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9721 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/waiters.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5906 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/toplevelbool.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10359 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/paginate.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4459 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/sessendemail.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3582 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/utils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      909 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/kms.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1805 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3endpoint.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1187 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/route53.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6746 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/ec2bundleinstance.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2778 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/rds.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12935 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/assumerole.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9505 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/flatten.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3518 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/awslambda.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5218 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/preview.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19648 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/opsworks.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3643 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/generatecliskeleton.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/s3/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13707 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/executor.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6204 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/comparator.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    15076 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/s3/filegenerator.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    24569 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/s3/utils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2845 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/transferconfig.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2656 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/s3.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3195 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/fileinfobuilder.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6492 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/filters.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13252 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/s3/fileinfo.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    25094 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/s3/s3handler.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    50238 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/s3/subcommands.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6029 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/fileformat.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/s3/syncstrategy/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2001 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/syncstrategy/register.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1232 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/syncstrategy/delete.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1300 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/syncstrategy/sizeonly.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/syncstrategy/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1686 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/syncstrategy/exacttimestamps.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10112 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/s3/syncstrategy/base.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    31170 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/s3/tasks.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1231 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/iot_data.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/emr/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    20172 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/createcluster.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     8482 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/steputils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9406 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/hbase.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3361 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/sshutils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5442 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/command.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9368 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/emrutils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7699 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/ssh.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12599 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/createdefaultroles.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2505 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/addinstancegroups.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2879 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/installapplications.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4001 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/describecluster.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2547 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/configutils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    16214 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/helptext.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1947 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/addsteps.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9813 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/argumentschema.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6535 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/applicationutils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1382 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/terminateclusters.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      952 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/hbaseutils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9106 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/emrfsutils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4761 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/config.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3135 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/instancegroupsutils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3639 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/modifyclusterattributes.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9917 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/exceptions.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3775 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/listclusters.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6458 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/constants.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1088 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/addtags.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3257 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/emr/emr.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3837 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/argrename.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6072 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/putmetricdata.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2351 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/iot.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    25967 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/configure.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/codedeploy/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5910 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/locationargs.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7196 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/register.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4595 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/utils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4205 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/install.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2202 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/uninstall.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6181 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/deregister.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10644 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/push.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2212 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/codedeploy.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7661 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codedeploy/systems.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1904 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/scalarparse.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1399 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/ec2protocolarg.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     8298 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/ec2secgroupsimplify.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/cloudtrail/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1641 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/cloudtrail/utils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    37906 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/cloudtrail/validation.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13705 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/cloudtrail/subscribe.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1337 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/cloudtrail/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1484 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4986 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/arguments.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7391 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/codecommit.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7503 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/ec2runinstances.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/configservice/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7116 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/configservice/subscribe.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      924 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/configservice/rename_cmd.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/configservice/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4258 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/configservice/getstatus.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3154 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/configservice/putconfigurationrecorder.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4703 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/ec2decryptpassword.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2480 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/customizations/s3errormsg.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1813 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/addexamples.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    16989 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/commands.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3679 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/cliinputjson.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2992 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/ec2addcount.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-19 21:34:11.000000 awscli-1.9.8/awscli/customizations/datapipeline/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9550 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/datapipeline/createdefaultroles.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7619 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/datapipeline/translator.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    17291 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/datapipeline/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1895 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/datapipeline/constants.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1074 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/customizations/cloudsearchdomain.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1464 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    18677 2015-11-19 21:34:10.000000 awscli-1.9.8/awscli/arguments.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    18849 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/argprocess.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7462 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/handlers.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5833 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/schema.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6176 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/argparser.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    11121 2015-11-19 21:34:09.000000 awscli-1.9.8/awscli/formatter.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    17249 2015-11-19 21:34:11.000000 awscli-1.9.8/PKG-INFO
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      549 2015-11-19 21:34:09.000000 awscli-1.9.8/LICENSE.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13505 2015-11-19 21:34:09.000000 awscli-1.9.8/README.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2247 2015-11-19 21:34:10.000000 awscli-1.9.8/setup.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      396 2015-11-19 21:34:09.000000 awscli-1.9.8/requirements.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      227 2015-11-19 21:34:11.000000 awscli-1.9.8/setup.cfg
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      141 2015-11-19 21:34:09.000000 awscli-1.9.8/MANIFEST.in
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli.egg-info/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        1 2015-11-24 01:59:33.000000 awscli-1.9.9/awscli.egg-info/dependency_links.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    17249 2015-11-24 01:59:33.000000 awscli-1.9.9/awscli.egg-info/PKG-INFO
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    44946 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli.egg-info/SOURCES.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      113 2015-11-24 01:59:33.000000 awscli-1.9.9/awscli.egg-info/requires.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        7 2015-11-24 01:59:33.000000 awscli-1.9.9/awscli.egg-info/top_level.txt
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/bin/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1411 2015-11-24 01:59:32.000000 awscli-1.9.9/bin/aws.cmd
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      818 2015-11-24 01:59:32.000000 awscli-1.9.9/bin/aws
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1139 2015-11-24 01:59:32.000000 awscli-1.9.9/bin/aws_completer
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1915 2015-11-24 01:59:32.000000 awscli-1.9.9/bin/aws_zsh_completer.sh
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    26286 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/clidriver.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/data/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2637 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/data/cli.json
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4284 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/text.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    26233 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/clidocs.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4339 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/utils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2265 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/plugin.py
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     6948 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/completer.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3027 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/errorhandler.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13200 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/help.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12651 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/topictags.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    14729 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/table.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3731 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/compat.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    27221 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/testutils.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/elb/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      611 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/describe-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      231 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/add-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      349 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/create-app-cookie-stickiness-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      390 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/enable-availability-zones-for-load-balancer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      166 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/delete-load-balancer.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      405 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/disable-availability-zones-for-load-balancer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      729 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/set-load-balancer-policies-of-listener.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      370 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/create-lb-cookie-stickiness-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      581 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/describe-load-balancer-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      305 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/delete-load-balancer-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      497 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/register-instances-with-load-balancer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      737 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/set-load-balancer-policies-for-backend-server.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      320 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/detach-load-balancer-from-subnets.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      990 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/modify-load-balancer-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      317 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/create-load-balancer-listeners.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      371 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/attach-load-balancer-to-subnets.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      460 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/deregister-instances-from-load-balancer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3090 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/describe-load-balancers.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1902 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/describe-load-balancer-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1561 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/describe-instance-health.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2303 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/create-load-balancer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      261 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/delete-load-balancer-listeners.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3454 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/describe-load-balancer-policy-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      365 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/set-load-balancer-listener-ssl-certificate.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/configure-health-check.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      189 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/remove-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2670 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/create-load-balancer-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      356 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elb/apply-security-groups-to-load-balancer.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/dynamodb/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1470 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/batch-get-item.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1373 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/create-table.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      593 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/put-item.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      288 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/list-tables.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1047 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/query.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/get-item.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      512 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/delete-item.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1310 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/update-table.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1109 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/describe-table.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      507 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/delete-table.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1423 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/scan.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1443 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/update-item.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1337 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/dynamodb/batch-write-item.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/codepipeline/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      609 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/delete-custom-action-type.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2415 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/get-pipeline.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      423 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/acknowledge-job.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3584 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/update-pipeline.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3246 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/poll-for-jobs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      314 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/disable-stage-transition.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2122 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/create-pipeline.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1472 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/create-custom-action-type.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2364 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/list-action-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      326 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/start-pipeline-execution.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1391 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/get-pipeline-state.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      311 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/enable-stage-transition.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      536 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/list-pipelines.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2730 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/get-job-details.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      287 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codepipeline/delete-pipeline.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/kms/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      777 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/kms/decrypt.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/kms/create-alias.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      690 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/kms/encrypt.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/autoscaling/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1780 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-tags.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      846 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/exit-standby.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      464 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/execute-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      249 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/attach-load-balancers.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2053 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-notification-configurations.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      417 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/delete-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      504 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/suspend-processes.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      358 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-lifecycle-hook-types.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      893 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/detach-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1031 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/put-scheduled-update-group-action.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2025 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-auto-scaling-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      674 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/delete-notification-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1306 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-auto-scaling-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      579 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/disable-metrics-collection.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1772 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-scaling-activities.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      250 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/attach-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1323 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/put-scaling-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      822 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-termination-policy-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/enable-metrics-collection.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      410 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/complete-lifecycle-action.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      642 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-adjustment-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      722 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/delete-auto-scaling-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      491 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/set-desired-capacity.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      595 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-account-limits.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      720 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/terminate-instance-in-auto-scaling-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2149 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-launch-configurations.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1625 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/create-auto-scaling-group.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      204 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/delete-lifecycle-hook.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      412 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/delete-launch-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      695 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/put-notification-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      412 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-load-balancers.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      770 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-lifecycle-hooks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      481 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/delete-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1078 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-metric-collection-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      973 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/update-auto-scaling-group.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      600 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/put-lifecycle-hook.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      510 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/resume-processes.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      330 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/record-lifecycle-action-heartbeat.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      502 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/delete-scheduled-action.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      401 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/create-or-update-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2164 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/create-launch-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2668 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-scheduled-actions.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      218 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/set-instance-health.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      257 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/detach-load-balancers.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      919 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-scaling-process-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      999 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-auto-scaling-notification-types.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      867 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/enter-standby.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2562 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/autoscaling/describe-policies.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2712 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/validate-configuration-settings.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2095 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-configuration-settings.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      210 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/abort-environment-update.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      163 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/delete-application.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1106 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-environments.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1586 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-events.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      408 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/request-environment-info.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1916 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-configuration-options.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      199 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/rebuild-environment.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      236 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/delete-environment-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      210 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/restart-app-server.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      226 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/create-storage-location.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      592 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/create-configuration-template.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1499 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-environment-health.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      938 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/retrieve-environment-info.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      855 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/terminate-environment.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      263 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/delete-configuration-template.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1276 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-applications.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      282 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/delete-application-version.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      915 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/update-configuration-template.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1186 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-application-versions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      781 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/update-application-version.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1737 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/create-environment.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      932 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/create-application-version.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3234 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/update-environment.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      236 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/swap-environment-cnames.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2560 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/list-available-solution-stacks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      317 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/check-dns-availability.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      986 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-environment-resources.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2052 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-instances-health.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      766 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/update-application.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      832 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/elasticbeanstalk/create-application.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/redshift/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      488 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-resize.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      945 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/modify-cluster.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      603 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/revoke-cluster-security-group-ingress.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      994 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-reserved-nodes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      937 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-events.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1446 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/create-cluster.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      865 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/create-cluster-subnet-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      184 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/delete-cluster-snapshot.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1268 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/create-cluster-security-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/create-cluster-parameter-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      329 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/delete-cluster-subnet-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2217 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-cluster-parameters.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      603 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/delete-cluster.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1459 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/reboot-cluster.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1499 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-reserved-node-offerings.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1310 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-default-cluster-parameters.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      930 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-cluster-subnet-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1351 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/revoke-snapshot-access.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1096 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/purchase-reserved-node-offering.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      556 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-cluster-versions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1806 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-orderable-cluster-options.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      222 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/delete-cluster-parameter-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      282 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/reset-cluster-parameter-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      939 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/create-cluster-snapshot.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1049 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/copy-cluster-snapshot.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1301 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/authorize-snapshot-access.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      626 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/authorize-cluster-security-group-ingress.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1152 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/modify-cluster-subnet-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      981 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-cluster-parameter-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1010 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-cluster-security-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      840 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/modify-cluster-parameter-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2445 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-cluster-snapshots.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/delete-cluster-security-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2005 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/describe-clusters.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1281 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/redshift/restore-from-cluster-snapshot.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/deploy/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      651 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/get-on-premises-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      904 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/deregister.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      292 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/delete-deployment-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      511 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/list-on-premises-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      389 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/list-deployment-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      209 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/delete-application.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      605 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/get-deployment-config.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1175 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/get-deployment.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      372 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/list-deployment-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      928 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/push.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      384 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/create-deployment-config.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      452 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/get-application.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1133 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/batch-get-on-premises-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      460 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/register-on-premises-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      442 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/list-deployment-configs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      473 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/uninstall.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      507 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/list-deployments.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      983 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/list-application-revisions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      964 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/register.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      641 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/remove-tags-from-on-premises-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      293 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/list-applications.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      259 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/delete-deployment-config.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      360 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/stop-deployment.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      588 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/update-deployment-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2009 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/get-deployment-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      543 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/deregister-on-premises-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      766 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/install.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      911 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/get-deployment-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      468 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/register-application-revision.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      745 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/batch-get-applications.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      585 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/create-deployment-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      279 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/update-application.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      419 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/add-tags-to-on-premises-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2361 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/batch-get-deployments.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      975 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/get-application-revision.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/create-application.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      481 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/deploy/create-deployment.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/ssm/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      709 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/create-document.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      862 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/list-associations.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      698 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/get-document.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      569 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/create-association.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      747 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/update-association-status.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      392 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/describe-document.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      332 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/list-documents.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      213 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/delete-document.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      842 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/describe-association.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      281 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/delete-association.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1042 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ssm/create-association-batch.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/ecs/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3569 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/create-service.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1550 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/describe-task-definition.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      484 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/update-service.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      498 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/create-cluster.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      636 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/update-container-agent.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      513 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/list-container-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      613 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/list-task-definition-families.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1732 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/describe-tasks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      497 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/delete-cluster.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1621 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/describe-services.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      238 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/delete-service.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1287 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/run-task.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2838 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/describe-container-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      263 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/list-services.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1107 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/deregister-task-definition.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      416 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/deregister-container-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2849 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/register-task-definition.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      331 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/list-clusters.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      586 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/describe-clusters.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      794 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/list-tasks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1257 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ecs/list-task-definitions.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/rds/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      778 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/rds/create-option-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      696 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/rds/download-db-log-file-portion.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      780 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/rds/add-tag-to-resource.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      546 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/rds/describe-db-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2028 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/rds/create-db-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      695 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/rds/create-db-security-group.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/cloudwatch/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1898 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/describe-alarm-history.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4200 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/get-metric-statistics.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1751 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/describe-alarms.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/disable-alarm-actions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      401 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/set-alarm-state.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3562 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/describe-alarms-for-metric.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      253 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/delete-alarms.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      803 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/put-metric-alarm.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/enable-alarm-actions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      755 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/put-metric-data.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2527 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudwatch/list-metrics.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/cloudformation/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      843 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudformation/list-stacks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1432 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudformation/create-stack.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1435 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudformation/describe-stacks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1266 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudformation/update-stack.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1077 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudformation/get-template.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudformation/cancel-update-stack.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      834 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudformation/validate-template.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/iam/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      492 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-user-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      369 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-login-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      852 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      789 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-role.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      733 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-policy-version.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      513 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/generate-credential-report.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      628 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-virtual-mfa-devices.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      446 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-saml-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1166 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/upload-server-certificate.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      525 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-user-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      506 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-group-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      399 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      784 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-virtual-mfa-device.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      586 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-signing-certificate.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      471 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-policy-version.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      824 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/put-role-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      340 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      705 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/resync-mfa-device.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      403 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-account-alias.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      715 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-access-key.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      846 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-policy-version.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      709 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/add-client-id-to-open-id-connect-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-saml-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      579 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-saml-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      659 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-attached-role-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      484 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/detach-group-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2139 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-login-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      393 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-user.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      896 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-groups-for-user.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      698 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-open-id-connect-provider-thumbprint.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1135 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-instance-profiles-for-role.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      820 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-account-password-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      592 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/put-user-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1003 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-access-keys.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      618 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-open-id-connect-providers.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1641 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/change-password.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      409 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-role-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      394 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-account-alias.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      877 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-group-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      842 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-access-key.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      873 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-user-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      510 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/attach-user-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      727 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/remove-client-id-from-open-id-connect-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      527 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/set-default-policy-version.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      403 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-instance-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      519 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-group-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      526 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-open-id-connect-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      710 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-assume-role-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      548 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/put-group-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      509 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/attach-group-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      650 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/add-role-to-instance-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      788 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-signing-certificates.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      634 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-role.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      981 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-role.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      895 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-login-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      454 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/detach-user-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      514 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/attach-role-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-mfa-devices.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      891 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-login-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2338 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-instance-profiles.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      491 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-credential-report.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      414 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-account-aliases.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      594 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      928 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-role-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      751 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-attached-user-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      802 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-policy-versions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      622 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-user.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      755 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-users.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1285 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-account-summary.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      394 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      619 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-access-key-last-used.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      580 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-saml-providers.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      772 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-entities-for-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      898 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/upload-signing-certificate.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      574 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-user.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      808 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-open-id-connect-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1283 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1336 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      597 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-role-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2405 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-open-id-connect-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      446 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-virtual-mfa-device.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      419 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-account-password-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      543 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/deactivate-mfa-device.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      803 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/enable-mfa-device.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-account-password-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      921 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/create-instance-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      445 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/add-user-to-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1491 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-roles.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1136 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-instance-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      620 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-access-key.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      612 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-signing-certificate.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      390 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/delete-user.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      778 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/list-attached-group-policies.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      676 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/update-saml-provider.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      474 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/remove-user-from-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9183 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/get-account-authorization-details.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      491 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/remove-role-from-instance-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      511 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iam/detach-role-policy.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/iot/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1532 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/iot/create-certificate-from-csr.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/s3/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4763 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/sync.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      525 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/mb.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      641 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/rb.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1414 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/rm.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7036 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/_concepts.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4809 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/cp.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2832 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/mv.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      883 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/website.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2846 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3/ls.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/workspaces/
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      735 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/workspaces/create-workspaces.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      920 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/workspaces/describe-workspaces.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/workspaces/terminate-workspaces.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1755 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/workspaces/describe-workspace-directories.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     3556 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/workspaces/describe-workspace-bundles.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/route53/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7633 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/change-resource-record-sets.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      193 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/delete-hosted-zone.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      293 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/get-health-check.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1434 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/list-hosted-zones-by-name.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      602 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/create-hosted-zone.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      804 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/list-health-checks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1390 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/create-health-check.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      264 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/delete-health-check.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      288 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/get-change.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      789 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/list-hosted-zones.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      215 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/get-hosted-zone.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      955 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/route53/list-resource-record-sets.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/emr/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      648 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/add-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      151 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/list-steps.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      196 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/modify-cluster-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1146 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/describe-step.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1462 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/ssh.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6239 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/describe-cluster.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19103 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/create-cluster-examples.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      287 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/put.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      258 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/get.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4477 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/add-steps.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      749 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/create-cluster-synopsis.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      526 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/schedule-hbase-backup.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      165 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/wait.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      670 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/list-clusters.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      184 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/remove-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5688 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/create-default-roles.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      273 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/socks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2182 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/emr/list-instances.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/storagegateway/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/storagegateway/describe-gateway-information.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      260 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/storagegateway/list-gateways.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      547 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/storagegateway/list-volumes.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/sns/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      587 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/create-topic.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      552 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/list-subscriptions-by-topic.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1304 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/get-topic-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      758 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/get-subscription-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      353 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/publish.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      173 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/unsubscribe.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      484 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/list-subscriptions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      220 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/list-topics.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      146 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/delete-topic.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/subscribe.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      651 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sns/confirm-subscription.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/opsworks/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2117 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/create-app.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      903 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/deregister-rds-db-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      637 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/delete-app.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      870 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/update-rds-db-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1030 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/register-rds-db-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1017 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/assign-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/update-layer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      608 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/associate-elastic-ip.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      720 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-elastic-ips.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1194 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/set-time-based-auto-scaling.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      877 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/delete-user-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1825 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-deployments.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      529 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/update-app.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      635 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/attach-elastic-load-balancer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      566 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/disassociate-elastic-ip.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1193 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/create-stack.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2379 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-stacks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/deregister-elastic-ip.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      845 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/delete-stack.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      809 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/register-elastic-ip.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      870 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/update-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1379 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/set-permission.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1462 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/set-load-based-auto-scaling.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1178 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-apps.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      882 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-stack-summary.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      874 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/stop-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      643 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/deregister-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1204 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/delete-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      947 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-volumes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1340 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-timebased-auto-scaling.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2100 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-commands.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/stop-stack.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      824 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/delete-layer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1365 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-load-based-auto-scaling.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1285 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/create-user-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      959 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/start-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/start-stack.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      835 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/update-my-user-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1015 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-permissions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7115 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/register.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      632 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/unassign-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      548 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/update-elastic-ip.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      831 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/unassign-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      698 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/create-layer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      950 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-my-user-profile.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      807 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/get-hostname-suggestion.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      597 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/update-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      560 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/reboot-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1154 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/create-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1247 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-elastic-load-balancers.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      750 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/deregister-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5885 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-layers.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      751 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/register-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      633 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/detach-elastic-load-balancer.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      665 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/assign-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1125 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-rds-db-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3512 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1034 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-user-profiles.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1185 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/describe-raid-arrays.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2623 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/opsworks/create-deployment.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/s3api/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      701 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-cors.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      144 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-bucket-tagging.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      531 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-acl.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      845 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/upload-part.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      489 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-notification-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1327 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/list-parts.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      596 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/create-multipart-upload.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1109 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-notification-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      631 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-lifecycle.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      417 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/head-object.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      790 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-object-acl.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      171 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-versioning.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      148 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-bucket-lifecycle.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1405 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-lifecycle-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      386 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/copy-object.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      880 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-lifecycle-configuration.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      434 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-website.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1035 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/list-multipart-uploads.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      391 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-object-torrent.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      483 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/list-buckets.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      285 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-tagging.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      553 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-object.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      558 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-objects.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      582 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-acl.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      300 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-website.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      960 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-cors.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1318 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-logging.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      152 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-bucket-replication.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      647 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-object.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1075 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      468 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-notification.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      195 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-versioning.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      372 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-tagging.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      554 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-object-acl.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      463 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/abort-multipart-upload.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1247 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-replication.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      538 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-object.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      560 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/list-objects.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      176 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/create-bucket.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1007 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1019 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-notification.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      135 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-bucket-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1598 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/put-bucket-lifecycle.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      225 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-location.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      667 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/get-bucket-replication.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2584 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/list-object-versions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      163 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-bucket-cors.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      126 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-bucket.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      144 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/delete-bucket-website.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      326 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/head-bucket.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1550 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/s3api/complete-multipart-upload.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/ses/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      820 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/verify-domain-dkim.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      498 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/set-identity-dkim-enabled.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1188 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/get-send-statistics.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1369 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/get-identity-notification-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1260 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/get-send-quota.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      630 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/verify-domain-identity.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      970 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/verify-email-identity.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2308 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/send-email.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      529 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/delete-identity.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1152 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/get-identity-dkim-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      890 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/set-identity-feedback-forwarding-enabled.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      997 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/get-identity-verification-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      728 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/set-identity-notification-topic.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      906 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/list-identities.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2043 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ses/send-raw-email.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/importexport/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      237 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/importexport/cancel-job.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      408 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/importexport/list-jobs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1539 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/importexport/create-job.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      936 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/importexport/get-shipping-label.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1210 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/importexport/get-status.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      482 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/importexport/update-job.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/glacier/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      799 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/upload-archive.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1307 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/list-parts.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      939 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/describe-job.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      647 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/get-vault-notifications.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      851 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/initiate-multipart-upload.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      259 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/create-vault.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1869 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/initiate-job.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      620 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/set-vault-notifications.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1866 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/list-jobs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      377 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/list-tags-for-vault.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      546 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/list-multipart-uploads.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      837 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/abort-multipart-upload.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      639 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/list-vaults.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      315 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/remove-tags-from-vault.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      965 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/set-data-retrieval-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      468 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/get-data-retrieval-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      297 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/delete-vault.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      270 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/describe-vault.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1020 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/upload-multipart-part.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1007 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/complete-multipart-upload.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1201 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/get-job-output.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      299 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/glacier/add-tags-to-vault.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/sqs/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      679 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/create-queue.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2011 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/receive-message.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2185 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/send-message-batch.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      789 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/list-queues.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      989 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/set-queue-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      859 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/send-message.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      192 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/delete-queue.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      594 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/delete-message-batch.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      274 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/remove-permission.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1270 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/get-queue-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      359 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/change-message-visibility.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      793 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/change-message-visibility-batch.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      429 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/list-dead-letter-source-queues.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      211 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/get-queue-url.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      204 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/purge-queue.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      230 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/delete-message.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      333 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/sqs/add-permission.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/configure/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/configure/get/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      807 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/configure/get/_examples.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1936 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/configure/get/_description.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/configure/set/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      864 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/configure/set/_examples.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      896 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/configure/set/_description.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2027 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/configure/_description.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/ec2/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3645 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4931 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-spot-fleet-requests.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      802 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-availability-zones.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      275 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-volume-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      349 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/replace-network-acl-association.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      239 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/reject-vpc-peering-connection.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      277 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/detach-internet-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      377 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/replace-route.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      318 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/attach-network-interface.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      244 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-route.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      290 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-vpn-connection-route.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1729 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-spot-fleet-request-history.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      311 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/disable-vgw-route-propagation.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      283 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/confirm-product-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      200 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-placement-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6201 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/request-spot-fleet.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3560 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-reserved-instances-offerings.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      274 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/cancel-conversion-task.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      662 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-flow-logs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      286 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/associate-route-table.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      217 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-internet-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      619 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-snapshot-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      245 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/disassociate-route-table.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1144 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/import-key-pair.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      350 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-prefix-lists.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      195 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/disable-vpc-classic-link.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      811 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-route.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      627 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-subnet.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1438 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpcs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      930 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-vpc-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      244 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpc-endpoint-services.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      757 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/stop-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      999 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/register-image.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      846 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpn-gateways.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      241 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/report-instance-status.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      411 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/unmonitor-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      426 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/purchase-reserved-instances-offering.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      265 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-network-acl-entry.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      622 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/authorize-security-group-egress.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1229 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      346 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/attach-vpn-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      626 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpc-endpoints.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      373 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-vpc-endpoints.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      723 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-security-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      545 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-subnet-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      272 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/attach-internet-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      164 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-vpc.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      285 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/detach-vpn-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      577 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-spot-fleet-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9440 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/run-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1252 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-vpc-peering-connection.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      304 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-vpn-connection-route.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2187 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-account-attributes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      691 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/accept-vpc-peering-connection.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      636 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/revoke-security-group-egress.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1161 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-internet-gateways.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      527 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-dhcp-options.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      220 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-network-interface.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      844 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-network-acl.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      268 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/detach-network-interface.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      336 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/unassign-private-ip-addresses.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      377 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-key-pair.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1376 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-conversion-tasks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      557 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-key-pairs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1273 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpn-connections.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4107 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-security-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      758 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/start-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      169 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-placement-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1440 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-instance-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      435 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-key-pair.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      220 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-vpn-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      179 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-flow-logs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      276 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/reset-snapshot-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1672 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3186 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-volumes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      413 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-spot-datafeed-subscription.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      505 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/cancel-bundle-task.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      368 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/cancel-spot-instance-requests.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      699 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-image-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      196 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-route-table.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1024 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-instance-status.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1981 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-regions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1476 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-subnets.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      323 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/copy-image.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      447 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/attach-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      581 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-snapshot.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1029 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-image.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      557 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/associate-dhcp-options.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      290 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/get-console-output.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1108 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-image-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      393 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-spot-datafeed-subscription.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      253 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/detach-classic-link-vpc.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      209 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-dhcp-options.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      403 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/reboot-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3624 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-network-interfaces.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2121 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-spot-price-history.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      856 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-dhcp-options.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1658 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-reserved-instances-modifications.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      354 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-placement-groups.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      866 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/assign-private-ip-addresses.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-route-table.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2029 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-network-interface-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      814 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-vpc.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      659 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpc-classic-link.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1199 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-tags.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      282 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/restore-address-to-classic.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      798 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-export-tasks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      777 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-vpc-endpoint.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1911 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-images.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      455 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-customer-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1787 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-snapshots.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      232 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-vpc-peering-connection.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      304 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/enable-vgw-route-propagation.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      216 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-customer-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      448 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-snapshot-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1090 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-customer-gateways.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      555 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-bundle-tasks.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      704 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-flow-logs.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      895 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/reset-instance-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      196 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-network-acl.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2801 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/authorize-security-group-ingress.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      887 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/bundle-instance.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      319 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/reset-image-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      225 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/move-address-to-vpc.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      179 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-subnet.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      382 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-volume-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      349 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/replace-route-table-association.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2553 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpc-peering-connections.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      395 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/detach-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1788 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-route-tables.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      405 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/replace-network-acl-entry.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1221 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-classic-link-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      515 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/disassociate-address.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      222 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-volume.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2320 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-reserved-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2442 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-spot-instance-requests.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      234 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-spot-datafeed-subscription.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      560 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/allocate-address.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1480 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-volume-status.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      274 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-internet-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2045 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-reserved-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      309 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/attach-classic-link-vpc.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1044 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/revoke-security-group-ingress.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      192 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/enable-vpc-classic-link.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1106 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-network-interface.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      405 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/monitor-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      894 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-instance-export-task.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      943 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/get-password-data.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1251 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-network-interface-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      498 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/release-address.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1627 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-instance-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4991 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/request-spot-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      727 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/terminate-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      775 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-security-group.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      688 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-spot-fleet-request.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3896 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-network-acls.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      441 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-network-acl-entry.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1548 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-vpn-connection.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1325 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-instances.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      181 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/deregister-image.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      223 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-snapshot.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2611 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-addresses.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      996 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/associate-address.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      469 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-moving-addresses.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1140 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/cancel-spot-fleet-requests.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1045 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/describe-vpc-attribute.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      327 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/modify-vpc-endpoint.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      435 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/copy-snapshot.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      208 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/delete-vpn-connection.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      327 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/create-vpn-gateway.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      240 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/ec2/cancel-export-task.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/logs/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1095 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/put-log-events.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      731 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/describe-log-streams.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      180 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/delete-retention-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      175 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/create-log-stream.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      116 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/create-log-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      167 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/put-retention-policy.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      181 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/delete-log-stream.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      879 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/get-log-events.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      116 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/delete-log-group.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      472 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/logs/describe-log-groups.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/codecommit/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      660 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/update-repository-name.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      336 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/update-repository-description.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      259 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/list-branches.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      329 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/get-branch.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      799 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/create-repository.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1756 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/batch-get-repositories.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      868 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/get-repository.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      286 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/create-branch.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      483 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/list-repositories.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      312 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/update-default-branch.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      244 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/delete-repository.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      312 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/codecommit/delete-branch.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/swf/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2720 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/list-domains.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1938 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/register-domain.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1759 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/deprecate-domain.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1321 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/count-open-workflow-executions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      948 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/register-workflow-type.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1462 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/count-closed-workflow-executions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1175 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/list-workflow-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7143 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/list-activity-types.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1094 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/swf/describe-domain.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/cloudfront/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3207 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/list-distributions.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2733 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/get-distribution-config.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      666 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/list-invalidations.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      528 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/delete-distribution.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3379 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/get-distribution.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1180 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/create-invalidation.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      913 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/get-invalidation.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6076 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/update-distribution.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4475 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/cloudfront/create-distribution.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/examples/datapipeline/
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      689 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/add-tags.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      361 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/activate-pipeline.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      367 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/deactivate-pipeline.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1186 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/list-runs.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      399 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/put-pipeline-definition.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      250 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/create-pipeline.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     2935 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/get-pipeline-definition.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      606 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/list-pipelines.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      205 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/remove-tags.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)      152 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/delete-pipeline.rst
+-rwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)     1625 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/examples/datapipeline/describe-pipelines.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4888 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/paramfile.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    14650 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/shorthand.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/topics/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5817 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/topics/s3-config.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9617 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/topics/config-vars.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1966 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/topics/return-codes.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1208 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/topics/topic-tags.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3135 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/globalargs.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2626 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/removals.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4291 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/cloudsearch.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3278 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/iamvirtmfa.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3897 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/streamingoutputarg.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9721 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/waiters.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5906 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/toplevelbool.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10359 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/paginate.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4459 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/sessendemail.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3582 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/utils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      909 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/kms.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1805 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3endpoint.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1187 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/route53.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6746 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/ec2bundleinstance.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2778 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/rds.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12935 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/assumerole.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9505 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/flatten.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3518 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/awslambda.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5218 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/preview.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19648 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/opsworks.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3643 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/generatecliskeleton.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/s3/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13707 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/executor.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6204 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/comparator.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    15076 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/filegenerator.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    24569 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/utils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2845 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/transferconfig.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2656 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/s3.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3195 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/fileinfobuilder.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6492 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/filters.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13252 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/fileinfo.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    25094 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/s3handler.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    50238 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/subcommands.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6029 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/fileformat.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/s3/syncstrategy/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2001 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/syncstrategy/register.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1232 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/syncstrategy/delete.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1300 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/syncstrategy/sizeonly.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/syncstrategy/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1686 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/syncstrategy/exacttimestamps.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10112 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/syncstrategy/base.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    31170 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3/tasks.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1231 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/iot_data.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/emr/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    20172 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/createcluster.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     8482 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/steputils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9406 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/hbase.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3361 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/sshutils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5442 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/command.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9368 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/emrutils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7699 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/ssh.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12599 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/createdefaultroles.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2505 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/addinstancegroups.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2879 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/installapplications.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4001 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/describecluster.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2547 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/configutils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    16214 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/helptext.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1947 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/addsteps.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9813 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/argumentschema.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6535 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/applicationutils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1382 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/terminateclusters.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      952 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/hbaseutils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9106 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/emrfsutils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4761 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/config.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3135 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/instancegroupsutils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3639 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/modifyclusterattributes.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9917 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/exceptions.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3775 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/listclusters.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6458 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/constants.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1088 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/addtags.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3257 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/emr/emr.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3837 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/argrename.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6072 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/putmetricdata.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2351 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/iot.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    25967 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/configure.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/codedeploy/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5910 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/locationargs.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7196 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/register.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4595 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/utils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4205 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/install.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2202 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/uninstall.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6181 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/deregister.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10644 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/push.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2212 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/codedeploy.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7661 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codedeploy/systems.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1904 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/scalarparse.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1399 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/ec2protocolarg.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     8298 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/ec2secgroupsimplify.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/cloudtrail/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1641 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/cloudtrail/utils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    37906 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/cloudtrail/validation.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13705 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/cloudtrail/subscribe.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1337 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/cloudtrail/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1484 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4986 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/arguments.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7391 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/codecommit.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7503 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/ec2runinstances.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/configservice/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7116 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/configservice/subscribe.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      924 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/configservice/rename_cmd.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      565 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/configservice/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4258 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/configservice/getstatus.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3154 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/configservice/putconfigurationrecorder.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4703 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/ec2decryptpassword.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2480 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/s3errormsg.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1813 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/addexamples.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    16989 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/commands.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3679 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/cliinputjson.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2992 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/ec2addcount.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2015-11-24 01:59:34.000000 awscli-1.9.9/awscli/customizations/datapipeline/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9550 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/datapipeline/createdefaultroles.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7619 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/datapipeline/translator.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    17291 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/datapipeline/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1895 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/datapipeline/constants.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1074 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/customizations/cloudsearchdomain.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1464 2015-11-24 01:59:33.000000 awscli-1.9.9/awscli/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    18677 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/arguments.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    18849 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/argprocess.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     7462 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/handlers.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5833 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/schema.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6176 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/argparser.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    11121 2015-11-24 01:59:32.000000 awscli-1.9.9/awscli/formatter.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    17249 2015-11-24 01:59:34.000000 awscli-1.9.9/PKG-INFO
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      549 2015-11-24 01:59:32.000000 awscli-1.9.9/LICENSE.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    13505 2015-11-24 01:59:32.000000 awscli-1.9.9/README.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2247 2015-11-24 01:59:33.000000 awscli-1.9.9/setup.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      396 2015-11-24 01:59:32.000000 awscli-1.9.9/requirements.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      227 2015-11-24 01:59:34.000000 awscli-1.9.9/setup.cfg
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      141 2015-11-24 01:59:32.000000 awscli-1.9.9/MANIFEST.in
```

### Comparing `awscli-1.9.8/awscli.egg-info/PKG-INFO` & `awscli-1.9.9/awscli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: awscli
-Version: 1.9.8
+Version: 1.9.9
 Summary: Universal Command Line Environment for AWS.
 Home-page: http://aws.amazon.com/cli/
 Author: Amazon Web Services
 Author-email: UNKNOWN
 License: Apache License 2.0
 Description: =======
         aws-cli
```

### Comparing `awscli-1.9.8/awscli.egg-info/SOURCES.txt` & `awscli-1.9.9/awscli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/bin/aws.cmd` & `awscli-1.9.9/bin/aws.cmd`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/bin/aws` & `awscli-1.9.9/bin/aws`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/bin/aws_completer` & `awscli-1.9.9/bin/aws_completer`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/bin/aws_zsh_completer.sh` & `awscli-1.9.9/bin/aws_zsh_completer.sh`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/clidriver.py` & `awscli-1.9.9/awscli/clidriver.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/data/cli.json` & `awscli-1.9.9/awscli/data/cli.json`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/text.py` & `awscli-1.9.9/awscli/text.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/clidocs.py` & `awscli-1.9.9/awscli/clidocs.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/utils.py` & `awscli-1.9.9/awscli/utils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/plugin.py` & `awscli-1.9.9/awscli/plugin.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/completer.py` & `awscli-1.9.9/awscli/completer.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/errorhandler.py` & `awscli-1.9.9/awscli/errorhandler.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/help.py` & `awscli-1.9.9/awscli/help.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/topictags.py` & `awscli-1.9.9/awscli/topictags.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/table.py` & `awscli-1.9.9/awscli/table.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/compat.py` & `awscli-1.9.9/awscli/compat.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/testutils.py` & `awscli-1.9.9/awscli/testutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/describe-tags.rst` & `awscli-1.9.9/awscli/examples/elb/describe-tags.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/set-load-balancer-policies-of-listener.rst` & `awscli-1.9.9/awscli/examples/elb/set-load-balancer-policies-of-listener.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/describe-load-balancer-attributes.rst` & `awscli-1.9.9/awscli/examples/elb/describe-load-balancer-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/set-load-balancer-policies-for-backend-server.rst` & `awscli-1.9.9/awscli/examples/elb/set-load-balancer-policies-for-backend-server.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/modify-load-balancer-attributes.rst` & `awscli-1.9.9/awscli/examples/elb/modify-load-balancer-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/describe-load-balancers.rst` & `awscli-1.9.9/awscli/examples/elb/describe-load-balancers.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/describe-load-balancer-policies.rst` & `awscli-1.9.9/awscli/examples/elb/describe-load-balancer-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/describe-instance-health.rst` & `awscli-1.9.9/awscli/examples/elb/describe-instance-health.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/create-load-balancer.rst` & `awscli-1.9.9/awscli/examples/elb/create-load-balancer.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/describe-load-balancer-policy-types.rst` & `awscli-1.9.9/awscli/examples/elb/describe-load-balancer-policy-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/configure-health-check.rst` & `awscli-1.9.9/awscli/examples/elb/configure-health-check.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elb/create-load-balancer-policy.rst` & `awscli-1.9.9/awscli/examples/elb/create-load-balancer-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/batch-get-item.rst` & `awscli-1.9.9/awscli/examples/dynamodb/batch-get-item.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/create-table.rst` & `awscli-1.9.9/awscli/examples/dynamodb/create-table.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/put-item.rst` & `awscli-1.9.9/awscli/examples/dynamodb/put-item.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/query.rst` & `awscli-1.9.9/awscli/examples/dynamodb/query.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/get-item.rst` & `awscli-1.9.9/awscli/examples/dynamodb/get-item.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/delete-item.rst` & `awscli-1.9.9/awscli/examples/dynamodb/delete-item.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/update-table.rst` & `awscli-1.9.9/awscli/examples/dynamodb/update-table.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/describe-table.rst` & `awscli-1.9.9/awscli/examples/dynamodb/describe-table.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/scan.rst` & `awscli-1.9.9/awscli/examples/dynamodb/scan.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/update-item.rst` & `awscli-1.9.9/awscli/examples/dynamodb/update-item.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/dynamodb/batch-write-item.rst` & `awscli-1.9.9/awscli/examples/dynamodb/batch-write-item.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/delete-custom-action-type.rst` & `awscli-1.9.9/awscli/examples/codepipeline/delete-custom-action-type.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/get-pipeline.rst` & `awscli-1.9.9/awscli/examples/codepipeline/get-pipeline.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/update-pipeline.rst` & `awscli-1.9.9/awscli/examples/codepipeline/update-pipeline.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/poll-for-jobs.rst` & `awscli-1.9.9/awscli/examples/codepipeline/poll-for-jobs.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/create-pipeline.rst` & `awscli-1.9.9/awscli/examples/codepipeline/create-pipeline.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/create-custom-action-type.rst` & `awscli-1.9.9/awscli/examples/codepipeline/create-custom-action-type.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/list-action-types.rst` & `awscli-1.9.9/awscli/examples/codepipeline/list-action-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/get-pipeline-state.rst` & `awscli-1.9.9/awscli/examples/codepipeline/get-pipeline-state.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/list-pipelines.rst` & `awscli-1.9.9/awscli/examples/codepipeline/list-pipelines.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codepipeline/get-job-details.rst` & `awscli-1.9.9/awscli/examples/codepipeline/get-job-details.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/kms/decrypt.rst` & `awscli-1.9.9/awscli/examples/kms/decrypt.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/kms/encrypt.rst` & `awscli-1.9.9/awscli/examples/kms/encrypt.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-tags.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-tags.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/exit-standby.rst` & `awscli-1.9.9/awscli/examples/autoscaling/exit-standby.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-notification-configurations.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-notification-configurations.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/detach-instances.rst` & `awscli-1.9.9/awscli/examples/autoscaling/detach-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/put-scheduled-update-group-action.rst` & `awscli-1.9.9/awscli/examples/autoscaling/put-scheduled-update-group-action.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-auto-scaling-groups.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-auto-scaling-groups.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/delete-notification-configuration.rst` & `awscli-1.9.9/awscli/examples/autoscaling/delete-notification-configuration.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-auto-scaling-instances.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-auto-scaling-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/disable-metrics-collection.rst` & `awscli-1.9.9/awscli/examples/autoscaling/disable-metrics-collection.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-scaling-activities.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-scaling-activities.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/put-scaling-policy.rst` & `awscli-1.9.9/awscli/examples/autoscaling/put-scaling-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-termination-policy-types.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-termination-policy-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/enable-metrics-collection.rst` & `awscli-1.9.9/awscli/examples/autoscaling/enable-metrics-collection.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-adjustment-types.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-adjustment-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/delete-auto-scaling-group.rst` & `awscli-1.9.9/awscli/examples/autoscaling/delete-auto-scaling-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-account-limits.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-account-limits.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/terminate-instance-in-auto-scaling-group.rst` & `awscli-1.9.9/awscli/examples/autoscaling/terminate-instance-in-auto-scaling-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-launch-configurations.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-launch-configurations.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/create-auto-scaling-group.rst` & `awscli-1.9.9/awscli/examples/autoscaling/create-auto-scaling-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/put-notification-configuration.rst` & `awscli-1.9.9/awscli/examples/autoscaling/put-notification-configuration.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-lifecycle-hooks.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-lifecycle-hooks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-metric-collection-types.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-metric-collection-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/update-auto-scaling-group.rst` & `awscli-1.9.9/awscli/examples/autoscaling/update-auto-scaling-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/put-lifecycle-hook.rst` & `awscli-1.9.9/awscli/examples/autoscaling/put-lifecycle-hook.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/create-launch-configuration.rst` & `awscli-1.9.9/awscli/examples/autoscaling/create-launch-configuration.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-scheduled-actions.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-scheduled-actions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-scaling-process-types.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-scaling-process-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-auto-scaling-notification-types.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-auto-scaling-notification-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/enter-standby.rst` & `awscli-1.9.9/awscli/examples/autoscaling/enter-standby.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/autoscaling/describe-policies.rst` & `awscli-1.9.9/awscli/examples/autoscaling/describe-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/validate-configuration-settings.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/validate-configuration-settings.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-configuration-settings.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-configuration-settings.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-environments.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-environments.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-events.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-events.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-configuration-options.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-configuration-options.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/create-configuration-template.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/create-configuration-template.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-environment-health.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-environment-health.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/retrieve-environment-info.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/retrieve-environment-info.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/terminate-environment.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/terminate-environment.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-applications.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-applications.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/update-configuration-template.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/update-configuration-template.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-application-versions.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-application-versions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/update-application-version.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/update-application-version.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/create-environment.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/create-environment.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/create-application-version.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/create-application-version.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/update-environment.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/update-environment.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/list-available-solution-stacks.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/list-available-solution-stacks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-environment-resources.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-environment-resources.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/describe-instances-health.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/describe-instances-health.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/update-application.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/update-application.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/elasticbeanstalk/create-application.rst` & `awscli-1.9.9/awscli/examples/elasticbeanstalk/create-application.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/modify-cluster.rst` & `awscli-1.9.9/awscli/examples/redshift/modify-cluster.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/revoke-cluster-security-group-ingress.rst` & `awscli-1.9.9/awscli/examples/redshift/revoke-cluster-security-group-ingress.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-reserved-nodes.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-reserved-nodes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-events.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-events.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/create-cluster.rst` & `awscli-1.9.9/awscli/examples/redshift/create-cluster.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/create-cluster-subnet-group.rst` & `awscli-1.9.9/awscli/examples/redshift/create-cluster-subnet-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/create-cluster-security-group.rst` & `awscli-1.9.9/awscli/examples/redshift/create-cluster-security-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/create-cluster-parameter-group.rst` & `awscli-1.9.9/awscli/examples/redshift/create-cluster-parameter-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-cluster-parameters.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-cluster-parameters.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/delete-cluster.rst` & `awscli-1.9.9/awscli/examples/redshift/delete-cluster.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/reboot-cluster.rst` & `awscli-1.9.9/awscli/examples/redshift/reboot-cluster.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-reserved-node-offerings.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-reserved-node-offerings.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-default-cluster-parameters.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-default-cluster-parameters.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-cluster-subnet-groups.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-cluster-subnet-groups.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/revoke-snapshot-access.rst` & `awscli-1.9.9/awscli/examples/redshift/revoke-snapshot-access.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/purchase-reserved-node-offering.rst` & `awscli-1.9.9/awscli/examples/redshift/purchase-reserved-node-offering.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-cluster-versions.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-cluster-versions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-orderable-cluster-options.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-orderable-cluster-options.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/create-cluster-snapshot.rst` & `awscli-1.9.9/awscli/examples/redshift/create-cluster-snapshot.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/copy-cluster-snapshot.rst` & `awscli-1.9.9/awscli/examples/redshift/copy-cluster-snapshot.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/authorize-snapshot-access.rst` & `awscli-1.9.9/awscli/examples/redshift/authorize-snapshot-access.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/authorize-cluster-security-group-ingress.rst` & `awscli-1.9.9/awscli/examples/redshift/authorize-cluster-security-group-ingress.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/modify-cluster-subnet-group.rst` & `awscli-1.9.9/awscli/examples/redshift/modify-cluster-subnet-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-cluster-parameter-groups.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-cluster-parameter-groups.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-cluster-security-groups.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-cluster-security-groups.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/modify-cluster-parameter-group.rst` & `awscli-1.9.9/awscli/examples/redshift/modify-cluster-parameter-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-cluster-snapshots.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-cluster-snapshots.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/describe-clusters.rst` & `awscli-1.9.9/awscli/examples/redshift/describe-clusters.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/redshift/restore-from-cluster-snapshot.rst` & `awscli-1.9.9/awscli/examples/redshift/restore-from-cluster-snapshot.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/get-on-premises-instance.rst` & `awscli-1.9.9/awscli/examples/deploy/get-on-premises-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/deregister.rst` & `awscli-1.9.9/awscli/examples/deploy/deregister.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/get-deployment-config.rst` & `awscli-1.9.9/awscli/examples/deploy/get-deployment-config.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/get-deployment.rst` & `awscli-1.9.9/awscli/examples/deploy/get-deployment.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/push.rst` & `awscli-1.9.9/awscli/examples/deploy/push.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/batch-get-on-premises-instances.rst` & `awscli-1.9.9/awscli/examples/deploy/batch-get-on-premises-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/list-application-revisions.rst` & `awscli-1.9.9/awscli/examples/deploy/list-application-revisions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/register.rst` & `awscli-1.9.9/awscli/examples/deploy/register.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/remove-tags-from-on-premises-instances.rst` & `awscli-1.9.9/awscli/examples/deploy/remove-tags-from-on-premises-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/update-deployment-group.rst` & `awscli-1.9.9/awscli/examples/deploy/update-deployment-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/get-deployment-instance.rst` & `awscli-1.9.9/awscli/examples/deploy/get-deployment-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/deregister-on-premises-instance.rst` & `awscli-1.9.9/awscli/examples/deploy/deregister-on-premises-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/install.rst` & `awscli-1.9.9/awscli/examples/deploy/install.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/get-deployment-group.rst` & `awscli-1.9.9/awscli/examples/deploy/get-deployment-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/batch-get-applications.rst` & `awscli-1.9.9/awscli/examples/deploy/batch-get-applications.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/create-deployment-group.rst` & `awscli-1.9.9/awscli/examples/deploy/create-deployment-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/batch-get-deployments.rst` & `awscli-1.9.9/awscli/examples/deploy/batch-get-deployments.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/deploy/get-application-revision.rst` & `awscli-1.9.9/awscli/examples/deploy/get-application-revision.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ssm/create-document.rst` & `awscli-1.9.9/awscli/examples/ssm/create-document.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ssm/list-associations.rst` & `awscli-1.9.9/awscli/examples/ssm/list-associations.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ssm/get-document.rst` & `awscli-1.9.9/awscli/examples/ssm/get-document.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ssm/create-association.rst` & `awscli-1.9.9/awscli/examples/ssm/create-association.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ssm/update-association-status.rst` & `awscli-1.9.9/awscli/examples/ssm/update-association-status.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ssm/describe-association.rst` & `awscli-1.9.9/awscli/examples/ssm/describe-association.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ssm/create-association-batch.rst` & `awscli-1.9.9/awscli/examples/ssm/create-association-batch.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/create-service.rst` & `awscli-1.9.9/awscli/examples/ecs/create-service.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/describe-task-definition.rst` & `awscli-1.9.9/awscli/examples/ecs/describe-task-definition.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/update-container-agent.rst` & `awscli-1.9.9/awscli/examples/ecs/update-container-agent.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/list-container-instances.rst` & `awscli-1.9.9/awscli/examples/ecs/list-container-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/list-task-definition-families.rst` & `awscli-1.9.9/awscli/examples/ecs/list-task-definition-families.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/describe-tasks.rst` & `awscli-1.9.9/awscli/examples/ecs/describe-tasks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/describe-services.rst` & `awscli-1.9.9/awscli/examples/ecs/describe-services.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/run-task.rst` & `awscli-1.9.9/awscli/examples/ecs/run-task.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/describe-container-instances.rst` & `awscli-1.9.9/awscli/examples/ecs/describe-container-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/deregister-task-definition.rst` & `awscli-1.9.9/awscli/examples/ecs/deregister-task-definition.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/register-task-definition.rst` & `awscli-1.9.9/awscli/examples/ecs/register-task-definition.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/describe-clusters.rst` & `awscli-1.9.9/awscli/examples/ecs/describe-clusters.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/list-tasks.rst` & `awscli-1.9.9/awscli/examples/ecs/list-tasks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ecs/list-task-definitions.rst` & `awscli-1.9.9/awscli/examples/ecs/list-task-definitions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/rds/create-option-group.rst` & `awscli-1.9.9/awscli/examples/rds/create-option-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/rds/download-db-log-file-portion.rst` & `awscli-1.9.9/awscli/examples/rds/download-db-log-file-portion.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/rds/add-tag-to-resource.rst` & `awscli-1.9.9/awscli/examples/rds/add-tag-to-resource.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/rds/describe-db-instances.rst` & `awscli-1.9.9/awscli/examples/rds/describe-db-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/rds/create-db-instance.rst` & `awscli-1.9.9/awscli/examples/rds/create-db-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/rds/create-db-security-group.rst` & `awscli-1.9.9/awscli/examples/rds/create-db-security-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudwatch/describe-alarm-history.rst` & `awscli-1.9.9/awscli/examples/cloudwatch/describe-alarm-history.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudwatch/get-metric-statistics.rst` & `awscli-1.9.9/awscli/examples/cloudwatch/get-metric-statistics.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudwatch/describe-alarms.rst` & `awscli-1.9.9/awscli/examples/cloudwatch/describe-alarms.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudwatch/describe-alarms-for-metric.rst` & `awscli-1.9.9/awscli/examples/cloudwatch/describe-alarms-for-metric.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudwatch/put-metric-alarm.rst` & `awscli-1.9.9/awscli/examples/cloudwatch/put-metric-alarm.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudwatch/put-metric-data.rst` & `awscli-1.9.9/awscli/examples/cloudwatch/put-metric-data.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudwatch/list-metrics.rst` & `awscli-1.9.9/awscli/examples/cloudwatch/list-metrics.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudformation/list-stacks.rst` & `awscli-1.9.9/awscli/examples/cloudformation/list-stacks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudformation/create-stack.rst` & `awscli-1.9.9/awscli/examples/cloudformation/create-stack.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudformation/describe-stacks.rst` & `awscli-1.9.9/awscli/examples/cloudformation/describe-stacks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudformation/update-stack.rst` & `awscli-1.9.9/awscli/examples/cloudformation/update-stack.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudformation/get-template.rst` & `awscli-1.9.9/awscli/examples/cloudformation/get-template.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudformation/validate-template.rst` & `awscli-1.9.9/awscli/examples/cloudformation/validate-template.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-policy.rst` & `awscli-1.9.9/awscli/examples/iam/get-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-role.rst` & `awscli-1.9.9/awscli/examples/iam/get-role.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-policy-version.rst` & `awscli-1.9.9/awscli/examples/iam/create-policy-version.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/generate-credential-report.rst` & `awscli-1.9.9/awscli/examples/iam/generate-credential-report.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-virtual-mfa-devices.rst` & `awscli-1.9.9/awscli/examples/iam/list-virtual-mfa-devices.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/upload-server-certificate.rst` & `awscli-1.9.9/awscli/examples/iam/upload-server-certificate.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/delete-user-policy.rst` & `awscli-1.9.9/awscli/examples/iam/delete-user-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-virtual-mfa-device.rst` & `awscli-1.9.9/awscli/examples/iam/create-virtual-mfa-device.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-group.rst` & `awscli-1.9.9/awscli/examples/iam/get-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/update-signing-certificate.rst` & `awscli-1.9.9/awscli/examples/iam/update-signing-certificate.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-groups.rst` & `awscli-1.9.9/awscli/examples/iam/list-groups.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/put-role-policy.rst` & `awscli-1.9.9/awscli/examples/iam/put-role-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/resync-mfa-device.rst` & `awscli-1.9.9/awscli/examples/iam/resync-mfa-device.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/update-access-key.rst` & `awscli-1.9.9/awscli/examples/iam/update-access-key.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-policy-version.rst` & `awscli-1.9.9/awscli/examples/iam/get-policy-version.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/add-client-id-to-open-id-connect-provider.rst` & `awscli-1.9.9/awscli/examples/iam/add-client-id-to-open-id-connect-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-saml-provider.rst` & `awscli-1.9.9/awscli/examples/iam/get-saml-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-saml-provider.rst` & `awscli-1.9.9/awscli/examples/iam/create-saml-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-attached-role-policies.rst` & `awscli-1.9.9/awscli/examples/iam/list-attached-role-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-login-profile.rst` & `awscli-1.9.9/awscli/examples/iam/create-login-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-groups-for-user.rst` & `awscli-1.9.9/awscli/examples/iam/list-groups-for-user.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/update-open-id-connect-provider-thumbprint.rst` & `awscli-1.9.9/awscli/examples/iam/update-open-id-connect-provider-thumbprint.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-instance-profiles-for-role.rst` & `awscli-1.9.9/awscli/examples/iam/list-instance-profiles-for-role.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-account-password-policy.rst` & `awscli-1.9.9/awscli/examples/iam/get-account-password-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/put-user-policy.rst` & `awscli-1.9.9/awscli/examples/iam/put-user-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-access-keys.rst` & `awscli-1.9.9/awscli/examples/iam/list-access-keys.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-open-id-connect-providers.rst` & `awscli-1.9.9/awscli/examples/iam/list-open-id-connect-providers.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/change-password.rst` & `awscli-1.9.9/awscli/examples/iam/change-password.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-group-policy.rst` & `awscli-1.9.9/awscli/examples/iam/get-group-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-access-key.rst` & `awscli-1.9.9/awscli/examples/iam/create-access-key.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-user-policy.rst` & `awscli-1.9.9/awscli/examples/iam/get-user-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/remove-client-id-from-open-id-connect-provider.rst` & `awscli-1.9.9/awscli/examples/iam/remove-client-id-from-open-id-connect-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/set-default-policy-version.rst` & `awscli-1.9.9/awscli/examples/iam/set-default-policy-version.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-group-policies.rst` & `awscli-1.9.9/awscli/examples/iam/list-group-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/delete-open-id-connect-provider.rst` & `awscli-1.9.9/awscli/examples/iam/delete-open-id-connect-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/update-assume-role-policy.rst` & `awscli-1.9.9/awscli/examples/iam/update-assume-role-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/put-group-policy.rst` & `awscli-1.9.9/awscli/examples/iam/put-group-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/add-role-to-instance-profile.rst` & `awscli-1.9.9/awscli/examples/iam/add-role-to-instance-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-signing-certificates.rst` & `awscli-1.9.9/awscli/examples/iam/list-signing-certificates.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/delete-role.rst` & `awscli-1.9.9/awscli/examples/iam/delete-role.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-role.rst` & `awscli-1.9.9/awscli/examples/iam/create-role.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/update-login-profile.rst` & `awscli-1.9.9/awscli/examples/iam/update-login-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/attach-role-policy.rst` & `awscli-1.9.9/awscli/examples/iam/attach-role-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-mfa-devices.rst` & `awscli-1.9.9/awscli/examples/iam/list-mfa-devices.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-login-profile.rst` & `awscli-1.9.9/awscli/examples/iam/get-login-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-instance-profiles.rst` & `awscli-1.9.9/awscli/examples/iam/list-instance-profiles.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-group.rst` & `awscli-1.9.9/awscli/examples/iam/create-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-role-policy.rst` & `awscli-1.9.9/awscli/examples/iam/get-role-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-attached-user-policies.rst` & `awscli-1.9.9/awscli/examples/iam/list-attached-user-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-policy-versions.rst` & `awscli-1.9.9/awscli/examples/iam/list-policy-versions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-user.rst` & `awscli-1.9.9/awscli/examples/iam/create-user.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-users.rst` & `awscli-1.9.9/awscli/examples/iam/list-users.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-account-summary.rst` & `awscli-1.9.9/awscli/examples/iam/get-account-summary.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-access-key-last-used.rst` & `awscli-1.9.9/awscli/examples/iam/get-access-key-last-used.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-saml-providers.rst` & `awscli-1.9.9/awscli/examples/iam/list-saml-providers.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-entities-for-policy.rst` & `awscli-1.9.9/awscli/examples/iam/list-entities-for-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/upload-signing-certificate.rst` & `awscli-1.9.9/awscli/examples/iam/upload-signing-certificate.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-user.rst` & `awscli-1.9.9/awscli/examples/iam/get-user.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-open-id-connect-provider.rst` & `awscli-1.9.9/awscli/examples/iam/get-open-id-connect-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-policies.rst` & `awscli-1.9.9/awscli/examples/iam/list-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-policy.rst` & `awscli-1.9.9/awscli/examples/iam/create-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-role-policies.rst` & `awscli-1.9.9/awscli/examples/iam/list-role-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-open-id-connect-provider.rst` & `awscli-1.9.9/awscli/examples/iam/create-open-id-connect-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/deactivate-mfa-device.rst` & `awscli-1.9.9/awscli/examples/iam/deactivate-mfa-device.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/enable-mfa-device.rst` & `awscli-1.9.9/awscli/examples/iam/enable-mfa-device.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/update-account-password-policy.rst` & `awscli-1.9.9/awscli/examples/iam/update-account-password-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/create-instance-profile.rst` & `awscli-1.9.9/awscli/examples/iam/create-instance-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-roles.rst` & `awscli-1.9.9/awscli/examples/iam/list-roles.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-instance-profile.rst` & `awscli-1.9.9/awscli/examples/iam/get-instance-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/delete-access-key.rst` & `awscli-1.9.9/awscli/examples/iam/delete-access-key.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/delete-signing-certificate.rst` & `awscli-1.9.9/awscli/examples/iam/delete-signing-certificate.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/list-attached-group-policies.rst` & `awscli-1.9.9/awscli/examples/iam/list-attached-group-policies.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/update-saml-provider.rst` & `awscli-1.9.9/awscli/examples/iam/update-saml-provider.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iam/get-account-authorization-details.rst` & `awscli-1.9.9/awscli/examples/iam/get-account-authorization-details.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/iot/create-certificate-from-csr.rst` & `awscli-1.9.9/awscli/examples/iot/create-certificate-from-csr.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/sync.rst` & `awscli-1.9.9/awscli/examples/s3/sync.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/mb.rst` & `awscli-1.9.9/awscli/examples/s3/mb.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/rb.rst` & `awscli-1.9.9/awscli/examples/s3/rb.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/rm.rst` & `awscli-1.9.9/awscli/examples/s3/rm.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/_concepts.rst` & `awscli-1.9.9/awscli/examples/s3/_concepts.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/cp.rst` & `awscli-1.9.9/awscli/examples/s3/cp.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/mv.rst` & `awscli-1.9.9/awscli/examples/s3/mv.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/website.rst` & `awscli-1.9.9/awscli/examples/s3/website.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3/ls.rst` & `awscli-1.9.9/awscli/examples/s3/ls.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/workspaces/create-workspaces.rst` & `awscli-1.9.9/awscli/examples/workspaces/create-workspaces.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/workspaces/describe-workspaces.rst` & `awscli-1.9.9/awscli/examples/workspaces/describe-workspaces.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/workspaces/describe-workspace-directories.rst` & `awscli-1.9.9/awscli/examples/workspaces/describe-workspace-directories.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/workspaces/describe-workspace-bundles.rst` & `awscli-1.9.9/awscli/examples/workspaces/describe-workspace-bundles.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/route53/change-resource-record-sets.rst` & `awscli-1.9.9/awscli/examples/route53/change-resource-record-sets.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/route53/list-hosted-zones-by-name.rst` & `awscli-1.9.9/awscli/examples/route53/list-hosted-zones-by-name.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/route53/create-hosted-zone.rst` & `awscli-1.9.9/awscli/examples/route53/create-hosted-zone.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/route53/list-health-checks.rst` & `awscli-1.9.9/awscli/examples/route53/list-health-checks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/route53/create-health-check.rst` & `awscli-1.9.9/awscli/examples/route53/create-health-check.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/route53/list-hosted-zones.rst` & `awscli-1.9.9/awscli/examples/route53/list-hosted-zones.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/route53/list-resource-record-sets.rst` & `awscli-1.9.9/awscli/examples/route53/list-resource-record-sets.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/add-tags.rst` & `awscli-1.9.9/awscli/examples/emr/add-tags.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/describe-step.rst` & `awscli-1.9.9/awscli/examples/emr/describe-step.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/ssh.rst` & `awscli-1.9.9/awscli/examples/emr/ssh.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/describe-cluster.rst` & `awscli-1.9.9/awscli/examples/emr/describe-cluster.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/create-cluster-examples.rst` & `awscli-1.9.9/awscli/examples/emr/create-cluster-examples.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/add-steps.rst` & `awscli-1.9.9/awscli/examples/emr/add-steps.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/create-cluster-synopsis.rst` & `awscli-1.9.9/awscli/examples/emr/create-cluster-synopsis.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/schedule-hbase-backup.rst` & `awscli-1.9.9/awscli/examples/emr/schedule-hbase-backup.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/list-clusters.rst` & `awscli-1.9.9/awscli/examples/emr/list-clusters.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/create-default-roles.rst` & `awscli-1.9.9/awscli/examples/emr/create-default-roles.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/emr/list-instances.rst` & `awscli-1.9.9/awscli/examples/emr/list-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/storagegateway/describe-gateway-information.rst` & `awscli-1.9.9/awscli/examples/storagegateway/describe-gateway-information.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/storagegateway/list-volumes.rst` & `awscli-1.9.9/awscli/examples/storagegateway/list-volumes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sns/create-topic.rst` & `awscli-1.9.9/awscli/examples/sns/create-topic.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sns/list-subscriptions-by-topic.rst` & `awscli-1.9.9/awscli/examples/sns/list-subscriptions-by-topic.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sns/get-topic-attributes.rst` & `awscli-1.9.9/awscli/examples/sns/get-topic-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sns/get-subscription-attributes.rst` & `awscli-1.9.9/awscli/examples/sns/get-subscription-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sns/confirm-subscription.rst` & `awscli-1.9.9/awscli/examples/sns/confirm-subscription.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/create-app.rst` & `awscli-1.9.9/awscli/examples/opsworks/create-app.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/deregister-rds-db-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/deregister-rds-db-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/delete-app.rst` & `awscli-1.9.9/awscli/examples/opsworks/delete-app.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/update-rds-db-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/update-rds-db-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/register-rds-db-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/register-rds-db-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/assign-volume.rst` & `awscli-1.9.9/awscli/examples/opsworks/assign-volume.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/update-layer.rst` & `awscli-1.9.9/awscli/examples/opsworks/update-layer.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/associate-elastic-ip.rst` & `awscli-1.9.9/awscli/examples/opsworks/associate-elastic-ip.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-elastic-ips.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-elastic-ips.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/set-time-based-auto-scaling.rst` & `awscli-1.9.9/awscli/examples/opsworks/set-time-based-auto-scaling.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/delete-user-profile.rst` & `awscli-1.9.9/awscli/examples/opsworks/delete-user-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-deployments.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-deployments.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/update-app.rst` & `awscli-1.9.9/awscli/examples/opsworks/update-app.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/attach-elastic-load-balancer.rst` & `awscli-1.9.9/awscli/examples/opsworks/attach-elastic-load-balancer.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/disassociate-elastic-ip.rst` & `awscli-1.9.9/awscli/examples/opsworks/disassociate-elastic-ip.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/create-stack.rst` & `awscli-1.9.9/awscli/examples/opsworks/create-stack.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-stacks.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-stacks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/deregister-elastic-ip.rst` & `awscli-1.9.9/awscli/examples/opsworks/deregister-elastic-ip.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/delete-stack.rst` & `awscli-1.9.9/awscli/examples/opsworks/delete-stack.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/register-elastic-ip.rst` & `awscli-1.9.9/awscli/examples/opsworks/register-elastic-ip.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/update-volume.rst` & `awscli-1.9.9/awscli/examples/opsworks/update-volume.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/set-permission.rst` & `awscli-1.9.9/awscli/examples/opsworks/set-permission.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/set-load-based-auto-scaling.rst` & `awscli-1.9.9/awscli/examples/opsworks/set-load-based-auto-scaling.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-apps.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-apps.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-stack-summary.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-stack-summary.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/stop-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/stop-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/deregister-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/deregister-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/delete-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/delete-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-volumes.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-volumes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-timebased-auto-scaling.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-timebased-auto-scaling.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-commands.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-commands.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/stop-stack.rst` & `awscli-1.9.9/awscli/examples/opsworks/stop-stack.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/delete-layer.rst` & `awscli-1.9.9/awscli/examples/opsworks/delete-layer.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-load-based-auto-scaling.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-load-based-auto-scaling.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/create-user-profile.rst` & `awscli-1.9.9/awscli/examples/opsworks/create-user-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/start-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/start-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/start-stack.rst` & `awscli-1.9.9/awscli/examples/opsworks/start-stack.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/update-my-user-profile.rst` & `awscli-1.9.9/awscli/examples/opsworks/update-my-user-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-permissions.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-permissions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/register.rst` & `awscli-1.9.9/awscli/examples/opsworks/register.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/unassign-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/unassign-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/update-elastic-ip.rst` & `awscli-1.9.9/awscli/examples/opsworks/update-elastic-ip.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/unassign-volume.rst` & `awscli-1.9.9/awscli/examples/opsworks/unassign-volume.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/create-layer.rst` & `awscli-1.9.9/awscli/examples/opsworks/create-layer.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-my-user-profile.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-my-user-profile.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/get-hostname-suggestion.rst` & `awscli-1.9.9/awscli/examples/opsworks/get-hostname-suggestion.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/update-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/update-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/reboot-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/reboot-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/create-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/create-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-elastic-load-balancers.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-elastic-load-balancers.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/deregister-volume.rst` & `awscli-1.9.9/awscli/examples/opsworks/deregister-volume.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-layers.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-layers.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/register-volume.rst` & `awscli-1.9.9/awscli/examples/opsworks/register-volume.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/detach-elastic-load-balancer.rst` & `awscli-1.9.9/awscli/examples/opsworks/detach-elastic-load-balancer.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/assign-instance.rst` & `awscli-1.9.9/awscli/examples/opsworks/assign-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-rds-db-instances.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-rds-db-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-instances.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-user-profiles.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-user-profiles.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/describe-raid-arrays.rst` & `awscli-1.9.9/awscli/examples/opsworks/describe-raid-arrays.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/opsworks/create-deployment.rst` & `awscli-1.9.9/awscli/examples/opsworks/create-deployment.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-cors.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-cors.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-acl.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-acl.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/upload-part.rst` & `awscli-1.9.9/awscli/examples/s3api/upload-part.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/list-parts.rst` & `awscli-1.9.9/awscli/examples/s3api/list-parts.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/create-multipart-upload.rst` & `awscli-1.9.9/awscli/examples/s3api/create-multipart-upload.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-notification-configuration.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-notification-configuration.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-bucket-lifecycle.rst` & `awscli-1.9.9/awscli/examples/s3api/get-bucket-lifecycle.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-object-acl.rst` & `awscli-1.9.9/awscli/examples/s3api/get-object-acl.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-lifecycle-configuration.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-lifecycle-configuration.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-bucket-lifecycle-configuration.rst` & `awscli-1.9.9/awscli/examples/s3api/get-bucket-lifecycle-configuration.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/list-multipart-uploads.rst` & `awscli-1.9.9/awscli/examples/s3api/list-multipart-uploads.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-object.rst` & `awscli-1.9.9/awscli/examples/s3api/get-object.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/delete-objects.rst` & `awscli-1.9.9/awscli/examples/s3api/delete-objects.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-bucket-acl.rst` & `awscli-1.9.9/awscli/examples/s3api/get-bucket-acl.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-bucket-cors.rst` & `awscli-1.9.9/awscli/examples/s3api/get-bucket-cors.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-logging.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-logging.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-object.rst` & `awscli-1.9.9/awscli/examples/s3api/put-object.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-bucket-policy.rst` & `awscli-1.9.9/awscli/examples/s3api/get-bucket-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-object-acl.rst` & `awscli-1.9.9/awscli/examples/s3api/put-object-acl.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-replication.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-replication.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/delete-object.rst` & `awscli-1.9.9/awscli/examples/s3api/delete-object.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/list-objects.rst` & `awscli-1.9.9/awscli/examples/s3api/list-objects.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-policy.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-notification.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-notification.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/put-bucket-lifecycle.rst` & `awscli-1.9.9/awscli/examples/s3api/put-bucket-lifecycle.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/get-bucket-replication.rst` & `awscli-1.9.9/awscli/examples/s3api/get-bucket-replication.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/list-object-versions.rst` & `awscli-1.9.9/awscli/examples/s3api/list-object-versions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/s3api/complete-multipart-upload.rst` & `awscli-1.9.9/awscli/examples/s3api/complete-multipart-upload.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/verify-domain-dkim.rst` & `awscli-1.9.9/awscli/examples/ses/verify-domain-dkim.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/get-send-statistics.rst` & `awscli-1.9.9/awscli/examples/ses/get-send-statistics.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/get-identity-notification-attributes.rst` & `awscli-1.9.9/awscli/examples/ses/get-identity-notification-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/get-send-quota.rst` & `awscli-1.9.9/awscli/examples/ses/get-send-quota.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/verify-domain-identity.rst` & `awscli-1.9.9/awscli/examples/ses/verify-domain-identity.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/verify-email-identity.rst` & `awscli-1.9.9/awscli/examples/ses/verify-email-identity.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/send-email.rst` & `awscli-1.9.9/awscli/examples/ses/send-email.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/delete-identity.rst` & `awscli-1.9.9/awscli/examples/ses/delete-identity.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/get-identity-dkim-attributes.rst` & `awscli-1.9.9/awscli/examples/ses/get-identity-dkim-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/set-identity-feedback-forwarding-enabled.rst` & `awscli-1.9.9/awscli/examples/ses/set-identity-feedback-forwarding-enabled.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/get-identity-verification-attributes.rst` & `awscli-1.9.9/awscli/examples/ses/get-identity-verification-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/set-identity-notification-topic.rst` & `awscli-1.9.9/awscli/examples/ses/set-identity-notification-topic.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/list-identities.rst` & `awscli-1.9.9/awscli/examples/ses/list-identities.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ses/send-raw-email.rst` & `awscli-1.9.9/awscli/examples/ses/send-raw-email.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/importexport/create-job.rst` & `awscli-1.9.9/awscli/examples/importexport/create-job.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/importexport/get-shipping-label.rst` & `awscli-1.9.9/awscli/examples/importexport/get-shipping-label.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/importexport/get-status.rst` & `awscli-1.9.9/awscli/examples/importexport/get-status.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/upload-archive.rst` & `awscli-1.9.9/awscli/examples/glacier/upload-archive.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/list-parts.rst` & `awscli-1.9.9/awscli/examples/glacier/list-parts.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/describe-job.rst` & `awscli-1.9.9/awscli/examples/glacier/describe-job.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/get-vault-notifications.rst` & `awscli-1.9.9/awscli/examples/glacier/get-vault-notifications.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/initiate-multipart-upload.rst` & `awscli-1.9.9/awscli/examples/glacier/initiate-multipart-upload.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/initiate-job.rst` & `awscli-1.9.9/awscli/examples/glacier/initiate-job.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/set-vault-notifications.rst` & `awscli-1.9.9/awscli/examples/glacier/set-vault-notifications.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/list-jobs.rst` & `awscli-1.9.9/awscli/examples/glacier/list-jobs.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/list-multipart-uploads.rst` & `awscli-1.9.9/awscli/examples/glacier/list-multipart-uploads.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/abort-multipart-upload.rst` & `awscli-1.9.9/awscli/examples/glacier/abort-multipart-upload.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/list-vaults.rst` & `awscli-1.9.9/awscli/examples/glacier/list-vaults.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/set-data-retrieval-policy.rst` & `awscli-1.9.9/awscli/examples/glacier/set-data-retrieval-policy.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/upload-multipart-part.rst` & `awscli-1.9.9/awscli/examples/glacier/upload-multipart-part.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/complete-multipart-upload.rst` & `awscli-1.9.9/awscli/examples/glacier/complete-multipart-upload.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/glacier/get-job-output.rst` & `awscli-1.9.9/awscli/examples/glacier/get-job-output.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/create-queue.rst` & `awscli-1.9.9/awscli/examples/sqs/create-queue.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/receive-message.rst` & `awscli-1.9.9/awscli/examples/sqs/receive-message.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/send-message-batch.rst` & `awscli-1.9.9/awscli/examples/sqs/send-message-batch.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/list-queues.rst` & `awscli-1.9.9/awscli/examples/sqs/list-queues.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/set-queue-attributes.rst` & `awscli-1.9.9/awscli/examples/sqs/set-queue-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/send-message.rst` & `awscli-1.9.9/awscli/examples/sqs/send-message.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/delete-message-batch.rst` & `awscli-1.9.9/awscli/examples/sqs/delete-message-batch.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/get-queue-attributes.rst` & `awscli-1.9.9/awscli/examples/sqs/get-queue-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/sqs/change-message-visibility-batch.rst` & `awscli-1.9.9/awscli/examples/sqs/change-message-visibility-batch.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/configure/get/_examples.rst` & `awscli-1.9.9/awscli/examples/configure/get/_examples.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/configure/get/_description.rst` & `awscli-1.9.9/awscli/examples/configure/get/_description.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/configure/set/_examples.rst` & `awscli-1.9.9/awscli/examples/configure/set/_examples.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/configure/set/_description.rst` & `awscli-1.9.9/awscli/examples/configure/set/_description.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/configure/_description.rst` & `awscli-1.9.9/awscli/examples/configure/_description.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-tags.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-tags.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-spot-fleet-requests.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-spot-fleet-requests.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-availability-zones.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-availability-zones.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-spot-fleet-request-history.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-spot-fleet-request-history.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/request-spot-fleet.rst` & `awscli-1.9.9/awscli/examples/ec2/request-spot-fleet.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-reserved-instances-offerings.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-reserved-instances-offerings.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-flow-logs.rst` & `awscli-1.9.9/awscli/examples/ec2/create-flow-logs.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-snapshot-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-snapshot-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/import-key-pair.rst` & `awscli-1.9.9/awscli/examples/ec2/import-key-pair.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-route.rst` & `awscli-1.9.9/awscli/examples/ec2/create-route.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-subnet.rst` & `awscli-1.9.9/awscli/examples/ec2/create-subnet.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-vpcs.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-vpcs.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-vpc-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-vpc-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/stop-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/stop-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/register-image.rst` & `awscli-1.9.9/awscli/examples/ec2/register-image.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-vpn-gateways.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-vpn-gateways.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/authorize-security-group-egress.rst` & `awscli-1.9.9/awscli/examples/ec2/authorize-security-group-egress.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-volume.rst` & `awscli-1.9.9/awscli/examples/ec2/create-volume.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-vpc-endpoints.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-vpc-endpoints.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/delete-security-group.rst` & `awscli-1.9.9/awscli/examples/ec2/delete-security-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-subnet-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-subnet-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-spot-fleet-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-spot-fleet-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/run-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/run-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-vpc-peering-connection.rst` & `awscli-1.9.9/awscli/examples/ec2/create-vpc-peering-connection.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-account-attributes.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-account-attributes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/accept-vpc-peering-connection.rst` & `awscli-1.9.9/awscli/examples/ec2/accept-vpc-peering-connection.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/revoke-security-group-egress.rst` & `awscli-1.9.9/awscli/examples/ec2/revoke-security-group-egress.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-internet-gateways.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-internet-gateways.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-dhcp-options.rst` & `awscli-1.9.9/awscli/examples/ec2/create-dhcp-options.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-network-acl.rst` & `awscli-1.9.9/awscli/examples/ec2/create-network-acl.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-conversion-tasks.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-conversion-tasks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-key-pairs.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-key-pairs.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-vpn-connections.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-vpn-connections.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-security-groups.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-security-groups.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/start-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/start-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-instance-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-instance-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-tags.rst` & `awscli-1.9.9/awscli/examples/ec2/create-tags.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-volumes.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-volumes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-image-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-image-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-instance-status.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-instance-status.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-regions.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-regions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-subnets.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-subnets.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-snapshot.rst` & `awscli-1.9.9/awscli/examples/ec2/create-snapshot.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-image.rst` & `awscli-1.9.9/awscli/examples/ec2/create-image.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/associate-dhcp-options.rst` & `awscli-1.9.9/awscli/examples/ec2/associate-dhcp-options.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-image-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-image-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-network-interfaces.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-network-interfaces.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-spot-price-history.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-spot-price-history.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-dhcp-options.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-dhcp-options.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-reserved-instances-modifications.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-reserved-instances-modifications.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/assign-private-ip-addresses.rst` & `awscli-1.9.9/awscli/examples/ec2/assign-private-ip-addresses.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-route-table.rst` & `awscli-1.9.9/awscli/examples/ec2/create-route-table.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-network-interface-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-network-interface-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-vpc.rst` & `awscli-1.9.9/awscli/examples/ec2/create-vpc.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-vpc-classic-link.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-vpc-classic-link.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/delete-tags.rst` & `awscli-1.9.9/awscli/examples/ec2/delete-tags.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-export-tasks.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-export-tasks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-vpc-endpoint.rst` & `awscli-1.9.9/awscli/examples/ec2/create-vpc-endpoint.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-images.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-images.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-snapshots.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-snapshots.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-customer-gateways.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-customer-gateways.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-bundle-tasks.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-bundle-tasks.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-flow-logs.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-flow-logs.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/reset-instance-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/reset-instance-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/authorize-security-group-ingress.rst` & `awscli-1.9.9/awscli/examples/ec2/authorize-security-group-ingress.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/bundle-instance.rst` & `awscli-1.9.9/awscli/examples/ec2/bundle-instance.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-vpc-peering-connections.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-vpc-peering-connections.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-route-tables.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-route-tables.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-classic-link-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-classic-link-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/disassociate-address.rst` & `awscli-1.9.9/awscli/examples/ec2/disassociate-address.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-reserved-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-reserved-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-spot-instance-requests.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-spot-instance-requests.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/allocate-address.rst` & `awscli-1.9.9/awscli/examples/ec2/allocate-address.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-volume-status.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-volume-status.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-reserved-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-reserved-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/revoke-security-group-ingress.rst` & `awscli-1.9.9/awscli/examples/ec2/revoke-security-group-ingress.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-network-interface.rst` & `awscli-1.9.9/awscli/examples/ec2/create-network-interface.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-instance-export-task.rst` & `awscli-1.9.9/awscli/examples/ec2/create-instance-export-task.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/get-password-data.rst` & `awscli-1.9.9/awscli/examples/ec2/get-password-data.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-network-interface-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-network-interface-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-instance-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-instance-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/request-spot-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/request-spot-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/terminate-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/terminate-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-security-group.rst` & `awscli-1.9.9/awscli/examples/ec2/create-security-group.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/modify-spot-fleet-request.rst` & `awscli-1.9.9/awscli/examples/ec2/modify-spot-fleet-request.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-network-acls.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-network-acls.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/create-vpn-connection.rst` & `awscli-1.9.9/awscli/examples/ec2/create-vpn-connection.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-instances.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-instances.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-addresses.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-addresses.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/associate-address.rst` & `awscli-1.9.9/awscli/examples/ec2/associate-address.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/cancel-spot-fleet-requests.rst` & `awscli-1.9.9/awscli/examples/ec2/cancel-spot-fleet-requests.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/ec2/describe-vpc-attribute.rst` & `awscli-1.9.9/awscli/examples/ec2/describe-vpc-attribute.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/logs/put-log-events.rst` & `awscli-1.9.9/awscli/examples/logs/put-log-events.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/logs/describe-log-streams.rst` & `awscli-1.9.9/awscli/examples/logs/describe-log-streams.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/logs/get-log-events.rst` & `awscli-1.9.9/awscli/examples/logs/get-log-events.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codecommit/update-repository-name.rst` & `awscli-1.9.9/awscli/examples/codecommit/update-repository-name.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codecommit/create-repository.rst` & `awscli-1.9.9/awscli/examples/codecommit/create-repository.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codecommit/batch-get-repositories.rst` & `awscli-1.9.9/awscli/examples/codecommit/batch-get-repositories.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/codecommit/get-repository.rst` & `awscli-1.9.9/awscli/examples/codecommit/get-repository.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/list-domains.rst` & `awscli-1.9.9/awscli/examples/swf/list-domains.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/register-domain.rst` & `awscli-1.9.9/awscli/examples/swf/register-domain.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/deprecate-domain.rst` & `awscli-1.9.9/awscli/examples/swf/deprecate-domain.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/count-open-workflow-executions.rst` & `awscli-1.9.9/awscli/examples/swf/count-open-workflow-executions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/register-workflow-type.rst` & `awscli-1.9.9/awscli/examples/swf/register-workflow-type.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/count-closed-workflow-executions.rst` & `awscli-1.9.9/awscli/examples/swf/count-closed-workflow-executions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/list-workflow-types.rst` & `awscli-1.9.9/awscli/examples/swf/list-workflow-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/list-activity-types.rst` & `awscli-1.9.9/awscli/examples/swf/list-activity-types.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/swf/describe-domain.rst` & `awscli-1.9.9/awscli/examples/swf/describe-domain.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/list-distributions.rst` & `awscli-1.9.9/awscli/examples/cloudfront/list-distributions.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/get-distribution-config.rst` & `awscli-1.9.9/awscli/examples/cloudfront/get-distribution-config.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/list-invalidations.rst` & `awscli-1.9.9/awscli/examples/cloudfront/list-invalidations.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/delete-distribution.rst` & `awscli-1.9.9/awscli/examples/cloudfront/delete-distribution.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/get-distribution.rst` & `awscli-1.9.9/awscli/examples/cloudfront/get-distribution.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/create-invalidation.rst` & `awscli-1.9.9/awscli/examples/cloudfront/create-invalidation.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/get-invalidation.rst` & `awscli-1.9.9/awscli/examples/cloudfront/get-invalidation.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/update-distribution.rst` & `awscli-1.9.9/awscli/examples/cloudfront/update-distribution.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/cloudfront/create-distribution.rst` & `awscli-1.9.9/awscli/examples/cloudfront/create-distribution.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/datapipeline/add-tags.rst` & `awscli-1.9.9/awscli/examples/datapipeline/add-tags.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/datapipeline/list-runs.rst` & `awscli-1.9.9/awscli/examples/datapipeline/list-runs.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/datapipeline/get-pipeline-definition.rst` & `awscli-1.9.9/awscli/examples/datapipeline/get-pipeline-definition.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/datapipeline/list-pipelines.rst` & `awscli-1.9.9/awscli/examples/datapipeline/list-pipelines.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/examples/datapipeline/describe-pipelines.rst` & `awscli-1.9.9/awscli/examples/datapipeline/describe-pipelines.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/paramfile.py` & `awscli-1.9.9/awscli/paramfile.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/shorthand.py` & `awscli-1.9.9/awscli/shorthand.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/topics/s3-config.rst` & `awscli-1.9.9/awscli/topics/s3-config.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/topics/config-vars.rst` & `awscli-1.9.9/awscli/topics/config-vars.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/topics/return-codes.rst` & `awscli-1.9.9/awscli/topics/return-codes.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/topics/topic-tags.json` & `awscli-1.9.9/awscli/topics/topic-tags.json`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/globalargs.py` & `awscli-1.9.9/awscli/customizations/globalargs.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/removals.py` & `awscli-1.9.9/awscli/customizations/removals.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/cloudsearch.py` & `awscli-1.9.9/awscli/customizations/cloudsearch.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/iamvirtmfa.py` & `awscli-1.9.9/awscli/customizations/iamvirtmfa.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/streamingoutputarg.py` & `awscli-1.9.9/awscli/customizations/streamingoutputarg.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/waiters.py` & `awscli-1.9.9/awscli/customizations/waiters.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/toplevelbool.py` & `awscli-1.9.9/awscli/customizations/toplevelbool.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/paginate.py` & `awscli-1.9.9/awscli/customizations/paginate.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/sessendemail.py` & `awscli-1.9.9/awscli/customizations/sessendemail.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/utils.py` & `awscli-1.9.9/awscli/customizations/utils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/kms.py` & `awscli-1.9.9/awscli/customizations/kms.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3endpoint.py` & `awscli-1.9.9/awscli/customizations/s3endpoint.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/route53.py` & `awscli-1.9.9/awscli/customizations/route53.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/ec2bundleinstance.py` & `awscli-1.9.9/awscli/customizations/ec2bundleinstance.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/rds.py` & `awscli-1.9.9/awscli/customizations/rds.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/assumerole.py` & `awscli-1.9.9/awscli/customizations/assumerole.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/flatten.py` & `awscli-1.9.9/awscli/customizations/flatten.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/awslambda.py` & `awscli-1.9.9/awscli/customizations/awslambda.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/preview.py` & `awscli-1.9.9/awscli/customizations/preview.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/opsworks.py` & `awscli-1.9.9/awscli/customizations/opsworks.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/generatecliskeleton.py` & `awscli-1.9.9/awscli/customizations/generatecliskeleton.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/executor.py` & `awscli-1.9.9/awscli/customizations/s3/executor.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/comparator.py` & `awscli-1.9.9/awscli/customizations/s3/comparator.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/filegenerator.py` & `awscli-1.9.9/awscli/customizations/s3/filegenerator.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/utils.py` & `awscli-1.9.9/awscli/customizations/s3/utils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/transferconfig.py` & `awscli-1.9.9/awscli/customizations/s3/transferconfig.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/s3.py` & `awscli-1.9.9/awscli/customizations/s3/s3.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/fileinfobuilder.py` & `awscli-1.9.9/awscli/customizations/s3/fileinfobuilder.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/filters.py` & `awscli-1.9.9/awscli/customizations/s3/filters.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/fileinfo.py` & `awscli-1.9.9/awscli/customizations/s3/fileinfo.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/s3handler.py` & `awscli-1.9.9/awscli/customizations/s3/s3handler.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/subcommands.py` & `awscli-1.9.9/awscli/customizations/s3/subcommands.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/__init__.py` & `awscli-1.9.9/awscli/customizations/s3/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/fileformat.py` & `awscli-1.9.9/awscli/customizations/s3/fileformat.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/syncstrategy/register.py` & `awscli-1.9.9/awscli/customizations/s3/syncstrategy/register.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/syncstrategy/delete.py` & `awscli-1.9.9/awscli/customizations/s3/syncstrategy/delete.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/syncstrategy/sizeonly.py` & `awscli-1.9.9/awscli/customizations/s3/syncstrategy/sizeonly.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/syncstrategy/__init__.py` & `awscli-1.9.9/awscli/customizations/s3/syncstrategy/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/syncstrategy/exacttimestamps.py` & `awscli-1.9.9/awscli/customizations/s3/syncstrategy/exacttimestamps.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/syncstrategy/base.py` & `awscli-1.9.9/awscli/customizations/s3/syncstrategy/base.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3/tasks.py` & `awscli-1.9.9/awscli/customizations/s3/tasks.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/iot_data.py` & `awscli-1.9.9/awscli/customizations/iot_data.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/createcluster.py` & `awscli-1.9.9/awscli/customizations/emr/createcluster.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/steputils.py` & `awscli-1.9.9/awscli/customizations/emr/steputils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/hbase.py` & `awscli-1.9.9/awscli/customizations/emr/hbase.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/sshutils.py` & `awscli-1.9.9/awscli/customizations/emr/sshutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/command.py` & `awscli-1.9.9/awscli/customizations/emr/command.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/emrutils.py` & `awscli-1.9.9/awscli/customizations/emr/emrutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/ssh.py` & `awscli-1.9.9/awscli/customizations/emr/ssh.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/createdefaultroles.py` & `awscli-1.9.9/awscli/customizations/emr/createdefaultroles.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/addinstancegroups.py` & `awscli-1.9.9/awscli/customizations/emr/addinstancegroups.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/installapplications.py` & `awscli-1.9.9/awscli/customizations/emr/installapplications.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/describecluster.py` & `awscli-1.9.9/awscli/customizations/emr/describecluster.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/configutils.py` & `awscli-1.9.9/awscli/customizations/emr/configutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/helptext.py` & `awscli-1.9.9/awscli/customizations/emr/helptext.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/addsteps.py` & `awscli-1.9.9/awscli/customizations/emr/addsteps.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/argumentschema.py` & `awscli-1.9.9/awscli/customizations/emr/argumentschema.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/applicationutils.py` & `awscli-1.9.9/awscli/customizations/emr/applicationutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/terminateclusters.py` & `awscli-1.9.9/awscli/customizations/emr/terminateclusters.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/hbaseutils.py` & `awscli-1.9.9/awscli/customizations/emr/hbaseutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/emrfsutils.py` & `awscli-1.9.9/awscli/customizations/emr/emrfsutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/config.py` & `awscli-1.9.9/awscli/customizations/emr/config.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/instancegroupsutils.py` & `awscli-1.9.9/awscli/customizations/emr/instancegroupsutils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/__init__.py` & `awscli-1.9.9/awscli/customizations/emr/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/modifyclusterattributes.py` & `awscli-1.9.9/awscli/customizations/emr/modifyclusterattributes.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/exceptions.py` & `awscli-1.9.9/awscli/customizations/emr/exceptions.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/listclusters.py` & `awscli-1.9.9/awscli/customizations/emr/listclusters.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/constants.py` & `awscli-1.9.9/awscli/customizations/emr/constants.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/addtags.py` & `awscli-1.9.9/awscli/customizations/emr/addtags.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/emr/emr.py` & `awscli-1.9.9/awscli/customizations/emr/emr.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/argrename.py` & `awscli-1.9.9/awscli/customizations/argrename.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/putmetricdata.py` & `awscli-1.9.9/awscli/customizations/putmetricdata.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/iot.py` & `awscli-1.9.9/awscli/customizations/iot.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/configure.py` & `awscli-1.9.9/awscli/customizations/configure.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/locationargs.py` & `awscli-1.9.9/awscli/customizations/codedeploy/locationargs.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/register.py` & `awscli-1.9.9/awscli/customizations/codedeploy/register.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/utils.py` & `awscli-1.9.9/awscli/customizations/codedeploy/utils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/install.py` & `awscli-1.9.9/awscli/customizations/codedeploy/install.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/uninstall.py` & `awscli-1.9.9/awscli/customizations/codedeploy/uninstall.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/deregister.py` & `awscli-1.9.9/awscli/customizations/codedeploy/deregister.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/push.py` & `awscli-1.9.9/awscli/customizations/codedeploy/push.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/codedeploy.py` & `awscli-1.9.9/awscli/customizations/codedeploy/codedeploy.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/__init__.py` & `awscli-1.9.9/awscli/customizations/codedeploy/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codedeploy/systems.py` & `awscli-1.9.9/awscli/customizations/codedeploy/systems.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/scalarparse.py` & `awscli-1.9.9/awscli/customizations/scalarparse.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/ec2protocolarg.py` & `awscli-1.9.9/awscli/customizations/ec2protocolarg.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/ec2secgroupsimplify.py` & `awscli-1.9.9/awscli/customizations/ec2secgroupsimplify.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/cloudtrail/utils.py` & `awscli-1.9.9/awscli/customizations/cloudtrail/utils.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/cloudtrail/validation.py` & `awscli-1.9.9/awscli/customizations/cloudtrail/validation.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/cloudtrail/subscribe.py` & `awscli-1.9.9/awscli/customizations/cloudtrail/subscribe.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/cloudtrail/__init__.py` & `awscli-1.9.9/awscli/customizations/cloudtrail/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/__init__.py` & `awscli-1.9.9/awscli/customizations/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/arguments.py` & `awscli-1.9.9/awscli/customizations/arguments.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/codecommit.py` & `awscli-1.9.9/awscli/customizations/codecommit.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/ec2runinstances.py` & `awscli-1.9.9/awscli/customizations/ec2runinstances.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/configservice/subscribe.py` & `awscli-1.9.9/awscli/customizations/configservice/subscribe.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/configservice/rename_cmd.py` & `awscli-1.9.9/awscli/customizations/configservice/rename_cmd.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/configservice/__init__.py` & `awscli-1.9.9/awscli/customizations/configservice/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/configservice/getstatus.py` & `awscli-1.9.9/awscli/customizations/configservice/getstatus.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/configservice/putconfigurationrecorder.py` & `awscli-1.9.9/awscli/customizations/configservice/putconfigurationrecorder.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/ec2decryptpassword.py` & `awscli-1.9.9/awscli/customizations/ec2decryptpassword.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/s3errormsg.py` & `awscli-1.9.9/awscli/customizations/s3errormsg.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/addexamples.py` & `awscli-1.9.9/awscli/customizations/addexamples.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/commands.py` & `awscli-1.9.9/awscli/customizations/commands.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/cliinputjson.py` & `awscli-1.9.9/awscli/customizations/cliinputjson.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/ec2addcount.py` & `awscli-1.9.9/awscli/customizations/ec2addcount.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/datapipeline/createdefaultroles.py` & `awscli-1.9.9/awscli/customizations/datapipeline/createdefaultroles.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/datapipeline/translator.py` & `awscli-1.9.9/awscli/customizations/datapipeline/translator.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/datapipeline/__init__.py` & `awscli-1.9.9/awscli/customizations/datapipeline/__init__.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/datapipeline/constants.py` & `awscli-1.9.9/awscli/customizations/datapipeline/constants.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/customizations/cloudsearchdomain.py` & `awscli-1.9.9/awscli/customizations/cloudsearchdomain.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/__init__.py` & `awscli-1.9.9/awscli/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 """
 AWSCLI
 ----
 A Universal Command Line Environment for Amazon Web Services.
 """
 import os
 
-__version__ = '1.9.8'
+__version__ = '1.9.9'
 
 #
 # Get our data path to be added to botocore's search path
 #
 _awscli_data_path = []
 if 'AWS_DATA_PATH' in os.environ:
     for path in os.environ['AWS_DATA_PATH'].split(os.pathsep):
```

### Comparing `awscli-1.9.8/awscli/arguments.py` & `awscli-1.9.9/awscli/arguments.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/argprocess.py` & `awscli-1.9.9/awscli/argprocess.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/handlers.py` & `awscli-1.9.9/awscli/handlers.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/schema.py` & `awscli-1.9.9/awscli/schema.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/argparser.py` & `awscli-1.9.9/awscli/argparser.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/awscli/formatter.py` & `awscli-1.9.9/awscli/formatter.py`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/PKG-INFO` & `awscli-1.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: awscli
-Version: 1.9.8
+Version: 1.9.9
 Summary: Universal Command Line Environment for AWS.
 Home-page: http://aws.amazon.com/cli/
 Author: Amazon Web Services
 Author-email: UNKNOWN
 License: Apache License 2.0
 Description: =======
         aws-cli
```

### Comparing `awscli-1.9.8/LICENSE.txt` & `awscli-1.9.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/README.rst` & `awscli-1.9.9/README.rst`

 * *Files identical despite different names*

### Comparing `awscli-1.9.8/setup.py` & `awscli-1.9.9/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import sys
 
 from setuptools import setup, find_packages
 
 import awscli
 
 
-requires = ['botocore==1.3.8',
+requires = ['botocore==1.3.9',
             'colorama>=0.2.5,<=0.3.3',
             'docutils>=0.10',
             'rsa>=3.1.2,<=3.3.0']
 
 
 if sys.version_info[:2] == (2, 6):
     # For python2.6 we have to require argparse since it
```

