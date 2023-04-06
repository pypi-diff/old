# Comparing `tmp/nameless-deploy-tools-1.98.tar.gz` & `tmp/nameless-deploy-tools-1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/nameless-deploy-tools-1.98.tar", last modified: Fri Sep 13 13:00:54 2019, max compression
+gzip compressed data, was "dist/nameless-deploy-tools-1.99.tar", last modified: Mon Sep 30 20:33:28 2019, max compression
```

## Comparing `nameless-deploy-tools-1.98.tar` & `nameless-deploy-tools-1.99.tar`

### file list

```diff
@@ -1,153 +1,153 @@
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/
--rw-r--r--   0 pasi      (1000) pasi      (1000)      312 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/MANIFEST.in
--rw-r--r--   0 pasi      (1000) pasi      (1000)      443 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/PKG-INFO
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4841 2019-09-13 13:00:48.000000 nameless-deploy-tools-1.98/README.md
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/bin/
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1575 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/create-shell-archive.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2926 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/encrypt-and-mount.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2388 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/ensure-letsencrypt-certs.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2346 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/lastpass-fetch-notes.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2276 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/lpssh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1905 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/mount-and-format.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1716 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/setup-fetch-secrets.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1536 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/bin/ssh-hostkeys-collect.sh
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/
--rw-r--r--   0 pasi      (1000) pasi      (1000)     5678 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/__init__.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4646 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/account_utils.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)    44628 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/aws_infra_util.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)    28809 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/cf_bootstrap.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)    12380 2019-07-08 13:43:01.000000 nameless-deploy-tools-1.98/n_utils/cf_deploy.py
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)    37274 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/cli.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     5200 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/cloudfront_utils.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1990 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/ecr_utils.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4471 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/git_utils.py
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/includes/
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     4885 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/apache_tools.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2452 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/autocomplete-helpers.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1480 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/aws_tools.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3828 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/bake-docker.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)    10588 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/bake-image.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)     9125 2019-09-13 12:59:34.000000 nameless-deploy-tools-1.98/n_utils/includes/bake-image.yml
--rw-r--r--   0 pasi      (1000) pasi      (1000)       56 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/bake-tags.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)     8424 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/bake-win-image.yml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      199 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/cloud-init-firewall-cmd.te
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      616 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/cloud_init_footer.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1987 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/cloud_init_functions.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2204 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/common_tools.sh
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/
--rw-r--r--   0 pasi      (1000) pasi      (1000)     3291 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/bakery-roles.yaml
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/
--rw-r--r--   0 pasi      (1000) pasi      (1000)    17295 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/generate_jobs.groovy
--rw-r--r--   0 pasi      (1000) pasi      (1000)      430 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/packages.txt
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1457 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/post_install.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)      421 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/pre_install.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1525 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/userdata.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4170 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins.yaml
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/network/
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1249 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/network/common.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4855 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/network.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)       47 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/route53.yaml
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3119 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.98/n_utils/includes/deploy-cdk.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3715 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.98/n_utils/includes/deploy-serverless.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3812 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.98/n_utils/includes/deploy-stack.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3757 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.98/n_utils/includes/deploy-terraform.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)      767 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/disk-by-drive-letter.ps1
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      599 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/ebs-functions.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)      283 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/fail2ban-rundir.te
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1806 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/fetch-secrets-lpass.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1351 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/fetch-secrets-s3.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1738 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/fetch-secrets-vault.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)    17013 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/generate_jobs.groovy
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3493 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/hook.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1691 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/install_tools.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     8827 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/jenkins_tools.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1501 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/lastpass-login.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      702 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/lastpass-logout.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)    67773 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.98/n_utils/includes/letsencrypt.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)   183299 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/lpass_centos_7
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_14.04
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_16.04
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_16.10
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_17.04
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1062 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/manage-account.yaml
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3477 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/nexus_tools.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      472 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/prepare.ps1
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)       22 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/prepare.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1836 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/print-create-instructions.sh
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/
--rw-r--r--   0 pasi      (1000) pasi      (1000)      258 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/libjpeg-turbo.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      136 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/logstash23.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      215 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/logstash6.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      211 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/mongodb32.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      194 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/mongodb34.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      200 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/mongodb36.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      200 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/mongodb40.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      195 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/mysql55-community.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      154 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/mysql57-community.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      239 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/newrelic-infra.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      151 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/newrelic.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      100 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/nginx.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      147 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/varnish41.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      147 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/repos/varnish62.repo
--rw-r--r--   0 pasi      (1000) pasi      (1000)      212 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/ssh-authorized-keys-command.te
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1337 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/ssh_tools.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      549 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/start-transcript.ps1
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      238 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/stop-transcript.ps1
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1493 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/store-secret-lpass.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      905 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/store-secret-s3.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      782 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/store-secret-vault.sh
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1015 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/apache-sg.yaml
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)      891 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/assume-deploy-role.sh
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/bootstrap/
--rw-r--r--   0 pasi      (1000) pasi      (1000)     3208 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/bootstrap/bakery-roles.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4926 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/bootstrap/network.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)     2617 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/delete-old-snapshots.js
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1900 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/delete-old-snapshots.min.js
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1622 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/delete-old-snapshots.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      990 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/external-lambdarole-policy.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      690 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/instanceprofile.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      924 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/internal-lambdarole-policy.yaml
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1392 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/nexus-userdata.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1850 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_baking.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1088 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_cloud_init.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      954 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_ec2_allow_volume_ops.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      845 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_ec2_associate_address.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      800 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_invoke_lambda.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      900 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_s3_secure_download.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      699 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policydoc_assumerole.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      843 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/role_bake.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      960 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/route53.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      890 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/sg_bake.yaml
--rw-r--r--   0 pasi      (1000) pasi      (1000)      969 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/template-snippets/sg_win_bake.yaml
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3008 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/terraform-pull-state.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     5956 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/tool_installers.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1236 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/trust-account-role.yaml
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2595 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/undeploy-cdk.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2882 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/undeploy-serverless.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2868 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/undeploy-stack.sh
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2912 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/undeploy-terraform.sh
--rw-r--r--   0 pasi      (1000) pasi      (1000)      243 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/win-userdata-unclean.txt.j2
--rw-r--r--   0 pasi      (1000) pasi      (1000)      496 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/includes/win-userdata.txt.j2
--rw-r--r--   0 pasi      (1000) pasi      (1000)     5501 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/log_events.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1966 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/maven_utils.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     5194 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/mfa_utils.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)       74 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/nameless-dt-enable-profile.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)       69 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/nameless-dt-load-project-env.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4784 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/ndt.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     9566 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/ndt_project.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)    12515 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/profile_util.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     2955 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/project_util.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     1536 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/tf_utils.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)    15386 2019-07-25 18:22:15.000000 nameless-deploy-tools-1.98/n_utils/utils.py
--rw-r--r--   0 pasi      (1000) pasi      (1000)     4179 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.98/n_utils/yuuuu3332111i1l1i.py
-drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/
--rw-r--r--   0 pasi      (1000) pasi      (1000)      443 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/PKG-INFO
--rw-r--r--   0 pasi      (1000) pasi      (1000)     5448 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/SOURCES.txt
--rw-r--r--   0 pasi      (1000) pasi      (1000)        1 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/dependency_links.txt
--rw-r--r--   0 pasi      (1000) pasi      (1000)      633 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/entry_points.txt
--rw-r--r--   0 pasi      (1000) pasi      (1000)        1 2019-07-08 13:38:33.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/not-zip-safe
--rw-r--r--   0 pasi      (1000) pasi      (1000)      180 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/requires.txt
--rw-r--r--   0 pasi      (1000) pasi      (1000)        8 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/top_level.txt
--rw-r--r--   0 pasi      (1000) pasi      (1000)      260 2019-09-13 13:00:54.000000 nameless-deploy-tools-1.98/setup.cfg
--rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2067 2019-09-13 13:00:48.000000 nameless-deploy-tools-1.98/setup.py
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      312 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/MANIFEST.in
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      443 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/PKG-INFO
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4841 2019-09-30 20:33:22.000000 nameless-deploy-tools-1.99/README.md
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/bin/
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1575 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/create-shell-archive.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2926 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/encrypt-and-mount.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2388 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/ensure-letsencrypt-certs.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2346 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/lastpass-fetch-notes.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2276 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/lpssh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1905 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/mount-and-format.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1716 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/setup-fetch-secrets.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1536 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/bin/ssh-hostkeys-collect.sh
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     5678 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/__init__.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4627 2019-09-30 10:49:57.000000 nameless-deploy-tools-1.99/n_utils/account_utils.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)    44628 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/aws_infra_util.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)    28809 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/cf_bootstrap.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)    12380 2019-07-08 13:43:01.000000 nameless-deploy-tools-1.99/n_utils/cf_deploy.py
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)    37274 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/cli.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     5200 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/cloudfront_utils.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1990 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/ecr_utils.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4471 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/git_utils.py
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/includes/
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     4885 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/apache_tools.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2452 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/autocomplete-helpers.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1480 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/aws_tools.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3828 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/bake-docker.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)    10588 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/bake-image.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     9125 2019-09-13 12:59:34.000000 nameless-deploy-tools-1.99/n_utils/includes/bake-image.yml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)       56 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/bake-tags.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     8424 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/bake-win-image.yml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      199 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/cloud-init-firewall-cmd.te
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      616 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/cloud_init_footer.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1987 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/cloud_init_functions.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2204 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/common_tools.sh
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     3291 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/bakery-roles.yaml
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)    17295 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/generate_jobs.groovy
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      430 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/packages.txt
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1457 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/post_install.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      421 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/pre_install.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1525 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/userdata.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4170 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins.yaml
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/network/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1249 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/network/common.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4855 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/network.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)       47 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/route53.yaml
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3119 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.99/n_utils/includes/deploy-cdk.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3715 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.99/n_utils/includes/deploy-serverless.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3961 2019-09-30 12:46:38.000000 nameless-deploy-tools-1.99/n_utils/includes/deploy-stack.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3757 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.99/n_utils/includes/deploy-terraform.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      767 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/disk-by-drive-letter.ps1
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      599 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/ebs-functions.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      283 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/fail2ban-rundir.te
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1806 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/fetch-secrets-lpass.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1351 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/fetch-secrets-s3.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1738 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/fetch-secrets-vault.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)    17013 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/generate_jobs.groovy
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3493 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/hook.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1691 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/install_tools.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     8827 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/jenkins_tools.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1501 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/lastpass-login.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      702 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/lastpass-logout.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)    67773 2019-09-04 05:55:32.000000 nameless-deploy-tools-1.99/n_utils/includes/letsencrypt.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)   183299 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/lpass_centos_7
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_14.04
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_16.04
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_16.10
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)   191632 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_17.04
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1062 2019-09-30 10:47:49.000000 nameless-deploy-tools-1.99/n_utils/includes/manage-account.yaml
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3477 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/nexus_tools.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      472 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/prepare.ps1
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)       22 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/prepare.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1836 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/print-create-instructions.sh
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      258 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/libjpeg-turbo.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      136 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/logstash23.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      215 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/logstash6.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      211 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/mongodb32.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      194 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/mongodb34.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      200 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/mongodb36.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      200 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/mongodb40.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      195 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/mysql55-community.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      154 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/mysql57-community.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      239 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/newrelic-infra.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      151 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/newrelic.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      100 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/nginx.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      147 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/varnish41.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      147 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/repos/varnish62.repo
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      212 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/ssh-authorized-keys-command.te
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1337 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/ssh_tools.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      549 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/start-transcript.ps1
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      238 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/stop-transcript.ps1
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1493 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/store-secret-lpass.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      905 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/store-secret-s3.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      782 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/store-secret-vault.sh
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1015 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/apache-sg.yaml
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)      891 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/assume-deploy-role.sh
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/bootstrap/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     3208 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/bootstrap/bakery-roles.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4926 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/bootstrap/network.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     2617 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/delete-old-snapshots.js
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1900 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/delete-old-snapshots.min.js
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1622 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/delete-old-snapshots.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      990 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/external-lambdarole-policy.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      690 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/instanceprofile.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      924 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/internal-lambdarole-policy.yaml
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     1392 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/nexus-userdata.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1850 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_baking.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1088 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_cloud_init.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      954 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_ec2_allow_volume_ops.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      845 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_ec2_associate_address.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      800 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_invoke_lambda.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      900 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_s3_secure_download.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      699 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policydoc_assumerole.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      843 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/role_bake.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      960 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/route53.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      890 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/sg_bake.yaml
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      969 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/template-snippets/sg_win_bake.yaml
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     3008 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/terraform-pull-state.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     5950 2019-09-30 20:32:13.000000 nameless-deploy-tools-1.99/n_utils/includes/tool_installers.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1236 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/trust-account-role.yaml
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2595 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/undeploy-cdk.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2882 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/undeploy-serverless.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2868 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/undeploy-stack.sh
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2912 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/undeploy-terraform.sh
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      243 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/win-userdata-unclean.txt.j2
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      496 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/includes/win-userdata.txt.j2
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     5501 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/log_events.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1966 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/maven_utils.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     5194 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/mfa_utils.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)       74 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/nameless-dt-enable-profile.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)       69 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/nameless-dt-load-project-env.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4784 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/ndt.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     9566 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/ndt_project.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)    12515 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/profile_util.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     2955 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/project_util.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     1536 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/tf_utils.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)    15386 2019-07-25 18:22:15.000000 nameless-deploy-tools-1.99/n_utils/utils.py
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     4179 2019-07-08 13:38:16.000000 nameless-deploy-tools-1.99/n_utils/yuuuu3332111i1l1i.py
+drwxr-xr-x   0 pasi      (1000) pasi      (1000)        0 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      443 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/PKG-INFO
+-rw-r--r--   0 pasi      (1000) pasi      (1000)     5448 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 pasi      (1000) pasi      (1000)        1 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/dependency_links.txt
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      633 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/entry_points.txt
+-rw-r--r--   0 pasi      (1000) pasi      (1000)        1 2019-07-08 13:38:33.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/not-zip-safe
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      180 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/requires.txt
+-rw-r--r--   0 pasi      (1000) pasi      (1000)        8 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/top_level.txt
+-rw-r--r--   0 pasi      (1000) pasi      (1000)      260 2019-09-30 20:33:28.000000 nameless-deploy-tools-1.99/setup.cfg
+-rwxr-xr-x   0 pasi      (1000) pasi      (1000)     2067 2019-09-30 20:33:22.000000 nameless-deploy-tools-1.99/setup.py
```

### Comparing `nameless-deploy-tools-1.98/README.md` & `nameless-deploy-tools-1.99/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # Nameless Deploy Tools
 [![Build Status](https://travis-ci.org/NitorCreations/nameless-deploy-tools.svg?branch=master)](https://travis-ci.org/NitorCreations/nameless-deploy-tools)
 [![Coverage Status](https://coveralls.io/repos/github/NitorCreations/nameless-deploy-tools/badge.svg?branch=master)](https://coveralls.io/github/NitorCreations/nameless-deploy-tools?branch=master)
 
-## Released version 1.98
+## Released version 1.99
 
 Nameless deploy tools are a set of tools to implement a true Infrastructure As Code workflow
 with various cloud infrastructure management tools. Currently supported tools are
 CloudFormation, AWS CDK, Serverless Framework and Terraform.
 
 ## Why Nameless?
```

### Comparing `nameless-deploy-tools-1.98/bin/create-shell-archive.sh` & `nameless-deploy-tools-1.99/bin/create-shell-archive.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/bin/encrypt-and-mount.sh` & `nameless-deploy-tools-1.99/bin/encrypt-and-mount.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/bin/ensure-letsencrypt-certs.sh` & `nameless-deploy-tools-1.99/bin/ensure-letsencrypt-certs.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/bin/lastpass-fetch-notes.sh` & `nameless-deploy-tools-1.99/bin/lastpass-fetch-notes.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/bin/lpssh` & `nameless-deploy-tools-1.99/bin/lpssh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/bin/mount-and-format.sh` & `nameless-deploy-tools-1.99/bin/mount-and-format.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/bin/setup-fetch-secrets.sh` & `nameless-deploy-tools-1.99/bin/setup-fetch-secrets.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/bin/ssh-hostkeys-collect.sh` & `nameless-deploy-tools-1.99/bin/ssh-hostkeys-collect.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/__init__.py` & `nameless-deploy-tools-1.99/n_utils/__init__.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/account_utils.py` & `nameless-deploy-tools-1.99/n_utils/account_utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -42,15 +42,15 @@
         if time() - startTime > timeout and not status == "SUCCEEDED":
             raise Exception("Timed out waiting to create account " + response['CreateAccountStatus']['State'])
         account_id = response['CreateAccountStatus']['AccountId']
 
     os.environ['paramManagedAccount'] = account_id
     os.environ['paramManageRole'] = role_name
     template = find_include("manage-account.yaml")
-    cf_deploy.deploy("managed-account-" + account_name + "-" + account_id, template, region())
+    cf_deploy.deploy("managed-account-" + account_name, template, region())
 
     if trusted_accounts:
         role_arn = "arn:aws:iam::" + account_id + ":role/" + role_name
         assumed_creds = utils.assume_role(role_arn, mfa_token_name=mfa_token)
         sess = session(aws_access_key_id=assumed_creds['AccessKeyId'],
                        aws_secret_access_key=assumed_creds['SecretAccessKey'],
                        aws_session_token=assumed_creds['SessionToken'])
```

### Comparing `nameless-deploy-tools-1.98/n_utils/aws_infra_util.py` & `nameless-deploy-tools-1.99/n_utils/aws_infra_util.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/cf_bootstrap.py` & `nameless-deploy-tools-1.99/n_utils/cf_bootstrap.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/cf_deploy.py` & `nameless-deploy-tools-1.99/n_utils/cf_deploy.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/cli.py` & `nameless-deploy-tools-1.99/n_utils/cli.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/cloudfront_utils.py` & `nameless-deploy-tools-1.99/n_utils/cloudfront_utils.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/ecr_utils.py` & `nameless-deploy-tools-1.99/n_utils/ecr_utils.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/git_utils.py` & `nameless-deploy-tools-1.99/n_utils/git_utils.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/apache_tools.sh` & `nameless-deploy-tools-1.99/n_utils/includes/apache_tools.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/autocomplete-helpers.sh` & `nameless-deploy-tools-1.99/n_utils/includes/autocomplete-helpers.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/aws_tools.sh` & `nameless-deploy-tools-1.99/n_utils/includes/aws_tools.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/bake-docker.sh` & `nameless-deploy-tools-1.99/n_utils/includes/bake-docker.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/bake-image.sh` & `nameless-deploy-tools-1.99/n_utils/includes/bake-image.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/bake-image.yml` & `nameless-deploy-tools-1.99/n_utils/includes/bake-image.yml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/bake-win-image.yml` & `nameless-deploy-tools-1.99/n_utils/includes/bake-win-image.yml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/cloud_init_footer.sh` & `nameless-deploy-tools-1.99/n_utils/includes/cloud_init_footer.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/cloud_init_functions.sh` & `nameless-deploy-tools-1.99/n_utils/includes/cloud_init_functions.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/common_tools.sh` & `nameless-deploy-tools-1.99/n_utils/includes/common_tools.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/bakery-roles.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/bakery-roles.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/generate_jobs.groovy` & `nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/generate_jobs.groovy`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/post_install.sh` & `nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/post_install.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins/userdata.sh` & `nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins/userdata.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/jenkins.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/jenkins.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/network/common.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/network/common.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/creatable-templates/network.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/creatable-templates/network.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/deploy-cdk.sh` & `nameless-deploy-tools-1.99/n_utils/includes/deploy-cdk.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/deploy-serverless.sh` & `nameless-deploy-tools-1.99/n_utils/includes/deploy-serverless.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/deploy-stack.sh` & `nameless-deploy-tools-1.99/n_utils/includes/deploy-stack.sh`

 * *Files 12% similar despite different names*

```diff
@@ -106,13 +106,20 @@
 #If assume-deploy-role.sh is on the path, run it to assume the appropriate role for deployment
 if [ -n "$DEPLOY_ROLE_ARN" ] && [ -z "$AWS_SESSION_TOKEN" ]; then
   eval $(ndt assume-role $DEPLOY_ROLE_ARN)
 elif which assume-deploy-role.sh > /dev/null && [ -z "$AWS_SESSION_TOKEN" ]; then
   eval $(assume-deploy-role.sh)
 fi
 
+cd ${component}/stack-${ORIG_STACK_NAME}
+if [ -x "./pre_deploy.sh" ]; then
+  "./pre_deploy.sh"
+fi
+cd ../..
+
 set -e
 cf-update-stack "${STACK_NAME}" "${component}/stack-${ORIG_STACK_NAME}/template.yaml" "$REGION" $DRY_RUN
 
+cd ${component}/stack-${ORIG_STACK_NAME}
 if [ -x "./post_deploy.sh" ]; then
   "./post_deploy.sh"
 fi
```

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/deploy-terraform.sh` & `nameless-deploy-tools-1.99/n_utils/includes/deploy-terraform.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/disk-by-drive-letter.ps1` & `nameless-deploy-tools-1.99/n_utils/includes/disk-by-drive-letter.ps1`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/ebs-functions.sh` & `nameless-deploy-tools-1.99/n_utils/includes/ebs-functions.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/fetch-secrets-lpass.sh` & `nameless-deploy-tools-1.99/n_utils/includes/fetch-secrets-lpass.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/fetch-secrets-s3.sh` & `nameless-deploy-tools-1.99/n_utils/includes/fetch-secrets-s3.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/fetch-secrets-vault.sh` & `nameless-deploy-tools-1.99/n_utils/includes/fetch-secrets-vault.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/generate_jobs.groovy` & `nameless-deploy-tools-1.99/n_utils/includes/generate_jobs.groovy`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/hook.sh` & `nameless-deploy-tools-1.99/n_utils/includes/hook.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/install_tools.sh` & `nameless-deploy-tools-1.99/n_utils/includes/install_tools.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/jenkins_tools.sh` & `nameless-deploy-tools-1.99/n_utils/includes/jenkins_tools.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/lastpass-login.sh` & `nameless-deploy-tools-1.99/n_utils/includes/lastpass-login.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/lastpass-logout.sh` & `nameless-deploy-tools-1.99/n_utils/includes/lastpass-logout.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/letsencrypt.sh` & `nameless-deploy-tools-1.99/n_utils/includes/letsencrypt.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/lpass_centos_7` & `nameless-deploy-tools-1.99/n_utils/includes/lpass_centos_7`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_14.04` & `nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_14.04`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_16.04` & `nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_16.04`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_16.10` & `nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_16.10`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/lpass_ubuntu_17.04` & `nameless-deploy-tools-1.99/n_utils/includes/lpass_ubuntu_17.04`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/manage-account.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/manage-account.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/nexus_tools.sh` & `nameless-deploy-tools-1.99/n_utils/includes/nexus_tools.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/print-create-instructions.sh` & `nameless-deploy-tools-1.99/n_utils/includes/print-create-instructions.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/ssh_tools.sh` & `nameless-deploy-tools-1.99/n_utils/includes/ssh_tools.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/start-transcript.ps1` & `nameless-deploy-tools-1.99/n_utils/includes/start-transcript.ps1`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/store-secret-lpass.sh` & `nameless-deploy-tools-1.99/n_utils/includes/store-secret-lpass.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/store-secret-s3.sh` & `nameless-deploy-tools-1.99/n_utils/includes/store-secret-s3.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/store-secret-vault.sh` & `nameless-deploy-tools-1.99/n_utils/includes/store-secret-vault.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/apache-sg.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/apache-sg.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/assume-deploy-role.sh` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/assume-deploy-role.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/bootstrap/bakery-roles.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/bootstrap/bakery-roles.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/bootstrap/network.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/bootstrap/network.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/delete-old-snapshots.js` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/delete-old-snapshots.js`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/delete-old-snapshots.min.js` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/delete-old-snapshots.min.js`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/delete-old-snapshots.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/delete-old-snapshots.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/external-lambdarole-policy.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/external-lambdarole-policy.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/instanceprofile.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/instanceprofile.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/internal-lambdarole-policy.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/internal-lambdarole-policy.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/nexus-userdata.sh` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/nexus-userdata.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_baking.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_baking.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_cloud_init.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_cloud_init.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_ec2_allow_volume_ops.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_ec2_allow_volume_ops.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_ec2_associate_address.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_ec2_associate_address.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_invoke_lambda.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_invoke_lambda.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policy_s3_secure_download.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policy_s3_secure_download.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/policydoc_assumerole.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/policydoc_assumerole.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/role_bake.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/role_bake.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/route53.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/route53.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/sg_bake.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/sg_bake.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/template-snippets/sg_win_bake.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/template-snippets/sg_win_bake.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/terraform-pull-state.sh` & `nameless-deploy-tools-1.99/n_utils/includes/terraform-pull-state.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/tool_installers.sh` & `nameless-deploy-tools-1.99/n_utils/includes/tool_installers.sh`

 * *Files 2% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 # Functions to install various tools meant to be sourced and used as Functions
 if [ -z "$DEPLOYTOOLS_VERSION" ]; then
   if [ -n "${CF_paramDeployToolsVersion}" ]; then
     DEPLOYTOOLS_VERSION="${CF_paramDeployToolsVersion}"
   fi
 fi
 if [ -z "$MAVEN_VERSION" ]; then
-  MAVEN_VERSION=3.3.9
+  MAVEN_VERSION=3.6.2
 fi
 if [ -z "$PHANTOMJS_VERSION" ]; then
   PHANTOMJS_VERSION=2.1.1
 fi
 if [ -z "$NEXUS_VERSION" ]; then
   NEXUS_VERSION=2.12.0-01
 fi
@@ -52,15 +52,15 @@
 install_cftools() {
   curl -s https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz | tar -xzvf -
   cd aws-cfn-bootstrap-*
   pip install .
   cd ..
 }
 install_maven() {
-  wget -O - http://mirror.netinch.com/pub/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar -xzvf - -C /opt/
+  wget -O - https://www-eu.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar -xzvf - -C /opt/
   ln -snf /opt/apache-maven-$MAVEN_VERSION /opt/maven
   ln -snf  /opt/maven/bin/mvn /usr/bin/mvn
 }
 install_nexus() {
   wget -O - https://sonatype-download.global.ssl.fastly.net/nexus/oss/nexus-$NEXUS_VERSION-bundle.tar.gz | tar -xzf - -C /opt/nexus
   chown -R nexus:nexus /opt/nexus
   ln -snf /opt/nexus/nexus-* /opt/nexus/current
```

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/trust-account-role.yaml` & `nameless-deploy-tools-1.99/n_utils/includes/trust-account-role.yaml`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/undeploy-cdk.sh` & `nameless-deploy-tools-1.99/n_utils/includes/undeploy-cdk.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/undeploy-serverless.sh` & `nameless-deploy-tools-1.99/n_utils/includes/undeploy-serverless.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/undeploy-stack.sh` & `nameless-deploy-tools-1.99/n_utils/includes/undeploy-stack.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/includes/undeploy-terraform.sh` & `nameless-deploy-tools-1.99/n_utils/includes/undeploy-terraform.sh`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/log_events.py` & `nameless-deploy-tools-1.99/n_utils/log_events.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/maven_utils.py` & `nameless-deploy-tools-1.99/n_utils/maven_utils.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/mfa_utils.py` & `nameless-deploy-tools-1.99/n_utils/mfa_utils.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/ndt.py` & `nameless-deploy-tools-1.99/n_utils/ndt.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/ndt_project.py` & `nameless-deploy-tools-1.99/n_utils/ndt_project.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/profile_util.py` & `nameless-deploy-tools-1.99/n_utils/profile_util.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/project_util.py` & `nameless-deploy-tools-1.99/n_utils/project_util.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/tf_utils.py` & `nameless-deploy-tools-1.99/n_utils/tf_utils.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/utils.py` & `nameless-deploy-tools-1.99/n_utils/utils.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/n_utils/yuuuu3332111i1l1i.py` & `nameless-deploy-tools-1.99/n_utils/yuuuu3332111i1l1i.py`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/SOURCES.txt` & `nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/nameless_deploy_tools.egg-info/entry_points.txt` & `nameless-deploy-tools-1.99/nameless_deploy_tools.egg-info/entry_points.txt`

 * *Files identical despite different names*

### Comparing `nameless-deploy-tools-1.98/setup.py` & `nameless-deploy-tools-1.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,18 +12,18 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 import sys
 from setuptools import setup
 from n_utils import PATH_COMMANDS, CONSOLESCRIPTS
 
 setup(name='nameless-deploy-tools',
-      version='1.98',
+      version='1.99',
       description='Tools for deploying to AWS via CloudFormation and Serverless framework that support a pull request based workflow',
       url='http://github.com/NitorCreations/nameless-deploy-tools',
-      download_url='https://github.com/NitorCreations/nameless-deploy-tools/tarball/1.98',
+      download_url='https://github.com/NitorCreations/nameless-deploy-tools/tarball/1.99',
       author='Pasi Niemi',
       author_email='pasi@nitor.com',
       license='Apache 2.0',
       packages=['n_utils'],
       include_package_data=True,
       scripts=PATH_COMMANDS,
       entry_points={
```

