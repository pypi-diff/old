# Comparing `tmp/bbot-1.0.5.1547rc0.tar.gz` & `tmp/bbot-1.0.5.1555rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bbot-1.0.5.1547rc0.tar", max compression
+gzip compressed data, was "bbot-1.0.5.1555rc0.tar", max compression
```

## Comparing `bbot-1.0.5.1547rc0.tar` & `bbot-1.0.5.1555rc0.tar`

### file list

```diff
@@ -1,182 +1,182 @@
--rw-r--r--   0        0        0    32473 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/LICENSE
--rw-r--r--   0        0        0    51009 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/README.md
--rw-r--r--   0        0        0      211 2023-04-06 03:38:45.423081 bbot-1.0.5.1547rc0/bbot/__init__.py
--rw-r--r--   0        0        0       25 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/agent/__init__.py
--rw-r--r--   0        0        0     6478 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/agent/agent.py
--rw-r--r--   0        0        0      376 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/agent/messages.py
--rwxr-xr-x   0        0        0    13387 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/cli.py
--rw-r--r--   0        0        0        0 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/__init__.py
--rw-r--r--   0        0        0     3222 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/configurator/__init__.py
--rw-r--r--   0        0        0     8919 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/configurator/args.py
--rw-r--r--   0        0        0     4261 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/configurator/environ.py
--rw-r--r--   0        0        0     1170 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/configurator/files.py
--rw-r--r--   0        0        0      632 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/errors.py
--rw-r--r--   0        0        0      104 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/event/__init__.py
--rw-r--r--   0        0        0    29858 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/event/base.py
--rw-r--r--   0        0        0     1498 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/event/helpers.py
--rw-r--r--   0        0        0       61 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/__init__.py
--rw-r--r--   0        0        0     3644 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cache.py
--rw-r--r--   0        0        0     1256 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/__init__.py
--rw-r--r--   0        0        0      565 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/aws.py
--rw-r--r--   0        0        0      716 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/azure.py
--rw-r--r--   0        0        0     2875 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/base.py
--rw-r--r--   0        0        0      297 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/digitalocean.py
--rw-r--r--   0        0        0      271 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/firebase.py
--rw-r--r--   0        0        0      352 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/gcp.py
--rw-r--r--   0        0        0     7432 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/command.py
--rw-r--r--   0        0        0       37 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/depsinstaller/__init__.py
--rw-r--r--   0        0        0    13841 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/depsinstaller/installer.py
--rw-r--r--   0        0        0       87 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/depsinstaller/sudo_askpass.py
--rw-r--r--   0        0        0     8540 2023-04-06 03:38:18.038997 bbot-1.0.5.1547rc0/bbot/core/helpers/diff.py
--rw-r--r--   0        0        0    29297 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/dns.py
--rw-r--r--   0        0        0     4146 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/helper.py
--rw-r--r--   0        0        0     5364 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/interactsh.py
--rw-r--r--   0        0        0     1414 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/logger.py
--rw-r--r--   0        0        0    28145 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/misc.py
--rw-r--r--   0        0        0    14848 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/modules.py
--rw-r--r--   0        0        0     9506 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/names_generator.py
--rw-r--r--   0        0        0     2578 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/ntlm.py
--rw-r--r--   0        0        0      795 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/punycode.py
--rw-r--r--   0        0        0     2919 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/queueing.py
--rw-r--r--   0        0        0     1890 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/regexes.py
--rw-r--r--   0        0        0     8092 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/threadpool.py
--rw-r--r--   0        0        0     3987 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/url.py
--rw-r--r--   0        0        0     3102 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/validators.py
--rw-r--r--   0        0        0     9324 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/web.py
--rw-r--r--   0        0        0    10675 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/helpers/wordcloud.py
--rw-r--r--   0        0        0       99 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/logger/__init__.py
--rw-r--r--   0        0        0     7859 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/core/logger/logger.py
--rw-r--r--   0        0        0     2091 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/db/neo4j.py
--rw-r--r--   0        0        0     3637 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/defaults.yml
--rw-r--r--   0        0        0      396 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/__init__.py
--rw-r--r--   0        0        0     1371 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/anubisdb.py
--rw-r--r--   0        0        0     3461 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/azure_tenant.py
--rw-r--r--   0        0        0     2350 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/badsecrets.py
--rw-r--r--   0        0        0    24937 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/base.py
--rw-r--r--   0        0        0     2197 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/bevigil.py
--rw-r--r--   0        0        0     1225 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/binaryedge.py
--rw-r--r--   0        0        0     5502 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/bucket_aws.py
--rw-r--r--   0        0        0     1065 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/bucket_azure.py
--rw-r--r--   0        0        0      847 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/bucket_digitalocean.py
--rw-r--r--   0        0        0     1167 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/bucket_firebase.py
--rw-r--r--   0        0        0     2169 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/bucket_gcp.py
--rw-r--r--   0        0        0     4550 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/builtwith.py
--rw-r--r--   0        0        0     5107 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/bypass403.py
--rw-r--r--   0        0        0     1116 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/c99.py
--rw-r--r--   0        0        0     5432 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/censys.py
--rw-r--r--   0        0        0      732 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/certspotter.py
--rw-r--r--   0        0        0     4526 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/crobat.py
--rw-r--r--   0        0        0     1165 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/crt.py
--rw-r--r--   0        0        0    13578 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/deadly/ffuf.py
--rw-r--r--   0        0        0    15204 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/deadly/nuclei.py
--rw-r--r--   0        0        0     5763 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/deadly/vhost.py
--rw-r--r--   0        0        0     2516 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/dnscommonsrv.py
--rw-r--r--   0        0        0     2954 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/dnsdumpster.py
--rw-r--r--   0        0        0     2862 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/dnszonetransfer.py
--rw-r--r--   0        0        0      866 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/emailformat.py
--rw-r--r--   0        0        0    11007 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/ffuf_shortnames.py
--rw-r--r--   0        0        0     2164 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/fingerprintx.py
--rw-r--r--   0        0        0     1093 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/fullhunt.py
--rw-r--r--   0        0        0     7290 2023-04-06 03:38:18.042997 bbot-1.0.5.1547rc0/bbot/modules/generic_ssrf.py
--rw-r--r--   0        0        0     2723 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/github.py
--rw-r--r--   0        0        0    10060 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/gowitness.py
--rw-r--r--   0        0        0      658 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/hackertarget.py
--rw-r--r--   0        0        0     7395 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/host_header.py
--rw-r--r--   0        0        0     5491 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/httpx.py
--rw-r--r--   0        0        0     7748 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/hunt.py
--rw-r--r--   0        0        0     1944 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/hunterio.py
--rw-r--r--   0        0        0     9336 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/iis_shortnames.py
--rw-r--r--   0        0        0        0 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/internal/__init__.py
--rw-r--r--   0        0        0      311 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/internal/aggregate.py
--rw-r--r--   0        0        0      578 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/internal/base.py
--rw-r--r--   0        0        0    14125 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/internal/excavate.py
--rw-r--r--   0        0        0     4481 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/internal/speculate.py
--rw-r--r--   0        0        0     1274 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/ipneighbor.py
--rw-r--r--   0        0        0     2037 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/ipstack.py
--rw-r--r--   0        0        0      707 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/leakix.py
--rw-r--r--   0        0        0    10777 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/masscan.py
--rw-r--r--   0        0        0    12443 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/massdns.py
--rw-r--r--   0        0        0     4012 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/naabu.py
--rw-r--r--   0        0        0     4867 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/ntlm.py
--rw-r--r--   0        0        0      728 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/otx.py
--rw-r--r--   0        0        0        0 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/__init__.py
--rw-r--r--   0        0        0     3561 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/asset_inventory.py
--rw-r--r--   0        0        0     1379 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/base.py
--rw-r--r--   0        0        0     1737 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/csv.py
--rw-r--r--   0        0        0     1809 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/http.py
--rw-r--r--   0        0        0     1787 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/human.py
--rw-r--r--   0        0        0     1007 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/json.py
--rw-r--r--   0        0        0     1255 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/neo4j.py
--rw-r--r--   0        0        0      204 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/python.py
--rw-r--r--   0        0        0     3609 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/web_report.py
--rw-r--r--   0        0        0     1747 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/output/websocket.py
--rw-r--r--   0        0        0     1532 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/paramminer_cookies.py
--rw-r--r--   0        0        0     1620 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/paramminer_getparams.py
--rw-r--r--   0        0        0     5360 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/paramminer_headers.py
--rw-r--r--   0        0        0     1533 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/passivetotal.py
--rw-r--r--   0        0        0     1310 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/pgp.py
--rw-r--r--   0        0        0      746 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/rapiddns.py
--rw-r--r--   0        0        0     1606 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/report/affiliates.py
--rw-r--r--   0        0        0     8304 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/report/asn.py
--rw-r--r--   0        0        0      105 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/report/base.py
--rw-r--r--   0        0        0      742 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/riddler.py
--rw-r--r--   0        0        0     2080 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/robots.py
--rw-r--r--   0        0        0     2578 2023-04-06 03:38:18.046997 bbot-1.0.5.1547rc0/bbot/modules/secretsdb.py
--rw-r--r--   0        0        0     1071 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/securitytrails.py
--rw-r--r--   0        0        0     1198 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/shodan_dns.py
--rw-r--r--   0        0        0     1432 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/skymem.py
--rw-r--r--   0        0        0     1607 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/smuggler.py
--rw-r--r--   0        0        0     1527 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/social.py
--rw-r--r--   0        0        0     8014 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/sslcert.py
--rw-r--r--   0        0        0     5752 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/subdomain_hijack.py
--rw-r--r--   0        0        0      507 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/sublist3r.py
--rw-r--r--   0        0        0    11271 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/telerik.py
--rw-r--r--   0        0        0      566 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/threatminer.py
--rw-r--r--   0        0        0     3819 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/url_manipulation.py
--rw-r--r--   0        0        0     2759 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/urlscan.py
--rw-r--r--   0        0        0     2458 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/viewdns.py
--rw-r--r--   0        0        0     1158 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/virustotal.py
--rw-r--r--   0        0        0     1569 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/wafw00f.py
--rw-r--r--   0        0        0     1169 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/wappalyzer.py
--rw-r--r--   0        0        0     2190 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/wayback.py
--rw-r--r--   0        0        0     2095 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/modules/zoomeye.py
--rw-r--r--   0        0        0       29 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/scanner/__init__.py
--rw-r--r--   0        0        0      427 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/scanner/dispatcher.py
--rw-r--r--   0        0        0    25196 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/scanner/manager.py
--rw-r--r--   0        0        0    22025 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/scanner/scanner.py
--rw-r--r--   0        0        0     3251 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/scanner/stats.py
--rw-r--r--   0        0        0     3723 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/scanner/target.py
--rw-r--r--   0        0        0        0 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/__init__.py
--rw-r--r--   0        0        0    18609 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/bbot_fixtures.py
--rw-r--r--   0        0        0      559 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/conftest.py
--rw-r--r--   0        0        0     2591 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/helpers.py
--rw-r--r--   0        0        0    70859 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/modules_test_classes.py
--rw-r--r--   0        0        0       15 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/pytest.ini
--rwxr-xr-x   0        0        0      578 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/run_tests.sh
--rw-r--r--   0        0        0      904 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test.conf
--rw-r--r--   0        0        0      322 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_output.json
--rw-r--r--   0        0        0        0 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_1/__init__.py
--rw-r--r--   0        0        0     1397 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_1/test_before_patching.py
--rw-r--r--   0        0        0     5669 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_1/test_modules_full.py
--rw-r--r--   0        0        0        0 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/__init__.py
--rw-r--r--   0        0        0      588 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_agent.py
--rw-r--r--   0        0        0     4012 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_cli.py
--rw-r--r--   0        0        0      932 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_cloud_helpers.py
--rw-r--r--   0        0        0      462 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_config.py
--rw-r--r--   0        0        0      722 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_depsinstaller.py
--rw-r--r--   0        0        0    15064 2023-04-06 03:38:18.050997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_events.py
--rw-r--r--   0        0        0    34666 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_helpers.py
--rw-r--r--   0        0        0     7171 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_manager.py
--rw-r--r--   0        0        0    11466 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_modules_basic.py
--rw-r--r--   0        0        0      789 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_python_api.py
--rw-r--r--   0        0        0     3215 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_scan.py
--rw-r--r--   0        0        0     1395 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_scope.py
--rw-r--r--   0        0        0     2163 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_target.py
--rw-r--r--   0        0        0      707 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_threadpool.py
--rw-r--r--   0        0        0      479 2023-04-06 03:38:18.054997 bbot-1.0.5.1547rc0/bbot/wordlists/devops_mutations.txt
--rw-r--r--   0        0        0   959424 2023-04-06 03:38:18.062997 bbot-1.0.5.1547rc0/bbot/wordlists/ffuf_shortname_candidates.txt
--rw-r--r--   0        0        0    32226 2023-04-06 03:38:18.062997 bbot-1.0.5.1547rc0/bbot/wordlists/nameservers.txt
--rw-r--r--   0        0        0     6068 2023-04-06 03:38:18.062997 bbot-1.0.5.1547rc0/bbot/wordlists/raft-small-extensions-lowercase_CLEANED.txt
--rw-r--r--   0        0        0   570241 2023-04-06 03:38:18.062997 bbot-1.0.5.1547rc0/bbot/wordlists/wordninja_dns.txt.gz
--rw-r--r--   0        0        0     1358 2023-04-06 03:38:45.423081 bbot-1.0.5.1547rc0/pyproject.toml
--rw-r--r--   0        0        0    52328 1970-01-01 00:00:00.000000 bbot-1.0.5.1547rc0/PKG-INFO
+-rw-r--r--   0        0        0    32473 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/LICENSE
+-rw-r--r--   0        0        0    51011 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/README.md
+-rw-r--r--   0        0        0      211 2023-04-06 17:31:06.204552 bbot-1.0.5.1555rc0/bbot/__init__.py
+-rw-r--r--   0        0        0       25 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/agent/__init__.py
+-rw-r--r--   0        0        0     6478 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/agent/agent.py
+-rw-r--r--   0        0        0      376 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/agent/messages.py
+-rwxr-xr-x   0        0        0    13323 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/cli.py
+-rw-r--r--   0        0        0       93 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/__init__.py
+-rw-r--r--   0        0        0     3137 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/configurator/__init__.py
+-rw-r--r--   0        0        0     8919 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/configurator/args.py
+-rw-r--r--   0        0        0     4261 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/configurator/environ.py
+-rw-r--r--   0        0        0     1170 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/configurator/files.py
+-rw-r--r--   0        0        0      632 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/errors.py
+-rw-r--r--   0        0        0      104 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/event/__init__.py
+-rw-r--r--   0        0        0    29858 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/event/base.py
+-rw-r--r--   0        0        0     1498 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/event/helpers.py
+-rw-r--r--   0        0        0       61 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/__init__.py
+-rw-r--r--   0        0        0     3644 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cache.py
+-rw-r--r--   0        0        0     1256 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/__init__.py
+-rw-r--r--   0        0        0      565 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/aws.py
+-rw-r--r--   0        0        0      716 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/azure.py
+-rw-r--r--   0        0        0     2875 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/base.py
+-rw-r--r--   0        0        0      297 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/digitalocean.py
+-rw-r--r--   0        0        0      271 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/firebase.py
+-rw-r--r--   0        0        0      352 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/gcp.py
+-rw-r--r--   0        0        0     7432 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/command.py
+-rw-r--r--   0        0        0       37 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/depsinstaller/__init__.py
+-rw-r--r--   0        0        0    13841 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/depsinstaller/installer.py
+-rw-r--r--   0        0        0       87 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/depsinstaller/sudo_askpass.py
+-rw-r--r--   0        0        0     8540 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/diff.py
+-rw-r--r--   0        0        0    29297 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/dns.py
+-rw-r--r--   0        0        0     4146 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/helper.py
+-rw-r--r--   0        0        0     5364 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/interactsh.py
+-rw-r--r--   0        0        0     1414 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/logger.py
+-rw-r--r--   0        0        0    28093 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/misc.py
+-rw-r--r--   0        0        0    14848 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/modules.py
+-rw-r--r--   0        0        0     9514 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/names_generator.py
+-rw-r--r--   0        0        0     2578 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/ntlm.py
+-rw-r--r--   0        0        0      795 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/punycode.py
+-rw-r--r--   0        0        0     2919 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/queueing.py
+-rw-r--r--   0        0        0     1890 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/regexes.py
+-rw-r--r--   0        0        0     8092 2023-04-06 17:30:43.100583 bbot-1.0.5.1555rc0/bbot/core/helpers/threadpool.py
+-rw-r--r--   0        0        0     3987 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/core/helpers/url.py
+-rw-r--r--   0        0        0     3102 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/core/helpers/validators.py
+-rw-r--r--   0        0        0     9324 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/core/helpers/web.py
+-rw-r--r--   0        0        0    10695 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/core/helpers/wordcloud.py
+-rw-r--r--   0        0        0       99 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/core/logger/__init__.py
+-rw-r--r--   0        0        0     7859 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/core/logger/logger.py
+-rw-r--r--   0        0        0     2091 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/db/neo4j.py
+-rw-r--r--   0        0        0     3637 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/defaults.yml
+-rw-r--r--   0        0        0      396 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/__init__.py
+-rw-r--r--   0        0        0     1371 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/anubisdb.py
+-rw-r--r--   0        0        0     3461 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/azure_tenant.py
+-rw-r--r--   0        0        0     2350 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/badsecrets.py
+-rw-r--r--   0        0        0    25405 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/base.py
+-rw-r--r--   0        0        0     2197 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/bevigil.py
+-rw-r--r--   0        0        0     1225 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/binaryedge.py
+-rw-r--r--   0        0        0     5502 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/bucket_aws.py
+-rw-r--r--   0        0        0     1065 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/bucket_azure.py
+-rw-r--r--   0        0        0      847 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/bucket_digitalocean.py
+-rw-r--r--   0        0        0     1167 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/bucket_firebase.py
+-rw-r--r--   0        0        0     2169 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/bucket_gcp.py
+-rw-r--r--   0        0        0     4550 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/builtwith.py
+-rw-r--r--   0        0        0     5107 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/bypass403.py
+-rw-r--r--   0        0        0     1116 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/c99.py
+-rw-r--r--   0        0        0     5432 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/censys.py
+-rw-r--r--   0        0        0      732 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/certspotter.py
+-rw-r--r--   0        0        0     4526 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/crobat.py
+-rw-r--r--   0        0        0     1165 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/crt.py
+-rw-r--r--   0        0        0    13578 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/deadly/ffuf.py
+-rw-r--r--   0        0        0    15204 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/deadly/nuclei.py
+-rw-r--r--   0        0        0     5763 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/deadly/vhost.py
+-rw-r--r--   0        0        0     2516 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/dnscommonsrv.py
+-rw-r--r--   0        0        0     2954 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/dnsdumpster.py
+-rw-r--r--   0        0        0     2862 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/dnszonetransfer.py
+-rw-r--r--   0        0        0      866 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/emailformat.py
+-rw-r--r--   0        0        0    11007 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/ffuf_shortnames.py
+-rw-r--r--   0        0        0     2164 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/fingerprintx.py
+-rw-r--r--   0        0        0     1093 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/fullhunt.py
+-rw-r--r--   0        0        0     7290 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/generic_ssrf.py
+-rw-r--r--   0        0        0     2723 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/github.py
+-rw-r--r--   0        0        0    10060 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/gowitness.py
+-rw-r--r--   0        0        0      658 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/hackertarget.py
+-rw-r--r--   0        0        0     7395 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/host_header.py
+-rw-r--r--   0        0        0     5491 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/httpx.py
+-rw-r--r--   0        0        0     7748 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/hunt.py
+-rw-r--r--   0        0        0     1944 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/hunterio.py
+-rw-r--r--   0        0        0     9336 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/iis_shortnames.py
+-rw-r--r--   0        0        0        0 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/internal/__init__.py
+-rw-r--r--   0        0        0      311 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/internal/aggregate.py
+-rw-r--r--   0        0        0      578 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/internal/base.py
+-rw-r--r--   0        0        0    14125 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/internal/excavate.py
+-rw-r--r--   0        0        0     4481 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/internal/speculate.py
+-rw-r--r--   0        0        0     1274 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/ipneighbor.py
+-rw-r--r--   0        0        0     2037 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/ipstack.py
+-rw-r--r--   0        0        0      707 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/leakix.py
+-rw-r--r--   0        0        0    10777 2023-04-06 17:30:43.104584 bbot-1.0.5.1555rc0/bbot/modules/masscan.py
+-rw-r--r--   0        0        0    12554 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/massdns.py
+-rw-r--r--   0        0        0     4012 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/naabu.py
+-rw-r--r--   0        0        0     4867 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/ntlm.py
+-rw-r--r--   0        0        0      728 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/otx.py
+-rw-r--r--   0        0        0        0 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/__init__.py
+-rw-r--r--   0        0        0     3561 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/asset_inventory.py
+-rw-r--r--   0        0        0     1379 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/base.py
+-rw-r--r--   0        0        0     1737 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/csv.py
+-rw-r--r--   0        0        0     1809 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/http.py
+-rw-r--r--   0        0        0     1787 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/human.py
+-rw-r--r--   0        0        0     1007 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/json.py
+-rw-r--r--   0        0        0     1255 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/neo4j.py
+-rw-r--r--   0        0        0      204 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/python.py
+-rw-r--r--   0        0        0     3609 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/web_report.py
+-rw-r--r--   0        0        0     1747 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/output/websocket.py
+-rw-r--r--   0        0        0     1532 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/paramminer_cookies.py
+-rw-r--r--   0        0        0     1620 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/paramminer_getparams.py
+-rw-r--r--   0        0        0     5360 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/paramminer_headers.py
+-rw-r--r--   0        0        0     1533 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/passivetotal.py
+-rw-r--r--   0        0        0     1310 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/pgp.py
+-rw-r--r--   0        0        0      746 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/rapiddns.py
+-rw-r--r--   0        0        0     1606 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/report/affiliates.py
+-rw-r--r--   0        0        0     8304 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/report/asn.py
+-rw-r--r--   0        0        0      105 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/report/base.py
+-rw-r--r--   0        0        0      742 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/riddler.py
+-rw-r--r--   0        0        0     2080 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/robots.py
+-rw-r--r--   0        0        0     2578 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/secretsdb.py
+-rw-r--r--   0        0        0     1071 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/securitytrails.py
+-rw-r--r--   0        0        0     1198 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/shodan_dns.py
+-rw-r--r--   0        0        0     1432 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/skymem.py
+-rw-r--r--   0        0        0     1607 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/smuggler.py
+-rw-r--r--   0        0        0     1527 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/social.py
+-rw-r--r--   0        0        0     8014 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/sslcert.py
+-rw-r--r--   0        0        0     5752 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/subdomain_hijack.py
+-rw-r--r--   0        0        0      507 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/sublist3r.py
+-rw-r--r--   0        0        0    11271 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/telerik.py
+-rw-r--r--   0        0        0      566 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/threatminer.py
+-rw-r--r--   0        0        0     3819 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/url_manipulation.py
+-rw-r--r--   0        0        0     2759 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/urlscan.py
+-rw-r--r--   0        0        0     2458 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/viewdns.py
+-rw-r--r--   0        0        0     1158 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/virustotal.py
+-rw-r--r--   0        0        0     1569 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/wafw00f.py
+-rw-r--r--   0        0        0     1169 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/wappalyzer.py
+-rw-r--r--   0        0        0     2190 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/wayback.py
+-rw-r--r--   0        0        0     2095 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/modules/zoomeye.py
+-rw-r--r--   0        0        0       29 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/scanner/__init__.py
+-rw-r--r--   0        0        0      427 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/scanner/dispatcher.py
+-rw-r--r--   0        0        0    25262 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/scanner/manager.py
+-rw-r--r--   0        0        0    22025 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/scanner/scanner.py
+-rw-r--r--   0        0        0     3251 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/scanner/stats.py
+-rw-r--r--   0        0        0     3723 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/scanner/target.py
+-rw-r--r--   0        0        0        0 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/test/__init__.py
+-rw-r--r--   0        0        0    18609 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/test/bbot_fixtures.py
+-rw-r--r--   0        0        0      559 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/test/conftest.py
+-rw-r--r--   0        0        0     2591 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/test/helpers.py
+-rw-r--r--   0        0        0    70817 2023-04-06 17:30:43.108584 bbot-1.0.5.1555rc0/bbot/test/modules_test_classes.py
+-rw-r--r--   0        0        0       15 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/pytest.ini
+-rwxr-xr-x   0        0        0      578 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/run_tests.sh
+-rw-r--r--   0        0        0      904 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test.conf
+-rw-r--r--   0        0        0      322 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_output.json
+-rw-r--r--   0        0        0        0 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_1/__init__.py
+-rw-r--r--   0        0        0     1397 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_1/test_before_patching.py
+-rw-r--r--   0        0        0     5669 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_1/test_modules_full.py
+-rw-r--r--   0        0        0        0 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/__init__.py
+-rw-r--r--   0        0        0      588 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_agent.py
+-rw-r--r--   0        0        0     4012 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_cli.py
+-rw-r--r--   0        0        0      932 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_cloud_helpers.py
+-rw-r--r--   0        0        0      462 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_config.py
+-rw-r--r--   0        0        0      722 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_depsinstaller.py
+-rw-r--r--   0        0        0    15064 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_events.py
+-rw-r--r--   0        0        0    34925 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_helpers.py
+-rw-r--r--   0        0        0     7171 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_manager.py
+-rw-r--r--   0        0        0    11466 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_modules_basic.py
+-rw-r--r--   0        0        0      789 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_python_api.py
+-rw-r--r--   0        0        0     3215 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_scan.py
+-rw-r--r--   0        0        0     1395 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_scope.py
+-rw-r--r--   0        0        0     2163 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_target.py
+-rw-r--r--   0        0        0      707 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_threadpool.py
+-rw-r--r--   0        0        0      479 2023-04-06 17:30:43.112583 bbot-1.0.5.1555rc0/bbot/wordlists/devops_mutations.txt
+-rw-r--r--   0        0        0   959424 2023-04-06 17:30:43.120583 bbot-1.0.5.1555rc0/bbot/wordlists/ffuf_shortname_candidates.txt
+-rw-r--r--   0        0        0    32226 2023-04-06 17:30:43.120583 bbot-1.0.5.1555rc0/bbot/wordlists/nameservers.txt
+-rw-r--r--   0        0        0     6068 2023-04-06 17:30:43.120583 bbot-1.0.5.1555rc0/bbot/wordlists/raft-small-extensions-lowercase_CLEANED.txt
+-rw-r--r--   0        0        0   570241 2023-04-06 17:30:43.120583 bbot-1.0.5.1555rc0/bbot/wordlists/wordninja_dns.txt.gz
+-rw-r--r--   0        0        0     1338 2023-04-06 17:31:06.204552 bbot-1.0.5.1555rc0/pyproject.toml
+-rw-r--r--   0        0        0    52289 1970-01-01 00:00:00.000000 bbot-1.0.5.1555rc0/PKG-INFO
```

### Comparing `bbot-1.0.5.1547rc0/LICENSE` & `bbot-1.0.5.1555rc0/LICENSE`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/README.md` & `bbot-1.0.5.1555rc0/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 
 # bleeding edge (dev branch)
 pip install --pre bbot
 
 bbot --help
 ~~~
 Prerequisites:
-- Linux (Windows, including WSL is not supported)
+- Linux (Windows and macOS are *not* supported)
 - Python 3.9 or newer
 
 ## Installation ([Docker](https://hub.docker.com/r/blacklanternsecurity/bbot))
 ~~~bash
 # bleeding edge (dev)
 docker run -it blacklanternsecurity/bbot --help
 
@@ -106,15 +106,15 @@
 Visit the wiki for more [tips and tricks](https://github.com/blacklanternsecurity/bbot/wiki#tips-and-tricks).
 
 ## Using BBOT as a Python library
 ~~~python
 from bbot.scanner import Scanner
 
 # any number of targets can be specified
-scan = Scanner("evilcorp.com", "1.2.3.0/24", modules=["httpx", "sslcert"])
+scan = Scanner("evilcorp.com", "evilcorp.co.uk", modules=["httpx", "sslcert"])
 for event in scan.start():
     print(event.json())
 ~~~
 
 # Output
 By default, BBOT saves its output in TXT, JSON, and CSV formats. To enable more output modules, you can use `--output-module`.
 ~~~bash
```

### Comparing `bbot-1.0.5.1547rc0/bbot/agent/agent.py` & `bbot-1.0.5.1555rc0/bbot/agent/agent.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/cli.py` & `bbot-1.0.5.1555rc0/bbot/cli.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,17 +8,15 @@
 from omegaconf import OmegaConf
 from contextlib import suppress
 
 # fix tee buffering
 sys.stdout.reconfigure(line_buffering=True)
 
 # logging
-from bbot.core.logger import init_logging, get_log_level, toggle_log_level
-
-logging_queue, logging_handlers = init_logging()
+from bbot.core.logger import get_log_level, toggle_log_level
 
 import bbot.core.errors
 from bbot import __version__
 from bbot.modules import module_loader
 from bbot.core.configurator.args import parser
 from bbot.core.helpers.logger import log_to_stderr
 from bbot.core.configurator import ensure_config_files, check_cli_args
```

### Comparing `bbot-1.0.5.1547rc0/bbot/core/configurator/__init__.py` & `bbot-1.0.5.1555rc0/bbot/core/configurator/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from pathlib import Path
 from omegaconf import OmegaConf
 
 from . import files, args, environ
 from ..errors import ConfigLoadError
 from ...modules import module_loader
 from ..helpers.logger import log_to_stderr
-from ..helpers.misc import mkdir, error_and_exit, filter_dict, clean_dict, closest_match, match_and_exit
+from ..helpers.misc import error_and_exit, filter_dict, clean_dict, match_and_exit
 
 # cached sudo password
 bbot_sudo_pass = None
 
 modules_config = OmegaConf.create(
     {
         "modules": module_loader.configs(type="scan"),
@@ -49,15 +49,14 @@
                 from ...modules import module_loader
 
                 modules_options = set()
                 for module_options in module_loader.modules_options().values():
                     modules_options.update(set(o[0] for o in module_options))
                 global_options = set(default_config.keys()) - {"modules", "output_modules"}
                 all_options = global_options.union(modules_options)
-                closest, score = closest_match(c, all_options)
                 match_and_exit(c, all_options, msg="module option")
 
 
 def ensure_config_files():
     secrets_strings = ["api_key", "username", "password", "token", "secret", "_id"]
     exclude_keys = ["modules", "output_modules", "internal_modules"]
```

### Comparing `bbot-1.0.5.1547rc0/bbot/core/configurator/args.py` & `bbot-1.0.5.1555rc0/bbot/core/configurator/args.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/configurator/environ.py` & `bbot-1.0.5.1555rc0/bbot/core/configurator/environ.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/configurator/files.py` & `bbot-1.0.5.1555rc0/bbot/core/configurator/files.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/errors.py` & `bbot-1.0.5.1555rc0/bbot/core/errors.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/event/base.py` & `bbot-1.0.5.1555rc0/bbot/core/event/base.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/event/helpers.py` & `bbot-1.0.5.1555rc0/bbot/core/event/helpers.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/cache.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/cache.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/__init__.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/__init__.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/aws.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/aws.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/azure.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/azure.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/cloud/base.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/cloud/base.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/command.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/command.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/depsinstaller/installer.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/depsinstaller/installer.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/diff.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/diff.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/dns.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/dns.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/helper.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/helper.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/interactsh.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/interactsh.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/logger.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/logger.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/misc.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/misc.py`

 * *Files 1% similar despite different names*

```diff
@@ -6,28 +6,28 @@
 import atexit
 import codecs
 import psutil
 import random
 import shutil
 import signal
 import string
+import difflib
 import inspect
 import logging
 import platform
 import ipaddress
 
 import traceback
 import subprocess as sp
 from pathlib import Path
 from itertools import islice
 from datetime import datetime
 from tabulate import tabulate
 import wordninja as _wordninja
 from contextlib import suppress
-from strsimpy.qgram import QGram
 import tldextract as _tldextract
 from hashlib import sha1 as hashlib_sha1
 from urllib.parse import urlparse, quote, unquote, urlunparse  # noqa F401
 
 from .url import *  # noqa F401
 from . import regexes
 from .. import errors
@@ -383,38 +383,38 @@
         if acronyms:
             if len(subwords) > 1:
                 words.add("".join([c[0] for c in subwords if len(c) > 0]))
 
     return words
 
 
-def closest_match(s, choices, n=1):
+def closest_match(s, choices, n=1, cutoff=0.0):
     """
     Given a string and a list of choices, returns the best match
 
-    closest_match("asdf", ["asd", "fds"]) --> ('asd', 1)
-    closest_match("asdf", ["asd", "fds", "asdff"], n=3) --> [('asd', 1), ('asdff', 1), ('fds', 5)]
+    closest_match("asdf", ["asd", "fds"]) --> "asd"
+    closest_match("asdf", ["asd", "fds", "asdff"], n=3) --> ["asd", "asdff", "fds"]
     """
-    qgram = QGram(2)
-    matches = {_: qgram.distance(_, s) for _ in choices}
-    matches = sorted(matches.items(), key=lambda x: x[-1])
+    matches = difflib.get_close_matches(s, choices, n=n, cutoff=cutoff)
+    if not choices or not matches:
+        return
     if n == 1:
         return matches[0]
-    return matches[:n]
+    return matches
 
 
 def match_and_exit(s, choices, msg=None, loglevel="HUGEWARNING", exitcode=2):
     """
     Return the closest match, warn, and exit
     """
     if msg is None:
         msg = ""
     else:
         msg += " "
-    closest, score = closest_match(s, choices)
+    closest = closest_match(s, choices)
     log_to_stderr(f'Could not find {msg}"{s}". Did you mean "{closest}"?', level="HUGEWARNING")
     sys.exit(2)
 
 
 def kill_children(parent_pid=None, sig=signal.SIGTERM):
     """
     Forgive me father for I have sinned
```

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/modules.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/modules.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/names_generator.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/names_generator.py`

 * *Files 1% similar despite different names*

```diff
@@ -69,15 +69,14 @@
     "enlightened",
     "esoteric",
     "ethereal",
     "euphoric",
     "evil",
     "exquisite",
     "extreme",
-    "feathery",
     "ferocious",
     "fiendish",
     "fierce",
     "fleecy",
     "flirtatious",
     "flustered",
     "foreboding",
@@ -145,14 +144,15 @@
     "nefarious",
     "negligent",
     "neurotic",
     "nihilistic",
     "normal",
     "overattached",
     "overcompensating",
+    "overenthusiastic",
     "overmedicated",
     "overwhelming",
     "overzealous",
     "paranoid",
     "pasty",
     "pedantic",
     "pernicious",
```

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/ntlm.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/ntlm.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/punycode.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/punycode.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/queueing.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/queueing.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/regexes.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/regexes.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/threadpool.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/threadpool.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/url.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/url.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/validators.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/validators.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/web.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/web.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/core/helpers/wordcloud.py` & `bbot-1.0.5.1555rc0/bbot/core/helpers/wordcloud.py`

 * *Files 1% similar despite different names*

```diff
@@ -232,19 +232,17 @@
     def top_mutations(self, n=None):
         if n is not None:
             return dict(sorted(self.items(), key=lambda x: x[-1], reverse=True)[:n])
         else:
             return dict(self)
 
     def _add_mutation(self, mutation):
-        if not None in mutation:
+        if None not in mutation:
             return
         mutation = tuple([m for m in mutation if m != ""])
-        if not any(mutation):
-            return
         try:
             self[mutation] += 1
         except KeyError:
             self[mutation] = 1
 
     def add_word(self, word):
         pass
@@ -278,11 +276,13 @@
             before = word[:start]
             after = word[end:]
             basic_mutation = [before, None, after]
             self._add_mutation(basic_mutation)
             match_str_split = self.model.split(match_str)
             if len(match_str_split) > 1:
                 for i, s in enumerate(match_str_split):
+                    if s.isdigit():
+                        continue
                     split_before = "".join(match_str_split[:i])
                     split_after = "".join(match_str_split[i + 1 :])
                     wordninja_mutation = [before + split_before, None, split_after + after]
                     self._add_mutation(wordninja_mutation)
```

### Comparing `bbot-1.0.5.1547rc0/bbot/core/logger/logger.py` & `bbot-1.0.5.1555rc0/bbot/core/logger/logger.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/db/neo4j.py` & `bbot-1.0.5.1555rc0/bbot/db/neo4j.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/defaults.yml` & `bbot-1.0.5.1555rc0/bbot/defaults.yml`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/anubisdb.py` & `bbot-1.0.5.1555rc0/bbot/modules/anubisdb.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/azure_tenant.py` & `bbot-1.0.5.1555rc0/bbot/modules/azure_tenant.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/badsecrets.py` & `bbot-1.0.5.1555rc0/bbot/modules/badsecrets.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/base.py` & `bbot-1.0.5.1555rc0/bbot/modules/base.py`

 * *Files 2% similar despite different names*

```diff
@@ -93,14 +93,15 @@
         )
         # additional callbacks to be executed alongside self.cleanup()
         self.cleanup_callbacks = []
         self._cleanedup = False
         self._watched_events = None
 
         self._lock = threading.RLock()
+        self._running_semaphore = threading.Semaphore()
         self.event_received = threading.Condition(self._lock)
 
         # string constant
         self._custom_filter_criteria_msg = "it did not meet custom filter criteria"
 
         # track number of failures (for .request_with_fail_count())
         self._request_failures = 0
@@ -217,14 +218,18 @@
         acceptable, reason = self._event_postcheck(event)
         if not acceptable:
             if reason:
                 self.debug(f"Not accepting {event} because {reason}")
             return
         return callback(event)
 
+    def _register_running(self, callback, *args, **kwargs):
+        with self._running_semaphore:
+            return callback(*args, **kwargs)
+
     def _handle_batch(self, force=False):
         if self.batch_size <= 1:
             return
         if self.num_queued_events > 0 and (force or self.num_queued_events >= self.batch_size):
             on_finish_callback = None
             events, finish, report = self.events_waiting
             if finish:
@@ -240,14 +245,15 @@
                     continue
                 checked_events.append(e)
             if checked_events:
                 self.debug(f"Handling batch of {len(events):,} events")
                 if not self.errored:
                     self._internal_thread_pool.submit_task(
                         self.catch,
+                        self._register_running,
                         self.handle_batch,
                         *checked_events,
                         _on_finish_callback=on_finish_callback,
                     )
                 return True
         return False
 
@@ -372,21 +378,21 @@
                             self.debug(f"Event queue is in bad state")
                             return
                     except queue.Empty:
                         continue
                     self.debug(f"Got {e} from {getattr(e, 'module', e)}")
                     # if we receive the special "FINISHED" event
                     if e.type == "FINISHED":
-                        self._internal_thread_pool.submit_task(self.catch, self.finish)
+                        self._internal_thread_pool.submit_task(self.catch, self._register_running, self.finish)
                     else:
                         if self._type == "output":
-                            self.catch(self._postcheck_and_run, self.handle_event, e)
+                            self.catch(self._register_running, self._postcheck_and_run, self.handle_event, e)
                         else:
                             self._internal_thread_pool.submit_task(
-                                self.catch, self._postcheck_and_run, self.handle_event, e
+                                self.catch, self._register_running, self._postcheck_and_run, self.handle_event, e
                             )
 
         except KeyboardInterrupt:
             self.debug(f"Interrupted")
             self.scan.stop()
         except ScanCancelledError as e:
             self.verbose(f"Scan cancelled, {e}")
@@ -477,15 +483,15 @@
         return True, ""
 
     def _cleanup(self):
         if not self._cleanedup:
             self._cleanedup = True
             for callback in [self.cleanup] + self.cleanup_callbacks:
                 if callable(callback):
-                    self.catch(callback, _force=True)
+                    self.catch(self._register_running, callback, _force=True)
 
     def queue_event(self, event):
         if self.incoming_event_queue in (None, False):
             self.debug(f"Not in an acceptable state to queue event")
             return
         acceptable, reason = self._event_precheck(event)
         if not acceptable:
@@ -533,17 +539,39 @@
         if self.incoming_event_queue:
             incoming_qsize = self.incoming_event_queue.qsize()
         status = {
             "events": {"incoming": incoming_qsize, "outgoing": self.outgoing_event_queue_qsize},
             "tasks": {"main_pool": main_pool, "internal_pool": internal_pool, "total": pool_total},
             "errored": self.errored,
         }
-        status["running"] = self._is_running(status)
+        status["running"] = self.running
+        status["active"] = self._is_active(status)
         return status
 
+    @staticmethod
+    def _is_active(status):
+        if status["running"]:
+            return True
+        total = status["tasks"]["total"] + status["events"]["incoming"] + status["events"]["outgoing"]
+        return total > 0
+
+    @property
+    def active(self):
+        """
+        Indicates whether the module has data yet to be processed
+        """
+        return self._foo
+
+    @property
+    def running(self):
+        """
+        Indicates whether the module is currently processing data.
+        """
+        return self._running_semaphore._value < 1
+
     def request_with_fail_count(self, *args, **kwargs):
         r = self.helpers.request(*args, **kwargs)
         if r is None:
             self._request_failures += 1
         else:
             self._request_failures = 0
         if self._request_failures >= self.failed_request_abort_threshold:
@@ -555,31 +583,14 @@
         web_spider_depth = self.scan.config.get("web_spider_depth", 1)
         spider_distance = getattr(event, "web_spider_distance", 0)
         web_spider_distance = self.scan.config.get("web_spider_distance", 0)
         if (url_depth > web_spider_depth) or (spider_distance > web_spider_distance):
             return True
         return False
 
-    @staticmethod
-    def _is_running(module_status):
-        for pool, count in module_status["tasks"].items():
-            if count > 0:
-                return True
-        for direction, qsize in module_status["events"].items():
-            if qsize > 0:
-                return True
-        return False
-
-    @property
-    def running(self):
-        """
-        Indicates whether the module is currently processing data.
-        """
-        return self.status["running"]
-
     @property
     def config(self):
         config = self.scan.config.get("modules", {}).get(self.name, {})
         if config is None:
             config = {}
         return config
```

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/bevigil.py` & `bbot-1.0.5.1555rc0/bbot/modules/bevigil.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/binaryedge.py` & `bbot-1.0.5.1555rc0/bbot/modules/binaryedge.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/bucket_aws.py` & `bbot-1.0.5.1555rc0/bbot/modules/bucket_aws.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/bucket_azure.py` & `bbot-1.0.5.1555rc0/bbot/modules/bucket_azure.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/bucket_digitalocean.py` & `bbot-1.0.5.1555rc0/bbot/modules/bucket_digitalocean.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/bucket_firebase.py` & `bbot-1.0.5.1555rc0/bbot/modules/bucket_firebase.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/bucket_gcp.py` & `bbot-1.0.5.1555rc0/bbot/modules/bucket_gcp.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/builtwith.py` & `bbot-1.0.5.1555rc0/bbot/modules/builtwith.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/bypass403.py` & `bbot-1.0.5.1555rc0/bbot/modules/bypass403.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/c99.py` & `bbot-1.0.5.1555rc0/bbot/modules/c99.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/censys.py` & `bbot-1.0.5.1555rc0/bbot/modules/censys.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/certspotter.py` & `bbot-1.0.5.1555rc0/bbot/modules/certspotter.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/crobat.py` & `bbot-1.0.5.1555rc0/bbot/modules/crobat.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/crt.py` & `bbot-1.0.5.1555rc0/bbot/modules/crt.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/deadly/ffuf.py` & `bbot-1.0.5.1555rc0/bbot/modules/deadly/ffuf.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/deadly/nuclei.py` & `bbot-1.0.5.1555rc0/bbot/modules/deadly/nuclei.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/deadly/vhost.py` & `bbot-1.0.5.1555rc0/bbot/modules/deadly/vhost.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/dnscommonsrv.py` & `bbot-1.0.5.1555rc0/bbot/modules/dnscommonsrv.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/dnsdumpster.py` & `bbot-1.0.5.1555rc0/bbot/modules/dnsdumpster.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/dnszonetransfer.py` & `bbot-1.0.5.1555rc0/bbot/modules/dnszonetransfer.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/emailformat.py` & `bbot-1.0.5.1555rc0/bbot/modules/emailformat.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/ffuf_shortnames.py` & `bbot-1.0.5.1555rc0/bbot/modules/ffuf_shortnames.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/fingerprintx.py` & `bbot-1.0.5.1555rc0/bbot/modules/fingerprintx.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/fullhunt.py` & `bbot-1.0.5.1555rc0/bbot/modules/fullhunt.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/generic_ssrf.py` & `bbot-1.0.5.1555rc0/bbot/modules/generic_ssrf.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/github.py` & `bbot-1.0.5.1555rc0/bbot/modules/github.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/gowitness.py` & `bbot-1.0.5.1555rc0/bbot/modules/gowitness.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/hackertarget.py` & `bbot-1.0.5.1555rc0/bbot/modules/hackertarget.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/host_header.py` & `bbot-1.0.5.1555rc0/bbot/modules/host_header.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/httpx.py` & `bbot-1.0.5.1555rc0/bbot/modules/httpx.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/hunt.py` & `bbot-1.0.5.1555rc0/bbot/modules/hunt.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/hunterio.py` & `bbot-1.0.5.1555rc0/bbot/modules/hunterio.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/iis_shortnames.py` & `bbot-1.0.5.1555rc0/bbot/modules/iis_shortnames.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/internal/base.py` & `bbot-1.0.5.1555rc0/bbot/modules/internal/base.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/internal/excavate.py` & `bbot-1.0.5.1555rc0/bbot/modules/internal/excavate.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/internal/speculate.py` & `bbot-1.0.5.1555rc0/bbot/modules/internal/speculate.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/ipneighbor.py` & `bbot-1.0.5.1555rc0/bbot/modules/ipneighbor.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/ipstack.py` & `bbot-1.0.5.1555rc0/bbot/modules/ipstack.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/leakix.py` & `bbot-1.0.5.1555rc0/bbot/modules/leakix.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/masscan.py` & `bbot-1.0.5.1555rc0/bbot/modules/masscan.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/massdns.py` & `bbot-1.0.5.1555rc0/bbot/modules/massdns.py`

 * *Files 2% similar despite different names*

```diff
@@ -267,26 +267,27 @@
             # word cloud
             for mutation in self.helpers.word_cloud.mutations(subdomains, cloud=False, numbers=3, number_padding=1):
                 for delimiter in ("", ".", "-"):
                     m = delimiter.join(mutation).lower()
                     add_mutation(domain_hash, m)
 
             # special dns mutator
+            to_mutate = subdomains.union(self.helpers.word_cloud.devops_mutations)
             for subdomain in self.helpers.word_cloud.dns_mutator.mutations(
-                subdomains, max_mutations=self.max_mutations
+                to_mutate, max_mutations=self.max_mutations
             ):
                 add_mutation(domain_hash, subdomain)
 
             if mutations:
                 self.info(f"Trying {len(mutations):,} mutations against {domain} ({i+1}/{len(found)})")
                 for hostname in self.massdns(query, mutations):
                     source_event = self.get_source_event(hostname)
                     if source_event is None:
-                        self.debug(f"Could not correlate source event from: {hostname}")
-                        continue
+                        self.verbose(f"Could not correlate source event from: {hostname}")
+                        source_event = self.scan.root_event
                     self.emit_result(hostname, source_event, query)
 
     def add_found(self, event):
         if self.helpers.is_subdomain(event.data):
             subdomain, domain = event.data.split(".", 1)
             if not self.helpers.is_ptr(subdomain):
                 try:
```

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/naabu.py` & `bbot-1.0.5.1555rc0/bbot/modules/naabu.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/ntlm.py` & `bbot-1.0.5.1555rc0/bbot/modules/ntlm.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/otx.py` & `bbot-1.0.5.1555rc0/bbot/modules/otx.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/asset_inventory.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/asset_inventory.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/base.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/base.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/csv.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/csv.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/http.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/http.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/human.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/human.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/json.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/json.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/neo4j.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/neo4j.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/web_report.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/web_report.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/output/websocket.py` & `bbot-1.0.5.1555rc0/bbot/modules/output/websocket.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/paramminer_cookies.py` & `bbot-1.0.5.1555rc0/bbot/modules/paramminer_cookies.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/paramminer_getparams.py` & `bbot-1.0.5.1555rc0/bbot/modules/paramminer_getparams.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/paramminer_headers.py` & `bbot-1.0.5.1555rc0/bbot/modules/paramminer_headers.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/passivetotal.py` & `bbot-1.0.5.1555rc0/bbot/modules/passivetotal.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/pgp.py` & `bbot-1.0.5.1555rc0/bbot/modules/pgp.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/rapiddns.py` & `bbot-1.0.5.1555rc0/bbot/modules/rapiddns.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/report/affiliates.py` & `bbot-1.0.5.1555rc0/bbot/modules/report/affiliates.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/report/asn.py` & `bbot-1.0.5.1555rc0/bbot/modules/report/asn.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/riddler.py` & `bbot-1.0.5.1555rc0/bbot/modules/riddler.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/robots.py` & `bbot-1.0.5.1555rc0/bbot/modules/robots.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/secretsdb.py` & `bbot-1.0.5.1555rc0/bbot/modules/secretsdb.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/securitytrails.py` & `bbot-1.0.5.1555rc0/bbot/modules/securitytrails.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/shodan_dns.py` & `bbot-1.0.5.1555rc0/bbot/modules/shodan_dns.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/skymem.py` & `bbot-1.0.5.1555rc0/bbot/modules/skymem.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/smuggler.py` & `bbot-1.0.5.1555rc0/bbot/modules/smuggler.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/social.py` & `bbot-1.0.5.1555rc0/bbot/modules/social.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/sslcert.py` & `bbot-1.0.5.1555rc0/bbot/modules/sslcert.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/subdomain_hijack.py` & `bbot-1.0.5.1555rc0/bbot/modules/subdomain_hijack.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/telerik.py` & `bbot-1.0.5.1555rc0/bbot/modules/telerik.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/threatminer.py` & `bbot-1.0.5.1555rc0/bbot/modules/threatminer.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/url_manipulation.py` & `bbot-1.0.5.1555rc0/bbot/modules/url_manipulation.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/urlscan.py` & `bbot-1.0.5.1555rc0/bbot/modules/urlscan.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/viewdns.py` & `bbot-1.0.5.1555rc0/bbot/modules/viewdns.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/virustotal.py` & `bbot-1.0.5.1555rc0/bbot/modules/virustotal.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/wafw00f.py` & `bbot-1.0.5.1555rc0/bbot/modules/wafw00f.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/wappalyzer.py` & `bbot-1.0.5.1555rc0/bbot/modules/wappalyzer.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/wayback.py` & `bbot-1.0.5.1555rc0/bbot/modules/wayback.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/modules/zoomeye.py` & `bbot-1.0.5.1555rc0/bbot/modules/zoomeye.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/scanner/manager.py` & `bbot-1.0.5.1555rc0/bbot/scanner/manager.py`

 * *Files 2% similar despite different names*

```diff
@@ -234,15 +234,15 @@
 
             ### Emit DNS children ###
             emit_children = -1 < event.scope_distance < self.scan.dns_search_distance
             # speculate DNS_NAMES and IP_ADDRESSes from other event types
             source_event = event
             if (
                 event.host
-                and event.type not in ("DNS_NAME", "IP_ADDRESS", "IP_RANGE")
+                and event.type not in ("DNS_NAME", "DNS_NAME_UNRESOLVED", "IP_ADDRESS", "IP_RANGE")
                 and not str(event.module) == "speculate"
             ):
                 source_module = self.scan.helpers._make_dummy_module("host", _type="internal")
                 source_module._priority = 4
                 source_event = self.scan.make_event(event.host, "DNS_NAME", module=source_module, source=event)
                 # only emit the event if it's not already in the parent chain
                 if source_event is not None and source_event not in source_event.get_sources():
@@ -428,15 +428,15 @@
 
         except Exception:
             log.critical(traceback.format_exc())
 
         finally:
             # Run .report() on every module
             for mod in self.scan.modules.values():
-                self.catch(mod.report, _force=True)
+                self.catch(mod._register_running, mod.report, _force=True)
 
     def log_status(self, frequency=10):
         # print status every 10 seconds
         timedelta_secs = timedelta(seconds=frequency)
         now = datetime.now()
         time_since_last_log = now - self.last_log_time
         if time_since_last_log > timedelta_secs:
@@ -457,15 +457,15 @@
 
             for num_tasks in status["scan"]["queued_tasks"].values():
                 if num_tasks > 0:
                     finished = False
 
             for m in self.scan.modules.values():
                 mod_status = m.status
-                if mod_status["running"]:
+                if mod_status["active"]:
                     finished = False
                 status["modules"][m.name] = mod_status
 
             for mod in self.scan.modules.values():
                 if mod.errored and mod.incoming_event_queue not in [None, False]:
                     with suppress(Exception):
                         mod.set_error_state()
@@ -479,26 +479,27 @@
         status["finished"] = finished
 
         modules_errored = [m for m, s in status["modules"].items() if s["errored"]]
 
         if _log:
             modules_status = []
             for m, s in status["modules"].items():
+                running = s["running"]
                 incoming = s["events"]["incoming"]
                 outgoing = s["events"]["outgoing"]
                 tasks = s["tasks"]["total"]
                 total = sum([incoming, outgoing, tasks])
-                modules_status.append((m, incoming, outgoing, tasks, total))
+                if running or total > 0:
+                    modules_status.append((m, running, incoming, outgoing, tasks, total))
             modules_status.sort(key=lambda x: x[-1], reverse=True)
 
-            modules_status = [s for s in modules_status if s[-2] or s[-1] > 0][:5]
             if modules_status:
-                modules_status_str = ", ".join([f"{m}({i:,}:{t:,}:{o:,})" for m, i, o, t, _ in modules_status])
-                running_modules_str = ", ".join([m[0] for m in modules_status])
-                self.scan.info(f"{self.scan.name}: Running modules: {running_modules_str}")
+                modules_status_str = ", ".join([f"{m}({i:,}:{t:,}:{o:,})" for m, r, i, o, t, _ in modules_status])
+                running_modules_str = ", ".join([m[0] for m in modules_status if m[1]])
+                self.scan.info(f"{self.scan.name}: Modules running: {running_modules_str}")
                 self.scan.verbose(
                     f"{self.scan.name}: Modules status (incoming:processing:outgoing) {modules_status_str}"
                 )
             event_type_summary = sorted(
                 self.scan.stats.events_emitted_by_type.items(), key=lambda x: x[-1], reverse=True
             )
             if event_type_summary:
```

### Comparing `bbot-1.0.5.1547rc0/bbot/scanner/scanner.py` & `bbot-1.0.5.1555rc0/bbot/scanner/scanner.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/scanner/stats.py` & `bbot-1.0.5.1555rc0/bbot/scanner/stats.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/scanner/target.py` & `bbot-1.0.5.1555rc0/bbot/scanner/target.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/bbot_fixtures.py` & `bbot-1.0.5.1555rc0/bbot/test/bbot_fixtures.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/conftest.py` & `bbot-1.0.5.1555rc0/bbot/test/conftest.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/helpers.py` & `bbot-1.0.5.1555rc0/bbot/test/helpers.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/modules_test_classes.py` & `bbot-1.0.5.1555rc0/bbot/test/modules_test_classes.py`

 * *Files 0% similar despite different names*

```diff
@@ -340,17 +340,16 @@
                 == "Known Secret Found. Secret Type: [HMAC/RSA Key] Secret: [1234] Product Type: [JSON Web Token (JWT)] Product: [eyJhbGciOiJIUzI1NiJ9.eyJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkJhZFNlY3JldHMiLCJleHAiOjE1OTMxMzM0ODMsImlhdCI6MTQ2NjkwMzA4M30.ovqRikAo_0kKJ0GVrAwQlezymxrLGjcEiW_s3UJMMCo] Detecting Module: [Generic_JWT]"
             ):
                 CookieBasedDetection = True
 
             if (
                 e.type == "VULNERABILITY"
                 and e.data["description"]
-                == "Known Secret Found. Secret Type: [Express SESSION_SECRET] Secret: [keyboard cat] Product Type: [Express Signed Cookie] Product: [s%3A8FnPwdeM9kdGTZlWvdaVtQ0S1BCOhY5G.qys7H2oGSLLdRsEq7sqh7btOohHsaRKqyjV4LiVnBvc] Detecting Module: [ExpressSignedCookies]"
+                == "Known Secret Found. Secret Type: [Express SESSION_SECRET] Secret: [keyboard cat] Product Type: [Express.js Signed Cookie] Product: [s%3A8FnPwdeM9kdGTZlWvdaVtQ0S1BCOhY5G.qys7H2oGSLLdRsEq7sqh7btOohHsaRKqyjV4LiVnBvc] Detecting Module: [ExpressSignedCookies]"
             ):
-                print(e.data["description"])
                 CookieBasedDetection_2 = True
 
         if SecretFound and IdentifyOnly and CookieBasedDetection and CookieBasedDetection_2:
             return True
         return False
```

### Comparing `bbot-1.0.5.1547rc0/bbot/test/run_tests.sh` & `bbot-1.0.5.1555rc0/bbot/test/run_tests.sh`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test.conf` & `bbot-1.0.5.1555rc0/bbot/test/test.conf`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_1/test_before_patching.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_1/test_before_patching.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_1/test_modules_full.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_1/test_modules_full.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_agent.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_agent.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_cli.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_cli.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_cloud_helpers.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_cloud_helpers.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_depsinstaller.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_depsinstaller.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_events.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_events.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_helpers.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -123,23 +123,20 @@
     assert "black" in extracted_words
     # assert "blacklantern" in extracted_words
     # assert "lanternsecurity" in extracted_words
     # assert "blacklanternsecurity" in extracted_words
     assert "bls" in extracted_words
 
     choices = ["asdf.fdsa", "asdf.1234", "4321.5678"]
-    best_match, score = helpers.closest_match("asdf.123a", choices)
+    best_match = helpers.closest_match("asdf.123a", choices)
     assert best_match == "asdf.1234"
     best_matches = helpers.closest_match("asdf.123a", choices, n=2)
     assert len(best_matches) == 2
-    first_match = best_matches[0]
-    assert len(first_match) == 2
-    assert first_match[0] == "asdf.1234"
-    second_match = best_matches[1]
-    assert second_match[0] == "asdf.fdsa"
+    assert best_matches[0] == "asdf.1234"
+    assert best_matches[1] == "asdf.fdsa"
 
     ipv4_netloc = helpers.make_netloc("192.168.1.1", 80)
     assert ipv4_netloc == "192.168.1.1:80"
     ipv6_netloc = helpers.make_netloc("dead::beef", "443")
     assert ipv6_netloc == "[dead::beef]:443"
 
     assert helpers.get_file_extension("https://evilcorp.com/evilcorp.com/test/asdf.TXT") == "txt"
@@ -687,31 +684,42 @@
     assert word_cloud["rumbus"] == 1
 
     # mutators
     from bbot.core.helpers.wordcloud import DNSMutator
 
     m = DNSMutator()
     m.add_word("blacklantern-security")
+    m.add_word("sec")
+    m.add_word("sec2")
+    m.add_word("black2")
     mutations = sorted(m.mutations("whitebasket"))
     assert mutations == sorted(
         [
+            "basket",
             "basket-security",
+            "basket2",
             "basketlantern-security",
             "blackbasket-security",
             "blacklantern-basket",
             "blacklantern-white",
             "blacklantern-whitebasket",
             "blackwhite-security",
             "blackwhitebasket-security",
+            "white",
             "white-security",
+            "white2",
+            "whitebasket",
             "whitebasket-security",
+            "whitebasket2",
             "whitebasketlantern-security",
             "whitelantern-security",
         ]
     )
+    top_mutations = sorted(m.top_mutations().items(), key=lambda x: x[-1], reverse=True)
+    assert top_mutations[:2] == [((None,), 3), ((None, "2"), 2)]
 
 
 def test_queues(scan, helpers):
     from bbot.core.helpers.queueing import EventQueue
 
     module_priority_1 = helpers._make_dummy_module("one")
     module_priority_2 = helpers._make_dummy_module("two")
```

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_manager.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_manager.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_modules_basic.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_modules_basic.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_python_api.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_python_api.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_scan.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_scan.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_scope.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_scope.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_target.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_target.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/test/test_step_2/test_threadpool.py` & `bbot-1.0.5.1555rc0/bbot/test/test_step_2/test_threadpool.py`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/wordlists/ffuf_shortname_candidates.txt` & `bbot-1.0.5.1555rc0/bbot/wordlists/ffuf_shortname_candidates.txt`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/wordlists/nameservers.txt` & `bbot-1.0.5.1555rc0/bbot/wordlists/nameservers.txt`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/wordlists/raft-small-extensions-lowercase_CLEANED.txt` & `bbot-1.0.5.1555rc0/bbot/wordlists/raft-small-extensions-lowercase_CLEANED.txt`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/bbot/wordlists/wordninja_dns.txt.gz` & `bbot-1.0.5.1555rc0/bbot/wordlists/wordninja_dns.txt.gz`

 * *Files identical despite different names*

### Comparing `bbot-1.0.5.1547rc0/pyproject.toml` & `bbot-1.0.5.1555rc0/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "bbot"
-version = "v1.0.5.1547rc"
+version = "v1.0.5.1555rc"
 description = "OSINT automation for hackers."
 authors = ["TheTechromancer"]
 license = "GPL-3.0"
 readme = "README.md"
 repository = "https://github.com/blacklanternsecurity/bbot"
 homepage = "https://github.com/blacklanternsecurity/bbot"
 
@@ -23,17 +23,16 @@
 ansible-runner = "^2.3.2"
 deepdiff = "^6.2.3"
 xmltojson = "^2.0.2"
 pycryptodome = "^3.17"
 idna = "^3.4"
 ansible = "^7.3.0"
 websocket-client = "^1.5.1"
-cloudcheck = "^2.0.0.23"
 tabulate = "0.8.10"
-strsimpy = "^0.2.1"
+cloudcheck = "^2.0.0.34"
 
 [tool.poetry.group.dev.dependencies]
 pytest = "^7.2.2"
 flake8 = "^6.0.0"
 black = "^23.1.0"
 pytest-cov = "^4.0.0"
 requests-mock = "^1.10.0"
```

### Comparing `bbot-1.0.5.1547rc0/PKG-INFO` & `bbot-1.0.5.1555rc0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,32 +1,31 @@
 Metadata-Version: 2.1
 Name: bbot
-Version: 1.0.5.1547rc0
+Version: 1.0.5.1555rc0
 Summary: OSINT automation for hackers.
 Home-page: https://github.com/blacklanternsecurity/bbot
 License: GPL-3.0
 Author: TheTechromancer
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: ansible (>=7.3.0,<8.0.0)
 Requires-Dist: ansible-runner (>=2.3.2,<3.0.0)
-Requires-Dist: cloudcheck (>=2.0.0.23,<3.0.0.0)
+Requires-Dist: cloudcheck (>=2.0.0.34,<3.0.0.0)
 Requires-Dist: deepdiff (>=6.2.3,<7.0.0)
 Requires-Dist: dnspython (>=2.3.0,<3.0.0)
 Requires-Dist: idna (>=3.4,<4.0)
 Requires-Dist: omegaconf (>=2.3.0,<3.0.0)
 Requires-Dist: psutil (>=5.9.4,<6.0.0)
 Requires-Dist: pycryptodome (>=3.17,<4.0)
 Requires-Dist: pydantic (>=1.10.6,<2.0.0)
 Requires-Dist: requests (>=2.28.2,<3.0.0)
-Requires-Dist: strsimpy (>=0.2.1,<0.3.0)
 Requires-Dist: tabulate (==0.8.10)
 Requires-Dist: tldextract (>=3.4.0,<4.0.0)
 Requires-Dist: websocket-client (>=1.5.1,<2.0.0)
 Requires-Dist: wordninja (>=2.0.0,<3.0.0)
 Requires-Dist: xmltojson (>=2.0.2,<3.0.0)
 Project-URL: Repository, https://github.com/blacklanternsecurity/bbot
 Description-Content-Type: text/markdown
@@ -60,15 +59,15 @@
 
 # bleeding edge (dev branch)
 pip install --pre bbot
 
 bbot --help
 ~~~
 Prerequisites:
-- Linux (Windows, including WSL is not supported)
+- Linux (Windows and macOS are *not* supported)
 - Python 3.9 or newer
 
 ## Installation ([Docker](https://hub.docker.com/r/blacklanternsecurity/bbot))
 ~~~bash
 # bleeding edge (dev)
 docker run -it blacklanternsecurity/bbot --help
 
@@ -139,15 +138,15 @@
 Visit the wiki for more [tips and tricks](https://github.com/blacklanternsecurity/bbot/wiki#tips-and-tricks).
 
 ## Using BBOT as a Python library
 ~~~python
 from bbot.scanner import Scanner
 
 # any number of targets can be specified
-scan = Scanner("evilcorp.com", "1.2.3.0/24", modules=["httpx", "sslcert"])
+scan = Scanner("evilcorp.com", "evilcorp.co.uk", modules=["httpx", "sslcert"])
 for event in scan.start():
     print(event.json())
 ~~~
 
 # Output
 By default, BBOT saves its output in TXT, JSON, and CSV formats. To enable more output modules, you can use `--output-module`.
 ~~~bash
```

